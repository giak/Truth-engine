---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-022-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-022"
---

<!-- DERIVED_FROM: te_run=20260906-1057-russie-operations-influence-france; artifact=2026-09-06_10-57_russie-operations-influence-france_INVESTIGATION.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3; renard=NO; inv=CLOSED -->
<!-- TRACE: same_day_post_run=true; truth_engine_final_rewritten=false; r3_e2e_verifier_defects_repaired_separately_in=R3P1 -->

# RUN_HANDOFF — INV-022

## INV_ID

`INV-022`

## TE status/path

```text
TE_STATUS = DELIVERY_PASS_R3
TE_RUN_ID = 20260906-1057-russie-operations-influence-france
TE_PATH = 2026-09-06_10-57_russie-operations-influence-france_INVESTIGATION.md
MNEMO = MNEMO_UNAVAILABLE degraded / terminal accounting coherent
POST_RUN = REVIEW_COMPLETE
```

## Central delta

The run establishes repeated and adaptive Russia-linked influence operations materially targeting France, with documented infrastructure/actor relations for several branches and observable local effects on content availability, intermediary workload and removed assets.

It does **not** establish a causal effect on French opinion, behavior or an electoral result. Exposure is heterogeneous and in several measured cases low or limited. The central model therefore remains:

```text
OPERATION / TARGETING / INFRASTRUCTURE = ESTABLISHED on several branches
EXPOSURE                              = HETEROGENEOUS / PARTIAL
PERSUASION                            = NOT_ESTABLISHED
BEHAVIORAL / ELECTORAL EFFECT         = NOT_ESTABLISHED
UNIFIED COMMAND ACROSS ALL MOI        = NOT_ESTABLISHED
```

The main attribution boundary is preserved rather than averaged away: VIGINUM 2026 attributes Storm-1516 to GRU Unit 29155, while the inspected public chain does not independently reproduce the full command bridge (`CLM-007`, `CAU-006`).

## Highest supported I0..I7

```text
I0 IDENTITY / RELATION             = VERIFIED for several operations/infrastructure branches; bounded attribution caveats remain
I1 RESOURCES / CAPABILITY / ACCESS = VERIFIED for documented infrastructure, automation, domains/accounts and operator assets
I2 DOCUMENTED ACTION               = VERIFIED for France-targeted operations and multiple mitigation actions
I3 COORDINATION / TASKING / CONTROL= VERIFIED/SUPPORTED for some bounded branches; direct GRU 29155 -> Storm-1516 command remains UNRESOLVED
I4 EXPOSURE / REACH                = PARTIAL / HETEROGENEOUS; some measurements are low or limited and not longitudinal
I5 RECEPTION / PERSUASION          = UNRESOLVED / NOT_ESTABLISHED
I6 BEHAVIOR / INSTITUTIONAL CHANGE = local operational effects and mitigation responses VERIFIED; opinion/electoral change NOT_ESTABLISHED
I7 COUNTERFACTUAL OUTCOME          = NOT_ESTABLISHED
```

## Material gaps/contradictions

- `CLM-002`: no longitudinal France-specific Portal Kombat audience series for 2022–2026.
- `CLM-003`, `CLM-005`, `CLM-006`, `CAU-005`: no public causal design isolates persuasion, behavior change or electoral effect.
- `CLM-007`, `CAU-006`: independent public reproduction of the `Storm-1516 -> GRU Unit 29155` attribution bridge remains incomplete.
- `CLM-008`: asset-level takedown effects are documented; aggregate deterrence on the wider ecosystem is not isolated.
- Public network topology remains incomplete; graph density/volume cannot be promoted to causal influence.

## RENARD decision + reason

```text
RENARD = NO
```

The decisive residuals are not good candidates for a generic delta-search immediately after this same-day APEX run:

- persuasion/electoral effect requires causal designs or new outcome data, not more operation examples;
- aggregate deterrence requires longitudinal ecosystem evidence;
- the GRU 29155 attribution gap requires a new independent/public attribution bridge, not repetition of the existing official assertion;
- Portal Kombat exposure requires a longitudinal France-specific audience series.

A broad RENARD pass would mostly add cases or duplicate already-inspected attribution/exposure material without a clear model-changing test. Reopen only when a material new source directly targets one of these discriminating gaps.

## New ideas triaged

```text
Storm-1516 -> GRU 29155 independent attribution bridge   -> RECHECK on new independent/public evidence
Portal Kombat longitudinal France audience               -> RECHECK when comparable time-series data exists
operation exposure -> persuasion/electoral effect        -> MERGE into later causal/synthesis work requiring causal design
takedown -> aggregate deterrence                          -> DEFER until longitudinal ecosystem evidence
new Russia-linked operation                              -> DEFER unless it changes actor/tasking/impact model
INV-023 financing/party-relations branch                 -> ALREADY_EXECUTED / separate CLOSED case
```

## Registry patch

```text
INV-022 -> CLOSED
truth_engine -> DELIVERY_PASS_R3
renard -> NO
result_path -> INV-022_RUN_HANDOFF.md
next_action -> NONE

INV-103 -> remains READY / NOT_RUN
```

No Truth Engine FINAL artifact is modified by this post-run closure.
