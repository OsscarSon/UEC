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

# Current coverage overlays; these do not rewrite historical audits.
current=json.loads((R/'data/curriculum.json').read_text());newkeys={(r['subject'],r['chapter_id']) for r in rows}
allbase={}
script="const fs=require('fs'),vm=require('vm'),c={};c.window=c;vm.createContext(c);for(const f of fs.readdirSync('lessons').filter(f=>/^(phys|chem|bio|math)[0-9]+[.]js$/.test(f)))vm.runInContext(fs.readFileSync('lessons/'+f,'utf8'),c);process.stdout.write(JSON.stringify(c.LESSONS))"
live=json.loads(subprocess.check_output(['node','-e',script],cwd=R))
import re
for key,base in live.items():
 match=re.fullmatch(r'(物理|化学|生物|数学)(\d+)',key)
 if match:allbase[(match[1],int(match[2]))]=base
course_counts={}
for subject,prefix in [('物理','phys'),('化学','chem'),('生物','bio'),('高级数学（I）','math'),('高级数学（II）','math')]:
 selected=[(k,v) for k,v in allbase.items() if k in newkeys and k[0]=={'phys':'物理','chem':'化学','bio':'生物','math':'数学'}[prefix]]
 course_counts[subject]={'new_chapters':len(selected),'new_sections':sum(len(v['sections']) for k,v in selected)}
totals.update(module_instances=totals['sections']*12,original_questions_total=totals['examples']+totals['practice']+totals['quiz'],course_entries=sum(x['new_chapters'] for x in course_counts.values()),per_course=course_counts,total_unique_note_chapters=len(allbase),total_saved_sections=sum(len(v['sections']) for v in allbase.values()))
(out/'COUNTS.json').write_text(json.dumps(totals,ensure_ascii=False,indent=2)+'\n')
coverage=[]
for c in current:
 key=c['subject'],c['chapter'];note=allbase.get(key)
 if key in newkeys:status='A';reason='本轮完整十二模块正文已写；来源部分核实，待教师审定；不等同所有图片或2027范围验收。'
 elif note:status='B';reason='前批笔记保留；本轮做功能回归，未冒称已重新全面审定旧内容深度。'
 elif c['subject']=='化学' and 12<=c['chapter']<=16:status='B';reason='前批已记录同版公开目录依据；本轮未写正文，属于待继续制作，不是资料不存在。'
 else:status='C';reason='原章框架保留，本轮未逐节编写/对照；公开内容表或下一册目录可继续核对，不断言原Claude照片不存在。'
 need='继续逐节写作并审内容/图示/适用性'
 if c['subject']=='数学' and c['chapter']>=7:need='取得或核对对应册同版实际小节目录；I/II章级归属已由用户确认，不再用归科未定阻挡。'
 coverage.append(dict(subject=c['subject'],chapter=c['chapter'],title=c['title'],category=status,notes_present=bool(note),saved_sections=len(note['sections']) if note else 0,reason=reason,next_step=need))
