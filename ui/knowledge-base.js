/* Built-In Textbook Knowledge Base Workspace UI */
(() => {
  'use strict';

  const TYPE_LABELS = {
    all: '全部条目',
    definition: '核心定义',
    law: '定量定律',
    formula: '核心公式',
    constant: '常数参数',
    experiment: '教材实验',
    table: '参考数据表'
  };

  let mode = 'entries'; // 'entries' | 'toc'
  let bookFilter = 'all';
  let chapterFilter = 'all';
  let typeFilter = 'all';
  let query = '';
  let focusedEntryId = '';

  function safeEsc(s) {
    return typeof window.esc === 'function'
      ? window.esc(s)
      : String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  }

  function rich(s) {
    return window.NoteV2?.richText ? window.NoteV2.richText(s) : safeEsc(s);
  }

  function kbData() {
    return window.UEC_KNOWLEDGE_BASE || { books: [], tocByBook: {}, entries: [] };
  }

  function filteredEntries() {
    const { entries } = kbData();
    const q = query.trim().toLowerCase();
    return entries.filter(e => {
      if (bookFilter !== 'all' && e.bookId !== bookFilter) return false;
      if (chapterFilter !== 'all' && String(e.chapter) !== String(chapterFilter)) return false;
      if (typeFilter !== 'all' && e.type !== typeFilter) return false;
      if (q) {
        const hay = [e.title, e.summary, e.page, e.section, ...(e.points || []), ...(e.tags || [])].join(' ').toLowerCase();
        if (!hay.includes(q)) return false;
      }
      return true;
    });
  }

  function renderBookShelf(books) {
    if (!books.length) return '<div class="panel"><p>尚未索引任何课本。</p></div>';
    return `<div class="kb-shelf">${books.map(b => `
      <article class="kb-book-card">
        <div class="kb-entry-head">
          <span class="tag">${safeEsc(b.subject)} · ${safeEsc(b.volume)}</span>
          <span class="mu">${safeEsc(b.edition)}</span>
        </div>
        <h3>${safeEsc(b.title)}</h3>
        <p class="mu">${safeEsc(b.publisher)}</p>
        <div class="kb-meta-row">
          <span class="note-v2-pill">目录全收录 · 共 ${safeEsc(b.printedPages)} 页</span>
          <span class="note-v2-pill is-source">精校章：${(b.chaptersIndexed || []).map(c => '第' + c + '章').join('、') || '目录待精校'}</span>
        </div>
      </article>`).join('')}</div>`;
  }

  function renderEntriesView(kb) {
    const list = filteredEntries();
    const chapters = [...new Set(kb.entries.map(e => String(e.chapter)))].sort((a, b) => {
      const na = Number(a), nb = Number(b);
      if (Number.isFinite(na) && Number.isFinite(nb)) return na - nb;
      if (Number.isFinite(na)) return -1;
      if (Number.isFinite(nb)) return 1;
      return a.localeCompare(b, 'zh-CN');
    });
    return `
      <section class="panel">
        <div class="kb-filter-bar">
          <select id="kb-book-filter" aria-label="按课本筛选">
            <option value="all" ${bookFilter === 'all' ? 'selected' : ''}>全部课本</option>
            ${kb.books.map(b => `<option value="${safeEsc(b.id)}" ${bookFilter === b.id ? 'selected' : ''}>${safeEsc(b.shortTitle)} · ${safeEsc(b.subject)}</option>`).join('')}
          </select>
          <select id="kb-chapter-filter" aria-label="按章节筛选">
            <option value="all" ${chapterFilter === 'all' ? 'selected' : ''}>全部精校章</option>
            ${chapters.map(c => `<option value="${safeEsc(c)}" ${chapterFilter === c ? 'selected' : ''}>第 ${safeEsc(c)} 章</option>`).join('')}
          </select>
          <input id="kb-query" type="search" value="${safeEsc(query)}" placeholder="搜索公式、实验、定律、页码…" aria-label="搜索内置知识库">
          <button type="button" data-a="dash-kb-reset">重置</button>
        </div>
        <div class="kb-type-chips" role="group" aria-label="知识条目类型筛选">
          ${Object.entries(TYPE_LABELS).map(([k, lbl]) => `<button type="button" class="${typeFilter === k ? 'on' : ''}" data-a="dash-kb-type" data-type="${k}">${lbl}</button>`).join('')}
        </div>
        <p class="mu">共匹配 <b>${list.length}</b> 条教材权威条目（严格标明教材原书页码；发送新课本 PDF 后会自动扩充入库）。</p>
      </section>
      <div class="kb-entry-list">
        ${list.length ? list.map(e => `
          <article class="kb-entry-card ${focusedEntryId === e.id ? 'is-highlighted' : ''}" id="kb-item-${safeEsc(e.id)}">
            <div class="kb-entry-head">
              <span><span class="kb-entry-type">${safeEsc(TYPE_LABELS[e.type] || e.type)}</span> <span class="note-v2-page-tag">${safeEsc(e.shortTitle)} ${safeEsc(e.page)}</span></span>
              <span>${e.lessonKey ? `<a href="#lesson=${encodeURIComponent(e.lessonKey)}&section=${encodeURIComponent(e.section || '')}">跳转对应精校笔记 →</a>` : ''}</span>
            </div>
            <h4>${rich(e.title)}</h4>
            <p>${rich(e.summary)}</p>
            ${e.tex ? `<div class="tex-block" data-tex="${safeEsc(e.tex)}">${safeEsc(e.tex)}</div>` : ''}
            ${e.points?.length ? `<ul>${e.points.map(p => `<li>${rich(p)}</li>`).join('')}</ul>` : ''}
            ${e.tags?.length ? `<div class="kb-meta-row">${e.tags.map(t => `<span class="tag">${safeEsc(t)}</span>`).join('')}</div>` : ''}
          </article>`).join('') : '<div class="panel"><p>没有找到匹配的教材条目，可放宽筛选条件或切换到“原书目录与页码树”。</p></div>'}
      </div>`;
  }

  function renderTocView(kb) {
    const books = kb.books.filter(b => bookFilter === 'all' || b.id === bookFilter);
    const scopeNames = { sem1_final: '上半年期末', pre_exam: '预试', sem2_final: '毕业考', uec: 'UEC统考' };
    return books.map(b => {
      const toc = kb.tocByBook[b.id] || [];
      return `<section class="panel"><h2>${safeEsc(b.title)} · 完整原书目录（p.1–${safeEsc(b.printedPages)}）</h2>
        <div class="kb-toc-grid">
          ${toc.map(ch => `
            <details class="kb-toc-chapter" ${ch.indexed ? 'open' : ''}>
              <summary>
                <span><b>${typeof ch.chapter === 'number' ? '第 ' + ch.chapter + ' 章' : safeEsc(ch.chapter)} · ${safeEsc(ch.title)}</b> <span class="note-v2-page-tag">${safeEsc(ch.pageRange)}</span> ${ch.indexed ? '<span class="note-v2-pill">已全深度入库</span>' : ''}</span>
                <span>${(ch.examScopes || []).map(sc => `<span class="tag">${scopeNames[sc] || sc}</span>`).join(' ')} ${ch.noteKey && window.LESSONS?.[ch.noteKey] ? `<a href="#lesson=${encodeURIComponent(ch.noteKey)}">查看章节笔记 →</a>` : ''}</span>
              </summary>
              <ul class="kb-toc-sections">
                ${(ch.sections || []).map(sec => `
                  <li>
                    <b>${safeEsc(sec.id)} ${safeEsc(sec.title)}</b> <span class="mu">(${safeEsc(sec.page)})</span>
                    ${sec.subsections?.length ? `<ul>${sec.subsections.map(sub => `<li>${safeEsc(sub.id)} ${safeEsc(sub.title)} <span class="mu">(${safeEsc(sub.page)})</span></li>`).join('')}</ul>` : ''}
                  </li>`).join('')}
                ${ch.extras?.length ? `<li class="mu">本章复习页：${ch.extras.map(ex => safeEsc(ex.title) + ' (' + safeEsc(ex.page) + ')').join(' · ')}</li>` : ''}
              </ul>
            </details>`).join('')}
        </div>
      </section>`;
    }).join('');
  }

  function view() {
    const kb = kbData();
    const totalChapters = Object.values(kb.tocByBook).reduce((n, t) => n + t.length, 0);
    return `
      <div class="page-heading">
        <span class="eyebrow">TEXTBOOK KNOWLEDGE BASE</span>
        <h1>内置教材知识库</h1>
        <p>直接以董总独中官方课本为唯一真实来源：完整收录原书目录页码树，并将精校章的定义、定律、公式、实验与数据表结构化入库。新发送的课本 PDF 会继续自动追加至此库。</p>
      </div>
      <section class="panel">
        <div class="row">
          <span>已接入课本：<b>${kb.books.length}</b> 册 · 收录章/附录：<b>${totalChapters}</b> 项 · 精校知识条目：<b>${kb.entries.length}</b> 条</span>
          <span class="mu">知识库构建日期：${safeEsc(kb.generatedAt || kb.updatedAt || '')}</span>
        </div>
      </section>
      ${renderBookShelf(kb.books)}
      <div class="kb-mode-tabs" role="tablist" aria-label="知识库浏览模式">
        <button type="button" class="${mode === 'entries' ? 'on' : ''}" data-a="dash-kb-mode" data-mode="entries">知识条目检索 (${kb.entries.length})</button>
        <button type="button" class="${mode === 'toc' ? 'on' : ''}" data-a="dash-kb-mode" data-mode="toc">原书目录与页码树 (${totalChapters})</button>
      </div>
      ${mode === 'entries' ? renderEntriesView(kb) : renderTocView(kb)}`;
  }

  function openEntry(entryId) {
    mode = 'entries';
    bookFilter = 'all';
    chapterFilter = 'all';
    typeFilter = 'all';
    query = '';
    focusedEntryId = entryId || '';
    if (typeof window.dashboardGo === 'function') {
      window.dashboardGo('kb');
      requestAnimationFrame(() => document.getElementById('kb-item-' + focusedEntryId)?.scrollIntoView({ block: 'center' }));
    }
  }

  if (typeof document !== 'undefined') {
    document.addEventListener('click', ev => {
      const btn = ev.target.closest('[data-a]');
      if (!btn) return;
      const a = btn.dataset.a;
      if (a === 'dash-kb-mode') {
        mode = btn.dataset.mode || 'entries';
        window.render?.();
      } else if (a === 'dash-kb-type') {
        typeFilter = btn.dataset.type || 'all';
        focusedEntryId = '';
        window.render?.();
      } else if (a === 'dash-kb-reset') {
        bookFilter = 'all';
        chapterFilter = 'all';
        typeFilter = 'all';
        query = '';
        focusedEntryId = '';
        window.render?.();
      } else if (a === 'dash-kb-open') {
        openEntry(btn.dataset.kbid);
      }
    });

    document.addEventListener('change', ev => {
      if (ev.target.id === 'kb-book-filter') {
        bookFilter = ev.target.value;
        window.render?.();
      } else if (ev.target.id === 'kb-chapter-filter') {
        chapterFilter = ev.target.value;
        window.render?.();
      }
    });

    document.addEventListener('input', ev => {
      if (ev.target.id === 'kb-query') {
        query = ev.target.value;
        focusedEntryId = '';
        window.render?.();
        const input = document.getElementById('kb-query');
        if (input) {
          input.focus();
          input.setSelectionRange(query.length, query.length);
        }
      }
    });
  }

  window.KnowledgeBaseUI = { view, openEntry };
})();
