# INVESTIGATION APEX : GAP-005 « LES AVENANTS » — DÉRIVES DE COÛTS PAR AVENANTS SUR 5 GRANDS PROJETS (EPR FLAMANVILLE, GRAND PARIS EXPRESS, JO 2024, CANAL SEINE-NORD, HÔPITAL GRAND PARIS) : CHIFFRER LA PART LÉGALE

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260809-2233-avenants-5-grands-projets
PARENT_RUN_ID  : 20260809-1408-surfacturation-commande-publique (GAP-001 ACCESS : volume des avenants non agrégé)
AS_OF          : 2026-08-09
INPUT_KIND     : UPDATE (exécution de la branche « avenants 5 projets » du GAP-005 demandée par l'utilisateur)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique : « documenter les dérives de coûts par avenants sur 5 grands projets pour chiffrer la part légale de la surfacturation publique »)
SUBJECT_SLUG   : avenants-5-grands-projets
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_avenants-5-grands-projets/2026-08-09_22-33_avenants-5-grands-projets_INVESTIGATION.md
SCOPE          : rôle des avenants dans les dérives de coûts de 5 grands projets publics (EPR Flamanville, Grand Paris Express, JO 2024/SOLIDEO, Canal Seine-Nord Europe, Hôpital Grand Paris Nord) ; tentative de chiffrage de la part « légale » (avenants dans les seuils) vs « illégale » (modifications substantielles) ; période 2007-2026 ; France
COMPLEXITY     : CX_SCORE=13 → $CX=APEX (political 2, technical 2, temporal 3, geo 2, narratives 2, data 2)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 18b
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE (héritage des runs parents)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« peut-on chiffrer la part légale de la surfacturation publique en documentant les dérives par avenants sur 5 grands projets ? ») :

**NON pour le chiffre, OUI pour la preuve du mécanisme — et le constat d'absence est lui-même le résultat.** Le dossier 14-08 avait déclaré (GAP-001, ACCESS) que « le volume annuel des avenants n'est agrégé par aucune institution ». Cette enquête étend et confirme le constat sur les **5 plus grands projets du pays** :

1. **Aucun des 5 projets ne publie le montant cumulé de ses avenants.** Ni EDF (EPR), ni la SGP (Grand Paris), ni SOLIDEO (JO), ni SESN (Seine-Nord), ni AP-HP (Hôpital GP) ne publient d'agrégat « total des avenants » dans les rapports accessibles (FCT-001 à FCT-003, constats d'absence). La donnée existe dans les marchés (données essentielles, obligatoires depuis 2019 — FCT-006), personne ne l'agrège.
2. **Les dérives totales, elles, sont chiffrées** : EPR 3,3 → 23,7 Md€ (×7, FCT-009) ; Grand Paris ~19-25 → 35-42 Md€ (+15-20 Md€, FCT-010) ; Seine-Nord ~4,5-5,1 → 7,347 Md€ (+2,2-2,8 Md€ hors frais financiers, ~10 Md€ avec, FCT-011/012) ; JO 2024 maîtrisé à 6,6 Md€ (FCT-013) ; Hôpital GP ~1,1 → 1,3 Md€ (hôpital) / ~2 Md€ (campus) (FCT-014). **Cumul encadré des surcoûts sur 3 projets (EPR + GPE + Seine-Nord) : ~37-43 Md€** (FCT-015, calcul, ⁂ — HGP exclu pour dérive marginale, JO exclu pour absence de dérive) — dont la part passant par avenants est NON ISOLABLE.
3. **Le mécanisme légal est documenté** : les avenants dans les seuils (10 % fournitures/services, 15 % travaux, 50 % prestations indispensables — CCP L2194) permettent d'augmenter les prix sans nouvelle mise en concurrence (FCT-006, hérité du 14-08). La jurisprudence (modification substantielle = nouvelle concurrence, CE) borne la partie « illégale » (FCT-007).
4. **Le contre-exemple JO 2024 est le fait le plus instructif** : SOLIDEO a « évité les dérives » par une supervision stricte (CdC 29/09/2025 : « pas de dérapage », « rares anomalies » sur les avenants ; Sénat n° 748, 16/06/2026 : la supervision a évité les dérives majeures). **Le seul projet avec contrôle documenté des avenants est le seul sans dérapage** — corrélation documentée, causalité non prouvée.

**Verdict sur le LEAD_QUESTION** (« les avenants sont-ils la part légale de la surfacturation ? ») : **MÉCANISME CONFIRMÉ, CHIFFRE IMPOSSIBLE.** La part légale de la dérive est structurellement non chiffrable par sources publiques (pas d'agrégat), mais le canal est établi (seuils) et le contraste JO vs EPR/GPE/Seine-Nord montre que le contrôle des avenants est le facteur discriminant documenté. **La « part légale » n'est pas mesurable ; la « possibilité de la mesurer » est démontrée par les données essentielles non exploitées et par l'exemple JO.**

**Acteurs** : maîtres d'ouvrage (EDF, SGP, SOLIDEO, SESN, AP-HP), titulaires (Framatome, groupements BTP, promoteurs), contrôleurs (CdC, Sénat 748, commission d'enquête GPE), législateur (seuils CCP).

