# INVESTIGATION : Wavestone, le cas français intégral (consolidation des 4 références V3_1)

```yaml
RUN_MANIFEST:
  ENGINE_VERSION: 2.9
  STATE: FINAL
  RUN_ID: 20260826-1620-wavestone-cas-francais-integral
  PARENT_RUN_ID: NONE
  AS_OF: 2026-08-26
  INPUT_KIND: TOPIC
  MISSION_MODE: INVESTIGATION
  INPUT_REF: V3_1 refs [^8][^9][^10][^21] ; INV-SERVICEPYR-001 (pyramide-services, 25/08)
  SUBJECT_SLUG: wavestone-cas-francais-integral
  INVESTIGATION_PATH: investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-26_16-20_wavestone-cas-francais-integral_INVESTIGATION.md
  SCOPE: lead_question=Wavestone est-il le meilleur thermomètre français de l'effet IA sur le conseil, et que mesure-t-il exactement ? | object_question=consolider les 4 références Wavestone de V3_1 en un dossier unique : cannibalisation interne (part IA 17 % → 22 % du CA), taux d'activité, TJM, effectifs, recrutements, objectifs ajustés | period=FY2024/25, FY2025/26, T1 FY2026/27 | geo=France (groupe Wavestone coté Euronext Paris) | domains=conseil, temps facturable, IA | actors=Wavestone, Wivoo, AI Builders | exclusions=comparaison sectorielle (INV-SERVICEPYR), fiscalité (INV-P0-04) | limits=données auditées annuelles non inspectées (marge 12,6 % = attendue) ; pas de distribution junior/mid/senior publiée
  COMPLEXITY: $CX_SCORE=5 → $CX=MEDIUM
  CHECKPOINT_SEQ: 1
  LAST_COMPLETED: 18b
  NEXT_ACTION: NONE
  RESUME_COUNT: 0
  ROUTE_OVERRIDES: []
  LOADED_MODULES: [SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, TEMPLATE.md, clusters/ICEBERG.md, clusters/MONEY.md, clusters/FRAMING.md]
  DEGRADED_FLAGS: [MNEMO_UNAVAILABLE_PARAMETRE]
MNEMO_ROW: FAILED_PARAM_TRANSMISSION
SELF_WRITE_ROW: PENDING_AT_SERIALIZATION
WRITEBACK_ROW: 0_WRITTEN
```

## MANIPULATION_REPORT

| Symbole | Score | Observation nommée |
|---|---|---|
| Ξ | 5 | Le T1 26/27 révèle une inflexion nette (organique −2 %) que les agrégats FY25/26 masquaient |
| € | 6 | Cannibalisation : la part IA double (8→17→22 %) sans hausse de TJM ni d'utilisation : le gain de valeur n'est pas capté par le cabinet |
| Λ | 5 | « L'IA cannibalise le conseil » vs « le conseil traverse un marché atone » : les deux lectures coexistent dans le même communiqué |
| ↕ | 3 | France +5 % vs GSA −5 % vs US/UK en net recul : divergence géographique |
| ⫸ | 4 | Deux communiqués primaires (30/04 et 29/07/2026) convergent sur le même récit : réallocation IA au détriment du reste |
| ⏰ | 3 | T1 26/27 (avril-juin 2026) = point d'inflexion : objectifs annuels ajustés à la baisse le 29/07/2026 |

CLUSTERS : MONEY (€=6), FRAMING (Λ=5), ICEBERG (Ξ=5).

## 1. RÉSUMÉ EXÉCUTIF

**RÉPONSE À L'OBJECT_QUESTION.** Les quatre références Wavestone de V3_1 ([^8] résultats FY25/26, [^9] CA FY25/26, [^10] recrutements, [^21] T1 26/27) sont consolidées dans ce dossier et **re-vérifiées sur les deux communiqués primaires inspectés en session (L2)**. Le cas Wavestone documente une **cannibalisation interne sans effondrement** : la part du CA liée à l'IA double en deux ans (8 % → 17 % → 22 %) pendant que le taux d'utilisation recule (73 % → 72 % → 71 %), que le TJM nominal stagne puis baisse (939 € → 938 € → 926 €, soit −1,3 %), et que la croissance organique passe de +1 % (FY25/26) à **−2 % (T1 26/27)**. Wavestone le dit explicitement : « la concentration des nouveaux investissements des clients vers les projets IA s'accélère, au détriment de la plupart des autres domaines » et « la croissance des projets liés à l'IA […] ne permet pas de compenser le recul des autres activités ».

