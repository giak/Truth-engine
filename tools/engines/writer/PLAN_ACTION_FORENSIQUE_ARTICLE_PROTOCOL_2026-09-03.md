# ARTICLE PROTOCOL — Plan d’action forensique de remise à plat

**Date :** 2026-09-03  
**Statut :** plan d’exécution candidat après double-check  
**Principe :** KISS / DRY / YAGNI / réparation locale / zéro régression / vérité d’exécution avant statut

---

## 0. Objectif

Remettre d’aplomb la chaîne complète :

```text
VISION / PFD
    ↓
EPICs
    ↓
Stories
    ↓
ARTICLE_PROTOCOL.md
    ↓
Runtime réel
    ↓
Article
    ↓
Audit du produit
```

Le but n’est pas d’ajouter une nouvelle architecture.

Le but est de rendre cette chaîne :

- **identifiable** ;
- **traçable** ;
- **navigable par un LLM ou un humain** ;
- **auditable dans les deux sens** ;
- **exécutable** ;
- **testée sur un corpus réel** ;
- **incapable de déclarer PASS lorsque la finalité VISION/PFD est perdue**.

Invariant :

```text
LOCAL_TEST_PASS
!=
FOUNDATION_CONFORMANCE_PASS
!=
PRODUCT_PASS
```

---

# 1. Résultats du double-check à considérer comme état de départ

## 1.1 Les bundles actuels ont été revérifiés

Bundle protocole courant :

```text
ARTICLE_PROTOCOL_EPICS_V1_2026-09-02.zip
SHA-256:
b45e487fcc4751c1efda46b5f87cb1baf83bdb5cf25a1f641b5abe02bae06f4e
```

Bundle runtime déchèteries courant :

```text
ARTICLE_PROTOCOL_RUNTIME_DECHETTERIES.zip
SHA-256:
8c624368f4541e0107d8423f76ca2a876c49064e2ccaec25ae8c58bb8fb3505b
```

Le ZIP protocole contient actuellement 11 entrées utiles :

```text
README.md
ARTICLE_PROTOCOL.md
EPIC_A0_COUVERTURE_FONDATRICE.md
EPIC_A1_MATIERE_CONTEXTE.md
EPIC_A2_COMPREHENSION_ENQUETE.md
EPIC_A3_DECISION_EDITORIALE.md
EPIC_A4_CONSTRUCTION_ECRITURE.md
EPIC_A5_REVIEW_REPARATION.md
EPIC_A6_BACK_REINVESTIGATION.md
EPIC_A7_VALIDATION.md
```

**VISION et PFD ne sont pas présents dans le bundle protocole.**

Ce n’est pas forcément une erreur d’exécution en soi, mais c’est un défaut sérieux de **portabilité forensique et d’identité du référentiel**, puisque les EPICs déclarent dépendre de `VISION V4.4 + PFD V4.4` sans embarquer ou verrouiller précisément les fichiers auxquels ces noms renvoient.

---

## 1.2 Il existe une ambiguïté réelle sur PFD

Deux fichiers `PFD.md` ont été retrouvés dans la Library.

### PFD A

```text
Nom: PFD.md
file_id: file_0000000090e88210949bdacebc5b61e6
271 lignes
En-tête:
Statut : fondation candidate V4.4
```

Il définit principalement :

```text
F-01..F-12
NFR-01..NFR-06
AC-01..AC-08
```

### PFD B

```text
Nom: PFD.md
file_id: file_000000003954824696e1331026cdd610
686 lignes
En-tête:
Statut : exigences fondatrices
```

Il contient notamment :

```text
FR-01..FR-23
NFR supplémentaires
AC détaillés
```

avec des exigences telles que :

```text
FR-06 Investigation essence
FR-07 Discovery inventory
FR-11 Author decision
FR-12 Article mode
FR-15 Show the investigations
```

### Verdict

Il est **interdit de présumer** que PFD B est la PFD V4.4 autoritative.

Le fait que son contenu paraisse plus riche ou plus adapté au défaut observé ne lui donne pas automatiquement autorité.

Avant toute réparation fondée sur `FR-*`, il faut établir :

```text
IDENTITÉ
+
VERSION
+
FILIATION
+
SUPERSESSION
```

