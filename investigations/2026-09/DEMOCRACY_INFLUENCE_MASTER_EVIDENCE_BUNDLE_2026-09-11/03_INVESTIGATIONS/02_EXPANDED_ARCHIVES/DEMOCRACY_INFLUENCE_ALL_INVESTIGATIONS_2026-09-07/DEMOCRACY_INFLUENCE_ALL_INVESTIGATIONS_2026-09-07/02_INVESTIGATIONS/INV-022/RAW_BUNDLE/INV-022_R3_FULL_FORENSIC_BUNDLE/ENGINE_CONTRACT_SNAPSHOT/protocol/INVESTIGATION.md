# INVESTIGATION v2.10.6 R3 — Lossless forensic investigation pipeline

Loaded at KERNEL step 8b. KERNEL owns order/load/save and cross-domain predicates; this file owns cognitive,
dialectical, factual, causal, verification and responsibility operations.

## §0 Data contracts

```text
RUN_MANIFEST:
  ENGINE_VERSION | STATE:{OPEN→FINAL@18b} | RUN_ID | PARENT_RUN_ID | AS_OF | INPUT_KIND | MISSION_MODE | INPUT_REF
  SUBJECT_SLUG | INVESTIGATION_PATH | SCOPE | COMPLEXITY
  CHECKPOINT_SEQ | LAST_COMPLETED | NEXT_ACTION | RESUME_COUNT
  ROUTE_OVERRIDES | LOADED_MODULES | DEGRADED_FLAGS

SCOPING_REPORT:
  LEAD_QUESTION | OBJECT_QUESTION | PERIOD | GEO | DOMAINS | ACTORS/INSTITUTIONS
  EXCLUSIONS | EVIDENCE_LIMITS | OBJECT_COVERAGE

LEAD_REGISTRY:
  ID | SOURCE_ID | LOCATOR | LEAD | EVIDENCE_EXCERPT | KIND | MATERIALITY | ROUTES | LINKED_IDS | ATTEMPT_IDS | RESULT_IDS | STATUS/GAP
  ID=LED-001... | KIND=CLAIM|EVENT|ENTITY|OBJECT|RELATION|MECHANISM|CONTEXT
  ROUTES=[AUDIT|EXPAND|LINK|CONTEXT] or [EXCLUDE(reason)]; EXCLUDE is exclusive
  STATUS=OPEN|ACTIVE|SATURATED|GAP|EXCLUDED

INVESTIGATION_MAP:
  AXS-ID | AXIS | QUESTION | SOUGHT_OBJECTS | LED/CLM LINKS | ATTEMPT_IDS | RESULT_IDS | STATUS/GAP
  AXS-ID=AXS-001... | STATUS=PLANNED|ACTIVE|SATURATED|GAP|N/A
  ATTEMPT_IDS=QRY/SRC IDs | RESULT_IDS=FCT/CAU/CTRL/ACT IDs
  AXIS=SOURCE_AUDIT|SCOPE_HISTORY|EVIDENCE_CASES|RESOURCES_FLOWS|MECHANISMS
       |ACTORS_RELATIONS|RULES_CONTROLS|IMPACT_RESPONSIBILITY|COUNTER_HYPOTHESES

CLAIM_REGISTRY:
  ID | CLAIM | CLAIMANT | MATERIALITY | SUPPORT | COUNTER/NONE_FOUND | GAP_TYPE | GAP | STATUS
  ID=CLM-001... | MATERIALITY=DECISIVE|IMPORTANT|CONTEXT
  no gap => GAP_TYPE=NONE and GAP=NONE; fields remain explicit

MODULE_EXECUTION:
  MODULE | TRIGGER | REASON | INPUT_IDS | OPERATIONS_APPLIED | RESULT_IDS | NEGATIVE_RESULTS | NOT_COMPUTABLE | GAPS | STATUS
  one row per conditionally loaded/materially executed module recorded in RUN_MANIFEST.LOADED_MODULES beyond ALWAYS_LOAD
  module-specific result shape remains owned by that module; this envelope records execution provenance only

EVIDENCE_REGISTRY:
  SRC-ID | CANONICAL_ID | TITLE/AUTHOR | PUBLICATION_DATE | CHECKED_AT
  LOCATOR | URL/INPUT_REF | SOURCE_ROLE:{UNASSESSED|role-by-claim} | UPSTREAM_FAMILY

COGNITIVE_MAP:
  CLUSTER_SCORES | HERMENEUTIC L1-L6 | FORENSIC(if Ξ≥5) | ALTERNATIVES | QUERY_GUIDANCE

DIALECTICAL_MAP:
  P1_DOMINANT | P2_CRITICAL | P3_EVIDENCE_ARBITRATION | TENSIONS | SILENCES | IMPACT

FACT_REGISTRY:
  | # | Fait | Date | Acteur | Chiffre | Source | URL/INPUT_REF | Fiabilité |
  # = FCT-001...; Source = SRC-ID + title/date + exact locator.
  Fiabilité = source role + exactly one fact status + corroboration, e.g. `◈ ✦ ⊕`.

RESOURCE_FLOW_MAP:
  RESOURCE:{MONEY|DATA|MATERIAL|AUTHORITY|ACCESS|OTHER} | SOURCE | VEHICLE/PROCESS
  INTERMEDIARY | RECIPIENT/BENEFICIARY | AMOUNT/VOLUME/UNIT/PERIOD
  DECISION/RULE/CONTRACT | CONTROL | FCT/SRC-IDs | STATUS/GAP

ACTOR_NETWORK_MAP:
  FROM | EDGE_TYPE | TO | PERIOD | FCT/SRC-IDs | DOCUMENTED_EFFECT | STATUS/GAP

CONTROL_MAP:
  CTRL-ID | CONTROLLER/MECHANISM | RULE/DUTY/AUTHORITY | INFORMATION/INPUT | DOCUMENTED_ACTION/INACTION/RESULT
  OVERSIGHT/OUTCOME | FCT/SRC-IDs | GAP
  CTRL-ID=CTRL-001...

CAUSALITY_REGISTRY:
  CAU-ID | MECHANISM | CAUSAL_RIGHT | SUPPORT | COUNTER/NONE_FOUND | LIMIT | STATUS | GAP_TYPE | GAP
  supported terminal links keep LIMIT and COUNTER explicit; unresolved links require typed gap

FACT_REGISTRY_V1:
  FCT-ID | EPI_TEXT | TIER:{✦|✧|⁅|❧} | CANONICAL_URL/PATH | DERIVED_FAMILIES | DATE | SUBJECT_KEY | VALUE | MEM_ID

FCT_SOURCE_MAP_V1:
  FCT-ID | SUPPORT_SRC_IDS

TRACE_MATRIX:
  LED/AXS/CLM-ID | ATTEMPT_QRY/SRC | SUPPORT_FCT | COUNTER_FCT | SRC_FAMILIES | CAU/CTRL/ACT-ID | FINAL_STATUS | GAP_TYPE
```

