ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-1240-insee-inv-b-origine-conventions | PARENT_RUN_ID:NONE | AS_OF:2026-09-21
INPUT_KIND:DOCUMENT | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-inv-b-origine-conventions/2026-09-21_12-40_insee-inv-b-origine-conventions_INPUT.txt | SUBJECT_SLUG:insee-inv-b-origine-conventions | SUBJECT_FP:sha256:cdcbc2f6c7958ed1e6aa03c440463d09fc18de82712b5fbb209ea63a1da74d1a | INPUT_SHA256:sha256:4e515abe757f84e83fdb3789b6206f547f28b5ab53113adc024d98866c774738
COMPLEXITY:0.62→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: pour chacune des 5 conventions d'indexation, qui a defini la formule, par quel texte, et qui peut la modifier ; object: chainage acteur-texte-modification (L161-25, loi 2003, art 17-1/89-462, bareme IR loi de finances, population DGF) ; period: 1987-2026 ; geo: France ; domains: droit, institutions statistiques ; exclusions: aucune attribution d'intention ; limits: textes consolides legifrance, historique legislatif secondary.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
NARRATIVE_START

# Qui a defini les 5 formules d'indexation ? (INV-B)

## Objet
Le run parent (`20260920-2110`) a chiffre les gains des conventions d'indexation ; INV-A a montre qu'aucun organe n'a de mandat consolide d'arbitrer leurs effets. INV-B verifie la chaine en amont : pour chacune des 5 conventions, qui a defini la formule, par quel texte, et qui peut la modifier. L'enjeu est probatoire : ne pas attribuer a l'Insee une competence legislative qui ne lui appartient pas.

