# TRUTH ENGINE v2.0 — Architecture & Dependency Graph

**Purpose:** Single source of truth for how all files relate, what loads what, and where the LLM can get lost.
**Last updated:** 2026-05-15

---

## §1 FILE INVENTORY (32 files)

### Layer 0: KERNEL (1 file)

| File | Lines | Role | Loaded |
|------|-------|------|--------|
| KERNEL.md | 235 | **Orchestrator.** Boot + TOOLS + pipeline + rules + gates | Always (user loads it) |

### Layer 1: ONTOLOGY (3 files, always loaded at §0 steps 1-3)

| File | Lines | Role | Loaded at |
|------|-------|------|-----------|
| definitions/SYMBOLS.md | 123 | 15 narrative + 17 epistemic + 8 factual symbols, cluster thresholds, symbol→action | §0 step 1 |
| definitions/PATTERNS.md | 200 | 9 @PAT[] with scoring formulas, 4 composite patterns, rhetorical families | §0 step 2 |
| definitions/THREATS.md | 129 | 10 @THR[] with detection signatures, scoring formulas | §0 step 3 |

### Layer 2: PIPELINE (1 file, loaded at step 8b)

| File | Lines | Role | Loaded at |
|------|-------|------|-----------|
| protocol/INVESTIGATION.md | 240 | Pipeline details: scoping, cognitive analysis, dialectical prism, construction, causality, verification, output format, wolves | §1 step 8b |

### Layer 3: CONDITIONAL (2 files, loaded on trigger)

| File | Lines | Role | Trigger |
|------|-------|------|---------|
| protocol/PERSO_FRESQUE.md | 54 | Biography investigation protocol (APEX), DSL compressed | Subject is a person |
| clusters/{NAME}.md (15 files) | ~1239 | Per-symbol scoring + triggers + queries | Score ≥5 for that symbol |

### Layer 4: SEARCH (3 files, loaded on demand)

| File | Lines | Role | When |
|------|-------|------|------|
| search/EPISTEMIC.md | 141 | Source stratification (◈◉○), EDI formula + dimension sub-formulas, convergence C(n), H7 media map | Step 9 (search) or step 16 (EDI) |
| search/TEMPLATES.md | 111 | Domain-adaptive query templates (10 domains), H7 adversary templates, dissident perspectives | Step 9 (search) |
| search/OPTIMIZATION.md | 124 | Query splitting (3-layer), ddq/websearch fallback, reformulation | Step 9 (when queries fail) |

### Layer 5: FORENSIC (2 files, loaded on trigger)

| File | Lines | Role | Trigger |
|------|-------|------|---------|
| forensic/REASONING.md | 55 | Iceberg reconstruction (shown/hidden/factor), 4 @Q[] reasoning questions, output transparency | Ξ ≥5 |
| forensic/REQUEST_LOG.md | 108 | Request log format (table structure + URL), quality gates, protocol header | Always (output) |

### Layer 6: TOOLS (2 files, loaded on demand)

| File | Lines | Role | When |
|------|-------|------|------|
| tools/DSL.md | 143 | 148 concepts, KB macros, core formulas, @HERM/@PRISM/@PF/@Q macros | Reference (step 8b or when needed) |
| tools/MACROS.md | 117 | Compact notation (CX_CHECK, QRY_MIN, EDI_TARGET, I_CONVERGE, CoverageScore, EDI*) | Reference (when macros needed) |

### Layer 7: OUTPUT (1 file, loaded on demand)

| File | Lines | Role | When |
|------|-------|------|------|
| output/TEMPLATE.md | 114 | Investigation format (M:7 sect, A:15 sect), article format (6 sect), TL;DR, validation gates, data storage | Step 14 (output) |

---

## §2 DEPENDENCY GRAPH

