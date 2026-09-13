---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-145-POST-RUN-REVIEW"
version: "1.0"
status: "closed"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-145"
---

<!-- DERIVED_FROM: te_run=20260907-0538-inv145-recovery; method=METHOD_PACK.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->
<!-- TRACE: recovery replaces no persisted prior INV-145 RUN_STATE; prior ephemeral IDs are non-authoritative -->

# POST-RUN REVIEW — INV-145

## Verdict

```text
TRUTH_ENGINE = DELIVERY_PASS_R3P1
PRE_GATE = PASS
DELIVERY_GATE = PASS
TESTS = 140 passed / 2 skipped
QRY = 9
SRC = 9
FCT = 21
PROVENANCE_FAMILIES = 5
G0_G10 = PASS
PERSISTENCE = PASS / 21 eligible facts terminally blocked MNEMO_UNAVAILABLE
RENARD = NO
P0 = 0
P1 = 0
P2 = 3
INV_STATUS = CLOSED
```

## Central delta

Le résultat robuste est une **asymétrie de conception juridique**, pas une asymétrie d'enforcement démontrée. FARA définit le principal étranger plus largement ; le dispositif français introduit un périmètre explicitement hors UE et lié aux puissances étrangères/partis/entités qualifiées ; le projet européen vise une représentation d'intérêts attribuable à un sponsor de pays tiers et exclut explicitement le financement étranger sans lien avec cette prestation.

La différence de périmètre est factuelle. Sa légitimité normative est une question distincte. L'hypothèse selon laquelle des comportements isomorphes seraient effectivement investigués ou sanctionnés différemment selon allié/adversaire n'est pas établie par les données disponibles.

## P2 résiduels

1. **BASELINE** — pas encore de fenêtre française pluriannuelle comparable à FARA avec dénominateurs communs.
2. **TEMPORAL** — la procédure européenne 2023/0463/COD n'est pas finalisée ; pas de transposition ni d'enforcement comparable.
3. **CAUSALITY** — aucun design causal commun ne mesure l'effet dissuasif ou comportemental des trois régimes.

Aucun de ces résiduels n'est réparable par une collecte générique supplémentaire au 7 septembre 2026.

## RENARD

`NO`.

Le seuil METHOD_PACK §8 n'est pas franchi : les gaps restants exigent du **temps**, de futurs actes juridiques/enforcement ou un design comparatif causal identifié. Relancer une recherche large produirait surtout de la redondance.

## Recovery accounting

Le précédent état partiel annoncé pour INV-145 n'avait pas de `_RUN_STATE.json` persisté. La reprise a donc été exécutée comme un run de récupération distinct à partir du `RUN_CARD` exact et du ZIP canonique Truth Engine 2.10.6 R3P1. Aucun identifiant runtime perdu n'a été réutilisé. Le run récupéré a été reconstruit avec de nouveaux IDs, puis PRE et DELIVERY ont été vérifiés indépendamment.
