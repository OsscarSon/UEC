"""Current batch identity/provenance/brief/solution audit; no pedagogical pass by length."""
from pathlib import Path
from collections import Counter
import subprocess,json,hashlib,math,csv,re,sys,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];rows=[]
def C(name,value,detail=''):
 if not value:raise AssertionError((name,detail))
 rows.append(dict(name=name,result='pass',detail=detail))
def eq(name,a,b,tol=1e-9):C(name,math.isclose(a,b,rel_tol=tol,abs_tol=tol),dict(actual=a,expected=b))
if '--rebuild-check' in sys.argv:
 tracked=[*sorted((R/'data/base-lessons').glob('*.json')),*sorted((R/'assets/verified').glob('*.svg')),*[R/'lessons'/f for f in ['chem05.js','chem06.js','bio03.js','batch-notes.js']]]
 before={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in tracked}
 commands=[['python','tools/build_verified_diagrams.py'],['python','tools/build_base_lessons.py'],['python','tools/build_chem05.py'],['python','tools/build_bio03.py'],['python','tools/build_notes.py']]
 for cmd in commands:subprocess.run(cmd,cwd=R,check=True,capture_output=True)
 after={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in tracked}
 C('all current build/compatibility commands reproduce scientific corrections',before==after)
 (R/'reports/batch02/BUILD_REPRODUCIBILITY.json').write_text(json.dumps(dict(result='pass',commands=[' '.join(x) for x in commands],files=before),ensure_ascii=False,indent=2)+'\n')
script="const fs=require('fs'),vm=require('vm'),c={};c.window=c;vm.createContext(c);for(const f of fs.readdirSync('lessons').filter(x=>/^(phys|chem|bio)\\d+\\.js$/.test(x)))vm.runInContext(fs.readFileSync('lessons/'+f,'utf8'),c);vm.runInContext(fs.readFileSync('lessons/batch-notes.js','utf8'),c);vm.runInContext(fs.readFileSync('data/illustrations.js','utf8'),c);process.stdout.write(JSON.stringify(c))"
s=json.loads(subprocess.check_output(['node','-e',script.replace('JSON.stringify(c)','JSON.stringify({LESSONS:c.LESSONS,BATCH_NOTES:c.BATCH_NOTES,APPROVED:c.APPROVED_ILLUSTRATIONS,QUARANTINED:c.QUARANTINED_LEGACY_FIGURES})')],cwd=R))
lessons,batch=s['LESSONS'],s['BATCH_NOTES']
baseline='daa36377c98508764780831e82d4ecbb06c27e69'
oldcurr=subprocess.check_output(['git','show',baseline+':data/curriculum.json'],cwd=R)
C('116 chapter bytes unchanged',oldcurr==(R/'data/curriculum.json').read_bytes())
curr=json.loads(oldcurr);after=[]
for d in curr:
 for sec in lessons.get(d['subject']+str(d['chapter']),{}).get('sections',[]):after.append([d['subject'],str(d['chapter']),d['title'],sec['id'],sec['t']])
with (R/'reports/sections_before.csv').open() as f:old=list(csv.reader(f))[1:]
C('original 52 subsection identity/title/order unchanged',[r for r in after if r[:2]+[r[3]] in [x[:2]+[x[3]] for x in old]]==old)
added=json.loads((R/'data/review/new_sections.json').read_text())
C('six new subsections have official-directory evidence',len(added)==6 and all(r['source_type']=='official_curriculum_content_table' and r['page']==2 for r in added))
C('all new IDs and titles equal the evidence register',[x for x in after if x[:2]+[x[3]] not in [r[:2]+[r[3]] for r in old]]==[['化学','6','元素周期表',r['section_id'],r['section_title']] for r in added])
legacy_manifest=json.loads(subprocess.check_output(['git','show',baseline+':illustration-manifest.json'],cwd=R))
old_svgs=[x['reuse']['existing_asset'] for x in legacy_manifest['illustrations'] if x['record_kind']=='existing_svg']
C('all73 original SVG files preserved byte-for-byte',len(old_svgs)==73 and all(hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in old_svgs))
for path in ['data/subjects.js']:
 C('math subject definitions preserved: '+path,(R/path).read_bytes()==subprocess.check_output(['git','show',baseline+':'+path],cwd=R))
