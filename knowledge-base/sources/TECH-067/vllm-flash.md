## XiaomiMiMo/MiMo-V2.6-Flash-RL

Xiaomi's efficiency-balanced omnimodal MoE reasoning model (309B total / 15B active) with hybrid attention, FP8-compute/mxfp4-stored weights, 1M context, and a DFlash speculative decoder

[View on HuggingFace](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)

moe309B / 15B1,048,576 ctx [vLLM nightly+](https://vllm.ai/#quick-start "Install vLLM") text

Guide

## Overview

MiMo-V2.6-Flash-RL is the efficiency-balanced checkpoint of Xiaomi's MiMo-V2.6 series, trained with large-scale mixed RL (GRPO + groupwise agentic grading). It is a sparse MoE model with 309B total parameters and 15B active per token: 48 layers (1 dense + 47 MoE) with 256 routed experts (top-8), hybrid attention (sliding-window 128 and global attention), and a 5-layer DFlash-style MTP drafter that predicts 7 tokens per pass. The model is natively omnimodal (text, image, video, audio via a 681M-param MiMo ViT and audio encoders) and supports up to 1M tokens of context.

Weights are stored as mxfp4 and computed as FP8 (block-wise e4m3, 128x128), so the checkpoint is only 173 GB on disk. Loading this mixed storage format requires vLLM with the MiMo V2 mxfp4/bf16-router support ([vllm-project/vllm#57784](https://github.com/vllm-project/vllm/pull/57784)), which is newer than the latest stable release — use the pre-built image or a nightly wheel.

## Prerequisites

- Hardware: 4x H200 (TP4) or equivalent aggregate VRAM (>= 208 GB)

### Pull the vLLM docker image

Stable vLLM (<= 0.29.0) cannot load the mxfp4-stored weights. Use the pre-built image published for the MiMo-V2.6 series:

```bash
docker pull vllm/vllm-openai:mimo-v26
```

A vLLM nightly wheel built after 2026-09-20 also works (`uv pip install -U vllm --extra-index-url https://wheels.vllm.ai/nightly/cu130`).

## Launch command

Single-node TP4 (H200):

```bash
vllm serve XiaomiMiMo/MiMo-V2.6-Flash-RL \
  --tensor-parallel-size 4 \
  --trust-remote-code \
  --gpu-memory-utilization 0.95 \
  --max-model-len auto \
  --reasoning-parser mimo \
  --tool-call-parser mimo \
  --enable-auto-tool-choice \
  --generation-config vllm
```

With DFlash speculative decoding (drafter ships inside the checkpoint). vLLM does not resolve a `<repo>/dflash` Hub subfolder as the draft model — `model` must be a concrete local path to the `dflash/` directory inside the downloaded snapshot. Replace `<hash>` with the actual snapshot revision (run `hf download XiaomiMiMo/MiMo-V2.6-Flash-RL` first if the checkpoint is not cached yet):

```bash
# resolve the on-disk path of the dflash drafter
DFLASH_DIR=$(ls -d ~/.cache/huggingface/hub/models--XiaomiMiMo--MiMo-V2.6-Flash-RL/snapshots/*/dflash)
echo "$DFLASH_DIR"
```
```bash
vllm serve XiaomiMiMo/MiMo-V2.6-Flash-RL \
  --tensor-parallel-size 4 \
  --trust-remote-code \
  --gpu-memory-utilization 0.95 \
  --max-model-len auto \
  --speculative-config "{\"method\":\"dflash\",\"model\":\"$DFLASH_DIR\",\"num_speculative_tokens\":7}" \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --reasoning-parser mimo \
  --tool-call-parser mimo \
  --enable-auto-tool-choice \
  --generation-config vllm
```

The drafter inherits the target's tensor-parallel size by default. To pin it explicitly, add `"draft_tensor_parallel_size": 4` to the speculative config (useful if you want the draft on fewer GPUs than the target, or to silence mis-detection on asymmetric topologies).

## Client Usage

```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "XiaomiMiMo/MiMo-V2.6-Flash-RL",
    "messages": [{"role": "user", "content": "Hello MiMo!"}],
    "temperature": 1.0,
    "top_p": 0.95,
    "chat_template_kwargs": {"enable_thinking": true}
  }'
```

Recommended sampling: `temperature=1.0`, `top_p=0.95`. Set `"enable_thinking": false` (or omit the kwargs) to disable thinking mode.

## References

- [MiMo-V2.6-Flash-RL on Hugging Face](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
- [MiMo-V2.6 technical report](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL/blob/main/MiMo_V2_6_technical_report.pdf)
- [MiMo-V2.6 blog post](https://mimo.xiaomi.com/mimo-v2-6)
- [vLLM PR #57784 — mxfp4 MoE / bf16 router / DFlash for MiMo V2](https://github.com/vllm-project/vllm/pull/57784)
- [SGLang MiMo cookbook](https://docs.sglang.io/cookbook/autoregressive/Xiaomi/MiMo-V2.5)