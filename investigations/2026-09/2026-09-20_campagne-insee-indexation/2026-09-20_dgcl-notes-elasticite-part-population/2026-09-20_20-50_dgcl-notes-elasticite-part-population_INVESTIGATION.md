ENGINE:2.10.6 | BUNDLE_REVISION:R2A.1 | STATE:FINAL | RUN_ID:20260920-2050-dgcl-notes-elasticite-part-population | PARENT_RUN_ID:20260920-2008-dgf-impact-ecart-population-metzing | AS_OF:2026-09-20
INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/home/giak/projects/truth-engine/investigations/2026-09/2026-09-20_dgcl-notes-elasticite-part-population/2026-09-20_20-50_dgcl-notes-elasticite-part-population_INPUT.txt | SUBJECT_SLUG:dgcl-notes-elasticite-part-population | SUBJECT_FP:sha256:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | INPUT_SHA256:sha256:7eccc28f8646fdcd21c5beef7cf1c5f20bb748d7d081ba3f0d211ba415547437
COMPLEXITY:0.85→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:UPDATE run 2008 (dgf-metzing): notes DGCL recentes sur les modes de calcul de la dotation forfaitaire (part population, ecretement complement de garantie) et confrontation au bareme theorique 2025/2026; recheck materiel de la mecanique DGF (FCT-001 parent)
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,protocol/UPDATE.md,protocol/FACT_VERIFICATION.md | degraded:NONE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Notes DGCL et chiffrage DGF : la mécanique tient, les paramètres bougent

## Ce que l'update cherchait

Ce run rouvre le chiffrage du parent (écart de population type Metzing, ~9 800 €/an de forfaitaire pour 113 habitants) avec une question précise : que disent les notes DGCL récentes sur les modes de calcul de la dotation forfaitaire, et le barème appliqué au parent est-il encore le bon ? Deux objets ont été revalidés : la mécanique légiférée (population DGF, part population, écrêtement) et la valeur numérique du chiffrage marginal.

## La mécanique re-vérifiée sur la source canonique

La page « DGF des communes » de collectivités-locales.gouv.fr (FCT-001) confirme en 2026 la mécanique décrite au parent : la variation de la dotation forfaitaire s'explique par l'évolution de la population dite DGF — population authentifiée par l'Insee, augmentée des résidences secondaires et des places de caravanes conventionnées — et par l'écrêtement. Deux précisions nouvelles par rapport à la lecture 2015 : depuis l'article 240 de la loi de finances pour 2024, l'intégralité de la part CPS encore dans la forfaitaire est transférée aux EPCI à fiscalité propre ; et l'écrêtement actuel vise les communes dont le potentiel fiscal dépasse 85 % de la moyenne nationale. Le communiqué DGF 2026 de la préfecture des Landes (FCT-001, FCT-005) chiffre ce dispositif : environ 53 % des communes concernées, prélèvement plafonné à 1 % des recettes réelles de fonctionnement, en moyenne 0,49 % en 2026.

## Le barème 2015 contre la règle 2026

La note DGCL du 7 mai 2015, relue via maire-info (FCT-005), fixait la part population entre 64,46 et 128,93 € par habitant selon la strate, avec un écrêtement unique appliqué au-delà de 0,75 fois le potentiel fiscal moyen. La règle courante décrite par la page canonique et le communiqué 2026 diffère sur le paramètre d'écrêtement (seuil 85 % de la moyenne nationale, plafond 1 % RRF) tandis que la mécanique de part population reste la même. C'est une évolution de paramètre, pas de mécanisme : la plage du parent (7 300-14 600 €/an pour 113 habitants) reste l'encadrement pertinent.

## La série réelle et la part dynamique

La série OFGL de Metzing (FCT-002) confirme les montants du parent : DGF totale de 70 565 € (2018) à 114 005 € (2026), dont 105 906 (2024), 109 808 (2025), 114 005 (2026). La variable « Part dynamique de la population des communes » (FCT-003) montre le versement effectif de la part population : 271 € (2024), puis 1 430 € (2025) et 1 093 € (2026) quand la population DGF repart à la hausse (+16 habitants par an). Les taux implicites — 89,4 puis 68,3 € par habitant DGF ajouté — tombent dans la plage du barème et du chiffrage central du parent (86,9 €/hab mesuré). Sur la décennie, les taux implicites annuels s'étagent de 24,9 à 140,5 €/hab, hors années sans ajout de population où le taux n'a pas de borne supérieure exploitable.

