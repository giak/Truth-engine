Oui. Et je corrige aussi ma proposition précédente : **ajouter davantage de registres et de phases serait une mauvaise réponse**. On risquerait de remplacer un protocole trop lisse par une usine à gaz.

Le véritable enjeu est plus simple et plus profond :

> **Le protocole d’écriture doit préserver la topologie de l’enquête, pas seulement ses conclusions.**

C’est cela que nous n’avons pas encore correctement formalisé.

## 1. Le but exact

Truth Engine n’est pas un générateur de faits vérifiés destiné ensuite à alimenter un rédacteur.

C’est un **moteur d’investigation adversarial**.

Il cherche le delta, les contradictions, les pièces manquantes, les relations inattendues, les signaux faibles ; chaque trouvaille devient une clé pour pivoter sur noms, organisations, montants, propriétaires, intermédiaires, fournisseurs, bénéficiaires, identifiants, juridictions, etc. Il conserve explicitement lièvres, anguilles, loups, zones d’ombre, rumeurs sourcées et faisceaux. 

L’article issu de ce travail doit donc transmettre au lecteur non seulement :

> « voici ce qui est vrai »

mais aussi :

> « voici le système que nous avons découvert, les acteurs qui l’occupent, les intérêts qui circulent, ce qui ne colle pas, les pistes que nous avons testées, celles que nous avons tuées, celles qui résistent et les endroits où la lumière s’arrête ».

**C’est cela, la fidélité forensique.**

---

# 2. « Tout raconter » ne signifie pas tout mettre dans l’article

Il faut être très précis ici.

Un article ne doit pas contenir chaque recherche Google, chaque doublon, chaque hypothèse morte ni chaque lead médiocre.

Ce serait illisible.

L’objectif réel est :

> **aucune dimension matériellement importante de l’enquête ne doit disparaître par compression éditoriale.**

Il faut préserver la **structure informationnelle**, pas tout le volume documentaire.

Exemple :

100 documents établissent une relation entre trois acteurs.

L’article n’a pas besoin des 100 documents.

Mais il ne doit pas transformer :

```text
A
├─ finance B
├─ contracte avec C
└─ partage un dirigeant avec D
       ↓
       fournisseur de B
```

en :

> « plusieurs acteurs interviennent ».

C’est exactement ce que j’appellerais désormais :

**`FORENSIC_LAUNDERING`**

Le matériau est techniquement présent mais il a été lavé de ce qui faisait son intérêt.

---

# 3. La séparation fondamentale doit être à trois niveaux

Le V2 avait deux pipelines :

`épistémique` et `éditorial`. 

Il en faut **trois**.

| Couche            | Question                                              |
| ----------------- | ----------------------------------------------------- |
| **INVESTIGATION** | Qu’est-ce qui se cache réellement derrière le sujet ? |
| **EPISTEMIC**     | Qu’avons-nous le droit d’affirmer ?                   |
| **EDITORIAL**     | Comment raconter ce que l’enquête a révélé ?          |

C’est essentiel.

Nous avions fusionné les deux premières.

Or :

### Investigation

peut contenir :

`LEAD`, `SUSPICION`, `ANOMALY`, `RUMOR_SOURCED`, `TRACE_BREAK`, `CONFLICT`, `NETWORK_EDGE`, `UNKNOWN_HIGH_VALUE`.

### Épistémique

dit ensuite :

`FACT`, `EVIDENCE`, `INFERENCE`, `HYPOTHESIS`, `FALSIFIED`, `UNKNOWN`.

### Éditorial

décide :

`BODY`, `CASE`, `BOX`, `FIGURE`, `DROP`.

**Un lead qui n’est pas devenu FACT n’a pas nécessairement échoué.**

Il peut avoir révélé :

* une nouvelle société ;
* une relation contractuelle ;
* un changement de version ;
* un trou documentaire ;
* une contradiction ;
* une question impossible à résoudre avec les données publiques.

C’est un résultat d’enquête.

---

# 4. La règle la plus importante à introduire

Je remplacerais une grande partie de nos mécanismes compliqués par cet invariant :

> **`ASSERTION_RIGHT != INVESTIGATION_VALUE != EDITORIAL_VALUE`**

Trois grandeurs indépendantes.

Une accusation non prouvée :

`ASSERTION_RIGHT = 0`

mais le lead qui l’a déclenchée peut avoir :

`INVESTIGATION_VALUE = HIGH`

et la manière dont nous avons tenté de la vérifier peut avoir :

`EDITORIAL_VALUE = HIGH`.

C’est cette séparation que nous avions ratée.

---

# 5. Le « 95 % suspicion »

