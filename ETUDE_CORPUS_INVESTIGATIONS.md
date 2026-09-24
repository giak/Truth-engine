# Étude du corpus d'investigations — État des lieux

> Document de travail. Pour orienter la restructuration de l'article à partir du corpus réel, et non d'une théorie préalable.
> Date : 2026-09-19
> Base : `10_A7_FULL_CORPUS/A7_EXTERNAL_RECONSTRUCTION_BUNDLE_V3/02_MASTER_EVIDENCE_BASE/03_INVESTIGATIONS/`

---

## 1. Ce que contient réellement le corpus

### 1.1 Statistiques (INVESTIGATION_ARTIFACT_MATRIX.csv)

| Dimension | Détail |
|---|---|
| Total | 147 investigations |
| Statut | 121 CLOSED, 12 BACKLOG, 7 CONDITIONAL, 6 MERGED, 1 DEFERRED |
| Type | 99 PRIMARY, 13 SYNTHESIS, 13 CASE, 7 CONDITIONAL_CASE, 6 CONTROL_SPEC, 2 STRUCTURAL, 1 DEFER_CONTEXT |
| Workstreams | W0(13) à W10(19), répartition inégale |
| CANONICAL_6_COMPLETE | 13 (investigations avec les 6 artefacts canoniques complets) |
| Handoffs disponibles | 97 fichiers DIRECT_RECOVERED_HANDOFFS + 2 recovery |
| Syntheses disponibles | 13 fichiers DIRECT_SYNTHESIS |
| Investigations avec texte complet | ~55 dans DIRECT_RECOVERED_INVESTIGATIONS (34 INV-xxx + 9 timestampées + SOURCE_CATALOG) |

### 1.2 Clarification : corpus vs article

Le corpus (`03_INVESTIGATIONS/`) est un **programme d'investigation forensique** — 147 investigations fermées, méthodologie intégrée. L'article (`01_TARGET/ARTICLE_MASTERWORK_SOUVERAINETE_2026.md`, 306 lignes, 86 références) en est un **produit dérivé** : il sélectionne, interprète et arrange certaines conclusions sous la forme "4 verrous de la souveraineté française". Ce n'est PAS le corpus lui-même.

L'utilisateur a demandé à oublier l'article. Le corpus reste le matériau brut.

## 1.3 Mission du corpus (INVESTIGATION_ORCHESTRATOR.md §1)

> Construire une cartographie falsifiable des mécanismes par lesquels des acteurs publics ou privés, domestiques ou étrangers modifient ou cherchent à modifier préférences, perceptions, comportements, élections, institutions ou politiques publiques d'une démocratie.

Qualifier à partir des **mécanismes observables et des preuves**, pas du camp, du statut ou du vocabulaire appliqué à l'acteur.

### 1.3 Verdict systémique terminal (PROGRAM_COMPLETION_2026-09-11.md, INV-133 SYNTHESIS)

> **Best-supported systemic model: polycentric, cumulative and emergent power under structural asymmetries**, combining networked access, bounded coordination, sectoral capture and real counter-powers. A unitary cross-sector command architecture is **NOT_ESTABLISHED**.

### 1.4 État actuel

- Aucun item ACTIF (READY=0, TE_ACTIVE=0, SYNTHESIS_SELECTED=0)
- INV-133 est SYNTHESIS TERMINAL — le programme est fermé dans son périmètre actuel
- Les 12 BACKLOG sont des items HOLD/REFAME (pas des dépendances bloquantes)

---

## 2. Cartographie thématique des investigations

### 2.1 Ingérences étrangères historiques

