/* Verification suite for Note V2 schema, KaTeX expressions, Knowledge Base bundles, and runtime hooks. */
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');

const root = process.cwd();
const checks = [];
function C(name, fn) {
  fn();
  checks.push({ name, status: 'pass' });
}

// 1. Load bundled vendor KaTeX inside VM (no node_modules needed)
const katexCtx = { console, window: {}, global: {}, self: {} };
katexCtx.window = katexCtx;
katexCtx.global = katexCtx;
katexCtx.self = katexCtx;
vm.createContext(katexCtx);
vm.runInContext(fs.readFileSync(path.join(root, 'vendor', 'katex', 'katex.min.js'), 'utf8'), katexCtx);
const katex = katexCtx.katex;

C('Knowledge Base manifest and book TOC cover all 16 chapters + appendix and match kb-bundle.js', () => {
  const manifest = JSON.parse(fs.readFileSync(path.join(root, 'data', 'knowledge-base', 'manifest.json'), 'utf8'));
  const book = JSON.parse(fs.readFileSync(path.join(root, 'data', 'knowledge-base', 'books', 'sm1-chemistry-2017.json'), 'utf8'));
  assert.equal(manifest.books.length, 1);
  assert.equal(book.toc.length, 17); // Ch 1-16 + 附录
  assert.ok(book.entries.length >= 15);

  const ctx = { console, window: {} };
  ctx.window = ctx;
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'vendor', 'knowledge-base', 'kb-bundle.js'), 'utf8'), ctx);
  const bundled = JSON.parse(JSON.stringify(ctx.UEC_KNOWLEDGE_BASE));
  assert.equal(bundled.books.length, 1);
  assert.equal(bundled.tocByBook['sm1-chemistry-2017'].length, 17);
  assert.equal(bundled.entries.length, book.entries.length);
  assert.equal(bundled.entriesByLesson['化学3'].length, book.entries.length);
});

C('Note V2 chem03.json has all 6 sections, 8 modules, and 30 L1-L4 verified questions', () => {
  const chem3 = JSON.parse(fs.readFileSync(path.join(root, 'data', 'notes-v2', 'chem03.json'), 'utf8'));
  assert.equal(chem3.lessonKey, '化学3');
  assert.equal(chem3.sections.length, 6);
  let totalPractice = 0;
  for (const s of chem3.sections) {
    assert.ok(s.anchor.goals.length >= 3);
    assert.ok(s.concepts.length >= 3);
    assert.ok(s.formulas.length >= 2);
    assert.ok(s.pitfalls.length >= 2);
    assert.ok(s.examples.length >= 2);
    assert.ok(s.practice.length === 5, `${s.id} should have 5 questions`);
    assert.ok(s.cheatSheet.length >= 3);
    assert.ok(s.kbEntryIds.length >= 1);
    const tiers = new Set(s.practice.map(q => q.tier));
    assert.ok(tiers.has('L1') && tiers.has('L2') && tiers.has('L3') && tiers.has('L4'), `${s.id} missing full L1-L4 tier spread`);
    totalPractice += s.practice.length;
  }
  assert.equal(totalPractice, 30);
});

C('Every single TeX expression in chem03.json and sm1-chemistry-2017.json passes strict KaTeX rendering', () => {
  let count = 0;
  function checkStr(s, loc) {
    if (typeof s !== 'string') return;
    for (const m of s.matchAll(/\\\(([\s\S]+?)\\\)|\\\[([\s\S]+?)\\\]/g)) {
      const tex = m[1] || m[2];
      katex.renderToString(tex, { throwOnError: true, displayMode: Boolean(m[2]), strict: 'error' });
      count++;
    }
  }
  function walk(v, loc) {
    if (Array.isArray(v)) v.forEach((x, i) => walk(x, `${loc}[${i}]`));
    else if (v && typeof v === 'object') {
      if (typeof v.tex === 'string') {
        katex.renderToString(v.tex, { throwOnError: true, displayMode: true, strict: 'error' });
        count++;
      }
      for (const [k, val] of Object.entries(v)) {
        if (k !== 'tex') walk(val, `${loc}.${k}`);
      }
    } else {
      checkStr(v, loc);
    }
  }
  walk(JSON.parse(fs.readFileSync(path.join(root, 'data', 'notes-v2', 'chem03.json'), 'utf8')), 'chem03');
  walk(JSON.parse(fs.readFileSync(path.join(root, 'data', 'knowledge-base', 'books', 'sm1-chemistry-2017.json'), 'utf8')), 'kb');
  assert.ok(count >= 80, `Expected >= 80 KaTeX expressions, got ${count}`);
});

