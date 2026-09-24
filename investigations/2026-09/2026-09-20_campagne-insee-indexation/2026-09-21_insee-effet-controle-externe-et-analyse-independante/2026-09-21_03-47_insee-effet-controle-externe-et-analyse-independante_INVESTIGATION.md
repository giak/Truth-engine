ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-0347-insee-effet-controle-externe-et-analyse-independante | PARENT_RUN_ID:20260921-0314-insee-avis-conformite-cnis-eec-gap-access | AS_OF:2026-09-21
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-effet-controle-externe-et-analyse-independante/2026-09-21_03-47_insee-effet-controle-externe-et-analyse-independante_INPUT.md | SUBJECT_SLUG:insee-effet-controle-externe-et-analyse-independante | SUBJECT_FP:sha256:3f051dffd958f49a593c23f7e20261e0bfdec445af5715e237de53a19d2a07b5 | INPUT_SHA256:sha256:fefb21828c0c93beceb4df1e8f6dfe93ca12a3fe07f48691d760c706213f2ebb
COMPLEXITY:10→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:period:2013-2027 (series 2020-2025); geo:France (Hors Mayotte / France entiere depuis T1 2024); axes:CAUSALITY,MECHANISMS,ACTORS_RELATIONS,RULES_CONTROLS,COUNTER_HYPOTHESES,SOURCE_AUDIT; exclusions:sondages d opinion, debat politique sur le niveau du chomage; limits:les figures de taux de reponse ne sont pas extractibles en texte (valeurs ponctuelles seules)
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/FACT_VERIFICATION.md,protocol/UPDATE.md,search/EPISTEMIC.md,search/TEMPLATES.md,output/TEMPLATE.md,clusters/ICEBERG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# L'effet du contrôle externe sur l'enquête Emploi : ce qui est mesurable dans les documents publics, et ce qui ne l'est pas (UPDATE du run 03-14)

## TL;DR

```text
SUJET: Traiter deux branches laissées ouvertes par le parent 20260921-0314 — (1) le gap CAUSALITY du CAU-003 (mesurer l'effet du contrôle externe sur les taux de réponse de l'enquête Emploi) et (2) la pénalité MISSING_COUNTER (chercher une analyse indépendante du Service statistique public sur la précision publiée).
OBJET: La question causale reçoit une réponse négative fondée: l'effet du contrôle externe sur les taux de réponse n'est PAS identifiable dans les documents publics (aucune attribution, exigences datées 2027 et au-delà, aucune série avant/après, aucun contrefactuel), et la dernière observation disponible est une baisse. Ce que le corpus établit, c'est un effet du contrôle sur le STATUT DE PUBLICATION: suspension de la labellisation des séries de demandeurs d'emploi inscrits du 1er janvier 2025 au 20 mai 2026 (FCT-007).
SOURCE: Deux familles non-Insee obtenues et inspectées — autorité de contrôle (famille D, rapport annuel 2024) et commission d'enquête parlementaire (famille B, rapport 2016). L'intervalle de confiance publié passe en ✦ sur A + B (FCT-004).
MANIPULATION/STRUCTURE: Aucun marqueur rhétorique (DEM 0, BF 0). Ξ omission reste à 4: le chiffre conjoncturel est diffusé sans incertitude attachée, et ni le contrôle ni la commission n'abordent ce point.
LIMITE: MISSING_COUNTER est levée, mais la perspective obtenue est INDÉPENDANTE du producteur, non OPPOSÉE: aucune source contestant l'intervalle de confiance publié n'a été trouvée. L'effet du contrôle sur les taux reste une MESURE DUE, pas une vérification due.
```

## 1. RÉSUMÉ EXÉCUTIF

**Question objet (préservée du parent, inchangée).** Quelle précision est effectivement attachée aux estimations que l'Insee publie (chômage BIT, population légale, pauvreté, IPC), mesurée par les taux de réponse par vague et les intervalles publiés, et que reste-t-il établi lorsque le chiffre diffusé est lu sans son incertitude ?

**Requête de cet UPDATE.** Deux branches laissées ouvertes par le parent : le gap `CAU-003` (`GAP_TYPE=CAUSALITY`, effet mesuré du contrôle non établi) et la pénalité `MISSING_COUNTER` (aucune perspective indépendante du Service statistique public).

**Réponse bornée, en deux parties.**

**1. La question causale est refermée en tant que question, non comblée par une mesure.** L'effet du contrôle externe sur les taux de réponse de l'enquête Emploi **n'est pas identifiable dans les documents publics**, et les raisons sont établies pièce par pièce :

