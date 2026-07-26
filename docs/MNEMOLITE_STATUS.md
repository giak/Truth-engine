# knowledge.md

> Source canonique : `../knowledge.md` (règles méta-projet), `../AGENTS.md` (règles agent).
> Statut session-bound 2026-07-14. Zéro tiret cadratin (U+2014). Wall-clock-honnête.

## Mnemolite : STATUT ÉTABLI (curator-asserted 2026-07-14)

**« Mnemolite FONCTIONNE »** : assertion curator-asserted, valable jusqu'à preuve contraire par audit contradictoire curator. Ne pas l'invalider sur faux positif d'audit basher.

**Procédure canonique de vérification** (si doute isolé) : 1 commande, exécution rapide :

```bash
rtk mnemo health
```

**Anti-pattern interdit** : audit basher de disponibilité (`curl http://localhost:8002/health`, scan ports, ping). Procédure officielle d'interrogation : `tools/call` MCP avec `params: {name, arguments}` et `search_mode: "hybrid"`.

**Si Mnemolite DOWN malgré le statut établi** : trust curator, retry 1 fois avec `rtk mnemo health`, puis escalade courte. NE PAS diagnostiquer l'infra réseau/ports.
