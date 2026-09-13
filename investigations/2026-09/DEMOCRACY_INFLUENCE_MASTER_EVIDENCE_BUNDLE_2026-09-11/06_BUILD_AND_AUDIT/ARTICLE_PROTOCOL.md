---
doc:
  id: ARTICLE_PROTOCOL
  type: protocol
  title: ARTICLE PROTOCOL - Protocole runtime vivant
  status: c2_experiment_no_go_value
foundation:
  ref: FOUNDATION.yml
summary: >
  Contrat d'exécution générique des stories du protocole Article. L'état runtime courant
  et l'historique des fixtures/replays sont externes au contrat exécutable.
history_ref: TRACEABILITY/ARTICLE_PROTOCOL_RUNTIME_HISTORY_C1.md
runtime_state_ref: ARTICLE_PROTOCOL_RUNTIME_*/STATE.json
---

# ARTICLE PROTOCOL - Protocole runtime vivant

**Fondation :** VISION V4.4 + PFD V4.4  
**Statut global :** `EXPERIMENTAL_INCREMENTAL`  
**Méthode :** une story n'entre dans le runtime qu'après écriture, test réel, audit et replay.  
**A0 :** gouvernance et couverture uniquement ; aucune phase runtime A0.

L'état d'une exécution réelle appartient au `STATE.json` du bundle runtime concerné.
Les preuves, anciens `NEXT`, replays et oracles historiques sont conservés dans
`TRACEABILITY/ARTICLE_PROTOCOL_RUNTIME_HISTORY_C1.md`.

## 1. Règles d'exécution

1. Exécuter uniquement les sections marquées `VALIDATED_RUNTIME_FIXTURE` ou, pendant leur test, `CANDIDATE_RUNTIME`.
2. Une EPIC contractuellement `READY` n'est pas pour autant validée en runtime.
3. Une story suit toujours :

```text
SPEC EPIC
-> PROTOCOLE MINIMAL
-> FIXTURE RÉELLE
-> AUDIT DES ÉCARTS
-> RÉPARATION LOCALE SI NÉCESSAIRE
-> REPLAY
-> STORY SUIVANTE
```

4. Les artefacts d'enquête restent la matière autoritative dans leur domaine. Le protocole ne réécrit pas Truth Engine.
5. Les sorties de test n'ajoutent aucune connaissance au corpus sauf décision explicite contraire.
6. Aucun score, registre universel, agent, format ou phase supplémentaire n'est créé sans besoin matériel démontré.
7. Une sélection éditoriale ne peut pas supprimer silencieusement une dimension déclarée matérielle pendant la compréhension. La liste de ces dimensions est propre au sujet ; aucune checklist universelle n'est imposée.
8. Une synthèse multi-investigations doit préserver les relations matérielles qui n'existent que dans le croisement des runs ; `N_INVESTIGATIONS != ONE_BIG_SUMMARY`.
9. Avant prose longue, A3 rend explicites les choix matériels de l'auteur que la prose n'a pas le droit d'inventer : sujet réel, question/thèse, tension, découvertes/mécanismes indispensables, coupes, intention de progression et conclusion probable bornée.
10. A4 construit depuis la décision éditoriale **et** le rendement investigatif préservé. Un article exact, traçable mais presque reproductible par recherche superficielle reste un FAIL produit.

## 2. STORY_CONTROL_DEFAULTS

**Portée :** `A1-S01..A4-S04`. Un default ne s'applique que si la story déclare déjà le contrôle correspondant (`HOLD_IF`, `REPAIR_IF` ou `STOP_WHEN`) ; il n'ajoute aucun état, transition, invariant ou propriétaire. Toute clause spécifique prévaut.

```text
HOLD_DEFAULT :=
  HOLD seulement si un blocage matériel empêche la responsabilité courante ou sa transition explicite
  et ne peut être résolu honnêtement par la matière accessible / récupération locale.
  Absence, incertitude, préférence ou difficulté de rédaction sans blocage matériel
  => limitation / décision / réparation, pas HOLD.

REPAIR_DEFAULT :=
  réparer d'abord le plus petit défaut dans la responsabilité courante, depuis la matière disponible.
  Pas de replay global, réinvestigation ou information nouvelle sauf routage explicite vers le propriétaire compétent, notamment A6.

STOP_DEFAULT :=
  arrêter la story lorsque sa sortie, ses invariants et ses contrôles spécifiques sont satisfaits.
  STOP ou PASS, lorsqu'il est permis par la story, n'autorise que la transition explicitement déclarée ;
  aucune responsabilité aval n'est préemptée.
```

---

# A1 - Matière et contexte

<!-- NODE: PROTOCOL.A1-S01 -->
<!-- TRACE: IMPLEMENTS=STORY.A1-S01 -->
## A1-S01 - Entrée et autorité

### But

Recevoir la matière réellement disponible et borner ce que chaque objet permet d'utiliser ou d'affirmer avant toute réduction de contexte ou compréhension du sujet.

### Invariants

```text
TYPE_D_OBJET != AUTORITÉ_ÉPISTÉMIQUE != CORROBORATION_INDÉPENDANTE
FINAL != COMPLETE != EXHAUSTIVE != CERTIFIED_TRUTH
IDENTITÉ_TECHNIQUE_D_UN_RUN != COUVERTURE_SÉMANTIQUE
SOURCE != PREUVE_AUTOMATIQUE
TRACE_D_EXÉCUTION != PREUVE_DU_FOND
REPRÉSENTATION_DÉRIVÉE != NOUVELLE_AUTORITÉ
RÉPÉTITION_D_UNE_LIGNÉE != CORROBORATION_INDÉPENDANTE
```

### Exécution

Pour la tâche courante :

1. **Inventorier la surface réellement disponible.**
   - Ne jamais reconstruire un fichier, une trace, une source ou une mémoire absente comme si elle avait été reçue.
   - Ne pas déduire la couverture d'un run depuis son nom, slug, dossier, statut ou identifiant.

2. **Qualifier seulement les objets matériels pour la tâche.**
   Déterminer leur fonction par leur contenu et leur provenance, pas par leur seule extension ou leur nom :
   - investigation / état de run ;
   - fait ou objet à statut épistémique ;
   - source ;
   - élément probatoire inspecté pour une affirmation déterminée ;
   - trace ou métadonnée d'exécution ;
   - représentation dérivée : quintessence, état réconcilié, synthèse, mémoire, article antérieur.

3. **Borner l'autorité.**
   - Une investigation `FINAL` vaut pour ce qu'elle établit effectivement sous son contrat ; elle ne certifie ni exhaustivité ni vérité totale du sujet.
   - Une source fournit du contenu ; elle ne prouve une affirmation que dans la mesure où son contenu, son périmètre et sa provenance la soutiennent.
   - Un élément probatoire ne soutient que l'affirmation et la portée qu'il permet réellement d'établir.
   - Une trace établit une exécution, une date ou un chemin lorsqu'elle le montre ; elle ne prouve pas le claim recherché.
   - Une représentation dérivée peut accélérer navigation et récupération ; elle ne remplace pas son origine lorsqu'une question matérielle exige de revenir au substrat disponible.

4. **Préserver les lignées.**
   Une même information présente dans une investigation, une proposition réconciliée, une quintessence, MnemoLite ou un article reste une seule lignée tant qu'une indépendance réelle n'est pas établie.

5. **Résoudre les conflits d'autorité localement.**
   Si une représentation dérivée contredit son origine disponible :
   - revenir à l'origine pertinente ;
   - ne pas arbitrer par fréquence, commodité ou répétition ;
   - conserver l'incertitude si le conflit ne peut pas être fermé.

6. **Dégrader honnêtement la provenance insuffisante.**
   Un objet dont l'origine, le chemin de retour ou l'autorité ne peuvent pas être établis peut orienter une récupération ou une vérification. Il ne devient ni preuve ni corroboration indépendante.

### Sortie minimale

Ne créer aucun registre universel. Conserver uniquement, dans le contexte de travail ou le journal de l'EPIC :

- les surfaces d'entrée réellement utilisées ;
- les limites d'autorité qui changent la tâche ;
- les conflits ou provenances insuffisantes encore matériels ;
- un verdict `PASS` ou `HOLD` pour S01.

### HOLD_IF

une ambiguïté d'autorité ou de provenance empêche matériellement la tâche suivante.

### STOP_WHEN

les objets matériels nécessaires à la tâche suivante ont une autorité bornée et les conflits matériels sont résolus ou explicitement ouverts.

---

<!-- NODE: PROTOCOL.A1-S02 -->
<!-- TRACE: IMPLEMENTS=STORY.A1-S02 -->
## A1-S02 - Réduction contextuelle

### But

Réduire le contexte pour la tâche cognitive courante sans transformer l'exclusion temporaire d'une pièce en suppression, réfutation, irrélevance définitive ou vérité canonique sur le dossier.

### Invariants

```text
AVAILABLE_UNIVERSE != PROJECT_WORKING_VIEW != ROLE_ACTIVE_CONTEXT
EXCLU_DU_CONTEXTE_ACTIF != IRRELEVANT != RÉFUTÉ != SUPPRIMÉ
RÉDUCTION != SÉLECTION_ÉDITORIALE
CONTEXTE_ACTIF_TÂCHE_A != CONTEXTE_ACTIF_TÂCHE_B PAR DÉFAUT
```

`ROLE_ACTIVE_CONTEXT` désigne le contexte actif d'une responsabilité cognitive. Il n'impose aucun agent séparé.

### Exécution

Pour chaque tâche cognitive :

1. **Nommer la tâche courante.**
   La formuler assez précisément pour savoir ce qui peut changer matériellement sa réponse.

2. **Distinguer les trois niveaux sans créer trois nouveaux artefacts obligatoires.**
   - `AVAILABLE_UNIVERSE` : matière actuellement récupérable et potentiellement pertinente ;
   - `PROJECT_WORKING_VIEW` : vue de travail courante, bornée et révisable ;
   - `ROLE_ACTIVE_CONTEXT` : plus petite surface suffisante pour exécuter la tâche courante.

3. **Construire le contexte actif minimal.**
   Inclure ce qui est déjà connu comme nécessaire à la tâche, y compris contradiction, limite, incertitude ou contre-hypothèse matérielle. Ne pas charger une pièce uniquement parce qu'elle existe dans l'univers disponible.