| INV | Sujet | Établi | Non établi |
|---|---|---|---|
| INV-010 | CIA et élections étrangères (Italie 1948, Chili 1964/70) | Intervention existe, soutien clandestin massif | Changement de vainqueur causé |
| INV-011 | CIA/médias (Church Committee, MOCKINGBIRD, Family Jewels) | Surveillance et manipulation médiatique documentées | Étendue systématique |
| INV-012 | COINTELPRO — FBI disruption politique intérieure | Programmes HQ-approuvés, exécutés | Generalisation, effet électoral |
| INV-013 | Active measures russes / IRA / interférence électorale France-EU | Opérations multicanal, infrastructure | Persuasion, effet électoral |
| INV-018 | Opération russe multicanal 2016 | Attribution principale forte | Coordination/conspiration générale |
| INV-022 | Russie influence France (VIGINUM, Portal Kombat, Storm-1516) | Opérations/infrastructure établies | Persuasion, effet électoral |
| INV-023 | Financement russe de partis européens | Flux documentés | Commandement |
| INV-014 | Printemps arabes — assistance extérieure vs causes endogènes | Infrastructure assistance, transfert CANVAS | Tasking, déclenchement, chute régime |
| INV-016 | Printemps arabes — assistance, plateformes, causalité | Capacité, transfert tactique, participation | Causalité changement régime |

### 2.2 Influence étrangère contemporaine (États, privés, diasporiques)

| INV | Sujet | Établi | Non établi |
|---|---|---|---|
| INV-025 | Chine / United Front — influence France/EU | Mécanismes multiples documentés | Architecture unifiée |
| INV-026 | Israël influence France/UE | Ressources, accès | Coordinated tasking généralisé |
| INV-027 | ELNET France — lobbying, accès, positions | Chaîne ressources→accès→position | Décision causée |
| INV-028 | AIPAC — mécanismes électoraux et lobbying | Électoral et lobbying réels | Plafond causal |
| INV-033 | Émirats — influence clandestine/réputationlle Europe | Alp Services, chaine client→paiement→prestataire | Fiabilité fiches, effets downstream |
| INV-038 | Maroc/Algérie — influence politique, diplomatique, diasporique France | (SYNTHESIS) | — |
| INV-071 | VIGINUM — doctrine, critères, attribution | Doctrine, capacités, chaîne publique | Attribution unitaire |
| INV-127 | Soft power académique/culturel | (PRIMARY, G1-G4 passed) | — |
| INV-128 | Influence-for-hire | Mécanismes documentés | — |
| INV-138 | France comme puissance d'influence à l'étranger | — | — |
| INV-137 | Renseignement exécutif ↔ médias | — | — |
| INV-036 | ? | — | — |
| INV-037 | ? | — | — |

### 2.3 Mécanismes de capture/influence intérieure

| INV | Sujet | Établi | Non établi |
|---|---|---|---|
| INV-056 | Astroturfing/front groups | Capacité réelle, cas-spécifiquement prouvable quand tasking prouvé | Chaîne générale |
| INV-059 | Think tank narrative laundering (R3P1, CANONICAL_6_COMPLETE) | Chaîne partielle ressources→capacité→accès | Tasking contenu, persuasion |
| INV-067 | Groupes d'experts publics — composition, accès | Canal formel d'accès, influence normative traçable | Causalité |
| INV-062 | McKinsey/conseils dans État français | Interventions matérielles, confusion conseil≠délégation | Délégation de souveraineté |
| INV-069 | Communication gouvernementale française | Infrastructure centralisée établie | Objectifs spécifiques |
| INV-081 | Concentration économique médias française | Propriété, ressources, capacités mesurables | Usage éditorial |
| INV-085 | Sélection éditoriale (gate éditorial) | Sélection sujets/claims explicite | Origine causale des différences |
| INV-042 | Lobbying UE — accès, portes tournantes | Canal institutionnalisé, règles | Visibilité réelle, effet |
| INV-066 | Financement recherche, agenda scientifique (Horizon, pharma) | Financements, partenariats | Agenda capturé |
| INV-053 | Financement ONG migrations/intégration | Capacité, plaidoyer, accès | Effet politique direct |
| INV-054 | ONG droits humains + contentieux stratégique | Influence par le droit, financement | Causalité politique |
| INV-049 | Open Society Foundations — France/UE | (PRIMARY) | — |
| INV-119 | Élites reproduction circuits | (PRIMARY, R3P1) | — |

### 2.4 Économie politique de l'influence

