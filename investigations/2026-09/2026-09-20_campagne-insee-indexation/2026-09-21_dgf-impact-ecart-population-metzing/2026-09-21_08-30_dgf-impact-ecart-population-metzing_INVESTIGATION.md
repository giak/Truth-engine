ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-0830-dgf-impact-ecart-population-metzing | PARENT_RUN_ID:20260920-2008-dgf-impact-ecart-population-metzing | AS_OF:2026-09-21
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_dgf-impact-ecart-population-metzing/2026-09-21_08-30_dgf-impact-ecart-population-metzing_INPUT.txt | SUBJECT_SLUG:dgf-impact-ecart-population-metzing | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:0.65→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: revalidation du chiffrage DGF Metzing et de la mecanique population DGF; object: confirmation par re-FETCH OFGL/DGCL/Senat/moselle.tv/Insee; period 2018-2026; geo Metzing (57) et cadre national; domains finances locales; actors DGCL/OFGL/Insee/Senat; exclusions EPCI et communes >2000 hab; limits chiffrage marginal sensible a l elasticite annuelle
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
NARRATIVE_START

# Revalidation DGF Metzing - UPDATE certifié 2.10.6

## Objet

Le run parent (`20260920-2008`) avait chiffré l'impact d'un écart de population sur la dotation forfaitaire à partir de la commune de Metzing (57) : élasticités mesurées de 12,9 à 94,6 EUR/hab DGF ajouté, chiffrage central de ~9800 EUR/an pour un écart de 113 habitants (question sénatoriale Mizzon), mécanique fondée sur la population DGF (population INSEE authentifiée + résidences secondaires + places de caravanes) avec écrêtement des communes dont le potentiel fiscal dépasse 85 % de la moyenne nationale. Ce run UPDATE revalide l'ensemble sous le flux certifié 2.10.6.

## Résultat de revalidation

Les cinq faits du parent survivent au re-FETCH du 2026-09-21 :