4. **Préserver la récupération.**
   Une pièce exclue reste récupérable tant qu'elle existe dans une vue plus large ou dans l'univers disponible. Il n'est pas nécessaire de journaliser chaque exclusion ; le chemin de retour vers la matière doit simplement rester praticable.

5. **Déclencher une réouverture locale si nécessaire.**
   Si une pièce absente peut raisonnablement changer compréhension, confiance, périmètre, mécanisme, relation, contradiction, gap ou décision ultérieure :
   - formuler la question de récupération ciblée ;
   - rechercher d'abord dans la plus petite vue plus large suffisante ;
   - inspecter seulement les candidats plausibles ;
   - revenir au substrat pertinent lorsque l'autorité ou le détail l'exige.

6. **Recomposer, ne pas gonfler.**
   Ajouter au contexte actif uniquement la substance récupérée qui change matériellement la tâche, avec ses bornes. Ne pas recharger l'univers complet par défaut.

7. **Recomposer au changement de tâche.**
   Un nouveau besoin cognitif peut réutiliser une partie du contexte précédent, mais cette réutilisation doit être justifiée par la nouvelle tâche et non héritée par inertie.

### Sortie minimale

Conserver seulement :

- la tâche courante ;
- la surface active réellement utilisée ;
- les récupérations locales déclenchées et leur motif matériel ;
- les limites encore pertinentes ;
- un verdict `PASS` ou `HOLD` pour S02.

Aucun classement universel des pièces exclues n'est requis.

### HOLD_IF

une pièce connue comme matériellement nécessaire ne peut plus être récupérée et que cette perte empêche la tâche suivante.

### STOP_WHEN

le contexte actif est suffisant sans surcharge manifeste, tout doute matériel détecté est traité par récupération locale ou limitation explicite, et la matière exclue reste récupérable lorsqu'elle existe encore en amont.

---

<!-- NODE: PROTOCOL.A1-S03 -->
<!-- TRACE: IMPLEMENTS=STORY.A1-S03 -->
## A1-S03 - Quintessence

### But

Réduire la plomberie d'exécution afin de libérer du budget cognitif sans perdre ni renforcer ce qui peut changer compréhension, confiance, périmètre, mécanisme, contradiction, gap, décision, narration ou conclusion.

### Invariants

```text
QUINTESSENCE != SOURCE
QUINTESSENCE != INVESTIGATION
QUINTESSENCE != NEW_AUTHORITY
DÉBRUITAGE != APLATISSEMENT
RÉDUCTION != AUGMENTATION_DE_CERTITUDE
DÉTAIL_SUPPRIMÉ != SUBSTANCE_MATÉRIELLE_SUPPRIMÉE
```

### Exécution

Pour chaque investigation :

1. **Fixer l'origine et la question.**
   Conserver l'identité du brut, sa date utile, sa question/périmètre et les limites de scope qui changent l'interprétation.

2. **Inventorier la matière avant réduction.**
   Avant de supprimer quoi que ce soit, relever la substance des éléments susceptibles de changer une propriété matérielle :
   - faits et leur statut ;
   - inférences/hypothèses ;
   - mécanismes/relations/causalités avec leur niveau d'établissement ;
   - contradictions, réfutations et contre-exemples ;
   - gaps, inconnues, connaissances négatives et limites ;
   - conclusion ou décision bornée lorsqu'elle existe.

   Les logs, requêtes, checkpoints, routing, répétitions et détails d'outil ne deviennent pas matériels par leur seule présence.

3. **Débruiter.**
   Retirer la plomberie sans portée cognitive ou probatoire et condenser la formulation des éléments matériels.

4. **Produire la quintessence.**
   La sortie doit permettre à A2 de comprendre ce que l'investigation établit, suggère, contredit et laisse ouvert sans relire le brut par défaut.

5. **Préserver les statuts.**
   Ne jamais transformer silencieusement hypothèse en fait, corrélation en causalité, implication en responsabilité, cas local en prévalence nationale, projection en mesure observée, `NOT_FOUND` en absence.

6. **Contrôler la perte pré/post.**
   Comparer l'inventaire matériel du brut à la quintessence :
   - la substance de chaque élément matériel doit survivre ;
   - un détail peut être omis seulement si son absence ne change pas matériellement compréhension ou décision ;
   - si la substance manque ou si le statut est renforcé, la quintessence est `REPAIR` et doit être corrigée avant usage aval.

7. **Retour ciblé au brut.**
   Lorsqu'un détail omis peut changer une propriété matérielle, revenir à l'origine ciblée. Le retour au brut complète la quintessence ; il ne remplace pas la conservation de la substance matérielle.

8. **Tracer sans créer une nouvelle autorité.**
   Chaque quintessence identifie son fichier source et, pour les éléments structurés, les identifiants ou ancres utiles permettant de revenir au brut.

### Sortie minimale

Conserver seulement ce qui sert la compréhension aval :

- origine ;
- question/périmètre ;
- faits matériels ;
- inférences/hypothèses ;
- mécanismes/relations ;
- contradictions/contre-exemples ;
- gaps/limites/connaissances négatives ;
- conclusion bornée si elle existe ;
- trace vers le brut ;
- verdict `PASS`, `REPAIR` ou `HOLD`.

Aucun format littéraire, longueur cible, score de compression ou schéma EPI universel n'est imposé.

### REPAIR_IF

la quintessence perd ou renforce un élément matériel alors que le brut est disponible.

### HOLD_IF

une matière matérielle nécessaire est identifiée mais que son origine ne peut plus être inspectée suffisamment pour produire une quintessence honnête.

### STOP_WHEN

le contrôle pré/post ne détecte plus de perte matérielle ni d'augmentation silencieuse de certitude et la trace vers le brut reste praticable.
---

<!-- NODE: PROTOCOL.A1-S04 -->
<!-- TRACE: IMPLEMENTS=STORY.A1-S04 -->
## A1-S04 - Mémoire et provenance

### But

Utiliser la mémoire pour retrouver et relier plus vite sans transformer un objet mémorisé, une répétition sémantique ou une représentation dérivée en preuve supplémentaire.

### Invariants

```text
MEMORY != EVIDENCE
MEMORY_ID != ORIGIN
MEMORY_TYPE != EPISTEMIC_STATUS
RETRIEVED_MEMORY != INDEPENDENT_CORROBORATION
MEMORY_CAN_SEED_DISCOVERY
MEMORY_CANNOT_CONFIRM_ITSELF
RETRIEVED != CURRENT
EDITORIAL_MEMORY != VERIFIED_FACT_MEMORY
INDÉPENDANCE_NON_ÉTABLIE != CORROBORATION_INDÉPENDANTE
```

### Exécution

Pour tout objet mémoire matériel utilisé par le travail courant :

1. **Identifier le type.**
   Distinguer mémoire factuelle, mémoire éditoriale, quintessence ou autre représentation dérivée. Le type n'attribue aucune autorité par lui-même.

2. **Exiger le minimum de provenance.**
   Le minimum est :
   - type ;
   - origine ;
   - chemin de retour vers l'artefact pertinent ;
   - statut épistémique lorsqu'il s'applique ;
   - date/version lorsqu'elle peut changer matériellement l'usage.

   Un UUID ou identifiant mémoire est un localisateur, pas une origine.

3. **Dégrader plutôt que fabriquer.**
   Si une information requise manque, marquer l'usage `DEGRADED` et revenir aux artefacts disponibles. Ne jamais reconstruire silencieusement provenance, statut, version ou indépendance.

4. **Réduire les représentations à leur lignée connue.**
   Investigation, quintessence, objet mémoire et ancien article dérivés d'une même origine restent une lignée connue. Leur multiplication n'augmente pas le nombre de corroborations indépendantes.

5. **Ne jamais présumer l'indépendance.**
   Une corroboration indépendante n'est comptée que si son indépendance est établie par une provenance distincte pertinente. Sinon : `INDÉPENDANCE_NON_ÉTABLIE`.

6. **Contrôler l'actualité.**
   Avant d'utiliser une mémoire comme état courant, confronter sa date/version aux corrections, réouvertures ou supersessions connues. Une ancienne mémoire reste historique si une couche ultérieure la corrige ou la borne.

7. **Retourner à la preuve lorsque le claim l'exige.**
   La mémoire sert à retrouver. Une affirmation matérielle doit revenir à l'artefact d'origine puis, lorsque nécessaire, à la source ou à l'élément probatoire inspecté.

8. **Tolérer MnemoLite dégradé.**
   Si MnemoLite live est indisponible :
   - utiliser les artefacts inspectables ;
   - signaler la perte de continuité si elle est matérielle ;
   - ne créer aucun faux objet mémoire ;
   - bloquer seulement si cette perte rend réellement impossible une décision matérielle.

### Sortie minimale

Conserver seulement :
- objet ou référence mémoire réellement observé ;
- type ;
- origine et chemin de retour disponibles ;
- statut épistémique si applicable ;
- date/version utile ;
- lignée connue ou indépendance non établie ;
- statut d'actualité ;
- mode `MEMORY` ou `DEGRADED_ARTIFACT_FALLBACK` ;
- verdict `PASS`, `DEGRADED_PASS` ou `HOLD`.

Aucun graphe de provenance universel, score d'autorité, score d'indépendance ou moteur de résolution de version n'est imposé.

### HOLD_IF

la perte de mémoire/provenance empêche une décision matérielle et qu'aucun artefact disponible ne permet de la prendre honnêtement.

### STOP_WHEN

les objets mémoire utilisés ne gagnent aucune autorité par répétition, que les chemins de retour nécessaires sont disponibles ou explicitement dégradés, que l'actualité n'est pas présumée et que MnemoLite indisponible n'entraîne ni fabrication ni blocage injustifié.


<!-- NODE: PROTOCOL.A2-S01 -->
<!-- TRACE: IMPLEMENTS=STORY.A2-S01 -->
## A2-S01 - Compréhension de travail suffisante

### But

Construire un noyau de compréhension explicatif, borné et révisable à partir de la matière préparée par A1, sans confondre compréhension, accumulation de claims ou sélection éditoriale.

### Invariants

```text
COMPRENDRE != ACCUMULER_DES_CLAIMS
COMPRENDRE != RÉSUMER_RUN_PAR_RUN
WORKING_UNDERSTANDING != CANON_DU_SUJET
SUFFICIENT_UNDERSTANDING != SUBJECT_EXHAUSTED
HYPOTHÈSE_ANALYTIQUE != THÈSE_ÉDITORIALE
RELATION_EXPLICATIVE != CAUSALITÉ_PAR_DÉFAUT
```

