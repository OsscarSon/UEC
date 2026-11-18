const fs=require('fs'),assert=require('node:assert/strict'),{chromium}=require('playwright');
(async()=>{
const root=process.env.UEC_TEST_BASE||'http://localhost:8025/',entries=JSON.parse(fs.readFileSync('data/review/batch05_sections.json'));
const chapters=[...new Set(entries.map(x=>x.subject+x.chapter_id))],errors=[],bad=[],checks=[];
const b=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']}),p=await b.newPage();
p.on('pageerror',e=>errors.push(e.message));p.on('response',r=>{if(r.url().startsWith(root)&&r.status()>=400)bad.push([r.status(),r.url()]);});
await p.goto(root);
const seed={mast:{'数学34':2,'物理3':1},learn:{'数学34':'2026-11-10'},rv:{'数学34':[1]},done:{old:true},err:[{s:'数学',c:34,q:'保留旧错题',w:'概念不懂',st:0,last:'',d:'2026-11-10'}],ex:[{n:'原考试',d:'2027-05-20',r:'原范围'}],mathSubjects:{adv_math_i:{study_note:'原I记录',study_minutes:11},adv_math_ii:{study_note:'原II记录',study_minutes:22}}};
await p.evaluate(s=>{localStorage.setItem('uec27',JSON.stringify(s))},seed);
await p.goto(root+'#subject=adv_math_i&chapter=1');await p.reload();
assert.equal(await p.locator('#subject-notes a[href*="&chapter="]').count(),29);
assert.equal(await p.getByLabel('累计学习分钟').inputValue(),'11');
await p.locator('[data-a="subject-math-learn"]').click();
await p.locator('[data-a="subject-math-mastery"][data-v="2"]').click();
await p.goto(root+'#subject=adv_math_ii&chapter=1');
assert.equal(await p.locator('#subject-notes a[href*="&chapter="]').count(),35);
assert.equal(await p.getByLabel('累计学习分钟').inputValue(),'22');
assert.equal(await p.locator('[data-a="subject-math-mastery"][data-v="0"]').getAttribute('aria-pressed'),'true');
let saved=await p.evaluate(()=>JSON.parse(localStorage.getItem('uec27')));
assert.ok(!saved.mathSubjects.adv_math_ii.chapters?.['1']?.learned_at);
for(const k of ['mast','learn','rv','done','err','ex'])assert.deepEqual(saved[k],seed[k]);
await p.locator('[data-a="subject-math-learn"]').click();await p.goto(root+'#subject=adv_math_i&chapter=1');
assert.equal(await p.locator('[data-a="subject-math-mastery"][data-v="2"]').getAttribute('aria-pressed'),'true');
await p.evaluate(()=>{S.mathSubjects.adv_math_i.chapters['1'].learned_at='2026-01-01';save();render();});
await p.locator('[data-a="subject-math-review"][data-v="1"]').click();
saved=await p.evaluate(()=>JSON.parse(localStorage.getItem('uec27')));
assert.deepEqual(saved.mathSubjects.adv_math_i.chapters['1'].rv,[1]);
assert.deepEqual(saved.mathSubjects.adv_math_ii.chapters['1'].rv,[]);
fs.mkdirSync('reports/batch05/screenshots',{recursive:true});
for(const width of [320,390,1280]){
 await p.setViewportSize({width,height:900});
 for(const key of chapters){
  const expected=entries.filter(x=>x.subject+x.chapter_id===key);
  const hash=key.startsWith('数学')?'subject=adv_math_i&chapter='+key.slice(2):'lesson='+encodeURIComponent(key);
  await p.goto(root+'#'+hash);
  assert.equal(await p.locator('.lesson-section').count(),expected.length);
  assert.equal(await p.locator('[data-module]').count(),12*expected.length);
  assert.deepEqual(await p.locator('.lesson-section > summary').allTextContents(),expected.map(x=>x.section_id+' '+x.section_title+' 12模块'));
  assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),key+' '+width);
  const imgs=p.locator('figure img');await imgs.evaluateAll(a=>Promise.all(a.map(i=>{i.loading='eager';return i.decode()})));
  checks.push({key,width,sections:expected.length,modules:12*expected.length});
  if(key===chapters[0]&&width!==320)await p.screenshot({path:'reports/batch05/screenshots/notes-'+width+'.png'});
 }
}
// Use one authored section to exercise independent answer/self-assessment storage.
const row=entries[0],key=row.subject+row.chapter_id;
await p.goto(root+'#lesson='+encodeURIComponent(key));
const unit=p.locator('.lesson-section').first();
await unit.getByRole('button',{name:'能独立解释',exact:true}).click();
await unit.getByRole('button',{name:'此目标需复习',exact:true}).first().click();
await p.reload();assert.equal(await p.getByRole('button',{name:'能独立解释 ✓',exact:true}).count(),1);
const solution=p.locator('[data-module="10"]').first().locator('details').first();await solution.locator('summary').click();assert.ok(await solution.getAttribute('open')!==null);
// Existing functions, backup/restore, and old data remain intact.
await p.locator('#n [data-k="cal"]').click();
const dl=p.waitForEvent('download');await p.getByRole('button',{name:'导出进度',exact:true}).click();
const stream=await(await dl).createReadStream();let raw='';for await(const v of stream)raw+=v.toString();
const backup=JSON.parse(raw);assert.equal(backup.mathSubjects.adv_math_i.study_note,'原I记录');assert.equal(backup.mathSubjects.adv_math_i.chapters['1'].mastery,2);
await p.evaluate(()=>{S.mathSubjects={};save();});await p.locator('#imp').setInputFiles({name:'restore.json',mimeType:'application/json',buffer:Buffer.from(raw)});
await p.waitForFunction(()=>JSON.parse(localStorage.getItem('uec27')).mathSubjects.adv_math_i.chapters['1'].mastery===2);
assert.deepEqual(await p.evaluate(()=>JSON.parse(localStorage.getItem('uec27'))),backup);
await p.goto(root);await p.getByRole('button',{name:'课程地图',exact:true}).click();await p.getByRole('button',{name:'高级数学（II）',exact:true}).click();await p.getByRole('button',{name:'记录本科错题',exact:true}).click();await p.locator('#eq').fill('II独立错题');await p.getByRole('button',{name:'添加',exact:true}).click();
await p.goto(root+'#subject=adv_math_i');assert.equal(await p.locator('#subject-errors').getByText('II独立错题',{exact:true}).count(),0);
await p.goto(root+'#subject=adv_math_ii');assert.equal(await p.locator('#subject-errors').getByText('II独立错题',{exact:true}).count(),1);
await p.getByRole('button',{name:'题库与练习',exact:true}).click();assert.ok(await p.locator('#bank-subject').count());
await p.emulateMedia({colorScheme:'dark'});await p.goto(root+'#lesson='+encodeURIComponent(key));await p.screenshot({path:'reports/batch05/screenshots/notes-dark.png'});
assert.deepEqual(errors,[]);assert.deepEqual(bad,[]);
fs.writeFileSync('reports/batch05/BROWSER_RESULTS.json',JSON.stringify({status:'pass',checks,legacy_data_preserved:true,math_ranges:[29,35],math_chapter_state_isolated:true,backup_roundtrip:true,errors,bad},null,2)+'\n');
console.log('PASS '+checks.length+' viewport/chapter checks, math isolation, backup and original error-book regression');await b.close();
})().catch(e=>{console.error(e);process.exit(1)});

