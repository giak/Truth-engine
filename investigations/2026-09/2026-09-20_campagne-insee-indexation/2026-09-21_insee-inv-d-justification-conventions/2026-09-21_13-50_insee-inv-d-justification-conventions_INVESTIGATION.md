ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-1350-insee-inv-d-justification-conventions | PARENT_RUN_ID:NONE | AS_OF:2026-09-21
INPUT_KIND:DOCUMENT | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-inv-d-justification-conventions/2026-09-21_13-50_insee-inv-d-justification-conventions_INPUT.txt | SUBJECT_SLUG:insee-inv-d-justification-conventions | SUBJECT_FP:sha256:b00e3e68e952bccab3b0340f0caa1bf840d4693a251161a614d2bbd8a99771aa | INPUT_SHA256:sha256:a93c2b0a596190d67fa9ecbfab09cbafb1f87ecd9ab241ab1e2a6bc5d2e90f8e
COMPLEXITY:0.65→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: chaque convention a-t-elle une justification methodologique documentee qui la rend rationnelle (steelman) ; object: objectifs, contraintes europeennes, coherence d'ensemble des 5 formules ; period: 1998-2026 ; geo: France + cadre europeen ; exclusions: aucune evaluation morale ; limits: justifications relevees dans les sources inspectees, pas d'interviews.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
NARRATIVE_START

# Pourquoi ces formules ? Le steelman des conventions (INV-D)

## Objet
Un article qui presente des conventions defavorables sans exposer leur justification ferait exactement ce qu'il denonce : chiffrer a moitie. INV-D documente le steelman de chacune des 5 conventions, puis teste sa solidite.

## Methode
Pour chaque convention, recherche de la justification dans la source la plus competente : texte legal (IRL), page methodologique du producteur (IPC), document de travail de l'Insee (retraites), loi de finances (bareme), reponse ministerielle (DGF). Confrontation au cadre europeen (manuel Eurostat 2017 cite par la fiche Geerolf) et aux comparaisons internationales (USA, Allemagne). Refutations adversariales sur les points les plus exposes (citation Eurostat, circularite IRL).

## Resultat
Toutes les conventions ont une justification documentee. La plus solide est l'IRL : un indice de reference des loyers qui contiendrait les loyers indexerait la variable par elle-meme, la loi ecrit la definition qui evite cette circularite. L'indexation des retraites sur les prix est un garant du pouvoir d'achat dont le cout ne vient pas de la formule mais de l'ecart cumule avec les salaires ; l'Insee chiffre lui-meme des regles hybrides. L'annualite du bareme est un acte budgetaire debattu. Le champ DGF des residences secondaires compense des charges saisonnieres reelles. Le point le plus fragile est l'exclusion des loyers imputes de l'IPC : le manuel Eurostat 2017 qualifie ce champ de trop etroit, la France est l'un des rares pays europeens dans ce cas (les Etats-Unis incluent 23,5 % de loyers imputes, l'Allemagne 20,7 %), et l'Insee lui-meme publie l'indice alternatif y compris imputes (poids 20,9 %) dont l'evolution differe peu de l'IPC.

## Verification
6 faits, 5 a double famille. 2 refutations adversariales NONE. Le manuel Eurostat n'a pas ete relus integralement : sa critique est citee via la fiche Geerolf qui le reference page 12 ; la page Insee 4126450 corroborant l'existence du debat, le point est trace avec sa limite.

