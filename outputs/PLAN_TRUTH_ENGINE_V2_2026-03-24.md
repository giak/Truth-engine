# TRUTH ENGINE v2.0 — FROM SCRATCH BUILD PLAN
## Complete implementation blueprint — greenfield architecture
## Date: 24 March 2026

---

## 1. PROBLEM STATEMENT

The current Truth Engine has evolved organically. Each new feature was added as a "patch" without rethinking the global architecture. Result:

- **45 files** with heavy overlap
- **~9400 lines** with ~30% duplication
- **Same symbols defined 4 times** (KERNEL, CORE, DSL, SYMBOLS)
- **Changing 1 concept = touching 3-4 files**
- **Names changed** (system.md → KERNEL.md, VALIDATION.md deleted) but references remain stale
- **Maintenance burden** makes every modification risky

3 optimization passes cleaned -79 lines (-9%), but the structural problem remains. The architecture was never designed as a coherent system.

**Verdict:** Refactoring has reached its limit. A clean rebuild is more efficient than continued patching.

---

## 2. DESIGN PRINCIPLES

### Principle 1: KERNEL = ORCHESTRATOR ONLY
No definitions, no formulas, no tables in KERNEL. Just:
- Protocol steps (reference protocol/)
- Rules (when to load what)
- Gates (when to block)

### Principle 2: ONE CONCEPT = ONE PLACE
If 15 symbols are defined in definitions/SYMBOLS.md, then NO other file defines them. KERNEL says "see definitions/SYMBOLS.md", full stop.

### Principle 3: LINEAR PIPELINE
Protocol follows a clear logical flow:
```
INPUT → ANALYZE → SEARCH → BUILD → SYNTHESIZE → VERIFY → OUTPUT → ARTICLE
```
No mixed steps (old §1 had step 0=text_analysis then step 7=text_analysis again).

### Principle 4: CLUSTERS = SOLE EXTENSION MECHANISM
No separate "protocols" beyond clusters. One cluster = one pattern + its protocols + its queries + its triggers + its output format. Everything in the same file.

### Principle 5: REFERENCES, NOT COPIES
KERNEL never copies KB content. It says "see kb/xxx.md §y", period.

### Principle 6: ENGLISH FOR CODE, FRENCH FOR OUTPUT
All definitions, protocols, clusters, tools in English. Investigation output and articles in French.

---

## 3. TARGET ARCHITECTURE

```
truth-engine-v2/
│
├── KERNEL.md                          [~300 lines] Orchestrator only
│
├── definitions/                       [~850 lines] Single source of truth
│   ├── SYMBOLS.md                     [~200 lines] 15 narrative + epistemic + factual
│   ├── PATTERNS.md                    [~500 lines] All @PAT[] with formulas
│   └── THREATS.md                     [~150 lines] All @THR[] with scoring
│
├── protocol/
│   └── INVESTIGATION.md               [~400 lines] Complete pipeline, 8 phases
│
├── clusters/                          [~1200 lines] Pattern-specific knowledge
│   ├── _TEMPLATE.md                   [~50 lines]  Standard format
│   ├── ICEBERG.md                     [~100 lines]
│   ├── MONEY.md                       [~100 lines]
│   ├── NETWORK.md                     [~100 lines]
│   ├── WAR.md                         [~100 lines]
│   ├── TEMPORAL.md                    [~100 lines]
│   ├── BIO.md                         [~80 lines]
│   ├── FRAMING.md                     [~80 lines]
│   ├── INVERSION.md                   [~80 lines]
│   ├── OVERLOAD.md                    [~80 lines]
│   ├── SPECTACLE.md                   [~60 lines]
│   ├── GASLIGHTING.md                 [~60 lines]
│   ├── CONFIRMATION.md                [~60 lines]
│   ├── RESISTANCE.md                  [~60 lines]
│   ├── FRAGMENTATION.md               [~60 lines]
│   └── POWER.md                       [~60 lines]
│
├── search/                            [~600 lines] Search infrastructure
│   ├── EPISTEMIC.md                   [~300 lines] ◈◉○ + EDI + BIAS + convergence
│   ├── TEMPLATES.md                   [~200 lines] Query templates by domain
│   └── OPTIMIZATION.md                [~100 lines] Split + fallback
│
├── forensic/                          [~180 lines] Forensic tools
│   ├── REASONING.md                   [~100 lines] Iceberg reconstruction
│   └── REQUEST_LOG.md                 [~80 lines]  Log format
│
├── tools/                             [~300 lines] Utilities
│   ├── MACROS.md                      [~100 lines] Compact notation
│   └── DSL.md                         [~200 lines] Full DSL reference
│
└── output/
    └── TEMPLATE.md                    [~150 lines] Investigation + article format
```

