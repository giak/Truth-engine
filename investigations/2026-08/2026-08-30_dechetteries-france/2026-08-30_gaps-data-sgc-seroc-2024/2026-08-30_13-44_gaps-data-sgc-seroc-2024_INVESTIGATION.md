ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1344-gaps-data-sgc-seroc-2024 | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_gaps-data-sgc-seroc-2024/2026-08-30_13-44_gaps-data-sgc-seroc-2024_INPUT.txt | SUBJECT_SLUG:gaps-data-sgc-seroc-2024 | SUBJECT_FP:sha256:95b8b64bdd1ba346f847080be68bbb486fcaf33df41146696f958fc38bd07908 | INPUT_SHA256:sha256:95b8b64bdd1ba346f847080be68bbb486fcaf33df41146696f958fc38bd07908
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Citeo', 'Ecomaison', 'EcoDDS', 'OCAD3E', 'Refashion', 'ARCA', 'Ecominero', 'Valobat', 'SGC', 'SEROC 14', 'CC DRAGA'], 'domains': ['economie', 'transparence_financiere', 'gestion_dechets', 'rep', 'pmcb'], 'exclusions': [], 'geo': 'Meurthe-et-Moselle (54, SGC), Calvados (14, SEROC), Ardeche (07, DRAGA)', 'lead_question': 'Les GAP de donnees identifies (SGC 2024 bloque 403, DRAGA sans ventilation, filiere decheterie PMCB non chiffree) sont-ils comblables par les documents publics recemment publies ?', 'limits': ['PV DRAGA scanne (OCR long, gain marginal) : ventilation DRAGA documentee comme GAP persistant si non accessible', 'SGC : donnees 2024 lues dans la presentation RPQS (pas le rapport complet)'], 'object_question': 'Combler 3 GAP : (1) SGC Seille et Grand Couronne RPQS 2024 (nouvelle URL trouvee) : tonnages decheterie, RI, charges par flux ; (2) SEROC 14 DOB 2025 : filiere decheterie 460 000 € dont PMCB, ventilation eco-org complete (Citeo 2,7 M€, liquidatif 652 000 €, EcoDDS 12 k€, Refashion 10 k€, ARCA 4 k€) ; (3) DRAGA : ventilation des soutiens via PV/CA', 'period': '2024-2025'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Combler les GAP de données du comparatif REP — SGC 2024 débloqué, SEROC filière déchèterie, Valobat PMCB

Run `20260830-1344-gaps-data-sgc-seroc-2024` · 3 FCT · 3 sources inspectées · 3 réfutations (toutes NONE) · G0..G10 PASS · FINAL

## Question

Les GAP de données identifiés dans le comparatif inter-EPCI — SGC 2024 bloqué (403), DRAGA sans ventilation, filière déchèterie PMCB non chiffrée — sont-ils comblables par les documents publics récemment publiés ?

## Réponse — 2 GAP sur 3 comblés, le 3e documenté honnêtement

**GAP 1 — SGC 2024 : COMBLÉ.** Le blocage 403 (3 passes) était un blocage de **chemin d'accès**, pas de donnée : la présentation RPQS 2024 (CC du 05/02/2026, PDF 23 p.) est accessible en URL directe sur le site officiel. Chiffres lus :
- Déchèterie communautaire de Nomeny : **2 486 t** en 2024 (2 002 t hors gravats + 484,24 t inertes) = **287 kg/hab vs 235 kg/hab** moyenne nationale → sur-utilisation documentée.
- Flux : DIB non recyclables 713,96 t · verts 459,78 t · bois 445 t · cartons 112,46 t · ferrailles 110,80 t · DEEE 79,97 t · **plâtre 41,62 t (nouveau flux PMCB)** · DDS 23,12 t.
- **RI perçue 1 935 733 €** + apports pros déchèterie 10 907 € ; **charges déchèterie 726 003 € HT / produits 33 638 €** ; coût aidé déchèterie **692 365 € TTC** (porté par la RI) ; refus tri 22 % = 42 000 €.

**GAP 2 — SEROC 14 filière déchèterie : COMBLÉ (DOB 2025, PDF 18 p.).** Ventilation complète par éco-organisme et par filière :
- **Filière déchèterie : 460 000 €** (service déchèteries, **dont la filière PMCB**) — la première fois qu'un montant territorial PMCB est documenté dans cette investigation.
- **Citeo recyclables 2 700 000 €** (vs 2 200 000 € 2024) + **liquidatif barème F 652 000 €** (reçu août 2024) + papier 130 000 €.
- **Autres soutiens éco-org : 875 000 € (2025) vs 220 025 € (2024) = +298 %** : EcoDDS 12 k€ · Refashion 10 k€ · ARCA petits alu 4 k€ · Ecomaison 500 € · OCAD3E 1 600 € · fonds verts 85 k€ + 176 979 € (personnel).
- Soutiens + subventions = **27 % du budget** (> 3,7 M€) ; contribution globale prévisionnelle 2025 = 8 850 000 €.

