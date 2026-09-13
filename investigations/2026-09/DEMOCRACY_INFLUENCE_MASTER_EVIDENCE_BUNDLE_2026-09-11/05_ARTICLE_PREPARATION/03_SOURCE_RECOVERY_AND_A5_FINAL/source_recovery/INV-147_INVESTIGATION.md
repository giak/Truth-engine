ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260910-2042-double-standard-matched | PARENT_RUN_ID:NONE | AS_OF:2026-09-10
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/dev/shm/inv147_te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-10_double-standard-matched/2026-09-10_20-42_double-standard-matched_INPUT.md | SUBJECT_SLUG:double-standard-matched | SUBJECT_FP:sha256:431d48b831661541391e1352aea8c3b32b21ad8956058b242cdc1a3d50f7595e | INPUT_SHA256:sha256:dfae52661ec779f433aadc39830e760c2bc52924d84e0b90032217b37b1004da
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE principalement 2018-2026; corpus apparié sur design juridique, mandat de détection, qualification institutionnelle et conséquence. Comparer uniquement des mécanismes suffisamment isomorphes et séparer périmètre légal, critères comportementaux, attention institutionnelle et enforcement.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/INFORMATION.md,clusters/NETWORK.md,clusters/TEMPORAL.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# Corps analytique technique — INV-147

## Verdict
La thèse forte d’un double standard géopolitique systématique à mécanisme et preuve comparables n’est pas établie. Le corpus ferme en revanche une asymétrie plus en amont : certains mandats et cadres juridiques sélectionnent explicitement un univers étranger ou non-UE avant l’évaluation cas par cas. La loi française de transparence exclut les mandants des États membres de l’UE; VIGINUM a par définition un mandat d’ingérence numérique étrangère. Ces choix de design peuvent modifier la population des cas observables sans démontrer un seuil de preuve discrétionnairement plus faible contre les adversaires.

## Critères et vocabulaire
La couche opérationnelle VIGINUM contient un contrôle important : le MOI est décrit par comportements et indicateurs techniques et peut être caractérisé avant de connaître identité, origine, intentions ou ressources. La qualification finale INE réintroduit toutefois le critère d’acteur étranger. Le SEAE utilise lui aussi une définition comportementale de FIMI centrée sur manipulation, intention et coordination. À l’inverse, la DGSE emploie dans son audition un vocabulaire propre à sa mission, distinguant lobbying/influence et ingérence-espionnage. Le vocabulaire interinstitutionnel n’est donc pas une métrique homogène.

## Attention et enforcement
La commission d’enquête de 2023 donne un signal d’asymétrie d’attention : Russie et Chine sont présentées comme les deux principales menaces, tandis que le traitement américain est placé à la lisière et contesté par le président de la commission. Mais le désaccord interne, le périmètre, la fréquence des menaces et la disponibilité des preuves empêchent d’attribuer cette allocation au seul camp géopolitique. La suspension de RT/Sputnik constitue une conséquence forte envers un adversaire, mais elle est explicitement confondue par guerre active, contrôle étatique et usage allégué comme outil opérationnel de manipulation. Sans cas allié/domestique isomorphe, elle ne mesure pas un double standard.

## Modèle explicatif
Le meilleur modèle courant est hybride : `design juridique/mandat -> population observable`, puis `propriétés du mécanisme + preuve + contexte -> qualification/procédure/consequence`. Une asymétrie d’attention peut s’ajouter, mais son origine n’est pas isolée. Le modèle `camp -> seuil de preuve/enforcement systématiquement différent` reste non établi faute de corpus apparié et surtout de dénominateurs.

## Limite décisive
Le registre HATVP est trop récent pour calculer des taux comparables d’enquête, qualification ou sanction. Un futur test valide devra pré-enregistrer un échantillon de conduites isomorphes, inclure des cas négatifs et domestiques, puis mesurer exposition au dispositif, détection, qualification, procédure et conséquence.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:5|SRC_COMPLETE:10/10

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-10
- **breaks:**
  - 2021 création VIGINUM
  - 2022 sanctions RT/Sputnik en contexte de guerre
  - 2023 commission AN et formalisation FIMI
  - 2025 entrée en vigueur registre HATVP
  - 2026 mise à jour critères/méthodes VIGINUM
- **status:** CURRENT
- **window:** France/UE principalement 2018-2026; FARA comme comparateur juridique seulement

### MANIPULATION_REPORT
- **assumptions:**
  - official definitions establish institutional criteria, not fairness of application
  - a parliamentary debate records positions and scope choices, not causal proof of bias
  - war sanctions are not directly comparable to ordinary foreign media regulation
- **clusters:**
  - POWER
  - INFORMATION
  - NETWORK
  - TEMPORAL
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - **I01:** mandates pre-select observable case populations
  - **I02:** mechanism criteria can coexist with origin-based legal scope
  - **I03:** attention asymmetry need not imply evidentiary discrimination
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - **P01:** legal-scope asymmetry
  - **P02:** attention selection
  - **P03:** mechanism-first technical characterization
  - **P04:** enforcement confounding
  - **P05:** terminology instability
- **priorities:**
  - pair mechanisms before camps
  - separate design from enforcement
  - require denominators for rates
  - use mechanism-based negative controls
- **query_guidance:** fresh-fetch every material source; prioritize official legal and institutional documents; reject unmatched comparisons
- **rhetorical:**
  - **R01:** counting adversary cases without denominator
  - **R02:** comparing sanctions across non-isomorphic contexts
  - **R03:** treating institutional vocabulary as a common metric
- **speaker:**
  - **goal:** test matched ally/adversary/domestic double-standard hypothesis
  - **target:** same mechanism+proof -> label/procedure/consequence
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** camp
  - **S02:** mandate
  - **S03:** legal_scope
  - **S04:** mechanism
  - **S05:** visibility
  - **S06:** tasking
  - **S07:** behavior
  - **S08:** attribution
  - **S09:** evidence
  - **S10:** label
  - **S11:** procedure
  - **S12:** consequence
  - **S13:** denominator
  - **S14:** context
  - **S15:** counterfactual
