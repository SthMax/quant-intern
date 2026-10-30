# Reproduction

Run from the repository root with the bundled runtimes:

```bash
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/streamlined-workflows-2026-10-30/src/build_streamlined.py
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/streamlined-workflows-2026-10-30/src/check_streamlined.py
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node presentation/final-report/streamlined-workflows-2026-10-30/src/finalize.mjs output/reproduced-streamlined-en.pptx
```

The finalizer requires a new destination and does not overwrite the reviewed deck. Its path argument is relative to this edition. It performs package/geometry/font-reference checks and Artifact Tool import validation before copying the native package. It does not re-export the final native objects through an importer. The expected count is 28, and the required native table belongs to slide 10.

Source is `../visual-workflows-2026-10-28/output/asset-management-llm-visual-en.pptx`, SHA256 `1dae3a54c474190f1ca41ddbbd1a923d61929df714f861828547a59ddd39a2e4`. The source is read only. Titles and source mapping follow `HANDOFF.md`; exact measured geometry/conversions come from `../corporate-template-2026-10-27/layout-spec.json`. The later footnote rule is recorded in the handoff: one 8 pt line above y13.55 cm. Source Arial and palette remain unchanged. Native primitives use centimeters and points, converted explicitly to EMU. The ZIP timestamp is fixed for reproducible bytes.

Fresh-process rendering:

```bash
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/streamlined-workflows-2026-10-30/src/render_all.py presentation/final-report/streamlined-workflows-2026-10-30/output/asset-management-llm-streamlined-en.pptx presentation/final-report/streamlined-workflows-2026-10-30/build/qa/final-render
```

Append page numbers for a subset. Each slide is imported/rendered in its own Node process. The manifest records the immutable input hash and each PNG hash. Do not modify the input while a render batch runs. `check_streamlined.py` accepts an optional PPTX path for checking the immutable output.

`page-plan.json` records all 28 pages and their original-page inputs. `speaker-notes.json` matches the embedded narration, supporting passages and URLs. `content-coverage.json` accounts for approved original content through visible text, notes, condensation/merging or retained source records. The three `original-*.json` files retain complete approved content, the exact visual-source notes and the earlier source-note archive. They are source records, not the audience's spoken narrative.

No PowerPoint UI automation, Git mutation, palette remapping or company-template upload belongs to this build.
