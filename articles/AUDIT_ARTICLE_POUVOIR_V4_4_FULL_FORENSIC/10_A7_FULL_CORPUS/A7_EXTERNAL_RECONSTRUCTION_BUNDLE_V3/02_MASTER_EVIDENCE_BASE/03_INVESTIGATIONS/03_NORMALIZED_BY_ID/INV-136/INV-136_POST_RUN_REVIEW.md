---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-136-POST-RUN-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-136"
---

<!-- DERIVED_FROM: te_run=20260906-2025-corruption-etrangere-ue; certification=DELIVERY_PASS_R3P1 -->
<!-- DECISION: review=PASS; renard=NO; close=true -->

# POST-RUN REVIEW — INV-136

```text
P0 = 0
P1 = 0
P2 = 3
REVIEW = PASS
RENARD = NO
```

## ROBUSTE

1. `CLM-001` impose une chaîne probatoire sérielle : `avantage/valeur -> payeur/client -> intermédiaire -> responsable public -> quid pro quo/tasking -> acte politique -> effet`. Argent, cadeau, proximité ou accès ne transmettent pas automatiquement la preuve aux maillons suivants.
2. `CLM-002/003` conserve le bon statut de Qatargate : base publique forte pour l'enquête, accord de repentir Panzeri et éléments relatifs au Qatar/Maroc, mais absence de jugement au fond du dossier belge principal. La validation procédurale de février 2026 ne tranche explicitement ni les charges suffisantes ni la culpabilité.
3. `CLM-004 / CTRL-002` distingue correctement le dossier Huawei : perquisitions, accusations de corruption dissimulée sous lobbying et inculpations sont établies comme faits procéduraux ; ils ne deviennent ni condamnation de Huawei ni preuve d'un effet sur une politique européenne déterminée.
4. `CLM-005/006 / CTRL-003` fournit avec Azerbaïdjan/PACE la chaîne la plus dense : enquête externe, sanctions institutionnelles, flux, courriels, acte politique identifié et jugement de première instance. Le run conserve toutefois l'issue d'appel de 2022 : prescription du volet de 500 000 euros et maintien d'acquittements sur d'autres transferts.
5. `CLM-007/008` sépare lobbying, influence étrangère et corruption. Un accès déclaré ou un intérêt étranger ne constitue pas un pacte corruptif ; inversement, l'habillage contractuel ou de lobbying ne neutralise pas une contrepartie illicite si elle est prouvée.
6. `CLM-009 / CAU-001..002` refuse le saut « corruption documentée -> politique européenne capturée ». Le corpus ferme plusieurs flux, relations et actes, mais pas un effet contrefactuel général sur les décisions européennes.
7. Le harnais externe R3P1 a été rejoué après finalisation : `140 passed, 2 skipped`; DELIVERY gate `PASS`; SHA du livrable inchangé.

## P2

1. **Qatargate/Morocco** : les arêtes spécifiques `payeur/commanditaire -> bénéficiaire -> contrepartie -> acte` restent inégalement corroborées et le dossier belge principal reste sans jugement au fond dans le corpus courant. Recheck seulement sur nouvelle décision ou pièce matérielle.
2. **Huawei** : la procédure 2025 documente les mécanismes allégués et les inculpations, mais pas encore un jugement au fond ni une cartographie causale vers un acte politique adopté. Recheck à évolution judiciaire.
3. **Effet politique** : aucun design ne permet d'estimer le nombre ou la nature des décisions qui auraient différé sans les avantages/paiements. Ce résiduel relève d'un problème de causalité, pas d'un manque de noms de scandales.

## RENARD

```text
RENARD = NO
```

Les résiduels matériels exigent des décisions judiciaires, pièces comptables/contractuelles, preuves de tasking ou un design causal. Une recherche générique supplémentaire sur d'autres scandales de corruption étrangère serait principalement cumulative et ne changerait pas le modèle central.

## Routing

```text
Qatargate merits / Morocco-specific chain -> RECHECK sur pièce ou décision nouvelle
Huawei merits / policy-act chain          -> RECHECK sur évolution judiciaire
foreign-agent / disclosure boundary       -> MERGE vers INV-145
ally/adversary qualification symmetry     -> MERGE vers INV-146
more scandal names without new mechanism  -> DROP
```
