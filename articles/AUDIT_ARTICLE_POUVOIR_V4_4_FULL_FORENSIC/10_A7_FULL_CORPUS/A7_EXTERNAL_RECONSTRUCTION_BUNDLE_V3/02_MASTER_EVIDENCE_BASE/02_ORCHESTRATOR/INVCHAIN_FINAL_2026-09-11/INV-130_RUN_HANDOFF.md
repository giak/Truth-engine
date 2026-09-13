---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-130"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-038;INV-131;INV-147"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-130

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-1722-morocco-influence-france`
- Deliverable: `INV-130_INVESTIGATION.md`
- Deliverable SHA-256: `78f3f859ae58d558c36aede8dbe14ffbe077c788737b9151df7d9b42b0286c32`
- Corpus runtime: `QRY=20 / SRC=10 / FCT=20 / provenance_families=5`
- Persistence: `PASS / eligible=20 / blocked=20 / success=0 / failure=0 / fabricated_memory_ids=0 / reason=MNEMO_UNAVAILABLE`

## Delta central

Le corpus ferme plusieurs mécanismes marocains en France sans les fusionner en un système unique. Le droit français distingue explicitement influence étrangère légitime et ingérence. Des canaux étatiques marocains de recrutement, financement, formation et désignation d'imams ferment une chaîne institutionnelle vers l'organisation du culte en France, mais pas une chaîne diaspora -> relais politique ou électoral. Les groupes d'amitié franco-marocains ont publiquement et de façon répétée plaidé pour un soutien français accru au plan marocain d'autonomie du Sahara avant le changement de position français de 2024 ; la séquence et l'alignement sont établis, pas la contribution causale marginale du groupe à la décision présidentielle. Pegasus ferme plus fortement une chaîne de ciblage clandestin de responsables français liée au Maroc que toute arête aval de levier politique. Moroccogate fournit un comparateur matériel de corruption/tasking allégué, mais les pièces publiques inspectées ne ferment pas conjointement paiement/tasking DGED et décision européenne causée. Aucune architecture coordonnée transversale ni effet électoral général n'est établi.

## Highest supported influence/effect edge

- `État/accords marocains -> recrutement/financement/formation/désignation d'imams -> présence institutionnelle religieuse en France` = **SUPPORTED** ; présence/influence religieuse != relais politique de la diaspora.
- `contact institutionnel marocain -> groupe d'amitié parlementaire français -> plaidoyer répété -> position française convergente sur le Sahara` = **SUPPORTED jusqu'à la séquence/alignement** ; contribution causale marginale à la décision = **UNRESOLVED**.
- `client Pegasus lié au Maroc -> ciblage technique de responsables français` = **SUPPORTED_BOUNDED** ; `-> information acquise -> levier -> changement de politique` = **UNRESOLVED**.
- `acteur marocain/intelligence -> intermédiaire/paiement/tasking -> acteur UE -> décision favorable` = **UNRESOLVED** dans le corpus public inspecté.

## Material gaps / contradictions

- **POLICY_FOOTPRINT** — aucun dossier interne français ne permet d'isoler la contribution du plaidoyer parlementaire à la décision présidentielle sur le Sahara.
- **EFFECT** — aucune chaîne fermée `exposition/accès/surveillance -> changement de comportement, vote ou décision` avec contrefactuel crédible.
- **RESPONSIBILITY** — Moroccogate ne ferme pas publiquement dans ce run une chaîne finale authentifiée DGED -> paiement/tasking -> décision causée.
- **DIASPORA/TASKING** — influence sur l'organisation du culte ne démontre ni coordination politique générale des citoyens d'origine marocaine ni tasking électoral.

## Contradictory review / causal ceiling

Les mécanismes ouverts de diplomatie, coopération religieuse et représentation d'intérêts doivent rester séparés des opérations clandestines ou corruptives. L'origine marocaine d'un acteur ne prouve aucun lien étatique ; la chronologie plaidoyer -> décision ne prouve pas causalité ; ciblage Pegasus ne prouve pas exploitation politique de l'information ; soupçon judiciaire ne vaut pas responsabilité finale. Le plafond causal reste donc élevé sur l'existence de plusieurs canaux d'influence et de ciblage, faible sur leur effet politique terminal et nul sur l'hypothèse d'un commandement transversal unique.

## RENARD

`NO` — les upgrades matériels exigent désormais des pièces internes de décision française, des éléments judiciaires/tasking publics plus définitifs ou des designs causaux/électoraux. Une collecte générique supplémentaire sur « l'influence marocaine » serait cumulative et favoriserait la fusion abusive de mécanismes non isomorphes.

## New ideas triaged

Aucun nouveau bundle actor-first. Alimenter `INV-147` avec des cas appariés par mécanisme/niveau de preuve ; utiliser `INV-131` comme contrôle Algérie suffisamment isomorphe ; alimenter `INV-038` uniquement après fermeture de sa dernière dépendance.

## Mechanical transition expected

`INV-130 TE_ACTIVE -> CLOSED`; `truth_engine=DELIVERY_PASS_R3P1`; `renard=NO`; `result_path=INV-130_RUN_HANDOFF.md`; semantic reclassification impact bounded to `INV-038;INV-131;INV-147`.