- **aucune attribution documentée** dans le corpus inspecté : ni le producteur, ni l'autorité de contrôle, ni la commission d'enquête ne rattachent une variation de taux à une exigence de contrôle ;
- **antériorité des exigences** : le cycle de contrôle précédent (avis initial du 8 octobre 2020, validité 2021-2025) ne formule **aucune exigence relative aux taux de réponse** (`SRC-004`) ; les exigences identifiées datent de 2026 pour l'exercice **2027-2030**, donc **postérieures** aux variations observées ;
- **attributions concurrentes** : les variations documentées sont attribuées par le producteur à la crise sanitaire (collecte fortement affectée à partir de la fin du T1 2020, retour au niveau d'avant crise depuis le T1 2022, `FCT-002`) et à des causes opérationnelles (cadre d'emploi des enquêteurs pour l'incident du T1 2013, `FCT-010`) ;
- **aucun contrefactuel** disponible, et **la dernière observation va dans l'autre sens** : 73,7 % de réponse et 60,6 % de collecte au T3 2025, soit **−1,1 point de collecte sur un an** (`FCT-003`).

**2. Ce qui est en revanche établi, c'est un effet du contrôle sur le statut de publication.** L'Autorité de la statistique publique a **suspendu la labellisation** des nouvelles statistiques de demandeurs d'emploi inscrits du **1er janvier 2025 au 20 mai 2026**, en prenant acte que leur stabilité et leur interprétabilité ne pourraient être garanties qu'à l'issue de la période de transition (`FCT-007`, `SRC-003`). Elle a par ailleurs attiré l'attention sur la nécessité d'un suivi et d'une analyse des impacts de la loi « Pour le plein emploi » sur les séries au sens du BIT issues de l'enquête Emploi (`FCT-008`). C'est le seul effet causal du contrôle que le corpus permet d'établir : il porte sur le **statut** (labellisé / non labellisé) et sur une **période explicite**, pas sur la valeur des indicateurs ni sur les taux de réponse.

**La pénalité `MISSING_COUNTER` est levée, avec une réserve nommée.** Deux pièces hors producteur sont obtenues et inspectées : le **rapport annuel 2024 de l'Autorité de la statistique publique** (autorité administrative indépendante chargée du contrôle du Service statistique public, famille `D`) et le **rapport de la commission d'enquête du Sénat** sur la mesure du chômage (famille `B`). Elles **engagent** la précision publiée sans la contredire : la commission restitue indépendamment l'intervalle de confiance de ± 0,3 point, en niveau comme en évolution (`FCT-004`), documente les limites de la mesure locale et un incident de publication (`FCT-010`), et l'autorité relaie la contestation savante de l'écart entre sources administratives d'emploi et enquête Emploi (`FCT-009`). Ce que la réserve signifie : **ce qui était absent, c'était une analyse indépendante du producteur, non une critique opposée**. Aucune source contestant l'intervalle de confiance publié n'a été trouvée après contre-recherche adversariale — statut consigné `NONE`, non comblé par symétrie.

**Ce que cela change pour l'objet.** Un fait passe en `✦` : `FCT-004`, sur deux familles indépendantes (`A` producteur qui publie l'intervalle, `B` commission d'enquête qui le restitue et le nuance). Et une contradiction nouvelle, ouverte et typée, apparaît : le contraste entre l'engagement le plus explicite de la qualité et la **dégradation** de la collecte à la dernière observation disponible. Le corpus ne soutient aucune des deux lectures ; la coexistence est consignée (`CTR-003`, `GAP_TYPE=CAUSALITY`).

**Acteurs.** Autorité de la statistique publique (contrôle, labellisation) ; Comité du label de la statistique publique (avis de conformité, cycles 2021-2025 / 2026 / 2027-2030) ; Insee, DSDS, Division Emploi (production, notes méthodologiques trimestrielles) ; commission d'enquête du Sénat (contrôle parlementaire, 2016) ; Eurostat (contrôle des rapports qualité, mention documentaire non inspectée) ; chercheurs contestant l'écart entre sources.

**Impact.** Deux dimensions documentées de plus qu'au parent : un bénéfice institutionnel (le statut de publication est vérifiable et opposable, une labellisation peut être retirée) et une investigation négative explicite (l'effet du contrôle sur les taux n'est pas mesurable avec les documents publics ; la mesure reste due, `NQ-001`). Le coût de la collecte reste un `GAP_TYPE=ACCESS` non comblé.

**Gaps principaux après cet UPDATE.** Cause mesurée (`AXS-008`, `CAU-003`, `NQ-001`) ; périmètre (aucune incertitude attachée à l'indicateur publié et effet de cette absence non chiffré, `CLM-004`, `CTR-002`, `NQ-003`) ; indépendance (aucune source opposée à l'intervalle publié, `NQ-004`) ; accès (textes légaux et règlement européen non inspectés, `NQ-002` ; coût de la collecte, `AXS-004`, `NQ-005`).

## 2. MANIPULATION_REPORT

Input `UPDATE`, mode `INVESTIGATION`, complexité `APEX` (10), symboles évalués sur le corpus final.

| Symbole | Score | Observation nommée |
|---|---:|---|
| Ξ omission | 4 | `CONFIDENCE_MISSING` inchangé : le chiffre conjoncturel est diffusé sans incertitude attachée. Les pièces nouvelles ne comblent pas l'absence — elles la contournent : la commission parlementaire restitue l'intervalle `± 0,3 point` mais ne discute jamais l'absence d'incertitude au moment de la diffusion |
| ⫸ convergence | 3 (parent 4) | la convergence baissse d'un cran : elle portait sur le suivi des taux de réponse comme indicateur de qualité ; elle ne porte plus, dans ce run, sur un second point — ni l'autorité de contrôle ni la commission ne rejoignent le producteur sur l'incertitude attachée au chiffre diffusé |
| ⏰ temporel | 4 | la chronologie est ici décisive et elle joue **contre** l'affirmation d'un effet : exigences de taux de réponse datées de 2026 pour 2027-2030, variations observées en 2020-2022 et 2024, cycle de contrôle précédent (2020, validité 2021-2025) sans aucune exigence de taux |
| Λ cadrage | 3 | « qualité contrôlée » continue d'absorber « incertitude publiée » dans le cadrage public : l'intervalle de confiance est publié, ce qui laisse lire que l'incertitude est attachée au chiffre diffusé, ce qu'aucune pièce n'établit |
| ↕ pouvoir vertical | 3 | le contrôle est interne à la puissance publique (autorité administrative indépendante, Comité du label, commission parlementaire) : institutionnellement distinct du producteur, non externe à l'État |
| ρ résistance | 4 | contre-puissance documentaire établie sur pièce et **exercée** : une labellisation a été suspendue, une étude d'impact a été demandée, un incident de publication a été documenté par une commission d'enquête |
| Κ cynisme | 2 | asymétrie documentaire entreprises/ménages maintenue ; intention non établie |
| κ influence subtile | 2 | architecture d'information possiblement orientante (le statut de publication et la labellisation sont des signaux), design non démontré |
| Σ sémiotique | 2 | le label est un signe ; ici il peut être retiré, ce qui le rend falsifiable |
| Φ spectacle | 2 | médiatisation des chiffres trimestriels, hors corpus |
| 🌐 réseau | 3 (parent 2) | chaîne documentée et élargie : producteur → Comité du label → autorité de contrôle → Cnis → commission parlementaire → Eurostat → contestation savante |
| € argent, Ω inversion, Ψ sidération | 1 | aucune observation matérielle dans ce run (aucun flux financier, aucune inversion, aucune saturation d'information) |
| ⚔ guerre cognitive | 0 | aucune activité d'influence organisée constatée |

**Rhétorique.** `NUM 3` inchangé (le chiffre brut coupé de son incertitude), `AUTH 1`, `FAC 1`. `DEM 0`, `BF 0` : aucun marqueur de mauvaise foi. Deux pièces de contrôle sont inspectées et l'une d'elles **retire** un label à des séries : le corpus ne peut pas être lu comme une caution de complaisance.

**Hypothèses implicites retenues comme telles.** (a) L'incertitude relève du producteur et du contrôle, non de l'attribut publié ; (b) un taux de réponse élevé vaut garantie de faible biais — le corpus engage cette hypothèse sans la démontrer. Aucune des deux n'est présentée comme établie par une source.

## 3. LEADS (LED-001 à LED-007)

| ID | Lead | Statut | Élément décisif |
|---|---|---|---|
| LED-001 | Le gap `CAU-003` du parent : mesurer l'effet du contrôle sur les taux de réponse | **SATURATED** (réponse négative fondée) | L'effet n'est pas identifiable : aucune attribution, exigences datées 2027 et au-delà, aucun contrefactuel, dernière observation en baisse (`FCT-001`, `FCT-003`, `FCT-002`, `FCT-010`, `SRC-004`) |
| LED-002 | Le producteur publie à chaque trimestre les taux de collecte, de réponse et une table de précision | SATURATED | Note méthodologique T3 2025 : 60,6 % de collecte, 73,7 % de réponse, 46,4 % de réponse par internet en réinterrogation (`FCT-003`, `FCT-005`) |
| LED-003 | La série de collecte se dégrade sur la période récente | SATURATED | 77 % au T1 2023 contre 73,7 % au T3 2025 ; −1,1 point de collecte sur un an (`FCT-001`, `FCT-003`) |
| LED-004 | Le contrôle externe a produit un effet daté et borné sur le statut de publication | SATURATED | Suspension de la labellisation des séries de demandeurs d'emploi inscrits, 1er janvier 2025 – 20 mai 2026 (`FCT-007`, `CTRL-001`) |
| LED-005 | Une analyse indépendante du Service statistique public sur la précision des indicateurs conjoncturels existe et est inspectable | SATURATED | Rapport annuel de l'autorité de contrôle (famille `D`) et commission d'enquête parlementaire (famille `B`) (`FCT-007`, `FCT-009`, `FCT-010`) |
| LED-006 | Une erreur de mesure d'un indicateur publié est documentée et réparée par le producteur | SATURATED | Couverture des bénéficiaires du RSA : sous-estimation jusqu'au T2 2024, ~90 % à partir du T3 2024, série passée retraitée (`FCT-006`) |
| LED-007 | Contestations externes de résultats publiés et réponses institutionnelles | SATURATED | Écart entre sources administratives d'emploi et enquête Emploi relevé par des chercheurs et relayé par l'autorité ; contestation de la mesure de population et réponse de l'autorité (`FCT-009`) |

Aucun lead n'est saturé par confirmation d'une hypothèse de rétention. `LED-001` est saturé par **réponse négative fondée** : le lead demandait une mesure, le run établit que la mesure n'est pas possible avec ces documents, et dit pourquoi.

## 4. FAITS (FCT-001 à FCT-010)

| FCT | Tier | Date | Famille(s) | Valeur retenue |
|---|---|---|---|---|
| FCT-001 | ✧ | 2023-08 | A (`SRC-001`) | T1 2023, France hors Mayotte : taux de collecte **64 %** (logements répondants sur l'échantillon), taux de réponse **77 %** (logements répondants sur les logements dans le champ) ; l'écart s'explique par les résidences non principales, dont le statut hors champ est souvent confirmé sur le terrain |
| FCT-002 | ✧ | 2023-08 | A (`SRC-001`) | Collecte fortement affectée à partir de la fin du T1 2020 (déplacements impossibles, face-à-face converti en téléphone) ; retour au niveau d'avant crise **depuis le T1 2022** |
| FCT-003 | ✧ | 2025-11-13 | A (`SRC-002`) | T3 2025 : collecte **60,6 %** (−1,1 point sur un an ; −1,2 point hors Mayotte, département entré dans l'échantillon au T1 2024), réponse **73,7 %**, réponse par internet en réinterrogation **46,4 %** |
| **FCT-004** | **✦** | 2025-11-13 | **A + B** (`SRC-002`, `SRC-005`) | **Intervalle de confiance à 95 % du taux de chômage trimestriel : ± 0,3 point, en niveau comme en évolution** (un taux mesuré à 10,0 % a 95 % de chances d'être entre 9,7 % et 10,3 %) ; la commission d'enquête du Sénat restitue **indépendamment la même valeur** et la nuance du producteur (le milieu de l'intervalle est plus probable) |
| FCT-005 | ✧ | 2025-11-13 | A (`SRC-002`) | Table de précision des principaux indicateurs (niveau, précision à 95 % en point, intervalle) par sexe et classe d'âge, pour le chômage, le halo et l'emploi |
| FCT-006 | ✧ | 2025-11-13 | A (`SRC-002`) | Bénéficiaires du RSA nettement sous-estimés jusqu'au T2 2024 ; amélioration du questionnaire puis taux de couverture ~**90 %** à partir du T3 2024 ; série passée corrigée par appariement individuel avec le dispositif administratif puis calage |
| FCT-007 | ✧ | 2025-03-14 | D (`SRC-003`) | L'autorité de contrôle a **suspendu la labellisation** des nouvelles statistiques de demandeurs d'emploi inscrits du **1er janvier 2025 au 20 mai 2026**, en prenant acte que stabilité et interprétabilité ne pourront être garanties qu'à l'issue de la transition ; suivi en lien avec le Cnis |
| FCT-008 | ✧ | 2025-03-14 | D (`SRC-003`) | La loi « Pour le plein emploi » est susceptible d'induire des variations significatives des séries de taux d'activité, de chômage et d'emploi au sens du BIT issues de l'enquête Emploi ; l'autorité attire l'attention sur l'importance d'un suivi et d'une analyse de ces impacts |
| FCT-009 | ✧ | 2025-03-14 | D (`SRC-003`) | Écart grandissant, relevé par certains chercheurs, entre les sources administratives sur l'emploi et le nombre d'actifs occupés de l'enquête Emploi : l'autorité juge cette explicitation importante et a soutenu publiquement une mesure de population contestée, en soulignant le manque de justifications méthodologiques des contestations |
| FCT-010 | ✧ | 2016-10-04 | B (`SRC-005`) | Incident de publication du T1 2013 : trois facteurs identifiés par le producteur (refonte de la chaîne des traitements, accroissement temporaire de la non-réponse lié au déploiement du nouveau cadre d'emploi des enquêteurs, rénovation du questionnaire) ; estimation en juin 2013, puis communications en septembre 2013 et mars 2014 avec rétropolation ; les taux locaux sont des estimations hybrides non estampillées BIT |

`FCT-004` est le seul fait `✦` du run : deux familles de provenance indépendantes (`A` producteur, `B` commission d'enquête parlementaire), deux sources inspectées dans ce run, et une réfutation terminale (statut `NONE`). Les neuf autres faits restent `✧`, dont trois reposent sur une famille unique hors producteur (`D` : `FCT-007`, `FCT-008`, `FCT-009`).

## 5. CHAÎNES CAUSALES (CAU-001 à CAU-004)

| ID | Chaîne | Statut |
|---|---|---|
| CAU-001 | Décision d'une autorité de contrôle (délibéré) → retrait du statut de labellisation d'une série, motivé et borné → effets documentés sur les usages pendant la suspension | **SUPPORTED** — c'est l'effet causal du contrôle le mieux établi du corpus ; il porte sur le statut, pas sur la valeur (`FCT-007`) |
| CAU-002 | Conditions de collecte (questionnaire, mode, base de sondage) → couverture d'une population dans l'enquête → correction du questionnaire puis retraitement de la série passée par appariement administratif et calage | **SUPPORTED** — erreur de mesure identifiée et réparée (couverture des bénéficiaires du RSA, ~90 % à partir du T3 2024, `FCT-006`) ; l'attribution de cette correction au contrôle n'est pas établie |
| CAU-003 | Qualité de la base de sondage et conditions de terrain → non-réponse → dégradation de la mesure → correction, nouvelle estimation et communications | **SUPPORTED** — incident du T1 2013, trois facteurs identifiés par le producteur (`FCT-010`, `FCT-002`) ; c'est la chaîne causale la mieux documentée côté conditions de collecte |
| CAU-004 | Exigence de contrôle externe → action du service sur la collecte → variation des taux de réponse | **GAP (CAUSALITY)** — aucune attribution documentée ; cycle de contrôle précédent sans aucune exigence de taux de réponse ; exigences identifiées datées de 2026 pour 2027-2030, donc postérieures aux variations ; aucun contrefactuel ; dernière observation en baisse |

`CAU-004` est la chaîne que le parent laissait ouverte sous l'identifiant `CAU-003`. Elle est ici **traitée et refermée en tant que question** : le run ne dit pas qu'aucun effet n'existe, il dit que cet effet n'est pas mesurable avec les documents publics, et il nomme les trois raisons qui rendent la mesure impossible en l'état. Ce qui reste ouvert est une **mesure**, non une vérification.

## 6. CONTRÔLES (CTRL-001 à CTRL-002)

| ID | Contrôleur | Règle / autorité | Information examinée | Action documentée | Statut |
|---|---|---|---|---|---|
| CTRL-001 | Autorité de la statistique publique (autorité administrative indépendante) | Labellisation des statistiques publiques ; code de bonnes pratiques ; pouvoir de suspendre une labellisation et d'adresser des observations | Dossiers du Service statistique public, audition du Cnis et de ses commissions, contestations externes | Suspension de la labellisation des nouvelles séries de demandeurs d'emploi inscrits (1er janvier 2025 – 20 mai 2026) ; appel à un suivi et à une analyse des impacts de la loi sur les séries BIT ; soutien public à une mesure de population contestée | **SATURATED** — `EFFET_DOCUMENTE_SUR_LE_STATUT_DE_PUBLICATION` |
| CTRL-002 | Comité du label de la statistique publique (Cnis) | Avis de conformité, label d'intérêt général et de qualité statistique, proposition du caractère obligatoire, publication au Journal officiel, suites exigées | Dossier de l'enquête, taux de réponse du test 2027, stratégie de tests | Cycle 2021-2025 : aucune exigence relative aux taux de réponse (avis initial du 8 octobre 2020) ; prolongation par avis rectificatif du 3 octobre 2025 pour 2026 ; cycle 2027-2030 : avis du 30 juin 2026 retenant les taux de réponse comme indicateurs de comparabilité et exigeant des suites | **SATURATED** — `EFFET_NON_ETABLI_SUR_LES_TAUX_DE_REPONSE` (`GAP_TYPE=CAUSALITY`) |

`CTRL-002` porte le point dur de ce run : c'est **le même dispositif** qui, en 2020, ne formulait aucune exigence de taux de réponse, et qui, en 2026, en fait un indicateur de comparabilité. L'écart entre les deux cycles est daté et documenté ; l'effet de ce changement sur les taux ne l'est pas.

## 7. ACTIONS (ACT-001 à ACT-004)

| ID | Acteur | Action | Statut |
|---|---|---|---|
| ACT-001 | Autorité de la statistique publique | Suspension de la labellisation des nouvelles séries de demandeurs d'emploi inscrits du 1er janvier 2025 au 20 mai 2026, avec suivi en lien avec le Cnis | SATURATED |
| ACT-002 | Autorité de la statistique publique | Attire l'attention sur l'importance d'un suivi et d'une analyse des impacts de la loi « Pour le plein emploi » sur les séries de taux d'activité, d'emploi et de chômage au sens du BIT issues de l'enquête Emploi | SATURATED |
| ACT-003 | Insee (service producteur) | Publie à chaque trimestre une note méthodologique contenant les taux de collecte et de réponse et la table de précision des principaux indicateurs ; a amélioré le questionnaire sur les bénéficiaires du RSA et retraité la série passée par appariement administratif puis calage | SATURATED |
| ACT-004 | Commission d'enquête du Sénat | Rapporte et documente la précision publiée (± 0,3 point), les limites de la mesure locale et l'incident de publication du T1 2013 | SATURATED |

Aucune intention n'est imputée : `RESPONSIBILITY_MAP` reste `N/A_NO_PERSON_ASSIGNED`, l'objet portant sur une configuration institutionnelle de production et de contrôle, et non sur des décisions individuelles. Le déclencheur de l'amélioration du questionnaire sur les bénéficiaires du RSA (`ACT-003`) **n'est pas établi** par le corpus : le run ne le rattache pas au contrôle.

## 8. AXES (AXS-001 à AXS-009)

| AXS | Axe | Statut | Résultat |
|---|---|---|---|
| AXS-001 | SOURCE_AUDIT | SATURATED | Cinq pièces inspectées : deux notes méthodologiques du producteur, un rapport annuel d'autorité de contrôle, un avis de labellisation du cycle précédent, un rapport de commission d'enquête |
| AXS-002 | SCOPE_HISTORY | SATURATED | Histoire du contrôle : cycle 2021-2025 **sans exigence de taux de réponse**, prolongation 2026, cycle 2027-2030 avec exigence ; incident de publication T1 2013 ; crise sanitaire et retour au niveau de 2022 |
| AXS-003 | EVIDENCE_CASES | SATURATED | Trois cas : incident T1 2013 (trois facteurs), sous-estimation puis correction de la couverture RSA, divergence entre sources d'emploi |
| AXS-004 | RESOURCES_FLOWS | **GAP (ACCESS)** | Coût de la collecte et financement non documentés ; aucune pièce budgétaire retrouvée |
| AXS-005 | MECHANISMS | SATURATED | Base de sondage, non-réponse, correction et calage : mécanismes documentés par le producteur lui-même |
| AXS-006 | ACTORS_RELATIONS | SATURATED | Producteur, autorité de contrôle, Comité du label, Cnis, commission parlementaire, Eurostat, contestation savante |
| AXS-007 | RULES_CONTROLS | SATURATED | Labellisation et sa suspension, avis de conformité et suites exigées, contrôle européen des rapports qualité, obligation de réponse |
| AXS-008 | IMPACT_RESPONSIBILITY | **GAP (CAUSALITY)** | L'effet du contrôle sur les taux reste non mesurable ; seul l'effet sur le statut de publication est établi |
| AXS-009 | COUNTER_HYPOTHESES | SATURATED | La précision publiée n'est pas contestée : la contre-recherche ne trouve ni contradiction, ni correction, ni autre valeur primaire |

## 9. DELTA_REPORT (protocole UPDATE §3)

```text
PARENT_RUN_ID:20260921-0314-insee-avis-conformite-cnis-eec-gap-access
PARENT_AS_OF:2026-09-21 | CURRENT_AS_OF:2026-09-21
```

| ID | CLASS | VALEUR/STATUT PARENT | VALEUR/STATUT COURANT | PREUVE | IMPACT AVAL |
|---|---|---|---|---|---|
| `CAU-003` | RECHECK → refermé en tant que question | GAP (CAUSALITY) — effet du contrôle sur les taux non établi | **Résolu en tant que question** : effet non identifiable, trois raisons nommées | `FCT-001`, `FCT-002`, `FCT-003`, `FCT-010` ; `SRC-004` (aucune exigence de taux de réponse dans le cycle 2021-2025) | `NQ-001` de ce run ; reste une **mesure due**, non une vérification due |
| `AXS-008` | RECHECK | GAP (CAUSALITY) — non quantifié | **GAP maintenu et précisé** : seule la mesure est due, la raison de son impossibilité est établie | idem | `IMPACT_MAP` INVESTIGATION NEGATIVE |
| `MISSING_COUNTER` (pénalité) | RECHECK → **levée** | Pénalité .10 appliquée | **Aucune pénalité** : analyse indépendante obtenue et inspectée | `SRC-003` (famille D), `SRC-005` (famille B) | EDI : LIMITED 0.4175 → BROAD 0.7843 |
| `FCT-004` (nouveau) | NEW | — | **✦** A + B | `SRC-002` (intervalle ± 0,3 point) + `SRC-005` (restitution indépendante) ; réfutation `NONE` | `CLM-003` SUPPORTED sur deux familles |
| `FCT-001`, `FCT-002`, `FCT-003`, `FCT-005`, `FCT-006` (nouveaux) | NEW | — | ✧ famille A | `SRC-001`, `SRC-002` | permettent la lecture chronologique (2023 vs 2025) qui fonde la réponse causale |
| `FCT-007`..`FCT-009` (nouveaux) | NEW | — | ✧ famille D | `SRC-003` | `CTRL-001`, `ACT-001`, `ACT-002` ; base de la levée de `MISSING_COUNTER` |
| `FCT-010` (nouveau) | NEW | — | ✧ famille B | `SRC-005` | couvre la temporalité archivistique ; `CAU-003` |
| `CTRL-001` (nouveau) | NEW | — | SATURATED, `EFFET_DOCUMENTE_SUR_LE_STATUT_DE_PUBLICATION` | `FCT-007` | `CAU-001`, `CLM-002` |
| `CTRL-002` (nouveau) | NEW | — | SATURATED, `EFFET_NON_ETABLI_SUR_LES_TAUX` | `SRC-004` | porte le gap `CAU-004` |
| `CTR-003` (nouveau) | NEW | — | OPEN (CAUSALITY) | `FCT-003` vs engagement de la qualité | contradiction consignée, non lissée |
| EDI | RECHECK | LIMITED — 0.4175, cible APEX 0.80 non atteinte, pénalités .20 | **BROAD — 0.7843**, pénalités .00, cible APEX **non atteinte de 0,0157** | 5 sources, 3 familles (A, B, D) | `MISSING_COUNTER` levée ; concentration signalée au seuil |
| Ξ (symbole) | RECHECK | 4 | **4** (inchangé) | `FCT-003`, `FCT-005` | `CONFIDENCE_MISSING` maintenue |
| ⫸ (symbole) | RECHECK | 4 | **3** | divergence sur l'incertitude attachée | la convergence ne porte plus que sur un point |

```text
AFFECTED_IDS: LED-001;LED-002;LED-003;LED-004;LED-005;LED-006;LED-007;AXS-002;AXS-003;AXS-008;CLM-001;CLM-002;CLM-003;CLM-004;CAU-001;CAU-002;CAU-003;CAU-004;CTRL-001;CTRL-002;ACT-001;ACT-002;ACT-003;ACT-004;FCT-001..FCT-010;SRC-001;SRC-002;SRC-003;SRC-004;SRC-005;EDI;Xi;convergence
UNCHANGED_IDS: AXS-001;AXS-004;AXS-005;AXS-006;AXS-007;AXS-009;CTR-001;CTR-002;OBJECT_QUESTION;OBJECT_COVERAGE;scope
NOT_REOPENED: faits de contrôle du parent (famille D, avis de conformité 2026, prolongation 2026, EAR 2026) classés REUSE — objet stable, non réexaminés ici;Eurostat LFS (mention documentaire, non inspectée);fiche de précision du recensement, DT2023-22 et baromètre entreprises (faits de producteur du parent, REUSE)
NEW_GAPS: CAUSALITY:2 (CAU-004, CTR-003);SCOPE:1 (CTR-002);INDEPENDENCE:1 (acteurs, NQ-004);ACCESS:2 (AXS-004, NQ-002)
```

**Delta de statut (DELTA_PLAN exécuté).** Les faits de contrôle du parent (famille `D`) sont classés `REUSE` — objet stable, non réouverts. Les deux questions de la requête sont traitées : l'une est refermée en tant que question (`CAU-004`), l'autre ferme une pénalité (`MISSING_COUNTER`). Aucun fait du parent n'est re-publié comme « vérifié par ce run » : seuls les faits nouveaux figurent au registre.

## 10. CONTRADICTIONS

| ID | Type | Conflit | Traitement | Statut |
|---|---|---|---|---|
| CTR-001 | Apparente | CV national du recensement très faible (0,01 %) contre non-réponse différentielle forte (56 % en résidences non principales contre 77 % dans le champ en 2021) | Deux sources d'erreur distinctes (erreur de sondage contre biais de non-réponse) ; aucune moyenne | RESOLVED (périmètre) |
| CTR-002 | Matérielle | Précision publiée et engagée (± 0,3 point, table de précision, engagement par une instance de contrôle) contre incertitude non attachée au chiffre conjoncturel diffusé et non mesurée dans ses effets | Écart de périmètre, et il n'est pas résolu par les pièces nouvelles : ni l'autorité ni la commission ne quantifient l'effet de cette absence | OPEN (SCOPE) |
| CTR-003 | Matérielle | Qualité présentée comme contrôlée et engagée (label, obligations, rapports) contre dégradation de la collecte à la dernière observation disponible (73,7 % de réponse, −1,1 point sur un an au T3 2025) | Aucun document inspecté ne relie les deux, ni ne l'examine comme un échec du contrôle : la coexistence est constatée, la relation causale n'est pas établie | OPEN (CAUSALITY) |

## 11. EDI

```text
[SOURCES] ◈:2 ◉:3 ○:0
EDI:0.7843 raw:0.7843 penalties:0.00[] N/A:[]
geo:0.667 lang:1.0 strat:0.65 owner:0.917 persp:0.75 temp:0.75
⟐:2 ⟐̅:1 🌍:0 🎓:1 🔥:0 | COV:0.889 IND:0.6 CC:0.5 EDI*:0.7789
band:BROAD — cible APEX 0.80 non atteinte de 0.0157 (parent : LIMITED 0.4175, pénalités .20)
DIAGNOSTIC_NOT_TRUTH
```

**Ce qui fait monter l'EDI, nommément.** Trois sources nouvelles hors producteur (rapport annuel d'autorité de contrôle, avis de labellisation du cycle précédent, rapport de commission d'enquête), la levée de `MISSING_COUNTER`, et la couverture d'une temporalité archivistique (incident de publication du T1 2013) qui manquait au parent.

**Ce qui empêche d'atteindre la cible APEX, nommément.** La perspective locale ou régionale reste absente (`🌍:0` : aucune pièce locale ou régionale inspectée), la couverture géographique est partielle (champ France hors Mayotte jusqu'au T1 2024), et la circularité amont reste notable : **6 faits sur 10 reposent au moins partiellement sur la famille `A`**.

**Décision de pénalité, explicite.** Aucune pénalité n'est appliquée. `OWNERSHIP_CONCENTRATION` n'est pas déclenchée : la famille `A` porte **2 sources sur 5 (40 %)** et **6 faits sur 10 (60 %)** — le seuil est *strictement* supérieur à 60 %. Le chiffre est signalé **au seuil exact** et non arrondi. Si l'on retenait le seuil comme inclusif, la pénalité vaudrait 0,10 et `EDI = 0.6843` ; **les deux valeurs sont données** et la valeur de référence reste celle du seuil strict. `MISSING_COUNTER` est **levée** : l'analyse indépendante du Service statistique public existe et a été inspectée. La réserve est ailleurs, et elle est inscrite : ce qui était absent était une analyse **indépendante du producteur**, pas une critique **opposée** — voir `CLM-004`.

**Profil de couverture des claims décisifs.** `CLM-001` : objet direct, **2 familles indépendantes**, aucun contre-crédible trouvé. `CLM-002` : objet direct, **1 famille** — le claim est borné à ce que la pièce établit et ne généralise pas. `CLM-003` : objet direct, **2 familles**. `CLM-004` : objet direct, 2 familles, `GAP_TYPE=INDEPENDENCE` — la perspective obtenue ne contredit pas la précision publiée.

## 12. CARTE DIALECTIQUE

**Thèse (le système statistique public).** La qualité n'est pas déclarative : elle est documentée, publiée et examinée par des instances distinctes. Le producteur publie à chaque trimestre les taux de collecte et de réponse et une table de précision (`FCT-003`, `FCT-005`) ; une autorité administrative indépendante rend un rapport annuel et **retire** une labellisation quand la comparabilité est en cause (`FCT-007`) ; elle demande une analyse d'impact sur des séries qui vont être affectées par une réforme (`FCT-008`) ; une commission d'enquête parlementaire restitue la précision publiée et documente un incident (`FCT-004`, `FCT-010`). Le label, lui, est falsifiable : il a été suspendu.

**Antithèse (la plus forte, inchangée au fond).** Ce qui est contrôlé est la qualité de l'opération, pas l'incertitude attachée au chiffre diffusé. Le contrôle exige lui-même des analyses qu'il ne détient pas encore — impact de la base de sondage, impact de la loi sur les séries — et il a dû retirer une labellisation, ce qui atteste que la qualité documentée n'est pas un uniforme. La précision publiée (± 0,3 point) n'est pas l'incertitude du nombre lu.

**Synthèse par les pièces.** Le corpus ne permet de trancher ni pour une lecture de complaisance ni pour une lecture d'insuffisance structurelle : il permet de **borner**. La contre-perspective existe (familles `B` et `D`, hors producteur), mais elle engage la qualité, non l'incertitude du chiffre diffusé — et aucune source ne contredit l'intervalle publié.

**Tensions réelles.** Le contrôle réclame un suivi et une analyse d'impacts (`FCT-008`) tout en développant ses propres indicateurs de comparabilité : exigence et capacité de mesure ne sont pas au même stade. Et la dernière observation disponible (`FCT-003`) est une **baisse** de la collecte, au moment précis où la qualité est le plus explicitement engagée.

**Silences documentaires.** Aucun document inspecté n'attribue une variation de taux de réponse à une exigence de contrôle. Aucune source inspectée ne conteste l'intervalle de confiance publié. Le coût de la collecte n'est documenté nulle part dans le corpus.

## 13. PÉRIMÈTRE & LIMITES

**Inclus.** Objet du parent (précision attachée aux estimations publiées, France, 2003-2026) ; branches traitées ici : la cause de l'effet du contrôle sur les taux et l'indépendance de la perspective.

**Exclus.** Sondages d'opinion ; débat politique sur le niveau du chômage ; reprises médiatiques (contexte non probatoire) ; analyse interne non publiée des services de l'Insee.

**Limites d'accès.** Les figures de taux de réponse ne sont pas extractibles en texte (seules les valeurs ponctuelles publiées sont utilisables) ; les textes légaux (loi du 7 juin 1951) et le règlement (UE) 2019/1700 ne sont **pas inspectés** (`NQ-002`) ; le dispositif européen de contrôle des rapports qualité est **mentionné mais non inspecté** ; aucune pièce budgétaire n'a été retrouvée (`AXS-004`).

**Limites de méthode.** Cinq sources seulement, dont **6 faits sur 10** reposant au moins partiellement sur le producteur — signalé au seuil exact, sans pénalité ; perspective locale ou régionale absente ; la contestation savante des écarts entre sources est **relayée par l'autorité de contrôle, non inspectée à la source** (`CLM-004`) ; les rapports et avis sont des actes institutionnels : leurs signataires sont une autorité d'émission, non une responsabilité personnelle.

**Limite de la réponse causale, énoncée sans détour.** « Non identifiable dans les documents publics » **n'est pas** « inexistant ». Le run établit qu'aucune pièce publique ne permet la mesure, et il nomme ce qui manque : une série avant/après rattachée à des exigences datées, un contrefactuel ou une comparaison internationale (`NQ-001`).

## 14. ÉTAT DES CONNAISSANCES

- **Établi (✦).** L'intervalle de confiance à 95 % du taux de chômage trimestriel est publié et vaut ± 0,3 point, en niveau comme en évolution ; il est restitué **indépendamment** par une commission d'enquête parlementaire, avec la nuance du producteur (`FCT-004`).
- **Établi (✧, familles A, B, D).** Les taux de collecte et de réponse et leur évolution (64 % / 77 % au T1 2023 ; 60,6 % / 73,7 % au T3 2025, −1,1 point sur un an) ; l'effet de la crise sanitaire sur la collecte et le retour au niveau d'avant crise depuis le T1 2022 ; la table de précision par sexe et classe d'âge ; la sous-estimation puis la correction de la couverture des bénéficiaires du RSA (~90 % à partir du T3 2024) ; la suspension de la labellisation des séries de demandeurs d'emploi inscrits (1er janvier 2025 – 20 mai 2026) ; l'appel à une analyse d'impact de la loi « Pour le plein emploi » sur les séries BIT ; l'écart entre sources administratives d'emploi et enquête Emploi relevé par des chercheurs ; l'incident de publication du T1 2013 et ses trois facteurs.
- **Établi (✧) — un fait négatif exploitable.** Le cycle de contrôle précédent (avis initial du 8 octobre 2020, validité 2021-2025) **ne formulait aucune exigence relative aux taux de réponse** : c'est ce fait qui rend la mesure de l'effet impossible sur la période où les variations se produisent.
- **Probable.** L'effet du contrôle passe par l'**agenda d'analyse** plutôt que par les taux : l'autorité demande une étude d'impact ciblée (`FCT-008`), ce qui est un effet documenté sur la production d'analyse. Retenu comme lecture possible, non comme résultat.
- **Contesté.** Aucune contestation matérielle de la précision publiée n'a été trouvée : la contre-recherche adversariale ne retourne ni contradiction, ni correction, ni autre valeur primaire (statut `NONE`, consigné).
- **Inconnu.** Effet mesuré du contrôle sur les taux de réponse (`CAU-004`, `NQ-001`) ; effet chiffré de l'absence d'incertitude attachée sur un montant indexé (`CTR-002`, `NQ-003`) ; coût de la collecte (`AXS-004`, `NQ-005`) ; base juridique et comparaison européenne (`NQ-002`) ; source opposée à l'intervalle publié (`NQ-004`).
- **Réfuté.** « Le contrôle externe n'était pas consultable » — établi comme faux au run précédent, non rouvert ici. Et « le suivi des taux de réponse est une pratique de producteur isolée » — réfuté : il est retenu par un contrôle externe comme indicateur de comparabilité, et l'exigence est datée.

## 15. SUSPICION / VÉRIFICATION

**Contrôles exécutés.** Acquisition et inspection de cinq pièces, dont trois nouvelles hors producteur : la note méthodologique de l'enquête Emploi (août 2023, référence T1 2023), la note méthodologique de la publication trimestrielle (T3 2025), le rapport annuel 2024 de l'autorité de contrôle, l'avis de prolongation du Comité du label portant l'avis initial de 2020, et le rapport de la commission d'enquête du Sénat (2016, chapitre sur l'enquête Emploi). Extraction texte avec conservation de la mise en page pour permettre la vérification des citations.

**Identité des pièces.** Les documents sont identifiés par leur taille et leur empreinte d'octets au moment de l'acquisition, et les extractions texte sont jointes : toute citation de ce rapport est vérifiable contre la pièce archivée.

**Échecs réels, consignés.** Les figures de taux de réponse ne sont pas extractibles en texte (limite déclarée dans le périmètre). Les textes légaux et le règlement européen n'ont pas été inspectés : le gap est typé `ACCESS` et routé (`NQ-002`), non comblé par une paraphrase. Aucune réfutation opposable n'a été trouvée sur le fait `✦` : l'absence est consignée comme `NONE`, non comblée par symétrie. Aucun succès n'a été simulé ; aucun canal payant ou privé n'a été employé.

**Delta de statut.** `CAU-003` du parent : `GAP CAUSALITY` → **refermé en tant que question** (effet non identifiable, raisons établies). `MISSING_COUNTER` : pénalité levée. `FCT-004` : `✧` → **`✦`** sur deux familles. Nouveaux : `CAU-001` à `CAU-003` (chaînes soutenues), `CTRL-001` (effet sur le statut de publication), `CTRL-002` (effet non établi sur les taux), `CTR-003` (contradiction ouverte). Ξ inchangé à 4 ; convergence de 4 à 3. EDI : `LIMITED 0.4175` → **`BROAD 0.7843`**, cible APEX 0.80 non atteinte de 0,0157.

**Vérification restante.** Effet mesuré du contrôle sur les taux (`NQ-001`) ; base juridique et comparaison européenne (`NQ-002`) ; effet de l'absence d'incertitude attachée sur les usages chiffrés (`NQ-003`) ; source opposée à l'intervalle publié (`NQ-004`) ; coût de la collecte (`NQ-005`).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:7|CLM:4|AXS:9|CAU:4|CTRL:2|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Effet mesure du controle externe sur les taux de reponse: non etabli (CAU-003 GAP CAUSALITY)","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le gap CAUSALITY herite (CAU-003): mesurer l effet du controle externe sur les taux de reponse de l enquete Emploi.","linked_ids":["CAU-003","CLM-001"],"locator":"NEXT_QUERIES NQ-001 du parent 20260921-0314 ; CAU-003 du parent","materiality":"DECISIVE","note":"Reponse bornee: l effet n est PAS identifiable a partir des documents publics. Aucune source inspectee ne l attribue; les variations documentees sont attribuees par le producteur a la crise sanitaire et a des causes operationnelles; le cycle de controle precedent (2020) ne comportait aucune exigence de taux de reponse; et la derniere observation disponible est une BAISSE (77 % au T1 2023, 73,7 % au T3 2025) alors que le controle est en place.","routes":["EXPAND","LINK"],"source_id":"SRC-IN","status":"SATURATED"}
LED-002 | {"evidence_excerpt":"Au 3e trimestre 2025, le taux de collecte [...] s etablit a 60,6 %. Il diminue sur un an (-1,1 point) [...] Le taux de reponse [...] s etablit a 73,7 %","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le producteur publie, dans la note methodologique jointe a chaque publication trimestrielle, les taux de collecte et de reponse de l enquete Emploi et la precision des indicateurs publies.","linked_ids":["FCT-003","FCT-004","FCT-005","CLM-003"],"locator":"evidence/eec_notemetho_T32025.txt (taux de collecte et de reponse par trimestre; precision des principaux indicateurs) ; evidence/eec_notemetho_2023.txt, section 6","materiality":"DECISIVE","note":"La note T3 2025 contient le taux de collecte, le taux de reponse, la part de reponse par internet et une table de precision des principaux indicateurs; la note d aout 2023 contient les memes elements au T1 2023. C est donc un dispositif continu, non un document isole.","routes":["EXPAND","LINK"],"source_id":"SRC-002","status":"SATURATED"}
LED-003 | {"evidence_excerpt":"le taux de collecte [...] s etablit a 60,6 % [...] (-1,1 point) [...] 73,7 %","gap":"","gap_type":"NONE","kind":"EVENT","lead":"La serie de collecte se degrade sur la periode recente: 77 % de reponse au T1 2023, 73,7 % au T3 2025, avec une baisse de la collecte de 1,1 point sur un an au T3 2025.","linked_ids":["FCT-001","FCT-003","CAU-003"],"locator":"comparaison des deux notes methodologiques (T1 2023 et T3 2025)","materiality":"IMPORTANT","note":"Le point est dechronologique pour la question causale: le mouvement observe va a l encontre de l objectif que le Comite dit saluer (maintien et amelioration des taux de reponse), et aucune source ne relie ce mouvement au controle.","routes":["EXPAND"],"source_id":"SRC-001,SRC-002","status":"SATURATED"}
LED-004 | {"evidence_excerpt":"l ASP decide de suspendre [...] la labellisation de ces series pour la periode restant a courir entre le 1er janvier 2025 et le 20 mai 2026","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Un controle externe de la statistique publique a produit un effet documente, date et borne sur le STATUT DE PUBLICATION: la suspension de la labellisation des series de demandeurs d emploi inscrits.","linked_ids":["FCT-007","CAU-001","CLM-002","CTRL-001"],"locator":"evidence/asp_rapport_2024.txt, delibere reproduit p.136 et section 2.4.4","materiality":"DECISIVE","note":"C est la seule forme d effet causal du controle que le corpus permet d etablir: l effet porte sur le statut (labellise / non labellise) et sur une periode explicite (1er janvier 2025 - 20 mai 2026), pas sur la valeur des indicateurs ni sur les taux de reponse.","routes":["EXPAND","LINK"],"source_id":"SRC-003","status":"SATURATED"}
LED-005 | {"evidence_excerpt":"la qualite des donnees issues des enquetes sur les forces de travail produites par les instituts statistiques nationaux est controlee par Eurostat","gap":"","gap_type":"NONE","kind":"OBJECT","lead":"Une analyse independante du Service statistique public sur la qualite et la precision des indicateurs conjoncturels existe et est inspectable: rapport annuel de l Autorite de la statistique publique (hors Insee) et commission d enquete du Senat.","linked_ids":["FCT-009","FCT-010","CLM-004","AXS-009"],"locator":"evidence/asp_rapport_2024.txt ; evidence/senat_r16-003_ch4.txt","materiality":"DECISIVE","note":"Deux familles non-Insee obtenues: D (autorite de controle independante) et B (commission d enquete parlementaire). Elles ne contredisent pas la precision publiee, elles l engagent (limites, incident de publication du T1 2013, ecarts entre sources, contestations de population).","routes":["EXPAND","LINK"],"source_id":"SRC-003,SRC-005","status":"SATURATED"}
LED-006 | {"evidence_excerpt":"Jusqu au deuxieme trimestre 2024, le nombre de beneficiaires du RSA etait nettement sous-estime dans l enquete Emploi [...] le taux de couverture [...] peut etre estime a 90 %","gap":"","gap_type":"NONE","kind":"EVENT","lead":"Une erreur de mesure d un indicateur publie est documentee et reparee par le producteur: la couverture des beneficiaires du RSA dans l enquete Emploi.","linked_ids":["FCT-006","CAU-002"],"locator":"evidence/eec_notemetho_T32025.txt, section La mise en oeuvre de la loi sur le plein emploi: mesure de l impact","materiality":"IMPORTANT","note":"Cas le plus proche d une chaine causale documentee sur la qualite: un defaut de questionnaire (sous-estimation) est identifie, corrige, et la serie passee est retraitee par appariement administratif puis calage. L attribution de l amelioration au controle externe reste non etablie.","routes":["EXPAND"],"source_id":"SRC-002","status":"SATURATED"}
LED-007 | {"evidence_excerpt":"l ecart grandissant, releve par certains chercheurs, entre les sources administratives sur l emploi et le nombre d actifs occupes issu de l enquete Emploi","gap":"","gap_type":"NONE","kind":"CONTEXT","lead":"Le producteur et l autorite de controle documentent des contestations externes de resultats publies (populations, ecart entre sources d emploi) et leurs reponses.","linked_ids":["FCT-009","CLM-004"],"locator":"evidence/asp_rapport_2024.txt (section 2.4.4 et points 2.1/2.5)","materiality":"IMPORTANT","note":"Materiau pour la contre-perspective: l ASP releve que des chercheurs contestent l ecart entre sources administratives d emploi et enquete Emploi, et qu elle-meme a soutenu publiquement la mesure de population contestee en soulignant le manque de justifications methodologiques des contestations.","routes":["EXPAND"],"source_id":"SRC-003","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-001","LED-003","CAU-003"],"proposition":"L effet du controle externe sur les taux de reponse de l enquete Emploi n est pas identifiable a partir des documents publics: aucune source inspectee ne l attribue, le cycle de controle precedent ne comportait aucune exigence de taux de reponse, et les exigences du cycle en cours sont datees 2027 et au-dela.","status":"SUPPORTED","support":"FCT-002, FCT-003, FCT-010 (attributions documentees a d autres causes) ; SRC-004 (aucune exigence de taux de reponse dans le cycle 2021-2025) ; QRY-009 NONE de refutation"}
CLM-002 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-004"],"proposition":"Le controle externe a en revanche produit un effet documente, date et borne sur le statut de publication des series du marche du travail: la suspension de leur labellisation du 1er janvier 2025 au 20 mai 2026.","status":"SUPPORTED","support":"FCT-007 (SRC-003) ; CTRL-001"}
CLM-003 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-002","LED-007"],"proposition":"L incertitude attachee aux indicateurs conjoncturels publies est elle-meme publiee: intervalle de confiance a 95 % de +/- 0,3 point sur le taux de chomage trimestriel, en niveau comme en evolution, et table de precision des principaux indicateurs.","status":"SUPPORTED","support":"FCT-004 (✦, familles A et B: note du producteur et restitution independante par la commission d enquete du Senat) ; FCT-005 ; QRY-009 NONE"}
CLM-004 | {"counter":"NONE_FOUND","gap":"L independance obtenue est institutionnelle (autorite de controle, commission parlementaire) et europenne (controle des rapports qualite); aucune source hostile contestant l intervalle de confiance publie n a ete trouvee, et la critique des ecarts entre sources est relayee par l autorite, non inspectee directement.","gap_type":"INDEPENDENCE","linked_leds":["LED-005","LED-007"],"proposition":"Une perspective independante du producteur existe et engage la precision et la qualite des indicateurs conjoncturels (limites de mesure, incident de publication, ecarts entre sources, contestations).","status":"PARTIAL","support":"FCT-009, FCT-010 (SRC-003, SRC-005) ; QRY-003, QRY-009"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009"],"axis":"SOURCE_AUDIT","links":["LED-001","LED-002","LED-005","CLM-001","CLM-003"],"question":"Quelles pieces documentent les taux de reponse, la precision publiee et le controle externe de l enquete Emploi, et que disent-elles exactement ?","result_ids":["SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010"],"sought_objects":["note methodologique de l enquete Emploi (producteur)","note methodologique de la publication trimestrielle","rapport annuel de l Autorite de la statistique publique","commission d enquete du Senat","avis de conformite du Comite du label (cycle precedent)"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-007","QRY-008","QRY-004","QRY-005"],"axis":"SCOPE_HISTORY","links":["LED-003","LED-006","CAU-003","CAU-004"],"question":"Quelle est l histoire documentee des conditions de collecte et de precision, et quelle place y occupe le controle externe ?","result_ids":["SRC-004","SRC-005","SRC-001","SRC-002","FCT-002","FCT-010"],"sought_objects":["cycle de controle 2020 (validite 2021-2025)","incident de publication du T1 2013","crise sanitaire 2020-2021 et retour a la normale 2022","entree de Mayotte dans l echantillon au T1 2024","renouvellement 2027-2030"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-008","QRY-005","QRY-006"],"axis":"EVIDENCE_CASES","links":["LED-006","LED-007","CAU-002","CAU-004"],"question":"Quel cas documente montre qu une condition de collecte degradee affecte reellement ce qui est publie ?","result_ids":["SRC-005","SRC-002","SRC-003","FCT-006","FCT-009","FCT-010"],"sought_objects":["incident de publication du T1 2013 et ses trois facteurs","sous-estimation puis correction de la couverture des beneficiaires du RSA","divergence entre sources d emploi et enquete Emploi"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":[],"axis":"RESOURCES_FLOWS","gap":"Le cout de la collecte et le financement de l enquete Emploi ne sont pas documentes dans le corpus inspecte; aucun document budgetaire dedie n a ete retrieve.","gap_type":"ACCESS","links":["LED-002"],"question":"Quelles ressources financent la collecte, et comment se comparent-elles au cout d une precision accrue ?","result_ids":[],"sought_objects":["piece budgetaire de l Insee","cout par logement de l enquete Emploi"],"status":"GAP"}
AXS-005 | {"attempt_ids":["QRY-004","QRY-005","QRY-008"],"axis":"MECHANISMS","links":["LED-002","LED-006","CAU-002","CAU-004"],"question":"Par quels mecanismes les conditions de collecte (base de sondage, non-reponse, mode, cadre d emploi des enqueteurs) entrent-elles dans ce qui est publie ?","result_ids":["SRC-001","SRC-002","SRC-005","FCT-001","FCT-004","FCT-006","FCT-010"],"sought_objects":["taux de collecte et taux de reponse definis et publies","correction de la non-reponse a partir de la base de sondage","traitements de correction et retropolation"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-006","QRY-007","QRY-008"],"axis":"ACTORS_RELATIONS","links":["LED-004","LED-005","CTRL-001","CTRL-002","ACT-001","ACT-002","ACT-003"],"question":"Qui produit, qui controle et qui conteste les indicateurs conjoncturels, et avec quels effets observes de chacun ?","result_ids":["SRC-003","SRC-004","SRC-005","FCT-007","FCT-008","FCT-009"],"sought_objects":["Insee (producteur)","Comite du label (avis, suites)","Autorite de la statistique publique (deliberes, labellisation)","Cnis (concertation)","Eurostat (rapports qualite)","chercheurs contestant l ecart entre sources"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-006","QRY-007"],"axis":"RULES_CONTROLS","links":["LED-004","CTRL-001","CTRL-002","CAU-001","CLM-002"],"question":"Quels pouvoirs de controle existent, et lesquels ont un effet documente sur ce qui est publie ?","result_ids":["SRC-003","SRC-004","FCT-007","FCT-008"],"sought_objects":["labellisation et sa suspension (ASP)","avis de conformite et suites exigees (Comite du label)","rapports qualite transmis a Eurostat","obligation de reponse"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-009","QRY-006"],"axis":"IMPACT_RESPONSIBILITY","gap":"L effet mesure du controle externe sur les taux de reponse de l enquete Emploi reste non identifiable (aucune attribution documentee, pas de contrefactuel, exigences datees 2027+); seul l effet sur le statut de publication (labellisation) est etabli.","gap_type":"CAUSALITY","links":["LED-001","LED-003","LED-004","CLM-001","CLM-002"],"question":"Quel effet mesurable le controle externe a-t-il sur les taux de reponse et, a defaut, sur ce qui est publie ?","result_ids":["FCT-007","SRC-004","CAU-001","CAU-003","CLM-001","CLM-002"],"sought_objects":["attribution d une variation des taux a une exigence de controle","serie avant/apres dans un cycle de controle","decision de labellisation et ses motifs"],"status":"GAP"}
AXS-009 | {"attempt_ids":["QRY-003","QRY-008","QRY-009"],"axis":"COUNTER_HYPOTHESES","links":["LED-005","LED-007","CLM-004","AXS-009"],"question":"La precision publiee est-elle contestee, et existe-t-il une perspective opposee documentee sur les indicateurs conjoncturels ?","result_ids":["SRC-003","SRC-005","FCT-004","FCT-009","FCT-010"],"sought_objects":["contestation de l intervalle de confiance publie","critique independante de la mesure du chomage","contestation des estimations de population","ecart entre sources d emploi"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"links":["FCT-007","CTRL-001","CLM-002"],"mechanism":"Decision d une autorite de controle (delibere) -> retrait du statut de labellisation d une serie, motive et borne dans le temps -> effets documentes sur les usages de la serie pendant la periode de suspension","note":"C est l effet causal du controle externe le mieux etabli du corpus: l objet affecte est le STATUT de publication, pas la valeur des indicateurs.","sources":["SRC-003"],"status":"SUPPORTED","type":"MECHANISM"}
CAU-002 | {"links":["FCT-006","CAU-002"],"mechanism":"Conditions de collecte (questionnaire, mode, base de sondage) -> couverture d une population specifique dans l enquete -> correction du questionnaire puis retraitement de la serie passee par appariement administratif et calage","note":"Cas documente d une erreur de mesure identifiee et reparee par le producteur (couverture des beneficiaires du RSA, environ 90 % a partir du T3 2024). L attribution de cette correction au controle externe n est pas etablie.","sources":["SRC-002"],"status":"SUPPORTED","type":"MECHANISM"}
CAU-003 | {"links":["FCT-010","FCT-002","CAU-004"],"mechanism":"Qualite de la base de sondage et conditions de terrain -> non-reponse (dont un accroissement temporaire lie au cadre d emploi des enqueteurs) -> degradation de la mesure -> correction, nouvelle estimation et communications","note":"Incident de publication du T1 2013, avec les trois facteurs identifies par le producteur; c est la chaine causale que le corpus documente le mieux cote conditions de collecte.","sources":["SRC-005","SRC-001"],"status":"SUPPORTED","type":"MECHANISM"}
CAU-004 | {"gap":"Aucune attribution documentee d une variation des taux de reponse a une exigence de controle; le cycle de controle precedent (2020, validite 2021-2025) ne comportait aucune exigence de taux de reponse; les exigences identifiees datent de 2026 pour l exercice 2027-2030, donc posterieures aux variations observees; les variations documentees sont attribuees par le producteur a la crise sanitaire et a des causes operationnelles; aucun contrefactuel n est disponible. La derniere observation disponible est une baisse (77 % au T1 2023, 73,7 % au T3 2025).","gap_type":"CAUSALITY","links":["FCT-001","FCT-003","FCT-002","FCT-010","CLM-001"],"mechanism":"Exigence de controle externe (Comite du label) -> action du service sur la collecte -> variation des taux de reponse","note":"Le gap est ici RESOLU EN TANT QUE QUESTION : la reponse est que l effet n est pas mesurable sur les taux de reponse avec les documents publics, et la raison est etablie (absence d attribution, anteriorite des exigences, absence de contrefactuel). Ce qui reste ouvert est une mesure, pas une verification.","sources":["SRC-001","SRC-002","SRC-004"],"status":"GAP","type":"MECHANISM"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"action":"Suspension de la labellisation des nouvelles series de demandeurs d emploi inscrits (1er janvier 2025 - 20 mai 2026); appel a un suivi et a une analyse des impacts de la loi Pour le plein emploi sur les series BIT; soutien public a la mesure de population contestee en soulignant le manque de justifications des contestations","controller":"Autorite de la statistique publique (ASP), autorite administrative independante chargee du controle du service statistique public","gap":"","gap_type":"NONE","information":"Dossiers du service statistique public, audition du Cnis et de ses commissions, contestations externes","oversight":"EFFET_DOCUMENTE_SUR_LE_STATUT_DE_PUBLICATION","rule":"Labellisation des statistiques publiques; code de bonnes pratiques; pouvoir de suspendre une labellisation et d adresser des observations","sources":["SRC-003"],"status":"SATURATED"}
CTRL-002 | {"action":"Cycle 2021-2025: aucun avis de conformite, prolongation par avis rectificatif du 3 octobre 2025 pour 2026 (aucune exigence relative aux taux de reponse) ; cycle 2027-2030: avis du 30 juin 2026 retenant les taux de reponse comme indicateurs de comparabilite et exigeant des suites","controller":"Comite du label de la statistique publique (Cnis)","gap":"Aucune attribution d une variation des taux de reponse a ce controle","gap_type":"CAUSALITY","information":"Dossier de l enquete, taux de reponse du test 2027, strategie de tests","oversight":"EFFET_NON_ETABLI_SUR_LES_TAUX_DE_REPONSE","rule":"Avis de conformite, label d interet general et de qualite statistique, proposition de caractere obligatoire, publication au Journal officiel, suites exigees","sources":["SRC-004"],"status":"SATURATED"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Suspension de la labellisation des nouvelles series de demandeurs d emploi inscrits du 1er janvier 2025 au 20 mai 2026, avec suivi en lien avec le Cnis","actor":"Autorite de la statistique publique","note":"Action de controle a effet documente et borne; aucune intention imputee.","sources":["SRC-003"],"status":"SATURATED"}
ACT-002 | {"action":"Attire l attention sur l importance d un suivi et d une analyse des impacts de la loi Pour le plein emploi sur les series de taux d activite, d emploi et de chomage au sens du BIT issues de l enquete Emploi","actor":"Autorite de la statistique publique","note":"Exigence de suivi adressee au systeme statistique: c est l exemple d un controle qui agit sur l agenda d analyse, non sur la valeur des indicateurs.","sources":["SRC-003"],"status":"SATURATED"}
ACT-003 | {"action":"Publie a chaque trimestre une note methodologique contenant les taux de collecte et de reponse et la table de precision des principaux indicateurs; a ameliore le questionnaire sur les beneficiaires du RSA et retraite la serie passee par appariement administratif puis calage","actor":"Insee (service producteur)","note":"Actions de production documentees et datees; le declencheur de l amelioration du questionnaire n est pas etabli dans le corpus.","sources":["SRC-001","SRC-002"],"status":"SATURATED"}
ACT-004 | {"action":"Rapporte et documente la precision publiee (+/- 0,3 point), les limites de la mesure locale et l incident de publication du T1 2013","actor":"Commission d enquete du Senat","note":"Perspective de controle parlementaire; restitue les chiffres du producteur sans les contester.","sources":["SRC-005"],"status":"SATURATED"}

SEARCH_ACTIVITY_V1:WEB:4|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND:ligne INSEE (memoires des runs 20260921-0255 et 20260921-0314) + snapshot:v1 subject-fp:3f051dff du parent 0314 (memory_id eb59eda8-0504-4e6a-811f-7cf98b07f11c) | mnemolite.search_memory | http://localhost:8002/mcp | MNEMO_Q
SYS-002 | SYS | FOUND | runtime | eb59eda8-0504-4e6a-811f-7cf98b07f11c | MEMORY_PROBE
SYS-003 | SYS | FOUND | runtime | eb59eda8-0504-4e6a-811f-7cf98b07f11c | HYDRATE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND:10 resultats; deux familles non-Insee identifiees sur la qualite des indicateurs conjoncturels: ASP (rapport annuel 2024, 2025) et Senat (commission d enquete 2016); notes methodologiques EEC identifiees cote producteur | - | - | Autorite de la statistique publique rapport annuel evaluation Insee qualite precision publication indicateurs conjoncturels
QRY-002 | WEB | FOUND:le producteur publie une note methodologique par trimestre attachee a la publication (note aout 2023, note T3 2025) contenant taux de collecte, taux de reponse et precision | - | - | taux de reponse enquete Emploi en continu Insee evolution 2019 2021 2023 2024 non-reponse
QRY-003 | WEB | FOUND:litterature et rapports critiques identifies (Senat r16-003, CNIS rapport 108 cite par la note T3 2025, divergence des sources relevee par des chercheurs et relayee par l ASP) | - | - | biais de non-reponse enquete Emploi France evaluation academique mesure du chomage imprecision
QRY-004 | FETCH | FOUND:673029 octets, HTTP 200, 21 pages, extraction pdftotext -layout (1019 lignes). Sections 6.1 taux de collecte et taux de reponse, 6.2 ponderation, 6.3 precision | SRC-001 | https://www.insee.fr/fr/metadonnees/source/fichier/EEC_note_methodologique_aout_2023.pdf | Note methodologique EEC aout 2023 (non-reponse, ponderation, precision)
QRY-005 | FETCH | FOUND:301133 octets, HTTP 200, extraction pdftotext -layout (370 lignes): taux de collecte et de reponse T3 2025, table par trimestre, precision des principaux indicateurs, couverture RSA | SRC-002 | https://www.insee.fr/fr/statistiques/documentation/Note_methodologique_T32025.pdf | Note methodologique de la publication trimestrielle T3 2025 (taux de collecte, taux de reponse, precision)
QRY-006 | FETCH | FOUND:1905823 octets, HTTP 200, extraction pdftotext -layout (6897 lignes): section 2.4.4, suspension de labellisation, ecart entre sources, contestations de population, appels au suivi des impacts de la loi plein emploi | SRC-003 | https://www.autorite-statistique-publique.fr/wp-content/uploads/2025/03/Rapport-ASP-2024.pdf | Rapport annuel 2024 de l Autorite de la statistique publique
QRY-007 | FETCH | FOUND:203583 octets, HTTP 200, extraction (244 lignes): le cycle de controle precedent (avis initial du 08/10/2020, validite 2021-2025) ne formule aucune exigence relative aux taux de reponse | SRC-004 | https://www.cnis.fr/wp-content/uploads/2025/10/ac-2020-insee-eec-prolongation-2026.pdf | Avis de conformite de prolongation EEC (cycle de controle precedent, avis initial 2020)
QRY-008 | FETCH | FOUND:169806 octets, HTTP 200, 792 lignes de texte: la commission restitue independamment l intervalle de confiance a 95 % (+/- 0,3 point, en niveau comme en evolution), documente l incident de publication du T1 2013 (dont accroissement temporaire de la non-reponse) et les limites de la mesure locale | SRC-005 | https://www.senat.fr/rap/r16-003/r16-0034.html | Senat, rapport de commission d enquete n 16-003 (2016), chapitre II: l enquete Emploi, sa precision et ses limites
QRY-009 | WEB | NO_RESULT:aucune source ne conteste l intervalle de confiance publie (+/- 0,3 point, +/- 1,0 point pour les 15-24 ans) ni ne propose une autre valeur; la nuance trouvee est interne au producteur et a la commission (le milieu de l intervalle est plus probable), consignee dans le fait lui-meme | - | - | REFUTATION intervalle de confiance 95 % taux de chomage enquete Emploi +/- 0,3 point 1,0 point 15-24 ans contestation autre chiffre methode de calcul contestee

## EVIDENCE_REGISTRY
SRC-001 | ◉ | fam:A | https://www.insee.fr/fr/metadonnees/source/fichier/EEC_note_methodologique_aout_2023.pdf
SRC-002 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/documentation/Note_methodologique_T32025.pdf
SRC-003 | ◈ | fam:D | https://www.autorite-statistique-publique.fr/wp-content/uploads/2025/03/Rapport-ASP-2024.pdf
SRC-004 | ◈ | fam:D | https://www.cnis.fr/wp-content/uploads/2025/10/ac-2020-insee-eec-prolongation-2026.pdf
SRC-005 | ◉ | fam:B | https://www.senat.fr/rap/r16-003/r16-0034.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.insee.fr/fr/metadonnees/source/fichier/EEC_note_methodologique_aout_2023.pdf | A | 2023-08 | eec-taux-collecte-et-taux-reponse-T1-2023 | Definitions et niveaux au T1 2023 (champ France hors Mayotte): le taux de collecte rapporte les logements repondants a l ensemble de l echantillon et vaut 64 %; le taux de reponse rapporte les logements repondants aux logements dans le champ et vaut 77 %. L ecart est eleve parce que l echantillon comporte des residences non principales, dont le statut hors champ est souvent confirme sur le terrain | e19bd438-9794-4f88-81b1-a47b6fa66e8e
FCT-002 | FACT | ✧ | https://www.insee.fr/fr/metadonnees/source/fichier/EEC_note_methodologique_aout_2023.pdf | A | 2023-08 | eec-collecte-affectee-par-la-crise-puis-retour-2022 | La collecte a ete fortement affectee a partir de la fin du T1 2020 (deplacements de terrain impossibles, entretiens en face-a-face convertis en telephone quand les coordonnees etaient disponibles); depuis le T1 2022, le taux de collecte a retrouve son niveau d avant crise sanitaire | bcf6304d-4489-49cf-87b9-1688abf2c72b
FCT-003 | FACT | ✧ | https://www.insee.fr/fr/statistiques/documentation/Note_methodologique_T32025.pdf | A | 2025-11-13 | eec-taux-collecte-et-reponse-T3-2025 | Au T3 2025: taux de collecte 60,6 %, en baisse de 1,1 point sur un an (-1,2 point hors Mayotte, departement entre dans l echantillon au T1 2024); taux de reponse 73,7 %; part de reponse par internet parmi les reinterrogations 46,4 % | f8c3301b-b5ae-4e89-81e9-69ffcff82b0d
FCT-004 | FACT | ✦ | https://www.insee.fr/fr/statistiques/documentation/Note_methodologique_T32025.pdf | A,B | 2025-11-13 | eec-intervalle-de-confiance-publie-et-restitue-independamment | L intervalle de confiance a 95 % du taux de chomage trimestriel est publie par le producteur et vaut +/- 0,3 point, en niveau comme en evolution d un trimestre sur l autre (un taux mesure a 10,0 % a 95 % de chances d etre compris entre 9,7 % et 10,3 %); la commission d enquete du Senat restitue independamment la meme valeur (+/- 0,3 point, en niveau comme en evolution) et la nuance du producteur (le milieu de l intervalle est plus probable) | a304c931-3b04-468e-9fe7-8499a15f37a7
FCT-005 | FACT | ✧ | https://www.insee.fr/fr/statistiques/documentation/Note_methodologique_T32025.pdf | A | 2025-11-13 | eec-table-de-precision-des-principaux-indicateurs | La note publie une table de precision des principaux indicateurs non corriges des variations saisonnieres au T3 2025, par sexe et par classe d age (niveau, precision a 95 % en point, intervalle de confiance), pour le chomage, le halo autour du chomage et l emploi | d8078d11-2fc3-4e6d-aa44-70c493f6f92d
FCT-006 | FACT | ✧ | https://www.insee.fr/fr/statistiques/documentation/Note_methodologique_T32025.pdf | A | 2025-11-13 | eec-sous-estimation-des-bénéficiaires-du-RSA-et-correction | Le nombre de beneficiaires du RSA etait nettement sous-estime dans l enquete Emploi jusqu au T2 2024; a partir du T3 2024, une amelioration du questionnaire porte le taux de couverture des beneficiaires parmi les menages ordinaires a environ 90 %; la serie passee est corrigee par appariement individuel avec le dispositif administratif Pasrau (sur 90 % des personnes identifiees, pour eviter une rupture) puis calage sur l indicateur publie par la DREES | e8b973fc-3a7d-4451-a427-c43bd058e37c
FCT-007 | FACT | ✧ | https://www.autorite-statistique-publique.fr/wp-content/uploads/2025/03/Rapport-ASP-2024.pdf | D | 2025-03-14 | asp-suspension-de-la-labellisation-des-series-de-demandeurs-d-emploi | L Autorite de la statistique publique a decide de suspendre la labellisation des nouvelles statistiques de demandeurs d emploi inscrits pour la periode du 1er janvier 2025 au 20 mai 2026, prenant note que leur stabilite et leur interpretabilite ne pourront etre garanties qu a l issue de la periode de transition; elle suivra le dispositif et les etudes en lien avec le Cnis | 82b79206-911f-4d0f-a8da-f3c68de0455c
FCT-008 | FACT | ✧ | https://www.autorite-statistique-publique.fr/wp-content/uploads/2025/03/Rapport-ASP-2024.pdf | D | 2025-03-14 | asp-appel-au-suivi-des-impacts-de-la-loi-plein-emploi-sur-les-series-BIT | L Autorite note que les dispositions de la loi Pour le plein emploi sont susceptibles d induire des variations significatives des series de taux d activite, de chomage et d emploi au sens du BIT etablies et publiees par l Insee a partir de l enquete Emploi, et attire l attention sur l importance d un suivi et d une analyse de ces impacts, en lien avec le Cnis | a336384f-cf59-42d6-bcee-bef177e0d55b
FCT-009 | FACT | ✧ | https://www.autorite-statistique-publique.fr/wp-content/uploads/2025/03/Rapport-ASP-2024.pdf | D | 2025-03-14 | asp-ecart-entre-sources-administratives-et-enquete-emploi | L Autorite releve que l Insee s est penche sur l ecart grandissant, releve par certains chercheurs, entre les sources administratives sur l emploi et le nombre d actifs occupes issu de l enquete Emploi, et juge cette explicitation des sources de divergence importante a un moment ou le micro-entreprenariat, l apprentissage ou le cumul emploi-retraite complexifient l appréhension du marche de l emploi; l Autorite a par ailleurs soutenu publiquement la mesure contree de la population, en soulignant le manque de justifications methodologiques des contestations | 41c7ee98-cf40-4c5f-ba99-842e4e40e6bf
FCT-010 | FACT | ✧ | https://www.senat.fr/rap/r16-003/r16-0034.html | B | 2016-10-04 | senat-incident-de-publication-T1-2013-et-limites-de-la-mesure | La commission d enquete du Senat documente un incident de publication: pour le T1 2013, trois facteurs ont ete identifies par l Insee (refonte de la chaine des traitements informatiques, accroissement temporaire de la non-reponse en lien avec le deploiement du nouveau cadre d emploi des enqueteurs, renovation du questionnaire); une estimation du taux de chomage du T1 2013 a ete realisee en juin 2013 puis deux communications ont suivi (septembre 2013, mars 2014 avec retropolation). Elle documente aussi que les taux de chomage locaux sont des estimations hybrides (enquete Emploi et demandeurs d emploi inscrits), non estampillees BIT, et que la mesure du chomage BIT ne renseigne pas sur le halo, la qualite de l emploi ou l inactivite | 58589655-de0e-4cb0-898e-9bb2f1a3c540
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-002,SRC-005
FCT-005 | SRC-002
FCT-006 | SRC-002
FCT-007 | SRC-003
FCT-008 | SRC-003
FCT-009 | SRC-003
FCT-010 | SRC-005

## REFUTATION_REGISTRY_V1
FCT-004 | QRY-009 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE
FCT-010 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -
FCT-010 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL:CAU-004 | PASS | LAST_COMPLETED:11:CAU-004 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T02:22:20.609628+00:00","fact_mem":{"FCT-001":"e19bd438-9794-4f88-81b1-a47b6fa66e8e","FCT-002":"bcf6304d-4489-49cf-87b9-1688abf2c72b","FCT-003":"f8c3301b-b5ae-4e89-81e9-69ffcff82b0d","FCT-004":"a304c931-3b04-468e-9fe7-8499a15f37a7","FCT-005":"d8078d11-2fc3-4e6d-aa44-70c493f6f92d","FCT-006":"e8b973fc-3a7d-4451-a427-c43bd058e37c","FCT-007":"82b79206-911f-4d0f-a8da-f3c68de0455c","FCT-008":"a336384f-cf59-42d6-bcee-bef177e0d55b","FCT-009":"41c7ee98-cf40-4c5f-ba99-842e4e40e6bf","FCT-010":"58589655-de0e-4cb0-898e-9bb2f1a3c540"},"mnemo_row":"PASS: 10/10 eligible facts persisted via MCP write_memory (8002) + 1 investigation memory (0cd575fb-2cef-4236-8093-786bce0f3bfe); no duplicate_warning; run 20260921-0347-insee-effet-controle-externe-et-analyse-independante","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-010","reason":"NONE","success":1}],"writeback_row":{"attempted":10,"blocked":0,"eligible":10,"failure":0,"success":10}}

PERSISTENCE_META: MNEMO_ROW:PASS: 10/10 eligible facts persisted via MCP write_memory (8002) + 1 investigation memory (0cd575fb-2cef-4236-8093-786bce0f3bfe); no duplicate_warning; run 20260921-0347-insee-effet-controle-externe-et-analyse-independante | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:10;attempted:10;success:10;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[10 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-010 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