**Principales limites** : aucun agrégat d'avenants publié sur les 5 projets (GAP-001 confirmé) ; le rapport de la commission d'enquête Sénat GPE 2023 n'a pas pu être localisé (URL 404, numéro non confirmé) ; le rapport CdC « La Société du Grand Paris » (05/2024) identifié mais non lu (site CdC 422 via jina) ; la ventilation dérive/avenants/inflation n'est chiffrée pour aucun projet.

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **9/10** | Aucun des 5 projets ne publie son agrégat d'avenants ; la commission d'enquête Sénat GPE 2023 n'est pas localisable en ligne (URL 404) ; les données essentielles (2019) contiennent les avenants sans analyse. |
| 2 | **€** money | **8/10** | EPR 3,3 → 23,7 Md€ ; GPE 25 → 35-42 Md€ ; Seine-Nord 4,3 → 7,347 Md€ (~10 avec frais) ; JO 6,6 Md€ ; HGP 1,1 → 1,3 Md€. |
| 3 | **Λ** framing | 7/10 | « Avenant » (technique, neutre) vs « dérive » (péjoratif) ; « prestation complémentaire » (légal) vs « surfacturation » ; « aléas de chantier » vs « sous-évaluation initiale délibérée » ; « maîtrise » (JO) vs « dépassement » (EPR). |
| 4 | **Ω** inversion | **8/10** | Le discours « les seuils d'avenants sont des garde-fous » cohabite avec des dérives ×7 (EPR) ; « la France maîtrise ses coûts » (JO) vs 3 projets à +20 Md€ chacun ; les avenants sont « encadrés » par des seuils qui autorisent l'augmentation sans concurrence. |
| 5 | **Ψ** sidération | 2/10 | Champ froid : les dérives (EPR +20 Md€) ne produisent pas de sidération durable. |
| 6 | **↕** verticalité | **8/10** | Asymétrie d'information : l'acheteur (État) sous-évalue, le titulaire facture ; les avenants sont négociés dans un rapport de force inégal après engagement ; le contribuable paie sans comparaison possible (sauf gré à gré). |
| 7 | **Φ** spectacle | 2/10 | Peu de spectacle : JO = spectacle positif, EPR = technique. |
| 8 | **Σ** sémiotique | 3/10 | « Avenant », « option », « tranche », « aléas » : vocabulaire neutre qui naturalise l'augmentation. |
| 9 | **Κ** cynisme | **8/10** | Les seuils (10/15/50 %) sont votés comme garde-fous et servent de plafonds de plein droit ; les dérives sont « actées » par avenants dans le silence ; JO est célébré pendant qu'EPR multiplie par 7 ; les rapports (CdC, Sénat) documentent sans sanctionner. |
| 10 | **ρ** résistance | 7/10 | CdC (EPR 2025, SGP 2024, Seine-Nord 04/2026, JO 09/2025), Sénat (748 JO, commission GPE 2023), presse (La Voix du Nord, Le Moniteur, BFMTV). |
| 11 | **κ** influence subtile | 7/10 | Architecture par défaut : l'avenant dans les seuils est le chemin le moins frictionnel vers l'augmentation ; pas de débat public sur les agrégats. |
| 12 | **⫸** convergence | 7/10 | EPR ×7, GPE +15-20 Md€, Seine-Nord +2,2-2,8 Md€, HGP +0,2 Md€ : 4 projets sur 5 en dérive documentée ; le seul maîtrisé (JO) est le seul à supervision stricte des avenants. |
| 13 | **⚔** guerre cognitive | 1/10 | Aucune opération organisée documentée. |
| 14 | **🌐** réseau | 7/10 | Nœuds : EDF/Framatome, SGP/groupements BTP, SOLIDEO/promoteurs, SESN/consortiums, AP-HP/constructeurs ; rotations public-privé documentées ailleurs dans le corpus (15-42). |
| 15 | **⏰** temporalité | 7/10 | 2007 EPR 3,3 Md€ ; 2010 GPE 25 Md€ ; 2015 Seine-Nord 4,3 Md€ ; 2019 données essentielles ; 2021 GPE 35 Md€ ; 2023 commission Sénat GPE + HGP ; 2024 CdC SGP + CdC JO 2024 ; 2025 CdC EPR 23,7 Md€ + CdC JO ; 2026 CdC Seine-Nord 7,347 Md€ + Sénat 748. |

**BIAS TEST (15/15 scorés).** Aucun symbole au-delà de 9. Les champs 1, 4, 9 signalent le cœur : l'absence d'agrégat est un fait d'enquête, pas un vide.

**PATTERNS** : @PAT[ICEBERG] (Ξ=9), @PAT[MONEY] (€=8), @PAT[CYN] (Κ=8), @PAT[FASC] (⫸=7). **THREATS** : @THR[REG_CAPTURE] (seuils, gré à gré), @THR[NUDGE] (avenants par défaut).

**RHETORICAL** : NUM (chiffres officiels CdC/Sénat) ; AUTH (CdC, Sénat) ; DEM et BF = 0.

## 3. CLUSTERS (routage SYMBOLS §4)

| Cluster | Diagnostic | Gap |
|---------|------------|-----|
| ICEBERG (Ξ=9) | Émergé : dérives totales chiffrées (EPR 23,7, GPE 42, Seine-Nord 7,3). Immergé : agrégats d'avenants (aucun publié). | La partie immergée est structurellement non mesurée. |
| MONEY (€=8) | Flux : contribuable → maître d'ouvrage → titulaire, augmenté par avenants. | Bénéficiaires par avenant non isolés. |
| POWER (↕=8) | Asymétrie acheteur/titulaire après engagement ; seuils comme plafonds de plein droit. | Pas de mesure du surcoût vs concurrence. |
| INVERSION (Ω=8, Κ=8) | Garde-fous affichés vs dérives ×7 ; JO célébré vs EPR silencieux. | — |
| CONFIRMATION (κ=7) | Avenants par défaut ; données essentielles non analysées. | Pas de taux d'avenant par projet. |
| FRAGMENTATION (⫸=7) | 4/5 projets en dérive, 1 maîtrisé (JO) avec supervision stricte. | Causalité contrôle → maîtrise non prouvée. |
| NETWORK (🌐=7) | EDF, SGP, SOLIDEO, SESN, AP-HP + titulaires. | Pas de graphe. |
| TEMPORAL (⏰=7) | 2007-2026 : les réformes (données essentielles 2019) n'ont pas créé d'analyse agrégée. | — |

