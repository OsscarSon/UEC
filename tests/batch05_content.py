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
protect=[x for x in tracked if x.startswith(('data/base-lessons/','data/notes/','lessons/','assets/','data/curriculum.json')) or x in ['data/illustrations.js','data/p0-illustrations.js','data/v22-illustrations.js','ui-polish.css']]
for f in protect:C('protected baseline '+f,subprocess.check_output(['git','show',baseline+':'+f],cwd=R)==(R/f).read_bytes())
C('original142 prompt tasks preserved',json.loads(subprocess.check_output(['git','show',baseline+':illustrations/PROMPTS_BATCH_ALL.json'],cwd=R))['tasks']==json.loads((R/'illustrations/PROMPTS_BATCH_ALL.json').read_text())['tasks'])
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

# Mathematics and chemistry: recompute representative authored results by independent routes.
for name,value,expected,section in [
 ('coordinate distance',math.hypot(4-(-2),9-1),10,'math1.1'),
 ('equidistant point squared distances',(3+1)**2+2**2,(3-5)**2+4**2,'math1.1'),
 ('internal division x',(2*1+7)/3,3,'math1.2'),('external division x',2*7-1,13,'math1.2'),
 ('triangle area',abs((5-1)*(4-1)-(1-1)*(2-1))/2,6,'math1.3'),
 ('polygon shoelace',abs(0*0+4*3+5*3+1*0-(0*4+0*5+3*1+3*0))/2,12,'math1.3'),
 ('slope',(8-2)/(4-1),2,'math1.4'),('perpendicular slope product',(2/3)*(-3/2),-1,'math1.4'),
 ('line through point',3*2-7,-1,'math1.5'),('perpendicular line point',2+2*3-8,0,'math1.5'),
 ('intersection first equation',2+3,5,'math1.6'),('intersection second equation',2*2-3,1,'math1.6'),
 ('point-line distance',abs(3*3+4*4-5)/math.hypot(3,4),4,'math1.7'),
 ('foot on line',3*(3/5)+4*(4/5)-5,0,'math1.7'),
 ('quadratic discriminant',(-3)**2-4*2*(-2),25,'math2.1'),
 ('quadratic roots product',2*(-.5),-1,'math2.1'),
 ('Vieta symmetric square',2**2+.5**2,17/4,'math2.2'),
 ('shifted root polynomial',(3+math.sqrt(5))/2+1+(3-math.sqrt(5))/2+1,5,'math2.2'),
 ('quadratic vertex',2*2**2-8*2+5,-3,'math2.3'),
 ('restricted quadratic minimum',-5**2+4*5+1,-4,'math2.3'),
 ('tangent second contact',(-2)**2-4*(-2)+5,17,'math2.4'),
 ('tangent line at contact',-8*(-2)+1,17,'math2.4'),
 ('polynomial expansion at1',(1+2)*(1-2+3),6,'math3.1'),
 ('remainder linear',2*(.5)**2+3*.5-1,1,'math3.2'),
 ('remainder quadratic plus root',1**3+2*1**2-1+4,6,'math3.2'),
 ('remainder quadratic minus root',(-1)**3+2*(-1)**2-(-1)+4,6,'math3.2'),
 ('factor parameter root1',1+2-1-2,0,'math3.3'),
 ('factor parameter root-2',(-2)**3+2*(-2)**2-(-2)-2,0,'math3.3'),
 ('group factor at4',(4-3)*(4-2)*(4+2),4**3-3*4**2-4*4+12,'math3.4'),
 ('even equation real root',(-2)**4-3*(-2)**2-4,0,'math3.5'),
 ('principal square root',math.sqrt((-2)**2),2,'math4.1'),
 ('rational power',27**(2/3),9,'math4.2'),
 ('negative rational power',16**(-3/4),1/8,'math4.2'),
 ('radical sum',math.sqrt(72)-math.sqrt(32)+math.sqrt(8),4*math.sqrt(2),'math4.3'),
 ('radical equation accepted',math.sqrt(2+2),2,'math4.3'),
 ('rationalized conjugate',1/(math.sqrt(3)+math.sqrt(2)),math.sqrt(3)-math.sqrt(2),'math4.4'),
 ('cubic rationalization',1/(2**(1/3)-1),4**(1/3)+2**(1/3)+1,'math4.4'),
 ('function substitution at0',2*(0+1)**2-3,-1,'math5.1'),
 ('range minimum at vertex',(2-2)**2+1,1,'math5.2'),
 ('range maximum at endpoint',(0-2)**2+1,5,'math5.2'),
 ('transformed point input',3*(3-1),6,'math5.3'),('transformed point output',-2*5+4,-6,'math5.3'),
 ('composition order first',2*(2**2)+1,9,'math5.4'),('composition order reversed',(2*2+1)**2,25,'math5.4'),
 ('linear bijection inverse sample',(7+2)/3,3,'math5.5'),
 ('inverse rational at5',(3*5+1)/(5-2),16/3,'math5.6'),
 ('inverse left parabola sample',2-math.sqrt(10-1),-1,'math5.6'),
 ('organic carbon moles',.44/44,.01,'chem26.1'),('organic hydrogen moles',2*.18/18,.02,'chem26.1'),
 ('organic oxygen mass',.30-.12-.02,.16,'chem26.1'),
 ('chromatography Rf',3/6,.5,'chem26.4'),('purity corrected yield',6*.867/6.5,.8003076923076924,'chem26.4'),
 ('green material accounting',10+30+10,50,'chem26.5'),
 ('allele A frequency',(2*100+60)/(2*200),.65,'bio19.4'),
 ('heterozygous expectation',2*(1-math.sqrt(.04))*math.sqrt(.04),.32,'bio19.4'),
 ('post-bottleneck allele',6/(2*10),.3,'bio19.4'),
 ('offspring proportion',40/(40+30),4/7,'bio19.3')]:
 eq(name,value,expected,section)