### Entrée par défaut

A2-S01 consomme d'abord les quintessences et métadonnées de provenance préparées par A1.

```text
50 QUINTESSENCES
-> COMPRÉHENSION

50 BRUTS
-> PAS DE RELECTURE PAR DÉFAUT
```

Un retour au brut reste autorisé uniquement lorsqu'un détail matériel omis, une contradiction ou une portée ne peut pas être résolu honnêtement depuis la matière active.

### Exécution

1. **Fixer le périmètre actif.**
   Identifier la matière effectivement lue, sa date utile et les limites de couverture. Une absence de matière reste une limite, jamais une invitation à compléter par connaissance générique.

2. **Raisonner en unités sémantiques, pas en frontières de runs.**
   Relier les investigations qui portent sur un même mécanisme, une même contradiction ou une même question, même si leurs noms et périmètres techniques diffèrent.

3. **Formuler des assertions de compréhension.**
   Une assertion de compréhension explique une propriété du sujet ou une relation matérielle. Elle ne devient ni claim supplémentaire ni proposition éditoriale.

4. **Conserver le statut.**
   Distinguer, lorsque matériel, ce qui est établi, borné, inféré, hypothétique, contradictoire ou inconnu. Ne jamais promouvoir une projection, corrélation, implication ou annonce future en fait plus fort.

5. **Challenger chaque assertion matérielle avant admission.**
   Pour chaque assertion de compréhension :

   ```text
   SUPPORT
   -> CHALLENGE / CONTRE-EXEMPLE / LIMITE / ACTUALISATION
   -> STATUT
   ```

   Le challenge porte sur l'ensemble du contexte actif pertinent, pas seulement sur les éléments qui soutiennent l'explication dominante. Une réouverture plus récente peut borner ou superseder une formulation historique.

6. **Préserver les hypothèses concurrentes.**
   Une hypothèse analytique matériellement viable reste visible même si elle affaiblit une explication plus spectaculaire. A2-S01 peut comparer plusieurs mécanismes sans choisir l'angle de l'article.

7. **Rendre les inconnues explicites.**
   Un gap matériel, une absence de série nationale, une causalité non isolée ou une portée locale restent dans la compréhension. `NON_ÉTABLI` ne devient pas `ABSENT`.

8. **Tracer vers les quintessences.**
   Chaque assertion matérielle conserve des références suffisantes vers les quintessences qui la soutiennent et celles qui la bornent. La quintessence reste une représentation dérivée, jamais une nouvelle preuve.

9. **Tracer les retours au brut.**
   Si un retour ciblé au brut devient nécessaire, enregistrer son motif. Zéro retour est légitime si les quintessences suffisent à la responsabilité S01.

### Sortie minimale

La sortie S01 doit rendre observables :

- périmètre et matière effectivement lus ;
- assertions de compréhension reliées sémantiquement ;
- supports et challenges matériels ;
- statuts et limites ;
- hypothèses analytiques concurrentes ;
- gaps encore ouverts ;
- absence de sélection éditoriale ;
- nombre de retours ciblés au brut.

Aucun score de compréhension, graphe obligatoire, formulaire universel, quota d'assertions ou taxonomie exhaustive n'est imposé.

### REPAIR_IF

une assertion de compréhension :

- repose seulement sur ses supports sans examen des contradictions matérielles disponibles ;
- renforce silencieusement un statut ;
- efface une contre-hypothèse matériellement viable ;
- transforme les frontières des runs en structure du sujet ;
- sélectionne déjà un angle éditorial.



### HOLD_IF

la compréhension nécessaire à la poursuite d'A2 dépend d'une information matérielle inaccessible que la matière active et la récupération ciblée ne permettent pas de résoudre honnêtement.

### STOP_WHEN

la compréhension est suffisamment formée pour poursuivre A2 : elle relie la matière, conserve les statuts et contre-hypothèses, rend les gaps visibles et reste non éditoriale.

<!-- NODE: PROTOCOL.A2-S02 -->
<!-- TRACE: IMPLEMENTS=STORY.A2-S02 -->
## A2-S02 - Reconstruction de la structure matérielle

### But

Reconstruire les dimensions du sujet dont l'absence ou la mauvaise compréhension pourrait changer matériellement l'explication courante, sans transformer la reconstruction en formulaire universel, graphe de connaissance ou plan d'article.

### Invariants

```text
RECONSTRUCTION_DU_SUJET != LISTE_DE_CONTRÔLE_UNIVERSELLE
FRONTIÈRES_DES_RUNS != FRONTIÈRES_DU_SUJET
RELATION_OBSERVÉE != CAUSALITÉ
SÉQUENCE_TEMPORELLE != CAUSALITÉ
IMPLICATION_D_UN_ACTEUR != RESPONSABILITÉ_ÉTABLIE
FLUX_OBSERVÉ != EFFET_DÉMONTRÉ
NON_TROUVÉ_DANS_LA_MATIÈRE != ABSENT
PLUS_DE_STRUCTURE != MEILLEURE_COMPRÉHENSION_PAR_DÉFAUT
```

### Entrée par défaut

S02 consomme :

- le noyau de compréhension A2-S01 ;
- les quintessences A1-S03 nécessaires à la reconstruction ;
- les métadonnées de provenance A1 utiles.

Les investigations brutes restent récupérables, mais ne sont pas rechargées par défaut.

### Exécution

1. **Fixer la matière active.**
   Enregistrer le noyau S01 et les quintessences effectivement consultées. Aucun élément absent ne doit être complété par connaissance générique.

2. **Tester la matérialité de chaque dimension candidate.**
   Pour toute dimension envisagée, poser :

   ```text
   SI_DIMENSION_ABSENTE_OU_MAL_COMPRISE
   -> EXPLICATION_PEUT_CHANGER_MATÉRIELLEMENT ?
   ```

   Si non, ne pas la documenter pour remplir une case. Si oui, la reconstruire au niveau nécessaire.

3. **Reconstituer le fonctionnement normal lorsque pertinent.**
   Établir la situation de référence avant d'interpréter exception, anomalie, controverse ou rupture. Ne pas transformer un cas spectaculaire en fonctionnement normal.

4. **Conserver seulement l'histoire utile.**
   Garder les antécédents qui changent le sens de l'état courant. Ne pas produire une chronologie exhaustive sans gain explicatif.

5. **Séparer acteurs, rôles et responsabilités.**
   Identifier qui décide, finance, exécute, fournit, contrôle, subit ou observe lorsque matériel. La présence, la proximité ou l'intérêt d'un acteur ne suffisent jamais à établir sa responsabilité.

6. **Reconstruire règles et contraintes sans leur attribuer automatiquement un effet.**
   Une règle, annonce, projet, règlement ou norme doit rester à son niveau réel : existence, application, portée et effet sont des questions distinctes.

7. **Suivre les flux utiles sans convertir le flux en effet.**
   Argent, déchets, données, décisions, incitations ou autres ressources peuvent être reliés lorsque cela change l'explication. Leur circulation ne démontre pas par elle-même un gagnant net, une causalité ou une conséquence générale.

8. **Qualifier chaque relation matérielle avant de l'utiliser.**
   Toute relation qui porte l'explication doit conserver son niveau autorisé : descriptive, temporelle, institutionnelle, fonctionnelle, financière, hypothétique ou causale lorsque la causalité est réellement établie.

   Une relation matérielle est refusée ou réparée si sa formulation ajoute silencieusement :
   - causalité ;
   - responsabilité ;
   - prévalence ;
   - universalité ;
   - effet net ;
   - actualité juridique ou factuelle.

9. **Traverser les frontières de runs.**
   Fusionner sémantiquement deux runs qui décrivent un même mécanisme lorsque pertinent, ou séparer plusieurs mécanismes contenus dans un même run. Conserver les références d'origine.

10. **Maintenir contradictions et contre-hypothèses.**
    Une reconstruction n'est pas correcte si elle devient cohérente uniquement en supprimant les éléments qui la fragilisent. Les explications concurrentes matériellement viables restent visibles.

11. **Préserver exactement la connaissance négative.**

    ```text
    NON_ÉTABLI
    NON_TROUVÉ_DANS_LA_MATIÈRE_DISPONIBLE
    RÉFUTÉ
    ABSENT
    INCONNU
    ```

    restent distincts. Une recherche sans résultat n'établit pas l'absence du phénomène.

12. **Limiter la profondeur.**
    Approfondir seulement tant qu'une dimension supplémentaire peut changer matériellement l'explication. Aucun annuaire exhaustif d'acteurs, règles, contrats, flux ou dates n'est requis.

13. **Tracer les retours au brut.**
    Si une relation ou portée matérielle ne peut pas être calibrée honnêtement depuis les quintessences, effectuer un retour ciblé et le consigner. Zéro retour est légitime lorsque la matière A1 suffit.

### Sortie minimale

S02 rend observables :

- dimensions considérées et décision de matérialité ;
- fonctionnement normal et histoire utile lorsqu'ils sont matériels ;
- acteurs/rôles sans responsabilité inventée ;
- règles/contraintes ;
- flux utiles ;
- mécanismes et relations avec leur niveau autorisé ;
- contradictions/refutations ;
- contre-hypothèses ;
- lacunes et connaissance négative ;
- références vers les quintessences ;
- nombre de retours ciblés au brut.

Aucun graphe universel, score de causalité, score de responsabilité, ontologie formelle, quota de dimensions ou plan narratif n'est imposé.

### REPAIR_IF

la reconstruction :

- remplit des dimensions sans matérialité démontrée ;
- transforme relation ou séquence en causalité ;
- transforme implication en responsabilité ;
- transforme flux en effet démontré ;
- transforme `NON_TROUVÉ` en `ABSENT` ;
- efface contradiction ou contre-hypothèse viable ;
- épouse les frontières techniques des runs ;
- commence déjà la narration ou la sélection éditoriale.



### HOLD_IF

une dimension matérielle nécessaire à la compréhension ne peut pas être reconstruite honnêtement depuis la matière active ni par récupération ciblée.

### STOP_WHEN

les dimensions qui changent matériellement l'explication sont reconstruites au niveau nécessaire, les relations restent calibrées, contradictions et inconnues sont visibles, et une structure supplémentaire n'apporterait pas de gain de compréhension matériel identifié.