```
                                     ┌─────────────────┐
                                     │    USER INPUT    │
                                     │  (text, URL,     │
                                     │   instruction)   │
                                     └────────┬────────┘
                                              │
                                     ┌────────▼────────┐
                                     │   KERNEL.md     │
                                     │   (235L)        │
                                     │   ORCHESTRATOR  │
                                     └────────┬────────┘
                                              │
                           §0 step 1 ─────────┼───────── §0 step 2 ────────── §0 step 3
                           ┌──────────────────┼──────────────────┐
                           │                  │                  │
                    ┌──────▼──────┐   ┌──────▼──────┐   ┌──────▼──────┐
                    │ SYMBOLS.md  │   │ PATTERNS.md │   │ THREATS.md  │
                    │ 123L        │   │ 200L        │   │ 129L        │
                    │ ONTOLOGY    │   │ FORMULAS    │   │ THREATS     │
                    └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
                           │                  │                  │
                           │           §0 step 5 (score ≥5)     │
                           │                  │                  │
                           │    ┌─────────────┼─────────────┐    │
                           │    │             │             │    │
                           │ ┌──▼───┐   ┌────▼───┐   ┌────▼──┐ │
                           │ │ICEBERG│   │ MONEY  │   │ TEMPORAL│
                           │ │86L   │   │ 100L   │   │ 110L  │ │
                           │ └──────┘   └────────┘   └───────┘ │
                           │   ...15 cluster files total...     │
                           │                                     │
                           │           §1 step 8b               │
                           │              │                      │
                           │       ┌──────▼──────┐              │
                           │       │INVESTIGATION│              │
                           │       │   240L      │              │
                           │       │  PIPELINE   │              │
                           │       └──────┬──────┘              │
                           │              │                      │
                           │     §1 step 8b references:         │
                           │     SYMBOLS.md, PATTERNS.md,       │
                           │     6 clusters, PERSO_FRESQUE,     │
                           │     REASONING.md, TEMPLATE.md      │
                           │                                     │
                           │           §1 step 9                │
                           │         ┌────┼────┐                │
                           │   ┌─────▼──┐│┌────▼─────┐         │
                           │   │EPISTEMIC│││TEMPLATES │         │
                           │   │  141L   │││  111L    │         │
                           │   └────┬───┘│└────┬─────┘         │
                           │        │    │     │                │
                           │        │    │  ┌──▼──────────┐    │
                           │        │    │  │OPTIMIZATION │    │
                           │        │    │  │   124L      │    │
                           │        │    │  └─────────────┘    │
                           │                                     │
                           │           Ξ ≥5                     │
                           │              │                      │
                           │       ┌──────▼──────┐              │
                           │       │ REASONING   │              │
                           │       │   55L       │              │
                           │       └─────────────┘              │
                           │                                     │
                           │           step 14                  │
                           │         ┌────┼────┐                │
                           │   ┌─────▼──┐│┌────▼─────┐         │
                           │   │TEMPLATE │││REQUEST_LOG│        │
                           │   │  114L   │││  108L    │        │
                           │   └────────┘│└──────────┘        │
                           │                                     │
                           │      REFERENCE (any step)          │
                           │     ┌──────┬──────┐                │
                           │ ┌───▼──┐ ┌─▼────┐ │                │
                           │ │ DSL  │ │MACROS│ │                │
                           │ │ 143L │ │ 117L │ │                │
                           │ └──────┘ └──────┘ │                │
                           │                                     │
                           └─────────────────────────────────────┘
```

---

## §3 PIPELINE → FILE LOADING MAP