Je conserverais l’idée, mais **pas comme probabilité**.

Sinon nous construisons institutionnellement un biais de confirmation.

La bonne spécification est :

```text
INVESTIGATION_POSTURE = MAX_ADVERSARIAL
DEFAULT_TRUST = LOW
DEFAULT_VERIFICATION = HIGH
EVIDENCE_THRESHOLD = UNCHANGED
```

Ou, en langage humain :

> **95 % de suspicion dans l’effort de recherche ; 0 % de cadeau dans la preuve.**

On soupçonne :

* la communication officielle ;
* l’accusation militante ;
* les statistiques ;
* les agrégations ;
* les motivations déclarées ;
* les coïncidences ;
* les conflits d’intérêts apparents ;
* les récits médiatiques ;
* nos propres hypothèses.

Mais la suspicion ne donne **aucun droit supplémentaire à affirmer**.

Le vrai Truth Engine doit être capable de passer dix heures à essayer de démontrer quelque chose puis d’écrire :

> `FALSIFIED`.

C’est même un signe de qualité.

---

# 6. Colombo et Sherlock : ce que cela signifie opérationnellement

Ce n’est pas « chercher du scandale ».

C’est une méthode.

Un détail cloche.

On ne l’abandonne pas parce qu’il paraît périphérique.

On demande :

> Pourquoi ?

Une date ne correspond pas.

> Pourquoi ?

Deux sociétés apparaissent.

> Quel lien ?

Un prestataire change de nom.

> Qui le possède ?

Un montant augmente.

> Où va l’argent ?

Un professionnel disparaît d’un dispositif public.

> Où va son flux ?

Une organisation finance un dispositif.

> Quel intérêt ? Quel pouvoir ? Quel contrat ?

Un chiffre disparaît de la version suivante d’un rapport.

> Pourquoi ? Quelle était la version précédente ?

Un article est supprimé.

> Archive.

Une affirmation est répétée par dix médias.

> Source originelle.

Trois « sources » remontent au même communiqué.

> Une seule source, pas trois.

Le protocole Truth Engine décrit déjà cette mécanique de pivot. 

**Le protocole d’écriture doit simplement ne pas l’effacer.**

---

# 7. Le plus gros changement : ne pas dupliquer Truth Engine

C’est là que ma proposition précédente était trop lourde.

Je proposais :

* forensic ledger ;
* entity graph ;
* money ledger ;
* contract ledger ;
* trace gap ledger ;
* lead register ;
* etc.

Trop.

DRY violation.

Truth Engine possède déjà la fonction investigation.

Le protocole d’article a seulement besoin d’un **contrat d’interface**.

Je réduirais tout à quatre artefacts canoniques.

| Artefact              | Fonction                                   |
| --------------------- | ------------------------------------------ |
| `CLAIM_MATRIX`        | ce que l’on peut affirmer                  |
| `FORENSIC_MAP`        | ce que l’enquête a révélé ou rendu suspect |
| `INVESTIGATION_QUEUE` | ce qui mérite encore d’être poursuivi      |
| `ARTICLE_MAP`         | ce qui sera raconté et comment             |

C’est tout.

Les autres objets sont des **vues** de `FORENSIC_MAP`.

`ACTORS`, `MONEY`, `CONTRACTS`, `LIEVRES`, `ANGUILLES`, `LOUPS`, `UNKNOWN`, etc. ne nécessitent pas chacun leur propre système.

---

# 8. Le cœur nouveau : `FORENSIC_MAP`

Il constitue le chaînon manquant.

Chaque item possède seulement les propriétés nécessaires :

```text
ID
TYPE
STATEMENT
ENTITIES
RELATIONS
EPI_STATUS
MATERIALITY
SOURCE_TRACE
OPEN_QUESTION
NEXT_ACTION
DISPOSITION
```

`TYPE` peut notamment être :

```text
FACT
CLAIM
ANOMALY
CONTRADICTION
LEAD
RUMOR_SOURCED
LIEVRE
ANGUILLE
LOUP_CANDIDATE
LOUP_ESTABLISHED
FAISCEAU
TRACE_BREAK
MONEY_FLOW
CONTRACT
OWNERSHIP
ACTOR
INTERMEDIARY
BENEFICIARY
UNKNOWN
DEAD_FRAME
```

Pas besoin de 17 CSV différents.

Une base logique.

Plusieurs vues.

**KISS + DRY.**

---

# 9. La matérialité devient plus importante que le statut probatoire pour l’APPEX

Nous avons également fait une erreur en donnant trop de pouvoir à `EVIDENCE_LEVEL`.

Pour savoir si on continue à enquêter, la bonne question n’est pas :

