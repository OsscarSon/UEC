/* Data adapters are additive: canonical curriculum and teaching text are untouched. */
(()=>{
const clone=x=>JSON.parse(JSON.stringify(x)),math=['adv_math_i','adv_math_ii'];
const courses=()=>SUBJECT_LIST.filter(s=>s.code!=='math_pending');
function ensure(){
 stateExtras();S.dashboard=S.dashboard||{};const d=S.dashboard;
 d.plans=d.plans||{};d.events=d.events||[];d.favorites=d.favorites||{};d.preferences=d.preferences||{};
 d.weeklyGoal=Number.isFinite(d.weeklyGoal)&&d.weeklyGoal>0?d.weeklyGoal:12;
 S.studyTools=S.studyTools||{boards:{}};S.studyTools.boards=S.studyTools.boards||{};
 if(!S.mathMigration){
  const raw={learn:{},mast:{},rv:{},checks:{},goalChecks:{},errors:[]};
  for(const field of ['learn','mast','rv','checks','goalChecks'])for(const [key,value] of Object.entries(S[field]||{}))if(key.startsWith('数学'))raw[field][key]=clone(value);
  raw.errors=S.err.filter(e=>e.s==='数学'&&!e.subject_code).map(clone);
  const counts={chapter_fields:0,section_checks:0,errors:0};
  for(const code of math){const st=S.mathSubjects[code];st.chapters=st.chapters||{};
   for(let chapter=1;chapter<=MATH_COURSES[code].last;chapter++){
    const key='数学'+chapter,fields={};if(Object.hasOwn(raw.learn,key))fields.learned_at=raw.learn[key];if(Object.hasOwn(raw.rv,key))fields.rv=raw.rv[key];if(Object.hasOwn(raw.mast,key))fields.legacy_mastery=raw.mast[key];
    if(Object.keys(fields).length){const target=st.chapters[chapter]||(st.chapters[chapter]={}),independent=!!target.learned_at||Number(target.mastery)>0||(target.rv||[]).length>0;for(const [f,v] of Object.entries(fields)){if(f!=='legacy_mastery'&&independent)continue;if(!Object.hasOwn(target,f)||(f==='learned_at'&&!target[f])||(f==='rv'&&target[f].length===0)){target[f]=clone(v);counts.chapter_fields++;}}}
   }
   for(const field of ['checks','goalChecks']){S[field]=S[field]||{};for(const [key,v] of Object.entries(raw[field])){const ch=Number(key.match(/^数学(\d+)/)?.[1]);if(ch>=1&&ch<=MATH_COURSES[code].last&&!Object.hasOwn(S[field],code+':'+key)){S[field][code+':'+key]=clone(v);counts.section_checks++;}}}
   raw.errors.forEach((e,i)=>{const chapter=Number(e.c);if(chapter<1||chapter>MATH_COURSES[code].last)return;const id=code+':'+i;if(!S.err.some(x=>x._legacyMathId===id)){S.err.push({...clone(e),s:code,subject_code:code,_legacyMathId:id});counts.errors++;}});
  }
  S.mathMigration={version:1,created_at:new Date().toISOString(),policy:'只填空缺；已有独立字段优先；共享章分科后各自记录；原始掌握等级不推测重映射。',counts,backup:raw};save();
 }
 return d;
}
function units(code){const s=courses().find(s=>s.code===code);if(!s)return[];return D.filter(d=>s.legacy?d[0]===s.legacy:d[0]==='数学'&&d[2]<=MATH_COURSES[code].last);}
function state(code,ch){return code.startsWith('adv_math_')?S.mathSubjects[code]?.chapters?.[ch]||{}:{learned_at:S.learn[(subjectByCode(code)?.legacy||'')+ch],rv:S.rv[(subjectByCode(code)?.legacy||'')+ch]||[],legacy_mastery:S.mast[(subjectByCode(code)?.legacy||'')+ch]};}
function href(code,ch,section=''){return code.startsWith('adv_math_')?'#subject='+code+(ch?'&chapter='+ch:'')+(section?'&section='+section:''):'#lesson='+encodeURIComponent((subjectByCode(code)?.legacy||'')+ch)+(section?'&section='+section:'');}
function record(type,detail={}){const d=ensure();d.events.push({type,date:today(),at:Date.now(),...detail});save();}
function plan(){const d=ensure(),date=today();if(!d.plans[date]){
 const codes=['physics','chemistry','biology',new Date().getDate()%2?'adv_math_i':'adv_math_ii'];
 d.plans[date]=codes.map(code=>{const list=units(code).filter(x=>LS(K(x))),u=list.find(x=>!state(code,x[2]).learned_at)||list[0],s=LS(K(u)).sections[0];return{id:code+'-'+u[2],course:code,chapter:u[2],section:s?.id||'',title:s?s.id+' '+s.t:u[3],done:false};});save();}
 return d.plans[date];}
function due(){const out=[];for(const course of courses())for(const d of units(course.code)){const st=state(course.code,d[2]);if(!st.learned_at)continue;const elapsed=days(st.learned_at,today()),interval=IV.find(v=>!(st.rv||[]).includes(v)&&elapsed>=v);if(interval)out.push({course:course.code,chapter:d[2],title:d[3],interval,overdue:elapsed-interval});}return out.sort((a,b)=>b.overdue-a.overdue);}
function activeErrors(){return S.err.map((e,index)=>({e,index})).filter(({e})=>!(e.s==='数学'&&!e.subject_code));}
function contextFromKey(key){const m=key.match(/^(?:(adv_math_i|adv_math_ii):)?((?:数学|物理|化学|生物)(\d+)):(\d+(?:\.\d+)+)/);if(!m||(!m[1]&&m[2].startsWith('数学')))return null;const course=m[1]||SUBJECT_LIST.find(s=>s.legacy===m[2].replace(/\d+$/,''))?.code;const section=LS(m[2])?.sections.find(s=>s.id===m[4]);return section?{course,key:m[2],chapter:Number(m[3]),section:m[4],title:section.t}:null;}
function weak(){const out=new Map();for(const [key,v] of Object.entries(S.checks||{}))if(v<2){const c=contextFromKey(key);if(c)out.set(c.course+key,{...c,reason:v===0?'自评：需重学':'自评：依赖解析'});}for(const [key,v] of Object.entries(S.goalChecks||{}))if(v==='review'){const c=contextFromKey(key);if(c)out.set(c.course+c.key+c.section,{...c,reason:'学习目标需复习'});}return [...out.values()];}
function stats(){const d=ensure(),date=today(),dt=new Date(date+'T12:00'),wd=(dt.getDay()+6)%7;dt.setDate(dt.getDate()-wd);const monday=iso(dt);let weekDone=0;const activity=new Map();const add=(date,n=1)=>{if(/^\d{4}-\d{2}-\d{2}$/.test(date))activity.set(date,(activity.get(date)||0)+n);};
 for(const [date,list] of Object.entries(d.plans)){weekDone+=date>=monday&&date<=today()?list.filter(x=>x.done).length:0;for(const t of list)if(t.done)add(date);}
 d.events.forEach(e=>add(e.date));for(const [k,date] of Object.entries(S.learn))if(!k.startsWith('数学'))add(date);for(const code of math)for(const st of Object.values(S.mathSubjects[code]?.chapters||{}))if(st.learned_at)add(st.learned_at);
 for(const k of Object.keys(S.done||{}))if(S.done[k]){const date=k.slice(0,10);add(date);if(date>=monday&&date<=today())weekDone++;}
 let current=new Date(date+'T12:00');if(!activity.has(date))current.setDate(current.getDate()-1);let streak=0;while(activity.has(iso(current))){streak++;current.setDate(current.getDate()-1);if(streak>10000)break;}
 const minutes=d.events.filter(e=>e.type==='focus'&&e.date===date).reduce((n,e)=>n+(e.seconds||0),0)/60;
 return {weekDone,weekGoal:d.weeklyGoal,weekPercent:Math.min(100,Math.round(weekDone/d.weeklyGoal*100)),streak,minutes,activity};}
window.StudyApp={ensure,courses,units,state,href,record,plan,due,activeErrors,weak,stats,contextFromKey};window.prepareDashboardState=()=>{ensure();window.pauseImportedFocus?.();};ensure();
})();