Sinon nous risquons de réparer le protocole contre une spécification qui n’est plus canonique.

---

## 1.3 VISION V4.4 fournit déjà plusieurs critères suffisants pour constater l’échec actuel

La VISION candidate V4.4 retrouvée affirme notamment :

```text
NO_EARLY_FLATTENING

CLAIM != DISCOVERY
CLAIM_SET != SUBJECT_UNDERSTANDING

l'article doit faire sentir le rendement de l'enquête

le lecteur doit comprendre réellement l'objet

le même article ne doit pas pouvoir être produit presque
à l'identique sans le travail profond de Truth Engine
```

Donc le défaut actuel de l’article déchèteries reste réel même sans utiliser le PFD détaillé non encore relié.

---

## 1.4 A0 a produit un PASS qui n’a pas suffi à protéger la finalité

A0 annonce notamment :

```text
F-01..F-12       = 12 / 12
NFR-01..NFR-06   = 6 / 6
AC-01..AC-08     = 8 / 8
Invariants VISION = 14 / 14

Aucune exigence fondatrice orpheline n'est visible.
```

Puis :

```text
A0 = READY
P0 = 0
P1 = 0
P2 = 2
```

Or le runtime réel a ensuite révélé un article :

- exact ;
- fortement tracé ;
- avec ses tests locaux verts ;
- mais insuffisant en profondeur d’objet et rendement d’enquête.

A0 a lui-même dû ajouter plus tard l’amendement :

```text
MATERIAL_OBJECT_UNDERSTANDING_SURVIVES_SELECTION_AND_PRODUCTION
```

### Verdict

A0 n’est pas inutile.

Mais son ancien crosswalk était **trop grossier** :

```text
FOUNDATION
→ EPIC
```

Il faut le rendre capable de contrôler :

```text
FOUNDATION NODE
→ EPIC
→ STORY
→ TEST
→ RUNTIME EVIDENCE
```

---

## 1.5 Le runtime courant contient un NEXT désormais non fiable

`STATE.json` indique encore :

```text
next =
Replay A4-S03 on ...A4_S02_REPLAY_DRAFT_V1.md;
then replay AC-07.
```

Le même état considère :

```text
A4-S02 replay = PASS
A4-S03 = autorisé
```

Or notre double-check de conformité a rouvert des défauts **en amont** de ce replay.

### Décision

Le `NEXT` courant doit être considéré :

```text
STALE / BLOCKED_BY_FOUNDATION_CONFORMANCE_REVIEW
```

A4-S03 ne doit pas être poursuivi avant réparation du référentiel et audit de dépendance.

---

# 2. Ce qui est prouvé, probable et non encore prouvé

## PROUVÉ

```text
P-01
Le bundle protocole ne contient pas VISION/PFD.

P-02
Au moins deux PFD.md sémantiquement différents existent.

P-03
Une seule des deux PFD retrouvées se déclare explicitement V4.4.

P-04
A0 a déclaré une couverture complète qui n'a pas empêché
un échec produit réel ensuite reconnu.

P-05
STATE.json autorise encore A4-S03 alors que la conformité
amont est désormais contestée.

P-06
A5 et A7 existent mais restent très peu développées
par rapport à A1-A4.
```

## PROBABLE MAIS À AUDITER

```text
H-01
La quintessence actuelle conserve la substance probatoire,
mais peut perdre une partie de la texture investigative.

H-02
A2 comprend correctement beaucoup de dimensions,
mais ne matérialise peut-être pas suffisamment
le paysage des découvertes inter-investigations.

H-03
A3 compresse probablement trop tôt la matière autour
d'un gain central / contrat éditorial.

H-04
A4 exécute ensuite correctement un contrat éditorial
déjà trop étroit.

H-05
Le NO_GO MARKET_VERTICALS d'A6 dépend probablement
d'une décision A3 qui devra être rechallengée.
```

## NON ENCORE PROUVÉ

```text
N-01
Le PFD détaillé FR-01..FR-23 est-il la vraie PFD courante ?

N-02
FR-12 ESSAI / ENQUÊTE doit-il être réintroduit tel quel ?

N-03
A1-S03 doit-il être modifié sur les 50 quintessences ?

N-04
A2 ou A3 est-il le choke point principal ?

N-05
Quel est le premier nœud exact à rejouer sur déchèteries ?
```

