/* Verification suite for Note V2 schema (all 16 Chem chapters), KaTeX expressions, SVG diagrams, Knowledge Base bundles, UI cleanup, and runtime hooks. */
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

C('Knowledge Base manifest and book TOC cover all 16 chapters + appendix (complete_16_chapters) and match kb-bundle.js', () => {
  const manifest = JSON.parse(fs.readFileSync(path.join(root, 'data', 'knowledge-base', 'manifest.json'), 'utf8'));
  const book = JSON.parse(fs.readFileSync(path.join(root, 'data', 'knowledge-base', 'books', 'sm1-chemistry-2017.json'), 'utf8'));
  assert.equal(manifest.books.length, 1);
  assert.equal(manifest.books[0].status, 'complete_16_chapters');
  assert.equal(manifest.books[0].chaptersIndexed.length, 16);
  assert.equal(book.toc.length, 17); // Ch 1-16 + 附录
  assert.ok(book.toc.every(c => c.indexed === true));
  assert.ok(book.entries.length >= 60, `Expected >= 60 KB entries across 16 chapters, got ${book.entries.length}`);

  const filesInBooks = fs.readdirSync(path.join(root, 'data', 'knowledge-base', 'books'));
  assert.ok(!filesInBooks.some(f => f.startsWith('_part_')), 'Temporary _part_* files must be cleaned up');

  const ctx = { console, window: {} };
  ctx.window = ctx;
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'vendor', 'knowledge-base', 'kb-bundle.js'), 'utf8'), ctx);
  const bundled = JSON.parse(JSON.stringify(ctx.UEC_KNOWLEDGE_BASE));
  assert.equal(bundled.books.length, 1);
  assert.equal(bundled.tocByBook['sm1-chemistry-2017'].length, 17);
  assert.equal(bundled.entries.length, book.entries.length);
  for (let ch = 1; ch <= 16; ch++) {
    assert.ok((bundled.entriesByLesson[`化学${ch}`] || []).length >= 2, `Missing KB entries for 化学${ch}`);
  }
});

C('All 16 Note V2 Chemistry chapters (chem01..chem16) satisfy complete 8-module schema, L1-L4 practice, and valid SVGs', () => {
  const kbBook = JSON.parse(fs.readFileSync(path.join(root, 'data', 'knowledge-base', 'books', 'sm1-chemistry-2017.json'), 'utf8'));
  const kbIds = new Set(kbBook.entries.map(e => e.id));
  let totalSections = 0;
  let totalPractice = 0;
  const svgPaths = new Set();

  for (let ch = 1; ch <= 16; ch++) {
    const file = path.join(root, 'data', 'notes-v2', `chem${String(ch).padStart(2, '0')}.json`);
    assert.ok(fs.existsSync(file), `Missing ${file}`);
    const data = JSON.parse(fs.readFileSync(file, 'utf8'));
    assert.equal(data.lessonKey, `化学${ch}`);
    assert.equal(data.chapter, ch);
    assert.ok(Array.isArray(data.sections) && data.sections.length >= 2, `chem${ch} sections missing`);

    for (const s of data.sections) {
      totalSections += 1;
      assert.ok(Array.isArray(s.anchor?.goals) && s.anchor.goals.length >= 3, `${data.lessonKey}:${s.id} goals < 3`);
      assert.ok(Array.isArray(s.concepts) && s.concepts.length >= 3, `${data.lessonKey}:${s.id} concepts < 3`);
      assert.ok(Array.isArray(s.formulas) && s.formulas.length >= 2, `${data.lessonKey}:${s.id} formulas < 2`);
      assert.ok(Array.isArray(s.pitfalls) && s.pitfalls.length >= 2, `${data.lessonKey}:${s.id} pitfalls < 2`);
      assert.ok(Array.isArray(s.examples) && s.examples.length >= 2, `${data.lessonKey}:${s.id} examples < 2`);
      assert.ok(Array.isArray(s.practice) && s.practice.length >= 4, `${data.lessonKey}:${s.id} practice < 4`);
      assert.ok(Array.isArray(s.cheatSheet) && s.cheatSheet.length >= 3, `${data.lessonKey}:${s.id} cheatSheet < 3`);
      assert.ok(s.quiz && s.quiz.q && s.quiz.ans, `${data.lessonKey}:${s.id} quiz incomplete`);

      const tiers = new Set(s.practice.map(q => q.tier));
      assert.ok(tiers.has('L1') && tiers.has('L2') && tiers.has('L3') && tiers.has('L4'), `${data.lessonKey}:${s.id} missing L1-L4 spread`);
      for (const q of s.practice) {
        if (q.options) {
          assert.equal(q.options.length, 4, `${q.id} options must be 4`);
          assert.ok(['A', 'B', 'C', 'D'].includes(q.correctOption), `${q.id} invalid correctOption`);
        }
      }
      totalPractice += s.practice.length;

      for (const id of s.kbEntryIds || []) {
        assert.ok(kbIds.has(id), `${data.lessonKey}:${s.id} references unknown kbEntryId "${id}"`);
      }

      for (const d of s.diagrams || []) {
        assert.ok(d.src && d.src.startsWith('assets/fig/v2/'), `${data.lessonKey}:${s.id} invalid diagram path ${d.src}`);
        svgPaths.add(d.src);
      }
    }
  }

  for (const rel of svgPaths) {
    const abs = path.join(root, rel);
    assert.ok(fs.existsSync(abs), `Missing SVG diagram: ${rel}`);
    const svg = fs.readFileSync(abs, 'utf8');
    assert.ok(svg.includes('<svg') && svg.includes('</svg>'), `Malformed SVG: ${rel}`);
  }
  assert.ok(svgPaths.size >= 18, `Expected >= 18 bespoke SVG diagrams, got ${svgPaths.size}`);
  assert.ok(totalPractice >= 240, `Expected >= 240 practice questions across 16 chapters, got ${totalPractice}`);
  console.log(`Schema summary: 16 chapters, ${totalSections} sections, ${totalPractice} practice questions, ${svgPaths.size} SVG diagrams.`);
});

