"""Source cover observations. A topic ledger is not proof all PDF appendices exist."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams';inv=json.loads((D/'source-inventory.json').read_text());out=[]
def add(c,y,fragment,cover_pages,date,mcq,wr,choice,minutes,notes,written_count=12):
 f=next(f for f in inv if f['exam_type']==c and f['year']==y and fragment in f['filename'])
 out.append(dict(exam_type=c,year=y,source_pdf_id=f['source_id'],cover_pdf_pages=cover_pages,exam_date_as_printed=date,mcq_count=mcq,mcq_weight=30 if y==2026 else 40,written_weight=70 if y==2026 else 60,written_count=written_count,printed_written_marks=wr,selection_rule=choice,paper_minutes=minutes,evidence='source_pdf_cover_visually_read',authenticity='uploaded_copy_not_independently_authenticated_by_issuer',notes=notes))
add('uec_math_i',2026,'2026',[1,4],'2026-10-27',15,70,'all',[60,120],['所有15选择和12作答题面均在所供扫描中。','卷首提及公式表印刷2–4页，但所供PDF在两卷均跳到印刷第5页，公式表未随扫描提供。','专用Q12答案纸不是第13题。','保留卷首最后空白面声明与所见末题页的差异，未进行发行真实性认证。'])
add('uec_math_ii',2026,'2026',[1,4],'2026-10-23',15,70,'all',[60,120],['题面15选择、12作答均在所供扫描中。','两卷公式表印刷2–5页未在本6页PDF提供；不得称完整附录。'])
add('semester_final',2026,'2026',[2,5],'2026-05-11',15,70,'all',[60,120],['PDF第1页为命题蓝图，不得再次计题。','卷二时段印为10.00a.m.–12.00a.m.，同时写2小时；保留a.m.文字并标时段笔误待学校确认，计时以明确2小时为练习依据。'])
add('preexam_math_ii',2025,'2025',[1,4],'2025-08-28',20,120,'12选6，四组各至少1至多2',[60,120],['选择40、作答实际60；120仅印刷备选曝光。'])
add('graduation_math_ii',2025,'2025',[1,5],'2025-09-24',20,120,'12选6，四组各至少1至多2',[60,120],['不倒改为2026新制。'])
add('uec_math_i',2025,'试卷二',[1],'2025-11-04',20,90,'甲5必答各4，乙7选4各10',[60,120],['另已阅读所供卷一全部4个PDF页：封面与20选择；两卷印刷公式表2–4均未随所供扫描提供。'])
add('uec_math_ii',2025,'试卷二',[1],'2025-11-01',20,120,'12选6，四组各至少1至多2',[60,120],['本卷二含公式表2–4，已定位但未逐式核验。','另已阅读卷一封面和第5–7页全部20选择；卷一公式表未逐式核验。'])
add('uec_math_ii',2024,'试卷二',[1],'2024-11-06',20,120,'12选6，四组各至少1至多2',[60,120],['公式表印刷2–4未在所供5页PDF。','本卷二本身不证明选择题逐题数量；所供配对卷一另有3个题面页。'])
add('semester_final',2025,'2025S3S12',[1],'2025-06-13',20,84,'甲2选1各12；乙5选4各12',[60,90],['另已读卷一全部20题与封面；印刷84不等于实际60。'],written_count=7)
add('semester_final',2024,'2024QMK_P2',[1],'2024-06-12',20,75,'A组1–5必答各6；B组6–8选2各15',[60,90],['另已读卷一全部20题与封面；印刷75不等于实际60。'],written_count=8)
add('semester_final',2023,'作答',[1],'2023-05-17',20,84,'甲2选1各12；乙5选4各12',[60,90],['另已读卷一全部20题与封面；此年卷二先于卷一进行（08:00–09:30与10:30–11:30），不得写成统一15分钟间隔。'],written_count=7)
add('preexam_math_ii',2024,'作答题',[1],'2024-08-29',20,120,'12选6，四组各至少1至多2',[60,120],['另已读卷一4页，08:00–09:00；卷二09:15–11:15。','原卷第12(b)共3%，两个小问未逐项给分，不重复计分。'])
add('preexam_math_ii',2023,'23S3S21',[1,4],'2023-08-21',20,120,'12选6，四组各至少1至多2',[60,120],['两卷各有封面，08:00–09:00与09:15–11:15。'])
add('preexam_math_ii',2022,'2022',[1],'2022-08-26',20,None,'作答卷未提供，选答规则未确认',[60,120],['只有卷一及其封面；封面说明40/60及第二阶段120分钟，但不证明未提供的作答题数或题目。'],written_count=None)
add('graduation_math_ii',2024,'2024',[2,6],'2024-10-02',20,120,'12选6，四组各至少1至多2',[60,120],['第1页是学校蓝图，不再计一套题。','第10a、10b题页为6%、4%，蓝图为5、5，以实际题页为分值依据。'])
add('graduation_math_ii',2022,'22S3Sbiye',[1,4],'2022-10-19',20,120,'12选6，四组各至少1至多2',[60,120],['卷二封面写4面，但所供为封面和两页题面，题1–12均出现；保留页面数声明差异。'])
add('graduation_math_ii',2021,'试卷二',[1],'2021-10-22',20,120,'12选6，四组各至少1至多2',[60,120],['另读卷一封面与20题，两卷均有独立文件。'])
add('uec_math_i',2023,'试卷二',[1],'2023-11-09',20,90,'甲5必答各4，乙7选4各10',[60,120],['另读卷一封面；两卷所供公式表2–4均已目视阅读。','选择第10题焦准轨迹按当前字典落33章，保留原卷科目并列当前1–29范围映射冲突。'])
add('uec_math_ii',2023,'试卷二',[1],'2023-11-06',20,120,'12选6，四组各至少1至多2',[60,120],['另读卷一封面，两卷公式表2–4均已读。','卷一18初值奇异、卷二4c退化底数、11a法线场表述分别保留核实问题。'])
f=next(f for f in inv if f['exam_type']=='graduation_math_ii'and f['year']==2023)
out.append(dict(exam_type='graduation_math_ii',year=2023,source_pdf_id=f['source_id'],cover_pdf_pages=[],exam_date_as_printed=None,mcq_count=20,mcq_weight=None,written_weight=None,written_count=12,printed_written_marks=120,selection_rule='题页可读四组每组至少1至多2；总选6仅报告未由缺失封面确认',paper_minutes=[None,None],evidence='source_question_pages_without_covers',authenticity='uploaded_annotated_copy_not_independently_authenticated_by_issuer',notes=['年份来自文件名；原红字答案未自动认证。','选择单题分、两卷时间及总选答规则保留待核；题页12大题及120%印刷分值已读。']))
f=next(f for f in inv if f['exam_type']=='semester_final'and f['year']==2022)
out.append(dict(exam_type='semester_final',year=2022,source_pdf_id=f['source_id'],cover_pdf_pages=[],exam_date_as_printed=None,mcq_count=20,mcq_weight=None,written_weight=60,written_count=6,printed_written_marks=90,selection_rule='A组2选1各15；B组4选3各15',paper_minutes=[None,None],evidence='source_question_pages_and_written_group_headers_visually_read',authenticity='uploaded_annotated_copy_not_independently_authenticated_by_issuer',notes=['原PDF没有封面，年份来自文件名；卷一总分、单题分、时间均未核实，2分只作推定。','原件红色答案属于附带批注，未自动认证为官方正确答案。','作答分项8.5、6.5照录，不四舍五入。']))
f=next(f for f in inv if f['exam_type']=='uec_math_i'and f['year']==2024)
out.append(dict(exam_type='uec_math_i',year=2024,source_pdf_id=f['source_id'],cover_pdf_pages=[],exam_date_as_printed=None,mcq_count=20,mcq_weight=None,written_weight=60,written_count=12,printed_written_marks=90,selection_rule='甲组5必答各4；乙组7选4各10',paper_minutes=[None,None],evidence='source_question_pages_and_written_group_headers_visually_read',authenticity='uploaded_copy_not_independently_authenticated_by_issuer',notes=['两卷封面均未提供，年份来自文件名，时间及选择单题分值未知。','写在题页上的甲20%乙40%与选答规则已读，作答备选题共印90%，不能当实际90%。']))
for r in out:
 if r['year']==2024 and r['exam_type']=='uec_math_ii':
  r['reported_mcq_count']=r['mcq_count'];r['mcq_count']=None;r['reported_paper1_minutes']=r['paper_minutes'][0];r['paper_minutes'][0]=None
 r['mcq_count_evidence']='question_pages_visually_counted'
 if r['year']==2024 and r['exam_type']=='uec_math_ii':
  r['mcq_count']=20;r['mcq_cover_missing']=True
  r['notes'].append('另已目视数出所供3页选择卷20题，但缺卷一封面，故卷一时间未确认，单题2分仅推定、不进入精确分值统计。')
 if r['year']==2025 and r['exam_type']in ['uec_math_i','uec_math_ii']:
  f=next(f for f in inv if f['exam_type']==r['exam_type']and f['year']==2025 and '试卷一'in f['filename'])
  r['mcq_cover_source_pdf_id']=f['source_id'];r['mcq_cover_pdf_page']=1
(D/'format-observations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('Recorded',len(out),'source format observations including missing appendices')
