ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-1258-russie-financement-partis-europe | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv023_r3p1/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-06_russie-financement-partis-europe/2026-09-06_12-58_russie-financement-partis-europe_INPUT.txt | SUBJECT_SLUG:russie-financement-partis-europe | SUBJECT_FP:sha256:34185f129d884989760ce6c2722cf3daa96378aa617a4ecf321034dd5cfe43cd | INPUT_SHA256:sha256:7a5e16f441442076c1b9d3a2d002c9089e784dea7c71969158a5353d195d829b
COMPLEXITY:15→APEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Russian state/state-linked actors', 'European parties/movements', 'politicians/intermediaries', 'financial entities', 'platform/media intermediaries'], 'domains': ['party finance', 'loans/donations', 'formal cooperation agreements', 'paid influence', 'structured contacts', 'access/travel', 'coordination/tasking', 'legal/judicial outcomes'], 'exclusions': ['ideological sympathy alone', 'vote convergence alone', 'ordinary diplomacy without material relation', 'unsupported guilt-by-association'], 'geo': ['Union européenne', 'Royaume-Uni lorsque matériel'], 'lead_question': 'Quels éléments du corpus antérieur concernant des liens russes avec des partis/mouvements européens méritent revalidation ?', 'limits': ['public inspectable evidence as of 2026-09-06', 'case-based not exhaustive'], 'object_question': 'Quels financements, accords, contacts structurés, rémunérations ou formes de coopération entre acteurs russes et partis/mouvements politiques européens sont matériellement établis entre 2014 et 2026, quels niveaux de relation/coordination peuvent être prouvés, et quelles allégations restent non établies ?', 'period': '2014-01-01/2026-09-06'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,forensic/REASONING.md,clusters/MONEY.md,clusters/NETWORK.md,clusters/POWER.md,clusters/ICEBERG.md,clusters/TEMPORAL.md,clusters/FRAMING.md,clusters/RESISTANCE.md,clusters/WAR.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-023 — Financement, contacts et relations entre acteurs russes et partis/mouvements européens

## Objet borné

L'enquête distingue six classes de situations au lieu d'agréger tout « lien russe » sous une qualification unique : financement effectivement reçu, coopération politique formelle, financement tenté mais non réalisé, véhicule financier d'influence documenté, responsabilité individuelle alléguée sous procédure, et contrôle négatif où des contacts existent sans financement russe établi. Cette séparation est nécessaire pour éviter les promotions abusives `relation → coordination → commandement → effet`.

## Résultats par cas

Le cas FN/RN établit un prêt supérieur à 9,1 M€ auprès de First Czech Russian Bank (`FCT-001`). Le corpus ne permet pas d'établir une contrepartie politique associée à ce prêt (`FCT-002`). `CLM-001` est donc limité à un financement reçu par une entité bancaire russe. `CAU-001` lui attribue au plus un droit causal d'**ENABLER** financier, pas un quid pro quo, un tasking ou un effet politique démontré.

Le FPÖ a signé avec Russie unie un accord formel de coopération incluant échanges de délégations et coopération politique/économique (`FCT-004`, `FCT-005`). Le corpus retenu n'établit ni transfert financier associé ni mise en œuvre matérielle substantielle ; l'accord n'a pas été renouvelé (`FCT-006`). `CLM-002` reste donc `PARTIAL`.

La Lega a eu un accord de coopération avec Russie unie (`FCT-007`), mais affirme qu'aucune initiative concrète n'en a résulté (`FCT-008`). L'épisode du Metropol est distinct : les actes examinés visaient un financement illégal de la Lega (`FCT-009`), mais la vente de pétrole et le transfert projeté n'ont pas eu lieu (`FCT-010`). `CLM-004` interdit donc de compter ce montage comme financement effectivement reçu.

Voice of Europe constitue le mécanisme le plus directement documenté du corpus : les actes de l'Union européenne décrivent un véhicule secrètement financé et dirigé par Viktor Medvedchuk via Artem Marchevskyi, utilisé pour acheminer des ressources à des propagandistes et construire un réseau d'influence auprès de représentants de partis européens (`FCT-011`, `FCT-012`). `CAU-004` retient ici un droit causal **CAUSE** au niveau du véhicule et du réseau documentés, sans généraliser cette qualification à toute personne exposée ou interviewée.

Pour Petr Bystron, les sources inspectées établissent une procédure et des accusations de paiements en espèces/crypto associés à un engagement politique allégué (`FCT-013`, `FCT-014`). Elles n'établissent pas une culpabilité judiciaire définitive. `CLM-006`, `CAU-005` et `ACT-006` restent donc bornés par un gap de responsabilité.

Pour Tatjana Ždanoka, le VDD a ouvert une procédure pénale sur une possible coopération avec les services russes et mené des perquisitions (`FCT-015`, `FCT-016`) ; des éléments journalistiques supplémentaires portent sur des échanges et demandes de financement allégués (`FCT-017`). Le corpus ne contient pas de jugement définitif établissant un tasking par le FSB. `CLM-007`, `CAU-006` et `ACT-007` restent donc `PARTIAL/UNRESOLVED/GAP` avec `RESPONSIBILITY` explicite.

Enfin, Leave.EU/Arron Banks joue le rôle de contrôle négatif. Les contacts avec des responsables russes et discussions d'affaires sont documentés (`FCT-018`), mais la NCA a indiqué n'avoir trouvé aucune preuve qu'un tiers ait financé les prêts examinés ni que Banks ait agi comme agent d'un tiers (`FCT-019`, `FCT-020`). `CAU-007` est donc `REFUTED` pour la chaîne « contacts russes → financement russe des prêts ».

## Typologie analytique

Les objets observés ne forment pas une seule relation homogène. Les accords FPÖ/Russie unie et Lega/Russie unie établissent des canaux politiques formels (`CAU-002`), sans suffire à prouver financement ou commandement. Le prêt FN/RN établit une relation créancier/emprunteur (`ACT-001`) mais non une contrepartie. Le Metropol documente une tentative (`ACT-004`) et non un flux reçu. Voice of Europe documente un mécanisme financier et de réseau (`ACT-005`) plus proche d'une opération d'influence organisée. Les cas Bystron et Ždanoka restent individuellement sous plafond probatoire judiciaire.

Le résultat central n'est donc pas « les partis européens sont financés ou contrôlés par la Russie », mais : **plusieurs mécanismes matériels différents existent et certains franchissent des seuils probatoires élevés ; leur relation, leur contrepartie, leur tasking et leur effet doivent être démontrés séparément**.

## Causalité, contrôles et effets

Les contrôles institutionnels observés incluent l'interdiction française des prêts de banques hors EEE postérieure au prêt FN/RN (`CTRL-001`), les sanctions européennes contre Voice of Europe/Medvedchuk/Marchevskyi (`CTRL-002`), la levée d'immunité dans le dossier Bystron (`CTRL-003`), la procédure du VDD dans le dossier Ždanoka (`CTRL-004`) et l'enquête NCA sur les prêts Leave.EU (`CTRL-005`).

Le corpus soutient des effets de **ressource**, **accès**, **coopération formelle**, **tentative de financement**, **véhicule d'influence** et **réponse institutionnelle**. Il ne permet pas d'attribuer causalement un changement électoral ou politique agrégé à ces relations ou financements. L'axe `AXS-008` reste donc un gap causal explicite plutôt qu'une conclusion extrapolée.

## Contradictions et résultats négatifs

Plusieurs contre-résultats sont matériellement nécessaires à l'enquête : absence de contrepartie démontrée pour le prêt FN/RN (`FCT-002`), absence de mise en œuvre substantielle établie pour certains accords (`FCT-006`, `FCT-008`), non-réalisation du montage Metropol (`FCT-010`), absence de jugement définitif pour Bystron et Ždanoka (`CAU-005`, `CAU-006`), et absence de preuve de financement par un tiers dans le dossier Leave.EU examiné par la NCA (`FCT-019`).

Ces négatifs empêchent de transformer proximité, contact, accord ou tentative en preuve automatique de financement reçu, coordination, commandement ou impact.

## État de connaissance et continuation

Les gaps principaux concernent la contrepartie éventuelle du prêt FN/RN, la mise en œuvre concrète des accords interpartis, l'issue judiciaire des dossiers Bystron et Ždanoka, et toute mesure causale reliant ces mécanismes à des changements politiques ou électoraux. Les prochaines recherches utiles sont celles qui pourraient fermer ces gaps par décision judiciaire, pièces financières, preuves de tasking ou mesures d'effet, non par simple accumulation de nouveaux cas de proximité.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:9|EDI_DECISIVE:6|SRC_COMPLETE:12/12

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **item 1:**
  - **date:** 2014
  - **event:** FN/RN Russian bank loan
  - **refs:**
    - FCT-001
- **item 2:**
  - **date:** 2016-12-19
  - **event:** FPÖ–United Russia cooperation agreement
  - **refs:**
    - FCT-004
    - FCT-005
- **item 3:**
  - **date:** 2017
  - **event:** Lega–United Russia agreement; France adopts non-EEA bank-loan restriction
  - **refs:**
    - FCT-003
    - FCT-007
- **item 4:**
  - **date:** 2018-10
  - **event:** Metropol negotiation later investigated
  - **refs:**
    - FCT-009
    - FCT-010
- **item 5:**
  - **date:** 2021-12
  - **event:** FPÖ says agreement will not be renewed
  - **refs:**
    - FCT-006
- **item 6:**
  - **date:** 2022
  - **event:** Lega agreement auto-renewed according to Reuters; war later drives disavowal argument
  - **refs:**
    - FCT-007
    - FCT-008
- **item 7:**
  - **date:** 2024
  - **event:** Voice of Europe sanctions; Ždanoka criminal case; Lega disavows agreement
  - **refs:**
    - FCT-008
    - FCT-011
    - FCT-012
    - FCT-015
    - FCT-016
- **item 8:**
  - **date:** 2025-05-06
  - **event:** European Parliament waives Bystron immunity in corruption/Voice of Europe procedure
  - **refs:**
    - FCT-013
    - FCT-014
- **item 9:**
  - **date:** 2026-09-06
  - **event:** As-of boundary; no final adjudication located in bounded corpus for Bystron quid pro quo or Ždanoka intelligence cooperation
  - **refs:**
    - CLM-006
    - CLM-007

### MANIPULATION_REPORT
- **assumptions:**
  - public inspectable evidence only
  - case sample is discriminant not exhaustive
  - no aggregate prevalence inference from case count
- **clusters:**
  - forensic/REASONING.md
  - clusters/MONEY.md
  - clusters/NETWORK.md
  - clusters/POWER.md
  - clusters/ICEBERG.md
  - clusters/TEMPORAL.md
  - clusters/FRAMING.md
  - clusters/RESISTANCE.md
  - clusters/WAR.md
- **complexity:**
  - **class:** APEX
  - **score:** 15
- **implicit:**
  - Russian origin can route scrutiny but cannot determine relation class
  - party self-statements are evidence of what party claims, not independent proof
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - MONEY: payer→vehicle→beneficiary with received/attempted/alleged/refuted split
  - NET: typed relation graph only
  - TEMP: dated agreement/law/procedure sequence
  - WAR: organized influence only where infrastructure/funding/tasking evidence exists