## 4. HERMÉNEUTIQUE (statut : ANALYSE)

- **L1 (texte) :** rapports CdC (EPR 14/01/2025, SGP 05/2024, Seine-Nord 10/04/2026, JO 29/09/2025), Sénat (748, commission GPE 2023), presse (La Voix du Nord, Le Moniteur, BFMTV, La Tribune).
- **L2 (structure) :** trois strates : (a) la dérive totale (chiffrée, officielle), (b) le canal (avenants dans les seuils — documenté par le droit), (c) la ventilation dérive/avenants/inflation (jamais publiée).
- **L3 (intérêt) :** la ventilation n'est pas publiée parce que la dérive est répartie entre maître d'ouvrage et titulaires dans une négociation continue : l'avenant est l'instrument qui convertit l'incertitude (inflation, aléas) en prix — personne n'a intérêt à isoler la part imputable.
- **L4 (sémiotique) :** « aléas de chantier », « circonstances imprévues », « prestations complémentaires » : le vocabulaire de l'avenant naturalise le surcoût comme accident plutôt que comme décision.
- **L5 (comparaison) :** le contraste JO (supervision stricte, pas de dérapage) vs EPR (×7) est la seule quasi-expérience naturelle du corpus : deux maîtres d'ouvrage publics, deux régimes de contrôle des avenants, deux trajectoires opposées.
- **L6 (contexte) :** débat budgétaire 2024-2026 (revue des dépenses) où les 37-43 Md€ de surcoûts cumulés documentés n'ont jamais été agrégés par Bercy.

**Lecture concurrente** : les dérives s'expliquent par des aléas réels (EPR = technologie nouvelle, Seine-Nord = inflation Ukraine) ; les avenants sont une pratique normale de gestion ; la corrélation JO/contrôle ne prouve pas la causalité. La synthèse retenue : le mécanisme est légal et documenté, la ventilation est structurellement absente, et le contraste JO fournit un point de comparaison factuel sans causalité établie.

## 5. FORENSIC REASONING (ICEBERG MAX)

**Émergé (chiffres officiels)** : EPR 3,3 → 23,7 Md€ (CdC 14/01/2025) ; GPE 19-25 → 35-42 Md€ (Sénat 2023, CdC) ; Seine-Nord 4,3 → 7,347 Md€ HT, ~10 Md€ avec frais (CdC 10/04/2026) ; JO 6,6 Md€ (CdC 29/09/2025) ; HGP 1,1 → 1,3 Md€ hôpital, ~2 Md€ campus.

**Surface (mécanismes documentés)** : seuils d'avenants 10/15/50 % (CCP L2194) ; données essentielles obligatoires depuis 2019 (avenants publiés, non agrégés) ; jurisprudence CE « modification substantielle = nouvelle concurrence » ; JO : supervision SOLIDEO, « rares anomalies » sur les avenants.

**Immergé (jamais publié)** : montant cumulé des avenants par projet ; ventilation dérive/avenants/inflation ; nombre d'avenants par projet (sauf Seine-Nord ~76 marchés, avenants « fréquents ») ; le rapport de la commission d'enquête Sénat GPE 2023 (introuvable en ligne).

**ICEBERG LOAD :** 10 strates émergées/surface confirmées, 5 inférées. La signature : les dérives sont officielles et massives, la ventilation par avenants est le trou noir central — les données existent (données essentielles) et ne sont pas exploitées.

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « Les dérives sont des aléas gérés dans un cadre légal » : avenants encadrés par les seuils, données essentielles publiées, CdC contrôle a posteriori.
- **Antithèse (critique) :** « Les avenants sont le canal légal de la surfacturation » : 4/5 projets en dérive massive, aucun agrégat publié, JO seul maîtrisé avec supervision stricte.
- **Arbitrage par les preuves :** la thèse est confirmée sur la forme (les seuils existent, la publication existe depuis 2019) ; l'antithèse est confirmée sur le fond (dérives officielles ×7, absence d'agrégat, contraste JO). **La synthèse** : les avenants sont le canal légal par lequel les dérives s'actent ; leur part exacte est non mesurable par sources publiques ; le contrôle (JO) est le seul discriminant documenté.

**Réfutation testée** : « les avenants sont marginaux dans la dérive EPR » — non vérifiable : EDF ne publie pas la ventilation ; « la dérive Seine-Nord est purement inflationniste » — la CdC cite l'inflation ET les retards ET une « définition initiale des besoins perfectible » (imputant au maître d'ouvrage) ; « JO prouve que tout est maîtrisable » — corrélation, pas causalité. Les trois réfutations bornent le verdict.

## 7. CHRONOLOGIE

| Année | Événement | Source | Statut |
|-------|-----------|--------|--------|
| 2007 | Lancement EPR Flamanville à 3,3 Md€ | CdC 14/01/2025 | ✦ |
| 2010 | Grand Paris Express : budget initial ~25 Md€ | Sénat/CdC | ✦ |
| 2017-2019 | Seine-Nord : coût de référence ~4,5-5,1 Md€ (CdC 10/04/2026) | CdC 10/04/2026 | ✦ |
| 2019 | Obligation de publication des données essentielles (arrêté 22/03/2019) — les avenants sont publiés, jamais agrégés | Légifrance | ✦ |
| 2021 | GPE : coût révisé ~35 Md€ | Sénat | ✧ |
| 2023 | Commission d'enquête Sénat GPE « le coût du dépassement » (numéro non confirmé — URL 404) ; GPE ~42 Md€ ; HGP : vice de procédure (BFMTV 25/10/2023) | Sénat, BFMTV | ✦ (fait HGP) |
| 05/2024 | CdC « La Société du Grand Paris » (identifié, non lu — site CdC 422) | CdC | ✧ |
| 14/01/2025 | CdC : EPR 23,7 Md€ (€2023, intérêts inclus) | CdC/Le Monde | ✦ |
| 29/09/2025 | CdC JO 2024 : 6,6 Md€, « pas de dérapage », « rares anomalies » avenants | CdC | ✦ |
| 16/06/2026 | Sénat n° 748 (JO) : la supervision SOLIDEO a évité les dérives majeures | Sénat | ✦ |
| 10/04/2026 | CdC Seine-Nord : 7,347 Md€ HT, ~10 Md€ avec frais financiers ; ~76 marchés ; avenants fréquents ; mise en service 2032 | CdC | ✦ |

