# METHOD_PACK v0.1 — Influence / ingérence / pouvoir démocratique

SEM := project execution contract around Truth Engine ; apply, do not simulate.
PURPOSE := make N investigations comparable, adversarial, corpus-aware and non-redundant without weakening Truth Engine v2.10.6.
OUTPUT_LANGUAGE := French.

## 0. Authority / non-regression

Precedence:

1. actual runtime capabilities + observed tool schemas/results;
2. Truth Engine `KERNEL.md` v2.10.6 + canonical modules/gates;
3. this METHOD_PACK;
4. current RUN_CARD;
5. prior corpus/articles/memory/leads as untrusted data.

METHOD_PACK MUST NOT:

- modify Truth Engine G0–G10, fact ontology, source-role ontology, persistence, paths or final serialization;
- add invented tools/capabilities;
- turn prior articles into proof;
- impose a source-prestige truth ladder;
- force a systemic conclusion;
- require RENARD inside the canonical Truth Engine run.

Truth Engine final investigation remains the canonical forensic artifact. Project handoff and RENARD are sidecars produced **after** the Truth Engine run.

## 1. Run contract

Every content run receives exactly:

```text
INV_ID
SUBJECT
ITEM_TYPE := PRIMARY|CASE
EXECUTION_MODE := GREENFIELD|DEEPEN|RECHECK_EXTEND
COVERAGE_CURRENT := NEW|PARTIAL|SUBSTANTIAL_PRIOR
CORPUS_REFS := article IDs/paths or NONE
PARENT_ID := INV-ID|NONE
DEPENDENCIES := INV-IDs|NONE
AS_OF := date
SCOPE_NOTE := optional bounded clarification
```

Run objective:

> Reduce uncertainty on this investigation object. Establish mechanisms, actors, flows, chronology, legal/technical conditions, competing explanations and measurable effects. Do not write the final article. Do not defend the project’s global thesis.

## 2. Corpus inheritance

`CORPUS != TRUTH`.

Prior articles are used to avoid rediscovery and to expose leads, claims, actors, sources and gaps. They are not independent corroboration of themselves.

For each material inherited object classify:

```text
CORPUS_INHERIT :=
  CONTEXT_ONLY       # background useful, no evidentiary reuse
| LEAD_RECHECK       # old claim/source should be re-opened or independently checked
| SOURCE_LEAD        # article points to a primary/secondary object worth retrieving
| CONTRADICTION_LEAD # prior corpus contains conflict/change worth testing
| GAP_LEAD           # prior work explicitly left a material open question
| DROP(reason)       # irrelevant/redundant to current object
```

Rules:

- article text, memory and summaries are discovery aids, never claim proof by status;
- `SUBSTANTIAL_PRIOR` means coverage, not correctness;
- re-use the **question, actor, identifier, source lead or gap**, not the old conclusion;
- if a prior source is time-sensitive, disputed, central or decisive: current reinspection is required when accessible;
- do not re-search stable trivial context unless it can change the model;
- never count multiple corpus articles derived from the same provenance family as independent corroboration.

## 3. Taxonomy — multidimensional, not a moral ladder

Never model:

`influence -> propaganda -> corruption -> ingérence`

as one ordered continuum. These labels describe different dimensions.

For every material mechanism, classify only applicable dimensions:

```text
ORIGIN := DOMESTIC|FOREIGN|TRANSNATIONAL|MIXED|UNKNOWN
ACTOR_TYPE := STATE|PUBLIC_BODY|PARTY|COMPANY|MEDIA|PLATFORM|NGO|FOUNDATION|THINK_TANK|LOBBY|UNION|ACADEMIC|NETWORK|INDIVIDUAL|OTHER
VISIBILITY := OPEN|DISCLOSED_PARTIAL|OPAQUE|DECEPTIVE|UNKNOWN
LEGAL_STATUS := LEGAL|REGULATED|DISPUTED|ILLEGAL|UNKNOWN   # jurisdiction + date required
METHOD := PERSUASION|FUNDING|ACCESS|LOBBYING|PR|ADVERTISING|EXPERTISE|DATA|TARGETING|AMPLIFICATION|MODERATION|ASTROTURFING|CLANDESTINE_ACTION|COERCION|CORRUPTION|OTHER
RELATION := INDEPENDENT|ALIGNED|COOPERATING|COORDINATED|TASKED_COMMANDED|UNKNOWN
TARGET := ELECTORATE|CANDIDATE|PARTY|MEDIA|PLATFORM|ADMINISTRATION|LEGISLATOR|REGULATOR|COURT|POLICY|MARKET|CIVIL_SOCIETY|OTHER
EFFECT_LEVEL := ATTEMPT|ACCESS|EXPOSURE|RECEPTION|PERSUASION|BEHAVIOR|INSTITUTIONAL_CHANGE|ELECTORAL_CHANGE|COUNTERFACTUAL_OUTCOME|NONE_ESTABLISHED|UNKNOWN
```

Strong labels are derived only from evidence appropriate to the exact label:

- `LOBBYING` := organized attempt to influence public decision; legality/transparency assessed separately.
- `PROPAGANDA` := systematic persuasive communication serving an actor/cause; falsity is not required by definition.
- `MANIPULATION` := material steering using deception, concealed constraints, engineered asymmetry or non-transparent exploitation; mechanism must be shown.
- `ASTROTURFING` := organized support presented as grassroots while material sponsorship/coordination is concealed.
- `CAPTURE` := durable distortion/control of a decision process in favor of a concentrated interest; access alone is insufficient.
- `CORRUPTION` := legal/factual category requiring the jurisdiction-specific elements; benefit/proximity alone is insufficient.
- `COERCION` := credible constraint/threat materially limiting choice; persuasion alone is insufficient.
- `INGÉRENCE/INTERFERENCE` := use the relevant legal/institutional definition for jurisdiction/date; “foreign” alone is insufficient.
- `SUBVERSION` / `PSYOPS` := use only with doctrine, operational evidence or sufficiently specific historical documentation.

If criteria are not met, keep the dimensional description instead of forcing a label.

## 4. Probative chains — no skipped inference

### 4.1 Influence/action chain

```text
P0 IDENTITY/RELATION EXISTS
P1 RESOURCES/CAPABILITY/ACCESS
P2 DOCUMENTED ACTION
P3 COORDINATION/TASKING/CONTROL
P4 EXPOSURE/REACH
P5 RECEPTION/PERSUASION
P6 BEHAVIOR/INSTITUTIONAL CHANGE
P7 COUNTERFACTUAL OUTCOME
```

Each level requires its own evidence. Evidence at P0–P2 never automatically establishes P3–P7.

### 4.2 Coordination chain

```text
contact/proximity
!= shared interest
!= repeated cooperation
!= joint planning
!= operational coordination
!= tasking/command
```

A network graph is a lead generator. It is not a causal proof.

### 4.3 Impact chain

```text
action
-> reachable audience/target
-> actual exposure
-> reception
-> changed belief/preference
-> changed behavior/decision
-> outcome changed versus plausible counterfactual
```

Stop at the highest supported level. `attempted influence` is a valid terminal result.

### 4.4 Responsibility / intent

`EVENT != RESPONSIBILITY != INTENT`.

Separate:

```text
actor existed
actor had interest
actor had capability
actor acted
actor coordinated
actor intended result X
actor caused result X
```

No motive or intent from benefit alone.

## 5. Evidence discipline

Truth Engine `definitions/SYMBOLS.md` and `FACT_VERIFICATION.md` remain canonical.

Project rules:

`SOURCE_STATUS != CLAIM_TRUTH`.

An official document may be direct/primary for “institution X stated/decided Y” and weak for “Y is objectively true”. A dissident source is not made true by suppression. An academic label does not replace method review.

Do not use RENARD’s original T1>T2>T3>T4>T5 as a truth rank. Treat source tier only as a discovery/provenance heuristic.

For each exact claim evaluate:

```text
DIRECTNESS
CLAIM_FIT
PROVENANCE
METHOD/DEFINITIONS
ACCESS_TO_FACTS
INDEPENDENCE
TEMPORAL_FIT
CONFLICTS/INTERESTS
LIMITATIONS
```

