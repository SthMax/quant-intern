# Static business presentation draft

Draft: `output/asset-management-llm-static-en.pptx`

SHA256: `f6df29e6361e34aa763177a67d54890e782f76bf08f474db0f9ecaecabebd5ba`

This is the complete 33-slide static draft for the newly requested independent design review. It is not the previously accepted transfer edition. Earlier editions are preserved; no commit, push or release was performed.

The canvas remains exactly **25.40 × 14.28 cm**. Title and subtitle boxes start at **2.00** and **3.00 cm**. Body objects stay within **x=1.27–24.13, y=3.92–13.01 cm**. The company master owns the clear brand/footer regions.

All 33 pages have new explicit compositions. Diagrams, text, document examples and the slide-11 table remain native and editable. The original cover artwork is the only slide picture. Animations, timing, transitions, Morph, page counters, control objects, detached upper-right tags, action links and internal slide-jump relationships have been removed. The three-office locator is plain static context.

Business text, figures, complete V1/V2 passages and research URLs remain. Changes are documented in `DESIGN-NOTES.md` and the per-page source-key record `src/copy-coverage.json`. Design choices and reference lessons are recorded per page in `src/page-design-notes.json`.

Mechanical checks pass with zero zone violations and zero text-fit flags. Artifact Tool import and package finalization pass. The finalizer retains one conservative native-table height estimate on slide11. Native PowerPoint inspection resolved that diagnostic: the table bottom and trader/portfolio-manager footnote are visibly separated, without overlap or clipping.

Root opened native PowerPoint pages1,3,11,17,18,22 and32 without repair prompts or material clipping. Complete content was immediately visible and the removed controls/tags were absent. The checked file was closed without saving and its SHA256 is unchanged. This bounded native check is recorded in `build/qa/native-check.json`. A mechanical or native-display pass is not an aesthetic verdict; independent recommendations belong in `DESIGN-REVIEW.md`.

Private verification: `build/qa/mechanical-check.json`, `fit-diagnostics.json`, `finalizer.json`, and `final-render/render-manifest.json`. Each final slide renders in a fresh Node process and records the input/PNG SHA256.

Reproduction commands and dependencies are in `src/README.md`. Arial sizes are design choices, not corporate typography requirements. The user can add animation manually after reviewing this static draft.
