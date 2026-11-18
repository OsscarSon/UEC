"""Append new drawing briefs without rewriting the original142 tasks."""
import json,pathlib,hashlib,xml.etree.ElementTree as E
R=pathlib.Path(__file__).resolve().parents[2]
out=R/'illustrations/batch05';out.mkdir(exist_ok=True)
curr=json.loads((R/'data/curriculum.json').read_text());chapter={(x['subject'],x['chapter']):x['title'] for x in curr}
assets={x['code']:x for x in json.loads((R/'reports/v22/ASSET_REVIEW.json').read_text())}
maps={'B42':('生物13','13.1','2n=4示例；染色体按着丝粒计，后期全细胞与每极分别标明。'),
'B46':('生物13','13.2','2n=4减数分裂示例；减Ⅰ分同源，减Ⅱ分姐妹；DNA含量需结合正文另计。'),
'B56':('生物13','13.2','正常对应片段的平衡交叉互换示例；非姐妹交换，不将所有结构变异概括为基因总数不变。'),
'P07':('物理7','7.5','理想重力场无阻力的下落距离—能量关系，不是时间图；零点须一致。'),
'P10':('物理8','8.1','补充独立示例：底4 s、峰6 N的合力脉冲，冲量12 N·s；与正文其他脉冲题数值不同。'),
'P18':('物理7','7.4','补充独立示例：k=200 N/m、x=0.10 m，弹性势能1 J；F=kx在此指大小，形变由自然长起算。'),
'P25':('物理7','7.2','补充独立示例：Fₓ=2x，0至4 m功16 J；这是示例函数，不是实测数据。'),
'P27':('物理8','8.4','补充独立示例：2 kg以3 m/s与1 kg静止物体黏合，末速2 m/s；动能9降至6 J。')}
reuse=[]
for code,(key,sid,caption) in maps.items():
 a=assets[code];assert a['review_status'] in ['PASS','FIXED'];path=R/a['reviewed_path']
 assert hashlib.sha256(path.read_bytes()).hexdigest()==a['reviewed_sha256'];E.parse(path)
 reuse.append(dict(id='B05-REUSE-'+code,code=code,lesson_key=key,section_id=sid,path=a['reviewed_path'],caption=caption,status='approved_for_limited_use',sha256=a['reviewed_sha256'],review='本轮重新读取SVG结构与标签，核对正文模型；历史逐图科学记录见reports/v22/ASSET_REVIEW.json。非教师全面审定。'))
(R/'data/batch05-illustrations.js').write_text('// Add approved reuse mappings only; historical V22 audit is unchanged.\nwindow.APPROVED_ILLUSTRATIONS.push(...'+json.dumps(reuse,ensure_ascii=False,indent=2)+');\n')
(R/'reports/batch05/ILLUSTRATION_REUSE.json').write_text(json.dumps(reuse,ensure_ascii=False,indent=2)+'\n')
tasks=[]
for evidence in sorted((R/'data/batch05').glob('*-sections.json')):
 stem=evidence.name.split('-')[0];notes=json.loads((R/f'data/notes/{stem}.json').read_text());sections=json.loads((R/f'data/base-lessons/{stem}.json').read_text())['sections']
 for sec in sections:
  u=notes[sec['id']];v=u['illustration_spec'];sid=sec['id'];name=chapter[u['subject'],u['chapter_id']];tid='B05-'+stem.upper()+'-'+sid.replace('.','-')
  objects='；'.join(v['objects']);relations='；'.join(v['relations']);labels='、'.join(v['labels'])
  theory='；'.join(u['derive']);goal='；'.join(u['goals'])
  reused=[x for x in reuse if x['lesson_key']==u['subject']+str(u['chapter_id']) and x['section_id']==sid]
  prompt=f"为UEC高中{u['subject']}第{u['chapter_id']}章《{name}》真实小节{sid}《{sec['t']}》制作《{v['title']}》教学图。学习目的：{goal}。本图是有条件的科学模型，非实测图或官方考题。必须出现：{objects}。必须保持关系：{relations}。中文标签逐字采用：{labels}。公式及条件：{theory}。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。"
  subject_en={'物理':'physics','化学':'chemistry','生物':'biology','数学':'mathematics'}[u['subject']]
  english=f"Create a UEC senior-high {subject_en} teaching diagram for chapter {u['chapter_id']}, authentic subsection {sid}. Display the original Chinese title exactly: {v['title']}. Topic-specific scientific requirements and instructional purpose: {v['english']} This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: {objects}. Preserve the following Chinese label strings exactly: {labels}. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: {theory}. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise."
  negative=f"禁止错误或省略以下关系：{relations}。不得把{sub if (sub:=sec['t']) else sid}画成另一知识主题；不得改动{labels}的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。"
  tasks.append(dict(id=tid,subject=u['subject'],subject_code=u['subject_code'],chapter_id=u['chapter_id'],chapter_title=name,section_id=sid,section_title=sec['t'],title=v['title'],teaching_purpose=u['goals'],modules=[3,4,5,6],required_objects=v['objects'],scientific_relations=v['relations'],chinese_labels=v['labels'],formulas_units_variables=u['derive'],composition='2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。',dimensions=dict(width=1280,height=960,ratio='4:3',min_label_px=24),prompt_zh=prompt,prompt_en=english,negative_prompt=negative,acceptance_criteria=v['relations']+['全部对象/标签齐全，数值与本文推导逐项一致','按明确模型审查条件，区分示例与实测数据','手机320/390及桌面1280宽检查，放大可读且无裁切','教学图不替代正文及完整解题；科学审阅不等于XML可解析'],sources=u['content_sources'],priority=v['priority'],reuse=dict(possible=bool(reused),assets=[x['path'] for x in reused],note=v['reuse'],coverage='partial' if reused else 'none'),deterministic_drawing_required=True,recommended_format=v['format'],category='mathematical_plot' if any(t in v['title'] for t in ['图象','图像','曲线','数轴']) else 'scientific_schematic',production_status='reuse_partial_remaining_pending' if reused else 'not_produced',verification_status='brief_authored_not_teacher_approved'))
