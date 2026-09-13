---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-093-RUN-HANDOFF"
version: "1.0"
status: "terminal"
updated: "2026-09-07"
inv_id: "INV-093"
---

<!-- TRACE: method_pack_section=10; runtime=2.10.6/R3P1; te_status=DELIVERY_PASS_R3P1 -->

# RUN_HANDOFF — INV-093

## INV_ID

`INV-093`

## TE status/path

`DELIVERY_PASS_R3P1`  
`INV-093_INVESTIGATION.md`

## Central delta

Le financement électoral français est un système multicanal fortement réglementé, où dons, prêts, financements de partis, prestations et remboursement public ont des régimes distincts. Les contrôles CNCCFP et juridictionnels produisent une gradation réelle entre réformation, modulation, rejet et responsabilité pénale. Des montages illicites sont établis dans des cas précis, sans permettre de qualifier prêts, partis, micro-partis ou prestations comme frauduleux par nature. Un trou de traçabilité amont demeure pour l'origine de certains fonds individuels.

## Highest supported I0..I7

`I0-I4 = VERIFIED case-specifically` pour source/vehicle/transaction, comptabilisation/règle, contrôle et conséquence administrative ou pénale.  
`I5 = NOT_ESTABLISHED` pour commandement politique dérivé du financement.  
`I6 = NOT_ESTABLISHED` pour persuasion électorale attribuable au mécanisme financier.  
`I7 = NOT_ESTABLISHED` pour résultat électoral contrefactuel.

## Material gaps/contradictions

- contrôle aval dense, mais origine amont de certains prêts/dons de personnes physiques incomplètement vérifiable ;
- réformation/rejet administratif et fraude pénale sont des objets distincts ;
- véhicule partisan, associatif ou de prestation peut être normal ou abusé : qualification cas par cas ;
- financement et conséquence institutionnelle ne ferment pas les arêtes commandement, persuasion ou résultat.

## RENARD decision + reason

`NO` — les trois plafonds nécessitent des pièces primaires d'origine des fonds, un corpus structuré de tarification/prestations ou un design causal électoral. Une collecte générique additionnelle ne changerait pas le verdict.

## New ideas triaged

- origine bénéficiaire / financement étranger indirect : `INV-094` et `INV-140` ;
- sélection/candidatures et structures de financement : `INV-095` ;
- effet sur choix réel, compétition et consentement : `INV-102`.

## Registry patch

`INV-093 TE_ACTIVE -> CLOSED`  
`truth_engine = DELIVERY_PASS_R3P1`  
`renard = NO`  
`result_path = INV-093_RUN_HANDOFF.md`  
Route terminal delta to `INV-095` and `INV-102`.