Le plan doit répondre à ces questions par preuve, pas par intuition.

---

# 3. Architecture documentaire minimale retenue

Le système documentaire doit servir deux fonctions différentes.

## 3.1 YAML front matter = orientation au niveau du document

Exemple minimal :

```yaml
---
doc:
  id: EPIC.A3
  type: epic
  title: Décision éditoriale
  status: repair_review

summary: >
  Décide la contribution éditoriale depuis la compréhension A2.
  Ne produit pas la prose.

foundation:
  ref: FOUNDATION.yml

depends_on:
  - EPIC.A2

feeds:
  - EPIC.A4
  - EPIC.A6

contains:
  - STORY.A3-S01
  - STORY.A3-S02
  - STORY.A3-S03
  - STORY.A3-S04
---
```

Le YAML doit permettre au LLM de savoir rapidement :

```text
QUOI ?
AUTORITÉ ?
STATUT ?
DÉPEND DE QUOI ?
CONTIENT QUOI ?
ALIMENTE QUOI ?
QUAND LE LIRE ?
```

Il ne doit pas recopier le contenu normatif.

---

## 3.2 Commentaires Markdown/HTML = traçabilité locale

Syntaxe :

```html
<!-- NODE: STORY.A3-S04 -->
<!-- TRACE: IMPLEMENTS=PFD.F-10; CONSTRAINED_BY=VISION.V11 -->
```

ou, si le PFD détaillé est finalement reconnu autoritatif :

```html
<!-- TRACE: IMPLEMENTS=PFD.FR-11,PFD.FR-12 -->
```

Les commentaires permettent la granularité locale sans polluer la lecture.

---

## 3.3 IDs stables > numéros de lignes

Identité canonique :

```text
VISION.V09
PFD.F-08
EPIC.A3
STORY.A3-S04
STORY.A3-S04.MODE
TEST.A3-S04.DECHETTERIES.MODE
```

Les lignes deviennent seulement des localisations calculées :

```text
ARTICLE_PROTOCOL.md:L1120-L1164
```

Invariant :

```text
SEMANTIC_ID = STABLE
LINE_NUMBER = GENERATED
```

---

# 4. Relations de graphe autorisées V1

KISS : cinq relations maximum.

```text
DERIVES_FROM
IMPLEMENTS
CONSTRAINED_BY
VERIFIED_BY
EXECUTES
```

Pas de nouvelle ontologie sans cas réel.

---

# 5. Un seul binding de fondation

L’ambiguïté actuelle justifie un petit artefact machine-readable :

```text
FOUNDATION.yml
```

Il ne contient aucune nouvelle norme.

Il verrouille seulement l’identité du référentiel.

Exemple :

```yaml
foundation:
  vision:
    id: VISION
    version: V4.4
    file: FOUNDATION/VISION.md
    sha256: "..."

  pfd:
    id: PFD
    version: V4.4
    file: FOUNDATION/PFD.md
    sha256: "..."

status: locked
```

Chaque EPIC référence ensuite :

```yaml
foundation:
  ref: FOUNDATION.yml
```

DRY : les hashes ne sont pas copiés dans huit EPICs.

---

# 6. Phase 0 — Freeze et correction de l’état d’exécution

## Actions

1. Conserver les deux ZIP actuels comme baseline immuable.
2. Conserver leurs SHA-256.
3. Conserver le draft A4-S02 actuel comme oracle négatif.
4. Ne modifier aucun ancien output runtime.
5. Marquer le `NEXT` runtime actuel comme bloqué.
6. Interdire A4-S03/A4-S04 tant que la conformité amont n’est pas résolue.

## Statut proposé

```text
CURRENT_RUNTIME
=
FOUNDATION_CONFORMANCE_REVIEW

A4-S02 CURRENT DRAFT
=
NEGATIVE_PRODUCT_ORACLE

A4-S03
=
BLOCKED

A4-S04
=
BLOCKED
```

## PASS

```text
baseline hashes enregistrés
+
anciens outputs préservés
+
aucun replay aval accidentel
```

---

# 7. Phase 1 — Résoudre l’autorité VISION/PFD