> ce point est-il fortement prouvé ?

Mais :

> **si nous comprenions ce point, cela changerait-il significativement notre compréhension du sujet ?**

Je n’utiliserais même pas un score 0-100.

Trois niveaux suffisent :

`HIGH | MEDIUM | LOW`

Un `HIGH` peut être :

* un bénéficiaire potentiel ;
* la destination d’un gros flux ;
* un marché majeur ;
* une relation de propriété ;
* une contradiction centrale ;
* un effet social important ;
* une suspicion sérieuse ;
* une donnée indispensable à une causalité.

Un `LOW` peut rester irrésolu.

Un `HIGH` ne peut pas disparaître silencieusement.

---

# 10. APPEX doit être très simple

Pas vingt critères.

L’APPEX est atteint quand :

> **aucune piste HIGH encore investigable à coût raisonnable n’est laissée volontairement inexplorée.**

C’est le critère.

Pour chaque item `HIGH`, trois sorties seulement :

```text
RESOLVED
BLOCKED
MORE_INVESTIGATION
```

`BLOCKED` doit préciser pourquoi :

```text
DATA_NOT_PUBLIC
SOURCE_UNAVAILABLE
LEGAL_LIMIT
NO_IDENTIFIABLE_SOURCE
REQUIRES_DIRECT_REQUEST
REQUIRES_NON_AVAILABLE_CAPABILITY
```

Et surtout :

`BLOCKED != UNIMPORTANT`.

---

# 11. Il faut supprimer l’actuelle logique de « fin de web »

Le V2 dit encore que la frontière publique peut constituer une sortie terminale. 

C’est trop simpliste.

Il existe une hiérarchie naturelle :

```text
web ordinaire
↓
sources primaires
↓
archives
↓
registres
↓
marchés publics
↓
documents juridiques
↓
données structurées
↓
historique des entités
↓
demandes de données
↓
source directe
↓
BLOCKED
```

On ne doit pas obligatoirement aller jusqu’au fond de cette pyramide pour chaque piste.

Mais un item `HIGH` ne peut pas devenir `UNKNOWN` simplement parce que trois requêtes web n’ont rien donné.

---

# 12. L’écriture elle-même peut rouvrir l’enquête

C’est un point sur lequel notre state machine est actuellement fausse.

Elle n’autorise pratiquement un retour à T2 que si le niveau de preuve requis change. 

Or écrire est aussi un **test cognitif**.

En essayant d’expliquer une relation, on découvre souvent :

> « Attends. Pourquoi A verse à B ? »

ou :

> « Nous savons que le flux quitte X, mais nous n’avons jamais vérifié où il arrive. »

ou :

> « Cet acteur apparaît dans quatre sections mais nous ne savons presque rien de lui. »

Ce n’est pas « chercher une meilleure histoire ».

C’est découvrir un **gap réel par reconstruction du système**.

Le retour doit donc être autorisé si :

```text
NEW_MATERIAL_GAP
NEW_ACTOR
NEW_RELATION
NEW_CONTRADICTION
NEW_HIGH_VALUE_LEAD
TRACE_BREAK
SYSTEM_INCOHERENCE
```

Pas seulement `CLAIM_NEEDS_MORE_PROOF`.

---

# 13. Mais il faut éviter l’enquête infinie

C’est l’autre danger.

Avec une posture de suspicion maximale, on peut toujours chercher davantage.

Le protocole doit protéger contre ça.

La règle d’arrêt est :

> **pas “avons-nous tout découvert ?”, mais “reste-t-il une action accessible à forte valeur informationnelle sur une question matérielle ?”**

Si non :

APPEX.

Même avec des UNKNOWN.

Même avec des BLOCKED.

Même avec des soupçons irrésolus.

C’est une vraie notion de saturation.

---

# 14. Le protocole final peut donc être beaucoup plus simple que V2

Je simplifierais même la state machine.

### Investigation

```text
T0 SUBJECT CONTRACT

T1 TRUTH ENGINE × N
    ↕
T2 RECONCILE / PROVE
    ↕
T3 FORENSIC MAP + INVESTIGATION QUEUE
    ↓
APPEX GATE
    ├─ MORE_INVESTIGATION → T1/T2
    └─ PASS / BLOCKED
```

### Écriture

```text
T4 SYNTHESIZE
T5 DESIGN
T6 MODULES
T7 WEAVE
T8 ATTACK
T9 FORENSIC COVERAGE
T10 FINAL
```

C’est plus simple que notre actuel T3A→T3F morcelé.

