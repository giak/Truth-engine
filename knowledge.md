# Truth Engine — Project Knowledge

> Rules that govern ALL agent behavior in this project. Read and apply before every task.

## DELIVERY GATE (OBLIGATOIRE)

Tout travail modifiant le projet est UNVERIFIED par défaut.

Avant toute livraison finale, l'agent DOIT exécuter le gate de vérification canonique :

- Codebuff : spawn l'agent `truth-verifier` (`.agents/truth-verifier.ts`).
- Hors Codebuff : `python3 tools/verify/verify.py check` puis `verify.py certify --review <verdict>`.

`NO PASS => NO DELIVERY`.

**Investigations KERNEL** : le pipeline `truth-engine-v2/KERNEL.md` est câblé à la gate. L'étape `19b GATE_VERIFY` impose, après le FREEZE (§18b) et le SAVE (§19), de lancer `python3 tools/verify/verify.py check` sur l'état livré :

- `PASS` → livraison autorisée, STATE_ID enregistré dans le manifeste.
- `FAIL` → corriger le livrable (nommage/em-dash), re-FREEZE, re-SAVE, re-run 19b. Jamais de livraison en FAIL.
- `BLOCKED` (branche protégée `main`/`master`) → le chantier DOIT être déplacé dans un worktree (`tools/verify/worktree-new.sh <chantier>`), jamais certifié sur `main`.

- `FAIL` : réparer puis relancer la vérification complète.
- `BLOCKED` : déclarer le blocage ; ne pas prétendre que le travail est validé.
- Toute modification postérieure à `PASS` invalide immédiatement le `PASS` (STATE_ID).

La revue finale doit être indépendante :

- reviewer en contexte neuf (`includeMessageHistory: false`) ;
- aucun historique de l'auteur ;
- reviewer sans permission d'écriture.

Le `PASS` doit correspondre exactement à l'état du chantier livré.

Isolation : `1 chantier = 1 worktree = 1 branche = 1 cycle de vérification`. Créer le chantier via `tools/verify/worktree-new.sh <chantier>` (dossier `.worktrees/<chantier>`). Jamais de chantier directement sur `main`/`master`.

Règles du projet (branches protégées, tests, contrôles) : `.verify/config.json`.

## Éthique de la vérité (IMPÉRATIF)

### 1. Absolute Honesty & Anti-sycophancy

- **Zéro flagornerie** : interdiction absolue de flatter l'utilisateur, de valider des idées fausses pour être « poli », ou d'utiliser des fioritures sociales (« Je suis ravi de vous aider », « Excellente question »).
- **Priorité à l'exactitude** : en cas de conflit entre la politesse et la vérité, choisir systématiquement la vérité brute et froide.
- **Droit de contradiction** : si l'utilisateur propose une théorie, une date ou un fait erroné, le contredire factuellement avec preuves à l'appui.
- Interdiction des formules comme « je te prie de m'excuser », « merci de me l'avoir signalé », « bonne question », « excellent point ».

### 2. Anti-hallucination & Fact-checking

- **Double Check Systématique** : avant de valider une information sensible (dates, chiffres, noms propres), effectuer une recherche web ou une vérification dans le système de fichiers.
- **Sourcing Primaire** : baser les réponses sur des données vérifiables. Citer les sources (URLs, fichiers, rapports).
- **Aveu d'ignorance** : si une information est manquante ou incertaine, le déclarer explicitement. Interdiction d'inventer de la confiance. Formules autorisées : « Les données disponibles ne permettent pas de conclure », « Je ne sais pas ».
- **Chaîne de Pensée (CoT)** : pour les problèmes complexes, décomposer le raisonnement étape par étape pour identifier les biais potentiels.
- Toute fabrication (affirmation sans source, chiffre inventé, événement inventé) est une violation grave.

### 3. Directness & Standalone Power

- **Style direct** : aller droit au but. Supprimer les introductions et les conclusions inutiles.
- **Standalone Results** : produire des résultats prêts à publier sans retouche.
- **Vérité médico-légale** : chaque tâche est une expertise forensique ; la précision à la virgule près est la norme.

