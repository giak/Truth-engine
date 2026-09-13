---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-017"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-123"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-017

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-1022-cambridge-analytica-targeting`
- Deliverable: `INV-017_INVESTIGATION.md`
- Deliverable SHA-256: `fcd2e264395613a7141a58d67e47100691a28b7d916e8e4932c96101266e1158`
- Corpus runtime: `QRY=19 / SRC=16 / FCT=26 / provenance_families=4`
- Persistence: `PASS / eligible=26 / blocked=26 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-017 ferme la chaîne amont Cambridge Analytica sans valider le récit d'une machine électorale dont l'effet serait démontré. FTC et ICO établissent collecte GSR/Facebook à grande échelle, génération de scores de personnalité, appariement avec des fichiers électoraux et usage pour des services de profilage/ciblage. Les paiements FEC et témoignages ferment une participation matérielle aux campagnes américaines. Les travaux académiques confirment qu'inférer des traits depuis des traces numériques et modifier certains comportements par ciblage psychologique est techniquement plausible, mais ces résultats ne démontrent ni l'exactitude des modèles Cambridge Analytica pour chaque électeur, ni l'exposition, la persuasion ou le vote. Pour Trump, l'usage psychographique précis reste non résolu : capacité Ripon/OCEAN et témoignages existent, mais Nix l'a nié et Vickery n'a pas pu vérifier un déploiement direct. Aucun design crédible ne mesure l'effet marginal de Cambridge Analytica sur le résultat de 2016. Leave.EU sert de contrôle négatif : le régulateur n'a trouvé qu'une phase exploratoire, sans prestation de campagne.

## Registre causal certifié

- `Facebook/GSR data -> personality scoring + voter-file matching -> profiling/targeting capability` = **SUPPORTED** — capacité et pipeline, pas précision individuelle garantie.
- `campaign procurement/use -> analytics/targeting services` = **SUPPORTED** — participation matérielle, pas effet électoral.
- `psychographic targeting capability -> actual Trump psychographic ad delivery` = **UNRESOLVED** — preuves contradictoires/partielles ; absence de trace segment -> creative -> impression.
- `psychological matching -> clicks/purchases in nonpolitical field experiments` = **SUPPORTED** — ne se transporte pas automatiquement au vote.
- `political microtargeting -> persuasion/vote change` = **UNRESOLVED** — ciblage et exposition sont imparfaits ; pas de design causal CA spécifique.
- `Cambridge Analytica services -> changed 2016 election outcome` = **UNRESOLVED** — aucun contrefactuel crédible identifié.
- `Cambridge Analytica -> Leave.EU referendum campaign execution` = **REFUTED** — relation exploratoire sans prestation de campagne établie par le régulateur.

## Gaps matériels certifiés

- `EXPOSURE` — journaux authentifiés reliant segment psychographique, creative, achat, livraison et impression individuelle.
- `CAUSAL_ATTRIBUTION` — design indépendant reliant exposition politique au changement d'attitude/comportement/vote.
- `COUNTERFACTUAL` — estimation crédible de l'effet marginal sur le résultat électoral de 2016.
- `RESPONSIBILITY/DEPLOYMENT` — preuve directe du déploiement psychographique Trump, distincte de la capacité technique disponible.

## RENARD

`NO`

Réouvrir seulement sur : logs Trump/Facebook authentifiés fermant `segment -> creative -> delivery -> exposure`; expérience/natural experiment politique indépendant lié au ciblage CA ; ou nouveaux contrats/factures/assets Leave.EU contredisant le constat du régulateur.

## Reclassification

Impact direct : `INV-123` uniquement. INV-017 apporte une preuve matérielle sur la chaîne plateforme/données -> profilage/ciblage politique, mais ne modifie pas directement les contrats plus généraux de propagande, médias ou indignation.

## Transition attendue

`INV-017 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
