j'ai des agents, orchestrator, des prompts très évolués, des frameworks complexes, etc. (regarde dans ma mémoire et historique de conversation).

ce qui me manque, c'est la vérification. je passe trop de temps à demander aux LLM de "double check" ou carrément "KISS, DRY, YAGNI, no-overgineering, pragmatique, éfficace, robuste, refactoring, concis, précis, rigoureux, maniaque, fiable. NO sycophancy, honnêteté absolue, vérité forensique, Double check tout. no regression."

cela doit passer obligatoirement par le contrat via  AGENT.md

il faut un examen, une boucle de vérification : une commande unique qu'un agent doit lancer lui-même avant d'afficher quoi que ce soit. l'agent n'a pas le droit de présenter un travail qui n'est pas vérifié.

bac à sable : un agent doit travailler dans un worktree par chantier avec permissions.

session neuve : le reviewer.


---

# Cahier des charges

## Gate de vérification obligatoire pour Truth Engine / Codebuff

**Statut :** spécification fonctionnelle et technique initiale
**Projet :** Truth Engine
**Cible principale :** Codebuff Terminal
**Compatibilité visée :** Freebuff / framework Codebuff
**Principe directeur :** aucun travail ne peut être déclaré terminé sans avoir passé une vérification indépendante et reproductible.

---

# 1. Expression du besoin

## 1.1 Contexte

Truth Engine dispose déjà d'un environnement agentique avancé :

* `AGENTS.md` ;
* orchestrateurs ;
* agents spécialisés ;
* prompts et frameworks cognitifs ;
* protocoles d'investigation ;
* KERNEL ;
* Mnemolite ;
* SUBLIMATOR ;
* contrôles déterministes ;
* agents reviewers/verifiers spécialisés.

Le contrat actuel impose déjà notamment :

* honnêteté absolue et anti-sycophancy ;
* double vérification des informations sensibles ;
* sourcing ;
* aveu explicite d'incertitude ;
* interdiction de prétendre avoir lu ou vérifié une ressource non consultée. 

Il contient également des invariants automatisables : conventions de nommage, règles typographiques, structure des investigations, exécution obligatoire du KERNEL, tests et gates spécialisés.  

Le problème n'est donc plus principalement **l'absence de règles**, mais **l'absence d'un mécanisme universel garantissant leur vérification avant livraison**.

Aujourd'hui, cette garantie repose encore trop souvent sur des rappels conversationnels :

```text
double check
KISS / DRY / YAGNI
no regression
vérifie tout
tu es sûr ?
review
fact-check
```

Cette méthode présente quatre faiblesses :

1. elle dépend de l'obéissance probabiliste du LLM ;
2. elle impose une intervention humaine répétitive ;
3. l'agent qui produit est souvent celui qui vérifie ;
4. aucune preuve technique n'empêche la livraison d'un état modifié après vérification.

---

# 2. Besoin fondamental

Transformer :

```text
« l'agent devrait vérifier son travail »
```

en :

```text
UNVERIFIED
    ↓
VERIFY
    ↓
PASS
    ↓
DELIVERABLE
```

La vérification doit devenir une **propriété du workflow**, et non une consigne rhétorique.

Le système doit répondre à l'invariant :

```text
NO VERIFIED STATE => NO FINAL DELIVERY
```

et à son corollaire :

```text
CHANGE AFTER PASS => PASS INVALID
```

---

# 3. Objectifs

## 3.1 Objectif principal

Tout travail modifiant Truth Engine doit subir automatiquement, avant livraison :

1. des contrôles déterministes ;
2. une revue indépendante ;
3. une vérification de non-régression ;
4. une vérification du respect du contrat projet ;
5. une certification de l'état exact ayant été examiné.

## 3.2 Objectifs secondaires

Le système doit :

* réduire drastiquement les demandes humaines de « double check » ;
* exploiter les capacités multi-agents natives de Codebuff ;
* séparer auteur et reviewer ;
* utiliser un contexte neuf pour la revue ;
* permettre au reviewer de consulter des thinkers/researchers si nécessaire ;
* isoler chaque chantier dans un worktree ;
* limiter les permissions des agents ;
* échouer explicitement plutôt que produire une fausse assurance ;
* rester simple à comprendre, auditer et maintenir.

## 3.3 Non-objectifs

La V1 ne doit pas chercher à :

* créer une plateforme CI/CD complète ;
* remplacer les tests existants ;
* attribuer des scores arbitraires sur 100 ;
* multiplier les personas ;
* créer une blockchain de certification ;
* introduire une PKI ou une signature cryptographique ;
* utiliser un consensus de dix LLM ;
* lancer systématiquement plusieurs reviewers ;
* réécrire KERNEL, SUBLIMATOR ou Mnemolite ;
* refactorer simultanément tout `AGENTS.md`.

---

# 4. Contraintes architecturales

## C1. Contrat canonique

La règle doit obligatoirement être inscrite dans le fichier de connaissance chargé par Codebuff.

Codebuff reconnaît `knowledge.md`, `AGENTS.md` et `CLAUDE.md`, avec priorité par répertoire :

```text
knowledge.md
> AGENTS.md
> CLAUDE.md
```

([Codebuff][1])

**Conséquence :**

si le projet utilise actuellement `AGENT.md` au singulier, le fichier canonique doit devenir :

```text
AGENTS.md
```

Il faudra également vérifier qu'aucun `knowledge.md` de même niveau ne masque les règles attendues.

