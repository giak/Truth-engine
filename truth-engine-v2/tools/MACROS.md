# MACROS v2.1 — Compact control notation

Macros abbreviate canonical behavior; they never override KERNEL or domain authorities.

## Status

```text
✅OK[msg]   = STATUS:msg OK
⚠️WARN[msg] = STATUS:msg WARNING + explicit impact
❌FAIL[msg] = STATUS:msg BLOCKED + gate/reason
🔄ITER[msg] = STATUS:msg TARGETED_CORRECTION
```

## Runtime/degraded mode

```text
FAIL_MCP[reason] = log FAILED:{reason}; continue degraded if evidence can still be inspected; otherwise INCONCLUSIVE
DEGRADE_MODE[gaps] = proceed with visible gaps unless a GATES critical condition depends on them
PARTIAL_I[n,gap] = record iteration, unresolved material gap and next bounded query; no automatic score penalty
ACCEPT_I[n,gaps] = accept only after saturation/limit; expose gaps
```

## Routing

```text
CX_CHECK[val] = $CX == val
CX_ROUTE[S,M,C,A] = choose branch from stored $CX
CX_TARGET[metric] = read canonical target from KERNEL/EPISTEMIC/OUTPUT owner
CHECK_THRESHOLD[metric,val,action] = compare observed metric; action routes work, never verdict
IF_GAP[condition,action] = if material condition unresolved, run bounded action per GATES §4
VALIDATE_TARGET[metric,action] = target miss → action while material; else disclose saturation
```

## Search and iteration

```text
QRY_MIN[cx] = KERNEL step 6 target (compatibility name; target, not quota)
QRY_ALLOC[p,h,c,d,o] = planning guide only; decisive gaps may reallocate
QRY_ENFORCE[tot,target,iter] = if material gap remains, bounded targeted iteration; else record shortfall
I_AUTO[gaps] = one GATES-bounded correction on material gaps
I_COMPLETE[] = critical gates pass + material searches saturated/limited
I_CONVERGE[score] = apply EPISTEMIC C(n); convergence never means truth
```

## EDI

```text
EDI_TARGET[cx] = search/EPISTEMIC.md §3
EDI_CALC[] = search/EPISTEMIC.md §3 applicable-weight calculation
EDI_CHECK[val,target] = diagnose gap; targeted diversity search if material; never upgrade facts
CoverageScore | IndependenceScore | ContradictionCoverage | EDI* = EPISTEMIC §4
```

## Output/save

```text
OUT_P1[content] = output content, not file-splitting authority
OUT_P2[content] = output continuation, not file-splitting authority
OUT_P3_WOLF[actors] = responsibility map with sourced action/intent type
OUT_P3_SKIP[reason] = NO INDIVIDUAL RESPONSIBILITY ESTABLISHED:{reason}
SAVE_LOG[file] = compatibility alias → append REQUEST_LOG to investigation; save via KERNEL step 19
SERIAL_PENDING[action] = REQUEST_LOG result PENDING_AT_SERIALIZATION
```

_Canonical authority: compact control aliases only._
