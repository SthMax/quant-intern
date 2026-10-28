# Reproduction

The source package is the preserved static edition, SHA256 `f6df29e6361e34aa763177a67d54890e782f76bf08f474db0f9ecaecabebd5ba`. The measured specification is read from `../corporate-template-2026-10-27/layout-spec.json`.

Run from the repository root with the bundled runtimes:

```bash
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/visual-workflows-2026-10-28/src/build_visual.py
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/visual-workflows-2026-10-28/src/check_visual.py
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node presentation/final-report/visual-workflows-2026-10-28/src/finalize.mjs output/reproduced-visual-en.pptx
```

The finalizer requires a new destination and will not overwrite the reviewed delivery. Its path argument is relative to this edition's directory. Native OOXML shapes/connectors, the native table and original cover asset remain editable. Artifact Tool imports, renders and validates the package; no importer re-export writes the final native file.

Render the immutable file in fresh processes:

```bash
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/visual-workflows-2026-10-28/src/render_all.py presentation/final-report/visual-workflows-2026-10-28/output/asset-management-llm-visual-en.pptx presentation/final-report/visual-workflows-2026-10-28/build/qa/final-render
```

Append page numbers for a subset. Render metadata records the input and PNG hashes and rejects a changed input. `check_visual.py` accepts an optional PPTX path and generates static, measured-zone, evidence, map, table and notes checks, plus `content-coverage.json`. Conservative typographic fit diagnostics are reviewed against actual renders and native display.

`approved-content.json` and `source-notes.json` preserve the complete approved source records. `speaker-notes.json` contains the usable spoken explanation, relevant evidence passages and source URLs embedded in the PPTX. `implementation-mapping.json` connects each page's native mechanism and SEE/SAY choices to `PAGE-DISCUSSION.md`. Semantic object-name prefixes support later manual animation.