<!-- NODE: PROTOCOL.A2-S03 -->
<!-- TRACE: IMPLEMENTS=STORY.A2-S03 -->
## A2-S03 - Challenge de suffisance et besoins d'information

### But

Mettre la compréhension A2-S01/S02 sous contradiction avant A3, distinguer ce qui est déjà résolu, ce qui exige une récupération locale et ce qui nécessiterait réellement une information nouvelle, sans transformer une absence de résultat en inexistence ni dupliquer l'autorité A6.

### Invariants

```text
CHALLENGE_DE_COMPRÉHENSION != PREUVE_D_EXHAUSTIVITÉ
NON_TROUVÉ / NON_RÉSOLU != ABSENT != N_EXISTE_PAS
MATIÈRE_ACTIVE_INSUFFISANTE != INFORMATION_INEXISTANTE
RÉCUPÉRATION_LOCALE != RÉINVESTIGATION
BESOIN_D_INFORMATION_NOUVELLE != AUTORISATION_A6
GAP_EXPLICITE != ÉCHEC_AUTOMATIQUE_D_A2
```

### Entrée par défaut

S03 consomme :

- le noyau de compréhension A2-S01 ;
- la structure matérielle A2-S02 ;
- les 50 quintessences A1-S03 et la provenance A1 utile ;
- les investigations brutes uniquement par récupération ciblée motivée.

Aucun rechargement global des 50 bruts n'est autorisé par défaut.

### Exécution

1. **Inventorier les fragilités plausibles.**
   Partir des gaps, contradictions, inconnues, relations bornées et actualités susceptibles de changer matériellement la compréhension ou la capacité d'A3 à l'évaluer honnêtement.

2. **Tester la matérialité.**
   Pour chaque besoin candidat :

   ```text
   SI_CORRIGÉ_OU_REQUALIFIÉ
   -> COMPRÉHENSION / CONFIANCE / PÉRIMÈTRE / MÉCANISME / CONTRE-HYPOTHÈSE / LIMITE
      PEUT_CHANGER_MATÉRIELLEMENT ?
   ```

   Si non, le besoin ne déclenche aucune réouverture.

3. **Chercher d'abord dans la matière active.**
   Une information déjà présente mais mal reliée entraîne une correction locale de compréhension, jamais un nouveau run.

4. **Récupérer localement avant de demander du nouveau.**
   Si la matière active ne suffit pas, ouvrir la plus petite surface disponible capable de résoudre l'ambiguïté : quintessence ciblée, provenance A1, puis brut précis si nécessaire. Tracer motif, cible et résultat.

5. **Préserver exactement la connaissance négative.**

   ```text
   NON_TROUVÉ_DANS_UN_RUN
   NON_TROUVÉ_DANS_LA_MATIÈRE_DISPONIBLE
   NON_RÉSOLU
   INCONNU
   ABSENT
   RÉFUTÉ
   ```

   restent distincts. Une recherche saturée dans un run ne prouve pas que l'objet n'existe pas hors de ce run.

6. **Classer le besoin après récupération.**
   Un besoin matériel aboutit à l'une des situations suivantes, sans imposer de taxonomie universelle :
   - compréhension corrigée depuis la matière disponible ;
   - limite explicite suffisamment bornée pour poursuivre A2 ;
   - information nouvelle réellement nécessaire pour une compréhension ou décision aval matérielle.

7. **Handoff A6 seulement si nécessaire.**
   Si une information nouvelle est réellement nécessaire, A2 transmet uniquement :
   - la question minimale ;
   - pourquoi elle est matérielle ;
   - le gain d'information plausible ;
   - la compréhension ou décision aval susceptible de changer.

   ```text
   A2_IDENTIFIE_LE_BESOIN
   A6_SEUL_AUTORISE_ET_CIBLE_UN_NOUVEAU_RUN
   ```

8. **Préférer la limite honnête au BACK opportuniste.**
   Un gap visible et non bloquant reste ouvert. Ne pas réinvestiguer pour obtenir une impression de complétude.

9. **Réparer localement.**
   Un défaut borné ne déclenche qu'un replay des relations, hypothèses ou limites affectées. Replay global seulement si une dépendance matérielle transversale est démontrée.

10. **Interdire la fermeture éditoriale.**
    Aucune thèse ou angle d'article ne peut être utilisé pour éliminer une contradiction ou décider qu'un gap est sans importance. A3 recevra les limites telles quelles.

### Sortie minimale

S03 rend observables :

- besoins challengés et matérialité ;
- matière active examinée ;
- récupérations locales réellement effectuées ;
- statut exact des connaissances négatives ;
- limites non bloquantes ;
- éventuels besoins d'information nouvelle transmis comme candidats à A6 ;
- absence d'autorisation A6 par A2 ;
- décision de suffisance A2 pour passer ou non à A3.

Aucun score de complétude, quota de gaps, replay global, recherche web automatique ou format universel de BACK n'est imposé.

### REPAIR_IF


- transforme `NON_TROUVÉ` ou `NON_RÉSOLU` en `ABSENT` / `N_EXISTE_PAS` ;
- demande une information nouvelle avant récupération locale de la matière disponible ;
- efface un gap pour rendre A2 artificiellement complète ;
- lance ou autorise elle-même une réinvestigation ;
- déclenche un replay global sans dépendance matérielle démontrée ;
- utilise un choix éditorial pour fermer la compréhension.

### HOLD_IF

un défaut matériel identifié empêche une compréhension honnête ou l'évaluation par A3 et qu'il reste non résolu après récupération locale, avec information nouvelle nécessaire. Le besoin est alors transmis à A6 ; A2 ne le résout pas par invention.

### STOP_WHEN

tous les défauts matériels identifiés ont été corrigés, bornés comme limites explicites ou transmis comme besoins d'information nouvelle ; qu'aucun `NON_TROUVÉ` n'a été transformé en inexistence ; et que la compréhension peut être remise à A3 sans prétention d'exhaustivité.


---

# A3 - Décision éditoriale

<!-- NODE: PROTOCOL.A3-S01 -->
<!-- TRACE: IMPLEMENTS=STORY.A3-S01 -->
## A3-S01 - Identifier la contribution éditoriale candidate

### But

Identifier, à partir de la compréhension bornée livrée par A2, un ou plusieurs gains éditoriaux plausibles qui dépendent réellement du rendement de l'enquête, sans encore confirmer leur nouveauté par le corpus publié, décider la forme, fixer le contrat éditorial ou écrire l'article.

### Invariants

```text
CONTRIBUTION != VOLUME_D_ENQUÊTE
IMPORTANCE_DU_SUJET != IMPORTANCE_DE_LA_CONTRIBUTION
REFORMULATION != NOUVEAUTÉ
NOUVEAUTÉ_CANDIDATE != NOUVEAUTÉ_CORPUS_CONFIRMÉE
RÉCIT_PLUS_FORT != POUVOIR_EXPLICATIF
CONTRIBUTION_CANDIDATE != THÈSE_FINALE
A3-S01 != DÉCISION_DE_FORME
A3-S01 != PUBLISH
```

### Entrée par défaut

S01 consomme la compréhension A2 déjà construite et challengée :

- noyau de compréhension A2-S01 ;
- structure matérielle A2-S02 ;
- challenge de suffisance A2-S03 ;
- besoins et candidats A6 conditionnels utiles pour borner ce qui ne peut pas être promis.

Les 50 quintessences et les bruts restent récupérables, mais ne sont pas relus par défaut si la compréhension A2 suffit à identifier le delta éditorial.

### Exécution

1. **Faire émerger les deltas plausibles.**
   Chercher ce que la compréhension A2 permettrait au lecteur de comprendre différemment, avec plus de précision ou avec une hiérarchie explicative meilleure. Ne pas partir d'un titre, d'une indignation ou d'une forme souhaitée.

2. **Appliquer le contrôle d'admission de contribution.**
   Avant d'admettre un candidat, rendre explicites quatre propriétés :

   ```text
   CANDIDAT
   -> DELTA_IDENTIFIABLE
   -> DÉPENDANCE_AU_RENDEMENT_D_ENQUÊTE
   -> BORNES_HÉRITÉES_D_A2
   -> NOUVEAUTÉ = CANDIDATE_SEULEMENT
   ```

   Si l'une manque, le candidat reste faible, incertain ou doit être réparé. Il n'est jamais renforcé pour obtenir un PASS.

3. **Faire le contrefactuel anti-généricité.**

   ```text
   RETIRER_LES_APPORTS_SPÉCIFIQUES_D_A2
   -> LE_GAIN_CENTRAL_SURVIT_PRESQUE_INCHANGÉ ?
   ```

   Si oui, le candidat dépend trop peu du travail d'enquête. Il peut rester exact ou intéressant, mais sa contribution éditoriale est faible au sens de S01.

4. **Raisonner les trois dimensions sans score.**
   Pour chaque candidat :
   - **nouveauté candidate** : quel type de delta est plausible, sans le déclarer inédit dans le corpus publié ;
   - **importance de la contribution** : ce que ce delta change matériellement dans la compréhension, la confiance, la causalité, la responsabilité, le périmètre ou les inconnues ;
   - **pouvoir explicatif** : ce qu'il aide à relier, expliquer ou borner sans dépasser les statuts A2.

   Aucune pondération, note ou total n'est calculé.

5. **Conserver les corrections et contre-hypothèses qui conditionnent le candidat.**
   Un candidat n'est pas recevable s'il exige de supprimer une borne A2, de promouvoir une hypothèse, ou d'effacer une explication concurrente matériellement viable.

6. **Tester le rendement de l'enquête.**
   Le gain central doit dépendre d'éléments que l'enquête a réellement apportés ou requalifiés : relation, contradiction, correction, limitation, données, mécanisme ou synthèse. Un texte générique sur un thème grave ne suffit pas.

7. **Accepter plusieurs candidats ou un candidat faible.**
   Plusieurs deltas matériellement différents peuvent rester ouverts. S01 ne crée ni classement, ni score, ni gagnant obligatoire. Une dimension faible ou incertaine reste telle quelle.

8. **Interdire la confirmation de nouveauté.**
   Aucun candidat ne devient `NOUVEAUTÉ_CORPUS_CONFIRMÉE` avant A3-S02. S01 ne peut pas conclure « jamais publié » ou « inédit pour les lecteurs » sans comparaison au corpus éditorial.

