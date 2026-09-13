---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-092"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-109"
updated: "2026-09-09"
---

# RUN_HANDOFF — INV-092

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260909-1331-generative-ai-deepfake-influence`
- Deliverable: `INV-092_INVESTIGATION.md`
- Deliverable SHA-256: `34b10ad348129aebddda129fe9698dc5bfc7cc9afe532152ad084acb62c04d95`
- Corpus runtime: `QRY=27 / SRC=16 / FCT=28 / provenance_families=5`
- Persistence: `PASS / eligible=28 / blocked=28 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

L'IA générative est désormais documentée comme composant opérationnel réel d'opérations d'influence. Le delta le plus robuste n'est pas un nouveau pouvoir magique de persuasion mais une baisse de friction : production, traduction, reformulation, cadence et volume augmentent, tandis que distribution et acquisition d'audience authentique restent des contraintes distinctes.

Les dénominateurs électoraux disponibles contredisent une lecture simple « plus d'incidents = plus d'effet ». Des incidents sont largement détectés, mais plusieurs corpus 2024–2025 trouvent une part virale ou nuisible faible et aucun effet significatif identifié sur les résultats électoraux étudiés.

En revanche, les expériences randomisées récentes ferment une arête différente : sous exposition contrôlée, des dialogues politiques interactifs avec une IA et des messages générés par LLM peuvent déplacer préférences, choix rapportés et attitudes. Ce résultat établit une capacité de persuasion expérimentale, pas un effet de terrain France/UE.

## Registre causal certifié

- `model/tool access -> automated generation/translation/reformulation -> lower linguistic friction and higher content volume/speed` = **SUPPORTED** — Productivity gain does not itself establish distribution, audience acquisition or persuasion.
- `AI-assisted content production -> distribution through existing channels -> authentic audience exposure` = **UNRESOLVED** — Incident detection and synthetic-content presence do not identify a common exposure denominator or virality mechanism.
- `interactive LLM political conversation or generated persuasive message -> exposed participant -> changed candidate preference/reported vote choice/policy attitude` = **SUPPORTED** — Experimental treatment effects establish persuasion under controlled exposure, not population-scale field election effects.
- `AI/deepfake/automation deployment in France/EU election environment -> population exposure -> changed turnout/vote/election result` = **UNRESOLVED** — Experimental susceptibility and incident visibility are upstream of actual field behavior and election outcomes.
- `higher synthetic-media realism -> reduced human discernment -> potential deception advantage` = **SUPPORTED** — Imperfect detection does not imply unique credibility, persuasion, virality or behavioral effect.

## Gaps matériels certifiés

- `CLM-003` / **MEASUREMENT** — Cross-platform population exposure and comparable denominator data are missing for France/EU; reporting intensity and detection differ by platform and election.
- `CLM-005` / **CAUSALITY** — No France/EU field design in the inspected corpus links identified AI-mediated exposure to individual behavior and aggregate electoral outcomes with a credible counterfactual.
- `CLM-006` / **CAUSALITY** — External validity, real-world repeated exposure, targeting quality, platform distribution and conversion from expressed preference to actual vote remain unresolved.

## RENARD

`NO`

## Reclassification

Impact direct : `INV-109`.

## Transition attendue

`INV-092 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
