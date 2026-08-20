# INVESTIGATION : « ATOS À LA CASSE » — Démantèlement du champion informatique français (scission, EPEI, Bull racheté par l'État, 2021-2026)

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260814-1000-atos-demantelement
PARENT_RUN_ID  : NONE (INPUT_KIND=TOPIC) ; corpus frère : 20260809-1507-decoupe-actifs-strategiques, 20260812-1800-iceberg-max-alstom-areva, 20260809-1535-grille-ief-photonis-latecoere
AS_OF          : 2026-08-13
INPUT_KIND     : TOPIC (thème : démantèlement du groupe Atos 2021-2026 : scission, tentatives de cession à EPEI, vente de Worldgrid, rachat de Bull par l'État, restructuration financière)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique utilisateur, re-pipeline T5 cessions)
SUBJECT_SLUG   : atos-demantelement
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-14_atos-demantelement/2026-08-14_10-00_atos-demantelement_INVESTIGATION.md
SCOPE          : Atos 2021-2026 : annonce de scission (2022), négociations EPEI/Křetínský (2023-2024), échec, restructuration financière (sauvegarde, 2024), ventes d'actifs (Worldgrid/ALTEN, Bull/État), rôle de l'État (Bpifrance, APE, action de préférence), cadre IEF ; période 2021-2026 ; géographie : France, Tchéquie
COMPLEXITY     : CX_SCORE=13 → $CX=APEX-léger (political 3, technical 2, temporal 3, geo 2, narratives 2, data 1)
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

**Réponse à l'OBJECT_QUESTION** (« Atos a-t-il été démantelé, et l'État a-t-il protégé les actifs stratégiques (supercalculateurs Bull, cyber) ? ») :

Atos, champion informatique français, a annoncé en **juin 2022** sa scission en deux entités (Tech Foundations / Eviden). En **août 2023**, il entre en négociations exclusives avec le groupe tchèque **EPEI (Daniel Křetínský)** pour vendre Tech Foundations (EV **2 Md€**, transfert de **1,9 Md€** de passifs) ; les négociations **échouent le 28/02/2024**. Le groupe accumule des pertes (plus de **3 Md€** en 2023) et une dette brute d'environ **4,8-5 Md€** ; un plan de restructuration sous sauvegarde accélérée est approuvé (tribunal de commerce de Nanterre, oct. 2024) et **finalisé le 18/12/2024** (dette réduite de 2,1 Md€, créanciers à ~91 % du capital). Atos vend **Worldgrid** à ALTEN (EV 270 M€, finalisé 12/2024) et surtout **l'activité Advanced Computing (Bull, supercalculateurs)** à l'**État français** (EV **404 M€**, finalisé **31/03/2026**), après que des sénateurs eurent appelé à l'entrée de Bpifrance (04/2024) et que l'État eut mis en place une protection juridique (action de préférence, 11/2024). La vente d'Eviden en bloc à EPEI (~2 Md€ évoqué) **n'a jamais abouti**.

**Verdict sur le LEAD_QUESTION** : **SOUTENU (démantèlement) / PARTIELLEMENT SOUTENU (protection)**. Le démantèlement est un fait : scission, échec de la cession à EPEI, restructuration par les créanciers, ventes d'actifs. La protection par l'État est réelle mais **tardive et partielle** : le rachat de Bull (404 M€) intervient après la crise, et les sénateurs réclamaient une entrée au capital dès 04/2024. Aucun fait pénal n'est documenté. Le pattern « laisser dégrader, puis racheter à perte » (Bull 404 M€ après des années de pertes) prolonge directement le pattern T5 « céder, perdre, racheter à perte » — ici en version inversée (le rachat par l'État après la destruction de valeur privée).