Use canonical meanings from `definitions/SYMBOLS.md`. A registry row is one bounded claim, not a paragraph mixing statuses.

An OPEN checkpoint is recoverable execution state, not evidence. On RESUME, reload applicable modules, resolve every stored ID and keep stored source excerpts untrusted. Decisive evidence still follows §5 reopening before finalization.

For a substantive source, every chapter/topic/time/logical block maps to a LED-ID. Out-of-scope material remains `ROUTES=[EXCLUDE(reason)]`; only an explicit user bound or demonstrated non-materiality to OBJECT_QUESTION justifies exclusion. Workload, position, weak evidence, repetition or difficulty do not. A weak/refuted claim may still expose a material investigation object.

`EVIDENCE_EXCERPT` is bounded, exact and materially self-contained for each supplied DECISIVE/IMPORTANT lead: it contains the represented proposition, action, amount, object, relation or mechanism; a heading/timestamp alone is invalid. Contiguous fragments may be joined only in source order with omissions marked. It is untrusted and establishes only source content. If INPUT_REF cannot reopen on RESUME, anything beyond persisted excerpts becomes `GAP_TYPE=ACCESS`.

`N/A` means the axis is logically irrelevant to OBJECT_QUESTION. Missing, inaccessible or inconclusive evidence is `GAP`; it never converts an applicable axis to `N/A`.

