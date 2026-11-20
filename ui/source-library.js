/* Index official/college exam sources and read the user's PDFs and photos locally. */
(() => {
  const store = SourceLibraryStore;
  const escape = value => esc(String(value ?? ''));
  const subjects = {biology: '生物', chemistry: '化学', physics: '物理', math: '高数'};
  const accepted = {pdf: 'application/pdf', jpg: 'image/jpeg', jpeg: 'image/jpeg', png: 'image/png', webp: 'image/webp', avif: 'image/avif'};
  const collator = new Intl.Collator('zh-CN', {numeric: true});
  const filters = {
    textbooks: {subject: '', query: '', page: 1},
    'past-papers': {type: '', year: '', query: '', page: 1},
  };
  const pageSize = 24;
  const maxFileBytes = 512 * 1024 ** 2;
  let local = [], loading, ready = false, busy = false, message = '', storageError = false;
  let archive, sourceByHash, sourceSizes, previewVersion = 0, previewUrl;
  const nameOnly = path => path.split(/[\\/]/).at(-1);
  function extension(name) {
    const normalized = nameOnly(name).normalize('NFKC').trim().toLowerCase();
    return normalized.replace(/(\.pdf)\s*\((?:副本|copy|\d+)\)$/, '$1').split('.').at(-1);
  }
  const categoryName = code => MATH_EXAM_RESEARCH.exam_types.find(type => type.exam_type === code)?.title || code;

  function paperCatalog() {
    if (archive) return archive;
    archive = MATH_EXAM_RESEARCH.inventory.map(source => {
      const annual = MATH_HEAT.exam_types.find(type => type.exam_type === source.exam_type)?.annual.find(row => row.year === source.year);
      return {...source, category: categoryName(source.exam_type), status: annual?.status, year_label: String(source.year)};
    }).sort((a, b) => b.year - a.year || collator.compare(a.filename, b.filename));
    sourceByHash = new Map(archive.map(source => [source.sha256, source]));
    sourceSizes = new Set(archive.map(source => source.bytes));
    return archive;
  }

  const labels = {
    textbooks: {title: '课本资料', description: '按科目和册别收纳课本 PDF 与拍照页。'},
    'past-papers': {title: '历届考试资料', description: '按类别和年份查找历届原卷，查看来源页与核验状态。'},
  };
  const options = (rows, selected) => rows.map(([value, label]) =>
    `<option value="${escape(value)}"${String(value) === selected ? ' selected' : ''}>${escape(label)}</option>`).join('');
  function view(mode) {
    const isBook = mode === 'textbooks';
    const filter = filters[mode];
    if (!isBook) paperCatalog();
    return `<div class="page-heading"><h1>${labels[mode].title}</h1><p>${labels[mode].description}</p></div>
      <section class="panel source-library" data-source-library="${mode}">
        <div class="panel-heading"><h2>${isBook ? '我的课本' : '高数原卷目录'}</h2>
          ${isBook ? '' : '<a href="#view=mock&mode=research">查看逐题核验与统计 →</a>'}
        </div>
        <div class="source-filters">
          ${isBook ? `<label>科目<select data-source-filter="subject">${options([['', '全部科目'], ...Object.entries(subjects)], filter.subject)}</select></label>`
            : `<label>考试类别<select data-source-filter="type">${options([['', '全部类别'], ...MATH_EXAM_RESEARCH.exam_types.map(s => [s.exam_type, s.title])], filter.type)}</select></label>
               <label>年份<select data-source-filter="year">${options([['', '全部年份'], ...[...new Set(archive.map(s => s.year))].map(y => [y, y])], filter.year)}</select></label>`}
          <label>搜索<input type="search" data-source-filter="query" value="${escape(filter.query)}" placeholder="${isBook ? '名称、册别或文件名' : '试卷名、类别或年份'}"></label>
        </div>
        <p class="muted" data-source-storage></p>
        <div data-source-results aria-busy="true"></div>
        <details class="source-import" ${isBook && !local.some(item => item.kind === 'textbook') ? 'open' : ''}>
          <summary>${isBook ? '导入课本 ZIP、PDF 或照片' : '导入原卷 PDF 或原卷 ZIP'}</summary>
          <p>${isBook ? '为本次文件选择科目和册别。照片按文件名数字顺序排列。' : '导入后按 SHA-256 匹配目录中的 47 份原卷。文件名更改也能匹配。'}</p>
          <form data-source-import>
            ${isBook ? `<label>科目<select name="subject">${options(Object.entries(subjects), filter.subject || 'biology')}</select></label>
              <label>册别（可选）<input name="volume" maxlength="80" placeholder="例如 高一上册"></label>` : ''}
            <label>选择文件<input name="files" type="file" multiple required accept="${isBook ? '.zip,.pdf,.jpg,.jpeg,.png,.webp,.avif' : '.zip,.pdf'}"></label>
            <button class="primary" type="submit">保存到本机</button>
          </form>
          <p class="muted">原文件保存在当前浏览器。换设备或清除网站数据后需重新导入。</p>
          <p data-source-message role="status">${escape(message)}</p>
        </details>
      </section>`;
  }

  function mount() {
    const panel = document.querySelector('[data-source-library]');
    if (!panel) return;
    rememberExamLink(panel);
    draw(panel);
    SourceTools.prepareSearch(() => { if (panel.isConnected) draw(panel); });
    if (ready || loading) return;
    loading = refresh().then(() => {
      const visible = document.querySelector('[data-source-library]');
      if (visible) draw(visible);
    }).finally(() => { loading = null; });
  }

  async function refresh() {
    try {
      local = await store.list();
      storageError = false;
    } catch {
      storageError = true;
    }
    ready = true;
  }

  function rememberExamLink(panel) {
    if (panel.dataset.sourceLibrary !== 'past-papers') return;
    const source = new URLSearchParams(location.hash.slice(1)).get('source');
    if (!source || !archive.some(item => item.source_id === source)) return;
    filters['past-papers'].query = source;
    filters['past-papers'].type = '';
    filters['past-papers'].year = '';
    filters['past-papers'].page = 1;
    panel.querySelector('[data-source-filter="query"]').value = source;
    panel.querySelector('[data-source-filter="type"]').value = '';
    panel.querySelector('[data-source-filter="year"]').value = '';
  }

  function draw(panel) {
    const mode = panel.dataset.sourceLibrary;
    const filter = filters[mode];
    const isBook = mode === 'textbooks';
    const textbooks = local.filter(item => item.kind === 'textbook');
    const available = new Set(local.filter(item => item.kind === 'paper').map(item => item.id));
    const listing = isBook ? textbooks.filter(item => !filter.subject || item.subject === filter.subject)
      .sort((a, b) => collator.compare(a.volume, b.volume) || collator.compare(a.path, b.path))
      : archive.filter(item => (!filter.type || item.exam_type === filter.type) && (!filter.year || item.year_label === filter.year));
    const keys = isBook ? ['name', 'volume', 'path'] : ['filename', 'category', 'year_label', 'source_id'];
    const exactSource = !isBook && listing.find(item => item.source_id === filter.query.trim());
    const matches = exactSource ? [exactSource] : filter.query.trim() ? SourceTools.find(filter.query, listing, keys, listing.length).rows : listing;
    const results = panel.querySelector('[data-source-results]');
    const pages = Math.max(1, Math.ceil(matches.length / pageSize));
    filter.page = Math.min(filter.page, pages);
    const visible = matches.slice((filter.page - 1) * pageSize, filter.page * pageSize);
    const count = isBook ? `本机 ${textbooks.length} 份课本文件` : `${archive.length} 份目录 · 本机已匹配 ${available.size} 份`;
    panel.querySelector('[data-source-storage]').textContent = storageError ? '浏览器无法读取本地资料。请检查网站储存权限。' : count;
    const status = panel.querySelector('[data-source-message]');
    status.textContent = message;
    panel.querySelectorAll('form input, form select, form button').forEach(control => { control.disabled = busy || storageError; });
    results.setAttribute('aria-busy', String(!ready));
    results.innerHTML = visible.length ? `<ul class="source-list">${visible.map(item => isBook ? bookRow(item) : examRow(item, available)).join('')}</ul>`
      + (pages > 1 ? `<nav class="source-pagination" aria-label="资料分页"><button data-source-page="-1" ${filter.page === 1 ? 'disabled' : ''}>上一页</button>
        <span>${filter.page} / ${pages} · ${matches.length} 份</span><button data-source-page="1" ${filter.page === pages ? 'disabled' : ''}>下一页</button></nav>` : '')
      : `<p class="source-empty">${!ready ? '正在读取本机资料…' : filter.query ? '没有符合关键词的资料。' : isBook ? '还没有课本文件，可在下方导入。' : '此类别或年份没有所供原卷。'}</p>`;
  }

  function bookRow(item) {
    return `<li><div class="source-row-copy"><b>${escape(item.name)}</b><small>${escape(subjects[item.subject])} · ${escape(item.volume || '未填册别')}${item.path === item.name ? '' : ' · ' + escape(item.path)}</small></div>
      <button data-source-open="${escape(item.id)}">阅读</button></li>`;
  }

  function examRow(item, available) {
    const annual = item.status === 'year_unconfirmed' ? ' · 年份待核' : item.status === 'partial_paper' ? ' · 卷别不全' : '';
    const params = new URLSearchParams(location.hash.slice(1));
    const page = params.get('source') === item.source_id ? Number(params.get('page')) : 0;
    const pdfPage = Number.isInteger(page) && page > 0 && page <= item.pages ? page : 1;
    const label = item.year === 2026 ? `${item.year} 新制` : item.year;
    return `<li><div class="source-row-copy"><b>${escape(item.filename)}</b><small>${escape(item.category)} · ${label} · ${item.pages} 页${annual}</small></div>
      ${available.has(item.source_id) ? `<button data-source-open="${escape(item.source_id)}" data-source-pdf-page="${pdfPage}">阅读原卷</button>`
        : `<button data-source-import-link>导入原卷</button>`}
      <button data-source-evidence="${escape(item.source_id)}">来源</button></li>`;
  }

  async function* archiveFiles(file, prefix = '', depth = 0) {
    const {ZipReader, BlobReader, BlobWriter} = await SourceTools.load('zip');
    const zip = new ZipReader(new BlobReader(file), {useWebWorkers: false, checkSignature: true});
    try {
      for await (const entry of zip.getEntriesGenerator()) {
        const ext = extension(entry.filename);
        if (entry.directory || entry.filename.includes('__MACOSX/') || nameOnly(entry.filename).startsWith('.')) continue;
        const nested = ext === 'zip' && depth === 0;
        if (!nested && !Object.hasOwn(accepted, ext)) continue;
        const path = prefix + entry.filename;
        let blob = null;
        if (entry.uncompressedSize <= maxFileBytes && !entry.encrypted) {
          try { blob = await entry.getData(new BlobWriter(nested ? 'application/zip' : accepted[ext])); }
          catch { /* The import summary counts the unreadable entry. */ }
        }
        if (nested && blob) {
          yield* archiveFiles(blob, path + '/', depth + 1);
        } else {
          yield {path, blob};
        }
      }
    } finally {
      await zip.close();
    }
  }

  async function* filesFrom(picked) {
    for (const file of picked) {
      if (extension(file.name) === 'zip') yield* archiveFiles(file);
      else yield {path: file.name, blob: file};
    }
  }

  function headerMatches(ext, h) {
    const ascii = (start, end) => String.fromCharCode(...h.slice(start, end));
    if (ext === 'pdf') return ascii(0, 5) === '%PDF-';
    if (ext === 'jpg' || ext === 'jpeg') return h[0] === 255 && h[1] === 216 && h[2] === 255;
    if (ext === 'png') return h[0] === 137 && ascii(1, 4) === 'PNG';
    if (ext === 'webp') return ascii(0, 4) === 'RIFF' && ascii(8, 12) === 'WEBP';
    return ascii(4, 8) === 'ftyp' && /^avi[fs]$/.test(ascii(8, 12));
  }

  async function importFiles(form) {
    if (busy) return;
    const panel = form.closest('[data-source-library]');
    const isBook = panel.dataset.sourceLibrary === 'textbooks';
    const {subject, volume, files} = form.elements;
    const book = isBook ? {subject: subject.value, volume: volume.value.trim()} : null;
    const picked = [...files.files];
    const seen = new Set(local.map(item => item.id));
    let added = 0, skipped = 0;
    busy = true;
    message = '正在读取资料…';
    draw(panel);
    try {
      for await (const {path, blob} of filesFrom(picked)) {
        const name = nameOnly(path), ext = extension(name), type = accepted[ext];
        if (!blob || blob.size > maxFileBytes || !Object.hasOwn(accepted, ext) || !isBook && (ext !== 'pdf' || !sourceSizes.has(blob.size))
          || !headerMatches(ext, new Uint8Array(await blob.slice(0, 16).arrayBuffer()))) {
          skipped++;
          continue;
        }
        const digest = await crypto.subtle.digest('SHA-256', await blob.arrayBuffer());
        const hash = [...new Uint8Array(digest)].map(byte => byte.toString(16).padStart(2, '0')).join('');
        const source = isBook ? null : sourceByHash.get(hash);
        if (!isBook && !source) { skipped++; continue; }
        const id = isBook ? `textbook:${JSON.stringify([book.subject, book.volume, hash])}` : source.source_id;
        if (seen.has(id)) { skipped++; continue; }
        const item = {id, kind: isBook ? 'textbook' : 'paper', name, path, type, ...book};
        await store.put(item, blob.slice(0, blob.size, type));
        seen.add(id);
        added++;
        panel.querySelector('[data-source-message]').textContent = `已保存 ${added} 份…`;
      }
      message = `已保存 ${added} 份${skipped ? `，跳过 ${skipped} 份重复或不适用文件` : ''}。`;
      studyToast(message, added ? 'success' : 'info');
      files.value = '';
    } catch (error) {
      message = `已保存 ${added} 份。导入中断，${error.name === 'QuotaExceededError' ? '浏览器储存空间不足' : '请检查压缩包及浏览器储存权限'}。`;
      studyToast(message, 'error');
    } finally {
      await refresh();
      busy = false;
      const visible = document.querySelector('[data-source-library]');
      if (visible) draw(visible);
    }
  }

  function dialog() {
    let element = document.getElementById('source-preview');
    if (element) return element;
    element = document.createElement('dialog');
    element.id = 'source-preview';
    element.setAttribute('aria-labelledby', 'source-preview-title');
    element.addEventListener('close', () => {
      previewVersion++;
      clearPreviewUrl();
      element.replaceChildren();
    });
    document.body.append(element);
    return element;
  }

  function clearPreviewUrl() {
    if (previewUrl) URL.revokeObjectURL(previewUrl);
    previewUrl = null;
  }

  function show(title, body) {
    const element = dialog();
    element.innerHTML = `<header><h2 id="source-preview-title">${escape(title)}</h2><button type="button" data-source-close autofocus>关闭</button></header>${body}`;
    if (!element.open) element.showModal();
    return element;
  }

  async function open(id, page) {
    const ticket = ++previewVersion;
    const item = local.find(row => row.id === id);
    if (!item) return studyToast('请先导入这份原卷。');
    const element = show(item.name, '<p role="status">正在打开…</p>');
    try {
      const blob = await store.read(id);
      if (ticket !== previewVersion || !element.open) return;
      if (!blob) throw Error('找不到资料');
      clearPreviewUrl();
      previewUrl = URL.createObjectURL(blob);
      const pdf = item.type === 'application/pdf';
      const url = previewUrl + (pdf && page ? `#page=${page}` : '');
      const siblings = pdf ? [] : local.filter(row => row.kind === 'textbook' && row.type !== 'application/pdf' && row.subject === item.subject && row.volume === item.volume)
        .sort((a, b) => collator.compare(a.path, b.path));
      const index = siblings.indexOf(item);
      const controls = `<div class="source-preview-actions"><a href="${url}" target="_blank" rel="noopener">新标签打开</a>
        <a href="${previewUrl}" download="${escape(item.name)}">下载原文件</a>
        <button data-source-delete="${escape(item.id)}">移除本机副本</button></div>`;
      const paging = siblings.length > 1 ? `<nav class="source-pagination" aria-label="课本照片翻页"><button data-source-open="${escape(siblings[index - 1]?.id)}" ${index === 0 ? 'disabled' : ''}>上一张</button>
        <span>${index + 1} / ${siblings.length}</span><button data-source-open="${escape(siblings[index + 1]?.id)}" ${index === siblings.length - 1 ? 'disabled' : ''}>下一张</button></nav>` : '';
      show(item.name, controls + paging + (pdf ? `<iframe src="${url}" title="${escape(item.name)}"></iframe>` : `<img src="${url}" alt="${escape(item.name)}">`));
    } catch {
      if (ticket === previewVersion) show(item.name, '<p role="alert">无法读取本机副本，请重新导入。</p>');
    }
  }

  function evidence(id) {
    const item = archive.find(source => source.source_id === id);
    if (!item) return;
    ++previewVersion;
    clearPreviewUrl();
    const ready = local.some(row => row.id === id);
    show(item.filename, `<p>${escape(item.category)} · 来源标年 ${item.year} · ${item.pages} 个 PDF 页面</p>
      <dl class="source-evidence"><dt>来源 ID</dt><dd>${escape(id)}</dd><dt>SHA-256</dt><dd>${escape(item.sha256)}</dd></dl>
      <p>文件指纹用于核对本机副本。逐题、答案和年份的核验边界见研究报告。</p>
      <div class="source-preview-actions"><a href="reports/math-exams/GAP_REGISTER.json" target="_blank" rel="noopener">逐份核验缺口</a>
      ${ready ? `<button data-source-open="${escape(id)}">阅读原卷</button>` : '<button data-source-import-link>导入匹配原卷</button>'}</div>`);
  }

  document.addEventListener('input', event => {
    const panel = event.target.closest('[data-source-library]');
    const field = event.target.dataset.sourceFilter;
    if (!panel || !field) return;
    const filter = filters[panel.dataset.sourceLibrary];
    if (panel.dataset.sourceLibrary === 'past-papers' && new URLSearchParams(location.hash.slice(1)).has('source')) {
      history.replaceState(null, '', '#view=past-papers');
    }
    filter[field] = event.target.value;
    filter.page = 1;
    draw(panel);
  });
  document.addEventListener('submit', event => {
    if (!event.target.matches('[data-source-import]')) return;
    event.preventDefault();
    importFiles(event.target);
  });
  document.addEventListener('click', async event => {
    const button = event.target.closest('button');
    if (!button) return;
    const data = button.dataset;
    const panel = document.querySelector('[data-source-library]');
    if (data.sourceOpen) open(data.sourceOpen, Number(data.sourcePdfPage) || undefined);
    if (data.sourceEvidence) evidence(data.sourceEvidence);
    if (data.sourceClose !== undefined) dialog().close();
    if (data.sourceImportLink !== undefined && panel) {
      if (dialog().open) dialog().close();
      panel.querySelector('.source-import').open = true;
      panel.querySelector('[name="files"]').focus();
    }
    if (data.sourcePage && panel) {
      filters[panel.dataset.sourceLibrary].page += Number(data.sourcePage);
      draw(panel);
      panel.querySelector('[data-source-results] button')?.focus();
    }
    if (data.sourceDelete && confirm('移除本机副本？你仍可重新导入原文件。')) {
      try {
        await store.remove(data.sourceDelete);
        await refresh();
        dialog().close();
        if (panel?.isConnected) draw(panel);
        studyToast('已移除本机副本', 'success');
      } catch { studyToast('移除失败，请重试', 'error'); }
    }
  });
  window.SourceLibrary = {view, mount};
})();
