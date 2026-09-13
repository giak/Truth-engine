---
doc:
  id: FOUNDATION.PFD
  type: foundation
  title: Project Foundation Requirements
  version: V4.4-R1-candidate
  status: candidate_repair
  authority: normative_candidate
summary: >
  Rend testables les propriétés de VISION sans prescrire l'architecture.
derives_from:
  - FOUNDATION.PFD.V4_4
constrained_by:
  - FOUNDATION.VISION
non_regression_oracles:
  - PARENT_V4_3/PFD_V4_3.md
  - AUDIT/FOUNDATION_V4_3_MULTIROLE_CHALLENGE.md
---

# PFD.md

# Project Foundation Requirements

**Projet : transformation de matière d'enquête Truth Engine en articles Substack**  
**Statut : fondation candidate V4.4**  
**Portée : exigences fondatrices testables. Les schémas canoniques sont dans `VISION.md`.**

---

## 1. Besoin

Truth Engine produit des runs d'investigation bornés, souvent répétés et chevauchants. MnemoLite rend récupérables des objets de natures différentes. Les quintessences réduisent le bruit d'exécution. Le protocole Article doit transformer cette matière en contexte cognitif exploitable, puis en article, **sans perdre, contaminer ou surinterpréter l'enquête**.

Le risque principal n'est pas seulement l'hallucination. Il est aussi :

- sélection trop précoce du contexte ;
- perte lors du débruitage ;
- circularité de mémoire ;
- confusion entre article, synthèse, fait et preuve ;
- répétition aveugle des enquêtes ;
- article exact mais générique ou cognitivement vide.

---

## 2. Entrées et frontières

Le système peut disposer de :

- investigations et packages Truth Engine ;
- faits avec statuts épistémiques et provenance ;
- quintessences ;
- MnemoLite ;
- corpus Substack.

Il doit distinguer :

```text
AVAILABLE_UNIVERSE
PROJECT_WORKING_VIEW
ROLE_ACTIVE_CONTEXT
```

Aucun de ces niveaux ne prouve l'exhaustivité du sujet.

Une investigation `FINAL` reste finalisée relativement au contrat/runtime qui l'a produite :

```text
FINAL != COMPLETE != CERTIFIED_TRUTH
```

---

## 3. Exigences fondatrices

<!-- NODE: PFD.F-01 -->
<!-- TRACE: DERIVES_FROM=VISION.CONTEXT; VERIFIED_BY=PFD.AC-01 -->
### F-01 - Préserver la matière récupérable

Le système doit garder accès à l'univers disponible même lorsqu'il réduit le contexte actif.

Une exclusion du contexte ne doit pas équivaloir à une suppression ni à une décision d'irrelevance définitive.

<!-- NODE: PFD.F-02 -->
<!-- TRACE: DERIVES_FROM=VISION.CONTEXT; VERIFIED_BY=PFD.AC-01 -->
### F-02 - Adapter le contexte à la tâche

Une vue de travail commune peut exister, mais chaque responsabilité doit pouvoir réduire son contexte ou remonter vers l'univers disponible lorsque sa tâche l'exige.

Le système doit éviter le double échec :

```text
TOO_MUCH_CONTEXT -> COGNITIVE_NOISE
TOO_LITTLE_CONTEXT -> MATERIAL_OMISSION
```

<!-- NODE: PFD.F-03 -->
<!-- TRACE: DERIVES_FROM=VISION.MEMORY; VERIFIED_BY=PFD.AC-03 -->
### F-03 - Typer la mémoire MnemoLite

Tout objet mémoire matériel doit conserver suffisamment d'information pour distinguer :

- type d'objet ;
- origine ;
- statut épistémique si applicable ;
- date/version utile ;
- lien vers l'artefact ou la preuve canonique.

Le système doit préserver :

```text
MEMORY_TYPE != EPISTEMIC_STATUS
EDITORIAL_MEMORY != VERIFIED_FACT_MEMORY
RETRIEVED_MEMORY != INDEPENDENT_CORROBORATION
```

<!-- NODE: PFD.F-04 -->
<!-- TRACE: DERIVES_FROM=VISION.MEMORY; VERIFIED_BY=PFD.AC-03 -->
### F-04 - Interdire le blanchiment par mémoire

Une interprétation provenant d'un article, d'une synthèse ou d'une ancienne quintessence ne doit jamais devenir une corroboration indépendante par simple réapparition sémantique.

```text
MEMORY_CAN_SEED_DISCOVERY
MEMORY_CANNOT_CONFIRM_ITSELF
```

Pour une affirmation matérielle, la chaîne doit pouvoir revenir vers l'artefact et, lorsque nécessaire, la preuve inspectée.

<!-- NODE: PFD.F-05 -->
<!-- TRACE: DERIVES_FROM=VISION.MEMORY; VERIFIED_BY=PFD.AC-04 -->
### F-05 - Tolérer un MnemoLite dégradé

