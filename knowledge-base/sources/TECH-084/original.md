## server-h200-tp4-c32.txt


INFO 09-20 06:35:04 [api_utils.py:286] non-default args: {'model_tag': 'deepseek-ai/DeepSeek-V4.1-Flash', 'api_server_count': 1, 'enable_auto_tool_choice': True, 'tool_call_parser': 'deepseek_v41', 'host': '0.0.0.0', 'port': 8888, 'disable_uvicorn_access_log': True, 'model': 'deepseek-ai/DeepSeek-V4.1-Flash', 'tokenizer_mode': 'deepseek_v41', 'max_model_len': 1048576, 'served_model_name': ['deepseek-ai/DeepSeek-V4.1-Flash'], 'safetensors_load_strategy': 'prefetch', 'reasoning_parser': 'deepseek_v41', 'tensor_parallel_size': 4, 'language_model_only': True, 'max_num_batched_tokens': 4096, 'max_num_seqs': 64, 'max_cudagraph_capture_size': 256, 'speculative_config': {'method': 'dspark', 'num_speculative_tokens': 5, 'draft_sample_method': 'probabilistic', 'rejection_sample_method': 'synthetic', 'synthetic_acceptance_length': 3.51, 'enable_adaptive_verification': False}, 'engram_config': EngramConfig(cpu_offload=True, embedding_across_dp=False, dp_shared_memory=False)}

(Worker_TP0 pid=763011) INFO 09-20 06:38:56 [model_runner.py:431] Model loading took 81.21 GiB memory and 145.488524 seconds

(Worker_TP1 pid=763012) INFO 09-20 06:38:56 [model_runner.py:431] Model loading took 81.21 GiB memory and 146.150271 seconds

(Worker_TP2 pid=763013) INFO 09-20 06:39:00 [model_runner.py:431] Model loading took 81.21 GiB memory and 150.085781 seconds

(Worker_TP3 pid=763014) INFO 09-20 06:39:02 [model_runner.py:431] Model loading took 81.21 GiB memory and 151.197460 seconds

(Worker_TP0 pid=763011) INFO 09-20 06:41:39 [gpu_worker.py:640] Available KV cache memory: 35.16 GiB

(EngineCore pid=762611) INFO 09-20 06:41:41 [kv_cache_utils.py:2395] GPU KV cache size: 18,326,608 tokens, Maximum concurrency for 1,048,576 tokens per request: 17.48x

## server-h100-c20.txt


INFO 09-18 06:33:25 [api_utils.py:286] non-default args: {'model_tag': 'deepseek-ai/DeepSeek-V4.1-Flash', 'api_server_count': 1, 'enable_auto_tool_choice': True, 'tool_call_parser': 'deepseek_v41', 'host': '0.0.0.0', 'port': 8888, 'disable_uvicorn_access_log': True, 'model': 'deepseek-ai/DeepSeek-V4.1-Flash', 'tokenizer_mode': 'deepseek_v41', 'max_model_len': 1048576, 'served_model_name': ['deepseek-ai/DeepSeek-V4.1-Flash'], 'reasoning_parser': 'deepseek_v41', 'tensor_parallel_size': 8, 'language_model_only': True, 'max_num_batched_tokens': 4096, 'max_num_seqs': 40, 'max_cudagraph_capture_size': 256, 'speculative_config': {'method': 'dspark', 'num_speculative_tokens': 5, 'draft_sample_method': 'probabilistic', 'rejection_sample_method': 'synthetic', 'synthetic_acceptance_length': 3.51, 'enable_adaptive_verification': False}, 'engram_config': EngramConfig(cpu_offload=True, embedding_across_dp=False, dp_shared_memory=False)}

(Worker_TP1 pid=474155) INFO 09-18 06:40:10 [model_runner.py:431] Model loading took 49.2 GiB memory and 302.100158 seconds

(Worker_TP0 pid=474154) INFO 09-18 06:40:10 [model_runner.py:431] Model loading took 49.2 GiB memory and 302.162213 seconds

(Worker_TP5 pid=474159) INFO 09-18 06:40:17 [model_runner.py:431] Model loading took 49.2 GiB memory and 308.954485 seconds