- **threats:**
  - camp=mechanism
  - vocabulary=evidence
  - legal design=enforcement bias
  - threat priority=proof threshold
  - foreign-only mandate=discretionary bias
  - war sanction=matched case
  - unmatched absence=immunity

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - mature French registry history and matched outcomes
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-020
    - FCT-021
    - FCT-022
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no comparable enforcement denominator
  - **not_computable:**
    - probability of investigation/sanction by camp
  - **operations_applied:**
    - mapped mandate/legal scope to obligations/exemptions
    - separated specific sanction chain from camp-wide enforcement
  - **reason:** separate institutional authority/design from discretionary application
  - **result_ids:**
    - CLM-002
    - CLM-006
    - CLM-007
    - CLM-008
    - CAU-001
    - CAU-004
    - CAU-005
  - **status:** DONE
  - **trigger:** legal scope and enforcement claims
- **item 2:**
  - **gaps:**
    - coded matched label corpus
  - **input_ids:**
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
    - FCT-017
    - FCT-018
  - **module:** clusters/INFORMATION.md
  - **negative_results:**
    - no uniform cross-institution vocabulary metric
  - **not_computable:**
    - systematic media vocabulary rate by camp
  - **operations_applied:**
    - mapped technical criteria and terminology
    - tested vocabulary != evidence
  - **reason:** separate behavioral observables from geopolitical label
  - **result_ids:**
    - CLM-004
    - CLM-005
    - CAU-003
  - **status:** DONE
  - **trigger:** label/vocabulary and FIMI/INE characterization
- **item 3:**
  - **gaps:**
    - authenticated tasking in matched cases
  - **input_ids:**
    - FCT-001
    - FCT-012
    - FCT-014
    - FCT-021
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - origin alone does not establish command
  - **not_computable:**
    - latent principals outside public record
  - **operations_applied:**
    - separated foreign relation, coordination and tasking
  - **reason:** prevent foreign relation from substituting for command/control proof
  - **result_ids:**
    - CLM-001
    - CLM-004
    - CAU-003
  - **status:** DONE
  - **trigger:** actor relation/tasking criteria
- **item 4:**
  - **gaps:**
    - future registry observations
  - **input_ids:**
    - FCT-004
    - FCT-019
    - FCT-020
    - FCT-021
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - no mature longitudinal French enforcement denominator
  - **not_computable:**
    - long-run comparative enforcement rate
  - **operations_applied:**
    - bounded enforcement window
    - preserved war as confounder
  - **reason:** avoid comparing 2022 sanctions with immature 2025-26 registry outcomes
  - **result_ids:**
    - CLM-006
    - CLM-007
    - CAU-004
  - **status:** DONE
  - **trigger:** regime maturity and war-context comparability

### SCOPING_REPORT
- **excluded:**
  - unmatched media anecdotes
  - partisan media corpus without reproducible sampling
  - raw counts of adversary cases
  - foreign cases lacking comparable French/UE procedure
- **included:**
  - French legal transparency regime
  - HATVP implementation timing
  - 2023 AN scope debate
  - DGSE mechanism vocabulary
  - VIGINUM INE/MOI criteria
  - EEAS FIMI definition
  - RT/Sputnik specific enforcement
  - FARA legal comparator
- **reason:** test double standard only where mechanism, evidence and consequence can be meaningfully separated

### CREDO
- **forbidden_shortcuts:**
  - camp=mechanism
  - vocabulary=proof
  - legal design=enforcement
  - count=rate
  - war sanction=ordinary media case
- **rule:** same-camp labels are not evidence; compare isomorphic conduct and proof before label/consequence

### COGNITIVE_MAP
- **chain:**
  - actor/camp
  - mandate/legal scope
  - mechanism/behavior
  - evidence/attribution
  - label
  - procedure
  - consequence
  - denominator/counterfactual
- **rival_models:**
  - general geopolitical double standard
  - mechanism-driven qualification
  - institutional/legal design asymmetry
  - threat-prevalence/availability selection
  - hybrid model

### DIALECTICAL_MAP
- **antithesis:** Differences can follow mandate, legal scope, mechanism properties, war context, threat prevalence and available evidence rather than camp bias.
- **synthesis:** The corpus establishes upstream design/mandate asymmetries and a partial attention asymmetry, but not a systematic case-level evidentiary or enforcement double standard. Mechanism-based criteria remain a stronger explanation for operational qualification; enforcement requires matched denominators.
- **thesis:** Institutional treatment may systematically be harsher for adversaries than allies/domestic actors at comparable conduct.

### RESOURCE_FLOW_MAP
- **flows:**
  - origin category -> legal scope -> registration obligation/exemption
  - technical behavior -> MOI characterization -> foreign attribution -> INE label
  - threat framing -> investigative attention -> report allocation
  - state control + manipulation + war -> restrictive measure
- **limits:**
  - scope difference != unfair enforcement
  - attention != proof threshold
  - sanction context != matched pair

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** French legislature
  - **relation:** defines non-EU foreign-principal scope
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-005
  - **to:** HATVP registry
- **item 2:**
  - **from:** AN commission/report process
  - **relation:** selects threat/country coverage and debates scope
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-009
  - **to:** public parliamentary framing
- **item 3:**
  - **from:** VIGINUM
  - **relation:** technical MOI analysis plus foreign-actor criterion
  - **support:**
    - FCT-012
    - FCT-014
    - FCT-015
    - FCT-017
  - **to:** INE characterization
- **item 4:**
  - **from:** Council EU
  - **relation:** sanctions state-controlled outlets under war/manipulation context
  - **support:**
    - FCT-020
    - FCT-021
  - **to:** RT/Sputnik broadcasting

### IMPACT_MAP
- **established:**
  - origin/geography-based legal scope asymmetry in French regime
  - foreign-only institutional mandate for INE
  - behavioral/technical pre-attribution analysis layer
  - specific RT/Sputnik enforcement chain under war/state-control context
- **not_established:**
  - systematic lower proof threshold for adversaries
  - systematic vocabulary asymmetry at matched evidence
  - systematic enforcement-rate asymmetry by camp
  - allied immunity
  - domestic-vs-foreign matched sanction bias
