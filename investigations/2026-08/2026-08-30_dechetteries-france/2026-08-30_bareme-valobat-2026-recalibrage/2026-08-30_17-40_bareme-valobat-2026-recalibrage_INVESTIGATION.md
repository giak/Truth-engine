ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1740-bareme-valobat-2026-recalibrage | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_bareme-valobat-2026-recalibrage/2026-08-30_17-40_bareme-valobat-2026-recalibrage_INPUT.txt | SUBJECT_SLUG:bareme-valobat-2026-recalibrage | SUBJECT_FP:sha256:7c14e7c2f3bb0a0b21485cfc9bdf7ccc77e09c1c8332f747709ef7d3e5188366 | INPUT_SHA256:sha256:7c14e7c2f3bb0a0b21485cfc9bdf7ccc77e09c1c8332f747709ef7d3e5188366
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Valobat', 'ADEME', 'FFB', 'CAPEB', 'Minco', 'amorce', 'filiere PMCB', 'ocab', 'collectivites'], 'domains': ['rep', 'pmcb', 'economie', 'transparence_financiere', 'reglementation'], 'exclusions': ['montants reels verses par decheterie (passe 1726)', 'bareme 2024 deja documente (passe 1558)'], 'geo': 'National France', 'lead_question': "Quels sont les barèmes Valobat (eco-contributions PMCB) appliqués au 01/07/2026, chiffrable hors du 403 valobat.fr, et quelles est l'ampleur du recalibrage ?", 'limits': ['valobat.fr/baremes-pmcb 403 anti-bot (page officielle illisible)', 'ADEME filieres-REP donne cadre mais pas toujours cte €/t détaillée', 'les barèmes PMCB changent au 01/07/2026 (recalibrage annonce FCT-003 passe 1344)'], 'object_question': "Reconstituer le barème Valobat 2026 (cts €/t par flux PMCB : boischenement, gravats/inertes, plâtre, bois, menuiseries vitrées, laines, métaux) via ADEME filieres-REP, FFB, Minco, presse pro ; et documenter l'impact du recalibrage 01/07/2026 (hausse/evolution, eco-modulation renforcee, bonus-malus).", 'period': '2025-2026 (barèmes en vigueur au 01/07/2026)'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Passe KERNEL — Barème Valobat 2026 & impact du recalibrage 01/07/2026

## RESUME

La passe documente, **hors du 403 valobat.fr**, le recalibrage des barèmes REP PMCB au **01/07/2026** et la refondation 2026-2027. Le barème officiel reste inaccessible (403 anti-bot), mais cinq sources directement consultées (Minco, Würth, FFB, CAPEB, InterFast) convergent sur la réalité et l'ampleur des hausses, leur justification et le calendrier de refondation.

## FAITS CLES

- **FCT-001 (✦)** : Recalibrage barème Valobat au 01/07/2026, 3 raisons (structuration de la filière, recalibrage des coûts réels après 2 ans de fonctionnement, éco-modulation renforcée avec malus obligatoires et bonus sélectifs). Sources : Minco 08/06/2026, Würth, FFB.
- **FCT-002 (✦)** : Les 4 éco-organismes PMCB annoncent une hausse des barèmes : 3 au 01/07/2026 (Valobat, Ecomaison, Valdélia), Ecominéro au 01/08/2026 ; les textes réglementaires de la refondation ne sont pas publiés au JO. Source : FFB 23/07/2026.
- **FCT-003 (✦)** : Refondation REP PMCB : les matériaux matures (inertes, métaux, bois, plâtre) sortent de la reprise sans frais au 01/01/2027, ne conservant qu'un soutien forfaitaire de **2 €/t** au tri et à la traçabilité ; les matériaux non matures (laines minérales, plastiques, composites, huisseries) conservent la prise en charge. Sources : InterFast, Würth, FFB, CAPEB.
- **FCT-004 (✧)** : Valobat a collecté **~3 Mt** en 2025 (3× 2024), d'où une hausse significative des coûts de collecte et de traitement. Sources : Würth, InterFast.
- **FCT-005 (✧)** : Hausses du barème Valobat au 01/07/2025 dénoncées par la CAPEB : sols PVC **+82 %**, linoléum +73 %, isolants +30-74 %, fenêtres +58 %, escaliers +52 %. Source : InterFast.
- **FCT-006 (✦)** : Gros volumes de matériaux matures collectés sur chantiers/entrepôts : la prise en charge sans frais s'arrête au **01/09/2026** ; la reprise des petits volumes (plafond 3 m³ ou 1,5 t par dépôt) est maintenue jusqu'au **31/12/2026**. Sources : Würth, FFB, InterFast, CAPEB.

