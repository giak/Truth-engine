# INVESTIGATION : La fuite hors assiette nationale : destination étrangère du gain (licences US, import technologique, profits délocalisables)

```yaml
RUN_MANIFEST:
  ENGINE_VERSION: 2.9
  STATE: FINAL
  RUN_ID: 20260826-1650-fuite-hors-assiette-nationale
  PARENT_RUN_ID: NONE
  AS_OF: 2026-08-26
  INPUT_KIND: TOPIC
  MISSION_MODE: INVESTIGATION
  INPUT_REF: V3_1 §XI ; INV-2026-08-25-0900-COUT-LICENCES-S3NS-BLEU ; INV-2026-08-25-1000-EMBARGO-US ; INV-P0-04 (périmètres) ; blueprint §5
  SUBJECT_SLUG: fuite-hors-assiette-nationale
  INVESTIGATION_PATH: investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-26_16-50_fuite-hors-assiette-nationale_INVESTIGATION.md
  SCOPE: lead_question=la destination étrangère du gain (licences US, import de services numériques, profits délocalisables) est-elle documentée ou inférée ? | object_question=consolider le pont XI/lignée A : temps économisé → valeur → où part-elle ? Documenter les canaux de sortie hors assiette française (cotisations, IS, CSG), fixer le statut probatoire des estimations 11-25 M€/an et 24-37 M€/an, et la projection 2028 | period=2024-2028 | geo=France, États-Unis | domains=fiscalité, cloud, souveraineté | actors=État français, DINUM, S3NS (Thales/Google), Bleu (Orange/Capgemini/Microsoft), ANSSI, Cour des comptes | exclusions=mesure du déficit (INV-P0-08) ; périmètres du financement social (INV-P0-04) ; formulation militante cloud (INV-P1-09) | limits=le flux exact des licences est un secret commercial (enquête blanche) : bornes uniquement
  COMPLEXITY: $CX_SCORE=6 → $CX=COMPLEX
  CHECKPOINT_SEQ: 1
  LAST_COMPLETED: 18b
  NEXT_ACTION: NONE
  RESUME_COUNT: 0
  ROUTE_OVERRIDES: []
  LOADED_MODULES: [SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, TEMPLATE.md, clusters/ICEBERG.md, clusters/MONEY.md, clusters/FRAMING.md, clusters/POWER.md]
  DEGRADED_FLAGS: [MNEMO_UNAVAILABLE_PARAMETRE]
MNEMO_ROW: FAILED_PARAM_TRANSMISSION
SELF_WRITE_ROW: PENDING_AT_SERIALIZATION
WRITEBACK_ROW: 0_WRITTEN
```

## MANIPULATION_REPORT

| Symbole | Score | Observation nommée |
|---|---|---|
| Ξ | 6 | Le flux exact des licences US est un secret commercial : l'enquête blanche est le verdict (F-018 cout-licences) |
| € | 7 | Le mécanisme de double fuite (cotisations ↓ + IS ↓) est le cœur du pont XI : le gain sort de l'assiette sociale ET de l'assiette de l'IS |
| Λ | 5 | « Fuite » vs « import de services » : la neutralité comptable (balance des services) vs le cadrage politique |
| ⫸ | 4 | DINUM (84 M€, +62 %), Cour des comptes (surcoût 25-40 %), FIPECO (élasticité) : sources indépendantes convergentes |
| ⏰ | 3 | La croissance de 62 %/an rend la projection 2028 sensible : > 100 M€ possibles |

CLUSTERS : MONEY (€=7), ICEBERG (Ξ=6), POWER (⫸).

## 1. RÉSUMÉ EXÉCUTIF

**RÉPONSE À LA LEAD_QUESTION.** La destination étrangère du gain est **partiellement documentée, pas mesurée**. Trois canaux de sortie sont documentés par sources primaires : (1) le flux de licences US via S3NS/Bleu (ordre de grandeur borné, voir §4) ; (2) l'import de services numériques (hors périmètre de cette investigation, GAP) ; (3) la délocalisation des profits logiciels (51 Md$ évités par 4 Big Tech **aux États-Unis** : à ne jamais convertir en recettes françaises perdues, décision actée). Le montant exact des licences est **secret commercial** : l'enquête est blanche, les bornes sont des modélisations.