9. **Interdire les décisions aval.**
   S01 ne décide ni forme longue/courte, ni question ou thèse finale, ni `PUBLISH`, ni `NO_ARTICLE`, ni `MORE_INVESTIGATION`. Les candidats A6 transmis par A2 restent conditionnels tant qu'une contribution ultérieure n'en dépend pas matériellement.

### Sortie minimale

Pour chaque candidat retenu ou conservé comme incertain, rendre observable :

- le delta éditorial plausible ;
- les éléments A2 dont il dépend ;
- nouveauté candidate, importance et pouvoir explicatif raisonnés qualitativement ;
- les bornes qui empêchent la sur-affirmation ;
- le résultat du contrefactuel anti-généricité ;
- le statut `CANDIDATE`, jamais `CONFIRMED` en S01.

Aucun plan, titre, longueur, score, persona ou classement obligatoire n'est ajouté.

### REPAIR_IF


- confond volume d'enquête ou gravité du sujet avec contribution ;
- admet un candidat générique qui ne dépend pas matériellement du rendement de l'enquête ;
- confirme la nouveauté avant S02 ;
- augmente causalité, responsabilité, prévalence, effet net ou actualité par rapport à A2 ;
- efface une contre-hypothèse nécessaire au candidat ;
- décide déjà une forme, une thèse finale, `PUBLISH` ou une réinvestigation.

### HOLD_IF

la compréhension A2 est insuffisante pour identifier honnêtement le delta d'un candidat matériel et qu'une récupération locale ou un besoin d'information est réellement nécessaire. Une contribution faible n'est pas un HOLD.

### STOP_WHEN

les candidats plausibles sont explicités avec leur delta, leur dépendance au rendement d'enquête, leurs bornes et leur statut de nouveauté candidate, sans promotion épistémique.

---

<!-- NODE: PROTOCOL.A3-S02 -->
<!-- TRACE: IMPLEMENTS=STORY.A3-S02 -->
## A3-S02 - Comparer au corpus publié

### But

Confronter les contributions candidates S01 à ce qui a déjà été publié afin de distinguer nouveauté relative, continuité cumulative, mise à jour, correction ou répétition, sans utiliser le corpus éditorial comme preuve du fond ni fabriquer une exhaustivité du corpus.

### Invariants

```text
CORPUS SUBSTACK = MÉMOIRE ÉDITORIALE != PREUVE AUTOMATIQUE DU FOND
MÊME SUJET != MÊME CONTRIBUTION
MOTS DIFFÉRENTS != NOUVEAUTÉ
RESSEMBLANCE LEXICALE != RÉPÉTITION
ARTICLE ANTÉRIEUR = PREUVE DE PUBLICATION != PREUVE DU FAIT PUBLIÉ
NON_RETROUVÉ_DANS_LE_CORPUS_INSPECTÉ != JAMAIS_PUBLIÉ
RÉUTILISER DU CONTEXTE != RÉPÉTER LE GAIN CENTRAL
A3-S02 != DÉCISION_DE_FORME
```

### Entrée par défaut

S02 consomme :

- les candidats A3-S01 ;
- la plus petite surface de mémoire éditoriale capable de tester leur gain central ;
- l'index des publications et/ou un atlas sémantique dérivé du corpus lorsqu'ils suffisent à comparer la substance ;
- les textes antérieurs ciblés seulement si le résumé éditorial disponible ne suffit pas à trancher la relation.

Un artefact de travail non établi comme publication n'entre pas dans le corpus publié par simple ressemblance.

### Exécution

1. **Borner la surface de comparaison.**
   Identifier la mémoire éditoriale effectivement accessible : index, corpus, atlas, article ou version. Conserver toute anomalie de couverture, de version ou de comptage pouvant changer le verdict.

2. **Chercher par substance avant de conclure par mots.**
   Les titres, mots-clés ou recherches lexicales servent au rappel, jamais au verdict. Une absence lexicale peut déclencher une recherche sémantique ; elle ne prouve pas la nouveauté.

3. **Comparer le gain central.**
   Pour chaque candidat :

   ```text
   CANDIDAT S01
   -> SURFACE ÉDITORIALE PERTINENTE
   -> GAIN CENTRAL ANTÉRIEUR RETROUVÉ ?
   -> DELTA MATÉRIEL ACTUEL ?
   -> RELATION ÉDITORIALE BORNÉE
   ```

   La relation porte sur ce que le lecteur pouvait déjà comprendre, non sur l'identité des formulations.

4. **Distinguer répétition et continuité.**
   - même gain central sans nouveau delta matériel : répétition possible ;
   - base déjà publiée + nouveau mécanisme, correction, donnée, portée ou relation : continuité cumulative ;
   - état des connaissances modifié : mise à jour ;
   - ancienne certitude bornée ou réfutée : correction/contradiction ;
   - gain central non retrouvé après une surface suffisante : nouveauté relative au corpus inspecté.

   Ces relations sont des descriptions de travail, pas une taxonomie obligatoire.

5. **Appliquer le contrefactuel de delta.**
   Si le nouveau candidat retire son delta sectoriel ou explicatif et redevient presque identique au gain déjà publié, sa nouveauté est faible ou nulle. Si le delta change matériellement ce que le lecteur comprend, une continuité cumulative reste possible.

6. **Séparer publication et vérité.**
   Une ancienne publication peut établir qu'une idée, une conclusion ou un mécanisme a déjà été publié. Elle ne confirme jamais par répétition le fait, la causalité ou la responsabilité qu'elle affirme. Toute question probatoire reste rattachée à A1/A2 et aux preuves de l'enquête.

7. **Élargir localement si le verdict peut changer.**
   Si l'atlas ou l'index laisse une ambiguïté matérielle, inspecter les articles candidats les plus proches. Ne pas relire le corpus complet par défaut.

8. **Préserver l'incertitude de corpus.**
   Un corpus incomplet, mal indexé ou versionné produit une borne explicite. Il ne produit ni faux inédit, ni BACK Truth Engine. Un problème de mémoire éditoriale n'est pas un gap probatoire sur le sujet.

9. **Requalifier sans décider la forme.**
   S02 transmet à S03 les candidats avec leur relation au corpus, leur delta restant et leurs limites. Elle ne choisit ni question/thèse finale, ni longueur, ni `PUBLISH`, ni `NO_ARTICLE`, ni `MORE_INVESTIGATION`.

### Sortie minimale

Pour chaque candidat matériel :

- surface éditoriale réellement inspectée ;
- gain antérieur pertinent retrouvé ou non ;
- delta actuel ;
- relation éditoriale bornée ;
- limite de couverture/version ;
- rappel explicite que le corpus n'est pas preuve du fond.

Aucun score de similarité, seuil lexical, nombre minimal d'articles ou classement algorithmique n'est requis.

### REPAIR_IF


- déclare un inédit depuis un titre ou une absence de mot-clé ;
- déclare un doublon depuis une simple ressemblance lexicale ;
- compte une ancienne publication comme corroboration du fond ;
- transforme `NON_RETROUVÉ` en `JAMAIS_PUBLIÉ` ;
- ignore une anomalie de corpus capable de changer le verdict ;
- relit tout le corpus sans besoin matériel ;
- décide déjà la forme ou une réinvestigation.

### HOLD_IF

la relation au corpus est matériellement nécessaire pour la suite et que la mémoire éditoriale accessible est trop insuffisante pour distinguer honnêtement répétition, continuité ou nouveauté. L'incertitude peut aussi être transmise à S03/S04 lorsqu'elle ne bloque pas la décision.

### STOP_WHEN

le gain central de chaque candidat a été comparé sur une surface éditoriale suffisante et bornée, le delta restant est explicite et aucune publication antérieure n'a été blanchie en preuve du fond.

---

<!-- NODE: PROTOCOL.A3-S03 -->
<!-- TRACE: IMPLEMENTS=STORY.A3-S03 -->
## A3-S03 - Établir le contrat éditorial

### But

Transformer les contributions requalifiées S01-S02 en **une promesse éditoriale minimale, honnête et bornée**, ou constater explicitement qu'aucun contrat honnête n'est tenable, sans décider la forme ni commencer la rédaction.

```text
CONTRAT ÉDITORIAL != PLAN != PROSE != DÉCISION DE FORME
CONTRIBUTION NON NULLE != THÈSE AFFIRMATIVE OBLIGATOIRE
CONTRIBUTION CUMULATIVE != PREUVE INDÉPENDANTE
```

### Entrée par défaut

S03 consomme :

- les contributions requalifiées de S02 ;
- leurs bornes A2 et dépendances au rendement de l'enquête ;
- les gaps ou contre-hypothèses qui peuvent changer matériellement la promesse.

S03 ne recharge ni les 50 quintessences ni les investigations brutes par défaut.

### Garde de disposition des dimensions matérielles

A3 reçoit désormais, avec la compréhension A2, le handoff des dimensions que le sujet courant a déclarées matérielles.

A3 doit disposer chaque dimension avant de pouvoir considérer un futur contrat éditorial comme compatible avec la compréhension amont :

```text
DIMENSION MATÉRIELLE A2
-> PRESERVE_IN_EXPLANATORY_FLOOR
   OU
-> EXCLUDE_WITH_MATERIAL_JUSTIFICATION
```

`PRESERVE_IN_EXPLANATORY_FLOOR` ne signifie ni section dédiée, ni poids égal, ni nouveauté, ni centralité éditoriale. Cela signifie seulement que la production doit conserver assez de cette dimension pour que son omission ne déforme pas l'objet compris en A2.

`EXCLUDE_WITH_MATERIAL_JUSTIFICATION` exige une raison explicite montrant que l'exclusion ne change pas matériellement la compréhension de l'objet ou de la contribution retenue.

### Invariants de sélection R2/R3

```text
EDITORIAL_CORE != EXPLANATORY_FLOOR
CONTRIBUTION_SELECTION != PERMISSION_TO_DROP_MATERIAL_UNDERSTANDING
METHOD_ALREADY_PUBLISHED != DIMENSION_EXPLICATIVE_DISPENSABLE
PRÉSENCE_LEXICALE != SURVIE_EXPLICATIVE
```

La contribution éditoriale peut rester étroite. Le plancher explicatif reste sujet-spécifique et dérive exclusivement de la matérialité établie en A2.

### Exécution