**Total: ~28 files, ~3600 lines** (vs 45 files, ~9400 lines = **-62%**)

---

## 4. COMPARISON: CURRENT vs NEW

| Aspect | Current | New |
|--------|---------|-----|
| Files | 45 | 28 |
| Lines | ~9400 | ~3600 |
| Symbol definitions | 4 copies | 1 file |
| Pattern definitions | 3 copies | 1 file |
| Protocols | 4 files (KERNEL §1, INVESTIGATION.md, INVESTIGATION_TREE.md, CLUSTER_INVESTIGATION_PROTOCOLS.md) | 1 file |
| Clusters | 19 files with embedded protocols | 15 files + 1 template |
| Output | KERNEL §2.15 + OUTPUT_TEMPLATE.md | protocol/ §7-§8 |
| Gates | KERNEL §3 + (deleted) VALIDATION.md | KERNEL §3 alone |
| References | KERNEL → 14 files | KERNEL → 6 directories |
| KERNEL size | 803 lines | ~300 lines |
| Duplication | ~30% | 0% |

---

## 5. WHAT DISAPPEARS

| Current File | Lines | Replaced By |
|-------------|-------|-------------|
| COGNITIVE_DSL.md | ~1000 | tools/DSL.md (~200) |
| COGNITIVE_DSL_CORE.md | ~150 | definitions/SYMBOLS.md |
| CLUSTER_INVESTIGATION_PROTOCOLS.md | ~197 | protocol/INVESTIGATION.md |
| INVESTIGATION.md | ~79 | protocol/INVESTIGATION.md |
| INVESTIGATION_TREE.md | ~953 | protocol/INVESTIGATION.md §parallel |
| OUTPUT_TEMPLATE.md | ~303 | output/TEMPLATE.md + protocol/ §7-§8 |
| VALIDATION.md | 0 (already deleted) | KERNEL.md §3 |
| CLUSTER_PROCESSUS_FORENSIQUE.md | 0 (already deleted) | forensic/REQUEST_LOG.md |
| 19 CLUSTER_*.md files | ~2800 | 15 clean cluster files (~1200) |

---

## 6. WHAT CHANGES FUNDAMENTALLY

### 6.1 KERNEL is pure orchestration
Current KERNEL contains definitions, formulas, tables, protocol steps. New KERNEL contains ONLY:
- Boot sequence (reflexes + self-check)
- Index to definitions/ (no content copied)
- Protocol reference (no steps duplicated)
- Rules (thresholds, targets, minimums — values only, formulas in KB)
- Gates (critical + severity)
- Checklist (references only)
- Mandatory/Forbidden lists

### 6.2 Protocol is ONE linear file
Current: KERNEL §1 (20 mixed steps) + INVESTIGATION.md (L0-L6) + INVESTIGATION_TREE.md (parallel) + CLUSTER_INVESTIGATION_PROTOCOLS.md (general)
New: protocol/INVESTIGATION.md with 8 clean phases:
```
§0 SCOPING → §1 ANALYSIS → §2 SEARCH → §3 CONSTRUCTION →
§4 CAUSALITY → §5 IMPACT → §6 VERIFICATION → §7 OUTPUT → §8 ARTICLE
```

### 6.3 Clusters are autonomous
Current: Clusters depend on KERNEL for trigger logic, on CLUSTER_INVESTIGATION_PROTOCOLS.md for protocols.
New: Each cluster is self-contained. Pattern + scoring + queries + triggers + output format. No external dependencies except definitions/.

### 6.4 Search is centralized
Current: EDI in KERNEL + SEARCH_EPISTEMIC.md. Query templates in QUERY_TEMPLATES.md. Optimization in QUERY_OPTIMIZATION.md. All separate with overlapping concepts.
New: search/ directory with 3 files, clear roles.

### 6.5 Output includes article production
Current: Investigation output only. Article production is ad-hoc.
New: protocol/INVESTIGATION.md §8 defines article transformation. output/TEMPLATE.md defines both investigation and article formats.

---

## 7. PHASE-BY-PHASE BUILD PLAN

### PHASE 0: FOUNDATIONS (definitions/)

**Priority:** CRITICAL — everything else depends on this.

#### 7.1 definitions/SYMBOLS.md (~200 lines)

**Source files to merge:**
- KERNEL.md §0bis (symbol scan procedure)
- KERNEL.md §2.10 (symbol reference)
- kb/dsl/COGNITIVE_DSL_CORE.md §1 (15 symbols + epistemic + factual)
- kb/dsl/COGNITIVE_DSL.md §1-§3 (same symbols, more detail)
- kb/dsl/SYMBOLS.md (current, 211 lines)

