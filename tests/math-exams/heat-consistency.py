"""Independent SQLite question counting and Fraction normalization, including missingness."""
from pathlib import Path
import json,sqlite3,collections,math
from fractions import Fraction
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams';checks=[]
def L(n):return json.loads((D/n).read_text())
def C(name,v):assert v,name;checks.append(name)
raw=L('research-ledger.json');qs=L('independent-questions.json');heat=L('heat-statistics.json');inv={x['source_id']:x for x in L('source-inventory.json')}
db=sqlite3.connect(':memory:');db.execute('create table source(c,y,p,n,unit)');db.executemany('insert into source values (?,?,?,?,?)',[(r['exam_type'],r['year'],r['paper'],r['question'],r['id'])for r in raw]);sql=db.execute('select c,y,p,n,count(*) from source group by c,y,p,n').fetchall();C('SQL independent question population945',len(sql)==len(qs)==945);C('SQL unit population1479',sum(x[4]for x in sql)==len(raw)==1479)
for q in qs:
 C('unique main chapter '+q['id'],isinstance(q['primary_chapter'],int)and q['primary_chapter']not in q['secondary_chapters'])
 C('source membership once '+q['id'],set(q['unit_ids'])=={r['id']for r in raw if(r['exam_type'],r['year'],r['paper'],int(r['question']))==(q['exam_type'],q['year'],q['paper'],q['number'])})
 for r in q['references']:C('real source page '+r['unit_id'],r['pdf']in inv and 1<=r['page']<=inv[r['pdf']]['pages'])
for st in heat['exam_types']:
 code=st['exam_type'];C('includes all available original year candidates '+code,{r['year']for r in raw if r['exam_type']==code}<={a['year']for a in st['annual']})
 for annual in st['annual']:
  y=annual['year'];yearqs=[q for q in qs if q['exam_type']==code and q['year']==y];cnt=collections.Counter(q['primary_chapter']for q in yearqs)
  C('observed main totals include no duplicate subparts '+str((code,y)),sum(c['observed_count']for c in annual['cells'])==len(yearqs))
  C('complete year means two papers and verified year '+str((code,y)),annual['valid']==bool(annual['complete_question_numbers']and annual['source_year_confirmed']and not annual['unmapped_question_count']))
  for cell in annual['cells']:
   C('independent topic count '+str((code,y,cell['chapter'])),cell['observed_count']==cnt[cell['chapter']])
   C('no missing equals zero '+str((code,y,cell['chapter'])),(cell['count']is None and cell['normalized_share']is None)if not annual['valid']else cell['count']==cnt[cell['chapter']]and abs(cell['normalized_share']-float(Fraction(cnt[cell['chapter']],len(yearqs))))<1e-12)
   C('cell evidence count '+str((code,y,cell['chapter'])),len(cell['question_ids'])==cell['observed_count'])
 for mode,b in st['boards'].items():
  years=[a for a in st['annual']if a['valid']and(mode=='combined'or(mode=='old'and a['year']<=2025)or(mode=='new'and a['year']==2026))]
  C('all effective years no rolling cutoff '+str((code,mode)),b['years']==[a['year']for a in years])
  if not years:C('absent2026 is not zero board '+code,all(r['question_count']is None and r['rank']is None for r in b['entries']));continue
  means=[]
  for row in b['entries']:
   counts=[next(c['count']for c in y['cells']if c['chapter']==row['chapter'])for y in years];rate=sum((Fraction(c,y['question_count'])for c,y in zip(counts,years)),Fraction())/len(years);means.append(rate)
   C('exact year-equal normalization '+str((code,mode,row['chapter'])),Fraction(row['mean_annual_fraction'])==rate and abs(row['mean_annual_share']-float(rate))<1e-12)
   C('one vote and occurrence years '+str((code,mode,row['chapter'])),row['question_count']==sum(counts)and row['appearance_count']==sum(c>0 for c in counts)and row['appearance_years']==[y['year']for c,y in zip(counts,years)if c>0])
   value=row['mean_annual_share']if mode=='combined'else row['question_count'];others=[r['mean_annual_share']if mode=='combined'else r['question_count']for r in b['entries']];C('competition ranking retains ties '+str((code,mode,row['chapter'])),row['rank']==1+sum(v>value for v in others))
   if mode=='new':
    low=b['nonzero_quantile_cutoffs']['lower'];high=b['nonzero_quantile_cutoffs']['upper'];v=row['question_count'];label='本年未考'if v==0 else '中'if len({r['question_count']for r in b['entries']if r['question_count']})==1 else '低'if v<=low else '高'if v>high else '中';C('2026 zero and nonzero intensity '+str((code,row['chapter'])),row['intensity']==label)
  C('annual normalized shares sum exactly1 '+str((code,mode)),sum(means)==1)
 for change in st['changes']:
  if change['delta']is None:C('no change label without new sample '+code,change['tags']==['缺少可比样本'])
  else:C('signed percentage-point change '+str((code,change['chapter'])),abs(change['delta']-(change['new_share']-change['old_share']))<1e-12)
C('pre22 partial cannot lower all-year rates',next(a for s in heat['exam_types']if s['exam_type']=='preexam_math_ii'for a in s['annual']if a['year']==2022)['status']=='partial_paper')
C('old II sample reaches2018 and2019',next(s for s in heat['exam_types']if s['exam_type']=='uec_math_ii')['boards']['old']['years'][:2]==[2018,2019])
C('source scope conflicts retained in evidence',any(q['scope_conflict']for q in qs))
com=L('historical-completions.json');C('67 newly completed source scoring units',len(com)==67)
C('60MCQ plus7written units',sum(':mcq:'in k for k in com)==60 and sum(':written:'in k for k in com)==7)
for k,c in com.items():
 C('independent nonofficial solution '+k,len(c['historical_solution_steps'])>=3 and c['independent_verification']['result']=='pass'and c['marking_scheme_status']=='author_suggested_not_official')
 if ':mcq:'in k:C('four distinct source choice transcriptions '+k,len(c['options_verified'])==4 and len(set(c['options_verified'].values()))==4)
 else:C('written teaching rubric matches printed marks '+k,sum(m['marks']for m in c['historical_marking_points'])==next(r['printed_marks']for r in raw if r['id']==k))
C('graph choices not falsely claimed as reproduced assets',all('semantic_graph_descriptions'in com[k]['options_representation']for k in ['uec_math_i:2022:mcq:12:whole','uec_math_i:2023:mcq:13:whole']))
(R/'reports/math-exams/HEAT_CONSISTENCY_TESTS.json').write_text(json.dumps(dict(status='pass',assertions=len(checks),checks=checks,limits='Independent accounting and normalization; not proof of all historical mathematical answers.'),ensure_ascii=False,indent=2)+'\n');print('PASS',len(checks),'independent question, trace and normalization assertions')
