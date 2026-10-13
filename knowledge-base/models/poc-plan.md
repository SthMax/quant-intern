# Local GPU Proof-of-Concept Plan

> 2026-09-09新增[本地LLM任务与可复现证据](local-llm-poc-evidence-2026-09-09.md)：用于Phase 2选题，不表示已经部署或测量。用户强调先在本地运行LLM，再利用其能力完成实际任务。

**Phase 2 — Weeks 3–5.** Required by [the final project plan](../../PROJECT_PLAN.md).
Status (12 October 2026): external single-GB10 serving/performance summary received
from the user's friend. Financial NLP task results and the full reproduction
package remain open. The user has confirmed that a formal PoC is currently not
feasible; this week's work uses external performance evidence for the Thursday
deployment presentation, then feeds TCO and pilot analysis.

The [Week 7 matrices](../infrastructure/data/week7-deployment-2026-10-12/README.md)
cover 131K/262K/512K/1M, cold input, warm additions, resident sessions and active
requests. [Public DeepSeek logs](../sources/TECH-084/evidence-note.md) establish
cache-pool and replay conditions; full-1M task latency and answer quality remain
open. CPU recalculation and source inspection do not close the GPU PoC checklist.

## External measurement received on 12 October

[TECH-076](../sources/TECH-076/original.md) records Qwen3.8-27B-FP8 on one DGX Spark,
TP1, FP8 KV, MTP3 and FlashInfer. The supplied summary includes 1K–500K input
performance, 3/4/8-way load tests, 1,000,000 total-token capacity and an MTP draft
length-gate diagnosis. Stable single-request generation is approximately 20 tokens/s
at 50K/100K and 14.82 at 500K; the latter cold TTFT is 1,470.1 seconds.

These are actual-device measurements reported by the experiment provider. Exact
model/engine revision, commands and raw traces are referenced in files not yet
provided; no financial task or answer-quality evaluation is included. The primary
run date is unknown, and 2026-10-12 is the date received. See the
[analysis and structured data](../infrastructure/dgx-spark-qwen27-external-benchmark-2026-10-12.md).
The execution record below remains the place for the complete project PoC;
source-reported results do not fill unobserved fields.


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
