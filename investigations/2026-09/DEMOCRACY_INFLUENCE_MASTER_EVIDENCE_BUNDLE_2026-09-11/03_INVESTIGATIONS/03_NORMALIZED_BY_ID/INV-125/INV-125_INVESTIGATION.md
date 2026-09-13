ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260909-2207-critical-digital-infrastructure-sovereignty | PARENT_RUN_ID:NONE | AS_OF:2026-09-09
INPUT_KIND:RUN_CARD | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/inv125/runtime/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-09_critical-digital-infrastructure-sovereignty/2026-09-09_22-07_critical-digital-infrastructure-sovereignty_INPUT.md | SUBJECT_SLUG:critical-digital-infrastructure-sovereignty | SUBJECT_FP:sha256:f03741a3f17f87cb5ca9f1a895637d1c801b7c3a9d3d86b5aec6cf713af1c633 | INPUT_SHA256:sha256:d98e718dcd7898ebc4a2e04612224266c0a5b6dec8070cb3899b84b9f72990cc
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France et Union européenne, principalement 2018-2026; fournisseur/juridiction/contrôle -> contrat ou dépendance technique -> point de contrainte (ordre, accès, interruption, refus, coût de sortie) -> institution/entreprise/média -> adaptation/décision -> effet; dependency != coercion; foreign provider != foreign control; legal reach != exercised access; outage != political action; switching cost != capture; capability != use.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/NETWORK.md,clusters/MONEY.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
## Question et chaîne testée

INV-125 teste une chaîne stricte : fournisseur, juridiction ou point de contrôle -> contrat ou dépendance technique -> contrainte effectivement disponible ou exercée -> acteur français/européen -> adaptation ou décision -> effet. La distinction centrale est entre **dépendance**, **capacité de contrainte**, **usage de cette capacité** et **effet politique**. Le corpus ne traite donc ni la présence d’un fournisseur étranger ni une vulnérabilité technique comme une preuve d’ingérence.

## Cloud : dépendance de marché et coût de sortie

La Commission européenne considère à titre préliminaire en 2026 qu’AWS et Azure occupent les deux premières positions du cloud dans l’Union et présentent des bases utilisateurs enracinées, des effets de lock-in et des coûts élevés de changement [FCT-001,FCT-002]. Cette constatation ferme un mécanisme économique : lorsqu’un workload, ses données, ses interfaces et ses applications sont fortement intégrés à un fournisseur, la capacité de sortie peut devenir coûteuse et lente. Ce mécanisme réduit les options de l’utilisateur mais ne démontre aucune instruction politique imposée par le fournisseur.

Le Data Act apporte un contrôle décisif. Il part explicitement de barrières au changement de fournisseur, notamment frais de sortie de données, procédures longues et manque d’interopérabilité, puis impose des obligations de portabilité, d’interfaces, d’assistance et de transparence [FCT-003,FCT-004,FCT-005]. L’objectif multi-cloud vise précisément à réduire la dépendance à un fournisseur unique [FCT-006]. Le fait qu’un législateur crée des droits de sortie confirme la matérialité du lock-in ; il ne transforme pas ce lock-in en coercition politique.

## Portée juridique extraterritoriale : capacité et usage

Le CLOUD Act fournit un cas clair de portée juridique. Le mécanisme permet, dans certaines conditions, des ordres légaux transfrontaliers visant des données sous contrôle de fournisseurs couverts [FCT-007]. Cette capacité doit être distinguée d’un accès effectivement demandé ou exécuté [FCT-008].

Le Health Data Hub fournit un cas français où la capacité juridique a produit un effet institutionnel sans preuve d’accès américain. Le contrat avec Microsoft Ireland exposait le service à un groupe soumis au droit américain ; le Conseil d’État a retenu que le risque d’une demande américaine ne pouvait être totalement exclu, mais n’a pas constaté d’accès effectif [FCT-009]. Il a exigé des précautions contractuelles supplémentaires et a situé celles-ci dans l’attente d’une solution éliminant le risque [FCT-010]. La CNIL formule la même distinction : la localisation européenne des données ne neutralise pas nécessairement la portée juridique liée au groupe contrôlant le fournisseur [FCT-011,FCT-012].

SecNumCloud 3.2 matérialise la réponse française à cette asymétrie. Le référentiel combine protections techniques, organisationnelles et juridiques, y compris des conditions de gouvernance et de contrôle capitalistique destinées à réduire l’exposition aux lois non européennes [FCT-013,FCT-014]. Ce dispositif prouve que le risque est suffisamment matériel pour modifier les critères d’achat et de certification. Il ne prouve pas qu’une injonction étrangère ait été exécutée dans chaque service concerné.

## Semi-conducteurs : la contrainte réglementaire la plus directement observée

Les contrôles à l’exportation fournissent une chaîne plus fermée. En 2024 puis 2025, les Pays-Bas ont élargi les obligations de licence applicables à des équipements avancés de fabrication, de métrologie et d’inspection [FCT-015,FCT-017]. Le gouvernement les motive par des risques de sécurité et le contexte géopolitique [FCT-016]. Le contrôle reste ciblé : obligation d’autorisation ne signifie pas embargo général [FCT-018].

ASML documente l’effet opérationnel de ces régimes. Son rapport 2024 indique que certains systèmes DUV auparavant concernés par les règles américaines doivent désormais faire l’objet d’une licence néerlandaise, et que les contrôles américains ont parallèlement étendu des restrictions sur technologies, logiciels et sites [FCT-019,FCT-020]. Son rapport 2025 précise que les changements de contrôle export peuvent affecter matériellement volume, mix et calendrier des ventes [FCT-021]. Ici, la chaîne `règle -> licence -> activité commerciale` est donc fermée. En revanche, aucun effet électoral ou décision politique européenne aval n’est identifié.

Le même rapport apporte un contrôle négatif utile sur les matières premières : face aux restrictions chinoises de 2025 sur certaines terres rares, ASML avait mis en place une équipe et des plans de mitigation, mais ne constatait pas encore d’impact matériel sur ses clients [FCT-022]. Dépendance et impact réalisé doivent donc rester séparés.

## Dépendances structurelles : exposition élevée, coercition conditionnelle

Le rapport européen sur la compétitivité décrit des dépendances fortes : absence de fonderie européenne sous 22 nm, 75 à 90 % de la capacité de fabrication de wafers située en Asie, dépendance aux GPU avancés américains et à plusieurs segments non européens de la chaîne de valeur [FCT-023]. Ces concentrations augmentent l’exposition à des contrôles, ruptures ou décisions de fournisseurs, mais ne constituent pas une preuve de capture ou de commandement politique [FCT-024].

