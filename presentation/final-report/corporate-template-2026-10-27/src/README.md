# Native corporate adaptation

`adapt_native.py` edits the latest approved business-English OOXML package directly. It does not rebuild the deck or export its native effects through an importer. The supplied `layout-spec.json` controls exact canvas, zones and conversion factors; local coordinates and half-point font sizes are production choices.

Use the bundled Python and Node runtimes listed in `DELIVERY.md`. From the repository root:

```bash
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/corporate-template-2026-10-27/src/adapt_native.py
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/corporate-template-2026-10-27/src/check_native.py
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node presentation/final-report/corporate-template-2026-10-27/src/finalize.mjs output/asset-management-llm-corporate-transfer-reproduced.pptx
```

The finalizer requires a new output path and refuses to overwrite a deliverable. Its positional path is relative to this adaptation directory. The source SHA is checked before authoring; package entry order and metadata are retained for deterministic reproduction.

Render the delivered output with one fresh Node process per slide:

```bash
/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 presentation/final-report/corporate-template-2026-10-27/src/render_all.py presentation/final-report/corporate-template-2026-10-27/output/asset-management-llm-corporate-transfer.pptx presentation/final-report/corporate-template-2026-10-27/build/qa/final-render
```

`render_all.py` accepts optional slide numbers after the render directory. It records the input and PNG hashes and rejects a changed input. `inspect-artifact.mjs` imports for inspection only. `check_native.py` accepts an optional PPTX path and checks the final bytes against the original source. Reports and renders stay in `build/`.
