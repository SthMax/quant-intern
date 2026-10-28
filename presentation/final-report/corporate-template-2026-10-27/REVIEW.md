# Independent final review

**Status: Accepted for delivery as the corporate transfer edition.** No unresolved material visual, content-preservation or geometry findings remain in the reviewed file. This acceptance covers the delivered transfer deck; it does not certify an unseen corporate master or a subsequent cross-presentation paste.

Reviewed file: `output/asset-management-llm-corporate-transfer.pptx`

Verified SHA256: `f7a92ebd1caf4f0257b89065d23b0eccc78456aa0248fdef13e4d7afbf0cf440`

Approved source SHA256: `4fd31b6f18748ccdfc202619ea97d499d2d2ec6e815008df35e8fe695b1df7a2`

The reviewer inspected both reference photographs, the exact specification, the source authoring/unit conversion, all 33 draft slides individually, every changed final render, the actual final PPTX package, geometry/content/interaction reports, finalizer receipt and transfer-selection manifest. The reviewer did not alter the production PPTX, production scripts or root-owned specifications, and did not operate PowerPoint.

## Geometry and visual acceptance

- Independently verified canvas: **9144000 × 5140800 EMU**, exactly **25.40 × 14.28 cm**.
- Independently verified title and subtitle box tops: **2.00 cm** and **3.00 cm**. Header text remains inside its respective zone.
- Independently checked all slide-level object bounds against the specified zones. Body objects fit **x=1.27–24.13, y=3.92–13.01 cm**, leaving the corporate brand/footer areas clear.
- The fixed workflow office map and main-body gutter are consistent. Full-map slides retain their intended alternate composition. Titles, example cues, source notes and controls remain distinct.
- Typography is legible at full-slide display in the reviewed renders. The compact field/table sizes are acceptable for this physically smaller canvas. Arial and point sizes remain adaptation choices, not invented company font requirements.
- Native diagrams, the slide-11 table and cover artwork are retained. Source-stripe and highlight adjustments follow their text; Company A, client-update and revised-wording colors remain coherent.

All 33 final PNG metadata files identify the reviewed output hash, and each recorded PNG hash was independently checked against the actual image. The render metadata records a fresh process per slide at scale 1.5. Final images for slides 01, 02, 12, 19, 22, 30 and 33 are byte-identical to the corresponding individually reviewed draft images. All other final images were individually re-inspected after the changes.

| Slides | Final result |
| --- | --- |
| 01–07 | Pass. Map spacing, evidence stripes and workflow-panel padding are resolved. Cover leaves the brand area clear. |
| 08 | Pass. Sales-volume values and both report hypotheses are fully visible; dividers and output band no longer obscure evidence. |
| 09–10 | Pass. Connector labels no longer split words or collide with system headings. Matching/routing text fits its background. |
| 11 | Pass. Native table units, current holding, available size, clean price and trader-supplied provenance remain clear. Footer and navigation are separated. |
| 12–16 | Pass. RFP citation and input-panel padding are resolved; source quotation and review criteria remain distinct. |
| 17–18 | Pass. V1/V2 fields, yellow highlights and risk panels contain their text. The visible LLM-assisted-review umbrella and complete final client prose remain. |
| 19–21 | Pass. Holdings face value is unobscured; monitoring requirement and assessment panels have clear boundaries. |
| 22–24 | Pass. HuaAn panel padding is resolved. V1/V2 wording and phrase highlights remain aligned; Added/Retained information is explicit. |
| 25–28 | Pass. Requirements, feedback-loop panels and business-analytics output are contained and readable. |
| 29–33 | Pass. Application summaries, information flows, shared capabilities, phase labels and evaluation definitions remain clear. First-phase divider spacing is resolved. |

## Independent package checks

The reviewer used a separate read-only comparison against the approved source, rather than relying only on the implementer's reported pass:

- 33 slides and identical original `cNvPr` ID/name sequences.
- All **407 hyperlink XML records** unchanged, with unchanged relationship parts and destinations.
- Complete descendant transition nodes and `mc:AlternateContent` subtrees unchanged. All **33 Morph branches explicitly retain 700 ms**.
- Appearance timing trees unchanged on **14 slides**, including the existing labels 9000, 9001 and 9002.
- Approved slide text is equal per original object after normalizing whitespace. There are no business-wording changes.
- The sole native table remains on slide 11.
- All non-slide/non-presentation package parts remain byte-identical, including speaker notes, relationships, themes and media. Only the 33 slide XML parts and presentation sizing XML differ.
- No object-zone violations were found.

The revised checker now tests descendant transitions and the Morph duration explicitly, exact header tops, and the declared line-width grid. The final geometry and interaction reports match the file hash. The text-fit report has zero flags. The finalizer receipt records package, Arial reference-font and first-party import passes, with no layout warnings.

## Integration guidance

`TRANSFER-GUIDE.md` appropriately distinguishes the delivered deck from a subsequent object transfer. It separates title/subtitle selection, excludes the source heading rule and cover white shape, identifies the corporate master as the logo/footer provider, and warns that cross-presentation object copying does not guarantee slide-level Morph or internal-link destinations.

The durable `src/transfer-selection-manifest.json` matches the QA copy. It covers all 33 slides, separates one title and one subtitle per slide, and contains no duplicate selected IDs within a slide.

Native PowerPoint playback is owned by root and recorded separately. After local corporate integration, the user should verify font rendering, placeholder duplication, internal destinations and progressive appearances in that destination presentation. No corporate template export is required.
