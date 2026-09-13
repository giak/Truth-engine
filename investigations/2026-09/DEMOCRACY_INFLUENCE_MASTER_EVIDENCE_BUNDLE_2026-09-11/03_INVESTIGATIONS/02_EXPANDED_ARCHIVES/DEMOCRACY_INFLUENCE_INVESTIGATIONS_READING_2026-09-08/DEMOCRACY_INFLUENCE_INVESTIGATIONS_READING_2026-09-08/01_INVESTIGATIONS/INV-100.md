ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260907-0935-roumanie-annulation-election | PARENT_RUN_ID:NONE | AS_OF:2026-09-07
INPUT_KIND:RUN_CARD | MISSION_MODE:DEEPEN | INPUT_REF:PATH:/mnt/data/inv100-exec/te/truth-engine-v2_2.10.6-R3P1_CANONICAL/investigations/2026-09/2026-09-07_roumanie-annulation-election/2026-09-07_09-35_roumanie-annulation-election_INPUT.md | SUBJECT_SLUG:roumanie-annulation-election | SUBJECT_FP:sha256:6526667365a488e5cb5877deb14667787b557ae7db4432f641e4a55b0e0f2ba3 | INPUT_SHA256:sha256:b2cb293b8a8f4df17a11640248479e706c08517230c798b1222522fb2c3f4c4e
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:6 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/Europe 2015-2026 with Romania 2024-2025 as the central case and Austria 2016 as a procedurally isomorphic control; distinguish allegation, legal finding, evidentiary basis, annulment, remedy, electoral effect and proven instrumentalization.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/FRAMING.md,clusters/CONFIRMATION.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-100 — Annulation ou neutralisation judiciaire/administrative d’une élection : Roumanie et comparaisons internationales

## Question et règle de preuve

L’enquête sépare six objets souvent fusionnés : **allégation d’irrégularité**, **preuve disponible**, **constat juridictionnel**, **base juridique et standard d’annulation**, **effet institutionnel**, puis **effet électoral et intention éventuelle**. Une décision judiciaire est une source primaire pour ce qu’elle décide et pour les motifs qu’elle énonce ; elle ne transforme pas automatiquement les évaluations de renseignement qu’elle cite en faits indépendamment établis.

Le cas roumain de 2024 est central. L’Autriche 2016 sert de contrôle procédural, non de précédent juridique contraignant : elle permet de tester l’idée erronée selon laquelle une annulation ne serait légitime que si une manipulation effective du vote était prouvée.

## 1. Une séquence institutionnelle exceptionnelle, mais documentée

Le 2 décembre 2024, la Cour constitutionnelle roumaine a rejeté une demande d’annulation fondée sur la fraude et a ensuite confirmé le résultat du premier tour. Elle a retenu Călin Georgescu et Elena Lasconi pour le second tour. Les procès-verbaux examinés ne révélaient pas, selon elle, d’irrégularités capables d’infirmer le résultat établi. [FCT-001, FCT-002, FCT-003]

Le 4 décembre, plusieurs notes de renseignement ont été déclassifiées. Le 6 décembre, la même Cour a ouvert d’office un contrôle sur cette nouvelle matière, interprété largement sa compétence constitutionnelle de surveillance de l’élection présidentielle, puis annulé l’intégralité du processus électoral. La décision a aussi atteint les votes du second tour déjà exprimés et imposé un redémarrage complet, avec nouvelles candidatures et nouvelle campagne. [FCT-004, FCT-005, FCT-010]

La contradiction apparente entre validation et annulation ne peut donc pas être réduite à « la Cour s’est contredite sans raison » : un **nouvel ensemble d’informations** est intervenu entre les deux décisions. Cela ne tranche pas la question plus difficile de savoir si ces informations et la procédure étaient suffisamment robustes pour justifier la mesure la plus radicale.

## 2. Ce que la Cour a effectivement constaté

La décision du 6 décembre affirme que le processus électoral a été vicié à plusieurs étapes par des violations touchant la liberté et la correction du vote, l’égalité des chances, la transparence de la campagne et son financement. Selon les notes de renseignement sur lesquelles elle s’appuie, les problèmes centraux tenaient à une utilisation non transparente et contraire au droit de technologies numériques et de l’intelligence artificielle, à une promotion agressive sur les réseaux sociaux, à des contenus électoraux non identifiés comme tels, à un traitement préférentiel sur des plateformes et à des financements non déclarés. [FCT-006, FCT-007, FCT-008]

Sur le financement, la décision avait notamment relevé l’incongruité entre un budget déclaré à zéro et l’ampleur apparente de la campagne. Un contrôle ultérieur de l’Autorité électorale permanente apporte ici une corroboration indépendante mais plus étroite : il a enregistré **0,00 lei de contributions électorales mais 591,86 lei de dépenses électorales**, puis infligé plusieurs amendes et un avertissement pour violations de la loi sur le financement politique. [FCT-009, FCT-011, FCT-012]

Ce contrôle postérieur consolide donc l’existence d’irrégularités financières. Il ne prouve pas pour autant la totalité de la chaîne suggérée en décembre : origine ultime des ressources, éventuel commanditaire étranger, tasking, coordination des réseaux en ligne et effet électoral.

## 3. Le point faible : attribution étrangère et chaîne causale

La décision 32 est forte comme preuve de l’**acte juridictionnel**, des **motifs retenus par la Cour** et du **rôle des notes déclassifiées**. Elle est plus faible comme preuve publique autonome de la chaîne :

`État étranger -> commanditaire -> opérateur -> campagne -> exposition -> persuasion -> modification du résultat`.

La décision publiée ne ferme pas, par elle-même, l’arête commanditaire étatique/tasking. L’ouverture par la Commission européenne d’une procédure DSA contre TikTok confirme qu’il existait des soupçons suffisamment sérieux pour examiner les risques liés aux systèmes de recommandation, à la manipulation inauthentique coordonnée et aux contenus politiques payés ; cette ouverture reste une **procédure pour violation présumée**, pas une décision finale établissant l’ingérence ou la responsabilité de TikTok. [FCT-019]

Un contrôle contradictoire complique encore l’attribution par simple ressemblance de méthode : une enquête de Snoop a rapporté, sur la base d’une source informée d’un contrôle ANAF et d’échanges avec Kensington Communication, que le PNL avait financé la campagne TikTok « Echilibru și Verticalitate ». Kensington a reconnu un financement PNL d’une campagne tout en affirmant que sa version avait été modifiée sans son implication. [FCT-022]

Ce point est matériel parce que des documents de renseignement avaient rapproché cette campagne d’un modèle russe. Mais la conséquence doit rester bornée : **une ressemblance opérationnelle ne prouve pas l’origine**, et l’existence d’un financement domestique pour cette campagne ne démontre pas que toute l’activité pro-Georgescu était domestique ni qu’aucune activité étrangère distincte n’existait.

## 4. Annuler sans prouver une manipulation effective : le contrôle autrichien

L’Autriche 2016 empêche d’appliquer un faux standard. La Cour constitutionnelle autrichienne a annulé le second tour de l’élection présidentielle après une audience publique de plusieurs jours, l’audition de 90 témoins et la constatation de violations des règles relatives au dépouillement des votes postaux dans 14 circonscriptions. Environ 77 000 votes étaient concernés, alors que l’écart entre candidats était d’environ 30 000 voix. [FCT-017]

La jurisprudence autrichienne n’exigeait pas de démontrer que ces violations avaient réellement produit une fraude ou changé des votes : il suffisait que des règles destinées à empêcher les abus aient été violées et que le nombre de votes concernés soit assez élevé pour **pouvoir** influencer le résultat. [FCT-018]

Le bon test n’est donc pas : « peut-on prouver exactement combien d’électeurs ont été manipulés ? ». Le test plus défendable est : **les irrégularités sont-elles clairement établies et leur ampleur permet-elle de montrer de façon convaincante qu’elles pouvaient modifier le résultat ?**

Sur ce second point, le dossier roumain publié est moins transparent que le contrôle autrichien : la décision affirme une exposition significative, une distorsion et une manipulation, mais ne présente pas un dénominateur quantifié comparable reliant les irrégularités à l’ordre des candidats ou à un résultat contrefactuel.

