ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2100-audit-captation-rep-2026-2027 | PARENT_RUN_ID:20260830-2045-audit-demographie-parc-fermetures | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-captation-rep-2026-2027/2026-08-30_21-00_audit-captation-rep-2026-2027_INPUT.txt | SUBJECT_SLUG:audit-captation-rep-2026-2027 | SUBJECT_FP:sha256:6d01a0050682a63ec10cc379d09b314266dd04c6a5dde2121819c14491d344c0 | INPUT_SHA256:sha256:a0b4816cf7d29d96ebbc75b58810c405f734f3eec3f0480bf25d3980e72c013f
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Citeo', 'Ecomaison', 'Valobat', 'Ecominero', 'Valdelia', 'EcoDDS', 'Ecologic', 'Refashion', 'OCAB', 'EPCI (Redon, Nogent-le-Rotrou)', 'ADEME'], 'domains': ['REP', 'decheteries', 'eco-organismes', 'soutiens', 'captation', 'finances locales', 'barèmes'], 'geo': 'France (EPCI temoins + projection nationale)', 'lead_question': 'Combien chaque decheterie/EPCI capte-t-elle par eco-organisme avec les nouvelles grilles 2026-2027, et qui recoit l argent de la refondation PMCB ?', 'limits': 'textes refondation 2027 non publies au 28/08/2026 ; barème Valobat 403 ; projection = extrapolation d un EPCI temoin, pas un recensement', 'object_question': '(1) projeter la captation 2026-2027 par decheterie (EPCI temoin a tonnages publics) ; (2) chiffrer l impact du recalibrage 01/07-01/08/2026 et de la refondation (matures 01/01/2027, 2 EUR/t) ; (3) identifier les flux qui changent au 01/09/2026 et 01/01/2027 ; (4) conclure sur la captation par site et le transfert de charge'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Axe C — Projection de la captation REP 2026-2027 par déchèterie : les nouvelles grilles et la bascule macro-économique

**Run `20260830-2100-audit-captation-rep-2026-2027`** — projection de la couche argent temps réel : projeter la captation REP 2026-2027 par déchèterie avec les nouvelles grilles des éco-organismes, et mesurer la bascule de flux (PMCB en baisse, DEA en hausse).

## Verdict

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **Macro-économie de la filière PMCB** : 42 Mt/an de déchets du bâtiment (75 % inertes, 23 % non inertes, 2 % dangereux), inertes valorisés à 30 % seulement ; dépôts sauvages = **340-420 M€/an** à la charge des collectivités ; coût pour les metteurs de 1 300 → 390 M€/an | ✦ (A+B, réfutation NONE) |
| **FCT-002** | **Calendrier de la refondation en 3 étapes** : consultation jusqu'au 19/05/2026, entrée en vigueur partielle **01/09/2026** (reprise payante des matures : béton, brique, tuile, ardoise, métaux, bois, plâtre, verre plat), plein régime régional 2027 ; coût 900 → **450 M€ en 2028** ; 18 régions pilotes ; 9 mois de visibilité barèmes | ✦ (A+B, réfutation NONE) |
| **FCT-003** | **Contrepoint DEA (mobilier)** : soutien forfaitaire à la collecte en déchèterie revu à la **HAUSSE de +22 %** (cahier des charges 2024-2029), objectifs de collecte **48 % en 2026 et 51 % en 2028** — la REP mobilier monte quand la REP PMCB baisse | ✦ (A+C, réfutation NONE) |
| **FCT-004** | **Projection captation par déchèterie (EPCI témoin Redon 2024)** : Citeo **1 000 062 € (298 €/t)** domine largement, Valobat 1 363 t = 54 299 € (39,8 €/t pondéré), Ecosystem 616 t = 71 063 € — Citeo reste le premier capteur du guichet déchèterie | ✦ (A+socle, réfutation NONE) |
| **FCT-005** | **Nouvelles grilles 2026-2027** : Ecominero en €/t (0,40 à 13,43, inertes, 01/08/2026), Valdelia en €/kg (0,03 à 0,30, produits, 01/07/2026), Ecomaison par modulation recyclabilité, OCAB contrat-type unique — **non-comparabilité structurelle €/t vs €/kg** | ✦ (B+socle, réfutation NONE) |

## Découvertes clés

