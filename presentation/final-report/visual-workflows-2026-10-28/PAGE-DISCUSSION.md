# Page discussion: visual workflows

Source: the 33-slide static draft, SHA256 `f6df29e6361e34aa763177a67d54890e782f76bf08f474db0f9ecaecabebd5ba`. Governing requirements: [HANDOFF.md](HANDOFF.md).

This is the author's and reviewer's implementation discussion. **SEE** defines the visible mechanism and essential evidence. **SAY** defines the explanation and complete source wording preserved in speaker notes/durable content. Concise labels and purposeful excerpts are authorized. The author owns the presentation and code; the reviewer owns this file and the final independent review.

## Shared design decisions

- Keep 33 English slides and the existing topic order. The company proposals remain proposals from the intern's workflow and industry research.
- Use the exact geometry in HANDOFF.md: 24 pt bold title at y2.00 cm, 16 pt blue subtitle at y3.00 cm, body y3.92–13.01 cm. Header boxes remain full width from x1.27 to24.13 cm. Remove the old rule if it conflicts with the larger subtitle.
- On task pages, place a readable static firm map within the x1.27–6.23 cm body span. Keep a 0.50 cm gutter after that region boundary, so visible main content starts around x6.73 cm and ends at 24.13 cm. This custom start prevents map/content outlines touching; subsequent major components should use the supplied guides where practical. Use three office groups and seven concise task nodes; highlight the current office/task. All seven themes remain identifiable: Research, Trading support, Client materials, Content review, Risk analysis, Document processing, Tool development. Cross-firm pages highlight the relevant span. Cover 1 and full-map pages 3/29 need no duplicate map.
- Use native editable shapes for meaningful actors, material, transformations and outputs. Neutral roles/tools; blue structure; teal Company A content; purple for the recurring quarterly client update and its associated preparation/version artifacts. Independent RFP14, generic records and unrelated documents stay neutral/structural blue, following the approved COLOR-MAP.md distinction. Yellow marks exact additions/revisions. A neutral edge marker identifies a passage under review. Keep the diagram readable as a complete static state.
- Connect every material source to its actual receiving step. Label distinct request/result paths where direction matters. A merge bracket can collect several sources; dependency brackets can show shared support. Keep connectors clear of text and terminate them at the relevant object.
- Each page should let a listener identify the input, business action, output and responsible person while hearing the explanation. Include the LLM's particular contribution on proposal pages and distinguish tools' operations from human judgment.
- Notes should contain a natural, concise spoken explanation, relevant complete evidence passages/figures and inherited source URLs. The complete original content can remain in durable approved-content/copy-coverage material; usable notes should avoid duplicating the old raw label inventory. Preserve all substantive approved facts even when a shorter excerpt is displayed. Essential uncertainty, units and claim scope stay visible beside the relevant evidence. Navigation/control text is excluded.
- Keep design trade-offs and QA commentary in this discussion/review file. Spoken narration should explain the business directly; it should not describe layout decisions, compare design alternatives or explain what diagram lines do not imply. Distinguish talk, supporting evidence and source references clearly in the notes.
- Preserve useful visual logic in 5's driver tree and 27's feedback loop. A common graphic grammar is welcome; composition follows the particular mechanism.

## Batch 1: pages 1–11

### 1. LLMs in Asset Management

- **Message:** introduce industry examples and proposed applications in mainland asset management.
- **SEE:** concise title/subtitle, geographic context/date, and the existing restrained business-scene image. Keep the cover open; the first explanatory diagram begins on 2.
- **SAY:** the report follows employee work across the firm and proposes applications based on peer research. The company had not adopted the proposed LLM workflows.
- **Visible facts:** English topic, mainland asset management, October2026, proposal framing.
- **Trade-off:** a scene is suitable on the cover; the working pages use editable business diagrams. No mini-map is needed here.

### 2. Scope of proposed LLM applications

- **Message:** employee tasks combine information, language-model work and operational tools to produce useful business outputs.
- **SEE:** four small source objects (documents, data, messages, business requests) **merge** into an LLM role; a separate neutral tools node exchanges requests/results with it; four output objects fan out (company analysis, quote summaries, client materials, business tools). Within the roles, use short labels such as “Read / compare / explain / draft” and “Retrieve / query / calculate / run.” The map highlights the firm-wide span.
- **SAY:** explain the four original supported-work categories and how different applications use different combinations. Preserve the complete original lists in notes.
- **Visible facts:** LLM versus tool responsibilities; all four input/output families; specific employee tasks as the purpose.
- **Trade-off:** an aggregate merge/fan-out conveys categories. Equal source/output rows would imply unsupported one-to-one pairings.

