---
name: mnemolite-mem-first
description: Vérification forensique d'un fait. Use when you must verify or source a fact, chiffre, date, mécanisme, événement, verdict, or source URL (also "vérifier", "source", "fact-check", read_url avant websearch). Imposes the order : recherche Mnemolite d'abord, recherche web ensuite, write-back obligatoire. tool-agnostic, MCP ou curl 8001.
---

# mnemolite-mem-first — Mémoire d'abord, write-back obligatoire

Procédure permanente de vérification des faits. Règle cardinale : **un fait sans entrée Mnemolite n'est pas vérifié** ; **aucun fait CONFIRME n'est automatiquement expiré** (pas de règle des 7 jours).

Contexte : `knowledge.md §Recherche et Vérification Forensique` + `§Mnemolite — Socle de données unique du livre`.

## Interfaces

| Interface | Quand | Accès |
|:--|:--|:--|
| **MCP mnemolite** | par défaut (agent qui a les outils `search_memory`, `write_memory`, `update_memory`, `read_memory`) | remote `http://localhost:8002/mcp` |
| **REST `curl` 8001** | fallback — tout agent avec bash | `http://localhost:8001` — `health` (200) avant usage ; commandes exactes en Règle 4 |

## Règles de la procédure

### Règle 1 — MÉMO D'ABORD

Toute question portant sur un fait (chiffre, date, mécanisme, événement, verdict) commence par une recherche Mnemolite, **avant tout appel web** :

- Recherche par concept : `search_memory(query=<fait>, search_mode="hybrid", tags=[project:book, project:truth-engine, …], limit=10)`. Inclure le tag `project:*` du projet en cours. **`search_mode: "hybrid"` recommandé** (voie vectorielle sémantique complète) ; sans lui, la recherche reste fonctionnelle (fallback texte libre depuis le 2026-08-07, re-testé le 2026-08-08 sans `search_mode` ni tags : la mémoire parrainages 293 est remontée).
- **Corpus hérité** : pour `project:book`, les mémoires `livre-cst` (schéma `source-chatgpt-csv`) classent les claims dans le **corps** (`Statut canonique` C1-C6/WEB, `Classe source` S0-S3), **sans tag `status:`** — inclure `livre-cst` dans la recherche par tags, lire ces champs, puis appliquer la réconciliation (FACT_VERIFICATION.md §11 / `tools/classify_legacy.py`). **`C1 — Confirmé` n'est PAS `status:CONFIRME`** : c'est un candidat L0 à re-vérifier par l'échelle L0→L4 ; seul `C5 — Faux` se mappe en direct (`status:REFUTE`).
- Si une URL est déjà en main : lookup par registre URL via le tag `source:<sha1-10-hex(url)>`.

### Règle 2 — TROUVÉ = STOP

Si une mémoire `status:CONFIRME` correspond au fait (même chiffre, même source, même date de publication) :

- Répondre avec : `source_url` + `source_date` + citation + `memory_id`.
- **Aucun appel web. Aucune re-vérification.** La vérification date du write-back. Revérifier à la demande seulement (fait contesté, nouvelle donnée, source défunte).

### Règle 3 — WEB SINON

Si rien de pertinent, ou uniquement une mémoire `status:VERIFIE` :

