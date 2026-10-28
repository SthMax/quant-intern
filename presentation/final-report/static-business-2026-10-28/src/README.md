# Reproduce the static edition

Run from the repository root with the bundled runtimes:

```bash
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/static-business-2026-10-28/src/build_static.py
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/static-business-2026-10-28/src/check_static.py
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node presentation/final-report/static-business-2026-10-28/src/finalize.mjs output/reproduced-static-en.pptx
```

`finalize.mjs` requires a new output path and refuses to overwrite the reviewed draft. The argument is relative to this edition's directory. The source is the corporate transfer edition with SHA256 `f7a92ebd1caf4f0257b89065d23b0eccc78456aa0248fdef13e4d7afbf0cf440`; the builder checks that hash. The exact corporate measurements come from `../corporate-template-2026-10-27/layout-spec.json`.

The builder composes native OOXML text, shapes and connectors, retains the native table and image asset, and removes the previous interaction parts. No Python presentation library, slide rasterization or importer re-export writes the deliverable. Artifact Tool imports, renders and validates it.

Render the immutable draft, with a fresh process for each page:

```bash
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/static-business-2026-10-28/src/render_all.py presentation/final-report/static-business-2026-10-28/output/asset-management-llm-static-en.pptx presentation/final-report/static-business-2026-10-28/build/qa/final-render
```

Append slide numbers to render a subset. The manifest rejects source-file changes during a render pass. `check_static.py` accepts an optional PPTX path and regenerates static requirements, bounds, notes/table parity and the durable `copy-coverage.json`. `source-content.json` is the original text inventory. `page-design-notes.json` records the per-page composition and reference lesson.
