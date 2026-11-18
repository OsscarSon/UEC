import collections,csv,hashlib,json,pathlib,xml.etree.ElementTree as E
R=pathlib.Path(__file__).resolve().parents[2]
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
A=json.loads((R/'reports/v22/ASSET_REVIEW.json').read_text());bycode={a['code']:a for a in A}
sections=json.loads((R/'reports/v22/SECTION_REFERENCES.json').read_text());lookup={(s['lesson_key'],s['id']):s for s in sections}
tasklinks={x['task']:x for x in csv.DictReader((R/'tools/v22/task-links.tsv').open(),delimiter='\t')}
T=json.loads((R/'illustrations/PROMPTS_BATCH_ALL.json').read_text())['tasks']
subject={'physics':'物理','chemistry':'化学','biology':'生物'}
candidate_chapters={
 'P06':[6],'P07':[7],'P10':[8],'P11':[8],'P17':[6],'P18':[7],'P19':[22],
 'P25':[7],'P26':[6],'P27':[8],'P30':[6],'P32':[18],'P33':[18],'P34':[22],'P35':[17],
 'P36':[21],'P37':[22],'P38':[19],'P39':[18],'P40':[22],'P41':[21],'P42':[17],'P43':[24],
 'P44':[21],'P45':[20],'P46':[23],'P47':[24],'P48':[24],'P49':[24],'P50':[21,22],
 'P51':[25],'P52':[20],'P53':[10],'P54':[13],'P55':[13],'P56':[15],'P57':[11],
 'B41':[6],'B42':[13],'B44':[14],'B45':[14],'B46':[13],'B47':[8],'B48':[14],
 'B49':[15],'B50':[10],'B51':[6],'B52':[6],'B53':[8],'B54':[10],'B55':[15,19],
 'B56':[13,15],'B57':[14],'B58':[6],'B59':[8]}
curr=json.loads((R/'data/curriculum.json').read_text())
titles={'B33':'酶与反应活化能','B34':'酶的温度效应：示意模型','B35':'乳酸发酵与NAD⁺再生','B36':'光照强度对净光合速率的影响','P28':'速度方向与加速度方向','P29':'动能与速率的平方关系','P30':'平抛运动：水平与竖直分运动','P31':'胡克定律：弹力与伸长量'}
suppressed={
 'assets/fig/p3_5a.svg':'P01','assets/fig/p3_5b.svg':'P01',
 'illustrations/incoming/batch01/physics/PH-3.5-motion-graphs.png':'P01',
 'assets/fig/p4_3b.svg':'P05','assets/fig/p4_8.svg':'P22','assets/fig/b3_2b.svg':'B03',
 'illustrations/incoming/p0/ILL-ASSET-B3_4.svg':'B04',
 'illustrations/incoming/p0/ILL-ASSET-B3_6B.svg':'B06',
}
runtime=[]
for a in A:
 p=R/(a['reviewed_path'] or a['original_path']);r=E.parse(p).getroot()
 labs=[e.text for e in r.iter() if e.tag.endswith('}text') and e.text]
 a['title']=titles.get(a['code'],labs[0] if labs else a['code'])
 a['task_ids']=[t for t,l in tasklinks.items() if a['code'] in l['codes'].split(',')]
 if a['section_id']:
  key=subject[a['subject']]+a['section_id'].split('.')[0]
  s=lookup[(key,a['section_id'])] # A real saved subsection is mandatory, including alternates.
  a.update(lesson_key=key,chapter_id=int(a['section_id'].split('.')[0]),section_title=s['title'])
  prefix={'physics':'phys','chemistry':'chem','biology':'bio'}[a['subject']]
  note_path=f"data/notes/{prefix}{a['chapter_id']:02d}.json"
  a['course_content_anchor']={'path':note_path,'json_pointer':'/'+a['section_id'],'learning_goals':json.loads((R/note_path).read_text())[a['section_id']]['goals']}
 else:
  a.update(lesson_key=None,chapter_id=None,section_title=None)
  a['candidate_chapters']=[{'chapter_id':c,'chapter_title':next(x['title'] for x in curr if x['subject']==subject[a['subject']] and x['chapter']==c),'status':'知识点对应的现有章级候选；不是已核实小节映射'} for c in candidate_chapters[a['code']]]
 if a['integration_status']=='integrated':
  assert a['review_status'] in ['PASS','FIXED']
  scope='教学模型；适用条件见图，曲线示例不代表实测数据。'
  if a['subject']=='physics' and a['code'] in ['P03','P09','P14','P22','P23']:scope='受力/装置示意不按尺寸或力值比例；按图中给定条件列式。'
  if a['code']=='P16':scope='虚线是mg的数学分量，并非新增作用力；按30°斜面、无摩擦、g=10 N/kg核算。'
  if a['code']=='P05':scope='虚线分量之和复原mg；光滑30°斜面无其他法向力，N=mg cosθ。'
  if a['module']==6:scope='补充图解例，图中数据与本节下列原创题分别核算。'+scope
  a['caption']=a['title']+'。'+scope
  if a['code']=='B32':a['caption']+='固定3个CO₂净输出1个G3P；2份净G3P才相当于1个六碳糖的碳骨架。'
  runtime.append({k:a[k] for k in ['id','code','title','lesson_key','section_id','section_title','module','caption','concept']}|{'path':a['reviewed_path'],'status':a['review_status']})
 register=json.loads((R/'illustrations/ILLUSTRATION_MASTER_MANIFEST.json').read_text())['scientific_source_register']
 related=[s for t in T if t['id'] in a['task_ids'] for s in t['theoretical_sources']]
 a['related_sources']=[next((x for x in register if x['id']==s.get('source_id')),s) for s in related]
 a['selection_reason']='本节选用：通过科学审查，补充已有笔记中的对应知识/推导/图解例' if a['selected'] else ('科学结构待重绘' if a['review_status']=='BLOCKED' else '真实小节未确认，不能编造编号' if not a['section_id'] else '同题材选更完整或更清晰的版本；参考concept分组及逐图审查意见')
