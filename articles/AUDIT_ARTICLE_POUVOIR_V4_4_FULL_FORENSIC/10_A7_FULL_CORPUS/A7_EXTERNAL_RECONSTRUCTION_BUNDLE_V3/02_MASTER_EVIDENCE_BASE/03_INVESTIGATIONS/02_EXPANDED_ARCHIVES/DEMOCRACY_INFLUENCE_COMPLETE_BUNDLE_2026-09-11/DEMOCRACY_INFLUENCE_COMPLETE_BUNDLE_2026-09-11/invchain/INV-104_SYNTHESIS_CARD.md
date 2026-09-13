---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "INV-104-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-104"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-104 -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+current_synthesis_selection_gate+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — INV-104

```text
SUBJECT = Mensonge institutionnel → défiance → vulnérabilité à la manipulation : la boucle causale existe-t-elle ?
OBJECT_QUESTION = Une perte de confiance envers les institutions augmente-t-elle de façon mesurable la vulnérabilité à la manipulation, à l’indignation ou à l’exploitation de récits complotistes, et quelles chaînes causales permettent de distinguer corrélation, causalité, sélection préalable et effets de plateforme ?
SCOPE = Synthèse stricte de INV-103, INV-106, INV-107, INV-111 et INV-112 lorsque les dépendances réellement matérielles sont CLOSED. Aucun Truth Engine ni web générique. Tracer erreur/mensonge ou perception d’échec -> confiance -> exposition/réception -> comportement informationnel/politique. Ne pas forcer INV-106/107 uniquement pour fermer la synthèse : reframe ou réviser explicitement les dépendances si leur valeur reste HOLD.
MODE = SYNTHESIS
COVERAGE = SUBSTANTIAL_PRIOR
CORPUS_REFS = A008:208733314.la-fabrique-de-la-menace-comment;A014:202848231.lecart-legalitelegitimite-la-signature;A041:198170736.le-paradoxe-francais-66-de-colere;A065:189043675.la-machine-a-silence;A072:186844276.tristan-mendes-france-la-machine;A077:185893876.budget-2026-larchitecture-du-mensonge;A082:183123537.lempire-du-mensonge-rapport-dautopsie;A097:180580808.pravda-quand-lelysee-ironise-sur;A098:180481861.quand-lelysee-attaque-un-journaliste;A106:180194877.407-mensonges-lautopsie-dun-systeme;A111:180120693.macron-et-la-paix-en-ukraine-ce-que
DEPENDENCIES = INV-103;INV-111;INV-112
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
INV-103 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-103_RUN_HANDOFF.md
INV-111 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-111_RUN_HANDOFF.md
INV-112 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-112_RUN_HANDOFF.md
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
