/* Run against python -m http.server 8000 from the repository root. */
const assert=require('node:assert/strict'),fs=require('node:fs');const shots=process.env.QA_SCREENSHOT_DIR||'/tmp/uec-qa-screenshots';fs.mkdirSync(shots,{recursive:true});const {chromium}=require('playwright');
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const context=await browser.newContext({viewport:{width:1280,height:900}}),page=await context.newPage(),errors=[],requests=[];
 page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.url().startsWith(process.env.UEC_TEST_BASE||'http://localhost:8000/')&&r.status()>=400)requests.push([r.status(),r.url()]);});
 const base=process.env.UEC_TEST_BASE||'http://localhost:8000/';await page.goto(base);
 const seed={mast:{'数学34':2,'物理3':1},learn:{'数学34':'2026-11-10','化学3':'2026-11-10'},rv:{'数学34':[1]},done:{custom:true},start:'2026-11-17',err:[{s:'数学',c:34,q:'legacy math',w:'概念不懂',st:0,last:'',d:'2026-11-10'}],ex:[{n:'用户考试',d:'2027-05-20',r:'用户范围'}]};
 await page.evaluate(s=>localStorage.setItem('uec27',JSON.stringify(s)),seed);await page.reload();
 await page.getByRole('button',{name:'课程地图',exact:true}).click();
 await page.getByRole('button',{name:'高级数学（I）',exact:true}).click();assert.equal(await page.locator('h2').textContent(),'高级数学（I）');
 await page.getByLabel('累计学习分钟').fill('45');await page.getByLabel('累计学习分钟').dispatchEvent('change');
 await page.locator('textarea').fill('I 的独立记录');await page.locator('textarea').dispatchEvent('change');
 await page.getByRole('button',{name:'高级数学（II）',exact:true}).click();assert.equal(await page.getByLabel('累计学习分钟').inputValue(),'0');assert.equal(await page.locator('textarea').inputValue(),'');
 await page.getByLabel('累计学习分钟').fill('90');await page.getByLabel('累计学习分钟').dispatchEvent('change');
 await page.locator('textarea').fill('II 的独立记录');await page.locator('textarea').dispatchEvent('change');await page.reload();
 assert.equal(await page.locator('textarea').inputValue(),'II 的独立记录');await page.getByRole('button',{name:'高级数学（I）',exact:true}).click();assert.equal(await page.locator('textarea').inputValue(),'I 的独立记录');
 let saved=await page.evaluate(()=>JSON.parse(localStorage.getItem('uec27')));for(const k of ['mast','learn','rv','done','err','ex'])assert.deepEqual(saved[k],seed[k]);
 // Subject-coded errors and paper number remain separate; no legacy assignment.
 await page.getByRole('button',{name:'记录本科错题'}).click();assert.equal(await page.locator('#es').inputValue(),'adv_math_i');await page.locator('#eq').fill('I 原创错题');await page.getByRole('button',{name:'添加',exact:true}).click();
 saved=await page.evaluate(()=>JSON.parse(localStorage.getItem('uec27')));assert.equal(saved.err.at(-1).subject_code,'adv_math_i');assert.equal(saved.err.at(-1).paper_no,null);assert.equal(saved.err[0].s,'数学');
 const errorCard=page.locator('.card').filter({hasText:'I 原创错题'});await errorCard.getByRole('button',{name:'重做对了（0/2）'}).click();await page.locator('.card').filter({hasText:'I 原创错题'}).getByRole('button',{name:'重做对了（1/2）'}).click();assert.ok((await page.locator('.card').filter({hasText:'I 原创错题'}).textContent()).includes('已掌握'));
 await page.goto(base+'#subject=adv_math_ii');assert.ok((await page.locator('#subject-errors').textContent()).includes('本科错题 0'));
 await page.getByRole('button',{name:'题库与练习',exact:true}).click();assert.ok((await page.locator('main').textContent()).includes('0题'));await page.locator('#bank-subject').selectOption('chemistry');await page.locator('#bank-query').fill('H₂SO₄');await page.getByRole('button',{name:'搜索',exact:true}).click();assert.ok((await page.locator('main').textContent()).includes('物质的量')||(await page.locator('main').textContent()).includes('0.250mol'));
 // Direct URLs work without relocating any original math unit.
 for(const hash of ['#lesson='+encodeURIComponent('数学34'),'#'+encodeURIComponent('数学34')]){await page.goto(base+hash);assert.ok((await page.locator('main').textContent()).includes('复数'));}
 await page.goto(base+'?lesson='+encodeURIComponent('数学34'));assert.ok((await page.locator('main').textContent()).includes('复数'));
 const chapters=['物理3','物理4','化学3','化学4','化学5','化学6','化学7','化学8','化学9','化学10','化学11','生物1','生物2','生物3'],sizes=[{width:320,height:800},{width:390,height:844},{width:1280,height:900}];let inspected=0;
 for(const size of sizes){await page.setViewportSize(size);for(const key of chapters){await page.goto(base+'#lesson='+encodeURIComponent(key));await page.waitForSelector('[data-module]');
 const n=await page.locator('.lesson-section').count();assert.ok(n>0);assert.equal(await page.locator('[data-module]').count(),n*12);
 await page.locator('figure img').evaluateAll(imgs=>Promise.all(imgs.map(i=>{i.loading='eager';return i.decode().catch(()=>{})})));assert.equal(await page.locator('figure img').evaluateAll(imgs=>imgs.filter(i=>!i.complete||i.naturalWidth===0).length),0);
 const overflow=await page.evaluate(()=>({doc:document.documentElement.scrollWidth,view:innerWidth,bad:[...document.querySelectorAll('.note-module,.formula,figure,.concept-flow')].filter(e=>e.getBoundingClientRect().right>innerWidth+1).map(e=>e.className)}));assert.ok(overflow.doc<=overflow.view+1,JSON.stringify({key,size,overflow}));assert.equal(overflow.bad.length,0);
 inspected++;if(key==='化学3'&&(size.width===390||size.width===1280))await page.screenshot({path:`${shots}/chemistry-${size.width}.png`});
 }}
 // Per-section self assessment and complete solutions work and persist.
 await page.goto(base+'#lesson='+encodeURIComponent('化学3')+'&section=3.6');const unit=page.locator('[id="unit-化学3-3.6"]');await unit.getByRole('button',{name:'能独立解释',exact:true}).click();await page.reload();assert.ok((await page.locator('[id="unit-化学3-3.6"]').getByRole('button',{name:'能独立解释 ✓'}).count())===1);
 const solution=page.locator('[id="unit-化学3-3.6-solution1"] details');await solution.locator('summary').click();assert.ok(await solution.getAttribute('open')!==null);
 // Existing chapter learning/mast, calendar and export/import round trip.
 await page.goto(base);await page.getByRole('button',{name:'课程地图',exact:true}).click();await page.evaluate(()=>{flt='物理';open='物理3';render()});await page.locator('[data-a="mast"][data-k="物理3"][data-v="3"]').click();await page.locator('[data-a="learn"][data-k="物理3"]').click();await page.reload();saved=await page.evaluate(()=>JSON.parse(localStorage.getItem('uec27')));assert.equal(saved.mast['物理3'],3);assert.ok(saved.learn['物理3']);assert.equal(saved.mast['数学34'],2);
 await page.getByRole('button',{name:'考试日历',exact:true}).click();assert.ok((await page.locator('main').textContent()).includes('用户范围'));
 await page.locator('input[data-d="0"]').fill('2027-05-21');await page.locator('input[data-d="0"]').dispatchEvent('change');
 const downloadPromise=page.waitForEvent('download');await page.getByRole('button',{name:'导出进度',exact:true}).click();const dl=await downloadPromise;const stream=await dl.createReadStream();let backup='';for await(const chunk of stream)backup+=chunk.toString();const exported=JSON.parse(backup);assert.equal(exported.mathSubjects.adv_math_i.study_note,'I 的独立记录');assert.equal(exported.ex[0].d,'2027-05-21');
 await page.locator('#imp').setInputFiles({name:'progress.json',mimeType:'application/json',buffer:Buffer.from(backup)});await page.waitForTimeout(150);saved=await page.evaluate(()=>JSON.parse(localStorage.getItem('uec27')));assert.deepEqual(saved,exported);
 await page.emulateMedia({colorScheme:'dark'});await page.goto(base+'#lesson='+encodeURIComponent('生物2'));await page.screenshot({path:shots+'/biology-dark.png'});
 assert.deepEqual(errors,[]);assert.deepEqual(requests,[]);
 const result={result:'pass',viewport_chapter_checks:inspected,viewports:sizes,checks:['旧数据无损保留','两个数学科目独立记录并刷新','旧数学无强制分配','本科错题隔离和两次正确掌握','科目题库筛选与跨科搜索','直接URL和旧章链接','86节×12模块DOM','全部所用图可加载','长笔记/公式/图示无页面溢出','小节检测存储','完整解析展开','原有章掌握度及学习存储','日历改期存储','导出/导入全部数据往返','暗色页面截图'],console_errors:errors,local_http_errors:requests};fs.writeFileSync('reports/BROWSER_RESULTS.json',JSON.stringify(result,null,2)+'\n');console.log('PASS browser regression and migration; '+inspected+' viewport/chapter checks.');await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
