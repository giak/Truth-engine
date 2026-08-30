# INVESTIGATION — Le terrain macroéconomique avant l'onde de choc : France → Europe → comparateurs (référentiel d'indicateurs)

```yaml
RUN_MANIFEST:
  ENGINE_VERSION: 2.9
  STATE: FINAL
  RUN_ID: 20260826-1710-terrain-macro-france-europe
  PARENT_RUN_ID: NONE
  AS_OF: 2026-08-26
  INPUT_KIND: TOPIC
  MISSION_MODE: INVESTIGATION
  INPUT_REF: NONE
  SUBJECT_SLUG: terrain-macro-france-europe
  INVESTIGATION_PATH: investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-26_17-10_terrain-macro-france-europe_INVESTIGATION.md
  SCOPE: lead_question=le « terrain » décrit par les remarques externes (refroidissement du marché du travail, tensions d'entreprises, contrainte budgétaire, Europe) est-il vérifiable indicateur par indicateur ? | object_question=fournir un référentiel macro borné et sourcé (≈25 indicateurs France → Europe → US) pour cadrer l'Acte charnière « L'IA n'arrive pas dans une économie immobile » | period=2023-2026 | geo=France, UE-27, US | domains=marché du travail, entreprises, finances publiques, productivité | actors=Insee, Banque de France, DARES, France Travail, FIPECO, EPSS, Eurostat, FMI, Commission européenne | exclusions=analyse sectorielle fine (INV-P0-01), fiscalité détaillée (INV-P0-04) | limits=IMF 403 (snippet corroboré), Draghi/Ageing Report en PDF non extraits, série « −6,5 % BMO » non retrouvée
  COMPLEXITY: $CX_SCORE=7 → $CX=COMPLEX
  CHECKPOINT_SEQ: 1
  LAST_COMPLETED: 18b
  NEXT_ACTION: NONE
  RESUME_COUNT: 0
  ROUTE_OVERRIDES: []
  LOADED_MODULES: [SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, TEMPLATE.md, clusters/ICEBERG.md, clusters/MONEY.md, clusters/FRAMING.md]
  DEGRADED_FLAGS: [MNEMO_UNAVAILABLE_PARAMETRE, IMF_403, PDF_DRAGHI_AGEING_NON_EXTRAITS]
MNEMO_ROW: FAILED_PARAM_TRANSMISSION
SELF_WRITE_ROW: PENDING_AT_SERIALIZATION
WRITEBACK_ROW: 0_WRITTEN
```

## MANIPULATION_REPORT

| Symbole | Score | Observation nommée |
|---|---|---|
| Ξ | 6 | La série « BMO −6,5 % » et « difficultés 64 %→49 % » du corpus n'ont pas été retrouvées (dénominateurs différents) ; l'IMF 403 laisse un trou de source |
| € | 5 | La destination des gains de productivité dépend du terrain (marges, dette, déficit) : enjeu de répartition |
| Λ | 5 | « Crise de l'emploi » vs « refroidissement » : le même 8,3 % peut être cadré différemment selon le dénominateur choisi |
| Ω | 2 | Faible |
| Ψ | 1 | Faible |
| ↕ | 3 | Pénuries (43,8 % projets difficiles) vs chômage (8,3 %) : asymétrie structurelle du marché |
| Φ | 1 | Faible |
| Σ | 1 | Faible |
| Κ | 1 | Faible |
| ρ | 3 | Statistique publique fournit les instruments de vérification |
| κ | 1 | Non établi |
| ⫸ | 5 | Insee, BdF, France Travail, EPSS, FIPECO convergent sur un même état du terrain (refroidissement sans effondrement) |
| ⚔ | 0 | Aucune coordination établie |
| 🌐 | 2 | Graphe institutionnel simple |
| ⏰ | 3 | T2 2026 = point de bascule apparent (chômage au plus haut depuis 2020, emploi privé 6e trimestre de baisse sur un an) |

CLUSTERS : ICEBERG (Ξ=6), MONEY (€=5), FRAMING (Λ=5). PATTERNS : @PAT[ICEBERG] (séries absentes).

## 1. RÉSUMÉ EXÉCUTIF

