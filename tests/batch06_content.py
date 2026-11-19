"""Structural protection and independently recomputed arithmetic for batch06."""
from pathlib import Path
import json,subprocess,math,collections
import sympy as sp
R=Path(__file__).resolve().parents[1];OUT=R/'reports/batch06';OUT.mkdir(exist_ok=True)
checks=[]
def C(name,ok,detail=None):
 assert ok,(name,detail)
 checks.append(dict(name=name,result='pass',detail=detail))
baseline='df94dd51fd7b14514eb6036af33de1228b969883'
paths=subprocess.check_output(['git','ls-tree','-r','--name-only',baseline],cwd=R,text=True).splitlines()
protected=[p for p in paths if p.startswith(('lessons/','assets/','data/base-lessons/','data/notes/','ui/','vendor/')) or p in ['data/curriculum.json','data/subjects.js','data/math-courses.js']]
for p in protected:
 C('preserved '+p,subprocess.check_output(['git','show',baseline+':'+p],cwd=R)==(R/p).read_bytes())
curr=json.loads((R/'data/curriculum.json').read_text());C('canonical116',len(curr)==116)
raw=json.loads((R/'sources/batch06/official-directory-index.json').read_text())
for path in ['physics-directory-index.json','math-directory-index.json']:raw+=json.loads((R/'sources/batch06'/path).read_text())
prior={p for p in paths if p.startswith('lessons/')};allq=[];paragraphs=[];counts=collections.Counter();audit=[]
for ev in sorted((R/'data/batch06').glob('*-sections.json')):
 stem=ev.name.split('-')[0];b=json.loads((R/f'data/base-lessons/{stem}.json').read_text());n=json.loads((R/f'data/notes/{stem}.json').read_text());rows=json.loads(ev.read_text())
 C(stem+' genuinely new chapter','lessons/'+stem+'.js' not in prior)
 C(stem+' real chapter',any(x['subject']==rows[0]['subject'] and x['chapter']==rows[0]['chapter_id'] for x in curr))
 C(stem+' exact identities',[(x['id'],x['t']) for x in b['sections']]==[(x['section_id'],x['section_title']) for x in rows])
 if rows[0]['subject'] in ['化学','生物','物理','数学']:
  rr=[r for r in raw if r['subject']==rows[0]['subject'] and r['chapter_id']==rows[0]['chapter_id']]
  leaves=[r for r in rr if not any(t['section_id'].startswith(r['section_id']+'.') for t in rr)]
  C(stem+' all independently transcribed directory leaf rows represented',[(r['section_id'],r['section_title']) for r in leaves]==[(s['id'],s['t']) for s in b['sections']])
 for s in b['sections']:
  u=n[s['id']];key=u['subject']+s['id'];text=s['body']+u['deep'];size=sum(map(len,text))
  C(key+' module inputs',all(u.get(k) for k in ['goals','prerequisites','flow','deep','derive','examples','exam','error_analysis','practice','quick','quiz','diagnostics']))
  C(key+' explanatory paragraphs',len(text)>=6 and size>=500,size)
  C(key+' examples and practice',len(u['examples'])>=3 and len(u['practice'])>=4)
  C(key+' goal feedback',sorted(d['goal_index'] for d in u['diagnostics'])==list(range(len(u['goals']))))
  C(key+' honest verification',u['verification_status']=='partially_verified' and not u['exam_evidence'])
  for q in u['examples']+u['practice']+[u['quiz']]:
   C(key+' full answer stages',all(q.get(k) for k in ['q','given','analysis','method','principle','steps','ans','verification','pitfall']) and len(q['steps'])>=2)
   C(key+' standalone assumptions',q['given'] in q['q'])
   C(key+' original not official',q['question_origin']=='original' and q['paper_no'] is None)
   allq.append(q['q'])
  audit.append(dict(subject=u['subject'],chapter=u['chapter_id'],section=s['id'],title=s['t'],explanatory_characters=size,paragraphs=len(text),examples=len(u['examples']),practice=len(u['practice']),module_inputs=12,review_status='structural_pass_scientific_review_pending',teacher_approved=False))
  paragraphs+=text;counts['sections']+=1;counts['examples']+=len(u['examples']);counts['practice']+=len(u['practice']);counts['quiz']+=1
 counts['chapters']+=1
C('no identical teaching paragraphs',len(paragraphs)==len(set(paragraphs)))
C('no repeated question stems counted twice',len(allq)==len(set(allq)))
# Recompute domains with symbolic algebra rather than comparing rendered answer strings.
x=sp.symbols('x',real=True)
for name,condition,expected in [
 ('6.1 negative multiplier',-3*x+4<=10,sp.Interval(-2,sp.oo)),
 ('6.1 absolute bound',sp.Abs(2*x-1)<5,sp.Interval.open(-2,3)),
 ('6.2 two roots',x*x-5*x+6<=0,sp.Interval(2,3)),
 ('6.2 negative leading term',-x*x+4*x-3>0,sp.Interval.open(1,3)),
 ('6.2 repeated root',(x-3)**2<=0,sp.FiniteSet(3)),
 ('6.2 no real root',x*x+x+1<0,sp.EmptySet),
 ('6.3 denominator exclusion',(x-2)/(x+1)>=0,sp.Union(sp.Interval.open(-sp.oo,-1),sp.Interval(2,sp.oo))),
 ('6.3 constant shift',1/(x-1)>2,sp.Interval.open(1,sp.Rational(3,2))),
 ('6.3 even multiplicity',(x-1)**2/(x+1)>0,sp.Union(sp.Interval.open(-1,1),sp.Interval.open(1,sp.oo))),
]:
 C(name,sp.solve_univariate_inequality(condition,x,relational=False)==expected)
