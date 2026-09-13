---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-134-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-134"
---

<!-- DERIVED_FROM: te_run=20260906-1805-attribution-ingerence; review=INV-134_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-134

```text
INV_ID = INV-134
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-1805-attribution-ingerence
TE_PATH = 2026-09-06_18-05_attribution-ingerence_INVESTIGATION.md
QRY = 15
SRC = 15
PROVENANCE_FAMILIES = 8
FCT = 22
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 22 blocked terminal outcomes
DELIVERABLE_SHA256 = 1af305d79fa8357672d05408c56994be5c20d640beee77929a4eed876eced56a
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

`CLM-001..009` transforme l'attribution d'ingérence en **graphe de preuve arête par arête**, au lieu d'un label binaire. La force peut décroître ou augmenter entre `incident`, `artefact`, `opérateur`, `intermédiaire`, `commanditaire/État`, `tasking/intention`, `exposition` et `effet`.

Plovdiv montre qu'un récit institutionnel peut se dégrader sous contrôle technique sans que le démenti adverse devienne vrai par défaut. Rokh Solis et Portal Kombat ferment des maillons techniques/opérateurs mais pas le commanditaire. RRN/Doppelganger ferme beaucoup plus haut la chaîne publique grâce à des documents internes décrits par le DOJ et une désignation administrative distincte du Trésor, sans devenir pour autant un jugement pénal définitif. Storm-1516 impose de ne pas importer automatiquement une attribution cyber GRU vers une opération informationnelle. `CAU-001..002` maintient l'effet démocratique non établi.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED case-by-case — opérateurs, infrastructures et certaines relations sont documentés
I1 resources/capability/access = VERIFIED/PARTIAL — infrastructures et capacités observables selon les cas
I2 documented action = VERIFIED for Rokh/Portal/RRN/Storm; hostile Plovdiv action NOT_ESTABLISHED
I3 coordination/tasking/control = STRONG public basis for RRN/Doppelganger; PARTIAL/UNKNOWN for several other cases
I4 exposure/reach = PARTIAL/MEASURED — notamment faible pour Rokh Solis; métriques hétérogènes
I5 reception/persuasion = NOT_ESTABLISHED généralement
I6 behavior/institutional/electoral change = NOT_ESTABLISHED généralement
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- Plovdiv : problème d'approche GPS supporté ; brouillage russe ciblé non fermé dans le dossier public inspecté ; récit `~1 h / cartes papier` contredit par les données de vol ; démenti russe conservé comme claim.
- Rokh Solis : marqueurs techniques israéliens et proximité Blackcore documentés ; commanditaire explicitement non établi par VIGINUM ; visibilité faible.
- Portal Kombat : rôle TigerWeb documenté ; hypothèse de prestation pour un opérateur dont l'identité reste inconnue.
- RRN/Doppelganger : base publique de commandement étatique forte mais statut `affidavit/allegation + administrative designation`, pas jugement définitif.
- Storm-1516 : attribution spécifique au mode opératoire forte ; pont direct vers GRU 29155 plus indirect dans le dossier public scoped.
- `CAU-001..002` : effet causal sur croyance, politique ou vote non identifié.

## RENARD decision + reason

```text
RENARD = NO
```

Les gaps restants exigent de nouvelles pièces techniques/tasking, décisions judiciaires, documents déclassifiés ou designs causaux. Une nouvelle recherche générique sur les mêmes attributions serait principalement cumulative.

## New ideas triaged

```text
intel -> executive -> media attribution laundering -> MERGE vers INV-137
counter-interference attribution economy           -> MERGE vers INV-144 quand dépendances closes
ally/adversary attribution symmetry                -> MERGE vers INV-146 quand dépendances closes
Plovdiv technical report                           -> RECHECK si pièce matérielle nouvelle
Rokh/Storm direct tasking evidence                 -> RECHECK si pièce matérielle nouvelle
generic catalogue of more attribution cases        -> DROP
```

## Registry patch

```text
INV-134 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-134_RUN_HANDOFF.md
next_action -> NONE — CLOSED; attribution-edge model available to INV-137/144/146; recheck only on material new technical/tasking/causal evidence.
```
