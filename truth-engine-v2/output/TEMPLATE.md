# OUTPUT TEMPLATE v2.10.6 — Investigation

This file alone defines the delivered investigation structure and filename. Gates live in `forensic/GATES.md`; statuses in `definitions/SYMBOLS.md`; save order in KERNEL.

The delivered investigation starts with the compact FINAL RUN_MANIFEST: engine/run/parent IDs, AS_OF, INPUT_KIND, MISSION_MODE, archived INPUT_REF, subject slug/fingerprint, scope, complexity, successful-OPEN checkpoint count, progress/resume count, route overrides, loaded modules and degraded flags. `NEXT_ACTION=NONE`; no required field remains `PENDING`.

KERNEL-owned `STATE:OPEN` checkpoints live only in the companion `_RUN_STATE.json`; the investigation Markdown does not exist before phase 19.

In `MISSION_MODE=INVESTIGATION`, the dossier answers `OBJECT_QUESTION` before the bounded verdict on `LEAD_QUESTION`. The input source is audited as one branch. A fact-check, debunk or provenance chain is never the whole output unless the user explicitly selected `VERIFY_ONLY`.

## §1 Investigation levels

### SIMPLE — exactly 5 core sections

1. RÉSUMÉ EXÉCUTIF
2. CHRONOLOGIE
3. DOMAINES
4. CARTE DES PREUVES
5. PÉRIMÈTRE & LIMITES

### MEDIUM — exactly 7 core sections

1. RÉSUMÉ EXÉCUTIF
2. CHRONOLOGIE
3. DOMAINES
4. RÉSEAU D’ACTEURS
5. CHAÎNES / PELOTE
6. CARTE DES PREUVES
7. PÉRIMÈTRE & LIMITES

### COMPLEX — exactly 8 core sections

MEDIUM + `CARTE DIALECTIQUE` after `CHAÎNES / PELOTE`.

### APEX — exactly 15 core sections

| # | Section | Required content |
|---:|---|---|
| 1 | RÉSUMÉ EXÉCUTIF | bounded answer to OBJECT_QUESTION, decisive findings, distinct source/lead verdict, actors, impact, main gaps |
| 2 | MANIPULATION_REPORT | 15 scores, observations, assumptions, loaded clusters |
| 3 | CLUSTERS | inputs, diagnostic result, competing explanation, gap |
| 4 | HERMÉNEUTIQUE | L1–L6, facts separated from inference |
| 5 | FORENSIC REASONING | shown/omitted/reconstruction or NOT APPLICABLE |
| 6 | PRISME DIALECTIQUE | dominant, strongest critical, evidence arbitration |
| 7 | CHRONOLOGIE | sourced relevant events; no forced count |
| 8 | DOMAINES | findings by applicable investigation axis and cross-domain boundaries |
| 9 | RÉSEAU D’ACTEURS | typed sourced entity edges plus applicable control map; centrality only if computed |
| 10 | CHAÎNES / PELOTE | underlying-object mechanisms, typed causal links, alternatives, coverage and gaps |
| 11 | CARTE DES PREUVES | LEAD/INVESTIGATION/CLAIM/FACT registries, TRACE_MATRIX, contradictions, EDI |
| 12 | CARTE DIALECTIQUE | scenarios, tensions, impact and responsibility map |
| 13 | PÉRIMÈTRE & LIMITES | inclusions, exclusions, access/method limits |
| 14 | ÉTAT DES CONNAISSANCES | known/probable/claimed/hypotheses/contested/unknown/refuted |
| 15 | SUSPICION / VÉRIFICATION | source audits, status delta, unresolved checks |

`SOURCES` and `REQUEST_LOG` are mandatory appendices for every factual investigation and do not change the core section count. `UPDATE` additionally includes `DELTA_REPORT`; the core count remains unchanged.

## §2 Content and trace rules

