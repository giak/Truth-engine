VISION
  ↓ explique / impose
PFD
  ↓ spécifie / rend testable
EPIC
  ↓ porte une responsabilité
STORY
  ↓ implémente une tranche minimale
FIXTURE / TEST
  ↓ éprouve
RUNTIME RESULT
  ↓ fournit la preuve d'exécution
AUDIT
  ↓ confirme / réfute
REPAIR
  ↓ corrige localement
REPLAY

---

Oui. Il faut profiter de cette réparation pour remettre **la chaîne entière sous contrôle forensique**, mais sans créer une deuxième architecture autour de l’architecture.

Le principe de départ est déjà dans l’EPIC Map : les EPIC dérivent de VISION/PFD, ne les remplacent pas, et aucune régression contre VISION/PFD n’est permise.  Le problème est que cette relation est aujourd’hui essentiellement déclarative. Il faut la rendre **navigable, auditable et testable**.

## 1. Traçabilité : utiliser `<!-- ... -->`, mais avec des identifiants stables

Je recommande de ne **pas** utiliser le numéro de ligne comme identifiant principal. Une modification de trois lignes casserait immédiatement les références.

Le modèle minimal :

```markdown
<!-- NODE: VISION.V16 -->
### V16. L'auteur décide ; le LLM ne déplace pas silencieusement le but.
```

Puis dans PFD :

```markdown
<!-- NODE: PFD.FR-12 -->
<!-- TRACE: DERIVES_FROM=VISION.V16 -->
### FR-12 — Article mode
```

Puis dans l’EPIC :

```markdown
<!-- NODE: EPIC.A3 -->
<!-- TRACE: IMPLEMENTS=PFD.FR-11,PFD.FR-12 -->
# A3 — Décision éditoriale
```

Puis dans la story :

```markdown
<!-- NODE: STORY.A3-S04 -->
<!-- TRACE: DERIVES_FROM=EPIC.A3; IMPLEMENTS=PFD.FR-11,PFD.FR-12; CONSTRAINED_BY=VISION.V16 -->
## A3-S04 — Prendre une décision pré-rédactionnelle
```

Puis le test :

```markdown
<!-- NODE: TEST.A3-S04.DECHETTERIES-ARTICLE-MODE -->
<!-- TRACE: VERIFIES=STORY.A3-S04; REQUIREMENT=PFD.FR-12 -->
```

Et le résultat runtime :

```markdown
<!-- TRACE: EXECUTES=STORY.A3-S04; TESTED_BY=TEST.A3-S04.DECHETTERIES-ARTICLE-MODE -->
```

### Ligne ou paragraphe

On peut générer automatiquement :

```text
PFD.md::PFD.FR-12::L557-L568
```

mais **ne pas maintenir ces lignes à la main**.

L’identité canonique reste :

```text
PFD.FR-12
```

Le numéro de ligne est seulement une vue calculée au moment de l’audit.

Cela évite une montagne de maintenance DRY.

---

# 2. Quatre relations suffisent

Je ne créerais pas une ontologie.

Seulement :

```text
DERIVES_FROM
IMPLEMENTS
CONSTRAINED_BY
VERIFIED_BY
```

Et pour le runtime, éventuellement :

```text
EXECUTES
```

C’est suffisant pour répondre aux questions importantes :

```text
Pourquoi cette règle existe ?
→ remonter vers PFD/VISION

Où FR-12 est-il implémenté ?
→ descendre vers EPIC/story

Comment savons-nous qu'il fonctionne ?
→ suivre VERIFIED_BY

Qu'est-ce qui a réellement été exécuté ?
→ suivre EXECUTES
```

Pas de Neo4j, pas de RDF, pas de base dédiée.

Un petit parser des commentaires suffit.

---

# 3. Un seul artefact de graphe dérivé

Les commentaires dans les documents constituent la source.

Un script très simple pourra produire :

```text
TRACEABILITY_GRAPH.tsv
```

Colonnes minimales :

