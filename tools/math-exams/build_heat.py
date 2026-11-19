"""Independent-question counts; each (exam, year, paper, printed number) votes once.
Analytical primary classifications do not certify answers or official topic labels.
"""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction
import json,hashlib,math
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams';O=R/'reports/math-exams'
def load(n):return json.loads((D/n).read_text())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def percentile(a,p):
 a=sorted(a);i=(len(a)-1)*p;lo=math.floor(i);hi=math.ceil(i);return a[lo]+(a[hi]-a[lo])*(i-lo)if a else None
rows=load('research-ledger.json');inv=load('source-inventory.json');formats=load('format-observations.json');coverage=load('paper-coverage.json');chapters=load('chapter-dictionary.json')
labels={s['exam_type']:s['title']for s in load('statistics.json')};groups=defaultdict(list)
for r in rows:
 if r['verification_status']=='visual_fields_checked':groups[(r['exam_type'],r['year'],r['paper'],r['question'])].append(r)
questions=[]
for (c,y,p,n),rs in sorted(groups.items()):
 # Parent marking units have children, but the parent's printed marks count once.
 atoms=[r for r in rs if not r.get('reported_part_split')]
 mass=defaultdict(float);first={}
 for i,r in enumerate(atoms):
  ch=r['primary_chapter']
  if ch is not None:
   first.setdefault(ch,i);mass[ch]+=r['printed_marks']or 0
 chosen=sorted(mass,key=lambda ch:(-mass[ch],first[ch],ch))[0]if mass else None
 if chosen is None:
  chosen=next((r['primary_chapter']for r in rs if r['primary_chapter']is not None),None)
 known={r['primary_chapter']for r in rs if r['primary_chapter']is not None}|{v for r in rs for v in r['secondary_chapters']}
 children=[r for r in rs if not any(s['subquestion']!=r['subquestion']and s['subquestion'].startswith(r['subquestion']+'(')for s in rs)]
 # Duplicate audit parents such as pre25 b are not independent subquestions.
 if len(rs)==1:children=rs
 printed=sum((r['printed_marks']or 0)for r in atoms)
 missing=[r for r in atoms if r['printed_marks']is None and not any(k['printed_marks']is not None and r['subquestion'].startswith(k['subquestion']+'(')for k in atoms)]
 all_marks=not missing
 questions.append(dict(id=f'{c}:{y}:{p}:{n}',exam_type=c,year=y,paper=p,number=int(n),primary_chapter=chosen,secondary_chapters=sorted(known-{chosen}),primary_basis='single chapter in reviewed subparts'if len(known)==1 else 'dominant sum of printed subpart marks; ties use first primary task; author analytical taxonomy, not official label',primary_confidence='derived_from_reviewed_topic_fields',primary_mark_mass=dict(mass),mapping_incomplete=any(r['primary_chapter']is None for r in rs),scope_conflict=c=='uec_math_i'and chosen is not None and chosen>29,scoring_units=len(rs),subquestion_count=len(children),unit_ids=[r['id']for r in rs],printed_marks=printed if all_marks else None,actual_available_marks=None,answer_recorded_units=sum(r['answer_verified']is not None for r in rs),all_answers_recorded=all(r['answer_verified']is not None for r in rs),official_answer_key_certified=False,answer_issue=any(r.get('review_issue')for r in rs),references=[dict(unit_id=r['id'],pdf=r['source_pdf_id'],page=r['source_page'],subquestion=r['subquestion'],topic=r['topic'],primary_chapter=r['primary_chapter'],secondary_chapters=r['secondary_chapters'],printed_marks=r['printed_marks'],formula=r['formula_latex_verified'],figure=r['figure_description_verified'],answer_status=r['answer_status'],answer=r['answer_verified'],options=r.get('options_verified'),options_representation=r.get('options_representation'),solution_steps=r.get('historical_solution_steps'),marking_points=r.get('historical_marking_points'),marking_scheme_status=r.get('marking_scheme_status'),notes=r['notes'])for r in rs]))
