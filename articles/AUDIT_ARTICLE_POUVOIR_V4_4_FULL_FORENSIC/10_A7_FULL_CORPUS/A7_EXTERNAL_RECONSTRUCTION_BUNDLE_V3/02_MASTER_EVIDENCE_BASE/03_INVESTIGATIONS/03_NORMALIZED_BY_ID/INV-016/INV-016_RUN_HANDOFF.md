---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-016"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-016

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-1042-arab-spring-mechanisms`
- Deliverable: `INV-016_INVESTIGATION.md`
- Deliverable SHA-256: `323d0a35b2479b8409c6dea1fcb5527bbf16584719264c178512e5a6ffe943e1`
- Corpus runtime: `QRY=11 / SRC=11 / FCT=13 / provenance_families=8`
- Persistence: `PASS / eligible=13 / blocked=13 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-016 établit trois contributions intermédiaires distinctes aux printemps arabes : une infrastructure d’assistance démocratique occidentale préexistait en Égypte ; un transfert tactique CANVAS/Otpor vers au moins un militant d’April 6 est documenté ; et les réseaux sociaux ont facilité information, logistique et participation précoce en Égypte ainsi que la coalition/information en Tunisie. Aucun de ces mécanismes ne ferme cependant `acteur extérieur -> tasking -> déclenchement -> chute du régime`. Le contrôle April 6 de 2008 montre qu’une forte audience Facebook peut ne pas produire une mobilisation de rue réussie, et le cas tunisien impose de distinguer catalyse numérique et origine domestique du soulèvement. Soutien != déclenchement ; formation != tasking ; réseau social != révolution ; participation != changement de régime attribuable.

## Registre causal certifié

- `assistance démocratique extérieure -> ressources/capacité de société civile` = **SUPPORTED** — Capacité institutionnelle fermée, tasking non inféré.
- `formation CANVAS -> apprentissage tactique -> transmission interne à April 6` = **SUPPORTED** — Transfert de méthode établi pour un acteur; effet marginal sur le soulèvement non isolé.
- `usage réseaux sociaux -> information/logistique -> participation au premier jour en Égypte` = **SUPPORTED** — Association multivariée forte et mécanisme plausible; pas d’assignation randomisée ni effet sur issue du régime.
- `réseaux sociaux -> coalition/mobilisation -> chute de régime en Tunisie` = **UNRESOLVED** — Catalyse informationnelle/coalition soutenue; déclenchement et résultat non isolés.
- `assistance extérieure + plateformes -> soulèvement -> changement de régime` = **UNRESOLVED** — Contributions intermédiaires documentées; causalité générale du changement de régime non établie.

## Gaps matériels certifiés

- `CLM-003` / **CAUSALITY** — Aucune instruction authentifiée reliant un financeur/État à la décision de lancer, au plan opérationnel ou à l’issue du soulèvement; le câble cité doute lui-même d’un plan coordonné.
- `CLM-006` / **CAUSALITY** — Les données ferment des mécanismes de capacité, diffusion et participation mais pas le contrefactuel de régime; répression, griefs locaux, coalitions et décisions des élites restent des causes concurrentes non isolées.

## RENARD

`NO`

## Reclassification

Impact direct : `NONE`.

## Transition attendue

`INV-016 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