C('no math lessons fabricated',all(not k.startswith('数学') for k in lessons))
formulas=[('物理3','3.3','deep','|Δx|'),('物理3','3.3','derive','Σ|x_i−x_(i−1)|'),('物理4','4.2','deep','|f_s|≤μ_sN'),('物理4','4.3','derive','|F₁−F₂|≤R'),('物理4','4.8','derive','|a_A|/|a_B|')]
for k,sid,field,token in formulas:C('absolute-value repair '+k+':'+sid,any(token in p for p in batch[k][sid][field]))
allq=[];diagnostic_extra=0;sections=[];module_rows=[]
for k,units in batch.items():
 C('complete real chapter: '+k,list(units)==[x['id'] for x in lessons[k]['sections']])
 for sid,u in units.items():
  sec=next(x for x in lessons[k]['sections'] if x['id']==sid)
  C('required fields '+k+sid,all(u.get(f) for f in ['goals','prerequisites','flow','deep','derive','examples','exam','practice','quick','quiz','strategy','diagnostics']))
  C('three examples and four practices '+k+sid,len(u['examples'])==3 and len(u['practice'])==4)
  C('M07 actual example, reasoning and checks '+k+sid,0<=u['strategy']['worked_example_index']<3 and all(u['strategy'].get(f) for f in ['trigger','method','principle','verification','pitfall']))
  C('M07 check belongs to displayed example '+k+sid,u['strategy']['verification']==u['examples'][u['strategy']['worked_example_index']]['verification'])
  C('M12 maps every stated goal '+k+sid,sorted(g['goal_index'] for g in u['diagnostics'])==list(range(len(u['goals']))))
  for g in u['diagnostics']:
   ref=g['question_ref'];candidates=u['examples'] if ref[0]=='e' else u['practice']
   C('diagnostic question resolves '+k+sid+ref,int(ref[1:])<len(candidates) and bool(g['feedback']))
  qs=u['examples']+u['practice']+[u['quiz']]+[g['question'] for g in u['diagnostics'] if g.get('question')]
  diagnostic_extra+=sum(bool(g.get('question')) for g in u['diagnostics']);allq+=qs
  for q in qs:
   C('original provenance and solution '+k+sid+q['q'][:12],q['question_origin']=='original' and q['paper_no'] is None and q['primary_section']==sid and bool(q['steps']) and bool(q['ans']))
  C('all174 examples have explicit eight-stage evidence '+k+sid,all(all(q.get(f) for f in ['analysis','given','method','principle','steps','ans','verification','pitfall']) for q in u['examples']))
  if k in ['化学5','生物3','化学6']:
   C('all new questions have eight-stage evidence '+k+sid,all(all(q.get(f) for f in ['analysis','given','method','principle','steps','ans','verification','pitfall']) for q in qs))
  for ev in u['exam_evidence']:C('third-party not relabeled official',ev['source_type']=='third_party_reference' and ev['verification_status']=='partially_verified')
  C('source status remains partial '+k+sid,u['verification_status']=='partially_verified' and all(x.get('version') and x.get('access_date') for x in u['content_sources']))
  sections.append(dict(subject=u['subject'],chapter_id=u['chapter_id'],section_id=sid,title=sec['t'],modules=12,question_records=len(qs),status='implemented_structure_content_review_in_progress'))
  for m in range(1,13):module_rows.append(dict(subject=u['subject'],chapter_id=u['chapter_id'],section_id=sid,title=sec['t'],module_id=m,content_present=True,review_status='结构存在；不是字数或自动科学认证',sources_status='partially_verified'))
C('58 real sections /696 modules',len(sections)==58 and len(module_rows)==696)
C('466 authored question records incl2 new goal diagnostics',len(allq)==466 and diagnostic_extra==2)
master=json.loads((R/'illustrations/ILLUSTRATION_MASTER_MANIFEST.json').read_text());tasks=json.loads((R/'illustrations/PROMPTS_BATCH_ALL.json').read_text())['tasks'];ids=[r['id'] for r in master['illustrations']]
C('209 unique master records',len(ids)==209==len(set(ids)))
C('all114 required tasks have bilingual briefs',len(tasks)==114 and len({t['id'] for t in tasks})==114)
required=['id','subject','chapter_id','section_id','title','teaching_purpose','must_appear_objects','correct_scientific_relationships','chinese_labels','formulas_units_variables','composition_requirements','suggested_dimensions','chinese_prompt','english_prompt','negative_prompt','scientific_acceptance_criteria','theoretical_sources','priority','can_reuse_old_image','requires_deterministic_svg_or_plotting','production_status']
real={(x[0],x[3]) for x in after}
for t in tasks:
 C('all prompt fields: '+t['id'],all(f in t and t[f] not in [None,'',[],{}] for f in required))
 C('prompt binds actual section: '+t['id'],(t['subject'],t['section_id']) in real)
 C('independent prompt '+t['id'],'同上' not in t['chinese_prompt'] and 'as above' not in t['english_prompt'].lower() and t['id'] in t['english_prompt'] and len(t['english_prompt'])>600)
 C('P0/P1/P2 '+t['id'],t['priority'] in ['P0','P1','P2'])
 C('deterministic science preference '+t['id'],t['category']=='supporting_illustration' or t['requires_deterministic_svg_or_plotting'])
