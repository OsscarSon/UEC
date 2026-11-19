"""Build a factual delivery index; never infer teacher approval from module or test counts."""
from pathlib import Path
import json,csv,collections
R=Path(__file__).resolve().parents[2];out=R/'reports/batch06'
progress=json.loads((out/'PROGRESS.json').read_text());st=progress['statistics']
profiles={
'bio04':'增殖与分化、组织器官层级、修复功能证据、克隆核与细胞质来源、差异表达、特化细胞物种范围、干细胞潜能边界。',
'bio05':'消化与吸收分开；胆汁非脂肪酶、来源与储存不同；微绒毛与绒毛层级；长链脂质淋巴路线；ATP净值不重复；尿素肝合成肾排出；甘油与偶数脂肪酸碳去向。',
'bio06':'表面积体积比及扩散时间；动静脉按流向；瓣膜压差和心输出；自律与神经调节；ECG非泵血保证；木质/韧皮结构与源库；水势、蒸腾和压力流。',
'bio08':'内外环境范围、负反馈按原偏差、ADH下丘脑合成及垂体后叶释放、蒸发散热、胰岛αβ分工、肾血液与滤液通路、排泄收支与回收上限。',
'bio14':'转化及示踪的对照/结论边界、DNA反平行与碱基/氢键计数、半保留标记分布、转录模板方向/翻译读取、突变类型及阅读框条件。',
'bio15':'显隐性与基因型分开、条件概率、独立分配条件及连锁限制、X连锁子女性别分母、单基因/染色体/多因素模型区分。',
'bio16':'线性环状DNA酶切、连接与复制不同、筛选不等表达/功能验证、宿主和内含子、PCR净增与总量及对照、科学风险与价值选择分层。',
'bio17':'丰富度与均匀度、分类层级和系统树读法、采样努力与因果边界、破碎化和连通、就地迁地及保育效果的对照证据。',
'chem15':'X₂与X⁻、反应方向与配平、MnO₂制氯氯原子分流、浓盐水与熔盐电解、HCl气体与水溶液、银卤化物例外及配位、含氧酸价数和不同歧化条件。',
'chem19':'体系与环境热号、恒压焓条件、整式热化学基准和物态、元素标准参考态非绝对能量零、燃烧水相、弱酸中和、Hess线性及断键吸热。',
'chem20':'平均/瞬时与归一反应速率、表面积保持体积、实验级数非系数、惰气恒容条件、绝对温度和能垒分开、催化不改起末焓。',
'chem21':'动态平衡非反应停止、各浓度非必相等、K倍式与反向、ICE合法根、浓度瞬变与后续位移、惰气恒容/恒压、温度改K及催化不改K、工业竞争条件。',
'chem22':'存在离子与可动离子、Ksp计量幂、自由离子与总溶解量、共同离子和络合、混合总体积、选择沉淀阈值、转化K与实际Q及物料上限。',
'chem24':'阳极恒氧化阴极恒还原、原电池与电解极性、电子/离子通路、标准还原电势不随倍式倍增、容量与能量、水相竞争、电镀精炼、Faraday效率、腐蚀环境和牺牲阳极。',
'chem28':'开链单烯通式边界、逐碳四价、连结与几何异构计数、母链和双键号、物性趋势条件、燃烧干气余量、加成区域选择与介质、氧化断裂全碳账、聚合重复单元及产率。',
'chem32':'醇与酚连接对象、元数与级数、氢键非共价第三键、混合体积、醇氧化/酯化条件、制备骨架和OH位置、发酵与回收、酚酸碱/取代、异丙苯联产物料。',
'phys09':'轴和垂距、角量弧度、惯量和轴型、质心动能分解、无滑动约束及摩擦上限、力矩力臂、角动量参考点及守恒不等动能守恒。',
'phys10':'周期次数、恢复力与平衡、简谐初值和相位、空间/时间图、能量参考、阻尼受迫稳态及精确位移峰ωr²=k/m−b²/(2m²)的条件。',
'phys12':'布朗观察对象、分子估算与空隙、物态和振动、应力应变单位及线性条件、双表面液膜因子2、接触角与毛细升降。',
'phys13':'温度与热能不同、绝对温度及温差、校准偏移、热容与量热平衡、分阶段潜热、孔洞膨胀与受限机械条件、液体和容器体胀分开。',
'phys14':'传导非体流、稳态热阻和相同热流、自然/强制对流的条件、辐射净交换与总发射以及T⁴绝对温度。',
'phys15':'绝对与表压、K温标、nR与NkB、封闭/刚性不同、状态式非过程热、混合物料、三种过程约束及实验死体积。',
'phys17':'质点运动与波传播、声级对数、空间与振动图、行波方向和两种速度、边界所画变量、驻波开闭端、介质系多普勒及亚声速条件。',
'phys18':'法线角、镜后虚线与真实光路、球面镜整套符号及近轴、Snell和静界面频率、视深近法线/平行板、全反射两条件/外介质、折射率正弦图和系统误差。',
'phys19':'棱镜角/最小偏向条件、频率与光谱、单光子E=hf=hc/λ、薄透镜近轴符号、虚像反延及焦距测量/位移法条件。',
'phys20':'模型证据边界、干涉初相和等幅条件、缝距/缝宽、单缝零级、光栅级次、偏振逐片强度、场正交、光谱/光子总功率、往返测光和仪器延迟。',
'math06':'乘负反号、绝对值并交、重根不翻号、分母零点、半平面边界和可行域、线性目标顶点及整数约束。',
'math07':'假命题仍命题、开放式域量词、包容或与De Morgan、量词顺序、充分必要方向和反例、有效推理及经验归纳非证明。',
'math08':'有向累计角与同终边、轴上角、度弧度、扇形弧/弦/周长、环扇与弓形、受限最值可达和单位。',
'math09':'坐标定义与r正、象限及轴上分母、诱导函数与符号、原域保留、图像平移除B/极点断线、反三角主值非倒数及全部解。',
'math10':'边角对位、SSA两支/无解、外接R因子2、SAS夹角及SSS存在、Heron半周长、面积取等、方位/仰角/眼高/共线建模。',
'math11':'同角及共同域、根号绝对值、恒等证明与数值验算不同、和差乘积/余弦号、辅助角象限与可达、半角新象限、周期分支/零因子/增根回代。',
'math28':'隐函数各支和竖直切线、三角导数rad、ln绝对值域、x^x正支、洛必达条件、驻点非必极值和二阶零非必拐点。',
'math29':'反链系数、n=−1对数、部分分式重复因子与二次分子、三角积分系数、代换范围绝对值、分部/循环积分和求导验算。',
'math30':'阶数与解回代、先保平衡解再除变量、ln绝对值和区间、积分因子全式乘、初值域、冷却温差和混合体积/单位。',
'math31':'基步和任意k递推、AMGM符号与取等、存在和唯一否定、二分连续与异号/区间宽界、Newton失败与残差非距离保证。',
'math32':'被动移轴与主动移点、旧新变量替换方向、正交转轴正逆、A=C不除零、消交叉仍分类、回代和距离不变量。',
'math33':'轨迹两向及消参数范围/原点、焦准e=0极限与直接代入不同、实点及退化、抛物p与4p/顶点切线、椭圆和双曲参数关系、焦和焦差、渐近线非分支。',
'math34':'i²与虚部定义、共轭非倒数、除零/复根主值规则、主Arg区间和零、乘模加角与主值折回、整数幂、全部n根与零重数、实系数共轭配对。',
'math35':'右手正交轴/投影非实交、点与自由向量、内分和线性相关、点积标量及零角、投影模平方、外积反序/面积/体积、异面/包含及角距分母。'
}
assert len(profiles)==40
rows=[];chap=[]
for c in progress['chapters']:
 stem=c['stem'];base=json.loads((R/f'data/base-lessons/{stem}.json').read_text());units=json.loads((R/f'data/notes/{stem}.json').read_text())
 assert stem in profiles
 ch={**c, 'author_review_focus':profiles[stem], 'review_basis':'author_content_sweep_plus_explicit_independent_samples', 'external_teacher_approved':False}
 chap.append(ch)
 for sec in base['sections']:
  u=units[sec['id']];questions=u['examples']+u['practice']+[u['quiz']]
  rows.append(dict(stem=stem,section=sec['id'],title=sec['t'],modules_present=12,explanation_chars=sum(map(len,sec['body']+u['deep'])),topic_paragraphs=len(sec['body']+u['deep']),worked_examples=len(u['examples']),practice=len(u['practice']),quiz=1,full_solution_fields=all(all(q.get(k) for k in ['given','analysis','method','principle','steps','ans','verification','pitfall']) for q in questions),M07_topic_tips=u['exam'],M07_worked_reference='e'+str(u['strategy']['worked_example_index']),M12_goal_checks=[dict(goal=u['goals'][d['goal_index']],question_ref=d['question_ref'],review_module=d['review_module']) for d in u['diagnostics']],source_status=u['verification_status'],author_review_profile=profiles[stem],scientific_status='author_reviewed_with_stated_sample_checks_not_teacher_approved'))
