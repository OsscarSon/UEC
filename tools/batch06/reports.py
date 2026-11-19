"""Living progress register; this batch is not complete until the requested targets pass."""
from pathlib import Path
import json,csv,collections
R=Path(__file__).resolve().parents[2];out=R/'reports/batch06';out.mkdir(exist_ok=True)
names={'bio':'生物','chem':'化学','phys':'物理','math':'数学共用内容'}
chapters=[];sources=[];sections=[];counts=collections.Counter()
for ev in sorted((R/'data/batch06').glob('*-sections.json')):
 stem=ev.name.split('-')[0];b=json.loads((R/f'data/base-lessons/{stem}.json').read_text());units=json.loads((R/f'data/notes/{stem}.json').read_text());rows=json.loads(ev.read_text());p=stem[:-2]
 counts[p]+=1;chapters.append(dict(stem=stem,subject=names[p],chapter=rows[0]['chapter_id'],sections=[dict(id=s['id'],title=s['t']) for s in b['sections']],status='authored_internal_checks_in_progress_not_teacher_approved'))
 for s in b['sections']:
  u=units[s['id']];sections.append(dict(subject=u['subject'],chapter=u['chapter_id'],section=s['id'],title=s['t'],modules=12,explanation_chars=sum(map(len,s['body']+u['deep'])),examples=len(u['examples']),practice=len(u['practice']),quiz=1,verification_status=u['verification_status']))
  sources += [dict(subject=u['subject'],chapter=u['chapter_id'],section=s['id'],**src) for src in u['content_sources']]
stats=dict(target_unique_chapters=40,minimum_new_chapters_each_course=8,new_unique_chapters=len(chapters),new_real_sections=len(sections),new_examples=sum(s['examples'] for s in sections),new_practice=sum(s['practice'] for s in sections),new_quiz=len(sections),new_original_questions=sum(s['examples']+s['practice']+s['quiz'] for s in sections),course_counts=dict(physics=counts['phys'],chemistry=counts['chem'],biology=counts['bio'],adv_math_i=sum(c['stem'].startswith('math') and c['chapter']<=29 for c in chapters),adv_math_ii=counts['math']),math_shared_counted_once=True,request_complete=False)
(out/'PROGRESS.json').write_text(json.dumps(dict(status='in_progress',statistics=stats,chapters=chapters),ensure_ascii=False,indent=2)+'\n')
for filename,rows in [('SECTION_MODULE_COVERAGE.csv',sections),('SOURCES.csv',sources)]:
 with (out/filename).open('w') as f:
  fields=list(dict.fromkeys(k for row in rows for k in row));w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
lines=['# Batch06 连续编写检查点（不是40章已交付声明）','',f"当前写入{len(chapters)}个未重复原章、{len(sections)}个真实小节；原创例题{stats['new_examples']}、分层练习{stats['new_practice']}、独立检测题{stats['new_quiz']}。数学共用章在总数中只计一次。",'','| 科目 | 当前新增章 | 最低目标 |','| --- | ---: | ---: |']
for code,label in [('physics','物理'),('chemistry','化学'),('biology','生物'),('adv_math_i','高数I'),('adv_math_ii','高数II')]:lines.append(f"| {label} | {stats['course_counts'][code]} | 8 |")
lines+=['','本轮要求为40个不重复章、每科至少8章。当前尚未达到，不能把模块存在、来源台账或重复数学入口算成完成数。','','## 当前实际写入','']
for ch in chapters:lines.append('- '+ch['subject']+' 第'+str(ch['chapter'])+'章：'+'；'.join(s['id']+' '+s['title'] for s in ch['sections'])+'。')
lines+=['','## 复核与边界','','- 结构与独立算例：见CONTENT_CHECKS.json；浏览器实际渲染、路径与两科高数自评隔离：见BROWSER_RESULTS.json。自动检查是所列范围的证据，不是教师或官方全面审定。','- 现有116章ID、名称、顺序与旧笔记保留；没有重新扫描Git历史，没有删除或复制学习进度，没有合并或部署。','- 化学、生物新小节按董总公开教材内容对照表核对；这是教材/课程内容资料，不是考试评量文件。新增物理按同系列2017教材中册公开目录事实，数学6按用户已确认系列的2025《数学》高一上册目录，28–31按公开2025《高级数学》高三上册目录。并未声称找回Claude原照片或逐页核对用户实体书。','- 题目与讲解原创；考试方法为教学策略，不冒充真题、官方分值、考频或2027适用确认。学校安排、统考要求继续使用原来分开的资料入口。','- 尚未核实的小节不得以常识编号补造：数学7–27、32–35的完整同版目录仍需可访问资料；新取得2025年9月第1版高三上册28–31目录已单独登记，可据此推进。用户资料表2026-11-19公开导出401、Google Sheets连接403；公开新版数学下册预览地址404，未读取其格子或虚称已核实。已知章级范围I1–29、II1–35继续保留，不强制排他归科。','- 当前数学6同时供I/II读取，记录继续独立；“两个入口”不作为两个新增不重复章。','- 图示需求另列illustrations/batch06/PROMPTS.json；缺图不删教学内容，也不将未制作图冒称已通过科学审核。','','## 下一步','','继续编写已取得可靠目录的未编章节，逐章做内容和独立计算复核；补充真实目录证据后再推进受阻数学范围。当前文件是连续任务恢复用检查点，不是缩减40章目标的新约定。','']
(out/'PROGRESS.md').write_text('\n'.join(lines))
print(json.dumps(stats,ensure_ascii=False))

