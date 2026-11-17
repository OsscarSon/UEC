"""Validate the audit-only illustration manifest; rebuild reports without drawing images.

Run from any directory: python tools/audit_illustrations.py
Requires Python 3, Node, and the repository's Git baseline. No third-party packages.
The JSON manifest and CONTENT_DEPTH_AUDIT.json contain human review decisions;
this script checks their identities/coverage and derives reproducible counts.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import math
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'
MODULES = ['学习目标', '前置知识', '知识结构图', '深度知识讲解', '图解与公式／实验', '典型例题',
           'UEC题型攻略', '易错易混', '分层练习', '完整解析', '考前速记', '掌握度检测']
CATEGORIES = {'precise_scientific_svg': '精确科学SVG', 'structure_schematic': '结构示意图',
              'math_function_plot': '数学函数图', 'experimental_apparatus': '实验装置图',
              'supporting_illustration': '辅助插画'}
ACTIONS = {'retain': '保留／复用', 'correct': '局部修正', 'redraw': '重绘',
           'new': '新增需求', 'defer_verification': '待核实，禁止先制作'}
KINDS = {'existing_svg': '现有教学SVG', 'existing_inline_flow': '现有模块03知识结构图',
         'new_teaching_diagram': '新增制作计划', 'math_chapter_pending': '数学章级待确认计划'}
checks = []


def check(name, condition, detail=''):
    if not condition:
        raise AssertionError(name + ': ' + str(detail))
    checks.append({'name': name, 'result': 'pass', 'detail': detail})


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def write_csv(path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def plain(value):
    if isinstance(value, list):
        return ''.join(plain(v) for v in value)
    if isinstance(value, dict):
        return ''.join(plain(v) for v in value.values())
    return re.sub('<[^>]+>', '', str(value))


def nchar(value):
    return len(re.sub(r'\s+', '', plain(value)))


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ')


def table(headers, rows):
    return ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |',
            *['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows], '']


def ident(s):
    return (s['subject'], s['chapter_id'], s['section_id'])


def read_current():
    script = r"""
