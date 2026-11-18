"""Protect existing course/content/art data and validate the new static tool build."""
from pathlib import Path
import json,subprocess,re
R=Path(__file__).resolve().parents[1];baseline='19f2ffaba16f446ebb7a7b3a0b3084d4e6253ccf';rows=[]
def C(name,condition):
 assert condition,name
 rows.append({'check':name,'status':'pass'})
files=subprocess.check_output(['git','ls-tree','-r','--name-only',baseline],cwd=R,text=True).splitlines()
protected=[f for f in files if f.startswith(('lessons/','data/notes/','data/base-lessons/','data/authoring/','data/batch05/','assets/','data/curriculum','data/review/','illustrations/')) or f in ['illustration-manifest.json','data/math-courses.js','data/subjects.js','ui-polish.css']]
for f in protected:C('unchanged '+f,subprocess.check_output(['git','show',baseline+':'+f],cwd=R)==(R/f).read_bytes())
old=subprocess.check_output(['git','show',baseline+':index.html'],cwd=R,text=True);new=(R/'index.html').read_text()
C('canonical embedded course array unchanged',re.search(r'const D=(\[.*\]);/\*',old)[1]==re.search(r'const D=(\[.*\]);/\*',new)[1])
C('116 canonical chapters retained',len(json.loads((R/'data/curriculum.json').read_text()))==116)
for path in ['ui/icons.js','ui/dashboard-state.js','ui/study-tools.js','ui/dashboard.js','data/formula-cards.js']:
 subprocess.run(['node','--check',str(R/path)],check=True);C('JS syntax '+path,True)
js="const fs=require('fs'),vm=require('vm'),k=require('katex'),c={window:{}};vm.runInNewContext(fs.readFileSync('data/formula-cards.js','utf8'),c);let n=0;for(const a of Object.values(c.window.STUDY_FORMULAS))for(const [,tex] of a){k.renderToString(tex,{throwOnError:true,trust:false,strict:'ignore'});n++;}process.stdout.write(String(n));"
count=int(subprocess.check_output(['node','-e',js],cwd=R));C('all explicit KaTeX formulas parse',count>=35)
for source,target in [('node_modules/katex/dist/katex.min.js','vendor/katex/katex.min.js'),('node_modules/jsxgraph/distrib/jsxgraphcore.js','vendor/jsxgraph/jsxgraphcore.js')]:C('exact upstream vendored runtime '+target,(R/source).read_bytes()==(R/target).read_bytes())
inputs=json.loads((R/'vendor/BUNDLE_INPUTS.json').read_text())['inputs']
C('Sass watcher and picomatch absent from browser build',not any(re.search(r'node_modules/(?:sass|@parcel/watcher|picomatch)/',p) for p in inputs))
C('all actual whiteboard assets present',all((R/p).is_file() for p in ['vendor/draw/whiteboard.js','vendor/draw/whiteboard.css','vendor/draw/subset-worker.chunk.js','vendor/draw/chunks/subset-worker.chunk.js']))
C('third party licenses retained',bool(list((R/'vendor/draw').rglob('*.LEGAL.txt'))) and (R/'vendor/THIRD_PARTY_NOTICES.md').is_file())
result={'status':'pass','baseline':baseline,'protected_files':len(protected),'explicit_formula_cards':count,'static_assertions':len(rows),'checks':rows,'limits':'源文件保护、结构与明确公式语法；不是所有旧公式已转换为TeX或教师审定。'}
(R/'reports/dashboard/STATIC_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print('PASS',len(protected),'baseline files preserved;',count,'explicit KaTeX formulas;',len(rows),'static assertions')
