# Plan de Mise à Jour des Markdowns Racine Truth Engine

**Date:** 2025-11-16
**Contexte:** Après commit majeur 53a954c (Investigation Tree, Query Optimization v8.3, architecture validée)
**Ampleur:** 6 fichiers obsolètes (11-09), ~400K lignes à revoir

---

## 📊 Analyse de la Situation

### État Actuel des Markdowns Racine

| Fichier | Taille | Dernière Modif | Statut | Priorité |
|---------|--------|----------------|--------|----------|
| **system.md** | 32K | 2025-11-15 | ✅ À JOUR | - |
| **CLAUDE.md** | 20K | 2025-11-14 | ⚠️ PARTIEL | HAUTE |
| **README.md** | 6.1K | 2025-11-09 | ❌ OBSOLÈTE | HAUTE |
| **TAD.md** | 283K | 2025-11-09 | ❌ OBSOLÈTE | CRITIQUE |
| **PRD.md** | 20K | 2025-11-09 | ❌ OBSOLÈTE | MOYENNE |
| **VISION.md** | 15K | 2025-11-09 | ❌ OBSOLÈTE | MOYENNE |
| **PFD.md** | 60K | 2025-11-09 | ❌ OBSOLÈTE | BASSE |
| **DASHBOARD.md** | 553B | 2025-11-09 | ❌ OBSOLÈTE | BASSE |

**Total à mettre à jour:** ~404K lignes (6 fichiers)

---

## 🎯 Changements Majeurs à Intégrer

Depuis 2025-11-09, Truth Engine a évolué significativement :

### 1. Query Optimization v8.3 (commit 1ffcbc5)
- Automatic query splitting (>5 keywords → 2-3 simple queries)
- Hybrid fallback (MCP DuckDuckGo → WebSearch Google)
- Productive query rate : 0-40% → 80-100%
- PRIMARY source discovery improved (+20-50%)

### 2. Investigation Tree (commit 53a954c + tests/tree/*)
- kb/INVESTIGATION_TREE.md (949 lignes nouveau KB)
- Tree depth protocols L0-L9
- COMPARABLES_ASYMMETRY analysis
- Multi-branch dialectical investigation
- Tests : 8 fichiers (PHASE1, PHASE2, simulations)

### 3. Architecture Dual-Engine VALIDÉE (commit 53a954c)
- Google Search MCP integration ABANDONED (post-mortem complet)
- Architecture actuelle OPTIMALE :
  - WebSearch (Google API) : 95%+ succès
  - MCP web-search (DuckDuckGo) : 60-80% succès
- Load testing : 25 requêtes, 0% succès Playwright scraping
- Decision documentée : docs/postmortems/

### 4. Configuration Claude Code
- WebSearch auto-approval (.claude/settings.local.json)
- MCP tools auto-approved (web-search, context7, mnemolite)
- Hooks nettoyés (auto-save-exchange.sh, auto-save-previous.sh)

### 5. Documentation Extensive
- docs/postmortems/ (Google Search MCP ABANDONED)
- docs/plans/archived/ (plans abandonnés)
- docs/memory/ (memory files)
- tests/query_optimization/ (6 fichiers audit/tests)
- tests/tree/ (12 fichiers validation Investigation Tree)
- prompts/ (7 fichiers TWEET generation/analysis)

---

## 📋 Plan d'Action Détaillé

### Phase 1 : Fichiers Critiques (Priorité HAUTE)

#### Task 1.1 : README.md (6.1K) - 15 min
**Obsolescence :** Manque Query Optimization v8.3, Investigation Tree, architecture validée

**Sections à mettre à jour :**
- Features actuelles (ajouter Query Optimization v8.3, Investigation Tree)
- Architecture (dual-engine WebSearch + MCP web-search)
- Quick Start (mentionner auto-approval configuré)
- Status badges (mettre v8.4 actuel)
- Links vers nouvelle doc (postmortems, plans)

**Approche :**
- Lire README.md actuel
- Identifier sections obsolètes
- Réécrire avec features v8.3/v8.4
- Ajouter liens vers Investigation Tree KB

---

#### Task 1.2 : CLAUDE.md (20K) - 30 min
**Obsolescence partielle :** Mis à jour 2025-11-14 mais manque :
- Investigation Tree workflow
- Query Optimization v8.4 automatic splitting
- Google Search MCP decision (abandonné)
- WebSearch auto-approval

