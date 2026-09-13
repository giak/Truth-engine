---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-062"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-063"
updated: "2026-09-09"
---

# RUN_HANDOFF — INV-062

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260909-1657-mckinsey-state-consulting-influence`
- Deliverable: `INV-062_INVESTIGATION.md`
- Deliverable SHA-256: `8c58fa3eeb46abff302beb87005aee0af48bb29ec88644b83a8707b4cae2f17b`
- Corpus runtime: `QRY=27 / SRC=16 / FCT=28 / provenance_families=5`
- Persistence: `PASS / eligible=28 / blocked=28 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-062 ferme la confusion entre recours au conseil et délégation de souveraineté. Le corpus établit des interventions matérielles de cabinets dans la préparation et parfois l’implémentation de politiques publiques, avec des cas de dépendance organisationnelle ponctuelle. Mais il documente aussi des filtres administratifs, des réécritures, des rejets, des missions sans effet identifiable et des transferts vers des capacités internes. La chaîne supportée est donc contrat -> contribution de conseil -> préparation/implémentation dans certains cas ; elle ne devient pas automatiquement cabinet -> décision souveraine ni cabinet -> effet politique causal. Le delta réduit la valeur d’une enquête générique sur « les consultants influencent l’État », mais laisse ouverte la question distincte d’INV-063 : effets spécifiques des rôles cumulés conseil/audit/normes/marchés et revolving doors sur une règle ou décision identifiable.

## Registre causal certifié

- `strategy consulting mission -> substantive scenarios/recommendations -> public decision preparation` = **SUPPORTED** — Decision preparation is established; marginal causal contribution to the final political choice is not generally isolated.
- `McKinsey vaccination support -> operational organisation/document contribution -> state vaccination campaign execution` = **SUPPORTED** — Operational contribution and temporary dependence do not establish that McKinsey made health-policy or vaccination decisions.
- `consulting-supported telework drafting -> administration editing/rejection -> published guide -> circular referral -> administrative implementation` = **SUPPORTED** — The edge reaches implementation of a shared output; consultant marginal authorship and independent control are not established.
- `teacher-profession consulting mission -> deliverables -> identifiable education-policy change` = **UNRESOLVED** — No inspected evidence identifies a direct policy consequence attributable to the mission.
- `external consulting at scale -> loss of internal capability/dependence -> consultant control of sovereign policy decision` = **UNRESOLVED** — Dependence indicators exist case-specifically; generalized decision displacement is not demonstrated and post-2022 controls/internalisation provide counter-evidence.

## Gaps matériels certifiés

- `CLM-005` / **GENERALIZATION** — The inspected record does not provide a denominator or causal design establishing persistent whole-of-state cognitive dependence across ministries and policy domains.
- `CLM-006` / **CAUSALITY** — A sovereignty-delegation claim would require decision-specific evidence that consultant recommendations displaced or controlled the responsible public authority, plus a counterfactual showing the public decision depended on that displacement.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-063`.

## Transition attendue

`INV-062 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
