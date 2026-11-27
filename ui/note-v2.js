/* Note V2 8-Module Renderer, KaTeX Inline/Display Hydrator & Interactive Question Controls */
(() => {
  'use strict';

  const MODULE_TITLES_V2 = [
    '考纲与教材锚点',
    '核心概念与本质',
    '公式与方程式卡',
    '高频陷阱与辨析',
    '阶梯典例精讲',
    '四阶实战题组',
    '考前60秒速记',
    '自检与知识库溯源'
  ];

  const KIND_LABELS = {
    definition: '核心定义',
    law: '定量定律',
    mechanism: '微观本质',
    experiment: '教材实验',
    table: '对比速览'
  };

  function safeEsc(s) {
    return typeof window.esc === 'function'
      ? window.esc(s)
      : String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  }

  // Safely render markdown-lite bold/code AND KaTeX display \[...\] / inline \(...\) without double-escaping TeX.
  function richText(str) {
    const raw = String(str ?? '');
    const mathTokens = [];
    const tokenized = raw.replace(/\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)/g, (_, disp, inl) => {
      const idx = mathTokens.length;
      mathTokens.push({ disp: disp !== undefined, tex: (disp !== undefined ? disp : inl).trim() });
      return `@@TEX_${idx}@@`;
    });
    let html = safeEsc(tokenized)
      .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\n/g, '<br>');
    html = html.replace(/@@TEX_(\d+)@@/g, (_, idxStr) => {
      const tok = mathTokens[Number(idxStr)];
      if (!tok) return '';
      if (tok.disp) {
        return `<div class="tex-block" data-tex="${safeEsc(tok.tex)}">${safeEsc(tok.tex)}</div>`;
      }
      return `<span class="tex-inline" data-tex-inline="${safeEsc(tok.tex)}">${safeEsc(tok.tex)}</span>`;
    });
    return html;
  }

  function richList(arr, ordered = false) {
    const tag = ordered ? 'ol' : 'ul';
    return `<${tag}>${(arr || []).map(item => `<li>${richText(item)}</li>`).join('')}</${tag}>`;
  }

  function renderTable(tbl) {
    if (!tbl || !Array.isArray(tbl.headers)) return '';
    return `<div class="note-v2-table-wrap"><table class="note-v2-table"><thead><tr>${tbl.headers
      .map(h => `<th>${richText(h)}</th>`)
      .join('')}</tr></thead><tbody>${(tbl.rows || [])
      .map(r => `<tr>${r.map(c => `<td>${richText(c)}</td>`).join('')}</tr>`)
      .join('')}</tbody></table></div>`;
  }

  function tierClass(tier) {
    return /^L[1-4]$/.test(tier) ? `tier-${tier}` : 'tier-L2';
  }

  function renderQuestionV2(q, show = false, idxLabel = '') {
    const tierBadge = q.tier
      ? `<span class="note-v2-tier ${tierClass(q.tier)}">${safeEsc(q.tierLabel || q.tier)}</span>`
      : '';
    const styleBadge = q.examStyle ? `<span class="tag">${safeEsc(q.examStyle)}</span>` : '';
    const head = (tierBadge || styleBadge || idxLabel)
      ? `<div class="note-v2-qhead"><span>${idxLabel ? `<b>${safeEsc(idxLabel)}</b> ` : ''}${tierBadge} ${styleBadge}</span>${q.subject_code ? `<button class="text-button" data-a="reader-v2-add-error" data-course="${safeEsc(q.subject_code)}" data-chapter="${safeEsc(q.chapter_id || '')}" data-qid="${safeEsc(q.id || '')}" data-q="${safeEsc(String(q.q || '').slice(0, 140))}">+ 记入错题本</button>` : ''}</div>`
      : '';
    const mcqHtml = Array.isArray(q.options) && q.options.length
      ? `<div class="note-v2-mcq-list" role="group" aria-label="选择题选项">${q.options
          .map((opt, idx) => {
            const letter = ['A', 'B', 'C', 'D'][idx] || opt.slice(0, 1);
            return `<button type="button" class="note-v2-mcq-btn" data-a="reader-v2-mcq" data-choice="${safeEsc(letter)}" data-correct="${safeEsc(q.correctOption || '')}">${richText(opt)}</button>`;
          })
          .join('')}</div>`
      : '';
    const stages = [
      q.analysis ? `<p><b>审题线索：</b>${richText(q.analysis)}</p>` : '',
      q.given ? `<p><b>已知条件：</b>${richText(q.given)}</p>` : '',
      q.method ? `<p><b>解题策略：</b>${richText(q.method)}</p>` : '',
      q.principle ? `<p><b>原理依据：</b>${richText(q.principle)}</p>` : ''
    ].join('');
    const rubric = Array.isArray(q.markingPoints) && q.markingPoints.length
      ? `<div class="note-v2-rubric"><b>采分点参考：</b>${richList(q.markingPoints)}</div>`
      : '';
    return `${head}<p>${richText(q.q)}</p>${mcqHtml}<details class="note-v2-sol-box" ${show ? 'open' : ''}><summary>规范解答与采分点</summary>${stages}${richList(q.steps || [], true)}<p><b>标准答案：</b>${richText(q.ans)}</p>${rubric}${q.verification ? `<p><b>验算校核：</b>${richText(q.verification)}</p>` : ''}${q.pitfall ? `<p><b>失分警示：</b>${richText(q.pitfall)}</p>` : ''}</details>`;
  }

  function renderSectionV2(s, chData, k, stateKey) {
    const v2Sec = chData.sections.find(x => x.id === s.id);
    if (!v2Sec) return null;
    const base = `unit-${stateKey}-${s.id}`;
    const check = `${stateKey}:${s.id}`;
    const kbEntries = (window.UEC_KNOWLEDGE_BASE?.entries || []).filter(e =>
      (v2Sec.kbEntryIds || []).includes(e.id) || (e.lessonKey === k && e.section === s.id)
    );

    const m1 = `
      <div class="note-v2-provenance">
        <span class="note-v2-pill is-source">${safeEsc(v2Sec.anchor.pages)}</span>
        <span class="note-v2-pill">考纲 ${safeEsc(v2Sec.anchor.syllabus)}</span>
        <span>${safeEsc(v2Sec.anchor.examWeight || '')}</span>
      </div>
      <div class="note-v2-anchor-grid">
        <div class="note-v2-anchor-box"><h5>本节核心学习目标</h5>${richList(v2Sec.anchor.goals)}</div>
        <div class="note-v2-anchor-box"><h5>前置知识与英语术语</h5>${richList(v2Sec.anchor.prerequisites || [])}${v2Sec.anchor.terms ? `<p class="mu">术语：${safeEsc(v2Sec.anchor.terms)}</p>` : ''}</div>
      </div>`;

    const m2 = `<div class="note-v2-concepts">${v2Sec.concepts.map(c => `
      <article class="note-v2-concept-card" data-kind="${safeEsc(c.kind)}">
        <div class="note-v2-concept-head">
          <h5><span class="tag">${safeEsc(KIND_LABELS[c.kind] || c.kind)}</span> ${richText(c.title)}</h5>
          <span class="note-v2-page-tag">${safeEsc(c.pageRef)}</span>
        </div>
        ${(c.body || []).map(p => `<p>${richText(p)}</p>`).join('')}
        ${renderTable(c.table)}
        ${c.takeaway ? `<div class="note-v2-takeaway"><b>核心提炼：</b>${richText(c.takeaway)}</div>` : ''}
      </article>`).join('')}</div>`;

    const v2FigsHtml = Array.isArray(v2Sec.diagrams) && v2Sec.diagrams.length
      ? `<div class="note-v2-figure-grid">${v2Sec.diagrams.map(d => `<figure class="note-v2-figure"><button type="button" class="figure-open" data-a="figure-open" data-src="${safeEsc(d.src)}" data-caption="${safeEsc(d.caption || d.alt || '')}" aria-label="放大查看：${safeEsc(d.caption || d.alt || '')}"><img src="${safeEsc(d.src)}" alt="${safeEsc(d.alt || d.caption || '')}" loading="lazy"></button><figcaption>${d.pageRef ? `<span class="note-v2-page-tag">${safeEsc(d.pageRef)}</span> ` : ''}${richText(d.caption || '')} <span class="mu">· 点击放大</span></figcaption></figure>`).join('')}</div>`
      : '';

    const legacyFigs = (s.figs || [])
      .filter(f => !(window.QUARANTINED_LEGACY_FIGURES || []).includes(f[0]) && !Object.hasOwn(window.V22_SUPERSEDED_FIGURES || {}, f[0]))
      .map(f => typeof window.figureBlock === 'function' ? window.figureBlock(f[0], f[1]) : '')
      .join('');

    const m3 = `${v2FigsHtml || legacyFigs}<div class="note-v2-formula-grid">${v2Sec.formulas.map(f => `
      <article class="note-v2-formula-card">
        <div class="note-v2-concept-head"><b>${safeEsc(f.title)}</b><span class="note-v2-page-tag">${safeEsc(f.pageRef)}</span></div>
        <div class="tex-block" data-tex="${safeEsc(f.tex)}">${safeEsc(f.tex)}</div>
        <div class="note-v2-formula-meta">
          <p><b>适用条件与单位：</b>${richText(f.conditions)}</p>
          ${f.note ? `<p><b>考场提醒：</b>${richText(f.note)}</p>` : ''}
        </div>
      </article>`).join('')}</div>`;

    const m4 = `<div class="note-v2-pitfall-grid">${v2Sec.pitfalls.map(p => `
      <article class="note-v2-pitfall-card">
        <h5>${richText(p.title)}</h5>
        <p><b>典型错解：</b>${richText(p.wrong)}</p>
        <p><b>病因诊断：</b>${richText(p.diagnosis)}</p>
        <p><b>正解规范：</b>${richText(p.right)}</p>
        <p class="mu"><b>自检口诀：</b>${richText(p.checkRule)}</p>
      </article>`).join('')}</div>`;

    const m5 = v2Sec.examples.map(ex => `
      <article class="note-v2-example-card">
        <div class="note-v2-qhead">
          <span><b>${safeEsc(ex.label)} · ${safeEsc(ex.title)}</b></span>
          <span class="note-v2-tier ${tierClass(ex.tier)}">${safeEsc(ex.tierLabel || ex.tier)}</span>
        </div>
        <p>${richText(ex.prompt)}</p>
        <p><b>审题线索：</b>${richText(ex.clues)}</p>
        <p><b>解题策略：</b>${richText(ex.strategy)}</p>
        <details class="note-v2-sol-box">
          <summary>展开规范步骤与采分点（建议先独立思索 60 秒）</summary>
          ${richList(ex.steps, true)}
          <p><b>答案：</b>${richText(ex.answer)}</p>
          ${ex.markingPoints ? `<div class="note-v2-rubric"><b>采分点：</b>${richList(ex.markingPoints)}</div>` : ''}
          ${ex.verification ? `<p><b>验算核对：</b>${richText(ex.verification)}</p>` : ''}
          ${ex.pitfall ? `<p class="mu"><b>易错提醒：</b>${richText(ex.pitfall)}</p>` : ''}
        </details>
      </article>`).join('');

    const m6 = `
      <div class="note-v2-practice-toolbar" role="group" aria-label="按难度筛选练习题">
        <button type="button" class="on" data-a="reader-v2-tier" data-tier="all">全部 (${v2Sec.practice.length})</button>
        ${['L1', 'L2', 'L3', 'L4'].map(t => {
          const n = v2Sec.practice.filter(q => q.tier === t).length;
          const lbl = { L1: 'L1 基础', L2: 'L2 期末', L3: 'L3 预试', L4: 'L4 统考压轴' }[t];
          return n ? `<button type="button" data-a="reader-v2-tier" data-tier="${t}">${lbl} (${n})</button>` : '';
        }).join('')}
      </div>
      ${v2Sec.practice.map((q, idx) => `
        <article class="note-v2-qcard" id="${base}-q${idx + 1}" data-tier="${safeEsc(q.tier)}">
          ${renderQuestionV2({ ...q, subject_code: chData.courseCode, chapter_id: chData.chapter }, false, `第 ${idx + 1} 题`)}
        </article>`).join('')}`;

    const m7 = `<div class="note-v2-cheatsheet">${richList(v2Sec.cheatSheet)}</div>`;

    const curCheck = window.S?.checks?.[check];
    const m8 = `
      ${kbEntries.length ? `<div><b>关联内置知识库条目（点击查阅原书页码）：</b><div class="note-v2-kb-links">${kbEntries.map(e => `<button type="button" class="note-v2-kb-chip" data-a="dash-kb-open" data-kbid="${safeEsc(e.id)}">[${safeEsc(e.shortTitle)} ${safeEsc(e.page)}] ${safeEsc(e.title)} →</button>`).join('')}</div></div>` : ''}
      <div class="note-v2-qcard">${renderQuestionV2(v2Sec.quiz, false, '本节通关快测')}</div>
      <div class="row">
        <span class="mu">掌握度自评（保存于本机）：</span>
        ${['需重学', '看解析才会', '能独立解释'].map((v, i) => `<button type="button" data-a="section-check" data-k="${safeEsc(check)}" data-v="${i}" class="${curCheck === i ? 'on' : ''}">${v}${curCheck === i ? ' ✓' : ''}</button>`).join('')}
      </div>`;

    const blocks = [m1, m2, m3, m4, m5, m6, m7, m8];
    return `<details class="card lesson-section lesson-section-v2" id="${base}" data-note-version="2" open>
      <summary>${safeEsc(s.id)} ${safeEsc(s.t)} <span class="note-v2-pill">教材精校 V2 · 8模块</span><span class="note-v2-pill is-source">${safeEsc(v2Sec.anchor.pages)}</span></summary>
      <div class="module-links">${MODULE_TITLES_V2.map((t, i) => `<a href="#${base}-m${i + 1}">${String(i + 1).padStart(2, '0')} ${t}</a>`).join('')}</div>
      ${blocks.map((b, i) => `<section class="note-module note-module-v2" data-module="${i + 1}" data-module-title="${MODULE_TITLES_V2[i]}" id="${base}-m${i + 1}"><h4>${String(i + 1).padStart(2, '0')} ${MODULE_TITLES_V2[i]}</h4>${b}</section>`).join('')}
    </details>`;
  }

  // Wrap renderSection
  const prevRenderSection = window.renderSection;
  if (typeof prevRenderSection === 'function') {
    window.renderSection = function (s, k, stateKey = k) {
      const v2 = window.NOTES_V2?.[k];
      if (v2) {
        const html = renderSectionV2(s, v2, k, stateKey);
        if (html) return html;
      }
      return prevRenderSection(s, k, stateKey);
    };
  }

  // Wrap renderQuestion globally so Question Bank / Mock / Search also render KaTeX + L1-L4 tiers cleanly.
  const prevRenderQuestion = window.renderQuestion;
  if (typeof prevRenderQuestion === 'function') {
    window.renderQuestion = function (q, show = false) {
      if (q && (q.tier || q.options || q.markingPoints || /\\\(|\\\[/.test(String(q.q || '') + String(q.ans || '')))) {
        return renderQuestionV2(q, show);
      }
      return prevRenderQuestion(q, show);
    };
  }

  // Wrap vLesson to render V2 chapter hero, scope pills, concept map, and strip duplicate legacy ex/pr dumps on V2 chapters.
  const prevVLesson = window.vLesson;
  if (typeof prevVLesson === 'function') {
    window.vLesson = function (k) {
      const html = prevVLesson(k);
      const v2 = window.NOTES_V2?.[k];
      if (!v2 || typeof document === 'undefined') return html;

      const holder = document.createElement('div');
      holder.innerHTML = html;

      const topCard = holder.firstElementChild;
      if (topCard) {
        topCard.classList.add('note-v2-hero');
        const scopeMap = { sem1_final: '上半年期末考', pre_exam: '预试', sem2_final: '毕业考', uec: 'UEC 统考' };
        const scopeHtml = (v2.examScopes || []).map(sc => `<span class="note-v2-pill is-scope">${scopeMap[sc] || sc}</span>`).join('');
        const treeHtml = v2.chapterOverview?.conceptTree
          ? `<div class="note-v2-overview-tree">${v2.chapterOverview.conceptTree.map(b => `<div class="note-v2-tree-branch"><b>${safeEsc(b.branch)}</b><ul>${b.items.map(it => `<li>${safeEsc(it)}</li>`).join('')}</ul></div>`).join('')}</div>`
          : '';
        const extraHero = document.createElement('div');
        extraHero.innerHTML = `
          <div class="note-v2-badge-row">
            <span class="note-v2-pill">UEC 教材精校 V2 · 8模块</span>
            <span class="note-v2-pill is-source">${safeEsc(v2.bookCitation)}</span>
            ${scopeHtml}
          </div>
          ${v2.chapterOverview?.summary ? `<p>${richText(v2.chapterOverview.summary)}</p>` : ''}
          ${treeHtml}
          ${v2.paperFocus?.length ? `<details style="margin-top:10px"><summary>兴华 2027 校内考 &amp; UEC 统考命题结构对齐</summary>${richList(v2.paperFocus)}</details>` : ''}`;
        topCard.append(extraHero);
      }

      // Remove redundant legacy bottom ex/pr/toc/exam cards if already integrated inside V2 hero, reader rail & 8-module sections.
      holder.querySelectorAll(':scope > section.card:not(.note-v2-hero), :scope > details.card:not(.lesson-section)').forEach(el => {
        const h3 = el.querySelector(':scope > h3')?.textContent?.trim() || '';
        const sum = el.querySelector(':scope > summary')?.textContent?.trim() || '';
        if (h3 === '本章小节目录' || ['兴华校内与UEC正式统考资料', '考试答题方式', '例题（含完整步骤）', '练习与模拟题（基础→困难）'].some(x => sum.startsWith(x))) {
          el.remove();
        }
      });

      return holder.innerHTML;
    };
  }

  // Upgrade renderStudyMath so KaTeX renders in ALL views (V2 notes, KB, Bank, Mock Review, Search) with both display and inline math.
  let katexPromise = null;
  function ensureKatex() {
    if (window.katex) return Promise.resolve();
    if (!katexPromise) {
      if (!document.getElementById('katex-style')) {
        const l = document.createElement('link');
        l.id = 'katex-style';
        l.rel = 'stylesheet';
        l.href = 'vendor/katex/katex.min.css';
        document.head.append(l);
      }
      katexPromise = new Promise((resolve, reject) => {
        const s = document.createElement('script');
        s.src = 'vendor/katex/katex.min.js';
        s.onload = resolve;
        s.onerror = () => {
          katexPromise = null;
          s.remove();
          reject(new Error('KaTeX load failed'));
        };
        document.head.append(s);
      });
    }
    return katexPromise;
  }

  const prevRenderStudyMath = window.renderStudyMath;
  window.renderStudyMath = async function () {
    // Sync V2 formulas into STUDY_FORMULAS for legacy consumers
    for (const [key, ch] of Object.entries(window.NOTES_V2 || {})) {
      window.STUDY_FORMULAS = window.STUDY_FORMULAS || {};
      for (const s of ch.sections || []) {
        if (s.formulas?.length) {
          window.STUDY_FORMULAS[`${key}/${s.id}`] = s.formulas.map(f => [f.title, f.tex, f.conditions]);
        }
      }
    }

    // Legacy Module 5 formula card injection for non-V2 chapters
    const legacySections = [...document.querySelectorAll('.lesson-section:not(.lesson-section-v2)')];
    for (const section of legacySections) {
      const m = section.id.match(/^unit-(?:(?:adv_math_i|adv_math_ii):)?((?:数学|物理|化学|生物)\d+)-([\d.]+)$/);
      if (!m) continue;
      const entries = window.STUDY_FORMULAS?.[m[1] + '/' + m[2]];
      if (!entries) continue;
      const host = section.querySelector('[data-module="5"]');
      if (!host || host.querySelector('.typeset-formulas')) continue;
      const box = document.createElement('div');
      box.className = 'typeset-formulas';
      box.innerHTML = '<h5>公式速览</h5>' + entries.map(([title, tex, condition]) => `<div class="formula-card"><b>${safeEsc(title)}</b><div class="tex-formula" data-tex="${safeEsc(tex)}">${safeEsc(tex)}</div><small>${safeEsc(condition)}</small></div>`).join('');
      host.querySelector('h4')?.after(box);
    }

    const displayNodes = [...document.querySelectorAll('[data-tex]:not([data-typeset="true"])')];
    const inlineNodes = [...document.querySelectorAll('[data-tex-inline]:not([data-typeset="true"])')];
    if (!displayNodes.length && !inlineNodes.length) {
      if (typeof prevRenderStudyMath === 'function' && legacySections.length) {
        return prevRenderStudyMath();
      }
      return;
    }

    try {
      await ensureKatex();
      for (const el of displayNodes) {
        window.katex.render(el.dataset.tex, el, { displayMode: true, throwOnError: false, trust: false, strict: 'warn' });
        el.dataset.typeset = 'true';
      }
      for (const el of inlineNodes) {
        window.katex.render(el.dataset.texInline, el, { displayMode: false, throwOnError: false, trust: false, strict: 'warn' });
        el.dataset.typeset = 'true';
      }
    } catch (_) {
      // Plain text / TeX fallback stays readable if KaTeX assets fail to load.
    }
  };

  // Interactive event listeners for Note V2 tier filter, MCQ grading, and error logging
  if (typeof document !== 'undefined') {
    document.addEventListener('click', ev => {
      const btn = ev.target.closest('[data-a]');
      if (!btn) return;
      const act = btn.dataset.a;

      if (act === 'reader-v2-tier') {
        const mod = btn.closest('.note-module');
        if (!mod) return;
        const chosen = btn.dataset.tier || 'all';
        btn.parentElement.querySelectorAll('button').forEach(b => b.classList.toggle('on', b === btn));
        mod.querySelectorAll('.note-v2-qcard').forEach(card => {
          card.classList.toggle('is-hidden', chosen !== 'all' && card.dataset.tier !== chosen);
        });
      } else if (act === 'reader-v2-mcq') {
        const group = btn.closest('.note-v2-mcq-list');
        if (!group) return;
        const correct = btn.dataset.correct;
        const choice = btn.dataset.choice;
        group.querySelectorAll('.note-v2-mcq-btn').forEach(b => {
          b.classList.remove('is-correct', 'is-wrong');
          if (correct && b.dataset.choice === correct) b.classList.add('is-correct');
          else if (b === btn && choice !== correct) b.classList.add('is-wrong');
        });
        const card = btn.closest('.note-v2-qcard') || btn.closest('.card');
        const sol = card?.querySelector('details.note-v2-sol-box');
        if (sol) sol.open = true;
      } else if (act === 'reader-v2-add-error') {
        if (!window.S) return;
        const code = btn.dataset.course || 'chemistry';
        const legacy = (window.SUBJECTS || []).find(s => s.code === code)?.legacy || '化学';
        const ch = Number(btn.dataset.chapter) || 0;
        const qText = btn.dataset.q || '章节练习错题';
        const qid = btn.dataset.qid || '';
        const dup = qid && window.S.err.some(e => e.noteRef === qid);
        if (!dup) {
          window.S.err.push({
            s: legacy,
            subject_code: code,
            c: ch,
            q: qText,
            w: '概念不懂',
            st: 0,
            last: '',
            d: typeof window.today === 'function' ? window.today() : new Date().toISOString().slice(0, 10),
            noteRef: qid || undefined,
            paper_no: null
          });
          window.StudyApp?.recordErrorAdded?.();
          window.save?.();
          window.studyToast?.('已将该题加入错题本');
        } else {
          window.studyToast?.('此题已在错题本中');
        }
      }
    });
  }

  window.NoteV2 = {
    MODULE_TITLES: MODULE_TITLES_V2,
    richText,
    renderQuestion: renderQuestionV2,
    renderSection: renderSectionV2
  };
})();