**Content:**
```markdown
# SYMBOLS — Single Source of Truth

## §1 NARRATIVE SYMBOLS (15)
| Symbol | Name | Concept | Techniques | Score Guide |
|--------|------|---------|------------|-------------|
| Ξ | Xi | Omission | cherry_picking, flooding_zone... | 0-10 |
| € | Euro | Money | dark_money, hidden_flows... | 0-10 |
| ... (all 15) | | | | |

## §2 EPISTEMIC SYMBOLS
| Symbol | Name | Concept | Confidence |
|--------|------|---------|------------|
| ◈ | Primary | Raw evidence | 0.90-0.95 |
| ... (all 17) | | | |

## §3 FACTUAL SYMBOLS
| Symbol | Name | Concept |
|--------|------|---------|
| V | Verifiability | Fact check |
| ... (all 8) | | |

## §4 CLUSTER THRESHOLDS
| Primitive | Default | Mandatory (lower) | Cluster File |
|-----------|---------|-------------------|--------------|
| Ξ | ≥5 | ≥3 | clusters/ICEBERG.md |
| ... (all 15) | | | |

## §5 CLAMPS
Ψ≤4.5 | Ω≤4.0 | Σ≤3.5 | Λ≤4.8 | ⫸≤4.0 | ⚔≤5.0 | 🌐≤5.0 | ⏰≤5.0

## §6 RESONANCE
Ψ≈Ω | Λ≈Σ | €≈♦ | Ξ≈⏰ | ⚔≈🌐

## §7 SYMBOL → ACTION MAP
Ξ [3-4]: NOTE → +1 query | [5-6]: BRANCH → FORENSIC_REASONING | [7-8]: DEEP_DIVE | [9-10]: EXPOSE
... (all 15 symbols × 4 ranges)
```

**What to keep:** All definitions, scoring guides, clamps, resonance, action map.
**What to drop:** Nothing. This is clean.

---

#### 7.2 definitions/PATTERNS.md (~500 lines)

**Source files to merge:**
- kb/dsl/PATTERNS.md (current, 2300+ lines)
- KERNEL.md §0bis B (10 patterns table)
- kb/dsl/COGNITIVE_DSL.md §3 (@PAT[] macros)

**Content:**
```markdown
# PATTERNS — All @PAT[] Definitions

## §1 CORE PATTERNS
For each pattern (ICEBERG, ASTRO, GAS, MONEY, BIO, WAR, NET, TEMP, CYN, FASC):
  - Definition (1 line)
  - Scan criteria
  - Scoring formula (from current PATTERNS.md, keep ALL formulas)
  - Triggers
  - Cluster file reference

## §2 EXTENDED PATTERNS
POLITICAL, GEOPOLITICAL, DEEPFAKE, SURV_CAP, COG_INFRA
Same format as §1

## §3 RHETORICAL FAMILIES
DEM, BF, NUM, AUTH, FAC
Table: Family | Aliases | Markers
```

**What to keep:** ALL pattern definitions with formulas (ICEBERG Factor, MONEY Factor, BIO Factor, NET Power, WAR Factor, TEMP Factor).
**What to drop:** Redundant examples, verbose explanations, investigation protocols (now in protocol/).

---

#### 7.3 definitions/THREATS.md (~150 lines)

**Source files to merge:**
- kb/dsl/THREATS.md (current, 248 lines)
- KERNEL.md §0bis C (10 threats table)

**Content:**
```markdown
# THREATS — All @THR[] Definitions

## §1 THREAT CATEGORIES
For each threat (SHOCK, BIDERMAN, GASLIGHT_SOC, INFODEMIC, DARK_MONEY,
REGULATORY_CAPTURE, MYTHOLOGIZATION, NUDGING, CIALDINI_7, ASTROTURFING):
  - Definition (1 line)
  - Detection criteria
  - Scoring formula
  - Response protocol

## §2 CIALDINI INFLUENCE WEAPONS
7 principles with detection criteria
```

**What to keep:** All threat definitions with scoring.
**What to drop:** Verbose examples.

---

### PHASE 1: CORE PROTOCOL (protocol/)

**Priority:** CRITICAL — this is the backbone.

#### 7.4 protocol/INVESTIGATION.md (~400 lines)

**Source files to merge:**
- KERNEL.md §1 (20 steps)
- KERNEL.md §2.11-§2.15 (5 new steps)
- kb/protocols/INVESTIGATION.md (L0-L6 cascade)
- kb/protocols/INVESTIGATION_TREE.md (parallel branches)
- kb/patterns/CLUSTER_INVESTIGATION_PROTOCOLS.md (general protocols)

