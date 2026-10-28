# Static business presentation redesign

User request, 28 October 2026: create another edition without animations, page numbers, Overview/Back/Next controls or the detached upper-right example/storyline tags. The user will add animation personally. The user explicitly finds the current layout unprofessional on every page and requests a new draft followed by a separate agent's business-slide review and recommendations. Both author and reviewer use GPT-6.1 Sol, xhigh. Coordinate in English.

## Scope and deliverables

- Author: the existing `corporate_template_ppt` agent. Create the complete 33-slide English static draft, then hand it to root for independent review.
- Reviewer: a fresh Sol xhigh agent, appointed after the draft is complete. Review the actual pages against professional business presentation references, give a candid page-by-page report and prioritized recommendations. Prior acceptance of the older edition does not establish visual quality for this task.
- Root coordinates, checks requirements and reviews representative pages in PowerPoint. Preserve the completed draft as reviewed so its recommendations refer to a stable artifact. This request does not authorize publishing or releasing it.
- Output: `output/asset-management-llm-static-en.pptx`, plus an independent `DESIGN-REVIEW.md`. Reproducible source and design decisions belong in `src/` and `DESIGN-NOTES.md`; private renders and checks in `build/`.

Source deck: `../corporate-template-2026-10-27/output/asset-management-llm-corporate-transfer.pptx`, SHA256 `f7a92ebd1caf4f0257b89065d23b0eccc78456aa0248fdef13e4d7afbf0cf440`. Keep all earlier deliverables. Retained user context is in that directory's `TEMPLATE-SPEC.md`; this request replaces its interaction and fixed-navigation preservation rules for the new edition.

## Static-edition requirements

1. Remove every object animation, timing tree, slide transition, Morph/fallback transition and interactive action. Show the complete intended composition immediately on every slide. Remove unused internal slide-jump relationships. Preserve source references in notes.
2. Remove page/slide counters and Overview/Home, Back, Next and Start controls. Delete those objects. Keep actual overview content, process-stage numbers and financial figures.
3. Remove all detached upper-right story/example headers, including Company A, Client update, Example, qualifiers such as Method reference/Review V1/Revised V2, and independent-case tags. Keep Company A and V1/V2 identifiers where they are substantive parts of the evidence, document or diagram itself.
4. Redesign all pages with intentional composition. Deleting interface objects and uniformly shifting the remainder is insufficient. Establish hierarchy, alignments, consistent type, clear relationships, breathing room inside and between text groups, and one strong focal point per page. Limit decorative frames and panel fills. Layouts should vary with the work being explained.
5. Keep the front/middle/back-office story and clear current-office/task context. A restrained static locator may retain the company map. It can be more compact and should no longer resemble a button interface. All substantive text, diagrams and the slide-11 native table remain editable for manual corporate-template integration.
6. Preserve the approved business English, facts, source attribution and 33-slide order. Concise refinements for slide readability may be proposed and logged. Keep repeated V1/V2 prose consistent and preserve complete business meaning. The LLM's own tasks must remain explicit on proposal slides.

## Measured company geometry

Use the exact `../corporate-template-2026-10-27/layout-spec.json` geometry as input: slide 25.40 × 14.28 cm, left/right/bottom margins 1.27 cm, title top 2.00 cm, subtitle top 3.00 cm, body top 3.92 cm, body bottom 13.01 cm. Brand and footer zones stay clear. All coordinates are from the slide's top-left; 1 cm = 360000 EMU.

Absolute vertical guide positions: 1.27, 6.23, 8.38, 9.15, 12.20, 13.20, 16.25, 17.02, 19.17 and 24.13 cm. They recommend alignment and component widths; each small object need not touch a guide. The previous sidebar width and main-body gutter are design choices and may be improved. The previous 20 pt/11.5 pt/other font sizes are also design choices, not supplied company requirements.

Company A content retains teal, client-document content purple, structure blue, people/tools neutral and changed passages yellow. Removing the detached headers does not erase the identity of the recurring evidence/documents. Use color sparingly and consistently.

### Header and component-size clarification, 28 October