### 3. Seven application areas across the firm

- **Message:** the seven tasks belong to a single firm architecture, with two recurring objects connecting the talk.
- **SEE:** full-width firm tree: one firm branches into Front office, Middle office and Back office; seven native task nodes sit under their offices in the established 3/2/2 grouping. Give each task one short outcome line. At the bottom, introduce a teal Company A information object and a purple quarterly-client-update document as the two recurring examples.
- **SAY:** explain the task sequence and how the two examples reappear. Keep the complete task/outcome wording in notes.
- **Visible facts:** all seven task names, office membership, Company A and quarterly client update. No duplicate mini-map.
- **Trade-off:** this page establishes architecture; detailed transfers appear on the task pages.

### 4. Company research: assessing revenue growth

- **Message:** analysts must assemble and reconcile several sources before forming a research view.
- **SEE:** three teal Company A source objects: a small prior/current-quarter financial table, meeting-note excerpt, and contrasting Report A/Report B claims. Connect all three to a neutral analyst work sequence: Find sources → Extract/calculate → Compare views → Record reasoning. End with a research-view object/question about growth sustainability. Highlight Research in the mini-map.
- **SAY:** describe repeated searching, extraction and checking, and why that preparation takes time away from analysis.
- **Visible facts:** revenue RMB 100m/110m; volume 1.0m/1.1m units; prior/current **quarter**; restocking lifted shipments; demand-recovery view versus uncertainty over continued restocking.
- **Trade-off:** source excerpts provide the evidence. Detailed procedural sentences move to notes; this remains the current human workflow, with no LLM intervention yet.

### 5. Tianhong: analyzing earnings drivers

- **Message:** the LLM structures an earnings-driver analysis while tools supply data/calculations and analysts assess quality.
- **SEE:** retain the driver tree: change in net profit branches to Revenue, Cost of sales and Expenses, then to their operating drivers. A compact LLM role identifies the structuring/linking work. A neutral data/calculation support node visibly feeds the driver analysis. A neutral analyst endpoint reads “Assess quality of growth.”
- **SAY:** explain the links between operating drivers and earnings, the tool work, and Tianhong's reported approach.
- **Visible facts:** volume/price; materials/production costs; distribution/selling expenses; distinct LLM/tool/analyst roles. Keep the diagram as a decomposition, not an assertion that net profit causes revenue.
- **Trade-off:** a hierarchy line or branch is sufficient for decomposition. Use directional arrows for supplied data and subsequent analyst use.

### 6. Fullgoal: comparing research views

- **Message:** comparison identifies agreement and the unresolved research question.
- **SEE:** two report objects merge into “LLM compares views,” then split into two concise findings: “Shared: higher volume” and “Open: sustainable growth?” A source-link/check path reaches the analyst. Keep short A/B claim excerpts visible near their source objects.
- **SAY:** describe report selection, topic summaries, consolidation and review; explain how the analyst investigates disagreement using the source links.
- **Visible facts:** A says demand recovery can sustain growth; B says continued restocking is uncertain; both associate higher volume with revenue. Keep the uncertainty explicit.
- **Trade-off:** the procedure becomes one transformation node; the contrasting evidence and open question receive the space.

### 7. Zhong Ou: populating research templates

- **Message:** source material becomes a structured research template that analysts verify and assess.
- **SEE:** three source objects → compact LLM population step → native three-row research template. Rows show Operating performance / Sales volume up 10%; Business driver / Restocking lifted shipments; Open question / Will restocking continue? A human check endpoint receives the template. Feature the reported efficiency figure with its qualification nearby.
- **SAY:** explain source checking and the analyst's added assessment; preserve the report's full wording and source context.
- **Visible facts:** approximately 50% higher **research-preparation efficiency**, reported by Zhong Ou as of May 2026; the three illustrative entries and the open question.
- **Trade-off:** the template is the central output. The statistic supports the example and retains its precise scope.

### 8. Proposed application: company research

- **Message:** sources, calculation tools and LLM comparison support a draft research view that the analyst judges.
- **SEE:** all three Company A sources visibly merge into the LLM. Show a separate neutral calculation-tool node with labeled request/result paths. Show a concise source-backed draft output and an analyst endpoint: “Check sources / Test thesis / Form view.” The calculation result can be one short evidence group: revenue +10%, volume +10%, average selling price unchanged.
- **SAY:** explain how restocking supports the growth interpretation, why reports disagree on sustainability, and why demand/input costs remain follow-up topics. Preserve the complete draft research summary with [1]–[3] source meanings in notes.
- **Visible facts:** quarter financials/units from4; the three sources; restocking; uncertainty over continuation/sustainability; both 10% changes and unchanged price. The LLM links drivers and compares views; tools calculate.
- **Trade-off:** sources, model, tools, draft and human judgment must each be traceable. Allocate output space by shortening explanatory labels, rather than turning the tool result into the largest panel.