**Content:**
```markdown
# INVESTIGATION — Complete Pipeline

## §0 SCOPING
Input: subject
Process:
  1. Define central question
  2. Identify relevant domains
  3. Identify key actors
  4. Generate CRÉDO questions (12-20)
  5. Determine evidence types
  6. Define exclusions
Output: SCOPING_REPORT
Complexity: 6 dimensions → SIMPLE/MEDIUM/COMPLEX/APEX
Budget: queries/wolves/domains/facts/chains/sections

## §1 ANALYSIS
Input: text
Process:
  1. Load definitions/SYMBOLS.md, PATTERNS.md, THREATS.md
  2. Scan all 15 symbols
  3. Check all @PAT[] patterns
  4. Check all @THR[] threats
  5. Check rhetorical families
  6. Generate MANIPULATION_REPORT
MANDATORY: All 15 symbols, all patterns, all threats
Output: MANIPULATION_REPORT

## §2 SEARCH
Input: MANIPULATION_REPORT + CRÉDO questions
Process:
  1. Execute queries with budget (12/18/25/35+)
  2. Stratify sources ◈◉○
  3. Track coverage
  4. Reallocate at 50% if gaps
Output: Search results

## §3 CONSTRUCTION
Input: Search results
Process:
  1. Extract: what happened, who, when, where, how much
  2. Classify: ✦ hard_fact / ✧ soft_fact / ⁕ claim / ⁂ speculation
  3. Source: ◈◉○ tier
  4. Cross-check: ⊕ confirmed / ⊗ contradicted / ⊙ partial
  5. Register: add to FACT_REGISTRY
Output: FACT_REGISTRY + KNOWLEDGE_STATE (KNOWN/SUSPECTED/UNKNOWN)
Feedback: If ✦ < minimum → return to §2

## §4 CAUSALITY
Input: FACT_REGISTRY + SYMBOL_SCORES
Process:
  1. Timeline: order ✦ facts chronologically
  2. Link: "what caused this?" and "what did this cause?"
  3. Chain: build chains of ≥3 links
  4. Cross-domain: trace MILITARY→ENERGY→FOOD→HUMANITARIAN etc.
  5. Quantify: each endpoint = deaths, $, %, populations
Output: TIMELINE + CASCADE_CHAINS + CROSS_DOMAIN_FLOWS + SUSPICIOUS_TIMING
Feedback: If chains < minimum → return to §2

## §5 IMPACT
Input: FACT_REGISTRY + CAUSALITY_CHAINS + WOLF_PROFILES
Process: Build 4 matrices from data
Output:
  Qui gagne. [Actor] — [gain]. [Actor] — [gain].
  Qui perd.  [Actor] — [perte]. [Actor] — [perte].
  Qui meurt. [Chiffre] — [contexte humanitaire].
  Qui recule. [Actor] — [signes de déclin].
Rules:
  - Each entry ≥1 number
  - "Qui meurt" prioritizes human cost
  - "Qui recule" identifies structural decline

## §6 VERIFICATION
Input: FACT_REGISTRY
Process:
  1. Classify facts by domain (MILITARY/FINANCIAL/DIPLOMATIC/HUMANITARIAN/ENERGY/LEGAL/TECHNICAL)
  2. Verify with domain-specific protocol
  3. Flag contradictions (official vs independent)
  4. Upgrade facts (⁕→✧, ✧→✦)
Output: VERIFICATION_REPORT
Feedback: If unverified >30% → return to §2

## §7 INVESTIGATION OUTPUT (in French)
Input: All previous phases
Structure (9 mandatory sections):
  1. EXECUTIVE SUMMARY (≤500 words)
  2. TIMELINE (chronological, ≥10 events)
  3. DOMAINS (thematic sections)
  4. ACTOR NETWORK (≥8 actors with roles)
  5. CASCADE CHAINS (≥3 chains)
  6. EVIDENCE MAP (sources + facts + EDI + symbols)
  7. IMPACT VERDICT (4 matrices)
  8. SCOPE & LIMITATIONS (≥3 exclusions)
  9. KNOWLEDGE STATE (KNOWN/SUSPECTED/UNKNOWN)
Tone: Factual, dense, no filler. Each sentence = 1 fact.

## §8 ARTICLE TRANSFORMATION (in French)
Input: Investigation from §7
Process:
  1. HOOK: Compress EXECUTIVE SUMMARY → 1 dense paragraph (5 facts)
  2. SECTIONS: Transform DOMAIN sections → thematic narrative
     - Each section starts with strongest fact
     - Each section ends with 1-line synthesis (blockquote)
  3. VERDICT: Transform IMPACT_VERDICT → 4-line matrices
  4. CLOSING: 1 sentence capturing entire case
  5. BIBLIOGRAPHY: Numbered, with URLs and dates
  6. DISCLAIMER: From SCOPE & LIMITATIONS
Tone: Dense, factual, no filler. Each sentence = 1 fact.
THIS IS THE ARTICLE. Separate from investigation.

## FEEDBACK LOOPS
§3 → §2: If FACT_REGISTRY ✦ < minimum OR ⊗ == 0
§4 → §2: If CAUSALITY_CHAINS < minimum
§6 → §2: If domains_verified < minimum OR unverified >30%
MAX: 2 loops per investigation

## WOLVES
Categories: GOVERNMENT, OPPOSITION, CORPORATE, CIVIL_SOCIETY, INTERNATIONAL, EXPERTS, MEDIA
Minimums: APEX ≥12, COMPLEX ≥8, MEDIUM ≥5
Auto-detect: € high → CORPORATE; ↕ high → EXPERTS; Ξ high → INSTITUTIONAL; Λ high → MEDIA
Output: WOLF_CATEGORY + ROLE + CENTRALITY [0-1]
```

