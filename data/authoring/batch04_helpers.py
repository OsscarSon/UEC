"""Compile explicitly authored teaching material; does not invent sections or prose."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
DATA={}; BASE={}
def Q(q,g,a,m,steps,ans,v,err):
 return dict(q=q,given=g,analysis=a,method=m,steps=steps.split('||'),ans=ans,verification=v,pitfall=err,question_origin='original',paper_no=None)
def U(ch,sid,title,goals,pre,body,derive,examples,practice,quiz,exam,quick,labels,english,source):
 assert len(examples)==3 and len(practice)==4
 paras=body.strip().split('\n');der=derive.strip().split('\n');g=goals.split('|')
 for q in examples+practice+[quiz]:q['principle']=der[0]
 unit=dict(goals=g,prerequisites=pre.split('|'),flow=labels.split('|'),concept_relation='；'.join(quick.split('|')),deep=paras[-2:],derive=der,examples=examples,practice=practice,quiz=quiz,exam=exam.split('|'),quick=quick.split('|'),verification_status='partially_verified',exam_evidence=[],strategy=dict(trigger=exam.split('|')[0],method=examples[2]['method'],principle=der[0],worked_example_index=2,verification=examples[2]['verification'],pitfall=examples[2]['pitfall']),diagnostics=[dict(goal_index=i,question_ref=['e1','e2'][i],review_module=5 if i else 4,feedback='本目标复核：'+examples[i+1]['verification']+'；错因：'+examples[i+1]['pitfall']) for i in range(len(g))],error_analysis=[dict(wrong_approach=quiz['pitfall'],correction=quiz['ans'],verification=quiz['verification'])],authoring_sources=[dict(source_id='os_batch04_'+sid,url='https://openstax.org/books/chemistry-2e/pages/'+source,page_or_section=source,version='Chemistry 2e；理论辅助，非UEC范围',access_date='2026-11-18',verification_status='partially_verified')],illustration_spec=dict(labels=labels.split('|'),english=english,scientific_requirements=der))
 refs=json.loads((R/'data/authoring/goal_refs.json').read_text()).get(sid,['e1','e2'])
 for i,ref in enumerate(refs):
  q=examples[int(ref[1:])] if ref[0]=='e' else practice[int(ref[1:])] if ref[0]=='p' else quiz
  unit['diagnostics'][i].update(question_ref=ref,feedback='本目标抽样复核：'+q['verification']+'；错因：'+q['pitfall']+'。还需结合其他题检查目标的其余子技能。')
 principles=json.loads((R/'data/authoring/example_principles.json').read_text())[sid]
 for q,principle in zip(examples,principles):q['principle']=principle
 unit['strategy']['principle']=examples[2]['principle']
 DATA.setdefault(ch,{})[sid]=unit
 BASE.setdefault(ch,dict(syl='2026化学 '+{7:'1.5',8:'1.6',9:'3.2',10:'3.3',11:'3.4'}[ch],status='原创，非官方。依2017董总化学上册同版目录证据编写；不是恢复原Claude照片。2027适用未锁定。',sections=[],method=dict(steps=['先读目标与概念，再完成例题、练习与目标检测'],types=['原创题与知识迁移；无未经证实考频'],format=['学校安排与UEC范围分别查阅科目资料'],score=['未取得官方评分表，不赋步骤分']),ex=[],pr=[],vid=[]))['sections'].append(dict(id=sid,t=title,syl='2026化学 '+{7:'1.5',8:'1.6',9:'3.2',10:'3.3',11:'3.4'}[ch],body=paras[:-2],figs=[],terms='教学图尚待制作；现有文字、式子与步骤可独立学习。',tips=[['易错',quiz['pitfall']]],status='partially_verified'))
def save():
 for ch,u in DATA.items():
  (R/f'data/notes/chem{ch:02}.json').write_text(json.dumps(u,ensure_ascii=False,indent=2)+'\n')
  (R/f'data/base-lessons/chem{ch:02}.json').write_text(json.dumps(BASE[ch],ensure_ascii=False,indent=2)+'\n')
