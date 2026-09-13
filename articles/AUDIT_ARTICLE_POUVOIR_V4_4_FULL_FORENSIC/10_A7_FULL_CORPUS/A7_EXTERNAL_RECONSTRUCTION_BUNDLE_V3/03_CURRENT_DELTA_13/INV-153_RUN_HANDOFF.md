---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-153"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-153

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-2033-dette-credit-aide-conditionnalite`
- Deliverable: `2026-09-11_20-33_dette-credit-aide-conditionnalite_INVESTIGATION.md`
- Deliverable SHA-256: `6d0cfc703d0f5688743c96282d7fb91f4eccc724cf56f265ef550ca225e46a4d`
- Runtime: `QRY=14 / SRC=14 / FCT=17 / provenance_families=3`
- PRE verifier: `PASS` after one trace-only repair on `CLM-010`
- DELIVERY verifier: `PASS`
- Persistence: `PASS / eligible=17 / attempted=0 / success=0 / failure=0 / blocked=17 / MNEMO_UNAVAILABLE`

## Delta central

INV-153 établit que la conditionnalité financière est un mécanisme autonome de pouvoir : une ressource peut être rendue conditionnelle à des actions, jalons, critères ou réformes sans passer par la persuasion. Le programme grec du MES ferme une chaîne particulièrement dense `financement -> conditions/MoU -> prior actions -> adoption de lois ou mesures -> évaluation de conformité -> tranche`. Le FMI et l'assistance macrofinancière de l'UE montrent que cette architecture est institutionnalisée au-delà du seul cas grec.

Le run réfute toutefois l'équivalence automatique `conditionnalité = coercition = ingérence`. La RRF française fournit un contrôle négatif : des paiements sont eux aussi déclenchés après réalisation de jalons et cibles, dans un cadre institutionnel accepté et co-gouverné. Le Pandemic Crisis Support du MES montre qu'un instrument de financement peut aussi comporter une condition étroite d'usage sans programme macroéconomique général.

La chaîne probatoire certifiée est donc :

`besoin de financement -> instrument/créancier -> condition explicite -> prior action/jalon -> conformité -> décaissement/non-décaissement -> réforme/adaptation -> effet`.

Le passage à `coercition` exige des éléments supplémentaires sur alternatives, asymétrie, coût du refus, menace ou non-décaissement crédible et adaptation sous contrainte. Le passage à `ingérence` exige encore une qualification distincte de mandat, origine, contrôle, légitimité et frontière institutionnelle affectée.

## Registre causal certifié

- `financement conditionnel -> actions/jalons -> conformité -> décaissement` = **SUPPORTED**.
- `MES Grèce -> prior actions/législation -> tranche` = **SUPPORTED**.
- `RRF France -> jalons/cibles -> versement` = **SUPPORTED** ; ne ferme pas coercition/ingérence.
- `IMF/MFA -> policy conditions -> phased disbursement` = **SUPPORTED**.
- `tout financement d'urgence -> large programme de réforme` = **REFUTED** par le contrôle Pandemic Crisis Support.
- `conditionnalité -> coercition/ingérence automatique` = **REFUTED**.
- `conditionnalité -> politique contraire aux préférences contrefactuelles de la cible` = **UNRESOLVED / case-specific**.

## Gaps matériels certifiés

- **COUNTERFACTUAL** : aucun design général n'isole la réforme qui aurait été absente sans condition financière.
- **DENOMINATOR** : aucun taux représentatif France/UE de politiques modifiées contre la préférence non contrainte de la cible.
- **CLASSIFICATION** : coercition et ingérence doivent être prouvées au-delà de l'existence de conditions.

## Transition

`INV-153 -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`.

Reclassifier `INV-152` et `INV-154`. Le meilleur test suivant doit privilégier un mécanisme de coercition économique où la condition politique n'est **pas formalisée contractuellement**, afin de départager pression informelle, mesure commerciale ordinaire et coercition attribuable.