### 3.5 Principe

LLM = échantillonneur stochastique : à prompt et template identiques, la sortie varie par construction (clés JSON ajoutées, modifiées, omises). Un parser déterministe consomme une grammaire close et finie, or la grammaire LLM effective est elle-même échantillonnée et non énumérable : le parser ne peut que constater la réalisation, jamais la prédire.

### 4. Anti-fausse-précision

Un script déterministe (regex, parseur string-strict) ne doit pas traiter du texte produit par un LLM.

## Règles de formatage critiques

### Interdiction du tiret cadratin dans les articles

- **Scope strict :** articles publiés (Phase 3) uniquement. Ne JAMAIS appliquer aux fiches internes (quintessences Phase 1, INVESTIGATIONS sources).
- Ne jamais utiliser le tiret cadratin (em dash U+2014, « — ») dans les articles.
- Utiliser « : » pour les séparateurs, « - » pour les listes, et des parenthèses pour les incises.
- Faire un grep de « — » sur le fichier avant de déclarer un article terminé.
- **Audit script** `tools/audit_phase1_sublimator_v35.py` : C3 « zéro em-dash » **NEUTRALISÉ** 2026-07-08 (informatif uniquement, hors score). Le scope originel articles/Phase 3 a été corrigé : les fiches internes Phase 1 tolèrent l'em-dash. Pour audit Phase 3 (articles), créer un script séparé `audit_phase3_em_dash.py` (à venir).

### Sourcing et fact-checking

- Avant de valider une information sensible, faire une recherche web ou dans les fichiers. Citer les sources.
- Si l'information manque : le dire. Formules autorisées : « Les données disponibles ne permettent pas de conclure », « Je ne sais pas ».
- Toute fabrication (affirmation sans source, chiffre inventé, événement inventé) est une violation grave.

#### Récupération web, accès bloqué et dérive de contenu

Un échec d'outil n'est pas un verdict : `403`, timeout, page JavaScript, paywall ou résultat vide de `web_search` ne prouvent ni source morte, ni donnée absente, ni claim réfuté.

Après un échec, appliquer `truth-engine-v2/protocol/FACT_VERIFICATION.md` §4.7 : variante canonique, navigateur ou Chrome headless, puis au plus trois recherches ciblées. Toute URL de remplacement doit être lue. À défaut, consigner un extrait manuel borné avec URL, section, date et méthode.

Snippet, résultat de recherche, mémoire Mnemolite, synthèse locale et copie interne ne remplacent jamais l'extrait primaire. Une page modifiée produit une dérive à journaliser, pas une réécriture silencieuse. Une absence dans une page non exhaustive produit `NO_ASSERTION`, pas `REFUTED`.

Aucun write-back à L0 : `EXCERPT_OK` + gate applicable seulement, `VERIFIE` à L1-L3, `CONFIRME` à L4.

### Vérification pré-affirmation

- N'affirmer avoir lu, vérifié, ou analysé un fichier que si un tool call `read` ou `grep` le prouve dans la session.
- « J'ai parcouru X articles » sans `read` correspondant = fabrication.
- Toute affirmation sur le contenu d'un fichier non lu doit être précédée de « Je n'ai pas lu ce fichier, je déduis de son titre que... »

## RTK : Optimisation Token (OBLIGATOIRE)

**RTK (Rust Token Killer)** est un proxy CLI qui réduit la consommation de tokens de 60 à 90 % en compressant la sortie des commandes shell avant qu'elle n'atteigne le LLM.

### Règle fondamentale

**TOUJOURS préfixer les commandes shell avec `rtk`** quand tu utilises l'agent `basher` ou tout outil exécutant des commandes terminal.