| Step | Action | Files Loaded | Produces |
|------|--------|-------------|----------|
| — | User loads KERNEL | KERNEL.md | — |
| 0 | TEXT_ANALYSIS | SYMBOLS.md + PATTERNS.md + THREATS.md + clusters/{≥5} | MANIPULATION_REPORT |
| 1 | TEMPORAL | — | date |
| 2 | MEMORY | mnemolite_search_memory | "MNEMOLITE: N" + "RELATED: ..." |
| 3 | COMPLEXITY | — | SIMPLE/MEDIUM/COMPLEX/APEX |
| 4 | PERSO_FRESQUE? | PERSO_FRESQUE.md (if person) | — |
| 5 | ACCUSATION? | — | SYMETRIC_CHECK |
| 6 | CRÉDO | — | 12-20 queries |
| 7 | SCOPING | — | domains, actors, exclusions |
| 8 | ANALYSIS | (re-scan, same files as step 0) | MANIPULATION_REPORT (refined) |
| 8b | COGNITIVE | INVESTIGATION.md §1bis + clusters (≥5) + REASONING.md (if Ξ≥5) | COGNITIVE_MAP |
| 8t | DIALECTICAL | INVESTIGATION.md §1ter | DIALECTICAL_MAP |
| 9 | SEARCH | EPISTEMIC.md + TEMPLATES.md + OPTIMIZATION.md (if queries fail) | Search results |
| 10 | CONSTRUCTION | INVESTIGATION.md §3 | FACT_REGISTRY + KNOWLEDGE_STATE |
| 11 | CAUSALITY | INVESTIGATION.md §4 | TIMELINE + CHAINS + CROSS-DOMAIN |
| 12 | IMPACT | INVESTIGATION.md §1ter (DIALECTICAL MAP) | Qui gagne/perd/meurt/recule |
| 13 | VERIFICATION | INVESTIGATION.md §5 | VERIFICATION_REPORT |
| 14 | OUTPUT | TEMPLATE.md + INVESTIGATION.md §6 + REQUEST_LOG.md | Investigation (.md) |
| 15 | ARTICLE | TEMPLATE.md §ARTICLE | Article (.md) |
| 16 | EDI | EPISTEMIC.md §4 (dimension sub-formulas) + KERNEL §1 step 16 (compact) | EDI score + BIAS |
| 17 | WOLVES | INVESTIGATION.md WOLVES section | Named wolves with roles |
| 18 | GATE_CHECK | KERNEL §2 | PASS/FAIL |
| 19 | SAVE | mnemolite_write_memory + write() | .md file + MnemoLite entry |

---

## §4 DATA FLOW

```
TEXT (user input)
  │
  ▼
MANIPULATION_REPORT (step 0)
  ├── SYMBOLS {15 × [0-10]}
  ├── PATTERNS {matching @PAT[]}
  ├── THREATS {matching @THR[]}
  ├── RHETORICAL {DEM BF NUM AUTH FAC × [0-10]}
  ├── CLUSTERS {to load — must match SYMBOLS.md §4}
  ├── IMPLICIT {implied / not-said / inverted}
  ├── SPEAKER {tone target goal}
  ├── PRIORITIES {verify first}
  └── QUERY_GUIDANCE {how techniques guide searches}
  │
  ▼
COGNITIVE_MAP (step 8b)
  ├── CLUSTER_SCORES {each loaded cluster scored with formula}
  ├── HERMENEUTIC {L1-L6 revelations}
  ├── FORENSIC {shown/hidden/factor (if Ξ≥5)}
  └── EMPIRE_OF_LIES {1-2 sentence synthesis}
  │
  ▼
DIALECTICAL_MAP (step 8t)
  ├── SCENARIO_A (official) {cui bono + evidence}
  ├── SCENARIO_B (critical) {cui bono + evidence}
  ├── TENSIONS {convergence/divergence/gaps/silences}
  └── WOLVES_IN_BOTH {actors profiting in all scenarios}
  │
  ▼
FACT_REGISTRY (step 10)
  ├── ✦ CONFIRMED: [N] (≥2 independent, ⊕)
  ├── ✧ PROBABLE: [N] (1 strong ◈)
  ├── ⁕ CLAIMED: [N] (○ only)
  ├── ⁂ SPECULATED: [N] (hypothesis)
  ├── ⊗ CONTRADICTED: [N]
  └── ⊙ PARTIAL: [N]
  │
  ▼
CAUSALITY_CHAINS (step 11)
  ├── TIMELINE {≥10 events}
  ├── CASCADE_CHAINS {≥3 chains, ≥3 links each}
  ├── CROSS_DOMAIN_FLOWS {≥1}
  └── SUSPICIOUS_TIMING {⚑ flagged}
  │
  ▼
IMPACT_VERDICT (step 12)
  ├── Qui gagne. {quantified}
  ├── Qui perd. {quantified}
  ├── Qui meurt. {quantified}
  └── Qui recule. {quantified}
  │
  ▼
VERIFICATION_REPORT (step 13)
  ├── VERIFIED: [N] facts upgraded
  ├── CONTRADICTIONS: [N] official vs independent
  ├── COVER-UPS: [N]
  └── PER-DOMAIN: breakdown
  │
  ▼
INVESTIGATION OUTPUT (step 14)
  ├── MEDIUM: 7 sections (1,7,8,9,10,11,13,14)
  ├── APEX: 15 sections (all)
  └── REQUEST_LOG {#|TYPE|QUERY/TOOL_CALL|RESULT|SOURCE|URL}
  │
  ▼
EDI (step 16)
  ├── EDI = geo×0.25+lang×0.20+strat×0.20+owner×0.15+persp×0.15+temp×0.05
  ├── BIAS: govt>60%:-.20 corp>60%:-.20 power>75%:-.25 no_adv:-.15 echo:-.20 ○>70%:-.15
  ├── EDI_final = max(0, raw + Σpenalties)
  └── OUTPUT: "EDI:{final} (raw:{r} penalties:{sum}[flags])"
  │
  ▼
WRITE (step 19)
  ├── mnemolite_write_memory (title, content, memory_type, tags, embedding_source)
  └── write(content, filePath=investigations/YYYY-MM-DD_HH-MM_{sujet}_INVESTIGATION.md)
```