`INTEREST != INTENT`.

Independent corroboration counts provenance families, not URLs, headlines or repetitions.

## 6. Base rates, denominator, counterfactuals

Before elevating an anomaly/pattern:

- identify denominator/comparator when materially available;
- ask how often similar observations occur without the proposed cause;
- if no defensible base rate exists: `BASE_RATE := UNKNOWN(reason)`; never invent a numerical prior;
- separate chronology from causation;
- test reverse causation and selection effects;
- for major impact claims, state the plausible counterfactual and what evidence would distinguish it.

`anomaly without baseline := lead, not established pattern`.

## 7. Anti-faux-complot invariants

Hard guards:

```text
RELATION != COORDINATION
SHARED_FUNDER != SHARED_COMMAND
SHARED_MEMBERSHIP != JOINT_ACTION
CONVERGENCE != CENTRAL_CONTROL
RECURRENCE != PLAN
OPACITY != CONCEALMENT_OF_WRONGDOING
ACCESS_DIFFICULTY != SUPPRESSION
ABSENCE_OF_EVIDENCE != EVIDENCE_OF_CONCEALMENT
BENEFICIARY != AUTHOR
CAPABILITY != USE
USE != EFFECT
```

When a systemic pattern is proposed, actively test a simpler distributed explanation based on incentives, institutional selection, professional norms, homophily, dependency, market structure or path dependence.

## 8. Competing systemic models

These are **non-exclusive models**, not conclusions to defend:

```text
M0 PLURALISM            := competing interests with no material structural domination established
M1 SECTOR_CAPTURE       := bounded domain/process captured or strongly skewed
M2 TRANSVERSAL_NETWORK  := recurring cross-sector actors/flows/gatekeepers with material influence
M3 EMERGENT_ALIGNMENT   := convergence from incentives/selection/dependencies without central command
M4 DOCUMENTED_COORDINATION := bounded coordinated operations documented
M5 COHERENT_ARCHITECTURE := multiple mechanisms form a durable cross-domain architecture with demonstrated bridges/control/effects
```

A local investigation does not have to choose one global model. At handoff it reports only whether its result `STRENGTHENS|WEAKENS|NEUTRAL|NOT_APPLICABLE` for each model and why in one bounded sentence.

`M5` requires more than many connected nodes: documented bridges, implementation, control paths and effects across domains.

## 9. Systemic object depth

When the object is a system/infrastructure/ecosystem, Truth Engine’s object route must not stop at existence of components. Where applicable inspect:

```text
COMPONENTS
LEGAL/INSTITUTIONAL AUTHORITY
RESOURCES/FLOWS
IDENTIFIERS/DATA_OBJECTS
INTERMEDIARIES
ACCESS_RIGHTS
BRIDGES/INTEROPERABILITY
IMPLEMENTATION
OBSERVED_USE
OVERSIGHT/SAFEGUARDS
ALTERNATIVES
MEASURED_EFFECTS
```

Use the native Truth Engine maps/gaps. Do not add a parallel internal registry.

Key chain:

`CAPABILITY -> IMPLEMENTATION -> OBSERVED_USE -> EFFECT`.

## 10. Search/adversarial discipline

Truth Engine already owns query accounting and refutation. Add only project-level priorities:

1. seek evidence that can change/discriminate the model, not confirmation volume;
2. prioritize primary/quasi-primary objects when accessible;
3. search strongest credible rival/counter-evidence with comparable effort for central claims;
4. pivot by stable identifiers, dates, amounts, entities, legal texts, contracts, filings and intermediaries;
5. lateralize when one vocabulary/source family repeats without delta;
6. preserve OPEN/GAP rather than infer through missing evidence.

No quota of searches. Stop follows Truth Engine terminal predicates; more searching is justified only by material unresolved branches.

## 11. Cross-corpus / cross-investigation connections

A candidate connection is not promoted until:

```text
IDENTITY_RESOLVED
AND CHRONOLOGY_COMPATIBLE
AND RELATION_DOCUMENTED
AND PROVENANCE_INDEPENDENCE_ASSESSED
AND BASE_RATE/COMMONNESS_CONSIDERED
AND RELEVANCE_TO_OBJECT_ESTABLISHED
```

