import {build} from 'esbuild';
import {existsSync, mkdirSync, readFileSync, writeFileSync} from 'node:fs';

const folder = 'vendor/source-tools';
mkdirSync(folder, {recursive: true});
const entries = {
  'fuzzy': 'export {default as Fuse} from "fuse.js";',
  'tabs': 'export {animate} from "motion/mini";',
  'zip': 'export {ZipReader, BlobReader, BlobWriter} from "@zip.js/zip.js/index-native.js";',
  'notifications': 'export {notify} from "./tools-src/study-notifications.jsx";',
};
for (const [name, contents] of Object.entries(entries)) {
  await build({stdin: {contents, resolveDir: process.cwd()}, outfile: `${folder}/${name}.js`,
    bundle: true, minify: true, format: 'esm', target: 'es2020', legalComments: 'linked',
    define: {'process.env.NODE_ENV': '"production"'}});
}
const packages = ['fuse.js', 'motion', 'framer-motion', 'motion-dom', 'motion-utils', 'sonner', '@zip.js/zip.js', 'react', 'react-dom', 'scheduler'];
const notices = packages.map(name => {
  const directory = `node_modules/${name}`;
  const pkg = JSON.parse(readFileSync(`${directory}/package.json`, 'utf8'));
  const license = ['LICENSE', 'LICENSE.md', 'LICENSE.txt'].find(file => existsSync(`${directory}/${file}`));
  if (!license) throw new Error(`Missing license for ${name}`);
  return `## ${name} ${pkg.version}\n\n${readFileSync(`${directory}/${license}`, 'utf8').trim()}\n`;
});
writeFileSync(`${folder}/LICENSES.md`, '# Source library and dashboard components\n\n' + notices.join('\n'));
