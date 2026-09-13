---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-128-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-128"
---

<!-- DERIVED_FROM: te_run=20260906-1732-influence-for-hire; review=INV-128_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-128

```text
INV_ID = INV-128
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260906-1732-influence-for-hire
TE_PATH = 2026-09-06_17-32_influence-for-hire_INVESTIGATION.md
QRY = 16
SRC = 16
PROVENANCE_FAMILIES = 9
FCT = 21
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 21 blocked terminal outcomes
DELIVERABLE_SHA256 = f75c96e5b32e77d14e87ad78af1711c01c46023a2bfc62366f1f327cd6244053
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

`CLM-001..009` établit que l'influence-for-hire est un marché privé réel de services opaques ou trompeurs, utilisable par des clients publics ou privés, domestiques ou étrangers. Le résultat discriminant n'est pas l'existence du marché mais la **décroissance de preuve le long de la chaîne** : `capacité -> action -> client/tasking -> exposition -> persuasion -> résultat`.

Team Jorge ferme surtout capacité/action, pas le palmarès électoral ni plusieurs clients. STOIC ferme opérateur/action mais le client ministériel reste contesté et la portée authentique mesurée est faible. Alp Services ferme le mieux client/paiement/tasking à partir du corpus interne, avec rebuttal conservé. `CLM-008 / CAU-001..002` interdit de convertir existence d'une opération en efficacité politique.

## Highest supported I0..I7

```text
I0 identity/relation = VERIFIED — prestataires et plusieurs relations commerciales/opérationnelles sont documentés
I1 resources/capability/access = VERIFIED — outils, faux profils, budgets/contrats ou capacités sont documentés selon les cas
I2 documented action = VERIFIED/PARTIAL — CIB, faux profils, hacking/placements et opérations de discrédit sont observés selon les cas
I3 coordination/tasking/control = PARTIAL — fort Alp/Rally Forge; contesté STOIC-ministère; UNKNOWN dans plusieurs cas Team Jorge
I4 exposure/reach = PARTIAL/MEASURED — followers, ads et amplification disponibles mais non homogènes; Zero Zeno faible
I5 reception/persuasion = NOT_ESTABLISHED généralement
I6 behavior/institutional/electoral change = NOT_ESTABLISHED généralement
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps / contradictions

- `CLM-005` : client ministériel de STOIC rapporté mais officiellement démenti ; attribution publique directe non fermée.
- Team Jorge : `30k profils / 33 campagnes` reste en partie marketing de prestataire ; clients et succès doivent être prouvés dossier par dossier.
- Alp Services : corpus interne fort mais contesté par le prestataire ; certaines allégations restent sous information judiciaire.
- `CAU-001..002` : persuasion et résultat politique causal non identifiés.
- Circularité : plusieurs médias/plateformes exploitent les mêmes traces ; multiplication de publications != familles indépendantes.

## RENARD decision + reason

```text
RENARD = NO
```

Les gaps restants exigent nouvelles pièces, décisions judiciaires ou designs causaux. Une recherche générique supplémentaire sur les mêmes prestataires serait principalement cumulative et violerait le delta-only gate.

## New ideas triaged

```text
provider/client attribution standards        -> MERGE vers INV-134
foreign indirect funding chains              -> MERGE vers INV-140
same mechanism ally vs adversary              -> MERGE vers INV-146
case-specific Team Jorge client files         -> RECHECK si nouvelle pièce matérielle
STOIC ministry contract/payment               -> RECHECK si document public apparaît
Alp judicial outcome                          -> RECHECK à décision/pièce nouvelle
generic list of more influence firms          -> DROP
```

## Registry patch

```text
INV-128 -> CLOSED
truth_engine -> DELIVERY_PASS_R3P1
renard -> NO
result_path -> INV-128_RUN_HANDOFF.md
next_action -> NONE — CLOSED; route attribution/client gaps to INV-134, indirect electoral funding to INV-140, symmetry to INV-146.
```