```
❌ PROHIBÉ (commande brute) :
command: "ls -la src/"
command: "grep -r 'pattern' ."
command: "git status"
command: "cat fichier.json"
command: "find . -name '*.ts'"

✅ OBLIGATOIRE (préfixer avec rtk) :
command: "rtk ls src/"
command: "rtk grep -r 'pattern' ."
command: "rtk git status"
command: "rtk read fichier.json"
command: "rtk find . -name '*.ts'"
```

**Note :** RTK gère ses propres flags de formatage. Les flags d'affichage natifs (`-la`, `--color`) sont ignorés ou adaptés par RTK.

### Commandes RTK disponibles

| Commande native | Équivalent RTK | Économie typique |
|----------------|----------------|------------------|
| `ls` | `rtk ls` | 70-80% |
| `cat` | `rtk read` | 60-80% |
| `grep` | `rtk grep` | 80-95% |
| `git status/log/diff` | `rtk git status` | 70-90% |
| `find` | `rtk find` | 75-85% |
| `tree` | `rtk tree` | 80-90% |
| `docker logs/ps` | `rtk docker logs` | 85-95% |
| `curl` | `rtk curl` | 60-80% (auto JSON schema) |
| `npm/pnpm` | `rtk pnpm` | 60-70% |
| `cargo` | `rtk cargo` | 60-70% |
| `pytest/vitest` | `rtk pytest` / `rtk vitest` | 70-85% (failures only) |
| `tsc/mypy` | `rtk tsc` / `rtk mypy` | 70-80% (grouped errors) |

### Commandes meta RTK

- `rtk gain` : afficher les économies totales de tokens
- `rtk gain --history` : historique des commandes avec économies
- `rtk gain --graph` : graphique ASCII sur 30 jours
- `rtk discover` : trouver les économies manquées dans l'historique
- `rtk proxy <cmd>` : exécuter la commande brute sans filtrage (debug uniquement)
- `rtk smart <cmd>` : résumé technique en 2 lignes (heuristique)
- `rtk summary <cmd>` : résumé heuristique de la sortie
- `rtk err <cmd>` : n'afficher que les erreurs/warnings

### Exceptions (PAS de préfixe rtk)

- Commandes avec effets de bord critiques : `git add`, `git commit`, `git push`, `npm install`, `pip install`, `mkdir`, `cp`, `mv`, `rm`
- Commandes interactives : `vim`, `htop`, `less`
- Commandes dont tu as besoin de la sortie complète non filtrée (rare, utiliser `rtk proxy <cmd>` si besoin)

## Compression Contexte (Headroom)

**CTX:** headroom MCP serveur disponible — compresser les tool outputs volumineux.

- Si tool output > 1000 tokens : appeler `headroom_compress` sur le contenu.
- `headroom_compress` supporte JSON/texte, préserve erreurs/anomalies.
- Si besoin de détail supplémentaire : `headroom_retrieve(hash)`.
- `headroom_stats` pour économies session.
- `memory_search` / `memory_save` pour mémoire persistante cross-agent.

## ANTI-PATTERN : Appels tool `write()` (OBLIGATOIRE)

**JAMAIS appeler `write()` sans les DEUX paramètres `content` et `filePath`.**

```
❌ PROHIBÉ — ces appels RETOURNERONT UNE ERREUR :
write()
write(content="...")
write(filePath="...")

✅ OBLIGATOIRE — TOUJOURS les deux paramètres :
write(content="le texte complet ici", filePath="/chemin/vers/fichier.md")
```

**Règle de fer :**

- `content=` DOIT être une string non-vide (le texte complet du fichier)
- `filePath=` DOIT être un chemin absolu
- Si le texte est long (>1000 mots), le contenu va DANS `content=`, jamais ailleurs
- Si `content` est manquant → l'outil retourne une erreur → le pipeline est cassé
- RELIS ton appel `write()` AVANT de l'exécuter. Vérifie que `content=` et `filePath=` sont tous deux présents.

**Pattern d'échec connu :** le LLM génère parfois `write()` comme placeholder puis oublie de remplir les paramètres. **TOUJOURS construire l'appel complet en une seule passe.**

### BUG DOCUMENTÉ : `write()` échoue silencieusement avec contenu long

