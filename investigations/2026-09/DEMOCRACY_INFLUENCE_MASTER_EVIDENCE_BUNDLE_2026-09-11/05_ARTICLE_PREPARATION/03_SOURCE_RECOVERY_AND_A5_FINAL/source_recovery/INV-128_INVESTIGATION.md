ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-1732-influence-for-hire | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth-engine/investigations/2026-09/2026-09-06_influence-for-hire/2026-09-06_17-32_influence-for-hire_INPUT.txt | SUBJECT_SLUG:influence-for-hire | SUBJECT_FP:sha256:13bd3ee080e9c94bc48430b5fda76040a76afdc26a4ec29497a4f3481471b328 | INPUT_SHA256:sha256:0d7909dfd828e3c222322bdf7365c5cb511a5b8c5537b28e2b04fd4c501a8f0e
COMPLEXITY:8→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:2010–2026; priority France/Europe; private influence-for-hire; client→provider→action→target→exposure/effect; exclude ordinary declared lobbying/PR and unattributed cybercrime.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "truth_engine_investigation"
artifact_id: "INV-128"
run_id: "20260906-1732-influence-for-hire"
status: "final_candidate"
updated: "2026-09-06"
---

<!-- TRACE: source=INV-128_RUN_CARD; runtime=Truth_Engine_2.10.6_R3P1 -->
<!-- DECISION: operation-first; capability!=use!=client!=reach!=effect -->

# INV-128 — Influence-for-hire

## Verdict exécutif

Le marché privé de l’**influence-for-hire** est réel et documenté. Des prestataires commerciaux ont fourni ou proposé des dispositifs combinant faux profils, amplification trompeuse, faux médias, ciblage politique, renseignement privé et, dans certains cas, piratage, infiltration, placement médiatique ou pression réputationnelle. Le phénomène n’est ni exclusivement étatique, ni exclusivement étranger : `CLM-001`, `CLM-002` et `CLM-007` sont soutenus.

Le résultat le plus important est cependant négatif : **il n’existe pas de raccourci probatoire entre capacité, contrat, opération, audience et succès**. Les trois familles de cas se ferment à des étages différents. Team Jorge est fort sur la capacité démontrée et certaines actions observées, mais beaucoup plus faible sur les clients et les succès électoraux revendiqués. STOIC/Zero Zeno est solidement attribué au niveau opérateur/action, mais sa portée authentique mesurée est faible et le lien exact avec le ministère israélien reste publiquement contesté. Alp Services fournit la chaîne client-paiement-prestataire-tasking la plus dense du corpus ouvert, mais le prestataire conteste la base documentaire et plusieurs effets revendiqués apparaissent surjoués. `CLM-003..006`.

Conséquence : **une opération existe peut être un fait ; qu’elle ait changé un vote, une élection ou une politique reste une autre proposition**. `CAU-001` et `CAU-002` restent `UNRESOLVED`.

## 1. Objet et méthode

Question : quels services clandestins peuvent être achetés, et jusqu’où peut-on reconstruire `client → prestataire → action → cible → exposition → effet` ?

Le run applique la chaîne I0-I7 du METHOD_PACK : identité/relation, ressources/capacité, action, tasking/contrôle, exposition, réception, changement puis contrefactuel. Les affirmations commerciales, les attributions de plateformes, les fuites documentaires, les démentis et les procédures judiciaires sont gardés dans leur statut propre.

Le corpus comporte 16 sources inspectées, 8 familles éditoriales/techniques amont, 21 faits et quatre contrôles adversariaux. La diversité brute surestime toutefois l’indépendance : Reuters relaie ici une attribution Meta ; Guardian et Le Monde participent au même consortium Story Killers ; Mediapart et EIC exploitent le même corpus Abu Dhabi Secrets. Cette circularité est explicitement conservée dans `EDI_REPORT`.

## 2. Le marché : existence et mécanismes

Meta décrit depuis 2021 des opérations d’influence coordonnées, étrangères **et domestiques**, conduites non seulement par des gouvernements mais aussi par des entités commerciales et politiques (`FCT-001`). Archimedes Group fournit un cas commercial ancien : réseau trompeur multi-pays lié par Meta à une entreprise israélienne, avec millions de followers de pages et dépenses publicitaires mesurables (`FCT-002`, `FCT-003`). Rally Forge fournit le contrôle miroir : une firme de marketing américaine liée à une campagne trompeuse orientée principalement vers un public américain, pour des clients américains (`FCT-004`, `FCT-005`).

La catégorie pertinente n’est donc pas « étranger » mais **prestataire + mécanisme + relation de commande + cible + effet**. Le caractère étranger peut transformer la qualification juridique ou politique ; il ne crée pas à lui seul le mécanisme.

Meta ajoute un garde-fou particulièrement matériel (`FCT-006`) : les prestataires privés peuvent fournir de la dénégation plausible à leurs clients, tout en ayant intérêt à exagérer leur propre efficacité auprès de ceux qui les paient. Cette double incitation rend les présentations commerciales intrinsèquement adversariales.

## 3. Team Jorge : capacité forte, palmarès faible

Le consortium Story Killers a documenté sous couverture une offre de services associant hacking, sabotage, faux profils, automatisation et placement médiatique (`FCT-012`). Ce matériau établit une **capacité offerte et démontrée** ; il n’établit pas, par répétition, les « 33 campagnes présidentielles » revendiquées par Tal Hanan.

Le contraste AIMS est révélateur. Team Jorge présentait un parc supérieur à 30 000 profils ; à partir des avatars exposés dans les démonstrations, les enquêteurs ont pu identifier environ 2 000 bots AIMS liés (`FCT-013`). Ce n’est pas une réfutation de la capacité maximale, mais un bornage : **30 000 est une revendication de prestataire ; ~2 000 est un périmètre indépendamment retracé à partir des traces publiques du dossier**.

Au Kenya, l’accès à des comptes Telegram de proches de William Ruto a été montré pendant la démonstration (`FCT-014`). Deux limites résistent : le client de l’interférence n’a pas été identifié publiquement dans ce dossier et Ruto a gagné l’élection. Le cas prouve une action intrusive ; il ne prouve pas un basculement électoral.

En France, des séquences non validées ont bien été diffusées sur BFM-TV et certaines recoupaient les récits de campagnes Team Jorge ; Team Jorge en a montré une comme preuve de sa capacité à placer un sujet (`FCT-015`). Mais l’arête décisive `Team Jorge → Duthion/M’Barki` n’est pas fermée : les deux intéressés ont nié connaître Team Jorge et Le Monde note que l’officine exagérait parfois l’étendue de ses services. Une procédure ultérieure a établi des paiements Duthion→M’Barki dans un dossier plus large (`FCT-016`), sans autoriser à réattribuer automatiquement ces paiements à Team Jorge.

**Position :** I1-I2 forts ; I3 partiel ; I4 variable ; I5-I7 non établis en général.

## 4. STOIC / Zero Zeno : attribution opérateur forte, portée faible

OpenAI attribue Zero Zeno à STOIC, firme israélienne de gestion de campagnes, et documente une opération multi-plateforme ciblant notamment Canada, États-Unis et Israël (`FCT-007`). Reuters rapporte parallèlement l’attribution Meta à STOIC (`FCT-009`), tandis que DFRLab avait observé le réseau avant l’attribution publique (`FCT-010`).

L’existence de l’opération ne doit pas être confondue avec son rendement. OpenAI classe Zero Zeno en **catégorie 2** sur la Breakout Scale, sans preuve d’amplification significative hors du réseau, et relève un exemple YouTube à zéro vue (`FCT-008`).