assert len(rows)==218
quality=dict(status='author_content_review_completed_with_limits',scope='All218 newly authored units checked for identity, explanation, solution structure, topic strategies, diagnostic links and stated conditions. Independent calculations cover named samples in test reports, not every statement or every one of1744 questions by a second person.',counts=st,chapters=chap,sections=rows,corrections=['15 question stems/conditions made standalone instead of relying on a previous example','18 biology units received explicit goal-aligned diagnostic references','extra TeX escaping in new batch formula cards corrected; original cards unchanged','final mathematics/optics notation clarified: equal signs, fraction slashes, axis-zero conditions','two stale dashboard test fixtures updated for newly written mathematics chapters and II-only chapter routing'],remaining_limits=['Teacher/external second-person exhaustive scientific review not performed','2027 official scope/assessment applicability not asserted','218 illustration briefs are unproduced requirements; no new diagrams certified','Two direct Dong Zong preview URLs return404; actual cached textbook directory evidence is separately recorded'])
(out/'CONTENT_QUALITY_REVIEW.json').write_text(json.dumps(quality,ensure_ascii=False,indent=2)+'\n')
md=['# 内容质量复核与边界','',f"本轮新增{st['new_unique_chapters']}章、{len(rows)}真实小节，12模块合计{len(rows)*12}个模块。完成作者一轮内容校核和列明的独立计算样本；未进行教师或第二人对全部1744题的穷尽审定。",'', '不能将“12个模块存在”或“字符数超过阈值”当作全部教学质量已经获官方批准。','', '## 实际整改','']+['- '+x for x in ['补全15道题的独立题干/条件，题库抽题不再需要回看前题。','18个生物小节改为显式目标—题目—复习模块对应，检测仅作该目标抽样，不声称一题涵盖全部子技能。','修正本批公式卡多余反斜线；检查真实分数、根号及新旧公式互不改写，100项公式结构检查通过。','补正最后数学/光学章部分等号、分式斜线与零坐标表达；未更改数值结果或原课程身份。','M07保留逐节方法选择、条件和具体完整例题，而非用固定提醒代替解题过程。']]
md+=['','## 深度信号（不是学术审定替代）','',f"每节至少6段独立讲解；本批讲解合计长度最小{min(r['explanation_chars'] for r in rows)}字、最大{max(r['explanation_chars'] for r in rows)}字（仅计概念讲解，不含例题练习）。每节3个例题、4题分层练习、1题独立检测，均有分析、条件、方法、原理、计算/推理、答案、验算和易错说明。",'', 'M01/M02/M11为目标、前置与速记，按教学功能简明呈现；M04–M10不能以目标短句替代。原理推导、模型限制和题目解析见实际笔记，图像仍待制作的知识未删去。','', '## 各章校核重点','']
for c in chap:md+=['- '+c['stem']+'：'+c['author_review_focus']]
md+=['','## 科学与数学核验','','- MATH_VERIFICATION.json：156项独立符号/逻辑/算例检查。','- SCIENCE_CALCULATIONS.json：210项独立理化生计算样本。','- FINAL_CALCULATIONS.json：82项最后四章精确算例及化学原子/电荷账。','- 共448项样本，不等于1744题全部经过第二人独立验证；非计算性生物过程依来源与作者条件复核，仍保留部分核实状态。','- 精确受迫振幅峰位置按分母求导，未将参考页面的近似ω₀表述当普适精确结论；光子能量按E=hf=hc/λ，未沿用个别页面与波长正比的文字误述。','','## 来源和后续','','学校安排与正式UEC要求继续分开。所有新题标原创，不捏造考频、官方步骤分或2027适用性。来源链和实际HTTP状态见SOURCES.csv、SOURCE_LINK_CHECKS.json及sources/batch06/MATH_DIRECTORY_RECOVERY.md。图像要求见illustrations/batch06/PROMPTS.json，218项均未制作，不冒称原142项图片任务已完成。','']
(out/'CONTENT_QUALITY_REVIEW.md').write_text('\n'.join(md))
# Complete retained framework coverage; lack of a lesson file is not proof of a missing textbook directory.
curr=json.loads((R/'data/curriculum.json').read_text());codes={'物理':'phys','化学':'chem','生物':'bio','数学':'math'};newstems={c['stem'] for c in chap}
direct=[]
for f in ['official-directory-index.json','physics-directory-index.json','math-directory-index.json']:direct+=json.loads((R/'sources/batch06'/f).read_text())
coverage=[]
for c in curr:
 stem=codes[c['subject']]+f"{c['chapter']:02}";exists=(R/f'lessons/{stem}.js').exists();dr=[r for r in direct if r['subject']==c['subject'] and r['chapter_id']==c['chapter']]
 state='new_batch06_notes' if stem in newstems else 'prior_notes_preserved_not_counted_new' if exists else 'not_authored_in_this_delivery'
 reason='' if exists else '有已登记目录依据，未纳入本轮40章；可后续继续编写' if dr else '本轮未取得完整同版小节目录；保留原章和全部数据，不认定原课本无小节'
 coverage.append(dict(subject=c['subject'],chapter=c['chapter'],title=c['title'],stem=stem,status=state,recorded_directory_rows=len(dr),reason=reason))
