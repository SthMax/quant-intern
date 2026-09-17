# Model Survey and Financial NLP Evaluation Plan

**Phase 2 — Weeks 3–5.** Derived from [the final project plan](../../PROJECT_PLAN.md).
Status (16 September 2026, revised): the user reprioritized eight current models
for professional workstations and shared services. See the [model survey](model-survey-2026-09-16.md) for archived
evidence, resource figures, runtime support and unresolved fields. No local
models have been deployed or tested. Final comparison acceptance remains open.

## Required outputs

- Survey and compare **5–8 open-source LLMs** on language proficiency, model size,
  inference speed, fine-tuning requirements, and community support.
- Maintain a reusable evaluation framework for financial named-entity recognition,
  financial question answering, and multi-document summarization.
- Select one model for the [local GPU proof of concept](poc-plan.md), which must
  measure inference latency and run a sample financial NLP task.
- Feed measured resource requirements into the
  [reference architecture](../infrastructure/reference-architecture.md) and
  Phase 3 [TCO comparison](../infrastructure/tco-model.md).

The 5–8-model requirement is a survey/comparison requirement. Record which models
were actually benchmarked locally. A one-model proof of concept does not imply
that all surveyed models were run on the same hardware.

## Model survey

Maintain findings in the [dated survey](model-survey-2026-09-16.md), with this
file governing the method and evaluation protocol. The current core pool is
Qwen3.8-27B, Qwen3.6-35B-A3B, Gemma 4 31B IT, Gemma 4 26B A4B IT,
DeepSeek-V4.1-Flash, GLM-5.3, GLM-5.3-Flash and Kimi K3. The previous 4B/9B,
Gemma 12B, Qwen3.5-35B and Mistral entries are historical research, not active
candidates. Quantization variants do not count as additional models.

Professional personal systems start at the 27B/35B and comparable Gemma class.
Research quality and service requirements first, then the resources and costs
needed to meet them. Keep large-model quality comparison separate from which
models can be deployed during this internship. Unreleased candidates are tracked
in the survey watchlist and do not count toward the eight-model survey.

Required fields: exact model/revision; official model/license sources; language
evidence; size/precision; speed and conditions; fine-tuning needs; dated
maintenance/runtime evidence; local test status; unresolved constraints.

For each row:

- Verify license and commercial-use terms using the [license review](license-review-2026-09-16.md), including affiliates, MaaS, internal-use exceptions and redistribution.
  Distinguish the brief's “open-source” wording from each actual license.
- Record languages assessed. Chinese and English are a proposed evaluation split
  for this desk; the brief does not specify languages or minimum proficiency.
- Record speed units, hardware, quantization, context/output length, concurrency,
  and whether a number is published or locally measured.
- Describe fine-tuning options and data/compute needs without assuming fine-tuning
  is necessary.
- Record dated support evidence such as release activity, maintained deployment
  integrations, documentation, and issue handling.
- Capture context limits, memory requirements, artifact versions, and sources
  where relevant to the architecture.

## Financial NLP evaluation

The [serving survey](../infrastructure/serving-framework-survey-2026-09-17.md)
and [harness survey](../infrastructure/harness-survey-2026-09-17.md) add a separate
comparison method: hold the model and task fixed when comparing engines or
harnesses, then evaluate the complete deployment combination. Run protocol/tool
loop checks before treating a custom model endpoint as an equivalent backend.

| Task | Evaluation unit | Proposed quality measures | Error analysis |
|---|---|---|---|
| Named-entity recognition | Sentence/document with labelled entities | Entity precision, recall, F1; exact and partial match | Entity type, company-name, number, and date errors |
| Financial question answering | Question with source context | Exact match/F1 where appropriate; rubric score; citation accuracy | Unsupported answers, calculation errors, appropriate abstention |
| Multi-document summarization | Filing/report/news packet | Coverage, faithfulness, citation precision/recall, human utility | Contradictions, omissions, temporal errors |

The measures above are an implementation proposal for the confirmed tasks.
Report sample size, annotation method, and limitations with each result.

## Reproducibility

- Freeze model artifact/version, dataset version, prompt, quantization, inference
  engine, decoding parameters, and hardware configuration.
- Separate development and held-out evaluation data; document contamination and
  time-split limitations.
- Verify dataset licensing and use public or synthetic data within project limits.
- Distinguish quality, latency, throughput, peak memory, and any energy measures.
- Retain test inputs or permitted references, raw outputs, scoring rules, and
  error analysis so the evaluation can be reused.
- Record refusals, unsupported answers, and prompt-injection behavior where
  relevant to the workflow.
- Use human review/adjudication for subjective quality labels and report whether
  that review has actually occurred.

## Week 3 research checkpoint

- [x] Archive official model cards, configs and repository revisions for the eight current candidates.
- [x] Record initial license evidence, language evidence and tensor sizes.
- [x] Inspect a fixed vLLM release and distinguish architecture registration
  from tested deployment combinations.
- [x] Read current core-model licenses; distinguish standard licenses from GLM-5.3/Kimi K3 conditions.
- [ ] Complete the deployment artifact/dependency license inventory and internal applicability questions.
- [ ] Confirm the PoC workstation and workload assumptions.
- [ ] Verify specific personal-runtime versions and quantized artifacts.
- [ ] Estimate runtime/cache memory and capacity for the shortlisted combinations.
- [ ] Complete fine-tuning/support gaps and comparable speed evidence, or record
  why evidence is unavailable.
- [ ] Prepare public financial development/test samples and scoring instructions.
- [ ] Freeze one primary PoC combination and one fallback, conditional on hardware.

Report restructuring follows its [own fixing plan](../../reports/phase1-llm-industry-2026-09-09/editorial/fixing-plan.md)
and does not gate these research tasks.

## Phase 2 completion record

- [ ] 5–8 model comparisons with all required dimensions and source IDs.
- [ ] Reusable financial NLP dataset/task/scoring specification.
- [ ] One-model GPU proof of concept with latency and task results.
- [ ] Measured results distinguished from published numbers and estimates.
- [ ] Resource and quality findings passed to architecture and Phase 3 analysis.
