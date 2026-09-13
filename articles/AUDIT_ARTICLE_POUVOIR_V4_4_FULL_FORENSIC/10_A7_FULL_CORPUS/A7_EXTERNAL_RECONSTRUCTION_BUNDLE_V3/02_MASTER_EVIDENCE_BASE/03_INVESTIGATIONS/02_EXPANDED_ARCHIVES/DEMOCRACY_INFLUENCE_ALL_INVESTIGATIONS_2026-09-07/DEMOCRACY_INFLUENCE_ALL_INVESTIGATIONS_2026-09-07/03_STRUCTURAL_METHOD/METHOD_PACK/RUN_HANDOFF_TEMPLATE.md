# RUN_HANDOFF — template

> Sidecar after Truth Engine FINAL. Do not duplicate internal QRY/SRC/FCT registries; reference IDs/path.

| Field | Value |
|---|---|
| INV_ID | |
| TE_STATUS | FINAL / BLOCKED / DEGRADED |
| TE_RESULT_PATH | |
| SUBJECT | |
| OBJECT_QUESTION | |
| EXECUTION_MODE | |
| CORPUS_INHERIT | CONTEXT_ONLY / LEAD_RECHECK / SOURCE_LEAD / CONTRADICTION_LEAD / GAP_LEAD summary |
| CENTRAL_CLAIM_DELTA | What became stronger/weaker/refuted/open? |
| MATERIAL_GAPS | |
| CONTRADICTIONS_RESIDUALS | |
| CAUSAL_LEVEL_REACHED | P0..P7 / N/A, with bounded description |
| IMPACT_LEVEL_REACHED | ATTEMPT..COUNTERFACTUAL_OUTCOME / NONE_ESTABLISHED / UNKNOWN |
| RENARD_DECISION | REQUIRED / NO |
| RENARD_REASON | |
| NEXT_RECOMMENDATION | |

## System models delta

| Model | Delta | Why |
|---|---|---|
| M0 PLURALISM | STRENGTHENS / WEAKENS / NEUTRAL / N/A | |
| M1 SECTOR_CAPTURE | | |
| M2 TRANSVERSAL_NETWORK | | |
| M3 EMERGENT_ALIGNMENT | | |
| M4 DOCUMENTED_COORDINATION | | |
| M5 COHERENT_ARCHITECTURE | | |

## New ideas — mandatory triage

| Idea | Trigger | Utility | Coverage | Materiality | Relation | Decision | Parent/Merge | Evidence lead | Why model-change |
|---|---|---|---|---|---|---|---|---|---|
| NONE | N/A | N/A | N/A | N/A | N/A | DROP | N/A | N/A | No material new branch |

## Registry patch

```text
status :=
truth_engine :=
result_path :=
renard :=
renard_reason :=
next_action :=
new_INV_rows := NONE|IDs
```
