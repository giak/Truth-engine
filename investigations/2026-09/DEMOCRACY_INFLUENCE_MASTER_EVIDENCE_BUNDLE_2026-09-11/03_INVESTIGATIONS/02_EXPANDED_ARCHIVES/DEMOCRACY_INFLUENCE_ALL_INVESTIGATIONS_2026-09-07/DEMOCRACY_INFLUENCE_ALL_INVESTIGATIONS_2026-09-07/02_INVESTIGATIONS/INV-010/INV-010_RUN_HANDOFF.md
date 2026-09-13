---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-010-R2A2-HANDOFF"
version: "1.0"
status: "pilot_review"
updated: "2026-09-05"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-010"
---

<!-- DERIVED_FROM: run=20260905-1635-inv010-r4; retry_scope=persistence_delivery_only -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R2A2; renard_execution=NOT_RUN -->

# RUN_HANDOFF — INV-010 / R2A.2

```text
TE_STATUS = DELIVERY_PASS_R2A2
DELIVERY_GATE = PASS / deterministic PASS
PERSISTENCE = ATTEMPT-001 PARTIAL -> ATTEMPT-002 PASS
MNEMO = MNEMO_UNAVAILABLE degraded
FACTS = 10 FACT/✧, mem="-" preserved
RESEARCH_REPLAY = NO
NARRATIVE_CHANGED = NO
SEMANTIC_REGISTRIES_CHANGED = NO
RENARD = CLOSED_NO_FURTHER_MATERIAL_DELTA
```

## Central delta

No epistemic/content delta was introduced by this retry. It only closes the R2A.2 persistence/delivery boundary.

The prior INV-010 substantive result remains the pilot result: documented intervention is much easier to establish than counterfactual change of winner; I6/I7 remain the material unresolved causal boundary.

## Forensic checks

- narrative SHA before/after retry: `0d8bb3d8160439f9b4218cd10312d6e8351f9160a8d944155b96357a8f7f48ee` — identical;
- semantic registries before/after retry: identical;
- investigation SHA-256: `b255454d184dbdad3e4e9417848c9c0e43cf260fffd38c15de70dcbab279bb8b`;
- snapshot SHA-256: `69a832d9377e3ce48b07cba82871b0fc28d8447baced086e15b075ddfafd334c`;
- certification SHA-256: `c314e427c3c8d8a44bf4d7ff8222c96db244d14449fdb107832a7760cd0cf111`;
- certification deliverable SHA == investigation SHA: PASS.

## Next

`INV-010 CLOSED -> INV-019 READY, not launched.`


## Pilot review decision

<!-- DERIVED_FROM: artifact=INV-010_PILOT_REVIEW.md; decision=RENARD_REQUIRED -->

```text
P0 = 0
P1 = 1
P2 = 1
PILOT = PASS_WITH_TARGETED_RENARD
RENARD = REQUIRED
RENARD_SCOPE = CHILE_1964_I6_I7_ONLY
```

Reason: the Chile 1964 margin/majority causal claim remains PARTIAL/UNRESOLVED,
depends centrally on one U.S. official provenance family, and an accessible
independent academic source provides a material domestic-rival explanation.

No global rerun. No Italy 1948 or Chile 1970 deepening.


## RENARD final delta

<!-- DERIVED_FROM: artifact=INV-010_RENARD.md; decision=CLOSED_NO_FURTHER_MATERIAL_DELTA -->

```text
Chile 1964:
I4 = VERIFIED
I5 = SUPPORTED qualitative
I6 = UNRESOLVED
I7 = NOT_ESTABLISHED

RENARD = CLOSED_NO_FURTHER_MATERIAL_DELTA
INV-010 = CLOSED
```

Material change: the prior positive formulation that U.S. covert support
affected Frei's margin/majority is narrowed. A contribution is plausible, but
no independent evidence consulted isolates its marginal electoral effect.

No Truth Engine FINAL content was rewritten; this is a post-TE sidecar delta.
