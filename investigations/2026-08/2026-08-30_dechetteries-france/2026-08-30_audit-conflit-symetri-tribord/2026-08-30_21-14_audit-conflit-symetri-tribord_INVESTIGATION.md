ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2114-audit-conflit-symetri-tribord | PARENT_RUN_ID:20260830-2103-audit-decheterie-dispositif-controle-2026 | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-conflit-symetri-tribord/2026-08-30_21-14_audit-conflit-symetri-tribord_INPUT.txt | SUBJECT_SLUG:audit-conflit-symetri-tribord | SUBJECT_FP:sha256:47782bc1677cdd548ae764e1b6f59485bec04214187fb652530b1818c7a9115b | INPUT_SHA256:sha256:11ba2df3df32054f5d0efcf02e22dfb33da27fab58f6dfafe583fd2a1187e28d
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Symetri (841351901)', 'TRIBORD (378801682)', 'Rennes Metropole', 'editeurs concurrence (Horanet, Gesbac, SeeTech, SIGRENEA-Suez, MyRFIDSolution, Sensoneo)', 'EPCI acheteurs', 'acheteurs publics (DAJ)'], 'domains': ['dechets', 'decheteries', 'controle-acces', 'marches-publics', 'conflit-interets', 'gouvernance', 'marchandisation'], 'geo': 'France (Rennes Metropole + echantillon national marches publics)', 'lead_question': "Le fournisseur du compteur (Symetri) est-il aussi l'exploitant des sites comptes (TRIBORD) sur les memes territoires — conflit d'interets structurel documentable par les marches publics ?", 'limits': 'donnees marches publics dispersees (BOAMP, DossiersGagnants, TED), montants parfois non publies, parts de marche non publiees par les editeurs', 'object_question': "(1) lien capitalistique/operationnel exact Symetri-TRIBORD ; (2) marches publics : contrats exploitation Rennes Metropole + marches controle d'acces Symetri ; (3) parts de marche editeurs ; (4) evaluation du conflit d'interets"}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Audit du conflit d'intérêts Symetri/TRIBORD : l'éditeur du compteur est la filiale de l'exploitant des sites

**Run `20260830-2114-audit-conflit-symetri-tribord`** — audit des marchés publics, des contrats d'exploitation des déchèteries de Rennes Métropole et de la structure capitalistique Symetri/TRIBORD.

