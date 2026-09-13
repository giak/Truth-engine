---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-040-RUN-HANDOFF"
version: "1.0-kiss"
status: "closed"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-040"
truth_engine: "NOT_RUN_BY_DESIGN"
renard: "NO"
reclass_impact: "INV-133"
---

<!-- DERIVED_FROM: synthesis=INV-040_SYNTHESIS.md; certification=INV-040_SYNTHESIS_CERTIFICATION.json -->
<!-- DECISION: synthesis=PASS; unitary_capture=NOT_ESTABLISHED; polycentric_fragmented_accountability=SUPPORTED -->

# RUN_HANDOFF — INV-040

```text
INV_ID = INV-040
TE_STATUS = NOT_RUN_BY_DESIGN / type=SYNTHESIS
SYNTHESIS_PATH = INV-040_SYNTHESIS.md
SYNTHESIS_SHA256 = 63608989b4fb5b34abb26c9cb1a7a0d840109c8e7158b20dcc30540f540d54f7
INPUT_GATE = PASS_WITH_RECOVERY / 9 of 9 dependencies usable / INV-044 bounded recovery
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

Le corpus soutient une gouvernance européenne polycentrique où l'initiative, l'expertise et l'accès sont asymétriques et où la responsabilité est souvent fragmentée entre institutions, États, régulateurs et juridictions. Cela permet d'objectiver certains mécanismes de « déficit démocratique » — visibilité de l'initiative, traçabilité de l'influence, égalité d'accès, attribution de responsabilité — mais ne ferme ni une absence générale de contrôle démocratique ni une capture unitaire du système. Co-législation, frontières de compétence, recours, juridictions et contrôles procéduraux constituent des contre-pouvoirs matériels.

## Highest supported influence/effect edge

`institutional delegation + asymmetric agenda/expertise/access -> fragmented accountability = SUPPORTED`; `named private access/input -> exact adopted rule = PARTIAL / case-specific`; `information-governance ecosystem -> bounded coordination/capacity = SUPPORTED`; `unitary command/capture -> system-wide political effect = NOT_ESTABLISHED`.

## Material gaps / contradictions

- legislative footprints nommés et versionnés ;
- dénominateurs complets d'accès formel/informel ;
- métriques comparables d'attribution de responsabilité ;
- causalité aval des dispositifs informationnels, sanctions et contraintes normatives ;
- contrôle post-déploiement des ponts EUDI/CSA/QWAC.

## Contradictory review / causal ceiling

`complexité != déficit`; `délégation != capture`; `consultation != adoption`; `financement/certification != tasking`; `supervision/modération != effet politique`; `sanction/compliance != adhésion`. Le corpus établit des asymétries et une fragmentation de responsabilité, pas une architecture unitaire de contrôle.

## RENARD

`NO` — les gaps résiduels exigent des designs ciblés, pas une collecte générique supplémentaire.

## New ideas triaged

`legislative-footprint matched corpus -> RECHECK`; `access-denominator dataset -> RECHECK`; `generic EU capture search -> DROP`; `post-deployment EUDI/CSA controls -> DEFER until implementation evidence`.

## Registry patch

`INV-040 BACKLOG -> CLOSED`  
`truth_engine = NOT_RUN_BY_DESIGN`  
`renard = NO`  
`result_path = INV-040_RUN_HANDOFF.md`  
`next_action = CLOSED — SYNTHESIS PASS; feed bounded result to INV-133.`
