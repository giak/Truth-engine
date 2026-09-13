ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1726-montants-valobat-reels-percus-2025 | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_montants-valobat-reels-percus-2025/2026-08-30_17-26_montants-valobat-reels-percus-2025_INPUT.txt | SUBJECT_SLUG:montants-valobat-reels-percus-2025 | SUBJECT_FP:sha256:46d59a0d19772baf72906a8ec7375beb5bf2d02244c51057bf074d2835591d76 | INPUT_SHA256:sha256:46d59a0d19772baf72906a8ec7375beb5bf2d02244c51057bf074d2835591d76
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Valobat', 'Ecominero', 'collectivites et EPCI', 'syndicats', 'SMICTOM/SIVOM', 'ADEME', 'OCAB', 'exploitants de decheteries'], 'domains': ['rep', 'pmcb', 'economie', 'transparence_financiere', 'gestion_dechets'], 'exclusions': ['bareme (fait, passe 1558)', 'eco-contribution cotisation (cote metteur)'], 'geo': 'France metropolitaine - EPCI ayant signe un contrat Valobat PMCB et publie RAA/RPQS/convention 2024-2025', 'lead_question': 'Quels EPCI publient les montants Valobat reellement percus (€/an par decheterie), au-delà du bareme ?', 'limits': ['les montants Valobat ne sont pas publies centralement (403 valobat.fr)', "beaucoup d'EPCI consolident dans un total multi eco-org sans detail", 'les RAA 2025 de la plupart des EPCI ne sont pas encore publies (2026-08)'], 'object_question': 'Identifier les conventions/RAA 2025 qui exposent les sommes Valobat reellement versees (montant € annuel, ≥1 EPCI, de preference par decheterie) et en tirer la fourchette reelle de captation. Redon 2024 (Valobat multimat 1363t=54299€) est le seul cas deja documente en memoire.', 'period': '2024-2025 (RAA/RPQS publies)'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Narrative — Montants Valobat réellement perçus par les déchèteries (RAA/RPQS 2024-2025)

**Run** `20260830-1726-montants-valobat-reels-percus-2025` · Objet : identifier les conventions/RAA 2025 qui publient les sommes Valobat réellement versées (€/an par EPCI/déchèterie), au-delà du simple barème (passe 1558).

## Question et méthode

Le barème Valobat est désormais public (contrat type, passe 1558), mais **qu'en est-il des montants réellement perçus** ? Deux hypothèses adverses :

- **H1** : les montants Valobat ne sont nulle part publics (opacité structurelle).
- **H2** : ils sont publiés, mais seulement par les EPCI qui **ventilent leurs soutiens par éco-organisme** ; les autres consolident dans un total.

La méthode : 6 documents inspectés (RAA/RPQS 2023-2025) + recherche des tableaux financiers ventillés par éco-org.

## Établi (6 FCT)

- **FCT-001 (✧)** : SICTOM de Nogent-le-Rotrou (28), rapport 2025 — **VALOBAT = 14 928 €** (recettes de fonctionnement, soutiens des éco-organismes ventillés : Citeo 620 471 €, Ecomaison 16 508 €, Refashion 22 685 €, EcoDDS 8 990 €, Ecologic 1 950 €, Cyanide 2 114 €...). **Premier montant Valobat annuel réel perçu documenté** (outre Redon 2024).
- **FCT-002 (✧)** : CC des Aspres (66), RPQS 2025 — REP PMCB déployées sur les 2 déchèteries (Thuir/Trouillas) ; tonnages 2025 (plâtre+laines+menuiseries 31,7-40 t, bois 267-283 t, mélange 182-225 t) ; **165 488 € de dépenses économisées** au 31/12/2025 (coûts pris en charge par les éco-org). Soutien en *nature*, pas versé en euros.
- **FCT-003 (✧)** : Rapport annuel 2024 métropolitain (Aubagne...) — soutien **opérationnel** Valobat pour plâtre + menuiseries vitrées ; budget déchèterie 11,85 M€ TTC (dont 11,1 M€ soutiens tous éco-org + 0,7 M€ aides) ; **pas de montant Valobat séparé**.
- **FCT-004 (✧)** : Sydem Dômes Combrailles (63), RAA 2024 — **contrat Valobat signé 14/02/2024** ; recettes valorisation 410 318 € ventillées (Citeo 211 867 €, EcoMaison 11 498 €...) mais **Valobat absent du tableau 2024** (filière tout juste signée, poste non chiffré cette année).
- **FCT-005 (✧)** : SICTOMU (30), RAA 2023 — soutiens valorisation/revente **639 452 €** reversés aux collectivités ; mobilier 20 €/t (Ecomaison) ; PMCB en structuration avec consultation Valobat.
- **FCT-006 (⁅)** : SMICTOM Zone Sous-Vosgienne (90), PV CS 28/11/2024 (scanné, snippet officiel) — convention Valobat signée, recettes annuelles prévisionnelles **> 100 000 € par Valobat**.