C’est le premier P0.

## 7.1 VISION

Identifier exactement :

```text
nom canonique
version
hash
fichier source
relation avec versions précédentes
```

## 7.2 PFD

Comparer au minimum :

```text
PFD candidate V4.4 / 271 lignes
vs
PFD détaillé / 686 lignes
```

Déterminer :

```text
A. le détaillé est ancien et supersédé
B. le détaillé est nouveau mais non versionné
C. le court est un refactoring qui a perdu des exigences
D. les deux ont des rôles différents
E. autre filiation démontrée
```

Aucune fusion automatique.

## 7.3 Sortie

Une décision d’autorité explicite :

```text
CANONICAL_VISION = ...
CANONICAL_PFD = ...
SUPERSEDED = ...
UNRESOLVED = ...
```

Puis création du snapshot :

```text
FOUNDATION/
  VISION.md
  PFD.md
FOUNDATION.yml
```

Copies read-only de packaging, avec SHA.

## BLOCKER

```text
FOUNDATION_IDENTITY_UNRESOLVED
→ NO STORY REPAIR
```

---

# 8. Phase 2 — Définir la convention de traçabilité dans README

Pas de nouveau gros document.

Ajouter au `README.md` existant une petite section :

```text
TRACE CONVENTION V1
```

Elle définit :

- YAML minimal ;
- `NODE` ;
- `TRACE` ;
- cinq relations ;
- IDs stables ;
- graph généré ;
- règle `metadata != authority`.

Invariant :

```text
YAML SUMMARY != NORMATIVE CONTENT
TRACE EDGE != PROOF BY ITSELF
GENERATED GRAPH != NEW AUTHORITY
```

---

# 9. Phase 3 — Instrumenter VISION/PFD sans changement sémantique

## Actions

1. Snapshot avant instrumentation.
2. Ajouter YAML.
3. Ajouter IDs aux unités normatives.
4. Ajouter les relations PFD → VISION seulement lorsqu’elles sont justifiées.
5. Comparer contenu sémantique pré/post.

## Exemple

```html
<!-- NODE: PFD.F-08 -->
<!-- TRACE: DERIVES_FROM=VISION.V09 -->
```

## Contrôle

```text
SEMANTIC_DIFF = 0
```

hors métadonnées.

---

# 10. Phase 4 — Instrumenter A0-A7 et ARTICLE_PROTOCOL

Pour chaque EPIC :

```text
doc.id
doc.type
status
summary
foundation.ref
depends_on
feeds
contains
```

Pour chaque story :

```html
<!-- NODE: STORY.Ax-Syy -->
<!-- TRACE: IMPLEMENTS=... -->
```

Pour chaque comportement important :

```html
<!-- TRACE: CONSTRAINED_BY=... -->
```

Ne pas taguer chaque phrase.

Seulement les unités qui portent une responsabilité ou une règle matérielle.

---

# 11. Phase 5 — Générer le graphe automatiquement

Créer **un seul petit parser**.

Entrées :

```text
YAML
<!-- NODE -->
<!-- TRACE -->
```

Sorties générées :

```text
TRACEABILITY_GRAPH.tsv
TRACEABILITY_INDEX.json
TRACEABILITY_AUDIT.md
```

Aucune édition manuelle de ces fichiers.

---

# 12. Contrôles mécaniques du graphe

Le parser doit vérifier :

```text
DUPLICATE_NODE
BROKEN_REFERENCE
UNKNOWN_TARGET
ORPHAN_FOUNDATION_NODE
STORY_WITHOUT_PARENT
TEST_WITHOUT_STORY
RUNTIME_WITHOUT_EXECUTED_STORY
```

Le graphe doit également produire les backlinks automatiquement.

Exemple :

```text
PFD.F-08
→ implemented by A2-S01/A2-S02/...
→ tested by ...
→ executed by runtime ...
```

et inversement :

```text
règle runtime
→ story
→ epic
→ PFD
→ VISION
```

---

# 13. Phase 6 — Refaire A0 à la granularité correcte

L’ancien A0 reste historique.

Le nouveau contrôle ne doit plus seulement demander :

```text
F-08 → A2
```

Il doit demander :

