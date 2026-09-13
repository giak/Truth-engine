---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-069-RUN-HANDOFF"
version: "1.0"
status: "CLOSED"
updated: "2026-09-08"
inv_id: "INV-069"
run_id: "20260908-1828-government-communication-france"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
---

<!-- TRACE: terminal_handoff=true; certified_delivery_sha256=47c169f73ec4217992935b26ba3066ec172254e2b058db32073dd0eeda73c681 -->

# RUN_HANDOFF — INV-069

- **INV_ID:** INV-069
- **TE status/path:** `DELIVERY_PASS_R3P1` — `2026-09-08_18-28_government-communication-france_INVESTIGATION.md`
- **Central delta:** une infrastructure gouvernementale centralisée de communication, analyse d'opinion, achat média, segmentation, partenariats et mesure d'exposition est établie ; des objectifs comportementaux existent case-specifically ; la conversion générale en usage partisan ou effet causal sur préférences, comportement ou scrutin n'est pas établie.
- **Highest supported I0..I7:** infrastructure/targeting/exposure `VERIFIED`; behavioral objective `VERIFIED case-specifically`; causal behavior/electoral effect `NOT_ESTABLISHED generally`.
- **Material gaps:** tasking partisan authentifié ; causalité campagne -> comportement/vote/décision ; dénominateur exhaustif dépenses/prestataires si matériel.
- **RENARD:** `NO` — réouvrir seulement sur ces classes probatoires discriminantes.
- **Controls preserved:** `public_communication != propaganda`; `budget != persuasion`; `objective != effect`; `reach != behavior`; `institution != party`; `campaign_metric != electoral_effect`.
- **Registry patch:** `TE_ACTIVE -> CLOSED`; `truth_engine=DELIVERY_PASS_R3P1`; `renard=NO`; `result_path=INV-069_RUN_HANDOFF.md`.