**Symptôme :** `write()` retourne `"expected string, received undefined"` même quand `content=` et `filePath=` sont explicitement fournis. Les appels `bash()` avec commandes longues échouent aussi.

**Cause :** quand le paramètre `content=` dépasse ~5000 caractères, la génération XML du LLM casse les valeurs de paramètres. Les balises sont produites mais VIDES — les valeurs ne sont pas émises. Ceci est un défaut de génération du LLM, pas de l'outil.

**Solution — STRATÉGIE WRITE+EDIT :**

```
ÉTAPE 1: write() avec première section seulement (≤3000 chars)
  write(content="# TITRE\n\n## §0 PREMIÈRE SECTION\n...", filePath="/chemin/fichier.md")

ÉTAPE 2: edit() pour ajouter chaque section suivante
  edit(oldString="dernière ligne existante", newString="dernière ligne\n\n## §1 SUITE\n...", filePath="/chemin/fichier.md")

ÉTAPE 3: Répéter edit() jusqu'au fichier complet
```

**Règles de la stratégie :**

1. **Segmenter** — découper le contenu en blocs de ≤3000 caractères
2. **Écrire le premier bloc** avec `write()` (titre + §0)
3. **Éditer pour le reste** — chaque `edit()` ajoute une section en remplaçant la dernière ligne
4. **`oldString`** = dernière ligne du fichier courant (unique pour éviter les doublons)
5. **`newString` = oldString + "\n\n" + nouveau contenu**
6. **Vérifier** après chaque `edit()` que le contenu est bien ajouté

**NE JAMAIS :** tenter un `write()` de >5000 caractères en une passe. Ça échouera et gaspillera des tours de conversation.

## Convention de nommage (OBLIGATOIRE)

### Format obligatoire

Tous les fichiers dans les dossiers `investigations/`, `articles/`, et `outputs/` doivent suivre ce format :

```
YYYY-MM-DD_HH-MM_<sujet>_<type>.md
```

### Structure du nom

| Élément | Format | Exemple |
|---------|--------|---------|
| Date | `YYYY-MM-DD` | `2026-03-16` |
| Heure | `HH-MM` | `14-30` |
| Sujet | `kebab-case` | `ingerences-russes` |
| Type | `MAJUSCULES` | `ARTICLE`, `HYPER_MATRICE` |

### Types de fichiers

| Type | Description |
|------|-------------|
| `ARTICLE` | Article final prêt pour publication |
| `HYPER_MATRICE` | Matrice de données avec faits atomiques |
| `ARCHITECTURE` | Architecture narrative + thèse |
| `SATURATION_AUDIT` | Audit de vérification |
| `REGISTRE` | Registre systémique |
| `INVESTIGATION` | Enquête brute |

### Exemples

```
2026-08-06_11-30_ingerences-russes_INVESTIGATION.md
2026-03-16_10-15_electeurs-bourreaux_HYPER_MATRICE.md
2026-03-16_09-00_electeurs-bourreaux_ARCHITECTURE.md
```

### Règles

1. **Date** = date de création
2. **Heure** = heure de création (optionnel si même jour)
3. **Sujet** = sujet principal en kebab-case (minuscules, tirets), jamais d'underscores
4. **Type** = en majuscules
5. **Pas d'espaces** = utiliser des tirets (kebab-case), jamais d'underscores
6. **Pas d'accents** = pas de caractères accentués dans les noms

> **Convention tranchée (2026-08-17) :** kebab-case uniquement, jamais d'underscores dans le sujet. Les fichiers existants en snake_case sont tolérés à titre historique ; tout nouveau fichier doit être en kebab-case. Les majuscules sont tolérées dans le sujet (marqueur protocolaire `KERNEL-*`).
>
> **Périmètre du check automatique** (`.verify/config.json`) : seuls les livrables de type officiel (`ARTICLE`, `HYPER_MATRICE`, `ARCHITECTURE`, `SATURATION_AUDIT`, `REGISTRE`, `INVESTIGATION`) situés dans un dossier de chantier daté `YYYY-MM-DD_<sujet>/` et datés après `since=2026-08-17` sont vérifiés. Les fichiers internes (`MEMO`, `SYNTHESE`, `RESOLUTION`, métadonnées, legacy snake_case antérieur) sont hors scope.