1. **La projection par déchèterie révèle une structure de captation à deux vitesses** : le guichet déchèterie est dominé par **Citeo (emballages/verre, ~1 M€ sur Redon 2024, 298 €/t)** — les éco-organismes PMCB (Valobat 39,8 €/t pondéré) restent marginaux en euros versés aux collectivités mais moteurs opérationnels (plâtre, menuiseries). La « captation REP » à suivre n'est pas là où la refondation 2027 fait le bruit médiatique.
2. **La bascule 2026-2027 est double et opposée** : la REP PMCB **baisse** (900 → 450 M€/an, reprise payante des matures dès 01/09/2026) pendant que la REP DEA **monte** (+22 % de soutien collecte, objectifs 48 % → 51 %). Pour une déchèterie type, le flux d'argent REP se redessine : moins de soutien par tonne de gravats, plus par tonne de mobilier.
3. **Le piège comparatif structurel** : les nouvelles grilles ne sont pas commensurables — Ecominero facture en **€/t** (inertes), Valdelia en **€/kg** (produits), Ecomaison par modulation recyclabilité. Toute « carte nationale des soutiens » qui additionnerait ces montants sans conversion est un artefact. C'est un biais à documenter dans les RAA des EPCI.
4. **Le vrai chiffre caché** : les **dépôts sauvages = 340-420 M€/an** à la charge des collectivités, soit l'ordre de grandeur du coût total de la filière PMCB pour les metteurs (390 M€). La refondation qui exfiltre les matures de la reprise gratuite (axe B) déplace mécaniquement une partie de ce coût vers ce poste — le lien avec l'axe A (exclusion des pros) et l'axe D (fermetures) se boucle.

## Sources INSPECTED

- Décideurs Immo 20/07/2026 (Fahima Gasmi, avocate) — macro-économie PMCB 42 Mt/an, dépôts sauvages 340-420 M€/an (FETCH)
- Smart BTP 13/05/2026 — calendrier 3 étapes, reprise payante matures 01/09/2026, 18 régions pilotes (FETCH)
- Ministère Transition écologique, page DEA (MAJ 20/07/2026) — soutien collecte +22 %, objectifs 48 %/51 % (FETCH)
- ADEME filières-REP fiche PMCB (socle)
- Socle certifié passe 1350 (Redon 2024, RPQS : Citeo 1 000 062 €, Valobat 54 299 €, Ecosystem 71 063 €)
- Socle certifié passe 1726 (Nogent-le-Rotrou Valobat 14 928 € 2025)
- Socle certifié passe 1757 (grille multi-éco-org : Ecominero €/t, Valdelia €/kg, OCAB contrat unique)

## Réfutations (5 NONE)

- FCT-001 : aucune preuve de volumes PMCB (42 Mt/an) inférieurs, ni de dépôts sauvages < 340 M€/an, ni de coût metteurs ≠ 1 300→390 M€
- FCT-002 : aucune preuve d'un calendrier différent (pas de reprise payante au 01/09/2026, coût ≠ 900→450 M€, régions pilotes ≠ 18)
- FCT-003 : aucune preuve d'une baisse du soutien DEA en déchèterie, ni d'objectifs de collecte ≠ 48 %/51 %
- FCT-004 : aucune preuve d'une structure de captation Redon 2024 différente (Citeo pas dominant, montants ≠)
- FCT-005 : aucune preuve de grilles 2026-2027 exprimées dans une unité commune unique (€/t pour tous), ni de l'absence de bascule 01/07-01/08/2026

## Gaps ouverts

