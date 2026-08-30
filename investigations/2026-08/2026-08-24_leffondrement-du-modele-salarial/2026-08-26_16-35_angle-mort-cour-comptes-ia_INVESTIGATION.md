# INVESTIGATION — L'angle mort « IA » du rapport annuel de la Cour des comptes sur la Sécurité sociale (2026)

```yaml
RUN_MANIFEST:
  ENGINE_VERSION: 2.9
  STATE: FINAL
  RUN_ID: 20260826-1635-angle-mort-cour-comptes-ia
  PARENT_RUN_ID: NONE
  AS_OF: 2026-08-26
  INPUT_KIND: TOPIC
  MISSION_MODE: INVESTIGATION
  INPUT_REF: NONE
  SUBJECT_SLUG: angle-mort-cour-comptes-ia
  INVESTIGATION_PATH: investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-26_16-35_angle-mort-cour-comptes-ia_INVESTIGATION.md
  SCOPE: lead_question=le rapport Sécu 2026 de la Cour des comptes « ne mentionne jamais l'IA » et n'intègre pas de scénario IA→emploi→recettes : cette affirmation résiste-t-elle à une recherche négative exhaustive ? | object_question=que modélise et que ne modélise pas la Cour dans la soutenabilité du financement social, et que permet d'examiner ce hors-champ ? | period=2025-2026 | geo=France | domains=finances publiques, statistique, IA | actors=Cour des comptes, EPSS, FIPECO, France Travail, SNFOCOS | exclusions=autres rapports Cour (IA service public traité en contexte), évaluation des dépenses de santé | limits=PDF extrait par pdftotext (pas de lecture graphique), rapport 2026 = version vie-publique 303409, aucune vérification indépendante du texte extrait
  COMPLEXITY: $CX_SCORE=7 → $CX=COMPLEX
  CHECKPOINT_SEQ: 1
  LAST_COMPLETED: 18b
  NEXT_ACTION: NONE
  RESUME_COUNT: 0
  ROUTE_OVERRIDES: []
  LOADED_MODULES: [SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, TEMPLATE.md, clusters/ICEBERG.md, clusters/FRAMING.md, clusters/POWER.md]
  DEGRADED_FLAGS: [MNEMO_UNAVAILABLE_PARAMETRE, PDF_EXTRACTION_PDFTOTEXT_SEULE, VIE_PUBLIQUE_ENBREF_NO_TEXT]
MNEMO_ROW: FAILED_PARAM_TRANSMISSION
SELF_WRITE_ROW: PENDING_AT_SERIALIZATION
WRITEBACK_ROW: 0_WRITTEN
```

## MANIPULATION_REPORT

| Symbole | Score | Observation nommée |
|---|---|---|
| Ξ | 7 | Le hors-champ IA du rapport Sécu est le sujet même de l'enquête : omission structurelle documentée par recherche exhaustive, pas par hypothèse |
| € | 5 | Enjeu : un choc d'emploi affecterait les recettes (cotisations 48 %, CSG) ; le coût de l'omission est budgétaire |
| Λ | 6 | Le cadrage « rapport d'application des LFSS » restreint l'horizon (conjoncture) au détriment des canaux structurels (IA) ; l'absence de scénario n'est pas une prise de position |
| Ω | 2 | Faible |
| Ψ | 1 | Faible |
| ↕ | 3 | L'information sur les risques structurels dépend d'une institution sans mandat explicite pour les modéliser |
| Φ | 1 | Faible |
| Σ | 1 | Faible |
| Κ | 2 | Faible (pas de façade documentée) |
| ρ | 3 | Le corpus (stress-test) fournit l'instrument que la Cour ne mobilise pas |
| κ | 1 | Non établi |
| ⫸ | 4 | EPSS (élasticité), FIPECO (masse salariale→cotisations) et la Cour (masse salariale conjoncture) convergent sur la mécanique, sans l'IA |
| ⚔ | 0 | Aucune coordination établie |
| 🌐 | 2 | Graphe institutionnel simple |
| ⏰ | 3 | Deux rapports successifs (2025, 2026) : l'IA outil apparaît en 2025, l'IA risque reste absente en 2026 |

CLUSTERS : ICEBERG (Ξ=7), FRAMING (Λ=6), POWER (↕≥3 non chargé, seuil 4 non atteint). PATTERNS : @PAT[ICEBERG] (omission sélective de canal). THREATS : aucune @THR majeure.