dump(R/'reports/v22/ASSET_REVIEW.json',A)
(R/'data/v22-illustrations.js').write_text('// Audited V22 only. Original files, notes and progress keys remain unchanged.\nwindow.V22_ILLUSTRATIONS='+json.dumps(runtime,ensure_ascii=False)+';\nwindow.V22_SUPERSEDED_FIGURES='+json.dumps(suppressed,ensure_ascii=False)+';\n')
coverage=[];missing=[]
for t in T:
 l=tasklinks.get(t['id']);codes=l['codes'].split(',') if l else []
 row={'task_id':t['id'],'subject':t['subject'],'chapter_id':t['chapter_id'],'section_id':t['section_id'],'title':t['title'],'v22_coverage':l['coverage'] if l else 'none',
      'asset_codes':codes,'reviewed_assets':[bycode[c]['id'] for c in codes],
      'displayed_assets':[c for c in codes if bycode[c]['selected']],
      'duplicates':dict((c,[x['code'] for x in A if x['concept']==bycode[c]['concept'] and x['code']!=c]) for c in codes),
      'remaining_requirements':l['remaining'] if l else 'V22未制作此任务的对应图；原任务的对象、科学关系、构图及检测要求仍保留。',
      'task_medium':'existing_inline_html' if t['production_target'].startswith('HTML') else 'standalone_image',
      'legacy_scope':'原内联M03实现保留，本轮未重做其完整科学验收；无V22图片不表示必须另画一张' if t['production_target'].startswith('HTML') else '本表计V22新增覆盖；旧合格SVG及P0限定用途图仍保留，不能把V22无图解释为网站无教学支持。'}
 coverage.append(row)
 if row['v22_coverage']!='full':missing.append(dict(t)|{'v22_remaining_requirements':row['remaining_requirements'],'v22_related_assets':codes,'task_medium':row['task_medium'],'legacy_scope':row['legacy_scope']})
dump(R/'reports/v22/TASK_COVERAGE.json',coverage);dump(R/'reports/v22/MISSING_TASKS.json',missing)
with (R/'reports/v22/ASSET_REVIEW.csv').open('w') as f:
 fields=['id','code','subject','title','review_status','integration_status','lesson_key','section_id','section_title','module','scientific_review','fixes','original_path','original_sha256','reviewed_path','reviewed_sha256','task_ids']
 w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(A)