---

# 5. Architecture cible

```text
                         UTILISATEUR
                             │
                             ▼
                     ORCHESTRATEUR
                             │
                     crée / sélectionne
                             │
                             ▼
                  WORKTREE DU CHANTIER
                    branche dédiée
                             │
                             ▼
                       AGENT AUTEUR
                             │
                        travaille
                             │
                             ▼
                    TRUTH-VERIFIER
                  gate programmatique
                             │
             ┌───────────────┴────────────────┐
             │                                │
             ▼                                ▼
     CONTRÔLES MACHINE                 TRUTH-REVIEWER
     déterministes                     session fraîche
             │                         lecture seule
             │                                │
             │                    ┌───────────┴──────────┐
             │                    ▼                      ▼
             │                 THINKER              RESEARCHER
             │               si nécessaire         si nécessaire
             │                    │                      │
             └────────────────────┴──────────┬───────────┘
                                             ▼
                                  PASS / FAIL / BLOCKED
                                             │
                                   ┌─────────┴─────────┐
                                   │                   │
                                 FAIL                PASS
                                   │                   │
                                   ▼                   ▼
                                REPAIR           STATE CHECK
                                   │                   │
                                   └── VERIFY ◄────────┤
                                                       │
                                                état identique
                                                       │
                                                       ▼
                                                   DELIVERY
```

---

# 6. Principe de séparation des responsabilités

Le système distingue trois rôles.

## 6.1 Auteur

L'auteur :

* comprend la mission ;
* modifie les fichiers ;
* exécute les tests nécessaires ;
* peut réparer les défauts ;
* ne peut pas certifier seul son propre travail.

## 6.2 Verifier

Le verifier :

* pilote le protocole ;
* exécute les vérifications déterministes ;
* construit les données nécessaires à la revue ;
* déclenche le reviewer indépendant ;
* agrège le verdict ;
* certifie l'état vérifié.

Il ne remplace pas le reviewer.

## 6.3 Reviewer

Le reviewer :

* examine ;
* contredit ;
* cherche les erreurs ;
* vérifie la conformité ;
* peut demander l'aide de spécialistes ;
* rend un verdict.

Il ne répare rien.

```text
AUTHOR != REVIEWER
```

---

# 7. Pourquoi ne pas utiliser simplement le reviewer Codebuff existant ?

Codebuff réalise déjà automatiquement des reviews et son architecture native repose sur plusieurs agents spécialisés. ([Codebuff][2])

Cependant, le reviewer natif actuel ne répond pas exactement au besoin de Truth Engine.

Sa définition actuelle contient :

```text
includeMessageHistory: true
spawnableAgents: []
```

Il hérite donc du contexte de la conversation qu'il critique et ne peut actuellement spawner aucun autre agent. Il est cependant déjà non-modificateur. ([Codebuff][3])

### Avantages du reviewer natif

* déjà disponible ;
* aucune maintenance ;
* rapide ;
* non-modificateur ;
* conçu pour la revue de code.

### Inconvénients

* contamination par l'historique de l'auteur ;
* connaissance des justifications de l'auteur ;
* risque accru de rationalisation ;
* pas de specialists spawnables ;
* essentiellement orienté code ;
* insuffisant pour investigations, documents, sources et raisonnements Truth Engine.

### Verdict

```text
Reviewer natif Codebuff :
utile comme contrôle supplémentaire
mais insuffisant comme autorité finale Truth Engine.
```

---

# 8. Reviewer Truth Engine dédié

Créer :

```text
.agents/truth-reviewer.ts
```

## 8.1 Propriété fondamentale

```typescript
includeMessageHistory: false
```

Codebuff documente cette propriété comme contrôlant explicitement l'héritage de l'historique du parent ; sa valeur par défaut est `false`. ([Codebuff][4])

Le reviewer reçoit donc un contexte propre.

---

# 9. Clean-room review

Le reviewer reçoit uniquement :

```text
MISSION
CONTRAT
CRITERES_ACCEPTATION
BASELINE
ETAT_COURANT
DIFF
FICHIERS_MODIFIES
RESULTATS_CONTROLES
```

Il ne reçoit pas :

```text
conversation de l'auteur
raisonnement de l'auteur
auto-évaluation de l'auteur
justifications
« normalement ça marche »
« j'ai choisi cela parce que... »
```

Schéma :

```text
AUTHOR CONTEXT
█████████████████████████
             │
             X  interdit
             │
             ▼
       TRUTH REVIEWER

INPUT REVIEWER
──────────────
mission
contrat
diff
fichiers
tests
preuves
```

L'objectif n'est pas de cacher les faits nécessaires à la revue, mais d'éliminer la contamination cognitive inutile.

---

# 10. Permissions du reviewer

Le reviewer doit être techniquement incapable de modifier le chantier via ses outils Codebuff.

Jeu d'outils recommandé :

```text
read_files
code_search
spawn_agents
set_output
end_turn
```

À exclure :

```text
write_file
str_replace
run_terminal_command
```

Le terminal est volontairement retiré : un terminal prétendument « read-only » reste capable d'exécuter des commandes destructrices.

Le verifier exécute les commandes nécessaires **avant** de transmettre les résultats au reviewer.

---

# 11. Agents que le reviewer peut spawner

