---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-063"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-041"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-063

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-0621-big-four-norm-production`
- Deliverable: `INV-063_INVESTIGATION.md`
- Deliverable SHA-256: `ee088d015ca5bbbf91ab4ee8ef398150764dc9ea679ab222938097b9db80181e`
- Corpus runtime: `QRY=15 / SRC=12 / FCT=16 / provenance_families=6`
- Persistence: `PASS / eligible=16 / blocked=16 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-063 ferme une partie importante du mécanisme « expertise privée -> norme » sans valider une capture générale. Le corpus établit une empreinte institutionnelle matérielle des Big Four dans l'audit, le conseil et des arènes techniques de normalisation, ainsi que des risques documentés de concentration, de rôles cumulés, de conflit et de revolving doors. Il établit surtout un cas concret où une étude d'impact commandée par la Commission, co-signée par un consortium incluant Deloitte, est reprise dans l'impact assessment de la Commission sur les machines, dont un case study est explicitement présenté comme confirmant le besoin d'une exigence sur le logiciel de sécurité; une exigence substantiellement correspondante figure ensuite dans le règlement (UE) 2023/1230. La chaîne supportée est donc expertise externe/étude -> préparation réglementaire -> continuité textuelle dans la norme, au niveau consortium. Elle ne devient pas Deloitte seul -> adoption, ni Big Four -> contrôle de la décision : EFRAG/ANC restent multi-acteurs et soumis à des gates publics, le marché étroit du conseil « policymaking » n'est pas dominé par les Big Four dans l'étude du Parlement, et aucun tasking de revolving door ni contre-factuel de capture générale n'est établi.

## Registre causal certifié

- `consulting contract/expertise -> study/advice -> public decision preparation` = **SUPPORTED** — Preparation input is not final decision control.
- `Deloitte-containing consortium study -> Commission impact assessment case-study conclusion -> standalone safety-software policy requirement -> final Machinery Regulation` = **SUPPORTED** — Consortium authorship and subsequent Commission/co-legislator choices prevent Deloitte-specific marginal attribution.
- `Big Four technical-panel membership/personnel -> standard-setting access/input` = **SUPPORTED** — Access/input does not establish adoption or control.
- `Big Four standard-setting access -> specific adopted standard because of Big Four input` = **UNRESOLVED** — No versioned text/meeting record in this run isolates a Big Four proposal as the cause of final adoption.
- `revolving door -> privileged access/tasking -> regulatory capture` = **UNRESOLVED** — Systemic risk and weakly mitigated cases do not prove Big Four-specific tasking or capture.

## Gaps matériels certifiés

- `CLM-003` / **ADOPTION** — Membership or technical contribution does not identify which proposal was adopted because of that participant.
- `CLM-005` / **ATTRIBUTION** — The study was consortium-authored and the final act was co-legislated; Deloitte-specific marginal causal contribution is not isolated.
- `CLM-006` / **CAUSAL_ATTRIBUTION** — Need named move -> privileged access/input -> identifiable text/decision -> counterfactual effect evidence.
- `CLM-007` / **COUNTERFACTUAL** — No general design isolates Big Four marginal effect on final decisions across the France/EU policy universe.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-041`.

## Transition attendue

`INV-063 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
