# AGENT.md

> Configuration agent pour la session Truth Engine.
> Sources de vérité : `../AGENTS.md` (règles agent complètes), `../knowledge.md` (STATUT Mnemolite + référentiel canonique racine) — design « chaque règle en un seul endroit ».

## Mnemolite

Trust curator sur `« Mnemolite FONCTIONNE »`. Vérification si doute : `rtk mnemo health` (1 commande). Procédure canonique : `tools/call` MCP avec `params: {name, arguments}` et `search_mode: "hybrid"`.

## Posture session

Anti-sycophancy stricte. Français soutenu, zéro em-dash (U+2014, conventions typographiques du manuscrit dans `book/`), zéro anglicisme, guillemets français `« »`, espaces insécables avant `:`. Wall-clock-honnête (jamais de timestamp inventé). RTK obligatoire pour toute commande shell.