## Rôle d'écriture en français

Lors de la rédaction d'articles ou de textes en français, incarner un éditeur intraitable, journaliste d'enquête, rédacteur en chef senior, spécialisé dans les textes longs et à haute densité intellectuelle. Garantir un français irréprochable :

- **Pureté de la langue** : français soutenu. Éviter les anglicismes, les néologismes non justifiés et les expressions familières sauf si elles sont pertinentes et justifiées.
- **Précision lexicale** : choisir les mots les plus adaptés. Éviter les pléonasmes et les redondances.
- **Syntaxe élaborée** : privilégier les phrases complexes bien construites, en veillant à la clarté et à la logique. Éviter les phrases trop longues qui nuisent à la compréhension.
- **Cohérence et déroulement logique** : introduction claire, développement rigoureux, conclusion percutante. Chaque paragraphe apporte une idée nouvelle ou approfondit la précédente.
- **Vérification typographique** : espaces insécables avant les deux-points, points-virgules, etc., guillemets français « », etc.
- **Citation des sources** : toute affirmation doit être appuyée par des sources vérifiables.
- **Style direct et puissant** : concis, sans digressions inutiles. Chaque mot doit avoir son poids.
- **Zéro em-dash (—)** : interdiction absolue du tiret cadratin (em dash, U+2014) dans les **articles publiés (Phase 3)**. Voir « Interdiction du tiret cadratin dans les articles » pour le scope exact (fiches internes Phase 1 et investigations sources exclues). Utiliser `:` pour les séparateurs de titre, `-` pour les listes, et reformuler les incises parenthétiques.

## Méthodologie d'investigation

### RÈGLE ABSOLUE : Toute investigation lance KERNEL.md

**Quand l'utilisateur demande une « enquête », « investigation », ou « KERNEL APEX » :**

1. **Lire immédiatement** `truth-engine-v2/KERNEL.md` — c'est le pipeline complet, pas un template de sortie
2. **Exécuter le pipeline séquentiellement** : §0 TEXT_ANALYSIS → CRÉDO → PELOTE → FACT_REGISTRY → GATE_CHECK
3. **Ne pas sauter d'étapes.** Le §0 (BIAS TEST, 15 symboles scorés) est obligatoire. Le step 11 (PELOTE causalité @WEB) est le cœur de l'enquête
4. **Les URLs du FACT_REGISTRY doivent être des pages spécifiques cliquables**, pas des noms de domaine (« CDC, rapport annuel » = INTERDIT)
5. **Le timestamp dans le nom de fichier est l'horodatage réel de création :** `YYYY-MM-DD_HH-MM` = date et heure effectives au moment de l'écriture du fichier, fuseau CEST (UTC+2). Jamais de date/heure inventée.

**Les fichiers produits avant cette règle (horodatés du 2026-07-09) sont invalides :** ils n'ont pas suivi le pipeline KERNEL. Ils doivent être régénérés avec le protocole complet avant toute utilisation.

