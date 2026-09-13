ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260831-1119-audit-tweets-verrou-poubelles | PARENT_RUN_ID:NONE | AS_OF:2026-08-31
INPUT_KIND:NEW | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-08/2026-08-31_audit-tweets-verrou-poubelles/2026-08-31_11-19_audit-tweets-verrou-poubelles_INPUT.txt | SUBJECT_SLUG:audit-tweets-verrou-poubelles | SUBJECT_FP:sha256:42216a984b0f4436aff9afc00a0392bd7f01a3a1b38fabdd9f3c189af71e928b | INPUT_SHA256:sha256:0fbf540a119fc53c107bd804ae6daf4c151e320d9987b97fd65b96f5dce9c7b2
COMPLEXITY:0.6→MEDIUM | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors': ['Vendee Grand Littoral', 'Ville de Paris', 'Marseille', 'EPCI Oise', 'Emmanuel Gregoire', 'TF1', 'France Inter'], 'domains': ['dechets', 'tweets', 'redevance incitative', 'controle acces', 'depots sauvages', 'corruption', 'police tri'], 'geo': 'France (Vendee, Marseille, Paris, Oise)', 'lead_question': 'Les phenomenes decrits par les 5 tweets correspondent-ils a des faits documentes ou relevent-ils de la rumeur ?', 'limits': 'tweets = signaux T5; source officielle VGL balance le recit depots sauvages; pas de serie nationale', 'object_question': '(1) source primaire par lead ; (2) coherence avec passes certifiees ; (3) fait verifie vs signal non confirme.'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Cinq tweets, un verrou : audit des signaux sociaux illustrant l'article

**Run `20260831-1119-audit-tweets-verrou-poubelles`** (MEDIUM, passe courte). OBJECT : vérifier 5 signaux sociaux (tweets T5) soumis par l'utilisateur comme illustrations de l'article déchèteries. Chaque tweet est un LEAD, pas une preuve : trouver la source primaire/officielle/presse derrière chaque phénomène, ou documenter le GAP.

## Verdict global

**4 leads sur 5 supportés par des sources primaires ou de la presse locale ; 1 GAP partiel (le « 700 000 € » vendéen). Aucun tweet ne contredit les passes certifiées de la fresque.**

## LEAD 1 — Poubelles à PASS en Vendée (tweet Sarah, 17/07/2025, 150k vues) : SUPPORTÉ, avec un point contesté et un GAP

