ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-2212-france-puissance-influence-exterieure | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth-engine/investigations/2026-09/2026-09-06_france-puissance-influence-exterieure/2026-09-06_22-12_france-puissance-influence-exterieure_INPUT.md | SUBJECT_SLUG:france-puissance-influence-exterieure | SUBJECT_FP:sha256:e6651bc8c8cbda2d8e81b1bc414a8001bed338177d7dea63ba38dc53cc43a541 | INPUT_SHA256:sha256:12d28e0dcfe9e054848adcedd88cb5073bc28a38297b68e9616dc5c30dc0dc0b
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:2000–2026, sample documentable: French public diplomacy, development aid, international media, cultural/educational networks, governance cooperation, military/intelligence support and documented political interventions; classify visibility, consent, legal basis, coordination, coercion/clandestinity and demonstrated effect.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/POWER.md,clusters/FRAGMENTATION.md,clusters/WAR.md,clusters/NETWORK.md,clusters/ICEBERG.md,clusters/MONEY.md,clusters/FRAMING.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "truth_engine_narrative"
artifact_id: "INV-138"
run_id: "20260906-2212-france-puissance-influence-exterieure"
status: "final_candidate"
updated: "2026-09-06"
---

<!-- TRACE: source=INV-138_RUN_CARD; runtime=Truth_Engine_2.10.6_R3P1 -->
<!-- DECISION: influence!=interference; consent!=no_effect; capability!=tasking; operation!=outcome -->

# INV-138 - France comme puissance d’influence à l’étranger

## Verdict exécutif

La France est, de manière explicite et documentée, une puissance d’influence extérieure. Ce constat n’est ni une accusation ni une inférence. Sa diplomatie présente l’influence comme une fonction stratégique, ses médias internationaux, ses dispositifs de coopération, son aide au développement et ses programmes d’expertise cherchent ouvertement à agir sur des perceptions, des capacités institutionnelles et des relations politiques. Les armées disposent en outre d’une doctrine publique de lutte informatique d’influence conduite hors du territoire national. [FCT-001, FCT-003, FCT-004, FCT-005, FCT-006, FCT-007, FCT-013]

Le résultat central est cependant négatif à l’égard d’une définition extensive de l’ingérence : **l’existence d’une influence étrangère ne suffit pas à établir une ingérence**. Le corpus impose au contraire une classification mécanisme par mécanisme selon la visibilité, le consentement, la base juridique, la relation de commandement, la coercition, la clandestinité et l’effet démontré. [CLM-001, CLM-002]

Le même État français emploie ainsi des instruments qui se situent dans des catégories matériellement différentes : coopération parlementaire transparente et co-construite, financement public de médias internationaux, aide ou expertise institutionnelle, pression par les visas et l’aide au développement, opérations militaires informationnelles, soutien militaire à un gouvernement, soutien armé à un camp dans une guerre civile et activité informationnelle trompeuse liée à des individus associés à l’armée. Les réunir sous une seule étiquette ferait perdre précisément ce que l’investigation cherche à mesurer.

## 1. Influence ouverte et consentie : le contrôle négatif indispensable

Le premier bloc est le plus important méthodologiquement. La France finance des instruments conçus pour renforcer son influence, diffuser des contenus, former des professionnels, appuyer des administrations et accroître les capacités de parlements étrangers. Ces actions peuvent modifier un environnement politique étranger sans être clandestines ni imposées. [FCT-001, FCT-003, FCT-004, FCT-005, FCT-006]

Le programme PACOP constitue le contrôle le plus propre. Financé par le ministère français de l’Europe et des affaires étrangères et mis en œuvre par Expertise France, il vise explicitement à renforcer les capacités législatives, de contrôle et de représentation de parlements du Bénin, du Botswana et du Gabon. Le programme est annoncé, contractuel, co-construit et présenté comme respectueux de la souveraineté des partenaires. [FCT-007]

Il y a donc bien action étrangère sur une capacité institutionnelle politique. Mais aucune des propriétés qui suffiraient à faire de ce seul fait une opération clandestine ou une captation n’est établie. Ce cas interdit de définir l’ingérence par la seule origine étrangère ou par l’intention d’influencer. [CTRL-001, CLM-002]

Le même contrôle vaut pour le financement public de France Médias Monde et pour les programmes d’appui aux médias. Le financement et la finalité d’influence sont documentés. Ils ne prouvent pas, par eux-mêmes, un ordre éditorial sur un contenu particulier, encore moins un changement de vote ou de politique. [FCT-003, FCT-004, FCT-005, CTRL-003]

## 2. Information militaire : une capacité d’État française explicite

La doctrine française de lutte informatique d’influence ferme un autre débat. Les armées définissent publiquement la L2I comme des opérations militaires dans la couche informationnelle du cyberespace, conduites à l’extérieur du territoire national, pouvant inclure renseignement et déception et pouvant être coordonnées avec d’autres ministères ou partenaires. Cette activité relève d’une capacité institutionnelle assumée, organisée et commandée. [FCT-013, CLM-004]

Ce constat est matériel pour le test de symétrie : les opérations informationnelles organisées ne sont pas une catégorie réservée aux adversaires de la France. La France reconnaît elle-même ce type d’instrument dans son action extérieure.

Mais ce fait ne permet pas de franchir une autre frontière probatoire. En décembre 2020, Meta a supprimé un réseau de comptes inauthentiques provenant de France, utilisant de fausses identités et visant plusieurs pays africains. Meta a relié le réseau à des individus associés à l’armée française. Graphika, qui a analysé les actifs, a explicitement maintenu ouverte la question de l’implication institutionnelle du gouvernement ou de l’armée. [FCT-010, FCT-012]

La doctrine L2I fournit donc **capacité et catégorie d’action**, pas le maillon de commandement de l’opération de 2020. Confondre les deux serait exactement l’erreur `capability -> use -> tasking` que le protocole interdit. [CTRL-004]

L’impact du réseau de 2020 doit aussi rester borné. Meta a publié des métriques d’audience modestes et a décrit ultérieurement le réseau comme ayant presque aucune audience au moment de sa suppression. Une opération trompeuse peut exister avec un effet faible. L’existence de l’opération ne doit donc pas être transformée en preuve d’une influence politique massive. [FCT-011, CTRL-005, CLM-011]

## 3. Tchad 2019 : consentement et effet politique direct peuvent coexister

En février 2019, des avions français ont frappé une colonne de l’Union des forces de la résistance qui avançait depuis la Libye et cherchait à renverser le président Idriss Déby. La France a agi après une demande formelle du président tchadien. La réponse française à l’Assemblée nationale invoque cette demande et une base juridique pour justifier l’intervention. [FCT-008]

Le contrôle indépendant apporte l’élément d’effet. L’armée tchadienne a annoncé la capture de plus de 250 rebelles et la destruction de plus de 40 véhicules ; l’armée française a indiqué avoir détruit environ 20 pick-up. Le lien entre l’action française et la dégradation de la force insurgée est donc documenté. [FCT-025]

L’intervention a objectivement favorisé la survie du pouvoir en place face à une tentative armée de renversement. Ce n’est pas la même proposition que de dire que la France a créé la crise, commandé le gouvernement tchadien ou qu’Idriss Déby serait nécessairement tombé sans les frappes. Ce dernier contrefactuel reste non identifié. [CLM-005, CAU-003]

Le cas démontre surtout une règle de méthode : **le consentement du gouvernement cible et la légalité revendiquée modifient la qualification juridique et normative, mais ils n’annulent pas l’effet matériel sur la compétition politique interne**. [CTRL-002, CTRL-006]

## 4. Côte d’Ivoire 2011 : mandat international et modification du rapport de force

En avril 2011, l’ONU a engagé une opération contre les armes lourdes des forces de Laurent Gbagbo. Le Secrétaire général a demandé aux forces françaises de Licorne d’apporter leur soutien à l’ONUCI sur la base des résolutions du Conseil de sécurité. Le cadre international est donc documenté. [FCT-014]

Le ministre français de la Défense a parallèlement reconnu que les forces républicaines favorables à Alassane Ouattara avaient exploité les frappes de l’ONU et de la France pour relancer leur offensive. Il existe ainsi une chaîne matérielle : neutralisation d’armements -> modification du rapport de force -> exploitation par une force ivoirienne -> progression dans la lutte pour le pouvoir. [FCT-015, CLM-006]

Cette chaîne n’autorise pas à attribuer à la France seule la chute de Gbagbo. Elle interdit en revanche de soutenir qu’un mandat international rend l’intervention politiquement neutre par définition. Mandat, légalité, légitimité électorale, intention et effet sont cinq objets distincts. [CAU-004]

## 5. Libye 2011 : le test de l’écart entre mandat, moyens et résultat

La résolution 1973 du Conseil de sécurité autorisait les mesures nécessaires à la protection des civils et excluait une force d’occupation étrangère. Le texte fournit la référence juridique de départ. [FCT-021]

La France a ensuite reconnu avoir parachuté des armes légères et des munitions à des rebelles libyens. Ce soutien matériel à l’un des camps est documenté, même si sa conformité à l’embargo sur les armes a été contestée. [FCT-022]

Enfin, le rapport de l’Assemblée nationale de 2026 décrit rétrospectivement l’intervention franco-britannico-américaine comme ayant conduit au renversement de Mouammar Kadhafi. [FCT-023]

Le dossier établit donc trois niveaux : mandat formel de protection, soutien militaire effectif à la rébellion, puis changement de régime comme résultat historique. Il ne suffit pas à établir que le changement de régime était l’objectif juridique du mandat, ni que la France en fut la cause unique ou nécessaire. [CLM-008, CAU-006]

Ce cas est particulièrement utile pour INV-146 : une comparaison symétrique devra demander, pour toute puissance, si la qualification retenue repose sur le texte juridique, l’action effectivement menée, l’intention documentée ou le résultat obtenu.

## 6. Visas et aide au développement : influence par conditionnalité

En mai 2026, Benjamin Haddad a déclaré que la France et l’Union européenne utilisaient les visas et l’aide au développement afin d’exercer davantage de pression sur les pays de départ et de transit pour obtenir des retours migratoires. Ici, le caractère instrumental n’est pas inféré : il est revendiqué. [FCT-017]

Le rapport du Sénat de 2025 apporte le contrepoids. Il souligne les limites d’une conditionnalité stricte de l’aide, les difficultés pratiques et juridiques d’une suspension et les règles de l’OCDE susceptibles d’exclure de l’aide publique au développement une dépense explicitement conditionnée à un avantage migratoire pour le pays donateur. Il note également les lacunes d’évaluation des politiques précédentes. [FCT-018]

La catégorie la plus fidèle est donc celle d’une **influence conditionnelle ou d’un levier de négociation**, potentiellement coercitif selon sa mise en œuvre. Le corpus ne permet pas de mesurer, pays par pays, le changement de comportement causé par ce levier. [CLM-007, CAU-005]

## 7. Bénin 2025 et Madagascar 2025 : deux interventions à ne pas confondre

Au Bénin, le gouvernement français a confirmé avoir fourni un soutien temporaire d’observation et de logistique pendant la tentative de coup d’État de décembre 2025, à la demande du président Patrice Talon, sans emploi direct de la force par le détachement français décrit dans la réponse parlementaire. [FCT-009, FCT-016]

Ce cas ressemble au Tchad par sa finalité immédiate, soutenir l’autorité en place contre un renversement armé, mais diffère par l’intensité des moyens employés. Il constitue une preuve de soutien politique et sécuritaire direct, non une preuve de contrôle du gouvernement béninois.

