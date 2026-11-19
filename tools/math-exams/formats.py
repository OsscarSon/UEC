"""Source cover observations. A topic ledger is not proof all PDF appendices exist."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams';inv=json.loads((D/'source-inventory.json').read_text());out=[]
def add(c,y,fragment,cover_pages,date,mcq,wr,choice,minutes,notes):
 f=next(f for f in inv if f['exam_type']==c and f['year']==y and fragment in f['filename'])
 out.append(dict(exam_type=c,year=y,source_pdf_id=f['source_id'],cover_pdf_pages=cover_pages,exam_date_as_printed=date,mcq_count=mcq,mcq_weight=30 if y==2026 else 40,written_weight=70 if y==2026 else 60,written_count=12,printed_written_marks=wr,selection_rule=choice,paper_minutes=minutes,evidence='source_pdf_cover_visually_read',authenticity='uploaded_copy_not_independently_authenticated_by_issuer',notes=notes))
add('uec_math_i',2026,'2026',[1,4],'2026-10-27',15,70,'all',[60,120],['所有15选择和12作答题面均在所供扫描中。','卷首提及公式表印刷2–4页，但所供PDF在两卷均跳到印刷第5页，公式表未随扫描提供。','专用Q12答案纸不是第13题。','保留卷首最后空白面声明与所见末题页的差异，未进行发行真实性认证。'])
add('uec_math_ii',2026,'2026',[1,4],'2026-10-23',15,70,'all',[60,120],['题面15选择、12作答均在所供扫描中。','两卷公式表印刷2–5页未在本6页PDF提供；不得称完整附录。'])
add('semester_final',2026,'2026',[2,5],'2026-05-11',15,70,'all',[60,120],['PDF第1页为命题蓝图，不得再次计题。','卷二时段印为10.00a.m.–12.00a.m.，同时写2小时；保留a.m.文字并标时段笔误待学校确认，计时以明确2小时为练习依据。'])
add('preexam_math_ii',2025,'2025',[1,4],'2025-08-28',20,120,'12选6，四组各至少1至多2',[60,120],['选择40、作答实际60；120仅印刷备选曝光。'])
add('graduation_math_ii',2025,'2025',[1,5],'2025-09-24',20,120,'12选6，四组各至少1至多2',[60,120],['不倒改为2026新制。'])
add('uec_math_i',2025,'试卷二',[1],'2025-11-04',20,90,'甲5必答各4，乙7选4各10',[60,120],['本文件只含卷二；选择20来自既有卷一/报告，选择逐题仍待核。','公式表2–4未在所供4页卷二PDF中。'])
add('uec_math_ii',2025,'试卷二',[1],'2025-11-01',20,120,'12选6，四组各至少1至多2',[60,120],['本文件含公式表2–4，已定位但未逐式核验。','此处选择20来自既有报告而非本卷二封面；该字段不是题面逐题核验结果。'])
add('uec_math_ii',2024,'试卷二',[1],'2024-11-06',20,120,'12选6，四组各至少1至多2',[60,120],['公式表印刷2–4未在所供5页PDF。','本卷二本身不证明选择题逐题数量；20来自既有报告。'])
for r in out:
 if r['year']!=2026 and r['exam_type']not in ['preexam_math_ii','graduation_math_ii']:
  r['reported_mcq_count']=r['mcq_count'];r['mcq_count']=None;r['reported_paper1_minutes']=r['paper_minutes'][0];r['paper_minutes'][0]=None
 r['mcq_count_evidence']='question_pages_visually_counted'if (r['year']==2026 or r['exam_type']in ['preexam_math_ii','graduation_math_ii'])else'uploaded_report_not_this_p2_cover'
(D/'format-observations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('Recorded',len(out),'source format observations including missing appendices')
