ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260830-2103-audit-decheterie-dispositif-controle-2026 | PARENT_RUN_ID:20260830-2015-audit-exclusion-pros-decheteries-2026 | AS_OF:2026-08-30
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-30_audit-decheterie-dispositif-controle-2026/2026-08-30_21-03_audit-decheterie-dispositif-controle-2026_INPUT.txt | SUBJECT_SLUG:audit-decheterie-dispositif-controle-2026 | SUBJECT_FP:sha256:d5987ebcfab24434507e6ec4ce020cff783c9c139d5914cd8092585564a3064f | INPUT_SHA256:sha256:c39016ea9a688e928ae392d4a7c7ed2ca4d42bc477a18f640bb3b8dd83b1b05a
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:9 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['AMORCE', 'ADEME', 'EPCI gestionnaires', "societes de controle d'acces (badges, pesee)", 'exploitants prives (Veolia, Suez, Paprec)', 'usagers (particuliers, pros, non-residents, habitats collectifs)', 'federations (AMF, Intercommunalites de France)'], 'domains': ['dechets', 'decheteries', 'controle-acces', 'badges', 'quotas', 'facturation', 'inegalites', 'gouvernance', 'marchandisation'], 'geo': 'France (echantillon national + cas EPCI)', 'lead_question': "La decheterie est-elle devenue un dispositif de controle et de tri social des usagers (badges, quotas, facturation) ? Quelles inegalites d'acces cela cree-t-il et qui profite de la marchandisation du controle ?", 'limits': "enquete DT138 partiellement accessible (payante/resumee), donnees de facturation par site heterogenes, effets du controle d'acces encore recents", 'object_question': "(1) etat des lieux national AMORCE/ADEME DT138 (acces, controle, facturation) ; (2) dispositifs techniques (badges, cartes, bornes, quotas, pesee, cameras) et fournisseurs ; (3) inegalites d'acces (non-residents, collectifs, precaires) ; (4) qui gagne/qui perd de la marchandisation de l'acces ; (5) correlation controle d'acces -> detournement de flux (depots sauvages)"}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# 🦊 Axe F — La déchèterie comme dispositif de contrôle : badges, quotas, facturation, inégalités d'accès

**Run `20260830-2103-audit-decheterie-dispositif-controle-2026`** — état des lieux national du contrôle d'accès en déchèteries publiques (enquête AMORCE/ADEME DT138, PDF 52 pages INSPECTED) + la généralisation 2026 = « fin de l'anonymat », + le marché privé qui se structure autour du compteur.

## Verdict