## Verdict

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **Lien capitalistique avéré** : Symetri (SASU créée 26/07/2018, capital 601 450 €) = **ancien département numérique de Tribord filialisé en 2018** (chronologie officielle e-tribord.com) ; TRIBORD exploite les déchèteries de Rennes Métropole **depuis 2002** (14 → 25 sites) ; profil LinkedIn (10/2025-05/2026) : « Gestion des flux de déchets avec l'ERP édité par Symetri » chez Tribord | ✦ (A+D, réfutation NONE) |
| **FCT-002** | **TRIBORD = 25 marchés publics, 64,1 M€ cumulés (2020-2026)** dont **RENNES METROPOLE 1 marché à 21 M€** (15/05/2025, procédure avec négociation) pour l'exploitation du réseau de déchèteries — contrat incluant explicitement **« le contrôle d'accès et l'accueil des usagers »** + clause de performance pour le contrôle des non-ménagers ; démarrage 01/10/2025 pour 5 ans (17 agents valoristes recrutés) | ✦ (A+B, réfutation NONE) |
| **FCT-003** | **NUANCE : Rennes Métropole n'a PAS confié son contrôle d'accès à Symetri** — carte **KorriGo Services** (marché fourniture cartes, clôture 01/07/2024) + logiciel **Gesbac NETVLM/GIDED** ; mise en œuvre retardée (« calendrier non stabilisé », 20minutes 11/10/2025) → **le conflit est INDIRECT** (TRIBORD exploite + utilise l'ERP Symetri en interne), pas un marché Symetri chez Rennes | ✦ (C+D, réfutation NONE) |
| **FCT-004** | **Marchés publics Symetri = 4 marchés, 440 k€ cumulés** : ARCHE Agglo 2 marchés 226 k€ (13/08/2026), **SITREVA 1 marché 214 k€ (22/09/2022) passé SANS PUBLICITÉ NI MISE EN CONCURRENCE PRÉALABLE**, Saint-Brieuc 1 marché (montant non renseigné) ; 2 contrats en cours, échéance 16/10/2027 | ✦ (B+E, réfutation NONE) |
| **FCT-005** | **Contexte du marché (Bretagne)** : Smictom Valcobreizh débourse **~200 000 €** (cartes, logiciel, barrières, badge obligatoire 01/11/2025, 90 000 habitants, marché 11/10/2024 : **51 000 cartes RFID** 13,56) ; Fougères contrôle depuis 10 ans ; **Janzé 18 passages/an** ; crainte dépôts sauvages/report OMr documentée ; Rennes : 18 déchèteries + 6 plateformes, KorriGo annoncé 2024 non déployé | ✦ (C+D, réfutation NONE) |

## Découvertes clés

1. **Le conflit d'intérêts est RÉEL, STRUCTUREL mais INDIRECT.** La chaîne capitalistique est avérée et documentée par la chronologie officielle : Symetri = ancien département numérique de TRIBORD, filialisé en 2018. L'éditeur du compteur est la fille de l'exploitant des sites. Et TRIBORD exploite les déchèteries de Rennes Métropole **depuis 2002**, avec un contrat de 21 M€ renouvelé en 2025 qui inclut le contrôle d'accès.
2. **La nuance honnête** : sur Rennes Métropole — le principal contrat de TRIBORD — le contrôle d'accès n'est PAS fourni par Symetri mais par **Gesbac + cartes KorriGo**. Le conflit opérationnel direct (marché Symetri chez Rennes) n'est donc PAS démontré par les données de commande publique. Ce qui EST documenté : l'usage interne de l'ERP Symetri par TRIBORD sur ses sites (LinkedIn) et la verticale exploitant/éditeur.
3. **Le point juridique le plus critique** : le marché SITREVA 214 k€ (22/09/2022) pour la gestion informatisée des déchèteries a été passé **« marché négocié sans publicité ni mise en concurrence préalable »** — l'une des 4 commandes publiques de Symetri. C'est le maillon faible procédural de la chaîne.
4. **L'ampleur du marché** : Symetri = 4 marchés publics (440 k€) + CA 977 k€ (2025, ×2 en 3 ans) + déploiement annoncé dans 380+ déchèteries (≈8 % des ~4 630 sites SINOE) — un acteur de niche en forte croissance dans un marché atomisé (9-10 fournisseurs par type de système selon DT138). TRIBORD encaisse 64,1 M€ de marchés publics.
5. **Honnêteté épistémique** : la couverture DossiersGagnants n'est pas exhaustive (certains acheteurs ne publient pas leurs données essentielles) ; les comptes consolidés du groupe TRIBORD et les parts de marché par éditeur ne sont pas publiés. Les 5 FCT sont ✦ (2 familles chacune) mais le conflit direct Rennes/Symetri reste non démontré — c'est un conflit structurel à surveiller, pas un fait avéré de captation.

## Sources INSPECTED

- e-tribord.com/a-propos (chronologie officielle : 1991 Spernot Brest, 2002 Rennes 14→25, 2018 filialisation Symetri)
- DossiersGagnants TRIBORD (25 marchés, 64,1 M€, Rennes 21 M€ avec contrôle d'accès dans l'objet)
- DossiersGagnants Symetri (4 marchés, 440 k€, SITREVA 214 k€ sans mise en concurrence)
- Nukema (marché cartes KorriGo Rennes, clôture 01/07/2024) + Gesbac (journal mises à jour : Rennes = NETVLM/GIDED, interface Symetri pour EPT Paris Terres d'Envol)
- bretagne-marchespublics (marché Valcobreizh 11/10/2024 : bornes + logiciel + 51 000 cartes RFID, interfaçage STYX)
- 20minutes 11/10/2025 (Valcobreizh 200 k€, KorriGo non déployé, Janzé 18 passages/an)
- Pappers (comptes Symetri/TRIBORD) + LinkedIn Nina CHA (ERP Symetri chez Tribord)

## Réfutations (5 NONE)

- FCT-001 : aucune preuve que Symetri ne soit pas issu du département numérique de Tribord, ni que TRIBORD n'exploite pas Rennes depuis 2002
- FCT-002 : aucune preuve que TRIBORD n'ait pas 25 marchés / 64,1 M€, ni que le marché Rennes soit différent de 21 M€
- FCT-003 : aucune preuve que Rennes ait confié son contrôle d'accès à Symetri (les sources convergent vers KorriGo/Gesbac)
- FCT-004 : aucune preuve de plus de 4 marchés Symetri, ni que le marché SITREVA ne soit pas de 214 k€ sans mise en concurrence
- FCT-005 : aucune preuve que Valcobreizh n'ait pas dépensé ~200 k€, ni que le quota Janzé soit différent de 18 passages/an

## Gaps ouverts

1. Attributaire exact du marché Valcobreizh 2024 (bornes + logiciel + 51 000 cartes) — Symetri y figure-t-il ?
2. Croisement géographique des 25 marchés TRIBORD × 4 marchés Symetri (EPCI où le groupe exploite ET fournit)
3. Audit procédural du marché SITREVA 214 k€ (motif du « sans publicité ni mise en concurrence », renouvellement ?)
4. Part de marché réelle de Symetri (380+ déchèteries annoncées vs ~4 630 SINOE ≈ 8 % — à corroborer)
5. Suivi du déploiement KorriGo/Rennes et de l'éventuel glissement vers Symetri via le contrat TRIBORD (2027-2030)
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"TRIBORD exploite Rennes depuis 2002 (14->25 sites), Symetri = ex-dept numerique filialise 2018, marche Rennes 21 ME 15/05/2025 inclut controle d'acces","kind":"EVENT","lead":"Conflit d'interets structurel presume : Symetri (editeur du logiciel de controle d'acces en decheterie) est la filiale a 100% de TRIBORD (exploitant de decheteries, notamment Rennes Metropole) — le fournisseur du compteur serait aussi l'exploitant des sites comptes","locator":"e-tribord.com chronologie + DossiersGagnants (25 marches TRIBORD, 4 marches Symetri) + Nukema (KorriGo) + 20minutes","materiality":"HIGH","routes":["marches publics (BOAMP, DossiersGagnants, TED)","contrats d'exploitation decheteries Rennes Metropole","fiches societes (Pappers, societe.com, annuaire-entreprises)","concurrence editeurs (Horanet, Gesbac, SeeTech, SIGRENEA)"],"source_id":"SRC-001","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (marches publics disperses, montants parfois non publies, parts de marche non publiees)","linked_ids":["LED-001","AXS-001"],"proposition":"Il existe un conflit d'interets structurel documentable : Symetri (editeur du compteur) et TRIBORD (exploitant des sites) appartiennent au meme groupe, et TRIBORD exploite les decheteries de Rennes Metropole — territoire ou Symetri vend ses solutions ; le marche du controle d'acces en decheterie est atomise (9-10 fournisseurs par type de systeme, DT138)","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006"],"gap_type":"NONE","led_links":["LED-001"],"question":"Le lien capitalistique Symetri/TRIBORD se traduit-il par des marches publics croises sur les memes EPCI (TRIBORD exploite les decheteries, Symetri vend le controle d'acces) ? Quelle est la part de marche de Symetri parmi les editeurs ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["marches publics Symetri (4 recenses DossiersGagnants)","contrats d'exploitation TRIBORD (Rennes Metropole, autres)","part de marche editeurs controle d'acces decheterie","liens marches TRIBORD/Symetri sur memes EPCI","chiffre d'affaires et commandes publiques par editeur"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"linked_ids":["LED-001","AXS-001","CLM-001"],"mechanism":"TRIBORD exploite les decheteries de Rennes Metropole (21 ME, depuis 2002) et detient Symetri (ex-departement numerique filialise 2018, ERP utilise en interne par TRIBORD) ; mais Rennes utilise Gesbac/KorriGo pour le controle d'acces -> conflit indirect et potentiel, non un marche Symetri direct chez Rennes ; le marche SITREVA 214 kE passe sans mise en concurrence est le point juridique le plus critique","question":"Le lien capitalistique Symetri/TRIBORD cree-t-il un conflit d'interets structurel dans l'exploitation et le controle des decheteries publiques ?","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:13|EXA:5
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | 52067326-19c0-467e-a638-dc10bb5e43b4 | MEMORY_PROBE
SYS-002 | SYS | FOUND: warm-route 52067326 (FCT-005 axe F : Symetri = filiale 100% TRIBORD, CA 977 kE 2025, apps Depos/Join/User-YT ; TRIBORD exploite decheteries Rennes Metropole) + Pappers 841351901/378801682 | mnemolite:search_memory | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime:load | - | ALWAYS_LOAD: definitions/SYMBOLS.md, definitions/PATTERNS.md, definitions/THREATS.md, forensic/GATES.md, forensic/REQUEST_LOG.md
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | - | - | FETCH groupe Tribord : chronologie, filialisation SYMETRI 2018, exploitation Rennes depuis 2002, 25 decheteries
QRY-002 | FETCH | FOUND | - | - | FETCH DossiersGagnants TRIBORD : 25 marches, 64,1 ME, Rennes 21 ME avec controle d'acces
QRY-003 | FETCH | FOUND | - | - | FETCH DossiersGagnants SYMETRI : 4 marches, 440 kE, SITREVA 214 kE sans mise en concurrence
QRY-004 | FETCH | FOUND | - | - | FETCH marches Rennes Metropole : cartes KorriGo 2024, logiciel Gesbac, interface SYMETRI Paris Terres d'Envol
QRY-005 | FETCH | FOUND | - | - | FETCH 20minutes : Valcobreizh 200 kE, Korrigo non deploye, Janze 18 passages, depots sauvages
QRY-006 | FETCH | FOUND | - | - | FETCH LinkedIn Nina CHA : TRIBORD utilise ERP Symetri oct 2025-mai 2026
QRY-007 | FETCH | FOUND | SRC-001 | https://e-tribord.com/a-propos/ | -
QRY-008 | FETCH | FOUND | SRC-002 | https://dossiersgagnants.fr/entreprise/378801682-tribord | -
QRY-009 | FETCH | FOUND | SRC-003 | https://dossiersgagnants.fr/entreprise/841351901-symetri | -
QRY-010 | FETCH | FOUND | SRC-004 | https://marches-publics.nukema.com/seo/consultation/view/2314444/Fourniture_de_cartes_d_acces_en_decheterie | -
QRY-011 | FETCH | FOUND | SRC-005 | https://www.20minutes.fr/planete/4178506-20251011-flicage-pourquoi-dechetteries-controlent-plus-plus-entrees | -
QRY-012 | FETCH | FOUND | SRC-006 | https://fr.linkedin.com/in/nina-cha-0a00b68a | -
QRY-013 | FETCH | FOUND | SRC-007 | https://www.pappers.fr/entreprise/symetri-841351901 | -
QRY-014 | EXA | FOUND | - | - | REFUTATION 05 07 10 14 2002 2018 2025 2026 25 26 450 601 : une preuve que Symetri n'est pas issu du departement numerique de Tribord filialise en 2018, ni que Tribord exploite Rennes depuis 2002
QRY-015 | EXA | FOUND | - | - | REFUTATION 01 05 1 10 15 17 2020 2025 2026 21 25 5 64 : une preuve que TRIBORD n'a pas 25 marches ni 64,1 ME cumules, ni que le marche Rennes Metropole est different de 21 ME
QRY-016 | EXA | FOUND | - | - | REFUTATION 01 02 05 07 10 11 20 2024 2025 241336018 : une preuve que Rennes Metropole a confie le controle d'acces a Symetri (et non KorriGo/Gesbac), ou que le deploiement n'est pas retarde
QRY-017 | EXA | FOUND | - | - | REFUTATION 000 01 10 11 13 18 200 2024 2025 35 51 56 6 90 : une preuve que Valcobreizh n'a pas depense ~200 000 EUR, ni que le quota Janze est different de 18 passages/an
QRY-018 | EXA | FOUND | - | - | REFUTATION 08 09 1 10 13 16 2 2022 2023 2026 2027 214 22 226 4 440 : une preuve que Symetri a plus de 4 marches, ou que le marche SITREVA n'est pas de 214 kE sans mise en concurrence

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://e-tribord.com/a-propos/
SRC-002 | ◈ | fam:B | https://dossiersgagnants.fr/entreprise/378801682-tribord
SRC-003 | ◈ | fam:B | https://dossiersgagnants.fr/entreprise/841351901-symetri
SRC-004 | ◈ | fam:C | https://marches-publics.nukema.com/seo/consultation/view/2314444/Fourniture_de_cartes_d_acces_en_decheterie
SRC-005 | ◈ | fam:D | https://www.20minutes.fr/planete/4178506-20251011-flicage-pourquoi-dechetteries-controlent-plus-plus-entrees
SRC-006 | ◈ | fam:D | https://fr.linkedin.com/in/nina-cha-0a00b68a
SRC-007 | ◈ | fam:E | https://www.pappers.fr/entreprise/symetri-841351901

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://e-tribord.com/a-propos/ | A,D | 2026-08-30 | Lien capitalistique avère : Symetri (SASU creee 26/07/2018, capital 601 450 EUR) = ancien departement numerique de Tribord filialise en 2018 (chronologie officielle e-tribord.com) ; TRIBORD exploite les decheteries de Rennes Metropole depuis 2002 (passage de 14 a 25 decheteries gerees) ; profil LinkedIn (10/2025-05/2026) : 'Gestion des flux de dechets avec l'ERP edite par Symetri' chez Tribord | e-tribord.com/a-propos INSPECTED : '2018 : Creation de la filiale SYMETRI SAS - Initialement departement numerique de Tribord, SYMETRI devient une filiale. Poursuite de son activite de conception et deploiement de solutions de tracabilite' ; '2002 : Fort developpement - grace a l'obtention du marche de gestion des decheteries de Rennes Metropole, nous passons de 14 a 25 decheteries gerees' ; '1991 : premier salarie en parcours d'insertion pour la gestion de la decheterie du Spernot a Brest'. LinkedIn Nina CHA (snippet) : Tribord oct 2025-mai 2026, 'Gestion des flux de dechets avec l'ERP edite par Symetri'. Pappers : Symetri SASU creee 26/07/2018, president TRIBORD. Source: e-tribord.com + linkedin.com (verifie 2026-08-30, tier ✦) | 0697d879-0a14-4f64-b42d-1cb01275dd54
FCT-002 | FACT | ✦ | https://dossiersgagnants.fr/entreprise/378801682-tribord | A,B | 2026-08-30 | TRIBORD = 25 marches publics, 64,1 ME cumules (2020-2026) dont RENNES METROPOLE 1 marche 21 ME (15/05/2025, procedure avec negociation) pour l'exploitation du reseau de decheteries et plateformes vegetaux — contrat qui inclut explicitement 'le controle d'acces et l'accueil des usagers' + 'clause de performance pour le controle des producteurs de dechets non-menagers' ; contrat demarre 01/10/2025 pour 5 ans (17 agents valoristes recrutes) | DossiersGagnants TRIBORD INSPECTED : 25 marches, 64,1 ME cumules, 23/04/2020-06/01/2026 ; acheteurs : Rennes Metropole 1 marche 21 ME, CC Coutances Mer et Bocage 2 marches 22,3 ME, Roi Morvan 4 marches 4,6 ME, Pays d'Iroise 3 marches 3,5 ME, Landerneau-Daoulas 3 marches 2,4 ME ; marche Rennes 15/05/2025 : objet 'exploitation du reseau de decheteries et de plateformes vegetaux de Rennes Metropole, a savoir notamment : le controle d'acces et l'accueil des usagers... (clause de performance pour le controle des producteurs de dechets non-menagers)'. e-tribord 13/10/2025 : 'depuis le 1er octobre, a demarre le nouveau marche... pour la gestion de ses decheteries pour les 5 prochaines annees', 17 Agents Valoristes recrutes. Source: dossiersgagnants.fr + e-tribord.com (verifie 2026-08-30, tier ✦) | ca25525a-53a6-4ecf-bdeb-c84743c86378
FCT-003 | FACT | ✦ | https://marches-publics.nukema.com/seo/consultation/view/2314444/Fourniture_de_cartes_d_acces_en_decheterie | C,D | 2026-08-30 | NUANCE : Rennes Metropole n'a PAS confie le controle d'acces a Symetri — la carte choisie est KorriGo Services (marche fourniture cartes, cloture 01/07/2024, ref 241336018_MAPA) et le logiciel de gestion est Gesbac NETVLM/GIDED (journal mises a jour 02/05/2024) ; la mise en oeuvre est retardee ('calendrier non stabilise', 20minutes 11/10/2025) ; le conflit est donc INDIRECT (TRIBORD exploite + utilise l'ERP Symetri en interne) et non un marche Symetri chez Rennes | Nukema INSPECTED : marche Rennes Metropole 'Fourniture de cartes d'acces en decheterie' (ref 241336018_MAPA, cloture 01/07/2024) : 'Rennes Metropole va deployer en 2024 le controle d'acces dans ses decheteries... La carte d'acces choisie pour ce controle d'acces est la carte KorriGo Services'. Gesbac (mises-a-jour-du-logiciel-2024) : '02/05/2024 - Rennes Metropole Lecture' sous le logiciel NETVLM/GIDED. 20minutes 11/10/2025 : 'L'acces avec une carte Korrigo avait meme ete annonce pour 2024, sauf que rien n'a bouge... le calendrier de mise en oeuvre n'est pas stabilise'. Source: nukema.com + gesbac.fr + 20minutes.fr (verifie 2026-08-30, tier ✦) | f6edbfb2-5084-445e-a06f-7970669cba75
FCT-004 | FACT | ✦ | https://www.20minutes.fr/planete/4178506-20251011-flicage-pourquoi-dechetteries-controlent-plus-plus-entrees | C,D | 2026-08-30 | Contexte marche du controle d'acces en decheterie (Bretagne) : Smictom Valcobreizh debourse ~200 000 EUR (cartes, logiciel, barrieres) pour equiper ses decheteries (badge obligatoire au 01/11/2025, 90 000 habitants, interfaçage logiciel STYX, marche 11/10/2024 : 51 000 cartes RFID 13,56) ; Fougeres controle depuis 10 ans ; Janze/Smictom sud-est 35 : 18 passages/an ; crainte de depots sauvages et report en OMr documentee par les elus ; Rennes Metropole : 18 decheteries + 6 plateformes vegetaux, KorriGo annonce 2024 non deploye | 20minutes 11/10/2025 INSPECTED : Valcobreizh 'a debourse un peu plus de 200.000 euros pour s'equiper en cartes, en logiciel et en barrieres' ; badge obligatoire au 1er novembre pour 90 000 habitants ; 'On table raisonnablement sur une baisse des apports de 5%. Si on atteint cela, on aura amorti l'investissement en un an' ; Janze '18 passages par an' ; 'certaines collectivites craignent des depots sauvages ou un report dans les poubelles d'ordures menageres' ; Rennes : '18 dechetteries et 6 plateformes pour vegetaux' (20minutes 16/12/2022) ; marche Valcobreizh (bretagne-marchespublics 11/10/2024, avis 24-115900) : bornes/barrieres + logiciel + 51 000 cartes RFID HF 13,56, interfaçage STYX. Source: 20minutes.fr + bretagne-marchespublics.com (verifie 2026-08-30, tier ✦) | e658fce7-fbcc-4bbf-ac63-a07836ab214a
FCT-005 | FACT | ✦ | https://dossiersgagnants.fr/entreprise/841351901-symetri | B,E | 2026-08-30 | Marches publics Symetri = 4 marches, 440 kE cumules (22/09/2022 - 13/08/2026) : ARCHE Agglo 2 marches 226 kE (controle d'acces + logiciel gestion decheteries, 13/08/2026), SITREVA 1 marche 214 kE (gestion informatisee des decheteries, 22/09/2022, MARCHE NEGOCIE SANS PUBLICITE NI MISE EN CONCURRENCE PREALABLE), Saint-Brieuc Armor Agglo 1 marche (montant non renseigne, 16/10/2023) ; 2 contrats en cours, prochaine echeance 16/10/2027 | DossiersGagnants Symetri INSPECTED : 4 marches, 440 kE cumules, premier 22/09/2022, dernier 13/08/2026 ; ARCHE Agglo : 2 marches, 226 kE ('26A09A - Fourniture et mise en place d'un controle d'acces et logiciel de gestion des decheteries d'ARCHE Agglo' 120 kE + 106 kE, 13/08/2026, procedure adaptee) ; SITREVA : 1 marche 214 kE ('GESTION INFORMATISEE DES DECHETERIES DE SITREVA', 22/09/2022, 'Marche negocie sans publicite ni mise en concurrence prealable', duree 3 ans, confirme Pappers) ; Saint-Brieuc : 1 marche non renseigne (16/10/2023). Source: dossiersgagnants.fr + pappers.fr (verifie 2026-08-30, tier ✦) | e8f37607-fbb3-4340-afab-bb8e5a9b6e27
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-006
FCT-002 | SRC-002,SRC-001
FCT-003 | SRC-004,SRC-005
FCT-004 | SRC-005,SRC-004
FCT-005 | SRC-003,SRC-007

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-014 | NONE
FCT-002 | QRY-015 | NONE
FCT-003 | QRY-016 | NONE
FCT-004 | QRY-017 | NONE
FCT-005 | QRY-018 | NONE

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
ATTEMPT-001 | {"created_at":"2026-08-30T19:21:06.988808+00:00","fact_mem":{"FCT-001":"0697d879-0a14-4f64-b42d-1cb01275dd54","FCT-002":"ca25525a-53a6-4ecf-bdeb-c84743c86378","FCT-003":"f6edbfb2-5084-445e-a06f-7970669cba75","FCT-004":"e658fce7-fbcc-4bbf-ac63-a07836ab214a","FCT-005":"e8f37607-fbb3-4340-afab-bb8e5a9b6e27"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory reference MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