### 9. Preparing a bond quote request

- **Message:** the trader mediates a manager request, system queries and counterparty quotes before returning a summary.
- **SEE:** four explicit actors: Portfolio manager, Trader, Market/holdings systems, Counterparty. PM → Trader carries “Company A / within 2 years.” Trader ↔ systems has “Query” and “Bonds + holdings” paths. Trader ↔ counterparty has separate “Request offers” and “Offer quotes” paths. Trader → PM returns a bond/quote summary. Keep main actors neutral and Company A material teal.
- **SAY:** explain screening, holdings checks, timestamps, copying messages and discussing next steps. Preserve the original four-stage preparation account in notes.
- **Visible facts:** Company A; bonds maturing within two years; request for offers/buying interest; price and available size are returned by the counterparty. This is the current workflow, so no LLM appears.
- **Trade-off:** an actor/transfer diagram replaces four prose columns. Numbering transfers is optional where it clarifies the sequence.

### 10. Trading support at Southern and Aegon-Industrial

- **Message:** two peer workflows support request execution and extraction from trading records.
- **SEE:** two short labeled lanes. Southern/Xiaonan: User request → LLM interprets/selects tools → Systems run task → User reviews result. Aegon-Industrial: Qtrade records → AI extracts fields → Match/route → Portfolio manager submits instruction. Show records as editable material and fields as Bond / Side / Price / Size.
- **SAY:** explain Xiaonan's queries, screening, instructions and notifications; describe matching/routing and the manager's separate submission step in the second example.
- **Visible facts:** organization attribution; the reported AI/LLM role in each lane; Qtrade field types; manager submission remains a human action.
- **Trade-off:** short transformations make the two examples comparable. Their different scopes remain distinct in notes and labels.

### 11. Proposed application: bond quote preparation

- **Message:** the LLM interprets a request and extracts trader-supplied quotes to prepare a verifiable summary.
- **SEE:** a request path to LLM query criteria and the systems' bond/holdings result; a distinct **Trader-supplied quote** object to the LLM extraction step; both feed the native editable bond/quote table. Beneath the table show Trader verifies → Manager reviews with trader. Keep quote supply separate from system holdings.
- **SAY:** explain criteria extraction, tool execution, received-quote extraction and verification of source, timestamp and amount. Preserve all source text in notes.
- **Visible facts:** Company A, buy/offer request, maturity within 2 years; Bond A maturity1.2 years; current holding RMB 20m **face value**; available RMB 20m **face value**; clean price 100.20 **per RMB 100 face value**. Keep holdings and availability in different table columns.
- **Trade-off:** the table is the main output. Diagram labels can be short because table evidence supplies the precise numbers/units. The LLM extracts received records; the proposal does not imply that it obtains live counterparty quotes autonomously.

## Batch 2: pages 12–24

### 12. Preparing a quarterly client update

- **Message:** the relationship manager selects, checks and adapts existing sources to answer a client's questions.
- **SEE:** client question plus three source objects (portfolio-manager views, product documentation, previous communications) converge on a neutral relationship-manager work area. Show concise Select → Check → Adapt actions and a purple quarterly-update output. Small related output objects can identify product Q&A and RFP responses using the same sources. Highlight Client materials.
- **SAY:** explain repeated searching, confirming the fund/reporting period and adapting wording to the client's needs.
- **Visible facts:** Company A; “What changed?” and “What should we watch?”; the three source families; human ownership. This remains the current workflow.
- **Trade-off:** show the source-to-client-material transformation; detailed task lists remain in notes.

### 13. Tianhong: investment views and market commentary

- **Message:** the LLM consolidates recent investment views into useful client-facing summaries.
- **SEE:** a small stack of presentations/commentary/reports → LLM Find / Deduplicate / Summarize → purple client-team summary. Include concise evidence of the resulting view: higher sales volume supported revenue growth; raw-material costs remain a focus. A client-facing-team endpoint receives the summary.
- **SAY:** explain selection by portfolio manager or product, source checking and the weekly-sector/daily-market-commentary applications. Preserve the complete original source quotation and summary in notes.
- **Visible facts:** Tianhong attribution; Company A's volume-driven growth and raw-material monitoring; the LLM's consolidation role.
- **Trade-off:** the material stack communicates multiple-source consolidation. One useful summary receives more emphasis than repeated source prose.