## 5. Le standard européen après la Roumanie

La Commission de Venise a précisément tiré de cette affaire un rapport urgent sur l’annulation d’élections. Elle ne s’est pas prononcée sur le fond de la décision roumaine. Elle a cependant posé un cadre exigeant : l’annulation doit rester exceptionnelle, les irrégularités doivent être clairement établies et assez significatives pour avoir pu influencer le résultat, le seuil doit être élevé, et il n’est pas nécessaire de démontrer avec certitude l’effet réel sur le résultat. [FCT-013]

Sur la procédure, elle demande des garanties permettant aux parties affectées de présenter leurs vues et leurs preuves et insiste sur une décision équitable, objective et suffisamment motivée. [FCT-014]

Pour les campagnes en ligne, elle ajoute une exigence directement pertinente au cas roumain : les violations et les preuves doivent être indiquées précisément et une décision ne doit pas reposer **uniquement** sur du renseignement classifié, qui ne peut servir que de contexte si l’on veut préserver transparence et vérifiabilité. [FCT-015]

Le résultat analytique est donc intermédiaire : la possibilité d’une annulation extraordinaire n’est pas en elle-même anormale ou antidémocratique, mais une compétence d’office très large accroît la nécessité d’un standard probatoire lisible et de garanties procédurales fortes.

## 6. Recours européen et exclusion de 2025

La Cour européenne des droits de l’homme a déclaré la requête Georgescu irrecevable en mars 2025 parce que, dans la structure constitutionnelle roumaine, la présidence n’entrait pas dans le champ de l’article 3 du Protocole n°1 invoqué. Cette décision n’a donc ni validé ni invalidé le bien-fondé de l’annulation de décembre. [FCT-016]

En mars 2025, la candidature de Georgescu au scrutin répété a ensuite été refusée par le Bureau électoral central et la Cour constitutionnelle a rejeté les contestations dirigées contre ce refus. [FCT-020]

L’ODIHR a, dans son rapport final sur l’élection répétée de mai 2025, jugé le scrutin efficacement administré et offrant un choix réel aux électeurs, tout en critiquant le fait que certaines conditions d’éligibilité reposent sur des décisions de justice plutôt que sur des dispositions juridiques suffisamment claires et en recommandant de renforcer les garanties de recours et de procédure. [FCT-021]

Ces éléments établissent une **neutralisation institutionnelle effective** de la candidature et une controverse sérieuse sur la sécurité juridique. Ils ne suffisent pas à établir une intention coordonnée des institutions de supprimer politiquement un adversaire.

## 7. Où s’arrête la preuve

Le dossier ferme fortement les niveaux suivants :

- **I0** : identité et compétence des institutions, candidat et décisions ;
- **I1** : existence de ressources de campagne et de dépenses, au moins partiellement ;
- **I2** : actes institutionnels et certaines violations de financement ;
- **I6 institutionnel** : annulation, reprise du scrutin et exclusion ultérieure de candidature.

Il reste incomplet sur :

- **I3** : commanditaire étranger, coordination et tasking ;
- **I4** : exposition avec un dénominateur robuste et comparable ;
- **I5** : réception et persuasion des électeurs ;
- **I7** : résultat contrefactuel — qui aurait accédé au second tour ou gagné sans les irrégularités.

Le dossier pénal Georgescu–Potra a franchi en août 2026 l’étape autorisant le jugement au fond sur d’autres accusations, notamment relatives à l’ordre constitutionnel. Ce statut ne constitue ni une condamnation ni une preuve rétroactive des effets de la campagne électorale de 2024. [FCT-023]

## Conclusion technique

Trois propositions résistent au contrôle contradictoire.

**Premièrement**, l’annulation de décembre 2024 n’est pas une fiction politique : c’est un acte juridictionnel définitif, motivé par de réelles catégories d’irrégularités, dont le volet financement a ensuite reçu une corroboration administrative indépendante.

**Deuxièmement**, ce constat ne ferme pas la thèse maximale d’une ingérence étrangère ayant causalement changé le résultat. Le dossier public examiné ne fournit pas une chaîne complète de commandement étranger ni une démonstration du résultat contrefactuel.

**Troisièmement**, l’hypothèse inverse — « annulation = coup judiciaire démontré » — n’est pas établie non plus. L’effet institutionnel est certain, les questions de procédure et de sécurité juridique sont matérielles, mais l’intention d’instrumentalisation politique n’est pas prouvée.

Le résultat le plus robuste pour les synthèses aval est donc : **irrégularités et intervention institutionnelle établies ; suffisance publique de la chaîne d’attribution et de causalité discutables et incomplètes ; instrumentalisation intentionnelle non établie**.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:3|EDI_DECISIVE:5|SRC_COMPLETE:12/12

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **anchor_events:**
  - 2016-07-01 Austria runoff annulled
  - 2024-11-24 Romania first round
  - 2024-12-02 CCR rejects annulment challenge and validates result
  - 2024-12-04 intelligence notes declassified
  - 2024-12-06 CCR annuls entire process
  - 2024-12-17 EU opens TikTok DSA proceedings
  - 2025-03-05 AEP audit closes
  - 2025-03-06 ECtHR inadmissibility
  - 2025-03-11 Georgescu candidacy rejection upheld
  - 2025-10-28 ODIHR final report
  - 2026-08-06 Georgescu-Potra merits trial authorized
- **as_of:** 2026-09-07
- **rules:**
  - event date != publication date
  - judicial finding != later audit finding
  - procedural step != merits judgment
  - new evidence can reopen prior validation but must be tested under safeguards
- **window:** 2016-2026

### MANIPULATION_REPORT
- **assumptions:**
  - official acts are primary for what institutions did/held
  - comparators must share legal-remedy structure
  - no intentionality without evidence
- **clusters:**
  - **loaded:**
    - clusters/POWER.md
    - clusters/FRAMING.md
    - clusters/CONFIRMATION.md
- **complexity:**
  - **band:** HIGH
  - **score:** 8
- **implicit:**
  - the 2-to-6 December reversal can be explained by new evidence without proving its sufficiency
  - legal validity and democratic legitimacy are separable
  - a domestic-funded campaign does not refute all foreign activity
- **input_kind:** RUN_CARD
- **mission_mode:** DEEPEN
- **patterns:**
  - exceptional election annulment
  - intelligence-to-judgment evidence transfer
  - algorithmic amplification claim
  - campaign-finance opacity
  - candidate exclusion
  - foreign-interference attribution
- **priorities:**
  - legal basis
  - evidence provenance
  - potential-effect threshold
  - procedural safeguards
  - foreign attribution
  - institutional versus voter effect
- **query_guidance:** trace allegation -> evidence -> legal standard -> finding -> remedy -> review -> institutional effect -> exposure -> persuasion -> counterfactual; compare only isomorphic annulment procedures
- **rhetorical:**
  - **AUTH:** institutional claims bounded to direct role
  - **BF:** N/A
  - **DEM:** avoid majority/mandate rhetoric as evidence
  - **FAC:** no actor-to-network generalization
  - **NUM:** vote/exposure numbers require denominator and causal relevance
- **speaker:**
  - **goal:** separate lawful remedy, evidentiary gap and proven instrumentalization
  - **target:** legal-evidentiary chain of election annulment
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 3
  - **Λ:** 5
  - **Ξ:** 4
  - **Σ:** 5
  - **Φ:** 4
  - **Ψ:** 4
  - **Ω:** 2
  - **κ:** 4
  - **ρ:** 6
  - **€:** 4
  - **↕:** 7
  - **⏰:** 7
  - **⚔:** 5
  - **⫸:** 5
  - **🌐:** 5