| INV | Sujet | Établi | Non établi |
|---|---|---|---|
| INV-052 | Philanthrocapitalisme (SYNTHESIS) | Financement → capacité, agenda-setting | Commandement → captation décision |
| INV-045 | Fact-checking certification/accès (SYNTHESIS) | Infrastructure distribuée de qualification | Standard unifié |
| INV-144 | Économie politique contre-ingérence (SYNTHESIS) | Réponse à menaces documentées + incitations bureaucratiques | Inflation volontaire coordonnée |
| INV-040 | Déficit démocratique UE (SYNTHESIS) | Architecture institutionnelle distribuée | Déficit mesurable généralisé |
| INV-039 | Qui exerce réellement le pouvoir dans l'UE ? | (PRIMARY) | — |
| INV-129 | Lawfare/coercition juridique (SYNTHESIS) | Droit utilisé comme canal d'influence | Architecture générale de lawfare |
| INV-124 | Debanking/sanctions/accès financier comme coercition | Infrastructure privée/publique de coercition | — |
| INV-047 | Sanctions UE comme instrument d'influence/coercition | (PRIMARY) | — |
| INV-136 | Corruption étrangère EU institutions | — | — |

### 2.5 Canaux numériques et informationnels

| INV | Sujet | Établi | Non établi |
|---|---|---|---|
| INV-017 | Cambridge Analytica — data→profilage→ciblage (CANONICAL_6_COMPLETE) | Pipeline données, capacité analytics | Persuasion, effet électoral |
| INV-096 | Microtargeting (CANONICAL_6_COMPLETE) | Ciblage data-driven réel | Persuasion, effet électoral |
| INV-090 | Plateformes friction visibilité (CANONICAL_6_COMPLETE) | Restriction/démonétisation mesurable | Effet systémique |
| INV-043 | DSA — gouvernance informationnelle (PRIMARY) | Architecture multiniveau gouvernance | Mécanisme unique de retrait |
| INV-097 | Bot amplification élections | — | — |
| INV-087 | Sondages→comportement électoral | Case-specifically établi | Effet général |
| INV-091 | ? | — | — |
| INV-092 | ? | — | — |
| INV-078 | Fonds Marianne | — | — |

### 2.6 Élections, fraude, coercition

| INV | Sujet | Établi | Non établi |
|---|---|---|---|
| INV-098 | Vote buying/clientélisme | — | — |
| INV-099 | Electoral fraud claims | — | — |
| INV-100 | Annulation/neutralisation judiciaire d'élection (Roumanie + comparaisons) | — | — |
| INV-143 | Timing institutionnel d'élection | — | — |
| INV-089 | ? (CASE) | — | — |
| INV-093 | Financement campagnes françaises (argent, prêts, partis) | Système multicanal documenté | Commandement, persuasion |
| INV-094 | Financement étranger partis/candidats UE | Flux étrangers documentés | Tasking, effet électoral |
| INV-095 | Sélection candidats avant élection (SYNTHESIS) | Filtres structurels inégaux | Architecture coordonnée de présélection |
| INV-102 | Consentement sans choix réel (SYNTHESIS) | Mécanismes de contrainte ponctuelle | Consentement généralement sans choix |

### 2.7 Preuve, attribution, ingérence

| INV | Sujet | Établi | Non établi |
|---|---|---|---|
| INV-134 | Attribution d'ingérence — où s'arrête la preuve ? | — | — |
| INV-135 | Hack-and-leak, kompromat, divulgations synchronisées | — | — |
| INV-141 | Spyware mercenaire → compromission → manipulation (CANONICAL_6_COMPLETE) | Compromission documentée (Pologne/Brejza) | Accès→manipulation→effet |
| INV-142 | Sponsorship caché/laundering source (CANONICAL_6_COMPLETE) | Influence source-laundérée vérifiée | — |
| INV-145 | FARA / France / UE / agent étranger | Conception juridique différente | Application sélective |
| INV-146 | Asymétrie alliés/adversaires (SYNTHESIS) | Asymétrie de DESIGN juridique | Application sélective, standard différent |
| INV-133 | Synthèse systémique finale (SYNTHESIS TERMINAL) | Modèle polycentrique, cumulatif, émergent | Architecture de commandement unifiée |
| INV-015 | ? (CASE) | — | — |
| INV-018 | Opération russe 2016 | Attribution forte | Conspiration générale |

### 2.8 SYNTHÈSES (13)