### 14. ICBCUBS: drafting institutional RFP responses

- **Message:** a source-backed draft answers a specific institutional question and then receives business review.
- **SEE:** client question (“How is investment research organized?”) and an internal research-process source merge into the LLM retrieval/drafting role. The source can contain a tiny Analyst → Research → Portfolio-manager discussion diagram. A neutral/structural-blue draft-response document retains the two answer sentences and a source reference; a business-team check follows. This independent RFP is distinct from the recurring purple quarterly client update.
- **SAY:** explain retrieval, responsibility identification and tailoring to the client's requirements. Preserve FundGPT's knowledge-base maintenance, question analysis, review and RFP-drafting scope in notes.
- **Visible facts:** analysts conduct company research; portfolio managers discuss the resulting investment views; answer grounded in the internal process description; business team reviews.
- **Trade-off:** the source diagram replaces its repeated prose, while the answer remains a purposeful readable excerpt.

### 15. Proposed application: drafting client updates

- **Message:** supplied client needs and investment/product sources become an initial draft for human review.
- **SEE:** three small inputs (client question, existing investment view, Q2 product information) merge into LLM Select / Draft. A larger purple V1 document shows the complete two-sentence investment view and compact fund/source/risk fields. A client-team endpoint checks and submits V1. The short fund name, older source and generic disclosure are deliberate evidence for the following review sequence.
- **SAY:** explain how the draft is assembled, its source basis and submission for review. Keep full wording and citations in notes.
- **Visible facts:** V1 identity; Product A Select; Q2 2026 source, V1; both V1 investment-view sentences; “Investing involves risk.”
- **Trade-off:** this document is evidence, so its compact field text legitimately remains visible. The drafting procedure becomes concise shapes and labels.

### 16. Reviewing client communications

- **Message:** the draft omits a growth driver and the source's uncertainty, which the reviewer must detect.
- **SEE:** purple V1 investment-view excerpt and the current portfolio-manager presentation feed a neutral Reviewer compares step. Show the two specific review questions/findings: Growth driver included? Uncertainty retained? Use neutral brackets/edge markers to relate passages under review. A small check label can retain fund/source/risk checking as the wider task.
- **SAY:** contrast the two claims and explain why stating volume growth alone loses the restocking driver and continuation uncertainty. Preserve the complete document/source text and review criteria in notes.
- **Visible facts:** both V1 investment-view sentences; source says channel restocking lifted volumes and continuation is uncertain. Source and draft must remain distinguishable.
- **Trade-off:** focus this page on the investment-view mismatch. Other fields become explicit review findings on 17. Yellow is reserved for actual changes later.

### 17. Penghua and Yingmi: reviewing client materials

- **Message:** source/rule-based review produces explained edits that the author revises and reviewers check again.
- **SEE:** a compact V1 material object plus current sources/review rules feed an LLM-assisted review step. Three output findings connect to the relevant fields: Full fund name/current period; Restocking driver + continuation uncertainty; Specific NAV/capital-risk wording. Show Author revises and a clear Recheck return path. Attribute Penghua's suggested edits and Yingmi's review/revision/repeat-review scope within the relevant flow.
- **SAY:** explain each issue and the two firms' distinct reported practices. Preserve complete V1 wording, suggested edits and Penghua's 91% acceptance-of-suggested-edits note in notes/source.
- **Visible facts:** the three issue categories; specific restocking/uncertainty meaning; human revision and repeat review. Any displayed 91% must explicitly mean acceptance of suggested edits.
- **Trade-off:** concise findings guide the talk; they should still explain the issue, rather than consist of unsupported isolated keywords. Keep V1 focus markers distinct from change highlighting.

### 18. Proposed application: reviewing client updates

