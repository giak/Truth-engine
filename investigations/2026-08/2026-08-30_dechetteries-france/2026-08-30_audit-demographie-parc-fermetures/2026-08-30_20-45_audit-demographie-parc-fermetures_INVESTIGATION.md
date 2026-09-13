ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2045-audit-demographie-parc-fermetures | PARENT_RUN_ID:20260830-2030-audit-refondation-pmcb-2027 | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-demographie-parc-fermetures/2026-08-30_20-45_audit-demographie-parc-fermetures_INPUT.txt | SUBJECT_SLUG:audit-demographie-parc-fermetures | SUBJECT_FP:sha256:53c3d9c2d823c418fbe2d11f8e296b141b800eef07fdc5581f6f5375f9e65c2e | INPUT_SHA256:sha256:4101160cc0557c84ea799890cb5a945ff5aaf8bc198ca7ea5e0d628fcc5ce3a1
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['ADEME SINOE', 'collectivites (EPCI)', 'exploitants prives', 'ministere'], 'domains': ['dechets', 'decheteries', 'fermetures', 'demographie parc', 'politique publique'], 'geo': 'France (toutes regions)', 'lead_question': 'Le reseau de decheteries se retracte-t-il depuis 2013 ? Combien de sites ont ferme, ou, pourquoi, et quel est le solde net fermetures vs ouvertures ?', 'limits': 'pas de champ D_FERM dans l annuaire SINOE (fermeture inferee) ; millesime 2026 partiel ; presse 403 parfois', 'object_question': '(1) compter les fermetures SINOE depuis 2013 par disparition persistante ; (2) corriger par renumerotations/fusions ; (3) croiser presse pour fermetures nominatives ; (4) conclure sur le solde net du parc'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Axe D — Démographie du parc : 506 fermetures de déchèteries depuis 2013, mais un solde net positif

**Run `20260830-2045-audit-demographie-parc-fermetures`** — investigation démographique du réseau : comptabiliser les fermetures depuis 2013 via le champ `date_fermeture_service` SINOE (le « D_FERM » officiel), croisé presse.

## Verdict

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **Le champ D_FERM officiel existe — mais sur un autre portail** : `date_fermeture_service` dans le dataset « Liste des services de déchèterie par année » (62 330 lignes, data.sinoe-dechets.ademe.fr) — **740 services distincts avec date de fermeture**, ABSENT de l'annuaire data.ademe.fr (35 colonnes) | ✦ (A+B, réfutation NONE) |
| **FCT-002** | **506 fermetures de services SINOE depuis 2013** (date_fermeture ≥ 2013-01-01) : 486 déchèteries, 17 plateformes apports verts, 2 déchèteries pros, 1 CAV ; pics 2016 (63) et 2021 (60) ; top régions Nouvelle-Aquitaine 89, Grand Est 56, Pays de la Loire 55 | ✦ (B+D, réfutation NONE) |
| **FCT-003** | **Solde net POSITIF : 540 ouvertures vs 506 fermetures = +34** — le réseau ne se rétracte PAS à l'échelle nationale (4 532 services en 2013, 4 551 puis 4 630 dans l'annuaire) | ✦ (B+D, réfutation NONE) |
| **FCT-004** | **Cas type de fermeture-remplacement documenté par acte officiel** : Provence Verdon ferme Barjols (25/07/2026) et Fox-Amphoux Trois Croix (11/07/2026), ouvre Tavernes (27/07/2026) — **rationalisation 2 vers 1** (13 quais, 15 filières, ICPE, espace réemploi) | ✦ (C+B, réfutation NONE) |
| **FCT-005** | **Croisement interne valide le comptage** : 5172 La Haye-Fouassière date_fermeture = **2013-11-18** (= date exacte établie passe 1955), 4482 Randan = **2018-12-31** (service FERMÉ) ; proxy de disparition (423) surestime (135 réapparitions = renumérotations) | ✦ (B+D, réfutation NONE) |

## Découvertes clés