- French output, dense and factual; one sentence = one bounded claim.
- Lead with the underlying-object investigation finding. Put `AUDIT DU LEAD/SOURCE` in a distinct subsection; never let it consume `DOMAINES`, `RÉSEAU`, `CHAÎNES` or `IMPACT` when those concern a broader object.
- Include compact `LEAD_COVERAGE`, `OBJECT_COVERAGE` and `INVESTIGATION_MAP` tables inside `CARTE DES PREUVES` for every level; these do not change the core section count.
- Every material input chapter/topic/time/logical block resolves to a SATURATED/GAP/EXCLUDED LED-ID; exclusions are exclusive and reasoned. Preserve SOURCE_ID/locator and materially self-contained exact excerpts for supplied DECISIVE/IMPORTANT leads not otherwise quoted.
- Every applicable AXS-ID displays ATTEMPT_IDS and result IDs or an auditable typed GAP; a bare GAP is invalid.
- `RESOURCE_FLOW_MAP`, `ACTOR_NETWORK_MAP` and `CONTROL_MAP` appear when their axes are applicable; absence of evidence is a visible GAP, not silent omission.
- A PELOTE of the source/statistic genealogy is labeled `SOURCE_PROVENANCE`; it cannot replace `OBJECT_CAUSALITY` unless provenance is the explicit OBJECT_QUESTION.
- Put specific clickable citations next to material claims when available. `✦` resolves to SRC-ID, exact locator and URL/validated INPUT_REF; a persisted exact excerpt substitutes only for the bounded fact that supplied content states X.
- Display canonical status for facts, causal links and responsibility claims.
- Emit `FACT_REGISTRY_V1` in `CARTE DES PREUVES` for every referenced FCT, whether written to MnemoLite or not. One row per fact, 9 fields separated by ` | `: `id | epi | tier | url | familles | date | sujet | valeur | mem`. `epi` is text (`FACT|EVIDENCE|INFERENCE|HYPOTHESIS|SPECULATION|UNKNOWN`); `tier` is restricted to {✦,✧,⁅,❧}. Narrative status glyphs `⁕⁂⊗⊙` never enter `tier`. `mem` carries the returned MnemoLite memory_id only after 19b rebind for written `EPI=FACT` rows (`✦`→CONFIRME, `✧`→VERIFIE); `-` otherwise.
- When `FACT_REGISTRY_V1` is present, emit `FCT_SOURCE_MAP_V1` with exactly one row per FCT: `FCT-### | SRC-###,SRC-###` or `FCT-### | -` for unsupported ⁅/❧. The map contains support-only SRCs; `families` in FACT_REGISTRY is derived from their explicit `fam:` values, never hand-counted.
- Required but unsupported content after bounded applicable search is `UNKNOWN` or `NONE ESTABLISHED`; logical irrelevance is `NOT APPLICABLE`; always give GAP_TYPE/reason.
- Preserve material contradictions; do not smooth them into a synthetic verdict.
- Include formula inputs when a score/metric is reported; otherwise `NOT COMPUTABLE`.
- Include TRACE_MATRIX and CONTRADICTION_LEDGER when non-empty; include STATUS_DELTA when a status changed during verification.
- Initial SERIAL_FINAL persists `MNEMO_ROW:PENDING_PRE_GATE`, `SELF_WRITE_ROW:PENDING_AT_SERIALIZATION`, `WRITEBACK_ROW:PENDING_PRE_GATE`, `WRITEBACK_EXECUTION_V1:[]` and `mem:-`. Only 19b REBIND may serialize observed Mnemo/writeback persistence metadata. RUN_STATE stores `writeback_row` as a structured JSON object; renderer alone emits canonical `{eligible:N;attempted:N;success:N;failure:N;blocked:N}`. REBIND keeps `SELF_WRITE_ROW:PENDING_AT_SERIALIZATION`, emits `WRITEBACK_EXECUTION_V1`, `MEMORY_WRITE_MODE_V1`, structured `WRITEBACK_ROW` and returned `mem` IDs; PRE_GATE/GATE verdicts and STATE_ID remain external.
- Step 14 produces a draft only. Step 18b rebuilds and freezes the final investigation after all corrections.

## §2.5 Canonical machine serialization contract


### Semantic IR serialization (runtime-owned)

Before `REQUEST_LOG`, renderer emits exactly one `SEMANTIC_COUNTS_V1` row and six runtime-owned registries:

```text
SEMANTIC_COUNTS_V1:LED:N|CLM:N|AXS:N|CAU:N|CTRL:N|ACT:N

## SEMANTIC_REGISTRIES_V1
### LEAD_REGISTRY_V1
LED-001 | {canonical JSON payload}
### CLAIM_REGISTRY_V1
CLM-001 | {canonical JSON payload}
### AXIS_REGISTRY_V1
AXS-001 | {canonical JSON payload}
### CAUSALITY_REGISTRY_V1
CAU-001 | {canonical JSON payload}
### CONTROL_REGISTRY_V1
CTRL-001 | {canonical JSON payload}
### ACTION_REGISTRY_V1
ACT-001 | {canonical JSON payload}
```

These rows are generated only from RUN_STATE. Narrative prose may explain them but MUST NOT duplicate these registry headings. The deterministic gate reconciles declared counts with rendered row counts and required non-empty registries.

This subsection is the **single formatting authority** for machine-readable rows consumed by the deterministic gate. In v2.10 the deterministic runtime renderer emits these shapes from RUN_STATE; the LLM must not hand-count or hand-format them. `verify.py` validates them but does not define alternate hidden syntax.

### SERIAL_FINAL / PRE_GATE shapes

```text
## REQUEST_LOG
QRY-001 | WEB | FOUND | - | -
QRY-002 | FETCH | FOUND | SRC-001 | https://example.org/evidence
QRY-003 | FETCH | FOUND | SRC-002 | https://example.net/corroboration
QRY-004 | WEB | NO_RESULT:bounded-refutation | - | -

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://example.org/evidence
SRC-002 | ◉ | fam:D | https://example.net/corroboration

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://example.org/evidence | A,D | 2026-08-27 | subject-key | bounded-value | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-004 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME

PERSISTENCE_META: MNEMO_ROW:PENDING_PRE_GATE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:PENDING_PRE_GATE | WRITEBACK_EXECUTION_V1:[]
```

Rules: QRY rows have exactly the five canonical fields shown; accepted web evidence gets numeric `SRC-###`; each SRC row has exactly one role glyph, explicit `fam:` and at most one URL; one FCT row = exactly 9 fields; one FCT_SOURCE_MAP/REFUTATION/WRITEBACK_PLAN row per applicable FCT. `mem` is `-` before PRE_GATE.

### REBIND_FINAL / DELIVERY additions

```text
PERSISTENCE_META: MNEMO_ROW:<actual-id-or-failure> | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:1;attempted:1;success:1;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[1 row, see section]

<!-- same FACT_REGISTRY_V1 row, only mem changes -->
FCT-001 | FACT | ✦ | https://example.org/evidence | A,D | 2026-08-27 | subject-key | bounded-value | <returned-memory-id>

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
```

Only KERNEL `PERSISTENCE_META` may change between SERIAL_FINAL and REBIND_FINAL. `SELF_WRITE_ROW` never becomes DONE. Gate verdicts/state IDs stay external in `.verify/result.json`.

### Optional activity counter

If activity is displayed, use only:

```text
SEARCH_ACTIVITY_V1:WEB:14|FETCH:25|EXA:0
```

Counts are derived from REQUEST_LOG modes. Do **not** serialize `query target/actual`; QUERY_TARGET is a non-binding planning hint and does not measure completeness.

## §3 TL;DR

```text
SUJET: {scope}
OBJET: {strongest bounded underlying-object finding + status + LED/AXS/FCT IDs}
SOURCE: {bounded lead/source verdict + CLM/FCT IDs}
MANIPULATION/STRUCTURE: {main diagnostic, explicitly non-verdict}
LIMITE: {largest unresolved GAP_TYPE}
```

## §4 Filename

```text
YYYY-MM-DD_HH-MM_{SUBJECT_SLUG}_INVESTIGATION.md
```

Always deliver exactly one investigation content file (`_INVESTIGATION.md`) inside one canonical run directory. The same directory also retains `_INPUT.*`, `_RUN_STATE.json`, `_NARRATIVE.tmp.md`, `_MNEMO_SNAPSHOT.json`, and `_CERTIFICATION.json` as forensic support artifacts. OPEN checkpoints update only `_RUN_STATE.json`; phase 19 creates the first FINAL investigation Markdown and 19b may deterministically re-render the same path for persistence metadata only. File size does not create a second output mode.

_Canonical authority: output structure and filename._
