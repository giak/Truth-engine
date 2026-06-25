# FREEBUFF SUB-AGENTS — Use Cases Avancés pour Truth Engine

**Version:** 2026-06-05
**Contexte:** Freebuff = orchestrateur multi-agents. Chaque sub-agent peut être invoqué directement ou orchestré par Buffy.

---

## §1 INVENTAIRE DES SUB-AGENTS

### Sub-agents (spawnables)

| Sub-agent | Rôle | Coût tokens | Quand l'utiliser |
|-----------|------|-------------|------------------|
| `file-picker` | Recherche fuzzy de fichiers pertinents | Faible | Début d'enquête, exploration |
| `code-searcher` | Recherche textuelle (ripgrep) dans le codebase | Faible | Recherche de patterns, cross-ref |
| `basher` | Commandes shell (via rtk) | Variable | Git, scripts, Mnemolite, curl |
| `researcher-web` | Recherche web sémantique | Élevé | Fact-checking, sources primaires |
| `researcher-docs` | Documentation technique | Faible | APIs, outils |
| `browser-use` | Navigation web automatisée | Très élevé | Pages interactives, login (⚠️ coût élevé) |
| `code-reviewer-deepseek` | Revue de code/article | Moyen | Validation post-rédaction |
| `thinker-with-files-gemini` | Raisonnement profond avec fichiers | Élevé | Problèmes complexes |
| `thinker-gpt` | Raisonnement sans fichiers (via ChatGPT) | Variable | Questions conceptuelles, décisions stratégiques |

### Outils directs (non spawnables)

| Outil | Rôle |
|-------|------|
| `read_files` | Lire des fichiers du projet |
| `str_replace` | Éditer des fichiers par remplacement |
| `write_file` | Créer ou écraser des fichiers |
| `list_directory` | Lister le contenu d'un dossier |
| `glob` | Recherche de fichiers par pattern |

---

## §2 PIPELINE D'INVESTIGATION (KERNEL v2)

### Phase 0 — Analyse textuelle (§0)

**Objectif:** Déconstruire un texte, scorer 15 symboles, détecter les patterns.

```
1. Charger le KERNEL et les définitions
   → read_files: truth-engine-v2/KERNEL.md, truth-engine-v2/definitions/SYMBOLS.md, truth-engine-v2/definitions/PATTERNS.md, truth-engine-v2/definitions/THREATS.md

2. Fact-checking web
   → researcher-web × 3: chiffres clés, acteurs nommés, sources primaires

3. Détection de patterns
   → code-searcher: recherche de termes manipulateurs dans les investigations passées
```

**Prompt type:**
```
Analyse ce texte avec le KERNEL v2. Charge SYMBOLS.md, PATTERNS.md, THREATS.md.
Vérifie 3 chiffres clés via researcher-web.
Produis le MANIPULATION_REPORT complet.
```

### Phase 1-3 — Complexité, Mémoire, Crédo

```
1. Classification de complexité
   → thinker-with-files-gemini: fichiers truth-engine-v2/KERNEL.md + investigation en cours

2. Recherche Mnemolite (KERNEL step 2: MEMORY)
   → basher: mnemo search (3-5 queries différentes)
   → basher: mnemo memories --limit 20

3. Génération des queries CRÉDO
   → researcher-web × 5: 1 query par domaine (⏰Ξ, €♦🌐, ◈⊕⊗, ΩΨΞ, ΛΦΣ)
```

### Phase 4-8 — Analyse cognitive et dialectique

```
1. Cartographie dialectique (3 perspectives)
   → thinker-with-files-gemini: truth-engine-v2/definitions/SYMBOLS.md + truth-engine-v2/definitions/PATTERNS.md + clusters chargés
   → researcher-web: sources pour chaque perspective (officielle, critique, dissidente)

2. Analyse cognitive (herméneutique L1-L6)
   → thinker-with-files-gemini: truth-engine-v2/protocol/INVESTIGATION.md + clusters + texte analysé
   → code-searcher: recherche de patterns similaires dans les enquêtes passées

3. Cross-référencement
   → file-picker × 3: investigations/, articles/, substack-online/
   → code-searcher × 3: noms d'acteurs, thèmes, patterns

4. Décision stratégique
   → thinker-gpt: choix des clusters à approfondir, priorisation des queries
```

### Phase 9-13 — Recherche, Construction, Vérification

