/* Generic multi-subject exam research, heat statistics, and assembly registry. */
(() => {
  'use strict';

  const subjects = new Map();
  const engines = new Map();

  function validateBundleContract(bundle) {
    const errors = [];
    if (!bundle || typeof bundle !== 'object') return { ok: false, errors: ['bundle must be an object'] };
    const cfg = bundle.examConfig;
    if (!cfg || typeof cfg.id !== 'string' || !cfg.id) errors.push('missing examConfig.id');
    if (!cfg || !Array.isArray(cfg.examTypes) || !cfg.examTypes.length) errors.push('missing examConfig.examTypes');
    if (!bundle.assemblyProfiles || typeof bundle.assemblyProfiles.profiles !== 'object') errors.push('missing assemblyProfiles.profiles');
    if (!bundle.heat || !Array.isArray(bundle.heat.exam_types)) errors.push('missing heat.exam_types');
    if (!bundle.research || !Array.isArray(bundle.research.inventory)) errors.push('missing research.inventory');
    if (!bundle.bank || !Array.isArray(bundle.bank.items)) errors.push('missing bank.items');
    return { ok: errors.length === 0, errors };
  }

  function createPlaceholderEngine(subjectId) {
    const bundle = subjects.get(subjectId);
    if (!bundle) throw new Error(`Unknown exam subject: ${subjectId}`);
    const cfg = bundle.examConfig;
    const types = Object.fromEntries(
      cfg.examTypes.map(t => [t.exam_type, { name: t.title, course: t.course, scope: t.scope, last: t.last }])
    );
    const strategies = {
      old_hot: '旧制热门优先',
      new_focus: '2026新制重点',
      combined: '全历年综合',
      balanced: '均衡覆盖',
      cold: '冷门强化'
    };
    const profile = (examType) => bundle.assemblyProfiles.profiles[examType] || null;
    const validate = () => ({
      ok: false,
      errors: [`${cfg.name}暂未导入历届原卷统计与核验题库，无法生成整卷。`]
    });
    const generate = () => {
      throw new Error(`${cfg.name}尚未导入核验历届原卷与原创组卷池（数据目录：data/${cfg.id}-exams/）。`);
    };
    return {
      subjectId,
      ready: cfg.status === 'ready',
      types,
      strategies,
      profile,
      validate,
      generate
    };
  }

  function registerSubject(id, bundle) {
    const check = validateBundleContract(bundle);
    if (!check.ok) throw new Error(`Invalid exam bundle for ${id}: ${check.errors.join('; ')}`);
    subjects.set(id, bundle);
    if (id === 'math') {
      window.MATH_ASSEMBLY_PROFILES = bundle.assemblyProfiles;
      window.MATH_HEAT = bundle.heat;
      window.MATH_EXAM_RESEARCH = bundle.research;
      window.MATH_EXAM_BANK = bundle.bank;
    }
    if (!engines.has(id)) {
      engines.set(id, createPlaceholderEngine(id));
    }
    return bundle;
  }

  function registerEngine(subjectId, engine) {
    if (!subjects.has(subjectId)) throw new Error(`Cannot register engine before subject: ${subjectId}`);
    engines.set(subjectId, engine);
  }

  function resolveSubjectId(idOrCourse) {
    if (!idOrCourse) return 'math';
    if (subjects.has(idOrCourse)) return idOrCourse;
    for (const [id, bundle] of subjects.entries()) {
      if (bundle.examConfig.code === idOrCourse || (bundle.examConfig.courses || []).includes(idOrCourse)) {
        return id;
      }
    }
    return null;
  }

  function getSubject(id) {
    const resolved = resolveSubjectId(id);
    return resolved ? subjects.get(resolved) : null;
  }

  function listSubjects() {
    return [...subjects.values()].map(b => b.examConfig);
  }

  function getExamTypes(subjectId) {
    return getSubject(subjectId)?.examConfig?.examTypes || [];
  }

  function getAssemblyProfile(subjectId, examType) {
    return getSubject(subjectId)?.assemblyProfiles?.profiles?.[examType] || null;
  }

  function getHeatData(subjectId) {
    return getSubject(subjectId)?.heat || null;
  }

  function getResearchData(subjectId) {
    return getSubject(subjectId)?.research || null;
  }

  function getOriginalBank(subjectId) {
    return getSubject(subjectId)?.bank || null;
  }

  function getEngine(subjectId) {
    const resolved = resolveSubjectId(subjectId);
    return resolved ? engines.get(resolved) || null : null;
  }

  if (window.UEC_EXAM_BUNDLES && typeof window.UEC_EXAM_BUNDLES === 'object') {
    for (const [id, bundle] of Object.entries(window.UEC_EXAM_BUNDLES)) {
      registerSubject(id, bundle);
    }
  }

  window.ExamRegistry = {
    registerSubject,
    registerEngine,
    resolveSubjectId,
    listSubjects,
    getSubject,
    getExamTypes,
    getAssemblyProfile,
    getHeatData,
    getResearchData,
    getOriginalBank,
    getEngine,
    validateBundleContract,
    createPlaceholderEngine
  };
})();
