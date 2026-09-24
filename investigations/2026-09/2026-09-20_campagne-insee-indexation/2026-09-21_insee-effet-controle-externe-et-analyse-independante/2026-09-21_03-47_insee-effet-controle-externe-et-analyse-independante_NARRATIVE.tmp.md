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