Le lien avec l’État israélien doit rester plus bas dans la hiérarchie probatoire. Le Jerusalem Post relaie l’enquête du New York Times selon laquelle le ministère des Affaires de la diaspora aurait financé l’opération à hauteur d’environ 2 millions de dollars et mandaté STOIC ; le même article reproduit le démenti explicite du ministère, qui qualifie la connexion STOIC de « baseless » (`FCT-011`). Le run ne transforme ni l’enquête journalistique ni le démenti en autorité terminale : **l’opérateur STOIC est établi ; le client ministériel est `PARTIAL / ATTRIBUTION` dans le corpus public inspecté**.

**Position :** I0-I2 forts ; I3 client étatique partiel ; I4 faible/mesuré ; I5-I7 non établis.

## 5. Alp Services / EAU : la chaîne contractuelle la plus dense

Le corpus Abu Dhabi Secrets est fondé sur des fichiers internes d’Alp Services obtenus après piratage puis exploités par Mediapart/EIC. Il documente un premier contrat en 2017 et au moins 5,7 millions d’euros reçus entre 2017 et 2020 d’Al Ariaf, présenté comme couverture des services émiratis (`FCT-017`). Les documents décrivent des objectifs de cartographie puis de discrédit, avec diffusion discrète et massive, campagnes de presse, modifications Wikipédia, tribunes sous faux profils et tentatives de fermeture de comptes bancaires (`FCT-018`).

C’est la meilleure chaîne `client/paiement → prestataire → tasking` des trois cas centraux. Mais elle ne doit pas être sur-certifiée. Les avocats d’Alp ont soutenu que les documents étaient en partie falsifiés et les questions construites sur des suppositions erronées (`FCT-019`). Ce démenti ne neutralise pas automatiquement le corpus ; il impose de le conserver dans la contradiction.

Surtout, l’opération « Constellation » fournit un test interne de vantardise : Mediapart décrit une mission secrète de contre-lobbying contre les réseaux qataris à Bruxelles, mais conclut qu’Alp a peu découvert au-delà d’un concurrent et s’est vanté d’une influence imaginaire auprès d’élus RN (`FCT-020`). Là encore, le prestataire peut vendre **une perception de capacité** en même temps qu’une opération réelle.

Enfin, une information judiciaire française a été ouverte en 2025 après la plainte de Sihem Souid pour une surveillance présumée susceptible d’avoir été menée par Alp Services (`FCT-021`). C’est un **statut judiciaire d’enquête**, pas une condamnation et pas la preuve que toutes les actions alléguées sont établies.

**Position :** I0-I3 forts pour la chaîne contractuelle/tasking tirée du corpus interne ; I2 partiel selon les actes précis ; I4-I7 très incomplets.

## 6. Matrice I0-I7

| Cas | I0 identité/relation | I1 capacité/ressources | I2 action | I3 tasking/client | I4 reach | I5 persuasion | I6 changement | I7 contrefactuel |
|---|---|---|---|---|---|---|---|---|
| Archimedes | VERIFIED | VERIFIED | VERIFIED platform-level | client UNKNOWN | MEASURED followers/ads | NOT_ESTABLISHED | NOT_ESTABLISHED | NOT_ESTABLISHED |
| Rally Forge | VERIFIED | VERIFIED | VERIFIED platform-level | VERIFIED by Meta for named clients | MEASURED followers/ads | NOT_ESTABLISHED | NOT_ESTABLISHED | NOT_ESTABLISHED |
| Team Jorge | VERIFIED | VERIFIED/observed | VERIFIED/PARTIAL | PARTIAL/UNKNOWN by case | PARTIAL | NOT_ESTABLISHED | NOT_ESTABLISHED | NOT_ESTABLISHED |
| STOIC | VERIFIED | VERIFIED | VERIFIED | PARTIAL for ministry client | LOW / measured | NOT_ESTABLISHED | NOT_ESTABLISHED | NOT_ESTABLISHED |
| Alp Services | VERIFIED | VERIFIED | VERIFIED/PARTIAL | STRONG in leaked contract/payment corpus | PARTIAL | NOT_ESTABLISHED | PARTIAL reputational consequences; general policy effect unknown | NOT_ESTABLISHED |

Cette matrice est le résultat principal de l’enquête : **les opérations clandestines privées sont plus faciles à prouver que leur efficacité politique**.

## 7. Contrôles adversariaux

### CTRL-001 — prestataire contre traces indépendantes
Team Jorge : 30 000+ profils commercialisés versus environ 2 000 retracés par les enquêteurs à partir des artefacts exposés. La différence n’est pas arrondie en « mensonge » ; elle empêche simplement de certifier le chiffre commercial comme déploiement observé.

### CTRL-002 — étranger contre domestique
Rally Forge démontre un mécanisme trompeur commercial et domestique. Il invalide toute définition qui ferait de la nationalité étrangère une condition du phénomène d’influence-for-hire.

### CTRL-003 — opération contre effet
Zero Zeno : faible amplification authentique. Kenya : le camp dont les proches ont été piratés gagne. Constellation : influence revendiquée décrite comme imaginaire. Ces trois tests falsifient `opération détectée => succès politique`.

### CTRL-004 — force variable de l’attribution client
Alp : documents internes + paiements + tasking. STOIC : opérateur solide, client ministériel publiquement contesté. Team Jorge Kenya : client inconnu. La même étiquette médiatique « ingérence » recouvre donc des chaînes probatoires très différentes.

## 8. Explications alternatives et limites

1. **Marketing agressif / perception hacking.** Une partie des performances revendiquées peut être destinée au client plutôt qu’au public.
2. **PR ou lobbying ordinaire.** Certaines activités deviennent influence clandestine seulement lorsque tromperie d’identité, action cachée ou tasking opaque sont établis ; une relation commerciale ouverte n’est pas requalifiée par soupçon.
3. **Agence domestique.** Une opération peut être interne et trompeuse sans puissance étrangère.
4. **Biais de détection.** Les plateformes et enquêtes ouvertes observent surtout ce qu’elles peuvent tracer ; le corpus ne mesure pas la prévalence totale du marché.
5. **Circularité des sources.** Plusieurs publications partagent les mêmes ensembles techniques ou fuites. Elles ne sont pas comptées comme corroborations indépendantes automatiques.

## 9. Gaps terminaux

- `CLM-005 / GAP=ATTRIBUTION` : chaîne publique directe ministère israélien→STOIC encore contestée dans le corpus inspecté.
- `CAU-001 / GAP=CAUSALITY` : opération→persuasion/comportement non identifiée généralement.
- `CAU-002 / GAP=CAUSALITY` : opération→résultat électoral/politique contrefactuel non identifié.
- Team Jorge : clients et palmarès électoral revendiqué non fermés dossier par dossier.
- Alp Services : issue judiciaire et matérialité exacte de plusieurs actes allégués à rechecker lorsque les procédures produiront des décisions ou pièces publiques.

## 10. Conclusion

L’« influence-for-hire » n’est pas une spéculation : **c’est une industrie observable de services opaques ou trompeurs**, mobilisable par des États, des campagnes, des entreprises ou d’autres clients. Le marché crée une couche d’intermédiation qui peut masquer le donneur d’ordre et brouiller la qualification politique.

Mais le résultat forensique est plus restrictif que le récit sensationnel : ce corpus permet souvent d’établir **qui opère** et **ce qui a été fait** ; il permet parfois d’établir **qui paie ou mandate** ; il permet beaucoup moins souvent d’établir **qui a réellement été persuadé** et presque jamais, dans les cas inspectés ici, **quel résultat électoral ou politique aurait été différent sans l’opération**.

La règle à conserver pour les investigations suivantes est donc :

`provider exists → capability → deployed action → tasking/client → exposure → persuasion → outcome`

