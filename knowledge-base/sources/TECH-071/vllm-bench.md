## vllm bench serve

## JSON CLI Arguments

When passing JSON CLI arguments, the following sets of arguments are equivalent:

- `--json-arg '{"key1": "value1", "key2": {"key3": "value2"}}'`
- `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

- `--json-arg '{"key4": ["value3", "value4", "value5"]}'`
- `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## Arguments

#### \--trust-remote-code

Trust remote code from huggingface

Default: `False`

#### \--seed

Default: `0`

#### \--num-prompts

Number of prompts to process.

Default: `1000`

#### \--dataset-name

Possible choices: `sharegpt`, `burstgpt`, `sonnet`, `random`, `random-mm`, `random-rerank`, `hf`, `custom`, `custom_audio`, `custom_image`, `prefix_repetition`, `spec_bench`, `speed_bench`, `timed_trace`

Name of the dataset to benchmark on.

Default: `random`

#### \--no-stream

Do not load the dataset in streaming mode.

Default: `False`

#### \--dataset-path

Path to the sharegpt/sonnet dataset or the HF dataset ID if using HF dataset.

#### \--no-oversample

Do not oversample if the dataset has fewer samples than num-prompts.

Default: `False`

#### \--skip-chat-template

Skip applying chat template to prompt for datasets that support it.

Default: `False`

#### \--enable-multimodal-chat

Enable multimodal chat transformation for datasets that support it.

Default: `False`

#### \--disable-shuffle

Disable shuffling of dataset samples for deterministic ordering.

Default: `False`

#### \--label

The label (prefix) of the benchmark results. If not specified, the value of '--backend' will be used as the label.

#### \--backend

Possible choices: `vllm`, `openai`, `openai-chat`, `openai-audio`, `openai-embeddings`, `openai-embeddings-chat`, `openai-embeddings-clip`, `openai-embeddings-vlm2vec`, `infinity-embeddings`, `infinity-embeddings-clip`, `vllm-pooling`, `vllm-rerank`

The type of backend or endpoint to use for the benchmark.

Default: `openai`

#### \--base-url

Server or API base url if not using http host and port.

#### \--host

Default: `127.0.0.1`

#### \--port

Default: `8000`

#### \--endpoint

API endpoint.

Default: `/v1/completions`

#### \--header

Key-value pairs (e.g, --header x-additional-info=0.3.3) for headers to be passed with each request. These headers override per backend constants and values set via environment variable, and will be overridden by other arguments (such as request ids).

#### \--max-concurrency

Maximum number of concurrent requests. This can be used to help simulate an environment where a higher level component is enforcing a maximum number of concurrent requests. While the --request-rate argument controls the rate at which requests are initiated, this argument will control how many are actually allowed to execute at a time. This means that when used in combination, the actual request rate may be lower than specified with --request-rate, if the server is not processing requests fast enough to keep up.

#### \--model

Name of the model. If not specified, will fetch the first model from the server's /v1/models endpoint.

#### \--input-len

General input length for datasets. Maps to dataset-specific input length arguments (e.g., --random-input-len, --sonnet-input-len). If not specified, uses dataset defaults.

#### \--output-len

General output length for datasets. Maps to dataset-specific output length arguments (e.g., --random-output-len, --sonnet-output-len). If not specified, uses dataset defaults.

#### \--tokenizer

Name or path of the tokenizer, if not using the default tokenizer.

#### \--tokenizer-mode

Tokenizer mode:
```
- "auto" will use the tokenizer from \`mistral_common\` for Mistral models
if available, otherwise it will use the "hf" tokenizer.

- "hf" will use the fast tokenizer if available.

- "slow" will always use the slow tokenizer.

- "mistral" will always use the tokenizer from \`mistral_common\`.

- "deepseek_v32" will always use the tokenizer from \`deepseek_v32\`.

- Other custom values can be supported via plugins.
```

Default: `auto`

#### \--use-beam-search

Default: `False`

#### \--logprobs

Number of logprobs-per-token to compute & return as part of the request. If unspecified, then either (1) if beam search is disabled, no logprobs are computed & a single dummy logprob is returned for each token; or (2) if beam search is enabled 1 logprob per token is computed

#### \--request-rate

Number of requests per second. If this is inf, then all the requests are sent at time 0. Otherwise, we use Poisson process or gamma distribution to synthesize the request arrival times.

Default: `inf`

#### \--burstiness

Burstiness factor of the request generation. Only take effect when request\_rate is not inf. Default value is 1, which follows Poisson process. Otherwise, the request intervals follow a gamma distribution. A lower burstiness value (0 < burstiness < 1) results in more bursty requests. A higher burstiness value (burstiness > 1) results in a more uniform arrival of requests.

Default: `1.0`

