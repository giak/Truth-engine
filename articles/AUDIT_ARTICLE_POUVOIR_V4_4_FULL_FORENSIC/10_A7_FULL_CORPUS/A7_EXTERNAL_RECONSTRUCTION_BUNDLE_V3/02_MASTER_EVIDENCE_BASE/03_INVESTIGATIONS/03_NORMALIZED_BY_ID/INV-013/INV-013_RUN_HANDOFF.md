---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-013"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-072;INV-109"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-013

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-0157-active-measures-soviet-russian`
- Deliverable: `INV-013_INVESTIGATION.md`
- Deliverable SHA-256: `5908d4c9e1e02201600037ddeada24b00801b476f8d3e01c49b5053e46ec7f5f`
- Corpus runtime: `QRY=20 / SRC=15 / FCT=30 / provenance_families=5`
- Persistence: `PASS / eligible=30 / blocked=30 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-013 ferme une distinction essentielle entre continuité tactique et continuité institutionnelle. Le corpus établit un répertoire soviétique documenté d'active measures (forgeries, fronts, influence agents, manipulation médiatique) et des opérations russes contemporaines actor-specific utilisant faux sites/personas, contenus fabriqués ou mis en scène, amplification coordonnée et dissimulation de provenance. La continuité est forte au niveau du répertoire et de l'adaptation technique, mais le corpus inspecté ne ferme pas une chaîne organisationnelle ininterrompue KGB/Service A -> opérateurs russes actuels. Les opérations modernes peuvent fermer opérateur/tasking/distribution dans des cas précis, y compris vers France/Europe, mais exposition, persuasion et résultat politique restent distincts : les mesures de portée sont hétérogènes et les études inspectées ne démontrent pas un effet électoral général. `doctrine/capacité != opération`, `opération != exposition`, `exposition != persuasion`, `activité != efficacité` restent les gardes centrales.

## Registre causal certifié

- `Soviet authority/KGB active-measures apparatus -> forged documents/fronts/media manipulation -> foreign distribution environments` = **SUPPORTED** — Technique execution and institutional use are established; generalized persuasion or policy change is not.
- `IRA organization -> false personas/US infrastructure -> interaction with U.S. audiences -> election-related activity` = **SUPPORTED** — Tasking/action are strong; measured marginal persuasion and result change remain unclosed.
- `Russian Presidential Administration -> SDA/Structura/ANO Dialog -> spoofed domains/influencers/bots -> foreign audience targeting` = **SUPPORTED** — Direct campaign command is alleged/documented by official U.S. action; downstream voter or policy effect is not established.
- `Russia-linked operator ecosystem -> Portal Kombat/Matriochka/Storm-1516 cross-amplification -> France/EU information exposure` = **SUPPORTED** — Distribution and targeting are established; common tasking for every downstream amplifier and political effect are not.
- `Russian influence-operation exposure -> attitude/polarization/vote change -> electoral or policy outcome` = **UNRESOLVED** — No general causal closure; the strongest inspected individual-level study finds no meaningful relationship in the 2016 Twitter sample.

## Gaps matériels certifiés

- `CLM-003` / **TEMPORAL** — A direct archival command/organizational bridge across the Soviet collapse and later Russian operator ecosystem is not established in the inspected record.
- `CLM-005` / **CAUSALITY** — No inspected France/EU design isolates marginal effects on political attitudes, voting or a named public decision.
- `CLM-007` / **CAUSALITY** — Case-specific effects outside the measured Twitter sample and later campaigns remain possible and require their own exposure-to-outcome designs.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-072;INV-109`.

## Transition attendue

`INV-013 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
