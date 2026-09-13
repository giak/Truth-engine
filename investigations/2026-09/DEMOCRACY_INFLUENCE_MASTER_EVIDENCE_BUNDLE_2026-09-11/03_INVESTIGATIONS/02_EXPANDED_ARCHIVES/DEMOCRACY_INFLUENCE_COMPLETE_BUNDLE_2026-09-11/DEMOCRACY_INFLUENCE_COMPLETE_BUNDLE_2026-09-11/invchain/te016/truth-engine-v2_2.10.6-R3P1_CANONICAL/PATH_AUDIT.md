# Truth Engine 2.10.6 / R3 P1 — path & package audit

- KERNEL/static authority graph: **PASS**.
- Runtime/config critical paths: **PASS**.
- Six-file investigation topology and sole `run_state.py paths` ownership: **UNCHANGED**.
- Generated-cache/run contamination: **removed**.
- Auxiliary fact tools/full legacy Sublimator: **EXTERNAL_BY_DESIGN**, not reimplemented.

`/Truth Engine/CANONICAL/` is the logical repo root for relative paths. Execute from the complete ZIP, not flattened Library files.


R3 P1 verifier portability replay: **PASS**. Git repository presence is non-blocking; no-Git STATE_ID uses filesystem fallback; naive run filename timestamps no longer depend on process timezone. No path/topology change.
