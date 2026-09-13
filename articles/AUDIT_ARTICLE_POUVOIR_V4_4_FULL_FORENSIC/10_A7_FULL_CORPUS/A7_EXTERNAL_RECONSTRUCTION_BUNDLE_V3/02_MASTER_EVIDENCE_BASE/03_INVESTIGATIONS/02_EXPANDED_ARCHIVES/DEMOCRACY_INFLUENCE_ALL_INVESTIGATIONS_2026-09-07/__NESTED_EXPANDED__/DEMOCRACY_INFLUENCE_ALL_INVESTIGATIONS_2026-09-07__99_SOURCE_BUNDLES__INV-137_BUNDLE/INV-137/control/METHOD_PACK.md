---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "method_contract"
artifact_id: "METHOD_PACK"
version: "1.0-kiss"
status: "active"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
---

<!-- TRACE: refactor=KISS; derived_from=METHOD_PACK_v0.5; full_history=history/PRE_REFACTOR_HISTORY.zip -->
<!-- TRACE: runtime_baseline_rebound=Truth_Engine_2.10.6_R3P1; method_semantics_unchanged=true -->

# METHOD_PACK — Influence / ingérence / pouvoir démocratique

`SEM := project-specific overlay around Truth Engine ; do not duplicate Truth Engine.`

## 1. Autorité

```text
1 actual capabilities
2 Truth Engine 2.10.6 / R3P1
3 METHOD_PACK
4 current RUN_CARD
5 prior corpus as leads, never truth-by-status
```

Locked baselines:

```text
TRUTH_ENGINE_BUNDLE_SHA256 = d113e3bd1848805bc3dbf1485eb1107a5767ebe74efd0cf27b601e01db278d30
TRUTH_ENGINE_KERNEL_SHA256 = 0d78b5d2db873d6bb9984867c3a4b1095b46400db2145487a763680b43e88974
CORPUS_BASELINE = SUBSTACK_BASELINE_2026-08-26_v0.4
CORPUS_BASELINE_SHA256 = 6774944e80f3c150e6d3506c4356e5ecb51243eb0ce8d4b99b207c3b69752052
```

Truth Engine owns facts, provenance, QRY/SRC/FCT/CAU/ACT, G0-G10,
persistence, serialization and FINAL. This pack MUST NOT duplicate them.

## 2. Run contract

Runnable iff registry says:

```text
status = READY
type = PRIMARY|CASE
object_question != empty
scope != empty
```

Objective: reduce uncertainty on actors, mechanisms, flows, chronology,
conditions, rival explanations and effects. Do not write the final article.
Do not defend a predetermined global thesis.

`control.py run-card INV-XXX` enforces this gate.

## 3. Corpus inheritance

`CORPUS != TRUTH`.

Prior articles may provide `CONTEXT | LEAD | SOURCE_LEAD | CONTRADICTION_LEAD | GAP_LEAD`.

- coverage = prior treatment, not correctness;
- reuse questions/IDs/source leads, not conclusions by status;
- recheck material, evolving, disputed or decisive sources;
- repeated articles from one provenance are not independent corroboration;
- do not rediscover stable context without model-changing value.

## 4. Influence model

Do not use a false ladder `influence -> propaganda -> corruption -> interference`.
For central mechanisms only, classify applicable dimensions:

```text
ORIGIN     DOMESTIC|FOREIGN|TRANSNATIONAL|MIXED|UNKNOWN
VISIBILITY OPEN|PARTIAL|OPAQUE|DECEPTIVE|UNKNOWN
LEGALITY   LEGAL|REGULATED|DISPUTED|ILLEGAL|UNKNOWN   # jurisdiction + date
METHOD     FUNDING|LOBBYING|PR|PROPAGANDA|DATA|TARGETING|AMPLIFICATION|
           MODERATION|ASTROTURFING|CLANDESTINE_ACTION|COERCION|CORRUPTION|OTHER
RELATION   INDEPENDENT|ALIGNED|COOPERATING|COORDINATED|TASKED_COMMANDED|UNKNOWN
TARGET     ELECTORATE|CANDIDATE|PARTY|MEDIA|PLATFORM|ADMINISTRATION|
           LEGISLATOR|REGULATOR|COURT|POLICY|MARKET|CIVIL_SOCIETY|OTHER
```