for t in tasks:
 t['category']=('experimental_apparatus' if any(w in t['title']+' '.join(t['required_objects']) for w in ['卡尺','长颈漏斗','反应器','电解两极']) else 'mathematical_plot' if any(w in t['title'] for w in ['图象','图像','函数','坐标','数轴','曲线']) else 'precise_scientific_svg' if t['subject'] in ['物理','化学'] else 'structural_schematic')
 t['module_visual_coverage']={str(i).zfill(2):{'requires_separate_image':i in [4,5],'task_ids':[t['id']] if i in [3,4,5,6,8,9,10,12] else [],'review_note':('关系结构与对象：'+'；'.join(t['scientific_relations']) if i in [3,4,5] else '主图模型辅助理解；本模块题干和解析已独立给出数据与条件，不依赖一张未提供的图，也不得套用主图不同数值。' if i in [6,8,9,10,12] else '以目标、前置、判断过程或速记文字完成相应功能；不强行添加装饰图替代内容。')} for i in range(1,13)}
bundle=dict(schema_version='batch05-1',scope='本轮新增真实小节；原142任务保留，不宣称全部完成',statistics=dict(tasks=len(tasks),reuse_mappings=len(reuse),generated_new_images=0),tasks=tasks)
(out/'PROMPTS.json').write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n')
md=['# 新增章节的独立教学绘图提示词','',f"共{len(tasks)}条复合教学图任务；复用{len(reuse)}幅已审核V22图，未生成新图。原142任务和缺口保持历史记录。每条为独立可复制规范，XML/路径合格不等于科学准确。",'']
for t in tasks:
 md += [f"## {t['subject']} 第{t['chapter_id']}章 · {t['section_id']} {t['section_title']}",'',f"ID：{t['id']}；优先级：{t['priority']}；状态：{t['production_status']}。",'',f"用途：{'；'.join(t['teaching_purpose'])}。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。",'',f"对象：{'；'.join(t['required_objects'])}。",'',f"关系：{'；'.join(t['scientific_relations'])}。",'',f"文字：{'、'.join(t['chinese_labels'])}。",'',f"公式与单位：{'；'.join(t['formulas_units_variables'])}。",'',f"构图：{t['composition']} 1280×960，4:3，SVG确定性制作。",'','### 中文Prompt','',t['prompt_zh'],'','### English Prompt','',t['prompt_en'],'','### Negative Prompt','',t['negative_prompt'],'','### 科学验收与来源','']+['- '+x for x in t['acceptance_criteria']]+['']+['- '+x['url'] for x in t['sources']]+['',f"旧图复用：{t['reuse']['note']}。实际匹配："+(', '.join(t['reuse']['assets']) or '无')+'。','']
(out/'PROMPTS.md').write_text('\n'.join(md))
for filename in ['illustration-manifest.json','illustrations/ILLUSTRATION_MASTER_MANIFEST.json','illustrations/PROMPTS_BATCH_ALL.json']:
 p=R/filename;x=json.loads(p.read_text());x.setdefault('additional_batches',{})['batch05']={'manifest':'illustrations/batch05/PROMPTS.json','prompts':'illustrations/batch05/PROMPTS.md','tasks':len(tasks),'reuse_mappings':'reports/batch05/ILLUSTRATION_REUSE.json','note':'原142任务不改号；新任务不是原任务已完成的声明。'};p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
p=R/'illustrations/PROMPTS_BATCH_ALL.md';text=p.read_text();marker='\n<!-- batch05 -->';text=text.split(marker)[0];p.write_text(text+marker+'\n\n本轮新增章节的全部详细任务见 [batch05/PROMPTS.md](batch05/PROMPTS.md) 与 [JSON](batch05/PROMPTS.json)，与本文件原142任务分列；不得将复用或新需求数当作历史任务全部完成。\n')
p=R/'index.html';text=p.read_text();tag='<script src="data/batch05-illustrations.js"></script>';text=text.replace(tag,'').replace('<script src="batch-ui.js"></script>',tag+'<script src="batch-ui.js"></script>');p.write_text(text)
print(len(tasks),'briefs;',len(reuse),'verified reuse mappings; no new artwork')