- **Message:** supplied sources support matching and explained revisions; people approve and check the revised material.
- **SEE:** small V1/current-source input objects → neutral document-tool matching → LLM Explain / Propose edits → larger purple V2 excerpt → Author approval / Reviewer check. Retain both V2 investment-view sentences together. Show the full fund name and Q3 source compactly where possible. Keep the approval handoff visible and preserve the division between matching and language interpretation.
- **SAY:** explain the source rationale, current product/risk wording and responsibilities. Full V1/V2 documents, including all metadata and disclosures, remain in notes/source.
- **Visible facts:** V2 identity; restocking supports sales-volume growth; continued restocking is uncertain; raw-material-cost monitoring is retained. Match the approved wording. Use yellow on changed phrases, leaving retained words unhighlighted. In the investment view, changed spans include “Channel restocking supported,” “sales volume,” and “whether restocking continues, alongside.”
- **Trade-off:**15–18 already form the sequence. Small V1 inputs on 18 suffice; the larger V2 excerpt and revision/approval mechanism receive the space. The two evidence sentences remain complete rather than becoming yellow fragments alone.
- **Document boundary:** the excerpt contains actual client-facing wording. Omit the synthetic status line “Risk wording aligned to current product source” from inside V2; the complete approved risk disclosure remains in notes. Show the actual disclosure only if that field is deliberately included as evidence.

### 19. Investigating a risk alert

- **Message:** a risk analyst gathers exposure, rule and issuer evidence for the same event.
- **SEE:** prominent teal Company A alert enters a neutral risk-analyst work area. Three source branches identify Holdings, Contracts/policies and Issuer research, linked to concise questions: Exposed funds? Applicable rules? Impact? Their evidence converges into the analyst's event assessment. Make the parallel searches clear rather than implying a compulsory three-stage sequence.
- **SAY:** explain searches across systems/documents and the repeated issuer matching for each alert.
- **Visible facts:** Company A credit rating on watch; operating cash flow under pressure; three evidence needs; assessment remains human work on this current-workflow page.
- **Trade-off:** the alert and collection relationships lead the audience. Detailed search/check sentences move to notes.

### 20. Risk analysis at China Universal and Tianhong

- **Message:** peers use source extraction, rule explanation and event comparison to support risk work.
- **SEE:** two attributed case areas. China Universal shows custodian alert → LLM extraction → risk workspace, and source regulations/controls/contracts → system rule links → LLM trigger explanation. Tianhong shows event/past-case information → LLM comparison/assessment → investment and risk teams' discussion. Attach source documents to the rule-explanation step.
- **SAY:** explain event details, comparable events, industry relationships/sentiment and follow-up actions. Preserve the complete reported scopes and source citations.
- **Visible facts:** both organization names; their distinct mechanisms; explanations grounded in source text; teams discuss implications.
- **Trade-off:** China Universal has two related functions while Tianhong has one event-analysis chain. The composition may differ inside the two case areas to preserve that distinction.

### 21. Proposed application: credit-risk assessment

- **Message:** linking an alert to supplied holdings and monitoring requirements produces a checkable assessment and follow-up.
- **SEE:** three input objects (Company A alert, holdings record, monitoring requirement) merge into LLM links evidence. A structured native output has Assessment / Affected fund / Research follow-up fields. Show human handoffs: Risk staff verify → Analyst updates credit assessment → Portfolio manager discusses response. The holdings record is supplied evidence, not an implied live query.
- **SAY:** explain issuer matching, clauses/research interpretation, debt-service implications and the professional checks.
- **Visible facts:** credit watch/cash-flow pressure; Product A holds Company A bonds; RMB 20m **face value**; update issuer research after a credit event; assess cash-flow trends. Preserve the stated causal meaning of cash-flow pressure affecting capacity to service debt.
- **Trade-off:** concise field grouping replaces the long output paragraph, while preserving the particular issuer, exposure and action.

### 22. Processing operational documents

- **Message:** operations converts incoming material into records and propagates document revisions.
- **SEE:** two manual workflows. First: fax/scan → Operations enters/validates → business record. Second: purple V1/V2 pair → Operations compares → change summary → revision of related documents → updated materials. Feed a related-document stack into the final revision step so the change-summary dependency is visible. Highlight Document processing.
- **SAY:** explain rekeying, interpretation and applying the same change consistently across materials.
- **Visible facts:** fax/scanned inputs; V1/V2 comparison; change summary; related-document updating. Operations owns the work; no LLM appears on this current-workflow page.
- **Trade-off:** the original three rows become two meaningful flows; comparison and related revision remain connected.

### 23. HuaAn and ICBCUBS: document processing

- **Message:** automated extraction populates records, while document comparison identifies meaningful additions.
- **SEE:** HuaAn lane: fax/form → model reads/extracts → client-service record, with the reported figure and scope. ICBCUBS lane: both existing V1/V2 inputs merge into Model compares → native comparison result containing readable V1/V2 investment-view excerpts. Yellow identifies added restocking/continuation information; retained raw-material monitoring remains plain.
- **SAY:** explain supported PDF/Word/scanned formats, change highlighting, typo checks and export. Preserve the full original passages and source details.
- **Visible facts:** HuaAn's **more than 80%** relates to automated data entry of faxes handled by its **direct-sales counter**; both client versions exist before comparison; added driver/uncertainty and retained costs remain intelligible.
- **Trade-off:** the model compares existing V1/V2; its arrow must lead to a comparison result, not imply that the comparison model created V2. Evidence excerpts receive the larger portion of the lower lane.