1. **Tester la tenabilité avant d'écrire un contrat.**

   ```text
   CONTRIBUTIONS REQUALIFIÉES
   -> PROMESSE CENTRALE COHÉRENTE SANS INFLATION ?
      OUI -> CONTRAT BORNÉ
      NON -> NON_TENABLE -> S04
   ```

   Une contribution survivante, cumulative ou étroite n'a aucune obligation de devenir une thèse autonome.

2. **Choisir le niveau exact de la promesse.**
   Employer une question, une proposition bornée, une correction ou une explication selon ce que soutient réellement A2. Une question forte vaut mieux qu'une thèse affirmative fabriquée.

3. **Ne pas additionner les candidats comme confirmations.**
   Des contributions cumulatives peuvent soutenir, préciser ou borner la promesse centrale. Elles ne deviennent ni nouveautés indépendantes ni preuves supplémentaires du fond par simple combinaison.

4. **Borner le périmètre.**
   Expliciter uniquement les frontières de temps, territoire, population, mécanisme, données ou statut juridique dont l'omission changerait matériellement le sens de la promesse.

5. **Définir le gain cognitif lecteur.**
   Répondre : « qu'est-ce qu'un lecteur devrait comprendre de mieux ou différemment ? ». Écarter tout objectif formulé comme convaincre, alerter, faire adhérer ou maximiser l'impact.

6. **Conserver les limites qui changent la promesse.**
   Causalité non établie, contre-hypothèse viable, portée locale, bilan net inconnu, droit non final, nouveauté corpus bornée ou donnée manquante restent visibles lorsqu'ils affectent la conclusion.

7. **Appliquer le test anti-inflation.**
   Retirer de la promesse toute généralisation, causalité, responsabilité ou importance qui n'existe qu'en fusionnant artificiellement plusieurs candidats ou en supprimant leurs caveats. Si le contrat perd alors son intérêt, transmettre `NON_TENABLE` à S04 au lieu de le regonfler.

8. **Ne pas préempter S04/A4.**
   S03 ne choisit ni `FORME_LONGUE`, ni `SHORTER_OUTPUT`, ni `MORE_INVESTIGATION`, ni `NO_ARTICLE`; elle ne produit ni plan détaillé, ni sections, ni prose, ni décision `PUBLISH`. Elle peut signaler une dépendance à une information, mais A6 reste seul compétent pour un BACK.

### Sortie minimale

Si le contrat est tenable :

- question ou proposition centrale au niveau réellement soutenu ;
- périmètre matériel ;
- gain cognitif lecteur ;
- limites matérielles ;
- rôle éventuel des contributions requalifiées lorsqu'il faut empêcher leur inflation.

Si aucun contrat honnête n'est tenable :

```text
CONTRAT = NON_TENABLE
RAISON MATÉRIELLE = EXPLICITE
NEXT = S04
```

Aucun template, score, persona, format de handoff, plan ou schéma obligatoire n'est requis.

### REPAIR_IF


- transforme automatiquement toute contribution survivante en thèse affirmative ;
- généralise une diffusion locale en tendance/politique nationale non établie ;
- utilise des contributions cumulatives comme corroborations indépendantes ;
- gonfle une contribution étroite pour lui donner une importance centrale ;
- supprime une contre-hypothèse ou limite matérielle pour renforcer la promesse ;
- définit la valeur lecteur comme persuasion ;
- décide déjà la longueur, la forme, le plan, la prose, `PUBLISH` ou un BACK A6.

### HOLD_IF

la promesse éditoriale dépend d'une ambiguïté matérielle que les sorties amont disponibles ne permettent pas de borner honnêtement. Un contrat non tenable n'est pas un HOLD : il est transmis comme tel à S04.

### STOP_WHEN

un contrat borné est établi ou sa non-tenabilité est explicitement démontrée, sans mutation silencieuse des bornes A2/S02.

---

<!-- NODE: PROTOCOL.A3-S04 -->
<!-- TRACE: IMPLEMENTS=STORY.A3-S04 -->
## A3-S04 - Prendre une décision pré-rédactionnelle

### But

Choisir **exactement une** suite éditoriale depuis le contrat S03 avant toute construction ou rédaction :

```text
DÉCISION_COURANTE ∈ {
  FORME_LONGUE,
  SHORTER_OUTPUT,
  MORE_INVESTIGATION,
  NO_ARTICLE
}

PUBLISH ∉ DÉCISION_COURANTE
```

### Invariants

```text
VOLUME_D_ENQUÊTE != JUSTIFICATION_DE_FORME_LONGUE
CONTRIBUTION_FORTE != FORME_LONGUE_AUTOMATIQUE
GAP_INTÉRESSANT != MORE_INVESTIGATION
CONTRAT_TENABLE != OBLIGATION_DE_PRODUIRE_LONG
FORME_LONGUE + SHORTER_OUTPUT = INTERDIT COMME DÉCISION COURANTE
MORE_INVESTIGATION + PRODUCTION_IMMÉDIATE = INTERDIT COMME DÉCISION COURANTE
```

### Entrée par défaut

S04 consomme :

- le contrat éditorial S03 ;
- les rôles requalifiés C-01 à C-04 ;
- les gaps A6 conditionnels déjà identifiés ;
- uniquement les sorties amont nécessaires pour tester si une forme plus simple préserverait ou détruirait le gain.

Aucune relecture globale des 50 quintessences ou des investigations brutes n'est requise par défaut.

### Exécution

1. **Vérifier qu'une production reste justifiée.**
   Si le contrat est non tenable ou la valeur lecteur nulle, considérer `NO_ARTICLE` ou, seulement si un besoin d'information précis peut changer la décision, `MORE_INVESTIGATION`.

2. **Tester d'abord l'indispensabilité d'une information nouvelle.**

   ```text
   BESOIN_NON_RÉSOLU
   + GAIN_D_INFORMATION_PLAUSIBLE
   + DÉCISION_MATÉRIELLE_SUSCEPTIBLE_DE_CHANGER
   -> MORE_INVESTIGATION CANDIDAT
   ```

   Un candidat A6 dormant, une curiosité ou une amélioration possible ne suffit pas. A6 conserve seule l'autorité d'autoriser et cibler le BACK.

3. **Tester la forme la plus simple suffisante.**
   Demander si le gain central, ses mécanismes indispensables, son contrepoint matériel et ses limites déterminantes peuvent être transmis par `SHORTER_OUTPUT` **sans changer ce que le lecteur comprend**.

   - si oui : `SHORTER_OUTPUT` ;
   - si non, et si le développement étendu est nécessaire : `FORME_LONGUE`.

   Le test porte sur la perte cognitive, pas sur le nombre d'investigations, de mots ou de sources.

4. **Refuser la forme longue par prestige ou inertie.**
   Une enquête volumineuse peut produire un delta court. Inversement, une contribution relativement simple peut exiger une forme longue si la compréhension honnête dépend de plusieurs mécanismes, contre-hypothèses et limites qui ne peuvent être compactés sans déformation.

5. **Refuser les décisions hybrides.**
   Une seule voie courante est conservée. Si `MORE_INVESTIGATION` est choisie, aucun départ A4 n'est autorisé avant retour A6 et nouvelle décision A3.

6. **Appliquer la règle d'arrêt.**

   ```text
   PAS_DE_NOUVELLE_INFORMATION
   + PAS_DE_DÉFAUT_MATÉRIEL_NOUVEAU
   + DÉCISION_JUSTIFIÉE
   -> PAS_DE_REPLAY_A3_PAR_DÉFAUT
   ```

7. **Ne pas préempter A4/A5.**
   S04 choisit la voie, pas le plan, la structure détaillée, la prose ni `PUBLISH`.

### Sortie minimale

- une décision courante unique ;
- la raison pour laquelle les trois autres voies sont écartées dans l'état courant ;
- les obligations de compréhension qui rendent la forme choisie suffisante et la forme rejetée insuffisante, si la décision porte sur la forme ;
- les conditions explicites qui forceraient un retour A3/A6 ;
- aucune prose d'article.

### REPAIR_IF


- choisit `FORME_LONGUE` parce que le corpus est volumineux ;
- choisit plusieurs voies simultanément ;
- déclenche `MORE_INVESTIGATION` parce qu'un gap existe mais sans gain décisionnel ;
- choisit `SHORTER_OUTPUT` en supprimant une nuance qui change le contrat ;
- choisit `NO_ARTICLE` malgré un contrat tenable et une valeur lecteur matérielle sans justification ;
- choisit `PUBLISH` ;
- produit déjà plan, sections ou prose.

### HOLD_IF

les sorties amont sont matériellement contradictoires au point d'empêcher de décider entre les quatre voies.

### STOP_WHEN

une seule décision est matériellement justifiée, que les autres voies sont explicitement écartées dans l'état courant et qu'aucun plan, prose, `PUBLISH` ou BACK non autorisé n'a été produit.


---

# A4 - Construction et écriture

<!-- NODE: PROTOCOL.A4-S01 -->
<!-- TRACE: IMPLEMENTS=STORY.A4-S01 -->
## A4-S01 - Construire la progression de compréhension

### But

Transformer la décision `FORME_LONGUE`, le contrat éditorial S03 et les obligations de transmission S04 en une progression cognitive qui indique ce que le lecteur doit comprendre, dans quel ordre explicatif et avec quelles bornes, **sans rédiger l'article**.

### Invariants

```text
PROGRESSION != ORDRE_DU_CORPUS
PROGRESSION != ORDRE_DES_INVESTIGATIONS
PROGRESSION != LISTE_DE_CLAIMS
PROGRESSION != LISTE_DES_CONTRIBUTIONS_A3
COUVRIR_DES_THÈMES != PRODUIRE_UNE_PROGRESSION
ORDRE_NARRATIF != CAUSALITÉ
JUXTAPOSITION != RELATION
RÉPÉTITION_D_EXEMPLES != PRÉVALENCE
CAS_VIVANT != CAS_REPRÉSENTATIF
OBLIGATION_A3_ABSENTE != DÉTAIL_OPTIONNEL
A4-S01 != PROSE
```

### Entrée par défaut

S01 consomme seulement :

- `A3_S03_EDITORIAL_CONTRACT.md` ;
- `A3_S04_PREWRITING_DECISION.md` ;
- `A3_S04_TRANSMISSION_OBLIGATIONS.tsv` ;
- les contributions, obligations et dispositions réellement émises par A3 pour le dossier courant ;
- une sortie A2 ciblée uniquement si une transition ne peut pas être calibrée honnêtement depuis A3.

