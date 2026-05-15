# MACROS v2.0 — Truth Engine Compact Notation System

## Status Macros

```
✅OK[msg]    = → STATUS: **msg** ✅
⚠️WARN[msg]  = → STATUS: **msg** ⚠️
❌FAIL[msg]  = → STATUS: **msg** ❌
🔄ITER[msg]  = → STATUS: **msg** 🔄
```

## Multi-Action Macros

```
FAIL_MCP[cx] =
  → STATUS: **INVESTIGATION FAILED** ❌
  → ERROR: "Web searches MANDATORY for {cx} but MCP not connected"
  → ACTION: "Check MCP_STATUS.md, reconnect, or downgrade to SIMPLE"
  → STOP

DEGRADE_MODE[warn_list] =
  → STATUS: **DEGRADED MODE** ⚠️
  → WARNING: {warn_list}
  → ASK USER: "Proceed? (y/n)"
  → IF no: STOP | IF yes: PROCEED

PARTIAL_I[n,gap] =
  → STATUS: **I{n} PARTIAL** ⚠️
  → WARNING: "I{n} executed {queries}/{min} (gap: -{gap})"
  → PENALTY: ISN -2.0, EDI cap 0.30
  → ACTION: Generate I{n+1} AUTO
  → OUTPUT: "[CRITICAL] INCOMPLETE - {gap} queries missing"

ACCEPT_I[n,gaps] =
  → STATUS: **I{n} ACCEPTABLE** ✅
  → FLAG: "Minor gaps {gaps} within tolerance"
  → ACTION: None
```

## Complexity Macros

```
CX_CHECK[val] = complexity ∈ {val}
CX_ROUTE[S,M,C,A] = IF CX[SIMPLE]:S ELIF CX[MEDIUM]:M ELIF CX[COMPLEX]:C ELIF CX[APEX]:A
CX_TARGET[metric] = {SIMPLE:metric[S], MEDIUM:metric[M], COMPLEX:metric[C], APEX:metric[A]}
```

## Conditional Macros

```
IF_GAP[condition,action] = IF {condition}_gap > 0: → {action}
CHECK_THRESHOLD[metric,val,action] = IF {metric} ≥ {val}: → {action} ELSE: CONTINUE
VALIDATE_TARGET[metric,penalty] = IF {metric} < target: → PENALTY:{penalty} ELSE: → BONUS:+0.1
```

## Query Macros

```
QRY_MIN[cx]       = ≥{SIMPLE:5, MEDIUM:8, COMPLEX:12, APEX:15}[cx]
QRY_ALLOC[p,h,c,d,o] = PRIMARY_◈={p} ADVERSARY_H7={h} CONTEXT_⟐={c} DIVERSITY={d} OPPORTUNISTIC={o}
QRY_ENFORCE[tot,min,iter] =
  IF tot < min AND iter < I2: PARTIAL_I[iter, min-tot]
  ELIF tot < min AND iter ≥ I2: ❌FAIL["Max iterations, queries {tot}/{min}"]
```

## EDI Macros

```
EDI_TARGET[cx] = {SIMPLE:0.30, MEDIUM:0.50, COMPLEX:0.70, APEX:0.80}[cx]
EDI_CALC[] = (geo×0.25 + lang×0.20 + strat×0.20 + owner×0.15 + persp×0.15 + temp×0.05)
EDI_CHECK[val,target] = IF val < target: → FLAG:"EDI gap {target-val}" → TRIGGER:Adaptive search
```

## Output Macros

```
OUT_P1[content] = Output Part 1: {content}
OUT_P2[diag,mod,src] = [DIAGNOSTICS]{diag} [MODULES]{mod} [SOURCES]{src}
OUT_P3_WOLF[actors] = Part 3 WOLF: {actors}
OUT_P3_SKIP[reason] = Part 3: (WOLF {reason})
SAVE_LOG[file] = Generate: logs/YYYY-MM-DD_HH-MM-SS_{file}.md → Write ALL 3 parts → Confirm
```

## Iteration Macros

```
I_AUTO[gaps] = → STATUS: ITERATION RECOMMENDED 🔄 → REASON: Gaps {gaps} → ACTION: Execute "I1 AUTO"
I_COMPLETE[] = → STATUS: INVESTIGATION COMPLETE ✅ → REASON: All targets met
I_CONVERGE[score] = IF score ≥ 0.85: I_COMPLETE[] ELIF score ≥ 0.75: ⚠️WARN["Acceptable"] ELSE: I_AUTO[critical_gaps]
```

## Source Quotas

```
QUOTAS:
  ◈ primary ≥3 (I2 ≥4 ; ≥1 non-EN if pertinent)
  continents ≥2 (geo ≥3)
  non-EN ≥40% (geo often ≥50%)
  non-corporate ≥50%
  adversary ≥1 (sensitive ≥2)
  temporalities ≥3 (real-time, recent, archival)
IF quota unmet → re-query targeted baskets
```

## Coverage & Independence Scores

```
CoverageScore = met_quotas / total_quotas
IndependenceScore = f(diversity_families, low_syndication)
ContradictionCoverage = adversary_present × divergence_processed
EDI* = 0.5×EDI + 0.3×Coverage + 0.2×Independence
Output: "COV:{c} IND:{i} CC:{cc} → EDI*:{e}"
```

---

*MACROS v2.0 — Compact notation. Canonical source (DSL §7 references this file).*