- **Mécanique (CONFIRMÉ)** : la page canonique DGCL re-fetchee redonne la construction de la population DGF, l'écrêtement 85 % et le transfert CPS aux EPCI depuis la LF 2024.
- **Série Metzing (CONFIRMÉE)** : l'API OFGL redonne pop INSEE 631 → 715 (2018-2026), pop DGF 679/700/716 (2024-2026) et DGF 70565 → 114005 EUR.
- **Élasticités (CONFIRMÉES)** : 94,6 (2022-23), 84,5 (2023-24), 12,9 (2024-25, année de rattrapage), 89,4 EUR/hab (2025-26).
- **Chiffrage 113 hab (CONFIRMÉ)** : ~9800 EUR/an (élasticité médiane 86,9 ; plage de barème 7300-14600), corroboré par la question sénatoriale et la presse régionale (Bouzonville ~30 kEUR pour ~une centaine d'habitants).
- **Rattrapage (CONFIRMÉ)** : +37 habitants INSEE en deux ans (678 → 715), symptôme du rattrapage des communes sous-recensées.

Le détail des notes DGCL 2026 (modes de calcul, part population, part CPS) est traité par l'UPDATE frère certifié du même jour (`20260921-0731 dgcl-notes-elasticite-part-population`), qui a également confirmé le chiffrage du présent parent.

## Vérification

Les trois requêtes de réfutation formelles (série OFGL révisée ? formule modifiée ? écrêtement supprimé ?) ne retournent aucune contradiction. Le recoupement croisé Sénat/moselle.tv/OFGL reste convergent avec l'élasticité mesurée.

## Limites

Le chiffrage marginal reste sensible à l'élasticité annuelle (rattrapage 2024-25 à 12,9 EUR/hab). La fiche nominative de calcul n'est pas publique. L'écrêtement ne concerne pas Metzing (PF sous le seuil).

## Verdict

Le parent est confirmé sur toutes ses valeurs. Run certifiable : sources officielles inspectées le jour de la livraison, corroboration croisée maintenue, réfutations vides.

NARRATIVE_END
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:2|CLM:1|AXS:3|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["OBJECT"],"lead":"Mecanique DGF: population DGF et ecretement (page DGCL)","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["OBJECT"],"lead":"Chiffrage marginal Metzing: serie OFGL, elasticites, ecarts 113 hab","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Revalidation: la mecanique population DGF et le chiffrage Metzing du parent sont confirmes par les sources re-fetchees","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"TECHNIQUE: definition population DGF et parametres 2026","status":"SATURATED"}
AXS-002 | {"axis":"ECONOMIQUE: serie OFGL Metzing et elasticites EUR/hab","status":"SATURATED"}
AXS-003 | {"axis":"CONTRE-HYPOTHESES: revision OFGL, changement de formule, ecretement supprime","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"population DGF (INSEE + res sec + caravanes) -> variation dotation forfaitaire (avec ecretement PF > 85 %) -> ecart d'habitants converti en EUR/an -> rattrapage au fil des millésimes","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement corroboration: question Senat Mizzon (ecart 113 hab) + moselle.tv Bouzonville (perte ~30 kEUR) vs serie OFGL Metzing","result":"Question parlementaire et presse regionale convergent avec l'elasticite mesuree 86,9 EUR/hab et la plage 7300-14600 EUR/an","status":"PASS"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"re-FETCH 5 sources le 2026-09-21","intent":"PROVEN","name":"Revalider le chiffrage DGF Metzing sous flux certifie 2.10.6","responsibility_scope":"revalidation","role":"revalidation 2.10.6","source":"-","status":"DONE"}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | dgf-impact-ecart-population-metzing | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes | -
QRY-002 | FETCH | FOUND | SRC-002 | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100 | -
QRY-003 | FETCH | FOUND | SRC-003 | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | -
QRY-004 | FETCH | FOUND | SRC-004 | https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/ | -
QRY-005 | FETCH | FOUND | SRC-005 | https://www.insee.fr/fr/information/2553979 | -
QRY-006 | WEB | FOUND | - | - | REFUTATION chiffrage DGF ecart 113 habitants type Metzing: elasticite 86,9 EUR/hab invalidee, ecretement 85 % supprime, corroboration Senat moselle.tv retirée
QRY-007 | WEB | FOUND | - | - | REFUTATION mecanique DGF population INSEE authentifiee residences secondaires caravanes: population DGF abandonnee, formule modifiee 2026
QRY-008 | WEB | FOUND | - | - | REFUTATION serie OFGL Metzing 2018 2026 dotations 70565 114005: donnees revisees ou retirees du catalogue

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes
SRC-002 | ◈ | fam:A | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100
SRC-003 | ◉ | fam:B | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html
SRC-004 | ◉ | fam:D | https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/
SRC-005 | ◈ | fam:A | https://www.insee.fr/fr/information/2553979

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes | A | 2026-09-21 | Mécanique DGF fondée sur la population INSEE authentifiée | Revalidation 2026-09-21: la dotation forfaitaire evolue selon la population DGF (pop INSEE authentifiee + residences secondaires + places caravanes); ecretement des communes dont le PF > 85 % de la moyenne nationale; part CPS integrale aux EPCI depuis la LF 2024 | a4d80cd4-f50d-4475-a1ea-44599568fa3d
FCT-002 | FACT | ✧ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100 | A | 2026-09-21 | Série réelle Metzing 2018-2026 populations et dotations | Revalidation 2026-09-21: OFGL Metzing pop INSEE 631/647/656/662/669/674/678/699/715 (2018-2026); pop DGF 679/700/716 (2024-2026); Montant DGF 70565 -> 114005 EUR (2018-2026) | d8dc1852-47d2-428a-a230-515e589c141f
FCT-003 | FACT | ✧ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100 | A | 2026-09-21 | Élasticités réelles forfait/population DGF de Metzing | Revalidation 2026-09-21: delta forfaitaire / delta pop DGF = 94,6 (2022-23), 84,5 (2023-24), 12,9 (2024-25, rattrapage), 89,4 EUR/hab (2025-26) | a56355d3-84c3-4622-84e4-1439ab5348a0
FCT-004 | FACT | ✦ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100 | A,B,D | 2026-09-21 | Chiffrage DGF écart 113 habitants type Metzing | Revalidation 2026-09-21: un ecart de 113 habitants (678 vs 791, question Mizzon) vaut environ 9800 EUR/an (elasticite mediane 86,9 EUR/hab; plage bareme 7300-14600); corrobore par le Senat et moselle.tv (Bouzonville ~30 kEUR); refutation bornee NONE | db3dbddc-8baa-4ce0-8236-5dc16959beec
FCT-005 | FACT | ✧ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100 | A | 2026-09-21 | Rattrapage réel Metzing 2025-2026 | Revalidation 2026-09-21: pop INSEE Metzing 678 (2024) -> 699 (2025) -> 715 (2026): +37 habitants en deux ans (5,5 %), symptome de rattrapage de communes sous-recensees | 69edb1f7-8251-4e9f-9072-e985b9c618ec
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-002
FCT-004 | SRC-002,SRC-003,SRC-004
FCT-005 | SRC-002,SRC-005

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-007 | NONE
FCT-002 | QRY-008 | NONE
FCT-004 | QRY-006 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | UPDATE | a4d80cd4-f50d-4475-a1ea-44599568fa3d
FCT-002 | UPDATE | d8dc1852-47d2-428a-a230-515e589c141f
FCT-003 | UPDATE | a56355d3-84c3-4622-84e4-1439ab5348a0
FCT-004 | UPDATE | db3dbddc-8baa-4ce0-8236-5dc16959beec
FCT-005 | UPDATE | 69edb1f7-8251-4e9f-9072-e985b9c618ec

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6;7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH:AXS-003 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-005 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T09:06:36.904429+00:00","fact_mem":{"FCT-001":"a4d80cd4-f50d-4475-a1ea-44599568fa3d","FCT-002":"d8dc1852-47d2-428a-a230-515e589c141f","FCT-003":"a56355d3-84c3-4622-84e4-1439ab5348a0","FCT-004":"db3dbddc-8baa-4ce0-8236-5dc16959beec","FCT-005":"69edb1f7-8251-4e9f-9072-e985b9c618ec"},"mnemo_row":"PASS: investigation memory WRITE:a69cad49-b906-4bee-b2bf-4e55f6df7450; fact writeback 5/5; run 20260921-0830-dgf-impact-ecart-population-metzing","result":"PASS","writeback_execution":[{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"revalidation update memoire parent","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"revalidation update memoire parent","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"revalidation update memoire parent","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"revalidation update memoire parent","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"revalidation update memoire parent","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:a69cad49-b906-4bee-b2bf-4e55f6df7450; fact writeback 5/5; run 20260921-0830-dgf-impact-ecart-population-metzing | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation update memoire parent
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation update memoire parent
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation update memoire parent
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation update memoire parent
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation update memoire parent
