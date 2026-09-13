---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_input_gate"
artifact_id: "INV-146-SYNTHESIS-INPUT-GATE"
version: "1.0"
status: "pass_with_recovery"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-146"
---

<!-- GATE: dependencies_closed=10/10; usable_terminal_handoffs=10/10 -->
<!-- RECOVERY: INV-139,INV-140; original_missing_library_artifacts_not_recreated=true -->
<!-- DECISION: synthesis_execution=AUTHORIZED; truth_engine_search=NO -->

# SYNTHESIS INPUT GATE — INV-146

## Verdict

```text
DEPENDENCIES_CLOSED = 10/10
CANONICAL_TERMINAL_HANDOFFS = 8
RECOVERY_HANDOFFS = 2
USABLE_SYNTHESIS_INPUTS = 10/10
MISSING_INPUT = 0
FABRICATED_RUNTIME_ID = 0
GATE = PASS_WITH_RECOVERY
```

## Input manifest

| Dependency | Input used | Provenance status | SHA-256 |
|---|---|---|---|
| INV-019 | `INV-019_RUN_HANDOFF.md` | CANONICAL terminal handoff | `c72fff3b19b5ab1b2bd36b064544c1a3635f42e3d30b99c8c225e616f1d76c9b` |
| INV-022 | `INV-022_RUN_HANDOFF.md` | CANONICAL terminal handoff | `23728306a8c672f7ed4b31f7e8c668676a16dcb6a295716df25697855d03ebe0` |
| INV-026 | `INV-026_RUN_HANDOFF.md` | CANONICAL terminal handoff | `bf70cae7b998ae0aa16949f1f12cb8258d4d4de9527316832b9cb398531ae4cb` |
| INV-033 | `INV-033_RUN_HANDOFF.md` | CANONICAL terminal handoff | `a33fa3cb614d41e2c2ac4319f2081bfaa210f7f556997cc853ac81a5b5549ebb` |
| INV-128 | `INV-128_RUN_HANDOFF.md` | CANONICAL terminal handoff | `e6ebbe716642c098fccd8d02f7ebd4bb6677f8647b7022e530d0c83fbdfc977d` |
| INV-134 | `INV-134_RUN_HANDOFF.md` | CANONICAL terminal handoff | `86ecbc873978c6a375d21dd9f145f299f2ba3edd8460615d040034b459e7cd6a` |
| INV-138 | `INV-138_RUN_HANDOFF.md` | CANONICAL terminal handoff | `33cf00cd572c2109187d853d87848aa22c0d81371fdbfcc089e3a085d8551845` |
| INV-139 | `INV-139_RECOVERY_HANDOFF.md` | RECOVERY / bounded | `4f1519ff60088529dcb42bed830fc5df8c8aa2218063e3dcb73f8e0d11a8405a` |
| INV-140 | `INV-140_RECOVERY_HANDOFF.md` | RECOVERY / bounded | `aec894571a3eee531ea92bd386da1ecb664e9a7bd27c82ee2a73b330f26cb083` |
| INV-145 | `INV-145_RUN_HANDOFF.md` | CANONICAL terminal handoff | `e1987224267601dc9d8ea84bbf33137cd9d2df7b0b348484cb26e7be6a085aee` |

## Recovery disposition

`INV-139`: the original final Library artifact is unavailable. Recovery uses the persisted CP3 state (14 factual records) plus append-only terminal metadata proving later DELIVERY PASS / 22 QRY / 22 SRC / 22 FCT / P0=0 / P1=0 / P2=3. Missing final fact IDs and bytes are not reconstructed.

`INV-140`: the final bundle/handoff is unavailable, but the frozen terminal technical narrative is present and contains the central delta, proof ceilings and terminal gaps. The recovery handoff compresses that material without inventing runtime IDs.

These recoveries are sufficient for INV-146 because the synthesis consumes terminal deltas and proof ceilings, not the duplicated source/fact registries. Any claim depending on unavailable detail is excluded rather than inferred.

## Gate rule

The synthesis may proceed only from the ten listed inputs. No generic web collection or Truth Engine run is authorized by this gate.