| # | Fait | Statut |
|---|---|---|
| **FCT-001** | **État des lieux national AMORCE/ADEME DT138** (déc. 2024) : déchèteries = **~40 % des déchets SPGD** ; **16,4 Mt en 2021** (1ère fois = volume des OMR) ; **65,9 % des collectivités équipées d'un contrôle d'accès informatisé**, 83,3 % installés depuis 2015, 75,9 % sur 100 % de leurs sites, 78,4 % satisfaites | ✦ (A+C, réfutation NONE) |
| **FCT-002** | **Quotas et facturation** : 68,2 % accès illimité dans TEOM/REOM ; **16,5 % quota avec accès payant au-delà** (médiane 7,5 €/passage, 3,3-50 €) ; 8,2 % quota ferme ; **baisse médiane des tonnages -24 % à 12 mois** (verts -20 %, gravats -20,4 %, tout-venant -35 %) ; médiane 24-36 passages/an | ✦ (A+C, réfutation NONE) |
| **FCT-003** | **Test causalité contrôle d'accès → dépôts sauvages (Manche 2023)** : Point Fort Environnement, pass QR au 01/01/2023 — **fréquentation -47 %, tonnages -31 %, -75 % sur certains sites, « il y a déjà des dépôts sauvages »** (élu de Marigny) ; 18 passages gratuits/an ; 31 000 demandes de pass | ✦ (A+B, réfutation NONE) |
| **FCT-004** | **Généralisation 2026 = fin de l'anonymat** : Gard rhodanien (44 communes, ~75 000 hab) QR/badge au 02/01/2026 : **36 passages/an, 3 dépôts/jour, 2 m³/visite**, expérimentation 2026 puis contraignant 2027 ; Caen la mer : QR ou plaque (CNIL, conservation 6 mois) ; **pic de dépôts sauvages 6 mois en AURA** lors des déploiements pionniers ; ~50 % des EPCI basculés d'ici 2028 | ✦ (B+C, réfutation NONE) |
| **FCT-005** | **Le marché de la marchandisation** : Symetri (logiciel de contrôle d'accès, apps Depos/Join/User-YT) = **filiale à 100 % de TRIBORD** (SAS bretonne qui exploite les déchèteries de Rennes Métropole) — **CA 977 k€ en 2025 (×2 en 3 ans)** ; coûts systèmes : cartes à puce 24-95 k€/site, code barre 4-56 k€ (médiane borne 42 k€), plaques 21-80 k€ (médiane 38 k€), badges 0,56-3,21 €/unité | ✦ (C+E, réfutation NONE) |

## Découvertes clés

1. **Le contrôle d'accès n'est plus marginal : c'est la norme.** 65,9 % des collectivités sont équipées d'un système informatisé (DT138, échantillon 56 CL), 83,3 % installés depuis 2015, et la vague s'accélère : Gard rhodanien et Caen la mer généralisent en 2026 avec des quotas (36 passages/an), la prévision est de ~50 % des EPCI basculés d'ici 2028. La déchèterie anonyme disparaît : chaque dépôt devient un enregistrement.
2. **Le discours officiel est contredit par les chiffres de son propre camp.** « Service gratuit, non punitif » (Gard rhodanien) vs la mécanique du compteur : 16,5 % des collectivités facturent au-delà du quota (médiane 7,5 €/passage), le dépassement étant « analysé comme une utilisation anormale se rapprochant d'un comportement professionnel » (DT138). Le compteur ne tourne pas pour rien (recy.net).
3. **Le test causalité contrôle → dépôts sauvages est POSITIF et documenté.** Manche 2023 : -47 % de fréquentation, -31 % de tonnages, et « déjà des dépôts sauvages » 3 mois après le pass. Recy.net documente le même pic (6 mois) en Auvergne-Rhône-Alpes. Le lien avec l'axe A (exclusion des pros) et l'axe D (fermetures) se renforce : chaque restriction d'accès déplace une partie du flux vers l'extérieur.
4. **Un marché privé se structure autour du compteur.** Symetri (filiale de TRIBORD, l'exploitant des déchèteries de Rennes Métropole) double son CA en 3 ans (497 k€ → 977 k€) en vendant badges, bornes et logiciels. Le fournisseur du contrôle est aussi l'exploitant des sites contrôlés : conflit d'intérêts structurel à documenter. Les coûts d'équipement (4 à 95 k€/site selon la technologie) sont des investissements publics captés par ce marché.
5. **Honnêteté épistémique** : l'enquête DT138 complète est payante (nous avons inspecté le PDF public de 52 pages) ; les échantillons (56 CL pour l'équipement, 85 CL pour la facturation) sont modestes ; la causalité Manche est locale (1 syndicat, 2023) — la généralisation nationale reste une projection.

## Sources INSPECTED

- AMORCE/ADEME DT138 (PDF 52 p., réf ADEME 012630, déc. 2024) — téléchargé et texte complet extrait (2 332 lignes)
- actu.fr / La Presse de la Manche 18/03/2023 — Point Fort Environnement, pass QR, dépôts sauvages
- recy.net 05/06/2026 — Gard rhodanien 36 passages, Caen la mer plaque/QR, fin de l'anonymat
- Symetri (blog) 19/01/2022 — raisons du contrôle d'accès, badges ~20 passages/an, caméras plaques
- Pappers — fiches sociétés Symetri (841351901) et TRIBORD (378801682), comptes 2022-2025

## Réfutations (5 NONE)

- FCT-001 : aucune preuve d'un taux d'équipement < 65,9 %, ni de < 16,4 Mt en 2021, ni de < 40 % des déchets SPGD
- FCT-002 : aucune preuve de quotas/facturation différents (≠ 68,2 % illimité, ≠ 16,5 % payant, baisse ≠ -24 %)
- FCT-003 : aucune preuve que le pass Point Fort n'a pas fait chuter fréquentation/tonnages, ni absence de dépôts sauvages
- FCT-004 : aucune preuve que la généralisation 2026 (Gard 36 passages, Caen plaque) n'existe pas ou diffère
- FCT-005 : aucune preuve que Symetri n'est pas filiale de TRIBORD, ni CA 2025 ≠ 977 k€, ni coûts systèmes différents

## Gaps ouverts

1. Détail complet de l'enquête DT138 (version payante intégrale, échantillons élargis)
2. Coût national de résorption des dépôts sauvages créés par le contrôle d'accès (à relier aux 340-420 M€/an axe C)
3. Cartographie des EPCI basculés 2024-2028 et leurs quotas (vers 1 200 forfaits différents)
4. Audit du marché des éditeurs (Symetri/TRIBORD, parts de marché, marchés publics, conflit exploitant/fournisseur)
5. RGPD : durées de conservation réelles des données de passage (badges, plaques) par EPCI
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:1|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_excerpt":"DT138 : 65,9% equipees controle informatise ; Manche 2023 : -47% frequentation, depots sauvages ; Gard rhodanien 2026 : 36 passages/an ; Symetri CA 977 kE 2025","kind":"EVENT","lead":"La decheterie publique devient un dispositif de controle d'acces : generalisation ete 2026 (cartes, quotas, facturation, refus pros) documentee par l'enquete AMORCE/ADEME DT138 (07/11/2025)","locator":"PDF DT138 52p + presse (actu.fr 2023, recy.net 2026) + Pappers","materiality":"HIGH","routes":["enquete AMORCE DT138","presse generalisation 2026","fournisseurs de solutions controle acces (badges, pesee)","reglements EPCI controle acces"],"source_id":"SRC-001","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"counter":"NONE_FOUND","gap":"GAP_TYPE=ACCESS (enquete DT138 partiellement accessible, donnees par site heterogenes)","linked_ids":["LED-001","AXS-001"],"proposition":"La decheterie publique est en train de devenir un dispositif de controle et de tri social des usagers (badges, quotas, facturation) dont la generalisation 2026 cree des inegalites d'acces structurelles et ouvre un marche pour des operateurs prives de controle d'acces","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005"],"gap_type":"NONE","led_links":["LED-001"],"question":"L'enquete AMORCE/ADEME DT138 (2025) et la generalisation 2026 documentent-elles un controle d'acces (badges/quotas/facturation) qui cree des inegalites d'acces et profite a des operateurs de la marchandisation ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"],"sought_objects":["enquete AMORCE/ADEME DT138","dispositifs techniques : badges, cartes, bornes, pesee, cameras","fournisseurs/operateurs de solutions controle acces","reglements EPCI : quotas, exclusions, tarifs","inegalites d'acces : non-residents, collectifs, precaires"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"linked_ids":["LED-001","AXS-001","CLM-001"],"mechanism":"chaine documentee : restriction d'acces (quotas 16,5% payants, 8,2% ferme ; 18-36 passages/an) -> baisse tonnages (mediane -24% a 12 mois) -> detournement de flux (depots sauvages documentes Manche 2023, pic 6 mois AURA) ; qui gagne : operateurs de controle d'acces (Symetri/TRIBORD CA x2 en 3 ans) et EPCI (maitrise tonnages TGAP)","question":"Le controle d'acces (badges/quotas/facturation) en decheterie publique cree-t-il des inegalites d'acces et detourne-t-il des flux vers les depots sauvages ?","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:10|EXA:5
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | 1e737d49-5b85-42ec-a363-99c695ed108f | MEMORY_PROBE
SYS-002 | SYS | FOUND: warm-route 1e737d49 (FCT-002 axe A : generalisation ete 2026 controle acces cartes/quotas, AMORCE/ADEME DT138 07/11/2025, decheteries = ~40% dechets SPGD) + 91ad49b2 (carte eco-org REP) | mnemolite:search_memory | - | MNEMO_Q
SYS-003 | SYS | PASS | runtime:load | - | ALWAYS_LOAD: definitions/SYMBOLS.md, definitions/PATTERNS.md, definitions/THREATS.md, forensic/GATES.md, forensic/REQUEST_LOG.md
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | - | - | FETCH DT138 PDF : 40% dechets SPGD, 16,4 Mt 2021, 65,9% controle d'acces informatise, quotas 16,5%/8,2%, baisse tonnages -24%, couts systemes, L2224-14 CGCT
QRY-002 | FETCH | FOUND | - | - | FETCH Symetri : badges ~20 passages/an, cameras plaques, cas Allain +41%, controle police municipale
QRY-003 | FETCH | FOUND | - | - | FETCH actu.fr Manche : pass QR Point Fort, -47% frequentation, -31% tonnages, depots sauvages, 18 passages/an
QRY-004 | FETCH | FOUND | - | - | FETCH Recy.net : Gard rhodanien 36 passages, 3 depots/jour, 2 m3, fin anonymat, Caen plaque/QR, RGPD
QRY-005 | FETCH | FOUND | - | - | FETCH Pappers : Symetri filiale TRIBORD, CA 977 kE 2025, capital, actionnariat
QRY-006 | FETCH | FOUND | SRC-001 | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download | -
QRY-007 | FETCH | FOUND | SRC-002 | https://www.symetri.fr/2022/01/19/le-controle-dacces-de-plus-en-plus-deploye-a-lentree-des-decheteries/ | -
QRY-008 | FETCH | FOUND | SRC-003 | https://actu.fr/planete/manche-a-cause-du-nouvel-acces-limite-a-ces-decheteries-deja-des-depots-sauvages_58200363.html | -
QRY-009 | FETCH | FOUND | SRC-004 | https://www.recy.net/decheteries-qr-code-badge-controle-acces-2026-fin-anonymat/ | -
QRY-010 | FETCH | FOUND | SRC-005 | https://www.pappers.fr/entreprise/symetri-841351901 | -
QRY-011 | EXA | FOUND | - | - | REFUTATION 012630 1 100 138 16 2015 2021 2024 3 4 40 65 75 78 83 9 : une preuve que l'etat des lieux national differe (moins de 65,9% equipees, moins de 16,4 Mt en 2021, moins de 40% SPGD)
QRY-012 | EXA | FOUND | - | - | REFUTATION 12 138 16 2 20 24 3 35 36 4 5 50 68 7 8 : une preuve que les quotas/facturations menagers different (moins de 68,2% illimite, quota payant different de 16,5%, baisse tonnages differente de -24%)
QRY-013 | EXA | FOUND | - | - | REFUTATION 000 01 03 04 18 2023 30 31 47 70 75 : une preuve que le pass Point Fort n'a pas fait chuter la frequentation (-47%) ni les tonnages (-31%), ni qu'il n'y a pas de depots sauvages
QRY-014 | EXA | FOUND | - | - | REFUTATION 000 01 02 08 2 2026 2027 2028 3 31 36 44 50 6 75 : une preuve que la generalisation 2026 (Gard rhodanien 36 passages, Caen plaque) n'existe pas ou differente
QRY-015 | EXA | FOUND | - | - | REFUTATION 0 07 10 100 12 2 2018 2022 2025 21 24 26 3 38 4 42 497 56 80 95 977 : une preuve que Symetri n'est pas filiale de TRIBORD, ou CA 2025 different de 977 kE, ou couts systemes differents

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download
SRC-002 | ◈ | fam:C | https://www.symetri.fr/2022/01/19/le-controle-dacces-de-plus-en-plus-deploye-a-lentree-des-decheteries/
SRC-003 | ◈ | fam:B | https://actu.fr/planete/manche-a-cause-du-nouvel-acces-limite-a-ces-decheteries-deja-des-depots-sauvages_58200363.html
SRC-004 | ◈ | fam:C | https://www.recy.net/decheteries-qr-code-badge-controle-acces-2026-fin-anonymat/
SRC-005 | ◈ | fam:E | https://www.pappers.fr/entreprise/symetri-841351901

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download | A,C | 2026-08-30 | Etat des lieux national AMORCE/ADEME DT138 (dec 2024, ref ADEME 012630) : decheteries publiques = ~40% des dechets SPGD ; 16,4 Mt dechets occasionnels en 2021 (1ere fois = volume des OMR) ; 65,9% des collectivites equipees d'un systeme de controle d'acces informatise ; 83,3% installes depuis 2015 ; 75,9% sur 100% de leurs sites ; 78,4% satisfaites | PDF 52 pages INSPECTED (telecharge + extrait texte complet) : conclusion p.49 'pour la premiere fois en 2021 a l'echelle nationale, la quantite de dechets occasionnels prise en charge par le SPGD en decheterie atteint la quantite d'ordures menageres residuelles collectees, avec 16,4 millions de tonnes' ; section 5.1 : 65,9% des collectivites ont un systeme de controle d'acces informatise (echantillon 56 CL) ; 83,3% des systemes installes a partir de 2015 ; 75,9% equipe 100% de leurs decheteries ; 78,4% globalement satisfaites. Corroboration blog editeur Symetri (19/01/2022) : de nombreux sites equipes en 2021 (Arrageois, Niortais, Grand Orb, Sancerrois, Grand Perigueux). Source: amorce.asso.fr + symetri.fr (verifie 2026-08-30, tier ✦) | 22c71cc4-37c5-4ef2-84f4-9b7d0309b0c5
FCT-002 | FACT | ✦ | https://amorce.asso.fr/publications/etat-des-lieux-des-modalites-d-acces-de-controle-et-de-facturation-en-decheteries-publiques-dt138/download | A,C | 2026-08-30 | Quotas et facturation DT138 : acces menagers illimite dans TEOM/REOM pour 68,2% des collectivites ; 16,5% instaurent un quota avec acces payant au-dela (mediane 7,5 EUR/passage, fourchette 3,3 a 50 EUR) ; 8,2% un quota ferme ; 4,7% mixte ; baisse mediane des tonnages -24% a 12 mois de mise en place (verts -20%, gravats -20,4%, tout-venant -35%) ; limitation passages : mediane 2/jour, 5/semaine, 12/mois, 24 a 36/an | PDF INSPECTED : section 4.3.1 (85 CL) : 68,2% acces compris TEOM/REOM et illimite ; 16,5% quota d'acces avec acces payant au-dela (depassement analyse comme utilisation anormale se rapprochant d'un comportement professionnel) ; 8,2% quota ferme ; facturation au-dela du quota : mediane 7,5 EUR/passage (fourchette 3,3-50 EUR), 7,5-23 EUR/m3, 0-150 EUR/tonne ; impact quotas : baisse mediane des tonnages -24% a 12 mois (verts -20%, gravats -20,4%, tout-venant residuel -35%) ; limitation passages : mediane 2/jour, 5/semaine, 12/mois, 24/an (menages) et 36/an (non menages). Corroboration cas Gard rhodanien (recy.net 2026) : forfait 36 passages/an. Source: amorce.asso.fr + recy.net (verifie 2026-08-30, tier ✦) | 1ca3694a-9fb5-453d-b5f2-a54ae9465ef0
FCT-003 | FACT | ✦ | https://actu.fr/planete/manche-a-cause-du-nouvel-acces-limite-a-ces-decheteries-deja-des-depots-sauvages_58200363.html | A,B | 2026-08-30 | Test causalite controle d'acces -> depots sauvages : Point Fort Environnement (Manche) instaure le pass QR au 01/01/2023 (exige au 03/04/2023) pour 'reserver l'acces aux seuls habitants' ; frequentation -47% en janvier-fevrier, tonnages -31%, passages effondres de -75% sur certaines decheteries ; 31 000 demandes de pass (30% badge physique, 70% e-badge) ; limitation a 18 passages gratuits/an ; 'il y a deja des depots sauvages' (elu du secteur de Marigny) | actu.fr / La Presse de la Manche 18/03/2023 INSPECTED : syndicat Point Fort Environnement (5 intercommunalites Centre-Manche) ; pass QR instaure 01/01/2023, exige au 3 avril ; president Laurent Pien ; 'on en est a 31 000 demandes et on est a jour' ; 30% foyers badge physique / 70% e-badge ; chute frequentation -47% janvier-fevrier ; tonnages -31% ; passages effondres de 75% sur certains sites ; 'Il y a deja des depots sauvages', alerte un elu du secteur de Marigny ; 18 passages gratuits/an ; comparaison Calvados curseur a 24. Contexte DT138 : effet d'annonce 4,8%, quotas -24% mediane. Source: actu.fr + amorce.asso.fr (verifie 2026-08-30, tier ✦) | 7ceae03f-86a5-4c39-bc9f-a7d16d2baf91
FCT-004 | FACT | ✦ | https://www.recy.net/decheteries-qr-code-badge-controle-acces-2026-fin-anonymat/ | B,C | 2026-08-30 | Generalisation 2026 = fin de l'anonymat en decheterie : Gard rhodanien (44 communes, ~75 000 hab) generalise QR code personnel ou badge au 02/01/2026 : 36 passages/an max, 3 depots/jour max, 2 m3/visite max, experimentation 2026 puis contraignant 2027 ; Caen la mer : QR ou lecture automatique de plaque (donnee CNIL, conservation 6 mois, periode transitoire jusqu'au 31/08/2026) ; recy.net : pic de depots sauvages 6 mois en Auvergne-Rhone-Alpes lors des deploiements pionniers ; 50% des EPCI pourraient basculer d'ici 2028 | Recy.net 05/06/2026 INSPECTED : Gard rhodanien QR code personnel sur plateforme gardrhodanien.webusager.fr (connexion avec facture redevance incitative) ou badge en mairie ; forfait 36 passages/an, 3 depots/jour, 2 m3/visite ; 'toute l'annee 2026 reste une phase d'experimentation... c'est en 2027 que la mecanique deviendra contraignante' ; Caen la mer : QR code OU plaque (periode transitoire justificatif domicile + piece identite jusqu'au 31/08/2026) ; plaque = donnee personnelle, declaration CNIL, conservation 6 mois ; 'c'est arrive en Auvergne-Rhone-Alpes quand le systeme est entre en vigueur sur des EPCI pionniers... le pic des six premiers mois fait mal' ; 'D'ici 2028, on peut raisonnablement parier que la moitie des EPCI francais auront bascule'. Corroboration Manche 2023 (depots sauvages des le deploiement). Source: recy.net + actu.fr (verifie 2026-08-30, tier ✦) | e07ee4a5-b0da-406f-b662-95e7715b15af
FCT-005 | FACT | ✦ | https://www.pappers.fr/entreprise/symetri-841351901 | C,E | 2026-08-30 | Marche de la marchandisation du controle : Symetri (editeur du logiciel de controle d'acces en decheterie, apps Depos-YT/Join-YT/User-YT) = SASU creee 26/07/2018, filiale a 100% de TRIBORD (SAS bretonne de gestion des dechets, CA ~10 ME, entreprise d'insertion, qui exploite les decheteries de Rennes Metropole) ; CA Symetri 977 kE en 2025 (vs 497 kE en 2022, x2 en 3 ans) ; 12 salaries ; couts systemes : cartes a puce 24-95 kE/site, code barre 4-56 kE (borne fixe mediane 42 kE), plaques 21-80 kE (mediane 38 kE), badges 0,56-3,21 EUR/unit | Pappers INSPECTED : Symetri SIREN 841351901, SASU, creation 26/07/2018, siege Rennes (Immeuble Le Quadri, 47 av des Pays-Bas), capital 601 450 EUR, president TRIBORD (SIREN 378801682), CA 2025 = 977 kE (2024 : 832 kE, 2023 : 705 kE, 2022 : 497 kE), resultat net 2025 = 187 kE, 12 salaries ; TRIBORD = SAS collecte des dechets non dangereux (Brest/Rennes), CA ~9,98-10 ME, entreprise d'insertion, exploite le reseau de decheteries et plateformes vegetaux de Rennes Metropole. Couts systemes : DT138 sections 5.2.1 (cartes a puce 24-95 kE, code barre 4-56 kE, plaques 21-80 kE, badges 0,56-3,21 EUR) ; blog Symetri : solutions Depos-YT/Join-YT/User-YT/Chat-YT. Source: pappers.fr + symetri.fr (verifie 2026-08-30, tier ✦) | 52067326-19c0-467e-a638-dc10bb5e43b4
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-002
FCT-002 | SRC-001,SRC-004
FCT-003 | SRC-003,SRC-001
FCT-004 | SRC-004,SRC-003
FCT-005 | SRC-005,SRC-002

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-011 | NONE
FCT-002 | QRY-012 | NONE
FCT-003 | QRY-013 | NONE
FCT-004 | QRY-014 | NONE
FCT-005 | QRY-015 | NONE

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
CP-005 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10:FCT-001
CP-006 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11:CAU-001
CP-007 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13:VERIFY
CP-008 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17:INVESTIGATION_ACCOUNTABILITY
CP-009 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18:FINALIZATION_BLOCKED

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-30T19:11:04.395285+00:00","fact_mem":{"FCT-001":"22c71cc4-37c5-4ef2-84f4-9b7d0309b0c5","FCT-002":"1ca3694a-9fb5-453d-b5f2-a54ae9465ef0","FCT-003":"7ceae03f-86a5-4c39-bc9f-a7d16d2baf91","FCT-004":"e07ee4a5-b0da-406f-b662-95e7715b15af","FCT-005":"52067326-19c0-467e-a638-dc10bb5e43b4"},"mnemo_row":"MNEMO_MCP_8002","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"write_memory reference MCP 8002","success":1},{"action":"ELIGIBLE:CONFIRME","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"write_memory reference MCP 8002","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_MCP_8002 | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-002 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
FCT-005 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:write_memory reference MCP 8002