- **partial:**
  - parliamentary attention asymmetry between Russia/China and US/other states

### CONTRADICTION_LEDGER
- **item 1:**
  - **issue:** French law explicitly excludes EU member-state mandants
  - **resolution:** classify as legal-design asymmetry only; do not infer selective enforcement or normative injustice
- **item 2:**
  - **issue:** AN report prioritized Russia/China and placed US at edge
  - **resolution:** retain attention asymmetry and internal contestation; do not infer camp as marginal cause without matched threat/evidence controls
- **item 3:**
  - **issue:** VIGINUM is foreign-only but its MOI method is pre-attribution and behavior-centered
  - **resolution:** separate institutional mandate from analytic criteria; both are true
- **item 4:**
  - **issue:** RT/Sputnik received severe enforcement
  - **resolution:** retain sanction as fact but reject unmatched ally/adversary inference due war, state-control and manipulation context
- **item 5:**
  - **issue:** FARA contains strategic-defense exemption
  - **resolution:** retain as comparator showing legal design can encode national-interest relation; current FAQ says no governments currently designated, so do not infer active allied immunity

### VERIFICATION_REPORT
- **facts:** 22
- **method:** official-source matched design; each candidate asymmetry tested against mandate/mechanism/context/denominator controls
- **negative_checks:**
  - VIGINUM pre-attribution MOI
  - AN internal disagreement
  - RT war/state-control confounders
  - immature HATVP history
  - FARA exemption conditions
- **research_queries:** 10
- **sources_fetched:** 10
- **verdict:** sufficient to establish design/mandate asymmetry and reject strong systematic-bias claim as currently unproven; insufficient for enforcement-rate estimation

### EDI_REPORT
- **corpus:** 10 accepted official sources across 7 provenance families
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-002
    - **families:**
      - A
      - B
  - **item 2:**
    - **claim:** CLM-003
    - **families:**
      - C
  - **item 3:**
    - **claim:** CLM-004
    - **families:**
      - D
  - **item 4:**
    - **claim:** CLM-006
    - **families:**
      - F
  - **item 5:**
    - **claim:** CLM-008
    - **families:**
      - A
      - B
      - C
      - D
      - E
      - other:council
      - other:doj
- **diagnostic_not_truth:** true
- **dimensions:**
  - law
  - registry implementation
  - parliamentary framing
  - intelligence terminology
  - technical characterization
  - EU external policy
  - sanctions
  - US comparator
- **edi:** DIVERSE_OFFICIAL_INSTITUTIONAL_PROVENANCE_WITH_MANDATE_BIAS_EXPLICIT
- **source_counts:**
  - **A:** 1
  - **B:** 1
  - **C:** 2
  - **D:** 3
  - **E:** 1
  - **other:council:** 1
  - **other:doj:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** Législateur français / HATVP
  - **documented_action:** définition et mise en œuvre du registre de transparence non-UE
  - **intent:** PROVEN
  - **scope:** legal design/registration; enforcement-rate bias not established
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-004
    - FCT-005
- **item 2:**
  - **actor:** Assemblée nationale commission 2023
  - **documented_action:** hiérarchisation et débat du périmètre des ingérences étudiées
  - **intent:** PROVEN
  - **scope:** attention/framing; systematic bias not established
  - **support:**
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-009
- **item 3:**
  - **actor:** VIGINUM
  - **documented_action:** détection/caractérisation INE et analyse MOI
  - **intent:** PROVEN
  - **scope:** foreign digital interference; method partly pre-attribution
  - **support:**
    - FCT-012
    - FCT-013
    - FCT-014
    - FCT-015
    - FCT-016
    - FCT-017
- **item 4:**
  - **actor:** SEAE
  - **documented_action:** définition et politiques de réponse FIMI
  - **intent:** PROVEN
  - **scope:** foreign information manipulation; not domestic comparator
  - **support:**
    - FCT-018
    - FCT-019
- **item 5:**
  - **actor:** Conseil de l’Union européenne
  - **documented_action:** suspension RT/Sputnik
  - **intent:** PROVEN
  - **scope:** specific war/manipulation enforcement; no camp-wide inference
  - **support:**
    - FCT-020
    - FCT-021
- **item 6:**
  - **actor:** DOJ/FARA framework
  - **documented_action:** application d’un régime d’enregistrement avec exemptions légales
  - **intent:** PROVEN
  - **scope:** US legal comparator only
  - **support:**
    - FCT-022

