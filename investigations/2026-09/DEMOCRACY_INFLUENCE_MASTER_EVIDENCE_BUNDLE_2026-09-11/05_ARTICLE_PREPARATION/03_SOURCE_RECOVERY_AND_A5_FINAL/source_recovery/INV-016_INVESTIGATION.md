ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260911-1042-arab-spring-mechanisms | PARENT_RUN_ID:NONE | AS_OF:2026-09-11
INPUT_KIND:RUN_CARD | MISSION_MODE:GREENFIELD | INPUT_REF:PATH:/mnt/data/invchain/te016/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-11_arab-spring-mechanisms/2026-09-11_10-42_arab-spring-mechanisms_INPUT.md | SUBJECT_SLUG:arab-spring-mechanisms | SUBJECT_FP:sha256:afd1ab83ec3a64d5316b93d585f66e743c3c8eb2960dc069aeb0934b145e7080 | INPUT_SHA256:sha256:99153e7421ef5b0db9cd8df2a790d7a49b454304bc1a07dc491b96a1a168fbde
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:Cas sélectionnés 2010–2013 où les flux et actions sont documentables. Tracer acteur extérieur -> ressource/formation/plateforme/diplomatie -> bénéficiaire ou audience -> action de mobilisation -> exposition/participation -> effet politique. Prioriser archives, programmes d’aide, données de plateformes, communications diplomatiques, chronologies et études causales. Gardes : soutien != déclenchement ; réseau social != révolution ; financement != contrôle ; simultanéité != coordination ; changement de régime != effet attribuable à un seul mécanisme.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/NETWORK.md,clusters/INFORMATION.md,clusters/TEMPORAL.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-016 — Printemps arabes : assistance extérieure, plateformes et causalité des mobilisations

## Objet
Tester, sur des cas bornés en Égypte et en Tunisie, les chaînes `acteur extérieur -> ressource/formation/plateforme -> bénéficiaire/audience -> mobilisation -> participation -> effet politique`, sans convertir une contribution intermédiaire en cause suffisante du déclenchement ou du changement de régime.

## Résultat central
**FACT.** Une infrastructure substantielle d’assistance démocratique américaine préexistait au soulèvement égyptien : le GAO recense environ 154,8 M$ de financements governance/justice/democracy vers l’Égypte sur FY2006-2008, au sein de programmes touchant notamment société civile, participation civique et liberté de l’information (FCT-001, FCT-002).

**FACT.** Un transfert tactique transnational est documenté : Mohamed Adel, militant d’April 6, s’est rendu en Serbie en 2009 pour recevoir une formation aux méthodes d’organisation non violente liées à CANVAS/Otpor, puis a rapporté ces méthodes en Égypte (FCT-006).

**INFERENCE.** Cela ferme `assistance/formation -> capacité/adoption` dans des cas précis. Cela ne ferme ni `financeur -> commandement`, ni `formation -> décision de déclencher le soulèvement`, ni `formation -> chute du régime`.

## Égypte : plateformes, information et participation
**FACT.** L’enquête Tahrir de Tufekci et Wilson observe, après contrôle de plusieurs facteurs, une forte augmentation de la probabilité de participation au premier jour chez les utilisateurs des médias sociaux ; Facebook, téléphone et face-à-face constituaient des vecteurs majeurs d’information et de logistique (FCT-003). Environ la moitié des répondants produisaient et diffusaient aussi des images des manifestations, principalement via Facebook (FCT-004).

**CONTROL.** En 2008, la page Facebook liée à April 6 avait rapidement réuni environ 70 000 personnes, mais les mobilisations prévues avaient largement échoué hors Mahalla sous l’effet de la répression et d’une organisation de rue insuffisante (FCT-005).

**INFERENCE.** `réseau social -> information/logistique -> participation` est soutenu. `audience numérique -> mobilisation réussie` est directement falsifié comme règle suffisante.

## Assistance extérieure et orchestration
**FACT.** Des récits contemporains décrivent des formations ou soutiens de mouvements arabes par des organisations américaines financées publiquement (FCT-007). Un câble diplomatique de 2008 documente également la participation d’un militant d’April 6 à un sommet de mouvements de jeunesse et ses réunions avec des responsables américains et des think tanks (FCT-008).

**CONTROL.** Le même câble exprime explicitement le doute de l’ambassade sur l’existence du plan coordonné de transition avancé par l’interlocuteur (FCT-008). Les données disponibles documentent donc contacts, assistance et transfert de savoir-faire, pas une chaîne authentifiée de tasking américain vers l’opération du 25 janvier.

## Tunisie : catalyse numérique et origine domestique
**FACT.** Une enquête post-révolution auprès de 333 internautes tunisiens identifie des fonctions politiques, informationnelles et médiatiques de Facebook perçues comme catalytiques (FCT-009). Une autre étude fondée sur entretiens et enquête auprès de 608 utilisateurs conclut que les médias sociaux ont facilité les réseaux, le contournement du black-out, la réduction de problèmes d’action collective et la formation d’une identité protestataire (FCT-010).

