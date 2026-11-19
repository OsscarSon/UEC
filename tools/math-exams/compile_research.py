"""Compile separate, denominator-explicit observations. Never treat missing as zero."""
from pathlib import Path
import json,collections,csv,re,hashlib
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams';OUT=R/'reports/math-exams'
def load(n):return json.loads((D/n).read_text())
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
claims=load('imported-claims.json');visual=[]
for p in sorted(D.glob('visual-review-*.json')):visual+=json.loads(p.read_text())
assert len({r['id'] for r in visual})==len(visual)
for r in visual:
 grade=load('visual-difficulty-review.json').get(r['id'])
 if grade:
  r['difficulty']={'level':grade,'status':'estimated','basis':'Explicit author review of steps, domain restrictions and modelling demand in the viewed PDF; not response statistics.'}

reviewed={(r['exam_type'],r['year'],r['paper'])for r in visual}
# Reviewed full-paper ledgers replace all old row granularity; old claims remain in original file.
records=[r for r in claims if (r['exam_type'],r['year'],r['paper'])not in reviewed]+visual
save(D/'research-ledger.json',records)
inv=load('source-inventory.json');dictionary=load('chapter-dictionary.json')
labels={'semester_final':'上半年校内期末考','graduation_math_ii':'下半年毕业考（高数II）','preexam_math_ii':'预试（高数II）','uec_math_i':'统考高级数学（I）','uec_math_ii':'统考高级数学（II）'}
# Confirmed reading spans, not merely pages that software rendered.
spans={('semester_final',2026):set(range(1,8)),('uec_math_i',2026):set(range(1,9)),('uec_math_ii',2026):set(range(1,7)),('preexam_math_ii',2025):set(range(1,7)),('graduation_math_ii',2025):set(range(1,9))}
for f in inv:
 if f['exam_type']=='semester_final' and f['year']in[2022,2023,2024,2025]:spans[f['source_id']]=set(range(1,f['pages']+1))
for c,y,frag,pages in [('uec_math_i',2025,'试卷二',range(1,5)),('uec_math_ii',2025,'试卷二',[1,5,6,7,8]),('uec_math_ii',2024,'试卷二',range(1,6)),('uec_math_i',2025,'试卷一',range(1,5)),('uec_math_ii',2024,'试卷一',range(1,4)),('uec_math_ii',2025,'试卷一',[1,5,6,7])]:
 for f in inv:
  if f['exam_type']==c and f['year']==y and frag in f['filename']:spans[f['source_id']]=set(pages)
page_audit=[]
for f in inv:
 pp=spans.get(f['source_id'],spans.get((f['exam_type'],f['year']),set()))
 for p in range(1,f['pages']+1):page_audit.append(dict(source_pdf_id=f['source_id'],page=p,text_or_ocr_extracted=True,formula_reliability_from_ocr=False,visual_status='viewed_source_page' if p in pp else 'not_visually_checked',needs_visual_review=p not in pp))
save(D/'page-audit.json',page_audit)
# Rows with disputed answer uniqueness can still support a topic observation, but are not used in precise rankings.
ambiguous={'uec_math_i:2026:mcq:5:whole','semester_final:2026:mcq:13:whole','preexam_math_ii:2025:mcq:7:whole'}
for r in records:
 r['statistics_eligible']=r.get('verification_status')=='visual_fields_checked' and r.get('printed_marks') is not None and r.get('primary_chapter') is not None and r['id']not in ambiguous
 r['scope_conflict']=r['exam_type']=='uec_math_i' and (r.get('primary_chapter')or 0)>29
 if r['scope_conflict']:r['statistics_eligible']=False
 if r['id']in ambiguous:r['review_issue']='question_conditions_or_options_need_teacher_resolution'
 # A parent printed mark b=5 and children with no individually printed marks are not double-counted.
 if r.get('reported_part_split'):r['statistics_eligible']=False