**RÉPONSE À LA LEAD_QUESTION (verdict borné).** Wavestone est le meilleur thermomètre français disponible : coté, trimestriel, chiffres publics. Mais il mesure **la réallocation de la demande, pas la substitution de l'emploi par l'IA** : l'effectif continue d'augmenter (6 076 → 6 111 → 6 122) et ~900 recrutements bruts/an se poursuivent. Ce que le cas démontre : une part IA qui double ne produit pas de gain agrégé visible (utilisation, TJM) : la thèse « plus de business IA = productivité capturée » est réfutée par les agrégats ; ce que le cas ne démontre pas : la destruction de postes.

## 2. CHRONOLOGIE (communiqués Wavestone)

| Date | Publication | Valeur clé |
|---|---|---|
| 30/04/2026 | CA FY2025/26 | 954,3 M€ (+1 % organique), IA = 17 % du CA, marge op attendue 12,6 % |
| 29/07/2026 | T1 FY2026/27 | 227,0 M€ (−2 % organique), IA = 22 % du CA, TJM 926 €, objectifs ajustés, acquisition AI Builders |
| 29/07/2026 | Acquisition | AI Builders finalisée (VE 19,3 M€, ~50 consultants, CA 2026 visé 10,3 M€) |
| 30/07/2026 | AG mixte | n/a |

## 3. FAITS (registre consolidé)

### 3.1 Exercice 2025/26 (CA publié 30/04/2026, page primaire inspectée)

| ID | Fait | Valeur | Statut |
|---|---|---|---|
| W-001 | CA consolidé FY25/26 | 954,3 M€, +1 % (organique +1 %), vs 943,7 M€ FY24/25 | **L2** (page primaire) |
| W-002 | Part IA du CA FY25/26 | **17 %** (vs 8 % un an plus tôt) | **L2** |
| W-003 | Taux d'utilisation FY25/26 | **72 %** (vs 73 % ; 4e trim. attendu 73 %, réalisé 72 %) | **L2** |
| W-004 | TJM FY25/26 | **938 €** (vs 939 €) ; à périmètre/change constants 947 €, +1 % | **L2** |
| W-005 | Effectifs 31/03/2026 | 6 111 (vs 6 076 ; dont 98 issus de Wivoo) | **L2** |
| W-006 | Recrutements bruts FY25/26 | ~900 | **L2** |
| W-007 | Turnover 12 mois glissants | 12 % (stable) | **L2** |
| W-008 | Marge op. récurrente FY25/26 | attendue 12,6 % (objectif ~13 %) | **L2** |
| W-009 | Carnet de commandes 31/03/2026 | 4,4 mois (vs 4,2 mois) | **L2** |

### 3.2 Premier trimestre 2026/27 (publié 29/07/2026, page primaire inspectée)

