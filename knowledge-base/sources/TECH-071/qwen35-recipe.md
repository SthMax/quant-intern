## Qwen/Qwen3.6-35B-A3B

Smaller Qwen3.6 multimodal MoE model (35B total / 3B active) with BF16, FP8, and NVIDIA NVFP4 variants

Compact Qwen3.6 MoE with 3B active parameters — single-GPU FP8 or 2-4 GPU or 4x Intel Arc Pro B60/B70 BF16 serving

[View on HuggingFace](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)

moe35B / 3B262,144 ctx [vLLM 0.17.0+](https://vllm.ai/#quick-start "Install vLLM") multimodaltext

Guide

## Overview

[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) is the smaller sibling of Qwen3.5, sharing the same gated-delta-networks MoE architecture but with 35B total parameters and 3B activated (256 experts, 8 routed + 1 shared). The recipe covers the BF16 base model, Qwen's official FP8 checkpoint, and NVIDIA's ModelOpt NVFP4 checkpoint.

## Prerequisites

- **vLLM version:** >= 0.17.0
- **NVFP4 vLLM version:** >= 0.28.0. 0.24.0 loads the checkpoint, but FlashInfer only selects its XQA decode kernel on SM120 GPUs from 0.28.0.
- **Hardware (BF16):** 1x H200, 2x H100, 4x Intel Arc Pro B60 / B70
- **Hardware (FP8):** single H100/H200 or 1x MI300X/MI325X/MI355X
- **Hardware (NVFP4):** NVIDIA Blackwell GPUs, including DGX Spark (GB10)

## NVFP4 on Blackwell

All NVFP4 tuning lives in `variants.nvfp4.hardware_overrides`, keyed by GPU profile, so the exact flag set for a box is readable straight from the recipe YAML (or from `by_hardware` in the JSON API) without going through the command builder.

Four profiles are tuned and verified. DGX Spark (GB10) and DGX Station (GB300) run the checkpoint on the default loader with FlashInfer attention, `--moe-backend marlin` and a 3-token MTP draft on Triton; Spark shares unified memory with the host, so `--gpu-memory-utilization` is capped at 0.5. The SM120 parts (RTX PRO 6000, RTX 5090) load through `--quantization modelopt_fp4` with FlashInfer's TRT-LLM attention kernels, which need `--block-size 128` and `VLLM_HAS_FLASHINFER_CUBIN=1`, and sustain a deeper 4-token MTP draft on `flashinfer_cutlass`. The RTX 5090's 32 GB caps context at 64K.

Datacenter Blackwell (B200/GB200/B300/GB300) intentionally carries no overrides — it runs vLLM's own NVFP4 defaults, which select the native FP4 path rather than the Marlin W4A16 kernel the workstation parts need.

### Measured on DGX Spark (GB10)

The GB10 profile above was re-measured on 2026-08-31 with aiperf 0.12.0 on vLLM 0.28.0 (Ubuntu 24.04.4, driver 580.159.03, CUDA 13.0), one GB10 at TP1, serving from `vllm/vllm-openai:v0.28.0`. On SPEED-Bench at 8K input / 256 output tokens and concurrency 1, it sustained 6,265 prefill tok/s and 97.7 decode tok/s at a 3.95 s mean end-to-end latency. The flag set is unchanged — the sweep confirms the tuning rather than revising it, so the command the builder emits for GB10 is the one that produced these numbers.

### Docker (Intel XPU B60 / B70)

Validated on 4× Intel Arc Pro B60 / B70 (B60 24 GB, B70 32 GB per card) with the official vLLM XPU image `vllm/vllm-openai-xpu:latest`.

```bash
docker run --device /dev/dri \
  -v /dev/dri/by-path:/dev/dri/by-path --shm-size=16g \
  --privileged --ipc=host -p 8000:8000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  vllm/vllm-openai-xpu:latest \
  Qwen/Qwen3.6-35B-A3B \
  --reasoning-parser qwen3 \
  --tensor-parallel-size 4 \
  --max-model-len 8192 \
  --enforce-eager
```

## Processing Ultra-Long Texts

Qwen3.6-35B-A3B natively supports `262,144` tokens. To serve longer inputs, turn on the **Long Context** feature above: it applies the model card's YaRN RoPE configuration via `--hf-overrides` and raises `--max-model-len` to ~1,010,000 tokens. Static YaRN holds the scaling factor constant regardless of input length, so leave it off unless you actually serve long prompts; for a ~524K workload, halve the card's `factor` to `2.0`.

See the [model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B#processing-ultra-long-texts) for the full parameter reference.

## Client Usage

```python
from openai import OpenAI

client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1")
resp = client.chat.completions.create(
    model="Qwen/Qwen3.6-35B-A3B",
    messages=[{"role": "user", "content": "Explain gated delta networks in one paragraph."}],
    max_tokens=512,
)
print(resp.choices[0].message.content)
```

## Troubleshooting

- **CUDA graph / Mamba cache size error:** reduce `--max-cudagraph-capture-size` (default 512). See [vLLM PR #34571](https://github.com/vllm-project/vllm/pull/34571).
- **Reasoning disable:** add `--default-chat-template-kwargs '{"enable_thinking": false}'`.
- **Prefix Caching (Mamba):** currently experimental in "align" mode.

## References

- [Qwen3.6-35B-A3B on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- [FP8 checkpoint](https://huggingface.co/Qwen/Qwen3.6-35B-A3B-FP8)
- [NVIDIA NVFP4 checkpoint](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4)
- [Qwen3.5 recipe (sibling 397B-A17B flagship)](../Qwen3.5-397B-A17B)