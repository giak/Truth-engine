---
project: truth-engine
engine_version: "2.10.6"
bundle_revision: "R3"
package_revision: "P0"
status: canonical
date: "2026-09-06"
---

# Truth Engine 2.10.6 / R3 — package revision P0

R3 closes a forensic output-contract gap exposed by real FINAL runs: a deterministic PASS could coexist with incomplete terminal semantic objects or material analytical state not projected into `_INVESTIGATION.md`.

## Contract changes

- `_RUN_STATE.json` remains the single canonical machine state and the six-file run topology is unchanged.
- `run_state.py` keeps sole ownership of paths and deterministic rendering.
- `_NARRATIVE.tmp.md` keeps its physical ABI name but is now a technical analytical body, not a reader-oriented report.
- `run_state.py` deterministically projects structured report sections as Markdown and keeps JSON only in runtime-owned machine registry payloads.
- FINAL semantic contracts are enforced for LED/AXS/CLM/CAU/CTRL/ACT.
- SATURATED LED/AXS require actual attempts and results.
- accepted SRC objects preserve canonical identity, publication/check dates and exact locator.
- `MANIPULATION_REPORT`, `MODULE_EXECUTION` and `EDI_REPORT` have structured FINAL contracts.
- `verify.py` independently reparses and verifies semantic completeness, source provenance, forensic projection and trace completeness.
- canonical loaded-module paths must be unique and relative; aliases such as `truth-engine-v2/...` are rejected.

## Output boundary

```text
KERNEL + KB
  -> RUN_STATE
  -> run_state.py render
  -> _INVESTIGATION.md
  -> verify.py
```

`output/TEMPLATE.md` is the projection specification only; it does not duplicate investigation or KB ontologies.

## Compatibility

Engine version remains `2.10.6`; the machine/output contract revision is `R3`. The R3 verifier only certifies the R3 bundle contract. Historical R2A.2 FINAL artifacts remain readable but are not silently recertified as R3.

## Validation

- full release suite: `136 passed, 2 skipped`;
- synthetic R3 FINAL render: PASS;
- modified `verify.py` PRE kernel contract: 24/24 deterministic checks PASS;
- adversarial fixtures reject the previously accepted incomplete AXS/SRC/projection states.

## Real-run regression proof

The previously delivered local run `2026-09-06_attribution-russie-fermetures-aeroports-europe` had been deterministically certified under R2A.1. Under R3 it is intentionally rejected because its serialized state contains, among other issues, SATURATED AXS rows without attempts/results, legacy four-field SRC rows, non-canonical duplicated module paths, and no deterministic forensic projection/trace blocks. This proves R3 closes the observed false-PASS class rather than only satisfying synthetic fixtures.
