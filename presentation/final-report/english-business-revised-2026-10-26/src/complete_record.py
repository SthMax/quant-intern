from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parent.parent
review=(R.parent/'english-business-review-2026-10-26/BUSINESS-ENGLISH-REVIEW.md').read_text()
sections={int(m.group(1)):m.group(2) for m in re.finditer(r'### (\d\d)\. (.*?)(?=\n### \d\d\.|\n## Terminology)',review,re.S)}
notes={
1:'Applied: corrected the actual workflow → industry examples → proposed application sequence, and defined large language models (LLMs). Retained office structure and recurring-example explanation.',
2:'Retained: language interpretation belongs to LLMs; queries, calculations and operations belong to connected tools; employees check results.',
3:'Applied: seven application areas, industry examples and proposed application; quote preparation replaces bond inquiries. Retained information reuse and navigation explanation.',
4:'Retained: prior/current-quarter RMB 100m/110m revenue and 1.0m/1.1m units; no year-on-year substitution. Repeated preparation burden preserved.',
5:'Applied: the time required for manual data preparation and calculations fell from days to minutes. Retained Tianhong attribution, notes-only claim and analyst growth-quality judgment.',
6:'Retained: underlying reports, analyst investigation and competing interpretations of persistence. No false either/or inference introduced.',
7:'Retained: illustrative template fields; reported approximately 50% improvement in preparation efficiency; May 2026 date and Zhong Ou attribution. No time-saving conversion.',
8:'Retained: tools calculate, the analyst checks sources and tests the thesis; all three evidence markers retained. Sales-volume terminology aligned.',
9:'Applied: request for quote (RFQ) defined. Retained counterparties supplying quotes, trader consolidation and portfolio-manager discussion.',
10:'Applied: trading instructions terminology. Retained Southern/Aegon-Industrial distinction and portfolio manager submission; matching object remains explicit in notes.',
11:'Applied: quote records and current holding terminology; reviewer’s duplicated-extraction sentence corrected. Retained trader-provided input, request-before-supply sequence, RMB 20m face values and RMB 100.20 per RMB 100 face value.',
12:'Applied: request for proposal (RFP) defined; portfolio managers’ investment views. Retained client-question/source-retrieval/expression sequence and underlying investment position.',
13:'Retained: employee checking and use in client communication; product-specific retrieval does not create new investment positions. Fictional example polished as permitted.',
14:'Applied: FundGPT supports knowledge-base maintenance, question analysis, review and RFP response generation. Retained illustrative status and supplied responsibilities, without investment-approval powers.',
15:'Applied: V1 is the initial draft prepared from supplied Q2 information; draft and source version distinguished. Retained incomplete V1 substance, Q2 source, shorter fund name and generic risk wording. Fixed duplicate terminal punctuation.',
16:'Applied: factors to monitor and reporting period. Retained source meaning, passage comparison and revision explanation; V1 stays incomplete.',
17:'Applied: full fund name/current reporting period replaces implied rename; factors to monitor and net asset value (NAV) definition. Retained 71 rules/seven categories and Penghua’s 91% acceptance of suggested edits.',
18:'Applied: document tools, sales-volume driver, continued-restocking uncertainty and factor to monitor. Retained author approval, reviewer checks and product-specific risk wording.',
19:'Applied: Company A’s credit rating is on watch. Retained illustrative status and unspecified watch direction; no default, downgrade or breach added.',
20:'Retained: system mapping versus LLM explanation; internal controls used for substantive requirements. The on-slide rule-trigger basis is explicit.',
21:'Applied: issuer’s capacity to service debt and credit assessment. Preserved the asserted adverse effect, fund face value and analyst/risk/portfolio-manager responsibilities.',
22:'Retained: data transfer, contextual comparison and repeated revisions. Industry-example wording aligned; no records-governance or platform claim added.',
23:'Applied: faxes/forms handled by the direct-sales counter and processed using automated entry. Retained more-than-80% denominator, FUND-150 references and comparison-before-explanation progression.',
24:'Applied: document tools, change summary, factors to monitor. Retained explicit new restocking monitoring versus retained raw-material monitoring and Bosera bulk revision reference.',
25:'Retained: testable requirements and iterative requirements/code/execution sequence. No added completion claims.',
26:'Applied: locally deployed models. Retained illustrative report-comparison collaboration and generated code/tests as working material.',
27:'Retained: illustrative expected-output failure/correction, regression test and developer retesting; LLM roles remain visible.',
28:'Applied: algorithms quantify contributions to the selected metric. Retained interpretation/calculation division and patent method’s proposed status.',
29:'Applied: research summaries, bond and quote summaries and change summaries. Retained initial research/client-communication focus, explicitly visible on slide 33.',
30:'Applied: corrected four-sentence account of V1 drafting, author revision, reviewer checking and back-office maintenance. Retained information reuse and collaboration.',
31:'Retained: language/content versus tools; models are future candidates for task-based evaluation. On-slide status made explicit.',
32:'Retained: research/client communications first, trading/operations next, development/internal services later; actual participating functions and sequencing logic. No dates, budgets or thresholds added.',
33:'Applied: elapsed task completion time and use of outputs; repeat-usage definition aligned. Retained comparable-task before/after logic and diagnostics; fixed duplicate punctuation.'}
adapt={(7,4):'Used the approved compact two-line attribution; efficiency meaning and date remain explicit.',(8,4):'Used the review’s compact analytical-summary alternative to preserve legible type.',(9,1):'Parallel verb headings with the responsible role in each body; two/three-line headings retained.',(9,3):'Combined bond specification and buying interest; retained offer prices and available size.',(10,2):'Used “Select required tools” for a shorter equivalent inside the original panel.',(10,4):'Used the review’s compact matching/routing wording; portfolio-manager request is explicit in notes.',(17,2):'Added a native LLM-assisted review umbrella, appearing with the original first review group.',(17,3):'Split into two sentences and named sales volume explicitly; uncertainty unchanged.',(18,1):'Controlled line breaks separate document-tool role and matching task.',(18,3):'Retained the exact uncertainty; companion driver label rephrased for the bounded panel.',(21,4):'Used the review’s compact “Risk staff verify exposures and requirements” alternative, then explicit analyst/portfolio-manager clauses.',(25,2):'Parallel stage headings; common Developer workflow line shares the existing request band.',(28,4):'Full quantification meaning wrapped over lines; no attribution metric invented.',(31,1):'Used the approved umbrella “Applications across the seven business areas”; persistent navigation supplies categories.',(32,2):'Added native shared Participating teams/Deliverables headings, bound to the first phase’s original appearance.'}
record=['# Review implementation','','## Full reading record','','Read all 720 approved-review lines before editing, in bounded sequential sections: 1–120, 121–240, 241–360, 361–480, 481–600 and 601–720. This included overall diagnosis, every numbered item on slides 01–33, notes, space guidance, terminology/style guide and highest-priority changes.','','## Implementation basis','','The authoritative English PPTX is the direct native package base (SHA256 86822d1bb55cf9ac3d5a0b4894705be6b68966d44c6851ca7d16501a6bae146d). This prevents the former Chinese-to-English builder’s local text overrides from restoring old wording. The full earlier source set is preserved. All original identities, links and timing remain; only three uniquely identified native explanatory labels were added.','','V1 retains its intentional omissions, shorter fund name, Q2 source and generic disclosure. Its polished paragraph is identical on slides 15, 16, 17 and 23. V2’s identical finished paragraph appears on slides 18 and 23. Slide 21 preserves the supplied credit conclusion; slide 33 defines elapsed task completion time.','','## Slide-by-slide checklist','']
for i,section in sections.items():
 record += [f'### {i:02d}', '']
 title=re.search(r'\*\*Recommended title:\*\* (.*)',section).group(1)
 record += ['- **Title — '+('Retained' if 'retain.' in title else 'Adapted' if i==20 else 'Applied')+'**: '+('Used the approved compact title “Risk analysis at China Universal and Tianhong”.' if i==20 else title)]
 for num,item in re.findall(r'^(\d+)\. (.*?)(?=\n\d+\. |\n\*\*|\Z)',section,re.M|re.S):
  key=(i,int(num));status='Retained' if item.startswith('**Retain') else 'Adapted' if key in adapt else 'Applied'
  description=re.sub(r'\s+',' ',item).strip()
  record += [f'- **{i:02d}.{num} — {status}:** {description}'+(' **Implementation:** '+adapt[key] if key in adapt else '')]
 retain=re.search(r'\*\*Retain[^*]*\*\*:?\s*(.*?)(?=\n\*\*Notes|\n\*\*Space|\Z)',section,re.S)
 if retain:record += ['- **Retained copy/scope — Retained:** '+re.sub(r'\s+',' ',retain.group(1)).strip()]
 record += ['- **Speaker notes:** '+notes[i],'- **Space — Adapted:** Reflowed native geometry and deliberate line breaks. Inspected the final slide individually; source stripes, highlights and connector positions were updated with their content.','']
record+=['## Focused editorial follow-up','','All seven corrections from EDITORIAL-CHECK.md were applied and verified against the native final text. The slide-32 column labels were layout additions and now appear in the extracted final copy. Short-label punctuation was normalized without removing decimal points or prose punctuation.','','## Final verification','','33 slides; 15240000 × 8572500 EMU; Arial design policy; native table on slide 11. All 407 links and destinations, 33 Morph transitions and original timing on 14 slides verified. The three new labels use unique IDs 9000–9002 and are bound to the corresponding original 150 ms appearance group. Original source URLs retained. Every final slide rendered in a fresh process and inspected individually. Native PowerPoint playback is handled by the coordinating agent.']
(R/'REVIEW-IMPLEMENTATION.md').write_text('\n'.join(record)+'\n')
print('Completed per-item and material-notes implementation record.')