Chaque flèche est un claim. Aucune ne s’hérite de la précédente.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:6|SRC_COMPLETE:16/16

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **as_of:** 2026-09-06
- **material_changes:**
  - 2023 Team Jorge exposure
  - 2023 Abu Dhabi Secrets
  - 2024 STOIC/Zero Zeno attribution
  - 2025 French Alp judicial investigation
- **measurement_focus:** current public evidence status, not retrospective omniscience
- **period:** 2010-2026
- **refresh_rule:** recheck litigation/client attribution if new judicial or documentary material appears

### MANIPULATION_REPORT
- **assumptions:**
  - private providers can be state or non-state intermediaries
  - foreignness is not itself interference
- **clusters:**
  - NONE
- **complexity:** HIGH
- **implicit:**
  - all official and private claims require evidence
  - faisceau is a routing lead, not edge proof
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - attribution layering
  - provider self-promotion
  - coordinated inauthentic behavior
  - media placement
  - reputation attack
- **priorities:**
  - documented action
  - client/tasking
  - reach/effect
  - rival explanations
- **query_guidance:** operation-first; reopen sources; distinguish claim status
- **rhetorical:**
  - NONE
- **speaker:** user/object question
- **symbol_stage:** FINAL
- **symbols:**
  - **M:** 5
  - **Κ:** 4
  - **Λ:** 5
  - **Ξ:** 5
  - **Σ:** 3
  - **Φ:** 4
  - **Ψ:** 4
  - **Ω:** 3
  - **κ:** 4
  - **ρ:** 4
  - **€:** 5
  - **↕:** 5
  - **⏰:** 4
  - **⚔:** 3
  - **⫸:** 5
- **threats:**
  - provider exaggeration
  - circular platform reporting
  - client opacity
  - effect inflation

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **geo:** France/Europe priority; international comparators when trace quality is higher
- **measurement_contract:**
  - separate marketed capability from observed deployment
  - separate provider attribution from client/tasking attribution
  - separate reach from persuasion and outcome
  - domestic/foreign symmetry
- **object:** Private influence-for-hire market and auditable client→provider→action→target→exposure/effect chains
- **period:** 2010-2026
- **priority_tests:**
  - Team Jorge
  - STOIC/Zero Zeno
  - Alp Services/UAE
  - Archimedes/Rally Forge controls

### CREDO
- accusation != fact
- official statement != proof
- official denial != proof
- funding != command
- capability != use != effect
- operation exists != result changed

### COGNITIVE_MAP
- **causal_boundary:** No general election/policy outcome is attributed without a counterfactual design.
- **core_model:** Private influence-for-hire is a real market; evidentiary strength generally decreases along capacity→use→client/tasking→reach→persuasion→outcome.
- **observed_structure:**
  - commercial providers
  - deceptive identities
  - multi-platform operations
  - client deniability layers
  - vendor performance claims
- **rival_models:**
  - ordinary PR/lobbying where no deception/tasking is shown
  - vendor bluff/perception hacking
  - domestic political marketing
  - platform detection bias toward observable networks

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** many headline claims come from vendors or takedown authorities
  - **resolution:** market existence supported; each action/client/effect edge separately graded
  - **thesis:** commercial covert influence market is real
- **item 2:**
  - **antithesis:** same mechanisms occur domestically
  - **resolution:** origin is a dimension, not the mechanism definition
  - **thesis:** foreign clients can purchase operations
- **item 3:**
  - **antithesis:** authentic engagement can be low
  - **resolution:** exposure metrics != persuasion/outcome
  - **thesis:** large bot/account numbers imply impact
- **item 4:**
  - **antithesis:** intermediary opacity can be ordinary subcontracting
  - **resolution:** tasking requires contract/payment/communication evidence
  - **thesis:** private provider gives deniability
- **item 5:**
  - **antithesis:** provider disputes integrity/interpretation
  - **resolution:** use leaks with provenance, rebuttal, and judicial follow-up; do not convert allegation into conviction
  - **thesis:** leaked internal files reveal hidden chains

### RESOURCE_FLOW_MAP
- **item 1:**
  - **chain:** UAE-linked Al Ariaf -> Alp Services -> mapping/discredit/influence tasks
  - **status:** DOCUMENTED_IN_LEAKED_INTERNAL_CORPUS
  - **support:**
    - FCT-017
    - FCT-018
    - FCT-019
- **item 2:**
  - **chain:** reported Israel Diaspora Affairs Ministry -> STOIC -> Zero Zeno
  - **status:** CONTESTED_ATTRIBUTION
  - **support:**
    - FCT-011
- **item 3:**
  - **chain:** domestic clients -> Rally Forge -> deceptive engagement campaign
  - **status:** PLATFORM_ATTRIBUTED
  - **support:**
    - FCT-004
    - FCT-005

### ACTOR_NETWORK_MAP
- **item 1:**
  - **actor:** Team Jorge/Tal Hanan
  - **documented_edges:**
    - AIMS capability
    - hacking demonstrations
    - campaign activity
  - **role:** private provider
  - **uncertain_edges:**
    - clients in key cases
    - claimed election wins
- **item 2:**
  - **actor:** STOIC
  - **documented_edges:**
    - Zero Zeno operator
    - cross-platform content generation
  - **role:** political marketing provider
  - **uncertain_edges:**
    - Diaspora Ministry tasking/payment publicly contested
- **item 3:**
  - **actor:** Alp Services/Mario Brero
  - **documented_edges:**
    - UAE-linked contract/payment in leaked internal records
    - mapping/discredit/influence tasks
  - **role:** private intelligence provider
  - **uncertain_edges:**
    - legality/adjudication of all alleged surveillance acts
    - performance claims
- **item 4:**
  - **actor:** Archimedes Group
  - **documented_edges:**
    - Meta-attributed CIB network
  - **role:** commercial influence provider
  - **uncertain_edges:**
    - client identities/effects
- **item 5:**
  - **actor:** Rally Forge
  - **documented_edges:**
    - Meta-attributed domestic US deceptive operation for named clients
  - **role:** domestic marketing provider
  - **uncertain_edges:**
    - causal persuasion/election effect
- **item 6:**
  - **actor:** platform/research/journalistic investigators
  - **documented_edges:**
    - takedowns
    - technical traces
    - undercover/leaked-document reporting
  - **role:** attribution/evidence intermediaries
  - **uncertain_edges:**
    - complete visibility into off-platform clients and effects

### IMPACT_MAP
- **downstream:**
  - INV-134 attribution audit
  - INV-140 indirect electoral funding
  - INV-146 ally/adversary symmetry
  - future case-specific causal studies
- **measured_objects:**
  - asset counts
  - followers
  - ad spend
  - platform amplification
  - observed placements/hacks
- **not_established:**
  - general persuasion rate
  - vote conversion
  - counterfactual election results
  - general policy change attributable to provider

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** only ~2k linked bots independently traced from disclosed artifacts; claimed wins not independently closed
  - **issue:** Team Jorge 30k/33 campaigns
  - **pro:** undercover sales demonstration and claimed scale
  - **status:** BOUNDED
- **item 2:**
  - **contra:** explicit ministry denial
  - **issue:** STOIC ministry client
  - **pro:** NYT-reported documents/sources; JPost relay
  - **status:** UNRESOLVED_ATTRIBUTION
- **item 3:**
  - **contra:** Duthion/M’Barki denied knowing Team Jorge; intermediary edge unresolved
  - **issue:** Team Jorge BFM placement
  - **pro:** Team Jorge displayed actual BFM segment matching campaigns
  - **status:** PARTIAL
- **item 4:**
  - **contra:** Alp lawyers say documents partly falsified / premises erroneous
  - **issue:** Alp UAE chain
  - **pro:** leaked internal contracts/payment/tasking
  - **status:** SUPPORTED_WITH_REBUTTAL
