---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-047"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-047

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-1108-eu-sanctions-coercion`
- Deliverable: `INV-047_INVESTIGATION.md`
- Deliverable SHA-256: `2778bb3a1ff721ca2bf823ae5464a93be8bd60dae063b329e9c727f336066051`
- Corpus runtime: `QRY=22 / SRC=18 / FCT=27 / provenance_families=4`
- Persistence: `PASS / eligible=27 / blocked=27 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-047 ferme le mécanisme générique des sanctions européennes au niveau où la preuve est la plus robuste : acte juridique -> obligation d'un intermédiaire -> restriction d'accès, de transaction, de commerce, d'actifs ou de diffusion -> coût/contrainte proximal mesurable. Sur la Russie, les sanctions sont associées à une contraction majeure des échanges, à l'effondrement de la part du pétrole russe dans les importations de l'UE, à l'immobilisation de plus de 210 Md EUR d'actifs de banque centrale et à des pertes de revenus ciblés ; les travaux contre-factuels sur 2014-2019 confirment un effet commercial réel mais aussi substitution, détournement et hétérogénéité d'application. Ces effets ne ferment pas sanctions -> changement de politique : la guerre et les mesures se poursuivent en 2026. Sur l'information, le règlement 2022/350 ferme directement interdiction de diffusion/licences RT-Sputnik -> restriction de distribution, validée en contrôle juridictionnel, mais aucune mesure causale d'exposition, croyance ou persuasion n'est identifiée. La Biélorussie fournit un contrôle négatif/mixte : quelques libérations coexistent avec au moins 863 prisonniers politiques et une répression persistante, sans attribution causale aux sanctions. Le JCPOA ferme en revanche une séquence de conditionnalité multilatérale : engagements nucléaires vérifiés -> levée coordonnée de sanctions, sans identifier la contribution marginale de l'UE seule. Le modèle soutenu est donc : sanctions = contrainte juridique/proximale souvent mesurable ; coercition politique terminale = effet distinct, hétérogène et rarement attribuable sans design causal spécifique.

## Registre causal certifié

- `EU legal act/listing/restriction -> obligation on EU operator -> denied transaction/access/distribution` = **SUPPORTED** — contrainte juridique directe, pas conformité politique de la cible.
- `Russia trade/energy restrictions -> lower sanctioned bilateral trade and EU Russian-oil dependence` = **SUPPORTED** — magnitude co-déterminée par guerre, boycotts, contre-sanctions et diversification.
- `asset freezes/revenue restrictions -> financial cost/resource constraint` = **SUPPORTED** — coût != changement de politique.
- `economic cost -> Russian policy reversal/war termination` = **UNRESOLVED** — pas de contre-factuel isolant les sanctions ; politique ciblée persistante en 2026.
- `RT/Sputnik restriction -> lower legal distribution availability in EU` = **SUPPORTED** — distribution != croyance/persuasion.
- `EU Belarus sanctions -> prisoner release/end repression` = **UNRESOLVED** — résultat mixte et attribution non fermée.
- `multilateral sanctions pressure/relief -> JCPOA commitments -> verified nuclear measures -> relief` = **SUPPORTED** au niveau de la conditionnalité multilatérale — contribution UE seule non isolée.

## Gaps matériels certifiés

- **CAUSALITY** — identifier un effet sanction-spécifique sur une décision politique russe, au-delà des coûts économiques et des facteurs militaires/diplomatiques concurrents.
- **INFORMATION_EFFECT** — mesurer `restriction RT/Sputnik -> exposition -> croyance/comportement` avec un design causal.
- **CAUSALITY** — attribuer une libération ou une décision répressive biélorusse à une modification précise des sanctions plutôt qu'à la diplomatie ou d'autres pressions.
- **IMPLEMENTATION** — mesurer le dénominateur réel de contournement/substitution par rapport aux flux légalement interdits.

## RENARD

`NO`

Recherche générique supplémentaire cumulative. Réouvrir uniquement sur un design causal décisionnel sanction -> comportement, un jeu de données fournisseur/audience pour la chaîne informationnelle, ou un dossier d'exécution permettant de quantifier contournement et effet net.

## Reclassification

Impact direct : `NONE`.

## Transition attendue

`INV-047 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant full-pool.