#### \--probe-request-rate

If positive, send single-token text-only probe requests at this rate (req/s) alongside the main workload, bypassing --max-concurrency, and report their latency separately. Useful for measuring how the main workload stalls unrelated requests.

Default: `0.0`

#### \--disable-tqdm

Specify to disable tqdm progress bar.

Default: `False`

#### \--num-warmups

Number of warmup requests.

Default: `0`

#### \--profile

Use vLLM Profiling. --profiler-config must be provided on the server.

Default: `False`

#### \--save-result

Specify to save benchmark results to a json file

Default: `False`

#### \--save-detailed

When saving the results, whether to include per request information such as response, error, ttfts, tpots, etc.

Default: `False`

#### \--append-result

Append the benchmark result to the existing json file.

Default: `False`

#### \--metadata

Key-value pairs (e.g, --metadata version=0.3.3 tp=1) for metadata of this run to be saved in the result JSON file for record keeping purposes.

#### \--result-dir

Specify directory to save benchmark json results.If not specified, results are saved in the current directory.

#### \--result-filename

Specify the filename to save benchmark json results.If not specified, results will be saved in {label}-{args.request\_rate}qps-{base\_model\_id}-{current\_dt}.json format.

#### \--ignore-eos

Set ignore\_eos flag when sending the benchmark request.Warning: ignore\_eos is not supported in deepspeed\_mii and tgi.

Default: `False`

#### \--self-timed, --no-self-timed

Use timing information from the traces instead of the configuration. This is useful when replaying traces faithfully based on their timestamps. When unset, defaults to False, except for --dataset-name=timed\_trace where it defaults to True. Use --no-self-timed to force off. When off, user defined generation rates are used and in trace timing info is ignored.

#### \--percentile-metrics

Comma-separated list of selected metrics to report percentiles. This argument specifies the metrics to report percentiles. Allowed metric names are "ttft", "tpot", "itl", "e2el", "client\_queue\_time", "e2el\_including\_client\_queue". If not specified, defaults to "ttft,tpot,itl" for generative models and "e2el" for pooling models.

#### \--metric-percentiles

Comma-separated list of percentiles for selected metrics. To report 25-th, 50-th, and 75-th percentiles, use "25,50,75". Default value is "99".Use "--percentile-metrics" to select metrics.

Default: `99`

#### \--goodput

Specify service level objectives for goodput as "KEY:VALUE" pairs, where the key is a metric name, and the value is in milliseconds. Multiple "KEY:VALUE" pairs can be provided, separated by spaces. Allowed request level metric names are "ttft", "tpot", "e2el". For more context on the definition of goodput, refer to DistServe paper: https://arxiv.org/pdf/2401.09670 and the blog: https://hao-ai-lab.github.io/blogs/distserve

#### \--request-id-prefix

Specify the prefix of request id.

Default: `bench-5e82c48e-`

#### \--served-model-name

The model name used in the API. If not specified, the model name will be the same as the `--model` argument.

#### \--lora-modules

A subset of LoRA module names passed in when launching the server. For each request, the script chooses a LoRA module at random by default. Use --lora-assignment to control selection strategy.

#### \--lora-assignment

Possible choices: `random`, `round-robin`

Strategy for assigning LoRA modules to requests. 'random' (default) selects a LoRA at random for each request. 'round-robin' cycles through LoRA modules deterministically.

Default: `random`

#### \--ramp-up-strategy

Possible choices: `linear`, `exponential`

The ramp-up strategy. This would be used to ramp up the request rate from initial RPS to final RPS rate (specified by --ramp-up-start-rps and --ramp-up-end-rps.) over the duration of the benchmark.

#### \--ramp-up-start-rps

The starting request rate for ramp-up (RPS). Needs to be specified when --ramp-up-strategy is used.

#### \--ramp-up-end-rps

The ending request rate for ramp-up (RPS). Needs to be specified when --ramp-up-strategy is used.

#### \--ready-check-timeout-sec

Maximum time to wait for the endpoint to become ready in seconds. Ready check will be skipped by default.

Default: `0`

#### \--chat-template-kwargs

A JSON string of kwargs forwarded to the tokenizer's apply\_chat\_template when a dataset renders prompts client-side (e.g. custom / speed\_bench). Example: '{"thinking": true}' to enable reasoning models.

#### \--extra-body

A JSON string representing extra body parameters to include in each request.Example: '{"chat\_template\_kwargs":{"enable\_thinking":false}}'

#### \--skip-tokenizer-init

Skip initialization of tokenizer and detokenizer

Default: `False`

#### \--insecure

Disable SSL certificate verification. Use this option when connecting to servers with self-signed certificates.

Default: `False`

#### \--plot-timeline

