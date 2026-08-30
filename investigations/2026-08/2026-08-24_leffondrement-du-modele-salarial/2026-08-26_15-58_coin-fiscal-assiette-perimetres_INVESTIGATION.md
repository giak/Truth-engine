# INVESTIGATION — Coin fiscal, financement social et tableau des périmètres (48/55/64/90/98 %)

```yaml
RUN_MANIFEST:
  ENGINE_VERSION: 2.9
  STATE: FINAL
  RUN_ID: 20260826-1555-coin-fiscal-assiette-perimetres
  PARENT_RUN_ID: NONE
  AS_OF: 2026-08-26
  INPUT_KIND: TOPIC
  MISSION_MODE: INVESTIGATION
  INPUT_REF: NONE
  SUBJECT_SLUG: coin-fiscal-assiette-perimetres
  INVESTIGATION_PATH: investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-26_15-58_coin-fiscal-assiette-perimetres_INVESTIGATION.md
  SCOPE: lead_question=le couple « 98 %→55 % » (tour 3) et les couples 64→48 % et 90→48 % sont-ils compatibles ou contradictoires ? | object_question=quel est le poids réel des cotisations sociales dans le financement du modèle social français, périmètre par périmètre, et que vaut la mécanique « baisse de masse salariale → baisse de recettes » ? | period=1980-2026 | geo=France | domains=fiscalité, protection sociale, comptabilité nationale | actors=EPSS, FIPECO, DREES, Cour des comptes, Insee, Sénat | exclusions=comparaison internationale détaillée (INV-P0-08) | limits=MNEMO paramétré indisponible ; vie-publique.fr sans texte ; DREES PDF non inspecté ; ART-V001 utilisé comme proxy documentaire du corpus
  COMPLEXITY: $CX_SCORE=7 → $CX=COMPLEX
  CHECKPOINT_SEQ: 1
  LAST_COMPLETED: 18b
  NEXT_ACTION: NONE
  RESUME_COUNT: 0
  ROUTE_OVERRIDES: []
  LOADED_MODULES: [SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, TEMPLATE.md, clusters/ICEBERG.md, clusters/MONEY.md, clusters/FRAMING.md, clusters/POWER.md, clusters/FRAGMENTATION.md]
  DEGRADED_FLAGS: [MNEMO_UNAVAILABLE_PARAMETRE, VIE_PUBLIQUE_NO_TEXT, DREES_PDF_NON_INSPECTE, ART_V001_PROXY_NON_PRIMAIRE]
MNEMO_ROW: FAILED_PARAM_TRANSMISSION
SELF_WRITE_ROW: PENDING_AT_SERIALIZATION
WRITEBACK_ROW: 0_WRITTEN (éligibles ✦/✧ mais MNEMO indisponible)
```

## MANIPULATION_REPORT

| Symbole | Score | Observation nommée |
|---|---|---|
| Ξ | 6 | Le débat public mélange périmètres et années ; aucun document grand public ne présente la table de correspondance des dénominateurs |
| € | 6 | Assiette travail = la plus taxée ; 77 Md€ d'allègements = transfert État vers Sécu ; enjeu de capture du prélèvement |
| Λ | 7 | 48/55/64/98 % circulent sans périmètre : le cadre interprétatif est contraint par le dénominateur choisi (grossir ou minimiser la dépendance au travail) |
| Ω | 2 | Faible |
| Ψ | 1 | Faible |
| ↕ | 5 | Travail taxé vs consommation intermédiaire non taxée : asymétrie constitutive du débat IA |
| Φ | 1 | Faible |
| Σ | 1 | Faible |
| Κ | 3 | « La Sécu ne repose plus sur les cotisations » : demi-vérité par périmètre |
| ρ | 3 | FIPECO/EPSS fournissent les instruments de vérification (contre-pouvoir épistémique) |
| κ | 1 | Non établi |
| ⫸ | 5 | EPSS, FIPECO, DREES, Insee convergent sur la diversification du financement, avec dénominateurs distincts |
| ⚔ | 0 | Aucune coordination établie |
| 🌐 | 2 | Graphe simple institutions/statisticiens |
| ⏰ | 3 | Séquence 1991 CSG → 1996 CRDS → allègements 1993-2019 : diversification étagée |

## 1. RÉSUMÉ EXÉCUTIF

