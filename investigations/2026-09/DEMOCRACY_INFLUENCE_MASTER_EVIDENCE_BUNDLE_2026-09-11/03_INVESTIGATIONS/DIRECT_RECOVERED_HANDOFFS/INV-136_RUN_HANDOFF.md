---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-136-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-136"
---

<!-- DERIVED_FROM: te_run=20260906-2025-corruption-etrangere-ue; review=INV-136_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-136

```text
INV_ID = INV-136
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-2025-corruption-etrangere-ue
TE_PATH = 2026-09-06_20-25_corruption-etrangere-ue_INVESTIGATION.md
QRY = 32
SRC = 16
PROVENANCE_FAMILIES = 9
FCT = 22
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 22 blocked terminal outcomes
DELIVERABLE_SHA256 = 64e654d0ae7a34168c47b47234757787ff91295c1655b37c526478857f3cc899
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

`CLM-001..009` établit que la corruption étrangère doit être traitée comme une chaîne `valeur -> payeur -> intermédiaire -> responsable -> quid pro quo -> acte -> effet`, et non comme une étiquette déduite de l'origine étrangère ou de la présence d'argent.

Qatargate ferme fortement l'existence de l'enquête et certains aveux/éléments de réseau, mais pas la culpabilité générale ni chaque chaîne Maroc/Qatar. Huawei ferme procédure, mécanisme allégué et inculpations, pas condamnation ni effet politique spécifique. Azerbaïdjan/PACE fournit la chaîne la plus dense jusqu'à un acte politique ciblé et un jugement de première instance, mais l'issue d'appel doit rester jointe à toute citation du cas Volontè. `CAU-001..002` maintient l'effet contrefactuel général non établi.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED/PARTIAL — acteurs, intermédiaires et plusieurs relations sont documentés selon les cas
I1 resources/value/access = VERIFIED/PARTIAL — paiements, avantages, cadeaux, flux ou accès documentés/allégués avec statut propre
I2 documented action = VERIFIED/PARTIAL — enquêtes, transferts, sanctions, actes ou lobbying allégué documentés selon les familles
I3 coordination/tasking/quid pro quo = STRONGEST in Volontè/PACE; PARTIAL in Qatargate/Huawei pending merits
I4 exposure/reach = N/A/PARTIAL — non homogène pour corruption; accès institutionnel documenté selon les cas
I5 reception/persuasion = NOT_ESTABLISHED généralement
I6 behavior/institutional/policy change = PARTIAL case-specific; NOT_ESTABLISHED généralement
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- Qatargate : 20 personnes mises en cause et procédure validée en février 2026, mais aucune décision au fond dans le dossier principal scoped ; culpabilité non déduite.
- Morocco : les déclarations Panzeri sont matérielles mais ne ferment pas indépendamment chaque paiement, destinataire, tasking étatique et acte.
- Huawei : charges et mécanisme allégué sérieux ; défense/démenti conservés ; pas de jugement au fond ni d'effet politique causally identified.
- Volontè : première instance 2021 et issue d'appel 2022 doivent être citées ensemble ; prescription n'équivaut ni à confirmation définitive d'une condamnation ni à innocence factuelle totale.
- `CAU-001..002` : effet causal global sur politiques/décisions européennes non identifié.

## RENARD decision + reason

```text
RENARD = NO
```

Les gaps restants exigent nouvelles pièces, jugements ou designs causaux. Accumuler d'autres scandales sans nouveau mécanisme serait du fishing.

## New ideas triaged

```text
Qatargate merits / Morocco-specific evidence -> RECHECK si nouvelle pièce/décision
Huawei judicial outcome / policy act         -> RECHECK si évolution matérielle
foreign-agent disclosure boundary            -> MERGE vers INV-145
ally/adversary symmetry                       -> MERGE vers INV-146
more scandal names                            -> DROP
```

## Registry patch

```text
INV-136 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-136_RUN_HANDOFF.md
next_action -> NONE — CLOSED; recheck Qatargate/Huawei only on material judicial/documentary evidence; route disclosure boundary to INV-145 and symmetry to INV-146.
```