md=['# V22 逐图科学审查与接入','', 'PASS/FIXED仅表示本轮记录的检查范围通过；不代表教师或官方审定。BLOCKED不进入教学页面。科学审核状态与接入状态分开计数，待映射和重复备选不等于科学错误。','', '|图ID（包内ID保留）|科目/真实小节|科学状态|接入状态|审查结论/修复|','|---|---|---|---|---|']
for a in A:md.append(f"|{a['code']} · {a['id']}|{subject[a['subject']]} {a['section_id'] or '待映射'}|{a['review_status']}|{a['integration_status']}|{a['scientific_review']} {'；'.join(a['fixes'])}|")
(R/'reports/v22/ASSET_REVIEW.md').write_text('\n'.join(md)+'\n')
md=['# 原142项绘图任务与V22对照','', '原清单为118项独立图任务和24项HTML/CSS关系图任务。内联图实现保留，本轮不重新宣告其科学验收，也不因没有V22图片而要求另画。按任务的必需对象/关系判断，资产数、同主题图数均不作为完成数。full可由互补图共同满足；partial保留明确缺项；none仅表示V22无对应图。原有任务ID及要求不变。','', '|原任务ID|科目/小节|V22图码|覆盖|仍需制作/核对|','|---|---|---|---|---|']
for x in coverage:md.append(f"|{x['task_id']}|{x['subject']} {x['section_id']}|{', '.join(x['asset_codes']) or '—'}|{x['v22_coverage']}|{x['remaining_requirements']}|")
(R/'reports/v22/TASK_COVERAGE.md').write_text('\n'.join(md)+'\n')
md=['# 未被V22完整覆盖的原始绘图任务','', '完整可复制的中英文Prompt、Negative Prompt、标签/单位/科学验收原文保存在 [MISSING_TASKS.json](MISSING_TASKS.json)。139条记录包括115项独立图片任务和24项原内联关系图任务，不能写成尚缺139张图片。内联图继续复用现有HTML/CSS，本轮不扩张其科学验收声明。本表逐项保留缺口，不把部分覆盖当作完成。','']
for t in missing:
 md += [f"## {t['id']} · {t['subject']} {t['section_id']} {t['title']}", '',t['task_medium']+'；'+t['legacy_scope'],'',t['v22_remaining_requirements'],'','必须对象：'+ '；'.join(t['must_appear_objects']),'','科学关系：'+ '；'.join(t['correct_scientific_relationships']),'','验收：'+ '；'.join(t['scientific_acceptance_criteria']),'']
(R/'reports/v22/MISSING_TASKS.md').write_text('\n'.join(md).rstrip()+'\n')
stats={'assets':len(A),'by_subject':dict(collections.Counter(a['subject'] for a in A)),'review_status':dict(collections.Counter(a['review_status'] for a in A)),
       'integration_status':dict(collections.Counter(a['integration_status'] for a in A)), 'integrated_unique_images':len(runtime),
       'integrated_subsections':len(set((a['lesson_key'],a['section_id']) for a in runtime)),
       'integrated_chapters':len(set(a['lesson_key'] for a in runtime)),
       'task_coverage':dict(collections.Counter(x['v22_coverage'] for x in coverage)),
       'task_media':dict(collections.Counter(x['task_medium'] for x in coverage)),
       'standalone_image_tasks_not_fully_covered':sum(x['task_medium']=='standalone_image' and x['v22_coverage']!='full' for x in coverage),
       'duplicate_concept_groups':[{'concept':g,'assets':[a['code'] for a in A if a['concept']==g]} for g,n in collections.Counter(a['concept'] for a in A).items() if n>1],
       'legacy_display_replacements':suppressed}
dump(R/'reports/v22/SUMMARY.json',stats);print(json.dumps(stats,ensure_ascii=False,indent=2))
# Keep current implementation anchors accurate while leaving original142 briefs untouched.
for name in ['illustration-manifest.json','illustrations/ILLUSTRATION_MASTER_MANIFEST.json']:
 p=R/name;m=json.loads(p.read_text())
 for row in m['illustrations']:
  if row['record_kind']=='existing_inline_flow':row['reuse']['existing_asset']['sha256']=hashlib.sha256((R/'batch-ui.js').read_bytes()).hexdigest()
 m['uploaded_v22']={'manifest':'reports/v22/ASSET_REVIEW.json','summary':'reports/v22/SUMMARY.json','task_coverage':'reports/v22/TASK_COVERAGE.json','missing_requirements':'reports/v22/MISSING_TASKS.json','original_count':149,'integrated_unique_images':len(runtime),'review_scope':'科学/视觉逐图记录；未将原142任务统一改成完成，原始任务要求保留'}
 dump(p,m)
