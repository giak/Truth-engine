---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-124-POST-RUN-REVIEW"
version: "1.0"
status: "terminal"
updated: "2026-09-07"
inv_id: "INV-124"
---

<!-- TRACE: runtime=2.10.6/R3P1; delivery=PASS; review_scope=delta-only -->

# Post-run review — INV-124

## Verdict

```text
TRUTH_ENGINE = DELIVERY_PASS_R3P1
QRY = 15
SRC = 14
PROVENANCE_FAMILIES = 8
FCT = 28
CHECKPOINTS = 6
G0_G10 = PASS
TESTS = 140 passed / 2 skipped
PERSISTENCE = PASS / 28 terminal MNEMO_UNAVAILABLE blocks
P0 = 0
P1 = 0
P2 = 3
RENARD = NO
INV_STATUS = CLOSED_AUTHORIZED
```

## Central delta

La restriction d'accès financier recouvre au moins trois architectures distinctes : droits d'accès réglementés avec recours, décisions privées de risque/conformité pouvant produire du de-risking légitime ou injustifié, et sanctions publiques imposant directement gel/interdiction de mise à disposition de fonds. Le corpus établit donc une infrastructure réelle de coercition/exclusion financière, mais ne permet pas de généraliser `restriction privée -> motif politique -> commandement public`. Le cas Farage est mixte et procéduralement défaillant, tandis que les contrôles FCA ne soutiennent pas une règle générale de fermeture pour opinions politiques. L'effet politique ou électoral causal reste non établi.

## Highest supported I0..I7

- `I0-I4 = VERIFIED case-specifically` pour règle, déclencheur, décisionnaire, restriction, procédure/recours et certaines conséquences institutionnelles/économiques.
- `I5 = PARTIAL / NOT_ESTABLISHED generally` pour motif politique, tasking ou commandement public d'une décision privée.
- `I6 = NOT_ESTABLISHED` pour persuasion/comportement politique causé par la restriction.
- `I7 = NOT_ESTABLISHED` pour résultat électoral/politique contrefactuel.

## P2 residuals

1. prévalence et dénominateur des restrictions visant effectivement des acteurs politiques/civiques en France/UE insuffisamment fermés ;
2. arête `acteur public -> instruction/pression -> prestataire financier -> restriction` non établie de façon générale hors sanctions formelles ;
3. chaîne `restriction financière -> coût/exposition -> comportement politique -> résultat` non causalement fermée.

## RENARD

`NO` — une collecte générique serait cumulative. Les résidus exigent des ordres/instructions, dossiers de clôture individuels, données de dénominateur comparables ou un design causal, pas davantage d'exemples anecdotiques.

## Routing

Delta terminal vers `INV-129`. Après fermeture d'INV-124, `INV-129` reste bloquée par `INV-080` uniquement.
