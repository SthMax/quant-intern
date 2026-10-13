# Three-Year TCO — On-Premise versus Commercial APIs

## Current cost inputs — 12 October 2026

The [Week 7 research](../../weekly/week-07-plan.md) uses **Spark＋Qwen27** for
personal work and **DeepSeek-V4.1-Flash** for shared Agents. Spark hardware is
**CNY58,407–61,840** rounded to whole CNY, an analytical China-delivery budget derived from the current
US storefront price. Initial implementation adds CNY10,000–20,000 for one user
or CNY20,000–37,500 for a shared setup; these alternatives are not added together.
See [Scenario 1](scenario-1-personal-agent-2026-09-24.md).

[Complete-server budgets](server-gpu-procurement-2026-10-12.md), in CNY10,000:
A100 eight-card refurbished SXM **91–102**; H100 eight-card SXM **285–298**;
H200 four-card NVL **161–283**; H200 eight-card SXM **291–304**. These are dated
analytical budgets with separately identified foreign price anchors, tax,
contingency and incremental support. The [price ledger](data/hardware-prices-2026-10-12.json)
records each component and excludes unquoted software/integration and facility
changes. Existing in-country equipment uses incremental reuse costs separately.

For [Scenario 3](scenario-3-company-agent-2026-09-23.md), compare one TP8 and two
TP4 instances on the same eight-H200 purchase. Current cache evidence supports
20×1M as a capacity candidate. Fixed-full-context latency and accepted-task
throughput remain unmeasured, so per-user hardware allocation is not yet a
cost per SLA-qualified concurrent slot. Add CPU tool workers only when they are
incremental: the historical two-node allowance is CNY120,000–260,000. The GPU
server's host RAM/CPU and existing NAS/RAG services are counted once.

The September sections below preserve earlier configuration and price inputs.
Their MiMo task simulations and short-context RAG performance do not supply the
new DeepSeek 1M workload rate.

**Phase 3 — Weeks 6–8.** The three-year comparison horizon and API alternative are
confirmed in [the final project plan](../../PROJECT_PLAN.md).
Status (12 October 2026): updated acquisition and capacity inputs; full three-year operating costs, API consumption and accepted-task volumes remain open.

**12 October update:** [external Spark measurements](dgx-spark-qwen27-external-benchmark-2026-10-12.md)
provide latency and output-rate inputs for a separate FP8-KV/MTP3 branch. Use the
full timing scope: CLI end-to-end output is 23.70/26.99 tokens/s at concurrency
4/8 for 131072 input and 8192 output per request; common decode-window rates
58.66/83.91 describe another interval. Task acceptance, human review and annual
volumes remain separate inputs. Cold random-token rates are not warm Agent task
rates. The immediate priority is the Thursday deployment presentation; these inputs
then feed the full TCO and pilot assessment.

**24 September acquisition baseline:** [Scenario 1](scenario-1-personal-agent-2026-09-24.md)
now compares one/two RTX PRO 6000D, M5 Ultra 256GB and DGX Spark using FP8-family
weights and full-precision KV. [Four-hardware cost inputs](data/scenario-1-personal-agent-2026-09-24/four-hardware-comparison.json)
replace the earlier six-workstation selection for current comparisons. Legacy
shared/independent-machine calculations remain historical. Add one-time software
deployment separately and count included server delivery/hardware support once.
Recurring electricity, support and accepted-task volume feed the three-year model.

**23 September update:** [Scenario 2](scenario-2-enterprise-rag-2026-09-23.md)
adds the Onyx Enterprise and Milvus/Open WebUI alternatives, two application/index
nodes, initial implementation person-days, and an explicit Onyx license variable.
The [scenario data](data/scenario-2-rag-2026-09-23/results.json) separates hardware,
initial implementation and license sensitivity. Performance values are uncalibrated
analytical scenarios; use measured accepted-task throughput for the later TCO.

[Scenario 3](scenario-3-company-agent-2026-09-23.md) adds Agent GPU capacity,
CPU execution workers and initial tool/skill integration. Its cost table separates
incremental spending from the combined Scenario 2/3 hardware total. The reuse case
assigns one existing Qwen GPU to Agents and reduces the RAG replica pool; dedicated
GPU cases retain Scenario 2 resources. Existing NAS, retrieval integration and
applicable platform licenses are counted once. Synthetic tasks/hour must be
replaced with observed accepted-task rates for the final cost-per-task comparison.

## Phase 2 acquisition inputs — 21 September 2026

The [workstation comparison](workstation-configurations-2026-09-21.md) records
seven personal/shared configurations and six three-person arrangements. The
[server study](server-gpu-procurement-2026-09-21.md) adds seven four/eight-GPU
complete-system scenarios. Reproducible amounts and sources are in the
[hardware price ledger](data/hardware-prices-2026-09-21.json).

