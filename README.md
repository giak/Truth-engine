# Truth Engine

**Système d'analyse cognitive pour détecter la manipulation dans les discours.**

**Version**: 11.0  
**Statut**: Production-ready

---

## Quick Start

```
1. Colle KERNEL.md dans la session LLM
2. Lance une analyse: "Analyse: [sujet]"
3. Reçois un rapport structuré
```

---

## Documentation Centrale

| Doc | Description | Quand lire |
|-----|-------------|------------|
| **[VISION.md](docs/VISION.md)** | Philosophie, principes, comment ça marche | Pour comprendre POURQUOI |
| **KERNEL.md** | Phases, formules, DSL, règles d'exécution | Pour exécuter une investigation |
| **[docs/STRUCTURE.md](docs/STRUCTURE.md)** | Architecture complète du projet | Pour naviguer |
| **[docs/user/PHILOSOPHY.md](docs/user/PHILOSOPHY.md)** | Contexte pédagogique approfondi | Pour aller plus loin |

---

## État du Projet

### Ce qui fonctionne ✓
- Investigation simple, complexe, APEX
- MnemoLite intégration (mémoire longue)
- EDI, ISN, Wolves métriques
- 19 clusters de patterns

### En cours / À faire
- [ ] Audit DSL v11 (en cours)
- [ ] Benchmarking en cours
- [ ] Nouveaux patterns selon besoins

### Problèmes Connus
- H7 coverage parfois insuffisant
- EDI target pas toujours atteint sur APEX

---

## Structure du Projet

```
truth-engine/
├── KERNEL.md                    # Point d'entrée — CHARGÉ EN PREMIER
├── docs/
│   ├── VISION.md               # PHILOSOPHIE — Lis ceci en premier
│   ├── STRUCTURE.md            # Architecture complète
│   ├── user/
│   │   ├── PHILOSOPHY.md      # Contexte détaillé
│   │   └── USER_GUIDE.md      # Guide utilisateur
│   ├── specs/
│   │   ├── PRD.md             # Requirements
│   │   └── SCL_NOTATION.md   # Notation compressée
│   └── audits/                 # Rapports d'audit
│
├── kb/                         # KNOWLEDGE BASE
│   ├── dsl/                   # DSL definitions
│   │   ├── COGNITIVE_DSL.md
│   │   └── COGNITIVE_DSL_CORE.md
│   ├── patterns/               # 19 clusters
│   │   ├── CLUSTER_ICEBERG.md
│   │   ├── CLUSTER_MONEY.md
│   │   └── ... (16 autres)
│   └── protocols/              # Investigation protocols
│       ├── INVESTIGATION.md
│       └── INVESTIGATION_TREE.md
│
├── investigations/            # Rapports d'investigation
├── outputs/                   # Productions (articles, social)
├── tools/                    # Infrastructure (tests, prompts)
└── logs/                    # Logs historiques
```

---

## Métriques Actuelles

| Métrique | Cible | Statut |
|----------|-------|--------|
| **EDI** | ≥0.80 (APEX) | En amélioration |
| **Sources** | ≥20 (APEX) | ✓ |
| **Wolves** | ≥8 | ✓ |
| **Clusters** | 19 | ✓ |

---

## Commands Utiles

```bash
# Investigation simple
"Analyse: [sujet]. Truth Engine protocol."

# Investigation APEX
"Investigation APEX: [sujet complexe]. Target EDI≥0.80."

# Avec mémoire MnemoLite
"Use MnemoLite MCP pour recall investigations similaires."
```

---

## Logs & Traces

Les investigations passées sont sauvegardées dans:
- `investigations/` — Rapports d'investigation
- `outputs/investigations/` — Rapports complets
- `outputs/simulations/` — Simulations APEX
- **MnemoLite** — Base vectorielle (recherche sémantique)

Pour voir les dernière investigations:
```bash
ls -lt outputs/investigations/ | head -10
```

---

## Évolution

**Boucle**: Investigation → Métriques → Feedback → Amélioration → Investigation

**Comment contribuer**:
1. Lance une investigation
2. Note les failles (EDI bas, pattern manquant, etc.)
3. Mets à jour les fichiers kb/
4. Commit avec description de l'amélioration

**Pas de roadmap complexe**. Use → feedback → improve → repeat.

---

## Fichiers Clés

| Fichier | Rôle |
|---------|------|
| `KERNEL.md` | Cœur opérationnel |
| `kb/dsl/COGNITIVE_DSL_CORE.md` | Primitives Ξ € Λ Ω Ψ ↕ |
| `kb/patterns/CLUSTER_*.md` | 19 clusters de manipulation |
| `investigations/` | Investigations récentes |
| `outputs/investigations/` | Toutes les investigations |

---

## Pour Commencer

1. **Lis [VISION.md](docs/VISION.md)** — Comprendre la philosophie
2. **Lis KERNEL.md** — Comprendre l'exécution
3. **Lance une investigation** — "Analyse: chômage France 2024"

---

**Truth Engine v11** — Utiliser → Apprendre → Évoluer → Répéter
