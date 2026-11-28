# UEC Project Rules for AI Agents

1. **Direct Push to `main`**
   - Always commit and push directly to `origin main` (never create PRs or feature branches unless explicitly asked).
   - Always pass explicit git author identity on commit/merge commands:
     `git -c user.name="OsscarSon" -c user.email="116643016+OsscarSon@users.noreply.github.com"`

2. **One-Command Build, Test & Push**
   - After editing `data/notes-v2/*.json`, `data/knowledge-base/**`, or `assets/fig/v2/*.svg`, run:
     `node tools/ship.mjs "<commit message>"`
   - This rebuilds `notes-v2-bundle.js` and `kb-bundle.js`, runs `tests/notes-v2-kb.cjs` and `tests/arch-cleanup.cjs`, stages repo files, commits, and pushes directly to `origin main`.

3. **Windows Antigravity Terminal Stability**
   - Python 3.12, PyMuPDF (`fitz`), and Node.js are ALREADY installed on this machine.
   - NEVER run `pip install` or slow commands that fall into background tasks (background tasks trigger a Windows Antigravity `Command failed to run: Access is denied..` lockup).
   - Keep every `run_command` fast and synchronous (`WaitMsBeforeAsync: 10000`), and batch shell steps into one command when possible.

4. **Strict KaTeX Authoring Rules (Zero Strict-Mode Errors)**
   - `tests/notes-v2-kb.cjs` compiles every TeX expression with `strict: 'error'`.
   - NEVER put `_`, `^`, `\cdot`, or `℃` inside `\text{...}` (e.g., NEVER write `\text{ mol H_2O}`, `\text{ mol\ L^{-1}}`, `\text{ m^3}`, `\text{℃}`).
   - Always write `\ \mathrm{mol\ H_2O}`, `\ \mathrm{mol\cdot L^{-1}}`, `\ \mathrm{m^3}`, `^\circ\mathrm{C}`.
   - Always verify balanced braces `{ }` in every `\(...\)` and `tex` field.

5. **Strict Knowledge Base & Note V2 Schema**
   - Valid KB entry `"type"` values are ONLY: `definition`, `law`, `formula`, `constant`, `experiment`, `table` (NEVER `"mechanism"`).
   - Every Note V2 section must have >= 3 `concepts`, >= 2 `formulas`, >= 2 `pitfalls`, >= 2 `examples`, >= 4 `practice` questions (covering `L1`–`L4`, using `"ans"` rather than `"answer"`), >= 3 `cheatSheet` items, and `quiz.q` + `quiz.ans`.

6. **Protected Data & Repo Hygiene**
   - NEVER modify `const D=[...]` in `index.html`.
   - NEVER commit `.pdf` files, temporary screenshots, or scratch artifacts into git (only bespoke vector diagrams in `assets/fig/v2/`).
