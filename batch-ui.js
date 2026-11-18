/* Additive UI: D and legacy progress keys are deliberately unchanged. */
const SUBJECT_LIST=window.SUBJECTS;
for(const s of SUBJECT_LIST){if(!s.legacy){SN[s.code]=s.name;SC[s.code]='#9333ea';IM[s.code]='math';}}
SN.数学='旧数学记录（兼容）';
SN.math_shared='高数I／II共用内容';
let mathChapter=0;
let subjectView='physics',bankFilter='all',bankQuery='';
const subjectByCode=c=>SUBJECT_LIST.find(s=>s.code===c);
const stateExtras=()=>{S.checks=S.checks||{};S.mathSubjects=S.mathSubjects||{};for(const c of ['adv_math_i','adv_math_ii'])S.mathSubjects[c]=S.mathSubjects[c]||{study_note:'',study_minutes:0};};
stateExtras();
function examPanels(code){
 const e=EXAM_SOURCES[code];if(!e)return '<p>旧数学未完成科目映射，不套用任一科目范围。</p>';
 return `<section class="card"><h3>兴华校内备考安排</h3><p class="mu">12/11/2026学校文件，第${e.page}页；适用于兴华2027校内。学校重点不用于删减课程。</p>${ul(e.school)}<p class="mu">原件由用户提供；逐页审核与摘要差异见 <a href="reports/SCHOOL_SOURCE_REVIEW.md">学校核对记录</a>。</p></section><section class="card"><h3>UEC正式统考资料</h3><p class="mu">以下为官网当前公开的2026文件，尚未确认2027继续适用。</p>${ul(e.official)}<p><a href="https://uec.dongzong.my/wp-content/uploads/2026/07/${e.file}" target="_blank" rel="noopener">董总${e.file}</a> · <a href="reports/SOURCE_AUDIT.csv">来源台账</a></p></section>`;
}
const subjectButtons=()=>'<div class="row subject-links">'+SUBJECT_LIST.map(s=>`<button data-a="subject" data-k="${s.code}">${s.name}</button>`).join('')+'</div>';
function subjectLessons(code){const s=subjectByCode(code);return s?.legacy?D.filter(d=>d[0]===s.legacy):[];}
function mathState(code,chapter){stateExtras();const st=S.mathSubjects[code];st.chapters=st.chapters||{};return st.chapters[chapter]=st.chapters[chapter]||{learned_at:'',rv:[],mastery:0};}
function mathCourseView(code){
 const config=window.MATH_COURSES[code],st=S.mathSubjects[code],units=D.filter(d=>d[0]==='数学'&&d[2]>=config.first&&d[2]<=config.last);
 const chapters=st.chapters||{},done=units.filter(d=>chapters[d[2]]?.learned_at).length;
 let h=`<section class="card" id="subject-notes"><h3>第${config.first}–${config.last}章</h3><p>${esc(config.source)}。沿用原章号、名称和顺序；共用笔记内容，I、II分别记录掌握度、完成日期和间隔复习。旧数学记录仍完整保留，未自动复制。</p><p class="mu">这是用户确认的课程对应；2027正式统考适用性仍按考试资料栏核实。每科分别有试卷一、试卷二。</p>${units.map(d=>`<div class="row"><a href="#subject=${code}&chapter=${d[2]}">第${d[2]}章 ${esc(d[3])}</a><span class="mu">${LS(K(d))?'已有笔记':'笔记待写'}${chapters[d[2]]?.learned_at?' · 已学 '+esc(chapters[d[2]].learned_at):''}</span></div>`).join('')}</section>`;
 if(units.some(d=>d[2]===mathChapter)){const key='数学'+mathChapter,L=LS(key),c=chapters[mathChapter]||{},d=find(key);h+=`<section class="card"><h3>${esc(subjectByCode(code).name)} 第${mathChapter}章 ${esc(d[3])}</h3><p>本科记录：${c.learned_at?'已学 '+esc(c.learned_at):'未登记学完'}</p><button data-a="subject-math-learn" data-k="${mathChapter}">今天学完，开始本科间隔复习</button><div class="row">${['待学习','需复习','已掌握'].map((x,i)=>`<button data-a="subject-math-mastery" data-k="${mathChapter}" data-v="${i}" aria-pressed="${(c.mastery||0)===i}">${x}</button>`).join('')}</div></section>`;
 h+=L?L.sections.map(x=>renderSection(x,key,code+':'+key)||'<p>本节内容待补齐。</p>').join(''):'<section class="card"><p>本章保留原目录，笔记尚待编写；未建立虚构课本小节。</p></section>';}
 h+=`<section class="card" id="subject-progress"><h3>本科独立学习记录</h3><p>已学${done}/${units.length}章。</p><label>累计学习分钟 <input type="number" min="0" step="1" value="${st.study_minutes}" data-math="study_minutes" aria-label="累计学习分钟"></label><label class="block">个人复习笔记<textarea data-math="study_note" rows="5">${esc(st.study_note)}</textarea></label>`;
 for(const d of units){const c=chapters[d[2]];if(!c?.learned_at)continue;const due=IV.filter(v=>!(c.rv||[]).includes(v)&&days(c.learned_at,today())>=v);if(due.length)h+=`<p>第${d[2]}章待回忆：${due.map(v=>`<button data-a="subject-math-review" data-k="${d[2]}" data-v="${v}">第${v}天回忆完成</button>`).join('')}</p>`;}
 return h+'</section>';
}
function vSubject(){
 stateExtras();const s=subjectByCode(subjectView),units=subjectLessons(subjectView),isMath=subjectView.startsWith('adv_math_');
 let h=subjectButtons()+`<section class="card"><h2>${s.name}</h2><p>${s.official||'现有课程与进度'}</p><div class="row"><button data-a="subject-notes">笔记与课程</button><button data-a="subject-bank">题库与练习</button><button data-a="subject-progress">学习进度</button><button data-a="subject-errors">本科错题</button><button data-a="subject-exams">考试资料</button></div></section>`;
 if(isMath){h+=mathCourseView(subjectView);}
 else{h+=`<section class="card" id="subject-notes"><h3>笔记与课程</h3>${units.map(d=>chLine(d[0],d[2])).join('')}</section><section class="card" id="subject-progress"><h3>学习进度</h3><p>已学${units.filter(d=>S.learn[K(d)]).length}/${units.length}章；沿用原有记录。</p></section>`;}
 const errs=S.err.filter(e=>errorCode(e)===subjectView);
 h+=`<section class="card" id="subject-errors"><h3>本科错题 ${errs.length}</h3>${errs.length?ul(errs.map(e=>e.q||'未填写题干')):'<p>暂无本科错题。</p>'}<button data-a="subject-error-add">记录本科错题</button></section><div id="subject-exams">${examPanels(subjectView)}</div>`;return h;
}
const errorCode=e=>e.subject_code||SUBJECT_LIST.find(s=>s.legacy===e.s)?.code||e.s;
function questionBank(){
 const out=[];for(const [key,ss] of Object.entries(window.BATCH_NOTES||{}))for(const [id,u] of Object.entries(ss))for(const [i,q] of u.practice.entries())out.push({...q,key,id,number:i+1});return out;
}
function questionBelongs(q,code){if(q.subject_code===code)return true;const range=window.MATH_COURSES?.[code];return q.subject_code==='math_shared'&&!!range&&q.chapter_id>=range.first&&q.chapter_id<=range.last;}
function questionLessonLinks(q){if(q.subject_code!=='math_shared')return `<a href="#lesson=${encodeURIComponent(q.key)}&section=${q.id}">回到本节</a>`;return ['adv_math_i','adv_math_ii'].filter(c=>(bankFilter==='all'||bankFilter===c)&&questionBelongs(q,c)).map(c=>`<a href="#subject=${c}&chapter=${q.chapter_id}&section=${q.id}">回到${esc(subjectByCode(c).name)}本章</a>`).join(' · ');}
function vBank(){
 const questions=questionBank().filter(q=>(bankFilter==='all'||questionBelongs(q,bankFilter))&&(!bankQuery||[q.q,q.ans,q.id,find(q.key)?.[3]].join(' ').includes(bankQuery)));
 return `<section class="card"><h2>题库与练习</h2><div class="row"><select id="bank-subject" aria-label="题库科目"><option value="all">全部科目</option>${SUBJECT_LIST.map(s=>`<option value="${s.code}" ${bankFilter===s.code?'selected':''}>${s.name}</option>`).join('')}</select><input id="bank-query" value="${esc(bankQuery)}" placeholder="搜索题干、答案或小节" aria-label="搜索题库"><button data-a="bank-search">搜索</button></div><p class="mu">${questions.length}题；新增题均为原创，非官方。科目独立于卷别；没有给原创题冒设官方卷号。旧章级练习仍保留在各章底部。</p></section>`+(questions.length?questions.map(q=>`<section class="card"><p>${q.subject_code==='math_shared'?SN.math_shared:SN[find(q.key)[0]]} ${q.id} · 练习${q.number}</p>${renderQuestion(q)}${questionLessonLinks(q)}</section>`).join(''):'<section class="card">本科尚无经过映射的题目。旧数学题目不会自动归入I或II。</section>');
}
function renderQuestion(q,show=false){const stages=q.method?`<p><b>题意分析：</b>${fm(q.analysis)}</p><p><b>已知条件：</b>${fm(q.given)}</p><p><b>方法选择：</b>${fm(q.method)}</p><p><b>原理与条件：</b>${fm(q.principle)}</p>`:'';return `<p>${fm(q.q)}</p><details ${show?'open':''}><summary>完整解析 · 原创，非官方</summary>${stages}${ol(q.steps)}<p><b>答：</b>${fm(q.ans)}</p>${q.verification?`<p><b>验算/证据检查：</b>${fm(q.verification)}</p><p><b>易错分析：</b>${fm(q.pitfall)}</p>`:''}</details>`;}
function diagnosticQuestion(u,ref,explicit){if(explicit)return explicit;const i=Number(ref.slice(1));return ref[0]==='e'?u.examples[i]:ref[0]==='p'?u.practice[i]:u.quiz;}
function strategyBlock(u,base){if(!u.strategy)return '';const x=u.strategy,q=u.examples[x.worked_example_index];return `<article class="strategy"><h5>由题干到解法：本节判断过程</h5><p><b>题干线索：</b>${fm(x.trigger)}</p><p><b>方法选择：</b>${fm(x.method)}</p><p><b>原理与条件：</b>${fm(x.principle)}</p><h5>用已有例题验证判断</h5><p>${fm(q.q)}</p><p><b>本例选法：</b>${fm(q.method||x.method)}</p><a href="#${base}-example${x.worked_example_index+1}">回看例${x.worked_example_index+1}的八步解析</a><p><b>独立复核：</b>${fm(x.verification)}</p><p><b>错法为何不成立：</b>${fm(x.pitfall)}</p><p class="mu">以上是原创教学答题方法，未赋予官方步骤分或考频。</p></article>`;}
function diagnosticsBlock(u,key,base){if(!u.diagnostics)return '';return '<div class="goal-diagnostics">'+u.diagnostics.map((g,i)=>{const q=diagnosticQuestion(u,g.question_ref,g.question),id=key+':goal'+g.goal_index,v=S.goalChecks?.[id];return `<article><h5>目标${g.goal_index+1}：${esc(u.goals[g.goal_index])}</h5>${renderQuestion(q)}<details ${v==='review'?'open':''}><summary>该目标的错因与回读</summary><p>${fm(g.feedback)}</p><a href="#${base}-m${g.review_module}">回读${g.review_module===5?'图解、推导及条件':g.review_module===7?'题型与判断方法':'深度讲解'}</a> · <a href="#${base}-m8">核对易错概念</a></details><div class="row"><button data-a="goal-check" data-k="${esc(id)}" data-v="review" aria-pressed="${v==='review'}">此目标需复习${v==='review'?' ✓':''}</button><button data-a="goal-check" data-k="${esc(id)}" data-v="ready" aria-pressed="${v==='ready'}">此目标能解释${v==='ready'?' ✓':''}</button></div></article>`}).join('')+'</div>';}
function figureBlock(path,caption,illustrationId){return `<figure${illustrationId?` class="v22-figure" data-illustration-id="${esc(illustrationId)}"`:''}><button class="figure-open" data-a="figure-open" data-src="${esc(path)}" data-caption="${esc(caption)}" aria-label="放大查看：${esc(caption)}"><img src="${esc(path)}" alt="${esc(caption)}" loading="lazy"></button><figcaption>${fm(caption)} <span class="mu">点击可放大查看</span></figcaption></figure>`;}
const supersededFigure=path=>Object.hasOwn(window.V22_SUPERSEDED_FIGURES||{},path);
function importedFigures(k,sid){return (window.APPROVED_ILLUSTRATIONS||[]).filter(x=>x.lesson_key===k&&x.section_id===sid&&x.status==='approved_for_limited_use'&&!supersededFigure(x.path)).map(x=>figureBlock(x.path,x.caption)).join('');}
function openFigure(src,caption){let d=document.getElementById('figure-viewer');if(!d){d=document.createElement('dialog');d.id='figure-viewer';d.innerHTML='<form method="dialog"><button autofocus>关闭放大图</button></form><p class="viewer-caption"></p><p class="mu">可横向滑动或滚动查看完整图；按Esc或关闭按钮返回。</p><div class="viewer-scroll"><img alt=""></div>';document.body.append(d);d.addEventListener('click',e=>{if(e.target===d)d.close()});}d.querySelector('img').src=src;d.querySelector('img').alt=caption;d.querySelector('.viewer-caption').textContent=caption;d.showModal();}
const MODULE_TITLES=['学习目标','前置知识','知识结构图','深度知识讲解','图解与公式／实验','典型例题','UEC题型攻略','易错易混','分层练习','完整解析','考前速记','掌握度检测'];
function flowDiagram(nodes){return `<ol class="concept-flow" aria-label="知识关系或学习路径">${nodes.map(n=>`<li>${esc(n.trim())}</li>`).join('')}</ol>`;}
function sectionOutline(L,k){return L.sections.map(s=>{const group=(L.directory_groups||[]).find(g=>g.children[0]===s.id);return (group?`<h4>${esc(group.id)} ${esc(group.t)}</h4>`:'')+`<p><a href="#lesson=${encodeURIComponent(k)}&section=${s.id}">${s.id} ${esc(s.t)}</a></p>`;}).join('');}
function renderSection(s,k,stateKey=k){
 const u=window.BATCH_NOTES?.[k]?.[s.id];if(!u)return null;
 const base=`unit-${stateKey}-${s.id}`,check=`${stateKey}:${s.id}`;
 const v22Figures=(window.V22_ILLUSTRATIONS||[]).filter(fig=>fig.lesson_key===k&&fig.section_id===s.id&&['PASS','FIXED'].includes(fig.status)&&[4,5,6].includes(fig.module));
 const terms=v22Figures.length&&s.terms==='教学图尚待制作；现有文字、式子与步骤可独立学习。'?'本节已接入部分图解；文字、式子与解题步骤请结合阅读。':s.terms;
 const held=(s.figs||[]).filter(f=>(window.QUARANTINED_LEGACY_FIGURES||[]).includes(f[0]));
 const figs=(s.figs||[]).filter(f=>!(window.QUARANTINED_LEGACY_FIGURES||[]).includes(f[0])&&!supersededFigure(f[0])).map(f=>figureBlock(f[0],f[1])).join('')+importedFigures(k,s.id)+(held.length?'<p class="mu">本节有'+held.length+'幅旧图待科学修订，文件保留，当前教学视图暂不展示。详见插图总清单。</p>':'');
 const blocks=[ul(u.goals),ul(u.prerequisites),(u.concept_relation?`<div class="concept-branches"><p><b>${esc(s.t)}</b></p><p>${fm(u.concept_relation)}</p><ul>${u.flow.map(n=>`<li>${esc(n)}</li>`).join('')}</ul><p class="mu">以上为知识项目与条件的关联，不把所有项目串成同一因果或反应顺序。</p></div>`:flowDiagram(u.flow)),s.body.concat(u.deep).map(p=>`<p>${fm(p)}</p>`).join(''),figs+u.derive.map(p=>`<p>${fm(p)}</p>`).join('')+(s.f?`<div class="formula">${s.f.map(f=>`<p><code>${esc(f)}</code></p>`).join('')}</div>`:'')+(s.terms?`<p class="mu">${esc(s.terms)}</p>`:''),u.examples.map((q,i)=>`<article id="${base}-example${i+1}"><h5>例${i+1} · ${['基础','标准','进阶'][i]}</h5>${renderQuestion(q,true)}</article>`).join(''),strategyBlock(u,base)+ul(u.exam)+`<p class="mu">范围对照：${esc(s.syl)}；具体董总文件页码及核实边界见本节来源。2027适用性待核实。${u.exam_evidence.length?u.exam_evidence.map(ev=>`第三方网页标示：2025卷${ev.paper_no}第${ev.question_no}题（<a href="${esc(ev.source)}" target="_blank" rel="noopener">题干索引</a>）；已核对网页，未核对官方原卷／评分表，不计考频。`).join(''):'本轮无已核实到本节的真题索引，exam_evidence为空，未统计考频。'}答题步骤为教学建议。</p>`,s.tips.map(t=>`<p class="tip"><b>${esc(t[0])}</b> ${fm(t[1])}</p>`).join('')+(u.error_analysis||[]).map(x=>`<article><h5>错解定位</h5><p>${fm(x.wrong_approach)}</p><p><b>纠正：</b>${fm(x.correction)}</p><p><b>怎样检查：</b>${fm(x.verification)}</p></article>`).join(''),u.practice.map((q,i)=>`<article id="${base}-q${i+1}"><h5>${['基础','理解','应用','跨小节综合'][i]} · 练习${i+1}</h5><p>${fm(q.q)}</p><a href="#${base}-solution${i+1}">查看完整解析${i+1}</a></article>`).join(''),u.practice.map((q,i)=>`<article id="${base}-solution${i+1}"><h5>练习${i+1}解析</h5>${renderQuestion(q)}<a href="#${base}-q${i+1}">返回题目</a></article>`).join(''),ul(u.quick),diagnosticsBlock(u,check,base)+renderQuestion(u.quiz)+`<p class="mu">先独立作答，再展开答案核对；答错时按解析末尾提示回读。自评保存在本设备。</p><div class="row">${['需重学','看解析才会','能独立解释'].map((v,i)=>`<button data-a="section-check" data-k="${esc(check)}" data-v="${i}" class="${S.checks?.[check]===i?'on':''}">${v}${S.checks?.[check]===i?' ✓':''}</button>`).join('')}</div>`];
 if(terms!==s.terms)blocks[4]=blocks[4].replace(esc(s.terms),esc(terms));
 for(const fig of v22Figures)blocks[fig.module-1]+=figureBlock(fig.path,fig.caption,fig.code);
 return `<details class="card lesson-section" id="${base}" open><summary>${s.id} ${esc(s.t)} <span class="tag">12模块</span></summary><p class="mu">核实状态：部分核实；目录对照来源见本节，2027考试适用性与教师审定尚待确认。</p><div class="module-links">${MODULE_TITLES.map((t,i)=>`<a href="#${base}-m${i+1}">${String(i+1).padStart(2,'0')} ${t}</a>`).join('')}</div>${blocks.map((b,i)=>`<section class="note-module" data-module="${i+1}" id="${base}-m${i+1}"><h4>${String(i+1).padStart(2,'0')} ${MODULE_TITLES[i]}</h4>${b}</section>`).join('')}<details><summary>本节来源与核实边界</summary>${ul(u.content_sources.map(x=>`${x.source_id} · ${x.page?(typeof x.page==='number'?'第'+x.page+'页':x.page):x.page_or_section} · ${x.version} · 查阅${x.access_date}`))}<ul>${u.content_sources.filter(x=>x.url).map(x=>`<li><a href="${esc(x.url)}" target="_blank" rel="noopener">${esc(x.source_id)}原理/目录来源</a></li>`).join('')}</ul><a href="reports/SOURCE_AUDIT.csv">来源登记表</a>${u.content_batch==='batch05'?'<a href="reports/batch05/SOURCES.md">本轮逐节来源与边界</a>':u.authoring_sources?'<a href="reports/batch04/SOURCES.csv">前批逐节来源</a>':''}</details></details>`;
}
// Attach explicit provenance to inherited original chapter exercises as well.
for(const d of D){const l=LS(K(d)),code=SUBJECT_LIST.find(s=>s.legacy===d[0])?.code;if(l)for(const q of [...(l.ex||[]),...(l.pr||[]),...(l.ext||[])]){q.subject_code=q.subject_code||code;q.paper_no=q.paper_no??null;q.question_origin=q.question_origin||'original';}}
const oldLesson=vLesson;
vLesson=function(k){const L=LS(k),d=find(k);if(d?.[0]==='数学'&&!L)return `<section class="card"><h2>数学旧资料 第${d[2]}章 ${esc(d[3])}</h2><p>原有章号与进度保留；本章的小节笔记尚待编写；已按用户确认的范围列入对应高数入口。旧进度保留在兼容记录中。</p><button data-a="subject" data-k="math_pending">查看兼容目录</button></section>`;
 const old=oldLesson(k);if(!L||!window.BATCH_NOTES?.[k])return old;
 // Replace only the original section cards. Keep all original chapter-level resources.
 const holder=document.createElement('div');holder.innerHTML=old;
 const cards=Array.from(holder.querySelectorAll(':scope > details')).slice(0,L.sections.length);
 cards.forEach((card,i)=>{const s=L.sections[i],tmp=document.createElement('div');tmp.innerHTML=renderSection(s,k);card.replaceWith(tmp.firstElementChild);});
 const toc=document.createElement('section');toc.className='card';toc.innerHTML=`<h3>本章小节目录</h3>${sectionOutline(L,k)}`;holder.children[0].after(toc);const evidence=document.createElement('details');evidence.className='card';evidence.innerHTML='<summary>兴华校内与UEC正式统考资料（分栏）</summary>'+examPanels(SUBJECT_LIST.find(x=>x.legacy===d[0]).code);toc.after(evidence);
 return holder.innerHTML;
};
const oldMap=vMap;
vMap=function(){return subjectButtons()+`<div class="card"><button data-a="bank">跨科题库与搜索</button><p class="mu">数学I、II为两个独立科目，各自包含试卷一、二。下列数学旧目录保留原顺序与数据。</p></div>`+oldMap();};
const oldErr=vErr;
vErr=function(){const h=document.createElement('div');h.innerHTML=oldErr();const select=h.querySelector('#es');for(const c of ['adv_math_i','adv_math_ii']){const op=document.createElement('option');op.value=c;op.textContent=SN[c];select.append(op);}return h.innerHTML;};
const oldCal=vCal;
vCal=function(){return `<section class="card"><h3>考试资料按科查看</h3>${subjectButtons()}<p class="mu">学校安排与UEC当前官方版本在各科入口分栏展示。下列旧版或用户日历备注原样保留，核实范围请查看对应科目资料。</p></section>`+oldCal();};
function navigateHash(){const raw=location.hash.slice(1),decoded=decodeURIComponent(raw),mathAnchor=decoded.match(/^unit-(adv_math_i|adv_math_ii):数学(\d+)-/),scienceAnchor=decoded.match(/^unit-((?:物理|化学|生物|数学)\d+)-/);
 if(mathAnchor){const code=mathAnchor[1],chapter=Number(mathAnchor[2]),range=window.MATH_COURSES[code];if(chapter>=range.first&&chapter<=range.last){if(tab!=='subject'||subjectView!==code||mathChapter!==chapter){subjectView=code;mathChapter=chapter;tab='subject';render();requestAnimationFrame(()=>document.getElementById(decoded)?.scrollIntoView());}return;}}
 if(scienceAnchor&&find(scienceAnchor[1])){if(tab!=='lesson'||lk!==scienceAnchor[1]){lk=scienceAnchor[1];tab='lesson';render();requestAnimationFrame(()=>document.getElementById(decoded)?.scrollIntoView());}return;}
 const p=new URLSearchParams(raw),key=p.get('lesson')||(find(decodeURIComponent(raw))?decodeURIComponent(raw):new URLSearchParams(location.search).get('lesson'));
 if(key&&find(key)){lk=key;tab='lesson';render();if(p.get('section'))requestAnimationFrame(()=>document.getElementById(`unit-${key}-${p.get('section')}`)?.scrollIntoView());}
 else if(subjectByCode(p.get('subject'))){subjectView=p.get('subject');mathChapter=Number(p.get('chapter'))||0;tab='subject';render();scrollTo(0,0);if(p.get('section'))requestAnimationFrame(()=>document.getElementById('unit-'+subjectView+':数学'+mathChapter+'-'+p.get('section'))?.scrollIntoView());}
 // Normal module anchors do not rerender the page or close answers.
}
const oldRender=render;
render=function(){stateExtras();if(tab==='subject'||tab==='bank'){$('#v').innerHTML=hdr()+(tab==='subject'?vSubject():vBank());$('#n').innerHTML=[['today','今日'],['map','课程地图'],['err','错题本'],['cal','考试日历']].map(x=>`<button aria-label="${x[1]}" data-a="tab" data-k="${x[0]}">${x[1]}</button>`).join('');}else oldRender();};
document.addEventListener('click',e=>{const b=e.target.closest('[data-a]');if(!b)return;const a=b.dataset.a;
 if(a==='figure-open'){openFigure(b.dataset.src,b.dataset.caption);}
 else if(a==='goal-check'){S.goalChecks=S.goalChecks||{};S.goalChecks[b.dataset.k]=b.dataset.v;save();const article=b.closest('article');article.querySelectorAll('[data-a="goal-check"]').forEach(x=>{const on=x===b;x.setAttribute('aria-pressed',String(on));x.textContent=x.textContent.replace(' ✓','')+(on?' ✓':'');});if(b.dataset.v==='review')article.querySelector('details:last-of-type').open=true;}
 else if(a==='subject'){subjectView=b.dataset.k;mathChapter=0;tab='subject';location.hash='subject='+subjectView;render();scrollTo(0,0);}
 else if(a==='les'){history.replaceState(null,'','#lesson='+encodeURIComponent(b.dataset.k));}
 else if(a==='bank'||a==='subject-bank'){bankFilter=a==='bank'?'all':subjectView;tab='bank';render();}
 else if(a==='bank-search'){bankFilter=$('#bank-subject').value;bankQuery=$('#bank-query').value.trim();render();}
 else if(a==='section-check'){stateExtras();S.checks[b.dataset.k]=+b.dataset.v;save();b.parentElement.querySelectorAll('button').forEach(x=>{const on=x===b;x.classList.toggle('on',on);x.textContent=x.textContent.replace(' ✓','')+(on?' ✓':'');});}
 else if(a==='subject-math-learn'||a==='subject-math-review'||a==='subject-math-mastery'){const st=mathState(subjectView,Number(b.dataset.k));if(a==='subject-math-learn'){st.learned_at=today();st.rv=[];}else if(a==='subject-math-review'){st.rv=st.rv||[];if(!st.rv.includes(Number(b.dataset.v)))st.rv.push(Number(b.dataset.v));}else st.mastery=Number(b.dataset.v);save();render();}
 else if(a==='subject-error-add'){tab='err';render();$('#es').value=subjectByCode(subjectView).legacy||subjectView;}
 else if(a.startsWith('subject-'))document.getElementById(a)?.scrollIntoView();
 if(a==='eadd'&&S.err.length){const last=S.err[S.err.length-1];if(!last.subject_code){last.subject_code=errorCode(last);last.paper_no=null;save();}}
});
document.addEventListener('change',e=>{if(e.target.dataset.math){stateExtras();const f=e.target.dataset.math;S.mathSubjects[subjectView][f]=f==='study_minutes'?Math.max(0,Math.trunc(Number(e.target.value)||0)):e.target.value;save();}});
window.addEventListener('hashchange',navigateHash);
