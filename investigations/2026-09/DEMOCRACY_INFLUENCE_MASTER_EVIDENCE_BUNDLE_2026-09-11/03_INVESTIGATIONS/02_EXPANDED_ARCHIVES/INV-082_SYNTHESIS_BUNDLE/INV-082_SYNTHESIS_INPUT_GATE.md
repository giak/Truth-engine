---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_input_gate"
artifact_id: "INV-082-SYNTHESIS-INPUT-GATE"
version: "1.0"
status: "pass"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-082"
---

<!-- GATE: dependencies_closed=2/2; canonical_terminal_handoffs=2/2 -->
<!-- DECISION: synthesis_execution=AUTHORIZED; truth_engine_search=NO; generic_web_collection=NO -->

# SYNTHESIS INPUT GATE — INV-082

## Verdict

```text
DEPENDENCIES_CLOSED = 2/2
CANONICAL_TERMINAL_HANDOFFS = 2/2
RECOVERY_HANDOFFS = 0
MISSING_INPUT = 0
GATE = PASS
```

## Input manifest

| Dependency | Input used | Provenance | SHA-256 |
|---|---|---|---|
| INV-081 | `INV-081_RUN_HANDOFF.md` | CANONICAL terminal handoff | `7ac635ec0f5e0726c2cd08bbf7c8d26dcc93daf688c6214ce4080a38bdb11a5f` |
| INV-085 | `INV-085_RUN_HANDOFF.md` | CANONICAL terminal handoff | `907c1e8bee0a4a740bdea31ea0e0fc9ec135297ea1547dc812d52fc1aed49273` |

## Gate rule

Synthesize only these two terminal deltas and proof ceilings. No Truth Engine run or generic collection is authorized. Preserve `economic_concentration != editorial_concentration`, `ownership != editorial_command`, `funding != topic_tasking`, `selection_asymmetry != owner_causation`, `shared_output != coordination`, `reach != persuasion`, and `editorial_effect != electoral_effect`.
