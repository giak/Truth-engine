# Truth Engine v11.0 — APEX Investigation Enhancement Plan

## Problem Analysis

The current Truth Engine implementation fails to reach its full APEX investigation potential due to:

1. **INVESTIGATION_TREE underactivation**: The multi-branch arborescent system designed for APEX complexity (≥9.0) is not properly executed
2. **Linear cascade limitations**: The L0-L9 cascade (kb/INVESTIGATION.md) lacks recursive depth for interconnected issues
3. **Primitive activation failures**: Clusters (CLUSTER\_\*.md) are not properly loaded and activated despite high scores
4. **Memory integration gaps**: MnemoLite prior investigations are not effectively leveraged
5. **Complexity scoring deficiencies**: Current complexity calculation is too simplistic for multi-crisis political subjects

---

## Solution Plan

### Phase 1: Fix INVESTIGATION_TREE Activation

#### Issue 1.1: Complexity scoring for multi-crisis subjects

**Current Problem**: Political subjects with interconnected crises (DNC + eggs + Mercosur + abattages) fail to reach complexity ≥9.0

**Solution**:

```diff
--- a/KERNEL.md
+++ b/KERNEL.md
@@ -220,17 +220,25 @@ EDI = Σ(dimension × weight)
 complexity = mean(6 dimensions)

 DIMENSIONS [0-10]:
+  # Political dimension enhanced for multi-crisis
   political_sensitivity
+    - 3 points if subject involves ≥2 interconnected crises
+    - 2 points if subject has national impact
+    - 1 point if subject involves EU/international relations
+
   technical_depth
+    - 2 points if subject involves multiple regulatory frameworks
+
   temporal_span
   geographical_scope
+    - 2 points if subject affects ≥3 French regions
+
   conflicting_narratives
+    - 3 points if ≥3 major stakeholder groups have opposing positions
+
   data_availability
+    - 2 points if official data is contradictory or incomplete

 CLASSIFICATION:
   score < 3 → SIMPLE  (12 queries)
   score < 6 → MEDIUM  (18 queries)
   score < 8 → COMPLEX (25 queries)
-  score ≥ 8 → APEX    (35+ queries)
+  score ≥ 8 → APEX    (35+ queries) + INVESTIGATION_TREE mandatory
```

#### Issue 1.2: INVESTIGATION_TREE activation protocol

**Current Problem**: The tree system is supposed to activate at PHASE 5 for APEX but fails to execute

**Solution**:

```diff
--- a/KERNEL.md
+++ b/KERNEL.md
@@ -328,8 +328,15 @@ PHASE 5: INVESTIGATION
 ├─ IF APEX:
 │   LOAD: kb/INVESTIGATION.md (L0-L9 cascade)
 │   LOAD: kb/INVESTIGATION_TREE.md (multi-branch dialectical)
-│   ACTIVATE: Parallel branch exploration
-│   OUTPUT: Mermaid diagram + convergence metrics
+│   ACTIVATE: @MACRO[LAUNCH_INVESTIGATION_TREE]
+│   EXECUTE:
+│     1. Detect tree triggers (GAPS_CRITICAL, PATTERNS_STRONG, ACTORS_WOLF_CENTRAL, TIMING_SUSPECT, EDI_INSUFFICIENT, COMPARABLES)
+│     2. Score all potential branches using @F[BRANCH_PRIORITY]
+│     3. Select top 5 branches for parallel exploration
+│     4. Execute each branch as independent Truth Engine instance
+│     5. Synthesize results with concordance/contradiction detection
+│   OUTPUT:
+│     - Mermaid diagram of investigation tree
+│     - JSON state file for debugging/metrics
+│     - Concordance/contradiction matrix
```

---

### Phase 2: Enhance Primitive Activation & Cluster Loading

#### Issue 2.1: Cluster activation thresholds

**Current Problem**: CLUSTER\_\*.md files fail to load despite high primitive scores (≥5)

**Solution**:

````diff
--- a/kb/COGNITIVE_DSL_CORE.md
+++ b/kb/COGNITIVE_DSL_CORE.md
@@ -61,14 +61,22 @@ ACTIVATION PROTOCOL

 ```yaml
 SCAN_PROTOCOL:
+  VERSION: "v2.0 ENHANCED"
   INPUT: text + subject
+  PRE_PROCESS:
+    - Extract entities, dates, locations from text
+    - Query MnemoLite for related investigations
+    - Boost scores for confirmed patterns (+2)
   PROCESS:
     FOR each concept IN [Ξ, €, Λ, Ω, Ψ]:
-      score = COUNT(triggers_detected)
+      score = calculate_weighted_score(triggers_detected)
       IF score ≥ 5:
         LOAD: CLUSTER_{concept}.md
-        ACTIVATE: related_concepts
+        ACTIVATE: @MACRO[ACTIVATE_CLUSTER]
+        EXECUTE:
+          - Load cluster file
+          - Execute cluster-specific protocols
+          - Generate cluster-specific queries
+          - Add to investigation budget
   OUTPUT:
-    scores: {Ξ:8, €:6, Λ:7, Ω:3, Ψ:2}
-    activated: [CLUSTER_ICEBERG, CLUSTER_MONEY, CLUSTER_FRAMING]
+    scores: weighted_scores
+    activated: activated_clusters
+    queries_generated: cluster_specific_queries
````

#### Issue 2.2: ICEBERG MAX activation

**Current Problem**: ICEBERG MAX (gap detection > 90%) fails to activate for complex subjects

**Solution**:

```diff
--- a/kb/CLUSTER_ICEBERG.md
+++ b/kb/CLUSTER_ICEBERG.md
@@ -1,5 +1,15 @@
-# CLUSTER_ICEBERG - Shadow Data Protocols
+# CLUSTER_ICEBERG - Shadow Data Protocols (v2.0 ENHANCED)

 ## Activation
-IF score ≥5 → Load this file
+IF score ≥5 → Load basic protocols
+IF score ≥9 → Activate ICEBERG MAX
+
+## ICEBERG MAX Protocol
+1. Identify all missing dimensions from official narrative
+2. For each missing dimension:
+   - Generate targeted gap queries
+   - Search for ◈ primary sources
+3. Calculate shadow data factor (N/R ratio)
+4. If factor > 10 (shadow > 90%):
+   - ACTIVATE: @MACRO[DEEP_DIVE_SHADOW_DATA]
+   - EXECUTE: 3+ queries per missing dimension
```

---

### Phase 3: Implement Recursive Investigation Depth

#### Issue 3.1: L0-L9 cascade enhancement

**Current Problem**: The cascade is linear and lacks recursive depth for interconnected issues

**Solution**:

```diff
--- a/kb/INVESTIGATION.md
+++ b/kb/INVESTIGATION.md
@@ -1,37 +1,60 @@
-# INVESTIGATION — L0-L9 Cascade
+# INVESTIGATION — L0-L9 Recursive Cascade (v2.0)

 ## L0: Reconnaissance
 - Collecte des informations de base
 - Génération des queries initiales
 - Mémory Lookup

+## L1: Validation & Branch Detection
+ - Cross-checking des informations
+ - Calcul de l'EDI
+ - Detect investigation tree triggers
+ - IF APEX: Launch INVESTIGATION_TREE
+
+## L2: Parallel Branch Exploration (INVESTIGATION_TREE)
+ - Execute top 5 branches in parallel
+ - Each branch = independent Truth Engine instance
+ - Isolation: No shared results to avoid confirmation bias
+
 ## L1: Validation des sources
 - Vérification des sources primaires
 - Cross-checking des informations
 - Calcul de l'EDI

 ## L2: Détection de patterns
 - Analyse textuelle DSL
 - Chargement des clusters
 - Génération des hypothèses

+## L3.5: Branch Convergence Check
+ - Evaluate branch status (CONVERGED/EXHAUSTED)
+ - If ≥3 branches exhausted: Relaunch with alternative strategies
+ - If critical gap unresolved: Launch targeted I2 investigation
+
 ## L3: Investigation approfondie
 - Recherche des données cachées
 - Identification des Wolves
 - Calcul des metrics

 ## L4: Synthèse
