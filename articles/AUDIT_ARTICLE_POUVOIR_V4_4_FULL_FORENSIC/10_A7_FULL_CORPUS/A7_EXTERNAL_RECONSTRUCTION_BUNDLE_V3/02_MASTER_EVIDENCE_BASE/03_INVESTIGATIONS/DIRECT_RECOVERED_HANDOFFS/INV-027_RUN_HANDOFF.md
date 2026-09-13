---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-027"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-027

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-1003-elnet-france-lobbying`
- Deliverable: `INV-027_INVESTIGATION.md`
- Deliverable SHA-256: `694e8094ae1fa158d36e180f7566411773974c76715424fa6ba265c2d36c7227`
- Corpus runtime: `QRY=19 / SRC=16 / FCT=26 / provenance_families=4`
- Persistence: `PASS / eligible=26 / blocked=26 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-027 établit ELNET France comme un dispositif déclaré et professionnalisé de représentation d'intérêts : dépenses HATVP de 100 à 200 k€ par an de 2021 à 2025, trois personnes dédiées, objectifs législatifs et diplomatiques explicites, événements et voyages parlementaires dont plusieurs prises en charge sont confirmées par les déclarations de l'Assemblée nationale. Ces dispositifs ferment la chaîne ressources -> voyage/événement/rencontre -> accès/exposition de responsables publics et fournissent une capacité d'agenda. Ils ne ferment pas voyage -> position/vote ni lobbying -> décision : aucun footprint borné n'isole une contribution ELNET comme cause d'une clause ou d'un vote, la HATVP déclare les intérêts représentés en propre et le financement étatique précis identifié par INV-026 concernait un événement ELNET Europe, pas un tasking général d'ELNET France. Le contre-exemple le plus discriminant est 2025 : ELNET déclarait vouloir empêcher la reconnaissance française de l'État palestinien, mais la France l'a reconnue le 22 septembre 2025. Accès et tentative d'influence sont donc établis ; contrôle/capture et effet politique marginal ne le sont pas.

## Registre causal certifié

- `ELNET resources/lobbying -> trips/events/meetings -> repeated parliamentary access/exposure` = **SUPPORTED** — Access/exposure only, not behavior change.
- `declared objective + suggestions/correspondence/events -> opportunity to shape policy agenda` = **SUPPORTED** — Intent/opportunity are not adoption.
- `ELNET trip/contact -> participant position/vote -> adopted decision` = **UNRESOLVED** — No causal identification.
- `Israeli-state tasking -> ELNET France general program -> French political action` = **UNRESOLVED** — Specific prior event funding cannot generalize.
- `ELNET anti-recognition lobbying -> French Palestine-recognition decision` = **UNRESOLVED** — Observed outcome opposed declared objective.
- `US Friends resources -> direct ELNET France financing -> lobbying capacity` = **UNRESOLVED** — US scale does not identify French transfers.

## Gaps matériels certifiés

- `CLM-002` / **CAUSALITY** — Access does not identify changed vote or decision.
- `CLM-003` / **CAUSALITY** — Intent does not establish success or control.
- `CLM-004` / **CAUSALITY** — No versioned contribution-to-text trace or counterfactual isolates marginal effect.
- `CLM-005` / **RESPONSIBILITY** — Own-account declaration and no authenticated general tasking record; prior INV-026 had only specific ELNET Europe transaction funding.
- `CLM-006` / **CAUSALITY** — The 2025 Palestine-recognition objective failed at final policy outcome.
- `CLM-007` / **RESOURCE_FLOW** — No direct transfer record to French entity obtained.

## RENARD

`NO`

## Reclassification

Impact direct : `NONE`.

## Transition attendue

`INV-027 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
