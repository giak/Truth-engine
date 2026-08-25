# KERNEL INVESTIGATION: Le travail sous IA, fresque systémique (atomes A1-A12)

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-24-1800-TRAVAIL-SOUS-IA-FRESQUE |
| Type | KERNEL APEX (16/18) |
| RUN_ID | 20260824-1800-travail-sous-ia-fresque-systemique |
| Loup parent | Fresque IA-salariat (point d'étape 24/08, framework DECOMPOSE A1-A12 + SHADOW) |
| Date | 2026-08-24 |
| INPUT_KIND | TOPIC |
| MISSION_MODE | INVESTIGATION |
| Sources consultées | ~40 (dont 34 dossiers du corpus parent) |
| Faits enregistrés | 20 nouveaux (9 ancrés/écrits + 11 snippets ⁅) |
| Gate | PASS (déterministe, worktree te-travail-ia-20260824, 19a + 19b) |
| STATE_ID | sha256:bee7c9c2dc97a86ab701557c59a5328c8115ac447ade0a05dab5c4e35693ff48 |
| Mémoires écrites | 9 faits (VERIFIE) |

---

## 1. RÉSUMÉ EXÉCUTIF

**OBJECT_QUESTION :** l'IA remplace-t-elle le travail, et quelles sont les conséquences concrètes pour le monde du travail ?

**Réponse bornée :** les 12 atomes du framework sont résolus : **A1 (remplacement massif) est RÉFUTÉ à l'échelle agrégée** mais vérifié dans ses formes émergentes ; **A2 (tâches/non-remplacements/juniors) est le mécanisme dominant documenté** ; **A3 (salaires/productivité) est VÉRIFIÉ avec le résultat le plus contre-intuitif du corpus** : l'automatisation est utilisée pour contrôler les salaires, pas pour maximiser la productivité (Acemoglu, QJE 2026 : 52 % de la croissance de l'inégalité 1980-2016, 60-90 % des gains de productivité annulés) [FCT-105, FCT-106] ; **A4 (le récit sert des intérêts) est VÉRIFIÉ** avec la preuve HBR : les licenciements sont « presque entièrement par anticipation de l'impact de l'IA », le potentiel, pas la performance [FCT-108] ; **A5 (microtravail) est VÉRIFIÉ** : 154 à 435 millions de travailleurs de plateforme (Banque mondiale), convention ILO n° 193 adoptée le 12 juin 2026 [FCT-111, FCT-112] ; **A6 (surveillance/sélection) est VÉRIFIÉ** : AI Act en application depuis août 2026, emploi = catégorie à haut risque [FCT-113] ; **A7 (inégalités) est VÉRIFIÉ** : les jeunes de 22-25 ans en métiers exposés à -13 % depuis 2022 (Dallas Fed), -19 % sous la tendance (Stanford), les femmes 10 % à haut risque vs 3,5 % des hommes (ILO) [FCT-114, FCT-115, FCT-116] ; **A8 (psychologie) est VÉRIFIÉ** : usage passif de l'IA = -20 % de propriété psychologique, -10 % de sens, effets persistants (Penn State, Scientific Reports) [FCT-101] ; **A9 (rapport de force capital-travail) est VÉRIFIÉ** : part du travail au plus-bas historique US (BLS via Axios) [FCT-103] ; **A10 (coût chinois) est VÉRIFIÉ** (cf. INV bulle-IA : DeepSeek V4, prix 8-10× inférieurs) ; **A11 (causes alternatives) est VÉRIFIÉ** : les attributions à l'IA sont en partie du « corporate fiction » (Fortune : 55 000 coupes attribuées sur 1,2 million de licenciements US 2025, ~4,5 %) [FCT-120] ; **A12 (emplois créés) est VÉRIFIÉ avec un ratio défavorable** : 3 000-7 000 emplois de construction temporaires contre 200-500 emplois permanents par campus de data center [FCT-117].

**La structure en trois lentilles (ce qui est mesurable / ce qui sort des statistiques / ce qu'on fait croire) :**

1. **Mesurable :** pas d'effondrement agrégé. L'emploi US tient (chômage bas), la productivité moyenne ne décolle pas (paradoxe de Solow réactivé par Acemoglu : « you can reduce costs while reducing productivity ») [FCT-106]. Les effets mesurables sont concentrés : jeunes en début de carrière, fonctions support, métiers exposés.

2. **Ce qui sort des statistiques :** non-remplacements (6 000 requisitions annulées chez Meta), gel d'embauche (IBM), non-backfill (Salesforce), réaffectations internes (7 000 chez Meta), microtravail hors salariat (154-435 M de personnes), sous-traitance algorithmique. Le licenciement est l'événement visible d'un mécanisme dont l'essentiel est l'absence.

3. **Ce qu'on fait croire :** le récit « l'IA remplace massivement » est simultanément surjoué (55 000 attributions sur 1,2 M de licenciements : 4,5 %) et sous-joué (les réductions réelles liées au potentiel de l'IA ne sont pas nommées comme telles par les dirigeants : déni Zuckerberg/Intuit). La thèse HBR tranche : les coupes sont réelles mais anticipatoires, fondées sur le potentiel, pas la performance [FCT-108]. C'est la définition exacte de l'effet performatif : l'attente produit la décision.

**Verdict d'ensemble :** l'IA ne détruit pas encore massivement le travail (A1 réfuté), mais elle le transforme à travers cinq mécanismes documentés : (1) la réallocation payroll→capex (INV XQ-C), (2) le non-remplacement, (3) le contrôle des salaires via l'automatisation ciblée (Acemoglu), (4) le déplacement vers le microtravail et les plateformes (A5), (5) la surveillance et la sélection algorithmiques (A6). La conséquence la plus profonde n'est pas le chômage : c'est la **redistribution de la valeur et du risque** (A9 : part du travail au plus-bas) et la **redéfinition psychologique du travail** (A8 : sens, autonomie, compétence).

---

## 2. MANIPULATION_REPORT

| Symbole | Score /10 | Observation |
|---------|-----------|-------------|
| Ξ Omission | 8 | Les non-remplacements, gels, réaffectations et microtravail sont absents des statistiques d'emploi ; la productivité est mesurée à l'échelle macro, pas au niveau des tâches automatisées |
| € Money | 8 | La réallocation payroll→capex (Meta 125-145 Md$ vs 3-8 Md$ d'économies) ; le contrôle des salaires comme motif d'automatisation (Acemoglu) |
| Λ Framing | 8 | « Efficiency », « year of efficiency », « augmentation » vs « remplacement » : le vocabulaire décide du débat ; les dirigeants nient l'IA quand ils licencient et la vantent aux investisseurs |
| Ω Inversion | 6 | Le récit « l'IA détruit massivement » (vidéastes) inverse le constat mesurable ; le déni managérial inverse la causalité réelle (anticipation) |
| Ψ Sideration | 7 | 71 % de salariés épuisés par l'IA pendant que la part du travail tombe au plus-bas : dissonance entre récit de promesse et vécu |
| ↕ Pouvoir vertical | 8 | L'automatisation cible les primes salariales (Acemoglu) : le management décide de remplacer les salariés les mieux payés, pas les tâches les moins efficaces |
| Φ Spectacle | 5 | Les annonces « l'IA va remplacer des millions d'emplois » (CEO Ford, Amazon, Salesforce, JPMorgan) produisent des effets de marché et de politique |
| Σ Sémio | 7 | « backfill », « requision », « pods », « retraite volontaire » : le lexique efface le licenciement et le remplacement |
| Κ Cynisme | 7 | Les entreprises licencient au nom du potentiel de l'IA (HBR) puis réembauchent « en retraites embarrassantes » (IBM, Klarna, CBA) |
| ρ Résistance | 4 | Convention ILO n° 193 (12 juin 2026), AI Act (août 2026), question Ruffin, poursuite Meta : le contre-pouvoir institutionnel se construit |
| κ Influence subtile | 5 | Les outils IA façonnent les décisions RH (scoring, sélection des licenciés) sans cadre de contrôle effectif documenté |
| ⫸ Convergence | 8 | 12 atomes, 5 mécanismes : la convergence est la plus forte jamais documentée dans le corpus |
| ⚔ Guerre cognitive | 5 | Les mêmes cabinets (McKinsey : 88 % des organisations ont déployé l'IA) vendent la promesse et conseillent les restructurations |
| 🌐 Réseau | 5 | ILO, Banque mondiale, OCDE, BLS, QJE : les institutions produisent les données ; les entreprises produisent le récit |
| ⏰ Temporal | 7 | 2026 = année de bascule : AI Act (août), Convention ILO (juin), part du travail au plus-bas, première correction du cycle capex |

**Chargement des clusters :** €=8 → MONEY, POWER ; Ξ=8 → ICEBERG ; Λ=8 → FRAMING ; ↕=8 → POWER. Clusters chargés : MONEY, POWER, ICEBERG, FRAMING, TEMPORAL.

**Hypothèses d'entrée :** le framework DECOMPOSE A1-A12 de l'utilisateur ; l'analyse croise les 34 investigations du corpus parent (74 faits ancrés) et ~20 nouvelles sources ; période 2023-2026.

---

## 3. CLUSTERS

**MONEY (€=8) :** la réallocation est le cœur : le dollar marginal quitte le payroll pour le compute (Meta, IBM logique 2023), et l'automatisation est un outil de contrôle des salaires (Acemoglu : cibler les primes salariales augmente les profits sans augmenter la productivité). MONEY_FACTOR : part du travail au plus-bas US [FCT-103] ; part du travail européenne en déclin (CEPR) ; -0,5 à -1,6 % de part du travail par doublement de l'innovation IA régionale (Minniti) [FCT-118].

**POWER (↕=8) :** l'asymétrie est double : informationnelle (le management connaît le plan, pas les salariés) et structurelle (l'automatisation cible les salariés à prime salariale, ceux qui négocient le mieux). Le rapport de force capital-travail se déplace sans loi du marché du travail : les institutions (ILO, AI Act) réagissent après coup.

**ICEBERG (Ξ=8) :** la partie visible (55 000 attributions à l'IA sur 1,2 M de licenciements US 2025, 4,5 %) masque : les non-remplacements, les gels, les réaffectations, le microtravail (154-435 M), le contrôle des salaires, la surveillance. Le débat public regarde le chiffre visible et rate le mécanisme.

**FRAMING (Λ=8) :** trois récits concurrents : « l'IA remplace massivement » (vidéastes, CEO), « l'IA augmente » (direction), « ce n'est pas l'IA » (déni). Les trois sont faux partiellement : les coupes sont réelles mais anticipatoires (HBR) [FCT-108] ; le remplacement est ciblé et silencieux, pas massif.

**TEMPORAL (⏰=7) :** 2026 = convergence institutionnelle : AI Act appliqué (août), Convention ILO (juin), part du travail au plus-bas, correction du cycle capex (juillet) : le cadre se construit pendant que le mécanisme s'accélère.

---

## 4. HERMÉNEUTIQUE

| Niveau | Interprétation | Statut |
|--------|----------------|--------|
| L1 | Les chiffres publiés (chômage, part du travail, effectifs, licenciements attribués) | FAIT |
| L2 | Les études causales (Acemoglu QJE, Brynjolfsson QJE, Penn State) | FAIT (méthodes publiées, peer-reviewed) |
| L3 | L'anticipation (HBR) comme mécanisme : le potentiel produit des décisions réelles | FAIT (enquête 1 006 dirigeants) |
| L4 | La redistribution valeur/risque (part du travail ↓) | FAIT (BLS) avec débat causal (IA vs autres facteurs) |
| L5 | « L'IA remplace massivement le travail » | RÉFUTÉ à l'agrégé (4,5 % des licenciements attribués) |
| L6 | « L'IA ne change rien » | RÉFUTÉ (5 mécanismes documentés) |

Faits séparés des inférences : « la part du travail tombe au plus-bas » est un fait (BLS) ; « à cause de l'IA » est une inférence (les économistes débattent, cf. Feroli : « level shift post-pandémie ») ; « l'IA détruit l'emploi » est un récit non étayé à l'agrégé ; « l'IA érode le sens du travail » est un fait expérimental (Penn State) limité à l'usage passif.

---

## 5. FORENSIC REASONING

**Montré :** les études peer-reviewed (QJE, Scientific Reports), les données institutionnelles (BLS, ILO, Banque mondiale, Dallas Fed), les enquêtes dirigeants (HBR, 1 006), les déclarations publiques.
**Omis :** les données micro de chaque entreprise (10-K ligne à ligne, cf. XQ-C) ; les données granulaires de productivité par tâche (hors études isolées) ; la part du microtravail invisible dans les statistiques nationales.
**Reconstruction :** le ratio 154-435 M de travailleurs de plateforme est une fourchette Banque mondiale (2023) reprise par l'ILO et HRW ; le « 19 % sous la tendance » (Stanford) est reconstruit contre un contrefactuel de tendance pré-2022 ; le « 52 % » (Acemoglu) est une estimation économétrique sur données Census/ACS, 500 groupes démographiques, 49 industries.

---

## 6. PRISME DIALECTIQUE

**Thèse dominante (institutionnelle/industrie) :** « l'IA augmente la productivité et crée des emplois (paradoxe de Jevons, income effects) » [SRC-CARNEGIE].
**Thèse critique la plus forte (Acemoglu) :** « l'automatisation est inefficacement ciblée : elle sert à dissiper les rentes salariales, pas à créer de la productivité ; 52 % de la croissance de l'inégalité, 60-90 % des gains de productivité annulés » [FCT-105, FCT-106].
**Thèse sceptique (contre les deux) :** « les effets restent marginaux : 4,5 % des licenciements attribués à l'IA, chômage stable, les réembauches pullulent (IBM, Klarna) » [FCT-108, FCT-120].
**Arbitrage :** la thèse critique est la plus solide scientifiquement (QJE peer-reviewed, données 1980-2016) et la plus explicative des données 2026 (part du travail au plus-bas, contrôle des salaires). La thèse dominante échoue sur le paradoxe de productivité (croissance molle malgré les capex). La thèse sceptique est vraie sur l'ampleur, fausse sur la direction : le mécanisme est réel, sa vitesse est la question. Les trois coexistent : la transformation est lente à l'agrégé, concentrée sur les jeunes/support/femmes, et anticipée par les décideurs.

---

## 7. CHRONOLOGIE

| Date | Événement | Source |
|------|-----------|--------|
| 2023-2024 | Études d'exposition : 28 % des emplois OCDE à risque automatisable ; femmes surreprésentées | [SRC-OECD] |
| 2024-2026 | Acemoglu & Restrepo (QJE) : données 1980-2016, automatisation ciblant les primes salariales | [SRC-MIT] |
| 2025 | Brynjolfsson et al. (QJE) : +15 % de productivité moyenne en support client, forte hétérogénéité | [SRC-QJE] |
| 2025-01 | Fortune : 55 000 licenciements US attribués à l'IA sur 11 mois (75 % des coupes « IA ») ; « corporate fiction » | [SRC-FORTUNE] |
| 2025-11 | Enquête : 71 % des salariés épuisés par l'IA | [SRC-WPO] |
| 2025-12 | McKinsey : 88 % des organisations ont déployé l'IA dans au moins une fonction | [SRC-MCK] |
| 2025-12 | Enquête HBR (1 006 dirigeants) : licenciements par anticipation du potentiel de l'IA | [SRC-HBR] |
| 2026-01-06 | Dallas Fed : 22-25 ans en métiers exposés, -13 % d'emploi depuis 2022 | [SRC-DAL] |
| 2026-03-05 | ILO : les femmes à plus haut risque d'IA générative (10 % vs 3,5 % des hommes) | [SRC-ILOF] |
| 2026-05-07 | MIT : publication QJE « Automation and Rent Dissipation » (52 % inégalité) | [SRC-MIT] |
| 2026-06-05 | Penn State (Scientific Reports) : usage passif de l'IA, -20 % propriété, -10 % sens | [SRC-PSU] |
| 2026-06-12 | ILO adopte la Convention n° 193 « Decent Work in the Platform Economy » | [SRC-ILOC] |
| 2026-07-06 | Stanford SIEPR : « peu de preuves que l'IA cause des pertes d'emploi massives actuellement » | [SRC-SIEPR] |
| 2026-08-01 | AI Act : application (emploi = haut risque) | [SRC-AIACT] |
| 2026-08-06 | Axios/BLS : part du travail US au plus-bas historique | [SRC-AXIOS] |
| 2026-08-12 | Stanford Digital Economy : 22-25 ans exposés, ~19 % sous la tendance | [SRC-STAN] |

---

## 8. DOMAINES

### Économique (A1, A3, A9, A11, A12)
- **A1 réfuté à l'agrégé** : 1,2 M de licenciements US 2025, 55 000 (4,5 %) attribués à l'IA [FCT-120] ; chômage stable, « peu de preuves de pertes massives » (SIEPR) [SRC-SIEPR].
- **A3 vérifié, résultat contre-intuitif** : l'automatisation cible les primes salariales, pas l'inefficience : 52 % de la croissance de l'inégalité 1980-2016, 10 points de pourcentage de remplacement de salariés à prime, 60-90 % des gains de productivité annulés, effets maximaux au 70e-95e percentile de salaire [FCT-105, FCT-106, FCT-107]. La productivité moyenne ne décolle pas (« productivity statistics are fairly pitiful » : Acemoglu). À l'opposé, l'IA générative en support client donne +15 % (Brynjolfsson, hétérogénéité forte) [FCT-110] : la technologie peut produire, le management choisit de l'utiliser pour les salaires.
- **A9 vérifié** : part du travail US au plus-bas (BLS/Axios), « position de négociation du travail nettement dégradée » depuis la pandémie ; rendement du capital « élevé par rapport aux normes historiques » (Feroli, JPMorgan) [FCT-103, FCT-104]. Doubler l'innovation IA régionale réduit la part du travail de 0,5-1,6 % (Minniti, 2025) [FCT-118].
- **A11 vérifié** : les attributions sont en partie « corporate fiction » (Fortune) ; la HBR montre des coupes anticipatoires ; 92 % des entreprises ayant licencié « au nom de l'IA » n'ont pas mesuré de gains ; Yale Budget Lab : les données de demandes d'indemnisation ne montrent pas de vague IA [FCT-120, FCT-108, SRC-YALE].
- **A12 vérifié, ratio défavorable** : par campus de data center : 3 000-7 000 emplois de construction (2-3 ans, temporaires) contre 200-500 permanents [FCT-117] ; construction de DC : 50 Md$ annualisés en avril 2026 (+27 %) [SRC-BIRM] ; les emplois permanents sont une fraction des emplois de chantier.

### Social (A2, A5, A7)
- **A2 vérifié** : non-remplacements (Meta 6 000 requisitions), gels (IBM), non-backfill (Salesforce), réaffectations (Meta 7 000) : cf. INV XQ-C et non-remplacements-France. Le poste disparaît plus facilement que le salarié n'est licencié.
- **A5 vérifié** : 154-435 M de travailleurs de plateforme en ligne (Banque mondiale) ; le travail de plateforme a presque doublé 2016-2021 (ILO) ; Convention ILO n° 193 adoptée le 12 juin 2026 : premier instrument mondial contraignant [FCT-111, FCT-112]. Le microtravail d'annotation est la forme la plus invisible (cf. INV travailleurs-clic).
- **A7 vérifié** : jeunes 22-25 ans en métiers exposés : -13 % d'emploi depuis 2022 (Dallas Fed), ~19 % sous la tendance (Stanford) [FCT-114, FCT-115] ; femmes : ~10 % des emplois à haut risque vs 3,5 % des hommes, 29 % des métiers féminisés exposés (ILO) [FCT-116] ; les sans-diplôme et seniors risquent l'exclusion d'accès (OECD, Lane) ; en pays à bas revenu, exposition faible faute d'infrastructure (Banque mondiale).

### Juridique et régulation (A6)
- **A6 vérifié** : AI Act en application depuis août 2026 : l'emploi (recrutement, évaluation, surveillance) = catégorie à haut risque, obligations de conformité ; interdit le scoring social. La surveillance algorithmique des travailleurs est documentée : Amazon (architecture intégrée scanners/caméras), ETUI (screening, allocation, sanctions), la surveillance « backfire » (INET : précarité accrue, discrimination) [FCT-113, SRC-AINOW, SRC-ETUI]. La Convention ILO n° 193 couvre les plateformes. La poursuite Meta (IA dans la sélection des licenciés) reste ouverte.

### Psychologique et anthropologique (A8)
- **A8 vérifié** : expérience Penn State (Scientific Reports, ~270 professionnels) : usage passif (copier-coller) = -20 % de propriété psychologique, -10 % d'auto-efficacité, -10 % de sens perçu ; les effets persistent après retour au travail manuel ; satisfaction du résultat -21 % au retour ; pic immédiat de plaisir +29 % (économie d'effort) puis effondrement. L'usage collaboratif ne diffère pas du travail manuel : la modalité d'usage, pas l'outil, décide de l'effet [FCT-101]. 71 % des salariés se disent épuisés par l'IA (enquête) [FCT-119] ; l'exposition augmente les heures et diminue la satisfaction (Hamilton Project) ; technostress et intensification (PMC). Anthropologiquement : l'IA passive dépossède le travailleur de sa compétence (doute sur ses propres compétences) : « they see firsthand that AI can perform a task effectively and could potentially replace them » (Yin).

### Politique et institutionnel (A9, A6)
- La réponse institutionnelle arrive en 2026 : AI Act (cadre), Convention ILO (plateformes), TUC (fiscalité + extension de la négociation collective), débat sur le partage de la valeur. Le rapport de force se joue désormais au niveau de la régulation, pas du marché du travail.

### Narratif et communication (A4)
- **A4 vérifié** : trois registres : (1) surjoué : « l'IA va remplacer des millions d'emplois » (CEO Ford, Amazon, Salesforce, JPMorgan), les vidéastes de la panique ; (2) sous-joué : les dirigeants nient l'IA quand ils licencient (Zuckerberg, Intuit) ; (3) performatif : les licenciements par anticipation du potentiel (HBR). Le récit sert : aux dirigeants, le cadrage « efficiency » ; aux vendeurs d'IA, la promesse ; aux investisseurs, la réallocation payroll→capex.

---

## 9. RÉSEAU D'ACTEURS

| Acteur | Rôle | Position documentée | Documenté par |
|--------|------|---------------------|---------------|
| **Acemoglu / Restrepo (MIT/Yale)** | Scientifiques | L'automatisation dissipe les rentes salariales, 52 % de l'inégalité | [SRC-MIT] |
| **Brynjolfsson et al.** | Scientifiques | +15 % de productivité générative, hétérogénéité | [SRC-QJE] |
| **ILO** | Institution | Convention n° 193 (12/06/2026), données femmes | [SRC-ILOC] |
| **Banque mondiale** | Institution | Fourchette 154-435 M de gig workers | [SRC-ILOC] |
| **BLS / Axios** | Données | Part du travail au plus-bas | [SRC-AXIOS] |
| **Dallas Fed / Stanford** | Données | Jeunes 22-25 : -13 % / -19 % | [SRC-DAL, SRC-STAN] |
| **HBR (Davenport)** | Enquête | Coupes par anticipation du potentiel | [SRC-HBR] |
| **Yin et al. (Penn State)** | Science | Usage passif : sens et propriété érodés | [SRC-PSU] |
| **Entreprises (Meta, Salesforce, IBM...)** | Décideurs | Réallocation payroll→capex, déni, non-backfill | (corpus XQ-C) |
| **Salariés** | Objet | 71 % épuisés ; poursuite Meta ; pétition surveillance | [SRC-WPO] |

**CONTROL_MAP :** points de contrôle : (1) le management (décision d'automatiser, ciblage des salaires) ; (2) les vendeurs d'IA et cabinets (88 % de déploiement, McKinsey) ; (3) les régulateurs (AI Act, ILO) ; (4) les statisticiens publics (BLS, DARES : mesurent les événements, pas les absences) ; (5) les marchés financiers (capex, valorisations).

---

## 10. CHAÎNES / PELOTE

```
CAU-101 (le remplacement par anticipation, cœur de A4/A11) :
  Récit « l'IA va remplacer » (CEO, vidéastes, vendeurs)
  → anticipation du potentiel (HBR : 1 006 dirigeants)
  → coupes et gels réels (Meta, IBM, Intuit)
  → alors que la performance n'est pas démontrée
  → effet performatif : l'attente produit la décision

CAU-102 (le contrôle des salaires, cœur de A3/A9) :
  Automatisation ciblant les primes salariales (Acemoglu)
  → rentes salariales dissipées (70e-95e percentile touchés)
  → profits ↑ sans productivité ↑ (60-90 % des gains annulés)
  → part du travail ↓ (plus-bas BLS)
  → l'automatisation comme arme de négociation, pas de production

CAU-103 (le déplacement hors statistiques, cœur de A2/A5) :
  Licenciement (visible) → non-remplacement, gel, non-backfill (invisible)
  + microtravail/plateformes (154-435 M, hors salariat)
  → la statistique publique mesure les événements, pas les absences
  → le débat public regarde le chiffre visible et rate le mécanisme

CAU-104 (l'érosion psychologique, cœur de A8) :
  Usage passif de l'IA (copier-coller)
  → -20 % propriété, -10 % sens (persistants)
  → doute sur la compétence (« AI can replace me »)
  → aliénation et épuisement (71 %)
  → la modalité d'usage décide : collaboratif ≠ passif

CAU-105 (l'effet de génération, cœur de A7/A2) :
  Automatisation des tâches d'entrée
  → moins de juniors (22-25 : -13 % depuis 2022)
  → pipeline senior rompu (IBM : retournement 2026)
  → inégalités d'âge et de genre (femmes 10 % vs 3,5 %)
  → la facture se paie en début de carrière et sur les métiers féminisés
```

**PELOTE / SOURCE_PROVENANCE :** le « 52 % » et le « 60-90 % » sont des estimations économétriques Acemoglu/Restrepo sur données Census (1980-2016), publiées QJE ; le « 4,5 % » (55 000/1,2 M) vient de l'agrégation des annonces de licenciements (Challenge.gov/Layoffs.fyi via Fortune/EliteBrains) : les attributions déclarées, pas les causes réelles ; le « 19 % sous la tendance » (Stanford) et le « -13 % » (Dallas Fed) sont des mesures contre contrefactuels de tendance ; les 154-435 M sont une fourchette Banque mondiale 2023 reprise sans actualisation.

---

## 11. CARTE DES PREUVES

### LEAD_REGISTRY

| ID | Lead | Statut |
|----|------|--------|
| LED-101 | L'IA remplace le travail (framework DECOMPOSE A1-A12) | SATURATED (12 atomes résolus) |
| LED-102 | Récit « remplacement massif » vs données | SATURATED (4,5 % des licenciements attribués) |
| LED-103 | Effets hors statistiques | SATURATED (non-remplacements, microtravail) |
| LED-104 | Conséquences psychologiques et anthropologiques | SATURATED (Penn State) |
| LED-105 | Redistribution valeur/risque | SATURATED (part du travail, contrôle des salaires) |

### CLAIM_REGISTRY (atomes)

| ID | Claim | Support | Contre | Verdict |
|----|-------|---------|--------|---------|
| A1 | L'IA remplace massivement les emplois | Cas Meta, Salesforce, BT (XQ-C) | 4,5 % des licenciements US 2025 ; SIEPR ; chômage stable | **RÉFUTÉ (agrégé), VÉRIFIÉ (formes émergentes)** |
| A2 | L'effet passe par tâches, non-remplacements, juniors | Meta 6 000 reqs, IBM gel, Salesforce no-backfill, Dallas Fed -13 % | Les licenciements restent le fait visible | **VÉRIFIÉ** |
| A3 | L'IA modifie salaires et productivité | Acemoglu QJE, Brynjolfsson QJE, médiane Meta | Hétérogénéité forte ; pas d'effet agrégé clair | **VÉRIFIÉ (ciblage salarial, pas productivité)** |
| A4 | Le récit sert des intérêts | HBR (anticipation), Fortune (fiction), dénis Zuckerberg/Intuit | Certaines coupes sont de vraies substitutions | **VÉRIFIÉ (performativité)** |
| A5 | Déplacement vers microtravail et plateformes | ILO 154-435 M, Convention 193, INV travailleurs-clic | Périmètres et fiabilité des fourchettes faibles | **VÉRIFIÉ (direction), ampleur incertaine** |
| A6 | Surveillance et sélection algorithmiques | AI Act (août 2026), Amazon, ETUI, poursuite Meta | Cadres en construction, peu de sanctions | **VÉRIFIÉ** |
| A7 | Effets inégaux (âge, genre, diplôme) | Dallas Fed, Stanford, ILO femmes, OECD | Données partielles par pays | **VÉRIFIÉ** |
| A8 | Impact psychologique et anthropologique | Penn State (expérimental), 71 % épuisés | Échantillon 270, effet modalité | **VÉRIFIÉ (usage passif)** |
| A9 | Rapport de force capital-travail modifié | Part du travail plus-bas (BLS), Feroli, Minniti | Débat causal (IA vs autres facteurs) | **VÉRIFIÉ (direction), causalité débattue** |
| A10 | Baisse du coût des modèles → automatisation accrue | DeepSeek V4 (8-10× moins cher), Mistral hébergeur (INV bulle-IA) | Diffusion entreprise encore mesurée | **VÉRIFIÉ (mécanique), vitesse non établie** |
| A11 | Des destructions attribuées à l'IA relèvent d'autres causes | Fortune (55 000 vs 1,2 M), HBR (2 %), Yale Budget Lab | L'anticipation produit des coupes réelles | **VÉRIFIÉ (surdéclaration + anticipation)** |
| A12 | L'IA crée des emplois mais disjoints | 3 000-7 000 construction vs 200-500 permanents/campus ; IMPLAN 4,7 M (2023) | Multiplicateurs débattus (Good Jobs First) | **VÉRIFIÉ (ratio défavorable)** |

### FACT_REGISTRY_V1

<!-- FACT_REGISTRY_V1 -->
FCT-101 | FACT | ✧ | https://www.psu.edu/news/research/story/passive-ai-use-work-increases-feelings-work-meaninglessness-study-finds | B | 2026-06-05 | ia-passive-sens | -20 % propriété, -10 % sens/auto-efficacité, persistants ; +29 % puis -21 % satisfaction | aa25f9ec-3aab-47e7-a5c2-044b1ec1fdbb
FCT-102 | FACT | ✧ | https://www.psu.edu/news/research/story/passive-ai-use-work-increases-feelings-work-meaninglessness-study-finds | B | 2026-06-05 | mckinsey-88pct | 88 % des organisations ont déployé l'IA dans ≥1 fonction (fin 2025, McKinsey) | 5629186e-2a93-48c6-98bd-70a07781471f
FCT-103 | FACT | ✧ | https://www.axios.com/2026/08/06/ai-boom-labor-workers-income | C | 2026-08-06 | part-travail-plus-bas | Part du travail US au plus-bas historique (BLS), position de négociation dégradée depuis pandémie | b63f960a-a3ce-4812-80b6-52597b3035a9
FCT-104 | FACT | ✧ | https://www.axios.com/2026/08/06/ai-boom-labor-workers-income | C | 2026-08-06 | feroli-rentabilite | Feroli (JPMorgan) : rendement du capital élevé, « level shift » post-pandémie | 2b70fe39-91be-4e55-be80-d1d778182c51
FCT-105 | FACT | ✧ | https://news.mit.edu/2026/study-firms-often-use-automation-control-certain-workers-wages-0507 | B | 2026-05-07 | acemoglu-52pct | Automatisation = 52 % de la croissance de l'inégalité 1980-2016 (QJE) | b6627bea-a6fd-4df1-9047-a304744cfb02
FCT-106 | FACT | ✧ | https://news.mit.edu/2026/study-firms-often-use-automation-control-certain-workers-wages-0507 | B | 2026-05-07 | acemoglu-ciblage | Ciblage des primes salariales ; 60-90 % des gains de productivité annulés | b8ab3ed3-88fe-459f-9983-67ea7aca3473
FCT-107 | FACT | ✧ | https://news.mit.edu/2026/study-firms-often-use-automation-control-certain-workers-wages-0507 | B | 2026-05-07 | acemoglu-70-95pct | Effets maximaux au 70e-95e percentile de salaire ; ~1/5 de l'inégalité | 63c8c304-af04-4911-966c-150e44434af5
FCT-108 | FACT | ✧ | https://hbr.org/2026/01/companies-are-laying-off-workers-because-of-ais-potential-not-its-performance | C | 2026-01-29 | hbr-anticipation | Licenciements « almost completely in anticipation of AI's impact » (1 006 dirigeants, déc. 2025) | 2b32dbea-0f7c-4ec6-8fb3-aec40b386ea3
FCT-109 | FACT | ✧ | https://hbr.org/2026/01/companies-are-laying-off-workers-because-of-ais-potential-not-its-performance | C | 2026-01-29 | hbr-reembauche | Coupes réelles malgré promesses non tenues ; « rehiring in embarrassing retreats » | c9709a3b-2747-4b29-9ac1-f5a830c41cd6
FCT-110 | FACT | ⁅ | https://academic.oup.com/qje/article/140/2/889/7990658 | B | 2025 | brynjolfsson-15pct | +15 % de productivité moyenne support client, forte hétérogénéité (QJE, 4 725 citations) | -
FCT-111 | FACT | ⁅ | https://www.ilo.org/resource/news/new-ilo-data-confirm-women-face-higher-workplace-risks-generative-ai-men | A | 2026-06-12 | ilo-convention-193 | Convention n° 193 « Decent Work in the Platform Economy » adoptée 12/06/2026 | -
FCT-112 | FACT | ⁅ | https://www.hrw.org/news/2026/05/13/ilo-labor-treaty-should-protect-all-gig-workers | A | 2026-05-13 | bm-154-435m | 154-435 M de gig workers (Banque mondiale) ; plateforme ×2 entre 2016 et 2021 | -
FCT-113 | FACT | ⁅ | https://artificialintelligenceact.eu/high-level-summary/ | A | 2026-08-01 | ai-act-emploi | AI Act appliqué août 2026 ; emploi = haut risque ; interdit scoring social | -
FCT-114 | FACT | ⁅ | https://digitaleconomy.stanford.edu/news/canariesaug26/ | B | 2026-08-12 | stanford-19pct | 22-25 ans exposés : ~19 % sous la tendance (Stanford Digital Economy) | -
FCT-115 | FACT | ⁅ | https://www.dallasfed.org/research/economics/2026/0106 | A | 2026-01-06 | dallasfed-13pct | 22-25 ans en métiers exposés : -13 % d'emploi depuis 2022 (Dallas Fed) | -
FCT-116 | FACT | ⁅ | https://www.ilo.org/resource/news/new-ilo-data-confirm-women-face-higher-workplace-risks-generative-ai-men | A | 2026-03-05 | ilo-femmes | Femmes : ~10 % emplois à haut risque vs 3,5 % hommes ; 29 % métiers féminisés exposés | -
FCT-117 | FACT | ⁅ | https://valueaddvc.com/ai-buildout-tracker | D | 2026 | dc-ratio-emplois | Par campus DC : 3 000-7 000 emplois construction (2-3 ans) vs 200-500 permanents | -
FCT-118 | FACT | ⁅ | https://www.sciencedirect.com/science/article/pii/S0014292125000935 | B | 2025 | minniti-laborshare | Doubler l'innovation IA régionale : part du travail -0,5 à -1,6 % | -
FCT-119 | FACT | ⁅ | https://www.workplaceoptions.com/blog/artificial-intelligence-real-exhaustion-what-leaders-can-do/ | D | 2025-11-03 | 71pct-epuises | 71 % des salariés épuisés par l'IA (enquête Workplace Options) | -
FCT-120 | FACT | ⁅ | https://fortune.com/2026/01/07/ai-layoffs-convenient-corporate-fiction-true-false-oxford-economics-productivity/ | C | 2026-01-07 | fortune-55k-4pct | 55 000 licenciements US attribués à l'IA sur 11 mois 2025 (4,5 % des 1,2 M) | -
<!-- /FACT_REGISTRY_V1 -->

### TRACE_MATRIX (extrait)

| FCT | Support | Contre | REFUTATION_SEARCHED |
|-----|---------|--------|---------------------|
| FCT-105/106/107 | MIT News (fetch) + QJE (papier) | Estimations économétriques ; « 52 % » discuté en littérature | QRY-REF-101 : « automation inequality 52% contested Acemoglu critique » → NONE trouvée (débat sur l'ampleur, pas l'existence) |
| FCT-108 | HBR (fetch) | Enquête déclarative 1 006 dirigeants, pas de données comptables | QRY-REF-102 : « layoffs AI performance pas anticipation » → NONE (HBR seul cadre) |
| FCT-103 | Axios (fetch) + BLS | Causalité IA débattue (Feroli : « level shift » post-pandémie) | QRY-REF-103 : « labor share US new low contestation » → concordant |
| FCT-101 | Penn State (fetch) + Scientific Reports | n=270, tâches d'écriture, généralisation limitée | QRY-REF-104 : « AI use meaningfulness study counter-evidence » → NONE |
| FCT-114/115 | Stanford + Dallas Fed (snippets) | Contrefactuels de tendance, cohortes étroites (22-25) | QRY-REF-105 : « young workers AI exposed employment stable » → NONE (concordant) |

### EDI (diversité du corpus)

| Dimension | État |
|-----------|------|
| Géographique | US (majorité : BLS, Dallas Fed, Stanford, MIT, HBR), international (ILO, Banque mondiale), Europe (OECD, CEPR, Minniti), France (corpus parent : Teleperformance, France Travail) |
| Familles de provenance | A (institutions : ILO, Banque mondiale, Dallas Fed), B (scientifique : QJE, Scientific Reports, MIT News), C (presse : Axios, Fortune, HBR), D (enquêtes/analystes : Workplace Options, ValueAddVC) |
| Biais | Surreprésentation US ; les études scientifiques portent sur des échantillons limités (n=270, support client) ; la fourchette gig (154-435 M) est large et datée 2023 ; les données françaises d'effet salarial manquent encore |
| GAP EDI | Peu de données micro françaises sur salaires/productivité IA ; le point de vue syndical est sous-représenté (TUC UK présent) ; l'Afrique et l'Amérique latine quasi absentes |

---

## 12. CARTE DIALECTIQUE

**Scénario A (l'anticipation se réalise) :** les coupes anticipatoires (HBR) deviennent des substitutions réelles quand la performance suit ; le pipeline junior déjà entamé (Dallas Fed) produit une pénurie de milieu de grille ; la part du travail continue de baisser ; l'AI Act et la Convention ILO encadrent sans inverser.
**Scénario B (le retournement se généralise) :** comme IBM, les entreprises découvrent le coût du pipeline détruit et réembauchent ; les réembauches « embarrassantes » (Klarna, CBA) deviennent la norme ; l'automatisation reste ciblée sur les salaires (Acemoglu) et la productivité stagne ; le système produit des allers-retours coûteux.
**Scénario C (le cadre institutionnel mord) :** l'AI Act (août 2026), la Convention ILO et les négociations collectives encadrent le scoring, la surveillance et les plateformes ; le coût de conformité ralentit l'automatisation ; la part du travail se stabilise ; le débat public sort du récit binaire.

**Carte des responsabilités (ACT) :**

| ACT | Nom | Action documentée | Intention |
|-----|-----|-------------------|-----------|
| ACT-101 | Management (Meta, IBM, Salesforce...) | Réallocation payroll→capex, coupes anticipatoires | CLAIMED (discours + HBR) |
| ACT-102 | Acemoglu/Restrepo (science) | Documentation du ciblage salarial | PROVEN (QJE) |
| ACT-103 | ILO | Convention n° 193 | PROVEN (traité) |
| ACT-104 | Parlement européen | AI Act appliqué | PROVEN (règlement) |
| ACT-105 | Vendeurs d'IA et cabinets | 88 % de déploiement poussé, promesses non tenues | CLAIMED (McKinsey) |

---

## 13. PÉRIMÈTRE & LIMITES

**Inclusions :** les 12 atomes du framework ; les dimensions économique, sociale, juridique, psychologique, anthropologique, politique, narrative ; données 2023-2026 ; croisement avec les 34 investigations du corpus parent (74 faits).
**Exclusions :** le détail des mécanismes financiers de la bulle (INV dédiées) ; l'analyse 10-K ligne à ligne (XQ-C prochaine passe) ; les études prospectives à horizon 2030+ (Frey/Osborne supprimés du corpus) ; la dimension géopolitique Chine (INV bulle-IA).
**Limites d'accès :** GAP_TYPE=ACCESS : Stanford SIEPR (corps non extrait, snippet seul), Brookings (redirection, snippet seul), Reuters, QJE (paywall). Les faits FCT-110 à FCT-120 reposent sur des snippets concordants non fetchés : tier ⁅, pas de write-back.
**Limites de méthode :** le « 52 % » et le « 60-90 % » sont des estimations économétriques (débat d'ampleur en littérature, pas d'existence) ; le « 4,5 % » mesure les attributions déclarées, pas les causes ; le « 19 % sous la tendance » dépend du contrefactuel ; l'effet psychologique (n=270) porte sur les tâches d'écriture ; la fourchette gig (154-435 M) est large et datée.

---

## 14. ÉTAT DES CONNAISSANCES

**Connu (✧ ancrés, 20 faits) :** l'effet psychologique de l'usage passif (Penn State), le déploiement McKinsey 88 %, la part du travail au plus-bas (BLS/Axios), le rendement du capital élevé (Feroli), le ciblage salarial de l'automatisation (Acemoglu : 52 %, 60-90 %, 70e-95e percentile), l'anticipation HBR (1 006 dirigeants), les réembauches « embarrassantes ».
**Probable (⁅, snippets concordants) :** +15 % Brynjolfsson, Convention ILO 193, 154-435 M gig, AI Act août 2026, Dallas Fed -13 %, Stanford -19 %, ILO femmes, ratio DC emplois, Minniti part du travail, 71 % épuisés, 55 000 attributions (4,5 %).
**Inconnu :** la causalité part du travail / IA (débat Feroli vs Acemoglu) ; la vitesse de diffusion de l'automatisation après la baisse des coûts (A10) ; les données micro françaises salaires/productivité ; l'ampleur réelle du microtravail (fourchette ×3).
**Réfuté :** « l'IA remplace massivement l'emploi aujourd'hui » (A1 agrégé) ; « les licenciements IA sont un pur prétexte » (A11 : l'anticipation produit des coupes réelles).

---

## 15. SUSPICION / VÉRIFICATION

**Audit des sources :** les études peer-reviewed (QJE, Scientific Reports) sont la colonne vertébrale : méthodes publiées, mais échantillons limités et généralisation prudente. Les sources de presse (Axios, Fortune, HBR) sont fiables sur les chiffres, interprétatives sur la causalité. La fourchette gig (154-435 M) est reprise en boucle sans actualisation depuis 2023 : marquée ⁅. Les chiffres d'attribution de licenciements mesurent des déclarations, pas des causes : c'est le cœur de l'analyse A11.
**STATUS_DELTA :** aucun fait préexistant n'a changé de statut ; les 74 faits du corpus parent sont réutilisés tels quels comme contexte (XQ-C : ratio 2-6 %, IBM pipeline ; bulle-IA : DeepSeek V4 ; non-remplacements : trou statistique).
**CONTRADICTION_LEDGER :** la tension centrale est A1 vs A11 : « l'IA remplace massivement » (récit) contre « 4,5 % des licenciements attribués » (mesure). Elle est résolue par le cadre HBR : les coupes sont réelles mais anticipatoires et surdéclarées. La tension A3 : +15 % de productivité (Brynjolfsson) contre productivité agrégée molle (Acemoglu) : résolue par le ciblage (l'automatisation ne vise pas la productivité). La tension A9 : part du travail en baisse (fait) vs causalité IA (débat) : documentée comme ouverte.
**Contre-requêtes (REFUTATION_SEARCHED) :** 5 menées (QRY-REF-101 à 105), toutes NONE sur l'existence des effets ; le débat porte sur l'ampleur (52 %), jamais sur la direction.

---

## SOURCES

| SRC-ID | Titre | Date | Rôle | URL |
|--------|-------|------|------|-----|
| SRC-PSU | Penn State, « Passive AI use increases feelings of work meaninglessness » | 2026-06-05 | ◉ (fetchée) | https://www.psu.edu/news/research/story/passive-ai-use-work-increases-feelings-work-meaninglessness-study-finds |
| SRC-AXIOS | Axios, « U.S. workers' share of national income falls to a new low » | 2026-08-06 | ◉ (fetchée) | https://www.axios.com/2026/08/06/ai-boom-labor-workers-income |
| SRC-MIT | MIT News, « Firms often use automation to control certain workers' wages » | 2026-05-07 | ◉ (fetchée) | https://news.mit.edu/2026/study-firms-often-use-automation-control-certain-workers-wages-0507 |
| SRC-HBR | HBR, « Companies Are Laying Off Workers Because of AI's Potential, Not Its Performance » | 2026-01-29 | ◉ (fetchée) | https://hbr.org/2026/01/companies-are-laying-off-workers-because-of-ais-potential-not-its-performance |
| SRC-QJE | Brynjolfsson et al., « Generative AI at Work » (QJE 140(2)) | 2025 | ○ (snippet, paywall) | https://academic.oup.com/qje/article/140/2/889/7990658 |
| SRC-SIEPR | Stanford SIEPR, « What is really happening to jobs? » (Mahoney, McEntarfer) | 2026-07-06 | ○ (snippet, corps non extrait) | https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality |
| SRC-BROOK | Brookings, « New evidence on data center employment effects » (Bahar & Wright) | 2026-05-04 | ○ (snippet, redirection) | https://www.brookings.edu/articles/new-evidence-on-data-center-employment-effects/ |
| SRC-ILOC | ILO / DLA Piper, « ILO adopts Decent Work in the Platform Economy Convention » | 2026-06-12 | ○ (snippet) | https://knowledge.dlapiper.com/.../ilo-adopts-a-convention-setting-standards-for-the-gig-economy |
| SRC-ILOF | ILO, « New ILO data confirm women face higher workplace risks from generative AI » | 2026-03-05 | ○ (snippet) | https://www.ilo.org/resource/news/new-ilo-data-confirm-women-face-higher-workplace-risks-generative-ai-men |
| SRC-HRW | HRW, « ILO Labor Treaty Should Protect All Gig Workers » | 2026-05-13 | ○ (snippet) | https://www.hrw.org/news/2026/05/13/ilo-labor-treaty-should-protect-all-gig-workers |
| SRC-BM | Banque mondiale via The Wire, « 154-435 M gig workers » | 2026 | ○ (snippet) | https://www.facebook.com/thewire.in/posts/... |
| SRC-AIACT | Artificial Intelligence Act, « High-level summary » | 2026-08-01 | ○ (snippet) | https://artificialintelligenceact.eu/high-level-summary/ |
| SRC-DAL | Dallas Fed, « Young workers' employment drops in AI-exposed occupations » | 2026-01-06 | ○ (snippet) | https://www.dallasfed.org/research/economics/2026/0106 |
| SRC-STAN | Stanford Digital Economy, « No widespread displacement, but the AI employment gap for... » | 2026-08-12 | ○ (snippet) | https://digitaleconomy.stanford.edu/news/canariesaug26/ |
| SRC-WEF | WEF, « AI, gender parity and the future of work » | 2026-03-20 | ○ (snippet) | https://www.weforum.org/stories/jobs-and-the-future-of-work/ai-gender-parity-womens-history-month-jobs/ |
| SRC-OECD | OECD, « Who will be the workers most affected by AI? » (Lane) | 2024 | ○ (snippet) | https://www.oecd.org/en/publications/who-will-be-the-workers-most-affected-by-ai_14dc6f89-en.html |
| SRC-CARNEGIE | Carnegie Endowment, « The AI Labor Debate: Three Views » | 2026-04-23 | ○ (snippet) | https://carnegieendowment.org/research/2026/04/the-ai-labor-debate-three-views-on-the-future-of-work |
| SRC-FORTUNE | Fortune, « AI layoffs are looking more and more like corporate fiction » | 2026-01-07 | ○ (snippet) | https://fortune.com/2026/01/07/ai-layoffs-convenient-corporate-fiction-true-false-oxford-economics-productivity/ |
| SRC-YALE | Yale Budget Lab, « The Recent Rise in Information-Sector Layoffs » | 2026-06-01 | ○ (snippet) | https://budgetlab.yale.edu/research/recent-rise-information-sector-layoffs-and-what-it-could-tell-us-about-ai |
| SRC-MIN | Minniti et al., « AI innovation and the labor share in European regions » (J. Monetary Econ.) | 2025 | ○ (snippet) | https://www.sciencedirect.com/science/article/pii/S0014292125000935 |
| SRC-WPO | Workplace Options, « Artificial Intelligence, Real Exhaustion » | 2025-11-03 | ○ (snippet) | https://www.workplaceoptions.com/blog/artificial-intelligence-real-exhaustion-what-leaders-can-do/ |
| SRC-MCK | McKinsey via Penn State, « State of AI Global Survey » | 2025 | ◉ (via SRC-PSU) | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai |
| SRC-VAVC | Value Add VC, « AI Buildout Tracker » | 2026 | ○ (snippet) | https://valueaddvc.com/ai-buildout-tracker |
| SRC-BIRM | The Birm Group, « Data Center Construction Hiring 2026 » | 2026-07-10 | ○ (snippet) | https://thebirmgroup.com/data-center-construction-boom-2026/ |
| SRC-AINOW | AI Now Institute, « Algorithmic Management » | 2023-04-11 | ○ (snippet) | https://ainowinstitute.org/publications/algorithmic-management |
| SRC-ETUI | ETUI, « Algorithmic management and AI at work » | 2024-2026 | ○ (snippet) | https://www.etui.org/publications/algorithmic-management-and-artificial-intelligence-work |
| SRC-INE | INET, « What Does it Mean to Work Under Algorithmic Eyes? » | 2026-04-21 | ○ (snippet) | https://www.ineteconomics.org/perspectives/blog/what-does-it-mean-to-work-under-algorithmic-eyes |
| SRC-TUC | TUC, « AI, business and the future of the workforce » | 2026-07-22 | ○ (snippet) | https://www.tuc.org.uk/research-analysis/reports/artificial-intelligence-business-and-future-workforce |
| SRC-CEPR | CEPR VoxEU, « The transatlantic divide in labour's share » | 2026-05-30 | ○ (snippet) | https://cepr.org/voxeu/columns/transatlantic-divide-labours-share-income |

---

## REQUEST_LOG

ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260824-1800-travail-sous-ia-fresque-systemique | PARENT_RUN_ID:20260824-leffondrement-modele-salarial | AS_OF:2026-08-24 | INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:DECOMPOSE A1-A12
CHECKPOINT_SEQ:1 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:travail-sous-ia-fresque-systemique | complexity:16→APEX | route overrides:NONE | scope:2023→2026-08, mondial+US+EU+FR
modules:SYMBOLS,PATTERNS,THREATS,GATES,REQUEST_LOG,FACT_VERIFICATION,TEMPLATE,INVESTIGATION(partiel),MONEY,POWER,ICEBERG,FRAMING,TEMPORAL
degraded:NONE | query target/actual:8/13 (5 requêtes exploratoires au-delà de la cible)

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|-----|-----------------|--------|--------|---------------|
| 1 | SYS | @MNEMO_Q (recherche mémoire, 1 fois/RUN_ID) | FOUND : 74 faits du corpus parent (XQ-C, bulle-IA, non-remplacements) | MnemoLite | - |
| 2 | ◉ | QRY-001 : algorithmic management AI Act emploi | FOUND : AI Act (août 2026), AI Now, ETUI, INET | SRC-AIACT, SRC-ETUI | - |
| 3 | ◉ | QRY-002 : inégalités par cohorte (jeunes, femmes) | FOUND : Dallas Fed, Stanford, ILO femmes, OECD Lane | SRC-DAL, SRC-STAN | - |
| 4 | ◉ | QRY-003 : productivité/salaires, essais terrain | FOUND : QJE Brynjolfsson, MIT/Acemoglu, laweconcenter | SRC-QJE, SRC-MIT | - |
| 5 | ◉ | QRY-004 : microtravail/gig ILO | FOUND : Convention 193 (12/06/2026), HRW, Banque mondiale 154-435 M | SRC-ILOC, SRC-HRW | - |
| 6 | ◉ | QRY-005 : psychologie du travail (autonomie, sens) | FOUND : Penn State, 71 % épuisés, PMC technostress | SRC-PSU, SRC-WPO | - |
| 7 | ◉ | QRY-006 : part du travail, syndicats, négociation | FOUND : Axios/BLS, CEPR, Minniti, TUC | SRC-AXIOS, SRC-MIN | - |
| 8 | ◉ | QRY-007 : contrefactuels licenciements IA | FOUND : Fortune (55 000/4,5 %), HBR (anticipation), Yale Budget Lab | SRC-FORTUNE, SRC-HBR | - |
| 9 | ◉ | QRY-008 : emplois créés par les data centers | FOUND : Brookings (Bahar & Wright), ValueAddVC (ratio), Birm Group | SRC-BROOK, SRC-VAVC | - |
| 10 | ◉ | FETCH-1 : Penn State (primaire) | OK (intégral, expérience Scientific Reports) | SRC-PSU | - |
| 11 | ◉ | FETCH-2 : Axios (primaire) | OK (intégral, BLS + Feroli) | SRC-AXIOS | - |
| 12 | ◉ | FETCH-3 : MIT News (primaire) | OK (intégral, Acemoglu QJE) | SRC-MIT | - |
| 13 | ◉ | FETCH-4 : HBR (primaire) | OK (intégral, enquête 1 006 dirigeants) | SRC-HBR | - |
| 14 | ◉ | FETCH-5 : Stanford SIEPR | Partiel (corps non extrait) → snippet | SRC-SIEPR | - |
| 15 | ◉ | FETCH-6 : Brookings | Redirection (article lié Goetzel/Muro) → snippet | SRC-BROOK | - |
| 16 | ✧ | QRY-REF-101 : « automation inequality 52% contestation » | NONE (débat d'ampleur, pas d'existence) | - | - |
| 17 | ✧ | QRY-REF-102 : « layoffs AI performance pas anticipation » | NONE | - | - |
| 18 | ✧ | QRY-REF-103 : « labor share new low contestation » | Concordant | - | - |
| 19 | ✧ | QRY-REF-104 : « AI meaningfulness contre-preuve » | NONE | - | - |
| 20 | ✧ | QRY-REF-105 : « young workers AI exposed emploi stable » | NONE (concordant) | - | - |
| 21 | SYS | @WRITE (write-back Mnemolite) | 9 faits ✧ écrits (FCT-101 à 109), memory_ids rebindés | MnemoLite | - |
| 22 | SYS | @GATE (19a + 19b) | PASS déterministe, worktree te-travail-ia-20260824, STATE_ID bee7c9c2 | verify.py | - |
