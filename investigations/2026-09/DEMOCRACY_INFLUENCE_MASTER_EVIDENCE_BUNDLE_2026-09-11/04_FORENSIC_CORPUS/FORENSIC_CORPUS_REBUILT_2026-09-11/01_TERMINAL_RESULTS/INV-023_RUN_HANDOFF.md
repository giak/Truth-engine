---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-023-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-023"
---

<!-- DERIVED_FROM: te_run=20260906-1258-russie-financement-partis-europe; artifact=2026-09-06_12-58_russie-financement-partis-europe_INVESTIGATION.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->
<!-- TRACE: process_deviation=pre_run_registry_gate_bypassed; historical_registry_status=BACKLOG; history_rewritten=false -->

# RUN_HANDOFF — INV-023

## INV_ID

`INV-023`

## TE status/path

```text
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-1258-russie-financement-partis-europe
TE_PATH = 2026-09-06_12-58_russie-financement-partis-europe_INVESTIGATION.md
MNEMO = MNEMO_UNAVAILABLE degraded / terminal accounting coherent
PROCESS_DEVIATION = run launched while registry still BACKLOG; project pre-run gate was bypassed and is logged, not retroactively rewritten
```

## Central delta

The investigation does **not** support a single class "European parties financed or controlled by Russia". It separates materially different mechanisms and evidentiary ceilings:

- received financing without demonstrated political quid pro quo (`CLM-001`, `CAU-001`);
- formal inter-party cooperation without demonstrated financing/tasking (`CLM-002`, `CLM-003`, `CAU-002`);
- attempted but unrealized party financing (`CLM-004`, `CAU-003`);
- a documented funded influence vehicle/network in the Voice of Europe case (`CLM-005`, `CAU-004`, `ACT-005`);
- individual responsibility allegations still under procedural/judicial ceiling (`CLM-006`, `CLM-007`, `ACT-006`, `ACT-007`);
- a negative control where Russian contacts did not establish third-party Russian funding (`CLM-008`, `CAU-007`).

The material model is therefore **typed relations + typed flows + typed evidentiary ceilings**, not guilt by proximity.

## Highest supported I0..I7

```text
I0 IDENTITY / RELATION             = VERIFIED across selected cases
I1 RESOURCES / CAPABILITY / ACCESS = VERIFIED where loan/vehicle/access objects exist; case-specific elsewhere
I2 DOCUMENTED ACTION               = VERIFIED/SUPPORTED for loan, agreements, attempted financing and Voice of Europe mechanism
I3 COORDINATION / TASKING / CONTROL= VERIFIED for the documented Voice of Europe vehicle/network only; party agreements establish cooperation, not command; Bystron/Ždanoka individual tasking remains UNRESOLVED
I4 EXPOSURE / REACH                = PARTIAL / not measured comparably across the case set
I5 RECEPTION / PERSUASION          = UNRESOLVED
I6 BEHAVIOR / INSTITUTIONAL CHANGE = institutional controls/responses VERIFIED; influence-caused political/electoral change NOT_ESTABLISHED
I7 COUNTERFACTUAL OUTCOME          = NOT_ESTABLISHED
```

## Material gaps/contradictions

- `FCT-002 / CLM-001`: no political quid pro quo established for the FN/RN Russian-bank loan.
- `FCT-006 / CLM-002`: material implementation/financing of the FPÖ–United Russia agreement remains unestablished in the bounded corpus.
- `FCT-010 / CLM-004`: Metropol targeted financing but the transaction did not occur; attempt must not be counted as received funding.
- `CLM-006 / CAU-005 / ACT-006`: Bystron individual quid pro quo remains under a responsibility/adjudication ceiling.
- `CLM-007 / CAU-006 / ACT-007`: Ždanoka intelligence cooperation/tasking remains under a responsibility/adjudication ceiling.
- `AXS-008`: no causal attribution of aggregate political/electoral change to these relations/flows.
- `CLM-008 / CAU-007`: Leave.EU is a material negative control against `Russian contacts -> Russian funding`.

## RENARD decision + reason

```text
RENARD = NO
```

The residuals are either future procedural endpoints (Bystron/Ždanoka), missing primary evidence of quid pro quo/implementation (RN/FPÖ), or causal-effect questions requiring new designs/data rather than more generic searching (`AXS-008`). None is an accessible residual that currently promises to change the **central typed-mechanism model**. A broad RENARD pass would mostly accumulate more cases and risk selection bias/fishing rather than discriminate the model.

A targeted current-status discovery check did not identify a final public adjudication closing the decisive Bystron/Ždanoka responsibility gaps; no Truth Engine FINAL content is rewritten by that check.

## New ideas triaged

```text
Bystron final adjudication / Voice of Europe quid pro quo   -> RECHECK when final judicial disposition becomes public
Ždanoka final adjudication / intelligence cooperation      -> RECHECK when final public disposition becomes available
RN loan political quid pro quo                             -> DEFER until new primary/court/financial evidence
FPÖ agreement material implementation                      -> DEFER until a concrete implementation trace appears
Voice of Europe wider network                              -> DEFER; create a new case only if a branch can change coordination/tasking model
aggregate financing -> political/electoral effect          -> MERGE into later causal/synthesis work; no standalone case accumulation
```

## Registry patch

```text
INV-023 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-023_RUN_HANDOFF.md
process_deviation -> pre-run registry status was BACKLOG; preserved in trace

INV-022 -> TE_DONE / DELIVERY_PASS_R3 / RENARD UNDECIDED
           (reconciles actual completed TE run without pretending post-run review is done)

INV-103 -> remains READY / NOT_RUN
```
