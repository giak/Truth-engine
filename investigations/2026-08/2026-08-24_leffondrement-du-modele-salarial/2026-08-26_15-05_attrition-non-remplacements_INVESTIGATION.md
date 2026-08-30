# INVESTIGATION — Attrition silencieuse et non-remplacements : le cas bancaire français

**Version :** v2 reconstruite intégralement le 26/08/2026 ~15h45 CEST après rejet de la v1 (fragment invalide). La v1 est remplacée au sens KERNEL §18b (replacement, jamais mutation en place).

```yaml
RUN_MANIFEST:
  ENGINE_VERSION: 2.9
  STATE: FINAL
  RUN_ID: 20260826-1505-attrition-non-remplacements
  PARENT_RUN_ID: NONE
  AS_OF: 2026-08-26
  INPUT_KIND: TOPIC
  MISSION_MODE: INVESTIGATION
  INPUT_REF: NONE
  SUBJECT_SLUG: attrition-non-remplacements
  INVESTIGATION_PATH: investigations/2026-08/2026-08-24_leffondrement-du-modele-salarial/2026-08-26_15-05_attrition-non-remplacements_INVESTIGATION.md
  SCOPE: lead_question=les affirmations du corpus (attrition silencieuse « −5 000 à −7 000 postes/an par l'IA » ; chiffres FBF, FO, BMO) sont-elles vérifiables ? | object_question=par quels mécanismes mesurables ou non mesurés l'emploi bancaire français s'érode-t-il, et l'IA y joue-t-elle un rôle documenté ? | period=2023-2026 | geo=France | domains=emploi, statistique publique, relations sociales, numérique | actors=FBF, AFB, Société Générale, BNP Paribas, Crédit Agricole, FO Banques/FEC-FO, DARES, France Travail, État | exclusions=assurances et télécoms (sources primaires non accessibles dans les bornes d'exécution) | limits=MNEMO paramétré indisponible, DARES socket fermé ×2, BFM périmètre imprécis
  COMPLEXITY: $CX_SCORE=7 → $CX=COMPLEX
  CHECKPOINT_SEQ: 2
  LAST_COMPLETED: 18b
  NEXT_ACTION: NONE
  RESUME_COUNT: 0
  ROUTE_OVERRIDES: []
  LOADED_MODULES: [SYMBOLS.md, PATTERNS.md, THREATS.md, GATES.md, TEMPLATE.md, clusters/ICEBERG.md, clusters/MONEY.md, clusters/FRAMING.md, clusters/POWER.md, clusters/RESISTANCE.md, clusters/FRAGMENTATION.md]
  DEGRADED_FLAGS: [MNEMO_UNAVAILABLE_PARAMETRE (search_memory/write_memory : paramètres non transmis ×3), DARES_ACCESS_SOCKET_FERME_X2_SESSION, VIE_PUBLIQUE_NO_TEXT, DREES_PDF_NON_INSPECTE]
MNEMO_ROW: FAILED_PARAM_TRANSMISSION (loggé, non inventé)
SELF_WRITE_ROW: PENDING_AT_SERIALIZATION
WRITEBACK_ROW: 0_WRITTEN_0_FAILURES_ELIGIBLES_NON_ECRITS (fcts ✧ éligibles mais MNEMO paramétré indisponible)
```

## 1. RÉSUMÉ EXÉCUTIF

**RÉPONSE À L'OBJECT_QUESTION.** Le non-remplacement est le canal principal et documenté de l'érosion de l'emploi bancaire français : effectifs 368 800 fin 2025 (−0,7 %), recrutements 34 400 (−10,2 % sur un an), départs en repli (−11 %), alternants 18 100 (−8,6 %), et Société Générale annonce −1 800 postes nets d'ici fin 2027 « sans plan de départs », par départs naturels (FCT-001 à FCT-006). Aucun instrument public ne mesure le taux de remplacement des postes libérés : les MMO de la DARES enregistrent les embauches et les fins de contrat, pas leur remplacement ; la demande du syndicat FO d'un « suivi consolidé des effectifs (ETP, taux de remplacement…) » le confirme par l'absurde (FCT-011). En revanche, la causalité « IA → non-remplacement » n'est établie par aucune source inspectée : les moteurs historiques documentés sont la digitalisation et les fermetures d'agences ; l'IA apparaît comme couche invoquée, non quantifiée (FCT-008, FCT-010). **La bonne formulation publiable est : nous savons mesurer les licenciements ; nous mesurons mal le poste qui disparaît faute de remplacement.**

