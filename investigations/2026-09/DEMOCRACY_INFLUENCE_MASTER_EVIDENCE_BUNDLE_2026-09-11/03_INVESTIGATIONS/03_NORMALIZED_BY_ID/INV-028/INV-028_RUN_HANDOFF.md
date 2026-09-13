---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-028"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-027"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-028

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-0400-aipac-electoral-lobbying-france`
- Deliverable: `INV-028_INVESTIGATION.md`
- Deliverable SHA-256: `ec95309f580365bea401e97404490d8c61835555956c59454f2e06c775f095e6`
- Corpus runtime: `QRY=37 / SRC=17 / FCT=30 / provenance_families=6`
- Persistence: `PASS / eligible=30 / blocked=30 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

AIPAC operates through three distinct, documented U.S. channels: registered lobbying, PAC contributions and UDP independent expenditures. Large candidate-specific spending and electoral outcomes are verified, but the inspected evidence does not identify the marginal causal effect on Bowman/Bush defeats, candidate control, vote buying or Israeli-state tasking. French campaign-finance rules make the U.S. PAC/Super-PAC architecture non-isomorphic; the remaining material France-side test is functional: whether documented lobbying/access resources can be tied to identifiable positions, actions or decisions.

## Registre causal certifié

- `AIPAC organizational resources -> registered federal lobbying -> access to and activity within the U.S. federal policy process` = **SUPPORTED** — Registered lobbying and disclosed expenditure establish an influence channel and access-seeking activity, not policy capture or a specific decision effect.
- `UDP resources -> candidate-specific independent expenditures -> purchased media/direct-mail support or opposition -> campaign information exposure` = **SUPPORTED** — The expenditure-to-exposure edge is supported by transaction records; persuasion and candidate control are not established by those records.
- `UDP candidate-specific spending -> voter persuasion/turnout -> Bowman or Bush defeat` = **UNRESOLVED** — Large spending and subsequent defeat coexist, but strategic selection, candidate quality, district factors and other campaign shocks prevent identification of the marginal spending effect.
- `AIPAC/UDP lobbying, contributions or spending -> candidate/office policy-position change or vote -> policy outcome` = **UNRESOLVED** — Resource and access channels are documented, but this run lacks matched before/after or counterfactual evidence on candidate or office behavior attributable to the intervention.
- `U.S. PAC/Super-PAC financing architecture -> direct legal analogue in French candidate financing` = **REFUTED** — Functional lobbying/advocacy comparison remains possible, but the campaign-finance vehicles are legally non-isomorphic.

## Gaps matériels certifiés

- `CLM-003` / **COUNTERFACTUAL** — No race-specific counterfactual or quasi-experimental design isolates the marginal effect of UDP spending from candidate, district, timing and strategic-spending confounders.
- `CLM-006` / **FRANCE_CASE_EVIDENCE** — This run does not establish a matched French actor-level case measuring access, policy-position change or decision effect under the French lobbying regime.
- `CLM-007` / **TASKING_AND_BEHAVIOR** — Authenticated principal-tasking records or candidate/office-level response evidence would be required to upgrade agency, control or capture claims.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-027`.

## Transition attendue

`INV-028 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
