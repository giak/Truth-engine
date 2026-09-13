---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-068-RUN-HANDOFF"
version: "1.0-kiss"
status: "closed"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-068"
truth_engine: "NOT_RUN_BY_DESIGN"
renard: "NO"
reclass_impact: "INV-133"
---

# RUN_HANDOFF — INV-068

```text
INV_ID = INV-068
TE_STATUS = NOT_RUN_BY_DESIGN / type=SYNTHESIS
SYNTHESIS_PATH = INV-068_SYNTHESIS.md
SYNTHESIS_SHA256 = 94f8cb692c0bcd707cdb7a1569dbbae1038bdc3b62636507b57b1894374255f2
INPUT_GATE = PASS / 9 of 9 terminal handoffs
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

Le corpus ferme une chaîne d'intermédiation institutionnelle `ressources -> capacité/accès -> sélection/expertise -> exposition/reprise`, avec certaines reprises normatives case-specific. Il ne ferme pas en général `financeur -> contenu dicté`, `répétition -> persuasion`, `exposition -> adoption causée` ni un réseau transversal coordonné. Le terme « narrative laundering » doit donc rester réservé aux cas où dissimulation/tasking sont prouvés, pas déduit du financement ou de la répétition.

## Highest supported influence/effect edge

`resources -> access/expertise = SUPPORTED`; `selection -> exposure/reuse = SUPPORTED`; `expertise -> normative preparation = SUPPORTED case-specific`; `funder tasking -> dictated content -> policy outcome = NOT_ESTABLISHED generally`.

## Material gaps / contradictions

Tasking direct, logs de sélection/rejet, legislative footprints versionnés, causalité exposition -> croyance/décision, dénominateurs représentatifs.

## RENARD

`NO` — generic collection cumulative.

## Registry patch

`INV-068 BACKLOG -> CLOSED`; `truth_engine=NOT_RUN_BY_DESIGN`; `renard=NO`; `result_path=INV-068_RUN_HANDOFF.md`; route `INV-133`.