À Madagascar, Reuters a rapporté qu’Andry Rajoelina avait quitté le pays à bord d’un avion militaire français pendant la crise d’octobre 2025. Le rapport parlementaire français de 2026 reprend ensuite cette exfiltration comme un fait ayant nourri l’incompréhension sur le rôle de la France. [FCT-019, FCT-020]

Le maillon causal suivant reste ouvert : le corpus public inspecté ne démontre ni le motif politique précis de l’évacuation, ni que cette action a provoqué la prise de pouvoir militaire. La chronologie et l’action sont établies ; l’intention et le contrefactuel ne le sont pas. [CLM-009, CAU-007]

## 8. Soutien à des candidats : une contradiction à conserver, pas à résoudre par intuition

Le rapport parlementaire de 2026 affirme de façon générale que les interférences françaises dans la vie politique africaine se sont aussi traduites récemment par des prises de position et des soutiens favorables ou défavorables à certains gouvernements ou candidats à des élections. [FCT-024]

Mais ce passage ne nomme pas les candidats concernés ni les actes probatoires associés. Il ne peut donc pas être converti en série de cas démontrés.

Un contre-élément institutionnel existe : en 2023, la ministre Catherine Colonna déclarait devant l’Assemblée nationale que la France ne soutenait aucun candidat et parlait avec les gouvernements comme avec les oppositions. [FCT-026]

Les deux propositions ne sont pas logiquement incompatibles sur toute période possible, mais elles créent une contradiction matérielle entre une doctrine publique de non-soutien et une rétrospective parlementaire affirmant des pratiques récentes de soutien ou d’opposition. Sans cas nommés et datés, la résolution est impossible. [CLM-010]

Le bon statut est donc `PARTIAL / SCOPE`, non « faux » et non « prouvé ».

## 9. Modèle de classification résultant

Le corpus ne produit pas une échelle morale unique. Il produit au moins cinq classes opérationnelles :

1. **Influence ouverte et consentie** : diplomatie publique, coopération, programmes parlementaires ou institutionnels. [FCT-001, FCT-006, FCT-007]
2. **Influence par ressources et infrastructures** : médias publics internationaux, soutien aux médias et capacités civiques. [FCT-003, FCT-004, FCT-005]
3. **Influence conditionnelle** : accès, visas, aide ou autres ressources utilisés comme levier de négociation. [FCT-017, FCT-018]
4. **Intervention directe dans un rapport de force** : soutien militaire demandé ou mandaté, frappes, logistique, armement d’un camp. [FCT-008, FCT-014, FCT-015, FCT-016, FCT-022, FCT-025]
5. **Influence trompeuse ou clandestine** : faux comptes, fausses identités, déception ou opérations informationnelles opaques, avec attribution institutionnelle à établir séparément. [FCT-010, FCT-012, FCT-013]

Ces classes peuvent se superposer. Elles ne se convertissent pas automatiquement les unes dans les autres.

## 10. Niveau de preuve I0 à I7

**I0 identité/relation : VERIFIED/PARTIAL.** Les institutions françaises, opérateurs publics et acteurs militaires sont identifiables pour les mécanismes ouverts. Le réseau 2020 est seulement relié à des individus associés à l’armée, pas à un commandement institutionnel. [FCT-010, FCT-012]

**I1 ressources/capacité/accès : VERIFIED.** Financements publics, programmes d’expertise, dispositifs médiatiques, doctrine L2I, moyens militaires et leviers visa/aide sont documentés. [FCT-003, FCT-006, FCT-013, FCT-017]

**I2 action documentée : VERIFIED.** Programmes de coopération, réseau trompeur, frappes, soutien logistique, parachutages d’armes et évacuation sont documentés à des degrés divers. [FCT-007, FCT-010, FCT-014, FCT-016, FCT-019, FCT-022, FCT-025]

**I3 coordination/tasking/contrôle : VERIFIED pour les dispositifs officiels ; PARTIAL/UNKNOWN pour les opérations opaques.** La L2I possède une chaîne de commandement doctrinale. Le réseau Meta 2020 n’a pas de tasking institutionnel public établi. [FCT-012, FCT-013]

**I4 exposition/reach : PARTIAL.** Le réseau Meta dispose de métriques faibles ; les autres mécanismes ont des portées hétérogènes non harmonisées dans ce run. [FCT-011]

**I5 réception/persuasion : NOT_ESTABLISHED généralement.** Les preuves de modification d’opinion ou de persuasion manquent pour les mécanismes non militaires.

**I6 comportement/institution/politique : PARTIAL.** Des effets tactiques directs sont observables au Tchad et en Côte d’Ivoire ; le résultat libyen est majeur mais multicausal. Les effets institutionnels des programmes de coopération ne sont pas isolés causalement. [FCT-015, FCT-023, FCT-025]

**I7 résultat contrefactuel : NOT_ESTABLISHED.** Aucun dossier central ne permet de démontrer que, sans l’action française, le résultat politique final aurait nécessairement été différent.

## 11. Ce que l’investigation change

Le principal delta n’est pas « la France ingère elle aussi ». Cette formulation serait trop grossière pour les preuves obtenues.

Le delta robuste est : **les mécanismes que la France utilise à l’étranger couvrent plusieurs catégories également observées chez les puissances étudiées lorsqu’elles visent la France, depuis l’influence ouverte jusqu’à l’action militaire et à l’influence trompeuse. Leur qualification dépend de propriétés matérielles, non de l’identité alliée ou adverse de l’émetteur.** [CLM-001]

Deux conséquences suivent.

Premièrement, une méthode symétrique doit reconnaître comme « influence » les activités françaises transparentes exactement comme elle le ferait pour une autre puissance, sans les promouvoir automatiquement au rang d’ingérence.

Deuxièmement, lorsqu’apparaissent tromperie, clandestinité, soutien à un camp, coercition ou modification directe d’un rapport de force interne, ces propriétés doivent être examinées avec les mêmes seuils de preuve, y compris lorsque l’acteur est français ou allié.

C’est précisément le matériau dont `INV-146` aura besoin pour tester les asymétries de vocabulaire et de seuil probatoire.

## Périmètre et limites

Le run ne démontre pas une architecture française unique de contrôle extérieur. Les instruments appartiennent à des institutions différentes, répondent à des bases juridiques différentes et poursuivent des finalités différentes. Une convergence de politique étrangère n’est pas un commandement opérationnel commun. [CLM-001]

Le tasking institutionnel du réseau Meta 2020 reste ouvert. [CLM-003]

Les récents cas de soutien ou d’opposition à des candidats évoqués par le rapport parlementaire ne sont pas individualisés dans le passage inspecté et restent un gap de périmètre. [CLM-010]

La causalité politique forte est rarement identifiable. Les cas militaires documentent mieux les actions et certains effets intermédiaires que les mécanismes médiatiques ou de coopération, mais même eux ne ferment généralement pas I7. [CLM-011, CAU-003, CAU-004, CAU-006]

Ces limites ne justifient pas une collecte générique supplémentaire. Elles demandent des pièces spécifiques : documents de tasking, déclassifications, cas électoraux nommés ou designs causaux. En leur absence, le protocole impose de conserver le gap plutôt que de remplir la chaîne par inférence.
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:7|EDI_DECISIVE:7|SRC_COMPLETE:22/22

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **anchor_events:**
  - 2011 Côte d’Ivoire and Libya
  - 2019 Chad strikes
  - 2020 Meta/Graphika CIB exposure
  - 2021 L2I doctrine
  - 2025 Benin coup support and Madagascar evacuation
  - 2026 parliamentary and policy reassessments
- **as_of:** 2026-09-06
- **rules:**
  - event date != publication date != investigation date
  - later parliamentary retrospective does not establish contemporaneous intent
  - current doctrine cannot be back-projected to prove 2020 tasking
- **window:** 2000–2026

### MANIPULATION_REPORT
- **assumptions:**
  - public evidence may under-observe covert tasking
  - host-state consent can be genuine, constrained or contested and must be evidenced case by case
  - political outcome may occur without being the stated legal objective
- **clusters:**
  - **loaded:**
    - clusters/POWER.md
    - clusters/FRAGMENTATION.md
    - clusters/WAR.md
    - clusters/NETWORK.md
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - France-as-sender is a symmetry control, not an accusation
  - open influence and clandestine influence must remain separate
  - consent/legal basis alter classification but not physical effect
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - classification asymmetry
  - mandate/consent compression
  - capability-to-attribution jump
  - operation-to-effect jump
  - aggregate-to-case extrapolation
- **priorities:**
  - direct official/operator records
  - independent platform/investigative corroboration
  - named case chains
  - effect/counterfactual limits
- **query_guidance:** trace France -> instrument/intermediary -> foreign target -> documented action -> consent/legal basis -> exposure -> effect; do not infer command from affiliation or effect from operation existence
- **rhetorical:**
  - **AUTH:** N/A
  - **BF:** N/A
  - **DEM:** N/A
  - **FAC:** N/A
  - **NUM:** N/A
- **speaker:**
  - **goal:** symmetrical evidentiary standard
  - **target:** mechanism classification
  - **tone:** forensic
- **symbol_stage:** CORPUS_FINAL
- **symbols:**
  - **Κ:** 3
  - **Λ:** 4
  - **Ξ:** 4
  - **Σ:** 2
  - **Φ:** 2
  - **Ψ:** 2
  - **Ω:** 3
  - **κ:** 2
  - **ρ:** 4
  - **€:** 4
  - **↕:** 6
  - **⏰:** 4
  - **⚔:** 7
  - **⫸:** 5
  - **🌐:** 6
- **threats:**
  - foreign=interference
  - legal=legitimate
  - funding=command
  - capability=use
  - operation=result_changed
  - official_assessment=case_proof

### MODULE_EXECUTION
- **item 1:**
  - **gaps:**
    - deferred to INV-146 comparative synthesis
  - **input_ids:**
    - CLM-001
    - CLM-005
    - CLM-006
    - CLM-007
    - CLM-008
  - **module:** clusters/POWER.md
  - **negative_results:**
    - no general unequal-enforcement conclusion inside INV-138
  - **not_computable:**
    - global ally/adversary double-standard rate
  - **operations_applied:**
    - defined comparison baseline
    - separated legal/consent status from material effect
  - **reason:** compare consent, leverage, mandate and accountability across equivalent foreign-influence mechanisms
  - **result_ids:**
    - CTRL-006
    - CLM-001
    - CLM-007
  - **status:** DONE
  - **trigger:** ↕=6
- **item 2:**
  - **gaps:**
    - cross-case synthesis belongs to INV-146/INV-133
  - **input_ids:**
    - CLM-001
    - CLM-003
    - CLM-004
    - CLM-005
    - CLM-006
    - CLM-007
    - CLM-008
  - **module:** clusters/FRAGMENTATION.md
  - **negative_results:**
    - no evidence of one central command architecture across all mechanisms
  - **not_computable:**
    - convergence ratio across unlike mechanisms
  - **operations_applied:**
    - deduplicated source families
    - kept institutional/tasking edges separate
  - **reason:** test whether heterogeneous French mechanisms form one coordinated architecture or only a portfolio of distinct instruments
  - **result_ids:**
    - CLM-001
    - CTRL-004
  - **status:** DONE
  - **trigger:** ⫸=5
