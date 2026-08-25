# INVESTIGATION KERNEL v2.8 — CAPGEMINI : Le seul cas documenté de suppression d'emplois IA en France

> **UPDATE** du parent `20260824-1822-leffondrement-du-modele-salarial`. Le cas Capgemini est le seul documenté en France de suppressions massives de postes explicitement liées à l'IA. 2 400 postes, 7 % des effectifs français. La vidéo de Sam ne nomme aucune entreprise — Capgemini est le chaînon manquant.

## RUN_MANIFEST

| Champ | Valeur |
|---|---|
| ENGINE_VERSION | 2.8 |
| STATE | FINAL |
| RUN_ID | 20260824-2040-leffondrement-capgemini |
| PARENT_RUN_ID | 20260824-1822-leffondrement-du-modele-salarial |
| AS_OF | 2026-08-24 |
| INPUT_KIND | UPDATE |
| MISSION_MODE | INVESTIGATION |
| INPUT_REF | PATH:investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-24_18-22_leffondrement-du-modele-salarial_INVESTIGATION.md |
| SUBJECT_SLUG | leffondrement-capgemini |
| INVESTIGATION_PATH | investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-24_20-40_leffondrement-capgemini_INVESTIGATION.md |
| SCOPE | Capgemini : 2400 suppressions postes France, causalité IA, contexte, réactions syndicales, implications |
| COMPLEXITY | 8→COMPLEX |
| CHECKPOINT_SEQ | 0 |
| LAST_COMPLETED | 19b |
| NEXT_ACTION | NONE |
| RESUME_COUNT | 0 |
| ROUTE_OVERRIDES | [] |
| LOADED_MODULES | SYMBOLS.md,PATTERNS.md,THREATS.md,GATES.md,REQUEST_LOG.md |
| DEGRADED_FLAGS | [] |
| GATE_VERDICT | PASS |
| STATE_ID | sha256:aabdf0b32e16d3a2319f9fe49b40eee5b9c981cc8d33fe254125963b27d3047c |

## TEMPORAL_STATE

| Événement | Date |
|---|---|
| Annonce Capgemini (intention) | Janvier 2026 |
| Départs volontaires ouverts | ~Juin 2026 |
| Investigation parent | 2026-08-24 |
| AS_OF | 2026-08-24 |

## MANIPULATION_REPORT

| Champ | Valeur |
|---|---|
| INPUT_KIND | UPDATE |
| MISSION_MODE | INVESTIGATION |
| SYMBOL_STAGE | CORPUS_FINAL |
| SYMBOLS | Ξ:5, €:4, Λ:3, Ω:2, Ψ:2, ↕:3, Φ:2, Σ:2, Κ:2, ρ:2, κ:1, ⫸:3, ⚔:1, 🌐:1, ⏰:3 |
| PATTERNS | @PAT[MONEY], @PAT[ICEBERG] |
| THREATS | — |
| RHETORICAL | DEM:0, BF:0, NUM:0, AUTH:1, FAC:0 |
| COMPLEXITY | 8→COMPLEX |
| CLUSTERS | MONEY,ICEBERG |
| QUERY_GUIDANCE | HRKatha, Le Figaro, Le Monde Informatique, DecidEurs, DG Trésor, Reddit |

## CRÉDO