(Worker_TP6 pid=474160) INFO 09-18 06:40:18 [model_runner.py:431] Model loading took 49.2 GiB memory and 310.381027 seconds

(Worker_TP7 pid=474161) INFO 09-18 06:40:19 [model_runner.py:431] Model loading took 49.2 GiB memory and 310.627588 seconds

(Worker_TP4 pid=474158) INFO 09-18 06:40:19 [model_runner.py:431] Model loading took 49.2 GiB memory and 310.882789 seconds

(Worker_TP2 pid=474156) INFO 09-18 06:40:27 [model_runner.py:431] Model loading took 49.2 GiB memory and 319.279012 seconds

(Worker_TP3 pid=474157) INFO 09-18 06:40:27 [model_runner.py:431] Model loading took 49.2 GiB memory and 319.383186 seconds

(Worker_TP0 pid=474154) INFO 09-18 06:43:34 [gpu_worker.py:640] Available KV cache memory: 12.36 GiB

(EngineCore pid=473862) INFO 09-18 06:43:34 [kv_cache_utils.py:2395] GPU KV cache size: 6,435,008 tokens, Maximum concurrency for 1,048,576 tokens per request: 6.14x

## server-h200-tp8-c32.txt


INFO 09-20 17:38:29 [api_utils.py:286] non-default args: {'model_tag': 'deepseek-ai/DeepSeek-V4.1-Flash', 'api_server_count': 1, 'enable_auto_tool_choice': True, 'tool_call_parser': 'deepseek_v41', 'host': '0.0.0.0', 'port': 8888, 'disable_uvicorn_access_log': True, 'model': 'deepseek-ai/DeepSeek-V4.1-Flash', 'tokenizer_mode': 'deepseek_v41', 'max_model_len': 1048576, 'served_model_name': ['deepseek-ai/DeepSeek-V4.1-Flash'], 'safetensors_load_strategy': 'prefetch', 'reasoning_parser': 'deepseek_v41', 'tensor_parallel_size': 8, 'language_model_only': True, 'max_cudagraph_capture_size': 256, 'speculative_config': {'method': 'dspark', 'num_speculative_tokens': 5, 'draft_sample_method': 'probabilistic', 'rejection_sample_method': 'synthetic', 'synthetic_acceptance_length': 3.51, 'enable_adaptive_verification': False}, 'engram_config': EngramConfig(cpu_offload=True, embedding_across_dp=False, dp_shared_memory=False)}

(Worker_TP0 pid=3197547) INFO 09-20 17:41:47 [model_runner.py:431] Model loading took 49.61 GiB memory and 96.023818 seconds

(Worker_TP2 pid=3197549) INFO 09-20 17:41:56 [model_runner.py:431] Model loading took 49.61 GiB memory and 104.672904 seconds

(Worker_TP1 pid=3197548) INFO 09-20 17:41:57 [model_runner.py:431] Model loading took 49.61 GiB memory and 105.285723 seconds

(Worker_TP4 pid=3197551) INFO 09-20 17:42:04 [model_runner.py:431] Model loading took 49.61 GiB memory and 112.748966 seconds

(Worker_TP5 pid=3197552) INFO 09-20 17:42:04 [model_runner.py:431] Model loading took 49.61 GiB memory and 112.971442 seconds

(Worker_TP6 pid=3197553) INFO 09-20 17:42:04 [model_runner.py:431] Model loading took 49.61 GiB memory and 113.207220 seconds

(Worker_TP3 pid=3197550) INFO 09-20 17:42:05 [model_runner.py:431] Model loading took 49.61 GiB memory and 113.424582 seconds

(Worker_TP7 pid=3197554) INFO 09-20 17:42:06 [model_runner.py:431] Model loading took 49.61 GiB memory and 114.318921 seconds

(Worker_TP0 pid=3197547) INFO 09-20 17:45:04 [gpu_worker.py:640] Available KV cache memory: 62.86 GiB

(EngineCore pid=3197150) INFO 09-20 17:45:07 [kv_cache_utils.py:2395] GPU KV cache size: 29,497,836 tokens, Maximum concurrency for 1,048,576 tokens per request: 28.13x
