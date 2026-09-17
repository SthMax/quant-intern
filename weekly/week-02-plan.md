# Week 2 Execution Plan — 7–11 September 2026

**Derived on:** 6 September 2026.

**Scope authority:** [Final mentor-confirmed project plan](../PROJECT_PLAN.md).

**Phase:** Phase 1 — Industry Research.

**Checkpoint:** Friday, 11 September 2026. Times below are Asia/Shanghai.

This is a working execution plan. The confirmed project brief remains final.
Week 2 completes and presents the Phase 1 company landscape and regulatory/MRM/CSRC
research. Technical assessment follows in Weeks 3–5; cost-benefit analysis and
pilot recommendations follow in Weeks 6–8.

## Starting point

The repository has a research structure, source schemas, and presentation outline.
At the 6 September review it contains **zero verified company entries and zero
registered external research sources**. Plan the week as active source collection,
verification, synthesis, and presentation preparation.

Confirmed terminology: COD is the infrastructure used in MSIM; MRM means model
risk management.

## Deliverables and acceptance criteria

| ID | Deliverable | Location | Completion criteria |
|---|---|---|---|
| W2-01 | Structured onshore fund-company database | [Company index](../knowledge-base/companies/index.md), with linked evidence notes | Distinct company count reported; eligibility, AUM/unit/metric/date/source, use cases, and disclosed partners recorded; missing disclosures labelled; count tested against mentor minimum if supplied |
| W2-02 | Regulatory/MRM/CSRC source matrix and synthesis | [Regulatory index](../knowledge-base/regulation/index.md), with linked evidence notes | Privacy, interpretability, and outsourcing each addressed with exact provisions or an explicit evidence gap; issuer, legal force, status, date, source content, interpretation, and applicability recorded |
| W2-03 | Traceable Markdown evidence base | [Source register](../knowledge-base/source-register.md) and [evidence template](../knowledge-base/templates/evidence-note.md) | Every material external claim points to a direct source and exact passage; research and human-check states recorded truthfully |
| W2-04 | Friday checkpoint presentation and evidence appendix | [Presentation outline](../presentation/deck-outline.md); final format to be chosen | Company landscape and regulatory findings traceable to W2-01/02/03; limitations and confirmed phase roadmap included |
| W2-05 | Phase 2 handoff | Handoff section below, updated after research/presentation | Findings translated into questions for model survey, architecture, and GPU proof of concept; mentor feedback recorded |

The phrase “at least onshore mutual fund companies” still has no numeric threshold.
Do not substitute a guessed number. Continue collecting qualifying companies,
report the actual count, and leave the numerical completion criterion open if the
mentor has not supplied it by Friday.

## Daily schedule

| Date | Main work | Concrete end-of-day output |
|---|---|---|
| Mon 7 Sep | Establish candidate universe and AUM comparison method; discover company disclosures; inventory authoritative regulatory and MRM sources | Candidate queue, initial source register, first verified company evidence, three-theme regulatory source inventory, unresolved-input list |
| Tue 8 Sep | Verify company identity and initiative detail; collect sourced AUM; classify use cases, maturity, AI/LLM type, and partners; begin regulatory extraction | Substantial company database with gaps visible; exact provisions and evidence notes started across the required themes |
| Wed 9 Sep | Close company evidence gaps; check regulatory dates/status and applicability; draft the three-theme synthesis and landscape findings | Research tables substantially complete; synthesis tied to sources; remaining unsupported claims or unavailable inputs explicitly listed |
| Thu 10 Sep | Build the presentation and appendix; trace each claim to its source; reconcile counts and AUM comparisons; prepare speaker notes | Complete presentation draft; citation/claim audit; working content freeze at 17:00 |
| Fri 11 Sep | Finish review, rehearse, present, and capture mentor feedback | Presentation and source-linked appendix; actual research coverage and unresolved items reported; Phase 2 handoff updated |

The Thursday cut-off is a proposed working convention. Record publication and
access dates per source, and log any material corrections/new sources added after
the cut-off before presenting.

## Company research workflow

1. Build a candidate list of onshore mutual fund managers and log discovery links.
   Prioritize firms with concrete public disclosures and traceable size data.
2. Verify the legal entity and each initiative from original company reports,
   announcements, filings, or properly attributed vendor disclosures.
3. Use separate company and initiative records: one company may have multiple
   initiatives but counts once toward the company requirement.
4. Capture AUM value, currency/unit, metric, entity scope, date, and source.
   Define size categories only on a comparable basis; mark incomparable entries.
5. Tag the required functions: research, trading, risk, marketing, compliance.
   Add supplemental categories only where needed.
6. Record models/stacks, technology partners, deployment maturity, and outcomes
   only to the extent disclosed. “Not disclosed” is a valid field value.
7. Synthesize patterns from the verified set, identify representative examples,
   and report evidence limitations. Do not generalize the sample into a claim
   about every onshore manager.

Evidence notes are saved as research proceeds and linked from the source
register. Candidate entries do not count as verified entries.

