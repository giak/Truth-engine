---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis_card"
artifact_id: "INV-052-SYNTHESIS-CARD"
version: "1.0-kiss"
status: "materialized"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-052"
---

<!-- TRACE: generated_by=control.py; generated_from=INVESTIGATION_REGISTRY.csv#INV-052 -->
<!-- GATE: requires=type=SYNTHESIS+status=BACKLOG+current_synthesis_selection_gate+all_dependencies=CLOSED; state=passed -->
<!-- DECISION: truth_engine_search=false; dependency_outputs_only=true; no_status_transition=true -->

# SYNTHESIS_CARD — INV-052

```text
SUBJECT = Philanthrocapitalisme : quand le financement privé définit problèmes, métriques et solutions publiques
OBJECT_QUESTION = Quand et comment le financement philanthropique privé convertit-il ressources en définition de problèmes, métriques, expertise, accès ou décision publique, et à quel point cette chaîne diffère-t-elle d’un soutien pluraliste ou d’une simple capacité opérationnelle ?
SCOPE = Synthèse stricte de INV-049, INV-051, INV-053, INV-054, INV-057 et INV-058 lorsqu’elles sont CLOSED ou explicitement remplacées par un contrôle équivalent. Aucun Truth Engine ni web générique. Comparer financeur -> sélection/subvention -> bénéficiaire/intermédiaire -> agenda/expertise/advocacy -> accès/décision -> effet. Gardes : financement != commandement ; mission alignment != tasking ; bénéficiaire != proxy ; accès != capture ; output != effet.
MODE = SYNTHESIS
COVERAGE = PARTIAL
CORPUS_REFS = A045:194518266.lingenierie-de-lenclos;A053:193017697.comment-la-richesse-verrouille-le;A082:183123537.lempire-du-mensonge-rapport-dautopsie
DEPENDENCIES = INV-049;INV-051;INV-053;INV-054;INV-057
METHOD_PACK = METHOD_PACK.md §10

DEPENDENCY_MANIFEST
INV-049 | status=CLOSED | truth_engine=DELIVERY_PASS_R2A2 | result=INV-049_RUN_HANDOFF.md
INV-051 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-051_RUN_HANDOFF.md
INV-053 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-053_RUN_HANDOFF.md
INV-054 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-054_RUN_HANDOFF.md
INV-057 | status=CLOSED | truth_engine=DELIVERY_PASS_R3P1 | result=INV-057_RUN_HANDOFF.md
```

Synthesize only the closed dependency outputs and their terminal handoffs/reviews.
Do not launch Truth Engine or generic web collection for this synthesis.
Compare only materially isomorphic mechanisms; preserve visibility, consent, legality,
funding, tasking, coordination, coercion/clandestinity, exposure and effect as separate dimensions.
Do not infer evidentiary, vocabulary or enforcement asymmetry from geopolitical labels alone.
Produce a synthesis artifact plus a concise RUN_HANDOFF per METHOD_PACK §10.
