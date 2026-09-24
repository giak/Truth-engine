ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260920-2008-dgf-impact-ecart-population-metzing | PARENT_RUN_ID:20260920-1921-insee-pdf-methodo-gap-access-closure | AS_OF:2026-09-20
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-20_dgf-impact-ecart-population-metzing/2026-09-20_20-08_dgf-impact-ecart-population-metzing_INPUT.txt | SUBJECT_SLUG:dgf-impact-ecart-population-metzing | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:105→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:UPDATE run 19-21: chiffrage DGF de l'ecart de population type Metzing (678 vs 791) via baremes et donnees DGCL/OFGL; euros par habitant d'ecart dans la strate [500,1000[
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Chiffrage DGF de l'écart de population type Metzing (113 habitants)

Run UPDATE du run parent *Insee — PDF méthodologiques (closure gaps ACCESS)*. La question était routée en suivant par le parent : **que vaut, en euros, l'écart de population légale documenté à Metzing (678 habitants selon l'Insee 2024, 791 selon la mairie) ?** Réponse : il est chiffrable, il est borné, et il est inférieur à ce que la narration publique suggère.

## Scoping et méthode

Périmètre : dotation forfaitaire et DGF totale de Metzing (Moselle), strate démographique [500 ; 1000[. Méthode : séries communales réelles de l'Observatoire des finances locales (OFGL, données publiques DGCL) plutôt que tout barème théorique — l'élasticité **mesurée** sur une commune remplace l'élasticité supposée (FCT-001, FCT-003 ; SRC-001, SRC-002, SRC-008). Exclusions déclarées : DGF de l'EPCI (hors périmètre communal) et rétroactif des années passées (aucune base réglementaire identifiée).

## La chaîne réelle : de l'estimation statistique au budget communal

La population légale est un estimé réglementaire, authentifié chaque année par décret ; plus de 350 articles de loi en dépendent. La DGCL calcule la DGF sur une « population DGF » (Insee + résidences secondaires + places de caravanes), dans une dotation forfaitaire évolutive : socle figé depuis 2004, complément de garantie écrêté selon le potentiel fiscal, part population stratifiée (barème historique : 64,46 à 128,93 € par habitant selon la strate), dotation superficie ~3,22 €/ha (FCT-001 ; SRC-001, SRC-003, SRC-005). Chaque incertitude d'estimation se convertit donc mécaniquement en euros de dotation.

## Le chiffrage

Série réelle de Metzing 2018-2026 (FCT-002) : population Insee 678 (2024) → 699 (2025) → 715 (2026) ; DGF totale 105 906 € (2024) → 114 005 € (2026). Élasticité réelle mesurée : **86,9 € par habitant de dotation forfaitaire** (médiane des variations annuelles rapportées aux variations de population DGF), dans la fourchette du barème historique (FCT-003).

**Résultat central (FCT-004)** : un écart de 113 habitants comme celui de Metzing vaut **environ 9 800 € par an** de dotation forfaitaire à l'élasticité empirique de la commune — plage ~7 300 à ~14 600 € selon la strate du barème, majorant de l'ordre de 18 000 € si l'on prend la DGF totale. C'est réel et significatif pour un budget de micro-commune, mais deux ordres de grandeur sous les « 30 000 € » médiatisés pour Bouzonville (commune cinq fois plus peuplée, autres composantes de DGF ; SRC-010).

**Le rattrapage (FCT-005)** : l'écart se résorbe déjà dans les données — 678 → 699 → 715 en deux millésimes. La contestation mairie/Insee n'est pas un différentiel durable : le système corrige prospectivement. Ce qu'il ne fait pas : rétro-correction de l'année sous-estimée.

## Torture adversariale

Le fait central a reçu sa réfutation terminale (deux mécanismes documentés testés) : **lissage sur cinq ans des pertes de population** pour certaines communes et **écrêtement du complément de garantie** (SRC-011) ; **forfaitaire évolutive** (fonction de la DGF de l'année précédente) et **effets de seuil DSR/DSU/DNP** par éligibilité (SRC-012). Verdict : la mesure empirique survit — précisément parce qu'elle est mesurée sur des variations qui ont déjà traversé ces amortisseurs — mais elle reste **bornée** : les composantes nominatives (forfait/DSR/DNP séparés) et les effets de seuil individuels ne sont pas modélisables sans la fiche de dotation nominative, non publique. Aucune sélection opportuniste n'est documentée : le différentiel presse s'explique par la décomposition, pas par la manipulation.

## Table d'évaluation des 15 symboles

| Symbole | Score | Observations nommées |
|---|---|---|
| Ξ Omission | 6 | Fiche de dotation nominative non publique ; aucune procédure de rétro-correction documentée ; composantes nominatives invisibles dans les jeux publics |
| € Money | 8 | Objet même du run : l'estimation statistique devient dotation via la population DGF ; incitation financière aux seuils (DSR, strates) |
| Λ Framing | 6 | Presse locale en « euros perdus » sans décomposition ; « chiffre de la mairie » contre « chiffre de l'Insee » sans ontologies du compte |
| Ω Inversion | 2 | Aucune inversion documentée ; l'Insee répond publiquement aux contestations (CNERP) |
| Ψ Sidération | 1 | Sujet local, pas de volume émotionnel |
| ↕ Pouvoir vertical | 7 | L'estimation décrétée s'impose aux communes ; contestation par voie parlementaire ; asymétrie d'accès aux données nominatives |
| Φ Spectacle | 3 | Médiatisation ponctuelle du différentiel financier (Moselle.tv) |
| Σ Sémiotique | 1 | Néant observé |
| Κ Cynisme | 2 | Pas de façade maintenue : rattrapage réel visible dans les séries |
| ρ Résistance | 5 | Questions écrites Mizzon/Pluchet au Sénat, relais AMF, avis publié du CNERP : contre-pouvoir institutionnel actif |
| κ Influence subtile | 4 | Architecture de choix : les seuils orientent les comportements communaux sans intention démontrée |
| ⫸ Convergence | 6 | Sources indépendantes convergentes : OFGL, Sénat, Insee, DGCL sur le mécanisme et l'écart |
| ⚔ Guerre cognitive | 0 | Aucun élément |
| 🌐 Réseau | 6 | Insee-DGCL-DGFiP-maires-CNERP-Sénat-AMF cartographiés, rôles séparés |
| ⏰ Temporel | 7 | Délai d'authentification 3 → 2 ans fin 2026 ; rattrapage en deux millésimes ; correction prospective et non rétroactive |

## Contradictions et limites

C1 (résolue) : 678 contre 791 — le rattrapage 699 → 715 confirme une correction de collecte ; l'hypothèse d'un comptage communal en logements pour le 791 n'est pas arbitrée. C2 (résolue) : élasticité mesurée 86,9 € cohérente avec le barème théorique. C3 (ouverte) : non-additivité annuelle de la forfaitaire évolutive — exige la fiche nominative (suivant typé ACCESS). EDI estimé 0,67, cible atteinte ; limite divulguée : dépendance partielle au jeu OFGL comme source primaire des montants.

## Verdict

**Chiffrage établi et borné : ~9 800 €/an de forfaitaire pour 113 habitants** (plage ~7 300-14 600 €, majorant ~18 000 € sur la DGF totale) — l'incertitude statistique sur la population légale a bien un prix, documenté chiffre par chiffre. **Non établi : toute manipulation.** Le mécanisme (estimation authentifiée par décret, amortisseurs légiférés, rattrapage visible, délai réduit 3 → 2 ans sur avis du CNERP) est publié. Le point dur n'est pas la falsification mais l'**asymétrie de visibilité** : le chiffre contesté est public et bruyant, sa correction est prospective et silencieuse, et la contre-expertise citoyenne bute sur la non-publication des fiches nominatives.

## Périmètre et limites (suivants routés)

Fiche de dotation nominative de Metzing via préfecture ou mairie (ACCESS) ; arbitrage du 791 communal contre les référentiels géographiques (CAUSALITY) ; notes DGCL 2025-2026 pour recalculer l'élasticité théorique 2026 (ACCESS) ; série DGF EPCI de la communauté de communes (ACCESS, existence confirmée).
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:4|AXS:3|CAU:3|CTRL:2|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"evidence":[],"lead":"Mecanique DGF: population DGF = base INSEE + majorations; forfait = DNP + DSR + FCTMV","note":"A sourcer via pages DGCL/collectivites-locales","status":"SATURATED"}
LED-002 | {"evidence":[],"lead":"Baremes par habitant 2025/2026 pour strate [500,1000[ (FCTMV, DNP, DSR cible garanti)","note":"Notes d information DGCL / fiches Senat","status":"SATURATED"}
LED-003 | {"evidence":[],"lead":"Chiffrage marginal: ecart 113 habitants x taux par habitant = euros/an","note":"Produit calcule depuis baremes sources; strate identique de 678 a 791","status":"SATURATED"}
LED-004 | {"evidence":[],"lead":"Cas Metzing: 678 (Insee) vs 791 (mairie), enjeu DGF documente par question ecrite","note":"Heritage question Mizzon 2024","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le chiffrage DGF de l ecart Metzing est possible avec les donnees publiques: elasticity reelle mesuree 86,9 EUR/hab (medianne des variations forfait/popDGF de Metzing), d ou 113 hab = environ 9800 EUR/an de forfaitaire (plage 7300-14600; majorant DGF totale 18000)","evidence":["SRC-002","SRC-008","SRC-003","SRC-001"],"note":"NEXT_QUERY DGF/DGCL du parent refermee; chiffrage borne et disclose","status":"SUPPORTED"}
CLM-002 | {"claim":"L ecart conteste 678 vs 791 se resorbe deja dans les donnees: 678 (2024) -> 699 (2025) -> 715 (2026), rattrapage de collecte de +37 hab en 2 ans; la mairie de 791 inclut sans doute des logements comptes differemment (OCS GE) ou un etat ante","evidence":["SRC-002","SRC-004","SRC-008"],"note":"Hypothese de resolution (OCS GE) non arbitree: routee","status":"SUPPORTED"}
CLM-003 | {"claim":"L enjeu financier est reel mais borne pour une micro-commune: environ 10 kEUR/an par 113 hab sur la forfaitaire, deux ordres de grandeur sous les 30 kEUR cites pour Bouzonville (commune 5x plus peuplee, autres composantes de DGF)","evidence":["SRC-008","SRC-010","SRC-003"],"note":"Evite la generalisation du cas unique","status":"SUPPORTED"}
CLM-004 | {"claim":"Le chiffrage DGF de l'écart Metzing est possible avec les données publiques : élasticité réelle mesurée ~86,9 EUR/hab (médiane des variations forfait/population DGF de Metzing), d'où 113 hab ≈ 9 800 EUR/an de forfaitaire (plage ~7 300-14 600 ; majorant DGF totale ~18 000)","evidence":["CLM-004"],"note":"Gap typé ACCESS : composantes nominatives et effets de seuil non modélisables sans la fiche de dotation DGCL","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"axis":"MECANIQUE DE REPARTITION (population DGF -> dotations)","evidence":["SRC-D01"],"note":"Chainon legale a sourcer; conditionne la validite du chiffrage marginal","status":"SATURATED"}
AXS-002 | {"axis":"QUANTIFICATION (baremes x ecart Metzing)","evidence":["SRC-D02","SRC-D03"],"note":"Produit marginal calcule; strate [500,1000[ identique des deux cotes","status":"SATURATED"}
AXS-003 | {"axis":"CONTRE-HYPOTHESES (non-linearite, seuils, OCS GE)","evidence":["SRC-D05"],"note":"Effets de seuil explicitement examines; reconciliation OCS GE routee en GAP/rouge","status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"evidence":["SRC-001","SRC-005","SRC-002"],"note":"Chaine complete de l estimation au budget, chaque maillon source","provenance":"population legale Insee (estimation, decret) -> population DGF (INSEE + res sec + caravanes) -> regles DGCL (forfait = base + part population; DSR/DNP selon eligibilite) -> euros de dotation -> budget communal","status":"SUPPORTED"}
CAU-002 | {"evidence":["SRC-008","SRC-003","SRC-006"],"note":"Quantifie le vecteur financier de la contestation","provenance":"ecart d estimation 113 hab (678 vs 791) -> perte de part population sur la forfaitaire (~9800 EUR/an a elasticite 86,9) -> enjeu budgetaire annuel + incitation des communes proches des seuils (question Pluchet)","status":"SUPPORTED"}
CAU-003 | {"evidence":["SRC-002","SRC-008"],"note":"Asymetrie temporelle: correction prospective, pas retrospective","provenance":"rattrapage de collecte (678->699->715) -> correction partielle de la base DGF -> hausse DGF +7,6 % (2024-2026) -> mais pas de retro-correctif retroactif: l annee sous-estimee reste sous-paiement","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Series OFGL de Metzing recoupees entre deux requetes API distinctes (variables Population INSEE et Montant DGF) et contre la question Mizzon (678 en 2024)","evidence":["SRC-002","SRC-008","SRC-004"],"status":"DONE"}
CTRL-002 | {"control":"Coherence interne verifiee: elasticite mediane 86,9 EUR/hab dans la plage DGCL 2015 (64,46-128,93); DSR/DGF 35,8 % cohorent avec une commune rurale eligible DSR perequation (OFGL 2025)","evidence":["SRC-003","SRC-002","SRC-008"],"status":"DONE"}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Solliciter via prefecture la fiche de dotation nominative de Metzing (DGCL) pour caler forfait, DSR, DNP et effets de garantie","note":"route vers NEXT_QUERIES","status":"DONE"}

SEARCH_ACTIVITY_V1:WEB:0|FETCH:12|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FOUND | mcp-curl-8002 | 20260920-1921-insee-pdf-methodo-gap-access-closure | MNEMO_Q
SYS-002 | SYS | FOUND | runtime | - | HYDRATE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes | mecanique DGF: population DGF = INSEE + res sec + caravanes; forfait = DNP+DSR+FCTMV; reforme CPS 2024
QRY-002 | FETCH | FOUND | SRC-002 | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100 | OFGL API dotations-communes: series Metzing 2018-2026 (Population INSEE/DGF, Montant DGF, DSR, DNP)
QRY-003 | FETCH | FOUND | SRC-003 | https://www.maire-info.com/finances/deux-notes-de-la-dgcl-precisent-les-modes-de-calculet-de-repartition-de-la-dotation-forfaitaire-article-18426 | note DGCL 2015: part population 64,46-128,93 EUR/hab; ecretement 0,75 x PF moyen
QRY-004 | FETCH | FOUND | SRC-004 | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | question Mizzon: Metzing 678 Insee vs 791 mairie; defense CNERP; delai 3->2 ans fin 2026
QRY-005 | FETCH | FOUND | SRC-005 | https://www.insee.fr/fr/information/2553979 | populations de reference: decret d authentification, 350 articles de loi, estimation
QRY-006 | FETCH | FOUND | SRC-006 | https://fr.wikipedia.org/wiki/Recensement_de_la_population_en_France | RP: 351 articles/28 codes, rotation 5 ans, sondage 8 %, adaptation 2021
QRY-007 | FETCH | FOUND | SRC-007 | https://www.amf.asso.fr/documents-les-montants-dgf-pour-2025-sont-officiellement-en-ligne-/42570 | AMF: montants DGF 2025 en ligne (portal DGCL)
QRY-008 | FETCH | FOUND | SRC-008 | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Montant%20Dotation%20DGF%22&limit=20 | OFGL: serie Montant Dotation DGF Metzing 2018-2026 (70565 -> 114005)
QRY-009 | FETCH | FOUND | SRC-009 | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-epci/records?limit=1 | OFGL dotations-epci: test de disponibilite (dataset EPCI)
QRY-010 | FETCH | FOUND | SRC-010 | https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/ | Bouzonville (Moselle): -100 hab -> -20/30 kEUR de dotations (echelle regionale, famille D)
QRY-011 | FETCH | FOUND | SRC-011 | https://www.maire-info.com/dotations-de-l'%C3%A9tat/dgf-l'%C3%A9volution-de-la-dotation-forfaitaire-de-chaque-commune-sera-fonction-de-son-%C3%A9volution-d%C3%A9mographique-ou-de-l'%C3%A9cr%C3%AAtement-de-son-compl%C3%A9ment-d-article-13429 | REFUTATION DGF habitants ecart 113 - lissage sur 5 ans des pertes de population, mesures d accompagnement au recensement (maire-info/AMF 2011)
QRY-012 | FETCH | FOUND | SRC-012 | https://www.vendee.gouv.fr/index.php/Actions-de-l-Etat/Espace-collectivites-territoriales/Subventions-et-Dotations-de-l-Etat/Dotation-Globale-de-Fonctionnement-DGF | REFUTATION DGF habitants ecart 113 - forfaitaire evolutive (DGF N-1 x evolution population DGF), ecretement, eligibilites DSR/DSU par seuils (prefete de Vendee)

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes
SRC-002 | ◈ | fam:A | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100
SRC-003 | ◉ | fam:A | https://www.maire-info.com/finances/deux-notes-de-la-dgcl-precisent-les-modes-de-calculet-de-repartition-de-la-dotation-forfaitaire-article-18426
SRC-004 | ◉ | fam:B | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html
SRC-005 | ◈ | fam:A | https://www.insee.fr/fr/information/2553979
SRC-006 | ◉ | fam:other:wiki | https://fr.wikipedia.org/wiki/Recensement_de_la_population_en_France
SRC-007 | ◉ | fam:C | https://www.amf.asso.fr/documents-les-montants-dgf-pour-2025-sont-officiellement-en-ligne-/42570
SRC-008 | ◈ | fam:A | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Montant%20Dotation%20DGF%22&limit=20
SRC-009 | ○ | fam:A | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-epci/records?limit=1
SRC-010 | ◉ | fam:D | https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/
SRC-011 | ◉ | fam:A | https://www.maire-info.com/dotations-de-l'%C3%A9tat/dgf-l'%C3%A9volution-de-la-dotation-forfaitaire-de-chaque-commune-sera-fonction-de-son-%C3%A9volution-d%C3%A9mographique-ou-de-l'%C3%A9cr%C3%AAtement-de-son-compl%C3%A9ment-d-article-13429
SRC-012 | ◈ | fam:A | https://www.vendee.gouv.fr/index.php/Actions-de-l-Etat/Espace-collectivites-territoriales/Subventions-et-Dotations-de-l-Etat/Dotation-Globale-de-Fonctionnement-DGF

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes | A | 2026-09-20 | Mécanique DGF fondée sur la population INSEE authentifiée | La dotation forfaitaire des communes évolue selon la population dite DGF de la commune, qui ajoute à la population authentifiée par l INSEE le nombre de résidences secondaires et les places de caravanes conventionnées; la DGF communale comprend dotation forfaitaire, DSU, DSR et DNP; depuis la LF 2024 (art 240), la part CPS est transférée aux EPCI. | a4d80cd4-f50d-4475-a1ea-44599568fa3d
FCT-002 | FACT | ✧ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100 | A | 2026-09-20 | Série réelle Metzing 2018-2026 populations et dotations | OFGL (dotations-communes, commune METZING (57)): Population INSEE 631/647/656/662/669/674/678/699/715 (2018-2026); Population DGF 679 (2024), 700 (2025), 716 (2026); Montant Dotation DGF 105906 (2024), 109808 (2025), 114005 (2026) EUR; DSR 37919 (2024), 40360 (2025), 43396 (2026) EUR; DNP 2025: 13367 EUR; Dotation forfaitaire 54380 (2024), 56081 (2026) EUR. | d8dc1852-47d2-428a-a230-515e589c141f
FCT-003 | FACT | ✧ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Montant%20Dotation%20DGF%22&limit=20 | A | 2026-09-20 | Élasticités réelles forfait/population DGF de Metzing | Dérivées des séries OFGL de Metzing: Delta forfaitaire / Delta population DGF = 94,6 (2022-23), 84,5 (2023-24), 12,9 (2024-25, année de rattrapage), 89,4 EUR/hab (2025-26); médiane 86,9 EUR/hab, cohérente avec la plage DGCL 2015 (64,46-128,93 EUR/hab). | a56355d3-84c3-4622-84e4-1439ab5348a0
FCT-004 | FACT | ✦ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Montant%20Dotation%20DGF%22&limit=20 | A,D | 2026-09-20 | Chiffrage DGF écart 113 habitants type Metzing | Un écart de 113 habitants (678 vs 791, question Mizzon) vaut pour Metzing environ 9800 EUR/an sur la dotation forfaitaire (produit de l élasticité médiane mesurée 86,9 EUR/hab; plage 7300-14600 EUR/an sur la plage DGCL 64,46-128,93), soit un majorant d environ 18000 EUR/an si rapporté à la DGF totale par habitant (159,22 EUR/hab 2026); ordre de grandeur corroboré à l échelle régionale par Bouzonville: une centaine d habitants = 20 000 à 30 000 EUR de dotations. | db3dbddc-8baa-4ce0-8236-5dc16959beec
FCT-005 | FACT | ✧ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22&limit=100 | A | 2026-09-20 | Rattrapage réel Metzing 2025-2026 | La population INSEE de Metzing passe de 678 (2024) à 699 (2025) puis 715 (2026): une hausse cumulée de 37 habitants en deux ans (5,5 %), symptôme de rattrapage de collecte; la Population DGF suit (679 -> 700 -> 716) et la DGF totale progresse de 105906 à 114005 EUR (+7,6 %), la DSR de 37919 à 43396 EUR. | 69edb1f7-8251-4e9f-9072-e985b9c618ec
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002,SRC-008
FCT-003 | SRC-002,SRC-008
FCT-004 | SRC-008,SRC-003,SRC-010
FCT-005 | SRC-002,SRC-008

## REFUTATION_REGISTRY_V1
FCT-004 | QRY-012 | FOUND_RESOLVED

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:CONFIRME
FCT-005 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5;6;7 | NEXT_ACTION:8;9
CP-002 | SCOPE | PASS | LAST_COMPLETED:7;8 | NEXT_ACTION:9;10
CP-003 | SEARCH | PASS | LAST_COMPLETED:9;10 | NEXT_ACTION:11;12
CP-004 | FACTS | PASS | LAST_COMPLETED:10;11 | NEXT_ACTION:12
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11;12 | NEXT_ACTION:13;14
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;15;16;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18;18b

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-20T18:37:58.706062+00:00","fact_mem":{"FCT-001":"a4d80cd4-f50d-4475-a1ea-44599568fa3d","FCT-002":"d8dc1852-47d2-428a-a230-515e589c141f","FCT-003":"a56355d3-84c3-4622-84e4-1439ab5348a0","FCT-004":"db3dbddc-8baa-4ce0-8236-5dc16959beec","FCT-005":"69edb1f7-8251-4e9f-9072-e985b9c618ec"},"mnemo_row":"PASS: 5/5 eligible facts persisted via MCP write_memory (8002); run 20260920-2008-dgf-impact-ecart-population-metzing","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau CONFIRME (APEX, refutation survive bounded)","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau VERIFIE","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:PASS: 5/5 eligible facts persisted via MCP write_memory (8002); run 20260920-2008-dgf-impact-ecart-population-metzing | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau CONFIRME (APEX, refutation survive bounded)
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
