# Mnemolite : État de l'art, point et pistes d'optimisation

**Horodatage** : 2026-08-07 16:51 CEST (wall-clock)
**Auteur** : Buffy (FreeBuff), audit de terrain sur machine locale
**Périmètre** : déploiement global (opencode + FreeBuff/Codebuff), serveur MnemoLite v5.0.0-dev, intégration Truth Engine + KERNEL v2.0

---

## 1. Vue d'ensemble du socle

### 1.1 Le serveur (source : `/home/giak/Work/MnemoLite`)

| Élément | Valeur constatée |
|---|---|
| Version | 5.0.0-dev, README badge « 1 570 tests passing », EPICs 28-36 + 42 complétés |
| Base | PostgreSQL 18 + pgvector 0.8.1 (HNSW + halfvec), pg_trgm, pg_partman (partitionnement mensuel) |
| Conteneurs (docker-compose) | db (mnemo-postgres), redis (mnemo-redis), api (mnemo-api), worker (mnemo-worker), mcp (mnemo-mcp), frontend, openobserve (observabilité) ; profiles dev (Vite HMR :3000) / prod (Nginx) |
| API REST | `http://localhost:8001` (FastAPI, docs /docs, /redoc) |
| MCP | `http://localhost:8002/mcp` (remote HTTP SSE, 29-31 outils déclarés) |
| Web UI | Vue 3 SPA, 13 pages (Dashboard, Search, Memories, Projects, Expanse, Monitoring, Alerts, Brain, Graph, Orgchart, Logs, Search Analytics), thème SCADA |
| CLI `mnemo` | health, status, search, write, memories |
| Embeddings | 100 % locaux : BAAI/bge-m3 (texte), jinaai/jina-embeddings-v2-base-code (code) ; registre central `api/core/embedding_models.py` (bge-m3, nomic v1.5, nomic v2-moe) |
| Cache | Triple couche L1 (mémoire) → L2 (Redis) → Postgres ; TTL 60 s hybride / 300 s tag |
| Recherche mémoire | hybride : lexical (pg_trgm) + vectoriel (HNSW halfvec) + **fusion RRF** + rerank BM25 optionnel (EPIC-24 P2, pur Python sans ML) |
| Modèle d'exécution | `search_mode` : `tag` (défaut, rapide) / `hybrid` / `semantic` ; fallback lexical ou tag-only si embedding indisponible |
| Pipeline write | write → INSERT (embedding=None) → embedding async → UPDATE embedding + `embedding_generated=True` ; dedup_check Jaccard ≥ 0.9 ; anti-secret 11 regex ; `embedding_source` (EPIC-24) |
| Décay / consolidation | services dédiés (`memory_decay_service`, `consolidation_suggestion_service`), tags `sys:*` (sys:core/anchor permanents, sys:history 14 j, etc.) |
| Auto-save conversations | worker Redis Streams (`conversations:autosave`) → `POST /v1/conversations/save` → mémoires de type `conversation` |

### 1.2 Volume réel (interrogé en direct, 2026-08-07)

