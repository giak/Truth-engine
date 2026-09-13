---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-084"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-084

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-0558-news-agencies-agenda-setting`
- Deliverable: `INV-084_INVESTIGATION.md`
- Deliverable SHA-256: `93f63eb197e2e68f23227606f6d9c9183f1e79d4d006ecd3ed3c1d7b995a7137`
- Corpus runtime: `QRY=18 / SRC=15 / FCT=19 / provenance_families=8`
- Persistence: `PASS / eligible=19 / blocked=19 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

AFP, Reuters et AP ont une puissance d'agenda structurelle vérifiable au niveau production -> sélection/vérification -> distribution -> reprise aval : réseaux globaux, flux/API intégrés et études empiriques montrent une dépendance parfois élevée et du verbatim. Mais cette dépendance varie fortement par marché (contre-exemple allemand dominé par dpa), les agences ne forment pas un bloc éditorial homogène et aucune preuve bornée ne ferme une coordination politique commune, la persuasion ou un effet électoral/politique attribuable à l'origine d'agence.

## Registre causal certifié

- `event/source -> agency selection and verification -> packaged wire output` = **SUPPORTED** — Editorial standards document the gate and its controls but do not enumerate every unpublished selection decision.
- `agency wire -> feed/API/client workflow -> downstream article reuse` = **SUPPORTED** — Magnitude varies across markets; no France-wide full denominator specific to the big three is available in this run.
- `agency topic salience/framing -> downstream media agenda salience/framing` = **UNRESOLVED** — Copy reuse and upstream filtering support propagation capacity, but event importance and client editing confound exact marginal agenda contribution.
- `agency-originated downstream exposure -> audience persuasion -> vote or policy outcome` = **UNRESOLVED** — No direct causal design specific to AFP/Reuters/AP wire exposure was found; exposure and agenda salience are not persuasion or vote effects.
- `shared AFP/Reuters/AP sourcing -> coordinated common political agenda command` = **REFUTED** — Shared professional routines or common event salience can generate convergence without tasking.

## Gaps matériels certifiés

- `CLM-002` / **GENERALIZATION** — Available samples do not provide a representative France-wide 2019-2026 denominator specifically for AFP, Reuters and AP.
- `CLM-005` / **TASKING** — No authenticated common editorial command/tasking record was found in the bounded search.
- `CLM-006` / **CAUSAL_ATTRIBUTION** — Interview evidence does not quantify topic-level causal effects of metrics on political coverage.
- `CLM-007` / **COUNTERFACTUAL** — No direct causal design was found linking exposure to agency-originated material through persuasion to a political behavior or outcome.

## RENARD

`NO`

## Reclassification

Impact direct : `NONE`.

## Transition attendue

`INV-084 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