- **priorities:**
  - financial flow identity
  - formal relation terms
  - procedural status
  - counterevidence
  - causal ceiling
- **query_guidance:**
  - seek direct loan/agreement/legal/procedural objects
  - search completion/non-completion and counterparty
  - seek current adjudication before upgrading allegations
- **rhetorical:**
  - CONTACTS≠FUNDING
  - FUNDING≠QUID_PRO_QUO
  - AGREEMENT≠TASKING
  - ALLEGATION≠CONVICTION
  - ATTEMPT≠RECEIPT
- **speaker:** multi-source case investigation; no single speaker treated as authority for the whole object
- **symbol_stage:** FINAL_CORPUS_REVIEW
- **symbols:**
  - **Κ:**
    - **observations:**
      - public/private gap not sufficiently evidenced as a general mechanism
    - **score:** 2
  - **Λ:**
    - **observations:**
      - label “ingérence” risks collapsing contact, finance, agreement, tasking and effect
      - negative control requires neutral category boundaries
    - **score:** 5
  - **Ξ:**
    - **observations:**
      - counterparties/implementation/adjudication are materially incomplete
      - cross-case hidden total cannot be reconstructed comparably
    - **score:** 6
  - **Σ:**
    - **observations:**
      - branding/party labels are secondary to documentary relation objects
    - **score:** 1
  - **Φ:**
    - **observations:**
      - spectacle/personality is not used as evidence
    - **score:** 1
  - **Ψ:**
    - **observations:**
      - no material urgency/volume impairment mechanism central to this case corpus
    - **score:** 1
  - **Ω:**
    - **observations:**
      - later disavowal/non-renewal of agreements changes current interpretation but does not erase historical relation
    - **score:** 3
  - **κ:**
    - **observations:**
      - choice architecture not material to object question
    - **score:** 1
  - **ρ:**
    - **observations:**
      - CNCCFP/Senate scrutiny
      - EU sanctions
      - VDD/NCA investigations
      - parliamentary immunity controls
    - **score:** 5
  - **€:**
    - **observations:**
      - RN loan
      - Metropol attempted financing
      - Voice of Europe funding vehicle
      - Bystron alleged cash/crypto
    - **score:** 9
  - **↕:**
    - **observations:**
      - foreign resource/access asymmetries and accountability mechanisms are material
      - legal controls differ by jurisdiction and period
    - **score:** 6
  - **⏰:**
    - **observations:**
      - 2014 loan predates 2017 French ban
      - agreements evolve across 2016/2017→2021/2024
      - post-2022 war materially changes party positions and controls
    - **score:** 7
  - **⚔:**
    - **observations:**
      - Voice of Europe is officially described as a coordinated influence/funding vehicle
      - other cases are not automatically information operations
    - **score:** 5
  - **⫸:**
    - **observations:**
      - multiple independent cases exist but mechanisms are heterogeneous and do not justify a unified-command inference
    - **score:** 4
  - **🌐:**
    - **observations:**
      - party-party agreements
      - financial intermediaries
      - Medvedchuk–Marchevskyi–Voice of Europe network
      - politician/intermediary relations
    - **score:** 8
- **threats:**
  - @THR[DARK_MONEY]: Metropol and Voice of Europe; counter-check actual transfer/legal object
  - @THR[POWER_PROX]: proximity/contact never responsibility by itself
  - @THR[COG_INFILTRATION]: Voice of Europe only where coordinated network evidence exists

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - RN counterparty
    - Bystron adjudication
    - Ždanoka adjudication
  - **input_ids:**
    - LED-001
    - LED-004
    - LED-006
    - LED-007
    - LED-008
  - **module:** forensic/REASONING.md
  - **negative_results:**
    - No common hidden-financing total can be inferred from heterogeneous cases
  - **not_computable:**
    - cross-case hidden financing factor
  - **operations_applied:**
    - visible/omitted split
    - reconstruction comparability test
    - innocent alternative test
  - **reason:** material hidden counterparty/implementation/adjudication dimensions
  - **result_ids:**
    - FCT-002
    - FCT-010
    - FCT-019
    - CAU-005
    - CAU-006
    - CAU-007
  - **status:** PASS
  - **trigger:** Ξ=6
- **item 2:**
  - **gaps:**
    - Bystron individual receipt not adjudicated
  - **input_ids:**
    - LED-001
    - LED-004
    - LED-005
    - LED-006
    - LED-008
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - No completed Metropol transfer
    - No third-party funding evidence in Leave.EU referred matter
  - **not_computable:**
    - aggregate Russian financing across European parties
  - **operations_applied:**
    - payer→vehicle→recipient trace
    - received vs attempted vs alleged vs refuted split
  - **reason:** financial flows central
  - **result_ids:**
    - FCT-001
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
    - FCT-019
    - CAU-001
    - CAU-003
    - CAU-004
    - CAU-005
    - CAU-007
  - **status:** PASS
  - **trigger:** €=9
- **item 3:**
  - **gaps:**
    - individual tasking for Bystron/Ždanoka unresolved
  - **input_ids:**
    - LED-002
    - LED-003
    - LED-005
    - LED-006
    - LED-007
    - LED-008
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - No single command graph supported across all cases
  - **not_computable:**
    - centrality metrics on non-population case sample
  - **operations_applied:**
    - typed edges
    - remove speculative command edges
    - link actions to evidence
  - **reason:** typed actor/intermediary relations central
  - **result_ids:**
    - ACT-002
    - ACT-003
    - ACT-005
    - ACT-006
    - ACT-007
    - ACT-008
    - CAU-002
    - CAU-004
  - **status:** PASS
  - **trigger:** 🌐=8 and €>=7
- **item 4:**
  - **gaps:**
    - comparability of legal regimes
  - **input_ids:**
    - LED-001
    - LED-005
    - LED-006
    - LED-007
  - **module:** clusters/POWER.md
  - **negative_results:**
    - No evidence that resource asymmetry alone generated command/control
  - **not_computable:**
    - cross-jurisdiction sanction-equivalence metric
  - **operations_applied:**
    - resource dependency review
    - accountability/oversight comparison
  - **reason:** dependency/access/accountability asymmetry material
  - **result_ids:**
    - CTRL-001
    - CTRL-002
    - CTRL-003
    - CTRL-004
    - CTRL-005
    - CAU-001
  - **status:** PASS
  - **trigger:** ↕=6 and €>=7
- **item 5:**
  - **gaps:**
    - counterparties
    - implementation
    - adjudication
  - **input_ids:**
    - CLM-001
    - CLM-002
    - CLM-006
    - CLM-007
  - **module:** clusters/ICEBERG.md
  - **negative_results:**
    - Unknown does not become zero or proof
  - **not_computable:**
    - hidden consideration total
  - **operations_applied:**
    - omission map
    - comparability test
    - alternative explanation
  - **reason:** material unknowns can inflate claims
  - **result_ids:**
    - FCT-002
    - FCT-006
    - FCT-008
    - FCT-010
    - FCT-019
  - **status:** PASS
  - **trigger:** Ξ=6
- **item 6:**
  - **gaps:**
    - some current procedural endpoints not public
  - **input_ids:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-006
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-014
    - FCT-015
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - Temporal co-occurrence is not used as coordination evidence
  - **not_computable:**
    - P_random for heterogeneous political events
  - **operations_applied:**
    - timeline normalization
    - before/after legal boundary
    - agreement expiry/disavowal chronology
  - **reason:** sequence changes legal/relational interpretation
  - **result_ids:**
    - CAU-001
    - CAU-002
    - CAU-003
    - CTRL-001
  - **status:** PASS
  - **trigger:** ⏰=7
- **item 7:**
  - **gaps:**
    - NONE
  - **input_ids:**
    - CLM-001
    - CLM-004
    - CLM-006
    - CLM-008
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - No global “all ties are interference” classification survives
  - **not_computable:**
    - audience effect of political labels
  - **operations_applied:**
    - neutral reclassification
    - alternative frame
    - context restoration
  - **reason:** “Russian ties/ingérence” can collapse distinct evidence classes
  - **result_ids:**
    - FCT-002
    - FCT-010
    - FCT-019
    - CAU-007
  - **status:** PASS
  - **trigger:** Λ=5
- **item 8:**
  - **gaps:**
    - deterrence/effectiveness not measured across cases
  - **input_ids:**
    - CTRL-001
    - CTRL-002
    - CTRL-003
    - CTRL-004
    - CTRL-005
  - **module:** clusters/RESISTANCE.md
  - **negative_results:**
    - Oversight action does not establish underlying allegation beyond its procedural scope
  - **not_computable:**
    - aggregate deterrent effect
  - **operations_applied:**
    - map independent checks
    - map legal/institutional responses
    - test whether controls establish truth by themselves
  - **reason:** multiple evidence-based counter-power mechanisms materially shape outcomes
  - **result_ids:**
    - CTRL-001
    - CTRL-002
    - CTRL-003
    - CTRL-004
    - CTRL-005
  - **status:** PASS
  - **trigger:** ρ=5
- **item 9:**
  - **gaps:**
    - Bystron individual quid pro quo unresolved
  - **input_ids:**
    - LED-005
    - LED-006
  - **module:** clusters/WAR.md
  - **negative_results:**
    - Other party agreements/loans are not automatically cognitive-warfare operations
  - **not_computable:**
    - common-command attribution across entire six-case corpus
  - **operations_applied:**
    - funding/infrastructure/targeting separation
    - attribution boundary
    - organic/proximity alternative test
  - **reason:** Voice of Europe meets organized influence-operation evidence threshold
  - **result_ids:**
    - FCT-011
    - FCT-012
    - FCT-013
    - CAU-004
    - CAU-005
  - **status:** PASS
  - **trigger:** ⚔=5

### SCOPING_REPORT
- **case_design:** case-based, non exhaustive
- **cases:**
  - RN/FN loan
  - FPÖ–United Russia agreement
  - Lega–United Russia + Metropol
  - Voice of Europe / Petr Bystron
  - Tatjana Ždanoka
  - Leave.EU / Arron Banks negative control
- **exclusions:**
  - ideological sympathy
  - vote convergence
  - ordinary diplomacy
  - guilt by association
  - unbounded census of all European parties
- **geo:**
  - France
  - Autriche
  - Italie
  - Allemagne/UE
  - Lettonie
  - Royaume-Uni
- **inclusion_rule:** material financing/agreement/paid-influence/structured-contact/intelligence-relation evidence with inspectable source
- **object_question:** Quels financements, accords, contacts structurés, rémunérations ou coopérations entre acteurs russes et partis/mouvements européens sont matériellement établis entre 2014 et 2026, à quel niveau de relation/coordination, et quelles allégations restent non établies ?
- **period:** 2014-01-01/2026-09-06
- **terminal_rule:** distinguish received financing, attempted financing, formal cooperation, alleged quid pro quo, alleged intelligence cooperation, and refuted foreign-funding inference.

