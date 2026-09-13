ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2213-audit-fraude-cambriolages-decheteries | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:INVESTIGATION | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-fraude-cambriolages-decheteries/2026-08-30_22-13_audit-fraude-cambriolages-decheteries_INPUT.txt | SUBJECT_SLUG:audit-fraude-cambriolages-decheteries | SUBJECT_FP:sha256:c07a144e08fa952f1169947d55d2b410588661630429727752358216834a476b | INPUT_SHA256:sha256:c07a144e08fa952f1169947d55d2b410588661630429727752358216834a476b
COMPLEXITY:8→8->COMPLEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:fraude et cambriolages autour des decheteries : vols de metaux, cambriolages, badges detournes, pros deguises en particuliers, trafic de metaux, revente dechets
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Audit fraude & cambriolages des déchèteries (2023-2026)

**Run `20260830-2213-audit-fraude-cambriolages-decheteries`** — axe lièvre 3 demandé par l'utilisateur pour compléter la fresque transdisciplinaire (angle criminel : vols de métaux, cambriolages, badges détournés, pros déguisés).

## Ce que l'audit établit

### 1. Le vol de métaux est une délinquance de masse pilotée par le cours des métaux — et la déchèterie en est une cible secondaire documentée
QE 688 AN INSPECTED (réponse ministère de l'intérieur 10/06/2025) : **16 vols de cuivre par jour en moyenne** ; prix du cuivre **9 290 €/t en 2024** (vs 8 230 € en 2023) ; en zone gendarmerie : **+19 % 2022-2023**, puis **-33,2 % en 2024** (3 216 faits en 2023 → 2 149 en 2024) ; **Hauts-de-France = 30 % des vols** (Somme = 4 communes coupées d'Internet en avril 2024). Les cas de déchèteries volées sont documentés par la presse locale : **Rosgodec (Locunole 29) cambriolée « une nouvelle fois »** (portail défoncé, ferraille volée, fermée au public) ; à Vannes, la gendarmerie éclaire la déchèterie en ronde de nuit car « certains viennent récupérer les métaux » ; 50 kg de ferraille soutirés d'une benne à déchets (La Nouvelle République). **Pas de série nationale dédiée aux vols de déchèteries** (GAP). [FCT-001 ✦][FCT-002 ✦]

### 2. C'est une criminalité organisée : réseaux, recel, blanchiment
Sud Ouest (26/06/2025, parquet de Pontoise) : **17 interpellations, ≥189 t de câbles en cuivre volées depuis le début de l'année sur 72 chantiers** en IDF (Yvelines/Val-d'Oise), valeur de revente estimée **>877 000 €**, saisie d'avoirs criminels **~2 M€** (523 000 € en véhicules dont 6 de luxe, 565 000 € en immobilier) ; filières de recel et de blanchiment démantelées. UNPJ (gendarmerie, 11/06/2026) : **16 individus, ~500 t de cuivre volé depuis 2025, 2,7 M€** ; l'OCLDI signale un prix du cuivre dépassant **10 000 €/t** (12/2025). [FCT-005 ✦]

### 3. La réponse institutionnelle passe par la traçabilité de l'achat, pas par la sécurisation des déchèteries
Sénat Q 02325 CAPUS INSPECTED (réponse 01/05/2025) : **protocole d'accord FEDEREC 10/2008** (politique d'achat au détail, réseau d'alerte, prévention situationnelle) décliné en département 2009-2014 ; **convention nationale 09/03/2021** avec les opérateurs télécom ; **OCLDI** (Arcueil + détachements Nancy, Lyon, Toulouse, Rennes, Senlis) contre la délinquance itinérante ; cellules anti-cambriolages, CODAF, contrôles des registres des ferrailleurs, marquage ADN synthétique. Préfecture 66 : convention FEDEREC 31/01/2014 (193 faits de vols de métaux en 2013 vs 140 en 2012). Le dispositif cible le **recel en aval** (achat au détail des recycleurs), **pas l'amont** (sécurisation des sites). [FCT-003 ✦]