# Additional new chapters: units, limiting reagents, polymer end groups and ecological accounts.
for name,value,expected,section in [
 ('normalized water uptake',(12-2)/2,5,'chem1.1'),('isotope weighted mass',12*.75+13*.25,12.25,'chem1.4.1'),
 ('evaporated salt fraction',10/(100-20),.125,'chem1.4.2'),
 ('ice volume',100/.92,108.69565217391305,'chem2.1.1'),('water heating',200*4.2*20,16800,'chem2.1.1'),
 ('metal temperature rise',420/(100*.42),10,'chem2.1.1'),('electrolysis H mass',18/18*2,2,'chem2.1.2'),
 ('zinc hydrogen volume',6.5/65*22.4,2.24,'chem2.2.1'),('acid limiting H2',.15/2,.075,'chem2.2.1'),
 ('zinc remaining',.10-.15/2,.025,'chem2.2.1'),('CuO reduction copper',7.95/79.5*63.5,6.35,'chem2.2.2'),
 ('CuO reduction water',7.95/79.5*18,1.8,'chem2.2.2'),('ammonia mass',.30*2/3*17,3.4,'chem2.2.3'),
 ('fuel cell electrical energy',242*.60,145.2,'chem2.2.3'),('hydrogen storage cubic metres',1000/2*22.4/1000,11.2,'chem2.2.3'),
 ('single alkyne formula H',2*5-2,8,'chem29.1'),('acetylene density',26/22.4,1.1607142857142858,'chem29.3'),
 ('acetylene-air relative density',26/29,.896551724137931,'chem29.3'),('full acetylene hydrogenation',.1*2,.2,'chem29.4'),
 ('carbide limiting water',.1/2,.05,'chem29.5'),('carbide purity volume',10*.8/64*22.4,2.8,'chem29.5'),
 ('carbide isolated yield',2.24/(10*.8/64*22.4),.8,'chem29.5'),
 ('polyethylene number average DP',28000/28,1000,'chem35.1'),('polymer chain amount',14/28000,.0005,'chem35.1'),
 ('number-average relative mass',(1000+3000)/2,2000,'chem35.1'),('break stress MPa',50/2,25,'chem35.3'),
 ('addition polymer isolated mass',14*.8,11.2,'chem35.4.1'),('nylon repeat mass',146+116-2*18,226,'chem35.4.2'),
 ('finite open-chain condensation links',10+10-1,19,'chem35.4.2'),('finite nylon mass',10*(146+116)-19*18,2278,'chem35.4.2'),
 ('PET repeat pairs',19200/(62+166-36),100,'chem35.4.2'),('rubber DP',136000/68,2000,'chem35.5.1'),
 ('ideal copolymer mass',3*54+104,266,'chem35.5.2'),('styrene mass fraction',104/(3*54+104),.39097744360902253,'chem35.5.2'),
 ('cracking ethene mass',10*28,280,'chem35.6'),('population balance',100+20+3-5-8,110,'bio10.1'),
 ('mark recapture',40*50/10,200,'bio10.1'),('logistic total at100',.2*100*(1-100/1000),18,'bio10.1'),
 ('logistic total at500',.2*500*(1-500/1000),50,'bio10.1'),('GPP respiration account',20000-12000,8000,'bio10.3'),
 ('consumer production',1000-400-450,150,'bio10.3'),('ecosystem total production',300*10e6,3e9,'bio10.4')]:
 eq(name,value,expected,section)
