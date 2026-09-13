---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-054-POST-RUN-REVIEW"
version: "1.0"
status: "closed_authorized"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-054"
---

<!-- DERIVED_FROM: te_run=20260907-1222-strategic-litigation-ngo; delivery_sha256=9b02a7b42d2289c9ea2e2b0d47481f091a4bccc35118d0448f9620ab8b409c03 -->
<!-- DECISION: P0=0; P1=0; P2=3; RENARD=NO; close=true -->

# POST-RUN REVIEW — INV-054

## Verdict

```text
TRUTH_ENGINE = DELIVERY_PASS_R3P1
PRE_GATE = PASS
DELIVERY_GATE = PASS
QRY = 11
SRC = 11
FCT = 24
PROVENANCE_FAMILIES = 5
CHECKPOINTS = 6
TESTS = 140 passed / 2 skipped
PERSISTENCE = PASS / second terminal attempt after degraded-flag correction
G0_G10 = PASS
P0 = 0
P1 = 0
P2 = 3
RENARD = NO
CLOSE = YES
```

## Contradictory review

Le résultat ne justifie ni « les ONG ne font que plaider » ni « les financeurs gouvernent par les tribunaux ». Le mécanisme stratégique est explicite et peut produire des obligations juridiques contraignantes, mais les juridictions restent un filtre observable : des affaires gagnent, perdent ou sont redirigées procéduralement.

Le financement de capacité est documenté. Le chaînon décisif `financeur externe -> affaire/argument/jugement demandé` n'est pas établi dans les sources examinées. Les cas de subvention affectée montrent en outre qu'un financement d'organisation ne doit pas être imputé automatiquement à toutes ses activités.

## P2 résiduels

1. documents primaires d'earmarking/tasking reliant un financeur à une affaire ou un argument précis ;
2. données d'exécution permettant de distinguer jugement et mise en œuvre effective ;
3. designs comparatifs permettant d'estimer l'effet politique durable contrefactuel du contentieux.

Ces résidus nécessitent des données identifiées, pas une collecte générique supplémentaire. RENARD reste donc `NO`.

## Runtime note

Le premier `set-persistence` a été `PARTIAL` parce que le flag `MNEMO_UNAVAILABLE` n'avait pas encore été inscrit dans `run.degraded_flags`. Aucun fait, source ou conclusion n'a été modifié. Le flag canonique a été ajouté, une seconde tentative terminale a obtenu `PASS`, puis snapshot et DELIVERY ont été validés.
