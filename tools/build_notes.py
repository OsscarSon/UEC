"""Compile authored supplements, refusing unknown or duplicate existing section IDs."""
import json,pathlib,re,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]
# JS remains the source of truth for the original course structure.
js="const fs=require('fs'),vm=require('vm');let c={};c.window=c;vm.createContext(c);for(const f of fs.readdirSync('lessons').filter(f=>/^(phys|chem|bio)\\d+\\.js$/.test(f)))vm.runInContext(fs.readFileSync('lessons/'+f,'utf8'),c);process.stdout.write(JSON.stringify(c.LESSONS));"
original=json.loads(subprocess.check_output(['node','-e',js],cwd=ROOT))
compiled={}
for p in sorted((ROOT/'data/notes').glob('*.json')):
 prefix,chapter=re.fullmatch(r'(phys|chem|bio)(\d+)',p.stem).groups()
 subject={'phys':'物理','chem':'化学','bio':'生物'}[prefix]
 code={'phys':'physics','chem':'chemistry','bio':'biology'}[prefix]
 key=subject+str(int(chapter));lesson=original[key]
 data=json.loads(p.read_text());ids=[s['id'] for s in lesson['sections']]
 if list(data)!=ids:raise ValueError(f'{p}: complete chapter and original order required: {ids}')
 for sid,u in data.items():
  for field in ['goals','prerequisites','flow','deep','derive','exam','examples','practice','quick','quiz']:
   if not u.get(field):raise ValueError((key,sid,field))
  if len(u['examples'])<3 or len(u['practice'])<4:raise ValueError((key,sid,'question depth'))
  for q in [*u['examples'],*u['practice'],u['quiz'],*[g['question'] for g in u.get('diagnostics',[]) if g.get('question')]]:
   if not q['q'] or len(q['steps'])<2 or not q['ans']:raise ValueError((key,sid,'solution'))
   related=re.search(r'综合(\d+(?:\.\d+)+)',q['q'])
   related_ids=[v['id'] for lk,ll in original.items() if lk.startswith(subject) for v in ll['sections']]
   rel=[related[1]] if related and related[1] in related_ids else []
   q.update(subject_code=code,chapter_id=int(chapter),primary_section=sid,related_sections=rel,question_origin='original',paper_no=None)
  for q in [*u['examples'],*u['practice'],u['quiz'],*[g['question'] for g in u.get('diagnostics',[]) if g.get('question')]]:
   if 'method' in q and not q.get('principle'):q['principle']=u['derive'][0]
  u.update(subject=subject,subject_code=code,chapter_id=int(chapter),section_id=sid,
   content_sources=[dict(source_id={'phys':'dz_physics','chem':'dz_chemistry','bio':'dz_biology'}[prefix],page=2,version='2026',access_date='2026-11-17'),dict(source_id='school',page=4 if prefix=='chem' else 3,version='12/11/2026',access_date='2026-11-17')])
  science={'chem05':'https://openstax.org/books/chemistry-2e/pages/6-introduction','chem06':'https://openstax.org/books/chemistry-2e/pages/6-5-periodic-variations-in-element-properties','bio03':'https://openstax.org/books/biology-2e/pages/6-introduction','phys03':'https://openstax.org/books/college-physics-2e/pages/2-introduction-to-one-dimensional-kinematics','phys04':'https://openstax.org/books/college-physics-2e/pages/4-3-newtons-second-law-of-motion-concept-of-a-system','bio01':'https://openstax.org/books/biology-2e/pages/3-introduction','bio02':'https://openstax.org/books/biology-2e/pages/4-introduction-to-cell-structure'}
  if p.stem in science:u['content_sources'].append(dict(source_id='science_'+p.stem,url=science[p.stem],page_or_section='来源台账逐节条目',version='OpenStax',access_date='2026-11-17'))
  if p.stem=='chem06':u['content_sources'].append(dict(source_id='dz_chem_content_table',url='https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf',page=2,version='公开课程内容跨学科表；版本与学校需继续核对',access_date='2026-11-18'))
  if p.stem=='chem06' and sid in ['6.1.1','6.1.2']:u['content_sources'].append(dict(source_id='rsc_periodic_history',url='https://periodic-table.rsc.org/history/about',page_or_section='三元素组、八音律与门捷列夫的分类/预测',version='RSC科学史页面；非考试范围',access_date='2026-11-18',verification_status='partially_verified'))
  if prefix=='chem' and int(chapter) in [3,4]:u['content_sources'].append(dict(source_id='chemistry_standard',page=2 if int(chapter)==3 else 3,version='官网文件；年份见来源审查',access_date='2026-11-17'))
  detailed={'chem05':{'5.1':'2-2-evolution-of-atomic-theory','5.2':'2-3-atomic-structure-and-symbolism','5.3':'6-2-the-bohr-model','5.4':'6-4-electronic-structure-of-atoms-electron-configurations'},'chem06':{'6.1.1':'2-5-the-periodic-table','6.1.2':'2-5-the-periodic-table','6.2':'2-5-the-periodic-table','6.3.1':'6-5-periodic-variations-in-element-properties','6.3.2':'6-4-electronic-structure-of-atoms-electron-configurations','6.3.3':'6-5-periodic-variations-in-element-properties'},'bio03':{'3.1':'6-5-enzymes','3.2':'6-5-enzymes','3.3':'6-5-enzymes','3.4':'6-4-atp-adenosine-triphosphate','3.5':'7-4-oxidative-phosphorylation','3.6':'8-3-using-light-energy-to-make-organic-molecules','3.7':'8-2-the-light-dependent-reactions-of-photosynthesis'}}
  if p.stem in detailed:u['content_sources'].append(dict(source_id='science_'+p.stem+'_'+sid,url='https://openstax.org/books/'+('biology-2e' if prefix=='bio' else 'chemistry-2e')+'/pages/'+detailed[p.stem][sid],page_or_section=detailed[p.stem][sid],version='OpenStax；相关原理部分核对',access_date='2026-11-18',verification_status='partially_verified'))
  if key=='化学3' and sid=='3.6':
   u['content_sources'].append(dict(source_id='bipm_mole',url='https://www.bipm.org/en/si-base-units/mole',page_or_section='SI base unit mole',version='modern SI',access_date='2026-11-17'))
   u['content_sources'].append(dict(source_id='nist_constants',url='https://physics.nist.gov/cuu/pdf/all.pdf',page=6,version='2022 CODATA',access_date='2026-11-17'))
 compiled[key]=data
(ROOT/'lessons/batch-notes.js').write_text('// Generated by python tools/build_notes.py; edit data/notes/*.json.\nwindow.BATCH_NOTES='+json.dumps(compiled,ensure_ascii=False,separators=(',',':'))+';\n')
print(f'Compiled {len(compiled)} complete chapters, {sum(map(len,compiled.values()))} sections')
