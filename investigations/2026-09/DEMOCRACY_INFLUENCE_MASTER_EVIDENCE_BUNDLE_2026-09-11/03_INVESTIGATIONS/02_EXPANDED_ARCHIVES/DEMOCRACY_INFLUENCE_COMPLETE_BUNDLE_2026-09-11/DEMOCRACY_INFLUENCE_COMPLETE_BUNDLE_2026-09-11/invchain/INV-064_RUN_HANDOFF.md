---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-064"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-065"
updated: "2026-09-09"
---

# RUN_HANDOFF — INV-064

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260909-2143-pr-strategic-communication-market`
- Deliverable: `INV-064_INVESTIGATION.md`
- Deliverable SHA-256: `adb572ccd938c0611901099018caf5da6ba9a8ea92de86c784b99be3040935d1`
- Corpus runtime: `QRY=28 / SRC=14 / FCT=28 / provenance_families=5`
- Persistence: `PASS / eligible=28 / blocked=28 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-064 establishes that the professional PR/public-affairs market is an operational influence channel, not merely a rhetorical label: HATVP records show named agencies converting client mandates into meetings, expertise, legislative suggestions, events and, in some declarations, online influence strategies. EU transparency rules treat such activity as a legitimate but accountable influence channel rather than proof of deception. The Monsanto case closes a stronger actor-specific chain from client to PR agencies/subcontractor to stakeholder mapping for glyphosate lobbying, while the CNIL sanction closes data-governance failures, not causal influence on the regulatory outcome. Bell Pottinger demonstrates that paid strategic communication can cross into unethical/divisive conduct, but does not establish prevalence in France/EU. Experimental evidence bounds downstream effect: persuasion and framing are real in some contexts but heterogeneous, often weak on behavior, and poorly predictable from message or exposure alone. General client -> agency -> influence activity is established; generalized agency -> opinion/behavior/policy outcome is not.

## Registre causal certifié

- `client -> cabinet PR/public affairs -> réunion, expertise, suggestion, événement ou stratégie influence -> décideur/public ciblé` = **SUPPORTED** — La chaîne de prestation et exposition est documentée; adoption, persuasion ou comportement ne suivent pas automatiquement.
- `client -> agence -> sous-traitant -> cartographie/segmentation parties prenantes -> infrastructure de ciblage lobbying` = **SUPPORTED** — Actor-specific Monsanto/Fleishman-Hillard/Publicis; ne prouve ni illégalité intrinsèque du mapping ni effet sur la décision glyphosate.
- `prestation stratégique rémunérée -> contenu trompeur/clivant ou pratique non éthique -> environnement narratif` = **SUPPORTED** — Démontré comme possibilité par Bell Pottinger, comparateur hors France/UE outcome; aucune prévalence transférable.
- `message, publicité ou cadrage -> exposition -> attitude/persuasion/comportement` = **SUPPORTED** — Effets contextuels et hétérogènes; comportement souvent nul/faible et prédiction ex ante limitée.
- `activité cabinet PR en France/UE -> changement opinion/comportement -> décision publique ou résultat électoral comme cause marginale` = **UNRESOLVED** — Pas de dénominateur exposition ni design contrefactuel liant un cabinet français/UE à un résultat politique précis.

## Gaps matériels certifiés

- `CLM-004` / **CAUSALITY** — Aucune estimation contrefactuelle ou trace décisionnelle ne ferme le lien cartographie/ciblage -> renouvellement du glyphosate.
- `CLM-006` / **PREVALENCE** — Le corpus ne mesure pas la fréquence de tels franchissements dans les cabinets actifs en France/UE.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-065`.

## Transition attendue

`INV-064 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
