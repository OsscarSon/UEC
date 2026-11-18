"""Independent arithmetic and equation ledgers plus immutable previous-course checks."""
import json,math,re,subprocess,csv,hashlib
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1];O=R/'reports/batch04';O.mkdir(exist_ok=True)
units={};bases={}
for ch in range(7,12):
 d=json.loads((R/f'data/notes/chem{ch:02}.json').read_text());b=json.loads((R/f'data/base-lessons/chem{ch:02}.json').read_text());units.update(d);bases.update({x['id']:x for x in b['sections']})
assert len(units)==28
# No re-audit of history: compare directly to the previously accepted PR HEAD.
for path in ['data/curriculum.json','data/subjects.js','data/illustrations.js','data/p0-illustrations.js']:
 assert (R/path).read_bytes()==subprocess.check_output(['git','show','a690a1a:'+path],cwd=R),path
for p in (R/'assets/fig').glob('*.svg'):assert p.read_bytes()==subprocess.check_output(['git','show','a690a1a:'+str(p.relative_to(R))],cwd=R)
for stem in ['phys03','phys04','chem03','chem04','chem05','chem06','bio01','bio02','bio03']:
 path=f'data/notes/{stem}.json';assert (R/path).read_bytes()==subprocess.check_output(['git','show','a690a1a:'+path],cwd=R),path
samples=[
('7.1.1:e0',2+2*(-1),0,'MgCl₂'),('7.1.1:e1',2*3+3*(-2),0,'Al₂(SO₄)₃'),
('7.1.2:e0',4+2*6,16,'16'),('7.1.2:e1',5+4-1,8,'NH₄'),('7.1.3:e0',100*1,100,'100'),
('7.3.1:e0',8/8,1,'AB'),('7.3.1:e2',4*58.5/(6e23*9e-23),13/3,'4.33'),
('7.3.2:e0',4/2,2,'1∶2'),('7.3.2:e1',1000*4/2,2000,'2000'),
('7.3.3:e0',.5*2,1,'1.00'),('7.3.4:e0',8/8+1,2,'2'),('7.3.4:e1',8/8+6/2,4,'4'),('7.3.4:e2',2**(1/3),1.2599210498948732,'1.260'),
('8.1:e0',2-0,2,'2'),('8.1:e2',2*1,2,'2mol'),('8.2.1:e0',-2-4*(-2),6,'+6'),('8.2.1:e1',-2/2,-1,'−1'),('8.2.1:e2',8/3,2.6666666666666665,'不能'),
('8.2.2:e0',2*(6-3),6,'6mol'),('8.2.2:e1',1*(1-0),1,'1电子'),('8.2.2:e2',2*(0-(-2)),4,'4mol'),('8.3:e2',.01-.03/5,.004,'0.004'),
('8.4.1:e0',2*3,6,'1∶3∶2∶3'),('8.4.1:e1',2*6,12,'2∶2∶3'),('8.4.1:e2',-1+5*2+8,17,'1、5、8'),('8.4.2:e0',-1+8-5,2,'5e⁻'),('8.4.2:e1',-1-3,-4,'3e⁻'),('8.4.2:e2',-2+14+6*2,24,'14'),
('9.1.1:e0',4.85/5,.970,'0.970'),('9.1.2:e0',2.3/23/2*24,1.2,'1.20'),('9.2:e0',6.63e-34*3e8/600e-9,3.315e-19,'3.32'),('9.3:e0',.1*2,.2,'0.20'),('9.3:e1',16.8/84/2*106,10.6,'10.6'),('9.3:e2',.3-.2,.1,'0.10'),
('10.1.1:e0',8.7/5,1.74,'1.74'),('10.1.1:e1',2.7/1.8,1.5,'1.5'),('10.1.2:e0',2.4/24*24,2.4,'2.40'),('10.2:e0',12.3/246,.05,'0.0500'),('10.2:e1',2/40*2,.1,'0.100'),('10.3:e0',5.6/56*74,7.4,'7.4'),('10.3:e2',34.4/172*27,5.4,'5.40'),('10.4:e0',.02*2,.04,'0.040'),('10.4:e2',1.28/128,.01,'0.0100'),
('11.1.1:e0',10*2.7,27,'27.0'),('11.1.1:e1',.4*1.5,.6,'0.60'),('11.1.2:e0',2.7/27*1.5*24,3.6,'3.60'),('11.1.2:e2',5.4/27*56,11.2,'11.2'),('11.2:e0',.1*4,.4,'0.40'),('11.2:e1',15.6/78/2*102,10.2,'10.2'),('11.2:e2',.1-(.35-.30),.05,'0.05'),('11.3:e0',102/102*2*27,54,'54.0'),('11.3:e1',.1*3*96500,28950,'2.895'),('11.3:e2',1000*.51*54/102*.8,216,'216')]
for key,a,b,snippet in samples:
 assert math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-27),(key,a,b)
 sid,ref=key.split(':');assert snippet in units[sid]['examples'][int(ref[1:])]['ans'],key