```
1. Recherche web massive
   → researcher-web × 8-10 (parallèle): queries du CRÉDO + dialectique
   Ordre: ◈35% ADVERSARY20% CONTEXT20% DIVERSITY15% WOLF10%

2. Recherche de sources primaires
   → browser-use: sites gouvernementaux, FOIA, archives
   → basher: curl pour APIs publiques

3. Vérification croisée
   → researcher-web × 3: chaque fait ✦ par 2 sources indépendantes
   → code-searcher: contradictions dans les enquêtes existantes
```

**Prompt type:**
```
Phase 9-13 du KERNEL. Voici le MANIPULATION_REPORT et les queries CRÉDO.
Lance 10 researcher-web en parallèle (stratification ◈◉○).
Pour chaque fait du FACT_REGISTRY, vérifie avec 2 sources.
Signale les contradictions avec les enquêtes Mnemolite existantes.
```

### Phase 14-19 — Output, EDI, Sauvegarde

```
1. Génération du rapport
   → write_file: INVESTIGATION complète (write+edit pour >5000 chars)
   → code-reviewer-deepseek: revue qualité (extension KERNEL — le KERNEL utilise GATE_CHECK/GATE_AUTO, pas de revue externe)

2. Calcul EDI
   → thinker-with-files-gemini: truth-engine-v2/search/EPISTEMIC.md + rapport final

3. Sauvegarde Mnemolite
   → basher: mnemo write --title "..." --content "..." --tags "..."

4. Vérification gates
   → thinker-with-files-gemini: truth-engine-v2/forensic/GATES.md + rapport final
```

---

## §3 RÉDACTION D'ARTICLE (SUBLIMATOR v28)

### Avant rédaction

```
1. Charger le contexte
   → read_files: investigation source + sections connexes
   → basher: mnemo search (sujet + thèmes liés)

2. Vérifier les sources
   → researcher-web × 3: re-vérifier les chiffres et citations
   → basher: curl -I URLs (vérifier que les liens sont vivants)

3. Audit de saturation
   → thinker-with-files-gemini: investigation + SUBLIMATOR
```

### Rédaction

```
1. Génération section par section
   → write_file: §0 RÉSUMÉ (≤3000 chars)
   → str_replace × N: ajouter §1, §2, ... §N

2. Lint français
   → basher: ./tools/scripts/lint-article.sh articles/xxx.md

3. Vérification anglicismes
   → code-searcher: pattern='\\b(business|digital|start-up|cluster|booster|sponsor|fake|mainstream|burn-out|coach|deal|leader|newsletter|podcast|prime|spam|sponsoring|timing|tweet|webinar|branch|fork|repo)\\b' flags='-i' dans l'article
   → basher: rtk grep -i -E '\b(business|digital|start-up|cluster|booster|sponsor|fake|mainstream|burn-out|coach|deal|leader|newsletter|podcast|prime|spam|sponsoring|timing|tweet|webinar|branch|fork|repo)\b' articles/xxx.md

4. Revue éditoriale
   → code-reviewer-deepseek: article complet
```

### Post-rédaction

```
1. Comptage caractères
   → basher: python3 tools/scripts/char_counter.py articles/xxx.md

2. Vérification typographique
   → basher: rtk grep '—' articles/xxx.md  (em-dash interdit)
   → basher: rtk grep '« ' articles/xxx.md  (espaces guillemets)

3. Publication Substack (si API dispo)
   → basher: curl POST localhost:8000/drafts/create-markup
```

---

## §4 AUDIT & QUALITÉ

### Audit de saturation

```
1. Vérifier tous les clusters requis
   → thinker-with-files-gemini: investigation + truth-engine-v2/definitions/SYMBOLS.md §4

2. Vérifier toutes les sources
   → basher × N: curl -I chaque URL (vérifier 200/301/404)
   → researcher-web: URLs cassées → trouver des remplacements

3. Vérifier les gates
   → thinker-with-files-gemini: truth-engine-v2/forensic/GATES.md §4 checklist + investigation
```

### Audit de cohérence

```
1. Cross-ref interne
   → code-searcher × 5: noms, dates, chiffres dans toute l'enquête
   → file-picker: investigations liées

2. Contradictions
   → thinker-with-files-gemini: toutes les sections côte à côte
```

---

## §5 MNEMOLITE — MÉMOIRE VECTORIELLE

### Avant chaque enquête

```bash
# Recherche sémantique
@basher mnemo search "sujet keywords"

# Lister les mémoires récentes
@basher mnemo memories --limit 20

# Lire une mémoire spécifique
@basher mnemo read <uuid>

# Explorer un thème
@basher mnemo search "thème connexe"
```

