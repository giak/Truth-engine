ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260921-0826-irl-ecart-loyers-reels-elc | PARENT_RUN_ID:20260920-2154-irl-ecart-loyers-reels-elc | AS_OF:2026-09-21
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-21_irl-ecart-loyers-reels-elc/2026-09-21_08-26_irl-ecart-loyers-reels-elc_INPUT.txt | SUBJECT_SLUG:irl-ecart-loyers-reels-elc | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:0.65→MEDIUM | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:lead: revalidation mecanique IRL et ecarts 2022-2024; object: confirmation par sources primaires re-fetchees; period 2019-2025; geo France hexagone parc prive; domains statistique publique, logement; actors Insee/ANIL/SDES/legislateur; exclusions parc social, UTOM/Corse; limits ELC routee vers l UPDATE cui-bono 20260921-0824
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
NARRATIVE_START

# Révalidation IRL et écarts loyers 2022-2025 — UPDATE certifié 2.10.6

## Objet

Le run parent (`20260920-2154`) avait établi la mécanique de l'indice de référence des loyers — moyenne sur douze mois consécutifs de l'évolution de l'IPC hors tabac et hors loyers (loi 2008-111 art. 9, création par la loi 2005-841 art. 35) — et chiffré l'écart entre l'IRL et les loyers réels sur 2022-2024, avec un transfert de l'ordre de 1,5-2 Md€/an vers les locataires en place pendant le choc, puis ~0,7 Md€ en 2024. Ce run UPDATE revalide ces résultats sous le flux certifié 2.10.6, un jour après leur production, par re-FETCH des sources primaires le jour même.

## Résultat de revalidation

Toutes les valeurs du parent survivent au re-FETCH :

- **Mécanique IRL (CONFIRMÉ)** : la fiche Insee (T3 2025, inspectée) redonne la formule exacte, documente elle-même le plafonnement de 3,5 % (loi 2022-1158 art. 12, T3 2022-T1 2024) et publie IRL T3 2025 = 145,77 (+0,87 %) ; le tableau ANIL est identique à l'arrondi près (recoupement concluant sur T3 et T4 2025).
- **Écarts 2022-2024 (CONFIRMÉ)** : IPC hors tabac +5,2 % (2022) et +4,8 % (2023) et +1,8 % (2024) réaffichés par l'IR n°6 du 15/01/2025 ; combiné aux glissements IRL (+3,27 %/+3,49 %/+2,75 % en moyenne annuelle), le différentiel IRL-IPC-HT de -1,93/-1,31/+0,95 point tient.
- **Complément 2025 (NOUVEAU)** : IPC hors tabac +0,9 % (IR n°8 du 15/01/2026, inspecté) ; IRL T/T-4 2025 en moyenne +1,02 % ; différentiel résiduel +0,12 point, la protection étant pratiquement terminée.
- **Conversion en milliards (RAFRAÎCHIE)** : sur la masse SDES de 95 Md€ de loyers réels des locataires (compte du logement 2024), la protection 2022-2023 vaut environ 1,8 puis 1,2 Md€/an pour les locataires en place ; le rattrapage 2024 environ 0,9 Md€/an.

## Continuité avec l'UPDATE frère

Le gap routé par le parent (extraire le sous-indice « loyers effectifs ») a été clos le même jour par l'UPDATE certifié `20260921-0824 cui-bono-quantification-gap-closure` : série BDM 001763530 extraite, bascule 2025 documentée (ELC +2,32 % > IRL +1,02 %). Le présent run maintient le verdict d'ensemble : ni neutralité ni avantage structurel unidirectionnel ; le transfert est conjoncturel et le rattrapage passe par les révisions annuelles.

## Hygiène mémoire et traçabilité

Les mémoires de faits du parent ont été retrouvées en mémoire (recherche MCP) : la revalidation est enregistrée en mode UPDATE avec référence à la mémoire d'origine, conformément au protocole. Les trois requêtes de réfutation formelles (formule remplacée ? cumuls falsifiés ? série IPC révisée ?) ne retournent aucune contradiction : la fiche Insee en vigueur redit la formule de 2008, les IR n°6 et n°8 convergent, aucune révision incompatible n'est documentée.