Strong labels require their own evidence. Origin, opacity, funding or proximity
alone do not establish manipulation, capture, corruption, interference or command.

## 5. Influence evidence chain

```text
I0 IDENTITY / RELATION
I1 RESOURCES / CAPABILITY / ACCESS
I2 DOCUMENTED ACTION
I3 COORDINATION / TASKING / CONTROL
I4 EXPOSURE / REACH
I5 RECEPTION / PERSUASION
I6 BEHAVIOR / INSTITUTIONAL / ELECTORAL CHANGE
I7 COUNTERFACTUAL OUTCOME
```

Never promote automatically:

```text
RELATION != COORDINATION
SHARED_FUNDER != SHARED_COMMAND
CONVERGENCE != CENTRAL_CONTROL
OPACITY != WRONGDOING
BENEFICIARY != AUTHOR
CAPABILITY != USE != EFFECT
EVENT != RESPONSIBILITY != INTENT
OPERATION_EXISTS != RESULT_CHANGED
```

Keep distributed rivals alive when plausible: incentives, selection, homophily,
professional norms, dependencies, market structure, path dependence, domestic agency.

## 6. Systemic objects / connections

When material:

```text
components -> authority -> resources/flows -> intermediaries/bridges
-> implementation -> observed use -> oversight -> measured effects
```

A connection remains candidate until identity, chronology, documented relation,
provenance independence, baseline/commonness and relevance are established.
Graph density is not causality. Global models belong to synthesis runs.

## 7. MnemoLite degraded mode

MnemoLite exists only in the user's local environment.

```text
Mnemo available
-> normal persistence + real memory IDs

Mnemo unavailable
AND prior Mnemo state is not materially required
-> degraded MNEMO_UNAVAILABLE
-> eligible FACT may end blocked=1 reason=MNEMO_UNAVAILABLE
-> no fake memory IDs
-> local snapshot may contain memory_id="-"
-> DELIVERY may PASS if terminal persistence/accounting is coherent

Mnemo unavailable
AND inaccessible prior Mnemo state is materially required
-> BLOCK
```

Never change `FACT -> EVIDENCE` to escape persistence.

Runtime invariants from INV-010:
- RUN_ID time comes from runtime/verifier clock;
- material `gap_type` requires non-empty `gap|reason|question`.

## 8. RENARD gate

RENARD is post-Truth-Engine and delta-only.

`REQUIRED` only if an accessible residual can still materially change the model:
central discriminating gap; fragile coordination/intent/causality/impact; one-family
central conclusion; material contradiction; high-value branch; decisive testable trace.
Otherwise `NO`.

If REQUIRED, use the preserved effective RENARD protocol from
`history/PRE_REFACTOR_HISTORY.zip`; never restart the whole investigation.

## 9. New-idea triage

Priority: `model_change > discrimination > dependency_unlock > coverage_gap > utility`.
Then `DO | RECHECK | MERGE | DEFER | DROP`.

Do not create a run merely because a new actor appeared. Shared vocabulary or
sources alone are not sufficient to merge two investigations.

## 10. Handoff / synthesis

RUN_HANDOFF contains only:

```text
INV_ID
TE status/path
central delta
highest supported I0..I7
material gaps/contradictions
RENARD decision + reason
new ideas triaged
registry patch
```

Reference Truth Engine IDs; do not duplicate its fact/source registries.
For syntheses, test pluralism, sector capture, transversal network, emergent
alignment, documented coordination and coherent architecture as competing/non-exclusive
models. Local coordination never proves global architecture.

## 11. Markdown traceability

Project-generated Markdown uses minimal YAML front matter plus sparse HTML comments
for `TRACE|SOURCE|DECISION|GATE|DERIVED_FROM|SUPERSEDES`. No hidden evidentiary
claims or private reasoning. Imported canonical sources are not mutated merely to add metadata.