**CONTROL.** Une analyse contemporaine de la révolution tunisienne met explicitement en garde contre le mythe de l’« e-révolution » : Internet a pu catalyser un mouvement né à Sidi Bouzid, sans constituer à lui seul son facteur déclencheur (FCT-011).

## Temporalité et assistance postérieure
**FACT.** Après 2011, la répression judiciaire des ONG américaines en Égypte a perturbé les programmes américains de démocratie et gouvernance ; Washington a fourni soutien diplomatique, juridique et flexibilité de subventions aux ONG concernées (FCT-012). NED décrit également la réponse au Printemps arabe comme une priorité de 2011 (FCT-013).

**INFERENCE.** Ces faits confirment l’existence d’un écosystème d’assistance, mais leur position temporelle interdit de les rétro-projeter comme preuve de conception préalable du soulèvement.

## Verdict
1. `assistance extérieure -> capacité civique/organisationnelle` : **établi**.
2. `formation transnationale -> adoption de tactiques par au moins certains militants` : **établi**.
3. `médias sociaux -> information/logistique/participation précoce` : **établi ou fortement soutenu dans les cas étudiés**.
4. `médias sociaux -> déclenchement unique de la révolution` : **non établi**.
5. `assistance occidentale -> commandement/orchestration des soulèvements` : **non fermé**.
6. `assistance ou plateformes -> chute du régime` : **non fermé causalement**.

Le modèle robuste est donc à étages : des capacités et savoir-faire externes existent réellement ; les plateformes diminuent certains coûts de coordination et accroissent l’exposition/participation ; mais les griefs domestiques, coalitions sociales, répression, décisions des élites et dynamiques locales restent indispensables pour expliquer le déclenchement et l’issue. `soutien != déclenchement ; financement != contrôle ; formation != tasking ; réseau social != révolution ; participation != changement de régime attribuable`.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:4|EDI_DECISIVE:6|SRC_COMPLETE:11/11

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-11
- **breaks:**
  - 2006-2008 assistance US préexistante
  - 2008 April 6 mobilisation Facebook et échec partiel hors Mahalla
  - 2009 formation CANVAS documentée
  - 2010-2011 soulèvements Tunisie/Égypte
  - 2012-2014 évaluations postérieures
- **status:** HISTORICAL_BOUNDED
- **window:** Égypte/Tunisie principalement 2006-2013, avec études rétrospectives ultérieures

### MANIPULATION_REPORT
- **assumptions:**
  - les montants d’aide prouvent une infrastructure mais pas un bénéficiaire particulier
  - les enquêtes de manifestants identifient participation/logistique mieux que l’issue du régime
  - les récits organisationnels et journalistiques sur formation exigent un plafond causal
- **clusters:**
  - POWER
  - NETWORK
  - INFORMATION
  - TEMPORAL
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - **I01:** transfert de capacité peut être réel sans principal commanditaire
  - **I02:** outils numériques réduisent des coûts sans déterminer l’issue
  - **I03:** chronologie distingue soutien préexistant et réponse post-soulèvement
- **input_kind:** RUN_CARD
- **mission_mode:** GREENFIELD
- **patterns:**
  - **P01:** assistance-to-capacity
  - **P02:** training-to-adoption
  - **P03:** platform-to-participation
  - **P04:** participation-without-outcome-closure
- **priorities:**
  - dater aide/formation
  - identifier bénéficiaire et adoption
  - mesurer participation
  - exiger contrefactuel pour issue
- **query_guidance:** archives publiques, documents de financement, câbles, études académiques; utiliser les récits militants comme preuve bornée de formation/adoption, pas de causalité générale
- **rhetorical:**
  - **R01:** transformer corrélation en commandement
  - **R02:** réduire une coalition à un outil numérique
  - **R03:** attribuer l’issue à un mécanisme intermédiaire
- **speaker:**
  - **goal:** tester les chaînes externes et numériques des printemps arabes
  - **target:** séparer capacité, mobilisation et changement de régime
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **S01:** acteur extérieur
  - **S02:** financement
  - **S03:** formation
  - **S04:** ONG
  - **S05:** militant
  - **S06:** plateforme
  - **S07:** information
  - **S08:** réseau
  - **S09:** tactique
  - **S10:** mobilisation
  - **S11:** participation
  - **S12:** répression
  - **S13:** coalition
  - **S14:** régime
  - **S15:** effet
- **threats:**
  - support=trigger
  - funding=control
  - training=tasking
  - social media=revolution
  - participation=regime change
  - post-hoc aid=pre-event orchestration

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - operational instructions/counterfactual
  - **input_ids:**
    - FCT-001
    - FCT-002
    - FCT-007
    - FCT-008
    - FCT-012
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no authenticated U.S. command chain to launch uprising
  - **not_computable:**
    - marginal regime-survival effect of assistance
  - **operations_applied:**
    - traced assistance to capacity
    - tested command/tasking edge
  - **reason:** séparer capacité, soutien et commandement
  - **result_ids:**
    - CLM-001
    - CLM-003
    - CAU-001
    - CAU-005
  - **status:** DONE
  - **trigger:** assistance/diplomatie/régime