**RÉPONSE À L'OBJECT_QUESTION.** Référentiel établi : **25 indicateurs**, dont **20 vérifiés L2 en session** (extrait primaire lu, locator exact) et 5 au statut snippet/GAP (Europe). L'état du terrain français au T2-août 2026 est cohérent avec la formulation robuste du tour 2 : **le marché du travail se refroidit sans s'effondrer** (chômage 8,3 %, plus haut depuis T3 2020 ; emploi privé −0,4 %/an mais +1,0 million vs fin 2019 ; 43,8 % des projets de recrutement jugés difficiles à pourvoir), **le tissu productif est sous tension avec des trajectoires sectorielles divergentes** (70 803 défaillances +19,3 % vs 2010-2019 mais >1,2 M créations +11,1 % ; climat des affaires 98, industrie 103, bâtiment 96), **l'État est sous forte contrainte budgétaire** (déficit 5,1 %, dette 115,7 %, ASSO −6,7 Md€, Sécu −21,6 Md€) et **l'Europe combine vieillissement et retard de productivité** (≈ −20 % vs US selon le FMI, contribution du travail à la croissance potentielle devenant négative). Ce référentiel valide l'équation de l'Acte charnière : une hausse de productivité de 20 % n'a pas la même destination dans une entreprise qui manque de personnel, une entreprise qui perd de l'argent, un secteur en guerre des prix ou un État qui cherche des recettes.

**RÉPONSE À LA LEAD_QUESTION (verdict borné).** Les affirmations du tour 2 sur la France sont **confirmées dans leurs grandeurs** par sources primaires (20/25 L2). Deux corrections : (1) la série « BMO −6,5 % » n'a pas été retrouvée sur la page BMO inspectée (le volume 2 279 500 et 43,8 % sont confirmés ; la variation annuelle reste à ancrer) ; (2) les éléments Europe (FMI −20 %, Draghi, Ageing Report) sont au statut snippet : non contredits, non confirmés primairement dans cette exécution.

## 2. CHRONOLOGIE (parutions clés)

| Date | Publication | Valeur clé |
|---|---|---|
| 29/05/2026 | Insee Première 2106 | Déficit 5,1 %, dette 115,7 %, ASSO −6,7 Md€ |
| 30/07/2026 | Insee IR 186 | Emploi privé −0,4 %/an, 6e trimestre de baisse |
| 07/08/2026 | Insee IR 192 | Chômage 8,3 % (+0,2 pt) |
| 07/08/2026 | BdF défaillances | 70 803 (+5,1 %/an, +19,3 % vs 2010-2019) |
| 21/08/2026 | Insee climat des affaires | 98 tous secteurs, 103 industrie |
| 25/08/2026 | Insee tableau de bord | PIB +0,2 % T2 ; coût du travail +2,4 %/an |
| 2026 | France Travail BMO | 2 279 500 projets, 43,8 % difficiles |

## 3. DOMAINES — TABLE DES INDICATEURS (pièce centrale)

### 3.1 Marché du travail (France)

| # | Indicateur | Valeur | Période | Source / URL | Statut |
|---|---|---|---|---|---|
| 1 | Chômage BIT | 8,3 % (+0,2 pt/trim., +0,7 pt/an ; +62 000 chômeurs/trim.) | T2 2026 | Insee IR 192 | **L2** |
| 2 | Emploi salarié privé | −0,1 %/trim. (−19 300) ; −0,4 %/an (−79 700) ; +5,0 % vs fin 2019 (+1,0 M) | T2 2026 | Insee IR 186 | **L2** |
| 3 | Intérim | −1,4 %/trim. ; −1,9 %/an (−13 500) ; −10,4 % vs 2019 | T2 2026 | Insee IR 186 | **L2** |
| 4 | Emploi salarié total | 20 951 milliers | T2 2026 | Insee tableau de bord | **L2** |
| 5 | BMO projets de recrutement | 2 279 500 ; 43,8 % difficiles ; 32,2 % saisonniers | 2026 | France Travail | **L2** |
| 6 | BMO variation annuelle | « −6,5 % » (corpus) | 2026 | non retrouvée sur la page | ⁅ GAP |
| 7 | Effectifs banques | 368 800 (−0,7 %) ; turnover 7,7 % vs 20 % national | 2025 | FBF (INV-P0-01) | **L2** |
| 8 | Alternants banques | 18 100 (−8,6 %) | 2025 | FBF (INV-P0-01) | **L2** |

### 3.2 Entreprises (France)

