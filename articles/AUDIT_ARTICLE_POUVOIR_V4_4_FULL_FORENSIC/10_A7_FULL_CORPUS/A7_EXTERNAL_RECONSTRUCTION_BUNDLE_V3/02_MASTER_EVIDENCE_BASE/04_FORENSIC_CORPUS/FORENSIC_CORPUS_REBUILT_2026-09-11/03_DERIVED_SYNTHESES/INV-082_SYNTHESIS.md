---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "synthesis"
artifact_id: "INV-082-SYNTHESIS"
version: "1.0"
status: "final"
updated: "2026-09-08"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-082"
input_gate: "INV-082_SYNTHESIS_INPUT_GATE.md"
---

<!-- TRACE: synthesized_from=INV-081,INV-085 -->
<!-- EXECUTION: truth_engine_search=false; generic_collection=false; dependency_delta_only=true -->
<!-- GUARD: economic_concentration!=editorial_concentration; ownership!=editorial_command; funding!=topic_tasking; selection_asymmetry!=owner_causation; shared_output!=coordination; reach!=persuasion; editorial_effect!=electoral_effect -->

# INV-082 — Concentration économique versus concentration éditoriale

## 1. Verdict

Les deux dépendances ferment deux objets distincts mais complémentaires :

1. `INV-081` établit une **concentration économique et capitalistique mesurable**, à condition de fixer explicitement métrique, univers, date et définition du contrôle. Elle établit des relations de propriété, des ressources et des capacités, mais **pas leur usage éditorial** ; la chaîne `propriété/financement -> intervention ou contrôle éditorial` reste non établie.
2. `INV-085` établit que la **sélection des sujets/claims est un véritable gate éditorial**, guidé par des critères explicites de pertinence, intérêt public, portée/viralité, dommage, vérifiabilité et jugement éditorial. Elle établit aussi des différences relatives de sélection entre rédactions dans un corpus français, mais **pas l'origine causale** de ces différences ; le commandement généralisé par propriétaire, financeur, État ou plateforme reste non établi.

La synthèse ferme donc une conclusion négative mais substantielle :

> **La coexistence d'une concentration économique et d'une sélection éditoriale non aléatoire ne suffit pas à démontrer une concentration éditoriale causée par la propriété ou le financement.**

Le mécanisme causal fort exige une arête supplémentaire documentée : droit d'intervention effectivement exercé, consigne, tasking, arbitrage attribuable, changement éditorial lié à une transaction ou un financeur, ou design causal équivalent. Cette arête manque dans les deux deltas terminaux.

```text
ECONOMIC_CONCENTRATION                         = ESTABLISHED / bounded by denominator and date
EDITORIAL_SELECTION_GATE                       = ESTABLISHED
SYSTEMATIC_RELATIVE_SELECTION_DIFFERENCES      = ESTABLISHED in one bounded French study
OWNERSHIP_OR_FUNDING_AS_CAUSE_OF_SELECTION     = NOT_ESTABLISHED
GENERAL_OWNER/FUNDER/STATE/PLATFORM_TASKING     = NOT_ESTABLISHED
TRANSVERSAL_DOCUMENTED_COORDINATION             = NOT_ESTABLISHED
GENERAL_EDITORIAL_CONCENTRATION_CAUSAL_CHAIN    = NOT_ESTABLISHED
PERSUASION / BEHAVIOR / ELECTORAL_EFFECT        = NOT_ESTABLISHED
```

## 2. Ce que la concentration économique prouve, et ce qu'elle ne prouve pas

`INV-081` remplace les slogans globaux de type « quelques milliardaires possèdent X % des médias » par une exigence de mesure : **métrique × univers × date × définition du contrôle**. Cette discipline permet d'établir des concentrations réelles dans des sous-univers précis et de documenter des relations juridiques ou organisationnelles.

Ce résultat soutient un modèle de **capacité structurelle** : la propriété, les actifs et le financement donnent accès à des ressources et peuvent créer des possibilités d'intervention. Mais la capacité n'est pas l'action. Le handoff d'INV-081 classe explicitement le contrôle/tasking éditorial en `NOT_ESTABLISHED` et conserve comme gaps `CAU-001` et `CAU-002` : propriété ou financement ne deviennent contrôle éditorial qu'avec des droits exercés ou des traces propres.

La concentration économique est donc un **facteur de risque et de capacité** pertinent pour le pluralisme ; elle n'est pas, à elle seule, une preuve de centralisation des décisions éditoriales.

## 3. Ce que la sélection éditoriale ajoute

`INV-085` montre qu'avant tout verdict ou traitement, les rédactions et fact-checkers opèrent une sélection. Cette sélection est structurée par des règles, des priorités et un jugement éditorial ; elle n'est ni exhaustive ni aléatoire.

