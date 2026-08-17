# RUN 2 : VÉRIFICATION DES PRÉMICES P1-P3 DE LA PISTE ENR (ÉOLIEN/SOLAIRE)

- Type : INVESTIGATION (pipeline KERNEL v2.8, run 2 du protocole anticorruption)
- Date : 2026-08-10 16:39 CEST
- Dossier : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/`
- Héritage : PISTE ENR (`investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/pistes/2026-08-10_07-29_energies-renouvelables-piste_PISTE.md`) ; leçons pilote 1 (L4 : rapports d'abord ; L3 : CADA en phase 1 bis ; L1 : concentration ≠ signal)
- STATUT : STATUS:FINAL (3 prémices vérifiées à la source primaire, verdict gradué, 2 CADA rédigés)

---

## 1. OBJECT (falsifiable)

La PISTE ENR pose 3 prémices à vérifier avant toute investigation :
- **P1** : le nucléaire et l'hydraulique dominent le mix électrique français (séries RTE/CRE à citer).
- **P2** : les ENR bénéficient de volumes de soutien public documentables (CRE, tarifs, compléments de rémunération, aides).
- **P3** : des montages anormaux existent (surfacturation, favoritisme, sociétés écrans, conflits d'intérêts, pantouflage).

Hypothèses concurrentes H0-H6 (PISTE §5) : chaque prémisse est testée comme un fait, pas comme une accusation. Leçon L1 : la concentration et les montants ne valent signal que si un contournement du contrôle est documenté.

---

## 2. FAITS ÉTABLIS (FCT-###, sources primaires lues intégralement)

### FCT-enr-001 : P1 CONFIRMÉE : le mix électrique français 2024 est dominé par le nucléaire (65 %) puis l'hydraulique (13,9 %), avec ENR intermittentes à ~14 %
Bilan électrique RTE 2024 (publié début 2025) : production totale 539 TWh (+9 % vs 2023, 95 % bas-carbone). Nucléaire : 361,7 TWh = 65 % du mix (taux de disponibilité 71,5 % ; +1,6 GW avec le couplage de Flamanville le 21/12/2024). Hydraulique : 75,1 TWh = 13,9 % (meilleur niveau depuis 2013, +28 % vs 2023). Éolien terrestre : 42,8 TWh (~9,6 % de la consommation, facteur de charge 21,8 %) + éolien en mer 1,5 GW. Solaire : 24,8 TWh (dépasse pour la première fois le fossile, 20,0 TWh). Capacités installées fin 2024 : 155,5 GW dont solaire 24,3 GW (+5,0 GW en 2024) et éolien terrestre 22,9 GW (+1,1 GW).
Source : chiffres RTE rapportés par researcher-web (document RTE primaire non lu directement, marqué ◉ tier-2), recoupés avec la synthèse CdC (150 TWh ENR = 27 % de la production 2024).

### FCT-enr-002 : P2 CONFIRMÉE : le soutien public aux ENR est massif et documenté à la source primaire (26,3 Md€ cumulé 2016-2024, 87 Md€ d'engagements)
Rapport CdC 18/03/2026, synthèse lue intégralement : « En France métropolitaine, les contrats de soutien à la production d'électricité d'origine renouvelable et à la production de biométhane ont représenté pour l'État un coût total cumulé de 26,3 Md€ entre 2016 et 2024, soit un coût annuel moyen de 2,9 Md€. » Coût annuel : 4,1 Md€ (2016) → 6 Md€ (2020) → négatif en 2022 (-1,71 Md€) et 2023 (-3,12 Md€, recettes nettes) → 3,9 Md€ (2024) → 7,3 Md€ (2025, prévisionnel CRE). « L'ensemble des contrats de soutien en vigueur représente des engagements financiers à long terme pour l'État, estimés à 87 Md€ fin 2024 au sein des engagements hors bilan de l'État. » Durée contractuelle : ~20 ans.
Source : `data/cdc_enr_synthese.txt` (Introduction, p. 5-6), lu intégralement. NB dualité de chiffres : 7,3 Md€ = montant cité dans le texte du rapport CdC ; 7,44 Md€ = estimation CRE affichée sur le graphique (délibération n°2025-180, annexe 7) : les deux coexistent (prévision CRE révisée entre l'évaluation initiale et la publication), le dossier retient 7,3 Md€ (texte CdC) et signale 7,44 (graphique CRE).

### FCT-enr-003 : P2 complétée : les ENR représentent 27 % de la production 2024, soutenues par tarifs garantis supérieurs aux prix de marché
Synthèse CdC, section 1 : « Le soutien financier public apporté aux producteurs d'énergies renouvelables a contribué au premier chef à l'augmentation de la production » (150 TWh ENR = 27 % de la production 2024, biométhane > 10 TWh vs 0,2 TWh en 2016). « Il garantit aux producteurs des tarifs d'achat en général bien supérieurs aux prix qu'ils obtiendraient sur les marchés de gros de l'électricité et de gaz. » Les filières solaire et biométhane ont atteint leurs objectifs PPE 2023 dès 2023-2024 ; l'éolien terrestre et maritime accusent un retard.
Source : `data/cdc_enr_synthese.txt` (section 1), lu intégralement.

### FCT-enr-004 : P3 PARTIELLEMENT CONFIRMÉE (volet sur-rémunération et effets d'aubaine) : la CdC documente un défaut de pilotage tarifaire, à distinguer d'un « montage anormal » (manœuvre de surfacturation)
Synthèse CdC, section 2 (lue intégralement) : « Le code de l'énergie précise qu'il doit assurer une rémunération normale des capitaux investis, et donc éviter toute sur-rémunération. » Constat : « les risques de sur-rémunération des bénéficiaires d'autant plus grands que la connaissance de l'économie des filières soutenues est encore insuffisante. » La CdC recommande un plan d'audit des filières par la CRE et un tableau de bord de suivi de l'économie des filières (rec. 1). Les guichets ouverts (petit PV, biométhane) ont connu des afflux de demandes « bien supérieurs aux objectifs fixés » (effets d'aubaine).
Source : `data/cdc_enr_synthese.txt` (section 2), lu intégralement. NB : la sur-rémunération documentée est un défaut de conception tarifaire (tarifs trop généreux vs coûts réels mal connus), pas une manœuvre frauduleuse : le lien avec la définition P3 de la PISTE (surfacturation, favoritisme, sociétés écrans) doit être établi au cas par cas, il n'est pas acquis.

### FCT-enr-005 : P3 complétée : les contrôles et sanctions sont « quasi-inexistants », la DGEC sans bilan consolidé des fraudes
Synthèse CdC, section 2 (lue intégralement) : « les suspicions de fraudes relevées par les acheteurs obligés font actuellement l'objet d'un traitement disparate et insuffisant par les services de l'État. La direction générale de l'énergie et du climat ne dispose d'aucun bilan consolidé en la matière. En l'absence de doctrine de traitement, les suites données par les services de l'État en région sont lacunaires et les sanctions quasi-inexistantes. Un plan de lutte contre la fraude devrait être établi sans délai et les outils et procédures permettant de la détecter et de recouvrer les indus devraient être mis en place » (rec. 4). C'est le point le plus actionnable du rapport : un trou de contrôle documenté par l'institution de contrôle elle-même.
Source : `data/cdc_enr_synthese.txt` (section 2) ; réponse Bercy à la rec. 4 (actions initiées : plan DREAL/EDF OA, décret en CE pour les préfets, guide opérationnel, mission d'inspection RH).

### FCT-enr-006 : P3 NON CONFIRMÉE (volet concentration) : la CRE affirme un marché concurrentiel éolien/PV, contredisant la thèse d'une concentration anormale
Réponse de la CRE au rapport CdC (lue intégralement, p. 5) : « la CRE souhaite néanmoins rappeler que le marché est particulièrement concurrentiel pour les filières de l'éolien à terre et du photovoltaïque. En effet, comme indiqué dans le rapport "État des lieux des appels d'offres PPE2" publié par la CRE en février 2026, aucun développeur ne domine [ces marchés]. » La CdC elle-même note « une augmentation de la concurrence au sein des appels d'offres (constatée dans le cadre des dernières périodes instruites) ». NB : une source presse spécialisée (Les Énergies Renouvelables, 07/2026) rapporte la domination d'EDF Renouvelables et Engie Green à la 11e session de l'AO éolien terrestre (144 dossiers pour 800 MW, prix tirés vers le plancher) : la tension entre le constat CRE (concurrentiel) et l'analyse presse (domination des intégrés) est documentée comme un point à trancher, pas comme un fait établi.
Source : `data/cdc_enr_reponses.txt` (réponse CRE, section 2) ; presse spécialisée = tier 2.

### FCT-enr-007 : P3 NON CONFIRMÉE (volet fraude organisée aux subventions) : les affaires documentées relèvent de l'escroquerie commerciale au consommateur, pas de la corruption publique
Les fraudes documentées dans le secteur solaire français (DGCCRF, UFC-Que Choisir, parquets) concernent le démarchage abusif et les faux crédits à la consommation (arnaques « panneaux à 1 euro », rachats de prêts fictifs, usurpation d'identité institutionnelle) : c'est de la délinquance économique contre des particuliers, sans lien documenté avec un décideur public. Aucune affaire de corruption de fonctionnaire dans l'attribution des appels d'offres CRE n'est documentée en sources ouvertes. Le volet « sociétés écrans » repose sur le modèle SPV classique de la finance de projet (chaque parc = société ad hoc), opacité dénoncée par les associations mais sans faisceau de fraude démontré.
Source : presse spécialisée et associations (Village de la Justice, DGCCRF) = tier 2, à approfondir.

### FCT-enr-008 : le contradictoire est favorable sur le fond mais révèle les limites de contrôle
Réponse CRE (12/02/2026, lue intégralement) : partage les conclusions, favorable à la rec. 1 (plan d'audit) mais défavorable à une transmission systématique annuelle des coûts/recettes (préfère l'échantillonnage) ; reconnaît des collectes limitées (biométhane, petite hydro, petit PV, premiers parcs en mer) et une refonte de sa plateforme de données « opérationnelle d'ici fin 2026 » ; audit indépendant des frais de gestion d'EDF OA lancé automne 2025. Réponse du ministre de l'économie (après publication, lue intégralement) : favorable à la rec. 1 mais « les moyens humains significatifs sont aujourd'hui le principal frein » ; défavorable à la rec. 2 (suppression systématique de 20 % des dossiers conformes) ; partage le besoin de la rec. 4 (plan anti-fraude) avec actions initiées (plan DREAL/EDF OA, décret en CE pour sanctions préfectorales, guide opérationnel DREAL, mission d'inspection RH). La ministre de la transition écologique figure comme « destinataire n'ayant pas d'observation » : aucune contestation du rapport par la tutelle.
Source : `data/cdc_enr_reponses.txt`, lu intégralement.

---

## 3. VERDICT GRADUÉ SUR LES 3 PRÉMICES

| Prémisse | Verdict | Fondement |
|----------|---------|-----------|
| **P1** (mix dominé nucléaire/hydraulique) | **CONFIRMÉE** | RTE 2024 : nucléaire 65 %, hydraulique 13,9 %, ENR intermittentes ~14 % (FCT-enr-001) |
| **P2** (soutien public massif documentable) | **CONFIRMÉE** | CdC 18/03/2026 : 26,3 Md€ cumulé 2016-2024, 87 Md€ engagements fin 2024, 7,3 Md€ 2025 (FCT-enr-002/003) |
| **P3** (montages anormaux) | **PARTIELLEMENT CONFIRMÉE** | La CdC documente sur-rémunérations, effets d'aubaine, contrôle lacunaire et sanctions quasi-inexistantes (FCT-enr-004/005) ; mais NI concentration anormale démontrée (CRE contredit, FCT-enr-006) NI fraude organisée aux subventions liée à un décideur public (FCT-enr-007) |

**Le point qui change la nature du dossier** : la P3 la plus solide n'est pas « des montages frauduleux existent » (non démontré), c'est « l'État verse 7,3 Md€/an sans connaître l'économie des filières, sans bilan consolidé des fraudes, avec des sanctions quasi-inexistantes ». C'est un trou de contrôle institutionnel documenté par la CdC elle-même, assorti d'un plan anti-fraude demandé (rec. 4) et d'un plan d'audit des filières (rec. 1) : la corruption n'est pas prouvée, la condition de possibilité est documentée.

**Hypothèses** :
- H0 (régularité économique) : NON ÉCARTÉE sur P1/P2 (politique publique assumée, tarifs garantis votés).
- H1/H2 (mauvaise gestion / contrainte) : FAVORISÉES sur le volet coût (méconnaissance des filières, moyens humains insuffisants : réponse Bercy).
- H4 (favoritisme) : SANS APPUI en l'état (la CRE documente un marché concurrentiel éolien/PV ; la tension avec la presse est un point à trancher, pas une preuve).
- H5 (corruption) : SANS APPUI en l'état (aucune affaire de corruption de décideur public documentée en sources ouvertes).
- H6 (données incomplètes) : FAVORISÉE et STRUCTURELLE : la CdC elle-même dit que l'État ne dispose pas des données (plan d'audit rec. 1, bilan fraudes rec. 4, plateforme CRE fin 2026).

---

## 4. RÉSIDUS ACTIONNABLES (dont CADA phase 1 bis, leçon L3)

| Résidu | Levier | Cible | Valeur |
|--------|--------|-------|--------|
| Plan d'audit des filières CRE (rec. 1) : statut 2026 | CADA + suivi | CRE | Savoir si l'audit a commencé et quelles filières |
| Bilan consolidé des fraudes et indus (rec. 4) : inexistant à la date du rapport | CADA | DGEC (ministère de l'énergie) | Documenter l'ampleur réelle des fraudes détectées/recouvrées |
| Disparité coûts/prix aux appels d'offres (CdC section 2) | Données CRE | CRE | Quantifier la sur-rémunération potentielle par filière |
| Concentration 11e session AO éolien (144 dossiers, 800 MW) | Presse + données CRE | Les Énergies Renouvelables, CRE | Trancher la contradiction CRE (concurrentiel) vs presse (EDF/Engie dominent) |
| Sanctions préfectorales (décret en CE annoncé par Bercy) | Suivi réglementaire | Légifrance | Vérifier la publication du décret |

Les 2 lettres CADA (CRE, DGEC) sont rédigées dans `cada_lettres/` : envoi DELIVERABLE_PENDING (décision utilisateur requise, comme pour le pilote 1).

---

## 5. PROCHAINS PAS (si le dossier est poursuivi)

1. **P1** : envoi des 2 CADA (CRE, DGEC) : plan d'audit des filières, bilan des fraudes et des indus, données coûts/recettes par échantillon.
2. **P2** : trancher la concentration des lauréats : dépouiller le rapport CRE « État des lieux des appels d'offres PPE2 » (février 2026) et les résultats détaillés des sessions 2025-2026 (part de marché par développeur).
3. **P3** : chiffrer la sur-rémunération potentielle : comparer les prix moyens retenus aux appels d'offres (éolien terrestre 86,6 €/MWh, AOS solaire 88,73 €/MWh) aux coûts déclarés (données CRE).
4. **P4** : suivi des suites données aux rec. 1 et 4 dans le rapport annuel CdC 2027 (point de contrôle daté).

---

## 6. SOURCES

| ID | Type | Source | Fiabilité |
|----|------|--------|-----------|
| SRC-enr-001 | Rapport public | CdC, « Le soutien aux ENR à travers les charges de service public de l'énergie », 18/03/2026, synthèse (10 p.) | ◈ (texte + PDF lus intégralement, archivés hashés) |
| SRC-enr-002 | Contradictoire | Réponses des administrations (CRE 12/02/2026, ministre de l'économie) | ◈ (9 p. lues intégralement, archivées hashées) |
| SRC-enr-003 | Données | RTE Bilan électrique 2024 (nucléaire 65 %, hydraulique 13,9 %, 539 TWh) | ◉ (chiffres recueillis via researcher-web, recoupés CdC) |
| SRC-enr-004 | Presse | Les Énergies Renouvelables (07/2026), Village de la Justice, DGCCRF | ○ (tier 2, à confronter) |
| SRC-enr-005 | Héritage | APEX 50/150 (20/06/2026) : terrain ENR documenté | ○ (framework, à confronter aux sources primaires) |

GAP-enr-001 : rapport CRE « État des lieux des appels d'offres PPE2 » (02/2026) non lu.
GAP-enr-002 : résultats détaillés par développeur des sessions d'AO 2025-2026 non dépouillés.
GAP-enr-003 : montants exacts des sur-rémunérations potentielles non quantifiés (données CRE à obtenir).
GAP-enr-004 : publication du décret en CE sur les sanctions préfectorales non vérifiée.