```text
F-08
→ quelle story ?
→ quel comportement ?
→ quel test peut le réfuter ?
→ quelle preuve runtime ?
```

Statuts autorisés :

```text
PASS
PARTIAL
GAP
WRONG_OWNER
UNVERIFIED
```

Interdiction :

```text
PASS_CONCEPTUEL
```

comme verdict final d’une exigence censée être exécutable.

---

# 14. Phase 7 — Audit sémantique complet du graphe

Pour chaque nœud normatif applicable :

1. Que demande réellement la fondation ?
2. Quelle EPIC en est responsable ?
3. Quelle story prétend l’implémenter ?
4. Le comportement de la story le fait-il réellement ?
5. Le test peut-il falsifier l’échec correspondant ?
6. Le runtime a-t-il réellement exécuté ce comportement ?
7. Le produit réel confirme-t-il la propriété ?

Formule :

```text
DECLARED_COVERAGE
!=
IMPLEMENTED_COVERAGE
!=
EXECUTED_COVERAGE
!=
PRODUCT_SUCCESS
```

---

# 15. Phase 8 — Réparations locales candidates

Les repairs exacts seront décidés par le graphe.

Les candidats déjà identifiés doivent être **testés**, pas présumés.

---

## 15.1 A1-S03 — Quintessence

Question :

```text
La quintessence conserve-t-elle seulement les unités matérielles
ou aussi le rendement investigatif nécessaire à la narration
et à la compréhension aval ?
```

Le PFD V4.4 court exige déjà que F-06 conserve tout élément pouvant modifier :

```text
compréhension
confiance
scope
décision
narration
conclusion
```

La VISION exige également que les quintessences préservent :

```text
mécanismes
relations
contradictions
réfutations
gaps
connaissance négative
narration
conclusion
```

### Test

Auditer un échantillon discriminant de quintessences contre leur investigation source.

Ne pas refaire les 50 par défaut.

Si un défaut systémique est démontré :

```text
LOCAL CONTRACT REPAIR A1-S03
→ puis replay des seules quintessences affectées
```

Si le PFD détaillé est reconnu canonique, tester en plus explicitement son `Investigation essence`.

---

## 15.2 A2 — Compréhension et rendement inter-investigations

A2 est déjà solide sur :

```text
fonctionnement
histoire
acteurs
règles
flux
mécanismes
contradictions
contre-hypothèses
gaps
```

Il ne faut pas le reconstruire par défaut.

Question :

```text
A2 conserve-t-il suffisamment les découvertes,
relations et surprises issues des investigations
pour que la sélection éditoriale ne parte pas
d'une compréhension aplatie ?
```

Si le PFD détaillé devient canonique :

```text
FR-07 Discovery inventory
```

devient une exigence directe.

Sinon, une vue équivalente ne sera ajoutée que si le défaut est démontré par le runtime et nécessaire pour protéger VISION/F-08.

Pas de nouveau ledger obligatoire.

---

## 15.3 A3 — Sélection éditoriale

Question centrale :

```text
A3 sélectionne-t-il
SANS remplacer la compréhension du sujet
par une promesse minimale trop étroite ?
```

À vérifier :

```text
gain central
contrat éditorial
forme
éléments indispensables
coupes
conclusion
```

Si le PFD détaillé est canonique :

```text
FR-11 Author decision
FR-12 Article mode
```

deviennent directement exécutoires.

Sinon, ne pas introduire mécaniquement `ESSAI|ENQUÊTE`.

On peut néanmoins introduire une distinction minimale de mode si le test réel démontre qu’elle est nécessaire pour protéger :

```text
NO_EARLY_FLATTENING
+
SUBJECT_UNDERSTANDING
+
ARTICLE MUST FEEL INVESTIGATION YIELD
```

---

## 15.4 A4 — Construction et prose

A4 possède déjà une bonne discipline probatoire.

À préserver :

```text
proposition
→ statut
→ portée
→ support
→ provenance
→ prose
```

Question supplémentaire :

```text
Pourquoi ce passage existe-t-il
dans CETTE enquête ?
```

Le chemin peut devoir devenir :

```text
PROSE
→ FONCTION DANS LA PROGRESSION
→ DÉCOUVERTE / MÉCANISME / DIMENSION
→ INVESTIGATION(S)
→ PREUVE
```