save(D/'research-ledger.json',records)
statistics=[]
for c,label in labels.items():
 fs=[f for f in inv if f['exam_type']==c];rs=[r for r in records if r['exam_type']==c];eligible=[r for r in rs if r['statistics_eligible']]
 years=sorted({f['year']for f in fs});sample_years=sorted({r['year']for r in eligible});chs=[]
 for chapter in dictionary:
  n=chapter['chapter']
  if c=='uec_math_i' and n>29:continue
  obs=[r for r in eligible if r['primary_chapter']==n];parts={}
  for paper in ['mcq','written']:
   pop=[r for r in eligible if r['paper']==paper];rr=[r for r in obs if r['paper']==paper]
   denom=sum(r['printed_marks']for r in pop)
   parts[paper]=dict(audited_units=len(rr),printed_marks=sum(r['printed_marks']for r in rr),denominator_audited_printed_marks=denom,share_of_audited_printed_marks=round(sum(r['printed_marks']for r in rr)/denom*100,3)if denom else None,years=sorted({r['year']for r in rr}),observed_paper_years=sorted({r['year']for r in pop}))
  observed=sorted({r['year']for r in obs})
  chs.append(dict(chapter=n,title=chapter['title'],observed_years=observed,observed_year_count=len(observed),sample_year_denominator=len(sample_years),year_rate_in_reviewed_sample=None,frequency_status='observed_lower_bound_in_partial_papers_not_full_year_frequency',topic_units=len(obs),papers=parts,heat_label='样本内出现；不足跨年冷热结论' if obs else '已核验样本未标到；不代表历届零频率',estimated_difficulty_counts=dict(collections.Counter(r['difficulty']['level']for r in obs if r['difficulty']['level'])),secondary_topic_units=sum(n in r.get('secondary_chapters',[])for r in eligible)))
 statistics.append(dict(exam_type=c,title=label,unreviewed_pages=sum(p['needs_visual_review']for p in page_audit if p['source_pdf_id']in{f['source_id']for f in fs}),available_pdfs=len(fs),available_pdf_years=years,available_pages=sum(f['pages']for f in fs),sample_years=sample_years,denominator_years=len(sample_years),reviewed_paper_years=[dict(year=y,paper=p)for cc,y,p in sorted(reviewed)if cc==c],pending_records=sum(r.get('verification_status')!='visual_fields_checked'for r in rs),visually_checked_units=sum(r.get('verification_status')=='visual_fields_checked'for r in rs),eligible_units=len(eligible),exclusions=[dict(id=r['id'],reason='scope_conflict'if r['scope_conflict']else r.get('review_issue')or'not_individually_printed_or_unverified')for r in rs if not r['statistics_eligible']],estimation_method='Descriptive partial-sample topic/printed-exposure analysis only. MCQ/written denominators stay separate. No full-history heat ranking; no student score difficulty.',confidence='limited_sample_not_population_inference',chapters=chs,actual_score_weight=None))