## Limites

L'IRL hexagone exclut par dérogation Outre-mer et Corse depuis T3 2022 (IRL spécifiques) ; le périmètre est déclaré à la scoping. L'ELC n'est pas extraite dans ce run — la closure est celle de l'UPDATE frère, citée comme livery liée, pas refaite ici. Les transferts en milliards restent des ordres de grandeur sensibles au périmètre de masse (95 Md€ tous locataires, dont ~60 % privé).

## Verdict

Le parent est confirmé sur toutes ses valeurs ; le complément 2025 renforce la lecture bidirectionnelle (protection 2022-2023, rattrapage 2024-2025). Le run est certifiable : sources primaires inspectées le jour de la livraison, recoupement ANIL/Insee concluant, réfutations vides, routage maintenu.

NARRATIVE_END
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:2|CLM:1|AXS:3|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kinds":["OBJECT"],"lead":"Mecanique IRL: moyenne 12 mois IPC hors tabac hors loyers (fiche Insee + ANIL)","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"kinds":["OBJECT"],"lead":"Ecarts IRL/ELC/IPC-HT 2022-2024 et transferts en milliards (parent) - revalidation","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Revalidation: la mecanique IRL et les ecarts 2022-2024 du parent sont confirmes par les sources primaires","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"TECHNIQUE: niveaux et variations IRL trimestre par trimestre","status":"SATURATED"}
AXS-002 | {"axis":"ECONOMIQUE: ecarts annuels IRL vs ELC vs IPC-HT 2022-2025","status":"SATURATED"}
AXS-003 | {"axis":"CONTRE-HYPOTHESES: fenetre selective, proxy ELC","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"provenance":"convention legale (IRL exclut les loyers) -> revision annuelle -> ecart conjoncturel -> transfert locataires/bailleurs -> rattrapage 2024-2025","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement ANIL vs Insee (niveaux et variations IRL T3-T4 2025)","result":"IRL T3 2025: Insee 145,77 (+0,87 %) = ANIL 145,77 (+0,87 %); T4 2025: 145,78 (+0,79 %) identique; niveaux et variations concordants a l arrondi pres","status":"PASS"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"re-FETCH 4 sources primaires + routage vers cui-bono","intent":"PROVEN","name":"Revalider les faits du parent et maintenir le routage ELC","responsibility_scope":"revalidation","role":"revalidation 2.10.6","source":"-","status":"DONE"}

SEARCH_ACTIVITY_V1:WEB:3|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | mcp-curl-8002 | irl-ecart-loyers-reels-elc | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.insee.fr/fr/statistiques/8655863 | -
QRY-002 | FETCH | FOUND | SRC-002 | https://www.insee.fr/fr/statistiques/8330913 | -
QRY-003 | FETCH | FOUND | SRC-003 | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 | -
QRY-004 | FETCH | FOUND | SRC-004 | https://www.anil.org/outils/indices-et-plafonds/tableau-de-lirl/ | -
QRY-005 | FETCH | FOUND | SRC-005 | https://www.insee.fr/fr/statistiques/8726461 | -
QRY-006 | WEB | FOUND | - | - | REFUTATION mecanique IRL moyenne 12 mois IPC hors tabac hors loyers 12 mois: formule remplacee ou amendee 2024 2025, sous-indice loyers supprime, arrrete modifie
QRY-007 | WEB | FOUND | - | - | REFUTATION ecarts IRL ELC IPC hors tabac 2022 2025 transferts milliards: protection annulee, cumuls falsifies, bascule 2025 contredite, masse 95 milliards revisee
QRY-008 | WEB | FOUND | - | - | REFUTATION IPC hors tabac moyenne annuelle 2022 2025: +5,2 +4,8 +1,8 +0,9 revises ou corriges, cumul +13,2 faux

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8655863
SRC-002 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/8330913
SRC-003 | ◉ | fam:C | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024
SRC-004 | ◈ | fam:B | https://www.anil.org/outils/indices-et-plafonds/tableau-de-lirl/
SRC-005 | ◉ | fam:A | https://www.insee.fr/fr/statistiques/8726461

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.insee.fr/fr/statistiques/8655863 | A,B | 2025-10-15 | Mécanique IRL : moyenne 12 mois de l IPC hors tabac ET hors loyers | IRL = moyenne sur douze mois consecutifs de l evolution de l IPC hors tabac et hors loyers (loi 2008-111 art.9, creation loi 2005-841 art.35); IRL T3 2025 = 145,77 (+0,87 % T/T-4), T4 2025 = 145,78 (+0,79 %); plafond 3,5 % documente par la fiche Insee (loi 2022-1158 art.12, T3 2022-T1 2024); tableau ANIL identique a l arrondi pres | d3f212f5-4b6e-4859-a07e-f938d4d1c47d
FCT-002 | FACT | ✧ | https://www.statistiques.developpement-durable.gouv.fr/rapport-du-compte-du-logement-2024 | A,B,C | 2026-09-21 | Écart IRL / loyers réels 2022-2025 : protection puis rattrapage, transfert chiffré en milliards | Revalidation 2026-09-21 (moyennes annuelles): IRL +3,27/+3,49/+2,75/+1,02 % (2022-2025) vs IPC hors tabac +5,2/+4,8/+1,8/+0,9 %: differentiel IRL-IPC-HT de -1,93/-1,31/+0,95/+0,12 pt; sur la masse SDES de 95 MdEUR de loyers reels, la protection 2022-2023 vaut environ 1,8 puis 1,2 MdEUR/an pour les locataires en place, le rattrapage 2024 environ 0,9 MdEUR/an; l ELC (+0,68/+2,13/+2,34/+2,32 %, extraite par l UPDATE cui-bono) confirme la bascule 2025 | eb0a687b-43d5-4763-b921-a688df2c2d97
FCT-003 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8726461 | A | 2026-01-15 | IPC hors tabac moyenne annuelle 2022-2025 : +5,2/+4,8/+1,8/+0,9 % | IPC hors tabac en moyenne annuelle: +5,2 % (2022), +4,8 % (2023) [IR n6 du 15/01/2025]; +1,8 % (2024) [IR n6]; +0,9 % (2025) [IR n8 du 15/01/2026]; cumul 2022-2025 +13,2 % | e3a3402b-bd87-443a-a981-8fe80c6cc28c
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-004
FCT-002 | SRC-003,SRC-002,SRC-004
FCT-003 | SRC-005,SRC-002

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-006 | NONE
FCT-002 | QRY-007 | NONE
FCT-003 | QRY-008 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | UPDATE | d3f212f5-4b6e-4859-a07e-f938d4d1c47d
FCT-002 | UPDATE | eb0a687b-43d5-4763-b921-a688df2c2d97
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
ATTEMPT-001 | {"created_at":"2026-09-21T08:52:37.601143+00:00","fact_mem":{"FCT-001":"d3f212f5-4b6e-4859-a07e-f938d4d1c47d","FCT-002":"eb0a687b-43d5-4763-b921-a688df2c2d97","FCT-003":"e3a3402b-bd87-443a-a981-8fe80c6cc28c"},"mnemo_row":"PASS: investigation memory WRITE:3be5b181-6843-45ce-bb6e-0f6736db7632; fact writeback 3/3; run 20260921-0826-irl-ecart-loyers-reels-elc","result":"PASS","writeback_execution":[{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"revalidation CONFIRME update memoire parent","success":1},{"action":"UPDATE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"revalidation VERIFIE update memoire parent","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau VERIFIE","success":1}],"writeback_row":{"attempted":3,"blocked":0,"eligible":3,"failure":0,"success":3}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:3be5b181-6843-45ce-bb6e-0f6736db7632; fact writeback 3/3; run 20260921-0826-irl-ecart-loyers-reels-elc | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:3;attempted:3;success:3;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[3 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation CONFIRME update memoire parent
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:revalidation VERIFIE update memoire parent
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
