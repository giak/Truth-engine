---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-042-RUN-HANDOFF"
version: "1.1-kiss"
status: "terminal"
updated: "2026-09-09"
inv_id: "INV-042"
run_id: "20260909-0833-eu-lobbying-access-revolving-doors"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-041;INV-063;INV-067;INV-120;INV-121;INV-123;INV-126"
---

<!-- TRACE: single_post_run_artifact=true; certified_delivery_sha256=9eac2e11af4e9b61b433f7816a2c54d83ad0ab3902d170386fca10efeace32e2 -->
<!-- CAUSAL_CEILING: resources_expertise_to_access=SUPPORTED_VENUE_SPECIFIC; access_input_to_policy_influence=PARTIAL_CASE_SPECIFIC; revolving_door_to_access=HETEROGENEOUS_GENERAL_EFFECT_NOT_IDENTIFIED; conflict_access_to_capture=NOT_ESTABLISHED_GENERAL -->

# RUN_HANDOFF — INV-042

- **INV_ID:** `INV-042`
- **Certified TE:** `DELIVERY_PASS_R3P1` — `INV-042_INVESTIGATION.md` — SHA-256 `9eac2e11af4e9b61b433f7816a2c54d83ad0ab3902d170386fca10efeace32e2`.
- **Central delta:** le lobbying européen est un canal institutionnalisé de participation et d'expertise, assorti de règles de registre, de conditionnalité et de publication, mais la visibilité reste incomplète. Des asymétries d'accès sont mesurables selon les acteurs et les arènes. La meilleure arête transversale est `ressources/expertise/capacité -> accès`, pas `dépense -> décision`.
- **Highest supported edge:** `resources/expertise -> access = SUPPORTED venue-specific`; `access/input -> policy influence = PARTIAL case-specific`; `revolving door -> access = HETEROGENEOUS, general effect NOT_IDENTIFIED`; `conflict/access -> capture = NOT_ESTABLISHED generally`.
- **Contradictory review / causal ceiling:** les règles de transparence produisent de vraies traces mais ne donnent pas un dénominateur complet des contacts; certains groupes d'affaires ont un avantage d'accès dans certaines arènes mais pas auprès de tous les responsables; des cas de portes tournantes ferment un risque d'intégrité réel sans fermer une capture décisionnelle; des études identifient une influence sur certains dossiers sans établir une capture générale du policy-making européen.
- **Material gaps:** contacts informels/non programmés; contrefactuels décisionnels dossier par dossier; estimation représentative de l'effet marginal des ressources/réunions sur les décisions; chaîne spécifique `conflit/accès -> changement de règle` pour qualifier une capture.
- **RENARD:** `NO` — une collecte générique supplémentaire sur les lobbyistes ou les budgets serait cumulative. Réouvrir seulement sur un legislative footprint décisionnel fermant `input -> amendement -> adoption`, ou sur une porte tournante nommée reliée à un gain d'accès/une action réglementaire mesurable.
- **New ideas triaged:** REVIEW seulement des investigations où INV-042 change directement le mécanisme générique d'accès/expertise/revolving-door/capture : `INV-041`, `INV-063`, `INV-067`, `INV-120`, `INV-121`, `INV-123`, `INV-126`. Les autres proximités thématiques restent REUSE.
- **Mechanical registry transition expected:** `TE_ACTIVE -> CLOSED`; `truth_engine=DELIVERY_PASS_R3P1`; `renard=NO`; `result_path=INV-042_RUN_HANDOFF.md`; next winner determined only by full-pool merged ranking.
