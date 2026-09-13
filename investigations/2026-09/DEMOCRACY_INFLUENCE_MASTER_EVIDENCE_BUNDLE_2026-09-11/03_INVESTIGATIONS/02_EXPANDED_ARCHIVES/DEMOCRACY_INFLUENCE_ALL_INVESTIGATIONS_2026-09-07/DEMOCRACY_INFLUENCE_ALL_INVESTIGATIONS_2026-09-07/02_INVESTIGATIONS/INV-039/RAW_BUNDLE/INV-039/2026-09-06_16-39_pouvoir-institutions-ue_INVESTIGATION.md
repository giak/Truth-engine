ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-1639-pouvoir-institutions-ue | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth-engine/investigations/2026-09/2026-09-06_pouvoir-institutions-ue/2026-09-06_16-39_pouvoir-institutions-ue_INPUT.md | SUBJECT_SLUG:pouvoir-institutions-ue | SUBJECT_FP:sha256:11ee526208d6b5475e3f447abafd5835732874ef26fd9d079870678f3c80f4ad | INPUT_SHA256:sha256:587a77b12e931cd4310d83d06110705744826db2186d4c8b1da0f16fa25510a6
COMPLEXITY:8→COMPLEX | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['European Commission', 'European Council', 'Council of the European Union', 'European Parliament', 'Court of Justice of the European Union', 'European Central Bank', 'Member States', 'interest representatives/lobbies'], 'domains': ['legislative initiative', 'ordinary and special legislation', 'budget', 'treaty revision', 'implementation/enforcement', 'monetary policy', 'judicial review', 'lobbying/access'], 'geo': 'European Union / Member States', 'lead_question': 'map real power by decision type rather than produce one global institutional ranking', 'limits': ['formal authority != agenda power != veto != implementation != access != causal control', 'do not infer capture from lobbying access', 'do not treat Member States as having individual veto under QMV', 'do not treat European Council political mandates as formal legislation'], 'object_question': "Selon le type de décision, qui dispose réellement de quels pouvoirs dans l'Union européenne entre Commission, Conseil européen, Conseil de l'UE, Parlement, CJUE, BCE et États membres, et où l'accès des lobbies peut-il influer sans être confondu avec une autorité formelle ou un contrôle de résultat ?", 'period': '2010-2026; current treaty architecture prioritized'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-039 — Qui exerce réellement le pouvoir dans l’Union européenne ?

## Question et résultat central

La question « qui exerce réellement le pouvoir dans l’UE ? » devient trompeuse dès qu’elle suppose qu’un acteur unique pourrait être classé au-dessus de tous les autres sur une même échelle. Le corpus vérifié conduit à une conclusion différente : **le pouvoir européen est distribué par domaine, base juridique et phase de décision**. Les compétences constitutionnelles, l’initiative, l’adoption, le veto, l’exécution, l’enforcement, le budget, la monnaie, le contrôle juridictionnel et l’accès d’influence ne sont pas détenus par le même acteur et ne sont pas interchangeables (`CLM-001`).

Cette conclusion ne dilue pas le pouvoir ; elle le localise. Elle permet aussi de réfuter plusieurs récits symétriquement excessifs : « la Commission gouverne seule », « chaque État peut bloquer l’UE », « le Conseil européen ne compte pas puisqu’il ne légifère pas », « le Parlement contrôle le budget », ou « les lobbies contrôlent la décision parce qu’ils ont accès aux institutions ».

## 1. Les États membres restent les constituants, pas des veto players universels

Le principe d’attribution fixe la frontière constitutionnelle : l’Union n’agit que dans les compétences qui lui ont été conférées par les États membres et les compétences non attribuées restent aux États (`FCT-005`). La révision ordinaire des traités confirme cette position en amont : plusieurs acteurs peuvent proposer une révision, mais les modifications sont arrêtées d’un commun accord entre gouvernements et n’entrent en vigueur qu’après ratification par tous les États membres selon leurs règles constitutionnelles (`FCT-006`).

Cela donne aux États une position de **principaux constitutionnels**. Mais cette position ne doit pas être extrapolée en droit de veto général sur la production législative ordinaire. Le Conseil adopte environ 80 % de la législation à la majorité qualifiée ; la règle standard exige au moins 55 % des États représentant au moins 65 % de la population (`FCT-007`). À l’inverse, l’unanimité subsiste dans des matières explicitement sensibles comme de larges pans de la PESC, la fiscalité indirecte, les ressources propres, le cadre financier pluriannuel ou certaines dispositions de justice, police et protection sociale (`FCT-008`).

La proposition correcte est donc double : **les États maîtrisent collectivement des frontières constitutionnelles décisives et conservent des veto dans certains domaines, mais un État isolé ne possède pas un veto général sur la législation européenne** (`CLM-002`, `CTRL-002`).

## 2. La Commission domine l’initiative ordinaire, pas l’adoption finale

Le traité attribue à la Commission un ensemble de leviers structurels : initiative, surveillance de l’application des traités et du droit de l’Union, exécution budgétaire, gestion de programmes et fonctions exécutives ou de coordination (`FCT-004`). La Commission décrit elle-même son droit d’initiative comme la responsabilité de planifier, préparer et proposer de nouvelles législations, tout en pouvant répondre aux demandes du Conseil européen, du Conseil, du Parlement ou à certaines initiatives citoyennes (`FCT-010`).

Cette position constitue un avantage d’agenda réel : définir la proposition initiale, son calendrier, son architecture et son évaluation prépare le terrain sur lequel les autres institutions négocient. Mais **initiative n’est pas adoption**. Dans la procédure législative ordinaire, Parlement et Conseil adoptent conjointement et sur un pied d’égalité à partir de la proposition de la Commission (`FCT-009`). La Commission ne peut donc pas être décrite comme législateur unilatéral (`CLM-004`).

Même après l’adoption, ses pouvoirs restent distribués. Les États membres portent la responsabilité première de la mise en œuvre. La Commission peut recevoir des pouvoirs d’exécution afin d’assurer des conditions uniformes, mais les États interviennent souvent via la comitologie. Les actes délégués ne peuvent modifier les éléments essentiels de la loi, et Parlement comme Conseil peuvent révoquer la délégation ou s’opposer aux actes (`FCT-011`). Enfin, la Commission peut engager des procédures d’infraction et saisir la CJUE lorsqu’un État n’applique pas le droit de l’Union (`FCT-016`).

Le résultat est un profil de pouvoir spécifique : **forte capacité d’initiative, d’exécution et d’enforcement, mais dépendance structurelle aux co-législateurs et aux bornes prévues par les traités et les actes de base**.

## 3. Parlement et Conseil : égalité dans la procédure ordinaire, asymétrie selon les matières