## Regulatory and MRM research workflow

1. Locate official instruments and authoritative guidance relevant to the three
   specified themes. Identify document type and jurisdiction.
2. Open the controlling/original text and capture exact title, issuer, provision,
   publication/effective dates, amendment/current status, and direct URL.
3. Write a faithful paraphrase tied to the passage. Keep legal force and
   applicability separate; a relevant topic does not establish that a provision
   applies to this particular entity or deployment.
4. For privacy, interpretability, and outsourcing, distinguish source content,
   practical interpretation, and unanswered internal-policy questions.
5. Use public MRM material with its jurisdiction/scope identified. Internal
   Morgan Stanley model risk management requirements need authorized evidence.
6. Follow material legal claims back to the original text during review and
   record verification status. Remove unsupported claims or present the gap.

This plan defines the research method; it does not assert that a particular
regulatory instrument or legal requirement has already been verified.

## Inputs and working decisions

| Input | Status | How work proceeds |
|---|---|---|
| Minimum company count | Still missing in final brief | Collect and verify candidates; report actual count; seek mentor number without inventing it |
| “Top tier” / asset-size measure | User requested size-first research; working cohort is reported top-20 non-money public AUM at 2026 Q2, ETF feeders excluded | Preserve secondary ranking provenance and separate official company AUM; cohort choice is not the mentor's missing minimum |
| AI versus LLM scope | Four report themes confirmed: research reasoning, controlled data querying, knowledge/compliance, and LLM-assisted quant; quant covers factor generation/iteration, text signals and research tools | Local deployment is a preference, not a case prerequisite; API-based frameworks qualify. Keep model serving separate from agent/framework assessment; no traditional-ML substitution or old-model tutorial expansion |
| MRM meaning | Confirmed: model risk management | Research relevant sources; identify applicable internal document/owner separately |
| COD meaning | Confirmed: infrastructure used in MSIM | Carry actual hardware/network/security questions into Phase 2 |
| Internal policy availability | Not supplied in repository | Continue public-source review and list internal applicability questions without reproducing restricted text |
| Presentation audience/time/language/format | Mentor and quant-department colleagues; user requested LaTeX report rendered to PDF on 9 Sep; Chinese working draft | Report saved under reports; live presentation time and final delivery review remain open |
| Research cut-off | Working proposal: 10 Sep, 17:00 | Log source dates and any subsequent material corrections |
| Model language proficiency and “fund outcomes” | Wording needs later operational detail | Carry to Phases 2/3; neither prevents Phase 1 research |

The intern owns research, notes, and the presentation. Mentor/internal stakeholder
inputs are tracked here for the user to coordinate; no outreach is scheduled by
this document.

## Friday review checklist

- [ ] Actual distinct verified company count stated; numerical target status clear.
- [ ] Company eligibility and AUM source/metric/date documented.
- [ ] Required functions and disclosed partners captured with unknowns visible.
- [ ] Privacy, model interpretability/MRM, and outsourcing synthesized.
- [ ] Material factual and legal claims resolve to source IDs, URLs, and passages.
- [ ] Instrument dates/status and applicability reasoning checked.
- [ ] Human-review status accurately recorded; no implied sign-off.
- [ ] Overview claims from the project brief independently sourced if used.
- [ ] Company/initiative counts and charts/tables agree.
- [ ] Presentation and appendix cover Phase 1 and show the confirmed roadmap.
- [ ] Feedback and Phase 2 input questions recorded after presentation.

## Phase 2 handoff — populate from Week 2 findings

| Phase 2 task | Input from Week 2 | Open question / evidence reference |
|---|---|---|
| Survey 5–8 open-source LLMs | Local research/RAG and transaction-parsing cases | FUND-007/011/013; choose models later against actual task requirements |
| Reference architecture | Service audience, data boundaries, outsourcing roles, AMAC deployment distinctions | REG-001/003/005/010; obtain COD-specific inputs |
| One-model local GPU proof of concept | Source-referenced financial text extraction/QA as candidate sample tasks | Peer evidence informs task design; no pilot selection or technical execution yet |
| Reusable financial NLP evaluation | General/financial evaluation and API/local comparability in AMAC 9.1.2 | REG-010; outcome/source-fidelity testing remains to be designed in Phase 2 |

## Completion log

### 6 September 2026 — research started ahead of Monday

- Read `RESEARCH_TOOLS.md` and used web/Exa discovery, original webpages, official
  PDF extraction, and selected-page visual checks.
- W2-01: six company notes, seven primary-source initiatives, six sourced AUM
  observations, and ten additional candidates. Numerical target and comparable
  public-fund AUM coverage remain open.
- W2-02: twelve official law/regulatory/standard/MRM/research sources inspected;
  initial synthesis covers privacy, interpretability, and outsourcing.
- W2-03: thirty registered sources, comprising twenty-five primary and five
  secondary/discovery candidates. All human checks remain pending.
- W2-04: [first research brief](../presentation/phase-1-research-brief.md) prepared;
  final slides and presentation review remain outstanding.
