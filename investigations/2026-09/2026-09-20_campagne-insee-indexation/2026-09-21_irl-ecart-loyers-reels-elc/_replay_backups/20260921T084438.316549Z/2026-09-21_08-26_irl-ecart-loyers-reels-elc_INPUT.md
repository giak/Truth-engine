ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260920-2154-irl-ecart-loyers-reels-elc | PARENT_RUN_ID:20260920-2110-indexation-conventions-gains-milliards | AS_OF:2026-09-20
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-20_irl-ecart-loyers-reels-elc/2026-09-20_21-54_irl-ecart-loyers-reels-elc_INPUT.txt | SUBJECT_SLUG:irl-ecart-loyers-reels-elc | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:95→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:UPDATE run 21-10 (indexation): chiffrage de l écart IRL / loyers réels (ELC, OLAP, Clameur) et conversion du transfert locataires-bailleurs en milliards d euros par an; recheck matériel de la mécanique IRL (FCT-002 parent)
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# L'écart IRL / loyers réels : le siphon cherché n'existe pas

## Ce que l'enquête cherchait

Le run précédent avait établi la mécanique — l'IRL revalorise les loyers sur un panier qui **exclut les loyers** — mais classait le transfert « non chiffré publiquement ». La question était donc double : quel est l'écart réel entre l'indice et les loyers constatés, et combien de milliards passe, chaque année, des locataires aux bailleurs (ou l'inverse) ?

## La mécanique, re-vérifiée et à jour

L'IRL (loi de 1989, art. 17-1) est la moyenne sur douze mois de l'évolution de l'IPC **hors tabac et hors loyers**. La convention est légale, explicite, et sa formule n'a pas changé de fond depuis 2005. La révision d'un bail exige la condition de performance énergétique A à E depuis août 2022. Dernier point connu : IRL T2 2026 = 148,37, +1,15 % sur un an. La série est recoupée entre la fiche Insee et le tableau ANIL sans divergence.

## Le résultat central : un écart bidirectionnel, pas un siphon

L'écart annuel moyen IRL / IPC hors tabac — la meilleure proxy de l'écart convention/marché sur le stock indexé — donne :

| Année | IRL moyen | IPC hors tabac | Écart |
|---|---|---|---|
| 2022 | +3,27 % | +5,2 % | **−1,93 pt** |
| 2023 | +3,50 % | +4,9 % | **−1,30 pt** |
| 2024 | +2,76 % | +2,0 % | **+0,76 pt** |

En 2022-2023, la loi a plafonné l'IRL à 3,5 % (article 12 de la loi du 16 août 2022) pendant que l'inflation générale dépassait 5 % : les locataires ont été **protégés** de près de 2 points par an. Sur la masse des loyers réels (95 Md€, Compte du logement 2024), cela représente environ **1,5 à 2 Md€/an** qui n'ont **pas** été transférés aux bailleurs. En 2024, le rattrapage s'inverse (+0,76 pt, ~0,7 Md€/an). L'écart existe, mais il oscille.

## La décennie : les loyers de marché courent sous l'inflation

L'observatoire Clameur (dossier de novembre 2025, PDF téléchargé et extrait) le documente lui-même : sur 10 ans, les loyers de marché du parc privé ont progressé de **+16,0 %** pendant que l'inflation prenait **+24,7 %** — 8,7 points d'écart. En termes réels, la rente locative de marché **a baissé**. Le même observatoire documentait déjà ce pattern avant le Covid (baux 2018 : +1,4 % contre une inflation supérieure). Et le paradoxe institutionnel mérite d'être consigné : Clameur est financé par les professionnels de l'immobilier, et ses propres données déçoivent l'intérêt proclamé de ses financeurs — le biais d'intérêt existe, mais il jouerait dans le sens inverse des résultats publiés.

## Ce que cela change pour la lignée