La stratégie européenne de sécurité économique fait précisément de la « weaponisation » des dépendances et de la coercition économique une catégorie de risque, tout en déclenchant des instruments de réduction de dépendance et de contrôle ciblé dans les technologies critiques [FCT-025,FCT-026]. L’adaptation de politique publique confirme la matérialité de l’exposition ; elle ne valide pas rétroactivement tous les scénarios de coercition.

## Câbles sous-marins : criticité et attribution

Les câbles constituent enfin un cas de dépendance physique critique. Ils transportent l’immense majorité du trafic intercontinental et plusieurs incidents récents ont mis en évidence vulnérabilités et dépendances [FCT-027]. Le plan européen 2025 puis la toolbox 2026 répondent par cartographie, stress tests, capacités de réparation, projets prioritaires et mesures de prévention/détection/réponse/dissuasion [FCT-028]. Le corpus ne permet toutefois pas de transformer l’existence d’incidents ou de vulnérabilités en attribution générale à une puissance étrangère ou en preuve d’un effet politique coercitif.

## Conclusion forensique

La dépendance numérique devient un **levier de pouvoir démontré** seulement lorsqu’un point de contrôle est identifiable et qu’une contrainte ou une adaptation observable suit. Trois formes sont fermées ici : (1) coûts et obstacles de sortie cloud reconnus et réglementés ; (2) portée juridique extra-européenne ayant provoqué des adaptations contractuelles et de certification en France ; (3) contrôles export ayant modifié les obligations de licence et la conduite commerciale d’ASML. Les dépendances semi-conducteurs et câbles sont également matérielles, mais leur conversion en coercition doit être démontrée cas par cas. Aucune preuve générale ne ferme `dépendance étrangère -> commandement politique -> effet démocratique`.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:2|EDI_DECISIVE:5|SRC_COMPLETE:14/14

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-09
- **notes:**
  - Commission cloud DMA view is preliminary as of 2026-06-25
  - Data Act switching charges phase-out completes 2027-01-12
  - ASML 2025 annual report includes controls and mitigation status through 2025
  - Cable toolbox published 2026-02-05
- **status:** CURRENT
- **window:** 2018-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official risk frameworks are not evidence every threat materialized
  - market concentration is not political tasking
  - export licensing is a stronger observed constraint than generic dependency
- **clusters:**
  - NETWORK
  - MONEY
- **complexity:** HIGH
- **implicit:**
  - exit options determine bargaining exposure
  - legal jurisdiction can matter independently of data location
  - supply concentration creates leverage potential but not necessarily exercised coercion
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - lock-in
  - extraterritorial reach
  - export licensing
  - supply-chain concentration
  - critical infrastructure resilience
- **priorities:**
  - constraint exercised
  - adaptation
  - effect ceiling
  - negative controls
- **query_guidance:** Prefer official legal decisions, regulators, government export rules and company filings; retain non-use and no-material-impact controls.
- **rhetorical:**
  - digital colony umbrella
  - sovereignty absolutism
  - foreign vendor guilt
- **speaker:**
  - **goal:** forensic dependency-to-constraint mapping
  - **target:** provider/jurisdiction/control -> dependency -> constraint -> adaptation -> effect
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** provider
  - **S02:** jurisdiction
  - **S03:** contract
  - **S04:** lock-in
  - **S05:** switching-cost
  - **S06:** legal-order
  - **S07:** data-access
  - **S08:** license
  - **S09:** export-control
  - **S10:** supply-chain
  - **S11:** chip
  - **S12:** raw-material
  - **S13:** cable
  - **S14:** adaptation
  - **S15:** political-effect
- **threats:**
  - dependency=coercion
  - foreign provider=foreign control
  - legal reach=exercised access
  - outage=political action
  - switching cost=capture
  - capability=use

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - actor-specific political downstream effect
  - **input_ids:**
    - FCT-001
    - FCT-007
    - FCT-009
    - FCT-019
    - FCT-023
    - FCT-027
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - foreign provider alone does not establish foreign control
  - **not_computable:**
    - NONE
  - **operations_applied:**
    - provider-jurisdiction mapping
    - supply-chain edge separation
  - **reason:** map control edges without dependency=command inflation
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CLM-006
    - CLM-007
    - CAU-001
    - CAU-002
    - CAU-003
  - **status:** PASS
  - **trigger:** provider-jurisdiction-supply-chain relations are central
- **item 2:**
  - **gaps:**
    - comparable switching-cost denominator
  - **input_ids:**
    - FCT-002
    - FCT-004
    - FCT-021
    - FCT-022
    - FCT-028
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - cost or sales impact does not establish political capture
  - **not_computable:**
    - NONE
  - **operations_applied:**
    - exit-cost separation
    - business-impact boundary
  - **reason:** trace economic constraint without cost=capture inference
  - **result_ids:**
    - CLM-001
    - CLM-006
    - CAU-001
    - CAU-003
    - CAU-004
  - **status:** PASS
  - **trigger:** switching costs, sales impacts and infrastructure investment are material

### SCOPING_REPORT
- **actors_institutions:**
  - European Commission
  - Microsoft/Azure
  - AWS
  - US Department of Justice
  - Health Data Hub
  - CNIL
  - ANSSI/SecNumCloud
  - Dutch government
  - ASML
- **domains:**
  - cloud
  - data jurisdiction
  - semiconductors
  - supply chains
  - submarine cables
- **evidence_limits:**
  - DMA cloud finding is preliminary
  - CLOUD Act capability not exercised access evidence
  - ASML rare-earth impact was not material at report date
  - cable toolbox addresses mixed intentional/non-intentional incidents
- **exclusions:**
  - generic anti-US or anti-China claims
  - outages without attribution
  - foreign dependency without constraint path
  - political effect without adaptation evidence
- **geo:** France and European Union
- **period:** 2018-2026

### CREDO
- dependency != coercion
- foreign provider != foreign control
- legal reach != exercised access
- outage != political action
- switching cost != capture
- capability != use
- license != embargo
- risk response != proof of attack

### COGNITIVE_MAP
- **input_kind:** RUN_CARD
- **mission_mode:** INVESTIGATION
- **patterns:**
  - lock-in
  - jurisdictional reach
  - export control
  - supply concentration
  - resilience response
- **priorities:**
  - exercised constraint
  - institutional adaptation
  - measured business effect
  - effect ceiling
- **query_guidance:** close each edge separately and preserve non-use/no-impact controls
- **speaker:**
  - **goal:** bounded causal mapping
  - **tone:** forensic
- **threats:**
  - capability inflation
  - jurisdiction=access leap
  - dependency=coercion leap

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Many dependencies remain market risks or legal capabilities without exercised coercion.
  - **support:**
    - FCT-002
    - FCT-008
    - FCT-010
    - FCT-021
    - FCT-024
    - FCT-028
  - **synthesis:** Classify leverage only when a constraint edge and adaptation/effect are evidenced.
  - **thesis:** Digital dependencies can create real leverage points over European actors.