Generate an HTML timeline plot showing request execution. The plot will be saved alongside the results JSON file.

Default: `False`

#### \--timeline-itl-thresholds

ITL thresholds in milliseconds for timeline plot coloring. Specify two comma-separated values to categorize inter-token latencies into three groups: below first threshold (green), between thresholds (orange), and above second threshold (red).

Default: `25,50`

#### \--plot-dataset-stats

Generate a matplotlib figure with dataset statistics showing prompt tokens, output tokens, and combined token distributions.

Default: `False`

### custom dataset options

#### \--custom-output-len

Number of output tokens per request. Unless it is set to -1, the value overrides potential output length loaded from the dataset. It is used only for custom dataset.

Default: `256`

#### \--custom-ensure-client-side-data

Ensure custom dataset media is sent as client-side data instead of references. For custom\_image datasets, this loads local and HTTP(S) images on the benchmark client and encodes them as base64 data URLs. Existing data:image URLs are kept unchanged.

Default: `False`

### spec bench dataset options

#### \--spec-bench-output-len

Num of output tokens per request, used only for spec bench dataset.

Default: `256`

#### \--spec-bench-category

Category for spec bench dataset. If None, use all categories.

### sonnet dataset options

#### \--sonnet-input-len

Number of input tokens per request, used only for sonnet dataset.

Default: `550`

#### \--sonnet-output-len

Number of output tokens per request, used only for sonnet dataset.

Default: `150`

#### \--sonnet-prefix-len

Number of prefix tokens per request, used only for sonnet dataset.

Default: `200`

### sharegpt dataset options

#### \--sharegpt-output-len

Output length for each request. Overrides the output length from the ShareGPT dataset.

### timed-trace dataset options

#### \--timed-trace-chunk-hash-size

Each hash tokens, if present, represent how many token hashes. For example in the Moonshot traces it is 512, while the Qwen/Alibaba has 16.

Default: `16`

#### \--timed-trace-sec-multiplier

What multiplier to use when converting timestamps to seconds. We will multiply timestamps by this. For exampleif the timestamps are in milliseconds, then pass 0.001.If they are already in seconds, then the default 1 is sufficient.

Default: `1`

#### \--timed-trace-label-timestamp

What json label to use to index the timestamp in the trace.

Default: `timestamp`

#### \--timed-trace-label-input-length

What json label to use to index the input length field in the trace.

Default: `input_length`

#### \--timed-trace-label-output-length

What json label to use to index the output length field in the trace.

Default: `output_length`

#### \--timed-trace-label-hash-ids

What json label to use to index the hash ids for the input prompts.

Default: `hash_ids`

### blazedit dataset options

#### \--blazedit-min-distance

Minimum distance for blazedit dataset. Min: 0, Max: 1.0

Default: `0.0`

#### \--blazedit-max-distance

Maximum distance for blazedit dataset. Min: 0, Max: 1.0

Default: `1.0`

### asr dataset options

#### \--asr-max-audio-len-sec

Maximum audio length in seconds for ASR dataset.

Default: `inf`

#### \--asr-min-audio-len-sec

Minimum audio length in seconds for ASR dataset.

Default: `0.0`

### random dataset options

#### \--random-input-len

Number of input tokens per request, used only for random sampling.

Default: `1024`

#### \--random-output-len

Number of output tokens per request, used only for random sampling.

Default: `128`

#### \--random-range-ratio

Range ratio for sampling input/output length, used only for random sampling. A single float applies to both ISL and OSL. A JSON dict like '{"input": 0.3, "output": 0.5}' sets them independently. Values must be in \[0, 1).

Default: `0.0`

#### \--random-prefix-len

Number of fixed prefix tokens before the random context in a request. The total input length is the sum of `random-prefix-len` and a random context length sampled from \[input\_len \* (1 - range\_ratio), input\_len \* (1 + range\_ratio)\].

Default: `0`

#### \--random-batch-size

Batch size for random sampling. Only used for embeddings benchmark.

Default: `1`

#### \--no-reranker

Whether the model supports reranking natively. Only used for reranker benchmark.

Default: `False`

### random multimodal dataset options extended from random dataset

#### \--random-mm-base-items-per-request

Base number of multimodal items per request for random-mm. Actual per-request count is sampled around this base using --random-mm-num-mm-items-range-ratio.

Default: `1`

#### \--random-mm-num-mm-items-range-ratio

Range ratio r in \[0, 1\] for sampling items per request. We sample uniformly from the closed integer range \[floor(n *(1-r)), ceil(n* (1+r))\] where n is the base items per request. r=0 keeps it fixed; r=1 allows 0 items. The maximum is clamped to the sum of per-modality limits from --random-mm-limit-mm-per-prompt. An error is raised if the computed min exceeds the max.

Default: `0.0`