Codebuff autorise explicitement chaque agent à définir les agents qu'il peut engendrer via `spawnableAgents`. Un agent ne peut donc pas librement appeler tout l'Agent Store : les descendants sont explicitement autorisés. ([Codebuff][4])

V1 :

```text
truth-reviewer
├── thinker
└── researcher
```

Rien d'autre.

Pas :

```text
editor
implementor
writer
committer
reviewer récursif
```

Le reviewer doit rester juge.

---

# 12. Thinker

Codebuff fournit plusieurs agents de raisonnement, dont `thinker`, `deep-thinker` et différentes variantes spécialisées. Le catalogue actuel les expose explicitement. ([Codebuff][5])

Le thinker natif actuel hérite de l'historique de son parent. ([Codebuff][6])

Ce comportement devient acceptable ici parce que son parent est justement le **reviewer clean-room**.

Ainsi :

```text
AUTHOR HISTORY
      X
      │
TRUTH REVIEWER
      │ contexte propre
      ▼
   THINKER
```

Le thinker n'hérite donc que du contexte propre du reviewer.

### Déclenchement

Ne pas lancer systématiquement le thinker.

Le reviewer le spawn uniquement lorsqu'un problème nécessite :

* raisonnement architectural ;
* analyse causale ;
* contradiction complexe ;
* recherche de cas limite ;
* arbitrage conceptuel.

---

# 13. Researcher

Le researcher doit être utilisé lorsqu'un verdict dépend d'une information externe :

* documentation technique ;
* API ;
* comportement d'une bibliothèque ;
* fait public ;
* source primaire ;
* affirmation sensible ;
* URL ou donnée évolutive.

Pour Truth Engine :

```text
FACT CLAIM + DOUBT
        ↓
researcher
        ↓
evidence
        ↓
review verdict
```

Le researcher ne doit pas être déclenché sur chaque modification triviale.

---

# 14. Verifier programmatique

Créer :

```text
.agents/truth-verifier.ts
```

Il doit utiliser le mécanisme programmatique Codebuff `handleSteps`.

Codebuff documente précisément `handleSteps` comme moyen de garantir des workflows déterministes, des embranchements et l'ordre des opérations plutôt que de compter sur un prompt. ([Codebuff][7])

C'est la primitive centrale du dispositif.

---

# 15. Fonctionnement du verifier

Pseudo-protocole :

```text
VERIFY(task)
{
    PRECHECK()

    state_before := HASH_WORKTREE()

    deterministic := RUN_CHECKS()

    if deterministic.FAIL:
        return FAIL

    review := SPAWN_FRESH_REVIEWER()

    if review.BLOCKED:
        return BLOCKED

    if review.FAIL:
        return FAIL

    state_after := HASH_WORKTREE()

    if state_before != state_after:
        return FAIL

    CERTIFY(state_after)

    return PASS
}
```

---

# 16. Une seule opération cognitive

Du point de vue de l'agent auteur :

```text
VERIFY
```

doit être une seule primitive.

Il ne doit pas décider lui-même :

```text
dois-je faire pytest ?
dois-je faire grep ?
dois-je lancer reviewer ?
dois-je faire un thinker ?
dois-je vérifier les URLs ?
```

Le verifier décide.

Conceptuellement :

```text
AUTHOR
  ↓
spawn truth-verifier
```

Une seule obligation.

---

# 17. Gate contractuel dans `AGENTS.md`

Ajouter une section courte, et seulement une section courte :

```text
## DELIVERY GATE

Tout travail modifiant le projet est UNVERIFIED par défaut.

Avant toute livraison finale, l'agent DOIT exécuter le gate
de vérification canonique du projet.

NO PASS => NO DELIVERY.

FAIL => réparer puis relancer la vérification complète.
BLOCKED => déclarer le blocage ; ne pas prétendre que le travail est validé.

Toute modification postérieure à PASS invalide immédiatement le PASS.

La revue finale doit être indépendante :
- reviewer en contexte neuf ;
- aucun historique de l'auteur ;
- reviewer sans permission d'écriture.

Le PASS doit correspondre exactement à l'état du chantier livré.
```

Pas de duplication du reste de `AGENTS.md`.

---

# 18. Contrôles déterministes

Tout ce qu'une machine peut vérifier ne doit pas être confié à un LLM.

Principe :

```text
DETERMINISTIC POSSIBLE
    => CODE

SEMANTIC JUDGMENT REQUIRED
    => REVIEWER
```

---

# 19. Contrôles globaux

Le verifier doit au minimum contrôler :

```text
Git valide
worktree valide
branche autorisée
état du projet récupérable
absence de modifications hors périmètre
tests applicables
syntaxe
schemas
invariants projet
```

---

# 20. Contrôles spécifiques Truth Engine

## 20.1 Convention de nommage

Le fichier projet définit déjà une convention machine-checkable pour `investigations/`, `articles/` et `outputs/`. 

Elle doit devenir un contrôle automatique.

Avant cela, une ambiguïté doit être corrigée dans la spécification actuelle :

```text
sujet = kebab-case
```

mais plusieurs exemples utilisent :

```text
reseaux_influence_elections
```

avec underscores. 

Le verifier ne doit jamais automatiser une règle contradictoire.

**Décision préalable nécessaire :**

```text
kebab-case
OU
snake_case
```

Une seule convention canonique.

---

# 21. Articles

Pour un fichier classé `ARTICLE` :

```text
CHECK article:
    U+2014 == 0
    naming == valid
    structure == valid
    links == parseable
```