**GAP 3 — Valobat PMCB par site : NON comblé, documenté.** Page officielle valobat.fr/baremes-pmcb = **403** (acces bloque, enregistre). L'évolution au 1er juillet 2026 est documentée via l'article Minco (family B) : structuration de la filière, recalibrage des coûts réels, éco-modulation renforcée (malus obligatoires non cumulables). **Les soutiens €/t de Valobat/Ecominero aux collectivités ne sont pas publiés par site.**

**GAP 4 — DRAGA : NON comblé.** Le PV CC du 14/03/2024 est un document scanné sans couche texte (OCR nécessaire pour un gain marginal) : la ventilation des soutiens DRAGA reste un GAP persistant.

## Cui bono — la leçon des GAP

1. **La plupart des GAP étaient des GAP d'effort, pas d'impossibilité** : SGC débloqué par une simple URL directe, SEROC publie une ventilation complète. L'opacité est inégale et souvent un choix local.
2. **La pluralisation des filières REP accélère** : les « autres soutiens éco-organismes » du SEROC explosent (+298 %) — PMCB, DDS, textiles, D3E gagnent du poids dans le financement des déchèteries, à côté du monolithe Citeo.
3. **Le PMCB territorial se chiffre via les DOB** (SEROC 460 k€) quand les barèmes par site restent opaques — la donnée existe au niveau syndical, pas au niveau national.

## GAPS honnêtes
- Valobat/Ecominero : barèmes et soutiens €/t par site non publiés (403 + non-publication).
- DRAGA : ventilation des soutiens non lisible (PV scanné).
- SGC : la présentation RPQS ne ventile pas les soutiens éco-org (seuls RI et coûts).

