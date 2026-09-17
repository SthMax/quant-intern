Model: [deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
Recipe: [`models/deepseek-ai/DeepSeek-V4.1-Flash.yaml`](https://github.com/vllm-project/recipes/blob/main/models/deepseek-ai/DeepSeek-V4.1-Flash.yaml) — verified on H200, GB200, GB300, MI350X

All open work: [`is:open label:DSv4.1`](https://github.com/vllm-project/vllm/issues?q=is%3Aopen+label%3ADSv4.1)

> **Everything below stacks on #56214.** That PR adds `DeepseekV41ForCausalLM` to
> `registry.py`, so until it lands the model does not resolve from `main`. Please
> base new work on it rather than on `main`.

## Model support
zyongye
- #56214 — `DeepseekV41ForCausalLM` registry entry, config and tokenizer wiring **(keystone, in review)**
- #56228 — model definitions (merged)

## Kernels
gau-nernst JaredforReal ZJY0516 zyongye
- DeepGEMM Mega-Gate and Mega-mHC — gau-nernst
- Sparse indexer — JaredforReal, #56254
- [DeepSelect](https://github.com/deepseek-ai/DeepSelect) — ZJY0516
- [FlashMLA](https://github.com/deepseek-ai/FlashMLA) — zyongye
- #56344 — attention megakernel
- Kernel detail tracked in #56217

## Engram
- #56219 — redistribute SP embeddings with all-to-all
- #56220 — overlap lookup with decoder compute
- #56224 — microbatch positions and Engram histories
- #56357 — prefetch offloaded lookups, share host tables via mmap

## Pipeline parallelism
- #56221 — validate sharing dependencies before construction
- #56222 — sequence-parallel stage boundaries
- #56223 — relay cache and index state across stages

## Attention / SWA
ivanium
- #56227 — SWA-bounded replay

## Frontend and tool calling
abmfy CedricHwong
- #56235 — constrain tool parameters by schema in structural tag
- #56299 — support Responses text content types
- #56297 — bug: Responses API rejects text content types

## AMD / ROCm
JohnQinAMD hongxiayang
- #56342 — fused TileLang mHC kernels on the AMD path
- #56347 — bug: segfault on 3rd decode token with `FULL_DECODE_ONLY` unless `--no-async-scheduling`
- [vllm-project/recipes#952](https://github.com/vllm-project/recipes/pull/952) — working CUDA graph mode for AMD


## Triage notes
- V4.1 has its own `DSv4.1` label as of today. It previously landed on `DSv4`,
  because that rule's title pattern had no boundary after `v4`. Automation fix in
  #56332; `DSv4` will be cleared off the 4.1 PRs once that merges.
- `DeepseekV41ForCausalLM` is a distinct architecture from V4 — separate tree,
  tokenizer mode, parsers and config class. Please don't file 4.1 issues under
  `DSv4`.

