---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-155-RUN-HANDOFF"
status: "terminal"
updated: "2026-09-11"
inv_id: "INV-155"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
---

# RUN_HANDOFF — INV-155

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-2122-isds-economic-lawfare`
- Deliverable: `2026-09-11_21-22_isds-economic-lawfare_INVESTIGATION.md`
- Deliverable SHA-256: `3514dc90e0806d3c7b403207dec57dee5a0cd593d992afa1489f7ea06d3be1be`
- Runtime corpus: `QRY=16 / SRC=16 / FCT=17 / provenance_families=4`
- Persistence: `PASS / eligible=17 / blocked=17 / success=0 / failure=0 / MNEMO_UNAVAILABLE`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`

## Delta central

INV-155 ferme un mécanisme autonome mais plus borné que l'hypothèse « regulatory chill » forte. L'arbitrage investisseur-État peut créer une exposition budgétaire et procédurale réelle, conduire à des indemnisations ou règlements et contribuer à une adaptation de l'architecture des traités. En revanche, l'existence d'une menace ou d'une procédure ne prouve pas qu'une politique publique a été abandonnée ou modifiée à cause de cette pression.

Les cas Allemagne/Vattenfall et Pays-Bas/RWE-Uniper sont des contrôles négatifs matériels : contentieux et coûts sont réels, mais les politiques centrales de sortie du nucléaire et du charbon ne sont pas démontrées comme inversées par l'ISDS. Le cas Rockhopper rappelle qu'un award n'est pas un état terminal immuable : l'award a ensuite été annulé. L'UE a modifié son architecture juridique (fin des BIT intra-UE, retrait du TCE, accord d'interprétation intra-UE), mais le run n'attribue pas cette évolution à un seul investisseur ou dossier.

## Chaînes certifiées

- `ISDS claim -> legal/fiscal exposure -> litigation/settlement/compensation` = **SUPPORTED**.
- `Germany nuclear claim -> compensation settlement -> nuclear phaseout reversed` = **REFUTED**.
- `Netherlands coal claims -> government postpones/adjusts climate decisions` = **REFUTED by explicit government negative control**.
- `award -> durable final pressure` = **REFUTED as automatic rule**.
- `intra-EU arbitration conflict -> EU treaty/legal architecture adaptation` = **SUPPORTED / multi-causal**.
- `ISDS -> economic lawfare/ingérence` = **REFUTED as automatic equivalence**.
- `mere threat -> abandoned France/EU public-interest policy` = **GAP**.
- `representative France/EU chill prevalence/success rate` = **GAP**.

## Gardes

`claim != chill`; `cost != policy reversal`; `settlement != capitulation`; `award != durable terminal outcome`; `treaty reform != single-case causation`; `ISDS != economic lawfare`; `economic lawfare != ingérence`.

## RENARD

`NO` — les deux gaps restants exigent soit un dataset comparatif représentatif, soit des archives internes de décision permettant d'isoler une menace antérieure à un abandon de politique. Une collecte générique supplémentaire favoriserait le cherry-picking.

## Reclassification

- `ISDS_ARBITRATION_ECONOMIC_LAWFARE` -> `COVERED_BY_INV-155`, avec gap borné `threat-only chill / denominator` conservé en RECHECK.
- meilleur gap autonome restant -> `PROCUREMENT_OFFSETS_COMMISSIONS`.
