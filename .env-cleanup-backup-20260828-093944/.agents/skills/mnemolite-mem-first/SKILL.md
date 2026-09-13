---
name: mnemolite-mem-first
description: Mémoire persistante d’abord pour les faits. MCP natif 8002 en priorité ; fallback MCP-par-curl si le client MCP est défectueux. En investigation KERNEL, KERNEL reste propriétaire des exigences probatoires.
---

# mnemolite-mem-first

## 1. Autorité et périmètre

MnemoLite est la mémoire persistante canonique des faits et investigations.

Invariant :

```text
MEMORY != EVIDENCE
```

Ce skill définit comment retrouver et persister la mémoire. Il ne remplace jamais les règles probatoires de `truth-engine-v2/KERNEL.md` ou de `protocol/FACT_VERIFICATION.md`.

### Deux contextes

**Vérification factuelle ordinaire** : une mémoire `status:CONFIRME` correspondant exactement au fait peut être réutilisée sans appel web, sauf demande explicite de revalidation, fait contesté, état temporellement mouvant ou source devenue indisponible.

**Investigation KERNEL** : KERNEL possède la cadence. La mémoire sert de warm route (`memory_id`, fait, URL canonique, evidence key, date, gaps). Les exigences d’inspection du run courant restent celles de KERNEL.

## 2. Interface canonique

Ordre :

```text
1. MCP natif http://localhost:8002/mcp
2. fallback MCP-par-curl sur le même endpoint 8002
3. REST 8001 uniquement pour santé/recherche de dernier recours
```

Ne jamais explorer OpenAPI ou deviner des endpoints pendant une investigation.

Configuration globale attendue :

```text
/home/giak/.agents/mcp.json
```

Outils principaux :

```text
search_memory(query, search_mode="hybrid", ...)
read_memory(id)
write_memory(title, content, ...)
update_memory(id, ...)
get_system_snapshot(...)
get_memory_health()
```

## 3. Mémoire d’abord

Avant une vérification factuelle ordinaire :

```text
search_memory(query=<fait>, search_mode="hybrid", tags=[project:*], limit=10)
```

Si une URL est déjà connue, rechercher également son tag `source:<sha1-10-hex(url)>` si disponible.

Pour KERNEL, ne pas ajouter une boucle de recherche Mnemo indépendante : utiliser l’appel et le WARM_ROUTE prévus par KERNEL.

## 4. Consommation

### CONFIRME, hors KERNEL

Correspondance stricte du fait, de la source et du périmètre :

```text
CONFIRME -> réutiliser source_url + source_date + citation + memory_id
```

Pas de web automatique.

Revalider si au moins une condition est vraie :

- l’utilisateur le demande ;
- le fait décrit un état actuel ou mouvant ;
- une contradiction apparaît ;
- la source a dérivé ou disparu ;
- le contexte ou le périmètre diffère matériellement.

### VERIFIE

`status:VERIFIE` n’est pas `CONFIRME`. Reprendre la vérification requise par le livrable.

### KERNEL

```text
Mnemo HIT -> warm route -> KERNEL décide REFETCH/discovery
```

Le skill ne transforme jamais `CONFIRME` en exemption automatique d’`INSPECTED_TRACE_OK`.

## 5. Write-back

Après une vérification aboutie, écrire ou mettre à jour une mémoire canonique avec :

```text
title
a content factuel avec citation
memory_type
tags project:*
status:CONFIRME ou status:VERIFIE
source:<hash10>
verifie-YYYY-MM-DD
```

Si `duplicate_warning` est retourné, utiliser `update_memory` sur l’ID existant au lieu de créer un doublon.

Ne jamais écrire `status:CONFIRME` sans preuve répondant au niveau requis par le protocole propriétaire.

## 6. Fallback MCP-par-curl

Si le client voit le serveur mais expose un schéma d’outil invalide, journaliser :

```text
TOOL_SCHEMA_UNAVAILABLE
```

Puis utiliser le même serveur MCP via HTTP, sans changer de mémoire ni de sémantique.

Headers requis :

```text
Content-Type: application/json
Accept: application/json, text/event-stream
```

Séquence :

```text
initialize
-> tools/list
-> tools/call
```

Exemple d’appel logique :

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "search_memory",
    "arguments": {
      "query": "gilets jaunes",
      "search_mode": "hybrid",
      "limit": 10
    }
  }
}
```

Ne pas retenter plusieurs fois un appel dont le schéma client est structurellement vide ou contradictoire.

## 7. REST 8001

REST 8001 est un fallback de santé/recherche, pas le canal canonique de write-back.

Autorisé :

```text
GET /health
GET /api/v1/memories/search?query=...
```

Interdit comme write-back de mémoire canonique :

```text
POST /v1/events/
```

Cet endpoint écrit un event et ne remplace pas `write_memory`.

## 8. MnemoLite indisponible

Si le MCP natif échoue, le fallback MCP-par-curl échoue et `http://localhost:8001/health` est indisponible :

```text
MNEMO_UNAVAILABLE
```

Pour une investigation KERNEL, appliquer l’ON_FAIL de KERNEL. Pour une vérification ordinaire qui exige MnemoLite, ne pas prétendre avoir persisté le résultat.

## 9. Validation rapide

1. `tools/list` expose `search_memory`, `read_memory`, `write_memory`, `update_memory` avec leurs arguments.
2. Une recherche `hybrid` retourne les mémoires attendues.
3. `read_memory(id)` retourne le contenu complet.
4. `write_memory` ou `update_memory` est immédiatement relisible via `search_memory`.
5. En KERNEL, aucune exploration OpenAPI/REST n’a lieu tant que le MCP natif ou le fallback MCP fonctionne.