- **threats:**
  - annulment=illegitimacy
  - authority=proof
  - foreign label=state tasking
  - exposure=persuasion
  - effect=intent

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - procedural comparability and discretion
  - **input_ids:**
    - FCT-005
    - FCT-010
    - FCT-014
    - FCT-020
    - FCT-021
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no proof of suppressive institutional intent
  - **not_computable:**
    - counterfactual political intent
  - **operations_applied:**
    - separated competence from legitimacy
    - compared procedural safeguards and downstream institutional effect
  - **reason:** test exceptional judicial power, legal limits, remedies and accountability without inferring intent
  - **result_ids:**
    - CLM-001
    - CLM-005
    - CLM-006
    - CTRL-001
  - **status:** DONE
  - **trigger:** ↕
- **item 2:**
  - **gaps:**
    - underlying attribution evidence
  - **input_ids:**
    - FCT-004
    - FCT-006
    - FCT-007
    - FCT-016
    - FCT-019
    - FCT-022
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - no basis to convert serious indications into closed foreign-state attribution
  - **not_computable:**
    - full public vocabulary effect
  - **operations_applied:**
    - distinguished official label from proof
    - retained domestic-funding contradiction and jurisdictional ECtHR limit
  - **reason:** separate labels such as interference, manipulation and validation from the evidence each term carries
  - **result_ids:**
    - CLM-003
    - CTRL-002
    - CTRL-005
    - CTRL-006
  - **status:** DONE
  - **trigger:** Λ
- **item 3:**
  - **gaps:**
    - platform exposure and causal voter data
  - **input_ids:**
    - FCT-008
    - FCT-013
    - FCT-017
    - FCT-018
  - **module:** clusters/CONFIRMATION.md
  - **negative_results:**
    - no measured persuasion or I7 outcome
  - **not_computable:**
    - individual voter persuasion counterfactual
  - **operations_applied:**
    - separated exposure from persuasion
    - used Austria potential-effect denominator as control
  - **reason:** test claims that online visibility or algorithmic amplification necessarily manufactured voter choice
  - **result_ids:**
    - CLM-004
    - CTRL-003
  - **status:** DONE
  - **trigger:** κ

### SCOPING_REPORT
- **classification_dimensions:**
  - legal basis
  - trigger
  - evidence provenance
  - standard of proof
  - party participation
  - irregularity
  - scale
  - potential outcome effect
  - remedy
  - appeal
  - intent
- **exclusions:**
  - accusation=judicial finding
  - annulment=illegitimate interference
  - intelligence assessment=fact by authority
  - institutional effect=voter persuasion
  - foreign suspicion=foreign-state attribution
- **scope:** Romania presidential election 2024-2025; Austria 2016 control; France/Europe only where legally comparable.
- **status:** ACTIVE

### CREDO
- accusation != judicial finding
- intelligence assessment != fact by authority
- legal annulment != illegitimate interference
- institutional effect != voter persuasion
- foreign suspicion != foreign-state tasking
- timing correlation != instrumentalization
- court finding != counterfactual outcome
- investigation or trial != conviction

### COGNITIVE_MAP
- **causal_boundary:** I0-I2 strong for institutional/legal identities and actions; I3 foreign tasking partial/unestablished; I4 partial; I5 not established; I6 verified for institutional consequences; I7 not established.
- **core_model:** Romania 2024 closes the legal-annulment and institutional-effect edges strongly; independent later audit corroborates campaign-finance violations; public evidence remains incomplete for foreign-state tasking, voter persuasion and counterfactual outcome.
- **relation_chain:**
  - irregularity/allegation
  - evidence provenance
  - legal standard
  - judicial finding
  - remedy
  - institutional effect
  - exposure
  - persuasion
  - counterfactual outcome
  - intent
- **rival_models:**
  - legitimate extraordinary remedy to serious irregularities
  - legally grounded but procedurally/evidentially under-specified annulment
  - politically instrumentalized judicial intervention
  - mixed model: real irregularities plus broad judicial discretion and incomplete public proof

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** Austria 2016 shows actual manipulation need not be proven when legal violations are established and the affected universe is large enough potentially to alter the result.
  - **resolution:** Require a high potential-effect threshold, not impossible proof of actual manipulation; then ask whether the Romanian public record satisfies that threshold transparently.
  - **thesis:** Without proof that manipulation actually changed votes, annulment was necessarily illegitimate.
- **item 2:**
  - **antithesis:** Decision 32 relies on intelligence notes but does not publish a complete sponsor-tasking-operator chain; one campaign has a material domestic-funding contradiction.
  - **resolution:** Treat foreign interference as an attribution gap, not a judicially closed fact.
  - **thesis:** The Romanian decision proves Russian/foreign control of the decisive campaign.
- **item 3:**
  - **antithesis:** The application was inadmissible because the presidency did not fall within the relevant Convention provision.
  - **resolution:** No ECtHR merits endorsement or rejection of Decision 32 is established.
  - **thesis:** The ECtHR validated the annulment.

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** campaign support sources
  - **limits:**
    - ultimate origin and tasking are heterogeneous and incompletely established
  - **resource:** online promotion / electoral expenditure
  - **support:**
    - FCT-007
    - FCT-008
    - FCT-009
    - FCT-011
    - FCT-022
  - **to:** Georgescu campaign visibility
  - **via:** social-media ecosystem and third parties
- **item 2:**
  - **from:** intelligence services
  - **limits:**
    - assessment flow != independent proof of every underlying fact
  - **resource:** declassified assessments
  - **support:**
    - FCT-004
    - FCT-006
    - FCT-010
  - **to:** constitutional annulment decision
  - **via:** public disclosure and CCR review

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** Romanian intelligence services
  - **limits:**
    - transmission and court reliance verified; underlying assertions not independently proven by this edge
  - **relation:** declassified information notes
  - **support:**
    - FCT-004
    - FCT-006
    - FCT-007
  - **to:** Romanian Constitutional Court
- **item 2:**
  - **from:** Romanian Constitutional Court
  - **limits:**
    - legal effect verified; legitimacy and proportionality require separate standard
  - **relation:** constitutional supervision / Decision 32
  - **support:**
    - FCT-005
    - FCT-010
  - **to:** 2024 presidential electoral process
- **item 3:**
  - **from:** Permanent Electoral Authority
  - **limits:**
    - does not establish full sponsor/tasking chain
  - **relation:** campaign-finance audit and sanctions
  - **support:**
    - FCT-011
    - FCT-012
  - **to:** Calin Georgescu campaign
- **item 4:**
  - **from:** BEC + Constitutional Court
  - **limits:**
    - institutional effect != proven suppressive intent
  - **relation:** candidacy registration rejection and final challenge decision
  - **support:**
    - FCT-020
  - **to:** Calin Georgescu 2025 candidacy

### IMPACT_MAP
- **I0_identity_relation:** VERIFIED for CCR, AEP, BEC and candidate; intelligence-source relation verified
- **I1_resources_capability:** VERIFIED/PARTIAL for electoral expenditure and online campaign resources; ultimate funding origins incomplete
- **I2_documented_action:** VERIFIED for annulment, finance sanctions, candidacy rejection and formal DSA investigation; digital campaign activity partly documented
- **I3_coordination_tasking:** PARTIAL / NOT_ESTABLISHED for foreign-state sponsor/tasking
- **I4_exposure_reach:** PARTIAL; significant online exposure asserted, but no stable adjudicative denominator comparable to Austria control
- **I5_reception_persuasion:** NOT_ESTABLISHED causally
- **I6_behavior_institutional_economic_change:** VERIFIED for institutional consequences: annulment, restart and later candidacy exclusion; voter behavior causation not established
- **I7_counterfactual_outcome:** NOT_ESTABLISHED
- **downstream:** Feeds INV-102 on consent/choice and INV-129 on lawfare/coercive legal intervention.

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** newly declassified intelligence material triggered ex officio total annulment four days later
  - **issue:** 2 December validation versus 6 December total annulment
  - **pro:** CCR validated first-round result and runoff after rejecting a fraud-based challenge
  - **resolution:** NEW_EVIDENCE_TRIGGER_VERIFIED; whether evidentiary threshold/safeguards were sufficient remains separately assessed
- **item 2:**
  - **contra:** AEP later recorded 591.86 lei expenditure and sanctioned multiple violations
  - **issue:** zero campaign budget reasoning
  - **pro:** Decision 32 relied on reported zero lei and scale incongruity
  - **resolution:** FINANCE_IRREGULARITY_CORROBORATED; exact hidden-funding chain not established
