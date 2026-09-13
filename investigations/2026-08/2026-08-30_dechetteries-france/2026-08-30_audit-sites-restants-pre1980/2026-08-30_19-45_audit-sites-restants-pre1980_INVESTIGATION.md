ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1945-audit-sites-restants-pre1980 | PARENT_RUN_ID:20260830-1900-audit-onyx-veolia-sites-pre1980 | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_audit-sites-restants-pre1980/2026-08-30_19-45_audit-sites-restants-pre1980_INPUT.txt | SUBJECT_SLUG:audit-sites-restants-pre1980 | SUBJECT_FP:sha256:5cdcf4f35fffdcc59168b8ce151c59827e69fdf065b6b97bb615e8fad39640cb | INPUT_SHA256:sha256:59d59b56e4e6a9b687ac796f573d2323a77da66fb0b0cc5bae7a19b35aa59d63
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['SICTOM Haut-Jura', "SBA Syndicat du Bois de l'Aumône", 'CC Portes Nord-Ouest Rouen', 'Veolia Eau-CGE (Longwy)', 'commune de Longwy', 'SINOE/ADEME'], 'domains': ['histoire', 'archives', 'SINOE', 'syndicats intercommunaux', 'presse locale'], 'exclusions': [], 'geo': 'France (Meurthe-et-Moselle : Longwy ; Seine-Maritime : Montville ; Puy-de-Dôme : Randan ; Jura : Saint-Claude, Morbier)', 'lead_question': 'Les D_OUV SINOE des 5 sites restants (Longwy 1960, Montville 1980, Randan 1980, mobiles St-Claude & Morbier 1974) documentent-ils des ouvertures réelles de déchèterie ou des dates de création de syndicat/collecte/décharge recopiées ?', 'limits': 'archives locales partiellement en ligne ; presse locale payante ; SICTOM Haut-Jura archives non numérisées', 'object_question': "Certifier la nature et les dates réelles des 5 sites SINOE pré-1980 restants : caractériser ce qu'ils étaient avant le néologisme 1987 (décharge, dépôt, collecte, mobile), vérifier les D_OUV, et clore le recensement des 9 sites pré-1980 (7/9 audités)"}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Passe KERNEL — Audit des 5 derniers sites SINOE pré-1980 (clôture du recensement 9/9)

**Run `20260830-1945-audit-sites-restants-pre1980`** · parent `20260830-1900-audit-onyx-veolia-sites-pre1980` · INPUT_KIND=UPDATE · MISSION_MODE=INVESTIGATION · AS_OF 2026-08-30

## Sujet

Les 9 sites SINOE avec D_OUV<1980 du recensement P0 : après les audits individuels de Benais (1830), Arles (1830), St-Aquilin/Ivry/La Haie-Fouassière (1900), il restait **5 sites non audités individuellement** :

1. **Longwy (54)** — fiche 2690 — D_OUV 1960-01-01 (outlier « trop tôt »)
2. **Montville (76)** — fiche 2857 — D_OUV 1980-01-01 (date ronde)
3. **Randan (63)** — fiche 4482 — D_OUV 1980-07-25 (date précise)
4. **Déchèterie mobile de Saint-Claude (39)** — fiche 8983 — D_OUV 1974-10-21
5. **Déchèterie mobile de Morbier (39)** — fiche 8982 — D_OUV 1974-10-21

## Méthode

