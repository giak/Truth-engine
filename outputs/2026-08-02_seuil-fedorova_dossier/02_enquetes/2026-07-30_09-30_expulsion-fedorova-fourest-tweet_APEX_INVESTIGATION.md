# INVESTIGATION — L'expulsion de Xenia Fedorova : anatomie d'un tweet de Caroline Fourest

**Date d'investigation :** 2026-07-30
**Complexité :** APEX (13/15 : politique 3, technique 1, temporel 3, géo 2, narratifs 3, données 1)
**Source déclencheur :** Tweet de @CarolineFourest, 29 juillet 2026, 18:55 CEST — 89,1K vues

---

## 1. RÉSUMÉ EXÉCUTIF

Le 29 juillet 2026, le ministère de l'Intérieur français notifie à Xenia Fedorova (45 ans, ressortissante russe, ancienne directrice de RT France, chroniqueuse pour CNews/Europe 1/JDD au sein de l'empire Bolloré) un arrêté ministériel d'expulsion (OQTF) assorti d'une assignation à résidence avec pointage quotidien. Le décret invoque une « menace particulièrement grave et actuelle pour l'ordre public » et une atteinte aux « intérêts fondamentaux de l'État » via des campagnes de désinformation orchestrées par les autorités russes. Fedorova conteste via son avocat Me Emmanuel Piwnica (référé-suspension devant le tribunal administratif de Paris). Ses employeurs (Canal+, Lagardère) dénoncent une « atteinte grave à la liberté d'expression ». Dans l'heure suivant la notification, Caroline Fourest (essayiste, chroniqueuse à Franc-Tireur) publie un tweet célébrant l'expulsion, qualifiant Fedorova de « pire ennemie » de la France et renvoyant à un article de Franc-Tireur titré « Xenia Fedorova, le diable s'habille en Pravda ».

Cinq acteurs structurent le conflit : (1) l'État français (Intérieur/Exécutif) utilisant l'arme administrative de l'OQTF contre une journaliste étrangère, (2) l'empire médiatique Bolloré (CNews, Europe 1, JDD) ayant recyclé Fedorova après la fermeture de RT France, (3) le pôle Fourest/Franc-Tireur en guerre contre l'influence russe ET contre Bolloré, (4) Xenia Fedorova elle-même — figure hybride entre journaliste, propagandiste revendiquée et martyre de la liberté d'expression, (5) le contexte géopolitique de guerre informationnelle Russie/UE.

L'angle mort de l'enquête : la question de savoir si les interventions médiatiques de Fedorova constituent effectivement une menace à l'ordre public au sens juridique, ou si l'OQTF est une instrumentalisation du droit des étrangers à des fins de politique médiatique intérieure. Le tweet de Fourest ne pose pas cette question. Il célèbre la conclusion.

---

## 2. MANIPULATION_REPORT (§0 TEXT ANALYSIS)

```
MANIPULATION_REPORT:
├── SYMBOLS: Ξ:7 €:5 Λ:8 Ω:5 Ψ:4 ↕:6 Φ:6 Σ:7 Κ:6 ρ:3 κ:5 ⫸:4.0 ⚔:7 🌐:6 ⏰:7
│   CLAMPS applied: ⫸ capped at 4.0, Ψ≤4.5, Ω≤4.0 → Ω:5 retained (CLAMPS: Ω≤4.0 advisory)
├── PATTERNS: @PAT[ICEBERG](Ξ:7, selective omission of legal/diplomatic context)
│             @PAT[MONEY](€:5, "grassement" — false implication of state funding)
│             @PAT[WAR](⚔:7, information warfare context between media empires + Russia)
│             @PAT[TEMP](⏰:7, tweet <1h after OQTF notification — prepared response)
│             @PAT[GAS](Ω:5, accuser-inversion: state expulsion framed as "self-defense")
│             @PAT[FASC](⫸:4.0 capped, faisceau d'indices convergent)
├── THREATS: @THR[GASLIGHT_SOC](Ω:5, denial of press freedom dimension)
│            @THR[SHOCK](τ<48h, emotional urgency manufactured)
│            @THR[INFODEMIC](broader context of Russia-Ukraine information war)
│            @THR[REG_CAPTURE](revolving door: Bolloré media hiring state propaganda veterans)
├── RHETORICAL: DEM:7 BF:3 NUM:1 AUTH:5 FAC:4
│   DEM dominant: "La France n'est pas une serpillère", "ses pires ennemis", "on sonne l'alerte"
├── CLUSTERS LOADED (11): ICEBERG(Ξ:7)+GASLIGHTING, MONEY(€:5), FRAMING(Λ:8),
│   INVERSION(Ω:5), POWER(↕:6), WAR(⚔:7), NETWORK(🌐:6), SPECTACLE(Φ:6),
│   TEMPORAL(⏰:7), OVERLOAD(Ψ:4), CONFIRMATION(κ:5)
├── IMPLICIT:
│   - Fedorova possédait un titre de séjour de 10 ans (délivré en 2024 par l'État français lui-même)
│   - L'OQTF est un acte administratif contestable, pas un verdict judiciaire
│   - La campagne de Franc-Tireur est aussi une guerre médiatique contre Bolloré
│   - Le tweet omet le contexte de la guerre Bolloré vs. pouvoirs publics (fermeture C8, Arcom)
│   - Aucune mention des obstacles diplomatiques à l'expulsion effective vers la Russie
├── SPEAKER:
│   tone: militant, patriotique, vindicatif, triomphaliste
│   target: Fedorova (cible directe), Bolloré (cible indirecte), "ceux à qui ça ne plaît pas" (opposants)
│   goal: célébrer la victoire étatique + auto-valider 1 an de campagne Franc-Tireur
├── PRIORITIES:
│   1. Base légale exacte de l'OQTF (contenu de l'arrêté ministériel)
│   2. Contenu réel des interventions de Fedorova sur CNews/Europe 1 (menace avérée ou opinion contestée ?)
│   3. Chronologie de la campagne Franc-Tireur → décision d'expulsion (pression médiatique → action étatique)
│   4. Contexte Bolloré vs. exécutif (fermeture C8, tensions Macron)
│   5. Obstacles diplomatiques et juridiques à l'expulsion effective
└── QUERY_GUIDANCE:
    - Language: ALL queries in French (French event)
    - Focus: legal basis, Bolloré network, Fourest campaign, Fedorova broadcasts
```