La règle d'interdiction du tiret cadratin dans les articles est déjà explicitement définie. 

Le fact-check sémantique reste au reviewer/researcher.

---

# 22. Investigations

Pour une investigation :

```text
CHECK investigation:
    naming
    timestamp
    KERNEL execution markers
    BIAS TEST present
    15 symbols present
    FACT_REGISTRY present
    URLs formées
    GATE_CHECK present
```

Ces exigences proviennent déjà du contrat KERNEL. 

Attention :

```text
présence d'une section
!=
qualité de son contenu
```

Le script vérifie la structure.

Le reviewer vérifie le sens.

---

# 23. Mnemolite

Le contrat projet impose actuellement :

```text
get_system_snapshot
```

avant session, avec HALTE si Mnemolite est indisponible. 

Le verifier doit donc considérer :

```text
Mnemolite requis + DOWN
=> BLOCKED
```

et non :

```text
warning puis livraison
```

---

# 24. Tests existants

Truth Engine possède déjà des contrôles spécialisés, notamment SUBLIMATOR et ses tests. Le projet documente actuellement 26 tests sur les extracteurs ainsi qu'un `GATE_G`. 

Le nouveau gate ne doit pas recréer ces tests.

Il doit les **orchestrer**.

Principe DRY :

```text
VERIFY
  └── appelle les tests existants
```

et non :

```text
VERIFY
  └── réimplémente les tests existants
```

---

# 25. Vérification du scope

Un agent peut produire un résultat fonctionnel tout en modifiant des fichiers sans rapport avec la mission.

Le verifier doit donc comparer :

```text
SCOPE ATTENDU
vs
DIFF REEL
```

et détecter :

```text
unexpected files
deleted files
generated junk
temporary files
secrets
large unrelated changes
```

Un changement hors périmètre matériel entraîne :

```text
FAIL
```

---

# 26. Isolation par chantier

Principe :

```text
1 chantier
=
1 branche
=
1 worktree
=
1 cycle de vérification
```

Exemple :

```text
truth-engine/
│
└── .worktrees/
    ├── TE-184-sublimator/
    ├── TE-185-kernel/
    └── TE-186-investigation/
```

---

# 27. Worktree et sandbox ne sont pas synonymes

Point important :

```text
git worktree
!=
security sandbox
```

Un worktree isole efficacement :

* branches ;
* modifications ;
* diff ;
* historique du chantier.

Mais un processus disposant d'un terminal peut toujours, en principe, écrire ailleurs dans le système de fichiers.

Codebuff recommande lui-même Docker lorsque l'on veut limiter réellement l'accès terminal à une copie déterminée du dépôt. ([Codebuff][1])

---

# 28. Deux niveaux d'isolation

## Niveau 1 : standard

```text
worktree
+
permissions agents
+
scope checks
```

### Avantages

* simple ;
* rapide ;
* léger ;
* compatible workflow actuel ;
* très peu de friction.

### Inconvénient

Ce n'est pas une frontière de sécurité OS.

### Usage

Mode par défaut.

---

## Niveau 2 : hardened

```text
worktree
+
sandbox OS / container
+
mount RW du chantier
+
reste RO ou inaccessible
```

### Avantages

* vraie limitation des dégâts ;
* meilleure sécurité pour agents disposant d'un terminal.

### Inconvénients

* configuration supplémentaire ;
* intégration Mnemolite/MCP plus délicate ;
* réseau et credentials à gérer ;
* coût opérationnel supérieur.

### Décision

Ne pas rendre ce niveau obligatoire en V1, sauf chantier sensible.

---

# 29. Freebuff

Freebuff repose désormais explicitement sur le framework multi-agent Codebuff. Sa documentation indique que des agents spécialisés peuvent partager le travail, exécuter des commandes et reviewer le résultat. ([GitHub][8])

Freebuff Desktop documente également des espaces séparés pour les agents parallèles. ([GitHub][8])

Cela ne suffit toutefois pas à conclure que **Freebuff CLI fournit nativement un worktree Git sécurisé par chantier**.

La gestion explicite des worktrees doit donc rester dans notre architecture tant que cette propriété n'est pas documentée.

---

# 30. État vérifié : correction importante

Un certificat basé uniquement sur :

```text
git HEAD
```

est insuffisant.

Pourquoi ?

Parce qu'un agent travaille souvent avec :

```text
HEAD
+
modified tracked files
+
untracked files
```

Deux états différents peuvent donc partager le même HEAD.

---

# 31. STATE_ID

La certification doit porter sur l'état complet du chantier.

Définir :

```text
STATE_ID :=
HASH(
    HEAD
    + tracked_diff
    + untracked_file_names
    + untracked_file_hashes
)
```

Exemple conceptuel :

```text
HEAD
a812cf...

DIFF
src/a.py changed
docs/x.md changed

UNTRACKED
tests/new_test.py => sha256(...)
```

puis :

```text
STATE_ID = SHA256(canonical_state)
```

---

# 32. Invalidation

Après :

```text
VERIFY => PASS
```

si un seul octet change :

```text
STATE_ID_NEW != STATE_ID_VERIFIED
```

alors :

```text
VERIFICATION_STALE
```

et :

```text
DELIVERY FORBIDDEN
```

jusqu'au prochain VERIFY.

---

# 33. Certificat minimal

Fichier :

```text
.verify/result.json
```

Exemple :