save(D/'statistics.json',statistics)
from sample_frequency import build
frequency_samples=build(records,dictionary,labels,OUT)
save(D/'sample-frequency.json',frequency_samples)
# The public UI only needs topic statistics and a compact audit ledger, not original question stems.
research_version='research-'+hashlib.sha256(json.dumps([statistics,frequency_samples],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:12]
public=dict(version=research_version,exam_types=statistics,frequency_samples=frequency_samples,inventory=[{k:v for k,v in f.items()if k!='private_input_path'}for f in inv],status_counts=dict(collections.Counter(r.get('verification_status')for r in records)),visual_units=len(visual),input_claims=len(claims),page_count=len(page_audit),visual_pages=sum(not p['needs_visual_review']for p in page_audit),full_history_verified=False)
(D/'research-data.js').write_text('window.MATH_EXAM_RESEARCH='+json.dumps(public,ensure_ascii=False,separators=(',',':'))+';\n')
with (OUT/'QUESTION_AUDIT.csv').open('w')as f:
 fields=['id','exam_type','year','paper','question','subquestion','source_pdf_id','source_page','primary_chapter','printed_marks','verification_status','statistics_eligible','scope_conflict','notes'];w=csv.DictWriter(f,fields,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(records)
fixes=[dict(id=r['id'],note=r['notes'],pdf=r['source_pdf_id'],page=r['source_page'])for r in visual if r.get('notes')]
save(OUT/'CORRECTIONS.json',fixes)
save(OUT/'AUDIT_SUMMARY.json',dict(unique_pdfs=len(inv),total_pages=len(page_audit),extracted_pages=len(page_audit),visually_viewed_pages=public['visual_pages'],visual_units=len(visual),imported_claims=len(claims),merged_ledger_units=len(records),statistics_eligible_units=sum(r['statistics_eligible']for r in records),pending_or_excluded_units=sum(not r['statistics_eligible']for r in records),all_history_questions_verified=False,missing_papers=[dict(exam_type='preexam_math_ii',year=2022,paper='written'),dict(exam_type='preexam_math_ii',year=2026,paper='both')],limits=['OCR is a locator, not formula evidence.','Unindexed questions in older papers are not included in pending-row counts.','Whole-paper confidence is not inherited from uploaded reports.']))
gaps=[]
for f in inv:
 pp=[p for p in page_audit if p['source_pdf_id']==f['source_id']];rr=[q for q in visual if q['source_pdf_id']==f['source_id']];pending=[p['page']for p in pp if p['needs_visual_review']]
 gaps.append(dict(source_pdf_id=f['source_id'],exam_type=f['exam_type'],year_candidate=f['year'],filename=f['filename'],sha256=f['sha256'],total_pdf_pages=f['pages'],unviewed_pdf_pages=pending,visually_read_pages=[p['page']for p in pp if not p['needs_visual_review']],reviewed_question_or_scoring_units=len(rr),known_answer_units=sum(q['answer_verified']is not None for q in rr),unknown_mark_unit_ids=[q['id']for q in rr if q['printed_marks']is None],total_question_population=None,remaining_actions=['逐页核对未查看页的题面或公式附录']if pending else ['继续核对未记录选项、独立答案及真实小节归属；已读页不等于全题答案验算通过'],source_authenticity='uploaded_copy_not_authenticated_by_issuer'))
save(OUT/'GAP_REGISTER.json',gaps)
lines=['# 五类高数考试：原卷核验与统计边界','','47份独立PDF、257页均已建立SHA-256来源登记并完成私有文本/OCR提取。OCR不等于逐符号目视核验。',f'当前明确目视查看{public["visual_pages"]}页，逐题/计分单元复核{len(visual)}条；全历史逐题核验仍未完成，未录入的历史题也不应由现有条目数推断总量。','','原PDF和原页截图保留在工作区私有来源目录，未复制到公开站点。公开数据记录题号、原页、规范化关键式及状态；题库只接入另行验证的原创题。','','## 分类样本与统计','','|考试|已提供年份|PDF|已目视单元|可计入样本单元|待核记录|','|---|---|---:|---:|---:|---:|']
for s in statistics:lines.append('|'+s['title']+'|'+','.join(map(str,s['available_pdf_years']))+'|'+str(s['available_pdfs'])+'|'+str(s['visually_checked_units'])+'|'+str(s['eligible_units'])+'|'+str(s['pending_records'])+'|')
lines+=['','限定题面样本的年度频率另见SAMPLE_FREQUENCY_REPORT.md与data/math-exams/sample-frequency.json；只在明确列出的年份内计算，旧新格式分开，不冒充全历史。', '', '详细每章选择/作答曝光统计见data/math-exams/statistics.json，分母为各自已核验样本的印刷分值，不是考生实际得分权重。旧选答作答总印刷120%或90%不得当成实际120分或90分；没有学生选题数据时actual_marks与effective_marks_model均保持null。','','目前已核验样本不足以认证各考试全部历年热门/冷门榜。可列样本内出现和未见，不能用缺失或未核验年份补零。历史报告的冷热结论仍是待原卷复核的研究主张，不直接驱动命题。难度仅为题面估计，没有实测正确率或区分度。','','## 已明确修正/争议','','见CORRECTIONS.json。包括n³误作n²、sin²误作sin³、反函数误记求导、转轴/圆章节误标、旋转轴错误、二阶/法线题型混淆、参数x=t−sin t误录、xe^(2x)误录、衰变题误写斜抛、极坐标面积误写旋转体积等。复核不自动认证全部历史答案。','','## 2026模板与历史格式','','已直接查看2026统考I、II和校内上半年原卷：15题选择×2%=30%，12题作答全部必答，依次5×4+5×6+2×10=70%；卷一60分钟、卷二120分钟。统考卷间15分钟；校内以各自卷首时段为准。毕业考/预试新模拟卷沿用用户指定2026目标模板，并不宣称提供了其2026原卷。','','2025统考I作答是5题必答各4%、7题选4各10%，印刷90%、实际60%；2024/2025统考II及2025毕业/预试是12题选四组共6题，印刷120%、实际60%。年份制度独立保存，模拟生成不得倒改旧制。','','## 课程保护与范围冲突','','现有116章编号/名称/顺序不变；输入包字典仅作别名对照，未覆盖网站。高数I仅按当前1–29章生成，II按1–35；2026I原卷选择第12题反射按系统字典落32章，保留原卷I身份并列范围冲突，不能因此迁移课程或谎称范围内已确认。未知真实小节ID保持null。','','## 附录和卷首差异\n\nformat-observations.json记录原卷封面与实际扫描范围。2026统考I、II虽包含所见全部题面，但公式表页未随这些扫描提供；不能称所有印刷附录齐全。2026校内卷二印12.00a.m.同时标2小时，保留笔误待学校确认。\n\n## 下一步缺口','','2018–2023统考大量扫描题、2024高数I题面、毕业考2021–2024及预试2022–2024逐符号/图形核验、所有历史题答案的第二遍独立核算仍需继续。上半年校内2022–2026所供题面已读，但2022缺封面与分值、部分年份选项及全部历史答案独立验证仍未完成。2022预试作答、2026预试原卷未提供；不伪造。复核页面与条目清单均可机器追溯。','']
(OUT/'RESEARCH_REPORT.md').write_text('\n'.join(lines))
print('Compiled',len(records),'records;',len(visual),'visual units; partial-sample statistics kept separate')