## 1. RÉSUMÉ EXÉCUTIF

**RÉPONSE À L'OBJECT_QUESTION.** Le rapport annuel 2026 de la Cour des comptes sur l'application des lois de financement de la Sécurité sociale (27/05/2026, 296+ pages) **ne contient aucune occurrence de « intelligence artificielle », « IA », « algorithme » ou « robot »** dans son texte intégral (FCT-001, recherche négative exhaustive par extraction PDF). Le rapport modélise pourtant la relation **masse salariale → cotisations** (analyses aux pages 1183-2211 du texte extrait, élasticité de la réduction générale) : le canal de transmission « choc d'emploi → recettes » existe donc dans l'outillage de la Cour, mais **jamais comme conséquence possible de l'IA** (FCT-002). En revanche, la formulation « la Cour ignore l'IA » serait excessive : le rapport 2025 la mentionne deux fois comme **outil recommandé** (modernisation des services support hospitaliers, recouvrement des indus, FCT-003), et la Cour traite l'IA dans des travaux dédiés (service public, FCT-004). **Le hors-champ documenté est donc précis : l'IA comme facteur de risque structurel sur l'assiette sociale, dans le rapport Sécu annuel.** Ce hors-champ n'implique ni faute ni mandat violé : le rapport est un audit d'exécution des LFSS (horizon de prévision court), pas une étude prospective.

**RÉPONSE À LA LEAD_QUESTION (verdict borné).** « La Cour des comptes ne mentionne jamais l'IA » : **confirmé au sens strict pour le rapport Sécu 2026** (recherche exhaustive, méthode documentée, conclusion bornée), **faux au sens absolu** (rapport 2025 : IA outil ; travaux dédiés ailleurs). La formulation publiable exigée par la résolution tour 3 est validée : « Dans son rapport 2026, la Cour analyse la soutenabilité financière sans intégrer explicitement un scénario de choc de masse salariale lié à l'IA ; cela laisse hors champ une question que notre stress-test permet d'examiner. » Le KO sentence du blueprint doit être scindé en deux clauses (fait constaté + interprétation neutre).

**Faits clés** : FCT-001 à FCT-005 (§7). **Gap** : le texte PDF extrait n'a pas été confronté à une seconde extraction indépendante (GAP-001, méthode) ; l'intention de la Cour n'est pas examinée (hors périmètre, non demandée).

## 2. CHRONOLOGIE

| Date | Événement | Source |
|---|---|---|
| 26/05/2025 | Rapport Sécu 2025 : déficit 15,3 Md€ (2024) ; l'IA apparaît ×2 comme outil recommandé | Cour, INSPECTÉ |
| 27/05/2026 | Rapport Sécu 2026 : déficit 21,6 Md€ (2025), 19,4 Md€ prévu (2026) ; zéro mention IA dans le texte intégral | Cour + vie-publique PDF, INSPECTÉ |
| 26/08/2026 | Recherche négative exhaustive (pdftotext + 6 chaînes) : 0 occurrence | présente investigation |
| (contexte) | 22/01/2026 : SNFOCOS relaie un contrôle Cour sur l'IA dans le service public (France Travail « épinglé », Sécu « à la traîne », 93 M€ investis) | SNFOCOS (snippet) |

## 3. DOMAINES

### AXS-001 CONTENU DU RAPPORT 2026 (saturée par recherche exhaustive)

Méthode : PDF vie-publique 303409 (6,7 Mo) → pdftotext -layout → 17 101 lignes → grep 6 chaînes. Résultats :

| Chaîne | Occurrences | Localisation |
|---|---|---|
| « intelligence artificielle » | 0 | - |
| « IA » (mot isolé) | 0 | - |
| « algorithme » | 0 | - |
| « robot » | 0 | - |
| « automatisation » | 2 | lignes 6383 (service des prestations) et 7112 (arrêté des comptes) : hors canal emploi/recettes |

### AXS-002 MODÉLISATION MASSE SALARIALE (saturée)

