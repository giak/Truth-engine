---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "INV-133-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-133"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-133 -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+current_synthesis_selection_gate+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — INV-133

```text
SUBJECT = Synthèse systémique finale : pluralisme, captures sectorielles, réseaux, émergence, coordinations et architecture de pouvoir — départager les modèles concurrents
OBJECT_QUESTION = Quel modèle explique le mieux l’ensemble du corpus : pluralisme concurrentiel, captures sectorielles, réseaux d’accès, émergence sans chef, coordinations ponctuelles ou architecture de pouvoir plus intégrée, et quelles prédictions discriminantes restent compatibles avec les faits ?
SCOPE = Synthèse terminale stricte des synthèses/dépendances déclarées lorsqu’elles sont CLOSED. Aucun Truth Engine ni collecte générique. Comparer les modèles sur les mêmes arêtes : ressource -> capacité -> accès -> action -> exposition -> persuasion/comportement -> décision/impact, avec contrôles tasking, coordination, coercition, clandestinité, dépendance et symétrie allié/adversaire/domestique. Ne pas conclure à un centre de commandement à partir d’effets cumulés ou d’isomorphismes.
MODE = SYNTHESIS
COVERAGE = PARTIAL
CORPUS_REFS = NONE
DEPENDENCIES = INV-038;INV-040;INV-052;INV-068;INV-082;INV-088;INV-095;INV-102;INV-104;INV-129;INV-144;INV-146
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
INV-038 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-038_RUN_HANDOFF.md
INV-040 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-040_RUN_HANDOFF.md
INV-052 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-052_RUN_HANDOFF.md
INV-068 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-068_RUN_HANDOFF.md
INV-082 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-082_RUN_HANDOFF.md
INV-088 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-088_RUN_HANDOFF.md
INV-095 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-095_RUN_HANDOFF.md
INV-102 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-102_RUN_HANDOFF.md
INV-104 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-104_RUN_HANDOFF.md
INV-129 | status=CLOSED | truth_engine=NOT_RUN | result=INV-129_RUN_HANDOFF.md
INV-144 | status=CLOSED | truth_engine=NOT_RUN_BY_DESIGN | result=INV-144_RUN_HANDOFF.md
INV-146 | status=CLOSED | truth_engine=NOT_RUN | result=INV-146_RUN_HANDOFF.md
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
