"""Explicit author estimates after reading the source pages, not OCR inference.
B/M/H describe the demand of a question, not student success probabilities.
No default grade is assigned to historical units absent from these lists.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams'
p=D/'visual-difficulty-review.json';grades=json.loads(p.read_text())
level={'B':'basic','M':'medium','H':'hard'}
mcq={
 ('uec_math_i',2019):'B B M M M B M M M H B M M B M B M B B B',
 ('uec_math_i',2020):'B B B B M M M M B M M M M M B B B B M H',
 ('uec_math_i',2021):'M M M B M M B M B M M B M M B B M B M B',
 ('uec_math_i',2022):'B M B B B M B M B M M M M M B B M B B M',
 ('uec_math_i',2023):'B M M M B M M M B M M M M B B M B M B M',
 ('uec_math_i',2024):'B B M M B M M M B M M M B B M M B B B B',
 ('uec_math_ii',2018):'B B M M M M M B B M M B M B M B M M B B',
 ('uec_math_ii',2019):'M B M B B B M M B M B M M B M B B B B M',
 ('uec_math_ii',2020):'M B B B M M M H M M M B M M M B B B M M',
 ('uec_math_ii',2021):'B M B M B M M B M M M M M M M H M M M B',
 ('uec_math_ii',2022):'B M B B M M B M M M M M M M M B M M M M',
 ('uec_math_ii',2023):'M M M M M M M M M M M M M M H B M H M M',
 ('uec_math_i',2025):'B M M B M M B B B M B M M B B M B M B B',
 ('uec_math_ii',2024):'B M M B M B M M B M M B M M M M B M M M',
 ('uec_math_ii',2025):'B B M M B B M M M M M B M M B B M B H B',
 ('semester_final',2025):'B M M H B B M M M B B B M B B M M M H M',
 ('semester_final',2024):'M M B M M M B M M M M B M M B M M H M M',
 ('semester_final',2023):'M M B B M M B M B M M M M M B M M B B B',
 ('semester_final',2022):'B B M B M M M M B B B B M B M M M M M M',
}
added={}
for (code,year),values in mcq.items():
 values=values.split();assert len(values)==20
 for n,l in enumerate(values,1):added[f'{code}:{year}:mcq:{n}:whole']=level[l]
written={
 2025:{'1:a':'B','1:b':'M','1:c':'M','2:a':'M','2:b':'M','2:c':'M','3:a':'M','3:b':'B','3:c':'B','4:a':'H','4:b':'M','5:a':'B','5:b':'M','5:c':'M','6:a':'M','6:b':'M','7:a':'B','7:b':'M','7:c':'H'},
 2024:{'1:whole':'M','2:whole':'M','3:a':'B','3:b':'M','4:whole':'M','5:a':'M','5:b':'B','6:a':'H','6:b':'H','7:a':'M','7:b':'H','7:c':'M','8:a':'M','8:b':'B','8:c':'M'},
 2023:{'1:a':'M','1:b(i)':'M','1:b(ii)':'H','2:a':'M','2:b':'M','3:a':'B','3:b(i)':'M','3:b(ii)':'B','4:a':'M','4:b':'M','5:a':'M','5:b':'H','6:a':'M','6:b':'M','6:c':'B','6:d':'M','7:a':'B','7:b':'M','7:c':'M'},
 2022:{'1:a':'M','1:b':'H','1:c':'H','2:a':'M','2:b':'M','2:c':'B','3:a':'H','3:b':'H','3:c':'M','4:a':'H','4:b':'M','5:a':'M','5:b':'M','5:c':'H','6:a(I)':'B','6:a(II)':'M','6:a(III)':'M','6:b':'H'},
}
for year,items in written.items():
 for key,l in items.items():added[f'semester_final:{year}:written:{key}']=level[l]
ids={r['id'] for f in (R/'reports/math-audit').glob('visual-review-*.json')for r in json.loads(f.read_text(encoding='utf-8'))}
assert set(added)<=ids
grades.update(added);p.write_text(json.dumps(grades,ensure_ascii=False,indent=2)+'\n')
(R/'reports/math-exams/RECENT_DIFFICULTY_METHOD.md').write_text('''# 本轮题面难度估计

明确阅读所供2018–2025统考选择（高数I自2019）及2022–2025校内期末题面后，按题逐项记录作者估计。basic指直接应用或单一条件转换；medium指多步代数、主值/端点筛选、标准综合方法；hard指较长证明、隐含条件、非常规建模或多重方法结合。

评级代码和逐题列表在tools/math-exams/recent_difficulty.py；未列条目保持未估计。题号、知识点、完整定义域和公式仍须读research-ledger.json，不能只由章节名称推测难度。分值不自动等于难度，原件红色答案不充当评级依据。

这是作者的定性教学判断，未使用考生正确率、耗时分布或区分度。学校蓝图中的难度是学校另一个来源层级，未冒充统考官方难度。本轮新增估计不能认证全历史难度分布。
''')
print('Recorded',len(added),'explicit difficulty estimates; other unknown units remain unknown')
