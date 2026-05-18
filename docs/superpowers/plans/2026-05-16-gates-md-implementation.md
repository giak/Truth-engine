# GATES.md Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create forensic/GATES.md and integrate it into KERNEL.md as an auto-validation pipeline.

**Architecture:** 1 new file (GATES.md) loaded at KERNEL step 0 and executed at step 18b. 2 lines added to KERNEL.md + 1 line in §5 FILES. ARCHITECTURE.md updated.

**Tech Stack:** Markdown, Truth Engine v2.0 conventions

---

### Task 1: Create forensic/GATES.md

**Files:**
- Create: `truth-engine-v2/forensic/GATES.md`

- [ ] **Step 1: Write GATES.md with all 5 sections**

Content (write the complete file):

```markdown
# TRUTH ENGINE — GATES v2.0
# Auto-validation pipeline. Loaded at KERNEL §0 step 4, executed at step 18b.

---

## §1 BEHAVIORAL RULES (loaded at step 0, apply to entire pipeline)

R1: 429 FALLBACK → DuckDuckGo immediately
  IF @EXA returns 429 → IMMEDIATELY retry same query with @WEB
  IF @WEB also fails → log as "FAILED" in REQUEST_LOG
  IF >3 searches failed after retry → BLOCKING (STOP, report to user)

R2: PROFONDEUR MINIMALE
  For each axis, search ≥3 angles: data, money, network
  After step 9, check: "What angles were NOT covered?"
  If gaps → add targeted queries before step 10

R3: SYMÉTRIE RENFORCÉE (clarifies KERNEL step 5)
  IF accusation → generate equal-strength arguments for BOTH sides
  If one side gets more scrutiny → REBALANCE before step 10

R4: INTERDICTION "KNOWN BUT NOT SOURCED"
  Never claim a fact without a source URL
  If unsourced → mark as ⁂ (SPECULATED) or don't claim

R5: CRÉDO COUNT ENFORCEMENT (enforces KERNEL step 6)
  Count queries before proceeding to step 7
  IF <12 → RETURN step 6

---

## §2 GATE REFERENCE (maps to KERNEL §2 — no redefinition)

| Checklist item | KERNEL §2 gate | Severity |
|---------------|----------------|----------|
| TEXT_ANALYSIS executed | ¬TEXT_ANALYSIS → P0 | CRITICAL |
| Clusters ≥5 loaded | ¬CLUSTER(≥5) → P7 | CRITICAL |
| ✦ facts ≥ min | ✦=0 → P9 | CRITICAL |
| Causality chains ≥ min | APEX: chains=0 → P9 | CRITICAL |
| "Qui meurt" present | "Qui meurt"∅ → P12 | CRITICAL |
| APEX sections ≥ 15 | sections<15 → P14 | CRITICAL |
| EDI gap > 0.5 ∧ queries < 35 | BLOCK if edi_gap>.5 ∧ queries<35 | BLOCKING |

New checks (NOT in KERNEL §2):
| Checklist item | Severity |
|---------------|----------|
| Every ✦ fact has a URL | CRITICAL (enforces step 113-114) |
| Dialectical has 3 perspectives | CRITICAL (enforces §3 MANDATORY) |
| Hermeneutic L1-L6 complete | CRITICAL (enforces §3 MANDATORY APEX) |
| Wolves ≥ min named | SEVERE (enforces step 17) |
| REQUEST_LOG complete | SEVERE (enforces step 136-142) |
| No failed searches without retry | BLOCKING (R1 enforcement) |

---

## §3 CORRECTION PROCEDURES (execute when checklist item fails at 18b)

| Failed check | Correction | Max loops |
|-------------|-----------|-----------|
| ✦ < min | RETURN step 9, +15◈ targeted | 2 (KERNEL feedback) |
| chains < min | RETURN step 9, +5 causal | 2 (KERNEL feedback) |
| domains < 2 | RETURN step 9, +5 cross-domain | 2 (KERNEL feedback) |
| 429 not retried | Retry failed queries with @WEB | 1 |
| Symétrie manquante | +5 queries under-scrutinized side | 1 |
| Profondeur insuffisante | +3 angles manquants | 1 |
| URLs manquantes | RETURN step 10, add URLs | 1 |
| >3 searches failed | BLOCKING → STOP, report | — |

---

## §4 PRE-DELIVERY CHECKLIST (executed at step 18b)

IF any □ unchecked → execute corresponding correction (§3). DO NOT proceed to step 19.

```
□ All 15 symbols scored in MANIPULATION_REPORT (KERNEL §0 step 4-6)
□ Clusters loaded per thresholds (KERNEL §0 step 5)
□ CRÉDO has ≥12 queries (KERNEL §1 step 6, enforced by R5)
□ FACT_REGISTRY has ≥min ✦ facts (KERNEL §1 step 10)
□ EVERY ✦ fact has a URL (KERNEL §1 step 113-114)
□ Causality chains ≥3 links, ≥min count (KERNEL §1 step 11)
□ Impact has ALL 4 matrices (KERNEL §3 MANDATORY APEX)
□ Dialectical has 3 perspectives (KERNEL §1 step 8t)
□ Hermeneutic L1-L6 complete (KERNEL §3 MANDATORY APEX)
□ Wolves ≥min named (KERNEL §1 step 17)
□ EDI calculated + BIAS applied (KERNEL §1 step 16)
□ REQUEST_LOG complete with ALL tool calls (KERNEL §1 step 136-142)
□ No failed searches without retry (R1 enforcement)
□ Symmetry applied if accusation (KERNEL §1 step 5, enforced by R3)
```

---

## §5 INTEGRATION NOTES

- Behavioral rules (§1) loaded at KERNEL §0 step 4
- Checklist (§4) executed at KERNEL §1 step 18b
- §2 references KERNEL §2 gates — no duplication
- §3 uses existing KERNEL feedback loops (lines 145-150) where applicable
- Target: ~120 lines

---

_GATES v2.0 — Enforcement mechanism for Truth Engine pipeline._
```