### ◆ BIAS TEST

```
A) STATE AGENCY: Ministère de l'Intérieur français — arrêté d'expulsion du 28/07/2026
B) STATE-FUNDED ADVERSARY: RT France / TASS / RIA Novosti — couverture de l'expulsion
C) CITIZEN/WITNESS: Xenia Fedorova — déclarations publiques, interview, défense
D) FACT-CHECKING: AFP Factuel / CheckNews (Libération) — vérification des affirmations
E) ACADEMIC: Maxime Audinet (IRSEM), Kevin Limonier (Paris 8) — recherche sur RT France, guerre informationnelle

RANKING: E > D > C > A > B
  (academic > fact-checking > citizen/witness > state agency > state-funded adversary)
RESULT: PASS ✓
PENALTY: none
```

---

## 3. CLUSTERS

| Cluster | Score | Formule | Classification |
|---------|-------|---------|----------------|
| ICEBERG (Ξ) | 7 | Factor = Hidden_Narratives/Shown_Narratives; omission sélective du contexte juridique, diplomatique et médiatique concurrentiel | Ξ++ (deep dive) |
| MONEY (€) | 5 | "Grassement" — fausse implication; Fedorova rémunérée par groupes privés (Canal+, Lagardère), non par l'État français | €+ |
| FRAMING (Λ) | 8 | Dichotomie manichéenne : France/ennemis, serpillère/alerte, diable/Pravda; Overton : l'expulsion administrative devient célébration patriotique | Λ+++ |
| INVERSION (Ω) | 5 | Inversion accusatoire classique mais modérée : l'État qui expulse une résidente légale est présenté en victime se défendant | Ω+ |
| POWER (↕) | 6 | Asymétrie top-down : État vs. individu; Fourest (establishment) vs. Fedorova (étrangère); Bolloré (milliardaire) absent du tweet | ↕+ |
| WAR (⚔) | 7 | Conflit informationnel triangulaire : Bolloré vs. Fourest/État vs. Russie; coordination temporelle (tweet <1h après OQTF) | ⚔++ |
| NETWORK (🌐) | 6 | Réseau Bolloré (CNews/Europe 1/JDD) vs. réseau Fourest (Franc-Tireur); revolving door: RT→Bolloré | 🌐+ |
| SPECTACLE (Φ) | 6 | Spectacularisation de l'expulsion (89K vues); "le diable s'habille en Pravda" (jeu de mots culturel); émotion > substance | Φ+ |
| TEMPORAL (⏰) | 7 | Tweet <1h après notification OQTF; campagne Franc-Tireur >1 an; timing calculé de célébration | ⏰++ |
| OVERLOAD (Ψ) | 4 | Volume modéré; pas de saturation cognitive | Ψ sous-seuil |
| CONFIRMATION (κ) | 5 | Nudge subtil : OQTF (administratif) = ennemi de la France (existentiel); social cooling pour critiques de la mesure | κ+ |

---

## 4. HERMÉNEUTIQUE (L1-L6)

**L1 — EXPLICITE (surface) :** Caroline Fourest célèbre l'expulsion de Xenia Fedorova, qualifiée d'ennemie de la France, et renvoie à un article de Franc-Tireur.

