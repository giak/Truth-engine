ENGINE:2.10.6 | BUNDLE_REVISION:R2A.2 | STATE:FINAL | RUN_ID:20260905-2145-open-society-foundations-france-ue | PARENT_RUN_ID:NONE | AS_OF:2026-09-05
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth_engine_inv049/root/truth-engine-v2_2.10.6-RC_R2A2P1_CANONICAL/investigations/2026-09/2026-09-05_open-society-foundations-france-ue/2026-09-05_21-45_open-society-foundations-france-ue_INPUT.txt | SUBJECT_SLUG:open-society-foundations-france-ue | SUBJECT_FP:sha256:a69d3e24a78394a86e7037b040f8d63195b65155c82d256b419c855d4621a139 | INPUT_SHA256:sha256:0520cf84e8093384f96500decf25f3480cb33ae02e37d1455c777fad66d8b2f8
COMPLEXITY:13→APEX | CHECKPOINT_SEQ:8 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:{'actors_entities': ['Open Society Foundations', 'Open Society Europe and Central Asia', 'Open Society European Policy Institute', 'George Soros', 'Alex Soros', 'selected grantees'], 'domains': ['funding', 'civil society', 'media', 'migration', 'litigation', 'policy advocacy'], 'exclusions': ['global claims not tied to France/EU', 'covert-control allegations without documented bridge'], 'geo': 'France and European Union', 'lead_question': 'N/A(NO_INPUT_LEAD)', 'limits': ['publicly accessible evidence only', 'MnemoLite unavailable'], 'object_question': 'Quels financements, bénéficiaires et mécanismes d’Open Society Foundations en France et dans l’UE sont documentés, et quels effets politiques, juridiques, médiatiques ou sociaux peuvent être établis sans confondre financement, influence et contrôle ?', 'period': '2015-2026; earlier only if structurally/causally necessary'}
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md,clusters/ICEBERG.md,clusters/MONEY.md,clusters/NETWORK.md,clusters/POWER.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
# INV-049 — Open Society Foundations / France / Union européenne

## 1. RÉSUMÉ EXÉCUTIF

L’enquête établit un **pouvoir d’influence réel mais non assimilable à un commandement centralisé**. Open Society Foundations (OSF) est un financeur transnational de grande taille : 1,2 Md$ de dépenses mondiales déclarées en 2024, dont 83,7 M$ pour l’Europe et l’Asie centrale (FCT-001, FCT-002). Son bureau bruxellois assume explicitement un objectif de politique publique : agir sur les politiques, lois et financements européens, soutenir des groupes de politique publique et des think tanks, et dialoguer avec responsables politiques et législateurs (FCT-003). Cette activité n’est donc pas « neutre » au sens d’absence d’objectif politique.

Des flux et mécanismes précis sont documentés. ECFR liste OSF parmi ses financeurs actuels, au sein d’un ensemble de bailleurs publics, philanthropiques et privés (FCT-006). Les déclarations fiscales publiques agrégées de More in Common indiquent 5,1 M$ reçus de Foundation to Promote Open Society sur neuf subventions entre 2020 et 2024 ; en 2024, cette source représente 1,1 M$ parmi 4,9 M$ de subventions provenant de treize financeurs (FCT-007, FCT-008). Destin Commun se présente comme la branche française de More in Common et reçoit un soutien de l’équipe internationale, notamment en gestion et recherche de financements (FCT-010).

Le corpus initial doit néanmoins être corrigé sur un point : **la relation OSF → More in Common et More in Common → Destin Commun est établie ; un versement direct d’OSF à l’entité juridique française Destin Commun n’a pas été établi par les sources inspectées** (LED-001, CLM-004). Écrire sans nuance « Destin Commun est financé directement par OSF » dépasserait donc l’état de preuve actuel.

Les mécanismes d’influence sont observables : financement, agenda-setting, recherche d’opinion, conseil en communication, formation, lobbying et contentieux stratégique. Destin Commun documente lui-même l’usage de segmentation psychosociale pour adapter stratégies et messages et la formation de plus de 200 salariés ou bénévoles d’organisations sociales et environnementales (FCT-011). Une réponse de la Commission européenne, accessible ici par un miroir, rapporte 32 réunions d’OSEPI avec des représentants de la Commission au cours de la période concernée (FCT-012). Dans Chowdury c. Grèce, la CEDH documente la représentation des requérants par le Greek Council for Refugees et Open Society Justice Initiative (FCT-013).

Ce que les données **ne permettent pas** d’établir : un commandement opérationnel général d’OSF sur ses bénéficiaires ; une chaîne OSF → média/ONG/institution → décision imposée ; ni un effet causal global mesurable sur l’opinion, les élections ou les politiques publiques en France/UE. Le niveau probatoire maximal est donc élevé pour les ressources, relations, capacités et actions, mais beaucoup plus faible pour persuasion, comportement et résultats contrefactuels (CAU-001..004).

## 2. MANIPULATION_REPORT

Scores finaux, utilisés comme routage analytique et non comme preuve : `Ξ=3 | €=8 | Λ=3 | Ω=1 | Ψ=0 | ↕=5 | Φ=0 | Σ=1 | Κ=2 | ρ=4 | κ=4 | ⫸=4 | ⚔=1 | 🌐=6 | ⏰=3`.

