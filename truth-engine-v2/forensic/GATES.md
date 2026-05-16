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
| Dialectical has 3 perspectives | CRITICAL (enforces KERNEL §3 MANDATORY) |
| Hermeneutic L1-L6 complete | CRITICAL (enforces KERNEL §3 MANDATORY APEX) |
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
□ All 15 symbols scored in MANIPULATION_REPORT (KERNEL §0 step 5-6)
□ Clusters loaded per thresholds (KERNEL §0 step 6)
□ CRÉDO has ≥12 queries (KERNEL §1 step 6, enforced by R5)
□ FACT_REGISTRY has ≥min ✦ facts (KERNEL §1 step 10)
□ EVERY ✦ fact has a URL (KERNEL §1 step 10)
□ Causality chains ≥3 links, ≥min count (KERNEL §1 step 11)
□ Impact has ALL 4 matrices (KERNEL §3 MANDATORY APEX)
□ Dialectical has 3 perspectives (KERNEL §1 step 8t)
□ Hermeneutic L1-L6 complete (KERNEL §3 MANDATORY APEX)
□ Wolves ≥min named (KERNEL §1 step 17)
□ EDI calculated + BIAS applied (KERNEL §1 step 16)
□ REQUEST_LOG complete with ALL tool calls (KERNEL §1 lines 140-146)
□ No failed searches without retry (R1 enforcement)
□ Symmetry applied if accusation (KERNEL §1 step 5, enforced by R3)
```

---

## §5 INTEGRATION NOTES

- Behavioral rules (§1) loaded at KERNEL §0 step 4
- Checklist (§4) executed at KERNEL §1 step 18b
- §2 references KERNEL §2 gates — no duplication
- §3 uses existing KERNEL feedback loops (lines 149-154) where applicable

---

_GATES v2.0 — Enforcement mechanism for Truth Engine pipeline._
