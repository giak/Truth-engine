---
project: truth-engine
investigation: INV-022
run_id: 20260906-1057-russie-operations-influence-france
engine_version: "2.10.6"
bundle_revision: "R3"
package_revision: "P0"
artifact_type: full_forensic_investigation_bundle
status: complete
---

# INV-022 — Full forensic bundle

This bundle contains everything retained for the INV-022 R3 end-to-end investigation test, while excluding unrelated repository/cache material.

## CANONICAL_RUN
The six canonical co-located investigation artifacts produced by the pipeline:
- `_INPUT.txt`
- `_RUN_STATE.json`
- `_NARRATIVE.tmp.md`
- `_INVESTIGATION.md`
- `_MNEMO_SNAPSHOT.json`
- `_CERTIFICATION.json`

## VERIFICATION
Delivery gate state/results from `.verify` plus the preserved delivery-result copy.

## E2E
The end-to-end test report, including the Git-blocker and timezone findings encountered before the successful final delivery gate.

## WORKING_TRACE
Files created specifically to continue and terminalize this investigation during the R3 test. These are execution traces/helpers, not canonical investigation artifacts.

## ENGINE_CONTRACT_SNAPSHOT
Minimal exact contract/runtime files used to execute and certify this run:
- `KERNEL.md`
- `output/TEMPLATE.md`
- `protocol/INVESTIGATION.md`
- `search/EPISTEMIC.md`
- `forensic/GATES.md`
- `tools/runtime/run_state.py`
- `tools/verify/verify.py`

## Explicit exclusions
Not included because they are not investigation-specific:
- full Truth Engine repository/package outside the contract snapshot;
- temporary `.git` repository created only to expose/work around the verifier Git-blocker;
- `.pytest_cache`, `__pycache__`, compiled bytecode;
- generic tests and unrelated documentation.

`SHA256SUMS.txt` covers every file in this bundle except itself.