`DISCOVERY_ATLAS`, `SYSTEM_MAP`, `QUESTION_GRAPH` restent utiles, mais deviennent **trois vues de SYNTHESIZE**, pas trois phases administratives.

Même chose pour `EDITORIAL_VALUE_MAP`, `ARCHITECTURE_LAB`, `PORTFOLIO` : vues de DESIGN.

Moins d’états.

Moins de fichiers.

Même rigueur.

---

# 15. Le protocole doit vérifier deux couvertures différentes

Nous n’avions qu’un Coverage Gate.

Il en faut deux.

### `FORENSIC_COVERAGE`

Avant écriture :

> avons-nous correctement représenté ce que Truth Engine a réellement découvert ?

Il compare :

`INVESTIGATIONS → FORENSIC_MAP`.

### `EDITORIAL_COVERAGE`

Après écriture :

> qu’avons-nous supprimé entre FORENSIC_MAP et ARTICLE ?

Il compare :

`FORENSIC_MAP → ARTICLE_MAP → ARTICLE`.

Cela aurait immédiatement détecté notre problème déchetteries.

---

# 16. Tout ne doit pas être dans le corps de l’article

Une investigation très riche peut produire :

* article ;
* encadrés ;
* graphes ;
* timeline ;
* annexes ;
* dossier acteurs ;
* notes méthodologiques.

Le Coverage Gate ne doit donc pas exiger :

`HIGH → BODY`.

Il exige :

`HIGH → EXPLICIT_DESTINATION`.

Par exemple :

```text
BODY
CASE_FILE
BOX
FIGURE
NETWORK_GRAPH
TIMELINE
ANNEX
OPEN_QUESTION
DROP_WITH_REASON
```

Cela permet de raconter **beaucoup** sans fabriquer un monstre illisible.

---

# 17. L’article doit conserver la texture de l’enquête

Voilà probablement le point éditorial le plus important.

Au lieu de :

> « Les données ne permettent pas d’établir une causalité entre les restrictions et les dépôts sauvages. »

on peut écrire :

> Des sacs sont pourtant là, au pied des colonnes. La tarification existe. Certains habitants l’accusent. Les élus répondent que les dépôts existaient avant. Nous avons cherché une série permettant de départager les deux récits. Nous ne l’avons pas trouvée.

Même niveau de preuve.

Mais **100 fois plus fidèle à l’enquête**.

La prose forensique doit souvent suivre :

```text
OBSERVATION
→ SOUPÇON
→ INVESTIGATION
→ CE QUE NOUS AVONS TROUVÉ
→ CE QUI RÉSISTE
```

Pas seulement :

```text
CONCLUSION PRUDENTE
```

C’est ce qui évite l’effet mainstream.

---

# 18. Il faut réhabiliter les hypothèses mortes

Une enquête puissante produit aussi du **négatif**.

Par exemple :

> Nous avons soupçonné X.

Puis :

> les documents ne soutiennent pas cette hypothèse.

Cela mérite parfois d’être raconté.

Pourquoi ?

Parce que cela montre :

* que nous avons réellement cherché ;
* où étaient les apparences trompeuses ;
* quelles explications ont survécu ;
* que l’article n’est pas construit à charge.

Un `DEAD_FRAME` important peut donc avoir une grande valeur éditoriale.

Truth Engine ne doit pas être visible seulement quand il trouve un loup.

Il doit aussi être visible quand il découvre que **le loup n’était qu’un chien dans l’ombre**.

---

# 19. Le réseau doit devenir une structure éditoriale de première classe

Un sujet systémique doit faire apparaître :

```text
QUI
↕
AVEC QUI
↕
POUR QUOI
↕
POUR COMBIEN
↕
PAR QUEL CONTRAT
↕
AVEC QUEL POUVOIR
↕
AVEC QUELLE DONNÉE
↕
AVEC QUEL BÉNÉFICE
```

Mais avec une règle extrêmement stricte :

> **relation ≠ collusion**
> **bénéfice ≠ intention**
> **proximité ≠ conflit d’intérêts**
> **conflit potentiel ≠ corruption**
> **corruption alléguée ≠ corruption établie**

C’est cette combinaison qui rend l’enquête forte :

**suspicion maximale + vocabulaire extrêmement calibré.**

---

# 20. Le principe de double attaque doit devenir invariant

Pour chaque piste `HIGH` :

### attaque accusatoire

> Comment cela pourrait-il cacher quelque chose ?

### attaque innocente

> Quelle explication banale pourrait produire exactement les mêmes observations ?

Puis rechercher des discriminants.

C’est probablement le meilleur remède à la fois :

* contre la naïveté ;
* contre le complotisme ;
* contre la flagornerie institutionnelle ;
* contre notre propre biais.