- **item 5:**
  - **contra:** Zero Zeno low amplification; Kenya winner unaffected; Alp overclaim evidence
  - **issue:** effectiveness
  - **pro:** large networks/followers/ad spend and claimed wins
  - **status:** GENERAL_EFFECT_UNRESOLVED

### VERIFICATION_REPORT
- **causal_assessment:** CAU-001..002 UNRESOLVED
- **facts:** 21
- **key_controls:**
  - provider self-claim vs observed traces
  - domestic/foreign symmetry
  - reach vs effect
  - client-attribution strength
- **known_limit:** Most public evidence is detection/investigation evidence, not randomized or counterfactual outcome evidence.
- **sources:** 16
- **tier_policy:** All web-backed facts at ✧; no automatic promotion of self-claims or contested attribution.
- **upstream_families:** 8

### EDI_REPORT
- **corpus:**
  - **circularity:** Meta/OpenAI/Reuters/DFRLab overlap on STOIC; Guardian/Le Monde share Forbidden Stories investigation on Team Jorge; Mediapart/EIC share Abu Dhabi Secrets. Families are not treated as fully independent for same underlying trace.
  - **counters:** 4
  - **coverage:** 0.93
  - **direct_objects:** 8
  - **edi_star:** 0.82
  - **independence:** 0.8
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 5
  - **item 2:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 4
  - **item 4:**
    - **claim_id:** CLM-005
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-006
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 2
  - **item 6:**
    - **claim_id:** CLM-008
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 5
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 0.9
  - **lang:** 0.9
  - **owner:** 0.85
  - **persp:** multi-actor with adversarial controls
  - **strat:** 0.9
  - **temp:** 0.95
- **edi:**
  - **final:** 0.82
  - **flags:**
    - STOIC_CLIENT_ATTRIBUTION_CONTESTED
    - GENERAL_CAUSAL_EFFECT_UNRESOLVED
    - CONSORTIUM_CIRCULARITY
  - **penalties:** 0.06
  - **raw:** 0.88
- **source_counts:**
  - **primary:** 0
  - **secondary:** 16
  - **total:** 16

### RESPONSIBILITY_MAP
- **item 1:**
  - **client:** UNKNOWN
  - **effect:** UNRESOLVED
  - **object:** Archimedes operation
  - **operator:** Archimedes Group
- **item 2:**
  - **client:** Turning Point USA / Inclusive Conservation Group per Meta
  - **effect:** UNRESOLVED
  - **object:** Rally Forge network
  - **operator:** Rally Forge
- **item 3:**
  - **client:** reported Ministry attribution CONTESTED
  - **effect:** LOW_REACH / CAUSAL_EFFECT_UNRESOLVED
  - **object:** Zero Zeno
  - **operator:** STOIC
- **item 4:**
  - **client:** UNKNOWN
  - **effect:** winner unaffected; broader effect unresolved
  - **object:** Team Jorge Kenya
  - **operator:** Team Jorge
- **item 5:**
  - **client:** UAE-linked services per leaked corpus
  - **effect:** targeting/action documented; broad political effect unresolved
  - **object:** Alp Services UAE work
  - **operator:** Alp Services

### NEXT_QUERIES
- Direct judicial or contractual evidence resolving STOIC ministry tasking if made public
- Case-specific client identity for Team Jorge Kenya/other elections
- Outcome designs linking exposure to persuasion or vote/policy change
- Final French/Swiss judicial outcomes concerning Alp Services allegations

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-004,QRY-008,QRY-009,QRY-010,QRY-011,QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-006,FCT-011,FCT-012,FCT-013,FCT-014,FCT-017,FCT-019,FCT-020,FCT-021 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004 | support:- | counter:- | results:FCT-001,FCT-002,FCT-004,FCT-006 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-005,QRY-009,QRY-010,QRY-011,QRY-014 | support:- | counter:- | results:FCT-007,FCT-012,FCT-013,FCT-014,FCT-018 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-009,QRY-010,QRY-011,QRY-012,QRY-013 | support:- | counter:- | results:FCT-012,FCT-013,FCT-014,FCT-015,FCT-016 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-005,QRY-006,QRY-007,QRY-008 | support:- | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-010,FCT-011 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-014,QRY-015,QRY-016 | support:- | counter:- | results:FCT-017,FCT-018,FCT-019,FCT-020,FCT-021 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-003 | support:- | counter:- | results:FCT-004,FCT-005 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-002,QRY-003,QRY-005,QRY-011,QRY-015 | support:- | counter:- | results:FCT-003,FCT-005,FCT-008,FCT-014,FCT-020 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-004,QRY-008,QRY-012,QRY-014 | support:- | counter:- | results:FCT-006,FCT-011,FCT-015,FCT-017,FCT-019 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-014,SRC-001,SRC-002,SRC-003,SRC-004,SRC-005,SRC-014 | support:FCT-001,FCT-002,FCT-004,FCT-006,FCT-007,FCT-017 | counter:- | results:FCT-001,FCT-002,FCT-004,FCT-006,FCT-007,FCT-017 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-002,QRY-005,QRY-009,QRY-010,QRY-011,QRY-014,SRC-002,SRC-005,SRC-009,SRC-010,SRC-011,SRC-014 | support:FCT-002,FCT-007,FCT-012,FCT-013,FCT-014,FCT-018 | counter:- | results:FCT-002,FCT-007,FCT-012,FCT-013,FCT-014,FCT-018 | final:SUPPORTED | gap:NONE
CLM-003 | attempts:QRY-009,QRY-010,QRY-011,QRY-012,SRC-009,SRC-010,SRC-011,SRC-012 | support:FCT-012,FCT-013,FCT-014,FCT-015 | counter:FCT-014(client unknown; winner unaffected) | results:FCT-012,FCT-013,FCT-014,FCT-015,FCT-014(client unknown; winner unaffected) | final:SUPPORTED | gap:NONE
CLM-004 | attempts:QRY-005,QRY-006,QRY-007,SRC-005,SRC-006,SRC-007 | support:FCT-007,FCT-008,FCT-009,FCT-010 | counter:- | results:FCT-007,FCT-008,FCT-009,FCT-010 | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-008,SRC-008 | support:FCT-011 | counter:FCT-011(ministry denial) | results:FCT-011,FCT-011(ministry denial) | final:PARTIAL | gap:ATTRIBUTION
CLM-006 | attempts:QRY-014,QRY-015,SRC-014,SRC-015 | support:FCT-017,FCT-018,FCT-019,FCT-020 | counter:FCT-019(provider rebuttal);FCT-020(overclaim control) | results:FCT-017,FCT-018,FCT-019,FCT-020,FCT-019(provider rebuttal);FCT-020(overclaim control) | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-003,SRC-003 | support:FCT-004,FCT-005 | counter:- | results:FCT-004,FCT-005 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-002,QRY-003,QRY-005,QRY-011,QRY-015,SRC-002,SRC-003,SRC-005,SRC-011,SRC-015 | support:FCT-003,FCT-005,FCT-008,FCT-014,FCT-020 | counter:- | results:FCT-003,FCT-005,FCT-008,FCT-014,FCT-020 | final:SUPPORTED | gap:NONE
CLM-009 | attempts:QRY-004,QRY-008,QRY-012,QRY-014,SRC-004,SRC-008,SRC-012,SRC-014 | support:FCT-006,FCT-011,FCT-015,FCT-017,FCT-019 | counter:- | results:FCT-006,FCT-011,FCT-015,FCT-017,FCT-019 | final:SUPPORTED | gap:NONE

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-005 | CLM | PARTIAL | ATTRIBUTION | Publicly auditable ministry→STOIC payment/tasking evidence is not directly available in the scoped sources beyond reported documents/sources and denial.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | The scoped evidence measures assets, followers, ads or platform amplification but does not identify general persuasion or behavior change caused by the operations.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | No scoped case identifies a counterfactual election/policy result attributable to the commercial operation; vendor success claims are not a substitute.

