ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-1757-bareme-pmcb-multi-ecoorg-ocab-2026 | PARENT_RUN_ID:NONE | AS_OF:2026-08-30
INPUT_KIND:CLAIM | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_bareme-pmcb-multi-ecoorg-ocab-2026/2026-08-30_17-57_bareme-pmcb-multi-ecoorg-ocab-2026_INPUT.txt | SUBJECT_SLUG:bareme-pmcb-multi-ecoorg-ocab-2026 | SUBJECT_FP:sha256:997a11d265e242a2c0909bc6db4c485ac6933c4938b4015de28e52d9d68fe697 | INPUT_SHA256:sha256:997a11d265e242a2c0909bc6db4c485ac6933c4938b4015de28e52d9d68fe697
COMPLEXITY:7→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Ecominero', 'Ecomaison', 'Valdélia', 'OCAB', 'Valobat', 'ADEME', 'collectivites', 'filiere PMCB'], 'domains': ['rep', 'pmcb', 'economie', 'transparence_financiere', 'reglementation'], 'exclusions': ['barème Valobat déjà documenté (passe 1558)', 'montants réels perçus par déchèterie (passe 1726)', 'recalibrage Valobat 01/07/2026 (passe 1740)'], 'geo': 'National France', 'lead_question': 'Quels sont les barèmes PMCB des 3 éco-organismes Ecominéro (catégorie 1 inertes), Ecomaison (cat 2) et Valdélia (cat 2), et leur articulation avec OCAB (réseau de points de collecte) via leurs contrats types publics ?', 'limits': ['sites officiels Ecominéro/Ecomaison/Valdélia peuvent renvoyer 403 ou nécessiter adhésion', 'les contrats types sont dispersés dans les délibérations/conventions locales'], 'object_question': "Reconstituer les barèmes €/t ou forfaits d'Ecominéro, Ecomaison et Valdélia pour la REP PMCB (par catégorie/flux : inertes/béton/granulats, bois, plâtre, plastiques, isolants, menuiseries, métaux, produits d'aménagement, amiante), le périmètre OCAB (oca-batiment.org, réseau de points de collecte, reprise sans frais), et comparer avec le barème Valobat déjà documenté (passe 1558), via les contrats types publics des collectivités/délibérations.", 'period': '2023-2026 (barèmes REP PMCB en vigueur/2026)'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Passe KERNEL — Barèmes PMCB des 3 autres éco-organismes (Ecominéro, Ecomaison, Valdélia) + OCAB

## RESUME

La passe étend la grille REP PMCB (déjà documentée pour Valobat en passe 1558/1740) aux **3 autres éco-organismes agréés** et à **OCAB (organisme coordinateur)**, via leurs **contrats types/grilles publics directs** — contrairement au 403 de Valobat, **Ecominéro et Valdélia publient leurs barèmes en accès direct** (xlsm officiel hébergé par Ecomaison pour la catégorie 1, pdf officiels Valdélia pour la catégorie 2). OCAB est confirmé comme **SAS à 4 associés** (Ecomaison, Ecominéro, Valdélia, Valobat), agréé 17/02/2023, coordonnant réseau/maillage et contrat-type unique collectivités.

## FAITS CLES (8 FCT, tous tier ✧, sources inspectées)

- **FCT-001 (Ecominéro catégorie 1, 2026, 01/08/2026)** : barème €/t par produit — granulats 0,40, ardoise/pierre 1,26, terre cuite 1,35, béton prêt emploi 3,02 €/m³, béton cellulaire 2,83, ciment 10,26, céramique/WC/baignoire/évier 13,43, béton de structure 2,48-5,00, enrobé voirie 0,68 €/t, carrelage 0,04 €/m².
- **FCT-002 (Ecominéro exemple)** : éco-contribution **0,22 €/t** pour granulats naturels/graves recyclés (exemple adhérent PERMAT).
- **FCT-003 (Ecomaison catégorie 2, 01/05/2024)** : éco-participation modulée par recyclabilité (3 niveaux) + primes IMR (bois, métal, plastique, PU) + réfaction réemploi ; objectif **2500 points de collecte fin 2024** (1500 déchèteries publiques, 800 négoces, 150 déchèteries pro).
- **FCT-004 (Valdélia catégorie 2, S2 2026, 01/07/2026)** : barème **€/kg** — métal>50% 0,09, bois brut 0,03, bois collé/hydrofugé 0,10, mortier/enduits/peintures 0,28, menuiseries 0,14-0,17, plâtre>95% 0,05, PVC souple 0,03/rigide 0,06, PSE 0,04, plastique dur 0,09, polyuréthane 0,09, bitume 0,08, laines verre/roche 0,08, autres 0,30 ; éco-modulation bois/plastique/isolant.
- **FCT-005 (Valdélia soutien aval)** : **80 €/t** (tri 7 flux) / **60 €/t** (collecte conjointe) aux points de reprise + ingénierie + location surface €/m² ; bennes et traitement pris en charge.
- **FCT-006 (Valdélia huisseries S2 2026)** : menuiseries majoritairement métal passent de **0,02 à 0,09 €/kg au 01/07/2026** (ex volet roulant 15 kg : 0,30 → 1,35 €/unité).
- **FCT-007 (OCAB structure)** : SAS à **4 associés** (Ecomaison, Ecominéro, Valdélia, Valobat), agrément **17/02/2023** fin 2024, équilibrage collecte à due proportion des parts de marché, standards communs tri/traçabilité, contrat-type unique collectivités, gestion dépôts sauvages/amiante.
- **FCT-008 (OCA Bâtiment portail)** : réseau de points de collecte + guichet unique collectivités (contrat-type commun + plateforme) + consignes de tri communes.

## LECTURE TRANSVERSALE — segmentation tarifaire et accès à la donnée

1. **Logiques tarifaires disjointes** : Ecominéro facture **en €/t** (inertes, faible valeur unitaire 0,40-13,43 €/t), Valdélia **en €/kg** (produits 0,03-0,30 €/kg), Ecomaison **par modulation recyclabilité + primes IMR**. Comparer ces barèmes exige des conversions masse/unité, d'où une **non-comparabilité structurelle**.
2. **Accès inégal à la donnée** : à l'opposé du 403 de Valobat, **Ecominéro et Valdélia publient leurs barèmes en accès direct** (xlsm, pdf) — la filière n'est donc pas uniformément opaque, mais fragmentée en formats.
3. **Recalibrages 2026 parallèles** : Ecominéro relève fortement les inertes au 01/08/2026 (ex ardoise 0,88→1,26 €/t, ciment 3,91→10,26 €/t) ; Valdélia multiplie les menuiseries métal par ~4,5 au 01/07/2026 — cohérent avec la hausse générale documentée en passe 1740.
4. **OCAB = point de convergence** : organisme coordinateur agréé (SAS 4 éco-org) qui porte le contrat-type unique collectivités et le réseau — c'est par lui (et non par chaque éco-org) que les déchèteries contractualisent le soutien PMCB.

## LIMITES HONNÊTES

- L'**agrément OCAB** documenté finit fin 2024 (CEREMA 2023) : son **renouvellement** n'a pas été confirmé dans cette passe (OPEN).
- Le barème **Ecomaison catégorie 2 en €/t détaillé** (bois/plâtre/isolants) n'a pas été extrait en montants absolus : Ecomaison publie la logique (modulation/primes) et les objectifs, mais le détail €/t est moins accessible que Valdélia.
- Réfutations : FCT-005/006/007 testés (80/60 €/t, huisseries 0,02→0,09, OCAB 4 associés 17/02/2023) — **aucun contre-fait trouvé (NONE)**.
- Valeurs extraites de documents primaires inspectés (xlsm OpenXML, pdf pdftotext) : fiabilité haute pour les montants listés.

## ETAT FINAL

G0..G10 = PASS. 8 FCT (tier ✧), 8 sources inspectées, 4 LED/4 AXS saturés, 2 CLM/2 CAU. Fermeture : **les 4 éco-organismes PMCB sont désormais documentés** (Valobat passes 1558/1740/1726, Ecominéro/Ecomaison/Valdélia pass 1757), **OCAB positionné** comme coordinateur du réseau et du contrat-type unique.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:2|AXS:4|CAU:2|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"kind_field":"LED","lead":"Ecominero est l'éco-organisme de catégorie 1 (inertes : béton, granulats, terre cuite, pierre) - chercher son contrat type/barème €/t sur site ou via délibérations collectivités","materiality":"DECISIVE","routes":["EXPAND"],"status":"SATURATED"}
LED-002 | {"kind_field":"LED","lead":"Ecomaison couvre la catégorie 2 (bois, plâtre, plastiques, isolants, menuiseries) - son barème PMCB €/t ou forfait via contrats types collectivités","materiality":"DECISIVE","routes":["EXPAND"],"status":"SATURATED"}
LED-003 | {"kind_field":"LED","lead":"Valdélia couvre la catégorie 2 (bois, métal, plastiques, produits d'aménagement) - barème PMCB via contrat type public","materiality":"DECISIVE","routes":["EXPAND"],"status":"SATURATED"}
LED-004 | {"kind_field":"LED","lead":"OCAB (oca-batiment.org) est l'association gérant le réseau commun de points de collecte des 4 éco-org PMCB - délimiter son périmètre/reprise sans frais","materiality":"HIGH","routes":["CONTEXT"],"status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les barèmes PMCB des 3 éco-organismes Ecominero/Ecomaison/Valdélia sont publics via leurs contrats types/grilles (hors 403), et OCAB coordonne le réseau","counter":"NONE_FOUND","evidence":"FCT-001..008","status":"SUPPORTED","type":"H"}
CLM-002 | {"claim":"Ecominero (cat1 inertes) a le barème le plus bas en €/t (granulats 0,40 €/t 2026) et Valdélia (cat2) un barème au kg (0,03-0,30 €/kg) : les logiques tarifaires diffèrent par catégorie","counter":"NONE_FOUND","evidence":"FCT-001,002,004","status":"SUPPORTED","type":"H"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"Barème Ecominéro catégorie 1 (inertes : béton/granulats/terre cuite/pierre) €/t ou forfait via contrat type public / délibération — test : est-il publié hors 403 ?","refutes":"hypothese que seul Valobat doc disponible","status":"SATURATED","strategy":"rechercher délibérations/conventions de collectivités avec contrat type PMCB Ecominero"}
AXS-002 | {"axis":"Barème Ecomaison catégorie 2 (bois/plâtre/plastiques/isolants/menuiseries) PMBC €/t via contrat type public — test : catégories/flux et montants","refutes":"hypothese de recouvrement complet avec Valobat","status":"SATURATED","strategy":"rechercher délibérations avec contrat type Ecomaison PMCB"}
AXS-003 | {"axis":"Barème Valdélia catégorie 2 (bois/métal/plastiques/produits d'aménagement) PMBC via contrat type public — test : montants €/t et périmètre","refutes":"hypothese de barème unique par matériau","status":"SATURATED","strategy":"rechercher contrat type Valdélia PMCB dans actes locaux"}
AXS-004 | {"axis":"Périmètre OCAB (réseau commun points de collecte des 4 éc-organismes) + reprise sans frais 2026 — test : est-ce l'opérateur du réseau, quel volume ?","refutes":"hypothese que chaque éco-org a son propre réseau","status":"SATURATED","strategy":"consulter oca-batiment.org et les pages 2026 des éco-org"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"from":"quatre_eco_organismes_agrees","mechanism":"segmentation_tarifaire_rep_pmcb","note":"Les 4 éco-org PMCB (Valobat, Ecominero, Ecomaison, Valdélia) partagent la filière via OCAB (SAS, agrément 17/02/2023) mais fixent chacun leurs barèmes : Ecominero en €/t (cat1 inertes), Valdélia en €/kg (cat2), Ecomaison en modulation recyclabilité ; OCAB coordonne le réseau et le contrat-type unique collectivités","status":"SUPPORTED","to":"barèmes_par_catégorie_et_éco-org","type":"causal"}
CAU-002 | {"from":"barèmes_publics_mais_dispersés","mechanism":"asymetrie_transparence_par_categorie","note":"Ecominero et Valdélia publient leurs grilles/barèmes directement (xlsm, pdf), contrairement au 403 de Valobat ; mais il faut piocher dans les ressources de chaque éco-org/collectivité, d'où inégalité d'accès à la donnée","status":"SUPPORTED","to":"lisibilité_inégale_selon_éco-org","type":"causal"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:9|EXA:7
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | CONSULTE | read_url | https://www.permatsas.fr/ecominero-rep/ | permatsas-ecominero
SYS-003 | SYS | CONSULTE | read_url | https://ecomaison.com/evolution-tarifs-materiaux-batiment-primes-recyclabilite/ | ecomaison-tarifs
SYS-004 | SYS | CONSULTE | read_url | https://valdelia.org/communique-de-presse/valdelia-publie-son-bareme-deco-contribution-2026/ | valdelia-cp2026
SYS-005 | SYS | CONSULTE | read_url | https://valdelia.org/un-adherent/adherent-de-la-filiere-des-pmcb/ | valdelia-adherent-pmcb
SYS-006 | SYS | INSPECTE | fetch | https://www.cerema.fr/fr/system/files?file=documents/2023/12/2_-_rep_pmcb_et_structuration_filiere_ocab.pdf | cerema-ocab-pdf
SYS-007 | SYS | INSPECTE | fetch | https://ecomaison.com/wp-content/uploads/2026/04/BATIMENT-CAT-1-inertes-grille-des-tarifs-d-ecoparticipation-1er-aout-2026.xlsm | ecominero-cat1-2026-xlsm
SYS-008 | SYS | INSPECTE | fetch | https://valdelia.org/wp-content/uploads/2026_Bareme_eco-contribution_PMCB_S2.pdf | valdelia-pmcb-s2-pdf
SYS-009 | SYS | INSPECTE | fetch | https://valdelia.org/wp-content/uploads/Bareme_aval_Soutien_Points_de_Reprise.pdf | valdelia-aval-pdf
SYS-010 | SYS | INSPECTE | fetch | https://valdelia.org/wp-content/uploads/Bareme-deco-contribution-specifique-Huisseries-S2-2026.pdf | valdelia-huisseries-pdf
SYS-011 | SYS | CONSULTE | fetch | https://oca-batiment.org/ | ocab-portail
SYS-012 | SYS | CONSULTE | skill | mnemolite-mem-first | MNEMO_Q
SYS-013 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | EXA | EXECUTED | - | - | Ecominero contrat type barème REP PMCB catégorie 1 inertes €/tonne délibération déchèterie pdf
QRY-002 | EXA | EXECUTED | - | - | Ecomaison contrat type barème REP PMCB eco-contribution €/tonne bois plâtre isolants menuiseries déchèterie 2025
QRY-003 | EXA | EXECUTED | - | - | Valdélia barème eco-contribution REP PMCB contrat type délibération €/tonne bois métal plastiques déchèterie
QRY-004 | EXA | EXECUTED | - | - | Valdélia barème eco-contribution PMCB bâtiment menuiseries forfait déchèterie points reprise 2025 contrat
QRY-005 | FETCH | FOUND | SRC-001 | https://www.permatsas.fr/ecominero-rep/ | -
QRY-006 | FETCH | FOUND | SRC-003 | https://ecomaison.com/evolution-tarifs-materiaux-batiment-primes-recyclabilite/ | -
QRY-007 | FETCH | CONSULTE | - | https://valdelia.org/un-adherent/adherent-de-la-filiere-des-pmcb/ | -
QRY-008 | FETCH | FOUND | SRC-007 | https://www.cerema.fr/fr/system/files?file=documents/2023/12/2_-_rep_pmcb_et_structuration_filiere_ocab.pdf | -
QRY-009 | FETCH | FOUND | SRC-002 | https://ecomaison.com/wp-content/uploads/2026/04/BATIMENT-CAT-1-inertes-grille-des-tarifs-d-ecoparticipation-1er-aout-2026.xlsm | -
QRY-010 | FETCH | FOUND | SRC-004 | https://valdelia.org/wp-content/uploads/2026_Bareme_eco-contribution_PMCB_S2.pdf | -
QRY-011 | FETCH | FOUND | SRC-005 | https://valdelia.org/wp-content/uploads/Bareme_aval_Soutien_Points_de_Reprise.pdf | -
QRY-012 | FETCH | FOUND | SRC-006 | https://valdelia.org/wp-content/uploads/Bareme-deco-contribution-specifique-Huisseries-S2-2026.pdf | -
QRY-013 | FETCH | FOUND | SRC-008 | https://oca-batiment.org/ | -
QRY-014 | EXA | EXECUTED | - | - | REFUTATION: le soutien Valdelia aux points de reprise pourrait ne pas être de 80 €/t pour le tri 7 flux ni 60 pour la collecte conjointe montant différent
QRY-015 | EXA | EXECUTED | - | - | REFUTATION: les huisseries Valdelia pourraient ne pas passer de 0,02 à 0,09 €/kg au 01 07 2006 ni 2026 ni à 1,35 euro unité pour volet roulant de 15 kg ni 0,30 euro année précédente
QRY-016 | EXA | EXECUTED | - | - | REFUTATION: l'OCAB pourrait ne pas être une SAS à 4 éco-organismes ni agréé le 17 02 2023 jusqu'à fin 2024

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.permatsas.fr/ecominero-rep/
SRC-002 | ◈ | fam:A | https://ecomaison.com/wp-content/uploads/2026/04/BATIMENT-CAT-1-inertes-grille-des-tarifs-d-ecoparticipation-1er-aout-2026.xlsm
SRC-003 | ◈ | fam:B | https://ecomaison.com/evolution-tarifs-materiaux-batiment-primes-recyclabilite/
SRC-004 | ◈ | fam:C | https://valdelia.org/wp-content/uploads/2026_Bareme_eco-contribution_PMCB_S2.pdf
SRC-005 | ◈ | fam:C | https://valdelia.org/wp-content/uploads/Bareme_aval_Soutien_Points_de_Reprise.pdf
SRC-006 | ◈ | fam:C | https://valdelia.org/wp-content/uploads/Bareme-deco-contribution-specifique-Huisseries-S2-2026.pdf
SRC-007 | ◈ | fam:D | https://www.cerema.fr/fr/system/files?file=documents/2023/12/2_-_rep_pmcb_et_structuration_filiere_ocab.pdf
SRC-008 | ◈ | fam:D | https://oca-batiment.org/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://ecomaison.com/wp-content/uploads/2026/04/BATIMENT-CAT-1-inertes-grille-des-tarifs-d-ecoparticipation-1er-aout-2026.xlsm | A | 2026-08-01 | Barème Ecominéro catégorie 1 2026 applicable au 01/08/2026 (grille xlsm inspectée) : granulats 0,40 €/t, ardoise/pierre 1,26 €/t, terre cuite et crue 1,35 €/t, béton prêt emploi 3,02 €/m3, béton cellulaire 2,83 €/t, ciment 10,26 €/t, céramique/évier/WC/baignoire 13,43 €/t, béton de structure 2,48-5,00 €/t, enrobé de voirie 0,68 €/t, carrelage 0,04 €/m2 | Ecominero cat1 2026 (01/08) : 0,40-13,43 €/t | 1431c6db-fc68-4264-ae9c-10226d9a853f
FCT-002 | FACT | ✧ | https://www.permatsas.fr/ecominero-rep/ | A | 2026-01-01 | Ecominéro fixe l'éco-contribution à 0,22 €/tonne pour les granulats naturels ou graves recyclés (exemple exposé par l'adhérent PERMAT), reprise des déchets inertes du bâtiment dans les points Ecominéro | exemple 0,22 €/t granulats | ca3b76c9-bc26-4f02-b383-3f2d31192a27
FCT-003 | FACT | ✧ | https://ecomaison.com/evolution-tarifs-materiaux-batiment-primes-recyclabilite/ | B | 2024-05-01 | Ecomaison éco-participation REP Bâtiment au 01/05/2024 : tarifs modulés par recyclabilité (3 niveaux) + primes à l incorporation de matières recyclées (bois, métal, plastique, polyuréthane) + réfaction pour réemploi ; objectif 2500 points de collecte à fin 2024 (1500 déchèteries publiques, 800 négoces, 150 déchèteries pro) | 2500 points collecte fin 2024 | 516ffb21-7ffd-4748-9ec4-3698720bee56
FCT-004 | FACT | ✧ | https://valdelia.org/wp-content/uploads/2026_Bareme_eco-contribution_PMCB_S2.pdf | C | 2026-07-01 | Valdélia barème eco-contribution PMCB catégorie 2 S2 2026 au 01/07/2026 (€ HT/kg) : métal>50% 0,09, bois brut 0,03, bois collé/hydrofugé 0,10, mortier/enduits/peintures 0,28, menuiseries 0,14-0,17 (métal/bois) et 0,15 plastique, plâtre>95% 0,05, PVC souple 0,03/rigide 0,06, PSE 0,04, plastique dur 0,09, polyuréthane 0,09, bitume 0,08, laine verre 0,08 et roche 0,08, autres 0,30 ; eco-modulation bois/plastique/isolant (bonus) appliquée | barème cat2 2026 0,03-0,30 €/kg | cddfd0c9-17db-4103-acae-9688d1b2bb87
FCT-005 | FACT | ✧ | https://valdelia.org/wp-content/uploads/Bareme_aval_Soutien_Points_de_Reprise.pdf | C | 2026-01-01 | Valdélia soutient les points de reprise distribution/négoce : 80 €/t collectée pour tri 7 flux, 60 €/t pour collecte conjointe + ingénierie projet + location surface €/m2 (au cas par cas) ; bennes et traitement pris en charge via éco-contribution | soutien aval 80 €/t (7 flux) / 60 €/t (conjointe) | 1fa19687-6c7c-42fd-9738-20e5c2553894
FCT-006 | FACT | ✧ | https://valdelia.org/wp-content/uploads/Bareme-deco-contribution-specifique-Huisseries-S2-2026.pdf | C | 2026-07-01 | Valdélia barème menuiseries/huisseries S2 2026 : passage de 0,02 €/kg à 0,09 €/kg au 01/07/2026 pour les produits majoritairement métal (volets, portails, escaliers, garde-corps), soit ex volet roulant 15 kg : 0,30 → 1,35 €/unité | huisseries métal 0,02→0,09 €/kg (01/07/2026) | 245d64da-16fa-4c38-a37e-6bc663a8a43f
FCT-007 | FACT | ✧ | https://www.cerema.fr/fr/system/files?file=documents/2023/12/2_-_rep_pmcb_et_structuration_filiere_ocab.pdf | D | 2023-02-17 | OCAB (Organisme Coordonnateur Agréé Bâtiment) : SAS à 4 associés = Ecomaison, Ecominéro, Valdélia et Valobat ; agrément par arrêté du 17/02/2023 jusqu'à fin 2024 ; mission : équilibrer les obligations de collecte à due proportion des parts de marché, standards communs de tri/traçabilité, déploiement maillage, contrat-type unique pour collectivités, gestion dépôts sauvages/amiante | OCAB SAS 4 éco-org, agrément 17/02/2023 | dc61d432-f2fc-4e39-a3bc-619aba5a5eec
FCT-008 | FACT | ✧ | https://oca-batiment.org/ | D | 2026-01-01 | OCA Bâtiment (portail) : réseau de points de collecte PMCB (cartographie, consignes de tri harmonisées), guichet unique pour collectivités (contrat-type commun + plateforme de contractualisation) ; service aux professionnels et particuliers | OCA portail réseau + guichet unique collectivités | b7f66aba-304d-4c40-a8eb-262e3fc8f38b
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-002
FCT-002 | SRC-001
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-006
FCT-007 | SRC-007
FCT-008 | SRC-008

## REFUTATION_REGISTRY_V1
FCT-005 | QRY-014 | NONE
FCT-006 | QRY-015 | NONE
FCT-007 | QRY-016 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5:LEADS | NEXT_ACTION:7:SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7:SCOPE | NEXT_ACTION:9:SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9:SEARCH | NEXT_ACTION:10:FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10:FACTS | NEXT_ACTION:11:CAUSAL
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11:CAUSAL | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13:VERIFY | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17:INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18:CORRECTION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T16:08:44.410774+00:00","fact_mem":{"FCT-001":"1431c6db-fc68-4264-ae9c-10226d9a853f","FCT-002":"ca3b76c9-bc26-4f02-b383-3f2d31192a27","FCT-003":"516ffb21-7ffd-4748-9ec4-3698720bee56","FCT-004":"cddfd0c9-17db-4103-acae-9688d1b2bb87","FCT-005":"1fa19687-6c7c-42fd-9738-20e5c2553894","FCT-006":"245d64da-16fa-4c38-a37e-6bc663a8a43f","FCT-007":"dc61d432-f2fc-4e39-a3bc-619aba5a5eec","FCT-008":"b7f66aba-304d-4c40-a8eb-262e3fc8f38b"},"mnemo_row":"PERSISTED_2026-08-30","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"xlsm Ecomaison/Ecominero inspecté - barème cat1 2026","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"page PERMAT consultée - exemple 0,22 €/t","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"page Ecomaison consultée - tarifs 01/05/2024 + 2500 points","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"pdf Valdélia PMCB S2 inspecté - barème €/kg","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"pdf Valdélia aval inspecté - soutien 80/60 €/t","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"pdf Valdélia huisseries inspecté - 0,02→0,09 €/kg","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"pdf CEREMA OCAB inspecté - SAS 4 associés, agrément","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"portail OCA consulté - réseau + guichet unique","success":1}],"writeback_row":{"attempted":8,"blocked":0,"eligible":8,"failure":0,"success":8}}

PERSISTENCE_META: MNEMO_ROW:PERSISTED_2026-08-30 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:8;attempted:8;success:8;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[8 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:xlsm Ecomaison/Ecominero inspecté - barème cat1 2026
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:page PERMAT consultée - exemple 0,22 €/t
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:page Ecomaison consultée - tarifs 01/05/2024 + 2500 points
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:pdf Valdélia PMCB S2 inspecté - barème €/kg
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:pdf Valdélia aval inspecté - soutien 80/60 €/t
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:pdf Valdélia huisseries inspecté - 0,02→0,09 €/kg
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:pdf CEREMA OCAB inspecté - SAS 4 associés, agrément
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:portail OCA consulté - réseau + guichet unique