L'univers complet des quintessences et investigations brutes n'est pas rechargé par défaut.

### Exécution runtime

1. **Fixer le gain final attendu.**
   Reprendre la question centrale, la proposition bornée et les obligations de transmission sans les transformer en plan.

2. **Construire des états de compréhension.**
   Pour chaque étape candidate :

   ```text
   ÉTAT DU LECTEUR AVANT
   -> CE QUI DOIT ÊTRE COMPRIS
   -> CE QUE CETTE ÉTAPE AUTORISE À COMPRENDRE ENSUITE
   ```

   Une étape n'existe pas parce qu'un thème ou une investigation existe ; elle doit changer matériellement la compréhension aval.

3. **Mapper les obligations et distinctions matérielles A3.**
   Chaque obligation déclarée matérielle doit apparaître là où elle change la compréhension, comme noyau, mécanisme, contrepoint ou borne. Une obligation peut traverser plusieurs étapes ; aucune section dédiée n'est imposée. Des mécanismes ou statuts distincts en amont ne peuvent pas être aplatis en une catégorie unique pour simplifier la narration.

4. **Préserver simultanément décision d'auteur et rendement d'enquête.**
   La contribution centrale peut organiser la progression si elle explique réellement le sujet. Elle ne peut pas devenir une autorisation de supprimer ou subordonner silencieusement les dimensions, découvertes ou relations inter-investigations déclarées matérielles.

5. **Placer les contre-hypothèses avant le verdict qu'elles bornent.**
   Toute contre-hypothèse matérielle doit intervenir avant ou au moment où le lecteur évalue le mécanisme qu'elle borne. La repousser après un verdict déjà narrativement induit ne remplit pas son rôle.

6. **Auditer chaque transition.**
   Refuser une transition qui fabrique implicitement :
   - causalité ;
   - responsabilité ;
   - prévalence nationale ;
   - effet net ;
   - actualité juridique ;
   - représentativité.

7. **Tester l'anti-inventaire sans détruire la topologie explicative.**
   Une progression qui copie mécaniquement l'ordre du corpus, des investigations ou une taxonomie de thèmes doit être reconstruite. En revanche, l'histoire, les acteurs, les flux ou les relations du sujet peuvent structurer l'article lorsqu'ils sont nécessaires pour comprendre l'objet.

   ```text
   MECHANICAL_CORPUS_ORDER = FAIL
   SUBJECT_FORENSIC_TOPOLOGY = PRESERVE_WHEN_MATERIAL
   ```

8. **Tester la nécessité des étapes.**
   Une étape qui ne prépare rien, ne résout rien, ne borne rien et ne change aucun état de compréhension est supprimée ou fusionnée.

9. **Interdire la rédaction.**
   S01 peut produire des libellés fonctionnels et une logique de transition. Elle ne produit ni paragraphes, ni chapô, ni conclusion, ni titre publiable.

### Sortie minimale

- question/gain final repris d'A3 ;
- étapes de compréhension ;
- état avant / gain de chaque étape / transition aval ;
- mapping des obligations et rendements matériels A3 ;
- risques narratifs détectés et bornes associées ;
- éventuelles récupérations ciblées ;
- verdict `PASS`, `REPAIR` ou `HOLD` ;
- `PROSE_WRITTEN = 0`.

Aucun nombre obligatoire d'étapes, template universel, score narratif ou persona n'est requis.

### REPAIR_IF


- reproduit mécaniquement l'ordre du corpus ou des investigations ;
- couvre des thèmes mais perd une obligation, une découverte ou une relation déclarée matérielle ;
- subordonne tout l'objet à une contribution centrale au point de détruire la compréhension amont ;
- place une contre-hypothèse matérielle après une séquence qui a déjà induit le verdict ;
- transforme juxtaposition en causalité, relation en responsabilité, bénéfice en intention ou cas en prévalence ;
- transforme une rupture documentaire locale en propriété générale non établie ;
- transforme une annonce ou trajectoire future en état courant ;
- généralise des cas documentés au-delà de leur portée ;
- rédige déjà l'article.

### HOLD_IF

une transition indispensable dépend d'une contradiction matérielle amont que les sorties A2/A3 disponibles ne permettent pas de borner sans changer le contrat.

### STOP_WHEN

la progression transmet le contrat avec toutes les obligations matérielles, les transitions n'ajoutent aucune relation non établie et aucune étape n'est justifiée seulement par la topologie du corpus.

<!-- NODE: PROTOCOL.A4-S02 -->
<!-- TRACE: IMPLEMENTS=STORY.A4-S02 -->
## A4-S02 - Rédiger une prose traçable

Transformer la progression S01 en prose à partir du contrat et de la compréhension préservée, pas à partir de priors génériques du modèle, tout en maintenant un chemin d'audit praticable entre chaque proposition matérielle et la matière qui l'autorise.

```text
PROSE CITÉE != PROSE SOUTENUE
CITATION DE PARAGRAPHE != SUPPORT DE TOUTES LES PROPOSITIONS
ARTEFACT A2/A3 != PREUVE PUBLIQUE AUTOMATIQUE
MÊME LIGNÉE RÉPÉTÉE != CORROBORATION INDÉPENDANTE
SYNTHÈSE DE PLUSIEURS PIÈCES != ÉNONCÉ D'UNE SOURCE UNIQUE
SUPPORT LOCAL != PORTÉE NATIONALE
TRACE INTERNE != CITATION LECTEUR
TRAÇABILITÉ != CLAIM MATRIX UNIVERSELLE
```

#### Entrée par défaut

S02 consomme d'abord :

- la progression cognitive S01 ;
- le contrat A3-S03 et les obligations matérielles A3-S04 du dossier courant ;
- les sorties A2/A3 qui portent déjà la compréhension et ses bornes ;
- A1, les investigations brutes et les sources seulement par récupération ciblée lorsqu'une formulation matérielle exige une précision ou une preuve que les sorties dérivées ne peuvent pas fournir honnêtement.

Aucun rechargement aveugle des 50 investigations n'est requis par défaut.

#### Unité matérielle de prose

La granularité de traçabilité n'est ni le mot, ni nécessairement la phrase entière. Une **unité matérielle de prose** est la plus petite proposition ou combinaison de propositions dont la fausseté, la portée ou le statut pourraient changer matériellement ce que le lecteur comprend.

Pour chaque unité matérielle :

```text
UNITÉ DE PROGRESSION S01
-> PROPOSITION AUTORISÉE
-> STATUT / PORTÉE AUTORISÉS
-> SUPPORT / BORNE / CONTRADICTION
-> ORIGINE ET CHEMIN DE RETOUR
-> SOURCE PUBLIQUE SI LE CLAIM L'EXIGE
-> PROSE
-> TRACE DE SUPPORT
```

Une unité non matérielle de liaison ou d'explication n'exige pas mécaniquement une ligne de registre.

#### Exécution

1. **Fixer la fonction de l'unité avant rédaction.**
   Identifier l'étape S01 servie et la compréhension qu'elle doit produire. La prose n'a pas le droit d'élargir la promesse pour rendre le passage plus spectaculaire.

2. **Identifier les propositions matérielles réellement exprimées.**
   Une phrase composée peut contenir plusieurs propositions différentes. Si leurs supports, statuts ou portées diffèrent, les traiter séparément ou scinder la formulation.

3. **Vérifier l'adéquation du support.**
   Pour chaque proposition matérielle, demander :

   ```text
   CE SUPPORT ÉTABLIT-IL
   LA SUBSTANCE + LE STATUT + LA PORTÉE
   RÉELLEMENT ÉCRITS ?
   ```

   Une source locale ne soutient pas une généralisation nationale. Une corrélation ne soutient pas une causalité. Une annonce ne soutient pas un état final. Un flux ne soutient pas un effet net.

4. **Distinguer les fonctions de la matière.**
   Une pièce peut :
   - soutenir ;
   - borner ;
   - contredire ;
   - fournir seulement du contexte ou une piste de récupération.

   Une borne ne devient pas un support positif par commodité rédactionnelle.

5. **Préserver les lignées.**
   Investigation, quintessence, mémoire et synthèse dérivées d'une même origine restent une seule lignée. Leur répétition ne crée pas de corroboration indépendante.

6. **Séparer trace interne et preuve publique.**
   A2/A3 servent à comprendre, naviguer et calibrer. Lorsqu'une affirmation matérielle de l'article demande une preuve publique ou une citation, revenir à la source ou à l'élément probatoire approprié. L'artefact interne reste dans la trace de production, pas comme substitut automatique de preuve lecteur.

7. **Traiter les synthèses comme des synthèses.**
   Si la prose combine plusieurs pièces pour produire une relation ou une conclusion que n'énonce aucune source isolée, la trace doit le signaler. Chaque composant doit être soutenu et la relation synthétique doit rester au niveau autorisé par A2/A3.

8. **Appliquer la localité des citations.**
   Une citation placée à la fin d'un paragraphe ne blanchit pas toutes les affirmations précédentes. La citation doit être assez proche de l'unité qu'elle soutient pour que son périmètre soit non ambigu, ou le passage doit être scindé.

9. **Récupérer localement si nécessaire.**
   Si le support ou la portée ne peuvent pas être établis depuis la matière active :

   ```text
   A2/A3
   -> A1 CIBLÉ
   -> BRUT / SOURCE CIBLÉS
   -> SI TOUJOURS INSUFFISANT : BORNE OU RETOUR A3/A6 SELON LE BESOIN
   ```

   Ne jamais compléter par connaissance générique du modèle.

10. **Produire une trace minimale.**
    La trace S02 doit suffire à retrouver les affirmations matérielles importantes sans devenir une matrice universelle. La forme minimale attendue est un support map limité aux unités matérielles de la production, avec au plus : étape S01, ancre de prose, proposition matérielle, statut/portée, fonction du support, origine/retour, source publique si requise, et éventuelle note de synthèse.

11. **Ne pas exposer la plomberie.**
    EPICs, stories, gates, UUID, replays et artefacts internes ne doivent pas apparaître dans le texte lecteur sauf nécessité éditoriale explicite.

12. **Ne pas préempter S03.**
    S02 doit empêcher une prose matériellement non soutenue. L'audit systématique de sur-affirmation, sous-affirmation et effets narratifs appartient encore à S03.

#### Sortie minimale lors de l'exécution réelle

