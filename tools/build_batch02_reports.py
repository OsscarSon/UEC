"""Report actual delivery, source limitations and unfinished work; never infer acceptance from fields."""
from pathlib import Path
from collections import Counter
import csv,json,subprocess,hashlib
R=Path(__file__).resolve().parents[1];OUT=R/'reports/batch02';OUT.mkdir(exist_ok=True)
js="const fs=require('fs'),vm=require('vm'),c={};c.window=c;vm.createContext(c);for(const f of fs.readdirSync('lessons').filter(x=>/^(phys|chem|bio)\\d+\\.js$/.test(x)))vm.runInContext(fs.readFileSync('lessons/'+f,'utf8'),c);vm.runInContext(fs.readFileSync('lessons/batch-notes.js','utf8'),c);process.stdout.write(JSON.stringify({lessons:c.LESSONS,batch:c.BATCH_NOTES}))"
s=json.loads(subprocess.check_output(['node','-e',js],cwd=R));curr=json.loads((R/'data/curriculum.json').read_text());master=json.loads((R/'illustrations/ILLUSTRATION_MASTER_MANIFEST.json').read_text())
rows=[];section_rows=[];module_names=['学习目标','前置知识','知识结构图','深度知识讲解','图解、公式、推导与实验','典型例题','UEC题型与考试攻略','易错易混','分层练习','完整解析','考前速记','掌握度检测与反馈']
for d in curr:
 key=d['subject']+str(d['chapter']);units=s['batch'].get(key,{});secs=s['lessons'].get(key,{}).get('sections',[])
 before='B' if key in ['物理3','物理4','化学3','化学4','化学5','生物1','生物2','生物3'] else 'D' if d['subject']=='数学' else 'C'
 after='B' if secs else 'D' if d['subject']=='数学' else 'C'
 if after=='B':reason='12模块实现且完成本轮改善；仍有部分结构/实验图、知识点全面教研及适用版本核对未最终验收，不用结构齐备宣称全部标准通过。'
 elif after=='D':reason='已找到2026修订高级数学课程标准的35章内容表；标准编号不直接当教材小节。仍缺学校真实目录与I/II逐项对应，S06正文/附注存在指向冲突，暂不迁移。'
 elif d['subject']=='物理':reason='本轮未取得可完整逐项复核的同版本物理小节表；公开课程页访问失败，保留原章，不造编号。'
 elif d['subject']=='化学' and d['chapter'] in [7,8]:reason='已取得董总公开内容表第3页候选小节；尚未写成全章笔记与完成逐项科学/图示审定。这是未完成工作，不是声称没有来源。'
 else:reason='找到化学/生物公开课程内容表候选，但未完成本章小节转录、版本对应、原创教学和逐项验证；不把检索到目录当完成。'
 rows.append(dict(subject=d['subject'],chapter_id=d['chapter'],chapter_title=d['title'],original_order=len(rows),category_before=before,category_after=after,actual_section_count=len(secs),actual_section_ids=';'.join(x['id'] for x in secs),modules_implemented=len(secs)*12 if units else 0,acceptance_status='not_claimed_fully_complete',reason=reason,source_status='partially_verified' if after=='B' else 'needs_review'))
 for sec in secs:
  u=units.get(sec['id']);section_rows.append(dict(subject=d['subject'],chapter_id=d['chapter'],chapter_title=d['title'],section_id=sec['id'],section_title=sec['t'],new_in_batch02=key=='化学6',depth_action='原41节深化' if before=='B' and key not in ['化学5','生物3'] else '原有11节新增十二模块' if key in ['化学5','生物3'] else '目录证据核对后新增小节及内容',module_count=12 if u else 0,example_count=len(u['examples']) if u else 0,practice_count=len(u['practice']) if u else 0,quiz_count=1 if u else 0,diagnostic_mapping_count=len(u['diagnostics']) if u else 0,status='implemented_pending_final_content_acceptance'))
def csvout(name,rs):
 with (OUT/name).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rs[0]),lineterminator='\n');w.writeheader();w.writerows(rs)
