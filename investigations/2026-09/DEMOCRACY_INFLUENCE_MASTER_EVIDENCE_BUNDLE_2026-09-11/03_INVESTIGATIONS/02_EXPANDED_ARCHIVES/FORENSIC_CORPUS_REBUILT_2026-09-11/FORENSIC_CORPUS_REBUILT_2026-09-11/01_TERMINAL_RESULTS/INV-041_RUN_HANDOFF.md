---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-041"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-120;INV-121;INV-123"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-041

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-0902-eu-commission-regulatory-production`
- Deliverable: `INV-041_INVESTIGATION.md`
- Deliverable SHA-256: `1d915938dd0a7cfa6236a6e7663cca386c13862aa86d28bb9d04539dcbf960ed`
- Corpus runtime: `QRY=20 / SRC=16 / FCT=26 / provenance_families=6`
- Persistence: `PASS / eligible=26 / blocked=26 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-041 ferme l’architecture générique de la production réglementaire de la Commission européenne sans valider une capture générale. Le corpus établit des canaux institutionnalisés de consultation, d’expertise et de représentation d’intérêts, mais aussi des gates internes et interinstitutionnels réels. Le cas ESRS ferme une chaîne agrégée consultation -> révision technique EFRAG -> modifications identifiables de la Commission -> acte délégué final, tandis que la procédure législative ordinaire ferme proposition Commission -> négociation/co-législation Parlement-Conseil -> acte final. En revanche, aucune chaîne bornée n’isole dans ce run un acteur privé nommé dont une contribution cause une clause finale précise, ni accès/expertise -> capture. Le prochain gain exige un legislative footprint acteur -> contribution versionnée -> modification identifiable -> adoption, avec attribution interne et contrôle des explications rivales.

## Registre causal certifié

- `stakeholder consultation -> EFRAG exposure-draft revision -> reduced disclosure requirements/datapoints and changed materiality approach` = **SUPPORTED** — Aggregate consultation effect; no named contributor marginal effect isolated.
- `EFRAG technical advice -> Commission modifications -> ESRS delegated act` = **SUPPORTED** — Does not attribute the Commission modifications to any single private stakeholder.
- `named private interest submission -> exact Commission text change -> adopted clause` = **UNRESOLVED** — Textual alignment or access alone is insufficient.
- `Commission proposal -> Parliament/Council negotiation and trilogue -> final ordinary-legislative text` = **SUPPORTED** — General process edge; dossier-level marginal attribution still needs versioned legislative footprint.
- `negative RSB opinion -> revised impact assessment -> resubmission before Commission adoption` = **SUPPORTED** — Quality-control effect does not itself determine the policy option chosen.
- `Commission delegated act adoption -> Parliament/Council objection window -> entry into force if no objection` = **SUPPORTED** — No-objection is not affirmative endorsement of every technical choice.
- `lobby access/meeting/expert-group participation -> policy influence -> regulatory capture` = **UNRESOLVED** — Access and participation are institutional facts, not proof of adoption or control.

## Gaps matériels certifiés

- `CLM-002` / **CAUSAL_ATTRIBUTION** — Need contribution-specific version trace and decision record to attribute marginal influence.
- `CLM-003` / **ACTOR_ATTRIBUTION** — Attribution is to consultation/EFRAG/Commission stages, not to a named private actor.
- `CLM-004` / **CAUSAL_ATTRIBUTION** — Need timestamped contribution, versioned text delta, internal attribution/minutes and competing explanations.
- `CLM-007` / **TRANSPARENCY_DENOMINATOR** — Unscheduled and lower-level interactions remain incompletely captured.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-120;INV-121;INV-123`.

## Transition attendue

`INV-041 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
