ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-0927-audit-collecte-dechets-france | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:NEW | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_audit-collecte-dechets-france/2026-08-31_09-27_audit-collecte-dechets-france_INPUT.txt | SUBJECT_SLUG:audit-collecte-dechets-france | SUBJECT_FP:sha256:32421339d3c6b6fb41fe1407fd2d4438bc15df269b8ba7ac657ac28cf8715bdb | INPUT_SHA256:sha256:390d8b01072e8a5fc97f17163e1e3e6023639f7eed5730c10ff64dc566c0cd04
COMPLEXITY:0.6→MEDIUM | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['collectivites', 'EPCI', 'syndicats', 'ADEME', 'SDES', 'Insee', 'Senat', 'menages'], 'domains': ['dechets', 'collecte', 'tarification', 'territoires'], 'geo': 'France metro + Reunion', 'lead_question': 'Pourquoi la collecte des dechets menagers est-elle si heterogene ? Determinants: organisation, financement, infrastructures.', 'limits': 'pas de carte nationale des modes', 'object_question': '(1) modes de collecte par EPCI ; (2) tarification ; (3) performance et couts.'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Ce que l'enquête établit

### Axe 1 — Le « bordel » est structurel, pas accidentel (FCT-001, FCT-003, FCT-006)

La collecte des déchets ménagers est organisée par **1 169 structures compétentes** en 2023 (ADEME, enquête 2025, citée par le rapport Sénat l25-049 du 21/10/2025) : EPCI, syndicats mixtes, et 6 communes en propre (Paris et les îles mono-communales Sein, Ouessant, Bréhat, Yeu). Le nombre a été **divisé par deux entre 2007 et 2023** (mutualisation) mais se stabilise depuis 2017.

La source profonde du « bordel » perçu est **juridique** : l'article L. 2224-13 CGCT laisse chaque collectivité organiser la collecte comme elle l'entend, dans un cadre minimal (collecte hebdomadaire en porte-à-porte en zone > 2 000 habitants, 4 filières de collecte séparée obligatoires : papier/verre/métal/plastique, déchets de construction, textile/dangereux, biodéchets). Pire : le **financement mixte TEOM + REOM sur un même territoire** est légal « pour des raisons historiques » (fusions de communes, syndicats) — FCT-003. Un même EPCI peut donc facturer une partie de ses habitants à la taxe foncière et l'autre à la redevance. C'est la fragmentation institutionnelle qui produit l'expérience utilisateur « chaque ville a son système ».

### Axe 2 — La TEOM domine, la tarification incitative reste marginale (FCT-002, FCT-004, FCT-008, FCT-009)

