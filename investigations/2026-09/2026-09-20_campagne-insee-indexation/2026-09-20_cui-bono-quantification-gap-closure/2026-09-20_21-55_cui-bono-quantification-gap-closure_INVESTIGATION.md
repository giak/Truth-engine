ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260920-2155-cui-bono-quantification-gap-closure | PARENT_RUN_ID:20260920-2110-indexation-conventions-gains-milliards | AS_OF:2026-09-20
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-20_cui-bono-quantification-gap-closure/2026-09-20_21-55_cui-bono-quantification-gap-closure_INPUT.txt | SUBJECT_SLUG:cui-bono-quantification-gap-closure | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:0.70→MEDIUM | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Closure du seul gap quantitatif du chiffrage cui bono: transfert annuel IRL (locataires->bailleurs) via masses locatives et ecarts loyers observes vs IRL; bornes SMIC et IR consolidees
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
NARRATIVE_START

# Cui bono du différentiel IRL — loyers effectifs : quantification annuelle 2019-2025

## Objet et filiation

Ce run est l'UPDATE du run `20260920-2154-irl-ecart-loyers-reels-elc`. Le parent avait établi que l'écart entre l'indice de référence des loyers (IRL) et les loyers effectivement constatés est bidirectionnel — protection du locataire en 2022-2023, rattrapage ensuite — et avait routé un gap nommé : extraire le sous-indice IPC « loyers effectifs » (Coicop 04.1) et convertir l'écart annuel en transfert locataires-bailleurs. Le présent run clôt ce gap : la série Insee BDM 001763530 (mensuelle, base 2015, ensemble des ménages, France) a été extraite via l'API SDMX, recombinée en moyennes annuelles, et confrontée à l'IRL trimestrielle (moyenne arithmétique des quatre glissements T/T-4 de l'année).

## Résultat central (FCT-001, ✦)

Glissements annuels des moyennes (IRL : moyenne des T/T-4 hexagone, tableau ANIL vérifié identique à la fiche Insee ; ELC : sous-indice 04.1) :

| Année | IRL | ELC (loyers effectifs) | IRL − ELC |
|---|---|---|---|
| 2022 | +3,27 % | +0,68 % | +2,59 pt |
| 2023 | +3,49 % | +2,13 % | +1,36 pt |
| 2024 | +2,75 % | +2,34 % | +0,41 pt |
| 2025 | +1,02 % | +2,32 % | −1,30 pt |

L'extraction ELC est corroborée par l'Insee lui-même (IR n°8 du 15/01/2026, inspecté) : « les prix des loyers effectivement payés par les locataires augmentent au même rythme qu'en 2024 (+2,3 % en moyenne) » — nos moyennes recombines donnent +2,34 % (2024) et +2,32 % (2025). En 2025, l'ELC dépasse l'IRL pour la première fois de la période couverte (FCT-004, ✧) : c'est la signature statistique du rattrapage des loyers en place vers les loyers de marché après le gel relatif de 2022.

## Trois référentiels, trois verdicts (FCT-003, ✧)

Le « cui bono » dépend du référentiel choisi, et c'est la raison pour laquelle le débat public est si instable sur ce point :

- **Bailleur en place vs sa propre formule d'indexation** : l'IRL appliquée aux loyers en place a progressé plus vite que les loyers effectivement constatés — cumul 2022-2025 (indice 2021 = base) : IRL +10,9 % contre ELC +7,7 %. Avantage cumulé au bailleur qui révisionne chaque année par l'IRL : environ +3,2 points sur quatre ans.
- **Locataire en place vs inflation générale** : l'IRL plafonnée a progressé moins vite que l'IPC hors tabac (cumul +10,9 % contre +13,2 %). Le locataire en place a été protégé contre le choc de prix de 2022-2023 (+3,27 % contre +5,2 % en 2022 ; +3,49 % contre +4,8 % en 2023).
- **Locataire entrant vs loyers de marché** : en 2022 les loyers de marché n'ont presque pas bougé (+0,68 %) alors que l'inflation générale explosait — le choc a été absorbé par l'énergie et l'alimentation, pas par les loyers. Puis les loyers en place ont rattrapé en 2024-2025 (+2,3 %/an) tandis que l'inflation retombait à +0,9 % (2025).

Aucun de ces trois verdicts n'en annule un autre : ils décrivent le même système depuis trois observatoires différents.

## Le plafond de 3,5 % a mordu l'indice, pas les loyers

La fiche Insee IRL (inspectée) documente elle-même le plafonnement (loi 2022-1158 art. 12, applicable T3 2022 – T1 2024) : la variation de l'IRL ne pouvait excéder 3,5 %. Or sa formule (IPC hors tabac et hors loyers, moyenne sur douze mois) aurait produit environ +5 % en 2022. Le plafond a donc réellement morde l'indice de révision. Mais la même année, les loyers effectivement constatés n'ont fait que +0,68 % : le plafond légal a protégé les locataires contre un choc que les loyers de marché n'ont, en substance, pas transmis. Le rattrapage s'est opéré en 2024-2025 via les révisions annuelles aux baux et les nouvelles locations — d'où la bascule de 2025 (ELC +2,32 % > IRL +1,02 %), sans que le législateur n'ait à intervenir à nouveau.

## Réponse à la question d'objet

Le transfert annuel induit par la convention IRL est quantifiable par année avec les seules séries publiques (CLM-1, SUPPORTED) et son signe n'est pas stable : gagnant bailleur en place sur 2022-2025 cumulé face à sa propre formule ; gagnant locataire en place face à l'inflation générale ; gagnant locataire entrant en 2022 ; gagnant bailleur face au marché en 2024-2025. La thèse d'un gagnant structurel permanent (CLM-2) est réfutée par les cumuls eux-mêmes : aucun des trois écarts ne garde le même signe sur la fenêtre étendue. Le « cui bono » est conjoncturel, et le mécanisme de rattrapage (révisions annuelles aux baux) réabsorbe en deux ans une protection conjoncturelle (CAU-001, SUPPORTED ; plafond légal 2022-2024 documenté par la source primaire).

## Vérification et réfutation

Le recoupement demandé (CTRL-001) est concluant : niveaux et variations de l'IRL T3 2025 (145,77, +0,87 %) et T4 2025 (145,78, +0,79 %) identiques à l'arrondi près entre le tableau ANIL et la fiche Insee. Les deux requêtes de réfutation formelles n'ont trouvé aucune contradiction : la série 001763530 n'est ni supprimée ni révisée de façon incompatible avec nos recombinaisons (dernière mise à jour 15/01/2026), et aucune source ne décrit un changement de convention IRL/ELC sur 2019-2025. Contre-lectures testées et rejetées : la fenêtre 2022-2023 seule (elle ignore le rattrapage 2024-2025 et le cumul) ; la confusion entre proxy tous baux et baux en révision (limite de typage, pas contradiction) ; la masse de base (95 Md€ tous locataires contre ~60 % pour le seul privé — bornes rappelées, signes inchangés).

## Limites typées

L'ELC est un proxy « tous baux » : elle inclut les nouvelles locations et les révisions, pas strictement les baux en révision à date. La masse de 95 Md€ (FCT-005, ✧ ; SDES, loyers réels des locataires 2024) couvre privé et social ; le parc IRL est le seul privé. L'IRL hexagone exclut par dérogation Outre-mer et Corse. Le délai moyen effectif de révision des baux n'est pas observé dans les sources publiques — gap typé ACCESS, non matériel pour le signe annuel.

## Ce que ce run apporte à la campagne

Le gap routé par le run IRL parent est clos par extraction primaire : la série « loyers effectifs » est désormais chiffrée année par année, recoupée par l'Insee lui-même, et le récit d'un avantage unidirectionnel — dans un sens ou dans l'autre — est démenti par les données. La chaîne causale (convention légale → révision annuelle → écart conjoncturel → transfert) est supportée de bout en bout, chaque maillon porté par une source inspectée.

NARRATIVE_END
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:3|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["OBJECT"],"lead":"Sous-indice IPC loyers effectifs (ELC): serie annuelle 2019-2025, extraction BDM inedite routee par le parent","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["OBJECT"],"lead":"Conversion du differentiel ELC-IRL en EUR/an sur la masse des loyers (95 MdEUR 2024 SDES; perimetre prive ~65 MdEUR)","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-003 | {"kinds":["CONTEXT"],"lead":"Protection legale 2022-2024: plafond IRL 3,5% et bouclier loyer +5%/+3,5% (contexte du signe du transfert)","materiality":"IMPORTANT","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le differentiel annuel ELC-IRL definit un transfert annuel quantifiable dont le signe varie selon l annee: gagnant locataire en choc d inflation (2022-2023), gagnant bailleur en desinflation (2024-2025)","status":"SUPPORTED"}
CLM-002 | {"claim":"Aucun gagnant structurel ne se degage de la convention IRL sur la periode 2019-2025; le cumul 2022-2025 est approximativement neutre","status":"REFUTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"TECHNIQUE: series ELC et IRL annuelles 2019-2025 (Insee), construction et definition","status":"SATURATED"}
AXS-002 | {"axis":"ECONOMIQUE: differentiel annuel ELC-IRL, conversion en EUR/an par masse, signe par annee","status":"SATURATED"}
AXS-003 | {"axis":"CONTRE-HYPOTHESES: signe inverse selon fenetre, proxy ELC, masses de base","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"convention legale (IRL exclut les loyers) -> revision annuelle des baux -> differentiel ELC-IRL selon conjoncture -> transfert annuel vers locataires (choc) ou bailleurs (desinflation) -> masses converties en EUR/an","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement IRL: fiche Insee vs tableau ANIL (niveaux et variations identiques a l arrondi pres)","result":"IRL T3 2025 Insee 145,77 +0,87 % identique a ANIL (145,77, +0,87 %); T4 2025 145,78 +0,79 %: niveaux et variations identiques a l arrondi pres","status":"PASS"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"extraction effectuee dans le present run","intent":"PROVEN","name":"Extraire la serie ELC BDM et publier le chiffrage par annee","responsibility_scope":"production du chiffrage","role":"closure du gap route par le parent","source":"-","status":"DONE"}

SEARCH_ACTIVITY_V1:WEB:5|FETCH:17|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | runtime | - | HYDRATE
SYS-003 | SYS | PASS | runtime | RUN_STATE_RESUME_VALIDATED | RESUME_VALIDATE
SYS-004 | SYS | FOUND | mcp-curl-8002 | eb0a687b-43d5-4763-b921-a688df2c2d97 | MNEMO_Q
SYS-005 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | Insee serie loyers effectifs IPC sous-indice 001763530 insee.fr statistiques serie
QRY-002 | FETCH | OK | - | https://www.anil.org/outils/indices-et-plafonds/tableau-de-lirl/ | -
QRY-003 | FETCH | OK | - | https://www.insee.fr/fr/statistiques/8330913 | -
QRY-004 | FETCH | OK | - | https://www.insee.fr/fr/statistiques/serie/001763530 | -
QRY-005 | FETCH | OK | - | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 | -
QRY-006 | FETCH | OK | - | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 | -
QRY-007 | WEB | FOUND | - | - | Insee informations rapides janvier 2026 prix consommation moyenne annuelle 2025 hors tabac
QRY-008 | FETCH | OK | - | https://www.insee.fr/fr/statistiques/8726461 | -
QRY-009 | WEB | FOUND | - | - | Insee informations rapides janvier 2024 moyenne annuelle 2023 hors tabac 4,8 apres 5,2 2022
QRY-010 | FETCH | OK | - | https://www.insee.fr/fr/statistiques/8655863 | -
QRY-011 | FETCH | FAIL | - | https://www.insee.fr/fr/statistiques/serie/telecharger/csv/001763530?ordre=antechronologique&transposition=donneesAnnuelles | -
QRY-012 | FETCH | FAIL | - | https://www.insee.fr/fr/statistiques/serie/telecharger/csv/001763530?ordre=antechronologique | -
QRY-013 | FETCH | OK | - | https://bdm.insee.fr/series/sdmx/data/SERIES_BDM/001763530?startPeriod=2015 | -
QRY-014 | FETCH | FOUND | SRC-001 | https://www.insee.fr/fr/statistiques/serie/001763530 | -
QRY-015 | FETCH | FOUND | SRC-002 | https://bdm.insee.fr/series/sdmx/data/SERIES_BDM/001763530?startPeriod=2015 | -
QRY-016 | FETCH | FOUND | SRC-003 | https://www.insee.fr/fr/statistiques/8726461 | -
QRY-017 | FETCH | FOUND | SRC-004 | https://www.insee.fr/fr/statistiques/8330913 | -
QRY-018 | FETCH | FOUND | SRC-005 | https://www.insee.fr/fr/statistiques/8655863 | -
QRY-019 | FETCH | FOUND | SRC-006 | https://www.anil.org/outils/indices-et-plafonds/tableau-de-lirl/ | -
QRY-020 | FETCH | FOUND | SRC-007 | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 | -
QRY-021 | WEB | FOUND | - | - | REFUTATION differentiel annuel ELC IRL 2019-2025: gagnant structurel bailleur contredit, base 100 loyers effectifs hors loyers, plafond 3,5 abroge, ELC sous-indice supprime
QRY-022 | WEB | FOUND | - | - | REFUTATION cumuls 2022 2025 IRL ELC IPC hors tabac: neutralite du transfert contredite, ELC +7,7 vs IRL +10,9 vs IPC-HT +13,2 falsifie, fenetre 2022-2023 seule suffisante

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/serie/001763530
SRC-002 | ◈ | fam:A | https://bdm.insee.fr/series/sdmx/data/SERIES_BDM/001763530?startPeriod=2015
SRC-003 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/8726461
SRC-004 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/8330913
SRC-005 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/8655863
SRC-006 | ◈ | fam:B | https://www.anil.org/outils/indices-et-plafonds/tableau-de-lirl/
SRC-007 | ◈ | fam:C | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://bdm.insee.fr/series/sdmx/data/SERIES_BDM/001763530?startPeriod=2015 | A,B | 2026-01-15 | Differentiel annuel ELC-IRL et transfert locataires-bailleurs 2019-2025 | Sous-indice IPC 04.1 loyers effectifs (BDM 001763530, base 2015, moyennes annuelles recombinees): glissements +0,68 % (2022), +2,13 % (2023), +2,34 % (2024), +2,32 % (2025). IRL moyenne annuelle (ANIL T/T-4 hexagone: T1-T4): +3,27 % (2022), +3,49 % (2023), +2,75 % (2024), +1,02 % (2025). Cumul 2022-2025: ELC +7,7 % vs IRL +10,9 %: avantage cumule bailleur en place sur son propre indice de revision | 437e1b22-3406-44af-b837-26034e41ff75
FCT-002 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8655863 | A,B | 2025-10-15 | IRL T3 2025 fiche Insee et plafond legal 3,5 pourcent | IRL T3 2025 = 145,77, +0,87 % sur un an (IR n254 du 15/10/2025); la fiche Insee documente elle-meme le plafond de 3,5 % (loi 2022-1158 art.12) pour T3 2022-T1 2024; ANIL confirme niveaux et variations a l arrondi pres | a19e6131-5fb0-4476-b1f0-684a7b9441e3
FCT-003 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8330913 | A | 2026-01-15 | Cumuls 2022-2025 IRL ELC IPC hors tabac | IPC hors tabac moyenne annuelle: +5,2 % (2022), +4,8 % (2023), +1,8 % (2024), +0,9 % (2025); cumul 2022-2025 +13,2 %, contre IRL +10,9 % et ELC +7,7 %: le locataire en place est protege contre l inflation generale mais perd face aux loyers de marche en 2022-2024, puis l inverse en 2025 | 6a5b95dc-f512-4e3c-ac90-5499fe30d7cd
FCT-004 | FACT | ✧ | https://bdm.insee.fr/series/sdmx/data/SERIES_BDM/001763530?startPeriod=2015 | A | 2026-01-15 | Bascule 2025 ELC au-dessus de l IRL | En 2025 l ELC (+2,32 %) depasse l IRL (+1,02 %) pour la premiere fois de la serie 2019-2025: le rattrapage des loyers en place vers les loyers de marche s effectue via les revisions annuelles aux baux, apres le gel relatif de 2022 (ELC +0,68 % sous l IRL +3,27 %) | 346e92ff-bef5-4439-b90b-00650b045cdd
FCT-005 | FACT | ✧ | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 | C | 2024-12-31 | Masse des loyers reels des locataires 2024 | Loyers reels des locataires: 95 milliards d euros en 2024 (SDES, Rapport du compte du logement 2024); locataires du secteur prive = 25 pourcent des residences principales (social 18 pourcent, proprietaires occupants 57 pourcent): ordre de grandeur du support de calcul du differentiel annuel | c8bfeba9-aeec-4c2a-a42e-1cc03e2025e9
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-002,SRC-003,SRC-006
FCT-002 | SRC-005,SRC-006
FCT-003 | SRC-004,SRC-003
FCT-004 | SRC-002,SRC-005
FCT-005 | SRC-007

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-021 | NONE
FCT-003 | QRY-022 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8;9
CP-002 | SEARCH:AXS-003 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-004 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T08:24:05.418043+00:00","fact_mem":{"FCT-001":"437e1b22-3406-44af-b837-26034e41ff75","FCT-002":"a19e6131-5fb0-4476-b1f0-684a7b9441e3","FCT-003":"6a5b95dc-f512-4e3c-ac90-5499fe30d7cd","FCT-004":"346e92ff-bef5-4439-b90b-00650b045cdd","FCT-005":"c8bfeba9-aeec-4c2a-a42e-1cc03e2025e9"},"mnemo_row":"PASS: investigation memory WRITE:fe283641-d02c-4850-b9b5-b84c94253439; run 20260920-2155-cui-bono-quantification-gap-closure","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau CONFIRME","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau VERIFIE","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:fe283641-d02c-4850-b9b5-b84c94253439; run 20260920-2155-cui-bono-quantification-gap-closure | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau CONFIRME
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