**Acteurs** : Atos (Bertrand Meunier, Nourdine Bihmane, Philippe Salle), EPEI (Daniel Křetínský), État (Bercy, APE, Bpifrance), ALTEN, CEA (utilisateur des supercalculateurs), Sénat (rapport r23-568), créanciers obligataires/bancaires.

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **9/10** | Chronologie complète des 15 cessions successives non consolidée ; valorisations confidentielles ; coûts de conseil ; le détail des « protections » de l'État (action de préférence) non publié ; rôle exact de l'IEF sur chaque cession non documenté. |
| 2 | **€** money | **9/10** | 2 Md€ (Tech Foundations), 1,9 Md€ passifs, 270 M€ (Worldgrid), 404 M€ (Bull), 3+ Md€ pertes 2023, 4,8-5 Md€ dette brute, 2,1 Md€ dette réduite, 2,9 Md€ conversion, 1,6 Md€ nouveaux financements, 91 % créanciers. |
| 3 | **Λ** framing | **8/10** | « Champion national » vs « boulet financier » ; « démantèlement » vs « recentrage » ; « souveraineté numérique » (supercalculateurs CEA) vs « sauvetage tardif » ; les créanciers présentés comme sauveurs vs liquidateurs de fait. |
| 4 | **Ω** inversion | **8/10** | L'État, qui avait laissé filer la valeur (absence de contrôle), se présente en protecteur final (rachat Bull) ; les créanciers (dont des fonds étrangers) deviennent propriétaires d'un champion stratégique ; EPEI échoue puis revient dans le paysage. |
| 5 | **Ψ** sidération | 4/10 | Champ technique (restructuration financière), peu de pic émotionnel. |
| 6 | **↕** verticalité | **8/10** | Décision concentrée (conseil d'administration, créanciers, État) ; salariés et sous-traitants subissent ; les actifs souverains (Bull/CEA) sont rachetés après destruction de valeur. |
| 7 | **Φ** spectacle | 3/10 | Peu de spectacle ; débats parlementaires (Sénat) techniques. |
| 8 | **Σ** sémiotique | **6/10** | « Bull », « supercalculateurs », « dissuasion » : symbolique technologique nationale forte. |
| 9 | **Κ** cynisme | **8/10** | L'État paie 404 M€ pour racheter un actif dont la valeur a été détruite sous ses yeux ; les appels à Bpifrance (04/2024) n'ont pas été suivis d'une entrée au capital, seulement d'un rachat tardif ; l'IEF (seuil 10 %, 2026) arrive après les faits. |
| 10 | **ρ** résistance | **7/10** | Sénat (rapport r23-568, 04/2024), sénateurs (appels Bpifrance), presse économique, syndicats ; pas de recours juridictionnel documenté. |
| 11 | **κ** influence subtile | **6/10** | Banques-conseils et conseils de restructuration (montants non publiés) ; négociations EPEI en huis clos ; rôle des agences de notation dans l'accélération de la crise. |
| 12 | **⫸** convergence | **7/10** | Convergence sans contamination : communiqués Atos, rapport Sénat, presse, communiqués Bercy convergent sur la même chronologie sans coordination documentée. |
| 13 | **⚔** guerre cognitive | 3/10 | Pas d'opération coordonnée documentée ; le récit « sauvetage souverain » (rachat Bull) est construit par l'exécutif. |
| 14 | **🌐** réseau | **7/10** | Nœuds : Atos, EPEI/Křetínský, Bercy/APE, Bpifrance, ALTEN, créanciers, CEA, Sénat. |
| 15 | **⏰** temporalité | **8/10** | 06/2022 (scission) → 08/2023 (EPEI) → 02/2024 (échec) → 10-12/2024 (sauvegarde) → 12/2024 (Worldgrid) → 06/2025 (offre État Bull) → 03/2026 (finalisation Bull) : boucle de 4 ans. |

## 3. CHRONOLOGIE

- **06/2022** : Atos annonce son plan de scission en deux sociétés cotées (Tech Foundations / Eviden).
- **01/08/2023** : négociations exclusives avec EPEI pour la vente de Tech Foundations (EV 2 Md€).
- **28/02/2024** : rupture des négociations EPEI/Tech Foundations (divergences financières).
- **04/2024** : rapport d'information du Sénat (r23-568) ; des sénateurs appellent à l'entrée de Bpifrance au capital.
- **06/2024** : négociations exclusives Worldgrid/ALTEN.
- **11/2024** : protections juridiques de l'État (action de préférence) pour sanctuariser les actifs critiques ; accord définitif Worldgrid/ALTEN (05/11/2024).
- **10-12/2024** : plan de sauvegarde accélérée approuvé (tribunal de commerce de Nanterre, oct. 2024) ; restructuration finalisée 18/12/2024.
- **12/2024** : finalisation de la vente de Worldgrid à ALTEN.
- **06/2025** : offre ferme de l'État pour l'activité Advanced Computing (Bull).
- **31/03/2026** : finalisation de la vente de Bull (Advanced Computing) à l'État (EV 404 M€).

## 4. FACT_REGISTRY (faits sourcés)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | Atos annonce (juin 2022) son plan de scission en deux sociétés cotées : Tech Foundations (infogérance historique) et Eviden (transformation numérique, cloud, cyber, HPC) | 06/2022 | SRC-01 communiqué Atos 06/2022 | ✦ |
| FCT-002 | 01/08/2023 : Atos entre en négociations exclusives avec EPEI (Daniel Křetínský) pour céder 100 % de Tech Foundations, valorisée EV 2 Md€ (impact trésorerie nette +0,1 Md€, transfert de 1,9 Md€ de passifs) | 2 Md€ ; 1,9 Md€ | SRC-02 communiqué Atos 01/08/2023 | ✦ |
| FCT-003 | EPEI prévoyait en outre de souscrire à une augmentation de capital réservée de 180 M€ pour acquérir 7,5 % d'Eviden | 180 M€ ; 7,5 % | SRC-02 communiqué Atos 01/08/2023 | ✦ |
| FCT-004 | 28/02/2024 : rupture officielle des négociations exclusives EPEI/Tech Foundations (divergences sur les conditions et la dégradation de la situation financière d'Atos) | 28/02/2024 | SRC-03 communiqué Atos 28/02/2024 ; SRC-04 Reuters 28/02/2024 | ✦ |
| FCT-005 | Atos enregistre plus de 3 Md€ de pertes nettes en 2023 ; dette brute d'environ 4,8 à 5 Md€ | >3 Md€ ; ~4,8-5 Md€ | SRC-05 publications financières Atos ; SRC-06 Les Echos | ✦ |
| FCT-006 | Procédure de sauvegarde accélérée ; plan de restructuration approuvé par le tribunal de commerce de Nanterre (octobre 2024) | 10/2024 | SRC-07 communiqué Atos 12/2024 | ✦ |
| FCT-007 | Restructuration finalisée le 18/12/2024 : réduction de la dette brute de 2,1 Md€ (conversion de créances obligataires/bancaires en capital à hauteur de 2,9 Md€), 1,6 Md€ de nouveaux financements, créanciers devenus actionnaires de référence à ~91 % | 2,1 Md€ ; 2,9 Md€ ; 1,6 Md€ ; 91 % | SRC-07 communiqué Atos 19/12/2024 ; SRC-06 Les Echos | ✦ |
| FCT-008 | Worldgrid (logiciels infrastructures énergétiques/nucléaires) vendu à ALTEN : accord définitif 05/11/2024, EV 270 M€, finalisé décembre 2024 | 270 M€ | SRC-08 communiqué Atos 11/2024 | ✦ |
| FCT-009 | Rapport d'information du Sénat sur la situation d'Atos (avril 2024) ; des sénateurs appellent à l'entrée de Bpifrance au capital du groupe | 04/2024 | SRC-09 senat.fr r23-568 ; SRC-10 Capital 11/04/2024 | ✦ |
| FCT-010 | Novembre 2024 : l'État met en place des protections juridiques (action de préférence) et formule des offres ciblées pour sanctuariser les actifs critiques de défense (supercalculateurs, cyber) | 11/2024 | SRC-11 presse/communiqués (état 11/2024) | ✧ |
| FCT-011 | Juin 2025 : offre ferme de l'État français pour l'acquisition de l'activité Advanced Computing d'Atos (Bull) | 06/2025 | SRC-12 communiqué ministère de l'Économie 02/06/2025 | ✦ |
| FCT-012 | Vente de Bull (Advanced Computing : supercalculateurs, quantique, ex-Eviden) à l'État français : EV 404 M€, dont 104 M€ de compléments de prix conditionnels ; exclusions Vision AI et zData | 404 M€ ; 104 M€ | SRC-13 communiqué Atos 31/03/2026 ; SRC-12 Bercy | ✦ |
| FCT-013 | Finalisation de la vente de Bull à l'État le 31/03/2026 ; l'État devient l'unique actionnaire de l'activité | 31/03/2026 | SRC-13 communiqué Atos 31/03/2026 | ✦ |
| FCT-014 | La vente d'Eviden en bloc à EPEI (montant ~2 Md€ évoqué par la presse) n'a jamais abouti : correction d'une rumeur répandue | — | SRC-05 publications Atos (état 2025-2026) | ✦ |
| FCT-015 | Cadre IEF consolidé : décret n° 2026-718 du 30/07/2026 (JO 02/08/2026), seuil de 10 % des droits de vote pour les investisseurs extra-européens dans les sociétés françaises cotées de secteurs sensibles | 10 % | SRC-14 Légifrance JORFTEXT000054596119 (déjà référencé corpus grille-ief) | ✦ |
| FCT-016 | Les supercalculateurs Bull/Atos sont utilisés pour la dissuasion nucléaire (CEA) : enjeu de souveraineté documenté à l'appui du rachat par l'État | — | SRC-09 Sénat r23-568 ; SRC-12 Bercy | ✧ |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-012 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-013 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-014 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-015 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
FCT-016 | FACT | ❧ | - | - | - | 2026-08-14_10-00_atos-demantelement | - | -
<!-- /FACT_REGISTRY_V1 -->

## 5. CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « Atos a été démantelé » | Scission (FCT-001), ventes d'actifs (FCT-008, FCT-012), restructuration par les créanciers à 91 % (FCT-007), échec EPEI (FCT-004) | Le groupe existe encore (plan Genesis) ; certaines activités sont rachetées par l'État (Bull) | SOUTENU (démantèlement de fait) |
| CLM-002 | « L'État protège les actifs stratégiques » | Action de préférence (FCT-010), rachat de Bull (FCT-011 à 013) | Intervention tardive (2024-2026) après des années de destruction de valeur ; pas d'entrée de Bpifrance au capital malgré les appels du Sénat ; l'IEF 10 % arrive en 2026 | PARTIELLEMENT SOUTENU (protection tardive et partielle) |
| CLM-003 | « EPEI a repris Atos » | Négociations 2023-2024 (FCT-002 à 004) | Négociations rompues le 28/02/2024 ; pas d'acquisition de Tech Foundations ni d'Eviden en bloc | RÉFUTÉE (à la date) |
| CLM-004 | « La France a racheté Bull à perte » | Bull vendu 404 M€ après >3 Md€ de pertes (FCT-005, FCT-012) | Le prix reflète l'actif net et les perspectives ; l'État n'a pas « payé plus que la valeur » documentée | PARTIELLEMENT SOUTENU (valeur détruite avant rachat, prix de marché) |

## 6. CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | « EPEI rachète Atos » (rumeur récurrente) vs « échec des négociations » (28/02/2024) | Les négociations exclusives ont été rompues ; aucune acquisition en bloc documentée ; EPEI n'est pas actionnaire | DOCUMENTÉE (rumeur réfutée) |
| CONTR-002 | « L'État protège la souveraineté numérique » vs « l'État intervient après la destruction de valeur » | Protection réelle (Bull 404 M€) mais tardive : les appels à Bpifrance datent de 04/2024, le rachat finalisé 03/2026 | DOCUMENTÉE (temporalité) |
| CONTR-003 | « Le sauvetage par les créanciers » (présenté comme un succès) vs « les actionnaires historiques sont dilués à ~9 % » | Le plan réduit la dette (2,1 Md€) mais transfère le contrôle aux créanciers (91 %) : le « sauvetage » est une reprise par les créanciers | DOCUMENTÉE (non tranchée) |

## 7. RÉSEAU D'ACTEURS

**Entreprises** : Atos (Tech Foundations, Eviden, Bull, Worldgrid), EPEI (Daniel Křetínský), ALTEN, Bpifrance (non entrée au capital), créanciers obligataires/bancaires.
**Institutions** : Bercy / APE, ministère de l'Économie, Sénat (rapport r23-568), tribunal de commerce de Nanterre, CEA (dissuasion, utilisateur des supercalculateurs), DG Trésor (IEF).
**Personnes** : Bertrand Meunier (président CA Atos 2022-2024), Nourdine Bihmane (ex-DG Atos), Philippe Salle (DG 2024-), Daniel Křetínský (EPEI).

## 8. MÉCANISMES / CHAÎNES CAUSALES

**M1 — Le démantèlement par la dette** : pertes massives (FCT-005) → sauvegarde accélérée (FCT-006) → contrôle par les créanciers (FCT-007) → ventes d'actifs pour apurer (FCT-008, FCT-012). Type : FINANCIER. Niveau : L2.
**M2 — Le rachat tardif par l'État (pattern « céder, perdre, racheter à perte » inversé)** : l'État laisse filer la valeur puis rachète l'actif souverain (Bull, 404 M€) après destruction de valeur ; les appels à Bpifrance (04/2024) précèdent le rachat de 2 ans. Type : STRUCTUREL. Niveau : L2.
**M3 — Le trou de contrôle** : l'IEF (seuil 10 %, décret 2026-718) arrive après les faits ; aucune procédure de blocage documentée sur les ventes intermédiaires ; les protections de l'État (action de préférence) sont postérieures à la crise. Type : PROCÉDURAL. Niveau : L2.

## 9. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Champion abandonné » | L'État a laissé Atos se faire démanteler faute de contrôle | Pertes et ventes en série (FCT-005 à 013) ; pas d'entrée de Bpifrance malgré les appels (FCT-009) | Le rachat final de Bull (FCT-012/013) ; les protections 11/2024 (FCT-010) ; le plan de sauvegarde a sauvé l'emploi partiellement | PARTIELLEMENT SOUTENU (abandon relatif, protection tardive) |
| S2 « Sauvetage souverain réussi » | L'État a finalement sanctuarisé les actifs critiques | Bull racheté 404 M€ (FCT-012/013), action de préférence (FCT-010) | Chronologie tardive (2024-2026) ; valeur détruite avant rachat ; 91 % aux créanciers (FCT-007) | PARTIELLEMENT SOUTENU (actifs critiques oui, groupe non) |
| S3 « Cession réussie à EPEI » | Le groupe tchèque a pris le contrôle d'Atos | Négociations exclusives 2023 (FCT-002/003) | Rupture le 28/02/2024 (FCT-004) ; aucune acquisition documentée | RÉFUTÉ |

**RESPONSIBILITY_MAP** : la responsabilité de la dérive financière relève de la gouvernance d'Atos (CA, direction) ; l'État a choisi une intervention tardive (action de préférence puis rachat Bull) ; les créanciers ont pris le contrôle dans le cadre du plan judiciaire. Aucune responsabilité pénale documentée. (BENEFIT != INTENT).

## 10. VERDICT 3 AXES

- **PÉNAL** : 0 fait pénal documenté.
- **INTÉGRITÉ** : GRAVEMENT CONTESTÉ — le démantèlement d'un champion stratégique (supercalculateurs de la dissuasion) s'est déroulé sans contrôle effectif de l'État pendant la phase de destruction de valeur ; l'intervention (404 M€) est postérieure aux pertes ; la « protection » par action de préférence (11/2024) est un dispositif tardif.
- **LÉGITIMITÉ** : CONTESTÉ — les appels du Sénat (04/2024) et le débat public n'ont pas été suivis d'une entrée de Bpifrance ; le rachat de Bull est présenté comme un succès alors que la valeur avait déjà été détruite.

## 11. PÉRIMÈTRE & LIMITES

**Inclusions** : scission, EPEI, restructuration, Worldgrid, Bull, rôle de l'État, cadre IEF. Période 2021-2026.

**Exclusions** : le détail des contrats publics d'Atos ; la gouvernance interne (hors faits saillants) ; les autres cessions du groupe.

**GAP déclarés** :
- GAP-001 (ACCESS) : montants des conseils et banques-conseils ; détail des « protections » de l'État (action de préférence) ; valorisations confidentielles.
- GAP-002 (CAUSALITY) : lien causal entre l'absence de contrôle de l'État et la destruction de valeur non démontré (la dérive est d'abord financière/industrielle).
- GAP-003 (SCOPE) : application réelle de l'IEF aux ventes intermédiaires (Worldgrid, Eviden) non documentée par source publique.

## 12. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : scission 06/2022 ; EPEI 01/08/2023 puis rupture 28/02/2024 ; pertes >3 Md€ (2023) ; dette ~4,8-5 Md€ ; sauvegarde 10/2024 finalisée 18/12/2024 (2,1 Md€ / 2,9 Md€ / 1,6 Md€ / 91 %) ; Worldgrid-ALTEN 270 M€ (12/2024) ; Bull-État 404 M€ (finalisé 31/03/2026) ; rapport Sénat 04/2024 ; décret 2026-718 (10 %).
- **PROBABLE (✧)** : protections de l'État 11/2024 (action de préférence) ; enjeu CEA/dissuasion.
- **HYPOTHÈSE (⁂)** : l'impact de la rumeur EPEI sur le cours ; l'effectivité des protections.
- **CONTESTÉ (⊗)** : « sauvetage réussi » vs « démantèlement » ; « Bull racheté à perte ».
- **INCONNU (⁅)** : montants de conseil ; détail des protections ; rôle précis de l'IEF sur chaque cession.

## 13. SUSPICION / VÉRIFICATION

- Les faits structurants (EPEI, sauvegarde, Worldgrid, Bull) sont confirmés par les communiqués officiels Atos/Bercy et la presse économique : fiables.
- FCT-010 (action de préférence, 11/2024) est rapporté par la presse sans communiqué officiel intégral lu : statut ✧, à confirmer.
- FCT-016 (usage CEA/dissuasion) est documenté par le rapport Sénat et Bercy : statut ✧.