SEMANTIC_COUNTS_V1:LED:2|CLM:9|AXS:8|CAU:2|CTRL:4|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016"],"evidence_excerpt":"client → prestataire → action → cible → exposition/effet","kind":"HYPOTHESIS","lead":"A private influence-for-hire market exists, but evidence strength may fall sharply as the chain moves from capacity to client/tasking, action, reach and effect.","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006","AXS-007","AXS-008","CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"],"routes":["OBJECT_INVESTIGATION","MECHANISMS","COUNTER_HYPOTHESES"],"source_id":"INV-128_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-004","QRY-008","QRY-009","QRY-010","QRY-011","QRY-014","QRY-015","QRY-016"],"evidence_excerpt":"sans confondre capacité annoncée, démonstration commerciale, opération exécutée, attribution et résultat","kind":"METHOD_CONSTRAINT","lead":"Provider claims, platform attribution, client identity, payment, action and result must be tested as separate edges; capability != use != effect.","linked_ids":["CLM-003","CLM-005","CLM-006","CLM-008","CLM-009","CAU-001","CAU-002","CTRL-001","CTRL-003","CTRL-004"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-006","FCT-011","FCT-012","FCT-013","FCT-014","FCT-017","FCT-019","FCT-020","FCT-021"],"routes":["COUNTER_HYPOTHESES","RULES_CONTROLS"],"source_id":"INV-128_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"A recurrent commercial influence-for-hire market is directly documented: covert/deceptive operations have been linked to commercial firms for both foreign and domestic clients across multiple regions.","claimant":"INV-128 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-004","FCT-006","FCT-007","FCT-017"]}
CLM-002 | {"claim":"The service bundle is heterogeneous: fake personas, deceptive amplification and fabricated media identities are common, while some providers also market or demonstrate hacking, private intelligence, media placement, reputational attack and financial-pressure tactics.","claimant":"INV-128 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-002","FCT-007","FCT-012","FCT-013","FCT-014","FCT-018"]}
CLM-003 | {"claim":"For Team Jorge, capacity and some actions are independently observable, but the advertised scale and claimed election-success record exceed what the scoped public evidence independently establishes; key clients remain unknown in decisive cases.","claimant":"INV-128 synthesis","counter":"FCT-014(client unknown; winner unaffected)","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-012","FCT-013","FCT-014","FCT-015"]}
CLM-004 | {"claim":"STOIC/Zero Zeno is independently attributable at the provider/action level across platform and research sources, but the operation achieved low authentic engagement in the measured period.","claimant":"INV-128 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-007","FCT-008","FCT-009","FCT-010"]}
CLM-005 | {"claim":"The specific claim that Israel’s Diaspora Affairs Ministry financed/tasked STOIC is materially supported by reported documents/sources but remains publicly contested by an explicit ministry denial; the scoped open evidence does not independently close the payment/tasking edge beyond that reporting.","claimant":"INV-128 synthesis","counter":"FCT-011(ministry denial)","gap":"Publicly auditable ministry→STOIC payment/tasking evidence is not directly available in the scoped sources beyond reported documents/sources and denial.","gap_type":"ATTRIBUTION","materiality":"HIGH","status":"PARTIAL","support":["FCT-011"]}
CLM-006 | {"claim":"Alp Services provides the densest scoped client→payment→provider→tasking chain: leaked internal records support UAE-linked contracting/payment and explicit mapping/discredit/influence tasks, while the provider disputes the integrity/interpretation of the leaked corpus and some performance claims are independently challenged.","claimant":"INV-128 synthesis","counter":"FCT-019(provider rebuttal);FCT-020(overclaim control)","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-017","FCT-018","FCT-019","FCT-020"]}
CLM-007 | {"claim":"Influence-for-hire is a mechanism class, not a synonym for foreign interference: Rally Forge shows a materially similar deceptive commercial mechanism operating for domestic US clients.","claimant":"INV-128 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-004","FCT-005"]}
CLM-008 | {"claim":"Exposure and success must be separated: large follower/ad counts can coexist with unknown persuasion; Zero Zeno had low authentic amplification; Team Jorge’s Kenya activity did not change the winner; Alp Services was reported to exaggerate influence.","claimant":"INV-128 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-003","FCT-005","FCT-008","FCT-014","FCT-020"]}
CLM-009 | {"claim":"Private intermediaries can create attribution layers and plausible deniability, but those layers are not themselves proof of state command; each client→provider edge requires its own documentary or technical evidence.","claimant":"INV-128 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-006","FCT-011","FCT-015","FCT-017","FCT-019"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004"],"axis":"MARKET","links":["CLM-001","CLM-007"],"question":"Is a recurrent commercial market for deceptive influence services documented across distinct providers and regions?","result_ids":["FCT-001","FCT-002","FCT-004","FCT-006"],"sought_objects":["MARKET"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-005","QRY-009","QRY-010","QRY-011","QRY-014"],"axis":"SERVICE_BUNDLE","links":["CLM-002","CLM-003","CLM-004","CLM-006"],"question":"Which capabilities are marketed and which are independently observed in use?","result_ids":["FCT-007","FCT-012","FCT-013","FCT-014","FCT-018"],"sought_objects":["SERVICE_BUNDLE"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-009","QRY-010","QRY-011","QRY-012","QRY-013"],"axis":"TEAM_JORGE","links":["CLM-003","CLM-008","CAU-002"],"question":"Where does Team Jorge evidence stop between demonstration, deployed action, client and outcome?","result_ids":["FCT-012","FCT-013","FCT-014","FCT-015","FCT-016"],"sought_objects":["TEAM_JORGE"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-005","QRY-006","QRY-007","QRY-008"],"axis":"STOIC","links":["CLM-004","CLM-005","CLM-008"],"question":"Can provider/action be separated from disputed government client attribution and weak reach?","result_ids":["FCT-007","FCT-008","FCT-009","FCT-010","FCT-011"],"sought_objects":["STOIC"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-014","QRY-015","QRY-016"],"axis":"ALP_SERVICES","links":["CLM-006","CLM-008","CAU-001"],"question":"Can client/payment/tasking/action be traced and vendor performance claims adversarially tested?","result_ids":["FCT-017","FCT-018","FCT-019","FCT-020","FCT-021"],"sought_objects":["ALP_SERVICES"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-003"],"axis":"DOMESTIC_SYMMETRY","links":["CLM-007","CTRL-002"],"question":"Does the same deceptive mechanism occur for domestic clients, independent of foreign origin?","result_ids":["FCT-004","FCT-005"],"sought_objects":["DOMESTIC_SYMMETRY"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-002","QRY-003","QRY-005","QRY-011","QRY-015"],"axis":"REACH_EFFECT","links":["CLM-008","CAU-001","CAU-002","CTRL-003"],"question":"What evidence exists from follower/ad metrics to authentic reach, persuasion and election/policy effect?","result_ids":["FCT-003","FCT-005","FCT-008","FCT-014","FCT-020"],"sought_objects":["REACH_EFFECT"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-004","QRY-008","QRY-012","QRY-014"],"axis":"ATTRIBUTION_DENIABILITY","links":["CLM-005","CLM-009","CTRL-004"],"question":"How do private intermediaries create deniability and where are client/tasking claims independently auditable?","result_ids":["FCT-006","FCT-011","FCT-015","FCT-017","FCT-019"],"sought_objects":["ATTRIBUTION_DENIABILITY"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"FCT-008(low amplification);FCT-014(winner unaffected)","gap":"The scoped evidence measures assets, followers, ads or platform amplification but does not identify general persuasion or behavior change caused by the operations.","gap_type":"CAUSALITY","limit":"Requires exposure at individual/group level plus credible comparative or experimental/quasi-experimental design.","mechanism":"Influence-for-hire operation -> authentic reception/persuasion/behavioral change","status":"UNRESOLVED","support":["FCT-003","FCT-005","FCT-008","FCT-014","FCT-020"]}
CAU-002 | {"counter":"FCT-014(Kenya winner unaffected)","gap":"No scoped case identifies a counterfactual election/policy result attributable to the commercial operation; vendor success claims are not a substitute.","gap_type":"CAUSALITY","limit":"Requires case-specific counterfactual evidence, not service-provider claims or temporal coincidence.","mechanism":"Influence-for-hire operation -> election or policy outcome","status":"UNRESOLVED","support":["FCT-014","FCT-015","FCT-017","FCT-018"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Team Jorge’s marketing claim of more than 30,000 AIMS profiles is bounded by reporters independently identifying about 2,000 AIMS-linked bots from disclosed traces; marketed capacity is not treated as verified deployed scale.","status":"SUPPORTED","support":["FCT-013"]}
CTRL-002 | {"control":"Rally Forge is a domestic US comparator showing that fake-persona/coordinated deception can be purchased or organized internally; foreign origin is not necessary for the mechanism.","status":"SUPPORTED","support":["FCT-004","FCT-005"]}
CTRL-003 | {"control":"Three independent impact controls reject success-by-existence: OpenAI found low external amplification for Zero Zeno, the Team Jorge Kenya case did not prevent the targeted camp’s victory, and Mediapart documented Alp Services boasting of influence described as imaginary.","status":"SUPPORTED","support":["FCT-008","FCT-014","FCT-020"]}
CTRL-004 | {"control":"Client attribution strength varies materially: Alp internal records provide contract/payment/tasking evidence; the STOIC-ministry edge is reported but explicitly denied; the Team Jorge Kenya client is unknown.","status":"SUPPORTED","support":["FCT-011","FCT-014","FCT-017","FCT-019"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:16|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-004 | SYS | OK | web | INV-128 | WEB_RESEARCH
SYS-005 | SYS | FAIL:MNEMO_UNAVAILABLE | mnemo | INV-128 | MNEMO_S
SYS-006 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://about.fb.com/news/2021/05/influence-operations-threat-report/ | Meta strategic IO report 2017-2020
QRY-002 | FETCH | FOUND | SRC-002 | https://about.fb.com/news/2019/05/removing-coordinated-inauthentic-behavior-from-israel/ | Meta Archimedes Group takedown
QRY-003 | FETCH | FOUND | SRC-003 | https://about.fb.com/news/2020/10/removing-coordinated-inauthentic-behavior-september-report/ | Meta Rally Forge takedown
QRY-004 | FETCH | FOUND | SRC-004 | https://about.fb.com/news/2023/02/metas-adversarial-threat-report-q4-2022/ | Meta Q4 2022 adversarial threat report
QRY-005 | FETCH | FOUND | SRC-005 | https://openai.com/index/disrupting-malicious-uses-of-ai-zero-zeno/ | OpenAI Zero Zeno case study
QRY-006 | FETCH | FOUND | SRC-006 | https://www.reuters.com/technology/meta-identifies-networks-pushing-deceptive-content-likely-generated-by-ai-2024-05-29/ | Reuters on Meta STOIC attribution
QRY-007 | FETCH | FOUND | SRC-007 | https://dfrlab.org/2024/03/28/inauthentic-campaign-amplifying-islamophobic-content-targeting-canadians/ | DFRLab Canadian inauthentic campaign
QRY-008 | FETCH | FOUND | SRC-008 | https://www.jpost.com/breaking-news/article-805086 | Jerusalem Post STOIC ministry claim and denial
QRY-009 | FETCH | FOUND | SRC-009 | https://www.theguardian.com/world/2023/feb/15/revealed-disinformation-team-jorge-claim-meddling-elections-tal-hanan | Guardian Team Jorge overview
QRY-010 | FETCH | FOUND | SRC-010 | https://www.theguardian.com/world/2023/feb/15/aims-software-avatars-team-jorge-disinformation-fake-profiles | Guardian AIMS bot investigation
QRY-011 | FETCH | FOUND | SRC-011 | https://www.theguardian.com/world/2023/feb/15/political-aides-hacked-by-team-jorge-in-run-up-to-kenyan-election | Guardian Team Jorge Kenya case
QRY-012 | FETCH | FOUND | SRC-012 | https://www.lemonde.fr/pixels/article/2023/02/15/derriere-les-fausses-infos-de-rachid-m-barki-sur-bfm-tv-l-officine-israelienne-team-jorge-et-un-intermediaire-francais_6161862_4408996.html | Le Monde Team Jorge/BFM case
QRY-013 | FETCH | FOUND | SRC-013 | https://www.lemonde.fr/societe/article/2024/12/16/ingerences-etrangeres-une-confrontation-organisee-chez-le-juge-d-instruction_6452493_3224.html | Le Monde French influence judicial follow-up
QRY-014 | FETCH | FOUND | SRC-014 | https://www.mediapart.fr/en/journal/international/021023/how-swiss-firm-handed-uae-names-1000-supposed-muslim-brotherhood-sympathisers-europe | Mediapart/EIC Abu Dhabi Secrets - Alp Services
QRY-015 | FETCH | FOUND | SRC-015 | https://www.mediapart.fr/journal/international/090723/operation-constellation-les-pieds-nickeles-d-abou-dhabi-bruxelles | Mediapart Operation Constellation
QRY-016 | FETCH | FOUND | SRC-016 | https://www.lemonde.fr/societe/article/2025/08/22/accusations-d-espionnage-d-une-communicante-du-qatar-en-france-une-information-judiciaire-ouverte_6633518_3224.html | Le Monde Alp Services judicial investigation

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:meta-threat-intel | META-IO-2021 | Meta strategic IO report 2017-2020 | 2021-05-26 | 2026-09-06T15:31:00Z | Definition, 150+ covert operations, domestic/foreign and commercial actors | https://about.fb.com/news/2021/05/influence-operations-threat-report/
SRC-002 | ◈ | fam:other:meta-enforcement | META-ARCHIMEDES-2019 | Meta Archimedes Group takedown | 2019-05-16 | 2026-09-06T15:31:00Z | 265 assets; commercial attribution; audience and ad metrics | https://about.fb.com/news/2019/05/removing-coordinated-inauthentic-behavior-from-israel/
SRC-003 | ◈ | fam:other:meta-enforcement | META-RALLYFORGE-2020 | Meta Rally Forge takedown | 2020-10-08 | 2026-09-06T15:31:00Z | US domestic deceptive network; firm and clients | https://about.fb.com/news/2020/10/removing-coordinated-inauthentic-behavior-september-report/
SRC-004 | ◈ | fam:other:meta-threat-intel | META-ATR-Q4-2022 | Meta Q4 2022 adversarial threat report | 2023-02-23 | 2026-09-06T15:31:00Z | Private actors, plausible deniability, client-facing perception hacking | https://about.fb.com/news/2023/02/metas-adversarial-threat-report-q4-2022/
SRC-005 | ◈ | fam:other:openai-threat-intel | OPENAI-ZERO-ZENO-2024 | OpenAI Zero Zeno case study | 2024-05-01 | 2026-09-06T15:31:00Z | STOIC attribution, cross-platform behavior, Breakout Scale category 2 | https://openai.com/index/disrupting-malicious-uses-of-ai-zero-zeno/
SRC-006 | ◈ | fam:other:reuters | REUTERS-STOIC-2024 | Reuters on Meta STOIC attribution | 2024-05-29 | 2026-09-06T15:31:00Z | Meta attribution to Tel Aviv firm STOIC and fake personas | https://www.reuters.com/technology/meta-identifies-networks-pushing-deceptive-content-likely-generated-by-ai-2024-05-29/
SRC-007 | ◈ | fam:other:dfrlab | DFRLAB-CANADA-2024 | DFRLab Canadian inauthentic campaign | 2024-03-28 | 2026-09-06T15:31:00Z | Pre-attribution observation of inauthentic network targeting Canadians | https://dfrlab.org/2024/03/28/inauthentic-campaign-amplifying-islamophobic-content-targeting-canadians/
SRC-008 | ◈ | fam:other:jpost | JPOST-STOIC-MINISTRY-2024 | Jerusalem Post STOIC ministry claim and denial | 2024-06-05 | 2026-09-06T15:31:00Z | NYT-reported ministry funding/tasking and explicit ministry denial | https://www.jpost.com/breaking-news/article-805086
SRC-009 | ◈ | fam:other:guardian-storykillers | GUARDIAN-TEAMJORGE-2023 | Guardian Team Jorge overview | 2023-02-15 | 2026-09-06T15:31:00Z | Undercover demonstrations, service bundle, 33-campaign self-claim | https://www.theguardian.com/world/2023/feb/15/revealed-disinformation-team-jorge-claim-meddling-elections-tal-hanan
SRC-010 | ◈ | fam:other:guardian-storykillers | GUARDIAN-AIMS-2023 | Guardian AIMS bot investigation | 2023-02-15 | 2026-09-06T15:31:00Z | 30k marketed capacity versus ~2k reporter-identified AIMS-linked bots | https://www.theguardian.com/world/2023/feb/15/aims-software-avatars-team-jorge-disinformation-fake-profiles
SRC-011 | ◈ | fam:other:guardian-storykillers | GUARDIAN-KENYA-2023 | Guardian Team Jorge Kenya case | 2023-02-15 | 2026-09-06T15:31:00Z | Account access demonstrated; client unknown; winner unaffected | https://www.theguardian.com/world/2023/feb/15/political-aides-hacked-by-team-jorge-in-run-up-to-kenyan-election
SRC-012 | ◈ | fam:other:lemonde | LEMONDE-BFM-TEAMJORGE-2023 | Le Monde Team Jorge/BFM case | 2023-02-15 | 2026-09-06T15:31:00Z | Unvalidated BFM segments; Team Jorge claimed placement; intermediary link unresolved | https://www.lemonde.fr/pixels/article/2023/02/15/derriere-les-fausses-infos-de-rachid-m-barki-sur-bfm-tv-l-officine-israelienne-team-jorge-et-un-intermediaire-francais_6161862_4408996.html
SRC-013 | ◈ | fam:other:lemonde | LEMONDE-FOREIGN-INFLUENCE-2024 | Le Monde French influence judicial follow-up | 2024-12-16 | 2026-09-06T15:31:00Z | M’Barki payment admission and divergent intermediary/Qatar claims | https://www.lemonde.fr/societe/article/2024/12/16/ingerences-etrangeres-une-confrontation-organisee-chez-le-juge-d-instruction_6452493_3224.html
SRC-014 | ◈ | fam:other:mediapart-eic | MEDIAPART-ALP-2023 | Mediapart/EIC Abu Dhabi Secrets - Alp Services | 2023-10-02 | 2026-09-06T15:31:00Z | Hacked internal files; UAE contract/payment and influence methods; rebuttal | https://www.mediapart.fr/en/journal/international/021023/how-swiss-firm-handed-uae-names-1000-supposed-muslim-brotherhood-sympathisers-europe
SRC-015 | ◈ | fam:other:mediapart-eic | MEDIAPART-CONSTELLATION-2023 | Mediapart Operation Constellation | 2023-07-09 | 2026-09-06T15:31:00Z | Secret counter-lobbying mission and evidence of exaggerated influence claims | https://www.mediapart.fr/journal/international/090723/operation-constellation-les-pieds-nickeles-d-abou-dhabi-bruxelles
SRC-016 | ◈ | fam:other:lemonde | LEMONDE-ALP-JUDICIAL-2025 | Le Monde Alp Services judicial investigation | 2025-08-22 | 2026-09-06T15:31:00Z | French judicial investigation into alleged surveillance; allegation not conviction | https://www.lemonde.fr/societe/article/2025/08/22/accusations-d-espionnage-d-une-communicante-du-qatar-en-france-une-information-judiciaire-ouverte_6633518_3224.html

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://about.fb.com/news/2021/05/influence-operations-threat-report/ | other:meta-threat-intel | 2021-05-26 | Commercial influence operations market | Meta defines influence operations as coordinated efforts to manipulate or corrupt public debate for a strategic goal and reported removing more than 150 covert operations from 2017-2020; the set included foreign and domestic operations run by governments, commercial entities, politicians and fringe groups. | -
FCT-002 | FACT | ✧ | https://about.fb.com/news/2019/05/removing-coordinated-inauthentic-behavior-from-israel/ | other:meta-enforcement | 2019-05-16 | Archimedes commercial deceptive operation | Meta removed 265 Facebook/Instagram assets in an Israel-origin coordinated inauthentic operation targeting countries in Africa plus activity in Latin America and Southeast Asia, and linked part of the activity to the Israeli commercial entity Archimedes Group. | -
FCT-003 | FACT | ✧ | https://about.fb.com/news/2019/05/removing-coordinated-inauthentic-behavior-from-israel/ | other:meta-enforcement | 2019-05-16 | Archimedes exposure metrics | Meta reported about 2.8 million page followers and about $812,000 in Facebook ad spend for the Archimedes-linked network; these are exposure/resource metrics, not demonstrated persuasion or electoral effect. | -
FCT-004 | FACT | ✧ | https://about.fb.com/news/2020/10/removing-coordinated-inauthentic-behavior-september-report/ | other:meta-enforcement | 2020-10-08 | Rally Forge domestic influence-for-hire | Meta linked a US-origin deceptive network focused primarily on domestic US audiences to US marketing firm Rally Forge, working on behalf of Turning Point USA and Inclusive Conservation Group. | -
FCT-005 | FACT | ✧ | https://about.fb.com/news/2020/10/removing-coordinated-inauthentic-behavior-september-report/ | other:meta-enforcement | 2020-10-08 | Rally Forge scale | Meta reported 202 Facebook accounts, 54 Pages, 76 Instagram accounts, about 372,500 Page followers, about 22,000 Instagram followers and about $1.15 million in advertising for the Rally Forge network. | -
FCT-006 | FACT | ✧ | https://about.fb.com/news/2023/02/metas-adversarial-threat-report-q4-2022/ | other:meta-threat-intel | 2023-02-23 | Provider incentives and plausible deniability | Meta states that private influence actors can provide plausible deniability to customers while also having an interest in exaggerating their effectiveness through client-facing perception hacking; impact should therefore be assessed from evidence rather than actor claims. | -
FCT-007 | FACT | ✧ | https://openai.com/index/disrupting-malicious-uses-of-ai-zero-zeno/ | other:openai-threat-intel | 2024-05-01 | STOIC Zero Zeno attribution | OpenAI attributed the Israel-origin Zero Zeno network to STOIC, an Israeli political campaign management firm; it operated across X, Facebook, Instagram, websites and YouTube and targeted audiences in Canada, the United States, Israel and later India. | -
FCT-008 | FACT | ✧ | https://openai.com/index/disrupting-malicious-uses-of-ai-zero-zeno/ | other:openai-threat-intel | 2024-05-01 | STOIC Zero Zeno impact bound | OpenAI rated Zero Zeno Category 2 on the Breakout Scale, with no evidence of significant amplification by people outside the network; one associated YouTube video had zero views as of 25 April 2024. | -
FCT-009 | FACT | ✧ | https://www.reuters.com/technology/meta-identifies-networks-pushing-deceptive-content-likely-generated-by-ai-2024-05-29/ | other:reuters | 2024-05-29 | Meta independent platform attribution of STOIC | Reuters reported that Meta attributed a deceptive campaign using fake civilian personas and likely AI-generated text to Tel Aviv-based political marketing firm STOIC and removed it early. | -
FCT-010 | FACT | ✧ | https://dfrlab.org/2024/03/28/inauthentic-campaign-amplifying-islamophobic-content-targeting-canadians/ | other:dfrlab | 2024-03-28 | Pre-attribution observation of STOIC-related behavior | DFRLab documented an inauthentic campaign using AI-generated photos and inauthentic accounts to amplify Islamophobic content targeting Canadians before subsequent platform attribution to STOIC. | -
FCT-011 | FACT | ✧ | https://www.jpost.com/breaking-news/article-805086 | other:jpost | 2024-06-05 | STOIC government-client attribution contested | Jerusalem Post reported the New York Times claim that Israel’s Diaspora Affairs Ministry allocated about $2 million and engaged STOIC to target US lawmakers and the public, while the Ministry explicitly denied any connection to STOIC and called the claims baseless. | -
FCT-012 | FACT | ✧ | https://www.theguardian.com/world/2023/feb/15/revealed-disinformation-team-jorge-claim-meddling-elections-tal-hanan | other:guardian-storykillers | 2023-02-15 | Team Jorge service bundle and self-claims | Undercover reporting documented Team Jorge offering hacking, sabotage, automated disinformation, intelligence gathering and media-placement services; Tal Hanan claimed involvement in 33 presidential-level campaigns, a claim not established merely by the sales presentation. | -
FCT-013 | FACT | ✧ | https://www.theguardian.com/world/2023/feb/15/aims-software-avatars-team-jorge-disinformation-fake-profiles | other:guardian-storykillers | 2023-02-15 | AIMS marketed versus observed scale | Team Jorge marketed AIMS as controlling more than 30,000 fake profiles, while Guardian/Le Monde/Der Spiegel reporters independently identified a wider network of about 2,000 AIMS-linked bots from disclosed avatars. | -
FCT-014 | FACT | ✧ | https://www.theguardian.com/world/2023/feb/15/political-aides-hacked-by-team-jorge-in-run-up-to-kenyan-election | other:guardian-storykillers | 2023-02-15 | Team Jorge Kenya documented action and effect limit | Undercover demonstration showed access to Telegram accounts of advisers close to William Ruto before Kenya’s 2022 election; the client behind the interference was unknown and the activity did not prevent Ruto winning the election. | -
FCT-015 | FACT | ✧ | https://www.lemonde.fr/pixels/article/2023/02/15/derriere-les-fausses-infos-de-rachid-m-barki-sur-bfm-tv-l-officine-israelienne-team-jorge-et-un-intermediaire-francais_6161862_4408996.html | other:lemonde | 2023-02-15 | BFM media-placement evidence and attribution gap | Le Monde/Forbidden Stories found several BFM-TV segments that bypassed normal editorial validation and matched Team Jorge campaign narratives; Team Jorge displayed one segment as proof of placement, but Jean-Pierre Duthion and Rachid M’Barki denied knowing Team Jorge and the direct intermediary relation remained unresolved. | -
FCT-016 | FACT | ✧ | https://www.lemonde.fr/societe/article/2024/12/16/ingerences-etrangeres-une-confrontation-organisee-chez-le-juge-d-instruction_6452493_3224.html | other:lemonde | 2024-12-16 | French intermediary payment admission is not a Team Jorge attribution | In the broader French foreign-influence judicial case, Le Monde reported that Rachid M’Barki eventually admitted receiving a total of 6,000-8,000 euros from Jean-Pierre Duthion; this establishes a payment relation in that case but does not by itself attribute those payments or every segment to Team Jorge. | -
FCT-017 | FACT | ✧ | https://www.mediapart.fr/en/journal/international/021023/how-swiss-firm-handed-uae-names-1000-supposed-muslim-brotherhood-sympathisers-europe | other:mediapart-eic | 2023-10-02 | Alp Services UAE client and payment chain | Based on hacked Alp Services internal files, Mediapart/EIC reported a first contract in 2017 and at least €5.7 million paid between 2017 and 2020 by Al Ariaf, described in the files/reporting as a cover for UAE intelligence, for operations led by Alp Services. | -
FCT-018 | FACT | ✧ | https://www.mediapart.fr/en/journal/international/021023/how-swiss-firm-handed-uae-names-1000-supposed-muslim-brotherhood-sympathisers-europe | other:mediapart-eic | 2023-10-02 | Alp Services documented tasking and methods | Internal documents reviewed by Mediapart described mapping and discrediting targets through discreet mass dissemination; methods included press campaigns, Wikipedia modification, false-profile op-eds and efforts to induce banks to close accounts; the project covered more than 1,000 individuals and 400 organisations across 18 European countries. | -
FCT-019 | FACT | ✧ | https://www.mediapart.fr/en/journal/international/021023/how-swiss-firm-handed-uae-names-1000-supposed-muslim-brotherhood-sympathisers-europe | other:mediapart-eic | 2023-10-02 | Alp Services rebuttal | Alp Services lawyers told Mediapart that obtained documents were partly falsified and that premises of the questions relied on erroneous suppositions; the UAE government did not answer Mediapart’s questions for the cited investigation. | -
FCT-020 | FACT | ✧ | https://www.mediapart.fr/journal/international/090723/operation-constellation-les-pieds-nickeles-d-abou-dhabi-bruxelles | other:mediapart-eic | 2023-07-09 | Alp Constellation overclaim control | Mediapart reported that Alp Services sold a secret counter-lobbying mission in Brussels to detect, hinder and attack Qatari networks, but found little beyond competitor Avisa and boasted of influence with RN elected officials that the investigation described as imaginary. | -
FCT-021 | FACT | ✧ | https://www.lemonde.fr/societe/article/2025/08/22/accusations-d-espionnage-d-une-communicante-du-qatar-en-france-une-information-judiciaire-ouverte_6633518_3224.html | other:lemonde | 2025-08-22 | Alp alleged surveillance judicial status | Le Monde reported that a French judicial investigation was opened in July 2025 after Sihem Souid’s complaint over alleged surveillance potentially carried out by Alp Services for UAE interests; this is an active allegation under judicial investigation, not a conviction. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-002
FCT-004 | SRC-003
FCT-005 | SRC-003
FCT-006 | SRC-004
FCT-007 | SRC-005
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
FCT-018 | SRC-014
FCT-019 | SRC-014
FCT-020 | SRC-015
FCT-021 | SRC-016

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 LEADS | NEXT_ACTION:7 SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 SCOPE | NEXT_ACTION:9 SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 SEARCH | NEXT_ACTION:10 FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 FACTS | NEXT_ACTION:11 CAUSAL_GAP
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 CAUSAL_GAP | NEXT_ACTION:13 VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 VERIFY | NEXT_ACTION:17 INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18 FINALIZATION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T15:43:49.001715+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":21,"eligible":21,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:21;attempted:0;success:0;failure:0;blocked:21} | WRITEBACK_EXECUTION_V1:[21 rows, see section]

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