Donc :

```text
EVIDENCE TRACE
+
INVESTIGATION-YIELD TRACE
```

Ne pas créer une claim matrix bis.

---

## 15.5 A5 — Review

A5 est actuellement très compact.

Ne pas l’élargir avant A1-A4.

À terme, il devra au minimum savoir détecter :

```text
OVERCLAIM
UNDERCLAIM
FORENSIC_LOSS
GENERICITY
```

plus les défauts déjà couverts par la fondation.

La review doit pouvoir déclarer FAIL même si :

```text
claims traced = 100 %
```

lorsque l’enquête a disparu du produit.

---

## 15.6 A6 — BACK

A6 est globalement cohérent sur :

```text
NO_BLIND_REINVESTIGATION
LOCAL_REPLAY
```

Mais les anciennes décisions dépendantes d’un contrat A3 éventuellement fautif doivent être marquées :

```text
DEPENDENT_DECISION
```

notamment :

```text
MARKET_VERTICALS = NO_GO_CURRENT_CONTRACT
```

Ne pas le transformer automatiquement en GO.

Le rechallenger seulement après nouvelle décision éditoriale si elle change matériellement son utilité.

---

## 15.7 A7 — Validation composée

A7 doit devenir le dernier juge, pas un simple résumé des tests.

Trois passes :

```text
TOP-DOWN
VISION/PFD → EPIC → STORY → TEST → RUNTIME

BOTTOM-UP
RUNTIME RULE → STORY → EPIC → PFD → VISION

PRODUCT
ARTICLE → FINALITÉ VISION/PFD
```

Les trois doivent PASS.

---

# 16. Phase 9 — Mise à jour continue de ARTICLE_PROTOCOL.md

Une story n’entre dans le runtime vivant qu’après :

```text
SPEC
→ TEST
→ FIXTURE
→ AUDIT
→ REPAIR SI NÉCESSAIRE
→ REPLAY
→ PASS
```

Puis seulement :

```text
EPIC story
→ ARTICLE_PROTOCOL.md
```

Pas de réécriture globale du runtime.

---

# 17. Phase 10 — Réparer STATE.json avant tout nouveau replay

Le nouvel état doit refléter le blocage réel.

Exemple sémantique :

```text
phase:
FOUNDATION_CONFORMANCE_REPAIR

blocked:
A4-S03
A4-S04

negative_oracle:
A4_S02_REPLAY_DRAFT_V1

next:
RESOLVE_FOUNDATION_BINDING
→ BUILD_TRACE_GRAPH
→ AUDIT STORY CONFORMANCE
```

L’ancien `NEXT=A4-S03` reste conservé dans l’historique.

---

# 18. Phase 11 — Replay déchèteries piloté par dépendances

Ne pas présumer le point de départ.

Le graphe doit déterminer le premier nœud affecté.

Exemples possibles :

```text
A1-S03
→ A2
→ A3
→ A4
```

ou :

```text
A2
→ A3
→ A4
```

ou seulement :

```text
A3
→ A4
```

Le replay global des 50 investigations est interdit sans preuve de nécessité.

---

# 19. Nouveau replay éditorial déchèteries

Avant prose :

```text
1. compréhension de l'objet
2. rendement des investigations
3. décision éditoriale
4. progression cognitive
```

Puis seulement :

```text
A4-S02 new prose
```

Le nouveau draft ne remplace jamais l’ancien.

---

# 20. Oracle produit

Comparer :

```text
OLD:
A4_S02_REPLAY_DRAFT_V1

NEW:
A4_S02_REPLAY_AFTER_FOUNDATION_REPAIR
```

Dimensions à challenger lorsqu’elles sont matérielles :

```text
objet
histoire
acteurs
relations
entreprises
contrats
flux physiques
flux financiers
données
décisions
incitations
contradictions
réfutations
pistes mortes
zones d'ombre
contribution
conclusion
lisibilité
calibration épistémique
```

Pas de quota.

La liste dépend du sujet.

---

# 21. Test final le plus important

La VISION V4.4 donne déjà ce test :

```text
Le même article aurait-il pu être produit presque à l'identique
sans le travail profond de Truth Engine ?
```

Si oui :

```text
FAIL
```