| INV | Titre |
|---|---|
| INV-038 | Maroc/Algérie influence en France |
| INV-040 | Déficit démocratique européen |
| INV-052 | Philanthrocapitalisme |
| INV-068 | Narrative laundering (intérêt→think tank→expert→média→décideur→consensus) |
| INV-082 | Concentration économique vs concentration éditoriale |
| INV-088 | Fact-checking comme infrastructure de qualification |
| INV-095 | Sélection des candidats avant l'élection |
| INV-102 | Consentement sans choix réel |
| INV-104 | Mensonge institutionnel → défiance → vulnérabilité (boucle causale) |
| INV-129 | Lawfare et coercition juridique |
| INV-133 | Synthèse systémique finale (TERMINAL) |
| INV-144 | Économie politique de la lutte contre l'ingérence |
| INV-146 | Asymétrie alliés/adversaires |

### 2.9 BACKLOG (12 HOLD/REFAME items)

INV-009 (généalogie historique), INV-024 (China bundle multi-mécanisme), INV-031 (UK bundle hétérogène), INV-032 (Qatar bundle multi-vehicle), INV-034 (Saudi bundle multi-vehicle), INV-058 (accountability), INV-105 (autorité/conformité psychologie), INV-106 (contrat production menace), INV-107 (moral panic), INV-108 (motivated reasoning), INV-109 (illusory-truth), INV-123 (Big Tech résiduel).

**Aucun n'est une dépendance de INV-133** — ce sont des items HOLD au sens de l'orchestrateur.

---

## 3. Méthodologie embarquée dans le corpus

Le corpus n'est pas une collection de dossiers : c'est un **programme d'investigation forensique** avec sa propre doctrine. Les principes suivants sont structurels :

### 3.1 Principes inviolables (INVESTIGATION_ORCHESTRATOR.md §2)

1. `MECHANISM_FIRST > ACTOR_FIRST` — le mécanisme avant l'acteur
2. Toute accusation ET tout démenti sont des claims à prouver
3. Source officielle ≠ vérité interprétative automatique
4. `funding ≠ command`; `network ≠ coordination`; `proximity ≠ tasking`; `correlation ≠ causality`
5. `absence_of_evidence ≠ evidence_of_guilt`; `not_found ≠ does_not_exist`
6. Séparer : fait, document, témoignage, accusation, inférence, hypothèse, intention, causalité, effet
7. Tester activement explications rivales et cas négatifs
8. Répétitions dérivées d'une même source ≠ corroborations indépendantes
9. Même standard pour État, médias, ONG, entreprises, plateformes, services, partis, alliés ET adversaires
10. `operation ≠ exposure ≠ persuasion ≠ behavior ≠ democratic/electoral_effect`
11. `capacity ≠ use`; `dependency ≠ coercion`; `access ≠ adoption`; `legal_design ≠ enforcement`

### 3.2 Niveaux de preuve I0-I7 (utilisés dans les handoffs)

- I0 identity/relation
- I1 resources/capability/access
- I2 documented action
- I3 coordination/tasking/control
- I4 exposure/reach
- I5 reception/persuasion
- I6 behavior/institutional change
- I7 counterfactual outcome

### 3.3 La règle des 4 distinctions fondamentales

Chaque investigation distingue explicitement (exemple INV-010) :
- **INTERVENTION_EXISTED** ≠ **INTERVENTION_CHANGED_MARGIN** ≠ **INTERVENTION_CHANGED_WINNER**
- **Capability ≠ Execution ≠ Exposure ≠ Persuasion ≠ Vote ≠ Outcome**
- **Operation ≠ Exposure ≠ Persuasion ≠ Behavior ≠ Effect**

### 3.4 RENARD (reopen decision)

Chaque investigation fermée porte un verdict RENARD = NO/YES :
- RENARD = NO : les deltas résiduels ne sont pas de bons candidats pour une recherche immédiate
- RENARD = YES : réouverture justifiée par nouvelle preuve matérielle

---

## 4. Ce que le corpus NE contient PAS

