# Truth Engine v2.6 — Investigation-first anti-regression release

## Incident

A real run on the 54-minute corruption transcript regressed into a bounded fact-check of the “120 milliards” claim instead of investigating corruption.

Observed output defects:

- `SCOPING_REPORT` reduced the question to whether 120 Md€/year was correctly presented.
- Its exclusions removed the general association audit, case inventory and alternative calculation.
- Six CLM rows all audited the post/number; later transcript cases and documentary leads were not routed.
- PELOTE explicitly traced “the provenance of the number, not the cause of corruption”.
- MONEY was declared non-computable without a real payer→vehicle→beneficiary investigation.
- Impact concerned possible reader misunderstanding rather than the real-world corruption object.

This output was a competent debunk. It was not the requested forensic investigation.

## Root cause

The v2.0→v2.1 refactor correctly removed forced counts of mechanisms, causal depth and named persons. It failed to replace those unsafe output quotas with mandatory exploration coverage.

The earlier audit had already identified this exact risk as `R5 — targets becoming too permissive`. Search could stop when central source claims were resolved, even while the underlying object, cases, money flows, mechanisms, actors, controls and impacts remained uninvestigated.

## Corrective contract

`MISSION_MODE=INVESTIGATION` is now the default. `VERIFY_ONLY` requires an explicit exclusive user request; a document, claim, post, video or transcript cannot select it implicitly.

Truth Engine now separates:

- `LEAD_QUESTION`: is the supplied source/claim accurate?
- `OBJECT_QUESTION`: what is materially happening in the real world?

In INVESTIGATION mode, the source audit is one branch and OBJECT_QUESTION is primary.

### Coverage without fabrication

- `LEAD_REGISTRY` maps every substantive chapter/topic/time block to `LED-ID`; exclusions remain registered as `ROUTE=EXCLUDE(reason)`.
- Multi-segment or COMPLEX/APEX documents checkpoint immediately after lead extraction, before scope/search planning.
- `INVESTIGATION_MAP` routes applicable axes: source audit, history/scale, cases, money, mechanisms, actors/networks, controls/response, impact/responsibility and counter-hypotheses.
- Every lead terminates `SATURATED`, `GAP` or `EXCLUDED`; each applicable axis receives an actual evidence-object attempt and terminates `SATURATED` or `GAP`.
- `N/A` means logically irrelevant; missing evidence is a GAP.
- Refuting a lead never refutes or closes the underlying phenomenon.
- Fact-check saturation never equals investigation saturation.

No fact, mechanism, causal depth, amount, network edge or responsible person is forced. Mandatory exploration and mandatory findings are deliberately distinct.

## Corruption-transcript acceptance case

For the incident source, compliant routing must:

1. cover all material transcript segments, including concrete cases, actors, documents, amounts and institutional claims;
2. audit the 120 Md€ claim as one branch;
3. investigate the underlying corruption/public-integrity object through applicable case, money, mechanism, actor/network, control, impact and counter-hypothesis axes;
4. use PELOTE for real-world mechanisms, not only the statistic’s publication genealogy;
5. report sourced findings or explicit gaps without manufacturing accusations.

## Preserved

- One canonical investigation Markdown and no article/PART files.
- v2.5 cumulative OPEN checkpoints, same-run RESUME and one FINAL write.
- Historical phase IDs `0→19a`, gate IDs `G0→G10`, ontology and fact statuses.
- Typed causality and the invariants `BENEFIT≠INTENT`, `ROLE≠RESPONSIBILITY`, `ASSOCIATION≠COORDINATION`.
- Targets remain effort guides, never truth quotas.
- Complexity is recomputed from actual expanded scope; case count alone does not force APEX or establish a system.

## Modified files

- `KERNEL.md`
- `forensic/GATES.md`
- `forensic/REQUEST_LOG.md`
- `protocol/INVESTIGATION.md`
- `protocol/UPDATE.md`
- `output/TEMPLATE.md`
- `search/EPISTEMIC.md`
- `search/OPTIMIZATION.md`
- `search/TEMPLATES.md`
- `tools/DSL.md`
- `tools/MACROS.md`
- `CHANGELOG_V2.6.md`

## Parent and rollback

Parent archive: `truth-engine-v2.5.zip`
Parent SHA-256: `465a02b2cacfc590e4ce2ad92436d2117cb5ab10cf49692a42e58742f28663f8`

A v2.6 `STATE:OPEN` snapshot is not resumable by v2.5 because MISSION_MODE, LED/AXS registries and object maps are new canonical state.