csvout('COURSE_COVERAGE_MASTER.csv',rows);csvout('COMPLETED_IMPLEMENTATION_SECTIONS.csv',section_rows)
# New evidence augments the migration ledger without changing any target assignment or old identity.
p=R/'reports/math_subject_mapping.csv'
with p.open() as f:reader=csv.DictReader(f);fields=reader.fieldnames;mapping=list(reader)
math_url='https://elearning.dongzong.my/pluginfile.php/73029/mod_resource/content/4/高级数学课程标准中文版%20Jan2026.pdf'
for item in mapping:
 if math_url not in item['evidence_link_or_page']:item['evidence_link_or_page']+='; '+math_url+' PDF12–20内容表'
 item['pending']='2026修订课程标准已取得部分内容表且35章主题可对照；仍无已核学校实际教材小节及I/II逐项归属。课程标准学习结果编号不冒充教材小节号；2027适用待确认，不迁移或复制进度。'
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(mapping)
# Sources consulted this round, with access failures distinguished from web-readable excerpts.
sources=[
 dict(id='new_kit',type='user_instruction_attachment',location='UEC_2027_Codex_Batch_Notes_Kit_v2 (1).zip',locator='8份Markdown＋2份模板；学校原件11页',status='read',scope='工作标准；与本轮用户请求冲突处以用户请求为准'),
 dict(id='school',type='school_original',location='ZIP/sources/HinHua_2027_subjects_scope_exam_arrangements.pdf',locator='p2–4；全11页原件已在前轮阅读，本轮SHA256同原件36591164fb6dc4dca3e8c440a6ffceee3e53b0557ebb6a8c21ee3250077f8fc0',status='verified_identity',scope='只用于兴华2027校内。摘要的物理第二学期与化学期末比例错误仍以原件核对记录为准'),
 dict(id='chem_directory',type='official_content_table',location='https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf',locator='p2化学6叶级编号；p3化学7/8候选',status='partially_verified',scope='公开跨学科内容表；文本网页可读，直接下载403；小节身份证据，不复制教材全文，不确认2027评分'),
 dict(id='bio_directory',type='official_content_table',location='https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf',locator='p1核对现有1–3章；p2等为后续候选，OCR“千细胞”等不直接当教材文字',status='partially_verified',scope='候选目录，不强制改已有生物3.1标题，不把学习条目层级混为独立课程'),
 dict(id='math_standard',type='official_curriculum_standard',location=math_url,locator='封面2023/2025.11/2026.1修订；PDF12–20内容表相关页',status='partially_verified',scope='获得真实标准主题和学习结果，不等于取得学校教材小节目录或完成I/II归科'),
 dict(id='math_textbook_preview',type='official_candidate_preview',location='https://elearning.dongzong.my/pluginfile.php/132764/mod_resource/content/1/《高级数学》高三上册.pdf',locator='搜索可见编辑说明；网页全文404，直接下载403',status='not_accessible_full',scope='不凭搜索摘要重建真实教材小节'),
 dict(id='physics_course',type='official_course_page',location='https://elearning.dongzong.my/course/view.php?id=214&lang=zh_cn',locator='课程页无法取得可用小节表',status='not_accessible',scope='未从非官方重传/受限资源猜目录'),
]
for code,file in [('physics','S12-2026-0623.pdf'),('chemistry','S11-2026-0623.pdf'),('biology','S10-2026-0623.pdf'),('math_i','S06-2026-0730.pdf'),('math_ii','S07-2026-0730.pdf')]:sources.append(dict(id='dz_'+code,type='official_uec',location='https://uec.dongzong.my/wp-content/uploads/2026/07/'+file,locator='已取得2026文件；化学1.3/1.4，生物2.3，数学p1',status='partially_verified',scope='当前取得2026框架；未声称锁定2027。I、II与各自卷一/卷二分别表示'))
seen=set()
for units in s['batch'].values():
 for u in units.values():
  for src in u['content_sources']:
   if src.get('url') and src['url'] not in seen:
    seen.add(src['url']);sources.append(dict(id=src['source_id'],type='science_or_curriculum_reference',location=src['url'],locator=src.get('page_or_section',str(src.get('page','相关条目'))),status='partially_verified',scope='相关科学原则核对，不代表所有段落独立教师审定或考试考频'))
csvout('SOURCE_ACCURACY_REGISTER.csv',sources)
counts=Counter(r['category_after'] for r in rows);chapters=[r for r in rows if r['actual_section_count']]
def table(headers,rr):return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(v).replace('|','&#124;') for v in row)+' |' for row in rr])
# M04/05/07 actual character counts are evidence only.
depth=[]
followup=json.loads((R/'data/review/content_followup.json').read_text())
followup_rows=[]
for row in section_rows:
 key=row['subject']+str(row['chapter_id']);u=s['batch'][key][row['section_id']];sec=next(x for x in s['lessons'][key]['sections'] if x['id']==row['section_id'])
 todo=followup[key+':'+row['section_id']]
 depth.append(dict(subject=row['subject'],chapter_id=row['chapter_id'],section_id=row['section_id'],section_title=row['section_title'],m04_original_plus_deep_chars=len(''.join(sec['body']+u['deep'])),m05_derive_chars=len(''.join(u['derive'])),m07_strategy_chars=sum(len(str(x)) for x in u['strategy'].values()),m06_examples_eight_stages=sum(all(q.get(f) for f in ['analysis','given','method','principle','verification','pitfall']) for q in u['examples']),goal_mappings=len(u['diagnostics']),specific_improvement=u['strategy']['method'],checking_evidence=u['strategy']['verification'],remaining=todo['required_expansion_or_verification']))
 related=[x['id'] for x in master['illustrations'] if x['subject']==row['subject'] and x['chapter_id']==row['chapter_id'] and x['section_id']==row['section_id'] and x.get('production_task_id')]
 followup_rows.append(dict(subject=row['subject'],chapter_id=row['chapter_id'],section_id=row['section_id'],section_title=row['section_title'],modules='/'.join(todo['modules']),specific_followup=todo['required_expansion_or_verification'],current_goal_question_refs=';'.join(str(g['goal_index']+1)+':'+g['question_ref'] for g in u['diagnostics']),related_illustration_tasks=';'.join(related),acceptance_status=todo['status']))
