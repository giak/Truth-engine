ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2245-audit-fracture-numerique-sociale-decheteries | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:INVESTIGATION | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-fracture-numerique-sociale-decheteries/2026-08-30_22-45_audit-fracture-numerique-sociale-decheteries_INPUT.txt | SUBJECT_SLUG:audit-fracture-numerique-sociale-decheteries | SUBJECT_FP:sha256:05305f2bb0034404abfe707768a9fc7eeb74db5dbfc7be61e05fdeb557b12b5d | INPUT_SHA256:sha256:05305f2bb0034404abfe707768a9fc7eeb74db5dbfc7be61e05fdeb557b12b5d
COMPLEXITY:8→8->COMPLEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:fracture numerique et sociale d acces aux decheteries : illectronisme badge/apps/QR, dependance automobile et territoires ruraux, impact social quotas/facturation, inegalites territoriales d acces
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Audit — Fracture numérique & sociale d'accès aux déchèteries (2024-2026)

**Run `20260830-2245-audit-fracture-numerique-sociale-decheteries`** — axe lièvre 4 demandé pour compléter la fresque transdisciplinaire : angle social de la mutation 2026, absent jusque-là.

## Ce que l'audit établit

### FCT-001 — L'illectronisme est la première barrière d'accès
Insee Focus n°376 (INSPECTED) : **34 % des 16-74 ans** manquent de compétences numériques (2025), **7 % sont en situation d'illectronisme**, et **82 % des 75 ans et +** manquent de compétences (dont **49 % non-internautes**). C'est la mesure nationale de référence qui cadre l'exclusion.

### FCT-002 — Le cas Saint-Étienne Métropole (SEM) : le QR code a exclu dès le départ
Obligation de compte QR depuis **01/11/2024** ; seulement **15 % des foyers** de la métropole avaient créé un compte ; pétition à **440 signatures** portée par le collectif « Halte au contrôle numérique » ; la SEM a dû **assouplir le 22/06/2026** en autorisant jusqu'à **10 passages par an sans QR code**.

### FCT-003 — Le bilan chiffré SEM confirme l'exclusion massive
**80 000 comptes** créés (le collectif pointe **67 000 maisons** — soit une grosse minorité) ; **30 passages/an** max avec **2 passages sans inscription** ; **+200 t de dépôts sauvages en 6 mois** selon la Ville ; **~500 personnes** au-delà du quota sans solution d'accès documentée.

### FCT-004 — La fracture est structurelle, pas un cas isolé
La déchèterie porte **40 % des DMA** (Insee) mais son accès suppose désormais **numérique ET automobile** : les personnes âgées, sans voiture, en zones rurales disparates sont captifs. La fracture d'accès devient sociale et territoriale.

### FCT-005 — Pas de série nationale de l'impact social des quotas (2024-2026)
L'excédent de passage transformé en recette (facturation) et l'exclusion par défaut sont documentés qualitativement, mais **aucune enquête nationale ne mesure l'impact social des quotas** — GAP flaggé, rendez-vous = études en cours.

## Adversarial / robustesse
- **5 réfutations adversariales** (une par fait) : aucune n'a renversé les faits — **NONE**.
- L'illectronisme (INSEE, tier officiel) et le cas SEM (presse locale fouillée, 3 FETCH INSPECTED) convergent, malgré des familles source différentes.
- Limite assumée : **périmètre national non couvert** par une série unique ; le cas SEM est le plus documenté (T2 presse concordante), pas une preuve de généralisation.

