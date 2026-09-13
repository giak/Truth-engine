---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-093-POST-RUN-REVIEW"
version: "1.0"
status: "closed_authorized"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-093"
---

<!-- DERIVED_FROM: te_run=20260907-1811-campaign-financing-france; delivery_sha256=550bb01304486c054564e48da1a4482ac937e1e00f2865a2acec21a5f167d393 -->
<!-- DECISION: P0=0; P1=0; P2=3; RENARD=NO; close=true -->

# POST-RUN REVIEW — INV-093

## Verdict

```text
TRUTH_ENGINE = DELIVERY_PASS_R3P1
PRE_GATE = PASS
DELIVERY_GATE = PASS
QRY = 14
SRC = 14
FCT = 28
PROVENANCE_FAMILIES = 5
CHECKPOINTS = 6
TESTS = 140 passed / 2 skipped
PERSISTENCE = PASS / 28 terminal blocked MNEMO_UNAVAILABLE
G0_G10 = PASS
P0 = 0
P1 = 0
P2 = 3
RENARD = NO
CLOSE = YES
```

## Revue contradictoire

Le run ne soutient ni « le financement des campagnes françaises est opaque et sans contrôle », ni « le contrôle CNCCFP rend toute origine des fonds entièrement traçable ». L'architecture juridique et comptable est dense, les voies de financement sont plurielles et réglementées, et les décisions distinguent réformation, modulation, rejet et pénal. Un trou amont subsiste néanmoins pour l'origine de certains fonds prêtés ou donnés par des personnes physiques.

Les contrôles 2017 et 2022 empêchent de convertir prêt, prêt miroir, financement partisan, micro-parti, prestation ou réformation comptable en fraude par catégorie. Les dossiers Sarkozy/Bygmalion et Jeanne montrent inversement que des montages précis peuvent franchir le seuil vers le rejet, le dépassement, le financement illégal, l'escroquerie ou des infractions connexes lorsque les faits sont établis.

Le plafond causal reste matériel : le run ferme des chaînes jusqu'aux conséquences administratives ou pénales, mais ne démontre pas que le financement ordinaire commande politiquement un candidat, persuade les électeurs ou change contrefactuellement le résultat d'une élection.

## P2 résiduels

1. pièces primaires permettant d'établir l'origine bénéficiaire de prêts/dons importants de personnes physiques lorsque le contrôle CNCCFP ne suffit pas ;
2. jeu de données comparable sur tarification, prestations, micro-partis/associations, réformations, rejets et décisions pénales ;
3. design causal reliant un mécanisme financier ou une sanction à un comportement électoral ou à un résultat contrefactuel.

Ces résidus nécessitent des données identifiées. Une recherche générique supplémentaire serait cumulative. `RENARD=NO`.
