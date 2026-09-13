ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2015-audit-exclusion-pros-decheteries-2026 | PARENT_RUN_ID:20260830-0904-dechetteries-france | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_dechetteries-france/2026-08-30_audit-exclusion-pros-decheteries-2026/2026-08-30_20-15_audit-exclusion-pros-decheteries-2026_INPUT.txt | SUBJECT_SLUG:audit-exclusion-pros-decheteries-2026 | SUBJECT_FP:sha256:a36a42c2611397d5bd90ab5c9e1e917ae2c166a2f42c9746619cd6bb83b7ab7d | INPUT_SHA256:sha256:5db6c89058e995e439a9645d03a740b5f542413d3dfe87029fd18664aa0b3c86
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['AMP Aix-Marseille-Provence', 'EPCI gestionnaires', 'ADEME', 'AMORCE', 'Cerema', 'professionnels/artisans', 'eco-organismes PMCB'], 'domains': ['dechets', 'decheteries', 'professionnels', 'depots sauvages', 'politique publique', 'finances locales'], 'geo': 'France', 'lead_question': "Qui a ete exclu des decheteries publiques en 2025-2026 (professionnels, gros apporteurs) et ou vont leurs dechets ? La fermeture de l'acces pros est-elle correlee a une hausse des depots sauvages / du cout de resorption ?", 'limits': 'donnees depots sauvages heterogenes (pas de referentiel national unifie) ; effet de la fermeture AMP 07/2025 encore recent', 'object_question': '(1) identifier les exclusions (acteurs, dates, motifs, flux) ; (2) tracer la destination des dechets des ex-exclus (prive, REP PMCB, depots sauvages) ; (3) tester la causalite fermeture -> depots sauvages avec baseline'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Axe A — « Qui a été exclu des déchèteries en 2025-2026 ? » et où vont les déchets

**Run `20260830-2015-audit-exclusion-pros-decheteries-2026`** — investigation depuis 2026 (inverse du travail historique pré-2010). Objet : documenter l'exclusion des professionnels des déchèteries publiques (2025-2026), tracer la destination des flux et tester la causalité fermeture → dépôts sauvages.

## Verdict

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **AMP = premier acte métropolitain français d'exclusion généralisée des professionnels** : règlement adopté par le conseil métropolitain le **27/02/2025**, en vigueur **01/07/2025** — pros exclus, particuliers quotas (3 passages/jour, 36 visites/an, 3 m³ verts, 3 m³ gravats, 4 pneus, 75 kg DDS), alternatives gratuites oca-batiment.org + pneus en garages | ✦ (A+B, réfutation NONE) |
| **FCT-002** | **Généralisation été 2026** : Nice, Lyon, Lille, Toulouse, St-Étienne, Orléans, Lannion, Pays de Falaise réservent aux particuliers ; Rennes interdit les tontes ; contrôle d'accès par cartes/quotas documenté par l'enquête AMORCE/ADEME DT138 (07/11/2025, déchèteries = ~40 % des déchets SPGD) | ✦ (E+D, réfutation NONE) |
| **FCT-003** | **Le risque de hausse des dépôts sauvages est documenté dès l'annonce** : Bouc-Bel-Air (01/08/2025 : « risque d'amplifier le phénomène », caméras/rondes renforcées), entrepreneur de Mallemort (10/06/2025 : 1-2 t/jour de déchets verts sans solution, risque incendie), presse nationale (21/04/2026) | ✦ (B+C, réfutation NONE) |
| **FCT-004** | **La refondation PMCB 2027 aggrave le risque** : suppression de la reprise gratuite des déchets « matures » (métal, bois, plâtre, inertes) au **01/01/2027** (annonce ministre Lefèvre, 2026) ; AMF/Intercommunalités/Régions de France + Capeb réclament un fonds dépôts sauvages jusqu'à 10 m³ ; Ouest-France titre « la réforme va encourager les dépôts sauvages » | ✦ (C+D, réfutation NONE) |
| **FCT-005** | **Verdict causalité : corrélation documentée mais causalité NON démontrée quantitativement** — baseline ADEME 2019 (90 % des collectivités, 21,4 kg/hab/an, 59 210 €/an/collectivité) et Cerema 2024 (30-90 M€/an) ; AUCUNE série nationale chiffrée post-2025 ; l'ADEME lance elle-même une nouvelle enquête (20/05/2026, Ecogeos/Rudologia) | ✦ (D+B, réfutation NONE) |

