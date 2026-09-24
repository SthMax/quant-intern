# Pilot Candidate Assessment and Proposal Roadmap

**Phase 3 — Weeks 6–8.** Derived from [the final project plan](../../PROJECT_PLAN.md).
Status: assessment template; no pilots have been scored or recommended.

Identify **3–5 pilot candidates** with clear ROI metrics, prioritized by
implementation complexity and regulatory risk. Develop **2–5 concrete proposals**
from the candidate set for the final roadmap. Each proposal needs estimated
effort, cost, and expected impact. These are the two ranges in the confirmed brief.

## Candidate set

The following examples come from the brief and are starting points for assessment.

| Use case | Business owner / workflow | Implementation complexity | Regulatory risk | Proposed ROI measure | Evidence / assumptions |
|---|---|---|---|---|---|
| Earnings-call summarization | | | | Reviewed minutes saved per transcript; factual error rate | |
| Research drafting assistance | | | | Net drafting/review time saved; revision burden | |
| Financial-news sentiment analysis | | | | Label quality and analyst time saved; downstream usefulness | |
| Model-building coding assistance | | | | Accepted coding time saved after testing/review | |
| Automated compliance checking for fund outcomes | | | | Reviewer time and detection quality | Exact meaning of “fund outcomes” remains to be specified |

Phase 1 may record peer use cases; internal pilot prioritization belongs to Phase 3.
Peer-reported benefits are evidence about the peer disclosure, not measured internal
ROI.

## Proposed supporting score

Weights are a working assessment method, not mentor-mandated weights. Preserve
complexity and regulatory risk as explicit fields even when using a total score.
Scores run from 1 (least favorable) to 5 (most favorable); for risk/complexity,
higher means lower risk or easier implementation.

| Criterion | Weight | Question |
|---|---|---|
| Business value | 20% | What measurable benefit could this workflow produce? |
| Data safety | 20% | What data classifications and access requirements apply? |
| Failure containment | 15% | Can errors be detected and corrected before impact? |
| Evaluation clarity | 15% | Can usefulness and errors be measured reliably? |
| Regulatory/governance risk | 15% | What requirements and unresolved applicability issues affect it? |
| Implementation feasibility | 10% | What integration and infrastructure effort is needed? |
| Adoption fit | 5% | How well does it fit the desk's workflow? |

Weighted score = sum of (score / 5) × weight. Explain any decision that overrides
the numerical ranking.

## Required proposal fields

For each final proposal record:

- Workflow, user, input data, output, and human review.
- Baseline process, measurement period, task volume, and current time/cost.
- Proposed design and dependencies on model, architecture, and data access.
- Implementation complexity and regulatory/MRM risks, with source references.
- Estimated effort by role/person-days, elapsed duration, setup cost, and
  recurring cost.
- Expected impact, ROI metric, measurement method, and uncertainty.
- Quality threshold, failure criteria, and conditions for continuing the pilot.
- Priority, owner to be identified, and implementation sequence.

A proposed productivity calculation is:

- Net hours saved = task count × (baseline minutes − assisted minutes −
  incremental review/rework minutes) / 60.
- Net quantified benefit = monetized benefit − incremental costs.
- ROI = net quantified benefit / incremental costs over a stated period.

Check that review/rework is not already included in assisted time. Capacity saved
is not automatically cash saved. Connect cost assumptions to the
[three-year TCO](../infrastructure/tco-model.md); any shorter pilot ROI period
must be labelled separately.

## Final report handoff

Provide the 3–5-candidate comparison and prioritized 2–5-proposal roadmap to the
final research report, alongside the executive summary, methodology, findings,
and recommended next steps required by the brief.