Le Parlement et le Conseil exercent conjointement les fonctions législative et budgétaire prévues par les traités (`FCT-001`, `FCT-003`). Dans la procédure ordinaire, aucun des deux ne peut normalement imposer seul le texte : les deux doivent parvenir à un texte identique (`FCT-009`). Cette symétrie formelle est un fait central souvent effacé par les récits qui réduisent l’UE soit à la Commission, soit aux gouvernements.

Mais cette égalité n’est pas universelle. Les procédures spéciales et les matières soumises à unanimité redonnent au Conseil et donc aux gouvernements un levier plus fort. Les règles de majorité qualifiée produisent également un pouvoir de coalition plutôt qu’un veto individuel (`FCT-007`, `FCT-008`). `CLM-005` doit donc être lu comme une règle conditionnelle : **Parlement et Conseil sont co-législateurs égaux en procédure ordinaire ; les équilibres changent lorsque le traité prévoit une autre procédure**.

## 4. Conseil européen : non-législateur en droit, acteur d’agenda en pratique

Le cas du Conseil européen montre pourquoi il faut distinguer pouvoir formel et pouvoir de fait. L’article 15 lui confie l’impulsion et la définition des orientations et priorités politiques générales, tout en précisant qu’il n’exerce pas de fonction législative (`FCT-002`). Le qualifier de « législateur » serait donc juridiquement faux.

Mais conclure à son insignifiance serait également faux. Une étude CEPS portant sur la législation relevant de la procédure ordinaire depuis 1999 rapporte que les conclusions du Conseil européen mentionnent environ 20 % des textes, avec une présence particulièrement élevée pour les dossiers de crise, redistributifs ou élargissant les compétences ; l’étude décrit également des mandats politiques adressés aux autres institutions à différentes phases (`FCT-019`).

Le contrôle `CTRL-001` ferme les deux erreurs : **le Conseil européen n’est pas le législateur formel, mais il peut exercer une capacité politique importante d’agenda, d’accélération et de sortie d’impasse** (`CLM-003`). La limite est causale : le corpus permet d’établir l’intervention systématique et sa sélection de dossiers, pas de mesurer de façon générale le contrefactuel « sans intervention du Conseil européen, cette loi aurait-elle été différente, retardée ou abandonnée ? » (`CAU-002`).

## 5. Le budget montre qu’il n’existe pas un seul « pouvoir financier européen »

Le budget annuel est déjà une chaîne distribuée : la Commission prépare le projet, tandis que Parlement et Conseil partagent le pouvoir d’adopter le budget annuel (`FCT-012`). Mais le cadre financier pluriannuel suit un autre régime : le Conseil doit l’adopter à l’unanimité après approbation du Parlement. Les ressources propres exigent à leur tour unanimité puis ratification par tous les États membres selon leurs règles constitutionnelles (`FCT-013`).

La même étiquette « budget » recouvre donc au moins trois architectures décisionnelles distinctes (`CLM-006`, `CTRL-003`). Affirmer que « le Parlement contrôle le budget », « la Commission contrôle l’argent » ou « les États contrôlent tout le budget » sans préciser le niveau considéré est insuffisant.

## 6. BCE et CJUE : des centres de pouvoir forts mais spécialisés

La BCE constitue un cas d’autonomie institutionnelle élevée : le principe d’indépendance interdit à la BCE, aux banques centrales nationales et à leurs décideurs de solliciter ou accepter des instructions des institutions européennes, des gouvernements nationaux ou d’autres organismes ; ces acteurs doivent réciproquement s’abstenir de chercher à les influencer (`FCT-014`). Cela en fait un centre de pouvoir particulièrement autonome dans son domaine monétaire, mais **pas un gouvernement général de l’Union** (`CLM-007`).

La CJUE dispose d’un autre type de pouvoir : elle interprète et fait respecter le droit de l’Union, contrôle la légalité des actes européens, veille au respect du droit par les États et les institutions et répond aux questions préjudicielles des juridictions nationales (`FCT-015`). La Commission peut en outre lui transmettre des infractions, avec possibilité de sanctions financières dans les cas prévus (`FCT-016`). Il s’agit d’un pouvoir de contrainte juridique et constitutionnelle, distinct de l’initiative politique ou de l’adoption législative (`CLM-008`).

## 7. Lobbies : accès et tentative d’influence sont documentés ; le contrôle du résultat ne l’est pas

Le registre de transparence définit explicitement les représentants d’intérêts comme des acteurs cherchant à influencer la formulation ou la mise en œuvre des politiques, la législation ou les processus décisionnels européens, et renseigne les intérêts et ressources mobilisés (`FCT-017`). L’existence organisée du lobbying n’est donc pas conjecturale.

Mais le registre ne mesure pas l’effet causal de cette activité. L’audit de la Cour des comptes européenne relève par ailleurs des lacunes de transparence et de données, notamment sur certaines réunions et données historiques (`FCT-018`). Deux conclusions doivent rester simultanément vraies : l’absence d’une interaction enregistrée ne prouve pas l’absence de lobbying ; la présence d’une interaction enregistrée ne prouve pas la capture ni que le texte final lui est causalement attribuable (`CTRL-004`).

`CLM-009` reste donc partiel par construction. Le mécanisme `CAU-001` ne peut être promu sans une analyse reliant positions défendues, amendements, chronologie, texte adopté et comparaison crédible avec un contrefactuel. Ce travail relève principalement d’INV-042 ou de cas ciblés.

## 8. Carte synthétique du pouvoir par type de décision

| Objet | Acteur(s) dominants ou nécessaires | Limite principale |
|---|---|---|
| Frontière des compétences | États membres via traités | compétences déjà transférées s’exercent selon les procédures de l’UE |
| Révision ordinaire des traités | États membres + procédure interinstitutionnelle | ratification de tous les États requise |
| Initiative législative ordinaire | Commission | proposition ≠ adoption |
| Adoption législative ordinaire | Parlement + Conseil | Conseil vote souvent à majorité qualifiée |
| Domaines sensibles à unanimité | Gouvernements au Conseil | champ défini par les traités, pas veto universel |
| Orientation stratégique/crise | Conseil européen | pas de fonction législative formelle |
| Mise en œuvre | États membres en premier lieu ; Commission si pouvoirs conférés | comitologie et contrôles des co-législateurs |
| Enforcement du droit de l’UE | Commission + CJUE | procédure et contrôle juridictionnel |
| Budget annuel | Commission propose ; Parlement + Conseil adoptent | procédure annuelle spécifique |
| MFF / ressources propres | Conseil/États avec rôles du Parlement et ratifications nationales | unanimité / ratification selon objet |
| Politique monétaire euro | BCE/Eurosystème | mandat spécialisé et indépendance de traité |
| Interprétation/légalité du droit | CJUE | pouvoir juridictionnel, pas agenda législatif général |
| Lobbying | représentants d’intérêts disposent de canaux d’accès | accès ≠ contrôle causal du résultat |

## Conclusion