---

### Task 2: Modify KERNEL.md — add step 4, step 18b, §5 FILES

**Files:**
- Modify: `truth-engine-v2/KERNEL.md`

- [ ] **Step 1: Add step 4 in KERNEL §0 (after step 3 @READ[definitions/THREATS.md])**

Find this section in KERNEL.md (lines 56-59):
```
1. @READ[definitions/SYMBOLS.md]   → load 15 narrative + epistemic + factual symbols
2. @READ[definitions/PATTERNS.md]   → load @PAT[] + rhetorical families DEM/BF/NUM/AUTH/FAC
3. @READ[definitions/THREATS.md]    → load @THR[]
```

Add line 4 after line 3:
```
4. @READ[forensic/GATES.md]        → load behavioral rules (see GATES.md §1)
```

- [ ] **Step 2: Add step 18b in KERNEL §1 (between step 18 and step 19)**

Find this section in KERNEL.md (lines 131-132):
```
18 GATE_CHECK       §3 → block if fail
19 SAVE             @MNEMO_S + @WRITE (BOTH mandatory)
```

Insert between them:
```
18b GATE_AUTO       Execute GATES.md §4 checklist
                     IF fail → correction (GATES.md §3) | BLOCKING → STOP
                     IF all pass → proceed to step 19
```

- [ ] **Step 3: Add GATES.md to KERNEL §5 FILES**

Find this section in KERNEL.md (lines 211-217):
```
@READ[definitions/SYMBOLS.md]  @READ[definitions/PATTERNS.md]  @READ[definitions/THREATS.md]
@READ[protocol/INVESTIGATION.md]  @READ[protocol/PERSO_FRESQUE.md]
@READ[clusters/{NAME}.md] (if score ≥5)
@READ[search/EPISTEMIC.md]  @READ[search/TEMPLATES.md]  @READ[search/OPTIMIZATION.md]
@READ[forensic/REASONING.md]  @READ[forensic/REQUEST_LOG.md]
@READ[tools/MACROS.md]  @READ[tools/DSL.md]  @READ[output/TEMPLATE.md]
```