1. **Pas de théorie générale unifiée** — le modèle terminal est polycentrique et cumulatif, pas une architecture de commandement
2. **Pas de "les X ont gagné les élections"** — aucune investigation ne ferme l'arête `intervention → changement de vainqueur`
3. **Pas de jugement moral sur les acteurs** — qualification mécaniste, pas moralisatrice
4. **Pas de présupposés idéologiques** — le corpus est construit pour tester, pas pour confirmer
5. **Pas de synthèse narrative unifiée** — les 13 synthèses existent, mais la systémique finale (INV-133) est la seule à prétendre à une vue d'ensemble
6. **Pas de données pour ~100 investigations** (HANDOFF_OR_DERIVED_ONLY, NO_ARTIFACT_RECOVERED) — 121 CLOSED ne signifie pas 121 complètes

---

## 5. Diagnostic : ce qui est utilisable pour l'article

### 5.1 Matériaux directement utilisables

| Matériau | Contenu | Utilité |
|---|---|---|
| 13 SYNTHÈSES | Résumés analytiques fermés | Corps analytique principal |
| ~97 handoffs | Conclusions certifiées, deltas, I0-I7, gaps | Cas d'illustration |
| 53 investigation files dans DIRECT_RECOVERED_INVESTIGATIONS (34 INV-xxx + 9 timestampées + SOURCE_CATALOG) | Rapports forensiques partiels à complets | Récits approfondis |
| INVESTIGATION_ORCHESTRATOR.md | Doctrine et méthodologie | Préambule méthodologique |
| PROGRAM_COMPLETION + DASHBOARD | État du programme | Cadre |
| SOURCE_CATALOG | 147 entrées de sources | Bibliographie |
| INVESTIGATION_ARTIFACT_MATRIX | Métadonnées de toutes les investigations | Table des matières |

**Note de précision** : INV-010 a été clôturé en mode **pilot review** (`DELIVERY_PASS_R2A2`, non `R3P1`). Son RENARD final est `CLOSED_NO_FURTHER_MATERIAL_DELTA` mais avec un périmètre ciblé : seul le Chile 1964 I6-I7 a fait l'objet d'un RENARD, et la conclusion a été **narbonnée** (passage de "soutenu" à "plausible mais pas isolé"). Ce n'est pas un cas pleinement certifié R3P1.

INV-011 est un cas **heterogeneous** : le corpus ferme un système CIA-médias Cold War hétérogène, **pas** un programme ombrelle unique. Le MOCKINGBIRD est un cas spécifique (fils téléphoniques Allen/Scott), pas la preuve d'un contrôle éditorial général.

INV-010 et INV-011 sont les deux investigations les plus didactiques pour illustrer la discipline forensique du corpus :
- **INV-010** : distinction explicite entre existence d'intervention et effet causal, avec 17 sections, 3 clusters, dialectique complète, cartes de preuves (mais clôturé en mode **pilot review** `DELIVERY_PASS_R2A2`, non `R3P1`)
- **INV-011** : séparation `surveillance ≠ disruption`, `memo ≠ execution`, `operation ≠ harm`, `operation ≠ editorial command`

### 5.2 Ce qui doit être rejeté

- **L'article V4.4 "4 verrous"** (ARTICLE_MASTERWORK_SOUVERAINETE_2026.md) : se contredit lui-même (ligne 148 : "Il n'établit pas que ces quatre verrous forment une architecture unique" alors que le titre et la prose promettent une architecture unifiée), mélange des verrous non homogènes, promet un garde-fou que le corpus ne fournit pas systématiquement. L'utilisateur a explicitement demandé à l'oublier.
- **Toute structure narrative qui présuppose** une thèse unifiée non établie par le corpus
- **La trilogie précédemment proposée** (qui nécessitait une synthèse que le corpus ne supporte pas)

---

## 6. Structures d'article possibles (fidèles au corpus)

### Option A : Investigation en profondeur (recommandé)

Un seul cas d'investigation forensique suivi dans ses ramifications, qui illustre les principes du corpus sans prétendre à une synthèse que les données ne supportent pas.

