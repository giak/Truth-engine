# Phase 1 : Quick Wins - Optimisation Contexte Claude Code

**Date** : 2024-11-24
**Status** : ✅ Implémenté, ⏳ À valider

## Changements effectués

### 1. `.claudeignore` créé
**Fichiers exclus du contexte automatique** :
- Documentation volumineuse : `TAD.md` (289KB), `PRD.md`, `PFD.md`, `VISION.md`
- Logs : `logs/`, `*.log`
- Tests : `tests/`
- Postmortems : `docs/postmortems/`
- Dépendances : `node_modules/`, `.venv/`, `__pycache__/`

**Gain estimé** : ~20-30% réduction contexte

### 2. `CLAUDE.md` minimaliste
**Avant** : 582 lignes, 24KB
**Après** : 74 lignes, 2.8KB
**Réduction** : **88%**

**Contenu conservé** :
- Essential files (pointeurs vers system.md, KB, TAD, PFD)
- Investigation commands (Basic, MCP, APEX)
- Key principles (résumé 6 points)
- Quality metrics (EDI, ISN, stratification)
- MCP integration (serveurs requis)
- Output structure
- Common pitfalls

**Contenu déplacé vers `CLAUDE_FULL.md`** :
- Philosophy détaillée (Empire of Lies, 5 fronts)
- Prism metaphor
- 10 Commandments complets
- Architecture détaillée
- Running investigations verbeux
- KB file reference
- Meta-development workflow

**Gain estimé** : ~15-25% réduction contexte

### 3. Hook `hook_read_context.sh` audité
**Verdict** : ✅ **Garder le hook**

**Analyse** :
- Injecte max 3 résultats MnemoLite (300 chars chacun)
- Coût : ~200-300 tokens par prompt
- Bénéfice : Mémoire contextuelle pertinente entre sessions
- Failsafe : Si MnemoLite down, échoue silencieusement (pas de blocage)

**MnemoLite status** : ✅ Actif (http://localhost:8001/health)

**Gain estimé** : 0% (hook conservé, coût acceptable)

## Gains cumulatifs Phase 1

| Optimisation | Gain estimé | Status |
|--------------|-------------|--------|
| `.claudeignore` | 20-30% | ✅ |
| `CLAUDE.md` minimaliste | 15-25% | ✅ |
| Hook audit | 0% (conservé) | ✅ |
| **TOTAL Phase 1** | **35-55%** | ✅ |

## Validation requise

### Test investigation SIMPLE

**Commande** :
```bash
cd /home/giak/projects/truth-engine
claude "Analyse: 'Unemployment 7.4% France'. Load system.md + kb/. Truth Engine protocol SIMPLE."
```

**Métriques à vérifier** :
1. ✅ Investigation se lance sans erreur
2. ✅ `system.md` chargé correctement
3. ✅ KB accessible via MnemoLite (pas de load complet)
4. ✅ EDI ≥ 0.30 (target SIMPLE)
5. ✅ Pas d'erreur "context exceeded"
6. ✅ TAD.md/PFD.md NON chargés automatiquement

**Baseline à comparer** :
- Avant Phase 1 : ~X tokens utilisés (à mesurer si `/stats` disponible)
- Après Phase 1 : ~Y tokens utilisés (devrait être 35-55% inférieur)

### Test investigation COMPLEX

**Commande** :
```bash
claude "Investigation COMPLEX: 'ARCOM composition members'. Load system.md. MnemoLite KB search. Target: EDI≥0.70."
```

**Métriques** :
1. ✅ EDI ≥ 0.70
2. ✅ Sources ≥ 10
3. ✅ Pas d'erreur contexte

## Rollback si nécessaire

Si les tests montrent une dégradation de qualité :

```bash
# Restaurer CLAUDE.md original
cp CLAUDE_FULL.md CLAUDE.md

# Désactiver .claudeignore (le renommer)
mv .claudeignore .claudeignore.disabled
```

## Prochaines étapes

**Phase 2** : MCP optimization (si Phase 1 validée)
- Lister outils MCP actifs
- Désactiver outils jamais utilisés
- Gain estimé : +10-20%

**Phase 3** : Structural optimizations
- Externaliser TAD.md/PFD.md (load on-demand)
- Claude Skills (2025 feature)
- Memory Bank stratégique
- Gain estimé : +30-50%

---

**Version** : Truth Engine v8.4
**Optimisation** : Phase 1 (Quick Wins)
**Baseline measurement** : À effectuer lors du test de validation
