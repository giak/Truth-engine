# INVESTIGATION : « Alcatel-Lucent à Nokia, puis ASN à l'État » — l'arc complet : un champion des télécoms autorisé à partir 15,6 Md€ (2015), son joyau stratégique racheté à perte (2024-2025)

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260814-1200-alcatel-nokia-asn
PARENT_RUN_ID  : NONE (INPUT_KIND=TOPIC) ; corpus frère : 20260814-0900-opella-sanofi-cdr, 20260814-1000-atos-demantelement, 20260814-1100-carrefour-couche-tard, 20260812-1800-iceberg-max-alstom-areva
AS_OF          : 2026-08-13
INPUT_KIND     : TOPIC (thème : rachat d'Alcatel-Lucent par Nokia en 2015-2016 autorisé par l'État avec engagements non chiffrés, puis reprise d'ASN (câbles sous-marins) par l'État en 2024-2025 — pattern « vendre bas, racheter à perte » et sélectivité du bouclier IEF)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique utilisateur, re-pipeline T5 cessions, vague 3)
SUBJECT_SLUG   : alcatel-nokia-asn
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-14_alcatel-nokia-asn/2026-08-14_12-00_alcatel-nokia-asn_INVESTIGATION.md
SCOPE          : opération Nokia/Alcatel-Lucent (annonce, valorisation, structure OPE, autorisation de l'État, engagements, clôture, conséquences emploi/R&D, sort d'ASN/CFIUS, cadre IEF décret 2014-479) ; reprise d'ASN par l'État via l'APE (annonce 2024, montants, conditions, clôture, contexte souveraineté des câbles sous-marins) ; période 2015-2026 ; géographie : France, Finlande, États-Unis
COMPLEXITY     : CX_SCORE=13 → $CX=STANDARD (political 4, technical 2, temporal 4, geo 2, narratives 2, data 2)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 12
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE | INVESTIGATION (tous chargés)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« l'État a-t-il laissé partir Alcatel-Lucent en 2015 sans protection réelle, puis racheté à perte en 2024 l'actif stratégique qu'il avait laissé partir ? ») :