| Métrique | Valeur |
|---|---|
| Mémoires totales | **39 534** (dont 55 aujourd'hui) |
| Avec embedding | 38 673 (**97,8 %** ; 861 sans embedding, alerte du serveur) |
| Répartition par type | conversation 33 612 (85 %), investigation 4 808, note 831, reference 94, quintessence 94, article 52, decision 45, task 2 |
| Modèle d'embedding texte | BAAI/bge-m3 (text_embeddings : 39 534 total, 38 673 ok) |
| Circuit breakers | embedding_text closed (1 succès), embedding_code closed, redis_cache closed, **tous sains** |
| Santé | `/health` 200, postgres + redis OK |
| Cache | L1 0 entrée, L2 redis connecté, 0 hit/0 miss (cache froid, TTL courts) |

### 1.3 État docker réel (source canonique : `/home/giak/Work/MnemoLite/README.md` + `docker ps`, tout tourne sous docker)

| Conteneur | Statut | Notes |
|---|---|---|
| mnemo-api | ✅ running healthy | 127.0.0.1:8001→8000 |
| mnemo-mcp | ✅ running healthy | 127.0.0.1:8002→8002 |
| mnemo-postgres | ✅ running healthy | 127.0.0.1:5432→5432 |
| mnemo-redis | ✅ running healthy | 0.0.0.0:6379→6379 |
| mnemo-openobserve | ✅ running | 5080 (traces/metrics/logs OTLP) |
| mnemo-frontend | ✅ running | profile dev (Vite, port 3000) |
| **mnemo-worker** | 🔴 **Restarting (crash-loop)** | **1 506 redémarrages**, ExitCode=1 |
| charming_engelbart | ✅ running | ghcr.io/mudler/mcps/duckduckgo (MCP DuckDuckGo, non mnémo) |

**🔴 Découverte critique : `mnemo-worker` est en crash-loop.** Erreur dans les logs :

```
File "/app/workers/conversation_worker.py", line 13, in <module>
    from api.core.settings import get_settings
ModuleNotFoundError: No module named 'api'
```

Le conteneur worker lance `conversation_worker.py` sans que le package `api` soit sur le PYTHONPATH (`/app/workers/` seul, pas `/app/`). **Conséquence directe : le pipeline d'auto-save des conversations (Redis Streams → mémoires type `conversation`) est à terre.** Les 33 612 mémoires `conversation` existantes ont été écrites avant la panne ; toute conversation nouvelle n'est plus sauvegardée tant que le worker n'est pas réparé (fix probable : corriger l'entrée/le PYTHONPATH du service worker dans `docker-compose.yml` ou `workers/Dockerfile`, puis `docker compose up -d worker`). Ce constat ne remet pas en cause les 4 conteneurs sains (api, mcp, db, redis) qui servent la boucle forensique.

- 85 % du volume est de la **conversation autosauvée** (pipeline Claude Code → hooks → Redis → worker). Le « vrai » socle forensique (investigations 4 808 + references 94 + quintessence 94 + notes 831) est un sous-ensemble minoritaire.
- Le cache L2 est connecté mais froid : TTL 60 s/300 s, peu de réutilisations inter-sessions.

---

## 2. Ce qui est mis en place (opencode + FreeBuff)

### 2.1 L'outillage forensique « mnemolite-mem-first » (design 2026-08-06, implémenté)

**Source unique versionnée** : `book/tools/mnemolite-mem-first/` (repo truth-engine, submodule book)
```
SKILL.md                            ← procédure complète (source unique, DRY)
hooks/opencode.AGENTS.md            ← hook global opencode
hooks/freebuff.AGENTS.md            ← hook global Codebuff/FreeBuff
templates/mcp.json                  ← config MCP remote 8002
templates/source-verifier.md        ← agent opencode dédié
setup.sh                            ← déploiement idempotent (5 fichiers globaux)
```

**Déployé en global user** (vérifié sur machine) :
| Fichier | Présent | Contenu |
|---|---|---|
| `~/.agents/skills/mnemolite-mem-first/SKILL.md` | ✅ (identique au repo) | Procédure 5 règles |
| `~/.agents/mcp.json` | ✅ | mnemolite → `http://localhost:8002/mcp` (type http) |
| `~/.config/opencode/AGENTS.md` | ✅ | Hook « Mémoire d'abord » |
| `~/.AGENTS.md` | ✅ | Hook global Codebuff/FreeBuff (lu par FreeBuff) |
| `~/.config/opencode/agent/source-verifier.md` | ✅ | Agent subagent opencode |
| `~/.agents/.mcp.json` | ✅ (hérité) | headroom + headroom-memory (désactivés dans opencode.json) |

**Les 5 règles du skill** : 1 MÉMO D'ABORD (search `hybrid` obligatoire, tags `project:*`) → 2 TROUVÉ = STOP (CONFIRME = réponse avec source + citation + memory_id, zéro web) → 3 WEB SINON (source primaire, read_url soi-même) → 4 WRITE-BACK obligatoire (une mémoire = claim + registre URL via tag `source:<sha1-10>`) → 5 MNEMO DOWN (stop, pas de conclusion).