| ID | Fait | Valeur | Statut |
|---|---|---|---|
| W-010 | CA T1 26/27 | 227,0 M€, **−2 %** organique (vs 231,5 M€ T1 25/26) | **L2** |
| W-011 | Part IA du CA T1 26/27 | **22 %** (vs 17 % FY25/26) | **L2** |
| W-012 | Taux d'activité T1 26/27 | **71 %** (vs 72 % FY25/26) | **L2** |
| W-013 | TJM T1 26/27 | **926 €, −1,3 %** vs 938 € FY25/26 | **L2** |
| W-014 | Effectifs 30/06/2026 | 6 122 ; turnover 12 % | **L2** |
| W-015 | Carnet 30/06/2026 | 4,5 mois (vs 4,4 au 31/03, 4,3 au 30/06/2025) | **L2** |
| W-016 | Objectifs 26/27 ajustés | organique −1 % à « low single-digit » (vs low single-digit) ; marge op 11-13 % (vs ~13 %) | **L2** |
| W-017 | Géographie T1 | France +5 % ; GSA −5 % (baisse sous-traitance) ; US/UK en net recul (trou d'air US) | **L2** |
| W-018 | Acquisition AI Builders (29/07/2026) | ~50 consultants ; CA 2026 visé 10,3 M€ ; EBITDA 15 % ; VE 19,3 M€ ; consolidé au 01/08/2026 | **L2** |

### 3.3 Citations primaires (communiqué T1 26/27, page inspectée)

| ID | Citation | Portée |
|---|---|---|
| W-C01 | « la concentration des nouveaux investissements des clients vers les projets IA s'accélère, au détriment de la plupart des autres domaines » | Cannibalisation |
| W-C02 | « la croissance des projets liés à l'IA, qui représentent 22 % du chiffre d'affaires […] ne permet pas de compenser le recul des autres activités » | Cannibalisation |
| W-C03 | « Wavestone n'a pas été en mesure de tirer pleinement parti de cette réallocation de la demande » | Autoréfutation de la thèse « gain capturé » |
| W-C04 | « le taux d'utilisation a été insuffisant » et « l'efficacité opérationnelle n'a pas été suffisante » | Pression sur le modèle de facturation du temps |

## 4. ANALYSE : ce que le cas Wavestone documente et ce qu'il ne démontre pas

### 4.1 La séquence chiffrée

```text
PART IA DU CA         8 % (FY24/25) → 17 % (FY25/26) → 22 % (T1 26/27)
TAUX D'UTILISATION    73 %           → 72 %            → 71 %
TJM (nominal)         939 €          → 938 €           → 926 € (−1,3 %)
CROISSANCE ORGANIQUE   :             → +1 % (annuel)   → −2 % (T1)
EFFECTIFS             6 076          → 6 111           → 6 122
```

### 4.2 Lecture : la part IA double sans gain agrégé

Le DELTA central (déjà posé par INV-SERVICEPYR-001) est **renforcé par les primaires** : la part IA double en deux ans sans hausse visible ni de l'utilisation ni du TJM nominal. Deux précisions nouvelles, non présentes dans V3_1 :

1. **Le TJM à périmètre constant progresse (+1 %, 947 €) en FY25/26** : la baisse nominale 939→938 s'explique par un effet change/périmètre. La vraie inflexion est au T1 26/27 : −1,3 % en nominal, et Wavestone lui-même lie cette dégradation à la réallocation IA et à un « taux d'utilisation insuffisant ».
2. **Wavestone assume la cannibalisation** : le communiqué du 29/07/2026 utilise le mot exact (« au détriment de la plupart des autres domaines »). Ce n'est plus une lecture externe : c'est l'analyse de l'entreprise elle-même.

### 4.3 Ce que le cas ne démontre pas

- **Pas de destruction d'emplois** : effectifs en hausse continue, ~900 recrutements bruts/an, turnover stable à 12 %.
- **Pas d'effondrement des prix** : le TJM est stable sur un an puis −1,3 % : une érosion, pas un effondrement.
- **Pas de preuve que l'IA dégrade la productivité** : l'interprétation la plus parcimonieuse est un marché atone + une réallocation de la demande vers l'IA que le cabinet n'a pas su facturer.

### 4.4 La réaction du cabinet (matériau pour l'Acte II/IV)

La réponse de Wavestone à la cannibalisation est **l'achat d'AI Builders** (cabinet IA & data, 10,3 M€ de CA visé) et l'ajustement à la baisse de ses objectifs : pas la réduction d'effectifs. C'est un contrepoint utile au récit « l'IA supprime le conseil » : le marché se réalloue, et les acteurs achètent la compétence plutôt que de la licencier. Mais la marge opé. cible passe de ~13 % à 11-13 % : la réallocation a un coût immédiat.

## 5. CONTRADICTION_LEDGER

| # | Contradiction | Résolution |
|---|---|---|
| 1 | TJM « stable » (V3_1, FY25/26) vs « −1,3 % » (T1 26/27) | Pas une contradiction : deux périodes. V3_1 dit « pratiquement stable » pour FY25/26 (vrai, 938 vs 939) ; la baisse de −1,3 % est au T1 26/27 (926 €) |
| 2 | « Croissance +1 % » (titre CA FY25/26) vs « repli de −2 % » (titre T1 26/27) | Deux périodes distinctes ; le repli T1 est l'inflexion que les agrégats annuels lissaient |
| 3 | IA = 17 % (FY25/26, communiqué CA 30/04) vs 22 % (T1 26/27) | Progression trimestrielle documentée ; les deux chiffres sont primaires |
| 4 | TJM nominal 938 € vs TJM périmètre constant 947 € (même communiqué) | L'écart = effets change/périmètre, explicitement signalé par Wavestone ; à ne jamais mélanger |

## 6. EDI : ÉLÉMENTS DISCRETS D'INFORMATION

- **Familles manquantes (V3_1 ne le dit pas)** : la distribution junior/mid/senior des effectifs n'est pas publiée ; le « ~900 recrutements bruts » ne distingue pas les postes créés des remplacements → le non-remplacement n'est pas mesurable dans les données Wavestone.
- Wivoo est consolidé depuis le 01/06/2025 : les comparaisons T1 vs T1 intègrent un effet périmètre explicite.
- AI Builders : acquisition intégralement financée en numéraire (fonds propres) : signal de trésorerie disponible, pas de dilution.

## 7. BIAS_TEST

- **Biais de l'énoncé** : présenter Wavestone comme « preuve que l'IA cannibalise le conseil » surinterprète : les données sont cohérentes avec un marché atone ; la causalité IA est l'analyse de Wavestone lui-même (source primaire), pas une mesure.
- **Biais de sélection** : Wavestone est un cabinet de conseil technologique « early adopter » : non représentatif du conseil stratégique pur (McKinsey/BCG) ni des ESN.
- **Contre-lecture testée** : l'hypothèse « marché atone » (macro P0-08 : climat des affaires 98, défaillances en hausse) est compatible avec les données : à mentionner en Acte VII pour ne pas attribuer à l'IA ce qui revient à la conjoncture.

## 8. VERDICT

**Verdict borné :** la cannibalisation interne du conseil par l'IA est **documentée (L2, primaires Wavestone)**, dans sa limite exacte : une réallocation de la demande vers les projets IA qui pèse sur le reste de l'activité, sans destruction d'emplois démontrée. Le cas est **publiable en Acte II (révélateur) et Acte IV (où part la valeur)**, avec la clause : la part IA double, le TJM et l'utilisation ne suivent pas, l'entreprise ajuste ses objectifs et achète la compétence.

**Formulations réservées pour l'article :**
- ✅ « la part du CA liée à l'IA a plus que doublé (8 % → 17 % → 22 %) sans hausse visible du taux d'utilisation ni du TJM » : sourcé W-002/003/004/011/012/013.
- ✅ « Wavestone décrit lui-même une concentration des investissements clients vers l'IA au détriment des autres domaines » : W-C01.
- ⚠️ « l'IA cannibalise le conseil » : acceptable uniquement avec la citation W-C01/C02 en support, et la clause conjoncture.
- ❌ « Wavestone supprime des postes à cause de l'IA » : non démontré (effectifs en hausse).

## SOURCES

| # | Source | URL | Statut |
|---|---|---|---|
| S1 | Wavestone, CA FY2025/26 (30/04/2026) | https://www.wavestone.com/fr/regul-information/chiffre-daffaires-2025-26-en-croissance-organique-de-1-marge-operationnelle-recurrente-2025-26-attendue-a-126/ | ◈ inspectée |
| S2 | Wavestone, résultats FY2025/26 : plan Lead the shift (communiqué référencé [^8]) | https://www.wavestone.com/fr/regul-information/resultats-2025-26-resultat-net-en-progression-de-8-lead-the-shift-le-plan-strategique-de-wavestone-a-lhorizon-2030/ | non re-inspectée (couvert par S1 pour les grandeurs) |
| S3 | Wavestone, T1 FY2026/27 (29/07/2026) | https://www.wavestone.com/fr/regul-information/2026-27-1er-trimestre-en-repli-de-2-objectifs-annuels-ajustes-ai-builders-acquisition-ciblee-dun-cabinet-francais-ia-et-data/ | ◈ inspectée |
| S4 | Wavestone EN, même publication CA FY25/26 (référence [^10]) | https://www.wavestone.com/en/regul-information/2025-26-revenue-up-1-on-an-organic-basis-recurring-operating-margin-expected-at-12-6/ | doublon S1 |
| S5 | INV-SERVICEPYR-001 (pyramide-services, 25/08) | articles/2026-08-26/IA_TRAVAIL_ARTICLE_ARCHIVE_2026-08-26/02_INVESTIGATIONS/2026-08-25_18-36_pyramide-services_INVESTIGATION.md | corpus |

## REQUEST_LOG

| Date | Requête | Résultat |
|---|---|---|
| 2026-08-26 | Lecture primaire communiqué CA FY25/26 | 200 OK, texte intégral extrait (W-001 à W-009) |
| 2026-08-26 | Lecture primaire communiqué T1 26/27 | 200 OK, texte intégral extrait (W-010 à W-018, W-C01 à C04) |
| 2026-08-26 | Page « résultats annuels + feuille de route » (S2) | non re-inspectée : S1 couvre les grandeurs citées ; GAP mineur (détail marge audité 12,6 % définitif non relu) |