### 24. Proposed application: document change analysis

- **Message:** tools locate changes, the LLM interprets their meaning, and operations files/propagates the result.
- **SEE:** purple V1/V2 pair → Document tools match passages → LLM explains changes → native change-summary object. Its short fields distinguish Added growth driver / Added monitoring question / Retained cost monitoring. Operations receives the summary and branches to Filed with V2 and Related updates/Q&A revised.
- **SAY:** explain fund-name/period/wording matching, new-versus-retained information and how related materials using the view are identified and updated. Preserve the complete change summary and operational check wording in notes.
- **Visible facts:** channel restocking as added driver; whether restocking continues as added monitoring; raw-material costs retained; operations checks and files with V2.
- **Trade-off:** a semantic change summary is the output, distinct from 23's literal comparison. Show the downstream operational use rather than merely enlarging another text frame.

## Batch 3: pages 25–33

### 25. Developing a document comparison tool

- **Message:** developing the tool requires translating a business rule into code, testing it and debugging false positives.
- **SEE:** purple V1/V2 document pair with a repeated-header region marked Ignore and body region marked Compare. A neutral developer owns Requirements → Code → Test, with a return path from a concrete failure (“Repeated header flagged”) to code/debugging. End with the comparison-tool output.
- **SAY:** explain additions/deletions/edits, paragraph matching, line/page-break problems and repeated debugging.
- **Visible facts:** compare the two versions; ignore repeated page headers; retain genuine body-text changes; testing can produce header false positives. Highlight Tool development.
- **Trade-off:** structural header/body labels suffice as an illustrative sample; avoid inventing additional financial or document wording. The test failure makes the development burden tangible.

### 26. E Fund and Invesco Great Wall: development support

- **Message:** peer firms use language models for coding support, with testing/review remaining developer work.
- **SEE:** two compact attributed case flows. E Fund: Developer task → LLM code/tests → Developer tests/feedback. Invesco Great Wall: Quantitative-team task → Locally deployed model coding support → Developer checks. Keep feedback visible where supported. Both organization statements receive equal typographic status.
- **SAY:** explain examples/expected results, generated processing code, testing and refinement. Preserve the full original common illustrative development workflow and the purple comparison-task context in notes.
- **Visible facts:** E Fund development/testing; Invesco Great Wall quantitative-team locally deployed coding support; developer responsibility. Preserve each firm's distinct reported scope.
- **Trade-off:** two short case flows avoid attributing every testing capability to both firms. Page 27 supplies the detailed proposed workflow for the recurring comparison tool.

### 27. Proposed application: software development support

- **Message:** examples, test failures and human feedback guide iterative LLM-assisted development.
- **SEE:** retain the six-stage return path: Developer examples → LLM code/tests → Test runner → Developer explains failure → LLM revises → Developer retests/delivers. Purple V1/V2 examples feed the first step. The test-result object states “Body changes detected / Header changes wrongly flagged”; the correction states “Exclude headers / Retain body changes.” Deliver a tool and user guide at the endpoint.
- **SAY:** explain matching paragraphs, the header filter, regression testing, code review and repeated testing.
- **Visible facts:** six distinct roles/actions; test runner executes tests; LLM drafts/revises; developer defines expected results, interprets failures and retests. A regression test protects the header fix.
- **Trade-off:** keep the useful loop geometry, with short labels replacing procedural sentences. The visible failure and correction are the evidence of the feedback mechanism.

### 28. Other back-office applications

- **Message:** additional back-office tasks combine language interpretation with sources or execution tools.
- **SEE:** three compact attributed flows. Employee question → LLM retrieves/explains guidance → Employee guidance (China Merchants/Ping An). Email/attachments/links → LLM context/intent → Detection tools → Security response (Maxwealth). Fund/period/metric request → LLM interpretation → Contribution algorithms → LLM analytical summary (China Universal patent proposal). The map highlights Back office; these additional cases need not be assigned to one of the seven principal task nodes.
- **SAY:** explain source retrieval, tool invocation and the separation of language interpretation from quantitative computation.
- **Visible facts:** organization names; the algorithms' distinct calculation role; China Universal case clearly labeled as a **patent proposal**; employee/security/analytics outputs.
- **Trade-off:** short native flows show different mechanisms. Preserve full scopes, patent identity and source attribution in notes.