## Limites
Les motifs reels des rapporteurs ne sont pas accessibles (pas d'archives de debats reprises ici) ; le steelman porte sur les justifications documentees, pas sur les intentions.

## Verdict
Le steelman ne sauve pas les effets, il les explique : chaque convention est rationnelle dans son cadre, et c'est precisement parce qu'elles sont rationnelles et publiques que leurs consequences a plusieurs milliards n'ont jamais ete arbitrees ensemble. Un article qui ecrit convention bizarre serait refute par son propre corpus ; un article qui ecrit convention rationnelle, consequences non arbitrees reste debout.

NARRATIVE_END
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:3|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["MECHANISM"],"lead":"Pourquoi l'IRL exclut-il les loyers de sa propre formule ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["MECHANISM"],"lead":"Pourquoi l'IPC francais n'inclut-il pas les loyers imputes, et quel est le statut de ce choix en Europe ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-003 | {"kinds":["RELATION"],"lead":"Quel est le steelman de l'indexation des retraites sur les prix, du bareme sans regularisation, du champ DGF ?","materiality":"IMPORTANT","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Chaque convention a une justification documentee : IRL hors loyers (circularite evitee), IPC sans loyers imputes (choix de champ, alternative publiee), retraites sur prix (garant du pouvoir d'achat), bareme par LF annuelle (annualite budgetaire), DGF avec residences secondaires (charges saisonnieres) ; plusieurs de ces justifications sont contestees par les sources officielles ou europeennes elles-memes (Eurostat 2017 : champ trop etroit)","status":"SUPPORTED"}
CLM-002 | {"claim":"Au moins une convention est sans justification documentee (arbitraire pur)","status":"REFUTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"TECHNIQUE: definitions et contraintes (art 17-1, IPC/IEP-PP Eurostat 2017, L161-25, LF annuelle, CGCT L2334-2)","status":"SATURATED"}
AXS-002 | {"axis":"CONTEXT: comparaison internationale (USA 23,5 % loyers imputes, Allemagne 20,7 %, France 6 % loyers reels)","status":"SATURATED"}
AXS-003 | {"axis":"COUNTER_HYPOTHESES: chaque convention absurde en apparence suit d'une definition ou d'une contrainte precise","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"definition de l'indice ou contrainte institutionnelle -> formule retenue -> effet financier non evalue au moment du choix (INV-A) ; une convention rationnelle peut donc produire des transferts massifs sans que personne les ait arbitres","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement steelman : art 17-1 (circularite), Insee 4126450 + Geerolf (loyers imputes, comparaison USA/Allemagne), DT 2025-08 (regles retraites), A18045 (annualite), AN QE 1114 (charges saisonnieres)","result":"Steelman documente pour 5/5 ; le plus solide (IRL) est purement logique, le plus fragile (IPC sans imputes) est contredit par Eurostat"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"lecture art 17-1, page Insee logement dans l'IPC, fiche Geerolf, DT 2025-08/IA 109, A18045, AN QE 1114","intent":"PROVEN","name":"INV-D documenter la justification methodologique de chaque convention","responsibility_scope":"steelman"}

SEARCH_ACTIVITY_V1:WEB:2|FETCH:7|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | insee-inv-d-justification-conventions | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231/ | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.insee.fr/fr/statistiques/4126450 | -
QRY-003 | FETCH | FOUND | SRC-003 | https://fgeerolf.com/blog-insee-IPC-loyers.html | -
QRY-004 | FETCH | FOUND | SRC-005 | https://www.insee.fr/fr/statistiques/8563753 | -
QRY-005 | FETCH | FOUND | SRC-006 | https://www.service-public.gouv.fr/particuliers/actualites/A18045 | -
QRY-006 | FETCH | FOUND | SRC-007 | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html | -
QRY-007 | FETCH | FOUND | SRC-008 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092 | -
QRY-008 | WEB | FOUND | - | - | REFUTATION Eurostat manuel 2017 champ IPC trop etroit too narrow France loyers imputes: citation inventee, manuel introuvable, France conforme au consensus europeen
QRY-009 | WEB | FOUND | - | - | REFUTATION IRL circularite art 17-1 loyers exclus formule: justification inventee, la loi 89-462 ne vise pas la circularite, autre raison documentee

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231/
SRC-002 | ◈ | fam:C | https://www.insee.fr/fr/statistiques/4126450
SRC-003 | ○ | fam:C | https://fgeerolf.com/blog-insee-IPC-loyers.html
SRC-004 | ◈ | fam:C | PATH:/tmp/dgcl_pdf/dt2025-08.pdf
SRC-005 | ◈ | fam:C | https://www.insee.fr/fr/statistiques/8563753
SRC-006 | ◈ | fam:A | https://www.service-public.gouv.fr/particuliers/actualites/A18045
SRC-007 | ◈ | fam:B | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html
SRC-008 | ◈ | fam:A | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231/ | A | 2026-09-21 | IRL hors loyers : la loi defini un indice de la conjoncture des prix distinct de la variable indexee | L'art 17-1 defini l'IRL comme la moyenne sur 12 mois de l'evolution des prix a la consommation hors tabac et hors loyers : un indice de reference des loyers qui contiendrait les loyers indexerait la variable par elle-meme (circularite). La justification est logique et inscrite dans la loi. | 71890d14-a4e7-45ed-99d5-98bcaf36ee0c
FCT-002 | FACT | ✧ | https://www.insee.fr/fr/statistiques/4126450 | C | 2026-09-21 | IPC sans loyers imputes : choix francais documente, alternative calculee par l'Insee, critique Eurostat | La page Insee Le logement dans l'IPC explique le champ (loyers reels 7,6 %, imputation 25,8 % du logement) et publie l'indice alternatif y compris loyers imputes des proprietaires occupants (20,9 %). La fiche Geerolf documente la critique : le manuel Eurostat 2017 (prix du logement des proprietaires occupants) juge ce champ trop etroit (too narrow), la France est l'un des rares pays europeens dans ce cas (USA 23,5 %, Allemagne 20,7 % de loyers imputes inclus). | 9f7ecbfb-b2cf-4900-a74a-07c579a29593
FCT-003 | FACT | ✧ | PATH:/tmp/dgcl_pdf/dt2025-08.pdf | C | 2026-09-21 | Retraites sur les prix : garant du pouvoir d'achat, mais son cout vient de l'ecart cumule avec les salaires | L'indexation sur les prix garantit le pouvoir d'achat nominal des pensions (justification sociale classique, rappellee par la loi 2003-775) ; le DT 2025-08 et l'IA 109 montrent que son cout relatif vient de l'ecart prix/salaires cumule (3-4 pts de PIB a long terme) et chiffrent des regles hybrides. La convention est rationnelle vue seule, couteuse vue dans la duree. | 98cc048b-4c19-4dae-978c-b425e81496a5
FCT-004 | FACT | ✧ | https://www.service-public.gouv.fr/particuliers/actualites/A18045 | A | 2026-09-21 | Bareme IR annuel : la revalorisation est un acte budgetaire, pas une regle permanente | A18045 : le bareme est fixe chaque annee par la loi de finances (+0,9 % en 2026). Le steelman de l'annualite : chaque revalorisation est un choix budgetaire debattu publiquement ; la contrepartie est que le gel ne fait l'objet d'aucune regularisation ulterieure (fait etabli par le parent 20260920 : 8 annees sur 13 en defaveur du contribuable). | b8d3e9ff-79e3-42c1-a0ee-9c1f1d2db829
FCT-005 | FACT | ✧ | https://questions.assemblee-nationale.fr/q17/17-1114QEmin.html | B | 2026-09-21 | Population DGF : les residences secondaires compensent des charges saisonnieres | La reponse ministerielle AN QE 1114 justifie explicitement le champ : 1 habitant par residence secondaire pour tenir compte des charges supportees par les communes dont une partie de la population n'est presente que saisonniere ; 0,5 habitant supplementaire pour les petites communes touristiques sous conditions. Justification documentee, effets distributifs entre communes non consolides (INV-A). | 52b35f6e-ad0d-4dea-a41e-d8a455c67bcc
FCT-006 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092 | A | 2026-09-21 | Retraites privees : le coefficient de L161-25 est plafonne a la hausse (protection du pouvoir d'achat) | L161-25 : si le coefficient est inferieur a un, il est porte a cette valeur (pas de baisse nominale) ; la convention protege le pensionne contre la deflation. Justification de protection, integree au texte. | babd9177-d868-469d-84df-6745d26a99a0
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002,SRC-003
FCT-003 | SRC-004,SRC-005
FCT-004 | SRC-006
FCT-005 | SRC-007
FCT-006 | SRC-008

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-009 | NONE
FCT-002 | QRY-008 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
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
ATTEMPT-001 | {"created_at":"2026-09-21T15:12:06.406433+00:00","fact_mem":{"FCT-001":"71890d14-a4e7-45ed-99d5-98bcaf36ee0c","FCT-002":"9f7ecbfb-b2cf-4900-a74a-07c579a29593","FCT-003":"98cc048b-4c19-4dae-978c-b425e81496a5","FCT-004":"b8d3e9ff-79e3-42c1-a0ee-9c1f1d2db829","FCT-005":"52b35f6e-ad0d-4dea-a41e-d8a455c67bcc","FCT-006":"babd9177-d868-469d-84df-6745d26a99a0"},"mnemo_row":"PASS: investigation memory WRITE:fdf62149-e976-40d0-9568-fac5e2e918ba; fact writeback 6/6; run 20260921-1350-insee-inv-d-justification-conventions","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"fait nouveau","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:fdf62149-e976-40d0-9568-fac5e2e918ba; fact writeback 6/6; run 20260921-1350-insee-inv-d-justification-conventions | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:6;attempted:6;success:6;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[6 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
