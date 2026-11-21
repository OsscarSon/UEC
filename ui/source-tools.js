/* Lazy utilities for the existing dashboard and source library. */
(() => {
  const moduleCache = new Map();
  const stylesheet = 'vendor/source-tools/notifications.css';
  const noticeQueue = [];
  let fuse, notifications, pendingNotices, tabMotion, previousTab;
  const fuzzyIndexes = new WeakMap();

  function load(name) {
    if (!moduleCache.has(name)) {
      const task = import(`../vendor/source-tools/${name}.js`).catch(error => {
        moduleCache.delete(name);
        throw error;
      });
      moduleCache.set(name, task);
    }
    return moduleCache.get(name);
  }

  function prepareSearch(onReady) {
    if (!fuse) load('fuzzy').then(module => { fuse = module.Fuse; onReady(); }).catch(() => {});
  }

  const normalize = value => String(value ?? '').normalize('NFKC').toLocaleLowerCase().trim();
  function find(query, entries, keys, limit = 100) {
    const term = normalize(query);
    if (!term) return {rows: [], total: 0};
    const exact = [];
    const matched = new Set();
    const numbered = /^\d+(?:\.\d+)+$/.test(term);
    for (const entry of entries) {
      const fields = keys.map(key => normalize(entry[key]));
      if (fields.some(field => numbered ? field === term : field.includes(term))) {
        exact.push(entry);
        matched.add(entry);
      }
    }
    // IDs are literal and short queries are too ambiguous for approximate matches.
    if (!fuse || term.length < 3 || /^\d/.test(term) || exact.length >= limit) {
      return {rows: exact.slice(0, limit), total: exact.length};
    }
    if (!fuzzyIndexes.has(entries)) {
      const index = new fuse(entries, {
        keys, threshold: 0.34, ignoreLocation: true, minMatchCharLength: 2,
        getFn: (row, path) => normalize(row[path.join('.')]),
      });
      fuzzyIndexes.set(entries, index);
    }
    const fuzzy = fuzzyIndexes.get(entries).search(term).map(result => result.item).filter(row => !matched.has(row));
    return {rows: [...exact, ...fuzzy].slice(0, limit), total: exact.length + fuzzy.length};
  }

  function notify(message, type, fallback) {
    if (notifications) {
      notifications.notify(message, type);
      return;
    }
    noticeQueue.push({message, type, fallback});
    if (pendingNotices) return;
    if (!document.querySelector(`link[href="${stylesheet}"]`)) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = stylesheet;
      document.head.append(link);
    }
    pendingNotices = load('notifications').then(module => {
      notifications = module;
      noticeQueue.splice(0).forEach(item => module.notify(item.message, item.type));
    }).catch(() => {
      noticeQueue.splice(0).forEach(item => item.fallback(item.message));
    }).finally(() => { pendingNotices = null; });
  }

  function animateTabs(nav, group) {
    if (!nav || matchMedia('(prefers-reduced-motion: reduce)').matches) {
      previousTab = null;
      return;
    }
    const active = nav.querySelector('[aria-current="page"]');
    const start = previousTab;
    const position = () => ({x: active.offsetLeft, y: active.offsetTop, width: active.offsetWidth, height: active.offsetHeight});
    previousTab = {group, id: active.hash, ...position()};
    if (!start || start.group !== group || start.id === active.hash) return;
    const slide = () => {
      if (!nav.isConnected || !active.isConnected) return;
      const end = position();
      const indicator = document.createElement('span');
      indicator.className = 'workspace-tab-indicator';
      indicator.setAttribute('aria-hidden', 'true');
      indicator.style.width = `${end.width}px`;
      indicator.style.height = `${end.height}px`;
      nav.prepend(indicator);
      nav.classList.add('is-sliding');
      const transform = p => `translate(${p.x}px,${p.y}px) scale(${p.width / end.width},${p.height / end.height})`;
      tabMotion.animate(indicator, {transform: [transform(start), transform(end)]}, {duration: 0.23, ease: [0.22, 1, 0.36, 1]})
        .then(() => { nav.classList.remove('is-sliding'); indicator.remove(); });
    };
    if (tabMotion) slide();
    else load('tabs').then(module => { tabMotion = module; slide(); }).catch(() => {});
  }
  window.SourceTools = {load, prepareSearch, find, notify, animateTabs};
})();
