"""Link supplied report claims to independently authored source-field ledgers.
A match is a locator, never an automatic promotion of a report's confidence.
"""
from pathlib import Path
import json,re,collections
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams';O=R/'reports/math-exams'
claims=json.loads((D/'imported-claims.json').read_text());rows=json.loads((D/'research-ledger.json').read_text())
def number(v):
 m=re.search(r'\d+',str(v));return str(int(m[0]))if m else str(v)
def sub(v):return re.sub('[^a-z0-9]','',str(v).lower())
lookup=collections.defaultdict(list)
for r in rows:lookup[(r['exam_type'],r['year'],r['paper'],r['question'])].append(r)
manual={
 'semester_final:2026:written:10:a':['semester_final:2026:written:10:a(i)','semester_final:2026:written:10:a(ii)'],
 'graduation_math_ii:2023:written:1:a.证明':['graduation_math_ii:2023:written:1:a-proof'],
 'graduation_math_ii:2023:written:1:a.解方程':['graduation_math_ii:2023:written:1:a-equation'],
 'graduation_math_ii:2023:written:4:a.i.分配':['graduation_math_ii:2023:written:4:a(i)-distribution'],
 'graduation_math_ii:2023:written:4:a.i.袋装':['graduation_math_ii:2023:written:4:a(i)-boxing'],
}
byid={r['id']:r for r in rows};result=[]
for c in claims:
 candidates=lookup[(c['exam_type'],c['year'],c['paper'],number(c['question']))]
 exact=[r for r in candidates if sub(r['subquestion'])==sub(c['subquestion'])]
 matches=exact or(candidates if c['subquestion']=='whole'else[])
 differences=[]
 if c['id']in manual:matches=[byid[k]for k in manual[c['id']]]
 if exact:
  r=exact[0]
  if c['reported_primary_chapter']!=r['primary_chapter']:differences.append('chapter_label_changed_by_source_review')
  if c['reported_printed_marks']!=r['printed_marks']:differences.append('printed_mark_changed_or_left_unknown')
  status='source_fields_replace_report_with_differences'if differences else 'source_locator_and_chapter_marks_agree_not_answer_certification'
 elif c['id']in manual:status='explicit_reviewed_label_correspondence'
 elif matches:status='whole_question_claim_replaced_by_source_subquestions'
 else:status='subquestion_label_needs_manual_correspondence'
 result.append(dict(claim_id=c['id'],claim_source=c['claim_source'],reported_primary_chapter=c['reported_primary_chapter'],reported_printed_marks=c['reported_printed_marks'],reported_topic=c['reported_topic'],status=status,differences=differences,source_unit_ids=[r['id']for r in matches],candidate_same_question_ids=[r['id']for r in candidates],source_fields=[dict(id=r['id'],chapter=r['primary_chapter'],printed_marks=r['printed_marks'],topic=r['topic'],pdf=r['source_pdf_id'],page=r['source_page'])for r in matches],original_claim_verification_status='needs_review',limits='Matching locators is mechanical; no report formula/answer/difficulty is certified by this comparison.'))
counts=dict(collections.Counter(r['status']for r in result));(O/'REPORT_CLAIM_RECONCILIATION.json').write_text(json.dumps(dict(count=len(result),status_counts=counts,claims=result),ensure_ascii=False,indent=2)+'\n')
lines=['# 附带研究报告与原卷审计的对应','','保留原始导入778条主张不变；网站使用独立逐页转录的1479条计分/题目单元。两者粒度不同，不能比较条目总数来判断题数是否相同。','','逐条旧主张→原页单元、章号及分值变化见[REPORT_CLAIM_RECONCILIATION.json](REPORT_CLAIM_RECONCILIATION.json)。自动匹配只用于定位和字段差异，不认证旧报告的公式、答案、难度或“人工核对”标签。','','|对应状态|旧主张数|','|---|---:|']
for k,v in counts.items():lines.append(f'|{k}|{v}|')
lines+=['','无法对应的小问保留同大题候选列表，不擅改原编号。旧报告整题单章的归类被原卷逐小问的多章记录取代，旧报告的选答“有效分值”没有作为实际考生权重。','','具体数学转录纠错与表述争议仍以[CORRECTIONS.json](CORRECTIONS.json)为准；2024毕业第10题分项采用原题6/4，不采用蓝图5/5。']
(O/'REPORT_CLAIM_RECONCILIATION.md').write_text('\n'.join(lines)+'\n');print('Reconciled',len(result),'supplied claims:',counts)