Le signal dominant est **€ / flux financiers** : les financements sont substantiels, identifiables et structurants. `🌐` et `↕` sont matériels parce que les flux s’insèrent dans des réseaux d’organisations disposant d’accès, de capacités de production intellectuelle, de plaidoyer et de communication. `Ξ` demeure modéré : il manque encore un registre France exhaustif des subventions et surtout des données de causalité aval. `⚔` reste faible : aucune chaîne clandestine ou de guerre cognitive centralisée n’est établie. Clusters chargés : `ICEBERG`, `MONEY`, `NETWORK`, `POWER`.

## 3. CLUSTERS

**MONEY** : la question utile n’est pas « Soros finance-t-il ? » mais « combien, à qui, sous quelle forme, avec quelles conditions et quelle dépendance ? ». Les données More in Common montrent à la fois un financement OSF matériel et une pluralité de bailleurs (FCT-007, FCT-008).

**NETWORK** : les relations OSF/OSEPI, ECFR, More in Common et Destin Commun sont documentées, mais leurs natures diffèrent : financement, affiliation de réseau, soutien opérationnel ou accès institutionnel. Une arête n’implique pas une chaîne de commandement.

**POWER** : un acteur privé doté de ressources peut peser sur l’agenda public sans mandat électif. Cette asymétrie est analytiquement pertinente, mais elle ne dispense pas de démontrer l’effet sur une décision donnée.

**ICEBERG** : les objets manquants décisifs sont les conventions de subvention, droits de contrôle éventuels, comptes détaillés de l’entité française et études capables d’isoler un effet causal.

## 4. HERMÉNEUTIQUE

**L1 faits** : budgets, financeurs, relations institutionnelles et activités déclarées sont vérifiables (FCT-001..013).

**L2 relations** : OSF finance certaines organisations ; More in Common est un réseau international dont Destin Commun est la branche française ; OSEPI pratique le plaidoyer européen.

**L3 mécanismes** : financement de capacité, production de recherche, conseil stratégique, formation, accès institutionnel et contentieux sont des voies plausibles et, pour leur existence, documentées.

**L4 causalité** : financer ou rencontrer ne prouve pas qu’une politique, une opinion ou un vote aurait été différent sans OSF.

**L5 contrôle** : le conseil d’administration contrôle la stratégie et les budgets d’OSF (FCT-005). Aucune preuve équivalente n’établit un contrôle général d’OSF sur la gouvernance ou les décisions quotidiennes des bénéficiaires.

**L6 résultat** : certains résultats institutionnels peuvent être établis cas par cas, notamment une procédure juridictionnelle ; l’effet politique agrégé reste non établi.

## 5. FORENSIC REASONING

Ce qui est montré : argent, objectifs déclarés, bénéficiaires, structures, outils d’action et accès. Ce qui serait nécessaire pour passer de « influence » à « contrôle » : clauses d’instruction, droit d’approbation, preuves de tasking, correspondances décisionnelles ou gouvernance dépendante. Ce qui serait nécessaire pour passer de « activité » à « effet » : exposition, réception, changement observé, contrefactuel et exclusion crédible des explications rivales.

L’enquête refuse donc deux raccourcis symétriques : `financement -> contrôle` et `absence de contrôle démontré -> neutralité`.

## 6. PRISME DIALECTIQUE

**Version favorable** : OSF finance des organisations autonomes alignées sur des valeurs de société ouverte ; le financement philanthropique est un soutien à la société civile, non une commande politique.

**Version critique forte** : une fortune privée peut sélectionner des causes, financer des capacités professionnelles, produire des cadres cognitifs, ouvrir des accès institutionnels et donc exercer un pouvoir politique sans mandat électif. La littérature de théorie politique considère d’ailleurs que la philanthropie d’élite peut poser un problème démocratique même lorsque ses intentions sont d’intérêt public.

**Arbitrage probatoire** : la seconde version est solide pour l’existence d’un pouvoir de sélection, de capacité et d’agenda ; elle devient trop forte si elle infère automatiquement contrôle coordonné ou résultat causal. La première est solide sur l’autonomie juridique possible des bénéficiaires ; elle devient trop faible si elle présente comme apolitique un dispositif dont OSF revendique lui-même les objectifs de politique publique.

## 7. CHRONOLOGIE

- **2015–2019** : OSF augmente son soutien aux organisations travaillant sur migration et réfugiés ; en 2019 il présente More in Common comme une organisation soutenue travaillant notamment sur les représentations des migrants (FCT-005 comme source de contexte OSF migration).
- **2017** : arrêt Chowdury c. Grèce ; OSJI participe à la représentation des requérants avec le Greek Council for Refugees (FCT-013).
- **2020–2024** : les données fiscales agrégées attribuent 5,1 M$ de Foundation to Promote Open Society à More in Common Inc sur neuf subventions (FCT-007).
- **2023** : une réponse de la Commission indique 32 réunions d’OSEPI avec des représentants de la Commission sur la période parlementaire visée (FCT-012).
- **2024** : OSF déclare 1,2 Md$ de dépenses mondiales et 83,7 M$ en Europe/Asie centrale (FCT-001, FCT-002). More in Common reçoit 1,1 M$ de Foundation to Promote Open Society parmi treize financeurs déclarés (FCT-008).
- **2026, AS_OF 5 septembre** : ECFR continue de lister OSF parmi de nombreux financeurs et Destin Commun se définit comme branche française de More in Common (FCT-006, FCT-010).

## 8. DOMAINES

**Financement** : établi et matériel. La difficulté n’est pas l’existence des flux mais leur interprétation.

**Think tanks** : ECFR constitue un exemple de bénéficiaire/partenaire financier, mais son financement est pluriel (FCT-006).