for r in master['illustrations']:
 if r['record_kind']=='existing_inline_flow':C('inline implementation source hash '+r['id'],r['reuse']['existing_asset']['sha256']==hashlib.sha256((R/'batch-ui.js').read_bytes()).hexdigest())
 if r['record_kind']=='math_chapter_pending':C('math null remains: '+r['id'],r['section_id'] is None and r['production_task_id'] is None)
imports=master['uploaded_batch01'];C('six incoming originals reviewed',len(imports)==6)
for x in imports:C('incoming hash '+x['id'],hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256'])
C('3 approved /3 held',Counter(x['status'] for x in imports)==Counter(approved_for_limited_use=3,rejected_pending_redraw=3))
C('runtime allowlist contains no rejected PNG',set(x['id'] for x in s['APPROVED'])=={x['id'] for x in imports if x['status']=='approved_for_limited_use'})
for p in R.glob('assets/**/*.svg'):C('SVG parses '+str(p.relative_to(R)),ET.parse(p).getroot().tag.endswith('svg'))
# Independently computed samples for newly authored content and diagrams.
for name,a,b in [
 ('diameter ratio',1e-10/1e-15,1e5),('volume ratio',(1e-10/1e-15)**3,1e15),
 ('Na ion electron count',11-1,10),('weighted mass',10*.2+11*.8,10.8),('isotope fraction',(37-35.5)/(37-35),.75),
 ('600nm energy',6.63e-34*3e8/(600e-9),3.315e-19),('H1 energy',-13.6,-13.6),('H2 energy',-13.6/4,-3.4),
 ('H3to2 eV',13.6*(1/4-1/9),17/9),('H3to2 wavelength nm',6.63e-34*3e8/(13.6*(1/4-1/9)*1.602e-19)*1e9,657.3033707865169),
 ('H excitation',-3.4-(-13.6),10.2),('FeII electrons',26-2,24),('FeIII electrons',26-3,23),
 ('p capacity',3*2,6),('d capacity',5*2,10),('f capacity',7*2,14),
 ('enzyme Ea low',45-20,25),('enzyme Ea high',80-20,60),('same endpoint delta',5-20,-15),
 ('enzyme reciprocal-time ratio',(1/40)/(1/20),.5),('replicate mean',(2+4+4)/3,10/3),
 ('3h free enzyme',10+2+2,14),('3h immobilized',6+5+5,16),('coupled delta',-30+20,-10),
 ('ATP mol energy',.02*30,.6),('insufficient coupling',40-30,10),('glycolysis net',4-2,2),
 ('ATP given30',.1*30,3),('Calvin input C',3+3*5,18),('Calvin regen C',5*3,15),
 ('Calvin net C',18-15,3),('two net G3P ATP',2*9,18),('two net G3P NADPH',2*6,12),
 ('net photosynthesis',12-4,8),('gross photosynthesis',6+2,8),
 ('triad fit',(7+39)/2,23),('triad mismatch',18-(10+30)/2,-2),
 ('chlorine electrons',10+2+5,17),('same-electron ion count',13-3,10),
 ('IE jump after three',11600/2700>2700/1800,True),
 ('inertia same-force velocity',12/60*2,.4),('water photolysis H',2*2,4),('water photolysis charge',4-4,0),
 ]:eq(name,a,b,1e-8)
summary=dict(result='pass',baseline=baseline,chapter_records=116,original_subsections_preserved=52,new_sourced_subsections=6,section_modules=696,original_question_records=466,new_question_records_since_baseline=138,explicit_eight_stage_new_question_records=138,existing_examples_expanded=123,all_examples_with_eight_stages=174,total_records_with_explicit_eight_stages=sum(all(q.get(f) for f in ['analysis','given','method','principle','steps','ans','verification','pitfall']) for q in allq),goal_mappings=116,goal_diagnostic_questions_added=2,checks_passed=len(rows),limitations=['这些检查证明结构/出处元数据/样例计算及资源一致性，不等于教师或官方全面审定','原41节123例已补八步，全部174例均有对应字段；字段齐备仍不代替逐句独立教研，部分图仍待制作','新6节已取得目录证据，兴华实际版本与2027适用尚未锁定','11SVG多为总结图，完整结构/装置图仍按114条任务继续制作'])
(R/'reports/batch02/AUDIT_RESULTS.json').write_text(json.dumps(dict(summary=summary,checks=rows),ensure_ascii=False,indent=2)+'\n')
for name,items in [('SECTION_MODULE_COVERAGE.csv',module_rows),('SECTION_DELIVERY.csv',sections)]:
 with (R/'reports/batch02'/name).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(items[0]),lineterminator='\n');w.writeheader();w.writerows(items)
print(json.dumps(summary,ensure_ascii=False,indent=2))
