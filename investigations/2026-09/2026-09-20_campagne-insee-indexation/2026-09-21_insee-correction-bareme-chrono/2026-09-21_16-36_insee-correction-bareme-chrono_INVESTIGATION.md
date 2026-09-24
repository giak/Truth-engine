ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-1636-insee-correction-bareme-chrono | PARENT_RUN_ID:NONE | AS_OF:2026-09-21
INPUT_KIND:DOCUMENT | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-correction-bareme-chrono/2026-09-21_16-36_insee-correction-bareme-chrono_INPUT.txt | SUBJECT_SLUG:insee-correction-bareme-chrono | SUBJECT_FP:sha256:14bd4b67dededfd478328f808f532e1642f69219bab5199c938de698c7238e2d | INPUT_SHA256:sha256:d8a38f0ff87b781cd88dbb21a6356e4f99f8535aab20fe8f246a5926ea25d364
COMPLEXITY:0.60→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: la chronologie d'indexation du bareme IR 2023-2026 et le chiffrage I-Frap ont-ils ete correctement documentes dans INV-E ; object: reparation de 2 erreurs materielles certifiees par double-check adversarial (taux LF 2025 affirme a 0,9 % sans source : reel 1,8 % ; cumul I-Frap affirme a 200 Mds depuis 2000 sans source : reel ~6 Md€ sur la periode recente) ; period: 2023-2026 ; geo: France ; exclusions: aucune nouvelle acception hors correction
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Reparation certifiee : chronologie du bareme IR 2023-2026 (CORRECTION de INV-E)
## Objet
Le double-check adversarial du 2026-09-21 a certifie deux erreurs materielles dans INV-E : le taux de revalorisation 2025 du bareme (affirme 0,9 % sans source ; reel : 1,8 %) et le cumul I-Frap (affirme 200 Mds depuis 2000 sans source ; reel : ~6 Md€ sur la periode recente). Ce run repare ces erreurs par des faits corriges, sources re-inspectees, sans toucher aux fichiers figes du parent.
## Methode
Re-inspection reelle des sources decisive : OFCE (prevision automne 2024, 200 : censure du 04/12/2024, loi speciale, 400 000 menages), economie.gouv.fr du 17/02/2025 (200 : tranches finales LF 2025, +1,8 %, premier seuil 11 497 EUR), Service-Public A18045 (200 : bareme fixe chaque annee, LF 2026 plein regime), I-Frap (200 : trop-paye ~6 Md€ recent). Requete REFUTATION executee pour chaque fait a tier ✦.
## Resultat
Chaine reelle 2023-2026 : gel total 2023 ; PLF 2024 chiffre le gel a +6,1 Md€ ; PLF 2025 propose +2,0 % ; censure le 04/12/2024 ; loi speciale du 20/12/2024 = gel de fait ; LF 2025 du 14/02/2025 = +1,8 % (pas plein regime) ; LF 2026 = plein regime. I-Frap : ~6 Md€ recents, pas de cumul 200 Mds trouve sur la page.
## Verification
Quatre sources re-inspectees le jour meme, coherence croisee (OFCE = economie.gouv.fr = A18045 sur la chaine) ; la contradiction PLF 2025 (2,0 %) vs LF 2025 (1,8 %) est resolue par la chronologie legislative (censure puis negociation) ; les deux faits ✦ portent chacun une refutation executee NONE.
## Limites
Le taux 1,8 % repose sur la source officielle economie.gouv.fr (tranches finales) : l'article de loi L 2025-127 n'a pas pu etre inspecte directement (legifrance 403 hors lecteur) ; la date de fin exacte de l'effet loi speciale n'est pas datee au jour pres. Le cumul I-Frap est l'estime d'un think tank, borne a la periode recente : il n'est corrige qu'en tier ✧ (famille expertise, jamais corroboree par une source officielle), ce qui ne change pas la reparation du fait (le chiffre 200 Mds n'existe pas sur la page).
## Verdict
Les deux erreurs sont reparees par des faits certifies (1 ✦ sur la chronologie corrigee ; les faits I-Frap et censure restent ✧, familles uniques assumees). Les memoires parentes sont mises a jour via writeback et les livrables de synthese doivent reprendre la chronologie corrigee avant toute redaction.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:2|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["EVENT"],"lead":"Quel est le taux final de revalorisation du bareme dans la LF 2025 et la chaine 2023-2026 ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["OBJECT"],"lead":"Que chiffre reellement I-Frap sur la non-indexation du bareme ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-003 | {"kinds":["EVENT"],"lead":"La censure de decembre 2024 a-t-elle modifie la trajectoire du bareme ?","materiality":"IMPORTANT","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La trajectoire du bareme 2023-2026 passe par une interruption (censure puis loi speciale) et une revalorisation incomplete en 2025 (+1,8 %), ce qu'aucun des runs parents ne documentait","status":"SUPPORTED"}
CLM-002 | {"claim":"Le chiffrage pluriannuel des transferts du bareme reste absent des canaux officiels ; le seul cumul disponible est celui d'un think tank (~6 Md€ recents)","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"CHRONOLOGY: gel 2023 > PLF2024 (+6,1 Md€) > PLF2025 (+2,0 %) > censure 04/12/2024 > loi speciale 20/12/2024 > LF2025 (+1,8 %) > LF2026 plein regime","status":"SATURATED"}
AXS-002 | {"axis":"COUNTER_HYPOTHESES: le taux 0,9 % ou 2,2 % existerait dans un texte promulgue : REFUTED par la source officielle primale","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"PLF 2025 (+2,0 % chiffre) -> censure du 04/12/2024 -> loi speciale du 20/12/2024 -> non-indexation de fait des revenus 2024 -> LF 2025 compense partiellement (+1,8 %) -> plein regime seulement en 2026","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Toutes les sources corrigees re-inspectees le 2026-09-21 : OFCE (200, contenu verifie), economie.gouv.fr (200, tranches finales lues), A18045 (200, LF 2026 lue), I-Frap (200, 6 Md€), Mercipourlinfo/IPP (heritees des runs certifies) ; refutations executees par recherche web"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"sources re-inspectees (OFCE, economie.gouv.fr, A18045, I-Frap) ; memoires E-5/E-6 mises a jour par writeback ; livrables de synthese a corriger","intent":"PROVEN","name":"CORRECTION bareme : reparer la chronologie certifiee","responsibility_scope":"correction de faits certifies"}

SEARCH_ACTIVITY_V1:WEB:2|FETCH:6|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"EMPTY","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"EMPTY","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"EMPTY","EDI_REPORT":"EMPTY","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"EMPTY","NEXT_QUERIES":"EMPTY","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"EMPTY","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | insee-correction-bareme-chrono | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.ofce.fr/prev/prev2409/es/loi_speciale/loi_speciale.html | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.economie.gouv.fr/particuliers/gerer-mon-argent/gerer-mon-budget-et-mon-epargne/ce-qui-change-pour-les-particuliers-avec-ladoption-du-budget-2025 | -
QRY-003 | FETCH | FOUND | SRC-003 | https://www.service-public.gouv.fr/particuliers/actualites/A18045 | -
QRY-004 | FETCH | FOUND | SRC-004 | https://www.mercipourlinfo.fr/actualites/impots/impot-sur-le-revenu-quelles-seraient-les-consequences-possibles-du-gel-du-bareme-1104075 | -
QRY-005 | FETCH | FOUND | SRC-005 | https://www.ipp.eu/publication/lindexation-sur-linflation-du-bareme-de-limpot-sur-le-revenu-implications-sur-les-taux-dimposition-et-la-redistribution/ | -
QRY-006 | FETCH | FOUND | SRC-006 | https://www.ifrap.org/budget-et-fiscalite/non-lindexation-du-bareme-de-lir-en-2024-nequivaut-pas-un-cadeau-de-6-milliards-aux-contribuables | -
QRY-007 | WEB | FOUND | - | - | REFUTATION LF 2025 bareme 1,8 pourcent revenus 2024: chercher un taux final different (0,9 ou 2,0 ou 2,2) dans les textes promulgues du 14/02/2025
QRY-008 | WEB | FOUND | - | - | REFUTATION I-Frap 200 milliards cumul bareme depuis 2000: verifier si une fiche I-Frap porte un cumul 200 Mds, ou si seul le chiffre 6 Md€ existe

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:E | https://www.ofce.fr/prev/prev2409/es/loi_speciale/loi_speciale.html
SRC-002 | ◈ | fam:A | https://www.economie.gouv.fr/particuliers/gerer-mon-argent/gerer-mon-budget-et-mon-epargne/ce-qui-change-pour-les-particuliers-avec-ladoption-du-budget-2025
SRC-003 | ◈ | fam:A | https://www.service-public.gouv.fr/particuliers/actualites/A18045
SRC-004 | ◈ | fam:D | https://www.mercipourlinfo.fr/actualites/impots/impot-sur-le-revenu-quelles-seraient-les-consequences-possibles-du-gel-du-bareme-1104075
SRC-005 | ○ | fam:D | https://www.ipp.eu/publication/lindexation-sur-linflation-du-bareme-de-limpot-sur-le-revenu-implications-sur-les-taux-dimposition-et-la-redistribution/
SRC-006 | ○ | fam:D | https://www.ifrap.org/budget-et-fiscalite/non-lindexation-du-bareme-de-lir-en-2024-nequivaut-pas-un-cadeau-de-6-milliards-aux-contribuables

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.economie.gouv.fr/particuliers/gerer-mon-argent/gerer-mon-budget-et-mon-epargne/ce-qui-change-pour-les-particuliers-avec-ladoption-du-budget-2025 | A,E | 2026-09-21 | Loi de finances pour 2025 : revalorisation finale du bareme a 1,8 % pour les revenus 2024 (pas plein regime) | La LF n 2025-127 du 14/02/2025 revalorise chaque tranche de 1,8 % (source officielle economie.gouv.fr du 17/02/2025 : premier seuil porte a 11 497 EUR). La chaine reelle 2023-2026 : gel total 2023 ; PLF 2024 chiffre un gel total a +6,1 Md€ (Merci pour l'info) ; PLF 2025 proposait +2,0 % (Senat) ; censure du gouvernement Barnier le 04/12/2024 (OFCE) ; loi speciale du 20/12/2024 = gel de fait (OFCE : +400 000 menages bascules) ; LF 2025 = +1,8 % ; LF 2026 du 19/02/2026 = plein regime a hauteur de l'inflation (A18045). | af4f4b46-aa46-4240-937e-c173dcb395a0
FCT-002 | FACT | ✧ | https://www.ofce.fr/prev/prev2409/es/loi_speciale/loi_speciale.html | E | 2026-09-21 | Censure du 04/12/2024 : bascule du bareme de plein regime vers gel de fait via loi speciale du 20/12/2024 | L'OFCE (prevision automne 2024) documente la censure du 04/12/2024 et la loi speciale : maintien de la legislation 2024 donc non-indexation du barème de l'IRPP et entree dans l'impot de pres de 400 000 menages ; le PLF 2025 qui proposait +2,0 % est abandonne. Corrobore par la couverture de presse (BFM 05/12/2024). | 4e2cc07b-8a17-4b11-b91d-4f8148240e2b
FCT-003 | FACT | ✧ | https://www.ifrap.org/budget-et-fiscalite/non-lindexation-du-bareme-de-lir-en-2024-nequivaut-pas-un-cadeau-de-6-milliards-aux-contribuables | D | 2026-09-21 | I-Frap : le chiffrage pluriannuel du bareme existe mais hors canaux officiels | CORRIGE (etait : 200 Mds depuis 2000). I-Frap estime ~6 Md€ de trop-paye du contribuable sur la periode recente de non-indexation du bareme (2022-2024), cohérent avec les +2,8 a 6 Md€/an des runs parents ; le cumul pluriannuel chiffre par un think tank n'est pas un document officiel de consolidation ; aucune serie officielle pluriannuelle des transferts n'a ete identifiee. | 73c69642-074f-4a59-ac39-b83662458046
FCT-004 | FACT | ✧ | https://www.mercipourlinfo.fr/actualites/impots/impot-sur-le-revenu-quelles-seraient-les-consequences-possibles-du-gel-du-bareme-1104075 | D | 2026-09-21 | Barème IR : le chiffrage annuel existe bien dans les documents officiels (PLF), la consolidation pluriannuelle manque | CORRIGE (etait : +2,2 Md€ en 2025, +0,9 %). Le chiffrage annuel officiel existe (PLF 2024 : +6,1 Md€ pour un gel total ; PLF 2025 : revalorisation 2,0 % chiffree au Senat) mais la trajectoire finale differe des propositions : censure, loi speciale, LF 2025 a +1,8 % seulement (pas plein regime), plein regime en 2026. Ce decalage annuel entre proposition et trajectoire renforce la these de l'absence de consolidation pluriannuelle. | 01035673-54b6-43e6-b74d-4c3feaf6cf2f
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-002,SRC-003,SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-006,SRC-005
FCT-004 | SRC-004,SRC-005

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-007 | NONE
FCT-003 | QRY-008 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | UPDATE | 73c69642-074f-4a59-ac39-b83662458046
FCT-004 | UPDATE | 01035673-54b6-43e6-b74d-4c3feaf6cf2f

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6;7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH:AXS-002 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-005 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T16:30:56.921568+00:00","fact_mem":{"FCT-001":"af4f4b46-aa46-4240-937e-c173dcb395a0","FCT-002":"4e2cc07b-8a17-4b11-b91d-4f8148240e2b","FCT-003":"73c69642-074f-4a59-ac39-b83662458046","FCT-004":"01035673-54b6-43e6-b74d-4c3feaf6cf2f"},"mnemo_row":"PASS: investigation memory WRITE:720dd4aa-aa58-4b79-aba1-9a5976946600; fact writeback 4/4; run 20260921-1636-insee-correction-bareme-chrono","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"revalidation update memoire parent","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"revalidation update memoire parent","success":1}],"writeback_row":{"attempted":4,"blocked":0,"eligible":4,"failure":0,"success":4}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:720dd4aa-aa58-4b79-aba1-9a5976946600; fact writeback 4/4; run 20260921-1636-insee-correction-bareme-chrono | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:4;attempted:4;success:4;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[4 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation update memoire parent
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation update memoire parent
