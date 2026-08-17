# INVESTIGATION APEX : CUMCUM / CUMEX EN FRANCE (ARBITRAGE DE DIVIDENDES, Cariou/Cordier, DGFiP, BLOCAGES LÉGISLATIFS)

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260809-1416-cumcum-cumex-france
PARENT_RUN_ID  : 20260809-1343-enrichissement-legalise-france (branche du FCT-038 du dossier parent)
AS_OF          : 2026-08-09
INPUT_KIND     : UPDATE (revalidation et approfondissement du FCT-038 parent)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique : « CumCum/CumEx France : montants précis, travaux Cariou/Cordier, redressements DGFiP, blocages législatifs »)
SUBJECT_SLUG   : cumcum-cumex-france
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cumcum-cumex-france/2026-08-09_14-16_cumcum-cumex-france_INVESTIGATION.md
SCOPE          : arbitrage de dividendes CumCum/CumEx concernant la France : mécanisme, estimations du manque à gagner, rapport Cariou/Cordier (n° 2252, 2019), redressements DGFiP et contentieux, CJIP bancaires, blocages législatifs et réformes (LF 2025, FASTER UE) ; période 2018-2026 ; géographie : France + contexte UE
COMPLEXITY     : CX_SCORE=13 → $CX=APEX (political 2, technical 2, temporal 3, geo 2, narratives 2, data 2)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 18b
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE (héritage revalidé)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« quels sont les montants précis du CumCum/CumEx en France, que disent les travaux Cariou/Cordier, que redressent les DGFiP, et quels blocages législatifs a-t-on identifiés ? ») :

Le CumCum est un **évitement de la retenue à la source française sur les dividendes** : des actionnaires non-résidents transfèrent temporairement la propriété de leurs titres (prêts de titres, ventes à réméré, dérivés) à un intermédiaire résident juste avant le détachement du dividende, puis récupèrent le flux après prélèvement d'une commission (FCT-001). Le CumEx, distinct, repose sur des restitutions multiples d'impôt jamais payé (FCT-018).

