# L'Insee, ses taux de réponse et sa précision : ce qui est publié, où, et ce que le chiffre diffusé ne porte pas

## TL;DR

```text
SUJET: Taux de réponse par vague et précision des estimations publiées par l'Insee (chômage BIT, population légale, recensement, enquêtes ménages), France, 2003-2026.
OBJET: Les taux de réponse et la précision existent, sont publics et chiffrés : taux de réponse EEC de 77 % en 2021 (56 % en résidences non principales) et taux de collecte de 60,5 % / 64,3 % par rang d'interrogation au T2 2023 (FCT-001, FCT-002) ; coefficient de variation communal de 3 % et intervalle de confiance à 95 % publiés pour le recensement (FCT-003). Ce qui n'existe pas, c'est un indicateur de qualité agrégé et central pour les enquêtes ménages, équivalent au baromètre annuel publié pour les entreprises (70,2 % en 2023, FCT-007). Statut : ✧, famille de provenance unique.
SOURCE: Le lead hérité (« gap ACCESS sur les taux de réponse par vague ») est réfuté dans sa formulation : le déficit est de centralisation, pas d'accès (LED-001, CLM-001, CLM-002).
MANIPULATION/STRUCTURE: Aucun marqueur de manipulation rhétorique (DEM 0, BF 0) ; diagnostic @PAT[ICEBERG] limité à CONFIDENCE_MISSING, avec obligation légale de réponse présentée comme garantie de qualité (MANIPULATION_REPORT).
LIMITE: GAP_TYPE=CAUSALITY — l'effet concret de l'incertitude non attachée au chiffre diffusé n'est pas chiffré (AXS-008, NQ-003).
```

## 1. RÉSUMÉ EXÉCUTIF

**Question objet.** Quelle précision est effectivement attachée aux estimations que l'Insee publie, mesurée par les taux de réponse par vague et les intervalles publiés, et que reste-t-il établi lorsque le chiffre diffusé est lu sans son incertitude ?

**Réponse bornée.** Le matériel de qualité existe et il est public. Les taux de collecte de l'enquête Emploi en continu sont publiés **par rang d'interrogation** : 60,5 % en première interrogation et 64,3 % en réinterrogation au T2 2023, sur le champ France hors Mayotte (FCT-002, source SRC-002). Le taux de réponse annuel de la même enquête atteint 77 % des logements du champ en 2021, mais tombe à 56 % pour les résidences non principales au sens de la base de sondage (FCT-001). La non-réponse partielle est elle aussi publiée et dépend du mode : 2,75 % des logements enquêtés par internet en 2021 (FCT-006). Côté recensement, la précision est chiffrée avec ses unités : pour un effectif de 4 900 établi au RP 2018, écart-type 140, coefficient de variation 3 % et intervalle de confiance à 95 % de [4 620 ; 5 180] (FCT-003) ; au niveau national, l'erreur aléatoire du sondage dans les grandes communes donne un coefficient de variation de 0,01 %, soit une imprécision de ±17 500 personnes (FCT-004).

**Le point de bascule.** L'inégalité documentaire est mesurable et se lit dans les sources : pour les **entreprises**, l'Insee publie un baromètre annuel de charge de réponse avec un indicateur agrégé — 65 enquêtes, 1 171 871 questionnaires, taux de réponse moyen de 70,2 % en 2023 (FCT-007, SRC-003). Pour les **ménages**, aucun équivalent central n'a été trouvé dans le corpus inspecté : les taux existent, mais dispersés par enquête, par rang d'interrogation et par caractéristique de logement (ACT-001). Le lead hérité du run parent est donc **partiellement réfuté et reformulé** : il n'y a pas de défaut d'accès, il y a un défaut de centralisation.

**Sur le lead utilisateur (« taux de réponse par vague non centralisés »).** La formulation stricte est démentie : les taux **par vague** existent et sont publiés (FCT-002). Le déficit porte sur l'agrégation et sur l'attachement de l'incertitude au chiffre diffusé, pas sur l'existence de la donnée.

**Acteurs.** Insee (production et publication), ménages échantillonnés (réponse), Eurostat (norme et comparaison), Autorité de la statistique publique et CNIS (contrôle externe, non inspecté).

**Impact.** L'usager du chiffre conjoncturel supporte l'effort de reconstitution de l'incertitude ; l'effet concret sur les montants indexés reste en `GAP_TYPE=CAUSALITY` (AXS-008).