---

### PHASE 2: CLUSTERS (clusters/)

**Priority:** HIGH — pattern-specific knowledge.

#### 7.5 clusters/_TEMPLATE.md (~50 lines)

```markdown
# CLUSTER_{NAME} — {description}

## Scoring
  Formula or criteria for scoring this pattern

## Triggers
  When to activate (threshold)
  Symbol reference: {symbol} ≥ {threshold}

## Queries
  Specific search queries for this pattern:
  - query:"{pattern-specific query 1}"
  - query:"{pattern-specific query 2}"

## Deep Dive Protocol
  What to do when score ≥7:
  1. Step 1
  2. Step 2
  3. Step 3

## Output Format
  What to include in investigation output:
  - Field 1: description
  - Field 2: description

## Connections
  Links to other clusters: {related clusters}
  Links to symbols: {related symbols}
  Links to patterns: {related @PAT[]}
```

#### 7.6-7.20: 15 cluster files

**Source:** Each existing CLUSTER_*.md, compressed to template format.

Each cluster file contains:
- Scoring formula (from current CLUSTER_*.md)
- Specific queries (from current CLUSTER_*.md)
- Trigger thresholds (from definitions/SYMBOLS.md §4)
- Deep dive protocol (compressed from current CLUSTER_*.md)
- Output format (compressed)
- Connections to other clusters/symbols/patterns

**What to keep:** Scoring formulas, queries, triggers, output format.
**What to drop:** Redundant investigation protocols (now in protocol/INVESTIGATION.md), verbose examples, duplicate trigger definitions.

**Compression estimate:** Current 15 clusters = ~2800 lines. New = ~1200 lines (-57%).

**Cluster list:**
| # | File | Symbol | Source |
|---|------|--------|--------|
| 1 | ICEBERG.md | Ξ | CLUSTER_ICEBERG.md (263L) |
| 2 | MONEY.md | € | CLUSTER_MONEY.md (155L) |
| 3 | NETWORK.md | 🌐 | CLUSTER_NETWORK.md (146L) |
| 4 | WAR.md | ⚔ | CLUSTER_WAR.md (133L) |
| 5 | TEMPORAL.md | ⏰↕ | CLUSTER_TEMPORAL_VERTICAL.md (152L) |
| 6 | BIO.md | ♦ | CLUSTER_BIO.md (118L) |
| 7 | FRAMING.md | Λ | CLUSTER_FRAMING.md (155L) |
| 8 | INVERSION.md | Ω | CLUSTER_INVERSION.md (147L) |
| 9 | OVERLOAD.md | Ψ | CLUSTER_OVERLOAD.md (160L) |
| 10 | SPECTACLE.md | Φ | CLUSTER_SPECTACLE.md (139L) |
| 11 | GASLIGHTING.md | Κ | CLUSTER_GASLIGHTING.md (152L) |
| 12 | CONFIRMATION.md | κ | CLUSTER_CONFIRMATION.md (122L) |
| 13 | RESISTANCE.md | ρ | CLUSTER_RESISTANCE.md (134L) |
| 14 | FRAGMENTATION.md | Σ | CLUSTER_FRAGMENTATION.md (116L) |
| 15 | POWER.md | ♦ | CLUSTER_POWER.md (141L) |

---