# Explicit element-vector sums, independent of displayed equation strings.
for name,left,right in [
 ('water electrolysis',{'H':4,'O':2},{'H':2*2,'O':2}),
 ('sodium and water',{'Na':2,'H':4,'O':2},{'Na':2,'H':2+2,'O':2}),
 ('iron steam magnetite',{'Fe':3,'H':8,'O':4},{'Fe':3,'H':4*2,'O':4}),
 ('carbide hydrolysis',{'Ca':1,'C':2,'H':4,'O':2},{'Ca':1,'C':2,'H':2+2,'O':2}),
 ('acetylene complete combustion',{'C':4,'H':4,'O':10},{'C':4,'H':4,'O':8+2}),
 ('ethylene PVC addition unit',{'C':2,'H':3,'Cl':1},{'C':2,'H':2+1,'Cl':1}),
 ('nylon repeat condensation',{'C':12,'H':10+16,'O':4,'N':2},{'C':12,'H':22+4,'O':2+2,'N':2}),
 ('decane cracking',{'C':10,'H':22},{'C':2+8,'H':4+18})]:
 C('element conservation '+name,left==right)


briefs=json.loads((R/'illustrations/batch05/PROMPTS.json').read_text())['tasks'];C('every new section has independently usable drawing brief',len(briefs)==len(sections) and len({x['id'] for x in briefs})==len(briefs))
for t in briefs:C(t['id']+' complete scientific drawing specification',all(t.get(f) for f in ['subject','chapter_id','section_id','title','teaching_purpose','required_objects','scientific_relations','chinese_labels','formulas_units_variables','composition','dimensions','prompt_zh','prompt_en','negative_prompt','acceptance_criteria','sources','priority','reuse','deterministic_drawing_required','production_status']) and len(t['prompt_zh'])>250 and len(t['prompt_en'])>500)
result=dict(status='pass',actual_counts=actual,independent_numeric_samples=sum('computed' in x['detail'] for x in checks if isinstance(x['detail'],dict)),protected_baseline_files=len(protect),limits='自动结构检查、原数据保护与列明的独立算例；不声称所有题目均独立审校、所有目录已对用户实体书确认，或已获官方/教师审定。',checks=checks)
(R/'reports/batch05/AUDIT_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS',len(checks),'checks;',result['independent_numeric_samples'],'independent numerical samples;',len(sections),'authored sections')
