# Week 7 deployment calculations — 2026-10-12

This directory is authored analysis. Primary documents, current source snapshots and public API/log excerpts are archived under TECH-079–085; user-provided Spark measurements remain unchanged in TECH-076.

## Reproduce

```sh
python3 knowledge-base/infrastructure/data/week7-deployment-2026-10-12/calculate.py
```

The script uses only the Python standard library, reads local archived inputs, and writes into this directory. It performs no GPU execution or network access.

## Outputs

- `results.json`: fixed input SHA-256, architectural byte arithmetic, published replay examples, 70 enterprise capacity limits, 280 enterprise capacity rows, 24 Spark state/precision/context rows, fit coefficients and explicit unknowns.
- `capacity-matrix.csv`: enterprise actual context 131072/262144/524288/1000000 with 8192 output tokens reserved; active1/5/20/30/50; resident count equal to or twice active count; seven topologies including expansion sensitivity.
- `capacity-limits.csv`: inverse calculation, maximum context for resident sessions under the selected public token-pool profile.
- `spark-matrix.csv`: FP8/BF16 KV, one resident/active, three resident/one active, three resident/three active; 1M full-precision remains a separate capacity constraint.
- `spark-price.json`: current storefront observation and explicit CNY scenario formula. GPU server prices are maintained separately in `../hardware-prices-2026-10-12.json` by the integration owner.
- `validation.json`: arithmetic, source fingerprint, row and output-budget checks. These are analytical validation, not model correctness tests.

## Evidence and assumptions

Enterprise admission uses **the published engine token pool**, not aggregated GPU bytes divided by a paper's cache size. Each replica has an independent pool; a user is assigned to a replica. The next observed AgentX concurrency at or above target active users per replica supplies the startup profile. AgentX concurrency denotes sessions, so this is a profile-selection rule for allocation, not evidence that all sessions decode together.

A 10% reserve is applied once to the observed token pool. The static Hopper layout calculation (1790 raw / 1827 page-padded bytes per token per rank) is explanatory and is not added again to the observed pool. Source code is current at the frozen commit; public startup pools were collected on an earlier pinned image. Framework updates require re-profiling.

Some public logs allocate more KV than their own post-graph recommendation for `gpu_memory_utilization=0.92`. The three retrieved startup logs yield a **separate** strict-budget sensitivity in `post_graph_budget_sensitivity`. A 10% token-workset reserve within a preallocated pool does not free physical GPU memory. The new smaller pool is a linear rescaling scenario, not another measured startup.

`max_users_capacity_only` searches whole users against the selected pool, distinct from performance SLA. It preserves the operational-reserve choice. H100 cases above the observed concurrency range have null pool/capacity; they are not silently extrapolated. Replica expansion assumes independent Engram copies and sufficient host memory; shared host-table deduplication is not assumed.

All target full-window enterprise cold TTFT, warm p95 and decode rates stay null. Published AgentX rows separately preserve exact metrics, variable-length input distribution, synthetic DSpark acceptance and cache-hit rate. Output throughput and total-token throughput are distinct.

Spark cold-prefill fit uses provided engine durations (input divided by engine prefill throughput) at 50K,100K,300K,500K. Decode shape fits seconds/output-token at 100K,300K,500K. Warm estimates difference the cold cost curve, assuming exact prefix and linear-state reuse; they exclude queue, networking, first decode, checkpoints and changed warm-kernel efficiency. They are not TTFT measurements or p95. No FP8-KV speed is attributed to BF16 KV.

Spark BF16 capacity is a labeled half-FP8-token-pool proxy under unchanged non-token overhead. Prefix caching can change recurrent-state allocation, so the real loaded pool supersedes this proxy.

## Source packets

- TECH-079 official DeepSeek model revision, config, tensor index and reference code.
- TECH-080 vLLM Engram, Hopper cache formats, allocator interfaces and frozen official recipe.
- TECH-081 SGLang cookbook, source and AgentX fixed-image recipes.
- TECH-082 Qwen serving, hybrid-state prefix caching and chunked prefill.
- TECH-083 OpenCode/Pi custom endpoint, context and compaction documentation.
- TECH-084 InferenceX API (220 rows), three startup log excerpts and schema.
- TECH-085 NVIDIA Spark specifications and US storefront extracted-price observation.

Agent inspection complete for the cited passages; human review remains pending. No commit, release, model download or server connection was performed.