- **item 3:**
  - **gaps:**
    - RESPONSIBILITY gap retained
  - **input_ids:**
    - FCT-010
    - FCT-012
    - FCT-013
  - **module:** clusters/WAR.md
  - **negative_results:**
    - no public institutional tasking bridge for 2020 Meta network
  - **not_computable:**
    - hidden command chain
  - **operations_applied:**
    - separated infrastructure from state attribution
    - tested targeting and tasking boundary
  - **reason:** organized military and deceptive information operations are directly in scope
  - **result_ids:**
    - CLM-003
    - CLM-004
    - CTRL-004
    - CTRL-005
  - **status:** DONE
  - **trigger:** ⚔=7
- **item 4:**
  - **gaps:**
    - systemic architecture deferred to synthesis
  - **input_ids:**
    - FCT-001
    - FCT-003
    - FCT-006
    - FCT-007
    - FCT-013
    - FCT-017
  - **module:** clusters/NETWORK.md
  - **negative_results:**
    - no single central operational controller established across diplomatic, media, aid and military mechanisms
  - **not_computable:**
    - network centrality without exhaustive actor universe
  - **operations_applied:**
    - typed actor-resource-action edges
    - excluded co-occurrence as control
  - **reason:** multiple state agencies, operators, partner governments and intermediaries form typed influence chains
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-004
    - CLM-007
  - **status:** DONE
  - **trigger:** 🌐=6
- **item 5:**
  - **gaps:**
    - RESPONSIBILITY/SCOPE/CAUSALITY retained
  - **input_ids:**
    - CLM-003
    - CLM-009
    - CLM-010
    - CLM-011
  - **module:** clusters/ICEBERG.md
  - **negative_results:**
    - no basis to reconstruct hidden command chains from affiliation alone
  - **not_computable:**
    - true prevalence of covert French operations
  - **operations_applied:**
    - made hidden/absent evidence explicit rather than inferred
    - separated unavailable tasking from negative finding
  - **reason:** material under-observation risks concern covert tasking, named candidate cases and counterfactual effects
  - **result_ids:**
    - CLM-003
    - CLM-009
    - CLM-010
    - CLM-011
  - **status:** DONE
  - **trigger:** Ξ=4 lower mandatory review
- **item 6:**
  - **gaps:**
    - country-level leverage effects not quantified
  - **input_ids:**
    - FCT-003
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
    - FCT-017
    - FCT-018
  - **module:** clusters/MONEY.md
  - **negative_results:**
    - funding alone did not establish command or outcome
  - **not_computable:**
    - full cross-program financial total
  - **operations_applied:**
    - traced payer-to-instrument-to-target
    - separated funding from editorial/political command
  - **reason:** state media, development aid and governance projects involve material public resource flows
  - **result_ids:**
    - CLM-001
    - CLM-002
    - CLM-007
    - CTRL-003
  - **status:** DONE
  - **trigger:** €=4 lower mandatory review
- **item 7:**
  - **gaps:**
    - comparative framing deferred to INV-146
  - **input_ids:**
    - CLM-001
    - CLM-005
    - CLM-006
    - CLM-008
    - CLM-010
  - **module:** clusters/FRAMING.md
  - **negative_results:**
    - different labels alone do not establish a double standard
  - **not_computable:**
    - systematic vocabulary asymmetry before INV-146
  - **operations_applied:**
    - reconstructed legal/official frames beside material actions
    - kept vocabulary separate from evidence chain
  - **reason:** labels diplomacy, influence, interference, support and regime change can collapse distinct mechanisms
  - **result_ids:**
    - CLM-001
    - CTRL-006
    - CLM-010
  - **status:** DONE
  - **trigger:** Λ=4 lower mandatory review

### SCOPING_REPORT
- **classification_dimensions:**
  - visibility
  - consent
  - legal_basis
  - funding_tasking
  - coordination
  - coercion
  - clandestinity
  - exposure
  - effect
- **exclusions:**
  - influence=interference by definition
  - funding=command
  - consent=absence of influence
  - official characterization=proof
- **scope:** 2000–2026; France as sender; documentable foreign-political influence mechanisms
- **status:** ACTIVE

### CREDO
- influence != interference
- foreign != interference
- legal != legitimate
- consent != no influence
- funding != command
- capability != use
- affiliation != tasking
- direct action != sole causation
- operation exists != result changed
- aggregate assessment != named-case proof

### COGNITIVE_MAP
- **causal_boundary:** Public evidence identifies several direct actions and some tactical/institutional effects, but rarely persuasion, electoral change or I7 counterfactual outcomes.
- **continuum:**
  - open public diplomacy/media/cooperation
  - conditional leverage
  - military information operations
  - direct security intervention
  - deceptive/covert activity
- **core_model:** France operates a plural portfolio of external influence instruments. Classification is mechanism-specific and depends on visibility, consent, legal basis, tasking, coercion/clandestinity and effect.
- **rival_models:**
  - ordinary diplomacy/cooperation
  - strategic state influence
  - conditional/coercive bargaining
  - legally mandated intervention with political side-effects
  - deliberate domestic political interference
  - covert state operation

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** PACOP and open diplomacy intentionally shape capacity/ideas with transparency and consent
  - **resolution:** classify mechanism, visibility, consent, legality and effect separately
  - **thesis:** Any foreign attempt to shape politics is interference
- **item 2:**
  - **antithesis:** official L2I doctrine includes deception and influence operations outside France
  - **resolution:** state capability/practice category is documented; specific covert attribution still requires tasking evidence
  - **thesis:** French military influence activity is only defensive communication
- **item 3:**
  - **antithesis:** Côte d’Ivoire and Chad show direct changes to internal force balances
  - **resolution:** legal/consent classification and material political effect are distinct variables
  - **thesis:** UN/host consent means no political interference effect
- **item 4:**
  - **antithesis:** Libya Resolution 1973 formally centered civilian protection while intervention and rebel support preceded Gaddafi overthrow
  - **resolution:** keep legal objective, operational support, intent and outcome as separate edges
  - **thesis:** Regime-change outcome proves regime-change mandate/intent

### RESOURCE_FLOW_MAP
- **item 1:**
  - **from:** French state/public financing
  - **limits:**
    - editorial tasking not established by funding alone
  - **resource:** broadcast/media capacity
  - **support:**
    - FCT-003
  - **to:** international audiences
  - **via:** France Médias Monde
- **item 2:**
  - **from:** MEAE/AFD
  - **limits:**
    - partner agency and consent vary by project
  - **resource:** grants, expertise, training, institutional capacity
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-006
    - FCT-007
  - **to:** foreign institutions/civil society/media
  - **via:** Expertise France/PACOP/media projects
- **item 3:**
  - **from:** French armed forces
  - **limits:**
    - specific tasking/effect case-dependent
  - **resource:** information operations, intelligence, logistics, kinetic force
  - **support:**
    - FCT-013
    - FCT-016
    - FCT-025
  - **to:** foreign information/military environments
  - **via:** COMCYBER/L2I and deployed forces
- **item 4:**
  - **from:** French policy leverage
  - **limits:**
    - implementation/effect not quantified
  - **resource:** access and financial cooperation conditions
  - **support:**
    - FCT-017
    - FCT-018
  - **to:** countries of origin/transit
  - **via:** visas and development aid
- **item 5:**
  - **from:** France
  - **limits:**
    - France-specific counterfactual contribution not isolated
  - **resource:** light weapons and ammunition
  - **support:**
    - FCT-022
  - **to:** Libyan rebel forces
  - **via:** airdrop

### ACTOR_NETWORK_MAP
- **item 1:**
  - **from:** French executive/MEAE
  - **limits:**
    - portfolio is not proof of unitary operational command
  - **relation:** strategy, funding and diplomacy
  - **support:**
    - FCT-001
    - FCT-003
    - FCT-004
    - FCT-006
    - FCT-007
  - **to:** FMM/AFD/Expertise France/foreign partners
- **item 2:**
  - **from:** French armed forces/CEMA/COMCYBER
  - **limits:**
    - does not identify operator of 2020 Meta network
  - **relation:** commanded L2I capability outside France
  - **support:**
    - FCT-013
  - **to:** military information environment
- **item 3:**
  - **from:** individuals associated with French military
  - **limits:**
    - institutional tasking unknown
    - reach low
  - **relation:** Meta/Graphika-linked deceptive network
  - **support:**
    - FCT-010
    - FCT-012
  - **to:** African social-media audiences
- **item 4:**
  - **from:** French forces
  - **limits:**
    - different legal bases and effects; do not merge
  - **relation:** requested/mandated military support
  - **support:**
    - FCT-008
    - FCT-014
    - FCT-016
    - FCT-025
  - **to:** Chad/Benin/Côte d’Ivoire cases
- **item 5:**
  - **from:** France
  - **limits:**
    - multi-actor coalition/outcome
  - **relation:** arms support
  - **support:**
    - FCT-022
  - **to:** Libyan rebels

### IMPACT_MAP
- **I0_I3_high:**
  - identity/resources/actions documented for open diplomacy, media, cooperation, L2I doctrine and multiple military cases
- **I4_partial:**
  - Meta network audience quantified but small; broadcast/cooperation reach exists but not uniformly measured in this run
- **I5_not_established:**
  - no robust persuasion estimates for central non-military mechanisms
- **I6_partial:**
  - direct tactical/institutional changes documented in Chad and Côte d’Ivoire; Libya outcome associated with intervention; project-level governance capacity changes intended but downstream decisions not isolated
- **I7_not_established:**
  - no general counterfactual attribution of election/regime/policy outcomes to France alone
- **downstream:** Provides France-as-sender controls for INV-146; candidate-specific and covert-tasking residuals remain bounded.

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Graphika says no evidence of institutional French governmental/military involvement
  - **issue:** 2020 deceptive network attribution
  - **pro:** Meta linked network to individuals associated with French military
  - **resolution:** INDIVIDUAL_ASSOCIATION_VERIFIED_INSTITUTIONAL_TASKING_OPEN
- **item 2:**
  - **contra:** 2026 National Assembly report itself describes interventions and recent support/opposition to governments/candidates as interference
  - **issue:** non-interference norm vs practice
  - **pro:** French policy/official discourse invokes consent, mandates and sovereignty
  - **resolution:** NORM_AND_REPORTED_PRACTICE_COEXIST_CASE_PROOF_REQUIRED
- **item 3:**
  - **contra:** France supplied rebels and parliamentary retrospective states intervention led to Gaddafi overthrow
  - **issue:** Libya legal objective vs outcome
  - **pro:** Resolution 1973 centered civilian protection
  - **resolution:** FORMAL_MANDATE_NOT_EQUAL_OUTCOME_OR_FULL_INTENT
- **item 4:**
  - **contra:** support directly protected incumbent authorities against armed overthrow attempts
  - **issue:** host consent vs internal political effect
  - **pro:** Chad/Benin requested French support
  - **resolution:** CONSENT_CHANGES_CLASSIFICATION_NOT_MATERIAL_EFFECT

### VERIFICATION_REPORT
- **analytical_secondary_role:** 6
- **direct_primary_role:** 16
- **independence_limits:**
  - several claims depend on French institutional self-description
  - Reuters/Euronews is one newsroom family
  - 2026 parliamentary report is a retrospective synthesis, not contemporaneous tasking evidence
- **negative_checks:**
  - no institutional tasking proof for 2020 CIB
  - no general candidate-level contemporary case chain from aggregate report
  - no broad persuasion/electoral causal design
  - 2023 official no-candidate-support statement retained against 2026 aggregate parliamentary claim
- **source_families:** 16
- **source_records_complete:** 22/22
- **status:** PASS_WITH_EXPLICIT_GAPS
- **web_fact_trace:** 26/26 facts mapped to accepted sources with current FETCH for evidence URLs