| from         | relation     | to           | document            | location |
| ------------ | ------------ | ------------ | ------------------- | -------- |
| PFD.FR-12    | DERIVES_FROM | VISION.V16   | PFD.md              | L...     |
| EPIC.A3      | IMPLEMENTS   | PFD.FR-12    | EPIC_A3...md        | L...     |
| STORY.A3-S04 | IMPLEMENTS   | PFD.FR-12    | ARTICLE_PROTOCOL.md | L...     |
| TEST...      | VERIFIED_BY  | STORY.A3-S04 | ...                 | L...     |

Ce TSV est **dérivé**.

Il ne devient pas une nouvelle vérité normative.

On pourra également générer une vue Mermaid, mais uniquement comme visualisation.

---

# 4. Plan de remise à plat

Je mènerais quatre chantiers en parallèle, mais avec des dépendances strictes :

| Chantier                 | Travail                                                       | Peut avancer immédiatement           |
| ------------------------ | ------------------------------------------------------------- | ------------------------------------ |
| **T — Trace**            | instrumenter VISION/PFD/EPIC/story/test/runtime               | oui                                  |
| **C — Conformance**      | construire le graphe et chercher les trous                    | oui                                  |
| **R — Repair**           | réparer les stories réellement non conformes                  | après identification du propriétaire |
| **P — Protocol runtime** | intégrer chaque réparation validée dans `ARTICLE_PROTOCOL.md` | au fil des repairs                   |

Ce n’est donc pas quatre branches indépendantes. C’est un pipeline de développement avec feedback rapide.

---

# 5. Étape 0 : geler le point de départ

Avant mutation :

```text
VISION/PFD semantic baseline = FROZEN
EPIC docs baseline = FROZEN
ARTICLE_PROTOCOL current = FROZEN
runtime déchèteries current = NEGATIVE ORACLE
draft actuel = NEGATIVE PRODUCT ORACLE
```

Hashes + manifest.

**Important : VISION/PFD ne sont pas à réécrire.**

Le double-check montre qu’ils contiennent déjà précisément les exigences que nous cherchons :

* essence de chaque investigation ;
* inventaire des découvertes ; 
* décision d’auteur ;
* distinction `ESSAI / ENQUÊTE` ; 
* enquête visible par documents, acteurs, contradictions, pistes fermées, mécanismes ; 
* flows concrets ; 
* anti-stérilisation. 

On leur ajoute seulement les `NODE`/`TRACE` nécessaires.

---

# 6. Étape 1 : instrumenter VISION et PFD

Pas chaque paragraphe.

Seulement les unités normatives réellement référencées :

```text
VISION.V1 ... V21
PFD.F-xx
PFD.FR-xx
PFD.NFR-xx
PFD.AC-xx
```

Chaque exigence PFD doit dire de quels invariants VISION elle découle.

Exemple :

```markdown
<!-- NODE: PFD.FR-15 -->
<!-- TRACE: DERIVES_FROM=VISION.V7,VISION.V17 -->
### FR-15 — Show the investigations
```

À la fin de cette étape, on peut mécaniquement répondre :

```text
VISION -> PFD
```

sans interprétation libre.

---

# 7. Étape 2 : instrumenter toutes les EPIC

Chaque EPIC doit déclarer :

```text
RESPONSIBILITY
IMPLEMENTS
CONSTRAINED_BY
DOES_NOT_OWN
```

Le dernier point est important pour éviter que deux EPIC pensent posséder la même décision.

Exemple :

```markdown
<!-- NODE: EPIC.A3 -->
<!-- TRACE:
IMPLEMENTS=PFD.FR-09,PFD.FR-10,PFD.FR-11,PFD.FR-12;
CONSTRAINED_BY=VISION.V13,VISION.V14,VISION.V16;
-->
```

Pas besoin de recopier les exigences.

---

# 8. Étape 3 : instrumenter toutes les stories

C’est là que l’audit devient réellement forensique.

Chaque story doit répondre implicitement à :

```text
Pourquoi existe-t-elle ?
Quelle exigence implémente-t-elle ?
Quelle partie seulement ?
Qui possède le reste ?
Comment savons-nous qu'elle fonctionne ?
```

