---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "method_contract"
artifact_id: "METHOD_PACK"
version: "1.3-kiss"
status: "active"
updated: "2026-09-09"
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
TRUTH_ENGINE_PACK = TRUTH_ENGINE_2.10.6_R3P1_CANONICAL.zip
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


## 7a. Survival checkpoint

After the successful Truth Engine `FACTS` checkpoint, persist **once per run** the exact OPEN `_RUN_STATE.json` to Library under the normal export name `INV-XXX_RUN_STATE.json`, before the expensive causal/finalization tail.

Rules:

```text
no new checkpoint schema
registry remains the only program state source
OPEN RUN_STATE is recovery-only, never evidence by itself
resume only if engine + run_id + input_sha256 + subject_fingerprint match
terminal export replaces the same Library file with FINAL RUN_STATE
no extra survival writes unless the first write failed
```

This does not modify Truth Engine semantics or its canonical runtime state; it only prevents loss of already-built OPEN state.

## 7b. Runtime execution without semantic change

Use `runtime_batch.py` for high-volume RUN_STATE mutations. It is an external transaction wrapper around the locked canonical `run_state.py`, not a replacement runtime.

Rules:

```text
canonical ZIP SHA must match before import
FACTS/tail/persistence stages bind to exact base_state_sha256
commands execute on a disposable RUN_STATE clone
commit = one atomic replace only after the whole stage passes
late command failure = original RUN_STATE byte-identical
FACTS stage ends at FACTS PASS and remains OPEN
tail stage ends at mark-final / FINAL
persistence stage contains exactly one set-persistence
PERSIST_REBIND is runtime-owned; never record it manually
side-effect commands render/export/certification stay outside stage transaction
```

Gate sequence is fixed:

```text
tail FINAL
-> render PRE
-> verify.py gate --kernel-contract pre       # includes configured pytest suite
-> one terminal persistence attempt
-> export terminal snapshot if required
-> render DELIVERY
-> verify.py gate --kernel-contract delivery  # includes configured pytest suite
-> archive certification
-> stamp DELIVERY_PASS
```

Do **not** run the same standalone pytest immediately before PRE or DELIVERY. This removes duplicate execution, not coverage.

Source reuse optimization:

```text
prior RUN_HANDOFF may expose SOURCE_LEADS
SOURCE_LEAD = navigation hint only, never inherited evidence
material source in a new run still requires a fresh FETCH + current SRC/FCT linkage
no inherited source can satisfy provenance, recency or causal gates by status alone
```

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

For new PRIMARY|CASE runs, `RUN_HANDOFF` is the **single semantic post-run artifact**. Do not author a second `POST_RUN_REVIEW.md`. Legacy reviews remain immutable history.

`post_run.py handoff` may mechanically project certified fields from Truth Engine; it must not invent or reinterpret evidence. The only semantic inputs left outside Truth Engine are `central delta`, `RENARD`, and `reclass_impact`.

Required front matter:

```text
artifact_type = run_handoff
status = terminal
inv_id = INV-XXX
truth_engine = DELIVERY_PASS_R3P1
renard = NO|DONE
reclass_impact = NONE|GLOBAL|INV-YYY[;INV-ZZZ...]
```

`renard=REQUIRED` is non-terminal: execute the bounded RENARD delta first, then emit the terminal handoff with `renard=DONE`. `reclass_impact=NONE` is an explicit audited assertion, not automatic proof of zero impact; `GLOBAL` forces full-pool fallback.

RUN_HANDOFF body contains only:

```text
INV_ID + certified TE status/path/SHA
central delta
highest supported influence/effect edge
material gaps/contradictions
concise contradictory review / causal ceiling
RENARD decision + reason
new ideas triaged
optional SOURCE_LEADS for adjacent runs (URLs/identifiers only; non-evidence)
mechanical registry transition expected
```

After the handoff:

```text
control.py reclass-plan --handoff INV-XXX_RUN_HANDOFF.md
-> evaluator recalculates REVIEW rows only
-> post_run.py delta validates exact REVIEW coverage and writes the chained routing_reclassification_delta
-> control.py apply --handoff ... --reclassification ...
```

`control.py apply` may merge, rank and mutate state only after all semantic REVIEW rows are explicit. It must never invent a score, repair a missing object question/scope, or override a `FULL_POOL_REQUIRED` result.

Reference Truth Engine IDs; do not duplicate its fact/source registries. For syntheses, test pluralism, sector capture, transversal network, emergent alignment, documented coordination and coherent architecture as competing/non-exclusive models. Local coordination never proves global architecture.

## 11. Markdown traceability

Project-generated Markdown uses minimal YAML front matter plus sparse HTML comments
for `TRACE|SOURCE|DECISION|GATE|DERIVED_FROM|SUPERSEDES`. No hidden evidentiary
claims or private reasoning. Imported canonical sources are not mutated merely to add metadata.