- **197 €/an CONFIRMÉ par le site officiel** Vendée Grand Littoral (grille Tarifs 2026, secteur Littoral) : abonnement 197 € pour un bac 80 L (212/237/263/343 € pour 140/240/340/660 L et pro). L'abonnement comprend 6 levées bac OMR, **9 ouvertures des colonnes enterrées OMR**, 24 passages en déchèteries ; au-delà : 1 €/ouverture de colonne, 2 €/passage déchèterie, 2,40-20,10 €/levée (FCT-001).
- **QR code 2 € CONFIRMÉ par le site officiel** : 11 colonnes OMR dotées d'un QR code payant pour les visiteurs extérieurs au territoire, 2 € par dépôt par carte bancaire (FCT-002).
- La REOMi a remplacé la TEOM sur les 20 communes au **01/01/2022** (rapport d'activités 2022) — ce n'est pas un dispositif de 2025, il a 3 ans au moment du tweet (FCT-001, SRC-004).
- **Contexte documenté** : le tweet date du 17/07/2025, jour du reportage TF1 JT 13h tourné à Saint-Vincent-sur-Jard contre la redevance incitative. Les 19 communes contre-attaquent le 19/07 (actu.fr 20/07/2025) : -2 000 t OMR en 3 ans, +657 t emballages, -120 000 € facture Trivalis (FCT-003).
- **Point CONTESTÉ** : les dépôts sauvages autour des bacs. Les élus : « ils ont toujours existé » (2 % de la population). Le maire Olivier Dalmasso : « jamais dans de telles proportions », et explique la baisse de production par le badge, la conjoncture et le **report vers Les Sables-d'Olonne** (commune non REOMi) (FCT-003).
- **GAP** : le « 700 000 € » du tweet n'est PAS établi. Le seul 700 000 € documenté dans le rapport d'activités VGL 2022 est un **emprunt du budget DMA**, pas le coût du système de badge. Le coût réel du dispositif de contrôle d'accès n'est pas publié (FCT-003).

## LEAD 2 — Cité des Rosiers, « océan de plastique » (tweet Wolf, 29/12/2025, 18,7k vues) : SUPPORTÉ

- **actu.fr 31/12/2025** documente précisément le phénomène : la vidéo d'un habitant des Rosiers (14e arr., quartiers Nord), publiée en fin de semaine précédente (29/12/2025), montre « des déchets par milliers » au pied de la plus grande barre : sacs-poubelles, métal, gravats, mobilier, « souvent balancés depuis les balcons ». L'auteur y dit exactement la phrase du tweet : « Ici, ce n'est pas la déchetterie » (FCT-004).
- Le CIQ (Gilbert Delage) : la cité « se dégrade depuis des années » (dealers, squatteurs, marchands de sommeil) ; des résidents se mobilisent le 31/12 pour nettoyer eux-mêmes.
- **Contexte structurel** : un décret signé le 26/12/2025 qualifie l'opération de requalification des Rosiers (14 bâtiments, 883 logements, 3 000 habitants) d'**intérêt national** (annonce Macron juin 2023). Le dépôt massif n'est pas un accident : c'est un quartier en décrochage documenté (FCT-004).
- Note d'honnêteté : actu.fr signale que la vidéo « suscite de violents commentaires, parfois racistes » — le tweet viral porte aussi cette charge, à ne pas amplifier.

## LEAD 3 — Paris « dans cet état », maire Grégoire (tweet TonyPittaro, 18/06/2026, 12,3k vues) : SUPPORTÉ (contexte)

- **Emmanuel Grégoire est élu maire de Paris le 22/03/2026** (51 % au 2e tour). Le tweet du 18/06/2026 intervient trois mois après son élection (FCT-005).
- La propreté est un **axe majeur de la campagne** : Grégoire reconnaît « des ratés » sur la propreté (BFMTV 16/01/2026) et propose de « mieux sanctionner les incivilités » (mégots, déjections canines) ; il juge la privatisation de la collecte (proposée par Dati, Bournazel, Knafo) « une mauvaise idée » (FCT-005).
- Nuance : le tweet est une **opinion** sur l'état de la ville, pas un fait mesuré. Il n'est vérifiable qu'au titre du contexte politique et des promesses de campagne, pas d'une donnée de propreté indépendante.

## LEAD 4 — « Racket » à l'espace tri Porte de Pantin (tweet Wolf, 06/03/2026, 15,7k vues) : SUPPORTÉ avec nuance essentielle

- **Le « racket » n'a aucune base tarifaire officielle** : pour les particuliers parisiens, le dépôt en espace tri n'est pas facturé. Les limites officielles de l'espace tri Porte de Pantin (page Ville de Paris) : **3 m³ par passage, 6 passages maximum**, et depuis le 01/01/2025 plus aucun déchet du bâtiment (FCT-007).
- **Mais le phénomène « des agents qui demandent un billet » est documenté** : France Inter (06/09/2024) révèle la corruption passive de trois agents de l'espace tri Porte de la Chapelle (18e), accusés d'avoir laissé entrer des « faux particuliers » (professionnels du bâtiment) « moyennant un billet ». La Ville de Paris réclame **17 M€** (surcoût 2016-2021). L'enquête IGS (fin 2019) conclut à un risque de corruption « majeur » et à des « conditions optimales pour l'avènement de la fraude », pointant Porte de la Chapelle **et Porte de Pantin**. Des avis Google récents mentionnent encore « des agents qui demandent un billet » (FCT-006).
- **Le « racket » est donc une interprétation du tweet d'un phénomène réel documenté** : la corruption ponctuelle des agents (extorsion à l'entrée), pas un tarif institutionnel. Nuance cruciale pour l'article : c'est l'envers du verrou — le contrôle d'accès censé filtrer produit sa propre fraude.

## LEAD 5 — La police des poubelles (tweet Jon De Lorraine, 05/02/2025, 66,6k vues) : SUPPORTÉ

