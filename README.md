# MSIM China On-Premise LLM Feasibility Study

Local research workspace for the two-month internship. The
[final, mentor-confirmed project plan](PROJECT_PLAN.md) controls project scope.
Derived schedules and templates must follow it.

## Confirmed phases

| Phase | Timing | Deliverables |
|---|---|---|
| 1 — Industry research | Weeks 1–2 | Onshore fund-company AI/LLM database; regulatory and model risk management (MRM)/CSRC summary |
| 2 — Technical feasibility | Weeks 3–5 | Survey of 5–8 open-source LLMs; on-premise reference architecture; one-model proof of concept on a local GPU workstation |
| 3 — Cost-benefit and recommendations | Weeks 6–8 | Three-year on-premise versus commercial API TCO; 3–5 pilot candidates with ROI metrics; final report and roadmap with 2–5 concrete proposals |

COD is the infrastructure used in MSIM. MRM means model risk management.
The confirmed plan also requires a reusable financial NLP evaluation framework
covering named-entity recognition, financial question answering, and
multi-document summarization.

## Current work: Weeks 3–5, technical feasibility

Use [the Weeks 3–5 execution plan](weekly/week-03-05-plan.md) for the mentor
feedback, schedule, deliverables, and acceptance criteria. Model research and
deployment are the main workstream. Phase 1 report/PPT restructuring follows
a separate [fixing plan](reports/phase1-llm-industry-2026-09-09/editorial/fixing-plan.md)
and does not gate research progress.

Phase 1 has produced a source-linked report and a 27-slide presentation. Phase 2
will compare 5–8 models, deploy one model on a local GPU, and develop reference
architectures using maintainable software and explicit workload assumptions.
Full three-year TCO and pilot recommendations remain in Weeks 6–8.

The [16 September model research](knowledge-base/models/model-survey-2026-09-16.md)
now follows the user's professional-workstation and quality requirements: eight
core Qwen, Gemma, DeepSeek, GLM and Kimi candidates, plus a pending-release
watchlist. The [license review](knowledge-base/models/license-review-2026-09-16.md)
examines commercial use, affiliates and internal-use conditions. Local
financial-task and performance tests have not started.

The 17 September [serving framework survey](knowledge-base/infrastructure/serving-framework-survey-2026-09-17.md)
and [harness survey](knowledge-base/infrastructure/harness-survey-2026-09-17.md)
compare GPU, Apple and heterogeneous runtime paths, workflow platforms and
general agents, including licenses and self-hosted API compatibility.
Updated on 18 September after checkpoint `9e5c2fe`: the harness survey now
explains product purpose, advantages and proposed fund-work uses, with additional
non-coding workspaces, research platforms and task assistants. Serving research
adds workload-specific performance and service-level comparisons.

The [Week 2 plan](weekly/week-02-plan.md) retains the historical research record.
The missing minimum company count and outstanding human/internal reviews remain
open; completed research artifacts do not establish those approvals.

## Research and version control

- Keep findings in the Markdown [knowledge base](knowledge-base/README.md), with
  source IDs, direct links, and exact locations that a reviewer can check.
- Keep supplied project context, verified source content, and researcher analysis
  distinguishable. The final plan itself is not evidence of industry adoption.
- Use public information for the landscape and public regulatory work. Handle
  internal requirements according to the user's stated confidentiality constraints.
- Do not store confidential internal documents, client/position data, credentials,
  or personal data in this repository.
- Internal MRM and other Morgan Stanley requirements require authorized internal
  evidence; public guidance cannot establish unpublished firm policy.
- Git is backed up to the public [SthMax/ms-intern](https://github.com/SthMax/ms-intern)
  repository. Releases package finalized research reports, presentations and
  selected model references for sharing.

## Current deliverables

The [Phase 2 technical research report](reports/phase2-technical-research-2026-09-18/README.md)
is available as of 18 September: 26 pages introducing and analyzing eight models,
licenses, serving frameworks, business applications and deployment patterns.
The current revision compares Open WebUI, LobeHub and Cherry Studio, focuses
personal task agents on Hermes and OpenClaw, and explains coding agents with
Skills/MCP as a general execution route. A financial-report/CSV example connects
these applications with personal and shared reference stacks.
The final PDF is distributed in the [Week 3 release](https://github.com/SthMax/ms-intern/releases/tag/phase2-week3-2026-09-18).
Its PDF, LaTeX source, references and validation records are kept together in the
report directory. It presents documentary research; local PoC results remain
outstanding.

The September 2026 delivery bundle contains:

- [Industry research report](reports/phase1-llm-industry-2026-09-09/report.pdf)
- [Presentation with speaker notes](presentation/phase1-llm-industry-2026-09-10/output/fund-llm-industry-2026-09-11-final.pptx)
- [DeepSeek-V4.1-Flash technical report](knowledge-base/models/deepseek-v4.1-flash/technical-report/DeepSeek_V41_Tech_Report.pdf)
- [DeepSeek architecture and KV Cache analysis, in Chinese](knowledge-base/models/deepseek-v4.1-flash/analysis/DeepSeek_V4_1_Flash_Architecture_and_KV_Cache_Guide_ZH.pdf)

## Repository map

| Location | Purpose |
|---|---|
| [PROJECT_PLAN.md](PROJECT_PLAN.md) | Final approved project brief and mentor clarifications |
| [Research tools](RESEARCH_TOOLS.md) | Tested MCP/tool inventory, research routing, and remaining setup gaps |
| [knowledge-base/README.md](knowledge-base/README.md) | Evidence workflow |
| [Company index](knowledge-base/companies/index.md) | Phase 1 database, candidates, coverage |
| [Regulatory index](knowledge-base/regulation/index.md) | Phase 1 provision map and MRM/internal questions |
| [Model evaluation](knowledge-base/models/benchmark-plan.md) | Phase 2 survey and reusable benchmark framework |
| [Current model survey](knowledge-base/models/model-survey-2026-09-16.md) | Eight core candidates, professional workstation/shared deployment, and watchlist |
| [Model license review](knowledge-base/models/license-review-2026-09-16.md) | Commercial use, affiliate boundaries and custom model-license conditions |
| [Report fixing plan](reports/phase1-llm-industry-2026-09-09/editorial/fixing-plan.md) | Independent Phase 1 report/PPT restructuring workstream |
| [Proof-of-concept plan](knowledge-base/models/poc-plan.md) | Phase 2 local GPU execution record template |
| [Reference architecture](knowledge-base/infrastructure/reference-architecture.md) | Phase 2 hardware/software/security specification template |
| [Serving frameworks](knowledge-base/infrastructure/serving-framework-survey-2026-09-17.md) | GPU, Apple and heterogeneous runtimes, model support and evaluation |
| [Harnesses](knowledge-base/infrastructure/harness-survey-2026-09-17.md) | Workflow platforms, general agents, licenses and local-model compatibility |
| [TCO model](knowledge-base/infrastructure/tco-model.md) | Phase 3 three-year on-premise/API comparison |
| [Pilot scorecard](knowledge-base/pilots/scorecard.md) | Phase 3 selection, ROI, and proposal template |
| [Week 1 record](weekly/week-01.md) | Historical setup and corrections |
| [Week 2 plan](weekly/week-02-plan.md) | Historical Phase 1 execution and delivery record |
| [Weeks 3–5 plan](weekly/week-03-05-plan.md) | Current execution plan, mentor feedback, and deployment scenarios |
| [Repository alignment review](weekly/repo-alignment-review-2026-09-06.md) | Whole-repository review against the final brief |