### EDI_REPORT
- **corpus:**
  - **circularity:** CONTROLLED_BY_FAMILY_DEDUP
  - **coverage:** MATERIAL_MECHANISM_FAMILIES_COVERED
  - **independence:** MIXED_HIGH
  - **limits:**
    - classified/covert evidence unavailable
    - electoral candidate aggregate claim under-specified
    - effect measurement sparse
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **gap_type:** NONE
    - **independent_families:** MULTIPLE
  - **item 2:**
    - **claim_id:** CLM-003
    - **direct_object:** YES_PARTIAL_ATTRIBUTION
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 2
  - **item 3:**
    - **claim_id:** CLM-005
    - **direct_object:** YES
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
  - **item 4:**
    - **claim_id:** CLM-006
    - **direct_object:** YES
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
  - **item 5:**
    - **claim_id:** CLM-007
    - **direct_object:** YES_POLICY
    - **gap_type:** CAUSALITY
    - **independent_families:** 2
  - **item 6:**
    - **claim_id:** CLM-008
    - **direct_object:** YES
    - **gap_type:** RESPONSIBILITY
    - **independent_families:** 3
  - **item 7:**
    - **claim_id:** CLM-011
    - **direct_object:** PARTIAL
    - **gap_type:** CAUSALITY
    - **independent_families:** MULTIPLE
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** MULTI_COUNTRY
  - **owner:** 16_PROVENANCE_FAMILIES
  - **perspective:** OFFICIAL+PLATFORM+INDEPENDENT_MEDIA+PARLIAMENTARY
  - **stratification:** DIRECT_RECORDS_AND_SECONDARY_CORROBORATION
  - **temporal:** 2011-2026_PLUS_POLICY_CONTEXT
- **edi:**
  - **assessment:** HIGH_DIVERSITY_WITH_INSTITUTIONAL_DEPENDENCE
  - **flags:**
    - OFFICIAL_SELF_DESCRIPTION
    - RETROSPECTIVE_PARLIAMENTARY_SYNTHESIS
    - SINGLE_NEWSROOM_REUTERS_SUBCASES
    - COVERT_TASKING_OPACITY
    - CAUSAL_EFFECT_LIMITS
- **source_counts:**
  - **primary:** 16
  - **provenance_families:** 16
  - **secondary:** 6
  - **total:** 22

### RESPONSIBILITY_MAP
- **item 1:**
  - **highest_supported:** individuals associated with French military
  - **not_supported:** French military institutional command/tasking
  - **object:** 2020 Meta network
  - **support:**
    - FCT-010
    - FCT-012
    - FCT-013
- **item 2:**
  - **highest_supported:** French armed forces institutional capability and command structure for L2I category
  - **not_supported:** link to any specific observed covert campaign absent case evidence
  - **object:** L2I doctrine
  - **support:**
    - FCT-013
- **item 3:**
  - **highest_supported:** French government/armed forces knowingly supported incumbent at his request and struck rebels
  - **not_supported:** France as sole cause of regime survival
  - **object:** Chad 2019
  - **support:**
    - FCT-008
    - FCT-025
- **item 4:**
  - **highest_supported:** UN-requested French military support altered force balance used by Ouattara-aligned forces
  - **not_supported:** France as sole cause of Gbagbo fall
  - **object:** Côte d’Ivoire 2011
  - **support:**
    - FCT-014
    - FCT-015
- **item 5:**
  - **highest_supported:** French intervention and arms support to rebels; regime-change outcome occurred
  - **not_supported:** regime change as sole/fully documented French operational intent or sole causation
  - **object:** Libya 2011
  - **support:**
    - FCT-021
    - FCT-022
    - FCT-023
- **item 6:**
  - **highest_supported:** French military aircraft evacuated Rajoelina
  - **not_supported:** French causation of military takeover or documented political purpose
  - **object:** Madagascar 2025
  - **support:**
    - FCT-019
    - FCT-020

### NEXT_QUERIES
- **item 1:**
  - **query:** named recent candidate-level French support/opposition with primary records
  - **route:** RECHECK
  - **trigger:** new documentary or archival evidence
- **item 2:**
  - **query:** 2020 France-origin CIB institutional tasking records or official investigation
  - **route:** RECHECK
  - **trigger:** declassification, judicial/platform disclosure or official admission
- **item 3:**
  - **query:** country-level causal evaluation of visa/development-aid migration leverage
  - **route:** DEFER
  - **trigger:** quantitative policy evaluation
- **item 4:**
  - **query:** ally/adversary isomorphic mechanism comparison
  - **route:** MERGE
  - **trigger:** INV-146 after INV-139/140/145

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-022,QRY-023 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-012 | support:- | counter:- | results:FCT-001,FCT-013 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-003,QRY-004,QRY-010,QRY-011 | support:- | counter:- | results:FCT-003,FCT-004,FCT-005,FCT-010,FCT-011,FCT-012 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-005,QRY-016,QRY-017 | support:- | counter:- | results:FCT-005,FCT-017,FCT-018 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-006,QRY-007 | support:- | counter:- | results:FCT-006,FCT-007 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-008,QRY-009,QRY-013,QRY-014,QRY-015,QRY-019,QRY-020,QRY-021 | support:- | counter:- | results:FCT-008,FCT-009,FCT-014,FCT-015,FCT-016,FCT-021,FCT-022,FCT-023,FCT-025 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-002,QRY-013,QRY-014,QRY-023 | support:- | counter:- | results:FCT-002,FCT-014,FCT-015,FCT-024,FCT-026 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-010,QRY-011,QRY-012,QRY-018 | support:- | counter:- | results:FCT-010,FCT-012,FCT-013,FCT-019,FCT-020 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025 | final:SATURATED | gap:NONE
AXS-009 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015,QRY-016,QRY-017,QRY-018,QRY-019,QRY-020,QRY-021,QRY-023 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022,FCT-023,FCT-024,FCT-025,FCT-026 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-001,QRY-003,QRY-006,QRY-007,QRY-012,QRY-016,QRY-022,SRC-001,SRC-003,SRC-006,SRC-007,SRC-012,SRC-016,SRC-021 | support:FCT-001,FCT-003,FCT-006,FCT-007,FCT-013,FCT-017,FCT-025 | counter:CTRL-001;CTRL-002;CTRL-003 | results:FCT-001,FCT-003,FCT-006,FCT-007,FCT-013,FCT-017,FCT-025,CTRL-001;CTRL-002;CTRL-003 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-006,QRY-007,SRC-006,SRC-007 | support:FCT-006,FCT-007 | counter:- | results:FCT-006,FCT-007 | final:SUPPORTED | gap:CAUSALITY
CLM-003 | attempts:QRY-010,QRY-011,QRY-012,SRC-010,SRC-011,SRC-012 | support:FCT-010,FCT-012,FCT-013 | counter:French armed forces possess public L2I doctrine/capability (FCT-013),which is capability evidence but not a bridge to the 2020 network. | results:FCT-010,FCT-012,FCT-013,French armed forces possess public L2I doctrine/capability (FCT-013),which is capability evidence but not a bridge to the 2020 network. | final:PARTIAL | gap:RESPONSIBILITY
CLM-004 | attempts:QRY-012,SRC-012 | support:FCT-013 | counter:The doctrine is bounded to military operations and does not prove use in every observed France-origin information campaign. | results:FCT-013,The doctrine is bounded to military operations and does not prove use in every observed France-origin information campaign. | final:SUPPORTED | gap:NONE
CLM-005 | attempts:QRY-008,QRY-022,SRC-008,SRC-021 | support:FCT-008,FCT-025 | counter:Host-government request and French legal justification (FCT-008) alter legal/consent classification; they do not negate the direct military effect. | results:FCT-008,FCT-025,Host-government request and French legal justification (FCT-008) alter legal/consent classification; they do not negate the direct military effect. | final:PARTIAL | gap:CAUSALITY
CLM-006 | attempts:QRY-013,QRY-014,SRC-013,SRC-014 | support:FCT-014,FCT-015 | counter:The intervention had a UN mandate and was framed as civilian/UN protection in a post-election crisis where the UN recognized Ouattara; legality and legitimacy are distinct from material political effect. | results:FCT-014,FCT-015,The intervention had a UN mandate and was framed as civilian/UN protection in a post-election crisis where the UN recognized Ouattara; legality and legitimacy are distinct from material political effect. | final:PARTIAL | gap:CAUSALITY
CLM-007 | attempts:QRY-016,QRY-017,SRC-016,SRC-017 | support:FCT-017,FCT-018 | counter:Pressure can be lawful diplomacy/conditional cooperation and does not by itself establish clandestine interference. | results:FCT-017,FCT-018,Pressure can be lawful diplomacy/conditional cooperation and does not by itself establish clandestine interference. | final:PARTIAL | gap:CAUSALITY
CLM-008 | attempts:QRY-002,QRY-019,QRY-020,SRC-002,SRC-019,SRC-020 | support:FCT-021,FCT-022,FCT-023 | counter:Resolution 1973 excluded occupation and stated civilian protection; multiple NATO and Libyan actors contributed to the outcome. | results:FCT-021,FCT-022,FCT-023,Resolution 1973 excluded occupation and stated civilian protection; multiple NATO and Libyan actors contributed to the outcome. | final:PARTIAL | gap:RESPONSIBILITY
CLM-009 | attempts:QRY-002,QRY-018,SRC-002,SRC-018 | support:FCT-019,FCT-020 | counter:The crisis already involved mass protest,military defections and institutional conflict; evacuation can have protective rather than regime-shaping purposes. | results:FCT-019,FCT-020,The crisis already involved mass protest,military defections and institutional conflict; evacuation can have protective rather than regime-shaping purposes. | final:PARTIAL | gap:RESPONSIBILITY
CLM-010 | attempts:QRY-002,QRY-023,SRC-002,SRC-022 | support:FCT-024 | counter:FCT-026 | results:FCT-024,FCT-026 | final:PARTIAL | gap:SCOPE
CLM-011 | attempts:QRY-003,QRY-004,QRY-005,QRY-007,QRY-010,QRY-022,SRC-003,SRC-004,SRC-005,SRC-007,SRC-010,SRC-021 | support:FCT-003,FCT-004,FCT-005,FCT-007,FCT-011,FCT-025 | counter:Absence of measured effect is not proof of zero effect. | results:FCT-003,FCT-004,FCT-005,FCT-007,FCT-011,FCT-025,Absence of measured effect is not proof of zero effect. | final:PARTIAL | gap:CAUSALITY

