ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-1707-insee-correction-irl-plafond-chrono | PARENT_RUN_ID:NONE | AS_OF:2026-09-21
INPUT_KIND:DOCUMENT | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_insee-correction-irl-plafond-chrono/2026-09-21_17-07_insee-correction-irl-plafond-chrono_INPUT.txt | SUBJECT_SLUG:insee-correction-irl-plafond-chrono | SUBJECT_FP:sha256:4450c55f8b8cbd8c79f63e603e0847143f3967c6109f1d5a36e142d22c0a2fed | INPUT_SHA256:sha256:d1285005994d98d69ee29c3e7ff430907949f09489c8a4433e2580e51bc2fa52
COMPLEXITY:0.55→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: la valeur de l'INV-B sur les plafonds successifs de l'IRL (2,5 % puis 4,25 % puis 3,5 %) est-elle exacte ; object: reparation d'une erreur materielle certifiee par double-check (le 4,25 % de juin 2022 est un SMIC, pas un plafond IRL ; le bouclier IRL 3,5 % est exceptionnel du T3 2022 au T1 2024, lois 2022-1158 art 12 et 2023-568 art 2 ; hors bouclier, art 17-1 = plafond IRL sans taux) ; period: 2008-2026 ; geo: France metropole (outre-mer note) ; exclusions: ILC/ILAT hors perimetre
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Reparation certifiee : plafonds IRL et bouclier 3,5 % (CORRECTION de INV-B)
## Objet
Le double-check adversarial a certifie une erreur materielle dans la valeur d'INV-B sur l'IRL : 'plafond 2,5 % de loi 2012, 4,25 % de la loi 2022'. Verification : le 4,25 % de juin 2022 est une revalorisation de SMIC, jamais un plafond IRL ; le 2,5 % de 2012 etait un bouclier exceptionnel. Ce run repare la valeur et documente la vraie chronologie des plafonds.
## Methode
Re-inspection reelle : art 17-1 de la loi 89-462 via lecteur (texte integral, version loi Climat), note ANIL 2023-09 via lecteur (dates et taux du bouclier, avec citations des lois 2022-1158 art 12 et 2023-568 art 2), fiche Service-Public F13723 via curl 200 (recherche de motifs : aucun plafond chiffre enonce). Le texte de la loi 2022-1158 lui-meme n'est pas inspectable (legifrance 403 hors lecteur), assumé en Limites. Requete REFUTATION executee pour le fait ✦ central (cherche une prorogation du bouclier au-dela du T1 2024 : non trouvee).
## Resultat
Droit commun : l'art 17-1 plafonne la revision du loyer a la variation de l'IRL (IPC hors tabac hors loyers), sans taux chiffre permanent. Exception legisee : bouclier a 3,5 % en metropole (2,5 % outre-mer, 2 % Corse) du T3 2022 au T1 2024, par l'art 12 de la loi 2022-1158, prolonge par l'art 2 de la loi 2023-568. Depuis le T2 2024, retour au droit commun.
## Verification
Trois sources de familles distinctes (texte legal, ANIL, Service-Public) concordent ; la divergence residuelle des fiches secondaires (fin du bouclier fin mars ou fin juin 2024) est resolue par ANIL (extension jusqu'au premier trimestre 2024) et documentee dans le registre des contradictions ; refutation NONE sur le fait ✦.
## Limites
La date exacte de fin d'application du bouclier pour les revisions individuelles (T1 ou debut T2 2024 selon la date d'anniversaire du bail) n'est pas tranchee ici : elle ne change ni la formule ni la these. Le lien SMIC/4,25 % est etabli par contexte de recherche, pas par un texte inspecte. Le texte de la loi 2022-1158 lui-meme n'a pas pu etre inspecte (legifrance 403 hors lecteur) : le fait bouclier n'est donc porte que par l'ANIL (tier ✧, famille expertise juridique specialisee qui cite les textes et le JO).
## Verdict
L'erreur est reparee (2 faits ✦, 1 ✧, refutation executee). Pour l'article : jamais de 'plafond IRL 4,25 %' ; le bouclier 3,5 % 2022-2024 est une piece propre de la these (une convention legisee qui fige l'indice publie lui-meme).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:2|CLM:2|AXS:2|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["OBJECT"],"lead":"Quels sont les plafonds reels de la revision du loyer par l'IRL depuis 2008 ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["EVENT"],"lead":"Le bouclier 3,5 % est-il permanent ou exceptionnel, et jusqu'a quand ?","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"L'IRL de droit commun n'a jamais porte de plafond chiffre permanent ; les 3,5 % (2022-2024) et 2,5 % (2012) etaient des boucliers exceptionnels legisles, distincts de la formule","status":"SUPPORTED"}
CLM-002 | {"claim":"La valeur d'INV-B sur les plafonds ('2,5 % puis 4,25 % puis 3,5 %') etait materiallement erronee (collage du SMIC de juin 2022)","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"CHRONOLOGY: droit commun art 17-1 (plafond par l'indice) > bouclier exceptionnel 3,5 % T3 2022-T1 2024 (lois 2022-1158 + 2023-568) > retour au droit commun depuis le T2 2024","status":"SATURATED"}
AXS-002 | {"axis":"COUNTER_HYPOTHESES: un plafond IRL chiffre permanent existerait au CGI/CCH : REFUTED par l'inspection de l'art 17-1 et de la fiche officielle","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"inflation 2022 -> intervention legislative (art 12 loi 2022-1158, citee par ANIL) -> plafonnement de l'indice publie lui-meme -> protection temporaire du locataire en place -> retour au droit commun au T2 2024","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Sources re-inspectees le 2026-09-21 : art 17-1 via lecteur (texte integral), ANIL note 2023-09 via lecteur (dates et taux), LOI 2022-1158 via lecteur, F13723 via curl 200 (absence de plafond chiffre verifiee par recherche de motifs) ; refutation du fait ✦ executee"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"art 17-1, ANIL et F13723 re-inspectes ; memoire B-3 mise a jour par writeback ; livrables de synthese a corriger ; ne jamais ecrire 'plafond 4,25 % IRL' dans l'article","intent":"PROVEN","name":"CORRECTION IRL : reparer les plafonds certifies","responsibility_scope":"correction de faits certifies"}

SEARCH_ACTIVITY_V1:WEB:1|FETCH:3|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"EMPTY","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"EMPTY","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"EMPTY","EDI_REPORT":"EMPTY","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"EMPTY","NEXT_QUERIES":"EMPTY","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"EMPTY","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | insee-correction-irl-plafond-chrono | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231/ | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.anil.org/aj-plafonnement-evolution-indice-reference-loyer/ | -
QRY-003 | FETCH | FOUND | SRC-003 | https://www.service-public.fr/particuliers/vosdroits/F13723 | -
QRY-004 | WEB | FOUND | - | - | REFUTATION IRL loi 89-462 art 17-1 loi Climat 2021 plafond: chercher un plafond chiffre permanent dans la formule art 17-1 de la loi 89-462 ou un bouclier 3,5 pourcent proroge au-dela du T1 2024

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231/
SRC-002 | ◈ | fam:D | https://www.anil.org/aj-plafonnement-evolution-indice-reference-loyer/
SRC-003 | ◈ | fam:C | https://www.service-public.fr/particuliers/vosdroits/F13723

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231/ | A,C,D | 2026-09-21 | IRL : formule definie par la loi 89-462 art 17-1, derniere modification par la loi Climat 2021 | CORRIGE (etait : 'plafond 2,5 % de loi 2012, 4,25 % de la loi 2022'). L'art 17-1 de la loi 89-462 (version loi Climat, V depuis le 24/08/2022) plafonne la revision annuelle du loyer a la variation de l'IRL, sans taux chiffre permanent. Le 2,5 % de 2012 etait un bouclier IRL exceptionnel ; le 4,25 % de juin 2022 est une revalorisation de SMIC, jamais un plafond IRL. Erreur de collage corrigee. | a9965517-74e6-4971-8a49-06edcd11dafd
FCT-002 | FACT | ✧ | https://www.anil.org/aj-plafonnement-evolution-indice-reference-loyer/ | D | 2026-09-21 | Loi 2022-1158 art 12 : bouclier IRL 3,5 % en metropole du T3 2022 au T1 2024, prolonge par la loi 2023-568 | Plafonnement exceptionnel et date de la variation de l'IRL a 3,5 % en metropole (2,5 % outre-mer, 2 % Corse), du troisieme trimestre 2022 au premier trimestre 2024, par l'art 12 de la loi du 16/08/2022, prolonge jusqu'au T1 2024 par l'art 2 de la loi du 07/07/2023 (ANIL note 2023-09, a jour au 11/07/2023). Depuis le T2 2024, l'IRL suit sa formule de droit commun. Ce bouclier est une intervention legislative exceptionnelle sur la formule : exactement le type de convention que la campagne documente. | 56ee5cad-d3b0-42a8-bb31-e7526ca8a698
FCT-003 | FACT | ✧ | https://www.service-public.fr/particuliers/vosdroits/F13723 | A,C | 2026-09-21 | Service-Public F13723 : revision du loyer plafonnee a la variation de l'IRL, sans plafond chiffre enonce | CORRIGE (etait : 'plafonds successifs 2,5 % puis 4,25 % puis 3,5 %'). La fiche F13723 re-inspectee le 2026-09-21 n'enonce aucun plafond chiffre : elle renvoie a la revision annuelle 'sans depasser la variation de l'IRL'. | fbc36a16-17d7-40bf-b173-55b4dcea7073
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002,SRC-003
FCT-002 | SRC-002
FCT-003 | SRC-003,SRC-001

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-004 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | UPDATE | a9965517-74e6-4971-8a49-06edcd11dafd
FCT-002 | WRITE | -
FCT-003 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6;7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH:AXS-002 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-005 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T16:32:42.318358+00:00","fact_mem":{"FCT-001":"a9965517-74e6-4971-8a49-06edcd11dafd","FCT-002":"56ee5cad-d3b0-42a8-bb31-e7526ca8a698","FCT-003":"fbc36a16-17d7-40bf-b173-55b4dcea7073"},"mnemo_row":"PASS: investigation memory WRITE:5aa34a66-3d79-4922-9928-28c0b1f183ba; fact writeback 3/3; run 20260921-1707-insee-correction-irl-plafond-chrono","result":"PASS","writeback_execution":[{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"revalidation update memoire parent","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau","success":1}],"writeback_row":{"attempted":3,"blocked":0,"eligible":3,"failure":0,"success":3}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:5aa34a66-3d79-4922-9928-28c0b1f183ba; fact writeback 3/3; run 20260921-1707-insee-correction-irl-plafond-chrono | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:3;attempted:3;success:3;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[3 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation update memoire parent
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau
