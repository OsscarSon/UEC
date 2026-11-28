/* One-command build, verify, commit, and direct push to origin main. */
import { execFileSync } from 'node:child_process';

const msg = process.argv[2] || 'chore: build, verify and publish updates';
const gitIdentity = [
  '-c', 'user.name=OsscarSon',
  '-c', 'user.email=116643016+OsscarSon@users.noreply.github.com'
];

function run(cmd, args) {
  console.log(`\n> ${cmd} ${args.join(' ')}`);
  execFileSync(cmd, args, { stdio: 'inherit' });
}

run('node', ['tools/build-notes-v2.mjs']);
run('node', ['tools/build-knowledge-base.mjs']);
run('node', ['tests/notes-v2-kb.cjs']);
run('node', ['tests/arch-cleanup.cjs']);
run('git', ['add', 'data', 'assets/fig/v2', 'vendor', 'tests', 'tools', 'AGENTS.md']);

try {
  execFileSync('git', ['diff', '--cached', '--quiet']);
  console.log('\nNo staged changes to commit.');
} catch {
  run('git', [...gitIdentity, 'commit', '-m', msg]);
}

run('git', ['push', 'origin', 'main']);
console.log('\nDONE: Built, verified, committed, and pushed to origin main.');
