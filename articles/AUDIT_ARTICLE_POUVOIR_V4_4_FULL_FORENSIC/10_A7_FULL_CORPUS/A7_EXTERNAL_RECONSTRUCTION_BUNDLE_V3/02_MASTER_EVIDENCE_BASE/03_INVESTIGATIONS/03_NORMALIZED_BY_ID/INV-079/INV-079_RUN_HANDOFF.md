---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
artifact_id: "INV-079-RUN-HANDOFF"
version: "1.0"
status: "terminal"
updated: "2026-09-07"
inv_id: "INV-079"
---

<!-- TRACE: method_pack_section=10; runtime=2.10.6/R3P1; te_status=DELIVERY_PASS_R3P1 -->

# RUN_HANDOFF — INV-079

## INV_ID

`INV-079`

## TE status/path

`DELIVERY_PASS_R3P1`  
`INV-079_INVESTIGATION.md`

## Central delta

Des financements publics récurrents et matériels soutiennent en France et dans l’UE des capacités de lutte contre haine/discrimination, radicalisation, désinformation et d’éducation aux médias. Les programmes documentent priorités, sélection, ressources, livrables et contrôles. Cela établit une économie publique de capacité et d’agenda programmatique, pas un commandement éditorial ou de modération transversal. `funding -> capacity/output` est fermé dans des cas bornés ; `funding -> dictated content/moderation -> political effect` ne l’est pas.

## Highest supported I0..I7

`I0-I2 = VERIFIED`  
`I3-I4 = VERIFIED/PARTIAL bounded`  
`I5 = NOT_ESTABLISHED generally`  
`I6 = NOT_ESTABLISHED`  
`I7 = NOT_ESTABLISHED`

## Material gaps/contradictions

- subvention, marché et partenariat ne sont pas des véhicules équivalents ;
- concentration/renouvellement des bénéficiaires incomplets ;
- tasking de contenu et workflow de modération non établis transversalement ;
- effet causal politique/électoral non établi.

## RENARD decision + reason

`NO` — il faut des datasets complets, contrats/instructions ou designs causaux ; recherche générique additionnelle cumulative.

## New ideas triaged

- économie politique de la contre-ingérence : `INV-144` ;
- infrastructure de qualification/fact-checking : `INV-088` ;
- Fonds Marianne reste un cas séparé : `INV-078` ;
- ne pas ouvrir de nouvel ID sur le seul constat d’une subvention publique.

## Registry patch

`INV-079 TE_ACTIVE -> CLOSED`  
`truth_engine = DELIVERY_PASS_R3P1`  
`renard = NO`  
`result_path = INV-079_RUN_HANDOFF.md`  
Route terminal delta to `INV-088`, `INV-144`.
