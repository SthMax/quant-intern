# Revised business English presentation

Final: `output/asset-management-llm-business-en.pptx`

SHA256: `4fd31b6f18748ccdfc202619ea97d499d2d2ec6e815008df35e8fe695b1df7a2`

The 33-slide deck implements the approved review across slide copy, diagrams, the native bond table, navigation and speaker notes. V1’s intentional omissions remain, and the corrected V2 passage repeats consistently. Company A remains teal, the client update and V1/V2 remain purple, and revised wording remains yellow.

The package retains all original object identities, all 407 internal links and destinations, 33 Morph transitions of 0.70 seconds, and the original appearance timing on 14 slides. Three native labels were added with unique IDs and bound to their corresponding existing appearance group. All diagrams remain editable.

Package, layout, import and Arial design-font checks pass, with no layout warnings. Slide size is 15240000 × 8572500 EMU. Every slide was rendered in a fresh process and inspected individually. Financial-unit, source-URL, V1/V2, reported-metric and output-wording checks pass. Native PowerPoint checks covered pages 3, 8, 11, 17, 18, 23, 24 and 32, including navigation and the new labels appearing with their original groups. The file hash remained unchanged after playback.

The previous presentations and approved review remain unchanged. No commit, push or release action was performed.

## Reproduction

Use the bundled Python and Node runtimes. Run `src/revise_copy.py`, `src/build_business.py`, `src/finalize.mjs`, `src/check_business.py` and `src/export_final_copy.py`, in that order. Preserve an existing final file and validation receipt before rebuilding. `src/render_all.py` launches `src/render-one.mjs` in a fresh process for every slide. The finalizer validates the native package without re-exporting it through an importer.

`ENGLISH-COPY.md` is extracted from the actual final package. `REVIEW-IMPLEMENTATION.md` maps every numbered recommendation and material notes recommendation. Private intermediate packages, previews and QA records are in `build/`. The original English source set is retained under `build/provenance/original-authoring/`.