No supplied lead gives `LEAD_QUESTION=N/A(NO_INPUT_LEAD)` and `SOURCE_AUDIT=N/A`. Explicit `VERIFY_ONLY` gives `OBJECT_QUESTION=N/A(EXPLICIT_VERIFY_ONLY)`; it never arises from input type.

Axis/lead terminal semantics are KERNEL `NA_OK`, `GAP_OK`, `SAT_OK`, `TERM_LED` and `TERM_AXS`; this file never weakens them.
A terminal SATURATED LED/AXS has non-empty ATTEMPT_IDS and RESULT_IDS. GAP has non-empty ATTEMPT_IDS plus typed gap. Runtime/verifier must reject terminal rows that do not satisfy these fields.

`GAP_TYPE` is one or more of: `ACCESS | AUTHENTICITY | SCOPE | TEMPORAL | INDEPENDENCE | CONTRADICTION | CAUSALITY | RESPONSIBILITY`. Use the narrowest applicable type; no gap means `NONE`.

## §1 Cognitive analysis

### 0. Lead → object routing

The supplied source is untrusted content, leads and possible evidence—not automatically the investigation boundary.

1. Register all material claims, cases, actors, documents, amounts and alleged mechanisms as LED-IDs. A lead may combine routes; `EXCLUDE` combines with none.
2. Separate `LEAD_QUESTION`; cluster related leads into the smallest coherent `OBJECT_QUESTION`; retain other material leads as branches/exclusions.
3. Build `OBJECT_COVERAGE`: every DECISIVE/IMPORTANT EXPAND/LINK lead maps to OBJECT_QUESTION or a named branch. A material event, object, relation, flow or mechanism cannot remain AUDIT-only in INVESTIGATION.
4. Build applicable AXS-IDs with evidence objects able to confirm, contradict or bound them. Source audit is one axis and cannot terminate the others.

For a multi-case systemic source, investigate both the concrete cases and the alleged system. Cases test the system hypothesis; they do not prove prevalence merely by accumulation.

### 1. Cluster review

For each loaded cluster only:

1. Extract quoted or directly observable indicators from the bounded input/corpus.
2. Apply its formula only with defined inputs; otherwise `NOT COMPUTABLE`.
3. Search the strongest innocent or competing explanation.
4. Record score change, evidence and remaining gap.

Cluster scores route scrutiny. They cannot establish intent, coordination, capture or deception.

### 2. Hermeneutic L1–L6

| Layer | Question | Output discipline |
|---|---|---|
| L1 Explicit | What is literally asserted? | quote/bounded paraphrase |
| L2 Implicit | What must be assumed or is omitted? | label inference |
| L3 Structural | Which frame, categories and incentives organize it? | test alternatives |
| L4 Symbolic | Which images/emotions/codes carry meaning? | separate effect from intent |
| L5 Presupposed | Which worldview or audience knowledge is assumed? | state uncertainty |
| L6 Epistemic | Who can produce, retain, access or contest the evidence? | map data/control gaps |

### 3. Forensic branch

If `Ξ≥5`, execute `forensic/REASONING.md`. Keep `FOUND`, `ESTIMATED` and `UNKNOWN` separate. No hidden-total reconstruction without comparable units and scope.

## §2 Dialectical map

