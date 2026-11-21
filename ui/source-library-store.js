/* Local blobs stay in a separate database from learning progress and cloud backups. */
(() => {
  let connection;
  function database() {
    if (!connection) {
      connection = new Promise((resolve, reject) => {
        const request = indexedDB.open('uec-source-library', 1);
        request.onupgradeneeded = () => {
          request.result.createObjectStore('catalog', {keyPath: 'id'});
          request.result.createObjectStore('files');
        };
        request.onsuccess = () => {
          const db = request.result;
          db.onversionchange = () => { db.close(); connection = null; };
          resolve(db);
        };
        request.onerror = () => reject(request.error);
      }).catch(error => { connection = null; throw error; });
    }
    return connection;
  }

  async function transaction(stores, mode, operation) {
    const db = await database();
    return new Promise((resolve, reject) => {
      const tx = db.transaction(stores, mode);
      const request = operation(tx);
      tx.oncomplete = () => resolve(request?.result);
      tx.onabort = () => reject(tx.error || new Error('资料写入中断'));
    });
  }

  const list = () => transaction(['catalog'], 'readonly', tx => tx.objectStore('catalog').getAll());
  const read = id => transaction(['files'], 'readonly', tx => tx.objectStore('files').get(id));
  const put = (item, blob) => transaction(['catalog', 'files'], 'readwrite', tx => {
    tx.objectStore('catalog').put(item);
    tx.objectStore('files').put(blob, item.id);
  });
  const remove = id => transaction(['catalog', 'files'], 'readwrite', tx => {
    tx.objectStore('catalog').delete(id);
    tx.objectStore('files').delete(id);
  });
  window.SourceLibraryStore = {list, read, put, remove};
})();