Le financement dominant est la **TEOM classique** : ~63 % des structures, **72 % de la population (48,8 millions d'habitants)** — un impôt assis sur la valeur locative, **découplé de la quantité de déchets produite** (FCT-002). La décomposition : TEOM+RS 33,3 %, TEOM 21,3 %, REOM incitative 14,0 %, REOM 9,6 %, mixte 7,4 %.

La **tarification incitative (TI)** est documentée comme efficace mais marginale : au 1/1/2021, 200 collectivités couvraient 6,6 M d'habitants (176 en REOMi, 24 en TEOMi) — FCT-008 ; en 2026, **7,2 M de Français** sont couverts, très loin de l'objectif LTECV de **25 M** (FCT-004). Les effets mesurés (SINOE) : **OMR -31 %** (-34 % en REOMi, -16 % en TEOMi), emballages +17 %, verre +10 %, apports en déchèterie +13 % (FCT-009). Le passage demande ≥ 3 ans (4 ans en TEOMi), des bacs à puces, un fichier des producteurs — une logistique qui explique la lenteur (FCT-010).

**Réfutation populaire traitée** : la TI est accusée de créer des dépôts sauvages ; l'étude ADEME/ECOGEOS/ALTAIR (2024, 28 collectivités dont 18 en TI et 10 témoins) montre qu'**elle ne systématise pas leur émergence**, et les OMR ne sont qu'une part infime des dépôts sauvages face aux déchets professionnels (FCT-005, FCT-011). Le rapport Sénat reprend cette nuance.

### Axe 3 — La performance : 615 kg/hab, trois circuits, 21,6 Md€ (FCT-012, FCT-013, FCT-014, FCT-015)

Insee Première 2055 (données 2021) : **41 Mt de DMA, 615 kg/hab** (+4 % en 10 ans), l'objectif LTECV de -10 % en 2020 **n'est pas atteint**. Les OMR reculent (-14 % à 245 kg/hab) mais les déchets triés progressent (+21 %). Trois circuits co-égaux : **OMR ~40 % du tonnage (porte-à-porte), collecte séparée ~20 %, déchèteries 40 %** (99 % des gravats, 88 % des encombrants passent par la déchèterie) — FCT-013. Le parc de traitement (2022) : ~1 800 installations dont 710 tri, 670 compostage, 120 incinération avec valorisation énergétique, 170 stockage (FCT-014).

Le coût total : **21,6 Md€ en 2022** pour la gestion des déchets (SDES, +8,5 % vs 2021) — FCT-015. C'est la facture agrégée derrière la perception « on paie plus pour un service compliqué ».

## Ce que l'article doit faire de ces résultats

1. **Expliquer la fragmentation par sa cause juridique** (L. 2224-13 + financement mixte « historique »), pas par l'incompétence des agents : le « bordel » est un choix d'organisation décentralisé, pas un accident.
2. **Quantifier le paradoxe de la TEOM** : 72 % des Français paient un impôt déconnecté de ce qu'ils jettent, alors que la TI (prouvée à -31 % OMR) couvre à peine 7,2 M d'habitants.
3. **Boucler avec la fresque déchèteries** : la déchèterie porte 40 % des DMA — le contrôle d'accès et l'exclusion des pros (passe 2015/2026) agissent sur un flux de premier ordre.
4. **Traiter la rumeur « la TI crée des dépôts sauvages »** avec la donnée ADEME, sans la retourner en argument pro-TI aveugle (les OMR sont minoritaires dans les dépôts sauvages ; ce sont les pros qui dominent).

## Ce qui reste ouvert

- **Pas de carte nationale des modes de collecte par EPCI** publiée (GAP nommé, COVERAGE_DATA_ABSENT) — vivrait dans les RPQS, non agrégée.
- **Pas de série nationale des taux TEOM/REOM par EPCI** ni des grilles TI (GAP nommé).
- Le coût des containers enterrés (achat 4 000-8 000 €, entretien 200-400 €/an — sources professionnelles PlaceDuPro/Hellopro, famille B non retenue faute de source officielle) reste un angle à confirmer par une source T2.
- L'inégalité territoriale de la TI (Bretagne ~30 % vs Île-de-France <1 %) est documentée par les ORD mais la consolidation nationale ADEME reste partielle.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:0|CLM:4|AXS:3|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"The perceived collection bordel is structural: 1,169 competent structures, legally permitted mixed financing (TEOM+REOM on one territory for historic reasons), modalities left to each collectivite within a minimal weekly PAP + 4-stream frame","counter":"The fragmentation has been halved since 2007 (mutualisation) and stabilised since 2017","gap":"No national per-EPCI collection-mode map published","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-006"]}
CLM-002 | {"claim":"TEOM classic (not based on waste produced) remains the dominant financing mode: ~63% of structures, 72% of the population (48.8M inhabitants) - the majority pays a tax decoupled from what they throw away","counter":"REOM-I is growing (+44% since 2016)","gap":"No consolidated per-EPCI TEOM rate map","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-002","FCT-004","FCT-008"]}
CLM-003 | {"claim":"Incentive pricing is documented as effective (OMR -31%, packaging +17%) but marginal: 7.2M inhabitants vs the 25M LTECV target; ADEME shows TI does not systematise wild dumping","counter":"TI blamed for wild dumps in public debate; 3+ years lead time and logistics slow roll-out","gap":"No national per-EPCI TI tariff/impact series","gap_type":"COVERAGE_DATA_ABSENT","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-008","FCT-009","FCT-010","FCT-011"]}
CLM-004 | {"claim":"Collection runs on three co-equal circuits: residual waste ~40% of tonnage (door-to-door), separate collection ~20%, decheteries 40% (99% of rubble, 88% of bulky) - the user faces different bins, schedules, drop points and prices depending on where they live","counter":"None found in consulted sources","gap":"No national collection-mode harmonisation indicator","gap_type":"SITE_LEVEL_DATA_ABSENT","status":"SUPPORTED","support":["FCT-013"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"How fragmented is the collection system: how many competent structures, what coexistence of financing/modes, what does that mean for the user?","routes":["AUDIT","EXPAND"],"sought_objects":["structures competentes dechets nombre","financement mixte TEOM REOM","modes de collecte par EPCI"],"status":"SATURATED"}
AXS-002 | {"question":"Who pays what: TEOM vs REOM vs incentive pricing, how many inhabitants covered, what are the territorial inequalities?","routes":["AUDIT","EXPAND"],"sought_objects":["TEOM REOM part population","tarification incitative habitants","inégalités territoriales TI"],"status":"SATURATED"}
AXS-003 | {"question":"What is the performance and cost ledger: 615kg/hab, three circuits, treatment installations, 21.6 Md EUR spending?","routes":["AUDIT","EXPAND"],"sought_objects":["DMA kg habitant circuits","installations traitement France","dépense gestion dechets SDES"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Legally permitted organisational freedom (L2224-13: communes/EPCI/syndicats can each organise collection), historic mixed financing, 1,169 structures","effect":"Heterogeneous collection systems: different bins, frequencies, financing across neighbouring territories - the perceived bordel","mechanism":"Each structure decides modalities within a minimal frame (weekly PAP >2000 hab, 4 separate streams); financement mixte only legal for historic reasons (fusions, syndicats)","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-006","FCT-013"]}
CAU-002 | {"cause":"TEOM classic is assessed on property rental value, not on waste produced (72% of population)","effect":"No price signal on quantities thrown away; DMA at 615 kg/hab and LTECV -10% 2020 target missed","mechanism":"TEOM decouples payment from usage; TI (REOMi/TEOMi) restores the signal and cuts OMR -31%","status":"SUPPORTED","support":["FCT-002","FCT-009","FCT-012"]}
CAU-003 | {"cause":"Decheteries collect 40% of DMA tonnage (99% rubble, 88% bulky) - co-equal with residual collection","effect":"Any access-control or exclusion policy at decheteries directly moves a major share of household waste flows","mechanism":"The 40% share (Insee/ADEME 2021) makes decheterie access policy a waste-policy lever of the first order, connecting this investigation to the decheteries dossier","status":"SUPPORTED","support":["FCT-013"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:7|FETCH:5|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | runtime | warm-route-none | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | OK | - | - | France collecte déchets ménagers modes différents par commune bacs jaunes gris containers enterrés points apport volontaire ADEME enquête
QRY-002 | WEB | OK | - | - | TEOM REOM REOMI tarification incitative déchets ménagers France part des collectivités 2024 2025
QRY-003 | WEB | OK | - | - | enquête ADEME collecte déchets service public 2022 modes de collecte porte-à-porte apport volontaire pourcentage EPCI
QRY-004 | WEB | OK | - | - | containers enterrés déchets coût installation maintenance collectivités France problèmes tri qualité
QRY-005 | FETCH | INSPECTED | SRC-001 | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement | SDES dechets menagers chiffres collecte
QRY-006 | FETCH | INSPECTED | SRC-002 | https://www.insee.fr/fr/statistiques/8574484 | Insee Premiere 2055 dechets menagers 2021
QRY-007 | WEB | OK | - | - | AMORCE observatoire tarification incitative 2024 nombre collectivités habitants France TEOMI REOMI part
QRY-008 | FETCH | INSPECTED | SRC-003 | https://economie-circulaire.ademe.fr/tarification-incitative | ADEME tarification incitative bilan 2021 collectivites
QRY-009 | WEB | OK | - | - | conteneurs enterrés déchets coût installation 8000 euros collectivité entretien avantages inconvénients France nombre
QRY-010 | FETCH | PARTIAL | - | https://rare.fr/les-actualites-du-rare/quel-est-la-part-des-populations-soumise-a-la-tarification-incitative-les-observatoires-regionaux-dechets-et-economie-circulaire-vous-repondent/ | RARE part populations tarification incitative regions
QRY-011 | WEB | OK | - | - | enquête ADEME 2023 collecte déchets porte-à-porte apport volontaire part des EPCI emballages verre OMR France
QRY-012 | FETCH | INSPECTED | SRC-004 | https://www.senat.fr/rap/l25-049/l25-0491.html | PPL qualite services gestion dechets Senat rapport Paccaud 2025

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement
SRC-002 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8574484
SRC-003 | ◈ | fam:A | https://economie-circulaire.ademe.fr/tarification-incitative
SRC-004 | ◈ | fam:A | https://www.senat.fr/rap/l25-049/l25-0491.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.senat.fr/rap/l25-049/l25-0491.html | A | 2025-10-21 | Nombre de structures competentes collecte/traitement | In 2023, 1,169 structures held the waste collection/treatment competence (ADEME 2025 survey, cited by Senate PPL l25-049 report): 6 communes in own hands (Paris + mono-communal islands Sein, Ouessant, Brehat, Yeu). Count nearly halved between 2007 and 2023 (mutualisation), stabilising since 2017. | 83112980-8d6e-41ef-98b8-800bbfc5adc9
FCT-002 | FACT | ✧ | https://www.senat.fr/rap/l25-049/l25-0491.html | A | 2025-10-21 | TEOM classique premier mode de financement | Classic TEOM remains the leading financing mode: ~63% of the 1,169 structures, serving 72% of French population (48.8M inhabitants). Breakdown of modes: TEOM+RS 33.3%, TEOM 21.3%, REOM-I 14.0%, REOM 9.6%, mixed financing 7.4%, budget general 0.9%, others minor. | db37fb3b-f9f1-4f0d-8e1c-8a46fd67c73b
FCT-003 | FACT | ✧ | https://www.senat.fr/rap/l25-049/l25-0491.html | A | 2025-10-21 | Financement mixte TEOM+REOM meme territoire | Mixed financing (part of the EPCI territory in TEOM, another in REOM, sometimes with special levy) is legally possible ONLY for 'historic' reasons: commune fusions or syndicates gathering EPCI members in different regimes. Same territory can therefore host different financing and collection rules - a structural source of perceived 'bordel'. | 178ce2a7-666b-4173-960e-7a7b041310b9
FCT-004 | FACT | ✧ | https://www.senat.fr/rap/l25-049/l25-0491.html | A | 2025-10-21 | Tarification incitative 7,2M habitants vs objectif 25M | Only 7.2M French inhabitants are covered by incentive pricing (TI) today, far from the 25M target set by LTECV; coverage grew +44% since 2016 but generalisation faces individualisation issues in urban/tourist areas, heavy investment and admin cost, variable revenue. ADEME estimates TI cuts residual household waste (OMR) by 30%. | 51d65a22-d126-4095-b206-0129e5a0bdb8
FCT-005 | FACT | ✧ | https://www.senat.fr/rap/l25-049/l25-0491.html | A | 2025-10-21 | TI et depots sauvages | TI is popularly blamed for wild dumping, but ADEME finds 'the incentive tax does not systematise the emergence of wild dumps' where good practices exist; household waste is a tiny share of wild dumps vs professional waste. The Senate finance committee repeated this caveat (2025). | c247eb92-b789-4f0d-b28c-b3f161dc49f9
FCT-006 | FACT | ✧ | https://www.senat.fr/rap/l25-049/l25-0491.html | A | 2025-10-21 | Obligations de collecte PAP hebdo + 4 filieres separees | Regulation mandates at minimum weekly door-to-door collection in agglomerated zones above 2,000 permanent inhabitants, and 4 mandatory separate collection streams: (1) paper/glass/metal/plastic, (2) mineral/wood/plaster construction waste, (3) textile and hazardous waste, (4) biowaste. All modalities left to each collectivite within this frame. | eb244cef-7bd7-48d3-b7f7-15afdcfecc45
FCT-007 | FACT | ✧ | https://www.senat.fr/rap/l25-049/l25-0491.html | A | 2025-10-21 | PPL modulation sociale REOM/TEOMi rejetee commission | Senate finance committee (rapporteur Olivier Paccaud, 21/10/2025) did NOT adopt article 1 of the PPL 'garantir la qualite des services de gestion des dechets': a proposed social modulation of REOM/TEOMi by income, household composition or health. The PPL itself signals the fragmentation/quality concern is on the legislative agenda. | 2a3748c0-69a2-4eef-b5ee-5ba0c41a7cd5
FCT-008 | FACT | ✧ | https://economie-circulaire.ademe.fr/tarification-incitative | A | 2024-01-01 | TI 1er janvier 2021 200 collectivites | ADEME (Bilan des collectivites en TI au 1er janvier 2021, rapport 2024): 200 collectivites had successfully set up incentive pricing covering 6.6M inhabitants - 176 with incentive levy (REOMi), 24 with incentive tax (TEOMi). Majority rural or 'mixed rural-dominant' typology; developing in denser and tourist areas. | 4382306f-8ef6-4393-a252-67034703024b
FCT-009 | FACT | ✧ | https://economie-circulaire.ademe.fr/tarification-incitative | A | 2024-01-01 | Effets TI OMR emballages verre decheteries | ADEME SINOE data on TI effects: DMA -5% average; residual household waste (OMR) -31% average (-34% under REOMi, -16% TEOMi); separate packaging/paper collection +17%; glass +10%; flows to decheteries +13%. TI cuts volumes most where the service is individually billed. | 635d5d20-b4b6-4a0a-8a0b-3a6a87f741be
FCT-010 | FACT | ✧ | https://economie-circulaire.ademe.fr/tarification-incitative | A | 2024-01-01 | Delai mise en place TI 3 ans | ADEME: at least 3 years between the elected decision and effective billing of an incentive levy (REOMi), +1 year for incentive tax (TEOMi). Requires bacs with chips, taxpayer/producer files, blank billing test - heavy logistics explaining slow national roll-out. | 37863c0d-d21b-4478-8ead-090b1bfa359f
FCT-011 | FACT | ✧ | https://economie-circulaire.ademe.fr/tarification-incitative | A | 2024-01-01 | Etude TI incivilites 28 collectivites | ADEME/ECOGEOS/ALTAIR study (2024) observed 28 collectivites (18 in TI, 10 control): field measurements show TI does not systematise wild dumps of residual waste; annual OMR wild-dump estimates remain moderate vs TI benefits (~30% OMR reduction). | d88b9d2c-ece4-4c14-9e17-009906dca5ba
FCT-012 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8574484 | A | 2025-06-04 | DMA 2021 615 kg/hab OMR 245 kg | Insee Premiere 2055 (data 2021, mainland+Reunion): 41Mt DMA collected, 615 kg/hab (+4% in 10 years; LTECV -10% 2020 target missed). Residual waste (OMR) 245.1 kg/hab (-14% vs 286.4 in 2011); sorted waste 369.6 kg/hab (+21%). More waste collected in tourist zones; less and better sorted under incentive pricing; more with income and commercial density. | 1f718c6b-60e7-4359-8e83-1c442cee2445
FCT-013 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8574484 | A | 2025-06-04 | 3 circuits collecte OMR 40 pourcent decheteries 40 pourcent | Three collection circuits in 2021: residual waste ~40% of tonnage (door-to-door mixed bins), separate collection ~20% (door-to-door tri bins or voluntary drop points PAV), decheteries 40% (incl. 99% of rubble, 88% of bulky waste, 78% of green waste/biowaste). Decheteries are co-equal to residual collection. | c4c216d3-d28b-4ba3-b98f-c9919cdc20c9
FCT-014 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8574484 | A | 2025-06-04 | 1800 installations de traitement 2022 | In 2022 France had ~1,800 waste treatment installations: 710 sorting (tri), 670 composting, 120 incineration with energy recovery, 170 landfill (stockage). The treatment mix constrains what any collection system can do with sorted waste. | 90d47fc6-cc79-4c83-ae12-fbfdb193f124
FCT-015 | FACT | ✧ | https://www.notre-environnement.gouv.fr/themes/societe/le-mode-de-vie-des-menages-ressources/article/les-dechets-menagers-en-france-chiffres-et-enjeux-pour-l-environnement | A | 2025-04-14 | Depense gestion dechets 2022 21,6 milliards | SDES (14/04/2025): 21.6 billion EUR spent on waste management in France in 2022, +8.5% vs 2021. This is the aggregate bill behind the 'bordel' perception - paid via TEOM/REOM and subsidies. | 9a810d1f-c1aa-43e0-8168-162cae4aa044
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-004
FCT-002 | SRC-004
FCT-003 | SRC-004
FCT-004 | SRC-004
FCT-005 | SRC-004
FCT-006 | SRC-004
FCT-007 | SRC-004
FCT-008 | SRC-003
FCT-009 | SRC-003
FCT-010 | SRC-003
FCT-011 | SRC-003
FCT-012 | SRC-002
FCT-013 | SRC-002
FCT-014 | SRC-002
FCT-015 | SRC-001

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE
FCT-010 | ELIGIBLE:VERIFIE
FCT-011 | ELIGIBLE:VERIFIE
FCT-012 | ELIGIBLE:VERIFIE
FCT-013 | ELIGIBLE:VERIFIE
FCT-014 | ELIGIBLE:VERIFIE
FCT-015 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -
FCT-010 | WRITE | -
FCT-011 | WRITE | -
FCT-012 | WRITE | -
FCT-013 | WRITE | -
FCT-014 | WRITE | -
FCT-015 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-31T07:41:38.319494+00:00","fact_mem":{"FCT-001":"83112980-8d6e-41ef-98b8-800bbfc5adc9","FCT-002":"db37fb3b-f9f1-4f0d-8e1c-8a46fd67c73b","FCT-003":"178ce2a7-666b-4173-960e-7a7b041310b9","FCT-004":"51d65a22-d126-4095-b206-0129e5a0bdb8","FCT-005":"c247eb92-b789-4f0d-b28c-b3f161dc49f9","FCT-006":"eb244cef-7bd7-48d3-b7f7-15afdcfecc45","FCT-007":"2a3748c0-69a2-4eef-b5ee-5ba0c41a7cd5","FCT-008":"4382306f-8ef6-4393-a252-67034703024b","FCT-009":"635d5d20-b4b6-4a0a-8a0b-3a6a87f741be","FCT-010":"37863c0d-d21b-4478-8ead-090b1bfa359f","FCT-011":"d88b9d2c-ece4-4c14-9e17-009906dca5ba","FCT-012":"1f718c6b-60e7-4359-8e83-1c442cee2445","FCT-013":"c4c216d3-d28b-4ba3-b98f-c9919cdc20c9","FCT-014":"90d47fc6-cc79-4c83-ae12-fbfdb193f124","FCT-015":"9a810d1f-c1aa-43e0-8168-162cae4aa044"},"mnemo_row":"WROTE:pending","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-010","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-011","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-012","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-013","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-014","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-015","reason":"NONE","success":1}],"writeback_row":{"attempted":15,"blocked":0,"eligible":15,"failure":0,"success":15}}

PERSISTENCE_META: MNEMO_ROW:WROTE:pending | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:15;attempted:15;success:15;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[15 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-010 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-011 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-012 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-013 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-014 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-015 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