- **La Dépêche (16/02/2025)** documente la « police des poubelles » : dans l'Oise, une communauté de 52 communes a recruté une **« brigade du tri »** (duo de contrôleurs) qui fouille les poubelles avant le passage du camion, palpe les sacs, parfois les éventre au cutter, et appose un ruban rouge « non conforme » (poubelle non ramassée). Les mauvais trieurs s'exposent à une amende de **35 €, voire 75 €** si non payée (base légale depuis 2012) (FCT-008).
- La Dépêche note que des « polices de la poubelle » de ce genre « fleurissent un peu partout dans le pays » — le tweet viral (05/02/2025) précède l'article de 11 jours.
- Séparation nécessaire pour l'article : la charge idéologique du tweet (« avec nos impôts ») vs la base légale (L2212-2 CGCT, pouvoir de police du maire/EPCI) et la réalité documentée des brigades.

## Bouclage fresque

Les 5 tweets illustrent les mécanismes déjà certifiés sans les contredire :
- **Redevance incitative et verrou du bac** (LEAD 1) → passe 0927 (TI, effets mesurés)
- **Contrôle d'accès, quotas, facturation** (LEAD 1, 4) → passes DT138/1002/2123
- **Dépôts sauvages et leur coût** (LEAD 1, 2) → passes 2135 (900 €/t, 340-420 M€/an)
- **Fracture et exclusion** (LEAD 2, 3) → passe 2245 (fracture numérique/sociale)
- **Corruption comme envers du verrou** (LEAD 4) → passe 2114 (conflit Symetri/TRIBORD : la donnée de contrôle crée sa propre économie grise)
- **Privatisation et mode de gestion** (LEAD 3, 5) → Cour des comptes 2024 (DSP « angle mort »)

## Gaps
- Coût réel du système de badge VGL non publié (« 700 000 € » non confirmé).
- Pas de série nationale sur les dépôts autour des colonnes à badge (le cas VGL est disputé localement).
- Le tweet Paris (LEAD 3) n'a pas de donnée de propreté indépendante pour le vérifier au-delà du contexte politique.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:5|CLM:1|AXS:1|CAU:1|CTRL:0|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence_key":"VGL REOMi 01/01/2022, abonnement 2026 197€ bac 80L, 11 colonnes QR 2€, polemique TF1 17/07/2025 (actu.fr 20/07/2025), 700k€ non etabli","note":"197€ et QR 2€ CONFIRMES par site officiel; 700k€ GAP; depots = point conteste","routes":["site officiel VGL","actu.fr TF1","rapport activites VGL"],"status":"SATURATED","title":"Tweet 1 (Sarah, 17/07/2025) : poubelles a PASS Vendee Grand Littoral, 197€/an, QR 2€ touristes, depots autour des bacs"}
LED-002 | {"evidence_key":"actu.fr 31/12/2025 video virale dechets balances depuis balcons, mobilisation habitants, decret interet national 26/12/2025","note":"phenomene documente par presse regionale; dimension raciste des commentaires signalee par actu.fr","routes":["actu.fr Rosiers","BFMTV place nette 2024","mairie 14e"],"status":"SATURATED","title":"Tweet 2 (Wolf, 29/12/2025) : depot massif cite des Rosiers 14e arrondissement Marseille"}
LED-003 | {"evidence_key":"Gregoire elu maire 22/03/2026 51%, reconnait des rates sur la proprete (BFMTV 16/01/2026), proprete = axe majeur campagne 2026","note":"contexte electoral documente; le tweet est une opinion sur l'etat de la ville, pas un fait mesure","routes":["BFMTV Gregoire","resultats municipales 2026","bilan proprete Paris"],"status":"SATURATED","title":"Tweet 3 (TonyPittaro, 18/06/2026) : Paris dans cet etat, maire Gregoire"}
LED-004 | {"evidence_key":"France Inter 06/09/2024 corruption passive 3 agents Porte de la Chapelle, faux particuliers moyennant billet, 17M€, Pantin pointee; regles officielles Pantin 3m3/6 passages, dechets batiment refuses","note":"le mot 'racket' = interpretation; le phenomene 'agents qui demandent un billet' = documente (corruption ponctuelle, pas tarif officiel)","routes":["France Inter corruption","page Paris Porte de Pantin","avis Google"],"status":"SATURATED","title":"Tweet 4 (Wolf, 06/03/2026) : racket a l'espace tri Porte de Pantin (Paris)"}
LED-005 | {"evidence_key":"La Depeche 16/02/2025 brigade du tri Oise 52 communes, fouille des sacs, ruban non conforme, amende 35-75€ (base legale 2012)","note":"phenomene reel et documente; la charge ideologique du tweet separee de la base legale","routes":["La Depeche","service-public amende tri","collectivites en brigade"],"status":"SATURATED","title":"Tweet 5 (Jon De Lorraine, 05/02/2025) : la police des poubelles avec nos impots"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"4 des 5 tweets sont supportes par des sources primaires ou de la presse locale (VGL: 197€/QR 2€ officiels; Rosiers: actu.fr; Gregoire: BFMTV+election; racket Pantin: corruption France Inter; police poubelles: La Depeche); seul le '700 000 €' du tweet VGL n'est pas etabli (GAP)","counter":"Chaque tweet est un signal social (T5) : le fait qu'une video soit virale ne prouve ni sa representativite ni sa cause; la seule source officielle VGL contrebalance le recit des depots sauvages (elus: 'ont toujours existe').","gap":"cout reel du systeme de badge VGL non public (le 700 000 € documente est un emprunt DMA); pas de serie nationale sur les depots autour des colonnes a badge","gap_type":"COVERAGE_PARTIAL","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-004","FCT-005","FCT-006","FCT-008"]}