INV-039 ne trouve pas une « institution qui gouverne réellement l’Europe » ; elle montre pourquoi cette formulation agrège abusivement des pouvoirs de nature différente. Le modèle le plus fidèle est un **système polycentrique et procédural**, dans lequel plusieurs acteurs peuvent être décisifs, mais sur des dimensions différentes : les États aux frontières constitutionnelles et dans les champs à unanimité ; la Commission à l’initiative et dans une partie de l’exécution/enforcement ; Parlement et Conseil dans l’adoption ordinaire ; le Conseil européen dans l’impulsion et certains arbitrages politiques ; la BCE dans la monnaie ; la CJUE dans la contrainte juridictionnelle.

Cette distribution n’implique ni équilibre parfait ni absence d’asymétries. Elle impose simplement la discipline analytique suivante : **avant de parler de pouvoir, préciser le domaine, la procédure, la phase, le type de levier et le niveau de preuve**. Les seules extensions encore matériellement ouvertes concernent des effets causaux ciblés : combien les mandats du Conseil européen modifient effectivement les trajectoires législatives (`CAU-002`) et dans quelle mesure les activités de lobbying modifient les décisions finales (`CAU-001`). Ni l’une ni l’autre ne peut être résolue honnêtement par une accumulation générique de sources descriptives.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:5|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-06
- **material_changes:**
  - 2026 Council voting/MFF procedural state
  - recent CEPS empirical mapping of European Council legislative intervention
- **measurement_focus:** current Treaty architecture and 2026 voting/budget rules; CEPS empirical study covers OLP since 1999
- **period:** 2010-2026
- **refresh_rule:** recheck after Treaty/procedure reform or new causal evidence on lobbying/European Council file effects

### MANIPULATION_REPORT
- **assumptions:**
  - power must be disaggregated by procedure/domain
  - formal Treaty text does not exhaust de facto agenda power
  - access evidence is insufficient for capture
- **clusters:**
  - NONE
- **complexity:**
  - **band:** COMPLEX
  - **score:** 8
- **implicit:**
  - initiative != unilateral adoption
  - state representation != general veto
  - political mandate != formal legislation
  - access != outcome control
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - competence mapping
  - veto-rule analysis
  - formal/de-facto comparison
  - causal-boundary enforcement
- **priorities:**
  - Treaties/institutional rules
  - current voting/budget procedure
  - independent European Council empirical control
  - independent lobbying audit
- **query_guidance:**
  - prefer primary rules for formal power
  - independent evidence for de facto claims
  - retain causal gaps
- **rhetorical:**
  - NONE
- **speaker:** N/A(TOPIC)
- **symbol_stage:** FINAL
- **symbols:**
  - **M:** 0
  - **Κ:** 0
  - **Λ:** 4
  - **Ξ:** 2
  - **Σ:** 0
  - **Φ:** 0
  - **Ψ:** 0
  - **Ω:** 0
  - **κ:** 0
  - **ρ:** 1
  - **€:** 1
  - **↕:** 5
  - **⏰:** 2
  - **⚔:** 0
  - **⫸:** 4
- **threats:**
  - NONE

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **geo:** European Union / Member States
- **measurement_contract:**
  - No global ranking without naming the decision class.
  - Separate formal authority, initiative, veto, implementation, enforcement, monetary/judicial power and access.
  - Treat lobbying as attempted influence absent causal outcome evidence.
  - Use official rules for formal claims and independent evidence for de facto claims.
- **object:** Procedure-specific distribution of formal and de facto power among EU institutions, Member States and lobbying channels.
- **period:** 2010-2026; current architecture prioritized
- **priority_tests:**
  - competence/treaty boundary
  - OLP/QMV versus unanimity
  - Commission initiative versus adoption
  - European Council formal limit versus de facto intervention
  - annual budget versus MFF/own resources
  - ECB/CJEU specialized authority
  - lobbying access versus capture

### CREDO
- No global power ranking without specifying decision type.
- Formal authority is distinct from agenda power.
- Agenda power is distinct from adoption and veto.
- Implementation/enforcement are separate from legislation.
- Access is not capture.
- Treaty, monetary and judicial powers are domain-specific.

### COGNITIVE_MAP
- **causal_boundary:** formal authority != agenda-setting != veto != implementation != access != causal control of outcomes
- **core_model:** EU power is procedure-dependent and domain-segmented; no actor has stable supremacy across competence, agenda, legislation, implementation, budget, monetary policy, judicial review and lobbying access.
- **observed_structure:**
  - Member States: competence-conferral/treaty ratification
  - Commission: default initiative plus executive/enforcement
  - Parliament+Council: OLP co-legislation
  - European Council: non-legislative formal role plus material political agenda intervention
  - ECB/CJEU: strong specialized powers
  - lobbying: attempted influence/access, not demonstrated outcome control
- **rival_models:**
  - Commission alone governs EU
  - each state has general veto
  - European Council is merely ceremonial
  - European Council is formal legislature
  - one actor controls all budget authority
  - lobbying access proves capture

### DIALECTICAL_MAP
- **item 1:**
  - **evidence:**
    - CLM-002
    - CTRL-002
  - **hypothesis:** Member States each retain a general veto over EU legislation
  - **result:** CONTRADICTED
- **item 2:**
  - **evidence:**
    - CLM-004
    - CLM-005
  - **hypothesis:** Commission can normally enact EU law alone because it proposes it
  - **result:** CONTRADICTED
- **item 3:**
  - **evidence:**
    - CLM-003
    - CTRL-001
    - CAU-002
  - **hypothesis:** European Council is irrelevant because it cannot legislate
  - **result:** CONTRADICTED_IN_PRACTICE_CAUSAL_MAGNITUDE_UNRESOLVED
- **item 4:**
  - **evidence:**
    - CLM-006
    - CTRL-003
  - **hypothesis:** One institution controls the whole EU budget architecture
  - **result:** CONTRADICTED
- **item 5:**
  - **evidence:**
    - CLM-009
    - CAU-001
    - CTRL-004
  - **hypothesis:** Lobbying access establishes capture/control
  - **result:** NOT_ESTABLISHED

### RESOURCE_FLOW_MAP
- **item 1:**
  - **classification:** FORMAL_AUTHORITY
  - **flow:** Treaty-conferred competences
  - **from:** Member States
  - **support:**
    - FCT-005
    - FCT-006
  - **to:** EU institutions
- **item 2:**
  - **classification:** ACCESS_NOT_CONTROL
  - **flow:** meetings/resources/submissions intended to influence
  - **from:** interest representatives
  - **support:**
    - FCT-017
    - FCT-018
  - **to:** EU policy process

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Member States
  - **relation:** confer competences / ratify treaty amendments
  - **support:**
    - FCT-005
    - FCT-006
  - **to:** European Union treaty order
