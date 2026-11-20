// Export the note sections actually registered by index.html, using the site's script order.
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const assert = require('node:assert/strict');
const root = path.join(__dirname, '..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const html = read('index.html');
const context = vm.createContext({STUDY_FORMULAS: {}});
context.window = context;
const curriculum = JSON.parse(html.match(/^const D=(\[.*?\]);/m)[1]);
for (const [, file] of html.matchAll(/<script src="(lessons\/[^"\s]+\.js)"/g)) {
  vm.runInContext(read(file), context, {filename: file});
}
const {LESSONS, BATCH_NOTES} = context.window;
const initializedFields = ['goals','prerequisites','flow','deep','derive','examples','exam','error_analysis','practice','quick','quiz'];
const records = [];
for (const [subject, volume, chapter, title] of curriculum) {
  const key = subject + chapter;
  const lesson = LESSONS[key];
  if (!lesson) continue;
  for (const section of lesson.sections) {
    const note = BATCH_NOTES[key]?.[section.id];
    assert.ok(note, `Missing module payload ${key}/${section.id}`);
    const missing = initializedFields.filter(field => !note[field] || Array.isArray(note[field]) && !note[field].length);
    assert.equal(note.section_id || section.id, section.id);
    assert.equal(Number(note.chapter_id || chapter), chapter);
    records.push({subject, volume, chapter, title, id: section.id, section: section.t,
      batch: note.content_batch || 'legacy', missing, bookPage: '', status: '待新上传课本原页核对'});
  }
}
assert.equal(records.length, Object.values(BATCH_NOTES).reduce((n, sections) => n + Object.keys(sections).length, 0));
const csv = value => `"${String(value).replace(/"/g, '""')}"`;
const columns = ['科目','网站册别','章号','章名','小节编号','小节名','笔记批次','现有结构缺字段','课本原页','教材核对状态'];
const rows = records.map(row => [row.subject,row.volume,row.chapter,row.title,row.id,row.section,row.batch,row.missing.join(';'),row.bookPage,row.status]);
fs.writeFileSync(path.join(root,'reports/textbook-review/NOTE_INVENTORY.csv'), '\ufeff' + [columns,...rows].map(row => row.map(csv).join(',')).join('\n') + '\n');
console.log(`Registered notes: ${Object.keys(LESSONS).length} chapters, ${records.length} sections. Required field gaps: ${records.filter(r => r.missing.length).length}. Textbook page matches: 0.`);
