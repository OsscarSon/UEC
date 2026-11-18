"""Compile independent bilingual briefs. No image generation or network requests."""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parents[1];OUT=R/'illustrations';OUT.mkdir(exist_ok=True)
base=json.loads((R/'illustration-manifest.json').read_text());records=deepcopy(base['illustrations'])
en=json.loads((R/'data/review/illustration_english.json').read_text())
add=[
 ('6.1.1','不同的元素组合','三元素组数值检验与证据边界',['以教学数据7/23/39示范两端均值23；另示10/18/30中预测20、差−2','数值关系与性质相似的证据分层；不伪装历史实测值或宣布全部元素适用'],['7/23/39','(7+39)/2=23','10/18/30','观测−预测=−2','教学数据，非实测史料'],'Show teaching triples7/23/39 with endpoint average23, and10/18/30 with predicted20 and observed-minus-predicted -2. Separate numerical fit from chemical-similarity evidence. Do not invent historical observations or infer a universal law.'),
 ('6.1.2','门捷列夫与元素周期表','历史质量排序与现代Z排序',['历史以质量和性质归纳、留空预测作为关系示意，不补猜具体年代或精确预测值','现代例A的Z18/Ar40、B的Z19/Ar39：A先；质量局部逆序不改Z排序'],['历史：质量/性质归纳','预测→后续验证','现代：Z递增','Z18在Z19前','Ar不必逐个递增'],'Compare historical mass/property classification and testable gaps with modern atomic-number ordering. Use hypothetical A:Z18,Ar40 and B:Z19,Ar39; A precedes B despite the mass reversal. No fabricated dates or exact historical prediction values.'),
 ('6.2','元素周期表的结构','组态到周期与族的条件判断',['[Ne]3s²3p⁵为第3周期17族；最高n和价层电子数分两个判断分支','He的1s²位于18族，Na⁺与Ne等电子不改变Na中性3周期1族身份'],['最高占据n=3','价层2+5=7','第3周期17族','He例外','Na⁺≠Ne元素'],'Branch [Ne]3s2 3p5 to highest occupied n3 -> period3, and seven valence electrons -> group17. Show He 1s2 in group18 and Na+ isoelectronic with Ne without moving Na out of period3 group1. Distinguish neutral-atom location from ionic electron configuration.'),
 ('6.3.1','元素周期律','核吸引、屏蔽与距离的趋势关系',['同周期通常核有效吸引增强、原子半径减小；同族向下新增主层与屏蔽使半径常增大','只画定性示意，不造精确pm或kJ/mol；标相同半径定义与中性状态比较'],['Z','有效核吸引','屏蔽','电子主层','通常趋势，局部例外'],'Draw qualitative causal branches for increasing effective attraction across a period and new shells/shielding down a group. Explain usual atomic-radius trends, with explicit neutral-atom and radius-definition conditions. No invented exact radii or ionization-energy measurements; periodicity is not strict pointwise monotonicity.'),
 ('6.3.2','原子的电子层结构与元素的分区','s/p/d/f分区与容量',['轨域数1/3/5/7，各最多2e，容量2/6/10/14；分区与周期不得共用一个判断','[Ar]3d⁶4s²的最高n4而特征副层3d，属第4周期d区；He标组态与族位置的特殊性'],['s/p/d/f','轨域1/3/5/7','容量2/6/10/14','Fe：周期4，d区','He说明'],'Map s/p/d/f orbital counts1/3/5/7 to capacities2/6/10/14. Keep block classification distinct from highest occupied n. Fe [Ar]3d6 4s2 is period4 d-block, not period3. Note the He configuration/group-location convention and do not imply p-block atoms contain no s electrons.'),
 ('6.3.3','元素基本性质的周期性变化规律','逐级电离跃升与等电子半径',['题给IE为600/1800/2700/11600kJ·mol⁻¹，第3后跃升支持主族3价电子，不画成4','Na⁺/Mg²⁺/Al³⁺均10e，Z11/12/13，半径定性Na⁺>Mg²⁺>Al³⁺；不造具体pm'],['逐级IE/kJ·mol⁻¹','第3→4步跃升','主族价电子3','10电子','Na⁺>Mg²⁺>Al³⁺'],'Plot the stated original exercise IE values600,1800,2700,11600 kJ/mol at steps1..4; the jump AFTER three removals suggests three valence electrons for a main-group atom, not four. In a separate qualitative panel compare10-electron Na+,Mg2+,Al3+ with Z11,12,13 and radius Na+>Mg2+>Al3+. Invent no precise ionic radii.')]