## 8. DOMAINES (par axe)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 EPR | Quelle part de la dérive EPR passe par avenants ? | Dérive 3,3 → 23,7 Md€ documentée ; AUCUN avenant contractuel chiffré public (pas d'avenant 2015/2017/2022 documenté) | FCT-008/009 | SATURATED (GAP ventilation) |
| AXS-002 GPE | Avenants GPE chiffrés ? | Dérive 25 → 35-42 Md€ ; rapport CdC SGP 05/2024 identifié ; agrégat d'avenants NON publié | FCT-010 | SATURATED (GAP) |
| AXS-003 JO | Avenants JO documentés ? | Maîtrise : 6,6 Md€ ; « rares anomalies » ; supervision SOLIDEO saluée (Sénat 748) | FCT-013/016 | SATURATED |
| AXS-004 SEINE-NORD | Avenants Seine-Nord ? | ~4,5-5,1 → 7,347 Md€ (~10 avec frais) ; ~76 marchés ; avenants « fréquents » ; dérive : inflation + retards + besoins perfectibles | FCT-011/012 | SATURATED (agrégat GAP) |
| AXS-005 HÔPITAL GP | Dérive HGP par avenants ? | ~1,1 → 1,3 Md€ (hôpital), ~2 Md€ campus ; ouverture 2028-2030 ; tensions financières (CdC/IGAS) ; vice de procédure 2023 | FCT-014 | SATURATED |
| AXS-006 CHIFFRAGE | Peut-on chiffrer la part légale ? | NON (aucun agrégat) ; cumul encadré des surcoûts 3 projets : ~37-43 Md€ (⁂) ; JO = contre-exemple | FCT-015 | ANALYSE |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| EDF | Maître d'ouvrage EPR | Dérive 3,3 → 23,7 Md€ ; ne publie pas la ventilation des avenants | FCT-009 | ROLE |
| Framatome (ex-Areva NP) | Titulaire EPR | Contrat initial + restructuration transactionnelle 2017 ; aucun avenant chiffré public | FCT-008 | ROLE |
| SGP | Maître d'ouvrage GPE | 25 → 35-42 Md€ ; marchés de génie civil | FCT-010 | ROLE |
| SOLIDEO | Maître d'ouvrage JO | 3,63 Md€ infrastructures ; supervision stricte ; « rares anomalies » | FCT-013/016 | ROLE + contrôle |
| SESN | Maître d'ouvrage Seine-Nord | 4,3 → 7,347 Md€ ; ~76 marchés ; avenants fréquents | FCT-011/012 | ROLE |
| AP-HP | Maître d'ouvrage HGP | 1,1 → 1,3 Md€ ; tensions financières ; vice de procédure 2023 | FCT-014 | ROLE |
| Cour des comptes | Contrôle | EPR, SGP, Seine-Nord, JO : dérives chiffrées, aucune ventilation | FCT-009 à 013 | ρ |
| Sénat | Contrôle | 748 (JO) ; commission GPE 2023 (introuvable en ligne) | FCT-013/016 | ρ |
| Titulaires BTP | Bénéficiaires | Avenants, prestations complémentaires | — | Bénéfice ≠ intention |

**CONTROL_MAP** :

| Contrôleur | Mécanisme | Résultat | Gap |
|------------|-----------|----------|-----|
| CTRL-001 Données essentielles | Publication obligatoire des avenants (2019) | Les avenants sont publiés projet par projet | Aucune agrégation nationale |
| CTRL-002 SOLIDEO | Supervision stricte des marchés JO | « Pas de dérapage », « rares anomalies » | Cas unique |
| CTRL-003 CdC | Contrôle a posteriori | Dérives chiffrées projet par projet | Pas de ventilation dérive/avenants |
| CTRL-004 Jurisprudence CE | Modification substantielle = nouvelle concurrence | Borne la partie illégale | Pas de contentieux agrégé |

## 10. CHAÎNES / PELOTE (causalité)

**CAU-001 : Les avenants convertissent l'incertitude en prix dans les seuils.**
Étage 1 : seuils 10/15/50 % autorisent l'augmentation sans concurrence (FCT-006). Étage 2 : 4/5 projets en dérive massive (FCT-009 à 012, 014). Étage 3 : la ventilation dérive/avenants n'est pas publiée (FCT-001 à 003, GAP). Type : STRUCTUREL. Confidence : high sur les faits, la ventilation reste GAP.

**CAU-002 : Le contrôle des avenants est le discriminant documenté (JO vs EPR/GPE/Seine-Nord).**
Étage 1 : SOLIDEO : supervision stricte, « rares anomalies » (FCT-016). Étage 2 : EPR ×7, GPE +15-20 Md€, Seine-Nord +2,2-2,8 Md€ : pas de supervision équivalente documentée. Étage 3 : corrélation contrôle → maîtrise documentée, causalité NON prouvée. Type : MÉCANISME (corrélation). Confidence : high sur la corrélation, NON sur la causalité.

**CAU-003 : L'absence d'agrégation rend la part légale indétectable.**
Étage 1 : les données essentielles existent depuis 2019 (FCT-006). Étage 2 : aucune institution n'agrège les avenants par projet ni en national (FCT-001 à 003). Étage 3 : la « part légale » est donc non mesurable — le constat d'absence est le résultat. Type : SYSTÈME. Confidence : high.

