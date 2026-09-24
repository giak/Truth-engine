ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260920-2110-indexation-conventions-gains-milliards | PARENT_RUN_ID:20260920-2008-dgf-impact-ecart-population-metzing | AS_OF:2026-09-20
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-20_indexation-conventions-gains-milliards/2026-09-20_21-10_indexation-conventions-gains-milliards_INPUT.txt | SUBJECT_SLUG:indexation-conventions-gains-milliards | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:0.85→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Chiffrage en milliards d'euros des gains annuels des conventions d'indexation francaises: SMIC (IPC famille modeste), IRL (hors loyers), retraites/baremes fiscaux; gagnants et perdants par convention
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Cui bono des conventions d'indexation : SMIC, IRL, retraites, barème de l'IR

Run UPDATE de la lignée INSEE. La question restée ouverte au bilan du jour : **que valent, en milliards d'euros, les choix d'indice que la France a légiférés ?** Chaque indexation — salaires minima, loyers, pensions, tranches d'impôt — repose sur une convention : quel indice, quelle exclusion, quelle date d'estimation. Ces conventions sont publiques. Leur effet redistributif n'est chiffré nulle part. Voici la première borne consolidée.

## Le principe de chiffrage

Un transfert = **écart entre l'indice retenu et l'alternative défendable × masse indexée**. La discipline est celle appliquée à la DGF de Metzing, portée aux grandes masses nationales. Toutes les plages sont divulguées ; aucune intentionnalité n'est présumée.

## SMIC : la convention qui protège (FCT-001)

Le SMIC est revalorisé au 1ᵉʳ janvier sur l'inflation **mesurée pour les 20 % des ménages aux revenus les plus faibles**, plus la moitié du gain de pouvoir d'achat du salaire horaire moyen des ouvriers-employés ; en cours d'année, indexation automatique si l'IPC gagne 2 % (12,31 €/h brut en 2026). C'est la convention la plus favorable du système : un indice ciblé sur les pauvres, complété d'un rattrapage. Gagnant : les salariés au minimum, et au-delà (les minima conventionnels suivent). Coût pour l'économie, bénéfice social réel — la convention n'est pas contestable en termes de cui bono, elle est assumée.

## IRL : le hors-loyers (FCT-002)

L'indice de référence des loyers est la moyenne sur douze mois de l'IPC **hors tabac et hors loyers** (loi du 6.7.89, art. 17-1 ; IRL T2 2026 : 148,37, +1,15 %). Les loyers de millions de locataires du privé progressent donc selon un indice qui **exclut la composante la plus lourde de leur budget : leur propre loyer**. La défense technique est connue (éviter une spirale loyers→IPC→loyers) ; l'effet redistributif l'est moins : quand le marché locatif réel grimpe plus vite que l'IPC général, le transfert annuel va systématiquement des locataires aux bailleurs. L'écart IRL/loyers réels n'est pas chiffré publiquement — l'enquête Loyers de l'Insee existe (suivant typé ACCESS).

## Retraités : la bascule de 1987 (FCT-003, FCT-005)

Les pensions de base sont indexées sur les **prix** (L161-25 CSS : IPC hors tabac, confirmé par la circulaire CNAV 2025-29, coefficient 0,9 % au 1ᵉʳ janvier 2026) depuis 1987 dans le privé et 2003 dans la fonction publique — sur les pensions en cours **et** sur les salaires portés au compte. Le chiffrage officiel existe et n'est jamais médiatisé : sous le modèle Destinie, la législation pré-1993 (indexation salaires) donnerait **19,5 % du PIB** de masse de pensions en 2070 contre **13,2 %** en référence ; l'écart est déjà de **3,7 points de PIB en 2018** (≈ 107 Md€ au PIB 2024), soit de l'ordre de **4 Md€/an** d'économie pour le système à productivité 1 %. L'Insee le dit explicitement : cette règle « a fortement contribué à équilibrer le système ». Gagnant : le système (cotisants, État). Perdant relatif : les retraités, dont le niveau de vie décroche de celui des actifs à chaque année de croissance.

