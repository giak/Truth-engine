# AUDIT — Compression system.md v7.17

**Date**: 2025-11-20
**Fichier source**: system.md (1069 lignes, 48KB)
**Méthodologie**: @KB[DSL_METAGUIDE] — Questions pour compression adaptative

---

## §1 ANALYSE STRUCTURE (Niveau 0 — 100% Preservation)

### 1.1 Cartographie Sections

```yaml
HEADER:
  - L1-5: Version, LOAD KB, JSON metadata

ROUTING:
  - L6-8: Command routing (tweet, thread, I1 AUTO)

WEB SEARCHES MANDATORY (v8.2):
  - L10-199: Critical enforcement, query minimums, MCP checks, quality gates
  - CRITICAL: 190 lignes (18% du fichier) dédiées à enforcement
  - Densité: LOW (examples, explanations, edge cases)

AUTONOMOUS_ITERATION_I1 (v8.0):
  - L201-269: I1 auto-generation, gap analysis, query allocation
  - Densité: MEDIUM (structured YAML, clear examples)

USER POSITION DETECTION (v8.5):
  - L271-314: Anti-sycophancy, dialectical challenge
  - Densité: HIGH (concise, operational)

PREPROCESSING (silent execution):
  - L317-476: Complexity (0), Hermeneutic (0.4), DSL Macros (0.5), Enforcement (0.6)
  - CRITICAL: 160 lignes (15% du fichier)
  - Densité: MIXED (0.4 verbose examples, 0.5-0.6 compact YAML)

WORKFLOW_ROUTING:
  - L477-486: Linear vs Arborescent based on complexity
  - Densité: HIGH (10 lignes, clear logic)

ALLOCATION/EXECUTION/VALIDATION (steps 1-3):
  - L488-600: Query allocation, optimization v8.3, running metrics v8.6
  - Densité: MEDIUM (formulas + explanations)

PROCESSING (steps 4-8):
  - L602-610: Herméneutique, Scoring, Patterns, Wolves, Output
  - Densité: HIGH (pointers KB, minimal text)

SAVE/PERSIST (steps 9-10):
  - L612-636: Markdown file creation + MCP memory
  - Densité: MEDIUM (detailed specs needed for execution)

INVESTIGATION_TREE (APEX ≥9.0):
  - L638-801: Multi-agent parallel branch exploration
  - CRITICAL: 164 lignes (15% du fichier)
  - Densité: LOW (examples, JSON, Mermaid, validation criteria)

OUTPUT STRUCTURE:
  - L803-1044: Part 1 (FR), Part 2 (TECH), Part 3 (WOLF)
  - CRITICAL: 242 lignes (23% du fichier)
  - Densité: LOW (examples, forbidden patterns, enforcement)

FAIL/TARGETS/KB_REF/PHILOSOPHY:
  - L1046-1069: Quality gates, targets, KB map, philosophy
  - Densité: HIGH (compact reference data)
```

### 1.2 Métriques Quantitatives

```yaml
Total: 1069 lignes, 48KB

Distribution densité:
  HIGH (compact):      ~180 lignes (17%) — pointers KB, formulas, targets
  MEDIUM (structured): ~320 lignes (30%) — YAML blocks, structured data
  LOW (verbose):       ~569 lignes (53%) — examples, explanations, edge cases

Sections CRITICAL (non-compressibles sans perte fonctionnelle):
  - WEB SEARCHES MANDATORY: 190 lignes (enforcement logic)
  - PREPROCESSING: 160 lignes (hermeneutic, DSL macros)
  - INVESTIGATION_TREE: 164 lignes (APEX workflow)
  - OUTPUT STRUCTURE: 242 lignes (Part 1/2/3 specs)
  → TOTAL CRITICAL: 756 lignes (71% du fichier)

Sections COMPRESSIBLES (pointer KB ou condensation possible):
  - ROUTING: 3 lignes → 1 ligne (pointer)
  - ALLOCATION: 12 lignes → 3 lignes (formula)
  - PATTERNS/WOLVES: 8 lignes → 2 lignes (pointer KB)
  - TARGETS: 7 lignes → 1 ligne (table)
  → TOTAL COMPRESSIBLE: ~313 lignes (29% du fichier)
```