- **item 2:**
  - **from:** European Commission
  - **relation:** normally proposes legislation
  - **support:**
    - FCT-004
    - FCT-010
  - **to:** Parliament + Council legislative process
- **item 3:**
  - **from:** European Council
  - **relation:** sets political directions / priorities; political mandates
  - **support:**
    - FCT-002
    - FCT-019
  - **to:** EU institutional agenda
- **item 4:**
  - **from:** Parliament + Council
  - **relation:** joint co-legislation in OLP
  - **support:**
    - FCT-009
  - **to:** EU legislative acts
- **item 5:**
  - **from:** Commission
  - **relation:** infringement referral
  - **support:**
    - FCT-016
  - **to:** CJEU
- **item 6:**
  - **from:** interest representatives
  - **relation:** attempted influence/access
  - **support:**
    - FCT-017
    - FCT-018
  - **to:** EU policy and decision-making

### IMPACT_MAP
- **downstream:** INV-040 can consume this power map; INV-041 and INV-042 can deepen Commission-production and lobbying causal pathways.
- **measured_objects:**
  - competence boundaries
  - initiative
  - OLP adoption/veto rules
  - implementation/enforcement
  - annual budget/MFF/own resources
  - ECB independence
  - CJEU authority
  - lobbying access
  - European Council de facto legislative involvement
- **not_established:**
  - single global power ranking
  - general causal effect of lobbying on policy
  - general causal effect of European Council mandates on legislative outcomes
  - unified command over EU institutions

### CONTRADICTION_LEDGER
- **item 1:**
  - **claim:** each Member State has a general veto over EU legislation
  - **counter:**
    - FCT-007
    - FCT-009
  - **resolution:** REJECT_GENERAL_VETO
- **item 2:**
  - **claim:** European Council is formal EU legislature
  - **counter:**
    - FCT-002
  - **resolution:** REJECT_FORMAL_LEGISLATOR_LABEL
- **item 3:**
  - **claim:** European Council is irrelevant to lawmaking
  - **counter:**
    - FCT-019
  - **resolution:** REJECT_IRRELEVANCE
- **item 4:**
  - **claim:** Commission initiative equals unilateral lawmaking
  - **counter:**
    - FCT-009
    - FCT-011
  - **resolution:** SEPARATE_INITIATIVE_FROM_ADOPTION
- **item 5:**
  - **claim:** registered lobbying proves policy capture
  - **counter:**
    - FCT-017
    - FCT-018
  - **resolution:** SEPARATE_ACCESS_FROM_CAUSAL_CONTROL

### VERIFICATION_REPORT
- **causal_assessment:** lobbying outcome effect and European Council file-level effect remain unresolved
- **facts:** 19
- **key_controls:**
  - Article 15 vs CEPS
  - QMV vs unanimity
  - annual budget vs MFF/own resources
  - Transparency Register vs ECA audit
- **known_limit:** de facto causal magnitude cannot be reduced to one cross-domain score
- **sources:** 16
- **tier_policy:** formal facts anchored in official/primary sources; independent research/audit used for de facto/transparency controls
- **upstream_families:**
  - other:eurlex-treaties
  - other:consilium-voting
  - other:europarl-olp
  - other:commission-lawmaking
  - other:europarl-budget
  - other:consilium-budget
  - other:ecb
  - other:curia
  - other:commission-enforcement
  - other:eu-transparency-register
  - other:eca
  - other:ceps

### EDI_REPORT
- **corpus:**
  - **circularity:** formal-rule sources cluster by issuing institution; CEPS and ECA are independent controls for de facto and lobbying claims
  - **counters:** 4
  - **coverage:** 0.94
  - **direct_objects:** 8
  - **edi_star:** 0.87
  - **independence:** 0.88
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 8
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 5:**
    - **claim_id:** CLM-009
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 1.0
  - **lang:** 0.95
  - **owner:** 0.9
  - **persp:** N/A(institutional architecture)
  - **strat:** 0.9
  - **temp:** 1.0
- **edi:**
  - **final:** 0.87
  - **flags:**
    - LOBBYING_CAUSAL_EFFECT_UNRESOLVED
    - EUROPEAN_COUNCIL_CAUSAL_EFFECT_UNRESOLVED
  - **penalties:** 0.04
  - **raw:** 0.91
- **source_counts:**
  - **primary:** 14
  - **secondary:** 2
  - **total:** 16

### RESPONSIBILITY_MAP
- **item 1:**
  - **object:** ordinary legislation adoption
  - **responsible:** European Parliament + Council
  - **support:**
    - FCT-009
- **item 2:**
  - **object:** default legislative proposal
  - **responsible:** European Commission
  - **support:**
    - FCT-004
    - FCT-010
- **item 3:**
  - **object:** primary implementation
  - **responsible:** Member States; Commission uniform acts where conferred
  - **support:**
    - FCT-011
- **item 4:**
  - **object:** EU-law legality/interpretation
  - **responsible:** CJEU
  - **support:**
    - FCT-015
- **item 5:**
  - **object:** euro-area monetary decisions
  - **responsible:** ECB/Eurosystem under Treaty independence
  - **support:**
    - FCT-014

### NEXT_QUERIES
- **item 1:**
  - **query:** match lobbying positions/amendments/timing/final text with causal comparison
  - **trigger:** INV-042 execution
- **item 2:**
  - **query:** measure Commission proposal-to-final-text change and agenda success by procedure
  - **trigger:** INV-041 execution
- **item 3:**
  - **query:** trace summit conclusion to response/timing/content with a file-level counterfactual
  - **trigger:** material European Council file claim
