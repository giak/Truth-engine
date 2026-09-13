---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-156"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
execution_context: "PROTOCOL_RECONSTRUCTION_NOT_CANONICAL_REGISTRY_APPLY"
canonical_registry_applied: false
reclass_impact: "DEFERRED_REWARD_REVOLVING_DOOR,PROFESSIONAL_ENABLERS_OPAQUE_INFLUENCE,PHYSICAL_INFRASTRUCTURE_CONTROL,OFFSET_SPECIFIC_MISCONDUCT"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-156

## Canonicality

`control.py`/`verify.py` existent dans la Library, mais le registre canonique disponible ne contient pas la branche `INV-148+`. Aucun `control.py apply` sur `INV-156` n'est donc revendiqué. Le statut ci-dessous est un **pass protocolaire reconstruit**, prêt pour replay/migration locale.

## Certification

- Truth Engine contract reconstructed: `DELIVERY_PASS_R3P1`
- Run: `20260911-2136-procurement-intermediaires-commissions`
- Deliverable: `2026-09-11_21-36_procurement-intermediaires-commissions_INVESTIGATION.md`
- Deliverable SHA-256: `47f778452ba307851428541da389852ffc43c7c19daa70960d80327568b66ef4`
- Corpus runtime: `QRY=11 / SRC=11 / FCT=18 / provenance_families=7`
- Persistence: `PASS / eligible=18 / blocked=18 / success=0 / failure=0 / fabricated_memory_ids=0`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`

## Delta central

INV-156 ferme la branche `intermédiaire/consultant/commission -> avantage illicite -> décideur/procédure -> assistance/traitement favorable -> contrat` sur plusieurs familles indépendantes, tout en réfutant les raccourcis `agent=corruption`, `commission=pot-de-vin` et `offset=corruption`. Airbus, Alstom et Siemens documentent des tiers utilisés comme conduits de paiements corruptifs liés à l'obtention d'affaires ou de marchés ; l'EPPO ferme un cas distinct de trafic d'influence/abus d'autorité dans une procédure d'achat. Le BIS fournit le contrôle négatif décisif sur les offsets, mécanismes industriels formels et reportables.

## Registre causal certifié

- `intermediary/consultant -> corrupt payment -> official assistance/business winning` = **SUPPORTED / case-specific**.
- `official manipulation/trading in influence -> bidder privilege -> procurement effect` = **SUPPORTED / case-specific**.
- `agent or commission -> corruption` = **REFUTED as automatic rule**.
- `offset -> corruption` = **REFUTED as automatic rule**.
- `payment linked to award -> but-for causation of award` = **PARTIAL / NOT GENERALIZABLE**.
- `offset-specific misconduct independent of bribe/intermediary` = **UNRESOLVED / RECHECK**.
- `representative France/EU denominator` = **GAP**.

## RENARD

`NO` — generic additional bribery cases would be cumulative. Material upgrade requires an offset-specific primary case or representative denominator/causal design.

## Transition attendue

`INV-156 ACTIVE_PRECOLLECTION -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, then mechanism-first reclassification. Do not create an autonomous offset investigation without a falsifiable primary case.
