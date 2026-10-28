# Corporate transfer edition

Deliverable: `output/asset-management-llm-corporate-transfer.pptx`

SHA256: `f7a92ebd1caf4f0257b89065d23b0eccc78456aa0248fdef13e4d7afbf0cf440`

Source: the final approved 33-slide business-English deck, SHA256 `4fd31b6f18748ccdfc202619ea97d499d2d2ec6e815008df35e8fe695b1df7a2`. Earlier deliverables are untouched. No commit, push or release is part of this delivery.

## Geometry and typography

The exact user geometry is in `TEMPLATE-SPEC.md` and `layout-spec.json`: **25.40 × 14.28 cm**, or **9144000 × 5140800 EMU**. Titles start at y=2.00 cm and subtitles at y=3.00 cm. All body objects, office navigation, current-example labels, controls and source notes fit x=1.27–24.13 and y=3.92–13.01 cm. The company header and lower 1.27 cm are clear.

The consistent workflow sidebar is x=1.27–6.23 cm. Its divider is x=6.56 cm and the main content starts at x=6.88 cm. Full-map pages retain their full-width composition. Native diagrams, the slide-11 table and the cover image remain editable or in their original native image form. The image's aspect ratio is preserved. No company logo or footer has been fabricated.

Typography is an adaptation choice because the user supplied no company font sizes: Arial, 20 pt titles on slides 2–33, 22 pt cover title, 11.5 pt subtitles, 9.5–14.5 pt principal content, 12 pt office headings, 10–10.5 pt navigation, 8–9 pt secondary cues, and 7 pt source notes. Sizes and positive line widths use deliberate 0.5 pt steps. Text rewrapping and background/field reallocation precede any local font choice.

## Copy and native interactions

No business wording changed. Normalized text matches the source per original object, including the financial units, trader-supplied quote provenance, complete V2 client prose, and Added/Retained distinction. The cover title's line break was rewrapped into one line.

- All original object IDs, names and types are retained, including IDs 9000/9001/9002 and their timing bindings.
- All 407 hyperlink XML records and unchanged relationship files preserve their destinations.
- All 33 Morph transitions retain 700 ms duration; both the Morph branch and fallback transition XML remain unchanged.
- Appearance timing XML remains identical on 14 slides. Speaker notes and source citations are unchanged.
- Slide 11 retains its editable four-column, two-row bond table.

## Verification record

The package finalizer passed with no warnings and verified Artifact Tool import. The native comparison and measured geometry reports pass; the text-fit estimate has zero flagged items. Artifact Tool is used only for import, rendering and inspection. The final PPTX is the native edited package, with no importer re-export.

Every source slide and adapted slide has been visually inspected. The independent Astra review accepted the exact final file for delivery, with no unresolved material findings; see `REVIEW.md`. It independently verified final PNG hashes, the package-preservation claims and measured zones.

Native PowerPoint checks passed on slides 1, 3, 8, 11, 17, 18, 22, 23, 24 and 32. Clicked sequences 16→17, 17→18, 23→24, 31→32 and 32→3 reached their intended destinations. Eighteen captured frames per progression confirmed slide 17's LLM-review label/comments and slide 32's phase-1 labels followed by later phases. The checked copy was closed without saving, and the final SHA256 remained unchanged. The record is `build/qa/native-playback-2026-10-27.json`.

Private records: `build/qa/finalizer.json`, `geometry-report.json`, `interaction-content-report.json`, `fit-review.json`, `production-visual-review.json`, `artifact-inspection.ndjson`, and `final-render/render-manifest.json`. The durable object-selection aid is `src/transfer-selection-manifest.json`. The transfer caveat and local integration steps are in `TRANSFER-GUIDE.md`.

## Reproduction

Implementation: GPT-6.1 Sol, xhigh. Independent review: the prior Astra PPT editor. Source scripts and commands are in `src/README.md`. A clean rerun of the final authoring script reproduced the final PPTX SHA256 exactly.

Bundled runtimes:

- Python: `/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`
- Node: `/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node`

Required source files, template photographs and corporate template files are not duplicated in the output directory.
