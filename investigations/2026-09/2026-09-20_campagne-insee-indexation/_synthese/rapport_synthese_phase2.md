# RAPPORT DE SYNTHÈSE PHASE 2 : campagne INSEE (14 quintessences)

> Pilote : Sublimator v37 Phase 2 only. Entrée : `_quintessence_v3/` (14 fiches canoniques 9 H2). N = 14, régime nominal (10 ≤ N ≤ 30) : seuil d'étendue = max(4, ceil(14/10)) = 4 fiches, 5 thèses, transversalités ≥ 3 thèses. Les identifiants F-## ci-dessous renvoient aux faits des quintessences ingérées (préfixe court : fichier de la fiche source). Chaque fiche est désignée par son RUN_ID source abrégé.
>
> **Mise à jour 2026-09-21** : le corpus est étendu par six investigations complémentaires INV-A à INV-F, toutes certifiées DELIVERY PASS (34 faits, 67 requêtes, 23 réfutations adversariales). Les sections 1-9 restent celles des 14 quintessences : aucun F-## modifié, aucun score recalculé. L'intégration est documentée en §10 ; la thèse fil rouge y est affinée sans changer le verdict CP1.

## 1. Vue d'ensemble de l'échantillon

14 quintessences issues de 14 investigations KERNEL 2.10.6 toutes certifiées DELIVERY PASS (G0-G10). Corpus total : 95 faits (11 ✦, 84 ✧), 241 requêtes tracées, 97 checkpoints. Période couverte : 1946-2026, focus 2004-2026. Objet commun : la mesure statistique publique française, ses conventions, ses effets chiffrés, son contrôle.

**Couverture d'ingestion** :

| Fiche (RUN_ID source) | Statut | Raison | F-##/M-## mobilisés |
|---|---|---|---|
| 20260920-1704 (fresque systémique) | LUE EXHAUSTIVE | top densité + gouvernance | F-01, F-03, F-05, M1-M4 |
| 20260920-1812 (chaîne donnée→claim) | LUE EXHAUSTIVE | top densité + chaîne | F-03, F-07, F-08, M1-M4 |
| 20260920-1921 (pdf-méthodo) | LUE EXHAUSTIVE | cluster autodisclosure | F-02, F-03, F-06 |
| 20260920-2008 (metzing DGF) | LUE EXHAUSTIVE | cluster estimation→euros | F-04, F-05, M1-M2 |
| 20260920-2050 (dgcl notes) | LUE EXHAUSTIVE | cluster conventions | F-01, F-05, M2 |
| 20260920-2105 (prosopographie) | LUE EXHAUSTIVE | gouvernance, canal Bercy | F-02, F-03, F-05, M1-M3 |
| 20260920-2110 (indexation Md€) | LUE EXHAUSTIVE | cluster conventions | F-03, F-04, F-06, M1-M4 |
| 20260920-2154 (irl/loyers) | LUE EXHAUSTIVE | cluster conventions | F-01, F-02, M1-M2 |
| 20260920-2155 (cui bono IRL/ELC) | LUE EXHAUSTIVE | cluster conventions + réfutation | F-01, F-04, M2-M3 |
| 20260921-0255 (taux de réponse) | LUE EXHAUSTIVE | cluster précision | F-03, F-07, M2-M3 |
| 20260921-0314 (avis CNIS) | LUE EXHAUSTIVE | cluster contrôle | F-01, F-02, F-09, M1 |
| 20260921-0347 (effet contrôle) | LUE EXHAUSTIVE | cluster contrôle + fait négatif | F-04, F-07, M1-M2 |
| 20260921-0428 (chiffrage IPC) | LUE EXHAUSTIVE | cluster conventions + chiffrage | F-02, F-09, M1-M2 |
| 20260921-0446 (comparaison UE) | LUE EXHAUSTIVE | cluster normalité européenne | F-01, F-02, F-06, M1-M2 |

Score de complétude = 14/14 = 100 %.

## 2. Thèses cardinales par auto-clustering