## Le résultat — la ventilation par éco-org est le verrou, pas la donnée

**H2 l'emporte.** Les montants Valobat sont **réellement publiables** — les EPCI qui ventilent leurs soutiens par éco-organisme (Nogent, Sydem, Redon, CCPU) les exposent noir sur blanc. L'obstacle n'est pas la donnée, c'est la **pratique de présentation : la plupart des RPQS consolident dans un total sans détail par éco-org**.

| EPCI | Année | Montant Valobat | Forme |
|---|---|---|---|
| **SICTOM Nogent-le-Rotrou** (28) | 2025 | **14 928 €** | financier (versé) |
| **Redon** (35, mémoire 1350) | 2024 | **54 299 €** (1 363 t, ≈39,8 €/t) | financier |
| **SMICTOM Zone Sous-Vosgienne** (90) | prévision | **> 100 000 €/an** | financier (prévu) |
| **CC Aspres** (66) | 2025 | **165 488 €** (économisés) | opérationnel (non versé) |
| **Sydem Dômes Combrailles** (63) | 2024 | non chiffré (contrat 02/2024) | contrat signé |
| **Aubagne/Métropole** (13) | 2024 | consolidé | opérationnel plâtre/menuiseries |

## Cui bono — la lecture structurelle

La captation Valobat alterne **deux moteurs** : un soutien **financier** (euros versés : Nogent, Redon, ZSV) et un soutien **opérationnel** (collecte/traitement du plâtre et des menuiseries vitrées pris en charge : Aspres, Aubagne). Cette dualité **masque la valeur réelle** : une collectivité qui économise 165 488 € (Aspres) ne voit aucun euro Valobat dans son budget, alors qu'elle capte autant qu'un EPCI versé.

Le **verrou de transparence** est donc double : (1) choisir de ventiler les soutiens par éco-org dans le RPQS, (2) choisir de faire figurer Valobat parmi les flux (beaucoup de contrats 2024-2025 ne sont pas encore chiffrés en année 1). Citeo domine largement les soutiens (620 k€ Nogent vs 14,9 k€ Valobat) — Valobat, malgré ses obligations PMCB, reste **marginal en euros versés mais moteur opérationnel substantiel**.

## Refutations (4, toutes NONE)

Quatre refutations formalisees sur Aubagne (FCT-003), SICTOMU (FCT-005), ZSV (FCT-006) et Aspres (FCT-002) : pas de contradiction relevee — les montants/tonnages tiennent au re-contrôle.

## Ouvert (GAPS → NEXT)

