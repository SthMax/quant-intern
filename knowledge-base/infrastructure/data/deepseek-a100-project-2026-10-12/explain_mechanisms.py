"""Recompute the presentation's component-level examples from archived config.

Standard library only; no upstream imports, network, GPU or model execution.
"""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[2] / 'sources/TECH-077'
config_path = SOURCE / 'official-inference-config.json'
c = json.loads(config_path.read_text())
params = 3 * c['dim'] * c['moe_inter_dim']
e, k, layers = c['n_routed_experts'], c['n_activated_experts'], c['n_layers']
native_index_path = SOURCE.parent / 'TECH-079/model.safetensors.index.json'
native_config_path = SOURCE.parent / 'TECH-079/config.json'
native_bytes = json.loads(native_index_path.read_text())['metadata']['total_size']
nc = json.loads(native_config_path.read_text())['text_config']
engram_bytes = sum(nc['engram_num_embeddings']) * (nc['engram_head_dim'] + nc['engram_head_dim']//32)
remaining_bytes = native_bytes - engram_bytes
bytes_per_fp4_weight = .5 + 1 / 32
per_expert = params * layers * bytes_per_fp4_weight
result = {
    'date': '2026-10-14',
    'source_revision': '580568edd6f84537ff042ded4ee842b892bf3ff4',
    'config_sha256': hashlib.sha256(config_path.read_bytes()).hexdigest(),
    'scope': 'Component-level CPU arithmetic; not whole-service speed predictions.',
    'native_checkpoint_budget': {
        'checkpoint_bytes': native_bytes,
        'engram_host_bytes': engram_bytes,
        'remaining_checkpoint_bytes': remaining_bytes,
        'remaining_checkpoint_gib': remaining_bytes / 2**30,
        'ideal_four_gpu_weight_gib_each': remaining_bytes / 4 / 2**30,
        'comparison_baseline': 'Official native mixed FP4/FP8 checkpoint with Engram host offload; common to both runtime approaches.',
        'scope': 'File payload allocation; runtime copies, buffers, KV, and per-rank imbalance are additional.',
        'index_sha256': hashlib.sha256(native_index_path.read_bytes()).hexdigest(),
        'config_sha256': hashlib.sha256(native_config_path.read_bytes()).hexdigest(),
    },
    'routed_experts': {
        'parameters_per_expert_per_layer': params,
        'parameters_all_layers': params * layers * e,
        'bf16_bytes': params * layers * e * 2,
        'bf16_comparison_role': 'Hypothetical dtype teaching example only; not a released full-BF16 deployment baseline or memory savings attributable to this project.',
        'fp4_with_one_scale_byte_per_32_values_bytes': params * layers * e * bytes_per_fp4_weight,
        'compressed_fraction_of_bf16': bytes_per_fp4_weight / 2,
        'reduction_percent': (1 - bytes_per_fp4_weight / 2) * 100,
    },
    'dense_w8': {'fraction_of_bf16': (1 + 1 / 1024) / 2},
    'ideal_expert_reuse': [
        {'batch': b, 'expert_routing_events': k * b,
         'expected_distinct_experts': e * (1 - (1 - k/e)**b),
         'ideal_weight_reuse': k * b / (e * (1 - (1 - k/e)**b))}
        for b in [1, 8, 32, 64, 256, 1024]
    ],
    'reuse_assumption': 'Independent uniform selection of 6 distinct experts per token; one ideal weight read per expert. Actual tiling and route skew change traffic.',
    'mtp': {'ordinary_ms_per_token': 15.8, 'k3_step_ms': 31,
            'k3_tokens': 2.53, 'k3_tokens_s': 2.53/.031,
            'k3_speedup': 2.53*15.8/31, 'k5_step_ms': 33,
            'k5_tokens': 2.79, 'k5_tokens_s': 2.79/.033,
            'k5_speedup': 2.79*15.8/33},
    'ced': {'prompt_tokens': 1000000, 'sequential_tail': 128,
            'pipeline_tail': 2048, 'full_layer_tokens': 40*1000000,
            'sequential_layer_tokens': 21*1000000+19*128,
            'pipeline_layer_tokens': 21*1000000+19*2048},
    'indexer_intermediate': {
        'queries_per_chunk': 64, 'keys': 1000000, 'heads': c['index_n_heads'],
        'dtype_bytes': 4, 'all_heads_bytes': 64*1000000*c['index_n_heads']*4,
        'one_head_bytes': 64*1000000*4, 'ideal_component_ratio': c['index_n_heads'],
        'scope': 'One score tensor; accumulator/current-head tensors and other allocations can coexist.'},
    'author_throughput_table': {
        'single_end_to_end': 50.3, 'c64_end_to_end': 167.5,
        'c64_peak_engine': 475.6, 'end_to_end_ratio': 167.5/50.3,
        'peak_ratio': 475.6/50.3,
        'workload_note': 'Different configured context caps, short actual prompts; no per-run raw records.'},
    'expert_rebalance': {
        'bytes_per_expert_all_layers': per_expert,
        'even_96_to_84_freed_gib': 12*per_expert/2**30,
        'standard_98_to_84_freed_gib': 14*per_expert/2**30},
}
assert native_bytes == 510286023000
assert engram_bytes == 202758032400
assert remaining_bytes == 307527990600
assert params * layers * e == 543581798400
assert result['routed_experts']['compressed_fraction_of_bf16'] == .265625
assert result['ideal_expert_reuse'][0]['expected_distinct_experts'] == 6
assert result['indexer_intermediate']['all_heads_bytes'] == 8192000000
assert round(result['expert_rebalance']['standard_98_to_84_freed_gib'], 2) == 9.81
(HERE/'mechanism-analysis.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print('Component examples passed: weights, ideal expert reuse, MTP, CED, indexer and rebalance.')