**RÉPONSE À L'OBJECT_QUESTION.** Le poids des cotisations sociales dépend du périmètre, et les écarts constatés (48, 55, 64, 90, 98 %) sont des dénominateurs différents, pas des contradictions (tableau §2). Le couple canonique, doublement vérifié L2 en session : **la part des cotisations dans le financement de la Sécurité sociale (régimes de base) est passée de 64 % en 1990 à 48 % en 2025** (EPSS, indicateur 1-3-1, INSPECTÉ), ce que FIPECO confirme à 48 % pour 2023 « hors cotisations de l'État employeur », contre ~90 % à la fin des années 1980 (INSPECTÉ). Le couple « 98 % (1980) → 55 % (2025) » attribué à FIPECO par le corpus (ART-V001) relève vraisemblablement du périmètre **administrations de sécurité sociale (ASSO) en comptabilité nationale**, mais **aucune source n'a pu être inspectée en session** : il reste SNIPPET, à ancrer avant usage. La mécanique « baisse de masse salariale → baisse de recettes » est structurellement valide mais amortie : cotisations (48 %) + CSG majoritairement assise sur l'activité et les revenus de remplacement ⇒ un choc sur l'emploi réduit les deux ; l'élasticité citée (0,95) et le montant 443 Md€ restent à ancrer primairement (GAP). Le déficit Sécu 2025 de 21,6 Md€ est confirmé L2 et antérieur à l'IA (EPSS : -10,8 Md€ 2023, -15,3 Md€ 2024, -21,6 Md€ 2025).

**RÉPONSE À LA LEAD_QUESTION (verdict borné).** « 98 %→55 % » n'est pas contredit par les sources inspectées, mais il n'est pas confirmé non plus : il coexiste avec deux autres séries vérifiées (64→48 % EPSS ; 90→48 % FIPECO) qui mesurent la Sécurité sociale stricte. La formulation robuste pour tout article : **les cotisations ont perdu environ un tiers de leur poids relatif dans le financement de la Sécurité sociale en 35 ans (64 % en 1990 → 48 % en 2025), et la France reste le pays de l'UE où les cotisations patronales sont les plus élevées en pourcentage du PIB** (dernière affirmation : corpus ART-V001, à ancrer).

**Faits clés** : FCT-001 (64→48 %, EPSS, L2) ; FCT-002 (90→48 %, FIPECO hors État employeur, L2) ; FCT-003 (98→55 % ASSO, ⁅ GAP) ; FCT-004 (déficit 21,6 Md€ 2025, L2) ; FCT-005 (77,3 Md€ allègements 2024, ✧ partiel) ; FCT-006 (443 Md€/assiette 1 078 Md€/élasticité 0,95, ⁅).

## 2. TABLEAU DES PÉRIMÈTRES (pièce centrale, à reproduire dans tout article)

| Périmètre | Définition | Valeurs | Années | Source | Statut en session |
|---|---|---|---|---|---|
| **Sécurité sociale (régimes de base)** | Financement des régimes obligatoires (maladie, vieillesse, famille, AT-MP, autonomie) | cotisations **64 % → 48 %** | 1990 → 2025 | EPSS, indicateur n°1-3-1, Synthèse Financement (INSPECTÉ) | **VERIFIE L2** |
| **Sécurité sociale, hors cotisations État employeur** | Idem, hors cotisations de l'État employeur (fonctionnaires) | ~90 % (fin années 1980) → **48 %** (2023) ; CSG 20 %, TVA 8 %, autres ITAF 8 % | fin 1980s → 2023 | FIPECO, fiche 18/02/2025 (INSPECTÉ) | **VERIFIE L2** |
| **ASSO (comptabilité nationale)** | Administrations de sécurité sociale (Insee : S13.2) | **98 % (1980) → 55 % (2025)** | 1980 → 2025 | FIPECO fiche 13, §B.2 « La part des cotisations dans le financement de la sécurité sociale » (INSPECTÉ) | **VERIFIE L2** |
| ASSO (ressources) | Prélèvements sur les ménages | 53 % des ressources ASSO | 2022 | EPSS fiche 1-1-2 (snippet) | SNIPPET ⁅ |
| **Protection sociale totale** | Sécu + assurance chômage + retraites complémentaires + prestations employeurs | ressources 997,8 Md€ (34,2 % PIB) ; ITAF 31 % des ressources | 2024 / 2022 | DREES CPS fiche 04 (PDF, non inspecté) ; vie-publique (snippet) | SNIPPET ⁅ |
| Finances publiques (contexte) | APU | déficit 152,5 Md€ (5,1 %), dette 115,7 %, ASSO −6,7 Md€ | 2025 | Insee Première 2106 (INSPECTÉ, session précédente) | **VERIFIE L2** |