### NEXT_QUERIES
- Do not claim systematic enforcement bias until a denominator exists for comparable conduct, detection, investigation and sanction.
- Revisit HATVP longitudinally only after a materially mature enforcement history exists.
- If a reproducible media-label corpus is built, pre-register matching fields and coding rules before inspecting camp outcomes.
- Feed upstream mandate/legal-design asymmetry and non-result on systematic evidentiary/enforcement bias into final systemic synthesis.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-011,QRY-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-022 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-003,QRY-004,QRY-013,QRY-014 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-005,QRY-006,QRY-007,QRY-015,QRY-016,QRY-017 | support:- | counter:- | results:FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-008,QRY-009,QRY-010,QRY-018,QRY-019,QRY-020 | support:- | counter:- | results:FCT-018,FCT-019,FCT-020,FCT-021,FCT-004,FCT-022 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-003,QRY-005,QRY-008,QRY-010 | support:- | counter:- | results:FCT-002,FCT-006,FCT-008,FCT-012,FCT-014,FCT-020,FCT-022 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-003,QRY-004,QRY-005,QRY-006,QRY-008,QRY-009,SRC-003,SRC-004,SRC-005,SRC-006,SRC-008,SRC-009 | support:FCT-006,FCT-008,FCT-019,FCT-020 | counter:FCT-009,FCT-010,FCT-011,FCT-012,FCT-014,FCT-018 | results:FCT-006,FCT-008,FCT-019,FCT-020,FCT-009,FCT-010,FCT-011,FCT-012,FCT-014,FCT-018 | final:PARTIAL | gap:DENOMINATOR
CLM-002 | attempts:QRY-001,QRY-002,SRC-001,SRC-002 | support:FCT-001,FCT-002,FCT-003,FCT-005 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-005 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-003,QRY-004,SRC-003,SRC-004 | support:FCT-006,FCT-007,FCT-008 | counter:FCT-009,FCT-010 | results:FCT-006,FCT-007,FCT-008,FCT-009,FCT-010 | final:PARTIAL | gap:CAUSALITY
CLM-004 | attempts:QRY-005,QRY-006,QRY-007,SRC-005,SRC-006,SRC-007 | support:FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017 | counter:FCT-012 | results:FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-012 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-004,QRY-005,QRY-008,SRC-004,SRC-005,SRC-008 | support:- | counter:FCT-011,FCT-012,FCT-018 | results:FCT-011,FCT-012,FCT-018 | final:REFUTED | gap:SEMANTIC
CLM-006 | attempts:QRY-009,SRC-009 | support:FCT-020,FCT-021 | counter:FCT-020,FCT-021 | results:FCT-020,FCT-021,FCT-020,FCT-021 | final:PARTIAL | gap:MATCHING
CLM-007 | attempts:QRY-002,SRC-002 | support:FCT-004 | counter:FCT-004,FCT-005 | results:FCT-004,FCT-004,FCT-005 | final:REFUTED | gap:DENOMINATOR
CLM-008 | attempts:QRY-001,QRY-002,QRY-003,QRY-005,QRY-006,QRY-008,QRY-009,QRY-010,SRC-001,SRC-002,SRC-003,SRC-005,SRC-006,SRC-008,SRC-009,SRC-010 | support:FCT-002,FCT-005,FCT-009,FCT-012,FCT-014,FCT-018,FCT-020,FCT-022 | counter:FCT-006,FCT-008,FCT-019 | results:FCT-002,FCT-005,FCT-009,FCT-012,FCT-014,FCT-018,FCT-020,FCT-022,FCT-006,FCT-008,FCT-019 | final:SUPPORTED | gap:NONE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-001 | CLM | PARTIAL | DENOMINATOR | Pas de dataset suffisamment apparié ni de dénominateur commun des conduites détectables, qualifiées, poursuivies et sanctionnées par camp.
CLM-003 | CLM | PARTIAL | CAUSALITY | La sélection peut refléter fréquence de menace, mandat, temps disponible, disponibilité des preuves ou choix éditorial; le corpus ne permet pas d’identifier le camp comme cause marginale.
CLM-005 | CLM | REFUTED | SEMANTIC | DGSE, VIGINUM, SEAE et droit de transparence utilisent des objets et missions différents; un même mot ne constitue pas une métrique sans protocole de codage.
CLM-006 | CLM | PARTIAL | MATCHING | Le cas est confondu par guerre active, contrôle étatique explicite et rôle opérationnel allégué; aucun cas allié/domestique isomorphe dans le corpus ne permet le contre-factuel.
CLM-007 | CLM | REFUTED | DENOMINATOR | Le registre français n’existe que depuis octobre 2025 et le corpus ne contient pas de dénominateur des conduites comparables détectées/non détectées par camp.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | Besoin de corpus codé de cas comparables et variables de menace/preuve/mandat.
CAU-005 | CAU | UNRESOLVED | DENOMINATOR | Matched outcomes et denominator commun manquants.