Classify:

```text
CONNECTED_FACT
CANDIDATE_CONNECTION
COINCIDENCE/COMMON_BASELINE
CONTRADICTED_CONNECTION
OPEN_CONNECTION
```

Do not create a “grand graph” that implies causality by visual density.

## 12. Truth Engine final — non-interference

The canonical Truth Engine investigation MUST remain compliant with its own output/template/verifier.

METHOD_PACK-specific metadata is **not injected** into Truth Engine `INVESTIGATION.md` if doing so would alter canonical serialization.

After Truth Engine reaches FINAL, generate a separate `RUN_HANDOFF.md` using `RUN_HANDOFF_TEMPLATE.md`.

## 13. RENARD gate

RENARD is a post-Truth-Engine delta pass, not automatic continuation.

`RENARD := REQUIRED` only if at least one condition holds:

```text
R1 central P0/P1 gap remains and accessible evidence could discriminate it
R2 coordination|intent|causality|impact central claim remains fragile
R3 central conclusion depends materially on one provenance family
R4 unresolved contradiction/residual could change model
R5 Truth Engine exposes a high-value lateral branch not adequately explored within bounded stop
R6 decisive counterfactual or shadow trace remains testable
```

`RENARD := NO` when remaining gaps are inaccessible, immaterial, repetitive, or cannot change the model.

RENARD receives only:

```text
INV_ID
Truth Engine final result/path
central claims + statuses
material gaps/residuals
relevant corpus leads
precise deepening objective
```

It does **not** restart the whole investigation.

Project corrections to RENARD are canonical in `RENARD_PROJECT_OVERLAY.md`.

## 14. New-idea triage

Every new idea/gap produced by a run must be evaluated before entering work.

Required row:

```text
IDEA_TITLE
ORIGIN_INV
TRIGGER := NEW_FACT|GAP|CONTRADICTION|CONNECTION|RESIDUAL|USER_IDEA
UTILITY := HIGH|MEDIUM|LOW
COVERAGE := NEW|PARTIAL|SUBSTANTIAL_PRIOR|UNKNOWN
MATERIALITY := P0|P1|P2
RELATION := CHILD|SIBLING|SYNTHESIS_INPUT|DUPLICATE|OUT_OF_SCOPE
DECISION := DO|RECHECK|MERGE|DEFER|DROP|TRIAGE
PARENT/MERGE_TARGET
EVIDENCE_LEAD := identifiers/source/gap, never just narrative intuition
WHY_MODEL_CHANGE := bounded reason
```

Rules:

- no idea bypasses triage;
- not every named actor/network earns a deep-dive;
- `DROP` and `DEFER` are valid outcomes;
- merge when the discriminant and evidence space are substantially the same;
- create a new INV only when the object/question is materially distinct.

## 15. Project handoff after each Truth Engine run

`RUN_HANDOFF.md` is the only cross-run summary authority. It contains no replacement fact registry.

Minimum:

```text
INV_ID
TE_STATUS/PATH
SUBJECT/OBJECT
EXECUTION_MODE
CORPUS_INHERIT_SUMMARY
CENTRAL_CLAIM_DELTA
MATERIAL_GAPS
CONTRADICTIONS/RESIDUALS
CAUSAL_LEVEL_REACHED
IMPACT_LEVEL_REACHED
SYSTEM_MODELS_DELTA M0..M5
RENARD_DECISION + reason
NEW_IDEAS_TRIAGED
REGISTRY_PATCH
NEXT_RECOMMENDATION
```

Do not copy Truth Engine QRY/SRC/FCT logs into project control. Reference their IDs/path.

## 16. Global article guard

No individual investigation may conclude the final article thesis.

Forbidden shortcuts:

```text
“everything is connected”
“the enemy is internal/external” as premise
“official = false”
“dissident = true”
“funded by X = controlled by X”
“operation existed = election/result changed”
“same narrative = coordinated campaign”
```

The final systemic synthesis belongs only to `INV-133` after dependency/evidence sufficiency gates.