**Lecture imposée** : 48 % (EPSS/FIPECO, Sécu) et 55 % (ASSO) et 31 % ITAF (protection sociale totale) ne sont **jamais interchangeables**. Tout article citant l'un doit préciser le périmètre et l'année. La règle de formulation : « cotisations = 48 % du financement de la Sécurité sociale en 2025 (régimes de base), contre 64 % en 1990 ; selon le périmètre retenu (administrations de sécurité sociale en comptabilité nationale), la part historique 1980 de ~98 % serait tombée à ~55 % » — la deuxième clause seulement après ancrage primaire (INV-P0-04bis).

## 3. CHRONOLOGIE (financement)

| Date | Événement | Source |
|---|---|---|
| 1945 | Création Sécu, modèle bismarckien de cotisations | FIPECO (contexte) |
| 1980 | Part cotisations : ~98 % (ASSO, selon corpus) / ~90 % (Sécu hors État employeur, FIPECO) | corpus / FIPECO |
| 1990 | Part cotisations Sécu : 64 % (EPSS) | EPSS L2 |
| 1991 | Création CSG (diversification du financement) | EPSS, FIPECO (contexte) |
| 1993-2019 | Montée des allègements généraux de cotisations (compensés par l'État, loi 1994) | FIPECO |
| 1996 | Création CRDS | EPSS |
| 2014 | Allègements généraux : 20,9 Md€ (selon corpus/Cour) | ART-V001 ⁅ |
| 2023 | Déficit Sécu −10,8 Md€ ; cotisations 48 % (FIPECO) | EPSS L2 / FIPECO L2 |
| 2024 | Allègements : 77,3 Md€ (Cour des comptes, rapport Sécu 2025) ; déficit −15,3 Md€ | snippets vie-publique/miroir + EPSS L2 |
| 2025 | Déficit −21,6 Md€ ; cotisations 48 % (EPSS) | EPSS L2 |
| 2026-2029 | Trajectoire LFSS : −19,4 Md€ (2026), −23,7 Md€ (2029) sans mesures | EPSS L2 |

## 4. RÉSEAU D'ACTEURS

| Acteur | Rôle | Apport | Statut |
|---|---|---|---|
| EPSS (Évaluation des politiques de Sécu) | Institutionnel ◈ | Indicateur 1-3-1, séries 1990-2025 | INSPECTÉ |
| FIPECO (F. Ecalle) | Analyste indépendant ◉ | Fiche 18/02/2025, 48 %/90 %, hors État employeur | INSPECTÉ |
| DREES | Statisticien ◈ | CPS 2024 (997,8 Md€) | PDF non inspecté |
| Cour des comptes | Institutionnel ◈ | Rapport Sécu 2025 : allègements 77,3 Md€ | snippets concordants |
| Insee | Statisticien ◈ | Comptes publics 2025 (5,1 %, 115,7 %) | INSPECTÉ (session) |
| Sénat (PLFSS 2026) | Institutionnel ◈ | Rapport Delahaye : déficit 23 Md€ (ex-ante) | INSPECTÉ partiel |

## 5. CHAÎNES / PELOTE

CAUSAL_ROUTE=REQUIRED (mécanisme masse salariale → recettes).

- **CAU-001 Mécanique cotisations (SUPPORTED, L2)** : masse salariale ↓ → assiette cotisée ↓ → recettes Sécu ↓, puisque les cotisations pèsent encore 48 % du financement (EPSS). Type : MECHANISM, sourcé.
- **CAU-002 Mécanique CSG (PARTIAL)** : la CSG (~145 Md€/an, corpus) est assise sur revenus d'activité + revenus de remplacement : un choc d'emploi réduit les deux (cotisations ET CSG), contrairement à une diversification parfaite. Le montant 145 Md€ reste à ancrer (snippet). Type : MECHANISM, partiellement sourcé.
- **CAU-003 Amortisseur allègements (SUPPORTED, partiel)** : les allègements (77,3 Md€) sont compensés par l'État (loi 1994) : l'érosion de l'assiette cotisée dégrade mécaniquement le solde public avant de toucher les prestations. Type : ENABLER, sourcé au niveau du montant.
- **GAP-001** : élasticité 0,95 et 443 Md€ (2025, assiette 1 078 Md€) attribués à FIPECO par ART-V001 : fiche correspondante non inspectée → GAP ACCESS/SNIPPET.

SOURCE_PROVENANCE : ART-V001 (`2026-08-26_ia-modele-salarial-forensique_ARTICLE.md`) est un livrable du corpus lignée A qui cite FIPECO juin 2026 (443 Md€, 14,8 % PIB, assiette 1 078 Md€, élasticité 0,95, taux moyen 34 %) et la Cour (allègements 20,9→77 Md€). Ce document est un proxy documentaire, pas une source primaire : il sert d'entrée à la vérification, jamais de preuve.

## 6. CARTE DIALECTIQUE

- **Position A (corpus vidéo)** : « l'assiette salariale porte tout le modèle social ; l'IA érode cette assiette → effondrement ». Vraie sur le mécanisme, fausse sur l'ampleur : la diversification (48 % cotisations) et la CSG assise aussi sur revenus de remplacement amortissent le choc.
- **Position B (corpus ART-V001)** : « la dépendance au travail a déjà été réduite de moitié en 40 ans ; le vrai déséquilibre de demain ne passera peut-être pas par la masse salariale ». Vraie en tendance, mais la CSG dépend encore majoritairement de l'activité : la diversification n'est pas une immunité.
- **Arbitrage** : la tension se résout par le périmètre (tableau §2). La proposition robuste : « le financement social est structurellement dépendant du travail, mais cette dépendance a été réduite de 64 % à 48 % en 35 ans ; l'IA attaque une assiette déjà en diversification, pas une assiette immuable ». Titre « effondrement commencé en 1991 » : rejeté (jalon de diversification, pas d'effondrement démontré).

