# Static business presentation design notes

This is a new draft for independent critique. The earlier corporate transfer edition and its acceptance are not an aesthetic approval of this version.

## Reference pages actually inspected

- Morgan Stanley 4Q2025 Strategic Update: cover, pages4,6,7 and9. [Official PDF](https://www.morganstanley.com/content/dam/msdotcom/en/about-us-ir/shareholder/4q2025-strategic-update.pdf).
- Morgan Stanley 4Q25 Fixed Income Investor Presentation, page5. [Official PDF](https://www.morganstanley.com/content/dam/msdotcom/en/about-us-ir/pdf/Morgan_Stanley_4Q25_Fixed_Income_Investor_Presentation.pdf).
- BlackRock 2025 Investor Day, pages4,12,22 and36. [Official PDF](https://s24.q4cdn.com/856567660/files/doc_presentations/2025/BLK-Investor-Day-2025-WEB.pdf). Page41's interactive overlay was excluded as a static design model.

Concrete lessons: MS07 uses a simple shared hierarchy and generous equal columns. MS09 aligns section headers and evidence while giving different evidence types their own space. MS06 makes the central outcome visually dominant. BLK22 shows a tangible output beside the producing method; its density and styling were not copied. BLK36 separates large stage markers, concise headings and supporting text in a timeline. The color palette, logos, black footers and business content of these references were not transplanted.

## Applied system

- Keep the exact measured corporate canvas and title/subtitle/body zones. The company logo and footer remain the master's responsibility.
- Replace the large card-like sidebar with plain, subordinate three-office context at the bottom of workflow pages. The task remains explicit in the subtitle. Full seven-task maps remain on3 and29;30 already supplies the office grid.
- Use full-width evidence columns, document/method comparisons, open workflow lanes, a driver tree, a native output table and a timeline according to the subject. Pale fills identify selected outputs or execution context; they do not frame every text group.
- Keep Company A evidence teal, client documents purple, structure blue, neutral supporting text and yellow revised wording. Do not use detached upper-right example tags.
- Arial and point sizes are design choices. Main content generally uses11–14pt, titles20.5pt, cover22pt; compact source/context text is lower priority. All text and diagrams remain editable. No transitions, animations, counters, control objects or jump actions remain.

## Copy coverage and changes

`src/copy-coverage.json` records each page's source keys reused, requested interface removal, legacy locator replacement, and deliberate caption removal. Every substantive source body is retained with its original words; line breaks and grouping change. Six redundant connector captions on9 were removed: Request, Bonds, Quotes, Query results, Quote request and Quote. Their actions remain explicit in the workflow and support lane. No financial fact or client-document passage was rewritten or omitted.

The cover adds the contextual line “Mainland asset management,” reflecting the established report scope. Slide3 speaker notes replace the obsolete direct-navigation instruction with “The task names locate the seven application areas across the firm.” All research URLs remain unchanged; other speaker notes are byte-identical.

## Per-page composition

| Slide | Composition | Applied reference lesson |
| --- | --- | --- |
| 01 | Minimal cover with full original landscape artwork | Morgan Stanley strategic-update cover: use whitespace and a simple cover hierarchy. |
| 02 | Input / LLM work / output overview with a dominant center column | Morgan Stanley09: shared header baseline and aligned evidence columns. |
| 03 | Seven-task editorial map in three open office columns | Morgan Stanley07: equal office columns and clear separation of hierarchy. |
| 04 | Three research evidence columns above the analyst preparation sequence | Morgan Stanley09: aligned evidence, with preparation work separated below. |
| 05 | Earnings-driver tree with a separate execution-tools lane | Morgan Stanley06: one dominant outcome with a structured driver tree. |
| 06 | Paired research hypotheses with a separated synthesis | Morgan Stanley09: common research question, paired hypotheses and separate synthesis. |
| 07 | Source-to-template mapping with one attributed performance callout | Morgan Stanley09: row alignment connects evidence to output fields. |
| 08 | Evidence / LLM analysis / calculation, with full-width output | BlackRock22: show the actual output next to the method; give the summary its own visual weight. |
| 09 | Four open trading stages with a separate systems/counterparty support lane | BlackRock36: readable sequence with consistent stage positions. |
| 10 | Two separate peer workflows with aligned four-stage lanes | Morgan Stanley09: aligned lanes distinguish two peer examples. |
| 11 | Query criteria and supplied quote into a native result table | BlackRock22: output table is concrete evidence, with method above. |
| 12 | Client questions and source material above a three-step preparation sequence | Morgan Stanley07: generous columns separate questions from inputs. |
| 13 | Source quotation and LLM method with an emphasized client-facing summary | BlackRock22: tangible client-facing output beside the producing method. |
| 14 | Reference material to LLM method to a traceable RFP response | BlackRock22: a traceable output document anchors the workflow. |
| 15 | Client inputs and explicit LLM drafting beside the complete V1 document | BlackRock22: document is the focal point; method remains explicit. |
| 16 | V1 document contrasted with current-source uncertainty and review criteria | Morgan Stanley09: comparison evidence stays aligned and separate. |
| 17 | Reviewed client document with three aligned LLM comments | BlackRock22: actual document and explanatory comments share a coherent reading order. |
| 18 | Three-stage review method beside the complete revised client document | BlackRock22: real output receives more area than the method. |
| 19 | Issuer risk alert above three evidence questions | Morgan Stanley06: alert has primary visual weight; questions form subordinate columns. |
| 20 | Two peer approaches aligned by risk activity | Morgan Stanley09: two aligned peer evidence columns. |
| 21 | Issuer evidence into an explicit LLM assessment and follow-up document | BlackRock22: evidence and explicit LLM tasks lead to a concrete output. |
| 22 | Open three-column operations matrix with one highlighted recurring example | Morgan Stanley09: aligned rows and restrained rules replace repeated panels. |
| 23 | Automated-entry evidence alongside a large V1/V2 document comparison | BlackRock22: a large output comparison makes the evidence tangible. |
| 24 | Version-analysis method beside a tangible change-summary document | BlackRock22: change-summary artifact is central to the method. |
| 25 | Three open development stages with explicit requirements, code and testing | BlackRock36: parallel stage alignment and clear sequence. |
| 26 | Three open development stages with explicit requirements, code and testing | BlackRock36: stage labels and actions have distinct visual levels. |
| 27 | Six-stage code-and-test feedback loop in a restrained serpentine flow | BlackRock36: sequence and feedback direction remain easy to follow. |
| 28 | Three compact application lanes separated by subject headings | Morgan Stanley09: repeated subject lanes with consistent evidence columns. |
| 29 | Seven-task editorial map in three open office columns | Morgan Stanley07: three-column office hierarchy. |
| 30 | Two colored information lanes across the three offices | Morgan Stanley07: shared office grid, with two information lanes. |
| 31 | Shared-capability hierarchy with distinct LLM and execution responsibilities | Morgan Stanley07: a clear hierarchy separates common platform from component roles. |
| 32 | Three-stage implementation timeline with aligned teams and deliverables | BlackRock36: generous timeline, large stage numbers and aligned detail rows. |
| 33 | Evaluation cycle above four concrete outcome measures | BlackRock36: sequence is separated from the outcome-measure section. |
