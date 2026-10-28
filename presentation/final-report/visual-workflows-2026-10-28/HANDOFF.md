# Visual workflow presentation revision

The user approved the author/reviewer discussion and authorized page-by-page discussion, revision and a local Git commit when complete. Both production and review use their existing GPT-6.1 Sol xhigh agents. All agent coordination is in English; root reports to the user in Chinese. Root owns the final commit. No push or release is requested.

## Governing communication goal

The audience must be able to follow the business mechanism while listening to the presenter. Design each page from its actors, material, transformations, relationships, states and output. Shapes and connectors should convey these relationships before the audience reads prose. Show concise labels, necessary figures and useful evidence. Put detailed procedure, rationale and complete passages in the speaker notes when they are not the evidence being examined on screen.

The previous static draft preserved on-screen wording too literally and converted useful diagrams into reading columns. This revision replaces that approach. More rectangles around the same paragraphs will not solve the problem. The original driver tree on page 5 and feedback loop on page 27 are useful structures to retain and improve.

## Source and output

Source static draft: `../static-business-2026-10-28/output/asset-management-llm-static-en.pptx`, SHA256 `f6df29e6361e34aa763177a67d54890e782f76bf08f474db0f9ecaecabebd5ba`.

Earlier visual/interaction structure for comparison: `../corporate-template-2026-10-27/output/asset-management-llm-corporate-transfer.pptx`, SHA256 `f7a92ebd1caf4f0257b89065d23b0eccc78456aa0248fdef13e4d7afbf0cf440`. Older visuals are references, not an instruction to restore all old containers or text.

Create a new 33-slide English PPTX at `output/asset-management-llm-visual-en.pptx`. Preserve earlier editions. Keep reproducible code/content in `src/`, private candidates/renders/checks in `build/`, and concise delivery/review records in this directory. An optional durable per-slide SEE/SAY plan is useful for the user's own later animation work. No PDF deliverable.

## Persistent requirements

- Keep the front-office → middle-office → back-office sequence, seven business tasks and approved case facts. Workflow, industry examples and company proposal remain the topic structure.
- Restore a compact, readable static company map on task pages: three office groups, seven task nodes, current office/task highlighted, consistent body placement. Use it to explain the company's architecture. On cross-firm pages highlight the relevant span; full-map pages do not need a duplicate locator.
- Keep the edition static: no animation/timing/transitions, no click/hover actions or internal jumps, no page counters, Overview/Home/Back/Next/Start controls, or detached upper-right story/example tags. The user will add animation personally.
- Maintain Company A's teal identity and the recurring quarterly client update's purple identity inside meaningful content. Purple also follows that update's preparation/version artifacts. Page14's independent RFP document and generic operational records remain neutral/structural blue. Structure is blue; roles/tools use restrained neutral treatment. Define yellow consistently for exact additions/revisions, with a distinct treatment for review focus when needed.
- Keep diagrams, document excerpts and the page-11 bond table native and editable. Images may explain a scene or object when helpful, but must not replace the editable business mechanism.
- Formal, natural business English remains required. Concise on-screen rewriting and purposeful excerpts are now authorized. Preserve meaning, units, uncertainty and source attribution; preserve the complete supporting wording in notes or durable source material.

## Exact geometry and header treatment

Read the measured geometry from `../corporate-template-2026-10-27/layout-spec.json`. Canvas25.40×14.28cm; left/right/bottom margins1.27cm; title top2.00cm; subtitle top3.00cm; body top3.92cm and bottom13.01cm. All coordinates are from the top-left. Keep corporate brand/footer areas clear.

Implement the discussed header proposal: ordinary main title24pt bold, approximately0.95cm box height; subtitle16pt blue, approximately0.70–0.75cm box height. Both have x1.27 and width22.86cm and the exact tops above. These are chosen design settings, not invented corporate font requirements. Current titles fit24pt by measured width estimates. Check actual rendering, especially long titles. Remove or relocate the previous3.72cm header rule if it conflicts with the subtitle band. Do not reduce every subtitle to breadcrumb size.

