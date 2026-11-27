/* Verification suite for architecture cleanup, examScopes, multi-subject registry, and backup reminders. */
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

// 1. Archive & deduplication checks
C('33 audit JSON files archived to reports/math-audit and removed from data/math-exams', () => {
  const auditFiles = fs.readdirSync(path.join(root, 'reports', 'math-audit'));
  assert.ok(auditFiles.includes('page-audit.json'));
  const visualReviews = auditFiles.filter(f => f.startsWith('visual-review-') && f.endsWith('.json'));
  assert.equal(visualReviews.length, 32);
  const mathDir = fs.readdirSync(path.join(root, 'data', 'math-exams'));
  assert.equal(mathDir.filter(f => f.endsWith('.js')).length, 0);
  assert.equal(mathDir.filter(f => f.startsWith('visual-review-')).length, 0);
  assert.ok(!mathDir.includes('page-audit.json'));
  assert.ok(mathDir.includes('research-data.json'));
});

C('unified exam-bundles.js matches canonical JSON files across math, phys, chem, bio', () => {
  const ctx = { window: {} };
  ctx.window = ctx;
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'vendor', 'exam-data', 'exam-bundles.js'), 'utf8'), ctx);
  for (const [id, dir] of [['math', 'math-exams'], ['phys', 'phys-exams'], ['chem', 'chem-exams'], ['bio', 'bio-exams']]) {
    const b = JSON.parse(JSON.stringify(ctx.UEC_EXAM_BUNDLES[id]));
    assert.ok(b, `missing bundle ${id}`);
    assert.deepEqual(b.examConfig, JSON.parse(fs.readFileSync(path.join(root, 'data', dir, 'exam-config.json'), 'utf8')));
    assert.deepEqual(b.assemblyProfiles, JSON.parse(fs.readFileSync(path.join(root, 'data', dir, 'assembly-profiles.json'), 'utf8')));
    assert.deepEqual(b.heat, JSON.parse(fs.readFileSync(path.join(root, 'data', dir, 'heat-statistics.json'), 'utf8')));
    assert.deepEqual(b.research, JSON.parse(fs.readFileSync(path.join(root, 'data', dir, 'research-data.json'), 'utf8')));
    assert.deepEqual(b.bank, JSON.parse(fs.readFileSync(path.join(root, 'data', dir, 'original-bank.json'), 'utf8')));
  }
});

C('index.html retains canonical D array and loads new unified scripts cleanly', () => {
  const cp = require('node:child_process');
  const headHtml = cp.execFileSync('git', ['show', 'HEAD:index.html'], { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 });
  const curHtml = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
  assert.equal(curHtml.match(/const D=(\[.*\]);\/\*/)[1], headHtml.match(/const D=(\[.*\]);\/\*/)[1]);
  assert.ok(curHtml.includes('<script src="data/curriculum-scopes.js"></script>'));
  assert.ok(curHtml.includes('<script src="vendor/exam-data/exam-bundles.js"></script><script src="ui/exam-registry.js"></script>'));
  assert.ok(!curHtml.includes('data/math-exams/'));
});

// 2. Curriculum examScopes checks
const curriculum = JSON.parse(fs.readFileSync(path.join(root, 'data', 'curriculum.json'), 'utf8'));
C('curriculum retains 116 chapters and valid examScopes arrays', () => {
  assert.equal(curriculum.length, 116);
  const valid = new Set(['sem1_final', 'pre_exam', 'sem2_final', 'uec']);
  for (const ch of curriculum) {
    assert.ok(Array.isArray(ch.examScopes), `${ch.subject}${ch.chapter} examScopes missing`);
    for (const s of ch.examScopes) assert.ok(valid.has(s), `invalid scope ${s}`);
  }
  const phys18 = curriculum.find(c => c.subject === '物理' && c.chapter === 18);
  assert.deepEqual(phys18.examScopes, ['sem2_final', 'uec']);
  const phys3 = curriculum.find(c => c.subject === '物理' && c.chapter === 3);
  assert.ok(phys3.examScopes.includes('sem1_final'));
  const chem9 = curriculum.find(c => c.subject === '化学' && c.chapter === 9);
  assert.ok(!chem9.examScopes.includes('pre_exam') && chem9.examScopes.includes('uec'));
  const scopeSet = (subj, tag) => curriculum.filter(c => c.subject === subj && c.examScopes.includes(tag)).map(c => c.chapter);
  assert.deepEqual(scopeSet('物理', 'sem1_final'), [3, 4, 5, 6, 7, 8, 11, 21, 22, 23]);
  assert.deepEqual(scopeSet('物理', 'pre_exam'), [3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24]);
  assert.deepEqual(scopeSet('化学', 'sem1_final'), [3, 4, 5, 6, 7, 8, 26, 27, 28, 29, 30]);
  assert.deepEqual(scopeSet('化学', 'pre_exam'), [3, 4, 5, 6, 7, 8, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]);
  assert.deepEqual(scopeSet('生物', 'sem1_final'), [10, 11, 17, 18, 19]);
  assert.equal(scopeSet('生物', 'uec').length, 19);
});