- **item 4:**
  - **query:** refresh procedure-specific power map
  - **trigger:** Treaty/procedure reform

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-017,FCT-018,FCT-019 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-002,QRY-003 | support:- | counter:- | results:FCT-005,FCT-006 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-007,QRY-016 | support:- | counter:- | results:FCT-002,FCT-004,FCT-010,FCT-019 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-004,QRY-005,QRY-006 | support:- | counter:- | results:FCT-003,FCT-007,FCT-008,FCT-009 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-008,QRY-013 | support:- | counter:- | results:FCT-011,FCT-016 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-009,QRY-010 | support:- | counter:- | results:FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-011 | support:- | counter:- | results:FCT-014 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-012,QRY-013 | support:- | counter:- | results:FCT-015,FCT-016 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-014,QRY-015 | support:- | counter:- | results:FCT-017,FCT-018 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-004,QRY-005,QRY-006,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,SRC-001,SRC-002,SRC-004,SRC-005,SRC-006,SRC-008,SRC-009,SRC-010,SRC-011,SRC-012 | support:FCT-001,FCT-005,FCT-007,FCT-008,FCT-009,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | counter:- | results:FCT-001,FCT-005,FCT-007,FCT-008,FCT-009,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-002,QRY-003,QRY-004,QRY-005,SRC-002,SRC-003,SRC-004,SRC-005 | support:FCT-005,FCT-006,FCT-007,FCT-008 | counter:FCT-007(QMV prevalence) | results:FCT-005,FCT-006,FCT-007,FCT-008,FCT-007(QMV prevalence) | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-001,QRY-016,SRC-001,SRC-016 | support:FCT-002,FCT-019 | counter:FCT-002(no formal legislative function) | results:FCT-002,FCT-019,FCT-002(no formal legislative function) | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-001,QRY-006,QRY-007,QRY-008,QRY-013,SRC-001,SRC-006,SRC-007,SRC-008,SRC-013 | support:FCT-004,FCT-009,FCT-010,FCT-011,FCT-016 | counter:- | results:FCT-004,FCT-009,FCT-010,FCT-011,FCT-016 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-001,QRY-004,QRY-005,QRY-006,SRC-001,SRC-004,SRC-005,SRC-006 | support:FCT-003,FCT-007,FCT-008,FCT-009 | counter:- | results:FCT-003,FCT-007,FCT-008,FCT-009 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-009,QRY-010,SRC-009,SRC-010 | support:FCT-012,FCT-013 | counter:- | results:FCT-012,FCT-013 | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-011,SRC-011 | support:FCT-014 | counter:- | results:FCT-014 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-012,QRY-013,SRC-012,SRC-013 | support:FCT-015,FCT-016 | counter:- | results:FCT-015,FCT-016 | final:SUPPORTED | gap:NONE
CLM-009 | attempts:QRY-014,QRY-015,SRC-014,SRC-015 | support:FCT-017,FCT-018 | counter:- | results:FCT-017,FCT-018 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-009 | CLM | PARTIAL | CAUSALITY | General causal effect of lobbying access/resources on adopted policy content is not identified by the reviewed transparency evidence.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | The evidence identifies actors, access channels and transparency limitations but does not identify the counterfactual effect of lobbying on final policy content.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | CEPS documents systematic intervention and association with selected files, but the general counterfactual causal effect on legislative outcomes is not identified by the scoped evidence.

