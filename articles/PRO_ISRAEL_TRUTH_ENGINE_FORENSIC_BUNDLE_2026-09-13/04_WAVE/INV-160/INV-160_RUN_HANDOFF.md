---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-160"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "DONE"
reclass_impact: "INV-162;INV-163;INV-164;INV-165;INV-166;INV-167;INV-168;INV-169;INV-170;INV-171;INV-172"
updated: "2026-09-13"
---

# RUN_HANDOFF — INV-160

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260913-1303-elnet-finance-topology`
- Deliverable: `2026-09-13_13-03_elnet-finance-topology_INVESTIGATION.md`
- Deliverable SHA-256: `1c1f10fb424bd5ee03ccd2ba3157c5b5269c0b784a58af604129f89429627908`
- State ID: `sha256:73754fb801af6093904024ee2f1fcc2f86f8d921c0cbb153721ba151657c5da9`
- Runtime: `QRY=15 / SRC=6 / FCT=16 / provenance_families=4`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`
- Tests: `140 passed / 2 skipped`
- Persistence: `PASS / eligible=16 / attempted=0 / success=0 / failure=0 / blocked=16 / MNEMO_UNAVAILABLE`

## Delta central

INV-160 ferme une topologie financière transnationale ELNET sans transformer automatiquement le financement en commandement.

- `donateurs/fondations privées -> Friends of ELNET US -> affiliés étrangers` = **SUPPORTED**.
- `Friends of ELNET -> ELNET France` = **SUPPORTED**, avec **1 034 210 USD** de grant déclaré en 2024.
- `grants étrangers Friends of ELNET -> formation de dirigeants européens / séminaires / débats / study trips` = **SUPPORTED** au niveau programme.
- `ELNET France -> opération française de représentation d'intérêts substantielle` = **SUPPORTED** par la HATVP.
- `grant US -> action HATVP française nommée` = **ALLOCATION / CAUSALITY GAP**.
- `Israeli MFA -> 72 000 EUR -> ELNET Europe-Israel -> événement au Sénat français en 2025` = **SUPPORTED / case-specific**.
- `financement étranger -> tasking général d'ELNET France -> décision française` = **NOT_ESTABLISHED**.

Le différentiel entre le grant américain vers ELNET France et les dépenses HATVP ne peut pas être interprété comme du lobbying caché : les deux chiffres couvrent des périmètres comptables et réglementaires différents.

## RENARD borné

`DONE`.

Le delta post-certification `INV-160_RENARD_DELTA.md` a trouvé un **lead documentaire matériel** relatif à un apparent financement public israélien direct d'ELNET France en 2020 (`Safe & Smart City Conference`, ordre `4501854883`, 37 664 EUR / 139 454,73 NIS).

Ce lead n'est **pas** incorporé au FINAL certifié d'INV-160 : la copie inspectée est un miroir média d'un apparent export gouvernemental et nécessite une authentification de provenance avant promotion en FACT.

## Plafond causal

Le corpus public actuel ferme des flux et quelques restrictions de programme, mais pas la chaîne générale :

`financeur étranger -> clause/tasking -> action française nommée -> delta de décision -> outcome contrefactuel`.

Pour la fermer, il faut des conventions de grant, comptes analytiques, livrables, factures ou contrats projet-spécifiques.

## Reclassification impact

`INV-162..172` — le delta affecte directement les branches funding/tasking, transparence, policy footprint, attribution et symétrie. Un run `INV-173` est proposé dans le RENARD mais n'est pas injecté à chaud dans le registre pendant la transaction de clôture.