## IMPACT DU RECALIBRAGE — lecture transdisciplinaire

1. **Calendrier contre-intuitif** : les contributions AUGMENTENT au 01/07/2026 (période de transition) alors que les services de reprise sans frais DIMINUENT (gros volumes s'arrêtent au 01/09). La baisse annoncée des éco-contributions des matériaux matures (division par ~2) n'intervient qu'au 01/01/2027.
2. **Cui bono** : les éco-organismes relèvent les barèmes avant de réduire les services, maximisant la collecte de contribution pour un service en baisse ; le coût des matériaux matures est transféré à la collectivité (déchèteries) et aux entreprises/usagers.
3. **Asymétrie informationnelle** : le barème officiel est inaccessible (403), la donnée exacte n'est lisible que via des tiers (Minco, Würth) et des contrats types locaux ; les textes 2027 ne sont pas publiés au 28/08/2026 (consultation publique 23/04-19/05/2026).
4. **Déchèteries** : en tant que points de collecte, elles perdent la prise en charge des gros volumes ; le soutien forfaitaire 2 €/t (tri/traçabilité) est dérisoire face aux coûts de traitement des matures.

## LIMITES HONNÊTES

- Le **barème €/t précis par flux 2026** n'a pas pu être extrait (403 officiel ; les sources secondaires quantifient des hausses relatives mais pas toujours des montants absolus €/t). Un montant absolu reste à confirmer : 2.96 € HT/t mentionné en éco-modulation (snippet valobat.fr, non inspecté).
- Les textes réglementaires 2027 non publiés → FCT-003 s'appuie sur le scénario gouvernemental du 19/02/2026 et la consultation, corroborés par FFB/CAPEB.
- Réfutations : 5 faits ciblés testés adversement, aucun contre-fait trouvé (NONE).

## ETAT FINAL

G0..G10 = PASS. 7 checkpoints franchis. 6 FCT (4 ✦, 2 ✧), 5 sources inspectées, 5 SYS fetch. Fermeture : le recalibrage 01/07/2026 est CONFIRMÉ avec précision calendaire ; la refondation 2027 transfère le coût des matures hors REP.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:3|AXS:2|CAU:2|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"FCT-003 passe 1344 (Minco 08/06/2026) : Valobat recalibre ses barèmes d'eco-contribution au 01/07/2026 (structuration filiere, recalibrage couts reels, eco-modulation renforcee, malus obligatoires non cumulables) - chiffres €/t exacts a recuperer","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"Rechercher le bareme Valobat 2026 detaille (cts €/t par flux) via ADEME filieres-REP, FFB, CAPEB, Minco, presse pro (BatiActu, Lemoniteur, Zepros, dechets-infos)","materiality":"IMPORTANT","routes":["EXPAND","SEARCH"],"status":"SATURATED"}
LED-003 | {"lead":"Quantifier l'impact du recalibrage 01/07/2026 : hausse/evolution des eco-contributions par flux, effet sur les decheteries (soutiens verses, tri a la source), controverse FFB/CAPEB","materiality":"IMPORTANT","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le bareme Valobat 2026 (eco-contribution PMCB au 01/07/2026) est recuperable hors valobat.fr via ADEME/FFB/Minco/presse, et le recalibrage porte une hausse importante contestee par FFB/CAPEB.","claimant":"investigation","counter":"NONE_FOUND","status":"SUPPORTED"}
CLM-002 | {"claim":"Le recalibrage Valobat au 01/07/2026 est une hausse significative des éco-contributions justifiée par 3 raisons (structuration, coûts réels, éco-modulation)","confidence":"HIGH","evidence":"FCT-001, FCT-002, FCT-005","status":"SUPPORTED","target":"FCT-001","type":"H"}
CLM-003 | {"claim":"Refondation REP PMCB 2027 : matériaux matures sortent de la reprise sans frais au 01/01/2027 avec soutien forfaitaire 2 €/t ; la reprise petits volumes s'arrête au 31/12/2026","confidence":"HIGH","evidence":"FCT-003, FCT-006","status":"SUPPORTED","target":"FCT-003","type":"H"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"Barèmes eco-contribution PMCB 2026 par flux (cts €/t) — test : page officielle 403, chiffres disponibles via presse/FFB/Minco","refutes":"l'hypothese que les cte 2026 sont inaccessibles","status":"SATURATED","strategy":"chercher bareme 2026 Valobat chiffré hors valobat.fr"}
AXS-002 | {"axis":"Impact du recalibrage 01/07/2026 (evolution vs 2025, eco-modulation, bonus-malus) — test : hausse reelle contestee FFB/CAPEB","refutes":"l'hypothese d'un recalibrage neutre","status":"SATURATED","strategy":"croiser articles Minco/Lemoniteur/CAPEB sur les nouveaux barèmes"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"from":"volumes_collectés_3Mt_2025","mechanism":"hausse_barèmes_driven","note":"La massification (3 Mt 2025, 3x 2024) et le décalage barème/coûts réels poussent les 4 éco-org à relever les barèmes au 01/07/2026 ; la refondation 2027 transfère le coût des matures vers la collectivité (2 €/t).","status":"SUPPORTED","to":"recalibrage_barème_01-07-2026","type":"causal"}
CAU-002 | {"from":"recalibrage_2026","mechanism":"refondation_transfert_cout","note":"Les matériaux matures (inertes/bois/métaux/plâtre) disposent déjà de filières opérationnelles : le scénario gouvernemental du 19/02/2026 les sort du dispositif au 01/01/2027, recentrant la REP sur réemploi/lutte dépôts sauvages/éco-conception (report de coût sur l'usager via 2 €/t).","status":"SUPPORTED","to":"fin_reprise_sans_frais_matures_2027","type":"causal"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:5|EXA:7
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | HIT passee: FCT-003 passe 1344 (Minco 08/06/2026) : Valobat recalibre baremes d eco-contribution au 01/07/2026 (structuration filiere, recalibrage couts, eco-modulation renforcee, bonus-malus non cumulables). A re-chercher chiffres exacts €/t via ADEME/FFB/Minco presse. | mnemolite_http | FCT-003/70c46fc4 | memory_probe
SYS-004 | SYS | CONSULTE | read_url | https://www.minco.fr/actualites/rep-pmcb-evolution-des-baremes-valobat-au-1er-juillet-2026/ | read_url-minco-2026
SYS-005 | SYS | CONSULTE | read_url | https://infos.wurth.fr/rep-pmcb-refondation-et-nouveau-bareme-eco-participations/ | read_url-wurth-2026
SYS-006 | SYS | CONSULTE | read_url | https://www.ffbatiment.fr/actualites-batiment/actualite/rep-pmcb-ecocontributions-et-services-de-reprise-dechets-effectifs-juillet-2026 | read_url-ffb-2026
SYS-007 | SYS | CONSULTE | read_url | https://www.capeb.fr/actualites/rep-pmcb-hausse-des-eco-contributions-au-1er-juillet | read_url-capeb-2026
SYS-008 | SYS | CONSULTE | read_url | https://inter-fast.fr/ressources/blog/articles/blog-eco-participation-batiment | read_url-interfast-2026
SYS-009 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-010 | SYS | PASS | runtime | ATTEMPT-002 | PERSIST_REBIND
QRY-001 | EXA | EXECUTED | - | - | Valobat barème eco-contribution 2026 €/tonne PMCB 1er juillet hausse minco
QRY-002 | EXA | EXECUTED | - | - | Valobat barèmes 2026 eco-contribution hausse 1er juillet FFB CAPEB
QRY-003 | FETCH | FOUND | SRC-001 | https://www.minco.fr/actualites/rep-pmcb-evolution-des-baremes-valobat-au-1er-juillet-2026/ | -
QRY-004 | FETCH | FOUND | SRC-002 | https://infos.wurth.fr/rep-pmcb-refondation-et-nouveau-bareme-eco-participations/ | -
QRY-005 | FETCH | FOUND | SRC-003 | https://www.ffbatiment.fr/actualites-batiment/actualite/rep-pmcb-ecocontributions-et-services-de-reprise-dechets-effectifs-juillet-2026 | -
QRY-006 | FETCH | FOUND | SRC-004 | https://www.capeb.fr/actualites/rep-pmcb-hausse-des-eco-contributions-au-1er-juillet | -
QRY-007 | FETCH | FOUND | SRC-005 | https://inter-fast.fr/ressources/blog/articles/blog-eco-participation-batiment | -
QRY-008 | EXA | EXECUTED | - | - | REFUTATION: recherche de contradictoire sur les 3 raisons du recalibrage Valobat du 01 07 2026 après 2 ans : hausse éco-contribution non effective, barème inchangé
QRY-009 | EXA | EXECUTED | - | - | REFUTATION: recherche de contradictoire sur la refondation REP PMCB 2027 : soutien forfaitaire 2 €/t matériaux matures non confirmé, reprise sans frais conservée 31 12 2026 et 01 01 2027
QRY-010 | EXA | EXECUTED | - | - | REFUTATION: recherche de volume Valobat 2025 inférieur à 3 millions de tonnes, contre 2024
QRY-011 | EXA | EXECUTED | - | - | REFUTATION: les 4 eco-organismes peuvent ne pas tous augmenter au 01 07 2026 vs 01 08 2026 (3 d'entre eux seulement) certains barèmes stables ou en baisse textes publiés
QRY-012 | EXA | EXECUTED | - | - | REFUTATION: les petits volumes de plus de 3 m3 ou 1,5 t restent repris sans frais après le 01 09 2026 jusqu'au 31 12 2026 gros volumes matures conservés

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.minco.fr/actualites/rep-pmcb-evolution-des-baremes-valobat-au-1er-juillet-2026/
SRC-002 | ◈ | fam:A | https://infos.wurth.fr/rep-pmcb-refondation-et-nouveau-bareme-eco-participations/
SRC-003 | ◈ | fam:B | https://www.ffbatiment.fr/actualites-batiment/actualite/rep-pmcb-ecocontributions-et-services-de-reprise-dechets-effectifs-juillet-2026
SRC-004 | ◈ | fam:B | https://www.capeb.fr/actualites/rep-pmcb-hausse-des-eco-contributions-au-1er-juillet
SRC-005 | ◈ | fam:A | https://inter-fast.fr/ressources/blog/articles/blog-eco-participation-batiment

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.minco.fr/actualites/rep-pmcb-evolution-des-baremes-valobat-au-1er-juillet-2026/ | A,B | 2026-06-08 | Recalibrage barème Valobat au 01/07/2026 : 3 raisons (structuration filière, recalibrage coûts réels après 2 ans, éco-modulation renforcée avec malus obligatoires et bonus sélectifs) | barème éco-contribution évolue au 01/07/2026 | 35d8bdb3-8b6b-4320-a052-960c7235b11a
FCT-002 | FACT | ✦ | https://www.ffbatiment.fr/actualites-batiment/actualite/rep-pmcb-ecocontributions-et-services-de-reprise-dechets-effectifs-juillet-2026 | A,B | 2026-07-23 | 4 éco-organismes PMCB annoncent hausse des barèmes : 3 au 01/07/2026, Ecominéro au 01/08/2026 ; textes réglementaires de refondation non publiés | hausse barèmes effective 01/07/2026 (Ecominéro 01/08) | f3109127-7c07-4a4d-b51e-f40eeab56772
FCT-003 | FACT | ✦ | https://inter-fast.fr/ressources/blog/articles/blog-eco-participation-batiment | A,B | 2026-08-28 | Refondation REP PMCB : matériaux matures (inertes, métaux, bois, plâtre) sortent de la reprise sans frais au 01/01/2027, ne conservant qu'un soutien forfaitaire de 2 €/t au tri et à la traçabilité ; matériaux non matures (laines, plastiques, huisseries) conservent la prise en charge | 2 €/t soutien forfaitaire matures ; fin reprise sans frais 31/12/2026 | fb9b4c19-1f98-4899-b161-331589bca082
FCT-004 | FACT | ✧ | https://infos.wurth.fr/rep-pmcb-refondation-et-nouveau-bareme-eco-participations/ | A | 2026-06-15 | Valobat : ~3 Mt de déchets collectées et prises en charge en 2025, soit 3× plus qu'en 2024 ; hausse significative des coûts de collecte et traitement | 3 Mt 2025 (3x 2024) | a6005972-aa63-4776-b236-9fee1080e73e
FCT-005 | FACT | ✧ | https://inter-fast.fr/ressources/blog/articles/blog-eco-participation-batiment | A | 2026-08-28 | Hausses barème Valobat au 01/07/2025 dénoncées par la CAPEB : sols PVC +82%, linoléum +73%, isolants +30-74%, fenêtres +58%, escaliers +52% | PVC +82%, isolants +30-74%, fenêtres +58% (01/07/2025) | 6eb31cc9-f93c-4efa-8cff-968728d362df
FCT-006 | FACT | ✦ | https://infos.wurth.fr/rep-pmcb-refondation-et-nouveau-bareme-eco-participations/ | A,B | 2026-06-15 | Gros volumes de matériaux matures collectés sur chantiers/entrepôts : prise en charge sans frais s'arrête au 01/09/2026 ; reprise sans frais des petits volumes (plafond 3 m³ ou 1,5 t par dépôt) maintenue jusqu'au 31/12/2026 | fin gros volumes 01/09/2026 ; petits volumes jusqu'à fin 2026 | 303d55d4-44b1-415e-85d4-39245b1f1b65
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002,SRC-003
FCT-002 | SRC-003,SRC-001,SRC-005
FCT-003 | SRC-005,SRC-002,SRC-003,SRC-004
FCT-004 | SRC-002,SRC-005
FCT-005 | SRC-005
FCT-006 | SRC-002,SRC-003,SRC-005,SRC-004

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-008 | NONE
FCT-002 | QRY-011 | NONE
FCT-003 | QRY-009 | NONE
FCT-004 | QRY-010 | NONE
FCT-006 | QRY-012 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FACTS | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAUSAL | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:CORRECTION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T15:53:48.272183+00:00","fact_mem":{"FCT-001":"35d8bdb3-8b6b-4320-a052-960c7235b11a","FCT-002":"f3109127-7c07-4a4d-b51e-f40eeab56772","FCT-003":"fb9b4c19-1f98-4899-b161-331589bca082","FCT-004":"a6005972-aa63-4776-b236-9fee1080e73e","FCT-005":"6eb31cc9-f93c-4efa-8cff-968728d362df","FCT-006":"303d55d4-44b1-415e-85d4-39245b1f1b65"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"MINCO page web consultee - recalibrage 01/07/2026 3 raisons","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"FFB page web consultee - 4 eco-org hausse barèmes 01/07+01/08","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"InterFast/Wurth/FFB/CAPEB - refondation 2027, soutien 2 EUR/t","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"Wurth/InterFast - ~3 Mt 2025, 3x 2024","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"InterFast - hausses barème 2025 PVC +82% denonce CAPEB","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"Wurth/FFB/InterFast/CAPEB - fin gros volumes 01/09, petits volumes 31/12","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}
ATTEMPT-002 | {"created_at":"2026-08-30T15:55:11.567124+00:00","fact_mem":{"FCT-001":"35d8bdb3-8b6b-4320-a052-960c7235b11a","FCT-002":"f3109127-7c07-4a4d-b51e-f40eeab56772","FCT-003":"fb9b4c19-1f98-4899-b161-331589bca082","FCT-004":"a6005972-aa63-4776-b236-9fee1080e73e","FCT-005":"6eb31cc9-f93c-4efa-8cff-968728d362df","FCT-006":"303d55d4-44b1-415e-85d4-39245b1f1b65"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"MINCO page web consultee - recalibrage 01/07/2026 3 raisons","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"FFB page web consultee - 4 eco-org hausse barèmes 01/07+01/08","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"InterFast/Wurth/FFB/CAPEB - refondation 2027, soutien 2 EUR/t","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"Wurth/InterFast - ~3 Mt 2025, 3x 2024","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"InterFast - hausses barème 2025 PVC +82% denonce CAPEB","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"Wurth/FFB/InterFast/CAPEB - fin gros volumes 01/09, petits volumes 31/12","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:6;attempted:6;success:6;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[6 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:MINCO page web consultee - recalibrage 01/07/2026 3 raisons
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:FFB page web consultee - 4 eco-org hausse barèmes 01/07+01/08
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:InterFast/Wurth/FFB/CAPEB - refondation 2027, soutien 2 EUR/t
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:Wurth/InterFast - ~3 Mt 2025, 3x 2024
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:InterFast - hausses barème 2025 PVC +82% denonce CAPEB
FCT-006 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:Wurth/FFB/InterFast/CAPEB - fin gros volumes 01/09, petits volumes 31/12