## Découvertes clés

1. **Une décision politique majeure jamais documentée dans le dossier** : l'exclusion des pros (AMP pionnière 01/07/2025, généralisation été 2026) est la mutation la plus structurante du réseau depuis la création. Le motif officiel (« responsabilité élargie du producteur ») est contesté par les acteurs locaux (« décidée sans concertation », entrepreneurs non prévenus).
2. **Le trou de la raquette : les déchets verts** — les alternatives gratuites annoncées (OCA-Bâtiment pour le BTP, garages pour les pneus) **ne couvrent pas les déchets verts** des paysagistes (1-2 t/jour à Mallemort, aucun débouché, trajets de +1 h jusqu'à Gardanne).
3. **Test de causalité : honnêteté épistémique** — le faisceau qualitatif converge (communes, Capeb, entrepreneurs, presse), mais aucune série nationale chiffrée post-2025 n'existe ; la corrélation est plausible, la causalité **non démontrée** (chronologie courte, pas de contrefactuel). L'ADEME elle-même reconnaît le manque de données en lançant une nouvelle enquête nationale.

## Sources INSPECTED (FETCH direct)

- Règlement déchèteries AMP (conseil métropolitain 27/02/2025, en vigueur 01/07/2025)
- Bouc-Bel-Air 01/08/2025 (risque d'amplification des dépôts sauvages, Mat'ild sous-dimensionnée)
- ici.fr 10/06/2025 (Mallemort : 1-2 t/jour déchets verts, risque incendie, non prévenu)
- France 3 21/04/2026 (Lefèvre, refondation PMCB 2027, Capeb 13, communiqué AMF/Intercommunalités/Régions)
- Enquête AMORCE/ADEME DT138 07/11/2025 (accès, contrôle, facturation ; ~40 % déchets SPGD)
- ADEME 20/05/2026 (nouvelle étude nationale dépôts sauvages, Ecogeos/Rudologia)
- Ami des Jardins 16/06/2026 (généralisation été 2026, profils à risque, alternatives payantes)
- Snippet Ouest-France 21/04/2026 (403 au fetch direct)

## Réfutations (5 NONE)

- FCT-001 : aucune exclusion pros à une autre date que le 01/07/2025 ni maintien d'accès après
- FCT-002 : aucune métropole ayant conservé un accès pro libre sans restriction en 2026
- FCT-003 : aucune source niant le risque de dépôts sauvages après la fermeture AMP
- FCT-004 : aucune preuve de maintien de la reprise gratuite des matures après 01/01/2027
- FCT-005 : aucune série nationale chiffrée post-2025 imputable à l'exclusion des pros

## Gaps ouverts

1. Résultats de l'étude ADEME 2026 (Ecogeos/Rudologia) à la publication
2. Chiffres dépôts sauvages AMP 2025-2026 (rapport annuel déchets de la Métropole)
3. Délibération exacte du conseil métropolitain AMP du 27/02/2025 (cote)
4. Données quantitatives locales (Saint-Raphaël 130 t 2025, +3 %/an)

## Conséquence sur la fresque

Le dossier couvrait l'histoire (pré-1980 → 2009) et la couche argent (REP) ; **la couche 2025-2026 manquait** : cette passe ajoute la mutation en cours (exclusion des pros, contrôle d'accès, quotas, refondation PMCB 2027) et documente le risque de transfert de coût vers les contribuables via les dépôts sauvages — en maintenant la distinction stricte corrélation ≠ causalité.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"Depuis le 1er juillet 2025, les professionnels ne peuvent plus acceder aux decheteries metropolitaines (AMP)","kind":"EVENT","lead":"AMP ferme l'acces des professionnels aux decheteries metropolitaines au 01/07/2025 ; restrictions generalisees a partir du 01/07/2026 (cartes d'acces, refus gros apporteurs)","linked_ids":["AXS-001"],"locator":"ampmetropole.fr reglement decheteries 01/07/2025 ; presse ete 2026","materiality":"DECISIVE","routes":["AUDIT","EXPAND"],"source_id":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (pas de referentiel national des depots sauvages)","linked_ids":["LED-001","AXS-001"],"proposition":"La fermeture de l'acces des professionnels aux decheteries publiques (2025-2026) detourne une partie des flux vers le prive payant et les depots sauvages, avec un cout de resorption en hausse — a tester avec baseline","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":[],"gap_type":"NONE","led_links":["LED-001"],"question":"Qui est exclu des decheteries 2025-2026, ou vont les dechets des ex-exclus, et la fermeture pros augmente-t-elle les depots sauvages ?","result_ids":[],"sought_objects":["reglements decheteries 2025-2026 (AMP, autres EPCI)","enquete AMORCE/ADEME DT138 (acces, controle, facturation)","cout depots sauvages (Cerema 2024, mise a jour 2025-2026)","destination des flux pros (REP PMCB, prive, depots sauvages)"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Exclusion des professionnels des decheteries publiques (motifs : cout, saturation, REP PMCB)","effect":"Redirection des flux pros vers le prive payant et/ou depots sauvages, hausse du cout de resorption","source":"FCT-002","status":"SUPPORTED","type":"MECHANISM"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:7|EXA:5
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND: warm-route mems b18be14a (acces pros = decision gestionnaire) + 42ec6571 (cout depots sauvages 30-90 Meur/an Cerema 2024) + ad7c53e5 (etat reseau 2026) ; GAP: exclusion pros 2025-2026 non documentee, causalite depots sauvages OPEN | mnemolite:search_memory | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-004 | SYS | LOADED | runtime:load | - | ALWAYS_LOAD: definitions/SYMBOLS.md, definitions/PATTERNS.md, definitions/THREATS.md, forensic/GATES.md, forensic/REQUEST_LOG.md
SYS-005 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-006 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/ | FETCH reglement AMP : conseil metropolitain 27/02/2025, en vigueur 01/07/2025, pros exclus, particuliers quotas 3 passages/jour 36 visites/an 3 m3 verts 3 m3 gravats 4 pneus 75 kg DDS, alternatives oca-batiment.org
QRY-002 | FETCH | FOUND | SRC-002 | https://www.boucbelair.fr/actualites/depots-sauvages-nouvelles-regles-pour-la-dechetterie-la-municipalite-se-mobilise/ | FETCH Bouc-Bel-Air : restriction acces dechetteries « risque d'amplifier le phenomene », renforcement rondes/cameras, decheterie pro Matild sous-dimensionnee, pros locaux en difficulte
QRY-003 | FETCH | FOUND | SRC-003 | https://www.ici.fr/infos/environnement/ca-va-contre-le-bon-sens-pour-les-professionnels-interdiction-au-1er-juillet-d-aller-dans-les-dechetteries-2387857 | FETCH ici.fr Mallemort : Patrice Theobald Provence Environnement, 1-2 t dechets verts/jour, pas prevenu, crainte depots sauvages + incendies, dechetteries privees refusent, Gardanne a 1h
QRY-004 | FETCH | FOUND | SRC-004 | https://france3-regions.franceinfo.fr/provence-alpes-cote-d-azur/bouches-du-rhone/marseille/des-dizaines-de-kilometres-pour-trouver-des-dechetteries-le-gouvernement-veut-supprimer-la-reprise-des-dechets-du-batiment-inquietude-autour-des-depots-sauvages-3338618.html | FETCH France 3 : ministre Lefevre (Capeb AG 2026) supprimer reprise gratuite dechets matures (metal, bois, platre, inertes) au 01/01/2027 ; Capeb 13 : « si on ne nous reprend plus les dechets, c'est le risque » ; AMF/Intercommunalites/Regions + Capeb demandent fonds depots sauvages jusqu'a 10 m3 des 01/01/2027
QRY-005 | FETCH | FOUND | SRC-005 | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138 | FETCH DT138 : decheteries captent ~40% des dechets SPGD ; etat des lieux acces/controle/facturation, quotas, evolution conditions accueil pros vs sondages anterieurs
QRY-006 | FETCH | FOUND | SRC-006 | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages | FETCH ADEME 20/05/2026 : nouvelle enquete nationale depots sauvages apres etude 2019, avec Ecogeos et Rudologia, actualiser les connaissances
QRY-007 | FETCH | FOUND | SRC-007 | https://lamidesjardins.maison-travaux.fr/actualites/des-le-1er-juillet-2026-lacces-aux-decheteries-sera-refuse-a-certains-usagers-etes-vous-concerne-19011.html | FETCH Ami des Jardins : ete 2026, metropoles suivent AMP (Nice, Lyon, Lille, Toulouse, Saint-Etienne, Orleans, Lannion, Pays de Falaise), Rennes tontes interdites, profils a risque (artisans, paysagistes, utilitaires floques), alternatives OCA-Batiment, Mat'ild, Suez, Pasini, garages 8 pneus
QRY-008 | EXA | NONE trouve : aucune source ne documente une exclusion des professionnels des decheteries metropolitaines a une autre date que le 01/07/2025, ni un maintien d'acces apres cette date ; AMP reste le premier acte metropolitain francais d'exclusion generalisee | - | - | REFUTATION Aix-Marseille 13 27 02 2025 01 07 3 36 4 75 : une preuve d'exclusion des professionnels des decheteries metropolitaines avant le 01/07/2025, a une autre date, ou d'un maintien d'acces apres cette date
QRY-009 | EXA | NONE trouve : aucune source ne documente une metropole ayant conserve un acces professionnel ouvert sans restriction en 2026 ; la tendance citee (Nice, Lyon, Lille, Toulouse, Saint-Etienne, Orleans, Lannion, Falaise) est coherente avec la generalisation | - | - | REFUTATION decheteries 2026 Nice Lyon Lille Toulouse Saint-Etienne Orleans Lannion Falaise : une preuve qu'une grande metropole francaise a conserve en 2026 un acces professionnel libre aux decheteries publiques sans restriction ni quota
QRY-010 | EXA | NONE trouve : aucune source ne documente une absence de crainte de depots sauvages apres la fermeture AMP ; au contraire, communes (Bouc-Bel-Air 01/08/2025), entrepreneurs (10/06/2025) et presse (21/04/2026) convergent vers un risque documente | - | - | REFUTATION depots sauvages Bouc-Bel-Air 01 08 2025 Mallemort 10 06 1 2 21 04 2026 : une preuve que la fermeture des decheteries aux professionnels n'a pas suscite de crainte ni de constat de depots sauvages sur le territoire AMP
QRY-011 | EXA | NONE trouve : aucune source ne documente un maintien de la reprise gratuite des dechets matures PMCB apres 01/01/2027 ; la suppression est annoncee par le ministre et confirmee par la presse, les collectivites et la Capeb en demandant des correctifs (fonds depots sauvages 10 m3) | - | - | REFUTATION PMCB 01 01 2027 10 m3 Lefevre 2026 : une preuve que la reprise gratuite des dechets matures (metal, bois, platre, inertes) serait maintenue apres le 01/01/2027 sans correctif ni fonds depots sauvages
QRY-012 | EXA | NONE trouve : aucune source ne fournit de serie nationale chiffree des depots sauvages post-2025 imputable a l'exclusion des professionnels ; l'ADEME elle-meme lance une nouvelle enquete nationale (20/05/2026) faute de donnees actualisees — la causalite demeure non demontree quantitativement | - | - | REFUTATION causalite depots sauvages 20 05 2026 2025 : une preuve chiffree nationale et post-2025 d'une hausse des depots sauvages directement imputable a l'exclusion des professionnels des decheteries publiques

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/
SRC-002 | ◈ | fam:B | https://www.boucbelair.fr/actualites/depots-sauvages-nouvelles-regles-pour-la-dechetterie-la-municipalite-se-mobilise/
SRC-003 | ◈ | fam:B | https://www.ici.fr/infos/environnement/ca-va-contre-le-bon-sens-pour-les-professionnels-interdiction-au-1er-juillet-d-aller-dans-les-dechetteries-2387857
SRC-004 | ◈ | fam:C | https://france3-regions.franceinfo.fr/provence-alpes-cote-d-azur/bouches-du-rhone/marseille/des-dizaines-de-kilometres-pour-trouver-des-dechetteries-le-gouvernement-veut-supprimer-la-reprise-des-dechets-du-batiment-inquietude-autour-des-depots-sauvages-3338618.html
SRC-005 | ◈ | fam:D | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138
SRC-006 | ◈ | fam:D | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages
SRC-007 | ◈ | fam:E | https://lamidesjardins.maison-travaux.fr/actualites/des-le-1er-juillet-2026-lacces-aux-decheteries-sera-refuse-a-certains-usagers-etes-vous-concerne-19011.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://dechets.ampmetropole.fr/nouveau-reglement-des-decheteries-ce-qui-change-au-1er-juillet-2025/ | A,B | 2026-08-30 | Aix-Marseille-Provence (13) : reglement decheteries adopte le 27/02/2025, en vigueur 01/07/2025 — professionnels exclus, particuliers quotas (3 passages/jour, 36 visites/an, 3 m3 verts, 3 m3 gravats, 4 pneus, 75 kg DDS), alternatives gratuites oca-batiment.org + pneus garages | Acte primaire INSPECTED : le conseil metropolitain AMP du 27/02/2025 adopte un reglement unifie en vigueur 01/07/2025. Professionnels : acces interdit (motifs : ameliorer accueil particuliers, reduire pression poids lourds, clarifier depot). Particuliers : acces reserve aux habitants, 3 passages max/jour, 36 visites/an, 3 m3 dechets verts/jour, 3 m3 gravats/jour, 4 pneus/jour, 75 kg DDS/jour. Alternatives gratuites annoncees : oca-batiment.org (dechets du batiment) et reprise pneus en garages. Premier acte metropolitain francais d'exclusion generalise des professionnels (ici.fr 10/06/2025 : decidee sans concertation, entrepreneurs non prevenus). | 25ae4fe7-2438-4f27-8db6-e1803818ffa5
FCT-002 | FACT | ✦ | https://lamidesjardins.maison-travaux.fr/actualites/des-le-1er-juillet-2026-lacces-aux-decheteries-sera-refuse-a-certains-usagers-etes-vous-concerne-19011.html | D,E | 2026-08-30 | Generalisation ete 2026 : Nice, Lyon, Lille, Toulouse, Saint-Etienne, Orleans, Lannion, Pays de Falaise reservent les decheteries aux particuliers ; Rennes interdit les tontes — acces controles par cartes, quotas et refus de vehicules pro | Ami des Jardins 16/06/2026 (INSPECTED) : « de plus en plus de decheteries publiques ferment leurs portes aux professionnels et gros apporteurs » ; metropoles citees : Nice Cote d'Azur, Lyon, Lille, Toulouse, Saint-Etienne, Orleans, Lannion, Pays de Falaise ; Rennes interdit les tontes. Profils a risque : artisans, paysagistes, auto-entrepreneurs, BTP, utilitaires floques, associations/syndics/coproprietes. Enquete AMORCE/ADEME DT138 (07/11/2025, INSPECTED) : les collectivites developpent strategies de controle d'acces et facturation ; decheteries captent ~40% des dechets du SPGD. | 1e737d49-5b85-42ec-a363-99c695ed108f
FCT-003 | FACT | ✦ | https://www.boucbelair.fr/actualites/depots-sauvages-nouvelles-regles-pour-la-dechetterie-la-municipalite-se-mobilise/ | B,C | 2026-08-30 | Risque de hausse des depots sauvages documente des l'annonce : Bouc-Bel-Air (01/08/2025 : la restriction « risque d'amplifier le phenomene », cameras/rondes renforcees), entrepreneur Mallemort (10/06/2025 : 1-2 t/jour dechets verts sans solution, risque incendie), presse nationale (21/04/2026 : inquietude sur les depots sauvages) | Constats INSPECTED : (1) Bouc-Bel-Air (01/08/2025) : la mairie declare que « la restriction d'acces aux dechetteries publiques risque d'amplifier le phenomene » (depots sauvages), renforce rondes et cameras dans les collines, zone Chabauds (usine Lafarge) regulierement ciblee ; decheterie pro Mat'ild sous-dimensionnee et source de plaintes. (2) ici.fr (10/06/2025) : Patrice Theobald (Provence Environnement, Mallemort), 1-2 t de dechets verts/jour, non prevenu, craint « depots d'ordures, dechets sauvages et risques securitaires (incendies) » ; dechetteries privees refusent, Gardanne a 1h. (3) France 3 (21/04/2026) : « les depots sauvages pourraient-ils augmenter encore davantage ? » | 61318dd7-fe4b-41c8-91c0-9b6e542b5c23
FCT-004 | FACT | ✦ | https://france3-regions.franceinfo.fr/provence-alpes-cote-d-azur/bouches-du-rhone/marseille/des-dizaines-de-kilometres-pour-trouver-des-dechetteries-le-gouvernement-veut-supprimer-la-reprise-des-dechets-du-batiment-inquietude-autour-des-depots-sauvages-3338618.html | C,D | 2026-08-30 | Refondation PMCB : suppression de la reprise gratuite des dechets matures (metal, bois, platre, inertes) au 01/01/2027 (annonce ministre Lefevre 2026) ; AMF/Intercommunalites/Regions de France + Capeb demandent un fonds depots sauvages jusqu'a 10 m3 — la reforme « va encourager les depots sauvages » | France 3 21/04/2026 (INSPECTED) : le ministre delegue Mathieu Lefevre annonce (Capeb AG 2026) la suppression de la reprise gratuite des dechets « matures » (metal, bois, platre, inertes) a partir du 01/01/2027. Capeb 13 (Patricia Blanchet-Bhang) : « Si on ne nous reprend plus les dechets, c'est le risque [que les depots sauvages augmentent] » ; points de collecte inefficients (des dizaines de km). Communique AMF/Intercommunalites de France/Regions de France + Capeb : reprise sans frais des petits volumes jusqu'a 3 m3 et fonds dedie depots sauvages jusqu'a 10 m3 des 01/01/2027 « pour eviter aux collectivites, et donc aux contribuables, les couts infliges par les eco-delinquants ». Ouest-France titre : « La reforme va encourager les depots sauvages » (21/04/2026). | b6dea4f9-56dd-4e95-8643-5acd226db594
FCT-005 | FACT | ✦ | https://amorce.asso.fr/actualite/l-ademe-lance-une-nouvelle-etude-nationale-sur-les-depots-sauvages | B,D | 2026-08-30 | Verdict causalite : exclusion pros (2025) -> depots sauvages = correelee et documentee par les acteurs mais causalite NON etablie quantitativement — pas de serie nationale post-2025, ADEME lance une nouvelle etude 20/05/2026 (Ecogeos/Rudologia) | Test de causalite (baseline requise) : (1) baseline depots sauvages : ADEME 2019 — 90% des collectivites confrontees, 21,4 kg/hab/an, cout moyen 59 210 EUR/an/collectivite (4,7 EUR/hab/an) ; Cerema 2024 : 30-90 MEUR/an. (2) Exclusion pros : AMP 01/07/2025 puis generalisation ete 2026. (3) Constat : correlations chronologiques locales (Bouc-Bel-Air 01/08/2025, Saint-Raphael 130 t 2025 +3%/an) et declarations d'acteurs (Capeb, communes, entrepreneurs) convergent vers un risque, mais AUCUNE serie nationale chiffree post-2025 n'existe — l'ADEME lance elle-meme une nouvelle enquete nationale (20/05/2026, Ecogeos/Rudologia) faute de donnees actualisees. → H : correlation plausible, causalite NON demontree (chronologie courte, pas de contrefactuel, donnees localisees). | 47df2b75-b055-4d69-a218-313fc4a41805
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-003
FCT-002 | SRC-007,SRC-005
FCT-003 | SRC-002,SRC-004
FCT-004 | SRC-004,SRC-005
FCT-005 | SRC-006,SRC-002

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-003 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9:AXS-001:QRY-001
CP-004 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:FCT-001
CP-005 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:CAU-001
CP-006 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:VERIFY
CP-007 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-008 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18:FINALIZATION_BLOCKED

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T18:24:37.653954+00:00","fact_mem":{"FCT-001":"25ae4fe7-2438-4f27-8db6-e1803818ffa5","FCT-002":"1e737d49-5b85-42ec-a363-99c695ed108f","FCT-003":"61318dd7-fe4b-41c8-91c0-9b6e542b5c23","FCT-004":"b6dea4f9-56dd-4e95-8643-5acd226db594","FCT-005":"47df2b75-b055-4d69-a218-313fc4a41805"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory note MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory note MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory note MCP 8002