- **item 2:**
  - **gaps:**
    - participant-level adoption records
  - **input_ids:**
    - FCT-006
    - FCT-007
    - FCT-008
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no network-wide tasking established
  - **not_computable:**
    - full diffusion denominator
  - **operations_applied:**
    - mapped trainer-trainee relation
    - separated adoption from principal-agent control
  - **reason:** distinguish contact/training from coordination
  - **result_ids:**
    - CLM-002
    - CAU-002
  - **status:** DONE
  - **trigger:** transnational tactical transfer
- **item 3:**
  - **gaps:**
    - randomized/platform outage causal design
  - **input_ids:**
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-009
    - FCT-010
    - FCT-011
  - **module:** clusters/INFORMATION.md
  - **negative_results:**
    - online reach not sufficient for street success
  - **not_computable:**
    - platform counterfactual for regime collapse
  - **operations_applied:**
    - tested information/logistics edge
    - used 2008 failure as negative control
  - **reason:** separate exposure, logistics, participation and outcome
  - **result_ids:**
    - CLM-004
    - CLM-005
    - CAU-003
    - CAU-004
  - **status:** DONE
  - **trigger:** Facebook/social media participation
- **item 4:**
  - **gaps:**
    - dated actor-specific grants/instructions
  - **input_ids:**
    - FCT-001
    - FCT-012
    - FCT-013
  - **module:** clusters/TEMPORAL.md
  - **negative_results:**
    - post-2011 support cannot prove pre-2011 orchestration
  - **not_computable:**
    - latent informal pre-event contacts beyond records
  - **operations_applied:**
    - ordered pre-2011 aid, 2011 uprising, post-2011 program response
  - **reason:** prevent post-event response from back-projection
  - **result_ids:**
    - CLM-001
    - CLM-006
    - CAU-005
  - **status:** DONE
  - **trigger:** pre/post uprising assistance claims

### SCOPING_REPORT
- **excluded:**
  - Libya/Syria military intervention
  - generic geopolitics
  - all Arab countries
  - claims without actor/case chain
- **included:**
  - Egypt pre-2011 democracy assistance
  - April 6/CANVAS transfer
  - Egypt social-media participation
  - Tunisia social-media coalition/catalyst
  - post-2011 aid chronology as control
- **reason:** bounded cases with traceable resource/platform mechanisms and explicit controls

### CREDO
- **forbidden_shortcuts:**
  - support=trigger
  - funding=control
  - training=tasking
  - social media=revolution
  - participation=outcome
- **rule:** prove each edge separately: assistance -> capacity -> adoption -> mobilization -> political outcome

### COGNITIVE_MAP
- **chain:**
  - acteur extérieur
  - ressource/formation
  - bénéficiaire
  - adoption
  - plateforme/information
  - mobilisation
  - participation
  - réaction régime
  - issue
- **rival_models:**
  - endogenous grievance
  - labor/social coalition
  - digital facilitation
  - external capacity support
  - external orchestration

### DIALECTICAL_MAP
- **antithesis:** Les soulèvements partent de griefs et coalitions domestiques; outils et formations ne déterminent ni déclenchement ni issue.
- **synthesis:** Capacités externes, transfert tactique et facilitation numérique sont établis dans des cas bornés; aucune chaîne ne ferme une orchestration externe ou une causalité générale sur la chute des régimes.
- **thesis:** Assistance occidentale et réseaux transnationaux/numériques ont contribué matériellement aux soulèvements.

### RESOURCE_FLOW_MAP
- **flows:**
  - US democracy assistance -> civil-society/media capacities in Egypt
  - CANVAS/Otpor -> tactical training -> April 6 activist
  - platforms -> information/logistics/amplification
- **limits:**
  - funding does not identify tasking
  - training does not identify command
  - platform use does not identify regime outcome

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** USAID/State/NED ecosystem
  - **relation:** democracy assistance
  - **support:**
    - FCT-001
    - FCT-002
  - **to:** Egypt civil-society/governance programs
- **item 2:**
  - **from:** CANVAS/Otpor trainers
  - **relation:** nonviolent tactics training
  - **support:**
    - FCT-006
  - **to:** Mohamed Adel / April 6
- **item 3:**
  - **from:** Facebook/social media interpersonal networks
  - **relation:** information/logistics
  - **support:**
    - FCT-003
    - FCT-004
  - **to:** Tahrir participants
- **item 4:**
  - **from:** Tunisian digital networks
  - **relation:** information/coalition facilitation
  - **support:**
    - FCT-009
    - FCT-010
    - FCT-011
  - **to:** protest ecosystem

