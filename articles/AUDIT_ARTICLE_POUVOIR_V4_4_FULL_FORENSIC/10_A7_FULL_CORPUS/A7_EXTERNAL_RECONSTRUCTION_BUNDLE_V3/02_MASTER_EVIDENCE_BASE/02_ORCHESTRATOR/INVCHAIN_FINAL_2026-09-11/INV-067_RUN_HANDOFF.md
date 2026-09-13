---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-067-RUN-HANDOFF"
version: "1.1-kiss"
status: "terminal"
updated: "2026-09-09"
inv_id: "INV-067"
run_id: "20260909-0917-public-expert-groups-composition"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-041;INV-065;INV-121"
---

<!-- TRACE: single_post_run_artifact=true; certified_delivery_sha256=fcb577e310739089965dd695302ea78c805ea984463fd7a7a17c064f01bda3c7 -->
<!-- CAUSAL_CEILING: selection_to_composition=VERIFIED; conflict_mismanagement_to_independence_failure=VERIFIED_CASE_SPECIFIC; advice_to_normative_uptake=VERIFIED_CASE_SPECIFIC; composition_to_advice_content=NOT_IDENTIFIED_GENERAL; conflict_composition_to_capture=NOT_ESTABLISHED_GENERAL -->

# RUN_HANDOFF — INV-067

- **INV_ID:** `INV-067`
- **Certified TE:** `DELIVERY_PASS_R3P1` — `INV-067_INVESTIGATION.md` — SHA-256 `fcb577e310739089965dd695302ea78c805ea984463fd7a7a17c064f01bda3c7`.
- **Central delta:** les groupes d’experts publics constituent un canal formel d’accès à l’expertise et peuvent transmettre une influence normative traçable, mais la chaîne doit être décomposée. Les règles de sélection, de classification des membres, de déclaration d’intérêts et de récusation sont réelles ; leur mise en œuvre peut échouer. Le cas CMU ferme `conflit mal géré -> indépendance/classification défaillante`, tandis que la Taxonomie ferme case-specifically `recommandation -> reprise normative`.
- **Highest supported edge:** `authority -> selection/composition -> advice = VERIFIED`; `mismanaged conflict -> independence/classification failure = VERIFIED case-specific`; `advice/recommendation -> normative uptake = VERIFIED case-specific`; `composition/interests -> advice content = NOT_IDENTIFIED generally`; `conflict/composition -> capture = NOT_ESTABLISHED generally`.
- **Contradictory review / causal ceiling:** les dispositifs de transparence, pluralisme et conflit sont des contrôles matériels mais non auto-exécutants ; une affiliation n’est pas automatiquement un conflit ; un avis peut être fortement repris sans devenir juridiquement contraignant ; un défaut de composition ou de conflit ne donne pas le contrefactuel nécessaire pour attribuer la décision finale.
- **Material gaps:** dénominateur complet des groupes France/UE ; traces membre/contribution -> modification d’un avis ; dessins causaux composition -> contenu ; chaînes nominatives conflit -> recommandation -> décision -> effet.
- **RENARD:** `NO` — collecte générique supplémentaire cumulative. Réouvrir uniquement sur une contribution membre-level reliée à un changement de recommandation/texte, ou sur un conflit documenté relié causalement à un résultat décisionnel.
- **New ideas triaged:** `INV-041=REVIEW` pour le rôle des groupes d’experts dans la production réglementaire Commission ; `INV-065=REVIEW` comme contrôle de symétrie sélection/conflits entre expertise publique et médiatique ; `INV-121=REVIEW` car expertise/régulation/conflits pharma recoupe directement le mécanisme. Les autres proximités thématiques restent REUSE.
- **Mechanical registry transition expected:** `TE_ACTIVE -> CLOSED`; `truth_engine=DELIVERY_PASS_R3P1`; `renard=NO`; `result_path=INV-067_RUN_HANDOFF.md`; next winner determined only by full-pool merged ranking.
