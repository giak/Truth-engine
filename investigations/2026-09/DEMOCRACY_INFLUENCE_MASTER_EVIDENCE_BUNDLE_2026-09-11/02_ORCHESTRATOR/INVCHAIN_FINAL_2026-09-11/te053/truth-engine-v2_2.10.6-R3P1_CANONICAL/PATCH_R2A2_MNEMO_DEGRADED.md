---
trace_schema: "forensic-md/v1"
project: "truth-engine"
artifact_type: "runtime_patch"
artifact_id: "R2A2-MNEMO-DEGRADED"
version: "R2A.2"
status: "candidate"
updated: "2026-09-05"
canonical_ref: "KERNEL.md"
---

<!-- DERIVED_FROM: bundle=R2A.1; defect=MNEMO_UNAVAILABLE_delivery_contradiction -->
<!-- DECISION: engine=2.10.6; revision_only=R2A.2; no_semantic_fact_downgrade=true -->

# R2A.2 — MNEMO_UNAVAILABLE delivery contract

## Defect

R2A.1 allowed an eligible FACT to be blocked for `MNEMO_UNAVAILABLE`, but
`persistence_attempt_result()` required every eligible FACT to have `success=1`
and a memory id. `export-snapshot` then also rejected every eligible FACT with
`mem:-`.

This made the documented degraded mode impossible to deliver.

## Contract

An eligible FACT has exactly one terminal persistence outcome:

```text
SUCCESS := attempted=1 success=1 failure=0 blocked=0 AND memory_id present
BLOCKED := attempted=0 success=0 failure=0 blocked=1 AND allowed observed reason
```

`PERSIST_REBIND=PASS` means every eligible FACT has one valid terminal outcome
and aggregate accounting matches. It does **not** mean every Mnemo write
succeeded.

For `MNEMO_UNAVAILABLE`, `BLOCKED` additionally requires:
- `run.degraded_flags` contains `MNEMO_UNAVAILABLE`;
- `MNEMO_ROW` visibly records `MNEMO_UNAVAILABLE`;
- FACT memory id remains `-`.

The local snapshot is still emitted. It keeps `memory_id:"-"` for blocked FACTs.
No fake memory id is created.

## Non-regression

When Mnemo is available:
- a successful eligible write still requires a real memory id;
- failures remain FAIL;
- malformed/unobserved block reasons remain non-terminal;
- DELIVERY still requires snapshot, terminal last persistence PASS and
  `PERSIST_REBIND=PASS`.

## Files changed

- `KERNEL.md`
- `tools/runtime/run_state.py`
- `tools/runtime/README.md`
- `.verify/config.json`
- `tests/runtime/test_mnemo_unavailable_delivery.py`

`tools/verify/verify.py` is intentionally unchanged: its accounting already
accepts legal blocked rows and correctly requires the final persistence
contract result to be PASS.
