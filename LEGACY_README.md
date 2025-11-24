# 🏷️ LEGACY v8.3 - Snapshot Pre-Optimization

## État Sauvegardé

**Date**: 2025-11-24
**Commit**: 9e817e5
**Tag**: v8.3-legacy
**Branche**: legacy-v8.3

## Métriques Baseline

### Taille du Système
- **system.md**: 1,109 lignes
- **KB total**: 12,108 lignes
- **Tokens contexte**: ~48,000
- **Fichiers KB chargés au démarrage**: 6
  - COGNITIVE_DSL (1,406 lignes)
  - PATTERNS (2,445 lignes)
  - SEARCH_EPISTEMIC (1,797 lignes)
  - QUERY_TEMPLATES (793 lignes)
  - QUERY_OPTIMIZATION (894 lignes)
  - VALIDATION (727 lignes)

### Fonctionnalités
- ✅ TEMPORAL CONTEXT avec date système dynamique
- ✅ Tous patterns fonctionnels
- ✅ Investigation SIMPLE/MEDIUM/COMPLEX/APEX
- ✅ WOLF protocol complet
- ✅ MCP integration (MnemoLite, Context7, WebSearch)
- ✅ Query optimization v8.3
- ✅ Investigation Tree (APEX)
- ✅ Forensic Reasoning

## Comment Revenir à cette Version

### Option 1: Checkout du Tag
```bash
git checkout v8.3-legacy
```

### Option 2: Basculer sur la Branche Legacy
```bash
git checkout legacy-v8.3
```

### Option 3: Reset Hard (⚠️ Destructif)
```bash
git reset --hard v8.3-legacy
```

### Option 4: Cherry-pick Specific Files
```bash
# Récupérer un fichier spécifique de la version legacy
git checkout v8.3-legacy -- system.md
git checkout v8.3-legacy -- kb/PATTERNS.md
```

## Prochaines Étapes (Optimization)

### Phase 1: Quick Wins (-36% system.md)
- [ ] Créer macros compactes pour YAML verbeux
- [ ] Compresser les conditions répétitives
- [ ] Externaliser exemples et edge cases

### Phase 2: KB Compression (-43% KB files)
- [ ] PATTERNS.md: Index compact + lazy-load
- [ ] SEARCH_EPISTEMIC.md: Formules en macros
- [ ] COGNITIVE_DSL.md: Dictionnaire aplati

### Phase 3: Lazy Loading Agressif
- [ ] Chargement conditionnel par complexité
- [ ] Patterns on-demand
- [ ] Cache intelligent

### Objectifs
- **Target**: -50% tokens (48k → 22k)
- **Temps première réponse**: -60% (8s → 3s)
- **Coût par investigation**: -58% ($0.12 → $0.05)

## Notes

Cette version LEGACY est entièrement fonctionnelle et testée. Elle sert de:
1. **Baseline** pour mesurer les gains de performance
2. **Rollback** en cas de régression
3. **Référence** pour la documentation

⚠️ **Ne pas supprimer** cette branche ou ce tag avant validation complète de v9.0