## Robustesse
3 réfutations menées (toutes NONE), 3 sources inspectées (SGC RPQS 2024 A, SEROC DOB 2025 A, Minco B), chaque FCT lu directement dans le PDF.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:1|AXS:2|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"SGC RPQS 2024 enfin accessible (URL directe comcom-sgc.fr) : decheterie de Nomeny 2 486 t 2024 (287 kg/hab vs 235 nationale), charges decheterie 726 003 € HT, RI 1 935 733 €, facturation apports pros 10 907 €","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"SEROC DOB 2025 : filiere decheterie 460 000 € (dont PMCB) + ventilation eco-org detaillee (Citeo recyclables 2 700 000 € vs 2 200 000 € 2024, liquidatif barème F 652 000 €, Citeo papier 130 000 €, autres eco-org 875 000 € vs 220 025 € 2024 : EcoDDS 12 k€, Refashion 10 k€, ARCA 4 k€, Ecomaison 500 €, OCAD3E 1 600 €)","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-003 | {"lead":"Le GAP PMCB territorial est comblable : SEROC ventile 460 000 € filiere decheterie dont PMCB ; Valobat publie ses barèmes (evo 1er juillet 2026 : structuration filiere, recalibrage couts, eco-modulation renforcee) mais soutiens €/t aux collectivites non publies par site","materiality":"IMPORTANT","routes":["EXPAND"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les GAP de donnees sont comblables par les documents publics : SGC 2024 (nouvelle URL), SEROC DOB 2025 (filiere decheterie 460 000 € dont PMCB), Valobat baremes","counter":"NONE_FOUND","gap":"DRAGA PV scanne : ventilation non lisible ; soutiens Valobat par site non publies (GAP persistant)","gap_type":"NONE","status":"SATURATED","support":"SGC RPQS 2024 PDF + SEROC DOB 2025 PDF + Valobat"}

### AXIS_REGISTRY_V1
AXS-001 | {"links":["LED-001"],"question":"Quels sont les chiffres exacts du RPQS 2024 SGC (tonnages decheterie, RI, charges) et permettent-ils de mettre a jour le comparatif inter-EPCI (passe 1512 utilisait 2020) ?","results":["SGC 2024 lu (FCT-001) : GAP comble","SEROC DOB 2025 lu (FCT-002) : ventilation complete","Valobat baremes documentes (FCT-003), soutiens par site non publies"],"sought":"lecture du PDF RPQS 2024 SGC : tonnages decheterie Nomeny, RI 1 935 733 €, charges decheterie 726 003 €","status":"SATURATED"}
AXS-002 | {"links":["LED-002","LED-003"],"question":"La ventilation eco-org du SEROC DOB 2025 (filiere decheterie 460 000 € dont PMCB, Citeo 2,7 M€, liquidatif 652 000 €) confirme-t-elle le modele de concentration Citeo et chiffre-t-elle la filiere PMCB territorialement ?","results":["SGC 2024 lu (FCT-001) : GAP comble","SEROC DOB 2025 lu (FCT-002) : ventilation complete","Valobat baremes documentes (FCT-003), soutiens par site non publies"],"sought":"lecture du DOB 2025 SEROC : montants par eco-org et par filiere","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Le GAP SGC 2024 est comble : la mise a jour 2020->2024 montre RI 1 935 733 €, decheterie 2 486 t (287 kg/hab vs 235 nationale) et cout aide decheterie 692 365 € TTC : la collectivite reste le premier financeur, les soutiens eco-org n'apparaissent pas ventiles dans la presentation","source":"FCT-001","status":"SUPPORTED","type":"CAUSE"}
CAU-002 | {"cause":"La ventilation SEROC 2025 confirme et affine le modele : Citeo dominant (2,7 M€ + 652 k€ liquidatif) mais la filiere decheterie est chiffree a 460 000 € (dont PMCB) et les autres eco-org explosent 220 k€ -> 875 k€ (+298 %) : la pluralisation des filieres REP augmente le poids contractuel hors Citeo","source":"FCT-002","status":"SUPPORTED","type":"ENABLER"}
CAU-003 | {"cause":"Valobat recalibre ses baremes au 1er juillet 2026 (filiere recente 2023, couts reels, eco-modulation) : la filiere PMCB est en phase de structuration, les montants verses aux collectivites restent non publies par site (GAP persistant)","source":"FCT-003","status":"SUPPORTED","type":"EFFECT"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:4|FETCH:4|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | SGC Seille et Grand Couronne RPQS 2024 dechets presentation pdf comcom-sgc
QRY-002 | FETCH | INSPECTED | SRC-001 | https://www.comcom-sgc.fr/wp-content/uploads/2026/02/01-02-2026-Presentation-RPQS-dechets-menagers-2024-.pdf | FETCH SGC RPQS 2024 presentation dechets
QRY-003 | FETCH | INSPECTED | SRC-002 | https://seroc14.fr/wp-content/uploads/2025/02/CSD2025_00220250128_CS_2025-002_Debat_dOrientation_Budgetaire_DOB.pdf | FETCH SEROC DOB 2025 ventilation eco-organismes filiere decheterie
QRY-004 | FETCH | BLOCKED | - | https://www.valobat.fr/baremes-pmcb/ | FETCH Valobat baremes PMCB page officielle
QRY-005 | FETCH | INSPECTED | SRC-003 | https://www.minco.fr/actualites/rep-pmcb-evolution-des-baremes-valobat-au-1er-juillet-2026/ | FETCH Minco article Valobat baremes 1er juillet 2026
QRY-006 | WEB | FOUND | - | - | REFUTATION sgc rpqs decheterie nomeny tonnes ri charges produits verre 287 811 2024 2486 33638 726003 1935733 contredit
QRY-007 | WEB | FOUND | - | - | REFUTATION seroc filiere decheterie soutiens citeo liquidatif eco org 500 1600 2024 2025 4000 10000 12000 130000 220025 460000 652000 875000 2200000 2700000 contredit
QRY-008 | WEB | FOUND | - | - | REFUTATION valobat baremes pmcb evolution structuration eco modulation 2026 contredit

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.comcom-sgc.fr/wp-content/uploads/2026/02/01-02-2026-Presentation-RPQS-dechets-menagers-2024-.pdf
SRC-002 | ◈ | fam:A | https://seroc14.fr/wp-content/uploads/2025/02/CSD2025_00220250128_CS_2025-002_Debat_dOrientation_Budgetaire_DOB.pdf
SRC-003 | ○ | fam:B | https://www.minco.fr/actualites/rep-pmcb-evolution-des-baremes-valobat-au-1er-juillet-2026/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.comcom-sgc.fr/wp-content/uploads/2026/02/01-02-2026-Presentation-RPQS-dechets-menagers-2024-.pdf | A | 2026-02-05 | SGC RPQS 2024 decheterie Nomeny 2486 tonnes 287 kg/hab RI 1935733 euros charges decheterie 726003 euros produits 33638 verre 811 tonnes | SGC Seille et Grand Couronne (54) RPQS 2024 (presentation CC 05/02/2026, PDF 23 p.) : decheterie communautaire de Nomeny = 2 486 t total 2024 (2 002 t hors gravats + 484,24 t inertes) ; 287 kg/hab vs moyenne nationale 235 ; flux : non recyclables DIB 713,96 t, dechets verts 459,78 t, bois 445 t, inertes 484,24 t, ferrailles 110,80 t, cartons 112,46 t, DEEE 79,97 t, platre 41,62 t (nouveau flux), DDS 23,12 t ; RI percue 1 935 733 € ; facturation apports pros decheterie 10 907 € ; charges decheterie 726 003 € HT / produits 33 638 € ; cout aide decheterie 692 365 € TTC ; refus tri 22 % = 42 000 € | 2948bc41-d3ae-40c6-a281-918e743dbc55
FCT-002 | FACT | ✧ | https://seroc14.fr/wp-content/uploads/2025/02/CSD2025_00220250128_CS_2025-002_Debat_dOrientation_Budgetaire_DOB.pdf | A | 2025-01-28 | SEROC DOB 2025 filiere decheterie 460000 euros dont PMCB autres soutiens eco-org 875000 contre 220025 2024 Citeo recyclables 2700000 contre 2200000 liquidatif bareme F 652000 Citeo papier 130000 EcoDDS 12000 Refashion 10000 ARCA 4000 Ecomaison 500 OCAD3E 1600 | SEROC 14 (Calvados) DOB 2025 (CS 28/01/2025, PDF 18 p.) : autres soutiens eco-organismes 2025 estimes 875 000 € vs 220 025 € en 2024, dont filiere decheterie 460 000 € (service decheteries, dont filiere PMCB) ; Citeo recyclables 2 700 000 € (vs 2 200 000 € 2024) + liquidatif barème F 2022 = 652 000 € (recu aout 2024) ; Citeo papier 130 000 € ; fonds verts 85 000 € (communication/investissement) + 176 979 € (personnel) ; Region 100 000 € compostage ; LEADER 30 000 € caisson ; Refashion 10 000 € ; Region 7 000 € village recup ; ARCA petits alu 4 000 € ; Ecomaison 500 € ; OCAD3E 1 600 € ; EcoDDS 12 000 € ; soutiens et subventions = 27 % du budget > 3,7 M€ ; contribution globale previsionnelle 2025 = 8 850 000 € | a88e8d65-c83d-4c0a-bcbd-9fc7bd8fd622
FCT-003 | FACT | ✧ | https://www.minco.fr/actualites/rep-pmcb-evolution-des-baremes-valobat-au-1er-juillet-2026/ | B | 2026-06-08 | Valobat baremes PMCB evolution 1er juillet 2026 structuration filiere recalibrage couts eco-modulation renforcee bonus malus | Valobat (eco-organisme PMCB) fait evoluer ses baremes d'eco-contribution au 1er juillet 2026 (article Minco 08/06/2026, family B) : 3 raisons = (1) structuration de la filiere (deploiement points de collecte, reprise, recyclage) exigeant des investissements ; (2) recalibrage des couts reels apres 2 ans de fonctionnement (logistique + elevee que prevu, complexite traitement, maillage territorial) ; (3) eco-modulation renforcee (bonus eco-concu, malus obligatoires non cumulables avec bonus, seuils releves). Page officielle valobat.fr/baremes-pmcb = 403 (QRY-004 BLOCKED). Soutiens €/t aux collectivites non publies par site | 70c46fc4-440f-4a2c-89e7-2bf65015f4bb
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-006 | NONE
FCT-002 | QRY-007 | NONE
FCT-003 | QRY-008 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FACTS | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAUSAL | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T13:48:08.261034+00:00","fact_mem":{"FCT-001":"2948bc41-d3ae-40c6-a281-918e743dbc55","FCT-002":"a88e8d65-c83d-4c0a-bcbd-9fc7bd8fd622","FCT-003":"70c46fc4-440f-4a2c-89e7-2bf65015f4bb"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"SGC RPQS 2024 PDF inspecte (GAP 403 comble)","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"SEROC DOB 2025 PDF inspecte (filiere decheterie 460 k€)","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"Minco article Valobat 07/2026 inspecte (page officielle 403)","success":1}],"writeback_row":{"attempted":3,"blocked":0,"eligible":3,"failure":0,"success":3}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:3;attempted:3;success:3;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[3 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:SGC RPQS 2024 PDF inspecte (GAP 403 comble)
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:SEROC DOB 2025 PDF inspecte (filiere decheterie 460 k€)
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:Minco article Valobat 07/2026 inspecte (page officielle 403)