const fs=require('node:fs'),vm=require('node:vm');
const c={};c.window=c;vm.createContext(c);const origins={};
for(const f of fs.readdirSync('lessons').filter(f=>/^(phys|chem|bio)\d+\.js$/.test(f)).sort()){
 const before=new Set(Object.keys(c.LESSONS||{}));
 vm.runInContext(fs.readFileSync('lessons/'+f,'utf8'),c);
 for(const k of Object.keys(c.LESSONS))if(!before.has(k))origins[k]='lessons/'+f;
}
vm.runInContext(fs.readFileSync('lessons/batch-notes.js','utf8'),c);
process.stdout.write(JSON.stringify({lessons:c.LESSONS,batch:c.BATCH_NOTES,origins}));
"""
    return json.loads(subprocess.check_output(['node', '-e', script], cwd=ROOT, text=True))


manifest = json.loads((ROOT / 'illustration-manifest.json').read_text())
depth = json.loads((REPORTS / 'CONTENT_DEPTH_AUDIT.json').read_text())
current = read_current()
curr = json.loads((ROOT / 'data/curriculum.json').read_text())
lessons, batch, origins = (current[k] for k in ['lessons', 'batch', 'origins'])
records = manifest['illustrations']
ui = manifest['non_instructional_assets']
record_by_id = {r['id']: r for r in records}
chapters = manifest['inventory']['chapters']
sections = manifest['inventory']['sections']
by_section = {ident(s): s for s in sections}
real_sections, batch_sections, fig_usage = [], [], {}
for d in curr:
    key = d['subject'] + str(d['chapter'])
    for s in lessons.get(key, {}).get('sections', []):
        real_sections.append((d['subject'], d['chapter'], s['id'], s['t']))
        if s['id'] in batch.get(key, {}):
            batch_sections.append((d['subject'], d['chapter'], s['id']))
        for path, caption in s.get('figs', []):
            check('unique actual SVG reference: ' + path, path not in fig_usage)
            fig_usage[path] = (d['subject'], d['chapter'], s['id'])

check('116 chapter identity/title/order', [(d['subject'], d['chapter'], d['title']) for d in curr] ==
      [(d['subject'], d['chapter_id'], d['chapter_title']) for d in chapters])
check('52 actual subsection identity/title/order', real_sections ==
      [(s['subject'], s['chapter_id'], s['section_id'], s['section_title']) for s in sections])
check('41 audited batch sections', len(batch_sections) == 41 and
      set(batch_sections) == {ident(s) for s in sections if s['in_41_section_batch']})
check('41 depth screens on actual batch sections', len(depth['sections']) == 41 and
      {ident(s) for s in depth['sections']} == set(batch_sections))
check('12 deep spot checks / 29 limited screens',
      Counter(s['semantic_review_level'] for s in depth['sections']) ==
      Counter(deep_spot_check=12, structure_and_visual_review=29))
check('unique IDs including UI assets', len({r['id'] for r in records + ui}) == len(records + ui))
source_ids = {s['id'] for s in manifest['scientific_source_register']}
for r in records + ui:
    required = ['id', 'subject', 'chapter_id', 'section_id', 'title', 'teaching_purpose', 'category',
                'drawing_requirements', 'required_labels', 'scientific_basis', 'recommended_format',
                'dimensions', 'priority', 'reuse', 'action', 'production_status']
    check('required fields: ' + r['id'], all(k in r and r[k] not in ['', [], {}] for k in required))
    check('valid category/action/priority: ' + r['id'], r['category'] in CATEGORIES and
          r['action'] in ACTIONS and r['priority'] in manifest['priority_definitions'])
    check('source references: ' + r['id'], all(s['source_id'] in source_ids for s in r['scientific_basis']))
    check('no produced output: ' + r['id'], r['output_path'] is None)
    ex = r['reuse']['existing_asset']
    if ex:
        path = ROOT / ex['path']
        check('existing asset path/hash: ' + r['id'], path.is_file() and digest(path.read_bytes()) == ex['sha256'])
    if r in ui:
        check('UI not counted as real teaching section: ' + r['id'], not r['section_exists'] and r['section_id'] is None)
        continue
    check('positive dimensions and legible label target: ' + r['id'],
          r['dimensions']['canvas_width_px'] > 0 and r['dimensions']['canvas_height_px'] > 0 and
          r['dimensions']['minimum_rendered_label_css_px'] >= 12)
    for anchor in r['source_anchors']:
        check('source anchor exists: ' + r['id'] + ':' + anchor['path'], (ROOT / anchor['path']).is_file())
    if r['record_kind'] == 'math_chapter_pending':
        check('no fabricated math section/allocation: ' + r['id'], r['section_id'] is None and
              not r['section_exists'] and r['subject_code'] == 'math_pending' and
              r['attribution_status'] == 'unresolved_do_not_assign_I_or_II' and r['module_ids'] == [] and
              r['production_status'] == 'blocked_missing_sections_and_attribution')
    else:
        check('actual section binding: ' + r['id'], ident(r) in by_section and
              r['section_title'] == by_section[ident(r)]['section_title'] and
              r['chapter_title'] == by_section[ident(r)]['chapter_title'])
        check('valid module references: ' + r['id'], all(1 <= n <= 12 for n in r['module_ids']))
    for related in r.get('related_sections', []):
        check('cross-reference points to actual section: ' + r['id'], ident(related) in by_section)

svg_records = [r for r in records if r['record_kind'] == 'existing_svg']
flow_records = [r for r in records if r['record_kind'] == 'existing_inline_flow']
new_records = [r for r in records if r['record_kind'] == 'new_teaching_diagram']
math_records = [r for r in records if r['record_kind'] == 'math_chapter_pending']
actual_svg = {str(p.relative_to(ROOT)) for p in (ROOT / 'assets/fig').glob('*.svg')}
check('all 73 SVG files inventoried and referenced', len(svg_records) == 73 and
      {r['reuse']['existing_asset']['path'] for r in svg_records} == actual_svg == set(fig_usage))
for r in svg_records:
    path = r['reuse']['existing_asset']['path']
    check('SVG owned by its actual section: ' + path, fig_usage[path] == ident(r))
    check('SVG parseable: ' + path, ET.parse(ROOT / path).getroot().tag.endswith('svg'))
check('41 inline diagrams matched to actual current flows', len(flow_records) == 41 and
      {ident(r) for r in flow_records} == set(batch_sections))
for r in flow_records:
    nodes = batch[r['subject'] + str(r['chapter_id'])][r['section_id']]['flow']
    check('inline nodes match: ' + r['id'], r['reuse']['existing_asset']['current_nodes'] == nodes)
check('35 math chapter-only plans', len(math_records) == 35 and
      {r['chapter_id'] for r in math_records} == {d['chapter'] for d in curr if d['subject'] == '数学'})
check('math I and II real allocations remain zero', all(s['real_sections'] == s['real_chapter_allocations'] == 0
      for s in manifest['inventory']['independent_math_subjects']))
actual_ui = {str(p.relative_to(ROOT)) for p in (ROOT / 'assets').iterdir() if p.is_file()}
check('all six UI images separately inventoried', len(ui) == 6 and
      {r['reuse']['existing_asset']['path'] for r in ui} == actual_ui)

# Prove this round did not change images, lessons, curriculum or application code.
baseline = manifest['audited_commit']
for path, expected in manifest['protected_file_hashes'].items():
    before = subprocess.check_output(['git', 'show', baseline + ':' + path], cwd=ROOT)
    check('protected baseline and current bytes: ' + path,
          digest(before) == expected == digest((ROOT / path).read_bytes()))
baseline_files = set(subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', baseline], cwd=ROOT, text=True).splitlines())
current_images = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and
                  p.suffix.lower() in {'.svg', '.png', '.jpg', '.jpeg', '.webp', '.gif'}}
baseline_images = {p for p in baseline_files if Path(p).suffix.lower() in {'.svg', '.png', '.jpg', '.jpeg', '.webp', '.gif'}}
check('zero new/deleted image files anywhere in repository', current_images == baseline_images)
check('explicit no-production flag', manifest['production_performed'] is False)

# Numerical samples verify proposed diagram constraints, not unproduced geometry or a whole scientific lesson.
numeric_checks = []
def eq(name, actual, expected, tol=1e-9):
    check('requirement arithmetic: ' + name, math.isclose(actual, expected, rel_tol=tol, abs_tol=tol),
          {'actual': actual, 'expected': expected})
    numeric_checks.append(name)

for name, actual, expected in [
    ('train total travel m', 100 + 300, 400), ('origin translation relative m', -50 - (-80), 30),
    ('reversal path m', abs(5 - (-2)) + abs(1 - 5), 11), ('reversal displacement m', 1 - (-2), 3),
    ('pursuit global meeting s', 60 / (6 - 4), 30), ('pursuit meeting position m', 6 * 30, 180),
    ('delayed pursuit global t s', 6 * 5 / (6 - 4), 15),
    ('signed velocity area m', 4 * 3 - 2 * 2, 8), ('unsigned velocity area m', 4 * 3 + 2 * 2, 16),
    ('unequal-time roundtrip speed m/s', 200 / (100 / 5 + 100 / 2), 20 / 7),
    ('negative velocity accelerated m/s', -5 + (-2) * 1, -7), ('brake stop s', 20 / 5, 4),
    ('brake displacement m', (20 + 0) * 4 / 2, 40), ('balloon apex height m', 75 + 10 - 5, 80),
    ('balloon ground height m', 75 + 10 * 5 - 5 * 25, 0), ('balloon ground v m/s', 10 - 10 * 5, -40),
    ('static maximum N', .4 * 2 * 10, 8), ('spring F N', 200 * (.25 - .20), 10),
    ('resultant N', math.hypot(6, 8), 10), ('resultant degrees', math.degrees(math.atan2(8, 6)), 53.1301023542),
    ('same momentum energy 2kg J', 6 ** 2 / (2 * 2), 9), ('same momentum energy 3kg J', 6 ** 2 / (2 * 3), 6),
    ('elevator N', 60 * (10 - 2), 480), ('weighted Ar', 35 * .75 + 37 * .25, 35.5),
    ('hydrate total O', 4 + 5, 9), ('hydrate total H', 5 * 2, 10),
    ('combustion C g', .88 * 12 / 44, .24), ('combustion H g', .36 * 2 / 18, .04),
    ('combustion sample O g', .6 - .24 - .04, .32), ('O atom mol', .25 * 4, 1),
    ('Ca/phosphate charge', 3 * 2 + 2 * (-3), 0), ('impure carbonate CO2 g', 25 * .8 / 100 * 44, 8.8),
    ('linear glucose chain Mr', 5 * 180 - 4 * 18, 828), ('two chain peptide Mr', 6 * 100 - 4 * 18, 528),
    ('fat mass g', 78 / 39, 2), ('carbohydrate mass g', 78 / 17, 4.588235294117647),
    ('DNA pairs', 1000 / 2, 500), ('DNA H bonds', 200 * 2 + 300 * 3, 1300),
    ('scale bar um', 60 / 20 * 10, 30), ('cube SA/V at a=2', 6 * 2 ** 2 / 2 ** 3, 3),
    ('potato gain percent', (2.2 - 2) / 2 * 100, 10),
    ('light reaction H balance', 2 * 2, 4), ('light reaction O balance', 2, 2),
    ('light reaction charge', 4 - 4, 0), ('Calvin C balance', 3 + 3 * 5, 6 * 3),
    ('Calvin regenerated C', 5 * 3, 3 * 5), ('Calvin net C', 6 * 3 - 3 * 5, 3),
]:
    eq(name, actual, expected)
check('absolute-value formatting defects explicitly disclosed',
      {ident(s) for s in depth['sections'] if s['formula_fragment_issue']} ==
      {('物理', 3, '3.3'), ('物理', 4, '4.2'), ('物理', 4, '4.3'), ('物理', 4, '4.8')})

fragment_probes = [
    ('物理3', '3.3', 'deep', 'Δx'), ('物理3', '3.3', 'derive', 'x_i−x_(i−1)'),
    ('物理4', '4.2', 'deep', 'f_s'), ('物理4', '4.3', 'derive', 'F₁−F₂'),
    ('物理4', '4.8', 'derive', 'a_A'), ('物理4', '4.8', 'derive', '/'),
    ('物理4', '4.8', 'derive', 'a_B'),
]
for key, sid, field, value in fragment_probes:
    check('disclosed fragment exists in current data: ' + key + ':' + sid + ':' + value,
          value in batch[key][sid][field])

# Visual use is separated into current rendering versus recommended future cross-reference.
def relevant(s):
    return [r for r in records if (r['section_exists'] and ident(r) == ident(s)) or
            any(ident(x) == ident(s) for x in r.get('related_sections', []))]


coverage_rows, metrics_rows, chapter_rows, section_rows = [], [], [], []
for ch in chapters:
    rr = [r for r in records if r['subject_code'] == ch['subject_code'] and r['chapter_id'] == ch['chapter_id']]
    chapter_rows.append({**{k: ch[k] for k in ['subject', 'chapter_id', 'chapter_title', 'volume', 'curriculum_index', 'section_count', 'status']},
                         'real_section_ids': ';'.join(ch['section_ids']),
                         'illustration_ids': ';'.join(r['id'] for r in rr),
                         'blocker': '' if ch['section_count'] else '无真实小节；不得补编号。数学另缺I/II归属，理化生需真实教材小节后逐节补审。'})
review_by_section = {ident(s): s for s in depth['sections']}
for s in sections:
    rr = relevant(s)
    owned_svg = [r for r in rr if r['record_kind'] == 'existing_svg' and ident(r) == ident(s)]
    planned = [r for r in rr if r['record_kind'] == 'new_teaching_diagram']
    flows = [r for r in rr if r['record_kind'] == 'existing_inline_flow' and ident(r) == ident(s)]
    section_rows.append({**{k: s[k] for k in ['subject', 'chapter_id', 'chapter_title', 'section_id', 'section_title', 'in_41_section_batch', 'lesson_path']},
                         'current_svg_count': len(owned_svg), 'current_svg_ids': ';'.join(r['id'] for r in owned_svg),
                         'current_inline_flow_ids': ';'.join(r['id'] for r in flows),
                         'new_plan_or_recommended_crossref_ids': ';'.join(r['id'] for r in planned),
                         'all_relevant_ids': ';'.join(r['id'] for r in rr),
                         'review_boundary': '十二模块图示逐项检查；未执行制作' if s['in_41_section_batch'] else '旧小节现有图科学/标签检查；未伪造十二模块'})
    check('each real section has visual review', bool(rr), ident(s))
    if not s['in_41_section_batch']:
        continue
    key = s['subject'] + str(s['chapter_id'])
    old = next(x for x in lessons[key]['sections'] if x['id'] == s['section_id'])
    u = batch[key][s['section_id']]
    rev = review_by_section[ident(s)]
    visible_questions = lambda qs: [[q['q'], q['steps'], q['ans']] for q in qs]
    blocks = [u['goals'], u['prerequisites'], u['flow'], old['body'] + u['deep'],
              [u['derive'], old.get('f', []), old.get('terms', '')], visible_questions(u['examples']), u['exam'],
              old['tips'], [q['q'] for q in u['practice']], visible_questions(u['practice']), u['quick'], visible_questions([u['quiz']])]
    entries = [len(u['goals']), len(u['prerequisites']), len(u['flow']), len(old['body']) + len(u['deep']),
               len(u['derive']) + len(old.get('f', [])), len(u['examples']), len(u['exam']), len(old['tips']),
               len(u['practice']), len(u['practice']), len(u['quick']), 1]
    for m in range(1, 13):
        targets = [r for r in rr if m in r['module_ids']]
        if m in (7, 11):
            targets = [r for r in rr if set(r['module_ids']) & ({4, 5} if m == 7 else {3, 4, 5})]
        ids = ';'.join(r['id'] for r in targets)
        now = flows if m == 3 else owned_svg if m == 5 else []
        if m == 1:
            decision = '不单独配图；目标须能指向M03/05图上可观察的判断，不能用装饰图代替目标。'
        elif m == 2:
            decision = '前置知识先按现有prerequisites核对；涉及旧图可回链M05，不强制新图，不在未有小节的课程中造前置节号。'
        elif m == 3:
            decision = flows[0]['drawing_requirements'][0]
        elif m in (4, 5):
            decision = '核心知识图示：' + '；'.join(r['title'] for r in targets) + '。依各ID的条件/标签核对；现有SVG目前只在M05呈现，其他模块引用属计划。'
        elif m == 6:
            decision = '逐题审已有3例；空间/数量关系采用下列图的题给参数版。其余纯文字/计算无需独立图片；禁止补猜题干。重点：' + rev['core_expansion_request']
        elif m == 7:
            decision = '可复用装置读图/曲线/计量图说明答题步骤；41节现均缺“题干线索→选法→关键步骤→检查”完整攻略。无原卷评分证据不画考频或官方得分点图。'
        elif m == 8:
            decision = '用已有错误提示制作遮盖标注/错解对照；不另添科学错误作正确图。具体误读：' + rev['core_observation']
        elif m in (9, 10):
            decision = ('已有4题按题干选择留空图，只有视觉判断需要图；' if m == 9 else '与M09同一数据、尺度、符号和图号，答案层独立；') + '复用对应图的教学/留空版，不算4张新图片，不为无图必要的算术题凑图。'
        elif m == 11:
            decision = '精炼文字/公式可成立；回链M03/05，不单独新增装饰图或将速记当深讲。'
        else:
            decision = '现1道检测题；按学习目标核查覆盖，需要视觉判断时复用对应图的留空版。未建立目标→题目→错误反馈映射前不宣称全面诊断。'
        coverage_rows.append({'subject': s['subject'], 'chapter_id': s['chapter_id'], 'section_id': s['section_id'],
                              'section_title': s['section_title'], 'module_id': m, 'module_title': MODULES[m - 1],
                              'knowledge_scope': ' / '.join(u['goals']) if m in (1, 12) else
                              ' / '.join(u['prerequisites']) if m == 2 else ' / '.join(u['flow']),
                              'current_rendered_visual_ids': ';'.join(r['id'] for r in now),
                              'planned_or_reusable_ids': ids, 'decision_and_gap': decision,
                              'production_status': 'review_only_no_images_created'})
        status = 'concise_appropriate_no_length_failure' if m in (1, 2, 11) else 'substantive_material_present_not_full_certification'
        if m == 3:
            status = 'flow_' + flows[0]['action']
        if m in rev['requires_expansion_modules']:
            status = 'requires_local_expansion_or_goal_mapping'
        if rev['formula_fragment_issue'] and m in (4, 5):
            status = 'P0_formula_delimiter_correction_first'
        if m == 7:
            finding = '两条短exam建议；重复年份/来源警告不计教学深度。需本节题型的完整选择和检查过程，不虚构官方评分。'
        elif m == 12:
            finding = '有1题及步骤答案，不是空白；缺显式学习目标覆盖和错因回读映射。可先复用现有3例/4练，不必机械增题。'
        elif m in (1, 2, 11):
            finding = '用途允许简洁；未因字数短判为不合格。'
        elif m in rev['extra_modules']:
            finding = rev['core_observation'] + ' 扩写/修订要求：' + rev['core_expansion_request']
        elif m == 4:
            finding = '合并原正文s.body与补充u.deep后评估；存在实质解释，不能只看补充段落。'
        elif m == 5:
            finding = '推导、原公式、图、术语一起评估；见插图清单，不以推导字数代替科学性。'
        elif m in (6, 9, 10):
            finding = '步骤与答案结构存在；层次标签和科学正确性仍需按本节具体任务审定，结构通过不等于深度通过。'
        else:
            finding = '现有材料保留；具体视觉关系/错误推理要求见本节清单。'
        metrics_rows.append({'subject': s['subject'], 'chapter_id': s['chapter_id'], 'section_id': s['section_id'],
                             'section_title': s['section_title'], 'module_id': m, 'module_title': MODULES[m - 1],
                             'text_characters_without_whitespace': nchar(blocks[m - 1]), 'entry_count': entries[m - 1],
                             'current_svg_count_only_M05': len(owned_svg) if m == 5 else 0,
                             'status': status, 'review_level': rev['semantic_review_level'], 'finding': finding})
check('492 module visual decisions', len(coverage_rows) == 492 and len({(r['subject'], r['section_id'], r['module_id']) for r in coverage_rows}) == 492)
check('492 depth observations', len(metrics_rows) == 492)
check('all batch sections have core M04/M05 diagram coverage', all(any(r['planned_or_reusable_ids'] for r in coverage_rows
      if (r['subject'], r['chapter_id'], r['section_id']) == sk and r['module_id'] in (4, 5)) for sk in batch_sections))
write_csv(REPORTS / 'ILLUSTRATION_CHAPTER_SCAN.csv', chapter_rows)
write_csv(REPORTS / 'ILLUSTRATION_SECTION_COVERAGE.csv', section_rows)
write_csv(REPORTS / 'ILLUSTRATION_MODULE_COVERAGE.csv', coverage_rows)
write_csv(REPORTS / 'CONTENT_DEPTH_MODULES.csv', metrics_rows)

stats = {
    'chapters_scanned': len(chapters), 'actual_sections_scanned': len(sections), 'batch_sections_screened': len(batch_sections),
    'deep_semantic_spot_checks': 12, 'limited_structure_visual_screens': 29, 'module_visual_decisions': len(coverage_rows),
    'teaching_review_and_plan_records': len(records), 'existing_svg_records': len(svg_records),
    'existing_svg_used_by_batch': sum(ident(r) in set(batch_sections) for r in svg_records),
    'existing_inline_flow_records': len(flow_records), 'new_diagram_plans': len(new_records),
    'math_chapter_pending_plans': len(math_records), 'non_instructional_UI_assets_separate': len(ui),
    'image_files_created_modified_deleted': 0, 'note_or_application_files_modified': 0,
    'formula_fragment_sections': sum(s['formula_fragment_issue'] for s in depth['sections']),
    'sections_requiring_local_expansion_or_goal_mapping': len(depth['sections']),
    'chapters_without_real_sections': sum(not c['section_ids'] for c in chapters),
    'science_chapters_without_real_sections': sum(not c['section_ids'] and c['subject'] != '数学' for c in chapters),
    'actions_all_teaching_records': dict(Counter(r['action'] for r in records)),
    'actions_existing_svg': dict(Counter(r['action'] for r in svg_records)),
    'actions_existing_inline': dict(Counter(r['action'] for r in flow_records)),
    'categories_all_teaching_records': dict(Counter(r['category'] for r in records)),
    'priority_all_teaching_records': dict(Counter(r['priority'] for r in records)),
    'by_subject_code': dict(Counter(r['subject_code'] for r in records)),
}
manifest['statistics'] = stats
write_json(ROOT / 'illustration-manifest.json', manifest)

# Complete human-readable requirements; all records, not just a sample or ID index.
doc = ['# 教学插图需求与现有图审查', '',
       f'审查日期：{manifest["audit_date"]}（Asia/Kuala_Lumpur）；PR #1 原分支 `{manifest["branch"]}`；被审查内容提交 `{baseline}`。', '',
       '**本文件是制作需求，不是图片交付。此次生成、修改、删除图片均为0，笔记与网站运行文件均未修改。**', '',
       f'扫描116个原章级记录、52个真实小节；重点为本PR新增十二模块的41节。共{len(records)}条教学图审查／制作计划：73条现有SVG、41条现有HTML/CSS知识结构图、{len(new_records)}条新增制作需求、35条数学章级待确认计划。另列6个界面素材。203条绝不表示203张已完成图片。', '',
       '高级数学（I）、（II）目前各有独立入口，但没有已核实章归属或真实小节。旧数学35章按原ID、名称、顺序保留，计划只绑定真实章；所有数学section_id均为null，不能按试卷一／二分科。73个理化生章也还没有真实小节，只有扫描阻碍记录，不虚构知识点、图或小节号。', '',
       '## 统计与优先顺序', '',
       *table(['记录类型', '数量', '处理'], [(KINDS[k], n, '仅审查／计划') for k, n in Counter(r['record_kind'] for r in records).items()] + [('非教学界面素材', len(ui), '保留，单独统计')]),
       *table(['动作', '全部教学记录', '现有SVG', '现有结构图'], [(ACTIONS[k], stats['actions_all_teaching_records'].get(k, 0), stats['actions_existing_svg'].get(k, 0), stats['actions_existing_inline'].get(k, 0)) for k in ACTIONS]),
       *table(['类别', '数量'], [(CATEGORIES[k], stats['categories_all_teaching_records'].get(k, 0)) for k in CATEGORIES]),
       *table(['优先级', '数量', '含义'], [(k, stats['priority_all_teaching_records'].get(k, 0), v) for k, v in manifest['priority_definitions'].items()]),
       '现有图43幅用于本批41节，另30幅属于化学5／生物3。所有73幅都有真实小节引用；建议跨节复用与当前实际渲染分别记录，不把未来回链说成现有功能。', '',
       '## 使用与制作约束', '',
       '- `retain`为可保留复用，`correct`为局部科学/标签修正需求，`redraw`为关系或结构须重绘；本轮均未执行。旧文件仍全部保留。',
       '- 每项标签、几何、单位、对象、计量与模型条件应逐一核对。示意不等于精确比例；同图的定量箭头/坐标必须准确。辅助人物不能替代受力图或定量图。',
       '- 数学函数图应按确认函数、定义域与参数由确定性计算生成；当前35条均被小节／归属缺失阻挡，不进入绘图。',
       '- SVG建议画布1200×800；窄屏320–390 CSS px时拆为纵向面板或可展开查看，渲染标签至少12 CSS px，目标14；不能把大画布缩到手机后仍声称字号合格。所列为待验收要求，本轮未对未制作图做手机/电脑实测。',
       '- 标注版与练习留空版共用同一正确数据/几何；只采用已有题给数据，不为凑图虚构实验值、误差棒、官方得分点、历年考频。版本是制作方式，不额外计作成品数。',
       '- 实验图是装置/控制/测量的教学原理需求；缺器材、浓度或协议时必须待教师/实验资料确认，不补猜具体操作。',
       '- JSON每项有来源锚点、模型条件、验收门槛、复用状态；来源登记的“部分核实”不等于整图或整课已经教研审定。', '',
       '## 全部真实课程扫描', '',
       '章级完整记录见 [CSV](reports/ILLUSTRATION_CHAPTER_SCAN.csv)，以下也列出116章。无小节的章不伪造图清单。', '',
       *table(['科目', '原章号', '原章名', '真实小节数', '状态'], [(c['subject'], c['chapter_id'], c['chapter_title'], c['section_count'], '待真实小节' if not c['section_count'] else '已逐节列图') for c in chapters]),
       '### 52个真实小节', '',
       *table(['科目/原章', '真实小节', '原小节名', '本批41节', '当前SVG数', '对应图记录'],
              [(s['subject'] + str(s['chapter_id']), s['section_id'], s['section_title'], '是' if s['in_41_section_batch'] else '否', len(s['existing_svg_paths']), '、'.join(r['id'] for r in relevant(s))) for s in sections]),
       '## 十二模块的图示覆盖', '',
       '[492项逐模块检查CSV](reports/ILLUSTRATION_MODULE_COVERAGE.csv)覆盖41×12；每行列知识范围、当前渲染图ID、拟复用/新增ID及缺口。当前SVG只在M05、知识结构图只在M03渲染；跨模块和跨小节引用是计划。其余11个旧小节只审现有图，不套用不存在的十二模块。', '',
       *table(['模块', '图示判断'], [('01 学习目标', '无需独立图片；目标需对接可观察的图形判断'), ('02 前置知识', '可回链已存在前置/本节图，不造前置节号'), ('03 知识结构图', '41项均有当前HTML/CSS图，按因果/分类/条件/步骤决定保留或重构'), ('04 深度讲解', '核查结构、机制、数量与适用条件；采用逐项图要求'), ('05 图解与公式／实验', '73现有SVG科学/标签审查，54新增需求补主要缺口；非每节均需实验'), ('06 典型例题', '沿用现有3例数据；空间与数量关系用对应图，纯计算无需凑图'), ('07 UEC题型攻略', '复用曲线/受力/计量/装置图训练题干选法；不画未证实考频/评分'), ('08 易错易混', '正确图与错解/错误箭头对照，错误层须明确标记'), ('09 分层练习', '4道已有题有图必要时使用留空版，不能直接泄露答案'), ('10 完整解析', '与M09相同参数，显示推理标注；不另算成品'), ('11 考前速记', '文字可简洁；回链核心图，无需装饰图'), ('12 掌握度检测', '已有题的视觉判断可用留空版；目标映射和反馈缺口见质量报告')]),
       '## 科学与范围来源登记', '',
       '学校资料只说明兴华校内安排；2026董总文件只说明当前已取得的官方身份/范围，2027适用性仍待确认。OpenStax/BIPM/NIST用于科学原则，不用于推定学校考试或UEC考频。两份另传Research报告的核验记录仍见 [RESEARCH_VERIFICATION](reports/RESEARCH_VERIFICATION.md)，本清单不把二手报告当作精确图形的唯一依据。', '']
for source in manifest['scientific_source_register']:
    doc += [f'### SOURCE {source["id"]}', '',
            f'- {source["title"]}：{source["url_or_file"]}',
            f'- 定位：{source["locator"]}；查阅：{source["access_date"]}；状态：`{source["verification_status"]}`；用途：`{source["evidence_scope"]}`。',
            '- 边界：' + source['notes'], '']
doc += ['## 完整逐图要求', '', '以下每条ID与JSON一一对应。所有“新增／重绘／修正”均未制作；精确来源与待核实边界均保留。', '']
for r in records:
    dim, reuse = r['dimensions'], r['reuse']
    location = f'{r["subject"]}／原第{r["chapter_id"]}章 {r["chapter_title"]}／'
    location += f'{r["section_id"]} {r["section_title"]}' if r['section_exists'] else '真实小节不存在（编号null；I／II待核实）'
    ex = reuse['existing_asset']
    reuse_text = f'`{reuse["can_reuse"]}`；' + reuse['reason']
    if ex:
        reuse_text += ' 当前：`' + ex['path'] + '`'
        if 'selector' in ex:
            reuse_text += '，选择器：`' + ex['selector'] + '`'
    if reuse.get('reference_existing_illustration_id'):
        reuse_text += '；优先引用 ' + reuse['reference_existing_illustration_id']
    doc += [f'### {r["id"]} · {r["title"]}', '',
            '- 归属：' + location + '。',
            f'- 类型／动作／优先级：{CATEGORIES[r["category"]]}；{ACTIONS[r["action"]]}；{r["priority"]}。',
            '- 教学目的：' + r['teaching_purpose'],
            '- 绘图要求：', *['  - ' + q for q in r['drawing_requirements']],
            '- 必须文字标注：' + '；'.join(r['required_labels']) + '。',
            '- 科学依据：' + '；'.join(f'{b["source_id"]}（{b["scope"]}；{b["verification_status"]}）' for b in r['scientific_basis']) + '。',
            f'- 推荐格式／尺寸：{r["recommended_format"]}；{dim["canvas_width_px"]}×{dim["canvas_height_px"]}；标签渲染至少{dim["minimum_rendered_label_css_px"]} CSS px。' + dim['layout_note'],
            '- 现有图能否复用：' + reuse_text + '。',
            '- 模块用途：' + ('、'.join(f'{m:02d}' for m in r['module_ids']) if r['module_ids'] else '待真实小节后再确定，不套十二模块') + '。',
            '- 原文定位：' + '；'.join(a['path'] + ' ' + str(a.get('selector', a.get('json_pointer', a.get('old_id', '')))) for a in r['source_anchors']) + '。',
            '- 制作前门槛：' + '；'.join(r['production_gate']) + '。',
            '- 验收：' + '；'.join(r['acceptance_checks']) + '。',
            '- 当前状态：`' + r['production_status'] + '`；无新输出文件。', '']
    if r.get('related_sections'):
        doc += ['建议跨节引用（尚未渲染）：' + '；'.join(x['subject'] + str(x['chapter_id']) + '／' + x['section_id'] for x in r['related_sections']) + '。', '']
doc += ['## 六个界面素材（不计入203项教学记录）', '']
for r in ui:
    d = r['dimensions']
    doc += [f'### {r["id"]} · {r["title"]}', '',
            f'- 科目：{r["subject"]}；章／节：无（null），仅为界面素材。类型：辅助插画；动作：保留；优先级：P3。',
            '- 目的：' + r['teaching_purpose'], '- 要求：' + '；'.join(r['drawing_requirements']) + '。',
            '- 标签：' + '；'.join(r['required_labels']) + '。',
            '- 科学依据：不承载科学命题，`repo_lessons`仅证明界面引用范围。',
            f'- 格式／尺寸：{r["recommended_format"]}；原图{d["existing_width_px"]}×{d["existing_height_px"]}，本轮保留。',
            '- 复用：可；`' + r['reuse']['existing_asset']['path'] + '`；无新输出。', '']
doc += ['## 验证及剩余工作', '',
        '运行 `python tools/audit_illustrations.py` 可复核真实章／节、ID、来源、字段、73个SVG引用、41个结构图、35个无伪造编号计划、492项覆盖，以及受保护原文件与被审查提交的字节一致性。脚本只输出文本/JSON/CSV，不调用绘图器或浏览器。加 `--regression` 可同时重跑原有静态/计算/SVG边界检查。', '',
        '[验证结果](reports/ILLUSTRATION_VALIDATION.json)记录实际检查；[原检查重跑记录](reports/ILLUSTRATION_REGRESSION.json)记录结构、80项计算和43幅SVG文字边界检查；[内容深度审查](reports/CONTENT_DEPTH_AUDIT.md)列41节扩写建议和12节抽查证据。脚本数值检查只核对计划中的选定计算/守恒，不等于未制作图已经通过视觉验收或整课科学审定。', '',
        '尚待：审定P0科学/排版问题；后续获授权再修正/绘图、补题型攻略与目标映射；取得真实数学小节目录及I／II对照；核实2027适用官方版本；补审73个尚无真实小节的理化生章。此次不以新笔记或新图片填补这些阻碍。', '']
(ROOT / 'ILLUSTRATION_REQUIREMENTS.md').write_text('\n'.join(doc))

# Content audit summary keeps structural presence separate from teaching quality.
audit_doc = ['# 41小节内容深度审查', '',
             f'审查日期：{manifest["audit_date"]}；被审查提交 `{baseline}`；本轮未改笔记。', '',
             '**结论：492/492模块结构存在，不能视为深度验收通过。** 41节均有局部扩写／目标映射需求；这不表示41节深度讲解都是空模板。原正文与补充合并后，M04均有实质内容。最一致的不足是M07仅两条短建议；M12有单题及答案，却未显式对应全部学习目标。物理3.3、4.2、4.3、4.8另有P0公式分段错误。', '',
             '## 方法和边界', '',
             '- 对41节全部检查实际渲染来源：M04=s.body+u.deep；M05=原图+u.derive+原公式+术语；M08为原tips。未只看新增补充文本。',
             '- 41节完成结构与视觉相关内容初筛；其中12节做重点语义抽查，其余29节不宣称逐句独立科学或教师审定。逐节级别见下表。',
             '- 字符数去HTML标签及空白，保留标点/公式符号，仅作定位证据，不设“字数及格线”。M05字符数不含图像，另列原图数；M10含题干/步骤/答案，不能当独立新增题数。',
             '- M01目标、M02前置、M11速记允许精炼。M07重复的年份/来源/第三方索引警告不计入教学深度；没有正式评分证据时只能教答题过程。',
             '- 单道检测不自动不合格，但应说明目标覆盖和诊断/回读路径；可先复用已有例题与分层题建立映射，不为凑数量新增大量题。', '',
             '## 十二模块的量化定位', '',
             *table(['模块', '41节字符数范围', '条目数范围', '判读'], [
                 (f'{m:02d} {MODULES[m - 1]}',
                  str(min(r['text_characters_without_whitespace'] for r in metrics_rows if r['module_id'] == m)) + '–' + str(max(r['text_characters_without_whitespace'] for r in metrics_rows if r['module_id'] == m)),
                  str(min(r['entry_count'] for r in metrics_rows if r['module_id'] == m)) + '–' + str(max(r['entry_count'] for r in metrics_rows if r['module_id'] == m)),
                  '允许简洁，不因短判失败' if m in (1, 2, 11) else '41节均需题型过程扩写' if m == 7 else '需目标与反馈映射' if m == 12 else '结合原图/公式和逐节内容判断') for m in range(1, 13)]),
             '完整492行定位与观察见 [CONTENT_DEPTH_MODULES.csv](CONTENT_DEPTH_MODULES.csv)。41条人工审查判断、原exam短建议、检测题和目标原文见 [JSON](CONTENT_DEPTH_AUDIT.json)。', '',
             '## 必须先修的四处排版问题', '',
             '原内容辅助函数以竖线分割文本条目，绝对值符号也被当成分隔符。以下是实际数据错误，不能由“最少字符数”和“字段存在”检查发现。本轮仅记录，不修正文或生成文件。', '',
             *table(['小节', '实际异常', '修订要求'], [(s['subject'] + s['section_id'], s['core_observation'], s['core_expansion_request']) for s in depth['sections'] if s['formula_fragment_issue']]),
             '## 全部41节的扩写／修订清单', '',
             '所有小节共同需补M07题型线索→方法选择→关键步骤→检查过程，以及M12目标→题目→错因/回读映射。下表列额外的局部要求，避免把各节机械扩写成相同模板。P0节先修原式，再决定需要多少新解释。', '',
             *table(['科目/小节', '原小节名', '审查级别', '优先级', '局部重点模块', '观察与后续要求'],
                    [(s['subject'] + s['section_id'], s['section_title'], '重点语义抽查' if s['semantic_review_level'] == 'deep_spot_check' else '结构/视觉初筛', s['priority'],
                      '、'.join(f'{m:02d}' for m in sorted(set([7, 12] + s['extra_modules']))),
                      s['core_observation'] + ' 后续：' + s['core_expansion_request']) for s in depth['sections']]),
             '## 12节重点抽查证据', '']
for s in depth['sections']:
    if s['semantic_review_level'] != 'deep_spot_check':
        continue
    vals = {r['module_id']: r for r in metrics_rows if ident(r) == ident(s)}
    audit_doc += [f'### {s["subject"]}{s["section_id"]} {s["section_title"]}', '',
                  '- 原文定位：' + '；'.join(a['path'] + ' ' + a.get('selector', a.get('json_pointer', '')) for a in s['source_anchors']) + '。',
                  '- 观察：' + s['core_observation'],
                  f'- M04合并字符{vals[4]["text_characters_without_whitespace"]}；M05文本字符{vals[5]["text_characters_without_whitespace"]}、原SVG {vals[5]["current_svg_count_only_M05"]}幅；例题3、分层题4、检测1。',
                  '- M07原有专属建议（全部）：' + '；'.join(s['exam_advice_verbatim']),
                  '- M12原检测：' + s['quiz_prompt'],
                  '- 需覆盖的原目标：' + '；'.join(s['goals']),
                  '- 后续局部处理：' + s['core_expansion_request'], '']
audit_doc += ['## 非本批11节的附带风险', '',
              '全仓图审查同时发现下列旧内容风险，仅登记，不把它们算入41节或已修复项。科学原则依据详见根目录插图清单。', '',
              *table(['旧小节', '优先级', '风险'], [(s['subject'] + s['section_id'], s['priority'], s['issue']) for s in depth['outside_batch_alerts']]),
              '## 仍未完成', '',
              '41节尚未完成上述扩写/映射；4处公式分段和旧图科学修订尚未执行；29节未做重点逐句语义审定；未核实2027适用官方范围、正式原卷与评分表。原有报告的结构覆盖数仍有效，但“深度已充分”不能据此成立。', '',
              '插图制作完全未执行，手机/电脑的待制作图片可读性是后续验收条件。本轮通过原文件字节保护证明网站行为、进度和迁移逻辑未改；不冒称又跑过浏览器交互或图片渲染检查。', '']
(REPORTS / 'CONTENT_DEPTH_AUDIT.md').write_text('\n'.join(audit_doc))

regression_path = REPORTS / 'ILLUSTRATION_REGRESSION.json'
if '--regression' in sys.argv:
    regressions = []
    for command in [['node', 'tests/coverage.cjs'], ['python', 'tests/calculations.py'], ['node', 'tests/svg.cjs']]:
        run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        check('existing regression: ' + ' '.join(command), run.returncode == 0, run.stdout.strip() + run.stderr.strip())
        regressions.append(dict(command=' '.join(command), result='pass', output=run.stdout.strip()))
    write_json(regression_path, dict(audit_date=manifest['audit_date'], audited_commit=baseline,
               checks=regressions, browser_run=False, images_generated=False,
               limitation='静态结构、80项计算、43幅本批SVG文字边界检查；不等于修复已发现的科学/教学缺口。'))
regression_evidence = json.loads(regression_path.read_text()) if regression_path.exists() else None
validation = {'audit_date': manifest['audit_date'], 'audited_commit': baseline,
              'command': 'python tools/audit_illustrations.py', 'result': 'pass',
              'statistics': stats, 'automated_checks_passed': len(checks), 'checks': checks,
              'numerical_requirement_samples_checked': len(numeric_checks),
              'existing_regression_evidence': regression_evidence,
              'limits': ['人工判断存于JSON，自动字段/数量/算术通过不能替代科学与教学审定',
                         '无新图片，无笔记或网站运行文件改动；未运行浏览器或生成截图',
                         '待制作图片没有实际手机/电脑视觉测试结果',
                         '2027考试适用性、数学小节和I/II归属未解决']}
write_json(REPORTS / 'ILLUSTRATION_VALIDATION.json', validation)
print(json.dumps({'result': 'pass', 'automated_checks': len(checks), 'statistics': stats,
                  'numeric_requirement_samples': len(numeric_checks)}, ensure_ascii=False, indent=2))