# Formula parser and separate atom/charge ledgers; each side is (coefficient, formula, net charge).
def atoms(f):
 tokens=re.findall(r'[A-Z][a-z]?|\d+|[()]',f);stack=[Counter()];i=0
 while i<len(tokens):
  t=tokens[i]
  if t=='(':stack.append(Counter());i+=1
  elif t==')':
   c=stack.pop();i+=1;n=int(tokens[i]) if i<len(tokens) and tokens[i].isdigit() else 1;i+=int(i<len(tokens) and tokens[i].isdigit())
   for e,k in c.items():stack[-1][e]+=k*n
  else:
   i+=1;n=int(tokens[i]) if i<len(tokens) and tokens[i].isdigit() else 1;i+=int(i<len(tokens) and tokens[i].isdigit());stack[-1][t]+=n
 assert len(stack)==1;return stack[0]
def ledger(side):
 c=Counter();q=0
 for n,f,z in side:
  for e,k in atoms(f).items():c[e]+=n*k
  q+=n*z
 return c,q
E=[
('alkali water',[(2,'Na',0),(2,'H2O',0)],[(2,'NaOH',0),(1,'H2',0)]),
('peroxide water',[(2,'Na2O2',0),(2,'H2O',0)],[(4,'NaOH',0),(1,'O2',0)]),
('carbonate acid',[(1,'CO3',-2),(2,'H',1)],[(1,'CO2',0),(1,'H2O',0)]),
('bicarbonate heat',[(2,'NaHCO3',0)],[(1,'Na2CO3',0),(1,'CO2',0),(1,'H2O',0)]),
('Mg nitride hydrolysis',[(1,'Mg3N2',0),(6,'H2O',0)],[(3,'Mg(OH)2',0),(2,'NH3',0)]),
('Mg CO2',[(2,'Mg',0),(1,'CO2',0)],[(2,'MgO',0),(1,'C',0)]),
('Ca bicarbonate',[(1,'CaCO3',0),(1,'CO2',0),(1,'H2O',0)],[(1,'Ca(HCO3)2',0)]),
('Al alkaline',[(2,'Al',0),(2,'OH',-1),(6,'H2O',0)],[(2,'Al(OH)4',-1),(3,'H2',0)]),
('Al hydroxide dissolution',[(1,'Al(OH)3',0),(1,'OH',-1)],[(1,'Al(OH)4',-1)]),
('Al hydroxide heat',[(2,'Al(OH)3',0)],[(1,'Al2O3',0),(3,'H2O',0)]),
('Al reduction',[(1,'Fe2O3',0),(2,'Al',0)],[(1,'Al2O3',0),(2,'Fe',0)]),
('Al electrolysis ideal',[(2,'Al2O3',0),(3,'C',0)],[(4,'Al',0),(3,'CO2',0)]),
('Mn acidic total',[(1,'MnO4',-1),(5,'Fe',2),(8,'H',1)],[(1,'Mn',2),(5,'Fe',3),(4,'H2O',0)]),
('Cr acidic total',[(1,'Cr2O7',-2),(14,'H',1),(6,'Fe',2)],[(2,'Cr',3),(7,'H2O',0),(6,'Fe',3)]),
('Cl disproportionation',[(1,'Cl2',0),(2,'OH',-1)],[(1,'Cl',-1),(1,'ClO',-1),(1,'H2O',0)]),
('S comproportionation',[(2,'H2S',0),(1,'SO2',0)],[(3,'S',0),(2,'H2O',0)]),
('Fe reduction CO',[(1,'Fe2O3',0),(3,'CO',0)],[(2,'Fe',0),(3,'CO2',0)]),
('chlorate decomposition',[(2,'KClO3',0)],[(2,'KCl',0),(3,'O2',0)]),
('Ca oxalate',[(1,'Ca',2),(1,'C2O4',-2)],[(1,'CaC2O4',0)])]
E += [('KNO3 heat',[(2,'KNO3',0)],[(2,'KNO2',0),(1,'O2',0)]),('Al2O3 alkaline',[(1,'Al2O3',0),(2,'OH',-1),(3,'H2O',0)],[(2,'Al(OH)4',-1)])]
for name,l,r in E:assert ledger(l)==ledger(r),(name,ledger(l),ledger(r))
reviews=[]
for sid,u in units.items():
 for i,q in enumerate(u['examples']):reviews.append(dict(section=sid,example=i+1,review='作者逐题内容/条件/答案复核；非外部教师审核',numeric_sample=any(k==sid+':e'+str(i) for k,*_ in samples),check=q['verification'],risk=q['pitfall']))
with (O/'EXAMPLE_REVIEW.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=reviews[0],lineterminator='\n');w.writeheader();w.writerows(reviews)
(O/'CALCULATIONS.json').write_text(json.dumps(dict(result='pass',numerical_samples=len(samples),balanced_equations=len(E),examples_authored_reviewed=len(reviews),numeric_results=[dict(question=k,actual=a,expected=b) for k,a,b,_ in samples],equation_results=[n for n,_,_ in E],limitations='53项为独立算式/题内答案对照，21式为元素和电荷账；其余定性例由作者复核，不冒充独立人员审定。'),ensure_ascii=False,indent=2)+'\n')
print('PASS',len(samples),'arithmetic samples;',len(E),'atom/charge balances; 58 previous notes and protected resources unchanged')
