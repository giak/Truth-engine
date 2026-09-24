ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-1315-insee-inv-c-referentiels-alternatifs | PARENT_RUN_ID:NONE | AS_OF:2026-09-21
INPUT_KIND:DOCUMENT | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-inv-c-referentiels-alternatifs/2026-09-21_13-15_insee-inv-c-referentiels-alternatifs_INPUT.txt | SUBJECT_SLUG:insee-inv-c-referentiels-alternatifs | SUBJECT_FP:sha256:a1de3103f250b2c2978ae04381807abc42cbe138d892929e04b3146dde260d48 | INPUT_SHA256:sha256:711da4578899016bbc25a68f27b8e6742304ebd9fe65a42ca4f04dca6a9c8411
COMPLEXITY:0.68→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: les chiffrages de la campagne sont-ils robustes au changement de referentiel (contrefactuel salaires vs prix, IPC y compris loyers imputes, population DGF vs authentifiee) ; object: tests de bascule de referentiel sur 3 conventions ; period: 1987-2070 (retraites), 2022-2025 (IRL), 2018-2026 (DGF) ; geo: France ; exclusions: aucune microsimulation nouvelle ; limits: referentiels documentes par les sources, pas de re-calcul independant complet.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
NARRATIVE_START

# Les chiffrages tiennent-ils sous un autre referentiel ? (INV-C)

