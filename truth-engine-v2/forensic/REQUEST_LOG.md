# REQUEST LOG v2.1 — Research and tool trace

The log is an audit trail, not a transcript dump. Record every material call that affected scope, evidence, contradiction, save or writeback; collapse exact duplicate/no-op calls without hiding failures.

## Canonical table

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL |
|---:|---|---|---|---|---|
| 1 | SYS/◈/◉/○ | exact query or alias | concise result/status | source or tool | specific URL or `—` |

Rules:

- Sequential numbering across the run; optional branch headings do not reset it.
- `TYPE` is `SYS` for memory/write calls; evidence roles `◈◉○` are claim-relative per SYMBOLS.md.
- One accepted source per result row. A search returning several material sources may occupy several rows.
- Result states: `FOUND`, `NO_RESULT`, `FAILED:{reason}`, `SKIPPED:{reason}`, `PENDING_AT_SERIALIZATION`.
- Evidence rows require the exact page/document URL. Internal calls and failures use `—`.
- Keep result excerpts short and paraphrased; preserve exact quotations only when analytically necessary.
- Cross-reference material claims to fact/source IDs, not necessarily every query number.

## Required lifecycle rows

1. `@MNEMO_Q` and result/degraded status.
2. Material `@WEB`, `@FETCH`, `@EXA` calls, including failure/fallback.
3. Decisive contradictions and source-audit calls.
4. `@MNEMO_S` result when known before file serialization.
5. Investigation write, article write and FACT_WRITEBACK as `PENDING_AT_SERIALIZATION` in the persisted file.
6. Their actual post-serialization outcomes in runtime/final delivery; never claim they already exist inside the file they create.

If `@MNEMO_S` is called with the complete pre-save investigation, its result may be inserted into the file-bound copy before `@WRITE`; the memory copy legitimately retains `PENDING_AT_SERIALIZATION` for that call.

## Header and footer

```text
Investigation:{subject} | date:{date} | complexity:{$CX_SCORE→$CX}
scope:{period,geo} | modes:{loaded modules} | query target/actual:{N/N}

COUNT: ◈{n} ◉{n} ○{n} | unique evidence objects:{n}
FAILURES:{n} | FALLBACKS:{n} | unresolved gaps:{list}
```

Syndicated copies and analyses sharing one upstream evidence object count as one provenance family for independence.

_Canonical authority: REQUEST_LOG format and serialization boundary._