- **item 2:**
  - **antithesis:** EU hosting and contractual safeguards can reduce risk, and no Health Data Hub access was established.
  - **support:**
    - FCT-007
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
    - FCT-013
  - **synthesis:** Legal reach is a material sovereignty risk but access/use remains a separate evidentiary gate.
  - **thesis:** Extraterritorial law can reach providers controlling EU-hosted data.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **flow:** customer workload/data -> concentrated cloud provider -> switching/egress/interoperability costs
  - **resource:** data, applications, operational continuity
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
- **item 2:**
  - **flow:** jurisdiction -> covered provider -> legal order capability -> controlled data
  - **resource:** legal authority and data control
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-011
- **item 3:**
  - **flow:** export-control authority -> license requirement -> ASML shipment/compliance -> sales timing/mix
  - **resource:** market access and technology transfer
  - **support:**
    - FCT-015
    - FCT-017
    - FCT-019
    - FCT-020
    - FCT-021

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** US legal jurisdiction
  - **relation:** potential lawful data orders
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-011
  - **to:** covered cloud/service providers
- **item 2:**
  - **from:** French/EU governance
  - **relation:** contractual/certification mitigation
  - **support:**
    - FCT-010
    - FCT-013
    - FCT-014
  - **to:** sensitive cloud/data processing
- **item 3:**
  - **from:** Dutch/US export-control regimes
  - **relation:** license and technology restrictions
  - **support:**
    - FCT-015
    - FCT-017
    - FCT-019
    - FCT-020
    - FCT-021
  - **to:** ASML/customer shipments

### IMPACT_MAP
- **highest_supported_edge:** rule or structural dependency -> concrete switching/licensing/governance constraint -> documented adaptation
- **not_established:**
  - general foreign cloud political tasking
  - Health Data Hub US access
  - dependency as capture
  - general cable sabotage attribution
  - downstream electoral effect
- **support:**
  - FCT-002
  - FCT-010
  - FCT-021
  - FCT-022
  - FCT-028

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Data Act creates portability and no political command by provider is shown
  - **issue:** cloud dependence vs coercion
  - **pro:** lock-in and switching costs are officially identified
  - **resolution:** material dependency supported; coercion unproven
  - **support:**
    - FCT-001
    - FCT-002
    - FCT-003
    - FCT-004
- **item 2:**
  - **contra:** Health Data Hub case found risk but no proven access and imposed safeguards
  - **issue:** legal reach vs access
  - **pro:** CLOUD Act and US-group control create legal capability
  - **resolution:** capability and governance effect supported; exercised access unresolved
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-010
    - FCT-011
    - FCT-012
- **item 3:**
  - **contra:** some rare-earth restrictions had no material customer impact at report date
  - **issue:** supply dependency vs actual constraint
  - **pro:** export licenses affect ASML operations and EU depends on non-EU chip capacity
  - **resolution:** constraint is actor-specific where licensing occurs; general dependency effects remain conditional
  - **support:**
    - FCT-019
    - FCT-021
    - FCT-022
    - FCT-023
    - FCT-024

### VERIFICATION_REPORT
- **circular_families:**
  - cloud competition/switching family A
  - jurisdiction/data governance family B
  - semiconductor export-control family C
  - EU structural-dependency family D
  - cable-resilience family E
- **contradiction_ids:**
  - dependency-vs-coercion
  - legal-reach-vs-access
  - structural-dependency-vs-realized-impact
- **downgraded_ids:**
  - foreign provider=foreign control
  - legal reach=access
  - switching cost=capture
  - outage=sabotage
  - capability=use
- **none_found_claims:**
  - US access to Health Data Hub data
  - general political tasking by hyperscalers
  - general coercive use of EU cable dependency
  - electoral effect caused by digital infrastructure dependency
- **remaining_gaps:**
  - provider-specific political command evidence
  - quantified switching-cost denominator by public-sector workload
  - decision-specific downstream effect from export-control dependency
- **verification:** 28 material facts resolve to 14 fresh FETCH sources across five provenance families; dependence, exercised constraint, adaptation and political effect remain separate.

### EDI_REPORT
- **corpus:** 14 sources / 28 facts
- **decisive_claim_coverage:**
  - CLM-001
  - CLM-003
  - CLM-004
  - CLM-006
  - CLM-008
- **diagnostic_not_truth:** true
- **dimensions:**
  - cloud market
  - jurisdiction
  - export controls
  - supply-chain dependency
  - cable resilience
- **edi:** official regulators/courts/governments/company filings plus EU strategic-risk controls
- **source_counts:**
  - **A:** 3
  - **B:** 4
  - **C:** 4
  - **D:** 2
  - **E:** 1

### RESPONSIBILITY_MAP
- **boundary:** Dependency, legal reach, regulatory control, interruption, coercion and political effect are distinct responsibility claims.
- **not_established:**
  - general foreign control of EU cloud customers
  - exercised US access to Health Data Hub
  - dependency equals capture
  - general cable incident political attribution
  - electoral effect
- **verified:**
  - cloud lock-in and switching barriers
  - extraterritorial legal capability and French governance response
  - export-license constraints on ASML
  - structural semiconductor dependencies
  - cable resilience response

### NEXT_QUERIES
- Reopen on authenticated order/refusal/access event affecting a French/EU sensitive cloud workload.
- Reopen on quantified migration or switching-cost evidence tied to a public decision or forced adaptation.
- Reopen on actor-specific export-control or supply interruption producing a documented French/EU policy concession or political outcome.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-003 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-004,QRY-005,QRY-006,QRY-007 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-008,QRY-009,QRY-010,QRY-011 | support:- | counter:- | results:FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-012,QRY-013,QRY-014 | support:- | counter:- | results:FCT-023,FCT-024,FCT-025,FCT-026,FCT-027,FCT-028 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-015,QRY-016,QRY-017,SRC-001,SRC-002,SRC-003 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006 | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-016,QRY-017,SRC-002,SRC-003 | support:FCT-003,FCT-004,FCT-005,FCT-006 | counter:- | results:FCT-003,FCT-004,FCT-005,FCT-006 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-018,QRY-020,SRC-004,SRC-006 | support:FCT-007,FCT-008,FCT-011,FCT-012 | counter:- | results:FCT-007,FCT-008,FCT-011,FCT-012 | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-019,QRY-020,SRC-005,SRC-006 | support:FCT-009,FCT-010,FCT-011,FCT-012 | counter:- | results:FCT-009,FCT-010,FCT-011,FCT-012 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-021,SRC-007 | support:FCT-013,FCT-014 | counter:- | results:FCT-013,FCT-014 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-022,QRY-023,QRY-024,QRY-025,SRC-008,SRC-009,SRC-010,SRC-011 | support:FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021 | counter:- | results:FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-026,QRY-027,SRC-012,SRC-013 | support:FCT-023,FCT-024,FCT-025,FCT-026 | counter:- | results:FCT-023,FCT-024,FCT-025,FCT-026 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-015,QRY-018,QRY-019,QRY-023,QRY-025,QRY-026,QRY-028,SRC-001,SRC-004,SRC-005,SRC-009,SRC-011,SRC-012,SRC-014 | support:FCT-001,FCT-007,FCT-023,FCT-027 | counter:FCT-002,FCT-008,FCT-010,FCT-018,FCT-022,FCT-024,FCT-028 | results:FCT-001,FCT-007,FCT-023,FCT-027,FCT-002,FCT-008,FCT-010,FCT-018,FCT-022,FCT-024,FCT-028 | final:REFUTED | gap:NONE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
NONE