def N(name,value,expected,tol=1e-10):C(name,math.isclose(float(value),expected,rel_tol=tol,abs_tol=abs(expected)*tol if expected else tol),dict(computed=float(value),expected=expected))
for name,val,ans in [
 ('quadratic vertex k-bound',sp.expand((x+1)**2-1)-(x*x+2*x),0),
 ('LP four vertices max',max(3*a+2*b for a,b in [(0,0),(4,0),(2,2),(0,3)]),12),
 ('integer LP complete enumeration',max(a+2*b for a in range(4) for b in range(3) if 2*a+3*b<=7),4),
 ('rate concentration',(.8-.5)/20,.015),
 ('stoichiometric rate',.06/2,.03),
 ('surface split area ratio',(8*6*1**2)/(6*2**2),2),
 ('second-order concentration ratio',.016/.004,4),
 ('Arrhenius exponent rounded as authored',round(50000/8.314*(1/300-1/310),3),.647),
 ('catalysis enthalpy',-10-20,-30),
 ('catalysis barriers ratio',(80-20)/(50-20),2),
 ('A/B equilibrium',.8/.2,4),
 ('2A/B equilibrium',.25/.5**2,1),
 ('physical root exclusion',1-2*1,-1),
 ('after A addition A',sp.Rational(2,5)-sp.Rational(2,15),4/15),
 ('after A addition B',sp.Rational(2,5)+sp.Rational(2,15),8/15),
 ('compression reaction quotient factor',2/2**2,.5),
 ('two-pass original material converted',30+.3*70,51),
 ('heterozygote among dominant',.5/.75,2/3),
 ('at least one recessive',1-(3/4)**2,7/16),
 ('three recessive children',(.25)**3,1/64),
 ('X-linked joint',.5*.5,.25),
 ('DNA total nucleotides',100*2,200),
 ('DNA hydrogen bonds',40*3+60*2,240),
 ('original strand fraction after3',2/2**3,.25),
 ('DNA after4 from2',2*2**4,32),
 ('translation dipeptide bonds',2-1,1),
 ('PCR6 total',5*2**6,320),
 ('PCR6 new',5*(2**6-1),315),
 ('PCR threshold previous',10*2**6,640),
 ('PCR threshold next',10*2**7,1280),
 ('PCR partial efficiency',100*1.5**2,225),
 ('linear DNA length',1000+2500+2500,6000),
 ('circular DNA length',1500+4500,6000),
 ('habitat relative loss',(1000-700)/1000,.3),
 ('CPUE decline',(10-800/200)/10,.6),
 ('control adjusted gain',(140-100)-(120-100),20),
 ('single molecule mass',round(.018/(6.02e23),28),2.99e-26),
 ('molecular occupied volume',2.4e-3/(.1*6e23),4e-26),
 ('molecular spacing nm',round((4e-26)**(1/3)/1e-9,2),3.42),
 ('oil film nm',1e-9/2/1e-9,.5),
 ('rod stress MPa',100/(.5e-6)/1e6,200),
 ('rod extension mm',100*2/(1e11*.5e-6)*1000,4),
 ('elastic work',.5*100*.004,.2),
 ('soap film force',2*.03*.05,.003),
 ('capillary height cm',2*.072/(1000*10*.0005)*100,2.88),
 ('Celsius to Kelvin',25+273.15,298.15),
 ('thermometer calibration',100*(10-2)/(22-2),40),
 ('thermometer resolution',.1/(20/100),.5),
 ('water mixing temperature',(.1*80+.2*20)/.3,40),
 ('metal specific heat',round((.2*4200+100)*5/(.1*75),1),626.7),
 ('three-stage ice heat',.1*2100*10+.1*334000+.1*4200*20,43900),
 ('partly melted ice',16700/334000,.05),
 ('rod thermal extension mm',12e-6*2*50*1000,1.2),
 ('hole radius increase mm',20e-6*10*100,.02),
 ('overflow mL',(.001-.00003)*1000*20,19.4),
 ('liquid density',round(1000/1.02,2),980.39),
 ('AB solubility',math.sqrt(1e-10),1e-5),
 ('AB2 solubility',round((4e-12/4)**(1/3),8),1e-4),
 ('common ion solubility',1e-10/.1,1e-9),
 ('mixed ion product',(.002/2)**2,1e-6),
 ('BX2 precipitation threshold',round(math.sqrt(1e-5/.01),4),.0316),
 ('precipitate conversion K',1e-10/1e-13,1000),
 ('conduction slab',.8*2*15/.020,1200),
 ('series thermal resistance',20/(.1/.2+.05/.1),20),
 ('conduction heat',30*2*3600,216000),
 ('convection given h',10*.5*20,100),
 ('radiative emission',5.67e-8*300**4,459.27),
 ('radiation doubled Kelvin',(600/300)**4,16),
 ('point source distance doubled',1/2**2,.25),
]:N(name,val,ans,1e-8)
counts=dict(counts);counts['original_questions']=len(allq)
(OUT/'CONTENT_CHECKS.json').write_text(json.dumps(dict(status='pass',baseline=baseline,protected_files=len(protected),counts=counts,checks=checks,limits='Arithmetic/domain samples and structure only; not official or teacher approval.'),ensure_ascii=False,indent=2)+'\n')
(OUT/'DEPTH_SIGNALS.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print('PASS',counts,';',len(protected),'prior files protected;',len(checks),'assertions')