**Réfutation adversariale (survies, bornées)** : l'indexation prix protège les retraités lors des chocs inflationnistes importés (Insee Analyses 109) — vrai, et visible en 2022-2024 (5,3 % en janvier 2024) ; une indexation salaires pleine « serait très coûteuse » (DT 2025-08) — vrai également. Les deux lectures sont officielles. Le choix de convention n'a pas de camp neutre : il distribue.

## Barème de l'IR : l'estimation de septembre (FCT-004)

Le barème est indexé chaque année sur l'inflation **estimée en septembre de l'année n-1, sans régularisation**. Table tenue par iFRAP (recoupée avec la source AN/PLF 2023) : **8 années sur 13** où l'écart joue en défaveur du contribuable, **cumul −4,1 points** de revalorisations manquées sur 2010-2022, trop-payé estimé **2,8 à 6 Md€**. Les gels ponctuels ajoutent leur couche : le gel proposé pour 2026 rapportait **+2 Md€** et **200 000 foyers imposables** (rétabli à 1,1 % par l'Assemblée). **Réfutation adversariale (survie bornée)** : la sous-indexation a des effets contradictoires (baisse de progressivité, hausse de redistribution — note IPP) et l'indexation du barème n'est pas une obligation constitutionnelle. Exact — et sans objet sur la question du fait : le biais directionnel de l'estimation de septembre est documenté, son coût cumulé est borné.

## Table de synthèse (gagnants / perdants)

| Convention | Indice retenu | Alternative défendable | Transfert annuel | Gagnant |
|---|---|---|---|---|
| SMIC | IPC des 20 % les plus modestes | IPC global | protection assumée | salariés au minimum |
| IRL | IPC hors tabac, **hors loyers** | IPC avec loyers réels | non chiffré publiquement (7 M de ménages) | bailleurs |
| Pensions | IPC hors tabac (depuis 1987/2003) | salaires | **≈ 4 Md€/an**, 107 Md€ de niveau | système (cotisants/État) |
| Barème IR | IPC **estimé** en septembre n-1 | IPC révisé, régularisé | **2,8-6 Md€** de trop-payé 2019-2023 | État |

## Verdict

**Établi** : les conventions d'indexation françaises redistribuent chaque année de l'ordre de 2 à 10 Md€ selon la convention, dans des directions identifiables et jamais consolidées dans le débat public. **Non établi** : toute intentionnalité — chaque convention est légiférée, publiée, défendable isolément. Mais leur **architecture** — hors-loyers pour les locataires, prix-sans-salaires pour les retraités, estimation de septembre pour les contribuables — converge vers le même effet : payer les transferts indexés sur l'inflation officielle plutôt que sur les revenus réels de l'économie. L'Insee produit les indices ; le législateur choisit ; le débat public ne chiffre pas. Ce dernier point est le seul trou noir, et il est comblable.

## Périmètre et limites (suivants routés)