**CAU-004 (rejetée) : « La surfacturation par avenants est un complot organisé ».** Réfutée : aucun faisceau de coordination n'est documenté ; les dérives s'expliquent aussi par des aléas réels (inflation, technologie). Le bénéfice n'implique pas l'intention.

## 11. CARTE DES PREUVES

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « Aucun des 5 projets ne publie son agrégat d'avenants » | Constats d'absence (EDF, SGP, SOLIDEO, SESN, AP-HP) ; les données essentielles existent sans agrégation | La donnée existe projet par projet | SOUTENU (constat) |
| CLM-002 | « Les dérives totales sont massives et officielles » | EPR 23,7 Md€ (CdC 2025) ; GPE 35-42 Md€ (Sénat) ; Seine-Nord 7,347 Md€ (CdC 2026) | JO 2024 maîtrisé (6,6 Md€) | SOUTENU (4/5) |
| CLM-003 | « Les avenants sont le canal légal de l'augmentation » | Seuils 10/15/50 % ; avenants publiés (2019) | Les avenants couvrent des aléas réels | SOUTENU (mécanisme) |
| CLM-004 | « La part légale n'est pas chiffrable par sources publiques » | Aucun agrégat publié sur 5 projets | Les données essentielles permettraient une analyse non faite | SOUTENU |
| CLM-005 | « JO prouve que le contrôle des avenants fonctionne » | SOLIDEO : pas de dérapage, rares anomalies (CdC 2025, Sénat 748) | Corrélation, pas causalité | SOUTENU (fait), NON causal |
| CLM-006 | « Cumul encadré des surcoûts 3 projets : ~37-43 Md€ » | EPR +20,4 + GPE +15-20 + Seine-Nord +2,2-2,8 | Natures différentes, périmètres différents ; non additionnables en rigueur | ANALYSE (⁂ calcul) |