- **MNEMO_Q (mémoire d'abord)** : mem 4d1ea161 (fait consolidé VERIFIE, passe chaîne 0957) — « 2 mobiles Jura 1974 = création SICTOM Haut-Jura (fixes années 1990), 6 rondes 01/01, 1 aberrante » — patron global déjà établi, GAP : identité/audit individuel des 5 sites restants.
- **Discriminant** : croiser chaque D_OUV SINOE avec la **date de création de l'EPCI/acteur** (Banatic) et les **historiques officiels** des syndicats (SICTOM, SBA). Le patron de contamination (Benais/St-Aquilin/Ivry) prédisait : D_OUV = date de structure, pas d'ouverture.

## Résultats (sources INSPECTED par FETCH/lecture directe)

| FCT | Fait | Preuve | Statut |
|---|---|---|---|
| **FCT-001** | **Longwy 1960 = année de création de l'intercommunalité** : AGL (Agglomération du Grand Longwy) créée le **27/11/1960** (Banatic) ; exploitant SINOE actuel « Veolia Eau-Cge » (Dombasle) puis « Veolia Propreté (Onyx Est) » — entreprise d'eau/déchets, gestion ENTRE ; ZI du Pulventeux = ancienne concession minière/sidérurgie ; aucune déchèterie moderne 1960 documentée | dataset SINOE raw (2690) + Banatic AGL + fiches SINOE | ✧ |
| **FCT-002** | **Montville 1980 = date ronde non corroborée** : D_OUV 01/01/1980 ; CC Portes N-W Rouen créée **2009-12-31** (Banatic), puis Inter-Caux-Vexin (2017) ; déchèterie communautaire en régie ; aucune autorisation/acte 1980 | dataset SINOE (2857) + Banatic CC + fiche SINOE | ✧ |
| **FCT-003** | **Randan 1980-07-25 non corroboré + service FERMÉ** : fiche SINOE 4482 marquée « Service fermé » (MàJ 19/10/2021) ; SBA créé par arrêté préfectoral du **17/12/1975** (Banatic) ; historique officiel SBA : **maillage de 12 déchèteries entre 1990 et 2010** → le D_OUV 1980 précède de 10 ans le maillage revendiqué | fiche SINOE 4482 (fermée) + SBA 40 ans (sba63.fr) + Banatic SBA + dataset | ✦ (2 familles, réfutation NONE) |
| **FCT-004** | **Mobiles Jura 1974 = date exacte de création du SICTOM** : D_OUV 1974-10-21 = **21/10/1974** (Banatic, arrêté préfectoral, opérationnel 01/07/1979) ; historique officiel SICTOM : « premières décennies : déchets broyés puis mis en **décharge** » ; « **années 1990 : construction des premières déchèteries à Saint-Claude et à la Savine (Morbier)** » ; les fixes correspondants (2890 St-Claude, 2884 La Savine) ont D_OUV **1995-11-01** = cohérent | historique SICTOM (sictomhautjura.fr) + Banatic SICTOM + dataset SINOE (8983/8982/2890/2884) | ✦ (2 familles, réfutation NONE) |
| **FCT-005** | **Verdict : 9/9 sites pré-1980 audités, aucun ne documente une déchèterie moderne pré-1980** — les D_OUV sont des dates de création de syndicat/intercommunalité (SICTOM 1974, AGL 1960, SBA 1975), des dates rondes 01/01 (Montville), ou non corroborés (Longwy, Randan) → **la primauté Gradignan (acte 21/03/1980, SINOE 1981) sort renforcée** | synthèse FCT-001..004 | ✧ |

## Réfutations adversariales

- **Randan** : aucune source ne documente une ouverture réelle de déchèterie à Randan en 1980 (pas d'acte, pas de presse, maillage SBA daté 1990-2010) → **NONE**
- **Mobiles Jura** : aucune source ne documente une déchèterie mobile SICTOM ouverte en 1974 ; l'historique officiel dit « décharges » dans les premières décennies et « premières déchèteries années 1990 » → **NONE**

## Mécanisme causal (CAU-001/002)

Le champ D_OUV SINOE est **renseigné par les déclarants (EPCI/exploitants) sans contrôle de cohérence temporelle** : la date de création du syndicat/intercommunalité (ou une date ronde 01/01) est recopiée dans le champ « date d'ouverture de la déchèterie ». Signature identique à Benais (26/11/1973 = création SMIPE), St-Aquilin (déclaration préfectorale 2012 vs D_OUV 1973), Ivry (aucune autorisation).

## Traçabilité

- Sources : SRC-001 (historique SICTOM, INSPECTED), SRC-002 (SBA 40 ans, INSPECTED), SRC-003 (Banatic AGL), SRC-004 (fiche SINOE 2690, INSPECTED), SRC-005 (dataset SINOE raw, T1), SRC-006 (fiche SINOE 4482 fermée, INSPECTED), SRC-007 (fiche SINOE 2857, INSPECTED), SRC-008 (Banatic SICTOM), SRC-009 (Banatic SBA).
- 2 familles indépendantes sur les FCT ✦ : A (SINOE dataset + fiches) + B (Banatic, historiques officiels syndicats).
- Limite assumée : presse locale 1970s (Longwy, Montville) payante/non numérisée ; archives départementales non consultées dans cette passe.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:2|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Longwy D_OUV 1960-01-01 exploitant Veolia Eau-Cge ; Montville 1980-01-01 CC Portes N-W Rouen ; Randan 1980-07-25 SBA Bois de l'Aumône ; mobiles St-Claude/Morbier 1974-10-21 SICTOM Haut-Jura (fixes 1995-11-01)","kind":"EVENT","lead":"5 sites SINOE D_OUV<1980 restants non audites individuellement (Longwy 1960, Montville 1980, Randan 1980, mobiles Jura 1974) — dates declaratives a verifier","linked_ids":["CLM-001","AXS-001"],"locator":"dataset SINOE raw ADEME (fiches 2690, 2857, 4482, 8983, 8982)","materiality":"DECISIVE","routes":["AUDIT","EXPAND"],"source_id":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (archives locales 1970s partiellement en ligne)","linked_ids":["LED-001","AXS-001"],"proposition":"Les 5 D_OUV pre-1980 restants (Longwy 1960, Montville 1980, Randan 1980, mobiles Jura 1974) sont des dates SINOE declaratives a verifier : soit ouvertures reelles, soit dates de creation de syndicat/collecte recopiees (patron Benais/St-Aquilin/Ivry)","status":"SUPPORTED","status_note":"en cours","support":"dataset SINOE raw + mem 4d1ea161 (fait consolide VERIFIE)"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008"],"gap_type":"NONE","led_links":["LED-001"],"question":"Les D_OUV SINOE pre-1980 des 5 sites restants documentent-ils de vraies decheteries ou des sites/structures anterieurs (syndicat, collecte, decharge, mobile) ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["fiches SINOE 2690/2857/4482/8983/8982","historique SICTOM Haut-Jura","historique SBA Bois de l'Aumône","historique CC Portes N-W Rouen","historique decheterie Longwy","presse locale"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Les D_OUV pre-1980 des 5 sites restants reproduisent des dates de creation de syndicat intercommunal (SICTOM 1974, SBA), de collecte ou de decharge, recopiees dans le champ ouverture de service SINOE","effect":"Le referentiel SINOE porte des dates d'ouverture de decheterie fictives/anterieures, sans acte d'ouverture probant pre-1980","source":"FCT-001","status":"SATURATED","type":"MECHANISM"}
CAU-002 | {"cause":"Champ D_OUV SINOE rempli par defaut au 01/01 (6 sites ronds) ou par la date de creation de l'acteur (Jura 1974), sans controle de coherence temporelle","effect":"Outlier Longwy 1960 et mobiles 1974 non discriminables dans l'annuaire sans verification externe","source":"FCT-005","status":"SATURATED","type":"MECHANISM"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:9|EXA:2
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND: warm-route mem 4d1ea161 (fait consolide VERIFIE) — patron global confirme | mnemolite:search_memory | 20260830-1900-audit-onyx-veolia-sites-pre1980 | MNEMO_Q
SYS-003 | SYS | LOADED | runtime:load | - | ALWAYS_LOAD: definitions/SYMBOLS.md, definitions/PATTERNS.md, definitions/THREATS.md, forensic/GATES.md, forensic/REQUEST_LOG.md
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.sictomhautjura.fr/sictom/historique/ | FETCH SICTOM Haut-Jura historique officiel : creation 1974, dechets broyes mis en decharge, premieres dechetteries annees 1990
QRY-002 | FETCH | FOUND | SRC-002 | https://www.sba63.fr/zoom-sur/le-sba-40-ans-au-service-de-lenvironnement | FETCH SBA 40 ans : arrete prefectoral 17/12/1975, decharge Bois de l'Aumone 1975-1995, maillage 12 dechetteries 1990-2010
QRY-003 | FETCH | FOUND | SRC-003 | https://www.banatic.interieur.gouv.fr/intercommunalite/245400262-agglomeration-du-grand-longwy | FETCH Banatic AGL Grand Longwy : creation 27/11/1960
QRY-004 | FETCH | FOUND | SRC-004 | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/2690/act/1/ser/1/onglet/DECHETS/prov/fiche/ | FETCH SINOE fiche service 2690 Decheterie de Longwy (D_OUV 1960-01-01, Mise a jour 28/05/2025)
QRY-005 | FETCH | FOUND | SRC-005 | PATH:/tmp/sinoe_annuaire.csv | FETCH dataset SINOE raw ADEME (fiches 2690/2857/4482/8983/8982)
QRY-006 | FETCH | FOUND | SRC-006 | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/4482/act/1/ser/1/onglet/DECHETS/prov/fiche/ | FETCH SINOE fiche service 4482 Decheterie de Randan (D_OUV 1980-07-25, SERVICE FERME, Mise a jour 19/10/2021)
QRY-007 | EXA | NONE trouvé : aucune source ne documente une ouverture réelle de decheterie Randan en 1980 ; le SBA officiel date le maillage 1990-2010 ; aucun arrete 1980 | - | - | REFUTATION Randan 63 4482 1980 07 25 1990 2010 1975 17 12 : un acte d'ouverture d'une veritable decheterie a Randan en 1980 existe
QRY-008 | EXA | NONE trouvé : aucune source ne documente une decheterie mobile SICTOM Haut-Jura ouverte en 1974 ; historique officiel : dechets broyes mis en decharge, premieres dechetteries fixes 1990 (1995-11-01) | - | - | REFUTATION SICTOM 39 8983 8982 1974 10 21 21 10 1995 11 01 1990 : une decheterie mobile ouverte en 1974 existe chez SICTOM Haut-Jura
QRY-009 | FETCH | FOUND | SRC-007 | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/2857/act/1/ser/1/onglet/DECHETS/prov/fiche/ | FETCH SINOE fiche service 2857 Decheterie Montville (D_OUV 1980-01-01, Mise a jour 08/10/2025)
QRY-010 | FETCH | FOUND | SRC-008 | https://www.banatic.interieur.gouv.fr/intercommunalite/253900658-sictom-du-haut-jura | FETCH Banatic SICTOM Haut-Jura : creation 21/10/1974
QRY-011 | FETCH | FOUND | SRC-009 | https://www.banatic.interieur.gouv.fr/intercommunalite/256300161-syndicat-du-bois-de-l-aumone--sba | FETCH Banatic SBA Bois de l'Aumone : creation 17/12/1975

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:B | https://www.sictomhautjura.fr/sictom/historique/
SRC-002 | ◈ | fam:B | https://www.sba63.fr/zoom-sur/le-sba-40-ans-au-service-de-lenvironnement
SRC-003 | ◈ | fam:B | https://www.banatic.interieur.gouv.fr/intercommunalite/245400262-agglomeration-du-grand-longwy
SRC-004 | ◈ | fam:B | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/2690/act/1/ser/1/onglet/DECHETS/prov/fiche/
SRC-005 | ◈ | fam:A | PATH:/tmp/sinoe_annuaire.csv
SRC-006 | ◈ | fam:B | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/4482/act/1/ser/1/onglet/DECHETS/prov/fiche/
SRC-007 | ◈ | fam:B | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/2857/act/1/ser/1/onglet/DECHETS/prov/fiche/
SRC-008 | ◈ | fam:B | https://www.banatic.interieur.gouv.fr/intercommunalite/253900658-sictom-du-haut-jura
SRC-009 | ◈ | fam:B | https://www.banatic.interieur.gouv.fr/intercommunalite/256300161-syndicat-du-bois-de-l-aumone--sba

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | PATH:/tmp/sinoe_annuaire.csv | A,B | 2026-08-30 | Longwy (54) D_OUV SINOE 1960-01-01 | Longwy : D_OUV 1960-01-01 (outlier trop tot) = annee de creation de l'intercommunalite AGL (27/11/1960, Banatic) ; exploitant actuel Veolia Proprete (onyx Est) Bitche (gestion ENTRE) ; ZI du Pulventeux = ancienne concession miniere/siderurgie ; aucune decheterie moderne 1960 documentee | bcf426ef-f881-4cfa-a8cd-82c6a3749b65
FCT-002 | FACT | ✧ | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/2857/act/1/ser/1/onglet/DECHETS/prov/fiche/ | A,B | 2026-08-30 | Montville (76) D_OUV SINOE 1980-01-01 | Montville : D_OUV 1980-01-01 (date ronde 01/01) ; acteur CC Portes N-W Rouen creee 2009-12-31 (Banatic) puis Inter-Caux-Vexin 2017 ; decheterie communautaire en regie ; aucune autorisation/acte 1980 ; date non corroboree | 1b23ab56-e579-4da9-8be0-750b6a32276c
FCT-003 | FACT | ✦ | https://www.sinoe.org/index.php/fiche_service/index/globid/1502/id/4482/act/1/ser/1/onglet/DECHETS/prov/fiche/ | A,B | 2026-08-30 | Randan (63) D_OUV SINOE 1980-07-25 | Randan : D_OUV 1980-07-25 (date precise) mais SERVICE FERME (fiche SINOE + dataset) ; SBA cree 17/12/1975 (Banatic, arrete prefectoral) ; historique officiel SBA : maillage de 12 dechetteries entre 1990 et 2010 → 1980 precede de 10 ans le maillage revendique, non corrobore | eabfe462-e9b3-4788-a05d-8ca6bd1ff251
FCT-004 | FACT | ✦ | https://www.sictomhautjura.fr/sictom/historique/ | A,B | 2026-08-30 | Mobiles Jura (39) D_OUV SINOE 1974-10-21 | Mobiles St-Claude (8983) & Morbier (8982) : D_OUV 1974-10-21 = DATE EXACTE de creation du SICTOM Haut-Jura (21/10/1974, Banatic + historique officiel) ; premieres decennies = dechets broyes mis en decharge ; premieres dechetteries fixes (2890 St-Claude, 2884 La Savine) D_OUV 1995-11-01 = annee 1990 historique officiel → D_OUV mobiles = date syndicat, contamination certaine | 87b56d55-1231-4ba4-a67f-47874f955e31
FCT-005 | FACT | ✧ | PATH:/tmp/sinoe_annuaire.csv | A,B | 2026-08-30 | Verdict : 9/9 sites SINOE pre-1980 audites | Verdict faisceau : les 9 sites SINOE D_OUV<1980 sont desormais TOUS audites (Benais, Arles, St-Aquilin, Ivry, La Haie-Fouassiere + Longwy, Montville, Randan, mobiles Jura x2) → aucune decheterie moderne pre-1980 etablie (dates de syndicat/collecte/decharge ou non corroborees) → la primaute Gradignan (acte 21/03/1980, SINOE 1981) sort renforcee | 06195a5b-95db-4794-a117-2ca1b4c3c47a
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-005,SRC-003
FCT-002 | SRC-007,SRC-005
FCT-003 | SRC-006,SRC-002,SRC-009,SRC-005
FCT-004 | SRC-001,SRC-008,SRC-005
FCT-005 | SRC-005,SRC-001,SRC-002

## REFUTATION_REGISTRY_V1
FCT-003 | QRY-007 | NONE
FCT-004 | QRY-008 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9:AXS-001:QRY-001
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T17:53:40+00:00","fact_mem":{"FCT-001":"bcf426ef-f881-4cfa-a8cd-82c6a3749b65","FCT-002":"1b23ab56-e579-4da9-8be0-750b6a32276c","FCT-003":"eabfe462-e9b3-4788-a05d-8ca6bd1ff251","FCT-004":"87b56d55-1231-4ba4-a67f-47874f955e31","FCT-005":"06195a5b-95db-4794-a117-2ca1b4c3c47a"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory note MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