### 29. Seven proposed applications

- **Message:** the seven proposals produce specific outputs for identifiable staff roles.
- **SEE:** full firm map with three office branches and seven task/output nodes. Each node pairs its recipient with a concise artifact: Analyst/source-backed summary; Trader/bond-quote summary; Client team/update-Q&A; Reviewer/findings-revisions; Risk team/assessment-follow-up; Operations/records-change summary; Developer/code-tests. Keep the office/task grouping identical to 3. A human-check/judgment line can join the summary beneath the map.
- **SAY:** connect each output to the case already shown and explain the shared reading/comparison/drafting contribution.
- **Visible facts:** all seven tasks, staff recipients and outputs; human verification/judgment. Preserve the full approved output descriptions in notes. No duplicate mini-map.
- **Trade-off:** this is an outcome map rather than a repeat of the opening capability descriptions.

### 30. Two information flows across the firm

- **Message:** Company A information and the client-update object connect work across office boundaries.
- **SEE:** two native horizontal lanes across Front / Middle / Back office. Teal Company A material links research/bond summaries, risk assessment/exposure monitoring and related-document maintenance. Purple client material progresses Draft V1 → Reviewed V2 → Version comparison/related updates. Label information transfers; Company A sharing can be bidirectional where appropriate rather than appearing to cause a credit event. The mini-map highlights the participating six business tasks; Tool development remains supporting context.
- **SAY:** explain how shared issuer identity, sources and version history reduce repeated searches and inconsistent materials. Preserve both complete original information-flow descriptions.
- **Visible facts:** both recurring objects/colors; three office boundaries; V1/V2 states; downstream comparison and related-material updating.
- **Trade-off:** use object states and handoffs as the row content. The detailed task workflows have already been explained.

### 31. Shared information, models and tools

- **Message:** shared approved information supports distinct language/tool roles that return a business output to staff.
- **SEE:** staff request → business application → distinct LLM and tools roles, with an explicit request/result exchange. A shared approved-source foundation visibly supports both. Return one concrete output, such as a purple client-update draft, to a staff check endpoint. The map highlights the shared firm-wide span. Keep dependency links distinct from directional request/return arrows.
- **SAY:** explain interpretation/comparison/drafting, system queries/calculations/file processing/code tests, access controls/source references/version history and candidate model evaluation.
- **Visible facts:** approved documents/knowledge/business data; LLM/tool division; output returned to people; application context across the seven tasks.
- **Trade-off:** a concrete output anchors the shared architecture. Qwen and DeepSeek remain **candidates for task evaluation** in notes/supporting material, rather than dominating the business mechanism.

### 32. Proposed implementation sequence

- **Message:** implementation proceeds through three business-led phases with concrete deliverables and owners.
- **SEE:** connected three-phase progression with attached stage markers. Phase1 Research/client communications → sample tasks, sources, initial applications. Phase2 Trading/operations → data definitions, query interfaces, document workflows. Phase3 Development/internal services → tools, guides, maintenance owners. Keep team labels aligned below the phase headings; use small editable deliverable objects. Map highlights the firm-wide span.
- **SAY:** explain participating Research/Sales/Compliance/IT, Trading/Operations/IT and Business/IT teams, sequencing and the complete deliverables.
- **Visible facts:** phase order; business areas; deliverable families; named maintenance ownership in the last phase. Keep the sequence undated because no schedule was approved.
- **Trade-off:** a clear phase diagram guides the talk; team and deliverable detail can use short labels with full descriptions in notes.

### 33. Evaluating application use and task outcomes

- **Message:** compare task outcomes with a baseline and use the findings to refine the workflow.
- **SEE:** Baseline enters an application-use → Record results → Team review/refine cycle. Attach four concise measures to the results stage: Completion time, Output use, Rework, Repeat usage. A return path shows subsequent use after refinement. Highlight Research and Client materials as the initial evaluation focus in the map.
- **SAY:** define time from task start to completed output, actual use of analysis/materials, revision rounds/repeated checks and continued employee use. Explain baseline comparison and refinement without inventing observed improvements or numerical targets.
- **Visible facts:** initial research/client-communications focus; all four measures; baseline and feedback relationships; human review of results.
- **Trade-off:** measures are instruments within the evaluation cycle, rather than four independent paragraphs. Full measure definitions remain in notes.

## Collaboration status