**RÉPONSE À L'OBJECT_QUESTION.** Le pont conceptuel est le suivant : **la masse salariale est l'assiette des cotisations (élasticité 0,95, FIPECO) ; si le temps de travail économisé est remplacé par des licences logicielles importées, le gain sort simultanément de l'assiette sociale (cotisations) et de l'assiette de l'IS (profits à l'étranger)**. C'est la « fuite hors assiette » : non pas une perte de recettes déjà constatée, mais un **mécanisme de désalimentation** du modèle social, dont l'ordre de grandeur cloud est borné (11-25 M€/an, voire 24-37 M€/an selon les hypothèses) et la projection 2028 supérieure à 100 M€ à +62 %/an : **sans que ce montant soit mesuré**. Le statut probatoire est clair : **INFERENCE bornée, jamais FACT**.

## 2. CHRONOLOGIE

| Date | Publication | Valeur clé |
|---|---|---|
| 07/2021 | Circulaire « Cloud au centre » | cloud = mode d'hébergement par défaut de l'État |
| 10/2025 | Cour des comptes (souveraineté numérique) | surcoût SecNumCloud « entre 25 et 40 % » ; absence de « chiffrage d'ensemble » |
| 03/2026 | DINUM (« L'État accélère sa transition cloud ») | marché « Nuage public » 84 M€ en 2025 (+62 %), 847 projets (+42 %) |
| 03/2026 | Audition Capgemini (Assemblée nationale) | Bleu a « un accord commercial avec Microsoft », termes non divulgués |
| 06/2026 | FIPECO fiche 13 (ancrée INV-P0-04) | cotisations 443 Md€, élasticité 0,95, assiette 1 078 Md€ |

## 3. FAITS (registre : sources primaires du corpus ancrées)

### 3.1 Le flux cloud public français

| ID | Fait | Source | Statut |
|---|---|---|---|
| F-001 | Marché « Nuage public » : **84 M€ de commandes en 2025 (+62 % vs 2024)**, 847 projets actifs (+42 %), 70 % vers fournisseurs européens, 99 % sur le périmètre État | DINUM, 26/03/2026 (INV-cout-licences F-010) | **L2** (corpus ancré) |
| F-002 | 70 % de 84 M€ ≈ 59 M€ vers fournisseurs européens : incluant OVHcloud/Scaleway/Outscale (réellement souverains) ET S3NS/Bleu (technologie US) | Calcul à partir de DINUM (F-011) | L1 (calcul) |
| F-003 | S3NS = Thales + Google Cloud ; Bleu = Orange/Capgemini + Microsoft Azure ; **100 % du code applicatif est américain** | NextHop, 27/06/2025 (performativité F-001/F-002 ; embargo F-001) | **L2** (corpus ancré) |
| F-004 | Surcoût d'une infrastructure SecNumCloud : « **entre 25 et 40 %** » (Cour des comptes, 10/2025) ; 20-40 % (NextHop/Markess) | Cour des comptes + NextHop (cout-licences F-006/007) | **L2** |
| F-005 | Le coût des licences Microsoft/Google dans S3NS/Bleu **n'est publié par aucune partie** (Thales, Orange, Capgemini, Microsoft, Google, ANSSI, DINUM) | Constat (cout-licences F-001) | **L2** (enquête blanche) |
| F-006 | La Cour des comptes : « aucun chiffrage d'ensemble des investissements nécessaires n'a été réalisé » ; « absence de stratégie chiffrée de souveraineté numérique » | Cour des comptes, 31/10/2025 (cout-licences F-002) | **L2** |
| F-007 | Audition Capgemini 26/03/2026 : Bleu a « un accord commercial avec Microsoft », termes non divulgués | CIO-online, 30/03/2026 (cout-licences F-003) | L2 (corpus) |

### 3.2 Les estimations bornées (modélisations : INFERENCE)

| ID | Estimation | Hypothèses | Statut |
|---|---|---|---|
| F-010 | **11-25 M€/an de flux public français vers les USA en 2025** (marché interministériel seul) | Part S3NS/Bleu 40-70 % des 59 M€ « européens » ; surcoût 25-40 % ; part licence US 60-75 % du prix | **INFERENCE** (modèle §4.2 cout-licences) |
| F-011 | **24-37 M€/an en 2025** | Part S3NS/Bleu 40-50 % (basse) à 60-70 % (haute) ; flux licence = 60-75 % du prix (F-014 cout-licences) | **INFERENCE** (même dossier, méthode alternative) |
| F-012 | **Estimation élargie (tous marchés publics) : 25-75 M€/an en 2025, 40-120 M€ en 2026** | Multiplicateur 2-3 × marché interministériel | **INFERENCE** (F-014 bis) |
| F-013 | **Projection 2028 (à +62 %/an) : flux > 100 M€/an, dépassant le budget ANSSI (~80 M€)** | Croissance 62 %/an maintenue | **INFERENCE** (scénario, non une prévision) |
| F-014 | Aucun acteur français (S3NS, Bleu, OVHcloud, Scaleway) n'a publié son auto-évaluation SEAL ; Safespring (Suède) seul à publier : 86,25 % | n/a | **L2** (comparaison-cloud F-007) |

### 3.3 Le mécanisme d'assiette (pont avec INV-P0-04)

| ID | Fait | Source | Statut |
|---|---|---|---|
| F-020 | Cotisations sociales : 443 Md€ (2025), assiette 1 078 Md€, élasticité 0,95 (+1 % revenus d'activité ≈ +4,4 Md€) | FIPECO fiche 13 (ancrée INV-P0-04) | **L2** |
| F-021 | Cotisations = 55 % des ressources des administrations de sécurité sociale (2025, vs 98 % en 1980) | FIPECO §B.2 (ancrée) | **L2** |
| F-022 | CSG = impôt sur le revenu, PAS une cotisation (correction terminologique actée) | FIPECO note [1] | **L2** |
| F-023 | Le capital logiciel et les profits immatériels sont plus internationalement mobiles que la masse salariale locale | Propriété structurelle (résolution tour 3, point 5) | L1 (raisonnement) |

## 4. ANALYSE : le mécanisme de la fuite hors assiette

### 4.1 Le schéma conceptuel (pont V3_1 §XI × lignée A)

```text
TEMPS DE TRAVAIL ÉCONOMISÉ PAR L'IA
        │
        ▼
VALEUR PRODUITE (inchangée ou ↑)
        │
        ├──→ SALAIRE (assiette cotisations : élasticité 0,95)
        ├──→ MARGE (assiette IS si profits en France)
        ├──→ CLIENT (baisse de prix / surplus consommateur)
        ├──→ LOGICIEL / LICENCES → SORTIE (Google, Microsoft, OpenAI…)
        └──→ CLOUD / IMPORT DE SERVICES → SORTIE
```

La **fuite hors assiette** = les deux canaux de droite : la valeur qui était taxée (salaire → cotisations ; marge → IS) devient un **paiement à un fournisseur étranger non taxé sur le territoire** (IS Ireland, US). Le mécanisme est identique à celui documenté par la vidéo pour l'asymétrie fiscale : mais la mesure exacte est impossible : le secret des licences (F-005) est le verrou central.

### 4.2 Ce qui est mesuré vs ce qui est estimé

- **Mesuré (L2)** : 84 M€/an de commandes cloud public, +62 %/an ; surcoût 25-40 % ; secret des licences confirmé par l'absence de toute donnée.
- **Estimé (INFERENCE bornée)** : la part de ces 84 M€ qui part effectivement aux USA. **Les deux fourchettes du corpus (11-25 et 24-37 M€) ne sont pas contradictoires : ce sont deux jeux d'hypothèses du même dossier** ; la fourchette publiable consolidée est **11-37 M€/an** avec hypothèses explicites.

### 4.3 La projection 2028 : scénario, pas prévision

À +62 %/an, 11-37 M€ (2025) → ~47-107 M€ (2028), dépassant le budget ANSSI (~80 M€). **C'est un scénario conditionnel** (croissance maintenue, parts de marché inchangées) : la résolution exige de le présenter comme tel, jamais comme une certitude.

### 4.4 Le piège à éviter (décision actée, tour 3)

- ❌ « 51 Md$ d'impôts évités par 4 Big Tech aux USA » → « 51 Md$ de recettes françaises perdues ». **Faux** : la perte est américaine, pas française.
- ✅ « Le capital logiciel et les profits immatériels sont plus internationalement mobiles que la masse salariale locale » : propriété structurelle, publiable.
- ❌ « La fuite hors assiette a causé le déficit » : causalité non démontrée (le déficit précède l'IA : ASSO −6,7 Md€ dès 2025, INV-P0-08).

## 5. CONTRADICTION_LEDGER

| # | Contradiction | Résolution |
|---|---|---|
| 1 | 11-25 M€/an (blueprint §5) vs 24-37 M€/an (F-014 cout-licences) | Deux jeux d'hypothèses du même dossier ; fourchette consolidée publiable : **11-37 M€/an**, avec les hypothèses (part 40-70 %, surcoût 25-40 %, licence 60-75 % du prix) |
| 2 | « enverra plus d'argent à Microsoft et Google que le budget ANSSI » (blueprint, assertion) vs projection 2028 conditionnelle | À reformuler en scénario : « si la croissance de 62 %/an se maintient, le flux pourrait dépasser le budget de l'ANSSI (~80 M€) d'ici 2028 » |
| 3 | 60-75 % du prix = licence US (hypothèse de modélisation) vs aucune ventilation publiée (F-018) | L'hypothèse 60-75 % est elle-même non sourcée (F-014 « estimation de l'auteur ») : à présenter comme borne, avec la clause « la ventilation licence/marge/conformité est le secret commercial central » |
| 4 | « fuite » (cadrage politique) vs « import de services » (cadrage comptable) | Neutre : « une partie de la commande publique cloud rémunère la technologie américaine » : le mot « fuite » réservé à la section d'analyse |

## 6. EDI : ÉLÉMENTS DISCRETS D'INFORMATION

- **Le secret est le verdict** : le fait central n'est pas un montant, c'est que **ni le Parlement ni la Cour des comptes ne connaissent le montant** (F-005/006). Formulation publiable : « le coût des licences est secret ; les bornes publiques vont de 11 à 37 M€/an ».
- Budget ANSSI ~80 M€ : valeur corpus (cout-licences §4.3) : non re-vérifiée en session ; GAP mineur à ancrer avant publication du comparatif.
- Le contrat Mistral pour « L'Assistant » (1 M de fonctionnaires) : 700 000-750 000 € de licences modèle vs 84 M€ de cloud : rapport 1:100 (F-015 cout-licences, Tech Insider 24/07/2026).
- FIPECO : un point de masse salariale = 10,8 Md€ (assiette 1 078 Md€) : l'ordre de grandeur de référence pour le stress-test (INV-P0-04).

## 7. BIAS_TEST

- **Biais de cadrage** : « fuite » préjuge l'illégitimité ; la neutralité exige « destination étrangère du gain » en première mention, puis la discussion.
- **Biais de modélisation** : les fourchettes reposent sur des hypothèses d'auteur (part S3NS/Bleu, ratio licence) : à ne jamais présenter comme des mesures.
- **Contre-lecture testée** : une partie de l'argent « sort » aussi en salaires de développeurs français et en impôts locaux (Thales, Orange, Capgemini créent de l'emploi) ; le bilan net n'est pas calculable : le dire.
- **Erreur de catégorie à éviter** : l'import de services numériques n'est pas de l'évasion fiscale ; c'est un flux commercial licite. Le sujet est l'**assiette**, pas la fraude.

## 8. VERDICT

**Verdict borné :** la fuite hors assiette nationale est un **mécanisme documenté (L2 pour les composantes) et borné (INFERENCE pour le montant)** : 11-37 M€/an pour le seul marché cloud public interministériel, projection 2028 conditionnelle > 100 M€ à +62 %/an, avec le secret des licences comme fait central. **Publiable** dans l'Acte VIII (« Qui capte la transition ? ») avec : (1) les faits mesurés, (2) les bornes explicites avec hypothèses, (3) la clause scénario pour 2028, (4) la non-causalité déficit (le déficit précède). **Jamais** comme pertes françaises dues aux Big Tech, jamais comme cause du déficit.

## SOURCES

| # | Source | URL | Statut |
|---|---|---|---|
| S1 | INV-2026-08-25-0900-COUT-LICENCES-S3NS-BLEU (F-001 à F-018) | investigations/2026-08/.../2026-08-25_09-00_cout-reel-licences-US_INVESTIGATION.md | corpus ancré |
| S2 | DINUM, « L'État accélère sa transition cloud », 26/03/2026 | cité dans S1 (F-010) | L2 (corpus) |
| S3 | Cour des comptes, rapport souveraineté numérique, 31/10/2025 | cité dans S1 (F-002/006) | L2 (corpus) |
| S4 | FIPECO fiche 13 (INV-P0-04, ancrée en session) | https://www.fipeco.fr/fiche/Les-cotisations-sociales | **L2 session** |
| S5 | INV-P0-08 (déficit ASSO −6,7 Md€, contexte) | investigations/2026-08/.../2026-08-26_17-10_terrain-macro-france-europe_INVESTIGATION.md | **L2 session** |

## REQUEST_LOG

| Date | Requête | Résultat |
|---|---|---|
| 2026-08-26 | Relecture dossier cout-licences (flux, fourchettes, ventilation) | Sections 3.3, 3.4, 4.1-4.3 extraites ; deux fourchettes identifiées et réconciliées |
| 2026-08-26 | Vérification budget ANSSI | Valeur corpus ~80 M€ non re-vérifiée (GAP mineur) |
| 2026-08-26 | Contrôle de non-causalité déficit | ASSO −6,7 Md€ (2025) antérieur à l'onde IA : causalité exclue (INV-P0-08) |