### AXIS_REGISTRY_V1
AXS-001 | {"question":"Les phenomenes decrits par les 5 tweets correspondent-ils a des faits documentes (sources primaires/officielles/presse locale) ou relevent-ils de la rumeur non verifiable ?","routes":["AUDIT","EXPAND"],"sought_objects":["source primaire par lead","700 000 € VGL","depots autour bacs VGL","racket Porte de Pantin","police poubelles"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"cause":"Redevance incitative + controle d'acces des colonnes OMR (badge/QR) restreignent l'acces au depot des ordures menageres","effect":"Depots sauvages autour des colonnes/bacs (conteste localement VGL) et reports vers communes sans REOMi (Les Sables-d'Olonne) ou vers la corruption ponctuelle des agents (Paris)","mechanism":"VGL: badge + QR payant 2€; Paris: faux particuliers entres moyennant billet (corruption passive); coherence avec passes 0927/1002/2135","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-006"]}

### CONTROL_REGISTRY_V1

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:5|FETCH:9|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"EMPTY","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"EMPTY","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FOUND | runtime | warm-route-tweets-verrou | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | OK | - | - | Vendee poubelles PASS badge 197 euros an QR code touristes 2 euros depots sauvages autour bacs
QRY-002 | FETCH | INSPECTED | SRC-001 | https://www.vendeegrandlittoral.fr/points-dapport-volontaire-2/ | Vendee Grand Littoral PAV ordures menageres pass controle acces QR 2 euros
QRY-003 | FETCH | INSPECTED | SRC-002 | https://www.vendeegrandlittoral.fr/la-redevance-incitative-secteur-littoral/ | Vendee Grand Littoral redevance incitative tarifs 2026 abonnement 197 euros 9 ouvertures
QRY-004 | FETCH | INSPECTED | SRC-003 | https://actu.fr/societe/apres-le-reportage-au-jt-de-13-h-de-tf1-sur-les-dechets-les-elus-de-vendee-grand-littoral-contre-attaquent_62933841.html | TF1 JT 17/07/2025 depots sauvages redevance incitative Vendee Grand Littoral contre-attaque elus Dalmasso
QRY-005 | FETCH | INSPECTED | SRC-004 | https://www.vendeegrandlittoral.fr/medias/2023/09/01.-Rapport-dactivites-2022-Vendee-Grand-Littoral.pdf | VGL rapport activites 2022 700 000 emprunt redevance incitative 2022
QRY-006 | WEB | OK | - | - | Marseille cite des Rosiers depot sauvage dechets plastique 2025
QRY-007 | FETCH | INSPECTED | SRC-005 | https://actu.fr/provence-alpes-cote-d-azur/marseille_13055/marseille-on-reste-vu-qu-il-n-y-a-pas-le-choix-ce-quartier-jonche-d-ordures-une-video-choque_63638741.html | Rosiers 14e arrondissement video dechets balcons 29/12/2025 mobilisation habitants decret interet national
QRY-008 | WEB | OK | - | - | Emmanuel Gregoire Paris proprete dechets elections municipales 2026 maire
QRY-009 | FETCH | INSPECTED | SRC-006 | https://www.bfmtv.com/politique/elections/municipales/municipales-a-paris-emmanuel-gregoire-reconnait-des-rates-sur-la-proprete-et-propose-de-mieux-sanctionner-les-incivilites_AD-202601160523.html | Grégoire reconnait des rates sur la proprete 16/01/2026 sanctionner incivilites
QRY-010 | WEB | OK | - | - | Paris Porte de Pantin decheterie payante volume trop important tarifs 2026
QRY-011 | FETCH | INSPECTED | SRC-007 | https://www.paris.fr/lieux/espace-tri-de-la-porte-de-pantin-decheterie-18537 | espace tri Porte de Pantin 3 m3 6 passages dechets du batiment refuses 01/01/2025
QRY-012 | FETCH | INSPECTED | SRC-008 | https://www.radiofrance.fr/franceinter/podcasts/l-info-de-france-inter/l-info-de-france-inter-6219401 | dechetteries Paris corruption passive 3 agents Porte de la Chapelle faux particuliers 17 millions IGS
QRY-013 | WEB | OK | - | - | police des poubelles collectivite brigade controle dechets menagers verbalisation 2025 impots
QRY-014 | FETCH | INSPECTED | SRC-009 | https://www.ladepeche.fr/2025/02/16/ordures-controles-amendes-comment-la-police-des-poubelles-sanctionne-les-mauvais-trieurs-12510741.php | police des poubelles Oise brigade du tri 52 communes amende 35 euros mauvais trieurs

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.vendeegrandlittoral.fr/points-dapport-volontaire-2/
SRC-002 | ◈ | fam:A | https://www.vendeegrandlittoral.fr/la-redevance-incitative-secteur-littoral/
SRC-003 | ◈ | fam:A | https://actu.fr/societe/apres-le-reportage-au-jt-de-13-h-de-tf1-sur-les-dechets-les-elus-de-vendee-grand-littoral-contre-attaquent_62933841.html
SRC-004 | ◈ | fam:A | https://www.vendeegrandlittoral.fr/medias/2023/09/01.-Rapport-dactivites-2022-Vendee-Grand-Littoral.pdf
SRC-005 | ◈ | fam:A | https://actu.fr/provence-alpes-cote-d-azur/marseille_13055/marseille-on-reste-vu-qu-il-n-y-a-pas-le-choix-ce-quartier-jonche-d-ordures-une-video-choque_63638741.html
SRC-006 | ◈ | fam:A | https://www.bfmtv.com/politique/elections/municipales/municipales-a-paris-emmanuel-gregoire-reconnait-des-rates-sur-la-proprete-et-propose-de-mieux-sanctionner-les-incivilites_AD-202601160523.html
SRC-007 | ◈ | fam:A | https://www.paris.fr/lieux/espace-tri-de-la-porte-de-pantin-decheterie-18537
SRC-008 | ◈ | fam:A | https://www.radiofrance.fr/franceinter/podcasts/l-info-de-france-inter/l-info-de-france-inter-6219401
SRC-009 | ◈ | fam:A | https://www.ladepeche.fr/2025/02/16/ordures-controles-amendes-comment-la-police-des-poubelles-sanctionne-les-mauvais-trieurs-12510741.php

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.vendeegrandlittoral.fr/la-redevance-incitative-secteur-littoral/ | A | 2026-01-01 | Vendee Grand Littoral: redevance incitative 01/01/2022, abonnement 2026 197€ (bac 80L) incluant 6 levees + 9 ouvertures colonnes + 24 passages decheterie | Site officiel VGL (secteur Littoral, grille Tarifs 2026) : la REOMi a remplace la TEOM sur les 20 communes au 01/01/2022 (rapport activites 2022, SRC-004). Tarifs 2026 secteur Littoral : abonnement 197 € pour bac 80 L, 212/237/263/343 € pour 140/240/340/660 L et pro. L'abonnement comprend 6 presentions du bac OMR, 9 ouvertures des colonnes enterrees OMR, 24 passages en decheteries ; au-dela : +2,40 a +20,10 €/levee, 2 €/passage decheterie, 1 €/ouverture colonne. Le tweet Sarah (197 €/an) = abonnement bac 80 L. | cc271115-ab1e-42a0-b01e-b5f68d5d2587
FCT-002 | FACT | ✧ | https://www.vendeegrandlittoral.fr/points-dapport-volontaire-2/ | A | 2026-01-01 | VGL: 11 colonnes OMR a QR code payant 2 €/depot pour visiteurs exterieurs; acces habitants par Pass a puce | Site officiel VGL (Points d'Apport Volontaire) : les colonnes OMR sont equipees d'un dispositif de controle d'acces (ouverture par Pass VGL a puce). Pour les usagers exterieurs au territoire, 11 colonnes dotees d'un systeme de QR code payant (2 € regles par carte bancaire) permettent de deposer des sacs OMR. Les flux selectifs (verre, papier, emballages) restent libres. Confirme le tweet : 'QR code au prix de 2 euros piece pour ouvrir la poubelle'. | 0b2f3bea-2111-4614-b6f0-4e2b696a9b49
FCT-003 | FACT | ✧ | https://actu.fr/societe/apres-le-reportage-au-jt-de-13-h-de-tf1-sur-les-dechets-les-elus-de-vendee-grand-littoral-contre-attaquent_62933841.html | A | 2025-07-20 | TF1 JT 17/07/2025 sur depots sauvages VGL : contre-attaque des 19 elus; depots sauvages = point CONTESTE (elus 'toujours existe' vs maire Dalmasso 'jamais dans de telles proportions') | actu.fr 20/07/2025 : reportage TF1 JT 13h du 17/07/2025 (jour du tweet Sarah) tourne a Saint-Vincent-sur-Jard, contre la redevance incitative, portant sur les depots sauvages d'OMR 'effet pervers'. Reunion d'urgence des 19 communes le 19/07 : les elus denoncent un reportage 'sans equilibre de l'information', donnent leurs chiffres (-2 000 t OMR en 3 ans, +657 t emballages, -120 000 € facture Trivalis), et affirment que les depots 'ont toujours existe'. Le maire Olivier Dalmasso (Saint-Vincent-sur-Jard) conteste : 'jamais dans de telles proportions', chiffre la baisse de production par le badge, la conjoncture et le report vers Les Sables-d'Olonne (non REOMi). Le montant '700 000 €' du tweet n'est PAS etabli par ce dossier : le seul 700 000 € documente (rapport VGL 2022, SRC-004) est un EMPRUNT du budget DMA, pas un cout du systeme de badge. GAP : cout reel du dispositif de controle d'acces non public. | b5e80786-6758-487d-a6cf-ee75854662c2
FCT-004 | FACT | ✧ | https://actu.fr/provence-alpes-cote-d-azur/marseille_13055/marseille-on-reste-vu-qu-il-n-y-a-pas-le-choix-ce-quartier-jonche-d-ordures-une-video-choque_63638741.html | A | 2025-12-31 | Marseille cite des Rosiers (14e) : video virale 29/12/2025 dechets balances depuis les balcons; mobilisation habitants 31/12; decret 26/12/2025 operation interet national | actu.fr 31/12/2025 : la video d'un habitant des Rosiers (14e arr., quartiers Nord), publiee fin de semaine precedente (29/12/2025, jour du tweet Wolf), montre 'des dechets par milliers' au pied de la plus grande barre : sacs-poubelles, metal, gravats, mobilier, 'souvent balances depuis les balcons'. L'auteur filme ('Ici, ce n'est pas la dechetterie'). Vague de reactions ; le CIQ Bon Secours-Saint Gabriel-Clair Soleil (Gilbert Delage) : la cite 'se degrade depuis des annees' (dealers, squatteurs, marchands de sommeil). Des residents se mobilisent le 31/12 pour nettoyer. Un decret signe 26/12/2025 qualifie l'operation de requalification d'interet national (14 batiments, 883 logements, 3 000 habitants, projets des 2026). | f358ca45-c933-45bf-9342-9552c9723b27
FCT-005 | FACT | ✧ | https://www.bfmtv.com/politique/elections/municipales/municipales-a-paris-emmanuel-gregoire-reconnait-des-rates-sur-la-proprete-et-propose-de-mieux-sanctionner-les-incivilites_AD-202601160523.html | A | 2026-01-16 | Gregoire (16/01/2026) reconnait 'des rates' sur la proprete parisienne, veut 'mieux sanctionner les incivilites'; la proprete electrise la campagne 2026 (Dati/Bournazel/Knafo: privatisation) | BFMTV 16/01/2026 : Emmanuel Gregoire, candidat de l'union de la gauche hors LFI, reconnait 'des rates' sur la proprete (et securite, violences sexistes) et propose de 'mieux sanctionner les incivilites' (megots, dejections canines). Il juge la privatisation de la collecte (proposee par Dati, Bournazel, Knafo) 'une mauvaise idee'. La proprete est un axe majeur des municipales 2026. Gregoire est ensuite elu maire de Paris le 22/03/2026 (51% des voix, 2e tour). Le tweet TonyPittaro (18/06/2026) intervient apres son election : expression d'un mecontentement sur l'etat de la ville, contexte de promesse de campagne non tenue a verifier par le bilan. | 96f7b059-3ca0-4bcb-996f-856ac394c36a
FCT-006 | FACT | ✧ | https://www.radiofrance.fr/franceinter/podcasts/l-info-de-france-inter/l-info-de-france-inter-6219401 | A | 2024-09-06 | Corruption aux dechetteries parisiennes (France Inter 06/09/2024) : 3 agents Porte de la Chapelle, 'faux particuliers' entres 'moyennant un billet', 17 M€ reclamés par la Ville, Porte de Pantin pointee; avis Google 2024 'agents qui demandent un billet' | France Inter 06/09/2024 : trois agents de l'espace tri de la Porte de la Chapelle (18e) compaissent pour corruption passive, accuses d'avoir accepte de l'argent de professionnels venant vider illegalement leurs dechets de chantier ('faux particuliers', 'portes ouvertes moyennant un billet'). La Ville de Paris reclame 17 M€ (surcout 2016-2021). L'enquete administrative de l'IGS (fin 2019, confidentielle) conclut a un risque de corruption 'majeur' et a des 'conditions optimales pour l'avenement de la fraude', pointant Porte de la Chapelle ET Porte de Pantin. Signalement au procureur 11/2021 ; BRDE : enquete 'baclee' selon plusieurs acteurs. Des avis Google recents mentionnent 'des agents qui demandent un billet'. Le tweet Wolf (06/03/2026, 'rackette pour deposer') s'inscrit dans ce phenomene documente : non un tarif officiel, mais une corruption ponctuelle des agents. | 371b5bcf-a6e6-4320-bf7f-b5c4568b2f09
FCT-007 | FACT | ✧ | https://www.paris.fr/lieux/espace-tri-de-la-porte-de-pantin-decheterie-18537 | A | 2025-01-01 | Paris espace tri Porte de Pantin : depots limites 3 m3/passage, 6 passages max; depuis 01/01/2025 plus aucun dechet du batiment (particuliers compris) | Page officielle Ville de Paris (espace tri Porte de Pantin, 5 bis place de la Porte de Pantin, Paris 19e) : depots limites a 3 m3 par passage, 6 passages maximum. Depuis le 01/01/2025, les decheteries de Paris n'accueillent plus de dechets du batiment (les particuliers sont renvoyes vers d'autres points). Le tweet Wolf (06/03/2026) decrit un depot refuse pour 'volume trop important' : les 3 m3/6 passages sont les limites officielles applicables ; le 'racket' (argent demande) n'a pas de base reglementaire - la facturation au depot n'existe pas pour les particuliers parisiens, le phenomene documente est la corruption ponctuelle (FCT-006). | 0e521eb9-3688-40c1-a43e-49aa68776b4f
FCT-008 | FACT | ✧ | https://www.ladepeche.fr/2025/02/16/ordures-controles-amendes-comment-la-police-des-poubelles-sanctionne-les-mauvais-trieurs-12510741.php | A | 2025-02-16 | Police des poubelles (La Depeche 16/02/2025) : brigade du tri dans l'Oise (52 communes), duo de controleurs fouillant les sacs, ruban 'non conforme', amende 35-75 € pour mauvais tri (base legale depuis 2012) | La Depeche 16/02/2025 : dans l'Oise, une communaute de 52 communes a recrute une 'brigade du tri' (duo de controleurs) qui fouille les poubelles avant le passage du camion, palpe les sacs, parfois les eventre au cutter, et appose un ruban rouge 'non conforme' (poubelle non ramassee). Les mauvais trieurs s'exposent a une amende de 35 €, voire 75 € si non payee (depuis 2012, base legale service-public). Des 'polices de la poubelle' fleurissent dans le pays. Le tweet Jon De Lorraine (05/02/2025) precede cet article : phenomene reel et documente, avec une dimension ideologique (controle par l'argent public) a separer de la base legale. | 9b47240d-64d0-472a-a154-469834e5bfcf
FCT-009 | FACT | ✧ | https://actu.fr/societe/apres-le-reportage-au-jt-de-13-h-de-tf1-sur-les-dechets-les-elus-de-vendee-grand-littoral-contre-attaquent_62933841.html | A | 2026-08-31 | Synthese 5 tweets : 4/5 supportes par sources primaires/presse (VGL, Rosiers, Gregoire, corruption Paris, police poubelles); 1 GAP partiel (700 000 € VGL); tous illustrent les mecanismes de la fresque | Verdict de l'audit : LEAD 1 SUPPORTE (197€/an et QR 2€ confirmes par le site officiel VGL ; depots sauvages = point conteste elus/maire ; '700 000 €' non etabli = GAP), LEAD 2 SUPPORTE (actu.fr 31/12/2025), LEAD 3 SUPPORTE (BFMTV 16/01/2026 + election 22/03/2026), LEAD 4 SUPPORTE avec nuance (corruption documentee France Inter 06/09/2024 vs tarif officiel inexistant), LEAD 5 SUPPORTE (La Depeche 16/02/2025). Les 5 tweets illustrent les mecanismes deja certifies de la fresque : redevance incitative et verrou du bac (passe 0927), controle d'acces et quotas (DT138/1002), depots sauvages et cout (2135), exclusion et fracture (2245), privatisation du service (Cour des comptes 2024). Aucun des 5 ne contredit les passes certifiees. | 30c8f948-f7f0-483e-b0d9-0a5a8ce3a084
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-002
FCT-002 | SRC-001
FCT-003 | SRC-003
FCT-004 | SRC-005
FCT-005 | SRC-006
FCT-006 | SRC-008
FCT-007 | SRC-007
FCT-008 | SRC-009
FCT-009 | SRC-003

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-08-31T09:24:49.772048+00:00","fact_mem":{"FCT-001":"cc271115-ab1e-42a0-b01e-b5f68d5d2587","FCT-002":"0b2f3bea-2111-4614-b6f0-4e2b696a9b49","FCT-003":"b5e80786-6758-487d-a6cf-ee75854662c2","FCT-004":"f358ca45-c933-45bf-9342-9552c9723b27","FCT-005":"96f7b059-3ca0-4bcb-996f-856ac394c36a","FCT-006":"371b5bcf-a6e6-4320-bf7f-b5c4568b2f09","FCT-007":"0e521eb9-3688-40c1-a43e-49aa68776b4f","FCT-008":"9b47240d-64d0-472a-a154-469834e5bfcf","FCT-009":"30c8f948-f7f0-483e-b0d9-0a5a8ce3a084"},"mnemo_row":"written investigation memory via API","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-006","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-007","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-008","reason":"NONE","success":1},{"action":"ELIGIBLE:VERIFIE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-009","reason":"NONE","success":1}],"writeback_row":{"attempted":9,"blocked":0,"eligible":9,"failure":0,"success":9}}

PERSISTENCE_META: MNEMO_ROW:written investigation memory via API | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:9;attempted:9;success:9;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[9 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-004 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-006 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-007 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-008 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
FCT-009 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:NONE