- un draft correspondant à la progression S01 ;
- un support map limité aux unités matérielles ;
- les récupérations ciblées réellement déclenchées ;
- les propositions encore `HOLD` ou à borner ;
- aucun nouveau claim obtenu par connaissance générique ;
- verdict `PASS`, `REPAIR` ou `HOLD`.

Aucun score de citation, quota de sources, nombre minimal de notes, claim matrix universelle ou agent de fact-check séparé n'est imposé.

#### REPAIR_IF


- confond présence d'une citation et adéquation du support ;
- laisse une citation de fin de paragraphe soutenir implicitement plusieurs propositions hétérogènes ;
- transforme un support local en portée nationale ;
- transforme corrélation, séquence, flux ou implication en causalité, effet net ou responsabilité ;
- compte plusieurs représentations d'une même lignée comme corroborations ;
- cite un artefact A2/A3 comme preuve publique lorsque le claim exige de revenir à la source ;
- utilise un ancien article comme preuve du fond ;
- présente une synthèse multi-source comme si une source unique l'énonçait ;
- complète une précision absente depuis les priors du modèle ;
- expose la plomberie du workflow comme contenu éditorial.

#### HOLD_IF

une proposition indispensable à la progression ne peut pas être formulée honnêtement avec la matière récupérable et une simple borne détruirait matériellement le contrat.

#### STOP_WHEN

chaque unité matérielle du draft possède un support et une portée adéquats ou une borne explicite, que les chemins de retour sont praticables, qu'aucune lignée n'est blanchie en corroboration et que la prose peut être transmise à S03 sans ajout matériel non tracé.

<!-- NODE: PROTOCOL.A4-S03 -->
<!-- TRACE: IMPLEMENTS=STORY.A4-S03 -->
## A4-S03 - Calibrer épistémiquement et narrativement

### But

Attaquer la prose S02 avant fermeture éditoriale afin que la force narrative, les verbes, transitions et synthèses restent exactement sous le plafond autorisé par les preuves et par la décision d'auteur, sans stériliser le rendement de l'enquête.

### Contrat minimal

Pour toute formulation matérielle ou transition qui augmente implicitement la force d'une proposition :

```text
RELATION != CAUSALITÉ
BÉNÉFICE != INTENTION
CAS != PRÉVALENCE
NON_TROUVÉ != ABSENT
ANNONCE != ÉTAT_FINAL
PRUDENCE != EFFACEMENT_DU_RENDEMENT
```

S03 doit également vérifier que la calibration n'a pas transformé les découvertes, contradictions, acteurs ou mécanismes matériels en caveats vagues.

### Exécution

1. relever les formulations qui portent causalité, responsabilité, intention, portée, fréquence, actualité ou généralisation ;
2. confronter chacune au support déjà tracé en S02 ;
3. réparer uniquement la plus petite formulation fautive ;
4. vérifier les transitions narratives et la conclusion provisoire contre les mêmes bornes ;
5. ne rouvrir A3/A6 que si le défaut ne peut pas être réparé sans changer la décision ou sans information nouvelle.

### Sortie

- défauts P0/P1/P2 avec disposition ;
- réparations locales ;
- prose V2 distincte si nécessaire ;
- `NEW_BACK = 0` sauf besoin probatoire matériel explicite ;
- verdict `PASS`, `REPAIR` ou `HOLD`.

---

<!-- NODE: PROTOCOL.A4-S04 -->
<!-- TRACE: IMPLEMENTS=STORY.A4-S04 -->
## A4-S04 - Fermer la progression

### But

Fermer titre, chapô, corps et conclusion après S03 sans créer une nouvelle thèse, une nouvelle preuve ou une portée plus forte que le corps audité.

### Contrat minimal

```text
TITRE <= CORPS_AUTORISÉ
CHAPÔ <= CORPS_AUTORISÉ
CONCLUSION <= CORPS_AUTORISÉ
FERMETURE != NOUVELLE_DÉCISION_ÉDITORIALE
```

La conclusion doit répondre, selon pertinence :

1. qu'avons-nous compris de plus ?
2. qu'est-ce que cela change ?
3. jusqu'où peut-on l'affirmer ?
4. qu'est-ce qui reste matériellement ouvert ?

### STOP_WHEN

titre, chapô et conclusion ne dépassent pas le corps calibré, que les références sont cohérentes et qu'aucun nouveau BACK ou changement de thèse n'est introduit.

---

# A5 - Review et réparation

<!-- NODE: PROTOCOL.A5-S01 -->
<!-- TRACE: IMPLEMENTS=STORY.A5-S01 -->
## A5-S01 - Contrat de review matérielle

Attaquer le candidat selon les modes d'échec réellement matériels : fidélité factuelle, raisonnement, contre-thèse, compréhension lecteur, valeur éditoriale, auditabilité, perte forensique et généricité. Aucun casting fixe d'agents n'est requis.

Un article exact et traçable doit encore échouer si son rendement d'enquête a été aplati au point qu'une recherche superficielle aurait produit presque le même texte.

<!-- NODE: PROTOCOL.A5-S02 -->
<!-- TRACE: IMPLEMENTS=STORY.A5-S02 -->
## A5-S02 - Classer les défauts

Séparer :

```text
P0 = défaut qui invalide matériellement le raisonnement ou le produit
P1 = faiblesse sérieuse à fermer avant décision terminale
P2 = amélioration non bloquante
```

Une préférence stylistique ne devient pas un P1 sans effet matériel démontré.

<!-- NODE: PROTOCOL.A5-S03 -->
<!-- TRACE: IMPLEMENTS=STORY.A5-S03 -->
## A5-S03 - Réparation locale aval

Réparer chaque P0/P1 au plus petit propriétaire aval suffisant. Si une nouvelle information est indispensable, transmettre un besoin ciblé à A6. Ne jamais relancer globalement le pipeline par défaut.

<!-- NODE: PROTOCOL.A5-S04 -->
<!-- TRACE: IMPLEMENTS=STORY.A5-S04 -->
## A5-S04 - Décision terminale de review

Après fermeture des défauts matériels, choisir une seule disposition :

```text
PUBLISH_CANDIDATE
SHORTER_OUTPUT
MORE_INVESTIGATION
NO_ARTICLE
```

`PUBLISH_CANDIDATE` signifie que la review éditoriale aval est fermée ; il ne préempte pas la validation composée A7 ni la canonicalisation.

---


# A6 - BACK et réinvestigation

A6 est transverse : les responsabilités aval peuvent signaler un besoin d'information,
mais A6 seul porte le retour ciblé vers Truth Engine.

```text
NO_BLIND_REINVESTIGATION
```

<!-- NODE: PROTOCOL.A6-S01 -->
<!-- TRACE: IMPLEMENTS=STORY.A6-S01 -->
<!-- TRACE: CONSTRAINED_BY=PFD.F-09 -->
### A6-S01 - Éligibilité du BACK

Un BACK n'est légitime que si le besoin non résolu est explicite, si un gain d'information plausible est attendu et si cette information peut changer une compréhension ou une décision matérielle.

Aucun format de requête ni nom de champ n'est figé à ce stade.

<!-- NODE: PROTOCOL.A6-S02 -->
<!-- TRACE: IMPLEMENTS=STORY.A6-S02 -->
<!-- TRACE: CONSTRAINED_BY=PFD.F-09 -->
### A6-S02 - Demande ciblée à Truth Engine

Définir la plus petite question investigable ou le plus petit gap nécessaire au protocole aval, sans prescrire les internals de Truth Engine.

<!-- NODE: PROTOCOL.A6-S03 -->
<!-- TRACE: IMPLEMENTS=STORY.A6-S03 -->
<!-- TRACE: CONSTRAINED_BY=PFD.F-12 -->
### A6-S03 - Reprise aval locale

Quand une nouvelle matière d'enquête revient, ne rouvrir que les surfaces de compréhension, décision, écriture ou review matériellement affectées.

## Critères de fin

- chaque réinvestigation a un but explicite ;
- un replay sans gain d'information plausible est refusé ;
- une réparation de prose ne remplace pas un gap probatoire matériel et investigable ;
- une nouvelle preuve ne force pas la reprise de travaux aval non affectés ;
- aucun schéma opérationnel BACK n'est prématurément figé.

---

# A7 - Validation composée

<!-- NODE: PROTOCOL.A7-S01 -->
<!-- TRACE: IMPLEMENTS=STORY.A7-S01 -->
## A7-S01 - Fixtures fondatrices

Exécuter les cas d'acceptation existants : recall, perte de quintessence, blanchiment mémoire, MnemoLite dégradé, préservation épistémique, réinvestigation utile vs aveugle, valeur article et convergence. Un test connu n'est pas présenté comme audit indépendant.

<!-- NODE: PROTOCOL.A7-S02 -->
<!-- TRACE: IMPLEMENTS=STORY.A7-S02 -->
## A7-S02 - Replay dossier réel

Exécuter le protocole composé sur au moins un corpus réel et vérifier simultanément qualité du produit et survie du rendement matériel des investigations.

<!-- NODE: PROTOCOL.A7-S03 -->
<!-- TRACE: IMPLEMENTS=STORY.A7-S03 -->
## A7-S03 - Régression adversariale

Réintroduire des défauts connus : aplatissement, faux upgrade épistémique, fausse corroboration, prose générique, replay inutile, causalité fabriquée ou non-convergence. Le candidat doit les rejeter.

<!-- NODE: PROTOCOL.A7-S04 -->
<!-- TRACE: IMPLEMENTS=STORY.A7-S04 -->
## A7-S04 - Audit froid

Faire auditer le produit final depuis un contexte réellement frais contre VISION/PFD et les preuves nécessaires, sans fournir l'intention d'implémentation comme réponse attendue.

```text
SAME_SESSION_INTERNAL_REVIEW != INDEPENDENT_COLD_AUDIT
```

Si aucun contexte réellement frais n'est disponible, A7 doit conserver `HOLD_EXTERNAL_COLD_AUDIT_ONLY` au lieu de simuler l'indépendance.

## Décision A7

```text
TOP_DOWN: FOUNDATION -> EPIC -> STORY -> TEST -> RUNTIME
BOTTOM_UP: RUNTIME RULE -> STORY -> EPIC -> FOUNDATION
PRODUCT: ARTICLE -> VISION/PFD SUCCESS
```

Les trois directions doivent résister. Un harnais interne vert ne compense jamais un produit qui échoue au test final de VISION/PFD.

---