## STATUS_DELTA_V1
DELTA-001 | CAU-003 | PARTIAL_SUPPORTED | UNRESOLVED | preserve causal boundary
DELTA-002 | CAU-004 | PARTIAL_SUPPORTED | UNRESOLVED | preserve causal boundary
DELTA-003 | CAU-006 | PARTIAL_SUPPORTED | UNRESOLVED | preserve causal boundary
DELTA-004 | AXS-001 | PLANNED | SATURATED | axis research completed to public-evidence boundary
DELTA-005 | AXS-002 | PLANNED | SATURATED | axis research completed to public-evidence boundary
DELTA-006 | AXS-003 | PLANNED | SATURATED | axis research completed to public-evidence boundary
DELTA-007 | AXS-004 | PLANNED | SATURATED | axis research completed to public-evidence boundary
DELTA-008 | AXS-005 | PLANNED | SATURATED | axis research completed to public-evidence boundary
DELTA-009 | AXS-006 | PLANNED | SATURATED | axis research completed to public-evidence boundary
DELTA-010 | AXS-007 | PLANNED | SATURATED | axis research completed to public-evidence boundary
DELTA-011 | AXS-008 | PLANNED | SATURATED | axis research completed to public-evidence boundary
DELTA-012 | AXS-009 | PLANNED | SATURATED | axis research completed to public-evidence boundary
DELTA-013 | LED-001 | ACTIVE | SATURATED | lead saturated at scoped public-evidence boundary
DELTA-014 | LED-002 | ACTIVE | SATURATED | lead saturated at scoped public-evidence boundary
DELTA-015 | CLM-003 | SUPPORTED_WITH_LIMIT | PARTIAL | terminal status with explicit evidentiary limit
DELTA-016 | CLM-005 | SUPPORTED_WITH_LIMIT | PARTIAL | terminal status with explicit evidentiary limit
DELTA-017 | CLM-006 | SUPPORTED_WITH_LIMIT | PARTIAL | terminal status with explicit evidentiary limit
DELTA-018 | CLM-007 | SUPPORTED_WITH_LIMIT | PARTIAL | terminal status with explicit evidentiary limit
DELTA-019 | CLM-008 | SUPPORTED_WITH_LIMIT | PARTIAL | terminal status with explicit evidentiary limit
DELTA-020 | CLM-009 | SUPPORTED_WITH_LIMIT | PARTIAL | terminal status with explicit evidentiary limit
DELTA-021 | CLM-011 | SUPPORTED_WITH_LIMIT | PARTIAL | terminal status with explicit evidentiary limit

## OPEN_GAPS_V1
CLM-002 | CLM | SUPPORTED | CAUSALITY | Measured downstream political effects remain sparse.
CLM-003 | CLM | PARTIAL | RESPONSIBILITY | No public tasking/command document or institutional admission links the CIB network to French military command.
CLM-005 | CLM | PARTIAL | CAUSALITY | Regime-survival counterfactual is not identified.
CLM-006 | CLM | PARTIAL | CAUSALITY | The marginal counterfactual contribution of French action to Gbagbo’s ultimate fall is not isolated.
CLM-007 | CLM | PARTIAL | CAUSALITY | Country-level implementation and behavioral effect are not established from the inspected general policy statements.
CLM-008 | CLM | PARTIAL | RESPONSIBILITY | French intent to achieve regime change as an operational objective and the counterfactual contribution of arms/strikes are not fully established by the inspected public sources.
CLM-009 | CLM | PARTIAL | RESPONSIBILITY | Purpose/tasking rationale and counterfactual political effect remain unresolved.
CLM-010 | CLM | PARTIAL | SCOPE | The 2023 official no-candidate-support position conflicts with the 2026 parliamentary aggregate statement that recent support/opposition to candidates occurred; the aggregate passage does not name cases, so the discrepancy cannot be resolved at case level.
CLM-011 | CLM | PARTIAL | CAUSALITY | Most non-military mechanisms lack causal designs linking exposure to behavior or policy change.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | Specific policy decisions caused by French assistance are not isolated.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | Persuasion, behavior, electoral effect and institutional tasking are not established.
CAU-003 | CAU | UNRESOLVED | CAUSALITY | No valid counterfactual establishes whether Déby would have fallen absent French strikes.
CAU-004 | CAU | UNRESOLVED | CAUSALITY | Marginal French causal contribution to the final transfer of power is not isolated.
CAU-005 | CAU | UNRESOLVED | CAUSALITY | No country-level causal estimate in inspected sources establishes how much behavior changed because of aid/visa pressure.
CAU-006 | CAU | UNRESOLVED | CAUSALITY | Regime-change intent and France-specific counterfactual contribution remain incompletely identified.
CAU-007 | CAU | UNRESOLVED | CAUSALITY | Purpose and causal effect on military takeover are not established.

