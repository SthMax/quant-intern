serve - vLLM       Skip to content
vLLM
serve
Initializing search
GitHub
Home
User Guide
Developer Guide
Benchmarking
API Reference
CLI Reference
Community
vLLM
GitHub
Home
User Guide
User Guide       Getting Started       Getting Started      Quickstart
Installation
Installation      GPU
CPU
TPU
Examples
Examples       Applications       Applications      API Server
Chatbot
Rag
Basic       Basic      Offline Inference
Online Serving
Deployment       Deployment      Async LLM Streaming
Helm Charts
LLM Engine Example
Sagemaker-Entrypoint
Disaggregated       Disaggregated      Disaggregated Encoder
Disaggregated Serving
Ec Both Encoder
Disaggregated Prefill V1
Flexkv Connector
KV Load Failure Recovery Test
LMCache Examples
Mooncake Connector
Features       Features      Automatic Prefix Caching
Batch Invariance
Context Extension
Data Parallel
Kv Events
Logging Configuration
Custom Logits Processors
LoRA
Offline Inference with the OpenAI Batch file format
Pause Resume
Profiling
Prompt Embed
Reset Kv
Sharded State
Speculative Decoding
Structured Outputs
Tensorize vLLM Model
Torchrun
Generate       Generate      Batched Chat Completions Online
Multimodal
Qwen 1M Offline
Trace Replay Offline
Observability       Observability      Monitoring Dashboards
Metrics
Setup OpenTelemetry POC
Prometheus and Grafana
Pooling       Pooling      Classify
Embed
Plugin
Reward
Score
Token Classify
Token Embed
Ray Serving       Ray Serving      Batch LLM Inference
Elastic Ep
Multi-Node-Serving
Ray Serve Deepseek
Run Cluster
Reasoning       Reasoning      OpenAI Chat Completion Tool Calls With Reasoning
OpenAI Chat Completion With Reasoning
OpenAI Chat Completion With Reasoning Streaming
OpenAI Responses Client
RL       RL      Rdt vLLM Serve
Rdt Weight Source
RLHF Async New APIs
RLHF Http IPC
RLHF Http NCCL
RLHF IPC Fsdp Ep
RLHF NCCL Fsdp Ep
RLHF Sharded Rdt Small Ep
RLHF Sparse NCCL
Routed Experts E2E
Skip Loading Weights In Engine Init
Scale Out       Scale Out      Init
Example Mm Serve
Token Generation Client
Speech To Text       Speech To Text      OpenAI
Realtime
Tool Calling       Tool Calling      Chat With Tools Offline
OpenAI Chat Completion Client With Tools
OpenAI Chat Completion Client With Tools Required
OpenAI Chat Completion Client With Tools Xlam
OpenAI Chat Completion Client With Tools Xlam Streaming
OpenAI Responses Client With Mcp Tools
OpenAI Responses Client With Tools
General       General      vLLM V1
Frequently Asked Questions
Production Metrics
Reproducibility
Security
Troubleshooting
Usage Stats Collection
Inference and Serving       Inference and Serving      Offline Inference
Online Serving
Online Serving      Derenderer APIs
Generative Scoring
OpenAI-Compatible Server
Renderer APIs
Speech to Text APIs
Trace Replay
Context Parallel Deployment
Data Parallel Deployment
Troubleshooting distributed deployments
Expert Parallel Deployment
Parallelism and Scaling
Integrations       Integrations      Claude Code
Codex
LangChain
LlamaIndex
Deployment       Deployment      Using Docker
Using Kubernetes
Using Nginx
Frameworks       Frameworks      Anyscale
AnythingLLM
AutoGen
BentoML
Cerebrium
Chatbox
Crusoe
Dify
dstack
Haystack
Helm
Hugging Face Inference Endpoints
LiteLLM
Lobe Chat
LWS
Modal
Open WebUI
Retrieval-Augmented Generation
RunPod
SkyPilot
Streamlit
NVIDIA Triton
Integrations       Integrations      AIBrix
NVIDIA Dynamo
KAITO
KServe
Kthena
KubeAI
KubeRay
Llama Stack
llm-d
llmaz
Production stack
Training       Training      Async Reinforcement Learning
What is Layerwise (Re)loading?
Reinforcement Learning from Human Feedback
Sampling Mask (Distribution Replay)
Transformers Reinforcement Learning
Weight Transfer
Weight Transfer      Base Classes and Custom Engines
IPC Engine
NCCL Engine
Sharded RDT Engine
Configuration
Configuration      Conserving Memory
Engine Arguments
Environment Variables
Model Resolution
Optimization and Tuning
Server Arguments
TPU
Models       Models      Supported Models
Generative Models
Pooling Models
Pooling Models      Classification Usages
Embedding Usages
Reward Usages
Scoring Usages
Specific Model Examples
Token Classification Usages
Token Embedding Usages
Extensions       Extensions      Loading model weights with fastsafetensors
Loading Model Weights with InstantTensor
Loading models with Run:ai Model Streamer
Loading models with CoreWeave's Tensorizer
Hardware Supported Models       Hardware Supported Models      CPU - Intel® Xeon®
XPU - Intel® GPUs
TPU
Features
Features      Automatic Prefix Caching
Batch Invariance
Context Extension
Custom Arguments
Custom Logits Processors
Disaggregated Encoder
Disaggregated Prefilling (experimental)
IndexCache
Interleaved Thinking
KV Offloading Usage Guide
LoRA Adapters
MooncakeConnector Usage Guide
MooncakeStoreConnector Usage Guide
MoRIIOConnector Usage Guide
Multimodal Inputs
NixlConnector Compatibility Matrix
NixlConnector Usage Guide
Per-Request Metrics
Prompt Embedding Inputs
Reasoning Outputs
Sleep Mode
Structured Outputs
Tool Calling
Quantization
Quantization      AutoAWQ
b12x Linear and MoE Backends
BitsAndBytes
FP8 ViT Encoder Attention
GGUF
GPTQModel
Intel Quantization Support
NVIDIA Model Optimizer
Online Quantization
Quantized KV Cache
AMD Quark
TorchAO
LLM Compressor
LLM Compressor      FP8 W8A8
INT4 W4A16
INT8 W4A8
INT8 W8A8
Speculative Decoding
Speculative Decoding      Per-Request Acceptance Metrics
Adaptive Verification
Draft Models
Dynamic Speculative Decoding
EAGLE Draft Models
Hidden State Extraction
MLP Draft Models
MTP (Multi-Token Prediction)
N-Gram Speculation
Parallel Draft Models
vLLM-Project/Speculators
Suffix Decoding
Developer Guide
Developer Guide       General       General      Deprecation Policy
Dockerfile
Editing Agent Instructions
Incremental Compilation Workflow
JIT Kernel Warmup
Labels
Profiling vLLM
Vulnerability Management
Model Implementation
Model Implementation      Basic Model
Registering a Model
Unit Testing
Multi-Modal Support
Speech-to-Text (Transcription/Translation) Support
CI       CI      CI Failures
Nightly Builds of vLLM Wheels
Update PyTorch version on vLLM OSS CI/CD
Design Documents       Design Documents       Plugins       Plugins      Endpoint Plugins
IO Processor Plugins
LoRA Resolver Plugins
Plugin System
Architecture Overview
Attention Backend Feature Support
CUDA Graphs
Vision Encoder (ViT) CUDA Graphs
CustomOp
Dual Batch Overlap
How to debug the vLLM-torch.compile integration
Fused MoE Modular Kernel
Fusion torch.compile passes
Integration with Hugging Face
Hybrid KV Cache Manager
Logits Processors
Metrics
Multi-Modal Data Processing
Model Runner V2 Design Document
Fused MoE Kernel Features
Python Multiprocessing
NIXL KV Cache Lease Renewal
NIXL push-mode KV transfer
Optimization Levels
Paged Attention
Automatic Prefix Caching
torch.compile integration
torch.compile with Multimodal Encoders
vLLM IR: Functional Intermediate Representation
Benchmarking
Benchmarking      Benchmark CLI
Parameter Sweeps
Performance Dashboard
API Reference
API Reference        vllm
vllm      collect_env
connections
env_override
envs
exceptions
forward_context
logger
logits_process
logprobs
model_inspection
outputs
pooling_params
sampling_params
scalar_type
scripts
sequence
tasks
version
assets
assets      audio
base
image
video
benchmarks
benchmarks      latency
mm_processor
plot
serve
startup
throughput
datasets
datasets      create_txt_slices_dataset
datasets
utils
lib
lib      endpoint_request_func
ready_checker
utils
sweep
sweep      cli
param_sweep
plot
plot_pareto
serve
serve_workload
server
startup
utils
compilation
compilation      backends
base_static_graph
breakable_cudagraph
caching
codegen
compiler_interface
counter
cuda_graph
decorators
monitor
partition_rules
piecewise_backend
wrapper
passes
passes      fx_utils
inductor_pass
pass_manager
vllm_inductor_pass
fusion
fusion      act_quant_fusion
add_rms_fusion
allreduce_rms_fusion
attn_quant_fusion
collective_fusion
matcher_utils
mla_attn_quant_fusion
mla_rope_kvcache_cat_fusion
qk_norm_rope_fusion
qk_norm_rope_kvcache_fusion
rms_quant_fusion
rocm_aiter_fusion
rope_kvcache_fusion
sequence_parallelism
ir
ir      clone_elimination
inplace_functionalization
lowering_pass
utils
utility
utility      fix_functionalization
noop_elimination
post_cleanup
scatter_split_replace
split_coalescing
config
config      attention
cache
compilation
device
diffusion
ec_manager_config
ec_transfer
fault_tolerance
kernel
kv_events
kv_transfer
load
lora
mamba
model
model_arch
multimodal
observability
offload
parallel
pooler
profiler
quantization
reasoning
scheduler
speculative
speech_to_text
structured_outputs
utils
vllm
weight_transfer
cute_utils
cute_utils      cvt
mbarrier
device_allocator
device_allocator      cumem
sleep_mode_backend
xpumem
distributed
distributed      communication_op
kv_events
nixl_utils
parallel_state
stateless_coordinator
utils
device_communicators
device_communicators      aiter_custom_all_reduce
all2all
all_reduce_utils
base_device_communicator
cpu_communicator
cuda_communicator
cuda_wrapper
custom_all_reduce
flashinfer_all_reduce
mnnvl_compat
pynccl
pynccl_allocator
pynccl_wrapper
quick_all_reduce
ray_communicator
shm_broadcast
shm_object_storage
symm_mem
xpu_communicator
ec_transfer
ec_transfer      ec_transfer_state
ec_connector
ec_connector      base
example_connector
factory
utils
cpu
cpu      common
connector
ec_shared_region
scheduler
scheduler      embedding_cache
worker
worker      descriptor_buffers
elastic_ep
elastic_ep      elastic_execute
elastic_state
standby_state
eplb
eplb      async_worker
eplb_communicator
eplb_state
eplb_utils
rebalance_execute
policy
policy      abstract
default
kv_transfer
kv_transfer      kv_transfer_state
kv_connector
kv_connector      base
factory
utils
v1
v1      base
decode_bench_connector
example_connector
example_hidden_states_connector
flexkv_connector
lmcache_connector
lmcache_mp_connector
metrics
multi_connector
offloading_connector
simple_cpu_offload_connector
ssm_conv_transfer_utils
hf3fs
hf3fs      hf3fs_client
hf3fs_connector
hf3fs_metadata_server
utils
utils      common
gather_scatter_helper
hf3fs_mock_client
lmcache_integration
lmcache_integration      multi_process_adapter
utils
vllm_v1_adapter
mooncake
mooncake      mooncake_connector
mooncake_utils
rdma_utils
stats
store
store      connector
coordinator
data
metrics
protocol
scheduler
worker
moriio
moriio      moriio_common
moriio_connector
moriio_engine
moriio_layout
nixl
nixl      base_scheduler
base_worker
connector
metadata
pull_scheduler
pull_worker
push_scheduler
push_worker
scheduler
stats
tp_mapping
utils
worker
offloading
offloading      canonical_mapping
common
config
events
metrics
scheduler
worker
weight_transfer
weight_transfer      base
clients
factory
ipc_engine
nccl_common
nccl_engine
packed_tensor
sharded_rdt_common
sharded_rdt_engine
sharded_rdt_fake
sharded_rdt_trainer
sparse_nccl_engine
engine
engine      arg_utils
async_llm_engine
llm_engine
protocol
entrypoints
entrypoints      chat_utils
grpc_server
llm
offline_utils
anthropic
anthropic      api_router
protocol
serving
cli
cli      collect_env
launch
main
openai
run_batch
serve
types
benchmark
benchmark      base
latency
main
mm_processor
serve
startup
sweep
throughput
cohere
cohere      api_router
cohere_chat_message
protocol
serving
generate
generate      api_router
factories
base
base      protocol
serving
beam_search
beam_search      offline
online
utils
generative_scoring
generative_scoring      api_router
serving
launchers
launchers      app
cli_args
dp_supervisor
launcher
run_batch
api_server
api_server      app_state
entry
routers
render
render      app_state
entry
utils
utils      constants
server_utils
ssl
mcp
mcp      tool
tool_server
openai
openai      api_server
run_batch
sse_keep_alive
chat_completion
chat_completion      api_router
batch_serving
protocol
serving
completion
completion      api_router
protocol
serving
models
models      api_router
protocol
serving
parser
parser      harmony_utils
responses
responses      api_router
context
harmony
protocol
serving
streaming_events
utils
pooling
pooling      factories
offline
typing
utils
base
base      io_processor
protocol
serving
classify
classify      api_router
io_processor
protocol
serving
embed
embed      api_router
io_processor
protocol
serving
pooling
pooling      api_router
io_processor
protocol
serving
scoring
scoring      api_router
io_processor
protocol
serving
typing
utils
scale_out
scale_out      factories
derender
derender      api_router
serving
render
render      api_router
serving
token_in_token_out
token_in_token_out      api_router
mm_serde
protocol
serving
serve
serve        dev
dev        cache
cache      api_router
rlhf
rlhf      api_router
rpc
rpc      api_router
server_info
server_info      api_router
sleep
sleep      api_router
elastic_ep
elastic_ep      api_router
middleware
engine
engine      protocol
serving
typing
exception_handling
exception_handling      error_response
register
utils
handlers
handlers      exception
http
validation
vllm_error
fault_tolerance
fault_tolerance      api_router
instrumentator
instrumentator      basic
health
metrics
offline_docs
lora
lora      api_router
protocol
middleware
middleware      authenticate
log_response
register
x_request_id
profile
profile      api_router
sagemaker
sagemaker      api_router
tokenize
tokenize      api_router
protocol
serving
utils
utils      api_utils
fingerprint
orca_metrics
request_logger
tool_calls_utils
speech_to_text
speech_to_text      factories
base
base      protocol
serving
utils
realtime
realtime      api_router
connection
metrics
protocol
serving
transcription
transcription      api_router
protocol
serving
translation
translation      api_router
protocol
serving
inputs
inputs      engine
llm
ir
ir      op
tolerances
util
ops
ops      layernorm
kernels
kernels      aiter_ops
oink_ops
vllm_c
helion
helion      case_key
config_manager
register
utils
ops
ops      dynamic_per_token_scaled_fp8_quant
fused_qk_norm_rope
per_token_group_fp8_quant
rms_norm_dynamic_per_token_quant
rms_norm_per_block_quant
silu_and_mul_per_block_quant
silu_mul_fp8
triton
triton      qkv_padded_fp8_quant
logging_utils
logging_utils      access_log_filter
dump_input
formatter
lazy
log_time
torch_tensor
lora
lora      lora_model
lora_weights
model_manager
peft_helper
request
resolver
utils
worker_manager
layers
layers      base
base_linear
column_parallel_linear
fused_moe
logits_processor
replicated_linear
row_parallel_linear
utils
vocab_parallel_embedding
ops
ops        torch_ops
torch_ops      lora_ops
triton_ops
triton_ops      fp8_kernel_utils
fused_moe_lora_fp8_op
fused_moe_lora_op
kernel_utils
lora_expand_fp8_op
lora_expand_op
lora_kernel_metadata
lora_shrink_fp8_op
lora_shrink_op
utils
xpu_ops
xpu_ops      lora_ops
punica_wrapper
punica_wrapper      punica_base
punica_cpu
punica_gpu
punica_selector
punica_xpu
utils
model_executor
model_executor      custom_op
parameter
utils
determinism
determinism      batch_invariant
batch_invariant_configs
hw_agnostic
hw_agnostic      custom_op
layers
layers      activation
layernorm
kernels
kernels        attention
attention        dsa
dsa      dcp_indexer_cutedsl
linear
linear      base
zentorch_utils
cute_dsl
cute_dsl      ll_bf16
skinny_gemm
mixed_precision
mixed_precision      allspark
conch
cpu
cutlass
dynamic_4bit
exllama
humming
MPLinearKernel
machete
marlin
rdna3_w4a16
rdna_hybrid_w4a16
triton_w4a16
xpu
zentorch
mxfp4
mxfp4      aiter
b12x
base
emulation
flashinfer
humming
marlin
xpu
mxfp6
mxfp6      base
emulation
mxfp8
mxfp8      b12x
emulation
flashinfer
humming
Mxfp8LinearKernel
marlin
rocm_native
xpu
nvfp4
nvfp4      b12x
base
cutlass
emulation
fbgemm
flashinfer
humming
marlin
scaled_mm
scaled_mm      aiter
BlockScaledMMLinearKernel
b12x
cpu
cutlass
deep_gemm
flashinfer
humming
marlin
pytorch
rocm
ScaledMMLinearKernel
triton
xpu
zentorch
mhc
mhc      aiter
tilelang
tilelang_kernels
torch
triton
layers
layers      activation
attention_layer_base
conv
fused_allreduce_gemma_rms_norm
fused_embed_norm
fused_qk_norm_rope
layernorm
lightning_attn
linear
logits_processor
mhc
mla
resampler
sparse_attn_indexer
utils
vocab_parallel_embedding
attention
attention      attention
chunked_local_attention
cross_attention
encoder_only_attention
kv_transfer_utils
mla_attention
mm_encoder_attention
prefill_prefix_lm_attention
rswa_attention
sparse_mla_attention
sparse_mla_mask
static_sink_attention
fused_moe
fused_moe      activation
all2all_utils
b12x
config
deep_gemm_utils
eep_reconfigure
expert_map_manager
fused_flydsl_moe
fused_moe
fused_moe_method_base
fused_moe_modular_method
hpc_moe
layer
modular_kernel
moe_align_block_size
moe_fused_mul_sum
moe_output
moe_permute_unpermute
routed_experts
routed_experts_capturer
topk_weight_and_reduce
unquantized_fused_moe_method
utils
experts
experts      aiter_mxfp4_w4a8_moe
aiter_mxfp8_moe
batched_deep_gemm_moe
cpu_int4_moe
cpu_moe
cutlass_moe
deep_gemm_moe
fallback
flashinfer_b12x_moe
flashinfer_cutedsl_batched_moe
flashinfer_cutedsl_moe
flashinfer_cutlass_moe
fused_batched_moe
fused_humming_moe
gpt_oss_triton_kernels_moe
int4_emulation_moe
lora_context
lora_experts_mixin
marlin_moe
mxfp8_emulation_moe
mxfp8_native_moe
nvfp4_emulation_moe
ocp_mx_emulation_moe
rocm_aiter_moe
triton_cutlass_moe
triton_deep_gemm_moe
triton_moe
trtllm_bf16_moe
trtllm_fp8_moe
trtllm_lora_moe
trtllm_mxfp4_moe
trtllm_mxint4_moe
trtllm_nvfp4_moe
xpu_moe
oracle
oracle      base
fp8
int8
int_wna16
mxfp4
mxfp8
nvfp4
unquantized
w4a8
w4a8_int8
prepare_finalize
prepare_finalize      batched
deepep_ht
deepep_ll
deepep_v2
flashinfer_nvlink_one_sided
flashinfer_nvlink_two_sided
mori
naive_dp_ep
nixl_ep
no_dp_ep
router
router      aiter_shared_routed_fused_moe_router
base_router
bf16x3_router_gemm_cutedsl
custom_routing_router
dsv4_topk
fused_moe_router
fused_topk_bias_router
fused_topk_router
gate_linear
grouped_topk_router
router_factory
routing_simulator_router
zero_expert_router
runner
runner      moe_runner
moe_runner_interface
shared_experts
fusion
fusion      quant_activation
hpc
hpc      gated_mla
hpc_ihc
hpc_module
rope_norm
mamba
mamba      abstract
mamba_mixer
mamba_mixer2
mamba_utils
short_conv
gdn
gdn      base
kimi_gdn_linear_attn
olmo_gdn_linear_attn
qwen_gdn_linear_attn
linear
linear      bailing_linear_attn
base
minimax_linear_attn
ops
ops      causal_conv1d
gather_initial_states
layernorm_gated
mamba_ssm
replayssm_config
selective_state_update_replayssm_output_only
ssd_bmm
ssd_chunk_scan
ssd_chunk_state
ssd_combined
ssd_state_passing
ssu_dispatch
triton_helpers
cpu
cpu      causal_conv1d
gdn_attention
mamba_ssm
gdn_chunk_cutedsl
gdn_chunk_cutedsl      kernel_h
kernel_kkt_inv_uw
kernel_o
minimax_rms_norm
minimax_rms_norm      lamport_workspace
rms_norm_tp
pooler
pooler      abstract
activations
common
special
seqwise
seqwise      heads
methods
poolers
tokwise
tokwise      heads
methods
poolers
quantization
quantization      auto_awq
auto_gptq
awq_triton
base_config
experts_int8
fbgemm_fp8
fp8
fp_quant
humming
input_quant_fp8
kv_cache
modelopt
moe_wna16
mxfp4
qutlass_utils
torchao
compressed_tensors
compressed_tensors      compressed_tensors
compressed_tensors_embedding
triton_scaled_mm
utils
compressed_tensors_moe
compressed_tensors_moe      compressed_tensors_moe
compressed_tensors_moe_w4a4_mxfp4
compressed_tensors_moe_w4a4_nvfp4
compressed_tensors_moe_w4a8_fp8
compressed_tensors_moe_w4a8_int8
compressed_tensors_moe_w4a16_flydsl
compressed_tensors_moe_w8a8_fp8
compressed_tensors_moe_w8a8_int8
compressed_tensors_moe_w8a8_mxfp8
compressed_tensors_moe_wna16
compressed_tensors_moe_wna16_rdna3
rocm_moe_rdna
schemes
schemes      compressed_tensors_scheme
compressed_tensors_w4a4_mxfp4
compressed_tensors_w4a4_nvfp4
compressed_tensors_w4a8_fp8
compressed_tensors_w4a8_int
compressed_tensors_w8a8_fp8
compressed_tensors_w8a8_int8
compressed_tensors_w8a8_mxfp8
compressed_tensors_w8a16_fp8
compressed_tensors_wNa4
compressed_tensors_wNa8
compressed_tensors_wNa8o8
compressed_tensors_wNa16
transform
transform      linear
module
utils
schemes
schemes      linear_qutlass_nvfp4
inc
inc      config_parser
inc
inc_linear
schemes
schemes      factory
inc_ark_ops
inc_fp8_linear
inc_fp8_scheme
inc_mxfp4_linear
inc_mxfp4_moe
inc_mxfp4_scheme
inc_mxfp8_linear
inc_mxfp8_moe
inc_mxfp8_scheme
inc_scheme
inc_w4a8_linear
inc_wna16_linear
inc_wna16_scheme
online
online      base
fp8
int8
moe_base
mxfp4
mxfp8
nvfp4
quark
quark      quark
quark_moe
utils
schemes
schemes      quark_nvfp4
quark_ocp_mx
quark_scheme
quark_w4a8_mxfp4_fp8
quark_w8a8_fp8
quark_w8a8_int8
turboquant
turboquant      centroids
config
utils
utils      allspark_utils
b12x_moe
config_utils
flashinfer_fp4_moe
flashinfer_mxint4_moe
flashinfer_utils
fp8_utils
gptq_utils
humming_utils
int8_utils
layer_utils
machete_utils
marlin_utils
marlin_utils_fp4
marlin_utils_fp8
marlin_utils_test
mxfp4_utils
mxfp6_utils
mxfp8_utils
nvfp4_emulation_utils
nvfp4_utils
ocp_mx_utils
quant_utils
w8a8_utils
rotary_embedding
rotary_embedding      base
common
deepseek_scaling_rope
dual_chunk_rope
dynamic_ntk_alpha_rope
dynamic_ntk_scaling_rope
ernie45_vl_rope
fope
gemma4_rope
linear_scaling_rope
llama3_rope
llama4_vision_rope
mrope
mrope_interleaved
ntk_scaling_rope
phi3_long_rope_scaled_rope
telechat3_scaling_rope
xdrope
yarn_scaling_rope
model_loader
model_loader      base_loader
checkpoint_weight_patch
default_loader
dummy_loader
ep_weight_filter
modelexpress_loader
mtp_validation
runai_streamer_loader
sharded_state_loader
tensorizer
tensorizer_loader
utils
weight_tying
weight_utils
reload
reload      layerwise
meta
sanitize
torchao_decorator
types
utils
models
models      AXK1
adapters
afmoe
aimv2
apertus
arcee
aria
audioflamingo3
bagel
bailing_moe
bailing_moe_linear
bailing_moe_mtp
bailing_moe_v3
bailing_moe_v3_mtp
bee
bert
bert_with_rope
blip
blip2
bloom
chatglm
clip
cohere2_moe
cohere2_vision
cohere_asr
cohere_eagle
colbert
colmodernvbert
colpali
colqwen3
colqwen3_5
commandr
config
conformer_encoder
cosmos3
cosmos3_edge
dbrx
deepencoder
deepencoder2
deepseek_eagle
deepseek_eagle3
deepseek_mtp
deepseek_ocr
deepseek_ocr2
deepseek_v2
deepseek_vl2
diffusion_gemma
dots_ocr
eagle2_5_vl
ernie45
ernie45_moe
ernie45_vl
ernie45_vl_moe
ernie_mtp
exaone
exaone4
exaone4_5
exaone4_5_mtp
exaone_moe
exaone_moe_mtp
extract_hidden_states
falcon
falcon_h1
fireredasr2
funasr
funaudiochat
gemma
gemma2
gemma3
gemma3_mm
gemma3n
gemma3n_audio_utils
gemma3n_mm
gemma4
gemma4_dspark
gemma4_mm
gemma4_mtp
gemma4_unified
glm
glm4
glm4_1v
glm4_moe
glm4_moe_lite
glm4_moe_lite_mtp
glm4_moe_mtp
glm4v
glm_ocr
glm_ocr_mtp
glmasr
glmasr_utils
gpt2
gpt_j
gpt_neox
gpt_oss
granite
granite4_vision
granite_speech
granite_speech_plus
granitemoe
granitemoehybrid
granitemoeshared
h2ovl
hrm_text
hy_v3
hy_v3_mtp
hyperclovax
hyperclovax_vision_v2
idefics2_vision_model
idefics3
interfaces
interfaces_base
intern_vit
internlm2
interns1
interns1_pro
interns1_vit
interns2_mobius
interns2_preview
internvl
iquest_loopcoder
isaac
jais2
jamba
jina
jina_vl
kanana_v
keye
keye_vl1_5
kimi_audio
kimi_k25
kimi_k25_vit
kimi_vl
laguna
laguna_dflash
lfm2
lfm2_moe
lfm2_siglip2
lfm2_vl
lightonocr
llama
llama4
llama4_eagle
llama_eagle
llama_eagle3
llava
llava_next
llava_next_video
llava_onevision
llava_onevision2
longcat_flash
longcat_flash_mtp
longcat_flash_ngram
mamba
mamba2
medusa
mellum
midashenglm
mimo
mimo_audio
mimo_mtp
mimo_v2
mimo_v2_mtp
mimo_v2_omni
minicpm
minicpm3
minicpm_eagle
minicpmo
minicpmv
minicpmv4_6
minimax_m2
mistral
mistral3
mistral_eagle
mistral_large_3
mistral_large_3_eagle
mixtral
mllama4
mlp_speculator
modernbert
module_mapping
molmo
molmo2
moondream3
moonvit
moss_audio
moss_transcribe_diarize
muse_glimmer
nano_nemotron_vl
nemotron
nemotron_h
nemotron_h_mtp
nemotron_nas
nemotron_parse
nemotron_vl
nvlm_d
olmo_hybrid
olmoe
openai_privacy_filter
opencua
openpangu
openpangu_mtp
openpangu_vl
openvla
opt
orion
ovis
ovis2_5
paddleocr_vl
paligemma
parakeet
param2moe
phi
phi3
phi3v
phi4mm
phi4mm_audio
phi4mm_utils
phi4siglip
phimoe
pixtral
plamo3
qianfan_ocr
qwen2
qwen2_5_omni_thinker
qwen2_5_vl
qwen2_audio
qwen2_moe
qwen2_rm
qwen2_vl
qwen3
qwen3_5
qwen3_5_mtp
qwen3_asr
qwen3_asr_forced_aligner
qwen3_asr_realtime
qwen3_dflash
qwen3_dflash2
qwen3_dspark
qwen3_eagle3
qwen3_moe
qwen3_next
qwen3_next_mtp
qwen3_omni_moe_thinker
qwen3_vl
qwen3_vl_moe
radio
registry
rnj1
roberta
rvl
sarvam
seed_oss
siglip
siglip2navit
skyworkr1v
smolvlm
solar
stablelm
step1
step3_text
step3_vl
step3p5
step3p5_mtp
step3p7
step_vl
telechat2
teleflm
terratorch
ultravox
unlimited_ocr
utils
vision
voxtral
voxtral_realtime
voyage
whisper
whisper_causal
whisper_utils
zamba2
transformers
transformers      base
causal
fuser
fx_utils
layers
legacy
moe
multimodal
pooling
utils
fusers
fusers      base
glu
mla
moe
packed_qkv
qkv
rms_norm
offloader
offloader      base
prefetch
prefetch_ops
uva
warmup
warmup      b12x_warmup
cutedsl_warmup
deep_gemm_warmup
deepseek_v4_mhc_warmup
fa4_cutedsl_warmup
flashinfer_autotune_cache
flashinfer_sparse_mla_warmup
jit_warmup
jit_warmup_triton_helper
kernel_warmup
kimi_k3_triton_warmup
minimax_m3_msa_warmup
qwen_triton_warmup
sparse_mla_triton_warmup
models
models        common
common        ops
ops      fused_allreduce_rms_norm
fused_qk_rmsnorm
sequence_parallel
deepseek_v4
deepseek_v4      attention
compressor
quant_config
sparse_mla
amd
amd      dspark
model
mtp
rocm
common
common      rope
ops
ops      cache_utils
fused_compress_quant_cache
fused_indexer_q
fused_inv_rope_fp8_quant
fused_mtp_input_rmsnorm
save_partial_states
nvidia
nvidia      dspark
fi_moe
flashinfer_sparse
flashmla
model
mtp
ops
ops      dequant_gather_k_cutedsl
fused_indexer_q_cutedsl
o_proj
prepare_megamoe
sparse_attn_compress_cutedsl
xpu
xpu      dspark
model
mtp
xpu_qnorm_rope_kv_fp8_insert
xpu_sparse
xpu_sparse_decode_fp8
deepseek_v32
deepseek_v32      attention
amd
amd      model
mtp
rocm
common
common      kernels
nvidia
nvidia      glm52_low_latency_gemm
model
mtp
ops
ops      fused_q_cutedsl
dots3_note
dots3_note        common
common      processor
video
nvidia
nvidia      attention
audio
audio_encoder
model
mtp
multimodal
vision
vision_attention
vision_moe
hy_v4
hy_v4        nvidia
nvidia      attention
flashmla_sparse
hc
model
moe
mtp
inkling
inkling      configs
amd
amd      attention
layernorm
logits_processor
mlp
model
moe
mtp
sconv_swa_attn
short_conv
ops
ops      fa4_rel_attention
fa4_warmup
lamport
mm_towers
norm
qkvr_prep
rel_attention_decode
sconv
silu_and_mul
gluon
gluon      rel_mha_decode_gfx950
rel_mha_extend_gfx950
utils
common
common      mm_preprocess
towers
nvidia
nvidia      attention
layernorm
logits_processor
mlp
model
moe
mtp
sconv_swa_attn
short_conv
ops
ops      fa4_rel_attention
lamport
mm_towers
norm
qkvr_prep
sconv
silu_and_mul
kimi_k3
kimi_k3        amd
amd      kda
kda_metadata
latent_moe_runner
linear
model
mtp
ops
ops      attn_res
kda_decode
third_party
third_party        kda
kda      chunk
chunk_intra
chunk_intra_token_parallel
fused_recurrent
common
common      mm_preprocess
mtp
nvidia
nvidia      dspark_mla
kda
kda_metadata
latent_moe_runner
low_latency_gemm
mla
model
mtp
ops
ops      attn_res
fused_mla_key_concat_kv_cache
latent_moe_tail
recoverssm
vision_fa4_warmup
cute_dsl
cute_dsl      gemm_rs_ar
latent_moe_tail
latent_moe_tail      allreduce_rmsnorm_reduce_scatter_early_exit
fused_add_multicast_gemm
fused_add_multicast_skinny_gemm
lamport_copy
primitives
third_party
third_party        kda
kda      chunk
chunk_intra
chunk_intra_token_parallel
fused_recurrent
minimax_m3
minimax_m3        amd
amd      model
mtp
sparse_attention_msa
ops
ops      gemma_rmsnorm
index_topk
sparse_attn
sparse_pa
swiglu_oai
common
common      indexer
mm_preprocess
sparse_attention
vision_tower
ops
ops      index_topk
sparse_attn
nvidia
nvidia      indexer_msa
model
msa_cutlass_sparse_decode
mtp
sparse_attention_msa
ops
ops      index_decode_score
qwen4_exp
qwen4_exp      config
amd
amd      hyperconnection
indexer_qsa
low_latency_gemm
model
model_state
mtp
ple_layer
qsa
ops
ops      hc
qsa
common
common      hyperconnection
ple
qsa_cache
nvidia
nvidia      hyperconnection
indexer_qsa
low_latency_gemm
model
model_state
mtp
ple_layer
qsa
ops
ops      hc
qsa
qsa_pre_indexer
multimodal
multimodal      audio
cache
encoder_budget
gpu_ipc_memory
hasher
image
inputs
parse
registry
utils
video
media
media      audio
base
connector
image
video
processing
processing      context
dummy_inputs
inputs
processor
video_decoders
video_decoders      base
deepstream
opencv
pynvvideocodec
torchcodec
video_prune
video_prune      evs
vidcom2
parser
parser      abstract_parser
deepseek_v4
deepseek_v32
gemma4
glm47_moe
harmony
inkling
kimi_k2
kimi_k3
ling3
metrics
minimax_m2
mistral
nemotron_v3
parser_manager
qwen3
seed_oss
utils
engine
engine      adapters
events
incremental_lexer
parser_engine
parser_engine_config
registered_adapters
streaming_parser_engine
token_id_scanner
platforms
platforms      cpu
cuda
interface
rocm
tpu
xpu
zen_cpu
plugins
plugins        endpoint_plugins
endpoint_plugins      interface
io_processors
io_processors      interface
lora_resolvers
lora_resolvers      filesystem_resolver
hf_hub_resolver
profiler
profiler      layerwise_profile
utils
wrapper
ray
ray      lazy_utils
ray_env
reasoning
reasoning      abs_reasoning_parsers
basic_parsers
cohere_command_reasoning_parser
deepseek_r1_reasoning_parser
deepseek_v3_reasoning_parser
deepseek_v4_engine_reasoning_parser
ernie45_reasoning_parser
gemma4_engine_reasoning_parser
gemma4_utils
glm47_moe_reasoning_parser
gptoss_reasoning_parser
granite_reasoning_parser
hunyuan_a13b_reasoning_parser
hy_v3_reasoning_parser
hy_v4_reasoning_parser
identity_reasoning_parser
inkling_reasoning_parser
kimi_k2_reasoning_parser
kimi_k3_reasoning_parser
ling3_reasoning_parser
minimax_m2_reasoning_parser
minimax_m3_reasoning_parser
mistral_reasoning_parser
muse_glimmer_reasoning_parser
nemotron_v3_engine_reasoning_parser
olmo3_reasoning_parser
poolside_v1_reasoning_parser
qwen3_engine_reasoning_parser
seed_oss_engine_reasoning_parser
step3_reasoning_parser
step3p5_reasoning_parser
renderers
renderers      base
cohere
deepseek_v4
deepseek_v32
embed_utils
hf
inkling
inkling_encoding
kimi_k3
mistral
online_derenderer
online_renderer
params
registry
terratorch
inputs
inputs      preprocess
tokenize
tilelang_utils
tilelang_utils
tokenizers
tokenizers      deepseek_v4
deepseek_v4_encoding
deepseek_v32
deepseek_v32_encoding
detokenizer_utils
fastokens
hf
kimi_audio
mistral
protocol
registry
tool_parsers
tool_parsers      abstract_tool_parser
apertus_tool_parser
cohere_command_tool_parser
deepseekv3_tool_parser
deepseekv4_engine_tool_parser
deepseekv31_tool_parser
deepseekv32_engine_tool_parser
dots_tool_parser
ernie45_tool_parser
functiongemma_tool_parser
gemma4_engine_tool_parser
gemma4_utils
gigachat3_tool_parser
glm47_moe_tool_parser
gptoss_tool_parser
granite4_tool_parser
granite_20b_fc_tool_parser
granite_tool_parser
hermes_tool_parser
hunyuan_a13b_tool_parser
hy_v3_tool_parser
hy_v4_tool_parser
inkling_tool_parser
internlm2_tool_parser
jamba_tool_parser
kimi_k2_tool_parser
kimi_k3_tool_parser
lfm2_tool_parser
ling3_tool_parser
llama4_pythonic_tool_parser
llama_tool_parser
longcat_tool_parser
minicpm5xml_tool_parser
minimax_m2_tool_parser
minimax_m3_tool_parser
mistral_tool_parser
muse_glimmer_tool_parser
olmo3_tool_parser
phi4mini_tool_parser
poolside_v1_tool_parser
pythonic_tool_parser
qwen3_engine_tool_parser
rust_tool_parser
seed_oss_engine_tool_parser
step3_tool_parser
step3p5_tool_parser
streaming
structural_tag_registry
utils
xlam_tool_parser
tracing
tracing      otel
utils
transformers_utils
transformers_utils      config
config_parser_base
dynamic_module
model_arch_config_convertor
processor
repo_utils
runai_utils
s3_utils
utils
chat_templates
chat_templates      registry
triton_utils
triton_utils      allocation
force_first_config
importing
tensor_descriptor
usage
usage      usage_lib
utils
utils      argparse_utils
async_utils
b12x
cache
collection_utils
counter
cpu_resource_utils
cpu_triton_utils
deep_gemm
flashinfer
flashinfer_moe_ep
func_utils
gc_utils
gpu_sync_debug
hashing
hpc
humming
import_utils
jit_monitor
jsontree
math_utils
mem_constants
mem_utils
mistral
multi_stream_utils
nccl
network_utils
numa_utils
nvtx_pytorch_hooks
ompmultiprocessing
platform_utils
print_utils
registry
serial_utils
sparse_utils
system_utils
tensor_schema
torch_utils
tqdm_utils
v1
v1      cudagraph_dispatcher
kv_cache_interface
kv_cache_layout
kv_cache_spec_registry
outputs
request
serial_utils
utils
attention
attention      backend
selector
backends
backends      cpu_attn
fa_utils
flash_attn
flash_attn_diffkv
flashinfer
flex_attention
gdn_attn
hpc_attn
linear_attn
mamba1_attn
mamba2_attn
mamba_attn
recoverssm_metadata
registry
rocm_aiter_fa
rocm_aiter_unified_attn
rocm_attn
short_conv_attn
triton_attn
triton_attn_diffkv
turboquant_attn
utils
mla
mla      aiter_triton_mla
amx_mla
compressor_utils
cpu_mla
cutlass_mla
flashattn_mla
flashattn_mla_sparse
flashinfer_mla
flashinfer_mla_sparse
flashinfer_mla_sparse_sm120
flashmla
flashmla_sparse
indexer
rocm_aiter_mla
rocm_aiter_mla_sparse
sparse_swa
sparse_utils
tokenspeed_mla
triton_mla
xpu_mla_sparse
prefill
prefill      aiter_flash_attn
base
cpu_sdpa
flash_attn
flashinfer
registry
selector
tokenspeed_mla
trtllm_ragged
ops
ops      chunked_prefill_paged_decode
common
cp_common
dcp
flashmla
flydsl_turboquant_decode
int4_per_token_head
merge_attn_states
paged_attn
pcp
prefix_prefill
rocm_aiter_mla_merge
rocm_aiter_mla_sparse
triton_attention_helpers
triton_decode_attention
triton_fp8_mqa_logits
triton_merge_attn_states
triton_prefill_attention
triton_reshape_and_cache_flash
triton_turboquant_decode
triton_turboquant_store
triton_unified_attention
triton_unified_attention_diffkv
vit_attn_wrappers
xpu_mla_sparse
flydsl_kernels
flydsl_kernels      tq_decode
tq_decode_gqa6
turboquant_soa
turboquant_soa      triton_turboquant_decode
triton_turboquant_decode_v2
triton_turboquant_store
triton_turboquant_unified_attention
core
core      block_pool
encoder_cache_manager
kv_cache_coordinator
kv_cache_manager
kv_cache_metrics
kv_cache_utils
single_type_kv_cache_manager
sched
sched      async_scheduler
interface
output
request_queue
scheduler
utils
engine
engine      async_llm
coordinator
core
core_client
detokenizer
exceptions
input_processor
llm_engine
logprobs
output_processor
parallel_sampling
tensor_ipc
utils
executor
executor      abstract
multiproc_executor
ray_env_utils
ray_executor
ray_executor_v2
ray_utils
uniproc_executor
vllm_net_devices
fault_tolerance
fault_tolerance      engine_core_sentinel
utils
kv_offload
kv_offload      base
config
factory
file_mapper
cpu
cpu      common
gpu_worker
manager
shared_offload_region
spec
swap_blocks_triton
policies
policies      arc
base
factory
lru
tiering
tiering      async_lookup
base
factory
manager
metrics
spec
example
example      manager
fs
fs      io
manager
thread_pool
obj
obj      config
manager
p2p
p2p      manager
control
control      base
zmq
data
data      base
nixl
session
session      client
protocol
server
session
metrics
metrics      loggers
perf
prometheus
ray_wrappers
reader
stats
utils
pool
pool      late_interaction
late_interaction_runner
metadata
sample
sample      metadata
rejection_sampler
sampler
thinking_budget_state
logits_processor
logits_processor      builtin
interface
state
ops
ops      bad_words
logprobs
penalties
topk_topp_sampler
topk_topp_triton
simple_kv_offload
simple_kv_offload      copy_backend
cuda_mem_ops
disk_backend
manager
metadata
worker
spec_decode
spec_decode      custom_class_proposer
dflash
draft_model
eagle
extract_hidden_states
gemma4
llm_base_proposer
medusa
metadata
metrics
ngram_proposer
ngram_proposer_gpu
step3p5
suffix_decoding
utils
vocab_mapping
dynamic
dynamic      utils
structured_output
structured_output      backend_guidance
backend_lm_format_enforcer
backend_outlines
backend_types
backend_xgrammar
request
utils
worker
worker      block_table
cp_utils
cpu_model_runner
cpu_worker
dp_utils
ec_connector_model_runner_mixin
encoder_cudagraph
encoder_cudagraph_defs
gpu_input_batch
gpu_model_runner
gpu_ubatch_wrapper
gpu_worker
kv_connector_model_runner_mixin
lora_model_runner_mixin
mamba_utils
mm_encoder_model_runner
startup_plan
tpu_input_batch
ubatch_utils
ubatching
utils
worker_base
workspace
xpu_model_runner
xpu_worker
cpu
cpu      buffer_utils
model_runner
shm
gpu
gpu      async_utils
attn_utils
block_table
buffer_utils
cp_utils
cudagraph_utils
dp_utils
ec_connector
eplb_utils
input_batch
kv_connector
lora_utils
model_runner
pcp_manager
pp_utils
shutdown
states
structured_outputs
warmup
metrics
metrics      logits
mm
mm      encoder_cache
encoder_runner
lora
rope
model_states
model_states      default
encoder_decoder
encoder_only
interface
mamba_hybrid
mm_pruning
prompt_embeds
recoverssm
pool
pool      pooling_runner
sample
sample      bad_words
batch_shard
gumbel
logit_bias
logprob
min_p
output
penalties
prompt_logprob
sampler
states
thinking_budget
trace_replay
spec_decode
spec_decode      adaptive_verification
extract_hidden_states
rejection_sampler
rejection_sampler_utils
speculator
utils
autoregressive
autoregressive      cudagraph_utils
speculator
dflash
dflash      cudagraph
speculator
utils
dflash2
dflash2      speculator
dspark
dspark      speculator
utils
eagle
eagle      eagle3_utils
speculator
utils
gemma4
gemma4      speculator
mtp
mtp      speculator
multi_module_mtp
multi_module_mtp      speculator
sentinel
sentinel      gpu_worker_sentinel
CLI Reference
CLI Reference       vllm       vllm      chat
complete
run-batch
serve
bench
bench      latency
mm-processor
serve      serve      Table of contents       JSON CLI Arguments
Arguments          custom dataset options
spec bench dataset options
sonnet dataset options
sharegpt dataset options
timed-trace dataset options
blazedit dataset options
asr dataset options
random dataset options
random multimodal dataset options extended from random dataset
hf dataset options
BFCL dataset options
prefix repetition dataset options
speed bench dataset options
sampling parameters
startup
throughput
sweep
sweep      plot
plot_pareto
serve
serve_workload
startup
launch
launch      render
Community       Community      Contact Us
Meetups
Sponsors
Governance       Governance      Collaboration Policy
Committers
Governance Process
Blog
Forum
Slack
Table of contents       JSON CLI Arguments
Arguments          custom dataset options
spec bench dataset options
sonnet dataset options
sharegpt dataset options
timed-trace dataset options
blazedit dataset options
asr dataset options
random dataset options
random multimodal dataset options extended from random dataset
hf dataset options
BFCL dataset options
prefix repetition dataset options
speed bench dataset options
sampling parameters
Home
CLI Reference
vllm
bench
vllm bench serve¶
JSON CLI Arguments¶
When passing JSON CLI arguments, the following sets of arguments are equivalent:
--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'
--json-arg.key1 value1 --json-arg.key2.key3 value2
Additionally, list elements can be passed individually using +:
--json-arg '{"key4": ["value3", "value4", "value5"]}'
--json-arg.key4+ value3 --json-arg.key4+='value4,value5'
Arguments¶
--trust-remote-code¶  Trust remote code from huggingface Default: False  --seed¶  Default: 0  --num-prompts¶  Number of prompts to process. Default: 1000  --dataset-name¶  Possible choices: sharegpt, burstgpt, sonnet, random, random-mm, random-rerank, hf, custom, custom_audio, custom_image, prefix_repetition, spec_bench, speed_bench, timed_trace Name of the dataset to benchmark on. Default: random  --no-stream¶  Do not load the dataset in streaming mode. Default: False  --dataset-path¶  Path to the sharegpt/sonnet dataset or the HF dataset ID if using HF dataset.  --no-oversample¶  Do not oversample if the dataset has fewer samples than num-prompts. Default: False  --skip-chat-template¶  Skip applying chat template to prompt for datasets that support it. Default: False  --enable-multimodal-chat¶  Enable multimodal chat transformation for datasets that support it. Default: False  --disable-shuffle¶  Disable shuffling of dataset samples for deterministic ordering. Default: False  --label¶  The label (prefix) of the benchmark results. If not specified, the value of '--backend' will be used as the label.  --backend¶  Possible choices: vllm, openai, openai-chat, openai-audio, openai-embeddings, openai-embeddings-chat, openai-embeddings-clip, openai-embeddings-vlm2vec, infinity-embeddings, infinity-embeddings-clip, vllm-pooling, vllm-rerank The type of backend or endpoint to use for the benchmark. Default: openai  --base-url¶  Server or API base url if not using http host and port.  --host¶  Default: 127.0.0.1  --port¶  Default: 8000  --endpoint¶  API endpoint. Default: /v1/completions  --header¶  Key-value pairs (e.g, --header x-additional-info=0.3.3) for headers to be passed with each request. These headers override per backend constants and values set via environment variable, and will be overridden by other arguments (such as request ids).  --max-concurrency¶  Maximum number of concurrent requests. This can be used to help simulate an environment where a higher level component is enforcing a maximum number of concurrent requests. While the --request-rate argument controls the rate at which requests are initiated, this argument will control how many are actually allowed to execute at a time. This means that when used in combination, the actual request rate may be lower than specified with --request-rate, if the server is not processing requests fast enough to keep up.  --model¶  Name of the model. If not specified, will fetch the first model from the server's /v1/models endpoint.  --input-len¶  General input length for datasets. Maps to dataset-specific input length arguments (e.g., --random-input-len, --sonnet-input-len). If not specified, uses dataset defaults.  --output-len¶  General output length for datasets. Maps to dataset-specific output length arguments (e.g., --random-output-len, --sonnet-output-len). If not specified, uses dataset defaults.  --tokenizer¶  Name or path of the tokenizer, if not using the default tokenizer.  --tokenizer-mode¶  Tokenizer mode:    - "auto" will use the tokenizer from `mistral_common` for Mistral models
if available, otherwise it will use the "hf" tokenizer.
- "hf" will use the fast tokenizer if available.
- "slow" will always use the slow tokenizer.
- "mistral" will always use the tokenizer from `mistral_common`.
- "deepseek_v32" will always use the tokenizer from `deepseek_v32`.
- Other custom values can be supported via plugins.
Default: auto
--use-beam-search¶  Default: False  --logprobs¶  Number of logprobs-per-token to compute & return as part of the request. If unspecified, then either (1) if beam search is disabled, no logprobs are computed & a single dummy logprob is returned for each token; or (2) if beam search is enabled 1 logprob per token is computed  --request-rate¶  Number of requests per second. If this is inf, then all the requests are sent at time 0. Otherwise, we use Poisson process or gamma distribution to synthesize the request arrival times. Default: inf  --burstiness¶  Burstiness factor of the request generation. Only take effect when request_rate is not inf. Default value is 1, which follows Poisson process. Otherwise, the request intervals follow a gamma distribution. A lower burstiness value (0 < burstiness < 1) results in more bursty requests. A higher burstiness value (burstiness > 1) results in a more uniform arrival of requests. Default: 1.0  --probe-request-rate¶  If positive, send single-token text-only probe requests at this rate (req/s) alongside the main workload, bypassing --max-concurrency, and report their latency separately. Useful for measuring how the main workload stalls unrelated requests. Default: 0.0  --disable-tqdm¶  Specify to disable tqdm progress bar. Default: False  --num-warmups¶  Number of warmup requests. Default: 0  --profile¶  Use vLLM Profiling. --profiler-config must be provided on the server. Default: False  --save-result¶  Specify to save benchmark results to a json file Default: False  --save-detailed¶  When saving the results, whether to include per request information such as response, error, ttfts, tpots, etc. Default: False  --append-result¶  Append the benchmark result to the existing json file. Default: False  --metadata¶  Key-value pairs (e.g, --metadata version=0.3.3 tp=1) for metadata of this run to be saved in the result JSON file for record keeping purposes.  --result-dir¶  Specify directory to save benchmark json results.If not specified, results are saved in the current directory.  --result-filename¶  Specify the filename to save benchmark json results.If not specified, results will be saved in {label}-{args.request_rate}qps-{base_model_id}-{current_dt}.json format.  --ignore-eos¶  Set ignore_eos flag when sending the benchmark request.Warning: ignore_eos is not supported in deepspeed_mii and tgi. Default: False  --self-timed, --no-self-timed¶  Use timing information from the traces instead of the configuration. This is useful when replaying traces faithfully based on their timestamps. When unset, defaults to False, except for --dataset-name=timed_trace where it defaults to True. Use --no-self-timed to force off. When off, user defined generation rates are used and in trace timing info is ignored.  --percentile-metrics¶  Comma-separated list of selected metrics to report percentiles. This argument specifies the metrics to report percentiles. Allowed metric names are "ttft", "tpot", "itl", "e2el". If not specified, defaults to "ttft,tpot,itl" for generative models and "e2el" for pooling models.  --metric-percentiles¶  Comma-separated list of percentiles for selected metrics. To report 25-th, 50-th, and 75-th percentiles, use "25,50,75". Default value is "99".Use "--percentile-metrics" to select metrics. Default: 99  --goodput¶  Specify service level objectives for goodput as "KEY:VALUE" pairs, where the key is a metric name, and the value is in milliseconds. Multiple "KEY:VALUE" pairs can be provided, separated by spaces. Allowed request level metric names are "ttft", "tpot", "e2el". For more context on the definition of goodput, refer to DistServe paper: https://arxiv.org/pdf/2401.09670 and the blog: https://hao-ai-lab.github.io/blogs/distserve  --request-id-prefix¶  Specify the prefix of request id. Default: bench-3919d2d8-  --served-model-name¶  The model name used in the API. If not specified, the model name will be the same as the --model argument.   --lora-modules¶  A subset of LoRA module names passed in when launching the server. For each request, the script chooses a LoRA module at random by default. Use --lora-assignment to control selection strategy.  --lora-assignment¶  Possible choices: random, round-robin Strategy for assigning LoRA modules to requests. 'random' (default) selects a LoRA at random for each request. 'round-robin' cycles through LoRA modules deterministically. Default: random  --ramp-up-strategy¶  Possible choices: linear, exponential The ramp-up strategy. This would be used to ramp up the request rate from initial RPS to final RPS rate (specified by --ramp-up-start-rps and --ramp-up-end-rps.) over the duration of the benchmark.  --ramp-up-start-rps¶  The starting request rate for ramp-up (RPS). Needs to be specified when --ramp-up-strategy is used.  --ramp-up-end-rps¶  The ending request rate for ramp-up (RPS). Needs to be specified when --ramp-up-strategy is used.  --ready-check-timeout-sec¶  Maximum time to wait for the endpoint to become ready in seconds. Ready check will be skipped by default. Default: 0  --chat-template-kwargs¶  A JSON string of kwargs forwarded to the tokenizer's apply_chat_template when a dataset renders prompts client-side (e.g. custom / speed_bench). Example: '{"thinking": true}' to enable reasoning models.  --extra-body¶  A JSON string representing extra body parameters to include in each request.Example: '{"chat_template_kwargs":{"enable_thinking":false}}'  --skip-tokenizer-init¶  Skip initialization of tokenizer and detokenizer Default: False  --insecure¶  Disable SSL certificate verification. Use this option when connecting to servers with self-signed certificates. Default: False  --plot-timeline¶  Generate an HTML timeline plot showing request execution. The plot will be saved alongside the results JSON file. Default: False  --timeline-itl-thresholds¶  ITL thresholds in milliseconds for timeline plot coloring. Specify two comma-separated values to categorize inter-token latencies into three groups: below first threshold (green), between thresholds (orange), and above second threshold (red). Default: 25,50  --plot-dataset-stats¶  Generate a matplotlib figure with dataset statistics showing prompt tokens, output tokens, and combined token distributions. Default: False  custom dataset options¶
--custom-output-len¶  Number of output tokens per request. Unless it is set to -1, the value overrides potential output length loaded from the dataset. It is used only for custom dataset. Default: 256  --custom-ensure-client-side-data¶  Ensure custom dataset media is sent as client-side data instead of references. For custom_image datasets, this loads local and HTTP(S) images on the benchmark client and encodes them as base64 data URLs. Existing data:image URLs are kept unchanged. Default: False  spec bench dataset options¶
--spec-bench-output-len¶  Num of output tokens per request, used only for spec bench dataset. Default: 256  --spec-bench-category¶  Category for spec bench dataset. If None, use all categories.  sonnet dataset options¶
--sonnet-input-len¶  Number of input tokens per request, used only for sonnet dataset. Default: 550  --sonnet-output-len¶  Number of output tokens per request, used only for sonnet dataset. Default: 150  --sonnet-prefix-len¶  Number of prefix tokens per request, used only for sonnet dataset. Default: 200  sharegpt dataset options¶
--sharegpt-output-len¶  Output length for each request. Overrides the output length from the ShareGPT dataset.  timed-trace dataset options¶
--timed-trace-chunk-hash-size¶  Each hash tokens, if present, represent how many token hashes. For example in the Moonshot traces it is 512, while the Qwen/Alibaba has 16. Default: 16  --timed-trace-sec-multiplier¶  What multiplier to use when converting timestamps to seconds. We will multiply timestamps by this. For exampleif the timestamps are in milliseconds, then pass 0.001.If they are already in seconds, then the default 1 is sufficient. Default: 1  --timed-trace-label-timestamp¶  What json label to use to index the timestamp in the trace. Default: timestamp  --timed-trace-label-input-length¶  What json label to use to index the input length field in the trace. Default: input_length  --timed-trace-label-output-length¶  What json label to use to index the output length field in the trace. Default: output_length  --timed-trace-label-hash-ids¶  What json label to use to index the hash ids for the input prompts. Default: hash_ids  blazedit dataset options¶
--blazedit-min-distance¶  Minimum distance for blazedit dataset. Min: 0, Max: 1.0 Default: 0.0  --blazedit-max-distance¶  Maximum distance for blazedit dataset. Min: 0, Max: 1.0 Default: 1.0  asr dataset options¶
--asr-max-audio-len-sec¶  Maximum audio length in seconds for ASR dataset. Default: inf  --asr-min-audio-len-sec¶  Minimum audio length in seconds for ASR dataset. Default: 0.0  random dataset options¶
--random-input-len¶  Number of input tokens per request, used only for random sampling. Default: 1024  --random-output-len¶  Number of output tokens per request, used only for random sampling. Default: 128  --random-range-ratio¶  Range ratio for sampling input/output length, used only for random sampling. A single float applies to both ISL and OSL. A JSON dict like '{"input": 0.3, "output": 0.5}' sets them independently. Values must be in [0, 1). Default: 0.0  --random-prefix-len¶  Number of fixed prefix tokens before the random context in a request. The total input length is the sum of random-prefix-len and a random context length sampled from [input_len * (1 - range_ratio), input_len * (1 + range_ratio)]. Default: 0  --random-batch-size¶  Batch size for random sampling. Only used for embeddings benchmark. Default: 1  --no-reranker¶  Whether the model supports reranking natively. Only used for reranker benchmark. Default: False  random multimodal dataset options extended from random dataset¶
--random-mm-base-items-per-request¶  Base number of multimodal items per request for random-mm. Actual per-request count is sampled around this base using --random-mm-num-mm-items-range-ratio. Default: 1  --random-mm-num-mm-items-range-ratio¶  Range ratio r in [0, 1] for sampling items per request. We sample uniformly from the closed integer range [floor(n(1-r)), ceil(n(1+r))] where n is the base items per request. r=0 keeps it fixed; r=1 allows 0 items. The maximum is clamped to the sum of per-modality limits from --random-mm-limit-mm-per-prompt. An error is raised if the computed min exceeds the max. Default: 0.0  --random-mm-limit-mm-per-prompt¶  Per-modality hard caps for items attached per request, e.g. '{"image": 3, "video": 0}'. The sampled per-request item count is clamped to the sum of these limits. When a modality reaches its cap, its buckets are excluded and probabilities are renormalized.OBS.: Only image sampling is supported for now. Default: {'image': 255, 'video': 1}  --random-mm-bucket-config¶  The bucket config is a dictionary mapping a multimodal itemsampling configuration to a probability.Currently allows for 2 modalities: images and videos. An bucket key is a tuple of (height, width, num_frames)The value is the probability of sampling that specific item. Example: --random-mm-bucket-config {(256, 256, 1): 0.5, (720, 1280, 1): 0.4, (720, 1280, 16): 0.10} First item: images with resolution 256x256 w.p. 0.5Second item: images with resolution 720x1280 w.p. 0.4 Third item: videos with resolution 720x1280 and 16 frames w.p. 0.1OBS.: If the probabilities do not sum to 1, they are normalized.OBS bis.: Only image sampling is supported for now. Default: {(256, 256, 1): 0.5, (720, 1280, 1): 0.5, (720, 1280, 16): 0.0}  hf dataset options¶
--hf-subset¶  Subset of the HF dataset.  --hf-split¶  Split of the HF dataset.  --hf-name¶  Name of the dataset on HuggingFace (e.g., 'lmarena-ai/VisionArena-Chat'). Specify this if your dataset-path is a local path.  --hf-output-len¶  Output length for each request. Overrides the output lengths from the sampled HF dataset.  BFCL dataset options¶
Berkeley Function Calling Leaderboard dataset.
https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard
BFCL ships one JSON-lines file per category at the repo root (e.g. BFCL_v3_simple.json, BFCL_v3_live_simple.json) rather than a single HuggingFace split. Each record has {id, question, function} where function uses a non-OpenAI schema dialect ("type": "dict").
This dataset loader: - downloads the selected per-category files via hf_hub_download and interleaves rows round-robin so sampling is balanced - translates BFCL function schemas to OpenAI tool format - sets :attr:SampleRequest.chat_messages directly and attaches tools / tool_choice via :attr:SampleRequest.request_overrides, producing production-alike tool calling traffic when used with an openai-chat backend
--bfcl-categories¶  Comma-separated list of BFCL v3 category names (without the 'BFCL_v3_' prefix or '.json' suffix) to sample from, e.g. 'simple,live_simple,multiple'. Defaults to 'simple,live_simple,multiple'.  prefix repetition dataset options¶
--prefix-repetition-prefix-len¶  Number of prefix tokens per request, used only for prefix repetition dataset. Default: 256  --prefix-repetition-suffix-len¶  Number of suffix tokens per request, used only for prefix repetition dataset. Total input length is prefix_len + suffix_len. Default: 256  --prefix-repetition-num-prefixes¶  Number of prefixes to generate, used only for prefix repetition dataset. Prompts per prefix is num_requests // num_prefixes. Default: 10  --prefix-repetition-output-len¶  Number of output tokens per request, used only for prefix repetition dataset. Default: 128  speed bench dataset options¶
SPEED-Bench dataset: https://huggingface.co/datasets/nvidia/SPEED-Bench
Download the dataset using:
curl -LsSf https://raw.githubusercontent.com/NVIDIA-NeMo/Skills/refs/heads/main/nemo_skills/dataset/speed-bench/prepare.py | python3 -
--speed-bench-dataset-subset¶  Possible choices: throughput_16k, throughput_8k, qualitative, throughput_1k, throughput_2k, throughput_32k Subset of the SPEED-Bench dataset. Default: qualitative  --speed-bench-output-len¶  Num of output tokens per request, used only for speed bench dataset. Default: 4096  --speed-bench-category¶  Category for speed bench dataset. If None, use all categories.  sampling parameters¶
--top-p¶  Top-p sampling parameter. Only has effect on openai-compatible backends.  --top-k¶  Top-k sampling parameter. Only has effect on openai-compatible backends.  --min-p¶  Min-p sampling parameter. Only has effect on openai-compatible backends.  --temperature¶  Temperature sampling parameter. Only has effect on openai-compatible backends.  --frequency-penalty¶  Frequency penalty sampling parameter. Only has effect on openai-compatible backends.  --presence-penalty¶  Presence penalty sampling parameter. Only has effect on openai-compatible backends.  --repetition-penalty¶  Repetition penalty sampling parameter. Only has effect on openai-compatible backends.       September 8, 2026
Back to top       Made with  Material for MkDocs