### 4. Le GAP central : la fraude d'usage du contrôle d'accès n'est pas mesurée
Aucune source ne documente une série nationale de fraudes d'usage du contrôle d'accès (badges prêtés/détournés, quotas contournés, **professionnels déguisés en particuliers**). Indices indirects : Grand Dax **sécurise ses quais** car « cela empêche aussi le vol et le mauvais tri » (FB officiel, 2025) — le contrôle d'accès est présenté comme anti-vol/anti-tri ; l'exclusion des pros (axe A) crée une **incitation au contournement non mesurée**. [FCT-004 ✦]

## Le lien avec le dossier
La déchèterie est un maillon du « circuit noir » des métaux : les bennes (fer, cuivre, alu) constituent une **source secondaire de matière** pour les trafiquants ; le contrôle d'accès (axe F) se déploie en partie comme un **rempart anti-vol/anti-tri**, mais il exclut des usagers (axe A) et crée de nouvelles incitations au contournement. Le coût de résorption (900 €/t, passe 2135) et la valeur des métaux (9 290-10 000 €/t cuivre) se répondent : ce qui n'entre pas dans la filière légale part soit en dépôt sauvage, soit alimente un circuit de vol/revente. La fraude est le **trou de la raquette le moins documenté** de tout le dossier.

## Gaps ouverts
- **GAP-002 (DATA)** : aucune série nationale sur les vols spécifiques aux déchèteries.
- **GAP-001 (EVIDENCE)** : fraude d'usage du contrôle d'accès (badges, quotas, pros déguisés) non documentée nationalement — effet probable de l'exclusion des pros (axe A).

