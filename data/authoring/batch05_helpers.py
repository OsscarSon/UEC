"""Compile explicitly authored topic-specific teaching, never synthesize textbook IDs."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
BASE={};NOTES={};REG=[]
NAMES={'bio':'生物','phys':'物理','chem':'化学','math':'数学'}
CODES={'bio':'biology','phys':'physics','chem':'chemistry','math':'math_shared'}
def Q(q,given,analysis,method,principle,steps,ans,verification,pitfall):
 return dict(q=q,given=given,analysis=analysis,method=method,principle=principle,steps=steps.split('||'),ans=ans,verification=verification,pitfall=pitfall,question_origin='original',paper_no=None)
def U(prefix,ch,sid,title,goals,pre,body,derive,examples,practice,quiz,exam,errors,quick,visual,source,directory,page):
 assert len(examples)>=3 and len(practice)>=4
 assert sid.startswith(str(ch)+'.')
 paragraphs=body.strip().split('\n');assert len(paragraphs)>=5
 g=goals.split('|');assert 2<=len(g)<=3
 refs=['e0','e2','p3'];allq=examples+practice+[quiz]
 for q in allq:
  assert all(q.get(f) for f in ['given','analysis','method','principle','steps','ans','verification','pitfall'])
  assert len(q['steps'])>=2
  q.update(subject_code=CODES[prefix],chapter_id=ch,primary_section=sid,related_sections=[])
 src=[dict(source_id='directory_'+prefix,url=directory,page=page,version='教材内容表/目录对照；非考试纲要',access_date='2026-11-18',verification_status='partially_verified'),dict(source_id='theory_'+prefix+'_'+sid,url=source,page_or_section=source.rsplit('/',1)[-1],version='原理参考；不是2027范围声明',access_date='2026-11-18',verification_status='partially_verified')]
 base=BASE.setdefault((prefix,ch),dict(syl='原章框架；2027适用另核',status='原创教学内容，非官方题；真实小节目录与来源逐项登记，教师审定待完成。',sections=[],method=dict(format=['学校安排与正式UEC范围请分别查看科目资料。'],steps=['先核对象、条件和方向，再选择模型、推理与复核。'],types=['原创基础、标准、综合迁移题；不虚构考频。'],score=['步骤为教学建议，未经官方评分表确认不赋步骤分。']),ex=[],pr=[],vid=[]))
 base['sections'].append(dict(id=sid,t=title,syl='原教材章/节；来源见本节',body=paragraphs[:3],figs=[],terms='',tips=[['易错'+str(i+1),e] for i,e in enumerate(errors.split('|'))]))
 unit=dict(subject=NAMES[prefix],subject_code=CODES[prefix],chapter_id=ch,section_id=sid,goals=g,prerequisites=pre.split('|'),flow=quick.split('|'),concept_relation='；'.join(quick.split('|')),deep=paragraphs[3:],derive=derive.strip().split('\n'),examples=examples,practice=practice,quiz=quiz,exam=exam.split('|'),quick=quick.split('|'),exam_evidence=[],content_sources=src,authoring_sources=src,verification_status='partially_verified',strategy=dict(trigger=exam.split('|')[0],method=examples[2]['method'],principle=examples[2]['principle'],worked_example_index=2,verification=examples[2]['verification'],pitfall=examples[2]['pitfall']),diagnostics=[],error_analysis=[dict(wrong_approach=quiz['pitfall'],correction=quiz['ans'],verification=quiz['verification'])],illustration_spec=visual)
 for i in range(len(g)):
  ref=refs[i];q=examples[int(ref[1:])] if ref[0]=='e' else practice[int(ref[1:])]
  unit['diagnostics'].append(dict(goal_index=i,question_ref=ref,review_module=4 if i==0 else 5,feedback='目标“'+g[i]+'”的抽样复核：'+q['verification']+'；若出现“'+q['pitfall']+'”，回读本节概念与适用条件，再重做本题。此题不是该目标全部子技能的唯一验收。'))
 NOTES.setdefault((prefix,ch),{})[sid]=unit
 REG.append(dict(subject=NAMES[prefix],chapter_id=ch,section_id=sid,section_title=title,source_url=directory,page=page,scope='已对照当前原章号和名称；不声称找回Claude原照片'))
def save():
 for (p,ch),b in BASE.items():
  (R/f'data/base-lessons/{p}{ch:02}.json').write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
  (R/f'data/notes/{p}{ch:02}.json').write_text(json.dumps(NOTES[p,ch],ensure_ascii=False,indent=2)+'\n')
  (R/f'data/batch05/{p}{ch:02}-sections.json').write_text(json.dumps([x for x in REG if x['subject']==NAMES[p] and x['chapter_id']==ch],ensure_ascii=False,indent=2)+'\n')
