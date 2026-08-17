# INVESTIGATION APEX : LE PRÉJUDICE DE LA SURFACTURATION ET DU GONFLEMENT DES FACTURES DANS LA COMMANDE PUBLIQUE (GAP-003)

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260809-1408-surfacturation-commande-publique
PARENT_RUN_ID  : 20260809-1343-enrichissement-legalise-france (résolu au step 2 ; branche ciblée sur le GAP-003 du dossier parent)
AS_OF          : 2026-08-09
INPUT_KIND     : UPDATE (revalidation et approfondissement d'une branche de l'investigation parente)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique : « chiffrer le préjudice de la surfacturation et du gonflement des factures dans la commande publique : avenants, options, prestations fictives »)
SUBJECT_SLUG   : surfacturation-commande-publique
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_surfacturation-commande-publique/2026-08-09_14-08_surfacturation-commande-publique_INVESTIGATION.md
SCOPE          : préjudice de la surfacturation et du gonflement des factures dans la commande publique française : volets légal (avenants, options, gré à gré), semi-légal (prestations surévaluées) et pénal (fausses factures, prestations fictives) ; période 2016-2026 ; géographie : France
COMPLEXITY     : CX_SCORE=13 → $CX=APEX (political 2, technical 1, temporal 3, geo 2, narratives 3, data 2)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 18b
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE (rechargés, héritage du run parent)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« quel est le préjudice de la surfacturation et du gonflement des factures dans la commande publique française, et peut-on chiffrer la partie légale ? ») :

Le préjudice exact est **non mesuré par aucune institution française** : ni le Sénat (rapport n° 830, 2025), ni la DAJ/Bercy, ni les chambres régionales des comptes n'ont produit de chiffrage global de la surfacturation (FCT-023, FCT-025, constats d'absence). En revanche, le dossier établit quatre ordres de grandeur qui **encadrent** le champ :

1. **Le champ financier : 170 Md€ de contrats recensés en 2023 (contrats > 90 k€ HT), 400 Md€/an selon le périmètre de la Cour des comptes européenne** (FCT-001). Le gré à gré a doublé en dix ans (83 → 170 Md€).
2. **Le préjudice potentiel selon la littérature internationale : 8 % à 25 % des investissements publics gaspillés (OCDE/Fazekas 2022), 20 % à 25 % des montants engagés selon Anticor** (FCT-019, FCT-021). Appliquées au champ français, ces fourchettes donnent un ordre de grandeur de **14 à 100 Md€/an selon le périmètre retenu (170 vs 400 Md€)** : 13,6 à 42,5 Md€ sur la base de 170 Md€, 32 à 100 Md€ sur la base de 400 Md€ (FCT-026, calcul encadré, extrapolation et non mesure).
3. **La partie jugée et recouvrée : un échantillon infime** : plus gros cas récent documenté, 58 M€ (fraude Assurance Maladie, FCT-012) ; cas de surfacturation de soins : 900 k€ (FCT-013) ; AP-HP : 1,8 M€ (FCT-014) ; CHU de Nîmes : marchés > 35 M€ HT (FCT-015) ; affaires de fausses factures locales de 51 k€ à 280 k€ (FCT-016 à 018). Le ratio entre l'ordre de grandeur estimé et la partie documentée (quelques centaines de M€ par an) est de l'ordre de **200 à 1 600 fois** (FCT-026, division directe 14-100 Md€ / ~61 M€, indicatif).
4. **Les dérives de projets : structurelles et massives** : 9 projets publics sur 10 dépassent leur budget (Flyvbjerg, FCT-008) ; EPR Flamanville passé de 3,3 Md€ à 23,7 Md€ (FCT-009) ; Grand Paris Express de ~19-25 Md€ à 35-42 Md€ (FCT-010) ; JO 2024 relativement maîtrisés à 6,6 Md€ de dépenses publiques (FCT-011).

**Verdict sur le LEAD_QUESTION** (« la surfacturation est-elle chiffrable ? ») : **SOUTENU pour l'encadrement, NON PROUVÉ pour le chiffre unique**. La partie légale (avenants, options, gré à gré) n'est pas de la fraude : elle est **autorisée par le code** (seuils de 10 %/15 %/50 %, FCT-004) et n'est pas mesurée ; la partie pénale est réelle mais microscopique dans les registres judiciaires. Le « gonflement des factures » se situe donc sur un continuum légal → illégal dont aucune institution ne trace la frontière quantitative.