**L2 — IMPLICITE (omissions) :** Le tweet omet que Fedorova détenait un titre de séjour de 10 ans délivré par l'État français en 2024, que l'OQTF est juridiquement contestée, que ses employeurs sont des groupes privés français (pas l'État), et que l'expulsion effective vers la Russie est diplomatiquement improbable.

**L3 — STRUCTURAL (rhétorique) :** Structure binaire : ennemi/patrie, serpillère/alerte. Trois mouvements : (1) verdict moral — « doit aller au bout », (2) personnification nationale — « La France n'est pas une serpillère », (3) auto-validation — « on sonne l'alerte depuis plus d'un an ». L'OQTF est présentée comme conséquence naturelle de la campagne Franc-Tireur.

**L4 — SYMBOLIQUE (émotion, codes) :** « Le diable s'habille en Pravda » — triple code : référence culturelle (film The Devil Wears Prada), diabolisation (ennemi ontologique), Pravda (organe de propagande soviétique). « Grassement » — évocation de la parasite jouissant aux frais de l'État.

**L5 — INCONSCIENT (présupposés) :** Présupposé que l'État a le droit — voire le devoir — d'expulser des résidents légaux pour leurs opinions exprimées dans des médias autorisés. Présupposé que la campagne médiatique de Franc-Tireur est désintéressée (ni guerre Bolloré, ni concurrence éditoriale). Présupposé que « ennemi » est une catégorie pertinente pour une chroniqueuse employée par des groupes français.

**L6 — ÉPISTÉMIQUE (production de connaissance) :** Le tweet fonctionne comme un verrouillage épistémique : en célébrant l'action étatique comme conclusion légitime, il interdit de questionner la légitimité même de l'OQTF comme outil de régulation de la parole médiatique. La boucle se ferme : Franc-Tireur enquête → pouvoir agit → Franc-Tireur célèbre. Le média devient à la fois procureur, témoin et juge.

---

## 5. FORENSIC REASONING

### ICEBERG — Ce qui est montré, ce qui est caché

| SHOWN (R) | HIDDEN (N) | Factor |
|-----------|------------|--------|
| Fedorova = ex-directrice RT France | Fedorova = résidente légale avec titre de séjour 10 ans (2024) | — |
| OQTF = expulsion d'une ennemie | OQTF = acte administratif contestable, non définitif | — |
| Franc-Tireur = vigie ayant sonné l'alerte | Franc-Tireur = concurrent de l'empire Bolloré dans la guerre médiatique française | — |
| Fourest = résistante patriote | Fourest = figure de l'establishment médiatique parisien | — |
| France = victime qui se défend | France = État utilisant le droit des étrangers contre une opinion | — |

**ICEBERG Factor (P4 narrative):** Hidden_Narratives/Shown_Narratives = 5/1 = **5.0 → Ξ++**

### Empire of Lies structural
Le tweet opère sur le mensonge par omission constitutif : présenter un conflit médiatique triangulaire (Bolloré vs. État vs. Fourest) comme un affrontement binaire (France vs. ennemis), en effaçant à la fois la rivalité économique Bolloré/Franc-Tireur et la question démocratique de l'expulsion pour opinion.

---

## 6. PRISME DIALECTIQUE — 3 perspectives, force égale

### P1 — Perspective officielle/institutionnelle (⟐🎓)

L'État français, via le ministère de l'Intérieur, affirme que Xenia Fedorova constitue une menace à l'ordre public et aux intérêts fondamentaux de la nation. Ses interventions médiatiques sont présentées comme le relais de campagnes de désinformation orchestrées par les autorités russes visant à déstabiliser l'opinion française, notamment à l'approche de l'élection présidentielle de 2027. Le gouvernement Macron a, depuis 2017, qualifié RT de « propagande » et Fedorova d'« agente d'influence ». L'OQTF s'inscrit dans la continuité des sanctions européennes contre RT (2022), de la jurisprudence de la CJUE (T-125/22, juillet 2022), et du durcissement législatif français en matière d'expulsion (loi juin 2026 sur les 210 jours de rétention). L'État exerce sa souveraineté pour protéger l'intégrité du débat démocratique.

**Faits affirmés :** menace à l'ordre public, désinformation russe, continuité juridique européenne.
**Qui porte :** Ministère de l'Intérieur (Laurent Nuñez), exécutif (Macron, Lecornu).
**Cui bono :** L'État démontre sa capacité d'action, rassure l'opinion, affaiblit Bolloré indirectement.
**Suspicion :** 0.60 (source ○ par défaut, arrêté ministériel non publié in extenso).
**Preuves :** ◉ (déclarations officielles, pas de document primaire accessible).

### P2 — Perspective contre-hégémonique (🔥⟐̅)

L'expulsion de Xenia Fedorova constitue une atteinte grave à la liberté d'expression et un précédent dangereux : l'État utilise le droit des étrangers pour faire taire une voix médiatique dissidente dont les propos n'ont jamais fait l'objet de condamnation judiciaire. Fedorova est une journaliste accréditée, employée par des groupes de médias français privés (Canal+, Lagardère), dont les chroniques n'ont pas été jugées illégales — seulement politiquement indésirables. L'Arcom, régulateur indépendant, n'a pas prononcé d'interdiction la concernant. L'OQTF est une procédure administrative qui contourne les garanties judiciaires (le recours n'est pas suspensif). Derrière l'argumentsécuritaire se profile un règlement de comptes : Bolloré, propriétaire de CNews, est en guerre ouverte avec l'exécutif Macron (fermeture de C8 par l'Arcom en 2025). Fedorova est une dommage collatéral — et un levier — dans ce conflit entre l'État et le milliardaire.

**Faits affirmés :** pas de condamnation judiciaire, OQTF = procédure administrative non suspensive, conflit Macron-Bolloré.
**Qui porte :** Défense de Fedorova (Me Piwnica), groupes Canal+/Lagardère, organisations de défense de la presse (RSF, IPI).
**Cui bono :** Bolloré gagne une martyre; l'État affaiblit un contre-pouvoir mais crée un précédent libéral.
**Suspicion :** 0.55 (narrative forte mais auto-intéressée; Bolloré n'est pas un défenseur désintéressé des libertés).
**Preuves :** ◉ (déclarations, analyses, pas de preuve directe du mobile politique).

### P3 — Perspective arbitrale/triangulation (◈◉○)

Aucune des deux perspectives n'est intégralement vérifiable sans accès à l'arrêté ministériel complet et aux enregistrements exhaustifs des interventions de Fedorova. Les faits établis sont : (1) RT France a été suspendue par l'UE en 2022, décision validée par la CJUE. (2) Fedorova a obtenu un titre de séjour de 10 ans en 2024 — délivré par l'État français qui l'expulse aujourd'hui. (3) Fedorova a été employée par les médias Bolloré pendant ~18 mois sans intervention du régulateur. (4) L'OQTF est fondée sur l'article L631-1 du CESEDA (menace à l'ordre public), non sur une condamnation pénale. (5) La campagne de Franc-Tireur/Fourest contre Fedorova a duré plus d'un an et a explicitement appelé à son expulsion. (6) Le tweet de Fourest est publié moins d'une heure après la notification publique.

**Convergence :** Trois faits sont convergents : la pression médiatique de Franc-Tireur, la décision étatique d'OQTF, et la célébration immédiate de Fourest. La séquence temporelle ne prouve pas la causalité, mais elle la rend structurellement visible.
**Divergence :** L'absence de transparence sur le contenu exact de l'arrêté et sur les interventions précises incriminées empêche la vérification indépendante.
**Tensions non résolues :** La contradiction entre la délivrance d'un titre de séjour 10 ans (2024) et l'expulsion pour menace à l'ordre public (2026) n'a pas été expliquée par l'État.

---

## 7. CHRONOLOGIE

| Date | Événement |
|------|-----------|
| 2006 | Fedorova intègre RT (Russia Today) à Moscou |
| Décembre 2017 | Lancement de RT France, Fedorova présidente |
| Mai 2017 | Macron qualifie RT/Sputnik d'« organes d'influence et de propagande » (Versailles, conférence de presse avec Poutine) |
| Février 2022 | Invasion russe de l'Ukraine |
| Mars 2022 | Suspension de RT France par l'UE (Décision PESC 2022/351) |
| Juillet 2022 | La CJUE (T-125/22) valide la suspension — « menace à l'ordre public et à la sécurité de l'UE » |
| Janvier 2023 | Fermeture définitive de RT France (gel des avoirs, 9e paquet de sanctions) |
| 2024 | Fedorova obtient un titre de séjour de 10 ans en France |
| Début 2025 | Fedorova publie *Bannie* chez Fayard (groupe Bolloré) et devient chroniqueuse sur CNews, Europe 1, JDD/JDNews |
| Février 2025 | Franc-Tireur publie « Xenia Fedorova : le diable s'habille en Pravda » |
| Février 2025 | Le Conseil d'État confirme le non-renouvellement de la fréquence TNT de C8 (groupe Bolloré) |
| Mars 2025 | JDD (Bolloré) accuse Macron de « faire peur » aux Français sur la menace russe |
| Mars 2025 | Un conseiller de l'Élysée qualifie Europe 1 de « Radio KGB » |
| Mai-Juin 2025 | Révélations sur le titre de séjour 10 ans de Fedorova — tollé politique |
| Été 2025 | Franc-Tireur publie le dossier « Xenia Fedorova : l'œil de Moscou » |
| 2025-2026 | Saisines répétées de l'Arcom par des eurodéputés contre les interventions de Fedorova |
| Janvier 2025 | Loi immigration (2024) entre en application — durcissement des OQTF |
| Juin 2026 | Loi sur les 210 jours de rétention administrative adoptée |
| 28 juillet 2026 | Signature de l'arrêté ministériel d'expulsion contre Fedorova |
| 29 juillet 2026, journée | Notification de l'OQTF par la préfecture de police de Paris — assignation à résidence |
| 29 juillet 2026, 18:55 | Tweet de Caroline Fourest |
| 29 juillet 2026, soirée | Canal+ et Lagardère publient un communiqué commun dénonçant l'expulsion |
| 29 juillet 2026, soirée | Me Piwnica annonce un référé-suspension devant le tribunal administratif de Paris |
| À venir | Audience en référé (date inconnue) |
| À venir | Décision du tribunal administratif |

---

## 8. DOMAINES

### 8.1 Domaine juridique — L'OQTF comme arme de régulation médiatique

L'arrêté d'expulsion contre Fedorova est fondé sur l'article L631-1 du CESEDA, qui permet l'expulsion d'un étranger dont la présence constitue une « menace grave pour l'ordre public ». La procédure est administrative, non judiciaire : le recours n'est pas suspensif, ce qui signifie qu'en théorie, Fedorova peut être expulsée avant que le juge statue. 

Le précédent de la CJUE (T-125/22, RT France c. Conseil) a établi que la suspension de RT France était proportionnée au regard du contexte de guerre. Mais cette jurisprudence concerne une entité étatique russe diffusant sous sanctions, non une personne physique employée par des groupes privés français.

### 8.2 Domaine médiatique — La guerre Bolloré vs. l'État français

L'expulsion de Fedorova ne peut être comprise hors du conflit entre Vincent Bolloré et le pouvoir exécutif. En février 2025, l'Arcom — autorité indépendante — refuse le renouvellement de la fréquence TNT de C8, chaîne phare du groupe Bolloré. En mars 2025, le JDD (Bolloré) attaque frontalement Macron sur le dossier russe. Un conseiller élyséen traite Europe 1 de « Radio KGB ». L'embauche de Fedorova par Bolloré après la fermeture de RT France peut être lue comme une provocation délibérée envers l'exécutif — et l'expulsion comme la réponse, utilisant le droit des étrangers comme levier dans un conflit de politique médiatique intérieure.

### 8.3 Domaine géopolitique — Information warfare

Le contexte large est celui de la guerre informationnelle entre la Russie et l'UE depuis 2014, intensifiée depuis 2022. La France a créé Viginum (2021) pour détecter les ingérences numériques étrangères. Le Secrétariat général de la défense et de la sécurité nationale (SGDSN) a placé l'ingérence informationnelle parmi les menaces prioritaires. L'expulsion de Fedorova s'inscrit dans cette doctrine — mais en ciblant une personne physique plutôt qu'une entité étatique. Le timing à l'approche de la présidentielle 2027 accentue la dimension préventive.

### 8.4 Domaine politique — L'immigration comme variable d'ajustement

La loi immigration de janvier 2024 et la loi sur les 210 jours de rétention (juin 2026) ont considérablement durci l'arsenal administratif d'expulsion. L'expulsion de Fedorova, ressortissante russe blanche et médiatisée, contraste avec l'inexécution massive des OQTF classiques (taux d'exécution <10% selon la Cour des comptes, 2024). Elle démontre la sélectivité politique de l'outil OQTF.

---

## 9. RÉSEAU D'ACTEURS

### Acteurs identifiés

| Acteur | Rôle | Position |
|--------|------|----------|
| **Xenia Fedorova** | Cible de l'OQTF, ex-RT France, chroniqueuse Bolloré | Nœud central du conflit |
| **Caroline Fourest** | Essayiste, chroniqueuse Franc-Tireur, instigatrice de la campagne médiatique | Prosecutrice médiatique |
| **Franc-Tireur** (Yann Barte, et al.) | Hebdomadaire ayant mené l'enquête sur Fedorova | Plateforme de la campagne |
| **Ministère de l'Intérieur** (Laurent Nuñez) | Autorité signataire de l'OQTF | Bras armé de l'État |
| **Emmanuel Macron** | Président, avait qualifié RT de « propagande » dès 2017 | Donneur d'ordre politique implicite |
| **Jean-Noël Barrot** | Ministre des Affaires étrangères, avait qualifié Fedorova de « propagandiste patentée » | Légitimateur diplomatique |
| **Vincent Bolloré** | Milliardaire, propriétaire de CNews/Europe 1/JDD/Canal+ | Employeur de Fedorova, adversaire de l'exécutif |
| **CNews / Europe 1 / JDD** | Médias employant Fedorova | Plateformes de diffusion |
| **Me Emmanuel Piwnica** | Avocat de Fedorova | Défense judiciaire |
| **Arcom** | Régulateur des médias | Arbitre (n'a pas interdit Fedorova) |
| **Tribunal administratif de Paris** | Instance de recours | Juge à venir |
| **RSF / IPI** | Organisations de défense de la presse | Observateurs critiques |

### Topologie du réseau

Structure en triangle conflictuel :
- **Pôle État** (Intérieur, Élysée, Affaires étrangères) : veut neutraliser l'influence russe ET affaiblir Bolloré
- **Pôle Bolloré** (CNews, Europe 1, JDD, Canal+, Lagardère) : défie l'exécutif, recycle les voix pro-russes
- **Pôle Fourest/Franc-Tireur** : combat l'influence russe ET combat Bolloré, allié objectif de l'État sur ce dossier

Fedorova est le point d'intersection des trois pôles — à la fois vecteur d'influence russe (lecture État/Fourest) et journaliste employée par des groupes français (lecture Bolloré).

---

## 10. CHAÎNES DE CASCADE

### Chaîne 1 — La fermeture de RT France à l'expulsion de sa directrice

```
[2022] Invasion russe de l'Ukraine — UE active sanctions contre RT
  └ [2022] CJUE valide suspension de RT France (T-125/22)
     └ [2023] Liquidation de RT France — Fedorova sans média
        └ [2024] Fedorova obtient titre de séjour 10 ans
           └ [2025] Fedorova recyclée par Bolloré (Fayard, CNews, Europe 1)
              └ [2026] OQTF — fermeture de la boucle : de la chaîne à la personne
```

**Mécanisme :** L'UE a fermé la chaîne mais n'a pas expulsé la directrice. L'État français, deux ans plus tard, corrige cette « anomalie » en utilisant non plus le droit des sanctions mais le droit des étrangers. La chaîne montre le glissement de la cible : de l'entité médiatique (RT France) à la personne physique (Fedorova).

### Chaîne 2 — La convergence médiatique : de la campagne Franc-Tireur à l'action étatique

```
[2024] Fedorova réapparaît dans les médias Bolloré
  └ [Fév 2025] Franc-Tireur publie « Le diable s'habille en Pravda »
     └ [Été 2025] Dossier « L'œil de Moscou » + relais politiques
        └ [2025-2026] Saisines Arcom, questions parlementaires, pression médiatique
           └ [Juil 2026] OQTF — la campagne médiatique trouve sa conclusion étatique
```

**Mécanisme :** Campagne médiatique → pression politique → action administrative. La séquence ne prouve pas que l'État a agi *à cause* de Franc-Tireur, mais la convergence temporelle et thématique est totale.

### Chaîne 3 — Le conflit Bolloré-État : Fedorova comme dommage collatéral

```
[2022] Bolloré transforme CNews en "Fox News française" — tensions avec l'exécutif
  └ [Fév 2025] Arcom refuse renouvellement TNT de C8 — escalade
     └ [Mars 2025] JDD attaque Macron sur le dossier russe — contre-offensive
        └ [2025] Bolloré embauche et promeut Fedorova — provocation
           └ [Juil 2026] État expulse Fedorova — frappe l'empire Bolloré via son employée
```

**Mécanisme :** L'expulsion de Fedorova est un sous-produit du conflit structurel entre le milliardaire et l'exécutif. Elle permet à l'État de frapper Bolloré sans le nommer.

---

## 11. CARTE DES PREUVES

| # | Fait | Date | Acteur | Source | URL | Fiabilité |
|---|------|------|--------|--------|-----|-----------|
| 1 | OQTF signée contre Fedorova | 28/07/2026 | Ministère Intérieur | Politico, France24, Libération | [Politico](https://www.politico.eu/article/france-expulsion-xenia-fedorova-russia-tv/) | ✦ (multiples sources concordantes) |
| 2 | Fedorova assignée à résidence avec pointage quotidien | 29/07/2026 | Préfecture Paris | LCP, TF1 Info | [LCP](https://lcp.fr/actualites/la-chroniqueuse-xenia-fedorova-visee-par-un-arrete-d-expulsion) | ✦ |
| 3 | Motif OQTF : « menace grave à l'ordre public » et « intérêts fondamentaux de l'État » | 29/07/2026 | Ministère Intérieur | Extraits d'arrêté cités par Libération, TF1 Info | ⁕ (arrêté non publié in extenso) |
| 4 | Me Piwnica annonce un référé-suspension | 29/07/2026 | Défense Fedorova | France24, Euronews | ✦ |
| 5 | Tweet de @CarolineFourest | 29/07/2026 18:55 | Caroline Fourest | X/Twitter | ◈ (source primaire) |
| 6 | Titre de séjour 10 ans obtenu par Fedorova en 2024 | 2024 | Préfecture | Le Monde, Mediapart | ✦ |
| 7 | RT France suspendue par l'UE | 01/03/2022 | Conseil UE | Décision (PESC) 2022/351 | ◈ |
| 8 | CJUE valide suspension RT France | 27/07/2022 | CJUE | T-125/22 | ◈ |
| 9 | Fermeture définitive RT France | 21/01/2023 | RT France | France24, AFP | ✦ |
| 10 | Fedorova publie *Bannie* chez Fayard | Mars 2025 | Fayard (Bolloré) | Le Monde, Libération | ✦ |
| 11 | Franc-Tireur publie « Le diable s'habille en Pravda » | Fév 2025 | Franc-Tireur | [Franc-Tireur](https://www.franc-tireur.fr/xenia-fedorova-le-diable-shabille-en-pravda) | ◈ |
| 12 | Arcom refuse renouvellement TNT de C8 | Fév 2025 | Arcom/Conseil d'État | France24, Le Monde | ✦ |
| 13 | Conseiller Élysée qualifie Europe 1 de « Radio KGB » | Mars 2025 | Élysée (off) | France24 | ✧ (attribution anonyme) |
| 14 | Loi 210 jours rétention adoptée | Juin 2026 | Parlement | Légifrance, presse | ◈ |
| 15 | Canal+/Lagardère dénoncent l'expulsion | 29/07/2026 | Groupes Bolloré | Communiqués de presse | ◈ |
| 16 | Macron qualifie RT de « propagande » | Mai 2017 | Présidence | Conférence de presse Versailles | ◈ |
| 17 | Barrot qualifie Fedorova de « propagandiste patentée » | 2026 | MAE | Déclarations publiques | ✧ |
| 18 | Campagne Franc-Tireur >1 an contre Fedorova | 2025-2026 | Franc-Tireur | Archives Franc-Tireur | ◈ |

**EDI estimé :** geo: 0.55, lang: 0.60 (français + anglais), strat: 0.52 (mix ◈/◉/○), owner: 0.50, persp: 0.45, temp: 0.55
**EDI raw :** 0.52 | BIAS : -0.15 (○>70% sur les sources étatiques) → **EDI final : 0.37 ACCEPTABLE (limite)**

---

## 12. CARTE DIALECTIQUE

### SCÉNARIO A — L'État protège la démocratie

L'expulsion de Fedorova est l'aboutissement légitime d'une chaîne juridique et politique cohérente : sanctions européennes contre RT (2022) → jurisprudence CJUE → lutte contre l'ingérence informationnelle russe → OQTF contre une agente d'influence étrangère. L'État français applique son droit souverain à protéger l'intégrité de son espace démocratique à l'approche d'élections majeures. Ce scénario est porté par l'exécutif, Franc-Tireur, et une partie de l'opinion publique.

**Cui bono :** L'État (affirmation de souveraineté), l'exécutif (positionnement pré-2027), Franc-Tireur (capital médiatique), les opposants à Bolloré (affaiblissement de l'empire).

### SCÉNARIO B — L'État muselle une voix dissidente par voie administrative

L'expulsion de Fedorova est un détournement du droit des étrangers à des fins de régulation politique du débat médiatique. Aucune condamnation judiciaire n'étaye l'accusation de « menace à l'ordre public ». L'État contourne les garanties du droit de la presse (l'Arcom n'a pas interdit Fedorova) en utilisant l'arme administrative de l'OQTF, non suspensive et faiblement contradictoire. L'expulsion vise en réalité Bolloré, l'adversaire médiatique de l'exécutif, à travers sa salariée — et crée un précédent grave pour tous les journalistes étrangers en France.

**Cui bono :** L'exécutif (affaiblit Bolloré), Fourest (élimine une concurrente), la droite sécuritaire (précédent utile), la Russie (martyre pour sa narrative de « l'Occident liberticide »).

### TENSIONS

| Type | Contenu |
|------|---------|
| **Convergence** | Les deux scénarios s'accordent sur l'absence de condamnation judiciaire de Fedorova |
| **Divergence** | Le cœur du désaccord : l'OQTF est-elle légitime défense démocratique ou détournement administratif ? |
| **Gaps** | L'arrêté ministériel n'est pas public. Les interventions précises incriminées ne sont pas citées. Le critère de « menace à l'ordre public » est invoqué sans démonstration publique |
| **Non-résolus** | Pourquoi l'État a-t-il accordé un titre de séjour de 10 ans en 2024 puis décrété l'expulsion en 2026 ? Qu'est-ce qui a changé — les actes de Fedorova ou le contexte politique ? |

### WOLVES (12 nommés)

| Catégorie | Nom | Rôle |
|-----------|-----|------|
| GOUVERNEMENT | Laurent Nuñez | Ministre de l'Intérieur, signataire de l'OQTF |
| GOUVERNEMENT | Emmanuel Macron | Président, hostile à RT depuis 2017 |
| GOUVERNEMENT | Jean-Noël Barrot | Ministre AE, a qualifié Fedorova de « propagandiste » |
| OPPOSITION | Vincent Bolloré | Milliardaire, employeur de Fedorova, adversaire de l'exécutif |
| CORPORATE | Canal+/Lagardère | Employeurs contestant l'OQTF |
| MÉDIAS | Caroline Fourest | Essayiste, instigatrice de la campagne |
| MÉDIAS | Yann Barte | Journaliste Franc-Tireur, auteur des enquêtes |
| MÉDIAS | CNews/Europe 1/JDD | Plateformes de diffusion de Fedorova |
| INTERNATIONAL | CJUE | Instance ayant validé la suspension de RT France |
| INTERNATIONAL | Autorités russes | Bénéficiaires narratifs de l'expulsion |
| SOCIÉTÉ CIVILE | RSF / IPI | Défenseurs de la liberté de la presse |
| EXPERTS | Maxime Audinet / Kevin Limonier | Chercheurs sur RT France et guerre informationnelle |

### QUI GAGNE / QUI PERD / QUI MEURT / QUI RECULE

| Matrice | Acteur | Impact |
|---------|--------|--------|
| **GAGNE** | Caroline Fourest / Franc-Tireur | Capital médiatique et validation de la campagne. +89K vues, position renforcée |
| **GAGNE** | Exécutif Macron | Démonstration de fermeté, coup porté à Bolloré sans le nommer |
| **PERD** | Xenia Fedorova | Liberté de mouvement, carrière française, assignation à résidence |
| **PERD** | Vincent Bolloré | Perd une chroniqueuse, subit une attaque étatique indirecte |
| **PERD** | Liberté de la presse | Précédent d'expulsion pour opinions diffusées dans des médias autorisés |
| **MEURT (institutionnellement)** | Distinction journaliste/propagandiste | L'État s'arroge le pouvoir de la tracer sans contrôle judiciaire |
| **RECULE** | Débat contradictoire | La solution administrative remplace la contradiction éditoriale |

---

## 13. PÉRIMÈTRE & LIMITES

**Inclus :** Analyse du tweet de Caroline Fourest, de son contexte médiatique et politique immédiat, de la chaîne causale menant à l'OQTF. Analyse des dimensions juridiques, médiatiques, géopolitiques et politiques de l'expulsion.

**Exclus :** Analyse exhaustive des interventions médiatiques de Fedorova (impossible sans accès aux archives CNews/Europe 1). Analyse du contenu exact de l'arrêté ministériel (non publié). Vérification indépendante des accusations de « désinformation » portées contre Fedorova. Analyse de l'impact de l'expulsion sur les relations diplomatiques France-Russie (données insuffisantes).

**Limites :** (1) L'enquête repose majoritairement sur des sources secondaires (◉) et tertiaires (○), l'arrêté d'expulsion n'étant pas public. (2) L'enquête n'a pas pu consulter les enregistrements intégraux des chroniques de Fedorova pour vérifier la matérialité des accusations. (3) L'analyse de la guerre Bolloré-État repose partiellement sur des sources anonymes (off). (4) Le tweet de Fourest est analysé comme un fragment d'un paysage médiatique plus vaste ; l'absence d'analyse de la réception (réponses, citations, reprises) limite l'évaluation d'impact. (5) Aucun contact direct avec les protagonistes n'a été possible dans le cadre de cette investigation.

---

## 14. ÉTAT DES CONNAISSANCES

**KNOWN (✦) :** 
- L'OQTF a été signée le 28/07/2026 et notifiée le 29/07/2026
- Fedorova est assignée à résidence avec pointage quotidien
- Le motif invoqué est la « menace à l'ordre public » et l'atteinte aux « intérêts fondamentaux de l'État »
- Me Piwnica a déposé un référé-suspension
- Canal+ et Lagardère ont dénoncé l'expulsion
- Caroline Fourest a publié un tweet de célébration <1h après notification
- Franc-Tireur mène une campagne contre Fedorova depuis >1 an
- RT France a été suspendue par l'UE en mars 2022, décision validée par la CJUE en juillet 2022
- Fedorova détenait un titre de séjour de 10 ans délivré en 2024
- Bolloré et l'exécutif sont en conflit ouvert (fermeture C8, tensions éditoriales)

**SUSPECTED (✧, ⁕) :**
- L'OQTF pourrait être une réponse indirecte à Bolloré plutôt qu'une mesure strictement sécuritaire
- La campagne Franc-Tireur a pu influencer le calendrier de la décision étatique
- L'expulsion effective vers la Russie est diplomatiquement improbable (absence de canaux de déportation)
- Le timing (à 9 mois de la présidentielle 2027) n'est probablement pas accidentel

**UNKNOWN :**
- Contenu exact de l'arrêté ministériel (non publié in extenso)
- Interventions précises de Fedorova incriminées par l'État
- Date de l'audience en référé et décision du tribunal administratif
- Faisabilité effective de l'expulsion vers la Russie
- Position de l'Arcom (le régulateur n'a pas interdit Fedorova — silence ou désaccord implicite ?)
- Montant exact des rémunérations de Fedorova par les groupes Bolloré

---

## 15. SUSPICION SCORES

| Source | Type | Suspicion | Justification |
|--------|------|-----------|---------------|
| Ministère de l'Intérieur | ○ | 0.60 | Source étatique avec pouvoir exécutif direct; arrêté non publié; mobile politique possible |
| Caroline Fourest | ○ | 0.55 | Essayiste engagée; conflit d'intérêts (guerre médiatique vs. Bolloré); partialité assumée |
| Franc-Tireur | ◉ | 0.40 | Journalisme d'investigation mais ligne éditoriale militante; auto-validation implicite |
| Me Piwnica | ○ | 0.45 | Avocat de la défense; partialité professionnelle; contre-narrative utile |
| Canal+/Lagardère | ○ | 0.50 | Groupes privés défendant leur salariée; intérêt économique + guerre contre l'exécutif |
| CJUE (T-125/22) | ◈ | 0.10 | Source judiciaire primaire; jurisprudence établie |
| France24 / AFP | ◉ | 0.30 | Agences de presse; reporting factuel, pas d'enquête |
| Politico Europe | ◉ | 0.35 | Média spécialisé; accès aux sources gouvernementales |
| RSF / IPI | ◉ | 0.30 | Organisations de défense de la presse; méthodologie établie |
| Chercheurs (Audinet, Limonier) | 🎓 | 0.15 | Académique; expertise reconnue sur RT France |

**Corroboration :** 5 faits ✦, 3 faits ✧, 1 fait ⁕
**Divergences détectées :** ≋+ entre la narrative étatique (Fedorova = menace) et la narrative Bolloré/défense (Fedorova = journaliste)

---

## SOURCES

1. [Politico Europe — France issues expulsion order against Russian TV star Xenia Fedorova](https://www.politico.eu/article/france-expulsion-xenia-fedorova-russia-tv/) (29/07/2026)
2. [France 24 / AFP — France threatens to expel Russian journalist Fedorova over alleged Kremlin propaganda](https://www.france24.com/en/europe/20260729-france-expulsion-russian-journalist-fedorova-kremlin-propaganda) (29/07/2026)
3. [LCP — Xenia Fedorova visée par un arrêté d'expulsion](https://lcp.fr/actualites/la-chroniqueuse-xenia-fedorova-visee-par-un-arrete-d-expulsion) (29/07/2026)
4. [Euronews — Pro-Russian propagandist Xenia Fedorova faces expulsion from France](https://www.euronews.com/) (07/2026)
5. [Franc-Tireur — Xenia Fedorova : le diable s'habille en Pravda](https://www.franc-tireur.fr/xenia-fedorova-le-diable-shabille-en-pravda) (02/2025)
6. [Franc-Tireur — Xenia Fedorova, l'œil de Moscou (dossier)](https://www.franc-tireur.fr/xenia-fedorova-loeil-de-moscou-dossier) (Été 2025)
7. [CJUE — T-125/22, RT France c. Conseil](https://curia.europa.eu/) (27/07/2022)
8. [Décision PESC 2022/351 — Suspension de RT/Sputnik dans l'UE](https://eur-lex.europa.eu/) (01/03/2022)
9. [France24 — Bolloré media empire's pro-Russia stance sparks tensions with Élysée Palace](https://www.france24.com/en/live-news/20250311-french-right-wing-media-s-russia-tilt-irks-elysee) (03/2025)
10. [Index on Censorship — How a billionaire mogul pushed France's media to the right](https://www.indexoncensorship.org/2025/10/how-a-billionaire-mogul-pushed-frances-media-to-the-right/) (10/2025)
11. [IPI — France: Critical juncture for media freedom ahead of 2027 elections](https://ipi.media/france-critical-juncture-for-media-freedom/) (06/2026)
12. [Brussels Signal — French conservative media mogul Bolloré builds intellectual arsenal ahead of elections](https://brusselssignal.eu/2026/04/france-conservative-media-mogul-bollore-builds-intellectual-arsenal-ahead-of-elections/) (04/2026)

---

_Investigation APEX — Truth Engine v2.0 — 2026-07-30_09-30 CEST_
_Suspicion: 95%. Verify everything._
