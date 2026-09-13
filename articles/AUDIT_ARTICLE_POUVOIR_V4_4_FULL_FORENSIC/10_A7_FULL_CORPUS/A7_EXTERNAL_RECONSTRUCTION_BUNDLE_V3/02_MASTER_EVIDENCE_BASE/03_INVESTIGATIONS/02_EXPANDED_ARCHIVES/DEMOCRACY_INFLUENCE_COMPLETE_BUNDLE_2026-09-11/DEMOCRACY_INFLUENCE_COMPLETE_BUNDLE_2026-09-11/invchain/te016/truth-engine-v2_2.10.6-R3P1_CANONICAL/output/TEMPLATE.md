# OUTPUT TEMPLATE v2.10.6 R3 — Technical forensic investigation

`output/TEMPLATE.md` owns only the FINAL investigation projection contract. It does not own investigation semantics, source epistemics, cluster methods, paths, state mutation or gate logic.

Authorities:

```text
KERNEL.md                  orchestration and phase order
protocol/INVESTIGATION.md  semantic investigation contracts
definitions/*.md           symbol/pattern/threat routing
search/EPISTEMIC.md        EDI/source epistemics
clusters/*.md              domain-specific methods/output contracts
run_state.py               deterministic state + paths + rendering
verify.py                  independent deterministic certification
TEMPLATE.md                technical body/projection requirements only
```

## §0 Purpose

`*_INVESTIGATION.md` is the canonical FINAL forensic snapshot used to:

```text
VERIFY | UPDATE | EXTEND | AGGREGATE | HANDOFF_TO_ARTICLE_PROTOCOL
```

It is not an article and not a reader-oriented report.

```text
NO_MATERIAL_SEMANTIC_LOSS
NO_EDITORIAL_SELECTION
NO_NARRATIVE_AS_SOLE_STATE
```

All material facts, claims, axes, evidence, causal links, contradictions, module outputs, gaps and statuses must already exist in RUN_STATE before SAVE.

## §1 Technical body (`_NARRATIVE.tmp.md` physical path retained)

The historical filename and `NARRATIVE_START/END` markers remain for ABI stability. The content is now a **technical analytical body**.

MUST:

- explain material analytical results using stable `LED/CLM/AXS/FCT/SRC/CAU/CTRL/ACT` IDs;
- distinguish observation, evidence, inference, hypothesis, causal right, counter-evidence and gap;
- preserve uncertainty and negative results;
- remain bounded and technical;
- contain no volatile QRY IDs.

MUST NOT:

- contain JSON state dumps;
- duplicate runtime-owned registry headings;
- duplicate `FORENSIC_SECTIONS_V1`, `TRACE_MATRIX_V1`, `STATUS_DELTA_V1` or `OPEN_GAPS_V1`;
- introduce a material fact/status/gap/result absent from RUN_STATE;
- optimize for article angle, hook, prose or human reading comfort.

The technical body may be short because canonical state is rendered deterministically after it.

## §2 Deterministic projection order

`run_state.py render` owns the exact composition:

```text
FINAL RUN_MANIFEST
NARRATIVE_START
  frozen technical analytical body
NARRATIVE_END
FORENSIC_CONTRACT_V1
FORENSIC_SECTIONS_V1
TRACE_MATRIX_V1
STATUS_DELTA_V1
OPEN_GAPS_V1
SEMANTIC_COUNTS_V1
SEMANTIC_REGISTRIES_V1
SEARCH_ACTIVITY_V1
SECTION_STATUS_V1
REQUEST_LOG
EVIDENCE_REGISTRY
FACT_REGISTRY_V1
FCT_SOURCE_MAP_V1
REFUTATION_REGISTRY_V1
WRITEBACK_PLAN_V1
MEMORY_WRITE_MODE_V1
CHECKPOINT_LOG_V1
WRITEBACK_ATTEMPT_LOG_V1
PERSISTENCE_META
WRITEBACK_EXECUTION_V1 (delivery)
```

The LLM never hand-formats these runtime-owned blocks.

## §3 Forensic report sections

Every non-derived canonical section is projected by `run_state.py` under `FORENSIC_SECTIONS_V1` as deterministic Markdown, not JSON.

Examples of state that must survive when applicable:

```text
TEMPORAL_STATE
MANIPULATION_REPORT
MODULE_EXECUTION
SCOPING_REPORT
CREDO
COGNITIVE_MAP
DIALECTICAL_MAP
RESOURCE_FLOW_MAP
ACTOR_NETWORK_MAP
IMPACT_MAP
CONTRADICTION_LEDGER
VERIFICATION_REPORT
EDI_REPORT
RESPONSIBILITY_MAP
NEXT_QUERIES
```

`SET` must render non-empty content. `EMPTY` renders `NONE`. `DERIVED` objects are rendered only from runtime-owned state and are never maintained as a second mutable copy.

## §4 Source provenance

The canonical `EVIDENCE_REGISTRY` row is runtime-owned and preserves, for each SRC:

```text
SRC-ID | role | fam | CANONICAL_ID | TITLE | PUBLICATION_DATE | CHECKED_AT | LOCATOR | URL/INPUT_REF
```

A source record missing any of these fields cannot reach certified FINAL. Explicit `UNKNOWN`/`N/A(reason)` may be used only when truthful under the owning source contract; omission is not allowed.

## §5 Semantic completeness

Runtime/verifier enforce the owner contracts from `protocol/INVESTIGATION.md`.

Critical terminal invariants include:

```text
SATURATED LED/AXS -> ATTEMPT_IDS != [] AND RESULT_IDS != []
GAP LED/AXS       -> ATTEMPT_IDS != [] AND typed GAP
terminal CLM      -> CLAIM + CLAIMANT + MATERIALITY + SUPPORT + COUNTER/NONE_FOUND + GAP_TYPE + GAP + STATUS
unresolved CAU    -> typed GAP
```

No prose or section status may substitute for these fields.

## §6 Module execution provenance

`MODULE_EXECUTION` is a generic envelope only. Each conditionally loaded/materially executed module records:

```text
MODULE
TRIGGER
REASON
INPUT_IDS
OPERATIONS_APPLIED
RESULT_IDS
NEGATIVE_RESULTS
NOT_COMPUTABLE
GAPS
STATUS
```

The module itself remains owner of its domain-specific output contract. TEMPLATE never duplicates it.

## §7 EDI

`EDI_REPORT` follows the structured FINAL state contract owned by `search/EPISTEMIC.md`. EDI is a corpus diagnostic, never a truth score. Hand-counted prose summaries are not authoritative.

## §8 Trace / continuation

Runtime derives and renders:

```text
TRACE_MATRIX_V1   material LED/AXS/CLM -> attempts -> results/support/counter -> final status/gap
STATUS_DELTA_V1   observed status/EPI/tier changes with reason
OPEN_GAPS_V1      typed unresolved semantic gaps
```

These views are derived; canonical objects remain authoritative.

## §9 Article Protocol boundary

Truth Engine preserves complete investigation state. Article Protocol later owns cross-investigation deduplication, selection, synthesis, editorial relevance, angle, structure and prose.

Truth Engine must not pre-compress material state for future article writing.

## §10 Filename / topology

Paths and filenames are owned exclusively by `run_state.py paths`. This template creates no new file and no alternate path generator.

The existing co-located six-file run topology remains unchanged.

_Canonical authority: FINAL technical projection contract only._