Add GATES.md to the forensic line:
```
@READ[forensic/REASONING.md]  @READ[forensic/REQUEST_LOG.md]  @READ[forensic/GATES.md]
```

---

### Task 3: Update ARCHITECTURE.md

**Files:**
- Modify: `truth-engine-v2/ARCHITECTURE.md`

- [ ] **Step 1: Add GATES.md to Layer 5 file inventory**

Find the Layer 5 section (lines 46-50):
```
### Layer 5: FORENSIC (2 files, loaded on trigger)

| File | Lines | Role | Trigger |
|------|-------|------|---------|
| forensic/REASONING.md | 55 | Iceberg reconstruction (shown/hidden/factor), 4 @Q[] reasoning questions, output transparency | Ξ ≥5 |
| forensic/REQUEST_LOG.md | 108 | Request log format (table structure + URL), quality gates, protocol header | Always (output) |
```

Change to:
```
### Layer 5: FORENSIC (3 files, loaded on trigger)

| File | Lines | Role | Trigger |
|------|-------|------|---------|
| forensic/REASONING.md | 55 | Iceberg reconstruction (shown/hidden/factor), 4 @Q[] reasoning questions, output transparency | Ξ ≥5 |
| forensic/REQUEST_LOG.md | 108 | Request log format (table structure + URL), quality gates, protocol header | Always (output) |
| forensic/GATES.md | ~120 | Auto-validation pipeline: behavioral rules, gate reference, correction procedures, pre-delivery checklist | Always (step 0 + 18b) |
```

- [ ] **Step 2: Update §1 FILE INVENTORY count**

Find line 8:
```
## §1 FILE INVENTORY (32 files)
```

Change to:
```
## §1 FILE INVENTORY (33 files)
```

- [ ] **Step 3: Update §3 PIPELINE → FILE LOADING MAP**

Find the table row for step 0 (line 157):
```
| 0 | TEXT_ANALYSIS | SYMBOLS.md + PATTERNS.md + THREATS.md + clusters/{≥5} | MANIPULATION_REPORT |
```

Change to:
```
| 0 | TEXT_ANALYSIS | SYMBOLS.md + PATTERNS.md + THREATS.md + GATES.md + clusters/{≥5} | MANIPULATION_REPORT |
```

Add row for step 18b (after step 18, before step 19):
```
| 18b | GATE_AUTO | GATES.md §4 checklist | PASS/FAIL + corrections |
```

- [ ] **Step 4: Update §6 RECOMMENDED FIXES**

Add new row to the table:
```
| G1 | Add GATES.md to Layer 5, update counts | 5 min | HIGH |
```

---

### Task 4: Self-review

- [ ] **Step 1: Verify spec coverage**

Check each spec requirement against tasks:
- §1 Behavioral Rules (R1-R5) → Task 1 (GATES.md §1) ✓
- §2 Gate Reference (mapping to KERNEL §2) → Task 1 (GATES.md §2) ✓
- §3 Correction Procedures → Task 1 (GATES.md §3) ✓
- §4 Pre-Delivery Checklist → Task 1 (GATES.md §4) ✓
- §5 Integration Notes → Task 1 (GATES.md §5) ✓
- KERNEL step 4 addition → Task 2 Step 1 ✓
- KERNEL step 18b addition → Task 2 Step 2 ✓
- KERNEL §5 FILES addition → Task 2 Step 3 ✓
- ARCHITECTURE Layer 5 update → Task 3 Step 1 ✓
- ARCHITECTURE file count → Task 3 Step 2 ✓
- ARCHITECTURE pipeline map → Task 3 Step 3 ✓
- ARCHITECTURE recommended fixes → Task 3 Step 4 ✓

- [ ] **Step 2: Placeholder scan**

Search for: TBD, TODO, "implement later", "fill in", "add appropriate", "write tests for", "similar to"
Expected: None found.

- [ ] **Step 3: Verify file paths**

All paths must be absolute or relative to project root:
- `truth-engine-v2/forensic/GATES.md` ✓
- `truth-engine-v2/KERNEL.md` ✓
- `truth-engine-v2/ARCHITECTURE.md` ✓