| # | Indicateur | Valeur | Période | Source / URL | Statut |
|---|---|---|---|---|---|
| 9 | Défaillances (cumul 12 mois) | 70 803 ; +5,1 %/an ; +19,3 % vs moyenne 2010-2019 | fin juin 2026 | BdF | **L2** |
| 10 | Créations d'entreprises | >1,2 M ; +11,1 % | 12 mois fin juin 2026 | Insee (cité BdF) | **L2** |
| 11 | Climat des affaires | 98 tous secteurs (+1) ; industrie 103 (+2) ; services 100 ; bâtiment 96 | août 2026 | Insee | **L2** |
| 12 | Production manufacturière | −1,1 %/mois ; +0,9 %/an | juin 2026 | Insee | **L2** |
| 13 | PIB | +0,2 %/trim. (après −0,1 %) ; +0,9 %/an | T2 2026 | Insee | **L2** |
| 14 | Coût horaire du travail | +2,4 %/an | T2 2026 | Insee | **L2** |
| 15 | Confiance des ménages | 86 (stable) | août 2026 | Insee | **L2** |

### 3.3 Finances publiques et social (France)

| # | Indicateur | Valeur | Période | Source / URL | Statut |
|---|---|---|---|---|---|
| 16 | Déficit public | 152,5 Md€ = 5,1 % PIB | 2025 | Insee Première 2106 | **L2** |
| 17 | Dette publique | 115,7 % PIB (112,6 % en 2024) | 2025 | Insee Première 2106 | **L2** |
| 18 | ASSO (Sécu, comptes nat.) | −6,7 Md€ (dégradation 7,9 Md€ ; première fois depuis 2021) | 2025 | Insee Première 2106 | **L2** |
| 19 | Déficit Sécu (régimes de base) | −21,6 Md€ (2025) ; −19,4 Md€ prévu (2026) ; −23,7 Md€ (2029 sans mesures) | 2025-2029 | Cour 2026 / EPSS | **L2** |
| 20 | Cotisations sociales | 443 Md€ = 14,8 % PIB = 34 % des prélèvements obligatoires ; assiette 1 078 Md€ ; élasticité 0,95 | 2025 | FIPECO fiche 13 | **L2** |
| 21 | Part des cotisations (Sécu) | 64 % (1990) → 48 % (2025) | 1990-2025 | EPSS / FIPECO | **L2** |
| 22 | Taux moyen de cotisations | 34 % (40 % mi-1990s, 38 % 2017) | 2025 | FIPECO fiche 13 | **L2** |

### 3.4 Europe et comparateurs

| # | Indicateur | Valeur | Période | Source / URL | Statut |
|---|---|---|---|---|---|
| 23 | Productivité UE vs US | ≈ −20 % (snippet ; 403 IMF) | mars 2026 | IMF blog (403) | ⁅ snippet |
| 24 | Valorisations jeunes entreprises | 42 900 Md$ US vs 5 000 Md$ UE (snippet) | 2026 | IMF blog (403) | ⁅ snippet |
| 25 | Draghi : 4 pressions | productivité, démographie, énergie, concurrence | 2024 | Commission (PDF) | ⁅ snippet |
| 26 | Ageing Report | contribution du volume de travail à la croissance potentielle négative dès fin des années 2020 | 2024 | Commission (PDF) | ⁅ snippet |
| 27 | Cotisations en % PIB (UE) | France 14,8 % ; Allemagne 17,2 % ; UE-27 13,5 % ; zone euro 14,2 % ; Suède 3,1 % | 2025 | FIPECO (Eurostat) | **L2** |
| 28 | Répartition cotisations | France 68 %/32 % (employeurs/ménages) ; UE 54 %/46 % ; Allemagne 42 %/58 % | 2025 | FIPECO (Eurostat) | **L2** |

**Bilan : 20 indicateurs L2 (France, sources primaires inspectées) + 5 snippets Europe (non contredits, non confirmés) + 1 GAP (BMO −6,5 %).**

## 4. RÉSEAU D'ACTEURS (producteurs de la statistique)

| Acteur | Rôle | Indicateurs | Accès |
|---|---|---|---|
| Insee | Statisticien national ◈ | Chômage, emploi, comptes publics, conjoncture | INSPECTÉ (5 publications) |
| Banque de France | Statistique financière ◈ | Défaillances, créations | INSPECTÉ |
| France Travail | Opérateur ◈ | BMO | INSPECTÉ |
| DARES | Statisticien ◈ | MMO, flux | INACCESSIBLE (socket fermé ×2, INV-P0-01) |
| FIPECO | Analyste indépendant ◉ | Cotisations, financement social | INSPECTÉ (fiche 13, INV-P0-04) |
| EPSS / Cour des comptes | Institutionnel ◈ | Déficit Sécu, financement | INSPECTÉ (INV-P0-02/04) |
| Eurostat / FMI / Commission | Européen ◈ | Comparaisons, productivité | IMF 403 ; Eurostat via FIPECO |