save(D/'independent-questions.json',questions)
# Rendering the actual source remains required for any previously missing answer/option.
summary=[]
for c,label in labels.items():
 years=sorted({f['year']for f in inv if f['exam_type']==c}|{2026});annual=[]
 for y in years:
  qs=[q for q in questions if q['exam_type']==c and q['year']==y];fm=next((f for f in formats if f['exam_type']==c and f['year']==y),None)
  cs=[p for p in coverage if p['exam_type']==c and p['year_candidate']==y]
  year_confirmed=bool(fm and fm.get('exam_date_as_printed'))
  complete={p['paper']for p in cs}=={'mcq','written'}and all(p['observed_question_numbers']==p['expected_question_numbers']for p in cs)
  mapped=all(q['primary_chapter']is not None for q in qs)
  valid=complete and mapped and year_confirmed
  status='verified_topic_population'if valid else 'missing_paper'if not qs else 'partial_paper'if not complete else 'year_unconfirmed'if not year_confirmed else 'mapping_pending'
  cells=[]
  for ch in chapters:
   ps=[q for q in qs if q['primary_chapter']==ch['chapter']];ss=[q for q in qs if ch['chapter']in q['secondary_chapters']]
   cnt=len(ps);cells.append(dict(chapter=ch['chapter'],count=cnt if valid else None,observed_count=cnt,normalized_share=float(Fraction(cnt,len(qs)))if valid and qs else None,normalized_fraction=f'{cnt}/{len(qs)}'if valid else None,subquestion_count=sum(q['subquestion_count']for q in ps),secondary_question_count=len(ss),printed_marks=sum(q['printed_marks']or 0 for q in ps)if all(q['printed_marks']is not None for q in qs)and valid else None,known_printed_marks=sum(q['printed_marks']or 0 for q in ps),mcq_count=sum(q['paper']=='mcq'for q in ps),written_count=sum(q['paper']=='written'for q in ps),question_ids=[q['id']for q in ps],secondary_question_ids=[q['id']for q in ss],status=('nonzero'if cnt else 'true_zero')if valid else status))
  annual.append(dict(year=y,regime='new_2026'if y==2026 else 'old_through_2025',valid=valid,status=status,source_year_confirmed=year_confirmed,complete_question_numbers=complete,question_count=len(qs)if valid else None,observed_question_count=len(qs),unmapped_question_count=sum(q['primary_chapter']is None for q in qs),partial_secondary_mapping_count=sum(q['mapping_incomplete']for q in qs),format_source=fm,cells=cells))
 boards={}
 for name in ['old','new','combined']:
  ys=[a for a in annual if a['valid']and(name=='combined'or(name=='old'and a['year']<=2025)or(name=='new'and a['year']==2026))]
  entries=[]
  for ch in chapters:
   cells=[next(x for x in a['cells']if x['chapter']==ch['chapter'])for a in ys];count=sum(v['count']for v in cells);appeared=[a['year']for a,v in zip(ys,cells)if v['count']>0];mean=sum((Fraction(v['normalized_fraction'])for v in cells),Fraction())/len(ys)if ys else None
   entries.append(dict(chapter=ch['chapter'],title=ch['title'],question_count=count if ys else None,subquestion_count=sum(v['subquestion_count']for v in cells)if ys else None,appearance_years=appeared,appearance_count=len(appeared)if ys else None,year_denominator=len(ys),frequency=len(appeared)/len(ys)if ys else None,mean_annual_share=float(mean)if mean is not None else None,mean_annual_fraction=str(mean)if mean is not None else None,printed_marks=sum(v['printed_marks']for v in cells)if ys and all(v['printed_marks']is not None for v in cells)else None,known_printed_marks=sum(v['known_printed_marks']for v in cells),mcq_count=sum(v['mcq_count']for v in cells),written_count=sum(v['written_count']for v in cells),scope_conflict=c=='uec_math_i'and ch['chapter']>29))
  metric='mean_annual_share'if name=='combined'else 'question_count';scores=[v[metric]for v in entries if v[metric]is not None];nonzero=[v['question_count']for v in entries if v['question_count']and name=='new'];lo=percentile(nonzero,1/3);hi=percentile(nonzero,2/3)
  for e in entries:
   e['rank']=1+sum(v>e[metric]for v in scores)if ys else None
   e['intensity']=('本年未考'if e['question_count']==0 else '中'if len(set(nonzero))==1 else '低'if e['question_count']<=lo else '高'if e['question_count']>hi else '中')if name=='new'and ys else None
  boards[name]=dict(years=[a['year']for a in ys],ranking_metric=metric,available=bool(ys),entries=entries,nonzero_quantile_cutoffs=dict(lower=lo,upper=hi,method='linear interpolated 1/3 and 2/3 quantiles; low <=lower, high >upper, otherwise medium; all equal =>medium; ties unsplit, tiers may be empty')if name=='new'else None)
 old=boards['old'];new=boards['new'];changes=[]
 oldshares=[v['mean_annual_share']for v in old['entries']if v['mean_annual_share']and v['mean_annual_share']>0];high=percentile(oldshares,2/3);low=percentile(oldshares,1/3)
 for a,b in zip(old['entries'],new['entries']):
  baseline=a['mean_annual_share'];current=b['mean_annual_share'];delta=current-baseline if baseline is not None and current is not None else None
  # Fixed two-percentage-point threshold is documented, not a significance test.
  tags=[]
  if delta is not None:
   if baseline>0 and baseline>=high and b['intensity']=='高':tags.append('持续热门')
   if delta>=.02-1e-12:tags.append('新制上升')
   elif delta<=-.02+1e-12:tags.append('新制下降')
   if baseline<=(low or 0)and b['intensity']in['低','本年未考']:tags.append('持续低频')
   if not tags:tags=['变化有限']
  changes.append(dict(chapter=a['chapter'],old_share=baseline,new_share=current,delta=delta,tags=tags or ['缺少可比样本'],limitation='2026只有一年；描述性变化，不是预测、显著性或因果结论。'))
 summary.append(dict(exam_type=c,title=label,annual=annual,boards=boards,changes=changes,limits=['独立题号只计一次；主章按已复核小问的印刷分值主导、平分取首主任务，属于系统分析分类而非官方章标。','次章节与小问另列，不重复进入主榜。','缺卷、年份未确认、映射未确认为null，不以0代替。','旧选答印刷分值不等于考生实际分值；没有选题数据不作权重假设。','全历年按每年总题数标准化后等权平均；不按跨年总题量加权。','原卷题面字段复核不认证所有答案、评分细则或发行真实性。']))
