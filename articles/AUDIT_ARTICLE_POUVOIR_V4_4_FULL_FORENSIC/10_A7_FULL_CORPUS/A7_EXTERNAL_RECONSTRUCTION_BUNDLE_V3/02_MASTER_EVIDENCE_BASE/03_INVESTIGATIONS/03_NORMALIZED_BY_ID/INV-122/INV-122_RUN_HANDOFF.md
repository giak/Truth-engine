---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-122"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-122

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-0646-defense-industry`
- Deliverable: `INV-122_INVESTIGATION.md`
- Deliverable SHA-256: `3e9201a05de411c4e7d8bf7471d18fd697b6948f6bdc0c45eda3281767f51168`
- Corpus runtime: `QRY=14 / SRC=14 / FCT=15 / provenance_families=5`
- Persistence: `PASS / eligible=15 / blocked=15 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-122 ferme un résultat borné : les industriels de défense français et européens déclarent des actions de lobbying explicitement liées à la LPM, au PLF, à des programmes et marchés ; l'interdépendance État-BITD est documentée, mais le corpus ne ferme pas une causalité spécifique lobbying -> décision ni une capture par expertise financée. Les chronologies A400M montrent des arbitrages publics non réductibles au seul intérêt industriel. Accès, contrat et financement d'expertise ne valent donc ni commandement ni capture sans empreinte décisionnelle démontrée.

## Registre causal certifié

- `industrial lobbying -> meetings/expertise -> LPM/PLF/programme decision` = **UNRESOLVED** — Temporal alignment and access do not identify the decisive cause.
- `sovereignty/operational strategy -> LPM budget and procurement rules -> orders/capacity -> industrial revenue and production continuity` = **SUPPORTED** — This establishes state-to-industry causation, not private capture of the state.
- `A400M capability and budget trade-off -> target reduction -> production-chain risk -> later France/Spain support and accelerated deliveries` = **SUPPORTED** — The later support has operational, export and industrial rationales; supplier lobbying is not isolated as the cause.
- `public-order dependence -> industrial incentive to lobby -> recurring access -> feedback into policy debate` = **SUPPORTED** — Feedback opportunity is established; capture requires a decision delta attributable to the private actor.
- `defence-company partnership funding -> think-tank agenda/conclusion -> policymaker uptake -> defence decision` = **UNRESOLVED** — Partner status cannot substitute for transmission evidence.

## Gaps matériels certifiés

- `CLM-002` / **CAUSALITY** — No matched documentary chain isolates lobbying as the decisive cause against operational, sovereignty, budget and parliamentary rationales.
- `CLM-006` / **EVIDENCE** — Partnership is documented; earmarking, editorial instruction, altered conclusion and decision uptake are not documented in the sampled source.

## RENARD

`NO`

## Reclassification

Impact direct : `NONE`.

## Transition attendue

`INV-122 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
