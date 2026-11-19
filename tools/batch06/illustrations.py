"""Detailed independent drawing briefs for newly authored real subsections; no images produced."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];out=R/'illustrations/batch06';out.mkdir(parents=True,exist_ok=True)
english={
'math06':[
'Show distance intervals about a with radius r greater than zero; interior is an intersection, exterior is a union. Excluded endpoints are open.',
'Compare upward-opening quadratics with two distinct real roots, a repeated root and no real roots. A repeated root does not reverse the sign.',
'For (x-2)/(x+1) at least zero, exclude x=-1 and include x=2. The signs are positive, negative, positive on consecutive intervals.',
'Graph x and y nonnegative, x+y at most4, x+2y at most6. The exact vertices are (0,0),(4,0),(2,2),(0,3).',
'Over that four-vertex region,3x+2y has values0,12,10,6. Its maximum is12 at(4,0). Distinguish continuous regions from integer lattice points.'],
'chem20':[
'Separate reactant consumption rate, product generation rate and stoichiometrically normalized reaction rate. Distinguish a secant average from an instantaneous tangent.',
'A2cm cube cut into eight1cm cubes keeps volume8cm cubed but doubles total area from24 to48cm squared. Equal reacted amounts can share the same gas plateau.',
'At fixed temperature, doubling A and quadrupling the initial rate supports order2 in A for the stated model. Adding inert gas at fixed volume does not increase A concentration.',
'Heating changes the molecular energy distribution and increases the fraction above a fixed activation threshold; it does not itself lower that threshold. Temperatures in Arrhenius formulas are kelvin.',
'Use reactant energy20 and product energy-10kJ/mol for both paths. Peaks80 and50 give activation barriers60 and30 while reaction enthalpy stays-30.'],
'chem21':[
'At equilibrium forward and reverse rates are equal and generally nonzero; different species concentrations can have different constant levels.',
'Write equilibrium powers from balanced stoichiometry. Pure solid activities are1 in the stated model. Reverse K=1/K; doubling all coefficients squares K.',
'For2A reversibly forming B, initial A1 and B0, equilibrium concentrations are1-2x and x. Reject x=1 for negative A; x=0.25 yields A0.50,B0.25 when the given K is1.',
'For A reversibly forming B with K2, adding A at fixed volume changes A instantly but not B. Final values may be A0.267,B0.533 rather than restoring original A.',
'For2A gas reversibly forming B gas, isothermal halving of volume divides Q by2. Inert-gas addition at fixed volume and at fixed total pressure are different operations.',
'For an exothermic forward reaction, heating generally lowers its K while it may accelerate reaction rates. Heat is not an ordinary concentration term.',
'A catalyst can increase both forward and reverse rates without changing their equality at equilibrium. At fixed temperature the final plateau and K remain unchanged.',
'Separate equilibrium yield, time, compression cost and recycling. Opposing temperature and pressure effects need quantitative information to decide their net result.'],
'chem22':[
'Distinguish the existence of ions from their mobility. Concentration, extent of ionization and solubility are separate properties; solid salt and its solution differ.',
'CaF2 releases one Ca2+ and two F-. Ksp uses free-ion activities or the specified dilute approximation. Q>Ksp means a precipitation tendency, not an instantaneous visible event.',
'For AB salt pure-water molar solubility gives Ksp=s squared. For AB2 it gives s times(2s)squared=4s cubed. These require no background ions or competing equilibria.',
'A common ion can reduce molar solubility while a complexing reaction can increase total dissolved metal by lowering free metal. Fixed-temperature Ksp need not change.',
'Calculate ion moles divided by the total mixed volume before Q. AB and AB2 have different precipitant thresholds; precipitation onset is not complete separation.',
'Combine AgCl dissolution with AgBr precipitation. The net reaction is AgCl solid plus Br- to AgBr solid plus Cl-. K is the ratio of matching Ksp values and actual direction also depends on Cl-/Br-.'],
'bio04':[
'Distinguish an increase in cell number from differentiation into new types. Connect each specific cellular structure to a mechanism and then its function.',
'Show a mesophyll cell, mesophyll tissue and whole leaf at distinct levels. A stomach contains multiple tissue types. Blood and bone can both be connective tissues.',
'Cell-number recovery, wound closure and restoration of original tissue function are different outcomes. Trace source, identity, structure and function separately.',
'Separate cell cloning from whole-organism cloning. Nuclear donor, cytoplasmic donor and developmental environment contribute differently; mitochondrial inheritance must not be omitted.',
'The same detectable DNA sequence may have different RNA levels between cell types. RNA, protein and functional evidence remain distinct; normalize signals by sample amount.',
'Draw mature mammalian red cells without nuclei or mitochondria but with membranes and cytoplasm. Do not generalize this to all animals. Differentiate xylem vessels from living phloem elements.',
'Stem cells self-renew and generate differentiated progeny under specified conditions. In the asymmetric toy model one stem cell produces one nondividing differentiated cell each round;5rounds leave1stem and5differentiated cells.'],
'bio14':[
'Separate discovery of transformation from identification of its chemical cause. Enzyme controls must verify effective degradation; a DNA-phage result does not make every virus DNA-based.',
'DNA strands are antiparallel. AT pairs have2 hydrogen bonds and GC3.100base pairs contain200nucleotides;100base pairs with40GC pairs have240hydrogen bonds.',
'Semiconservative replication preserves one template strand per daughter duplex. Starting with fully heavy DNA and light precursors gives all hybrid after1round, half hybrid and half light after2rounds.',
'Template3-prime TACGGA5-prime produces RNA5-prime AUGCCU3-prime. Stop codons do not add amino acids; distinguish template DNA from coding DNA and whole mRNA from its reading frame.',
'In the standard code GCU and GCC both encode alanine, while UAU to UAA can introduce a stop. A one-base coding insertion can shift the downstream frame; a three-base insertion need not shift it but can still affect function.'],
'bio15':[
'Aa crossed with Aa gives AA,Aa,Aa,aa. Under complete dominance the genotype ratio is1:2:1 but phenotype ratio3:1. Among dominant offspring the heterozygote probability is2/3.',
'Independent AaBb produces four equally likely gamete types. Complete linkage AB/ab with no recombination produces only AB and ab. State the assumptions for9:3:3:1.',
'For carrier mother XAXa and unaffected father XAY, fathers transmit X to daughters and Y to sons. Affected sons are1/4 of all children but1/2 of sons in the stated model.',
'Keep single-gene inheritance, chromosome-number abnormalities and multifactorial conditions distinct. A classroom risk model and screening result are not a personalized diagnosis.'],
'bio16':[
'A linear6000bp molecule cut at1000 and3500 gives1000,2500,2500bp fragments. A circular6000bp molecule cut at two sites separated by1500 gives1500 and4500bp.',
'DNA presence, transcription, protein presence and function require distinct evidence. Include unmodified-host and empty-vector controls where appropriate; do not equate selection with proven correct expression.',
'PCR separates denaturation, primer annealing and extension. New strands grow5-prime to3-prime. Ideal5templates after6rounds give320total and315new copies; actual efficiency may be lower.',
'Separate scientific risk questions, exposure routes, evidence limits and ethical choices. A short greenhouse result does not prove permanent zero risk in every environment.'],
'bio17':[
'Genetic, species and ecosystem diversity are different levels. Two samples can each contain4species but have25,25,25,25 versus97,1,1,1 individuals.',
'Taxonomic levels are nested. Genus plus specific epithet form a binomial. Rotating a phylogenetic node does not change ancestry; unscaled branch length does not measure time.',
'Equal habitat area need not mean equal connectivity.1000to700ha is30percent loss. Catch per effort can fall even when effort increases.',
'In-situ and ex-situ conservation are complementary but not interchangeable. An intervention change40minus a reference change20 gives an adjusted change20 under the stated comparable design.'],
'phys12':[
'Brownian motion directly tracks a suspended particle, not a visible water molecule. Net intermolecular force can vanish while attraction and repulsion are both nonzero.',
'Molar mass divided by Avogadro constant is single-particle mass. Gas volume per particle includes empty spacing and is not molecular material volume. Film thickness V/A needs a monolayer assumption.',
'Particles in solids still vibrate, liquid particles remain relatively close and gas particles can have large spacing. Distinguish noncrystalline solids and ionized plasma.',
'Stress F/A, strain extension/original length and Young modulus have different units. A2m rod,0.50mm squared section,E100GPa,F100N stretches4mm in the stated linear model.',
'For a two-surface soap film F=2gamma times edge length. In a narrow static tube balance2pi r gamma cos(theta) against rho g pi r squared h. Negative cosine can produce capillary depression.'],
'phys13':[
'25C is298.15K, while25to40C is a15K interval. Temperature, stored internal energy and transferred heat must remain distinct.',
'Use the offset-corrected two-point calibration100(X-X0)/(X100-X0). Sensitivity, display resolution, accuracy and response time are separate measurement properties.',
'Include every absorbing body and calorimeter heat capacity.0.10kg water at80C plus0.20kg at20C gives40C under ideal isolated conditions.',
'Heating0.10kg ice from-10C to20C water requires2100+33400+8400=43900J in the given model. Half melting can leave0.050kg each ice and water at0C.',
'Free uniform thermal expansion enlarges a hole. A larger expansion-coefficient layer lies on the outside of a heated bimetal bend. Constrained rods need a different mechanical analysis.',
'Liquid true expansion and container expansion differ. In the given example20mL liquid increase minus0.60mL container increase gives19.4mL overflow. State the initial full-container condition.'],
'phys14':[
'Conduction can transfer energy without bulk mass flow. Thermal touch sensation does not by itself establish a different initial temperature.',
'In a steady one-dimensional slab P=kA deltaT/L. Series layers carry the same heat flow and share the total temperature difference; they need not share equal differences.',
'Natural convection requires the stated density, gravity and geometry conditions. Forced convection is driven by a fan or pump. Heat itself is not a material that always rises.',
'Radiation uses absolute temperature and distinguishes gross emission from net exchange. At equal body and surroundings temperature net radiation can be zero while emission continues.']
}
english.update(json.loads((out/'TOPIC_CONSTRAINTS_ADDITIONS.json').read_text()))
english.update(json.loads((out/'TOPIC_CONSTRAINTS_SCIENCE.json').read_text()))
tasks=[]
curr={(r['subject'],r['chapter']):r['title'] for r in json.loads((R/'data/curriculum.json').read_text())}
for ev in sorted((R/'data/batch06').glob('*-sections.json')):
 stem=ev.name.split('-')[0];b=json.loads((R/f'data/base-lessons/{stem}.json').read_text());units=json.loads((R/f'data/notes/{stem}.json').read_text())
 assert len(english[stem])==len(b['sections'])
 for i,s in enumerate(b['sections']):
  u=units[s['id']];v=u['illustration_spec'];tid='B06-'+stem.upper()+'-'+s['id'].replace('.','-')
  title=f"{u['subject']}第{u['chapter_id']}章《{curr[u['subject'],u['chapter_id']]}》{s['id']}《{s['t']}》"
  specs='；'.join(v['relations']);labels='；'.join(v['labels']);objects='；'.join(v['objects']);formula='；'.join(u['derive'])
  zh=f"制作{title}的教学图《{v['title']}》。教学目标：{'；'.join(u['goals'])}。必须对象：{objects}。不可画错的关系：{specs}。中文标签：{labels}。公式、单位和条件：{formula}。采用2至3个逻辑面板，主关系在左/上，条件与验算在右/下。建议1280×960、4:3，最小标签24px，四周留48px，不靠颜色单独区分。图形须SVG或数学绘图库确定性构造；AI只可作构图草稿，科学校验通过前不得教学发布。图中数据是原创教学示例，不是实测或官方考题。手机缩放和放大应可读，文字不裁切。"
  en=f"Create a standalone UEC senior-high teaching diagram for chapter{u['chapter_id']}, authentic subsection{s['id']}, with original Chinese title {s['t']}. Topic-specific mandatory science: {english[stem][i]} {v['english']} Required objects, preserving these Chinese labels: {objects}. Additional literal Chinese annotation strings: {labels}. Typeset and verify these reference formulas, units and stated conditions: {formula}. Use two or three separated panels, main relationship on the left or top and conditions/checks on the right or bottom. Size1280x960,ratio4:3,minimum label24px,safe margin48px. Use SVG or a deterministic plotting library for scientific geometry, structure, arrows and numbers. AI output may only be a draft layout and cannot be published before scientific review. Values are illustrative teaching data, not measurements or official examination figures. Ensure mobile scaling, zoom readability and no clipped labels."
  tasks.append(dict(id=tid,subject=u['subject'],chapter_id=u['chapter_id'],chapter_title=curr[u['subject'],u['chapter_id']],section_id=s['id'],section_title=s['t'],title=v['title'],teaching_purpose=u['goals'],required_objects=v['objects'],scientific_relations=v['relations'],scientific_relations_en=english[stem][i],chinese_labels=v['labels'],formulas_units_variables=u['derive'],composition='2–3逻辑面板；主结构左/上，条件与验算右/下；不以颜色独占编码',dimensions=dict(width=1280,height=960,ratio='4:3',min_label_px=24,safe_margin_px=48),prompt_zh=zh,prompt_en=en,negative_prompt='No incorrect arrow directions, reversed DNA polarity, unbalanced chemical charges, omitted denominator exclusions, Celsius in absolute-temperature powers, invented data, fake official scoring, impossible cell structures, decorative curves replacing equations, duplicate labels, tiny low-contrast text, clipping, watermark or photorealism replacing a scientific schematic.',acceptance_criteria=v['relations']+['逐项核对对象、中文、数值、单位与定义域/模型条件','图示与原例题条件一致，不机械套用其他题的数据','检查320/390px与桌面缩放及放大，无文字裁切','XML/路径通过不代表科学审核通过，发布前需单独复核'],sources=u['content_sources'],priority=v['priority'],reuse=dict(possible=False,note=v['reuse'],assets=[]),deterministic_drawing_required=True,recommended_format='SVG',category='mathematical_plot' if u['subject']=='数学' else 'precise_scientific_svg' if u['subject'] in ['物理','化学'] else 'structural_schematic',production_status='not_produced_pending_review',module_visual_coverage={str(k).zfill(2):dict(task_ids=[tid] if k in [3,4,5,6,8,9,10,12] else [],note='主模型辅助；题目各有独立条件与数据，不能以缺图删减教学，也不强称一图涵盖所有题的不同模型') for k in range(1,13)}))
bundle=dict(schema_version='batch06-1',status='authoring_target_reached_drawing_tasks_unproduced' if len(list((R/'data/batch06').glob('*-sections.json')))>=40 else 'ongoing_not40_chapters_complete',statistics=dict(tasks=len(tasks),new_images_generated=0),tasks=tasks)
(out/'PROMPTS.json').write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n')
md=['# Batch06 新增真实小节绘图任务','',f'{len(tasks)}项独立复合教学图规范；没有生成新图片，也没有将原142项缺口冒称补齐。','']
for t in tasks:
 md += [f"## {t['id']} · {t['subject']} {t['section_id']} {t['section_title']}",'',f"优先级：{t['priority']}；状态：{t['production_status']}；推荐SVG1280×960。",'','用途：'+'；'.join(t['teaching_purpose']),'','对象：'+'；'.join(t['required_objects']),'','关系：'+'；'.join(t['scientific_relations']),'','中文标签：'+'；'.join(t['chinese_labels']),'','公式/单位：'+'；'.join(t['formulas_units_variables']),'','### 中文Prompt','',t['prompt_zh'],'','### English Prompt','',t['prompt_en'],'','### Negative Prompt','',t['negative_prompt'],'','### 科学验收','']+['- '+x for x in t['acceptance_criteria']]+['','旧图复用：'+t['reuse']['note'],'','来源：']+['- '+s['url'] for s in t['sources']]+['']
(out/'PROMPTS.md').write_text('\n'.join(md))
print('Authored',len(tasks),'detailed bilingual briefs; generated0images')