1. Recherche web pour localiser la **source primaire** (jamais un chiffre rapporté depuis un snippet).
2. Lire la source en entier (outil de lecture d'URL — `webfetch`/`read_url` ; fallback `browser-use`/pdftotext pour PDF/JavaScript). L'agent qui vérifie exécute lui-même, ne délègue pas.
3. Exiger **les trois éléments** : URL exacte + date de publication + citation du passage contenant le chiffre. Un seul manque → fait non publiable.

### Règle 4 — WRITE-BACK OBLIGATOIRE

À la fin de toute session de recherche web **aboutie**, écrire **une seule mémoire** qui sert à la fois de claim et d'entrée du registre par URL.

**Schéma (MCP `write_memory`) :**

```
title     = fait vérifié, en français, avec chiffre
content   = fait + citation du passage source
tags      = ["project:book" (ou project:*), "status:CONFIRME",
             "source:<sha1-10-hex(url)>", "verifie-YYYY-MM-DD",
             "circuit-{N}" (livre)] 
```

- `status:CONFIRME` si vérifié en lisant la source ; `status:VERIFIE` si source lue mais pas encore recoupée (L1-L3). **Jamais écrire un fait sans source lue (NON VÉRIFIÉ).**
- **Registre des tags (EPIC-60, 2026-08-07)** : casse canonique `status:CONFIRME` (MAJUSCULE, jamais `status:confirme`) ; `fact:verifie` est OBSOLÈTE (le write le remplace par `status:CONFIRME` + émet un warning) ; namespaces réservés : `status`, `fact`, `project`, `sys`, `session`, `date`, `source` ; `kernel` documenté. Vocabulaire serveur réel : `CONFIRME`/`DOUTE`/`REFUTE`/`VERIFIE` — le serveur rejette `status:PLAUSIBLE` (drift corrigé 2026-08-16 : L1-L3 = `status:VERIFIE`). Registre complet : `MCP_SETUP.md` §8.
- La réponse du write peut contenir un champ `tag_warnings` (optionnel, NON bloquant) : namespace inconnu, statut inconnu, mémoire `kernel*` sans `status:*`, casse normalisée. À vérifier sans bloquer.
- Si la réponse contient un `duplicate_warning` (Jaccard ≥ 0.9) → `update_memory` sur la mémoire existante au lieu de re-écrire.
- **Fallback REST 8001** — commandes VÉRIFIÉES uniquement ; ne pas explorer l'API, ne pas deviner d'endpoint. ⚠️ **`POST /v1/events/` écrit un event, pas une mémoire** : invisible de `search_memory`/`read_memory` et de `GET /api/v1/memories/search` (constaté en test 2026-08-06). Réservé à la trace d'audit — pour un write-back que la boucle MCP doit relire, préférer le Fallback MCP par curl ci-dessous :

```bash
# santé
curl -s http://localhost:8001/health                      # mnémo UP ?

# RECHERCHE (seul endpoint fonctionnel, GET /api/v1/memories/search)
curl -s "http://localhost:8001/api/v1/memories/search?query=<fait>&limit=10"

# WRITE-BACK (POST /v1/events/)
curl -s -X POST http://localhost:8001/v1/events/ \
  -H "Content-Type: application/json;charset=UTF-8" \
  -d '{
    "content": {"fr": "FAIT", "source_url": "URL", "source_date": "YYYY-MM-DD"},
    "metadata": {"tags": ["project:book","status:CONFIRME","source:HASH","verifie-YYYY-MM-DD"],
                 "status": "CONFIRME"}
  }'
```

> ⚠️ Voies REST de recherche : `GET /api/v1/memories/search?query=...` reste la voie de référence (délègue à `_search_memories`, même logique que `search_memory` MCP). Depuis l'unification REST (EPIC-59, 2026-08-07), `POST /v1/search/` est RÉÉCRIT et fiable : il délègue aussi à `_search_memories` (query requis, réponse au format `data` unifié). `POST /api/v1/memories/search` (body JSON) déléguait déjà et fonctionne. `POST /v1/search/content` et `POST /v1/search/similarity` ont été SUPPRIMÉS (routes orphelines, EPIC-59). Restent non fiables : `POST /v1/events/search/embedding`, `POST /v1/events/filter/metadata`. `GET /v1/search/` (voie events legacy) est conservé mais lit les events, pas les mémoires.

- **Fallback MCP par curl** — **voie recommandée pour tout agent sans MCP natif** (même serveur `http://localhost:8002/mcp`, même sémantique : la mémoire écrite est immédiatement visible de `search_memory`, `read_memory` et de `GET /api/v1/memories/search`). Exige les headers `Accept: application/json, text/event-stream` :

```bash
curl -s -N -X POST http://localhost:8002/mcp -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"probe","version":"1"}}}'
# puis tools/list puis tools/call (search_memory, write_memory…) avec les même headers.
```

Ordre : MCP natif d'abord (outils `search_memory`, `write_memory`, …) → **Fallback MCP par curl** (recommandé sans MCP natif : mêmes résultats, write-back visible) → Fallback REST 8001 en dernier recours (trace d'audit via events). Ne jamais deviner d'endpoint.

### Règle 5 — MNEMO DOWN

Si Mnemolite ne répond pas (MCP indisponible ET `curl 8001/health` sans 200) : **stop**. Pas de recherche web, pas de conclusion. Signaler l'indisponibilité et demander la reprise une fois le socle rétabli.

## Registre par URL et tags

| Tag | Rôle |
|:--|:--|
| `project:book` / `project:truth-engine` / … | Périmètre du projet. Toujours injecter celui du périmètre courant. |
| `status:CONFIRME` / `status:VERIFIE` | Verdict forensique |
| `source:<sha1>` | Registre par URL — lookup « ai-je déjà vérifié cette URL ? » (`sha1(url)` tronqué à 10 hex) |
| `verifie-YYYY-MM-DD` | Date du write-back — re-vérification à la demande |
| `circuit-{N}` | circuit du livre (project:book uniquement) |
| `livre-cst` | tag maître du livre (project:book uniquement) |

## Forme de sortie d'une vérification

Toujours rendre sur un fait vérifié :

- Fait
- statut (`CONFIRME`/`VERIFIE`/`NON VÉRIFIÉ`)
- source : URL + date de publication + citation
- memory_id Mnemolite (nouveau ou existant)
- zéro appel web si statut CONFIRME récupéré

Contre-cas : si la source contredit le fait, écrire un write-back avec le fait corrigé et marquer le précédent via `update_memory` (`status` inchangé, tags dédiés de correction).

## Rappels du protocole

- L'agent qui écrit est l'agent qui vérifie. Pas de délégation.
- Ne pas deviner une URL. Une URL non lue n'existe pas.
- Un claim Mnemolite n'est pas une source — seule la lecture de la source (ou un write-back) fait foi.
- Chercher le contraire : antithèse acier, comparateurs symétriques.

## Validation

Suite d'épreuves rapide après toute utilisation :

1. Un fait déjà en mémoire `CONFIRME` → réponse avec source + citation + memory_id, **zéro appel web**.
2. Un fait nouveau → write-back produit une mémoire complète (URL + date + citation + tags).
3. Rewrite d'un même fait → doublon signalé → `update_memory`.
4. Mnemolite DOWN → stop, aucune conclusion.