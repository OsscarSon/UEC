const {chromium}=require('playwright'),assert=require('node:assert/strict'),fs=require('node:fs');
(async()=>{
 const b=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']}),p=await b.newPage({viewport:{width:390,height:844}}),errors=[];
 p.on('pageerror',e=>errors.push(e.stack));const root=process.env.UEC_TEST_BASE||'http://localhost:8000/';
 await p.goto(root+'#lesson='+encodeURIComponent('物理3')+'&section=3.3');
 let unit=p.locator('[id="unit-物理3-3.3"]');assert.ok((await unit.locator('[data-module="4"]').textContent()).includes('|Δx|'));assert.ok((await unit.locator('[data-module="5"]').textContent()).includes('Σ|x_i−x_(i−1)|'));
 const goal=unit.locator('[data-module="12"] article').first();await goal.getByRole('button',{name:'此目标需复习',exact:true}).click();assert.equal(await goal.getByRole('button',{name:'此目标需复习 ✓'}).getAttribute('aria-pressed'),'true');assert.ok(await goal.locator('details').last().getAttribute('open')!==null);
 await p.reload();unit=p.locator('[id="unit-物理3-3.3"]');assert.equal(await unit.getByRole('button',{name:'此目标需复习 ✓'}).count(),1);
 await unit.getByRole('button',{name:'此目标能解释',exact:true}).first().click();await p.reload();assert.equal(await p.locator('[id="unit-物理3-3.3"]').getByRole('button',{name:'此目标能解释 ✓'}).count(),1);
 await p.getByRole('button',{name:'考试日历',exact:true}).click();
 const dlPromise=p.waitForEvent('download');await p.getByRole('button',{name:'导出进度',exact:true}).click();const dl=await dlPromise,stream=await dl.createReadStream();let backup='';for await(const part of stream)backup+=part.toString();const saved=JSON.parse(backup);assert.equal(saved.goalChecks['物理3:3.3:goal0'],'ready');
 await p.evaluate(()=>{S.goalChecks={};save()});await p.locator('#imp').setInputFiles({name:'goal-backup.json',mimeType:'application/json',buffer:Buffer.from(backup)});await p.waitForFunction(()=>JSON.parse(localStorage.getItem('uec27')).goalChecks['物理3:3.3:goal0']==='ready');
 const seen=[];
 for(const key of ['物理3','化学4','生物2']){
  await p.goto(root+'#lesson='+encodeURIComponent(key));const approved=p.locator(key==='物理3'?'[data-illustration-id="P01"] img':'figure img[src*="illustrations/incoming/batch01/"]');assert.equal(await approved.count(),1);seen.push(await approved.getAttribute('src'));
  await approved.scrollIntoViewIfNeeded();await approved.evaluate(i=>{i.loading='eager';return i.decode()});const trigger=approved.locator('..');await trigger.focus();await p.keyboard.press('Enter');const d=p.locator('#figure-viewer');assert.ok(await d.isVisible());assert.ok(await d.locator('img').evaluate(i=>i.decode().then(()=>i.naturalWidth>0)));
  assert.ok(await d.locator('.viewer-scroll').evaluate(e=>e.scrollWidth>e.clientWidth));assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));await p.keyboard.press('Escape');assert.equal(await d.isVisible(),false);assert.ok(await trigger.evaluate(e=>e===document.activeElement));
 }
 for(const width of [320,390,1280]){await p.setViewportSize({width,height:900});for(const key of ['化学5','化学6','生物3']){
  await p.goto(root+'#lesson='+encodeURIComponent(key));await p.locator('figure img').evaluateAll(xs=>Promise.all(xs.map(x=>{x.loading='eager';return x.decode()})));assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));assert.equal(await p.locator('[data-module="7"] .strategy').count(),await p.locator('.lesson-section').count());assert.equal(await p.locator('[data-module="12"] .goal-diagnostics').count(),await p.locator('.lesson-section').count());
  const imgs=await p.locator('figure img').evaluateAll(xs=>xs.map(x=>x.getAttribute('src')));assert.ok(!imgs.some(x=>['c5_1a.svg','c5_4c.svg','b3_4.svg','b3_6b.svg','b3_6c.svg'].some(name=>x.endsWith(name))));
 }}
 await p.goto(root+'#lesson='+encodeURIComponent('化学6'));assert.equal(await p.locator('.lesson-section').count(),6);assert.ok((await p.locator('[data-module="6"]').first().textContent()).includes('已知条件'));assert.ok((await p.locator('[data-module="6"]').first().textContent()).includes('验算/证据检查'));
 await p.goto(root+'#lesson='+encodeURIComponent('化学3')+'&section=3.6');assert.ok((await p.locator('[id="unit-化学3-3.6-m12"]').textContent()).includes('6.02214076'));
 // Keep review screenshots synchronized with the tested content, including the final IE exception explanation.
 fs.mkdirSync('reports/batch02/screenshots',{recursive:true});
 for(const width of [390,1280]){
  await p.setViewportSize({width,height:900});await p.goto(root+'#lesson='+encodeURIComponent('化学6')+'&section=6.3.3');
  const strategy=p.locator('[id="unit-化学6-6.3.3-m7"]');assert.ok((await strategy.textContent()).includes('Mg⁺价层为3s¹'));
  await strategy.screenshot({path:`reports/batch02/screenshots/strategy-${width}.png`});
 }
 await p.setViewportSize({width:390,height:844});await p.goto(root+'#lesson='+encodeURIComponent('物理3'));
 const preview=p.locator('[data-illustration-id="P01"] img');await preview.scrollIntoViewIfNeeded();await preview.evaluate(i=>{i.loading='eager';return i.decode()});await preview.locator('..').click();
 await p.locator('#figure-viewer img').evaluate(i=>i.decode());await p.screenshot({path:'reports/batch02/screenshots/zoom-mobile.png'});await p.keyboard.press('Escape');
 assert.deepEqual(errors,[]);
 // New SVG text and numeric geometries: bounds, energy positions, curve endpoint/peak numbers.
 const clips=[];for(const name of fs.readdirSync('assets/verified')){
  await p.setContent(fs.readFileSync('assets/verified/'+name,'utf8'));await p.evaluate(()=>document.fonts.ready);
  const bad=await p.evaluate(()=>{const s=document.querySelector('svg'),v=s.viewBox.baseVal;return [...s.querySelectorAll('text')].flatMap(t=>{const r=t.getBBox();return r.x<0||r.y<0||r.x+r.width>v.width+1||r.y+r.height>v.height+1?[t.textContent]:[]})});if(bad.length)clips.push({name,bad});
 }
 assert.deepEqual(clips,[]);
 const out={result:'pass',checks:['四处绝对值公式DOM','目标对应题/反馈结构（全量静态检查另列）','目标自评与回读状态刷新保存','新增目标状态导出/清空/导入往返','3幅现用代表图可加载（P01 SVG及2张保留PNG）','键盘Enter打开放大与Esc关闭/焦点回归','手机放大区滚动且整页不溢出','3视窗×新增模块3章无溢出','已隔离P0旧图不进入教学DOM','新题八步说明可见','现代SI检测题可见','11幅新SVG文字边界'],approved_images_seen:seen,new_svg_text_clipping:clips,browser_errors:errors};fs.writeFileSync('reports/batch02/UI_RESULTS.json',JSON.stringify(out,null,2)+'\n');console.log('PASS batch02 image viewer, diagnostics, quarantine, 9 extra viewport/chapter cases and 11 SVG bounds');await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