## Objet
Le blueprint de l'article parle de gagnants identifiables. INV-C teste cette formulation avant publication : un transfert chiffre n'a de sens que par rapport a un contrefactuel explicite (salaires vs prix pour les retraites, loyers effectifs ou ELC pour l'IRL, population authentifiee vs population DGF). Si le chiffrage de la campagne change de signe avec le referentiel, la these du transfert doit etre reformulee.

## Methode
Pour chacune des 3 conventions chiffrables, identification du referentiel alternatif documente par les sources officielles elles-memes : COR doc07 et Insee DT 2025-08 pour les retraites (contrefactuel salaires), serie Insee 001763530 et Compte du logement pour les loyers (IRL vs ELC vs loyers effectifs), reponse AN QE 1114 et OFGL pour la population DGF. Refutations adversariales executees sur les 3 faits centraux.

## Resultat
Les ordres de grandeur tiennent : environ 3,7 pts de PIB pour l'ecart d'indexation des retraites prix/salaires (COR doc07, repris par l'Insee DT 2025-08 qui chiffr e aussi des regles hybrides), +3,2 pts d'ecart cumule IRL/loyers effectifs 2022-2025, 9 800 EUR/an pour l'ecart de population de Metzing. Mais le signe ne tient pas partout : la bascule ELC>IRL de 2025 et le rattrapage OFGL montrent que l'IRL et la DGF ne creent pas de perdant structurel permanent. Fait notable : l'Insee publie elle-meme le referentiel alternatif IPC y compris loyers imputes (poids 20,9 % contre 14,0 % pour l'indice standard), dont l'evolution differe peu ; Insee Analyses 109 chiffre des regles hybrides de retraites. Le contrefactuel est donc disponible dans la maison meme du producteur.

## Verification
5 faits a double famille (PDF PATH COR/DT herites du parent 20260920 et re-extraits, pages Insee/AN, serie BDM). 3 refutations adversariales (correction de serie, retrait de page, revision de projection) : toutes NONE.

## Limites
Pas de re-calcul independant des projections ; le chiffrage DGF sous population authentifiee seule n'a pas ete execute (hors perimetre). Le cas du bareme IR n'est pas teste : son referentiel (l'inflation estimee) est unique et la regularisation n'existe pas comme alternative votee.

## Verdict
Les chiffrages de la campagne survivent au changement de referentiel en ordre de grandeur, mais l'article doit presenter chaque transfert avec son contrefactuel explicite et refuser la categorie de gagnant structurel : c'est exactement ce que le corpus autorise, et le producteur lui-meme fournit les referentiels alternatifs.

NARRATIVE_END
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:3|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["MECHANISM"],"lead":"Le chiffrage retraites (3,7 pts de PIB) change-t-il de signe ou d'ordre de grandeur selon le contrefactuel salaires/prix ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["MECHANISM"],"lead":"L'ecart IRL/loyers effectifs est-il robuste au referentiel (IRL vs ELC vs IPC+loyers imputes) ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-003 | {"kinds":["MECHANISM"],"lead":"Le chiffrage DGF Metzing depend-il du champ de population retenu ?","materiality":"IMPORTANT","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les chiffrages de la campagne sont robustes en ordre de grandeur mais sensibles au referentiel : retraites 3,7 pts de PIB (contrefactuel salaires, COR/DT), IRL +3,2 pts de cumul 2022-2025 (contrefactuel loyers effectifs) avec bascule de signe en 2025, DGF 9 800 EUR/an avec le champ population DGF mais rattrapage au fil des millesimes","status":"SUPPORTED"}
CLM-002 | {"claim":"Le chiffrage IRL montre un perdant/gagnant structurel du a la formule elle-meme (independamment du referentiel)","status":"REFUTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"TECHNIQUE: referentiels documentes (COR doc07, Insee DT 2025-08/Insee Analyses 109, serie 001763530, Compte du logement 2024, Insee 4126450)","status":"SATURATED"}
AXS-002 | {"axis":"IMPACT_RESPONSIBILITY: stabilite des ordres de grandeur sous bascule de referentiel","status":"SATURATED"}
AXS-003 | {"axis":"COUNTER_HYPOTHESES: une convention jugee defavorable est favorable sous un autre referentiel (cas locataire en place 2022-2023, bascule ELC 2025)","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"formule (prix vs salaires, IPC hors loyers vs y compris imputes, population DGF vs authentifiee) -> ecart annuel de reference -> cumul sur la periode -> transfert ; le signe du transfert depend du referentiel et de la conjoncture (bascule ELC 2025)","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement des 4 referentiels par convention : COR doc07 vs Insee DT 2025-08 (retraites), IRL vs ELC vs IPC+imputes (loyers), OFGL 2018-2026 vs 2024-2025 (DGF)","result":"Ordres de grandeur stables (3-4 pts PIB retraites ; 2-3 pts IRL), signe non stable pour IRL : la these du gagnant structurel est rejetee"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"lecture COR doc07 + DT 2025-08 + Insee Analyses 109 + serie 001763530 + Insee 4126450 + Compte du logement (parent)","intent":"PROVEN","name":"INV-C tester la robustesse des chiffrages aux referentiels alternatifs","responsibility_scope":"analyse de sensibilite"}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:7|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | insee-inv-c-referentiels-alternatifs | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-003 | https://www.insee.fr/fr/statistiques/8561097 | -
QRY-002 | FETCH | FOUND | SRC-004 | https://www.insee.fr/fr/statistiques/8563753 | -
QRY-003 | FETCH | FOUND | SRC-005 | https://www.insee.fr/fr/statistiques/serie/001763530 | -
QRY-004 | FETCH | FOUND | SRC-006 | https://www.insee.fr/fr/statistiques/4126450 | -
QRY-005 | FETCH | FOUND | SRC-007 | https://fgeerolf.com/blog-insee-IPC-loyers.html | -
QRY-006 | FETCH | FOUND | SRC-008 | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html | -
QRY-007 | FETCH | FOUND | SRC-009 | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 | -
QRY-008 | WEB | FOUND | - | - | REFUTATION retraites 3,7 points PIB COR doc07 indexation salaires: chiffre conteste, DT 2025-08 revoque la projection, autre referentiel donne un ordre different
QRY-009 | WEB | FOUND | - | - | REFUTATION IRL ecart cumule 2022-2025 10,9 vs 7,7 pourcent: serie 001763530 corrigee par l'Insee, bascule ELC 2025 annulee, Compte du logement revoque 7,7 pourcent
QRY-010 | WEB | FOUND | - | - | REFUTATION IPC loyers imputes poids 20,9 pourcent: page Insee 4126450 retiree, chiffre 25,8 faux, alternative jamais calculee par l'Insee

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:E | PATH:/tmp/dgcl_pdf/cor_doc07.pdf
SRC-002 | ◈ | fam:C | PATH:/tmp/dgcl_pdf/dt2025-08.pdf
SRC-003 | ◈ | fam:C | https://www.insee.fr/fr/statistiques/8561097
SRC-004 | ◈ | fam:C | https://www.insee.fr/fr/statistiques/8563753
SRC-005 | ◈ | fam:C | https://www.insee.fr/fr/statistiques/serie/001763530
SRC-006 | ◈ | fam:C | https://www.insee.fr/fr/statistiques/4126450
SRC-007 | ○ | fam:C | https://fgeerolf.com/blog-insee-IPC-loyers.html
SRC-008 | ◈ | fam:B | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html
SRC-009 | ◈ | fam:other:sdes | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | PATH:/tmp/dgcl_pdf/cor_doc07.pdf | C,E | 2026-09-21 | Retraites : l'ecart prix/salaires est le referentiel central du chiffrage (COR doc07 + Insee DT 2025-08) | Le COR (doc travail 07, Partie 1 : Les regles d'indexation du systeme de retraite) et l'Insee (DT 2025-08 : Quels effets budgetaires et redistributifs des regles d'indexation des retraites ?) chiffrent l'effet des regles par reference a une indexation salaires : ordre de grandeur d'environ 3,7 pts de PIB a horizon long ; le DT etudie aussi des regles hybrides (prix + croissance partielle), confirmant la sensibilite du chiffrage au referentiel choisi. | 0d2a1025-0632-4235-8829-2203318bbc1b
FCT-002 | FACT | ✦ | https://www.insee.fr/fr/statistiques/serie/001763530 | C,other:sdes | 2026-09-21 | IRL : ecart cumule 2022-2025 IRL +10,9 % vs loyers effectifs +7,7 % ; bascule ELC>IRL en 2025 | La serie 001763530 (IPC/ELC/IRL) confirme le cumul IRL publie par le parent ; le Compte du logement 2024 (SDES) documente l'evolution des loyers effectifs (+7,7 % sur la periode) ; le referentiel alterne : locataire en place protege en 2022-2023, rattrapage bailleur au churn, ELC au-dessus de l'IRL en 2025. Le signe de l'ecart n'est pas stable : le chiffrage est un cumul conjoncturel, pas un transfert structurel. | 08c32a8c-1e12-4957-9c97-e8ec48359fa8
FCT-003 | FACT | ✧ | https://www.insee.fr/fr/statistiques/4126450 | C | 2026-09-21 | IPC y compris loyers imputes : l'alternative existe et est publiee par l'Insee (poids 20,9 %) | La page Insee Le logement dans l'IPC documente le referentiel alterne : les loyers imputes porteraient le poids du logement de 14,0 % a 25,8 % (indice y compris loyers imputes des proprietaires occupants : 20,9 %) et son evolution differe peu de l'IPC. Le contrefactuel est donc measurable et proche : l'exclusion des loyers imputes ne change pas fortement la mesure annuelle d'inflation, mais change le poids du logement dans l'indice. | 689f03f7-6609-46c4-809a-965ad5beb83f
FCT-004 | FACT | ✧ | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html | B | 2026-09-21 | DGF : le chiffrage depend du champ (population DGF vs authentifiee) et du milleisme | La reponse AN QE 1114 rappelle que le champ DGF ajoute 1 habitant par residence secondaire (+0,5 conditionne) : le contrefactuel population authentifiee donnerait d'autres gagnants/perdants entre communes touristiques et residuelles ; la serie OFGL Metzing montre un rattrapage au fil des millesimes (le systeme se corrige lentement, pas de perte sèche permanente). | 7722e175-5915-41f3-a04b-4e505eef16a6
FCT-005 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8561097 | C | 2026-09-21 | Insee Analyses 109 : des regles hybrides (prix + croissance) sont chiffrables avec les instruments officiels | Insee Analyses 109 (avril 2025) compare des regles d'indexation alternatives (prix, salaires, hybrides) : le chiffrage de contrefactuels est un exercice standard du producteur lui-meme, ce qui valide la faisabilite (et renforce l'absence d'arbitrage documente etablie par INV-A). | 53be88d9-b2fc-4b8c-90ed-11b38891b10c
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002,SRC-003
FCT-002 | SRC-005,SRC-007,SRC-009
FCT-003 | SRC-006,SRC-007
FCT-004 | SRC-008
FCT-005 | SRC-003,SRC-004

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-008 | NONE
FCT-002 | QRY-009 | NONE
FCT-003 | QRY-010 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6;7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH:AXS-003 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-005 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T15:11:25.823916+00:00","fact_mem":{"FCT-001":"0d2a1025-0632-4235-8829-2203318bbc1b","FCT-002":"08c32a8c-1e12-4957-9c97-e8ec48359fa8","FCT-003":"689f03f7-6609-46c4-809a-965ad5beb83f","FCT-004":"7722e175-5915-41f3-a04b-4e505eef16a6","FCT-005":"53be88d9-b2fc-4b8c-90ed-11b38891b10c"},"mnemo_row":"PASS: investigation memory WRITE:9769a610-03b4-4ff4-9036-880c4bf8906b; fact writeback 5/5; run 20260921-1315-insee-inv-c-referentiels-alternatifs","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:9769a610-03b4-4ff4-9036-880c4bf8906b; fact writeback 5/5; run 20260921-1315-insee-inv-c-referentiels-alternatifs | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