**Gaps principaux.** Access (avis CNIS 2026 en HTTP 403, CTRL-001 ; textes légaux non inspectés, AXS-007), causalité (effet chiffré sur les indexations, AXS-008), indépendance (une seule famille de provenance porte 8 faits sur 9, EDI band `LIMITED`).

## 2. MANIPULATION_REPORT

Input `TOPIC`, mode `INVESTIGATION`, symboles évalués sur corpus final.

| Symbole | Score | Observation nommée |
|---|---:|---|
| Ξ omission | 4 | `CONFIDENCE_MISSING` : le chiffre conjoncturel est diffusé sans incertitude attachée ; les taux existent mais dispersés (FCT-001, FCT-002) |
| ⫸ convergence | 4 | fiche précision, DT2023-22 et baromètre entreprises convergent sur une qualité publiée mais séparée de l'objet publié |
| ⏰ temporel | 4 | forte volatilité des taux de réponse en enquête continue, refonte 2021, rupture de série (FCT-002) |
| Λ cadrage | 3 | l'incertitude est cadrée comme affaire de méthode, non comme attribut du chiffre |
| ↕ pouvoir vertical | 3 | obligation légale de réponse et asymétrie de charge entreprises/ménages (ACT-001) |
| ρ résistance | 3 | contrôle externe (ASP, CNIS, comité du label), dont l'avis 2026 n'a pas pu être lu (CTRL-001) |
| Κ cynisme | 2 | asymétrie documentaire maintenue dans la durée, intention non établie |
| κ influence subtile | 2 | architecture d'information possiblement orientante, design non démontré |
| Σ sémiotique | 2 | autorité du chiffre officiel |
| Φ spectacle | 2 | médiatisation des chiffres trimestriels, hors corpus |
| 🌐 réseau | 2 | chaîne ASP/CNIS/comité du label/Eurostat documentée |
| € argent, Ω inversion, Ψ sidération | 1 | aucune observation matérielle (aucun flux, aucune contradiction archivée, aucune saturation d'information) |
| ⚔ guerre cognitive | 0 | aucune activité coordonnée constatée |

**Rhétorique.** `NUM 3` (le chiffre brut coupé de son incertitude), `AUTH 1`, `FAC 1` (écart potentiel entre précision documentée et précision affichée). `DEM 0`, `BF 0` : aucun marqueur de mauvaise foi, aucun scénario de manipulation retenu.

**Hypothèses implicites.** (a) L'incertitude est du ressort du producteur, non attribut de l'objet publié ; (b) l'obligation légale de réponse vaut garantie de qualité, sans quantification du biais résiduel.

**Clusters chargés.** `clusters/ICEBERG.md` (Ξ=4, seuil de revue bas atteint à 3). `forensic/REASONING.md` non requis (Ξ<5).

**Complexité.** 12 → APEX.

## 3. CLUSTERS

`@PAT[ICEBERG]` appliqué sur l'axe `CONFIDENCE_MISSING`.

| Entrée | Valeur observée | Sensibilité | Statut |
|---|---|---|---|
| Définition visible | taux de réponse EEC 77 % (2021) ; taux de collecte 60,5 % / 64,3 % par rang (T2 2023) | le taux dépend du champ (logements ordinaires, France hors Mayotte) et du rang | FCT-001, FCT-002 |
| Précision visible | CV communal 3 % pour 4 900 habitants, intervalle [4 620 ; 5 180] ; CV national 0,01 % | la précision se dégrade quand l'effectif d'intérêt diminue | FCT-003, FCT-004, FCT-005 |
| Omission matérielle | absence d'indicateur agrégé de qualité pour les enquêtes ménages, alors qu'il existe pour les entreprises | non quantifiable sans définition d'un périmètre | ACT-001, `NOT COMPUTABLE` |
| Facteur caché | aucun : pas de dénominateur substitué, pas de période sélective détectée | — | — |

**Explication concurrente testée.** La dispersion documentaire peut relever d'une organisation normale (un document par enquête, un rang d'interrogation par protocole) plutôt que d'une stratégie. Cette explication est **matérielle** : la fiche précision et le document de travail publient l'information en détail, ce qui affaiblit l'hypothèse de dissimulation. Le constat conservé se limite donc à l'absence d'agrégation et d'attachement de l'incertitude au chiffre diffusé.

**Gap du cluster.** L'effet mesurable de cette absence sur un usage concret reste non établi.

## 4. HERMÉNEUTIQUE

