# DOUBLE-CHECK FORENSIQUE — V3 « Quand le travail ne vaut plus son temps »

**Date :** 2026-08-25  
**Audit ID :** `AUD-V3-DOUBLECHECK-001`  
**Verdict :** `HOLD_P0`

## Verdict exécutif

La thèse générale survit au fact-check. Aucun élément ne justifie un reset conceptuel.
Mais la V3 n’est pas publiable au standard forensique demandé : 7 P0 et 11 P1 restent à réparer.

## Fix queue

| ID | Priorité | Catégorie | Problème | Réparation |
|---|---|---|---|---|
| V3-P0-01 | P0 | METHODOLOGY | Les résultats 9/10, 5/10 et 7/10 correspondent au rapport interne, mais la V3 ne publie ni grille 0–5, ni liste des cas, ni annexe. « La communication sur l’IA est un mauvais proxy » généralise un panel purposif. | Publier/citer l’annexe méthodologique et écrire : « dans notre panel exploratoire, l’intensité du récit public prédit mal la profondeur opérationnelle documentée ». |
| V3-P0-02 | P0 | SOURCE_LINEAGE | Le fond est exact mais la diversification CSG/impôts/taxes n’a pas de note. | Ajouter la source officielle : cotisations 64 % en 1990 → 48 % en 2025. |
| V3-P0-03 | P0 | SOURCE_LINEAGE | La diffusion large et l’usage significatif minoritaire sont exacts mais sans source. | Ajouter BCE SAFE : 27 % aucun, 33 % très peu, 31 % modéré, 7 % significatif. |
| V3-P0-04 | P0 | SOURCE_LINEAGE | Le passage est vérifié dans le rapport n°572, mais non sourcé dans la V3. | Ajouter le rapport du Sénat et attribuer Yann Ferguson. |
| V3-P0-05 | P0 | SOURCE_LINEAGE | 76 453 salariés au 31/01/2025 est exact ; la note 26 ne contient pas le 10-K FY2025. | Ajouter le 10-K FY2025. |
| V3-P0-06 | P0 | CALIBRATION | Les agrégats ne montrent pas de dividende spectaculaire ; cela ne réfute pas des gains locaux. | Remplacer par « Ce n’est pas démontré par ces agrégats ». |
| V3-P0-07 | P0 | FIGURE_CALIBRATION | Le schéma est plus causal que la prose ; une technologie peut ne produire aucun gain net. | Écrire : « La technologie peut créer un surplus ; le contrat, la concurrence, le droit et le rapport de force déterminent sa répartition. » |
| V3-P1-01 | P1 | SOURCE_QUALITY | Le fait est exact ; Shopify republie officiellement le mémo. | Privilégier Shopify, garder TechCrunch en secondaire. |
| V3-P1-02 | P1 | SOURCE_QUALITY | Reuters rapporte que les rôles supprimés en juillet 2026 ne sont pas directement remplacés par l’IA. | Utiliser Reuters direct et intégrer ce contre-fait. |
| V3-P1-03 | P1 | SOURCE_QUALITY | Le 7 800 / 30 % / cinq ans / attrition est vérifié. | Remplacer Yahoo par Reuters/Bloomberg ou une reprise Reuters plus propre. |
| V3-P1-04 | P1 | CALIBRATION | Le 10-K prouve >900 salariés, >430 ingénieurs et hausse des coûts IA, pas à lui seul le flux de recrutement. | Écrire que l’effectif et le nombre d’ingénieurs ont augmenté, ou ajouter une source de recrutements. |
| V3-P1-05 | P1 | SOURCE_LINEAGE | A&O documente directement expertise intégrée au tech stack et licence SaaS. | Ajouter A&O Shearman primaire. |
| V3-P1-06 | P1 | CALIBRATION | Le risque est plausible, l’horizon précis ne l’est pas. | Écrire « pourrait créer à terme un déficit d’expérience ou imposer d’autres formes de formation ». |
| V3-P1-07 | P1 | CALIBRATION | Distribution aussi déterminée par contrats, marché et droit. | Élargir la formulation. |
| V3-P1-08 | P1 | FIGURE_CALIBRATION | L’écart agrégé n’est pas quantifié. | Écrire « peut sous-estimer ». |
| V3-P1-09 | P1 | FIGURE_CALIBRATION | Toutes les tâches routinières ne sont pas formatrices. | Écrire « certaines tâches routinières contribuent à former les débutants ». |
| V3-P1-10 | P1 | EDITORIAL | workflow, headcount, back-office, value billing, AI-first restent présents. | Traduire/expliciter au premier usage. |
| V3-P1-11 | P1 | SOURCE_PRECISION | Claim exact, source trop large. | Pointer directement vers Convention n°1, article 2. |