## 5. CHAÎNES / PELOTE (le terrain comme déterminant)

CAUSAL_ROUTE=REQUIRED (comment le terrain conditionne la destination des gains IA).

- **CAU-001 Terrain → destination des gains (SUPPORTED, mécanisme)** : une entreprise florissante (climat 103 industrie) peut convertir +20 % de productivité en croissance ; une entreprise sous contrainte de marge (défaillances +19,3 % vs 2010-2019) le convertira en non-remplacement, baisse de prix ou coupe. Le terrain n'est pas un décor : c'est le filtre de répartition. (Soutenu par la coexistence documentée des deux états, tableaux 3.1-3.2.)
- **CAU-002 Tensions de recrutement vs chômage (SUPPORTED)** : 8,3 % de chômage et 43,8 % de projets difficiles coexistent : l'IA ne « frappe pas le travail » uniformément, elle arrive dans un marché segmenté (métiers en tension, métiers en contraction). (FCT-001, FCT-005.)
- **CAU-003 Contrainte budgétaire → arbitrages (SUPPORTED)** : déficit 5,1 %, Sécu −21,6 Md€ : toute transition à financer (formation, reconversion) entre en concurrence avec le redressement des comptes. L'équation « transition à financer + finances contraintes = arbitrages plus durs » est documentée par les deux états. (FCT-016 à 019.)
- **CAU-004 Europe : impératif de productivité (PARTIAL, snippet)** : vieillissement + retard −20 % ⇒ l'Europe a besoin de productivité au moment où l'IA en promet ; la tension « nécessité économique vs menace sociale » est posée mais non sourcée primairement (snippet FMI/Draghi/Ageing). Type : CONTEXT, partiellement sourcé.
- **GAP-001** : BMO −6,5 % non retrouvé ; GAP-002 : série « difficultés 64 %→49 % » non retrouvée (dénominateur probablement différent de 43,8 %).

## 6. CARTE DIALECTIQUE

- **⟐ Lecture « refroidissement maîtrisé »** : chômage en hausse mais loin du pic 2015 (−2,2 pts) ; emploi +1,0 M vs 2019 ; déficit en baisse (5,8 %→5,1 %) ; climat des affaires au-dessus de 100 dans l'industrie. Support : tableaux 3.1-3.3.
- **⟐̅ Lecture « détérioration de long terme »** : 6e trimestre consécutif de baisse de l'emploi privé ; intérim −10,4 % vs 2019 (canari du cycle) ; défaillances +19,3 % vs 2010-2019 ; dette 115,7 % ; ASSO déficitaire pour la première fois depuis 2021. Support : mêmes sources, autres séries.
- **Arbitrage** : les deux lectures sont vraies simultanément (niveaux vs dynamiques ; stocks vs flux). La formulation publiable du tour 2 est validée telle quelle : « refroidissement, pas effondrement ; coexistence chômage/pénuries ; tissu productif sous fortes tensions, trajectoires sectorielles divergentes ; État sous forte contrainte budgétaire ».

## 7. CARTE DES PREUVES

### FACT_REGISTRY_V1 (extrait : faits L2 nouveaux de cette exécution)

`FCT-001 | FACT | ✦ | https://www.banque-france.fr/fr/statistiques/entreprises/defaillances-dentreprises-2026-06 | BdF◈ | 2026-08-07 | terrain-macro-france-europe | 70 803 défaillances cumul 12 mois fin juin 2026 ; +5,1 %/an ; +19,3 % vs moyenne 2010-2019 ; contexte : conjoncture dégradée, chocs successifs | mem:-`

`FCT-002 | FACT | ✦ | même URL BdF (Insee cité) | BdF◈+Insee◈ | 2026-08-07 | terrain-macro-france-europe | >1,2 M d'entreprises créées sur 12 mois fin juin 2026, +11,1 % : les défaillances brutes ne sont pas un taux de mortalité à population constante | mem:-`

`FCT-003 | FACT | ✦ | https://www.insee.fr/fr/statistiques/2107840 | Insee◈ | 2026-08-25 | terrain-macro-france-europe | Climat des affaires août 2026 : 98 tous secteurs (+1), industrie 103 (+2), services 100, bâtiment 96 ; PIB +0,2 %/trim. T2 ; coût horaire du travail +2,4 %/an | mem:-`

`FCT-004 | CLAIMED | ⁅ | IMF blog (403) | IMF◈ | 2026-03-12 | terrain-macro-france-europe | Productivité UE ≈ −20 % vs US ; valorisations jeunes entreprises 42 900 Md$ US vs 5 000 Md$ UE | mem:-`

