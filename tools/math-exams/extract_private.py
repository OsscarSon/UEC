"""Private, reproducible extraction. OCR remains unverified; no page images are published."""
from pathlib import Path
import fitz,json,subprocess,concurrent.futures,os
B=Path(os.environ.get('UEC_EXAM_SOURCE','/workspace/research-math-exams'));inv=json.loads((B/'inventory.json').read_text());out=B/'ocr';out.mkdir(exist_ok=True)
T=B/'tessdata'
eng=T/'eng.traineddata'
if not eng.exists():eng.symlink_to('/usr/share/tesseract-ocr/5/tessdata/eng.traineddata')
def run(item):
 f,page=item;folder=out/f['category'];folder.mkdir(exist_ok=True);dest=folder/(f['file']+f'.p{page+1}.txt')
 if dest.exists():return
 doc=fitz.open(B/f['category']/f['file']);p=doc[page];t=p.get_text()
 if len(t)<80:
  image=dest.with_suffix('.png');p.get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(image)
  r=subprocess.run(['tesseract',str(image),'stdout','--tessdata-dir',str(T),'-l','chi_sim+eng','--psm','3'],env={**os.environ,'OMP_THREAD_LIMIT':'1'},capture_output=True,text=True)
  t=r.stdout;image.unlink();assert r.returncode==0,r.stderr
 dest.write_text(t)
items=[(f,p) for f in inv for p in range(f['pages'])]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
 for i,_ in enumerate(e.map(run,items)):
  if (i+1)%20==0:print('Unverified extraction',i+1,'/',len(items),flush=True)
print('Extracted',len(items),'pages. OCR is not visual or mathematical verification.')
