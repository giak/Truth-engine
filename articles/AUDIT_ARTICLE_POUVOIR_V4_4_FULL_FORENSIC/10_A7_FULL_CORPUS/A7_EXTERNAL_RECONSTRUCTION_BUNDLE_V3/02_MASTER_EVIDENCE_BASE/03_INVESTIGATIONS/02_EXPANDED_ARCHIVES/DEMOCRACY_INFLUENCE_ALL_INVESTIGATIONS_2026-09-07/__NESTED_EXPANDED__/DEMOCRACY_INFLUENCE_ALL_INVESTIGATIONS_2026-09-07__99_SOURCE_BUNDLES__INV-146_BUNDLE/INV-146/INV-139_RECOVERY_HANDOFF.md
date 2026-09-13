---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "recovery_handoff"
artifact_id: "INV-139-RECOVERY-HANDOFF"
version: "1.0"
status: "recovered"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-139"
---

<!-- RECOVERY: original_final_artifact_missing_from_library=true -->
<!-- DERIVED_FROM: INV-139_RUN_STATE.json persisted OPEN/CP3 subset + TRACELOG final terminal metadata -->
<!-- NON_CLAIM: does_not_recreate_missing_FCT-015..022_or_original_deliverable_bytes=true -->
<!-- DECISION: usable_for_INV-146=YES; scope=central_delta+proof_ceiling+terminal_residuals -->

# RECOVERY_HANDOFF — INV-139

```text
INV_ID = INV-139
ORIGINAL_TE_STATUS = DELIVERY_PASS_R3P1
ORIGINAL_FINAL_COUNTS = 22 QRY / 22 SRC / 22 FCT / 21 provenance families
ORIGINAL_DELIVERABLE_SHA256_PREFIX = 93b805bd99ec
ORIGINAL_POST_RUN = P0=0 / P1=0 / P2=3 / RENARD=NO / CLOSED
RECOVERY_EVIDENCE = 14 persisted FCT in OPEN CP3 state + terminal TRACELOG metadata
RECOVERY_SCOPE = central delta / symmetry control / proof ceiling only
INV_STATUS = CLOSED
```

## Central delta recoverable without fabrication

L’Union européenne est elle-même un émetteur documenté d’influence politique extérieure ouverte. Les éléments persistés établissent un portefeuille comprenant financement de démocratie/société civile/médias, soutien à des acteurs politiques, observation électorale suivie de dialogue et d’assistance à la réforme, conditionnalité d’adhésion ou d’aide, et sanctions explicitement conçues pour obtenir un changement de politique ou d’activité.

La propriété discriminante n’est pas « UE = ingérence » mais la combinaison `visibilité + consentement + base juridique + destinataire + affectation/tasking + coercition + exposition + effet`. Certains instruments sont invités et ouvertement encadrés ; certains financements thématiques peuvent opérer sans approbation du gouvernement tiers ; la conditionnalité et les sanctions sont ouvertement coercitives. Ces classes ne sont donc pas isomorphes à une opération clandestine simplement parce qu’elles cherchent toutes à modifier un environnement politique.

## Highest supported I0..I7 — recovery-bounded

```text
I0 identity/relation = VERIFIED — institutions, programmes et bénéficiaires-types identifiés
I1 resources/capability/access = VERIFIED — budgets, subventions, instruments de conditionnalité et sanctions documentés
I2 documented action = VERIFIED — financements, EOM/follow-up, soutien politique/média, conditionnalité et sanctions documentés
I3 coordination/tasking/control = VERIFIED pour dispositifs officiels et conditions formelles ; beneficiary-level tasking remains case-specific
I4 exposure/reach = PARTIAL — portefeuille et certains programmes documentés, mesure homogène absente
I5 reception/persuasion = NOT_ESTABLISHED généralement
I6 behavior/institutional change = PARTIAL / CASE_SPECIFIC — réforme visée et réactions observables, causalité indépendante non isolée
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Terminal residuals preserved from TRACELOG

1. `RESPONSIBILITY/TASKING` — beneficiary-level tasking records remain required for stronger downstream-control claims.
2. `CAUSALITY` — country-level causal designs are required to isolate institutional/behavioral effects.
3. `COMPARABILITY` — ally/adversary symmetry belongs to INV-146 and must use materially isomorphic mechanisms.

## RENARD

`NO` — terminal trace states generic further collection would be cumulative; only targeted records/designs could upgrade the residuals.

## Recovery guard

This artifact does **not** claim to reproduce the missing final INV-139 deliverable, missing final fact IDs, or original SHA. It restores only the material terminal handoff needed by INV-146 from evidence still persisted plus the append-only terminal trace.