**RÉPONSE À LA LEAD_QUESTION (verdict borné).** Le chiffre « −5 000 à −7 000 postes/an supprimés par l'IA dans banques + assurances + télécoms » est une reconstruction fondée sur une hypothèse de turnover naturel, pas une observation : il est rétrogradé (FCT-010, EPI=INFERENCE, tier ⁅). Les grandeurs FBF (368 800, −0,7 %, turnover 7,7 %) sont confirmées par source primaire (✦/✧). Le qualificatif FO « PSE silencieux hors de tout cadre juridique et légal » est une citation syndicale exacte et datée, à attribuer comme telle. La part « IA » de l'érosion demeure une incitation structurelle probable (asymétrie fiscale, corpus lignée A), pas une mesure.

**Acteurs clés.** FBF/AFB (◈ opérateur, discours « baisse maîtrisée ») ; banques (SG ◈, annonce −1 800) ; FO Banques (🔥 contre-pouvoir, « PSE silencieux ») ; DARES (statisticien, inaccessible) ; France Travail (BMO 2026).

**Impacts documentés.** −1 800 postes nets SG 2026-2027 ; recrutements bancaires au plus bas depuis 13 ans (BFM ○) ; alternants −8,6 % (repli politique publique) ; alerte FO sur RPS (AVC, burnout) non vérifiée primairement (FCT-012, ⁅).

**Gaps majeurs.** (1) Élasticité réelle IA → non-remplacement non mesurée ; (2) MMO DARES inaccessible (socket fermé ×2 en session, ×2 antérieurement) ; (3) chiffres assurances/télécoms non revérifiés ; (4) 4,1 Md€ de bénéfice SG cités par FO sans source primaire inspectée.

## 2. CHRONOLOGIE (événements sourcés, non forcés)