All 33 page proposals are recorded. The author may implement these batches and raise concrete semantic or layout trade-offs. Review will inspect small rendered batches, identify actual mechanism/evidence/notes defects early, and recheck repaired pages. Root handles native PowerPoint checks and the final local commit.

### Current working status

| Scope | Final status |
|---|---|
| Visual pages1–33 | All individually inspected across versioned batches; all local findings resolved. Final 2/4/9 caption/clearance changes and 17 attribution frame checked on immutable output. |
| Notes | All 33 final embedded notes match the reviewed notes source. Cover AI-image credit, 2's punctuation and 18's real full risk disclosure verified. Relevant V1/V2 evidence and source URLs are present. |
| Final reconciliation | SHA256 `1dae3a54c474190f1ca41ddbbd1a923d61929df714f861828547a59ddd39a2e4` verified. All 33 final-render input/PNG hashes verified; 30 PNGs exactly match their latest inspected batches; changed 2/4/9 inspected again. |
| Reviewer findings | None outstanding. See FINAL-REVIEW.md. |
| Coordinator handoff | Native PowerPoint/package checks and the final local commit remain with root. |

Unchanged passed pages require no further reopening. The final review is attached to the immutable hash above.

### Draft-stage review: batch 1

Reviewed pages1–11 rendered from candidate SHA256 `269073ccce3d2225cb30f71d516529b3b29fe292068546e2f7cc2af4c63dae0b`.

- **Keep:**1/2/3/9 compositions. The map/header are readable.9 restores distinct actors, query/result, offer-request/return and manager-summary paths.8's source merge, tool exchange and analyst handoff also work once its local fit defects are repaired.
- **4/8:** fit all financial/source evidence inside its native object, including sales-volume units.4's merge line must clear the Analyst preparation label.8 needs source identifiers[1]–[3] matching the draft references.
- **5/6:** attach5's analyst handoff to the whole driver analysis; its arrow currently leaves only the last leaf.6's source-check path should reach both reports, not only ReportB.
- **7/10:** fix7's visible word/number spacing. Name the trading system as10's Qtrade routing destination.
- **11:** route holdings and quote fields into a common summary merge, or their correct columns; the current Holdings arrow points to Available size. Separate quote heading/body, clear the summary caption from its connector, and separate human checks from the table body. Table figures and financial units are correct.
- **Notes:** remove design commentary from the proposed spoken explanation, including map/line/lane descriptions and defensive exclusions. Keep source inventories in durable approved-content material. Usable notes retain direct business explanation, relevant full evidence and references.

These are local repair targets for the next rendered batch. They preserve the agreed mechanisms.

**Targeted repair check, candidate `e05fd316…`:**4/5/6/7/10 issues above are resolved.8 now has legible source units, matching source IDs and a fitted analyst role; its tools role still needs enough height for “unchanged,” and[3] should stay with its claim.11 now merges both inputs into the LLM summary correctly; its native data row must still be cleared of the human-check boxes/arrowhead so “1.2 years” and all values are fully visible. Recheck8/11 after that local repair while later-page production continues.

**Second targeted check, candidate `dfc46635…`:**8/11 local fit repairs are resolved.11's complete native data row and human checks are separated;8's source IDs, tools role and claim citation fit. One later8 wording/width improvement is being made by the author to keep the sales-volume result together and state that views differ on sustainability.

### Draft-stage review: batch 2

Reviewed pages12–24 and the actual embedded notes at candidate SHA256 `a7c3dafa6b83f1bc6444b45f7903643d34ca91449714e6c0d7ccd0b8eac8653b`.

- **Keep:**12/13/14/15/17/18/19 mechanisms.14 correctly distinguishes the independent RFP with neutral/blue.18 preserves both V2 investment-view sentences, precise changed spans, retained cost monitoring, matching/revision roles and human approval/checking.
- **16:** join the reviewer output to both finding boxes with a proper fork.
- **20/21:** clear20's Sources heading/body overlap.21 needs a fitted Requirement object, separation from the human row and a return path clear of that input; retain “Company A bonds” and “RMB 20m face value.”
- **23:** keep the full comparison evidence; fit the last highlighted line within the output frame and correct “More than 80%” spacing.
- **24:** retain precise single-line meanings: “Added driver: channel restocking”; “Added question: whether restocking continues”; “Retained: raw-material cost monitoring.”
- **Color/notes:**22/24 generic related-file/Q&A containers stay neutral; the recurring versions/change summary/filed-V2 record stay purple. Notes now separate usable narration and full relevant evidence/URLs. Trim remaining design-commentary sentences from16/17/18.
