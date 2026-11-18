"""Identity/resource checks and independent numeric/geometry samples, not teacher approval."""
from pathlib import Path
import os,collections,hashlib,json,math,re,subprocess,xml.etree.ElementTree as E
R=Path(__file__).resolve().parents[1]; rows=[]
def check(name,value,detail=''):
    assert value,(name,detail)
    rows.append({'check':name,'result':'pass','detail':detail})
def eq(name,a,b):check(name,math.isclose(a,b,rel_tol=1e-7,abs_tol=1e-7),{'computed':a,'expected':b})
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
A=json.loads((R/'reports/v22/ASSET_REVIEW.json').read_text());B={a['code']:a for a in A}
check('149 unique input and audit IDs',len(A)==len({a['id'] for a in A})==len(B)==149)
registry=json.loads(subprocess.check_output(['node','-e',"const fs=require('fs'),vm=require('vm'),c={};c.window=c;vm.createContext(c);vm.runInContext(fs.readFileSync('data/v22-illustrations.js','utf8'),c);process.stdout.write(JSON.stringify({a:c.V22_ILLUSTRATIONS,s:c.V22_SUPERSEDED_FIGURES}))"],cwd=R))
real={(s['lesson_key'],s['id']) for s in json.loads((R/'reports/v22/SECTION_REFERENCES.json').read_text())}
live=json.loads(subprocess.check_output(['node','-e',"const fs=require('fs'),vm=require('vm'),c={};c.window=c;vm.createContext(c);for(const f of fs.readdirSync('lessons').filter(f=>/^(phys|chem|bio|math)\\d+\\.js$/.test(f)))vm.runInContext(fs.readFileSync('lessons/'+f,'utf8'),c);process.stdout.write(JSON.stringify(Object.entries(c.LESSONS).flatMap(([k,l])=>l.sections.map(s=>({key:k,id:s.id,title:s.t})))))"],cwd=R))
new={(s['subject']+str(s['chapter_id']),s['section_id']) for s in json.loads((R/'data/review/batch05_sections.json').read_text())}
check('historical plus registered new section evidence equals live catalog',real|new=={(s['key'],s['id']) for s in live})
for a in A:
    p=R/a['original_path'];check(a['code']+' original hash',digest(p)==a['original_sha256']==a['sha256'])
    root=E.parse(p).getroot();check(a['code']+' XML root',root.tag.endswith('}svg'))
    check(a['code']+' no active/external content',all(e.tag.split('}')[-1] not in ['script','foreignObject'] and all(not k.lower().startswith('on') for k in e.attrib) and all(not (k.endswith('href') and not v.startswith('#')) for k,v in e.attrib.items()) for e in root.iter()))
    check(a['code']+' individual scientific evidence',len(a['scientific_review'])>20 and a['review_status'] in ['PASS','FIXED','BLOCKED'])
    check(a['code']+' visual record',bool(a['visual_sheet']) and (R/'reports/v22'/a['visual_sheet']).is_file())
    if a['reviewed_path']:check(a['code']+' reviewed hash',digest(R/a['reviewed_path'])==a['reviewed_sha256'])
    if a['section_id']:
        check(a['code']+' real section',(a['lesson_key'],a['section_id']) in real)
        check(a['code']+' actual subsection title',next(s['title'] for s in live if (s['key'],s['id'])==(a['lesson_key'],a['section_id']))==a['section_title'])
        anchor=a['course_content_anchor'];unit=json.loads((R/anchor['path']).read_text())[a['section_id']]
        check(a['code']+' live learning goal evidence',anchor['learning_goals']==unit['goals'])
    if a['review_status']=='FIXED':check(a['code']+' fix recorded',bool(a['fixes']) and a['original_sha256']!=a['reviewed_sha256'])
    if a['review_status']=='BLOCKED':check(a['code']+' quarantine',not a['selected'] and a['reviewed_path'] is None)
    if not a['section_id']:check(a['code']+' no fabricated subsection',not a['selected'] and a['chapter_id'] is None)