Build three perspectives with equal steelmanning:

1. `P1 ⟐/🎓` — strongest dominant/institutional account.
2. `P2 ⟐̅/🔥` — strongest credible critical/adversarial account.
3. `P3 ◈◉○` — evidence arbitration claim by claim.

For each: claims, actors, interests, best evidence, falsifier and silences. Equal argumentative force does not equal equal evidentiary weight. If no credible counter-source is found, write `NONE_FOUND` and preserve the strongest counter-argument; never invent a source or false balance.

```text
SCENARIO_A | SCENARIO_B | CONVERGENCES | DIVERGENCES | UNRESOLVED | SHARED_SILENCES
ARBITRATION: CLM-ID → support → counter → status → next check
```

## §3 Search and factual construction

### Search transformation

- Preserve each KERNEL `QRY-ID`; convert every material LED/CLM gap, AXS question and CRÉDO entry into the shortest query that can locate the named evidence object.
- Run `LEAD_AUDIT` and `OBJECT_INVESTIGATION` as distinct routes. A query/result may serve both, but completion of one cannot be inferred from the other.
- For every applicable AXS-ID, record QRY/SRC `ATTEMPT_IDS`; seek a direct/closest object or retain an auditable typed GAP. This requires exploration, not a finding.
- Search original language/name variants, primary repositories and credible counterevidence.
- Open the exact document/page; a result snippet is not evidence.
- Track upstream provenance. Syndicated copies or analyses using one object are one evidence family.
- Use query budgets as targets; stop on saturation, not on a cosmetically complete count.

### Evidence anchors

Assign `SRC-001...` once per accepted evidence object. Prefer a stable canonical identifier appropriate to the domain: DOI, ECLI, CELEX, docket/case number, official report or filing identifier, SIREN/SIRET, dataset/version or archive identifier. Otherwise use validated INPUT_REF for supplied content, then the normalized specific URL.

Every material use records an exact locator: page, paragraph, article/section, table/cell, timestamp, record key or quoted field. A homepage, search page, generic repository root or inaccessible object is not an anchor.

### FACT_REGISTRY

For every material result:

1. State one falsifiable fact with bounded scope.
2. Extract what/who/when/where/how much.
3. Assign source role `◈◉○` claim-relatively for each evidence object.
4. Assign `EPI` as text: `FACT|EVIDENCE|INFERENCE|HYPOTHESIS|SPECULATION|UNKNOWN`.
5. Assign `TIER` only from `{✦,✧,⁅,❧}` under `protocol/FACT_VERIFICATION.md`; **EPI != TIER**. Narrative glyphs `⁕⁂⊗⊙` never enter the tier column.
6. Record `SRC-ID`, exact locator, specific URL/validated INPUT_REF; emit `FCT_SOURCE_MAP_V1` with support-only SRC IDs and derive provenance families from those SRC rows.
7. Preserve contradiction as a separate row or linked note; never average incompatible claims. Persisted exact excerpt is sufficient only for “supplied content states X”.

```text
KNOWN       = EPI=FACT + tier ✦ within stated scope
PROBABLE    = EPI=FACT + tier ✧
CLAIMED     = EPI=UNKNOWN with narrative status ⁕
HYPOTHESES  = EPI=HYPOTHESIS with narrative status ⁂
CONTESTED   = claim-level status ⊗/⊙ in CLAIM/STATUS views, not FACT tier
UNKNOWN     = tier ⁅
REFUTED     = tier ❧
```

Confirmed-fact targets guide effort only. Fewer facts with honest limitations beat upgraded weak evidence.

### Silent evidence — conditional

Use only when the claim predicts a record or trace that should normally exist. Absence is informative only if the expected object, retention/publication duty, repositories and access completeness are known.

```text
SILENT_EVIDENCE:
EXPECTED_OBJECT | WHY_EXPECTED | REPOSITORIES_CHECKED | ACCESS_COMPLETENESS | RESULT | LIMIT
```

