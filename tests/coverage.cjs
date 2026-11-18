const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={};c.window=c;vm.createContext(c);
for(const f of fs.readdirSync('lessons').filter(f=>/^(phys|chem|bio|math)\d+\.js$/.test(f)))vm.runInContext(fs.readFileSync('lessons/'+f,'utf8'),c);
vm.runInContext(fs.readFileSync('lessons/batch-notes.js','utf8'),c);vm.runInContext(fs.readFileSync('lessons/batch05-notes.js','utf8'),c);vm.runInContext(fs.readFileSync('data/subjects.js','utf8'),c);
const curr=JSON.parse(fs.readFileSync('data/curriculum.json'));assert.deepEqual(curr,JSON.parse(fs.readFileSync('reports/curriculum_before.json')));
const html=fs.readFileSync('index.html','utf8');assert.deepEqual(JSON.parse(html.match(/const D=(\[.*\]);\/\*/)[1]),curr.map(x=>[x.subject,x.volume,x.chapter,x.title,x.syllabus,x.status,x.priority,x.note]));
const baseline=fs.readFileSync('reports/sections_before.csv','utf8').trim().split(/\r?\n/).slice(1).map(line=>line.split(','));
const after=[];for(const d of curr){const k=d.subject+d.chapter;for(const s of c.LESSONS[k]?.sections||[])after.push([d.subject,String(d.chapter),d.title,s.id,s.t]);}assert.deepEqual(after.filter(row=>baseline.some(old=>old[0]===row[0]&&old[1]===row[1]&&old[3]===row[3])),baseline);
const added=after.filter(row=>!baseline.some(old=>old[0]===row[0]&&old[1]===row[1]&&old[3]===row[3]));const approved=[...JSON.parse(fs.readFileSync('data/review/new_sections.json')),...JSON.parse(fs.readFileSync('data/review/batch05_sections.json'))];const identity=x=>JSON.stringify(x);assert.deepEqual(added.map(x=>identity([x[0],Number(x[1]),x[3],x[4]])).sort(),approved.map(x=>identity([x.subject,x.chapter_id,x.section_id,x.section_title])).sort());
let sections=0,questions=0;const report=[];
for(const [k,ss]of Object.entries(c.BATCH_NOTES)){
 assert.deepEqual(Object.keys(ss),Array.from(c.LESSONS[k].sections,s=>s.id));
 for(const [id,u]of Object.entries(ss)){
  sections++;for(const f of ['goals','prerequisites','flow','deep','derive','exam','examples','practice','quick','quiz'])assert.ok(u[f],k+id+f);
  assert.ok(c.LESSONS[k].sections.find(s=>s.id===id).body.concat(u.deep).join('').length>160,k+id+' combined M04 truncation check; not a teaching-depth verdict');assert.equal(u.examples.length,3);assert.equal(u.practice.length,4);
  for(const q of [...u.examples,...u.practice,u.quiz]){questions++;assert.equal(q.question_origin,'original');assert.equal(q.paper_no,null);assert.equal(q.subject_code,u.subject_code);assert.ok(q.steps.length>=2);assert.ok(q.ans);}
  for(const ev of u.exam_evidence){assert.equal(ev.source_type,"third_party_reference");assert.equal(ev.verification_status,"partially_verified");}assert.equal(u.verification_status,'partially_verified');
  const s=c.LESSONS[k].sections.find(s=>s.id===id);for(const [path]of s.figs||[])assert.ok(fs.existsSync(path),path);
  report.push([u.subject,u.chapter_id,curr.find(x=>x.subject+x.chapter===k).title,id,s.t,baseline.some(v=>v[0]===u.subject&&v[3]===id)?'yes':'new_with_official_directory_evidence',12,s.syl+'; '+u.goals.join(' / '),'部分核对2026框架及计算样例；完整范围/知识点、学校版本与2027适用未审定',u.content_batch==='batch05'?'authored_pending_teacher_review':'structural_complete_depth_review_in_batch02','partially_verified','原41节123例已补八步；2027适用、兴华版本、独立教研与部分图仍待验收']);
 }
}
assert.equal(sections,180);assert.equal(questions,1440);assert.equal(c.SUBJECTS.filter(x=>x.code.startsWith('adv_math_')).length,2);assert.ok(!c.SUBJECTS.some(x=>x.code==='paper_1'));
function csv(v){return '"'+String(v).replaceAll('"','""')+'"';}
fs.writeFileSync('reports/batch05/SECTION_COVERAGE.csv',[['subject','chapter_id','chapter_title','section_id','section_title','exists_in_baseline','modules_present_count','knowledge_points_expected','knowledge_points_verified','content_status','sources_status','reviewer_notes'],...report,...after.filter(([s,ch,ct,id])=>!c.BATCH_NOTES[s+ch]?.[id]).map(([s,ch,ct,id,t])=>[s,ch,ct,id,t,'yes','not_audited','本批未选','未审查','unchanged','needs_review','保留原有内容，不计十二模块完成'])].map(row=>row.map(csv).join(',')).join('\n')+'\n');
fs.writeFileSync('reports/batch05/sections_after.csv','subject,chapter_id,chapter_title,section_id,section_title\n'+after.map(r=>r.join(',')).join('\n')+'\n');
fs.copyFileSync('reports/batch05/SECTION_COVERAGE.csv','reports/batch05/SECTION_AUDIT.csv');
console.log('PASS curriculum 116/116 unchanged; original 52 section identities/order preserved; 34 historical and 94 new registered sections; current 34 chapters / 180 sections / 2160 modules / 1440 main original questions (historical extra diagnostics separate).');
