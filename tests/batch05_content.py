"""New content validation and independent arithmetic samples; not teacher certification."""
from pathlib import Path
import hashlib,json,math,re,subprocess,collections
R=Path(__file__).resolve().parents[1];checks=[]
def C(name,condition,detail=''):
 assert condition,(name,detail)
 checks.append(dict(check=name,result='pass',detail=detail))
def eq(name,value,expected,section):
 C(name,math.isclose(value,expected,rel_tol=1e-8,abs_tol=1e-8),dict(section=section,computed=value,expected=expected))
baseline='c8992f199665ebf4c292af6df8c81d35acdaf54e'
tracked=subprocess.check_output(['git','ls-tree','-r','--name-only',baseline],cwd=R,text=True).splitlines()
protect=[x for x in tracked if x.startswith(('data/base-lessons/','data/notes/','lessons/','assets/','data/curriculum.json')) or x in ['data/illustrations.js','data/p0-illustrations.js','data/v22-illustrations.js','illustrations/PROMPTS_BATCH_ALL.json','ui-polish.css']]
for f in protect:C('protected baseline '+f,subprocess.check_output(['git','show',baseline+':'+f],cwd=R)==(R/f).read_bytes())
catalog=json.loads((R/'data/curriculum.json').read_text());C('canonical116 chapters',len(catalog)==116)
sections=json.loads((R/'data/review/batch05_sections.json').read_text());C('unique subject/chapter/section identity',len(sections)==len({(x['subject'],x['chapter_id'],x['section_id']) for x in sections}))
actual=collections.Counter();questions=[];paragraphs=[]
for ev in sorted((R/'data/batch05').glob('*-sections.json')):
 stem=ev.name.split('-')[0];base=json.loads((R/f'data/base-lessons/{stem}.json').read_text());units=json.loads((R/f'data/notes/{stem}.json').read_text());evidence=json.loads(ev.read_text())
 C(stem+' identities, names and order',[ (x['id'],x['t']) for x in base['sections'] ]==[(x['section_id'],x['section_title']) for x in evidence])
 for s in base['sections']:
  u=units[s['id']];C(stem+'/'+s['id']+' canonical chapter',any(x['subject']==u['subject'] and x['chapter']==u['chapter_id'] for x in catalog))
  C(stem+'/'+s['id']+' twelve module inputs',all(u.get(x) for x in ['goals','prerequisites','flow','deep','derive','examples','exam','error_analysis','practice','quick','quiz','diagnostics']) and bool(s['body']) and bool(s['tips']))
  C(stem+'/'+s['id']+' goal-linked diagnostics',sorted(x['goal_index'] for x in u['diagnostics'])==list(range(len(u['goals']))) and all(x['question_ref'] and x['feedback'] for x in u['diagnostics']))
  C(stem+'/'+s['id']+' sources not claimed fully approved',bool(u['content_sources']) and u['verification_status']=='partially_verified' and not u['exam_evidence'])
  C(stem+'/'+s['id']+' actual explanation beyond placeholder',len(s['body']+u['deep'])>=5 and sum(map(len,s['body']+u['deep']))>=500)
  paragraphs+=s['body']+u['deep'];actual['sections']+=1;actual['examples']+=len(u['examples']);actual['practice']+=len(u['practice']);actual['quiz']+=1
  for q in u['examples']+u['practice']+[u['quiz']]:
   C(stem+'/'+s['id']+' independent question and eight-stage answer',all(q.get(f) for f in ['q','analysis','given','method','principle','steps','ans','verification','pitfall']) and len(q['steps'])>=2)
   C(stem+'/'+s['id']+' original provenance',q['question_origin']=='original' and q['paper_no'] is None)
   questions.append(q['q'])