### CREDO
- **item 1:**
  - **answer:** Loan/agreement/proceeding/sanctions/contact objects are separated and source-anchored.
  - **question:** Que sait-on directement ?
- **item 2:**
  - **answer:** RN counterparty, full implementation of party agreements, adjudicated Bystron quid pro quo, adjudicated Ždanoka tasking, aggregate political/electoral effect.
  - **question:** Que ne sait-on pas ?
- **item 3:**
  - **answer:** Contacts or ideological affinity alone can be mistaken for foreign funding or command; Leave.EU/NCA is the explicit negative control.
  - **question:** Quelle accusation forte peut être fausse ?
- **item 4:**
  - **answer:** Voice of Europe provides the strongest official evidence of a financing vehicle deliberately used to remunerate propagandists and build a political influence network.
  - **question:** Quel mécanisme matériel est le plus fort ?
- **item 5:**
  - **answer:** Metropol: documented aim to illegally fund Lega, but transaction did not occur.
  - **question:** Quel cas montre tentative sans résultat ?
- **item 6:**
  - **answer:** RN 2014 loan: financing is established, counterparty is not.
  - **question:** Quel cas montre financement sans quid pro quo démontré ?
- **item 7:**
  - **answer:** I0-I3 relationship/resource/action evidence must not be promoted to I5-I7 persuasion, behavioral change or counterfactual electoral outcome.
  - **question:** Quel seuil ne doit pas être franchi sans preuve ?

### COGNITIVE_MAP
- **bias_guards:**
  - relation≠coordination
  - funding≠quid pro quo
  - attempt≠receipt
  - allegation≠conviction
  - contact≠foreign funding
- **case_classes:**
  - **attempted_financing:**
    - Metropol
  - **formal_cooperation:**
    - FPÖ–UR
    - Lega–UR
  - **individual_quid_pro_quo_allegation:**
    - Bystron
  - **intelligence_cooperation_allegation:**
    - Ždanoka
  - **negative_control:**
    - Leave.EU/Banks contacts without third-party funding evidence
  - **officially_designated_financial_influence_network:**
    - Voice of Europe
  - **received_financing:**
    - RN loan
- **causal_ceiling:** No corpus-level causal estimate of persuasion, vote change or electoral counterfactual.
- **core:** foreign/state-linked resource or institutional relation → access/capability → documented action/attempt → possible coordination/tasking → possible effect
- **strongest_discriminators:**
  - actual transfer
  - contract text
  - procedural status
  - direct command/tasking evidence
  - counterevidence

### DIALECTICAL_MAP
- **IMPACT:** Supports a differentiated typology, not a single global “Russian control of European parties” conclusion.
- **P1_DOMINANT:** Russian actors have cultivated material relationships with some European political actors using loans, formal party agreements, intermediaries and at least one officially designated funding/influence network.
- **P2_CRITICAL:** These heterogeneous cases do not justify treating every pro-Russian party, contact, loan or agreement as Kremlin tasking, corruption or effective electoral interference.
- **P3_EVIDENCE_ARBITRATION:**
  - RN: finance yes / quid pro quo unknown
  - FPÖ/Lega: formal cooperation yes / command or material implementation not shown
  - Metropol: attempted illicit funding yes / transfer no
  - Voice of Europe: network mechanism established / individual Bystron guilt unresolved
  - Ždanoka: serious investigation + leaked-email evidence / judicial responsibility unresolved
  - Leave.EU: contacts yes / specific Russian-funding inference rejected by NCA
- **SILENCES:**
  - comprehensive population denominator
  - comparative baseline across all European parties
  - measured downstream electoral effect
- **TENSIONS:**
  - official sanctions findings vs individual criminal proof
  - party agreements vs claimed non-implementation
  - contact density vs funding causation

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** loan >€9.1m
  - **from:** First Czech Russian Bank → Aviazapchast creditor chain
  - **refs:**
    - FCT-001
    - FCT-002
  - **status:** RECEIVED
  - **to:** FN/RN
- **item 2:**
  - **flow:** alleged/negotiated ~€65m target described by ANSA summary
  - **from:** Russian/Italian intermediaries via proposed oil-sale margin
  - **refs:**
    - FCT-009
    - FCT-010
  - **status:** ATTEMPTED_NOT_COMPLETED
  - **to:** Lega
- **item 3:**
  - **flow:** financial resources, amount not established here
  - **from:** Medvedchuk via Marchevskyi / Voice of Europe
  - **refs:**
    - FCT-011
    - FCT-012
  - **status:** ESTABLISHED_NETWORK_MECHANISM
  - **to:** propagandists + political influence network
- **item 4:**
  - **flow:** cash/crypto
  - **from:** Voice of Europe operator
  - **refs:**
    - FCT-013
    - FCT-014
  - **status:** ALLEGED_NOT_ADJUDICATED
  - **to:** Petr Bystron
- **item 5:**
  - **flow:** funding requests
  - **from:** Russian sources alleged in leaked emails
  - **refs:**
    - FCT-017
    - FCT-015
  - **status:** ALLEGED/INVESTIGATED
  - **to:** Ždanoka political activities
- **item 6:**
  - **flow:** £8m examined
  - **from:** alleged Russian/third-party source
  - **refs:**
    - FCT-019
    - FCT-020
  - **status:** SPECIFIC_THIRD_PARTY_FUNDING_INFERENCE_NOT_SUPPORTED_BY_NCA
  - **to:** Leave.EU/BFTC loans

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** First Czech Russian Bank
  - **refs:**
    - FCT-001
  - **relation:** creditor/borrower
  - **strength:** documented
  - **to:** FN/RN
- **item 2:**
  - **from:** FPÖ
  - **refs:**
    - FCT-004
    - FCT-005
    - FCT-006
  - **relation:** formal party cooperation agreement
  - **strength:** documented
  - **to:** United Russia
- **item 3:**
  - **from:** Lega
  - **refs:**
    - FCT-007
    - FCT-008
  - **relation:** formal party cooperation agreement
  - **strength:** documented
  - **to:** United Russia
- **item 4:**
  - **from:** Savoini/intermediaries
  - **refs:**
    - FCT-009
    - FCT-010
  - **relation:** attempted illicit-financing mechanism
  - **strength:** judicially described aim, unfulfilled
  - **to:** Lega
- **item 5:**
  - **from:** Medvedchuk
  - **refs:**
    - FCT-011
    - FCT-012
  - **relation:** secret financing/direction according to EU listing
  - **strength:** official listing
  - **to:** Marchevskyi/Voice of Europe
- **item 6:**
  - **from:** Voice of Europe operator
  - **refs:**
    - FCT-013
    - FCT-014
  - **relation:** alleged cash/crypto quid pro quo
  - **strength:** criminal allegation, not conviction
  - **to:** Petr Bystron
- **item 7:**
  - **from:** persons identified as FSB / Russian services
  - **refs:**
    - FCT-015
    - FCT-017
  - **relation:** alleged cooperation/reporting/funding requests
  - **strength:** criminal suspicion + investigative reporting
  - **to:** Tatjana Ždanoka
- **item 8:**
  - **from:** Russian Embassy/officials
  - **refs:**
    - FCT-018
  - **relation:** meetings/business discussions
  - **strength:** documented by parliamentary inquiry
  - **to:** Arron Banks/Andy Wigmore

### IMPACT_MAP
- **I0_IDENTITY_RELATION:**
  - **refs:**
    - FCT-001
    - FCT-004
    - FCT-007
    - FCT-011
    - FCT-018
  - **status:** VERIFIED_IN_MULTIPLE_CASES
- **I1_RESOURCES_CAPABILITY_ACCESS:**
  - **refs:**
    - FCT-001
    - FCT-005
    - FCT-009
    - FCT-011
  - **status:** VERIFIED_OR_PARTIAL
- **I2_DOCUMENTED_ACTION:**
  - **refs:**
    - ACT-001
    - ACT-002
    - ACT-003
    - ACT-004
    - ACT-005
    - ACT-008
  - **status:** VERIFIED_CASE_DEPENDENT
- **I3_COORDINATION_TASKING_CONTROL:**
  - **limit:** Voice of Europe network strongest; individual tasking allegations unresolved.
  - **refs:**
    - CAU-004
    - CAU-005
    - CAU-006
  - **status:** PARTIAL
- **I4_EXPOSURE_REACH:**
  - **gap:** This case study investigates financial/relational channels, not audience exposure.
  - **gap_type:** SCOPE
  - **status:** NOT_CENTRAL_NOT_QUANTIFIED
- **I5_RECEPTION_PERSUASION:**
  - **gap:** No persuasion measurement tied to these relations/flows.
  - **gap_type:** CAUSALITY
  - **status:** NOT_ESTABLISHED
- **I6_BEHAVIOR_INSTITUTIONAL_ELECTORAL_CHANGE:**
  - **limit:** Institutional responses are documented; behavioral quid pro quo remains alleged.
  - **refs:**
    - FCT-013
    - CTRL-001
    - CTRL-002
    - CTRL-003
    - CTRL-004
    - CTRL-005
  - **status:** PARTIAL
- **I7_COUNTERFACTUAL_OUTCOME:**
  - **gap:** No counterfactual electoral outcome attributable to the examined financing/relations.
  - **gap_type:** CAUSALITY
  - **status:** NOT_ESTABLISHED

### CONTRADICTION_LEDGER
- **item 1:**
  - **claim:** RN Russian loan proves interference/quid pro quo
  - **counter:**
    - FCT-002
  - **resolution:** FINANCING ESTABLISHED; COUNTERPARTY/INGÉRENCE NOT ESTABLISHED
  - **support:**
    - FCT-001
- **item 2:**
  - **claim:** Formal FPÖ/Lega agreements imply executed coordination
  - **counter:**
    - FCT-006
    - FCT-008
  - **resolution:** FORMAL RELATION ESTABLISHED; MATERIAL IMPLEMENTATION/TASKING NOT ESTABLISHED
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-007
- **item 3:**
  - **claim:** Metropol means Lega received Russian financing
  - **counter:**
    - FCT-010
  - **resolution:** ATTEMPTED ILLEGAL-FINANCING AIM DOCUMENTED; COMPLETED TRANSFER REFUTED WITHIN CASE
  - **support:**
    - FCT-009
- **item 4:**
  - **claim:** Bystron was paid to act for Russia
  - **counter:** NONE_FOUND
  - **resolution:** SERIOUS CRIMINAL ALLEGATION; RESPONSIBILITY UNRESOLVED
  - **support:**
    - FCT-013
    - FCT-014
- **item 5:**
  - **claim:** Ždanoka was an FSB agent/tasked actor
  - **counter:** NONE_FOUND
  - **resolution:** INVESTIGATIVE/CRIMINAL SUSPICION STRONG; JUDICIAL RESPONSIBILITY UNRESOLVED
  - **support:**
    - FCT-015
    - FCT-017
- **item 6:**
  - **claim:** Banks Russian contacts prove Russian financing of Leave.EU
  - **counter:**
    - FCT-019
  - **resolution:** CONTACTS ESTABLISHED; SPECIFIC THIRD-PARTY FUNDING INFERENCE REJECTED BY NCA
  - **support:**
    - FCT-018