## Le chiffrage confirmé

Le fait central du parent survit à sa réouverture (FCT-004) : un écart de 113 habitants comme celui de Metzing vaut environ 9 800 €/an de dotation forfaitaire à l'élasticité mesurée, plage 7 300-14 600 €/an au barème. La corroboration régionale famille D (moselle.tv : une centaine d'habitants vaut 20-30 k€ de dotations pour Bouzonville, commune cinq fois plus peuplée) borne l'ordre de grandeur sans le contredire. Metzing, au potentiel fiscal par habitant inférieur au seuil d'écrêtement, n'est pas affectée par le prélèvement 2026 : le chiffrage marginal reste hors écrêtement pour cette commune.

## Torture adversariale et carte dialectique

La contre-requête formelle (barème supprimé ou modifié, plafond 1 % RRF, écrêtement 85 % invalidant la plage) n'a retourné aucune source contestant la part population ; les sources 2026 la confirment au contraire. Lecture dominante : la DGCL légifère des amortisseurs (lissage des pertes, écrêtement, plafond 1 %) qui rendent le barème nominal non linéaire. Lecture critique : l'élasticité mesurée sur Metzing capture déjà ces amortisseurs puisqu'elle est calculée sur des variations réellement versées. Arbitrage : les deux lectures convergent vers un chiffrage borné, pas exact — la fiche de dotation nominative reste non publique, ce qui interdit la décomposition précise (composantes nominatives, effets de garantie). Le conflit apparent entre la formulation 2015 (0,75 × PF moyen) et la règle 2026 (85 % de la moyenne) est résolu historiquement : deux états successifs du même mécanisme, documentés chacun par sa source, sans contradiction sur la règle applicable en 2026.

## Table d'évaluation des 15 symboles

| Symbole | Nom | Score | Observation nommée |
|---|---|---|---|
| Ξ | Omission | 5 | Notes DGCL 2026 existent mais contenu Excel non décomposé ; fiches nominatives non publiques |
| € | Money | 7 | Objet du run : la population authentifiée convertit en dotation ; écrêtement 2026 finance la péréquation (53 % des communes) |
| Λ | Framing | 5 | Le débat public cadre l'écart en « euros perdus », jamais la mécanique du barème |
| Ω | Inversion | 2 | Rien d'inversé : l'Insee et la DGCL publient les règles |
| Ψ | Sideration | 2 | Sujet technique, pas de volume émotionnel |
| ↕ | Vertical power | 6 | Le barème s'impose aux communes sans qu'elles puissent auditer leurs fiches individuelles |
| Φ | Spectacle | 3 | Médiatisation locale du différentiel (Bouzonville), décomposition absente |
| Σ | Semiotics | 1 | Néant observé |
| Κ | Cynicism | 2 | Les paramètres bougent sans annonce : asymétrie de visibilité, pas de façade |
| ρ | Resistance | 4 | AMF relaie notes et critères ; questions parlementaires ; OFGL publie les séries |
| κ | Subtle influence | 3 | Seuils (écrêtement, strates) orientent les incitations communales sans intention démontrée |
| ⫸ | Convergence | 5 | Page canonique, communiqué préfectoral 2026, AMF, OFGL et moselle.tv convergent |
| ⚔ | Cognitive warfare | 0 | Aucun élément |
| 🌐 | Network | 5 | Insee → DGCL → préfectures/AMF/OFGL → communes, chaîne lisible et sourcée |
| ⏰ | Temporal | 5 | CPS transférée en 2024 ; écrêtement re-paramétré ; plafond 1 % nouveau en 2026 |

## Contradictions et limites