Et surtout :

```text
STORY CLAIMS PFD.FR-xx
mais
BEHAVIOR DOES NOT IMPLEMENT PFD.FR-xx
```

doit devenir détectable.

C’est précisément notre cas actuel.

---

# 9. Étape 4 : construire le crosswalk complet

Le parser produit alors :

```text
VISION
 ↓
PFD
 ↓
EPIC
 ↓
STORY
 ↓
TEST
 ↓
RUNTIME
```

Puis on cherche quatre anomalies seulement :

```text
ORPHAN_REQUIREMENT
PARTIAL_IMPLEMENTATION
UNJUSTIFIED_BEHAVIOR
UNVERIFIED_IMPLEMENTATION
```

Définitions :

```text
ORPHAN_REQUIREMENT
PFD requirement sans story propriétaire

PARTIAL_IMPLEMENTATION
story reliée mais comportement incomplet

UNJUSTIFIED_BEHAVIOR
règle de story sans parent VISION/PFD/failure mode

UNVERIFIED_IMPLEMENTATION
implémentation sans test réel
```

Cela suffit.

---

# 10. Le premier audit va probablement produire ces défauts

Nous en connaissons déjà plusieurs.

### FR-06 : Investigation essence

PFD exige explicitement l’apport propre de chaque investigation avant hiérarchisation. 

Propriétaire minimal probable :

```text
A1-S03
```

Aujourd’hui A1-S03 conserve correctement la substance épistémique, mais beaucoup moins explicitement :

```text
ce que l'enquête cherchait
la découverte
la surprise
la piste détruite
l'incarnation narrative
```



**Réparation locale A1-S03.**

Pas nouvelle story.

---

### FR-07 : Discovery inventory

Il manque actuellement une implémentation claire de l’inventaire inter-investigations.

Propriétaire probable :

```text
A2-S01
```

ou à la frontière S01/S02.

Je privilégie **A2-S01** :

```text
N quintessences
→ comprendre ensemble
→ rendre visibles découvertes et relations inter-investigations
```

Puis A2-S02 peut reconstruire l’objet.

Pas nouveau ledger.

Une **vue** de la matière existante.

---

# 11. Réparation A1-S03

Il ne faut surtout pas transformer chaque quintessence en formulaire monstrueux.

Ajouter seulement une obligation sémantique :

```text
Pour chaque investigation importante, la quintessence doit permettre
de retrouver, lorsque présents :

QUESTION / OBJET CHERCHÉ
DÉCOUVERTE
MÉCANISME / RELATION
RÉFUTATION / PISTE MORTE
SURPRISE / ANOMALIE
INCONNUE IMPORTANTE
INCARNATION UTILE
```

Pas nécessairement sept champs.

Cela peut être du texte.

Le test porte sur la récupération, pas le format.

---

# 12. Réparation A2

A2 doit produire deux choses différentes :

```text
OBJECT UNDERSTANDING
+
DISCOVERY LANDSCAPE
```

Pas deux systèmes.

Deux **vues cognitives** de la même matière.

Exemple déchèteries :

```text
OBJECT
déchetterie comme nœud territorial de flux

DISCOVERIES
- généalogie 1980 → massification
- dates SINOE trompeuses
- centralité tonnage 2024
- contrôle multi-local
- Saint-Étienne
- professionnels
- dépôts sauvages
- Symetri/TRIBORD
- marchés/exploitants
- REP
- money flows
- contradictions de responsabilités
- dead frames
...
```

Cette vue aurait empêché qu’un corpus de 50 investigations devienne une seule question sur la prévalence du contrôle.

---

# 13. Réparation A3 : séparer enfin MODE et FORME

C’est probablement la réparation la plus petite et la plus importante.

Aujourd’hui :

```text
FORME_LONGUE
SHORTER_OUTPUT
MORE_INVESTIGATION
NO_ARTICLE
```



Il faut distinguer deux décisions orthogonales :

```text
ARTICLE_MODE
=
ESSAI | ENQUÊTE
```

et :

