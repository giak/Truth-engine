---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-074"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-075"
updated: "2026-09-09"
---

# RUN_HANDOFF — INV-074

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260909-1624-arcom-regulation-pluralism`
- Deliverable: `INV-074_INVESTIGATION.md`
- Deliverable SHA-256: `492876e943a1a7bc2839d5b46a8ce869dd65c3733fdb01170e9b3f4fa0de4b79`
- Corpus runtime: `QRY=27 / SRC=16 / FCT=28 / provenance_families=5`
- Persistence: `PASS / eligible=28 / blocked=28 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-074 établit que l’ARCOM est une autorité dotée de pouvoirs matériels et non un simple secrétariat procédural : sanctions financières, contrôle du pluralisme, choix d’accès à la TNT et coordination DSA produisent des effets juridiques ou économiques directement observables. Ces pouvoirs sont cependant bornés par des critères légaux, des instruments gradués et un contrôle juridictionnel effectif qui peut aussi corriger ou compléter l’action du régulateur. Les nominations politiques d’une partie du collège, les sanctions défavorables et le non-renouvellement de C8/NRJ12 ne ferment pas une chaîne de tasking politique. Le corpus ne fournit ni dénominateur suffisant pour établir un biais systémique après contrôle des cas et gravités, ni design causal reliant les interventions de l’ARCOM à une orientation éditoriale générale, à l’opinion ou au vote. Le DSA confirme enfin une frontière de compétence : priorité de traitement des trusted flaggers, mais décision de retrait conservée par les plateformes dans ce mécanisme et compétence exclusive de la Commission sur les obligations de diligence des VLOP/VLOSE.

## Registre causal certifié

- `statutory mandate -> monitoring/referral -> ARCOM procedure -> graded decision or sanction` = **SUPPORTED** — The legal chain establishes regulatory authority, not political motive.
- `Conseil d’État 13 Feb 2024 judgment -> mandatory reexamination -> broadened pluralism framework -> CNews warning/request for compliance measures` = **SUPPORTED** — Judicially induced regulatory change is supported; downstream editorial change is not measured here.
- `repeated C8 contractual/legal breaches -> ARCOM financial sanction -> judicial review -> sanction maintained` = **SUPPORTED** — Case-specific enforcement legality/proportionality; no inference to all ARCOM cases.
- `TNT call + statutory comparative criteria -> rejection/non-renewal of C8 and NRJ12 -> new service authorisations / loss of terrestrial market access` = **SUPPORTED** — Direct access effect is established; political intent or democratic downstream effect is separate.
- `ARCOM as French DSA coordinator -> designation of trusted flaggers -> priority platform review -> platform content decision` = **SUPPORTED** — Priority processing is mandatory, but providers retain decision responsibility and the Commission has exclusive VLOP due-diligence competence.

## Gaps matériels certifiés

- `CLM-004` / **MEASUREMENT** — Case existence proves cross-sector enforcement, not symmetry of rates, severity, issue mix or exposure to complaints across all editors.
- `CLM-006` / **CAUSALITY** — A political-control claim requires authenticated instruction, dependence or decision-specific tasking; a downstream pluralism claim requires measured editorial/exposure effects with a credible counterfactual.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-075`.

## Transition attendue

`INV-074 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
