---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-135-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-135"
---

<!-- DERIVED_FROM: te_run=20260906-1842-hack-and-leak; review=INV-135_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-135

```text
INV_ID = INV-135
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-1842-hack-and-leak
TE_PATH = 2026-09-06_18-42_hack-and-leak_INVESTIGATION.md
QRY = 16
SRC = 16
PROVENANCE_FAMILIES = 15
FCT = 23
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 23 blocked terminal outcomes
DELIVERABLE_SHA256 = 353a82a97819f95366c9ab146b64c2ed72865fd4df2fec2cfd168bad6c555c72
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

`CLM-001..009` remplace le label global « hack-and-leak » par une chaîne falsifiable : `compromission → vol → attribution → intégrité → timing → publication → amplification → exposition → persuasion → résultat → contrefactuel`. Chaque arête doit être prouvée séparément.

MacronLeaks montre une attribution qui évolue avec le temps : prudence/non-attribution publique française en 2017-2018, puis attribution officielle GRU/APT28 en 2025, sans que le dossier public inspecté fournisse pour autant une authentification exhaustive de l'archive ou transforme l'incertitude historique en faute méthodologique. DNC/Podesta ferme beaucoup plus haut l'opération, le vol, le canal et le timing, mais `CAU-001..002` maintient le résultat électoral contrefactuel non identifié. Iran/Trump 2024 sert de contrôle symétrique et montre que la décision des médias de publier ou non est un gate d'amplification distinct.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED/PARTIAL case-by-case — GRU/DNC fort; Iran/IRGC fort au niveau accusation/attribution officielle; Macron attribution officielle renforcée en 2025
I1 resources/capability/access = VERIFIED — spearphishing, accès, exfiltration et infrastructures documentés selon les cas
I2 documented action = VERIFIED — hacks/leaks et publications documentés dans les trois familles, avec intégrité corpus variable
I3 coordination/tasking/control = STRONG for GRU 2016 operation; PARTIAL/CONTESTED on narrower timing/client edges; no inherited proof from temporal coincidence
I4 exposure/reach = PARTIAL/MEASURED — volumes et audiences disponibles mais non homogènes; Macron reach domestique limité dans le contrôle retenu
I5 reception/persuasion = NOT_ESTABLISHED généralement
I6 behavior/institutional/electoral change = NOT_ESTABLISHED généralement
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- MacronLeaks : fraction exacte de documents altérés/non authentiques non établie dans le corpus public inspecté.
- MacronLeaks : attribution officielle 2025 plus forte que l'état public 2017-2018 ; le pont technique public rétroactif reste moins détaillé que le claim étatique final.
- DNC/Podesta : timing stratégique documenté, mais la coïncidence du 7 octobre ne suffit pas à prouver un déclenchement coordonné par la campagne Trump.
- DNC/Podesta : effet d'agenda soutenu ; effet winner-changing non identifié.
- Iran 2024 : procédure et effets politiques finaux non clos dans le corpus courant.

## RENARD decision + reason

```text
RENARD = NO
```

Les gaps restants exigent nouvelles pièces techniques/judiciaires ou données/design causal. Une recherche générique additionnelle sur des hacks électoraux serait principalement cumulative.

## New ideas triaged

```text
attribution chronology / intelligence-to-media -> MERGE vers INV-137
judicial/administrative timing effects         -> MERGE vers INV-143 lorsque matériel
ally/adversary symmetry                        -> MERGE vers INV-146 lorsque dépendances closes
Macron 2017 technical corpus                    -> RECHECK si nouvelle pièce publique matérielle
Iran 2024 judicial outcome                      -> RECHECK à décision/pièce nouvelle
generic catalogue of more hack-and-leak cases  -> DROP
```

## Registry patch

```text
INV-135 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-135_RUN_HANDOFF.md
next_action -> NONE — CLOSED; route attribution chronology to INV-137, timing questions to INV-143, symmetry to INV-146; recheck only on material new technical/judicial/causal evidence.
```