check('runtime exactly selected eligible assets',{x['code'] for x in registry['a']}=={a['code'] for a in A if a['integration_status']=='integrated'})
for p,code in registry['s'].items():check('legacy replacement '+p,(R/p).is_file() and B[code]['selected'])
check('one image per concept in same section',len(registry['a'])==len({(a['lesson_key'],a['section_id'],a['concept']) for a in registry['a']}))
# Every baseline course/note/assessment/asset file is protected byte for byte.
protected=[]
for name in subprocess.check_output(['git','ls-tree','-r','--name-only','origin/main'],cwd=R,text=True).splitlines():
    if name.startswith(('lessons/','data/notes/','data/base-lessons/','assets/','data/curriculum','data/subjects','data/review/new_sections')) or name in ['illustrations/PROMPTS_BATCH_ALL.json','data/p0-illustrations.js','data/illustrations.js']:
        original=subprocess.check_output(['git','show','origin/main:'+name],cwd=R)
        if name=='data/subjects.js':
            js="const vm=require('vm'),fs=require('fs'),c={window:{}};vm.runInNewContext(fs.readFileSync(0,'utf8'),c);process.stdout.write(JSON.stringify(c.window));"
            before=json.loads(subprocess.check_output(['node','-e',js],input=original));after=json.loads(subprocess.check_output(['node','-e',js],input=(R/name).read_bytes()))
            check('course identity codes preserved',[(x['code'],x.get('legacy')) for x in before['SUBJECTS']]==[(x['code'],x.get('legacy')) for x in after['SUBJECTS']])
            for a,b in zip(before['SUBJECTS'],after['SUBJECTS']):
                check(a['code']+' subject metadata preserved',a==b if a['code']!='math_pending' else {k:v for k,v in a.items() if k!='name'}=={k:v for k,v in b.items() if k!='name'})
            for code in ['physics','chemistry','biology']:check(code+' examination sources unchanged',before['EXAM_SOURCES'][code]==after['EXAM_SOURCES'][code])
            for code in ['adv_math_i','adv_math_ii']:
                check(code+' source file school and page preserved',all(before['EXAM_SOURCES'][code][f]==after['EXAM_SOURCES'][code][f] for f in ['file','page','school']))
        elif name=='illustrations/PROMPTS_BATCH_ALL.json':check('original142 prompt data unchanged',json.loads(original)['tasks']==json.loads((R/name).read_bytes())['tasks'])
        else:check('baseline protected '+name,original==(R/name).read_bytes())
        protected.append(name)