C('Runtime integration: Note V2 renders 8 modules for chem3, 12 modules for legacy phys3, syncs questionBank + KB UI', () => {
  const curriculum = JSON.parse(fs.readFileSync(path.join(root, 'data', 'curriculum.json'), 'utf8'));
  const ctx = {
    console,
    crypto: require('node:crypto').webcrypto,
    localStorage: { getItem: () => null, setItem: () => {}, removeItem: () => {} },
    navigator: {},
    document: {
      hidden: false,
      addEventListener: () => {},
      querySelector: () => null,
      querySelectorAll: () => [],
      getElementById: () => null,
      head: { append: () => {} },
      createElement: () => ({ style: {}, classList: { toggle: () => {} }, append: () => {}, setAttribute: () => {}, querySelector: () => null })
    },
    window: null,
    addEventListener: () => {},
    requestAnimationFrame: cb => cb(),
    S: { mast: {}, learn: {}, rv: {}, done: {}, start: '', err: [], ex: [], checks: {} },
    save: () => true,
    today: () => '2026-11-28',
    days: () => 0,
    esc: s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])),
    D: curriculum.map(c => [c.subject, c.volume, c.chapter, c.title, c.syllabus, c.status, c.priority, c.note]),
    SN: { 物理: '物理', 化学: '化学', 生物: '生物', 数学: '高数' },
    SC: { 物理: '#3b82f6', 化学: '#d97706', 生物: '#16a34a', 数学: '#9333ea' },
    IV: [1, 3, 7, 14, 30],
    IM: { 物理: 'physics', 化学: 'chemistry', 生物: 'biology', 数学: 'math' },
    CAUSE: ['概念不懂', '公式忘', '计算错', '没看清题目'],
    LESSONS: {},
    BATCH_NOTES: {},
    render: () => {},
    vToday: () => '',
    vMap: () => '',
    vErr: () => '',
    vLesson: k => `<section class="card"><h2>${k}</h2></section>` + ctx.LESSONS[k].sections.map(() => '<details open></details>').join(''),
    vCal: () => '',
    ul: a => `<ul>${a.map(x => `<li>${x}</li>`).join('')}</ul>`,
    ol: a => `<ol>${a.map(x => `<li>${x}</li>`).join('')}</ol>`,
    fm: s => String(s)
  };
  ctx.K = d => d[0] + d[2];
  ctx.find = k => ctx.D.find(d => ctx.K(d) === k);
  ctx.ch = (s, c) => ctx.find(s + c);
  ctx.LS = k => ctx.LESSONS?.[k];
  ctx.window = ctx;
  vm.createContext(ctx);

  for (const rel of [
    'data/subjects.js',
    'data/math-courses.js',
    'data/curriculum-scopes.js',
    'lessons/phys03.js',
    'lessons/chem03.js',
    'lessons/batch-notes.js',
    'lessons/batch05-notes.js',
    'lessons/batch06-notes.js',
    'vendor/knowledge-base/kb-bundle.js',
    'vendor/notes-v2/notes-v2-bundle.js',
    'batch-ui.js',
    'ui/icons.js',
    'ui/dashboard-state.js',
    'data/formula-cards.js',
    'ui/study-tools.js',
    'ui/note-v2.js',
    'ui/knowledge-base.js',
    'data/prerequisites.js',
    'ui/learning-engine.js'
  ]) {
    vm.runInContext(fs.readFileSync(path.join(root, rel), 'utf8'), ctx);
  }

  const chemHtml = ctx.renderSection(ctx.LESSONS['化学3'].sections[0], '化学3');
  const v2Mods = chemHtml.match(/class="note-module note-module-v2"/g) || [];
  assert.equal(v2Mods.length, 8, 'Chem3 section should render 8 V2 modules');
  assert.ok(chemHtml.includes('data-tex-inline=') || chemHtml.includes('data-tex='), 'Chem3 V2 note should carry KaTeX attributes');
  assert.ok(chemHtml.includes('tier-L4'), 'Chem3 V2 note should contain L4 tier exercises');

  const physHtml = ctx.renderSection(ctx.LESSONS['物理3'].sections[0], '物理3');
  const legacyMods = physHtml.match(/class="note-module"/g) || [];
  assert.equal(legacyMods.length, 12, 'Legacy Phys3 section should still render 12 V1 modules');

  const bank = ctx.questionBank().filter(q => q.subject_code === 'chemistry' && q.chapter_id === 3);
  assert.equal(bank.length, 30, 'questionBank should expose all 30 V2 Ch3 questions');
  assert.equal(ctx.LearningEngine.pool('chemistry', [3], '', 'sem1_final').length, 30);
  assert.ok(ctx.LearningEngine.pool('chemistry', [], '', 'sem1_final').length >= 30);

  const kbHtml = ctx.KnowledgeBaseUI.view();
  assert.ok(kbHtml.includes('sm1-chemistry-2017'));
  assert.ok(kbHtml.includes('活动探究1'));
});

for (const c of checks) console.log(`PASS: ${c.name}`);
console.log(`ALL ${checks.length} NOTE-V2 & KB CHECKS PASSED.`);
