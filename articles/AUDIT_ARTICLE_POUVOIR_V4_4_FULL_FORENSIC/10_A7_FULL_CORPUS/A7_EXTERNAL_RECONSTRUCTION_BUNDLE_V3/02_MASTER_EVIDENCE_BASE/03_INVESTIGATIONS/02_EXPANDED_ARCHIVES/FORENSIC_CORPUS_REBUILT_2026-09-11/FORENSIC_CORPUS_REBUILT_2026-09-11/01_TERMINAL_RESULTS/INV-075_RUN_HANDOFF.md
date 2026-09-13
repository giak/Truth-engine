---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-075"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-075

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-0650-public-broadcast`
- Deliverable: `INV-075_INVESTIGATION.md`
- Deliverable SHA-256: `a4fbf5da649c1051b94d56b7e63586ea76d4db859f254b7fe4d38c883d13b308`
- Corpus runtime: `QRY=12 / SRC=12 / FCT=13 / provenance_families=5`
- Persistence: `PASS / eligible=13 / blocked=13 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-075 ferme un modèle à quatre leviers distincts : financement et contrats d'objectifs contraignent ressources et stratégie sans fermer un ordre éditorial précis ; la présidence de France Télévisions est nommée par l'Arcom et non directement par le Gouvernement, tandis que le conseil conserve une présence étatique et parlementaire ; l'Arcom peut corriger le pluralisme mais le Conseil d'État protège une sphère de responsabilité éditoriale ; enfin la production indépendante et la concentration de fournisseurs créent une dépendance commerciale plausible sans établir une capture politique. Aucun pont actor-specific responsable politique -> instruction -> décision éditoriale -> exposition n'est fermé.

## Registre causal certifié

- `tax allocation / annual budget / COM -> resource envelope and strategic priorities -> programming constraints` = **SUPPORTED** — No direct content-specific instruction or political effect is identified.
- `Arcom appointment -> president strategic authority -> specific editorial decision` = **UNRESOLVED** — Appointment establishes governance influence, not tasking.
- `Arcom pluralism monitoring -> request/correction -> political exposure balance` = **SUPPORTED** — This is regulator-based legal oversight, not evidence of partisan governmental direction.
- `legal/judicial pluralism control -> attempted intervention in debate participation -> higher-court protection of editorial freedom` = **SUPPORTED** — Shows real review power and a counter-limit, not persistent political command.
- `independent-production quotas + supplier concentration -> commissioning dependence -> potential content influence` = **UNRESOLVED** — Commercial dependence risk is not equivalent to political capture.

## Gaps matériels certifiés

- `CLM-001` / **CAUSALITY** — Resource and strategy leverage are documented; content-specific transmission is not.
- `CLM-003` / **EVIDENCE** — Need actor-specific minutes, instructions or documented interventions linking a political principal to a content decision.
- `CLM-006` / **EVIDENCE** — Supplier concentration and commissioning are documented; political tasking, editorial command and content-effect links are not.

## RENARD

`NO`

## Reclassification

Impact direct : `NONE`.

## Transition attendue

`INV-075 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
