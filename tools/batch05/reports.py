"""Report only the actual additive notes; historical reports remain historical."""
from pathlib import Path
import csv,json,subprocess
R=Path(__file__).resolve().parents[2];out=R/'reports/batch05';out.mkdir(exist_ok=True)
rows=json.loads((R/'data/review/batch05_sections.json').read_text())
summary=[];sources=[];audits=[];totals={'chapters':0,'sections':0,'examples':0,'practice':0,'quiz':0}
for evidence in sorted((R/'data/batch05').glob('*-sections.json')):
 stem=evidence.name.split('-')[0];base=json.loads((R/f'data/base-lessons/{stem}.json').read_text());notes=json.loads((R/f'data/notes/{stem}.json').read_text());n=len(notes);totals['chapters']+=1;totals['sections']+=n
 summary.append('- '+{'bio':'生物','phys':'物理','chem':'化学','math':'数学'}[stem[:-2]]+' '+str(int(stem[-2:]))+'：'+'；'.join(s['id']+' '+s['t'] for s in base['sections'])+'。')
 for section in base['sections']:
  u=notes[section['id']]
  for k in ['examples','practice']:totals[k]+=len(u[k])
  totals['quiz']+=1
  texts=section['body']+u['deep'];size=sum(len(t) for t in texts)
  audits.append(dict(subject=u['subject'],chapter=u['chapter_id'],section=section['id'],title=section['t'],teaching_characters=size,teaching_paragraphs=len(texts),derivation_items=len(u['derive']),examples=len(u['examples']),practice=len(u['practice']),diagnostic_goals=len(u['diagnostics']),twelve_module_fields=True,status='authored_pending_teacher_review',limitations='字段齐备不等于教师审定；图示缺口及2027考试适用性仍需核实'))
  for s in u['content_sources']:sources.append(dict(subject=u['subject'],section=section['id'],**s))
(out/'CONTENT_DEPTH.json').write_text(json.dumps(audits,ensure_ascii=False,indent=2)+'\n')
(out/'COUNTS.json').write_text(json.dumps(totals,ensure_ascii=False,indent=2)+'\n')
with (out/'MODULE_COVERAGE.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(audits[0]),lineterminator="\n");w.writeheader();w.writerows(audits)
(out/'CONTENT_DELIVERY.md').write_text('# 本轮新增正文（持续批量编写）\n\n'+'\n'.join(summary)+f"\n\n实际新增 {totals['chapters']} 章、{totals['sections']} 个目录小节；{totals['examples']} 道原创例题、{totals['practice']} 道原创分层练习、{totals['quiz']} 道额外检测题。M12复用的目标题不重复计数。\n\n十二模块字段与浏览器呈现已检查的范围见测试报告；科学内容仍属部分核实、待教师审定。不能以字段数、字数或自动测试通过冒充教学质量全面验收。本文件记录已写正文，不把目录已存在或仅有笔记待写卡片计为完成。\n\n## 尚未完成\n\n至少20个原章、每科至少5章的批量目标仍在推进；高数章级归属已经按用户确认落实，小节资料证据不足的部分不能伪造编号。其余章节沿用原框架与现有笔记，不宣布完成。\n")
sourcehead='''# 来源与准确性边界

- 原课程116章来自仓库现有课程数据，编号、名称、顺序不变。本轮没有重新扫描Git历史，也没有声称找回Claude会话照片。
- 生物新增节按董总公开《高中生物》内容表对照章名和节名；它是课程/教材内容对照资料，不能作为2027考试评量规格使用。与用户实际印本逐页核对尚待进行。
- 物理新增节采用2017版《物理》上册公开预览的目录事实，对照原章名；来源为第三方预览，并非官方考试原卷。只提取目录事实；讲解、例题与练习均为原创。
- 化学新增节名按董总《高中化学》内容表与原章框架对应；新有机笔记仍需对实体印本逐页复核。
- 原理参考列在各节；与学校2027校内安排、董总2026公开评量文件分别呈现。2027适用性仍待确认。
- 高数I第1–29章、II第1–35章由用户在本会话明确确认。两范围重叠表示共用内容，不能强制把一章排他地归某一科；进度不复制。
- 数学前五章采用2025年10月第1版《数学》高一上册公开目录，并经用户明确确认所示小节与其课本一致；不是把考试纲要条目充作教材小节。具体目录页定位随节登记。
- 用户表格链接（gid 1832568942）在2026-11-18读取时，Google Sheets连接返回403，公开导出返回401。未读取其中格子或链接，不把截图、链接存在或章级范围确认当作具体小节已核实。
- 数值核验与定性科学审阅分别记录；测试不构成官方、学校或教师背书。所有新题标明原创，无虚构考频、官方步骤分或卷别。

## 逐节来源

'''
lines=[]
for s in sources:lines.append(f"- {s['subject']} {s['section']}：[{s['source_id']}]({s['url']})；定位 {s.get('page',s.get('page_or_section'))}；{s['version']}；{s['verification_status']}。")
(out/'SOURCES.md').write_text(sourcehead+'\n'.join(lines)+'\n')
with (out/'SOURCES.csv').open('w') as f:
 fields=['subject','section','source_id','url','page','page_or_section','version','access_date','verification_status'];w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n");w.writeheader();w.writerows(sources)
print(totals)