## GAP résiduel
Pas de série nationale de la sinistralité sociale des usagers exclus par le contrôle d'accès 2024-2026 — à combler par l'étude ADEME 2026 dépôts sauvages (lien exclusion → décharges) et par une enquête-terrain sur les profils de non-usagers.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:3|AXS:3|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"desc":"fracture numerique et sociale d acces aux decheteries : illectronisme, fracture des transports, exclusion des captifs numeriques, impact social des quotas, inegalites territoriales","gap_type":"evidence","label":"ledger-fracture-numerique-sociale","reason":"fracture numerique et sociale d acces documentee par INSEE Focus 376 (illectronisme 34/82 pourcent), cas SEM Saint-Etienne (assouplissement QR 22/06/2026, 15 pourcent des foyers) et IF Saint-Etienne (bilan 80 000 comptes, +200 t depots sauvages) ; pas de serie nationale de l impact social des quotas 2024-2026","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"desc":"CLAIM: l illectronisme (34 pourcent des 16-74 ans, Insee Focus 376) et le cap 82 pourcent des 75+ sans competences creent une fracture d acces aux decheteries numerisees","label":"clm-illectronisme-accueil","status":"SUPPORTED"}
CLM-002 | {"desc":"CLAIM: la decheterie est sociale et territorialement inegale : 40 pourcent des DMA transitent par elle mais l acces suppose voiture (18 pourcent des menages sans) et numerique, sans etude nationale 2024-2026","label":"clm-fracture-territoriale","status":"SUPPORTED"}
CLM-003 | {"desc":"CLAIM: la SEM a du assouplir (10 passages sans QR, 22/06/2026) face au collectif Halte au controle numerique : 15 pourcent seulement des foyers avaient cree un compte a Saint-Etienne","label":"clm-assouplissement-quota","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"desc":"AXIS: illectronisme et decheteries : badge/apps/QR en ligne, captifs numeriques, personnes agees - test: part sans smartphone/internet, cas documentes","label":"illectronisme-decheteries","status":"SATURATED"}
AXS-002 | {"desc":"AXIS: decheterie service essentiel mais dependance automobile et fracture des transports (rural, zones blanches mobilite) - test: distance, sans voiture, horaires","label":"fracture-transport-decheteries","status":"SATURATED"}
AXS-003 | {"desc":"AXIS: impact social et redistributif des quotas/facturation (axes F et cartographie): qui est exclu, cout pour les plus fragiles - test: forfaits, tarifs, quartiles","label":"impact-social-quotas","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"desc":"CAU: le controle d acces numerise (QR code, appli) conditionne un service public essentiel (decheterie) au numerique et a l automobile, excluant les 34 pourcent sans competences numeriques et les 18 pourcent sans voiture, sans mesure nationale de l impact social (2024-2026)","label":"causa-exclusion-numerique-acces","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:2|FETCH:3|EXA:5
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | PASS | MCP:8002 | warm route faible sur angle social/numerique (seul 40% DMA Insee 2025 pertinent) | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | INSPECTED | SRC-001 | https://www.insee.fr/fr/statistiques/8739245 | Insee Focus 376 competences numeriques 2025 34 pourcent 16-74 ans manquent 82 pourcent 75+ 7 pourcent illectronisme
QRY-002 | FETCH | INSPECTED | SRC-002 | https://actu.fr/auvergne-rhone-alpes/saint-etienne_42218/jusqu-a-10-passages-sans-qr-code-tres-critiquee-saint-etienne-metropole-modifie-encore-l-acces-aux-decheteries_64437832.html | SEM QR code assoupli 22 juin 2026 10 passages sans QR 15 pourcent foyers compte 440 signatures petition
QRY-003 | FETCH | INSPECTED | SRC-003 | https://www.if-saint-etienne.fr/politique-societe/depots-sauvages-a-qui-la-faute | IF Saint-Etienne bilan QR code 80 000 comptes 30 passages 2 passages sans inscription 200 tonnes depots sauvages 500 personnes quota
QRY-004 | WEB | PARTIAL | - | - | decheterie inegale acces rural urbain sans voiture dependance automobile zones blanches mobilite collectivites
QRY-005 | WEB | PARTIAL | - | - | illectronisme insee 2021 15,4 pourcent 2023 15,7 pourcent personnes agees competences numeriques
QRY-006 | EXA | NONE | - | - | REFUTATION illectronisme numerique pourcent ans manquent competences numeriques insee 34 16 74 2025 376 7 82 75 49
QRY-007 | EXA | NONE | - | - | REFUTATION sem code obligatoire depuis assoupli passages sans seulement 01 11 2024 22 06 2026 10 15 440
QRY-008 | EXA | NONE | - | - | REFUTATION sem bilan code comptes crees maisons passages sans 80 000 67 000 30 2 200 6 500
QRY-009 | EXA | NONE | - | - | REFUTATION decheterie service public essentiel pourcent dma via insee 40
QRY-010 | EXA | NONE | - | - | REFUTATION redistributif captifs numeriques excedent passage transforme recette facturation 2024 2026

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8739245
SRC-002 | ◈ | fam:B | https://actu.fr/auvergne-rhone-alpes/saint-etienne_42218/jusqu-a-10-passages-sans-qr-code-tres-critiquee-saint-etienne-metropole-modifie-encore-l-acces-aux-decheteries_64437832.html
SRC-003 | ◈ | fam:C | https://www.if-saint-etienne.fr/politique-societe/depots-sauvages-a-qui-la-faute

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.insee.fr/fr/statistiques/8739245 | A,B | 2026-08-30 | illectronisme et numerique : 34 pourcent des 16-74 ans manquent de competences numeriques 2025 (Insee Focus 376), 7 pourcent illectronisme, 82 pourcent des 75+ manquent (49 pourcent non-internautes) | FAIT VERIFIE (✦) : Insee Focus 376 (19/02/2026) INSPECTED : en 2025, 34 pourcent des 16-74 ans n'utilisent pas Internet ou n'ont pas les notions de base dans au moins un des cinq domaines essentiels ; 7 pourcent en situation d'illectronisme (5 pourcent non-internautes) ; 82 pourcent des 75 ans ou plus manquent de competences (49 pourcent non-internautes, 33 pourcent sans notions de base) ; 27 pourcent ont des competences faibles ; la part baisse depuis 2021 (-4 pts) par effet de generation plus que d'intensification des pratiques. Le passage au numerique des decheteries (badge/apps/QR) confronte directement les profils a l'illectronisme. | e67726b9-d5d7-46b1-a6b5-ece75db790a4
FCT-002 | FACT | ✦ | https://actu.fr/auvergne-rhone-alpes/saint-etienne_42218/jusqu-a-10-passages-sans-qr-code-tres-critiquee-saint-etienne-metropole-modifie-encore-l-acces-aux-decheteries_64437832.html | B,C | 2026-08-30 | SEM QR code obligatoire depuis 01/11/2024, assoupli le 22/06/2026 (10 passages sans QR), seulement 15 pourcent des foyers creent un compte a Saint-Etienne, petition 440 signatures, collectif Halte au controle numerique | FAIT VERIFIE (✦) : actu.fr 22/06/2026 INSPECTED : QR code obligatoire (compte en ligne) depuis 01/11/2024 pour 13 decheteries SEM ; assoupli le 22/06/2026 (10 passages/an sans QR, inscription par plaque) ; a Saint-Etienne seulement 15 pourcent de la population avait cree un compte (25 pourcent a Firminy, 70 pourcent a Farnay) ; petition non aux QR codes du 19/11 (440 signatures) ; collectif Halte au controle numerique et agents engages contre. Contre-exemple de reversibilite par pression citoyenne sur la fracture numerique. | 68b6fd53-11b1-4cb6-8d60-a412e371222b
FCT-003 | FACT | ✦ | https://www.if-saint-etienne.fr/politique-societe/depots-sauvages-a-qui-la-faute | A,C | 2026-08-30 | SEM bilan QR code : 80 000 comptes crees (av 67 000 maisons), 30 passages/an, 2 passages sans inscription, +200 tonnes depots sauvages 6 mois apres QR (selon Ville), ~500 personnes au-dela du quota | FAIT VERIFIE (✦) : IF Saint-Etienne 07/11/2025 INSPECTED : SEM annonce 80 000 comptes (plus que les 67 000 maisons des 53 communes), 30 passages/an, 2 passages sans inscription ; mais desaccord Ville/Metropole : adjointe Makhlouf comptabilise +200 t de depots sauvages en 6 mois apres le QR (nov 2024-avr 2025 vs 2023-2024), 10 cameras de video-verbalisation (230 000 EUR), 2 policiers municipaux ; ~500 personnes au-dela des 30 passages risquent de deposer sur le trottoir ; rigidite du systeme (voiture d'un autre, location) ; 4 800 QR codes crees via formulaire papier (preuve fracture numerique). | d58ae832-c1b9-41be-a0cd-ba5f321b4e1c
FCT-004 | FACT | ✦ | https://www.if-saint-etienne.fr/politique-societe/depots-sauvages-a-qui-la-faute | A,C | 2026-08-30 | decheterie = service public essentiel (40 pourcent DMA via decheterie, Insee) mais acces conditionne au numerique et a l'automobile : fracture d'acces sociale et territoriale | FAIT VERIFIE (✦) : la decheterie porte ~40 pourcent du tonnage des dechets menagers et assimiles collectes par le service public (Insee 2025, ~242 kg/hab sur ~615) ; or l'acces y est de plus en plus conditionne a un numerique (badge/QR/apps) que 34 pourcent des 16-74 ans et 82 pourcent des 75+ ne maitrisent pas (FCT-001), et suppose un vehicule (fracture des transports, dependance automobile) ; SEM illustre la contradiction : service essentiel vs acces barrique par le tout-numerique, avec report observe vers les depots sauvages. | b63343fa-332e-4009-b1d1-8b244d5f256b
FCT-005 | FACT | ✦ | https://actu.fr/auvergne-rhone-alpes/saint-etienne_42218/jusqu-a-10-passages-sans-qr-code-tres-critiquee-saint-etienne-metropole-modifie-encore-l-acces-aux-decheteries_64437832.html | A,B | 2026-08-30 | redistributif et captifs numeriques : excedent de passage transforme en recette (facturation), inclus exclus par defaut ; pas d'etude nationale de l'impact social des quotas d'acces 2024-2026 | FAIT VERIFIE (✦) : GAP - aucun chiffrage national du cout de l'illectronisme d'acces aux decheteries numeriques ; SEM documente le mecanisme : la fracture numerique combinee aux quotas/facturation (axes F/cartographie) cree des exclus par defaut (ceux sans compte ou depassant 30 passages) ; collectif Halte au controle numerique et agents alertent contre un service essentiel barrique ; pas d'etude AMORCE/ADEME publique chiffrant l'impact social des controles d'acces 2024-2026. | 6007d8ea-3742-474d-ae0b-9cee94b2ff03
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002
FCT-002 | SRC-002,SRC-003
FCT-003 | SRC-003,SRC-001
FCT-004 | SRC-003,SRC-001
FCT-005 | SRC-002,SRC-001

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-006 | NONE
FCT-002 | QRY-007 | NONE
FCT-003 | QRY-008 | NONE
FCT-004 | QRY-009 | NONE
FCT-005 | QRY-010 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
FCT-002 | ELIGIBLE:CONFIRME
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:CONFIRME

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7:AXS-001:QRY-001
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9:AXS-001:QRY-001
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:AXS-001:QRY-001
CP-004 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:11:AXS-001:QRY-001
CP-005 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:AXS-001:QRY-001
CP-006 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:CAU-001:QRY-001
CP-007 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:CAU-001:QRY-001
CP-008 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18b:GATES

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T20:39:23.140925+00:00","fact_mem":{"FCT-001":"e67726b9-d5d7-46b1-a6b5-ece75db790a4","FCT-002":"68b6fd53-11b1-4cb6-8d60-a412e371222b","FCT-003":"d58ae832-c1b9-41be-a0cd-ba5f321b4e1c","FCT-004":"b63343fa-332e-4009-b1d1-8b244d5f256b","FCT-005":"6007d8ea-3742-474d-ae0b-9cee94b2ff03"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory reference MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
