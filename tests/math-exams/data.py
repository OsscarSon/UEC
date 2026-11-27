from pathlib import Path
import json,collections,subprocess,hashlib
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams';B=Path('/workspace/research-math-exams');checks=[]
def L(n):return json.loads((D/n).read_text(encoding='utf-8'))
def C(n,v):assert v,n;checks.append(n)
inv=L('source-inventory.json');rows=L('research-ledger.json');pages=json.loads((R/'reports/math-audit/page-audit.json').read_text(encoding='utf-8'));C('47 unique PDF hashes',len(inv)==47 and len({x['sha256']for x in inv})==47);C('257 indexed pages',len(pages)==257 and sum(x['pages']for x in inv)==257)
if B.exists():
 for f in inv:C('private original SHA '+f['source_id'],hashlib.sha256((B/f['private_input_path']).read_bytes()).hexdigest()==f['sha256'])
 pack_hashes={hashlib.sha256(p.read_bytes()).hexdigest()for p in (B/'packs').rglob('*') if p.is_file() and '.pdf'in p.name.lower()}
 C('three split packs PDFs equal five original archives, duplicates not counted',pack_hashes=={x['sha256']for x in inv})
C('all ids unique',len(rows)==len({r['id']for r in rows}));C('import never promoted confidence labels',all(r['formula_latex_verified']is None and r['verification_status']=='needs_review'for r in L('imported-claims.json')))
byid={f['source_id']:f for f in inv}
for r in rows:
 if r['verification_status']=='visual_fields_checked':
  C('page trace '+r['id'],r['source_pdf_id']in byid and 1<=r['source_page']<=byid[r['source_pdf_id']]['pages'])
  C('formula/figure evidence '+r['id'],bool(r['formula_latex_verified'])and bool(r['figure_description_verified']))
 if r['statistics_eligible']:C('unknown/ambiguous not ranked '+r['id'],r['primary_chapter']is not None and r['printed_marks']is not None and not r['scope_conflict'] and r.get('review_issue')is None)
C('no raw PDFs in public module',not list(D.rglob('*.pdf')))
for c,y,p,total in [('uec_math_i',2026,'mcq',30),('uec_math_i',2026,'written',70),('uec_math_ii',2026,'mcq',30),('uec_math_ii',2026,'written',70),('semester_final',2026,'mcq',30),('semester_final',2026,'written',70),('graduation_math_ii',2025,'written',120),('graduation_math_ii',2025,'mcq',40),('preexam_math_ii',2025,'mcq',40),('preexam_math_ii',2025,'written',120),('uec_math_i',2025,'written',90),('uec_math_ii',2024,'written',120),('uec_math_ii',2025,'written',120),('uec_math_i',2024,'written',90),('uec_math_i',2019,'written',90),('uec_math_i',2019,'mcq',40),('uec_math_ii',2019,'written',120),('uec_math_ii',2019,'mcq',40),('uec_math_i',2020,'written',90),('uec_math_ii',2020,'written',120),('uec_math_i',2021,'written',90),('uec_math_i',2021,'mcq',40),('uec_math_ii',2021,'written',120),('uec_math_ii',2021,'mcq',40),('uec_math_ii',2018,'written',120),('uec_math_ii',2018,'mcq',40),('uec_math_i',2022,'written',90),('uec_math_i',2022,'mcq',40),('uec_math_ii',2022,'written',120),('uec_math_ii',2022,'mcq',40),('uec_math_i',2023,'written',90),('uec_math_i',2023,'mcq',40),('uec_math_ii',2023,'written',120),('uec_math_ii',2023,'mcq',40),('graduation_math_ii',2021,'written',120),('graduation_math_ii',2021,'mcq',40),('graduation_math_ii',2022,'written',120),('graduation_math_ii',2022,'mcq',40),('graduation_math_ii',2023,'written',120),('graduation_math_ii',2024,'written',120),('graduation_math_ii',2024,'mcq',40),('preexam_math_ii',2022,'mcq',40),('preexam_math_ii',2023,'mcq',40),('preexam_math_ii',2023,'written',120),('preexam_math_ii',2024,'mcq',40),('preexam_math_ii',2024,'written',120)]:
 rs=[r for r in rows if (r['exam_type'],r['year'],r['paper'])==(c,y,p) and r['verification_status']=='visual_fields_checked']
 C('source printed sum '+str((c,y,p)),sum((r['printed_marks']or 0)for r in rs)==total)
 if p=='written':
  for q in range(1,13):
   actual=sum((r['printed_marks']or 0)for r in rs if r['question']==str(q));expected=(4 if q<=5 else 6 if q<=10 else 10)if y==2026 else (4 if c=='uec_math_i'and q<=5 else 10)
   C('each big-question source sum '+str((c,y,q)),actual==expected)
for st in L('statistics.json'):
 C('five categories do not mix denominator '+st['exam_type'],st['available_pdfs']==sum(f['exam_type']==st['exam_type']for f in inv))
 C('unverified years not zero-filled '+st['exam_type'],set(st['sample_years'])<=set(st['available_pdf_years'])and all(year in st['sample_years']for year in {r['year']for r in rows if r['exam_type']==st['exam_type']and r['statistics_eligible']}))
 C('no actual student marks invented '+st['exam_type'],st['actual_score_weight']is None)
 for ch in st['chapters']:
  for paper in ['mcq','written']:
   rr=[r for r in rows if r['exam_type']==st['exam_type']and r['statistics_eligible']and r['paper']==paper and r['primary_chapter']==ch['chapter']]
   C('single primary mark attribution '+str((st['exam_type'],ch['chapter'],paper)),ch['papers'][paper]['printed_marks']==sum(r['printed_marks']for r in rr))