L'opération Nokia/Alcatel-Lucent a été annoncée les **14-15/04/2015** sous forme d'OPE en actions (0,55 action Nokia pour 1 action Alcatel-Lucent), valorisant Alcatel-Lucent **~15,6 Md€** (4,48 €/action, prime ~28 %). L'État français, informé et consulté, a **autorisé** l'opération en **octobre 2015** dans le cadre du décret n° 2014-479 du 14/05/2014 (décret Montebourg), sans refuser : les engagements obtenus de Nokia étaient **généraux et non chiffrés** (maintien « Shift Plan », sans obligation quantitative sur l'emploi ni la R&D, documenté par Marianne 14/10/2022). L'AMF a constaté le succès de l'OPE le **04/01/2016** (Nokia ~70,5 % du capital). Les conséquences documentées ensuite : plans de suppressions de postes en France (fonctions support, commerciales, équipes de recherche), réduction de la R&D (sites historiques Villarceaux, Lannion) — rapport de la commission d'enquête de l'Assemblée nationale sur la souveraineté industrielle (n° 897). Alcatel Submarine Networks (ASN), joyau des câbles sous-marins, a été **conservée** par Nokia (feu vert CFIUS 16/09/2015). Près d'une décennie plus tard, le **27/06/2024**, Nokia et l'État français annoncent la cession d'ASN : valeur d'entreprise **350 M€**, l'État (via l'APE) acquiert **80 % pour ~100 M€** (Nokia conserve 20 % avec option de rachat à terme vers 100 %). Signature à Calais le **05/11/2024**, opération finalisée le **31/12/2024**. ASN est l'un des 3-4 fabricants mondiaux de câbles sous-marins (SubCom, NEC, HMN Tech), qui portent ~99 % du trafic transcontinental de données.

**Verdict sur le LEAD_QUESTION** : **CONTEXTE DOCUMENTÉ, LECTURE DE SÉLECTIVITÉ SOUTENUE**. Le fait est documenté : l'État a autorisé en 2015 la sortie du champion français des télécoms contre des engagements non chiffrés, puis a racheté en 2024-2025 à la décote (80 % pour ~100 M€, EV 350 M€) la filiale la plus stratégique du même groupe — l'arc « vendre bas, racheter à perte » est chiffré (15,6 Md€ vs 350 M€), la sélectivité (Nokia autorisé en 2015, Photonis/Carrefour bloqués ailleurs, L'Express parle de « revirement » de Macron le 05/11/2024) est documentée. Aucun fait pénal n'est documenté.

**Acteurs** : Nokia (Rajeev Suri), Alcatel-Lucent, Emmanuel Macron (ministre de l'Économie 2015), Manuel Valls (Premier ministre), APE (Agence des participations de l'État), Antoine Armand (ministre de l'Économie 2024), Bercy/DG Trésor (IEF), CFIUS, AMF, salariés/syndicats, commission d'enquête de l'Assemblée nationale.

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **8/10** | Engagements Nokia de 2015 non publics dans le détail et non chiffrés ; montant exact payé par l'État pour les 80 % (≈100 M€ rapporté) ; option de rachat des 20 % non valorisée publiquement ; texte de l'accord 2024 non public. |
| 2 | **€** money | **8/10** | 15,6 Md€ (2015) ; 4,48 €/action ; prime ~28 % ; EV ASN 350 M€ ; 80 % ≈ 100 M€ (2024) ; CA ASN > 1 Md€. |
| 3 | **Λ** framing | **8/10** | « Airbus des télécoms » (Macron, 2015) vs « nationalisation » / « revirement » (presse, 2024) vs « recentrage de Nokia » (version Nokia). |
| 4 | **Ω** inversion | **7/10** | L'État qui « protège la souveraineté » en 2024 est le même qui a autorisé la sortie en 2015 sans contreparties chiffrées ; le rachat de rattrapage est présenté comme une victoire. |
| 5 | **Ψ** sidération | **5/10** | Champ technique (OPE, CFIUS, câbles sous-marins), pic émotionnel modéré (emplois perdus, souveraineté numérique). |
| 6 | **↕** verticalité | **8/10** | Décisions au sommet (gouvernement Valls/Macron 2015, gouvernement 2024) ; salariés et sites (Villarceaux, Lannion, Calais, Les Ulis) subissent ; pas de débat public préalable documenté en 2015. |
| 7 | **Φ** spectacle | **5/10** | Annonce 2015 fortement médiatisée (« Airbus des télécoms ») ; reprise ASN médiatisée comme acte de souveraineté (05/11/2024, déplacement à Calais). |
| 8 | **Σ** sémiotique | **7/10** | « Champion européen » (2015) ; « câbles sous-marins = 99 % du trafic » (2024) ; « nationalisation » vs « retour sous pavillon public » ; le lexique de la souveraineté réinvesti. |
| 9 | **Κ** cynisme | **7/10** | L'État encaisse la communication « souveraineté » sur le rachat 2024 d'un actif qu'il a laissé partir en 2015 sans condition chiffrée ; le contraste est documenté (L'Express 05/11/2024). |
| 10 | **ρ** résistance | **6/10** | Commission d'enquête de l'Assemblée nationale sur la souveraineté industrielle (rapport n° 897) ; presse d'investigation (Marianne, L'Express) ; syndicats (plans sociaux). |
| 11 | **κ** influence subtile | **6/10** | Rôle des conseils et de la diplomatie économique ; discussion interne d'une participation publique (2015) évoquée par la presse puis abandonnée ; lobbying Nokia. |
| 12 | **⫸** convergence | **7/10** | Convergence sans contamination : communiqués officiels (Nokia 2015/2024, Bercy 2024), presse d'investigation (Marianne 2022, L'Express 2024), rapport parlementaire (n° 897), presse économique (Les Échos, La Tribune) documentent le même arc. |
| 13 | **⚔** guerre cognitive | 3/10 | Pas d'opération coordonnée documentée ; en revanche le récit « champion européen » (2015) puis « souveraineté retrouvée » (2024) est construit par l'exécutif à chaque étape. |
| 14 | **🌐** réseau | **6/10** | Nœuds : Nokia, Alcatel-Lucent, État français (Macron, Valls, Armand, APE, Bercy/IEF), CFIUS, AMF, ASN, syndicats, commission d'enquête. |
| 15 | **⏰** temporalité | **7/10** | 14-15/04/2015 (annonce) → 10/2015 (autorisation) → 04/01/2016 (clôture OPE) → 2016-2024 (destruction de valeur documentée) → 27/06/2024 (accord ASN) → 31/12/2024 (finalisation) : boucle longue de 9 ans, arc complet vérifiable. |

## 3. CHRONOLOGIE

- **14-15/04/2015** : annonce de l'opération Nokia/Alcatel-Lucent (fuites puis communiqués conjoints) ; Macron assure « pas de suppression d'emplois en France » (Les Échos 14/04/2015).
- **04/2015** : débat public ; une prise de participation publique évoquée par la presse puis abandonnée ; Macron parle d'un « Airbus des télécoms ».
- **10/2015** : autorisation préalable du ministre de l'Économie (Le Monde 21/10/2015) dans le cadre du décret n° 2014-479 (14/05/2014).
- **04/01/2016** : AMF constate le succès de l'OPE ; Nokia contrôle ~70,5 % du capital d'Alcatel-Lucent avant retrait obligatoire.
- **2016-2024** : suppressions de postes en France, réduction de la R&D (Villarceaux, Lannion) ; ASN conservée par Nokia (feu vert CFIUS 16/09/2015).
- **27/06/2024** : annonce de l'accord Nokia/État français sur la cession d'ASN (put option agreement ; EV 350 M€).
- **05/11/2024** : signature de l'acquisition de 80 % par l'État (APE) à Calais, en présence du ministre Antoine Armand.
- **31/12/2024** : finalisation de l'opération ; Nokia conserve 20 % avec option de rachat à terme (vers 100 %).
- **2025-2026** : mise en œuvre des conditions (consultation IRP, maintien des sites, sanctuarisation du savoir-faire) ; suivi non documenté publiquement à la date.

## 4. FACT_REGISTRY (faits sourcés)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | Annonce de l'opération Nokia/Alcatel-Lucent les 14-15/04/2015 (fuites puis communiqués conjoints) | 14-15/04/2015 | SRC-01 communiqué Nokia 15/04/2015 ; Les Échos 14/04/2015 | ✦ |
| FCT-002 | Valorisation d'Alcatel-Lucent : ~15,6 Md€ (≈16,6 Md$), prix implicite 4,48 €/action | 15,6 Md€ | SRC-02 Les Échos 15/04/2015 ; La Tribune 04/2015 | ✦ |
| FCT-003 | Structure : OPE 100 % en actions, 0,55 action Nokia pour 1 action Alcatel-Lucent, prime ~28 %, sans versement en numéraire | 0,55/1 ; +28 % | SRC-03 CNBC 15/04/2015 ; Les Échos | ✦ |
| FCT-004 | Autorisation préalable du ministre de l'Économie accordée en octobre 2015 | 10/2015 | SRC-04 Le Monde 21/10/2015 | ✦ |
| FCT-005 | Cadre applicable : décret n° 2014-479 du 14/05/2014 (décret Montebourg) élargissant le contrôle des investissements étrangers aux réseaux de communications électroniques ; autorisation accordée, pas de refus | 14/05/2014 | SRC-05 Légifrance ; Le Monde 21/10/2015 | ✦ |
| FCT-006 | Une prise de participation publique pour contrer Nokia (protéger les actifs stratégiques, dont ASN) a été évoquée en interne/dans la presse, puis abandonnée | — | SRC-06 L'Opinion 15/04/2015 ; L'Express 05/11/2024 | ⚠ (rapporté, aucune décision documentée) |
| FCT-007 | Emmanuel Macron qualifie l'opération d'« Airbus des télécoms » ; les engagements de Nokia sur l'emploi et la R&D en France sont généraux et non chiffrés (maintien basé sur le « Shift Plan » d'Alcatel-Lucent, sans obligation quantitative) | — | SRC-07 L'Opinion 15/04/2015 ; Marianne 14/10/2022 | ⚠ (propos rapporté + constat d'absence d'engagement chiffré) |
| FCT-008 | Clôture : AMF constate le succès de l'OPE le 04/01/2016 ; Nokia contrôle ~70,5 % du capital d'Alcatel-Lucent avant retrait obligatoire | 04/01/2016 ; 70,5 % | SRC-08 Le MagIT 04/01/2016 | ✦ |
| FCT-009 | Répartition prévue du groupe fusionné : ~66,5 % pour les actionnaires Nokia / ~33,5 % pour les anciens actionnaires Alcatel-Lucent | 66,5/33,5 % | SRC-09 Le Monde ; Agefi 04/2015 | ✦ |
| FCT-010 | Conséquences documentées en France : plans de suppressions de postes (fonctions support, commerciales, équipes de recherche), réduction de la R&D (sites historiques Villarceaux, Lannion), restructurations et cessions | — | SRC-10 Rapport Assemblée nationale n° 897 (commission d'enquête souveraineté industrielle) | ✦ |
| FCT-011 | ASN (Alcatel Submarine Networks) conservée par Nokia lors de la fusion, après feu vert du régulateur américain CFIUS (16/09/2015) | 16/09/2015 | SRC-11 Communications Daily 16/09/2015 | ✦ |
| FCT-012 | Annonce de l'accord Nokia/État français sur la cession d'ASN le 27/06/2024 (put option agreement) | 27/06/2024 | SRC-12 communiqué Nokia 27/06/2024 ; Reuters 27/06/2024 | ✦ |
| FCT-013 | Valeur d'entreprise d'ASN : 350 M€ ; l'État acquiert 80 % du capital pour ~100 M€ ; Nokia conserve 20 % avec option de rachat à terme (vers 100 %) | 350 M€ ; 80 % ≈ 100 M€ | SRC-13 communiqué Bercy 05/11/2024 ; Décideurs 06/11/2024 | ✦ |
| FCT-014 | Acheteur : l'État français via l'APE (Agence des participations de l'État), sous l'impulsion du ministre Antoine Armand ; signature à Calais le 05/11/2024 ; opération finalisée le 31/12/2024 | 05/11/2024 ; 31/12/2024 | SRC-14 communiqué Bercy 05/11/2024 ; communiqué Nokia 03/01/2025 | ✦ |
| FCT-015 | ASN est l'un des 3-4 fabricants mondiaux de câbles sous-marins (SubCom, NEC, HMN Tech) ; les câbles sous-marins portent ~99 % du trafic transcontinental de données ; enjeu de souveraineté numérique | ~99 % | SRC-15 Bercy 05/11/2024 ; La Tribune 27/06/2024 | ✦ |
| FCT-016 | ASN : ~2 000-2 400 employés (dont 1 300+ en France : site historique de Calais, R&D des Ulis, sites UK/Norvège), flotte de 7 navires, chiffre d'affaires > 1 Md€ | 2 000-2 400 ; 1 300+ ; 7 ; > 1 Md€ | SRC-16 Bercy 05/11/2024 ; VIPress 07/01/2025 | ✦ |
| FCT-017 | Conditions de la cession 2024 : consultation des instances représentatives du personnel, maintien du siège et des sites en France/Europe, sanctuarisation du savoir-faire souverain | — | SRC-17 communiqué Bercy 05/11/2024 | ✦ |
| FCT-018 | Arc documenté : Alcatel-Lucent cédée ~15,6 Md€ en 2015 (État autorisateur) ; son actif le plus stratégique (ASN) revendu à l'État 80 % pour ~100 M€ (EV 350 M€) en 2024-2025 — décote composée (≈1/150e du prix de 2015, pour 80 % d'une filiale) | 15,6 Md€ vs 350 M€ | SRC-18 synthèse FCT-002/FCT-013 (constat composé) | ⚠ (calcul composé, inférence étiquetée) |

## 5. CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « La France a laissé partir son champion des télécoms en 2015 sans protection réelle » | Autorisation 10/2015 (FCT-004) ; engagements non chiffrés (FCT-007) ; suppression de postes et réduction R&D documentées ensuite (FCT-010) | L'État a appliqué la procédure d'autorisation préalable du décret 2014-479 (FCT-005) ; l'opération créait un « champion européen » (FCT-007) | PARTIELLEMENT SOUTENU (la procédure a été appliquée, mais sans contreparties quantifiées) |
| CLM-002 | « L'État a racheté à perte en 2024 le joyau qu'il avait laissé partir en 2015 » | ASN : EV 350 M€, 80 % pour ~100 M€ (FCT-013) vs 15,6 Md€ pour Alcatel-Lucent (FCT-002) | ASN n'est qu'une filiale, pas tout Alcatel-Lucent ; la décote reflète le recentrage stratégique de Nokia et l'état du marché ; l'État n'a pas « perdu » l'argent : il rachète un actif public | PARTIELLEMENT SOUTENU (l'arc est chiffré ; la causalité reste une lecture) |
| CLM-003 | « Le décret Montebourg n'a pas protégé Alcatel-Lucent » | Autorisation accordée 10/2015 malgré la sensibilité (réseaux de communications électroniques) (FCT-005) | Le décret soumet à autorisation préalable, il ne bloque pas par défaut ; l'État a choisi d'autoriser | SOUTENU (fait : l'autorisation a été accordée — sélectivité documentée) |
| CLM-004 | « La reprise d'ASN est une nationalisation de rattrapage » | État 80 % via l'APE (FCT-014) ; « revirement » documenté (L'Express 05/11/2024) | Vente volontaire de Nokia (recentrage), pas d'expropriation ; prix négocié (EV 350 M€) ; l'État reprend un actif stratégique | PARTIELLEMENT SOUTENU (rachat public à la décote documenté ; « nationalisation » discutable) |

## 6. CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | « Pas de suppression d'emplois en France, assure Macron » (14/04/2015) vs plans de suppressions de postes documentés ensuite (fonctions support, commerciales, R&D) | Les faits ultérieurs contredisent l'assurance initiale ; la commission d'enquête (n° 897) documente la destruction d'emplois | DOCUMENTÉE (tranchée par les faits ultérieurs) |
| CONTR-002 | « Airbus des télécoms » (2015) vs rachat public de rattrapage d'ASN (2024) | Le champion européen s'est transformé en cession d'une filiale stratégique à l'État une décennie plus tard ; L'Express documente le « revirement » | DOCUMENTÉE (non tranchée) |
| CONTR-003 | « Nokia devait céder ASN » (rumeurs 2015, pressions de sécurité américaines) vs ASN conservée par Nokia jusqu'en 2024 | ASN a été conservée après le feu vert CFIUS (16/09/2015) puis cédée à l'État en 2024-2025 ; la cession a eu lieu 9 ans plus tard et au bénéfice de l'État | DOCUMENTÉE (tranchée : conservation jusqu'en 2024) |

## 7. RÉSEAU D'ACTEURS

**Entreprises** : Nokia (acquéreur 2015, cédant 2024), Alcatel-Lucent (cible 2015), ASN (cible 2024), SubCom/NEC/HMN Tech (concurrents câbles sous-marins).
**Institutions** : Bercy / ministère de l'Économie, APE (Agence des participations de l'État), DG Trésor (IEF), CFIUS (États-Unis), AMF, Assemblée nationale (commission d'enquête souveraineté industrielle, rapport n° 897).
**Personnes** : Emmanuel Macron (ministre de l'Économie 2015, qualifie l'opération d'« Airbus des télécoms »), Manuel Valls (Premier ministre 2015), Antoine Armand (ministre de l'Économie 2024, signature ASN à Calais), Rajeev Suri (direction Nokia 2015).

## 8. MÉCANISMES / CHAÎNES CAUSALES

**M1 — L'autorisation comme acte de sélectivité** : le même outil (autorisation préalable du ministre, décret 2014-479) produit des issues opposées selon la volonté politique : Nokia autorisé en 10/2015 avec contreparties non chiffrées, Photonis bloqué (2020), Carrefour bloqué (2021), Opella encadrée par contrat (2024). Type : STRUCTUREL. Niveau : L2.
**M2 — Le cycle « vendre, perdre, racheter à perte »** : cession ~15,6 Md€ (2015) → destruction de valeur documentée (emplois, R&D, FCT-010) → rachat public de l'actif stratégique (ASN, 80 % ≈ 100 M€, EV 350 M€) en 2024-2025. L'arc est le même que Toulouse (+199 M€), les autoroutes (14,8 vs 45-50 Md€) et EDF (9,7 Md€) : le rachat de rattrapage est plus cher humainement et industriellement que la rétention initiale. Type : STRUCTUREL/CONJONCTUREL. Niveau : L2.
**M3 — Le contrôle étranger d'abord, le rattrapage français ensuite** : en 2015, c'est le régulateur américain (CFIUS) qui a conditionné l'opération (ASN conservée, 16/09/2015), pas l'État français ; en 2024, l'État français rachète ce que la contrainte américaine avait contribué à sanctuariser. Type : STRUCTUREL. Niveau : L2.

## 9. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Champion européen » | L'OPE Nokia était une consolidation industrielle bénéfique | Valorisation 15,6 Md€, prime 28 % ; autorisation de l'État ; logique 5G | Suppressions de postes et réduction R&D documentées (FCT-010) ; engagements non chiffrés (FCT-007) | PARTIELLEMENT SOUTENU (logique industrielle réelle, contreparties faibles) |
| S2 « Abandon de souveraineté » | L'État a laissé partir sans condition un champion stratégique | Engagements non chiffrés (FCT-007) ; autorisation sans refus (FCT-005) ; rachat de rattrapage 9 ans après (FCT-013) | Le décret 2014-479 a été appliqué (procédure) ; la souveraineté d'ASN a été préservée par CFIUS (FCT-011) | RETENU (scénario principal, documenté) |
| S3 « Réparation tardive » | Le rachat d'ASN en 2024 corrige la sortie de 2015 | État 80 % (FCT-014) ; ASN stratégique (FCT-015) | Rachat à la décote d'une filiale seulement ; les emplois/R&D perdus ne sont pas restaurés | PARTIELLEMENT SOUTENU (réparation partielle, documentée) |

**RESPONSIBILITY_MAP** : la décision de 2015 relève du gouvernement (autorisation, engagements non chiffrés) et de Nokia/Alcatel-Lucent (accord) ; la décision de 2024 relève de l'État (rachat via APE) et de Nokia (cession volontaire). Aucune personne physique n'est mise en cause pénalement. (BENEFIT != INTENT).

## 10. VERDICT 3 AXES

- **PÉNAL** : 0 fait pénal documenté (aucune infraction, aucune mise en examen).
- **INTÉGRITÉ** : GRAVEMENT CONTESTÉ (non) — l'autorisation de 2015 sans contreparties chiffrées, suivie du rachat public de rattrapage en 2024, documente une sélectivité du bouclier IEF (Nokia autorisé, Photonis/Carrefour bloqués) et une asymétrie de traitement entre opérations ; la question est documentée par la commission d'enquête (n° 897) et la presse d'investigation (Marianne, L'Express).
- **LÉGITIMITÉ** : CONTESTÉ — le « revirement » documenté (L'Express 05/11/2024) et l'absence de débat public préalable en 2015 attestent d'un déficit de légitimité perçu ; le récit « souveraineté retrouvée » (2024) contraste avec la sortie non conditionnée (2015).

## 11. PÉRIMÈTRE & LIMITES

**Inclusions** : opération Nokia/Alcatel-Lucent (annonce, valorisation, structure, autorisation, engagements, clôture, conséquences, sort d'ASN, cadre IEF) ; reprise d'ASN par l'État (annonce, montants, conditions, clôture, contexte). Période 2015-2026.

**Exclusions** : la stratégie industrielle globale de Nokia ; la gouvernance interne d'Alcatel-Lucent avant 2015 ; la technologie des câbles sous-marins ; les autres opérations de Nokia (Infineon, etc.).

**GAP déclarés** :
- GAP-001 (ACCESS) : montant exact payé par l'État pour les 80 % d'ASN (~100 M€ rapporté) ; valorisation de l'option de rachat des 20 % ; texte de l'accord 2024 non public.
- GAP-002 (ACCESS) : contenu exact des engagements Nokia de 2015 (non chiffrés, non publiés) ; procès-verbaux des discussions sur la participation publique.
- GAP-003 (CAUSALITY) : le lien entre l'autorisation 2015 et la destruction d'emplois ultérieure est chronologique et documenté par la commission d'enquête, mais la causalité juridique n'est pas tranchée.

## 12. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : annonce 14-15/04/2015 ; valorisation 15,6 Md€ (4,48 €/action) ; structure OPE 0,55/1 ; autorisation 10/2015 ; décret 2014-479 appliqué ; clôture OPE 04/01/2016 (Nokia 70,5 %) ; suppressions de postes et réduction R&D (rapport n° 897) ; ASN conservée (CFIUS 16/09/2015) ; accord ASN 27/06/2024 ; EV 350 M€, 80 % ≈ 100 M€ ; signature 05/11/2024 à Calais ; finalisation 31/12/2024 ; ASN 3-4 fabricants mondiaux, ~99 % du trafic ; effectifs 2 000-2 400 (1 300+ en France), 7 navires, CA > 1 Md€ ; conditions (IRP, sites, savoir-faire).
- **PROBABLE (✧)** : montant exact des 80 % (~100 M€, deux sources convergentes, communiqué officiel non chiffré) ; discussion interne d'une participation publique en 2015 (presse, non documentée officiellement).
- **HYPOTHÈSE (⁂)** : l'effectivité future des conditions 2024 ; l'impact du rachat sur la stratégie industrielle.
- **CONTESTÉ (⊗)** : le qualificatif « Airbus des télécoms » (2015) vs « revirement » (2024) ; la nature « nationale » de la reprise.
- **INCONNU (⁅)** : montants exacts de conseil ; texte des accords ; suivi des engagements 2015 et 2024.

## 13. SUSPICION / VÉRIFICATION

- Les chiffres structurants (15,6 Md€, 0,55/1, 350 M€, 80 %/100 M€, dates) sont confirmés par les communiqués officiels (Nokia 2015/2024, Bercy 2024) et la presse économique : fiables.
- L'absence d'engagements chiffrés en 2015 est documentée par Marianne (14/10/2022, enquête) et le rapport parlementaire n° 897 : constat d'absence robuste.
- Les éléments « participation publique évoquée » (FCT-006) et « Airbus des télécoms » (FCT-007) sont des propos rapportés par la presse : statut ⚠, pas de document officiel.
- Aucune source ne documente un refus IEF en 2015 : l'autorisation accordée est un fait (FCT-004/FCT-005), le non-blocage est le corollaire documenté.