SEMANTIC_COUNTS_V1:LED:0|CLM:8|AXS:5|CAU:5|CTRL:8|ACT:6

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"À mécanisme et preuve comparables, alliés, adversaires et acteurs domestiques sont systématiquement qualifiés et sanctionnés différemment en France/UE.","claimant":"hypothèse double standard forte","counter":["FCT-009","FCT-010","FCT-011","FCT-012","FCT-014","FCT-018"],"gap":"Pas de dataset suffisamment apparié ni de dénominateur commun des conduites détectables, qualifiées, poursuivies et sanctionnées par camp.","gap_type":"DENOMINATOR","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-006","FCT-008","FCT-019","FCT-020"]}
CLM-002 | {"claim":"Le design juridique français introduit une asymétrie explicite de périmètre selon l’origine du mandant, notamment par l’exclusion des États membres de l’UE.","claimant":"INV-147","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-005"]}
CLM-003 | {"claim":"La commission d’enquête de 2023 montre une asymétrie d’attention observable vers Russie/Chine et une marginalisation relative du cas américain dans le projet de rapport.","claimant":"INV-147","counter":["FCT-009","FCT-010"],"gap":"La sélection peut refléter fréquence de menace, mandat, temps disponible, disponibilité des preuves ou choix éditorial; le corpus ne permet pas d’identifier le camp comme cause marginale.","gap_type":"CAUSALITY","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-006","FCT-007","FCT-008"]}
CLM-004 | {"claim":"Les critères opérationnels VIGINUM reposent substantiellement sur des propriétés du mécanisme, et le MOI peut être décrit avant attribution de l’acteur.","claimant":"INV-147","counter":["FCT-012"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017"]}
CLM-005 | {"claim":"Le vocabulaire institutionnel est uniforme et directement comparable entre services et cadres juridiques.","claimant":"hypothèse vocabulaire stable","counter":["FCT-011","FCT-012","FCT-018"],"gap":"DGSE, VIGINUM, SEAE et droit de transparence utilisent des objets et missions différents; un même mot ne constitue pas une métrique sans protocole de codage.","gap_type":"SEMANTIC","materiality":"IMPORTANT","status":"REFUTED","support":"NONE_FOUND"}
CLM-006 | {"claim":"La sanction RT/Sputnik établit une préférence punitive envers les adversaires à conduite comparable.","claimant":"hypothèse enforcement bias","counter":["FCT-020","FCT-021"],"gap":"Le cas est confondu par guerre active, contrôle étatique explicite et rôle opérationnel allégué; aucun cas allié/domestique isomorphe dans le corpus ne permet le contre-factuel.","gap_type":"MATCHING","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-020","FCT-021"]}
CLM-007 | {"claim":"Une asymétrie systématique d’enforcement est mesurable avec les données publiques françaises actuelles.","claimant":"hypothèse mesurabilité actuelle","counter":["FCT-004","FCT-005"],"gap":"Le registre français n’existe que depuis octobre 2025 et le corpus ne contient pas de dénominateur des conduites comparables détectées/non détectées par camp.","gap_type":"DENOMINATOR","materiality":"DECISIVE","status":"REFUTED","support":["FCT-004"]}
CLM-008 | {"claim":"Les asymétries observées se décomposent mieux en design de mandat/droit, propriétés du mécanisme, contexte et disponibilité probatoire qu’en un unique biais géopolitique discrétionnaire.","claimant":"INV-147","counter":["FCT-006","FCT-008","FCT-019"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-005","FCT-009","FCT-012","FCT-014","FCT-018","FCT-020","FCT-022"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-011","QRY-012"],"axis":"LEGAL_DESIGN_MATCH","links":["CLM-002","CLM-008","CAU-001"],"question":"À conduite d’influence comparable, le droit définit-il les mandants et exemptions de manière géographiquement ou stratégiquement asymétrique ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-022"],"sought_objects":["MANDANT","CONTROL","EU_EXCLUSION","EXEMPTION","REGISTRATION"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-013","QRY-014"],"axis":"INSTITUTIONAL_ATTENTION","links":["CLM-003","CAU-002"],"question":"Le corpus parlementaire français montre-t-il une sélection d’attention par camp indépendamment du mécanisme et du niveau de preuve ?","result_ids":["FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011"],"sought_objects":["THREAT_PRIORITY","COUNTRY_SCOPE","US_SCOPE","INTERNAL_DISAGREEMENT"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-005","QRY-006","QRY-007","QRY-015","QRY-016","QRY-017"],"axis":"MECHANISM_BEFORE_ATTRIBUTION","links":["CLM-004","CLM-005","CAU-003"],"question":"Les cadres techniques permettent-ils une qualification par comportement avant ou indépendamment du camp géopolitique ?","result_ids":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017"],"sought_objects":["BEHAVIOR","COORDINATION","CLANDESTINITY","ATTRIBUTION","FOREIGN_ACTOR"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-008","QRY-009","QRY-010","QRY-018","QRY-019","QRY-020"],"axis":"ENFORCEMENT_MATCH","links":["CLM-006","CLM-007","CAU-004","CAU-005"],"question":"Peut-on comparer une sanction envers un adversaire à un cas allié/domestique isomorphe, même mécanisme et mêmes circonstances ?","result_ids":["FCT-018","FCT-019","FCT-020","FCT-021","FCT-004","FCT-022"],"sought_objects":["SANCTION","STATE_CONTROL","WAR_CONTEXT","MATCHED_CASE","DENOMINATOR"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-003","QRY-005","QRY-008","QRY-010"],"axis":"MODEL_DISCRIMINATION","links":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-006","CLM-008","CAU-005"],"question":"Les écarts observés sont-ils mieux expliqués par le camp, ou par design juridique/mandat, propriétés du mécanisme, contexte et disponibilité probatoire ?","result_ids":["FCT-002","FCT-006","FCT-008","FCT-012","FCT-014","FCT-020","FCT-022"],"sought_objects":["CAMP","MANDATE","MECHANISM","EVIDENCE","CONTEXT","CONSEQUENCE"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"origin category -> legal scope -> registration duty/exemption","counter":"L’exclusion juridique ne prouve ni immunité pratique ni absence d’autres règles applicables.","limit":"Asymétrie de design fermée; asymétrie d’enforcement non inférée.","mechanism":"origine du mandant -> périmètre juridique -> obligation déclarative ou exclusion","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-005"]}
CAU-002 | {"counter":"Le rapport invoque les auditions des services, d’autres pays sont inclus, et le choix américain est contesté à l’intérieur de la commission.","gap":"Besoin de corpus codé de cas comparables et variables de menace/preuve/mandat.","gap_type":"CAUSALITY","limit":"Attention asymétrique observable; cause géopolitique indépendante non isolée.","mechanism":"camp géopolitique -> priorité parlementaire -> fréquence de qualification publique","status":"UNRESOLVED","support":["FCT-006","FCT-008"]}
CAU-003 | {"causal_right":"technical behavior -> MOI characterization -> foreign attribution criterion -> INE label","counter":"La qualification INE finale inclut structurellement un critère d’acteur étranger.","limit":"Analyse comportementale pré-attribution établie; mandat final reste étranger-only.","mechanism":"comportements techniques coordonnés/clandestins -> caractérisation MOI -> attribution étrangère -> label INE","status":"SUPPORTED","support":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017"]}
CAU-004 | {"causal_right":"state control + manipulation + war context -> EU broadcast suspension","counter":"Ce cas n’est pas apparié à un média d’État allié/domestique sous contexte identique.","limit":"Chaîne spécifique de sanction fermée; aucune généralisation par camp.","mechanism":"contrôle étatique + campagne de manipulation + contexte de guerre -> mesure restrictive RT/Sputnik","status":"SUPPORTED","support":["FCT-020","FCT-021"]}
CAU-005 | {"counter":["FCT-009","FCT-012","FCT-014","FCT-020"],"gap":"Matched outcomes et denominator commun manquants.","gap_type":"DENOMINATOR","limit":"Le design institutionnel peut encoder l’origine ou l’intérêt stratégique, mais l’effet causal sur décisions d’enforcement à conduite identique n’est pas mesuré.","mechanism":"alignement stratégique -> seuil de preuve/qualification/enforcement différentiel à conduite identique","status":"UNRESOLVED","support":["FCT-002","FCT-008","FCT-022"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"camp géopolitique != mécanisme","status":"PASS","support":["FCT-012","FCT-014","FCT-018"]}
CTRL-002 | {"control":"vocabulaire != preuve","status":"PASS","support":["FCT-011","FCT-012","FCT-018"]}
CTRL-003 | {"control":"différence de périmètre légal != biais d’enforcement","status":"PASS","support":["FCT-002","FCT-004","FCT-005"]}
CTRL-004 | {"control":"priorité de menace != seuil probatoire discriminatoire","status":"PASS","support":["FCT-006","FCT-007","FCT-009","FCT-010"]}
CTRL-005 | {"control":"mandat foreign-only != preuve de biais discrétionnaire cas par cas","status":"PASS","support":["FCT-012","FCT-014"]}
CTRL-006 | {"control":"sanction en contexte de guerre != paire isomorphe de média étranger","status":"PASS","support":["FCT-020","FCT-021"]}
CTRL-007 | {"control":"désaccord interne à une commission != standard institutionnel général","status":"PASS","support":["FCT-008","FCT-009"]}
CTRL-008 | {"control":"absence de cas allié apparié != immunité alliée","status":"PASS","support":["FCT-006","FCT-010","FCT-011"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Définition d’un régime déclaratif d’influence étrangère avec exclusion explicite des mandants UE","actor":"Législateur français / HATVP","intent":"PROVEN","status":"DONE","support":["FCT-001","FCT-002","FCT-004","FCT-005"]}
ACT-002 | {"action":"Sélection et hiérarchisation parlementaire des puissances étudiées dans le rapport 2023","actor":"Commission d’enquête de l’Assemblée nationale","intent":"PROVEN","status":"DONE","support":["FCT-006","FCT-007","FCT-008","FCT-009"]}
ACT-003 | {"action":"Caractérisation technique des ingérences numériques étrangères et des MOI","actor":"VIGINUM","intent":"PROVEN","status":"DONE","support":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017"]}
ACT-004 | {"action":"Définition et réponse institutionnelle au FIMI","actor":"SEAE","intent":"PROVEN","status":"DONE","support":["FCT-018","FCT-019"]}
ACT-005 | {"action":"Suspension des activités de diffusion de RT/Sputnik dans le contexte de l’agression russe","actor":"Conseil de l’Union européenne","intent":"PROVEN","status":"DONE","support":["FCT-020","FCT-021"]}
ACT-006 | {"action":"Maintien d’un régime FARA incluant une exemption conditionnelle liée à la défense vitale des États-Unis","actor":"Législateur américain / DOJ FARA","intent":"PROVEN","status":"DONE","support":["FCT-022"]}

SEARCH_ACTIVITY_V1:WEB:10|FETCH:10|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | UNAVAILABLE | mnemolite | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050052952 | fresh fetch for material source
QRY-002 | FETCH | FOUND | SRC-002 | https://www.hatvp.fr/presse/entree-en-vigueur-du-dispositif-dencadrement-de-linfluence-etrangere/ | fresh fetch for material source
QRY-003 | FETCH | FOUND | SRC-003 | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N035.html | fresh fetch for material source
QRY-004 | FETCH | FOUND | SRC-004 | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N012.html | fresh fetch for material source
QRY-005 | FETCH | FOUND | SRC-005 | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/les-missions-de-viginum | fresh fetch for material source
QRY-006 | FETCH | FOUND | SRC-006 | https://www.sgdsn.gouv.fr/publications/definitions-et-objectifs-du-concept-de-mode-operatoire-informationnel-moi | fresh fetch for material source
QRY-007 | FETCH | FOUND | SRC-007 | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-un-reseau-structure-et-coordonne-de-propagande-prorusse | fresh fetch for material source
QRY-008 | FETCH | FOUND | SRC-008 | https://www.eeas.europa.eu/delegations/united-kingdom/tackling-foreign-information-manipulation-and-interference-together_en?s=3225 | fresh fetch for material source
QRY-009 | FETCH | FOUND | SRC-009 | https://www.consilium.europa.eu/fr/press/press-releases/2022/03/02/eu-imposes-sanctions-on-state-owned-outlets-rtrussia-today-and-sputnik-s-broadcasting-in-the-eu/ | fresh fetch for material source
QRY-010 | FETCH | FOUND | SRC-010 | https://www.justice.gov/nsd-fara/fara-index-and-act | fresh fetch for material source
QRY-011 | WEB | FOUND | - | - | France influence foreign principal EU member states exclusion article 18-11
QRY-012 | WEB | FOUND | - | - | HATVP foreign influence registry start enforcement denominator 2025 2026
QRY-013 | WEB | FOUND | - | - | French parliamentary commission foreign interference Russia China United States scope 2023
QRY-014 | WEB | FOUND | - | - | DGSE difference influence interference lobbying friendly states Gulf 2023
QRY-015 | WEB | FOUND | - | - | VIGINUM four criteria foreign digital interference content behavior intention foreign actor
QRY-016 | WEB | FOUND | - | - | VIGINUM information manipulation set technical behavior before attribution identity origin intent
QRY-017 | WEB | FOUND | - | - | Portal Kombat coordinated pro-Russian network France foreign digital interference
QRY-018 | WEB | FOUND | - | - | EEAS FIMI intentional coordinated state non-state proxies foreign
QRY-019 | WEB | FOUND | - | - | RT Sputnik sanctions war state controlled disinformation information manipulation EU
QRY-020 | WEB | FOUND | - | - | FARA foreign government vital defense exemption 22 USC 613f

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | LEGIFRANCE-18-11 | Article 18-11 - transparence des activités influence pour mandant étranger | 2024-07-25 | 2026-09-10T18:45:00+00:00 | scope, control relationship, EU-member-state exclusion, diplomatic exemption | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050052952
SRC-002 | ◈ | fam:B | HATVP-INFLUENCE-2025 | Entrée en vigueur du dispositif encadrement influence étrangère | 2025-10-01 | 2026-09-10T18:45:00+00:00 | registry launch and non-EU scope | https://www.hatvp.fr/presse/entree-en-vigueur-du-dispositif-dencadrement-de-linfluence-etrangere/
SRC-003 | ◈ | fam:C | AN-CE-ING-N035 | Commission enquête ingérences étrangères - examen du rapport compte rendu 35 | 2023-06-01 | 2026-09-10T18:45:00+00:00 | report scope, Russia/China priority, US-edge dispute, other states | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N035.html
SRC-004 | ◈ | fam:C | AN-CE-ING-N012 | Commission enquête ingérences étrangères - audition Bernard Emie compte rendu 12 | 2023-03-02 | 2026-09-10T18:45:00+00:00 | mechanism terminology, hostile/friendly states, Gulf lobbying | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N012.html
SRC-005 | ◈ | fam:D | VIGINUM-MISSIONS-2026 | Les missions de VIGINUM | 2026-05-15 | 2026-09-10T18:45:00+00:00 | four INE criteria and MOI method | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/les-missions-de-viginum
SRC-006 | ◈ | fam:D | VIGINUM-MOI-2026 | Définitions et objectifs du mode opératoire informationnel | 2026-01-22 | 2026-09-10T18:45:00+00:00 | technical behavior before attribution | https://www.sgdsn.gouv.fr/publications/definitions-et-objectifs-du-concept-de-mode-operatoire-informationnel-moi
SRC-007 | ◈ | fam:D | VIGINUM-PORTAL-KOMBAT-2024 | Portal Kombat - réseau structuré et coordonné de propagande prorusse | 2024-02-12 | 2026-09-10T18:45:00+00:00 | foreign digital interference case and behavior | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-un-reseau-structure-et-coordonne-de-propagande-prorusse
SRC-008 | ◈ | fam:E | EEAS-FIMI-2023 | Tackling foreign information manipulation and interference together | 2023-09-28 | 2026-09-10T18:45:00+00:00 | FIMI definition and policy history | https://www.eeas.europa.eu/delegations/united-kingdom/tackling-foreign-information-manipulation-and-interference-together_en?s=3225
SRC-009 | ◈ | fam:other:council | COUNCIL-RT-SPUTNIK-2022 | UE sanctions RT Russia Today et Sputnik | 2022-03-02 | 2026-09-10T18:45:00+00:00 | sanction context, state control, war and manipulation | https://www.consilium.europa.eu/fr/press/press-releases/2022/03/02/eu-imposes-sanctions-on-state-owned-outlets-rtrussia-today-and-sputnik-s-broadcasting-in-the-eu/
SRC-010 | ◈ | fam:other:doj | DOJ-FARA-ACT | Foreign Agents Registration Act - Index and Act | 2026-09-10 | 2026-09-10T18:45:00+00:00 | foreign-principal regime and exemptions including section 613f | https://www.justice.gov/nsd-fara/fara-index-and-act

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050052952 | A | 2025-07-01 | FR_CONTROL_RELATION | La loi française impose une déclaration lorsque la personne agit sur ordre, demande, direction ou contrôle d’un mandant étranger afin d’influer sur une décision ou politique publique. | -
FCT-002 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050052952 | A | 2025-07-01 | FR_EU_EXCLUSION | La définition française du mandant étranger exclut explicitement les États membres de l’Union européenne et les partis issus de ces États. | -
FCT-003 | FACT | ✧ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000050052952 | A | 2025-07-01 | FR_DIPLOMATIC_EXEMPTION | Les personnels diplomatiques et consulaires ainsi que les agents d’un État étranger agissant dans leurs fonctions sont exclus de l’obligation déclarative française. | -
FCT-004 | FACT | ✧ | https://www.hatvp.fr/presse/entree-en-vigueur-du-dispositif-dencadrement-de-linfluence-etrangere/ | B | 2025-10-01 | HATVP_REGISTRY_START | La HATVP a mis en ligne le répertoire de l’influence étrangère le 1er octobre 2025. | -
FCT-005 | FACT | ✧ | https://www.hatvp.fr/presse/entree-en-vigueur-du-dispositif-dencadrement-de-linfluence-etrangere/ | B | 2025-10-01 | HATVP_NON_EU_SCOPE | Le dispositif HATVP vise notamment les personnes agissant pour une puissance hors UE, une entité qu’elle contrôle ou finance majoritairement, ou un parti politique non européen. | -
FCT-006 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N035.html | C | 2023-06-01 | AN_RUSSIA_CHINA_PRIORITY | Lors de l’examen du rapport, la rapporteure indique que les auditions des services ont conduit à traiter Russie et Chine comme les deux principales menaces et à leur consacrer des sous-parties distinctes. | -
FCT-007 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N035.html | C | 2023-06-01 | AN_OTHER_STATES_INCLUDED | Le même panorama inclut Iran, Maroc, Turquie et Qatar dans une sous-partie dédiée aux autres pays cités. | -
FCT-008 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N035.html | C | 2023-06-01 | AN_US_EDGE_DISPUTE | Le président de la commission critique le projet de rapport parce qu’il situe les ingérences américaines à la lisière du champ; la rapporteure répond notamment que le lawfare est traité par une autre commission et invoque les limites de périmètre. | -
FCT-009 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N035.html | C | 2023-06-01 | AN_INTERNAL_DISAGREEMENT | Le président affirme que les ingérences de puissances alliées devraient également être signalées malgré une différence de nature; cette position est contestée dans le débat de périmètre et ne constitue pas un consensus institutionnel. | -
FCT-010 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N012.html | C | 2023-03-02 | DGSE_HOSTILE_FRIENDLY | Le directeur de la DGSE décrit Russie et Chine comme puissances systémiques agressives tout en précisant qu’il ne faut pas être naïf sur des actions hostiles conduites par des pays amis aux intérêts divergents. | -
FCT-011 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L16S2023PO812752N012.html | C | 2023-03-02 | DGSE_GULF_LOBBYING | Bernard Émié distingue influence, ingérence et outils et qualifie l’action des pays du Golfe pour orienter des décisions plutôt de lobbying; il rappelle qu’un ambassadeur fait lui-même du lobbying. | -
FCT-012 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/les-missions-de-viginum | D | 2026-05-15 | VIGINUM_FOUR_CRITERIA | VIGINUM définit une ingérence numérique étrangère par la combinaison de critères de contenu trompeur, comportement artificiel ou automatisé massif et délibéré, intention de nuire aux intérêts fondamentaux, et implication directe ou indirecte d’un acteur étranger. | -
FCT-013 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/comprendre-viginum/les-missions-de-viginum | D | 2026-05-15 | VIGINUM_NO_FACTCHECK | VIGINUM indique ne pas faire de fact-checking et privilégier l’analyse des modes opératoires informationnels, notamment clandestinité et coordination. | -
FCT-014 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/definitions-et-objectifs-du-concept-de-mode-operatoire-informationnel-moi | D | 2026-01-22 | MOI_PRE_ATTRIBUTION | Le concept VIGINUM de MOI permet de décrire et imputer des ensembles techniques cohérents sans connaître l’identité, l’origine, les intentions ou les ressources de l’acteur. | -
FCT-015 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/definitions-et-objectifs-du-concept-de-mode-operatoire-informationnel-moi | D | 2026-01-22 | MOI_BEHAVIOR_CENTERED | Le MOI est explicitement centré sur les indicateurs techniques et comportements en ligne plutôt que sur les narratifs. | -
FCT-016 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-un-reseau-structure-et-coordonne-de-propagande-prorusse | D | 2024-02-12 | PORTAL_KOMBAT_BEHAVIOR | VIGINUM documente Portal Kombat comme réseau d’au moins 193 sites relayant massivement des contenus pro-russes, avec automatisation et optimisation de référencement, ciblant notamment la France. | -
FCT-017 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/portal-kombat-un-reseau-structure-et-coordonne-de-propagande-prorusse | D | 2024-02-12 | PORTAL_KOMBAT_LABEL | VIGINUM qualifie ce réseau d’ingérence numérique étrangère à partir de ses caractéristiques techniques et de sa finalité apparente. | -
FCT-018 | FACT | ✧ | https://www.eeas.europa.eu/delegations/united-kingdom/tackling-foreign-information-manipulation-and-interference-together_en?s=3225 | E | 2023-09-28 | EEAS_FIMI_DEFINITION | Le SEAE décrit la FIMI comme un comportement principalement non illégal, manipulateur, intentionnel et coordonné, mené par des acteurs étatiques ou non étatiques y compris des proxies. | -
FCT-019 | FACT | ✧ | https://www.eeas.europa.eu/delegations/united-kingdom/tackling-foreign-information-manipulation-and-interference-together_en?s=3225 | E | 2023-09-28 | EEAS_RUSSIA_HISTORY | Le SEAE rappelle que la préoccupation européenne a été institutionnalisée dès 2015 autour des campagnes de désinformation russes, puis élargie dans le temps au cadre FIMI. | -
FCT-020 | FACT | ✧ | https://www.consilium.europa.eu/fr/press/press-releases/2022/03/02/eu-imposes-sanctions-on-state-owned-outlets-rtrussia-today-and-sputnik-s-broadcasting-in-the-eu/ | other:council | 2022-03-02 | RT_SANCTION_WAR_CONTEXT | La suspension de RT et Sputnik est décidée dans le contexte explicite de l’agression militaire russe contre l’Ukraine et doit durer jusqu’à la fin de l’agression et des actions de désinformation/manipulation. | -
FCT-021 | FACT | ✧ | https://www.consilium.europa.eu/fr/press/press-releases/2022/03/02/eu-imposes-sanctions-on-state-owned-outlets-rtrussia-today-and-sputnik-s-broadcasting-in-the-eu/ | other:council | 2022-03-02 | RT_STATE_CONTROL | Le Conseil décrit RT et Sputnik comme sous contrôle permanent direct ou indirect des autorités russes et comme instruments essentiels de soutien à l’agression et à la déstabilisation. | -
FCT-022 | FACT | ✧ | https://www.justice.gov/nsd-fara/fara-index-and-act | other:doj | 2026-09-10 | FARA_DEFENSE_EXEMPTION | Le FARA contient une exemption pour certaines activités exercées pour un gouvernement étranger dont la défense est jugée vitale pour celle des États-Unis, sous conditions de compatibilité avec les politiques/intérêts publics et de transparence des communications. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-003
FCT-008 | SRC-003
FCT-009 | SRC-003
FCT-010 | SRC-004
FCT-011 | SRC-004
FCT-012 | SRC-005
FCT-013 | SRC-005
FCT-014 | SRC-006
FCT-015 | SRC-006
FCT-016 | SRC-007
FCT-017 | SRC-007
FCT-018 | SRC-008
FCT-019 | SRC-008
FCT-020 | SRC-009
FCT-021 | SRC-009
FCT-022 | SRC-010

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | ELIGIBLE:VERIFIE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | ELIGIBLE:VERIFIE
FCT-009 | ELIGIBLE:VERIFIE
FCT-010 | ELIGIBLE:VERIFIE
FCT-011 | ELIGIBLE:VERIFIE
FCT-012 | ELIGIBLE:VERIFIE
FCT-013 | ELIGIBLE:VERIFIE
FCT-014 | ELIGIBLE:VERIFIE
FCT-015 | ELIGIBLE:VERIFIE
FCT-016 | ELIGIBLE:VERIFIE
FCT-017 | ELIGIBLE:VERIFIE
FCT-018 | ELIGIBLE:VERIFIE
FCT-019 | ELIGIBLE:VERIFIE
FCT-020 | ELIGIBLE:VERIFIE
FCT-021 | ELIGIBLE:VERIFIE
FCT-022 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-002 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-008 | WRITE | -
FCT-009 | WRITE | -
FCT-010 | WRITE | -
FCT-011 | WRITE | -
FCT-012 | WRITE | -
FCT-013 | WRITE | -
FCT-014 | WRITE | -
FCT-015 | WRITE | -
FCT-016 | WRITE | -
FCT-017 | WRITE | -
FCT-018 | WRITE | -
FCT-019 | WRITE | -
FCT-020 | WRITE | -
FCT-021 | WRITE | -
FCT-022 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-10T19:38:50.757466+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":22,"eligible":22,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:22;attempted:0;success:0;failure:0;blocked:22} | WRITEBACK_EXECUTION_V1:[22 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-002 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-003 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-004 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-005 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-006 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-007 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-008 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-009 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-010 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-011 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-012 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-013 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-014 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-016 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-017 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-018 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-019 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-020 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-021 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-022 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