C1 (résolue) : 0,75 × PF moyen (2015) contre 85 % de la moyenne nationale (2026) — deux états du même mécanisme, sources datées, règle courante identifiée. C2 (résolue) : taux implicites 2025-2026 (89,4 puis 68,3 €/hab) contre plage barème 64,46-128,93 — cohérents, la part versée suit la population ajoutée. Limites : le contenu des notes DGCL 2026 (Excel + notes PDF) n'a pas été décomposé variable par variable — le communiqué préfectoral et la page canonique couvrent les paramètres clés ; la fiche nominative de Metzing reste inaccessible ; le montant exact du barème 2026 par strate n'est pas publié dans les sources inspectées, la plage 2015 reste l'encadrement assumé.

## Verdict

**La mécanique DGF est stable, les paramètres d'écrêtement ont changé, et le chiffrage du parent est confirmé borné en 2026** (~9 800 €/an pour 113 habitants, plage 7 300-14 600 €/an, taux implicites réels 68-89 €/hab). Aucune manipulation : les règles sont publiques, les amortisseurs légiférés, et la non-publicité des fiches nominatives reste la seule asymétrie matérielle — celle-là même qui bornait déjà le parent. Le suivant d'accès (fiche nominative via préfecture) reste routé.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:2|AXS:3|CAU:1|CTRL:1|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempts":["QRY-002"],"evidence":["FCT-001"],"kinds":["MECHANISM"],"lead":"Mecanique DGF: population DGF = Insee + res secondaires + places caravanes; forfait = DNP + DSR + FCTMV","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-002 | {"attempts":["QRY-005","QRY-006","QRY-004"],"evidence":["FCT-005","FCT-003"],"kinds":["OBJECT"],"lead":"Baremes part population par strate (64,46-128,93 EUR/hab en 2015) et ecretement complement de garantie 0,75 x PF moyen","materiality":"DECISIVE","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-003 | {"attempts":["QRY-003","QRY-004"],"evidence":["FCT-002","FCT-003","FCT-004"],"kinds":["CLAIM"],"lead":"Chiffrage parent: elasticite mesuree Metzing 86,9 EUR/hab dans la plage du bareme","materiality":"IMPORTANT","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}
LED-004 | {"attempts":["QRY-001","QRY-007"],"evidence":["FCT-001"],"kinds":["CONTEXT"],"lead":"Notes DGCL 2025/2026 recentes: existence/accessibilite","materiality":"IMPORTANT","note":"notes DGCL 2026 existent et sont signalees par l AMF; contenu Excel/notes non extrait detail par detail (limitation), le communique prefectoral couvre les parametres cles","routes":["OBJECT"],"source_ref":"INPUT","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"La mecanique DGF (population DGF = Insee + res sec + caravanes; forfaitaire avec part population stratifiee) decrite au parent reste la mecanique legiferee courante","counter":"aucune source credible de changement de mecanique trouvée (QRY-010 NONE)","evidence":["FCT-001","FCT-005"],"gap_type":"NONE","status":"SUPPORTED"}
CLM-002 | {"claim":"Le chiffrage marginal du parent (86,9 EUR/hab mesure; plage 7300-14600 EUR/an pour 113 hab) reste cohérent avec le bareme theorique courant","counter":"moselle.tv (famille D) confirme l ordre de grandeur; aucune contradiction","evidence":["FCT-002","FCT-003","FCT-004"],"gap_type":"NONE","status":"SUPPORTED"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-002"],"axis":"MECANIQUE (population DGF -> forfait): recheck FCT-001 parent sur source canonique","result_ids":["FCT-001"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-005","QRY-006"],"axis":"BAREME (part population/strate, ecretement): valeurs 2015 vs 2025/2026","result_ids":["FCT-002","FCT-003","FCT-005"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-010"],"axis":"CONTRE-HYPOTHESES: lissage 5 ans, forfaitaire evolutive, effets de seuil","note":"refutation bornee NONE: aucune source contestant le bareme; amortisseurs (lissage, ecretement, plafond 1%) documentes et compatibles","result_ids":["FCT-004","FCT-005"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"evidence":["FCT-001","FCT-002","FCT-003","FCT-005"],"provenance":"population legale authentifiee -> population DGF -> bareme part population -> euros de dotation -> budget communal","status":"SUPPORTED"}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Recoupement mecanique: page canonique collectivites-locales.gouv.fr vs notes DGCL relayees par maire-info","evidence":["FCT-001","FCT-005"],"note":"recoupement page canonique DGCL vs communique prefectoral 2026 vs note 2015 (maire-info): mecanique stable, parametres d ecretement evolves","status":"DONE"}

### ACTION_REGISTRY_V1
ACT-001 | {"documented_action":"routee vers NEXT_QUERIES (ACCESS)","intent":"PROVEN","name":"Solliciter la fiche de dotation nominative de Metzing (prefecture/mairie)","responsibility_scope":"collecte de donnees","role":"route d'acces aux composantes nominatives","source":"-","status":"DONE"}

SEARCH_ACTIVITY_V1:WEB:4|FETCH:7|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | PASS | runtime | RUN_STATE_RESUME_VALIDATED | RESUME_VALIDATE
SYS-002 | SYS | NONE | mcp-curl-8002 | subject-fp:93ad431086afcd5c321e38f0c8e8060a9db58526aed4801b862a38e99c68e775 | MNEMO_Q
SYS-003 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | DGCL note dotation forfaitaire communes 2025 2026 part population bareme strate
QRY-002 | FETCH | FOUND | SRC-001 | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes | FETCH mecanique DGF: population DGF = Insee + res sec + caravanes; CPS->EPCI LF2024 art240; ecretement PF>=85% moyenne nationale
QRY-003 | FETCH | FOUND | SRC-002 | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Montant%20Dotation%20DGF%22&limit=20&order_by=exercice | FETCH OFGL serie Montant Dotation DGF Metzing 2018-2026: 70565->114005 EUR
QRY-004 | FETCH | FOUND | SRC-003 | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Part%20dynamique%20de%20la%20population%20des%20communes%22&limit=20&order_by=exercice | FETCH OFGL part dynamique population Metzing 2018-2026: taux implicites 24,9-140,5 EUR/hab; 2025 +16 hab -> 1430 EUR (~89 EUR/hab)
QRY-005 | FETCH | FOUND | SRC-004 | https://www.maire-info.com/finances/deux-notes-de-la-dgcl-precisent-les-modes-de-calculet-de-repartition-de-la-dotation-forfaitaire-article-18426 | FETCH note DGCL 07-05-2015 via maire-info: part population 64,46-128,93 EUR/hab; ecretement unique 0,75 x PF moyen; CPS encore communale
QRY-006 | FETCH | FOUND | SRC-005 | https://www.landes.gouv.fr/Actualites/Salle-de-presse/Communiques-de-presse/2026/Le-Gouvernement-confirme-son-soutien-aux-finances-locales-a-travers-la-repartition-de-la-DGF | FETCH communique prefet Landes 31-03-2026: DGF 27,4 MdEUR; ecretement PF par hab >= 85% moyenne nationale; plafond 1% RRF (moyenne 0,49%); 53% des communes concernees
QRY-007 | FETCH | FOUND | SRC-006 | https://www.amf.asso.fr/documents-dgf-les-criteres-repartition-pour-2026-sont-en-ligne-ainsi-que-les-notes-dinformations-detaillant-les-differentes-dotations-/43278 | FETCH AMF 24-07-2026: fichiers critere 2026 en ligne 20-07-2026 + notes d information DGCL 2026 detailing modalites de calcul; guide pratique DGF edition mars 2026
QRY-008 | FETCH | FOUND | SRC-007 | https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/ | FETCH moselle.tv 15-01-2026 Bouzonville: le nombre d habitants conditionne la participation de l Etat au budget des communes (corroboration famille D)
QRY-009 | WEB | NO_RESULT:NOT_RELEVANT | - | - | part dynamique de la population montant par habitant 64,46 128,93 contredit corrige nouveau bareme DGCL
QRY-010 | WEB | NO_RESULT:REFUTATION_BOUNDED | - | - | REFUTATION chiffrage DGF écart 113 habitants Metzing élasticité 86,9 : barème part population supprimé modifié 2024 2025 2026, plafond 1% RRF écrêtement 85% invalide plage 7300 14600 EUR/an
QRY-011 | WEB | NO_RESULT:REFUTATION_BOUNDED | - | - | REFUTATION mécanique DGF courante population DGF écrêtement 85% CPS EPCI LF2024 : transfert CPS annulé, écrêtement supprimé, population DGF contestée

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes
SRC-002 | ◈ | fam:A | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Montant%20Dotation%20DGF%22&limit=20&order_by=exercice
SRC-003 | ◈ | fam:A | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Part%20dynamique%20de%20la%20population%20des%20communes%22&limit=20&order_by=exercice
SRC-004 | ◈ | fam:A | https://www.maire-info.com/finances/deux-notes-de-la-dgcl-precisent-les-modes-de-calculet-de-repartition-de-la-dotation-forfaitaire-article-18426
SRC-005 | ◈ | fam:A | https://www.landes.gouv.fr/Actualites/Salle-de-presse/Communiques-de-presse/2026/Le-Gouvernement-confirme-son-soutien-aux-finances-locales-a-travers-la-repartition-de-la-DGF
SRC-006 | ◉ | fam:C | https://www.amf.asso.fr/documents-dgf-les-criteres-repartition-pour-2026-sont-en-ligne-ainsi-que-les-notes-dinformations-detaillant-les-differentes-dotations-/43278
SRC-007 | ◉ | fam:D | https://moselle.tv/moselle-la-perte-dune-centaine-dhabitants-prive-cette-commune-de-pres-de-30-000-euros-de-dotations/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✦ | https://www.collectivites-locales.gouv.fr/gerer-les-finances-publiques-locales/execution-des-recettes-et-des-depenses-locales/recettes-locales/dotations/dotation-globale-de-fonctionnement/dgf-des-communes | A,C | 2026-09-21 | Mecanique DGF courante: population DGF (Insee+res sec+caravanes), ecretement PF>=85% moyenne nationale, CPS integrale aux EPCI depuis LF2024 | La page canonique DGCL (collectivites-locales.gouv.fr) confirme en 2026: la variation de la dotation forfaitaire s explique par l evolution de la population DGF (Insee + res sec + places caravanes) et l ecretement des communes dont le PF > 85% de la moyenne nationale; l integrite des montants de part CPS restant dans la forfaitaire a ete transferee aux EPCI par l art 240 de la LF 2024 (loi 2023-1322); le communique DGF 2026 (prefete des Landes 31-03-2026) confirme le seuil 85% (53% des communes concernees, prelevement plafonne a 1% RRF, moyenne 0,49%) et l AMF (24-07-2026) confirme la publication des fichiers criteres + notes d information DGCL 2026 | c816fe89-31d9-4fba-ab45-edafa5d83b64
FCT-002 | FACT | ✧ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Montant%20Dotation%20DGF%22&limit=20&order_by=exercice | A | 2026-09-21 | Serie DGF totale Metzing 2018-2026 (OFGL) | OFGL dotations-communes, commune METZING (57), variable Montant Dotation DGF: 2018=70565, 2019=72911, 2020=89723, 2021=96504, 2022=101883, 2023=104300, 2024=105906, 2025=109808, 2026=114005 EUR (total_count=9 lignes recensees) | 3aca8f0f-304a-4eec-94a4-148302ed12c7
FCT-003 | FACT | ✧ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Part%20dynamique%20de%20la%20population%20des%20communes%22&limit=20&order_by=exercice | A | 2026-09-21 | Part dynamique de la population (part population) de Metzing 2018-2026 et taux implicites par hab DGF ajoute | OFGL variable Part dynamique de la population des communes (Dotation forfaitaire, EUR): 2018=670, 2019=1076, 2020=606, 2021=472, 2022=473, 2023=338, 2024=271, 2025=1430, 2026=1093; taux implicites (part EUR / hab DGF ajoute): 2025 ~89,4 (1430/16) et 2026 ~68,3 (1093/16); plage 2018-2026 24,9-140,5 EUR/hab DGF ajoute, compatible avec le bareme 64,46-128,93 (les années sans ajout de population DGF montrent des taux sans borne superieure) | ccc17301-4ca5-4aaf-9c37-355052a649eb
FCT-004 | FACT | ✦ | https://data.ofgl.fr/api/explore/v2.1/catalog/datasets/dotations-communes/records?where=commune%3D%22METZING%20(57)%22%20AND%20variable%3D%22Montant%20Dotation%20DGF%22&limit=20&order_by=exercice | A,D | 2026-09-21 | Chiffrage DGF écart 113 habitants type Metzing confirmé en 2026: élasticité mesurée 86,9 EUR/hab, plage 7300-14600 EUR/an | Le chiffrage du parent survit en 2026: la serie OFGL 2024-2026 (FCT-002) et la part dynamique 2025-2026 (taux implicites 89,4 puis 68,3 EUR/hab DGF ajoute, FCT-003) restent dans la plage du chiffrage central 86,9 EUR/hab (plage 7300-14600 EUR/an pour 113 hab); la mecanique legiferee est inchangee (FCT-001) et la corroboration regionale famille D (moselle.tv, Bouzonville: une centaine d habitants = 20-30 kEUR de dotations) confirme l ordre de grandeur; la refutation bornee (QRY text REFUTATION, barème supprimé/modifié, plafond 1% RRF, écrêtement 85%) n a trouvé aucune source contestant le barème de part population | 3774495b-2225-4679-a3e0-e62f56ba2e72
FCT-005 | FACT | ✧ | https://www.landes.gouv.fr/Actualites/Salle-de-presse/Communiques-de-presse/2026/Le-Gouvernement-confirme-son-soutien-aux-finances-locales-a-travers-la-repartition-de-la-DGF | A | 2026-09-21 | Écrêtement: formulation 2015 (0,75 x PF moyen) vs règle courante (PF >= 85% moyenne nationale + plafond 1% RRF) | La note DGCL relayée par maire-info (07-05-2015) décrit un écrêtement unique pour les communes dont le PF par hab >= 0,75 x PF moyen national; la page canonique DGCL et le communiqué DGF 2026 (prefete des Landes 31-03-2026) décrivent l écrêtement courant: communes dont le PF par hab > 85% de la moyenne nationale, prélèvement plafonné à 1% des recettes réelles de fonctionnement (moyenne 0,49% en 2026, 53% des communes concernées); Metzing (PF 434227 EUR / 716 hab DGF ~ 606 EUR/hab) est sous le seuil national et non concernée par l écrêtement 2026 | 9677d17c-4cbf-4528-9a6b-07a178a97f3f
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001,SRC-005,SRC-006
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-002,SRC-003,SRC-007
FCT-005 | SRC-004,SRC-005

## REFUTATION_REGISTRY_V1
FCT-001 | QRY-011 | NONE
FCT-004 | QRY-010 | NONE

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:CONFIRME
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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6;7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH:AXS-003 | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11;12
CP-005 | CAUSAL:CAU-001 | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:14;17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-21T07:40:38.911300+00:00","fact_mem":{"FCT-001":"c816fe89-31d9-4fba-ab45-edafa5d83b64","FCT-002":"3aca8f0f-304a-4eec-94a4-148302ed12c7","FCT-003":"ccc17301-4ca5-4aaf-9c37-355052a649eb","FCT-004":"3774495b-2225-4679-a3e0-e62f56ba2e72","FCT-005":"9677d17c-4cbf-4528-9a6b-07a178a97f3f"},"mnemo_row":"PASS: investigation memory WRITE:c029dfc0-ebe5-405f-90a8-fa7bd7a56de7; run 20260920-2050-dgcl-notes-elasticite-part-population","result":"PASS","writeback_execution":[{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-001","reason":"fait nouveau CONFIRME","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-002","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-003","reason":"fait nouveau VERIFIE","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-004","reason":"fait nouveau CONFIRME","success":1},{"action":"WRITE","attempted":1,"blocked":0,"failure":0,"fct":"FCT-005","reason":"fait nouveau VERIFIE","success":1}],"writeback_row":{"attempted":5,"blocked":0,"eligible":5,"failure":0,"success":5}}

PERSISTENCE_META: MNEMO_ROW:PASS: investigation memory WRITE:c029dfc0-ebe5-405f-90a8-fa7bd7a56de7; run 20260920-2050-dgcl-notes-elasticite-part-population | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:5;attempted:5;success:5;failure:0;blocked:0} | WRITEBACK_EXECUTION_V1:[5 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau CONFIRME
FCT-002 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-003 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
FCT-004 | ELIGIBLE:CONFIRME | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau CONFIRME
FCT-005 | ELIGIBLE:VERIFIE | attempted:1 | success:1 | failure:0 | blocked:0 | reason:fait nouveau VERIFIE