`NOT_FOUND` means only “not found within the searched perimeter”. It never by itself proves intent, guilt, non-occurrence or concealment. Unknown access completeness → `⁅` with `GAP_TYPE=ACCESS`.

### Time × domain view — conditional

For multi-period and multi-domain COMPLEX/APEX cases, derive a compact matrix from existing FCT IDs:

```text
PERIOD × DOMAIN → FCT-IDs | change/continuity | gap
```

This is a view, not a new registry, score or evidence status. Skip it when chronology or DOMAINES already communicates the relationship.

### Object maps — when applicable

**Resources/flows.** Identify the resource and unit before tracing it: money, data, material, authority and access are distinct. For money, direct diversion, overcharge, transfer, private benefit, public loss, opportunity cost and modeled macroeconomic loss remain distinct units. Use the closest inspectable records and populate `RESOURCE_FLOW_MAP`; an incomplete applicable chain ends in `GAP`, not `NOT APPLICABLE`.

**Actors/networks.** Build only sourced, typed and dated edges from registers, filings, minutes, contracts, declarations or direct statements. Co-occurrence is a lead. Populate `ACTOR_NETWORK_MAP`; do not infer influence or coordination from proximity.

**Controls/response.** Identify the applicable legal, organizational, scientific or technical rule/control; who or what had authority/capacity/input; then record action, inaction, test result, oversight and outcome. Populate `CONTROL_MAP`. Control failure does not by itself establish an individual offence or intent.

## §4 PELOTE — causal tracing

Run when KERNEL sets `CAUSAL_ROUTE=REQUIRED`, or when OPTIONAL and an explanatory chain materially affects the conclusion. REQUIRED mandates cause/mechanism research, not a successful chain. If no link survives evidence checks, return `NO VERIFIED CAUSAL CHAIN` plus `GAP_TYPE=CAUSALITY`.

Trace OBJECT_QUESTION. The genealogy of a statistic, post or narrative belongs to `SOURCE_AUDIT` and cannot replace the object’s causal/mechanism route unless provenance is itself the explicit object.

### A. Discover candidate mechanisms

Research before naming causes. Adapt these families to the event’s language:

```text
{event} causes/origins/historical roots
{event} institutional or systemic failure
{event} competing explanations
{event} enabling law/institution/material condition
{event} contemporaneous inquiry/commission/archive
```

Fetch the strongest sources and extract candidate mechanisms with provenance. Merge candidates only when they share the same evidenced trajectory.

### B. Trace each mechanism backward

Start at the nearest evidenced law, decision, institution, material condition or event. At each step:

1. Hypothesize the immediately prior enabler.
2. Search/fetch a specific source; reformulate once if noisy.
3. Classify the link: `CAUSE`, `ENABLER`, `PRECEDENT`, `CONTEXT` or `UNKNOWN`.
4. Record source, competing explanation and status.
5. Stop at a meaningful root, max depth 6 or exhausted evidence. Never insert a node to meet depth.

```text
| ID | FROM | LINK_TYPE | MECHANISM | TO | SUPPORT | COUNTER | LIMIT | STATUS | GAP_TYPE/GAP |
ID = CAU-001...
```

`CAUSE` requires evidence that the mechanism produced the outcome. `ENABLER` made it materially possible/easier without determining it. `PRECEDENT` and `CONTEXT` remain descriptive.

### C. Weave and coverage

- Merge trees only on the same evidenced ancestor; otherwise state independence.
- For each relevant FACT_REGISTRY row, cite the existing node that explains it or `UNEXPLAINED`.
- At most two focused attempts may fill an important unexplained link; then retain `⁅` and `GAP_TYPE=CAUSALITY`.
- Descriptive facts survive a causal gap. The causal conclusion does not.

Output `TIMELINE`, typed `PELOTE_TREES`, `COVERAGE N/N`, competing explanations and gaps. A short verified chain is valid.