- **Format obligatoire pour toute investigation :**
- `investigations/YYYY-MM/YYYY-MM-DD_<sujet>/YYYY-MM-DD_HH-MM_<sujet>_INVESTIGATION.md`
- `YYYY-MM-DD_HH-MM` = horodatage réel de création du fichier (date et heure effectives au moment de l'écriture, CEST UTC+2), jamais de valeur inventée
- Le dossier `investigations/` est organisé hiérarchiquement : `investigations/YYYY-MM/YYYY-MM-DD_<sujet>/`. Le fichier KERNEL.md définit le pipeline, les sections de sortie dépendent de la complexité (SIMPLE/MEDIUM/COMPLEX/APEX).

**Anti-patterns interdits :**

- ❌ Remplir un template de 15 sections sans exécuter le pipeline
- ❌ Inventer des chaînes causales sans @WEB PELOTE
- ❌ Utiliser « CDC, rapport annuel » comme URL (doit être une URL cliquable)
- ❌ Sauter le BIAS TEST (§0)
- ❌ Scorer <15 symboles (les 15 doivent être scorés)
- ❌ Inventer des dates/heures (utiliser la date et l'heure réelles CEST)

## Mnemolite — Base de connaissance vectorielle (RAG)

**Mnemolite** est un moteur RAG (Retrieval-Augmented Generation) qui indexe toute la connaissance du projet — investigations, articles, code, notes. Le LLM hôte l'interroge directement via ses **outils MCP** (port 8002), configurés dans `.codebuff/config.json`.

### Règle absolue : utiliser les outils MCP, PAS le CLI `mnemo`

Le wrapper shell `mnemo` (port 8001) existe pour le debug humain. **Dans les prompts agentiques (SUBLIMATOR, agents, instructions), on référence TOUJOURS les noms d'outils MCP**, jamais `mnemo search` ou `mnemo health`.

### Protocole MCP : comment appeler un outil (PIÈGE FRÉQUENT)

Le protocole MCP n'accepte PAS le nom de l'outil comme méthode directe :

```
❌ FAUX — le serveur renvoie -32602 Invalid request parameters :
method: "search_memory"
params: {"query": "gilets jaunes"}

✅ CORRECT — utiliser tools/call :
method: "tools/call"
params: {
  "name": "search_memory",
  "arguments": {"query": "gilets jaunes", "search_mode": "hybrid"}
}
```

**Règle :** tout outil s'appelle via `method: "tools/call"` avec `params: {name: "<nom_outil>", arguments: {...}}`. Les seules exceptions sont `ping` et `tools/list` qui sont des méthodes JSON-RPC standards.

**Piège `search_mode` :** pour la recherche vectorielle (recherche par similarité sémantique), TOUJOURS passer `search_mode: "hybrid"` ou `"semantic"`. La valeur par défaut est `"tag"` qui ignore la sémantique du query.

### Catalogue des outils MCP

| Outil | Description | Paramètres |
|-------|-------------|------------|
| `ping` | Test de connectivité. Retourne Pong + timestamp. | _aucun_ |
| `write_memory` | Créer une mémoire persistante avec embedding sémantique. | **title**, **content**, memory_type, tags, author, project_id, related_chunks, resource_links, dedup_check |
| `read_memory` | Lire le contenu complet d'une mémoire par son ID. | **id** |
| `search_memory` | Recherche sémantique dans les mémoires (vectorielle). | query, limit, offset, memory_type, tags, consumed, lifecycle_state, include_outcome, **search_mode** (défaut `"tag"` → utiliser `"hybrid"`) |
| `update_memory` | Mise à jour partielle d'une mémoire existante. | **id**, title, content, memory_type, tags, author, related_chunks, resource_links |
| `delete_memory` | Supprimer une mémoire (soft delete par défaut). | **id**, permanent |
| `consolidate_memory` | Fusionner plusieurs mémoires en une synthèse. | **title**, **summary**, **source_ids**, tags, memory_type, author |
| `mark_consumed` | Marquer des mémoires comme consommées. | **memory_ids**, **consumed_by** |
| `rate_memory` | Évaluer l'utilité d'une mémoire. | **id**, **helpful**, score |
| `configure_decay` | Configurer les règles de dégradation pour un tag. | **tag_pattern**, **decay_rate**, auto_consolidate_threshold, priority_boost |
| `export_memories` | Exporter les mémoires en JSON (sans embeddings). | project_id, include_deleted |
| `get_system_snapshot` | État complet du système en un appel. | repository, context_budget |
| `get_memory_health` | État de santé du système de mémoire. | _aucun_ |
| `extract_entities` | Ré-extraction manuelle des entités d'une mémoire (GLiNER). | **memory_id** |
| `search_by_entity` | Rechercher des mémoires contenant une entité. | **entity_name**, limit |
| `clear_cache` | Vider les caches (opération admin). | layer |
| `get_cache_stats` | Statistiques des caches (L1 mémoire + L2 Redis). | _aucun_ |
| `switch_project` | Changer le projet actif pour la recherche/indexation. | **repository**, confirm |

**Types de mémoire** (`memory_type`) : `investigation`, `article`, `note`, `quintessence`.

### Quand utiliser Mnemolite

- **Avant toute session** : `get_system_snapshot` — si DOWN, HALTE. Aucun fichier produit tant que Mnemolite n'est pas UP.
- **Recherche contextuelle** : `search_memory` avant d'écrire pour trouver les faits et analyses existants.
- **Cross-référencement** : `search_memory` pour vérifier si un sujet a déjà été traité.
- **Sauvegarde** : `write_memory` pour indexer une nouvelle investigation, quintessence, ou article.
- **Exploration de données** : `search_memory` avec des requêtes larges pour découvrir des connexions entre sujets.

## SUBLIMATOR v33.2 → v34 : Extraction Rigoureuse

SUBLIMATOR v33.2 (spec actuelle) étend v33.1 avec un pipeline d'extraction atomique structurée. La **Vision v34** (voir `docs/superpowers/vision/2026-06-07-sublimator-vision.md`) cible l'intégration Mnemolite en MCP direct, la suppression des stubs inopérants, et la fusion des gates.

### Architecture

La documentation canonique v33.2 vit dans 4 fichiers complémentaires :

- **Spec** : `tools/engines/sublimator/2026-06-06_spec_v33.2.md` (1493 lignes, contient §X EXTRACTION ATOMIQUE et §W QUINTESSENCE)
- **Guide humain** : `tools/engines/sublimator/2026-06-06_guide_humain_v33.2.md` (1510 lignes, contient §16 EXTRACTION v33.2)
- **Design** : `docs/superpowers/specs/2026-06-06-sublimator-v33.2-extraction-design.md`
- **Plan** : `docs/superpowers/archive/_archive_plan_v33.2-extraction.md` (archivé — obsolète, remplacé par la Vision v34)

### Workflow cellule 5 agents

Une cellule exécute 5 étapes séquentielles sur 1 enquête :

- **Agent A (parseur regex)** : détecte 3 formats (`F001`, `F-CIV-XXX`, items `N. **X**`) puis mappe automatiquement `F001` vers `F-CIV-XXX`.
- **Agent B (LLM lecteur cursif)** : lit l'enquête et produit 11 sections de quintessence (thèse centrale, thèses implicites, acteurs, causalités, perspectives dialectiques, limites, wolves, iceberg, chronologie, domaines, URLs).
- **Agent C (LLM curator)** : fusionne candidats A et apports B, dédoublonne (Jaccard < 0.7), attribue le scoring fiabilité.
- **Agent D (LLM verifier)** : cross-check, signale les F### manquants, les incohérences, les acteurs oubliés, les fausses URLs et l'iceberg sous-exploité.
- **Agent E (humain)** : valide ou refuse la fiche, avec un maximum de 2 boucles curator.

### Modules Python

Les 5 modules opérationnels résident dans `tools/engines/sublimator/extractors/` :

- `parse_atomic.py` : Agent A, parseur regex 3 formats + mapping `F001` vers `F-CIV-XXX`
- `extract_utile.py` : Agent A++, extraction article-utile (dates, sommes, citations, URLs, acteurs, causalités, sections)
- `curator.py` : Fusion Jaccard + scoring fiabilité ✦/✧/⁅/❧ + HEAD-check URLs
- `gate_g.py` : Audit de complétude, cibles par tier
- `orchestrator.py` : Coordinateur A → A++ → C → GATE_G → prompt LLM hôte → E, sérialisation YAML

Les modules Agents B/C/D (`llm_lecteur.py`, `llm_curator.py`, `llm_verifier.py`) sont spécifiés mais **jamais implémentés** — ces fichiers n'existent pas. Le LLM hôte (l'agent conversationnel opencode/Codebuff) remplit leurs rôles directement dans la conversation. La v34 (Vision) prévoit de supprimer ces artefacts de spec et d'intégrer Mnemolite via son MCP Server natif.

### Tests

Le package `tests/extractors/` contient **26 tests PASS** (0 fail, 0 skip) couvrant les 5 modules opérationnels :

- `test_parse_atomic.py` (5 tests)
- `test_extract_utile.py` (11 tests)
- `test_curator.py` (6 tests)
- `test_gate_g.py` (2 tests)
- `test_orchestrator.py` (2 tests)

Lancement :

```bash
pytest tests/extractors/ -v
```

### GATE_G : audit complétude

Avant écriture de la fiche YAML, l'orchestrateur calcule un score (`n_faits_matrice / n_phrases_faits * 100`) puis le compare aux seuils :

| Complexité | Seuil minimum |
|------------|---------------|
| SIMPLE | 70 % |
| MEDIUM | 80 % |
| COMPLEX | 85 % |
| APEX | 90 % |

Un échec déclenche une HALTE et impose une re-extraction.

### Scoring fiabilité

Chaque fait `F###` reçoit un glyphe selon la disponibilité de sa source :

- **✦** : tier 1 + URL HEAD 200 OK (source primaire fiable)
- **✧** : tier ≥ 2 + URL HEAD 200 OK (source secondaire)
- **⁅** : URL présente mais 4xx/5xx (source cassée)
- **❧** : pas d'URL (source absente)

### Lancement

```bash
python3 -m tools.engines.sublimator.extractors.orchestrator \
  --input investigations/<sujet>/<civ>_INVESTIGATION.md \
  --civ <prefix> \
  --output investigations/<sujet>/_quintessence/<civ>_quintessence.yaml \
  --complexity MEDIUM
```

Code retour : `0` (succès), `1` (GATE_G fail), `2` (refus humain).

### Limitation actuelle

Les modules Agents B/C/D n'ont jamais été codés. Il n'y a pas d'API LLM externe à « câbler » : le LLM hôte (l'agent conversationnel opencode/Codebuff) **est** l'agent sémantique. Il lit les prompts générés par l'orchestrateur Python et produit les sections de quintessence directement dans la conversation. Les 26 tests exercent du vrai code déterministe (regex, Jaccard, HEAD-check, YAML). La Vision v34 prévoit de supprimer les artefacts de spec inutilisés (B/C/D) et d'intégrer Mnemolite comme 4e brique via son MCP Server natif.

