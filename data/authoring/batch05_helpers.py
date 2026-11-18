"""Compile explicitly authored topic-specific teaching, never synthesize textbook IDs."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
BASE={};NOTES={};REG=[]
NAMES={'bio':'生物','phys':'物理','chem':'化学','math':'数学'}
CODES={'bio':'biology','phys':'physics','chem':'chemistry','math':'math_shared'}
DIAGNOSTIC_REFS={('bio', '18.1'): ['e2', 'e0'], ('bio', '18.3'): ['e0', 'p1'], ('bio', '18.4'): ['e0', 'e1'], ('bio', '11.3'): ['e2', 'p0'], ('phys', '1.2'): ['e0', 'q'], ('phys', '2.1'): ['e0', 'e1'], ('phys', '2.2'): ['e0', 'e1'], ('phys', '2.3'): ['e2', 'q'], ('phys', '5.1'): ['e1', 'e2'], ('phys', '5.2'): ['e0', 'e1'], ('phys', '5.3'): ['e0', 'p3'], ('phys', '7.1'): ['e0', 'p3'], ('phys', '7.3'): ['e1', 'q'], ('phys', '7.5'): ['p0', 'e1'], ('phys', '7.6'): ['p1', 'e2'], ('phys', '8.1'): ['e1', 'e2'], ('phys', '8.2'): ['e2', 'e1'], ('phys', '8.3'): ['e0', 'e1'], ('chem', '26.1'): ['e0', 'e1'], ('chem', '26.2'): ['e1', 'e2'], ('chem', '26.3'): ['e2', 'e0'], ('chem', '26.4'): ['e1', 'e2'], ('math', '4.1'): ['e2', 'e1'], ('math', '4.2'): ['e0', 'e1'], ('math', '4.4'): ['e1', 'e2']}
DIAGNOSTIC_REFS.update({('math','1.4'):['e0','q'],('math','1.5'):['e0','e1'],('math','1.7'):['e1','e2'],('math','5.5'):['e2','e0']})
DIAGNOSTIC_REFS.update({('chem','1.4.1'):['e0','e1'],('chem','1.4.2'):['e0','e1'],('chem','2.1.2'):['e0','e1'],('chem','2.2.2'):['e0','e1'],('chem','2.2.3'):['e0','e1'],('chem','29.3'):['e2','e0'],('chem','35.1'):['p0','e2'],('chem','35.4.1'):['e0','e1'],('chem','35.4.2'):['p0','e1'],('chem','35.5.1'):['p0','e1']})
# Causal reasoning and experimental decisions return to the appropriate teaching module.
DIAGNOSTIC_REVIEW={('bio','11.1'):[4,7],('bio','11.2'):[4,7],('bio','11.3'):[4,7],('bio','13.3'):[4,7],('bio','18.2'):[4,7],('bio','18.3'):[4,7],('bio','18.4'):[4,7],('bio','19.1'):[4,7],('bio','19.2'):[4,7],('bio','19.3'):[4,7],('bio','19.4'):[4,5],('bio','10.1'):[4,5],('bio','10.2'):[4,7],('bio','10.4'):[4,7],('chem','1.1'):[4,7],('chem','1.2'):[4,7],('chem','1.3'):[4,7],('chem','26.4'):[4,7],('chem','26.5'):[4,7],('chem','35.6'):[4,7],('phys','1.2'):[4,7]}
EXTRA_THEORY={('bio', '10.1'): ['https://openstax.org/books/biology-2e/pages/45-1-population-demography'], ('bio', '10.3'): ['https://openstax.org/books/biology-2e/pages/46-3-biogeochemical-cycles'], ('bio', '10.4'): ['https://openstax.org/books/biology-2e/pages/44-4-aquatic-biomes'], ('bio', '19.1'): ['https://openstax.org/books/biology-2e/pages/22-1-prokaryotic-diversity'], ('bio', '18.2'): ['https://openstax.org/books/microbiology/pages/9-1-how-microbes-grow'], ('chem', '29.1'): ['https://openstax.org/books/organic-chemistry/pages/9-1-naming-alkynes'], ('chem', '29.2'): ['https://openstax.org/books/organic-chemistry/pages/9-7-alkyne-acidity-formation-of-acetylide-anions'], ('chem', '29.4'): ['https://openstax.org/books/organic-chemistry/pages/9-4-hydration-of-alkynes', 'https://openstax.org/books/organic-chemistry/pages/9-summary-of-reactions']}
DIRECTORY_GROUPS={('chem', 1): [{'id': '1.4', 't': '化学的研究对象——物质', 'children': ['1.4.1', '1.4.2', '1.4.3', '1.4.4']}], ('chem', 2): [{'id': '2.1', 't': '水的性质', 'children': ['2.1.1', '2.1.2']}, {'id': '2.2', 't': '成水元素之一——氢元素', 'children': ['2.2.1', '2.2.2', '2.2.3']}], ('chem', 35): [{'id': '35.4', 't': '高分子化合物的化学性质', 'children': ['35.4.1', '35.4.2']}, {'id': '35.5', 't': '天然橡胶和合成橡胶', 'children': ['35.5.1', '35.5.2']}]}
def Q(q,given,analysis,method,principle,steps,ans,verification,pitfall):
 return dict(q=q,given=given,analysis=analysis,method=method,principle=principle,steps=steps.split('||'),ans=ans,verification=verification,pitfall=pitfall,question_origin='original',paper_no=None)
def U(prefix,ch,sid,title,goals,pre,body,derive,examples,practice,quiz,exam,errors,quick,visual,source,directory,page):
 assert len(examples)>=3 and len(practice)>=4
 assert sid.startswith(str(ch)+'.')
 paragraphs=body.strip().split('\n');assert len(paragraphs)>=5
 g=goals.split('|');assert 2<=len(g)<=3
 refs=DIAGNOSTIC_REFS.get((prefix,sid),['e0','e2','p3']);allq=examples+practice+[quiz]
 for q in allq:
  assert all(q.get(f) for f in ['given','analysis','method','principle','steps','ans','verification','pitfall'])
  assert len(q['steps'])>=2
  q.update(subject_code=CODES[prefix],chapter_id=ch,primary_section=sid,related_sections=[])
 src=[dict(source_id='directory_'+prefix,url=directory,page=page,version='教材内容表/目录对照；非考试纲要',access_date='2026-11-18',verification_status='partially_verified'),dict(source_id='theory_'+prefix+'_'+sid,url=source,page_or_section=source.rsplit('/',1)[-1],version='原理参考；不是2027范围声明',access_date='2026-11-18',verification_status='partially_verified')]
 for i,url in enumerate(EXTRA_THEORY.get((prefix,sid),[])):src.append(dict(source_id='extra_theory_'+sid+'_'+str(i),url=url,page_or_section=url.rsplit('/',1)[-1],version='专项原理参考；不是2027范围声明',access_date='2026-11-18',verification_status='partially_verified'))
 base=BASE.setdefault((prefix,ch),dict(syl='原章框架；2027适用另核',status='原创教学内容，非官方题；真实小节目录与来源逐项登记，教师审定待完成。',sections=[],method=dict(format=['学校安排与正式UEC范围请分别查看科目资料。'],steps=['先核对象、条件和方向，再选择模型、推理与复核。'],types=['原创基础、标准、综合迁移题；不虚构考频。'],score=['步骤为教学建议，未经官方评分表确认不赋步骤分。']),ex=[],pr=[],vid=[]))
 base['directory_groups']=DIRECTORY_GROUPS.get((prefix,ch),[])
 base['sections'].append(dict(id=sid,t=title,syl='原教材章/节；来源见本节',body=paragraphs[:3],figs=[],terms='',tips=[['易错'+str(i+1),e] for i,e in enumerate(errors.split('|'))]))
 unit=dict(content_batch='batch05',subject=NAMES[prefix],subject_code=CODES[prefix],chapter_id=ch,section_id=sid,goals=g,prerequisites=pre.split('|'),flow=quick.split('|'),concept_relation='；'.join(quick.split('|')),deep=paragraphs[3:],derive=derive.strip().split('\n'),examples=examples,practice=practice,quiz=quiz,exam=exam.split('|'),quick=quick.split('|'),exam_evidence=[],content_sources=src,authoring_sources=src,verification_status='partially_verified',strategy=dict(trigger=exam.split('|')[0],method=examples[2]['method'],principle=examples[2]['principle'],worked_example_index=2,verification=examples[2]['verification'],pitfall=examples[2]['pitfall']),diagnostics=[],error_analysis=[dict(wrong_approach=quiz['pitfall'],correction=quiz['ans'],verification=quiz['verification'])],illustration_spec=visual)
 for i in range(len(g)):
  ref=refs[i];q=examples[int(ref[1:])] if ref[0]=='e' else practice[int(ref[1:])] if ref[0]=='p' else quiz
  unit['diagnostics'].append(dict(goal_index=i,question_ref=ref,review_module=DIAGNOSTIC_REVIEW.get((prefix,sid),[4,5,7])[i],feedback='目标“'+g[i]+'”的抽样复核：'+q['verification']+'；若出现“'+q['pitfall']+'”，回读本节概念与适用条件，再重做本题。此题不是该目标全部子技能的唯一验收。'))
 NOTES.setdefault((prefix,ch),{})[sid]=unit
 REG.append(dict(subject=NAMES[prefix],chapter_id=ch,section_id=sid,section_title=title,source_url=directory,page=page,scope='已对照当前原章号和名称；不声称找回Claude原照片'))
def save():
 for (p,ch),b in BASE.items():
  (R/f'data/base-lessons/{p}{ch:02}.json').write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
  (R/f'data/notes/{p}{ch:02}.json').write_text(json.dumps(NOTES[p,ch],ensure_ascii=False,indent=2)+'\n')
  (R/f'data/batch05/{p}{ch:02}-sections.json').write_text(json.dumps([x for x in REG if x['subject']==NAMES[p] and x['chapter_id']==ch],ensure_ascii=False,indent=2)+'\n')