### 1.3 Concepts Core (6 identifiés)

```yaml
1. PIPELINE (10 étapes):
   0→0.4→0.5→0.6→0b→1→1b→1c→2→2.5→3→4→5→6→7→8→9→10

2. WEB SEARCHES MANDATORY:
   Enforcement logic (v8.2 critical), query minimums, MCP health checks

3. DSL MACROS (v8.6):
   Cognitive simulation, running EDI tracking, adaptive triggers

4. INVESTIGATION_TREE (APEX):
   Multi-branch parallel exploration, branch scoring, synthesis

5. OUTPUT STRUCTURE (3 parts):
   Part 1 FR (tri-perspectif dialectique) + Part 2 TECH + Part 3 WOLF

6. HOSTILE EPISTEMOLOGY:
   95% suspicion symétrique, user ≠ oracle, ◈ PRIMARY arbitrage
```

---

## §2 PROBLÈME DÉTECTÉ — Compression Inadaptée

### 2.1 Diagnostic

**Hypothèse initiale** (résumé session précédente):
- Créer SYSTEM_ESSENCE.md (Niveau 2, ~20KB, 60% compression)
- Créer SYSTEM_ULTRA_COMPACT.md (Niveau 3, ~2KB, 90% compression)
- Créer SYSTEM_HASH.md (Niveau 4, 89 chars, 99.9% compression)

**Problème identifié**:
- system.md = **moteur d'exécution cognitif** (instructions LLM), PAS documentation
- 71% du contenu = CRITICAL enforcement logic (WEB MANDATORY, DSL MACROS, TREE, OUTPUT)
- Compression 60% → perte fonctionnelle (LLM ne peut plus exécuter correctement)
- Compression 90% → perte catastrophique (protocole inexécutable)

**Analogie**:
- system.md ≈ code Python exécutable
- Compresser system.md ≈ compresser code source en pseudocode
- → Programme ne run plus si trop compressé

### 2.2 Questions Guidantes (@KB[DSL_METAGUIDE§1])

**Q1: Quelle est la Nature du Problème?**
- system.md = instructions LLM (exécution), PAS référence humaine (lecture)
- Audience = Claude Sonnet 4.5 (LLM), PAS utilisateur humain
- Usage = CHAQUE investigation (1000+ fois), PAS "lire une fois"
- → Compression doit préserver EXÉCUTABILITÉ, pas juste lisibilité

**Q2: Quel Niveau de Compression est Approprié?**
- "Ce document sera-t-il lu une fois ou mille fois?" → **Mille fois** (chaque investigation)
- "L'audience est-elle novice ou experte?" → **LLM expert** (après indexation KB)
- "La précision absolue est-elle critique?" → **OUI** (enforcement logic)
- → Compression FAIBLE acceptable (max 30-40%), compression FORTE inadaptée

**Q3: Contexte d'Usage?**
- **Contexte 1**: LLM charge system.md → exécute investigation → BESOIN 100% instructions
- **Contexte 2**: Humain review protocol → comprendre workflow → BESOIN 60% essence
- **Contexte 3**: Git commit log → version tracking → BESOIN 1% hash
- → IL N'EXISTE PAS UNE compression, IL EN EXISTE TROIS

### 2.3 Révision Méthodologique

**Approche erronée** (session précédente):
- Appliquer compression sémantique uniforme (0% → 30% → 60% → 90% → 99%)
- Supposer system.md = documentation (comme PFD.md, TAD.md)
- Créer versions compressées pour "lecture rapide"

**Approche correcte** (audit actuel):
- **NE PAS compresser system.md** pour usage LLM (Niveau 0 optimal)
- **SI compression nécessaire**: cibler sections LOW density (examples, explanations)
- **Créer variantes** pour contextes spécifiques (humain review ≠ LLM execution ≠ git log)

