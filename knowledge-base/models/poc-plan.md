# Local GPU Proof-of-Concept Plan

> 2026-09-09新增[本地LLM任务与可复现证据](local-llm-poc-evidence-2026-09-09.md)：用于Phase 2选题，不表示已经部署或测量。用户强调先在本地运行LLM，再利用其能力完成实际任务。

**Phase 2 — Weeks 3–5.** Required by [the final project plan](../../PROJECT_PLAN.md).
Status: plan template; no workstation, deployment, or measurements recorded.

**16 September selection update:** choose among the four professional workstation
candidates in the [current survey](model-survey-2026-09-16.md): Qwen3.8-27B,
Qwen3.6-35B-A3B, Gemma 4 31B IT and Gemma 4 26B A4B IT. The earlier 4B/9B default
is withdrawn. A larger shared-model experiment remains possible if hardware
permits. Record hardware limitations separately from the target deployment
requirements; check the [license review](license-review-2026-09-16.md) for the
selected exact artifact.

## Confirmed minimum

Deploy **one open-source model on a local GPU workstation**, measure inference
latency, and run a sample financial NLP task. Keep enough configuration and
measurement detail for another researcher to repeat the experiment.

## Execution record

| Item | Value / evidence |
|---|---|
| Model and artifact version | |
| Model selection rationale / survey link | |
| License and source IDs | |
| Workstation GPU/VRAM, CPU, RAM, OS | |
| Driver, inference engine, dependency versions | |
| Precision / quantization | |
| Sample task and dataset / license | |
| Prompt, context/output length, decoding settings | |
| Warm-up, repetitions, concurrency, timing method | |
| Inference latency results and units | |
| Time to first token / throughput, if measured | |
| Peak memory / resource observations | |
| Sample outputs and scoring / error review | |
| Reproduction instructions and execution date | |
| Limitations and open questions | |

Select a sample from the financial NLP tasks in
[the evaluation plan](benchmark-plan.md). Published benchmark figures must be
labelled separately from local measurements.

## Completion checklist

- [ ] Model selection traced to the 5–8-model survey.
- [ ] One model deployed and served on the local GPU workstation.
- [ ] Latency measured under documented conditions.
- [ ] Sample financial NLP task completed with outputs and quality review.
- [ ] Reproduction instructions and limitations recorded.
- [ ] Findings linked to reference architecture and later TCO assumptions.

If the specified workstation is unavailable, record the dependency and continue
survey/evaluation design; do not represent a CPU or API experiment as completion
of the required GPU proof of concept.