### Après chaque enquête

```bash
# Sauvegarder
@basher mnemo write \
  --title "Titre enquête" \
  --content "$(cat investigations/xxx.md)" \
  --tags "tag1,tag2,tag3"

# Vérifier l'indexation
@basher mnemo search "mots-clés enquête"
```

### Maintenance

```bash
# État du serveur
@basher mnemo health
@basher mnemo status

# Événements récents
@basher mnemo events --limit 20
```

---

## §6 ORCHESTRATION AVANCÉE

### Pattern 1 — Enquête complète APEX

```
Étape 1: Charger le contexte (read_files × 5 + file-picker × 3)
Étape 2: Recherche Mnemolite (basher mnemo × 3)
Étape 3: Analyse textuelle (thinker-with-files-gemini)
Étape 4: Recherche web massive (researcher-web × 10 en parallèle)
Étape 5: Recherche sources primaires (browser-use + basher curl)
Étape 6: Construction FACT_REGISTRY (thinker-with-files-gemini)
Étape 7: Vérification croisée (researcher-web × 5 + code-searcher × 3)
Étape 8: Rédaction (write_file + str_replace × 7)
Étape 9: Lint + audit (basher scripts + code-reviewer-deepseek)
Étape 10: Sauvegarde (basher mnemo write)
```

### Pattern 2 — Audit de saturation rapide

```
Étape 1: Charger l'article + SUBLIMATOR (read_files × 2)
Étape 2: Lint automatique (basher lint-article.sh)
Étape 3: Vérification anglicismes (code-searcher)
Étape 4: Vérification em-dash (basher rtk grep)
Étape 5: Revue éditoriale (code-reviewer-deepseek)
Étape 6: Rapport d'audit (write_file)
```

### Pattern 3 — Cross-référencement thématique

```
Étape 1: Rechercher le thème dans tout le projet (code-searcher × 3)
Étape 2: Lister les fichiers pertinents (file-picker × 3)
Étape 3: Lire les fichiers (read_files × 5)
Étape 4: Synthétiser les connexions (thinker-with-files-gemini)
Étape 5: Générer un rapport de connexions (write_file)
```

### Pattern 4 — Vérification post-publication

```
Étape 1: Vérifier les URLs (basher curl -I × N)
Étape 2: Vérifier les chiffres (researcher-web × 3)
Étape 3: Vérifier les noms/orthographes (researcher-web × 2)
Étape 4: Rapport de corrections (write_file)
```

---

## §7 RÈGLES D'UTILISATION

### Parallélisme

- **Toujours lancer en parallèle** les agents indépendants (researcher-web, code-searcher, file-picker, basher)
- **Séquencer** les agents dépendants (d'abord file-picker, puis read_files, puis thinker)
- Maximum 10-12 agents parallèles pour éviter la saturation

### Optimisation tokens (RTK)

- **TOUJOURS** préfixer les commandes shell avec `rtk` (sauf git add/commit/push, npm/pip install, rm, mkdir, cp, mv)
- Exemple: `rtk grep`, `rtk find`, `rtk git status`, `rtk curl`
- Économie typique: 60-95% de tokens sur les sorties shell

### Écriture de longs fichiers

- **NE JAMAIS** dépasser 5000 caractères dans un `write_file`
- Utiliser `write_file` pour la base + `str_replace` pour ajouter les sections
- Vérifier après chaque `str_replace` que le contenu est bien ajouté

---

## §8 ANTI-PATTERNS

| Pattern | Problème | Solution |
|---------|----------|----------|
| Lancer 20 researcher-web d'un coup | Saturation, coût tokens | Max 10, puis synthèse, puis re-lancer si nécessaire |
| Lire 30 fichiers avant d'agir | Surcharge cognitive | Lire par vagues: 5 fichiers → décision → 5 fichiers |
| Écrire un article de 8000 mots en un write_file | Échec silencieux | write+edit segmenté, 3000 chars max par bloc |
| Oublier Mnemolite | Perte de mémoire entre sessions | mnemo search SYSTÉMATIQUE en début d'enquête |
| Sauter le code-reviewer-deepseek | Fautes non détectées | Revue systématique post-rédaction |
| Chercher sans file-picker d'abord | Pertes de tokens | file-picker → read_files → action |
| Utiliser browser-use pour des pages statiques | Coût tokens ×10 vs curl | curl pour les APIs/JSON, browser-use seulement pour les pages interactives |

---

*Document généré le 2026-06-05 — À mettre à jour avec l'évolution des sub-agents Freebuff.*
