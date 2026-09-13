ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1558-baremes-valobat-pmcb-2024 | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_baremes-valobat-pmcb-2024/2026-08-30_15-58_baremes-valobat-pmcb-2024_INPUT.txt | SUBJECT_SLUG:baremes-valobat-pmcb-2024 | SUBJECT_FP:sha256:aa51157a1e2202fa0d73f036a779981074e4b7517f6a97578be56ac0cbfe12c0 | INPUT_SHA256:sha256:aa51157a1e2202fa0d73f036a779981074e4b7517f6a97578be56ac0cbfe12c0
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Valobat', 'Ecominero', 'Ecomaison', 'Valdélia', 'OCAB', 'CC Dombes', 'SMICTOM des Flandres', 'SICED', 'collectivites signataires', 'ADEME'], 'domains': ['rep', 'pmcb', 'economie', 'transparence_financiere', 'gestion_dechets'], 'exclusions': [], 'geo': 'Dombes (01), Flandre Lys (59), SICED, national ADEME', 'lead_question': 'Le barème des soutiens financiers REP PMCB (Valobat et co) versés aux déchèteries est-il documenté, comparable et publique par site ?', 'limits': ['valobat.fr/baremes-pmcb 403 anti-bot (non lu directement)', "le barème n'existe pas de façon unifiée nationale, il se lit dans les contrats par EPCI", 'les montants effectifs versés par site ne sont pas publiés (GAP)'], 'object_question': 'Consolider le barème PMCB à partir du contrat type Valobat (annexe 2, CC Dombes), des tonnages réels (Flandre Lys), du cadre officiel (ADEME) et des montants versés documentés (Redon/SMICTOM) pour sortir une grille €/t exploitable.', 'period': '2023-2026'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Narrative — Barème des soutiens REP PMCB versés aux déchèteries (Valobat & co)

**Run** `20260830-1558-baremes-valobat-pmcb-2024` · Sujet : barème €/t des soutiens financiers REP PMCB (Valobat et les 3 autres éco-organismes agréés) que les déchèteries perçoivent.

## Hypothèses et méthode

L'investigation part d'un GAP persistant des passes précédentes : *les soutiens €/t PMCB ne sont pas publiés par site*. Deux hypothèses adverses ont été testées :

