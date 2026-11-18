const fs=require('fs'),assert=require('node:assert/strict'),{chromium}=require('playwright');
(async()=>{
 const reportDir=process.env.UEC_V22_REPORT_DIR||'reports/v22';
 const root=process.env.UEC_TEST_BASE||'http://localhost:8015/',a=JSON.parse(fs.readFileSync('reports/v22/ASSET_REVIEW.json'));
 const approved=a.filter(x=>x.integration_status==='integrated'),chapters=[...new Set(approved.map(x=>x.lesson_key))];
 const b=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']}),p=await b.newPage(),errors=[],badResponses=[],cases=[],zooms=[];
 p.on('pageerror',e=>errors.push(e.message));p.on('response',r=>{if(r.url().startsWith(root)&&r.status()>=400)badResponses.push([r.status(),r.url()]);});
 fs.mkdirSync(reportDir+'/screenshots',{recursive:true});
 for(const width of [320,390,1280]){
  await p.setViewportSize({width,height:900});
  for(const key of chapters){
   await p.goto(root+'#lesson='+encodeURIComponent(key));await p.locator('.lesson-section').first().waitFor();
   const expected=approved.filter(x=>x.lesson_key===key);
   assert.equal(await p.locator('[data-illustration-id]').count(),expected.length);
   assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
   for(const row of expected){
    const fig=p.locator(`[data-illustration-id="${row.code}"]`),img=fig.locator('img');
    assert.equal(await fig.locator('..').getAttribute('data-module'),String(row.module));
    assert.equal(await fig.locator('..').locator('..').getAttribute('id'),`unit-${row.lesson_key}-${row.section_id}`);
    assert.ok(!(await p.locator(`[id="unit-${row.lesson_key}-${row.section_id}-m5"]`).textContent()).includes('教学图尚待制作'));
    await img.evaluate(i=>{i.loading='eager';return i.decode()});
    assert.ok(await img.evaluate(i=>i.naturalWidth>0&&i.getBoundingClientRect().width>0));
    assert.ok(await img.evaluate(i=>i.getBoundingClientRect().right<=innerWidth+1));
    if(width===390||width===1280){
     const trigger=fig.locator('button');await trigger.scrollIntoViewIfNeeded();await trigger.focus();await p.keyboard.press('Enter');
     const d=p.locator('#figure-viewer');assert.ok(await d.isVisible());await d.locator('img').evaluate(i=>i.decode());
     assert.ok(await d.locator('img').evaluate(i=>i.getBoundingClientRect().width>=1200));
     assert.ok(await d.locator('.viewer-scroll').evaluate(e=>e.scrollWidth>e.clientWidth));
     if(width===390&&['P16','C17','B22'].includes(row.code))await p.screenshot({path:`${reportDir}/screenshots/zoom-${row.code}-390.png`});
     if(width===390&&row.code==='B22'){await d.locator('.viewer-scroll').evaluate(e=>e.scrollLeft=e.scrollWidth);await p.screenshot({path:reportDir+'/screenshots/zoom-B22-390-active.png'});}
     await p.keyboard.press('Escape');assert.equal(await d.isVisible(),false);assert.ok(await trigger.evaluate(e=>e===document.activeElement));zooms.push({width,code:row.code});
    }
   }
   const shown=await p.locator('figure img').evaluateAll(es=>es.map(e=>e.getAttribute('src')));
   const superseded=await p.evaluate(()=>Object.keys(window.V22_SUPERSEDED_FIGURES||{}));assert.ok(!shown.some(s=>superseded.includes(s)));
   assert.ok(!a.filter(x=>x.integration_status!=='integrated').some(x=>shown.includes(x.reviewed_path)||shown.includes(x.original_path)));
   assert.equal(await p.locator('[data-module]').count(),12*await p.locator('.lesson-section').count());
   cases.push({width,chapter:key,loaded_v22:expected.length,overflow:false});console.log('Checked',width,key,expected.length);
  }
 }
 // Reopen representatives in actual site context in light and dark modes.
 for(const row of approved.filter(x=>['P16','C17','B22'].includes(x.code))){
  for(const width of [390,1280]){
   await p.setViewportSize({width,height:900});await p.goto(root+'#lesson='+encodeURIComponent(row.lesson_key)+'&section='+row.section_id);
   const fig=p.locator(`[data-illustration-id="${row.code}"]`);await fig.locator('img').evaluate(i=>{i.loading='eager';return i.decode()});await fig.scrollIntoViewIfNeeded();
   await p.screenshot({path:`${reportDir}/screenshots/${row.code}-${width}-light.png`});
   await p.evaluate(()=>document.documentElement.setAttribute('data-theme','dark'));await p.screenshot({path:`${reportDir}/screenshots/${row.code}-${width}-dark.png`});
   assert.equal(await fig.locator('img').evaluate(i=>getComputedStyle(i).backgroundColor),'rgb(255, 255, 255)');
   assert.notEqual(await fig.locator('figcaption').evaluate(e=>getComputedStyle(e).color), 'rgb(0, 0, 0)');
   await p.evaluate(()=>document.documentElement.setAttribute('data-theme','light'));
  }
 }
 // Every reviewed asset including unmapped alternates is renderable, without making a teaching link.
 await p.goto(root);
 const resourceResults=await p.evaluate(async paths=>{
  const out=[];for(const path of paths){const im=new Image();im.src=path;try{await im.decode();out.push({path,loaded:im.naturalWidth>0})}catch(e){out.push({path,loaded:false})}}return out;
 },a.map(x=>x.reviewed_path||x.original_path));assert.ok(resourceResults.every(x=>x.loaded));
 assert.deepEqual(errors,[]);assert.deepEqual(badResponses,[]);
 fs.writeFileSync(reportDir+'/BROWSER_RESULTS.json',JSON.stringify({result:'pass',cases,zoom_cases:zooms.length,images_rendered:resourceResults.length,resource_results:resourceResults,errors,badResponses,screenshot_scope:`实际教学页面390/1280、浅色/深色，P16/C17/B22三科代表；全部${approved.length}图在3视窗加载，390/1280逐图放大/滚动/Esc/焦点回归。截图不是全部学科教师审定。`},null,2)+'\n');
 await b.close();console.log(`PASS V22: ${cases.length} viewport/chapter cases, ${zooms.length} zoom cases, ${resourceResults.length} resource renders`);
})().catch(e=>{console.error(e);process.exit(1)});