### IMPACT_MAP
- **established:**
  - pre-2011 democracy-assistance infrastructure in Egypt
  - CANVAS tactical transfer to at least one April 6 activist
  - social-media facilitation of first-day participation/logistics in Egypt
  - social-media catalytic/network role in Tunisia
- **not_established:**
  - U.S. command of January 25 uprising
  - social media as sole trigger
  - external assistance as sufficient cause of regime change
- **partial:**
  - extent of U.S.-financed training links to April 6 as an organization
  - marginal contribution of tactical training to mobilization

### CONTRADICTION_LEDGER
- **item 1:**
  - **issue:** reports of U.S.-financed training versus lack of authenticated tasking
  - **resolution:** retain support-network fact; do not infer command or funding of the uprising
- **item 2:**
  - **issue:** large Facebook audience in 2008 but weak street result
  - **resolution:** use as direct sufficiency control against online reach = mobilization
- **item 3:**
  - **issue:** Tunisia studies call Facebook catalyst while warning against e-revolution myth
  - **resolution:** separate information/coalition mechanism from trigger/outcome causality
- **item 4:**
  - **issue:** post-2011 U.S./NED response may be mistaken for pre-event design
  - **resolution:** enforce temporal ordering; post-event response cannot establish prior orchestration

### VERIFICATION_REPORT
- **facts:** 13
- **method:** official funding records + diplomatic archive + academic participation studies + bounded training accounts + explicit negative controls
- **negative_checks:**
  - 2008 April 6 Facebook mobilization fizzled outside Mahalla
  - embassy doubted claimed transition plan
  - Tunisia e-revolution caution
  - post-2011 assistance temporal control
- **research_queries:** 11
- **sources_fetched:** 11
- **verdict:** sufficient for capacity/training/platform facilitation; insufficient for external orchestration or general regime-change causality

### EDI_REPORT
- **corpus:** 11 accepted sources across 9 provenance families
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim:** CLM-001
    - **families:**
      - A
  - **item 2:**
    - **claim:** CLM-002
    - **families:**
      - C
  - **item 3:**
    - **claim:** CLM-003
    - **families:**
      - A
      - D
      - other:iri
  - **item 4:**
    - **claim:** CLM-004
    - **families:**
      - B
      - C
  - **item 5:**
    - **claim:** CLM-005
    - **families:**
      - E
      - other:orbi
  - **item 6:**
    - **claim:** CLM-006
    - **families:**
      - A
      - B
      - C
      - E
      - other:orbi
- **diagnostic_not_truth:** true
- **dimensions:**
  - funding
  - diplomatic contact
  - training transfer
  - platform participation
  - Tunisia coalition
  - temporal control
- **edi:** DIVERSE_OFFICIAL_ACADEMIC_ARCHIVAL_WITH_CONTESTED_SUPPORT_SEPARATED
- **source_counts:**
  - **A:** 2
  - **B:** 1
  - **C:** 2
  - **D:** 1
  - **E:** 2
  - **other:iri:** 1
  - **other:ned:** 1
  - **other:orbi:** 1

### RESPONSIBILITY_MAP
- **item 1:**
  - **actor:** U.S. democracy-assistance institutions
  - **documented_action:** financed democracy/civil-society/media programs in Egypt before 2011
  - **intent:** PROVEN
  - **scope:** capacity support; uprising tasking not established
  - **support:**
    - FCT-001
    - FCT-002
- **item 2:**
  - **actor:** CANVAS/Otpor network
  - **documented_action:** trained at least one April 6 activist in nonviolent organizing tactics
  - **intent:** PROVEN
  - **scope:** training transfer; regime-change causality not established
  - **support:**
    - FCT-006
- **item 3:**
  - **actor:** social-media networks
  - **documented_action:** facilitated information/logistics and were associated with early protest participation
  - **intent:** N/A
  - **scope:** mechanism of communication/coordination, not intentional principal
  - **support:**
    - FCT-003
    - FCT-004
    - FCT-009
    - FCT-010
- **item 4:**
  - **actor:** domestic protest coalitions
  - **documented_action:** converted grievances/networks into street mobilization under repression
  - **intent:** PARTIAL
  - **scope:** domestic causal structure incompletely measured here
  - **support:**
    - FCT-005
    - FCT-011

### NEXT_QUERIES
- To close external orchestration, require authenticated instructions tying a funder/state to launch timing, operational plan and beneficiary compliance.
- To estimate platform causal effect, seek exogenous outages or stronger quasi-experimental variation linked to protest participation and outcome.
- For synthesis, retain capacity/training/platform mechanisms separately from trigger and regime-change claims.