```json
{
  "schema": 1,
  "task": "TE-186",
  "verdict": "PASS",
  "head": "a812cf...",
  "state_id": "sha256:91bd...",
  "deterministic": "PASS",
  "review": "PASS"
}
```

YAGNI :

pas de signature cryptographique en V1.

---

# 34. Verdicts

Trois états uniquement :

```text
PASS
FAIL
BLOCKED
```

## PASS

Aucun défaut matériel identifié.

## FAIL

Un défaut démontrable doit être corrigé.

## BLOCKED

La vérification ne peut pas aboutir correctement :

* source indispensable inaccessible ;
* Mnemolite indisponible ;
* tests impossibles ;
* ambiguïté contractuelle ;
* donnée requise absente ;
* erreur d'infrastructure.

`BLOCKED` est essentiel pour empêcher le LLM de convertir artificiellement :

```text
« je ne peux pas vérifier »
```

en :

```text
« probablement bon »
```

---

# 35. Pas de score

Interdits :

```text
93/100
confiance 97 %
quality score 8.7
```

sauf métrique objective existante du projet.

Un LLM n'est pas un instrument calibré permettant de transformer son impression en probabilité fiable.

---

# 36. Sortie du reviewer

Sortie structurée minimale :

```json
{
  "verdict": "FAIL",
  "findings": [
    {
      "location": "src/foo.py:84",
      "problem": "La condition inverse le comportement attendu.",
      "evidence": "Le test X exige A mais le code retourne B."
    }
  ]
}
```

Pour `PASS` :

```json
{
  "verdict": "PASS",
  "findings": []
}
```

Pour `BLOCKED` :

```json
{
  "verdict": "BLOCKED",
  "findings": [
    {
      "problem": "Impossible de vérifier la source primaire."
    }
  ]
}
```

---

# 37. Critères du reviewer

Le reviewer doit rechercher prioritairement :

```text
correctness
completeness
contract compliance
scope violations
regressions
fabrication
unsupported claims
missing evidence
hidden assumptions
contradictions
dead code
unnecessary complexity
DRY violations
YAGNI violations
failure modes
```

Le but n'est pas de produire un commentaire éditorial général.

Le but est de trouver ce qui empêcherait rationnellement la livraison.

---

# 38. Boucle de réparation

```text
AUTHOR
   │
   ▼
VERIFY
   │
   ├── PASS ─────────────► DELIVER
   │
   ├── BLOCKED ──────────► STOP
   │
   └── FAIL
        │
        ▼
      REPAIR
        │
        ▼
      VERIFY
```

La vérification doit être intégrale après réparation.

Pas :

```text
« j'ai corrigé uniquement le point signalé,
donc l'ancien PASS reste valable »
```

---

# 39. Pourquoi une nouvelle revue après correction ?

La correction d'un défaut peut :

* créer une nouvelle régression ;
* modifier un invariant ;
* toucher un autre fichier ;
* invalider une conclusion précédente.

Donc :

```text
NEW STATE
=> NEW REVIEW
```

---

# 40. Options d'architecture étudiées

## Solution A : règles supplémentaires dans `AGENTS.md`

```text
AGENTS.md
→ « pense à vérifier »
```

### Avantages

* coût presque nul ;
* immédiat.

### Inconvénients

* probabiliste ;
* contournable ;
* auto-review ;
* aucune preuve ;
* aucune certification de l'état.

### Verdict

**Rejetée comme solution principale.**

Le contrat reste nécessaire, mais pas suffisant.

---

# 41. Solution B : reviewer Codebuff natif

```text
AUTHOR
→ codebuff/reviewer
```

### Avantages

* natif ;
* rapide ;
* zéro développement ;
* déjà intégré au workflow Codebuff.

### Inconvénients

* hérite actuellement de l'historique ;
* reviewer conçu essentiellement pour le code ;
* aucune orchestration Truth Engine ;
* aucun thinker/researcher spawnable dans sa définition actuelle. ([Codebuff][3])

### Verdict

**Contrôle complémentaire, pas gate final.**

---

# 42. Solution C : reviewer Truth Engine personnalisé

```text
AUTHOR
→ truth-reviewer(clean)
```

### Avantages

* contexte neuf ;
* permissions maîtrisées ;
* spécialisé Truth Engine ;
* sortie structurée ;
* peut consulter thinker/researcher.

### Inconvénient

Si l'auteur doit simplement « penser à le lancer », l'enforcement reste partiellement contractuel.

### Verdict

**Nécessaire mais incomplet seul.**

---

# 43. Solution D : verifier programmatique Codebuff

```text
AUTHOR
→ truth-verifier
   → machine checks
   → truth-reviewer
   → verdict
```

Codebuff fournit précisément les agents programmatiques et `handleSteps` pour imposer l'ordre des opérations. ([Codebuff][7])

### Avantages

* natif Codebuff ;
* ordre déterministe ;
* faible duplication ;
* peut spawner agents ;
* peut gérer FAIL/BLOCKED ;
* exploite les capacités existantes ;
* pas besoin d'un framework externe.

### Inconvénients

* petite quantité de TypeScript à maintenir ;
* l'orchestrateur principal doit réellement imposer son invocation.

### Verdict

**Solution recommandée.**

---

# 44. Solution E : verifier externe via SDK

Codebuff permet de lancer programmatiquement n'importe quel agent via `@codebuff/sdk`, y compris des agents locaux, et documente explicitement les usages CI/CD et automatisation. ([Codebuff][9])

