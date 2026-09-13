# EXECUTION_PLAN v0.7

## Foundation

`INV-001 PASS -> INV-002 PASS -> backlog audit PASS -> METHOD_PACK v0.1 BUILT/PASS_STATIC`

## Current gate

`HUMAN_REVIEW_METHOD_PACK`

No content investigation is runnable until this gate is accepted.

## Pilot

Execute sequentially, never batch:

1. INV-010
2. INV-019
3. INV-049
4. INV-071
5. INV-103

After each:

1. inspect Truth Engine final/gates;
2. build RUN_HANDOFF;
3. decide RENARD;
4. if RENARD, run delta-only and update handoff;
5. triage new ideas;
6. patch registry/dashboard;
7. patch METHOD_PACK only for a demonstrated generalizable defect.

## After pilot

If `PILOT_GATE` passes, enable `MAIN_DYNAMIC`.
Choose one next investigation at a time by:

`model_change > discrimination > dependency_unlock > coverage_gap > utility`

Conditional cases require their explicit gate. Syntheses require dependencies. INV-133 remains final.