## TRACE_MATRIX_V1
AXS-001 | attempts:QRY-001,QRY-002,QRY-004,QRY-005,QRY-006,QRY-007,QRY-011 | support:- | counter:- | results:FCT-001,FCT-002,FCT-005,FCT-006,FCT-007,FCT-008,FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-003,QRY-004,QRY-005,QRY-008,QRY-009,QRY-010 | support:- | counter:- | results:FCT-003,FCT-004,FCT-005,FCT-009,FCT-010,FCT-011 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-002,QRY-003,QRY-004,QRY-008,QRY-009,QRY-010 | support:- | counter:- | results:FCT-003,FCT-005,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,SRC-001 | support:FCT-001,FCT-002 | counter:- | results:FCT-001,FCT-002 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-004,QRY-005,SRC-004,SRC-005 | support:FCT-006 | counter:- | results:FCT-006 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-001,QRY-002,QRY-006,QRY-007,QRY-011,SRC-001,SRC-002,SRC-006,SRC-007,SRC-011 | support:FCT-001,FCT-002,FCT-007,FCT-008 | counter:FCT-008,FCT-012,FCT-013 | results:FCT-001,FCT-002,FCT-007,FCT-008,FCT-008,FCT-012,FCT-013 | final:PARTIAL | gap:CAUSALITY
CLM-004 | attempts:QRY-003,QRY-004,QRY-005,SRC-003,SRC-004,SRC-005 | support:FCT-003,FCT-004 | counter:FCT-005 | results:FCT-003,FCT-004,FCT-005 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-008,QRY-009,QRY-010,SRC-008,SRC-009,SRC-010 | support:FCT-009,FCT-010,FCT-011 | counter:- | results:FCT-009,FCT-010,FCT-011 | final:SUPPORTED | gap:NONE
CLM-006 | attempts:QRY-002,QRY-003,QRY-004,QRY-005,QRY-008,QRY-009,QRY-010,SRC-002,SRC-003,SRC-004,SRC-005,SRC-008,SRC-009,SRC-010 | support:FCT-003,FCT-006,FCT-009,FCT-010 | counter:FCT-005,FCT-011,FCT-012 | results:FCT-003,FCT-006,FCT-009,FCT-010,FCT-005,FCT-011,FCT-012 | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-003 | CLM | PARTIAL | CAUSALITY | Aucune instruction authentifiée reliant un financeur/État à la décision de lancer, au plan opérationnel ou à l’issue du soulèvement; le câble cité doute lui-même d’un plan coordonné.
CLM-006 | CLM | PARTIAL | CAUSALITY | Les données ferment des mécanismes de capacité, diffusion et participation mais pas le contrefactuel de régime; répression, griefs locaux, coalitions et décisions des élites restent des causes concurrentes non isolées.
CAU-004 | CAU | UNRESOLVED | CAUSALITY | Les études sont rétrospectives/perceptives et le mouvement naît localement à Sidi Bouzid; absence de contrefactuel sans réseaux sociaux.
CAU-005 | CAU | UNRESOLVED | CAUSALITY | Pas de chaîne unique de commandement ni de design identifiant l’effet marginal sur la survie du régime.

