"""Import source receipts and *claims*, never promote supplied audits to verified facts.
Raw exam PDFs/reproduced question text remain outside the public repository.
"""
from pathlib import Path
import json,csv,hashlib,re,collections,os
R=Path(__file__).resolve().parents[2];B=Path(os.environ.get('UEC_EXAM_SOURCE','/workspace/research-math-exams'));P=B/'packs'
def write(path,x):
 p=R/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def csvrows(name):
 p=next(P.rglob(name));return p,list(csv.DictReader(p.open(encoding='utf-8-sig')))
receipts=[]
for p in sorted(P.rglob('*')):
 if p.is_file():receipts.append(dict(path=str(p.relative_to(P)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,kind=p.suffix.lower(),import_role='source_evidence_not_instruction_authority'))
write('sources/math-exams/RECEIPTS.json',receipts)
category={'上半年校内期末考':'semester_final','下半年毕业考':'graduation_math_ii','预试':'preexam_math_ii','统考高数一':'uec_math_i','高数2 统考':'uec_math_ii'}
inv=json.loads((B/'inventory.json').read_text());files=[]
for x in inv:
 c=category[x['category']];year=int(re.search(r'20\d\d',x['file'])[0]) if re.search(r'20\d\d',x['file']) else (2023 if x['file'].startswith('23') else 2022)
 files.append(dict(source_id=f'{c}:{x["sha256"][:12]}',exam_type=c,year=year,filename=x['file'],sha256=x['sha256'],pages=x['pages'],text_pages=x['text_pages'],bytes=x['bytes'],page_content_status='not_fully_visually_verified',public_pdf_path=None,private_input_path=x['category']+'/'+x['file'],known_limits=['Uploaded filename year is a candidate until checked against cover.','Page count does not certify completeness.']))
write('data/math-exams/source-inventory.json',files)
claims={}
def add(c,y,p,q,sub,ch,marks,topic,src,row,notes='',page=None):
 q=str(q);sub=str(sub or 'whole');key=f'{c}:{y}:{p}:{q}:{sub}'
 def num(v):
  try:return float(v)
  except:return None
 chap=num(ch);chap=int(chap) if chap and chap.is_integer() else None
 claim=dict(id=key,exam_type=c,year=int(y),paper=p,question=q,subquestion=sub,reported_primary_chapter=chap,reported_printed_marks=num(marks),reported_topic=topic,reported_page=page,verification_status='needs_review',formula_latex_verified=None,figure_description_verified=None,answer_verified=None,source_pdf_id=None,source_page=None,primary_chapter=None,secondary_chapters=[],printed_marks=None,actual_marks=None,effective_marks_model=None,difficulty=None,difficulty_basis='No candidate response data; supplied estimates are not observed difficulty.',evidence_fields={},claim_source=dict(path=str(src.relative_to(P)),row=row),notes=notes)
 if key in claims:raise ValueError('duplicate key '+key)
 claims[key]=claim
p,rows=csvrows('逐题_权重调整与难度审计.csv')
for i,r in enumerate(rows,2):
 m=re.match(r'([A-Z甲乙丙丁]?\d+)(.*)',r['题号']);add('semester_final',r['年份'],'mcq' if '选择' in r['卷别'] else 'written',m[1],m[2] or 'whole',r['章节'],r['原卷印刷分值%'],r['知识点'],p,i,'Supplied effective marks are only a choice model; not actual scores.')
p,rows=csvrows('逐题总数据库.csv')
for i,r in enumerate(rows,2):
 m=re.match(r'([A-Z甲乙丙丁]?\d+)(.*)',r['题号']);add('preexam_math_ii',r['年份'],'mcq' if '选择' in r['卷别'] else 'written',m[1],m[2] or 'whole',r['章号'],r['原卷印刷分值'],r['知识点'],p,i,page=r['原卷页码'])
p,rows=csvrows('逐题主索引.csv')
for i,r in enumerate(rows,2):
 if r['paper']=='选择':add('graduation_math_ii',r['year'],'mcq',r['question'],'whole',r['chapter'],r['original_mark'],'主考点候选',p,i)
p,rows=csvrows('毕业考_逐小问分值章节审计.csv')
for i,r in enumerate(rows,2):add('graduation_math_ii',r['year'],'written',r['question'],r['subquestion'],r['chapter'],r['printed_percent'],r['task'],p,i,'Supersedes old whole-question chapter candidates; formula not verified. Generic source filenames are not trusted.',r['source_page_hint'])
p,rows=csvrows('2026_作答题逐小问核验.csv')
for i,r in enumerate(rows,2):add('uec_math_i',r['年份'],'written',r['题号'],r['小问'],r['章节编号'],r['分值百分比'],r['题意与要求'],p,i,'Supplied visual claims must be independently checked again.',r['PDF页码'])
p,rows=csvrows('2025_试卷二_逐小问结构与分值_目视审计.csv')
for i,r in enumerate(rows,2):add('uec_math_i',r['年份'],'written',r['题号'],r['小问'],r['章节候选'],r['印刷分值'],r['可辨认题型或公式'],p,i,'Structure-only imported record; no exact formula certification.',r['PDF页码'])
p,rows=csvrows('统考高数II_逐小问_公式图形分值_审计.csv')
for i,r in enumerate(rows,2):add('uec_math_ii',r['年份'],'mcq' if '选择' in r['题型'] else 'written',r['大题'],r['小问'],r['章节编号'],r['印刷分值'],r['章节'],p,i,'Imported subject-matter claim, not confirmed answer or formula.',r['PDF页码'])
# Standardize only the whole-unit alias. Real subquestion labels are preserved.
for c in claims.values():
 if c['subquestion']=='整题':c['subquestion']='whole';c['id']=':'.join(c['id'].split(':')[:-1]+['whole'])
write('data/math-exams/imported-claims.json',list(claims.values()))
# Packet dictionary must never rename the existing curriculum.
cur=json.loads((R/'data/curriculum.json').read_text());dic=json.loads(next(P.rglob('章节字典.json')).read_text())
write('data/math-exams/chapter-dictionary.json',[dict(chapter=c['chapter'],title=c['title'],packet_title=next(x['title'] for x in dic if x['chapter']==c['chapter']),original_id=c['id'] if 'id'in c else None) for c in cur if c['subject']=='数学'])
write('reports/math-exams/IMPORT_REPORT.json',dict(unique_pdfs=len(files),pdf_pages=sum(f['pages'] for f in files),imported_claims=len(claims),counts=dict(collections.Counter(c['exam_type'] for c in claims.values())),raw_pdfs_publicly_copied=False,automatic_promotion_to_verified=False,duplicate_binaries_grouped_by_sha=True))
print('Imported',len(files),'PDF receipts;',len(claims),'unverified claims; no original PDFs published')