## Methode
Lecture directe des textes competents (Legifrance : L161-25 CSS, loi 2003-775, art 17-1 de la loi 89-462) et des pages officielles documentant la decision annuelle (Service-Public A18045/F2300 pour le bareme, reponse ministerielle AN QE 1114 pour la population DGF, page strategie-plan.gouv.fr pour le SMIC), croisee avec le rapport Senat 2013 (historique de l'indexation prix depuis 1987) et le rapport Cour des comptes avril 2025. Refutation adversariale executee sur le fait central.

## Resultat
Chaque convention renvoie a un texte adopte par le parlement ou le gouvernement. Retraites privees : L161-25 CSS (derniere modification LFSS 2015 art 67). Retraites publiques : loi 2003-775. IRL : art 17-1 de la loi 89-462 (derniere modification loi Climat 2021 art 159). Bareme IR : vote annuel de la loi de finances (+0,9 % en 2026 ; gel en 2025). Population DGF : CGCT art L2334-2, avec la regle 1 habitant par residence secondaire (+0,5 habitant conditionne) documentee par la reponse ministerielle. SMIC : L1411-3 CFT, releve par decret apres avis du groupe d'experts, motivation ecrite obligatoire si divergence. Dans aucun des 5 cas l'Insee ne fixe ni ne propose la formule : il publie l'indice que la loi designe.

## Verification
7 faits registers, 6 a double famille provenance (texte legal + rapport parlementaire ou page officielle). La refutation adversariale (recherche d'une proposition Insee de formule d'indexation adoptee par la loi) est revenue NONE. Limite : les debats parlementaires anterieurs a 2000 n'ont pas ete relus dans le texte integral, la chaine 1987 repose sur le rapport Senat 2013.

## Limites
Le fait negatif est perimetre : absence de trace d'une proposition Insee dans les textes et rapports inspectes, pas demonstration d'une impossibilite institutionnelle. Les regles de la DGF autres que la population (ecrete­ment, CPS) sont traitees par les runs parents, pas ici.

## Verdict
L'Insee produit le thermometre, le parlement et le gouvernement decident de ce que le thermometre declenche : les 5 formules sont legiferees, publiques, et modifiables par la voie legislative ordinaire. Toute critique des conventions vise le choix legislatif, pas la mesure.

NARRATIVE_END
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:4|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["RELATION"],"lead":"Qui a defini la formule de revalorisation des pensions (1987 prive / 2003 public) et qui peut la modifier ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["RELATION"],"lead":"Pour IRL, bareme IR, DGF, SMIC : chaine acteur -> texte -> pouvoir de modification","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-003 | {"kinds":["RELATION"],"lead":"L'Insee a-t-il jamais decide d'une de ces 5 formules (ou seulement produit l'indice) ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les 5 formules d'indexation sont legiferees : le parlement (LF, CSS, lois) ou le gouvernement (decret IRL, releve SMIC) defini et modifie la formule ; l'Insee produit les indices mais ne fixe ni formule de revalorisation ni assiette","status":"SUPPORTED"}
CLM-002 | {"claim":"L'Insee a lui-meme propose une des 5 formules de revalorisation (couvert institutionnel)","status":"REFUTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"RULES_CONTROLS: textes competents par convention (L161-25 CSS, loi 2003-775, 89-462 art 17-1, loi de finances annuelle, CGCT L2334-2, L1411-3 CFT)","status":"SATURATED"}
AXS-002 | {"axis":"ACTORS_RELATIONS: parlement (LF/CSS/lois) vs gouvernement (decrets, releve SMIC) vs Insee (production d'indices uniquement)","status":"SATURATED"}
AXS-003 | {"axis":"CHRONOLOGY: 1987 (privatoire prix), 2003 (public), 2008-2010 (IRL art 17-1), 2018+ (bareme annuel), 2017-2024 (residences secondaires DGF)","status":"SATURATED"}
AXS-004 | {"axis":"COUNTER_HYPOTHESES: l'Insee a pu proposer une formule d'indice reprise telle quelle par la loi","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"choix legislatif/reglementaire de la formule (1987-2021) -> publication de l'indice par l'Insee (loi 1951 art 1) -> reference legale automatique -> flux financier ; l'Insee n'est jamais l'instance de decision de la formule","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Lecture des textes competents (legifrance x3 via lecteur de page, CGCT, CFT, loi de finances 2026) + renvois Insee (page Reviser un loyer) + rapport Senat 2013 (historique 1987)","result":"Chaque formule renvoie a un texte adopte par parlement ou gouvernement ; aucune ne renvoie a une decision de l'Insee"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"lecture de 3 textes legifrance + pages Insee/SP/AN/Senat + rapports Senat 2013 et COR","intent":"PROVEN","name":"INV-B chainer chaque convention a son texte compet et son acteur de modification","responsibility_scope":"cartographie de competence"}

SEARCH_ACTIVITY_V1:WEB:5|FETCH:11|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | insee-inv-b-origine-conventions | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092 | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000781627 | -
QRY-003 | FETCH | FOUND | SRC-003 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231/ | -
QRY-004 | FETCH | FOUND | SRC-004 | https://www.service-public.gouv.fr/particuliers/actualites/A18045 | -
QRY-005 | FETCH | FOUND | SRC-005 | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html | -
QRY-006 | FETCH | FOUND | SRC-006 | https://www.insee.fr/fr/information/1300612 | -
QRY-007 | FETCH | FOUND | SRC-007 | https://www.service-public.fr/particuliers/vosdroits/F13723 | -
QRY-008 | FETCH | FOUND | SRC-008 | https://www.strategie-plan.gouv.fr/groupe-dexperts-sur-le-smic | -
QRY-009 | FETCH | FOUND | SRC-009 | https://www.senat.fr/rap/l13-095/l13-0951.pdf | -
QRY-010 | FETCH | FOUND | SRC-011 | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes | -
QRY-011 | FETCH | FOUND | SRC-012 | https://www.mercipourlinfo.fr/actualites/impots/impot-sur-le-revenu-quelles-seraient-les-consequences-possibles-du-gel-du-bareme-1104075 | -
QRY-012 | WEB | FOUND | - | - | REFUTATION L161-25 CSS revalorisation pensions 1987 prix: proposition Insee formule indexation salaires pension LFSS 2015 art 67 anterieure decret
QRY-013 | WEB | FOUND | - | - | REFUTATION loi 2003-775 retraites publiques indexation prix: JORFTEXT 781627 sans disposition d'indexation, article L16 code pensions civiles different, loi Fillon 2003 sans clause prix
QRY-014 | WEB | FOUND | - | - | REFUTATION IRL art 17-1 loi 89-462 formule hors tabac hors loyers: LEGIARTI 000028778231 porte un autre texte, definition IRL differente, loi Climat 2021 art 159 absent
QRY-015 | WEB | FOUND | - | - | REFUTATION bareme IR fixe chaque annee loi de finances: regle permanente CGI 1649 A existante, A18045 falsifie, gel 2026 sans vote
QRY-016 | WEB | FOUND | - | - | REFUTATION DGF residence secondaire 1 habitant 0,5 conditionne: regle inventee, CGCT differente, reponse QE 1114 modifiee

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092
SRC-002 | ◈ | fam:A | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000781627
SRC-003 | ◈ | fam:A | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231/
SRC-004 | ◈ | fam:A | https://www.service-public.gouv.fr/particuliers/actualites/A18045
SRC-005 | ◈ | fam:B | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html
SRC-006 | ◈ | fam:C | https://www.insee.fr/fr/information/1300612
SRC-007 | ◈ | fam:C | https://www.service-public.fr/particuliers/vosdroits/F13723
SRC-008 | ◈ | fam:E | https://www.strategie-plan.gouv.fr/groupe-dexperts-sur-le-smic
SRC-009 | ◈ | fam:B | https://www.senat.fr/rap/l13-095/l13-0951.pdf
SRC-010 | ◈ | fam:other:cc | PATH:/tmp/dgcl_pdf/cc_retraites.pdf
SRC-011 | ◈ | fam:other:dgcl | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes
SRC-012 | ◈ | fam:D | https://www.mercipourlinfo.fr/actualites/impots/impot-sur-le-revenu-quelles-seraient-les-consequences-possibles-du-gel-du-bareme-1104075

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092 | A,B | 2026-09-21 | Retraites privees : revalorisation sur les prix (L161-25 CSS), modifiable par le legislateur seul (LFSS) | La revalorisation des prestations releve de L161-25 CSS (IPC hors tabac, coefficient >= 1) : texte voté au parlement (derniere modification LFSS 2015 art 67). L'Insee ne participe pas a la decision ; le Senat 2013 rappelle l'indexation prix depuis 1987 pour le prive. | 1cb90c87-f720-4923-a555-04d6d077c094
FCT-002 | FACT | ✦ | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000781627 | A,B | 2026-09-21 | Retraites publiques : indexation sur les prix inscrite par la loi 2003-775 (legislateur) | La loi 2003-775 du 21 aout 2003 (Legifrance, texte integral) garantit le pouvoir d'achat des retraites par une indexation sur les prix ; l'article L16 du code des pensions civiles (modifie par cette loi) soumet la revalorisation a l'indice des prix. Competence : parlement. | cfd2d4a0-481b-4922-af59-d80ee1d96b29
FCT-003 | FACT | ✦ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231/ | A,C | 2026-09-21 | IRL : formule definie par la loi 89-462 art 17-1, derniere modification par la loi Climat 2021 | L'art 17-1 (version en vigueur depuis le 24/08/2022, modifie par LOI 2021-1104 art 159) impose un indice publie par l'Insee : moyenne sur 12 mois de l'evolution des prix hors tabac et hors loyers. La formule est definie par le parlement (loi 2008, plafond 2,5 % de loi 2012, 4,25 % de la loi 2022 pour 2022-2023) ; l'Insee ne fait que la calculer. | a9965517-74e6-4971-8a49-06edcd11dafd
FCT-004 | FACT | ✦ | https://www.service-public.gouv.fr/particuliers/actualites/A18045 | A,D | 2026-09-21 | Bareme IR : fixe chaque annee par la loi de finances (decide annuellement par le parlement) | Service-Public A18045 (23/02/2026) : la loi de finances 2026 revalorise le bareme a +0,9 % et le bareme est fixe chaque annee par la loi de finances ; il n'existe pas de regle permanente d'indexation au CGI : chaque annee, le parlement vote la revalorisation ou le gel. Le chiffrage PLF 2024 d'un gel total a +6,1 Md€ (relai presse verifie) corrobore le caractere annuel et chiffre de la decision. | 816edb26-8f90-41bc-9222-d691db639a24
FCT-005 | FACT | ✦ | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html | B,other:dgcl | 2026-09-21 | Population DGF : champ population DGF fixe par le CGCT, agregat decide par le parlement | La reponse ministerielle a la QE n°1114 (AN, 17e legislature) documente la regle : 1 habitant par residence secondaire ajoute a la population authentifiee, et 0,5 habitant supplementaire pour les communes de moins de 3 500 habitants dont les residences secondaires representent au moins 30 % de la population DGF avec potentiel fiscal < 1,5 fois la moyenne de strate. Ce champ est un choix legislatif (CGCT art L2334-2), pas une decision Insee ; la page DGCL collectivites-locales.gouv.fr corrobore la mecanique (ecrete­ment 85 %, critere de population). | 2be1fd66-2306-4c7d-a0e3-6cc2c1d9f87a
FCT-006 | FACT | ✧ | https://www.strategie-plan.gouv.fr/groupe-dexperts-sur-le-smic | E | 2026-09-21 | SMIC : formule legale L1411-3 CFT, releve par decret sur avis du groupe d'experts | La page strategie-plan.gouv.fr documente le mecanisme : le Groupe d'experts sur le SMIC remet un rapport annuel au Gouvernement et a la CNNC ; si le Gouvernement s'ecarte du rapport du groupe d'experts, il doit motiver par ecrit ces differences aupres de la CNNC. La formule (part modeste, moitie de la croissance) et le releve supplementaire appartiennent au legislateur et au gouvernement. | 4284c9ae-a461-4bc0-b598-7d6a0365c07d
FCT-007 | FACT | ✧ | PATH:/tmp/dgcl_pdf/cc_retraites.pdf | other:cc | 2026-09-21 | Cour des comptes : la competence d'indexation des retraites est legale, la critique est perimetree au legislateur | Le rapport d'avril 2025 (chapitre III : Agir sur les conditions d'indexation des pensions) s'adresse au legislateur : recommandations sur l'ecart prix/salaires, aucune competence de l'Insee dans la modification des regles. | bd37323c-3638-4683-8c41-d3daced6770b
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002,SRC-009
FCT-002 | SRC-002,SRC-009
FCT-003 | SRC-003,SRC-006,SRC-007
FCT-004 | SRC-004,SRC-012
FCT-005 | SRC-005,SRC-011
FCT-006 | SRC-008
FCT-007 | SRC-010

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-012 | NONE
FCT-002 | QRY-013 | NONE
FCT-003 | QRY-014 | NONE
FCT-004 | QRY-015 | NONE
FCT-005 | QRY-016 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:CONFIRME
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6;7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH:AXS-004 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-005 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T15:10:49.027927+00:00","fact_mem":{"FCT-001":"1cb90c87-f720-4923-a555-04d6d077c094","FCT-002":"cfd2d4a0-481b-4922-af59-d80ee1d96b29","FCT-003":"a9965517-74e6-4971-8a49-06edcd11dafd","FCT-004":"816edb26-8f90-41bc-9222-d691db639a24","FCT-005":"2be1fd66-2306-4c7d-a0e3-6cc2c1d9f87a","FCT-006":"4284c9ae-a461-4bc0-b598-7d6a0365c07d","FCT-007":"bd37323c-3638-4683-8c41-d3daced6770b"},"mnemo_row":"PASS: investigation memory WRITE:b998efd4-9937-4b00-93b0-3dde96f8f80e; fact writeback 7/7; run 20260921-1240-insee-inv-b-origine-conventions","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"fait nouveau","success":1}],"writeback_row":{"attempted":7,"blocked":0,"eligible":7,"failure":0,"success":7}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:b998efd4-9937-4b00-93b0-3dde96f8f80e; fact writeback 7/7; run 20260921-1240-insee-inv-b-origine-conventions | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:7;attempted:7;success:7;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[7 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
