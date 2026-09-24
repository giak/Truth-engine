ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-0255-insee-taux-de-reponse-par-vague-precision-des-estimations | PARENT_RUN_ID:NONE | AS_OF:2026-09-21
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-taux-de-reponse-par-vague-precision-des-estimations/2026-09-21_02-55_insee-taux-de-reponse-par-vague-precision-des-estimations_INPUT.md | SUBJECT_SLUG:insee-taux-de-reponse-par-vague-precision-des-estimations | SUBJECT_FP:sha256:3f051dffd958f49a593c23f7e20261e0bfdec445af5715e237de53a19d2a07b5 | INPUT_SHA256:sha256:fefb21828c0c93beceb4df1e8f6dfe93ca12a3fe07f48691d760c706213f2ebb
COMPLEXITY:12→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:period:2003-2026; geo:France+UE/ONS/Destatis; axes:SOURCE_AUDIT,SCOPE_HISTORY,EVIDENCE_CASES,RESOURCES_FLOWS,MECHANISMS,ACTORS_RELATIONS,RULES_CONTROLS,IMPACT_RESPONSIBILITY,COUNTER_HYPOTHESES; exclusions:sondages d opinion, projections demographiques, reprises mediatiques; limits:tableaux PDF non OCR-ises, taux par vague parfois seulement surveilles en interne
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/INVESTIGATION.md,protocol/FACT_VERIFICATION.md,search/EPISTEMIC.md,search/TEMPLATES.md,output/TEMPLATE.md,clusters/ICEBERG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
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
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:5|CLM:4|AXS:9|CAU:2|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"4 questions restent ouvertes et routees (OCR, taux de reponse par vague, DGF/DGCL, COICOP)","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le gap ACCESS herite n'a pas ete referme : les taux de reponse des enquetes menages Insee ne sont pas centralises par vague, ce qui empeche de quantifier la precision reelle des estimations publiees.","linked_ids":[],"locator":"INPUT.md (archive du run 2026-09-20_19-21, sections NEXT_QUERIES/OPEN_GAPS)","materiality":"DECISIVE","note":"Lead tranche: le deficit n est pas un defaut d acces mais de centralisation. Les taux existent (FCT-001, FCT-002) dans des documents methodologiques disperses; aucun tableau de qualite unique pour les menages.","routes":["EXPAND","LINK"],"source_id":"SRC-IN","status":"SATURATED"}
LED-002 | {"evidence_excerpt":"La non-reponse totale des enquetes annuelles de recensement s'eleve a 3,9 % en 2019, dont 36 % de refus explicites ; le nombre de personnes des logements non repondants est determine par une procedure d'imputation statistique hot deck.","gap":"Le chiffre de non-reponse du recensement (3,9 % en 2019) provient de l archive du run 19-21 (IM136) et n a pas ete re-inspecte a la source dans ce run; la fiche precision confirme la precision par strate mais pas ce taux.","gap_type":"ACCESS","kind":"CLAIM","lead":"La non-reponse totale des enquetes annuelles de recensement atteint 3,9 % en 2019 dont 36 % de refus explicites, et les logements non repondants sont completes par imputation hot deck.","linked_ids":[],"locator":"INPUT.md (section 2, tableau des pieces extraites, ligne Insee Methodes 136)","materiality":"IMPORTANT","routes":["AUDIT","EXPAND"],"source_id":"SRC-IN","status":"GAP"}
LED-003 | {"evidence_excerpt":"Qualite publiee : coefficient de variation par strate ; communes de moins de 10 000 habitants enquetees exhaustivement (1 an sur 5), communes de 10 000 ou plus par sondage d'adresses ; intervalles de confiance constructibles.","gap":"","gap_type":"NONE","kind":"CLAIM","lead":"La precision est publiee sous forme de coefficient de variation par strate, avec recensement exhaustif des communes de moins de 10 000 habitants une annee sur cinq et sondage d'adresses au-dela.","linked_ids":[],"locator":"INPUT.md (section 2, ligne fiche precision du recensement)","materiality":"IMPORTANT","note":"Confirme a la source: CV par strate, intervalles de confiance, et partage exhaustif (moins de 10 000 habitants) / sondage (10 000 et plus).","routes":["AUDIT","LINK"],"source_id":"SRC-IN","status":"SATURATED"}
LED-004 | {"evidence_excerpt":"Note methodologique EEC (Division emploi) | Codage BIT en 3 criteres, surveillance de la non-reponse, calage : la mecanique du chomage mesure, a la source.","gap":"","gap_type":"NONE","kind":"MECHANISM","lead":"Le codage BIT du chomage repose sur trois criteres, avec surveillance de la non-reponse et calage : la mecanique du chomage mesure est documentee a la source mais la precision par vague reste hors corpus.","linked_ids":[],"locator":"INPUT.md (section 2, ligne note methodologique EEC)","materiality":"DECISIVE","note":"Confirme: codage BIT en trois criteres, correction de la non-reponse et calage documentes dans DT2023-22 et le Courrier des statistiques N6.","routes":["EXPAND"],"source_id":"SRC-IN","status":"SATURATED"}
LED-005 | {"evidence_excerpt":"le premier chiffre domine structurellement le recit avant toute revision (CAU-006)","gap":"La dominance du premier chiffre dans le recit public est heritee (CAU-006 du run parent) et non re-mesuree ici; l absence d incertitude attachee au chiffre diffuse est, elle, constatee.","gap_type":"SCOPE","kind":"RELATION","lead":"Le parent retient que le premier chiffre publie domine structurellement le recit avant toute revision, sans avoir documente la part d'incertitude publiee avec ce premier chiffre.","linked_ids":[],"locator":"INPUT.md (section CESURE/limites du parent)","materiality":"IMPORTANT","routes":["LINK","CONTEXT"],"source_id":"SRC-IN","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"La precision est publiee pour le recensement et dans des documents methodologiques, mais pas attachee au chiffre conjoncturel diffuse","gap_type":"SCOPE","linked_leds":["LED-001","LED-003","LED-004"],"proposition":"L'Insee publie une incertitude chiffree (coefficient de variation ou intervalle de confiance) pour ses estimations principales, accessible aupres du chiffre publie.","status":"PARTIAL","support":"FCT-003, FCT-004, FCT-005 (fiche precision RP: CV et IC publies par strate communale) ; FCT-002 (taux de collecte par rang)"}
CLM-002 | {"counter":"NONE_FOUND","gap":"Les taux de reponse menages sont publies par rang et par caracteristique, mais disperses; aucun tableau de qualite unique par vague","gap_type":"SCOPE","linked_leds":["LED-001","LED-004"],"proposition":"Les taux de reponse des enquetes menages de l'Insee sont documentes et publiables par vague d'enquete.","status":"PARTIAL","support":"FCT-001 (77 % / 56 % EEC 2021), FCT-002 (60,5 % et 64,3 % par rang T2 2023), FCT-007 (barometre entreprises)"}
CLM-003 | {"counter":"NONE_FOUND","gap":"","gap_type":"NONE","linked_leds":["LED-002"],"proposition":"La non-reponse est traitee par imputation, avec un effet quantifiable sur les niveaux estimes.","status":"SUPPORTED","support":"FCT-006 (non-reponse partielle par mode), FCT-008 (determinants), imputation hot deck heritee d IM136"}
CLM-004 | {"counter":"NONE_FOUND (a tester au niveau des reprises publiques, hors perimetre documentaire strict de ce run).","gap":"La reprise publique du chiffre sans son incertitude n a pas ete mesuree: hors perimetre documentaire du run (exclusion explicite)","gap_type":"SCOPE","linked_leds":["LED-005"],"proposition":"La narration publique du chiffre officiel escamote l'incertitude attachee (le premier chiffre domine le recit).","status":"GAP","support":"Herite du run parent: le premier chiffre domine structurellement le recit avant toute revision."}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010"],"axis":"SOURCE_AUDIT","links":["LED-001","LED-002","LED-003","CLM-001","CLM-002"],"question":"Quelles pieces Insee documentent officiellement la non-reponse et la precision, et que disent-elles exactement ?","result_ids":["SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009"],"sought_objects":["Insee Methodes 136","fiche precision du recensement","note methodologique EEC","documentation qualite IPC/ERFS"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-002","QRY-006","QRY-007"],"axis":"SCOPE_HISTORY","links":["LED-002","LED-005"],"question":"Depuis quand l'Insee publie-t-elle cette documentation qualite, et quelles refontes ont deplace les niveaux ?","result_ids":["FCT-002","FCT-009"],"sought_objects":["chronologie des refontes EEC/ERFS","revue de qualite","calendriers de publication"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-006","QRY-007"],"axis":"EVIDENCE_CASES","links":["LED-002"],"question":"Quels cas documentes chiffrent l'ecart entre estimation publiee et mesure directe ou verifiee ?","result_ids":["FCT-003","FCT-004","FCT-005"],"sought_objects":["cas Metzing","revisions de croissance","comparaison recensement/enquete"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002"],"axis":"RESOURCES_FLOWS","gap":"Cout de la collecte et financement non documentes dans le corpus inspecte; aucune piece budgetaire dediee retrievee","gap_type":"ACCESS","links":[],"question":"Quels moyens et couts la collecte represente-t-elle, et qui les finance ?","result_ids":[],"sought_objects":["programme budgetaire de l'Insee","cout de l'EEC et du recensement"],"status":"GAP"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-007"],"axis":"MECHANISMS","links":["LED-001","LED-002","CLM-002","CLM-003"],"question":"Par quel mecanisme la non-reponse se transforme-t-elle en chiffre publie (relances, redressement, calage, imputation) ?","result_ids":["FCT-001","FCT-002","FCT-006","FCT-008"],"sought_objects":["protocole de relance","methodes de redressement et calage","imputation hot deck"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-003","QRY-011"],"axis":"ACTORS_RELATIONS","gap":"Role de controle de l ASP et du CNIS non inspecte a la source: le PDF d avis CNIS 2026 renvoie HTTP 403","gap_type":"ACCESS","links":["LED-001"],"question":"Qui controle et valide la qualite publiee (ASP, CNIS, Eurostat, CNIL) ?","result_ids":[],"sought_objects":["roles ASP/CNIS","reglements Eurostat sur la qualite","avis CNIL sur l'obligation de reponse"],"status":"GAP"}
AXS-007 | {"attempt_ids":["QRY-002","QRY-007"],"axis":"RULES_CONTROLS","gap":"Base legale de l obligation de reponse (loi 1951) et reglement (UE) 2019/1700 non inspectes directement; seules des mentions indirectes dans DT2023-22","gap_type":"ACCESS","links":["LED-001"],"question":"Quelles regles rendent la reponse obligatoire ou volontaire, et avec quelles limites legales ?","result_ids":["FCT-002"],"sought_objects":["loi du 7 juin 1951","code des relations avec le public","reglement (UE) 2019/1700"],"status":"GAP"}
AXS-008 | {"attempt_ids":["QRY-001","QRY-002"],"axis":"IMPACT_RESPONSIBILITY","gap":"Effet de l incertitude publiee sur les montants indexes (SMIC, IRL, dotations) non mesure dans ce run: aucun chiffrage retrieve","gap_type":"CAUSALITY","links":["LED-004","LED-005"],"question":"Quel effet concret l'incertitude non publiee produit-elle sur les montants indexes et les decisions ?","result_ids":[],"sought_objects":["indexations legales","dotations DGF","seuils"],"status":"GAP"}
AXS-009 | {"attempt_ids":["QRY-003","QRY-010","QRY-006"],"axis":"COUNTER_HYPOTHESES","links":["LED-001","LED-004"],"question":"La non-reponse peut-elle etre jugee non biaisante, et la precision insuffisamment publiee plutot que dissimulee ?","result_ids":["FCT-005","FCT-008"],"sought_objects":["etudes sur le biais de non-reponse","pratiques de publication d'autres instituts (ONS, Destatis)"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"links":["FCT-001","FCT-008","CLM-003"],"mechanism":"Non-reponse differentielle selon le revenu d'activite, le type de logement et la region, corrigee par redressement et calage","note":"La non-reponse n'est pas aleatoire (56 % en residences non principales contre 77 % au total en 2021; CV communal jusqu'a 3 %). La precision du chiffre publie depend donc de la qualite du modele de correction, non du seul plan de sondage.","sources":["SRC-002"],"status":"SATURATED","type":"MECHANISM"}
CAU-002 | {"gap":"Le dernier maillon de la chaine (chiffre diffuse sans son incertitude attachee) est constate mais non quantifie dans ce run","gap_type":"SCOPE","links":["FCT-002","FCT-006","CLM-001"],"mechanism":"Chaine d'edition: collecte -> correction de la non-reponse -> calage -> estimation -> chiffre diffuse","sources":["SRC-002"],"status":"GAP","type":"MECHANISM"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"action":"Avis CNIS 2026 sur l'enquete Emploi identifie mais non inspecte","controller":"Autorite de la statistique publique / Comite du label et CNIS","gap":"Le PDF de l avis CNIS 2026 est inaccessible (HTTP 403); le controle externe n a donc pas pu etre verifie a la source","gap_type":"ACCESS","information":"Avis de conformite et rapports qualite","oversight":"GAP","rule":"Qualite statistique et conformite des enquetes","sources":["SRC-002"],"status":"GAP"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Publication d'un barometre annuel de charge de reponse pour les enquetes entreprises (taux de reponse moyen, temps de reponse, charge en ETP), sans equivalent public centralise pour les enquetes menages","actor":"Insee","note":"Asymetrie documentaire constatee: pour les entreprises un indicateur agrege est publie et suivi annuellement; pour les menages, les taux existent dans des documents methodologiques disperses.","sources":["SRC-003","SRC-002"],"status":"SATURATED"}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:8|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND:5 memories (leads INSEE/IPC/IRL), aucun snapshot exact pour subject-fp:3f051dff. TOOL_SCHEMA_UNAVAILABLE (MCP mnemolite non exposé à la session) -> fallback MCP-par-curl 8002/ mnemolite 1.12.3 | mnemolite.search_memory | http://localhost:8002/mcp | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND:10 resultats, 3 objets canoniques retenus (DT2023-22, fiche precision RP, Courrier des statistiques N6) | - | - | Insee taux de reponse non-reponse enquete emploi en continu par vague qualite
QRY-002 | WEB | FOUND:10 resultats, 2 objets canoniques (fiche-precision.pdf, IM136) | - | - | Insee Methodes 136 qualite estimations population recensement non-reponse refus hot deck
QRY-003 | WEB | FOUND:10 resultats, 1 famille externe retenue (Eurostat), 1 echec annonce (CNIS) | - | - | Eurostat LFS quality report response rate + CNIS avis qualite enquete emploi
QRY-004 | FETCH | FAILED:content-type application/pdf non extractible par le lecteur de page | - | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf | Fiche precision des resultats du recensement
QRY-005 | FETCH | FAILED:content-type application/pdf non extractible par le lecteur de page | - | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf | La refonte de l'enquete Emploi 2017-2021
QRY-006 | FETCH | FOUND:345472 octets, PDF extrait par pdftotext (461 lignes), source acceptee | SRC-001 | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf | Fiche precision des resultats du recensement (acquisition locale + extraction)
QRY-007 | FETCH | FOUND:5228396 octets, PDF extrait par pdftotext (3909 lignes), source acceptee | SRC-002 | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf | Insee DT2023-22 La refonte de l'enquete Emploi 2017-2021 (acquisition locale + extraction)
QRY-008 | FETCH | FOUND:page inspectee, tableau indicateurs de reponse 2023 (taux de reponse moyen 70,2 %), source acceptee | SRC-003 | https://www.insee.fr/fr/information/8889594 | Barometre annuel de la charge de reponse aupres des entreprises
QRY-009 | FETCH | FOUND:page inspectee (Numerique/sommaire N6 2021), source acceptee | SRC-004 | https://www.insee.fr/fr/statistiques/5398681?sommaire=5398695 | Courrier des statistiques N6 (2021) - Une nouvelle enquete Emploi en 2021
QRY-010 | FETCH | FOUND:page inspectee, taux de non-reponse LFS 2011 de 2,1 % (DE) a 67,3 % (LU) et limite de comparabilite du rapport qualite UE, source acceptee | SRC-005 | https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Disability_statistics_background_-_Labour_force_survey_-_non-response_analysis | Eurostat Statistics Explained - Labour force survey non-response analysis
QRY-011 | FETCH | FAILED:HTTP 403 (acces refuse) | - | https://www.cnis.fr/app/uploads/2025/07/ac-2026-insee-enquete-emploi-annuelle.pdf | CNIS - avis de conformite 2026 enquete Emploi

## EVIDENCE_REGISTRY
SRC-001 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf
SRC-002 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf
SRC-003 | ◈ | fam:A | https://www.insee.fr/fr/information/8889594
SRC-004 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/5398681?sommaire=5398695
SRC-005 | ◉ | fam:other:eurostat | https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Disability_statistics_background_-_Labour_force_survey_-_non-response_analysis

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf | A | 2023-10-22 | Taux de reponse EEC 2021 | 77 % sur l'ensemble des logements dans le champ de l'enquete; 56 % pour les residences non principales au sens de la base de sondage (France metropolitaine, logements ordinaires) | d422fb4d-9a88-4ccf-a99d-5ecfd01129ef
FCT-002 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf | A | 2023-10-22 | Taux de collecte EEC par rang d'interrogation T2 2023 | 60,5 % en premiere interrogation et 64,3 % en reinterrogation (part des fiches-adresses reussies sur l'ensemble de l'echantillon), France hors Mayotte | a95a5c49-17c4-48db-96b7-9d0e81213937
FCT-003 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf | A | 2021-01-01 | Precision publiee d'un effectif communal (recensement) | Pour un effectif de 4 900 etabli au RP 2018 (enquetes annuelles 2016-2020): ecart-type 140, coefficient de variation 3 %, intervalle de confiance a 95 % [4 620 ; 5 180] | fadd770e-70ec-4e67-b5e7-ab6b46d7459f
FCT-004 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf | A | 2021-01-01 | Precision nationale du recensement par sondage | Au niveau national, l'erreur aleatoire introduite par le sondage dans les grandes communes donne un coefficient de variation de 0,01 %, soit une imprecision de +/- 17 500 personnes | 2083635a-f7b7-4c19-b789-77f2c5086b36
FCT-005 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/2383177/fiche-precision.pdf | A | 2021-01-01 | Distribution communale du coefficient de variation (RP 2018) | Communes de 10 000 a 19 999 habitants: CV median inferieur a 1,16 %; pour un quart des communes superieur a 1,29 %; pour le quart le plus faible inferieur a 1,05 % | 01274ca1-fe49-4720-aa8b-0490edca9eaf
FCT-006 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf | A | 2023-10-22 | Non-reponse partielle selon le mode de collecte (EEC 2021) | La non-reponse individuelle est tres rare dans l'EEC (1 %); en 2021, 2,75 % des logements enquetes par internet font l'objet d'une non-reponse partielle | 64a63224-5d71-4b4c-a075-1bf5fb01b497
FCT-007 | FACT | ✧ | https://www.insee.fr/fr/information/8889594 | A | 2026-05-05 | Barometre de charge de reponse entreprises 2023 | 65 enquetes realisees, 1 171 871 questionnaires envoyes, taux de reponse moyen par enquete 70,2 % (+3,5 points vs 2022) | 8de4cc5b-d03a-4a4f-978d-83d02db94fce
FCT-008 | FACT | ✧ | https://www.insee.fr/fr/statistiques/fichier/8201155/DT2023-22.pdf | A | 2023-10-22 | Determinants de la non-reponse EEC | Taux de reponse plus faible dans les residences non principales, a Paris, chez les locataires et en QPV; plus eleve hors QPV, en maison, en Alsace ou en Bretagne; variables les plus explicatives: region, type de logement et nombre de pieces | dc619b96-975a-4c2e-93b9-07ac14d6c424
FCT-009 | FACT | ✧ | https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Disability_statistics_background_-_Labour_force_survey_-_non-response_analysis | other:eurostat | 2014-01-01 | Non-reponse LFS dans l'UE (2011) | Taux de non-reponse au coeur du LFS en 2011 de 2,1 % (Allemagne) a 67,3 % (Luxembourg); le rapport qualite UE conclut qu'il n'est pas possible de comparer les taux de non-reponse entre pays (calculs menages vs individus) | 423f9c24-49fc-4acd-b00c-4d8a2a3870fa
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-002
FCT-002 | SRC-002
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-001
FCT-006 | SRC-002
FCT-007 | SRC-003
FCT-008 | SRC-002
FCT-009 | SRC-005

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18b

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T01:05:02.316680+00:00","fact_mem":{"FCT-001":"d422fb4d-9a88-4ccf-a99d-5ecfd01129ef","FCT-002":"a95a5c49-17c4-48db-96b7-9d0e81213937","FCT-003":"fadd770e-70ec-4e67-b5e7-ab6b46d7459f","FCT-004":"2083635a-f7b7-4c19-b789-77f2c5086b36","FCT-005":"01274ca1-fe49-4720-aa8b-0490edca9eaf","FCT-006":"64a63224-5d71-4b4c-a075-1bf5fb01b497","FCT-007":"8de4cc5b-d03a-4a4f-978d-83d02db94fce","FCT-008":"dc619b96-975a-4c2e-93b9-07ac14d6c424","FCT-009":"423f9c24-49fc-4acd-b00c-4d8a2a3870fa"},"mnemo_row":"33d64ebc-8824-4455-a052-8147020e9839","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"NONE","success":1}],"writeback_row":{"attempted":9,"blocked":0,"eligible":9,"failure":0,"success":9}}

PERSISTENCE_META: MNEMO_ROW:33d64ebc-8824-4455-a052-8147020e9839 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:9;attempted:9;success:9;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[9 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
