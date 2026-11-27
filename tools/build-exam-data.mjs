/* Build unified browser exam bundles and curriculum exam-scope helpers from canonical JSON files. */
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const curriculumPath = path.join(root, 'data', 'curriculum.json');
const curriculum = JSON.parse(fs.readFileSync(curriculumPath, 'utf8'));

const stageOptions = [
  ['all', '全部阶段（不限）'],
  ['sem1_final', '第一学期期末考'],
  ['pre_exam', '校内预试'],
  ['sem2_final', '毕业考 / 第二学期期末'],
  ['uec', 'UEC 正式统考']
];
const validStages = new Set(stageOptions.map(([k]) => k));
const stageLabels = Object.fromEntries(stageOptions);

const scopesMap = {};
for (const entry of curriculum) {
  if (!Array.isArray(entry.examScopes)) {
    throw new Error(`Missing examScopes on ${entry.subject} ch${entry.chapter}`);
  }
  scopesMap[`${entry.subject}${entry.chapter}`] = entry.examScopes;
}

const scopesBundle = `/* Generated from data/curriculum.json by tools/build-exam-data.mjs. Do not edit manually. */
(() => {
  'use strict';
  const EXAM_STAGE_OPTIONS = ${JSON.stringify(stageOptions)};
  const EXAM_STAGE_LABELS = ${JSON.stringify(stageLabels)};
  const CURRICULUM_EXAM_SCOPES = ${JSON.stringify(scopesMap)};
  const VALID_SCOPES = new Set(${JSON.stringify([...validStages])});
  const COURSE_TO_LEGACY = {
    physics: '物理',
    chemistry: '化学',
    biology: '生物',
    adv_math_i: '数学',
    adv_math_ii: '数学',
    math_shared: '数学',
    phys: '物理',
    chem: '化学',
    bio: '生物',
    math: '数学'
  };

  function validScope(scope) {
    return VALID_SCOPES.has(scope);
  }

  function legacySubject(subjectOrCourse) {
    if (!subjectOrCourse) return '';
    if (['物理', '化学', '生物', '数学'].includes(subjectOrCourse)) return subjectOrCourse;
    return COURSE_TO_LEGACY[subjectOrCourse] || '';
  }

  function getCurrentScope() {
    const scope = window.S?.dashboard?.preferences?.examScope;
    return validScope(scope) ? scope : 'all';
  }

  function setCurrentScope(scope) {
    const next = validScope(scope) ? scope : 'all';
    if (window.S) {
      window.S.dashboard = window.S.dashboard || {};
      window.S.dashboard.preferences = window.S.dashboard.preferences || {};
      window.S.dashboard.preferences.examScope = next;
      if (typeof window.save === 'function') window.save();
    }
    return next;
  }

  function scopesFor(subjectOrCourse, chapter) {
    const legacy = legacySubject(subjectOrCourse);
    const ch = Number(chapter);
    if (!legacy || !Number.isInteger(ch)) return [];
    return CURRICULUM_EXAM_SCOPES[legacy + ch] || [];
  }

  function matchesChapter(subjectOrCourse, chapter, scope = getCurrentScope()) {
    if (!scope || scope === 'all' || !validScope(scope)) return true;
    const list = scopesFor(subjectOrCourse, chapter);
    return list.includes(scope);
  }

  function filterChapters(courseCode, scope = getCurrentScope()) {
    const legacy = legacySubject(courseCode);
    if (!legacy) return [];
    const maxCh = courseCode === 'adv_math_i' ? 29 : 999;
    return curriculumChaptersFor(legacy)
      .filter(ch => ch <= maxCh && matchesChapter(courseCode, ch, scope));
  }

  function curriculumChaptersFor(legacy) {
    const prefix = legacy;
    return Object.keys(CURRICULUM_EXAM_SCOPES)
      .filter(k => k.startsWith(prefix))
      .map(k => Number(k.slice(prefix.length)))
      .filter(Number.isInteger)
      .sort((a, b) => a - b);
  }

  function labelFor(scope) {
    return EXAM_STAGE_LABELS[scope] || EXAM_STAGE_LABELS.all;
  }

  window.EXAM_STAGE_OPTIONS = EXAM_STAGE_OPTIONS;
  window.EXAM_STAGE_LABELS = EXAM_STAGE_LABELS;
  window.CURRICULUM_EXAM_SCOPES = CURRICULUM_EXAM_SCOPES;
  window.ExamScopeHelper = {
    stages: EXAM_STAGE_OPTIONS.map(([value, label]) => ({ value, label })),
    labels: EXAM_STAGE_LABELS,
    validScope,
    getCurrentScope,
    setCurrentScope,
    scopesFor,
    matchesChapter,
    filterChapters,
    labelFor
  };
})();
`;

fs.writeFileSync(path.join(root, 'data', 'curriculum-scopes.js'), scopesBundle, 'utf8');

const subjectDirs = ['math-exams', 'phys-exams', 'chem-exams', 'bio-exams'];
const bundles = {};

for (const dirName of subjectDirs) {
  const dirPath = path.join(root, 'data', dirName);
  const configPath = path.join(dirPath, 'exam-config.json');
  if (!fs.existsSync(configPath)) {
    throw new Error(`Missing exam-config.json in data/${dirName}`);
  }
  const examConfig = JSON.parse(fs.readFileSync(configPath, 'utf8'));
  const loadJson = (relPath) => JSON.parse(fs.readFileSync(path.join(root, relPath), 'utf8'));
  bundles[examConfig.id] = {
    examConfig,
    assemblyProfiles: loadJson(examConfig.dataFiles.assemblyProfiles),
    heat: loadJson(examConfig.dataFiles.heatStatistics),
    research: loadJson(examConfig.dataFiles.researchData),
    bank: loadJson(examConfig.dataFiles.originalBank)
  };
}

fs.mkdirSync(path.join(root, 'vendor', 'exam-data'), { recursive: true });
const bundleOutput = `/* Generated from canonical JSON files in data/*-exams/ by tools/build-exam-data.mjs. */\nwindow.UEC_EXAM_BUNDLES=${JSON.stringify(bundles)};\n`;
fs.writeFileSync(path.join(root, 'vendor', 'exam-data', 'exam-bundles.js'), bundleOutput, 'utf8');

console.log(
  `Built data/curriculum-scopes.js (${Object.keys(scopesMap).length} chapters) and vendor/exam-data/exam-bundles.js (${Object.keys(bundles).join(', ')})`
);
