---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-121"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "NONE"
updated: "2026-09-11"
---

# RUN_HANDOFF — INV-121

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260911-0740-pharma-influence`
- Deliverable: `INV-121_INVESTIGATION.md`
- Deliverable SHA-256: `157591f61bffb1253ff105a2e03cbe2100cbcd58a8162aaca5075b5639eea944`
- Corpus runtime: `QRY=10 / SRC=10 / FCT=12 / provenance_families=5`
- Persistence: `PASS / eligible=12 / blocked=12 / success=0 / failure=0 / fabricated_memory_ids=0`

## Delta central

INV-121 ferme un résultat borné : des entreprises pharmaceutiques déclarent un lobbying précis sur PLFSS, financement et régulation, tandis que l’EMA reconnaît et encadre des risques réels de conflits d’intérêts et d’interactions pré-soumission. Le refus d’Aduhelm fournit cependant un contrôle direct contre un modèle de détermination mécanique par le sponsor, et le dossier Pfizer/messages ferme une défaillance de transparence et d’archivage sans fermer une causalité sur prix, quantité ou clauses du marché. Les capacités d’influence et les risques d’intégrité sont donc établis ; aucune capture actor-specific d’une recommandation, autorisation, remboursement ou procurement n’est démontrée dans l’échantillon.

## Registre causal certifié

- `pharma lobbying -> meetings/expertise -> PLFSS amendment or regulatory delta` = **UNRESOLVED** — Access and stated persuasion intent are not sufficient causal attribution.
- `industry interest -> expert conflict risk -> EMA disclosure/restriction controls -> constrained participation` = **SUPPORTED** — Controls reduce risk but cannot prove absence of all bias.
- `sponsor dossier/scientific advice -> EMA evaluation -> marketing authorisation` = **SUPPORTED** — One refusal is a falsifying control against mechanical capture, not a prevalence estimate.
- `pre-submission interaction -> perception/bias risk -> separation/transparency reforms` = **SUPPORTED** — Risk management does not itself establish that past authorisations were biased.
- `Commission President/pharma CEO contact -> vaccine procurement term -> distributive outcome` = **UNRESOLVED** — Transparency failure cannot substitute for substantive procurement causality.

## Gaps matériels certifiés

- `CLM-002` / **CAUSALITY** — No dated intervention-to-amendment chain isolates the marginal policy effect.
- `CLM-004` / **EVIDENCE** — Aduhelm provides a direct negative-authorisation control despite sponsor dossier and regulator interaction.
- `CLM-006` / **CAUSALITY** — The official findings concern document search/access and do not establish a substantive contact-to-contract causal chain.

## RENARD

`NO`

## Reclassification

Impact direct : `NONE`.

## Transition attendue

`INV-121 TE_ACTIVE -> CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`, puis sélection mécanique du gagnant après REVIEW explicite.