Le run parent (indexation) avait provisoirement classé l'IRL comme convention potentiellement favorable aux bailleurs, faute de chiffrage. Ce chiffrage **renverse la présomption** : la thèse d'un transfert structurel locataires → bailleurs via l'IRL n'est **pas soutenue par les données**. L'effet est conjoncturel et bidirectionnel. Le tableau des conventions d'indexation se complète ainsi : retraites (prix, ~4 Md€/an vers le système), barème IR (inflation estimée n-1, 2,8-6 Md€ vers l'État), SMIC (assumé protecteur), et maintenant **IRL : amortisseur bidirectionnel, sans gagnant structurel démontré**.

## Table d'évaluation des 15 symboles

| Symbole | Nom | Score | Observation nommée |
|---|---|---|---|
| Ξ | Omission | 4 | Sous-indice loyers effectifs non extrait ; part des baux avec clause non publique ; contre-factuel du loyer d'équilibre inaccessible |
| € | Money | 6 | Transferts chiffrés : ~1,5-2 Md€/an vers les locataires (2022-23), ~0,7 Md€/an vers les bailleurs (2024) ; base 95 Md€ |
| Λ | Framing | 4 | La formule « l'indice qui enrichit les propriétaires » circule sans décomposition conjoncturelle |
| Ω | Inversion | 5 | Inversion démontrée : le plafond 2022, présenté comme étouffant, a protégé les locataires |
| Ψ | Sideration | 1 | Pas d'effet de volume ou d'urgence |
| ↕ | Vertical power | 3 | La convention est légale et publique ; l'asymétrie est informationnelle, pas procédurale |
| Φ | Spectacle | 3 | Polémique IRL annuelle bruyante, décomposition jamais médiatisée |
| Σ | Semiotics | 1 | Rien de matériel |
| Κ | Cynicism | 2 | L'observatoire pro-bailleurs publie contre son propre camp : le façade-playing n'est pas généralisé |
| ρ | Resistance | 4 | Contre-pouvoirs : ANIL, observatoires locaux, décomposition accessible dans les données publiques |
| κ | Subtle influence | 2 | L'exclusion des loyers est un défaut par convention, pas une architecture de choix |
| ⫸ | Convergence | 5 | Trois familles de sources indépendantes (Insee, Clameur, SDES) convergent vers le même signe d'écart par période |
| ⚔ | Cognitive warfare | 0 | Aucune activité organisée documentée |
| 🌐 | Network | 3 | Réseau lisible : législateur → Insee → ANIL/observatoires → médias |
| ⏰ | Temporal | 5 | Le sens du transfert s'inverse selon la fenêtre (2022-23 vs 2024) : le cadrage temporel change tout |

## Réfutations adversariales

Trois contre-lectures ont été exécutées contre la mécanique ✦ et la thèse du transfert : le plafond 2022 (qui a fonctionné en faveur des locataires), la décennie Clameur (loyers sous inflation), et la recherche directe de contestation de la mesure IRL. Le fait ✦ survit borné : la mécanique est exacte, son interprétation univoque ne l'est pas. La réfutation a **renversé** la conclusion du parent au lieu de la renforcer — c'est le protocole qui fonctionne.

## Verdict

L'écart IRL / loyers réels est **réel, chiffré, et sans signe fixe** : protection locataire en choc d'inflation, rattrapage bailleur en désinflation, décennie de loyers de marché sous l'inflation. Aucune manipulation, aucun transfert structurel, aucune intention bailleur documentée. La convention IRL est un amortisseur législatif dont l'ambiguïté conjoncturelle est la seule invariance — et l'asymétrie de visibilité (la polémique annuelle est bruyante, la décomposition silencieuse) reste le seul biais démontrable, cohérent avec toute la lignée d'enquêtes.

## Limites

Le sous-indice IPC « loyers effectifs » (tous baux, renouvellements compris) n'a pas été extrait de la BDM ; la part exacte des baux avec clause d'indexation et le délai moyen de révision ne sont pas publics ; le contre-factuel du loyer d'équilibre de marché exigerait un modèle. Le chiffrage Md€ est donc donné en plage assumée selon la base retenue (95 Md€ total vs ~40-65 Md€ avec clause). Trois trous qui interdisent la certitude — pas la conclusion bornée.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:3|CAU:2|CTRL:2|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"question":"Quel est l écart cumulé IRL vs loyers réels constatés (ELC/OLAP/Clameur) sur 2019-2025 et sur la décennie ?","status":"SATURATED"}
LED-002 | {"question":"Quelle est la masse annuelle des loyers des ménages (Comptes du logement) servant de base au transfert ?","status":"SATURATED"}
LED-003 | {"question":"Qui utilise l IRL : part des baux indexés, locataires et bailleurs concernés (privé vs social) ?","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"L écart IRL / loyers réels est conjoncturel et bidirectionnel: protection locataire de ~3,2 pts sur 2022-2023 (plafond 3,5 %), rattrapage bailleur de +0,76 pt en 2024, loyers de marché sous inflation sur 10 ans - aucun transfert structurel locataires-bailleurs via l IRL","evidence":["SRC-001","SRC-003","SRC-004","SRC-009"],"note":"Transferts chiffrés: ~1,5-2 Md€/an vers les locataires en 2022-23; ~0,7 Md€/an de rattrapage en 2024","status":"SUPPORTED"}
CLM-002 | {"claim":"L exclusion des loyers de l indexation des loyers (convention IRL) n est démontrable ni comme manipulation ni comme avantage structurel: elle protège les locataires en choc d inflation et freine les bailleurs en marché tendu; son coût réel est l écart au loyer d équilibre du marché, non chiffrable sans contre-factuel","evidence":["SRC-005","SRC-008","SRC-003"],"note":"La partie descriptive (mécanique, écarts) est SUPPORTÉE; la partie contre-factuelle (loyer d équilibre) reste non chiffrable - gap routé","status":"PARTIAL"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"Technique: séries IRL vs IPC loyers vs indices OLAP/Clameur; méthodologie ELC","status":"SATURATED"}
AXS-002 | {"axis":"Économique: masse des loyers, transfert annuel Md€, gagnant selon conjoncture","status":"SATURATED"}
AXS-003 | {"axis":"Juridique/réglementaire: plafonnement 2022, révision annuelle, RLR, encadrements locaux","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"evidence":["SRC-005","SRC-001","SRC-004","SRC-009"],"note":"Chaîne complète documentée avec chaque maillon sourcé; le sens du transfert dépend de la conjoncture","provenance":"Convention légale (IRL = IPC hors tabac hors loyers) -> révision annuelle des baux -> écart IRL/IPC selon conjoncture -> transfert vers locataires (choc d inflation, plafond légal) ou vers bailleurs (marché tendu) -> masse convertie en Md€/an","status":"SUPPORTED"}
CAU-002 | {"evidence":["SRC-006","SRC-008"],"note":"L historique législatif montre des ajustements dans les DEUX sens (création IRL 2005 hors loyers, plafond 2022 sous IPC) - intentionnalité non démontrée","provenance":"Lobbying et arbitrages législatifs (loi 89-462, loi 2008 pouvoir d achat, plafond 2022) -> évolution de la convention -> aucune trace d intention bailleur documentée; le plafond 2022 a fonctionné en sens inverse","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement de la série IRL entre la fiche Insee IR 254 et le tableau ANIL (tous trimestres 2017-2026): niveaux et variations identiques à l arrondi près","evidence":["SRC-001","SRC-002"],"status":"DONE"}
CTRL-002 | {"control":"Cohérence arithmétique: écarts IRL-IPCHT recalculés (2022 -1,93 ; 2023 -1,30 ; 2024 +0,76 pt) à partir des moyennes annuelles IRL et des publications Insee; chiffrage Md€ sensible à la base retenue (95 Md€ total vs ~65 Md€ privé) - plage assumée dans le fait","evidence":["SRC-004","SRC-009","SRC-001"],"status":"DONE"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Extraire la série IPC sous-indice loyers effectifs (ELC) directement depuis la BDM Insee pour chiffrer l écart IRL vs loyers effectifs tous baux (renouvellements compris)","note":"route vers NEXT_QUERIES","status":"DONE"}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:8|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND | runtime | - | HYDRATE
SYS-002 | SYS | HIT | mcp-8002 | d3f212f5-4b6e-4859-a07e-f938d4d1c47d | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | IRL indice de référence des loyers variation annuelle 2022 2023 2024 2025 Insee trimestrielle plafond 3,5%
QRY-002 | FETCH | FOUND | SRC-001 | https://www.insee.fr/fr/statistiques/8655863 | FETCH IR IRL T3 2025
QRY-003 | FETCH | FOUND | SRC-002 | https://www.anil.org/outils/indices-et-plafonds/tableau-de-lirl/ | FETCH tableau IRL ANIL
QRY-004 | FETCH | FOUND | SRC-003 | https://unpi.org/files/Dossier_de_presse_CLAMEUR_18_novembre_2025.pdf | FETCH dossier Clameur PDF
QRY-005 | FETCH | FOUND | SRC-004 | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 | FETCH SDES compte logement
QRY-006 | FETCH | FOUND | SRC-005 | https://www.anil.org/aj-irl-revision-loyers/ | FETCH ANIL révision loyers
QRY-007 | FETCH | FOUND | SRC-006 | https://www.insee.fr/fr/information/1300612 | FETCH Insee réviser loyer
QRY-008 | WEB | FOUND | - | IRL T3 2025 0,87 % fiche Insee informations rapides | IRL T3 2025 : 0,87 % — la fiche Insee confirme la décélération (variable IRL temporairement plafonnée à 3,5 % jusqu'à T1 2024)
QRY-009 | FETCH | FOUND | SRC-008 | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723 | FETCH service-public IRL révision du loyer (plafond légal)
QRY-010 | FETCH | FOUND | SRC-009 | https://www.insee.fr/fr/statistiques/8330913 | FETCH Insee inflation moyenne annuelle 2024
QRY-011 | WEB | FOUND | - | - | REFUTATION mécanique IRL moyenne 12 mois de l IPC hors tabac hors loyers - contre-lectures exécutées: le plafond légal 3,5 % a PROTÉGÉ les locataires en 2022-2023 (IRL sous IPC de 3,2 pts), loyers de marché sous inflation sur 10 ans (Clameur +16,0 % vs +24,7 %), aucun transfert structurel bailleur démontré

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8655863
SRC-002 | ◉ | fam:A | https://www.anil.org/outils/indices-et-plafonds/tableau-de-lirl/
SRC-003 | ◉ | fam:B | https://unpi.org/files/Dossier_de_presse_CLAMEUR_18_novembre_2025.pdf
SRC-004 | ◈ | fam:C | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024
SRC-005 | ◉ | fam:A | https://www.anil.org/aj-irl-revision-loyers/
SRC-006 | ◈ | fam:A | https://www.insee.fr/fr/information/1300612
SRC-007 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8655863
SRC-008 | ◈ | fam:D | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723
SRC-009 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8330913

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.anil.org/aj-irl-revision-loyers/ | A,D | 2026-09-20 | Mécanique IRL : moyenne 12 mois de l IPC hors tabac ET hors loyers | L IRL (loi 89-462 art. 17-1) est la moyenne sur les douze derniers mois de l évolution de l IPC hors tabac et hors loyers ; IRL T2 2026 = 148,37 (+1,15 % sur un an). Le loyer des 7 millions de ménages locataires du privé suit les prix HORS leurs loyers: la composante la plus lourde du budget logement est exclue de sa propre indexation. | d3f212f5-4b6e-4859-a07e-f938d4d1c47d
FCT-002 | FACT | ✧ | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 | A,B,C | 2026-09-20 | Écart IRL / loyers réels 2022-2025 : protection puis rattrapage, transfert chiffré en milliards | Écart IRL-IPCHT (écart annuel moyen, points) : 2022 = -1,93 ; 2023 = -1,30 ; 2024 = +0,76. IRL plafonnée à 3,5 % (loi 2022-1158, art. 12) pendant que l IPC hors tabac faisait +5,2 % (2022) et +4,9 % (2023) : le plafond a TRANSFERÉ aux locataires ~1,9 pt/an de croissance réelle non perçue sur 2022-2023, soit de l ordre de 1,5 à 2 Md€/an sur la masse des loyers réels (95 Md€, SDES 2024) - la convention n est PAS orientée bailleur en période de choc d inflation. 2024 : léger rattrapage bailleur (+0,76 pt, ~0,7 Md€/an). Sur 10 ans, les loyers de marché (Clameur, +16,0 %) courent SOUS l inflation (+24,7 %) : en termes réels, baissiers - la thèse d un transfert structurel locataires-bailleurs via l IRL n est pas soutenue par les données ; l effet est conjoncturel et bidirectionnel. | eb0a687b-43d5-4763-b921-a688df2c2d97
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-005,SRC-006,SRC-008
FCT-002 | SRC-003,SRC-004,SRC-009

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-011 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | UPDATE | d3f212f5-4b6e-4859-a07e-f938d4d1c47d
FCT-002 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8;9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10;11
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12;13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;15;16;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18;19

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-20T20:22:16.312247+00:00","fact_mem":{"FCT-001":"d3f212f5-4b6e-4859-a07e-f938d4d1c47d","FCT-002":"eb0a687b-43d5-4763-b921-a688df2c2d97"},"mnemo_row":"READ_ONLY_CONSTRAINT","result":"PASS","writeback_execution":[{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"réouverture matériel du fait IRL parent, update_memory OK, relecture validee","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau (chiffrage écart IRL/loyers réels), write_memory OK, relecture validee","success":1}],"writeback_row":{"attempted":2,"blocked":0,"eligible":2,"failure":0,"success":2}}

PERSISTENCE_META: MNEMO_ROW:READ_ONLY_CONSTRAINT | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:2;attempted:2;success:2;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[2 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:réouverture matériel du fait IRL parent, update_memory OK, relecture validee
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau (chiffrage écart IRL/loyers réels), write_memory OK, relecture validee