**Acteurs** : acheteurs publics (État, collectivités ~80 % des marchés), titulaires privés (BTP, conseil, santé), élus (perception d'un « risque pénal », Sénat 830), contrôleurs (AFA : 27 contrôles en 2024, ~17/an en moyenne, FCT-024 ; juridictions financières).

**Principales limites** : aucune mesure nationale ; les fourchettes 8-25 %/20-25 % sont des extrapolations d'études internationales et d'ONG, non des mesures françaises ; la décomposition légale/illégale est inférée, pas observée (GAP-001, GAP-002).

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **9/10** | La partie légale (avenants, options, gré à gré) est invisible : aucune institution ne publie la somme des avenants, leur volume total, ni leur répartition. Le Sénat n° 830 ne chiffre pas le préjudice (FCT-023). La DAJ ne calcule pas le coût de la non-qualité (FCT-025). |
| 2 | **€** money | 8/10 | Champ 170-400 Md€ (FCT-001), fourchettes 8-25 %/20-25 % (FCT-019/021), cas jugés (FCT-012 à 018), dérives projets (FCT-009/010). |
| 3 | **Λ** framing | 6/10 | Cadrages : « avenant » (technique, neutre) vs « dérive » (péjoratif) ; « gré à gré légal » vs « passoire » ; « prestation complémentaire » vs « surfacturation » ; le Sénat parle de « pilotage » là où la fraude parlerait de « détournement ». |
| 4 | **Ω** inversion | 7/10 | Le discours de la transparence (data.gouv, données essentielles obligatoires, FCT-005) cohabite avec un gré à gré qui double ; l'État « maîtrise » les coûts (JO 2024) pendant que l'EPR multiplie par 7 sa facture ; les seuils d'avenants (10/15/50 %) sont présentés comme des garde-fous alors qu'ils autorisent l'augmentation de prix sans mise en concurrence. |
| 5 | **Ψ** sidération | 2/10 | Champ froid : les dérives (EPR +20 Md€) ne produisent aucun moment de sidération durable. |
| 6 | **↕** verticalité | **8/10** | Asymétrie d'information structurelle : l'acheteur public sait moins que le titulaire sur le prix juste ; le gré à gré (170 Md€) supprime la concurrence ; la sanction frappe les exécutants (salariée d'EHPAD, anciennes salariées d'association) plus que les donneurs d'ordre. |
| 7 | **Φ** spectacle | 3/10 | Peu de spectacle : les affaires médiatisées (Bygmalion) absorbent l'attention, le volume diffus des avenants reste hors champ. |
| 8 | **Σ** sémiotique | 3/10 | Signaux faibles : « maîtrise des coûts », « sobriété budgétaire » comme marqueurs. |
| 9 | **Κ** cynisme | **8/10** | Discours de maîtrise (Sénat : 67 recommandations, FCT-023) sans chiffrage ni sanction ; les seuils d'avenants autorisent ce que le discours dénonce ; le contrôle (27 dossiers AFA/an pour ~400 Md€, FCT-024) est un « scanner sans bras ». |
| 10 | **ρ** résistance | 6/10 | Cour des comptes (EPR, JO), Sénat (n° 578, 830), chambres régionales (Flamboyants), AFA (signalements ×1,9 depuis 2019), TF1 Vérif (démontage du 120 Md€), presse locale (cas EHPAD, association). |
| 11 | **κ** influence subtile | 7/10 | Architecture par défaut : avenants faciles (seuils), options publiées d'emblée, gré à gré dominant (170 Md€) ; la « prestation complémentaire » est le chemin le moins frictionnel vers l'augmentation de prix. |
| 12 | **⫸** convergence | 7/10 | Convergence sans mesure : OCDE (8-25 %), Anticor (20-25 %), Flyvbjerg (9/10 en dérive), cas locaux répétés : tous pointent vers un préjudice réel massif, sans qu'aucune institution française ne le chiffre. |
| 13 | **⚔** guerre cognitive | 1/10 | Aucune opération organisée documentée sur ce champ. |
| 14 | **🌐** réseau | 7/10 | Nœuds : acheteurs publics, grands groupes du BTP, cabinets de conseil (McKinsey 18 M€ sur la crise sanitaire), cliniques privées, élus ; rotations et interconnexions documentées cas par cas (AP-HP : ex-associé d'EI-Technologies recruté, FCT-014). |
| 15 | **⏰** temporalité | 7/10 | Chronologie : 2016 RAND, 2019 données essentielles, 2021 conseil >1 Md€, 2022 Sénat 578 + CRC Flamboyants, 2023 170 Md€ gré à gré, 2024 condamnations (Nîmes, Saint-Maur), 2025 Sénat 830 + EPR 23,7 Md€ + JO 6,6 Md€, 2026 CPAM 58 M€. |

**BIAS TEST (15/15 scorés).** Aucun symbole au-delà de 9. Les champs 7-9 signalent des zones où la preuve est partielle (pas de mesure, cas dispersés) : à traiter en PÉRIMÈTRE & LIMITES.

**PATTERNS** : @PAT[ICEBERG] (Ξ=9), @PAT[MONEY] (€=8), @PAT[CYN] (Κ=8), @PAT[TEMP] (⏰=7), @PAT[NET] (🌐=7). **THREATS** : @THR[REG_CAPTURE] (gré à gré, rotations), @THR[DARK_MONEY] (flux opaques, partiellement contré : les avenants sont publiés dans les données essentielles), @THR[NUDGE] (avenants/options par défaut).

**RHETORICAL** : NUM (chiffres officiels + fourchettes d'ONG, tous étiquetés) ; AUTH (CdC, Sénat, OCDE) ; DEM et BF = 0.

## 3. CLUSTERS (routage SYMBOLS §4)

| Cluster | Diagnostic | Gap |
|---------|------------|-----|
| ICEBERG (Ξ=9) | Émergé : cas jugés (58 M€, 0,9 M€, 1,8 M€) et dérives de projets. Immergé : masse des avenants, options, gré à gré (170 Md€). | Aucune mesure de la partie immergée. |
| MONEY (€=8) | Flux : contribuable → collectivité → titulaire, augmenté par avenants ; → cliniques (santé) ; → conseil. | Bénéficiaires nominatifs non publiés. |
| POWER (↕=8) | Asymétrie d'information acheteur/titulaire ; gré à gré sans concurrence. | Pas de mesure du surcoût du gré à gré vs mise en concurrence. |
| INVERSION (Ω=7, Κ=8) | Transparence affichée vs gré à gré doublé ; maîtrise affichée vs EPR ×7. | — |
| CONFIRMATION (κ=7) | Avenants et options par défaut ; gré à gré dominant. | Pas de taux d'option mesuré. |
| FRAGMENTATION (⫸=7) | OCDE + Anticor + Flyvbjerg + cas locaux convergent sans mesure française. | Pas d'explication alternative unifiée. |
| NETWORK (🌐=7) | Acheteurs, BTP, conseil, santé, élus. | Pas de graphe. |
| TEMPORAL (⏰=7) | 2016-2026 : réformes de transparence sans inflexion des dérives. | — |
| RESISTANCE (ρ=6) | CdC, Sénat, CRC, AFA, TF1 Vérif. | — |

## 4. HERMÉNEUTIQUE (statut : ANALYSE)

- **L1 (texte) :** registres officiels (Sénat n° 830, CdC, CRC, AFA, OCDE) + cas judiciaires + littérature académique (Flyvbjerg).
- **L2 (structure) :** trois strates : (a) le légal (avenants, options, gré à gré), (b) le semi-légal (prestations surévaluées, HSM fictifs facturés le week-end, FCT-013), (c) le pénal (fausses factures, soins fictifs, FCT-012/016/017/018).
- **L3 (intérêt) :** le préjudice n'est pas mesuré parce que la plupart des canaux sont légaux et publiés (les données essentielles existent depuis 2019, FCT-005) : la masse des avenants est dans les données publiques, mais personne ne l'agrège.
- **L4 (sémiotique) :** le « risque pénal » perçu par les élus (Sénat 830) est le miroir du « risque budgétaire » jamais chiffré.
- **L5 (comparaison) :** contraste avec le corpus parent : les niches (91,83 Md€) sont chiffrées au centime près, la surfacturation (14-100 Md€ potentiels) n'est pas chiffrée du tout : la mesure suit l'objet (budget) et non le préjudice.
- **L6 (contexte) :** débat budgétaire 2024-2026 (réduction des dépenses, revue des dépenses publiques) où le Sénat propose un « pilotage » sans chiffrage.

**Lecture concurrente** : les avenants sont une pratique normale de gestion (aléas de chantier, circonstances imprévues) ; les fourchettes 8-25 % sont des extrapolations non spécifiques à la France. La synthèse retenue : le préjudice est réel, distribué sur un continuum légal→illégal, et l'absence de mesure est elle-même un fait d'enquête (Ξ=9).

## 5. FORENSIC REASONING (ICEBERG MAX)

**Émergé (mesuré, jugé)** : CPAM 58 M€ (FCT-012) ; Flamboyants 900 k€ (FCT-013) ; AP-HP 1,8 M€ (FCT-014) ; Nîmes >35 M€ HT (FCT-015) ; Saint-Maur 280 k€ (FCT-016) ; EHPAD Saint-Berthevin (FCT-017) ; association Réunion 51 k€ (FCT-018).

**Surface (mesuré, non attribué)** : EPR +20,4 Md€ (FCT-009) ; Grand Paris +15-20 Md€ (FCT-010) ; JO 6,6 Md€ (FCT-011) ; dérive 9/10 des méga-projets (FCT-008) ; OCDE 8-25 % (FCT-019) ; EPRS 29,6 Md€ UE 2016-2021 (FCT-020) ; Anticor 20-25 % (FCT-021) ; RAND 116-135 / 8-18 Md€ (FCT-022).

**Immergé (inféré)** : masse annuelle des avenants et options (non agrégée) ; surcoût du gré à gré vs concurrence (non mesuré) ; préjudice de la « non-qualité » (FCT-025, déclaré non chiffré) ; part légale vs illégale du gonflement des factures (frontière inférée).

**ICEBERG LOAD :** 8 strates émergées confirmées, 8 en surface, 4 inférées. Le contraste entre les registres judiciaires (minuscules) et les registres budgétaires (massifs, non analysés) est la signature du champ : la donnée existe, l'analyse n'existe pas.

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « La commande publique est encadrée et transparente » : code de la commande publique, seuils d'avenants, données essentielles obligatoires, AFA, Sénat.
- **Antithèse (critique) :** « La commande publique est une passoire à surfacturation » : gré à gré doublé à 170 Md€, avenants jusqu'à 50 %, contrôle microscopique, préjudice jamais chiffré.
- **Arbitrage par les preuves :** la thèse est confirmée sur la forme (les règles existent, la publication existe depuis 2019) ; l'antithèse est confirmée sur le fond (9/10 projets en dérive, EPR ×7, fourchettes 8-25 %, cas pénaux réels mais microscopiques). **La synthèse** : le système est réglementairement dense et statistiquement aveugle : les canaux d'augmentation de prix sont légaux et publiés, le préjudice est réel et non mesuré, la sanction est rare et concentrée sur les exécutants.

**Réfutation testée** : « le gré à gré est vertueux car rapide » est démenti par le Sénat 830 (67 recommandations de pilotage) ; « la fraude est marginale » est démenti par les cas convergents (58 M€, 0,9 M€, 1,8 M€, 35 M€) et par la convergence internationale (8-25 %). La synthèse tient.

## 7. CHRONOLOGIE

| Année | Événement | Source | Statut |
|-------|-----------|--------|--------|
| 2007 | Lancement EPR Flamanville à 3,3 Md€ | CdC | ✦ |
| 2016 | RAND Europe : corruption UE 990 Md€, France 116-135 Md€ (max) / 8-18 Md€ (plausible) | RAND/TF1 Vérif | ✦ |
| 2019 | Obligation de publication des données essentielles de la commande publique (arrêté 22/03/2019) | Légifrance | ✦ |
| 2019 | CRC AP-HP : commandes suspectes 1,8 M€ (projet SIP) | CRC/Le Parisien (parent FCT-104) | ✦ |
| 2021 | Conseil à l'État >1 Md€ (893,9 M€ ministères) ; McKinsey 18 M€ crise sanitaire | Sénat n° 578 / TF1 Vérif | ✦ |
| 2022 | CRC Réunion : groupe Les Flamboyants, surfacturations 900 k€ (04/10) | La 1ère | ✦ |
| 2023 | Gré à gré 170 Md€ (vs 83 en 2014) ; EHPAD Saint-Berthevin : fausses factures (03/11) | Sénat 830, TC Laval | ✦ |
| 2024 | CHU Nîmes : N. Best condamné pour favoritisme (25/11) ; Saint-Maur/Bygmalion : 226 k€ (27/02) ; AFA 435 signalements ; association Réunion 51 k€ (01/11) | presse, tribunaux, AFA | ✦ |
| 2025 | Sénat n° 830 (08/07) : 170/83/400 Md€, 67 recommandations, sans chiffrage du préjudice ; EPR 23,7 Md€ (CdC 14/01) ; JO 2024 : 6,6 Md€ (CdC 29/09) | Sénat, CdC | ✦ |
| 2026 | Fraude CPAM 58 M€, 7 mises en examen (26/03) ; OCDE : 8-25 % des investissements publics gaspillés (24/03) | Franceinfo, OCDE | ✦ |

## 8. DOMAINES (par axe)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 MÉCANISMES-LÉGAUX | Comment le droit permet-il d'augmenter les prix ? | Seuils d'avenants 10/15/50 % ; options ; données essentielles publiées mais non agrégées | FCT-004 à 007 | SATURATED |
| AXS-002 SURCOÛTS-PROJETS | Quelle est l'ampleur des dérives ? | 9/10 en dérive ; EPR ×7 ; Grand Paris +15-20 Md€ ; JO maîtrisé | FCT-008 à 011 | SATURATED |
| AXS-003 CAS-JUGÉS | Que documente la justice ? | CPAM 58 M€, Flamboyants 0,9 M€, AP-HP 1,8 M€, Nîmes 35 M€, fausses factures locales | FCT-012 à 018 | SATURATED |
| AXS-004 CHIFFRAGES | Quelles estimations existent ? | OCDE 8-25 %, Anticor 20-25 %, EPRS 29,6 Md€ UE, RAND ; Sénat 830 et DAJ : aucun chiffrage | FCT-019 à 025 | SATURATED |
| AXS-005 ENCADREMENT | Que vaut un chiffrage encadré ? | 14-100 Md€/an selon la fourchette appliquée ; ratio préjudice potentiel/jugé 100-1000x | FCT-026 | ANALYSE (extrapolation) |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| Acheteurs publics (État, collectivités) | Donneurs d'ordre | ~80 % des marchés (collectivités) ; avenants et options activés | FCT-003/004 | ROLE |
| Titulaires privés (BTP, conseil, santé) | Bénéficiaires | Prestations complémentaires, HSM fictifs, marchés >35 M€ | FCT-013/015 | Bénéfice ≠ intention |
| Élus locaux | Décideurs | Perception d'un « risque pénal » (Sénat 830) | FCT-023 | ROLE |
| Juridictions financières (CdC, CRC) | Contrôle | EPR 23,7 Md€ ; JO 6,6 Md€ ; Flamboyants 0,9 Md€... | FCT-009/011/013 | ρ |
| AFA | Anticorruption | 27 contrôles en 2024 (~17/an depuis 2018) ; signalements 229→435 | FCT-024 | ρ |
| Justice pénale | Sanction | CPAM 58 M€ ; Nîmes ; Saint-Maur | FCT-012/015/016 | Sanction exécutants |
| Cabinets de conseil | Interface | McKinsey 18 M€ crise sanitaire ; 893,9 M€ conseil ministères 2021 | FCT-027 | ROLE |

**CONTROL_MAP** :

| Contrôleur | Mécanisme | Résultat | Gap |
|------------|-----------|----------|-----|
| CTRL-001 AFA | Contrôles ciblés | 27 contrôles en 2024 (~17/an depuis 2018) pour ~400 Md€ | 1 contrôle pour ~15 Md€ |
| CTRL-002 Données essentielles | Publication obligatoire | Données publiées depuis 2019 | Aucune analyse agrégée des avenants |
| CTRL-003 Juridictions financières | Contrôle a posteriori | Cas documentés au cas par cas | Aucune agrégation nationale |
| CTRL-004 Justice pénale | Poursuites | Cas 58 M€ et locaux | Part jugée infime vs fourchettes |

## 10. CHAÎNES / PELOTE (causalité)

**CAU-001 : Le droit autorise l'augmentation de prix sans nouvelle concurrence.**
Étage 1 : avenants de plein droit jusqu'à 10 % (fournitures/services) et 15 % (travaux), jusqu'à 50 % pour prestations indispensables (FCT-004). Étage 2 : ces seuils sont légaux et publiés (FCT-005). Étage 3 : l'activation massive d'avenants est donc un vecteur de surcoût sans fraude et sans contrôle spécifique. Type : STRUCTUREL. Confidence : high.

**CAU-002 : Le gré à gré supprime le prix de référence.**
Étage 1 : gré à gré 170 Md€ en 2023, doublé en 10 ans (FCT-001). Étage 2 : sans mise en concurrence, le « prix juste » n'existe pas de référence. Étage 3 : la surfacturation devient indétectable en l'absence de comparaison. Type : MÉCANISME. Confidence : high sur le fait, la capture est inférée (pas de mesure du surcoût du gré à gré).

**CAU-003 : Le sous-contrôle rend la détection aléatoire.**
Étage 1 : 27 contrôles AFA en 2024 (~17/an en moyenne depuis 2018) pour ~400 Md€ (FCT-024). Étage 2 : les cas détectés (58 M€, 0,9 M€, 1,8 M€) sont rares et dispersés (FCT-012/013/014). Étage 3 : la partie jugée (quelques centaines de M€/an) est un échantillon, pas une carte. Type : SYSTÈME. Confidence : high.

**CAU-004 : Les grands projets dérivent structurellement (lock-in + avenants).**
Étage 1 : 9/10 méga-projets en dérive (Flyvbjerg, FCT-008). Étage 2 : EPR ×7 (FCT-009), Grand Paris +15-20 Md€ (FCT-010). Étage 3 : l'irréversibilité technique et les avenants transforment la dérive en fatalité. Type : MÉCANISME. Confidence : high (études internationales + cas français).

**CAU-005 : L'absence de mesure empêche toute réforme ciblée.**
Étage 1 : Sénat 830 : 67 recommandations, zéro chiffrage (FCT-023) ; DAJ : non-qualité non chiffrée (FCT-025). Étage 2 : sans chiffre, le débat public traite le sujet qualitativement. Étage 3 : les réformes (données essentielles, AFA) améliorent la transparence sans mesurer l'effet. Type : SYSTÈME. Confidence : high sur les constats.

**CAU-006 (rejetée) : « la surfacturation est un complot organisé des entreprises ».** Réfutée : aucun faisceau de coordination n'est documenté ; les cas sont dispersés et souvent opportunistes (salariée d'EHPAD, association). Le bénéfice n'implique pas l'intention.

## 11. CARTE DES PREUVES

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « Le préjudice de la surfacturation n'est mesuré par aucune institution française » | Sénat 830 (pas de chiffrage), DAJ (non-qualité non chiffrée), CRC (pas d'agrégation) | Les données essentielles existent et sont publiques | SOUTENU |
| CLM-002 | « La partie pénalisée est un échantillon infime » | Cas 58 M€/0,9 M€/1,8 M€ vs fourchettes 14-100 Md€ | La « dark figure » pénale est inconnue des deux côtés | SOUTENU |
| CLM-003 | « Avenants et options sont le vecteur légal d'augmentation des prix » | Seuils 10/15/50 %, EPR, Grand Paris | Les avenants couvrent aussi des aléas réels | SOUTENU |
| CLM-004 | « Les grands projets publics dérivent systématiquement » | Flyvbjerg 9/10, EPR ×7 | JO 2024 maîtrisé (6,6 Md€) | SOUTENU (majorité, pas universalité) |
| CLM-005 | « Le préjudice potentiel est de 14-100 Md€/an » | OCDE 8-25 % et Anticor 20-25 % appliqués à 170-400 Md€ | Extrapolations internationales/ONG, non mesures françaises | ANALYSE encadrée, NON une mesure |
| CLM-006 | « Le contrôle est sous-proportionné » | 27 contrôles AFA en 2024 (~17/an depuis 2018) pour ~400 Md€ | L'AFA cible les risques, pas le volume | SOUTENU |

### FACT_REGISTRY (26 faits)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | Commande publique : 170 Md€ (2023, >90 k€ HT) vs 83 Md€ (2014) ; 400 Md€ (14 % PIB, CdC européenne) | 170/83/400 Md€ | SRC-01 Sénat n° 830 (citation exacte) | ✦ |
| FCT-002 | OECP/DAJ : 233,2 Md€ de commande publique recensés en 2024 | 233,2 Md€ | SRC-02 DAJ RA 2024 | ✧ |
| FCT-003 | Collectivités territoriales : ~80 % des marchés (2023) | 80 % | SRC-01 | ✦ |
| FCT-004 | Avenants de plein droit : <10 % (fournitures/services), <15 % (travaux) ; jusqu'à 50 % prestations indispensables ; au-delà : circonstances imprévues | 10/15/50 % | SRC-03 CCP L2194/R2194 | ✦ |
| FCT-005 | Publication obligatoire des modifications (avenants) via données essentielles depuis 2019 (décret 2022-767) | 2019 | SRC-04 Légifrance | ✦ |
| FCT-006 | Options/tranches : montant total évalué et publié dans l'AAPC ; activation = majoration de l'engagement sans avenant | — | SRC-03 | ✦ |
| FCT-007 | Jurisprudence : modification substantielle = nouvelle mise en concurrence requise (sinon illégalité) | — | SRC-05 Conseil d'État | ✦ |
| FCT-008 | Flyvbjerg : 9/10 méga-projets en dérive ; surcoût moyen rail +44,7 %, routes ~+20 % | 90 %, 44,7 % | SRC-06 Cato/Flyvbjerg | ✦ |
| FCT-009 | EPR Flamanville : 3,3 Md€ (2007) → 23,7 Md€ (€2023, intérêts intercalaires inclus, CdC 14/01/2025), ×7 ; l'estimation EDF (~13,2 Md€ en €2015, hors coûts financiers) diffère par périmètre, cf. CONTR-004 | +20,4 Md€ | SRC-07 CdC 14/01/2025 (Le Monde) | ✦ |
| FCT-010 | Grand Paris Express : ~19-25 Md€ initial → 35-42 Md€ | +15-20 Md€ | SRC-08 Vie-publique/Sénat | ✧ |
| FCT-011 | JO Paris 2024 : 6,6 Md€ de dépenses publiques (3,02 organisation + 3,63 infrastructures SOLIDEO) | 6,6 Md€ | SRC-09 CdC 29/09/2025 | ✦ |
| FCT-012 | Fraude CPAM 58 M€ (26/03/2026) : 18 centres de santé, soins fictifs, patients fantômes, 7 mises en examen | 58 M€ | SRC-10 Franceinfo (parent FCT-035) | ✦ |
| FCT-013 | Groupe Les Flamboyants (Réunion) : 900 k€ de surfacturations de soins psychiatriques (HSM fictifs facturés les week-ends), CRC 04/10/2022 | 900 k€ | SRC-11 La 1ère | ✦ |
| FCT-014 | AP-HP : 1,8 M€ de commandes suspectes (projet SIP), favoritisme et conflits d'intérêts, CRC 2019 | 1,8 M€ | SRC-12 Le Parisien (parent FCT-104) | ✦ |
| FCT-015 | CHU de Nîmes : N. Best condamné 25/11/2024 pour favoritisme (marchés Bouygues >35 M€ HT) | >35 M€ HT | SRC-13 Midi Libre (parent FCT-105) | ✦ |
| FCT-016 | Saint-Maur-des-Fossés/Bygmalion : ~280 k€ de factures douteuses (60 factures), 226 k€ dommages, CA Paris 27/02/2024 | 280 k€ | SRC-14 Le Figaro | ✦ |
| FCT-017 | EHPAD Saint-Berthevin : fausses factures et faux bulletins, 15 mois sursis probatoire (TC Laval 03/11/2023) | — | SRC-15 Courrier de la Mayenne | ✦ |
| FCT-018 | Association d'insertion (Réunion) : 51 k€ détournés via factures falsifiées, TC Saint-Pierre 01/11/2024 | 51 k€ | SRC-16 Zinfos974 | ✦ |
| FCT-019 | OCDE 2026 : 8-25 % des investissements publics mondiaux gaspillés (Fazekas et al. 2022) ; marchés publics 13-15 % du PIB | 8-25 % | SRC-17 OCDE 24/03/2026 | ✦ |
| FCT-020 | EPRS : 29,6 Md€ de coût du risque de corruption dans les marchés publics UE 2016-2021 | 29,6 Md€ | SRC-17 (OCDE citant EPRS) | ✧ |
| FCT-021 | Anticor : déperdition de 20-25 % des montants engagés par fraude marchés publics (littérature experte ancienne) | 20-25 % | SRC-18 Anticor/CdC 12/2025 | ✧ |
| FCT-022 | RAND 2016 : France 116-135 Md€ (scénario max) / 8-18 Md€ (plausible) ; pas de ventilation marchés publics | 116-135 / 8-18 Md€ | SRC-19 TF1 Vérif 02/10/2024 | ✦ |
| FCT-023 | Sénat n° 830 (08/07/2025) : 67 recommandations, aucun chiffrage monétaire du préjudice de la surfacturation | 0 chiffrage | SRC-01 | ✦ (constat) |
| FCT-024 | AFA : signalements 229 (2019) → 435 (2024) ; 18 nouveaux contrôles engagés (RA 2025) ; 27 contrôles en 2024 (cumul 101 depuis 2018, soit ~17/an en moyenne, parent FCT-036) | 229→435 | SRC-20 AFA RA 2025 | ✦ |
| FCT-025 | DAJ/Bercy : coût de la non-qualité dans la commande publique : non chiffré (constat d'absence) | NON CHIFFRÉ | SRC-02 | ✦ (constat) |
| FCT-027 | Conseil à l'État 2021 : >1 Md€ (893,9 M€ pour les seuls ministères) ; McKinsey : ~18 M€ de contrats cumulés (crise sanitaire et réformes), à ne pas confondre avec le total du conseil d'État | 893,9 M€ / 18 M€ | SRC-19 TF1 Vérif (correction de la confusion « 900 M€ ») ; SRC-01 (parent FCT-034) | ✦ |
| FCT-026 | Calcul encadré : 8-25 % × 170 Md€ = 13,6-42,5 Md€/an ; × 400 Md€ = 32-100 Md€/an ; Anticor 20-25 % × 170 = 34-42,5 Md€/an ; ratio préjudice potentiel/jugé ≈ 100-1000x | 14-100 Md€/an | calcul annexe (SRC-17/18/01), étiquette « 14-100 Md€ » = union arrondie de deux périmètres (170 vs 400 Md€) ; tension avec RAND plausible (8-18 Md€ de corruption totale) signalée en CONTR-004 | ⁂ extrapolation |

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | McKinsey : « 900 M€ » vs « 1 Md€ » de contrats | TF1 Vérif : 893,9 M€ = conseil total ministères 2021 ; McKinsey (crise sanitaire) = ~18 M€ cumulés ; les deux chiffres cohabitent avec des périmètres distincts | RÉSOLUE |
| CONTR-002 | Fourchettes du préjudice : 8-25 % (OCDE) vs 20-25 % (Anticor) vs 8-18 Md€ (RAND plausible) | Périmètres différents (gaspillage/investissements vs fraude/marchés vs corruption totale) ; on cite chaque fourchette avec son périmètre, aucune n'est une mesure française | DOCUMENTÉE (non unifiée) |
| CONTR-003 | JO 2024 : « maîtrise » (6,6 Md€) vs dérives générales | Le cas JO est un contre-exemple relatif (infrastructures maîtrisées), il borne la thèse « 9/10 en dérive » sans la réfuter | RÉSOLUE |
| CONTR-004 | EPR : 23,7 Md€ (CdC, €2023, coûts financiers inclus) vs ~13,2 Md€ (EDF, €2015, hors coûts financiers) | Écart de périmètre (devises, intérêts intercalaires), pas une contradiction ; les deux sont cités avec leur périmètre (FCT-009) ; la fourchette « 14-100 Md€ » (marchés publics, extrapolation) chevauche le RAND « plausible » de corruption totale (8-18 Md€) : signal de fragilité méthodologique, jamais présenté comme mesure | DOCUMENTÉE |

### EDI

```
geo:0.80 lang:0.80 strat:0.80 owner:0.75 persp:0.80 temp:0.80
EDI_raw = .25×.80 + .20×.80 + .20×.80 + .15×.75 + .15×.80 + .05×.80 = 0.7925
Pénalité : MISSING_COUNTER (-.10) : perspective des titulaires/entreprises (défense de la pratique des avenants) absente.
EDI = 0.69 (BROAD, sous la cible APEX 0.80, écart déclaré)
COV = 0.85 | IND = 0.55 (11 familles amont / 20 sources) | CC = 3/3
EDI* = .5×.69 + .3×.85 + .2×.55 = 0.71
Perspectives : ⟐ 4 | ⟐̅ 3 | 🌍 2 (CRC Réunion) | 🎓 2 (Flyvbjerg, Fazekas) | 🔥 1 (Anticor)
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait)

| FCT | QRY | SRC | URL (référence) | Statut |
|-----|-----|-----|-----------------|--------|
| FCT-001/023 | QRY-001/QRY-004 | SRC-01 | senat.fr r24-830-1 | ✦ |
| FCT-004 | QRY-001 | SRC-03 | legifrance.gouv.fr CCP L2194 | ✦ |
| FCT-009 | QRY-002 | SRC-07 | lemonde.fr 14/01/2025 | ✦ |
| FCT-011 | QRY-002 | SRC-09 | tf1info.fr + ccomptes.fr 29/09/2025 | ✦ |
| FCT-019/020 | QRY-004 | SRC-17 | oecd.org (Perspectives intégrité 2026) | ✦ |
| FCT-022 | QRY-004 | SRC-19 | tf1info.fr 02/10/2024 | ✦ |
| FCT-013 | QRY-003 | SRC-11 | la1ere.franceinfo.fr 04/10/2022 | ✦ |
| FCT-016 | QRY-003 | SRC-14 | lefigaro.fr 27/02/2024 | ✦ |
| FCT-024 | QRY-003 | SRC-20 | agence-francaise-anticorruption.gouv.fr RA 2025 | ✦ |

## 12. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Passoire légale » | Avenants + gré à gré + sous-contrôle = fuite massive non mesurée | FCT-001/004/019/024 | Les avenants couvrent des aléas réels ; aucune mesure française | Retenue (structure) |
| S2 « Aléas de gestion » | Les surcoûts sont des aléas techniques (EPR = technologie nouvelle) | FCT-009/010 | Flyvbjerg : la dérive est la règle, pas l'exception (9/10) | Partiellement valide |
| S3 « Mesure manquante » | Le préjudice existe mais n'est pas chiffrable avec les outils actuels | FCT-023/025 | Les données essentielles permettent une analyse qui n'est pas faite | Retenue (la donnée existe, l'analyse non) |

**IMPACT_MAP** :

| Acteur | Gain | Perte |
|--------|------|-------|
| Titulaires privés (BTP, santé, conseil) | Avenants, prestations complémentaires, gré à gré | Peu de pertes mesurées |
| Acheteurs publics | — | Surcoûts (EPR +20 Md€, Grand Paris +15-20 Md€), service public dégradé |
| Contribuables | — | Fourchettes 14-100 Md€/an (potentiel), dette |
| Élus | Procédures accélérées (gré à gré) | « Risque pénal » perçu (Sénat 830) |
| Justice/AFA | Cas documentés (58 M€) | Sanction concentrée sur les exécutants |

**RESPONSIBILITY_MAP** : aucun auteur d'intention n'est établi (BENEFIT != INTENT). Rôles documentés : acheteurs (activation des avenants), titulaires (facturation), contrôleurs (sous-dotation), législateur (seuils). La responsabilité systémique (RÉSULTAT) est celle d'un système où la donnée publique existe (données essentielles) et n'est pas analysée : c'est une omission d'exploitation, pas une fraude.

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : surfacturation et gonflement des factures dans la commande publique française : avenants, options, gré à gré, prestations fictives, fausses factures, surcoûts de projets. Période 2016-2026. Sources officielles et judiciaires.

**Exclusions explicites** : la fraude sociale dans son ensemble (sauf cas de facturation de soins, FCT-012/013, qui relèvent du mécanisme) ; la fraude fiscale ; les cas nominatifs non jugés ; la commande publique européenne hors UE.

**GAP déclarés** :
- GAP-001 (ACCESS) : volume annuel des avenants et options (montants) non agrégé par aucune institution. **CONFIRMÉ ET ÉTENDU 09/08/2026 22:33** : dossier `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_avenants-5-grands-projets/2026-08-09_22-33_avenants-5-grands-projets_INVESTIGATION.md` — aucun des 5 plus grands projets (EPR, GPE, JO, Seine-Nord, Hôpital GP) ne publie son agrégat d'avenants ; les données essentielles (2019) les contiennent sans agrégation. Mécanisme confirmé (seuils 10/15/50 %), chiffre de la part légale impossible par sources publiques ; JO = seul projet maîtrisé (supervision stricte, CdC 2025, Sénat 748).
- GAP-002 (METHOD) : décomposition légale/illégale du gonflement des factures non mesurable ; frontière inférée.
- GAP-003 (METHOD) : les fourchettes 8-25 %/20-25 % sont des extrapolations internationales/ONG, pas des mesures françaises ; FCT-026 est une ANALYSE encadrée, pas un fait.
- GAP-004 (ACCESS) : le surcoût du gré à gré vs mise en concurrence n'est mesuré nulle part.
- GAP-005 (CORPUS) : perspective des titulaires privés absente (MISSING_COUNTER, EDI).
- GAP-006 (ACCESS) : aucune série chronologique du préjudice ; les « 12 ans » de l'EPR et les 67 recommandations du Sénat restent sans chiffrage.

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : champ 170-400 Md€ ; gré à gré doublé ; seuils d'avenants 10/15/50 % ; EPR ×7 (23,7 Md€) ; JO 6,6 Md€ ; cas CPAM 58 M€, Flamboyants 0,9 M€, AP-HP 1,8 M€, Nîmes >35 M€, fausses factures locales ; AFA 229→435 signalements ; Sénat 830 sans chiffrage ; DAJ : non-qualité non chiffrée.
- **PROBABLE (✧)** : Grand Paris 35-42 Md€ ; 233,2 Md€ recensés 2024 ; Anticor 20-25 % ; EPRS 29,6 Md€ UE.
- **HYPOTHÈSE (⁂)** : fourchettes 14-100 Md€/an appliquées au champ français (FCT-026) ; ratio préjudice potentiel/jugé 100-1000x ; capture du gré à gré.
- **CONTESTÉ (⊗)** : périmètre des chiffres McKinsey (CONTR-001) ; unification des fourchettes (CONTR-002).
- **INCONNU (⁅)** : masse des avenants ; surcoût du gré à gré ; part légale/illégale ; dark figure pénale.
- **RÉFUTÉ (❧)** : « la surfacturation est un complot organisé » (aucun faisceau de coordination).

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD** : input TOPIC/UPDATE (branché sur GAP-003 du parent). Le verdict d'objet est distinct du verdict de lead : la question « peut-on chiffrer ? » reçoit une réponse honnête en deux volets (encadrement possible, chiffre unique non).

**Vérifications contradictoires exécutées** : CONTR-001 (McKinsey résolu par TF1 Vérif) ; CONTR-002 (fourchettes documentées avec périmètres distincts, aucune unifiée) ; CONTR-003 (JO comme contre-exemple partiel). Faits du parent revalidés par sources fraîches (CPAM, gré à gré, AP-HP, Nîmes via rapports et presse).

**Verdict final : PRÉSUMPTION FORTE sur l'encadrement (le préjudice est réel, massif, non mesuré), NON PROUVÉ sur le chiffre unique.** La partie légale (avenants, options, gré à gré) est le canal dominant et le moins contrôlé ; la partie pénale est réelle mais microscopique dans les registres ; aucune institution ne chiffre l'ensemble. Le GAP-003 du parent est **partiellement résolu** : encadré (14-100 Md€/an potentiels) mais non mesuré.

---

# ANNEXE A. SOURCES

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | Sénat, commission d'enquête n° 830 « Piloter la commande publique au service de la souveraineté économique » | 08/07/2025 | ◈ | https://www.senat.fr/rap/r24-830-1/r24-830-10.html |
| SRC-02 | DAJ/Bercy, rapport d'activité 2024 (OECP) | 2025 | ◈ | https://www.economie.gouv.fr/files/files/directions_services/daj/publications/rapports-activite-daj/2024/RA2024_compressed.pdf |
| SRC-03 | Code de la commande publique, articles L2194-1 à L2194-3 et R2194-5 à R2194-9 | 2019-2026 | ◈ | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000037701019/LEGISCTA000037725131/2019-10-27 |
| SRC-04 | Arrêté du 22/03/2019 + décret n° 2022-767 (données essentielles de la commande publique) | 2019/2022 | ◈ | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038318675 |
| SRC-05 | Conseil d'État, jurisprudence « modification substantielle » | constant | ◈ | https://www.conseil-etat.fr |
| SRC-06 | Flyvbjerg / Cato Institute, « Megaprojects: Over Budget, Over Time, Over and Over » | 01-02/2017 | 🎓 | https://www.cato.org/policy-report/january/february-2017/megaprojects-over-budget-over-time-over-over |
| SRC-07 | Cour des comptes (EPR) relayée par Le Monde | 14/01/2025 | ◈ | https://www.lemonde.fr/economie/article/2025/01/14/epr-de-flamanville-la-cour-des-comptes-estime-le-cout-total-a-23-7-milliards-d-euros_6497010_3234.html |
| SRC-08 | Vie-publique + Sénat PLF : Grand Paris Express | 2020-2023 | ◈ | https://www.vie-publique.fr/en-bref/277104-grand-paris-express-augmentation-des-couts |
| SRC-09 | Cour des comptes, JO Paris 2024 (rapport global) | 29/09/2025 | ◈ | https://www.tf1info.fr/jeux-olympiques/jo-paris-2024-ce-que-dit-le-rapport-de-la-cour-des-comptes-sur-le-budget-des-jeux-olympiques-2397479.html |
| SRC-10 | Franceinfo, fraude CPAM 58 M€ | 26/03/2026 | ◈ | https://www.franceinfo.fr/economie/fraude/sept-personnes-mises-en-examen-dans-une-affaire-hors-norme-de-fraudes-a-l-assurance-maladie-pour-un-montant-estime-a-58-millions-d-euros_7896257.html |
| SRC-11 | La 1ère France Info, CRC Réunion, groupe Les Flamboyants | 04/10/2022 | ◈ | https://la1ere.franceinfo.fr/reunion/le-groupe-les-flamboyants-epingle-par-la-chambre-regionale-des-comptes-pour-des-surfacturations-de-soins-1327736 |
| SRC-12 | Le Parisien, AP-HP direction informatique (CRC 2019) | 16/12/2019 | ◈ | (hérité du parent FCT-104 ; URL non archivée dans le parent, référence : Le Parisien 16/12/2019) |
| SRC-13 | Midi Libre, CHU de Nîmes (N. Best) | 25/11/2024 | ◈ | (hérité du parent FCT-105 ; URL non archivée dans le parent, référence : Midi Libre 25/11/2024) |
| SRC-14 | Le Figaro, Saint-Maur-des-Fossés/Bygmalion | 27/02/2024 | ◈ | https://www.lefigaro.fr/flash-actu/fausses-factures-avec-bygmalion-henri-plagnol-condamne-a-six-mois-avec-sursis-20240227 |
| SRC-15 | Le Courrier de la Mayenne, EHPAD Saint-Berthevin | 06/11/2023 | 🌍 | https://www.lecourrierdelamayenne.fr/actualite-21804-mayenne-l-ancienne-employee-d-un-ehpad-condamnee-pour-de-fausses-factures-et-de-faux-bulletins-de-salaire |
| SRC-16 | Zinfos974, association d'insertion (La Réunion) | 01/11/2024 | 🌍 | https://www.zinfos974.com/factures-falsifiees-et-cheques-en-blanc-trois-anciennes-salariees-dune-association-condamnees/ |
| SRC-17 | OCDE, Perspectives sur l'intégrité et la lutte contre la corruption 2026 (chap. marchés publics) | 24/03/2026 | ◈ | https://www.oecd.org/fr/publications/perspectives-de-l-ocde-sur-l-integrite-et-la-lutte-contre-la-corruption-2026_9b8b4cae-fr/full-report/component-14.html |
| SRC-18 | Anticor (estimations marchés publics), synthèse Cour des comptes « Évaluation de la lutte contre la corruption » | 12/2025 | ⟐̅ | https://www.ccomptes.fr/sites/default/files/2025-12/20251209-Evalution-de-la-lutte-contre-la-corruption_1.pdf |
| SRC-19 | TF1 Info/Les Vérificateurs, RAND 2016 (120 Md€) | 02/10/2024 | ◉ | https://www.tf1info.fr/economie/la-corruption-coute-t-elle-chaque-annee-120-milliards-d-euros-en-france-comme-l-affirme-anticor-2326055.html |
| SRC-20 | AFA, rapport d'activité 2025 | 2026 | ◈ | https://www.agence-francaise-anticorruption.gouv.fr/files/2026-07/Rapport%20d%27activit%C3%A9%202025%20AFA.pdf |

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260809-1408-surfacturation-commande-publique | PARENT_RUN_ID:20260809-1343 | AS_OF:2026-08-09 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:surfacturation-commande-publique | complexity:13→APEX | route overrides:NONE | scope:2016-2026, France
modules:SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|KERNEL
degraded:NONE | query target/actual: 10/10

COUNT: ◈15 ◉2 ○1 | unique evidence objects:26 | upstream families:11
LEADS:terminal 1/1 | AXES:terminal 5/5 | N/A:none
FAILURES:2 (2 agents incomplets au 1er passage, relancés avec succès) | FALLBACKS:0
unresolved gaps:GAP-002..GAP-006 (ACCESS/METHOD/CORPUS) | GAP-001 CONFIRMÉ ET ÉTENDU (22-33, dossier avenants-5-grands-projets)
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @MNEMO_Q « surfacturation commande publique avenants prestations fictives » | NO_RESULT (0 mémoire) | Mnemolite | — |
| 2 | SYS | @READ dossier parent (GAP-003) + modules | Chargés (héritage revalidé) | run 20260809-1343 | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_enrichissement-legalise-france/ |
| 3 | ○ | QRY-001 (AXS-001) : avenants, options, seuils, données essentielles | FOUND : FCT-004 à 007 | SRC-03/04/05 | legifrance.gouv.fr, conseil-etat.fr |
| 4 | ○ | QRY-002 (AXS-002) : surcoûts grands projets (EPR, JO, Grand Paris, Flyvbjerg) | FOUND : FCT-008 à 011 (1er agent incomplet, relancé) | SRC-06/07/08/09 | cato.org, lemonde.fr, vie-publique.fr, tf1info.fr |
| 5 | ○ | QRY-003 (AXS-003) : prestations fictives, fausses factures, cas jugés | FOUND : FCT-012 à 018 (1er agent incomplet, relancé) | SRC-10 à 16 | franceinfo.fr, la1ere.franceinfo.fr, lefigaro.fr, presse locale |
| 6 | ○ | QRY-004 (AXS-004) : chiffrages existants (OCDE, Anticor, RAND, Sénat 830, DAJ) | FOUND : FCT-019 à 025 | SRC-17/18/19/01/02 | oecd.org, ccomptes.fr, tf1info.fr, senat.fr |
| 7 | SYS | Calcul encadré FCT-026 (fourchettes appliquées) | ANALYSE étiquetée ⁂ (extrapolation, non mesure) | SRC-17/18/01 | — |
| 8 | SYS | @MNEMO_S + FACT_WRITEBACK | PENDING_AT_SERIALIZATION | — | — |
| 9 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_surfacturation-commande-publique/2026-08-09_14-08_surfacturation-commande-publique_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 | Modules chargés ; manifest FINAL ; 15 symboles scorés, aucun ✗ | ✅ |
| G1 | LEAD vs OBJECT distincts ; 5 axes terminaux ; périmètre explicite | ✅ |
| G2 | 6 CLM avec support/counter/gap | ✅ |
| G3 | FACT_REGISTRY 26 faits, statuts canoniques | ✅ |
| G4 | Chaque ✦ → SRC-ID + URL ; ✧ pour corroboration restante | ✅ |
| G5 | CAU-001 à 006 typés, arrêt à l'évidence, chaîne « complot » réfutée | ✅ |
| G6 | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités | ✅ |
| G7 | CONTR-001 à 003 documentés et résolus | ✅ |
| G8 | TRACE_MATRIX ; QRY-001 à 004 tracés ; IDs résolus | ✅ |
| G9 | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis ; corrections P0-P1 appliquées après relecture (FCT-024/027, CONTR-004, étiquettes) | ✅ |
| G10 | Un seul chemin ; une seule write FINAL ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY** : edi_gap = (0.80-0.69)/0.80 = 0.1375 ; query_gap = N/A ; coverage_gap = 0. GAP_SEVERITY = 0.1375 × 1.00 = 0.14 < 0.20 → procéder avec divulgation (gaps GAP-001 à GAP-006 déclarés).

---

*TL;DR : SUJET : préjudice de la surfacturation et du gonflement des factures dans la commande publique française. OBJET : préjudice réel et massif mais non mesuré par aucune institution ; encadrement 14-100 Md€/an (extrapolation OCDE 8-25 % / Anticor 20-25 % appliquées à 170-400 Md€) ; partie jugée infime (58 M€ CPAM = plus gros cas récent) ; dérives de projets structurelles (EPR ×7, 9/10 en dérive) ; la partie légale (avenants 10/15/50 %, options, gré à gré 170 Md€) est le canal dominant et le moins contrôlé. SOURCE : UPDATE du GAP-003 parent. MANIPULATION : Ξ=9, €=8, ↕=8, Κ=8 ; non-verdict. LIMITE : GAP-001 à GAP-006 (pas de mesure nationale, fourchettes = extrapolations).*