**Société civile / opinion** : More in Common et Destin Commun travaillent explicitement sur segmentation, récits, communication et polarisation ; le mécanisme d’action est visible, son effet marginal ne l’est pas (FCT-011, CAU-003).

**Migration** : OSF assume un soutien aux droits des migrants et à des organisations travaillant sur les perceptions et politiques migratoires ; cela établit une orientation, pas l’efficacité de cette orientation.

**Plaidoyer UE** : objectifs et accès sont documentés ; causalité sur les décisions non établie (FCT-003, FCT-012, CAU-002).

**Justice/contentieux** : la participation d’OSJI à un contentieux CEDH est un exemple concret d’action institutionnelle ; extrapoler ce cas à une capture de la justice serait invalide (FCT-013, CAU-004).

## 9. RÉSEAU D’ACTEURS

`OSF Board -> stratégies/budgets OSF` : gouvernance interne établie (CTRL-001).

`OSF/OSEPI -> institutions UE` : plaidoyer et accès (FCT-003, FCT-012).

`OSF -> ECFR` : financement au sein d’un portefeuille diversifié de bailleurs (FCT-006).

`Foundation to Promote Open Society -> More in Common` : financement substantiel (FCT-007, FCT-008).

`More in Common -> Destin Commun` : branche nationale et soutien transversal (FCT-009, FCT-010).

Aucune de ces arêtes, seule ou combinée, ne démontre `OSF -> commandement opérationnel de l’ensemble du réseau` (CTRL-002).

## 10. CHAÎNES / PELOTE

**Chaîne 1 — financement de capacité** : `ressources OSF -> subventions -> capacité/projets des bénéficiaires`. Statut : **SUPPORTED** (CAU-001). Droit causal limité à l’activation de ressources ; pas de droit automatique sur les résultats aval.

**Chaîne 2 — plaidoyer** : `OSF/OSEPI -> réunions/arguments -> décideurs UE -> éventuelle politique`. Accès : documenté. Dernier maillon : **UNRESOLVED** (CAU-002).

**Chaîne 3 — recherche et communication** : `financement/réseau -> recherche d’opinion -> segmentation/conseil/formation -> publics`. Les trois premiers éléments sont documentés ; persuasion et comportement : **UNRESOLVED** (CAU-003).

**Chaîne 4 — contentieux** : `soutien juridique -> représentation -> procédure -> décision judiciaire`. Cas Chowdury : chaîne institutionnelle observable (CAU-004), mais elle ne prouve ni capture judiciaire ni effet politique systémique.

## 11. CARTE DES PREUVES

Les quatre leads corpus sont tous terminalisés : deux réévalués matériellement et deux exclus comme contexte sans delta probatoire spécifique (LED-001..004). Les huit axes sont `SATURATED` ou `GAP` typé (AXS-001..008). Les huit claims centraux séparent explicitement les relations établies, la revendication directe sur Destin Commun qui reste partielle, le contrôle général réfuté dans sa forme forte, et l’effet causal global qui reste inconnu (CLM-001..008).

Treize faits web sont enregistrés au niveau **✧**. Ce choix est volontaire : chaque fait repose sur une famille de provenance principale actuelle ; aucune confirmation **✦** n’a été fabriquée par duplication de sources ou par simple prestige institutionnel.

Le diagnostic de diversité est `EDI≈0,815`, au-dessus de la cible APEX 0,80, avec `COV=1,0`. Ce score mesure la diversité du corpus, **pas la vérité**. La principale faiblesse reste l’absence de données OSF-spécifiques permettant un contrefactuel d’impact.

## 12. CARTE DIALECTIQUE

### Scénario A — philanthropie autonome
OSF finance selon des objectifs de société ouverte ; les bénéficiaires conservent leur autonomie. Compatible avec la pluralité des bailleurs d’ECFR et More in Common et avec l’existence de subventions de fonctionnement général.

### Scénario B — influence par agenda et capacité
OSF sélectionne des priorités, augmente les capacités d’acteurs alignés, produit ou finance expertise, communication, contentieux et plaidoyer. **Très compatible** avec les faits établis.

### Scénario C — réseau centralement commandé
OSF contrôlerait les décisions et productions des bénéficiaires en aval. **Non établi** dans le périmètre inspecté.

### Scénario D — aucun effet réel
Les financements et actions n’auraient aucun effet politique. **Non établi non plus** : certains résultats cas par cas existent, mais une mesure agrégée manque.

La position la plus robuste est donc B, avec des éléments A selon les organisations, et sans droit probatoire vers C ni vers D.

## 13. PÉRIMÈTRE & LIMITES

Périmètre principal : France et Union européenne, 2015–2026. Les éléments antérieurs ne sont utilisés que pour éclairer une structure ou une causalité. Sources publiques accessibles uniquement. MnemoLite n’est pas disponible : aucune mémoire externe n’est inventée.

Limites majeures : absence de registre public consolidé des subventions OSF strictement françaises ; comptes/accords de certains bénéficiaires non récupérés ; une page de la Charity Commission a renvoyé HTTP 403 ; l’accès aux réunions OSEPI repose ici en partie sur un miroir de réponse de la Commission et un agrégateur du registre de transparence ; aucune étude identifiée n’isole un effet France/UE global d’OSF.

## 14. ÉTAT DES CONNAISSANCES

**Connu / fortement supporté** : taille financière d’OSF ; dépenses Europe ; objectifs de plaidoyer européen ; financement d’ECFR et More in Common ; appartenance de Destin Commun au réseau More in Common ; outils de segmentation/formation ; existence d’accès institutionnel OSEPI ; rôle d’OSJI dans le cas Chowdury.

