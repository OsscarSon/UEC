"""Register corroborated textbook identities and authored illustration tasks; no image generation."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
p=R/'data/review/new_sections.json';registry=json.loads(p.read_text());registry=[x for x in registry if x['chapter_id']<7]
manifest=json.loads((R/'illustration-manifest.json').read_text());en=json.loads((R/'data/review/illustration_english.json').read_text());seen={x['id'] for x in manifest['illustrations']}
for ch in range(7,12):
 base=json.loads((R/f'data/base-lessons/chem{ch:02}.json').read_text());units=json.loads((R/f'data/notes/chem{ch:02}.json').read_text())
 for sec in base['sections']:
  sid=sec['id'];u=units[sid];spec=u['illustration_spec'];id='ILL-B04-CHEM-'+sid.replace('.','_')
  registry.append(dict(subject='化学',chapter_id=ch,section_id=sid,section_title=sec['t'],source_url='https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf',page=3 if ch<=10 else 4,locator='高中化学上册2017版，第'+str(ch)+'章叶级目录；版次/书单/既有章匹配见reports/batch04/TEXTBOOK_MATCH.md',source_type='corroborated_textbook_directory',verification_status='directory_identity_corroborated',scope='目录身份经出版社资料、学校历史书单和现有章名交叉核对；原Claude照片未恢复、2027使用及全部学术内容不是已确认',access_date='2026-11-18'))
  en[id]+=' '+json.loads((R/'data/authoring/illustration_conditions.json').read_text())[sid]
  source_id='os_b04_'+sid
  if not any(x['id']==source_id for x in manifest['scientific_source_register']):manifest['scientific_source_register'].append(dict(id=source_id,title='OpenStax Chemistry 2e '+sec['t'],url_or_file=u['authoring_sources'][0]['url'],locator=u['authoring_sources'][0]['page_or_section'],verification_status='partially_verified',evidence_scope='辅助理论；非教材小节编号或考试范围',access_date='2026-11-18'))
  en[id]=spec['english']
  req=spec['scientific_requirements']+['分面板覆盖本节知识关系与例题对象；M03关联为条件/分类，不把所有标签串成因果。','示意非比例；凡用数量或坐标必须从已给题干逐项计算。独立教学标注版与检测留空版分开。']
  r=dict(id=id,subject='化学',subject_code='chemistry',chapter_id=ch,chapter_title={7:'化学键与分子间作用力',8:'氧化还原反应',9:'IA族元素：钠和钾',10:'IIA族元素：镁和钙',11:'IIIA族元素：铝'}[ch],section_id=sid,section_title=sec['t'],section_exists=True,record_kind='new_teaching_diagram',title=sid+' '+sec['t']+'：结构、条件及守恒图',teaching_purpose='支持本节从组成/条件到性质/计算的推理，帮助检验例题而非仅装饰。',action='new',category='precise_scientific_svg',module_ids=[3,4,5,6,7,8,9,10,12],drawing_requirements=req,required_labels=spec['labels'],scientific_basis=[dict(source_id=source_id,scope='理论',verification_status='partially_verified')],source_anchors=[dict(path=f'lessons/chem{ch:02}.js',selector='sections[id='+sid+']'),dict(path=f'data/notes/chem{ch:02}.json',json_pointer='/'+sid)],recommended_format='SVG',dimensions=dict(canvas_width_px=1200,canvas_height_px=1000,minimum_rendered_label_css_px=12,target_rendered_label_css_px=14,mobile_css_width_range=[320,390]),priority='P1',reuse=dict(can_reuse='partial',existing_asset=None,reason='可复用旧符号和布局，不复用已隔离错误图；本小节专用结构尚未制作。'),production_status='brief_ready_not_produced',output_path=None)
  r['formula_spec']=u['derive']
  if id not in seen:manifest['illustrations'].append(r);seen.add(id)
  else:manifest['illustrations'][next(i for i,x in enumerate(manifest['illustrations']) if x['id']==id)]=r
(R/'data/review/illustration_english.json').write_text(json.dumps(en,ensure_ascii=False,indent=2)+'\n');p.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n');(R/'illustration-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
manifest['scope_note']='116章保留、86个已保存/有目录证据小节；237教学图记录、142条制作任务，非全科完成。'
manifest['inventory']['non_section_sources_note']='当前67科学章未制作完整小节笔记，35数学旧章待归科；仅表示实施/资料保存状态，不表示教材无小节。'
for c in manifest['inventory']['chapters']:
 if c['subject']=='化学' and c['chapter_id'] in range(7,12):
  ch=c['chapter_id'];u=json.loads((R/f'data/notes/chem{ch:02}.json').read_text());c.update(section_ids=list(u),section_count=len(u),lesson_path=f'lessons/chem{ch:02}.js',status='directory_corroborated_notes_authored')
  for sec in json.loads((R/f'data/base-lessons/chem{ch:02}.json').read_text())['sections']:
   if not any(x['subject']=='化学' and x['section_id']==sec['id'] for x in manifest['inventory']['sections']):manifest['inventory']['sections'].append(dict(subject='化学',subject_code='chemistry',chapter_id=ch,chapter_title=c['chapter_title'],section_id=sec['id'],section_title=sec['t'],lesson_path=f'lessons/chem{ch:02}.js',batch_note_path=f'data/notes/chem{ch:02}.json',in_41_section_batch=False,existing_svg_paths=[],in_current_batch=True))
manifest['current_reports']='reports/batch04/DELIVERY.md'
(R/'illustration-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Registered28 new textbook sections and illustration tasks')
