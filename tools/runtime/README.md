# Truth Engine runtime 2.10.6 — bundle R2A.1

Deterministic mechanics only. KERNEL owns semantics.

## Canonical run directory

First derive paths, never hand-build them:

```bash
python3 tools/runtime/run_state.py paths --run-id "$RUN_ID" --as-of "$AS_OF" --subject-slug "$SLUG"
python3 tools/runtime/run_state.py init --state "$CANONICAL_RUN_STATE" ...
```

All artifacts share one RUN_DIR/prefix:

- `_INPUT.<ext>` exact supplied input archive
- `_RUN_STATE.json` OPEN/FINAL IR
- `_NARRATIVE.tmp.md` frozen narrative
- `_MNEMO_SNAPSHOT.json` compact routing memory
- `_INVESTIGATION.md` sole delivered investigation content
- `_CERTIFICATION.json` immutable copy of successful delivery result

`archive-input` must run before Mnemo search. It sets `SUBJECT_FINGERPRINT` V2, byte-exact `INPUT_SHA256`, legacy V1 bridge metadata and archived `INPUT_REF`. V2 normalizes only typographic variants (apostrophes/quotes/dashes/NBSP/ellipsis); it does not lowercase, strip accents, remove emoji or use semantic similarity. Same typographic content has the same fingerprint even if the LLM chooses another slug.

## Memory

Search Mnemo for exact `snapshot:v1 + subject-fp:<hex>`.

- found: save JSON to canonical snapshot path and `hydrate --memory-id ...`; then record DELTA rows; reuse snapshot fact keys exactly.
- not found: `memory-probe --status NONE`.
- legacy snapshot without `subject_fingerprint` is warm-route only, never exact HYDRATE.

## Mutation rules

- source family argument is bare `A|B|C|D|E|other:stable-token`, never `fam:A`.
- semantic objects use `record-object` / `update-object`; postconditions may use `assert-counts`.
- all non-derived report sections must be explicitly populated with content or `[]`; `NOT_INITIALIZED` blocks FINAL. Runtime-derived sections cannot be manually set.
- a refutation query must start with `REFUTATION`, echo a stable subject anchor and all numeric discriminators, and have an executed non-failure result.
- terminal GAP/UNKNOWN/UNRESOLVED semantic objects require a specific `gap_type` and a non-empty `gap`, `reason` or `question`.
- narrative prose cannot contain `QRY-###`; cite stable `FCT-###`/`SRC-###` identifiers. Renderer-owned narrative markers let the verifier enforce this boundary.
- `set-persistence` accepts exactly one of `--json`, `--json-file`, `--stdin`.
- write narrative through `write-narrative`; render/export use canonical paths by default and reject alternate paths.

`set-run`, `set-section`, `append-section`, `record-object`, `update-object`, `update-fact`, `update-sys` and `set-persistence` accept the documented JSON input modes. `update-fact`/`update-sys` are controlled pre-persistence repairs: if invoked on FINAL they reopen the run, clear gates, archive materialized outputs and append an auditable repair SYS row. After persistence, create an UPDATE run instead.

`init --force` archives the entire prior generation under `_replay_backups/` before creating a fresh state. It removes canonical narrative, snapshot, investigation and certification files so reallocated IDs cannot coexist with stale output.

## Final sequence

```text
write-narrative
mark-final
validate --phase pre
render --phase pre
verify.py gate --kernel-contract pre
Mnemo investigation + fact writeback
set-persistence
export-snapshot   # POST-REBIND only; rejects eligible facts whose mem is still "-"
render --phase delivery
verify.py gate --kernel-contract delivery
archive-certification
stamp DELIVERY_PASS
```

PRE/DELIVERY finalization additionally requires all five ALWAYS LOAD modules recorded in `loaded_modules`.

### 2.10.6 persistence invariant

`set-persistence` MUST bind current fact memory ids before `export-snapshot`. DELIVERY validation rejects a missing snapshot, any eligible fact without a current memory id, or any snapshot/RUN_STATE memory-id mismatch. Source family tokens use one exact ABI end-to-end: `A|B|C|D|E|other:stable-token`.
Every `set-persistence` call is retained in `attempt_history` and rendered in `WRITEBACK_ATTEMPT_LOG_V1`; a later PASS does not erase an earlier FAIL/PARTIAL. DELIVERY requires the last attempt and the last corresponding `SYS PERSIST_REBIND` row to be PASS.

### 2.10.6 fingerprint migration invariant

Lookup order is V2 first. If absent, one compatibility lookup may target `subject_fingerprint_legacy_v1`; `hydrate` accepts that path only for an engine 2.10.4 snapshot whose fingerprint equals the current legacy V1. New snapshots are always V2. `INPUT_SHA256` remains a byte-exact archive hash. FINAL rejects unresolved `original_input_ref`.


### 2.10.6 state-authority invariant

- Never edit `_RUN_STATE.json` directly. If a FETCH was recorded before its already-existing source, repair it only with `link-query-source --qry QRY-### --src SRC-###`; runtime requires an unlinked successful FETCH and exact QRY/SRC URL identity.
- `set-persistence` is strict-schema: unknown keys, malformed execution rows, invalid memory maps, and mutable `self_write_row` are rejected.
- Before PRE, exactly one explicit `SYS ... MNEMO_Q` row and at least one runtime-owned memory-route SYS row (`MEMORY_PROBE` or `HYDRATE`) are required. DELIVERY additionally requires runtime-owned `PERSIST_REBIND`.
- FINAL snapshots contain no `NOT_INITIALIZED`; absent contradiction material serializes as `[]`.
- `origin_memory_id` identifies a prior fact memory, never the enclosing snapshot memory id.
