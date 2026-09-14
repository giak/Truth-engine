---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-162"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-163;INV-164;INV-165;INV-166;INV-167;INV-168;INV-169;INV-170;INV-171;INV-172"
updated: "2026-09-13"
---

# RUN_HANDOFF — INV-162

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260913-1340-voices-israel-civil-society-funding`
- Deliverable: `2026-09-13_13-40_voices-israel-civil-society-funding_INVESTIGATION.md`
- Deliverable SHA-256: `295819a632a55d10e65bc1a5ebc177da148eff662b29aa49cff39d229519f41a`
- State ID: `sha256:199ce4e5940dcc69ae2c8b246dfe42d049a03649248b9fadf758540eef96392d`
- Runtime: `QRY=30 / SRC=6 / FCT=16 / provenance_families=4`
- PRE gate: `PASS`
- DELIVERY gate: `PASS`
- Tests: `140 passed / 2 skipped`
- Persistence: `PASS / eligible=16 / attempted=0 / success=0 / failure=0 / blocked=16 / MNEMO_UNAVAILABLE`

## Delta central

INV-162 ferme un niveau de relation plus fort que le simple financement : le mécanisme Voices of Israel documenté dans le RFP impose un **cofinancement 50/50, des objectifs préalables, des critères de sélection, des jalons, des justificatifs de dépenses et des rapports de performance avant paiement**. Cela soutient un `project-level tasking / monitoring` contractuel.

- `ministère israélien -> Voices -> cofinancement projet -> objectifs/jalons/rapports -> paiement` = **SUPPORTED**.
- `project funding -> commandement général de l'organisation bénéficiaire` = **NOT_ESTABLISHED**.
- ELNET est relié de manière **PARTIAL / PROVENANCE GAP** à un projet Voices visant des délégations/conférences pour décideurs européens : l'enquête inspectée rapporte la sélection, mais la page primaire Voices n'était plus directement récupérable au moment du run.
- Les publications ELNET ferment `organisation -> délégation -> exposition à responsables israéliens / briefings / demandes politiques` = **SUPPORTED** au niveau action/exposition.
- `Voices payment précis -> délégation française nommée` = **ALLOCATION GAP**.
- `financement/exposition -> persuasion -> comportement -> décision publique France/UE` = **CAUSALITY GAP**.

## Contrôles

- matching 50/50 != financement intégral par l'État ;
- contrôle contractuel d'un projet != gouvernance de l'organisation entière ;
- acteur-published material établit activité/intention, pas effet ;
- financement public étranger != ingérence clandestine par nature ;
- absence de ledger public != absence de financement.

## RENARD

`NO` — le résiduel matériel est identifié mais dépend d'un accès primaire actuellement non disponible : awards/portfolio Voices archivés, conventions et budgets projet France/UE. Une collecte générique supplémentaire serait cumulative. Réouvrir seulement sur pièce primaire/archivée permettant de fermer un bénéficiaire, un montant et un livrable.

## Reclassification impact

`INV-163..INV-172` — le run ajoute un mécanisme discriminant `funding -> project-level tasking` et doit reclasser les dossiers consacrés au seuil juridique de mandant étranger, aux policy footprints, à Bruxelles et aux contrôles négatifs.