Prices use CNY. Overseas observations use the explicit assumption USD 1 = CNY
7.00, not an observed spot rate. Domestic posted prices retain their own tax and
support status. Server and tower estimates separately include hardware VAT,
price contingency and three-year hardware-support allowances. Do not add those
included amounts again in the annual maintenance rows below. Apple and other
compact-system public prices have different base warranties and need a separately
priced equivalent support level for a like-for-like TCO comparison.

These are acquisition inputs. Add facility changes, electricity, software and
integration, staffing, backup/recovery, utilization and accepted-task volumes
when calculating the three-year comparison.

Compare production-grade on-premise deployment with commercial LLM API
consumption. The brief lists OAI, Anthropic, and DeepSeek as examples.
Provider inclusion in the comparison does not establish internal approval,
service availability, or suitability for a particular data class.

## Shared comparison basis

Use the same workload, output-quality threshold, service level, currency,
price date, and tax treatment across options. Connect on-premise capacity to the
[Phase 2 architecture](reference-architecture.md) and measured proof of concept.

| Input | Unit / definition | Low | Base | High | Source / assumption |
|---|---|---|---|---|---|
| Analysis horizon | 3 years / 36 months — confirmed | 3 | 3 | 3 | Final project plan |
| Users and peak concurrency | Users | | | | |
| Annual workload and growth | Tasks/year; growth by year | | | | |
| Input/output tokens | Tokens/task, including retries | | | | |
| Quality and human review | Accepted-task criteria; review minutes | | | | |
| Service hours / availability | Hours/year; target % | | | | |
| Inference latency | Seconds under stated load | | | | |
| Retained data / traffic | GB stored and transferred | | | | |
| Currency, FX, tax | Currency and valuation date | | | | |

## On-premise costs

| Component | Cost driver | Timing | Source ID / assumption |
|---|---|---|---|
| GPU servers, spares, and capacity | Server/GPU count and configuration | Upfront / refresh | |
| CPU, memory, storage, networking | Architecture specification | Upfront / refresh | |
| Rack and facility integration | Space, installation, power | Mixed | |
| Electricity | IT kWh, facility overhead, tariff | Annual | |
| Cooling | PUE or separately priced facility charge | Annual | |
| Software, commercial licenses, and support | Node/user/model terms | Mixed | |
| Maintenance | Support contracts and repair assumptions | Annual | |
| Security, monitoring, backup, recovery | Required controls and architecture | Mixed | |
| Implementation and model validation | Person-months | Upfront / changes | |
| Operations and governance personnel | FTE, release and evaluation effort | Annual | |

## Commercial API costs

| Component | Cost driver | Required evidence |
|---|---|---|
| Input and output consumption | Separate token volumes and prices | Dated provider prices with units and currency |
| Volume-based pricing | Usage tiers, discounts, commitments, minimums | Published terms or clearly labelled indicative quote |
| Cache / batch terms | Eligible volumes and separate rates | Applicable provider terms; no automatic discount assumption |
| Data egress and transfer | Billable GB by direction and service | Provider/network terms; mark unknown or not applicable with a reason |
| Security premiums | Incremental enterprise/private connectivity, isolation, retention, audit or contractual controls | Priced feature/quote or explicit scenario assumption |
| Platform integration and support | Gateway, application, retrieval, observability, support | Architecture and staffing assumptions |
| Review and governance | Validation, human review, monitoring, change management | Comparable effort assumptions to on-premise |

Do not assume a provider charges egress fees or security premiums. Record a
sourced charge, a justified non-applicable entry, or an unknown input requiring
sensitivity analysis. Avoid counting an included feature again as a premium.

## Calculation method

- Annual IT energy = average IT load in kW × operating hours.
- Facility energy = IT energy × PUE, where this method matches facility charging.
- Electricity cost = facility energy × tariff. Do not add cooling again if PUE
  or a facility charge already includes it.
- Annual API consumption cost = sum across billed input/output/cache/batch/volume
  categories of quantity × applicable price, plus relevant commitments/minimums.
- Three-year on-premise TCO = upfront implementation and capex + year 1, 2, and 3
  operating costs + refresh/contingency assumptions.
- Three-year API TCO = upfront integration + year 1, 2, and 3 consumption,
  transfer, security, platform, personnel, and governance costs.
- Cost per accepted task = three-year TCO / accepted tasks over the same period.

Model each year separately to capture growth, utilization, price changes, and
staffing. Report low/base/high scenarios and break-even volume where the inputs
support it. Keep cash TCO separate from depreciation or discounted-value views.

## Phase 3 output

A traceable three-year comparison, sensitivity table, major cost drivers, and
limitations. Link the model to the pilot proposal effort/cost/ROI assumptions
and the final report.