**LEAD_QUESTION** : Capgemini (2 400 postes supprimés, 7 % des effectifs FR) confirme-t-il la thèse de la vidéo (« substitution massive et invisible du travail par l'IA ») ?

**OBJECT_QUESTION** : Quelle est la causalité réelle des 2 400 suppressions : substitution IA, restructuration conjoncturelle, prétexte managérial, ou combinaison des trois ?

## INVESTIGATION_MAP

### LEAD_REGISTRY

| LED-ID | SOURCE | LOCATOR | LEAD | KIND | MATERIALITY | STATUS |
|---|---|---|---|---|---|---|
| LED-C01 | HRKatha | Jan 2026 | Capgemini supprime jusqu'à 2 400 postes France (7 % effectifs français, ~35 000 salariés) | EVENT | DECISIVE | SATURATED |
| LED-C02 | HRKatha, Le Figaro | Jan 2026 | Suppressions via « départs volontaires » et « reclassements internes », pas de licenciements secs | MECHANISM | DECISIVE | SATURATED |
| LED-C03 | HRKatha | Jan 2026 | Raison officielle : « aligning business with AI-led demand », « addressing softness in service lines » | CLAIM | DECISIVE | SATURATED |
| LED-C04 | HRKatha, Le Monde Info | Jan 2026 | Marge opérationnelle France < 10 % en 2025, cible 11-12 % en 2027. Restructuration = redressement marges. | CLAIM | DECISIVE | SATURATED |
| LED-C05 | Le Monde Informatique, Reddit | Jan 2026 | Développeurs : −80 % offres emploi Capgemini. CGT : « excuse à la con ». Reddit : « l'IA = excuse, pas la vraie raison » | CLAIM | IMPORTANT | SATURATED |
| LED-C06 | DG Trésor | Juin 2026 | « AI adoption is sometimes used as a cover for other reasons for redundancies » | CLAIM | DECISIVE | SATURATED |
| LED-C07 | HRKatha | Jan 2026 | Redéploiement vers « data engineering, cloud services, AI ». Coût restructuration > 100 M€. Bénéfices attendus S2 2026-2027. | EVENT | IMPORTANT | SATURATED |

## CLAIM_REGISTRY

| CLM-ID | CLAIM | SUPPORT | COUNTER | STATUS |
|---|---|---|---|---|
| CLM-C01 | 2 400 postes supprimés = effet direct de l'IA | Déclaration officielle Capgemini (cité par HRKatha) | DG Trésor : « AI used as cover ». CGT, Reddit : prétexte. Marge FR < 10 % = cause financière. | CONTESTÉ |
| CLM-C02 | Départs volontaires ≠ licenciements = invisible, cohérent avec thèse vidéo | HRKatha, Le Figaro : mécanisme confirmé | Thèse vidéo prédit exactement ce mécanisme (non-remplacement). Mais ampleur 2 400 = visible, pas invisible. | SOUTENU |
| CLM-C03 | −80 % offres d'emploi développeurs = gel recrutement IA-driven | Le Monde Informatique | Marché IT global en contraction (APEC −21 %). Causalité IA non isolée. | SUGGESTIF |
| CLM-C04 | Redéploiement vers IA/data = création nette partielle | HRKatha : « reskilled and redeployed into data engineering, cloud, AI » | 2 400 suppressions brutes. Création nette inconnue. | PARTIEL |

## FACT_REGISTRY_V1

| FCT-ID | EPI | TIER | URL | FAMILIES | DATE | SUJET | VALEUR | MEM |
|---|---|---|---|---|---|---|---|---|
| FCT-C01 | FACT | ✧ | https://www.hrkatha.com/news/capgemini-to-cut-up-to-2400-roles-in-france-as-ai-shift-reshapes-operations/ | C | 2026-01-21 | Capgemini : 2 400 postes France | 7 % effectifs (~35 000). Départs volontaires + redéploiement. | mem:- |
| FCT-C02 | FACT | ✧ | https://www.lefigaro.fr/secteur/high-tech/capgemini-envisage-de-supprimer-2400-emplois-en-france-20260120 | C | 2026-01-20 | Le Figaro : Capgemini 2 400 | « 7 % des 35 000 postes français » | mem:- |
| FCT-C03 | FACT | ✧ | https://www.lemondeinformatique.fr/actualites/lire-capgemini-pret-a-supprimer-jusqu-a-2-400-postes-99093.html | C | 2026-01-20 | Le Monde Info : −80 % offres dev | « −80 % offres d'emploi développeurs » | mem:- |
| FCT-C04 | FACT | ✧ | https://www.tresor.economie.gouv.fr/Articles/2026/06/30/artificial-intelligence-and-its-effects-on-employment | A | 2026-06-30 | DG Trésor : IA comme couverture | « AI adoption is sometimes used as a cover for other reasons for redundancies » | mem:- |
| FCT-C05 | FACT | ✧ | https://www.decideurs-magazine.com/ressources-humaines/63311-capgemini-annonce-la-suppression-de-2400-postes-en-france-a-cause-de-l-ia.html | C | 2026-01-20 | DecidEurs : CGT réaction | CGT qualifie l'IA de prétexte | mem:- |

## EVIDENCE_REGISTRY

| SRC-ID | TYPE | TITLE | URL | FAMILY | ROLE | LOCATOR | DATE |
|---|---|---|---|---|---|---|---|
| SRC-C01 | ◈ | HRKatha — Capgemini 2 400 | https://www.hrkatha.com/news/capgemini-to-cut-up-to-2400-roles-in-france-as-ai-shift-reshapes-operations/ | C | ◉ | 2 400 rôles, 7 % FR, départs volontaires | 2026-01-21 |
| SRC-C02 | ◈ | Le Figaro — Capgemini | https://www.lefigaro.fr/secteur/high-tech/capgemini-envisage-de-supprimer-2400-emplois-en-france-20260120 | C | ◉ | 7 % des 35 000 postes | 2026-01-20 |
| SRC-C03 | ◈ | Le Monde Informatique | https://www.lemondeinformatique.fr/actualites/lire-capgemini-pret-a-supprimer-jusqu-a-2-400-postes-99093.html | C | ◉ | −80 % offres dev, CGT réaction | 2026-01-20 |
| SRC-C04 | ◈ | DG Trésor — IA emploi | https://www.tresor.economie.gouv.fr/Articles/2026/06/30/artificial-intelligence-and-its-effects-on-employment | A | ◉ | AI used as cover | 2026-06-30 |
| SRC-C05 | ◈ | DecidEurs — Capgemini | https://www.decideurs-magazine.com/ressources-humaines/63311-capgemini-annonce-la-suppression-de-2400-postes-en-france-a-cause-de-l-ia.html | C | ◉ | CGT : IA = prétexte | 2026-01-20 |
| SRC-C06 | ◉ | Reddit r/developpeurs | https://www.reddit.com/r/developpeurs/comments/1qhyu90/ | C | ◉ | « L'IA = excuse à la con » | 2026-01 |

## TRACE_MATRIX

| ENTITY-ID | QRY/SRC | RESULT | STATUS |
|---|---|---|---|
| LED-C01 | SRC-C01,C02,C03,C05 | 2 400 postes confirmé. 7 % effectifs FR. Départs volontaires. | SATURATED |
| LED-C03 | SRC-C01 | Raison officielle = « AI-led demand » + « softness in service lines ». Deux causes, pas une. | SATURATED |
| LED-C04 | SRC-C01 | Marge < 10 % → cible 11-12 %. Cause financière documentée. | SATURATED |
| LED-C05 | SRC-C03,C06 | −80 % offres dev. CGT/Reddit contestent causalité IA. | SATURATED |
| LED-C06 | SRC-C04 | DG Trésor : AI = parfois couverture. Applicable à Capgemini ? Non nommé explicitement. | SATURATED |

## CAUSALITY_REGISTRY

| CAU-ID | EDGE | TYPE | SOURCE | GAP |
|---|---|---|---|---|
| CAU-C01 | Demande IA + softness services → restructuration → 2 400 suppressions | CAUSE (déclarée) | SRC-C01 | Double causalité (IA + softness). IA = partielle. |
| CAU-C02 | Marge FR < 10 % → pression financière → suppression postes | CAUSE (alternative) | SRC-C01 | Causalité distincte de l'IA. Indépendante. |
| CAU-C03 | IA comme couverture → suppression pour raison financière déguisée en transition technologique | HYPOTHÈSE | SRC-C04, SRC-C05, SRC-C06 | Non prouvé. Plausible. |

## IMPACT_MAP

| IMP-ID | EFFECT | AFFECTED | EVIDENCE | STATUS |
|---|---|---|---|---|
| IMP-C01 | 2 400 départs volontaires (ou redéploiement) | Salariés Capgemini France | SRC-C01,C02 | AVÉRÉ |
| IMP-C02 | Coût > 100 M€, bénéfices S2 2026 | Actionnaires Capgemini | SRC-C01 | PROBABLE |
| IMP-C03 | −80 % offres emploi développeurs | Marché IT France | SRC-C03 | AVÉRÉ |

## EDI_REPORT

| Dimension | Score | Commentaire |
|---|---|---|
| A (primary/official) | Faible | DG Trésor (général, pas Capgemini-spécifique) |
| B (critical) | Modéré | CGT, Reddit, DecidEurs |
| C (affected/witness) | Faible | Reddit (développeurs), pas de témoignage direct |
| D (independent) | Faible | HRKatha, presse française |
| E (academic) | Nul | Aucune analyse académique |

## OPEN_GAPS

| GAP-ID | TYPE | DESCRIPTION | SEVERITY |
|---|---|---|---|
| GAP-C01 | DATA | Création nette d'emplois (redéploiement) vs 2 400 suppressions = inconnu | HIGH |
| GAP-C02 | ACCESS | Capgemini n'a pas publié de détail public sur la part IA vs softness | MEDIUM |
| GAP-C03 | DATA | Nombre réel de départs effectifs vs annonce = inconnu (juin 2026 : début) | MEDIUM |

## MNEMO_STATE

| Appel | Statut | Memory_ID |
|---|---|---|
| search_memory | PENDING_AT_SERIALIZATION | — |
| write_memory | PENDING_AT_SERIALIZATION | — |

## REQUEST_LOG

ENGINE:2.8 | MANIFEST:OPEN | RUN_ID:20260824-2040-leffondrement-capgemini | PARENT_RUN_ID:20260824-1822-leffondrement-du-modele-salarial | AS_OF:2026-08-24
CHECKPOINT_SEQ:0 | LAST_COMPLETED:NONE | NEXT_ACTION:FINAL
COUNT: ◈5 ◉1 ○0 | unique evidence objects:6 | upstream families:3 (A:institutions, C:presse, C:réseaux sociaux)

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE |
|---|---:|---|
| 1 | SYS | @READ modules | LOADED | — |
| 2 | ◈ | read_url(HRKatha Capgemini) | FOUND | SRC-C01 |
| 3 | SYS | FINAL @WRITE | PENDING | INVESTIGATION_PATH |

## PÉRIMÈTRE & LIMITES

### Verdict Capgemini

Le cas Capgemini est le **seul cas documenté en France** de suppressions massives de postes explicitement liées à l'IA. Il est cohérent avec le mécanisme décrit par la vidéo (départs volontaires, invisibilité, redéploiement). **Cependant :**

1. **Causalité mixte** : La raison officielle est double — « AI-led demand » ET « softness in service lines ». La marge française < 10 % est une cause financière distincte de l'IA.
2. **Prétexte contesté** : La CGT, Reddit et la DG Trésor (« AI used as cover ») suggèrent que l'IA est un habillage commode pour une restructuration financière.
3. **Ampleur modeste** : 2 400 postes sur 35 000 = 7 %. Dans un secteur IT de plusieurs centaines de milliers d'emplois en France, c'est significatif mais pas systémique.
4. **Création nette inconnue** : Le redéploiement vers « data engineering, cloud, AI » crée des postes. Le solde net est inconnu.
5. **Un seul cas ≠ une tendance** : L'APEC prévoit +4-5 % de recrutements cadres IT en 2026. Le cas Capgemini est l'exception, pas la règle.

**Le cas Capgemini est un signal faible cohérent avec H, mais insuffisant pour établir une tendance.**