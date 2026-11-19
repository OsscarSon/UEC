from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];folder=R/'reports/math-exams/generated'
for p in sorted(folder.glob('*.json')):
 paper=json.loads(p.read_text());out=folder/p.stem;out.mkdir(exist_ok=True)
 title='# '+paper['title']+'\n\n原创教学模拟，非官方试题。种子 '+paper['seed']+'；题库 '+paper['bank_version']+'。\n\n15×2分选择＋5×4、5×6、2×10分作答，共100分，全必答。卷一60分钟，卷二120分钟。\n\n'
 question=[title];answers=['# 答案卷\n'];solutions=['# 原创完整解析与教学评分点\n\n非官方评分细则，作答题需自主或教师核对。\n']
 for q in paper['questions']:
  heading=f'## {"选择"if q["kind"]=="mcq"else"作答"} {q["number"]} · 第{q["primary_chapter"]}章 · {q["marks"]}分\n'
  question += [heading,q['stem']+'\n']
  if q.get('figure'):question.append('![原创坐标图](../../../../'+q['figure']+')\n')
  if q.get('options'):question += ['\n'.join(f'{"ABCD"[i]}. {o["text"]}'for i,o in enumerate(q['options']))+'\n']
  answer=('ABCD'[q['correct_option']]+'：'+q['options'][q['correct_option']]['text'])if q['kind']=='mcq'else q['answer']
  answers.append(heading+'\n'+answer+'\n');solutions += [heading,'答案：'+answer+'\n']+ [f'{i+1}. {s}'for i,s in enumerate(q['solution_steps'])]+['\n教学评分点：\n']+[f'- {m["description"]}（{m["marks"]}分）'for m in q['marking_points']]+['\n易错：'+q['common_error']+'\n']
 for n,lines in [('paper.md',question),('answer_key.md',answers),('worked_solutions.md',solutions)]: (out/n).write_text('\n'.join(lines)+'\n')
 (out/'paper.json').write_text(json.dumps(paper,ensure_ascii=False,indent=2)+'\n')
 (out/'marking_scheme.json').write_text(json.dumps(dict(official=False,questions=[dict(id=q['id'],kind=q['kind'],number=q['number'],points=q['marking_points'])for q in paper['questions']]),ensure_ascii=False,indent=2)+'\n')
 (out/'audit.json').write_text(json.dumps(paper['audit'],ensure_ascii=False,indent=2)+'\n')
print('Exported five original papers, answer keys, solutions, marking schemes and audits')