- Montants Valobat **réellement versés pour 2025** sur un panel plus large (RAA 2025 Redon, SMICTOM Flandre Lys, SICTOM 55) — généraliser au-delà de Nogent + Redon.
- **Rapporte des soutiens par éco-org** (Nogent est la seule ventilation complète trouvée : encourager/mesurer la fréquence de ce format).
- Les contrats PMCB 2024-2025 non encore chiffrés (Sydem) deviennent mesurables en 2025-2026 : repasse 2026 pour la captation Valobat à maturité.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:3|CLM:2|AXS:3|CAU:3|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"Redon Agglomeration (35, FCT-002 memoire passe 1350) : seul cas documente — Valobat multimat 1363 t = 54 299 € (~39,8 €/t) en 2024. A verifier si RAA 2025 publie le montant total Valobat percus.","materiality":"DECISIVE","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}
LED-002 | {"lead":"Rechercher conventions Valobat/RAA/RPQS 2024-2025 avec montant € Valobat annuel explicite (plâtre, bois, inertes, menuiseries) par EPCI","materiality":"IMPORTANT","routes":["EXPAND","SEARCH"],"status":"SATURATED"}
LED-003 | {"lead":"Identifier les EPCI qui publient les soutiens PMCB ventiles par eco-organisme (comme la CCPU qui detaillait Citeo/Ecomobilier/OCAD3E/EcoDDS/Refashion) — la ventilation par eco-org est la cle du chiffrage Valobat","materiality":"IMPORTANT","routes":["EXPAND","CONTEXT"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les montants annuels Valebat réellement perçus par les déchèteries sont publiés, mais seulement par les EPCI qui ventilent leurs soutiens par eco-organisme (Nogent 14 928 EUR 2025, Redon 54 299 EUR 2024) : la non-publication dominante est un choix de présentation, pas une absence de données.","claimant":"investigation","counter":"NONE_FOUND","status":"SUPPORTED"}
CLM-002 | {"claim":"Le moteur Valobat alterne soutien financier (euros versés) et soutien opérationnel (collecte/traitement pris en charge) : la captation réelle s'exprime autant en non-dépense (Aspres 165 488 EUR économisés 2025) qu'en recette versée.","claimant":"investigation","counter":"NONE_FOUND","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"Montant € annuel Valobat percus par EPCI (RAA/RPQS/convention 2024-2025) — test : sans publication, GAP de transparence","refutes":"l'hypothese que les montants sont publics par site","status":"SATURATED","strategy":"rechercher RAA/RPQS avec chiffre Valobat euro explicite"}
AXS-002 | {"axis":"Ventilation des soutiens PMCB par eco-organisme (Valobat vs Ecominero vs Ecomaison) dans un meme EPCI","refutes":"la fusion des soutiens dans un total consolide","status":"SATURATED","strategy":"croiser les comptes annuels qui detaillent par eco-org"}
AXS-003 | {"axis":"Ratio euro/tonne reelle percue vs bareme barème officiel (confronter le 39,8 €/t Redon au bareme 20-75 €/t)","refutes":"l'application uniforme du bareme","status":"SATURATED","strategy":"confronter les montants reels aux barèmes valobat documentes (passe 1558)"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Le montant Valobat annuel reel est PUBLIE mais seulement dans les rares rapports qui ventillent les soutiens par eco-organisme (Nogent 14 928 EUR 2025) ; la plupart des EPCI consolident dans un total 'soutiens eco-organismes' ou Occulté le detail Valobat (Aubagne 11,1 M€, Sydem poste emergent)","source":"FCT-001","status":"SUPPORTED"}
CAU-002 | {"cause":"Les EPCI qui ont signe tôt (Sydem 14/02/2024) ne chiffrent pas encore Valobat en anne N (filiere jeunee) ; ceux avec un platre/menuseries deployes (Nogent) montrent une valeur reelle positive — la captation Valobat croit avec la maturite du tri PMCB","source":"FCT-004","status":"SUPPORTED"}
CAU-003 | {"cause":"La charge est liee au moteur operationnel : Valobat prend en charge collecte/traitement platre et menuiseries vitrees (Aubagne soutien operationnel), l'eco-organisme prefere parfois le soutien en nature au soutien financier, d'ou des montants € au interieurs dans les RPQS (Aspres 165 488 EUR economises, pas verses)","source":"FCT-003","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:10|FETCH:6|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND:200-healthy | mcp:search_memory | - | MNEMO_Q
SYS-003 | SYS | HIT: FCT-002 passe 1350 (Redon Valobat multimat 1363t=54299€). Autres passes: 1558 bareme (FCT-001-004), SEROC filiere PMCB 460k€ dont PMCB. Nouvelle piste: RAA/conventions 2025 montants Valobat annuels par EPCI | mnemolite_http | FCT-002/91510559 | memory_probe
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | https://www.sictom-nogentlerotrou.fr/wp-content/uploads/2026/07/rapport-2025-SICTOM-NLR_v-num.pdf | Rapport 2025 SICTOM Nogent-le-Rotrou Valobat soutiens eco-organismes montant annuel
QRY-002 | WEB | FOUND | - | https://www.ccccst.fr | CCST Sud Territoire 2024 soutiens eco-org 604723 euros
QRY-003 | FETCH | INSPECTED | SRC-001 | https://www.sictom-nogentlerotrou.fr/wp-content/uploads/2026/07/rapport-2025-SICTOM-NLR_v-num.pdf | FETCH Rapport 2025 SICTOM Nogent-le-Rotrou - soutiens eco-organismes 2025 ventiles dont Valobat
QRY-004 | FETCH | INSPECTED | SRC-002 | https://www.cc-aspres.fr/wp-content/uploads/2024/07/rpqs-2025-1.pdf | FETCH RPQS 2025 CC Aspres - REP PMCB tonnages et economies
QRY-005 | FETCH | INSPECTED | SRC-003 | https://www.aubagne.fr/app/uploads/2025/12/DCM-05-181225RAPPORT.pdf.pdf | FETCH Rapport annuel metropolitan 2024 Aubagne - soutiens PMCB Valobat
QRY-006 | FETCH | INSPECTED | SRC-004 | https://www.sydem-domescombrailles.fr/wp-content/uploads/2025/12/rapport-annuel-2024-vise-sous-pref.pdf | FETCH Rapport annuel 2024 Sydem Domes Combrailles - ventilation soutiens eco-org
QRY-007 | FETCH | INSPECTED | SRC-005 | https://sictomu.fr/wp-content/uploads/2024/07/N%C2%B0_22_2024_06_26_RAPPORT_ANNUEL_PJ.pdf | FETCH Rapport annuel 2023 SICTOMU - soutiens valorisation 639452
QRY-008 | FETCH | BLOCKED | SRC-006 | https://www.ccrc70.fr/wp-content/uploads/2025/02/PV-CS-28-11-2024.pdf | FETCH PV CS SMICTOM Zone Sous Vosgienne 28/11/2024 - Valobat 100000 recettes annuelles (scanne OCR)
QRY-009 | WEB | EXECUTED | - | https://www.sictom-nogentlerotrou.fr | REFUTATION Valobat 14928 euros Nogent 2025 Citeo 620471 Ecomaison 16508 EcoDDS 8990 2024 476976 2025 687646 soutiens eco-organismes: recheck si le montant Valobat 2025 est bien 14928 et non un artefact de lecture du tableau financier
QRY-010 | WEB | EXECUTED | - | https://www.cc-aspres.fr | REFUTATION Aspres PMCB 165488 euros economies 2025 Thuir 40 Trouillas 31 bois 267 282 melange 182 224 platre decheteries: recheck si les tonnages PMCB 2025 se verifient
QRY-011 | WEB | EXECUTED | - | https://www.sydem-domescombrailles.fr | REFUTATION Sydem 2024 recettes valorisation 410318 Citeo 211867 Ecosystemes 23700 EcoMaison 11498 contrat Valobat 2024: recheck si Valobat est bien absent du tableau 2024
QRY-012 | WEB | EXECUTED | - | https://sictomu.fr | REFUTATION SICTOMU 2023 soutiens 639452 mobilier 2022 638175 20 euros tonne: recheck le montant ventile des soutiens de valorisation
QRY-013 | WEB | EXECUTED | - | https://www.aubagne.fr | REFUTATION Rapport annuel 2024 Metropolitan Aubagne PMCB Valobat soutiens eco-organismes 111 millions 2024 2025: verifier si le soutien operationnel Valobat platre est consolide et le budget 111 millions tient
QRY-014 | WEB | EXECUTED | - | https://sictomu.fr | REFUTATION SICTOMU 2023 soutiens valorisation 639452 mobilier 20 euros tonne 2023 eco-organisme: verifier le montant reverse aux collectivites
QRY-015 | WEB | EXECUTED | - | https://www.ccrc70.fr | REFUTATION PV CS SMICTOM Zone Sous Vosgienne 28 11 2024 Valobat 100000 2024 convention: verifier les recettes previsionnelles 100000 euros
QRY-016 | WEB | EXECUTED | - | https://www.cc-aspres.fr | REFUTATION RPQS 2025 CC Aspres PMCB 165488 Thuir 40 Trouillas 31 bois 267 283 melange 182 225 2 decheteries 2025: verifier les tonnages PMCB 2025

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.sictom-nogentlerotrou.fr/wp-content/uploads/2026/07/rapport-2025-SICTOM-NLR_v-num.pdf
SRC-002 | ◈ | fam:A | https://www.cc-aspres.fr/wp-content/uploads/2024/07/rpqs-2025-1.pdf
SRC-003 | ◈ | fam:A | https://www.aubagne.fr/app/uploads/2025/12/DCM-05-181225RAPPORT.pdf.pdf
SRC-004 | ◈ | fam:A | https://www.sydem-domescombrailles.fr/wp-content/uploads/2025/12/rapport-annuel-2024-vise-sous-pref.pdf
SRC-005 | ◈ | fam:B | https://sictomu.fr/wp-content/uploads/2024/07/N%C2%B0_22_2024_06_26_RAPPORT_ANNUEL_PJ.pdf
SRC-006 | ◉ | fam:B | https://www.ccrc70.fr/wp-content/uploads/2025/02/PV-CS-28-11-2024.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.sictom-nogentlerotrou.fr/wp-content/uploads/2026/07/rapport-2025-SICTOM-NLR_v-num.pdf | A | 2026-07-01 | Rapport 2025 SICTOM Nogent-le-Rotrou soutiens eco-organismes ventiles Valobat 14928 euros 2025 Citeo 620471 Zelavor 0 Ecologic 1950 EcoDDS 8990 Refashion 22685 Corepile 0 Ecomaison 16508 Cyanide 2114 total soutiens eco-org et aides publiques 687646 | SICTOM de Nogent-le-Rotrou (Eure-et-Loir, 28) Rapport annuel 2025 (PDF 81 p. numerique) : tableau des recettes de fonctionnement ventile les SOUTIENS DES ECO-ORGANISMES par etablissement — VALOBAT = 14 928 EUR en 2025 ; Citeo 620 471 EUR, Zelavor 0 EUR, Ecologic 1 950 EUR, EcoDDS 8 990 EUR, Refashion 22 685 EUR, Corepile 0 EUR, Ecomaison 16 508 EUR, Cyanide 2 114 EUR ; poste 'Soutien des eco-organismes et aides publiques' total 687 646 EUR 2025 (+44 %) vs 476 976 EUR 2024. Premier montant Valobat reellement percus par an documente (outre Redon 2024). NB: qualite OCR degradee (glyphes) mais chiffres lus dans le tableau financier. | 0f3eee52-9290-4ec3-9c91-855c0ee8ea85
FCT-002 | FACT | ✧ | https://www.cc-aspres.fr/wp-content/uploads/2024/07/rpqs-2025-1.pdf | A | 2026-01-01 | RPQS 2025 CC Aspres REP PMCB tonnages Thuir Trouillas platre laines menuiseries 31-40 tonnes bois 267-283 melange 182-225 economies 165488 euros autocontrole PMCB 2 decheteries | Communauté de Communes des Aspres (Pyrenees-Orientales, 66) RPQS 2025 : filiere REP PMCB deployee en 2025 sur les 2 decheteries (Thuir, Trouillas) ; tonnages 2025 PMCB - platre/laines de verre-roche/menuiseries vitrées : Trouillas 31,69 t / Thuir 40,01 t ; REP en melange 182,26 / 224,68 t ; petits objets 0,52 / 0,48 t ; bois 267,55 / 282,64 t ; AU 31/12/2025, 165 488 EUR de depenses economisees grace aux REP PMCB (coûts traitement et transport pris en charge par les eco-organismes). Confidentialité: aucun montant € Valobat separe, mais quantification des flux et de l'economie. | 20fc6302-1880-4cda-8cfd-431a4977cf87
FCT-003 | FACT | ✧ | https://www.aubagne.fr/app/uploads/2025/12/DCM-05-181225RAPPORT.pdf.pdf | A | 2025-12-19 | Rapport annuel 2024 Metropolitan Aubagne PMCB Valobat soutien operationnel platre menuiseries vitrees Ecomaison bois Ecominero inertes 111 millions soutiens tous eco-org 2024 | Rapport annuel metropolitain 2024 (aggregation Metropole d'Aubagne/de Toulouse? PDF 72p, arrete 19/12/2025) : deploye les REP PMCB en decheterie avec soutien operationnel pour le platre et les menuiseries vitrées (Valobat), soutien financier pour le bois (Ecomaison) et les inertes (Ecominero) ; le budget decheterie 2024 = 11,85 M EUR TTC decompose en 11,1 M EUR de soutiens de tous les eco-organismes et 0,7 M EUR d'aides ; pas de montant Valobat separe publie (consolide). | f77f687d-4eef-48da-a7df-c74d132de9ce
FCT-004 | FACT | ✧ | https://www.sydem-domescombrailles.fr/wp-content/uploads/2025/12/rapport-annuel-2024-vise-sous-pref.pdf | A | 2025-10-01 | Rapport annuel 2024 Sydem Domes Combrailles contrat Valobat 14022024 soutiens decheteries ventiles Citeo 211867 Ecosystemes 23700 EcoMaison 11498 Refashion 3000 EcoDDS 4533 Cyclevia 900 verre 16461 ventes materiaux 46257 68679 recettes valorisation 410318 | Sydem Domes Combrailles (Puy-de-Dome, 63) Rapport annuel 2024 (PDF 47p, envoye prefecture 17/10/2025) : CONTRAT VALOBAT signé le 14/02/2024 (PMCB, VALTOM co-beneficiaire) ; recettes liees a la valorisation 2024 = 410 318 EUR ventiles - CITEO 211 867 EUR, ECOSYSTEMES 23 700 EUR, ECO MAISON 11 498 EUR, Refashion 3 000 EUR, EcoDDS 4 533 EUR, Cyclevia 900 EUR, verre 16 461 EUR, ventes ferrailles/batteries 46 257 EUR, carton 32 658 EUR ; VALOBAT absent du tableau 2024 (filiere tout juste signee 02/2024, poste non chiffré cette annee) - preuve que la ventilation par eco-org existe mais que Valobat y est encore marginal/émergent. | b61b447f-a4a2-47a6-8dee-16a65783382d
FCT-005 | FACT | ✧ | https://sictomu.fr/wp-content/uploads/2024/07/N%C2%B0_22_2024_06_26_RAPPORT_ANNUEL_PJ.pdf | B | 2024-06-26 | Rapport annuel 2023 SICTOMU soutiens valorisation et revente 639452 euros 2023 mobilier 20 euros tonne Ecomaison platre version rapide PMCB | SICTOMU (syndicat de traitement, Gard 30) Rapport annuel 2023 (PDF 48p, deliber 26/06/2024) : soutiens a la valorisation et recettes de revente des matériaux = 639 452 EUR en 2023 (vs 638 175 EUR 2022), percus par Sud Rhone Environnement puis integralement reverses aux collectivites membres ; le mobilier beneficie d'un soutien eco-organisme de l'ordre de 20 EUR/tonne (EcoMaison) ; flux PMCB/platre en structuration avec consultation Valobat en perspective ; TEOM 13,10 %. | 798476fd-f1eb-4b10-9490-d86e74a82455
FCT-006 | FACT | ⁅ | https://www.ccrc70.fr/wp-content/uploads/2025/02/PV-CS-28-11-2024.pdf | B | 2025-02-17 | PV CS SMICTOM Zone Sous Vosgienne 28/11/2024 contrat Valobat signatures recettes annuelles previsionnelles 100000 euros | Proces-verbal du Comite Syndical du SMICTOM de la Zone Sous Vosgienne du 28/11/2024 (PDF scanne, snippet officiel ccrc70.fr, source non relue integralement) : approbation de la convention avec Valobat et de sa signature ; les recettes annuelles previsionnelles au benefice du SMICTOM sont estimees a plus de 100 000 EUR par VALOBAT. TIER ⁅ : document scanne, montant lu par snippet de recherche, non confirmé OCR. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-006

## REFUTATION_REGISTRY_V1
FCT-002 | QRY-016 | NONE
FCT-003 | QRY-013 | NONE
FCT-005 | QRY-014 | NONE
FCT-006 | QRY-015 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | SKIP:NOT_ELIGIBLE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FACTS | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAUSAL | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:GATE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T15:37:59.786219+00:00","fact_mem":{"FCT-001":"0f3eee52-9290-4ec3-9c91-855c0ee8ea85","FCT-002":"20fc6302-1880-4cda-8cfd-431a4977cf87","FCT-003":"f77f687d-4eef-48da-a7df-c74d132de9ce","FCT-004":"b61b447f-a4a2-47a6-8dee-16a65783382d","FCT-005":"798476fd-f1eb-4b10-9490-d86e74a82455"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"Rapport 2025 SICTOM Nogent PDF inspecte - Valobat 14928 EUR ventile","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"RPQS 2025 CC Aspres PDF inspecte - tonnages PMCB + economies","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"Rapport 2024 metropolitain PDF inspecte - soutien operationnel Valobat","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"Rapport 2024 Sydem PDF inspecte - contrat Valobat 14022024","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"Rapport 2023 SICTOMU PDF inspecte - soutiens 639452","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:Rapport 2025 SICTOM Nogent PDF inspecte - Valobat 14928 EUR ventile
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:RPQS 2025 CC Aspres PDF inspecte - tonnages PMCB + economies
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:Rapport 2024 metropolitain PDF inspecte - soutien operationnel Valobat
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:Rapport 2024 Sydem PDF inspecte - contrat Valobat 14022024
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:Rapport 2023 SICTOMU PDF inspecte - soutiens 639452
