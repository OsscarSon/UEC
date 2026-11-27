/* Compile data/notes-v2/*.json into vendor/notes-v2/notes-v2-bundle.js and sync LESSONS/BATCH_NOTES/STUDY_FORMULAS. */
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const srcDir = path.join(root, 'data', 'notes-v2');
const outDir = path.join(root, 'vendor', 'notes-v2');
const outFile = path.join(outDir, 'notes-v2-bundle.js');

const VALID_TIERS = new Set(['L1', 'L2', 'L3', 'L4']);

function assert(cond, msg) {
  if (!cond) throw new Error(`[build-notes-v2] ${msg}`);
}

const files = fs.readdirSync(srcDir).filter(f => f.endsWith('.json')).sort();
assert(files.length > 0, 'No JSON files found in data/notes-v2');

const chapters = {};
let sectionTotal = 0;
let questionTotal = 0;

for (const file of files) {
  const ch = JSON.parse(fs.readFileSync(path.join(srcDir, file), 'utf8'));
  assert(ch.lessonKey && ch.courseCode && ch.subject && ch.chapter && ch.title, `${file} missing chapter header fields`);
  assert(Array.isArray(ch.sections) && ch.sections.length > 0, `${file} must have sections`);

  const seenSec = new Set();
  for (const s of ch.sections) {
    assert(s.id && s.t && !seenSec.has(s.id), `${file} invalid/duplicate section id ${s.id}`);
    seenSec.add(s.id);
    assert(s.anchor && Array.isArray(s.anchor.goals) && s.anchor.goals.length > 0, `${file}:${s.id} missing anchor.goals`);
    assert(Array.isArray(s.concepts) && s.concepts.length > 0, `${file}:${s.id} missing concepts`);
    assert(Array.isArray(s.formulas), `${file}:${s.id} missing formulas array`);
    assert(Array.isArray(s.pitfalls) && s.pitfalls.length > 0, `${file}:${s.id} missing pitfalls`);
    assert(Array.isArray(s.examples) && s.examples.length >= 2, `${file}:${s.id} needs >= 2 examples`);
    assert(Array.isArray(s.practice) && s.practice.length >= 4, `${file}:${s.id} needs >= 4 practice questions`);
    assert(Array.isArray(s.cheatSheet) && s.cheatSheet.length > 0, `${file}:${s.id} missing cheatSheet`);
    assert(s.quiz && s.quiz.q && s.quiz.ans, `${file}:${s.id} missing quiz`);

    for (const q of s.practice) {
      assert(VALID_TIERS.has(q.tier), `${file}:${s.id} invalid tier "${q.tier}" on ${q.id}`);
      assert(q.q && q.ans && Array.isArray(q.steps) && q.steps.length > 0, `${file}:${s.id} incomplete question ${q.id}`);
      if (q.options) {
        assert(Array.isArray(q.options) && q.options.length === 4 && ['A', 'B', 'C', 'D'].includes(q.correctOption), `${file}:${s.id} invalid MCQ options on ${q.id}`);
      }
      questionTotal += 1;
    }
    sectionTotal += 1;
  }

  chapters[ch.lessonKey] = ch;
}

