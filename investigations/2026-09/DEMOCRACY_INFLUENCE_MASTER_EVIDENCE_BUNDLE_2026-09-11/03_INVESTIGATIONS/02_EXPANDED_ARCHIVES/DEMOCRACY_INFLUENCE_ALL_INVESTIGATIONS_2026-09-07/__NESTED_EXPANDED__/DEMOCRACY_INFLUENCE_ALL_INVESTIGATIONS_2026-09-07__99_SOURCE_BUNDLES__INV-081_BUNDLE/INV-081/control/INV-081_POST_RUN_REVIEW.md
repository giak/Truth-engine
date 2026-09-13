---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-081-POST-RUN-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-081"
---

<!-- DERIVED_FROM: te_run=20260906-1555-propriete-medias-francais; certification=DELIVERY_PASS_R3P1 -->
<!-- DECISION: review=PASS; renard=NO; close=true -->

# POST-RUN REVIEW — INV-081

```text
P0 = 0
P1 = 0
P2 = 2
REVIEW = PASS
RENARD = NO
```

## ROBUSTE

1. `CLM-001..002` casse correctement le faux agrégat « 80-90 % des médias » : le 91,4 % tracé est borné à la diffusion des quotidiens nationaux généralistes en 2021, pas à l'ensemble des médias français.
2. `CLM-003 / CTRL-001` impose un recheck temporel réel : l'actionnariat du Groupe Le Monde en 2026 invalide la reprise automatique des anciennes cartes de propriétaires.
3. `CLM-006 / CTRL-002` démontre la matérialité du dénominateur : PQN et PQR sont deux univers ACPM distincts ; Ouest-France est un contre-exemple de grande diffusion hors catégorie « milliardaire propriétaire ».
4. `CLM-004 / CTRL-003` maintient simultanément les deux propositions nécessaires : la concentration est un risque structurel réel, mais le score MPM de 71 % n'est pas une part de propriété.
5. `CLM-007 / CAU-001..002` préserve la frontière causale : propriété juridique, financement, audience et influence éditoriale ne sont pas substitués.
6. La provenance est diversifiée : 15 SRC, 12 familles ; aucune confirmation forte n'est fabriquée à partir de répétitions d'une même famille.

## P2

1. Les chiffres parlementaires 2026 `93 % / ~60 % / 50 %` restent non reproduits faute de méthode publique suffisamment explicite dans les matériaux examinés. Les conserver comme claims, puis `RECHECK` si le calcul source devient disponible.
2. Une reconstruction cross-media officielle complète doit être rejouée lorsque la base Arcom/EMFA couvrira effectivement presse et médias en ligne ; l'absence actuelle est une limite d'infrastructure, pas une invitation à fabriquer un dénominateur ad hoc.

## Runtime note

Le premier passage de persistance a produit `PARTIAL` parce que le flag runtime `MNEMO_UNAVAILABLE` n'avait pas encore été porté dans `degraded_flags`. Le flag a été ajouté sans modifier les faits ni le narratif ; le second passage est `PASS`, la DELIVERY-gate est `PASS`, et l'historique des deux tentatives reste dans `_RUN_STATE.json`.

## RENARD

```text
RENARD = NO
```

Les résiduels matériels ne sont pas des trous qu'une recherche générique supplémentaire peut raisonnablement fermer aujourd'hui :

- le calcul sous-jacent aux pourcentages parlementaires n'est pas exposé de façon reproductible dans les matériaux examinés ;
- la base publique Arcom n'offre pas encore le périmètre presse + online nécessaire au dénominateur cross-media ;
- propriété/financement -> contrôle éditorial relève d'INV-082 et demande des preuves propres de gouvernance, d'intervention ou d'effet.

Un RENARD général ajouterait surtout des cartes et des pourcentages hétérogènes, donc du fishing. Réouvrir seulement sur nouvelle méthodologie publiée, extension Arcom/EMFA, transaction matérielle ou preuve propre à INV-082.