C('Every single TeX expression across all 16 Chem chapters and sm1-chemistry-2017.json passes strict KaTeX rendering', () => {
  let count = 0;
  function checkStr(s) {
    if (typeof s !== 'string') return;
    for (const m of s.matchAll(/\\\(([\s\S]+?)\\\)|\\\[([\s\S]+?)\\\]/g)) {
      const tex = m[1] || m[2];
      katex.renderToString(tex, { throwOnError: true, displayMode: Boolean(m[2]), strict: 'error' });
      count++;
    }
  }
  function walk(v) {
    if (Array.isArray(v)) v.forEach(walk);
    else if (v && typeof v === 'object') {
      if (typeof v.tex === 'string') {
        katex.renderToString(v.tex, { throwOnError: true, displayMode: true, strict: 'error' });
        count++;
      }
      for (const [k, val] of Object.entries(v)) {
        if (k !== 'tex') walk(val);
      }
    } else {
      checkStr(v);
    }
  }
  for (let ch = 1; ch <= 16; ch++) {
    walk(JSON.parse(fs.readFileSync(path.join(root, 'data', 'notes-v2', `chem${String(ch).padStart(2, '0')}.json`), 'utf8')));
  }
  walk(JSON.parse(fs.readFileSync(path.join(root, 'data', 'knowledge-base', 'books', 'sm1-chemistry-2017.json'), 'utf8')));
  assert.ok(count >= 400, `Expected >= 400 KaTeX expressions across all 16 chapters, got ${count}`);
});

C('UI cleanup & runtime integration: redundant tabs removed, math-research-entry placement fixed, Note V2 + KB runtime active', () => {
  const dashSrc = fs.readFileSync(path.join(root, 'ui', 'dashboard.js'), 'utf8');
  assert.ok(!dashSrc.includes("['textbooks','课本资料']"));
  assert.ok(!dashSrc.includes("['plan','原四周计划']"));
  const mathUiSrc = fs.readFileSync(path.join(root, 'ui', 'math-exams.js'), 'utf8');
  assert.ok(!mathUiSrc.includes("document.getElementById('v').prepend(n)"));

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

  for (let ch = 1; ch <= 16; ch++) {
    const key = `化学${ch}`;
    assert.ok(ctx.NOTES_V2[key], `Missing NOTES_V2[${key}]`);
    const html = ctx.renderSection(ctx.LESSONS[key].sections[0], key);
    const v2Mods = html.match(/class="note-module note-module-v2"/g) || [];
    assert.equal(v2Mods.length, 8, `${key} section[0] should render 8 V2 modules`);
  }

  const physHtml = ctx.renderSection(ctx.LESSONS['物理3'].sections[0], '物理3');
  const legacyMods = physHtml.match(/class="note-module"/g) || [];
  assert.equal(legacyMods.length, 12, 'Legacy Phys3 section should still render 12 V1 modules');

  const chemBank = ctx.questionBank().filter(q => q.subject_code === 'chemistry' && q.chapter_id >= 1 && q.chapter_id <= 16);
  assert.ok(chemBank.length >= 240);
  const kbHtml = ctx.KnowledgeBaseUI.view();
  assert.ok(kbHtml.includes('sm1-chemistry-2017'));
});

for (const c of checks) console.log(`PASS: ${c.name}`);
console.log(`ALL ${checks.length} NOTE-V2 & KB CHECKS PASSED.`);