Architecture :

```text
tools/verify.ts
    ↓
Codebuff SDK
    ↓
truth-reviewer
```

### Avantages

* processus réellement séparé ;
* intégrable CI ;
* facile à automatiser hors session Codebuff.

### Inconvénients

* API key nécessaire pour le SDK documenté ;
* dépendance Node/SDK ;
* nouvelle couche d'exécution ;
* complexité inutile pour la V1 interactive.

### Verdict

**À réserver à une V2/CI si nécessaire.**

---

# 45. Solution retenue

```text
AGENTS.md
+
worktree par chantier
+
truth-verifier programmatique
+
truth-reviewer clean-room
+
thinker/researcher facultatifs
+
STATE_ID
```

C'est le meilleur compromis :

```text
simplicité
×
robustesse
×
indépendance
×
intégration Codebuff
```

---

# 46. Enforcement final

Il existe deux niveaux.

## Niveau A : contrat

`AGENTS.md` impose :

```text
NO VERIFY => NO DELIVERY
```

## Niveau B : orchestration

L'orchestrateur empêche matériellement son workflow normal de se terminer avant le verdict.

Cible finale :

```text
IMPLEMENT
   ↓
VERIFY
   ↓
IF FAIL:
    REPAIR
    GOTO VERIFY

IF BLOCKED:
    STOP

IF PASS:
    DELIVER
```

Le niveau B est préférable parce que Codebuff documente justement la possibilité de rendre des étapes déterministes avec ses agents programmatiques. ([Codebuff][2])

---

# 47. Arborescence cible minimale

```text
Truth-engine/
│
├── AGENTS.md
│
├── .agents/
│   ├── truth-verifier.ts
│   └── truth-reviewer.ts
│
├── tools/
│   └── verify/
│       └── checks existants ou glue minimale
│
├── .verify/
│   └── result.json
│
└── .worktrees/
    └── <chantier>/
```

Ne pas multiplier les fichiers avant nécessité réelle.

---

# 48. Gestion de RTK

Le contrat actuel impose RTK pour la majorité des commandes terminal. 

Le verifier doit respecter ces règles lorsqu'elles sont pertinentes.

Cependant, le protocole de vérification lui-même constitue une abstraction :

```text
AUTHOR
→ VERIFY
```

L'auteur ne doit pas connaître ni répéter la séquence interne des commandes.

Cela évite de transformer :

```text
double check
```

en :

```text
rtk grep...
rtk pytest...
rtk git...
...
```

Le problème serait simplement déplacé.

---

# 49. Scénarios d'acceptation

## AC-01 : modification correcte

```text
agent modifie
→ checks PASS
→ reviewer PASS
→ state inchangé
→ certificat PASS
→ livraison
```

Résultat attendu :

```text
PASS
```

---

## AC-02 : tests en échec

```text
agent modifie
→ deterministic FAIL
```

Le reviewer n'est pas lancé inutilement.

Résultat :

```text
FAIL
```

---

## AC-03 : régression sémantique

Tests :

```text
PASS
```

mais reviewer détecte une erreur logique.

Résultat :

```text
FAIL
```

---

## AC-04 : modification post-review

```text
VERIFY PASS
→ agent modifie un caractère
→ STATE_ID change
```

Résultat :

```text
VERIFICATION_STALE
NO DELIVERY
```

---

## AC-05 : fichier non suivi

L'agent crée :

```text
new_test.py
```

non ajouté à Git.

Le fichier doit quand même entrer dans `STATE_ID`.

Résultat :

```text
état correctement certifié
```

---

## AC-06 : reviewer tente d'écrire

Il ne possède pas les outils d'édition.

Résultat :

```text
écriture impossible par design
```

---

## AC-07 : doute conceptuel

Reviewer :

```text
spawn thinker
```

Thinker retourne son analyse.

Reviewer reste seul responsable du verdict.

---

## AC-08 : fait externe douteux

Reviewer :

```text
spawn researcher
```

Researcher apporte les sources.

Reviewer tranche :

```text
PASS | FAIL | BLOCKED
```

---

## AC-09 : Mnemolite indisponible

Si le workflow exige Mnemolite :

```text
get_system_snapshot => DOWN
```

Résultat :

```text
BLOCKED
```

conformément au contrat existant. 

---

## AC-10 : agent sur branche protégée

Tentative de chantier directement sur :

```text
main
master
```

Résultat attendu selon politique retenue :

```text
BLOCKED
```

---

# 50. Critères de réussite

La V1 est considérée opérationnelle si :

1. l'auteur n'a qu'une primitive de vérification à connaître ;
2. le reviewer ne voit pas l'historique auteur ;
3. le reviewer ne peut pas écrire ;
4. les contrôles déterministes précèdent le reviewer ;
5. les erreurs déterministes empêchent la consommation d'une review inutile ;
6. toute correction invalide le PASS ;
7. les fichiers non suivis participent à l'identité de l'état ;
8. un état non vérifié ne peut pas être présenté comme terminé ;
9. FAIL provoque une nouvelle boucle complète ;
10. BLOCKED ne peut jamais être converti implicitement en PASS.

---

# 51. Risques

## R1. Fausse indépendance du reviewer

**Cause :**

```text
includeMessageHistory: true
```

**Mitigation :**

```text
false obligatoire
```

---

## R2. Reviewer disposant d'un terminal