MnemoLite peut être indisponible, incomplet ou obsolète.

Le système doit alors :

- utiliser les artefacts directement disponibles ;
- signaler la continuité mémoire perdue ;
- bloquer seulement si cette perte empêche une décision matérielle.

<!-- NODE: PFD.F-06 -->
<!-- TRACE: DERIVES_FROM=VISION.QUINTESSENCE; VERIFIED_BY=PFD.AC-02 -->
### F-06 - Débruiter sans perdre

Une quintessence doit réduire la plomberie d'exécution tout en conservant tout élément susceptible de modifier compréhension, confiance, scope, décision, narration ou conclusion.

Elle doit rester :

- traçable vers l'investigation ;
- réversible vers le brut ;
- non autoritaire ;
- porteuse des limites épistémiques matérielles.

<!-- NODE: PFD.F-07 -->
<!-- TRACE: DERIVES_FROM=VISION.QUINTESSENCE,VISION.PRODUCT; VERIFIED_BY=PFD.AC-05 -->
### F-07 - Préserver les statuts épistémiques

Les distinctions matérielles entre fait, preuve, inférence, hypothèse, spéculation, inconnu, causalité et responsabilité ne doivent pas être aplaties pendant le trajet :

```text
INVESTIGATION
-> QUINTESSENCE
-> MEMORY / CONTEXT
-> ARTICLE
```

Le PFD n'impose pas un schéma EPI particulier ; il impose la non-perte des distinctions qui changent ce que l'article peut affirmer.

<!-- NODE: PFD.F-08 -->
<!-- TRACE: DERIVES_FROM=VISION.UNDERSTAND; VERIFIED_BY=PFD.AC-07 -->
### F-08 - Comprendre avant sélection éditoriale

Avant de figer un angle ou une thèse, le système doit avoir une compréhension suffisante du fonctionnement, des mécanismes, acteurs, flux, contradictions, contre-hypothèses et inconnues matériels.

Sur un corpus multi-investigations, cette compréhension doit aussi reconstruire les relations matérielles entre investigations lorsque leur omission peut changer l'explication : complémentarités, recouvrements, contradictions, supersessions, évolutions temporelles, mécanismes transversaux, relations nouvelles, trous communs ou changements d'échelle. Une découverte qui n'existe que dans la relation entre plusieurs investigations doit rester récupérable.

Les claims servent à contrôler la preuve, pas à représenter seuls cette compréhension.

<!-- NODE: PFD.F-09 -->
<!-- TRACE: DERIVES_FROM=VISION.REINVESTIGATE; VERIFIED_BY=PFD.AC-06 -->
### F-09 - Autoriser les réinvestigations à but explicite

Le système doit appliquer :

```text
NO_BLIND_REINVESTIGATION
```

Une nouvelle investigation est légitime si son objectif est explicite et son gain d'information plausible : approfondissement, angle alternatif, contre-thèse, gap, mise à jour, contradiction ou nouvelle piste.

<!-- NODE: PFD.F-10 -->
<!-- TRACE: DERIVES_FROM=VISION.CONTRIBUTION; VERIFIED_BY=PFD.AC-07 -->
### F-10 - Évaluer la contribution éditoriale

Avant la prose longue, le système doit établir ce que l'article apporte au corpus publié en termes de nouveauté, importance et pouvoir explicatif.

Si une production reste candidate, la décision d'auteur doit rendre explicites, à la profondeur nécessaire : le sujet réel, la question ou thèse organisatrice, la tension principale, les découvertes et mécanismes indispensables, les coupes conscientes, l'intention de progression cognitive et la conclusion probable avec sa borne. Ces décisions viennent de la matière ; la prose ne doit pas les fabriquer silencieusement.

Si la contribution est insuffisante, `SHORTER_OUTPUT`, `MORE_INVESTIGATION` et `NO_ARTICLE` sont des sorties valides.

<!-- NODE: PFD.F-11 -->
<!-- TRACE: DERIVES_FROM=VISION.PRODUCT; VERIFIED_BY=PFD.AC-07 -->
### F-11 - Produire un article autonome, cumulatif et auditable

L'article final doit être :

- compréhensible par un lecteur froid sans lecture obligatoire du corpus antérieur ;
- non répétitif pour un lecteur assidu ;
- traçable pour ses affirmations matérielles ;
- suffisamment porteur du rendement réel de l'enquête pour que les découvertes, mécanismes, acteurs, relations, contradictions ou autres éléments matériels retenus restent reconnaissables dans le produit.

Un article exact et traçable mais générique, aplati ou presque reproductible sans le travail profond de Truth Engine échoue à cette exigence.

<!-- NODE: PFD.F-12 -->
<!-- TRACE: DERIVES_FROM=VISION.REINVESTIGATE,VISION.SUCCESS; VERIFIED_BY=PFD.AC-08 -->
### F-12 - Réparer localement et converger

