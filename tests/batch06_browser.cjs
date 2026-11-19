const {chromium}=require('playwright'),assert=require('node:assert/strict'),fs=require('node:fs');
const root=process.env.UEC_TEST_BASE||'http://localhost:8043/',out='reports/batch06';
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce',timezoneId:'Asia/Kuala_Lumpur'});
 const errors=[],bad=[],cases=[];page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.url().startsWith(root)&&r.status()>=400)bad.push([r.status(),r.url()]);});
 await page.goto(root);const keys=await page.evaluate(()=>Object.keys(BATCH_NOTES).filter(k=>Object.values(BATCH_NOTES[k])[0]?.content_batch==='batch06'));
 const courses=keys.flatMap(key=>key.startsWith('数学')?(Number(key.slice(2))<=29?[['adv_math_i',key],['adv_math_ii',key]]:[['adv_math_ii',key]]):[[null,key]]);
 for(const width of [390,1440]){await page.setViewportSize({width,height:1000});for(const [course,key]of courses){
  const url=course?'#subject='+course+'&chapter='+key.slice(2):'#lesson='+encodeURIComponent(key);
  await page.goto(root+url);await page.locator('.lesson-section').first().waitFor();
  const expected=await page.evaluate(k=>LESSONS[k].sections.length,key);
  const formulaCount=await page.evaluate(k=>LESSONS[k].sections.reduce((n,s)=>n+(STUDY_FORMULAS[k+'/'+s.id]?.length||0),0),key);
  if(formulaCount){await page.waitForFunction(n=>document.querySelectorAll('.lesson-section [data-typeset=\"true\"]').length===n,formulaCount);assert.equal(await page.locator('.katex-error').count(),0,key);}
  assert.ok(await page.locator('a[href=\"reports/batch06/SOURCES.csv\"]').count()===expected,key);
  assert.equal(await page.locator('.lesson-section').count(),expected,key);
  assert.equal(await page.locator('.note-module').count(),expected*12,key);
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),key+width);
  assert.ok(!(await page.locator('main').innerText()).includes('[object Object]'),key);
  for(const sec of await page.locator('.lesson-section').all()){
   await sec.evaluate(n=>n.open=true);
   assert.equal(await sec.locator('.note-module').count(),12);
  }
  cases.push({key,course,width,sections:expected,modules:expected*12,typeset_formulas:formulaCount});
  if(['数学6','化学21','生物14','物理14'].includes(key)&&course!=='adv_math_ii'){
   await page.evaluate(()=>scrollTo(0,0));await page.screenshot({path:out+'/'+encodeURIComponent(key)+'-'+width+'.png'});
  }
 }}
 await page.goto(root+'#subject=adv_math_i&chapter=6');await page.locator('.lesson-section').first().waitFor();
 await page.locator('[data-a="section-check"][data-v="2"]').first().click();
 assert.ok(await page.evaluate(()=>Object.keys(S.checks).some(k=>k.startsWith('adv_math_i:数学6:'))));
 assert.ok(await page.evaluate(()=>!Object.keys(S.checks).some(k=>k.startsWith('adv_math_ii:数学6:'))));
 const text=await page.locator('main').innerText();assert.ok(text.includes('|2x−1|<5')||text.includes('|2x−1|'));
 assert.deepEqual(errors,[]);assert.deepEqual(bad,[]);
 fs.writeFileSync(out+'/BROWSER_RESULTS.json',JSON.stringify({status:'pass',new_unique_chapters:keys.length,viewport_cases:cases,checks:['all new real sections have12 rendered modules','mobile and desktop no horizontal overflow','absolute-value pipes remain readable','math I/II new section self-check isolation','all local resources load','new formula cards rendered without KaTeX errors','new source links point to batch06'],page_errors:errors,resource_errors:bad,limits:'Chromium simulated viewports and explicit self-check fixture, not teacher certification.'},null,2)+'\n');
 await browser.close();console.log('PASS',keys.length,'chapters,',cases.length,'course/viewport cases and math isolation');
})().catch(e=>{console.error(e);process.exit(1)});

