---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-049-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-049"
---

<!-- DERIVED_FROM: te_run=20260905-2145-open-society-foundations-france-ue; pilot_review=INV-049_PILOT_REVIEW.md; renard=INV-049_RENARD.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R2A2; inv=CLOSED; next=INV-071_READY_NOT_LAUNCHED -->

# RUN_HANDOFF — INV-049

```text
TE_STATUS = DELIVERY_PASS_R2A2
TE_RUN_ID = 20260905-2145-open-society-foundations-france-ue
QRY = 63
SRC = 17
PROVENANCE_FAMILIES = 10
FCT = 13
CHECKPOINTS = 8
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 13 blocked terminal outcomes
RENARD = CLOSED_NO_FURTHER_MATERIAL_DELTA
INV_STATUS = CLOSED
```

## Central delta

OSF est établi comme financeur transnational doté d'objectifs politiques/publics explicites et de mécanismes d'influence observables : grants, recherche, plaidoyer, formation, communication et contentieux.

Le RENARD ajoute un bridge important : des grants à More in Common sont explicitement orientés vers de la recherche d'opinion incluant la France et le niveau UE, tandis que Destin Commun appartient à un réseau à gouvernance mutualisée.

Cela **ne** suffit toujours pas à établir :

```text
OSF -> grant direct à l'entité juridique Destin Commun
OSF -> commandement/tasking de Destin Commun
OSF -> effet causal global France/UE
```

## Highest supported I0..I7

```text
I0 relation/identity = VERIFIED
I1 resources/capability/access = VERIFIED
I2 documented action = VERIFIED/SUPPORTED selon mécanisme
I3 coordination/tasking/control = NOT_ESTABLISHED pour OSF -> bénéficiaires
I4 exposure/reach = PARTIAL / cas spécifiques
I5 persuasion = UNRESOLVED
I6 behavior/institutional change = SUPPORTED seulement au cas par cas, pas agrégé
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps

1. grant/comptabilité nommant directement Destin Commun comme bénéficiaire OSF ;
2. clause de contrôle/tasking/validation substantielle ;
3. design causal isolant un effet France/UE.

## Registry patch

```text
INV-049 -> CLOSED
truth_engine -> DELIVERY_PASS_R2A2
renard -> CLOSED_NO_FURTHER_MATERIAL_DELTA
result_path -> INV-049_RUN_HANDOFF.md
INV-071 -> READY_NOT_LAUNCHED
INV-103 -> BLOCKED
```
