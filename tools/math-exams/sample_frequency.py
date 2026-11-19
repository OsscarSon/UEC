"""Frequency only within explicitly page-reviewed sample years and regimes.
The historical population is NOT assumed complete from imported report rows.
"""
from collections import Counter
import json
REGISTRY={
 'semester_final':{'old_40_60':[2023,2024,2025],'new_30_70':[2026]},
 'graduation_math_ii':{'old_40_60':[2025]},
 'preexam_math_ii':{'old_40_60':[2025]},
 'uec_math_i':{'old_40_60':[2025],'new_30_70':[2026]},
 'uec_math_ii':{'old_40_60':[2024,2025],'new_30_70':[2026]},
}
def build(records,dictionary,labels,out):
 result=[];lines=['# 限定样本的年度出现频率','','这里仅对已逐页阅读题面的年份计算，不代表全部已提供历史年份均已完成。按五类考试和旧40/60、新30/70分开，不将不同考试或制度的分值混算。题面字段复核不等于每道历史答案已独立验算。','','热门/冷门只在至少3个完整题面样本年内作描述：≥2/3年出现称“样本常见”，零年称“样本未见”；不足3年不作稳定冷热结论。出现频率只数年度，不把一题的多个小问当作多个年度。副章和主章分列。','','学校2022选择缺封面、单题分值未知，年份仅文件名，不纳入这组年度频率。2024统考II选择虽已看完，分值未知，保留题目与年度出现记录，分值占比保持null。已核实题面中的答案歧义不会被假装解决；对应题的主题出现单列，不使用其答案训练命题。','']
 for code,regimes in REGISTRY.items():
  for regime,years in regimes.items():
   rs=[r for r in records if r['exam_type']==code and r['year']in years and r.get('verification_status')=='visual_fields_checked']
   # Refuse silently incomplete MCQ collections before reporting annual rates.
   for y in years:
    expected=15 if y==2026 else 20
    assert len([r for r in rs if r['year']==y and r['paper']=='mcq'])==expected,(code,y)
   chs=[]
   lines.extend([f'## {labels[code]} · {regime}','','题面样本年份：'+', '.join(map(str,years))+'。完整历史总体：未完成；独立答案核算：非全量。','','|章|名称|主考年份|出现频率|样本说明|','|---:|---|---|---|---|'])
   for ch in dictionary:
    n=ch['chapter']
    if code=='uec_math_i'and n>29:continue
    primary=[r for r in rs if r['primary_chapter']==n];seen=sorted({r['year']for r in primary});secondary=sorted({r['year']for r in rs if n in r.get('secondary_chapters',[])})
    heat=('样本常见'if len(seen)/len(years)>=2/3 else '样本未见'if not seen else '样本偶见')if len(years)>=3 else '不足3年，不判稳定冷热'
    annual=[]
    for y in years:
     parts={}
     for paper in ['mcq','written']:
      pop=[r for r in rs if r['year']==y and r['paper']==paper and not r.get('reported_part_split')];rr=[r for r in pop if r['primary_chapter']==n]
      known=all(r['printed_marks']is not None for r in pop)
      denom=sum((r['printed_marks']or 0)for r in pop)
      # Children without printed marks must not invalidate their printed parent.
      unknown=[r for r in pop if r['printed_marks']is None]
      if unknown and all(any(p['question']==r['question']and p['subquestion']==r['subquestion'].split('(')[0]and p['printed_marks']is not None for p in pop)for r in unknown):known=True
      marks=sum((r['printed_marks']or 0)for r in rr)
      parts[paper]=dict(printed_marks=marks if known else None,denominator_printed_marks=denom if known else None,printed_share_percent=round(marks/denom*100,3)if known and denom else None,actual_student_weight=None,missing_mark_unit_ids=[r['id']for r in unknown])
     annual.append(dict(year=y,papers=parts))
    item=dict(chapter=n,title=ch['title'],primary_years=seen,secondary_years=secondary,year_numerator=len(seen),year_denominator=len(years),sample_year_frequency_percent=round(100*len(seen)/len(years),3),heat_label=heat,topic_units=len(primary),estimated_difficulty_counts=dict(Counter(r['difficulty']['level']for r in primary if r.get('difficulty')and r['difficulty']['level'])),annual_printed_exposure=annual)
    chs.append(item);lines.append(f'|{n}|{ch["title"]}|'+(', '.join(map(str,seen))or'未见')+f'|{len(seen)}/{len(years)}|{heat}|')
   result.append(dict(exam_type=code,title=labels[code],format_regime=regime,years=years,sample_confidence='source_field_reviewed_author_chapter_classification',population_confidence='not_full_history',empirical_difficulty=False,chapters=chs))
 (out/'SAMPLE_FREQUENCY_REPORT.md').write_text('\n'.join(lines)+'\n')
 return result