Même avec :

```text
100 % claims traced
0 HOLD
0 P0/P1 internes
hashes corrects
français parfait
19 sources
```

---

# 22. Packaging final

## Bundle protocole

Doit contenir :

```text
FOUNDATION/
  VISION.md
  PFD.md

FOUNDATION.yml

README.md
EPIC_A0...
...
EPIC_A7...

ARTICLE_PROTOCOL.md

trace parser
TRACEABILITY_GRAPH.tsv
TRACEABILITY_INDEX.json
TRACEABILITY_AUDIT.md

history / decisions utiles
manifest
sha256
```

Les copies `FOUNDATION/` sont des snapshots read-only de packaging, pas une nouvelle autorité éditable.

---

## Bundle runtime déchèteries

Doit contenir :

```text
README
STATE
inputs manifests
outputs historiques
negative oracles
new outputs
tests
audits
repro
manifest
sha256
```

Append-only pour les preuves historiques.

---

# 23. Contrôles mécaniques avant livraison

```text
YAML parses
all NODE ids unique
all TRACE targets resolve
foundation hashes match
no unknown authority
STATE matches files
ARTICLE_PROTOCOL matches validated stories
manifest matches files
bundle root stable
zip test PASS
unzip test PASS
sha256 PASS
no essential historical artifact lost
```

---

# 24. Ordre d’exécution définitif

```text
P0-1 FREEZE BASELINE
    ↓
P0-2 BLOCK STALE NEXT
    ↓
P0-3 RESOLVE FOUNDATION IDENTITY
    ↓
TRACE CONVENTION V1
    ↓
INSTRUMENT FOUNDATION
    ↓
INSTRUMENT A0-A7 + ARTICLE_PROTOCOL
    ↓
GENERATE GRAPH
    ↓
REBUILD A0 CONFORMANCE AUDIT
    ↓
IDENTIFY REAL GAPS
    ↓
LOCAL STORY REPAIRS
    ↓
LOCAL FIXTURE REPLAYS
    ↓
UPDATE ARTICLE_PROTOCOL
    ↓
DEPENDENCY-BASED DECHETTERIES REPLAY
    ↓
NEW A4 PROGRESSION
    ↓
NEW ARTICLE
    ↓
A5
    ↓
A7
    ↓
COLD PRODUCT AUDIT
    ↓
BUNDLE + HASH + UNZIP + POSTCHECK
```

---

# 25. Stop conditions

## STOP immédiat si

```text
FOUNDATION identity unresolved
```

ou :

```text
trace points to unknown/superseded requirement
```

ou :

```text
repair requires inventing a new normative requirement
without demonstrated failure mode
```

ou :

```text
downstream replay starts before impacted upstream node is repaired
```

---

# 26. Definition of Done

Le chantier est terminé seulement si :

```text
1.
Chaque comportement matériel du protocole
peut remonter à une fondation ou à un mode d'échec démontré.

2.
Chaque exigence fondatrice applicable
descend jusqu'à une story, un test et une preuve runtime.

3.
Aucun PASS de couverture n'est fondé uniquement
sur une déclaration d'EPIC.

4.
Le runtime sait dire exactement
quelle fondation il exécute.

5.
Le replay déchèteries produit un article
dont le rendement Truth Engine est identifiable.

6.
L'augmentation de profondeur forensique
ne produit aucune inflation de causalité,
de responsabilité, de portée ou de certitude.

7.
Le produit final passe le test :
"presque le même article sans Truth Engine ?" = NON.

8.
Le système sait s'arrêter.
```

---

# 27. Principe directeur

```text
VISION/PFD
ne doivent plus être des documents que les EPICs disent respecter.

Ils doivent devenir des nœuds dont on peut suivre
l'implémentation réelle jusqu'au produit.

Et inversement,
toute règle du produit doit pouvoir expliquer
pourquoi elle existe.
```

La traçabilité YAML + commentaires n’est donc pas une couche administrative supplémentaire.

Elle devient l’instrument minimal permettant de vérifier :

```text
FOUNDATION
→ IMPLEMENTATION
→ EXECUTION
→ PRODUCT
```

sans perdre le fil, sans charger inutilement le LLM et sans reconstruire mentalement le projet à chaque session.