Lorsqu'un défaut est détecté, le système doit revenir vers la plus petite surface suffisante et ne rejouer que les dépendances affectées, sauf raison matérielle contraire.

Le système doit pouvoir terminer en :

```text
PUBLISH
SHORTER_OUTPUT
MORE_INVESTIGATION
NO_ARTICLE
```

---

## 4. Contraintes non fonctionnelles

<!-- NODE: PFD.NFR-01 -->
### NFR-01 - KISS
Une règle, un artefact ou un contrôle doit protéger une propriété nommée. Sinon il est candidat à suppression.

<!-- NODE: PFD.NFR-02 -->
### NFR-02 - DRY
La même information ne doit pas être dupliquée dans plusieurs couches sans gain démontrable.

<!-- NODE: PFD.NFR-03 -->
### NFR-03 - YAGNI
Ne pas transformer les fondations en moteur de workflow. Les noms d'étapes, formats et rôles appartiennent à l'architecture future.

<!-- NODE: PFD.NFR-04 -->
### NFR-04 - Charge cognitive proportionnée
Le contexte actif doit être aussi petit que possible **après** protection contre la perte matérielle, jamais au prix de celle-ci.

<!-- NODE: PFD.NFR-05 -->
### NFR-05 - Dégradation honnête
Une dépendance mémoire ou une source indisponible produit une limitation explicite, pas une reconstruction silencieuse.

<!-- NODE: PFD.NFR-06 -->
### NFR-06 - Non-régression
Toute simplification future doit conserver les propriétés fondatrices de VISION/PFD ou démontrer pourquoi elles ne sont plus nécessaires.

---

## 5. Tests d'acceptation fondateurs

<!-- NODE: PFD.AC-01 -->
### AC-01 - Recall test

Introduire une pièce contradictoire peu évidente hors du contexte actif initial. Avant décision finale, le système doit pouvoir la redécouvrir si elle change matériellement l'interprétation.

**FAIL** si une exclusion précoce devient irréversible.

<!-- NODE: PFD.AC-02 -->
### AC-02 - Quintessence-loss test

Faire prendre une décision importante à partir du brut puis à partir de la quintessence.

**FAIL** si la quintessence change matériellement compréhension, confiance, scope ou conclusion sans justification explicite.

<!-- NODE: PFD.AC-03 -->
### AC-03 - Memory-laundering test

Indexer un ancien article ou une synthèse contenant une interprétation non prouvée.

**FAIL** si cette interprétation revient comme fait ou corroboration indépendante.

<!-- NODE: PFD.AC-04 -->
### AC-04 - Mnemo-degraded test

Rendre MnemoLite indisponible ou incomplet.

Le système doit continuer avec les artefacts disponibles ou bloquer pour une raison matérielle précise.

**FAIL** s'il invente la mémoire manquante ou bloque systématiquement.

<!-- NODE: PFD.AC-05 -->
### AC-05 - Epistemic-preservation test

Injecter des objets de statuts différents : fait, hypothèse, gap, causalité non établie.

**FAIL** si le passage investigation -> quintessence -> contexte -> article augmente silencieusement leur certitude.

<!-- NODE: PFD.AC-06 -->
### AC-06 - Reinvestigation-purpose test

Proposer deux nouveaux runs : un avec objectif explicite et gain d'information plausible, un replay sans but nouveau.

Le premier doit pouvoir être accepté, le second refusé.

<!-- NODE: PFD.AC-07 -->
### AC-07 - Article-value test

Un lecteur froid doit comprendre l'objet ; un lecteur assidu doit identifier la contribution ; un auditeur doit remonter les affirmations matérielles vers leur support ; le produit doit transmettre suffisamment le rendement de l'enquête et sa progression de compréhension.

**FAIL** si l'article est exact mais générique, répétitif, non auditable, s'il perd une relation inter-investigations matérielle sans justification, ou s'il pourrait être produit presque à l'identique par une recherche superficielle malgré un corpus Truth Engine profond.

<!-- NODE: PFD.AC-08 -->
### AC-08 - Convergence test

Après fermeture des défauts matériels, répéter le workflow sans nouvelle information.

**FAIL** si cela rouvre une boucle globale sans gain décisionnel attendu.

---

## 6. Faux signaux de réussite

Ne suffisent pas :

- 100 % des claims tracés ;
- toutes les investigations résumées ;
- 0 P0/P1/P2 internes ;
- hashes corrects ;
- français correct ;
- prudence rhétorique ;
- nombre élevé de sources ;
- MnemoLite consulté ;
- tous les rôles exécutés.

Le seul succès utile est un article qui **conserve le rendement réel de l'enquête, ajoute quelque chose d'important, reste calibré et sait pourquoi il existe**.
