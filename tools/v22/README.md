# V22 import and verification

Run from the repository root. No image-generation service is used.

1. `python tools/v22/build.py` verifies input hashes, applies the recorded deterministic SVG fixes and writes the per-image decisions from `decisions.tsv`.
2. `python tools/v22/finalize.py` binds only existing subsections, builds the runtime allowlist and all142 task comparisons from `task-links.tsv`. It updates current renderer hashes in the existing master manifests without changing the original142 prompt JSON.
3. `python tests/v22_audit.py` verifies provenance, live course identity, baseline protection, sample calculations, atom/charge balances and edited vector/membrane geometry. It does not certify all scientific claims automatically.
4. `node tools/v22/layout.cjs` checks native and transformed SVG text bounds; any detected clipping fails the command.
5. Serve locally: `python3 -m http.server 8022`. Then run `UEC_TEST_BASE=http://localhost:8022/ node tests/v22_browser.cjs` for all selected assets, zoom interactions, resource rendering and representative light/dark screenshots.
6. `node tools/v22/contact-sheets.cjs` renders every input independently using an `img`, avoiding shared marker/clip IDs. It writes temporary PNG sheets. Convert them to `reports/v22/contact-sheets/NN.webp` using Pillow before removing the temporary PNGs; the index and per-image records reference WebP.
7. `python tools/v22/write_reports.py` summarizes already-passed reports into the delivery and mapping documents. It does not run tests or promote a scientific decision.

Keep `illustrations/v22/original/` byte-for-byte unchanged. BLOCKED originals and images awaiting real subsection mapping never enter the runtime allowlist. Original course files, progress keys and stored learning data are protected by the regression suite.
