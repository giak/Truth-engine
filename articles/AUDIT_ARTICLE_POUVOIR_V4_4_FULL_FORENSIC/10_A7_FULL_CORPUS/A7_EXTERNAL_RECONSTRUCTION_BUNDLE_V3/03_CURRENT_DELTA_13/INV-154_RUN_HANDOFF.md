---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-154"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-154

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-2034-represailles-economiques-informelles`
- Deliverable: `2026-09-11_20-34_represailles-economiques-informelles_INVESTIGATION.md`
- Deliverable SHA-256: `8740ae245acedcfa6e254859508a908f9fb4cba2719d55bdea51f7de6edba068`
- Runtime: `QRY=16 / SRC=16 / FCT=20 / provenance_families=2`
- PRE verifier: `PASS` after trace-only repair on `CLM-003` and `CLM-011`
- DELIVERY verifier: `PASS`
- Persistence: `PASS / eligible=20 / attempted=0 / success=0 / failure=0 / blocked=20 / MNEMO_UNAVAILABLE`

## Delta central

INV-154 établit qu'une coercition économique informelle peut modifier l'espace des choix sans contrat, MoU ou prise de contrôle. La chaîne minimale certifiée est `demande politique -> mesure/menace attribuable -> pression matérielle -> adaptation -> concession/résistance -> effet`. La qualification exige cependant un objectif politique et une attribution; un dommage commercial ou une mesure antidumping ne suffisent pas.

Lituanie-Chine ferme le mieux `demande -> mesures attribuées par l'UE -> coût`, mais réfute `reprise du commerce -> capitulation` : en 2026, la Lituanie continue d'utiliser officiellement le nom Taiwanese Representative Office et approfondit sa coopération avec Taiwan. THAAD ferme une pression économique substantielle avec attribution détaillée partiellement contestée, mais le déploiement central n'a pas été inversé. Australie-Chine ferme une large perturbation commerciale et un lien politique, sans fermer une unique chaîne `demande précise -> concession précise`.

## Registre causal certifié

- `trade harm -> coercion` = **REFUTED AS AUTOMATIC EQUIVALENCE**.
- `political demand + attributable economic measure/threat + material pressure -> economic coercion` = **SUPPORTED**.
- `coercion exercised -> requested political concession` = **CASE-SPECIFIC / NOT GENERALLY ESTABLISHED**.
- `measure removed / trade resumed -> target capitulated` = **REFUTED**.
- `formal trade remedy -> coercion` = **REFUTED AS AUTOMATIC EQUIVALENCE**.

## Gaps matériels certifiés

- **ATTRIBUTION** : les mesures informelles ne ferment pas toujours chaque ordre administratif ou tasking individuel.
- **COUNTERFACTUAL** : le changement politique causé marginalement par la pression reste case-specific.
- **DENOMINATOR** : aucun taux représentatif de succès de la coercition économique informelle.

## Transition

`INV-154 -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`.

Reclassifier les gaps restants. Le prochain dossier doit éviter sanctions/debanking déjà couverts par INV-124 et isoler le mécanisme transfrontalier de juridiction/rails financiers.
