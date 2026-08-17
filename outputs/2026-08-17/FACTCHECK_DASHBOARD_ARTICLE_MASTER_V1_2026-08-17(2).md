# FACTCHECK — Dashboard maître de l’article V1

**Date de gel :** 2026-08-17 16:02 Europe/Paris  
**Statut :** `ACTIVE / ARTICLE_PREP / EVIDENCE_FIRST`  
**Objet :** suivi unique de l’article en préparation sur l’écosystème français/européen du fact-checking, de l’intégrité informationnelle et de ses interfaces avec financeurs, plateformes, certification, recherche et régulation.

## 1. Santé du corpus maître

| Indicateur | État |
|---|---:|
| Base avant consolidation | 66 337 enregistrements |
| Base après consolidation | **67 516 enregistrements** |
| Ajouts cumulés du 2026-08-17 | **1 179** |
| Enregistrements sémantiques ajoutés | **470** |
| Mentions dérivées ajoutées | **709** |
| JSON d’investigation intégrés | **16 / 16** |
| Intégrité SQLite | **OK** |
| `RECORD_ID` uniques | **OUI** |
| `CANONICAL_KEY` uniques | **OUI** |
| Lignes CSV = lignes SQLite | **67 516 = 67 516** |
| Colonnes CSV = SQLite | **33 = 33** |

**Masters canoniques :**
- `FACTCHECK_DATABASE_MASTER_V2_2026-08-16.sqlite`
- `FACTCHECK_DATABASE_MASTER_V2_2026-08-16.csv`
- contrôle : `FACTCHECK_DATABASE_MASTER_V2_INTEGRITY_CHECK_2026-08-17.json`

## 2. État de la thèse de l’article

### Établi ou fortement supporté

1. **Sédimentation institutionnelle longue.** Le couple réseau européen de fact-checkers + infrastructure commune est explicitement présent dans la politique de la Commission dès 2018, puis se densifie par repository, coopération/rémunération, standardisation, certification, capacité de crise et protection.
2. **Co-construction plutôt qu’invention tardive.** Le modèle actuellement le mieux supporté est une co-construction institutionnelle sédimentée : impulsion et financements publics, engagements de plateformes, infrastructures de recherche et professionnalisation/certification par les acteurs du champ.
3. **Dépendances financières parfois matérielles et indirectes.** Le cas Full Fact permet déjà un calcul quantifié ; plusieurs autres organisations présentent des portefeuilles multi-principals et des intermédiaires qui imposent de distinguer payeur immédiat et financeur ultime.
4. **Les garde-fous formels existent.** L’EFCSN prévoit évaluateurs externes, récusations, majorité qualifiée, délais et sanctions ; les dossiers d’admission montrent une friction réelle.
5. **Le risque analytique le plus intéressant est en amont du verdict.** Sélection des claims/cibles, accès à l’infrastructure, certification, données et incitations de projet sont des objets plus probants à mesurer que l’hypothèse simpliste d’un verdict directement dicté par un financeur.

### Non établi / interdit à surinterpréter

- `FINANCEMENT IMPORTANT` ≠ `CONTRÔLE ÉDITORIAL`.
- `MULTIPLEXITÉ DE RÔLES` ≠ `CONFLIT EFFECTIF`.
- `RÈGLES DE RÉCUSATION` ≠ `RÉCUSATION EFFECTIVE`.
- `ABSENCE DE DÉCISION INDEXÉE` ≠ `ABSENCE DE SANCTION`.
- Collusion, corruption ou capture réglementaire : **non établies** à ce stade.
- Le vocabulaire *trusted flaggers* utilisé en 2018 ne doit pas être assimilé au statut juridique ultérieur de signaleur de confiance du DSA.
- Un graphe de relations, un financement ou une appartenance commune ne constituent pas une chaîne causale indépendante.

## 3. Tableau de bord des investigations

