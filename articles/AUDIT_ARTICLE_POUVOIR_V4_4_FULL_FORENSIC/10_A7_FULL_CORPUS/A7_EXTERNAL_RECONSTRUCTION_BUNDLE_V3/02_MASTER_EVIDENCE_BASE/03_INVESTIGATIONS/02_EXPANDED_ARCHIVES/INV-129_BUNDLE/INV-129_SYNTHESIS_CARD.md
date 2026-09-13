---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "INV-129-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-129"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-129 -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+gate=DEPENDENCIES_DONE+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — INV-129

```text
SUBJECT = Lawfare et coercition juridique : contentieux stratégique, SLAPP, sanctions administratives, procédures et droit comme instruments d’influence
OBJECT_QUESTION = Dans quelle mesure le droit et les procédures peuvent-ils devenir des instruments de coercition politique ou institutionnelle — via contentieux stratégique, annulation/neutralisation électorale, sanctions administratives et restrictions financières — et quelles preuves permettent de distinguer remède légal, influence juridique, sur-conformité, abus, instrumentalisation intentionnelle et effet politique ?
SCOPE = France/Europe 2015–2026. Synthèse stricte des dépendances fermées INV-054, INV-080, INV-100 et INV-124. Comparer seulement les mécanismes isomorphes sur base légale, initiateur, décisionnaire, standard de preuve, contradictoire/recours, sanction ou restriction, intention/tasking et effet. Gardes : legal != legitimate ; adverse_effect != political_motive ; litigation != control_of_judge ; administrative_measure != guilt ; restriction != electoral_effect ; annulment != instrumentalization.
MODE = SYNTHESIS
COVERAGE = PARTIAL
CORPUS_REFS = A006:209222653.du-narratif-a-lingerence-le-seuil;A087:182502562.la-justice-spectrale-lere-du-bannissement;A098:180481861.quand-lelysee-attaque-un-journaliste
DEPENDENCIES = INV-054;INV-080;INV-100;INV-124
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
INV-054 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-054_RUN_HANDOFF.md
INV-080 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-080_RUN_HANDOFF.md
INV-100 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-100_RUN_HANDOFF.md
INV-124 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-124_RUN_HANDOFF.md
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