```text
OUTPUT_FORM
=
LONG | SHORT | NONE | MORE_INVESTIGATION
```

PFD impose déjà explicitement la différence ESSAI/ENQUÊTE. 

Cela corrige une confusion conceptuelle réelle :

```text
LONG != ENQUÊTE
SHORT != ESSAI
```

Un essai peut être long.

Une enquête peut être relativement courte.

---

# 14. Compléter A3-S04 avec FR-11, pas le réinventer

La décision pré-rédactionnelle doit devenir réellement la **décision d’auteur** définie par PFD.

Elle doit connaître :

```text
sujet réel
mode
apport
tension
découverte centrale
question/thèse organisatrice
éléments indispensables
coupes conscientes
conclusion probable
question ouverte
```



Pas besoin d’un nouveau fichier si l’artefact S04 existant peut les contenir.

---

# 15. Réparation A4-S01 : comportement différent selon le mode

### ESSAI

Une thèse ou un mécanisme peut réellement organiser le reste :

```text
QUESTION / THÈSE
↓
mécanisme
↓
preuve
↓
contre-hypothèse
↓
conséquences
↓
conclusion
```

### ENQUÊTE

L’objet organise :

```text
ANOMALIE / QUESTION
↓
OBJET
↓
HISTOIRE UTILE
↓
MACHINE / ACTEURS
↓
FLUX
↓
ARGENT / CONTRATS
↓
MÉCANISMES
↓
ANOMALIES / PISTES
↓
CONTRE-HYPOTHÈSES
↓
CE QUI RÉSISTE
↓
CE QUI RESTE OUVERT
```

Ce second schéma n’est **pas un template obligatoire**.

La règle générique est simplement :

```text
ENQUÊTE
→ ORCHESTRATE MATERIAL DIMENSIONS OF THE OBJECT
→ DO NOT SUBORDINATE THEM ALL TO ONE CLAIM
```

---

# 16. Retirer du protocole générique ce qui appartient au fixture déchèteries

C’est une anomalie importante.

A4-S01 contient actuellement des règles comme :

> « préserver le noyau C-01 » et faire du paradoxe diffusion multi-locale / tendance nationale le structurant de progression. 

Cela appartient à **l’exécution déchèteries**, pas à la règle générique de construction.

Il faut séparer :

```text
GENERIC PROTOCOL RULE
```

de :

```text
FIXTURE-SPECIFIC DECISION
```

Sinon le protocole vivant se contamine progressivement avec chaque sujet testé.

---

# 17. Réparation A4-S02 : double provenance

A4-S02 sait déjà vérifier :

```text
PROSE
→ proposition
→ preuve
```

Il faut simplement ajouter l’autre axe :

```text
PROSE
→ découverte / mécanisme / objet
→ investigation(s)
```

Donc :

```text
EVIDENCE TRACE
+
INVESTIGATION TRACE
```

Une unité peut être parfaitement soutenue et malgré tout être éditorialement stérile.

Les deux questions deviennent :

```text
Est-ce vrai ?
Pourquoi ce passage existe-t-il dans CETTE enquête ?
```

---

# 18. Réparation A4-S03 / A5

Le review doit alors attaquer dans les deux directions :

```text
OVERCLAIM
UNDERCLAIM
FORENSIC_LOSS
GENERICITY
```

Et poser réellement FR-15 :

> sent-on qu’une enquête a eu lieu ?

PFD donne déjà les discriminants : documents, chiffres, histoires, acteurs, contradictions, découvertes, recherches difficiles, pistes fermées, mécanismes. 

Donc aucune nouvelle théorie d’audit n’est nécessaire.

---

# 19. A6 : vérifier qu’il accepte bien les gaps découverts par reconstruction

A6 ne doit pas seulement rouvrir pour :

```text
CLAIM NEEDS MORE EVIDENCE
```

Mais aussi pour un trou matériel découvert pendant l’écriture :

```text
acteur inconnu
relation inconnue
destination de flux inconnue
contrat manquant
contradiction nouvelle
bénéficiaire non déterminé
```