const syncScript = `/* Generated from data/notes-v2/*.json by tools/build-notes-v2.mjs. Do not edit manually. */
(() => {
  'use strict';
  const NOTES_V2_DATA = ${JSON.stringify(chapters)};
  window.NOTES_V2 = Object.assign(window.NOTES_V2 || {}, NOTES_V2_DATA);
  window.LESSONS = window.LESSONS || {};
  window.BATCH_NOTES = window.BATCH_NOTES || {};
  window.STUDY_FORMULAS = window.STUDY_FORMULAS || {};

  function conceptToParagraphs(concepts) {
    const out = [];
    for (const c of concepts) {
      out.push('**' + c.title + '**（' + c.pageRef + '）：' + (c.body || []).join(' '));
      if (c.takeaway) out.push('**核心要点：**' + c.takeaway);
    }
    return out;
  }

  function toBatchQuestion(q, ch) {
    return {
      id: q.id,
      tier: q.tier,
      tierLabel: q.tierLabel,
      examStyle: q.examStyle,
      subject_code: ch.courseCode,
      chapter_id: ch.chapter,
      paper_no: null,
      question_origin: 'original_textbook_aligned',
      q: q.q,
      options: q.options || null,
      correctOption: q.correctOption || null,
      analysis: q.clues || q.analysis || '',
      given: q.given || '',
      method: q.method || '',
      principle: q.principle || '',
      steps: q.steps || [],
      ans: q.ans,
      markingPoints: q.markingPoints || [],
      verification: q.verification || '',
      pitfall: q.pitfall || ''
    };
  }

  for (const [lessonKey, ch] of Object.entries(NOTES_V2_DATA)) {
    const existingLesson = window.LESSONS[lessonKey] || {};
    const existingBatch = window.BATCH_NOTES[lessonKey] || {};
    const flatExamples = [];
    const flatPractice = [];

    const syncedSections = ch.sections.map(s => {
      const prevSec = (existingLesson.sections || []).find(x => x.id === s.id) || {};
      const bodyParas = conceptToParagraphs(s.concepts);
      for (const ex of s.examples) {
        flatExamples.push({
          lv: ex.tierLabel || ex.tier,
          q: '[' + s.id + '] ' + ex.prompt,
          steps: ex.steps,
          ans: ex.answer,
          pts: (ex.markingPoints || []).join('；')
        });
      }
      for (const p of s.practice) {
        flatPractice.push({
          lv: p.tier === 'L1' ? '基础' : p.tier === 'L2' ? '中等' : '困难',
          q: '[' + s.id + ' · ' + (p.tierLabel || p.tier) + '] ' + p.q,
          ans: p.ans,
          sol: p.steps.join(' ')
        });
      }
      return {
        id: s.id,
        t: s.t,
        syl: s.anchor.syllabus,
        body: bodyParas,
        figs: prevSec.figs || s.figs || [],
        f: s.formulas.map(f => f.title + '：' + (f.plain || f.tex)),
        terms: s.anchor.terms || prevSec.terms || '',
        tips: s.pitfalls.map(p => [p.title, p.diagnosis + ' 正解：' + p.right])
      };
    });

    window.LESSONS[lessonKey] = {
      ...existingLesson,
      syl: ch.syllabus || existingLesson.syl || '',
      status: ch.bookCitation + ' · 已按教材精校并升级为 UEC 高效笔记 V2（' + ch.sections.length + ' 节）。',
      sections: syncedSections,
      ex: flatExamples,
      pr: flatPractice,
      method: {
        format: ch.paperFocus || existingLesson.method?.format || [],
        steps: ch.solvingWorkflow || existingLesson.method?.steps || [],
        types: ch.questionTypes || existingLesson.method?.types || [],
        score: ch.scoringNotes || existingLesson.method?.score || []
      },
      vid: ch.vid || existingLesson.vid || []
    };

    const nextBatch = { ...existingBatch };
    for (const s of ch.sections) {
      const prevB = existingBatch[s.id] || {};
      nextBatch[s.id] = {
        ...prevB,
        note_version: 2,
        subject_code: ch.courseCode,
        chapter_id: ch.chapter,
        section_id: s.id,
        goals: s.anchor.goals,
        prerequisites: s.anchor.prerequisites || [],
        flow: s.concepts.map(c => c.title),
        deep: conceptToParagraphs(s.concepts),
        derive: s.formulas.map(f => '**' + f.title + '**：\\[' + f.tex + '\\]（' + f.conditions + '）'),
        examples: s.examples.map(ex => ({
          subject_code: ch.courseCode,
          chapter_id: ch.chapter,
          paper_no: null,
          q: ex.prompt,
          analysis: ex.clues,
          given: ex.given || '',
          method: ex.strategy,
          principle: ex.principle || '',
          steps: ex.steps,
          ans: ex.answer,
          verification: ex.verification || '',
          pitfall: ex.pitfall || '',
          markingPoints: ex.markingPoints || []
        })),
        strategy: {
          worked_example_index: 0,
          trigger: s.examples[0]?.clues || '',
          method: s.examples[0]?.strategy || '',
          principle: s.examples[0]?.principle || '',
          verification: s.examples[0]?.verification || '',
          pitfall: s.examples[0]?.pitfall || ''
        },
        exam: ch.paperFocus || prevB.exam || [],
        exam_evidence: prevB.exam_evidence || [],
        error_analysis: s.pitfalls.map(p => ({
          wrong_approach: p.wrong,
          correction: p.diagnosis + '；' + p.right,
          verification: p.checkRule
        })),
        practice: s.practice.map(q => toBatchQuestion(q, ch)),
        quick: s.cheatSheet,
        quiz: toBatchQuestion({ ...s.quiz, id: lessonKey + '-' + s.id + '-quiz', tier: 'L2', tierLabel: '自检' }, ch),
        content_sources: [
          {
            source_id: ch.bookId,
            page: s.anchor.pages,
            version: ch.bookCitation,
            access_date: '2026-11-28'
          }
        ]
      };
      if (s.formulas.length) {
        window.STUDY_FORMULAS[lessonKey + '/' + s.id] = s.formulas.map(f => [f.title, f.tex, f.conditions]);
      }
    }
    window.BATCH_NOTES[lessonKey] = nextBatch;
  }
})();
`;

fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(outFile, syncScript, 'utf8');
console.log(`Built ${path.relative(root, outFile)} (${files.length} chapters, ${sectionTotal} sections, ${questionTotal} V2 questions).`);
