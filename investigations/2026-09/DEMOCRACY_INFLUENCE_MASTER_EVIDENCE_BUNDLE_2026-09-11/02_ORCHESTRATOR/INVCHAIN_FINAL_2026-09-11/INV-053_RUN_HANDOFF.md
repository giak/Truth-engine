---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-053"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-052"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-053

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-1027-migration-ngo-funding`
- Deliverable: `INV-053_INVESTIGATION.md`
- Deliverable SHA-256: `354d2135419166a77df2faae2981f0641bbb25342ee1aa4fb4ea371dd47301a2`
- Corpus runtime: `QRY=10 / SRC=10 / FCT=13 / provenance_families=6`
- Persistence: `PASS / eligible=13 / blocked=13 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-053 sépare trois niveaux : (1) les financements publics, européens et privés créent des capacités opérationnelles substantielles ; (2) certaines organisations financées, notamment France Terre d'Asile, ECRE et PICUM, mènent parallèlement un plaidoyer explicite et disposent de canaux d'accès institutionnel ; (3) aucun cas échantillonné ne ferme une chaîne `financeur -> tasking politique -> ONG -> décision capturée`. Le contrôle SOS Méditerranée montre au contraire une séparation juridiquement contrôlée entre financement humanitaire et activité politique. Le plafond probatoire est donc : financement != tasking ; assistance humanitaire != lobbying ; lobbying != capture ; accès/output != effet causal de politique publique.

## Registre causal certifié

- `financement public -> capacité opérationnelle -> hébergement/accompagnement/intégration` = **SUPPORTED** — Chaîne capacité/service fermée; aucun tasking inféré.
- `financement public -> dépendance -> tasking/lobbying -> décision publique` = **UNRESOLVED** — Coexistence financement+plaidoyer établie; commandement/capture non établi.
- `financement mixte institutionnel/privé -> ressources organisationnelles -> advocacy/accès -> outputs` = **SUPPORTED** — Capacité, advocacy et accès fermés; tasking par un financeur non établi.
- `advocacy NGO -> recommandation -> modification de texte/décision UE` = **UNRESOLVED** — Contribution revendiquée/documentée; causalité marginale spécifique non isolée.
- `règle juridique de ciblage -> affectation de subvention humanitaire -> exclusion des activités politiques` = **SUPPORTED** — Contrôle juridique spécifique établi; ne prouve pas la séparation parfaite de toutes les subventions existantes.

## Gaps matériels certifiés

- `CLM-005` / **CAUSALITY** — Les auto-attributions d’incorporation et l’accès institutionnel ne fournissent pas un contrefactuel ni une attribution indépendante article-par-article du delta décisionnel.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-052`.

## Transition attendue

`INV-053 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