**Risque :** mutation accidentelle.

**Mitigation :**

aucun `run_terminal_command`.

---

## R3. Explosion agentique

```text
reviewer
→ thinker
→ thinker
→ reviewer
→ researcher
→ ...
```

**Mitigation :**

liste fermée :

```text
truth-reviewer
├── thinker
└── researcher
```

---

## R4. Coût excessif

**Mitigation :**

```text
machine checks first
reviewer second
specialists only on demand
```

---

## R5. Faux PASS après changement

**Mitigation :**

`STATE_ID`.

---

## R6. Rules drift

Le contrat évolue mais les checks restent anciens.

**Mitigation :**

tests du verifier + référence claire entre invariant et check.

Pas de duplication massive du texte de `AGENTS.md`.

---

## R7. Overengineering

**Mitigation :**

V1 limitée à :

```text
2 agents
1 gate
1 state id
1 certificat
1 worktree / chantier
```

---

# 52. Ordre d'implémentation recommandé

## Étape 0 : assainissement minimal

Avant de coder :

* confirmer `AGENTS.md` ;
* vérifier absence de `knowledge.md` contradictoire ;
* résoudre `kebab-case` vs underscores ;
* résoudre toute ambiguïté directement nécessaire au verifier.

Ne pas refactorer le reste.

---

## Étape 1 : reviewer

Créer :

```text
truth-reviewer.ts
```

avec :

```text
includeMessageHistory = false
read-only
structured output
spawn thinker
spawn researcher
```

Le tester manuellement.

---

## Étape 2 : deterministic gate

Implémenter les quelques contrôles universels :

```text
git
scope
tests
naming
project invariants
```

Réutiliser les scripts existants.

---

## Étape 3 : STATE_ID

Implémenter :

```text
HEAD
+
diff
+
untracked hashes
```

Puis vérifier l'invalidation après modification.

---

## Étape 4 : truth-verifier

Créer l'agent programmatique :

```text
precheck
→ deterministic
→ reviewer
→ state check
→ certificate
```

---

## Étape 5 : AGENTS.md

Ajouter uniquement le contrat DELIVERY GATE.

---

## Étape 6 : worktrees

Imposer :

```text
1 chantier = 1 worktree
```

dans le launcher/orchestrateur existant.

---

## Étape 7 : enforcement orchestrateur

Une fois les composants éprouvés :

```text
orchestrator cannot finalize
unless verifier == PASS
```

---

# 53. Ce qu'il ne faut pas construire maintenant

Ne pas ajouter en V1 :

```text
multi-review consensus
reviewer voting
quality scoring
complex policy DSL
distributed locks
database
dashboard web
cryptographic signing
automatic PR workflow
full container orchestration
20 reviewer personas
```

Tout cela pourra être ajouté uniquement si un problème réel le justifie.

---

# 54. Vision finale

Le changement recherché est conceptuellement simple.

### Avant

```text
USER
  ↓
« fais »
  ↓
AGENT
  ↓
RESULTAT
  ↓
USER
  ↓
« double check »
  ↓
AGENT
  ↓
« oui »
```

### Après

```text
USER
  ↓
TASK
  ↓
AGENT
  ↓
WORK
  ↓
VERIFY
  ├── machine
  └── independent reviewer
          ├── thinker ?
          └── researcher ?
  ↓
PASS
  ↓
STATE VALID
  ↓
DELIVERY
```

L'utilisateur n'a plus à être le système qualité.

---

# 55. Contrat architectural final

```text
INVARIANTS :=

TASK_MUTATION
    => ISOLATED_WORKTREE

FINAL_DELIVERY
    => VERIFIED_STATE

VERIFIED_STATE
    => DETERMINISTIC_CHECKS_PASS
    AND INDEPENDENT_REVIEW_PASS

INDEPENDENT_REVIEW
    => FRESH_CONTEXT
    AND READ_ONLY

REVIEWER
    => MAY_SPAWN[THINKER, RESEARCHER]
    AND MAY_NOT_SPAWN[EDITOR, AUTHOR]

CHANGE
    AFTER VERIFY_PASS
    => VERIFICATION_INVALID

UNVERIFIABLE
    => BLOCKED

FAIL
    => REPAIR
    => FULL_VERIFY

NO_PASS
    => NO_DELIVERY
```

---

# 56. Synthèse de décision

La solution recommandée n'est ni un nouveau prompt, ni un nouveau framework cognitif.

Elle ajoute une **frontière de qualité obligatoire** autour de ceux qui existent déjà :

```text
AGENTS.md
       ↓
WORKTREE
       ↓
AUTHOR
       ↓
TRUTH-VERIFIER
       ├── deterministic checks
       └── TRUTH-REVIEWER
              ├── thinker
              └── researcher
       ↓
STATE_ID
       ↓
PASS
       ↓
DELIVERY
```

Le système reste volontairement petit :

```text
1 contrat
1 worktree
1 verifier
1 reviewer
2 spécialistes facultatifs
3 verdicts
1 identité d'état
```

C'est suffisant pour faire passer la vérification de **discipline conversationnelle** à **mécanisme d'exécution vérifiable**, sans reconstruire une nouvelle usine à gaz au-dessus de Truth Engine.

