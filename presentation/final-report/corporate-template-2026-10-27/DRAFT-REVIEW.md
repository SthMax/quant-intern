# Independent draft review

Stage: **draft calibration and first full-render pass, not final acceptance**. All 33 images in `build/qa/render/` were inspected individually. Files were updating during the pass; no final package hash is certified here. Findings were relayed to the implementer through root. Production files were not edited by this reviewer.

The exact corporate zones and fixed office-map strategy are sound. The smaller point sizes are generally readable at full-slide display; a blanket font increase is not required. The remaining problems are principally local text/background padding, evidence-row allocation and narrow connector labels.

| Slides | Draft finding / action |
| --- | --- |
| 01–02 | No material visual issue. Cover artwork stays in the body and leaves the brand region clear. |
| 03 | Two-line outcomes sit very close to the following task bars. Minor spacing improvement if practical. |
| 04 | Report B text extends below its teal source stripe; extend the stripe with its text. |
| 05 | No material overlap. |
| 06 | Final line in Fullgoal workflow is flush with pale-panel bottom; add internal bottom padding. |
| 07 | No material visual issue. Efficiency meaning and attribution remain clear. |
| 08 | **Required repair:** sales-volume values cross the next evidence divider; Report B's final word is obscured by the output band. Reallocate evidence rows and summary-band space. |
| 09 | **Required repair:** Query results wraps into the system heading; Quote splits mid-word; Quote request crowds Counterparty. Widen/reposition connector labels independently of arrows and clear the system bodies. |
| 10 | Match-and-route final line extends below its background. |
| 11 | Pass at calibration/draft stage: units, provenance, table stripe, arrow and footer are clear. |
| 12–13 | No material collision. |
| 14 | RFP answer's source citation extends below the answer background. |
| 15 | Existing-investment-view input's final line touches/exceeds its pale background. |
| 16 | No material overlap; source quotation and review criteria remain distinguishable. |
| 17 | Calibration: V1 monitoring line exceeds highlight and risk-comment final line exceeds panel. Later draft shows improvement; recheck final padding. Visible LLM umbrella retained. |
| 18 | Source-panel last line, document-tool last line and V2 risk disclosure reach/exceed their backgrounds or border. Recheck after local repairs, retaining complete client prose. |
| 19–20 | No material collision. |
| 21 | **Required repair:** face value line is crossed by the next evidence divider and exceeds holdings background. Assessment's final line touches its lower border. |
| 22 | Pass at calibration/draft stage. |
| 23 | HuaAn input-panel final line reaches/exceeds its background. Version wording and addition highlights remain clear. |
| 24 | Document-tools panel is tight but contained; no material output collision. |
| 25–26 | No material collision. |
| 27 | Feedback panel's final word extends below its background. |
| 28 | Business-analytics middle panel's final line touches/exceeds the background. |
| 29–30 | No material visual issue. |
| 31 | LLM panel's final line reaches/exceeds its background; retain clearance from shared-data text below. |
| 32 | First divider sits very close to the participating-team text. Column labels are present and clear. |
| 33 | No material visual issue; elapsed-time and repeat-usage definitions remain intact. |

## Verification audit to resolve before final acceptance

The draft `check_native.py` checks direct `p:transition` children, while the source's transitions are inside `mc:AlternateContent`. Compare the complete alternate-content transition subtree or all descendant transition nodes, and explicitly assert `p14:dur="700"` on the Morph branch. A `None == None` comparison does not certify transition preservation.

Check exact title/subtitle top coordinates as well as zone containment. Validate the stated line-width half-point grid, or remove the untested claim from the report. These points strengthen verification; they do not establish a current package defect.

Final review will examine the corrected renders, actual candidate package, geometry/content/interaction reports, and transfer guide. Root owns native PowerPoint playback checks.