Le rapport analyse la masse salariale comme déterminant des recettes : lignes 1183 (ralentissement de la masse salariale), 1350-1382 (CSG, croissance masse salariale privée 1,8 %), 2162-2211 (prévisions, effet d'un point de masse salariale), 5482-5536 (GVT, fonction publique). Le canal « masse salariale → cotisations » est donc **outillé**, mais uniquement en horizon conjoncturel (prévisions de recettes à 1-3 ans), jamais comme canal structurel technologique.

### AXS-003 L'IA DANS LES AUTRES TRAVAUX DE LA COUR (contextuelle)

- Rapport Sécu 2025 (INSPECTÉ) : « recourir notamment à l'intelligence artificielle » (services support des hôpitaux) ; « recourir à l'intelligence artificielle pour exploiter les nombreux dossiers concernés » (indus/fraude). L'IA = outil de gestion, pas facteur de risque.
- Contrôles dédiés : SNFOCOS (22/01/2026) : « Intelligence artificielle dans le Service public - France Travail épinglé, la Sécurité sociale à la traîne », 93 M€ investis entre (2022 ?) — la Cour évalue le déploiement de l'IA, pas son effet sur l'assiette. (Snippet, ⁅)

### AXS-004 CE QUE LE HORS-CHAMP PERMET D'EXAMINER (saturée, renvoi stress-test)

Le corpus dispose de l'instrument absent du rapport : élasticité des cotisations (0,95, FIPECO, L2) + décomposition des recettes (cotisations 48 %, EPSS, L2) ⇒ le stress-test « baisse de X % de masse salariale → baisse de recettes » est calculable (voir INV-P0-04). Le rapport de la Cour fournit le référentiel de départ (déficit 21,6 Md€, FCT-005).

## 4. RÉSEAU D'ACTEURS

| Acteur | Rôle | Action documentée | Source | Intent |
|---|---|---|---|---|
| Cour des comptes | Institutionnel ◈ | Rapport Sécu annuel (audit LFSS) ; zéro IA en 2026, IA outil en 2025 | Cour 2025/2026 | N/A (mission constitutionnelle) |
| EPSS | Institutionnel ◈ | Indicateur 1-3-1 (cotisations 48 %) | EPSS, L2 (session) | N/A |
| FIPECO | Analyste ◉ | Élasticité 0,95, masse salariale→cotisations | FIPECO fiche 13, L2 | N/A |
| France Travail | Opérateur ◈ | Objet du contrôle Cour sur l'IA (service public) | SNFOCOS (snippet) | N/A |
| SNFOCOS | Syndicat 🔥 | Relaie le contrôle ; « Sécu à la traîne » | SNFOCOS (snippet) | CLAIMED |

## 5. CHAÎNES / PELOTE

CAUSAL_ROUTE=REQUIRED (pourquoi le hors-champ, et que signifie-t-il).

- **CAU-001 Le mandat explique l'horizon (SUPPORTED, contexte)** : le rapport annuel évalue l'exécution des LFSS (prévisions court terme) ; les canaux structurels (démographie, technologie) relèvent d'autres travaux. L'absence de scénario IA n'est pas une anomalie procédurale documentée. Type : CONTEXT, sourcé (nature du rapport).
- **CAU-002 Le canal existe mais n'est pas branché sur l'IA (SUPPORTED)** : la Cour calcule l'effet d'un point de masse salariale sur les cotisations (lignes 2185, 2204) ; aucune variante « l'IA réduit la masse salariale » n'est testée. Le raccord est techniquement trivial et absent. Type : MECHANISM, sourcé (texte du rapport).
- **CAU-003 Interprétation (HYPOTHESIS, non tranchée)** : omission routinière (pas de scénario structurel par défaut) vs défaut d'anticipation (la Cour n'a pas mandat prospectif sur l'emploi) : aucune intention ne peut être déduite des sources. La formulation d'accusation est interdite (résolution tour 3 §2.4). Type : HYPOTHESIS.
- **GAP-001** : le texte extrait n'a pas été confronté à une seconde extraction indépendante (limite de méthode, non bloquante : 6 chaînes, 0 hit).

SOURCE_PROVENANCE du « −1 % d'emploi ≈ −5,5 Md€ » : chiffre du corpus (stress-test-secu F-005) **non retrouvé dans le rapport Cour** ; l'élasticité FIPECO donne −4,4 Md€ pour −1 % des revenus d'activité (L2). L'écart 5,5 vs 4,4 reste à expliquer (probablement cotisations + CSG + prestations) : signalé, non reconstruit (GAP-002).

## 6. CARTE DIALECTIQUE

- **⟐ Position institutionnelle** : le rapport Sécu est un audit d'exécution ; son périmètre (recettes/dépenses/maîtrise comptable) est défini par la mission d'assistance au Parlement ; la prospective technologique n'en relève pas directement. L'absence d'IA n'est pas un défaut au regard du mandat strict. Support : nature du rapport (FCT-001, contexte).
- **⟐̅ Position critique (corpus stress-test)** : la soutenabilité à moyen terme dépend de canaux structurels ; si la masse salariale décroche des prévisions sans chômage visible (attrition, non-remplacement), les recettes sociales décrochent sans signal précoce ; un rapport qui ne teste pas ce canal laisse l'État découvrir l'érosion avec retard. Support : FCT-002 (canal outillé), INV-P0-01 (non-remplacement non mesuré).
- **Arbitrage** : les deux positions sont compatibles si on distingue fait constaté et interprétation. Le fait est établi (0 occurrence, canal non branché). L'interprétation de gravité dépend du mandat qu'on assigne à la Cour : le dossier ne tranche pas et l'article doit le laisser ouvert (formulation factuelle validée en résolution).

## 7. CARTE DES PREUVES

### FACT_REGISTRY_V1

`FCT-001 | FACT | ✦ | https://www.vie-publique.fr/files/rapport/pdf/303409.pdf (texte intégral extrait, 17 101 lignes) | Cour◈ | 2026-05-27 | angle-mort-cour-comptes-ia | Rapport Sécu 2026 (296+ pages) : 0 occurrence « intelligence artificielle », « IA », « algorithme », « robot » ; « automatisation » ×2 hors canal emploi (prestations, comptes) | mem:-`

`FCT-002 | FACT | ✦ | même texte (lignes 1183, 1350-1382, 2162-2211) | Cour◈ | 2026-05-27 | angle-mort-cour-comptes-ia | Le rapport modélise masse salariale → cotisations (horizon conjoncturel : prévisions recettes, CSG, effet d'un point de masse salariale) sans variante IA | mem:-`

`FCT-003 | FACT | ✦ | https://www.ccomptes.fr/fr/publications/securite-sociale-2025 | Cour◈ | 2025-05-26 | angle-mort-cour-comptes-ia | Rapport Sécu 2025 : « intelligence artificielle » ×2, uniquement comme outil recommandé (services support hôpitaux ; recouvrement des indus) | mem:-`

`FCT-004 | EVIDENCE | ⁅ | https://snfocos.org/intelligence-artificielle-dans-le-service-public-france-travail-epingle-la-securite-sociale-a-la-traine/ (snippet) | SNFOCOS🔥 | 2026-01-22 | angle-mort-cour-comptes-ia | La Cour traite l'IA dans le service public (contrôles dédiés : France Travail épinglé, Sécu « à la traîne », 93 M€ investis) : l'absence dans le rapport Sécu n'est pas une ignorance institutionnelle globale | mem:-`

`FCT-005 | FACT | ✦ | https://www.ccomptes.fr/fr/publications/securite-sociale-2026 | Cour◈ | 2026-05-27 | angle-mort-cour-comptes-ia | Déficit Sécu 21,6 Md€ (2025), 19,4 Md€ prévu (2026) ; 15,3 Md€ (2024, rapport 2025) ; antérieur à tout choc IA documenté | mem:-`

`FCT-006 | INFERENCE | ⁅ | corpus (stress-test-secu F-005) | corpus interne | 2026-08-25 | angle-mort-cour-comptes-ia | « −1 % d'emploi ≈ −5,5 Md€ » : non retrouvé dans le rapport Cour ; l'élasticité FIPECO (0,95) donne −4,4 Md€ pour −1 % des revenus d'activité ; écart 5,5 vs 4,4 non expliqué (GAP-002) | mem:-`

### TRACE_MATRIX

| FCT | QRY/SRC | REFUTATION_SEARCHED | Résultat |
|---|---|---|---|
| FCT-001 | PDF intégral (pdftotext) + QRY-1 site:ccomptes | QRY-2 « cour des comptes sécurité sociale 2026 IA emploi recettes » | NONE : aucun hit IA dans le rapport 2026 (0/6 chaînes) |
| FCT-003 | QRY-1 | QRY-2 | CONTRADICTION PARTIELLE TROUVÉE : le rapport 2025 contient IA ×2 (outil) → le « jamais » du corpus est scindé |
| FCT-005 | communiqué Cour 2026 | QRY-3 | NONE (EPSS concordant, L2) |

### CONTRADICTION_LEDGER

1. **« La Cour ne mentionne jamais l'IA » (corpus/blueprint)** vs **rapport 2025 (IA ×2)** : résolue par scission : vrai pour le rapport 2026 (recherche exhaustive), faux au sens absolu. Le KO sentence doit être reformulé en deux clauses.
2. **« −1 % d'emploi ≈ −5,5 Md€ » (corpus)** vs **−4,4 Md€ (élasticité FIPECO)** : écart non expliqué, consigné, non reconstruit (GAP-002).

### EDI

Familles : A ⟐ (Cour, EPSS, FIPECO), C/🔥 (SNFOCOS), D (presse/presse spécialisée) partiel. B (contre-audit indépendant du rapport) et E (académique) absents. La recherche négative elle-même est rejouable (méthode documentée) : c'est la garantie principale.

## 8. PÉRIMÈTRE & LIMITES

**Inclusions** : rapport Sécu 2026 (texte intégral), rapport Sécu 2025 (page publiée), contexte travaux Cour sur l'IA, mécanique masse salariale→cotisations. **Exclusions** : évaluation des dépenses (Ondam, dentaire, hospitalisations), travaux prospectifs de la Cour hors Sécu, intention de la Cour (hors périmètre). **Limites** : extraction pdftotext seule (pas de relecture humaine du PDF), version vie-publique 303409 (une seule édition), SNFOCOS en snippet (page non inspectée), GAP-002 (écart 5,5 vs 4,4) non résolu.

## SOURCES

1. Cour des comptes, « Sécurité sociale 2026 », 27/05/2026, page publication (INSPECTÉ) : https://www.ccomptes.fr/fr/publications/securite-sociale-2026
2. Rapport complet (PDF, INSPECTÉ par pdftotext, 17 101 lignes) : https://www.vie-publique.fr/files/rapport/pdf/303409.pdf
3. Cour des comptes, « Sécurité sociale 2025 », 26/05/2025 (INSPECTÉ) : https://www.ccomptes.fr/fr/publications/securite-sociale-2025
4. SNFOCOS, « Intelligence artificielle dans le Service public - France Travail épinglé, la Sécurité sociale à la traîne », 22/01/2026 (snippet) : https://snfocos.org/intelligence-artificielle-dans-le-service-public-france-travail-epingle-la-securite-sociale-a-la-traine/
5. EPSS, Synthèse Financement (L2, session) : https://evaluation.securite-sociale.fr/home/financement/SyntheseFinancement.html
6. FIPECO, fiche 13 « Les cotisations sociales », 20/06/2026 (L2, session) : https://www.fipeco.fr/fiche/Les-cotisations-sociales

## REQUEST_LOG

| # | Type | Cible | Résultat |
|---|---|---|---|
| 1 | @FETCH | ccomptes.fr securite-sociale-2026 | 200, INSPECTÉ (page) |
| 2 | @WEB | site:ccomptes.fr Sécu 2026 IA | 0 hit direct (participation citoyenne + RPA seulement) |
| 3 | @WEB | Cour Sécu 2026 IA emploi masse salariale | snippets 2025 + SNFOCOS identifiés |
| 4 | @FETCH | ccomptes.fr securite-sociale-2025 | 200, INSPECTÉ (IA ×2 outil) |
| 5 | @FETCH | vie-publique 303409.pdf | UNSUPPORTED (PDF) → dégradation |
| 6 | @TERM | curl + pdftotext + grep ×6 chaînes | 0 « IA/intelligence artificielle/algorithme/robot » ; « automatisation » ×2 hors sujet |
| 7 | @WEB | réfutation | NONE |
| 8 | @MNEMO_Q | recherche mémoire | ÉCHEC paramètres (session) → MNEMO_UNAVAILABLE |

**Gate 19a (exécuté 14h07 UTC) :** verdict **BLOCKED** (branche protégée main). Checks : naming PASS, no-em-dash PASS, tests extractors PASS. state_id `d84bc725210e3327e606a7a32aa511b7749cbd8de8d3ad0db8908f509a782c6e`. Aucune certification de livraison sur main : worktree requis (voir P0-01).

---
*Fin du dossier. Conclusion bornée : zéro occurrence IA dans le rapport Sécu 2026 (méthode exhaustive) ; l'IA outil existe en 2025 ; l'interprétation reste ouverte.*