#### \--random-mm-limit-mm-per-prompt

Per-modality hard caps for items attached per request, e.g. '{"image": 3, "video": 0}'. The sampled per-request item count is clamped to the sum of these limits. When a modality reaches its cap, its buckets are excluded and probabilities are renormalized.OBS.: Only image sampling is supported for now.

Default: `{'image': 255, 'video': 1}`

#### \--random-mm-bucket-config

The bucket config is a dictionary mapping a multimodal itemsampling configuration to a probability.Currently allows for 2 modalities: images and videos. An bucket key is a tuple of (height, width, num\_frames)The value is the probability of sampling that specific item. Example: --random-mm-bucket-config {(256, 256, 1): 0.5, (720, 1280, 1): 0.4, (720, 1280, 16): 0.10} First item: images with resolution 256x256 w.p. 0.5Second item: images with resolution 720x1280 w.p. 0.4 Third item: videos with resolution 720x1280 and 16 frames w.p. 0.1OBS.: If the probabilities do not sum to 1, they are normalized.OBS bis.: Only image sampling is supported for now.

Default: `{(256, 256, 1): 0.5, (720, 1280, 1): 0.5, (720, 1280, 16): 0.0}`

### hf dataset options

#### \--hf-subset

Subset of the HF dataset.

#### \--hf-split

Split of the HF dataset.

#### \--hf-name

Name of the dataset on HuggingFace (e.g., 'lmarena-ai/VisionArena-Chat'). Specify this if your dataset-path is a local path.

#### \--hf-output-len

Output length for each request. Overrides the output lengths from the sampled HF dataset.

### BFCL dataset options

Berkeley Function Calling Leaderboard dataset.

https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard

BFCL ships one JSON-lines file per category at the repo root (e.g. `BFCL_v3_simple.json`, `BFCL_v3_live_simple.json`) rather than a single HuggingFace split. Each record has `{id, question, function}` where `function` uses a non-OpenAI schema dialect (`"type": "dict"`).

This dataset loader: - downloads the selected per-category files via `hf_hub_download` and interleaves rows round-robin so sampling is balanced - translates BFCL function schemas to OpenAI tool format - sets:attr:`SampleRequest.chat_messages` directly and attaches `tools` / `tool_choice` via:attr:`SampleRequest.request_overrides`, producing production-alike tool calling traffic when used with an `openai-chat` backend

#### \--bfcl-categories

Comma-separated list of BFCL v3 category names (without the 'BFCL\_v3\_' prefix or '.json' suffix) to sample from, e.g. 'simple,live\_simple,multiple'. Defaults to 'simple,live\_simple,multiple'.

### prefix repetition dataset options

#### \--prefix-repetition-prefix-len

Number of prefix tokens per request, used only for prefix repetition dataset.

Default: `256`

#### \--prefix-repetition-suffix-len

Number of suffix tokens per request, used only for prefix repetition dataset. Total input length is prefix\_len + suffix\_len.

Default: `256`

#### \--prefix-repetition-num-prefixes

Number of prefixes to generate, used only for prefix repetition dataset. Prompts per prefix is num\_requests // num\_prefixes.

Default: `10`

#### \--prefix-repetition-output-len

Number of output tokens per request, used only for prefix repetition dataset.

Default: `128`

### speed bench dataset options

SPEED-Bench dataset: https://huggingface.co/datasets/nvidia/SPEED-Bench.

Download the dataset using:

`curl -LsSf https://raw.githubusercontent.com/NVIDIA-NeMo/Skills/refs/heads/main/nemo_skills/dataset/speed-bench/prepare.py | python3 -`

#### \--speed-bench-dataset-subset

Possible choices: `throughput_2k`, `qualitative`, `throughput_1k`, `throughput_8k`, `throughput_32k`, `throughput_16k`

Subset of the SPEED-Bench dataset.

Default: `qualitative`

#### \--speed-bench-output-len

Num of output tokens per request, used only for speed bench dataset.

Default: `4096`

#### \--speed-bench-category

Category for speed bench dataset. If None, use all categories.

### sampling parameters

#### \--top-p

Top-p sampling parameter. Only has effect on openai-compatible backends.

#### \--top-k

Top-k sampling parameter. Only has effect on openai-compatible backends.

#### \--min-p

Min-p sampling parameter. Only has effect on openai-compatible backends.

#### \--temperature

Temperature sampling parameter. Only has effect on openai-compatible backends.

#### \--frequency-penalty

Frequency penalty sampling parameter. Only has effect on openai-compatible backends.

#### \--presence-penalty

Presence penalty sampling parameter. Only has effect on openai-compatible backends.

#### \--repetition-penalty

Repetition penalty sampling parameter. Only has effect on openai-compatible backends.