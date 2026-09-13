---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-033-RUN-HANDOFF"
version: "1.0"
status: "closed"
updated: "2026-09-07"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-033"
---

<!-- DERIVED_FROM: te_run=20260907-0711-emirats-influence-europe; review=INV-033_POST_RUN_REVIEW.md -->
<!-- DECISION: truth_engine=DELIVERY_PASS_R3P1; renard=NO; inv=CLOSED -->

# RUN_HANDOFF — INV-033

```text
INV_ID = INV-033
TE_STATUS = DELIVERY_PASS_R3P1
TE_RUN_ID = 20260907-0711-emirats-influence-europe
QRY = 13
SRC = 13
PROVENANCE_FAMILIES = 9
FCT = 22
CHECKPOINTS = 7
MNEMO = MNEMO_UNAVAILABLE degraded
PERSISTENCE = PASS / 22 blocked terminal outcomes
DELIVERABLE_SHA256 = 6882743d76521abaf201035c2d0148116b76c0f3f28fc5bfb95595ea42e67a8e
RENARD = NO
INV_STATUS = CLOSED
```

## Central delta

Le dossier Alp Services apporte au contrôle de symétrie un cas où la chaîne `client lié au renseignement émirati -> paiement/tasking -> prestataire privé -> opérations/cibles` est beaucoup plus fortement fermée que de simples relations de financement ou de proximité. En revanche, la fiabilité des fiches, la connaissance du client ultime par chaque intermédiaire et les effets downstream restent distincts et partiellement non établis.

## Highest supported I0..I7

```text
I0 identity/relation = STRONG pour le noyau client-Alp ; variable downstream
I1 resources/capability = VERIFIED pour paiements/contrats/capacités
I2 documented action = VERIFIED pour profilage, opérations réputationnelles et collecte
I3 coordination/tasking/control = STRONG pour le noyau client-Alp ; non transférable à chaque intermédiaire
I4 exposure/reach = PARTIAL / opération-spécifique
I5 reception/persuasion = NOT_ESTABLISHED
I6 behavior/institutional change = PARTIAL sur certains effets ; causalité hétérogène
I7 counterfactual outcome = NOT_ESTABLISHED
```

## Material gaps

- listes/profilages documentés `!=` exactitude de chaque allégation ;
- paiement/contrat `!=` succès opérationnel ;
- accès/information `!=` causalité institutionnelle ;
- clôture procédurale `!=` réfutation des documents internes ;
- opération existe `!=` résultat politique changé.

## Routing

```text
MERGE -> INV-146 : UAE-linked private-intelligence / covert-reputation symmetry control
RECHECK -> only on material judicial/tasking/causal evidence
```
