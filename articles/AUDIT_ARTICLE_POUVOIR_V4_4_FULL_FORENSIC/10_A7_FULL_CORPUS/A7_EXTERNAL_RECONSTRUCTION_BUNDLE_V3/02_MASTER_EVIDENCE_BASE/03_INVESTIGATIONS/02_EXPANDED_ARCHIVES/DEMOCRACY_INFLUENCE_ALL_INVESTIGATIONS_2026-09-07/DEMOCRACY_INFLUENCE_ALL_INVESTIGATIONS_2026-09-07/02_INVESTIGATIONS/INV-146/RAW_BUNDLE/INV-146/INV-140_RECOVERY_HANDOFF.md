---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "recovery_handoff"
artifact_id: "INV-140-RECOVERY-HANDOFF"
version: "1.0"
status: "recovered"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-140"
---

<!-- RECOVERY: original_final_bundle_or_handoff_missing_from_library=true -->
<!-- DERIVED_FROM: inv140_narrative.md frozen terminal narrative + TRACELOG final terminal metadata -->
<!-- DECISION: usable_for_INV-146=YES; no_missing_ID_reconstruction=true -->

# RECOVERY_HANDOFF — INV-140

```text
INV_ID = INV-140
ORIGINAL_TE_STATUS = DELIVERY_PASS_R3P1
ORIGINAL_FINAL_COUNTS = 13 QRY / 13 SRC / 17 FCT / 8 provenance families
ORIGINAL_DELIVERABLE_SHA256_PREFIX = 3281778a44c2
ORIGINAL_POST_RUN = P0=0 / P1=0 / P2=3 / RENARD=NO / CLOSED
RECOVERY_EVIDENCE = frozen terminal technical narrative + terminal TRACELOG metadata
INV_STATUS = CLOSED
```

## Central delta

Le financement étranger indirect doit être décomposé en `origine ultime -> véhicule -> affectation électorale -> coordination/tasking -> exposition -> réception/comportement -> résultat contrefactuel`. Aucun maillon ne prouve automatiquement le suivant.

Le corpus distingue notamment financement général d’une organisation, campagne électorale indépendante, véhicule domestique alimenté par des fonds étrangers, soutien clandestin désigné à des acteurs politiques et publicité politique régulée. Cette décomposition empêche de traiter de manière identique une subvention étrangère générale, une campagne transnationale ouverte et un mécanisme clandestin de soutien électoral.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED/PARTIAL selon origine ultime et véhicule
I1 resources/capability/access = VERIFIED pour les flux et capacités documentés
I2 documented action = VERIFIED pour plusieurs activités électorales/civiques ouvertes ou clandestines
I3 coordination/tasking/control = VERIFIED/PARTIAL uniquement lorsque affectation ou soutien désigné est documenté
I4 exposure/reach = PARTIAL/MEASURED dans certains cas
I5 reception/persuasion = NOT_ESTABLISHED généralement
I6 behavior/electoral change = NOT_ESTABLISHED indépendamment dans les cas centraux
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps

1. `ATTRIBUTION/EARMARKING` — pièces comptables, conventions ou instructions reliant précisément certains fonds amont aux dépenses électorales de destination.
2. `TASKING` — autonomie, coordination et commandement doivent rester distingués.
3. `IMPACT` — aucun design indépendant ne ferme persuasion, comportement ou résultat électoral contrefactuel.

## RENARD

`NO` — les gaps exigent des pièces ou méthodes spécifiques ; l’extension générique serait cumulative.

## Recovery guard

This artifact does **not** reconstruct missing original bundle bytes or invent missing runtime IDs. It compresses the frozen terminal narrative for dependency handoff use only.