version='heat-'+hashlib.sha256(json.dumps(summary,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:12]
payload=dict(version=version,exam_types=summary,independent_questions=len(questions),scoring_units=len(rows),method_version='independent-question-v2.0',evidence_url='data/math-exams/independent-questions.json')
save(D/'heat-statistics.json',payload)
# Compact topic statistics load for assembly; detailed references lazy fetch on demand.
(D/'heat-data.js').write_text('window.MATH_HEAT='+json.dumps(payload,ensure_ascii=False,separators=(',',':'))+';\n')
lines=['# 三套独立题目冷热榜 2.0','','每个(考试类别,年份,试卷,原大题题号)只计一次；605道选择与340道作答，共945道独立题目，小问/计分单元1479条另列。五类考试独立，所有可证年份均保留，不限近三年。','','主章：同章题直接沿用复核章标；跨章题按已印小问分值的同章合计最大者确定，平分取首个主任务。此为可复现的作者分析分类，不是官方教材归属认证；其余章保留为次章。原卷超当前高数I1–29的章标仍显示，不迁移学习数据。','','旧制按所有有效≤2025年份独立题数排名；2026只对非零章的题数用1/3、2/3分位线分层，不高于低线为低、严格高于高线为高，其余为中；同题数不拆开，分位线重合时可能有一层为空，零题仅本年未考。若所有非零题数相同，则均为中，不强行拆并列。','','综合榜=各年(该章主问题数/当年总题数)的等权平均，使用有理数计算后显示；不是所有年份题数直接相加的占比。新旧变化用标准化占比相减，±2个百分点为上升/下降；旧制非零份额上三分位且新制高为持续热门，下三分位及新制低/零为持续低频；仅为描述，不是统计显著性。','','对只有文件名年份、缺卷或缺映射的年份展示已观察下界与具体题号，排名使用null排除；不把未知当本年未考。印刷分值是辅助曝光，未知不补2分，选答印刷120%不当实际120分。详细数据heat-statistics.json；逐题原页independent-questions.json。','']
for st in summary:
 lines.extend([f'## {st["title"]}','','|榜|有效年份|主指标|','|---|---|---|'])
 for mode,b in st['boards'].items():lines.append(f'|{mode}|'+(','.join(map(str,b['years']))or'无有效样本')+f'|{b["ranking_metric"]}|')
 lines+=['','未进主榜的来源年份：'+('；'.join(f'{a["year"]} {a["status"]}'for a in st['annual']if not a['valid'])or'无')+'。','']
(O/'HEAT_METHOD.md').write_text('\n'.join(lines)+'\n')
print('Built',len(questions),'independent questions and three boards for',len(summary),'exam categories')
