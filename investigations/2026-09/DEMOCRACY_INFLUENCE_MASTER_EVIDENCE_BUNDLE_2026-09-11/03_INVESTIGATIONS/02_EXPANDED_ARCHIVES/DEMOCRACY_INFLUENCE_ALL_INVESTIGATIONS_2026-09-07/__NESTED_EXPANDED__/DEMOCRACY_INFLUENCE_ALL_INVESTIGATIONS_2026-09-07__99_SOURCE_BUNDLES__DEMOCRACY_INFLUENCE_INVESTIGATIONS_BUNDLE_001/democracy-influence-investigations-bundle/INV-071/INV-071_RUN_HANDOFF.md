---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-071-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-071"
---

<!-- DERIVED_FROM: te_run=20260905-2245-viginum-doctrine-impact; pilot_review=INV-071_PILOT_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R2A2; renard=NO; inv=CLOSED; next=INV-103_READY_NOT_LAUNCHED -->

# RUN_HANDOFF — INV-071

```text
TE_STATUS = DELIVERY_PASS_R2A2
TE_RUN_ID = 20260905-2245-viginum-doctrine-impact
QRY = 24
SRC = 14
PROVENANCE_FAMILIES = 5
FCT = 20
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 20 blocked terminal outcomes
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

VIGINUM est mieux décrit comme une **infrastructure étatique d'OSINT et de sécurité informationnelle, juridiquement bornée par l'extranéité mais en expansion fonctionnelle**, que comme une simple vigie ou une police générale du vrai.

Deux corrections corpus sont matérielles :

1. `VIGISCORE = aucune mesure d'impact` est trop fort. VIGISCORE estime un **risque d'impact** à partir de visibilité, propagation, contexte et signaux techniques ; il ne mesure pas causalement les effets réels sur opinions ou intentions de vote.
2. `VIGINUM n'attribue jamais des opérations liées à des acteurs d'un pays allié` est faux comme absolu depuis Rokh Solis : des marqueurs impliquant des acteurs israéliens/Blackcore sont documentés, tandis que le commanditaire final reste non établi.

Le run confirme aussi que l'accountability est réelle mais composite : CES auprès du SGDSN, CNIL sur les données, contrôle parlementaire et commission électorale indépendante créée en juillet 2026.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED
I1 resources/capability/access = VERIFIED
I2 documented action = VERIFIED
I3 coordination/tasking/control = SUPPORTED/VERIFIED par maillon ; sponsor ultime parfois UNRESOLVED
I4 exposure/reach = PARTIAL mais directement mesuré sur certains cas
I5 reception/persuasion = UNRESOLVED
I6 behavior/institutional change = réponses opérationnelles VERIFIED ; changement électoral NOT_ESTABLISHED
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps

1. causalité exposition -> opinion/vote ;
2. commanditaire final quand l'infrastructure/opérateur est identifié mais pas le tasking ;
3. effectivité pratique des nouveaux contrôles et garanties 2026.

## RENARD

`NO` : aucun résiduel accessible actuel ne promet un changement matériel du modèle sans basculer vers une investigation de cas spécifique ou attendre de nouvelles données.

## Corrections corpus

```text
A004: remplacer "pas de mesure d'impact" par la distinction risque d'impact / effet causal réel.
A004: retirer l'absolu d'asymétrie "jamais les alliés" ; dater et intégrer Rokh Solis.
A072: ne pas inférer de liens causaux VIGINUM -> experts/médias sans pièce de coordination spécifique.
```

## Registry patch

```text
INV-071 -> CLOSED
truth_engine -> DELIVERY_PASS_R2A2
renard -> NO
result_path -> INV-071_RUN_HANDOFF.md
INV-103 -> READY_NOT_LAUNCHED
```
