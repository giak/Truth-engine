# 🚀 Truth Engine Optimization Roadmap

## Vision
Réduire la consommation de tokens de **50%** tout en maintenant 100% des fonctionnalités.

## Principes Directeurs

1. **KISS** - Compression simple avant complexe
2. **Mesurer** - Baseline avant/après chaque changement
3. **Tester** - Régression tests à chaque phase
4. **Documenter** - Chaque macro/symbole expliqué
5. **Réversible** - Pouvoir rollback à tout moment

---

## 📊 Métriques Cibles

| Métrique | v8.3 Legacy | v9.0 Target | Gain |
|----------|------------|------------|------|
| Lignes totales | 12,108 | 6,000 | -50% |
| Tokens contexte | 48,000 | 22,000 | -54% |
| Temps 1ère réponse | 8s | 3s | -63% |
| Coût/investigation | $0.12 | $0.05 | -58% |
| RAM utilisée | 52% | 23% | -56% |

---

## 🎯 Phase 1: Quick Wins System.md
**Timeline**: 2-3 jours
**Impact**: -400 lignes (-36%)

### 1.1 Macros YAML
```yaml
# AVANT (10 lignes)
IF condition:
  → STATUS: **WARNING**
  → OUTPUT: "Long message..."
  → ACTION: Do something
  → CONTINUE

# APRÈS (1 ligne)
IF condition: →WARN[msg,action]
```

### 1.2 Tables de Décision
Remplacer les IF/ELIF cascadés par des lookup tables compactes.

### 1.3 Externalisation
- `kb/EXAMPLES/` - Tous les exemples
- `kb/EDGE_CASES.md` - Cas rares
- `kb/DEV_NOTES.md` - Commentaires développeur

### Fichiers à Modifier
- [ ] system.md lignes 50-300 (TEMPORAL CONTEXT)
- [ ] system.md lignes 310-550 (USER POSITION DETECTION)
- [ ] system.md lignes 600-850 (VALIDATION loops)

---

## 🎯 Phase 2: PATTERNS.md Refactor
**Timeline**: 3-4 jours
**Impact**: -1,600 lignes (-65%)

### 2.1 Index Compact
```yaml
# patterns_index.yaml (50 lignes max)
ICEBERG:
  code: Ξ
  threshold: 7
  file: patterns/iceberg.md  # Lazy-load si triggered
MONEY:
  code: €
  threshold: 6
  file: patterns/money.md
```

### 2.2 SCL (Symbolic Compression Language)
Utiliser la notation ultra-compacte déjà définie:
```
Ξ7→ICEBERG_FULL  # Si score≥7, charger définition complète
€6→MONEY_FULL
```

### 2.3 Pattern Bundles
```yaml
POLITICAL_BUNDLE: [ICEBERG,FRAMING,SPECTACLE,GASLIGHTING]
FINANCIAL_BUNDLE: [MONEY,BIO,NET]
WARFARE_BUNDLE: [WAR,TEMP,DOXA]
```

---

## 🎯 Phase 3: KB Stratified Loading
**Timeline**: 4-5 jours
**Impact**: -2,000 lignes contexte adaptatif

### 3.1 Core Minimal (~1000 lignes)
```yaml
ALWAYS_LOAD:
  - kb/COGNITIVE_DSL_MINI.md  # 300L - Symbols only
  - kb/PATTERNS_INDEX.md       # 50L - Index only
  - kb/FORMULAS_CORE.md        # 200L - EDI/ISN macros
```

### 3.2 Complexity-Based Loading
```yaml
SIMPLE:
  base: ALWAYS_LOAD
  extra: []  # Rien

MEDIUM:
  base: ALWAYS_LOAD
  extra: [SEARCH_EPISTEMIC_CORE]  # +300L

COMPLEX:
  base: ALWAYS_LOAD
  extra: [SEARCH_FULL, VALIDATION, QUERY_TEMPLATES]  # +800L

APEX:
  base: ALWAYS_LOAD
  extra: [ALL_KB]  # Full power mode
```

### 3.3 Domain-Based Loading
```yaml
IF subject contains ["GDP","inflation","economy"]:
  LOAD: [FINANCIAL_BUNDLE, MONEY_PATTERNS]

IF subject contains ["war","military","defense"]:
  LOAD: [WARFARE_BUNDLE, GEOPOLITICAL_KB]
```

---

## 🎯 Phase 4: DSL Ultra-Compact
**Timeline**: 5-6 jours
**Impact**: -1,500 lignes (compression 3:1)

### 4.1 Truth Engine Shorthand (TES)
```
# Notation actuelle (5 lignes)
Execute web searches
Validate sources
Calculate metrics
Output results

# Notation TES (1 ligne)
→WS→VAL→CALC→OUT
```

### 4.2 Commandes Atomiques
```yaml
# Dictionnaire de base (50 commandes)
WS: Web Search
VAL: Validate
CALC: Calculate
OUT: Output
CHK: Check
RTY: Retry
...
```

### 4.3 Pipelines Composables
```
→WS[MCP,10]|VAL[◈≥3]|EDI[]|OUT[P1:FR,P2:TECH,P3:WOLF]
```

---

## 🧪 Tests de Régression

### Suite de Tests Minimale
1. **test_simple.sh** - Investigation SIMPLE basique
2. **test_medium.sh** - Investigation MEDIUM avec patterns
3. **test_complex.sh** - Investigation COMPLEX avec WOLF
4. **test_apex.sh** - Investigation APEX avec Tree
5. **test_edge_cases.sh** - Cas limites et erreurs

### Métriques à Valider
- [ ] EDI scores identiques (±0.05)
- [ ] Patterns détectés identiques
- [ ] WOLF actors identiques
- [ ] Temps de réponse amélioré
- [ ] Tokens consommés réduits

---

## 📅 Timeline Global

| Semaine | Phase | Livrable | Test |
|---------|-------|----------|------|
| S1 (25-29 Nov) | Phase 1 | system.md optimisé | ✓ |
| S2 (2-6 Dec) | Phase 2 | PATTERNS.md refactoré | ✓ |
| S3 (9-13 Dec) | Phase 3 | Loading stratifié | ✓ |
| S4 (16-20 Dec) | Phase 4 | DSL compact | ✓ |
| S5 (23-27 Dec) | Integration | v9.0-beta | ✓ |
| S6 (30 Dec-3 Jan) | Validation | v9.0-release | ✓ |

---

## ⚠️ Risques et Mitigations

| Risque | Impact | Mitigation |
|--------|--------|------------|
| Perte de fonctionnalité | HIGH | Tests régression à chaque commit |
| Confusion macros | MEDIUM | Documentation exhaustive |
| Complexité debugging | MEDIUM | Mode verbose/debug |
| Résistance utilisateur | LOW | Migration graduelle |
| Performance dégradée | LOW | Benchmarks continus |

---

## 📝 Checklist Pre-Launch

- [ ] Backup v8.3 complet ✅ (fait)
- [ ] Tag et branche legacy ✅ (fait)
- [ ] Documentation legacy ✅ (fait)
- [ ] Tests baseline créés
- [ ] Métriques actuelles mesurées
- [ ] Plan approuvé
- [ ] Environnement test isolé

---

## 🎉 Success Criteria

Une investigation COMPLEX doit:
- Consommer **<25,000 tokens** (vs 48,000 actuels)
- Répondre en **<4 secondes** (vs 8 actuels)
- Maintenir **EDI ≥0.70**
- Détecter **tous les patterns** comme v8.3
- Coûter **<$0.06** (vs $0.12 actuels)

---

**Ready to start Phase 1?** 🚀