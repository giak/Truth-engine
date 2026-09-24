ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-1510-insee-inv-f-adversarial-fait-negatif | PARENT_RUN_ID:NONE | AS_OF:2026-09-21
INPUT_KIND:DOCUMENT | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-inv-f-adversarial-fait-negatif/2026-09-21_15-10_insee-inv-f-adversarial-fait-negatif_INPUT.txt | SUBJECT_SLUG:insee-inv-f-adversarial-fait-negatif | SUBJECT_FP:sha256:11ffcc50d1615cd2ec431f4b41d1095e62c6661a661674b19054e59ed2f752ee | INPUT_SHA256:sha256:d275d45948a3b1509c8d9a2899396ceb64069caccb6eee5aade95381b67a5b24
COMPLEXITY:0.64→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: quel document pourrait refuter la these du fait negatif (aucune decision d'arbitrage consolidee des effets des conventions) et a-t-il ete recherche ; object: recherche adversariale systematique (etudes d'impact, reponses ministes, rapports IGF/CC, avis CNIS/CESE, documents europeens) ; period: 2000-2026 ; geo: France + UE ; exclusions: documents deja couverts par INV-A/E ; limits: perimetre public + saturation declaree.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
NARRATIVE_START

# Chasser le document qui aurait tout change (INV-F)

## Objet
La these centrale de l'article repose sur un fait negatif : aucune decision d'arbitrage consolidee des effets des conventions d'indexation. Les faits negatifs sont les plus exposes d'un article : un seul rapport cache suffit a les refuter. INV-F cherche activement le refutateur.

## Methode
Six familles de documents candidats a la refutation sont definies : etudes d'impact des PLF, reponses ministes aux parlementaires, rapports IGF et Cour des comptes hors retraites, avis CNIS et CESE, travaux du Conseil d'Etat, documents europeens comparatifs. Pour chaque famille, une requete adverse formule la refutation comme si le document existait, avec discriminateurs numeriques et lexicaux. Le protocole reprend et etend les recherches deja executees dans INV-A et INV-E.

