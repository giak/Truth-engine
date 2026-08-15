# REQUEST LOG v2.8 — Research and investigation trace

The log is an audit trail, not a transcript dump. Record every material call that affected scope, evidence, contradiction, memory, checkpoint, final save or writeback; collapse exact duplicate/no-op calls without hiding failures.

## Canonical table

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS/◈/◉/○ | exact query or alias | concise result/status | SRC-ID + title + locator, or tool | specific URL/INPUT_REF or `—` |

Rules:

- Number sequentially across the run; optional branch headings do not reset it.
- `TYPE` is `SYS` for memory/write/internal lifecycle calls; evidence roles `◈◉○` are claim-relative per SYMBOLS.md.
- Research `QUERY/TOOL_CALL` begins with its stable `QRY-ID` and cross-references affected LED/CLM/AXS IDs; changed query text receives a new ID. Every applicable AXS terminal row resolves to its QRY/SRC attempts here.
- One accepted evidence object per result row. A search yielding several material objects may occupy several rows.
- Result states: `FOUND`, `NO_RESULT:{perimeter}`, `FAILED:{reason}`, `SKIPPED:{reason}`, `CHECKPOINTED:SEQ-{n}`, `PENDING_AT_SERIALIZATION`.
- Evidence rows require `SRC-ID`, exact locator and a specific URL or validated INPUT_REF for supplied content. Internal calls and failures use `—`.
- Keep excerpts short and paraphrased; preserve exact quotations only when analytically necessary.
- Cross-reference material results to QRY/LED/CLM/AXS/FCT IDs. Do not invent tool success, calls or source access.

## Required lifecycle rows

1. `@READ_INV` and validation result when RESUME is used.
2. `@MNEMO_Q` and result/degraded status once per RUN_ID; RESUME does not duplicate a proven completed call.
3. Material `@WEB`, `@FETCH`, `@EXA` calls, including failures/fallbacks.
4. Initial source load plus INPUT_REF/reopenability; on RESUME, source reopen or excerpt-only ACCESS result.
5. Complete-source segmentation/lead-coverage result for a substantive DOCUMENT.
6. Decisive reopening, contradiction, provenance-audit and object-investigation calls.
7. Every axis terminalization: AXS-ID, ATTEMPT_IDS, sought object/repository, observed outcome and perimeter.
8. Prior checkpoint writes as `CHECKPOINTED:SEQ-{n}` or `FAILED:{reason}` once their outcome is observed.
9. `@MNEMO_S` result when known before FINAL serialization.
10. STATE:FINAL write and FACT_WRITEBACK as `PENDING_AT_SERIALIZATION` in the FINAL file.
11. Actual FINAL/writeback outcomes only in runtime/final delivery; never claim they already exist inside the file they create.

A checkpoint cannot prove its own write inside itself. Snapshot `n+1` or FINAL reconciles the observed outcome of snapshot `n`; `CHECKPOINT_SEQ` counts successful OPEN writes only. If `@MNEMO_S` is called with the complete pre-save investigation, its result may be inserted into the file-bound copy before FINAL `@WRITE`; the memory copy legitimately retains `PENDING_AT_SERIALIZATION` for that call.

## Header and footer

```text
ENGINE:2.7 | MANIFEST:{OPEN|FINAL} | RUN_ID:{id} | PARENT_RUN_ID:{id|NONE|UNKNOWN} | AS_OF:{date} | INPUT_KIND:{kind} | MISSION_MODE:{mode} | INPUT_REF:{ref}
CHECKPOINT_SEQ:{n} | LAST_COMPLETED:{step/batch} | NEXT_ACTION:{action|NONE} | RESUME_COUNT:{n}
Investigation:{subject} | complexity:{$CX_SCORE→$CX} | route overrides:{list|NONE} | scope:{period,geo}
modules:{loaded modules}
degraded:{flags|NONE} | query target/actual:{N/N}

COUNT: ◈{n} ◉{n} ○{n} | unique evidence objects:{n} | upstream families:{n}
LEADS:terminal {n}/{n} | AXES:terminal {n}/{applicable n} | N/A:{AXS-IDs+reason}
FAILURES:{n} | FALLBACKS:{n} | unresolved gaps:{GAP_TYPE:list}
```

Syndicated copies and analyses sharing one upstream evidence object count as one provenance family for independence.

_Canonical authority: REQUEST_LOG format and serialization boundary._