Je rendrais cette double attaque **obligatoire uniquement pour les items HIGH**.

Pas partout.

KISS.

---

# 21. Ce que doit être le protocole d’écriture, finalement

Il ne doit pas devenir Truth Engine bis.

Il doit remplir quatre fonctions seulement :

| Fonction   | Responsabilité                                |
| ---------- | --------------------------------------------- |
| **HERIT**  | ne rien perdre d’important de Truth Engine    |
| **REOPEN** | renvoyer les gaps matériels à Truth Engine    |
| **DESIGN** | sélectionner et structurer sans blanchir      |
| **VERIFY** | vérifier que l’article reste fidèle au corpus |

C’est le noyau.

Tout le reste est implémentation.

---

# 22. Les invariants V3 que je retiendrais

Je les réduirais à **sept**, pas cinquante :

1. **`SUSPICION_HIGH / EVIDENCE_UNCHANGED`**
2. **`ASSERTION_RIGHT != INVESTIGATION_VALUE != EDITORIAL_VALUE`**
3. **`NO_MATERIAL_FORENSIC_LOSS`**
4. **`HIGH_UNRESOLVED → INVESTIGATE_OR_BLOCK_EXPLICITLY`**
5. **`RELATION != CAUSATION != COLLUSION`**
6. **`EVERY_HIGH_SUSPICION_GETS_BENIGN_FALSIFIER`**
7. **`APPEX_BEFORE_EDITORIAL_FREEZE`**

Je pense que nous tenons là le vrai noyau.

---

# 23. Ce que je supprimerais de V2

C’est important pour le refactoring.

Je ne conserverais pas :

* T3A/T3B/T3C comme trois phases d’état distinctes ;
* T3D/T3E/T3F comme trois phases distinctes ;
* certaines micro-gates séparées alors qu’elles peuvent être des checks d’une gate plus large ;
* multiplication des registres ;
* idée que `PUBLIC_EVIDENCE_FRONTIER` est quasiment terminale ;
* retour à l’enquête uniquement sur besoin probatoire ;
* notion de discovery comme dénominateur ultime de couverture.

Le V2 compte déjà 14 contrats de phase, plusieurs gates, huit schémas CSV et trois templates. 

On peut probablement obtenir **plus de fidélité avec moins de mécanique**.

---

# 24. Architecture V3 que je considère maintenant comme la meilleure candidate

```text
               TRUTH ENGINE
                    │
           investigations × N
                    │
                    ▼
          RECONCILE / PROVE
                    │
                    ▼
            FORENSIC MAP
                    │
          INVESTIGATION QUEUE
                    │
                    ▼
               APPEX GATE
          ┌─────────┴─────────┐
          │                   │
    MORE INVESTIGATION     SATURATED
          │                   │
          └──────→ TE          ▼
                         SYNTHESIZE
                             │
                           DESIGN
                             │
                          MODULES
                             │
                           WEAVE
                             │
                           ATTACK
                             │
                    FORENSIC COVERAGE
                             │
                            FINAL
```

C’est probablement assez.

---

# 25. Le test ultime du protocole

Je modifierais aussi celui que j’ai donné précédemment.

Pas :

> « retrouve-t-on tout dans l’article ? »

Mais :

> **Si un autre enquêteur reçoit uniquement l’article, comprend-il les principales forces visibles et cachées du système, les acteurs matériels, les relations importantes, les anomalies, les soupçons investigués, les hypothèses tuées et les zones où l’enquête a réellement buté ?**

Si oui :

le protocole a transmis l’enquête.

S’il reçoit seulement :

* une thèse raisonnable ;
* quelques statistiques ;
* des précautions méthodologiques ;
* une conclusion équilibrée ;

alors même si tout est exact :

**le protocole a échoué.**

---

## Conclusion de cette passe

Je modifierais donc mon diagnostic précédent sur un point important :

**nous n’avons pas besoin d’ajouter beaucoup de complexité au protocole. Nous devons corriger son modèle mental.**

Le défaut V1 était :

`THESIS_COLLAPSE`.

Le défaut V2 est plus profond :

**`FORENSIC_COLLAPSE`.**

V2 sait maintenant préserver plusieurs *conclusions*.

Il ne sait toujours pas suffisamment préserver **l’enquête qui les a produites**.

La V3 doit donc avoir pour objectif unique :

> **transformer les investigations en article sans perdre leur structure forensique, et rouvrir Truth Engine chaque fois qu’une reconstruction sérieuse du sujet révèle un trou matériel encore investigable.**

C’est beaucoup plus simple, et beaucoup plus proche du véritable but.