### PHASE 3: SEARCH (search/)

**Priority:** HIGH — search infrastructure.

#### 7.21 search/EPISTEMIC.md (~300 lines)

**Source:** kb/dsl/SEARCH_EPISTEMIC.md (current, 1797 lines)

**Content:**
```markdown
# EPISTEMIC — Source Stratification, EDI, Diversity

## §1 SOURCE STRATIFICATION (◈◉○)
Classification algorithm
Confidence ranges
Ownership types

## §2 DIVERSITY ANALYSIS
Geographic (continents/zones)
Linguistic (languages/families)
Ownership (6 types)
Perspective (7 dimensions)
Temporal (5 temporalities)

## §3 CORROBORATION (⊕⊗⊙)
Confirmed/contradicted/partial protocol
Fact quality: ✦✧⁅⁂

## §4 EDI CALCULATION
Full formula: EDI = geo×0.25 + lang×0.20 + strat×0.20 + owner×0.15 + persp×0.15 + temp×0.05
Normalization rules (6 dimensions)
BIAS adjustments (5 penalties):
  - Institutional monoculture (govt>60%, corp>60%, power>75%)
  - Missing adversary (adversary==0 AND dissident==0)
  - Echo chamber (official>0 AND counter==0 AND dissident==0)
  - Tertiary over-reliance (○>70%)
EDI_final = max(0, EDI_raw + sum(penalties))
Target by topic type (DEFAULT/SENSITIVE/PROSPECTIVE/INTERNATIONAL)

## §5 CONVERGENCE
4-iteration protocol
Orchestration detection (⚑)

## §6 ADVERSARY MEDIA MAP (H7)
Framework for counter-narrative sources
```

**What to keep:** ALL formulas, algorithms, protocols.
**What to drop:** Verbose examples, redundant explanations, Python pseudocode.
**Compression:** 1797 → 300 lines (-83%).

---

#### 7.22 search/TEMPLATES.md (~200 lines)

**Source:** kb/dsl/QUERY_TEMPLATES.md (current, 821 lines)

**What to keep:** Template patterns, domain-adaptive rules, H7 framework.
**What to drop:** Verbose examples, test cases.

---

#### 7.23 search/OPTIMIZATION.md (~100 lines)

**Source:** kb/dsl/QUERY_OPTIMIZATION.md (current, 893 lines)

**What to keep:** Split rules (3-layer architecture), fallback logic, reformulation strategy.
**What to drop:** Verbose test cases, implementation checklist.

---

### PHASE 4: FORENSIC (forensic/)

**Priority:** MEDIUM — forensic tools.

#### 7.24 forensic/REASONING.md (~100 lines)

**Source:** kb/dsl/FORENSIC_REASONING.md (current, 125 lines)

**What to keep:** Core principle, 4 reasoning questions, output transparency (shown/hidden/reality).
**What to drop:** Nothing significant. Already clean.

---

#### 7.25 forensic/REQUEST_LOG.md (~80 lines)

**Source:** kb/patterns/CLUSTER_REQUEST_LOG.md (current, 228 lines)

**What to keep:** Log format (table structure), quality gates, protocol description.
**What to drop:** Verbose examples.

---

### PHASE 5: TOOLS (tools/)

**Priority:** LOW — utilities.

#### 7.26 tools/MACROS.md (~100 lines)

**Source:** kb/dsl/MACROS.md (current, 210 lines)

**What to keep:** All macro definitions (status, complexity, conditional, query, EDI, output, iteration).
**What to drop:** Verbose before/after examples.

---

#### 7.27 tools/DSL.md (~200 lines)

**Source:** kb/dsl/COGNITIVE_DSL.md (current, ~1000 lines) + kb/dsl/COGNITIVE_DSL_CORE.md (~150 lines)

**Content:** Slim reference card. All DSL constructs in compact format.
**What to keep:** DSL syntax, macro definitions, function signatures, investigation syntax.
**What to drop:** Verbose explanations, implementation details.
**Compression:** 1150 → 200 lines (-83%).

---

### PHASE 6: OUTPUT (output/)

**Priority:** MEDIUM — output formatting.

#### 7.28 output/TEMPLATE.md (~150 lines)

**Source:** kb/protocols/OUTPUT_TEMPLATE.md (current, 303 lines)

**What to keep:** Section templates, validation gates, soft checks.
**What to drop:** Duplicate compliance checklist (now in KERNEL §4).

---

### PHASE 7: KERNEL.md (~300 lines)

**Priority:** LAST — orchestrator, depends on everything else.

**Source:** KERNEL.md (current, 803 lines)