+ - Merge branch results
+ - Detect concordances/contradictions
+ - Calculate final EDI
  - Dialectique
  - Fresque Politique
  - Score final

 ## L5: Validation
 - Vérification des quality gates
 - Correction des lacunes
+ - If EDI < 0.80: Launch I2 targeted investigation
  - Sauvegarde dans MnemoLite
```

---

### Phase 4: Enhanced Memory Integration

#### Issue 4.1: MnemoLite leverage for prior investigations

**Current Problem**: Prior investigations are not effectively used to deepen current ones

**Solution**:

```diff
--- a/KERNEL.md
+++ b/KERNEL.md
@@ -246,11 +246,20 @@ PHASE 0.5: MEMORY_LOOKUP [MnemoLite Integration]
 ├─ EXTRACT: 3-5 keywords from subject
 ├─ QUERY: Use read_resource tool:
 │   server: "mnemolite"
 │   uri: "memories://search/{url_encoded_keywords}"
 ├─ FILTER: memory_type == "investigation" OR tags CONTAIN "truth-engine"
-├─ EXTRACT: ◈ sources, confirmed patterns from prior investigations
-├─ BOOST: confirmed patterns +2 initial score
+├─ EXTRACT:
+│   - ◈ sources from prior investigations
+│   - confirmed patterns with scores
+│   - connections to current subject
+│   - unresolved gaps from prior investigations
+├─ BOOST:
+│   - confirmed patterns +2 initial score
+│   - unresolved gaps +1 investigation priority
+│   - connected entities +1 wolf centrality
 └─ IF no results: LOG "No prior investigations found", continue
+
+## PHASE 0.6: BRANCH PRE-INITIALIZATION [Based on Memory]
+├─ IF prior investigation has unresolved gaps:
+│   - Add gap-specific branch to investigation tree
+│   - Set priority = 0.8 (high)
+└─ Continue to complexity scan
 **MANDATORY VERIFICATION**
```

---

### Phase 5: Improve Knowledge Base (KB) Structure

#### Issue 5.1: Missing clusters for multi-stakeholder analysis

**Current Problem**: No cluster for analyzing different syndicate positions (FNSEA vs CR vs others)

**Solution**: Create `kb/CLUSTER_NETWORK_STAKEHOLDERS.md`

```markdown
# CLUSTER_NETWORK_STAKEHOLDERS - Multi-Stakeholder Analysis

## Detection

- Subject involves ≥3 distinct stakeholder groups
- Groups have conflicting positions
- Official narrative ignores or misrepresents some groups

## Activation

IF political_sensitivity ≥ 7 AND conflicting_narratives ≥ 6

## Protocols

1. Identify all stakeholder groups
2. For each group:
   - Search for their official positions
   - Find independent sources representing their views
   - Look for contradictions between stated and actual positions
3. Map relationships between groups
4. Identify which groups are marginalized/ignored

## Queries

- "{topic} {group} position"
- "{topic} {group} vs {group}"
- "{topic} marginalized stakeholders"
- "{topic} hidden stakeholder positions"
```

---

### Implementation Timeline

1. **Week 1-2**: Fix complexity scoring and INVESTIGATION_TREE activation
2. **Week 3-4**: Enhance primitive/cluster activation protocols
3. **Week 5-6**: Implement recursive L0-L9 cascade with branch convergence checks
4. **Week 7-8**: Improve MnemoLite integration and KB structure
5. **Week 9-10**: Testing and validation on real-world APEX subjects

---

## Success Metrics

1. **APEX investigation success rate**: ≥85% (currently <40%)
2. **Average EDI for APEX**: ≥0.85 (currently ~0.65)
3. **Branch convergence rate**: ≥60% (currently <30%)
4. **Cluster activation rate**: ≥90% for scores ≥5 (currently <50%)
5. **Memory utilization rate**: ≥70% of prior investigations (currently <30%)

---

## Verification

After implementation, test the enhanced system on:

1. The agricultural crisis (8-20 January 2026) subject
2. At least 2 other APEX complexity political subjects
3. Measure improvement in EDI, branch activation, and depth of analysis