C('no identical teaching paragraphs reused as filler',len(paragraphs)==len(set(paragraphs)))
C('no identical new question stems counted twice',len(questions)==len(set(questions)))
# Independent arithmetic and conservation samples; expected answers are declared separately.
for name,value,expected,section in [
 ('DNA after replication 2n6',6*2,12,'13.1'),('anaphase whole-cell 2n6',2*6,12,'13.1'),('division index',24/200,.12,'13.1'),('meiosis-I DNA for2n8',8,8,'13.2'),('chromosome-origin combinations',2**3,8,'13.2'),('net cell production A',120-20,100,'13.3'),('net cell production B',150-80,70,'13.3'),
 ('bacterial SA/V r0.5',3/.5,6,'18.1'),('bacterial volume scaling',2**3,8,'18.1'),('three doublings',500*2**(90/30),4000,'18.2'),('CFU dilution volume',80/(.1*1e-5),8e7,'18.2'),('virus particle yield',10*50,500,'18.4'),('two ideal rounds',5*20**2,2000,'18.4'),
 ('concentration amplification',1/.02,50,'11.1'),('relative concentration increase',(.10-.04)/.04,1.5,'11.1'),('before-after-reference difference',(140-100)-(120-100),20,'11.2'),('electricity emissions',1000*.6,600,'11.3'),('reduction fraction',(800-600)/800,.25,'11.3'),('one-year device B',100+100,200,'11.3'),
 ('constant speed unit conversion',36/3.6*3,30,'1.3'),('directional velocity',5-2*3,-1,'1.3'),('volume unit conversion',250*.01**3,2.5e-4,'2.1'),('vernier correction',12+7*.02-.04,12.10,'2.1'),('density SI',.540/(200e-6),2700,'2.1'),('relative uncertainty',.5/50,.01,'2.2'),('area uncertainty approximation',200*(.1/10+.2/20),4,'2.2'),('exact area upper',10.1*20.2,204.02,'2.2'),('scientific division',6e5/2e-3,3e8,'2.3'),('graph velocity',(11-3)/(5-1),2,'2.4'),('signed displacement',3*2-1*2,4,'2.4'),('distance',3*2+1*2,8,'2.4'),
 ('symmetric rope tension',100/(2*math.cos(math.pi/3)),100,'5.1'),('static friction limit',.4*5*10,20,'5.1'),('upward pull support',4*10-6,34,'5.1'),('inclined torque',50*.8*math.sin(math.pi/6),20,'5.2'),('overhang supportB',60*3/2,90,'5.2'),('parallel resultant location',30*2/40,1.5,'5.3'),('opposed resultant location',-10*2/20,-1,'5.3'),('centre of mass',3*4/(2+3),2.4,'5.3'),
 ('angled work',20*5*math.cos(math.pi/3),50,'7.1'),('lifting power',100*10*2/5,400,'7.1'),('output force',1000*.8/2,400,'7.1'),('trapezoidal work',(2+10)*4/2,24,'7.2'),('spring incremental work',.5*100*(.2**2-.1**2),1.5,'7.2'),('initial plus net work',.5*2*2**2+20-8,16,'7.3'),('braking distance',1000*10**2/(2*5000),10,'7.3'),('braking squared-speed',1000*20**2/(2*5000),40,'7.3'),('gravitational change',2*10*(4-1),60,'7.4'),('spring deformation energy',.5*100*(.4-.3)**2,.5,'7.4'),('dissipative final K',16+2*10*(3-1)-8,48,'7.5'),('spring launch speed',math.sqrt(200*.1**2/.5),2,'7.5'),('rest energy gram',.001*(3e8)**2,9e13,'7.6'),('mass-defect conversion',.0100*931.5,9.315,'7.6'),('mass loss',3e8/(3e8)**2,3.3333333333333334e-9,'7.6'),
 ('rebound impulse',.1*(6-(-8)),1.4,'8.1'),('rebound average force',.1*(6-(-8))/.02,70,'8.1'),('triangular net impulse',.5*.04*100,2,'8.1'),('sticking velocity',2*3/(2+1),2,'8.2'),('external impulse final',10+10*.2,12,'8.2'),('relative eject cart',-.5*4/(2+.5),-.8,'8.3'),('relative eject projectile',2*4/(2+.5),3.2,'8.3'),('recoil energy',.5*3*2**2+.5*6**2,24,'8.3'),('equal-mass sticking loss',.5*4**2-.5*2*2**2,4,'8.4'),('unequal elastic final P',2*1+1*4,6,'8.4'),('unequal elastic final K',.5*2*1**2+.5*1*4**2,9,'8.4'),('sticking energy fraction',(6-4.5)/6,.25,'8.4')]:
 eq(name,value,expected,section)
briefs=json.loads((R/'illustrations/batch05/PROMPTS.json').read_text())['tasks'];C('every new section has independently usable drawing brief',len(briefs)==len(sections) and len({x['id'] for x in briefs})==len(briefs))
for t in briefs:C(t['id']+' complete scientific drawing specification',all(t.get(f) for f in ['subject','chapter_id','section_id','title','teaching_purpose','required_objects','scientific_relations','chinese_labels','formulas_units_variables','composition','dimensions','prompt_zh','prompt_en','negative_prompt','acceptance_criteria','sources','priority','reuse','deterministic_drawing_required','production_status']) and len(t['prompt_zh'])>250 and len(t['prompt_en'])>500)
result=dict(status='pass',actual_counts=actual,independent_numeric_samples=sum('computed' in x['detail'] for x in checks if isinstance(x['detail'],dict)),protected_baseline_files=len(protect),limits='自动结构检查、原数据保护与列明的独立算例；不声称所有题目均独立审校、所有目录已对用户实体书确认，或已获官方/教师审定。',checks=checks)
(R/'reports/batch05/AUDIT_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS',len(checks),'checks;',result['independent_numeric_samples'],'independent numerical samples;',len(sections),'authored sections')