VISION prévoit déjà explicitement ce BACK cognitif. 

Donc ici encore : **conformance repair**, pas invention.

---

# 20. A7 devient le vrai juge composé

A7 doit parcourir le graphe dans les deux sens.

### Top-down

```text
VISION/PFD
→ chaque exigence importante a-t-elle une implémentation ?
→ un test ?
→ un résultat réel ?
```

### Bottom-up

```text
chaque comportement important du runtime
→ pourquoi existe-t-il ?
→ quelle exigence protège-t-il ?
```

Et surtout le test réel de PFD reste souverain :

> aurait-on pu produire presque le même article sans plusieurs jours d’investigations Truth Engine ?

Si oui, échec. 

---

# 21. Replay déchèteries

Seulement après les réparations minimales.

Je ne repartirais pas des 50 investigations brutes aveuglément.

Le graphe de dépendance donnera probablement :

```text
A1-S03 local replay
      ↓
A2-S01/S02 affected replay
      ↓
A3 full replay
      ↓
A4 full replay
      ↓
A5
      ↓
A7
```

A1-S01/S02/S04 ne sont probablement pas à rejouer sauf impact découvert.

Même principe pour les parties A2 non affectées.

---

# 22. Oracle réel du replay

Le draft actuel est conservé.

Le nouveau produit est comparé à lui sur des questions qui comptent :

| Dimension     | Draft actuel         | Attendu                                      |
| ------------- | -------------------- | -------------------------------------------- |
| Histoire      | superficielle        | enquête historique exploitable               |
| Objet         | correct              | profond                                      |
| Acteurs       | taxonomie            | acteurs nommés + rôles + relations           |
| Sociétés      | marginales           | investiguées selon matérialité               |
| Contrats      | exemples             | chaîne reconstruite autant que possible      |
| Money         | prudence             | `follow the money` réel                      |
| Cui bono      | quasiment neutralisé | bénéficiaires testés sans intention inventée |
| Flux matière  | partiel              | chaînes et ruptures                          |
| Pistes mortes | quasi absentes       | visibles lorsqu’instructives                 |
| Zones d’ombre | caveats              | résultats d’enquête                          |
| Narration     | note analytique      | enquête                                      |
| Épistémologie | forte                | au moins aussi forte                         |

La dernière ligne est impérative :

```text
FORENSIC_DEPTH ↑
MUST NOT CAUSE
EPISTEMIC_DISCIPLINE ↓
```

---

# 23. Ordre d’exécution concret

Je suivrais cet ordre de travail unique :

1. **Snapshot + hashes** de VISION/PFD/EPIC/protocole/runtime.
2. Ajouter les `NODE` aux VISION/PFD sans changement sémantique.
3. Ajouter les `TRACE` PFD → VISION.
4. Ajouter les `NODE/TRACE` aux EPICs.
5. Ajouter les `NODE/TRACE` aux stories actuelles.
6. Générer le premier `TRACEABILITY_GRAPH.tsv`.
7. Auditer tous les `PFD FR/NFR/AC → EPIC → STORY`.
8. Classer uniquement `PASS / PARTIAL / GAP / WRONG_OWNER`.
9. Réparer les vrais gaps dans la plus petite story existante.
10. Mettre `ARTICLE_PROTOCOL.md` à jour **à chaque repair validé**, pas à la fin.
11. Rejouer localement les fixtures de chaque story réparée.
12. Recalculer le graphe après chaque repair.
13. Vérifier zéro `ORPHAN_REQUIREMENT` matériel.
14. Rejouer déchèteries depuis le premier nœud réellement affecté.
15. Produire un nouvel article complet.
16. Audit froid contre PFD + quatre derniers articles Substack.
17. A7 composé.
18. Seulement ensuite décider si la nouvelle implémentation des EPIC peut être considérée comme cohérente avec VISION/PFD.

C’est la voie que je considère la plus robuste : **on ne redessine plus le système ; on transforme enfin VISION/PFD en graphe normatif traçable, puis on répare uniquement les arêtes cassées jusqu’au produit réel.**
