# MACROS v2.8 — Compact control notation

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
REQUIRED_LOAD[f] = scheduled canonical @READ; failure → BLOCK_IF[MODULE_UNAVAILABLE:f]
OPTIONAL_LOAD[f] = failure → DEGRADE_IF[MODULE_UNAVAILABLE:f ∧ branch non-material]; material branch → EMIT[INCONCLUSIVE:MODULE_UNAVAILABLE:f]
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
LEAD_ROUTE[id,routes] = KERNEL ROUTE_OK
OBJECT_COVERAGE[] = KERNEL COVER_OK
AXIS_ROUTE[id,objects] = KERNEL GAP_OK + SAT_OK + TERM_AXS
INVESTIGATION_STOP[] = KERNEL STOP_OK
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
WOLVES_MAP[actors] = responsibility map with sourced action/intent type
WOLVES_SKIP[reason] = NO INDIVIDUAL RESPONSIBILITY ESTABLISHED:{reason}
TRACE_CHECK[] = KERNEL TRACE_OK
CHECKPOINT_SAVE[label] = KERNEL CP_OK
RESUME_LOAD[path] = KERNEL RESUME_OK, including validated v2.7→v2.8 OPEN migration
FINALIZE[] = KERNEL FINAL_OK
DELTA_BUILD[] = UPDATE.md differential classification + affected-ID propagation
SAVE_LOG[file] = compatibility alias → include REQUEST_LOG; persist via KERNEL checkpoints/final step 19
SERIAL_PENDING[action] = FINAL-write/writeback REQUEST_LOG result PENDING_AT_SERIALIZATION
SOURCE_TAG[key] = computed SHA1_UTF8 hash tag when preflight capability exists; otherwise omit tag and use the pre-freeze HASH_UNAVAILABLE flag; never invent hash
```

_Canonical authority: compact control aliases only._
