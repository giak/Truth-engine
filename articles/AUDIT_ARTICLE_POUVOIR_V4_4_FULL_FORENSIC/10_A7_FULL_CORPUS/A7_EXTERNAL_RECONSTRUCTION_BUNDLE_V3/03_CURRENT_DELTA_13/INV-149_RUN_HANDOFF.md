# RUN_HANDOFF — INV-149

Status: **CLOSED / DELIVERY_PASS_R3P1**  
Run: `20260911-1805-finance-opaque-beneficiaires-effectifs`  
Deliverable SHA-256: `0ce2347657b799ac2ff06cf2875048f74390162b701b8dbcc6cdc5285930a3b5`  
Runtime: `QRY=12 / SRC=12 / FCT=17 / provenance_families=3`  
Verifier: `PRE=PASS / DELIVERY=PASS / tests=140 passed, 2 skipped`

## Delta central

INV-149 ferme un mécanisme que la taxonomie précédente sous-modélisait : l'opacité financière peut servir d'**infrastructure de séparation d'attribution** entre le détenteur juridique, le bénéficiaire effectif, le nominateur, la source économique des fonds et le principal politique. Elle ne devient cependant une chaîne d'influence que si des preuves indépendantes reconnectent ces couches à un bénéficiaire/intermédiaire politique puis à un acte identifiable.

Le cas Azerbaïdjan/PACE constitue le contrôle positif le plus dense : véhicules sociétaires opaques et flux transfrontaliers ont alimenté des acteurs ou structures politiques, avec des activités favorables à l'Azerbaïdjan documentées. Les décisions allemandes Lintner (2025) et Fischer (2026) renforcent le mécanisme `paiement -> conduite parlementaire favorable`, tout en conservant le statut non définitif signalé par les communiqués consultés.

## Registre causal certifié

- `legal holder != beneficial owner != nominator != political principal` = **SUPPORTED**.
- `shell / nominee -> concealment capability` = **SUPPORTED**, avec usages légitimes possibles.
- `professional gatekeeper -> facilitation` = **SUPPORTED AS CAPABILITY**, pas complicité automatique.
- `opaque vehicle -> transfer -> political beneficiary/intermediary -> political act` = **SUPPORTED CASE-SPECIFICALLY** pour la lignée Azerbaïdjan/PACE.
- `money laundering / suspicious structure -> political influence` = **REFUTED AS AUTOMATIC INFERENCE**.
- `beneficial owner -> political commanditaire` = **REFUTED AS AUTOMATIC INFERENCE**.
- prévalence France/UE de ces chaînes = **GAP / SCOPE**, aucun dénominateur représentatif.

## Réparation runtime

Les 12 consultations directes avaient été journalisées comme `WEB` alors que le contrat canonique exige `FETCH` pour une source inspectée et mappée aux faits. La réparation a modifié uniquement ce mode de journalisation, sans changer URLs, sources, faits ou conclusions. Les gates PRE et DELIVERY ont ensuite passé le kernel.

## Reclassification

Le gap le plus discriminant aval n'est plus seulement « qui est derrière l'argent ? », mais **quels droits de contrôle l'acquisition ou la participation donne-t-elle sur un actif stratégique, et ces droits sont-ils exercés comme levier ?**

`NEXT = INV-150 — Investissements stratégiques, acquisitions et fonds souverains`.