SEMANTIC_COUNTS_V1:LED:0|CLM:6|AXS:3|CAU:5|CTRL:5|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Une infrastructure substantielle d’assistance démocratique américaine existait en Égypte avant 2011 et finançait des capacités de société civile, participation et médias.","claimant":"INV-016","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-001","FCT-002"]}
CLM-002 | {"claim":"Un transfert tactique transnational de méthodes de mobilisation non violente vers au moins un militant d’April 6 est documenté avant 2011.","claimant":"INV-016","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-006"]}
CLM-003 | {"claim":"L’assistance occidentale documentée établit que les États-Unis ont commandé ou orchestré le soulèvement égyptien de janvier 2011.","claimant":"hypothèse forte","counter":["FCT-008","FCT-012","FCT-013"],"gap":"Aucune instruction authentifiée reliant un financeur/État à la décision de lancer, au plan opérationnel ou à l’issue du soulèvement; le câble cité doute lui-même d’un plan coordonné.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-001","FCT-002","FCT-007","FCT-008"]}
CLM-004 | {"claim":"En Égypte, les réseaux sociaux ont facilité information, logistique et participation précoce aux manifestations.","claimant":"INV-016","counter":["FCT-005"],"gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-004"]}
CLM-005 | {"claim":"En Tunisie, Facebook et les réseaux sociaux ont contribué à l’information, aux réseaux et à la formation d’une coalition protestataire, sans être démontrés comme déclencheur unique.","claimant":"INV-016","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"IMPORTANT","status":"SUPPORTED","support":["FCT-009","FCT-010","FCT-011"]}
CLM-006 | {"claim":"L’assistance extérieure ou les plateformes suffisent à expliquer causalement la chute des régimes lors des printemps arabes.","claimant":"hypothèse générale","counter":["FCT-005","FCT-011","FCT-012"],"gap":"Les données ferment des mécanismes de capacité, diffusion et participation mais pas le contrefactuel de régime; répression, griefs locaux, coalitions et décisions des élites restent des causes concurrentes non isolées.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-003","FCT-006","FCT-009","FCT-010"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-004","QRY-005","QRY-006","QRY-007","QRY-011"],"axis":"EXTERNAL_ASSISTANCE_TO_CAPACITY","links":["CLM-001","CLM-002","CLM-003","CAU-001","CAU-002"],"question":"Quelles aides, formations ou contacts extérieurs ont créé une capacité organisationnelle documentable sans établir un commandement externe ?","result_ids":["FCT-001","FCT-002","FCT-005","FCT-006","FCT-007","FCT-008","FCT-012","FCT-013"],"sought_objects":["funding","training","contact","recipient","adoption","instruction"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-005","QRY-008","QRY-009","QRY-010"],"axis":"PLATFORMS_TO_MOBILIZATION","links":["CLM-004","CLM-005","CAU-003","CAU-004"],"question":"Les réseaux sociaux ont-ils modifié information, logistique et probabilité de participation, et avec quel niveau causal ?","result_ids":["FCT-003","FCT-004","FCT-005","FCT-009","FCT-010","FCT-011"],"sought_objects":["platform_use","information","logistics","participation","offline_action"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-002","QRY-003","QRY-004","QRY-008","QRY-009","QRY-010"],"axis":"MOBILIZATION_TO_POLITICAL_OUTCOME","links":["CLM-006","CAU-004","CAU-005"],"question":"Quelles preuves isolent l’effet marginal de l’aide extérieure ou des plateformes sur la chute du régime plutôt que sur la seule capacité ou participation ?","result_ids":["FCT-003","FCT-005","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012"],"sought_objects":["counterfactual","outcome","repression","coalition","local_grievance","regime_response"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"financement/programmes -> capacités civiques/médiatiques/organisationnelles documentées","counter":"Programmes multiples et bénéficiaires hétérogènes; capacité ne vaut pas instruction opérationnelle.","limit":"Capacité institutionnelle fermée, tasking non inféré.","mechanism":"assistance démocratique extérieure -> ressources/capacité de société civile","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-012"]}
CAU-002 | {"causal_right":"formation identifiée -> retour en Égypte -> enseignement de tactiques non violentes","counter":["FCT-005"],"limit":"Transfert de méthode établi pour un acteur; effet marginal sur le soulèvement non isolé.","mechanism":"formation CANVAS -> apprentissage tactique -> transmission interne à April 6","status":"SUPPORTED","support":["FCT-006"]}
CAU-003 | {"causal_right":"usage social media -> information/logistique -> probabilité accrue de participation initiale","counter":["FCT-005"],"limit":"Association multivariée forte et mécanisme plausible; pas d’assignation randomisée ni effet sur issue du régime.","mechanism":"usage réseaux sociaux -> information/logistique -> participation au premier jour en Égypte","status":"SUPPORTED","support":["FCT-003","FCT-004"]}
CAU-004 | {"counter":["FCT-011"],"gap":"Les études sont rétrospectives/perceptives et le mouvement naît localement à Sidi Bouzid; absence de contrefactuel sans réseaux sociaux.","gap_type":"CAUSALITY","limit":"Catalyse informationnelle/coalition soutenue; déclenchement et résultat non isolés.","mechanism":"réseaux sociaux -> coalition/mobilisation -> chute de régime en Tunisie","status":"UNRESOLVED","support":["FCT-009","FCT-010"]}
CAU-005 | {"counter":["FCT-005","FCT-008","FCT-011","FCT-012"],"gap":"Pas de chaîne unique de commandement ni de design identifiant l’effet marginal sur la survie du régime.","gap_type":"CAUSALITY","limit":"Contributions intermédiaires documentées; causalité générale du changement de régime non établie.","mechanism":"assistance extérieure + plateformes -> soulèvement -> changement de régime","status":"UNRESOLVED","support":["FCT-001","FCT-006","FCT-003","FCT-009"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"audience numérique != mobilisation de rue réussie","status":"PASS","support":["FCT-005"]}
CTRL-002 | {"control":"contact/formation externe != tasking étatique","status":"PASS","support":["FCT-006","FCT-008"]}
CTRL-003 | {"control":"assistance démocratique != orchestration de révolution","status":"PASS","support":["FCT-001","FCT-002","FCT-012"]}
CTRL-004 | {"control":"réseau social != déclencheur unique","status":"PASS","support":["FCT-011","FCT-005"]}
CTRL-005 | {"control":"participation accrue != chute du régime attribuable","status":"PASS","support":["FCT-003","FCT-010","FCT-011"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:11|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | UNAVAILABLE | mnemolite | - | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | ACCEPTED | SRC-001 | https://www.gao.gov/products/gao-09-993 | INV-016 source fetch 1
QRY-002 | FETCH | ACCEPTED | SRC-002 | https://www.gao.gov/products/gao-14-799 | INV-016 source fetch 2
QRY-003 | FETCH | ACCEPTED | SRC-003 | https://academic.oup.com/joc/article-abstract/62/2/363/4085823 | INV-016 source fetch 3
QRY-004 | FETCH | ACCEPTED | SRC-004 | https://archive-yaleglobal.yale.edu/content/revolution-u | INV-016 source fetch 4
QRY-005 | FETCH | ACCEPTED | SRC-005 | https://www.pbs.org/wgbh/pages/frontline/revolution-in-cairo/inside-april6-movement/ | INV-016 source fetch 5
QRY-006 | FETCH | ACCEPTED | SRC-006 | https://wikileaks.org/plusd/cables/08CAIRO2572_a.html | INV-016 source fetch 6
QRY-007 | FETCH | ACCEPTED | SRC-007 | https://www.iri.org/news/new-york-times-discusses-iris-support-for-democracy-groups-in-egypt/ | INV-016 source fetch 7
QRY-008 | FETCH | ACCEPTED | SRC-008 | https://journals.sagepub.com/doi/full/10.1089/cyber.2011.0177 | INV-016 source fetch 8
QRY-009 | FETCH | ACCEPTED | SRC-009 | https://academic.oup.com/book/8138/chapter-abstract/153623879 | INV-016 source fetch 9
QRY-010 | FETCH | ACCEPTED | SRC-010 | https://orbi.uliege.be/handle/2268/178830 | INV-016 source fetch 10
QRY-011 | FETCH | ACCEPTED | SRC-011 | https://www.ned.org/publications-test-2/ | INV-016 source fetch 11

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:A | GAO-09-993 | U.S. GAO — Democracy Assistance (2009) | 2009-09-28 | 2026-09-11T08:42:00+00:00 | highlights/full report | https://www.gao.gov/products/gao-09-993
SRC-002 | ◈ | fam:A | GAO-14-799 | U.S. GAO — Lessons Learned from Egypt | 2014-07-24 | 2026-09-11T08:42:00+00:00 | highlights | https://www.gao.gov/products/gao-14-799
SRC-003 | ◉ | fam:B | JOC-2012-TUFEKCI-WILSON | Tufekci & Wilson — Tahrir protest participation | 2012-03-06 | 2026-09-11T08:42:00+00:00 | abstract/results | https://academic.oup.com/joc/article-abstract/62/2/363/4085823
SRC-004 | ◉ | fam:C | YALEGLOBAL-REVOLUTION-U | YaleGlobal — Revolution U | 2011-02-24 | 2026-09-11T08:42:00+00:00 | April 6/CANVAS account | https://archive-yaleglobal.yale.edu/content/revolution-u
SRC-005 | ◉ | fam:C | PBS-FRONTLINE-APRIL6 | PBS FRONTLINE — Inside April 6 Movement | 2011 | 2026-09-11T08:42:00+00:00 | movement chronology | https://www.pbs.org/wgbh/pages/frontline/revolution-in-cairo/inside-april6-movement/
SRC-006 | ◈ | fam:D | 08CAIRO2572 | U.S. diplomatic cable 08CAIRO2572 | 2008-12-30 | 2026-09-11T08:42:00+00:00 | summary/comment | https://wikileaks.org/plusd/cables/08CAIRO2572_a.html
SRC-007 | ◉ | fam:other:iri | IRI-NYT-2011 | IRI republication — U.S. Groups Helped Nurture Arab Uprisings | 2011-04-14 | 2026-09-11T08:42:00+00:00 | reported training/funding | https://www.iri.org/news/new-york-times-discusses-iris-support-for-democracy-groups-in-egypt/
SRC-008 | ◉ | fam:E | CYBER-2012-TUNISIA | Marzouki et al. — Facebook and Tunisian Revolution | 2012-04-23 | 2026-09-11T08:42:00+00:00 | abstract | https://journals.sagepub.com/doi/full/10.1089/cyber.2011.0177
SRC-009 | ◉ | fam:E | OUP-BREUER-2016 | Breuer — Social Media in Tunisian Revolution | 2016-08-18 | 2026-09-11T08:42:00+00:00 | abstract | https://academic.oup.com/book/8138/chapter-abstract/153623879
SRC-010 | ◉ | fam:other:orbi | LECOMTE-2011 | Lecomte — Révolution tunisienne et Internet | 2011 | 2026-09-11T08:42:00+00:00 | abstract/full text metadata | https://orbi.uliege.be/handle/2268/178830
SRC-011 | ◉ | fam:other:ned | NED-ANNUAL-INDEX | NED — Annual reports index 2010–2012 | 2012 | 2026-09-11T08:42:00+00:00 | 2010/2011 annual report descriptions | https://www.ned.org/publications-test-2/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.gao.gov/products/gao-09-993 | A | 2009-09-28 | U.S. democracy assistance in Egypt before 2011 | GAO reports about $154.8 million in governance/justice/democracy funding allocated to Egypt over FY2006-2008, placing Egypt among the larger recipients outside Iraq/Afghanistan. | -
FCT-002 | FACT | ✧ | https://www.gao.gov/products/gao-09-993 | A | 2009-09-28 | Content of U.S. democracy assistance | U.S. democracy assistance programs included civic participation, civil-society strengthening, media freedom/freedom of information and related governance activities; funding was implemented through USAID, State DRL and NED structures. | -
FCT-003 | FACT | ✧ | https://academic.oup.com/joc/article-abstract/62/2/363/4085823 | B | 2012-03-06 | Egypt social media and first-day protest participation | A survey of Tahrir participants found that, controlling for other factors, social-media use greatly increased the odds a respondent attended protests on the first day; information was primarily interpersonal via Facebook, phone or face-to-face contact. | -
FCT-004 | FACT | ✧ | https://academic.oup.com/joc/article-abstract/62/2/363/4085823 | B | 2012-03-06 | Egypt protest media production | About half of surveyed Tahrir participants produced and disseminated visual material from demonstrations, mainly through Facebook, documenting an information/amplification function distinct from regime-change causality. | -
FCT-005 | FACT | ✧ | https://archive-yaleglobal.yale.edu/content/revolution-u | C | 2011-02-24 | 2008 Facebook mobilization negative control | The April 6 Facebook page rapidly accumulated roughly 70,000 followers in 2008, yet planned solidarity protests largely fizzled outside Mahalla under repression and organizational uncertainty, showing online reach was not sufficient for successful street mobilization. | -
FCT-006 | FACT | ✧ | https://archive-yaleglobal.yale.edu/content/revolution-u | C | 2011-02-24 | CANVAS tactical training transfer | April 6 activist Mohamed Adel traveled to Serbia in 2009 and received training in nonviolent organization and street-mobilization tactics associated with CANVAS/Otpor, then returned to Egypt and trained others. | -
FCT-007 | FACT | ✧ | https://www.iri.org/news/new-york-times-discusses-iris-support-for-democracy-groups-in-egypt/ | other:iri | 2011-04-14 | Reported U.S.-financed democracy training links | A contemporaneous report republished by IRI stated that Arab activists, including figures linked to Egypt’s April 6 movement, had received training or support from U.S.-financed democracy organizations; this establishes a reported support network, not an authenticated command chain. | -
FCT-008 | FACT | ✧ | https://wikileaks.org/plusd/cables/08CAIRO2572_a.html | D | 2008-12-30 | April 6 activist contact with U.S. officials | A 2008 U.S. diplomatic cable records an April 6 activist’s participation in an Alliance of Youth Movements summit and meetings with U.S. officials and think tanks; the embassy explicitly expressed doubt about his claim of a coordinated opposition transition plan. | -
FCT-009 | FACT | ✧ | https://journals.sagepub.com/doi/full/10.1089/cyber.2011.0177 | E | 2012-04-23 | Tunisia Facebook perceived catalyst | A post-revolution online survey of 333 Tunisian Internet users identified political, informational and media-platform functions through which respondents perceived Facebook as a catalyst in the revolution. | -
FCT-010 | FACT | ✧ | https://academic.oup.com/book/8138/chapter-abstract/153623879 | E | 2016-08-18 | Tunisia social media coalition mechanisms | Research using expert interviews and a web survey of 608 Tunisian Facebook users argues that social media helped build networks, circumvent the media blackout, mitigate collective-action problems and support a national protest identity. | -
FCT-011 | FACT | ✧ | https://orbi.uliege.be/handle/2268/178830 | other:orbi | 2011 | Tunisia e-revolution caution | Lecomte describes Internet/social-media use as a catalyst for a protest movement born in Sidi Bouzid while warning against the e-revolution narrative that treats social networks as the triggering cause. | -
FCT-012 | FACT | ✧ | https://www.gao.gov/products/gao-14-799 | A | 2014-07-24 | Post-2011 U.S. democracy assistance and NGO trial | GAO found that Egypt’s prosecution of four U.S. NGOs significantly disrupted U.S. democracy-and-governance assistance after 2011; the U.S. government provided diplomatic, legal and grant-flexibility support, demonstrating an assistance infrastructure without proving orchestration of the 2011 uprising. | -
FCT-013 | FACT | ✧ | https://www.ned.org/publications-test-2/ | other:ned | 2012 | Temporal control on NED Arab Spring response | NED describes responding to the Arab Spring as a priority in 2011 and continued a broad global grants program; post-uprising expansion or response cannot by itself be back-projected as evidence of pre-uprising tasking. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-001
FCT-003 | SRC-003
FCT-004 | SRC-003
FCT-005 | SRC-004,SRC-005
FCT-006 | SRC-004,SRC-005
FCT-007 | SRC-007
FCT-008 | SRC-006
FCT-009 | SRC-008
FCT-010 | SRC-009
FCT-011 | SRC-010
FCT-012 | SRC-002
FCT-013 | SRC-011

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:FACTS
CP-003 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:CAUSAL
CP-004 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:FINALIZE

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-11T08:45:57.678038+00:00","fact_mem":{},"mnemo_row":"MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated.","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":13,"eligible":13,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:MNEMO_UNAVAILABLE — local memory service not available; no memory ids fabricated. | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:13;attempted:0;success:0;failure:0;blocked:13} | WRITEBACK_EXECUTION_V1:[13 rows, see section]

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