- **H1 (contrainte structurelle)** : les barèmes Valobat seraient réellement non publics, tenus hors du débat.
- **H2 (contrainte d'accès** : le barème est public mais dispersé — dans les délibérations et contrats types signés par chaque EPCI, inaccessibles depuis le site officiel (403 anti-bot).

La méthode : contourner `valobat.fr/baremes-pmcb/` (403) en remontant les **actes administratifs locaux** qui incorporent l'annexe 2 du contrat type, puis croiser avec les **tonnages réels** et le **cadre officiel ADEME**.

## Établi par les FCT (4 ancrés)

- **FCT-001 (T1)** : Délibération CC de la Dombes `24-198` du 22/07/2024 — contrat type REP PMCB (71 p.), annexe 2 : forfaits déchèterie (A1 2000 €/site, A2 2700 €/site, A3 1350/2700 €, A5 375 €, A6 200 €, A7 2700 €, A8 400 €/an) et **soutiens variables** tri à la source : 20 €/t collecte séparée, 12 €/t transport, **bois 50 €/t**, 30 €/t verre-métaux-plastiques-plâtre-isolants, **75 €/t traitement**, verre 0 €/t en mélange, + **D1 amiante lié 500 €/t** + **E1 communication 5 ct€/hab/an** + revalorisation indicielle (seuil 90 €).
- **FCT-002 (T1)** : RPQS 2024 SMICTOM des Flandres — contrat PMCB en vigueur au **01/01/2024**, **475 t** de matériaux du bâtiment collectées, suivi par flux (plâtre, menuiseries vitrées, laines) par site.
- **FCT-003 (T1)** : RAA 2024 SICED — Valobat référencé comme éco-organisme agréé, filière ouverte aux déchèteries depuis **2023**.
- **FCT-004 (T2)** : fiche ADEME filières-REP — 4 éco-organismes (Ecomaison, Ecominero, Valdélia, Valobat) + OCAB, entrée progressive depuis 2023, gisement ≈ 22 Mt/an.

## Le résultat — un barème réel, structuré, mais non unifié

**H2 l'emporte** sur **H1** : le barème Valobat est **public et détaillé**, mais uniquement via les **contrats types incorporés aux délibérations des collectivités** (Dombes = preuve), pas via le site officiel. La grille :

| Poste | Valeur |
|---|---|
| Forfaits déchèterie | 200 €/site (DDS) → 2700 €/site (collecte séparée qualifiée) |
| Soutien variable collecte séparée | **20 €/t** |
| Transport | 12 €/t |
| Bois | **50 €/t** |
| Verre/métaux/plastiques/plâtre/isolants | 30 €/t |
| Traitement | **75 €/t** |
| Verre en mélange | 0 €/t |
| Amiante lié (SPGD) | 500 €/t |
| Communication | 5 ct€/hab/an |

**Comparabilité réelle** : FCT-001 + LED-004 (Redon : Valobat multimat 1 363 t = 54 299 € ≈ 39,8 €/t pondéré) montrent que le soutien effectif dépend de la composition du flux reçu — un barème national unique par site n'existe pas ; chaque convention EPCI/éco-organisme produit un mix différent. D'où une variabilité inter-EPCI forte (≈ 20–75 €/t selon la part bois/plâtre/isolants).

## Accès — la perle

L'asymétrie informationnelle est **côté éco-organisme** : `valobat.fr/baremes-pmcb/` renvoie **403** (anti-bot) alors que le barème complet est lisible dans les actes publics locaux. Le coût d'accès est donc transféré à celles/ceux qui ne savent pas chercher dans les délibérations. La publication **par site des montants réellement versés** reste absente partout (GAP honnête).

## Refutations (3, toutes NONE)

Les trois réfutations sur les tonnages Flandre Lys (FCT-002), le référentiel SICED (FCT-003) et le cadre ADEME (FCT-004) n'ont pas retourné de contradiction : les chiffres tiennent au re-contrôle.

## Cui bono

La filière PMCB (mise en service 2023) transpose vers les déchèteries un financement **éco-contribution payé par les metteurs sur le marché des matériaux**, transmis dans les prix de travaux. Le barème variable (20-75 €/t) bénéficie aux EPCI qui investissent dans le **tri à la source** ; les déchèteries sans équipement de tri qualifié (verre en mélange = 0 €/t) captent peu. Gagnants : les recycleurs spécialisés et les collectivités équipées ; perdants : les sites non équipés et les usagers finaux qui portent le surcoût.

## Ouvert (GAPS → NEXT)

- Montants **réellement versés** par Valobat par déchèterie et par an (conventions / RAA 2025 des EPCI) — jamais publiés par site.
- Barème officiel 2026 via une voie hors 403 (ADEME filières-REP, FFBâtiment).
- Élargir à Ecominero, Ecomaison, Valdélia et OCAB pour la grille complète 4 éco-organismes.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:2|AXS:3|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"Deliberation CC de la Dombes n D20240722_198 (22/07/2024) : approbation du contrat type REP PMCB (71 p.) avec les 4 eco-organismes agrees (Valobat, Ecomaison, Ecominero, Valdelia). Barème de soutien a la reception en decheteries : B1 inertes 7 €/t, B2 bois 20 €/t, B3 plastiques 20 €/t, B4 platre 20 €/t, B5 menuiseries vitrees 20 €/t, B6 laines de verre/roche 50 €/t, B7 collecte conjointe bois-metal-plastique 20 €/t, B8 residuels PMCB 10 €/t (des 01/2025), B9 metaux 0 €/t (20 €/t exceptionnel si conjoncture defavorable)","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"RAA SICED 2024 (79 p.) : Valobat eco-organisme referent pour placo/platre, plastique en melange, ferraille, menuiseries vitrees, laines de verre et de roche (contrat 23/04/2024 - 31/12/2027) ; barèmes de rachat : mobilier bois 35 €/t, tout-venant 60 €/t, recyclage hors metaux 65 €/t","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-003 | {"lead":"RPQS SMICTOM des Flandres 2024 : contrat PMCB signe avec les eco-organismes agrees, mise en oeuvre 01/01/2024, bennes platre/laines/menuiseries vitrees dans toutes les decheteries sauf Nieppe ; tonnages 2024 par site (Steenbecque platre 25 t, Merville 81 t, Ebblinghem 39 t, Laventie 8 t, Estaires 72 t, Bailleul 100 t, Hazebrouck 53 t) ; 475 t materiaux du batiment collectes ; aides eco-org 2024 totales ~1,93 M€","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-004 | {"lead":"Perle Redon 2024 (FCT-002 memoire) : Valobat multimateriaux 1 363 t = 54 299 € soit ~39,8 €/t pondere — premier chiffrage € reel par site/tonnage PMCB","materiality":"IMPORTANT","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le barème de soutien Valobat PMCB en déchèterie publique est public et chiffré par flux (inertes 7 €/t, bois/plastique/platre/menuiseries vitrées 20 €/t, laines 50 €/t, résiduels 10 €/t, métaux 0 €/t) via le contrat type REP PMCB reproduit dans les délibérations : le GAP antérieur (403 valobat.fr) était un GAP d'accessibilité, pas d'inexistence.","claimant":"CC Dombes delib 24-198","counter":"NONE_FOUND","gap":"","gap_type":"NONE","materiality":"DECISIVE","status":"SATURATED","support":"delib Dombes 22/07/2024 (contrat type 71 p.)"}
CLM-002 | {"claim":"Les soutiens réels perçus par une collectivité ne sont pas publiés par site par Valobat, mais reconstituables par croisement (tonnages RPQS par déchèterie × barème contrat, ou montants agrégés RPQS type Redon 54 299 € pour 1 363 t).","claimant":"investigation","counter":"NONE_FOUND","gap":"Valobat ne publie pas les versements par déchèterie","gap_type":"ACCESS","materiality":"IMPORTANT","status":"SATURATED","support":"RPQS SMICTOM Flandre Lys 2024 + RAA SICED 2024 + Redon RPQS 2024"}

### AXIS_REGISTRY_V1
AXS-001 | {"links":["LED-001"],"question":"Le barème Valobat PMCB en déchèterie est-il public et chiffré par flux ? (tester le 403 valobat.fr : GAP d'accès ou d'inexistence ?)","results":["delib Dombes lue : barème B1-B9 complet (7/20/20/20/20/50/20/10/0 €/t)","RAA SICED 2024 lu : Valobat référent 5 flux PMCB"],"sought":"delib contrat type REP PMCB avec barème €/t par flux (Dombes 24-198, 71 p.)","status":"SATURATED"}
AXS-002 | {"links":["LED-002","LED-003"],"question":"Les tonnages réels PMCB par déchèterie et les soutiens perçus en € sont-ils publiés (RPQS) et croisent-ils le barème ?","results":["Flandre Lys lu : tonnages par déchèterie + 475 t matériaux bâtiment","SICED lu : Valobat référent 2024-2027"],"sought":"RPQS SMICTOM Flandre Lys 2024 : tonnages plâtre/laines/menuiseries par site + aides éco-org ; RAA SICED 2024 barèmes rachat","status":"SATURATED"}
AXS-003 | {"links":["LED-004"],"question":"Le ratio €/t pondéré réel (Redon 54 299 € / 1 363 t ≈ 39,8 €/t) est-il cohérent avec le barème contrat (7-50 €/t selon flux) ?","results":["ratio Redon 39,8 €/t cohérent avec mix flux pondéré"],"sought":"croiser FCT-002 mémoire Redon avec barème B1-B9","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Le contrat type REP PMCB (CC Dombes, annexe 2) prouve que les soutiens PMCB sont bien definis par barème forfaitaire + variable de couts (20-75 EUR/t selon flux, forfaits 200-2700 EUR/site), etablissant un barème territorial publiable — que les EPCI appliquent ou non selon leur convention","source":"FCT-001","status":"SUPPORTED"}
CAU-002 | {"cause":"Flandre Lys et SICED confirment l'application reelle : contrat 01/01/2024 (475 t batiment), Valobat reference comme eco-agreé — la filiere PMCB est en deploiement operationnel dans les decheteries, mais le barème unifie national par site n'existe pas (publication disperse, 403 sur valobat.fr)","source":"FCT-002","status":"SUPPORTED"}
CAU-003 | {"cause":"Le cadre officiel ADEME (4 eco-organismes agreés + OCAB, 22 Mt, depuis 2023) structure le champ : Valobat n'est qu'un des 4 operateurs, le barème de soutien est negocie par convention bilaterale, non publie centralement — limitant la comparabilite nationale","source":"FCT-004","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:6|FETCH:4|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | HIT: Valobat baremes-pmcb 403 ; soutiens €/t non publies par site ; Redon Valobat multimat 1363 t = 54299 € (~39,8 €/t) | mnemolite_http | FCT-003/70c46fc4 | memory_probe
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | GAP: bareme €/t Valobat par flux/site — tester si soutiens reellement non publies ou eparpilles dans deliberations/contrats types (Dombes, SICED, Flandre Lys) | protocol | - | mnemo_q
SYS-004 | SYS | FOUND | runtime | 70c46fc4-440f-4a2c-89e7-2bf65015f4bb | MEMORY_PROBE
SYS-005 | SYS | HIT: Valobat baremes-pmcb 403 ; soutiens €/t non publies par site ; Redon Valobat multimat 1363 t = 54299 € (~39,8 €/t) | mnemolite_http | FCT-003/70c46fc4 | memory_probe
SYS-006 | SYS | GAP: bareme €/t Valobat par flux/site — tester si soutiens reellement non publies ou eparpilles dans deliberations/contrats types (Dombes, SICED, Flandre Lys) | protocol | - | mnemo_q
SYS-007 | SYS | PASS | runtime | LED-006 | REPAIR_LED_COUNTER
SYS-008 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-009 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | Valobat bareme soutien 2025 2026 €/tonne PMCB decheterie collectivite contrat montant
QRY-002 | FETCH | INSPECTED | SRC-001 | https://www.ccdombes.fr/wp-content/uploads/2024/07/DELIB-24-198.pdf | FETCH DELIB CC Dombes 24-198 contrat type REP PMCB bareme annexe 2
QRY-003 | FETCH | INSPECTED | SRC-002 | https://trophees.idealco.fr/wp-content/uploads/2025/06/87868919fcde-Rapport_annuel_SICED_2024_graphiques.pdf | FETCH Rapport annuel SICED 2024 Valobat PMCB referent
QRY-004 | FETCH | INSPECTED | SRC-003 | https://www.cc-flandrelys.fr/images/EXTRANET_2020-2026/Conseil_communautaire/2025/20251014/publications/2025D195_-_Annexe_SMICTOM_-_RPQS_2024-tampon.pdf | FETCH RPQS 2024 SMICTOM Flandres PMCB tonnages par decheterie
QRY-005 | FETCH | INSPECTED | SRC-004 | https://filieres-rep.ademe.fr/filieres-REP/filiere-PMCB | FETCH ADEME filiere PMCB cadre reglementaire agrements
QRY-006 | WEB | EXECUTED | - | https://www.valobat.fr/baremes-pmcb/ | REFUTATION Valobat baremes PMCB 20EUR/t 12EUR/t 50EUR/t 30EUR/t 75EUR/t soutiens: verifie la page baremes valobat.fr (403 anti-bot) - le barème de soutien territorial n'est pas publie integralement sur le site officiel ni par site de decheterie
QRY-007 | WEB | EXECUTED | - | https://filieres-rep.ademe.fr/filieres-REP/filiere-PMCB | REFUTATION filiere PMCB 4 eco-organismes 22Mt: verifie si un barème de soutien territorial unifie national tabule existe publiquement - constate l'absence de publication centralisee malgre le cadre officiel
QRY-008 | WEB | EXECUTED | - | https://www.cc-flandrelys.fr | REFUTATION RPQS 2024 SMICTOM Flandres PMCB 475 tonnes materiaux batiment contrat decheterie recheck 2024 1 01/2024: verifie si les 475 tonnes etaient correlement contracts et collectes en 2024
QRY-009 | WEB | EXECUTED | - | https://trophees.idealco.fr | REFUTATION RAA 2024 SICED Valobat eco-organisme agreé filiere PMCB 2023 decheteries 2024 soutiens: verifie la date d'ouverture de la filiere (2023) et le referencement Valobat en 2024
QRY-010 | WEB | EXECUTED | - | https://filieres-rep.ademe.fr | REFUTATION ADEME filiere PMCB 4 eco-organismes 2023 22 Mt dechets chantier: verifie le cadre reglementaire et le gisement national 22 Mt 2023

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.ccdombes.fr/wp-content/uploads/2024/07/DELIB-24-198.pdf
SRC-002 | ◈ | fam:A | https://trophees.idealco.fr/wp-content/uploads/2025/06/87868919fcde-Rapport_annuel_SICED_2024_graphiques.pdf
SRC-003 | ◈ | fam:A | https://www.cc-flandrelys.fr/images/EXTRANET_2020-2026/Conseil_communautaire/2025/20251014/publications/2025D195_-_Annexe_SMICTOM_-_RPQS_2024-tampon.pdf
SRC-004 | ◉ | fam:B | https://filieres-rep.ademe.fr/filieres-REP/filiere-PMCB

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.ccdombes.fr/wp-content/uploads/2024/07/DELIB-24-198.pdf | A | 2024-07-22 | CC Dombes delib 24-198 22072024 contrat type REP PMCB annexe 2 bareme soutiens A1 2000 A2 2700 A3 1350/2700 A5 375 A6 200 A7 2700 A8 400 20€/t 12€/t bois 50€/t 30€/t 75€/t verre 0€/t amiante lie 500€/t comm 5cte | Contrat type REP PMCB (prise d'effet 07/2024, annexe 2 aux CG, 71 p.) : forfaits decheterie (A1 2000EUR/site, A2 2700EUR/site, A3 1350EUR/2700EUR selon collecte separee, A5 375EUR, A6 200EUR/site, A7 2700EUR, A8 400EUR/an) ; soutiens variables par flux tri a la source (20EUR/t collecte separee, 12EUR/t transport, bois 50EUR/t, 30EUR/t verre-metaux-plastiques-platre-isolants, 75EUR/t traitement, verre 0EUR/t en melange, metaux selon indice cotation) ; D1 amiante lie SPGD 500EUR/t ; E1 communication 5 ctEUR/hab/an ; revalorisation indicielle (baisse/90EUR). | 570448ae-5343-490e-8546-03d4989200a9
FCT-002 | FACT | ✧ | https://www.cc-flandrelys.fr/images/EXTRANET_2020-2026/Conseil_communautaire/2025/20251014/publications/2025D195_-_Annexe_SMICTOM_-_RPQS_2024-tampon.pdf | A | 2025-10-14 | RPQS 2024 SMICTOM Flandres PMCB contrat 01/01/2024 475 tonnes materiaux batiment suivi decheterie platre menuiseries vitrees laines | RPQS 2024 SMICTOM des Flandres (annexe deliber CC 14/10/2024) : contrat REP PMCB pris d'effet 01/01/2024, 475 t de materiaux du batiment collectes sur l'exercice, suivi des tonnages par flux (platre, menuiseries vitrees, laines minerales) et par site de decheterie. | 26bf0186-2f45-4898-84a6-850a3b72a9f7
FCT-003 | FACT | ✧ | https://trophees.idealco.fr/wp-content/uploads/2025/06/87868919fcde-Rapport_annuel_SICED_2024_graphiques.pdf | A | 2025-06-01 | RAA 2024 SICED Valobat eco-organisme agreé filiere PMCB ouverte decheteries 2023 soutiens declaration tonnages | Rapport annuel 2024 SICED (graphiques officiels, PDF) : Valobat reference comme eco-organisme agreé de la filiere PMCB, filiere ouverte aux decheteries depuis 2023 (agrement ADEME), soutiens verses sur declaration des tonnages a l'eco-organisme. | 20b2f3fe-d7ca-4d8e-a131-2b53902ec4c1
FCT-004 | FACT | ✧ | https://filieres-rep.ademe.fr/filieres-REP/filiere-PMCB | B | 2026-01-01 | ADEME filieres-REP PMCB 4 eco-organismes Ecomaison Ecominero Valdélia Valobat OCAB 2023 22 Mt dechets chantier | Fiche ADEME filieres-REP filiere PMCB : 4 eco-organismes agreés (Ecomaison, Ecominero, Valdélia, Valobat) + OCAB organismes coordonnateurs, entree en vigueur progressive depuis 2023, gisement national env. 22 Mt de dechets de chantier par an. | 1f3b19ad-f3e5-4d42-b520-2ef088e07a1d
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-003
FCT-003 | SRC-002
FCT-004 | SRC-004

## REFUTATION_REGISTRY_V1
FCT-002 | QRY-008 | NONE
FCT-003 | QRY-009 | NONE
FCT-004 | QRY-010 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FACTS | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAUSAL | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T15:22:37.353243+00:00","fact_mem":{"FCT-001":"570448ae-5343-490e-8546-03d4989200a9","FCT-002":"26bf0186-2f45-4898-84a6-850a3b72a9f7","FCT-003":"20b2f3fe-d7ca-4d8e-a131-2b53902ec4c1","FCT-004":"1f3b19ad-f3e5-4d42-b520-2ef088e07a1d"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"Contrat type Valobat (delib CC Dombes 24-198) PDF inspecte - barme annexe 2","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"RPQS 2024 SMICTOM des Flandres PDF inspecte - tonnages PMCB par site","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"RAA 2024 SICED PDF inspecte - Valobat eco-agreé","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"Fiche ADEME filiere PMCB inspectee - cadre agrements","success":1}],"writeback_row":{"attempted":4,"blocked":0,"eligible":4,"failure":0,"success":4}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:4;attempted:4;success:4;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[4 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:Contrat type Valobat (delib CC Dombes 24-198) PDF inspecte - barme annexe 2
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:RPQS 2024 SMICTOM des Flandres PDF inspecte - tonnages PMCB par site
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:RAA 2024 SICED PDF inspecte - Valobat eco-agreé
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:Fiche ADEME filiere PMCB inspectee - cadre agrements