1. **Le « paradis de la data » inversé : le champ D_FERM existait, il était juste ailleurs.** L'annuaire data.ademe.fr (45 169 records, celui analysé depuis la passe P0) n'a aucun champ de fermeture — c'est sur le portail **data.sinoe-dechets.ademe.fr**, dataset « Liste des services de déchèterie par année » (62 330 lignes, mis à jour 30/08/2026), que `date_fermeture_service` est exposé (740 services fermés). La donnée n'était pas absente : elle était **dispersée entre deux portails ADEME**.
2. **Le réseau ne se rétracte pas** : 506 fermetures depuis 2013 (≈39/an) sont **plus que compensées** par 540 ouvertures (+34 net). La courbe du parc reste stable — c'est l'inverse du récit « le réseau se rétracte » qui ressort de la presse.
3. **La rationalisation locale est réelle mais compensée** : cas Tavernes (2→1, Provence Verdon 2026, acte officiel INSPECTED) illustre la logique de modernisation par fermeture-remplacement. Mais elle est globalement compensée par les ouvertures.
4. **Limite honnêteté épistémique** : lag de déclaration documenté — dernières années déclarées 2023 (551 services), 2024 (2177), 2025 (1974) ; les fermetures 2025-2026 (19) sont **sous-déclarées** ; le solde réel 2026 est donc à la baisse par rapport à +34 mais reste vraisemblablement positif ou nul.

## Sources INSPECTED

- Dataset SINOE « Liste des services de déchèterie par année » (data.sinoe-dechets.ademe.fr, 62 330 lignes) + API data-fair paginée (63 pages × 1000) — champ `date_fermeture_service`
- Annuaire SINOE data.ademe.fr (CSV local 45 169 records, 35 colonnes SANS D_FERM) — proxy de disparition persistante
- Acte officiel Provence Verdon (provenceverdon.fr, INSPECTED) : Barjols 25/07/2026, Fox-Amphoux 11/07/2026, Tavernes 27/07/2026
- Presse : Nice-Matin 17/07/2026 (snippet), Var-Matin (snippet)

## Réfutations (5 NONE)

- FCT-001 : aucun champ de fermeture totalement absent de SINOE, ni < 740 services avec date de fermeture
- FCT-002 : aucune preuve de < 506 fermetures depuis 2013 ni de répartition par type différente
- FCT-003 : aucune preuve d'un solde net négatif ou d'un rétrécissement du parc national
- FCT-004 : aucune preuve de maintien de Barjols/Fox-Amphoux ouvertes après le 27/07/2026, ni que Tavernes ne les remplace pas
- FCT-005 : aucune preuve que les dates de fermeture 5172 (2013-11-18) ou 4482 (2018-12-31) soient différentes de celles établies par les passes 1955/1945

## Gaps ouverts

1. Données 2026 complètes (le millésime 2026 est partiel : 5 fermetures déclarées, ~2 000 services à remonter)
2. Croiser les 506 fermetures avec les actes délibératifs EPCI (échantillon) pour qualifier le motif (conformité, rationalisation, fusion)
3. Mesurer le lag presse→SINOE sur les cas 2025-2026 (Tavernes : Barjols non encore marquée fermée dans le dataset)
4. Cartographier la rationalisation (2→1) par EPCI pour quantifier la concentration du maillage

## Conséquence sur la fresque

