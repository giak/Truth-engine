#!/usr/bin/env python3
import sys, json, time
sys.path.insert(0, '/home/giak/projects/truth-engine/tools/engines/auditor')
from audit import *
from pathlib import Path

article_text = Path('/home/giak/projects/truth-engine/articles/2026-06-13_11-16_eloge_surface_levier_V2_ARTICLE.md').read_text(encoding='utf-8')
blocks = parse_sections(PROMPT_FILE.read_text())

results = {}
total_start = time.time()

def run_phase(idx, pe_tok):
    pid = PHASE_CONFIG[idx][0]
    model = PHASE_CONFIG[idx][1]
    block = blocks[PHASE_CONFIG[idx][2]]
    bench = BENCHMARKS[model]
    label = block.get('label', pid)
    np = PHASE_NUM_PREDICT[pid]
    extra = build_extra(pid, results)
    print()
    print('=' * 60)
    print(f'PHASE {idx}: {label} | {bench["label"]} | np={np}')
    if extra:
        print(f'EXTRA: {len(extra)} chars')
    print('=' * 60)
    messages = build_messages(blocks, block, article_text, pid, extra=extra)
    output, elapsed, tok_count, pe_dur = call_ollama(messages, model, pid, bench, pe_tok)
    valid, warning = validate_output(pid, output)
    print(f'TOK: {tok_count}/{np} | TEMPS: {round(elapsed)}s | PE: {round(pe_dur)}s | VALID: {valid}')
    if warning:
        print(f'WARN: {warning}')
    print(f'OUTPUT ({len(output)} chars):')
    print(output[:250] + ('...' if len(output) > 250 else ''))
    results[pid] = {'pid': pid, 'model': model, 'label': label, 'output': output, 'tok_count': tok_count, 'elapsed': elapsed, 'valid': valid, 'warning': warning}
    return results[pid]

run_phase(0, 500)   # Ph0
run_phase(2, 4000)  # G1
run_phase(3, 4000)  # G2
run_phase(4, 4000)  # G3
run_phase(5, 4000)  # G4
run_phase(6, 5000)  # Ph3
run_phase(7, 5000)  # Ph4
run_phase(8, 3000)  # Ph5
run_phase(9, 2000)  # Ph6 VETO

print()
print('=' * 60)
print(f'PIPELINE TERMINE - {round(time.time() - total_start)}s')
print('=' * 60)

ph6_out = results.get('phase6_veto', {}).get('output', '')
print('\n=== Ph6 VETO COMPLET ===')
print(ph6_out)
print('=== FIN Ph6 ===')
