const {delimiter} = require('node:path');
const assert = require('node:assert/strict');
const {chromium} = require('playwright');
const base = process.env.UEC_TEST_BASE || 'http://127.0.0.1:8052/';
const privateArchives = process.env.UEC_PAPER_ZIP?.split(delimiter);
const photo = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jY1sAAAAASUVORK5CYII=', 'base64');

(async () => {
  const browser = await chromium.launch({executablePath: '/usr/bin/chromium', args: ['--no-sandbox']});
  try {
    const page = await browser.newPage({viewport: {width: 1440, height: 960}, timezoneId: 'Asia/Kuala_Lumpur'});
    const errors = [], missing = [], requested = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('request', r => requested.push(r.url()));
    page.on('response', r => { if (r.url().startsWith(base) && r.status() >= 400) missing.push(r.url()); });
    await page.goto(base + '#view=exams');
    const tabs = page.getByRole('navigation', {name: '考试资料内导航'});
    assert.deepEqual(await tabs.getByRole('link').allTextContents(), ['考试资料','考试日历','课本资料','历届考试资料']);
    assert.ok(!requested.some(url => url.includes('vendor/source-tools/')), 'UI vendor bundles load lazily');
    await tabs.getByRole('link', {name: '课本资料', exact: true}).click();
    await page.locator('.workspace-tab-indicator').waitFor({state:'attached'});
    await page.locator('.workspace-tab-indicator').waitFor({state:'detached'});
    const importForm = page.locator('[data-source-import]');
    await importForm.getByRole('combobox').selectOption('physics');
    await importForm.getByPlaceholder('例如 高一上册').fill('高一上册');
    // Two distinct images allow deduplication and natural photo ordering to be tested independently.
    await importForm.locator('[type=file]').setInputFiles([
      {name: 'page10.png', mimeType: 'image/png', buffer: Buffer.concat([photo, Buffer.from([0])])},
      {name: 'page2.png', mimeType: 'image/png', buffer: photo},
    ]);
    await importForm.getByRole('button', {name: '保存到本机'}).click();
    await page.locator('[data-source-storage]').getByText('本机 2 份课本文件').waitFor();
    await page.locator('[data-sonner-toast]').getByText('已保存 2 份。').waitFor();
    assert.deepEqual(await page.locator('.source-list b').allTextContents(), ['page2.png','page10.png']);
    await page.locator('.source-list').getByRole('button', {name:'阅读'}).first().click();
    const viewer = page.getByRole('dialog');
    await viewer.getByRole('img').waitFor();
    assert.equal(await viewer.getByRole('img').evaluate(img => img.decode().then(() => img.naturalWidth)), 1);
    await viewer.getByRole('button', {name: '下一张'}).click();
    await viewer.getByRole('img', {name:'page10.png'}).waitFor();
    await page.keyboard.press('Escape');
    await page.reload();
    await page.locator('[data-source-storage]').getByText('本机 2 份课本文件').waitFor();
    await tabs.getByRole('link', {name: '历届考试资料'}).click();
    await page.locator('[data-source-storage]').getByText(/47 份目录/).waitFor();
    await page.locator('[data-source-filter=type]').selectOption('uec_math_i');
    await page.locator('[data-source-filter=year]').selectOption('2026');
    assert.ok(await page.locator('.source-list li').count() > 0);
    const target = 'uec_math_i:4a3947f81fa6';
    await page.goto(base + '#view=past-papers&source=' + encodeURIComponent(target) + '&page=5');
    assert.equal(await page.locator('.source-list li').count(), 1);
    await page.getByRole('button', {name:'来源',exact:true}).click();
    assert.ok((await viewer.innerText()).includes(target));
    await page.keyboard.press('Escape');
    if (privateArchives) {
      await page.getByRole('button', {name:'导入原卷',exact:true}).click();
      await importForm.locator('[type=file]').setInputFiles(privateArchives);
      await importForm.getByRole('button', {name:'保存到本机'}).click();
      await page.locator('[data-source-storage]').getByText(/本机已匹配 47 份/).waitFor({timeout:60000});
      await page.getByRole('button', {name:'阅读原卷'}).click();
      const pdf = viewer.locator('iframe');
      await pdf.waitFor();
      assert.match(await pdf.getAttribute('src'), /^blob:.*#page=5$/);
      const bytes = await page.evaluate(async () => {
        const src = document.querySelector('#source-preview iframe').src;
        return (await (await fetch(src.split('#')[0])).blob()).size;
      });
      assert.equal(bytes, await page.evaluate(id => MATH_EXAM_RESEARCH.inventory.find(x => x.source_id === id).bytes, target));
      await page.getByRole('button', {name:'关闭',exact:true}).click();
      await page.reload();
      await page.locator('[data-source-storage]').getByText(/本机已匹配 47 份/).waitFor();
    }
    await page.locator('#global-search').fill('物质的亮');
    await page.locator('#global-search').press('Enter');
    await page.locator('.search-result').filter({hasText:'物质的量'}).first().waitFor();
    await page.locator('#page-search').fill('３．６');
    await page.locator('#page-search').press('Enter');
    assert.ok((await page.locator('.search-result b').allTextContents()).every(title => title.startsWith('3.6 ')));
    await page.emulateMedia({reducedMotion:'reduce', colorScheme:'dark'});
    for (const width of [320,390,1440]) {
      await page.setViewportSize({width,height:900});
      for (const view of ['exams','cal','textbooks','past-papers']) {
        await page.goto(base + '#view=' + view);
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), `${view} ${width}px`);
        assert.equal(await tabs.locator('[aria-current="page"]').getAttribute('href'), '#view=' + view);
        assert.equal(await page.locator('.workspace-tab-indicator').count(),0);
      }
    }
    assert.deepEqual(errors, []);
    assert.deepEqual(missing, []);
    console.log('PASS source navigation, photo reading, persistence, Fuse typo and numeric search, Sonner, Motion, PDF trace and responsive layouts.' + (privateArchives ? ' All 47 original PDFs imported and matched.' : ' Private original ZIP not supplied to test.'));
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