### VERIFICATION_REPORT
- **counts:**
  - **ACT:** 8
  - **AXS:** 9
  - **CAU:** 7
  - **CLM:** 8
  - **CTRL:** 5
  - **LED:** 8
  - **facts:** 20
  - **queries:** 24
  - **sources:** 12
- **fact_policy:** All material FCT are tier ✧; no ✦ claim used, avoiding false precision where independent corroboration or direct adjudication is incomplete.
- **negative_control:** Leave.EU/Banks prevents promotion of contact density to foreign financing.
- **procedural_boundaries:**
  - Bystron: immunity/prosecutor allegations ≠ conviction
  - Ždanoka: criminal investigation + leaked-email reporting ≠ judgment
  - Metropol: attempted aim ≠ completed transfer
  - Leave.EU: contacts ≠ third-party funding
- **remaining_material_gaps:**
  - Bystron adjudication
  - Ždanoka adjudication/current procedural endpoint
  - aggregate downstream political/electoral effects
- **source_contract:** 12/12 accepted sources carry canonical_id/title/publication_date/checked_at/locator/url/role/family

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW
  - **counters:** 5
  - **coverage:** 1.0
  - **direct_objects:** 7
  - **edi_star:** 0.899
  - **independence:** 0.833
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **credible_counter:** FOUND
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 2:**
    - **claim_id:** CLM-004
    - **credible_counter:** FOUND
    - **direct_object:** NO
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 3:**
    - **claim_id:** CLM-005
    - **credible_counter:** NONE_FOUND
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 1
  - **item 4:**
    - **claim_id:** CLM-006
    - **credible_counter:** NONE_FOUND
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 1
  - **item 5:**
    - **claim_id:** CLM-007
    - **credible_counter:** NONE_FOUND
    - **direct_object:** PARTIAL
    - **freshness:** UNKNOWN
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 2
  - **item 6:**
    - **claim_id:** CLM-008
    - **credible_counter:** FOUND
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:**
    - **note:** France/Austria/Italy/EU-Germany/Latvia/UK
    - **score:** 1.0
  - **lang:**
    - **note:** French/German/English source surfaces
    - **score:** 0.8
  - **owner:**
    - **note:** multiple independent institutional/media owners
    - **score:** 0.9
  - **persp:**
    - **note:** official findings plus party denials/non-implementation claims and negative control
    - **score:** 0.7
  - **strat:**
    - **note:** regulators, legal acts, parliamentary records, major media, investigative reporting
    - **score:** 0.85
  - **temp:**
    - **note:** 2014-2026 chronology including contemporary legal updates
    - **score:** 0.9
- **edi:**
  - **band:** BROAD
  - **final:** 0.865
  - **flags:**
    - NONE
  - **penalties:** 0.0
  - **raw:** 0.865
  - **target_note:** APEX target .80 met as process diagnostic; not truth
- **source_counts:**
  - **other:** 0
  - **primary:** 7
  - **secondary:** 5
  - **total:** 12

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** RN/FN
  - **established:** accepted Russian-bank loan
  - **not_established:** political quid pro quo or Russian command
  - **refs:**
    - FCT-001
    - FCT-002
- **item 2:**
  - **actor:** FPÖ / Lega
  - **established:** formal cooperation agreements with United Russia
  - **not_established:** tasking/control or material implementation from agreement alone
  - **refs:**
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-008
- **item 3:**
  - **actor:** Savoini/intermediaries
  - **established:** acts aimed at illegal Lega funding according to shelving decision summary
  - **not_established:** completed transfer or proven corruption offence
  - **refs:**
    - FCT-009
    - FCT-010
- **item 4:**
  - **actor:** Medvedchuk/Marchevskyi/Voice of Europe
  - **established:** secret financing/direction and financial influence-network function in EU listing
  - **not_established:** automatic culpability of all political representatives connected to platform
  - **refs:**
    - FCT-011
    - FCT-012
- **item 5:**
  - **actor:** Petr Bystron
  - **established:** criminal procedure and detailed allegations; immunity waived
  - **not_established:** guilt/quid pro quo as adjudicated fact
  - **refs:**
    - FCT-013
    - FCT-014
- **item 6:**
  - **actor:** Tatjana Ždanoka
  - **established:** VDD criminal suspicion/searches + leaked-email investigation reporting funding requests
  - **not_established:** judicially established FSB tasking/cooperation
  - **refs:**
    - FCT-015
    - FCT-016
    - FCT-017
- **item 7:**
  - **actor:** Arron Banks/Leave.EU
  - **established:** Russian contacts/business discussions
  - **not_established:** Russian/third-party funding of referred loans; NCA found no evidence
  - **refs:**
    - FCT-018
    - FCT-019
    - FCT-020

### NEXT_QUERIES
- **item 1:**
  - **priority:** 1
  - **query:** Petr Bystron Voice of Europe final indictment judgment conviction acquittal Munich prosecutor after 2025
  - **resolves:** CLM-006/CAU-005 responsibility
- **item 2:**
  - **priority:** 2
  - **query:** Tatjana Ždanoka VDD final criminal case decision indictment judgment after July 2024
  - **resolves:** CLM-007/CAU-006 responsibility
- **item 3:**
  - **priority:** 3
  - **query:** FPÖ United Russia agreement implementation funding projects documentary evidence 2016-2021
  - **resolves:** CLM-002 scope
- **item 4:**
  - **priority:** 4
  - **query:** comparative dataset foreign state-linked party finance Europe 2014-2026 outcomes
  - **resolves:** prevalence/denominator; only if later synthesis needs it

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-013,SRC-001 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-002,QRY-014,SRC-002,QRY-015,SRC-003 | support:- | counter:- | results:FCT-004,FCT-005,FCT-006 | final:SATURATED | gap:NONE
LED-003 | attempts:QRY-003,QRY-016,SRC-004 | support:- | counter:- | results:FCT-007,FCT-008 | final:SATURATED | gap:NONE
LED-004 | attempts:QRY-004,QRY-017,SRC-005 | support:- | counter:- | results:FCT-009,FCT-010 | final:SATURATED | gap:NONE
LED-005 | attempts:QRY-005,QRY-018,SRC-006,QRY-019,SRC-007 | support:- | counter:- | results:FCT-011,FCT-012 | final:SATURATED | gap:NONE
LED-006 | attempts:QRY-006,QRY-020,SRC-008,QRY-011 | support:- | counter:- | results:FCT-013,FCT-014 | final:SATURATED | gap:NONE
LED-007 | attempts:QRY-007,QRY-021,SRC-009,QRY-012 | support:- | counter:- | results:FCT-015,FCT-016,FCT-017 | final:SATURATED | gap:NONE
LED-008 | attempts:QRY-009,QRY-023,SRC-011,QRY-010,QRY-024,SRC-012 | support:- | counter:- | results:FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:- | counter:- | results:FCT-001,FCT-004,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-014,FCT-015,FCT-018,FCT-019 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-004,QRY-005,QRY-006,QRY-008,QRY-009,QRY-013,SRC-001,QRY-017,SRC-005,QRY-018,SRC-006,QRY-019,SRC-007,QRY-020,SRC-008,QRY-022,SRC-010,QRY-023,SRC-011 | support:- | counter:- | results:FCT-001,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-017,FCT-019,FCT-020,CAU-001,CAU-003,CAU-004,CAU-005,CAU-007 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:- | counter:- | results:CAU-001,CAU-002,CAU-003,CAU-004,CAU-005,CAU-006,CAU-007 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:- | counter:- | results:ACT-001,ACT-002,ACT-003,ACT-004,ACT-005,ACT-006,ACT-007,ACT-008,CAU-002,CAU-004,CAU-005,CAU-006,CAU-007 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:- | counter:- | results:CTRL-001,CTRL-002,CTRL-003,CTRL-004,CTRL-005 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:- | counter:- | results:CAU-001,CAU-002,CAU-003,CAU-004,CAU-005,CAU-006,CAU-007,ACT-001,ACT-002,ACT-003,ACT-004,ACT-005,ACT-006,ACT-007,ACT-008 | final:GAP | gap:CAUSALITY
AXS-009 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023,QRY-024,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-006,SRC-007,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:- | counter:- | results:FCT-002,FCT-006,FCT-008,FCT-010,FCT-019,CAU-005,CAU-006,CAU-007 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-013,SRC-001 | support:FCT-001 | counter:FCT-002 | results:FCT-001,FCT-002 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-014,QRY-015,SRC-002,SRC-003 | support:FCT-004,FCT-005,FCT-006 | counter:- | results:FCT-004,FCT-005,FCT-006 | final:PARTIAL | gap:SCOPE
CLM-003 | attempts:QRY-016,SRC-004 | support:FCT-007 | counter:FCT-008 | results:FCT-007,FCT-008 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-017,SRC-005 | support:FCT-009,FCT-010 | counter:FCT-010 | results:FCT-009,FCT-010,FCT-010 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-018,QRY-019,SRC-006,SRC-007 | support:FCT-011,FCT-012 | counter:- | results:FCT-011,FCT-012 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-020,SRC-008 | support:FCT-013,FCT-014 | counter:- | results:FCT-013,FCT-014 | final:PARTIAL | gap:RESPONSIBILITY
CLM-007 | attempts:QRY-021,QRY-022,SRC-009,SRC-010 | support:FCT-015,FCT-016,FCT-017 | counter:- | results:FCT-015,FCT-016,FCT-017 | final:PARTIAL | gap:RESPONSIBILITY
CLM-008 | attempts:QRY-023,QRY-024,SRC-011,SRC-012 | support:FCT-018,FCT-019,FCT-020 | counter:FCT-019 | results:FCT-018,FCT-019,FCT-020,FCT-019 | final:SUPPORTED | gap:NONE

## STATUS_DELTA_V1
DELTA-001 | LED-001 | ACTIVE | SATURATED | evidence review after FCT construction
DELTA-002 | LED-002 | ACTIVE | SATURATED | evidence review after FCT construction
DELTA-003 | LED-003 | ACTIVE | SATURATED | evidence review after FCT construction
DELTA-004 | LED-004 | ACTIVE | SATURATED | evidence review after FCT construction
DELTA-005 | LED-005 | ACTIVE | SATURATED | evidence review after FCT construction
DELTA-006 | LED-006 | ACTIVE | SATURATED | evidence review after FCT construction
DELTA-007 | LED-007 | ACTIVE | SATURATED | evidence review after FCT construction
DELTA-008 | LED-008 | ACTIVE | SATURATED | evidence review after FCT construction
DELTA-009 | CLM-001 | PARTIAL | SUPPORTED | evidence review after FCT construction
DELTA-010 | CLM-003 | PARTIAL | SUPPORTED | evidence review after FCT construction
DELTA-011 | CLM-004 | PARTIAL | SUPPORTED | evidence review after FCT construction
DELTA-012 | CLM-005 | PARTIAL | SUPPORTED | evidence review after FCT construction
DELTA-013 | CLM-008 | PARTIAL | SUPPORTED | evidence review after FCT construction
DELTA-014 | AXS-001 | PLANNED | SATURATED | axis closure after evidence causal and accountability review
DELTA-015 | AXS-002 | PLANNED | SATURATED | axis closure after evidence causal and accountability review
DELTA-016 | AXS-003 | PLANNED | SATURATED | axis closure after evidence causal and accountability review
DELTA-017 | AXS-004 | PLANNED | SATURATED | axis closure after evidence causal and accountability review
DELTA-018 | AXS-005 | PLANNED | SATURATED | axis closure after evidence causal and accountability review
DELTA-019 | AXS-006 | PLANNED | SATURATED | axis closure after evidence causal and accountability review
DELTA-020 | AXS-007 | PLANNED | SATURATED | axis closure after evidence causal and accountability review
DELTA-021 | AXS-008 | PLANNED | GAP | axis closure after evidence causal and accountability review
DELTA-022 | AXS-009 | PLANNED | SATURATED | axis closure after evidence causal and accountability review

