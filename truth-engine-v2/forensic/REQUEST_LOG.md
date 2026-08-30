# REQUEST LOG v2.10.6 — Research and investigation trace

The log is an audit trail, not a transcript dump. Record every material call that affected scope, evidence, contradiction, memory, checkpoint, final save or writeback; collapse exact duplicate/no-op calls without hiding failures.

## Canonical rows

Two namespaces, two meanings. Never mix them.

```text
SYS-001 | SYS | {observed result/status} | {tool/module|—} | {URL/INPUT_REF|—} | {exact lifecycle/tool call}
QRY-001 | {WEB|FETCH|EXA|equivalent retrieval} | {observed result/status} | {SRC-ID|—} | {specific URL|—} | {exact research query/tool call}
```

Rules:

- `SYS-###` is for memory, module reads, filesystem/checkpoint/final writes, hashing, gate calls and other lifecycle/internal operations.
- `QRY-###` is reserved for actual evidence discovery/retrieval/refutation operations. A `SYS` call is NEVER assigned a QRY-ID.
- SYS and QRY sequences are independently contiguous from `001`; they never share a counter.
- `QUERY_TARGET` is an advisory discovery/refutation planning hint only; it is never serialized as `query target/actual`, never a gate and never a quota.
- `SEARCH_ACTIVITY_V1` may report observed activity as `WEB:n | FETCH:n | EXA:n`; values are derived from QRY modes only. SYS rows never contribute.
- Every material QRY cross-references affected LED/CLM/AXS IDs where applicable; changed research text receives a new QRY-ID.
- One accepted evidence object per QRY result row. A discovery yielding several material objects may allocate several QRY rows only when distinct retrievals/results were actually observed.
- Result states: `FOUND`, `NO_RESULT:{perimeter}`, `FAILED:{reason}`, `SKIPPED:{reason}`, `CHECKPOINTED:SEQ-{n}`, `PENDING_AT_SERIALIZATION`.
- Evidence QRY rows require `SRC-ID`, exact locator and a specific URL or validated INPUT_REF when an evidence object is accepted. Internal SYS calls and failures may use `—`.
- Keep excerpts bounded; preserve exact quotations only when analytically necessary.
- Do not invent tool success, calls, source access or IDs.

## Required lifecycle rows

1. `@READ_INV` and validation result when RESUME is used → `SYS-###`.
2. `@MNEMO_Q` and result/degraded status once per RUN_ID → `SYS-###`; RESUME does not duplicate a proven completed call.
3. Material `@WEB`, `@FETCH`, `@EXA` calls, including failures/fallbacks → `QRY-###`.
4. Initial source load plus INPUT_REF/reopenability; on RESUME, source reopen or excerpt-only ACCESS result.
5. Complete-source segmentation/lead-coverage result for a substantive DOCUMENT.
6. Decisive reopening, contradiction, provenance-audit and object-investigation calls.
7. Every axis terminalization: AXS-ID, ATTEMPT_IDS, sought object/repository, observed outcome and perimeter.
8. Prior RUN_STATE checkpoint operations as `SYS-###` rows with `CHECKPOINTED:SEQ-{n}` or `FAILED:{reason}` once their outcome is observed.
9. Initial `SERIAL_FINAL` records `MNEMO_ROW:=PENDING_PRE_GATE`, `SELF_WRITE_ROW:=PENDING_AT_SERIALIZATION`, `WRITEBACK_ROW:=PENDING_PRE_GATE`; no Mnemo side effect exists yet.
10. After PRE_GATE PASS, record observed `@MNEMO_S` and per-FCT FACT_WRITEBACK outcomes during 19b; REBIND may serialize only KERNEL `PERSISTENCE_META` values.
11. DELIVERY gate verdict/state_id remain runtime-only in `.verify/result.json` and user-visible delivery; never serialize them into the investigation.

RUN_STATE checkpoint success is observed from the deterministic helper; `CHECKPOINT_SEQ` counts successful atomic state checkpoints only. The investigation Markdown is never an OPEN checkpoint. `@MNEMO_S` and FACT_WRITEBACK occur only after PRE_GATE PASS. They may be reflected only by the same-path 19b REBIND in persistence metadata; semantic investigation content is frozen.

## Header and footer

```text
ENGINE:2.10.6 | MANIFEST:{OPEN|FINAL} | RUN_ID:{id} | PARENT_RUN_ID:{id|NONE|UNKNOWN} | AS_OF:{date} | INPUT_KIND:{kind} | MISSION_MODE:{mode} | INPUT_REF:{ref}
CHECKPOINT_SEQ:{n} | LAST_COMPLETED:{step/batch} | NEXT_ACTION:{action|NONE} | RESUME_COUNT:{n}
Investigation:{subject} | complexity:{$CX_SCORE→$CX} | route overrides:{list|NONE} | scope:{period,geo}
modules:{loaded modules}
degraded:{flags|NONE} | SEARCH_ACTIVITY_V1:WEB:{n}|FETCH:{n}|EXA:{n}  # optional; derived from REQUEST_LOG

COUNT: ◈{n} ◉{n} ○{n} | unique evidence objects:{n} | upstream families:{n-derived-from-source-registry}
LEADS:terminal {n}/{n} | AXES:terminal {n}/{applicable n} | N/A:{AXS-IDs+reason}
FAILURES:{n} | FALLBACKS:{n} | unresolved gaps:{GAP_TYPE:list}
```

Syndicated copies and analyses sharing one upstream evidence object count as one provenance family for independence.

_Canonical authority: REQUEST_LOG format and serialization boundary._


## SYS minimum audit — 2.10.6

Canonical calls: `MNEMO_Q` (explicit, exactly once per RUN_ID), `MEMORY_PROBE` or `HYDRATE` (runtime-owned routing trace), and `PERSIST_REBIND` at delivery (runtime-owned). These are SYS rows, never QRY rows. `link-query-source` repairs only existing truthful FETCH/SRC linkage and does not create evidence.
