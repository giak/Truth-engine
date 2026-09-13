---
project: truth-engine
engine_version: "2.10.6"
bundle_revision: "R3"
package_revision: "P1"
status: canonical
date: "2026-09-06"
---

# Truth Engine 2.10.6 / R3 — package revision P1

P1 is a bounded verifier-portability correction discovered by the real INV-022 end-to-end replay. It does not modify the R3 forensic state/output contract.

## Fixed defects

1. **Git false BLOCK** — `verify.py` previously returned `BLOCKED` when `REPO_ROOT` was not a Git repository or had no commit, contradicting the KERNEL rule that Git topology must not influence certification. P1 makes Git absence non-blocking and derives `STATE_ID` from a deterministic filesystem fallback.
2. **Timezone false FAIL** — the canonical filename contains a naive local `YYYY-MM-DD_HH-MM` timestamp but no timezone. Comparing it to `datetime.now()` made the verdict depend on the verifier process timezone. P1 validates the calendar value and rejects only a timestamp beyond the maximum possible civil offset (`UTC now + 14h`).

## Preserved invariants

- engine version remains `2.10.6`;
- bundle contract remains `R3`;
- six-file investigation topology unchanged;
- `run_state.py paths` remains the sole path generator;
- KERNEL, `run_state.py`, TEMPLATE, investigation ontology, EDI and gates semantics unchanged;
- R3 semantic/source/projection/trace checks unchanged.

## Validation

- full release suite: `140 passed, 2 skipped`;
- INV-022 DELIVERY gate from a clean extracted package with **no `.git`**: PASS;
- same replay with process `TZ` unset/default UTC: PASS;
- 24 R3 KERNEL contract checks: PASS;
- 69 QRY, 20 SRC, 26 FCT and full provenance/trace from INV-022 remain certified;
- impossible filename future beyond UTC+14: FAIL fixture.

P0 is retained as historical package metadata; P1 is the canonical package revision.