C('science assembly-profiles satisfy exact 2027 Hing Hua paper mark and question structures', () => {
  const phys = JSON.parse(fs.readFileSync(path.join(root, 'data', 'phys-exams', 'assembly-profiles.json'), 'utf8')).profiles;
  for (const p of Object.values(phys)) {
    assert.equal(p.mcq_count, 30);
    assert.equal(p.mcq_marks, 30);
    assert.equal(p.written_marks, 70);
    assert.equal(p.printed_written_marks, 90);
    assert.deepEqual(p.paper_minutes, [70, 120]);
    assert.equal(p.written_sequence.reduce((a, b) => a + b, 0), 90);
  }
  const chem = JSON.parse(fs.readFileSync(path.join(root, 'data', 'chem-exams', 'assembly-profiles.json'), 'utf8')).profiles;
  assert.equal(chem.chem_sem1_final.mcq_count, 25);
  assert.equal(chem.chem_sem1_final.mcq_marks, 50);
  assert.equal(chem.chem_sem1_final.written_marks, 50);
  for (const k of ['chem_preexam', 'chem_sem2_final', 'uec_chemistry']) {
    const p = chem[k];
    assert.equal(p.mcq_count, 30);
    assert.equal(p.mcq_marks, 30);
    assert.equal(p.written_marks, 70);
    assert.equal(p.printed_written_marks, 106);
    assert.equal(p.written_sequence.reduce((a, b) => a + b, 0), 106);
  }
  const bio = JSON.parse(fs.readFileSync(path.join(root, 'data', 'bio-exams', 'assembly-profiles.json'), 'utf8')).profiles;
  for (const p of Object.values(bio)) {
    assert.equal(p.mcq_count, 30);
    assert.equal(p.mcq_marks, 30);
    assert.equal(p.written_marks, 70);
    assert.equal(p.printed_written_marks, 82);
    assert.equal(p.written_sequence.reduce((a, b) => a + b, 0), 82);
  }
});