**Sections à ajouter/modifier :**
- § "Query Optimization (v8.3 Automatic)" → Update to v8.4
- § "Investigation Tree" → NEW section explaining kb/INVESTIGATION_TREE.md usage
- § "MCP Integration" → Clarify WebSearch auto-approved, Google MCP NOT recommended
- § "Common Pitfalls" → Add "Don't try Google Search MCP (see postmortem)"

**Approche :**
- Read CLAUDE.md current state
- Add Investigation Tree section after Query Optimization
- Update MCP section with WebSearch auto-approval
- Add reference to docs/postmortems/ for Google Search decision

---

#### Task 1.3 : TAD.md (283K) - 90-120 min ⚠️ CRITIQUE
**Obsolescence :** Architecture technique complète obsolète

**GROS MORCEAU - Approche par sections :**

**Sections probablement obsolètes :**
1. § Architecture Search (dual-engine pas documenté correctement)
2. § Query Allocation (Query Optimization v8.3 pas intégré)
3. § MCP Servers (Google Search MCP mentionné? WebSearch pas clair?)
4. § Investigation Protocols (Investigation Tree pas documenté)
5. § Validation (VALIDATION.md mis à jour, TAD pas synchronisé)
6. § Performance Metrics (EDI boost dual-engine pas reflété)

**Stratégie TAD.md :**
- **Sous-tâche 1.3.1** (30 min) : Audit complet TAD.md → Identifier sections obsolètes précises
- **Sous-tâche 1.3.2** (20 min) : Architecture Search → Documenter WebSearch + MCP web-search dual-engine
- **Sous-tâche 1.3.3** (20 min) : Query Optimization → Intégrer v8.3 automatic splitting + hybrid fallback
- **Sous-tâche 1.3.4** (15 min) : Investigation Tree → Ajouter section kb/INVESTIGATION_TREE.md
- **Sous-tâche 1.3.5** (15 min) : MCP Integration → Clarifier WebSearch, web-search, context7, mnemolite (supprimer mention Google Search MCP si présente)
- **Sous-tâche 1.3.6** (10 min) : Performance Metrics → EDI boost dual-engine, ISN targets
- **Sous-tâche 1.3.7** (10 min) : Validation synchronisation avec kb/VALIDATION.md

**Total TAD.md :** 120 min

---

### Phase 2 : Fichiers Moyens (Priorité MOYENNE)

#### Task 2.1 : PRD.md (20K) - 25 min
**Obsolescence :** Product Requirements pas à jour avec v8.3/v8.4 features

**Sections à mettre à jour :**
- § Requirements → Query Optimization v8.3 automatic (DONE)
- § Requirements → Investigation Tree (DONE)
- § Non-Requirements → Google Search MCP integration (explicitly REJECTED, reference postmortem)
- § Success Criteria → EDI targets v8.4, productive query rate 80-100%

**Approche :**
- Read PRD.md actuel
- Mark Query Optimization v8.3 as IMPLEMENTED (was requirement, now done)
- Add Investigation Tree as IMPLEMENTED
- Add Google Search MCP to Non-Requirements with link to postmortem
- Update success metrics avec v8.4 targets

---

#### Task 2.2 : VISION.md (15K) - 20 min
**Obsolescence :** Roadmap pas à jour, features complétées pas marquées

**Sections à mettre à jour :**
- § Completed Features → Ajouter Query Optimization v8.3, Investigation Tree
- § Roadmap → Retirer Google Search MCP (abandoned)
- § Future Enhancements → Clarifier ce qui reste à faire vs. déjà fait
- § Meta-Development → Mentionner postmortem workflow (docs/postmortems/)

**Approche :**
- Read VISION.md current roadmap
- Move Query Optimization, Investigation Tree to "Completed Features"
- Remove Google Search MCP from roadmap (ou marquer REJECTED)
- Add section on postmortem-driven decision-making

---

### Phase 3 : Fichiers Basse Priorité

#### Task 3.1 : PFD.md (60K) - 30 min (optionnel)
**Obsolescence faible :** Philosophie stable, peu de changements

**Potentielles mises à jour :**
- § Epistemology → Mentionner Investigation Tree comme concrétisation prism metaphor
- § Examples → Ajouter exemples avec Query Optimization v8.3
- § 148 Concepts → Vérifier si Investigation Tree ajoute nouveaux concepts