| Investigation | P | Statut courant | Ce qui est acquis | Gate / manque principal |
|---|---:|---|---|---|
| `INV-ULTIMATE-PRINCIPAL-61` | P0 | **MATERIALITY_PASS_MULTI_CASE_PARTIAL** | Full Fact : dépendance directe Big Tech ~25,1 % en 2025 et >£1m Google l’année précédente ; Science Feedback : plusieurs principals >5 % ; monétisation de corpus documentée chez Maldita | Ratios primaires Maldita/Les Surligneurs ; Science Feedback 2025 ; comparabilité multi-cas |
| `INV-RECUSAL-ENFORCEMENT-64` | P0 | **FORMAL_PASS + ADMISSION_ENFORCEMENT_PASS / POSTCERT_OPEN** | Code formel + non-conformités / `Requires Action` et corrections observables dans les dossiers dpa/Maldita | Série post-certification : plaintes, sanctions, retraits, délais, récusations |
| `INV-DENOMINATOR-32X` | P0 | **HISTORICAL_SELECTION_PASS / CURRENT_REPLICATION_OPEN** | JEEA : 10 628 articles jusqu’en 07/2021 ; 232 claims multi-vérifiés, seulement 2 désaccords ; canal dominant = sélection | Dénominateur indépendant + matching 2022-2026 |
| `INV-REGTRACE-53B` | P0→P2 | **DOWNGRADED** | Reconnaissance EFCSN antérieure aux guidelines 2024 | Origine verbatim du §50 encore ouverte mais non critique |
| `INV-5M-ORIGIN-63` | P0→P1 | **MAJOR_GENEALOGY_PASS** | Réseau/repository tracés jusqu’à 2018-2021 | Origine précise protection + emergency response + redistribution |
| `INV-DATA-RIGHTS-AI-65` | P0 | **INFRASTRUCTURE_PASS + CORPUS_FEEDBACK_PASS / DOWNSTREAM_BIAS_OPEN** | Full Fact AI et FRAME réutilisent explicitement données annotées et fact-checks historiques pour filtrage, matching, alertes et republication | Test causal du feedback ; licences, clients, versioning, propagation des corrections, usages RAG/LLM |
| `INV-EFFECT-APPEALS-66` | P0 | **MECHANISM_PASS + FIRST_CASE_CHAIN_PASS / COHORT_OPEN** | Effets aval documentés par Meta/TikTok ; cas Surligneurs : rating trop strict → visibilité réduite → rating corrigé | 10-20 cas avec portée, appel, reversal, restauration et délai |
| `INV-NATURAL-EXPERIMENTS-62` | P0 | **QUASI_EXPERIMENT_DESIGN_PASS / OUTCOME_ESTIMATION_PENDING** | 4 chocs datés : Google→Full Fact, Meta/TikTok→Science Feedback, entrée Meta→Surligneurs, sortie Meta USA vs maintien France/UE | Séries pré/post, contrôles négatifs et estimation des outcomes |

## 4. Maturité de l’article

| Bloc | Maturité | Publication aujourd’hui |
|---|---|---|
| Généalogie 2018→2025 | **FORTE** | Oui, avec bornes causales |
| Architecture institutionnelle / standardisation | **FORTE** | Oui |
| Financement / principal ultime | **MOYENNE+** | Oui pour cas quantifiés ; prudence pour généralisation |
| Gouvernance formelle EFCSN | **FORTE descriptive** | Oui |
| Effectivité sanctions/récusations | **FAIBLE / OUVERTE** | Non comme conclusion |
| Biais de sélection 2022→2026 | **HISTORIQUE SOLIDE / ACTUEL OUVERT** | Publier le résultat 2009-2021 avec borne stricte ; pas de généralisation 2026 |
| Effets aval sur portée/modération | **MOYENNE / PREMIER CAS COMPLET PARTIEL** | Oui pour mécanisme + cas Surligneurs ; pas de généralisation sans cohorte |
| Influence causale des financeurs sur agenda | **NON ÉTABLIE** | Hypothèse uniquement |
| Collusion / corruption / capture | **NON ÉTABLIE** | Ne pas affirmer |
| Données / IA / RAG | **FORTE SUR INFRASTRUCTURE / BIAIS AVAL OUVERT** | Oui pour la boucle corpus→matching ; non pour un biais partisan aval |

## 5. Points contradictoires à conserver visibles