**Sujet candidat : INV-010 (CIA/élections étrangères)** — c'est l'investigation la plus complète (327 lignes, 17 sections), la plus didactique pour illustrer la discipline forensic, mais clôturée en mode **pilot review** (`DELIVERY_PASS_R2A2`, non `R3P1`) :
- 3 clusters, 17 sections, dialectique complète
- Distinction explicite entre existence d'intervention et effet causal
- Règle `covert_operation ≠ electoral_determinism`
- **Limite à signaler** : RENARD final = `CLOSED_NO_FURTHER_MATERIAL_DELTA`, mais le Chile 1964 I6/I7 a été **narbonné** (passage de "soutenu" à "plausible mais pas isolé"). Ce n'est pas un cas pleinement certifié R3P1.

**Structure :**
1. Méthode forensic employée (1 paragraphe)
2. Question posée (2 sous-questions séparées)
3. Réponse sur l'existence de l'intervention → VERIFIED
4. Réponse sur l'effet → OPEN/NOT ESTABLISHED (avec les 3 cas)
5. Leçons méthodologiques (les 4 distinctions + RENARD)
6. Ce que cela dit et ne dit pas du corpus global

### Option B : Cartographie thématique guidée par les 13 synthèses

Utiliser les 13 synthèses comme chapitres, encadrées par la synthèse systémique (INV-133) en préambule et conclusion.

**Structure :**
1. Préambule : méthode et verdict terminal (INV-133)
2. Chapitre : Les ingérences étrangères (7-10 investigations clés)
3. Chapitre : La capture intérieure (think tanks, experts, conseils, ONG)
4. Chapitre : Les canaux numériques (plateformes, microtargeting, DSA)
5. Chapitre : L'économie de l'influence (financements, lawfare, sanctions)
6. Chapitre : Preuve et attribution (difficultés structurelles)
7. Conclusion : modèle polycentrique, ce qui reste ouvert

⚠️ Risque : nécessiterait des regroupements thématiques que le corpus ne fait pas explicitement. Les synthèses ne partagent pas de fil conducteur commun autre que leur domaine.

### Option C : Atlas des mécanismes

Une structure encyclopédique : chaque mécanisme observable (comme défini par l'orchestrateur) est un article court.

**Structure :**
1. Introduction : qu'est-ce qu'un mécanisme d'influence falsifiable
2. ~30-40 entrées courtes : chaque mécanisme est une fiche
   - Format : Acteur → Ressource → Action → Cible → Exposition → Effet → Gaps
3. Annexe : état du programme (147 investigations, 121 CLOSED)

⚠️ Risque : trop fragmenté pour un article, plus adapté à un outil de référence.

### Option D : Méthode et limites (le plus honnête)

Un article sur ce que l'investigation forensique de l'influence démocratique peut et ne peut pas faire, en s'appuyant sur les investigations les plus probantes comme exemples.

**Structure :**
1. La question et ses pièges (pourquoi c'est dur)
2. La méthode (principes 1-11 de l'orchestrateur)
3. Ce qu'on sait établir (3-4 cas types : INV-012 COINTELPRO, INV-017 Cambridge Analytica, INV-022 Russie/France, INV-033 Émirats)
4. Ce qu'on ne peut pas établir (causalité électorale, attribution, effet général)
5. Le verdict terminal (polycentrique, cumulatif, émergent)
6. Ce qui reste à faire (les 12 HOLD, les 26 GAPS)

---

## 7. Recommandation

**Option D + Option A hybride** :

- Préambule : la question et sa difficulté méthodologique (Option D §1-2)
- Corps : un cas d'étude approfondi (INV-012 ou INV-017 — tous deux DELIVERY_PASS_R3P1, INV-017 étant CANONICAL_6_COMPLETE) qui illustre la méthode en action (Option A)
- Contrepoint : 2-3 investigations secondaires qui montrent d'autres mécanismes
- Conclusion : ce que le corpus entier dit et ne dit pas (Option D §4-6)

**Pourquoi :** cette structure ne prétend pas à une synthèse que les données ne supportent pas, elle est fidèle à la discipline forensic du corpus, et elle permet de montrer *comment* on investiggue plutôt que *ce qu'on conclut*.

---

## 8. Prochaines étapes

1. Choisir une option (ou un hybride)
2. Identifier les 3-5 investigations à lire en profondeur
3. Lire les INVESTIGATION.md complets pour celles-ci
4. Rédiger un plan détaillé
5. Rédiger l'article