SEMANTIC_COUNTS_V1:LED:0|CLM:8|AXS:4|CAU:5|CTRL:10|ACT:4

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Le cloud européen présente des dépendances de marché matérielles liées à la concentration, au lock-in et aux coûts de changement; cela réduit les options de sortie sans prouver une coercition politique exercée.","claimant":"INV-125","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006"]}
CLM-002 | {"claim":"Le Data Act constitue une réponse institutionnelle directe aux obstacles de switching et vise à réduire la dépendance à un fournisseur cloud unique.","claimant":"INV-125","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-005","FCT-006"]}
CLM-003 | {"claim":"Le CLOUD Act et autres portées juridiques extra-européennes créent une capacité légale potentielle d accès à des données sous contrôle d un fournisseur couvert; capacité ne vaut pas accès exercé.","claimant":"INV-125","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-011","FCT-012"]}
CLM-004 | {"claim":"Le cas Health Data Hub ferme une chaîne risque juridique -> précautions contractuelles/gouvernance, sans établir qu une autorité américaine a effectivement accédé aux données de santé.","claimant":"INV-125","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011","FCT-012"]}
CLM-005 | {"claim":"SecNumCloud 3.2 encode explicitement une stratégie de réduction du risque extraterritorial par gouvernance, contrôle capitalistique et localisation opérationnelle européenne.","claimant":"INV-125","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-013","FCT-014"]}
CLM-006 | {"claim":"Les contrôles export semi-conducteurs ont produit des contraintes réelles de licence et des adaptations commerciales chez ASML; ils démontrent un levier réglementaire effectif sur une entreprise européenne stratégique.","claimant":"INV-125","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"]}
CLM-007 | {"claim":"Les dépendances européennes aux fonderies asiatiques, GPU américains et segments critiques de la chaîne semi-conducteurs augmentent l exposition aux contrôles ou ruptures, mais ne constituent pas à elles seules une capture politique.","claimant":"INV-125","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-023","FCT-024","FCT-025","FCT-026"]}
CLM-008 | {"claim":"Toute dépendance étrangère ou vulnérabilité de câble prouve une coercition politique ou une ingérence exercée.","claimant":"strongest adverse hypothesis","counter":["FCT-002","FCT-008","FCT-010","FCT-018","FCT-022","FCT-024","FCT-028"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"REFUTED","support":["FCT-001","FCT-007","FCT-023","FCT-027"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003"],"axis":"cloud","links":["DMA cloud investigation","Data Act"],"question":"Quels mécanismes de lock-in et de switching rendent une dépendance cloud matériellement contraignante?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006"],"sought_objects":["market position","switching costs","egress","interoperability","multi-cloud"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-004","QRY-005","QRY-006","QRY-007"],"axis":"jurisdiction","links":["DOJ","Conseil Etat","CNIL","Senat"],"question":"Quand la portée juridique extra-européenne produit-elle une adaptation réelle de gouvernance des données?","result_ids":["FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014"],"sought_objects":["CLOUD Act","provider control","health data","contract safeguards","SecNumCloud"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-008","QRY-009","QRY-010","QRY-011"],"axis":"semiconductors","links":["Government.nl","ASML"],"question":"Quels contrôles et dépendances de chaîne de valeur modifient effectivement activité, licences ou ventes européennes?","result_ids":["FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022"],"sought_objects":["export license","US rules","Dutch rules","rare earths","sales impact"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-012","QRY-013","QRY-014"],"axis":"resilience","links":["Commission competitiveness","Economic Security Strategy","Cable toolbox"],"question":"Comment l UE traite-t-elle les dépendances numériques et physiques comme risques de coercition ou interruption?","result_ids":["FCT-023","FCT-024","FCT-025","FCT-026","FCT-027","FCT-028"],"sought_objects":["structural dependency","weaponisation","cables","stress tests","policy response"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"La Commission et le Data Act identifient explicitement lock-in, egress et interopérabilité comme obstacles.","counter":"NONE_FOUND","limit":"Réduit autonomie et pouvoir de sortie; aucune injonction politique ou décision imposée par AWS/Azure n est établie.","mechanism":"concentration cloud + coûts de switching/interoperabilité -> options de sortie réduites -> dépendance contractuelle et technique","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006"]}
CAU-002 | {"causal_right":"DOJ, Conseil d Etat, CNIL et SecNumCloud documentent le lien juridique et les mesures de mitigation.","counter":"NONE_FOUND","limit":"Le cas ferme l adaptation institutionnelle au risque, pas un accès américain effectivement exercé au Health Data Hub.","mechanism":"juridiction américaine -> fournisseur couvert -> capacité d ordre d accès -> risque données -> adaptation contractuelle/gouvernance française","status":"SUPPORTED","support":["FCT-007","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014"]}
CAU-003 | {"causal_right":"Règles néerlandaises et rapports ASML relient directement changements réglementaires et licensing/compliance.","counter":"NONE_FOUND","limit":"Contrainte réglementaire réelle; licence ne vaut pas embargo général et effet politique aval européen non identifié.","mechanism":"règle export -> obligation de licence -> limitation/conditionnement de livraisons -> adaptation commerciale ASML","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"]}
CAU-004 | {"causal_right":"La dépendance est documentée et déclenche mitigation/politique, avec un contre-fait d impact matériel nul à date.","counter":["FCT-022"],"limit":"ASML ne constatait pas d impact matériel client des restrictions terres rares au moment du rapport; dépendance et effet restent séparés.","mechanism":"dépendance matières premières/chaîne semi-conducteurs -> restrictions ou risque de rupture -> mitigation fournisseurs/industrial policy","status":"SUPPORTED","support":["FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"]}
CAU-005 | {"causal_right":"La toolbox 2026 relie incidents et vulnérabilités à des mesures concrètes de résilience.","counter":"NONE_FOUND","limit":"Les incidents incluent dommages intentionnels et non intentionnels; aucune attribution générale à une puissance ni effet politique coercitif n est démontré.","mechanism":"dépendance câbles sous-marins + incidents -> cartographie/stress tests/investissement réparation -> résilience UE","status":"SUPPORTED","support":["FCT-027","FCT-028"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Appréciation DMA cloud 2026 est préliminaire, pas décision finale ni preuve de coercition","status":"PASS","support":["FCT-001","FCT-002"]}
CTRL-002 | {"control":"Data Act traite lock-in/switching comme problème de marché et crée une sortie réglementée","status":"PASS","support":["FCT-003","FCT-004","FCT-005","FCT-006"]}
CTRL-003 | {"control":"CLOUD Act capability != exercised access","status":"PASS","support":["FCT-007","FCT-008"]}
CTRL-004 | {"control":"Health Data Hub: risque non nul mais aucun accès américain établi; précautions plutôt que suspension","status":"PASS","support":["FCT-009","FCT-010"]}
CTRL-005 | {"control":"CNIL: localisation UE != immunité juridique extraterritoriale","status":"PASS","support":["FCT-011","FCT-012"]}
CTRL-006 | {"control":"SecNumCloud démontre une mitigation institutionnelle, pas la preuve qu une injonction étrangère a eu lieu","status":"PASS","support":["FCT-013","FCT-014"]}
CTRL-007 | {"control":"Contrôles néerlandais sont ciblés par licence et sécurité, pas embargo général","status":"PASS","support":["FCT-015","FCT-016","FCT-017","FCT-018"]}
CTRL-008 | {"control":"ASML ferme effet business des export controls mais rare-earth impact client était nul à date","status":"PASS","support":["FCT-019","FCT-020","FCT-021","FCT-022"]}
CTRL-009 | {"control":"Dépendance semi-conducteurs structurelle != capture politique","status":"PASS","support":["FCT-023","FCT-024","FCT-025","FCT-026"]}
CTRL-010 | {"control":"Incidents câbles critiques != sabotage/attribution politique automatique","status":"PASS","support":["FCT-027","FCT-028"]}

### ACTION_REGISTRY_V1
ACT-001 | {"action":"Exiger pour toute qualification de coercition un point de contrainte exercé: ordre, refus, licence, interruption, accès ou coût de sortie documenté.","actor":"future investigations","intent":"dependency != coercion","status":"DONE","support":["FCT-002","FCT-008","FCT-018","FCT-024","FCT-028"]}
ACT-002 | {"action":"Séparer systématiquement portée juridique, demande d accès, accès effectif et effet aval sur décision ou comportement.","actor":"future investigations","intent":"capability != use","status":"DONE","support":["FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012"]}
ACT-003 | {"action":"Mesurer les coûts et obstacles de sortie cloud avant toute inférence de capture ou dépendance irréversible.","actor":"future investigations","intent":"switching cost != capture","status":"DONE","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006"]}
ACT-004 | {"action":"Pour semi-conducteurs et câbles, distinguer vulnérabilité, restriction réglementaire, incident, attribution et effet politique.","actor":"future investigations","intent":"éviter la fusion dépendance/attaque/ingérence","status":"DONE","support":["FCT-015","FCT-018","FCT-019","FCT-022","FCT-027","FCT-028"]}

SEARCH_ACTIVITY_V1:WEB:14|FETCH:14|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL | MNEMO | MNEMO_UNAVAILABLE | MNEMO_Q
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | WEB | PASS | - | - | EU cloud AWS Azure lock-in switching costs DMA 2026
QRY-002 | WEB | PASS | - | - | EU Data Act cloud switching barriers egress interoperability
QRY-003 | WEB | PASS | - | - | Data Act 2023/2854 switching cloud providers
QRY-004 | WEB | PASS | - | - | US CLOUD Act covered providers overseas data orders
QRY-005 | WEB | PASS | - | - | Health Data Hub Microsoft Cloud Act Conseil Etat 2020
QRY-006 | WEB | PASS | - | - | CNIL Health Data Hub Microsoft US law access risk
QRY-007 | WEB | PASS | - | - | SecNumCloud 3.2 extraterritorial laws Senate
QRY-008 | WEB | PASS | - | - | Netherlands export control DUV lithography September 2024
QRY-009 | WEB | PASS | - | - | Netherlands semiconductor metrology export controls April 2025
QRY-010 | WEB | PASS | - | - | ASML 2024 annual report US Dutch export controls licensing
QRY-011 | WEB | PASS | - | - | ASML 2025 annual report rare earth export controls business
QRY-012 | WEB | PASS | - | - | EU semiconductor dependencies Asia GPUs US Draghi report
QRY-013 | WEB | PASS | - | - | EU economic security weaponisation economic dependencies critical technologies
QRY-014 | WEB | PASS | - | - | EU submarine cable security toolbox 2026 incidents dependencies
QRY-015 | FETCH | FOUND | SRC-001 | https://digital-markets-act.ec.europa.eu/commission-reaches-preliminary-position-amazons-and-microsofts-market-leading-cloud-services-should-2026-06-25_en | https://digital-markets-act.ec.europa.eu/commission-reaches-preliminary-position-amazons-and-microsofts-market-leading-cloud-services-should-2026-06-25_en
QRY-016 | FETCH | FOUND | SRC-002 | https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained | https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained
QRY-017 | FETCH | FOUND | SRC-003 | https://eur-lex.europa.eu/eli/reg/2023/2854 | https://eur-lex.europa.eu/eli/reg/2023/2854
QRY-018 | FETCH | FOUND | SRC-004 | https://www.justice.gov/criminal/criminal-oia/regarding-cloud-act-executive-agreements | https://www.justice.gov/criminal/criminal-oia/regarding-cloud-act-executive-agreements
QRY-019 | FETCH | FOUND | SRC-005 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2020-10-13/444937 | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2020-10-13/444937
QRY-020 | FETCH | FOUND | SRC-006 | https://www.cnil.fr/fr/les-principaux-avis-et-recommandations-de-la-cnil-sur-la-plateforme-des-donnees-de-sante | https://www.cnil.fr/fr/les-principaux-avis-et-recommandations-de-la-cnil-sur-la-plateforme-des-donnees-de-sante
QRY-021 | FETCH | FOUND | SRC-007 | https://www.senat.fr/rap/l25-199/l25-1994.html | https://www.senat.fr/rap/l25-199/l25-1994.html
QRY-022 | FETCH | FOUND | SRC-008 | https://www.government.nl/latest/news/2024/09/06/the-netherlands-expands-export-control-measure-advanced-semiconductor-manufacturing-equipment | https://www.government.nl/latest/news/2024/09/06/the-netherlands-expands-export-control-measure-advanced-semiconductor-manufacturing-equipment
QRY-023 | FETCH | FOUND | SRC-009 | https://www.government.nl/latest/news/2025/01/15/klever-export-controls-on-advanced-semiconductor-manufacturing-equipment-to-be-tightened | https://www.government.nl/latest/news/2025/01/15/klever-export-controls-on-advanced-semiconductor-manufacturing-equipment-to-be-tightened
QRY-024 | FETCH | FOUND | SRC-010 | https://ourbrand.asml.com/m/3035813cf1b8ea4f/original/2024-Annual-Report-based-on-IFRS-FINAL.pdf | https://ourbrand.asml.com/m/3035813cf1b8ea4f/original/2024-Annual-Report-based-on-IFRS-FINAL.pdf
QRY-025 | FETCH | FOUND | SRC-011 | https://ourbrand.asml.com/m/6ea363f69344ebd4/original/asml-2025-annual-report-based-on-ifrs.pdf | https://ourbrand.asml.com/m/6ea363f69344ebd4/original/asml-2025-annual-report-based-on-ifrs.pdf
QRY-026 | FETCH | FOUND | SRC-012 | https://commission.europa.eu/document/download/ec1409c1-d4b4-4882-8bdd-3519f86bbb92_en?filename=The+future+of+European+competitiveness_+In-depth+analysis+and+recommendations_0.pdf | https://commission.europa.eu/document/download/ec1409c1-d4b4-4882-8bdd-3519f86bbb92_en?filename=The+future+of+European+competitiveness_+In-depth+analysis+and+recommendations_0.pdf
QRY-027 | FETCH | FOUND | SRC-013 | https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/story-von-der-leyen-commission/investing-europes-prosperity_en | https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/story-von-der-leyen-commission/investing-europes-prosperity_en
QRY-028 | FETCH | FOUND | SRC-014 | https://digital-strategy.ec.europa.eu/en/library/submarine-cable-security-toolbox-and-cable-projects-european-interest | https://digital-strategy.ec.europa.eu/en/library/submarine-cable-security-toolbox-and-cable-projects-european-interest

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | European Commission DMA cloud preliminary view | European Commission DMA cloud preliminary view | 2026-06-25 | 2026-09-09T20:12:00Z | AWS/Azure preliminary gatekeeper assessment; lock-in and switching costs | https://digital-markets-act.ec.europa.eu/commission-reaches-preliminary-position-amazons-and-microsofts-market-leading-cloud-services-should-2026-06-25_en
SRC-002 | ◈ | fam:A | European Commission Data Act explained | European Commission Data Act explained | 2025-12-01 | 2026-09-09T20:12:00Z | Cloud switching barriers, contractual transparency and egress charges | https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained
SRC-003 | ◈ | fam:A | EU Data Act Regulation 2023/2854 | EU Data Act Regulation 2023/2854 | 2023-12-13 | 2026-09-09T20:12:00Z | Binding switching, interoperability and portability framework | https://eur-lex.europa.eu/eli/reg/2023/2854
SRC-004 | ◈ | fam:B | US Department of Justice CLOUD Act overview | US Department of Justice CLOUD Act overview | 2023-09-29 | 2026-09-09T20:12:00Z | Legal mechanism for cross-border orders to covered providers | https://www.justice.gov/criminal/criminal-oia/regarding-cloud-act-executive-agreements
SRC-005 | ◈ | fam:B | Conseil d Etat Health Data Hub 444937 | Conseil d Etat Health Data Hub 444937 | 2020-10-13 | 2026-09-09T20:12:00Z | Microsoft Azure contract, third-country access risk and contractual precautions | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2020-10-13/444937
SRC-006 | ◈ | fam:B | CNIL Health Data Hub recommendations | CNIL Health Data Hub recommendations | 2024-01-01 | 2026-09-09T20:12:00Z | US-law access risk despite EU storage; recommendation trajectory | https://www.cnil.fr/fr/les-principaux-avis-et-recommandations-de-la-cnil-sur-la-plateforme-des-donnees-de-sante
SRC-007 | ◈ | fam:B | French Senate SecNumCloud extraterritorial protection | French Senate SecNumCloud extraterritorial protection | 2025-12-01 | 2026-09-09T20:12:00Z | SecNumCloud 3.2 legal, technical and governance protections against extraterritorial laws | https://www.senat.fr/rap/l25-199/l25-1994.html
SRC-008 | ◈ | fam:C | Netherlands semiconductor export controls September 2024 | Netherlands semiconductor export controls September 2024 | 2024-09-06 | 2026-09-09T20:12:00Z | National licensing expanded for advanced semiconductor manufacturing equipment | https://www.government.nl/latest/news/2024/09/06/the-netherlands-expands-export-control-measure-advanced-semiconductor-manufacturing-equipment
SRC-009 | ◈ | fam:C | Netherlands semiconductor export controls April 2025 | Netherlands semiconductor export controls April 2025 | 2025-01-15 | 2026-09-09T20:12:00Z | Additional metrology and inspection technologies subject to authorization | https://www.government.nl/latest/news/2025/01/15/klever-export-controls-on-advanced-semiconductor-manufacturing-equipment-to-be-tightened
SRC-010 | ◈ | fam:C | ASML 2024 Annual Report | ASML 2024 Annual Report | 2025-02-12 | 2026-09-09T20:12:00Z | Dutch and US export controls and licensing effects on ASML | https://ourbrand.asml.com/m/3035813cf1b8ea4f/original/2024-Annual-Report-based-on-IFRS-FINAL.pdf
SRC-011 | ◈ | fam:C | ASML 2025 Annual Report | ASML 2025 Annual Report | 2026-02-25 | 2026-09-09T20:12:00Z | Export controls and China rare-earth restrictions; business mitigation | https://ourbrand.asml.com/m/6ea363f69344ebd4/original/asml-2025-annual-report-based-on-ifrs.pdf
SRC-012 | ◈ | fam:D | European Commission future competitiveness semiconductor dependencies | European Commission future competitiveness semiconductor dependencies | 2024-09-09 | 2026-09-09T20:12:00Z | EU semiconductor, GPU, fabrication and third-country dependencies | https://commission.europa.eu/document/download/ec1409c1-d4b4-4882-8bdd-3519f86bbb92_en?filename=The+future+of+European+competitiveness_+In-depth+analysis+and+recommendations_0.pdf
SRC-013 | ◈ | fam:D | European Commission economic security strategy risks | European Commission economic security strategy risks | 2024-01-24 | 2026-09-09T20:12:00Z | Risk categories include weaponisation of economic dependencies and critical technologies | https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/story-von-der-leyen-commission/investing-europes-prosperity_en
SRC-014 | ◈ | fam:E | EU Submarine Cable Security Toolbox 2026 | EU Submarine Cable Security Toolbox 2026 | 2026-02-05 | 2026-09-09T20:12:00Z | Cable incidents, risk scenarios, resilience toolbox and prioritized projects | https://digital-strategy.ec.europa.eu/en/library/submarine-cable-security-toolbox-and-cable-projects-european-interest

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://digital-markets-act.ec.europa.eu/commission-reaches-preliminary-position-amazons-and-microsofts-market-leading-cloud-services-should-2026-06-25_en | A | 2026-09-09 | Cloud market concentration | La Commission a estimé à titre préliminaire en juin 2026 que AWS et Azure sont respectivement les premier et deuxième services cloud de l UE et des passerelles importantes pour les entreprises européennes. | -
FCT-002 | FACT | ✧ | https://digital-markets-act.ec.europa.eu/commission-reaches-preliminary-position-amazons-and-microsofts-market-leading-cloud-services-should-2026-06-25_en | A | 2026-09-09 | Cloud lock-in | La même appréciation préliminaire relève des bases utilisateurs enracinées, des effets de verrouillage, des coûts élevés de changement et de larges écosystèmes; cela documente une dépendance de marché, pas une coercition politique exercée. | -
FCT-003 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained | A | 2026-09-09 | Switching barriers | La Commission décrit comme obstacles actuels au changement de cloud les frais de sortie de données, les procédures longues et le manque d interopérabilité pouvant entraîner perte de données ou de fonctionnalités. | -
FCT-004 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained | A | 2026-09-09 | Data Act mitigation | Le Data Act impose transparence contractuelle, interfaces et facilitation du changement; les frais de switching et de data egress doivent disparaître entièrement à compter du 12 janvier 2027. | -
FCT-005 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2023/2854 | A | 2026-09-09 | Binding portability | Le règlement 2023/2854 oblige les fournisseurs à faciliter le changement de service et, selon les cas, à fournir interfaces ouvertes, assistance, export dans un format lisible par machine et équivalence fonctionnelle raisonnable. | -
FCT-006 | FACT | ✧ | https://eur-lex.europa.eu/eli/reg/2023/2854 | A | 2026-09-09 | Multi-cloud objective | Le Data Act présente l interopérabilité et le multi-cloud comme moyens de réduire la dépendance à un fournisseur unique; il reconnaît donc le lock-in comme risque structurel sans présumer qu il soit utilisé comme levier politique. | -
FCT-007 | FACT | ✧ | https://www.justice.gov/criminal/criminal-oia/regarding-cloud-act-executive-agreements | B | 2026-09-09 | CLOUD Act mechanism | Le CLOUD Act permet des accords exécutifs facilitant des ordres légaux transfrontaliers visant des données détenues par des fournisseurs couverts de communications ou de traitement/stockage. | -
FCT-008 | FACT | ✧ | https://www.justice.gov/criminal/criminal-oia/regarding-cloud-act-executive-agreements | B | 2026-09-09 | Legal reach boundary | L existence de cette compétence juridique crée une capacité d accès sous conditions légales; elle ne prouve ni demande visant un acteur français donné ni accès effectivement exercé à une donnée déterminée. | -
FCT-009 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2020-10-13/444937 | B | 2026-09-09 | Health Data Hub contract | Le Health Data Hub a contracté avec Microsoft Ireland pour Azure; le Conseil d Etat a constaté que Microsoft relève d un groupe américain et qu un risque de demande d accès par autorités américaines ne pouvait être totalement exclu. | -
FCT-010 | FACT | ✧ | https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2020-10-13/444937 | B | 2026-09-09 | Health Data Hub effect | Le Conseil d Etat n a pas suspendu la plateforme mais a ordonné des précautions contractuelles supplémentaires et retenu une solution pérenne visant à éliminer le risque; la portée juridique a donc produit une adaptation de gouvernance, non une preuve d accès américain. | -
FCT-011 | FACT | ✧ | https://www.cnil.fr/fr/les-principaux-avis-et-recommandations-de-la-cnil-sur-la-plateforme-des-donnees-de-sante | B | 2026-09-09 | CNIL third-country risk | La CNIL souligne que l hébergeur Microsoft Ireland appartient à un groupe dont la société mère américaine est soumise au droit des Etats-Unis, ce qui implique une possibilité légale de demandes de communication. | -
FCT-012 | FACT | ✧ | https://www.cnil.fr/fr/les-principaux-avis-et-recommandations-de-la-cnil-sur-la-plateforme-des-donnees-de-sante | B | 2026-09-09 | Storage not immunity | La localisation des données en France ou dans l UE ne suffit donc pas, à elle seule, à neutraliser toute portée juridique extraterritoriale; la CNIL distingue stockage territorial et risque juridique. | -
FCT-013 | FACT | ✧ | https://www.senat.fr/rap/l25-199/l25-1994.html | B | 2026-09-09 | SecNumCloud protection design | Le rapport du Sénat décrit SecNumCloud 3.2 comme visant la protection contre les lois extraterritoriales par une combinaison de mesures techniques, organisationnelles et juridiques. | -
FCT-014 | FACT | ✧ | https://www.senat.fr/rap/l25-199/l25-1994.html | B | 2026-09-09 | SecNumCloud governance thresholds | Le rapport indique notamment siège dans l UE, plafonds de participation non européenne et majorité des activités d administration/maintenance en Europe; cette architecture constitue une réponse institutionnelle au risque de contrôle juridique externe. | -
FCT-015 | FACT | ✧ | https://www.government.nl/latest/news/2024/09/06/the-netherlands-expands-export-control-measure-advanced-semiconductor-manufacturing-equipment | C | 2026-09-09 | Dutch export control 2024 | Depuis septembre 2024 les Pays-Bas ont étendu l obligation d autorisation à davantage d équipements avancés de fabrication de semi-conducteurs, notamment certains systèmes DUV. | -
FCT-016 | FACT | ✧ | https://www.government.nl/latest/news/2024/09/06/the-netherlands-expands-export-control-measure-advanced-semiconductor-manufacturing-equipment | C | 2026-09-09 | Security rationale | Le gouvernement néerlandais motive cette mesure par des risques de sécurité liés aux avancées technologiques et au contexte géopolitique; une position technologique stratégique devient ainsi un point de contrôle réglementaire explicite. | -
FCT-017 | FACT | ✧ | https://www.government.nl/latest/news/2025/01/15/klever-export-controls-on-advanced-semiconductor-manufacturing-equipment-to-be-tightened | C | 2026-09-09 | Dutch export control 2025 | A compter du 1er avril 2025 les Pays-Bas ont encore étendu la licence à des technologies spécifiques de mesure et inspection utilisées pour les semi-conducteurs avancés. | -
FCT-018 | FACT | ✧ | https://www.government.nl/latest/news/2025/01/15/klever-export-controls-on-advanced-semiconductor-manufacturing-equipment-to-be-tightened | C | 2026-09-09 | Authorization not embargo | Le mécanisme est une obligation d autorisation ciblée et non une interdiction générale; contrôle réglementaire, refus éventuel et coercition doivent rester distingués. | -
FCT-019 | FACT | ✧ | https://ourbrand.asml.com/m/3035813cf1b8ea4f/original/2024-Annual-Report-based-on-IFRS-FINAL.pdf | C | 2026-09-09 | ASML licensing shift | ASML indique qu après la règle néerlandaise du 7 septembre 2024 certains systèmes DUV NXT:1970i et 1980i nécessitent une licence néerlandaise plutôt qu américaine, en cohérence avec les règles US. | -
FCT-020 | FACT | ✧ | https://ourbrand.asml.com/m/3035813cf1b8ea4f/original/2024-Annual-Report-based-on-IFRS-FINAL.pdf | C | 2026-09-09 | US rule business constraint | ASML rapporte aussi l élargissement en décembre 2024 des restrictions américaines à des technologies, logiciels et sites supplémentaires; l entreprise adapte livraisons et conformité, ce qui ferme une chaîne règle étrangère/nationale -> licence -> activité commerciale. | -
FCT-021 | FACT | ✧ | https://ourbrand.asml.com/m/6ea363f69344ebd4/original/asml-2025-annual-report-based-on-ifrs.pdf | C | 2026-09-09 | Export controls business impact | ASML indique en 2025 que les changements de contrôles à l exportation peuvent affecter matériellement volume, mix et calendrier des ventes; cela documente un effet économique réel, sans établir un effet politique aval en Europe. | -
FCT-022 | FACT | ✧ | https://ourbrand.asml.com/m/6ea363f69344ebd4/original/asml-2025-annual-report-based-on-ifrs.pdf | C | 2026-09-09 | Rare earth dependency response | ASML rapporte des restrictions chinoises 2025 sur certaines terres rares et technologies, une préparation depuis 2024 autour notamment des aimants et des plans de mitigation; aucun impact matériel client n était observé à la date du rapport. | -
FCT-023 | FACT | ✧ | https://commission.europa.eu/document/download/ec1409c1-d4b4-4882-8bdd-3519f86bbb92_en?filename=The+future+of+European+competitiveness_+In-depth+analysis+and+recommendations_0.pdf | D | 2026-09-09 | EU semiconductor dependency | Le rapport de compétitivité de la Commission décrit une forte dépendance européenne hors UE pour les semi-conducteurs: absence de fonderie sous 22 nm, 75 à 90 % de capacité de fabrication de wafers en Asie et dépendance aux GPU avancés américains. | -
FCT-024 | FACT | ✧ | https://commission.europa.eu/document/download/ec1409c1-d4b4-4882-8bdd-3519f86bbb92_en?filename=The+future+of+European+competitiveness_+In-depth+analysis+and+recommendations_0.pdf | D | 2026-09-09 | Dependency not capture | Ces dépendances sont structurelles et concentrées par segments de chaîne de valeur; elles augmentent l exposition à ruptures ou contrôles mais ne constituent pas par elles-mêmes une preuve de coercition ou capture. | -
FCT-025 | FACT | ✧ | https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/story-von-der-leyen-commission/investing-europes-prosperity_en | D | 2026-09-09 | Weaponisation risk category | La stratégie européenne de sécurité économique classe explicitement la weaponisation des dépendances économiques et la coercition économique parmi ses catégories de risque. | -
FCT-026 | FACT | ✧ | https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/story-von-der-leyen-commission/investing-europes-prosperity_en | D | 2026-09-09 | EU policy response | L UE a ciblé pour évaluation renforcée les semi-conducteurs avancés, IA, quantique et biotechnologies et développé contrôle export, filtrage investissement et sécurité des chaînes; l adaptation politique confirme la matérialité du risque sans prouver chaque scénario. | -
FCT-027 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/library/submarine-cable-security-toolbox-and-cable-projects-european-interest | E | 2026-09-09 | Cable criticality | La Commission rappelle que les câbles sous-marins transportent 99 % du trafic internet intercontinental et que plusieurs incidents récents ont exposé leur criticité et vulnérabilité. | -
FCT-028 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/library/submarine-cable-security-toolbox-and-cable-projects-european-interest | E | 2026-09-09 | Cable resilience response | Le plan 2025 et la toolbox 2026 couvrent prévention, détection, réponse, réparation et dissuasion, avec cartographie, stress tests et projets prioritaires; ces mesures attestent une dépendance critique et une réponse de résilience, pas l attribution automatique des incidents à une action politique étrangère. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-002
FCT-004 | SRC-002
FCT-005 | SRC-003
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-004
FCT-009 | SRC-005
FCT-010 | SRC-005
FCT-011 | SRC-006
FCT-012 | SRC-006
FCT-013 | SRC-007
FCT-014 | SRC-007
FCT-015 | SRC-008
FCT-016 | SRC-008
FCT-017 | SRC-009
FCT-018 | SRC-009
FCT-019 | SRC-010
FCT-020 | SRC-010
FCT-021 | SRC-011
FCT-022 | SRC-011
FCT-023 | SRC-012
FCT-024 | SRC-012
FCT-025 | SRC-013
FCT-026 | SRC-013
FCT-027 | SRC-014
FCT-028 | SRC-014

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
FCT-023 | ELIGIBLE:VERIFIE
FCT-024 | ELIGIBLE:VERIFIE
FCT-025 | ELIGIBLE:VERIFIE
FCT-026 | ELIGIBLE:VERIFIE
FCT-027 | ELIGIBLE:VERIFIE
FCT-028 | ELIGIBLE:VERIFIE

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
FCT-023 | WRITE | -
FCT-024 | WRITE | -
FCT-025 | WRITE | -
FCT-026 | WRITE | -
FCT-027 | WRITE | -
FCT-028 | WRITE | -

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:search
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:facts
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:causal
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:verify
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:accountability
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:finalize

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-09T20:20:03.409556+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-027","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-028","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":28,"eligible":28,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:28;attempted:0;success:0;failure:0;blocked:28} | WRITEBACK_EXECUTION_V1:[28 rows, see section]

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
FCT-023 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-024 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-025 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-026 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-027 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
FCT-028 | ELIGIBLE:VERIFIE | attempted:0 | success:0 | failure:0 | blocked:1 | reason:MNEMO_UNAVAILABLE