## 7. CARTE DES PREUVES

### FACT_REGISTRY_V1

`FCT-001 | FACT | ✦ | https://evaluation.securite-sociale.fr/home/financement/SyntheseFinancement.html | EPSS◈ | 2026-05 | coin-fiscal-assiette-perimetres | Cotisations = 64 % du financement de la Sécu en 1990 → 48 % en 2025 (indicateur n°1-3-1) ; déficit −21,6 Md€ 2025 ; trajectoire −19,4 Md€ 2026 / −23,7 Md€ 2029 | mem:-`

`FCT-002 | FACT | ✦ | https://www.fipeco.fr/fiche/Quel-financement-pour-la-s%C3%A9curit%C3%A9-sociale-%253F | FIPECO◉ | 2025-02-18 | coin-fiscal-assiette-perimetres | 48 % des cotisations (2023) vs ~90 % fin années 1980, hors cotisations État employeur ; CSG 20 %, TVA 8 %, autres ITAF 8 % | mem:-`

`FCT-003 | FACT | ✦ | https://www.fipeco.fr/fiche/Les-cotisations-sociales (§B.2) | FIPECO◉ | 2026-06-20 | coin-fiscal-assiette-perimetres | 98 % (1980) → 55 % (2025) des ressources des administrations de sécurité sociale (ASSO) : citation exacte FIPECO, périmètre ASSO, remplacement par CSG/TVA | mem:-`

`FCT-004 | FACT | ✦ | https://evaluation.securite-sociale.fr/home/financement/SyntheseFinancement.html | EPSS◈ | 2026-05 | coin-fiscal-assiette-perimetres | Déficit Sécu : −10,8 Md€ (2023), −15,3 Md€ (2024), −21,6 Md€ (2025) ; antérieur à l'IA | mem:-`

`FCT-005 | FACT | ✧ | Cour des comptes rapport Sécu 2025 via vie-publique (no-text) + miroir social (snippets concordants) | Cour◈ (snippets) | 2025-05 | coin-fiscal-assiette-perimetres | Allègements généraux de cotisations patronales : 77,3 Md€ en 2024, multipliés par ~4 depuis 2014 (20,9 Md€ selon corpus) | mem:-`

