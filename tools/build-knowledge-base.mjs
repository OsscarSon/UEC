/* Build bundled browser Knowledge Base from canonical data/knowledge-base/ JSON files. */
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const kbDir = path.join(root, 'data', 'knowledge-base');
const manifestPath = path.join(kbDir, 'manifest.json');
const outDir = path.join(root, 'vendor', 'knowledge-base');
const outFile = path.join(outDir, 'kb-bundle.js');

const VALID_TYPES = new Set(['definition', 'law', 'formula', 'constant', 'experiment', 'table']);

function assert(cond, msg) {
  if (!cond) throw new Error(`[build-kb] ${msg}`);
}

const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
assert(Array.isArray(manifest.books) && manifest.books.length > 0, 'manifest.books must be a non-empty array');

const books = [];
const tocByBook = {};
const allEntries = [];
const seenIds = new Set();

for (const meta of manifest.books) {
  const filePath = path.join(kbDir, meta.dataFile);
  assert(fs.existsSync(filePath), `Missing book data file: ${meta.dataFile}`);
  const payload = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  assert(payload.book && payload.book.id === meta.id, `Book metadata id mismatch in ${meta.dataFile}`);
  assert(Array.isArray(payload.toc) && payload.toc.length > 0, `Missing toc array in ${meta.dataFile}`);
  assert(Array.isArray(payload.entries), `Missing entries array in ${meta.dataFile}`);

  books.push(payload.book);
  tocByBook[meta.id] = payload.toc;

  for (const entry of payload.entries) {
    assert(entry.id && typeof entry.id === 'string', `Entry missing string id in ${meta.dataFile}`);
    assert(!seenIds.has(entry.id), `Duplicate KB entry id: ${entry.id}`);
    seenIds.add(entry.id);
    assert(VALID_TYPES.has(entry.type), `Invalid KB entry type "${entry.type}" on ${entry.id}`);
    assert(entry.bookId === meta.id, `Entry ${entry.id} bookId mismatch`);
    assert(entry.title && entry.summary && entry.page, `Entry ${entry.id} missing title/summary/page`);
    allEntries.push({
      ...entry,
      shortTitle: payload.book.shortTitle,
      bookTitle: payload.book.title,
      subject: payload.book.subject,
      courseCode: payload.book.courseCode
    });
  }
}

const entriesByLesson = {};
const entriesBySection = {};
for (const entry of allEntries) {
  if (entry.lessonKey) {
    entriesByLesson[entry.lessonKey] = entriesByLesson[entry.lessonKey] || [];
    entriesByLesson[entry.lessonKey].push(entry);
    if (entry.section) {
      const secKey = `${entry.lessonKey}/${entry.section}`;
      entriesBySection[secKey] = entriesBySection[secKey] || [];
      entriesBySection[secKey].push(entry);
    }
  }
}

fs.mkdirSync(outDir, { recursive: true });
const bundle = {
  schemaVersion: manifest.schemaVersion || 1,
  updatedAt: manifest.updatedAt,
  generatedAt: new Date().toISOString().slice(0, 10),
  books,
  tocByBook,
  entries: allEntries,
  entriesByLesson,
  entriesBySection
};

const js = `/* Generated from data/knowledge-base/ by tools/build-knowledge-base.mjs. Do not edit manually. */\nwindow.UEC_KNOWLEDGE_BASE = ${JSON.stringify(bundle)};\n`;
fs.writeFileSync(outFile, js, 'utf8');
console.log(`Built ${path.relative(root, outFile)} (${books.length} books, ${allEntries.length} KB entries).`);
