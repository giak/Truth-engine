---
trace_schema: "forensic-md/v1"
artifact_type: "proposed_run_contract"
status: "BACKLOG_PROPOSED"
inv_id: "INV-161"
priority_hint: "P0"
bottleneck: "EFFECT"
dependencies: "INV-158; plus relevant prior runs"
---

# INV-161 — ELNET : voyages parlementaires et effet causal

OBJECT_QUESTION = Les voyages financés par ELNET sont-ils suivis d'un changement mesurable de positions publiques, au-delà de l'auto-sélection ?

SCOPE = France 2017-2026 : voyages, participants, discours/QE/amendements/votes avant-après, contrôles appariés.

FALSIFIER = Aucune différence robuste ; positions préexistantes expliquent les voyages.

GUARDS =
- identity != state relation
- funding != command
- access != adoption
- chronology != causality
- network overlap != coordination
- exposure != persuasion
- operation != outcome
- absence_of_evidence != evidence_of_guilt

ICEBERG =
OMISSION_SELECTIVE | CATEGORY_TRICK | SHADOW_POPULATION | DENOMINATOR_MANIPULATION |
TIMEFRAME_CHERRY | PROXY_SUBSTITUTION | COMPARATIVE_ABSENCE | METHODOLOGY_OPACITY

OUTPUT = Truth Engine investigation only; no article transformation inside the run.