`FCT-006 | FACT | ✦ | https://www.fipeco.fr/fiche/Les-cotisations-sociales (§B.1) | FIPECO◉ | 2026-06-20 | coin-fiscal-assiette-perimetres | Cotisations 443 Md€ en 2025 (net des allègements, 14,8 % PIB, 34 % des prélèvements obligatoires), après 429 Md€ en 2024 ; assiette 1 078 Md€ (738 privé, 171 fonctionnaires, 105 indépendants) ; 1 pt = 10,8 Md€ ; élasticité 0,95 aux revenus d'activité (+1 % ≈ +4,4 Md€) | mem:-`

`FCT-007 | FACT | ✦ | même fiche FIPECO (§A.4) | FIPECO◉ | 2026-06-20 | coin-fiscal-assiette-perimetres | Taux moyen des cotisations : ~30 % fin 1970s → 40 % mi-1990s → 38 % en 2017 → 34 % en 2025 | mem:-`

`FCT-008 | FACT | ✦ | même fiche FIPECO (note [1]) | FIPECO◉ | 2026-06-20 | coin-fiscal-assiette-perimetres | La CSG n'est pas une cotisation sociale mais un impôt sur le revenu : terminologie à respecter dans tout article | mem:-`

`FCT-009 | FACT | ✦ | même fiche FIPECO (§C) | FIPECO◉ | 2026-06-20 | coin-fiscal-assiette-perimetres | France : cotisations 14,8 % du PIB en 2025 (Eurostat), derrière l'Allemagne 17,2 % ; la France était le pays UE le plus élevé en 2018 ; cotisations patronales les plus élevées de l'UE en % du PIB derrière l'Estonie ; répartition 68 %/32 % (employeurs/ménages) vs 54 %/46 % UE | mem:-`

`FCT-010 | FACT | ✦ | même fiche FIPECO (§D.3) | FIPECO◉ | 2026-06-20 | coin-fiscal-assiette-perimetres | Modèle Insee/DG Trésor : +1 pt de PIB de cotisations employeurs → −1,0 % PIB et −320 000 emplois à 5 ans ; salariales → −0,8 % PIB et −260 000 emplois ; tendance long terme −360 000 emplois | mem:-`

### CONTRADICTION_LEDGER

1. **48 % (2023, FIPECO) vs 48 % (2025, EPSS)** : coïncidence de niveau, périmètres quasi identiques, années différentes ; pas une contradiction.
2. **90 % fin années 1980 (FIPECO) vs 98 % 1980 (FIPECO)** : RÉSOLU. Deux périmètres distincts du même auteur : ~90 % = Sécu hors cotisations État employeur (fiche « Quel financement »), 98 % = ressources ASSO (fiche 13, §B.2). Les deux sont maintenant ancrés L2.
3. **« La Sécu ne repose plus sur les cotisations » (récit courant) vs 48 % cotisations** : faux en valeur (48 % est encore le premier poste) ; le récit minimise la dépendance résiduelle au travail.
4. **ART-V001 « la France est le pays UE aux cotisations patronales les plus élevées derrière l'Estonie » vs FIPECO « derrière l'Allemagne en 2025 (14,8 % vs 17,2 %) »** : cohérent après lecture : le premier cite les cotisations patronales en % du PIB (Estonie devant), le second les cotisations totales (Allemagne devant). Les deux affirmations FIPECO sont exactes, sur des objets différents (FCT-009).
5. **CSG comptée comme « cotisation » dans certains récits** : FIPECO tranche : la CSG est un impôt sur le revenu, pas une cotisation (FCT-008). Toute phrase « cotisations + CSG » doit être reformulée « prélèvements sociaux » ou distinguer les deux natures.

### TRACE_MATRIX (extrait)

| FCT | QRY/SRC | REFUTATION_SEARCHED | Résultat |
|---|---|---|---|
| FCT-001 | QRY-1 EPSS + FETCH | QRY-5 « cotisations 48 % Sécu contredit » | NONE (FIPECO, CGT, lafinancepourtous concordants) → ✦ |
| FCT-002 | QRY-2 FIPECO + FETCH | QRY-5 | NONE → ✦ |
| FCT-003 | QRY-3 « 98 % 55 % FIPECO ASSO » | QRY-6 | Aucune source inspectable → ⁅ |
| FCT-005 | QRY-4 Cour allègements | QRY-7 | NONE (vie-publique, miroir, Sénat concordants) → ✧ |

### EDI

