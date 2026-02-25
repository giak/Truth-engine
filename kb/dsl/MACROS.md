# Truth Engine Macros v9.0 - Compact Notation System

## Action Macros (Replace verbose YAML)

### Status Macros
```
✅OK[msg] = → STATUS: **msg** ✅
⚠️WARN[msg] = → STATUS: **msg** ⚠️
❌FAIL[msg] = → STATUS: **msg** ❌
🔄ITER[msg] = → STATUS: **msg** 🔄
```

### Multi-Action Macros
```
FAIL_MCP[complexity] =
  → STATUS: **INVESTIGATION FAILED** ❌
  → ERROR: "Web searches MANDATORY for {complexity} but MCP not connected"
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
  → OUTPUT: Flag "[CRITICAL] INCOMPLETE - {gap} queries missing"

ACCEPT_I[n,gaps] =
  → STATUS: **I{n} ACCEPTABLE** ✅
  → FLAG: "Minor gaps {gaps} within tolerance"
  → ACTION: None
  → OUTPUT: Continue with I{n} results
```

## Complexity Macros

```
CX_CHECK[val] = complexity ∈ {val}
CX_ROUTE[S,M,C,A] =
  IF CX[SIMPLE]: S
  ELIF CX[MEDIUM]: M
  ELIF CX[COMPLEX]: C
  ELIF CX[APEX]: A

CX_TARGET[metric] =
  SIMPLE: {metric}_targets[SIMPLE]
  MEDIUM: {metric}_targets[MEDIUM]
  COMPLEX: {metric}_targets[COMPLEX]
  APEX: {metric}_targets[APEX]
```

## Conditional Macros

```
IF_GAP[condition,action] =
  IF {condition}_gap > 0:
    → {action}

CHECK_THRESHOLD[metric,val,action] =
  IF {metric} ≥ {val}:
    → {action}
  ELSE:
    → CONTINUE

VALIDATE_TARGET[metric,penalty] =
  IF {metric} < target_{metric}:
    → PENALTY: {penalty}
  ELSE:
    → BONUS: +0.1
```

## Query Macros

```
QRY_MIN[cx] = ≥{SIMPLE:5, MEDIUM:8, COMPLEX:12, APEX:15}[cx]
QRY_ALLOC[primary,h7,context,div,opp] =
  PRIMARY_◈={primary}
  ADVERSARY_H7={h7}
  CONTEXT_⟐={context}
  DIVERSITY={div}
  OPPORTUNISTIC={opp}

QRY_ENFORCE[total,min,iter] =
  IF total < min AND iter < I2:
    PARTIAL_I[iter, min-total]
  ELIF total < min AND iter ≥ I2:
    ❌FAIL["Max iterations, queries {total}/{min}"]
```

## EDI Macros

```
EDI_TARGET[cx] = {SIMPLE:0.30, MEDIUM:0.50, COMPLEX:0.70, APEX:0.80}[cx]
EDI_CALC[] = (geo×0.25 + lang×0.20 + strat×0.20 + owner×0.15 + persp×0.15 + temp×0.05)
  # geo=géographie, lang=langues, strat=stratification sources ◈◉○,
  # owner=propriété médias, persp=perspectives narratives, temp=temporalités
  # Source unique de vérité: KERNEL.md §4.2
EDI_CHECK[val,target] =
  IF val < target:
    → FLAG: "EDI gap {target-val}"
    → TRIGGER: Adaptive search
```

## Output Macros

```
OUT_P1[content] = Output Part 1: {content}
OUT_P2[diag,modules,sources] =
  [DIAGNOSTICS] {diag}
  [MODULES] {modules}
  [SOURCES] {sources}
OUT_P3_WOLF[actors] = Part 3 WOLF: {actors}
OUT_P3_SKIP[reason] = Part 3: (WOLF {reason})

SAVE_LOG[file] =
  Generate: logs/YYYY-MM-DD_HH-MM-SS_{file}.md
  Write: ALL 3 parts
  Confirm: Success
```

## Iteration Macros

```
I_AUTO[gaps] =
  → STATUS: ITERATION RECOMMENDED 🔄
  → REASON: Gaps identified {gaps}
  → ACTION: Execute "I1 AUTO"
  → PRIORITY: {gaps ranked}

I_COMPLETE[] =
  → STATUS: INVESTIGATION COMPLETE ✅
  → REASON: All targets met
  → ACTION: None

I_CONVERGE[score] =
  IF score ≥ 0.85: I_COMPLETE[]
  ELIF score ≥ 0.75: ⚠️WARN["Acceptable, minor gaps"]
  ELSE: I_AUTO[critical_gaps]
```

## Usage Examples

### Before (12 lines):
```yaml
IF complexity ∈ {COMPLEX, APEX}:
  → STATUS: **INVESTIGATION FAILED** ❌
  → ERROR: "Web searches MANDATORY for {complexity} investigation but MCP not connected"
  → ACTION: "1. Check MCP status: MCP_STATUS.md
            2. Reconnect web-search MCP server
            3. OR downgrade to SIMPLE analysis"
  → STOP: Do not proceed with KB-only analysis

ELIF complexity ∈ {SIMPLE, MEDIUM}:
  → STATUS: **DEGRADED MODE** ⚠️
  → WARNING: "Web searches unavailable. KB-only analysis will have:
              - EDI ≤0.30
              - ◈ PRIMARY likely 0
              - Mono-perspective bias"
  → ASK USER: "Proceed with degraded KB-only analysis? (y/n)"
  → IF user declines: STOP
  → IF user accepts: PROCEED with warnings
```

### After (2 lines):
```
IF CX_CHECK[COMPLEX,APEX]: FAIL_MCP[complexity]
ELIF CX_CHECK[SIMPLE,MEDIUM]: DEGRADE_MODE[EDI≤0.30, ◈=0, mono-bias]
```

## Compression Ratio
- Average: 6:1 (6 lines → 1 line)
- Best case: 12:1
- Worst case: 3:1
- Estimated savings: ~400 lines in system.md

---

## Source Quotas [SOURCE: kb/dsl/QUOTAS.md]

```
QUOTAS (defaults — adapter par domaine/profil):
  ◈ primary    ≥3  (I2 target ≥4 ; ≥1 non-EN si pertinent)
  continents   ≥2  (geo ≥3)
  non-EN       ≥40% (geo souvent ≥50%)
  non-corporate ≥50%
  adversary    ≥1  (sensitive ≥2)
  temporalities ≥3 (real-time, recent, archival)

IF quota unmet → re-query targeted baskets
```

## Coverage & Independence Scores [SOURCE: kb/dsl/SCORES.md]

```
CoverageScore     = met_quotas / total_quotas          (0-1)
IndependenceScore = f(diversity_families, low_syndication) (0-1)
ContradictionCoverage = adversary_present × divergence_processed (0-1)

EDI_star = 0.5×EDI + 0.3×CoverageScore + 0.2×IndependenceScore

Output (optional Part 2):
  "COV:{c} IND:{i} CC:{cc} → EDI*:{e}"
```

