# Initial independent design and integration review

Status: advisory only. The production PPTX, scripts and root-owned specifications have not been edited. The exact specification takes precedence over the proposed design choices below.

## Why the source canvas was oversized

`interactive-full-revised-2026-10-26/build/build.mjs:10` explicitly creates a 1600 × 900 slide. The runtime uses CSS-pixel geometry at 96 DPI, and the subsequent package editor uses 9525 EMU per coordinate unit. Thus 1600/96 × 900/96 inches is 42.333333 × 23.8125 cm, matching the actual PPTX. The English editions inherited that canvas. This is a production canvas/unit choice, not evidence of a Mac/Windows incompatibility or an exporter defect.

## Exact requirements

- Canvas: 25.40 × 14.28 cm, or 9144000 × 5140800 EMU. Do not round the height to 14.2875 cm.
- Title box top: 2.00 cm. Subtitle box top: 3.00 cm. Keep each within its allotted vertical zone.
- Body bounds: x=1.27–24.13 and y=3.92–13.01 cm. This includes the office map, example labels, controls and source notes.
- Keep the top brand region and bottom 1.27 cm clear for the corporate master. The supplied guide positions are alignment options, not mandatory divisions.
- Preserve 33-slide order, approved business meaning, colors, editable diagrams/table, IDs/names, all 407 links and destinations, all 33 Morph transitions at 700 ms, and the existing appearance groups on 14 slides.

## Proposed execution choices

1. Use the proposed x=1.27–6.23 sidebar consistently on workflow slides, then record one narrow gutter before the main body (approximately x=6.6–6.75 is a starting point). Full-map overview/summary pages can retain their distinct map composition. Reserve the control/source band before allocating diagram height.
2. Treat uniform scaling as an initial geometry calculation, not the final layout. A 60% reduction would turn common 19.5 pt source body text into 11.7 pt and 10.5 pt source notes into 6.3 pt. Proposed starting sizes: titles about 20–24 pt; principal body 14–16 pt; dense table/document fields 12–13 pt if necessary and visually checked; source notes about 8.5–10 pt. These are design targets, not company requirements or blanket minimums. Reflow panels and deliberate line breaks before reducing type.
3. Keep the approved English. Log any necessary concise adaptation separately for meaning review. Do not drop financial units, trader-supplied quote provenance, V2 client prose, or the Added/Retained distinction to obtain a fit. Repeated V1/V2 passages must remain identical in substance and wording.
4. Edit the final business-English package directly. Preserve original identities, relationships, timing trees and transition nodes. Compare against this final package, including its three added labels; do not revert to an earlier source. Avoid wrapping all content in a new group merely to simplify transfer, since grouping can affect Morph and appearance behavior. Named logical selection sets are safer. The native table must remain a table.
5. Keep title/subtitle separate from transferable body objects. Do not transfer a page-sized white shape that hides the corporate master. Handle the cover explicitly: its title/kicker/artwork use different object names from ordinary slides and must respect the same reserved zones.
6. Calibrate 22, 11, 18, 17 and 32 first, then inspect every slide. In particular: 08 evidence-to-summary spacing; 11 complete units/provenance and table footer; 17 visible LLM-assisted review; 18 document-field space; 23 phrase-aligned highlights; 24 Added/Retained output; 32 column labels and phase spacing.

## Review and transfer checks

The independent review will inspect all 33 renders plus geometry/font diagnostics and interaction comparisons. Bounds checks should cover native tables, image cropping, grouped transforms, text insets, background limits and connector endpoints, not only text-box coordinates. Render each slide in a fresh process.

The adapted file can preserve its own complete interaction system. Copying only objects into a different presentation does not transfer slide-level Morph and cannot guarantee correct cross-deck hyperlink targets or appearance sequences. The transfer guide must distinguish those two contexts and require local verification/rebinding where needed. Root handles native PowerPoint checks; no concurrent UI access is planned.
