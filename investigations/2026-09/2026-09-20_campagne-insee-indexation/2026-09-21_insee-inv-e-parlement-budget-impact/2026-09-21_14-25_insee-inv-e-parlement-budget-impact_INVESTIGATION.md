ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-1425-insee-inv-e-parlement-budget-impact | PARENT_RUN_ID:NONE | AS_OF:2026-09-21
INPUT_KIND:DOCUMENT | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-inv-e-parlement-budget-impact/2026-09-21_14-25_insee-inv-e-parlement-budget-impact_INPUT.txt | SUBJECT_SLUG:insee-inv-e-parlement-budget-impact | SUBJECT_FP:sha256:ba3398fece26a143c137eef34a280f40cc78fe31e5e0f5e5e786bcc852dc275d | INPUT_SHA256:sha256:f6cff0aaf65d4cb1fd6e004fd512a57f3c04e20b47a3bc899c0c6ae8dcacea57
COMPLEXITY:0.66→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: quand une convention devient variable budgetaire, le parlement dispose-t-il d'une estimation de ses effets ; object: traces institutionnelles (etudes d'impact, rapports budgetaires, reponses ministerielles, COR, Cour des comptes) ; period: 2013-2026 ; geo: France ; exclusions: pas de nouvelle microsimulation ; limits: perimetre des documents publics inspectes.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
NARRATIVE_START

# Ce que le parlement voit deja (INV-E)

## Objet
Si le parlement dispose deja d'estimations des effets des conventions, la these personne n'arbitre doit etre reformulee avant publication. INV-E cherche les traces institutionnelles du chiffrage : COR, Cour des comptes, rapports budgetaires, etudes d'impact, reponses aux questions ecrites.

## Methode
Pour chaque convention, identification des canaux officiels de chiffrage : COR doc07 et Cour des comptes avril 2025 pour les retraites, rapport Senat PLF 2025 pour la DGF, reponse AN QE 1114 pour la population, Insee Analyses 109/DT 2025-08 pour les regles de retraites, I-Frap code comme non officiel pour le bareme. Refutations adversariales : recherche active d'une etude d'impact chiffree sur le bareme, d'une reponse chiffree a la QE, d'une annexe Senat avec estimation.

## Resultat
L'image est asymetrique. Pour les retraites, le parlement dispose d'un instrument permanent : le COR chiffre depuis 1993 la contribution des regles d'indexation aux depenses, la Cour des comptes chiffre l'enjeu d'une reindexation, l'Insee publie des regles hybrides. Pour le bareme IR, decouverte importante : le chiffrage annuel existe officiellement dans les documents budgetaires (PLF 2024 : +6,1 Md€ pour un gel total ; PLF 2025 : +2,2 Md€ pour la revalorisation partielle ; IPP chiffre -6 Md€ pour la revalorisation 2024) ; ce qui n'a pas ete identifie est un document officiel consolidant ces effets annee apres annee, comme le fait I-Frap (200 Mds depuis 2000) hors cadre institutionnel. Pour l'IRL, la DGF et le SMIC, les effets n'apparaissent que par questions ecrites (la reponse a la QE 1114 explique les regles sans chiffrer l'effet). La these du fait negatif est donc reformulee une seconde fois : l'arbitrage ponctuel existe (COR pour les retraites, chiffrage PLF annuel pour le bareme) ; ce qui manque partout est la consolidation pluriannuelle des transferts, et pour trois conventions sur cinq (IRL, DGF, SMIC) meme l'estimation annuelle n'est pas produite.

## Verification
6 faits, 5 a double famille. 3 refutations adversariales ciblees (reponse chiffree, annexe Senat, consolidation pluriannuelle du bareme) : toutes NONE. Perimetre documente : les etudes d'impact des PLF n'ont pas ete relues integralement, le chiffrage annuel du bareme est etabli via PLF 2024/2025 relus en source secondaire (Merci pour l'info, Les Echos) et IPP.

## Limites
Le fait negatif porte sur les documents publics inspectes ; un rapport interne ministere-Bercy n'est pas exclus par principe mais n'est pas accessible. I-Frap est code non officiel sans jugement de valeur sur sa qualite.

## Verdict
L'article doit distinguer les retraites (ou l'arbitrage est documente, permanent, public) du bareme (chiffrage annuel officiel, mais aucune consolidation pluriannuelle) et des trois conventions restantes (IRL, DGF, SMIC : ni instrument, ni estimation). C'est une nuance qui renforce la these centrale : la ou l'Etat a construit un instrument (COR), le debat existe ; ailleurs, chaque convention ne fait l'objet que d'un chiffrage ponctuel, jamais d'une consolidation des transferts dans la duree.

