---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "renard_delta"
artifact_id: "INV-049-RENARD"
version: "1.0"
status: "closed"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-049"
parent_te_run: "20260905-2145-open-society-foundations-france-ue"
---

<!-- DERIVED_FROM: INV-049_INVESTIGATION.md; protocol=RENARD_CORE_V3; mode=targeted_delta_only -->
<!-- DECISION: renard=REQUIRED_THEN_CLOSED; scope=FPOS_MORE_IN_COMMON_FRANCE_EU_BRIDGE_ONLY -->

# INV-049 — RENARD ciblé

## Discriminant

```text
DISCRIMINANT = Un financement FPOS/OSF de More in Common est-il explicitement relié à des travaux France/UE,
               et ce bridge permet-il d'établir un financement direct ou un tasking de Destin Commun ?
WHY_IT_MATTERS = Distingue financement réseau réellement orienté France/UE d'une simple proximité de marque,
                 sans promouvoir financement en contrôle.
TARGET_EVIDENCE = filings fiscaux / agrégations dérivées des filings + gouvernance More in Common/Destin Commun.
```

## [DECOMPOSE]

| Atom | Sub-claim | Source_tier_needed | Search_target | Verdict |
|---|---|---|---|---|
| A1 | Foundation to Promote Open Society finance More in Common de manière matérielle | T1/T2 | filings 990 / agrégations IRS | VERIFIED |
| A2 | Au moins un grant vise explicitement la France et le niveau UE | T1/T2 | grant purpose / filings | SUPPORTED |
| A3 | Destin Commun est intégré à la gouvernance du réseau More in Common | T1/T2 | gouvernance officielle Destin Commun | VERIFIED |
| A4 | Le grant OSF est versé directement à l'entité juridique Destin Commun | T1 | comptes/grant agreement France | OPEN |
| A5 | OSF dispose d'un droit de tasking/validation sur Destin Commun | T1 | convention/correspondance/gouvernance | OPEN |

## [SHADOW]

| Atom | Trace_if_H_true | Trace_if_H_false | Discriminant? |
|---|---|---|---|
| A1 | grants nominatifs récurrents More in Common | aucun grant ou identité non résolue | Y |
| A2 | purpose mentionnant France/UE | grants génériques sans géographie France/UE | Y |
| A3 | gouvernance réseau explicitement mutualisée | entité française gouvernée séparément sans supervision réseau | Y |
| A4 | Destin Commun nommé comme bénéficiaire ou transfert documenté | seul More in Common Inc/global est bénéficiaire | Y |
| A5 | clause d'approbation/tasking OSF | autonomie du bénéficiaire / aucune clause accessible | Y |

## TRACE — pièces consultées

1. `philanthropy.org`, données dérivées des filings IRS : Foundation to Promote Open Society est le premier financeur identifié de More in Common sur 2020–2024, **5,1 M$ / 9 grants**.  
   Réf: https://philanthropy.org/990/who-funds/823043917/more-in-common-inc
2. `Cause IQ`, données fiscales : un grant Open Society est décrit comme soutien à la **recherche d'opinion et analytics** au bénéfice de sociétés démocratiques en **Allemagne, France, Pologne et au niveau UE**.  
   Réf: https://www.causeiq.com/organizations/more-in-common%2C823043917/
3. `InfluenceWatch`, agrégation secondaire de filings : même objet de grant France/UE apparaît pour un financement FPOS de More in Common ; utilisé comme corroboration de la description, pas comme autorité idéologique.  
   Réf: https://www.influencewatch.org/non-profit/more-in-common/
4. Destin Commun, source officielle : l'association française est la branche française de More in Common et indique que la gouvernance du réseau est mutualisée ; le CA global supervise stratégie et gouvernance du réseau.  
   Réf: https://www.destincommun.fr/qui-sommes-nous/notre-gouvernance/
5. More in Common, source officielle : le réseau est enregistré en France sous forme d'association loi 1901 et reçoit des financements de fondations dans ses pays d'activité et de financeurs globaux.  
   Réf: https://www.moreincommon.com/about-us/funding/