(out/'COURSE_COVERAGE.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
(out/'UNFINISHED_CHAPTERS.json').write_text(json.dumps([x for x in coverage if x['status']=='not_authored_in_this_delivery'],ensure_ascii=False,indent=2)+'\n')
with (out/'COURSE_COVERAGE.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(coverage[0]),lineterminator='\n');w.writeheader();w.writerows(coverage)
missing=[x for x in coverage if x['status']=='not_authored_in_this_delivery']
(out/'UNFINISHED_CHAPTERS.md').write_text('# 未编章节与真实原因\n\n未编不等于课本没有小节。保留116章原框架，不把尚未获本轮目录证据的章说成原照片不存在。\n\n'+'\n'.join('- '+x['subject']+' '+str(x['chapter'])+' '+x['title']+'：'+x['reason']+'。' for x in missing)+'\n')
(R/'illustrations/BATCH_INDEX.md').write_text('# 绘图任务索引\n\n- 原始142任务：[完整旧Prompt](PROMPTS_BATCH_ALL.md)、[原master](ILLUSTRATION_MASTER_MANIFEST.json)。历史状态与缺口保留，未被新增任务数冲抵。\n- Batch05：[94项新增任务](batch05/PROMPTS.md)。\n- Batch06：[218项完整中英文Prompt](batch06/PROMPTS.md)、[机器清单](batch06/PROMPTS.json)。每项包含真实章/节、对象、科学关系、标签/公式/单位、尺寸、中文/英文Prompt、Negative Prompt、验收与来源、优先级、旧图复用判断及确定性SVG要求。\n\nBatch06没有生成新图片，没有发布任何隔离图，也没有将缺图知识删去。任务是复合教学图需求，不将一个需求数冒充已制作图片数；制作后仍须逐图科学和可读性审核。\n')
print('Reviewed218 units; retained116 framework chapters;',len(missing),'chapters without integrated notes remain')