SEMANTIC_COUNTS_V1:LED:2|CLM:9|AXS:8|CAU:2|CTRL:4|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"evidence_excerpt":"selon le type de décision","kind":"HYPOTHESIS","lead":"A single global ranking of who rules the EU may be analytically invalid because formal authority, agenda power, veto, implementation, judicial and monetary authority are distributed by legal basis and procedure.","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006","AXS-007","CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"],"routes":["OBJECT_INVESTIGATION","SCOPE_HISTORY","COUNTER_HYPOTHESES"],"source_id":"INV-039_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-014","QRY-015","QRY-016"],"evidence_excerpt":"ne pas inférer capture à partir du lobbying seul","kind":"METHOD_CONSTRAINT","lead":"Lobbying access and political agenda-setting must be separated from formal legal authority and from demonstrated causal control of outcomes.","linked_ids":["AXS-008","CLM-003","CLM-009","CAU-001","CAU-002","CTRL-001","CTRL-004"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-017","FCT-018","FCT-019"],"routes":["MECHANISMS","COUNTER_HYPOTHESES","RULES_CONTROLS"],"source_id":"INV-039_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"There is no defensible single institution-wide ranking of who rules the EU: power is procedure- and domain-dependent, with different actors controlling competence boundaries, initiative, co-legislation, veto, implementation, judicial review, budget and monetary policy.","claimant":"INV-039 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-005","FCT-007","FCT-008","FCT-009","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015"]}
CLM-002 | {"claim":"Member States are upstream constitutional principals because EU competences are conferred by Treaty and ordinary Treaty amendments require ratification by all Member States; however, an individual Member State does not possess a general veto over ordinary EU legislation.","claimant":"INV-039 synthesis","counter":"FCT-007(QMV prevalence)","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-005","FCT-006","FCT-007","FCT-008"]}
CLM-003 | {"claim":"The European Council is not a formal legislator under Article 15 TEU, yet it is a material de facto agenda, crisis and impasse actor: CEPS reports its conclusions mention about 20% of OLP legislation and disproportionately target crisis, redistributive and competence-expanding files.","claimant":"INV-039 synthesis","counter":"FCT-002(no formal legislative function)","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-002","FCT-019"]}
CLM-004 | {"claim":"The Commission is the default legislative initiator and an important executive/enforcement actor, but it normally cannot enact ordinary legislation alone and its delegated/implementing powers are bounded by legislative delegations, Member-State comitology and co-legislator controls.","claimant":"INV-039 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-009","FCT-010","FCT-011","FCT-016"]}
CLM-005 | {"claim":"Parliament and Council are equal co-legislators under the ordinary legislative procedure, while Council voting rules preserve stronger Member-State veto leverage in Treaty-specified sensitive fields requiring unanimity.","claimant":"INV-039 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-007","FCT-008","FCT-009"]}
CLM-006 | {"claim":"EU fiscal authority is layered: Commission drafts the annual budget; Parliament and Council adopt it; the MFF requires Council unanimity after Parliament consent; own resources require unanimous adoption and national ratification.","claimant":"INV-039 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-012","FCT-013"]}
CLM-007 | {"claim":"The ECB is an unusually autonomous EU power centre in euro-area monetary policy because Treaty-based independence prohibits instructions from EU institutions or national governments, but this autonomy is domain-specific rather than a general governing mandate.","claimant":"INV-039 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-014"]}
CLM-008 | {"claim":"The CJEU exercises binding judicial/constitutional constraint through interpretation, legality review and compliance adjudication, while Commission infringement action supplies an enforcement route; this is judicial constraint, not general legislative agenda-setting.","claimant":"INV-039 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-015","FCT-016"]}
CLM-009 | {"claim":"EU lobbying is a documented channel of attempted influence and access, but registration, meetings and resource disclosures do not by themselves establish capture, tasking or causal control of adopted policy; the audit record also shows transparency gaps.","claimant":"INV-039 synthesis","counter":"NONE_FOUND","gap":"General causal effect of lobbying access/resources on adopted policy content is not identified by the reviewed transparency evidence.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-017","FCT-018"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-002","QRY-003"],"axis":"COMPETENCE_CONSTITUTION","links":["CLM-001","CLM-002"],"question":"Who controls the boundary of EU competences and Treaty revision?","result_ids":["FCT-005","FCT-006"],"sought_objects":["principle of conferral","Treaty revision/ratification"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-007","QRY-016"],"axis":"AGENDA_INITIATIVE","links":["CLM-003","CLM-004","CAU-002"],"question":"Who can set political priorities and initiate ordinary EU legislation?","result_ids":["FCT-002","FCT-004","FCT-010","FCT-019"],"sought_objects":["European Council directions","Commission right of initiative"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-004","QRY-005","QRY-006"],"axis":"COLEGISLATION_VETO","links":["CLM-002","CLM-005","CTRL-002"],"question":"Who adopts legislation and when do Member States retain individual vetoes?","result_ids":["FCT-003","FCT-007","FCT-008","FCT-009"],"sought_objects":["OLP equal footing","QMV","unanimity-sensitive fields"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-008","QRY-013"],"axis":"IMPLEMENTATION_ENFORCEMENT","links":["CLM-004","CLM-008"],"question":"Who implements, delegates, monitors and enforces EU law after adoption?","result_ids":["FCT-011","FCT-016"],"sought_objects":["national implementation","delegated/implementing acts","infringement route"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-009","QRY-010"],"axis":"BUDGET_FISCAL","links":["CLM-006","CTRL-003"],"question":"How is annual budget authority separated from MFF and own-resources authority?","result_ids":["FCT-012","FCT-013"],"sought_objects":["annual budget","MFF","own resources"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-011"],"axis":"MONETARY","links":["CLM-007"],"question":"How autonomous is the ECB inside its Treaty mandate?","result_ids":["FCT-014"],"sought_objects":["Article 130 independence"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-012","QRY-013"],"axis":"JUDICIAL","links":["CLM-008"],"question":"What binding power does the CJEU exercise and how does it interact with Commission enforcement?","result_ids":["FCT-015","FCT-016"],"sought_objects":["legality review","preliminary rulings","infringement sanctions"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-014","QRY-015"],"axis":"LOBBYING_ACCESS","links":["CLM-009","CAU-001","CTRL-004"],"question":"What does documented lobbying access establish about influence, and what does it not establish about causal control?","result_ids":["FCT-017","FCT-018"],"sought_objects":["Transparency Register scope","audit limitations","outcome attribution"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"NONE_FOUND","gap":"The evidence identifies actors, access channels and transparency limitations but does not identify the counterfactual effect of lobbying on final policy content.","gap_type":"CAUSALITY","limit":"Requires matched positions/text amendments/timing and a credible comparative or causal design; access != capture.","mechanism":"Lobbying access/resources -> adopted policy content or institutional control","status":"UNRESOLVED","support":["FCT-017","FCT-018"]}
CAU-002 | {"counter":"FCT-002(no formal legislative authority)","gap":"CEPS documents systematic intervention and association with selected files, but the general counterfactual causal effect on legislative outcomes is not identified by the scoped evidence.","gap_type":"CAUSALITY","limit":"Political agenda-setting != formal command; file-level causal tracing would be required.","mechanism":"European Council political mandates -> speed, shape or adoption of specific legislation","status":"UNRESOLVED","support":["FCT-002","FCT-019"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Treaty Article 15 plus CEPS evidence jointly falsify both extremes: the European Council is neither the formal EU legislature nor irrelevant to ordinary lawmaking.","status":"SUPPORTED","support":["FCT-002","FCT-019"]}
CTRL-002 | {"control":"QMV prevalence and unanimity exceptions jointly falsify the claim that every Member State has a veto over EU legislation while preserving real veto domains in sensitive fields.","status":"SUPPORTED","support":["FCT-007","FCT-008"]}
CTRL-003 | {"control":"Annual-budget procedure versus MFF/own-resources procedure falsifies blanket claims that either Parliament or national governments control the whole EU budget architecture alone.","status":"SUPPORTED","support":["FCT-012","FCT-013"]}
CTRL-004 | {"control":"Transparency Register plus ECA audit prevents two symmetric errors: absence of a recorded interaction cannot prove absence of lobbying, and presence of a registered interaction cannot prove capture or policy causation.","status":"SUPPORTED","support":["FCT-017","FCT-018"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-004 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-005 | SYS | OK | web | INV-039 | WEB_RESEARCH
SYS-006 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | INV-039 | MNEMO_S
SYS-007 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://eur-lex.europa.eu/eli/treaty/teu_2016/2025-03-15 | current TEU Articles 14-17 institutional functions
QRY-002 | FETCH | FOUND | SRC-002 | https://eur-lex.europa.eu/eli/treaty/teu_2016/art_5/oj | Article 5 TEU conferral member state competences
QRY-003 | FETCH | FOUND | SRC-003 | https://eur-lex.europa.eu/eli/treaty/teu_2016/art_48/oj/eng | Article 48 TEU treaty revision ratification all member states
QRY-004 | FETCH | FOUND | SRC-004 | https://www.consilium.europa.eu/en/council-eu/how-does-the-council-vote/qualified-majority/ | Council qualified majority 80 percent legislation double majority
QRY-005 | FETCH | FOUND | SRC-005 | https://www.consilium.europa.eu/en/council-eu/how-does-the-council-vote/unanimity/ | Council unanimity sensitive matters CFSP taxation own resources MFF
QRY-006 | FETCH | FOUND | SRC-006 | https://www.europarl.europa.eu/olp/en/ordinary-legislative-procedure/overview | ordinary legislative procedure Parliament Council equal footing Commission proposal
QRY-007 | FETCH | FOUND | SRC-007 | https://commission.europa.eu/law/law-making-process/planning-and-proposing-law_en | Commission right of initiative planning preparing proposing EU law
QRY-008 | FETCH | FOUND | SRC-008 | https://commission.europa.eu/law/law-making-process/adopting-eu-law/implementing-and-delegated-acts_en | delegated implementing acts member state primary implementation comitology
QRY-009 | FETCH | FOUND | SRC-009 | https://www.europarl.europa.eu/about-parliament/en/parliaments-powers/budgetary-powers | annual EU budget Commission draft Parliament Council adopt
QRY-010 | FETCH | FOUND | SRC-010 | https://www.consilium.europa.eu/en/policies/the-eu-s-long-term-budget-2028-2034/ | MFF unanimity Parliament consent own resources national ratification 2028 2034
QRY-011 | FETCH | FOUND | SRC-011 | https://www.ecb.europa.eu/ecb/our-values/independence/html/index.en.html | ECB independence Article 130 no instructions governments EU institutions
QRY-012 | FETCH | FOUND | SRC-012 | https://curia.europa.eu/site/jcms/d2_5390/en/about-the-court-of-justice-of-the-eu | CJEU role legality EU acts institutions member states preliminary rulings
QRY-013 | FETCH | FOUND | SRC-013 | https://commission.europa.eu/law/application-eu-law/implementing-eu-law/infringement-procedure_en | Commission infringement procedure refer Member State CJEU financial sanctions
QRY-014 | FETCH | FOUND | SRC-014 | https://transparency-register.europa.eu/index_en | EU Transparency Register activities intended to influence policy legislation decision making
QRY-015 | FETCH | FOUND | SRC-015 | https://www.eca.europa.eu/ECAHTML/SR-2024-05/en/body.html | European Court Auditors lobbying transparency register weaknesses gaps 2024
QRY-016 | FETCH | FOUND | SRC-016 | https://www.ceps.eu/ceps-publications/the-european-council-truly-the-law-maker-in-chief/ | European Council role in ordinary legislation 20 percent empirical study

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:eurlex-treaties | TEU-CONSOLIDATED-2025 | Consolidated Treaty on European Union - current text | 2025-03-15 | 2026-09-06T14:42:00Z | Articles 14-17: Parliament, European Council, Council, Commission | https://eur-lex.europa.eu/eli/treaty/teu_2016/2025-03-15
SRC-002 | ◈ | fam:other:eurlex-treaties | TEU-ART5 | Treaty on European Union - Article 5 | 2016-06-07 | 2026-09-06T14:42:00Z | principle of conferral; non-conferred competences remain with Member States | https://eur-lex.europa.eu/eli/treaty/teu_2016/art_5/oj
SRC-003 | ◈ | fam:other:eurlex-treaties | TEU-ART48 | Treaty on European Union - Article 48 | 2016-06-07 | 2026-09-06T14:42:00Z | ordinary and simplified treaty revision; ratification requirements | https://eur-lex.europa.eu/eli/treaty/teu_2016/art_48/oj/eng
SRC-004 | ◈ | fam:other:consilium-voting | CONSILIUM-QMV-2026 | Qualified majority | 2026-03 | 2026-09-06T14:42:00Z | QMV most used; about 80% legislation; 55% states and 65% population | https://www.consilium.europa.eu/en/council-eu/how-does-the-council-vote/qualified-majority/
SRC-005 | ◈ | fam:other:consilium-voting | CONSILIUM-UNANIMITY-2026 | Unanimity | 2026-02-12 | 2026-09-06T14:42:00Z | fields where unanimity applies and state veto remains | https://www.consilium.europa.eu/en/council-eu/how-does-the-council-vote/unanimity/
SRC-006 | ◈ | fam:other:europarl-olp | EP-OLP-OVERVIEW | Ordinary legislative procedure - Overview | 2026 | 2026-09-06T14:42:00Z | Parliament and Council joint equal-footing adoption; Commission proposal | https://www.europarl.europa.eu/olp/en/ordinary-legislative-procedure/overview
SRC-007 | ◈ | fam:other:commission-lawmaking | EC-RIGHT-INITIATIVE | Planning and proposing law | 2026 | 2026-09-06T14:42:00Z | Commission right of initiative and invitations from other actors | https://commission.europa.eu/law/law-making-process/planning-and-proposing-law_en
SRC-008 | ◈ | fam:other:commission-lawmaking | EC-DELEGATED-IMPLEMENTING | Implementing and delegated acts | 2026 | 2026-09-06T14:42:00Z | implementation split; delegation limits; Parliament/Council objection/revocation | https://commission.europa.eu/law/law-making-process/adopting-eu-law/implementing-and-delegated-acts_en
SRC-009 | ◈ | fam:other:europarl-budget | EP-BUDGETARY-POWERS | Budgetary powers | 2026 | 2026-09-06T14:42:00Z | annual budget draft and joint adoption | https://www.europarl.europa.eu/about-parliament/en/parliaments-powers/budgetary-powers
SRC-010 | ◈ | fam:other:consilium-budget | CONSILIUM-MFF-2028-2034 | The EU long-term budget for 2028-2034 | 2026-07-15 | 2026-09-06T14:42:00Z | MFF unanimity; EP consent; own resources unanimous and national ratification | https://www.consilium.europa.eu/en/policies/the-eu-s-long-term-budget-2028-2034/
SRC-011 | ◈ | fam:other:ecb | ECB-INDEPENDENCE | Independence | 2026 | 2026-09-06T14:42:00Z | institutional independence and no-instructions rule | https://www.ecb.europa.eu/ecb/our-values/independence/html/index.en.html
SRC-012 | ◈ | fam:other:curia | CJEU-ROLE | About the Court of Justice of the EU | 2026 | 2026-09-06T14:42:00Z | legality review, compliance and preliminary rulings | https://curia.europa.eu/site/jcms/d2_5390/en/about-the-court-of-justice-of-the-eu
SRC-013 | ◈ | fam:other:commission-enforcement | EC-INFRINGEMENT | Infringement procedure | 2026 | 2026-09-06T14:42:00Z | Commission enforcement route; Court may impose sanctions | https://commission.europa.eu/law/application-eu-law/implementing-eu-law/infringement-procedure_en
SRC-014 | ◈ | fam:other:eu-transparency-register | EU-TRANSPARENCY-REGISTER | Transparency Register | 2026 | 2026-09-06T14:42:00Z | scope and purpose of registered interest representation | https://transparency-register.europa.eu/index_en
SRC-015 | ◈ | fam:other:eca | ECA-SR-2024-05 | Special report 05/2024 - EU Transparency Register | 2024-04 | 2026-09-06T14:42:00Z | audit identifies transparency gaps and data limitations | https://www.eca.europa.eu/ECAHTML/SR-2024-05/en/body.html
SRC-016 | ◈ | fam:other:ceps | CEPS-EC-LAWMAKING-2026 | The European Council: truly the law-maker-in-chief? | 2026-08 | 2026-09-06T14:42:00Z | study of OLP since 1999; about 20% laws mentioned in summit conclusions | https://www.ceps.eu/ceps-publications/the-european-council-truly-the-law-maker-in-chief/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://eur-lex.europa.eu/eli/treaty/teu_2016/2025-03-15 | other:eurlex-treaties | 2025-03-15 | Formal institutional functions | The Treaty assigns Parliament and Council joint legislative and budgetary functions; the European Council provides political direction and does not exercise legislative functions; the Commission promotes the Union general interest, ensures application of the Treaties and Union law, executes the budget and exercises coordinating, executive and management functions. | -
FCT-002 | FACT | ✧ | https://eur-lex.europa.eu/eli/treaty/teu_2016/2025-03-15 | other:eurlex-treaties | 2025-03-15 | European Council formal limit | Article 15 TEU states that the European Council provides the Union with necessary impetus and defines general political directions and priorities, but does not exercise legislative functions. | -
FCT-003 | FACT | ✧ | https://eur-lex.europa.eu/eli/treaty/teu_2016/2025-03-15 | other:eurlex-treaties | 2025-03-15 | Council state representation | Article 16 TEU makes the Council a joint legislator with Parliament and specifies that it is composed of ministerial-level representatives able to commit and vote for their Member State governments. | -
FCT-004 | FACT | ✧ | https://eur-lex.europa.eu/eli/treaty/teu_2016/2025-03-15 | other:eurlex-treaties | 2025-03-15 | Commission treaty functions | Article 17 TEU gives the Commission initiative, Treaty/application oversight, budget execution, programme management and coordinating/executive functions; Union legislative acts normally require a Commission proposal except where Treaties provide otherwise. | -
FCT-005 | FACT | ✧ | https://eur-lex.europa.eu/eli/treaty/teu_2016/art_5/oj | other:eurlex-treaties | 2016-06-07 | Principle of conferral | Article 5 TEU provides that the Union acts only within competences conferred by Member States in the Treaties and that competences not conferred remain with Member States. | -
FCT-006 | FACT | ✧ | https://eur-lex.europa.eu/eli/treaty/teu_2016/art_48/oj/eng | other:eurlex-treaties | 2016-06-07 | Treaty revision control | Under Article 48 TEU, governments, Parliament or Commission may propose Treaty amendments, but ordinary amendments are determined by common accord of Member-State government representatives and enter into force only after ratification by all Member States according to constitutional requirements. | -
FCT-007 | FACT | ✧ | https://www.consilium.europa.eu/en/council-eu/how-does-the-council-vote/qualified-majority/ | other:consilium-voting | 2026-03 | Qualified-majority prevalence | Consilium states that qualified majority is the Council voting method used most frequently and applies to about 80% of EU legislation; the standard threshold is at least 55% of Member States representing at least 65% of the EU population. | -
FCT-008 | FACT | ✧ | https://www.consilium.europa.eu/en/council-eu/how-does-the-council-vote/unanimity/ | other:consilium-voting | 2026-02-12 | Unanimity-sensitive domains | Consilium lists sensitive fields requiring Council unanimity, including much of CFSP, citizenship, accession, indirect-tax harmonisation, own resources/MFF and certain justice, police and social-security provisions. | -
FCT-009 | FACT | ✧ | https://www.europarl.europa.eu/olp/en/ordinary-legislative-procedure/overview | other:europarl-olp | 2026 | Ordinary legislative procedure | The European Parliament describes the ordinary legislative procedure as the general rule for most EU legislation: Parliament and Council adopt jointly on equal footing, beginning from a Commission proposal, and neither co-legislator can normally adopt the act alone. | -
FCT-010 | FACT | ✧ | https://commission.europa.eu/law/law-making-process/planning-and-proposing-law_en | other:commission-lawmaking | 2026 | Commission right of initiative | The Commission states that it plans, prepares and proposes new EU legislation under its right of initiative, while also being able to respond to invitations from the European Council, Council, Parliament or a successful Citizens Initiative. | -
FCT-011 | FACT | ✧ | https://commission.europa.eu/law/law-making-process/adopting-eu-law/implementing-and-delegated-acts_en | other:commission-lawmaking | 2026 | Implementation and delegated powers | Primary responsibility for implementing EU law lies with Member States; where uniform implementation is needed the Commission, exceptionally the Council, may adopt implementing acts. Delegated acts cannot change essential legislative elements and Parliament/Council may revoke delegation or object. | -
FCT-012 | FACT | ✧ | https://www.europarl.europa.eu/about-parliament/en/parliaments-powers/budgetary-powers | other:europarl-budget | 2026 | Annual budget authority | The European Parliament states that the Commission prepares the annual draft EU budget and Parliament and Council share adoption power over the annual budget, with Parliament having the final say in the procedure. | -
FCT-013 | FACT | ✧ | https://www.consilium.europa.eu/en/policies/the-eu-s-long-term-budget-2028-2034/ | other:consilium-budget | 2026-07-15 | Long-term budget and own resources | For the 2028-2034 MFF, Consilium states that the Council must adopt the MFF regulation unanimously after Parliament consent, while the own-resources decision is adopted unanimously and ratified by all Member States under constitutional requirements. | -
FCT-014 | FACT | ✧ | https://www.ecb.europa.eu/ecb/our-values/independence/html/index.en.html | other:ecb | 2026 | ECB institutional independence | The ECB states that neither the ECB nor national central banks or their decision-makers may seek or take instructions from EU institutions, Member-State governments or other bodies, and those actors must not seek to influence them, pursuant to Article 130. | -
FCT-015 | FACT | ✧ | https://curia.europa.eu/site/jcms/d2_5390/en/about-the-court-of-justice-of-the-eu | other:curia | 2026 | CJEU judicial authority | The Court of Justice states that it interprets and enforces EU law, reviews legality of EU acts, ensures Member States and EU institutions comply with EU law, and gives preliminary rulings to national courts. | -
FCT-016 | FACT | ✧ | https://commission.europa.eu/law/application-eu-law/implementing-eu-law/infringement-procedure_en | other:commission-enforcement | 2026 | Commission enforcement and Court sanctions | The Commission may initiate infringement proceedings against a Member State that fails to implement EU law and refer the case to the Court of Justice; the Court can impose financial sanctions in applicable cases. | -
FCT-017 | FACT | ✧ | https://transparency-register.europa.eu/index_en | other:eu-transparency-register | 2026 | Lobbying as attempted influence | The interinstitutional Transparency Register defines interest representatives as actors conducting activities intended to influence EU policy, legislation or decision-making and records represented interests and resources; registration documents attempted access/influence activity, not success or causal control of outcomes. | -
FCT-018 | FACT | ✧ | https://www.eca.europa.eu/ECAHTML/SR-2024-05/en/body.html | other:eca | 2024-04 | Lobbying transparency limitations | The European Court of Auditors found weaknesses and gaps in the EU Transparency Register framework and public data, including incomplete meeting and historical information, reducing transparency; the audit does not establish that recorded lobbying caused policy outcomes. | -
FCT-019 | FACT | ✧ | https://www.ceps.eu/ceps-publications/the-european-council-truly-the-law-maker-in-chief/ | other:ceps | 2026-08 | European Council de facto legislative involvement | A CEPS empirical study of ordinary-legislative-procedure legislation since 1999 reports that European Council conclusions mention about 20% of legislation and disproportionately prioritise redistributive, competence-expanding and crisis-response laws; its summit mandates are politically consequential but not formal legislative acts. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-001
FCT-004 | SRC-001
FCT-005 | SRC-002
FCT-006 | SRC-003
FCT-007 | SRC-004
FCT-008 | SRC-005
FCT-009 | SRC-006
FCT-010 | SRC-007
FCT-011 | SRC-008
FCT-012 | SRC-009
FCT-013 | SRC-010
FCT-014 | SRC-011
FCT-015 | SRC-012
FCT-016 | SRC-013
FCT-017 | SRC-014
FCT-018 | SRC-015
FCT-019 | SRC-016

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 LEADS | NEXT_ACTION:7 SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 SCOPE | NEXT_ACTION:9 SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 SEARCH | NEXT_ACTION:10 FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 FACTS | NEXT_ACTION:11 CAUSAL_GAP
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 CAUSAL_GAP | NEXT_ACTION:13 VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 VERIFY | NEXT_ACTION:17 INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18 FINALIZATION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T14:50:40.479053+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":19,"eligible":19,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:19;attempted:0;success:0;failure:0;blocked:19} | WRITEBACK_EXECUTION_V1:[19 rows, see section]

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
