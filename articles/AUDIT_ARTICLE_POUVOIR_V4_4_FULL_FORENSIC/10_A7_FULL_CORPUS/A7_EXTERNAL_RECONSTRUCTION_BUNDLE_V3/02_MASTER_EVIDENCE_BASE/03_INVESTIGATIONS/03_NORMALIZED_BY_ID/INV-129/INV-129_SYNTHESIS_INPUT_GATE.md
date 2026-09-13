---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_input_gate"
artifact_id: "INV-129-SYNTHESIS-INPUT-GATE"
version: "1.0"
status: "pass"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-129"
---

<!-- GATE: dependencies_closed=4/4; canonical_terminal_handoffs=4/4 -->
<!-- DECISION: synthesis_execution=AUTHORIZED; truth_engine_search=NO; generic_web_collection=NO -->

# SYNTHESIS INPUT GATE — INV-129

## Verdict

```text
DEPENDENCIES_CLOSED = 4/4
CANONICAL_TERMINAL_HANDOFFS = 4/4
RECOVERY_HANDOFFS = 0
MISSING_INPUT = 0
GATE = PASS
```

## Input manifest

| Dependency | Input used | Provenance | SHA-256 |
|---|---|---|---|
| INV-054 | `INV-054_RUN_HANDOFF.md` | CANONICAL terminal handoff | `64c37752d4c1dd713f6143766d652b8c6fe39981e603fcc2854d9cb71d574c1a` |
| INV-080 | `INV-080_RUN_HANDOFF.md` | CANONICAL terminal handoff | `fdcb8afe0233186f15b7fbb8a1c3e157a3cb255078cc5423eed8c477f989a355` |
| INV-100 | `INV-100_RUN_HANDOFF.md` | CANONICAL terminal handoff | `aa8fb0bf28eb888c88e5c913703a9e5d008ab7dc73bd3e052e193dc98bd385e6` |
| INV-124 | `INV-124_RUN_HANDOFF.md` | CANONICAL terminal handoff | `9c77cc8bafdf50cb43bad1b99fa96a1347f5b205170b78ebebdf5bd2478a14b4` |

## Gate rule

Synthesize only the four listed terminal deltas and proof ceilings. No Truth Engine run or generic collection is authorized. Preserve `legal != legitimate`, `adverse_effect != political_motive`, `litigation != control_of_judge`, `administrative_measure != guilt`, `private_decision != state_command`, and `institutional_effect != electoral_effect`.