### CONTRADICTION_LEDGER

1. **« Difficultés de recrutement en chute 64 %→49 % » (corpus) vs BMO 43,8 % (2026)** : séries probablement de dénominateurs différents (part des établissements vs part des projets) ; la série 64→49 n'a pas été retrouvée. Non résolue (GAP-002).
2. **Climat des affaires industrie 103 (+2) vs production manufacturière −1,1 %/mois** : l'enquête d'opinion et la production réelle divergent à court terme (phénomène classique d'avance/retard) ; les deux sont consignées sans moyennage.
3. **Défaillances +19,3 % vs créations +11,1 %** : non contradictoires (stock vs flux), mais toute phrase « les entreprises sont en crise » est interdite sans cette nuance (BdF le souligne elle-même).

### EDI

Familles : A ◈ (Insee, BdF, France Travail, EPSS, Cour, Eurostat via FIPECO), ◉ (FIPECO). B/D/E absents dans ce référentiel (référentiel de statistique publique, pas un débat) ; les faits centraux reposent sur au moins deux familles pour les finances publiques (Insee + Cour/EPSS) et le social (FIPECO + EPSS).

## 8. PÉRIMÈTRE & LIMITES

**Inclusions** : indicateurs macro France (marché du travail, entreprises, finances publiques), Europe (productivité, cotisations), période 2023-2026. **Exclusions** : analyses sectorielles fines (renvoi INV-P0-01), fiscalité détaillée (renvoi INV-P0-04), scénarios de stress-test chiffrés (Acte VI, sur la base FIPECO 0,95). **Limites** : IMF 403 (productivité UE en snippet, corroboré par la littérature mais non inspecté) ; Draghi/Ageing Report en PDF non extraits (même statut) ; BMO −6,5 % et série 64→49 non retrouvées (GAP-001/002) ; champ Mayotte dans les séries Insee (extension 2026, +0,06 pt mécanique sur le chômage).

## SOURCES

1. Insee IR 192, 07/08/2026 (L2) : https://www.insee.fr/fr/statistiques/9032359
2. Insee IR 186, 30/07/2026 (L2) : https://www.insee.fr/fr/statistiques/9032830
3. Insee Première 2106, 29/05/2026 (L2) : https://www.insee.fr/fr/statistiques/8997691
4. Insee tableau de bord conjoncture, 25/08/2026 (L2) : https://www.insee.fr/fr/statistiques/2107840
5. France Travail BMO 2026 (L2) : https://statistiques.francetravail.org/bmo/bmo?lg=0&pp=2026&ss=1
6. Banque de France, défaillances juin 2026, 07/08/2026 (L2) : https://www.banque-france.fr/fr/statistiques/entreprises/defaillances-dentreprises-2026-06
7. EPSS Synthèse Financement (L2) : https://evaluation.securite-sociale.fr/home/financement/SyntheseFinancement.html
8. FIPECO fiche 13, 20/06/2026 (L2) : https://www.fipeco.fr/fiche/Les-cotisations-sociales
9. IMF blog, 12/03/2026 (403, snippet) : https://www.imf.org/en/blogs/articles/2026/03/12/europe-can-regain-its-productivity-edge-by-scaling-up
10. Draghi report (snippet) : https://commission.europa.eu/topics/competitiveness/draghi-report_en
11. 2024 Ageing Report (snippet) : https://economy-finance.ec.europa.eu/system/files/2023-11/ip257_en_1.pdf

## REQUEST_LOG

| # | Type | Cible | Résultat |
|---|---|---|---|
| 1 | @FETCH | BdF défaillances 2026-06 | 200, INSPECTÉ (tableaux A/B) |
| 2 | @FETCH | IMF blog | 403 → snippet conservé |
| 3 | @FETCH | Insee tableau de bord 2107840 | 200, INSPECTÉ |
| 4-10 | (réutilisés de la session) | Insee 192/186/2106, BMO, EPSS, FIPECO 13 | INSPECTÉS (L2, sessions précédentes) |
| 11 | @MNEMO_Q | recherche mémoire | ÉCHEC paramètres → MNEMO_UNAVAILABLE |

**Gate 19a :** à exécuter ; BLOCKED attendu (branche protégée main), checks de contenu visés PASS.

---
*Fin du dossier. Référentiel : 20 indicateurs L2 France + 5 snippets Europe + 1 GAP. L'Acte charnière peut être rédigé sur cette base.*