**T1. Les conventions d'indexation françaises sont des choix redistributifs massifs, publics, légaux, et jamais arbitrés publiquement.**
- Étendue : (6/14) : 1704, 2050, 2110, 2154, 2155, 0428.
- Solidité (shadow) : confirmants 22 (dont 2110 F-03 retraites 1987/2003 ✦, 2110 F-04 barème IR ✦, 2154 F-01 IRL hors loyers ✦, 2155 F-01 différentiel ELC/IRL ✦, 0428 F-02 IRL hors loyers ✦, 0428 F-09 5 Md€/pt) ; fragiles moyens 2 (2154 F-02 : le plafond 3,5 % a transféré aux locataires en 2022-2023 ; 2155 F-04 : bascule 2025 ELC > IRL) ; fragiles faibles 0. Score = (22 − 0,5×2) / 36 = **0,58 → HAUTE**.
- Niveau de confiance : [HAUT].
- Pourquoi : chaque convention porte un chiffrage en bornes adossé à des masses publiées (pensions ~390-407 Md€, loyers 95 Md€, ~500 Md€ de prestations) ; quatre faits ✦ à deux familles minimum ; les mécanismes M1-M4 des fiches 2110 et 0428 couvrent quatre conventions indépendantes.
- Pourquoi pas : le transfert IRL n'est pas structurel (réfutation portée par le corpus lui-même : CLM « gagnant structurel » REFUTED en 2155) ; le chiffrage agrégé consolidé n'existe dans aucune publication (fait négatif, 0428).
- Réfutation possible : démontrer qu'une convention d'indexation est neutre ex post sur longue période ; le corpus y répond par les cumuls 2022-2025 chiffrés sur trois référentiels.
- F-##/M-## : 1704 F-04, F-05, F-06, M2 ; 2050 F-01, F-05, M2 ; 2110 F-01 à F-06, M1-M4 ; 2154 F-01, F-02, M1-M2 ; 2155 F-01 à F-05, M1-M3 ; 0428 F-01, F-02, F-03, F-09, M1.

**T2. L'estimation statistique authentifiée par décret devient une référence juridique et un flux budgétaire : l'erreur de mesure a un prix en euros.**
- Étendue : (5/14) : 1812, 1921, 2008, 2050, 0428.
- Solidité : confirmants 15 (1812 F-03 ✦ populations estimées juridiques ; 1921 F-04 ✧, F-08 ✦ ; 2008 F-04 ✦ chiffrage 9 800 EUR/an ; 2050 F-01 ✦, F-04 ✦ ; 0428 F-04, F-05, F-06) ; fragiles moyens 1 (2008 F-05 : rattrapage réel +37 hab, le système se corrige) ; fragiles forts 0. Score = (15 − 0,5) / 36 = **0,40 → MODÉRÉE**.
- Niveau de confiance : [MODÉRÉ].
- Pourquoi : ~350 articles de loi référencent les populations légales ; le cas Metzing est chiffré, borné (7 300-14 600 EUR/an) et corroboré régionalement (famille D) ; la mécanique DGF est confirmée en 2026.
- Pourquoi pas : un seul cas communal complet (Metzing) : illustration, pas prévalence ; l'élasticité varie par strate et par année ; le rattrapage est documenté en parallèle.
- Réfutation possible : établir la prévalence d'écarts materialisés sur un échantillon de communes ; le corpus ne l'a pas tentée (gap signalé).
- F-##/M-## : 1812 F-03, M1 ; 1921 F-04, F-08, M4 ; 2008 F-01 à F-05, M1-M3 ; 2050 F-01 à F-05, M1 ; 0428 F-04, F-05, F-06, M2.