T=json.loads((R/'illustrations/PROMPTS_BATCH_ALL.json').read_text())['tasks'];C=json.loads((R/'reports/v22/TASK_COVERAGE.json').read_text())
check('exact142 task identity',len(C)==142 and {t['id'] for t in T}=={t['task_id'] for t in C})
check('no asset-count completion claim',sum(c['v22_coverage']=='full' for c in C)==3)
for x in C:check('specific task remaining '+x['task_id'],bool(x['remaining_requirements']))
# Independent scalar arithmetic, using model parameters printed in the SVG.
scalar_start=len(rows)
for code,label,a,b in [
 ('P02','signed displacement',2*4-1*2,6),('P02','distance',2*4+1*2,10),
 ('P08','final v',2+1.5*4,8),('P08','trapezoid displacement',(2+8)*4/2,20),
 ('P09','acceleration',(10-2)/2,4),('P10','impulse',6*4/2,12),
 ('P11','collision v',2*3/3,2),('P27','kinetic loss',.5*2*3**2-.5*3*2**2,3),
 ('P12','braking t',20/4,5),('P12','braking displacement',20**2/(2*4),50),
 ('P13','catch time',30/(6-3),10),('P13','position at catch',6*10,60),
 ('P14','Atwood a',(3-2)*10/(3+2),2),('P14','tension',2*(10+2),24),
 ('P15','friction limit',.4*2*10,8),('P16','tangent weight',2*10*math.sin(math.pi/6),10),
 ('P16','normal weight',2*10*math.cos(math.pi/6),10*math.sqrt(3)),
 ('P17','fall time',math.sqrt(2*20/10),2),('P17','range',10*2,20),
 ('P18','spring energy',.5*200*.1**2,1),('P19','parallel R',1/(1/2+1/4),4/3),
 ('P19','parallel I',12/(4/3),9),('P20','secant slope',(.5*3**2-.5*1**2)/(3-1),2),
 ('P21','terminal v',10*3,30),('P21','fall displacement',.5*10*3**2,45),
 ('P23','static maximum',.6*20*math.cos(math.pi/6),6*math.sqrt(3)),
 ('P24','signed area',2*2-2*2+4*2,8),('P24','absolute area',2*2+2*2+4*2,16),
 ('P25','work integral',4**2,16),('P29','kinetic energy at4',.5*2*4**2,16),
 ('P30','fall time',math.sqrt(2*5/10),1),('P31','force at10cm',50*10/100,5),
 ('P33','refracted angle',math.degrees(math.asin(math.sin(math.pi/4)/1.33)),32.117631277991194),
 ('P38','image v/f',1/(1-1/3),1.5),('P39','critical angle',math.degrees(math.asin(1/1.5)),41.810314895778596),
 ('P40','total parallel power',12**2/6+12**2/12,36),('P43','voltage ratio',12*200/100,24),
 ('P44','charge microC',2*10,20),('P49','rms',10/math.sqrt(2),7.0710678118654755),
 ('P50','charge at tau',1-math.exp(-1),.6321205588285577),('P55','equilibrium temperature',(.2*80+.3*20)/(.2+.3),44),
 ('P56','final pressure',200*2/4,100),('C04','S oxidation number',4*2-2,6),
 ('C04','Mn oxidation number',4*2-1,7),('C04','ammonium N',1-4,-3),
 ('C06','leftover H2',5-2*2,1),('C23','chloride cell count',8/8+6/2,4),('C23','sodium cell count',12/4+1,4),
 ('C26','CaO mass',50*56/100,28),('C26','CO2 mass',50*44/100,22),
 ('B24','carbon fixation',3*5+3,6*3),('B32','carbon split',5*3+3,18),('B32','ATP',6+3,9),
 ('B31','net ATP',4-2,2),('B55','genotype sum',.6**2+2*.6*.4+.4**2,1)]:eq(code+' '+label,a,b)
scalar_count=len(rows)-scalar_start
# Vector geometry is verified from edited line endpoints, not from a text label.
for code,x,y,w in [('P05',362,368,160),('P16',420,368.30973451327435,200)]:
    r=E.parse(R/B[code]['reviewed_path']).getroot();vectors={e.get('stroke'):(float(e.get('x2'))-x,float(e.get('y2'))-y) for e in r if e.tag.endswith('line') and e.get('x1')==str(x) and abs(float(e.get('y1'))-y)<1e-7}
    t=vectors['#ca4b52'];n=vectors['#bd7d13'];N=vectors['#177b59'];g=vectors['#7155bb']
    eq(code+' component x closure',t[0]+n[0],g[0]);eq(code+' component y closure',t[1]+n[1],g[1]);eq(code+' orthogonality',t[0]*n[0]+t[1]*n[1],0)
    eq(code+' normal reaction x',N[0],-n[0]);eq(code+' normal reaction y',N[1],-n[1]);eq(code+' weight length',math.hypot(*g),w)
r=E.parse(R/B['P17']['reviewed_path']).getroot();pts=[tuple(map(float,p.split(','))) for p in next(e for e in r if e.tag.endswith('polyline')).get('points').split()]
check('P17 ends at ground',pts[-1]==(600,550) and max(y for x,y in pts)==550)
r=E.parse(R/B['C17']['reviewed_path']).getroot();circles=[(float(e.get('cx')),float(e.get('cy'))) for e in r if e.tag.endswith('circle')]
for triple in [circles[:3],circles[3:]]:
    o,h1,h2=triple;v=(h1[0]-o[0],h1[1]-o[1]);w=(h2[0]-o[0],h2[1]-o[1]);eq('C17 intramolecular water angle',math.degrees(math.acos((v[0]*w[0]+v[1]*w[1])/(math.hypot(*v)*math.hypot(*w)))),104.5)