**Approche :**
- Skim PFD.md rapidement
- Identifier si philosophie Investigation Tree apporte nouveaux concepts
- Si oui, ajouter section
- Si non, skip (BASSE priorité)

---

#### Task 3.2 : DASHBOARD.md (553B) - 5 min
**Obsolescence :** Probablement dashboard metrics obsolètes

**Approche :**
- Read DASHBOARD.md (très court)
- Update metrics si nécessaire (EDI, ISN, version)
- Si inutile, considérer suppression

---

## 🔧 Stratégie d'Exécution

### Option A : Séquentiel (Recommandé pour qualité)
1. Phase 1 Task 1.1 README.md (15 min)
2. Phase 1 Task 1.2 CLAUDE.md (30 min)
3. Phase 1 Task 1.3 TAD.md (120 min) ← GROS MORCEAU, faire en 7 sous-tâches
4. Phase 2 Task 2.1 PRD.md (25 min)
5. Phase 2 Task 2.2 VISION.md (20 min)
6. Phase 3 Tasks (35 min optionnel)

**Total temps estimé :** 210 min (3h 30min) + optionnel 35 min

### Option B : Parallèle (Risqué, incohérences possibles)
- Dispatcher 3 subagents pour Phase 1, Phase 2, Phase 3
- Risque : incohérences entre fichiers si changements interdépendants
- Gain temps : 2h max au lieu de 3h 30min

**Recommandation :** Option A séquentiel, surtout pour TAD.md (283K, interdépendances)

---

## 📌 Précautions

### Avant de Commencer
1. ✅ Commit actuel propre (53a954c)
2. ✅ Backup implicite via git history
3. ⚠️ Vérifier que system.md (32K) n'a pas besoin update (dernière modif 2025-11-15)

### Pendant Exécution
- **Commits intermédiaires** après chaque phase
- **Validation croisée** : CLAUDE.md ↔ TAD.md ↔ README.md cohérence
- **References exactes** : Vérifier tous les liens vers kb/, docs/, tests/

### Après Mise à Jour
- **Commit final** : "docs: Update root markdowns to v8.4 (Query Optimization + Investigation Tree)"
- **Validation** : Lire README.md + CLAUDE.md end-to-end pour cohérence
- **Tag git** : Considérer tag v8.4 sur ce commit

---

## 🎯 Critères de Succès

### Validation Checklist
- [ ] README.md mentionne Query Optimization v8.3, Investigation Tree
- [ ] CLAUDE.md a section Investigation Tree workflow
- [ ] TAD.md architecture dual-engine WebSearch + MCP web-search documentée
- [ ] TAD.md Query Optimization v8.3 intégré (automatic splitting, hybrid fallback)
- [ ] PRD.md marque Query Optimization, Investigation Tree comme IMPLEMENTED
- [ ] VISION.md roadmap à jour (features complétées déplacées)
- [ ] Tous markdowns référencent docs/postmortems/2025-11-16-google-search-mcp-ABANDONED.md
- [ ] Aucune mention positive de Google Search MCP (seulement REJECTED/ABANDONED avec lien postmortem)
- [ ] Links internes valides (kb/INVESTIGATION_TREE.md, tests/tree/, etc.)

---

## 📝 Notes Importantes

### Décisions Documentées
- **Google Search MCP:** ABANDONNÉ (0% success rate), voir docs/postmortems/
- **Architecture:** WebSearch (Google API) + MCP web-search (DuckDuckGo) = OPTIMAL
- **Query Optimization:** v8.3 automatic splitting INTÉGRÉ
- **Investigation Tree:** kb/INVESTIGATION_TREE.md opérationnel, tests validés

### Références Clés
- Commit majeur : 53a954c
- Post-mortem Google Search : docs/postmortems/2025-11-16-google-search-mcp-ABANDONED.md
- Investigation Tree KB : kb/INVESTIGATION_TREE.md (949 lignes)
- Query Optimization tests : tests/query_optimization/* (6 fichiers)
- Investigation Tree tests : tests/tree/* (12 fichiers)

---

**FIN DU PLAN**

Prêt pour exécution séquentielle Phase 1 → Phase 2 → Phase 3.
Durée estimée : 3h 30min + 35min optionnel.