## OPEN_GAPS_V1
AXS-008 | AXS | GAP | CAUSALITY | Le corpus établit plusieurs relations, flux, tentatives et mécanismes, mais ne permet pas d’attribuer causalement un changement électoral ou politique agrégé à ces relations/financements.
CLM-002 | CLM | PARTIAL | SCOPE | Aucun transfert financier ni mise en œuvre matérielle substantielle de l’accord FPÖ–Russie unie n’est établi par le corpus borné.
CLM-006 | CLM | PARTIAL | RESPONSIBILITY | Les sources inspectées établissent une procédure et des allégations détaillées, pas une condamnation judiciaire définitive pour le quid pro quo Voice of Europe.
CLM-007 | CLM | PARTIAL | RESPONSIBILITY | L’enquête pénale et les fuites journalistiques ne constituent pas une décision judiciaire établissant coopération/tasking par le FSB.
CAU-005 | CAU | UNRESOLVED | RESPONSIBILITY | Quid pro quo individuel non judiciairement établi dans les sources inspectées au 2026-09-06.
CAU-006 | CAU | UNRESOLVED | RESPONSIBILITY | Tasking/coopération avec le FSB non judiciairement établi dans les sources inspectées.

SEMANTIC_COUNTS_V1:LED:8|CLM:8|AXS:9|CAU:7|CTRL:5|ACT:8

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-013","SRC-001"],"evidence_excerpt":"Le prêt de plus de 9,1 M€ est documenté; la CNCCFP dit n’avoir aucun moyen de savoir s’il était assorti de contreparties.","kind":"RELATION","lead":"RN/FN a contracté en 2014 un prêt >9,1 M€ auprès de First Czech Russian Bank; CNCCFP ne peut établir l’existence de contreparties.","linked_ids":["AXS-003","AXS-004","AXS-006","AXS-009"],"locator":"lines 126-132","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003"],"routes":["EXPAND","LINK"],"source_id":"SRC-001","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-002","QRY-014","SRC-002","QRY-015","SRC-003"],"evidence_excerpt":"Accord formel de coopération FPÖ–Russie unie, cinq ans, échanges de délégations et coopération politique/économique.","kind":"RELATION","lead":"FPÖ et Russie unie ont signé un accord de coopération formel incluant échanges de délégations, activité législative et soutien économique.","linked_ids":["AXS-003","AXS-006"],"locator":"accord du 19 décembre 2016","materiality":"IMPORTANT","result_ids":["FCT-004","FCT-005","FCT-006"],"routes":["EXPAND","LINK"],"source_id":"SRC-002","status":"SATURATED"}
LED-003 | {"attempt_ids":["QRY-003","QRY-016","SRC-004"],"evidence_excerpt":"Reuters documente l’accord 2017, son renouvellement automatique en 2022, son désaveu en 2024 et l’absence d’initiatives concrètes revendiquée par Lega.","kind":"RELATION","lead":"Lega et Russie unie ont eu un accord de coopération 2017, renouvelé automatiquement en 2022 puis désavoué en 2024; Lega dit qu’il n’a produit aucune initiative concrète.","linked_ids":["AXS-003","AXS-006"],"locator":"lines 161-171","materiality":"IMPORTANT","result_ids":["FCT-007","FCT-008"],"routes":["EXPAND","LINK"],"source_id":"SRC-004","status":"SATURATED"}
LED-004 | {"attempt_ids":["QRY-004","QRY-017","SRC-005"],"evidence_excerpt":"Le juge décrit des actes visant sans équivoque le financement illégal de la Lega, objectif non réalisé notamment parce que la vente de pétrole n’a pas eu lieu.","kind":"MECHANISM","lead":"Une négociation au Metropol visait selon le juge à financer illégalement la Lega, mais l’opération n’a pas abouti et aucun crime n’a pu être prouvé.","linked_ids":["AXS-003","AXS-004","AXS-005","AXS-009"],"locator":"Metropol 2018; décision de classement 27 avril 2023","materiality":"DECISIVE","result_ids":["FCT-009","FCT-010"],"routes":["EXPAND","LINK"],"source_id":"SRC-005","status":"SATURATED"}
LED-005 | {"attempt_ids":["QRY-005","QRY-018","SRC-006","QRY-019","SRC-007"],"evidence_excerpt":"Le règlement UE décrit financement/direction secrets par Medvedchuk via Marchevskyi et funneling de ressources pour un réseau d’influence auprès de représentants de partis.","kind":"MECHANISM","lead":"Voice of Europe est décrit par l’UE comme secrètement financé et dirigé par Medvedchuk et utilisé pour acheminer des ressources vers des propagandistes et un réseau reliant des représentants de partis européens.","linked_ids":["AXS-003","AXS-004","AXS-005","AXS-006"],"locator":"entry Voice of Europe / reasons for listing","materiality":"DECISIVE","result_ids":["FCT-011","FCT-012"],"routes":["EXPAND","LINK"],"source_id":"SRC-007","status":"SATURATED"}
LED-006 | {"attempt_ids":["QRY-006","QRY-020","SRC-008","QRY-011"],"evidence_excerpt":"La demande de levée d’immunité rapporte des accusations de corruption passive incluant espèces/crypto et contrepartie politique alléguée.","kind":"CLAIM","lead":"Le parquet de Munich allègue que Petr Bystron a reçu espèces/crypto de l’opérateur de Voice of Europe contre engagement à parler et voter dans l’intérêt du gouvernement russe; aucune condamnation n’est établie ici.","linked_ids":["AXS-003","AXS-005","AXS-008","AXS-009"],"locator":"recitals A-C","materiality":"DECISIVE","result_ids":["FCT-013","FCT-014"],"routes":["AUDIT","EXPAND","LINK"],"source_id":"SRC-008","status":"SATURATED"}
LED-007 | {"attempt_ids":["QRY-007","QRY-021","SRC-009","QRY-012"],"evidence_excerpt":"VDD confirme une procédure pénale ouverte sur soupçon de coopération possible avec les services russes et des perquisitions en juillet 2024.","kind":"CLAIM","lead":"Le VDD letton enquête pénalement sur une possible coopération de Tatjana Ždanoka avec les services russes; l’enquête publique disponible ne constitue pas une condamnation.","linked_ids":["AXS-003","AXS-006","AXS-008","AXS-009"],"locator":"criminal case opened 22 Feb 2024; searches 22 Jul 2024","materiality":"DECISIVE","result_ids":["FCT-015","FCT-016","FCT-017"],"routes":["AUDIT","EXPAND","LINK"],"source_id":"SRC-009","status":"SATURATED"}
LED-008 | {"attempt_ids":["QRY-009","QRY-023","SRC-011","QRY-010","QRY-024","SRC-012"],"evidence_excerpt":"La NCA conclut qu’aucune preuve reçue n’indique un financement par un tiers des prêts examinés ni un rôle d’agent pour un tiers.","kind":"CONTEXT","lead":"Leave.EU/Banks constitue un contrôle négatif: contacts russes documentés, mais la NCA n’a trouvé aucune preuve que les prêts examinés provenaient d’un tiers ou que Banks agissait pour un tiers.","linked_ids":["AXS-003","AXS-006","AXS-009"],"locator":"NCA update 29 April 2020","materiality":"IMPORTANT","result_ids":["FCT-018","FCT-019","FCT-020"],"routes":["EXPAND","LINK"],"source_id":"SRC-011","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le prêt russe au RN établit un financement par une entité bancaire russe, mais pas à lui seul une contrepartie, une coordination ou un commandement.","claimant":"INV-023","counter":["FCT-002"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001"]}
CLM-002 | {"claim":"L’accord FPÖ–Russie unie établit une coopération politique formelle; sa mise en œuvre matérielle et tout financement restent non établis dans le corpus retenu.","claimant":"INV-023","counter":"NONE_FOUND","gap":"Aucun transfert financier ni mise en œuvre matérielle substantielle de l’accord FPÖ–Russie unie n’est établi par le corpus borné.","gap_type":"SCOPE","materiality":"IMPORTANT","status":"PARTIAL","support":["FCT-004","FCT-005","FCT-006"]}
CLM-003 | {"claim":"L’accord Lega–Russie unie établit une coopération formelle mais Lega affirme qu’aucune initiative concrète n’en a résulté.","claimant":"INV-023","counter":["FCT-008"],"gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-007"]}
CLM-004 | {"claim":"Le schéma Metropol constitue une tentative documentée de financement illégal de la Lega, non réalisée; il ne peut être compté comme financement effectivement reçu.","claimant":"INV-023","counter":["FCT-010"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-010"]}
CLM-005 | {"claim":"Voice of Europe a servi de véhicule financier et de réseau d’influence reliant Medvedchuk et ses associés à des représentants de partis européens.","claimant":"INV-023","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-012"]}
CLM-006 | {"claim":"Le quid pro quo individuel allégué contre Petr Bystron reste une accusation pénale sérieuse, non une culpabilité judiciairement établie.","claimant":"INV-023","counter":"NONE_FOUND","gap":"Les sources inspectées établissent une procédure et des allégations détaillées, pas une condamnation judiciaire définitive pour le quid pro quo Voice of Europe.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-013","FCT-014"]}
CLM-007 | {"claim":"La coopération de Tatjana Ždanoka avec les services russes fait l’objet d’une enquête pénale et d’éléments journalistiques substantiels, mais n’est pas judiciairement établie dans les sources publiques retenues.","claimant":"INV-023","counter":"NONE_FOUND","gap":"L’enquête pénale et les fuites journalistiques ne constituent pas une décision judiciaire établissant coopération/tasking par le FSB.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-015","FCT-016","FCT-017"]}
CLM-008 | {"claim":"Les contacts russes d’Arron Banks sont documentés, mais la NCA a rejeté dans le dossier référé l’hypothèse d’un financement des prêts par un tiers; contacts ne valent donc pas financement étranger.","claimant":"INV-023","counter":["FCT-019"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-018","FCT-019","FCT-020"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-007","SRC-008","SRC-009","SRC-010","SRC-011","SRC-012"],"axis":"SOURCE_AUDIT","links":["LED-001","LED-002","LED-003","LED-004","LED-005","LED-006","LED-007","LED-008"],"question":"Les sources retenues distinguent-elles faits établis, allégations, décisions judiciaires et auto-déclarations ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020"],"sought_objects":["provenance","independence","procedural status"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-007","SRC-008","SRC-009","SRC-010","SRC-011","SRC-012"],"axis":"SCOPE_HISTORY","links":["LED-001","LED-002","LED-003","LED-004","LED-005","LED-006","LED-007","LED-008"],"question":"Quels liens matériels Russie–partis/mouvements sont documentés entre 2014 et 2026 et comment évoluent-ils ?","result_ids":["FCT-001","FCT-004","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-014","FCT-015","FCT-018","FCT-019"],"sought_objects":["chronology","agreements","finance","legal outcomes"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-007","SRC-008","SRC-009","SRC-010","SRC-011","SRC-012"],"axis":"EVIDENCE_CASES","links":["LED-001","LED-002","LED-003","LED-004","LED-005","LED-006","LED-007","LED-008"],"question":"Quels cas franchissent réellement les seuils relation, financement, accord, rémunération ou coopération ?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020"],"sought_objects":["case facts","amounts","agreements","proceedings"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-004","QRY-005","QRY-006","QRY-008","QRY-009","QRY-013","SRC-001","QRY-017","SRC-005","QRY-018","SRC-006","QRY-019","SRC-007","QRY-020","SRC-008","QRY-022","SRC-010","QRY-023","SRC-011"],"axis":"RESOURCES_FLOWS","links":["LED-001","LED-004","LED-005","LED-006","LED-008"],"question":"Quels flux financiers sont reçus, tentés, allégués ou réfutés ?","result_ids":["FCT-001","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-017","FCT-019","FCT-020","CAU-001","CAU-003","CAU-004","CAU-005","CAU-007"],"sought_objects":["loan","cash","crypto","attempted oil-sale funding","no-third-party-funding finding"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-007","SRC-008","SRC-009","SRC-010","SRC-011","SRC-012"],"axis":"MECHANISMS","links":["LED-001","LED-002","LED-003","LED-004","LED-005","LED-006","LED-007"],"question":"Quels mécanismes convertissent ressources ou relations en capacité d’influence politique ?","result_ids":["CAU-001","CAU-002","CAU-003","CAU-004","CAU-005","CAU-006","CAU-007"],"sought_objects":["loan dependence","party cooperation","paid influence","access/intermediation"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-007","SRC-008","SRC-009","SRC-010","SRC-011","SRC-012"],"axis":"ACTORS_RELATIONS","links":["LED-002","LED-003","LED-005","LED-006","LED-007","LED-008"],"question":"Quel niveau de relation peut être établi: indépendant, aligné, coopérant, coordonné, taské/commandé ?","result_ids":["ACT-001","ACT-002","ACT-003","ACT-004","ACT-005","ACT-006","ACT-007","ACT-008","CAU-002","CAU-004","CAU-005","CAU-006","CAU-007"],"sought_objects":["party agreements","intermediaries","intelligence allegations","network roles"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-007","SRC-008","SRC-009","SRC-010","SRC-011","SRC-012"],"axis":"RULES_CONTROLS","links":["LED-001","LED-004","LED-005","LED-006","LED-007","LED-008"],"question":"Quels contrôles juridiques/institutionnels détectent, limitent ou sanctionnent ces relations/flux ?","result_ids":["CTRL-001","CTRL-002","CTRL-003","CTRL-004","CTRL-005"],"sought_objects":["party-finance law","sanctions","criminal probes","parliamentary immunity"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-007","SRC-008","SRC-009","SRC-010","SRC-011","SRC-012"],"axis":"IMPACT_RESPONSIBILITY","gap":"Le corpus établit plusieurs relations, flux, tentatives et mécanismes, mais ne permet pas d’attribuer causalement un changement électoral ou politique agrégé à ces relations/financements.","gap_type":"CAUSALITY","links":["LED-001","LED-002","LED-003","LED-005","LED-006","LED-007"],"question":"Quels effets politiques ou institutionnels peuvent être causally attribués à ces financements/relations ?","result_ids":["CAU-001","CAU-002","CAU-003","CAU-004","CAU-005","CAU-006","CAU-007","ACT-001","ACT-002","ACT-003","ACT-004","ACT-005","ACT-006","ACT-007","ACT-008"],"sought_objects":["policy behavior","votes","access","institutional response"],"status":"GAP"}
AXS-009 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023","QRY-024","SRC-001","SRC-002","SRC-003","SRC-004","SRC-005","SRC-006","SRC-007","SRC-008","SRC-009","SRC-010","SRC-011","SRC-012"],"axis":"COUNTER_HYPOTHESES","links":["LED-001","LED-003","LED-004","LED-006","LED-007","LED-008"],"question":"Quelles accusations fortes échouent face aux contre-preuves ou restent non établies ?","result_ids":["FCT-002","FCT-006","FCT-008","FCT-010","FCT-019","CAU-005","CAU-006","CAU-007"],"sought_objects":["quid pro quo absence","no transfer","no third-party funding","no adjudication"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"ENABLER","counter":["FCT-002"],"limit":"Le financement reçu établit une dépendance/créance matérielle, pas une contrepartie, une instruction ni un effet politique causé.","mechanism":"Prêt bancaire russe → ressource financière disponible pour le parti RN/FN","status":"SUPPORTED","support":["FCT-001"]}
CAU-002 | {"causal_right":"ENABLER","counter":["FCT-006","FCT-008"],"limit":"Un accord formel crée un canal d’accès; l’implémentation, le financement et le tasking ne suivent pas automatiquement.","mechanism":"Accord interpartis FPÖ/Lega–Russie unie → canal institutionnalisé de contact et coopération","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-007"]}
CAU-003 | {"causal_right":"ENABLER","counter":["FCT-010"],"limit":"Le mécanisme est documenté comme objectif non réalisé; aucun flux reçu ne peut être inféré.","mechanism":"Négociation Metropol → mécanisme tenté de financement illégal de la Lega","status":"SUPPORTED","support":["FCT-009","FCT-010"]}
CAU-004 | {"causal_right":"CAUSE","counter":"NONE_FOUND","limit":"La chaîne est établie au niveau du véhicule/réseau selon l’UE; elle ne prouve pas que tout représentant exposé ou interviewé ait été rémunéré ou taské.","mechanism":"Financement/direction de Voice of Europe par Medvedchuk → rémunération de propagandistes + réseau d’influence auprès de représentants de partis","status":"SUPPORTED","support":["FCT-011","FCT-012"]}
CAU-005 | {"counter":"NONE_FOUND","gap":"Quid pro quo individuel non judiciairement établi dans les sources inspectées au 2026-09-06.","gap_type":"RESPONSIBILITY","limit":"La source est une procédure de levée d’immunité relayant les accusations du parquet, pas une décision de culpabilité.","mechanism":"Paiements Voice of Europe allégués à Petr Bystron → engagement allégué à parler/voter dans l’intérêt du gouvernement russe","status":"UNRESOLVED","support":["FCT-013","FCT-014"]}
CAU-006 | {"counter":"NONE_FOUND","gap":"Tasking/coopération avec le FSB non judiciairement établi dans les sources inspectées.","gap_type":"RESPONSIBILITY","limit":"Procédure pénale ouverte et matériau journalistique substantiel; absence de jugement définitif public dans le corpus.","mechanism":"Relations/courriels Ždanoka avec personnes identifiées comme FSB + demandes de financement alléguées → coopération politique/renseignement alléguée","status":"UNRESOLVED","support":["FCT-015","FCT-016","FCT-017"]}
CAU-007 | {"causal_right":"NO_VERIFIED_LINK","counter":["FCT-019"],"limit":"Les contacts et discussions d’affaires sont réels, mais la NCA n’a trouvé aucune preuve de financement des prêts par un tiers ni de rôle d’agent pour un tiers.","mechanism":"Contacts de Banks avec responsables russes → financement russe des prêts Leave.EU","status":"REFUTED","support":["FCT-018"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Interdiction française des prêts de banques hors EEE aux partis/campagnes depuis la loi du 15 septembre 2017","status":"SATURATED","support":["FCT-003"]}
CTRL-002 | {"control":"Sanctions UE contre Voice of Europe, Medvedchuk et Marchevskyi visant le véhicule financier et réseau d’influence","status":"SATURATED","support":["FCT-011","FCT-012"]}
CTRL-003 | {"control":"Levée d’immunité parlementaire permettant la poursuite de la procédure allemande Bystron","status":"SATURATED","support":["FCT-014"]}
CTRL-004 | {"control":"Procédure pénale et perquisitions du VDD dans le dossier Ždanoka","status":"SATURATED","support":["FCT-015","FCT-016"]}
CTRL-005 | {"control":"Enquête NCA sur la provenance des prêts Leave.EU, concluant à l’absence de preuve d’un financement par tiers dans le dossier référé","status":"SATURATED","support":["FCT-019","FCT-020"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Contracter un prêt de plus de 9,1 M€ auprès de First Czech Russian Bank","actor":"Front national / Rassemblement national et First Czech Russian Bank","intent":"Financement partisan documenté; toute contrepartie politique reste inconnue","status":"SATURATED","support":["FCT-001","FCT-002"]}
ACT-002 | {"action":"Signer un accord de coopération interpartis","actor":"FPÖ et Russie unie","intent":"Coopération politique/organisationnelle/économique telle qu’écrite dans l’accord","status":"SATURATED","support":["FCT-004","FCT-005","FCT-006"]}
ACT-003 | {"action":"Signer puis désavouer un accord de coopération interpartis","actor":"Lega et Russie unie","intent":"Coopération formelle; Lega affirme absence d’initiatives concrètes","status":"SATURATED","support":["FCT-007","FCT-008"]}
ACT-004 | {"action":"Négocier au Metropol un montage visant le financement illégal de la Lega","actor":"Gianluca Savoini et intermédiaires italiens/russes non tous identifiés","intent":"Objectif de financement illégal tel que décrit par le juge; objectif non réalisé","status":"SATURATED","support":["FCT-009","FCT-010"]}
ACT-005 | {"action":"Financer et diriger secrètement Voice of Europe comme véhicule de ressources et réseau d’influence","actor":"Viktor Medvedchuk via Artem Marchevskyi / Voice of Europe","intent":"Rémunérer des propagandistes et construire un réseau d’influence auprès de représentants de partis selon les actes UE","status":"SATURATED","support":["FCT-011","FCT-012"]}
ACT-006 | {"action":"Recevoir des paiements en espèces/crypto en échange d’engagements politiques","actor":"Petr Bystron / opérateur Voice of Europe","gap":"Alleged quid pro quo and receipt of payments remain under criminal proceedings in the inspected corpus; no final judicial finding establishing individual responsibility was inspected.","gap_type":"RESPONSIBILITY","intent":"Quid pro quo allégué par le parquet de Munich; non judiciairement établi ici","status":"GAP","support":["FCT-013","FCT-014"]}
ACT-007 | {"action":"Coopérer avec les services russes et solliciter des financements pour activités politiques","actor":"Tatjana Ždanoka / personnes identifiées comme FSB","gap":"Alleged cooperation/tasking with Russian intelligence remains under investigation in the inspected corpus; no final judicial finding establishing individual responsibility was inspected.","gap_type":"RESPONSIBILITY","intent":"Coopération/tasking allégués; enquête VDD en cours dans le corpus","status":"GAP","support":["FCT-015","FCT-016","FCT-017"]}
ACT-008 | {"action":"Rencontrer des responsables russes et discuter d’affaires pendant la période référendaire","actor":"Arron Banks / Andy Wigmore / responsables russes","intent":"Contacts et discussions d’affaires documentés; financement russe des prêts non établi","status":"SATURATED","support":["FCT-018","FCT-019"]}

SEARCH_ACTIVITY_V1:WEB:12|FETCH:12|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | PASS | runtime | R3P1 | INIT_CONTRACT
SYS-003 | SYS | PASS | controller | - | CORPUS_BOUND: six cases RN, FPÖ, Lega/Metropol, Voice of Europe/Bystron, Zdanoka, Leave.EU negative control; no exhaustive party census
SYS-004 | SYS | PASS | runtime | FCT-001 | REPAIR_FACT
SYS-005 | SYS | PASS | runtime | FCT-002 | REPAIR_FACT
SYS-006 | SYS | PASS | runtime | FCT-003 | REPAIR_FACT
SYS-007 | SYS | PASS | runtime | FCT-004 | REPAIR_FACT
SYS-008 | SYS | PASS | runtime | FCT-005 | REPAIR_FACT
SYS-009 | SYS | PASS | runtime | FCT-006 | REPAIR_FACT
SYS-010 | SYS | PASS | runtime | FCT-007 | REPAIR_FACT
SYS-011 | SYS | PASS | runtime | FCT-008 | REPAIR_FACT
SYS-012 | SYS | PASS | runtime | FCT-009 | REPAIR_FACT
SYS-013 | SYS | PASS | runtime | FCT-010 | REPAIR_FACT
SYS-014 | SYS | PASS | runtime | FCT-011 | REPAIR_FACT
SYS-015 | SYS | PASS | runtime | FCT-012 | REPAIR_FACT
SYS-016 | SYS | PASS | runtime | FCT-013 | REPAIR_FACT
SYS-017 | SYS | PASS | runtime | FCT-014 | REPAIR_FACT
SYS-018 | SYS | PASS | runtime | FCT-015 | REPAIR_FACT
SYS-019 | SYS | PASS | runtime | FCT-016 | REPAIR_FACT
SYS-020 | SYS | PASS | runtime | FCT-017 | REPAIR_FACT
SYS-021 | SYS | PASS | runtime | FCT-018 | REPAIR_FACT
SYS-022 | SYS | PASS | runtime | FCT-019 | REPAIR_FACT
SYS-023 | SYS | PASS | runtime | FCT-020 | REPAIR_FACT
SYS-024 | SYS | MNEMO_UNAVAILABLE | MnemoLite | NONE | MNEMO_Q
SYS-025 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | FOUND | - | - | Rassemblement National prêt russe Sénat 2024 CNCCFP banque russe contrepartie
QRY-002 | WEB | FOUND | - | - | FPÖ United Russia cooperation agreement 2016 2021 ORF
QRY-003 | WEB | FOUND | - | - | Lega United Russia cooperation agreement 2017 Reuters April 2024
QRY-004 | WEB | FOUND | - | - | Metropol Lega Savoini investigation shelved no money transferred 2023 ANSA
QRY-005 | WEB | FOUND | - | - | Voice of Europe Medvedchuk sanctions EU political parties financing Bystron
QRY-006 | WEB | FOUND | - | - | Petr Bystron immunity Voice of Europe European Parliament 2025
QRY-007 | WEB | FOUND | - | - | Tatjana Zdanoka VDD criminal proceedings Russia intelligence 2024
QRY-008 | WEB | FOUND | - | - | Ždanoka emails FSB funding request Latvian public media 2024
QRY-009 | WEB | FOUND | - | - | Leave.EU Arron Banks NCA Russian funding no evidence Electoral Commission
QRY-010 | WEB | FOUND | - | - | Arron Banks Russian embassy meetings House of Commons DCMS
QRY-011 | WEB | FOUND | - | - | Petr Bystron Voice of Europe conviction trial 2026
QRY-012 | WEB | FOUND | - | - | Tatjana Ždanoka 2026 investigation Russia intelligence
QRY-013 | FETCH | FOUND | SRC-001 | https://www.senat.fr/rap/r23-739-1/r23-739-113.html | FETCH inspected canonical source
QRY-014 | FETCH | FOUND | SRC-002 | https://newsv2.orf.at/stories/2371673/ | FETCH inspected canonical source
QRY-015 | FETCH | FOUND | SRC-003 | https://orf.at/stories/3239554/ | FETCH inspected canonical source
QRY-016 | FETCH | FOUND | SRC-004 | https://www.reuters.com/world/europe/italys-league-disavows-accord-with-russias-ruling-party-2024-04-02/ | FETCH inspected canonical source
QRY-017 | FETCH | FOUND | SRC-005 | https://www.ansa.it/amp/english/news/2023/04/27/league-russian-funds-probe-shelved_ec89ae0d-6dcb-42d2-ac42-92dd33d97689.html | FETCH inspected canonical source
QRY-018 | FETCH | FOUND | SRC-006 | https://www.consilium.europa.eu/en/press/press-releases/2024/05/27/information-manipulation-in-russia-s-war-of-aggression-against-ukraine-eu-lists-two-individuals-and-one-entity/ | FETCH inspected canonical source
QRY-019 | FETCH | FOUND | SRC-007 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1493 | FETCH inspected canonical source
QRY-020 | FETCH | FOUND | SRC-008 | https://www.europarl.europa.eu/doceo/document/TA-10-2025-0067_EN.html | FETCH inspected canonical source
QRY-021 | FETCH | FOUND | SRC-009 | https://vdd.gov.lv/en/news/press-releases/vdd-carries-out-criminal-proceedings-in-the-criminal-case-against-tatjana-zdanoka | FETCH inspected canonical source
QRY-022 | FETCH | FOUND | SRC-010 | https://eng.lsm.lv/article/politics/politics/29.01.2024-latvian-mep-zdanoka-named-as-russian-fsb-asset.a540771/ | FETCH inspected canonical source
QRY-023 | FETCH | FOUND | SRC-011 | https://www.electoralcommission.org.uk/cy/node/606 | FETCH inspected canonical source
QRY-024 | FETCH | FOUND | SRC-012 | https://publications.parliament.uk/pa/cm201719/cmselect/cmcumeds/363/36308.htm | FETCH inspected canonical source

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:senat | SENAT:R23-739-1:CH13 | Lutte contre les influences étrangères malveillantes — Rapport n°739, tome I | 2024-07-23 | 2026-09-06 | lines 113-149; financement politique, CNCCFP, prêt RN | https://www.senat.fr/rap/r23-739-1/r23-739-113.html
SRC-002 | ◉ | fam:other:orf | ORF:2371673 | Kooperationsvertrag zwischen FPÖ und Putin-Partei | 2016-12-19 | 2026-09-06 | accord FPÖ–United Russia, contenu et durée | https://newsv2.orf.at/stories/2371673/
SRC-003 | ◉ | fam:other:orf | ORF:3239554 | FPÖ verlängert Kooperation mit Putin-Partei nicht | 2021-12-09 | 2026-09-06 | non-renouvellement 2021; rappel du contenu de l’accord | https://orf.at/stories/3239554/
SRC-004 | ◉ | fam:other:reuters | REUTERS:2024-04-02:LEAGUE-UR | Italy's League disavows accord with Russia's ruling party | 2024-04-02 | 2026-09-06 | lines 151-176; accord 2017, renouvellement 2022, désaveu 2024 | https://www.reuters.com/world/europe/italys-league-disavows-accord-with-russias-ruling-party-2024-04-02/
SRC-005 | ◉ | fam:other:ansa | ANSA:2023-04-27:METROPOL | League Russian-funds probe shelved | 2023-04-27 | 2026-09-06 | Metropol 2018; classement; objectif de financement illégal non réalisé | https://www.ansa.it/amp/english/news/2023/04/27/league-russian-funds-probe-shelved_ec89ae0d-6dcb-42d2-ac42-92dd33d97689.html
SRC-006 | ◈ | fam:other:eu-sanctions | EU-CONSILIUM:2024-05-27:VOICE-EUROPE | Information manipulation: EU lists Medvedchuk, Marchevskyi and Voice of Europe | 2024-05-27 | 2026-09-06 | Voice of Europe as funding vehicle and political influence network | https://www.consilium.europa.eu/en/press/press-releases/2024/05/27/information-manipulation-in-russia-s-war-of-aggression-against-ukraine-eu-lists-two-individuals-and-one-entity/
SRC-007 | ◈ | fam:other:eu-sanctions | EURLEX:32024R1493 | Council Implementing Regulation (EU) 2024/1493 | 2024-05-27 | 2026-09-06 | entry 426 Voice of Europe; secret financing/direction and funneling resources | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1493
SRC-008 | ◈ | fam:other:ep | EP:P10_TA(2025)0067 | European Parliament decision of 6 May 2025 on waiver of immunity of Petr Bystron | 2025-05-06 | 2026-09-06 | recitals A-C; alleged Voice of Europe cash/crypto quid pro quo | https://www.europarl.europa.eu/doceo/document/TA-10-2025-0067_EN.html
SRC-009 | ◈ | fam:other:vdd | VDD:2024-07-24:ZDANOKA | VDD carries out criminal proceedings in case against Tatjana Ždanoka | 2024-07-24 | 2026-09-06 | criminal case opened 22 Feb 2024; searches 22 Jul 2024; suspicion of cooperation with Russian services | https://vdd.gov.lv/en/news/press-releases/vdd-carries-out-criminal-proceedings-in-the-criminal-case-against-tatjana-zdanoka
SRC-010 | ◉ | fam:other:rebaltica-zdanoka | LSM:2024-01-29:ZDANOKA | Latvian MEP Ždanoka named as Russian FSB asset | 2024-01-29 | 2026-09-06 | summary of Re:Baltica/The Insider leaked-email investigation and funding requests | https://eng.lsm.lv/article/politics/politics/29.01.2024-latvian-mep-zdanoka-named-as-russian-fsb-asset.a540771/
SRC-011 | ◈ | fam:other:uk-ec-nca | UK-EC:LEAVEEU:NCA-UPDATE-2020 | Investigation into payments made to Better for the Country and Leave.EU | 2020-04-29 | 2026-09-06 | NCA update: no evidence of third-party funding or agency for third party | https://www.electoralcommission.org.uk/cy/node/606
SRC-012 | ◈ | fam:other:uk-hoc | UK-HOC:HC363:2018:CH5 | Disinformation and 'fake news': Interim Report — Leave.EU, Arron Banks, and Russia | 2018-07-29 | 2026-09-06 | paras 177-191; Russian embassy meetings, business discussions, funding concern | https://publications.parliament.uk/pa/cm201719/cmselect/cmcumeds/363/36308.htm

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-113.html | other:senat | 2024-07-23 | RN_LOAN_2014_AMOUNT | En 2014, le Front national a obtenu un prêt de plus de 9,1 millions d’euros auprès de First Czech Russian Bank. | -
FCT-002 | EVIDENCE | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-113.html | other:senat | 2024-07-23 | RN_LOAN_COUNTERPARTY_UNKNOWN | La CNCCFP a indiqué n’avoir aucun moyen de savoir si le prêt russe du RN était assorti de contreparties et n’a jamais pris de position permettant de le qualifier positivement d’ingérence. | -
FCT-003 | FACT | ✧ | https://www.senat.fr/rap/r23-739-1/r23-739-113.html | other:senat | 2024-07-23 | FRANCE_NON_EEA_BANK_LOAN_BAN | Depuis la loi du 15 septembre 2017, les banques hors EEE ne peuvent plus financer un parti politique ou une campagne en France. | -
FCT-004 | FACT | ✧ | https://newsv2.orf.at/stories/2371673/ | other:orf | 2016-12-19 | FPO_UR_AGREEMENT_SIGNED | Le FPÖ et Russie unie ont signé à Moscou le 19 décembre 2016 un accord de coopération initialement valable cinq ans. | -
FCT-005 | FACT | ✧ | https://newsv2.orf.at/stories/2371673/ | other:orf | 2016-12-19 | FPO_UR_AGREEMENT_TERMS | L’accord FPÖ–Russie unie prévoyait notamment échanges réguliers de délégations, échanges d’expérience législative et soutien à la coopération économique, commerciale et d’investissement. | -
FCT-006 | FACT | ✧ | https://orf.at/stories/3239554/ | other:orf | 2021-12-09 | FPO_UR_NOT_RENEWED | En décembre 2021, le FPÖ a annoncé qu’il ne prolongerait pas l’accord avec Russie unie arrivant à échéance. | -
FCT-007 | FACT | ✧ | https://www.reuters.com/world/europe/italys-league-disavows-accord-with-russias-ruling-party-2024-04-02/ | other:reuters | 2024-04-02 | LEGA_UR_AGREEMENT_TIMELINE | La Lega a conclu en 2017 un accord de coopération de cinq ans avec Russie unie; Reuters rapporte qu’il a été automatiquement renouvelé en 2022. | -
FCT-008 | EVIDENCE | ✧ | https://www.reuters.com/world/europe/italys-league-disavows-accord-with-russias-ruling-party-2024-04-02/ | other:reuters | 2024-04-02 | LEGA_UR_DISAVOWAL_NO_INITIATIVES | Le 2 avril 2024, la Lega a déclaré l’accord avec Russie unie sans validité après l’invasion de l’Ukraine et a affirmé qu’il n’avait produit aucune initiative concrète. | -
FCT-009 | EVIDENCE | ✧ | https://www.ansa.it/amp/english/news/2023/04/27/league-russian-funds-probe-shelved_ec89ae0d-6dcb-42d2-ac42-92dd33d97689.html | other:ansa | 2023-04-27 | METROPOL_ILLICIT_FINANCING_AIM | Le juge milanais ayant classé l’enquête Metropol a estimé que les actes découverts visaient sans équivoque l’objectif final de financer illégalement la Lega. | -
FCT-010 | FACT | ✧ | https://www.ansa.it/amp/english/news/2023/04/27/league-russian-funds-probe-shelved_ec89ae0d-6dcb-42d2-ac42-92dd33d97689.html | other:ansa | 2023-04-27 | METROPOL_UNFULFILLED_SHELVED | L’objectif financier du schéma Metropol n’a pas été réalisé, notamment parce que la transaction pétrolière principale n’a pas eu lieu; l’enquête a été classée faute de crime prouvé. | -
FCT-011 | FACT | ✧ | https://www.consilium.europa.eu/en/press/press-releases/2024/05/27/information-manipulation-in-russia-s-war-of-aggression-against-ukraine-eu-lists-two-individuals-and-one-entity/ | other:eu-sanctions | 2024-05-27 | VOICE_EUROPE_FINANCIAL_INFLUENCE_NETWORK | Les actes de l’UE décrivent Voice of Europe comme un véhicule d’acheminement de ressources financières destinées à rémunérer des propagandistes et à construire un réseau influençant des représentants de partis politiques européens. | -
FCT-012 | FACT | ✧ | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1493 | other:eu-sanctions | 2024-05-27 | VOICE_EUROPE_MEDVEDCHUK_DIRECTION | Le règlement UE indique que Voice of Europe était secrètement financé et dirigé par Viktor Medvedchuk via Artem Marchevskyi. | -
FCT-013 | EVIDENCE | ✧ | https://www.europarl.europa.eu/doceo/document/TA-10-2025-0067_EN.html | other:ep | 2025-05-06 | BYSTRON_VOE_ALLEGED_QUID_PRO_QUO | La demande transmise au Parlement européen allègue que Petr Bystron a pu recevoir espèces ou cryptomonnaies de l’opérateur de Voice of Europe en contrepartie d’un engagement à parler et voter dans l’intérêt du gouvernement russe. | -
FCT-014 | FACT | ✧ | https://www.europarl.europa.eu/doceo/document/TA-10-2025-0067_EN.html | other:ep | 2025-05-06 | BYSTRON_IMMUNITY_WAIVED_VOE_CASE | Le Parlement européen a levé le 6 mai 2025 l’immunité de Petr Bystron dans la procédure liée notamment aux accusations de corruption passive, blanchiment, fraude et fraude fiscale. | -
FCT-015 | FACT | ✧ | https://vdd.gov.lv/en/news/press-releases/vdd-carries-out-criminal-proceedings-in-the-criminal-case-against-tatjana-zdanoka | other:vdd | 2024-07-24 | ZDANOKA_VDD_CRIMINAL_CASE | Le VDD letton a ouvert le 22 février 2024 une affaire pénale sur la suspicion d’une possible coopération de Tatjana Ždanoka avec les services russes de renseignement et de sécurité. | -
FCT-016 | FACT | ✧ | https://vdd.gov.lv/en/news/press-releases/vdd-carries-out-criminal-proceedings-in-the-criminal-case-against-tatjana-zdanoka | other:vdd | 2024-07-24 | ZDANOKA_VDD_SEARCHES | Le VDD a mené le 22 juillet 2024 des opérations de perquisition sur deux sites liés à Ždanoka et saisi supports de données, notes et documents pour analyse. | -
FCT-017 | EVIDENCE | ✧ | https://eng.lsm.lv/article/politics/politics/29.01.2024-latvian-mep-zdanoka-named-as-russian-fsb-asset.a540771/ | other:rebaltica-zdanoka | 2024-01-29 | ZDANOKA_LEAKED_EMAILS_FUNDING_REQUESTS | LSM rapporte l’enquête Re:Baltica/The Insider fondée sur des courriels divulgués décrivant des échanges avec des personnes identifiées comme agents du FSB, dont des demandes de financement pour des activités politiques. | -
FCT-018 | FACT | ✧ | https://publications.parliament.uk/pa/cm201719/cmselect/cmcumeds/363/36308.htm | other:uk-hoc | 2018-07-29 | BANKS_RUSSIAN_EMBASSY_CONTACTS | La commission DCMS de la Chambre des communes a documenté plusieurs rencontres entre Arron Banks/Andy Wigmore et des responsables russes, dont l’ambassadeur, ainsi que des discussions d’affaires. | -
FCT-019 | FACT | ✧ | https://www.electoralcommission.org.uk/cy/node/606 | other:uk-ec-nca | 2020-04-29 | LEAVEEU_NCA_NO_THIRD_PARTY_FUNDING | Après enquête, la NCA a conclu n’avoir reçu aucune preuve suggérant que Banks ou ses sociétés avaient reçu des fonds d’un tiers pour financer les prêts examinés, ni que Banks agissait comme agent d’un tiers; l’Electoral Commission a accepté cette conclusion. | -
FCT-020 | FACT | ✧ | https://www.electoralcommission.org.uk/cy/node/606 | other:uk-ec-nca | 2020-04-29 | LEAVEEU_LOANS_SCOPE | Le dossier référé portait sur 8 millions de livres de financement à Better for the Country et Leave.EU, dont 6 millions destinés à Leave.EU. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-002
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-004
FCT-009 | SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-006,SRC-007
FCT-012 | SRC-007
FCT-013 | SRC-008
FCT-014 | SRC-008
FCT-015 | SRC-009
FCT-016 | SRC-009
FCT-017 | SRC-010
FCT-018 | SRC-012
FCT-019 | SRC-011
FCT-020 | SRC-011

## REFUTATION_REGISTRY_V1

## WRITEBACK_PLAN_V1
FCT-001 | ELIGIBLE:VERIFIE
FCT-002 | SKIP:NOT_ELIGIBLE
FCT-003 | ELIGIBLE:VERIFIE
FCT-004 | ELIGIBLE:VERIFIE
FCT-005 | ELIGIBLE:VERIFIE
FCT-006 | ELIGIBLE:VERIFIE
FCT-007 | ELIGIBLE:VERIFIE
FCT-008 | SKIP:NOT_ELIGIBLE
FCT-009 | SKIP:NOT_ELIGIBLE
FCT-010 | ELIGIBLE:VERIFIE
FCT-011 | ELIGIBLE:VERIFIE
FCT-012 | ELIGIBLE:VERIFIE
FCT-013 | SKIP:NOT_ELIGIBLE
FCT-014 | ELIGIBLE:VERIFIE
FCT-015 | ELIGIBLE:VERIFIE
FCT-016 | ELIGIBLE:VERIFIE
FCT-017 | SKIP:NOT_ELIGIBLE
FCT-018 | ELIGIBLE:VERIFIE
FCT-019 | ELIGIBLE:VERIFIE
FCT-020 | ELIGIBLE:VERIFIE

## MEMORY_WRITE_MODE_V1
FCT-001 | WRITE | -
FCT-003 | WRITE | -
FCT-004 | WRITE | -
FCT-005 | WRITE | -
FCT-006 | WRITE | -
FCT-007 | WRITE | -
FCT-010 | WRITE | -
FCT-011 | WRITE | -
FCT-012 | WRITE | -
FCT-014 | WRITE | -
FCT-015 | WRITE | -
FCT-016 | WRITE | -
FCT-018 | WRITE | -
FCT-019 | WRITE | -
FCT-020 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:6
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:8
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:12
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18b

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T11:36:29.440141+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":15,"eligible":15,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:15;attempted:0;success:0;failure:0;blocked:15} | WRITEBACK_EXECUTION_V1:[15 rows, see section]

## WRITEBACK_EXECUTION_V1
FCT-001 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-003 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-004 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-005 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-006 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-007 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-010 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-011 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-012 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-014 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-015 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-016 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-018 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-019 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-020 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
