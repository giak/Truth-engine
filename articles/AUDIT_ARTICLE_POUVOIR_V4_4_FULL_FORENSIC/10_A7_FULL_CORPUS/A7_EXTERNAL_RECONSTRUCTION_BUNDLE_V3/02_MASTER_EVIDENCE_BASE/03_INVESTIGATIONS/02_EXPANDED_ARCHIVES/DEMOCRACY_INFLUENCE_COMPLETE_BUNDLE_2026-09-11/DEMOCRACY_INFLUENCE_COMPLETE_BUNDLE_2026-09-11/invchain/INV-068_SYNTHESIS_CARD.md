---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "INV-068-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-068"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-068 -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+current_synthesis_selection_gate+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — INV-068

```text
SUBJECT = Narrative laundering : intérêt → think tank → expert → média → décideur → apparence de consensus indépendant
OBJECT_QUESTION = Dans quelles conditions une chaîne intérêt/financeur -> think tank -> expert -> média -> décideur produit-elle une apparence de consensus indépendant, et quelles arêtes sont réellement établies entre financement, accès, reprise, coordination, tasking, persuasion et décision ?
SCOPE = Synthèse stricte des handoffs CLOSED INV-059, INV-061 à INV-067 et INV-085. Aucun Truth Engine ni web générique. Comparer ressources, droits de participation, sélection d’experts, amplification, auditions/reprises et effets. Gardes : funding != command ; expert selection != tasking ; citation/reprise != adoption ; répétition != consensus causal ; réseau != coordination.
MODE = SYNTHESIS
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A008:208733314.la-fabrique-de-la-menace-comment;A012:204169916.le-debat-qui-nexistait-pas-6-mecanismes;A025:199654938.medias-censure-et-desinformation;A072:186844276.tristan-mendes-france-la-machine;A091:181572197.lindustrie-de-linfluence-enquete
DEPENDENCIES = INV-059;INV-061;INV-062;INV-063;INV-064;INV-065;INV-066;INV-067;INV-085
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
INV-059 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-059_RUN_HANDOFF.md
INV-061 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-061_RUN_HANDOFF.md
INV-062 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-062_RUN_HANDOFF.md
INV-063 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-063_RUN_HANDOFF.md
INV-064 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-064_RUN_HANDOFF.md
INV-065 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-065_RUN_HANDOFF.md
INV-066 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-066_RUN_HANDOFF.md
INV-067 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-067_RUN_HANDOFF.md
INV-085 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-085_RUN_HANDOFF.md
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