## §5 Verification and trace

For every decisive `✦/✧/⊗/⊙`:

1. Reopen the exact source and locator; verify it contains the claimed material.
2. Check date/version, definition, population, jurisdiction and units.
3. Separate source authenticity from the truth of its assertions.
4. Test independence and upstream circularity.
5. Seek the strongest credible disconfirming object or record `NONE_FOUND`.
6. Upgrade/downgrade only through SYMBOLS.md; reasoning coherence cannot upgrade status.

Domain prompts: legal—operative text/jurisdiction; financial—filing/beneficial ownership/accounting period; scientific—design/data/uncertainty/replication; conflict—time/location/provenance/access; humanitarian—definitions/coverage/local testimony; technical—version/configuration/reproduction conditions.

Do not label `COVER-UP` from discrepancy alone. Record the observable event: non-disclosure, deletion, inconsistency, access refusal or verified concealment, with status.

```text
STATUS_DELTA:
FCT/CLM-ID | BEFORE | AFTER | REASON | SRC-ID

CONTRADICTION_LEDGER:
CON-ID | CLM/FCT-IDs | conflicting propositions | SRC-IDs | resolution/status | remaining check

VERIFICATION_REPORT:
REOPENED_IDS:{ids} | UPGRADED_IDS:{ids} | DOWNGRADED_IDS:{ids} | CONTRADICTION_IDS:{ids}
CIRCULAR_FAMILIES:{families} | NONE_FOUND_CLAIMS:{ids} | REMAINING_GAPS:{ids/descriptions}
Counts displayed later are runtime-derived from these collections; never hand-count them in the report state.
```

Build TRACE_MATRIX after these updates. Every material LED-ID, applicable AXS-ID and material CLM-ID must resolve through actual attempt/result IDs or an explicit auditable GAP_TYPE; unused contextual evidence need not be forced into it.

## §6 Impact and responsibility (`WOLVES`)

Impact map: `BENEFITS | COSTS/HARMS | AFFECTED | RESPONSE/CHANGE` for OBJECT_QUESTION; identify persons, groups, systems or objects as applicable. Source/message effects may be a separate branch but cannot substitute for object effects. For each, identify metric/baseline/period/source when meaningful. Use `NONE ESTABLISHED` only after bounded applicable research and `NOT APPLICABLE` only for logical irrelevance.

Responsibility includes a person only when a source connects them to a relevant signature, command, vote, decision, implementation, ownership, documented benefit or public claim.

Before naming persons, use `CONTROL_MAP` to separate applicable rule/duty, available input/information, authority, action/inaction/result and oversight outcome. A failed control can be established while individual intent/responsibility remains unknown.

```text
| ID | NAME | ROLE | DOCUMENTED_ACTION | SOURCE | INTENT | RESPONSIBILITY_SCOPE |
ID = ACT-001... | INTENT = PROVEN | CLAIMED | UNKNOWN
```

No individual minimum. Do not infer intent from benefit, responsibility from title, guilt from association, or coordination from network proximity.

## §7 Output handoff

KERNEL loads `forensic/REQUEST_LOG.md` at step 0. Step 14 applies `output/TEMPLATE.md`. `_INVESTIGATION.md` is a technical forensic snapshot, not an editorial report. Every material result must already exist in RUN_STATE under its owning contract before phase 19; the technical Markdown body may explain stable IDs but is never the sole owner of a fact, status, gap, contradiction, module result or causal conclusion.

`run_state.py render` deterministically projects structured report sections, TRACE/STATUS/GAP views, semantic registries and machine bookkeeping. It must not invent missing state. Article selection/narrative belongs downstream to Article Protocol.

French technical output; bounded propositions; stable IDs adjacent; hypotheses, contradictions, negative results and unknowns visible.

_Canonical authority: investigation operations and intermediate data contracts._