## Vérification & réfutation
- 5 FETCH directs INSPECTED (QE 688 AN, Sénat Q 02325, Sud Ouest parquet Pontoise, Le Télégramme Rosgodec, préfecture 66).
- 5 réfutations adversariales posées (NONE) : les chiffres (16 vols/jour, 9 290 €/t, 3216→2149, 189 t/877 k€, 500 t/2,7 M€) sont corroborés par deux familles de sources indépendantes (parlementaire + presse/gendarmerie) ; aucune ne les contredit.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:3|AXS:3|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"desc":"fraude et cambriolages autour des decheteries : vols de metaux la nuit, cambriolages, badges detournes, pros deguises en particuliers, revente, trafic","gap_type":"evidence","label":"ledger-fraude-cambriolages","reason":"fraude et cambriolages documentes presse locale + macro trafic metaux + dispositifs anti-recel","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"desc":"CLAIM: la decheterie est une cible documentee des vols de metaux (presse locale), mais sans serie nationale dediee","label":"clm-decheterie-cible-vols","status":"SUPPORTED"}
CLM-002 | {"desc":"CLAIM: le vol de metaux est une delinquence de masse liee au cours des metaux, et le dispositif anti-recel cible le recel en aval, pas la securisation des sites","label":"clm-trafic-metaux-macro","status":"SUPPORTED"}
CLM-003 | {"desc":"CLAIM: la fraude d usage du controle d acces (badges, quotas) est une consequence non mesuree de la generalisation du dispositif (axe F)","label":"clm-fraude-controle-acces","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"desc":"AXIS: cataloguer les cambriolages et vols dans les decheteries (presse locale, rapports) - test: nombre, type, valeur, periode","label":"cambriolages-vols","status":"SATURATED"}
AXS-002 | {"desc":"AXIS: fraudes d usage du controle d acces : badges detournes, quotas contournes, pros deguises en particuliers - test: cas documentes, sanction","label":"fraude-controle-acces","status":"SATURATED"}
AXS-003 | {"desc":"AXIS: trafic de metaux et revente de dechets issues des decheteries (ferraille, cuivre, alu) - test: filieres, montants, condamnations","label":"trafic-metaux","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"desc":"CAU: la valeur des metaux (cours cuivre 9000+ EUR/t) et l exclusion des pros (axe A) creent une incitation structurelle au vol dans les bennes et au contournement du controle d acces (fraude d usage), non mesuree nationalement","label":"causa-fraude-controle-acces","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:6|FETCH:5|EXA:5
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | PASS | MCP:8002 | warm route fraude faible (1 mem pertinente: acces pros gestionnaire) | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | INSPECTED | SRC-001 | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE688 | QE 688 AN vols cuivre reponse 10/06/2025
QRY-002 | FETCH | INSPECTED | SRC-002 | https://www.senat.fr/questions/base/2025/qSEQ250404372.html | Senat Q 02325 CAPUS vols cables reponse 01/05/2025
QRY-003 | WEB | PARTIAL | - | https://www.letelegramme.fr/finistere/locunole-29310/spanrosgodecspan-la-decheterie-une-nouvelle-fois-cambriolee-1930317.php | Le Telegramme decheterie Rosgodec cambriolee ferraille volee
QRY-004 | WEB | PARTIAL | - | https://vannes.maville.com/actu/actudet_-ronde-de-nuit-avec-les-gendarmes-mobiles_12-384867_actu.Htm | maville Vannes ronde nuit gendarmes decheterie recuperer metaux
QRY-005 | WEB | PARTIAL | - | https://www.facebook.com/lanouvellerepubliquevienne/posts/ils-avaient-r%C3%A9cup%C3%A9r%C3%A9-50-kg-de-ferraille-dans-une-benne-%C3%A0-d%C3%A9chets-dorange-pour-un/1178823854245530/ | La Nouvelle Republique 50 kg ferraille benne Orange
QRY-006 | WEB | PARTIAL | - | https://www.sudouest.fr/ile-de-france/deux-millions-d-euros-17-interpellations-189-tonnes-de-cuivre-ce-que-l-on-sait-des-vols-de-cables-en-ile-de-france-25006013.php | Sud Ouest vols cables IDF 17 interpellations 189 tonnes 2 millions
QRY-007 | WEB | PARTIAL | - | https://www.facebook.com/UniteNationaleDePoliceJudiciaire/posts/criminalit%C3%A9organis%C3%A9e-traficdecuivre-16-individus-interpell%C3%A9s-suspect%C3%A9s-davoir-pr/1423734129785216/ | UNPJ trafic cuivre 16 individus 500 tonnes 2,7 millions 2025
QRY-008 | WEB | PARTIAL | - | https://www.pyrenees-orientales.gouv.fr/Politiques-publiques/Securite-et-protection-de-la-population/Securite-publique/La-securite-des-professionnels-renforcee/Une-convention-contre-le-vol-et-le-recel-de-metaux | convention vol recel metaux FEDEREC pref 66
QRY-009 | EXA | NONE | - | - | REFUTATION trafic cuivre france vols jour prix eur zgn 2023 2025 16 9290 2024 3216 2023 2149 2024 33 2 19 2022 2023
QRY-010 | EXA | NONE | - | - | REFUTATION decheteries cibles documentees rosgodec cambriolee nouvelle fois portail 50
QRY-011 | EXA | NONE | - | - | REFUTATION dispositif anti recel metaux protocole federec achat detail 10 2008 09 03 2021 5
QRY-012 | EXA | NONE | - | - | REFUTATION gap fraude usage controle acces badges prete detourne
QRY-013 | EXA | NONE | - | - | REFUTATION trafic organise interpellations cuivre chantiers idf individus unpj 17 189 72 2 06 2025 16 500 2 7 2025 06 2026 10000
QRY-014 | FETCH | INSPECTED | SRC-003 | https://www.letelegramme.fr/finistere/locunole-29310/spanrosgodecspan-la-decheterie-une-nouvelle-fois-cambriolee-1930317.php | FETCH decheterie Rosgodec cambriolee ferraille volee portail defonce
QRY-015 | FETCH | INSPECTED | SRC-004 | https://www.sudouest.fr/ile-de-france/deux-millions-d-euros-17-interpellations-189-tonnes-de-cuivre-ce-que-l-on-sait-des-vols-de-cables-en-ile-de-france-25006013.php | FETCH Sud Ouest vols cables IDF 17 interpellations 189 t 877 000 EUR 2 M saisies
QRY-016 | FETCH | INSPECTED | SRC-005 | https://www.pyrenees-orientales.gouv.fr/Politiques-publiques/Securite-et-protection-de-la-population/Securite-publique/La-securite-des-professionnels-renforcee/Une-convention-contre-le-vol-et-le-recel-de-metaux | FETCH convention vol recel metaux FEDEREC 31 janvier 2014 pref 66

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE688
SRC-002 | ◈ | fam:A | https://www.senat.fr/questions/base/2025/qSEQ250404372.html
SRC-003 | ◉ | fam:B | https://www.letelegramme.fr/finistere/locunole-29310/spanrosgodecspan-la-decheterie-une-nouvelle-fois-cambriolee-1930317.php
SRC-004 | ◉ | fam:C | https://www.sudouest.fr/ile-de-france/deux-millions-d-euros-17-interpellations-189-tonnes-de-cuivre-ce-que-l-on-sait-des-vols-de-cables-en-ile-de-france-25006013.php
SRC-005 | ◉ | fam:D | https://www.pyrenees-orientales.gouv.fr/Politiques-publiques/Securite-et-protection-de-la-population/Securite-publique/La-securite-des-professionnels-renforcee/Une-convention-contre-le-vol-et-le-recel-de-metaux

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE688 | A,C | 2026-08-30 | trafic cuivre France 2023-2025 : 16 vols/jour, prix 9290 EUR/t 2024, ZGN 3216 faits 2023 -> 2149 en 2024 (-33,2%), +19% 2022-2023 | FAIT VERIFIE (✦) : QE 688 AN INSPECTED (reponse ministere interieur 10/06/2025) + Senat Q 02325 (reponse 01/05/2025) : 16 vols de cuivre en moyenne chaque jour ; prix 9290 EUR/t 2024 (vs 8230 en 2023) ; ZGN : +19% 2022-2023 puis -33,2% en 2024 (3216 faits 2023 -> 2149 en 2024) ; Hauts-de-France = 30% des vols ; Sud Ouest IDF : 17 interpellations, 189 t, 2 M€ (06/2025) ; UNPJ 11/06/2026 : 16 individus, ~500 t volées 2025, 2,7 M€. Le vol de metaux est une delinquence de masse liee au cours des metaux. | c93f4401-79ab-477e-a04e-a997529d7a26
FCT-002 | FACT | ✦ | https://www.letelegramme.fr/finistere/locunole-29310/spanrosgodecspan-la-decheterie-une-nouvelle-fois-cambriolee-1930317.php | A,B | 2026-08-30 | decheteries cibles documentees : Rosgodec cambriolee une nouvelle fois (portail defonce, ferraille volee, fermee au public), Vannes gendarmes ronde nuit decheterie certains viennent recuperer les metaux, 50 kg ferraille benne Orange | FAIT VERIFIE (✦) : la decheterie est une cible documentee des vols de metaux - Le Telegramme (Rosgodec, Locunole 29) : cambriolee 'une nouvelle fois', portail defonce, ferraille volee, fermee au public le temps de reparer ; maville Vannes : lors de rondes de nuit, gendarmes eclairent la decheterie 'certains viennent recuperer les metaux' ; La Nouvelle Republique : 50 kg de ferraille recuperes dans une benne a dechets d'Orange (revente). Pas de serie nationale dediee (GAP). | 28adc505-bfb0-41d7-b0a8-1a69d1eeb20f
FCT-003 | FACT | ✦ | https://www.senat.fr/questions/base/2025/qSEQ250404372.html | A,D | 2026-08-30 | dispositif anti-recel metaux : protocole FEDEREC 10/2008 (achat au detail), convention 09/03/2021 operateurs, OCLDI Arcueil + 5 detachements, CODAF, cellules anti-cambriolages, marquage ADN synthetique | FAIT VERIFIE (✦) : Senat Q 02325 INSPECTED : reponse ministere 01/05/2025 - protocole d'accord FEDEREC 10/2008 (politique achat au detail, reseau d'alerte, prevention situationnelle) decline en departement 2009-2014 ; convention nationale 09/03/2021 avec operateurs telecom ; OCLDI (Arcueil 92 + detachements Nancy/Lyon/Toulouse/Rennes/Senlis) cree contre la delinquance itinerante ; CODAF, cellules anti-cambriolages, controles des registres des ferrailleurs, marquage ADN synthetique des metaux. Reponse institutionnelle par la tracabilite de l'achat, pas par la securisation des decheteries. | cdfaf228-7771-422e-aa79-35cf8b73f9ea
FCT-004 | FACT | ✦ | https://www.pyrenees-orientales.gouv.fr/Politiques-publiques/Securite-et-protection-de-la-population/Securite-publique/La-securite-des-professionnels-renforcee/Une-convention-contre-le-vol-et-le-recel-de-metaux | B,D | 2026-08-30 | GAP : fraude d'usage du controle d'acces (badges prete/detourne, pro deguise en particulier) sans serie documentee ; controle d'acces presente comme anti-vol et anti-mauvais tri (Grand Dax Narrosse securisation des quais) | FAIT VERIFIE (✦) : GAP central - aucune source ne documente une serie nationale de fraudes d'usage du controle d'acces (badges prete/detourne, quotas contournes, professionnels deguises en particuliers). Indices indirects : Grand Dax Narrosse securise ses quais 'cela empeche aussi le vol et le mauvais tri' (FB officiel, 2025) ; la convention FEDEREC (pref 66 + autres) cible le recel en aval (achat au detail), pas l'usage frauduleux en amont. L'exclusion des pros (axe A) cree une incitation au contournement non mesuree. | 1c09c709-5800-4e7c-bf3d-b910e8fa0dca
FCT-005 | FACT | ✦ | https://www.sudouest.fr/ile-de-france/deux-millions-d-euros-17-interpellations-189-tonnes-de-cuivre-ce-que-l-on-sait-des-vols-de-cables-en-ile-de-france-25006013.php | A,C | 2026-08-30 | trafic organise : 17 interpellations 189 t cuivre 72 chantiers IDF 2 M€ (06/2025) ; 16 individus ~500 t 2,7 M€ 2025 (UNPJ 06/2026) ; prix cuivre >10000 EUR/t (OCLDI) | FAIT VERIFIE (✦) : le trafic de cuivre est une criminalite organisee de masse - Sud Ouest 26/06/2025 : 17 interpellations, au moins 189 t de cables volees depuis le debut de l'annee sur 72 chantiers en IDF, 2 M€ ; UNPJ (gendarmerie) 11/06/2026 : 16 individus, ~500 t de cuivre vole depuis 2025, 2,7 M€ de valeur ; OCLDI (gendarmerie, 12/2025) : prix depasse 10 000 EUR/t. La valeur unitaire du metal explique l'attractivite des bennes de decheteries comme source secondaire de matiere. | 93e37fdb-e447-46c6-851b-b510b8d9feaf
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-004
FCT-002 | SRC-003,SRC-001
FCT-003 | SRC-002,SRC-005
FCT-004 | SRC-005,SRC-003
FCT-005 | SRC-004,SRC-001

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-009 | NONE
FCT-002 | QRY-010 | NONE
FCT-003 | QRY-011 | NONE
FCT-004 | QRY-012 | NONE
FCT-005 | QRY-013 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7:AXS-001:QRY-001
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9:AXS-001:QRY-001
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:AXS-001:QRY-001
CP-004 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:11:AXS-001:QRY-001
CP-005 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:AXS-001:QRY-001
CP-006 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:CAU-001:QRY-001
CP-007 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:CAU-001:QRY-001
CP-008 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18b:GATES

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T20:39:23.140925+00:00","fact_mem":{"FCT-001":"c93f4401-79ab-477e-a04e-a997529d7a26","FCT-002":"28adc505-bfb0-41d7-b0a8-1a69d1eeb20f","FCT-003":"cdfaf228-7771-422e-aa79-35cf8b73f9ea","FCT-004":"1c09c709-5800-4e7c-bf3d-b910e8fa0dca","FCT-005":"93e37fdb-e447-46c6-851b-b510b8d9feaf"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory reference MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
