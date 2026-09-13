ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-0800-enquete-complementaire-decheteries | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_enquete-complementaire-decheteries/2026-08-31_08-00_enquete-complementaire-decheteries_INPUT.txt | SUBJECT_SLUG:enquete-complementaire-decheteries | SUBJECT_FP:sha256:c4abddf7bf387030505d98c9af183f033005ec8f65b8782349abd3dc3894b747 | INPUT_SHA256:sha256:c4abddf7bf387030505d98c9af183f033005ec8f65b8782349abd3dc3894b747
COMPLEXITY:6→MEDIUM | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'lead_question': 'Do professional decheteries exist at scale (cost, coverage) as the alternative for excluded pros; does the decheterie network meet its environmental purpose (valorisation, refus de tri); what happens to reusable objects; has CNIL ever enforced badge/LAPI rules?'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Ce que l'enquête établit

### Lièvre 1 — L'alternative des exclus : un réseau pro mince et payant (FCT-001, FCT-002, FCT-006)

L'axe A (exclusion des pros) avait sa moitié manquante : où vont les professionnels exclus ? Réponse documentée :

- **Le réseau professionnel est mince** : environ **200 déchèteries professionnelles** en France contre **4 500+** déchèteries ménagères (estimation Gurdebeke, opérateur — chiffre d'une partie intéressante, à présenter comme estimation) ;
- **L'accès pro public est facturé à la tonne** : Caen la mer (27/07/2026) facture les encombrants **298,20 €/t**, le bois **134,21 €/t**, les déchets verts **71,80 €/t** ;
- **Le privé agrège l'offre** : Ecodrop (IDF, 45 sites partenaires) facture le DIB mélangé **188 €/t**, gravats **34 €/t**, déchets verts **65 €/t**, cartons gratuits — accès par code de paiement unique, réservé aux pros.

**Impact sur l'article** : l'exclusion (AMP 01/07/2025) ne supprime pas une charge, elle la facture. Un artisan paie désormais 34-298 €/t ce qui était gratuit — l'écart avec l'accès ménager gratuit financé par la TEOM quantifie l'incitation au dépôt sauvage. **GAP nommé (COVERAGE_DATA_ABSENT)** : aucun recensement officiel du réseau pro ni de coût moyen par artisan.

### Lièvre 2 — La promesse de 1980 n'est tenue qu'aux trois quarts (FCT-004)

La donnée officielle (SDES/Insee/ADEME via notre-environnement.gouv.fr, 05/12/2025) dresse le bilan environnemental du réseau : les déchèteries reçoivent **40 % des déchets ménagers et assimilés** (242 kg/hab en 2021), et de ce qui y est déposé : **43 % recyclé, 25 % composté/méthanisé, 25 % stocké sans valorisation, 6 % énergie**.

**Un quart de ce qui entre en déchèterie est enfoui.** C'est le contre-récit que l'article doit porter : le réseau a résolu le problème des décharges sauvages de 1980, mais son rendement matière reste incomplet. **GAP nommé (SITE_LEVEL_DATA_ABSENT)** : pas de série de refus de tri par site ; le split est national.

### Lièvre 3 — Le réemploi : obligatoire, réel, non mesuré (FCT-005)

La loi AGEC rend les **zones réservantes** obligatoires en déchèterie ; les partenariats avec ressourceries et boutiques ESS (Nouvelle Fabrique, 29/01/2026) détournent « des milliers d'objets par an » des bennes. Mais l'échelle nationale du réemploi en déchèterie **n'est pas mesurée** — les « 350 t d'objets en bon état détruits/an » restent une estimation OPEN. L'article présente le réemploi comme le potentiel le plus sous-exploité du dispositif.

### Lièvre 4 — La CNIL fait respecter, mais pas encore sur les déchèteries (FCT-003)

L'enforcement CNIL est réel : le 25/08/2020, **quatre communes ont été mises en demeure** pour verbalisation LAPI illégale, et les communes restent interdites d'usage LAPI judiciaire. Mais **aucune sanction trouvée** visant spécifiquement un traitement badge/LAPI de déchèterie. La frappe RGPD de l'article s'appuie donc sur la doctrine (durées), pas sur un précédent de sanction — formulation à respecter.

## Ce que l'article doit faire de ces résultats

1. **Boucler l'axe A** : exclusion → alternative mince (~200 sites, estimation) et payante (34-298 €/t) → incitation chiffrée au dépôt sauvage.
2. **Ajouter le contre-récit environnemental** : 25 % d'enfouissement — le réseau ne tient qu'incomplètement sa promesse de 1980.
3. **Traiter le réemploi comme potentiel sous-exploité**, pas comme acquis.
4. **Ancrer la frappe RGPD sur la doctrine**, en nommant l'absence de sanction déchèterie spécifique.

## Ce qui reste ouvert

- Recensement officiel du réseau pro (ADEME/SINOE) — inexistant publiquement.
- Série de refus de tri par site — vivrait dans les RPQS, non agrégée.
- Échelle nationale du réemploi — à la charge d'un futur travail ADEME.
- Les quatre publications attendues (PMCB, ADEME, PPL, fonds ≤10 m³) — inchangées depuis la passe frappes-juridiques du même jour.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:0|CLM:4|AXS:4|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"The alternative for excluded professionals is thin (~200 pro sites) and priced per tonne","counter":"NONE_FOUND","gap":"No national census of pro decheterie capacity or average artisan cost","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-006"]}
CLM-002 | {"claim":"Decheteries meet their environmental purpose only partially: 25% of intake is landfilled without valorisation","counter":"NONE_FOUND","gap":"No per-site refus-de-tri series; national split only","gap_type":"SITE_LEVEL_DATA_ABSENT","status":"SUPPORTED","support":["FCT-004"]}
CLM-003 | {"claim":"Reuse zones are mandatory (AGEC) but reuse scale is not nationally measured","counter":"NONE_FOUND","gap":"The 350t/yr destroyed-objects figure remains an OPEN estimate","gap_type":"REUSE_SCALE_UNMEASURED","status":"SUPPORTED","support":["FCT-005"]}
CLM-004 | {"claim":"CNIL enforcement of access-control data rules is real but has never targeted decheterie badge/LAPI processing","counter":"NONE_FOUND","gap":"Enforcement search bounded to public CNIL communications","gap_type":"ENFORCEMENT_HISTORY_NARROW","status":"SUPPORTED","support":["FCT-003"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"Do professional decheteries exist at scale in France: how many, what do they cost artisans (per visit/subscription), what coverage?","routes":["EVIDENCE_CASES"],"sought_objects":["decheteries professionnelles reseau","tarifs artisans dechets","coverage maps"],"status":"SATURATED"}
AXS-002 | {"question":"Does the decheterie network meet its environmental purpose: diversion/valorisation rates, sorting rejects (refus de tri) at decheteries?","routes":["EVIDENCE_CASES"],"sought_objects":["ADEME valorisation decheteries","refus de tri taux","performance tri"],"status":"SATURATED"}
AXS-003 | {"question":"What happens to reusable objects dropped at decheteries: reuse platforms, the 350t/year destroyed estimate?","routes":["EVIDENCE_CASES"],"sought_objects":["ressourceries decheteries","reemploi encombrants","plateformes reemploi"],"status":"SATURATED"}
AXS-004 | {"question":"Has CNIL ever enforced (mises en demeure/sanctions) badge or LAPI access-control processing at collectivites?","routes":["RULES_CONTROLS"],"sought_objects":["CNIL mises en demeure LAPI","CNIL sanctions badges collectivites","decheterie RGPD sanction"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Only ~200 professional decheteries exist vs 4,500+ household sites; public pro access is per-tonne priced","effect":"Excluded professionals face a thin, paid alternative network","mechanism":"Exclusion (AMP 2025) pushes pros to Ecodrop-style paid depots (DIB 188 EUR/t) or public pro tariffs (Caen bulky 298 EUR/t); the cost gap vs free household access creates the wild-dumping incentive","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-006"]}
CAU-002 | {"cause":"Mixed/contaminated flows and absent sorting capacity at small sites","effect":"A quarter of decheterie intake is landfilled without valorisation","mechanism":"Official SDES/Insee/Ademe destination split: 43% recycled, 25% composted, 25% landfilled, 6% energy","status":"SUPPORTED","support":["FCT-004"]}
CAU-003 | {"cause":"AGEC-mandated zones reservantes depend on local ressourcerie partnerships","effect":"Reuse captures only a fraction of deposited objects","mechanism":"Mandatory reuse zones route objects to ESS shops; scale not nationally measured","status":"SUPPORTED","support":["FCT-005"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:14|FETCH:8|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | - | warm-route-none | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | OK | - | - | decheterie professionnelle nombre France reseau tarifs artisans
QRY-002 | FETCH | INSPECTED | SRC-001 | https://gurdebeke.com/les-dechetteries-professionnelles/ | Gurdebeke dechetteries professionnelles 200 vs 4500
QRY-003 | FETCH | INSPECTED | SRC-002 | https://www.ecodrop.net/depot-2-2/ | Ecodrop depot dechetterie pro tarifs DIB gravats
QRY-004 | WEB | OK | - | - | RecyclInn Pro Veolia decheteries professionnelles reseau nombre sites
QRY-005 | FETCH | INSPECTED | SRC-003 | https://www.recyclage.veolia.fr/gerer-mes-dechets/entreprises/solutions-services/recyclinn-pro-decheteries-professionnelles | Veolia RecyclInn Pro reseau decheteries professionnelles
QRY-006 | FETCH | INSPECTED | SRC-004 | https://caenlamer.fr/conditions-acces-decheterie-professionnels | Caen la mer tarifs professionnels decheterie
QRY-007 | WEB | OK | - | - | taux valorisation decheterie recyclage compostage stockage
QRY-008 | FETCH | INSPECTED | SRC-005 | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement | notre-environnement.gouv.fr dechets menagers chiffres destins dechetterie
QRY-009 | WEB | OK | - | - | taux refus tri centres de tri 30 pourcent Insee
QRY-010 | WEB | OK | - | - | reemploi decheterie ressourcerie encombrants detruits tonnage
QRY-011 | FETCH | INSPECTED | SRC-006 | https://www.nouvelle-fabrique.org/actualites/decheterie/ | Nouvelle Fabrique zones reservantes reemploi decheterie AGEC
QRY-012 | FETCH | INSPECTED | SRC-007 | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement | notre-environnement dechets menagers chiffres dechetterie 40 pourcent
QRY-013 | WEB | OK | - | - | Insee taux refus centres de tri 30 pourcent 2021
QRY-014 | WEB | OK | - | - | CNIL mises en demeure LAPI communes verbalisation 2020
QRY-015 | FETCH | INSPECTED | SRC-008 | https://www.cnil.fr/fr/verbalisation-par-lecture-automatisee-des-plaques-dimmatriculation-lapi-la-cnil-met-en-garde | CNIL mise en garde verbalisation LAPI communes mises en demeure
QRY-016 | WEB | PARTIAL | - | - | CNIL sanction decheterie badge controle acces collectivite
QRY-017 | WEB | OK | - | - | REFUTATION Professional decheterie network scarcity: decheteries professionnelles nombre autre chiffre 300 500 reseau national
QRY-018 | WEB | OK | - | - | REFUTATION Ecodrop pro depot pricing: tarifs dechetterie pro autre chiffre gratuit subventionne artisans
QRY-019 | WEB | OK | - | - | REFUTATION Caen la mer professional decheterie tariffs: tarifs professionnels autre chiffre 2025 reduction
QRY-020 | WEB | OK | - | - | REFUTATION Decheterie environmental outcomes: dechetterie valorisation autre chiffre 60 pourcent stockage
QRY-021 | WEB | OK | - | - | REFUTATION Decheterie reuse zones: zones reservantes obligatoire AGEC autre date decret application
QRY-022 | WEB | OK | - | - | REFUTATION CNIL LAPI enforcement history: sanction LAPI decheterie controle acces 2024 2025 2026

## EVIDENCE_REGISTRY
SRC-001 | ◉ | fam:B | https://gurdebeke.com/les-dechetteries-professionnelles/
SRC-002 | ◉ | fam:B | https://www.ecodrop.net/depot-2-2/
SRC-003 | ◉ | fam:B | https://www.recyclage.veolia.fr/gerer-mes-dechets/entreprises/solutions-services/recyclinn-pro-decheteries-professionnelles
SRC-004 | ◈ | fam:A | https://caenlamer.fr/conditions-acces-decheterie-professionnels
SRC-005 | ◈ | fam:A | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement
SRC-006 | ◉ | fam:C | https://www.nouvelle-fabrique.org/actualites/decheterie/
SRC-007 | ◈ | fam:A | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement
SRC-008 | ◈ | fam:A | https://www.cnil.fr/fr/verbalisation-par-lecture-automatisee-des-plaques-dimmatriculation-lapi-la-cnil-met-en-garde

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://gurdebeke.com/les-dechetteries-professionnelles/ | B | 2026-08-31 | Professional decheterie network scarcity | Professional decheteries are scarce in France: roughly 200 sites vs 4,500+ household decheteries (Gurdebeke operator estimate, 2026). Coverage gaps force excluded pros to either pay private operators or travel far. | ae84b9b0-47bd-49ea-b2b1-6b9252a8e6aa
FCT-002 | FACT | ✧ | https://www.ecodrop.net/depot-2-2/ | B | 2026-08-31 | Ecodrop pro depot pricing | Ecodrop (IDF, 45 partner pro decheteries, founded 2017): DIB mixed 188 EUR/t, rubble 34 EUR/t, green waste 65 EUR/t, paper/cardboard free; per-visit paid deposits with unique payment codes; explicitly reserved to professionals — the priced alternative excluded pros are pushed toward. | fe73e8eb-463d-45af-8815-e2e74dc0a6d5
FCT-003 | FACT | ✧ | https://www.cnil.fr/fr/verbalisation-par-lecture-automatisee-des-plaques-dimmatriculation-lapi-la-cnil-met-en-garde | A | 2020-08-25 | CNIL LAPI enforcement history | CNIL enforcement is real but dated and narrow: 25/08/2020 four communes were formally put on notice (mises en demeure) for illegal LAPI verbalisation; communes remain barred from judicial-police LAPI use. No CNIL sanction found to date targeting decheterie badge/access-control processing specifically. | 4b4758f4-0092-4039-94b3-04f4664748e2
FCT-004 | FACT | ✧ | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement | A | 2025-12-05 | Decheterie environmental outcomes | Official SDES/Insee/Ademe data (notre-environnement.gouv.fr, 05/12/2025): decheteries receive 40% of household+assimilated waste (242 kg/hab 2021); of what is deposited: 43% recycled, 25% composted/methanised, 25% landfilled WITHOUT valorisation, 6% energy. A quarter of decheterie intake is buried. | 1c4a7c59-e749-416d-a9b6-77265b389a68
FCT-005 | FACT | ✧ | https://www.nouvelle-fabrique.org/actualites/decheterie/ | C | 2026-01-29 | Decheterie reuse zones | Nouvelle Fabrique (29/01/2026): AGEC law made 'zones reservantes' (reuse areas) mandatory in public decheteries; partnership networks route reusable objects to ressourceries/ESS shops; 'thousands of objects per year' diverted from bins at their sites — reuse exists but scale is not nationally measured. | 93368350-24b0-499c-abfd-1c7ad2eed151
FCT-006 | FACT | ✧ | https://caenlamer.fr/conditions-acces-decheterie-professionnels | A | 2026-07-27 | Caen la mer professional decheterie tariffs | Caen la mer public decheterie pro tariffs (27/07/2026): bulky 298.20 EUR/t, green waste 71.8 EUR/t, wood 134.21 EUR/t — a public network charging pros per-tonne rates far above the household-free baseline. | a3c7c07f-1adc-4aac-b9e7-4f48a29b5f96
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-008
FCT-004 | SRC-005,SRC-007
FCT-005 | SRC-006
FCT-006 | SRC-004

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-017 | NONE
FCT-002 | QRY-018 | NONE
FCT-003 | QRY-022 | NONE
FCT-004 | QRY-020 | NONE
FCT-005 | QRY-021 | NONE
FCT-006 | QRY-019 | NONE

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
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-31T06:16:31.964623+00:00","fact_mem":{"FCT-001":"ae84b9b0-47bd-49ea-b2b1-6b9252a8e6aa","FCT-002":"fe73e8eb-463d-45af-8815-e2e74dc0a6d5","FCT-003":"4b4758f4-0092-4039-94b3-04f4664748e2","FCT-004":"1c4a7c59-e749-416d-a9b6-77265b389a68","FCT-005":"93368350-24b0-499c-abfd-1c7ad2eed151","FCT-006":"a3c7c07f-1adc-4aac-b9e7-4f48a29b5f96"},"mnemo_row":"WROTE:pending","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}

PERSISTENCE_META: MNEMO_ROW:WROTE:pending | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:6;attempted:6;success:6;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[6 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
