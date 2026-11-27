/* Generated from data/curriculum.json by tools/build-exam-data.mjs. Do not edit manually. */
(() => {
  'use strict';
  const EXAM_STAGE_OPTIONS = [["all","全部阶段（不限）"],["sem1_final","第一学期期末考"],["pre_exam","校内预试"],["sem2_final","毕业考 / 第二学期期末"],["uec","UEC 正式统考"]];
  const EXAM_STAGE_LABELS = {"all":"全部阶段（不限）","sem1_final":"第一学期期末考","pre_exam":"校内预试","sem2_final":"毕业考 / 第二学期期末","uec":"UEC 正式统考"};
  const CURRICULUM_EXAM_SCOPES = {"物理1":[],"物理2":[],"物理3":["sem1_final","pre_exam","sem2_final","uec"],"物理4":["sem1_final","pre_exam","sem2_final","uec"],"物理5":["sem1_final","pre_exam","sem2_final","uec"],"物理6":["sem1_final","pre_exam","sem2_final","uec"],"物理7":["sem1_final","pre_exam","sem2_final","uec"],"物理8":["sem1_final","pre_exam","sem2_final","uec"],"物理9":[],"物理10":["pre_exam","sem2_final","uec"],"物理11":["sem1_final","pre_exam","sem2_final","uec"],"物理12":[],"物理13":["pre_exam","sem2_final","uec"],"物理14":["pre_exam","sem2_final","uec"],"物理15":["pre_exam","sem2_final","uec"],"物理16":["pre_exam","sem2_final","uec"],"物理17":["pre_exam","sem2_final","uec"],"物理18":["sem2_final","uec"],"物理19":["sem2_final","uec"],"物理20":["pre_exam","sem2_final","uec"],"物理21":["sem1_final","pre_exam","sem2_final","uec"],"物理22":["sem1_final","pre_exam","sem2_final","uec"],"物理23":["sem1_final","pre_exam","sem2_final","uec"],"物理24":["pre_exam","sem2_final","uec"],"物理25":["sem2_final","uec"],"物理26":["sem2_final","uec"],"物理27":["sem2_final","uec"],"化学1":[],"化学2":["sem2_final","uec"],"化学3":["sem1_final","pre_exam","sem2_final","uec"],"化学4":["sem1_final","pre_exam","sem2_final","uec"],"化学5":["sem1_final","pre_exam","sem2_final","uec"],"化学6":["sem1_final","pre_exam","sem2_final","uec"],"化学7":["sem1_final","pre_exam","sem2_final","uec"],"化学8":["sem1_final","pre_exam","sem2_final","uec"],"化学9":["sem2_final","uec"],"化学10":["sem2_final","uec"],"化学11":["sem2_final","uec"],"化学12":["sem2_final","uec"],"化学13":["sem2_final","uec"],"化学14":["sem2_final","uec"],"化学15":["sem2_final","uec"],"化学16":["sem2_final","uec"],"化学17":["pre_exam","sem2_final","uec"],"化学18":["pre_exam","sem2_final","uec"],"化学19":["pre_exam","sem2_final","uec"],"化学20":["pre_exam","sem2_final","uec"],"化学21":["pre_exam","sem2_final","uec"],"化学22":["pre_exam","sem2_final","uec"],"化学23":["pre_exam","sem2_final","uec"],"化学24":["pre_exam","sem2_final","uec"],"化学25":["pre_exam","sem2_final","uec"],"化学26":["sem1_final","pre_exam","sem2_final","uec"],"化学27":["sem1_final","pre_exam","sem2_final","uec"],"化学28":["sem1_final","pre_exam","sem2_final","uec"],"化学29":["sem1_final","pre_exam","sem2_final","uec"],"化学30":["sem1_final","pre_exam","sem2_final","uec"],"化学31":["pre_exam","sem2_final","uec"],"化学32":["pre_exam","sem2_final","uec"],"化学33":["pre_exam","sem2_final","uec"],"化学34":["pre_exam","sem2_final","uec"],"化学35":["pre_exam","sem2_final","uec"],"生物1":["pre_exam","sem2_final","uec"],"生物2":["pre_exam","sem2_final","uec"],"生物3":["pre_exam","sem2_final","uec"],"生物4":["pre_exam","sem2_final","uec"],"生物5":["pre_exam","sem2_final","uec"],"生物6":["pre_exam","sem2_final","uec"],"生物7":["pre_exam","sem2_final","uec"],"生物8":["pre_exam","sem2_final","uec"],"生物9":["pre_exam","sem2_final","uec"],"生物10":["sem1_final","pre_exam","sem2_final","uec"],"生物11":["sem1_final","pre_exam","sem2_final","uec"],"生物12":["pre_exam","sem2_final","uec"],"生物13":["pre_exam","sem2_final","uec"],"生物14":["pre_exam","sem2_final","uec"],"生物15":["pre_exam","sem2_final","uec"],"生物16":["pre_exam","sem2_final","uec"],"生物17":["sem1_final","pre_exam","sem2_final","uec"],"生物18":["sem1_final","pre_exam","sem2_final","uec"],"生物19":["sem1_final","pre_exam","sem2_final","uec"],"数学1":["sem1_final","pre_exam","sem2_final","uec"],"数学2":["sem1_final","pre_exam","sem2_final","uec"],"数学3":["sem1_final","pre_exam","sem2_final","uec"],"数学4":["sem1_final","pre_exam","sem2_final","uec"],"数学5":["sem1_final","pre_exam","sem2_final","uec"],"数学6":["sem1_final","pre_exam","sem2_final","uec"],"数学7":["sem1_final","pre_exam","sem2_final","uec"],"数学8":["sem1_final","pre_exam","sem2_final","uec"],"数学9":["sem1_final","pre_exam","sem2_final","uec"],"数学10":["sem1_final","pre_exam","sem2_final","uec"],"数学11":["sem1_final","pre_exam","sem2_final","uec"],"数学12":["sem1_final","pre_exam","sem2_final","uec"],"数学13":["sem1_final","pre_exam","sem2_final","uec"],"数学14":["sem1_final","pre_exam","sem2_final","uec"],"数学15":["sem1_final","pre_exam","sem2_final","uec"],"数学16":["sem1_final","pre_exam","sem2_final","uec"],"数学17":["sem1_final","pre_exam","sem2_final","uec"],"数学18":["sem1_final","pre_exam","sem2_final","uec"],"数学19":["sem1_final","pre_exam","sem2_final","uec"],"数学20":["sem1_final","pre_exam","sem2_final","uec"],"数学21":["sem1_final","pre_exam","sem2_final","uec"],"数学22":["sem1_final","pre_exam","sem2_final","uec"],"数学23":["sem1_final","pre_exam","sem2_final","uec"],"数学24":["sem1_final","pre_exam","sem2_final","uec"],"数学25":["sem1_final","pre_exam","sem2_final","uec"],"数学26":["sem1_final","pre_exam","sem2_final","uec"],"数学27":["sem1_final","pre_exam","sem2_final","uec"],"数学28":["sem1_final","pre_exam","sem2_final","uec"],"数学29":["sem1_final","pre_exam","sem2_final","uec"],"数学30":["sem1_final","pre_exam","sem2_final","uec"],"数学31":["sem1_final","pre_exam","sem2_final","uec"],"数学32":["pre_exam","sem2_final","uec"],"数学33":["pre_exam","sem2_final","uec"],"数学34":["sem1_final","pre_exam","sem2_final","uec"],"数学35":["pre_exam","sem2_final","uec"]};
  const VALID_SCOPES = new Set(["all","sem1_final","pre_exam","sem2_final","uec"]);
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
