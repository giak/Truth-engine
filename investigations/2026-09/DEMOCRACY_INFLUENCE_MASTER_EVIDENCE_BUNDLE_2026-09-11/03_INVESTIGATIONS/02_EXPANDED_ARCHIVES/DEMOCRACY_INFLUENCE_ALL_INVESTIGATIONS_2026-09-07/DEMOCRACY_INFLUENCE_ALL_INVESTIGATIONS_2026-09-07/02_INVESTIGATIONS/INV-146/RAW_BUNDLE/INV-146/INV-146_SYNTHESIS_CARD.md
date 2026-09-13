---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "INV-146-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-146"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-146 -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+gate=DEPENDENCIES_DONE+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — INV-146

```text
SUBJECT = Asymétrie alliés/adversaires : mêmes mécanismes, mêmes standards de preuve, mêmes mots ?
OBJECT_QUESTION = À mécanismes comparables, les influences provenant d’alliés, d’adversaires et d’acteurs domestiques sont-elles décrites, documentées et sanctionnées avec les mêmes catégories et seuils de preuve ?
SCOPE = Synthèse comparative France/UE. Construire des paires ou triplets isomorphes par mécanisme : financement, lobbying, média, faux comptes, prestataire clandestin, sanctions, promotion démocratique. Comparer seulement des objets suffisamment semblables en visibilité, légalité, relation au commanditaire, cible et effet. Ne pas conclure à l’asymétrie sur simple différence de pays ou de vocabulaire.
MODE = SYNTHESIS
COVERAGE = PARTIAL
CORPUS_REFS = A004:210182384.lingerence-sans-mesure;A091:181572197.lindustrie-de-linfluence-enquete
DEPENDENCIES = INV-019;INV-022;INV-026;INV-033;INV-128;INV-134;INV-138;INV-139;INV-140;INV-145
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
INV-019 | status=CLOSED | truth_engine=DELIVERY_PASS_R2A2 | result=INV-019_RUN_HANDOFF.md
INV-022 | status=CLOSED | truth_engine=DELIVERY_PASS_R3 | result=INV-022_RUN_HANDOFF.md
INV-026 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-026_RUN_HANDOFF.md
INV-033 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-033_RUN_HANDOFF.md
INV-128 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-128_RUN_HANDOFF.md
INV-134 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-134_RUN_HANDOFF.md
INV-138 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-138_RUN_HANDOFF.md
INV-139 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=/INV-139_INVESTIGATION.md
INV-140 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=/INV-140_INVESTIGATION.md
INV-145 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-145_RUN_HANDOFF.md
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