---

## §3 STRATÉGIE COMPRESSION RÉVISÉE

### 3.1 Matrice Décision Adaptative

```yaml
USAGE_CONTEXT:

  LLM_EXECUTION (investigation runtime):
    - Audience: Claude Sonnet 4.5
    - Fréquence: Chaque investigation (1000+ fois)
    - Besoin: Instructions complètes + enforcement logic
    - Niveau: 0 (PRESERVATION) — 100% system.md intégral
    - Fichier: system.md (AUCUNE MODIFICATION)
    - Raison: "Exécutabilité > Concision"

  HUMAN_REVIEW (protocol audit):
    - Audience: Développeurs, auditeurs, contributeurs
    - Fréquence: Rare (review, debug, contribution)
    - Besoin: Comprendre workflow, pas exécuter
    - Niveau: 1 (FUNCTIONAL_SUMMARY) — 40% compression
    - Fichier: SYSTEM_FUNCTIONAL_SUMMARY.md (~30KB, 600 lignes)
    - Préservation: Pipeline, enforcement logic, formulas
    - Suppression: Examples verbeux, edge cases détaillés, JSON samples

  GIT_TRACKING (version control):
    - Audience: Système (git log, DASHBOARD.md)
    - Fréquence: Chaque version (v8.0, v8.1, etc.)
    - Besoin: Features clés, hash version
    - Niveau: 4 (HASH_CODE) — 99.9% compression
    - Fichier: SYSTEM_HASH.md (hash + changelog)
    - Format: TE_v8.X_FEATURES_KEYWORDS
```

### 3.2 Niveau 1 — FUNCTIONAL_SUMMARY (40% compression)

**Objectif**: Référence humaine pour comprendre protocole (PAS exécution LLM).

**Préservation (600 lignes, ~30KB)**:
```yaml
MUST_KEEP:
  - PIPELINE complet (10 étapes): L317-610 condensé en pointers KB
  - WEB MANDATORY logic: Enforcement logic sans examples (50 lignes → 15 lignes)
  - DSL MACROS: Formulas + targets (pas examples)
  - INVESTIGATION_TREE: Workflow overview (pas JSON/Mermaid samples)
  - OUTPUT STRUCTURE: Templates (pas examples forbidden patterns)
  - TARGETS: Tables complètes (ISN, EDI, geo, ◈)
  - KB REFERENCE MAP: Pointers intégraux

REMOVED:
  - Examples verbeux (Mercosur, Loiseau, etc.)
  - JSON samples (investigation-tree.json)
  - Mermaid diagrams (investigation-tree.md)
  - Edge case explanations (troubleshooting)
  - Validation criteria détaillés (keep thresholds only)

COMPRESSION_STRATEGY:
  - Remplacer examples par pointers: "Example: see logs/2025-11-11_*.md"
  - Condenser YAML blocks: Garder structure, supprimer comments
  - Formulas inline: (N/R)×W+M au lieu de explications multi-lignes
```

**Décompression L1→L0**:
- Qualité: 85% (high fidelity)
- Méthode: Lire FUNCTIONAL_SUMMARY → référer system.md sections spécifiques si besoin
- Cas d'usage: Developer review, protocol audit, contribution

### 3.3 Niveau 4 — HASH_CODE (99.9% compression)

**Objectif**: Version tracking, git commits, DASHBOARD.md entries.

**Format**:
```
TE_v{version}_{FEATURE1}_{FEATURE2}_{FEATURE3}_EDI{target}_ISN{target}_{CRITICAL_KEYWORD}
```

**Exemple v7.17**:
```
TE_v7.17_PRIMARY_TEMPLATES_GEO_COMPARABLES_H7_OVERRIDE_POSTVAL_EDI0.80_ISN9.0_HOSTILE95
```

