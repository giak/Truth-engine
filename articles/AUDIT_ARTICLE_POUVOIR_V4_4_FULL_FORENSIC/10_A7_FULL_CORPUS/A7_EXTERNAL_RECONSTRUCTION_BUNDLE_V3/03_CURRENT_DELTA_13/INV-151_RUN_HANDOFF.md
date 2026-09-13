# RUN_HANDOFF — INV-151

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-1846-energie-matieres-critiques-coercition`
- Deliverable: `2026-09-11_18-46_energie-matieres-critiques-coercition_INVESTIGATION.md`
- Deliverable SHA-256: `9a4fd072794e2d87cf8817f943b7accb9b15a96f485a7c4bfceb924168ad8fa8`
- Corpus runtime: `QRY=13 / SRC=13 / FCT=19 / provenance_families=3`
- Tests: `140 passed / 2 skipped`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`
- Persistence: `PASS / eligible=19 / blocked=19 / success=0 / failure=0 / MNEMO_UNAVAILABLE`
- Canonical artifacts: `6/6`

## Delta central

INV-151 établit un seuil mécaniste entre vulnérabilité économique et coercition exercée. Une dépendance énergétique ou minérale n'est pas une coercition par elle-même. Le statut change lorsque l'on ferme une chaîne `dépendance -> point de contrôle réel -> restriction/condition/coupure imputable -> coût matériel ou rupture -> adaptation de la cible`. Une concession politique spécifique constitue encore une arête supplémentaire.

- **Gaz russe 2022** : dépendance élevée + condition de paiement en roubles + coupures/réductions imputables + choc de prix/approvisionnement + adaptation européenne = **COERCITION_ECONOMIQUE_EXERCEE**. Une concession politique européenne à Moscou causée par ce levier = **NOT_ESTABLISHED**.
- **Terres rares / contrôles chinois** : restrictions d'exportation et effets industriels = **SUPPORTED** sur plusieurs épisodes ; l'intention et une concession politique européenne restent **CASE_SPECIFIC / GAP_CAUSALITY**.
- **Critical Raw Materials Act** : `dépendance identifiée -> architecture de résilience` = **SUPPORTED** ; il ne prouve pas qu'une dépendance donnée a déjà été weaponisée.
- **Uranium / enrichissement russes** : exposition et diversification préventive = **SUPPORTED** ; coupure russe analogue au gaz 2022 dans le corpus borné = **NOT_ESTABLISHED**.

## Modèle causal certifié

```text
FOURNISSEUR / ETAT / ENTREPRISE
-> DEPENDANCE DE FLUX
-> POINT DE CONTROLE REEL
-> RESTRICTION / CONDITION / COUPURE / MENACE
-> COUT / PENURIE / RISQUE DE CONTINUITE
-> ADAPTATION
-> CONCESSION OU DECISION EVENTUELLE
-> EFFET
```

Trois statuts doivent rester séparés :

```text
EXPOSITION
!= COERCITION_ECONOMIQUE_EXERCEE
!= COERCITION_POLITIQUEMENT_REUSSIE
```

## Règles probatoires conservées

```text
dependency != coercion
supply interruption != political intent
price shock != coercion
export control != political concession
adaptation != concession
strategic exposure != exercised leverage
restriction effect != requested-policy effect
absence of concession evidence != absence of coercive attempt
```

## Gap matériel

`DENOMINATOR_GAP` : le run ne fournit pas de base représentative permettant d'estimer la fréquence ni le taux de succès des dépendances énergétiques/minérales converties en coercition politique contre la France ou l'Union européenne.

## Statut

`INV-151 = CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`.

Aucune reclassification post-run n'est exécutée dans cette transaction : le mandat utilisateur portait uniquement sur le full run d'INV-151.
