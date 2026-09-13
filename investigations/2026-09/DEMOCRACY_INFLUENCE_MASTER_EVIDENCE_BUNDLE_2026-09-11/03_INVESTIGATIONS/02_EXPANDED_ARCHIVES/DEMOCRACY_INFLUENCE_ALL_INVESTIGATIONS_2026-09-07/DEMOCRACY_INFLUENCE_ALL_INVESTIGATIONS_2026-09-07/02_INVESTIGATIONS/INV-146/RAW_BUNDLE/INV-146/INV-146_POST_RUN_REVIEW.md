---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_synthesis_review"
artifact_id: "INV-146-POST-SYNTHESIS-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-146"
---

<!-- DERIVED_FROM: INV-146_SYNTHESIS_CARD.md + INV-146_SYNTHESIS_INPUT_GATE.md + INV-146_SYNTHESIS.md -->
<!-- DECISION: P0=0; P1=0; P2=4; RENARD=NO; close_INV-146=true -->

# POST-SYNTHESIS REVIEW — INV-146

## Verdict

```text
EXECUTION_PATH = SYNTHESIS / NO_TRUTH_ENGINE_RUN_BY_DESIGN
CONTROL_VALIDATE = PASS
SYNTHESIS_CARD_POSITIVE = PASS
SYNTHESIS_CARD_NEGATIVE_PRIMARY = PASS
SYNTHESIS_CARD_NEGATIVE_OPEN_DEP = PASS
RUN_CARD_REJECTS_SYNTHESIS = PASS
DEPENDENCIES_REPRESENTED = 10/10
INPUT_GATE = PASS_WITH_RECOVERY
STATIC_SYNTHESIS_AUDIT = PASS
P0 = 0
P1 = 0
P2 = 4
RENARD = NO
INV_STATUS = CLOSED_AUTHORIZED
```

## Contradictory review

### 1. Does the synthesis prove a general ally/adversary double standard?

**No.** The deliverable explicitly rejects that overclaim. It separates legal-design asymmetry from evidentiary threshold, vocabulary and enforcement, and leaves the latter three non-established.

### 2. Is the positive asymmetry claim actually supported?

**Yes, bounded to legal design.** INV-145 establishes real differences in scope among FARA, the French regime and the European framework, including a geographic EU/non-EU distinction in the French design examined. The synthesis does not convert this into selective enforcement.

### 3. Are non-isomorphic mechanisms falsely compared?

**No material conflation found.** Open democracy promotion/observation/aid is separated from covert/deceptive operations. Funding is separated from earmarking and tasking. State relation is separated from private operator/client relation. Operation is separated from effect.

### 4. Is the ally-side evidence artificially weakened or strengthened?

**No material defect found.** INV-026 preserves unknown sponsor/tasking edges; INV-033 preserves downstream knowledge/effect gaps; INV-138 preserves affiliation/tasking uncertainty; INV-139 recovery is explicitly bounded. The synthesis also notes that UAE/Alp provides a strong covert partner-state control without converting it into universal state control or electoral effect.

### 5. Is the adversary-side evidence over-promoted?

**No.** INV-022 remains strong on operation/infrastructure and bounded tasking, but I5-I7 are not promoted. INV-134’s edge-by-edge attribution model is retained.

### 6. Are vocabulary and enforcement conclusions supported by a denominator?

**No denominator exists, and the synthesis says so.** Those hypotheses remain NOT_ESTABLISHED and become explicit P2 residuals rather than conclusions.

### 7. Does the domestic branch meet the canonical question?

**Only partially.** Purely domestic isomorphic controls are insufficiently represented. This is a material coverage limitation, but it is disclosed and does not invalidate the ally/adversary result. Classified P2 rather than silently filled.

### 8. Recovery risk

INV-139 and INV-140 original terminal Library artifacts are incomplete/missing. The recovery handoffs do not recreate absent runtime IDs or original bytes. This lowers provenance completeness but not enough to alter the bounded synthesis verdict, because claims requiring missing detail were excluded. Classified P2.

## P2 residuals

1. systematic matched vocabulary dataset;
2. enforcement denominators across comparable regimes/camps;
3. pure domestic isomorphic comparator;
4. original terminal Library persistence for INV-139/140.

## RENARD

`NO`.

The remaining gaps require dedicated comparative datasets, mature enforcement history, or recovery of original persisted bytes. Generic searching would not close them cleanly.

## Closure decision

`INV-146` may close as a completed comparative synthesis. Its bounded findings should feed `INV-133`; `INV-133` remains blocked on its other direct dependencies.
