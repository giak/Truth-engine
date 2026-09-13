---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-088-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-10"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-088"
truth_engine: "NOT_RUN_BY_DESIGN"
renard: "NO"
reclass_impact: "INV-133"
---

<!-- DERIVED_FROM: synthesis=INV-088_SYNTHESIS.md; input_gate=INV-088_SYNTHESIS_INPUT_GATE.md -->
<!-- DECISION: truth_engine=NOT_RUN_BY_DESIGN; synthesis=PASS; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-088

```text
INV_ID = INV-088
TE_STATUS = NOT_RUN_BY_DESIGN / type=SYNTHESIS
SYNTHESIS_PATH = INV-088_SYNTHESIS.md
INPUT_GATE = PASS / 5 of 5 canonical terminal handoffs
P0 = 0
P1 = 0
P2 = 4
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

Certification/financement, signalement prioritaire, décisions de plateforme et systèmes de recommandation forment une infrastructure distribuée qui structure réellement capacité, ordre de traitement, visibilité et exposition. Les autorités restent séparées : certification/financement ne vaut pas commandement, trusted flagger ne vaut pas ordre de retrait, décision plateforme ne vaut pas décision étatique. La chaîne jusqu’à l’exposition est matériellement documentée et l’effet attitudinal est contingent ; tasking étatique transversal, biais partisan systémique, censure coordonnée et effet électoral général restent `NOT_ESTABLISHED`.

## Highest supported edge

`règle/acteur intermédiaire -> traitement/décision de visibilité -> exposition = SUPPORTED` ; `exposition -> attitude = MIXED/CONTINGENT` ; `-> résultat électoral = NOT_ESTABLISHED generally`.

## Material gaps / contradictions

- attribution décisionnelle multi-acteurs incomplète ;
- absence de dénominateur politiquement typé commun ;
- tasking étatique/funder transversal non établi ;
- effet électoral causal non établi.

## RENARD

`NO` — upgrade seulement par logs décisionnels, dataset décision/recours typé politiquement, tasking authentifié ou design causal aval.

## Route

`INV-088 BACKLOG -> CLOSED`; `truth_engine=NOT_RUN_BY_DESIGN`; `renard=NO`; `result_path=INV-088_RUN_HANDOFF.md`. Feed bounded result to `INV-133`.
