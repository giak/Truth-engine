---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-166"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "DONE"
reclass_impact: "INV-163;INV-164;INV-165;INV-167;INV-168;INV-169;INV-170;INV-171;INV-172"
updated: "2026-09-13"
---

# RUN_HANDOFF — INV-166

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260913-1504-foreign-influence-register-threshold`
- Deliverable: `2026-09-13_15-04_foreign-influence-register-threshold_INVESTIGATION.md`
- Deliverable SHA-256: `b9d4a3b7cfeea010149f0bd6dc4d2f5deba38febbad234c06fdcd6ce536b35a2`
- State ID: `sha256:4cce4c6f16b75f5b013ca27ecd043375a282edf519d793295fb48543db2fe089`
- Runtime: `QRY=7 / SRC=7 / FCT=16 / provenance_families=4`
- Semantic objects: `LED=4 / AXS=4 / CLM=8 / CAU=4 / CTRL=6 / ACT=4`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`
- Tests: `140 passed / 2 skipped`
- Persistence: `PASS / eligible=14 / blocked=14 / MNEMO_UNAVAILABLE`

## Delta central

INV-166 transforme la question vague « acteur étranger = influence étrangère déclarable ? » en test juridique à deux étages :

`relation qualifiante avec un mandant étranger` **ET** `action entrant dans le champ du régime`.

Résultats :

- `ordre / demande / direction / contrôle -> seuil juridique` = **SUPPORTED** ;
- `intermédiaire indirect -> champ possible du régime` = **SUPPORTED** ;
- `participation à une commande publique / échanges strictement prévus par le contrat -> exclusion de la branche entrée en communication` = **SUPPORTED / branch-specific, not blanket exemption** ;
- `MFA israélien -> 72 000 EUR -> ELNET Europe-Israel -> colloque au Sénat du 10/11/2025` = **SUPPORTED / bounded by prior-certified procurement evidence** ;
- `ELNET France -> organisateur déclaré de l'événement` = **SUPPORTED** ;
- `ELNET Europe-Israel -> mandat/sous-traitance/instruction -> ELNET France` = **UNRESOLVED / RESPONSIBILITY_GAP** ;
- `ELNET absent de la liste publique inspectée -> violation` = **NOT ESTABLISHED / automatic inference refuted**.

## RENARD

`DONE / NO_UPGRADE`.

Le delta ciblé n'a trouvé aucune pièce primaire publique fermant le pont entre les deux personnes morales pour l'événement du 10 novembre 2025. Le gap devient donc un résultat terminal borné, non une invitation à accumuler des mentions redondantes.

## Causal ceiling

Le niveau maximal supporté est :

`financement étatique spécifique -> entité ELNET Europe-Israel -> événement institutionnel français`

plus séparément :

`ELNET France -> organisation déclarée de l'événement`.

La chaîne suivante reste non fermée :

`MFA -> ELNET Europe-Israel -> mandat ELNET France -> action déclarable pour compte étranger -> obligation ARGOS/manquement`.

## Reclassification impact

`INV-163;INV-164;INV-165;INV-167;INV-168;INV-169;INV-170;INV-171;INV-172` — fermeture d'un test juridique transversal sur le portefeuille ICEBERG; les autres workstreams restent réutilisables. Les dossiers suivants doivent être recalculés en privilégiant désormais les policy footprints, les effets et les attributions qui peuvent dépasser ce plafond plutôt qu'une nouvelle collecte générique de relations.