The user repeated all measured geometry and component-width guides after seeing the static draft, and specifically asked whether the title/subtitle had been compressed too much. Root resent the complete measurements to the author. A read-only author/root inspection confirmed that the subtitle's small size came from our own typography decisions.

Actual frozen static draft: ordinary titles are 20.5 pt bold in a 22.86 × 0.80 cm box at (1.27, 2.00); subtitles are 10.5 pt regular gray in a 22.86 × 0.52 cm box at (1.27, 3.00). This makes the subtitle smaller and less prominent than much of the body. The user specified positions and margins, not these compressed font sizes. Title/subtitle typography must be designed to use their available bands and maintain a clear hierarchy.

The concrete proposal discussed with the author is 24 pt bold main titles in approximately 0.95 cm-high boxes, and 16 pt blue subtitles in 0.70–0.75 cm-high boxes. Keep the exact top positions 2.00 and 3.00 cm and body top 3.92 cm. All current title/subtitle strings fit those proposed widths in font-metric estimates. These values are a design proposal, not user-supplied corporate font sizes, and have not been applied to the frozen PPTX. A later implementation should check actual PowerPoint display and remove/reposition the author-added 3.72 cm header rule if it conflicts with the larger subtitle band.

The supplied width guides should define deliberate reusable major component spans. The current two-/three-column layouts do use the measured anchors; several document/method splits, four-stage flows, the driver tree and internal table columns still use custom widths. Record and justify those major custom spans in the design notes rather than claiming all components already follow the grid. Internal text padding remains separate from major component alignment.

## Reference study and review standard

Study actual pages from official business presentations. Initial reference material:

- Morgan Stanley, 4Q2025 Strategic Update: https://www.morganstanley.com/content/dam/msdotcom/en/about-us-ir/shareholder/4q2025-strategic-update.pdf
- Morgan Stanley, 4Q25 Fixed Income Investor Presentation: https://www.morganstanley.com/content/dam/msdotcom/en/about-us-ir/pdf/Morgan_Stanley_4Q25_Fixed_Income_Investor_Presentation.pdf
- BlackRock, 2025 Investor Day: https://ir.blackrock.com/news-and-events/2025-Investor-Day/default.aspx

Local Morgan Stanley PDFs and selected page PNGs are in `../workflow-proposal-2026-10-23/build/style-reference/`. Root will provide a second publisher's selected pages. Use the references to assess title/body hierarchy, grid, whitespace, composition, evidence framing and information density. Do not transplant their business claims, logos or dense regulatory pages.

Root downloaded the official BlackRock presentation from https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf and rendered reference pages under `build/style-reference/`. Selected PDF page numbers (one-based): Morgan Stanley Strategic Update 6, 7 and 9; BlackRock Investor Day 4, 12, 22 and 36. The PNG filenames identify these pages. Root inspected each at readable size. MS7 is useful for clear hierarchy and equal gutters; MS9 for aligned column headings/evidence; BlackRock36 for a spacious staged process with strong type hierarchy. BlackRock22 is a dense example of showing the actual output beside supporting information. Its density is a trade-off to evaluate, not a target for every slide. BlackRock's palette, footer and logos are not requested. The additionally rendered BlackRock41 is an interactive-overlay state and should not guide the static edition.

The independent reviewer should identify the reference pages it actually inspected, explain specific visual lessons, and assess each of our 33 pages against them. A pass on boundaries or text-fit estimates is not an aesthetic verdict. Recommendations should identify the page, concrete problem, priority and implementable change, with brief reasoning. Report real strengths where useful, but do not inherit the author's self-assessment or the older review's acceptance.

## Production and checks

Use the Presentations skill for local PPTX authoring, with native editable evidence/diagrams and Artifact Tool rendering/validation. Render each page in a fresh process. Inspect every slide at readable size, plus deck-level rhythm. Check exact geometry; zero timing/transitions/jump actions; absence of the removed controls/counters/header tags; source notes; necessary business text; table editability and numerical units. Confirm normal PowerPoint display separately from package checks. No PDF deliverable is requested.