csvout('DEPTH_IMPROVEMENTS.csv',depth)
csvout('FOLLOWUP_CONTENT_REQUIREMENTS.csv',followup_rows)
(OUT/'DEPTH_IMPROVEMENTS.md').write_text('# 内容深度改进与未通过项\n\n基线：`daa3637`。本报告描述已写入的教学内容，不把结构或八步字段通过当作全面教研通过。\n\n原41节均追加逐节解释/推导，M07给题干线索、方法选择、原理、例题回链、验算及错法原因；M08加入针对性错解分析。原123例逐题补五项人工式注释，使所有174例均可呈现题意→已知→方法→原理→步骤→答案→验算→易错。八步字段仍需逐题审阅，不以字段存在自动判定深度。\n\n化学5、生物3原11节新增完整模块数据，化学6按官方目录新增6节；新增138条原创题（51例、68练习、17原检测、2个补充目标检测）。116条目标映射多数复用现有题，复用展示不算新题。M12映射仍是目标抽样，不能保证一题覆盖目标的每个子技能。已修正6.3.3逐级电离等错配回链；[58节后续扩写/验收范围](FOLLOWUP_CONTENT_REQUIREMENTS.csv)逐节指出尚未被检测覆盖的子技能和具体图示需求，不统一用“待核”代替问题定位。\n\n四处公式已修：物理3.3的|Δx|和Σ|Δx_i|、4.2的|f_s|、4.3的|F₁−F₂|、4.8的|a_A|/|a_B|。另修复物理3.2、4.6及生物1.6三道原例题的跨例指代，补全6道原练习和新氢谱例的独立条件，补写物理4.5进阶例的同合力跨地点比较。\n\n化学6追加分类史、周期定位、分区例外及性质定义的分层解释；纠正最高占据n被无条件当周期的捷径。原生物3、化学5的已知错误已改正文，不在错误正文旁仅追加警告：ATP整体水解、卡尔文统一计数、发酵ATP、温度/抑制模型、质谱m/z、4s/3d条件等。30幅待修旧SVG原文件全部保留，但不进入当前十二模块视图；11幅新增确定性SVG多为关系/账本总结，不能冒充完整结构替代。\n\n'+table(['科目/小节','M04合并字符','M07字符','八步例数','目标映射','本节方法与核查'],[(r['subject']+r['section_id'],r['m04_original_plus_deep_chars'],r['m07_strategy_chars'],r['m06_examples_eight_stages'],r['goal_mappings'],r['specific_improvement']+'；'+r['checking_evidence']) for r in depth])+'\n\n字符只用于定位，不是及格线；M04计原正文+补充，M05另有原图/公式/术语。详细CSV见同目录。全部58节保持partially_verified，仍待全面知识点及独立教研审定。\n')
report=['# 本轮集中交付：笔记深化、插图接入与全部后续提示词','',
'继续PR #1原分支 `codex/uec-2027-batch-notes-math-split`，不新建PR、不合并、不部署。基线为daa3637。','',
'## 实际完成的实施范围','',
'9个章级记录、58个真实小节已有本轮十二模块内容，共696模块；保留原116章与原52小节ID/名称/顺序，新增化学6的6个有官方目录证据的小节。原41节深化，原11节补齐模块，另6节首次建立。这里是实施范围，不是宣布整章全部标准最终验收通过。','',
table(['科目','原章号与章名','真实小节数'],[(r['subject'],str(r['chapter_id'])+' '+r['chapter_title'],r['actual_section_count']) for r in chapters]),'',
'58节完整标题与逐节动作见 [COMPLETED_IMPLEMENTATION_SECTIONS.csv](COMPLETED_IMPLEMENTATION_SECTIONS.csv)。原始52节与新增6节分别核对，未用新编号掩盖重排。','',
'## 全课程覆盖与未完成','',
'完整116章A/B/C/D表见 [COURSE_COVERAGE_MASTER.csv](COURSE_COVERAGE_MASTER.csv)。A=全部要求最终验收；B=有真实小节但仍有待补/待验收；C=仅章目录或候选目录需落实；D=归属/教材/适用证据不足。当前保守记A0、B9、C72、D35。没有将696个结构模块等同于A。','',
'物理其余25章未取得可完整核对的同版本小节表；化学其余31章与生物其余16章尚未逐章完成目录对应、原创笔记及科学验收。化学7/8已有公开内容表候选，不能说无来源，但尚未实际编写。数学35章虽有新版标准内容表，仍未得到学校真实教材目录与I/II归属，不迁移或复制进度。','',
'## 内容与题目','',
'[深度改进报告](DEPTH_IMPROVEMENTS.md)列58节方法、核查及待验收点；[逐节后续扩写要求](FOLLOWUP_CONTENT_REQUIREMENTS.csv)明确检测覆盖缺口及需要继续深化的内容。174例均有八步字段，原123例为逐题扩写。十二模块补充层共466条原创题记录（保留的原章级及ext题另计）：174例题、232分层练习、58节检测、2个额外目标检测；相对基线新增138，不将116个目标回链或M07复用例题重复计数。','',
'[696项模块覆盖](SECTION_MODULE_COVERAGE.csv)核实模块存在。原样例的80项数值/原子守恒检查及本轮新增样例检查有明确范围；定性机制不因数值通过自动成为verified。','',
'## 上传图与后续图任务','',
'六张上传PNG逐张检查，3张限定用途接入：物理3.5、化学4.2.3、生物2.3概览。3张隔离：物理4.3向量几何、化学3.6运算箭头/温压/NA、生物2.2主动运输及梯度概括。原文件均保留；原73幅SVG逐字节不变。','',
'[逐张审核JSON](../../illustrations/IMPORT_BATCH01_REVIEW.json)；[完整主清单](../../illustrations/ILLUSTRATION_MASTER_MANIFEST.json)为209项教学记录：60保留、35数学冻结、114制作任务。另列6张导入图、6界面素材和11幅新确定性总结SVG，不混计。','',
'[全部中文/英文Prompt](../../illustrations/PROMPTS_BATCH_ALL.md)／[机器JSON](../../illustrations/PROMPTS_BATCH_ALL.json)按科目及完整章分组；114条中24条为HTML/CSS关系图重构、90条为其他图制作。每条含20项要求、独立中英文Prompt、Negative、来源、验收、复用、优先级及确定性绘图要求。未调用AI生图。','',
'[图像质量检查表](../../illustrations/IMAGE_QUALITY_CHECKLIST.md)区分定量图、结构、装置、函数与辅助画；AI图仍需科学重建/审查，不能因清单齐备就上线。','',
'## 数学与资料准确性','',
'两个数学入口与独立记录保留；仍各0个已归属章节、0题本科题库、0本科模拟卷。旧35章维持math_pending。2026修订标准包含与旧35章相符的主题，但学习结果编号不能直接冒充课本小节；S06正文《高中数学》与末注《高级数学课程标准》的指向冲突仍未解决。','',
'[来源与准确性台账](SOURCE_ACCURACY_REGISTER.csv)分别记录学校、UEC、公开目录、科学原则、403/404与部分可读状态。学校原件与前轮SHA256相同，仍按原件纠正ZIP摘要；两份早先另传Research报告的历史核验见原报告，不声称新ZIP包含它们，也未重做全部64题统计。','',
'## 测试与限制','',
'运行 `python tools/build_notes.py`、`node tests/coverage.cjs`、`python tests/calculations.py`、`python tests/batch02_audit.py --rebuild-check`，本地服务下运行 `node tests/browser.cjs` 与 `node tests/batch02_browser.cjs`。可用UEC_TEST_BASE指定本地端口。','',
'[当前手机策略截图](screenshots/strategy-390.png)／[电脑策略截图](screenshots/strategy-1280.png)／[手机放大图](screenshots/zoom-mobile.png)来自本地验证，不是部署。放大图可在容器内横向滑动，不撑开页面。','',
'[实际测试命令](TEST_COMMANDS.md)、[构建与兼容命令可复现](BUILD_REPRODUCIBILITY.json)、[静态/计算/资源/Prompt结果](AUDIT_RESULTS.json)、[专项UI与SVG边界](UI_RESULTS.json)、[全站回归](../BROWSER_RESULTS.json)提供实际结果。数学I/II记录与错题隔离、原进度、日历、题库、旧链接、导出导入往返，以及3视窗×9章、目标反馈、放大与键盘都需通过；测试通过仍不等于教师/官方全面审定。','',
'剩余：未实施107个章级记录（72科学C、35数学D）；58节的最终知识点/图示/教研验收；114条图制作/修正任务；2027适用及学校真实教材版本；完整官方原卷、评分及考频证据。新内容未以“全科完成”交付。','']
(OUT/'DELIVERY.md').write_text('\n'.join(report))
print('Reported116 chapters /58 sections; categories',dict(counts))