- W2-05: source-backed Phase 2 questions are recorded in the regulatory synthesis;
  mentor feedback is not yet available.

See [the research log](research-log-2026-09-06.md) for checks, retrieval limitations,
and next actions. These outputs are the initial batch, not completion of the
entire Week 2 plan.

### 6 September 2026 — size-first expansion and E Fund deep dive

The user prioritized large fund managers and authorized subagents. Research now
starts with a sourced 20-manager universe and records a disposition for all 20.
Fifteen have qualifying primary AI/LLM initiative evidence; five retain detailed
secondary/unresolved records. Dacheng remains a supplementary prior case.

Current catalogue: 21 dossiers, 16 primary-backed managers, 25 platform/workflow
records and 101 registered sources (68 primary / 29 candidate / 4 unresolved).
E Fund has a dedicated deep dive with chronology, named platforms, technical
details, control/metric limitations and original source trails.

- [Large-fund universe](../knowledge-base/companies/large-fund-universe-2026q2.md)
- [E Fund deep dive](../knowledge-base/companies/efund-llm-deep-dive.md)
- [Cross-manager synthesis](../knowledge-base/companies/large-fund-synthesis-2026-09-06.md)
- [Current presentation brief](../presentation/large-fund-research-update.md)
- [Research/review log](research-large-funds-2026-09-06.md)

The broader legal-status sweep, human verification, comparable official AUM gaps
and final presentation remain outstanding. No Phase 2 implementation or pilot
ranking was performed in this fund-focused pass.

### 9 September 2026 — Phase 1 LaTeX report

- Preserved the research baseline in commit `e51e4c9` before report authoring.
- Re-read the mentor-confirmed project plan and produced a [Phase 1 report](../reports/phase1-llm-industry-2026-09-09/README.md) with LaTeX source, PDF, charts, company tables and a source manifest.
- W2-04: report rewritten around business tasks and reader needs after independent mentor-agent review; final PDF and revision records are in the report directory. Rehearsal, live presentation and feedback from the actual mentor remain outstanding.
- W2-05: report translates all four themes into Phase 2 task/evaluation candidates and lists missing COD, internal-policy, data and cost inputs. No model deployment, benchmark or TCO calculation was performed.
- W2-01/02/03 remain source-based research, with independent human review and the mentor's missing numeric company target still open. The report distinguishes 20 core managers plus one supplementary dossier, source quality, LLM relevance and workflow completeness.

### 9 September 2026 — business-focused report rewrite

- Preserved the prior report at `39a2417`; rewrote the official PDF around four workflows, concrete inputs/outputs, author-reported results and conditional next-step choices. Internal scores and selection history are excluded.
- Independent mentor-agent v1 review prompted the rewrite; v2 review and the author response are retained in the report editorial folder. The final artifact has 24 physical pages and 46 source entries; full-page rendering, source links, source hashes and comparable AUM values were checked.
- Phase 1 conclusions remain distinct from model deployment, backtest reproduction, TCO/ROI and internal approval; none of those later-stage outcomes is claimed. Knowledge-base originals and the confirmed project plan remain unchanged.

### 9 September 2026 — authorial narrative and Table A overview

- Following the user's approval of an in-conversation sample, revised the full report into connected prose and added an opening overview of Table A before the four directions. Rewrote table cells as readable descriptions while preserving facts and source roles.
- The report now has 21 physical pages. Company outcomes, quantitative results and regulatory conditions remain sourced; the work is still Phase 1 research. Current verification and narrative revision records are in the report directory.
- Prior mentor-agent reviews remain historical records of the earlier version; no new independent mentor review, model deployment, backtest or internal approval is implied by this edit.

### 10 September 2026 — PowerPoint draft

- Committed the approved eight wording changes in `98bab07`.
- Prepared an editable [PowerPoint deck](../presentation/phase1-llm-industry-2026-09-10/README.md) from the report, with 18 main slides and six appendix slides. Speaker notes carry the Chinese talk track and source references.
- The deck retains the four research directions and Phase 1 scope. Actual presentation, mentor feedback and Phase 2 implementation remain future work.

### 15 September 2026 — Phase 2 handoff and mentor feedback

- The current report is the revised Phase 1 deliverable, and the 11 September PPT contains 20 main slides plus seven appendix slides. Current artifact descriptions are in the existing report and presentation directories.
- The user relayed feedback from the actual mentor: organize the story by the fund manager's front, middle, and back office; connect specific work to LLM responsibilities and architecture; explain one representative case for repeated mechanisms such as RAG.
- The mentor expects personal LLM use or a small data-center deployment serving dozens of users, with mature, maintainable software and economic viability as selection criteria.
- Execution now follows [the Weeks 3–5 plan](week-03-05-plan.md). It retains the confirmed 5–8-model survey, one-model local GPU proof of concept, and reference architecture, with full TCO and pilot recommendations in Weeks 6–8. Model deployment and performance testing have not yet been performed.