A ⟐ : EPSS, Insee, Cour, Sénat, DREES. ◉ : FIPECO (indépendant). ⟐̅ : aucun contre-discours structuré du statu quo (par ex. défense d'un financement intégralement par cotisations) trouvé dans les bornes → GAP EDI côté B. Aucune conclusion ne repose sur une seule famille pour les faits centraux.

## 8. PÉRIMÈTRE & LIMITES

**Inclusions** : financement Sécu (régimes de base), ASSO, protection sociale (contexte), allègements, déficit, période 1980-2026.
**Exclusions** : comparaison internationale détaillée (INV-P0-08), réforme des retraites, détails ITAF.
**Limites (mises à jour)** : 98 %→55 % ANCRÉ (FIPECO fiche 13 §B.2) ; 443 Md€/assiette/élasticité ANCRÉS (FIPECO fiche 13 §B.1) ; restent non inspectés : 20,9 Md€ (2014, allègements, via ART-V001), CSG ~145 Md€/an, DREES PDF, vie-publique ; MNEMO indisponible (pas de write-back).

## SOURCES

1. EPSS, « Synthèse Financement » (INSPECTÉ) : https://evaluation.securite-sociale.fr/home/financement/SyntheseFinancement.html
2. FIPECO, « Quel financement pour la sécurité sociale ? », 18/02/2025 (INSPECTÉ) : https://www.fipeco.fr/fiche/Quel-financement-pour-la-s%C3%A9curit%C3%A9-sociale-%253F
2bis. **FIPECO, « Les cotisations sociales », fiche 13, 20/06/2026 (INSPECTÉ intégralement, §A.4, §B.1, §B.2, §C, §D.3)** : https://www.fipeco.fr/fiche/Les-cotisations-sociales
3. Insee Première n°2106, 29/05/2026 (INSPECTÉ, session précédente) : https://www.insee.fr/fr/statistiques/8997691
4. vie-publique.fr, « Sécurité sociale : un financement non assuré à terme » (NO TEXT) : https://www.vie-publique.fr/en-bref/298737-securite-sociale-un-financement-non-assure-terme
5. Sénat, rapport PLFSS 2026 (INSPECTÉ partiel) : https://www.senat.fr/rap/a25-126/a25-126_mono.html
6. DREES, CPS 2025 fiche 04 (PDF, non inspecté) : https://drees.solidarites-sante.gouv.fr/sites/default/files/2026-05/CPS2025%20-%20Fiche%2004%20-%20Le%20financement%20de%20la%20protection%20sociale%20en%202024.pdf
7. ART-V001 (proxy corpus, non primaire) : articles/2026-08-26/IA_TRAVAIL_ARTICLE_ARCHIVE_2026-08-26/01_ARTICLE_VERSIONS/2026-08-26_ia-modele-salarial-forensique_ARTICLE.md

## REQUEST_LOG

| # | Type | Cible | Résultat |
|---|---|---|---|
| 1 | @FETCH | EPSS SynthèseFinancement | 200, INSPECTÉ |
| 2 | @WEB | FIPECO financement cotisations | fiche identifiée |
| 3 | @FETCH | FIPECO fiche | 200, INSPECTÉ |
| 4 | @WEB | Cour allègements 77 Md€ | vie-publique + miroir + Sénat |
| 5 | @FETCH | vie-publique | NO TEXT (JS) |
| 6 | @FETCH | Sénat PLFSS 2026 | 200, INSPECTÉ partiel |
| 7 | @WEB | réfutation 48 % | NONE |
| 8 | @WEB | réfutation 98/55 | fiche FIPECO 13 identifiée |
| 8bis | @FETCH | FIPECO fiche 13 (max 30k) | 200, INSPECTÉ intégralement : 98→55 % (§B.2), 443 Md€/assiette/élasticité (§B.1), taux moyen (§A.4), CSG impôt (note 1), comparaison UE (§C), modèle emploi (§D.3) |
| 9 | @CODE_SEARCH | ART-V001 chiffres FIPECO | proxy trouvé (443 Md€, 0,95, 98/55, 20,9/77) |

**Gate 19a :** re-exécution requise après les mises à jour d'ancrage (§16h00). Verdict attendu inchangé : BLOCKED (branche protégée main) avec checks de contenu PASS. À rejouer avant toute certification en worktree.

---
*Fin du dossier.*