check('C17 donorO-H-acceptorO collinear',circles[0][1]==circles[1][1]==circles[3][1] and circles[0][0]<circles[1][0]<circles[3][0])
r=E.parse(R/B['B22']['reviewed_path']).getroot();dots=[e for e in r if e.tag.endswith('circle') and e.get('fill')=='#d36265' and float(e.get('cx'))>800]
check('B22 primary pump low to high particle count',sum(float(e.get('cy'))<365 for e in dots)==7 and sum(float(e.get('cy'))>427 for e in dots)==1)
template='TACGGAT';check('B45 reverse-oriented template complement',''.join(dict(T='A',A='U',C='G',G='C')[n] for n in template)=='AUGCCUA')
# Chemical atom and charge conservation, independent of diagram layout.
def species(s):
    if s=='e^-':return collections.Counter(),-1
    parts=s.split('^');q=0
    if len(parts)>1:q=(1 if parts[1][-1]=='+' else -1)*int(parts[1][:-1] or '1')
    form=parts[0]
    while '(' in form:
        form=re.sub(r'\(([^()]+)\)(\d*)',lambda m:''.join(el+str(int(n or '1')*int(m[2] or '1')) for el,n in re.findall(r'([A-Z][a-z]?)(\d*)',m[1])),form)
    c=collections.Counter()
    for el,n in re.findall(r'([A-Z][a-z]?)(\d*)',form):c[el]+=int(n or '1')
    return c,q
reactions=[('C05',[(1,'Zn'),(1,'Cu^2+')],[(1,'Zn^2+'),(1,'Cu')]),
 ('C06',[(2,'H2'),(1,'O2')],[(2,'H2O')]),('C08',[(1,'Mg'),(1,'H2O')],[(1,'MgO'),(1,'H2')]),
 ('C08',[(1,'Ca'),(2,'H2O')],[(1,'Ca(OH)2'),(1,'H2')]),
 ('C09',[(1,'Al2O3'),(6,'HCl')],[(2,'AlCl3'),(3,'H2O')]),
 ('C14',[(1,'MnO4^-'),(8,'H^+'),(5,'e^-')],[(1,'Mn^2+'),(4,'H2O')]),
 ('C15',[(1,'Al^3+'),(3,'OH^-')],[(1,'Al(OH)3')]),('C15',[(1,'Al(OH)3'),(1,'OH^-')],[(1,'Al(OH)4^-')]),
 ('C18',[(1,'Cl2'),(2,'OH^-')],[(1,'Cl^-'),(1,'ClO^-'),(1,'H2O')]),
 ('C20',[(1,'CO3^2-'),(2,'H^+')],[(1,'CO2'),(1,'H2O')]),('C20',[(1,'HCO3^-'),(1,'H^+')],[(1,'CO2'),(1,'H2O')]),
 ('C21',[(1,'Ca(OH)2'),(1,'CO2')],[(1,'CaCO3'),(1,'H2O')]),('C21',[(1,'CaCO3'),(1,'CO2'),(1,'H2O')],[(1,'Ca(HCO3)2')]),
 ('C22',[(2,'Al2O3'),(3,'C')],[(4,'Al'),(3,'CO2')]),
 ('C25',[(1,'MnO4^-'),(8,'H^+'),(5,'Fe^2+')],[(1,'Mn^2+'),(4,'H2O'),(5,'Fe^3+')]),
 ('C26',[(1,'CaCO3')],[(1,'CaO'),(1,'CO2')]),('B40',[(2,'H2O')],[(1,'O2'),(4,'H^+'),(4,'e^-')])]
def total(side):
    counts=collections.Counter();charge=0
    for n,s in side:
        c,q=species(s);charge+=n*q
        for el,k in c.items():counts[el]+=n*k
    return counts,charge
for code,left,right in reactions:check(code+' atom/charge balance '+str(left),total(left)==total(right))
out={'result':'pass','checks':len(rows),'protected_baseline_files':len(protected),'independent_scalar_samples':scalar_count,'balanced_reactions':len(reactions),'scope':'逐图定性审查见ASSET_REVIEW；自动检查只覆盖资源/结构/身份与所列数值、向量、配平样本，非全学科教师审定','details':rows}
(R/os.environ.get('UEC_V22_STATIC_RESULT','reports/v22/STATIC_TEST_RESULTS.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='details'},ensure_ascii=False))
