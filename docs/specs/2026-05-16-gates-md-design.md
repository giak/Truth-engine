# DESIGN — GATES.md: Auto-Validation Pipeline for Truth Engine v2

**Date:** 2026-05-16
**Author:** Truth Engine
**Status:** Draft — awaiting user review (rev2 after double-check)

---

## §1 Problem Statement

Truth Engine v2.0 has a well-defined pipeline (KERNEL.md, 19 steps) with gates defined in §2, but **no enforcement mechanism**. The LLM can deliver incomplete investigations because:

1. Gates exist on paper (§2 GATES) but are never actually checked before delivery
2. Failed searches (429) are ignored instead of retried
3. Depth defaults to minimum effort — user must prompt "approfondis"
4. Symmetry (KERNEL step 5) is applied inconsistently
5. No pre-delivery checklist forces the LLM to verify its own output

**Result:** 3 of 4 investigations were incomplete or had unaddressed search failures.

---

## §2 Solution: GATES.md

A new file in `forensic/GATES.md` that adds what KERNEL §2 lacks:

1. **Behavioral rules** (R1-R5) — how the LLM must behave during the pipeline
2. **Pre-delivery checklist** (§4) — explicit checks executed at step 18b BEFORE delivery
3. **Fallback rules** — what to do when searches fail (429)
4. **No duplication** — references KERNEL §2 gates, doesn't redefine them

### File Location
`truth-engine-v2/forensic/GATES.md`

### Load Points
- **KERNEL §0 step 4:** Loaded after THREATS.md — behavioral rules apply to entire pipeline
- **KERNEL §1 step 18b:** Executed as GATE_AUTO — pre-delivery checklist

### Relationship with KERNEL §2 GATES
- KERNEL §2 = gate definitions (severity formula, CRITICAL/BLOCK conditions)
- GATES.md = enforcement mechanism (checklist, behavioral rules, fallbacks)
- GATES.md §2 **references** KERNEL §2 gates, doesn't redefine them
- GATES.md §4 checklist **verifies** that KERNEL §2 gates would pass

### KERNEL Modifications (2 lines)

**KERNEL §0 (add as step 4, after @READ[definitions/THREATS.md]):**
```
4. @READ[forensic/GATES.md] → load behavioral rules (see GATES.md §1)
```

**KERNEL §1 (add step 18b, between step 18 GATE_CHECK and step 19 SAVE):**
```
18b GATE_AUTO: Execute GATES.md §4 checklist
  IF any check fails → apply correction (GATES.md §3)
  IF blocking condition → STOP, report to user
  IF all pass → proceed to step 19
```

**KERNEL §5 FILES (add 1 line):**
```
@READ[forensic/GATES.md]
```

---

## §3 GATES.md Content

### §1 Behavioral Rules (R1-R5)

**R1: 429 fallback → DuckDuckGo immediately**
- IF @EXA returns 429 → IMMEDIATELY retry same query with @WEB (DuckDuckGo)
- IF @WEB also fails → log as "FAILED" in REQUEST_LOG
- IF >3 searches failed after retry → BLOCKING (stop, report to user)
- *Not in KERNEL. KERNEL §1 line 38 says "STOP using Exa" but doesn't say "retry with @WEB".*

**R2: Profondeur minimale**
- For each investigation axis, search at least 3 angles: data, money, network
- After step 9 searches complete, explicitly check: "What angles were NOT covered?"
- If gaps identified → add targeted queries before step 10
- *Not in KERNEL.*

**R3: Symétrie renforcée**
- KERNEL step 5 says "SYMETRIC_CHECK (accusator too)" but doesn't define what that means
- R3 defines it: generate equal-strength arguments for BOTH sides
- If one side gets more scrutiny → REBALANCE before step 10
- *Clarifies KERNEL step 5, doesn't replace it.*

**R4: Interdiction "known but not sourced"**
- Never claim a fact without a source URL
- If you "know" something but can't source it → don't claim it, or mark as ⁂ (SPECULATED)
- *Reinforces KERNEL step 10 rules.*

**R5: CRÉDO count enforcement**
- KERNEL step 6 says "12-20 queries" but LLM can skip
- R5: Count queries before proceeding to step 7. If <12 → RETURN step 6
- *Enforces existing KERNEL rule, doesn't create a new one.*

### §2 Gate Reference (not redefinition)

This section maps pre-delivery checklist items to KERNEL §2 gates:

