---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-146-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-146"
---

<!-- DERIVED_FROM: synthesis=INV-146_SYNTHESIS.md; review=INV-146_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=NOT_RUN_BY_DESIGN; synthesis=PASS; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-146

```text
INV_ID = INV-146
TE_STATUS = NOT_RUN_BY_DESIGN / type=SYNTHESIS
TE_PATH = NONE
SYNTHESIS_PATH = INV-146_SYNTHESIS.md
INPUT_GATE = PASS_WITH_RECOVERY / 10 of 10 dependencies usable
CONTROL_VALIDATE = PASS
P0 = 0
P1 = 0
P2 = 4
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

La synthèse n’établit pas un double standard géopolitique général. Elle établit une **asymétrie de design juridique** entre certains régimes d’influence étrangère, tandis que l’asymétrie systématique de seuil probatoire, de vocabulaire et d’enforcement reste non démontrée.

Le modèle le mieux soutenu est mécanistique : visibilité, consentement, légalité, financement, tasking, clandestinité/coercition, exposition et effet expliquent les différences de qualification mieux qu’un simple axe allié/adversaire. Les cas Russie, Israël/opérateurs privés, UAE/Alp et France imposent les mêmes plafonds de preuve ; l’existence d’une opération ne ferme presque jamais I5-I7.

## Highest supported I0..I7

```text
I0 identity/relation = COMPARABLE / generally well supported in constituent cases
I1 resources/capability/access = COMPARABLE / generally supported
I2 documented action = COMPARABLE / supported on multiple ally, adversary and sender controls
I3 coordination/tasking/control = HETEROGENEOUS / case-specific; no camp-wide inference
I4 exposure/reach = HETEROGENEOUS / partial
I5 reception/persuasion = GENERALLY NOT_ESTABLISHED
I6 behavior/institutional/electoral change = PARTIAL or NOT_ESTABLISHED depending on case
I7 counterfactual outcome = GENERALLY NOT_ESTABLISHED
```

## Material gaps / contradictions

- `LEGAL_DESIGN_ASYMMETRY = ESTABLISHED` does not establish selective enforcement.
- `SYSTEMATIC_VOCABULARY_ASYMMETRY = NOT_ESTABLISHED` because no matched label corpus exists.
- `ENFORCEMENT_ASYMMETRY = NOT_ESTABLISHED` because comparable denominators and mature French/EU histories are missing.
- Domestic isomorphic controls are insufficient for the full third branch of the canonical question.
- INV-139/140 use bounded recovery handoffs because original terminal Library persistence is incomplete.

## RENARD decision + reason

```text
RENARD = NO
```

Residuals require dedicated matched datasets, future enforcement history, pure domestic controls, or original artifact recovery. Generic collection would be cumulative or non-discriminating.

## New ideas triaged

```text
matched vocabulary/enforcement dataset -> DEFER until a dedicated design is justified
pure domestic isomorphic comparator      -> DEFER / possible future control investigation
INV-139/140 original-byte recovery       -> RECHECK only if artifacts become available
```

## Registry patch

```text
INV-146 BACKLOG -> CLOSED
truth_engine remains NOT_RUN
renard -> NO
result_path -> INV-146_RUN_HANDOFF.md
next_action -> CLOSED; feed bounded asymmetry findings to INV-133
INV-133 remains BLOCKED on 11 other direct dependencies
```