---

## §5 POTENTIAL ISSUES (Bizarreries)

### ⚠️ B1: KERNEL §0 step 5 duplicates SYMBOLS.md §4

KERNEL has cluster mapping inline + HIGH rules. SYMBOLS.md §4 has the same. The LLM loads SYMBOLS.md at step 1 then reads KERNEL step 5 — sees the mapping twice.

**Impact:** None (identical). But wastes context window.
**Fix option:** KERNEL could say "See SYMBOLS.md §4 for mapping" instead of inline. Saves 5 lines.

### ⚠️ B2: KERNEL §1 step 16 EDI duplicates EPISTEMIC §4

KERNEL has EDI formula + BIAS + TARGET inline. EPISTEMIC §4 has the full version + dimension sub-formulas. When both are loaded, formula appears twice.

**Impact:** Minor. KERNEL's version is compact, EPISTEMIC's is complete.
**Fix option:** KERNEL could reference EPISTEMIC §4. Saves 3 lines.

### ⚠️ B3: INVESTIGATION.md §3 references SYMBOLS.md for fact quality, but SYMBOLS.md §2 has the symbols

INVESTIGATION.md §3 says "CLASSIFY: ✦✧⁅❧". But the actual definitions of ✦✧⁅❧ are in SYMBOLS.md §2 (epistemic symbols). The LLM must have loaded SYMBOLS.md already (step 1) — OK.

**Impact:** None if step 1 executed. Would fail if SYMBOLS.md not loaded.
**Fix option:** Add explicit "See SYMBOLS.md §2" in INVESTIGATION.md §3.

### ⚠️ B5: INVESTIGATION.md §1 references clusters/MONEY.md, FRAMING.md, etc. directly

But these clusters are only loaded if scores ≥5. INVESTIGATION.md should say "if loaded" not assume they're available.

**Impact:** None in practice (LLM has them in context if step 0 loaded them).
**Fix option:** Add "(if loaded)" qualifier.

---

## §6 RECOMMENDED FIXES

| ID | Fix | Effort | Impact |
|----|-----|--------|--------|
| B3 | INVESTIGATION.md §3: add "See SYMBOLS.md §2" | 1 min | LOW |
| B5 | INVESTIGATION.md: add "(if loaded)" qualifiers | 2 min | LOW |
| B1 | KERNEL: inline mapping → reference SYMBOLS.md §4 | 2 min | LOW |
| B2 | KERNEL: EDI compact → reference EPISTEMIC §4 | 2 min | LOW |

**Resolved:** B4 (GASLIGHTING note added), B6 (sections<15 gate fixed), B7 (IMPACT/DIALECTICAL aligned).

---

*Architecture doc v2.0 — Single source of truth for system design._
