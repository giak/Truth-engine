---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "INV-040-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-040"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-040 -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+current_synthesis_selection_gate+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — INV-040

```text
SUBJECT = Déficit démocratique européen : réalité mesurable versus slogan politique
OBJECT_QUESTION = Dans quelle mesure l’architecture institutionnelle de l’Union européenne distribue-t-elle initiative, expertise, accès, veto, contrôle et responsabilité de façon susceptible de produire un déficit démocratique mesurable, et quels mécanismes relèvent plutôt de la délégation, de la co-législation ou de contre-pouvoirs réels ?
SCOPE = Synthèse stricte des dépendances INV-039 à INV-048 une fois CLOSED. Comparer initiative réglementaire, lobbying/consultation, DSA/gouvernance informationnelle, dispositifs anti-FIMI, certification, Chat Control/eIDAS, sanctions et puissance normative. Aucun Truth Engine ni collecte web. Gardes : complexité != déficit ; délégation != capture ; consultation != adoption ; pouvoir réglementaire != absence de contrôle ; effet défavorable != illégitimité.
MODE = SYNTHESIS
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A007:206399715.le-peuple-nexiste-que-sur-convocation;A010:205911763.le-verrou-invisible-anatomie-du-ric;A014:202848231.lecart-legalitelegitimite-la-signature;A022:199655164.le-verrou-28-recours-au-493-57-dabstention;A037:199049245.le-changement-de-regime-pourquoi;A057:192293819.la-democratie-en-cage
DEPENDENCIES = INV-039;INV-041;INV-042;INV-043;INV-044;INV-045;INV-046;INV-047;INV-048
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
INV-039 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-039_RUN_HANDOFF.md
INV-041 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-041_RUN_HANDOFF.md
INV-042 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-042_RUN_HANDOFF.md
INV-043 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-043_RUN_HANDOFF.md
INV-044 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-044_RUN_HANDOFF.md
INV-045 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-045_RUN_HANDOFF.md
INV-046 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-046_RUN_HANDOFF.md
INV-047 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-047_RUN_HANDOFF.md
INV-048 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-048_RUN_HANDOFF.md
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