// 3. Runtime simulation for ExamScopeHelper, ExamRegistry, LearningEngine & StudyApp backup reminders
function createRuntime() {
  const storage = new Map();
  const ctx = {
    console,
    crypto: require('node:crypto').webcrypto,
    localStorage: {
      getItem: k => (storage.has(k) ? storage.get(k) : null),
      setItem: (k, v) => storage.set(k, String(v)),
      removeItem: k => storage.delete(k)
    },
    URL: { createObjectURL: () => 'blob:mock', revokeObjectURL: () => {} },
    navigator: {},
    document: {
      hidden: false,
      addEventListener: () => {},
      querySelector: () => null,
      querySelectorAll: () => [],
      getElementById: () => null,
      createElement: () => ({ style: {}, classList: { toggle: () => {} }, append: () => {}, setAttribute: () => {}, querySelector: () => null })
    },
    window: null,
    addEventListener: () => {},
    scrollTo: () => {},
    setInterval: () => 0,
    requestAnimationFrame: cb => cb(),
    matchMedia: () => ({ matches: false }),
    location: { hash: '', search: '' },
    history: { replaceState: () => {}, pushState: () => {} }
  };
  ctx.window = ctx;
  ctx.D = curriculum.map(c => [c.subject, c.volume, c.chapter, c.title, c.syllabus, c.status, c.priority, c.note]);
  ctx.SN = { 物理: '物理', 化学: '化学', 生物: '生物', 数学: '高数' };
  ctx.SC = { 物理: '#3b82f6', 化学: '#d97706', 生物: '#16a34a', 数学: '#9333ea' };
  ctx.IV = [1, 3, 7, 14, 30];
  ctx.IM = { 物理: 'physics', 化学: 'chemistry', 生物: 'biology', 数学: 'math' };
  ctx.CAUSE = ['概念不懂', '公式忘', '计算错', '没看清题目'];
  ctx.S = { mast: {}, learn: {}, rv: {}, done: {}, start: '', err: [], ex: [{ n: 'UEC 2027 统考', d: '', r: '' }] };
  ctx.save = () => true;
  ctx.today = () => '2026-11-27';
  ctx.iso = t => t.toISOString().slice(0, 10);
  ctx.days = (a, b) => Math.round((new Date(b + 'T00:00') - new Date(a + 'T00:00')) / 864e5);
  ctx.esc = s => String(s);
  ctx.K = d => d[0] + d[2];
  ctx.find = k => ctx.D.find(d => ctx.K(d) === k);
  ctx.ch = (s, c) => ctx.find(s + c);
  ctx.LS = k => ctx.LESSONS?.[k];
  ctx.LESSONS = {};
  ctx.BATCH_NOTES = {};
  ctx.render = () => {};
  ctx.vToday = () => '';
  ctx.vMap = () => '';
  ctx.vErr = () => '';
  ctx.vLesson = () => '';
  ctx.vCal = () => '';
  ctx.renderSection = () => '';
  ctx.ul = () => '';
  ctx.ol = () => '';
  ctx.fm = s => String(s);

  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'data', 'subjects.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'data', 'math-courses.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'data', 'curriculum-scopes.js'), 'utf8'), ctx);
  for (const f of fs.readdirSync(path.join(root, 'lessons')).filter(f => /^(phys|chem|bio|math)\d+\.js$/.test(f))) {
    vm.runInContext(fs.readFileSync(path.join(root, 'lessons', f), 'utf8'), ctx);
  }
  vm.runInContext(fs.readFileSync(path.join(root, 'lessons', 'batch05-notes.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'lessons', 'batch06-notes.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'batch-ui.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'ui', 'dashboard-state.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'data', 'prerequisites.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'ui', 'learning-engine.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'vendor', 'exam-data', 'exam-bundles.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'ui', 'exam-registry.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'ui', 'math-exams-engine.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'ui', 'math-exams-v2-engine.js'), 'utf8'), ctx);
  vm.runInContext(fs.readFileSync(path.join(root, 'ui', 'math-exam-study.js'), 'utf8'), ctx);
  return ctx;
}

const rt = createRuntime();

C('ExamRegistry validates and serves all 4 subjects and placeholder engines honestly refuse empty banks', () => {
  const subs = rt.ExamRegistry.listSubjects();
  assert.deepEqual([...subs.map(s => s.id)], ['math', 'phys', 'chem', 'bio']);
  for (const id of ['math', 'phys', 'chem', 'bio']) {
    const bundle = rt.ExamRegistry.getSubject(id);
    assert.equal(rt.ExamRegistry.validateBundleContract(bundle).ok, true);
  }
  assert.equal(rt.ExamRegistry.getResearchData('math').inventory.length, 47);
  for (const id of ['phys', 'chem', 'bio']) {
    const eng = rt.ExamRegistry.getEngine(id);
    assert.equal(eng.ready, false);
    assert.throws(() => eng.generate({}), /尚未导入/);
  }
});

C('ExamScopeHelper filters LearningEngine.pool and LearningEngine.recommend by selected stage', () => {
  // Physics ch18 is NOT in sem1_final, Physics ch3 IS in sem1_final
  assert.equal(rt.ExamScopeHelper.matchesChapter('physics', 18, 'sem1_final'), false);
  assert.equal(rt.ExamScopeHelper.matchesChapter('physics', 18, 'uec'), true);
  assert.equal(rt.ExamScopeHelper.matchesChapter('physics', 3, 'sem1_final'), true);

  rt.ExamScopeHelper.setCurrentScope('sem1_final');
  const sem1Pool = rt.LearningEngine.pool('physics', [], '');
  assert.ok(sem1Pool.length > 0);
  assert.ok(sem1Pool.every(q => rt.ExamScopeHelper.matchesChapter('physics', q.chapter_id, 'sem1_final')));

  // Add due review for physics ch18 (outside sem1_final) and ch3 (inside sem1_final).
  // Use a recommend date !== today() so wall-clock time of day never shrinks capacity.
  rt.S.learn['物理18'] = '2026-11-19';
  rt.S.learn['物理3'] = '2026-11-19';
  rt.today = () => '2026-11-26';
  const recSem1 = rt.LearningEngine.recommend('2026-11-27', 'sem1_final');
  assert.ok(!recSem1.chosen.some(t => t.course === 'physics' && Number(t.chapter) === 18));
  const recAll = rt.LearningEngine.recommend('2026-11-27', 'all');
  assert.ok(recAll.chosen.some(t => t.course === 'physics' && Number(t.chapter) === 18));
  rt.today = () => '2026-11-27';
  rt.ExamScopeHelper.setCurrentScope('all');
});

C('Backup reminder triggers after >3 days or >20 new errors, resets on export, and respects snooze', () => {
  const fresh = createRuntime();
  const baseNow = new Date('2026-11-27T12:00:00Z').getTime();
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow).needed, false);

  // Trigger by >3 days
  fresh.S.learn['物理3'] = '2026-11-20';
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow).needed, true);
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow).overdueByDays, true);

  // Reset on export
  fresh.StudyApp.markBackupExported(baseNow);
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow).needed, false);
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow + 3 * 86400000).needed, false);
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow + 3 * 86400000 + 1000).overdueByDays, true);

  // Reset and trigger by >20 new errors
  fresh.StudyApp.markBackupExported(baseNow);
  for (let i = 0; i < 20; i++) fresh.StudyApp.recordErrorAdded(baseNow);
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow).overdueByErrors, false);
  fresh.StudyApp.recordErrorAdded(baseNow);
  const status21 = fresh.StudyApp.backupReminderStatus(baseNow);
  assert.equal(status21.overdueByErrors, true);
  assert.equal(status21.needed, true);
  assert.equal(status21.newErrorsSinceExport, 21);

  // Snooze suppresses reminder banner for 24h
  fresh.StudyApp.snoozeBackupReminder(24, baseNow);
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow + 3600000).snoozed, true);
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow + 25 * 3600000).snoozed, false);

  // Export clears errorsAddedSinceExport and snooze
  fresh.StudyApp.markBackupExported(baseNow);
  assert.equal(fresh.StudyApp.backupReminderStatus(baseNow).needed, false);
});

console.log('PASS', checks.length, 'architecture cleanup and generalization assertions');