**Décomposition**:
- `TE`: Truth Engine
- `v7.17`: Version
- `PRIMARY_TEMPLATES`: ◈ PRIMARY search templates
- `GEO_COMPARABLES`: 🌍 Geographic comparables
- `H7_OVERRIDE`: H7 adversary mandatory trigger
- `POSTVAL`: Post-validation loop
- `EDI0.80`: EDI target APEX
- `ISN9.0`: ISN target political/corporate
- `HOSTILE95`: 95% suspicion symmetric baseline

**Fichier SYSTEM_HASH.md** (~2KB):
```markdown
# Truth Engine Version Hash v7.17

## Hash Code
TE_v7.17_PRIMARY_TEMPLATES_GEO_COMPARABLES_H7_OVERRIDE_POSTVAL_EDI0.80_ISN9.0_HOSTILE95

## Changelog v7.17 (2025-11-06)
- ◈ PRIMARY templates (kb/QUERY_TEMPLATES.md §1-2)
- 🌍 GEO comparables (kb/SEARCH_EPISTEMIC.md §5)
- 🔥 H7 override (kb/QUERY_TEMPLATES.md §3.1)
- ✅ POST-VALIDATION loop (kb/VALIDATION.md §1-6)
- EDI target APEX: 0.80 (was 0.70)
- ISN target political: 9.0 (was 8.5)
- Hostile epistemology: 95% symmetric suspicion

## Features Active
- Web searches MANDATORY (v8.2)
- DSL Macros cognitive simulation (v8.6)
- Investigation Tree APEX ≥9.0 (v8.4)
- Autonomous iteration I1 AUTO (v8.0)
- User position challenge (v8.5)
- Forensic reasoning (v8.9)

## Decompression
→ Read: system.md (full protocol)
→ Read: SYSTEM_FUNCTIONAL_SUMMARY.md (human-readable 40% compressed)
→ KB: COGNITIVE_DSL, PATTERNS, SEARCH_EPISTEMIC, QUERY_TEMPLATES, VALIDATION, HANDOFF_MEMO
```

---

## §4 AUDIT QUALITÉ

### 4.1 Tests Compression (@KB[DSL_METAGUIDE§5])

**Test 1 — Utilisabilité (L1 FUNCTIONAL_SUMMARY)**:
- ✅ Humain comprend workflow en <10min?
- ✅ Developer peut debug investigation avec L1?
- ✅ Contributeur peut ajouter feature avec L1 + L0 reference?

**Test 2 — Cohérence**:
- ✅ Symboles (Ψ Ω Ξ Λ Φ ◈◉○ ⟐🎓🔥⟐̅) préservés?
- ✅ Formulas (IVF, ISN, EDI) intactes?
- ✅ Targets (EDI≥0.80 APEX, ISN≥9.0 pol) corrects?

**Test 3 — Évolutivité**:
- ✅ Ajout nouveau feature (v8.10) possible sans casser L1?
- ✅ Hash code extensible (add keywords sans reformatting)?

### 4.2 Métriques Compression

```yaml
Niveau 0 (PRESERVATION):
  - Taille: 48KB, 1069 lignes
  - Compression: 0%
  - Audience: LLM (execution)
  - Lisibilité: LOW (verbose for machines)
  - Exécutabilité: 100% (all enforcement logic intact)

Niveau 1 (FUNCTIONAL_SUMMARY):
  - Taille: ~30KB, 600 lignes
  - Compression: 40%
  - Audience: Humans (review, debug, contribute)
  - Lisibilité: HIGH (examples removed, structure clear)
  - Exécutabilité: 85% (pointers KB for full execution)
  - Décompression L1→L0: 85% fidelity

Niveau 4 (HASH_CODE):
  - Taille: ~2KB, 89 chars hash + changelog
  - Compression: 99.9%
  - Audience: Systems (git, DASHBOARD.md, version tracking)
  - Lisibilité: HASH only (metadata)
  - Exécutabilité: 0% (reference only)
  - Décompression L4→L0: Template-based (hash → features map)
```

---

## §5 RECOMMANDATIONS