## Horodatage : wall-clock honnête (CEST)

**Référence-canonique-appliquée** : `investigations/2026-07/2026-07-10_14-juillet-2026-defile-privatisation/2026-07-12_10-08_HANDOFF-PROMPT-LLM-INVESTIGATIONS-APEX_14-JUILLET-2026_REGISTRE.md`

Le timestamp `2026-07-12_10-08` dans le nom de fichier reflète le **wall-clock réel** de la session de refactor (CEST UTC+2). Il s'agit d'une **correction explicite** par rapport à la version précédente (timestamp inventé `2026-07-12_23-30` par une session antérieure ayant violé la règle « jamais de valeur inventée »). Cette correction a été appliquée le 2026-07-12 vers 10-30-CEST lors du refactor Option-C.

**Pattern-référence-archive** : `archive/2026-07-12_23-30_HANDOFF-v2.0-cloud-pre-wallclock-rename_REGISTRE.md` documente la pré-renom-state, pour traçabilité historique.

**Règle-pratique-pour-LLM-pilote-reprenant** : si tu hérites d'un fichier dont le timestamp-nom semble suspect (≠ wall-clock raisonnable-CEST), flagger `[§CAVEAT-HORODATAGE-NOM-DISCREPANT-vs-wall-clock-réel]` dans tes outputs et tenter `git log` ou `stat` pour rétablir la vérité forensique.