**Partiel** : financement direct de l’entité juridique Destin Commun par OSF ; portée exacte de certains programmes français.

**Inference bornée** : OSF possède un pouvoir d’agenda et de capacité politique/philanthropique supérieur à celui d’un simple donateur passif.

**Inconnu** : effet marginal global sur opinion, vote, médias ou décisions publiques ; degré de dépendance organisationnelle de chaque bénéficiaire.

**Réfuté dans sa forme forte** : `financement = contrôle` ; `réseau = commandement unique` ; `absence de chaîne secrète publique = preuve d’absence de toute influence`.

## 15. SUSPICION / VÉRIFICATION

### Audit du corpus
Le point « Destin Commun financé par OSF » est **rétréci** : financement OSF de More in Common + relation organique More in Common/Destin Commun établis ; financement direct de l’entité française non établi. Les représentations de type « nœud central Open Society » doivent être remplacées par des arêtes typées et des droits d’inférence séparés.

### Tests de réouverture
1. document comptable ou registre de subventions identifiant explicitement Destin Commun comme bénéficiaire OSF ;
2. contrat ou correspondance donnant à OSF un droit de tasking/validation substantiel sur un bénéficiaire ;
3. étude avec exposition, outcome et contrefactuel permettant d’isoler un effet causal ;
4. contradiction matérielle avec les flux ou structures actuels.

En l’absence de ces objets, continuer à chercher une « preuve de contrôle total » serait du fishing. Le résiduel doit rester un GAP, pas être comblé narrativement.
<!-- NARRATIVE_END -->

