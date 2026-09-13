---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-021"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-147"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-021

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-1932-us-services-france-europe`
- Deliverable: `INV-021_INVESTIGATION.md`
- Deliverable SHA-256: `638c9fa2eb1599460e606df3d10d247f8c7dc5bb8ebe05b8d7fd015097644557`
- Corpus runtime: `QRY=18 / SRC=8 / FCT=17 / provenance_families=5`
- Persistence: `PASS / eligible=17 / blocked=17 / success=0 / failure=0 / fabricated_memory_ids=0 / reason=MNEMO_UNAVAILABLE`

## Delta central

Des opérations clandestines américaines d'influence sont historiquement établies en Europe, avec une interface française directe ou structurante. Le Congress for Cultural Freedom ferme la chaîne la plus forte : OPC/CIA -> financement clandestin et conditions organisationnelles -> infrastructure culturelle européenne pilotée depuis Paris -> conférences/revues/exposition. Le même corpus fournit toutefois un contrôle interne contre `funding=content_control`: des participants disposaient d'une autonomie substantielle et pouvaient critiquer les États-Unis. La branche Force Ouvrière ferme un soutien américain matériel mais ne permet pas d'attribuer la création ou la scission à la CIA seule : Braden attribue des flux CIA aux réseaux Lovestone/Brown, Lovestone dément, Meany reconnaît 35 000 dollars d'aide AFL tout en niant l'origine CIA, et Caffery documente des causes domestiques immédiates. Pour la période moderne, les révélations NSA ferment `collecte -> révélation -> réaction institutionnelle/diplomatique`, mais `surveillance = influence politique` est rejeté comme saut de catégorie.

## Highest supported influence/effect edge

- `CIA/OPC -> financement clandestin + condition organisationnelle -> CCF/infrastructure culturelle -> production et exposition` = **SUPPORTED** ; `-> persuasion/comportement/résultat politique contrefactuel` = **NOT ESTABLISHED**.
- `soutiens américains -> intermédiaires syndicaux -> Force Ouvrière/capacité organisationnelle` = **PARTIAL** ; `CIA -> création/causalité unique de la scission` = **CONTRADICTED**.
- `collecte NSA -> révélation -> crise de confiance -> discussions France/Allemagne/USA + contrôle européen` = **SUPPORTED** ; `collecte de renseignement -> opération d'influence intentionnelle` = **NOT ESTABLISHED**.
- `guerre froide -> 2026, programme clandestin unique et continu` = **NOT ESTABLISHED**.

## Material gaps / contradictions

- **CAUSALITY** — aucune estimation indépendante ne ferme CCF/FO -> persuasion, vote ou résultat politique terminal.
- **CONTRADICTION** — provenance CIA exacte des fonds FO reste disputée entre Braden, Lovestone et Meany ; soutien américain et causes domestiques sont simultanément documentés.
- **TEMPORAL** — aucune pièce publique du corpus ne ferme une continuité programmatique/tasking unique entre opérations de guerre froide et activité actuelle en France/UE.
- **CATEGORY** — la surveillance peut produire des effets institutionnels après révélation sans constituer en elle-même une opération d'influence.

## Contradictory review / causal ceiling

L'enquête invalide deux raccourcis symétriques : nier l'existence d'opérations clandestines américaines historiques est incompatible avec le dossier CCF ; inversement, déduire de ces opérations un contrôle continu de la politique française ou un effet électoral général dépasse les preuves. `funding != command`, sauf lorsque des conditions organisationnelles précises sont documentées ; `support != creation`; `historical operation != current continuity`; `surveillance != influence`; `operation != persuasion/electoral_effect`.

## RENARD

`NO` — les résiduels matériels sont des gaps de causalité, de provenance ou de déclassification. Une collecte générique supplémentaire sur « CIA/USA en France » risquerait de substituer volume documentaire à la fermeture d'arêtes. Réouvrir seulement sur archive primaire FO décisive, tasking contemporain authentifié ou design causal terminal.

## New ideas triaged

- `INV-147` reçoit un contrôle allié fort : un allié peut satisfaire des critères matériels d'opération clandestine lorsque financement/tasking/action sont documentés ; le label géopolitique n'annule donc pas le mécanisme.
- Le CCF constitue aussi un cas méthodologique utile pour distinguer **contrôle organisationnel** et **autonomie de contenu**, sans créer un nouveau dossier.
- Aucun nouveau dossier actor-first n'est créé.

## Mechanical transition expected

`INV-021 TE_ACTIVE -> CLOSED`; `truth_engine=DELIVERY_PASS_R3P1`; `renard=NO`; `result_path=INV-021_RUN_HANDOFF.md`; semantic reclassification impact bounded to `INV-147`.
