# OUTPUT TEMPLATE v2.8 — Investigation

This file alone defines the delivered investigation structure and filename. Gates live in `forensic/GATES.md`; statuses in `definitions/SYMBOLS.md`; save order in KERNEL.

The delivered investigation starts with the compact FINAL RUN_MANIFEST: engine/run/parent IDs, AS_OF, INPUT_KIND, MISSION_MODE, INPUT_REF, subject/path, scope, complexity, successful-OPEN checkpoint count, progress/resume count, route overrides, loaded modules and degraded flags. `NEXT_ACTION=NONE`; no required field remains `PENDING`.

KERNEL-owned `STATE:OPEN` checkpoint snapshots use this same path but are not delivered output and do not follow the core-section structure below.

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
- Emit the machine-readable `FACT_REGISTRY_V1` block in `CARTE DES PREUVES` when the investigation writes facts to Mnemolite (write-back ✦/L4 or ✧/L1-L3). One row per fact, 9 fields separated by ` | `: `id | epi | tier | url | familles | date | sujet | valeur | mem`. `epi` is text (`FACT|EVIDENCE|INFERENCE|HYPOTHESIS|SPECULATION|UNKNOWN`); `tier` is a glyph restricted to {✦,✧,⁅,❧}. The SYMBOLS.md epistemic status glyphs `⁕`(CLAIMED), `⁂`(SPECULATED), `⊗`(CONTRADICTED), `⊙`(PARTIAL) never enter the `tier` column: express them as EPI text (⁕→UNKNOWN, ⁂→HYPOTHESIS). `mem` carries the Mnemolite memory_id of each written fact (`status:CONFIRME` ✦ or `status:VERIFIE` ✧), read verbatim downstream; `-` for non-written facts (⁅/❧). A run with zero written facts (✦/✧) performs no write-back and the block is optional.
- Required but unsupported content after bounded applicable search is `UNKNOWN` or `NONE ESTABLISHED`; logical irrelevance is `NOT APPLICABLE`; always give GAP_TYPE/reason.
- Preserve material contradictions; do not smooth them into a synthetic verdict.
- Include formula inputs when a score/metric is reported; otherwise `NOT COMPUTABLE`.
- Include TRACE_MATRIX and CONTRADICTION_LEDGER when non-empty; include STATUS_DELTA when a status changed during verification.
- Persist FINAL-write/writeback rows as `PENDING_AT_SERIALIZATION` per REQUEST_LOG.
- Step 14 produces a draft only. Step 18b rebuilds and freezes the final investigation after all corrections.

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

Always deliver exactly one complete investigation file on one path. OPEN checkpoints replace compact state on that path; exactly one write carries `STATE:FINAL`. File size does not create a second output mode. On a real FINAL serialization failure, log `FAILED:{reason}` and stop persistence; never split or truncate silently.

_Canonical authority: output structure and filename._