source=dict(source_id='dz_chem_content_table',scope='真实小节身份；不是2027适用锁定',verification_status='partially_verified')
for sid,title,fig,req,labels,eng in add:
 id='ILL-PLAN-CHEM-'+sid.replace('.','_')+'-01';en[id]=eng
 if id in {r['id'] for r in records}:continue
 records.append(dict(id=id,subject='化学',subject_code='chemistry',chapter_id=6,chapter_title='元素周期表',section_id=sid,section_title=title,section_exists=True,record_kind='new_teaching_diagram',title=fig,teaching_purpose='使本节的结构推理、数值账本和适用条件可直接检查。',action='new',category='precise_scientific_svg',module_ids=[3,4,5,6,7,8,9,10,12],drawing_requirements=req,required_labels=labels,scientific_basis=[source,dict(source_id='os_periodic',scope='电子结构/趋势；非历史精确值',verification_status='partially_verified')],source_anchors=[dict(path='lessons/chem06.js',selector='sections[id='+sid+']'),dict(path='data/notes/chem06.json',json_pointer='/'+sid)],recommended_format='SVG',dimensions=dict(canvas_width_px=1200,canvas_height_px=800,minimum_rendered_label_css_px=12,target_rendered_label_css_px=14,mobile_css_width_range=[320,390]),priority='P1',reuse=dict(can_reuse='partial',existing_asset=None,reason='可复用已核基础符号和版式；本节专用图尚待制作。'),production_status='brief_ready_not_produced',output_path=None))
# Extend the six new-section briefs with the conditions added during the final depth review.
for r in records:
 if r['id']=='ILL-PLAN-CHEM-6_1_1-01':
  r['drawing_requirements'] += [x for x in ['把Li/Na/K作为共同+1价性质的例子，与无元素身份的教学三数检验明确分栏；历史近似值不写成现代精确测量'] if x not in r['drawing_requirements']]
  r['required_labels'] += [x for x in ['Li/Na/K：常见+1价','数值证据≠全部性质证据'] if x not in r['required_labels']]
  en[r['id']] += ' Add a separate Li/Na/K chemical-similarity panel with common +1 ions; keep the anonymous teaching triples distinct from measured historical data.'
 if r['id']=='ILL-PLAN-CHEM-6_3_2-01':
  r['drawing_requirements'] += [x for x in ['最高占据n是主族常用捷径，不作全元素定义；注Pd基态[Kr]4d¹⁰仍是第5周期，周期以Z和实际表位核查'] if x not in r['drawing_requirements']]
  r['required_labels'] += [x for x in ['主族捷径有适用条件','Pd：第5周期'] if x not in r['required_labels']]
  en[r['id']] += ' Do not universalize the highest-occupied-n shortcut: Pd [Kr]4d10 remains in period5. Verify period from atomic number and actual table position.'
 if r['id']=='ILL-PLAN-CHEM-6_3_3-01':
  r['drawing_requirements'] += [x for x in ['独立第三面板对照X(g)→X⁺(g)+e⁻的IE、X(g)+e⁻→X⁻(g)的电子添加能量、键中吸引共享电子的电负性；电子亲和能两种符号约定明确区分，Pauling电负性不带kJ/mol', '半径面板标相同半径定义的定性比较；电离能数据为原创题给，非实际某元素数据'] if x not in r['drawing_requirements']]
  r['required_labels'] += [x for x in ['X(g)→X⁺(g)+e⁻','X(g)+e⁻→X⁻(g)','电子亲和能：先定符号','电负性：键中共享电子','Pauling标度无单位'] if x not in r['required_labels']]
  r['dimensions']['canvas_height_px']=1200
  en[r['id']] += ' Add a separate third panel comparing first ionization X(g)->X+(g)+e-, electron addition X(g)+e-->X-(g), and attraction to shared electrons in a chemical bond. State the electron-affinity sign convention; Pauling electronegativity is dimensionless. Never present the exercise IE values as measured values for an identified element.'
