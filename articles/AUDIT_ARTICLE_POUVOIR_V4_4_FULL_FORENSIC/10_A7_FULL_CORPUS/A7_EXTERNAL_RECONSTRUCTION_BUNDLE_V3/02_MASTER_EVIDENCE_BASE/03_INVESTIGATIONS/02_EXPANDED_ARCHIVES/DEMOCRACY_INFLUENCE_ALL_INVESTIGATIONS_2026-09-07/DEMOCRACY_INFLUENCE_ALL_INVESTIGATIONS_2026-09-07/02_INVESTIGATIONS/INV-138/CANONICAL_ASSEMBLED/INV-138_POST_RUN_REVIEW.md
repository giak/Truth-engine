---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-138-POST-RUN-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-138"
---

<!-- DERIVED_FROM: te_run=20260906-2212-france-puissance-influence-exterieure; certification=DELIVERY_PASS_R3P1 -->
<!-- DECISION: review=PASS; renard=NO; close=true -->

# POST-RUN REVIEW - INV-138

```text
P0 = 0
P1 = 0
P2 = 4
REVIEW = PASS
RENARD = NO
DELIVERABLE_SHA256 = 54cc64ec22dff754b445b41bb921b9dd7b90c1397c4938a891f79675e050d823
```

## Robuste

1. `CLM-001/002` répond à l'objet sans faux binaire : la France possède un portefeuille explicite d'influence extérieure, mais origine étrangère, financement ou intention d'influencer ne suffisent pas à qualifier une ingérence.
2. `CLM-003/004 / CTRL-004/005` sépare proprement doctrine L2I, capacité institutionnelle et attribution du réseau Meta 2020. La liaison publique s'arrête aux individus associés à l'armée française ; le tasking institutionnel reste ouvert.
3. `CLM-005/006/008` établit des interventions modifiant matériellement des rapports de force internes au Tchad, en Côte d'Ivoire et en Libye, tout en conservant demande du gouvernement, mandat international, légalité, intention et contrefactuel comme dimensions séparées.
4. `CLM-007` établit un levier explicite visas/aide au développement et conserve l'absence d'estimation causale pays par pays.
5. `CLM-009` borne Madagascar 2025 à l'exfiltration documentée de Rajoelina ; aucun saut vers une causalité française du changement de pouvoir.
6. `CLM-010` conserve la contradiction entre la doctrine publique de 2023 « aucun candidat » et le rapport parlementaire 2026 évoquant des soutiens/oppositions récents à des candidats, sans inventer les cas absents du passage.
7. `CLM-011 / CAU-001..007` bloque la promotion exposition/action -> persuasion/vote/régime : I7 n'est pas établi.
8. PRE puis DELIVERY passent le contrat KERNEL R3P1 ; DELIVERY vérifie 23 QRY, 22 SRC, 16 familles, 26 FCT, 7 checkpoints, persistence terminale MNEMO_UNAVAILABLE et 140 tests PASS / 2 skipped.

## P2

1. **Meta 2020** : tasking institutionnel français non public. Recheck seulement sur déclassification, enquête, divulgation plateforme ou pièce de commandement.
2. **Candidats étrangers** : le rapport AN 2026 reste agrégé ; des cas nommés récents avec pièces primaires pourraient préciser la branche électorale, mais ne sont pas nécessaires pour le modèle actuel.
3. **Causalité** : impact des médias, programmes de coopération et leviers visa/aide sur comportements et décisions non isolé. Exige évaluation quantitative ou design causal, pas davantage d'exemples.
4. **Libye/Madagascar** : intention finale et contrefactuel restent ouverts ; attendre archives, déclassification ou pièces judiciaires/décisionnelles.

## RENARD

```text
RENARD = NO
```

Les résiduels accessibles par simple collecte générique ne changeraient plus le modèle. Les gaps décisifs exigent des pièces spécifiques de tasking/intention, des cas électoraux nommés avec documents primaires ou des designs causaux. Les contrôles symétriques produits sont suffisants pour alimenter `INV-146` après fermeture de ses autres dépendances.