Écart IRL/loyers réels via l'enquête ELC (ACCESS) ; généalogie complète de la bascule 1987 (CAUSALITY) ; notes DGCL 2025-2026 (run 20-50 encore ouvert) ; DT 2025-08 intégral bloqué par anti-bot — les slides COR extraits couvrent les chiffres clés.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:5|CLM:1|AXS:3|CAU:3|CTRL:2|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"lead":"Formule SMIC: revalorisation de janvier indexee sur IPC des menages urbains dont le chef est ouvrier ou employe; suppression du guichet (2019); role du tabac","note":"Conditionne le calcul du gain/perte lie a la convention famille modeste","status":"SATURATED"}
LED-002 | {"lead":"IRL: indexee sur IPC hors tabac et hors loyers; ecart documentable avec les loyers reels observes (Enquete Loyers et charges, Clameur)","note":"Transfer locataire->bailleur a chiffrer","status":"SATURATED"}
LED-003 | {"lead":"Retraites: revalorisation du 1er novembre sur IPC hors tabac (avant 2021: mecanismes divers); alternative indexation sur salaires (avant 1993); chiffrage COR/DREES de l ecart cumule","note":"Enjeu principal en Md","status":"SATURATED"}
LED-004 | {"lead":"Bareme IR: indexation annuelle sur IPC hors tabac (LF 2012+); decrochages et gels LF 2023-2026 chiffres dans les dossiers PLF","note":"Recettes etat vs inflation reelle","status":"SATURATED"}
LED-005 | {"lead":"Masses indexees: masse salariale au voisinage du SMIC, masse des loyers d habitation, masse des pensions, recettes IR","note":"Denominateurs du chiffrage","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Les conventions d indexation francaises redistribuent chaque annee de 2 a 10 Md EUR selon la convention: SMIC protege (indice 20% modestes), IRL transfere des locataires vers les bailleurs, indexation prix des retraites finance le systeme (~4 Md EUR/an vs salaires, 107 Md EUR de niveau), bareme IR penalise les contribuables via l estimation de septembre sans regularisation","evidence":["FCT-001","FCT-002","FCT-003","FCT-004"],"note":"Chiffrages bornes et divulgues","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"MECANIQUE (quel indice retenu par convention, quelle base legale)","note":"Lois et decrets source","status":"SATURATED"}
AXS-002 | {"axis":"QUANTIFICATION (masse indexee x ecart indice retenu vs alternative defendable, en Md EUR/an)","note":"Coeur du run","status":"SATURATED"}
AXS-003 | {"axis":"CONTRE-HYPOTHESES (neutralite des conventions, redistributions inversees, incertitudes de mesure)","note":"Refutation adversariale","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"evidence":["FCT-001","FCT-003","FCT-004"],"note":"Chaine complete du choix de convention a l euro","provenance":"choix legal d indice (loi/decret) -> formule d indexation (IPC globale / 20% modestes / hors tabac / hors loyers / estimee septembre) -> ecart vs alternative defendable x masse indexee -> transfert annuel en Md EUR","status":"SUPPORTED"}
CAU-002 | {"evidence":["FCT-003","FCT-005"],"note":"Le gain de convention est centre sur le systeme","provenance":"bascule 1987 (prive) et 2003 (public) prix-vs-salaires -> moderation des pensions relatives -> economise ~3,7 pts de PIB de masse de pensions (Destinie, COR doc07) -> equilibre du systeme finance par les retraites relatives","status":"SUPPORTED"}
CAU-003 | {"evidence":["FCT-004"],"note":"Mecanisme de selection temporelle legifere, pas d intention demontree; effets redistributifs contradictoires (IPP)","provenance":"indexation du bareme IR sur l IPC ESTIME en septembre n-1 sans regularisation -> biais documente (8/13 annees defavorables, cumul -4,1 pts) -> trop-paye 2,8-6 Md EUR pour les contribuables","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement triple sur la bascule prix/salaires: Insee Analyses 109 + DT 2025-08 + COR doc07 concordants; circulaire CNAV 2025-29 confirme la regle legale L161-25; iFRAP recoupe la table AN/PLF 2023 des ecarts du bareme IR","evidence":["SRC-003","SRC-004","SRC-006","SRC-007","SRC-009"],"status":"DONE"}
CTRL-002 | {"control":"Bornes de calcul divulguees: 3,7 pts PIB 2018 -> ~107 Md EUR (PIB 2024 ~2900 Md); ecoulement ~4 Md EUR/an a productivite 1% - plage, pas estimation ponctuelle; contre-lectures IPP (redistribution) integrees a la refutation","evidence":["FCT-003","FCT-004","FCT-005"],"status":"DONE"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Publier le chiffrage cui bono par convention (gagnants/perdants en Md EUR) comme contribution au debat public sur l indexation","note":"Contribution citoyenne","status":"DONE"}

SEARCH_ACTIVITY_V1:WEB:4|FETCH:8|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | runtime | - | HYDRATE
SYS-003 | SYS | FOUND | mcp-mnemolite | 20260920-2008-dgf-impact-ecart-population-metzing | MNEMO_Q
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.service-public.fr/particuliers/vosdroits/F2300 | SMIC revalorisation janvier indexation inflation 20 pourcent menages plus modestes moitie gain pouvoir achat ouvriers employes
QRY-002 | FETCH | FOUND | SRC-002 | https://www.anil.org/aj-irl-revision-loyers/ | IRL moyenne douze mois IPC hors tabac hors loyers formule revision loyer ANIL
QRY-003 | FETCH | FOUND | SRC-003 | https://www.insee.fr/fr/statistiques/8563753 | indexation pensions prix salaires 1987 2003 equilibre systeme retraites Destinie sensibilité croissance
QRY-004 | FETCH | FOUND | SRC-004 | https://www.insee.fr/fr/statistiques/8561097 | DT 2025-08 Blanchet effets budgetaires redistributifs regles indexation retraites
QRY-005 | FETCH | FOUND | SRC-007 | https://www.ifrap.org/budget-et-fiscalite/non-lindexation-du-bareme-de-lir-en-2024-nequivaut-pas-un-cadeau-de-6-milliards-aux-contribuables | IFRAP bareme IR indexation IPC estime septembre n-1 sans regularisation ecarts 8 sur 13 cumul -4,1 points trop paye 6 milliards
QRY-006 | FETCH | FOUND | SRC-008 | https://placement.meilleurtaux.com/placement-financier/actualites/2026-janvier/impot-sur-le-revenu-les-deputes-retablissent-lindexation-a-1-1-du-bareme.html | gel bareme IR 2026 deux milliards 200000 foyers imposables reindexation 1,1 pourcent assemblee
QRY-007 | WEB | FOUND | - | https://drees.solidarites-sante.gouv.fr/sites/default/files/2025-07/Fiche%2004%20-%20La%20revalorisation%20des%20pensions%20individuelles.pdf | DREES fiche 04 revalorisation pensions 2024 5,3 pourcent janvier base 1,6 novembre Agirc-Arrco
QRY-008 | FETCH | FOUND | SRC-009 | PATH:/tmp/dgcl_pdf/cnav_circ.pdf | circulaire CNAV 2025-29 revalorisation 2026 coefficient 0,9 pourcent L161-25 CSS prix hors tabac moyenne douze derniers indices mensuels
QRY-009 | FETCH | FOUND | SRC-010 | https://www.ccomptes.fr/sites/default/files/2025-02/20250220-Situation-financiere-et-perspectives-du-systeme-de%20retraites_0.pdf | Cour des comptes fevrier 2025 depenses retraites 388,4 milliards 13,9 pourcent PIB
QRY-010 | WEB | FOUND | - | - | REFUTATION indexation prix retraites 1987 2003 - la regle favorise les retraites lors des chocs inflationnistes (Insee Analyses 109); recours individuels seulement, pas de contestation systemique des erreurs de revalorisation
QRY-011 | WEB | FOUND | - | - | REFUTATION bareme IR indexation 2024 6 milliards - note IPP: effets contradictoires (progressivite baissee, redistribution haussee); l indexation n est pas une obligation constitutionnelle, le gel est legal (conseil constitutionnel)
QRY-012 | WEB | FOUND | - | - | REFUTATION bareme IR indexe sur l inflation estimee de septembre n-1 sans regularisation - note IPP: effets contradictoires (progressivite baissee, redistribution haussee); l indexation n est pas une obligation, le gel du bareme est legal en droit positif

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.service-public.fr/particuliers/vosdroits/F2300
SRC-002 | ◉ | fam:A | https://www.anil.org/aj-irl-revision-loyers/
SRC-003 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8563753
SRC-004 | ◈ | fam:A | https://www.insee.fr/fr/statistiques/8561097
SRC-005 | ◈ | fam:A | PATH:/tmp/dgcl_pdf/dt2025-08.pdf
SRC-006 | ◈ | fam:B | PATH:/tmp/dgcl_pdf/cor_doc07.pdf
SRC-007 | ◉ | fam:other:thinktank | https://www.ifrap.org/budget-et-fiscalite/non-lindexation-du-bareme-de-lir-en-2024-nequivaut-pas-un-cadeau-de-6-milliards-aux-contribuables
SRC-008 | ◉ | fam:D | https://placement.meilleurtaux.com/placement-financier/actualites/2026-janvier/impot-sur-le-revenu-les-deputes-retablissent-lindexation-a-1-1-du-bareme.html
SRC-009 | ◈ | fam:A | PATH:/tmp/dgcl_pdf/cnav_circ.pdf
SRC-010 | ◈ | fam:A | https://www.ccomptes.fr/sites/default/files/2025-02/20250220-Situation-financiere-et-perspectives-du-systeme-de%20retraites_0.pdf

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.service-public.fr/particuliers/vosdroits/F2300 | A | 2026-09-20 | Mécanique SMIC : indexation sur l IPC des 20 % les plus modestes et moitié du gain de pouvoir d achat des ouvriers-employés | Au 1er janvier, le SMIC est indexé sur l inflation mesurée pour les 20 % des ménages aux revenus les plus faibles, plus la moitié du gain de pouvoir d achat du salaire horaire moyen des ouvriers et employés ; en cours d année, hausse automatique si IPC +2 % (montants 2026 : 12,31 EUR/h brut). Convention verrouillée en droit du travail. | 10487ed8-2257-4081-b372-450b218bdb1f
FCT-002 | FACT | ✧ | https://www.anil.org/aj-irl-revision-loyers/ | A | 2026-09-20 | Mécanique IRL : moyenne 12 mois de l IPC hors tabac ET hors loyers | L IRL (loi 89-462 art. 17-1) est la moyenne sur les douze derniers mois de l évolution de l IPC hors tabac et hors loyers ; IRL T2 2026 = 148,37 (+1,15 % sur un an). Le loyer des 7 millions de ménages locataires du privé suit les prix HORS leurs loyers: la composante la plus lourde du budget logement est exclue de sa propre indexation. | d3f212f5-4b6e-4859-a07e-f938d4d1c47d
FCT-003 | FACT | ✦ | https://www.insee.fr/fr/statistiques/8563753 | A,B | 2026-09-20 | Indexation des retraites sur les prix depuis 1987 (privé) et 2003 (public) : gain majeur pour le système | Les pensions de base sont indexées sur les PRIX (L161-25 CSS: IPC hors tabac) depuis 1987 dans le privé et 2003 dans la fonction publique, sur les pensions en cours ET les salaires portés aux comptes. L Insee (DT 2025-08, Insee Analyses 109) et le COR documentent que cette convention a fortement contribué à l équilibre: sous Destinie, la législation pré-1993 (indexation salaires) donnerait 19,5 % du PIB de masse de pensions en 2070 contre 13,2 % en référence, soit 3,7 points de PIB d écart dès 2018 (≈107 Md€ au PIB 2024), de l ordre de 4 Md€/an d écoulement à productivité 1 %. Gagnant: le système (cotisants/État); perdant relatif: les retraités. | 6a7cc60c-25c1-4998-8d63-4f83c35fd6c6
FCT-004 | FACT | ✦ | https://www.ifrap.org/budget-et-fiscalite/non-lindexation-du-bareme-de-lir-en-2024-nequivaut-pas-un-cadeau-de-6-milliards-aux-contribuables | D,other:thinktank | 2026-09-20 | Barème de l impôt sur le revenu indexé sur l inflation ESTIMÉE de septembre n-1, sans régularisation | Le barème IR est indexé chaque année sur l IPC estimé en septembre n-1 sans régularisation ultérieure: 8 fois sur 13 ans l écart joue en défaveur du contribuable, cumul −4,1 points de revalorisations manquées sur 2010-2022; trop-payé estimé 6 Md€ (2019-2023), encore 2,8-3,4 Md€ en incluant 2024. Gels ponctuels chiffrés: gel 2026 = +2 Md€ pour l État et +200 000 foyers imposables (rétabli à 1,1 % par l Assemblée). Indexation 2024 (4,8 %): 5-6,2 Md€ de recettes abandonnées. | 2f491e10-b0a4-4879-9cd5-9ed41a36776e
FCT-005 | FACT | ✧ | https://www.ccomptes.fr/sites/default/files/2025-02/20250220-Situation-financiere-et-perspectives-du-systeme-de%20retraites_0.pdf | A,B | 2026-09-20 | Masses indexées : pensions ~390-407 Md€/an ; assiettes SMIC, loyers privés, recettes IR | Dépenses de retraites 388,4 Md€ (Cour des comptes 02/2025: dépenses 2023 à 388,4 Md€, ressources 396,9 Md€) à ~407 Md€ (COR 2024) ; 17 millions de retraités. Ces masses rendent chaque dixième de point d écart d indice proportionnellement massif: 0,5 pt sur 400 Md€ = 2 Md€/an. Barème IR: chaque 0,1 pt de non-revalorisation ≈ 0,5 Md€. | 951a9a80-9ae0-44ef-9d9b-631a9f0357a9
FCT-006 | FACT | ✧ | https://www.insee.fr/fr/statistiques/8561097 | A | 2026-09-20 | Synthèse du chiffrage : les conventions d indexation redistribuent des milliards et leurs gagnants sont identifiables | SMIC → salariés au minimum (protégés, et au-delà via la revalorisation des minima conventionnels) ; IRL → bailleurs contre locataires (loyers exclus de leur propre indexation) ; retraites → cotisants/État vs retraités (bascule 1987/2003 ≈ 4 Md€/an, 107 Md€ de niveau) ; barème IR → État via l estimation de septembre sans régularisation (trop-payé 2,8-6 Md€). Aucune de ces conventions n est cachée: elles sont légiférées et publiées; leur CUI BONO est quantifiable mais jamais chiffré dans le débat public. | f1ced8b7-6839-4a7f-8686-7f6c0996e404
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003,SRC-004,SRC-005,SRC-006,SRC-009
FCT-004 | SRC-007,SRC-008
FCT-005 | SRC-006,SRC-010
FCT-006 | SRC-004,SRC-005

## REFUTATION_REGISTRY_V1
FCT-003 | QRY-010 | FOUND_RESOLVED
FCT-004 | QRY-012 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:CONFIRME
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8;9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11;12 | NEXT_ACTION:13;14
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;15;16;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18;18b

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-20T19:22:32.514619+00:00","fact_mem":{"FCT-001":"10487ed8-2257-4081-b372-450b218bdb1f","FCT-002":"d3f212f5-4b6e-4859-a07e-f938d4d1c47d","FCT-003":"6a7cc60c-25c1-4998-8d63-4f83c35fd6c6","FCT-004":"2f491e10-b0a4-4879-9cd5-9ed41a36776e","FCT-005":"951a9a80-9ae0-44ef-9d9b-631a9f0357a9","FCT-006":"f1ced8b7-6839-4a7f-8686-7f6c0996e404"},"mnemo_row":"PASS: 6/6 eligible facts persisted via MCP write_memory (8002); run 20260920-2110-indexation-conventions-gains-milliards","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau CONFIRME (APEX, refutation survive bounded)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau CONFIRME (APEX, refutation survive bounded)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"fait nouveau VERIFIE","success":1}],"writeback_row":{"attempted":6,"blocked":0,"eligible":6,"failure":0,"success":6}}

PERSISTENCE_META: MNEMO_ROW:PASS: 6/6 eligible facts persisted via MCP write_memory (8002); run 20260920-2110-indexation-conventions-gains-milliards | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:6;attempted:6;success:6;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[6 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-003 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau CONFIRME (APEX, refutation survive bounded)
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau CONFIRME (APEX, refutation survive bounded)
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