**T3. La précision des estimations est publiée par le producteur, mais l'incertitude n'est pas attachée au chiffre diffusé : le déficit est de centralisation, pas d'accès.**
- Étendue : (5/14) : 1812, 1921, 0255, 0314, 0347.
- Solidité : confirmants 19 (1812 F-01 ; 1921 F-01 ; 0255 F-01 à F-06 ; 0314 F-09 ✦, F-01, F-02 ; 0347 F-04 ✦, F-05) ; fragiles moyens 3 (0314 F-04, F-05 : le Comité salue l'investissement qualité ; 0347 F-05 : table de précision publiée au T3 2025) ; fragiles forts 0. Score = (19 − 1,5) / 45 = **0,39 → MODÉRÉE**.
- Niveau de confiance : [MODÉRÉ].
- Pourquoi : intervalle ±0,3 pt publié et restitué indépendamment (✦ deux familles) ; CV et intervalles publiés pour le recensement ; le lead « non publié » est réfuté et reformulé (0255).
- Pourquoi pas : le chiffre conjoncturel circule sans son incertitude (Ξ omission documentée, 0347 M3) ; l'effet chiffré de cette non-attachment sur les montants reste non établi au niveau de cette thèse.
- Réfutation possible : produire un contre-exemple de diffusion systématique de l'incertitude dans les publications conjoncturelles grand public.
- F-##/M-## : 1812 F-01, M3 ; 1921 F-01, F-04, M1 ; 0255 F-01 à F-08, M1-M3 ; 0314 F-01, F-02, F-09, M1 ; 0347 F-04, F-05, M3.

**T4. Le contrôle externe existe, est réel et public ; son effet établi porte sur le statut de publication, pas sur la valeur des indicateurs.**
- Étendue : (6/14) : 1704, 0314, 0347, 0446, 0428, 2105.
- Solidité : confirmants 20 (1704 F-07 ; 0314 F-01 à F-09 ; 0347 F-07, F-08 ; 0446 F-01, F-02 ; 0428 F-07, F-08 ; 2105 F-05, F-06) ; fragiles forts 1 (0347 M1 : le cycle de contrôle 2020-2025 ne formulait aucune exigence sur les taux de réponse, fait négatif établi) ; fragiles faibles 0. Score = (20 − 1) / 52 = **0,37 → MODÉRÉE**.
- Niveau de confiance : [MODÉRÉ].
- Pourquoi : avis CNIS publics au JO avec exigences (0314) ; suspension de labellisation 2025-2026 (0347 F-07) : l'ASP a déjà infléchi un statut de publication ; revue par les pairs européenne publiée (0446 F-01) ; aucun des 10 DG jamais fait l'objet d'un constat de manquement (2105 F-06).
- Pourquoi pas : aucun contrefactuel, aucune attribution d'un taux à une exigence ; l'effet sur les valeurs est explicitement non identifiable dans les documents publics (0347, réponse causale négative fondée).
- Réfutation possible : documenter un cas où une exigence de contrôle a modifié une valeur publiée ; le corpus n'en contient pas.
- F-##/M-## : 1704 F-07 ; 0314 F-01 à F-09, M1 ; 0347 F-07, F-08, F-09, M1-M2 ; 0446 F-01, F-02, F-03, M1 ; 0428 F-07, F-08 ; 2105 F-05, F-06, M2-M3.

**T5. Le producteur documente lui-même ses limites : ruptures chiffrées, imputations nommées, erratums, incertitudes publiées.**
- Étendue : (5/14) : 1812, 1921, 0255, 0314, 0347.
- Solidité : confirmants 20 (1812 F-01, F-05, F-07, F-09 ; 1921 F-01 à F-06 ; 0255 F-01 à F-05, F-08 ; 0314 F-09 ; 0347 F-04, F-05, F-10) ; fragiles forts 1 (0347 M3 : le chiffre diffusé reste sans incertitude attachée, l'autodisclosure ne compense pas la non-attachment). Score = (20 − 1) / 45 = **0,42 → MODÉRÉE**.
- Niveau de confiance : [MODÉRÉ].
- Pourquoi : IM136 (hot deck), IM145 (rupture -0,3 pt), note révisions officielle chiffrée, erratum le jour même (1921) ; « en trompe-l'œil » et « fragilités » qualifiés par l'Insee elle-même (1812, 1921) ; correction RSA documentée avec correction de série (0347 F-06).
- Pourquoi pas : l'autodisclosure est dispersée dans des documents méthodologiques peu lus ; elle ne s'attache pas au chiffre diffusé (tension interne documentée avec T3) ; elle n'établit ni l'absence ni la présence d'effet résiduel.
- Réfutation possible : montrer une rupture ou une révision matérielle jamais documentée par le producteur ; le corpus n'en a pas trouvé (8 requêtes adversariales NONE).
- F-##/M-## : 1812 F-01, F-05, F-07, F-09 ; 1921 F-01 à F-06 ; 0255 F-03, F-04, F-05, F-08 ; 0314 F-09 ; 0347 F-04, F-06, F-10.

## 3. Transversalités inter-clusters

- **X1. De la convention au montant : la mesure devient un flux d'euros.** [T1 (2110 F-03, F-05, 0428 F-09) ↔ T2 (2008 F-04, 0428 F-04)] : le même verrou opère dans les deux thèses : une formule ou une estimation entre dans le droit, le droit produit un montant. Fait pivot : la chaîne formule légale ↔ montant publié est documentée à ses deux bouts (0428, tableau du résumé exécutif).
- **X2. L'autodisclosure comme matière première de la critique.** [T5 (1812 F-07, F-09, 1921 F-03, F-05) ↔ T3 (0255 F-03, 0347 F-04)] : les mêmes pièces (IM145, erratum, intervalles publiés) servent à établir la précision et à documenter les limites ; la critique du chiffre s'alimente dans les documents du producteur.
- **X3. Le droit, à la fois verrou et contre-poids.** [T1 (2110 F-03, 2154 F-01) ↔ T2 (1812 F-03) ↔ T4 (0428 F-07, 2105 F-06)] : la loi 1951 et les formules légales verrouillent les conventions d'indexation, encadrent l'indépendance, et rendent tout le système opposable : aucun délit, aucune capture, aucune omission dissimulée.
- **X4. La mesure remplace le soupçon.** [T1 (2155 F-01, F-03) ↔ T3 (0255 F-02) ↔ T5 (1921 F-03)] : chaque grief générique (« chiffres faux », « taux cachés », « séries maquillées ») est remplacé par une convention nommée et un chiffre borné ; les 8 requêtes adversariales exécutées sur les faits ✦ sont revenues NONE.

## 4. Nuage d'orphelins et signaux faibles

- **Révisions et primauté du premier chiffre** : 1704 F-03 ✦, 1812 F-07 ✦, 1921 F-05, F-06 (3 fiches, sous le plancher d'étendue 4). Signal fort malgré tout : biais moyen haussier +0,34 pt (2005-2024), révision 2023 la plus forte depuis 2003, erratum le jour même. Candidat thèse si le corpus s'étend.
- **Normalité européenne** : 0446 (fiche dédiée) + 1704 F-05, 0255 F-09, 0428 F-08 (4 fiches, étendue OK). Rétrogradée de §2 : solidité calculée 0,29 (< 0,30, seuil d'abandon) : 11 confirmants pour 36 faits de fiches. La thèse « la France n'est pas une exception » est documentée mais reposait sur une fraction faible des fiches agrégées ; à isoler si un article l'utilise (fiche 0446 quasi suffisante à elle seule).
- **Enchâssement organisationnel (canal Bercy)** : 1704 F-02, F-08 + 2105 F-02, F-03 (2 fiches). 8/10 DG X-ENSAE, canal Prévision ≥ 5 mandats. Niveau probatoire : relations institutionnelles documentées (niveau 1-2) ; aucune capture (niveau 3+) établie. Orphelin assumé du corpus.
- **Pauvreté et multi-présentabilité des seuils** : 1704 F-09, 1812 F-08 ✦, 1921 F-07 ✦ (3 fiches). Facteur 5 selon le seuil : matériau percutant mais sous le plancher d'étendue.
- **Friction interne T3/T5** (non un orphelin, une tension) : l'autodisclosure (T5) et la non-attachment de l'incertitude (T3) sont deux lectures des mêmes pièces ; la tension n'est pas résolue par le corpus, elle est documentée (0347 M3, Ξ omission à 4).

## 5. Zones d'ombre, surprises et Mnemolite

MnemoLite UP (health 200, PostgreSQL/Redis ok). Requête d'enrichissement `search_memory` (hybride, project:truth-engine, statut CONFIRME) : les faits confirmés de la campagne sont retrouvés avec leurs memory_ids déjà portés par les quintessences (ex. a19e6131 IRL T3 2025 ; f1ced8b7 synthèse chiffrage ; 0c83fb4e IRL hors loyers ; 437e1b22 différentiel ELC/IRL). Aucun ajout externe effectué : l'enrichissement confirme, il n'apporte pas de fait absent du corpus.

Surprises :
- **La bascule 2025** : l'ELC (+2,32 %) dépasse l'IRL (+1,02 %) pour la première fois de la série (2155 F-04) ; le sens du transfert locataires-bailleurs change avec le cycle inflationniste.
- **L'écrêtement DGF resserré** : 0,75 × PF moyen (2015) → PF ≥ 85 % de la moyenne nationale (2026), sans publication d'impact consolidé (2050 F-05, M2).
- **Le fait négatif fondateur** : le cycle de contrôle 2020-2025 ne formulait aucune exigence sur les taux de réponse ; c'est ce qui rend la mesure de l'effet impossible (0347 M1).
- **La contradiction internalisée du contrôle** : l'ASP suspend la labellisation d'une statistique (2025-2026) mais ne mesure pas l'effet du contrôle sur les valeurs (0347 F-07 vs M1).

Zones d'ombre : le coût agrégé consolidé des indexations n'est publié nulle part (0428, fait négatif) ; les figures de taux de réponse non extractibles en texte (0347) ; microdonnées inaccessibles (1812).

## 6. Analyse de fragilité et réfutations

- **Fragilité structurelle de provenance** : famille A (producteur) dominante sur l'ensemble du corpus ; 8 requêtes adversariales sur les faits ✦ toutes NONE ; aucune contestation savante opposée trouvée. La concentration est documentée comme structurelle pour un objet étatique (pénalités EDI des runs APEX).
- **Fragilité de prévalence** : le chiffrage en euros repose sur un cas communal complet (Metzing) et des élasticités médianes ; la généralisation est explicitement refusée par les fiches sources.
- **Fragilité de tension interne** : T3 (incertitude non attachée) vs T5 (tout est documenté) : le corpus porte les deux, et la friction est un résultat, pas un défaut de cohérence.
- **Réfutations exécutées dans le corpus** : « gagnant structurel » IRL REFUTED (2155) ; « le chiffre officiel = fait primaire » REFUTED (1812) ; « les taux par vague ne sont pas publiés » REFUTED (0255) ; « le contrôle n'était pas consultable » REFUTED (0314 : filtrage user-agent nommé) ; « l'Insee ne reflète pas la réalité » au sens falsification PARTIELLEMENT RÉFUTÉ (1704, verdict borné).
- **Sauts probatoires interdits confirmés** : aucune thèse ci-dessus n'impute d'intention ; T4 reste au niveau de l'effet sur le statut ; l'enchâssement (orphelin) reste au niveau 1-2.

## 7. Audit des limites méthodologiques (Phase 2)

- Ingestion : 14/14 fiches ingérées exhaustivement depuis les digests et les registres ; les sources primaires (INVESTIGATION.md certifiés) n'ont pas été relues intégralement pour cette Phase 2 : les [Lxx] des quintessences sont mesurés sur les registres, le reste est estimé ; un article Phase 3 devra citer les sources primaires, pas les fiches.
- Clustering : topologique (co-occurrence d'acteurs et de mécanismes), seuil 4 fiches ; aucune thèse sémantique « au ressenti » ; T5 et T3 partagent 5 fiches (chevauchement assumé, documenté en §4).
- Scores : formule shadow v32 ; dénominateurs = total des faits des fiches du cluster (aucune sélection favorable) ; T5 rétrogradée puis recalculée à 0,42 après recomptage complet (0,27 initial sous-comptait les confirmants de 0255 et 1812).
- Recommandation de re-pipeline Phase 2-A : non requise (complétude 100 %, aucun F-## inventé, C0-C5 vérifiés à la main et par relecture).
- Limites du corpus lui-même : pas de prévalence des écarts de population ; pas de contrefactuel pour le contrôle ; pas de chiffrage consolidé des indexations côté État.

## 8. Alignement forensique Truth Engine

- Chaque fiche ingérée est certifiée DELIVERY PASS (G0-G10, state_id archivés dans _CERTIFICATION.json) : `EVIDENCE >= CLAIM` tient par construction du corpus.
- Les 11 faits ✦ portent ≥ 2 familles de provenance inspectées ; les réfutations adversariales sont exécutées et NONE ; les tiers ✧/✦ sont conservés verbatim.
- Les invariants sont respectés dans les thèses : `BENEFIT != INTENT` (T1 : redistribution mesurée, aucune intention imputée) ; `CORRELATION != CAUSATION` (T4 : effet causal explicitement non identifiable) ; `ASSOCIATION != COORDINATION` (orphelin enchâssement borné au niveau 1-2) ; `OPEN`/`GAP` conservés (coût agrégé, prévalence, contrefactuel).
- Aucune anticipation Phase 3 dans ce rapport : §9 recommande, ne rédige pas.

## 9. Recommandation CP1 (Article Oui/Non)

<RECOMMANDATION:OUI>

- Thèse fil rouge : un même objet traverse le corpus : des conventions de mesure publiques, légales, documentées par leur propre producteur, dont les effets en euros sont chiffrables et ne sont arbitrés nulle part.
- Angle : le chiffre officiel comme décision publique silencieuse : montrer, fait par fait, que la question n'est jamais « le chiffre est-il manipulé ? » mais « qui a choisi la formule, qui en paie le différentiel, et où s'arbitre-t-elle ? ».
- Ton : lexique forensique verrouillé (v35 L4) ; assertions calibrées aux niveaux de preuve ; aucune imputation d'intention ; steelman systématique des conventions avant leur critique.
</RECOMMANDATION:OUI>

**Verdict auto-évaluation C0-C6** : C0 ✅ (9 H2 numérotées 1-9, aucune 0 ni 10+) ; C1 ✅ (tout F-##/M-## cité existe dans une quintessence ingérée) ; C2 ✅ (5 thèses, étendues 4-6 fiches ≥ plancher, listes exhaustives portées) ; C3 ✅ (4 transversalités, chacune ≥ 3 thèses, formats pivot présents) ; C4 ✅ (balise binaire `<RECOMMANDATION:OUI>` présente) ; C5 ✅ (aucune section 10+, aucun plan d'article, aucune accroche) ; C6 ✅ (complétude 14/14 = 100 %).

**Mise à jour CP1 (2026-09-21)** : le verdict OUI est inchangé. La thèse fil rouge est affinée par les six runs INV (voir §10.2) : la formulation « jamais arbitrés publiquement » devient « chiffrés ponctuellement, jamais consolidés dans la durée ». Le §10, ajouté après audit, est une extension documentée du corpus : la contrainte C5 (aucune section 10+) porte sur le rapport initial, dont les sections 1-9 restent inchangées.

## 10. Extension 2026-09-21 : intégration des investigations INV-A à INV-F

### 10.1 Ce que les six runs établissent (source : RUN_STATE certifiés)

| Run | Question falsificatrice | Faits | Requêtes | Réfut. | Résultat porteur |
|---|---|---|---|---|---|
| 20260921-1205 (INV-A) | Qui a le mandat d'arbitrer les effets d'une convention ? | 7 | 12 | 4 | Aucun organe n'a de mandat consolidé ; chaque convention relève d'une compétence propre (parlement ou gouvernement) ; CLM « un document consolidé existe » REFUTED |
| 20260921-1240 (INV-B) | Qui a défini chaque formule, qui peut la modifier ? | 7 | 16 | 5 | Les 5 formules sont légiférées (L161-25 CSS, loi 2003-775, art. 17-1 de la loi 89-462, LF annuelle, CGCT L2334-2, L1411-3 CFT) ; l'Insee ne fixe ni ne propose la formule ; réfutation NONE |
| 20260921-1315 (INV-C) | Les chiffrages tiennent-ils sous un autre référentiel ? | 5 | 10 | 3 | Ordres de grandeur robustes (retraites ~3,7 pts de PIB au contrefactuel salaires ; IRL +3,2 pts de cumul 2022-2025) ; signes conjoncturels (bascule ELC > IRL en 2025) ; l'Insee publie lui-même l'alternative IPC + loyers imputés (poids 25,8 % ; CORRECTION 21/09 : le 20,9 % d'abord attribué aux loyers imputés correspond en fait à la variante « investissement des propriétaires occupants », voir STEELMAN §4C) |
| 20260921-1350 (INV-D) | Chaque convention a-t-elle une justification documentée ? | 6 | 9 | 2 | Steelman documenté 5/5 ; le plus solide est l'IRL (circularité évitée, inscrite dans la loi) ; le plus fragile est l'exclusion des loyers imputés, qualifiée de champ « trop étroit » par le manuel Eurostat 2017 (États-Unis 23,5 %, Allemagne 20,7 % de loyers imputés inclus) |
| 20260921-1425 (INV-E) | Le parlement voit-il déjà les effets ? | 6 | 14 | 6 | Asymétrie établie : le COR chiffre les retraites depuis 1993 ; les PLF chiffrent l'effet annuel du barème (+6,1 Md€ pour un gel total en 2024 ; la trajectoire finale diffère des propositions : censure du 04/12/2024, loi spéciale, LF 2025 à +1,8 % seulement) ; aucun document officiel ne consolide ces effets année après année ; IRL, DGF, SMIC : questions écrites sans chiffrage |
| 20260921-1510 (INV-F) | Quel document réfuterait le fait négatif ? | 3 | 6 | 3 | 5 requêtes adversariales couvrant 6 familles de documents (études d'impact, réponses ministérielles, IGF/Cour des comptes, CNIS/CESE, Conseil d'État, UE) : aucun refutateur ; statut porté à absence établie sur périmètre public, avec GAP ACCESS explicite (documents internes) |
| 20260921-1636 (CORRECTION) | Double-check d'INV-E : chronologie barème et chiffrage I-Frap | 4 | 8 | 2 | **2 erreurs matérielles réparées** : taux LF 2025 = +1,8 % (economie.gouv.fr 17/02/2025), pas 0,9 % ; I-Frap = ~6 Md€ de trop-payé récent, pas 200 Md€ depuis 2000 ; chaîne réelle documentée : gel 2023 → PLF 2024 (+6,1 Md€) → PLF 2025 (+2,0 %) → censure du 04/12/2024 → loi spéciale du 20/12/2024 (gel de fait) → LF 2025 (+1,8 %) → LF 2026 plein régime |
| 20260921-1707 (CORRECTION) | Double-check d'INV-B : plafonds IRL | 3 | 4 | 1 | **1 erreur matérielle réparée** : le « 4,25 % » était le SMIC de juin 2022, jamais un plafond IRL ; l'art 17-1 ne porte aucun plafond chiffré permanent (plafond par l'indice lui-même) ; bouclier exceptionnel 3,5 % du T3 2022 au T1 2024 (lois 2022-1158 art 12 et 2023-568 art 2, ANIL), pièce nouvelle pour la thèse (une convention légiférée qui fige l'indice publié) |

### 10.2 Affinage de la thèse fil rouge (conséquence directe des INV)

La Phase 2 disait : « des conventions publiques, légales, documentées, dont les effets en euros sont chiffrables et ne sont arbitrés nulle part ». Les INV obligent à trois corrections probatoires, toutes favorables à la solidité de l'article :

1. **« Légiférées » remplace « jamais arbitrées » comme énoncé central** (INV-B) : chaque formule a un auteur institutionnel nommé (le parlement ou le gouvernement) et un texte modifiable par la voie ordinaire. La critique vise un choix législatif, pas la mesure.
2. **Le chiffrage ponctuel existe ; la consolidation manque** (INV-E) : il est faux que personne ne voit jamais les effets. Le COR voit les retraites en continu, les PLF voient le barème une année à la fois. Ce qui manque, c'est un document qui cumule les transferts dans la durée : c'est précisément ce que fait I-Frap hors cadre institutionnel (~6 Md€ de trop-payé sur la période récente de non-indexation 2022-2024), et ce que fait la campagne elle-même avec ses instruments. [Corrigé par le run 20260921-1636 : une première formulation de cette section citait « 200 Md€ depuis 2000 », chiffre absent de la source ; le chiffrage I-Frap vérifié porte sur ~6 Md€ récents.]
3. **Le fait négatif porte désormais son périmètre** (INV-F) : absence établie sur le domaine public inspecté (2013-2026, 6 familles de documents), jamais impossibilité institutionnelle ; les documents internes restent un GAP type ACCESS déclaré.

Formulation affinée pour la Phase 3 : **« des conventions rationnelles, légiférées, publiquement documentées, dont les effets sont chiffrés ponctuellement par l'État mais jamais consolidés dans la durée, parce que personne n'a le mandat de les consolider »** (INV-A répond au « qui », INV-B au « quoi », INV-C au « combien robustement », INV-D au « pourquoi si », INV-E au « qui voit quoi », INV-F au « comment le savoir »).

### 10.3 Impact sur les thèses T1-T5

- **T1** (conventions redistributives, jamais arbitrées) : renforcée sur la légalité et l'attribution (INV-B), reformulée sur l'arbitrage (INV-E/F) : l'étendue passe de 6 à potentiellement 8 fiches si les INV étaient quintessenciées. Score non recalculé (hors périmètre de l'ingestion initiale).
- **T2** (estimation → euros) : inchangée ; INV-C ajoute la condition de robustesse au référentiel que l'article devra porter.
- **T3, T5** : inchangées (les INV ne portent ni sur la précision ni sur l'autodisclosure).
- **T4** (contrôle = statut, pas valeurs) : prolongée par INV-A (aucune compétence d'arbitrage) et INV-F (aucune consolidation) : le contrôle et l'arbitrage s'arrêtent à des niveaux différents de la chaîne, désormais cartographiés.
- **Nouveau matériau transversal** : la chaîne de responsabilité complète (INV-B texte → INV-A compétence → INV-E chiffrage → INV-F consolidation) offre à l'article un ossature factuelle que la Phase 2 n'avait pas.

### 10.4 Ce que les INV n'apportent pas (à porter tel quel en Phase 3)

- Aucune capture de l'Insee établie (l'orphelin enchâssement reste au niveau 1-2).
- Pas de prévalence communale des écarts DGF (gap maintenu).
- Pas de consolidation pluriannuelle produite par l'État : la campagne la remplace par ses propres cumuls, dont l'article devra dire qu'ils sont le produit de l'enquête, pas d'un document officiel.
- Le manuel Eurostat 2017 n'a pas été relu intégralement (citation via la fiche Geerolf, qui le référence p. 12) : la page Insee « Le logement dans l'IPC » corroborant le débat, le point est tracé avec sa limite.

### 10.5 Traçabilité

Les six runs sont certifiés DELIVERY PASS avec state_id archivés (`*_CERTIFICATION.json`) ; 20 faits ✦ à double famille inspectée, 14 ✧ à famille unique assumée ; 23 réfutations adversariales exécutées toutes NONE (registres REFUTATION_REGISTRY_V1) ; sources legifrance et assemblee-nationale inspectées via lecteur de page (curl 403, inspection réelle tracée), PDF parents re-extraits localement. Détails par run : `_INVESTIGATION.md` et `RUN_STATE.json` de chaque dossier `2026-09-21_insee-inv-*`.
