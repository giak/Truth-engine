---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "INV-038-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-038"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-038 -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+current_synthesis_selection_gate+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — INV-038

```text
SUBJECT = Maroc et Algérie : influence politique, diplomatique et diasporique en France — séparer les deux États dans l’enquête
OBJECT_QUESTION = Quels mécanismes d’influence marocains et algériens en France sont réellement isomorphes, où divergent-ils, et quelles preuves permettent de distinguer diplomatie/cooperation/diaspora ordinaire, influence politique, tasking, coercition ou ingérence sans fusionner les causalités des deux États ?
SCOPE = Synthèse stricte de INV-130 et INV-131 une fois CLOSED. Comparer uniquement des chaînes homologues acteur public/para-public -> intermédiaire/ressource/tasking -> action -> cible -> accès/exposition/décision -> effet. Aucun Truth Engine ni web générique. Gardes : nationalité/diaspora != lien étatique ; coopération != contrôle ; investissement != influence ; proximité != tasking ; un cas marocain != preuve sur l’Algérie et inversement.
MODE = SYNTHESIS
COVERAGE = NEW
CORPUS_REFS = NONE
DEPENDENCIES = INV-130;INV-131
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
INV-130 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-130_RUN_HANDOFF.md
INV-131 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-131_RUN_HANDOFF.md
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