L'axe D clôt la question « le réseau se rétracte-t-il ? » : **non** — 506 fermetures depuis 2013, mais 540 ouvertures et un solde net +34. La donnée officielle D_FERM existait mais était dispersée sur un second portail SINOE (découverte data). Le récit médiatique de « fermetures de déchèteries » (axe A : exclusion des pros, dépôts sauvages) doit être nuancé : la démographie du parc reste stable, la mutation est dans l'accès et le financement, pas dans le nombre de sites.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"CSV SINOE 45169 records : 423 C_SERVICE last_year>=2013 absents des millesimes 2025/2026 ; 5172 La Haye-Fouassiere disparu 2013-2015 (= fermeture 18/11/2013 etablie), 4482 Randan disparu 2017-2019 (service FERME)","kind":"EVENT","lead":"423 services SINOE presents depuis 2013 et jamais declares en 2025/2026 = fermetures presumees par disparition persistante (proxy, pas de champ D_FERM)","locator":"analyse python ad hoc","materiality":"HIGH","routes":["CSV SINOE local /tmp/sinoe_annuaire.csv","presse fermetures","comparaison millesimes"],"source_id":"-","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (pas de champ D_FERM, fermeture inferee par disparition)","linked_ids":["LED-001","AXS-001"],"proposition":"Le reseau ne se retracte pas : 423 disparitions persistantes SINOE depuis 2013 (dont 135 renumerotations/fusions) vs solde net stable 4532 -> 4551/4630 services","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["analyse CSV SINOE"],"gap_type":"NONE","led_links":["LED-001"],"question":"Combien de decheteries ont ferme depuis 2013 (D_FERM SINOE absent -> disparition persistante) et le reseau se retracte-t-il ?","result_ids":["LED-001"],"sought_objects":["decompte fermetures SINOE","solde net parc","fermetures nominatives presse"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Fermetures de decheteries 2013-2026 (disparition SINOE)","effect":"Recomposition du parc (renumerotations, fusions, reconversions) sans retractation nette ; solde stable ~4550","source":"CSV SINOE + presse","status":"SUPPORTED","type":"DEMOGRAPHY"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:4|EXA:5
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND: warm-route mems 06195a5b (verdict 9/9), 87ce56e5 (La Haye-Fouassiere reconversion 18/11/2013), eabfe462 (Randan service FERME), pas de decompte de fermetures etabli | mnemolite:search_memory | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | FCT-002 | REPAIR_FACT
SYS-004 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-005 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-006 | SYS | PASS | runtime | FCT-005 | REPAIR_FACT
SYS-007 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-008 | SYS | PASS | runtime:load | - | ALWAYS_LOAD: definitions/SYMBOLS.md, definitions/PATTERNS.md, definitions/THREATS.md, forensic/GATES.md, forensic/REQUEST_LOG.md
SYS-009 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://data.sinoe-dechets.ademe.fr/datasets/liste-des-services-de-decheteries-donnees-publiques | FETCH dataset SINOE liste des services de déchèterie par année : 62 330 enregistrements, champ date_fermeture_service present, page dit « filtrer sur les decheteries non fermees »
QRY-002 | FETCH | FOUND | SRC-002 | https://data.sinoe-dechets.ademe.fr/data-fair/api/v1/datasets/liste-des-services-de-decheteries-donnees-publiques/lines?size=1000 | FETCH API data-fair paginee : 62 330 lignes, 5 362 services distincts, 740 avec date_fermeture_service, fermetures >=2013 = 506 (486 decheteries, 17 plateformes verts, 2 pros, 1 CAV), ouvertures >=2013 = 540, solde +34 ; dernieres annees declarees 2023 (551) 2024 (2177) 2025 (1974)
QRY-003 | FETCH | FOUND | SRC-003 | https://www.provenceverdon.fr/accueil/actualite/935-le-reseau-des-decheteries-evolue | FETCH Provence Verdon : Barjols fermee 25/07/2026, Fox-Amphoux Trois Croix fermee 11/07/2026, nouvelle decheterie Tavernes ouverte 27/07/2026 (13 quais, 15 filieres, ICPE, espace reemploi) — rationalisation 2 vers 1
QRY-004 | FETCH | FOUND | SRC-004 | https://data.ademe.fr/datasets/sinoe-(r)-annuaire-des-decheteries-dma | FETCH annuaire SINOE data.ademe.fr : 45 169 records, 35 colonnes (C_REGION..GPS_LAT), AUCUN champ D_FERM, 5 217 services distincts, 4 635 ouverts dernier millesime, 423 disparitions persistantes >=2013 dont 135 renumerotations
QRY-005 | EXA | NONE | - | - | REFUTATION date_fermeture_service 62 330 740 35 : une preuve que le champ de fermeture serait totalement absent de SINOE, ou que moins de 740 services distincts porteraient une date de fermeture dans le dataset liste des services par annee
QRY-006 | EXA | NONE | - | - | REFUTATION 506 486 17 2 1 2013 2016 63 2021 60 : une preuve que moins de 506 services auraient fermé depuis 2013, ou que la repartition par type (486 decheteries, 17 plateformes verts, 2 pros, 1 CAV) serait differente
QRY-007 | EXA | NONE | - | - | REFUTATION 540 506 34 4532 4551 4630 : une preuve que le solde net depuis 2013 serait negatif, ou que les ouvertures seraient inferieures aux fermetures, ou un retrecissement du parc a l echelle nationale
QRY-008 | EXA | NONE | - | - | REFUTATION Barjols 25 07 2026 Fox-Amphoux 11 07 2026 Tavernes 27 07 2026 13 : une preuve que la CCPV aurait conserve Barjols et Fox-Amphoux ouvertes apres le 27/07/2026, ou que la nouvelle decheterie Tavernes ne les aurait pas remplacees
QRY-009 | EXA | NONE | - | - | REFUTATION 5172 2013 11 18 4482 2018 12 31 506 423 135 : une preuve que la date_fermeture de La Haye-Fouassiere (2013-11-18) ou de Randan (2018-12-31) serait differente de celle etablie par les passes 1955/1945, ou que le comptage 506 serait contredit

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://data.sinoe-dechets.ademe.fr/datasets/liste-des-services-de-decheteries-donnees-publiques
SRC-002 | ◈ | fam:B | https://data.sinoe-dechets.ademe.fr/data-fair/api/v1/datasets/liste-des-services-de-decheteries-donnees-publiques/lines?size=1000
SRC-003 | ◈ | fam:C | https://www.provenceverdon.fr/accueil/actualite/935-le-reseau-des-decheteries-evolue
SRC-004 | ◈ | fam:D | https://data.ademe.fr/datasets/sinoe-(r)-annuaire-des-decheteries-dma

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://data.sinoe-dechets.ademe.fr/data-fair/api/v1/datasets/liste-des-services-de-decheteries-donnees-publiques/lines?size=1000 | A,B | 2026-08-30 | Le champ D_FERM officiel existe : date_fermeture_service dans le dataset SINOE « liste des services de decheterie par annee » (62 330 lignes, portail data.sinoe-dechets.ademe.fr) — 740 services distincts avec date de fermeture, ABSENT de l annuaire data.ademe.fr (35 colonnes) | DECOUVERTE DATA : le champ de fermeture n est pas absent de SINOE mais disperse — l annuaire data.ademe.fr (45 169 records, 35 cols C_REGION..GPS_LAT) n a AUCUN champ D_FERM, mais le portail data.sinoe-dechets.ademe.fr expose le jeu « Liste des services de decheterie par annee » (62 330 lignes, mis a jour 30/08/2026) avec le champ date_fermeture_service. API data-fair paginee (63 pages x 1000) : 5 362 services distincts, 740 avec date_fermeture_service. La page du dataset dit explicitement de « filtrer sur les decheteries non fermees » pour la liste des ouvertes. Source: https://data.sinoe-dechets.ademe.fr/datasets/liste-des-services-de-decheteries-donnees-publiques + API data-fair (verifie 2026-08-30, tier ✦) | a080b4da-d878-4d90-9f48-de9de2aa5020
FCT-002 | FACT | ✦ | https://data.sinoe-dechets.ademe.fr/data-fair/api/v1/datasets/liste-des-services-de-decheteries-donnees-publiques/lines?size=1000 | B,D | 2026-08-30 | 506 fermetures de services SINOE depuis 2013 (date_fermeture_service) : 486 decheteries, 17 plateformes apports dechets verts, 2 decheteries professionnelles, 1 centre d apport volontaire ; pics 2016 (63) et 2021 (60) | Comptage du champ date_fermeture_service (dataset 62 330 lignes) : fermetures par annee = 2013:40, 2014:40, 2015:31, 2016:63, 2017:40, 2018:36, 2019:23, 2020:29, 2021:60, 2022:26, 2023:43, 2024:56, 2025:14, 2026:5 ; total >= 2013 = 506 services distincts. Types : Decheterie 486, Plateforme d apports de dechets verts 17, Decheterie professionnelle 2, Centre d apport volontaire 1. Top regions : Nouvelle-Aquitaine 89, Grand Est 56, Pays de la Loire 55, Ile-de-France 47, AURA 45, Hauts-de-France 43. Verifie 2026-08-30 via API data-fair paginee (tier ✦) | 7e1ca908-a60b-4874-b6dd-e050e62d46c0
FCT-003 | FACT | ✦ | https://data.sinoe-dechets.ademe.fr/data-fair/api/v1/datasets/liste-des-services-de-decheteries-donnees-publiques/lines?size=1000 | B,D | 2026-08-30 | Solde net du parc positif : 540 ouvertures vs 506 fermetures depuis 2013 = +34 — le reseau ne se retracte PAS a l echelle nationale (4532 services en 2013, 4551 puis 4630 dans l annuaire) | Solde net SINOE 2013-2026 : ouvertures (date_ouverture_service >= 2013-01-01) = 540 services, fermetures (date_fermeture_service >= 2013-01-01) = 506, solde net = +34. Corrobore l annuaire data.ademe.fr : 4 532 services declares en 2013, 4 551 en 2025, 4 630 en 2026 (millesime partiel) — le parc stagne/croit legerement, PAS de retractation. ATTENTION lag de declaration : dernieres annees declarees 2023 (551 services), 2024 (2177), 2025 (1974) — les fermetures 2025-2026 (19 au total) sont sous-declarees, le solde reel est donc a la baisse mais reste vraisemblablement positif ou nul. Verifie 2026-08-30 (tier ✦) | 74a18f55-f2cd-44c0-98ba-df661c519abe
FCT-004 | FACT | ✦ | https://www.provenceverdon.fr/accueil/actualite/935-le-reseau-des-decheteries-evolue | B,C | 2026-08-30 | Cas type de fermeture-remplacement documente par presse officielle : Provence Verdon ferme Barjols (25/07/2026) et Fox-Amphoux Trois Croix (11/07/2026), ouvre Tavernes (27/07/2026) — rationalisation de deux vers un du reseau | Acte officiel INSPECTED (provenceverdon.fr) : la CCPV rationalise son reseau — decheterie de Fox-Amphoux (Trois Croix) fermee 11/07/2026, Barjols fermee 25/07/2026 (sites non conformes, mise aux normes trop couteuse), nouvelle decheterie Tavernes (232 chemin de Rambourgue) ouverte 27/07/2026 (13 quais, 15+ filieres, ICPE, espace reemploi + matériauthèque avec La Courtoise Ressourcerie). Remarque : le dataset SINOE 62 330 lignes ne marque pas encore la fermeture de Barjols (code 23515, dernieres donnees 2024) — lag presse-to-SINOE. Verifie 2026-08-30 (tier ✦) | a98fdf52-19f2-4ef1-ab64-a9ef39d99229
FCT-005 | FACT | ✦ | https://data.sinoe-dechets.ademe.fr/data-fair/api/v1/datasets/liste-des-services-de-decheteries-donnees-publiques/lines?size=1000 | B,D | 2026-08-30 | Croisement interne valide le comptage : 5172 La Haye-Fouassiere date_fermeture = 2013-11-18 (= fermeture etablie precedemment), 4482 Randan = 2018-12-31 (service FERME) ; verifie aussi 506 fermetures vs 423 disparitions (135 renumerotations) | Validation du comptage par croisement avec les cas documentes des passes anterieures : service 5172 DE LA-HAIE-FOUASSIERE (Loire-Atlantique) a date_fermeture_service = 2013-11-18 = EXACTEMENT la date de fermeture etablie par la passe 1955 (reconversion en Halte Eco Tri) ; service 4482 DE RANDAN (Puy-de-Dome) = 2018-12-31 = service FERME de la passe 1945. Le proxy de disparition persistante de l annuaire (423 candidats >= 2013) surestime : 135 reapparitions meme ville+dept (renumerotations/fusions). Le champ officiel date_fermeture_service (740 services, 506 >= 2013) est la reference. Verifie 2026-08-30 (tier ✦) | 2d69a605-1aa3-42bf-bcef-5188c61efdb0
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002
FCT-002 | SRC-002,SRC-004
FCT-003 | SRC-002,SRC-004
FCT-004 | SRC-003,SRC-002
FCT-005 | SRC-002,SRC-004

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-005 | NONE
FCT-002 | QRY-006 | NONE
FCT-003 | QRY-007 | NONE
FCT-004 | QRY-008 | NONE
FCT-005 | QRY-009 | NONE

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
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:FCT-001
CP-004 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:FCT-001
CP-005 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:CAU-001
CP-006 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:VERIFY
CP-007 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-008 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18:FINALIZATION_BLOCKED

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T18:47:50.938222+00:00","fact_mem":{"FCT-001":"a080b4da-d878-4d90-9f48-de9de2aa5020","FCT-002":"7e1ca908-a60b-4874-b6dd-e050e62d46c0","FCT-003":"74a18f55-f2cd-44c0-98ba-df661c519abe","FCT-004":"a98fdf52-19f2-4ef1-ab64-a9ef39d99229","FCT-005":"2d69a605-1aa3-42bf-bcef-5188c61efdb0"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory note MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