SEMANTIC_COUNTS_V1:LED:2|CLM:11|AXS:9|CAU:7|CTRL:7|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023"],"evidence_excerpt":"classify visibility, consent, legal basis, coordination, coercion/clandestinity and demonstrated effect","kind":"HYPOTHESIS","lead":"France uses an explicit portfolio of foreign-influence instruments ranging from transparent/consensual diplomacy and cooperation to coercive or direct intervention; classification must be mechanism-by-mechanism rather than actor-by-actor.","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006","AXS-007","AXS-008","AXS-009","CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009","CLM-010","CLM-011"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"],"routes":["OBJECT_INVESTIGATION","MECHANISMS","COUNTER_HYPOTHESES"],"source_id":"INV-138_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-022","QRY-023"],"evidence_excerpt":"Do not call aid, media or diplomacy interference by nature","kind":"METHOD_CONSTRAINT","lead":"Influence, interference and illegality are not synonyms: transparent funding or technical cooperation can change institutions while remaining consented and lawful; military or covert support requires separate tests of consent, legal basis, tasking and effect.","linked_ids":["CTRL-001","CTRL-002","CTRL-003","CTRL-004","CTRL-005","CTRL-006","CTRL-007"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"],"routes":["RULES_CONTROLS","COUNTER_HYPOTHESES"],"source_id":"INV-138_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"France uses a documented portfolio of foreign influence mechanisms spanning open public diplomacy, state-funded media and governance cooperation, explicit policy leverage, military information operations and direct security interventions; these mechanisms cannot be assigned one global label without testing visibility, consent, legality, tasking and effect separately.","claimant":"INV-138 synthesis","counter":"CTRL-001;CTRL-002;CTRL-003","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-003","FCT-006","FCT-007","FCT-013","FCT-017","FCT-025"]}
CLM-002 | {"claim":"Transparent and consented French support can intentionally change foreign political or institutional capacity without sufficient evidence to classify it as interference: PACOP and governance cooperation are positive evidence of influence but negative controls against foreign=inference of interference.","claimant":"INV-138 synthesis","counter":"NONE_FOUND","gap":"Measured downstream political effects remain sparse.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-006","FCT-007"]}
CLM-003 | {"claim":"The 2020 France-origin social-media network was a deceptive coordinated influence operation linked by Meta to individuals associated with the French military, but the public evidence inspected does not establish direct institutional tasking by the French Government or armed forces.","claimant":"INV-138 synthesis","counter":"French armed forces possess public L2I doctrine/capability (FCT-013), which is capability evidence but not a bridge to the 2020 network.","gap":"No public tasking/command document or institutional admission links the CIB network to French military command.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-010","FCT-012","FCT-013"]}
CLM-004 | {"claim":"French military doctrine explicitly authorizes commanded information-influence operations outside national territory, including deception and coordination with other ministries or allies; therefore military information influence is a documented French state capability and practice category, not merely an allegation about adversaries.","claimant":"INV-138 synthesis","counter":"The doctrine is bounded to military operations and does not prove use in every observed France-origin information campaign.","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-013"]}
CLM-005 | {"claim":"In Chad in February 2019, French air strikes requested by President Idriss Déby directly degraded a rebel force seeking to overthrow him and materially contributed to repelling the incursion; the exact counterfactual question of whether the regime would otherwise have fallen is not identified.","claimant":"INV-138 synthesis","counter":"Host-government request and French legal justification (FCT-008) alter legal/consent classification; they do not negate the direct military effect.","gap":"Regime-survival counterfactual is not identified.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-008","FCT-025"]}
CLM-006 | {"claim":"In Côte d’Ivoire in April 2011, French Licorne forces acted in support of UNOCI under a UN request and Security Council mandate; French and UN strikes against heavy weapons were then exploited by Ouattara-aligned forces to renew their offensive, creating a documented pathway from international intervention to an internal power transition.","claimant":"INV-138 synthesis","counter":"The intervention had a UN mandate and was framed as civilian/UN protection in a post-election crisis where the UN recognized Ouattara; legality and legitimacy are distinct from material political effect.","gap":"The marginal counterfactual contribution of French action to Gbagbo’s ultimate fall is not isolated.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-014","FCT-015"]}
CLM-007 | {"claim":"French officials explicitly describe visas and development aid as leverage to put pressure on countries of origin and transit over migration returns; this is a documented coercive/conditional influence mechanism, while Senate analysis shows legal, practical and ODA-classification limits to strict aid conditionality.","claimant":"INV-138 synthesis","counter":"Pressure can be lawful diplomacy/conditional cooperation and does not by itself establish clandestine interference.","gap":"Country-level implementation and behavioral effect are not established from the inspected general policy statements.","gap_type":"CAUSALITY","materiality":"HIGH","status":"PARTIAL","support":["FCT-017","FCT-018"]}
CLM-008 | {"claim":"In Libya in 2011, the formal UN mandate centered on civilian protection, while France also acknowledged supplying light weapons and ammunition to rebels; a 2026 French parliamentary report retrospectively describes the intervention as leading to Gaddafi’s overthrow. This establishes direct support to one side and a regime-change outcome, but not that regime change was the legally authorized objective or that France alone caused it.","claimant":"INV-138 synthesis","counter":"Resolution 1973 excluded occupation and stated civilian protection; multiple NATO and Libyan actors contributed to the outcome.","gap":"French intent to achieve regime change as an operational objective and the counterfactual contribution of arms/strikes are not fully established by the inspected public sources.","gap_type":"RESPONSIBILITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-021","FCT-022","FCT-023"]}
CLM-009 | {"claim":"France’s evacuation of Andry Rajoelina by military aircraft during Madagascar’s October 2025 crisis is supported by contemporaneous Reuters reporting and later French parliamentary reporting, but public evidence inspected does not establish that France caused the military takeover or specify the political purpose of the evacuation.","claimant":"INV-138 synthesis","counter":"The crisis already involved mass protest, military defections and institutional conflict; evacuation can have protective rather than regime-shaping purposes.","gap":"Purpose/tasking rationale and counterfactual political effect remain unresolved.","gap_type":"RESPONSIBILITY","materiality":"HIGH","status":"PARTIAL","support":["FCT-019","FCT-020"]}
CLM-010 | {"claim":"The 2026 National Assembly report’s aggregate statement that France recently supported or opposed certain foreign governments or electoral candidates is a material lead but is insufficient, without named case-level evidence, to prove a general contemporary French electoral-interference program.","claimant":"INV-138 synthesis","counter":["FCT-026"],"gap":"The 2023 official no-candidate-support position conflicts with the 2026 parliamentary aggregate statement that recent support/opposition to candidates occurred; the aggregate passage does not name cases, so the discrepancy cannot be resolved at case level.","gap_type":"SCOPE","materiality":"HIGH","status":"PARTIAL","support":["FCT-024"]}
CLM-011 | {"claim":"Measured influence effects are heterogeneous: direct military actions can establish I2 and sometimes partial I6 through observable force-balance changes, whereas media, training, diplomacy and the 2020 covert network generally do not establish persuasion, electoral change or I7 counterfactual outcomes; the Meta network’s small audience specifically constrains large-effect claims.","claimant":"INV-138 synthesis","counter":"Absence of measured effect is not proof of zero effect.","gap":"Most non-military mechanisms lack causal designs linking exposure to behavior or policy change.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-003","FCT-004","FCT-005","FCT-007","FCT-011","FCT-025"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-012"],"axis":"DOCTRINE","links":["CLM-001","CLM-004"],"question":"What foreign influence does France explicitly claim as state strategy?","result_ids":["FCT-001","FCT-013"],"sought_objects":["DOCTRINE","PUBLIC_DIPLOMACY"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-003","QRY-004","QRY-010","QRY-011"],"axis":"MEDIA_INFORMATION","links":["CLM-003","CLM-004","CLM-011"],"question":"How does France finance or shape foreign information ecosystems, and with what safeguards?","result_ids":["FCT-003","FCT-004","FCT-005","FCT-010","FCT-011","FCT-012"],"sought_objects":["MEDIA","TRAINING","INFORMATION"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-005","QRY-016","QRY-017"],"axis":"DEVELOPMENT_CONDITIONALITY","links":["CLM-007"],"question":"When does development assistance become leverage or conditionality rather than ordinary cooperation?","result_ids":["FCT-005","FCT-017","FCT-018"],"sought_objects":["AFD","CONDITIONALITY"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-006","QRY-007"],"axis":"INSTITUTIONAL_ENGINEERING","links":["CLM-002"],"question":"What changes to foreign administrations/parliaments are directly supported, and are they consented/co-constructed?","result_ids":["FCT-006","FCT-007"],"sought_objects":["GOVERNANCE","PARLIAMENTS"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-008","QRY-009","QRY-013","QRY-014","QRY-015","QRY-019","QRY-020","QRY-021"],"axis":"MILITARY_REGIME_SUPPORT","links":["CLM-005","CLM-006","CLM-008"],"question":"When does French security or military action directly affect survival of a foreign government?","result_ids":["FCT-008","FCT-009","FCT-014","FCT-015","FCT-016","FCT-021","FCT-022","FCT-023","FCT-025"],"sought_objects":["MILITARY","REGIME_SUPPORT"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-002","QRY-013","QRY-014","QRY-023"],"axis":"ELECTION_POLITICAL_SUPPORT","links":["CLM-006","CLM-010"],"question":"Are supports for/against governments or electoral candidates publicly documentable beyond broad retrospective claims?","result_ids":["FCT-002","FCT-014","FCT-015","FCT-024","FCT-026"],"sought_objects":["ELECTION","POLITICAL_SUPPORT"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-010","QRY-011","QRY-012","QRY-018"],"axis":"COVERT_INTELLIGENCE","links":["CLM-003","CLM-004","CLM-009"],"question":"Which clandestine/intelligence actions are sufficiently documented for attribution and tasking?","result_ids":["FCT-010","FCT-012","FCT-013","FCT-019","FCT-020"],"sought_objects":["INTELLIGENCE","COVERT"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021"],"axis":"EFFECT","links":["CLM-005","CLM-006","CLM-007","CLM-008","CLM-009","CLM-011"],"question":"What exposure, reception, behavioral/institutional change or counterfactual effect is actually demonstrated?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025"],"sought_objects":["I4","I5","I6","I7"],"status":"SATURATED"}
AXS-009 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015","QRY-016","QRY-017","QRY-018","QRY-019","QRY-020","QRY-021","QRY-023"],"axis":"SYMMETRY_CONTROL","links":["CLM-001","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-010","CLM-011"],"question":"Would the same mechanism be classified identically if emitted by an adversary or ally?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022","FCT-023","FCT-024","FCT-025","FCT-026"],"sought_objects":["SYMMETRY","INV-146"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"Partner consent/co-construction and sparse outcome measurement","gap":"Specific policy decisions caused by French assistance are not isolated.","gap_type":"CAUSALITY","limit":"Influence intent and resource flow are documented; downstream political behavior is not counterfactually identified.","mechanism":"Transparent governance/parliamentary cooperation -> capacity/resources -> possible institutional practice change","status":"UNRESOLVED","support":["FCT-006","FCT-007"]}
CAU-002 | {"counter":"FCT-011 low audience; FCT-012 institutional attribution limit","gap":"Persuasion, behavior, electoral effect and institutional tasking are not established.","gap_type":"CAUSALITY","limit":"Operation existence is established; large effect and state command are not.","mechanism":"Deceptive France-origin CIB -> audience exposure -> perception/political effect","status":"UNRESOLVED","support":["FCT-010","FCT-011"]}
CAU-003 | {"counter":"Chadian forces and other conditions also contributed; French intervention was requested by incumbent government.","gap":"No valid counterfactual establishes whether Déby would have fallen absent French strikes.","gap_type":"CAUSALITY","limit":"Direct tactical effect is documented; regime-survival counterfactual is not.","mechanism":"French air strikes -> UFR force degradation -> failure of armed challenge to Déby government","status":"UNRESOLVED","support":["FCT-008","FCT-025"]}
CAU-004 | {"counter":"UN mandate, multiple combatants, prior election legitimacy dispute and broader military dynamics.","gap":"Marginal French causal contribution to the final transfer of power is not isolated.","gap_type":"CAUSALITY","limit":"A direct enabling pathway is documented, not sole causation.","mechanism":"UNOCI/French heavy-weapons strikes -> altered military balance -> FRCI renewed offensive -> Gbagbo loss of power","status":"UNRESOLVED","support":["FCT-014","FCT-015"]}
CAU-005 | {"counter":"Senate notes strict conditionality limits and weak evaluation.","gap":"No country-level causal estimate in inspected sources establishes how much behavior changed because of aid/visa pressure.","gap_type":"CAUSALITY","limit":"Policy intent is explicit; effect is not quantified.","mechanism":"Visas/development-aid pressure -> bargaining leverage -> cooperation on migration returns","status":"UNRESOLVED","support":["FCT-017","FCT-018"]}
CAU-006 | {"counter":"Multiple coalition and Libyan actors; formal UN mandate centered on civilian protection.","gap":"Regime-change intent and France-specific counterfactual contribution remain incompletely identified.","gap_type":"CAUSALITY","limit":"Direct material support and outcome are documented; sole/decisive causation is not.","mechanism":"French/NATO intervention + support to Libyan rebels -> rebel capacity/pressure -> Gaddafi overthrow","status":"UNRESOLVED","support":["FCT-021","FCT-022","FCT-023"]}
CAU-007 | {"counter":"Mass protest, military defections and impeachment dynamics pre-existed evacuation.","gap":"Purpose and causal effect on military takeover are not established.","gap_type":"CAUSALITY","limit":"Evacuation is documented; political engineering is not.","mechanism":"French military evacuation of Rajoelina -> altered availability/safety of incumbent -> Madagascar transition","status":"UNRESOLVED","support":["FCT-019","FCT-020"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Transparency/consent control: PACOP explicitly seeks to alter parliamentary capacity and democratic governance, but is funded transparently, co-constructed with partner parliaments and stated to respect sovereignty; foreign political influence is therefore not sufficient to classify interference.","status":"SUPPORTED","support":["FCT-007"]}
CTRL-002 | {"control":"Direct-effect control: the 2019 Chad strikes were direct French military action requested by the incumbent government. Host-government consent/legal justification changes the legal and normative classification but does not erase the fact that the action could affect domestic power survival.","status":"SUPPORTED","support":["FCT-008"]}
CTRL-003 | {"control":"Funding/control separation: public financing of France Medias Monde and support to foreign media ecosystems establish resources and state policy objectives, not editorial tasking or proof that a particular audience or election outcome was changed.","status":"SUPPORTED","support":["FCT-003","FCT-004","FCT-005"]}
CTRL-004 | {"control":"Capability-use separation: public L2I doctrine proves an institutional French military influence capability outside France but cannot be used to close the attribution gap from the 2020 Meta network to French military command.","status":"SUPPORTED","support":["FCT-012","FCT-013"]}
CTRL-005 | {"control":"Reach-effect separation: Meta/Graphika establish a deceptive operation, but low audience metrics prevent promotion from operation existence to broad persuasion or electoral impact.","status":"SUPPORTED","support":["FCT-010","FCT-011"]}
CTRL-006 | {"control":"Mandate/consent-effect separation: UN mandate or host-government request can materially change legality and legitimacy while the same action still alters an internal political or military balance.","status":"SUPPORTED","support":["FCT-008","FCT-014","FCT-015","FCT-016","FCT-025"]}
CTRL-007 | {"control":"Aggregate institutional assessment is not case-level proof: the National Assembly statement about recent support/opposition to governments or candidates is retained as a lead until named cases are evidenced.","status":"SUPPORTED","support":["FCT-024"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:1|FETCH:22|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-003 | SYS | PARTIAL:9_FETCH_9_SRC_9_FCT; doctrine/media/governance/military support established; clandestine/electoral/causal branches still open | web | INV-138 initial source batch | WEB_RESEARCH
SYS-004 | SYS | WEB discovery row had auto-created SRC-021 linkage invalid under 2.10.6; source pointer cleared atomically, then exact FETCH QRY-022 linked to SRC-021 via canonical link-query-source command; no fact/source content changed. | runtime | QRY-021 | REQUEST_LOG_CORRECTION
SYS-005 | SYS | Verifier PRE requires canonical SEARCH checkpoint; SEARCH_PARTIAL label normalized to SEARCH at same phase/rank. Evidence, counts and checkpoint order unchanged. | runtime | CP-003 | CHECKPOINT_CORRECTION
SYS-006 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.diplomatie.gouv.fr/fr/le-ministere/publications-programmes-et-documentation-institutionnelle/publications/documents-institutionnels/feuille-de-route-de-l-influence | French official influence doctrine 2021
QRY-002 | FETCH | FOUND | SRC-002 | https://www.assemblee-nationale.fr/dyn/docs/RINFANR5L17B2683.raw | France foreign influence postcolonial parliamentary report 2026
QRY-003 | FETCH | FOUND | SRC-003 | https://www.francemediasmonde.com/fr/le-groupe/financement/ | France Medias Monde public funding 2026 international hubs
QRY-004 | FETCH | FOUND | SRC-004 | https://www.diplomatie.gouv.fr/fr/le-ministere-en-action/agir-pour-la-paix-et-le-respect-des-droits-de-l-homme/diplomatie-numerique/les-domaines-d-action-de-la-diplomatie-numerique/la-france-a-l-initiative-face-a-la-desinformation | MEAE support foreign media ecosystems journalists fact-checkers
QRY-005 | FETCH | FOUND | SRC-005 | https://www.afd.fr/fr/ressources/lafd-et-les-medias | AFD media support journalists democratic debate since 2018
QRY-006 | FETCH | FOUND | SRC-006 | https://www.expertisefrance.fr/fr/expertises/gouvernance | Expertise France governance public administration institutional capacity 2025
QRY-007 | FETCH | FOUND | SRC-007 | https://expertisefrance.fr/en/projects/pacop-support-project-parliamentary-cooperation | PACOP France funded parliament capacity Benin Botswana Gabon co-construction sovereignty
QRY-008 | FETCH | FOUND | SRC-008 | https://questions.assemblee-nationale.fr/q15/15-17383QE.htm | France strikes Chad 2019 Deby formal request official answer
QRY-009 | FETCH | FOUND | SRC-009 | https://www.reuters.com/world/africa/france-provided-logistical-support-benin-thwart-coup-elysee-says-2025-12-09/ | France intelligence logistical support Benin coup 2025 Reuters
QRY-010 | FETCH | SUCCESS | SRC-010 | https://about.fb.com/news/2020/12/removing-coordinated-inauthentic-behavior-france-russia/ | France coordinated inauthentic behavior Africa Meta 2020
QRY-011 | FETCH | SUCCESS | SRC-011 | https://www.graphika.com/reports/more-troll-kombat | Graphika More Troll Kombat French operation Africa 2020
QRY-012 | FETCH | SUCCESS | SRC-012 | https://www.defense.gouv.fr/ema/actualites/armees-se-dotent-dune-doctrine-militaire-lutte-informatique-dinfluence-l2i | French military doctrine L2I influence operations 2021
QRY-013 | FETCH | SUCCESS | SRC-013 | https://www.un.org/sg/en/content/sg/statement/2011-04-10/statement-secretary-general-situation-c%C3%B4te-d39ivoire-french-version | UN Côte d Ivoire Licorne 10 April 2011 heavy weapons
QRY-014 | FETCH | SUCCESS | SRC-014 | https://www.vie-publique.fr/discours/181782-declaration-de-m-gerard-longuet-ministre-de-la-defense-et-des-anciens | France Côte d Ivoire Licorne 4 April 2011 FRCI exploited strikes
QRY-015 | FETCH | SUCCESS | SRC-015 | https://questions.assemblee-nationale.fr/q17/17-11898QE.htm | France Benin intervention legal basis response May 2026
QRY-016 | FETCH | SUCCESS | SRC-016 | https://www.vie-publique.fr/discours/303517-entretien-benjamin-haddad-29052026-rmc-politique-de-limmigration | France visas development aid pressure migration May 2026
QRY-017 | FETCH | SUCCESS | SRC-017 | https://www.senat.fr/rap/r25-067/r25-0670.html | Senate development aid migration conditionality 2025 France
QRY-018 | FETCH | SUCCESS | SRC-018 | https://www.reuters.com/world/asia-pacific/madagascars-president-dissolves-national-assembly-escalating-crisis-2025-10-14/ | Madagascar Rajoelina French military plane October 2025 Reuters
QRY-019 | FETCH | SUCCESS | SRC-019 | https://press.un.org/en/2011/sc10200.doc.htm | UN Libya resolution 1973 civilian protection mandate March 2011
QRY-020 | FETCH | SUCCESS | SRC-020 | https://www.lemonde.fr/libye/article/2011/06/30/la-france-reconnait-avoir-livre-des-armes-aux-rebelles-libyens-malgre-l-embargo_1542945_1496980.html | France admits arming Libyan rebels June 2011
QRY-021 | WEB | SUCCESS | - | https://www.euronews.com/2019/02/09/scores-of-chadian-rebels-held-after-french-air-strikes | France Chad February 2019 air strikes UFR rebels observable effect 250 rebels vehicles Reuters
QRY-022 | FETCH | FOUND | SRC-021 | https://www.euronews.com/2019/02/09/scores-of-chadian-rebels-held-after-french-air-strikes | FETCH Reuters Euronews Chad 2019 French air strikes UFR rebels
QRY-023 | FETCH | FOUND | SRC-022 | https://questions.assemblee-nationale.fr/q16/16-613QG.htm | REFUTATION French support opposition foreign electoral candidates official position no candidate 2023

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:meae | MEAE-INFLUENCE-2021 | Feuille de route de l influence | 2021-12-14 | 2026-09-06T20:26:00+00:00 | lines 21-34 | https://www.diplomatie.gouv.fr/fr/le-ministere/publications-programmes-et-documentation-institutionnelle/publications/documents-institutionnels/feuille-de-route-de-l-influence
SRC-002 | ◈ | fam:other:an-report-2683 | AN-RINF-2683-2026 | Rapport sur l influence de la France dans un monde postcolonial | 2026-04-15 | 2026-09-06T20:26:00+00:00 | lines 156-223, 578-613, 853-867 | https://www.assemblee-nationale.fr/dyn/docs/RINFANR5L17B2683.raw
SRC-003 | ◈ | fam:other:fmm | FMM-FINANCEMENT-2026 | Financement France Medias Monde | 2026-09-01 | 2026-09-06T20:26:00+00:00 | lines 51-64 | https://www.francemediasmonde.com/fr/le-groupe/financement/
SRC-004 | ◈ | fam:other:meae | MEAE-DESINFO-MEDIA | La France a l initiative face a la desinformation | 2026-09-01 | 2026-09-06T20:26:00+00:00 | lines 65-88 | https://www.diplomatie.gouv.fr/fr/le-ministere-en-action/agir-pour-la-paix-et-le-respect-des-droits-de-l-homme/diplomatie-numerique/les-domaines-d-action-de-la-diplomatie-numerique/la-france-a-l-initiative-face-a-la-desinformation
SRC-005 | ◈ | fam:other:afd | AFD-MEDIA-2023 | L AFD et les medias | 2023-09-27 | 2026-09-06T20:26:00+00:00 | lines 17-29 | https://www.afd.fr/fr/ressources/lafd-et-les-medias
SRC-006 | ◈ | fam:other:expertise-france | EF-GOVERNANCE | Gouvernance publique | 2026-09-01 | 2026-09-06T20:26:00+00:00 | lines 48-57, 165-171 | https://www.expertisefrance.fr/fr/expertises/gouvernance
SRC-007 | ◈ | fam:other:expertise-france | EF-PACOP-2026 | PACOP Support Project for Parliamentary Cooperation | 2026-05-26 | 2026-09-06T20:26:00+00:00 | lines 23-90 | https://expertisefrance.fr/en/projects/pacop-support-project-parliamentary-cooperation
SRC-008 | ◈ | fam:other:minarm-parliament | AN-QE-17383-2019 | Question 17383 Tchad reponse Ministere des Armees | 2019-06-18 | 2026-09-06T20:26:00+00:00 | lines 116-135 | https://questions.assemblee-nationale.fr/q15/15-17383QE.htm
SRC-009 | ◉ | fam:other:reuters | REUTERS-BENIN-2025-12-09 | France provided logistical support to Benin to thwart coup Elysee says | 2025-12-09 | 2026-09-06T20:26:00+00:00 | lines 151-169 | https://www.reuters.com/world/africa/france-provided-logistical-support-benin-thwart-coup-elysee-says-2025-12-09/
SRC-010 | ◉ | fam:other:meta | META-CIB-FRANCE-2020-12-15 | Removing Coordinated Inauthentic Behavior from France and Russia | 2020-12-15 | 2026-09-06T20:34:02Z | What We Found item 1; France network and follower metrics | https://about.fb.com/news/2020/12/removing-coordinated-inauthentic-behavior-france-russia/
SRC-011 | ◉ | fam:other:graphika | GRAPHIKA-MORE-TROLL-KOMBAT-2020 | More-Troll Kombat | 2020-12-15 | 2026-09-06T20:34:02Z | Executive summary and French-operation attribution/reach discussion | https://www.graphika.com/reports/more-troll-kombat
SRC-012 | ◈ | fam:other:minarm | MINARM-L2I-2021-10-22 | Les armées se dotent d’une doctrine militaire de lutte informatique d’influence L2I | 2021-10-22 | 2026-09-06T20:34:02Z | Doctrine overview; external-only operations; coordination and resources | https://www.defense.gouv.fr/ema/actualites/armees-se-dotent-dune-doctrine-militaire-lutte-informatique-dinfluence-l2i
SRC-013 | ◈ | fam:other:un | UN-SG-CIV-2011-04-10 | Statement by the Secretary-General on Côte d’Ivoire | 2011-04-10 | 2026-09-06T20:34:02Z | Paragraphs on heavy weapons, UNOCI action and French Licorne support | https://www.un.org/sg/en/content/sg/statement/2011-04-10/statement-secretary-general-situation-c%C3%B4te-d39ivoire-french-version
SRC-014 | ◈ | fam:other:vie-publique | VIEPUB-LONGUET-CIV-2011-04-07 | Déclaration de Gérard Longuet sur l’intervention en Côte d’Ivoire | 2011-04-07 | 2026-09-06T20:34:02Z | Description of Licorne strikes and FRCI exploitation of their effects | https://www.vie-publique.fr/discours/181782-declaration-de-m-gerard-longuet-ministre-de-la-defense-et-des-anciens
SRC-015 | ◈ | fam:other:an-qe | AN-QE-11898-2026 | Question 11898 Intervention française au Bénin - réponse du ministère | 2026-05-12 | 2026-09-06T20:34:02Z | Response lines 113-118: request, consent, limited confidential military support | https://questions.assemblee-nationale.fr/q17/17-11898QE.htm
SRC-016 | ◈ | fam:other:vie-publique | VIEPUB-HADDAD-MIGRATION-2026-05-29 | Entretien Benjamin Haddad - politique de l’immigration | 2026-05-29 | 2026-09-06T20:34:02Z | Exchange stating use of visas and development aid to pressure origin/transit states | https://www.vie-publique.fr/discours/303517-entretien-benjamin-haddad-29052026-rmc-politique-de-limmigration
SRC-017 | ◈ | fam:other:senat | SENAT-R25-067-2025 | Prise en compte des questions migratoires dans la politique de développement | 2025-10-23 | 2026-09-06T20:34:02Z | Section B on strict aid conditionality limits and evaluation gaps | https://www.senat.fr/rap/r25-067/r25-0670.html
SRC-018 | ◉ | fam:other:reuters | REUTERS-MDG-2025-10-14 | Madagascar military takes power, fleeing president impeached | 2025-10-14 | 2026-09-06T20:34:02Z | Lines 150-183: flight aboard French military plane amid political crisis | https://www.reuters.com/world/asia-pacific/madagascars-president-dissolves-national-assembly-escalating-crisis-2025-10-14/
SRC-019 | ◈ | fam:other:un | UN-SC-1973-2011-03-17 | Security Council Resolution 1973 Libya coverage | 2011-03-17 | 2026-09-06T20:34:02Z | Resolution 1973 paragraphs authorizing all necessary measures to protect civilians | https://press.un.org/en/2011/sc10200.doc.htm
SRC-020 | ◉ | fam:other:lemonde | LEMONDE-LIBYA-ARMS-2011-06-30 | La France reconnaît avoir livré des armes aux rebelles libyens | 2011-06-30 | 2026-09-06T20:34:02Z | Military spokesperson confirmation of June arms airdrops to rebels | https://www.lemonde.fr/libye/article/2011/06/30/la-france-reconnait-avoir-livre-des-armes-aux-rebelles-libyens-malgre-l-embargo_1542945_1496980.html
SRC-021 | ◉ | fam:other:reuters-euronews | REUTERS-CHAD-2019-02-09 | Scores of Chadian rebels held after French air strikes | 2019-02-09 | 2026-09-06T20:40:00+00:00 | Reuters report via Euronews | https://www.euronews.com/2019/02/09/scores-of-chadian-rebels-held-after-french-air-strikes
SRC-022 | ◈ | fam:other:an-qe | AN-QG-613-2023 | Politique de la France en Afrique - Question au Gouvernement n°613 | 2023-03-07 | 2026-09-06T20:44:00+00:00 | ministerial answer: no candidate support; talks with all sides | https://questions.assemblee-nationale.fr/q16/16-613QG.htm

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.diplomatie.gouv.fr/fr/le-ministere/publications-programmes-et-documentation-institutionnelle/publications/documents-institutionnels/feuille-de-route-de-l-influence | other:meae | 2021-12-14 | French influence doctrine | The MEAE publicly framed influence as a strategic field, calling for France to rethink cultural/influence diplomacy, recognize new battles of influence, and assume a balance of power over values and ideas. | -
FCT-002 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/docs/RINFANR5L17B2683.raw | other:an-report-2683 | 2026-04-15 | Parliamentary assessment of French interference history | A 2026 National Assembly information report states that French military presence has been associated with interference in African domestic politics, through military interventions and, still recently, positions or support for or against governments or election candidates; this is a parliamentary assessment, not case-level proof by itself. | -
FCT-003 | FACT | ✧ | https://www.francemediasmonde.com/fr/le-groupe/financement/ | other:fmm | 2026-09-01 | France Medias Monde public financing | France Medias Monde states that 90% of its 2026 annual budget, 273.1 million euros, comes from an allocated share of VAT, with an additional 14.9 million euros of MEAE development-aid funding for international hubs and support. | -
FCT-004 | FACT | ✧ | https://www.diplomatie.gouv.fr/fr/le-ministere-en-action/agir-pour-la-paix-et-le-respect-des-droits-de-l-homme/diplomatie-numerique/les-domaines-d-action-de-la-diplomatie-numerique/la-france-a-l-initiative-face-a-la-desinformation | other:meae | 2026-09-01 | French support to foreign media ecosystems | The MEAE says it supports media ecosystems worldwide, trains journalists and fact-checkers, supports external public broadcasting and independent public-interest media, and reports 100 media financially supported in more than 30 countries through IFPIM with 14.5 million euros contributed by France since 2022. | -
FCT-005 | FACT | ✧ | https://www.afd.fr/fr/ressources/lafd-et-les-medias | other:afd | 2023-09-27 | AFD media support | AFD states that since 2018 it has supported professionalization of journalists and media technicians and production of content, explicitly linking media to public debate, citizen participation and consolidation of democratic societies. | -
FCT-006 | FACT | ✧ | https://www.expertisefrance.fr/fr/expertises/gouvernance | other:expertise-france | 2026-09-01 | French governance cooperation | Expertise France states that it supports partner administrations in state reform, civil-service modernization, digital transformation, decentralization and justice; its 2025 figures report 2,835 structures and 30,000 personnel capacity-built in democratic/economic/financial governance and support for 199 binding governance documents. | -
FCT-007 | FACT | ✧ | https://expertisefrance.fr/en/projects/pacop-support-project-parliamentary-cooperation | other:expertise-france | 2026-05-26 | PACOP parliamentary cooperation | PACOP is a 1 million euro MEAE-funded project for Benin, Botswana and Gabon that seeks to strengthen law-making, government oversight and policy evaluation; Expertise France describes it as co-constructed with partner parliaments and respectful of their sovereignty. | -
FCT-008 | FACT | ✧ | https://questions.assemblee-nationale.fr/q15/15-17383QE.htm | other:minarm-parliament | 2019-06-18 | French strikes in Chad 2019 | The French Armed Forces ministry stated that French strikes on 3, 5 and 6 February 2019 were conducted after a formal, punctual request from President Idriss Deby on 2 February; the ministry characterized the request as the legal basis and denied that the action constituted unlawful interference. | -
FCT-009 | FACT | ✧ | https://www.reuters.com/world/africa/france-provided-logistical-support-benin-thwart-coup-elysee-says-2025-12-09/ | other:reuters | 2025-12-09 | French support during Benin coup attempt | Reuters reported, citing French presidency officials, that France provided intelligence, surveillance, observation and logistical support to Benin during the December 2025 coup attempt, and shared intelligence with Nigeria, which intervened at Benin request. | -
FCT-010 | FACT | ✧ | https://about.fb.com/news/2020/12/removing-coordinated-inauthentic-behavior-france-russia/ | other:meta | 2020-12-15 | France-origin coordinated inauthentic behavior network | Meta removed 84 Facebook accounts, 6 Pages, 9 Groups and 14 Instagram accounts from a coordinated inauthentic behavior network originating in France, targeting primarily Central African Republic and Mali and posing through fake accounts as local users; Meta reported links to individuals associated with the French military. | -
FCT-011 | FACT | ✧ | https://about.fb.com/news/2020/12/removing-coordinated-inauthentic-behavior-france-russia/ | other:meta | 2020-12-15 | Reach of French-linked CIB network | Meta reported approximately 4,700 followers across the removed Pages, about 1,400 members in Groups and about 200 Instagram followers; its later monthly report described the network as having nearly no following when removed, constraining any inference of large audience effect. | -
FCT-012 | FACT | ✧ | https://www.graphika.com/reports/more-troll-kombat | other:graphika | 2020-12-15 | Institutional attribution limit for French operation | Graphika independently analyzed the network but explicitly stated that Facebook did not attribute it directly to the French Government or French military and that Graphika likewise had no evidence of institutional involvement; the operation nevertheless used deceptive personas and doctored evidence. | -
FCT-013 | FACT | ✧ | https://www.defense.gouv.fr/ema/actualites/armees-se-dotent-dune-doctrine-militaire-lutte-informatique-dinfluence-l2i | other:minarm | 2021-10-22 | French military L2I doctrine | The French armed forces publicly define L2I as military operations in the information layer of cyberspace, including detection, intelligence and deception, conducted exclusively outside national territory and potentially coordinated with other ministries or allies; this establishes institutional capability and doctrine, not attribution of a specific covert network. | -
FCT-014 | FACT | ✧ | https://www.un.org/sg/en/content/sg/statement/2011-04-10/statement-secretary-general-situation-c%C3%B4te-d39ivoire-french-version | other:un | 2011-04-10 | French Licorne support in Côte d’Ivoire | The UN Secretary-General stated that, at his request and under Security Council resolutions, French Licorne forces provided necessary support to UNOCI operations intended to prevent heavy-weapons attacks; the same statement said Laurent Gbagbo had to cede power. | -
FCT-015 | FACT | ✧ | https://www.vie-publique.fr/discours/181782-declaration-de-m-gerard-longuet-ministre-de-la-defense-et-des-anciens | other:vie-publique | 2011-04-07 | Domestic force exploitation of UN/French strikes in Côte d’Ivoire | French Defence Minister Gérard Longuet stated that the Republican Forces of Côte d’Ivoire exploited UN and French strikes against heavy weapons and relaunched their offensive, documenting a pathway by which an internationally mandated intervention altered the internal military balance. | -
FCT-016 | FACT | ✧ | https://questions.assemblee-nationale.fr/q17/17-11898QE.htm | other:an-qe | 2026-05-12 | French support during Benin coup attempt | The French government confirmed that President Patrice Talon requested French support during the December 2025 coup attempt and that France provided a small, temporary observation and logistical support detachment without direct use of force; it invoked Benin’s request and consent as legal basis. | -
FCT-017 | FACT | ✧ | https://www.vie-publique.fr/discours/303517-entretien-benjamin-haddad-29052026-rmc-politique-de-limmigration | other:vie-publique | 2026-05-29 | Use of visas and development aid as external pressure | Minister Benjamin Haddad stated that France and the EU were putting more pressure on countries of departure and transit through visas and development aid to obtain migration returns, explicitly identifying these instruments as leverage on foreign governments. | -
FCT-018 | FACT | ✧ | https://www.senat.fr/rap/r25-067/r25-0670.html | other:senat | 2025-10-23 | Limits of strict development-aid conditionality | A French Senate report concluded that strict migration conditionality of development aid has legal, practical and classification limits, including that aid explicitly conditioned for a donor migration advantage may cease to qualify as official development assistance under OECD rules; it also noted weak evaluation of prior migration-development strategy. | -
FCT-019 | FACT | ✧ | https://www.reuters.com/world/asia-pacific/madagascars-president-dissolves-national-assembly-escalating-crisis-2025-10-14/ | other:reuters | 2025-10-14 | Rajoelina evacuation amid Madagascar political crisis | Reuters reported, citing an opposition official, a military source and a foreign diplomat, that Andry Rajoelina left Madagascar aboard a French military aircraft during the October 2025 political crisis; this was contemporaneous reporting, not an official French admission of purpose or tasking. | -
FCT-020 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/docs/RINFANR5L17B2683.raw | other:an-report-2683 | 2026-04-15 | French parliamentary corroboration of Rajoelina exfiltration | The 2026 National Assembly report states that the exfiltration of former Malagasy president Andry Rajoelina by a French military aircraft during the October 2025 demonstrations caused public incomprehension about France’s role; the report does not establish a French role in causing the subsequent military takeover. | -
FCT-021 | FACT | ✧ | https://press.un.org/en/2011/sc10200.doc.htm | other:un | 2011-03-17 | UN Security Council mandate for Libya intervention | Security Council resolution 1973 authorized all necessary measures to protect civilians and civilian-populated areas under threat in Libya while excluding a foreign occupation force; the text did not itself authorize regime change as an objective. | -
FCT-022 | FACT | ✧ | https://www.lemonde.fr/libye/article/2011/06/30/la-france-reconnait-avoir-livre-des-armes-aux-rebelles-libyens-malgre-l-embargo_1542945_1496980.html | other:lemonde | 2011-06-30 | French arms airdrops to Libyan rebels | France acknowledged through military officials that it airdropped light weapons and ammunition to Libyan rebels in the Nafusa Mountains in June 2011; the legality of the action under the UN arms embargo was publicly disputed. | -
FCT-023 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/docs/RINFANR5L17B2683.raw | other:an-report-2683 | 2026-04-15 | Outcome of Libya 2011 in French parliamentary retrospective | The 2026 National Assembly report describes the 2011 French intervention alongside the United Kingdom and United States as leading to the overthrow of Muammar Gaddafi, documenting a major political outcome beyond the formal civilian-protection wording of Resolution 1973 without by itself identifying the counterfactual contribution of each actor. | -
FCT-024 | FACT | ✧ | https://www.assemblee-nationale.fr/dyn/docs/RINFANR5L17B2683.raw | other:an-report-2683 | 2026-04-15 | French support or opposition to foreign governments and electoral candidates | The 2026 National Assembly report states in aggregate that French military presence has been associated with interference in African domestic politics through military interventions and, more recently, public positions and support for or opposition to certain governments or electoral candidates; the passage does not name or prove each recent candidate-level case. | -
FCT-025 | FACT | ✧ | https://www.euronews.com/2019/02/09/scores-of-chadian-rebels-held-after-french-air-strikes | other:reuters-euronews | 2019-02-09 | Observable effect of French strikes against Chadian rebels | Reuters reported that Chad said more than 250 UFR rebels were captured and over 40 vehicles destroyed after the incursion; the French military said its aircraft had destroyed about 20 pickup trucks after President Idriss Déby requested support. The UFR objective was to topple Déby. | -
FCT-026 | FACT | ✧ | https://questions.assemblee-nationale.fr/q16/16-613QG.htm | other:an-qe | 2023-03-07 | Official French no-candidate-support position 2023 | Foreign Minister Catherine Colonna stated in the National Assembly that France sought partnerships without interference, supported no candidate and spoke with everyone including oppositions. This is a contemporaneous official policy statement, not proof that no contrary conduct ever occurred. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-005
FCT-006 | SRC-006
FCT-007 | SRC-007
FCT-008 | SRC-008
FCT-009 | SRC-009
FCT-010 | SRC-010
FCT-011 | SRC-010
FCT-012 | SRC-011
FCT-013 | SRC-012
FCT-014 | SRC-013
FCT-015 | SRC-014
FCT-016 | SRC-015
FCT-017 | SRC-016
FCT-018 | SRC-017
FCT-019 | SRC-018
FCT-020 | SRC-002
FCT-021 | SRC-019
FCT-022 | SRC-020
FCT-023 | SRC-002
FCT-024 | SRC-002
FCT-025 | SRC-021
FCT-026 | SRC-022

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

## CHECKPOINT_LOG_V1
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:Finalize scope matrix and begin source-by-source evidence collection
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:Collect official and independent evidence across doctrine, media, governance, military support and counterexamples
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:Consolidate facts and explicit causal gaps
CP-004 | FACTS | PASS | LAST_COMPLETED:10 FACTS | NEXT_ACTION:Formalize causal boundaries and rival explanations
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 CAUSAL_GAP | NEXT_ACTION:Verify provenance independence, classification symmetry and report sections
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 VERIFY | NEXT_ACTION:Complete accountability and final forensic report contract
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:Set explicit gates and freeze technical narrative

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T20:51:02.072773+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-023","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-024","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-025","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-026","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":26,"eligible":26,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:26;attempted:0;success:0;failure:0;blocked:26} | WRITEBACK_EXECUTION_V1:[26 rows, see section]

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