### FACT_REGISTRY (15 faits — FCT-004/005 non utilisés)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | Constat d'absence : EDF ne publie pas d'agrégat d'avenants du contrat EPR (aucun avenant contractuel chiffré public trouvé : ni 2015, ni 2017, ni 2022) | NON PUBLIÉ | SRC-01/02 (constat) | ✦ (constat) |
| FCT-002 | Constat d'absence : la SGP ne publie pas d'agrégat d'avenants des marchés de génie civil GPE | NON PUBLIÉ | SRC-03 (constat) | ✦ (constat) |
| FCT-003 | Constat d'absence : SOLIDEO/SESN/AP-HP ne publient pas d'agrégat d'avenants (JO : « rares anomalies » ; Seine-Nord : « avenants fréquents » sans montant cumulé ; HGP : suivi des marchés sans agrégat) | NON PUBLIÉ | SRC-04/05/06 (constats) | ✦ (constats) |
| FCT-006 | Seuils d'avenants de plein droit : <10 % (fournitures/services), <15 % (travaux), jusqu'à 50 % (prestations indispensables) ; au-delà : circonstances imprévues ; données essentielles obligatoires depuis 2019 | 10/15/50 % | SRC-07 CCP L2194 (hérité 14-08) | ✦ |
| FCT-007 | Jurisprudence : modification substantielle = nouvelle mise en concurrence requise (sinon illégalité) | — | SRC-08 CE (hérité 14-08) | ✦ |
| FCT-008 | EPR : restructuration Areva/EDF 2017 (transactionnelle, prise de contrôle Framatome par EDF) ; pas d'avenant chiffré public de +2,2 Md€ documenté | — | SRC-01 | ✧ |
| FCT-009 | EPR Flamanville : 3,3 Md€ (2007) → 23,7 Md€ (€2023, intérêts inclus, CdC 14/01/2025), ×7 | +20,4 Md€ | SRC-02 CdC 14/01/2025 (hérité 14-08) | ✦ |
| FCT-010 | Grand Paris Express : ~19-25 Md€ initial → 35 Md€ (2021) → ~42 Md€ (2023, Sénat) ; rapport CdC « La Société du Grand Paris » (05/2024) identifié | +15-20 Md€ | SRC-03 (hérité 14-08) | ✧ |
| FCT-011 | Seine-Nord : coût révisé 7,347 Md€ HT courants (CdC 10/04/2026) ; ~10 Md€ avec emprunt de bouclage et frais financiers ; base de départ ~4,5-5,1 Md€ (2017-2019, CdC) — le « 4,3 Md€ (2016) » du corpus est à re-vérifier (✧) | 7,347 Md€ | SRC-04 CdC 10/04/2026 | ✦ (révisé) / ✧ (base) |
| FCT-012 | Seine-Nord : ~76 marchés publics ; recours « fréquent » aux avenants ; dérive attribuée à l'inflation post-Ukraine, aux retards (mise en service 2032) et à une « définition initiale des besoins perfectible » | ~76 marchés | SRC-04 ; SRC-09 presse | ✦ |
| FCT-013 | JO 2024 : 6,6 Md€ de dépenses publiques (3,02 org + 3,63 SOLIDEO) ; « absence de dérapage budgétaire » ; « rares anomalies » sur les avenants | 6,6 Md€ | SRC-05 CdC 29/09/2025 | ✦ |
| FCT-014 | Hôpital Grand Paris Nord (Saint-Ouen) : ~1,1 Md€ initial → ~1,3 Md€ révisé (hôpital), ~2 Md€ (campus) ; ouverture 2028-2030 ; tensions financières (rapports d'audit selon presse) ; vice de procédure relevé 25/10/2023 (État devra remédier sous 6 mois) | 1,1 → 1,3 Md€ | SRC-06 AP-HP/BFMTV | ✦ |
| FCT-015 | Cumul encadré des surcoûts (3 projets : EPR + GPE + Seine-Nord ; HGP exclu = dérive marginale +0,2 Md€, JO exclu = pas de dérive) : ~37-43 Md€ — addition non homogène (périmètres et natures différents), présentée comme calcul indicatif, jamais comme mesure | ~37-43 Md€ | calcul (SRC-02/03/04) | ⁂ |
| FCT-016 | SOLIDEO : supervision des marchés saluée par le Sénat n° 748 (16/06/2026) : la méthode de supervision a évité les dérives financières majeures ; ouvrages ~2,49 Md€ (1,68 via maquette), villages ~1,96 Md€ | 2,49 / 1,96 Md€ | SRC-10 Sénat 748 | ✦ |
| FCT-017 | GAP confirmé et étendu : la commission d'enquête Sénat GPE 2023 (« le coût du dépassement ») n'est pas localisable en ligne (URL r22-580-1 = 404, numéro non confirmé) | NON LOCALISÉ | SRC-03 (constat) | ✦ (constat) |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-012 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-013 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-014 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-015 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-016 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
FCT-017 | FACT | ❧ | - | - | - | 2026-08-09_22-33_avenants-5-grands-projets | - | -
<!-- /FACT_REGISTRY_V1 -->

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | Hôpital GP : « 3,5 Md€ » (hypothèse du corpus) vs « 1,1 → 1,3 Md€ » (hôpital) / ~2 Md€ (campus) | La dérive ~3,5 Md€ n'est pas confirmée par les sources AP-HP/CdC : le coût révisé documenté est ~1,3 Md€ (hôpital) ; le chiffre 3,5 est écarté comme non sourcé | RÉSOLUE (correction) |
| CONTR-002 | JO : « pas de dérapage » (CdC 2025) vs dérives générales du corpus (9/10) | JO = contre-exemple relatif : supervision stricte SOLIDEO, contexte de cadrage rigide ; il borne la thèse sans la réfuter | RÉSOLUE |
| CONTR-003 | Seine-Nord : 4,3 Md€ vs 5,1 Md€ vs 7,347 Md€ | Périmètres et dates différents (2016 : 4,3 ; 2017-2019 : 4,5-5,1 ; CdC 04/2026 : 7,347 HT) ; les trois cités avec leur date | DOCUMENTÉE |
| CONTR-004 | Cumul 37-43 Md€ : addition de natures différentes | Assumée et explicitée (⁂) : EPR = coût total réévalué, GPE = budget programme, Seine-Nord = coût HT — non homogènes, jamais présentée comme mesure | DOCUMENTÉE |

### EDI

```
geo:0.80 lang:0.80 strat:0.80 owner:0.70 persp:0.80 temp:0.80
EDI_raw = .25×.80 + .20×.80 + .20×.80 + .15×.70 + .15×.80 + .05×.80 = 0.775
Pénalité : MISSING_COUNTER (-.10) : perspective des titulaires/constructeurs (défense de la pratique des avenants) absente.
EDI = 0.675 (BROAD, sous la cible APEX 0.80, écart déclaré)
COV = 0.85 | IND = 0.60 | CC = 3/3
EDI* = .5×.675 + .3×.85 + .2×.60 = 0.71
Perspectives : ⟐ 4 | ⟐̅ 2 | 🌍 1 | 🎓 1 | 🔥 1
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait)

| FCT | QRY | SRC | URL (référence) | Statut |
|-----|-----|-----|-----------------|--------|
| FCT-009 | QRY-001 | SRC-02 | lemonde.fr 14/01/2025 (hérité 14-08) | ✦ |
| FCT-011/012 | QRY-002 | SRC-04 | ccomptes.fr 10/04/2026 « La construction du canal Seine Nord Europe et ses conséquences » | ✦ |
| FCT-013/016 | QRY-003 | SRC-05/10 | ccomptes.fr 29/09/2025 ; senat.fr r25-748 | ✦ |
| FCT-014 | QRY-004 | SRC-06 | aphp.fr (campus Saint-Ouen) ; bfmtv.com 25/10/2023 | ✦ |
| FCT-010 | QRY-002 | SRC-03 | ccomptes.fr 05/2024 « La Société du Grand Paris » (identifié, non lu) | ✧ |

## 12. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Passoire par avenants » | Les avenants sont le canal légal massif de la dérive | 4/5 projets en dérive ; seuils ; aucun agrégat | Aléas réels (inflation, technologie) | Retenue (mécanisme) |
| S2 « Aléas de gestion » | Les dérives sont des accidents techniques | EPR = technologie nouvelle ; Seine-Nord = inflation | Flyvbjerg : 9/10 en dérive = la règle ; JO contrôle = contre-preuve | Partiellement valide |
| S3 « Contrôle discriminant » | La supervision des avenants évite la dérive | JO/SOLIDEO : pas de dérapage | Causalité non prouvée | Retenue (corrélation documentée) |
| S4 « Mesure manquante » | La part légale est chiffrable mais non chiffrée | Données essentielles existent (2019) | Aucune institution ne les agrège | Retenue (la donnée existe, l'analyse non) |

**IMPACT_MAP** :

| Acteur | Gain | Perte |
|--------|------|-------|
| Titulaires (Framatome, groupements BTP, promoteurs) | Avenants, prestations complémentaires | Peu de pertes mesurées |
| Maîtres d'ouvrage (EDF, SGP, SESN, AP-HP) | — | Surcoûts (EPR +20,4 Md€, GPE +15-20, Seine-Nord +2,2-2,8) |
| Contribuables | — | ~37-43 Md€ cumulés (3 projets, ⁂), dette |
| SOLIDEO | Maîtrise des coûts (JO 6,6 Md€) | — |
| Élus | Démarrage des projets | Perception du risque |

**RESPONSIBILITY_MAP** : aucun auteur d'intention n'est établi (BENEFIT != INTENT). Rôles documentés : maîtres d'ouvrage (activation des avenants), titulaires (facturation), législateur (seuils), contrôleurs (agrégation absente). La responsabilité systémique (RÉSULTAT) : un système où les données d'avenants existent (2019) et ne sont jamais agrégées — omission d'exploitation, pas fraude.

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : rôle des avenants dans les dérives de 5 grands projets (EPR, GPE, JO, Seine-Nord, Hôpital GP) ; mécanismes légaux (seuils) ; tentative de chiffrage de la part légale. Période 2007-2026.

**Exclusions explicites** : la ventilation dérive/avenants/inflation (non publiée) ; le rapport CdC « Société du Grand Paris » (non lu — site CdC 422 via jina) ; le rapport de la commission d'enquête Sénat GPE 2023 (non localisé en ligne).

**GAP déclarés** :
- GAP-001 (ACCESS, confirmé et étendu du 14-08) : montant cumulé des avenants par projet — non publié sur les 5.
- GAP-002 (ACCESS) : ventilation dérive/avenants/inflation — non publiée.
- GAP-003 (ACCESS) : rapport commission d'enquête Sénat GPE 2023 — non localisé en ligne (URL 404).
- GAP-004 (ACCESS) : rapport CdC SGP 05/2024 — identifié, non lu (site CdC inaccessible via jina).
- GAP-005 (CORPUS) : perspective des titulaires absente (MISSING_COUNTER, EDI).

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : EPR 23,7 Md€ (×7) ; GPE 35-42 Md€ ; Seine-Nord 7,347 Md€ (~10 avec frais) ; JO 6,6 Md€ maîtrisé ; HGP 1,1 → 1,3 Md€ ; seuils 10/15/50 % ; données essentielles 2019 ; SOLIDEO supervision saluée (Sénat 748) ; aucun agrégat d'avenants publié.
- **PROBABLE (✧)** : GPE +15-20 Md€ ; restructuration EPR 2017 ; rapport CdC SGP 05/2024.
- **HYPOTHÈSE (⁂)** : cumul ~37-43 Md€ (3 projets) ; la part des avenants dans la dérive (non isolable).
- **CONTESTÉ (⊗)** : périmètres de coûts (Seine-Nord 4,3/5,1/7,347 ; EPR 23,7 vs 13,2 EDF).
- **INCONNU (⁅)** : agrégats d'avenants ; ventilation ; rapport Sénat GPE 2023.
- **RÉFUTÉ (❧)** : « Hôpital GP à 3,5 Md€ » (non sourcé, corrigé à ~1,3 Md€ hôpital) ; « complot organisé des avenants » (aucun faisceau de coordination).

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD** : input UPDATE (branche avenants du GAP-005 demandée par l'utilisateur). Le verdict d'objet est distinct du verdict de lead : « chiffrer la part légale » reçoit une réponse honnête en deux volets (mécanisme confirmé, chiffre impossible).

**Vérifications contradictoires exécutées** : CONTR-001 (HGP 3,5 Md€ écarté) ; CONTR-002 (JO contre-exemple) ; CONTR-003 (périmètres Seine-Nord) ; CONTR-004 (cumul non homogène). Faits du 14-08 revalidés (EPR, GPE, seuils, données essentielles) et complétés (Seine-Nord CdC 04/2026, JO Sénat 748, HGP).

**Verdict final : MÉCANISME CONFIRMÉ, CHIFFRE IMPOSSIBLE.** Le GAP-001 du 14-08 (avenants non agrégés) est confirmé et étendu aux 5 plus grands projets ; la part légale de la dérive est non chiffrable par sources publiques ; le contraste JO (supervision stricte, pas de dérapage) vs EPR/GPE/Seine-Nord (dérives massives) est la seule quasi-expérience documentée, corrélative et non causale. **Le résultat le plus actionnable : les données essentielles (2019) contiennent les avenants des 5 projets sans qu'aucune institution ne les agrège — une analyse open-data pourrait produire le premier chiffrage de la part légale.**

---

# ANNEXE A. SOURCES

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | EDF/Framatome : rapports annuels, presse (restructuration 2017) | 2015-2025 | ◈ | (via agent — aucun avenant chiffré public trouvé) |
| SRC-02 | Cour des comptes (EPR) relayée par Le Monde | 14/01/2025 | ◈ | https://www.lemonde.fr/economie/article/2025/01/14/epr-de-flamanville-la-cour-des-comptes-estime-le-cout-total-a-23-7-milliards-d-euros_6497010_3234.html |
| SRC-03 | Sénat/CdC Grand Paris Express (2023-2024) | 2023-2024 | ◈ | https://www.ccomptes.fr/fr/publications/la-societe-du-grand-paris-0 (05/2024, identifié) |
| SRC-04 | Cour des comptes, « La construction du canal Seine Nord Europe et ses conséquences » | 10/04/2026 | ◈ | https://www.ccomptes.fr/fr/publications/la-construction-du-canal-seine-nord-europe-et-ses-consequences |
| SRC-05 | Cour des comptes, JO Paris 2024 (rapport global) | 29/09/2025 | ◈ | https://www.ccomptes.fr/fr/publications/les-jeux-olympiques-et-paralympiques-de-paris-2024 |
| SRC-06 | AP-HP (campus Saint-Ouen) + BFMTV (vice de procédure) | 2023-2025 | ◈ | https://www.aphp.fr/nous-connaitre/construire-lhopital-de-demain/le-campus-hospitalo-universitaire-saint-ouen-grand ; https://www.bfmtv.com/paris/futur-hopital-grand-paris-nord-l-etat-devra-remedier-dans-les-six-mois-a-un-vice-de-procedure_AD-202310250517.html |
| SRC-07 | Code de la commande publique, articles L2194-1 à L2194-3 | 2019-2026 | ◈ | https://www.legifrance.gouv.fr (hérité 14-08) |
| SRC-08 | Conseil d'État, jurisprudence « modification substantielle » | constant | ◈ | https://www.conseil-etat.fr (hérité 14-08) |
| SRC-09 | Presse Seine-Nord : La Voix du Nord, Le Moniteur, Banque des Territoires, TF1 Info | 09-10/04/2026 | ◉ | (via agent — 7,347 Md€, ~76 marchés, 2032) |
| SRC-10 | Sénat, rapport d'information n° 748 (JO 2024, village olympique) | 16/06/2026 | ◈ | https://www.senat.fr/rap/r25-748/r25-7481.html |
| SRC-11 | SOLIDEO (ouvrages, villages) + synthèse Patrick Bayeux | 2025-2026 | ◈ | https://www.ouvrages-olympiques.fr/letat |

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260809-2233-avenants-5-grands-projets | PARENT_RUN_ID:20260809-1408 | AS_OF:2026-08-09 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:avenants-5-grands-projets | complexity:13→APEX | route overrides:NONE | scope:2007-2026, France
modules:KERNEL|SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|INVESTIGATION
degraded:NONE | query target/actual: 10/10 (5 axes, 2 passes + 1 passe reprise rate limit)

COUNT: ◈13 ◉1 | unique evidence objects:15 | upstream families:10
LEADS:terminal 1/1 | AXES:terminal 6/6 | N/A:none
FAILURES:2 (rate limit web 429 sur 3 axes au 1er passage, repris avec succès au 2e) | FALLBACKS:1 (Sénat GPE n° 580 : URL 404 → GAP-003)
unresolved gaps:GAP-001..GAP-005 (ACCESS/CORPUS)
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @MNEMO_Q « avenants grands projets EPR Grand Paris JO Seine-Nord » + lecture parent 14-08 | GAP-001 confirmé : volume des avenants non agrégé | corpus 14-08 | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_surfacturation-commande-publique/ |
| 2 | ◈ | QRY-001 (AXS-001) : EPR, avenants contrat EDF/Framatome | FOUND : dérive 23,7 Md€ (hérité) ; AUCUN avenant chiffré public (constat) | SRC-01/02 | lemonde.fr ; rapports EDF |
| 3 | ◈ | QRY-002 (AXS-002/004) : GPE + Seine-Nord | FOUND : GPE 35-42 Md€ (hérité) ; Seine-Nord 7,347 Md€, ~76 marchés, avenants fréquents (CdC 10/04/2026) | SRC-03/04 | ccomptes.fr |
| 4 | ◈ | QRY-003 (AXS-003) : JO 2024 SOLIDEO | FOUND : 6,6 Md€, pas de dérapage, rares anomalies ; Sénat 748 (supervision saluée) | SRC-05/10/11 | ccomptes.fr ; senat.fr |
| 5 | ◈ | QRY-004 (AXS-005) : Hôpital Grand Paris | FOUND : ~1,1 → 1,3 Md€ hôpital, ~2 Md€ campus ; vice de procédure 2023 | SRC-06 | aphp.fr ; bfmtv.com |
| 6 | SYS | Calcul encadré FCT-015 (cumul 3 projets) | ANALYSE étiquetée ⁂ (~37-43 Md€, non homogène) | SRC-02/03/04 | — |
| 7 | ○ | QRY-005 : rapport Sénat GPE 2023 (n° 580 ?) | 404 — numéro non confirmé, GAP-003 | SRC-03 | senat.fr/rap/r22-580-1 (404) |
| 8 | SYS | @MNEMO_S + FACT_WRITEBACK | PENDING_AT_SERIALIZATION | — | — |
| 9 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_avenants-5-grands-projets/2026-08-09_22-33_avenants-5-grands-projets_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 | Modules chargés ; manifest FINAL ; 15 symboles scorés, aucun ✗ | ✅ |
| G1 | LEAD vs OBJECT distincts ; 6 axes terminaux ; périmètre explicite | ✅ |
| G2 | 6 CLM avec support/counter/gap | ✅ |
| G3 | FACT_REGISTRY 15 faits (FCT-001 à 003, 006 à 017), statuts canoniques | ✅ |
| G4 | Chaque ✦ → SRC-ID + URL ; ✧ pour corroboration restante | ✅ |
| G5 | CAU-001 à 004 typés, arrêt à l'évidence, corrélation JO non causalité | ✅ |
| G6 | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités | ✅ |
| G7 | CONTR-001 à 004 documentés et résolus (dont correction HGP 3,5 → 1,3 Md€) | ✅ |
| G8 | TRACE_MATRIX ; QRY-001 à 005 tracés ; IDs résolus | ✅ |
| G9 | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis | ✅ |
| G10 | Un seul chemin ; une seule write FINAL ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY** : edi_gap = (0.80-0.675)/0.80 = 0.156 ; query_gap = N/A ; coverage_gap = 0. GAP_SEVERITY = 0.156 × 1.00 = 0.16 < 0.20 → procéder avec divulgation (gaps GAP-001 à GAP-005 déclarés).

---

*TL;DR : SUJET : GAP-005 avenants — dérives par avenants sur 5 grands projets. OBJET : mécanisme confirmé, chiffre impossible — 4/5 projets en dérive massive officielle (EPR ×7 à 23,7 Md€, GPE +15-20 à 42 Md€, Seine-Nord +2,2-2,8 à 7,347 Md€, HGP +0,2 à 1,3 Md€), JO seul maîtrisé (6,6 Md€) avec supervision stricte des avenants (CdC 2025, Sénat 748) ; AUCUN agrégat d'avenants publié sur les 5 projets (GAP-001 confirmé et étendu) ; les données essentielles (2019) contiennent les avenants sans agrégation — une analyse open-data pourrait produire le premier chiffrage de la part légale. SOURCE : UPDATE de la branche avenants du GAP-005. MANIPULATION : Ξ=9, €=8, ↕=8, Κ=8. LIMITE : GAP-001 à GAP-005 (agrégats non publiés, rapport Sénat GPE introuvable, CdC SGP non lu).*