## [ADVERSARY]

| Axis | H_prediction | Rival_prediction | Observation | Favors |
|---|---|---|---|---|
| France/UE specificity | OSF finance un programme explicitement France/UE | lien OSF-France purement indirect/générique | purpose de grant mentionne France + UE | H |
| Direct Destin grant | Destin Commun apparaît comme bénéficiaire juridique | seul More in Common/global apparaît | aucun grant direct Destin Commun retrouvé | Rival |
| Command | clauses/tasking OSF visibles | financement sans commandement prouvé | aucune clause de tasking/validation retrouvée | Rival |
| Network bridge | structure France rattachée à gouvernance globale | entité France isolée | gouvernance mutualisée documentée | H |
| Causal effect | outcome attribuable isolable | activité sans effet causal mesuré | aucun design causal France/UE trouvé | Rival |

## UPDATE

```text
H1 OSF materially funds More in Common                         -> STRENGTHEN
H2 OSF funding has an explicit France/EU programmatic bridge   -> STRENGTHEN
H3 Destin Commun is directly funded by OSF legal-entity-to-entity -> UNRESOLVED
H4 OSF commands/tasks Destin Commun                            -> UNRESOLVED / NOT_ESTABLISHED
H5 OSF causes measurable France/EU policy/opinion outcomes     -> UNRESOLVED
```

Delta matériel : le modèle devient plus précis :

```text
Foundation to Promote Open Society / OSF
    -> grants documentés à More in Common
    -> au moins un objet de grant explicitement France/UE
    -> réseau More in Common à gouvernance mutualisée
    -> Destin Commun = branche française
```

Mais les deux arêtes suivantes **ne sont pas établies** :

```text
OSF -> versement direct à l'entité juridique Destin Commun
OSF -> tasking/commandement de la gouvernance ou des opérations de Destin Commun
```

Le financement orienté France/UE établit donc une **capacité et une finalité programmatique**, pas un contrôle ni un effet causal.

## [EVALUATE]

| Atom | Source_tier | Independent? | Survives_break? | Status | Confidence |
|---|---|---|---|---|---:|
| A1 | T1-derived/T2 | Y | Y | K | 0.97 |
| A2 | T1-derived/T3 corroboration | Y | Y | S | 0.90 |
| A3 | T1 self-description | N/A | Y | K | 0.96 |
| A4 | T1 required, absent | N/A | Y | O | 0.25 |
| A5 | T1 required, absent | N/A | Y | O | 0.15 |

EPISTEMIC_LEDGER := `verified:2 | supported:1 | disputed:0 | open:2 | refuted:0`

`CALIBRATION` du protocole RENARD n'est pas utilisé comme preuve de qualité ; le pilotage reste fondé sur les gaps décisifs et le pouvoir discriminant.

## [REPORT]

| Field | Content |
|---|---|
| what_changed_since_last | Bridge France/UE renforcé : purpose de grant explicite + gouvernance réseau France documentée |
| surviving_H | financement matériel ; objectif programmatique France/UE ; influence/capacité réseau |
| killed_H | aucune hypothèse supplémentaire tuée ; la forme forte contrôle total reste non établie |
| confidence_before -> confidence_after | bridge France/UE : 0.70 -> 0.90 ; contrôle OSF->Destin : 0.20 -> 0.15 |
| next_priority | uniquement convention de grant/comptes Destin ou clause de tasking si une pièce concrète apparaît |
| CALIBRATION | non-décisionnel ; gaps décisifs restants = 2 |

## Stop

```text
RENARD = CLOSED_NO_FURTHER_MATERIAL_DELTA
STOP_REASON = next discriminants require a concrete grant agreement/accounting record/tasking document;
              generic further searching would be fishing.
TRUTH_ENGINE_FINAL = UNCHANGED
```

<!-- DECISION: do_not_rewrite_truth_engine_final=true -->
