---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-161"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-160;INV-162;INV-163;INV-164;INV-165;INV-166;INV-167;INV-168;INV-169;INV-170;INV-171;INV-172"
updated: "2026-09-13"
---

# RUN_HANDOFF — INV-161

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260913-1200-elnet-voyages-effet-causal`
- Deliverable: `2026-09-13_12-00_elnet-voyages-effet-causal_INVESTIGATION.md`
- Deliverable SHA-256: `6342536bb88762deb8c1dc95add623a20273f22b4a8a1e56e5f18a9c83985d78`
- State ID: `sha256:7eb930bffd3b0d96e54b4e23feab2102e8d1f9a014dfcc898054e4cbfa3ba298`
- Runtime: `QRY=39 / SRC=13 / FCT=16 / provenance_families=3`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`
- Persistence: `PASS / eligible=16 / attempted=0 / success=0 / failure=0 / blocked=16 / MNEMO_UNAVAILABLE`

## Delta central

INV-161 ferme solidement l'arête `ressources ELNET -> voyages parlementaires -> exposition structurée` et montre que l'intensité est matériellement élevée dans le registre public : 38 des 82 invitations à voyager déclarées sous la XVIIe législature au 1er décembre 2025 sont financées par ELNET. Des délégations antérieures documentent également des briefings politiques, sécuritaires et diplomatiques ainsi que des engagements ou intentions rapportés par l'organisateur.

Le run ne ferme pas l'arête décisive `voyage -> persuasion -> changement de comportement`. Deux confondants majeurs restent observables : **auto-sélection/pré-alignement** des parlementaires et **choc commun du 7-Octobre** pour les comportements 2023-2024. Plusieurs outputs congruents existent, mais ils ne permettent pas un effet causal représentatif sans panel longitudinal et contrôles appariés.

## Registre causal certifié

- `ELNET funding/resources -> parliamentary trip -> curated briefings/exposure` = **SUPPORTED**.
- `March 2023 delegation -> policy prompt/commitment -> specific later adopted output` = **PARTIAL / lineage not closed**.
- `ELNET trip -> changed parliamentary behavior -> policy outcome` = **GAP / CAUSAL_DESIGN**.
- `trip -> quid pro quo / Israeli-state tasking -> specific decision` = **NOT_ESTABLISHED**.
- `later congruent statements/votes -> proof of conversion by trip` = **REFUTED as automatic inference**.

## Contrôles / contradictions

- Des positions pro-Israël ou critiques de dossiers palestiniens sont observables chez certains participants avant leur voyage, ce qui matérialise le biais d'auto-sélection.
- Les outputs postérieurs à octobre 2023 sont fortement confondus par un choc politique exogène majeur.
- Les affirmations ELNET selon lesquelles les voyages ont « inspiré » ou produit des engagements sont des auto-déclarations de l'organisateur, pas une mesure indépendante de l'effet.
- Le statut HATVP `en propre` ne ferme aucune relation de tasking étatique général.

## Plafond causal

Le meilleur upgrade exige un dataset complet 2017-2026 : participant, date, sponsor, coût/prise en charge, parti, commission, groupe d'amitié, positions pré-traitement, questions/amendements/votes/prises de parole post-traitement, puis matched controls. Sans ce design, accumuler des cas congruents renforcerait surtout un biais de sélection.

## RENARD

`NO` — davantage d'anecdotes de voyages seraient cumulatives. Le résiduel est un **CAUSAL_DESIGN_GAP** qui exige un panel structuré, pas une recherche narrative supplémentaire.

## Reclassification impact

La valeur marginale se déplace vers les branches qui peuvent fermer `funding/tasking` par pièces primaires (`INV-160`, `INV-162`, `INV-166`), des policy footprints spécifiques (`INV-163`, `INV-168`) et les contrôles de symétrie (`INV-170/171`). `INV-169` reste très discriminant mais access-limited tant qu'aucune nouvelle piste primaire sur le sponsor de Rokh Solis n'apparaît.