with (out/'COURSE_COVERAGE.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(coverage[0]),lineterminator='\n');w.writeheader();w.writerows(coverage)
mapping=[]
for c in current:
 if c['subject']!='数学':continue
 codes=['adv_math_i','adv_math_ii'] if c['chapter']<=29 else ['adv_math_ii']
 mapping.append(dict(legacy_id='数学'+str(c['chapter']),chapter=c['chapter'],title=c['title'],courses=codes,content_key='数学'+str(c['chapter']),progress_keys=['mathSubjects.'+code+'.chapters.'+str(c['chapter']) for code in codes],legacy_progress='learn/rv/mast原键完整保留；未自动复制或删除',basis='用户2026-11-18明确确认I1–29、II1–35；2027官方范围另核',real_subsections='2025版高一上前五章用户确认' if c['chapter']<=5 else '本批未建立小节'))
(out/'MATH_COURSE_MAPPING.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
with (out/'MATH_COURSE_MAPPING.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(mapping[0]),lineterminator='\n');w.writeheader();w.writerows({**x,'courses':' / '.join(x['courses']),'progress_keys':' / '.join(x['progress_keys'])} for x in mapping)
chapters='\n'.join(f"- {name}：新增{v['new_chapters']}章、{v['new_sections']}节。" for name,v in course_counts.items())
(out/'CONTENT_DELIVERY.md').write_text(f"""# 本轮批量正文交付

实际新增{totals['chapters']}个原章、{totals['sections']}个独立目录小节、{totals['module_instances']}个模块。高数前五章在两科共享正文，计一次原章；按入口计{totals['course_entries']}个科目章条目，不虚报为不同原章。

{chapters}

原创题目：{totals['examples']}道例题、{totals['practice']}道分层练习、{totals['quiz']}道额外检测，合计{totals['original_questions_total']}道。M12引用例题/练习的目标题不重复计数。例题与练习均含题意、已知、选法、原理、步骤、答案、复核和易错分析，非官方真题或评分表。

## 新增章节清单

"""+'\n'.join(summary)+f"""

## 内容深度与验证边界

每节有5段以上实质讲解、推导/条件、3例题、4练习、检测及目标反馈；M07以题干线索、方法选择、原理和实际例题推理组织。字数、字段与DOM模块数只是完整性筛查，不是自动教学质量证书。图未齐部分仍有文字与推导及完整绘图任务，不以缺图删知识。科学和数学的独立计算范围见AUDIT_RESULTS.json，来源按节登记，不声称全部题目已获独立教师复核。

实际写作后累计保存{totals['total_unique_note_chapters']}个原章、{totals['total_saved_sections']}节。原116章身份、前批笔记、图片、题目和进度均保留；没有重扫Git历史或假称照片不存在。

## 尚未完成与原因

其余{len(current)-totals['total_unique_note_chapters']}个原章尚未写成本批完整笔记，逐章见COURSE_COVERAGE.csv。化学12–16等已有可继续使用的公开目录依据，未写属于制作待办，不能标成“无来源”。其他章应继续核对相应册实际小节及版本；未编写不等于原课本没有小节。前批内容深度整改、完整插图制作、2027官方适用性与教师全面审定仍未完工。

高数I1–29、II1–35归属已经按用户确认落实；6–35中未写的章保留原号与兼容资料，没有新增推测小节。前五章教材目录得到用户确认；私有Google表格仍未读到，未把权限失败当照片不存在。

## 插图与测试

新增94项独立中英文复合图任务见illustrations/batch05/PROMPTS.md及JSON（若以后扩写，由构建统计更新）。复用8幅已审核V22图，未生成新图；原142任务及95项无V22对应的历史缺口不因新需求而宣布完成。具体图审及测试见本目录相应JSON与TEST_RESULTS.md。

全部改动在Draft PR #3持续集中交付；不合并、不部署。
""".replace('新增94项',f"新增{totals['sections']}项"))
(out/'REMAINING_WORK.md').write_text('# 未完成范围与证据需求\n\n不把缺笔记等同缺原教材目录。以下只列本批未写章；已有公开目录也仍可继续制作。\n\n'+'\n'.join(f"- {x['subject']} {x['chapter']}《{x['title']}》：{x['reason']} 下一步：{x['next_step']}。" for x in coverage if not x['notes_present'])+'\n\n生物10.1.1在公开内容表中作为“种群成长模式”细项。本批在10.1《种群》覆盖，不把细项额外假称新独立教材小节。化学1.4、2.1/2.2、35.4/35.5是目录分组，叶级笔记依来源保留，不把父组重复计成已完成小节。\n')
(out/'DEPTH_REVIEW.md').write_text('# 实际内容深度审阅\n\n新增各节从概念、条件到推导/实验解释，再到基础—标准—迁移例题及练习；原子数、方向、定义域、参数退化、端基与单位是本轮具体检查点。\n\n- 物理：同时检查力与力矩，静摩擦上限，动能/动量守恒的不同条件，反弹符号、相对速度和缓冲平均力；不以短时无条件消灭外力。\n- 化学：分子间作用与化学键不混，摩尔体积注明温压，炔烃加成/水合按条件，聚合重复结构保侧基，缩聚有限链2n−1脱水与高n近似分开。\n- 生物：染色体与DNA计数、原核与病毒结构、能流与物质循环、遗传漂变/选择及平衡模型的条件分别说明。\n- 数学：绝对值、偶根与分母域、平方增根、参数降次、函数陪域和值域、反函数分支和几何例外均有题目检验。\n\n已修正编写中发现的数学回代值、缺等号缩写和来源路径；M12选题按具体目标调整，不机械地总引用同一序号。内容均仍为部分核实、待教师审定；不能把自动字数门槛当深度通过。后续重点包括精确插图、更多跨章综合与真实题型页码索引；未编造频率或官方步骤分。\n')
