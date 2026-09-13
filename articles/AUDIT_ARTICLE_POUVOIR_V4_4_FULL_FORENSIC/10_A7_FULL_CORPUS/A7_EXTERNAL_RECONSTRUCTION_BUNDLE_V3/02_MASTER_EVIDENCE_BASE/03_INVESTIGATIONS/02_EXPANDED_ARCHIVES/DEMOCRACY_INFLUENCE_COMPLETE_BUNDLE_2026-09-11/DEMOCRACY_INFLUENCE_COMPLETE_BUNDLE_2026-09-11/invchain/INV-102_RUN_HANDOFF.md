---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-102-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-10"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-102"
truth_engine: "NOT_RUN_BY_DESIGN"
renard: "NO"
reclass_impact: "INV-133"
---

<!-- DERIVED_FROM: synthesis=INV-102_SYNTHESIS.md; input_gate=INV-102_SYNTHESIS_INPUT_GATE.md -->
<!-- DECISION: truth_engine=NOT_RUN_BY_DESIGN; synthesis=PASS; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-102

```text
INV_ID = INV-102
TE_STATUS = NOT_RUN_BY_DESIGN / type=SYNTHESIS
SYNTHESIS_PATH = INV-102_SYNTHESIS.md
INPUT_GATE = PASS / 5 of 5 canonical terminal handoffs
P0 = 0
P1 = 0
P2 = 4
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

Le corpus établit des contraintes et distorsions hétérogènes du choix — filtres amont, vote-buying/clientélisme, fraude/erreur et annulation institutionnelle — mais ne démontre ni leur coordination ni une absence générale de choix réel. Les mécanismes ont des dénominateurs et chaînes causales distincts. Abstention et vote stratégique ne sont pas directement couverts par les dépendances et restent explicitement non résolus.

## Highest supported edge

`mécanisme borné -> contrainte/irrégularité/neutralisation institutionnelle = SUPPORTED case-specifically` ; `ensemble -> absence générale de choix réel / illégitimité causale = NOT_ESTABLISHED`.

## Material gaps / contradictions

- abstention et vote stratégique hors couverture directe ;
- dénominateurs non comparables ;
- aucune coordination transversale ;
- aucune mesure causale commune du « choix réel » ou de la légitimité.

## RENARD

`NO` — upgrade par investigations dédiées et designs causaux/dénominateurs, pas par recherche générique.

## Route

`INV-102 BACKLOG -> CLOSED`; `truth_engine=NOT_RUN_BY_DESIGN`; `renard=NO`; `result_path=INV-102_RUN_HANDOFF.md`. Feed bounded result to `INV-133`.