Cela rend plausible une concentration éditoriale au sens descriptif — plusieurs acteurs peuvent sélectionner des objets similaires ou laisser hors champ certains objets — mais le delta terminal impose deux limites :

- les critères publiés et les normes d'impartialité coexistent avec des asymétries observées ;
- l'univers des claims rejetés ou non traités n'est pas observé, et les pièces internes de tasking sont absentes.

Par conséquent, `sélection asymétrique -> cause propriétaire/financeur` reste une inférence non fermée.

## 4. Modèles concurrents testés

Conformément à METHOD_PACK §10, les modèles suivants restent concurrents et peuvent coexister.

### A. Pluralisme sous concentration économique

**Compatible avec le corpus.** Des groupes concentrés peuvent héberger plusieurs rédactions dont les décisions éditoriales ne sont pas démontrées comme directement commandées par le propriétaire. Le corpus ne prouve pas l'indépendance parfaite ; il montre seulement que le lien causal fort n'est pas établi.

### B. Capture sectorielle par propriétaire ou financeur

**Possible mais non établie transversalement.** Pour promouvoir ce modèle, il faut des arêtes attribuables entre droits économiques et décisions éditoriales : instructions, nominations assorties d'objectifs éditoriaux, veto, arbitrages documentés, sanctions internes, changements avant/après transaction, ou équivalents.

### C. Alignement émergent

**Compatible et partiellement plausible, mais non démontré comme architecture globale.** Des acteurs peuvent converger sans commandement commun parce qu'ils partagent des critères professionnels, signaux d'audience, contraintes de vérifiabilité, risques juridiques, calendriers d'actualité ou infrastructures de plateforme. `INV-085` documente plusieurs de ces critères ; elle ne démontre pas qu'ils expliquent l'ensemble des convergences observées.

### D. Réseau transversal coordonné

**Non établi.** Ni la propriété concentrée ni des critères de sélection similaires ne démontrent une coordination inter-rédactions. Il manque tasking, échanges, gouvernance commune ou autre mécanisme de coordination documenté.

### E. Architecture cohérente de contrôle éditorial

**Non établie.** Les deux dépendances ne ferment pas une chaîne `centre économique/institutionnel -> tasking transversal -> sélection/cadrage -> exposition -> persuasion -> comportement politique`.

## 5. Frontière probatoire commune

Le plafond de preuve de la synthèse est le suivant :

```text
I0 identity/relation = VERIFIED pour les relations de propriété/organisation et autorités éditoriales documentées
I1 resources/capability/access = VERIFIED/PARTIAL — ressources économiques et gates éditoriaux existent
I2 documented action = VERIFIED séparément pour opérations économiques et sélection éditoriale ; CROSS-EDGE PARTIAL/NOT_ESTABLISHED
I3 coordination/tasking/control = NOT_ESTABLISHED pour un commandement éditorial généralisé attribuable à propriétaire/financeur/État/plateforme
I4 exposure/reach = MEASURED/PARTIAL selon secteurs et contextes ; aucune exposition d'influence causale généralisée
I5 reception/persuasion = NOT_ESTABLISHED
I6 behavior/institutional change = NOT_ESTABLISHED
I7 counterfactual political/electoral outcome = NOT_ESTABLISHED
```

La distinction décisive est donc :

```text
concentration économique -> capacité potentielle              ESTABLISHED
sélection éditoriale -> arbitrage réel                         ESTABLISHED
capacité potentielle -> tasking/intervention éditoriale        NOT_ESTABLISHED generally
tasking/intervention -> concentration éditoriale transversale NOT_ESTABLISHED
concentration éditoriale -> persuasion/effet politique         NOT_ESTABLISHED
```

## 6. Gaps matériels

Trois classes de preuves pourraient changer le verdict :

1. **pièces internes de tasking ou d'intervention** reliant propriétaire/financeur à des décisions éditoriales précises ;
2. **dénominateurs de sélection observables** — calendrier éditorial, claims proposés/rejetés, longitudinal avant/après changement de propriété ou de financement — permettant de tester causalement la sélection ;
3. **chaîne d'effet** reliant sélection/cadrage à exposition différentielle, réception, comportement et résultat politique avec un design causal crédible.

Une nouvelle collecte générique sur la concentration ou les politiques éditoriales serait cumulative tant qu'elle ne fournit pas l'une de ces arêtes.

## 7. Conclusion opérationnelle

La synthèse ne justifie ni le slogan `propriété concentrée = ligne éditoriale concentrée`, ni son inverse `absence de preuve de tasking = indépendance éditoriale`. Le résultat robuste est plus étroit : **capacité économique et gate éditorial sont tous deux réels ; leur relation causale générale n'est pas établie par le corpus fermé.**

Pour `INV-133`, ce delta favorise une comparaison explicite entre pluralisme, captures sectorielles et alignements émergents, et empêche de promouvoir un modèle de coordination ou d'architecture globale sans arêtes supplémentaires.