Use the vertical guides as deliberate reusable major component anchors: x1.27,6.23,8.38,9.15,12.20,13.20,16.25,17.02,19.17,24.13cm. Useful spans include the full22.86cm body, the first4.96cm for a map, the10.93cm two-column spans and7.10–7.11cm three-column spans. Use custom major spans only where the diagram needs them and document the choice. Keep text padding separate from grid alignment. Gain main-diagram space by relocating explanatory prose to notes, not by shrinking essential evidence.

## Agreed exemplar mechanisms

- **8, company research:** all three source objects visibly merge into an LLM role. Show a calculation request and return, a concise source-backed research output, and analyst judgment. Keep quarter evidence and the uncertainty over continued restocking visible; explain the reasoning in notes/speech.
- **9, trading workflow:** restore manager/trader/system/counterparty identities and query/quote request/return relationships. Company A and the within-two-years condition remain visible. The proposed LLM intervention belongs on11; quote inputs there remain trader-supplied records.
- **15–18, client materials:** these pages together form the document sequence. On18 use small V1/current-source inputs, matching/revision roles, a larger V2 evidence excerpt and author/reviewer approval. Keep both investment-view sentences where needed to show the added driver, uncertainty and retained cost monitoring. Full metadata, risk wording and process explanation can remain in notes when not the displayed issue. Avoid repeating the entire storyboard on every page.
- **31, shared capabilities:** shared approved sources visibly support distinct LLM/tool roles. Show a concrete business output returning to staff. Detailed operations, access/version information and candidate model names can be supporting notes. Keep this business-led rather than restoring a hardware/deployment chapter.

## Facts and wording to preserve

Company A's prior/current-quarter revenue is RMB100m/110m and sales volume1.0m/1.1m units; both rise10% and average selling price is unchanged. These are quarter comparisons. Bond A matures in1.2years, current/available face value is RMB20m, and clean price100.20 is perRMB100face. The trader supplies received quotes; the LLM extracts supplied records. Keep holdings and availability distinct.

V1 deliberately has the shorter fund name, Q2 product source and generic risk wording; V2 uses the full fund name and Q3 source. The full V1 investment view is: “Higher sales volumes drove Company A’s revenue growth. We are monitoring raw-material costs.” The full V2 passage is: “Channel restocking supported Company A’s sales volume growth. We are monitoring whether restocking continues, alongside raw-material costs.” Preserve this meaning and version consistency in on-screen excerpts and complete notes.

Zhong Ou's approximately50% refers to research-preparation efficiency; HuaAn's more-than80% refers to automated entry of the specified direct-sales-counter faxes. Penghua's91% note concerns acceptance of suggested edits. China Universal's business-analytics case is a proposed patent method. Qwen/DeepSeek remain candidates for evaluation. Preserve the source URLs and other underlying facts in the approved source.

## Page-by-page collaboration

The reviewer owns `PAGE-DISCUSSION.md`: for each of33 pages, record the business message, what the audience should SEE, what the presenter should SAY, needed evidence and any design trade-off. The author owns production source and an implementation mapping. They should exchange specific page decisions, resolve differences and review small batches instead of silently rewriting the whole deck before discussion. Sibling messaging may be unavailable; use root as relay and the shared files.

Start with the first topic batch and the core shared components. The author may proceed on agreed pages while the reviewer plans later pages. Root will review representative renders and handle native PowerPoint checks. The reviewer then inspects all33 final pages individually and verifies that visible mechanisms, evidence and speaker notes serve the talk. Repair actual defects and recheck affected pages. Avoid repeated full-deck acceptance loops once remaining concerns are resolved.

Use the Presentations skill and existing local native/Artifact Tool workflow. Render each page in a fresh process. Keep a final input-hash manifest, static-removal checks, measured-zone checks, native-table evidence and content/notes coverage. Object IDs may change; meaningful names should help the user's later animation work. Validate both the output file and the speaker notes. Root commits only the finished deliverables, source and relevant review/handoff records, excluding caches, third-party reference PDFs and Office lock files.
