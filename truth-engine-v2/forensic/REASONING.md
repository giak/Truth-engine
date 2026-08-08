# FORENSIC REASONING v2.1 — Hidden-reality reconstruction

**Trigger:** `Ξ≥5`. This module separates shown, omitted, reconstructed and unknowable quantities; it does not assume that omission is deliberate.

## Four questions

```text
@Q[1:HIDDEN]      Which definitions, populations, periods, regions or denominators are excluded?
@Q[2:EVIDENCE]    Which direct sources expose inclusion/exclusion and methodology?
@Q[3:RECONSTRUCT] Can a comparable total or bounded range be calculated without mixing units/scopes?
@Q[4:LIMITS]      Which assumptions dominate the result, and what would invalidate it?
```

## Method

1. Quote the visible claim and its scope.
2. Retrieve definition, method, denominator and revisions.
3. List omitted components with source and inclusion rationale.
4. Reconstruct only comparable quantities; show formula, units and range.
5. Run sensitivity on uncertain inputs and test an innocent methodological explanation.
6. Label every component `FOUND`, `ESTIMATED` or `UNKNOWN`.

`ICEBERG_FACTOR = comparable_total / visible_value` only when both values share definition, unit, population and period. Otherwise report `NOT COMPUTABLE` plus the omission map.

## Output

```text
[FORENSIC] Ξ:{score} | domain:{domain}
VISIBLE: {value, definition, period, source, status}
OMITTED: {component → evidence → reason applicable}
RECONSTRUCTION: {formula, range, sensitivity} OR NOT COMPUTABLE
VISIBLE_SHARE/FACTOR: {value} OR NOT COMPUTABLE
ALTERNATIVE EXPLANATION: {tested result}
CONFIDENCE: {HIGH|MEDIUM|LOW} | LIMITS:{assumptions/gaps}
```

Useful domain contrasts: direct/indirect deaths; unemployment/underemployment/halo; reported/excess mortality; sentenced/pre-trial/control; reported/dark-figure losses; territorial/consumption emissions. Apply only definitions supported in the case.

_Canonical authority: Ξ reconstruction method._
