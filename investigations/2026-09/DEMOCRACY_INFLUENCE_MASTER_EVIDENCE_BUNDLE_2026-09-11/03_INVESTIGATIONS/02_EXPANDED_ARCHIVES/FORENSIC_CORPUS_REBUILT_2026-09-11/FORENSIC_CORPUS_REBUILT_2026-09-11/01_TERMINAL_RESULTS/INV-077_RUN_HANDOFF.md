---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-077"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-076"
updated: "2026-09-09"
---

# RUN_HANDOFF — INV-077

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260909-1124-public-advertising-media-leverage`
- Deliverable: `INV-077_INVESTIGATION.md`
- Deliverable SHA-256: `e58ab20d9eee627f05146257e2e2fb3a4bdd9b66ad435892400f1dda7830df68`
- Corpus runtime: `QRY=23 / SRC=12 / FCT=26 / provenance_families=5`
- Persistence: `PASS / 21 eligible FACT blocked=MNEMO_UNAVAILABLE / 5 EVIDENCE non-eligible / 0 fabricated memory IDs`

## Delta central

La France dispose d'une infrastructure matérielle et partiellement centralisée d'achat publicitaire public reliant budgets de communication, marchés/centrales d'achat et allocations d'espaces médias. La publicité représente par ailleurs une part économiquement significative des revenus de plusieurs classes de médias. Ces deux faits rendent un levier économique possible mais ne suffisent pas à établir une contrepartie éditoriale.

Le droit européen traite désormais l'allocation opaque ou discriminatoire de publicité d'État comme un risque crédible pour l'indépendance éditoriale et impose des garde-fous de transparence et de non-discrimination. Ce cadre établit un modèle de risque, pas la preuve d'une violation française.

## Arête d'influence la plus élevée supportée

`public authority -> communication budget/procurement -> media agency -> paid media allocation` = **SUPPORTED**.

`government advertising -> changed political editorial tone` = **SUPPORTED uniquement dans le comparateur mexicain étudié** ; non transférable comme estimation française.

## Plafond causal / contradictions

- `advertising revenue -> public-advertiser bargaining vulnerability` = **UNRESOLVED** : dépendance spécifique à la publicité publique non mesurée au niveau des bénéficiaires.
- `public-ad allocation/withdrawal -> editorial pressure/self-censorship in France` = **UNRESOLVED** : cas français principalement testimoniaux/rapportés, sans instruction authentifiée ni discontinuité causale.
- `French state advertising -> changed coverage/opinion/turnout/vote/election result` = **UNRESOLVED**.
- `spending != influence`; `allocation != tasking`; `payment != quid_pro_quo`; `testimony != causal_proof`; `foreign_effect != France_effect`.

## RENARD

`NO`. Une collecte générique supplémentaire serait cumulative. Réouvrir seulement sur : instruction/condition authentifiée, retrait/allocation exploitable comme quasi-expérience, ou panel français joignant dépense publique, dépendance du média et contenu éditorial.

## Reclassification

Impact direct : `INV-076` uniquement. INV-077 fournit un contrôle causal et économique direct pour l'enquête sur aides/subventions à la presse, sans fermer son mécanisme propre. Les autres investigations conservent leur évaluation sauf dérive mécanique détectée par `reclass-plan`.

## Transition attendue

`INV-077 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant du full-pool fusionné après REVIEW explicite.