| Checklist item | KERNEL §2 gate | Severity |
|---------------|----------------|----------|
| TEXT_ANALYSIS executed | ¬TEXT_ANALYSIS → P0 | CRITICAL |
| Clusters ≥5 loaded | ¬CLUSTER(≥5) → P7 | CRITICAL |
| ✦ facts ≥ min | ✦=0 → P9 | CRITICAL |
| Causality chains ≥ min | APEX: chains=0 → P9 | CRITICAL |
| "Qui meurt" present | "Qui meurt"∅ → P12 | CRITICAL |
| APEX sections ≥ 15 | sections<15 → P14 | CRITICAL |
| EDI gap > 0.5 ∧ queries < 35 | BLOCK if edi_gap>.5 ∧ queries<35 | BLOCKING |

**New checks NOT in KERNEL §2:**
| Checklist item | Severity |
|---------------|----------|
| Every ✦ fact has a URL | CRITICAL (enforces step 10 rule) |
| Dialectical has 3 perspectives | CRITICAL (enforces §3 MANDATORY) |
| Hermeneutic L1-L6 complete | CRITICAL (enforces §3 MANDATORY APEX) |
| Wolves ≥ min named | SEVERE (enforces step 17) |
| REQUEST_LOG complete | SEVERE (enforces step 136-142) |
| No failed searches without retry | BLOCKING (new — R1 enforcement) |
| @MNEMO_S called | SEVERE (enforces step 19) |

Note: @WRITE is NOT checked at 18b — it happens at step 19, after 18b.

### §3 Correction Procedures

These execute when a checklist item fails at step 18b:

| Failed check | Correction | Max loops |
|-------------|-----------|-----------|
| ✦ < min | RETURN step 9, +15◈ targeted queries | 2 (KERNEL feedback loop) |
| chains < min | RETURN step 9, +5 causal queries | 2 (KERNEL feedback loop) |
| domains < 2 | RETURN step 9, +5 cross-domain queries | 2 (KERNEL feedback loop) |
| 429 not retried | Retry failed queries with @WEB | 1 |
| Symétrie manquante | Add 5 queries for under-scrutinized side | 1 |
| Profondeur insuffisante | +3 angles manquants (data/money/network) | 1 |
| URLs manquantes | RETURN step 10, add URLs | 1 |
| >3 searches failed | BLOCKING → STOP, report to user | — |

### §4 Pre-Delivery Checklist (step 18b)

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

**IF any □ unchecked → execute corresponding correction procedure (§3). DO NOT proceed to step 19.**

### §5 Integration Notes

- GATES.md §1 behavioral rules are loaded at KERNEL §0 step 4
- GATES.md §4 checklist is executed at KERNEL §1 step 18b
- GATES.md §2 references KERNEL §2 gates — no duplication
- GATES.md §3 correction procedures use existing KERNEL feedback loops (lines 145-150) where applicable
- Total file size target: ~120-150 lines

---

## §4 Scope & Boundaries

**In scope:**
- 1 new file: `forensic/GATES.md` (~120-150 lines)
- 2 lines added to KERNEL.md (§0 step 4, §1 step 18b)
- 1 line added to KERNEL §5 FILES
- ARCHITECTURE.md update (Layer 5, dependency graph)

**Out of scope:**
- No changes to SYMBOLS.md, PATTERNS.md, THREATS.md
- No changes to cluster files
- No changes to search/ files
- No changes to output/TEMPLATE.md
- No changes to KERNEL §2 GATES (references, not replaces)
- No MnemoLite modifications

---

## §5 Success Criteria

After implementation:
1. No investigation delivered with failed searches unaddressed (R1 + checklist)
2. CRÉDO always has ≥12 queries (R5 enforcement)
3. Symmetry applied on all accusations (R3)
4. Depth defaults to 3 angles per axis (R2)
5. Pre-delivery checklist catches all incomplete outputs (§4)
6. User no longer needs to prompt "approfondis" or "double check"

---

## §6 Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Context window overflow from GATES.md load | Medium | Keep file <150 lines, compact notation |
| Correction loops consume too many tokens | Medium | Max 2 loops (uses existing KERNEL feedback) |
| LLM ignores gates anyway | High | Checklist is explicit, checkable, with consequences |
| Over-engineering for SIMPLE investigations | Low | Checklist items scale by complexity (fewer checks for SIMPLE) |