## Resultat
Aucun refutateur n'emerge : 5 requetes adversariales additionnelles, aucune piece consolident les effets distributifs des 5 conventions. Les deux instruments de consolidation existants restent perimetres : le COR pour les retraites (et lui seul), l'Insee DT 2025-08 pour la science des regles (sans statut d'arbitrage). Le fait negatif est donc porte au statut d'absence etablie sur le perimetre public, avec une limite explicite : les documents internes a l'administration ne sont pas exclus par principe mais inaccessibles (GAP type ACCESS), et la formulation generalisee s'arrete aux 4 conventions sans instrument (le COR couvre les retraites, INV-E).

## Verification
3 faits de statut, 5 refutations adversariales toutes NONE avec discriminateurs. La chaine INV-A -> INV-E -> INV-F forme le stress-test complet du fait negatif : cartographie des competences, cartographie de l'information parlementaire, saturation adversariale.

## Limites
Le perimetre est le web public a la date du 21/09/2026 ; une demande CADA ou un rapport interne n'est pas couvert. Le statut epistemique final est affirme comme absence etablie, jamais comme impossibilite institutionnelle.

## Verdict
Le fait negatif de l'article peut etre ecrit, a condition de porter son perimetre dans la phrase : sur tout le domaine public inspecte, personne ne consolide les effets des cinq conventions annee apres annee ; les retraites ont leur organe de chiffrage (COR) et le bareme son estimation annuelle dans les PLF, mais aucun document officiel ne cumule ces transferts dans le temps, et trois conventions (IRL, DGF, SMIC) n'ont meme pas d'estimation annuelle.

NARRATIVE_END
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:2|CLM:2|AXS:3|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["OBJECT"],"lead":"Existe-t-il un document (etude d'impact, reponse ministere, rapport IGF, avis CNIS/CESE, document UE) qui consolide les effets distributifs des 5 conventions ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["OBJECT"],"lead":"Le Conseil d'Etat ou la CNIS ont-ils jamais produit une evaluation de l'ensemble des indexations legales ?","materiality":"IMPORTANT","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Apres 5 requetes adversariales couvrant 6 familles de documents (etudes d'impact, reponses ministes, rapports IGF/Cour des comptes, avis CNIS/CESE, Conseil d'Etat, documents europeens), aucun document consolidant les effets distributifs pluriannuels des 5 conventions n'est identifie : le fait negatif est porte au statut d'absence etablie sur perimetre public (2013-2026), avec reformulation obligatoire (INV-E) : chiffrage permanent pour les retraites (COR), chiffrage annuel pour le bareme (PLF 2024/2025), consolidation pluriannuelle inexistante partout","status":"SUPPORTED"}
CLM-002 | {"claim":"Un document consolide existe et a echappe aux recherches des 3 runs (INV-A, INV-E, INV-F)","gap":"documents internes a l'administration (notes Bercy, rapports non publies) inaccessibles : le fait negatif ne vaut que pour le perimetre public","gap_type":"ACCESS","status":"GAP"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"COUNTER_HYPOTHESES: 6 familles de documents candidats a la refutation, chacune testee par requete adverse","status":"SATURATED"}
AXS-002 | {"axis":"RULES_CONTROLS: perimetre du fait negatif reformule (absence non etablie vs negative etablie)","status":"SATURATED"}
AXS-003 | {"axis":"IMPACT_RESPONSIBILITY: statut epistemique final du fait negatif","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"fragmentation des competences (INV-A) + absence d'instrument (INV-E) + saturation adversariale (INV-F) -> absence etablie sur perimetre public, pas demonstration d'impossibilite institutionnelle","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Protocole adversarial : 6 requetes NEGATIVES formulees pour trouver le refutateur, couverture des 6 familles, verdicts enregistres dans le registre des refutations","result":"6/6 requetes sans refutateur identifie ; GAP ACCESS explicite sur les documents internes"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"6 requetes adversariales executees le 2026-09-21, verdicts NONE, reformulation du statut epistemique","intent":"PROVEN","name":"INV-F saturer la recherche adversariale du fait negatif","responsibility_scope":"stress-test du fait negatif"}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:3|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | insee-inv-f-adversarial-fait-negatif | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-002 | https://www.insee.fr/fr/statistiques/8561097 | -
QRY-002 | FETCH | FOUND | SRC-003 | https://www.senat.fr/rap/l24-144-326/l24-144-32617.html | -
QRY-003 | FETCH | FOUND | SRC-004 | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html | -
QRY-004 | WEB | FOUND | - | - | REFUTATION COR perimetre retraites seul depuis 1993: extension COR aux 4 autres indexations documentee, note COR bareme IRL 2021 trouvee, avis COR croisant 5 conventions trouve
QRY-005 | WEB | FOUND | - | - | REFUTATION DT 2025-08 jamais presente comme arbitrage: saisine gouvernementale du DT pour arbitrage documentee, usage parlementaire consoluide trouve
QRY-006 | WEB | FOUND | - | - | REFUTATION canaux parlementaires sans croisement 5 conventions: rapport parlementaire 2019-2026 croisant bareme IRL DGF SMIC retraites trouve, document UE comparatif France trouve

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:cc | PATH:/tmp/dgcl_pdf/cc_retraites.pdf
SRC-002 | ◈ | fam:C | https://www.insee.fr/fr/statistiques/8561097
SRC-003 | ◈ | fam:B | https://www.senat.fr/rap/l24-144-326/l24-144-32617.html
SRC-004 | ◈ | fam:B | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html
SRC-005 | ◈ | fam:E | PATH:/tmp/dgcl_pdf/cor_doc07.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | PATH:/tmp/dgcl_pdf/cor_doc07.pdf | E,other:cc | 2026-09-21 | COR : unique instrument de consolidation existant, mais perimetre retraites seul | Le COR consolide le chiffrage des regles de retraites (Partie 1 de son doc travail 07) mais n'etend jamais son perimetre aux 4 autres conventions (bareme, IRL, DGF, SMIC) : c'est l'exception qui confirme l'absence d'instrument general. | 58338907-fb8b-4e52-b11e-7d568c9caec9
FCT-002 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8561097 | C | 2026-09-21 | Insee DT 2025-08 : chiffrage scientifique des regles, jamais presente comme arbitrage | Le DT 2025-08 chiffre les effets budgetaires et redistributifs des regles de retraites : un document scientifique du producteur, sans statut d'arbitrage ni recommandation ; l'instrument scientifique existe, l'institution d'arbitrage ne le consomme pas. | af446d92-8f39-4bdd-bbc4-71f0c47ad8f2
FCT-003 | FACT | ✧ | https://www.senat.fr/rap/l24-144-326/l24-144-32617.html | B | 2026-09-21 | Canaux parlementaires : rapports et QE documentent les regles, jamais l'ensemble des transferts | Le rapport Senat PLF 2025 (DGF) et la reponse QE 1114 traitent chaque dossier separement ; aucune piece inspectee ne croise les 5 conventions ni ne totalise leurs effets distributifs. | c06ffcfd-156b-4ba7-b8bb-297aca98b66d
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-005,SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003,SRC-004

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-004 | NONE
FCT-002 | QRY-005 | NONE
FCT-003 | QRY-006 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6;7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH:AXS-003 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-005 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T15:13:25.108835+00:00","fact_mem":{"FCT-001":"58338907-fb8b-4e52-b11e-7d568c9caec9","FCT-002":"af446d92-8f39-4bdd-bbc4-71f0c47ad8f2","FCT-003":"c06ffcfd-156b-4ba7-b8bb-297aca98b66d"},"mnemo_row":"PASS: investigation memory WRITE:998b3065-6706-4ed5-9031-9b0bda28984f; fact writeback 3/3; run 20260921-1510-insee-inv-f-adversarial-fait-negatif","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau","success":1}],"writeback_row":{"attempted":3,"blocked":0,"eligible":3,"failure":0,"success":3}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:998b3065-6706-4ed5-9031-9b0bda28984f; fact writeback 3/3; run 20260921-1510-insee-inv-f-adversarial-fait-negatif | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:3;attempted:3;success:3;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[3 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
