---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-127"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-024;INV-032"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-127

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-1143-soft-power-academic-cultural`
- Deliverable: `INV-127_INVESTIGATION.md`
- Deliverable SHA-256: `6eda01016b9dcb0151802b15416f90905bedb4b1b3f3ac633f9fe426935c2361`
- Corpus runtime: `QRY=24 / SRC=20 / FCT=29 / provenance_families=5`
- Persistence: `PASS / eligible=29 / blocked=29 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-127 ferme le mécanisme générique du soft power culturel et académique jusqu'aux couches réellement démontrables : budget/mandat -> programme -> exposition ou mobilité -> compétences, contacts, réseaux et parfois attitudes. La France finance explicitement une diplomatie culturelle d'influence ; Eiffel vise explicitement la formation de futurs décideurs étrangers et France Alumni entretient les liens à grande échelle. Erasmus+ ferme une infrastructure massive de mobilité et des effets robustes sur certains réseaux/compétences, mais les études longitudinales et pré-post sont contradictoires sur un effet uniforme d'identité européenne. Aucun footprint borné ne ferme bourse/exposition/affinité -> tasking, capture ou décision politique précise. La frontière avec l'ingérence reste institution-spécifique : affiliation étatique ou promotion culturelle ne suffisent pas ; il faut des propriétés supplémentaires de coercition, clandestinité, tromperie, corruption ou contrôle documenté. Le modèle soutenu est donc une infrastructure d'exposition et de relations aux effets hétérogènes, non une chaîne automatique d'alignement politique.

## Registre causal certifié

- `public budget/institutional mandate -> scholarship, institute, exchange or language programme -> participant/public exposure` = **SUPPORTED** — exposition != alignement.
- `academic/cultural programme -> repeated contact, skills and alumni/professional network formation` = **SUPPORTED** — réseau != coordination.
- `Erasmus mobility -> stronger European identity` = **UNRESOLVED** — résultats longitudinaux/pré-post contradictoires et sélection/ceiling effects.
- `international education mobility -> modest increase in environmental concern` = **SUPPORTED** dans un design observationnel borné — attitude != alignement politique général.
- `Eiffel scholarship -> future-decision-maker training + France Alumni retention infrastructure` = **SUPPORTED** au niveau architecture/intention — décision ultérieure non attribuée.
- `scholarship/cultural exposure or alumni affinity -> specific later policy decision favorable to sponsor state` = **UNRESOLVED** — aucun footprint participant -> décision ni contrefactuel crédible.
- `state-linked academic/cultural presence + coercive/covert/deceptive/corrupting control -> foreign interference risk/action` = **SUPPORTED** comme frontière de qualification — présence étatique/culturelle seule insuffisante.

## Gaps matériels certifiés

- **CAUSALITY** — identifier un participant/alumni nommé, son exposition au programme, une interaction ultérieure pertinente et une décision politique précise, avec contrôle des explications rivales.
- **CAUSALITY / SELECTION** — disposer d'un design Erasmus multi-pays plus fort contrôlant identité pré-traitement et auto-sélection pour estimer l'effet d'identité.
- **RESPONSIBILITY / CONTROL** — obtenir contrats, MOU, droits de gouvernance, instructions ou interventions authentifiées lorsqu'une institution culturelle/académique est qualifiée d'ingérence.

## RENARD

`NO`

Recherche générique supplémentaire cumulative. Réouvrir uniquement sur un footprint participant -> décision, un design causal de mobilité plus fort, ou des preuves authentifiées de contrôle institutionnel dans un cas d'ingérence alléguée.

## Reclassification

Impact direct : `INV-024`, `INV-032`.

## Transition attendue

`INV-127 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis REVIEW bornée des dossiers Chine/universités et Qatar/soft power avant sélection mécanique full-pool.
