# RENARD CORE V3 — corrections minimales avant intégration

Le protocole fourni est conservé comme **post-investigation adversarial/deepening pass**. Les corrections suivantes sont nécessaires avant usage canonique.

## R1 — Source tier != force probatoire automatique

Remplacer :

`CLAIM_STRENGTH <= min(SOURCE_TIER of supporting evidence). No claim above its weakest source.`

Par :

`SOURCE_TIER := retrieval/provenance heuristic, not truth rank.`

`EVIDENCE_WEIGHT := directness|claim_fit|provenance|method|independence|access_to_facts|recency|limitations.`

`CLAIM_STRENGTH <= strength of the strongest surviving independent evidence combination relevant to that exact claim.`

Une source faible ajoutée à une preuve forte ne doit pas mécaniquement abaisser la conclusion. Une source primaire peut établir qu’un acteur a écrit X sans établir que X est vrai.

## R2 — Supprimer CALIBRATION actuelle

Supprimer :

`CALIBRATION := verified/(verified+refuted)`

Ce ratio pénalise une bonne réfutation et ignore `SUPPORTED|DISPUTED|OPEN`.

Utiliser seulement des métriques descriptives :

- `MATERIAL_RESOLUTION := terminal_material_atoms / total_material_atoms`
- `TRACE_COVERAGE := traced_material_claims / total_material_claims`
- `ADVERSARIAL_COVERAGE := material_atoms_tested_against_rival / total_material_atoms`

Aucun seuil numérique ne remplace un gap décisif. Un seul atom central OPEN peut bloquer une conclusion forte.

## R3 — Base rate / prior

Ne pas fabriquer un prior numérique. Si aucun taux de base défendable n’existe : `PRIOR := UNKNOWN(reason)` ou appréciation qualitative explicitement fondée.

## R4 — Structured outputs

`No cell may be skipped` devient : chaque cellule contient une valeur **ou** `N/A(reason)` **ou** `OPEN(reason)`. Ne jamais remplir pour satisfaire le format.

## R5 — Mémoire/capabilités

`via MCP` ne doit pas imposer un outil inexistant. Utiliser le mécanisme de persistance réellement disponible dans le parent (Truth Engine/MnemoLite ou autre). Sinon émettre un état de handoff, sans simuler la persistance.

## R6 — Stop

RENARD est delta-only. Arrêt si :

- 0 nouveau delta matériel ; ou
- 2 cycles sans changement de statut d’hypothèse ; ou
- aucune branche accessible ne peut changer le modèle ; ou
- budget atteint **et** aucun gap décisif n’exige une extension justifiée.

Ne pas utiliser `CALIBRATION >= 0.85` comme critère de vérité.

## R7 — Intégration projet

RENARD reçoit :

- `INV_ID` ;
- résultat final Truth Engine ;
- gaps et claims centraux ;
- corpus pertinent ;
- objectif précis de deepening.

Il ne relance pas toute l’investigation par défaut. Il cherche le **delta qui peut changer le modèle**.
