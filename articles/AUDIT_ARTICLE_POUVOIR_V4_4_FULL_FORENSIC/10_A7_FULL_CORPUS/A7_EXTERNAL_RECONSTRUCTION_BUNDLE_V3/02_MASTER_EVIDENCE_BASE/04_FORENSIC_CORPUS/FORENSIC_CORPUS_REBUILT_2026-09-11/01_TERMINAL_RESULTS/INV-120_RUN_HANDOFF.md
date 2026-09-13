---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-120"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-120

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-0710-finance-banking-influence`
- Deliverable: `INV-120_INVESTIGATION.md`
- Deliverable SHA-256: `a40e54aa5d6d68ce5a3b7b66a4d2c00832e2b2f51ae92ba376ea2d9d1fef1555`
- Corpus runtime: `QRY=10 / SRC=10 / FCT=12 / provenance_families=5`
- Persistence: `PASS / eligible=12 / blocked=12 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-120 ferme un résultat borné : le lobbying bancaire français et européen est dense, spécifique et orienté vers des décisions réglementaires ou fiscales identifiables ; les cas Farkas/AFME et BlackRock établissent en outre des risques d'intégrité sérieux, jusqu'à une constatation de mauvaise administration pour la revolving door EBA->AFME. En revanche, le corpus ne ferme pas une chaîne actor-specific intervention privée -> delta réglementaire précis -> effet. Les flexibilités CRR/FRTB sont aussi explicitement reliées par la Commission à des causes institutionnelles concurrentes, notamment coordination internationale et level playing field. Influence structurelle et risques de conflit sont donc établis ; capture décisionnelle spécifique non démontrée.

## Registre causal certifié

- `banking federation lobbying -> meetings/submissions -> prudential or fiscal rule delta` = **UNRESOLVED** — Access and policy alignment are insufficient to identify causation.
- `international Basel implementation asymmetry -> EU level-playing-field concern -> FRTB postponement/adaptation` = **SUPPORTED** — This does not exclude industry lobbying as a contributing factor, but it supplies a direct institutional rival cause.
- `senior regulator move to financial lobby -> conflict/confidentiality risk -> Ombudsman finding -> ethics-policy correction` = **SUPPORTED** — This closes governance harm and reform, not downstream regulatory capture.
- `BlackRock policy-study contract -> privileged policy-relevant expertise access -> conflict risk -> Commission procurement-rule reflection` = **SUPPORTED** — No final banking-rule delta is traced to BlackRock recommendations.
- `BlackRock study recommendations -> Commission legislative choice -> adopted ESG banking-rule delta` = **UNRESOLVED** — Policy relevance and conflict risk cannot substitute for uptake evidence.

## Gaps matériels certifiés

- `CLM-003` / **CAUSALITY** — Commission records identify international implementation asymmetry and co-legislative design as explicit rival causes; no intervention-to-amendment chain isolates private lobbying as decisive.
- `CLM-005` / **EVIDENCE** — The governance failure and risk are documented; no sampled decision-specific transmission from Farkas to a changed rule is documented.
- `CLM-006` / **CAUSALITY** — No traced recommendation-to-final-rule delta in the sampled record.

## RENARD

`NO`

## Reclassification

Impact direct : `NONE`.

## Transition attendue

`INV-120 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