# Extend science metadata; no inference that a directory establishes school adoption.
sources=deepcopy(base['scientific_source_register'])
sources.extend([dict(id='dz_chem_content_table',title='董总公开高中化学课程内容跨学科表',url_or_file='https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf',locator='PDF第2页第6章；页3第7–8章可作后续研究候选',verification_status='partially_verified',evidence_scope='小节身份，不是整本教材全文或2027适用确认',access_date='2026-11-18'),dict(id='os_periodic',title='OpenStax Chemistry 2e periodic variations',url_or_file='https://openstax.org/books/chemistry-2e/pages/6-5-periodic-variations-in-element-properties',locator='电子结构、半径、电离能定义与趋势',verification_status='partially_verified',evidence_scope='科学原则，非考试频率',access_date='2026-11-18')])
source_by_id={s['id']:s for s in sources};sources=list(source_by_id.values())
base['illustrations']=records
base['scientific_source_register']=sources
(R/'illustration-manifest.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
neg={
 'precise_scientific_svg':('不得反转箭头运算、偷换单位、改变题给数据、使用错误比例、吞掉绝对值、隐藏条件或伪造实测刻度。','No reversed operations/arrows, changed problem values, inconsistent units/scales, missing absolute-value bars, hidden conditions or invented measured axes.'),
 'structure_schematic':('不得把分类画成因果、把旁路画成货物必经站、把膜画成不连续碎片，或把示意画成真实比例。','No classification-as-causation, energy supply as cargo route, disconnected membranes, impossible compartment crossings, or schematic geometry presented as measured scale.'),
 'math_function_plot':('不得忽略定义域、奇点、开闭端点、坐标尺度及参数条件。','No missing domain, singularities, endpoint conditions, axis scale or parameter assumptions.'),
 'experimental_apparatus':('不得虚构器材、药品配方、剂量、实验数据、误差棒或操作安全保证；不画产气刚性密闭容器。','No invented hardware, recipes, doses, experimental data, error bars or safety guarantees; no rigid sealed gas-generation container.'),
 'supporting_illustration':('不得以装饰替代受力或结构图，不画虚构的惯性力，不加入可误读为定量的箭头。','No decoration replacing a required force/structure diagram, invented inertial force, or decorative arrows interpreted as quantities.')}
subject_en={'physics':'Physics','chemistry':'Chemistry','biology':'Biology'}
tasks=[];master=[]
for r in records:
 item=deepcopy(r)
 item['legacy_audit_commit']=base['audited_commit'];item['generated_image_is_not_scientific_approval']=True
 if r['action'] in ('new','correct','redraw'):
  assert r['id'] in en,r['id']
  dim=r['dimensions'];w,h=dim['canvas_width_px'],dim['canvas_height_px'];det=r['category']!='supporting_illustration'
  urls=[source_by_id[b['source_id']]['url_or_file'] for b in r['scientific_basis']]
  labels=r['required_labels'];cnneg,eneg=neg[r['category']]
  cn=(f'为UEC中文原创学习笔记绘制“{r["title"]}”。唯一ID：{r["id"]}。科目{r["subject"]}，原第{r["chapter_id"]}章“{r["chapter_title"]}”，真实小节{r["section_id"]}“{r["section_title"]}”。教学目的：{r["teaching_purpose"]}。'
      +'必须画出的对象与正确关系：'+'；'.join(r['drawing_requirements'])+'。'
      +'图中文字逐项准确保留：'+'；'.join(labels)+'。'
      +f'采用{w}×{h}画布；双面板在手机可拆为纵向，渲染文字至少12 CSS px、目标14；线型/形状与颜色共同区分。白底高对比，科学层、箭头、文字分层，公式变量和单位不能装饰化。'
      +('最终科学图优先用SVG/数学绘图库确定性制作。AI仅可作构图草稿，所有数值、几何、膜层和文字须重建核验后才能用于教学。' if det else '辅助人物轮廓可AI绘制，但科学箭头与定量信息必须另用确定性矢量层核验。')
      +'标注版与练习留空版分开，只采用已有题给条件，不泄露检测答案。来源/理论核对：'+'；'.join(urls)+'。来源不等于2027考试范围确认；制作前重新核对。')
  eng=(f'Create an original Chinese-language teaching diagram titled "{r["title"]}". Unique ID {r["id"]}; {subject_en[r["subject_code"]]}, existing chapter {r["chapter_id"]}, actual subsection {r["section_id"]} ("{r["section_title"]}"). Scientific objects, relationships and exact constraints: '+en[r['id']]
       +' Required on-canvas Chinese labels, preserved verbatim: '+ '; '.join(labels)+'. '
       +f'Use a {w} by {h} canvas. Reflow panels vertically on mobile, with rendered labels at least12 CSS px, target14. Use shape/line style as well as color, white background and high contrast. Keep geometry, arrows and editable text on separate layers. '
       +('The final scientific output must be constructed with SVG or deterministic mathematical plotting; an AI image is only a layout draft and cannot certify geometry, counts, membranes or formulas. ' if det else 'An AI-generated silhouette is allowed only as supporting art; independently computed vector overlays must carry all forces and quantities. ')
       +'Make annotated teaching and blank assessment variants separately, using only existing stated problem data. Recheck these theory/source references before production: '+'; '.join(urls)+'. These sources do not certify2027 exam scope or official marking rules.')
  task=dict(id=r['id'],subject=r['subject'],subject_code=r['subject_code'],chapter_id=r['chapter_id'],chapter_title=r['chapter_title'],section_id=r['section_id'],section_title=r['section_title'],title=r['title'],teaching_purpose=r['teaching_purpose'],must_appear_objects=labels,correct_scientific_relationships=r['drawing_requirements'],chinese_labels=labels,formulas_units_variables=[x for x in labels if any(ch.isascii() and(ch.isalpha() or ch.isdigit()) for ch in x)] or ['按所列关系使用结构名称，不添加未经核实的数值/公式'],composition_requirements=r['drawing_requirements']+['科学图层与文字分层；相邻面板坐标/颜色语义一致'],suggested_dimensions=dict(width_px=w,height_px=h,aspect_ratio=f'{w}:{h}',minimum_rendered_label_css_px=12),chinese_prompt=cn,english_prompt=eng,negative_prompt=dict(zh=cnneg+'不使用乱码、伪官方标志、水印遮挡、未说明的缩写或“同上”。',en=eneg+' No garbled Chinese, fake official logos, obscuring watermarks, unexplained abbreviations or references to another prompt.'),scientific_acceptance_criteria=r['drawing_requirements']+['逐字核对标签，逐项验算计数、单位、坐标与箭头','标注版/留空版不混用；人工科学复核后才能接入正式页面'],theoretical_sources=[dict(id=b['source_id'],url_or_file=source_by_id[b['source_id']]['url_or_file'],verification_status=b['verification_status'],scope=b['scope']) for b in r['scientific_basis']],priority=r['priority'],can_reuse_old_image=r['reuse']['can_reuse'],reuse_details=r['reuse'],requires_deterministic_svg_or_plotting=det,production_target='HTML/CSS关系图或可引用SVG' if r['record_kind']=='existing_inline_flow' else 'SVG/确定性绘图' if det else '辅助插画+独立矢量科学层',production_status='brief_ready_requires_science_review' if r['category']!='experimental_apparatus' else 'concept_brief_ready_protocol_parameters_unconfirmed',category=r['category'],action=r['action'],source_anchors=r['source_anchors'],module_ids=r['module_ids'])
  tasks.append(task);item['production_task_id']=task['id'];item['current_production_status']=task['production_status']
 else:
  item['production_task_id']=None;item['current_production_status']='retained_existing_asset' if r['action']=='retain' else 'blocked_missing_math_sections_and_attribution'
 master.append(item)
(R/'data/review/illustration_english.json').write_text(json.dumps(en,ensure_ascii=False,indent=2)+'\n')
imports=json.loads((OUT/'IMPORT_BATCH01_REVIEW.json').read_text())
summary_svg=[]
import xml.etree.ElementTree as ET
for p in sorted((R/'assets/verified').glob('*.svg')):
 prefix,num=p.stem.split('-');sub='化学' if prefix=='chem5' else '生物';ch=5 if sub=='化学' else 3;sid=str(ch)+'.'+num
 tree=ET.parse(p).getroot();labels=[''.join(x.itertext()) for x in tree.iter() if x.tag.endswith('}text')]
 summary_svg.append(dict(id='SUMMARY-'+p.stem.upper(),subject=sub,chapter_id=ch,section_id=sid,title=labels[0],path=str(p.relative_to(R)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),format='SVG',view_box=[0,0,1100,760],teaching_purpose='核对过的关系/账本总结；不是全部结构/装置替代',chinese_labels=labels,requires_deterministic_svg_or_plotting=True,generator='tools/build_verified_diagrams.py',source_anchor='lessons/'+('chem05' if ch==5 else 'bio03')+'.js sections[id='+sid+']',verification_status='partially_verified',status='implemented_deterministic_summary_not_full_structural_replacement'))
statistics=dict(teaching_records=len(master),production_briefs=len(tasks),retained_records=sum(r['action']=='retain' for r in records),blocked_math_plans=sum(r['action']=='defer_verification' for r in records),new_chapter6_tasks=6,briefs_by_subject=dict(Counter(t['subject'] for t in tasks)),briefs_by_priority=dict(Counter(t['priority'] for t in tasks)),inline_relationship_tasks=sum(t['production_target'].startswith('HTML') for t in tasks),uploaded_images_reviewed=len(imports),uploaded_images_approved_limited=sum(x['status']=='approved_for_limited_use' for x in imports),uploaded_images_quarantined=sum(x['status']=='rejected_pending_redraw' for x in imports),deterministic_summary_svgs=len(summary_svg),ai_images_generated_this_round=0)
obj=dict(schema_version='2.0',date='2026-11-18',baseline_commit='daa36377c98508764780831e82d4ecbb06c27e69',scope='58真实小节的现有/新增需求；数学仍仅章级待确认，不编小节或函数参数',statistics=statistics,scientific_source_register=sources,illustrations=master,uploaded_batch01=imports,produced_summary_svgs=summary_svg,non_instructional_assets=base['non_instructional_assets'],limitations=['完整Prompt是待制作任务，不代表图片已生成或通过科学审定','11幅新增SVG多为关系/账本总结，不能冒充完整细胞解剖或实验装置图','数学35章均无可执行Prompt：需真实小节与I/II依据后再制作','其余只有章级目录的部分先查目录和知识范围，未虚构全科插图任务'])
if (OUT/'P0_REVIEW.json').exists():
 p0=json.loads((OUT/'P0_REVIEW.json').read_text());obj['uploaded_p0']=p0
 statistics.update(uploaded_p0_reviewed=len(p0),uploaded_p0_limited=sum(x['status']=='approved_for_limited_use' for x in p0),uploaded_p0_quarantined=sum(x['status']=='quarantined' for x in p0),uploaded_p0_full_tasks_accepted=0)
 for items in [obj['illustrations'],tasks,base['illustrations']]:
  for item in items:
   review=next((x for x in p0 if x['task_id']==item['id']),None)
   if review:item['uploaded_artifact_review']=dict(path=review['path'],status=review['status'],finding=review['finding'],full_task_accepted=False)
 (R/'illustration-manifest.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
(OUT/'ILLUSTRATION_MASTER_MANIFEST.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
(OUT/'PROMPTS_BATCH_ALL.json').write_text(json.dumps(dict(schema_version='2.0',statistics=statistics,tasks=tasks),ensure_ascii=False,indent=2)+'\n')
md=['# 全部已确定的后续教学插图任务','',f'共{len(tasks)}条独立中英文制作Brief；其中{statistics["inline_relationship_tasks"]}条针对HTML/CSS知识关系图，其余为图像制作。另35条数学章级计划因无真实小节/归属而冻结，不假造编号或函数参数。203条旧记录加化学6的6条为209条总记录；60条保留、35条冻结、114条需制作/修正。','',
'本文件不调用AI生图。精确科学图默认SVG或数学绘图库；AI结果仅可作草稿。上传6图的审核与11幅确定性总结SVG另见总清单，不能把它们与新Prompt数混算。','',
'来源身份：学校文件仅用于兴华校内；2026董总文件未自动锁定2027；科学辅助来源不提供考频或官方评分。每条Prompt可独立复制，无“同上”。','']
last=None
for t in sorted(tasks,key=lambda x:({'物理':0,'化学':1,'生物':2}[x['subject']],x['chapter_id'],tuple(map(int,x['section_id'].split('.'))),x['id'])):
 group=t['subject']+' 第'+str(t['chapter_id'])+'章 '+t['chapter_title']
 if group!=last:md+=['## '+group,''];last=group
 md += ['### '+t['id']+' · '+t['title'],'',
 '1. 唯一ID：'+t['id'],
 '2. 科目：'+t['subject'],
 '3. 真实章节及小节：第'+str(t['chapter_id'])+'章 '+t['chapter_title']+'／'+t['section_id']+' '+t['section_title'],
 '4. 插图标题：'+t['title'],
 '5. 教学目的：'+t['teaching_purpose'],
 '6. 必须出现的对象：'+'；'.join(t['must_appear_objects']),
 '7. 不可画错的科学关系：'+'；'.join(t['correct_scientific_relationships']),
 '8. 中文文字及标签：'+'；'.join(t['chinese_labels']),
 '9. 公式、单位与变量：'+'；'.join(t['formulas_units_variables']),
 '10. 精确构图要求：'+'；'.join(t['composition_requirements']),
 '11. 比例及尺寸：'+str(t['suggested_dimensions']),
 '12. 完整中文Prompt：见本条下方完整中文Prompt，可独立复制。',
 '13. 完整英文Prompt：见本条下方Complete English prompt，可独立复制。',
 '14. Negative Prompt：见本条下方中英文Negative Prompt。',
 '15. 科学准确性验收：'+'；'.join(t['scientific_acceptance_criteria']),
 '16. 来源／理论依据：'+'；'.join(s['id']+' '+s['url_or_file']+'（'+s['verification_status']+'）' for s in t['theoretical_sources']),
 '17. 优先级：'+t['priority'],
 '18. 旧图复用：'+t['can_reuse_old_image']+'；'+t['reuse_details']['reason'],
 '19. 需要SVG等确定性绘图：'+str(t['requires_deterministic_svg_or_plotting'])+'；制作目标：'+t['production_target'],
 '20. 制作状态：'+t['production_status']+'；分类：'+t['category']+('；上传P0草稿：'+t['uploaded_artifact_review']['status']+'；仅部分用途，整项任务尚未验收' if t.get('uploaded_artifact_review') else ''),'',
 '**完整中文Prompt**','',t['chinese_prompt'],'','**Complete English prompt**','',t['english_prompt'],'','**Negative Prompt**','',t['negative_prompt']['zh'],'',t['negative_prompt']['en'],'']
md+=['## 冻结的数学计划','', '高数I/II入口保留，旧数学35章均未迁移。总清单为35章保留null小节号。未获取可靠归属、真实目录和参数前，不生成看似可执行的数学图Prompt。','']
(OUT/'PROMPTS_BATCH_ALL.md').write_text('\n'.join(md))
(OUT/'IMAGE_QUALITY_CHECKLIST.md').write_text('''# 教学图科学与界面验收清单

AI生成图一律先是草稿。不能用美观、字段齐备或自动测试通过代替科学审定。每项记录审查者、日期、证据、发现、处理状态；无法核实时保留隔离。

- [ ] 唯一ID、科目、真实章/节、来源锚点完全对应；数学待核不补编号。
- [ ] 中文逐字对照；下标、上标、绝对值、正负号、箭头、分数与变量清楚；不信任AI文字。
- [ ] 定量点/箭头/面积来自明确函数或题给数据；统一比例、坐标、单位、定义域、端点与模型时段。
- [ ] 向量平移后端点闭合；合力不是标量和；夹角端点明确；分量不重复计力；v/a不是额外力。
- [ ] 化学原子、电荷与电子守恒；相态、反应条件与实体写明；mol换算乘除方向与箭头一致。
- [ ] Vm=RT/p只用于适用气体模型；22.4必须绑定273.15K/101.325kPa近似，不混100kPa、液体或固体；NA精确值与题给近似区别。
- [ ] 细胞双层膜叶片、包膜、嵴连续性及区室正确；核孔贯通双膜；核糖体/ER/高尔基体/囊泡货物次序正确。
- [ ] 膜运输区分化学/电化学梯度、初级/次级主动、易化与膜泡；胞吐必须发生膜融合，不穿越完整脂双层。
- [ ] ATP整体水解而非断键本身放能；光解配平；卡尔文碳数使用统一基准；发酵净ATP不重复相加。
- [ ] 实验原理图的控制、测量与边界清楚；未知器材、浓度、剂量、误差、结果不补猜；有待确认门槛。
- [ ] 光路若后续需要，法线、入射/折射角、真实/虚像与介质条件须逐条核验；无真实小节和题设不先造图。
- [ ] 化学结构键型、价态、官能团位置须对可靠结构源；不能只凭轮廓美观验收。
- [ ] 函数图由确定性计算验证，定义域/间断/渐近线/参数齐；未核数学归属不投产。
- [ ] 320/390/1280 CSS px实测；整页无横向溢出，图可放大且文字可辨；放大区可横向滚动但不撑开页面。
- [ ] 键盘可打开/关闭放大框，Esc关闭、焦点回到触发按钮；alt和图注描述模型条件；颜色外还有线型/形状。
- [ ] 练习留空版不泄露答案，与解析版使用相同数据；复用不重复计算成新图数量。
- [ ] 保留旧资源与引用历史；错误图可隔离但不以脚注掩饰已知错误；只有通过审查的图进入教学页。
- [ ] 单独记录学校安排、官方考试范围、科学模型来源；不伪称2027必考、官方评分或实测数据。

本轮状态：6张上传图逐张查看；3张限定用途接入、3张隔离。11幅确定性SVG为总结/账本辅助，不替代全部待制作结构/实验图。教师、官方及全体知识点的独立审定尚未完成。
''')
print(json.dumps(statistics,ensure_ascii=False,indent=2))