- **item 3:**
  - **contra:** Snoop reported PNL funding and Kensington acknowledgment for the Echilibru si Verticalitate campaign
  - **issue:** foreign-origin inference for one TikTok campaign
  - **pro:** intelligence note described pattern similarity with prior Russian campaign
  - **resolution:** PATTERN_SIMILARITY_NOT_ORIGIN_PROOF; do not generalize domestic funding finding to all online activity
- **item 4:**
  - **contra:** rejection was based on Article 3 Protocol No. 1 scope, not merits
  - **issue:** ECtHR inadmissibility
  - **pro:** application against annulment was rejected
  - **resolution:** NO_MERITS_ENDORSEMENT

### VERIFICATION_REPORT
- **independence_limits:**
  - CCR judgment transmits intelligence-note findings rather than publishing all underlying evidence
  - Snoop PNL-funding item is secondary and partly confidential-source based
  - Austria comparator differs in legal system and irregularity type
- **negative_checks:**
  - 2 December validation retained
  - Venice report not treated as merits reversal
  - ECtHR inadmissibility not treated as merits endorsement
  - PNL control not generalized to all online activity
  - no foreign-state I3 promotion
  - no I5/I7 claim
- **source_families:** 9
- **source_records_complete:** 12/12
- **status:** PASS_WITH_EXPLICIT_GAPS
- **web_fact_trace:** 23/23 facts mapped to accepted FETCH-backed sources

### EDI_REPORT
- **corpus:**
  - **circularity:** LOW_TO_MODERATE
  - **coverage:** CORE_LEGAL_CHAIN_COVERED
  - **independence:** STRONG_PRIMARY_DOMINANCE
  - **limits:**
    - underlying intelligence exhibits not independently reconstructed
    - one domestic-funding contradiction relies on investigative reporting/confidential ANAF source
    - no causal voter-level design
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** EVIDENCE
    - **independent_families:** 3
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** PARTIAL
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 3
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** PARTIAL
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-005
    - **direct_object:** YES_STANDARD
    - **gap_type:** COMPARABILITY
    - **independent_families:** 2
- **diagnostic_not_truth:** true
- **dimensions:**
  - **owner:** 9_PROVENANCE_FAMILIES
  - **perspective:** CCR+AEP+VENICE+ECHR+ODIHR+AUSTRIA+EU_COMMISSION+INVESTIGATIVE_MEDIA
  - **stratification:** DOMESTIC_JUDGMENT+AUDIT+EUROPEAN_STANDARD+COMPARATOR+PLATFORM_PROCEEDING
  - **temporal:** 2016-2026
- **edi:**
  - **assessment:** HIGH_LEGAL_AND_INSTITUTIONAL_COVERAGE_WITH_ATTRIBUTION_AND_CAUSAL_LIMITS
  - **flags:**
    - INTELLIGENCE_EVIDENCE_DEPENDENCE
    - NO_PUBLIC_SPONSOR_TASKING_CHAIN
    - NO_COUNTERFACTUAL_VOTE_MODEL
    - SECONDARY_PNL_FUNDING_CONTROL
    - COMPARATOR_LEGAL_SYSTEM_DIFFERENCE
- **source_counts:**
  - **claim_source:** 0
  - **primary:** 10
  - **provenance_families:** 9
  - **secondary:** 2
  - **total:** 12

### RESPONSIBILITY_MAP
- **item 1:**
  - **highest_supported:** CCR unanimously adopted Decision 32 under its stated constitutional competence
  - **not_supported:** political instrumentalization intent by the Court
  - **object:** annulment decision
  - **support:**
    - FCT-005
    - FCT-010
- **item 2:**
  - **highest_supported:** AEP recorded nonzero expenditure and imposed sanctions
  - **not_supported:** complete hidden-financing chain or foreign principal
  - **object:** campaign-finance violations
  - **support:**
    - FCT-011
    - FCT-012
- **item 3:**
  - **highest_supported:** intelligence notes and EU statements identified serious foreign-interference indications/risks
  - **not_supported:** public edge-by-edge state sponsor/tasking chain sufficient for I3
  - **object:** foreign interference attribution
  - **support:**
    - FCT-004
    - FCT-007
    - FCT-019
    - FCT-022
- **item 4:**
  - **highest_supported:** CCR found significant exposure and distortion; institutional outcome changed
  - **not_supported:** measured persuasion or counterfactual election result
  - **object:** voter/result effect
  - **support:**
    - FCT-008
    - FCT-010
    - FCT-013
    - FCT-017
    - FCT-018

### NEXT_QUERIES
- **item 1:**
  - **query:** authenticated underlying declassified intelligence evidence objects with sponsor/tasking and platform-exposure chain
  - **route:** RECHECK
  - **trigger:** new primary evidence or declassification
- **item 2:**
  - **query:** direct ANAF audit/report on PNL-Kensington Echilibru si Verticalitate funding chain
  - **route:** RECHECK
  - **trigger:** primary report becomes public
- **item 3:**
  - **query:** final merits outcome of Romanian-election-specific TikTok DSA proceeding
  - **route:** RECHECK
  - **trigger:** final Commission decision
- **item 4:**
  - **query:** causal exposure/persuasion design linking identified online irregularity to candidate-order counterfactual
  - **route:** DEFER
  - **trigger:** independent causal dataset

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-007,QRY-008 | support:- | counter:- | results:FCT-001,FCT-002,FCT-004,FCT-006,FCT-010,FCT-011,FCT-013,FCT-017,FCT-018,FCT-021 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-005,QRY-008 | support:- | counter:- | results:FCT-013,FCT-014,FCT-015,FCT-017,FCT-018 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-005 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-013 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-004,QRY-009,QRY-011 | support:- | counter:- | results:FCT-006,FCT-007,FCT-008,FCT-009,FCT-011,FCT-012,FCT-019,FCT-022 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-005,QRY-008 | support:- | counter:- | results:FCT-008,FCT-010,FCT-013,FCT-017,FCT-018 | final:GAP | gap:CAUSALITY
AXS-004 | attempts:QRY-005,QRY-006,QRY-007,QRY-010 | support:- | counter:- | results:FCT-014,FCT-015,FCT-016,FCT-020,FCT-021 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-009,QRY-011 | support:- | counter:- | results:FCT-004,FCT-007,FCT-019,FCT-022 | final:GAP | gap:RESPONSIBILITY
AXS-006 | attempts:QRY-001,QRY-007,QRY-010,QRY-012 | support:- | counter:- | results:FCT-010,FCT-020,FCT-021,FCT-023 | final:GAP | gap:INTENT
CLM-001 | attempts:QRY-001,SRC-001 | support:FCT-004,FCT-005,FCT-006,FCT-007,FCT-010 | counter:CTRL-001;CTRL-002 | results:FCT-004,FCT-005,FCT-006,FCT-007,FCT-010,CTRL-001;CTRL-002 | final:SUPPORTED | gap:EVIDENCE
CLM-002 | attempts:QRY-001,QRY-004,SRC-001,SRC-004 | support:FCT-009,FCT-011,FCT-012 | counter:CTRL-004 | results:FCT-009,FCT-011,FCT-012,CTRL-004 | final:SUPPORTED | gap:RESPONSIBILITY
CLM-003 | attempts:QRY-001,QRY-009,QRY-011,SRC-001,SRC-009,SRC-011 | support:FCT-004,FCT-007,FCT-019,FCT-022 | counter:CTRL-002;CTRL-005 | results:FCT-004,FCT-007,FCT-019,FCT-022,CTRL-002;CTRL-005 | final:PARTIAL | gap:RESPONSIBILITY
CLM-004 | attempts:QRY-001,QRY-005,QRY-008,SRC-001,SRC-005,SRC-008 | support:FCT-008,FCT-013,FCT-017,FCT-018 | counter:CTRL-003 | results:FCT-008,FCT-013,FCT-017,FCT-018,CTRL-003 | final:PARTIAL | gap:CAUSALITY
CLM-005 | attempts:QRY-005,SRC-005 | support:FCT-013,FCT-014,FCT-015 | counter:CTRL-001 | results:FCT-013,FCT-014,FCT-015,CTRL-001 | final:SUPPORTED | gap:COMPARABILITY
CLM-006 | attempts:QRY-001,QRY-007,QRY-010,SRC-001,SRC-007,SRC-010 | support:FCT-010,FCT-020,FCT-021 | counter:CTRL-001;CTRL-006 | results:FCT-010,FCT-020,FCT-021,CTRL-001;CTRL-006 | final:PARTIAL | gap:INTENT

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
AXS-003 | AXS | GAP | CAUSALITY | Romanian published decision provides no quantified affected-vote denominator or causal design comparable to Austria 2016; actual counterfactual result remains unresolved.
AXS-005 | AXS | GAP | RESPONSIBILITY | Decision 32 does not itself establish a public edge-by-edge foreign-state sponsor/tasking chain; one reported TikTok campaign has a material domestic-funding contradiction.
AXS-006 | AXS | GAP | INTENT | Institutional effects are verified, but evidence proving that Romanian authorities intentionally used the process to suppress a candidate rather than apply their legal interpretation is not established.
CLM-001 | CLM | SUPPORTED | EVIDENCE | The public judgment is strongest as proof of the court finding and remedy, not as independent validation of every intelligence allegation.
CLM-002 | CLM | SUPPORTED | RESPONSIBILITY | The audit does not identify a complete hidden-financing chain or foreign sponsor for the full online campaign.
CLM-003 | CLM | PARTIAL | RESPONSIBILITY | Underlying intelligence evidence, platform data and sponsor/tasking records remain incomplete in the public record used here.
CLM-004 | CLM | PARTIAL | CAUSALITY | Online exposure and irregularity may justify concern, but persuasion and counterfactual candidate ordering are not measured in the examined adjudicative record.
CLM-005 | CLM | SUPPORTED | COMPARABILITY | The Venice Commission expressly did not decide the Romanian merits; it provides a standard, not a binding reversal of Decision 32.
CLM-006 | CLM | PARTIAL | INTENT | No direct evidence in the examined corpus proves that decision-makers used the legal process with the purpose of suppressing Georgescu rather than applying their stated constitutional interpretation.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | I4 exposure is partial; I5 persuasion and I7 counterfactual outcome are not established; I3 foreign-state tasking remains partial/unestablished.

