---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "INV-082-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-082"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-082 -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+gate=DEPENDENCIES_DONE+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — INV-082

```text
SUBJECT = Concentration économique versus concentration éditoriale : quelle causalité peut réellement être démontrée ?
OBJECT_QUESTION = Dans quelle mesure la concentration économique et capitalistique des médias se traduit-elle réellement par une concentration éditoriale observable, par quels mécanismes documentés, et quelles preuves permettent de distinguer capacité structurelle, sélection éditoriale, intervention ou tasking, alignement émergent et contrôle causal ?
SCOPE = Synthèse stricte des dépendances fermées INV-081 et INV-085, centrée sur la France et sur les mécanismes effectivement couverts par leurs deltas terminaux. Comparer uniquement les arêtes isomorphes entre propriété/financement, capacité d'accès, sélection des sujets, autorité éditoriale et contrôle externe. Aucune nouvelle collecte web ni nouveau run Truth Engine. Gardes : economic_concentration != editorial_concentration ; ownership != editorial_command ; funding != topic_tasking ; selection_asymmetry != owner_causation ; shared_output != coordination ; reach != persuasion ; editorial_effect != electoral_effect.
MODE = SYNTHESIS
COVERAGE = PARTIAL
CORPUS_REFS = A012:204169916.le-debat-qui-nexistait-pas-6-mecanismes;A025:199654938.medias-censure-et-desinformation;A049:193809543.audiovisuel-public-anatomie-dune;A091:181572197.lindustrie-de-linfluence-enquete
DEPENDENCIES = INV-081;INV-085
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
INV-081 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-081_RUN_HANDOFF.md
INV-085 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-085_RUN_HANDOFF.md
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