- **L1 explicite.** L'Insee documente la qualité de ses enquêtes : taux de collecte par rang d'interrogation, taux de réponse selon les caractéristiques de la base de sondage, coefficient de variation et intervalle de confiance pour le recensement (FCT-001 à FCT-006).
- **L2 implicite.** L'incertitude est traitée comme un sujet de producteur destiné aux utilisateurs avertis, non comme un attribut de l'objet publié au grand public. Inférence, pas fait.
- **L3 structurel.** La séparation entre document méthodologique et publication d'indicateur organise l'écart entre précision documentée et précision affichée. L'asymétrie entreprises/ménages est institutionnalisée par un baromètre annuel d'un côté, rien de central de l'autre (FCT-007, ACT-001).
- **L4 alternatives.** Alternative bénigne testée et retenue : l'information existe, est publique, chiffrée et rejouable ; la charge de la preuve est satisfaite par les sources elles-mêmes (fiche précision, document de travail).
- **L5 rhétorique.** Vocabulaire normatif et technique ; aucun appel à l'autorité sans support, aucune equivalence fallacieuse détectée.
- **L6 impact.** Effet concret laissé en gap typé (`CAUSALITY`), non comblé par inférence.

## 5. FORENSIC REASONING

Non applicable au sens strict (`Ξ=4 < 5`). La méthode `@PAT[ICEBERG]` a néanmoins été appliquée dans le cluster : signature `CONFIDENCE_MISSING` reconnue (précision montrée sans que l'incertitude soit attachée au chiffre diffusé), avec test de l'explication méthodologique innocente, qui est retenue comme matérielle.

## 6. PRISME DIALECTIQUE

- **Position dominante (institutionnelle).** La qualité est documentée, publique et méthodologiquement détaillée ; la non-réponse est corrigée par redressement et calage ; l'erreur d'échantillonnage est quantifiée. Aucune intention n'est postulée.
- **Position critique la plus forte.** La documentation n'est pas attachée au chiffre diffusé. Pour les entreprises, un indicateur agrégé est publié et suivi annuellement ; pour les ménages, rien d'équivalent n'a été identifié. L'utilisateur du chiffre conjoncturel ne dispose pas de son incertitude au moment de l'usage.
- **Arbitrage par les pièces.** La fiche précision publie CV et intervalles par strate communale (FCT-003, FCT-004, FCT-005) et le document de travail publie les taux de collecte par rang (FCT-002). L'argument de dissimulation tombe ; l'argument de défaut de centralisation tient, mais reste non quantifié en effet concret (AXS-008).
- **Tensions conservées.** (a) CV national très faible (0,01 %) contre non-réponse différentielle forte (56 % contre 77 %) : deux sources d'erreur distinctes, aucune moyenne faite. (b) Obligation légale de réponse présentée comme garantie de qualité contre biais résiduel non chiffré.

## 7. CHRONOLOGIE

| Date | Événement documenté | Source |
|---|---|---|
| 2003-2026 | Période couverte par l'objet ; fiche précision calculée sur les enquêtes annuelles 2016-2020 | SRC-001 |
| 2020, octobre | Publication d'`Insee Méthodes 136` sur la qualité des estimations de population (héritée du run parent, non ré-inspectée ici) | LED-002 |
| 2021 | Nouvelle enquête Emploi : mode internet en réinterrogation ; taux de réponse 77 % du champ, 56 % en résidences non principales ; non-réponse individuelle environ 1 % | SRC-002, SRC-004 |
| 2021-2023 | Gain de près de 10 points du taux de réponse par internet en deux ans et demi ; retour aux niveaux d'avant-crise dès 2022 | SRC-002 |
| T2 2023 | Taux de collecte 60,5 % en première interrogation, 64,3 % en réinterrogation (figure 25) | SRC-002 |
| 2026, mai | Baromètre de charge de réponse entreprises : taux de réponse moyen 70,2 % en 2023 | SRC-003 |
| 2026, juin | Avis de conformité CNIS 2026 sur l'enquête Emploi : identifié, **non inspecté** (HTTP 403) | CTRL-001 |

## 8. DOMAINES

**SOURCE_AUDIT (AXS-001, SATURATED).** Cinq sources acceptées : fiche précision du recensement (SRC-001), document de travail `DT2023-22` sur la refonte de l'enquête Emploi (SRC-002), baromètre de charge de réponse entreprises (SRC-003), `Courrier des statistiques` N6 (SRC-004), page Eurostat sur la non-réponse au LFS (SRC-005). Deux échecs réels consignés : lecteur de page incapable de traiter les PDF (contourné par acquisition locale et extraction), et PDF CNIS en HTTP 403 (non contourné).

**SCOPE_HISTORY (AXS-002, SATURATED).** La refonte de 2021 déplace les niveaux et impose une rétropolation documentée ; le document signale explicitement une forte volatilité des taux de réponse et de faibles taux pendant les vacances scolaires.

**EVIDENCE_CASES (AXS-003, SATURATED).** Trois cas chiffrés et bornés : effectif communal de 4 900 avec CV 3 % et intervalle [4 620 ; 5 180] ; CV national de sondage 0,01 % (±17 500 personnes) ; distribution communale avec médiane inférieure à 1,16 % pour les communes de 10 000 à 19 999 habitants.

**MECHANISMS (AXS-005, SATURATED).** La non-réponse est différentielle : plus faible en résidences non principales, à Paris, chez les locataires et en quartiers prioritaires ; plus élevée hors QPV, en maison, en Alsace ou en Bretagne. Les variables les plus explicatives sont la région, le type de logement et le nombre de pièces. La correction passe par redressement et calage (CAU-001, CAU-002).

**ACTORS_RELATIONS (AXS-006, GAP ACCESS).** La chaîne de contrôle externe (ASP, CNIS, comité du label) est identifiée mais son avis 2026 n'a pas pu être lu : le rôle est documenté en creux, non vérifié.

**RULES_CONTROLS (AXS-007, GAP ACCESS).** L'obligation légale de réponse est mentionnée indirectement dans le corpus ; le règlement européen sur les statistiques sociales n'est cité que par sa contrainte de délai de collecte. Les textes n'ont pas été inspectés.

**RESOURCES_FLOWS (AXS-004, GAP ACCESS).** Le flux documenté est un flux de **données** (ménages → Insee → Eurostat), avec correction et calage comme contrôles. Le flux financier (coût de la collecte) reste non documenté dans le corpus inspecté.

**IMPACT_RESPONSIBILITY (AXS-008, GAP CAUSALITY).** L'effet d'une incertitude non attachée sur un montant indexé (SMIC, IRL, dotations) n'est pas chiffré dans ce run.

**COUNTER_HYPOTHESES (AXS-009, SATURATED).** L'hypothèse adverse — non-réponse sans biais matériel après redressement — reste ouverte : aucun élément inspecté ne quantifie le biais résiduel, et aucun élément inspecté ne démontre un biais matériel.

## 9. RÉSEAU D'ACTEURS

| De | Relation | Vers | Effet documenté | Statut |
|---|---|---|---|---|
| Ménages échantillonnés | répond / ne répond pas | Insee | 77 % de réponse dans le champ en 2021, 56 % en résidences non principales | SATURATED |
| Insee | transmet et déclare la qualité | Eurostat | déclinaison française du LFS ; taux publiés dans le document de travail | SATURATED |
| Eurostat | norme et compare | Insee | le rapport qualité UE juge les taux de non-réponse non comparables entre pays | SATURATED (FCT-009) |
| ASP / CNIS | contrôle la conformité | Insee | avis 2026 identifié, non inspecté (HTTP 403) | GAP ACCESS |

**Centralité** non calculée : graphe trop petit pour un calcul significatif. **Responsabilité individuelle** : aucune personne désignée ; l'objet porte sur une configuration documentaire institutionnelle (`RESPONSIBILITY_MAP` vide avec motif).

## 10. CHAÎNES / PELOTE

**`OBJECT_CAUSALITY`.**

- **CAU-001 (SATURATED).** Sélection différentielle de réponse selon le revenu d'activité, le type de logement et la région → correction par redressement et calage. Conséquence borner : la précision du chiffre publié dépend de la qualité du modèle de correction, pas du seul plan de sondage (FCT-001, FCT-008, CLM-003).
- **CAU-002 (GAP SCOPE).** Chaîne d'édition collecte → correction de la non-réponse → calage → estimation → chiffre diffusé. Le dernier maillon est **constaté** (incertitude non attachée) mais **non quantifié**.

**Alternatives.** Une pesée par étapes (modèle de non-réponse puis calage sur marges externes) existe et est documentée, ce qui atténue l'idée d'une estimation non corrigée.

**Couverture.** Six axes terminaux positifs, quatre axes en gap typé. Les liens vers l'effet concret restent ouverts.

## 11. CARTE DES PREUVES

### LEAD_COVERAGE

| Lead | Statut | Note |
|---|---|---|
| LED-001 — taux par vague non centralisés | SATURATED | déficit de centralisation, non d'accès |
| LED-002 — non-réponse recensement 3,9 % (2019) | GAP ACCESS | chiffre hérité du run parent, non ré-inspecté à la source |
| LED-003 — CV par strate et partage exhaustif/sondage | SATURATED | confirmé à la source |
| LED-004 — codage BIT, surveillance de la non-réponse, calage | SATURATED | confirmé |
| LED-005 — dominance du premier chiffre | SATURATED | dominance héritée ; absence d'incertitude attachée constatée |

### OBJECT_COVERAGE

| Branche | Axes | Résultat |
|---|---|---|
| Qualité publiée (ce qui existe) | AXS-001, AXS-002, AXS-003 | SATURATED |
| Mécanique de correction | AXS-005, CAU-001 | SATURATED |
| Contrôle et règles | AXS-006, AXS-007 | GAP ACCESS |
| Effet concret | AXS-008, AXS-009 | GAP CAUSALITY / SATURATED (hypothèse adverse ouverte) |

### INVESTIGATION_MAP (lecture)

| Axe | Tentatives | Résultats | Statut |
|---|---|---|---|
| AXS-001 | 8 | 5 SRC, 9 FCT | SATURATED |
| AXS-002 | 3 | FCT-002, FCT-009 | SATURATED |
| AXS-003 | 2 | FCT-003 à FCT-005 | SATURATED |
| AXS-004 | 2 | — | GAP ACCESS |
| AXS-005 | 2 | FCT-001, FCT-002, FCT-006, FCT-008 | SATURATED |
| AXS-006 | 2 | — | GAP ACCESS |
| AXS-007 | 2 | FCT-002 | GAP ACCESS |
| AXS-008 | 2 | — | GAP CAUSALITY |
| AXS-009 | 3 | FCT-005, FCT-009 | SATURATED |

### Faits décisifs

| Fait | Énoncé borné | Tier | Famille |
|---|---|---|---|
| FCT-001 | EEC 2021 : 77 % de réponse dans le champ, 56 % en résidences non principales | ✧ | A |
| FCT-002 | T2 2023 : taux de collecte 60,5 % (1re interrogation) et 64,3 % (réinterrogation) | ✧ | A |
| FCT-003 | Effectif 4 900 : écart-type 140, CV 3 %, intervalle [4 620 ; 5 180] | ✧ | A |
| FCT-004 | Erreur de sondage nationale : CV 0,01 %, ±17 500 personnes | ✧ | A |
| FCT-005 | Communes de 10 000 à 19 999 hab. : CV médian < 1,16 % | ✧ | A |
| FCT-006 | Non-réponse partielle par internet : 2,75 % (2021) ; non-réponse individuelle ≈ 1 % | ✧ | A |
| FCT-007 | Baromètre entreprises 2023 : taux de réponse moyen 70,2 % | ✧ | A |
| FCT-008 | Déterminants de la non-réponse : résidences non principales, Paris, locataires, QPV | ✧ | A |
| FCT-009 | LFS 2011 : non-réponse de 2,1 % (DE) à 67,3 % (LU), comparaison jugée impossible par le rapport qualité UE | ✧ | other:eurostat |

**Aucun fait n'atteint `✦`** : huit faits sur neuf reposent sur la seule famille A (producteur intéressé). Aucune contre-recherche active n'a donc été requise, et aucune adjudication documentaire à deux familles n'a été obtenue. C'est une limite, pas un résultat.

### Contradictions

- **CTR-001, résolue par périmètre.** CV national très faible (0,01 %) contre non-réponse différentielle forte (56 % contre 77 %) : deux sources d'erreur distinctes (échantillonnage contre non-réponse). Aucune moyenne n'a été faite entre les deux.
- **CTR-002, partiellement résolue (`CAUSALITY`).** Qualité documentée publiquement contre incertitude absente du chiffre conjoncturel : écart de périmètre de publication, effet non quantifié.

### EDI

```text
SOURCES ◈:1 ◉:4 ○:0
EDI:0.4175 raw:0.6675 penalties:0.25 [POWER_BLOC_CONCENTRATION, MISSING_COUNTER]
geo:0.833 lang:1.0 strat:0.533 owner:0.5 persp:0.25 temp:0.8
⟐:1 ⟐̅:0 🌍:0 🎓:0 🔥:0 | COV:1.0 IND:0.4 CC:1.0 EDI*:0.5888
band:LIMITED — cible APEX 0.80 non atteinte
DIAGNOSTIC_NOT_TRUTH
```

Profil de couverture des claims décisifs : CLM-001 et CLM-002 avec objet direct mais **une seule famille indépendante** (`SCOPE`) ; CLM-003 soutenu (`NONE`) ; CLM-004 sans objet direct (`SCOPE`).

## 12. CARTE DIALECTIQUE

**Scénarios.** (a) *Configuration documentaire ordinaire* : la qualité est publiée par enquête, comme le veut la division du travail statistique ; aucune anomalie. (b) *Défaut de centralisation* : l'utilisateur du chiffre conjoncturel n'a pas d'indicateur agrégé d'incertitude, alors que l'entreprise en a un. (c) *Manipulation* : non soutenue par les pièces inspectées, écartée.

**Scénario retenu.** (b), avec (a) conservé comme explication matérielle de la dispersion. Le tiers (c) est réfuté par le contenu même des documents, qui publient les limites (taux faibles, volatilité, non-réponse partielle par mode).

**Tensions et silences.** Aucun document inspecté ne quantifie le biais résiduel après redressement ni ne publie une incertitude attachée au chiffre conjoncturel.

**Impact et responsabilité.** Aucune personne morale ou physique n'est désignée responsable : l'`ACT-001` documente une action institutionnelle (existence d'un baromètre entreprises, absence d'équivalent ménages identifié) sans imputation d'intention.

## 13. PÉRIMÈTRE & LIMITES

**Inclus.** Enquête Emploi en continu et recensement de la population, 2003-2026 (accent 2016-2026) ; France métropolitaine et comparaison Eurostat ; documents méthodologiques et pages de qualité publiés.

**Exclus.** Sondages d'opinion ; projections démographiques de long terme ; reprises médiatiques du chiffre (contexte non probatoire) ; Outre-mer hors mention de champ.

**Limites d'accès.** Tableaux PDF non OCR-isés ; lecteur de page incapable de traiter les PDF (contourné par extraction locale) ; avis CNIS 2026 inaccessible (HTTP 403) ; textes légaux non inspectés.

**Limites de méthode.** Une seule famille de provenance pour huit faits sur neuf ; pas de codage indépendant ; l'absence d'équivalent ménages du baromètre est **constatée dans le corpus inspecté**, non établie comme absence générale.

## 14. ÉTAT DES CONNAISSANCES

- **Connu (✧, famille unique).** Les taux de réponse et de collecte, par enquête et par rang ; la précision du recensement avec CV et intervalles ; les déterminants de la non-réponse ; l'existence d'un baromètre entreprises.
- **Probable.** La non-réponse différentielle déplace la charge de la précision vers le modèle de correction (CAU-001).
- **Allégué.** Rien retenu comme allégué sans vérification ; le chiffre de 3,9 % de non-réponse au recensement reste hérité et non ré-inspecté (LED-002, GAP ACCESS).
- **Hypothèses ouvertes.** Le biais résiduel après redressement est-il matériel ? (AXS-009)
- **Contesté.** Aucune contestation matérielle détectée dans le corpus.
- **Inconnu.** Effet chiffré de l'incertitude non attachée sur un montant indexé (AXS-008).
- **Réfuté.** Le lead « les taux de réponse par vague ne sont pas publiés » est réfuté (FCT-002).

## 15. SUSPICION / VÉRIFICATION

**Contrôles exécutés.** Taux de réponse et de collecte vérifiés à la source dans `DT2023-22` (figure 25 et section non-réponse) ; précision du recensement vérifiée dans la fiche précision ; contre-perspective externe obtenue auprès d'Eurostat, limitée à 2011 et non comparable selon le rapport qualité UE.

**Échecs réels.** Lecteur de page inapte aux PDF (deux échecs, contournés) ; PDF CNIS en HTTP 403 (non contourné). Aucun succès n'a été simulé.

**Delta de statut.** Le lead hérité passe de « gap ACCESS ouvert » à « réfuté dans sa formulation, reformulé en défaut de centralisation ». Le fait de non-réponse recensement de 3,9 % passe de « cité » à « gap ACCESS » faute de ré-inspection.

**Vérification restante.** Avis CNIS 2026 ; textes légaux ; analyse indépendante sur la précision publiée ; chiffrage de l'effet sur les montants indexés.