**Content:**
```markdown
# TRUTH ENGINE — KERNEL v2.0

## §0 BOOT — YOUR COGNITIVE REFLEXES
  12 reflexes (kept inline)
  Self-check (8 lines)

## §0bis TEXT ANALYSIS — MANDATORY
  PROCEDURE:
    1. LOAD SYMBOLS: definitions/SYMBOLS.md §1
    2. LOAD PATTERNS: definitions/PATTERNS.md
    3. LOAD THREATS: definitions/THREATS.md
    4. LOAD CLUSTERS: clusters/*.md (thresholds in definitions/SYMBOLS.md §4)
    5. EXECUTE SCAN
    6. GENERATE MANIPULATION_REPORT
  MANDATORY: 5 checks
  MANIPULATION_REPORT format (15 lines)
  Pass to §1

## §1 PROTOCOL
  Reference: protocol/INVESTIGATION.md
  Steps 0-8 with line references (no content duplicated)
  Feedback loops reference: protocol/INVESTIGATION.md FEEDBACK LOOPS

## §2 RULES
  §2.1 Complexity + budget-driven (reference definitions/SYMBOLS.md + protocol/)
  §2.2 EDI targets (reference search/EPISTEMIC.md §4)
  §2.3 Cluster loading (reference definitions/SYMBOLS.md §4)
  §2.4 MnemoLite (20 lines, kept inline)
  §2.5 Reallocation (10 lines, kept inline)
  §2.6 Wolf categories (reference protocol/INVESTIGATION.md WOLVES)
  §2.7 Accusation trigger (10 lines, kept inline)
  §2.8 CRÉDO dimensions (table, kept inline)
  §2.9 Query distribution (table, kept inline)
  §2.10 Symbols (reference definitions/SYMBOLS.md)

## §3 GATES
  Critical gates (15 lines)
  Severity calculation (10 lines)
  Severity-based gates (15 lines)
  APEX validation (5 lines)
  PERSO_FRESQUE severity (3 lines)

## §4 CHECKLIST
  16 items (reference protocol/ + output/)

## §5 REFERENCES
  Table: all 6 directories with file lists

## §6 MANDATORY
  16 items

## §7 FORBIDDEN
  20 items

## §8 BOOT COMPLETE
```

---

## 8. MIGRATION STRATEGY

```
Step 1:  Create truth-engine-v2/ directory structure
Step 2:  Build definitions/ (SYMBOLS, PATTERNS, THREATS)
Step 3:  Build protocol/INVESTIGATION.md
Step 4:  Build clusters/_TEMPLATE.md + 5 priority clusters (ICEBERG, MONEY, NETWORK, WAR, TEMPORAL)
Step 5:  Build remaining 10 clusters
Step 6:  Build search/ (EPISTEMIC, TEMPLATES, OPTIMIZATION)
Step 7:  Build forensic/ (REASONING, REQUEST_LOG)
Step 8:  Build tools/ (MACROS, DSL)
Step 9:  Build output/TEMPLATE.md
Step 10: Build KERNEL.md
Step 11: Test with real investigation
Step 12: Fix issues found in testing
Step 13: Archive old truth-engine/ to archive/truth-engine-v1/
Step 14: Rename truth-engine-v2/ to truth-engine/
```

---

## 9. EXECUTION TIMELINE

```
Day 1 (Morning):  definitions/SYMBOLS.md (200 lines)
Day 1 (Afternoon): definitions/PATTERNS.md (500 lines)
Day 2 (Morning):  definitions/THREATS.md (150 lines)
Day 2 (Afternoon): protocol/INVESTIGATION.md (400 lines)
Day 3 (Morning):  clusters/_TEMPLATE.md + ICEBERG, MONEY, NETWORK, WAR, TEMPORAL
Day 3 (Afternoon): clusters/BIO, FRAMING, INVERSION, OVERLOAD, SPECTACLE
Day 4 (Morning):  clusters/GASLIGHTING, CONFIRMATION, RESISTANCE, FRAGMENTATION, POWER
Day 4 (Afternoon): search/EPISTEMIC.md (300 lines)
Day 5 (Morning):  search/TEMPLATES.md + search/OPTIMIZATION.md
Day 5 (Afternoon): forensic/REASONING.md + forensic/REQUEST_LOG.md + tools/MACROS.md + tools/DSL.md + output/TEMPLATE.md
Day 6 (Morning):  KERNEL.md (300 lines)
Day 6 (Afternoon): Testing + fixes
Day 7:            Migration + cleanup
```

**Total: ~7 days**

---

## 10. VALIDATION CHECKLIST

After build, verify:

- [ ] No symbol defined in more than 1 file
- [ ] No pattern defined in more than 1 file
- [ ] No threat defined in more than 1 file
- [ ] KERNEL contains no definitions (only references)
- [ ] KERNEL contains no formulas (only values)
- [ ] Protocol flows linearly (§0→§1→§2→§3→§4→§5→§6→§7→§8)
- [ ] Each cluster follows _TEMPLATE.md format
- [ ] All feedback loops documented in protocol/
- [ ] All gates documented in KERNEL §3
- [ ] All mandatory items documented in KERNEL §6
- [ ] All forbidden items documented in KERNEL §7
- [ ] All references in KERNEL §5 are valid (no stale links)
- [ ] No reference to VALIDATION.md anywhere
- [ ] No reference to system.md anywhere
- [ ] No reference to COGNITIVE_DSL_CORE.md (merged into SYMBOLS.md)
- [ ] Test investigation produces expected output
- [ ] Article transformation produces publishable French article

---

## 11. OPEN QUESTIONS

### Q1: MnemoLite integration
Current MnemoLite is an MCP tool. Should KERNEL reference it directly or should there be a search/MEMORY.md file?
**Recommendation:** Keep MnemoLite in KERNEL §2.4 (it's orchestration logic, not definition).

### Q2: PERSO_FRESQUE
Current PROTOCOLE_FRESQUE_POLITIQUE.md is specific to political figures. Should it become a cluster or stay as a separate protocol file?
**Recommendation:** Keep as separate file in protocol/PERSO_FRESQUE.md (~100 lines). It's a specialized sub-protocol, not a pattern cluster.

### Q3: Investigation Tree (parallel branches)
Current INVESTIGATION_TREE.md is 953 lines. Should it stay as a separate file or be integrated into protocol/INVESTIGATION.md?
**Recommendation:** Add a §parallel section in protocol/INVESTIGATION.md (~50 lines) that describes the parallel branching concept. Keep the full INVESTIGATION_TREE.md as a reference in protocol/ for APEX investigations only.

### Q4: Output in French
Protocol and definitions are in English, but investigation output and article are in French. Where should the French templates live?
**Recommendation:** output/TEMPLATE.md has both English section headers and French content templates. The §8 ARTICLE TRANSFORMATION in protocol/INVESTIGATION.md specifies "in French".

### Q5: Archive strategy
Keep old truth-engine/ in archive/ or delete completely?
**Recommendation:** Archive to archive/truth-engine-v1/ with date stamp. Never delete — preserve for reference.

### Q6: Cross-references in existing files
Many files in archive/ and tools/tests/ reference old file names (VALIDATION.md, system.md). Should these be updated?
**Recommendation:** No. Archive files are frozen. Only active files (kb/, KERNEL.md) should be migrated.

---

## 12. RISK ASSESSMENT

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Content lost during migration | LOW | HIGH | Keep v1 in archive/, verify each file |
| New system misses edge cases from v1 | MEDIUM | MEDIUM | Test with real investigation before cutover |
| Cluster files too compressed | MEDIUM | LOW | Can always expand later |
| KERNEL still too complex | LOW | MEDIUM | Hard limit: 300 lines, any more = move to KB |
| Feedback loops cause infinite loops | LOW | HIGH | MAX 2 loops per investigation, enforced in protocol/ |

---

## 13. SUCCESS METRICS

| Metric | Current (v1) | Target (v2) | Improvement |
|--------|-------------|-------------|-------------|
| Total files | 45 | 28 | -38% |
| Total lines | ~9400 | ~3600 | -62% |
| KERNEL lines | 803 | ~300 | -63% |
| Symbol definition copies | 4 | 1 | -75% |
| Pattern definition copies | 3 | 1 | -67% |
| Protocol files | 4 | 1 | -75% |
| Cluster files | 19 | 15 | -21% |
| Stale references | ~50 | 0 | -100% |
| Duplication rate | ~30% | 0% | -100% |
| Time to modify 1 concept | ~15 min (3-4 files) | ~3 min (1 file) | -80% |

---

## 14. POST-MIGRATION

After v2 is built and tested:

1. **Archive v1:** Move old truth-engine/ to archive/truth-engine-v1-2026-03-24/
2. **Rename v2:** Move truth-engine-v2/ to truth-engine/
3. **Update references:** Any external references to old paths
4. **Document:** Update README.md with new architecture
5. **Celebrate:** 62% less code, 0% duplication, 100% functionality preserved

---

_PLAN generated 24 March 2026 — Truth Engine v2.0 from scratch_
_All definitions in English. User output in French._
_Agnostic. Hostile. Precise._