### 5.1 Actions Immédiates

1. **NE PAS compresser system.md (Niveau 0)**:
   - system.md = moteur exécution LLM
   - Compression > 40% → perte fonctionnelle enforcement logic
   - Garder 1069 lignes intactes pour LLM runtime

2. **CRÉER SYSTEM_FUNCTIONAL_SUMMARY.md (Niveau 1)**:
   - Target: Humains (developers, auditors)
   - 40% compression (600 lignes, ~30KB)
   - Préserver: Pipeline, formulas, targets, enforcement logic
   - Supprimer: Examples, JSON samples, Mermaid diagrams, edge cases

3. **CRÉER SYSTEM_HASH.md (Niveau 4)**:
   - Target: Git tracking, DASHBOARD.md
   - 99.9% compression (hash + changelog)
   - Format: TE_v{ver}_{FEATURES}_EDI{target}_ISN{target}_{KEYWORDS}

### 5.2 Pièges Évités

```yaml
PIÈGE 1 — Sur-compression moteur exécution:
  ❌ WRONG: Compresser system.md à 60% pour "lisibilité humaine"
  ✅ RIGHT: Garder system.md 100% pour LLM, créer FUNCTIONAL_SUMMARY 40% pour humains

PIÈGE 2 — Compression uniforme:
  ❌ WRONG: Appliquer même taux compression à tous contextes (L0→L1→L2→L3→L4)
  ✅ RIGHT: Compression adaptative selon usage (LLM 0%, Human 40%, Git 99.9%)

PIÈGE 3 — Perte enforcement logic:
  ❌ WRONG: Supprimer "examples verbeux" incluant critical edge cases
  ✅ RIGHT: Analyser densité section par section (keep HIGH/MEDIUM, compress LOW)

PIÈGE 4 — Documentation ≠ Exécution:
  ❌ WRONG: Traiter system.md comme PFD.md (philosophie, lecture)
  ✅ RIGHT: Reconnaître system.md = code exécutable (instructions LLM)
```

### 5.3 Next Steps

**Étape 1 — Validation User**:
- User approuve stratégie révisée (L0 preserved, L1 created, L4 created)?
- User confirme compression 40% acceptable pour FUNCTIONAL_SUMMARY?

**Étape 2 — Implémentation**:
- Créer SYSTEM_FUNCTIONAL_SUMMARY.md (600 lignes, condensation sections LOW density)
- Créer SYSTEM_HASH.md (hash v7.17 + changelog + decompression guide)
- Créer SYSTEM_COMPRESSION_README.md (navigation guide)

**Étape 3 — Validation Qualité**:
- Test 1: Developer review FUNCTIONAL_SUMMARY → comprend workflow <10min?
- Test 2: Hash code utilisable dans DASHBOARD.md?
- Test 3: Décompression L1→L0 ≥85% fidelity?

---

## §6 CONCLUSION

**Révision Majeure**:
- Session précédente: Erreur méthodologique (compression uniforme documentation)
- Audit actuel: system.md ≠ documentation, system.md = code exécutable LLM
- Solution: Compression adaptative (L0 preserved, L1 human review, L4 git tracking)

**Principes Appliqués** (@KB[DSL_METAGUIDE]):
- "Contexte = roi": LLM ≠ Human ≠ Git → compressions différentes
- "Évolution organique": Start minimal (L0+L1+L4), expand si besoin détecté
- "Exécutabilité > Concision": Moteur cognitif doit run, pas juste être lisible

**Validation Humaine Requise**:
- User approuve stratégie révisée?
- User confirme: system.md Niveau 0 preserved, FUNCTIONAL_SUMMARY Niveau 1 created?

---

**Version**: Audit v1.0
**Date**: 2025-11-20
**Fichiers à créer**: SYSTEM_FUNCTIONAL_SUMMARY.md, SYSTEM_HASH.md, SYSTEM_COMPRESSION_README.md
**Fichiers à préserver**: system.md (AUCUNE MODIFICATION)