[1]: https://www.codebuff.com/docs/help/faq "help | Codebuff Docs | Codebuff"
[2]: https://www.codebuff.com/docs/agents/overview "agents | Codebuff Docs | Codebuff"
[3]: https://www.codebuff.com/publishers/codebuff/agents/reviewer "reviewer v0.0.11 - Agent Details | Codebuff"
[4]: https://www.codebuff.com/docs/agents/agent-reference "agents | Codebuff Docs | Codebuff"
[5]: https://www.codebuff.com/publishers/codebuff "Codebuff - Codebuff Publisher | Codebuff"
[6]: https://www.codebuff.com/publishers/codebuff/agents/thinker "thinker v0.0.6 - Agent Details | Codebuff"
[7]: https://www.codebuff.com/docs/agents/creating-new-agents "agents | Codebuff Docs | Codebuff"
[8]: https://github.com/CodebuffAI/codebuff/blob/main/README.md "freebuff/README.md at main · CodebuffAI/freebuff · GitHub"
[9]: https://www.codebuff.com/docs/advanced/sdk "advanced | Codebuff Docs | Codebuff"


---


Après double check, je **corrige ma réponse précédente** : ajouter un `§18c` dans le KERNEL dès maintenant serait trop intrusif et risquerait de mélanger deux niveaux de vérification.

Le KERNEL v2.8 possède déjà une chaîne interne cohérente : §13 vérifie les sources, contradictions, provenance et traces ; §18 applique G0-G8 ; §18b corrige, reconstruit puis applique G9-G10 avant §19 SAVE.   **Il ne faut pas dupliquer cette logique avec des reviewers à l'intérieur.**

### Architecture KISS

```text
                AGENTS.md
                    │
                    ▼
              AGENT / CODEBUFF
                    │
                    ▼
                 KERNEL
          ┌─────────┴─────────┐
          │ vérification      │
          │ interne existante │
          │                   │
          │ §13 VERIFY        │
          │ §18 GATES         │
          │ §18b CORRECT      │
          │ §19 SAVE          │
          └─────────┬─────────┘
                    │
                    ▼
            TRUTH-REVIEWER
              session neuve
                    │
             ┌──────┴──────┐
             │             │
          thinker ?    researcher ?
             │             │
             └──────┬──────┘
                    ▼
          PASS / FAIL / BLOCKED
                    │
          ┌─────────┴─────────┐
          │                   │
        FAIL                PASS
          │                   │
          ▼                   ▼
    retour auteur          DELIVERY
    correction
          │
          └────────► KERNEL/VERIFY
```

**Donc, en V1 : les nouveaux agents de vérification ne s'immiscent nulle part dans les étapes 0-19a du KERNEL.**

Ils sont **au-dessus**, comme gate de livraison.

C'est aussi cohérent avec Codebuff : son architecture actuelle sait déjà orchestrer auteur → reviewer → tests et ses agents peuvent être spécialisés/spawnés. ([Codebuff][1])

### Mais il reste un problème réel

Le KERNEL sauvegarde actuellement en §19 et effectue le `FACT_WRITEBACK` en §19a. 

Donc avec l'architecture V1 :

```text
KERNEL SAVE
→ REVIEW EXTERNE
→ éventuellement FAIL
```

Un reviewer pourrait découvrir une erreur **après persistance**.

Ce n'est pas parfait.

Mais je ne modifierais **pas immédiatement** le KERNEL pour résoudre ça. Ce serait introduire une dépendance agentique nouvelle dans un pipeline v2.8 déjà fortement contraint simplement sur hypothèse.

### Évolution éventuelle, après validation de la V1

Si les tests montrent que le reviewer externe détecte réellement des erreurs importantes échappant à G0-G10, alors seulement on introduit **un unique hook**, pas une nouvelle phase complexe :

```text
18b GATE_AUTO
      │
      ▼
 FINAL_CANDIDATE
      │
      ▼
EXTERNAL_REVIEW_GATE
      │
   PASS ?
  /     \
NO       YES
│         │
18b      §19 SAVE
```

Le KERNEL ne saurait pas ce qu'est un thinker, un researcher ou un reviewer.

Il connaîtrait seulement :

```text
EXTERNAL_REVIEW_GATE => PASS | FAIL | BLOCKED
```

**C'est beaucoup plus propre.**

Le sous-système de review resterait extérieur :

```text
EXTERNAL_REVIEW_GATE
        │
        ▼
 truth-reviewer
      ├── thinker ?
      └── researcher ?
```

Cela conserve la séparation :

```text
KERNEL
= produit + vérifie une investigation

REVIEW SYSTEM
= attaque indépendamment le résultat

AGENTS.md
= impose que les deux passent avant livraison
```

### Verdict après double check

Je recommande donc maintenant :

**V1**

```text
KERNEL inchangé
      ↓
review indépendante
      ↓
PASS
      ↓
livraison
```

Puis uniquement si la V1 démontre le besoin :

**V2**

```text
KERNEL §18b
      ↓
unique EXTERNAL_REVIEW_GATE
      ↓
§19 SAVE
```

Pas de reviewer entre §9 et §10, pas de thinker dans §11, pas de reviewer supplémentaire en §13, pas de multiplication des gates.

C'est le meilleur compromis **KISS + DRY + no regression** : ton KERNEL conserve sa responsabilité et son déterminisme ; la nouvelle architecture ajoute une vraie red team indépendante sans contaminer son fonctionnement.

[1]: https://www.codebuff.com/publishers/codebuff/agents/base2-max/0.0.24?utm_source=chatgpt.com "base2-max v0.0.24 - Agent Details"