SEMANTIC_COUNTS_V1:LED:2|CLM:6|AXS:6|CAU:1|CTRL:6|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-007","QRY-008"],"evidence_excerpt":"The public record closes the legal act and some finance violations strongly while leaving sponsor/tasking, persuasion and counterfactual result edges open.","kind":"HYPOTHESIS","lead":"Romania 2024 is a discriminating case for separating legal annulment, evidentiary sufficiency, foreign attribution, institutional effect and political instrumentalization.","linked_ids":["CLM-001","CLM-003","CLM-004","CLM-006"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-004","FCT-006","FCT-010","FCT-011","FCT-013","FCT-017","FCT-018","FCT-021"],"routes":["LEGAL_BASIS","CAUSALITY","RESPONSIBILITY","DUE_PROCESS"],"source_id":"INV-100_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-005","QRY-008"],"evidence_excerpt":"Austria demonstrates potential-influence annulment after proven violations and a quantified affected-vote universe; Venice requires high threshold, reasoned facts and safeguards.","kind":"METHOD_CONSTRAINT","lead":"Annulment must be tested against an isomorphic comparator rather than against the impossible demand for proof of actual manipulation; Austria 2016 supplies that control while Venice standards bound evidentiary and procedural safeguards.","linked_ids":["CLM-004","CLM-005"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-013","FCT-014","FCT-015","FCT-017","FCT-018"],"routes":["COMPARATOR","CONTROL","PROCEDURE"],"source_id":"INV-100_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Romania 6 December 2024 presidential-election annulment is a verified legal act resting on the Constitutional Court broad reading of its constitutional supervisory competence and on declassified intelligence-note findings of digital, fairness and campaign-finance irregularities.","claimant":"INV-100 synthesis","counter":"CTRL-001;CTRL-002","gap":"The public judgment is strongest as proof of the court finding and remedy, not as independent validation of every intelligence allegation.","gap_type":"EVIDENCE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-005","FCT-006","FCT-007","FCT-010"]}
CLM-002 | {"claim":"Campaign-finance irregularity is independently corroborated beyond Decision 32 because the AEP later recorded nonzero electoral expenditure and imposed multiple sanctions.","claimant":"INV-100 synthesis","counter":"CTRL-004","gap":"The audit does not identify a complete hidden-financing chain or foreign sponsor for the full online campaign.","gap_type":"RESPONSIBILITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-009","FCT-011","FCT-012"]}
CLM-003 | {"claim":"The public record examined does not establish an edge-by-edge foreign-state sponsor -> tasking -> operator chain sufficient to treat the annulment as proof of Russian or other foreign state control of the decisive campaign mechanisms.","claimant":"INV-100 synthesis","counter":"CTRL-002;CTRL-005","gap":"Underlying intelligence evidence, platform data and sponsor/tasking records remain incomplete in the public record used here.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-004","FCT-007","FCT-019","FCT-022"]}
CLM-004 | {"claim":"The published Romanian decision does not establish the counterfactual electoral outcome with a quantified affected-vote denominator or causal design comparable to Austria 2016; voter persuasion and result change therefore remain unestablished.","claimant":"INV-100 synthesis","counter":"CTRL-003","gap":"Online exposure and irregularity may justify concern, but persuasion and counterfactual candidate ordering are not measured in the examined adjudicative record.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-008","FCT-013","FCT-017","FCT-018"]}
CLM-005 | {"claim":"European comparative standards support annulment only as an exceptional remedy with a high potential-effect threshold, clear evidence and procedural safeguards; classified intelligence alone should not carry the decision.","claimant":"INV-100 synthesis","counter":"CTRL-001","gap":"The Venice Commission expressly did not decide the Romanian merits; it provides a standard, not a binding reversal of Decision 32.","gap_type":"COMPARABILITY","materiality":"HIGH","status":"SUPPORTED","support":["FCT-013","FCT-014","FCT-015"]}
CLM-006 | {"claim":"The institutional consequences are verified: the 2024 process was annulled and restarted, Georgescu 2025 candidacy was later rejected, and ODIHR identified legal-certainty and due-process concerns; political instrumentalization intent by Romanian institutions is not established by these effects alone.","claimant":"INV-100 synthesis","counter":"CTRL-001;CTRL-006","gap":"No direct evidence in the examined corpus proves that decision-makers used the legal process with the purpose of suppressing Georgescu rather than applying their stated constitutional interpretation.","gap_type":"INTENT","materiality":"HIGH","status":"PARTIAL","support":["FCT-010","FCT-020","FCT-021"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-005"],"axis":"LEGAL_BASIS_AND_TRIGGER","links":["CCR_H32"],"question":"What legal competence and trigger supported the 6 December annulment after the 2 December validation?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-013"],"sought_objects":["LEGAL_BASIS","EX_OFFICIO_TRIGGER","REVISION"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-004","QRY-009","QRY-011"],"axis":"EVIDENTIARY_BASIS","links":["CCR_H32","AEP_R4471"],"question":"Which irregularities were established directly and which were transmitted through intelligence assessments?","result_ids":["FCT-006","FCT-007","FCT-008","FCT-009","FCT-011","FCT-012","FCT-019","FCT-022"],"sought_objects":["EVIDENCE","INTELLIGENCE_NOTE","CAMPAIGN_FINANCE","DIGITAL_ACTIVITY"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-005","QRY-008"],"axis":"OUTCOME_CAUSALITY","gap":"Romanian published decision provides no quantified affected-vote denominator or causal design comparable to Austria 2016; actual counterfactual result remains unresolved.","gap_type":"CAUSALITY","links":["ROMANIA_CASE","AUSTRIA_CONTROL"],"question":"Does the evidence show that the irregularities could or did change the candidate ordering or final electoral outcome?","result_ids":["FCT-008","FCT-010","FCT-013","FCT-017","FCT-018"],"sought_objects":["EXPOSURE","PERSUASION","VOTE_EFFECT","COUNTERFACTUAL"],"status":"GAP"}
AXS-004 | {"attempt_ids":["QRY-005","QRY-006","QRY-007","QRY-010"],"axis":"PROCEDURAL_SAFEGUARDS","links":["VENICE_STANDARD","ODIHR_FOLLOWUP"],"question":"What hearing, adversarial participation, reasoning and remedy safeguards accompanied annulment and later candidacy exclusion?","result_ids":["FCT-014","FCT-015","FCT-016","FCT-020","FCT-021"],"sought_objects":["HEARING","PARTICIPATION","REASONING","APPEAL","DUE_PROCESS"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-009","QRY-011"],"axis":"FOREIGN_ATTRIBUTION","gap":"Decision 32 does not itself establish a public edge-by-edge foreign-state sponsor/tasking chain; one reported TikTok campaign has a material domestic-funding contradiction.","gap_type":"RESPONSIBILITY","links":["INTELLIGENCE_NOTES","PNL_CONTROL"],"question":"Can the annulment evidence close a chain from foreign state sponsor to tasking and operation rather than only describing suspicious patterns or foreign-interference risk?","result_ids":["FCT-004","FCT-007","FCT-019","FCT-022"],"sought_objects":["SPONSOR","TASKING","OPERATOR","ATTRIBUTION"],"status":"GAP"}
AXS-006 | {"attempt_ids":["QRY-001","QRY-007","QRY-010","QRY-012"],"axis":"INSTITUTIONAL_EFFECT_AND_INTENT","gap":"Institutional effects are verified, but evidence proving that Romanian authorities intentionally used the process to suppress a candidate rather than apply their legal interpretation is not established.","gap_type":"INTENT","links":["CCR_H32","CCR_H7","ODIHR"],"question":"Which institutional consequences are proven, and is political instrumentalization intent proven?","result_ids":["FCT-010","FCT-020","FCT-021","FCT-023"],"sought_objects":["ANNULMENT","CANDIDACY_REJECTION","REPEAT_ELECTION","INTENT"],"status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"Underlying intelligence assertions, domestic-campaign contradiction, unmeasured persuasion, judicial discretion and ordinary legal-remedy explanations can break or confound several links.","gap":"I4 exposure is partial; I5 persuasion and I7 counterfactual outcome are not established; I3 foreign-state tasking remains partial/unestablished.","gap_type":"CAUSALITY","limit":"Institutional effects are directly verified; voter persuasion and counterfactual election outcome are not, and foreign-state tasking is not closed in the public adjudicative record.","mechanism":"alleged/verified irregularity -> evidence -> legal finding -> annulment/candidacy consequence -> changed electoral opportunity -> possible voter/competition effect -> counterfactual outcome","status":"UNRESOLVED","support":["FCT-006","FCT-008","FCT-010","FCT-013","FCT-017","FCT-018","FCT-020","FCT-021"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Legal-annulment control: a court-annulled election is not thereby proven to be an illegitimate institutional interference; legal basis, evidence threshold, safeguards and remedy must be tested separately.","status":"DONE","support":["FCT-005","FCT-010","FCT-013","FCT-014","FCT-015"]}
CTRL-002 | {"control":"Authority-source control: Decision 32 proves what the Constitutional Court held and relied on, but it does not automatically prove the underlying intelligence assessments true or close a foreign-state attribution chain.","status":"DONE","support":["FCT-004","FCT-006","FCT-007","FCT-015","FCT-019"]}
CTRL-003 | {"control":"Outcome control: Austria 2016 shows actual manipulation need not be proven when concrete legal violations and a quantified affected-vote universe are sufficient to show potential influence; Romania therefore cannot be judged by an impossible actual-causation standard.","status":"DONE","support":["FCT-013","FCT-017","FCT-018"]}
CTRL-004 | {"control":"Campaign-finance control: the later AEP audit independently establishes nonzero expenditure and sanctionable campaign-finance violations, but does not establish the full intelligence narrative, hidden sponsor identity or foreign command.","status":"DONE","support":["FCT-009","FCT-011","FCT-012"]}
CTRL-005 | {"control":"Domestic-funding contradiction: Snoop reporting on PNL funding of one TikTok campaign materially weakens origin-by-pattern inference for that campaign, but cannot be generalized to every Georgescu online network or exclude separate foreign activity.","status":"DONE","support":["FCT-007","FCT-022"]}
CTRL-006 | {"control":"ECtHR control: Georgescu v Romania inadmissibility was jurisdictional under Article 3 Protocol No. 1 and is not a merits endorsement of Decision 32.","status":"DONE","support":["FCT-016"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:12|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | MNEMO_Q | MNEMO_Q subject_fingerprint
SYS-003 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | MNEMO_Q | MNEMO_Q
SYS-004 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | PASS | SRC-001 | https://legislatie.just.ro/Public/FormaPrintabila/00000G2OH5FWE05C8WF3A5SI29IWJBGG | Romanian Constitutional Court Decision 32 6 December 2024 annul presidential election declassified intelligence notes
QRY-002 | FETCH | PASS | SRC-002 | https://legislatie.just.ro/public/DetaliiDocument/291969 | Romanian Constitutional Court Decision 31 2 December 2024 validates first round and runoff Georgescu Lasconi
QRY-003 | FETCH | PASS | SRC-003 | https://legislatie.just.ro/public/DetaliiDocument/292331 | Romanian Constitutional Court Decision 30 Terhes annulment request fraud threshold 2 December 2024
QRY-004 | FETCH | PASS | SRC-004 | https://legislatie.just.ro/public/DetaliiDocument/299977 | AEP report 4471 Calin Georgescu campaign contributions expenditures sanctions 2025
QRY-005 | FETCH | PASS | SRC-005 | https://www.venice.coe.int/webforms/documents/default.aspx?pdffile=CDL-AD%282025%29003-e | Venice Commission urgent report cancellation election results constitutional courts Romania 2025
QRY-006 | FETCH | PASS | SRC-006 | https://www.echr.coe.int/w/inadmissiblity-decision-concerning-romania-1 | ECtHR Calin Georgescu Romania inadmissibility annulment presidential election 6 March 2025
QRY-007 | FETCH | PASS | SRC-007 | https://odihr.osce.org/odihr/elections/romania/600295 | ODIHR final report repeat Romanian presidential election 2025 dispute resolution candidate eligibility
QRY-008 | FETCH | PASS | SRC-008 | https://www.vfgh.gv.at/timeline/2016__Bundespraesidentenstichwahl.en.html | Austrian Constitutional Court 2016 presidential runoff annulment 77000 postal votes 30000 margin
QRY-009 | FETCH | PASS | SRC-009 | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | European Commission TikTok formal proceedings Romanian election risks 17 December 2024 DSA
QRY-010 | FETCH | PASS | SRC-010 | https://legislatie.just.ro/public/DetaliiDocument/295597 | Romanian Constitutional Court Decision 7 11 March 2025 Georgescu candidacy rejection repeat election
QRY-011 | FETCH | PASS | SRC-011 | https://snoop.ro/anaf-a-descoperit-ca-pnl-a-platit-o-campanie-care-l-a-promovat-masiv-pe-calin-georgescu-pe-tiktok/ | Snoop ANAF PNL funded Echilibru si Verticalitate TikTok Calin Georgescu campaign December 2024
QRY-012 | FETCH | PASS | SRC-012 | https://agerpres.ro/news-alert/2026/08/06/iccj-dispune-inceperea-judecatii-pe-fond-in-dosarul-georgescu---gruparea-potra--1582763 | ICCJ August 2026 Georgescu Potra trial merits begins constitutional order charges status

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:romania-ccr | CCR-H32-2024 | Hotararea nr. 32 din 6 decembrie 2024 privind anularea procesului electoral | 2024-12-06 | 2026-09-07T07:58:00+00:00 | paras 1,3-17 and operative part | https://legislatie.just.ro/Public/FormaPrintabila/00000G2OH5FWE05C8WF3A5SI29IWJBGG
SRC-002 | ◈ | fam:other:romania-ccr | CCR-H31-2024 | Hotararea nr. 31 din 2 decembrie 2024 privind rezultatul primului tur | 2024-12-02 | 2026-09-07T07:58:00+00:00 | paras 4-12 and operative part | https://legislatie.just.ro/public/DetaliiDocument/291969
SRC-003 | ◈ | fam:other:romania-ccr | CCR-H30-2024 | Hotararea nr. 30 din 2 decembrie 2024 privind cererea de anulare Terhes | 2024-12-02 | 2026-09-07T07:58:00+00:00 | request, statutory fraud threshold, rejection | https://legislatie.just.ro/public/DetaliiDocument/292331
SRC-004 | ◈ | fam:other:romania-aep | AEP-R4471-2025 | Raport nr. 4.471 din 5 martie 2025 privind veniturile si cheltuielile electorale Calin Georgescu | 2025-07-23 | 2026-09-07T07:58:00+00:00 | control period, findings, sanctions | https://legislatie.just.ro/public/DetaliiDocument/299977
SRC-005 | ◈ | fam:other:venice-commission | CDL-AD-2025-003 | Urgent Report on the Cancellation of Election Results by Constitutional Courts CDL-AD(2025)003 | 2025-03-18 | 2026-09-07T07:58:00+00:00 | paras 27-42, 56-59, 71-78 | https://www.venice.coe.int/webforms/documents/default.aspx?pdffile=CDL-AD%282025%29003-e
SRC-006 | ◈ | fam:other:echr | ECHR-GEORGESCU-2025-03-06 | Inadmissibility decision concerning Romania - Calin Georgescu v Romania | 2025-03-06 | 2026-09-07T07:58:00+00:00 | inadmissibility rationale under Article 3 Protocol No. 1 | https://www.echr.coe.int/w/inadmissiblity-decision-concerning-romania-1
SRC-007 | ◈ | fam:other:osce-odihr | ODIHR-ROMANIA-2025-FINAL | Romania Repeat Presidential Election 4 and 18 May 2025 Final Report | 2025-10-28 | 2026-09-07T07:58:00+00:00 | executive summary and recommendations on eligibility/disputes | https://odihr.osce.org/odihr/elections/romania/600295
SRC-008 | ◈ | fam:other:austria-vfgh | VFGH-WI6-2016 | 2016 Run-off Election of the Federal President | 2016-07-01 | 2026-09-07T07:58:00+00:00 | hearing, 77,000 affected votes, ~30,000 margin, potential influence test | https://www.vfgh.gv.at/timeline/2016__Bundespraesidentenstichwahl.en.html
SRC-009 | ◈ | fam:other:eu-commission | EC-TIKTOK-ROMANIA-2024-12-17 | Commission opens formal proceedings against TikTok on election risks under the DSA | 2024-12-17 | 2026-09-07T07:58:00+00:00 | suspected DSA breach; recommender systems and paid political content | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act
SRC-010 | ◈ | fam:other:romania-ccr | CCR-H7-2025 | Hotararea nr. 7 din 11 martie 2025 privind candidatura Calin Georgescu | 2025-03-11 | 2026-09-07T07:58:00+00:00 | challenge to BEC Decision 18D; operative rejection | https://legislatie.just.ro/public/DetaliiDocument/295597
SRC-011 | ◉ | fam:other:media-snoop | SNOOP-PNL-TIKTOK-2024-12-20 | ANAF a descoperit ca PNL a platit o campanie care l-a promovat masiv pe Calin Georgescu pe TikTok | 2024-12-20 | 2026-09-07T07:58:00+00:00 | ANAF-source claim, Kensington confirmation, campaign mechanics and caveat | https://snoop.ro/anaf-a-descoperit-ca-pnl-a-platit-o-campanie-care-l-a-promovat-masiv-pe-calin-georgescu-pe-tiktok/
SRC-012 | ◉ | fam:other:media-agerpres | AGERPRES-GEORGESCU-POTRA-2026-08-06 | ICCJ dispune inceperea judecatii pe fond in dosarul Georgescu - gruparea Potra | 2026-08-06 | 2026-09-07T07:58:00+00:00 | trial-start status and charges; no conviction | https://agerpres.ro/news-alert/2026/08/06/iccj-dispune-inceperea-judecatii-pe-fond-in-dosarul-georgescu---gruparea-potra--1582763

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://legislatie.just.ro/public/DetaliiDocument/292331 | other:romania-ccr | 2024-12-02 | CCR pre-annulment challenge | On 2 December 2024 the Romanian Constitutional Court rejected Cristian-Vasile Terhes request to annul the first-round presidential election under the statutory fraud threshold requiring fraud capable of changing the mandate allocation or runoff candidate order. | -
FCT-002 | FACT | ✧ | https://legislatie.just.ro/public/DetaliiDocument/291969 | other:romania-ccr | 2024-12-02 | CCR validation of first round | On 2 December 2024 the Court confirmed and validated the 24 November first-round result and ordered a runoff on 8 December between Calin Georgescu, with 2,120,401 votes, and Elena Lasconi, with 1,772,500 votes. | -
FCT-003 | FACT | ✧ | https://legislatie.just.ro/public/DetaliiDocument/291969 | other:romania-ccr | 2024-12-02 | CCR protocol irregularities finding | In validating the result, the Court stated that the voting-result protocols did not reveal irregularities capable of invalidating the established result. | -
FCT-004 | FACT | ✧ | https://legislatie.just.ro/Public/FormaPrintabila/00000G2OH5FWE05C8WF3A5SI29IWJBGG | other:romania-ccr | 2024-12-04 | Declassified intelligence notes | Decision 32 records that intelligence notes from MAI-DGPI, SIE, SRI and STS were declassified and made public on 4 December 2024, after the Court had validated the first-round result on 2 December. | -
FCT-005 | FACT | ✧ | https://legislatie.just.ro/Public/FormaPrintabila/00000G2OH5FWE05C8WF3A5SI29IWJBGG | other:romania-ccr | 2024-12-06 | CCR ex officio constitutional competence | In Decision 32 the Court relied on Article 146(f) of the Constitution and interpreted its duty to oversee the presidential-election procedure as non-restrictive and connected to its role as guarantor of constitutional supremacy. | -
FCT-006 | FACT | ✧ | https://legislatie.just.ro/Public/FormaPrintabila/00000G2OH5FWE05C8WF3A5SI29IWJBGG | other:romania-ccr | 2024-12-06 | CCR finding of systemic electoral irregularities | After taking note of the declassified intelligence notes, the Court found the electoral process vitiated throughout by multiple irregularities and electoral-law violations affecting free and fair voting, equality of opportunity, campaign transparency and campaign-finance rules. | -
FCT-007 | FACT | ✧ | https://legislatie.just.ro/Public/FormaPrintabila/00000G2OH5FWE05C8WF3A5SI29IWJBGG | other:romania-ccr | 2024-12-06 | Digital and financing grounds stated by CCR | The Court stated, according to the intelligence notes, that key issues included voter manipulation and unequal opportunity through non-transparent and unlawful use of digital technologies and artificial intelligence, together with campaign financing from undeclared sources including online. | -
FCT-008 | FACT | ✧ | https://legislatie.just.ro/Public/FormaPrintabila/00000G2OH5FWE05C8WF3A5SI29IWJBGG | other:romania-ccr | 2024-12-06 | Online promotion findings stated by CCR | The Court found that one candidate benefited from aggressive promotion that bypassed national electoral rules, abusive exploitation of social-media algorithms, unlabeled electoral promotional materials and preferential treatment on social platforms. | -
FCT-009 | FACT | ✧ | https://legislatie.just.ro/Public/FormaPrintabila/00000G2OH5FWE05C8WF3A5SI29IWJBGG | other:romania-ccr | 2024-12-06 | CCR campaign finance reasoning | The Court noted a declared campaign budget of zero lei and held that this conflicted with intelligence-note data and with the evident scale of the campaign, creating an obvious incongruity and breaching campaign-finance transparency. | -
FCT-010 | FACT | ✧ | https://legislatie.just.ro/Public/FormaPrintabila/00000G2OH5FWE05C8WF3A5SI29IWJBGG | other:romania-ccr | 2024-12-06 | Total annulment and restart | Decision 32 annulled the entire 2024 presidential electoral process, including votes already cast for the second round, and ordered the process to restart in full with new candidacies and a new campaign. | -
FCT-011 | FACT | ✧ | https://legislatie.just.ro/public/DetaliiDocument/299977 | other:romania-aep | 2025-03-05 | AEP Georgescu campaign audit | The Permanent Electoral Authority audit recorded zero electoral contributions and 591.86 lei of electoral expenditure for Calin Georgescu 2024 presidential campaign. | -
FCT-012 | FACT | ✧ | https://legislatie.just.ro/public/DetaliiDocument/299977 | other:romania-aep | 2025-03-05 | AEP sanctions | The Permanent Electoral Authority imposed multiple fines and a warning on Georgescu for breaches of several provisions of Law 334/2006 governing campaign financing. | -
FCT-013 | FACT | ✧ | https://www.venice.coe.int/webforms/documents/default.aspx?pdffile=CDL-AD%282025%29003-e | other:venice-commission | 2025-03-18 | Venice Commission outcome threshold | The Venice Commission stated that election cancellation should be exceptional and based on clearly established significant irregularities; it is not necessary to prove actual effect, but it must be shown convincingly that the result could have been different without the irregularities and the annulment threshold should be high. | -
FCT-014 | FACT | ✧ | https://www.venice.coe.int/webforms/documents/default.aspx?pdffile=CDL-AD%282025%29003-e | other:venice-commission | 2025-03-18 | Venice Commission procedural safeguards | For ex officio annulment, the Venice Commission stated that some form of hearing or consultation with affected parties must be provided so they can submit views and evidence, and the decision must be fair, objective, reasoned and bounded by law. | -
FCT-015 | FACT | ✧ | https://www.venice.coe.int/webforms/documents/default.aspx?pdffile=CDL-AD%282025%29003-e | other:venice-commission | 2025-03-18 | Venice Commission intelligence evidence rule | For online and social-media violations, the Venice Commission stated that cancellation decisions should precisely identify violations and evidence and must not be based solely on classified intelligence, which may be used only as contextual information. | -
FCT-016 | FACT | ✧ | https://www.echr.coe.int/w/inadmissiblity-decision-concerning-romania-1 | other:echr | 2025-03-06 | ECtHR Georgescu inadmissibility | The European Court of Human Rights declared Georgescu application inadmissible because the Romanian presidency was not shown to form part of the legislature for Article 3 of Protocol No. 1; the decision therefore did not adjudicate the substantive merits of the Romanian Constitutional Court annulment. | -
FCT-017 | FACT | ✧ | https://www.vfgh.gv.at/timeline/2016__Bundespraesidentenstichwahl.en.html | other:austria-vfgh | 2016-07-01 | Austria 2016 annulment comparator | The Austrian Constitutional Court annulled the 2016 presidential runoff after a public multi-day hearing and evidence from 90 witnesses established postal-vote counting violations in 14 constituencies affecting about 77,000 votes, compared with an approximately 30,000-vote margin. | -
FCT-018 | FACT | ✧ | https://www.vfgh.gv.at/timeline/2016__Bundespraesidentenstichwahl.en.html | other:austria-vfgh | 2016-07-01 | Austria potential influence standard | The Austrian Court applied its longstanding rule that proven violations of provisions designed to prevent abuse justify annulment when the number of affected votes is large enough potentially to influence the result, without requiring proof that manipulation actually occurred. | -
FCT-019 | FACT | ✧ | https://digital-strategy.ec.europa.eu/en/news/commission-opens-formal-proceedings-against-tiktok-election-risks-under-digital-services-act | other:eu-commission | 2024-12-17 | EU TikTok proceedings | The European Commission opened formal DSA proceedings against TikTok for a suspected breach of election-risk obligations in the Romanian election, focusing on recommender-system risks, coordinated inauthentic manipulation and paid political content; the opening was an investigation, not a final merits finding. | -
FCT-020 | FACT | ✧ | https://legislatie.just.ro/public/DetaliiDocument/295597 | other:romania-ccr | 2025-03-11 | Georgescu repeat-election candidacy rejection | On 11 March 2025 the Romanian Constitutional Court rejected challenges to BEC Decision 18D refusing registration of Calin Georgescu candidacy for the repeat presidential election; the ruling was final. | -
FCT-021 | FACT | ✧ | https://odihr.osce.org/odihr/elections/romania/600295 | other:osce-odihr | 2025-10-28 | ODIHR repeat-election assessment | ODIHR reported that the May 2025 repeat election was efficiently managed and voters had genuine choice, but criticized candidate-eligibility requirements based on court rulings rather than clear legal provisions and recommended stronger due-process and dispute-resolution safeguards. | -
FCT-022 | FACT | ✧ | https://snoop.ro/anaf-a-descoperit-ca-pnl-a-platit-o-campanie-care-l-a-promovat-masiv-pe-calin-georgescu-pe-tiktok/ | other:media-snoop | 2024-12-20 | Echilibru si Verticalitate funding contradiction | Snoop reported, citing a confidential source familiar with an ANAF control and correspondence with Kensington Communication, that PNL money funded the Echilibru si Verticalitate TikTok campaign; Kensington acknowledged PNL paid for a campaign but said its original campaign had been modified without its involvement. | -
FCT-023 | FACT | ✧ | https://agerpres.ro/news-alert/2026/08/06/iccj-dispune-inceperea-judecatii-pe-fond-in-dosarul-georgescu---gruparea-potra--1582763 | other:media-agerpres | 2026-08-06 | Georgescu Potra criminal case status | On 6 August 2026 AGERPRES reported that the High Court allowed the Georgescu-Potra case to proceed to trial on the merits after preliminary objections were rejected; this procedural step is not a conviction and concerns alleged post-annulment conduct among other charges. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-003
FCT-002 | SRC-002
FCT-003 | SRC-002
FCT-004 | SRC-001
FCT-005 | SRC-001
FCT-006 | SRC-001
FCT-007 | SRC-001
FCT-008 | SRC-001
FCT-009 | SRC-001
FCT-010 | SRC-001
FCT-011 | SRC-004
FCT-012 | SRC-004
FCT-013 | SRC-005
FCT-014 | SRC-005
FCT-015 | SRC-005
FCT-016 | SRC-006
FCT-017 | SRC-008
FCT-018 | SRC-008
FCT-019 | SRC-009
FCT-020 | SRC-010
FCT-021 | SRC-007
FCT-022 | SRC-011
FCT-023 | SRC-012

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

## CHECKPOINT_LOG_V1
CP-001 | SCOPE | PASS | LAST_COMPLETED:scope and six forensic axes fixed | NEXT_ACTION:SEARCH
CP-002 | SEARCH | PASS | LAST_COMPLETED:SEARCH corpus: 12 accepted sources, 23 facts | NEXT_ACTION:FACT_VERIFICATION
CP-003 | FACTS | PASS | LAST_COMPLETED:FACTS 23 facts and terminal leads | NEXT_ACTION:CAUSAL_ANALYSIS
CP-004 | CAUSAL_GAP | PASS | LAST_COMPLETED:CAUSAL_GAP causal chain bounded | NEXT_ACTION:VERIFY
CP-005 | VERIFY | PASS | LAST_COMPLETED:VERIFY source, contradiction and comparator review complete | NEXT_ACTION:INVESTIGATION_ACCOUNTABILITY
CP-006 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:INVESTIGATION_ACCOUNTABILITY actors, responsibility and gaps bounded | NEXT_ACTION:FINALIZATION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-07T08:38:49.286794+00:00","fact_mem":{},"mnemo_row":"FAIL:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":23,"eligible":23,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:FAIL:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:23;attempted:0;success:0;failure:0;blocked:23} | WRITEBACK_EXECUTION_V1:[23 rows, see section]

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