SEMANTIC_COUNTS_V1:LED:4|CLM:8|AXS:8|CAU:4|CTRL:3|ACT:1

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempts":["QRY-017","QRY-022","QRY-052","QRY-053","QRY-057","QRY-058"],"claim":"Destin Commun is financed in part by Open Society Foundations","outcome":"PARTIAL: OSF funding of More in Common is established and Destin Commun is the French branch; a direct OSF grant to the French legal entity was not established in the sources inspected.","ref":"A045:194518266.lingenierie-de-lenclos","sources":["SRC-007","SRC-009","SRC-011","SRC-012"],"status":"SATURATED"}
LED-002 | {"attempts":["QRY-016","QRY-018","QRY-023","QRY-024","QRY-039"],"claim":"Open Society appears as a finance/network node around French influence actors","outcome":"BOUNDED: OSF funding and policy-advocacy infrastructure are real; no global command chain to the named French actors is established by this run.","ref":"A072:186844276.tristan-mendes-france-la-machine","sources":["SRC-002","SRC-006","SRC-013","SRC-014"],"status":"SATURATED"}
LED-003 | {"claim":"Potential Open Society / information-governance lead","outcome":"No material OSF-specific evidence from this lead changed INV-049 after independent recheck; retained as corpus context only.","ref":"A097:180580808.pravda-quand-lelysee-ironise-sur","status":"EXCLUDED"}
LED-004 | {"claim":"Potential Open Society / media-influence lead","outcome":"No material OSF-specific evidence from this lead changed INV-049 after independent recheck; retained as corpus context only.","ref":"A098:180481861.quand-lelysee-attaque-un-journaliste","status":"EXCLUDED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"OSF is a large transnational philanthropic funder with substantial Europe/Central Asia spending.","status":"SUPPORTED","support":["FCT-001","FCT-002"]}
CLM-002 | {"claim":"OSF's Brussels activity is explicitly intended to shape EU policy conditions and includes engagement with political leaders and legislators.","status":"SUPPORTED","support":["FCT-003","FCT-012"]}
CLM-003 | {"claim":"OSF funds ECFR and More in Common.","status":"SUPPORTED","support":["FCT-006","FCT-007","FCT-008"]}
CLM-004 | {"claim":"Destin Commun itself is directly funded by OSF as a French legal entity.","limit":"Network-level funding and French branch relationship are established; direct French-entity grant is not.","status":"PARTIAL","support":["FCT-007","FCT-009","FCT-010"]}
CLM-005 | {"claim":"Destin Commun operationalizes audience segmentation and communication research for civil-society actors in France.","status":"SUPPORTED","support":["FCT-011"]}
CLM-006 | {"claim":"OSF funding proves command or capture of grantees and downstream institutions.","reason":"Available evidence shows grant support and sometimes project objectives, but also general support, diversified grantee funding and no documented general tasking chain.","status":"REFUTED","support":["FCT-004","FCT-006","FCT-008"]}
CLM-007 | {"claim":"OSF can achieve identifiable case-level institutional/legal outcomes through supported litigation.","limit":"Case-level mechanism only; not a system-wide causal estimate.","status":"SUPPORTED","support":["FCT-013"]}
CLM-008 | {"claim":"OSF funding has a demonstrated France/EU-wide causal effect on elections, public opinion, media outputs or policy outcomes.","gap":"No identified design or evidence isolates OSF's marginal effect at this scale.","gap_type":"COUNTERFACTUAL_EFFECT","status":"GAP"}

### AXIS_REGISTRY_V1
AXS-001 | {"attempts":["QRY-006","QRY-007","QRY-035","QRY-036","QRY-037"],"name":"Scale and financial flows","result":"Global and regional OSF scale established; selected grantee flows established, but no complete France-only grant ledger was recoverable from public pages in this run.","status":"SATURATED"}
AXS-002 | {"attempts":["QRY-013"],"name":"Governance and control inside OSF","result":"Board-level strategy/budget oversight established; this does not extend operational control to grantees.","status":"SATURATED"}
AXS-003 | {"attempts":["QRY-018","QRY-023","QRY-024","QRY-032","QRY-039","QRY-042","QRY-043"],"name":"EU advocacy and institutional access","result":"Explicit Brussels advocacy objectives and repeated Commission access are established; policy causation is not.","status":"SATURATED"}
AXS-004 | {"attempts":["QRY-014","QRY-015","QRY-019","QRY-020"],"name":"Think-tank funding / ECFR","result":"Current ECFR donor relationship with OSF established; ECFR also has a broad multi-funder base.","status":"SATURATED"}
AXS-005 | {"attempts":["QRY-016","QRY-017","QRY-021","QRY-022","QRY-025","QRY-026","QRY-027","QRY-028","QRY-029","QRY-030","QRY-048","QRY-049","QRY-051","QRY-052","QRY-055","QRY-056","QRY-057","QRY-058"],"name":"More in Common / Destin Commun","result":"OSF-to-More-in-Common funding and France-relevant work established; Destin Commun is the French branch and applies message/audience research. Direct grant to the French legal entity remains unestablished.","status":"SATURATED"}
AXS-006 | {"attempts":["QRY-004","QRY-005","QRY-010","QRY-034","QRY-059"],"name":"Migration and litigation","result":"OSF support for migrant-rights work and OSJI participation in a successful ECtHR litigation chain are established at case level.","status":"SATURATED"}
AXS-007 | {"gap":"Funding and activities are observable, but this run found no defensible France/EU-wide estimate of persuasion, public-opinion change, media-output change, or policy change attributable to OSF funding.","gap_type":"CAUSAL_EFFECT","name":"Media / civil-society effects","status":"GAP"}
AXS-008 | {"gap":"No source inspected establishes a general OSF command chain over grantees, media, courts, or EU decision-makers; funding and access alone are insufficient.","gap_type":"CONTROL_ATTRIBUTION","name":"Control / capture hypothesis","status":"GAP"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"causal_right":"ENABLER","limit":"Does not imply command or downstream outcome.","mechanism":"OSF resources -> grants -> grantee capacity / projects","status":"SUPPORTED","support":["FCT-004","FCT-006","FCT-007","FCT-008"]}
CAU-002 | {"gap":"Access and topics are documented; adoption or marginal policy change caused by OSF is not isolated.","gap_type":"POLICY_CAUSATION","mechanism":"OSF/OSEPI advocacy -> institutional access -> policy outcome","status":"UNRESOLVED","support":["FCT-003","FCT-012"]}
CAU-003 | {"gap":"Implementation is documented but downstream persuasion or behavior attributable to OSF funding is not measured here.","gap_type":"PERSUASION_EFFECT","mechanism":"More in Common research -> Destin Commun communication/training -> audience/persuasion change","status":"UNRESOLVED","support":["FCT-007","FCT-010","FCT-011"]}
CAU-004 | {"causal_right":"ACTION_TO_CASE_OUTCOME","limit":"The judgment establishes representation and adjudication in one case, not broader political control.","mechanism":"OSJI legal support -> litigation -> ECtHR adjudication","status":"SUPPORTED","support":["FCT-013"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"OSF board over OSF strategies/budgets","status":"PASS","support":["FCT-005"]}
CTRL-002 | {"control":"OSF operational command over grantees","gap":"Not established by inspected grant/funding evidence.","gap_type":"COMMAND_CHAIN","status":"GAP"}
CTRL-003 | {"control":"ECFR donor plurality as anti-single-funder control","status":"PASS","support":["FCT-006"]}

### ACTION_REGISTRY_V1
ACT-001 | {"actor":"Alexander Soros","responsibility_limit":"Role establishes governance position, not personal authorship of specific downstream grants/actions absent evidence.","role":"Chair, Open Society Foundations board","status":"PASS","support":["FCT-005"]}

SEARCH_ACTIVITY_V1:WEB:40|FETCH:23|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | PASS | runtime | SYS-001 | REPAIR_SYS
SYS-004 | SYS | BLOCKED:GIT_METADATA_ABSENT | verify.py | pre | PRE_GATE_VERIFY
SYS-005 | SYS | PASS | git | local-working-copy | VERIFY_ENV_GIT_BOOTSTRAP
SYS-006 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | investigation-summary | MNEMO_S
SYS-007 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
SYS-008 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | snapshot:v1 | SNAPSHOT_MEMORY_WRITE
QRY-001 | WEB | FOUND | - | - | site:opensocietyfoundations.org/grants/past France Open Society Foundations grant 2024 France
QRY-002 | WEB | FOUND | - | - | site:opensocietyfoundations.org/grants/past "European Council on Foreign Relations" Open Society grant
QRY-003 | WEB | FOUND | - | - | site:opensocietyfoundations.org/grants/past "More in Common" Open Society
QRY-004 | WEB | FOUND | - | - | site:opensocietyfoundations.org/grants/past PICUM Open Society Europe grant
QRY-005 | WEB | FOUND | - | - | site:opensocietyfoundations.org/grants/past ECRE Open Society grant Europe
QRY-006 | FETCH | FOUND | SRC-001 | https://www.opensocietyfoundations.org/who-we-are/financials | FETCH OSF financials
QRY-007 | FETCH | FOUND | SRC-002 | https://www.opensocietyfoundations.org/what-we-do/regions/europe-and-central-asia | FETCH OSF Europe and Central Asia
QRY-008 | FETCH | FAIL:unsafe-url | - | https://www.opensocietyfoundations.org/grants/how-we-fund | FETCH OSF how we fund
QRY-009 | FETCH | FAIL:unsafe-url | - | https://www.opensocietyfoundations.org/who-we-are/board | FETCH OSF board
QRY-010 | FETCH | FOUND | SRC-005 | https://www.opensocietyfoundations.org/voices/addressing-migration-challenges-in-a-globalized-world | FETCH OSF migration 2019
QRY-011 | FETCH | FOUND | - | https://www.opensocietyfoundations.org/who-we-are/our-history | FETCH OSF history
QRY-012 | FETCH | FOUND | SRC-003 | https://www.opensocietyfoundations.org/how-we-work/how-we-fund | FETCH OSF how we fund canonical
QRY-013 | FETCH | FOUND | SRC-004 | https://www.opensocietyfoundations.org/who-we-are/board-of-directors | FETCH OSF board of directors canonical
QRY-014 | WEB | FOUND | - | - | "European Council on Foreign Relations" funding Open Society 2024 annual report
QRY-015 | WEB | FOUND | - | - | "European Council on Foreign Relations" "Open Society" Charity Commission accounts
QRY-016 | WEB | FOUND | - | - | "More in Common" "Open Society" funding Europe
QRY-017 | WEB | FOUND | - | - | "Destin Commun" "Open Society" financement
QRY-018 | WEB | NO_RESULT | - | - | "Open Society European Policy Institute" "Transparency Register" Brussels
QRY-019 | FETCH | FOUND | SRC-006 | https://ecfr.eu/donors/funding/ | FETCH ECFR current funding
QRY-020 | FETCH | FAIL:HTTP403 | - | https://register-of-charities.charitycommission.gov.uk/en/charity-search?_uk_gov_ccew_onereg_charitydetails_web_portlet_CharityDetailsPortlet_objectiveId=A15659078&_uk_gov_ccew_onereg_charitydetails_web_portlet_CharityDetailsPortlet_priv_r_p_mvcRenderCommandName=%2Faccounts-and-annual-returns&_uk_gov_ccew_onereg_charitydetails_web_portlet_CharityDetailsPortlet_priv_r_p_organisationNumber=4049916&p_p_cacheability=cacheLevelPage&p_p_id=uk_gov_ccew_onereg_charitydetails_web_portlet_CharityDetailsPortlet&p_p_lifecycle=2&p_p_mode=view&p_p_resource_id=%2Faccounts-resource&p_p_state=maximized | FETCH Charity Commission ECFR 2022 accounts
QRY-021 | WEB | FOUND | - | - | "Open Society Initiative for Europe" "More in Common" 2021 2022 2023
QRY-022 | WEB | FOUND | - | - | "Destin Commun" "Open Society Foundations" "More in Common"
QRY-023 | WEB | FOUND | - | - | "Open Society European Policy Institute" lobbyfacts
QRY-024 | WEB | FOUND | - | - | "Open Society European Policy Institute" transparency register number
QRY-025 | WEB | FOUND | - | - | "We receive funding in all six countries in which we have offices" "Open Society Foundations"
QRY-026 | WEB | FOUND | - | - | "These funders include" "Open Society Foundations" "More in Common"
QRY-027 | WEB | FOUND | - | - | "Open Society Foundations" "More in Common" "William and Flora Hewlett Foundation"
QRY-028 | WEB | FOUND | - | - | "Foundation to Promote Open Society" "More In Common" 3000000 2023
QRY-029 | WEB | FOUND | - | - | "More In Common Inc" "Foundation to Promote Open Society" 2023
QRY-030 | WEB | FOUND | - | - | "More in Common" 3000000 "democratic societies" Germany France Poland EU
QRY-031 | WEB | FOUND | - | - | "E-000422/2022" Open Society European Policy Institute Commission answer
QRY-032 | WEB | FOUND | - | - | "Open Society European Policy Institute" "32 meetings" Commission answer
QRY-033 | WEB | FOUND | - | - | "Open Society European Policy Institute" transparency register 8557515321-37
QRY-034 | WEB | FOUND | - | - | "Chowdury and Others v. Greece" Open Society Justice Initiative Greek Council refugees
QRY-035 | FETCH | FOUND | - | https://philanthropy.org/990/grants-by/263753801/foundation-to-promote-open-society | FETCH Foundation to Promote Open Society grants aggregation
QRY-036 | FETCH | FOUND | SRC-007 | https://philanthropy.org/990/who-funds/823043917/more-in-common-inc | FETCH More in Common funders IRS-derived aggregation
QRY-037 | FETCH | FOUND | SRC-008 | https://philanthropy.org/990/report/823043917/more-in-common-inc | FETCH More in Common 990 report IRS-derived aggregation
QRY-038 | WEB | FOUND | - | - | "Open Society" "almost EUR 5 million" lobbying 2020 European Parliament answer
QRY-039 | WEB | FOUND | - | - | "Open Society European Policy Institute" "32 meetings" "European Commission"
QRY-040 | WEB | FOUND | - | - | "Open Society European Policy Institute" "14 meetings" 2020 "4 meetings" 2021
QRY-041 | WEB | FOUND | - | - | "8557515321-37" "European Parliament" Open Society
QRY-042 | FETCH | FOUND | SRC-013 | https://politique.pappers.fr/question/contacts-with-open-society-policy-institute-QECR943784 | FETCH mirrored Commission answer on OSEPI contacts
QRY-043 | FETCH | FOUND | SRC-014 | https://www.openlobby.eu/org/open-society-european-policy-institute | FETCH OpenLobby OSEPI profile
QRY-044 | WEB | FOUND | - | - | "Contacts with Open Society Policy Institute" site:europarl.europa.eu 1.12.2022
QRY-045 | WEB | NO_RESULT | - | - | "Open Society Policy Institute" "30 January 2023" site:europarl.europa.eu
QRY-046 | WEB | NO_RESULT | - | - | "Open Society Foundations" "14 meetings" "2020" site:europarl.europa.eu
QRY-047 | WEB | NO_RESULT | - | - | "almost EUR 5 million" "Open Society" site:europarl.europa.eu
QRY-048 | WEB | FOUND | - | - | "public opinion research and analytics" "More in Common" "Foundation to Promote Open Society"
QRY-049 | WEB | FOUND | - | - | "More in Common" "France, Poland" "Foundation to Promote Open Society"
QRY-050 | FETCH | FOUND | SRC-016 | https://www.influencewatch.org/non-profit/more-in-common/ | FETCH More in Common grant-selection secondary profile
QRY-051 | WEB | FOUND | - | - | "More in Common" funding Open Society Foundations site:moreincommon.com
QRY-052 | WEB | FOUND | - | - | "Destin Commun" "More in Common" partenaires financeurs
QRY-053 | WEB | NO_RESULT | - | - | site:destincommun.fr partenaires financeurs "Open Society"
QRY-054 | WEB | FOUND | - | - | site:destincommun.fr "More in Common" "200" formations
QRY-055 | FETCH | FOUND | SRC-009 | https://www.moreincommon.com/about-us/funding/ | FETCH More in Common funding page
QRY-056 | FETCH | FOUND | SRC-010 | https://www.destincommun.fr/que-faisons-nous/notre-approche/ | FETCH Destin Commun approach
QRY-057 | FETCH | FOUND | SRC-011 | https://www.destincommun.fr/qui-sommes-nous/notre-equipe/ | FETCH Destin Commun team
QRY-058 | FETCH | FOUND | SRC-012 | https://www.moreincommon.com/where-we-work/destin-commun-france/ | FETCH More in Common France page
QRY-059 | FETCH | FOUND | SRC-015 | https://hudoc.echr.coe.int/app/conversion/docx/pdf?filename=CASE+OF+CHOWDURY+AND+OTHERS+v.+GREECE.pdf&id=001-172701&library=ECHR&logEvent=False | FETCH ECtHR Chowdury judgment
QRY-060 | WEB | FOUND | - | - | "philanthropy" democracy political influence foundations academic review private foundations policy agenda
QRY-061 | WEB | FOUND | - | - | "elite philanthropy" democracy foundations political influence academic
QRY-062 | FETCH | FOUND | SRC-017 | https://www.journals.uchicago.edu/doi/abs/10.1086/694103 | FETCH Journal of Politics Plutocratic Philanthropy abstract
QRY-063 | FETCH | FAIL:HTTP405 | - | https://www.degruyterbrill.com/document/doi/10.1515/npf-2019-0049/html | FETCH Agenda-setting and Public Policy in Private Foundations

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:osf-self | https://www.opensocietyfoundations.org/who-we-are/financials
SRC-002 | ◈ | fam:other:osf-self | https://www.opensocietyfoundations.org/what-we-do/regions/europe-and-central-asia
SRC-003 | ◈ | fam:other:osf-self | https://www.opensocietyfoundations.org/how-we-work/how-we-fund
SRC-004 | ◈ | fam:other:osf-self | https://www.opensocietyfoundations.org/who-we-are/board-of-directors
SRC-005 | ◈ | fam:other:osf-self | https://www.opensocietyfoundations.org/voices/addressing-migration-challenges-in-a-globalized-world
SRC-006 | ◈ | fam:other:ecfr-self | https://ecfr.eu/donors/funding/
SRC-007 | ◉ | fam:other:irs-aggregation | https://philanthropy.org/990/who-funds/823043917/more-in-common-inc
SRC-008 | ◉ | fam:other:irs-aggregation | https://philanthropy.org/990/report/823043917/more-in-common-inc
SRC-009 | ◈ | fam:other:mic-self | https://www.moreincommon.com/about-us/funding/
SRC-010 | ◈ | fam:other:destin-self | https://www.destincommun.fr/que-faisons-nous/notre-approche/
SRC-011 | ◈ | fam:other:destin-self | https://www.destincommun.fr/qui-sommes-nous/notre-equipe/
SRC-012 | ◈ | fam:other:mic-self | https://www.moreincommon.com/where-we-work/destin-commun-france/
SRC-013 | ◉ | fam:other:eu-answer-mirror | https://politique.pappers.fr/question/contacts-with-open-society-policy-institute-QECR943784
SRC-014 | ◉ | fam:other:openlobby | https://www.openlobby.eu/org/open-society-european-policy-institute
SRC-015 | ◈ | fam:A | https://hudoc.echr.coe.int/app/conversion/docx/pdf?filename=CASE+OF+CHOWDURY+AND+OTHERS+v.+GREECE.pdf&id=001-172701&library=ECHR&logEvent=False
SRC-016 | ○ | fam:other:influencewatch | https://www.influencewatch.org/non-profit/more-in-common/
SRC-017 | ◉ | fam:other:academic-jop | https://www.journals.uchicago.edu/doi/abs/10.1086/694103

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.opensocietyfoundations.org/who-we-are/financials | other:osf-self | 2024 | OSF global expenditure 2024 | Open Society Foundations reports 1.2 billion US dollars in expenditures in 2024 and more than 24.2 billion dollars in expenditures to date. | -
FCT-002 | FACT | ✧ | https://www.opensocietyfoundations.org/what-we-do/regions/europe-and-central-asia | other:osf-self | 2024 | OSF Europe and Central Asia expenditure 2024 | OSF reports 83.7 million US dollars in 2024 expenditure for Europe and Central Asia, representing 7 percent of global expenditures. | -
FCT-003 | FACT | ✧ | https://www.opensocietyfoundations.org/what-we-do/regions/europe-and-central-asia | other:osf-self | 2026-09-05 | OSF Brussels policy objective | OSF states that its Brussels work seeks to ensure EU policies, laws, and funding uphold open-society values and that it engages European political leaders and legislators while supporting policy groups and think tanks. | -
FCT-004 | FACT | ✧ | https://www.opensocietyfoundations.org/how-we-work/how-we-fund | other:osf-self | 2026-09-05 | OSF grantmaking model | OSF states that most grants are made to organizations it approaches directly; grants can be project-specific or general operating support; in most cases OSF funding is capped at one third of an organization budget. | -
FCT-005 | FACT | ✧ | https://www.opensocietyfoundations.org/who-we-are/board-of-directors | other:osf-self | 2026-09-05 | OSF board governance | OSF states that its board oversees all programs and entities, reviews strategies, and recommends budgets; Alexander Soros is chair and the board includes Soros-family and non-family members. | -
FCT-006 | FACT | ✧ | https://ecfr.eu/donors/funding/ | other:ecfr-self | 2026-09-05 | ECFR current donor plurality | ECFR lists Open Society Foundations among a broad current donor base that also includes European governments and public bodies, foundations, companies, and individual donors. | -
FCT-007 | FACT | ✧ | https://philanthropy.org/990/who-funds/823043917/more-in-common-inc | other:irs-aggregation | 2019-2024 | More in Common funding from Foundation to Promote Open Society | IRS-derived filings aggregated by philanthropy.org report that More in Common Inc received 5.1 million US dollars across nine grants from Foundation to Promote Open Society between 2020 and 2024, while receiving 23.4 million dollars across 104 grants from 50 funders in 2019-2024. | -
FCT-008 | FACT | ✧ | https://philanthropy.org/990/report/823043917/more-in-common-inc | other:irs-aggregation | 2024 | More in Common FY2024 funding plurality | The FY2024 public filing aggregation reports 1.1 million US dollars from Foundation to Promote Open Society and 4.9 million dollars in grants received from 13 funders. | -
FCT-009 | FACT | ✧ | https://www.moreincommon.com/about-us/funding/ | other:mic-self | 2026-09-05 | More in Common funding and legal presence | More in Common states that it receives funding from private foundations in all countries where it operates and global funders, and that it is registered as a nonprofit association in France among several national legal entities. | -
FCT-010 | FACT | ✧ | https://www.destincommun.fr/qui-sommes-nous/notre-equipe/ | other:destin-self | 2026-09-05 | Destin Commun relation to More in Common | Destin Commun states that it is the French branch of the international More in Common network and receives support from the international team in areas including administration, management, and fundraising. | -
FCT-011 | FACT | ✧ | https://www.destincommun.fr/que-faisons-nous/notre-approche/ | other:destin-self | 2026-09-05 | Destin Commun operational methods | Destin Commun describes applying social-psychology segmentation to strategy and communications, training more than 200 staff and volunteers from environmental and social organizations, and running workshops including on French attitudes toward immigration. | -
FCT-012 | FACT | ✧ | https://politique.pappers.fr/question/contacts-with-open-society-policy-institute-QECR943784 | other:eu-answer-mirror | 2023-01-30 | OSEPI contacts with European Commission | A mirrored European Commission answer states that Open Society European Policy Institute held 32 meetings with Commission representatives during the referenced parliamentary term on subjects including democracy and rule of law, media and disinformation, climate, Covid-19, and Roma inclusion. | -
FCT-013 | FACT | ✧ | https://hudoc.echr.coe.int/app/conversion/docx/pdf?filename=CASE+OF+CHOWDURY+AND+OTHERS+v.+GREECE.pdf&id=001-172701&library=ECHR&logEvent=False | A | 2017-03-30 | OSJI participation in Chowdury v Greece | The ECtHR judgment records that the applicants were represented by lawyers from the Greek Council for Refugees and by the director and a lawyer of the Open Society Justice Initiative. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-002
FCT-004 | SRC-003
FCT-005 | SRC-004
FCT-006 | SRC-006
FCT-007 | SRC-007
FCT-008 | SRC-008
FCT-009 | SRC-009
FCT-010 | SRC-011
FCT-011 | SRC-010
FCT-012 | SRC-013
FCT-013 | SRC-015

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 | NEXT_ACTION:7
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 | NEXT_ACTION:9
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 | NEXT_ACTION:10
CP-004 | FACTS | PASS | LAST_COMPLETED:10 | NEXT_ACTION:11
CP-005 | CAUSAL | PASS | LAST_COMPLETED:11 | NEXT_ACTION:13
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 | NEXT_ACTION:17
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 | NEXT_ACTION:18
CP-008 | CORRECTION | PASS | LAST_COMPLETED:18b | NEXT_ACTION:18b

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-05T21:59:31.264531+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":13,"eligible":13,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:13;attempted:0;success:0;failure:0;blocked:13} | WRITEBACK_EXECUTION_V1:[13 rows, see section]

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
