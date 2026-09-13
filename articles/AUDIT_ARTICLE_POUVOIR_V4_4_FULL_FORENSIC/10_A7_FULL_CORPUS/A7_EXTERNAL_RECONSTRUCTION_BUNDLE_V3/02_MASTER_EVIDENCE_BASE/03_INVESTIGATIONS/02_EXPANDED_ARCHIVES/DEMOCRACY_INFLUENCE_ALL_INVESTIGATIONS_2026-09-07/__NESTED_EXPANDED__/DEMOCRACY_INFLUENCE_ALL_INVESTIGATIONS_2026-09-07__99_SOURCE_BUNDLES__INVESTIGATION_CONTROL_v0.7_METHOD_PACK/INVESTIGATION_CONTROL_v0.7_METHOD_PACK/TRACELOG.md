# TRACELOG — append-only

Format : `YYYY-MM-DD HH:MM | EVENT | INV-ID | détail court`

2026-09-05 00:00 | INIT | GLOBAL | Création du registre maître, dashboard dérivé et workflow de suivi.
2026-09-05 00:00 | BASELINE | GLOBAL | 112 investigations candidates + 12 idées complémentaires enregistrées.
2026-09-05 00:00 | DECISION | GLOBAL | INV-001 puis INV-002 obligatoires avant confirmation du triage global.
2026-09-05 00:00 | RENARD | GLOBAL | Intégration delta-only ; corrections R1-R7 requises avant usage canonique.
2026-09-05 16:18 | INV-001_FAIL | INV-001 | Corpus non canonique: index/CSV/HTML divergent; snapshot 2026-08-26 non courant; INV-002 maintenue BLOCKED.
2026-09-05 16:45 | BASELINE_FREEZE | INV-001 | Corpus explicitement gelé au 2026-08-26; baseline canonique reconstruite à 121 articles + 8 exclusions tracées.
2026-09-05 16:45 | INV-001_PASS | INV-001 | Replay structurel PASS: index=CSV=HTML=121, IDs uniques=121, 0 ligne index malformée, 0 doublon exact; INV-002 passe READY.
2026-09-05 16:55 | DISPOSITION | INV-001 | `181863121.truth-engine-lia-qui-revolutionne` confirmé comme brouillon; statut -> DRAFT_EXCLUDED; aucun impact sur CANONICAL_COUNT=121 ni sur PASS.

2026-09-05 16:38 | PASS | INV-002 | Cartographie 121 articles terminée. 42 SUBSTANTIAL_PRIOR / 73 PARTIAL / 9 NEW sur les 124 sujets initiaux; 78 requalifications; 5 nouveaux gaps ajoutés (INV-125..129). Aucun claim re-fact-checké par INV-002. HUMAN_REVIEW requis avant INV-003+.

2026-09-05 | BACKLOG-AUDIT | v0.5 flat backlog rejected for industrial execution. v0.6 refactor: control specs separated, 6 merges, 11 syntheses gated, elite-network cases conditional, Maroc/Algérie split, final systemic synthesis added, 5-run pilot gate introduced. No content investigation launched.
2026-09-05 | BACKLOG-AUDIT-R1 | Removed pseudo-precise Wave1/2/3 ordering after detecting 88 items in Wave1. Replaced by MAIN_DYNAMIC: one next item selected after each result by model_change/discrimination/dependency unlock/gap/utility.
2026-09-05 | METHOD_PACK | GLOBAL | Built v0.1 from INV-003..008 + Truth Engine v2.10.6 + corrected RENARD integration. Static audit PASS. No content investigation launched. Pilots blocked by HUMAN_REVIEW_METHOD_PACK.
2026-09-05 | METHOD_PACK-R1 | GLOBAL | Removed manual SCOPE_NOTE drift from sample INV-010 card; sample now regenerates exactly from canonical registry.