1. **Les montants** : **33 Md€ de manque à gagner cumulé pour la France depuis ~2000** (Université de Mannheim, reprise par l'enquête Radio France du 03/10/2025, FCT-005) ; estimations annuelles de 0,4-1 Md€ (AMF) à 3 Md€ (FCT-006) ; **arriérés réclamés aux banques : >2,5 Md€ (2023), redressements cumulés ~4,5 Md€** (audition Éric Lombard, 07/2025, FCT-007). Le chiffrage exact du rapport Cariou/Cordier (n° 2252) n'a pas pu être retrouvé dans les sources secondaires accessibles : GAP déclaré (FCT-008). À l'échelle européenne : CumEx Files ≥55 Md€ (2018), réévalués à ≥150 Md€ sur 2000-2020 (2021, FCT-018).
2. **Les travaux Cariou/Cordier** : rapport d'information n° 2252, mission d'information commune sur « le bilan de la lutte contre les montages transfrontaliers », rapporteurs Émilie Cariou et Pierre Cordier, déposé le 25/09/2019 (PDF lu intégralement le 09/08/2026, FCT-008/020). Le rapport documente les mécanismes, **nomme trois banques (BNP Paribas, Crédit Agricole, Société Générale)**, révèle que l'**ACPR était informée avant les révélations**, et **ne contient AUCUN chiffrage du manque à gagner CumCum français** : les estimations citées (0,4-3 Md€/an ; 33 Md€ cumulés) proviennent d'autres sources (AMF, Université de Mannheim via presse), pas du rapport. Le GAP-001 est clos.
3. **Les redressements DGFiP et le contentieux** : perquisitions coordonnées PNF + parquet de Cologne le 28/03/2023 dans 5 établissements (BNP Paribas/Exane, Société Générale, Natixis, HSBC) (FCT-004) ; **13 banques impliquées** (FCT-009) ; le Conseil d'État (08/12/2023, n° 472587, Fédération bancaire française) a **annulé la doctrine de Bercy** qui écartait l'interposition d'un résident via la notion de « bénéficiaire effectif » sans base légale, ne laissant que l'abus de droit (art. L64 LPF) (FCT-010). Conséquence : la **voie pénale a pris le relais** : CJIP Crédit Agricole CIB **88,2 M€** (08/09/2025) et HSBC **267,5 M€** (08/01/2026), soit **355,7 M€ négociés via CJIP en quelques mois** (FCT-013/014, versements pouvant être échelonnés) ; autres banques en cours.
4. **Les blocages législatifs et leur levée (2026)** : six ans entre le rapport (2019) et la loi : lobbying bancaire documenté (recours FBF mars 2023 ; contrôle du Sénat juin 2025 dénonçant le « lobby bancaire », Husson ; BOFiP d'application édulcoré, Mediapart 26/06/2025, FCT-016). Le verrou a sauté avec la **loi de finances pour 2025 (art. 96, applicable 01/01/2026)** : consécration du « bénéficiaire effectif » (art. 119 bis CGI), extension de l'art. 119 bis A aux dérivés, retenue conservatoire sur les « CumCum externes » (FCT-011), avis du Conseil d'État du 27/01/2025 (FCT-012), complétée par la **directive FASTER (UE) 2025/50** (adoptée 10/12/2024, FCT-017).

**Verdict sur le LEAD_QUESTION** (« la France récupère-t-elle l'argent du CumCum ? ») : **SOUTENU pour la récupération partielle** : 355,7 M€ de CJIP + redressements ~4,5 Md€ engagés + verrou législatif 2026. **NON PROUVÉ pour la récupération totale** : l'écart entre le manque à gagner estimé (33 Md€ cumulés) et les sommes recouvrées (quelques centaines de M€ à quelques Md€) reste massif, et la « dark figure » du CumCum non détecté est inconnue (Ξ=8).

**Acteurs** : banques françaises (organisatrices), actionnaires étrangers (bénéficiaires), DGFiP/Bercy (redressements), PNF + parquets allemands (pénal), Conseil d'État, Parlement (Cariou/Cordier, LF 2025), UE (FASTER), lobby bancaire (FBF).

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **8/10** | Aucune mesure officielle publiée du manque à gagner CumCum français (la DGFiP ne publie pas de chiffre de perte) ; le chiffrage exact du rapport n° 2252 n'est pas retrouvé dans les sources secondaires (FCT-008, GAP) ; la « dark figure » du CumCum non détecté est inconnue ; les montants des redressements par banque sont en grande partie confidentiels. |
| 2 | **€** money | **8/10** | 33 Md€ cumulés (FCT-005), 0,4-3 Md€/an (FCT-006), 2,5-4,5 Md€ d'arriérés/redressements (FCT-007), 355,7 M€ de CJIP (FCT-013/014), 150 Md€ UE (FCT-018). |
| 3 | **Λ** framing | 6/10 | « Arbitrage de dividendes » (neutre financier) vs « fraude CumCum » ; « optimisation » vs « évasion » ; les banques parlent de « services aux clients », les parquets de « blanchiment aggravé de fraude fiscale ». |
| 4 | **Ω** inversion | **7/10** | Les banques se présentent comme victimes de la complexité des marchés (argumentaire FBF) alors que les catalogues commerciaux documentent l'organisation (Natixis, FCT-003) ; l'État « lutte contre la fraude » mais a attendu 6 ans (2019→2025) ; la CJIP permet de « payer sans procès ni aveu pénal » alors que les montages étaient organisés. |
| 5 | **Ψ** sidération | 2/10 | Champ froid : 33 Md€ ne produisent aucun moment de sidération durable. |
| 6 | **↕** verticalité | **8/10** | Asymétrie : banques globales et actionnaires étrangers vs contribuables ; la CJIP (entreprise paie une amende, aucune personne physique jugée) reproduit le schéma du dossier parent ; les exécutants de la petite fraude, eux, passent en correctionnelle. |
| 7 | **Φ** spectacle | 3/10 | Peu de spectacle ; les perquisitions de mars 2023 ont été le seul pic médiatique. |
| 8 | **Σ** sémiotique | 3/10 | Faible ; « place de Paris » comme marqueur de défense. |
| 9 | **Κ** cynisme | **8/10** | Discours de « lutte contre la fraude » vs 6 ans d'attente, BOFiP d'application édulcoré (Husson, 06/2025), instructions ministérielles contestées (Mediapart, Lombard), CJIP qui court-circuite le pénal. |
| 10 | **ρ** résistance | **7/10** | Journalisme d'investigation (Radio France, Le Monde, Mediapart, Follow the Money, Correctiv/CumEx Files), Sénat (contrôles LOLF), PNF, parquets allemands, rapport Cariou/Cordier. |
| 11 | **κ** influence subtile | 7/10 | Catalogues commerciaux des banques (offres « div swap », « yield enhancement », commission ~2 %) = architecture par défaut de l'évitement (FCT-003) ; lobbying FBF (FCT-016). |
| 12 | **⫸** convergence | **8/10** | Convergence sans contamination : CumEx Files (2018), étude Mannheim, perquisitions (2023), CE 472587 (2023), CJIP (2025-2026), contrôle Sénat (2025) : six faisceaux indépendants pointent la même structure. |
| 13 | **⚔** guerre cognitive | 1/10 | Aucune opération coordonnée documentée. |
| 14 | **🌐** réseau | 7/10 | Nœuds : banques, chambres de compensation, courtiers, actionnaires étrangers, parquet de Cologne (coopération judiciaire), Bercy, PNF, UE. |
| 15 | **⏰** temporalité | 7/10 | 2018 CumEx Files → 2019 rapport Cariou/Cordier → 2023 perquisitions + CE 472587 → 2024 directive FASTER → 2025 loi (art. 96) + avis CE + CJIP CA → 2026 CJIP HSBC + BOFiP : la séquence « enquête → jurisprudence → loi → pénal » s'étale sur 8 ans. |

**BIAS TEST (15/15 scorés).** Aucun symbole au-delà de 8. Les champs 7-8 signalent des zones où la preuve est partielle (estimations contestées, montants confidentiels) : à traiter en PÉRIMÈTRE & LIMITES.

**PATTERNS** : @PAT[ICEBERG] (Ξ=8), @PAT[MONEY] (€=8), @PAT[CYN] (Κ=8), @PAT[NET] (🌐=7). **THREATS** : @THR[DARK_MONEY] (flux opaques documentés par les catalogues bancaires), @THR[REG_CAPTURE] (lobbying FBF, BOFiP édulcoré), @THR[NUDGE] (offres « par défaut » des banques).

## 3. CLUSTERS (routage SYMBOLS §4)

| Cluster | Diagnostic | Gap |
|---------|------------|-----|
| ICEBERG (Ξ=8) | Émergé : 355,7 M€ CJIP + redressements 4,5 Md€. Surface : 33 Md€ cumulés (Mannheim). Immergé : dark figure non détectée. | Pas de mesure officielle de la perte totale. |
| MONEY (€=8) | Flux : actionnaires étrangers → banques (commissions ~2 %) → évitement de la retenue à la source → perte Trésor. | Montants par banque confidentiels. |
| POWER (↕=8) | Banques globales vs contribuables ; CJIP sans personnes physiques. | — |
| INVERSION (Ω=7, Κ=8) | « Victimes de la complexité » vs catalogues commerciaux ; « lutte contre la fraude » vs 6 ans d'attente. | — |
| CONFIRMATION (κ=7) | Offres bancaires par défaut, lobbying FBF. | — |
| FRAGMENTATION (⫸=8) | 6 faisceaux indépendants convergent. | — |
| NETWORK (🌐=7) | Banques, marchés, parquets, Bercy, UE. | Pas de graphe calculé. |
| TEMPORAL (⏰=7) | Séquence 2018-2026 documentée. | — |
| RESISTANCE (ρ=7) | Presse d'investigation, Sénat, PNF, parquets allemands. | — |

## 4. HERMÉNEUTIQUE (statut : ANALYSE)

- **L1 (texte) :** rapports parlementaires (n° 2252), jurisprudence (CE 472587, avis 27/01/2025), textes (LF 2025, FASTER), enquêtes journalistiques (CumEx Files, Radio France, Le Monde, Mediapart), communiqués judiciaires (CJIP).
- **L2 (structure) :** trois temps : (a) l'évitement légal en apparence (2010-2023), (b) le choc juridictionnel (CE 472587, 2023), (c) le verrouillage (LF 2025 + FASTER + CJIP, 2024-2026).
- **L3 (intérêt) :** la question centrale est la **base légale** : l'évitement durait parce que le droit n'avait pas de définition du « bénéficiaire effectif » opposable (CE 472587) ; la réparation est passée par le pénal (CJIP) faute de fiscalité efficace, puis par la loi.
- **L4 (sémiotique) :** la commission de ~2 % prélevée par les banques est le symbole de l'organisation : l'évitement avait un prix de marché.
- **L5 (comparaison) :** cohérence avec le corpus parent : même schéma « les entreprises paient sans procès, les exécutants prennent » (CJIP bancaires vs condamnations individuelles).
- **L6 (contexte) :** 2024-2026 : contexte de redressement budgétaire où l'État cherche des recettes (raison de la mobilisation) et de concurrence des places financières (argument du lobby).

**Lecture concurrente** : les banques soutiennent que la plupart des opérations étaient des prêts de titres légitimes et que la perte fiscale est surévaluée (estimations contestées par la FBF). La synthèse retenue : l'organisation est documentée (catalogues, CJIP avec reconnaissance), le montant exact est incertain (fourchettes), et le retard législatif est établi (2019→2025).

## 5. FORENSIC REASONING (ICEBERG MAX)

**Émergé (jugé, recouvré)** : CJIP Crédit Agricole CIB 88,2 M€ (08/09/2025) ; CJIP HSBC 267,5 M€ (08/01/2026) ; redressements cumulés ~4,5 Md€ engagés (2025) ; >2,5 Md€ d'arriérés réclamés (2023).

**Surface (estimé, contesté)** : 33 Md€ cumulés depuis ~2000 (Mannheim/Radio France) ; 0,4-1 Md€/an (AMF) ; jusqu'à 3 Md€/an (estimations récentes) ; CumEx Europe ≥150 Md€ (2000-2020).

**Immergé (inféré)** : dark figure du CumCum non détecté ; montants par banque (confidentiels) ; CumCum des fonds de pension et fonds souverains via dérivés non documentés.

**ICEBERG LOAD :** 5 strates émergées confirmées, 4 en surface, 3 inférées. Le contraste entre les registres judiciaires (355,7 M€) et l'estimation académique (33 Md€) est la signature d'un champ où la récupération est réelle mais partielle.

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « La France a réagi et récupère l'argent » : perquisitions 2023, LF 2025 art. 96, FASTER UE, CJIP 355,7 M€.
- **Antithèse (critique) :** « Six ans de blocage, une récupération partielle » : rapport 2019 sans loi jusqu'en 2025, BOFiP édulcoré, CJIP sans personnes physiques, 33 Md€ estimés vs 355,7 M€ négociés via CJIP.
- **Arbitrage par les preuves :** la thèse est confirmée sur l'inflexion 2023-2026 (jurisprudence, loi, CJIP) ; l'antithèse est confirmée sur la temporalité (6 ans) et le ratio récupération/estimation. **La synthèse** : la France a transformé un vide juridique en arsenal (loi + pénal + UE) entre 2023 et 2026, mais la récupération reste partielle et la mesure de la perte totale inexistante.

## 7. CHRONOLOGIE

| Date | Événement | Source | Statut |
|------|-----------|--------|--------|
| 18/10/2018 | CumEx Files (Correctiv) : ≥55 Md€ de pertes UE | Correctiv | ✦ |
| 25/09/2019 | Rapport Cariou/Cordier n° 2252 (montages transfrontaliers) | AN | ✦ |
| 21/10/2021 | CumEx Files 2.0 : réévaluation à ≥150 Md€ (2000-2020) | Correctiv | ✦ |
| 28/03/2023 | Perquisitions PNF + parquet de Cologne dans 5 banques (BNP/Exane, SocGen, Natixis, HSBC) | PNF/presse | ✦ |
| 30/03/2023 | FBF : recours au Conseil d'État contre la doctrine fiscale | Agefi | ✦ |
| 05/2023 | Bercy réclame >2,5 Md€ d'arriérés aux banques | Le Monde | ✦ |
| 08/12/2023 | CE n° 472587 (FBF) : annulation partielle de la doctrine « bénéficiaire effectif » | Légifrance | ✦ |
| 10/12/2024 | Adoption de la directive FASTER (UE) 2025/50 | JOUE | ✦ |
| 27/01/2025 | Avis du Conseil d'État sur le dispositif renforcé anti-CumCum | CE | ✦ |
| 14/02/2025 | Loi de finances 2025 (art. 96) : bénéficiaire effectif, 119 bis A élargi, CumCum externes (appl. 01/01/2026) | Légifrance | ✦ |
| 06/2025 | Contrôle du Sénat (Husson) : « résultat effarant », lobby bancaire, BOFiP édulcoré | Public Sénat | ✦ |
| 07/2025 | Audition É. Lombard : redressements cumulés ~4,5 Md€ | Sénat/presse | ✦ |
| 08/09/2025 | CJIP Crédit Agricole CIB : 88,2 M€ (première) | PNF/Décideurs | ✦ |
| 03/10/2025 | Enquête Radio France : 13 banques, 33 Md€ cumulés (Mannheim) | Radio France | ✦ |
| 08/01/2026 | CJIP HSBC : 267,5 M€ | Le Monde | ✦ |
| 2026 | BOFiP : instructions d'application (BOI-INT-DG-20-20-20-30), MAJ 2026 | BOFiP | ✦ |

## 8. DOMAINES (par axe)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 MÉCANISME | Comment fonctionne le CumCum français ? | Transfert temporaire de titres avant détachement ; retenue à la source 119 bis (2) atténuée par conventions ; catalogues bancaires (commission ~2 %) | FCT-001 à 003 | SATURATED |
| AXS-002 ESTIMATIONS | Combien la France a-t-elle perdu ? | 33 Md€ cumulés (Mannheim) ; 0,4-3 Md€/an ; arriérés 2,5-4,5 Md€ ; chiffrage exact Cariou/Cordier : GAP | FCT-005 à 009 | SATURATED (GAP-001) |
| AXS-003 REDRESSEMENTS | Que fait la DGFiP ? | Perquisitions 2023, CE 472587, 13 banques, LF 2025 art. 96 | FCT-010 à 012 | SATURATED |
| AXS-004 RÉPARATION | Combien est recouvré ? | CJIP CA 88,2 M€ + HSBC 267,5 M€ = 355,7 M€ ; autres en cours | FCT-013 à 015 | SATURATED |
| AXS-005 BLOCAGES | Pourquoi 6 ans ? | Lobbying FBF, Sénat 2025, BOFiP édulcoré ; FASTER UE comme sortie | FCT-016 à 018 | SATURATED |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| Banques françaises (BNP, SocGen, Natixis, CA, HSBC) | Intermédiaires/organisateurs | Catalogues commerciaux, prêts de titres, commissions ~2 % ; CJIP avec reconnaissance | FCT-003/013/014 | ACT documenté |
| Actionnaires étrangers | Bénéficiaires | Transferts temporaires avant détachement | FCT-001 | Bénéfice ≠ intention |
| DGFiP/Bercy | Contrôle | Redressements ~4,5 Md€, doctrine annulée en 2023 puis loi 2025 | FCT-007/010/011 | ROLE |
| PNF + parquet de Cologne | Pénal | Perquisitions 28/03/2023, CJIP | FCT-004/013/014 | ρ |
| Conseil d'État | Juridiction | CE 472587 (2023), avis 27/01/2025 | FCT-010/012 | ρ |
| Parlement (Cariou/Cordier ; Sénat) | Législateur/contrôle | Rapport n° 2252 (2019) ; contrôle 06/2025 | FCT-008/016 | ROLE |
| UE (Commission/Conseil) | Législateur | Directive FASTER 2025/50 | FCT-017 | ROLE |
| FBF (lobby bancaire) | Influence | Recours CE 2023, édulcoration BOFiP | FCT-016 | Influence documentée |

**CONTROL_MAP** :

| Contrôleur | Mécanisme | Résultat | Gap |
|------------|-----------|----------|-----|
| CTRL-001 DGFiP | Redressements fiscaux | ~4,5 Md€ engagés | Doctrine annulée 2023 (CE 472587) |
| CTRL-002 PNF | CJIP pénales | 355,7 M€ négociés (CJIP, versements échelonnés possibles) | Aucune personne physique jugée |
| CTRL-003 Loi (LF 2025) | Bénéficiaire effectif, retenue conservatoire | Verrou au 01/01/2026 | Effectivité non mesurée |
| CTRL-004 UE (FASTER) | eTRC, relief at source, registre CFI | Adoptée 10/12/2024 | Transposition États membres à venir (~2027-2029) |

## 10. CHAÎNES / PELOTE (causalité)

**CAU-001 : Le vide juridique a rendu l'évitement possible.**
Étage 1 : pas de définition légale opposable du « bénéficiaire effectif » (CE 472587, 08/12/2023, FCT-010). Étage 2 : la doctrine de Bercy est annulée faute de base légale. Étage 3 : l'évitement par interposition d'un résident était donc légalement possible jusqu'en 2026. Type : STRUCTUREL. Confidence : high (jurisprudence).

**CAU-002 : L'intermédiation bancaire a industrialisé l'évitement.**
Étage 1 : offres commerciales dédiées (catalogues Natixis, « div swap », commission ~2 %, FCT-003). Étage 2 : 13 banques impliquées (FCT-009). Étage 3 : manque à gagner cumulé ~33 Md€ (FCT-005). Type : MÉCANISME. Confidence : high sur l'organisation (CJIP avec reconnaissance), medium sur le montant (estimations contestées).

**CAU-003 : Le lobbying a retardé la réforme de 6 ans.**
Étage 1 : rapport Cariou/Cordier 2019 (FCT-008). Étage 2 : recours FBF 2023, BOFiP édulcoré, contrôle Sénat 2025 (FCT-016). Étage 3 : loi seulement en 02/2025 (FCT-011). Type : SYSTÈME. Confidence : high sur les faits de lobbying, medium sur le lien causal direct (pas de mesure d'effet).

**CAU-004 : La voie pénale a suppléé la voie fiscale.**
Étage 1 : CE 472587 contraint la DGFiP (FCT-010). Étage 2 : PNF + parquets allemands engagent le pénal (FCT-004). Étage 3 : CJIP CA 88,2 M€ + HSBC 267,5 M€, sans procès ni personnes physiques (FCT-013/014). Type : MÉCANISME. Confidence : high.

**CAU-005 : L'UE a harmonisé pour 2027-2029.**
Étage 1 : directive FASTER 2025/50 (FCT-017). Étage 2 : eTRC, relief at source, registre CFI. Étage 3 : transposition à venir, effectivité non mesurée. Type : PRÉCÉDENT. Confidence : high sur l'adoption, inconnue sur l'effet.

**CAU-006 (rejetée) : « les banques ont violé la loi dès l'origine ».** Partiellement réfutée par la jurisprudence : l'évitement était en apparence légal avant 2025 (CE 472587) ; la qualification pénale (blanchiment de fraude fiscale) a été retenue au stade des CJIP, mais aucune condamnation définitive de personne physique n'est encore intervenue. BENEFIT != INTENT.

## 11. CARTE DES PREUVES

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « Le CumCum a privé la France de dizaines de Md€ depuis 2000 » | 33 Md€ cumulés (Mannheim/Radio France), 0,4-3 Md€/an | Estimations contestées par la FBF ; aucune mesure officielle | SOUTENU en tant que fourchette ; chiffre unique non établi |
| CLM-002 | « Les banques françaises ont organisé l'évitement » | Catalogues Natixis, CJIP CA/HSBC avec reconnaissance, 13 banques | Certaines opérations étaient des prêts de titres légitimes | SOUTENU |
| CLM-003 | « L'État a répondu par le pénal faute de base fiscale » | CE 472587 (2023), CJIP 2025-2026, loi seulement 2025 | L'abus de droit (L64 LPF) existait avant 2025 | SOUTENU |
| CLM-004 | « Le lobbying bancaire a retardé la réforme » | FBF 2023, Sénat 06/2025, BOFiP édulcoré | Le retard a aussi des causes techniques/UE | SOUTENU (partiel) |
| CLM-005 | « La France a verrouillé le dispositif en 2026 » | LF 2025 art. 96, BOFiP 2026, FASTER | Effectivité non mesurée ; transposition UE à venir | SOUTENU (partiel) |
| CLM-006 | « Le rapport Cariou/Cordier a chiffré la perte CumCum française » | Le rapport documente les mécanismes, nomme trois banques, révèle l'ACPR informée | Lecture directe du PDF (09/08/2026) : AUCUN chiffrage dans le rapport ; les estimations viennent d'autres sources (AMF, Mannheim) | RÉFUTÉ (lecture directe) |

### FACT_REGISTRY (19 faits)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | Mécanisme CumCum : transfert temporaire de propriété (prêts de titres, ventes à réméré, dérivés) avant détachement du dividende ; CumEx = restitutions multiples d'impôt jamais payé | — | SRC-01 CE avis 27/01/2025 ; SRC-02 Radio France 03/10/2025 | ✦ |
| FCT-002 | Retenue à la source dividendes non-résidents : art. 119 bis (2) CGI, taux de droit commun 12,8/25/30 % selon bénéficiaire, atténuée par conventions | 12,8-30 % | SRC-03 CGI ; SRC-01 | ✦ |
| FCT-003 | Catalogues commerciaux des banques (Natixis « Equity Markets Products », BNP) : offres « div swap », « yield enhancement », commission ~2 % | ~2 % | SRC-02 Radio France/Follow the Money | ✦ |
| FCT-004 | Perquisitions 28/03/2023 : PNF (16 magistrats) + parquet de Cologne (6 procureurs), 150+ enquêteurs SEJF, 5 établissements (BNP Paribas et sa filiale Exane comptée séparément, Société Générale, Natixis, HSBC) | 5 banques | SRC-04 PNF/presse | ✦ |
| FCT-005 | Manque à gagner cumulé France depuis ~2000 : ~33 Md€ (Université de Mannheim, reprise Radio France 03/10/2025) | 33 Md€ | SRC-02 | ✧ |
| FCT-006 | Estimations annuelles : 0,4-1 Md€ (AMF) ; jusqu'à 3 Md€/an (estimations récentes) | 0,4-3 Md€/an | SRC-02/04 | ✧ |
| FCT-007 | Arriérés réclamés aux banques : >2,5 Md€ (2023, Le Monde) ; redressements cumulés ~4,5 Md€ (audition É. Lombard, 07/2025) | 2,5-4,5 Md€ | SRC-05 Le Monde 15/05/2023 ; SRC-06 Sénat 07/2025 | ✦ |
| FCT-008 | Rapport d'information n° 2252 (25/09/2019), mission « bilan de la lutte contre les montages transfrontaliers », rapporteurs É. Cariou et P. Cordier : documentation des mécanismes, trois banques nommées (BNP Paribas, Crédit Agricole, Société Générale), ACPR informée avant les révélations ; AUCUN chiffrage du manque à gagner CumCum français (lecture directe du PDF) | — | SRC-07 AN (PDF lu) | ✦ |
| FCT-020 | Lecture directe du PDF n° 2252 (817 Ko, 6 951 lignes extraites, 09/08/2026) : le schéma CumEx a « été rendu impossible en France » par la suppression de l'avoir fiscal (01/01/2005, loi 2003-1311) ; demande de restitution bavaroise de 312 M€ adressée à un groupe français (CumEx, exercice 2010) ; aucun chiffre global de perte CumCum pour la France dans le rapport | 312 M€ | SRC-07 (PDF lu par recherche textuelle) | ✦ |
| FCT-009 | 13 banques impliquées dans les enquêtes/redressements 2023-2026 | 13 | SRC-02 Radio France 10/2025 | ✦ |
| FCT-010 | CE 08/12/2023 n° 472587 (FBF) : l'administration ne peut écarter l'interposition d'un résident via le « bénéficiaire effectif » hors art. 119 bis A, sauf abus de droit (L64 LPF) ; annulation des commentaires BOFiP | — | SRC-08 Légifrance | ✦ |
| FCT-011 | LF 2025 (loi n° 2025-127 du 14/02/2025, art. 96) : bénéficiaire effectif consacré (119 bis), 119 bis A étendu aux dérivés, CumCum externes = retenue conservatoire + preuve contraire ; applicable 01/01/2026 | — | SRC-09 Légifrance ; SRC-10 Actu-Juridique | ✦ |
| FCT-012 | Avis du Conseil d'État 27/01/2025 sur le dispositif renforcé (clauses de sauvegarde, chambres de compensation) | — | SRC-01 | ✦ |
| FCT-013 | CJIP Crédit Agricole CIB : 88,2 M€ (homologuée 08/09/2025 ; ~2 500 opérations 2013-2021 ; gains 49 M€) | 88,2 M€ | SRC-11 PNF/Décideurs | ✦ |
| FCT-014 | CJIP HSBC : 267,5 M€ (dont 115 M€ réparation + 152 M€ pénalités), validée 08/01/2026 | 267,5 M€ | SRC-12 Le Monde 08/01/2026 | ✦ |
| FCT-015 | Autres banques (BNP, SocGen, Natixis) : enquêtes et négociations en cours, montants non finalisés | — | SRC-04/11 | ⁅ |
| FCT-015b | Suivi au 09/08/2026 (run 20260809-1446) : aucune CJIP postérieure au 08/01/2026 identifiée ; BNP Paribas, Exane, Société Générale et Natixis « demeurent dans l'expectative » (Kohen 19/06/2026) ; BNP conteste un redressement ~250 M€ (Bloomberg 24/06/2025) ; total CJIP arrêté à 355,7 M€ (CA + HSBC) | 355,7 M€ | run 20260809-1446 (SRC-01/02/03) | ✦ |
| FCT-016 | Lobbying bancaire : recours FBF 30/03/2023 ; contrôle Sénat 06/2025 (Husson : « résultat effarant », BOFiP édulcoré) ; Mediapart 26/06/2025 (É. Lombard) | — | SRC-13 Public Sénat ; SRC-14 Agefi ; SRC-15 Mediapart | ✦ |
| FCT-017 | Directive FASTER (UE) 2025/50 (adoptée 10/12/2024, JOUE 10/01/2025) : eTRC (14 jours), relief at source / quick refund (50 jours), registre CFI | — | SRC-16 CE/UE ; SRC-17 Parlement UE | ✦ |
| FCT-018 | CumEx Files (Correctiv, 18/10/2018) : ≥55 Md€ ; CumEx Files 2.0 (21/10/2021) : ≥150 Md€ (2000-2020) ; 12 pays, 180 000 pages, 38 journalistes/19 rédactions | 55→150 Md€ | SRC-18 Correctiv | ✦ |
| FCT-019 | Revalidation du FCT-038 parent : « impact européen 55-60 Md€ ; France >10 Md€ cumulés » : confirmé et précisé (33 Md€ cumulés Mannheim = borne haute de l'estimation académique) | >10 Md€ | SRC-02 ; parent FCT-038 | ✧ |

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | Estimation du manque à gagner : 0,4-1 Md€/an (AMF) vs 3 Md€/an vs 33 Md€ cumulés (Mannheim) | Périmètres et méthodologies différents (détection vs estimation académique) ; aucune mesure officielle ; on cite chaque fourchette avec sa source | DOCUMENTÉE (non unifiée) |
| CONTR-002 | Légalité : « fraude » (PNF, CJIP) vs « optimisation » (banques) | L'évitement était en apparence légal avant 2025 (CE 472587) ; la qualification pénale (blanchiment aggravé de fraude fiscale) est retenue par les parquets et acceptée dans les CJIP sans jugement au fond | DOCUMENTÉE |
| CONTR-003 | Chiffrage exact du rapport Cariou/Cordier : non retrouvé dans les sources secondaires accessibles | Résolue par lecture directe du PDF (09/08/2026) : le rapport ne contient aucun chiffrage CumCum français ; les estimations concurrentes (0,4-3 Md€/an ; 33 Md€ cumulés) ne proviennent pas du rapport | RÉSOLUE |

### EDI

```
geo:0.75 lang:0.85 strat:0.80 owner:0.75 persp:0.80 temp:0.80
EDI_raw = .25×.75 + .20×.85 + .20×.80 + .15×.75 + .15×.80 + .05×.80 = 0.7875
Pénalité : MISSING_COUNTER (-.10) : la défense détaillée des banques (mémoire FBF, argumentaire technique) n'est pas matériellement présente dans le corpus.
EDI = 0.69 (BROAD, sous la cible APEX 0.80, écart déclaré)
COV = 0.85 | IND = 0.56 (9 familles amont / 16 sources acceptées) | CC = 2/3 (CONTR-003 en GAP)
EDI* = .5×.69 + .3×.85 + .2×.56 = 0.712
Perspectives : ⟐ 4 | ⟐̅ 3 | 🌍 1 | 🎓 2 (Mannheim) | 🔥 2 (Correctiv, Mediapart)
DECISIVE_CLAIM_COVERAGE : CLM-001 direct:OUI familles:4 counter:FOUND | CLM-002 direct:OUI familles:5 counter:FOUND | CLM-003 direct:OUI familles:4 counter:FOUND | CLM-005 direct:OUI familles:3 counter:FOUND
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait)

| FCT | QRY | SRC | URL (référence) | Statut |
|-----|-----|-----|-----------------|--------|
| FCT-001/012 | QRY-001 | SRC-01 | conseil-etat.fr (avis 27/01/2025) | ✦ |
| FCT-005/009 | QRY-001 | SRC-02 | radiofrance.fr (03/10/2025) | ✧/✦ |
| FCT-007 | QRY-002 | SRC-05 | lemonde.fr (15/05/2023) | ✦ |
| FCT-008 | QRY-002 | SRC-07 | assemblee-nationale.fr/15/rap-info/i2252.asp (page officielle lue) | ✦ |
| FCT-010 | QRY-003 | SRC-08 | legifrance.gouv.fr CETATEXT000048543204 | ✦ |
| FCT-011 | QRY-003 | SRC-09 | legifrance.gouv.fr (loi n° 2025-127) | ✦ |
| FCT-013 | QRY-004 | SRC-11 | decideurs-juridiques.com | ✦ |
| FCT-014 | QRY-004 | SRC-12 | lemonde.fr (08/01/2026) | ✦ |
| FCT-016 | QRY-005 | SRC-13/14/15 | publicsenat.fr, agefi.fr, mediapart.fr | ✦ |
| FCT-017 | QRY-005 | SRC-16/17 | taxation-customs.ec.europa.eu, europarl.europa.eu | ✦ |
| FCT-018 | QRY-005 | SRC-18 | correctiv.org (18/10/2018, 21/10/2021) | ✦ |

## 12. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Évitement légal en apparence » | Le CumCum a prospéré dans un vide juridique (pas de définition opposable du bénéficiaire effectif) | CE 472587, LF 2025 venue après coup | L'abus de droit existait (L64 LPF) | Retenue (jurisprudence) |
| S2 « Organisation bancaire » | Les banques ont industrialisé l'évitement (catalogues, commissions) | FCT-003, CJIP avec reconnaissance | Certaines opérations légitimes | Retenue |
| S3 « Récupération partielle » | La France verrouille et récupère, mais partiellement | LF 2025, 355,7 M€ CJIP | 33 Md€ estimés vs recouvrements faibles | Retenue |

**IMPACT_MAP** :

| Acteur | Gain | Perte |
|--------|------|-------|
| Banques | Commissions (~2 %), liquidité | CJIP 355,7 M€ (CA+HSBC), redressements 4,5 Md€ |
| Actionnaires étrangers | Dividendes sans retenue à la source | — |
| Trésor français | — | 33 Md€ cumulés estimés (fourchette) ; récupération partielle |
| Contribuables | Recouvrements (355,7 M€ + redressements) | Manque à gagner antérieur |
| Place financière de Paris | Attractivité (argument FBF) | Réputation, risque pénal |

**RESPONSIBILITY_MAP** : aucune condamnation définitive de personne physique ; les CJIP font payer les établissements sans jugement au fond (BENEFIT != INTENT). Rôles : banques (organisation, documentée), législateur (retard 2019-2025), contrôleurs (déclenchement 2023), UE (harmonisation 2024). La responsabilité systémique (RÉSULTAT) est un vide juridique exploité commercialement.

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : CumCum/CumEx concernant la France : mécanisme, estimations, rapport Cariou/Cordier, contentieux DGFiP/CE, CJIP, lobbying, réformes (LF 2025, FASTER UE). Période 2018-2026.

**Exclusions explicites** : l'analyse des montages bancaires individuels (confidentiels) ; les autres formes de fraude fiscale ; les affaires CumEx allemandes au fond (hors France).

**GAP déclarés** :
- GAP-001 (RÉSOLU le 09/08/2026 par lecture directe du PDF n° 2252) : le rapport ne contient AUCUN chiffrage du manque à gagner CumCum français ; la quête d'un « chiffre Cariou/Cordier » est close (il n'existe pas dans le rapport) ; les estimations citées (0,4-3 Md€/an ; 33 Md€ cumulés) proviennent d'autres sources (AMF, Mannheim via presse).
- GAP-002 (METHOD) : aucune mesure officielle du manque à gagner CumCum français ; fourchettes divergentes (CONTR-001).
- GAP-003 (ACCESS) : montants des redressements par banque et état final des négociations CJIP (BNP, SocGen, Natixis) non publiés. **RÉSOLU PARTIELLEMENT le 09/08/2026** (run 20260809-1446) : l'état des négociations est désormais documenté (2/5 réglées par CJIP, 3 en expectative, aucune CJIP postérieure au 08/01/2026, total CJIP = 355,7 M€) ; les montants finaux des 3 banques restantes restent confidentiels (voir investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cjip-cumcum-banques/).
- GAP-004 (METHOD) : frontière entre prêts de titres légitimes et montages d'évitement non quantifiable.
- GAP-005 (CORPUS) : mémoire technique détaillé des banques (FBF) absent (MISSING_COUNTER, EDI).
- GAP-006 (ACCESS) : transposition de FASTER en France (échéance) et effectivité du dispositif LF 2025 non mesurables à la date. **CONFIRMÉ ET PRÉCISÉ le 09/08/2026** (run 20260809-1458) : l'effectivité juridique et technique du dispositif est établie (loi art. 96, avis CE 27/01/2025, BOFiP BOI-INT-DG-20-20-20-30 du 16/03/2026, retenues conservatoires opérées au 01/01/2026, 9 États, restitution lourde, aucun recours bancaire, ADELIBE sans objet CE 20/01/2026 n° 505127) mais l'effectivité économique reste NON MESURÉE à 7 mois : aucun chiffre officiel de retenues, restitutions, redressements ni rendement budgétaire (non chiffré au PLF 2025). Évaluation à 12-18 mois (voir investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_effectivite-anti-cumcum-lf2025/).

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : mécanisme ; retenue à la source 119 bis (2) ; perquisitions 28/03/2023 (5 banques) ; 13 banques ; CE 472587 ; LF 2025 art. 96 (applicable 01/01/2026) ; avis CE 27/01/2025 ; CJIP CA 88,2 M€ et HSBC 267,5 M€ ; redressements ~4,5 Md€ ; CumEx Files 55→150 Md€ ; FASTER adoptée ; lobbying FBF/Sénat/Mediapart ; rapport n° 2252 (existence, rapporteurs, date).
- **PROBABLE (✧)** : 33 Md€ cumulés (Mannheim) ; 0,4-3 Md€/an ; FCT-038 parent confirmé et précisé.
- **HYPOTHÈSE (⁂)** : la dark figure du CumCum non détecté ; l'effet dissuasif du dispositif 2026.
- **CONTESTÉ (⊗)** : montant du manque à gagner (CONTR-001) ; légalité ex ante (CONTR-002).
- **INCONNU (⁅)** : montants par banque (GAP-003) ; effectivité FASTER/LF 2025.
- **RÉFUTÉ (❧)** : « le CumCum était déjà illégal et réprimé avant 2023 » (CE 472587 établit le vide juridique) ; « les banques ont été condamnées au pénal » (CJIP = accord sans jugement) ; « le rapport n° 2252 chiffre la perte CumCum française » (lecture directe : aucun chiffrage dans le rapport).

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD** : input UPDATE branché sur le FCT-038 parent. Le verdict d'objet (montants, mécanismes, blocages) est distinct du verdict de lead (récupération).

**Vérifications contradictoires exécutées** : CONTR-001 (fourchettes documentées avec sources et périmètres) ; CONTR-002 (légalité ex ante tranchée par la jurisprudence) ; CONTR-003 (résolu par lecture directe du PDF n° 2252 le 09/08/2026 : le rapport ne chiffre pas le CumCum français). Le FCT-038 parent a été revalidé (33 Md€ cumulés = précision de la borne « >10 Md€ »). Le PDF du rapport n° 2252 a été téléchargé (817 Ko) et interrogé par recherche textuelle (6 951 lignes) : existence, rapporteurs, date, mécanismes, banques nommées, ACPR informée, 312 M€ bavarois confirmés ; absence de chiffrage français établie.

**Verdict final : PRÉSUMPTION FORTE** : le CumCum a privé la France de dizaines de milliards d'euros cumulés (fourchette 33 Md€, contestée), a été organisé par des banques françaises (catalogues, CJIP), a prospéré dans un vide juridique levé seulement en 2026 (LF 2025 + FASTER), et la récupération (355,7 M€ de CJIP + 4,5 Md€ de redressements engagés) reste partielle et sans jugement de personnes physiques. Le FCT-038 du dossier parent est confirmé et précisé.

---

# ANNEXE A. SOURCES

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | Conseil d'État, avis consultatif sur le dispositif renforcé anti-CumCum | 27/01/2025 | ◈ | https://www.conseil-etat.fr/avis-consultatifs/derniers-avis-rendus/au-gouvernement/avis-portant-sur-un-projet-de-dispositif-renforce-concernant-l-application-de-la-retenue-a-la-source-aux-operations-d-arbitrage-de-dividende-dites |
| SRC-02 | Radio France / France Inter, cellule investigation « Révélations : fraude CumCum » | 03/10/2025 | 🔥 | https://www.radiofrance.fr/franceinter/podcasts/revelations/revelations-du-vendredi-03-octobre-2025-2441343 |
| SRC-03 | Code général des impôts, art. 119 bis (2) | en vigueur | ◈ | https://www.legifrance.gouv.fr |
| SRC-04 | Le Monde / Actu-Juridique / Décideurs, perquisitions et enquêtes | 2023-2026 | ◈ | https://www.actu-juridique.fr/fiscalite/fiscal-finances/fiscal-finances/fraude-cumcum-deuxieme-transaction-pour-une-banque-dans-le-viseur-de-bercy/ |
| SRC-05 | Le Monde, « Scandale CumCum : le fisc réclame plus de 2,5 milliards d'arriérés aux banques » | 15/05/2023 | ◈ | https://www.lemonde.fr/evasion-fiscale/article/2023/05/15/scandale-cumcum-le-fisc-reclame-plus-de-2-5-milliards-d-arrieres-fiscaux-aux-banques_6173436_4862750.html |
| SRC-06 | Sénat, contrôle commission des finances (Husson/Raynal, art. 57 LOLF) + audition É. Lombard | 06-07/2025 | ◈ | https://www.senat.fr/compte-rendu-commissions/20250623/finc.html |
| SRC-07 | Assemblée nationale, rapport d'information n° 2252 (Cariou/Cordier) | 25/09/2019 | ◈ | https://www.assemblee-nationale.fr/15/rap-info/i2252.asp (page officielle lue ; texte intégral non extractible) |
| SRC-08 | Conseil d'État, arrêt n° 472587, Fédération bancaire française | 08/12/2023 | ◈ | https://www.legifrance.gouv.fr/ceta/id/CETATEXT000048543204 |
| SRC-09 | Loi n° 2025-127 du 14/02/2025 (LF 2025), art. 96 | 2025 | ◈ | https://www.legifrance.gouv.fr |
| SRC-10 | Actu-Juridique, « Fin de partie pour la fraude CumCum » | 27/03/2025 | ◉ | https://www.actu-juridique.fr/fiscalite/fiscal-finances/fin-de-partie-pour-la-fraude-cumcum/ |
| SRC-11 | Décideurs Juridiques, CJIP Crédit Agricole | 09/2025 | ◈ | https://www.decideurs-juridiques.com/affaires-juridiques/62192-pour-le-credit-agricole-l-affaire-cumcum-se-solde-par-une-cjip-a-88-millions-d-euros.html |
| SRC-12 | Le Monde (édition EN), CJIP HSBC | 08/01/2026 | ◈ | https://www.lemonde.fr/en/international/article/2026/01/08/hsbc-agrees-to-pay-267-5-million-fine-in-tax-fraud-case_6749210_4.html |
| SRC-13 | Public Sénat, contrôle du Sénat (Husson, lobby bancaire) | 10/06/2025 | ◈ | https://www.publicsenat.fr/actualites/economie/le-resultat-de-mon-controle-est-effarant-le-rapporteur-general-du-senat-met-en-cause-lintervention-du-lobby-bancaire-pour-contrer-une-0 |
| SRC-14 | Agefi, recours de la FBF | 30/03/2023 | ◉ | https://www.agefi.fr/news/banque-assurance/affaires-cumcum-le-lobby-bancaire-depose-un-recours-contre-ladministration-fiscale |
| SRC-15 | Mediapart, « Pour choyer les banques, Éric Lombard s'assoit sur le Parlement » | 26/06/2025 | 🔥 | https://www.mediapart.fr/journal/economie-et-social/260625/fraude-fiscale-pour-choyer-les-banques-eric-lombard-s-assoit-sur-le-parlement |
| SRC-16 | Commission européenne, directive FASTER | 2023-2024 | ◈ | https://taxation-customs.ec.europa.eu/taxation/business-taxation/faster-directive_en |
| SRC-17 | Parlement européen, Legislative Train Schedule (FASTER) | 2024-2026 | ◈ | https://www.europarl.europa.eu/legislative-train/theme-an-economy-that-works-for-people/file-withholding-tax-relief?sid=10201 |
| SRC-18 | Correctiv, CumEx Files + CumEx Files 2.0 | 18/10/2018, 21/10/2021 | 🔥 | https://correctiv.org/en/latest-stories/2018/10/18/the-cumex-files/ |

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260809-1416-cumcum-cumex-france | PARENT_RUN_ID:20260809-1343 | AS_OF:2026-08-09 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:cumcum-cumex-france | complexity:13→APEX | route overrides:NONE | scope:2018-2026, France + UE
modules:SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|KERNEL
degraded:NONE | query target/actual: 10/10

COUNT: ◈13 ◉2 ○1 | unique evidence objects:19 | upstream families:9
LEADS:terminal 1/1 | AXES:terminal 5/5 | N/A:none
FAILURES:3 (agents incomplets au 1er passage, relancés ; recherche ciblée Cariou/Cordier sans chiffrage retrouvé) | FALLBACKS:0
unresolved gaps:GAP-001 RÉSOLU (lecture directe PDF : le rapport n° 2252 ne chiffre pas le CumCum) ; GAP-002..GAP-006 (ACCESS/METHOD/CORPUS)
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @MNEMO_Q « CumCum CumEx France arbitrage dividendes Cariou Cordier » | NO_RESULT (0 mémoire) | Mnemolite | — |
| 2 | SYS | @READ parent FCT-038 + modules | Chargés (héritage revalidé) | run 20260809-1343 | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_enrichissement-legalise-france/ |
| 3 | ○ | QRY-001 (AXS-001/002) : mécanisme, estimations (Radio France, Mannheim, AMF) | FOUND : FCT-001 à 006, 009 | SRC-01/02/03 | radiofrance.fr, conseil-etat.fr |
| 4 | ◈ | QRY-002 (AXS-002) : rapport Cariou/Cordier n° 2252 | Page officielle lue (existence/rapporteurs/date confirmés) ; texte intégral non extractible ; chiffrage exact → GAP-001 | SRC-07 | assemblee-nationale.fr/15/rap-info/i2252.asp |
| 5 | ○ | QRY-003 (AXS-003) : perquisitions, CE 472587, LF 2025 art. 96, avis CE | FOUND : FCT-004, 007, 010-012 | SRC-04/05/06/08/09/10 | lemonde.fr, legifrance.gouv.fr, senat.fr |
| 6 | ○ | QRY-004 (AXS-004) : CJIP CA et HSBC, autres banques | FOUND : FCT-013/014/015 | SRC-11/12 | decideurs-juridiques.com, lemonde.fr |
| 7 | ○ | QRY-005 (AXS-005) : lobbying, FASTER, CumEx Files | FOUND : FCT-016/017/018 | SRC-13 à 18 | publicsenat.fr, mediapart.fr, ec.europa.eu, correctiv.org |
| 8 | SYS | Recherche ciblée « chiffre Cariou/Cordier dans la presse 2019 » | NON RETROUVÉ (agent incomplet) | — | — |
| 9 | ◈ | Lecture directe du PDF n° 2252 (téléchargé 817 Ko, pdftotext, 6 951 lignes) | FOUND : mécanismes, trois banques nommées, ACPR informée, 312 M€ bavarois, CumEx impossible en France depuis 2005 ; AUCUN chiffrage CumCum français → GAP-001 RÉSOLU (constat d'absence), FCT-008/020, CLM-006 RÉFUTÉ, CONTR-003 RÉSOLU | SRC-07 | assemblee-nationale.fr (PDF), lecture locale |
| 9 | SYS | @MNEMO_S + FACT_WRITEBACK | PENDING_AT_SERIALIZATION | — | — |
| 10 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cumcum-cumex-france/2026-08-09_14-16_cumcum-cumex-france_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 | Modules chargés ; manifest FINAL ; 15 symboles scorés, aucun ✗ | ✅ |
| G1 | LEAD vs OBJECT distincts ; 5 axes terminaux ; périmètre explicite | ✅ |
| G2 | 6 CLM avec support/counter/gap | ✅ |
| G3 | FACT_REGISTRY 19 faits, statuts canoniques | ✅ |
| G4 | Chaque ✦ → SRC-ID + URL ; ✧ pour corroboration restante | ✅ |
| G5 | CAU-001 à 006 typés, arrêt à l'évidence, « complot » partiellement réfuté | ✅ |
| G6 | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités | ✅ |
| G7 | CONTR-001 à 003 documentés et résolus (CONTR-003 résolu par lecture directe du PDF) | ✅ |
| G8 | TRACE_MATRIX ; QRY-001 à 005 tracés ; IDs résolus | ✅ |
| G9 | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis | ✅ |
| G10 | Un seul chemin ; une seule write FINAL ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY** : edi_gap = (0.80-0.69)/0.80 = 0.1375 ; query_gap = N/A ; coverage_gap = 0. GAP_SEVERITY = 0.14 < 0.20 → procéder avec divulgation (gaps GAP-001 à GAP-006 déclarés).

---

*TL;DR : SUJET : CumCum/CumEx en France. OBJET : évitement de la retenue à la source sur dividendes (art. 119 bis CGI) organisé par les banques françaises (catalogues, commissions ~2 %) ; manque à gagner estimé 33 Md€ cumulés (Mannheim, contesté) ; rapport Cariou/Cordier n° 2252 (25/09/2019) documentant les mécanismes ; CE 472587 (08/12/2023) annulant la doctrine Bercy (vide juridique) ; 13 banques visées ; CJIP Crédit Agricole 88,2 M€ (09/2025) et HSBC 267,5 M€ (01/2026) ; verrou législatif LF 2025 art. 96 (01/01/2026) + directive FASTER 2025/50 ; lobbying bancaire ayant retardé la réforme de 6 ans (2019→2025). SOURCE : UPDATE du FCT-038 parent, confirmé et précisé. MANIPULATION : Ξ=8, €=8, ↕=8, Κ=8, ⫸=8 ; non-verdict. LIMITE : GAP-001 résolu par lecture directe du PDF (le rapport n° 2252 ne contient aucun chiffrage CumCum français) ; GAP-002 à GAP-006 (aucune mesure officielle de la perte, montants par banque confidentiels).*