## Sources cardinales

| Source | Statut | Tier | Conclusion |
|---|---|---|---|
| Thompson / discipline du temps | VERIFIED | T2 | Task-oriented → discipline temporelle confirmé. |
| Taylor / temps standard | VERIFIED | T1 | Tâche, méthode, temps exact, chronométrage confirmés. |
| OIT Convention n°1 | VERIFIED_LINK_UPGRADE | T1 | 8 h/jour, 48 h/semaine confirmé. |
| Sécurité sociale 1945 | VERIFIED | T1 | Financement employeurs/salariés confirmé. |
| Financement social 2025 | VERIFIED_MISSING_IN_ARTICLE | T1 | Cotisations 64 % en 1990 → 48 % en 2025. |
| Billable hour / Choi | VERIFIED | T2 | Standard années 1970 + monitoring confirmé. |
| Insee AI 2025 | VERIFIED | T1 | 18 %, 15 %, 58 %, 59 % et série 2023–25 confirmés. |
| France Num 2025 | VERIFIED | T1 | 26 % usage IA ; 5 % automatisation. |
| BCE SAFE | VERIFIED_MISSING_IN_ARTICLE | T1 | 27 / 33 / 31 / 7 % confirmés. |
| Wavestone FY25/26 | VERIFIED | T1 | 17 % IA ; 72 % ; 938 € ; ~900 recrutements. |
| Wavestone Q1 26/27 | VERIFIED | T1 | 22 % IA ; 71 % ; 926 € ; budgets IA au détriment d’autres domaines. |
| Shopify headcount gate | VERIFIED_SOURCE_UPGRADE | T1 | Mémo confirmé par Shopify. |
| Duolingo effectifs/coûts IA | VERIFIED | T1 | >900 salariés ; >430 ingénieurs ; coûts IA en hausse. |
| Klarna substitution | VERIFIED_CORPORATE | T1 | 80 % chats, >700 ETP, $39m, headcount ; métriques internes. |
| IBM 7 800 | VERIFIED | T2 | Projection cinq ans, 30 %, attrition possible. |
| Microsoft restructuration | VERIFIED_SOURCE_UPGRADE | T2 | Réallocation confirmée ; RH nie remplacement direct par IA. |
| Chegg 22 % | VERIFIED | T2 | 22 % (~248), abonnés -31 %, CA -30 %. |
| Sénat « coupable idéale » | VERIFIED_MISSING_IN_ARTICLE | T1 | Citation Yann Ferguson confirmée. |
| Thomson Reuters legal market | VERIFIED | T3 | 90 % des dollars suivis à taux horaire standard. |
| TR Future of Professionals | VERIFIED | T3 | 71 % / 28 % confirmés. |
| Reuters IT Inde | VERIFIED | T2 | Pression prix/productivité + outcome/performance. |
| Harvey / A&O | VERIFIED_VENDOR | T4 | 4 000, 43 juridictions, 2–3 h/semaine ; fournisseur. |
| A&O capital logiciel | VERIFIED_MISSING_IN_ARTICLE | T1 | Expertise dans tech stack + SaaS confirmé. |
| Robots France | VERIFIED | T2 | 55 390 firmes, 598 adopteurs, effet sectoriel négatif. |
| BEI 2026/02 | VERIFIED | T2 | >12 000 firmes ; +4 % ; pas de pertes emploi CT. |
| JPMorgan 2025 | VERIFIED_CORPORATE | T1 | Capacité réinvestie ; objectif ≠ moins de headcount. |
| Salesforce FY2025 | VERIFIED_MISSING_IN_FOOTNOTE | T1 | 76 453 salariés au 31/01/2025. |
| Salesforce FY2026 / Informatica | VERIFIED | T1 | 83 334 consolidés + M&A + >5 200 Informatica. |

## Figures

- FIG 01 : cohérente ; garder le garde-fou anti-téléologie.
- FIG 02 : cohérente si la méthode du panel est publiée.
- FIG 03 : « sous-estime » → « peut sous-estimer ».
- FIG 04 : cohérente ; Microsoft doit intégrer le non-remplacement direct explicite.
- FIG 05 : solide comme modèle simplifié.
- FIG 06 : « les tâches routinières forment » → « certaines tâches routinières contribuent à former ».
- FIG 07 : cohérente avec le précédent robotique français.
- FIG 08 : blocker, « crée le gain » → « peut créer un surplus ».

## Traçabilité

Cette passe repart du SQLite inclus dans le bundle V3, qui contient ART-V003 et les huit figures. Le SQLite monté au début du double-check était antérieur à cette version.
Les URL de la bibliographie V3 sont réenregistrées dans le registre sources. Les snapshots immuables restent à constituer.

## Gate

`HOLD_P0`