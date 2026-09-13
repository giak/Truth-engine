---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-043-RUN-HANDOFF"
version: "1.1-kiss"
status: "terminal"
updated: "2026-09-09"
inv_id: "INV-043"
run_id: "20260909-1037-dsa-information-governance"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-123"
---

<!-- TRACE: single_post_run_artifact=true; certified_delivery_sha256=35a6d5cf1ebf6e4d9562a912c084a5841c9825b4c5f57d2e4f0e4127d8b8db06 -->
<!-- CAUSAL_CEILING: dsa_to_procedures_transparency_redress=VERIFIED; trusted_flagger_to_priority_review=VERIFIED; trusted_flagger_to_automatic_state_removal=NOT_ESTABLISHED; dsa_to_platform_system_change=VERIFIED_CASE_SPECIFIC; dsa_to_general_opinion_election_effect=NOT_IDENTIFIED -->

# RUN_HANDOFF — INV-043

- **INV_ID:** `INV-043`
- **Certified TE:** `DELIVERY_PASS_R3P1` — `INV-043_INVESTIGATION.md` — SHA-256 `35a6d5cf1ebf6e4d9562a912c084a5841c9825b4c5f57d2e4f0e4127d8b8db06`.
- **Central delta:** le DSA est une architecture multiniveau de gouvernance des plateformes, pas un mécanisme unique de retrait. Il ferme `règle -> procédures de notification/transparence/recours/supervision` et, case-specifically, `supervision -> modification de systèmes/processus`. Les signaleurs de confiance obtiennent une priorité de traitement, mais le corpus n’établit pas `trusted flagger -> ordre automatique de retrait`. Les recours produisent des renversements matériels ; parallèlement, la très grande majorité des décisions de modération déclarées provient des règles propres des plateformes, contrôle négatif contre `DSA -> toute modération`.
- **Highest supported edge:** `DSA -> notification/transparency/redress/supervision procedures = VERIFIED`; `trusted flagger -> priority review = VERIFIED`; `moderation -> appeal -> reversal/restoration = VERIFIED case-specific`; `systemic-risk supervision -> platform system/process change = VERIFIED case-specific`; `DSA -> general opinion/debate/election outcome = NOT_IDENTIFIED`.
- **Contradictory review / causal ceiling:** injonction publique, notice ordinaire, trusted flagger, décision de plateforme et supervision systémique sont des mécanismes distincts. Une procédure Commission n’est pas une constatation finale ; un renversement en recours ne prouve pas l’illégalité initiale ; la transparence n’est pas un effet comportemental ; la modération sous conditions propres d’une plateforme n’est pas automatiquement causée par le DSA.
- **Material gaps:** chaîne décisionnelle nominative `public authority -> specific moderation restriction -> exposure/behavior`; dénominateur causal distinguant DSA, règles propres des plateformes et autres droits nationaux ; designs crédibles reliant le DSA à exposition politique, opinion ou résultat électoral.
- **RENARD:** `NO` — collecte générique supplémentaire cumulative. Réouvrir seulement sur une chaîne décisionnelle publique nominative vers une restriction spécifique, ou sur un design causal robuste identifiant un effet du DSA sur exposition/comportement/résultat politique.
- **New ideas triaged:** `INV-123=REVIEW` car le résultat DSA borne directement la composante modération/pouvoir normatif de Big Tech. Les dossiers fermés `INV-089/090/091` servent de comparateurs déjà acquis ; les autres proximités informationnelles ne changent pas matériellement de mécanisme et restent REUSE. `INV-040` est une synthèse dépendante : son changement de dépendance est laissé au planner mécanique.
- **SOURCE_LEADS:** Commission DSA transparency/impact pages; EU trusted-flagger registry; Arcom DSA obligations/trusted flaggers; DSA Transparency Database; Appeals Centre Europe. Navigation hints only; fresh FETCH required before any evidentiary reuse.
- **Mechanical registry transition expected:** `TE_ACTIVE -> CLOSED`; `truth_engine=DELIVERY_PASS_R3P1`; `renard=NO`; `result_path=INV-043_RUN_HANDOFF.md`; next winner determined only by full-pool merged ranking.