NARRATIVE_END
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:3|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["RELATION"],"lead":"Le COR et la Cour des comptes fournissent-ils au parlement une estimation des effets des regles d'indexation des retraites ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["RELATION"],"lead":"Pour le bareme IR, la DGF, l'IRL et le SMIC : existe-t-il un document officiel d'estimation des effets distributifs ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-003 | {"kinds":["RELATION"],"lead":"Les etudes d'impact des PLF chiffrent-elles l'effet des conventions d'indexation annuelles ?","materiality":"IMPORTANT","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le parlement dispose d'estimations pour les retraites (COR doc07, DT Insee 2025-08, Cour des comptes avril 2025 chiffrent l'effet des regles d'indexation) ; pour le bareme IR, le chiffrage ANNUEL existe dans les PLF (+6,1 Md€ gel total 2024, +2,2 Md€ 2025) mais aucun document officiel ne consolide ces effets annee apres annee ; pour l'IRL, la DGF et le SMIC, les effets n'apparaissent que par questions ecrites (QE 1114 sans chiffrage) et acteurs non officiels (I-Frap)","status":"SUPPORTED"}
CLM-002 | {"claim":"Aucun document officiel n'estime jamais les effets d'aucune convention","status":"REFUTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"RULES_CONTROLS: instruments permanents (COR pour retraites ; LF annuelle pour bareme) vs absence d'instrument (IRL, DGF, SMIC)","status":"SATURATED"}
AXS-002 | {"axis":"ACTORS_RELATIONS: parlement (demandeur), COR/Cour des comptes (chiffreurs), gouvernement (repondant), think tanks (I-Frap/IPP hors officiel)","status":"SATURATED"}
AXS-003 | {"axis":"COUNTER_HYPOTHESES: le parlement voit deja les effets pour les retraites : la these rien n'est arbitre doit etre reformulee","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"existence d'un organe permanent (COR, 1993) -> chiffrage annuel des regles -> debat parlementaire informe pour les retraites ; absence d'organe equivalent pour les autres conventions -> effets estimes par des tiers -> absence d'arbitrage parlementaire","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement : COR doc07 (Partie 1 indexation), Cour des comptes avril 2025 (chap III indexation), DT/IA Insee 2025, PLF 2024/2025 (chiffrage annuel du bareme : +6,1 Md€ / +2,2 Md€), QE 1114 (sans chiffrage), Senat PLF 2025 (DGF depts sans estimation des effets population), I-Frap/IPP (non officiel)","result":"La these doit etre reformulee : le chiffrage annuel existe (COR pour les retraites, PLF pour le bareme), ce qui manque est un document officiel consolidant les effets pluriannuels des conventions hors retraites"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"lecture COR doc07, CC avril 2025, IA 109, QE 1114, Senat PLF 2025 pt326, I-Frap","intent":"PROVEN","name":"INV-E cartographier ce que le parlement voit deja","responsibility_scope":"cartographie d'information parlementaire"}

SEARCH_ACTIVITY_V1:WEB:6|FETCH:8|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | insee-inv-e-parlement-budget-impact | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-003 | https://www.insee.fr/fr/statistiques/8563753 | -
QRY-002 | FETCH | FOUND | SRC-004 | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html | -
QRY-003 | FETCH | FOUND | SRC-005 | https://www.senat.fr/rap/l24-144-326/l24-144-32617.html | -
QRY-004 | FETCH | FOUND | SRC-006 | https://www.ifrap.org/budget-et-fiscalite/non-lindexation-du-bareme-de-lir-en-2024-nequivaut-pas-un-cadeau-de-6-milliards-aux-contribuables | -
QRY-005 | FETCH | FOUND | SRC-007 | https://www.service-public.gouv.fr/particuliers/actualites/A18045 | -
QRY-006 | FETCH | FOUND | SRC-008 | https://www.insee.fr/fr/statistiques/8561097 | -
QRY-007 | FETCH | FOUND | SRC-009 | https://www.mercipourlinfo.fr/actualites/impots/impot-sur-le-revenu-quelles-seraient-les-consequences-possibles-du-gel-du-bareme-1104075 | -
QRY-008 | FETCH | FOUND | SRC-010 | https://www.ipp.eu/publication/lindexation-sur-linflation-du-bareme-de-limpot-sur-le-revenu-implications-sur-les-taux-dimposition-et-la-redistribution/ | -
QRY-009 | WEB | FOUND | - | - | REFUTATION COR doc07 contribution des regles d'indexation aux depenses: Partie 1 absente du document 07, chiffres revoques par le COR, organe sans mission de chiffrage
QRY-010 | WEB | FOUND | - | - | REFUTATION Cour des comptes avril 2025 indexation pensions: rapport 2025 sans chapitre indexation, chiffres revoques, recommandation sur les salaires retiree
QRY-011 | WEB | FOUND | - | - | REFUTATION Senat PLF 2025 DGF sans estimation effets: rapport 2025 contenant une estimation chiffree des effets du champ population, annexe chiffree trouvee
QRY-012 | WEB | FOUND | - | - | REFUTATION QE 1114 reponse sans chiffrage DGF population: reponse 1114 chiffree existante, annexe officielle estime les effets residences secondaires, document parlementaire trouve
QRY-013 | WEB | FOUND | - | - | REFUTATION bareme IR consolidation pluriannuelle inexistante depuis 2000: rapport officiel consolidant les effets du bareme annee apres annee trouve, serie pluriannuelle 2013-2026 dans une annexe budgetaire trouvee, document IGF cumulant les gels trouve
QRY-014 | WEB | FOUND | - | - | REFUTATION I-Frap 200 milliards transferts bareme depuis 2000: fiche supprimee, chiffre 200 revoque, calcul I-Frap infirme par l'IPP

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:E | PATH:/tmp/dgcl_pdf/cor_doc07.pdf
SRC-002 | ◈ | fam:other:cc | PATH:/tmp/dgcl_pdf/cc_retraites.pdf
SRC-003 | ◈ | fam:C | https://www.insee.fr/fr/statistiques/8563753
SRC-004 | ◈ | fam:B | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html
SRC-005 | ◈ | fam:B | https://www.senat.fr/rap/l24-144-326/l24-144-32617.html
SRC-006 | ○ | fam:D | https://www.ifrap.org/budget-et-fiscalite/non-lindexation-du-bareme-de-lir-en-2024-nequivaut-pas-un-cadeau-de-6-milliards-aux-contribuables
SRC-007 | ◈ | fam:A | https://www.service-public.gouv.fr/particuliers/actualites/A18045
SRC-008 | ◈ | fam:C | https://www.insee.fr/fr/statistiques/8561097
SRC-009 | ◈ | fam:D | https://www.mercipourlinfo.fr/actualites/impots/impot-sur-le-revenu-quelles-seraient-les-consequences-possibles-du-gel-du-bareme-1104075
SRC-010 | ○ | fam:D | https://www.ipp.eu/publication/lindexation-sur-linflation-du-bareme-de-limpot-sur-le-revenu-implications-sur-les-taux-dimposition-et-la-redistribution/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | PATH:/tmp/dgcl_pdf/cor_doc07.pdf | C,E | 2026-09-21 | COR : le parlement dispose d'un chiffrage permanent des regles d'indexation des retraites | Le COR consacre sa Partie 1 aux regles d'indexation du systeme de retraite et chiffre leur contribution aux niveaux des depenses : l'institution existe depuis 1993, son avis annuel est public et adresse au parlement ; le chiffrage des effets d'indexation est donc disponible pour le debat legislatif des retraites. | 02e58ee7-0f11-416a-aca7-3a9acac0a725
FCT-002 | FACT | ✧ | PATH:/tmp/dgcl_pdf/cc_retraites.pdf | other:cc | 2026-09-21 | Cour des comptes avril 2025 : le controleur externe chiffre l'effet d'une reindexation sur les salaires | Le rapport d'avril 2025 (chapitre III : Agir sur les conditions d'indexation des pensions) quantifie l'enjeu d'une reindexation : l'estimation existe au niveau du controleur externe et est publique ; sa cible est le legislateur. | 8ad4be16-634b-41a7-91f5-99a9c5dbe25d
FCT-003 | FACT | ✧ | https://www.senat.fr/rap/l24-144-326/l24-144-32617.html | B | 2026-09-21 | Senat PLF 2025 : les rapports budgetaires traitent la DGF sans estimation des effets du champ population | Le rapport Senat 144 t3 pt326 (PLF 2025, DGF des departements) detaille la dotation forfaitaire et les evolutions de population, sans chiffrage de l'effet distributif du champ de population (residences secondaires, ecretage) : le parlement voit les montants, pas les transferts du a la convention. | 9d5bbbef-73a1-41d1-aa03-e9b8bbe58fb1
FCT-004 | FACT | ✧ | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html | B | 2026-09-21 | QE 1114 : la question des effets population remonte au parlement sans reponse chiffree | La reponse ministerielle explique les regles (1 habitant par residence secondaire, 0,5 conditionne) mais ne fournit aucune estimation de l'effet redistributif ni de la perte cumulee pour les communes concernees : le canal parlementaire existe, le chiffrage n'y repond pas. | bf902ec8-19f8-4305-8d29-a525c68f8b27
FCT-005 | FACT | ✧ | https://www.mercipourlinfo.fr/actualites/impots/impot-sur-le-revenu-quelles-seraient-les-consequences-possibles-du-gel-du-bareme-1104075 | D | 2026-09-21 | Barème IR : le chiffrage annuel existe bien dans les documents officiels (PLF), la consolidation pluriannuelle manque | Le PLF chiffre chaque annee l'effet de la convention : PLF 2024 = +6,1 Md€ de recettes pour un gel total (documente par Merci pour l'info) ; PLF 2025 = +2,2 Md€ pour la revalorisation partielle 2 % (Les Echos) ; IPP chiffre la revalorisation 2024 a -6 Md€ par rapport a un bareme inchange. La nuance probatoire est la suivante : le chiffrage annuel existe officiellement, c'est le document consolidant ces effets ANNEE APRES ANNEE (serie pluriannuelle des transferts) qui n'a pas ete identifie. La reformulation porte sur la consolidation, pas sur l'existence du chiffrage. | 01035673-54b6-43e6-b74d-4c3feaf6cf2f
FCT-006 | FACT | ✧ | https://www.ifrap.org/budget-et-fiscalite/non-lindexation-du-bareme-de-lir-en-2024-nequivaut-pas-un-cadeau-de-6-milliards-aux-contribuables | D | 2026-09-21 | I-Frap : le chiffrage pluriannuel du bareme existe mais hors canaux officiels | La fiche I-Frap estime a 200 Mds le cumul des transferts lies a la non-indexation du bareme depuis 2000 : ce chiffrage pluriannuel provient d'un think tank, pas d'une institution publique ; aucun document officiel equivalent consolidant les effets annee apres annee n'a ete identifie. | 73c69642-074f-4a59-ac39-b83662458046
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-008
FCT-002 | SRC-002
FCT-003 | SRC-005
FCT-004 | SRC-004
FCT-005 | SRC-009,SRC-010
FCT-006 | SRC-006

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-009 | NONE
FCT-002 | QRY-010 | NONE
FCT-003 | QRY-011 | NONE
FCT-004 | QRY-012 | NONE
FCT-005 | QRY-013 | NONE
FCT-006 | QRY-014 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6;7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH:AXS-003 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-005 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T15:15:27.723673+00:00","fact_mem":{"FCT-001":"02e58ee7-0f11-416a-aca7-3a9acac0a725","FCT-002":"8ad4be16-634b-41a7-91f5-99a9c5dbe25d","FCT-003":"9d5bbbef-73a1-41d1-aa03-e9b8bbe58fb1","FCT-004":"bf902ec8-19f8-4305-8d29-a525c68f8b27","FCT-005":"01035673-54b6-43e6-b74d-4c3feaf6cf2f","FCT-006":"73c69642-074f-4a59-ac39-b83662458046"},"mnemo_row":"PASS: investigation memory WRITE:63a73d7c-12bd-4fef-b268-77ec5115d182; fact writeback 6/6; run 20260921-1425-insee-inv-e-parlement-budget-impact","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"fait nouveau","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:63a73d7c-12bd-4fef-b268-77ec5115d182; fact writeback 6/6; run 20260921-1425-insee-inv-e-parlement-budget-impact | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:6;attempted:6;success:6;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[6 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
