---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-046"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-040"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-046

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-2310-chat-control-eudi`
- Deliverable: `INV-046_INVESTIGATION.md`
- Deliverable SHA-256: `b3d1aaf1f5ed6f02bd954b741e4091e82c95df6f06797c5bf46d60a60ce607d1`
- Corpus runtime: `QRY=11 / SRC=8 / FCT=13 / provenance_families=8`
- Persistence: `PASS / eligible=13 / blocked=13 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-046 ferme un modèle borné : EUDI, QWAC/eIDAS et le régime CSA créent des capacités numériques réelles mais sectorielles ; les garde-fous d’EUDI et de sécurité navigateur sont explicites, le scanning CSA actuel est volontaire et temporaire, et aucun pont probant ne ferme aujourd’hui une architecture intégrée identité→communications→sanction politique. Le risque de mission creep reste conditionnel à l’implémentation et à des ponts futurs démontrables.

## Registre causal certifié

- `wallet EUDI -> authentification/attributs -> accès service` = **SUPPORTED** — Capacité d’authentification fermée; contrôle politique non inféré.
- `QWAC -> reconnaissance navigateur -> interception générale` = **UNRESOLVED** — Reconnaissance QWAC établie; MITM général non établi.
- `détection CSA -> contenu signalé -> action police/retrait` = **SUPPORTED** — Capacité actuelle bornée à la dérogation et aux choix fournisseurs.
- `EUDI + CSA + QWAC -> profil citoyen commun -> sanction politique` = **UNRESOLVED** — Convergence rhétorique/capacitaire ne ferme pas intégration système.

## Gaps matériels certifiés

- `CLM-001` / **CAUSALITY** — Aucun pont juridique/technique démontré ne relie EUDI, QWAC et détection CSA à une décision politique automatisée ou à un profil citoyen commun.
- `CLM-002` / **TEMPORAL** — Implémentations nationales concrètes et qualité des contrôles devront être auditées après déploiement.
- `CLM-003` / **CAUSALITY** — Une attaque ou émission abusive spécifique reste techniquement possible selon gouvernance PKI, mais elle n’est pas une autorisation générale établie par le texte inspecté.
- `CLM-004` / **TEMPORAL** — Texte permanent final non adopté; capacités obligatoires terminales non fixées.
- `CLM-005` / **TEMPORAL** — Le compromis final du cadre permanent peut encore diverger; position du Conseil et du Parlement ne sont pas identiques.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-040`.

## Transition attendue

`INV-046 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
