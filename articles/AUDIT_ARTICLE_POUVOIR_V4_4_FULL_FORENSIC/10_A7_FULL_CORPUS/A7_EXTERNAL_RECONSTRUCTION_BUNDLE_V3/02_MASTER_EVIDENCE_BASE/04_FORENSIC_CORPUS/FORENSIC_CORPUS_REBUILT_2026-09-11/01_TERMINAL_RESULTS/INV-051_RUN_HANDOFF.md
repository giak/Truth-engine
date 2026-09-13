---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-051"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-052"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-051

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-0532-philanthropy-policy`
- Deliverable: `INV-051_INVESTIGATION.md`
- Deliverable SHA-256: `8b176dbef7867ac6bfb5832ca331510edcb8c80b2f889a025182894dedbcf10d`
- Corpus runtime: `QRY=12 / SRC=12 / FCT=13 / provenance_families=8`
- Persistence: `PASS / eligible=13 / blocked=13 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-051 ferme un modèle borné : les grandes fondations peuvent convertir des ressources en capacité institutionnelle, contrainte d'allocation ou capacité d'advocacy et d'accès ; le cas Rockefeller/Paris ferme une contribution matérielle à la production d'une stratégie municipale, tandis que l'OMS documente un effet structurel du financement fléché sur sa discrétion et que Reset/EDRi documentent advocacy et accès au processus UE. Aucune chaîne inspectée ne justifie financement=commandement, accès=capture ou donor-specific policy authorship sans tasking, conditionnalité ou empreinte décisionnelle supplémentaire.

## Registre causal certifié

- `Rockefeller 100RC resources/method -> Paris resilience capacity/CRO -> municipal resilience strategy and 35-action programme` = **SUPPORTED** — The strategy was co-produced by municipal directorates and more than 800 partners; foundation support does not establish substantive command.
- `tightly specified voluntary funding -> reduced WHO discretion over resource allocation` = **SUPPORTED** — This is a structural financing effect; it does not identify which donor caused which policy output.
- `Gates philanthropic funding -> donor leverage -> specific WHO policy/recommendation` = **UNRESOLVED** — Major funding and structural leverage are documented; marginal effect on a specific decision is not identified.
- `Luminate/Sandler support -> Reset advocacy/access -> specific DSA legislative provision/adoption` = **UNRESOLVED** — Advocacy intent, self-reported contribution and formal access are documented; clause-level independent attribution is absent.
- `foundation grants -> EDRi policy advocacy -> formal EU policymaker access` = **SUPPORTED** — Access and advocacy are established; donor tasking and adoption of a donor-preferred policy are not.

## Gaps matériels certifiés

- `CLM-002` / **CAUSALITY** — No inspected public record closes a Gates grant/condition -> specific WHO recommendation or policy text -> adoption counterfactual.
- `CLM-003` / **CAUSALITY** — No independently verified clause-level contribution -> text delta -> adoption chain was found in the inspected corpus.
- `CLM-004` / **CAUSALITY** — Grant terms inspected do not close donor instruction -> EDRi position -> specific adopted rule.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-052`.

## Transition attendue

`INV-051 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