**Interfaces ordonnées** : MCP natif (8002) → fallback MCP par curl 8002 (recommandé sans MCP) → REST 8001 dernier recours (health + `GET /api/v1/memories/search`).

### 2.2 Câblage opencode (`~/.config/opencode/opencode.json`)

- Modèle : ollama `Qwen3.6-abliterated:35b` (baseURL 127.0.0.1:11434) ; plugins context-mode, warp, superpowers.
- **MCP mnemolite remote activé** (type remote, url 8002/mcp, timeout 10 s).
- **Tools whitelist explicite** : `mnemolite_clear_cache`, `configure_decay`, `consolidate_memory`, `delete_memory`, `export_memories`, `extract_entities`, `find_path`, `get_*`, `index_*`, `mark_consumed`, `rate_memory`, `reindex_file`, `retry_indexing`, `search_code`, `switch_project`, `traverse_graph` = **tous `false`** (désactivés). Restent actifs : ping, write_memory, read_memory, update_memory, search_memory, search_by_entity (non listés).
- **Lecture** : le hook global `~/.config/opencode/AGENTS.md` est honoré.

### 2.3 Câblage FreeBuff / Codebuff

- **Knowledge files globaux** : FreeBuff (built on Codebuff) lit `~/.knowledge.md` puis `~/.AGENTS.md` (premier trouvé) → le hook global vit dans `~/.AGENTS.md` (vérifié, contenu correct).
- **MCP global** : `~/.agents/mcp.json` (remote 8002). Vérifié fonctionnel dans cette session (tous les appels search/write/update/read passent par ce MCP).
- **Skills globaux** : `~/.agents/skills/` scruté par opencode ET FreeBuff ; **constat récurrent : l'auto-découverte du skill global n'est PAS fiable en session FreeBuff** (déjà documenté dans le design 2026-08-06, confirmé à nouveau : l'outil `skill` de cette session liste « no skills available »). Le hook `~/.AGENTS.md` prévoit le repli : lire directement `~/.agents/skills/mnemolite-mem-first/SKILL.md`.
- Le projet n'a plus de config locale : zéro `.agents/`, zéro `opencode.json` projet, tout est global.

### 2.4 Intégration Truth Engine / KERNEL v2.0 (`truth-engine-v2/KERNEL.md`)

Le KERNEL est un pipeline d'investigation (19+ étapes) avec Mnemolite intégré à 3 points :
- **Entrée (step 2)** : `@MNEMO_Q` = `search_memory(query, search_mode="hybrid", tags=["project:truth-engine","kernel"], limit=5)` → `$EXISTING`. Règle dure : hybrid obligatoire sinon tag_only → 0 résultat. Échec → skip (log « MnemoLite unavailable »), pipeline continue.
- **Sortie (step 19)** : `@MNEMO_S` = `write_memory` (mémoire = investigation complète) + `@WRITE` fichier INVESTIGATION, **les deux obligatoires**.
- **Step 19a** : `@FACT_WRITEBACK` (registre des faits) + règle anti-doublon : `duplicate_warning` (Jaccard ≥ 0.9) → `@MNEMO_U` (update) au lieu de recréer ; faits déjà dans `$EXISTING` → update.
- **Priorité de recherche** : @MNEMO_Q (local, sans rate limit) → @WEB (DuckDuckGo) → @FETCH → @EXA (Exa, last resort).
- 18 mentions `@MNEMO` dans le KERNEL.

**Écart constaté** : la règle KERNEL « @MNEMO_Q tags=["project:truth-engine","kernel"] » est plus stricte que le skill global (qui recommande d'inclure le `project:*` courant). Le tag `kernel` n'est pas documenté dans les conventions du skill (§Registre par URL et tags), divergence de conventions à harmoniser.

### 2.5 Docs projet

- `knowledge.md` (racine truth-engine) : §Mnemolite, règles, interdictions (pas de claim sans read_url, pas de tag inventé, writer_chain déprécié = NON VÉRIFIÉ), interfaces.
- `book/knowledge.md` : §Mnemolite, socle de données unique du livre, schéma de tags `project:book` + `livre-cst` + `circuit-{N}` + `status:CONFIRME` + `source:<sha1>` + `verifie-YYYY-MM-DD` + `chapitre-{C}`.
- `docs/MNEMOLITE_STATUS.md` : statut curator-asserted « Mnemolite FONCTIONNE », procédure de vérification `rtk mnemo health` (1 commande), interdiction des audits basher de ports.

---

## 3. Points de vigilance constatés (état réel, vérifié en direct)

### 3.1 Endpoints REST cassés (documentés et re-confirmés)
- `POST /v1/search/` → `{"detail":"Search failed"}` (confirme le skill).
- `POST /v1/search/content`, `/v1/search/similarity`, `POST /api/v1/memories/search` (corps) → vide ou erreur. Seul fiable : `GET /api/v1/memories/search`.
- `GET /api/v1/memories/search?query=parrainages&limit=3` → OK, mais **ne remonte pas la mémoire consolidée `58cc0e69`** (qui contient pourtant « parrainages ») : retrouvée seulement par recherche sémantique MCP hybride ou tags. Comportement déjà constaté en session précédente : **la recherche par chaîne exacte échoue sur les contenus longs** (dilution pg_trgm) et **les embeddings sont calculés sur `embedding_source`, pas sur le contenu complet** → une chaîne exacte présente dans le contenu mais absente du résumé n'est pas retrouvée.

### 3.2 Le wrapper MCP impose le mode hybride (défaut `tag`)
- `search_memory` sans `search_mode` explicite retombe en `tag`/`tag_only` et rend 0 résultat même pour des faits présents. **C'est le piège n° 1 d'utilisation** (documenté dans le skill et le KERNEL, re-constaté en session).

### 3.3 Corpus hétérogène
- 33 612 conversations autosauvées (85 %) non taggées `project:*` ni `status:*` : elles polluent la recherche hybride (remontées avec des scores bas) et ne portent aucun verdict forensique.
- 861 mémoires sans embedding (alerte serveur).
- Doublons hérités (1 461 mémoires `livre-cst` historiques, schéma writer-chain déprécié).

### 3.4 Cache froid
- L2 Redis connecté mais 0 hit/0 miss : TTL courts (60 s/300 s) → peu de réutilisation inter-sessions. Les écritures à répétition (mêmes sources revérifiées) restent possibles si le réflexe mémoire n'est pas systématique.

---

## 4. Brainstorm : optimisations / robustesse / généralisation

Classées par levier, avec priorité (P0 = impact immédiat, P1 = court terme, P2 = moyen terme).

### A. Fiabiliser la recherche (P0, le cœur du socle)

1. **Fusionner les deux voies de recherche** : corriger les endpoints REST morts (`POST /v1/search/`, `POST /api/v1/memories/search`) pour qu'ils exécutent la MÊME logique hybride RRF que le MCP, aujourd'hui ils renvoient vide ou échouent, forçant à passer par le wrapper MCP. Cible : un seul chemin de recherche, 3 transports (MCP / REST / curl fallback).
2. **Recherche par chaîne exacte sur contenu long** : le pg_trgm dilue le score sur les contenus longs et l'embedding est calculé sur `embedding_source` (résumé) et non sur le contenu. Pistes : (a) indexer AUSSI l'embedding du contenu complet en plus du résumé (double embedding par mémoire) ; (b) ajouter un passage tsvector/ILIKE exact comme 3e composant du RRF ; (c) documenter fortement `embedding_source` comme obligatoire et le générer automatiquement (résumé LLM du content) à l'écriture si absent.
3. **`search_mode` par défaut = hybrid** : changer le défaut du serveur (actuellement `tag`), ou faire en sorte que `tag_only` sans tags ne retourne pas 0 mais fasse un vrai fallback hybride. Supprimer la classe d'erreur « j'ai oublié hybrid » à la racine.
4. **Pondération projet** : enrichir le RRF d'un boost par tag `project:*` (filtre) afin que la recherche d'un fait dans `project:truth-engine` ne soit pas noyée par les 33 k conversations non taggées. Exposer `project` comme paramètre de premier niveau (pas seulement tags).

### B. Nettoyer le corpus (P1)

5. **Campagne de taggage des conversations** : soit les exclure de la recherche par défaut (`memory_type=conversation` exclu du RRF sauf demande), soit les tagger rétroactivement (`project:*` par heuristique de chemin/remarque). 85 % du volume sans verdict est un risque de bruit permanent.
6. **Backfill des 861 embeddings manquants** (alerte serveur) + régénération périodique (job hebdomadaire : mémoires sans embedding OU `embedding_source` absent).
7. **Nettoyage des doublons hérités** : campagne `consolidate` / `update_memory` sur `livre-cst` (1 461) avec l'outil de suggestion existant (`suggest_consolidation`, threshold 0.3), le socle de code existe déjà.

### C. Renforcer le write-back et l'anti-doublon (P1)

8. **Registre URL en 1 appel** : aujourd'hui le registre par URL est un tag `source:<sha1>` ; le rendre interrogable via un outil dédié `find_by_url(url)` (exposer le lookup) pour que « ai-je déjà vérifié cette URL ? » soit un appel MCP explicite, pas une astuce de tags.
9. **Dedup plus tôt dans le pipeline** : le check Jaccard ≥ 0.9 se fait à l'écriture ; étendre au contenu vectoriel (similarité cosine > seuil) pour rattraper les reformulations.
10. **Statut par défaut** : imposer `status:` (CONFIRME/PLAUSIBLE) dans le schéma write (validation serveur douce, pas bloquante) pour que zéro mémoire écrite soit sans verdict.

### D. Généraliser aux projets (P2)

11. **CLI `mnemo` (setup/status/validate/test)** : l'AUTOMATION_MNEMOLITE_SETUP.md propose déjà le design complet (init, status, validate, remove, list, update, report). Le déploiement global existe (setup.sh) mais pas d'outil de contrôle par projet. Priorité si 10+ projets.
12. **Hook de SessionStart / auto-détection** : détecter projet non configuré et proposer l'activation conversationnelle (design Niveau 5 du doc), le hook global AGENTS.md couvre déjà l'instruction, pas le « setup automatique ».
13. **Onboarding projet standardisé** : template « section Mnemolite » d'AGENTS.md projet (périmètre `project:*`, tags, schéma write-back), copier le bloc `book/knowledge.md` §Mnemolite en modèle.

### E. Truth Engine / KERNEL (P1, spécifique)

14. **Harmoniser les conventions de tags** : le KERNEL utilise `tags=["project:truth-engine","kernel"]` ; le skill global ne documente pas `kernel`. Ajouter `kernel` au §Registre par URL et tags du skill (ou retirer du KERNEL). Unifier aussi `status:CONFIRME` (skill/KERNEL) vs `fact:verifie`/`status:confirme` (mémoires récentes de cette session), **trois variantes de casse/format coexistent déjà**.
15. **Généraliser le pattern KERNEL à tout le projet** : le KERNEL impose `@MNEMO_Q` en step 2 et `@MNEMO_S` + `@FACT_WRITEBACK` en step 19, étendre l'obligation aux autres pipelines (audits phase 1/2, relectures d'articles, ICEBERG MAX) : chaque investigation de truth-engine devrait suivre le même contrat d'entrée/sortie.
16. **Écrire les quintessences comme mémoires `quintessence`** : les 94 quintessences existantes montrent le pattern ; le généraliser (chaque investigation KERNEL produit SA quintessence en mémoire, taggée `quintessence` + `project:truth-engine` + `kernel`).
17. **Boucle KERNEL↔Mnemo plus riche** : le step 2 ne fait que `limit=5` ; proposer une variante `@MNEMO_Q_PELOTE` (limit=20) pour alimenter le step 11 (PELOTE, causalité) et le FACT_REGISTRY depuis les faits CONFIRME existants, éviter de re-vérifier ce qui est déjà confirmé (principe « ne jamais reconfirmer »).

### F. Robustesse infrastructure (P2)

18. **Single point de défaillance** : tout repose sur une machine locale (docker-compose, ports 8001/8002, postgres+redis en conteneurs). Pistes : systemd/healthcheck de supervision, restart policies, sauvegarde postgres automatique (pg_dump quotidien), observabilité openobserve déjà présente (activer les alertes).
18bis. **Réparer le crash-loop du worker (URGENT)** : `ModuleNotFoundError: No module named 'api'` sur `conversation_worker.py` (1 506 restarts). Corriger le PYTHONPATH/entrée du service worker dans `docker-compose.yml` ou `workers/Dockerfile` (`cd /app` avant le lancement, ou `PYTHONPATH=/app`), puis `docker compose up -d worker` et vérifier `docker logs` + `GET /v1/conversations/metrics`. Sans cette réparation, l'auto-save des conversations reste coupé et le corpus `conversation` (85 % du volume) se fige.
18ter. **Ajouter un healthcheck au worker** (comme api/mcp/db/redis en ont un) pour que la panne soit visible dans `docker ps` au lieu d'un `Restarting` muet.
19. **Tests du pipeline critique** : le plan de test `plans/2026-06-13_mnemolite-mcp-test-protocol.md` liste des tests APEX (write→search e2e, race async embedding, dedup, cache invalidation), vérifier qu'ils sont couverts par les 1 570 tests et les faire tourner en CI avant toute modif du moteur de recherche.
20. **Versionnage des schémas de tags** : introduire un tag `schema:vN` ou un registre des conventions par projet pour éviter la dérive (ex. `verifie-*`, `status:*`, `fact:*`, `source:*` vus ensemble dans ce corpus).

---

## 5. Synthèse

**Ce qui est solide** : le socle est réellement fonctionnel (39 534 mémoires, 97,8 % d'embedding, recherche hybride RRF, MCP remote opérationnel, hooks globaux déployés pour opencode et FreeBuff, KERNEL câblé avec contrat d'entrée/sortie). Le design « mnemolite-mem-first » (2026-08-06) a tenu : les 5 règles, l'ordre MCP→curl→REST, l'anti-doublon.

**Les 3 failles réelles** :
1. **Recherche par défaut = tag** → piège systématique (0 résultat sans `hybrid`).
2. **Recherche exacte sur contenus longs dégradée** (pg_trgm dilué + embedding sur résumé uniquement) → risque de cache miss à tort.
3. **85 % du corpus sans verdict** (conversations autosauvées) → bruit permanent dans les résultats hybrides.

**L'anomalie d'infra du jour (2026-08-07 16:5x CEST)** : le conteneur `mnemo-worker` est en crash-loop (1 506 redémarrages, `ModuleNotFoundError: No module named 'api'`) : l'auto-save des conversations est coupé. Les 4 conteneurs de la boucle forensique (api, mcp, db, redis) sont sains et répondent.

**Les 3 gains immédiats à coût faible** : défaut hybrid + filtrage `project:*` dans le RRF ; backfill des 861 embeddings ; harmonisation des tags KERNEL/skill (`kernel`, `status:*`/`fact:*`).

---

*Sources interrogées en direct : health 8001, /v1/cache/stats, /api/v1/memories/stats, /api/v1/memories/embeddings/health, /api/v1/memories/decay/config, GET /api/v1/memories/search ; code : memory_tools.py, hybrid_memory_search_service.py, memory_repository.py, conversation_worker.py ; configs : ~/.agents/mcp.json, ~/.config/opencode/opencode.json, ~/.AGENTS.md, book/tools/mnemolite-mem-first/* ; README.md et MCP_SETUP.md de /home/giak/Work/MnemoLite ; docker ps + docker logs/inspect mnemo-worker ; KERNEL v2.0 ; docs/projets : MNEMOLITE_STATUS.md, book/knowledge.md, plans/2026-06-13_mnemolite-mcp-test-protocol.md.*