- Les organisations peuvent être financièrement dépendantes de certains principals **et** publier des critiques contre eux : cela réfute la règle générale « financeur = silence » sans résoudre les questions de sélection, fréquence ou intensité.
- Les mécanismes EFCSN comportent de vrais garde-fous d’admission ; leur présence contredit l’hypothèse d’un club totalement sans contrôle, mais leur efficacité post-certification reste à mesurer.
- La Commission finance et cadre des objectifs de politique publique, tandis que le contenu détaillé des standards est élaboré par un consortium et la communauté : éviter les formulations d’imposition unilatérale non démontrée.
- L’architecture 2025 est une consolidation de briques antérieures, non une création ex nihilo ; toute narration d’un « basculement soudain » doit être abandonnée.

## 6. Gates avant version forte de l’article

**GATE A — matérialité financière :** obtenir au moins plusieurs cas comparables avec principal ultime + ratio budgétaire.  
**GATE B — effectivité de gouvernance :** documenter plaintes, décisions, sanctions, retraits et récusations effectives.  
**GATE C — sélection :** répliquer ou falsifier l’asymétrie de sélection sur 2022-2026 avec dénominateur contrôlé.  
**GATE D — causalité :** au moins trois chaînes causales indépendantes doivent survivre à la falsification avant toute montée de thèse.  
**GATE E — effets :** mesurer plusieurs cas de bout en bout, de la qualification au rétablissement éventuel après appel.

## 7. Prochaine séquence recommandée

1. **Test causal Data/IA** : obtenir un univers indépendant de discours et mesurer si le corpus historique modifie la probabilité de détection/sélection.
2. **Cohorte Effects** : construire 10-20 chaînes `rating → effet → appel → correction → restauration` avec métriques et délais.
3. **Natural experiment Full Fact** : série mensuelle 2024-2026 autour de la coupure Google du 16/10/2025, puis contrôles négatifs.
4. **Natural experiments Science Feedback / Surligneurs** : pré/post début 2025 et mars 2024, avec contrôles d’actualité et autres financements.
5. **Enforcement post-certification** : obtenir/exploiter directement les décisions/Annual Reports et logs de récusation.
6. **Finance final ratios** : compléter Maldita, Les Surligneurs et Science Feedback 2025.
7. **32X 2022-2026** : exécuter le matching dès qu’un corpus indépendant brut (Pluralisme/équivalent) est accessible.

### Delta Cycle 14 — 17/08/2026

- `61` monte de `PARTIAL_PASS` à **matérialité multi-cas partiellement établie**.
- `64` gagne un **PASS empirique à l’admission/renouvellement** ; le post-certification reste ouvert.
- `65` passe de piste à **mécanisme d’infrastructure établi** : corpus historique → filtrage/matching/alertes.
- `66` gagne un **premier cas français** de chaîne rating → réduction de visibilité → correction du rating.
- `32X` est requalifié : **sélection historique fortement supportée**, mais aucune extrapolation 2022-2026 autorisée.
- `62` passe de piste à **quatre quasi-expériences prêtes à être estimées**.
- Hypothèse de travail prioritaire : **`sélection → corpus → automatisation → resélection`**, et non `financeur → verdict`.

## 8. Conclusion maximale autorisée à ce stade

> L’écosystème européen du fact-checking apparaît comme un champ progressivement institutionnalisé et co-construit, reliant politiques publiques, financements, plateformes, recherche, standards professionnels et infrastructures communes. Certaines dépendances économiques sont substantielles ou indirectes et certains mécanismes d’accès sont structurants. En parallèle, des contre-pouvoirs formels et des contre-exemples existent. Les données actuelles justifient une enquête serrée sur la sélection, la matérialité financière, l’effectivité des garde-fous et les effets aval ; elles ne suffisent pas à établir un contrôle éditorial systémique, une collusion, une corruption ou une capture réglementaire.

## 9. Règle de maintenance

Ce fichier devient le **dashboard maître de l’article**. Toute investigation significative doit mettre à jour :
- le statut de l’investigation ;
- les claims confirmés, réfutés ou abaissés ;
- les contradictions et connaissances négatives ;
- les gates ;
- la maturité de publication ;
- la prochaine action ;
- la date de synchronisation avec les deux masters V2.
