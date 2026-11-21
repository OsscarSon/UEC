const {chromium}=require('playwright');
const assert=require('node:assert/strict'),fs=require('node:fs');
const root=process.env.UEC_TEST_BASE||'http://localhost:8042/';
const out='reports/navigation';fs.mkdirSync(out+'/screenshots',{recursive:true});
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const page=await browser.newPage({viewport:{width:1440,height:1000},timezoneId:'Asia/Kuala_Lumpur',reducedMotion:'reduce'});
 const go=async view=>{await page.goto(root+(view==='today'?'#dashboard':'#view='+view));await page.waitForFunction(v=>tab===v,view);};
 const errors=[],bad=[],cases=[];page.on('pageerror',e=>errors.push(e.message));
 page.on('response',r=>{if(r.url().startsWith(root)&&r.status()>=400)bad.push(r.url());});
 await page.goto(root);
 await page.evaluate(()=>{S.learn['物理3']='2026-11-01';S.mathSubjects.adv_math_i.study_minutes=17;S.mathSubjects.adv_math_ii.study_minutes=41;S.mathSubjects.adv_math_i.chapters['2']={mastery:2};S.mathSubjects.adv_math_ii.chapters['2']={mastery:1};save();});
 const expected=['today','map','bank','review','records','exams','tools','favorites','settings'];
 const destinations=[['today','today'],['adaptive','today'],['plan','today'],['map','map'],['curriculum','map'],['bank','bank'],['mock','bank'],['review','review'],['diagnose','review'],['err','review'],['records','records'],['exams','exams'],['cal','exams'],['textbooks','exams'],['past-papers','exams'],['tools','tools'],['favorites','favorites'],['settings','settings'],['sync','settings']];
 for(const width of [320,390,1440,1920]){
  await page.setViewportSize({width,height:1000});
  for(const [view,parent]of destinations){
   await go(view);
   await page.locator('#n .nav-item').first().waitFor();
   assert.deepEqual(await page.locator('#n .nav-item').evaluateAll(ns=>ns.map(n=>n.dataset.tab)),expected);
   assert.equal(await page.locator('#n .nav-item[aria-current="page"]').getAttribute('data-tab'),parent);
   assert.equal(await page.locator('#n .nav-item.active').count(),1);
   if(!['today','records','tools','favorites'].includes(view)){
    assert.equal(await page.locator('.workspace-tabs').count(),1);
    assert.ok(['static','relative'].includes(await page.locator('.workspace-tabs').evaluate(n=>getComputedStyle(n).position)));
    assert.ok(await page.locator('.workspace-tabs').evaluate(n=>n.getBoundingClientRect().left>=document.getElementById('v').getBoundingClientRect().left));
    assert.equal(await page.locator('.workspace-tabs [aria-current="page"]').getAttribute('href'),'#view='+view);
   }
   assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),view+' '+width);
   cases.push({view,parent,width});
  }
 }
 await page.setViewportSize({width:1440,height:1000});
 await go('settings');
 await page.getByRole('navigation',{name:'设置与备份内导航'}).getByRole('link',{name:'账号与云同步'}).click();
 assert.ok(await page.getByRole('heading',{name:'账号与云同步',exact:true}).isVisible());
 assert.ok(await page.getByRole('button',{name:'使用 Google 登录'}).isDisabled());
 await page.screenshot({path:out+'/screenshots/settings-cloud-desktop.png'});
 await page.goBack();
 assert.ok(await page.getByRole('heading',{name:'设置与备份',exact:true}).isVisible());
 await page.reload();assert.ok(await page.getByLabel('导入备份',{exact:false}).count());
 await page.locator('#n [data-tab="bank"]').click();
 await page.getByRole('navigation',{name:'题库练习内导航'}).getByRole('link',{name:'限时模拟'}).click();
 await page.locator('#mock-form').waitFor({state:'visible'});
 await page.screenshot({path:out+'/screenshots/practice-desktop.png'});
 await page.locator('#n [data-tab="review"]').click();
 await page.getByRole('navigation',{name:'智能复习内导航'}).getByRole('link',{name:'前置诊断'}).click();
 await page.locator('#diagnostic-form').waitFor({state:'visible'});
 await page.getByRole('navigation',{name:'智能复习内导航'}).getByRole('link',{name:'错题本'}).click();
 await page.getByRole('heading',{name:'错题本',exact:true}).waitFor({state:'visible'});
 await page.locator('#n [data-tab="map"]').click();
 await page.getByRole('navigation',{name:'课程笔记内导航'}).getByRole('link',{name:'课程地图'}).click();
 await page.locator('tbody tr').first().waitFor();
 assert.equal(await page.locator('tbody tr').count(),145);
 await go('today');
 await page.getByRole('link',{name:'根据诊断、失分和个人课表生成今日建议 →'}).click();
 await page.locator('#profile-form').waitFor({state:'visible'});
 await page.screenshot({path:out+'/screenshots/plan-desktop.png'});
 await go('today');await page.screenshot({path:out+'/screenshots/dashboard-desktop.png'});
 await page.setViewportSize({width:390,height:844});await go('sync');
 await page.screenshot({path:out+'/screenshots/settings-cloud-mobile.png'});
 await page.getByRole('button',{name:'打开导航',exact:true}).click();
 assert.ok(await page.locator('body').evaluate(n=>n.classList.contains('menu-open')));
 await page.screenshot({path:out+'/screenshots/sidebar-mobile.png'});
 await page.locator('#n [data-tab="review"]').click();
 assert.ok(!await page.locator('body').evaluate(n=>n.classList.contains('menu-open')));
 await page.getByRole('navigation',{name:'智能复习内导航'}).getByRole('link',{name:'前置诊断'}).click();
 await page.locator('#diagnostic-form').waitFor({state:'visible'});
 await page.screenshot({path:out+'/screenshots/review-mobile.png'});
 await page.evaluate(()=>{S.dashboard.preferences.theme='dark';save();render();});
 assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
 await page.screenshot({path:out+'/screenshots/review-mobile-dark.png'});
 const kept=await page.evaluate(()=>({learned:S.learn['物理3'],i:S.mathSubjects.adv_math_i.study_minutes,ii:S.mathSubjects.adv_math_ii.study_minutes,mi:S.mathSubjects.adv_math_i.chapters['2'].mastery,mii:S.mathSubjects.adv_math_ii.chapters['2'].mastery}));
 assert.deepEqual(kept,{learned:'2026-11-01',i:17,ii:41,mi:2,mii:1});assert.deepEqual(errors,[]);assert.deepEqual(bad,[]);
 fs.writeFileSync(out+'/TEST_RESULTS.json',JSON.stringify({status:'pass',primary_items:9,previous_primary_items:16,viewport_route_cases:cases,checks:['all secondary destinations retain a highlighted parent','settings contains disabled cloud controls and local backup','practice contains timed mock','review contains diagnosis and error book','course map retains145 entries over116 chapters','home opens adaptive plan','deep links reload and browser back work','mobile drawer closes on navigation','dark and light secondary navigation fits viewport','original learning and independent math records preserved'],page_errors:errors,resource_errors:bad},null,2)+'\n');
 await browser.close();console.log(`PASS ${cases.length} navigation/viewport cases, grouped workflows and preserved records`);
})().catch(e=>{console.error(e);process.exit(1)});