for y,total,n,per in [(2022,90,6,15),(2023,84,7,12),(2024,75,8,None),(2025,84,7,12)]:
 rs=[r for r in rows if r['exam_type']=='semester_final'and r['year']==y and r['paper']=='written']
 C('school historical printed pool '+str(y),sum(r['printed_marks']for r in rs)==total)
 for q in range(1,n+1):
  expected=per if per else 6 if q<=5 else 15
  C('school historical question total '+str((y,q)),sum(r['printed_marks']for r in rs if r['question']==str(q))==expected)
for r in rows:
 if r.get('inferred_marks')is not None:
  C('inference never certified as printed mark '+r['id'],r['printed_marks']is None and not r['statistics_eligible'])
freq=L('sample-frequency.json')
for f in freq:
 C('frequency has explicit complete sample years '+f['exam_type']+f['format_regime'],bool(f['years'])and f['population_confidence']=='not_full_history')
 for ch in f['chapters']:
  C('frequency counts years not subquestions '+str((f['exam_type'],f['format_regime'],ch['chapter'])),ch['year_numerator']==len(ch['primary_years'])and ch['year_denominator']==len(f['years']))
  if f['exam_type']=='uec_math_ii'and f['format_regime']=='old_40_60':
   y=next(y for y in ch['annual_printed_exposure']if y['year']==2024)
   C('missing cover leaves per-question mark share null '+str(ch['chapter']),y['papers']['mcq']['printed_share_percent']is None)
C('all supplied original pages actually reviewed',all(p['visual_status']=='viewed_source_page'and not p['needs_visual_review']for p in pages))
coverage=L('paper-coverage.json');C('61 supplied paper populations, missing pre22 written not invented',len(coverage)==61 and not any(p['exam_type']=='preexam_math_ii'and p['year_candidate']==2022 and p['paper']=='written'for p in coverage))
for p in coverage:
 C('all supplied big-question numbers accounted '+str((p['exam_type'],p['year_candidate'],p['paper'])),p['observed_question_numbers']==p['expected_question_numbers']and not p['independent_full_solution_certification'])
for r in rows:
 if r['year']==2020 and r['exam_type']in['uec_math_i','uec_math_ii']:
  C('2020 filename evidence never promoted to cover evidence '+r['id'],r['evidence_fields']['year']=='source_filename_2020_without_printed_cover')
 if r['paper']=='mcq'and r['year']==2020:
  C('2020 unknown MCQ marks remain unknown '+r['id'],r['printed_marks']is None)
reconciled=json.loads((R/'reports/math-exams/REPORT_CLAIM_RECONCILIATION.json').read_text())
C('all778 report claims reconciled without deleting original claims',reconciled['count']==len(L('imported-claims.json'))==778)
known_ids={r['id']for r in rows}
for c in reconciled['claims']:
 C('claim locator references actual reviewed unit '+c['claim_id'],bool(c['source_unit_ids'])and set(c['source_unit_ids'])<=known_ids and c['original_claim_verification_status']=='needs_review')
older=json.loads((R/'reports/math-exams/OLDER_INDEPENDENT_CALCULATIONS.json').read_text());by_q={r['id']:r for r in rows}
for c in older['checks']:
 C('independent computation tied to exact reviewed formula '+c['name'],c['status']=='pass'and hashlib.sha256(by_q[c['id']]['formula_latex_verified'].encode()).hexdigest()==c['formula_sha256'])
# Preserve existing curriculum, all teaching/illustration/vendor resources and prior study state code.
base='efd3445';tracked=subprocess.check_output(['git','ls-tree','-r','--name-only',base],cwd=R,text=True).splitlines();protected=[p for p in tracked if p.startswith(('lessons/','assets/','data/','vendor/','illustrations/','ui/','cloud/'))or p=='batch-ui.js']
for p in protected:C('original file protected '+p,subprocess.check_output(['git','show',base+':'+p],cwd=R)==(R/p).read_bytes())
bank=L('original-bank.json')['items'];C('original 84 distinct items',len(bank)==84 and len({q['id']for q in bank})==84);C('no invented subsection IDs',all(q['subchapter_id']is None for q in bank))
for q in bank:
 C('valid chapter '+q['id'],1<=q['primary_chapter']<=35)
 C('full original solution '+q['id'],len(q['solution_steps'])>=3 and q['answer'] and q['question_origin']=='original_generated')
 C('score sum '+q['id'],sum(p['marks']for p in q['marking_points'])==q['marks'])
 if q['kind']=='mcq':C('unique four choices and concrete explanations '+q['id'],len(q['options'])==len({x['text']for x in q['options']})==4 and all(len(o['reason'])>=10 for o in q['options'][1:]))
(R/'reports/math-exams/DATA_TESTS.json').write_text(json.dumps(dict(status='pass',assertions=len(checks),protected_files=len(protected),checks=checks,limits='Structural/scope/accounting checks, not a substitution for unperformed visual or teacher review.'),ensure_ascii=False,indent=2)+'\n')
print('PASS',len(checks),'data and protection assertions;',len(protected),'old files unchanged')