| Date | Événement | Source |
|---|---|---|
| 2023 | Effectifs bancaires en hausse (référence « après avoir connu une hausse en 2023 ») | FBF ◈ |
| 2024 | 373 200 salariés fin 2024 (AEF, périmètre FBF) ; turnover 8,4 % | FBF ◈ / AEF ○ |
| 15/12/2025 | Société Générale signe accord « Emploi » avec 3 organisations syndicales | SG ◈ |
| 09/01/2026 | FO interpelle la FBF : « la technologie n'est ni une finalité ni un prétexte » | FO 🔥 |
| 22/01/2026 | SG dépose un projet de simplification ; −1 800 postes nets, sans plan de départs ; grève Crédit Agricole (fermetures d'agences) | SG ◈ / FO 🔥 |
| 02/02/2026 | Tribune FO : « PSE silencieux », citations Reinert/Herriberry | FO 🔥 |
| 28/07/2026 | FBF publie les chiffres 2025 (368 800, −0,7 %, 34 400 recrutements) | FBF ◈ |
| 2026 (enquête BMO) | 2 279 500 projets de recrutement, 43,8 % difficiles | France Travail ◈ |

## 3. DOMAINES (résultats par axe d'investigation)

### AXS-001 STATISTIQUE PUBLIQUE (saturée partiellement)

- Les MMO (source DSN) recensent les débuts et fins de contrats au niveau des établissements, par motif ; ils ne comportent pas de variable « poste libéré remplacé ou non ». (casd ○, snippet ; DARES inaccessible → GAP ACCESS). ATTEMPT: @WEB ×1, @FETCH ×2 (socket fermé) ; RESULT: FCT-011 ⁅.
- Le BMO 2026 est publié et inspecté : 2 279 500 projets, 43,8 % difficiles, 32,2 % saisonniers (FCT-009 ✧). Le chiffre « −6,5 % vs 2025 » (corpus) n'apparaît pas sur la page inspectée : GAP (QRY-id BMO-2).

### AXS-002 EMPLOI BANCAIRE (saturée)

- Effectifs 368 800 fin 2025 (−0,7 %) ; 34 400 recrutements (−10,2 %) ; turnover 7,7 % vs 20 % national ; tech 15,9 % (+3 pts) ; back office 2,6 % (−1,3 pt) ; alternants −8,6 % ; départs −11 % (FCT-001 à FCT-005, ✧).
- Contradiction non résolue : BFM avance « 350 700 salariés » (périmètre non précisé, peut-être AFB hors alternants) vs FBF 368 800. CONSIGNÉE, non moyennée (voir CONTRADICTION_LEDGER).

### AXS-003 RELATIONS SOCIALES (saturée)

- FO documente : annonces SG −1 800 et BNP −1 200, « PSE silencieux hors de tout cadre juridique et légal » (citations exactes), décisions unilatérales, opposition « secret industriel » aux questions syndicales sur l'IA, demande de suivi consolidé ETP/taux de remplacement (FCT-006, 007, 008, 013).
- Contradiction interne FO : « BNP Paribas a annoncé la suppression de 1 200 emplois, soit 20 % des effectifs » : 1 200 ≈ 0,7 % des ~183 000 salariés BNP. Erreur arithmétique ou approximation ; consignée, la proportion n'est pas reprise.

### AXS-004 CAUSALITÉ IA (partiellement saturée, gap central)

- Couche invoquée : FO rapporte que la cause annoncée inclut « services en ligne et adoption de l'IA qui remplacerait certaines tâches administratives » (FCT-008). SG mentionne « automatisation et usage de l'IA » parmi les leviers de la démarche participative (FCT-006).
- Aucune quantification de la part IA dans l'érosion des postes n'est disponible. Moteurs historiques documentés : digitalisation, fermetures d'agences (FO), repli de l'apprentissage (FBF, politique publique). GAP-001 : élasticité IA → non-remplacement non mesurée.

## 4. RÉSEAU D'ACTEURS (edges typés, sources citées)

| Acteur | Rôle | Action documentée | Source | Intent |
|---|---|---|---|---|
| FBF/AFB | Fédération ◈ | Publie « baisse maîtrisée » ; chiffres 2025 ; valorise emplois pérennes | FBF 28/07/2026 | CLAIMED (communication) |
| Société Générale | Employeur ◈ | Dépose projet −1 800 postes nets, sans plan de départs, départs naturels ; accord 15/12/2025 avec 3 OS | SG 22/01/2026 | CLAIMED (objectif affiché : efficacité) |
| BNP Paribas | Employeur ◈ | −1 200 emplois (selon FO) | FO 02/02/2026 | CLAIMED |
| FO Banques (FEC-FO) | Syndicat 🔥 | Qualifie « PSE silencieux hors cadre juridique » ; interpelle FBF et ministres ; demande suivi taux de remplacement | FO 02/02/2026 | CLAIMED (position syndicale) |
| DARES | Statisticien ◈ | Publie MMO (embauches/fins de contrat) | Page DARES (snippet) | N/A |
| France Travail | Opérateur ◈ | BMO 2026 : 2 279 500 projets | FT BMO | N/A |
| Salariés bancaires | Affectés | Angoisse, RPS (AVC, burnout, selon FO) | FO 02/02/2026 | UNKNOWN |

CONTROL_MAP : les décisions d'effectifs relèvent de la direction (consultation IRP obligatoire, accord GEPP signé) ; le suivi consolidé du taux de remplacement n'existe pas (demandé par FO) ; l'information quantitative disponible (FBF) est produite par l'employeur de branche lui-même.

## 5. CHAÎNES / PELOTE (mécanismes de l'objet)

CAUSAL_ROUTE=REQUIRED (mécanismes d'érosion). Recherche effectuée, edges typés, arrêt à la preuve.

- **CAU-001 Évitement du licenciement formel (SUPPORTED, source déclaratoire)** : SG annonce −1 800 nets « sans plan de départs », par départs naturels + mobilité interne (FCT-006) ; FO constate un processus « hors de tout cadre juridique et légal » de PSE (FCT-007). La substitution licenciement → non-remplacement est la stratégie annoncée par l'employeur et dénoncée par le syndicat. Type : ENABLER (choix organisationnel), pas une mesure de flux.
- **CAU-002 Digitalisation/IA réduisant des fonctions (PARTIAL)** : back office à 2,6 % des recrutements (−1,3 pt) ; FO : « services en ligne et adoption de l'IA qui remplacerait certaines tâches administratives » (FCT-004, FCT-008). La part respective digitalisation vs IA est indistinguable dans les sources. Type : ENABLER, partiellement sourcé.
- **CAU-003 Tension de recrutement persistante (CONTEXT)** : 43,8 % des projets BMO difficiles à pourvoir, dont santé 53,8 % (FCT-009) : le marché ne redistribue pas mécaniquement les volumes libérés par la banque. Type : CONTEXT.
- **GAP-001 CAUSAL** : aucune source ne quantifie la contribution de l'IA à la non-création de postes bancaires ; la chaîne asymétrie fiscale → non-remplacement (corpus lignée A) reste un mécanisme théorique non testé. CAUSALITY GAP explicite, non comblé par la narration.

SOURCE_PROVENANCE (généalogie du chiffre « −5k/−7k ») : quintessence legacy v36 « attrition-silencieuse » → hypothèse de turnover naturel 8-9 % → reconstruction 3 700-7 400 non-remplacements → NON REPRODUCTIBLE depuis les sources primaires inspectées (FBF ne publie pas de taux de non-remplacement). Classement : reconstruction, pas observation.

## 6. CARTE DIALECTIQUE

### Position dominante/institutionnelle (⟐)

« Baisse maîtrisée des effectifs » + « emplois pérennes, très qualifiés » + turnover record bas (7,7 %) comme preuve de stabilité. La banque affirme embaucher (34 400) et se transformer (tech 15,9 %). La réduction nette serait un ajustement « responsable » (FBF ◈).

### Position critique la plus forte (⟐̅)

FO : l'attrition est un « PSE silencieux » qui contourne le cadre juridique du licenciement, prive les IRP de leur rôle, et transforme l'emploi en « variable d'ajustement d'une trajectoire exclusivement financière » (4,1 Md€ de bénéfice SG invoqués). Le « secret industriel » oppose un mur aux questions sur l'IA. (FO 🔥, citations exactes.)

### Arbitrage par la preuve (evidence arbitration)

- La position FBF est exacte sur les chiffres publiés (vérifiés ◈) mais autoproduite : l'employeur de branche mesure sa propre érosion, sans indicateur de non-remplacement.
- La position FO est exacte sur les faits qu'elle documente (SG −1 800, non-remplacement assumé) et perd de la force sur le terrain quantitatif (pas de séries, une erreur arithmétique sur BNP).
- Le point de jonction solide des deux : la réduction se fait par non-remplacement (SG le déclare, FO le dénonce). Le désaccord porte sur l'interprétation (ajustement responsable vs contournement du droit), pas sur le mécanisme.

### Scénarios sous tension

1. **Attrition lente absorbée** : turnover 7,7 % + départs naturels ⇒ réduction progressive sans heurt social visible. C'est la trajectoire 2023-2025 (FBF).
2. **Attrition accélérée par IA** : si l'IA absorbe les fonctions administratives (back office, 2,6 %) plus vite que les départs, l'érosion se concentre sur les flux. Non mesurable avec les instruments actuels (GAP-001).
3. **Risque social déplacé** : RPS (alerte FO), fermetures d'agences rurales, alternants en repli (−8,6 %). Effets hors chiffres d'effectifs.

## 7. CARTE DES PREUVES

### LEAD_COVERAGE

| LED | SOURCE | Lead | Statut |
|---|---|---|---|
| LED-001 | Corpus legacy v36 | « −5 000 à −7 000 postes/an supprimés par l'IA (banques+assurances+télécoms) » | GAP : reconstruction non reproductible (FCT-010 ⁅) |
| LED-002 | Corpus legacy v36 | « Turnover bancaire 7,7 % vs 20 % national » | SATURATED : FCT-003 ✧ |
| LED-003 | Corpus legacy v36 | « FO : PSE silencieux hors cadre légal » | SATURATED : FCT-007 ✧ (citation exacte) |
| LED-004 | Corpus legacy v36 | « BMO −6,5 %, difficultés en chute 64 %→49 % » | GAP PARTIEL : 2 279 500 projets et 43,8 % vérifiés (FCT-009) ; la variation −6,5 % et la série 64→49 non retrouvées |
| LED-005 | Tour 3 (SNIPPET) | « 34 400 recrutements, tech 15,9 %, support 2,6 % » | SATURATED : FCT-002, FCT-004 ✧ |
| LED-006 | Tour 3 (SNIPPET) | « SG assume des réductions sans départs contraints » | SATURATED : FCT-006 ✦ |

### OBJECT_COVERAGE

| AXS | QUESTION | ATTEMPT_IDS | RESULT_IDS | STATUT |
|---|---|---|---|---|
| AXS-001 | Que mesure la statistique publique ? | QRY-1 (DARES MMO), FETCH ×2 | FCT-011 | GAP (ACCESS) |
| AXS-002 | Quelle érosion bancaire documentée ? | QRY-2 (FBF), FETCH FBF | FCT-001 à 005 | SATURATED |
| AXS-003 | Que documentent les relations sociales ? | QRY-3 (FO), FETCH FO, FETCH SG | FCT-006 à 008, 012, 013 | SATURATED |
| AXS-004 | L'IA est-elle un moteur mesuré ? | QRY-1 à 3 | CAU-001 à 003, GAP-001 | GAP (élasticité) |

### CLAIM_REGISTRY (extrait)

| CLM | Proposition | SUPPORT | COUNTER | GAP | STATUS |
|---|---|---|---|---|---|
| CLM-001 | L'attrition est le canal principal de l'érosion bancaire | FCT-001/002/006 (SG explicite) | FBF : « baisse maîtrisée » | Élasticité IA non mesurée | PROBABLE (mécanisme) |
| CLM-002 | L'IA « supprime » 5-7k postes/an en France | FCT-010 (reconstruction) | Aucune observation | Reconstruction non reproductible | UNSUPPORTED |
| CLM-003 | Le non-remplacement n'est mesuré par aucun instrument | FCT-011 (INFERENCE) + demande FO | Aucun | DARES inaccessible | PROBABLE |

### FACT_REGISTRY_V1

`FCT-001 | FACT | ✧ | https://www.fbf.fr/fr/communique_de_presse/solidite-des-marqueurs-de-lemploi-dans-la-banque-en-2025/ | FBF◈+AEF○ | 2026-07-28 | attrition-non-remplacements | Banques : 368 800 salariés fin 2025 (CDI+CDD+alternants), −0,7 % vs 2024 ; ~1,8 % de l'emploi salarié privé | mem:-`

`FCT-002 | FACT | ✧ | même URL FBF + BFM | FBF◈+BFM○ | 2026-07-28 | attrition-non-remplacements | 34 400 recrutements 2025 dont 16 300 AFB (12 300 CDI) ; −10,2 % vs 2024 (BFM), plus bas depuis 13 ans (BFM) | mem:-`

`FCT-003 | FACT | ✧ | même URL FBF | FBF◈ | 2026-07-28 | attrition-non-remplacements | Turnover bancaire 7,7 % en 2025 (8,4 % en 2024), vs moyenne nationale 20 % | mem:-`

`FCT-004 | FACT | ✧ | même URL FBF | FBF◈ | 2026-07-28 | attrition-non-remplacements | Fonctions technologiques = 15,9 % des recrutements (+3 pts vs 2024) ; back office 2,6 % (−1,3 pt) | mem:-`

`FCT-005 | FACT | ✧ | même URL FBF | FBF◈ | 2026-07-28 | attrition-non-remplacements | Alternants 19 800 → 18 100 (−8,6 %) ; départs −11 % en 2025 | mem:-`

`FCT-006 | FACT | ✦ | https://www.societegenerale.com/fr/actualites/communiques-de-presse/renforcement-de-lefficacite-par-la-simplification-de-lorganisation-et-du-developpement-des + https://www.force-ouvriere.fr/dans-les-banques-les-transformations-technologiques-ne-doivent | SG◈+FO🔥 | 2026-01-22 | attrition-non-remplacements | SG dépose le 22/01/2026 un projet de simplification : réduction nette de 1 800 postes d'ici fin 2027, sans plan de départs, via départs naturels et mobilité interne ; accord Emploi du 15/12/2025 avec 3 OS ; IA/automatisation citées parmi les leviers | mem:-`

`FCT-007 | FACT | ✧ | https://www.force-ouvriere.fr/dans-les-banques-les-transformations-technologiques-ne-doivent | FO🔥 | 2026-02-02 | attrition-non-remplacements | Citation exacte Reinert (FO Banques) : « Un PSE qui ne dit pas son nom car cela se déroule hors de tout cadre juridique et légal » | mem:-`

`FCT-008 | FACT | ✧ | même URL FO | FO🔥 | 2026-02-02 | attrition-non-remplacements | FO rapporte comme cause annoncée les services en ligne et l'IA « qui remplacerait certaines tâches administratives », sans concertation (« secret industriel » opposé) | mem:-`

`FCT-009 | FACT | ✧ | https://statistiques.francetravail.org/bmo/bmo?lg=0&pp=2026&ss=1 | FT◈ | 2026 | attrition-non-remplacements | BMO 2026 : 2 279 500 projets de recrutement ; 43,8 % difficiles ; 32,2 % saisonniers ; finances/assurance 38 600 projets (28,8 % difficiles) | mem:-`

`FCT-010 | INFERENCE | ⁅ | corpus legacy v36 (non reproductible) | corpus interne | 2026-08-25 | attrition-non-remplacements | « −5 000 à −7 000 postes/an par l'IA » : reconstruction sur hypothèse de turnover naturel ; non reproductible depuis sources primaires | mem:-`

`FCT-011 | INFERENCE | ⁅ | https://dares.travail-emploi.gouv.fr/donnees/les-mouvements-de-main-doeuvre (inaccessible : socket fermé) ; https://www.casd.eu/source/mouvements-de-main-doeuvre/ (snippet) | DARES◈/casd○ | 2026 | attrition-non-remplacements | Les MMO recensent embauches et fins de contrat (DSN, par motif) ; pas de variable « poste libéré remplacé ». Aucun instrument public ne mesure le taux de remplacement | mem:-`

`FCT-012 | CLAIMED | ⁅ | FO 🔥 | FO | 2026-02-02 | attrition-non-remplacements | FO cite 4,1 Md€ de bénéfice SG et une alerte RPS (AVC, burnout) ; source primaire SG non inspectée | mem:-`

`FCT-013 | EVIDENCE | ⁅ | FO 🔥 | FO | 2026-02-02 | attrition-non-remplacements | FO annonce −1 200 emplois BNP Paribas ; la proportion « 20 % des effectifs » qu'il avance est arithmétiquement incohérente (≈0,7 % des ~183 000 salariés) | mem:-`

Aucun ✦/✧ n'a fait l'objet de FACT_WRITEBACK (MNEMO paramétré indisponible) ; mem:- conservé. WRITEBACK_ROW=0.

### TRACE_MATRIX

| FCT | QRY/SRC | REFUTATION_SEARCHED | Résultat |
|---|---|---|---|
| FCT-001 | QRY-2 FBF | QRY-4 « effectifs banque 2025 baisse 0,7 % » | NONE (AEF, Lesechos, BFM concordants ; BFM 350 700 = périmètre non précisé → contradiction consignée, pas ✦) |
| FCT-002 | QRY-2 FBF | QRY-4 | NONE |
| FCT-003 | QRY-2 FBF | QRY-4 | NONE |
| FCT-004 | QRY-2 FBF | QRY-4 | NONE |
| FCT-005 | QRY-2 FBF | QRY-4 | NONE |
| FCT-006 | QRY-3 FO + FETCH SG | QRY-5 « Société Générale 1 800 postes contredit correction » | NONE (Le Monde, Le Parisien, L'Agefi, investir.lesechos concordants) → ✦ |
| FCT-007 | QRY-3 FO | QRY-6 « PSE silencieux banques réfutation » | NONE (convergence FO/fosg.net/fo-computacenter) → ✧ |
| FCT-008 | QRY-3 FO | QRY-6 | NONE → ✧ |
| FCT-009 | QRY-7 BMO | QRY-8 « BMO 2026 nombre projets révision » | NONE (page officielle inspectée) → ✧ |
| FCT-010 | corpus legacy | QRY-9 « banques non-remplacement 5000 7000 postes étude » | Aucune source primaire → ⁅ |
| FCT-011 | QRY-1 DARES | QRY-10 « taux de remplacement postes statistique France » | Aucun instrument trouvé → ⁅ (ACCESS) |

### CONTRADICTION_LEDGER

1. **FBF 368 800 vs BFM 350 700** (fin 2025) : périmètres vraisemblablement différents (BFM : champ AFB ou hors alternants), non documentés par BFM. Non résolue, non moyennée. Impact : le chiffre FBF est retenu avec attribution explicite.
2. **FO interne : « BNP 1 200 emplois soit 20 % des effectifs »** : erreur arithmétique ou proportion fausse. La proportion est écartée ; le volume (−1 200) reste une déclaration syndicale ⁅.
3. **FBF « emplois pérennes » vs BFM « plus bas depuis 13 ans »** : pas une contradiction de fait mais de cadrage (Λ) ; les deux sont vrais simultanément (CDI majoritaires + volume de recrutements historiquement bas).
4. **Corpus « difficultés de recrutement 64 %→49 % » vs BMO 43,8 %** : séries probablement différentes (part des établissements vs part des projets) ; la série 64→49 n'a pas été retrouvée. Non résolue.

### EDI (diversité épistémique, jamais vérité)

Familles présentes : A ⟐ (FBF, SG, France Travail, DARES tenté) ; C/🔥 ⟐̅ (FO Banques). Familles absentes : B (concurrents/contre-pouvoir indépendant), D (audit/review indépendant du secteur bancaire sur l'emploi), E (académique : pas d'étude universitaire citée sur le non-remplacement bancaire 2025-2026). EDI_GAP : déficit B/D/E documenté ; aucune conclusion ne repose sur une seule famille de provenance pour les faits centraux (FBF ◈ recoupé AEF○ ; SG ◈ recoupé FO🔥).

### BIAS_TEST (sources effectivement collectées)

- FBF (A, ⟐) : productrice et juge de ses chiffres d'emploi ; directe, méthode publiée partiellement, intérêt porteur (valorisation du secteur). Vérifiée sur la cohérence interne ; pas de séries indépendantes de contrôle.
- SG (A) : annonce officielle ; intérêt à présenter la réduction comme « simplification responsable » ; faits chiffrés recoupés par la presse et FO.
- FO (C/🔥) : contre-pouvoir, citations directes nommées (Reinert, Herriberry) ; intérêt militant ; une erreur arithmétique détectée (BNP) → crédibilité pondérée au niveau du fait, pas du jugement.
- France Travail/BMO (A) : statistique publique, méthode standard ; page inspectée.
- BFM, AEF, Lesechos (journalisme) : reprise de la source FBF (dépendance ascendante), utilisés en corroboration de surface uniquement.

## 8. PÉRIMÈTRE & LIMITES

**Inclusions** : banques (FBF), décisions d'effectifs SG, position FO, statistique publique (BMO, MMO), période 2023-2026, géographie France.
**Exclusions (explicites)** : assurances et télécoms (sources primaires des chiffres legacy non accessibles dans les bornes de cette exécution) ; quantification macro de l'effet IA sur l'emploi total (autre chantier, INV-P0-08) ; fiscalité/assiette (INV-P0-04).
**Limites d'accès** : DARES socket fermé (×2 session, ×2 antérieur) ; vie-publique.fr sans texte extractible ; DREES fiche CPS non inspectée (PDF) ; MNEMO paramétré indisponible (pas de write-back, pas de vérification mémoire).
**Limites de méthode** : périmètre BFM inconnu (contradiction non résolue) ; le chiffre « −5k/−7k » est classé reconstruction ; les déclarations FO sur RPS et bénéfice SG sont attribuées, non vérifiées primairement ; aucune étude indépendante du secteur n'a été trouvée dans les bornes.

## SOURCES

1. FBF, « Solidité des marqueurs de l'emploi dans la banque en 2025 », 28/07/2026 (INSPECTÉ) : https://www.fbf.fr/fr/communique_de_presse/solidite-des-marqueurs-de-lemploi-dans-la-banque-en-2025/
2. Société Générale, communiqué 22/01/2026 (INSPECTÉ) : https://www.societegenerale.com/fr/actualites/communiques-de-presse/renforcement-de-lefficacite-par-la-simplification-de-lorganisation-et-du-developpement-des
3. FO Banques, « Dans les banques, les transformations technologiques ne doivent pas être une machine à supprimer les postes », 02/02/2026 (INSPECTÉ) : https://www.force-ouvriere.fr/dans-les-banques-les-transformations-technologiques-ne-doivent
4. France Travail, BMO 2026 (INSPECTÉ) : https://statistiques.francetravail.org/bmo/bmo?lg=0&pp=2026&ss=1
5. DARES, « Les mouvements de main-d'œuvre » (INACCESSIBLE, socket fermé) : https://dares.travail-emploi.gouv.fr/donnees/les-mouvements-de-main-doeuvre
6. CASD, « MMO : Mouvements de Main d'Œuvre » (snippet) : https://www.casd.eu/source/mouvements-de-main-doeuvre/
7. AEF info (snippet) : https://www.aefinfo.fr/depeche/754874-...
8. BFM Business (snippet) : https://www.bfmtv.com/economie/entreprises/assurance-banque/...
9. AEF info, SG −1 800 postes (snippet, answer box) : https://www.aefinfo.fr/depeche/744628-...
10. Le Monde (snippet) : https://www.lemonde.fr/economie/article/2026/01/22/societe-generale-prevoit-de-supprimer-1-800-postes-en-france_6663624_3234.html

## REQUEST_LOG (appels matériels réels)

| # | Type | Cible | Résultat |
|---|---|---|---|
| 1 | @WEB | FBF emploi banque 2025 | 10 résultats, communiqué FBF en position 1 |
| 2 | @FETCH | fbf.fr communiqué | 200, texte complet (INSPECTÉ) |
| 3 | @WEB | FO « PSE silencieux » | feed force-ouvriere.fr, snippet partiel |
| 4 | @WEB | FO SG BNP PSE | article FO 02/02/2026 identifié |
| 5 | @FETCH | force-ouvriere.fr article | 200, texte complet (INSPECTÉ) |
| 6 | @FETCH | francetravail.org BMO | 200, tableau complet (INSPECTÉ) |
| 7 | @WEB | DARES MMO méthode | page DARES + casd identifiés |
| 8 | @FETCH | dares.travail-emploi.gouv.fr/donnees | SOCKET FERMÉ |
| 9 | @FETCH | dares.travail-emploi.gouv.fr/enquete-source | SOCKET FERMÉ |
| 10 | @WEB | SG 22/01/2026 1 800 postes | answer box AEF + 10 résultats concordants |
| 11 | @FETCH | societegenerale.com communiqué | 200, texte complet (INSPECTÉ) |
| 12 | @WEB | réfutation SG (contredit/correction) | NONE : concordance Le Monde/Le Parisien/L'Agefi |
| 13 | @WEB | réfutation PSE silencieux | NONE : convergence FO/fosg.net |
| 14 | @WEB | réfutation BMO 2026 | NONE |
| 15 | @WEB | réfutation −5k/−7k postes | aucune source primaire |
| 16 | @WEB | taux de remplacement postes statistique | aucun instrument trouvé |
| 17 | @MNEMO_Q | recherche mémoire attrition | ÉCHEC paramètres (×3 session) → MNEMO_UNAVAILABLE |

**Gate 19a (exécuté 13h57 UTC) :** `verify.py gate` → verdict **BLOCKED** (branche protégée main). Checks : naming PASS (39 fichiers, 0 violation), no-em-dash PASS (67 fichiers, 0 occurrence), tests extractors PASS (111 passed, 1 skipped). state_id `76faf0b6effbed9fcda73d898b7cf5713fce0b2e`. **Aucune certification de livraison n'est revendiquée sur main** ; pour un PASS certifié, le chantier doit être déplacé en worktree (`tools/verify/worktree-new.sh <chantier>`) puis re-verify en UPDATE.

---
*Fin du dossier. Toute reprise postérieure doit citer ce fichier et le REGISTRE de session du 26/08.*
