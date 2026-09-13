---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-014-RUN-HANDOFF"
version: "1.1-kiss"
status: "terminal"
updated: "2026-09-09"
inv_id: "INV-014"
run_id: "20260909-0718-color-revolutions-assistance-endogenous"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-015;INV-016"
---

<!-- TRACE: single_post_run_artifact=true; certified_delivery_sha256=b64393da73833543db8f3e9b61b72c2062104d30b98bce4fa87a95809bce85fc -->
<!-- CAUSAL_CEILING: assistance_to_capacity=VERIFIED; capacity_to_fraud_detection=VERIFIED_CASE_SPECIFIC; assistance_to_turnover=NOT_IDENTIFIED; common_foreign_command=NOT_ESTABLISHED -->

# RUN_HANDOFF — INV-014

- **INV_ID:** `INV-014`
- **Certified TE:** `DELIVERY_PASS_R3P1` — `INV-014_INVESTIGATION.md` — SHA-256 `b64393da73833543db8f3e9b61b72c2062104d30b98bce4fa87a95809bce85fc`.
- **Central delta:** l'assistance extérieure est directement documentée dans les quatre environnements, mais sa meilleure arête probatoire est `assistance -> capacité domestique` (formation, monitoring, polling, médias, administration électorale, conseil organisationnel). Dans plusieurs cas, ces capacités alimentent la détection publique de fraude. Le corpus ne ferme ni un commandement étranger commun, ni un effet nécessaire/suffisant ou marginal identifiable de l'aide sur le changement final de dirigeant.
- **Highest supported edge:** `external assistance -> domestic organizational/election-integrity capacity = VERIFIED multi-case`; `monitoring/polling -> fraud visibility = VERIFIED case-specific`; `assistance -> mass mobilization -> turnover = UNRESOLVED/NOT_IDENTIFIED`.
- **Contradictory review / causal ceiling:** Serbie fournit la chaîne d'assistance directe la plus forte; Géorgie et Ukraine combinent assistance, fraude documentée, acteurs domestiques et remèdes institutionnels; Kirghizistan est un contrôle négatif matériel, avec mobilisation davantage localiste/fragmentée malgré assistance et diffusion tactique. `similar tactics != common command` reste fermé comme garde.
- **Material gaps:** aucun dessin causal cross-case n'isole l'effet marginal de l'assistance sur mobilisation/turnover; pas de ledger exhaustif comparable de financement direct des mouvements; aucune chaîne authentifiée commune de tasking/commandement n'a été établie.
- **RENARD:** `NO` — une collecte supplémentaire générique serait cumulative. Réouvrir seulement sur documents authentifiés fermant `funding/training -> tasking/control`, ou sur design causal crédible fermant l'effet marginal sur mobilisation/résultat.
- **New ideas triaged:** `INV-015=REVIEW` uniquement pour le résidu post-2000 Otpor/CANVAS/export institutionnalisé; `INV-016=REVIEW` pour vérifier si les printemps arabes apportent un mécanisme discriminant au-delà de la simple diffusion du répertoire.
- **Expected mechanical transition:** `INV-014 TE_ACTIVE -> CLOSED`, `truth_engine=DELIVERY_PASS_R3P1`, `renard=NO`, `result_path=INV-014_RUN_HANDOFF.md`.