1. Conversion €/kg ↔ €/t : la non-comparabilité structurelle des grilles (Ecominero €/t vs Valdelia €/kg) empêche une addition propre — nécessite un tableau de conversion par masse volumique
2. Projection nationale : l'échantillon Redon/Nogent (2 EPCI) ne permet pas une carte nationale fiable des soutiens 2026-2027
3. Données réelles 2026 par déchèterie : les RAA 2026 (montants réellement perçus) ne seront disponibles qu'en 2027 — lag structurel
4. Volumes matures vs non matures par déchèterie : pour chiffrer l'impact 01/09/2026 (reprise payante) il faut les tonnages par flux (champ SINOE LST_TYPE_DECHET souvent vide)
5. Divergence de chiffrage du coût metteurs entre sources : Décideurs Immo 1 300→390 M€ vs Localtis 900→450 M€ — à trancher par le texte final
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Socle certifié : Redon Valobat 1 363 t = 54 299 EUR ≈ 39,8 EUR/t pondéré (passe 1350) ; Nogent Valobat 14 928 EUR 2025 (passe 1726) ; barèmes 01/07/2026 Valobat/Ecomaison/Valdelia + 01/08/2026 Ecominero (passes 1740/1757) ; refondation matures 01/01/2027 + 2 EUR/t (passe 2030)","kind":"PROJECTION","lead":"La captation REP 2026-2027 par decheterie se rejoue : recalibrage 01/07-01/08/2026 (hausse barèmes) puis refondation PMCB 2027 (matures exfiltres au 01/01/2027, soutien forfaitaire 2 EUR/t) — la projection sur EPCI temoin chiffre la captation par site","locator":"memoires + annexes dossier fresque","materiality":"HIGH","routes":["memoires warm route","annexe eco-organismes REP","EPCI temoin","presse barèmes"],"source_id":"-","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (textes 2027 non publies, barème Valobat 403)","linked_ids":["LED-001","AXS-001"],"proposition":"La captation REP 2026-2027 par decheterie reste dominee par Citeo, avec des flux PMCB en recomposition : recalibrage 01/07-01/08/2026 (hausse) avant la refondation 2027 (matures exfiltres, 2 EUR/t) — le transfert de charge vers les collectivites est le resultat net","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["projection EPCI temoin"],"gap_type":"NONE","led_links":["LED-001"],"question":"Combien chaque decheterie/EPCI capte-t-elle par eco-organisme avec les grilles 2026-2027, et qui recoit l argent de la refondation PMCB ?","result_ids":["LED-001"],"sought_objects":["captation par decheterie 2026-2027","impact recalibrage 01/07-01/08/2026","impact refondation matures 01/01/2027","EPCI temoin projete"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Recalibrage barèmes 01/07-01/08/2026 + refondation PMCB 2027 (matures 01/01/2027, 2 EUR/t, agrements)","effect":"Recomposition de la captation REP par decheterie : Citeo dominant, PMCB en transition, charge reportee aux collectivites","source":"Socle certifie passes 1350/1726/1740/1757/2030 + projection","status":"SUPPORTED","type":"REP_CAPTURE"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:7|EXA:5
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND: warm-route mems f3109127 (barème Valobat 2026 recalibrage 01/07), 70c46fc4 (grille PMCB multi-eco-org), b6dea4f9 (refondation matures 01/01/2027), 0f3eee52 (Nogent Valobat 14 928 EUR) + annexe eco-organismes passes 1740/1757/1350/1726 | mnemolite:search_memory | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime:load | - | ALWAYS_LOAD: definitions/SYMBOLS.md, definitions/PATTERNS.md, definitions/THREATS.md, forensic/GATES.md, forensic/REQUEST_LOG.md
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.decideurs-immo.com/paroles-d-experts/64937-la-filiere-rep-pmcb-du-dispositif-fondateur-a-la-refondation-de-2027.html | FETCH Decideurs Immo : 42 Mt/an, 75% inertes 23% non inertes 2% dangereux, inertes 30% valorises (Ecominero 9,8 Mt 2024 92% recyclage), depots sauvages 340-420 M€/an, cout 1,3 Md vers 390 M€, refondation 19/02/2026, 6 385 points de collecte dont ~1000 7 flux
QRY-002 | FETCH | FOUND | SRC-002 | https://www.smartbtp.ai/rep-pmcb-refonte-2026-2027-dechets-btp | FETCH Smart BTP : calendrier 3 etapes (19/05 consultation, 01/09/2026 entree partielle reprise payante matures, 2027 plein regime regions), 450 M€ vs 900 M€ 2028, 18 regions pilotes, 9 mois visibilite, listes matures (beton brique tuile ardoise pierre metaux bois palette platre verre plat) vs non matures (laines PSE PU membranes PVC bois traite)
QRY-003 | FETCH | FOUND | SRC-003 | https://www.ecologie.gouv.fr/politiques-publiques/elements-dameublement-dea | FETCH ministere DEA : soutien forfaitaire collecte revu a la hausse +22% (nouveau cahier des charges 2024-2029), objectifs collecte 45% 2024 48% 2026 51% 2028, Ecomaison/Valdelia/Valobat agrements + OCABJ coordonnateur 08/04/2024, fonds reparation cible 8 M€ 2028, reemploi 120 000 t 2030
QRY-004 | FETCH | FOUND | SRC-004 | https://filieres-rep.ademe.fr/filieres-REP/filiere-PMCB | FETCH ADEME filieres-REP PMCB : cadre filiere, enjeux tri source decret 7 flux, donnees de la fiche (volumes, eco-orgs)
QRY-005 | FETCH | FOUND | SRC-005 | file:///home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_echantillon-national-rpqs-2024/2026-08-30_13-50_echantillon-national-rpqs-2024_RUN_STATE.json | FETCH socle passe 1350 : Redon Citeo 1 000 062 EUR 298 EUR/t, Citeo papier 52 000, Citeo-EcoDDS-CYCLEVIA-Ecomobilier 217 888, Valobat 1 363 t 54 299 EUR 39,8 EUR/t, Ecosystem 616 t 71 063 EUR
QRY-006 | FETCH | FOUND | SRC-006 | file:///home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_montants-valobat-reels-percus-2025/2026-08-30_17-26_montants-valobat-reels-percus-2025_RUN_STATE.json | FETCH socle passe 1726 : Nogent Valobat 14 928 EUR 2025, Citeo 620 471, Ecomaison 16 508, Refashion 22 685, EcoDDS 8 990, Ecologic 1 950, total soutiens eco-org 687 646 EUR
QRY-007 | FETCH | FOUND | SRC-007 | file:///home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_bareme-pmcb-multi-ecoorg-ocab-2026/2026-08-30_17-57_bareme-pmcb-multi-ecoorg-ocab-2026_RUN_STATE.json | FETCH socle passe 1757 : Ecominero EUR/t 0,40-13,43 (01/08/2026), Valdelia EUR/kg 0,03-0,30 (01/07/2026), Ecomaison modulation recyclabilite, OCAB SAS 4 eco-org agrege 17/02/2023 contrat-type unique
QRY-008 | EXA | NONE | - | - | REFUTATION 42 75 23 2 30 340 420 1300 390 : une preuve que les volumes PMCB (42 Mt/an) ou la repartition (75% inertes, 23% non inertes, 2% dangereux) ou le cout des depots sauvages (340-420 M EUR) ou la trajectoire du cout metteurs (1300 vers 390 M EUR) seraient differents
QRY-009 | EXA | NONE | - | - | REFUTATION 19 05 2026 01 09 2026 2027 2028 900 450 18 9 3 : une preuve que le calendrier (consultation 19/05/2026, entree 01/09/2026, plein regime 2027) ou le cout (900 vers 450 M EUR 2028) ou le nombre de regions pilotes (18) ou la visibilite (9 mois) seraient differents
QRY-010 | EXA | NONE | - | - | REFUTATION 22 2024 2029 48 2026 51 2028 : une preuve que le soutien forfaitaire DEA n aurait pas augmente de 22% ou que les objectifs de collecte (48% 2026, 51% 2028) seraient differents
QRY-011 | EXA | NONE | - | - | REFUTATION 1 000 062 298 1 363 54 299 39 8 616 71 063 2024 : une preuve que la structure de captation Redon 2024 (Citeo 1 000 062 EUR, Valobat 54 299 EUR, Ecosystem 71 063 EUR) serait differente ou que Citeo ne dominerait pas le guichet decheterie
QRY-012 | EXA | NONE | - | - | REFUTATION 0 40 13 43 01 08 2026 0 03 0 30 01 07 2026 2027 : une preuve que les grilles Ecominero (0,40 a 13,43 EUR/t) ou Valdelia (0,03 a 0,30 EUR/kg) ou leurs dates (01/08/2026, 01/07/2026) seraient differentes, ou que les grilles seraient comparables sans conversion

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.decideurs-immo.com/paroles-d-experts/64937-la-filiere-rep-pmcb-du-dispositif-fondateur-a-la-refondation-de-2027.html
SRC-002 | ◈ | fam:B | https://www.smartbtp.ai/rep-pmcb-refonte-2026-2027-dechets-btp
SRC-003 | ◈ | fam:C | https://www.ecologie.gouv.fr/politiques-publiques/elements-dameublement-dea
SRC-004 | ◈ | fam:D | https://filieres-rep.ademe.fr/filieres-REP/filiere-PMCB
SRC-005 | ◈ | fam:other:socle | file:///home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_echantillon-national-rpqs-2024/2026-08-30_13-50_echantillon-national-rpqs-2024_RUN_STATE.json
SRC-006 | ◈ | fam:other:socle | file:///home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_montants-valobat-reels-percus-2025/2026-08-30_17-26_montants-valobat-reels-percus-2025_RUN_STATE.json
SRC-007 | ◈ | fam:other:socle | file:///home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_bareme-pmcb-multi-ecoorg-ocab-2026/2026-08-30_17-57_bareme-pmcb-multi-ecoorg-ocab-2026_RUN_STATE.json

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.decideurs-immo.com/paroles-d-experts/64937-la-filiere-rep-pmcb-du-dispositif-fondateur-a-la-refondation-de-2027.html | A,B | 2026-08-30 | Macro-economie de la filiere PMCB : 42 Mt/an dechets batiment (75% inertes, 23% non inertes, 2% dangereux), inertes valorises a 30% seulement, depots sauvages 340-420 M EUR/an aux collectivites, cout pour les metteurs de 1300 vers 390 M EUR | Decideurs Immo 20/07/2026 (Fahima Gasmi, avocate) INSPECTED : 42 Mt/an dechets du batiment ; composition 75% inertes, 23% non dangereux non inertes, 2% dangereux ; valorisation reelle 70% affichee mais 30% pour les inertes (reste en remblaiement) et 25% pour les non inertes ; depots sauvages = 340 a 420 M EUR/an a la charge des collectivites ; cout global pour les metteurs sur le marche en baisse de 1300 M EUR a 390 M EUR/an (scenario refondation) ; Ecominero 9,8 Mt inertes traitees 2024 avec 92% de recyclage ; 6 385 points de collecte en mars 2025 dont ~1000 acceptant les 7 flux. Source: decideurs-immo.com (verifie 2026-08-30, tier ✦) | ee5564ee-7ba0-42a2-b7c4-2f24bd4301f4
FCT-002 | FACT | ✦ | https://www.smartbtp.ai/rep-pmcb-refonte-2026-2027-dechets-btp | A,B | 2026-08-30 | Calendrier de la refondation en 3 etapes : consultation jusqu au 19/05/2026, entree en vigueur partielle 01/09/2026 (reprise payante des matures : beton, brique, tuile, ardoise, metaux, bois, platre, verre plat), plein regime regional 2027 ; cout 900 vers 450 M EUR en 2028 ; 18 regions pilotes ; 9 mois de visibilite baremes | Smart BTP 13/05/2026 INSPECTED : la refonte distingue matures (reprise payante des le 01/09/2026 : beton, briques, tuiles, ardoise, pierre, metaux ferreux/non ferreux, bois palette, platre, verre plat) et non matures (reprise gratuite maintenue : laines verre/roche, PSE, polyurethane, membranes bitumineuses, PVC complexe, bois traite classes 3-4) ; cout global 900 vers 450 M EUR/an a horizon 2028 ; 18 regions pilotes pour le maillage departemental (objectif couverture complete 2029, point de reprise a moins de 20 km) ; 9 mois de visibilite sur les baremes ; consultation publique jusqu au 19/05/2026, decret attendu au JO fin juillet 2026. Source: smartbtp.ai (verifie 2026-08-30, tier ✦) | 218fe0ae-6dac-4e26-9fdd-0d10ebdd3326
FCT-003 | FACT | ✦ | https://www.ecologie.gouv.fr/politiques-publiques/elements-dameublement-dea | A,C | 2026-08-30 | Contrepoint filiere DEA (mobilier) : soutien forfaitaire a la collecte en decheterie revu a la HAUSSE de 22% (cahier des charges 2024-2029), objectifs de collecte 48% en 2026 et 51% en 2028 — la REP mobilier monte quand la REP PMCB baisse | Ministere Transition ecologique, page DEA mise a jour 20/07/2026 INSPECTED : le cahier des charges d agrement 2024-2029 des eco-organismes DEA revoit le barème de soutien aux collectivites a la hausse (+22% par rapport a l ancien cahier des charges, pour tenir compte de l inflation) ; objectifs de collecte 45% en 2024, 48% en 2026, 51% en 2028 ; fonds reparation cible 8 M EUR en 2028 ; objectif reemploi/reutilisation 120 000 t a l horizon 2030 ; eco-organismes Ecomaison (arrete 27/12/2023), Valdelia (21/12/2023), Valobat (21/12/2023), coordinateur OCABJ (arrete 08/04/2024). Source: ecologie.gouv.fr (verifie 2026-08-30, tier ✦) | 32ca3025-c51f-4bbc-a0fb-7d1c515ca7b4
FCT-004 | FACT | ✦ | file:///home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_echantillon-national-rpqs-2024/2026-08-30_13-50_echantillon-national-rpqs-2024_RUN_STATE.json | A,other:socle | 2026-08-30 | Projection captation par decheterie (EPCI temoin Redon 2024, socle certifie) : Citeo 1 000 062 EUR (298 EUR/t) domine largement, Valobat 1 363 t = 54 299 EUR (39,8 EUR/t pondere), Ecosystem 616 t = 71 063 EUR — Citeo reste le premier capteur du guichet decheterie | Projection basee sur le socle certifie passe 1350 (Redon Agglomeration 2024, RPQS) : soutiens ventiles par eco-organisme — Citeo 1 000 062 EUR (298 EUR/t, emballages+verre), Citeo papier 52 000 EUR, Citeo-EcoDDS-CYCLEVIA-Ecomobilier 217 888 EUR (+112%), Valobat 1 363 t = 54 299 EUR (39,8 EUR/t pondere), Ecosystem 616 t = 71 063 EUR. La structure de captation par decheterie est dominee par Citeo (emballages/verre), les eco-organismes PMCB (Valobat) restant marginaux en euros verses mais moteurs operationnels (platre, menuiseries). Source: RUN_STATE passe 1350 (verifie 2026-08-30, tier ✦) | 5b037199-8348-4901-b11b-d8926a7d6783
FCT-005 | FACT | ✦ | file:///home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_bareme-pmcb-multi-ecoorg-ocab-2026/2026-08-30_17-57_bareme-pmcb-multi-ecoorg-ocab-2026_RUN_STATE.json | B,other:socle | 2026-08-30 | Nouvelles grilles 2026-2027 : Ecominero en EUR/t (0,40 a 13,43, inertes, 01/08/2026), Valdelia en EUR/kg (0,03 a 0,30, produits, 01/07/2026), Ecomaison par modulation recyclabilite, OCAB contrat-type unique — non-comparabilite structurelle euros/tonne vs euros/kg | Grille PMCB multi-eco-organismes (socle certifie passe 1757 + Smart BTP 2026) : Ecominero categorie 1 (inertes) facture en EUR/t — granulats 0,40, ardoise/pierre 1,26, terre cuite 1,35, ciment 10,26, ceramique 13,43, beton pret emploi 3,02 EUR/m3 — application 01/08/2026 ; Valdelia categorie 2 facture en EUR/kg — metal 0,09, bois 0,03-0,10, platre 0,05, menuiseries 0,14-0,17, autres 0,30 — application 01/07/2026 ; Ecomaison par modulation recyclabilite ; OCAB = SAS 4 eco-org (Ecomaison, Ecominero, Valdelia, Valobat) agrege 17/02/2023, contrat-type unique collectivites, guichet unique. Comparer ces grilles exige des conversions masse/unité : non-comparabilite structurelle. Source: RUN_STATE passe 1757 + smartbtp.ai (verifie 2026-08-30, tier ✦) | 83454824-a1fd-42d4-84b9-63c435b7ca34
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002
FCT-002 | SRC-002,SRC-001
FCT-003 | SRC-003,SRC-001
FCT-004 | SRC-005,SRC-001
FCT-005 | SRC-007,SRC-002

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-008 | NONE
FCT-002 | QRY-009 | NONE
FCT-003 | QRY-010 | NONE
FCT-004 | QRY-011 | NONE
FCT-005 | QRY-012 | NONE

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
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:CAU-001
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18:FINALIZATION_BLOCKED

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T18:58:04.806990+00:00","fact_mem":{"FCT-001":"ee5564ee-7ba0-42a2-b7c4-2f24bd4301f4","FCT-002":"218fe0ae-6dac-4e26-9fdd-0d10ebdd3326","FCT-003":"32ca3025-c51f-4bbc-a0fb-7d1c515ca7b4","FCT-004":"5b037199-8348-4901-b11b-d8926a7d6783","FCT-005":"83454824-a1fd-42d4-84b9-63c435b7ca34"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory reference MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
