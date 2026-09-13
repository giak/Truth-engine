ENGINE:2.10.6 | BUNDLE_REVISION:R3 | STATE:FINAL | RUN_ID:20260906-1805-attribution-ingerence | PARENT_RUN_ID:NONE | AS_OF:2026-09-06
INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:PATH:/mnt/data/truth-engine/investigations/2026-09/2026-09-06_attribution-ingerence/2026-09-06_18-05_attribution-ingerence_INPUT.txt | SUBJECT_SLUG:attribution-ingerence | SUBJECT_FP:sha256:89cbe2336beabbdc1c01160b7dcf58aae19ec35855f92e499bcc7a8b3d061c02 | INPUT_SHA256:sha256:785a52114285ad80ccf9bb44f8d39eea80e993e4a13bdd89b9669f85c42e0507
COMPLEXITY:9→HIGH | CHECKPOINT_SEQ:7 | LAST_COMPLETED:18b | NEXT_ACTION:NONE
scope:France/UE 2017–2026 with documented comparators; attribution chain incident→artifact/infrastructure→operator→intermediary→state/commanditaire→intent/tasking→exposure/effect; all official claims and denials remain claims until evidenced.
RESUME_COUNT:0 | ROUTE_OVERRIDES:[NONE] | modules:definitions/SYMBOLS.md,definitions/PATTERNS.md,definitions/THREATS.md,forensic/GATES.md,forensic/REQUEST_LOG.md | degraded:MNEMO_UNAVAILABLE
GATE_STATUS_V1 | G0:PASS|G1:PASS|G2:PASS|G3:PASS|G4:PASS|G5:PASS|G6:PASS|G7:PASS|G8:PASS|G9:PASS|G10:PASS

<!-- NARRATIVE_START -->
---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "truth_engine_investigation"
artifact_id: "INV-134"
run_id: "20260906-1805-attribution-ingerence"
status: "final_candidate"
updated: "2026-09-06"
---

<!-- TRACE: source=INV-134_RUN_CARD; runtime=Truth_Engine_2.10.6_R3P1 -->
<!-- DECISION: attribution=edge_graph; official_claim!=proof; official_denial!=proof; attribution!=effect -->

# INV-134 — Attribution d’ingérence : où s’arrête réellement la preuve ?

## Verdict exécutif

Une attribution d’ingérence n’est pas un verdict binaire. Le corpus impose une chaîne plus stricte :

`incident → artefact/infrastructure → opérateur → intermédiaire → commanditaire/État → tasking/intention → exposition → effet`

Chaque flèche est un claim autonome. Les cinq familles de cas inspectées montrent que la preuve peut être forte à un étage et faible au suivant.

Le cas **Plovdiv / von der Leyen** est le contrôle négatif le plus utile. Un problème d’approche GPS signalé par l’équipage est documenté. En revanche, le dossier public inspecté ne ferme pas le saut vers « GPS brouillé », encore moins vers « brouillage russe ciblant la présidente de la Commission ». L’assertion initiale de brouillage reposait sur une information/suspicion bulgare relayée par la Commission (`FCT-001`). Quatre jours plus tard, la Commission reconnaissait n’avoir jamais affirmé un ciblage délibéré (`FCT-002`), tandis que les données ADS-B exploitées par Flightradar24 ne présentaient pas les signatures NIC/NACp observées sur le même appareil lors d’un épisode réel d’interférence la veille (`FCT-005`). L’histoire de l’heure de circuit et des cartes papier est également contredite (`FCT-006`). Le démenti russe reste, lui aussi, une simple affirmation (`FCT-007`).

À l’autre extrémité, **Doppelgänger/RRN** fournit une attribution publique beaucoup plus dense. Le DOJ ne se contente pas d’une similarité technique : il indique que l’affidavit sous-jacent décrit des notes de réunions stratégiques, propositions de projets et autres documents internes, et allègue une direction/contrôle par l’administration présidentielle russe (`FCT-015..016`). Le Trésor américain a, séparément, sanctionné SDA et Structura en les décrivant comme agissant à la direction de cette administration (`FCT-017`). VIGINUM reprend ensuite cette attribution tout en maintenant une réserve essentielle sur l’efficacité réelle (`FCT-018`). Ce n’est pas un jugement pénal définitif, mais la base publique est matériellement plus forte que dans Plovdiv, Rokh Solis ou Portal Kombat.

Entre les deux, **Rokh Solis**, **Portal Kombat** et **Storm-1516** montrent trois façons différentes de s’arrêter proprement avant le commanditaire.

## 1. La grille : l’attribution est un graphe probatoire

Le mot « attribution » masque au moins huit objets :

1. **incident** : quelque chose s’est-il réellement produit ?
2. **artefact/infrastructure** : quels domaines, comptes, signaux, serveurs, fichiers ou outils sont observés ?
3. **opérateur** : qui contrôle matériellement ces actifs ?
4. **intermédiaire** : prestataire, proxy, agence, société écran ou sous-traitant ?
5. **commanditaire/État** : qui paie, ordonne ou contrôle ?
6. **tasking/intention** : quel objectif a été donné pour l’opération considérée ?
7. **exposition** : quelle audience authentique a réellement été atteinte ?
8. **effet** : quelle perception, décision, participation ou issue électorale a changé à cause de l’opération ?

VIGINUM fournit lui-même un garde-fou important : l’origine géographique des actifs ou intermédiaires peut différer de celle du commanditaire (`FCT-008`). Un domaine israélien, russe ou américain ne vaut donc pas identité du donneur d’ordre.

## 2. Plovdiv 2025 : une attribution qui se dégrade sous contrôle

### 2.1 Ce qui est établi

Le 31 août 2025, l’équipage de l’avion transportant Ursula von der Leyen a signalé un problème avec une arrivée fondée sur GPS et a demandé une approche ILS. L’avion a atterri sans incident (`FCT-004`). Ce fait minimal ne doit pas être effacé par la réfutation d’assertions plus fortes.

### 2.2 Ce qui fut affirmé

Le 1er septembre, Reuters rapporte la déclaration de la Commission : « GPS jamming » confirmé, avec information reçue des autorités bulgares qui « suspectent » une interférence russe (`FCT-001`). L’article précise que l’UE ne fournit pas davantage de détails et ne dit pas que l’avion a été délibérément ciblé.

Le 4 septembre, la Commission maintient la référence au communiqué bulgare initial sur une disparition du signal GPS, mais précise qu’elle **n’a jamais parlé de ciblage** et qu’elle ne dispose pas d’information en ce sens (`FCT-002`). Le niveau `Russie → ciblage délibéré` est donc explicitement plus faible que le titre médiatique initial pouvait le laisser penser.

### 2.3 Le contrôle technique

Flightradar24 exploite les données ADS-B brutes. Sur Varsovie–Plovdiv, l’appareil transmet NIC=8 et NACp=10 tout au long du vol, sans signature indiquant un brouillage GPS. Le contrôle est particulièrement fort parce que **le même appareil**, la veille, a traversé une zone d’interférence réelle : NIC et NACp y tombent à zéro pendant environ onze minutes (`FCT-005`). La méthode détecte donc un épisode positif sans retrouver la même signature à Plovdiv.

Flightradar24 ne prétend pas connaître la panne exacte : il conclut qu’un problème a empêché l’approche GPS, mais que les données n’indiquent pas un brouillage dirigé contre l’appareil. Cette nuance est conservée.

Les données de vol contredisent également le récit initial d’une heure de circuit et de cartes papier : l’allongement n’est que de quelques minutes (`FCT-006`).

### 2.4 Le démenti n’est pas la preuve inverse

Le ministère russe des Affaires étrangères qualifie l’accusation de fausse et paranoïaque (`FCT-007`). Ce démenti ne ferme rien. Il ne fournit ni télémétrie, ni cause alternative, ni preuve d’absence d’action russe.

**Verdict Plovdiv :**
- problème d’approche GPS : `SUPPORTED` ;
- brouillage GPS de cet appareil : `NOT_ESTABLISHED in public scoped evidence` ;
- brouillage russe : `NOT_ESTABLISHED` ;
- ciblage délibéré de von der Leyen : `NOT_ESTABLISHED` ;
- « une heure / cartes papier » : `CONTRADICTED` ;
- démenti russe : `CLAIM_ONLY`.

La bonne correction n’est donc pas « rien ne s’est passé ». C’est : **le fait minimal subsiste, mais les étages hostiles de l’attribution publique ne sont pas fermés par le dossier accessible**.

## 3. Rokh Solis 2026 : opération forte, commanditaire inconnu

Rokh Solis est beaucoup plus solide au niveau de l’opération. VIGINUM documente des sites techniquement liés, des relais coordonnés et inauthentiques, une campagne de discrédit visant des candidats français, ainsi que des marqueurs techniques d’extranéité reliés à Israël (`FCT-009`).

Le rapport détaillé est toutefois plus prudent que le résumé. VIGINUM écrit que le MOI **pourrait** présenter des caractéristiques communes avec l’activité de Blackcore et précise qu’aucun élément ne permet alors d’établir l’identité et l’origine des commanditaires ayant pu recourir à cette société (`FCT-010`).

La chaîne correcte est donc :

`opération Rokh Solis VERIFIED → extranéité/israeli markers VERIFIED → Blackcore PARTIAL → commanditaire UNKNOWN`

Elle ne devient pas `État israélien` par transitivité.

Enfin, la visibilité est faible malgré les tentatives d’amplification. Le RCPE évalue plus largement les opérations municipales détectées comme ayant une visibilité limitée et un impact faible sur le débat public numérique (`FCT-011`). Le propre rapport distingue estimation du **risque d’impact** et mesure des effets réels. Il n’existe donc aucune base ici pour convertir l’existence de l’opération en changement de vote.

## 4. Portal Kombat : trouver l’infrastructure n’est pas trouver le patron

VIGINUM attribue à TigerWeb, société russe domiciliée en Crimée, un rôle majeur dans la création et l’administration des sites de Portal Kombat (`FCT-012`). C’est une arête robuste de type infrastructure/opérateur technique.

Mais la phrase suivante est précisément la frontière recherchée : les similarités avec Inforos permettent de **formuler l’hypothèse** que TigerWeb serait un prestataire pour un opérateur dont l’identité n’est pas connue (`FCT-013`).

**Position :** infrastructure forte ; relation de prestation hypothétique ; commanditaire non établi.

## 5. RRN / Doppelgänger : quand la chaîne remonte réellement jusqu’à l’État

Le cas RRN montre que l’attribution peut évoluer avec les preuves disponibles. En 2023, VIGINUM documente 355 domaines usurpant des médias, des dizaines d’articles et l’implication d’individus russes/russophones et de sociétés russes (`FCT-014`). Cela suffit pour l’opération et plusieurs opérateurs, pas encore pour une chaîne publique jusqu’au Kremlin.

En 2024, le DOJ décrit une base différente. Selon l’affidavit FBI rendue publique, SDA, Structura et ANO Dialog opéraient sous la direction/contrôle de l’administration présidentielle russe et de Sergei Kiriyenko (`FCT-015`). Le communiqué précise que l’affidavit s’appuie notamment sur des **notes internes de réunions stratégiques, propositions de projets et autres documents obtenus au cours de l’enquête** (`FCT-016`).

Le Trésor américain avait déjà désigné SDA et Structura en mars 2024 en affirmant qu’ils menaient une campagne d’influence sous la direction de l’administration présidentielle et avaient agi pour ou au nom du gouvernement russe (`FCT-017`). Cette seconde action reste une action de l’exécutif américain, pas une famille totalement indépendante du renseignement/enquête américaine ; la circularité est conservée dans `EDI_REPORT`.

VIGINUM reprend en 2025 l’attribution publique DOJ au niveau Kiriyenko/SDA/Structura/ANO Dialog (`FCT-018`). Mais son propre bilan apporte un contrepoids essentiel : l’efficacité est jugée faible et des documents internes SDA suggèrent que le prestataire peut bénéficier commercialement de la publicité faite à son attribution et exagérer sa capacité d’influence.

**Verdict Doppelgänger :** la chaîne publique `opération → opérateurs → documents internes/tasking → administration présidentielle` est substantiellement plus forte que les chaînes fondées sur marqueurs techniques ou proximité. Son statut doit néanmoins rester correctement nommé : **attribution étayée par affidavit/enquête et sanctions administratives, pas condamnation finale ayant jugé chaque assertion au fond**.

## 6. Storm-1516 : ne pas fusionner l’imputation du MOI et celle de son commanditaire

VIGINUM analyse 77 opérations Storm-1516 et décrit un écosystème d’influence russe coordonné, tout en reconnaissant que l’impact réel reste difficile à estimer (`FCT-019`).

En février 2026, pour une opération visant Emmanuel Macron, VIGINUM attribue avec une **confiance élevée** l’opération à Storm-1516, avec soutien technique de CopyCop, sur la base du narratif, du type de contenu et de la chaîne de diffusion (`FCT-020`). C’est une attribution forte `opération → MOI`.

Le rapport municipal de juin 2026 décrit ensuite Storm-1516 comme « attribué en source ouverte » à l’unité 29155 du GRU (`FCT-021`). Cette formulation n’est pas équivalente à la précédente : elle change d’arête et de fondement probatoire.

Un avis multi-agences NSA/FBI/CISA et alliés attribue indépendamment des activités **cyber** malveillantes à des acteurs affiliés à l’unité 29155 (`FCT-022`). Cela renforce l’existence et l’activité de l’unité, mais ne ferme pas mécaniquement `29155 → tasking de Storm-1516`. Une preuve sur le cyber ne se transplante pas dans une opération informationnelle par simple identité d’acteur supposée.

**Position Storm :** `opération → Storm` fort ; `Storm → GRU 29155` public mais plus indirect dans le corpus inspecté ; `effet électoral` non établi.

## 7. Matrice de fermeture des arêtes

| Cas | Incident/opération | Infrastructure/opérateur | Commanditaire/État | Tasking/intention | Reach | Effet |
|---|---|---|---|---|---|---|
| Plovdiv | GPS-approach issue SUPPORTED | jamming NOT_ESTABLISHED | Russia NOT_ESTABLISHED | targeting NOT_ESTABLISHED | N/A | N/A |
| Rokh Solis | VERIFIED | Israeli markers VERIFIED; Blackcore PARTIAL | UNKNOWN | malicious electoral targeting attributed by VIGINUM | LOW | vote effect NOT_ESTABLISHED |
| Portal Kombat | VERIFIED | TigerWeb VERIFIED | UNKNOWN | provider hypothesis only | PARTIAL | NOT_ESTABLISHED |
| Doppelgänger | VERIFIED | SDA/Structura/ANO Dialog strong | Russian Presidential Administration STRONG PUBLIC BASIS | internal records/tasking described | MEASURED/PARTIAL | causal electoral effect NOT_ESTABLISHED |
| Storm-1516 | VERIFIED | MOI HIGH-CONFIDENCE on cases | GRU29155 PARTIAL in scoped public chain | PARTIAL | sometimes high | causal effect difficult/not established |

La matrice interdit une pratique fréquente : utiliser le niveau le plus fort d’une colonne pour remplir automatiquement les suivantes.

## 8. Ce que cette enquête change

### 8.1 Une attribution peut être fausse ou surjouée sans que toutes les alertes soient fausses

Plovdiv montre qu’une affirmation officielle peut se dégrader fortement après contrôle. Doppelgänger montre l’inverse : certaines attributions disposent de traces publiques beaucoup plus substantielles. La conclusion correcte n’est donc ni « croire les services » ni « ne jamais croire les services ».

### 8.2 Les démentis n’ont aucun privilège probatoire

Le démenti russe sur Plovdiv n’est pas plus auto-validant que la première assertion de la Commission. De même, une absence de commanditaire identifié dans Rokh Solis ne prouve pas que Blackcore ou un État n’a eu aucun client : elle fixe simplement la limite du dossier public.

### 8.3 La confiance doit être attachée à une arête, pas à un dossier

Dire « attribution à confiance élevée » sans préciser **de quoi à quoi** est ambigu. Storm-1516 le montre : VIGINUM peut avoir une confiance élevée dans `opération → MOI` alors que `MOI → unité étatique → tasking précis` reste une autre question.

### 8.4 L’effet est encore une enquête distincte

Rokh Solis : visibilité limitée. RRN : efficacité faible selon VIGINUM. Storm : impact difficile à estimer. La preuve de l’auteur n’est pas la preuve de l’effet.

## 9. Gaps terminaux

- Plovdiv : logs avioniques/airline et résultat complet d’une éventuelle enquête technique bulgare non présents dans le dossier public inspecté.
- Rokh Solis : identité/origine des commanditaires explicitement inconnue dans le rapport VIGINUM.
- Portal Kombat : opérateur ultime inconnu dans la source publique inspectée.
- Storm-1516 : bridge public direct `GRU 29155 → tasking des opérations informationnelles spécifiques` non fermé ici.
- Tous les cas : persuasion et résultat électoral contrefactuel généralement non identifiés (`CAU-001`).
- Effet propre d’une attribution publique erronée/corrigée sur opinions ou politiques non identifié (`CAU-002`).

## 10. Conclusion

La règle opérationnelle issue d’INV-134 est simple :

**ne plus enregistrer « attribution = X » comme un seul claim.**

Il faut enregistrer au minimum :

`OBSERVED_EVENT → TECHNICAL_ARTIFACT → OPERATOR → INTERMEDIARY → PRINCIPAL/STATE → TASKING/INTENT → EXPOSURE → EFFECT`

avec un statut séparé pour chaque arête : `SUPPORTED | PARTIAL | ALLEGED | CONTRADICTED | UNKNOWN`.

Cette règle traite de la même manière l’accusation officielle, le démenti officiel, le rapport technique, la fuite et la décision judiciaire. Elle permet de dire simultanément deux choses qui sont toutes deux vraies dans ce corpus : **certaines opérations étrangères sont fortement documentées jusqu’au commandement étatique ; certaines accusations publiques vont plus loin que les preuves accessibles.**
<!-- NARRATIVE_END -->

FORENSIC_CONTRACT_V1:SYMBOLS:15|MODULE_EXECUTION:0|EDI_DECISIVE:7|SRC_COMPLETE:15/15

## FORENSIC_SECTIONS_V1

### TEMPORAL_STATE
- **Plovdiv:** initial 2025-09-01 claim -> 2025-09-04 technical/official contradiction
- **RRN:** 2023 operation-level evidence -> 2024 stronger US state-direction attribution -> 2025 French synthesis
- **Rokh:** 2026 investigation still leaves commanditaire unresolved
- **as_of:** 2026-09-06

### MANIPULATION_REPORT
- **assumptions:**
  - attribution can strengthen or weaken over time
  - authority is not evidence
  - technical overlap is not command
- **clusters:**
  - NONE
- **complexity:**
  - **band:** HIGH
  - **score:** 9
- **implicit:**
  - incident != jamming != hostile action
  - operator != commanditaire
  - geographic origin != state tasking
  - sanction != final merits adjudication
  - operation != persuasion != electoral effect
- **input_kind:** TOPIC
- **mission_mode:** INVESTIGATION
- **patterns:**
  - attribution layering
  - technical-marker overreach
  - state-command inference
  - official claim laundering
  - official denial laundering
  - effect inflation
- **priorities:**
  - separate every attribution edge
  - test official claim and denial symmetrically
  - seek technical positive/negative controls
  - separate intent/exposure/effect
- **query_guidance:** reopen public source for every decisive edge; prefer technical/internal records; keep allegation, administrative designation, technical attribution and final adjudication distinct
- **rhetorical:**
  - NONE
- **speaker:** user/object question
- **symbol_stage:** FINAL
- **symbols:**
  - **M:** 4
  - **Κ:** 5
  - **Λ:** 5
  - **Ξ:** 5
  - **Σ:** 4
  - **Φ:** 5
  - **Ψ:** 4
  - **Ω:** 4
  - **κ:** 4
  - **ρ:** 5
  - **€:** 2
  - **↕:** 5
  - **⏰:** 5
  - **⚔:** 2
  - **⫸:** 5
- **threats:**
  - attribution laundering
  - denial laundering
  - source circularity
  - state-command overreach
  - effect overclaim

### MODULE_EXECUTION
NONE

### SCOPING_REPORT
- **cases:**
  - Plovdiv GPS
  - Rokh Solis
  - Portal Kombat
  - RRN/Doppelganger
  - Storm-1516
- **exclusions:**
  - generic geopolitical blame
  - classified evidence not publicly inspectable
  - effect inferred from operation existence
- **object:** Attribution chain audit
- **scope:** France/UE 2017–2026 plus documented comparator Doppelganger

### CREDO
- accusation != fact
- official statement != proof
- official denial != proof
- infrastructure != operator != commanditaire
- actor nationality != state tasking
- attribution != intent
- operation exists != effect
- absence of public proof != proof of absence

### COGNITIVE_MAP
- **causal_boundary:** Attribution and effect are separate propositions.
- **core_model:** Attribution is an evidence graph, not a label. Strength can rise or fall independently at each edge.
- **observed_structure:**
  - incident
  - artifact/infrastructure
  - operator
  - intermediary
  - state/commanditaire
  - tasking/intent
  - exposure/effect
- **rival_models:**
  - technical failure/no hostile operation
  - commercial provider without state client
  - state-aligned actor without tasking
  - correct attribution but negligible effect

### DIALECTICAL_MAP
- **item 1:**
  - **antithesis:** official attribution can also outrun public technical evidence
  - **resolution:** grade each edge; Plovdiv and Doppelganger legitimately receive different verdicts
  - **thesis:** official services can identify real foreign operations
- **item 2:**
  - **antithesis:** intermediary geography may differ from commanditaire
  - **resolution:** markers support actor/extranéity, not automatic state/client identity
  - **thesis:** foreign technical markers identify origin
- **item 3:**
  - **antithesis:** visibility/effect can be low
  - **resolution:** intent, reach and causal outcome remain separate
  - **thesis:** state-linked operation implies political impact

### RESOURCE_FLOW_MAP
- **item 1:**
  - **classification:** CLAIM_RELAY
  - **flow:** initial attribution information
  - **from:** Bulgarian authorities
  - **support:**
    - FCT-001
  - **to:** European Commission/media
- **item 2:**
  - **classification:** TECHNICAL_CONTROL
  - **flow:** NIC/NACp values and flight path
  - **from:** technical telemetry
  - **support:**
    - FCT-004
    - FCT-005
    - FCT-006
  - **to:** Flightradar24 analysis
- **item 3:**
  - **classification:** EVIDENCE_TO_ATTRIBUTION
  - **flow:** internal strategy notes/project proposals summarized in affidavit/press release
  - **from:** DOJ/FBI investigative records
  - **support:**
    - FCT-015
    - FCT-016
  - **to:** public attribution

### ACTOR_NETWORK_MAP
- **item 1:**
  - **actor:** European Commission/Bulgarian authorities
  - **documented_edges:**
    - crew GPS issue
    - initial Bulgarian/Commission interference assertion
  - **role:** initial Plovdiv attribution chain
  - **uncertain_edges:**
    - actual jamming mechanism
    - Russian operator/state
    - deliberate targeting
- **item 2:**
  - **actor:** VIGINUM / Rokh Solis / Blackcore
  - **documented_edges:**
    - coordinated inauthentic assets
    - Israeli technical markers
  - **role:** technical attribution chain
  - **uncertain_edges:**
    - Blackcore as exact operator
    - client/commanditaire
    - electoral effect
- **item 3:**
  - **actor:** TigerWeb / Portal Kombat
  - **documented_edges:**
    - creation/administration of network sites
  - **role:** infrastructure administrator
  - **uncertain_edges:**
    - ultimate operator
    - state command
- **item 4:**
  - **actor:** SDA / Structura / ANO Dialog / Russian Presidential Administration
  - **documented_edges:**
    - DOJ affidavit-based direction/control allegation
    - internal strategy records described
    - Treasury designation
  - **role:** Doppelganger command chain
  - **uncertain_edges:**
    - final judicial adjudication
    - causal electoral effect
- **item 5:**
  - **actor:** Storm-1516 / CopyCop / GRU 29155
  - **documented_edges:**
    - specific operations -> Storm/CopyCop high-confidence VIGINUM attribution
    - GRU29155 cyber activity independently attributed
  - **role:** MOI/state attribution layers
  - **uncertain_edges:**
    - direct public tasking bridge GRU29155 -> specific Storm information operations

### IMPACT_MAP
- **downstream:** INV-144 can consume the distinction between risk/impact and observed effect; INV-146 can use the attribution-edge model for ally/adversary symmetry; INV-137 can investigate attribution laundering through intelligence/executive/media chains.
- **measured_objects:**
  - technical interference indicators
  - operation/infrastructure attribution
  - operator/client uncertainty
  - public state-direction evidence
  - visibility/impact bounds
- **not_established:**
  - general causal persuasion
  - counterfactual electoral outcomes
  - all classified evidence behind official attributions
  - generic reliability ranking of institutions

### CONTRADICTION_LEDGER
- **item 1:**
  - **contra:** Bulgarian later position + Flightradar raw ADS-B control
  - **issue:** Plovdiv GPS jamming
  - **pro:** initial Commission/Bulgarian statement
  - **status:** STRONGER_JAMMING_CLAIM_NOT_ESTABLISHED_PUBLICLY
- **item 2:**
  - **contra:** Commission later says it never claimed targeting; no public operator/state chain
  - **issue:** Plovdiv Russian targeting
  - **pro:** initial suspicion attributed to Bulgarian authorities
  - **status:** NOT_ESTABLISHED
- **item 3:**
  - **contra:** denial supplies no independent technical evidence
  - **issue:** Russia denial
  - **pro:** Russian MFA rejection
  - **status:** CLAIM_ONLY
- **item 4:**
  - **contra:** VIGINUM explicitly cannot identify commanditaires
  - **issue:** Rokh Solis Blackcore/client
  - **pro:** technical commonalities/Israeli markers
  - **status:** PARTIAL
- **item 5:**
  - **contra:** scoped public record lacks direct tasking bridge for specific info operations
  - **issue:** Storm GRU29155
  - **pro:** VIGINUM cites open-source attribution; unit independently known
  - **status:** PARTIAL
- **item 6:**
  - **contra:** DOJ allegation/affidavit and executive sanction are not final merits adjudication
  - **issue:** Doppelganger state direction
  - **pro:** internal records described by DOJ + Treasury designation + VIGINUM later synthesis
  - **status:** STRONG_PUBLIC_BASIS

### VERIFICATION_REPORT
- **checks:**
  - official claims distinguished from evidence
  - denials distinguished from evidence
  - positive technical control used for Plovdiv
  - commanditaire gaps explicit
  - effect not inherited from attribution
  - legal status of DOJ/Treasury claims explicit
- **status:** PASS_PENDING_EXTERNAL_GATE

### EDI_REPORT
- **corpus:**
  - **circularity:** DOJ/Treasury and later VIGINUM Doppelganger attribution partly share the same US investigative basis; VIGINUM publications are one institutional family across cases. Reuters carries Commission/Russian statements rather than independent technical proof.
  - **counters:** 4
  - **coverage:** 0.92
  - **direct_objects:** 8
  - **edi_star:** 0.84
  - **independence:** 0.82
- **decisive_claim_coverage:**
  - **item 1:**
    - **claim_id:** CLM-001
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 5
  - **item 2:**
    - **claim_id:** CLM-002
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** ACCESS
    - **independent_families:** 4
  - **item 3:**
    - **claim_id:** CLM-003
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 4
  - **item 4:**
    - **claim_id:** CLM-004
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 1
  - **item 5:**
    - **claim_id:** CLM-006
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** NONE
    - **independent_families:** 3
  - **item 6:**
    - **claim_id:** CLM-008
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** ATTRIBUTION
    - **independent_families:** 2
  - **item 7:**
    - **claim_id:** CLM-009
    - **direct_object:** YES
    - **freshness:** CURRENT
    - **gap_type:** CAUSALITY
    - **independent_families:** 3
- **diagnostic_not_truth:** true
- **dimensions:**
  - **geo:** 0.9
  - **lang:** 0.9
  - **owner:** 0.9
  - **persp:** official claims + technical counter + opposing denial + cross-case controls
  - **strat:** 0.92
  - **temp:** 1.0
- **edi:**
  - **final:** 0.84
  - **flags:**
    - PLOVDIV_RAW_AVIONICS_NOT_PUBLIC
    - ROKH_CLIENT_UNKNOWN
    - STORM_STATE_BRIDGE_PARTIAL
    - GENERAL_EFFECT_CAUSALITY_UNRESOLVED
  - **penalties:** 0.06
  - **raw:** 0.9
- **source_counts:**
  - **primary:** 10
  - **secondary:** 5
  - **total:** 15

### RESPONSIBILITY_MAP
- **item 1:**
  - **burden:** technical evidence of jamming + source/operator + state link
  - **claim:** Plovdiv Russian jamming
  - **owner:** Commission/Bulgarian initial statement chain
  - **status:** NOT_CLOSED
- **item 2:**
  - **burden:** technical operator link then contract/tasking/client
  - **claim:** Rokh Blackcore/client
  - **owner:** VIGINUM
  - **status:** PARTIAL
- **item 3:**
  - **burden:** internal records + legal/administrative attribution; status explicit
  - **claim:** Doppelganger Russian Presidential Administration direction
  - **owner:** DOJ/Treasury
  - **status:** STRONG_PUBLIC_BASIS_NOT_FINAL_ADJUDICATION
- **item 4:**
  - **burden:** direct tasking/operational bridge
  - **claim:** Storm -> GRU29155
  - **owner:** open-source attribution cited by VIGINUM
  - **status:** PARTIAL

### NEXT_QUERIES
- **item 1:**
  - **query:** Plovdiv aircraft avionics logs / completed technical investigation
  - **route:** RECHECK
  - **trigger:** new Bulgarian/airline avionics report
- **item 2:**
  - **query:** Rokh Solis Blackcore contract payment commanditaire
  - **route:** RECHECK
  - **trigger:** new Blackcore client/tasking document
- **item 3:**
  - **query:** Storm-1516 GRU29155 command/tasking evidence
  - **route:** RECHECK
  - **trigger:** direct public Storm tasking document
- **item 4:**
  - **query:** trace intelligence briefing -> executive statement -> media certainty -> correction
  - **route:** MERGE
  - **trigger:** INV-137
- **item 5:**
  - **query:** apply same edge-wise attribution threshold to ally/adversary pairs
  - **route:** MERGE
  - **trigger:** INV-146

## TRACE_MATRIX_V1
LED-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007,FCT-008,FCT-009,FCT-010,FCT-011,FCT-012,FCT-013,FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,FCT-019,FCT-020,FCT-021,FCT-022 | final:SATURATED | gap:NONE
LED-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-010,QRY-015 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-005,FCT-007,FCT-008,FCT-010,FCT-013,FCT-015,FCT-016,FCT-021,FCT-022 | final:SATURATED | gap:NONE
AXS-001 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-008,FCT-010,FCT-013,FCT-015,FCT-016,FCT-021 | final:SATURATED | gap:NONE
AXS-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-006,FCT-007 | final:SATURATED | gap:NONE
AXS-003 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-008,FCT-009,FCT-010,FCT-011 | final:SATURATED | gap:NONE
AXS-004 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-012,FCT-013 | final:SATURATED | gap:NONE
AXS-005 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-014,FCT-015,FCT-016,FCT-017,FCT-018 | final:SATURATED | gap:NONE
AXS-006 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-019,FCT-020,FCT-021,FCT-022 | final:SATURATED | gap:NONE
AXS-007 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-011,FCT-018,FCT-019 | final:SATURATED | gap:NONE
AXS-008 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,QRY-005,QRY-006,QRY-007,QRY-008,QRY-009,QRY-010,QRY-011,QRY-012,QRY-013,QRY-014,QRY-015 | support:- | counter:- | results:FCT-001,FCT-005,FCT-007,FCT-010,FCT-015,FCT-016 | final:SATURATED | gap:NONE
CLM-001 | attempts:QRY-007,QRY-008,QRY-010,SRC-007,SRC-008,SRC-010 | support:FCT-008,FCT-010,FCT-013,FCT-015,FCT-016,FCT-021 | counter:- | results:FCT-008,FCT-010,FCT-013,FCT-015,FCT-016,FCT-021 | final:SUPPORTED | gap:NONE
CLM-002 | attempts:QRY-001,QRY-002,QRY-003,QRY-004,SRC-001,SRC-002,SRC-003,SRC-004 | support:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005 | counter:FCT-001(initial official jamming statement) | results:FCT-001,FCT-002,FCT-003,FCT-004,FCT-005,FCT-001(initial official jamming statement) | final:SUPPORTED | gap:ACCESS
CLM-003 | attempts:QRY-001,QRY-002,QRY-004,QRY-005,SRC-001,SRC-002,SRC-004,SRC-005 | support:FCT-001,FCT-002,FCT-005,FCT-007 | counter:FCT-007(official denial is only a claim) | results:FCT-001,FCT-002,FCT-005,FCT-007,FCT-007(official denial is only a claim) | final:PARTIAL | gap:ATTRIBUTION
CLM-004 | attempts:QRY-006,QRY-007,SRC-006,SRC-007 | support:FCT-008,FCT-009,FCT-010,FCT-011 | counter:- | results:FCT-008,FCT-009,FCT-010,FCT-011 | final:SUPPORTED | gap:ATTRIBUTION
CLM-005 | attempts:QRY-008,SRC-008 | support:FCT-012,FCT-013 | counter:- | results:FCT-012,FCT-013 | final:SUPPORTED | gap:ATTRIBUTION
CLM-006 | attempts:QRY-009,QRY-010,QRY-011,QRY-012,SRC-009,SRC-010,SRC-011,SRC-012 | support:FCT-014,FCT-015,FCT-016,FCT-017,FCT-018 | counter:The DOJ language is allegation based on an affidavit and Treasury is an executive administrative designation,not a final criminal adjudication. | results:FCT-014,FCT-015,FCT-016,FCT-017,FCT-018,The DOJ language is allegation based on an affidavit and Treasury is an executive administrative designation,not a final criminal adjudication. | final:SUPPORTED | gap:NONE
CLM-007 | attempts:QRY-009,QRY-010,QRY-011,QRY-012,SRC-009,SRC-010,SRC-011,SRC-012 | support:FCT-014,FCT-015,FCT-016,FCT-017,FCT-018 | counter:- | results:FCT-014,FCT-015,FCT-016,FCT-017,FCT-018 | final:SUPPORTED | gap:NONE
CLM-008 | attempts:QRY-007,QRY-013,QRY-014,QRY-015,SRC-007,SRC-013,SRC-014,SRC-015 | support:FCT-019,FCT-020,FCT-021,FCT-022 | counter:- | results:FCT-019,FCT-020,FCT-021,FCT-022 | final:SUPPORTED | gap:ATTRIBUTION
CLM-009 | attempts:QRY-007,QRY-012,QRY-013,QRY-014,SRC-007,SRC-012,SRC-013,SRC-014 | support:FCT-011,FCT-018,FCT-019,FCT-020 | counter:- | results:FCT-011,FCT-018,FCT-019,FCT-020 | final:SUPPORTED | gap:CAUSALITY

## STATUS_DELTA_V1
NONE

## OPEN_GAPS_V1
CLM-002 | CLM | SUPPORTED | ACCESS | Aircraft/airline avionics logs and any completed Bulgarian technical investigation were not public in the scoped record.
CLM-003 | CLM | PARTIAL | ATTRIBUTION | No public technical chain from signal source/operator to Russian state tasking/intent was found.
CLM-004 | CLM | SUPPORTED | ATTRIBUTION | Commanditaire identity and causal electoral effect remain unresolved.
CLM-005 | CLM | SUPPORTED | ATTRIBUTION | Ultimate operator/commanditaire not identified in the scoped public source.
CLM-008 | CLM | SUPPORTED | ATTRIBUTION | Direct public tasking evidence between GRU Unit 29155 and the specific Storm information operations was not identified in the scoped sources.
CLM-009 | CLM | SUPPORTED | CAUSALITY | General causal effects require exposure/behavior data and credible counterfactual designs.
CAU-001 | CAU | UNRESOLVED | CAUSALITY | The reviewed public sources do not identify individual/group persuasion or a counterfactual vote effect.
CAU-002 | CAU | UNRESOLVED | CAUSALITY | No causal design in the scoped evidence identifies the effect of the attribution claim itself.

SEMANTIC_COUNTS_V1:LED:2|CLM:9|AXS:8|CAU:2|CTRL:4|ACT:0

## SEMANTIC_REGISTRIES_V1

### LEAD_REGISTRY_V1
LED-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015"],"evidence_excerpt":"audit attribution chain: incident observable -> operator -> commanditaire/state -> intention -> effect","kind":"HYPOTHESIS","lead":"Public attribution of interference is a multi-edge chain whose evidentiary strength can differ sharply at incident, operator, state/tasking and effect levels.","linked_ids":["AXS-001","AXS-002","AXS-003","AXS-004","AXS-005","AXS-006","AXS-007","AXS-008","CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009"],"locator":"OBJECT_QUESTION","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007","FCT-008","FCT-009","FCT-010","FCT-011","FCT-012","FCT-013","FCT-014","FCT-015","FCT-016","FCT-017","FCT-018","FCT-019","FCT-020","FCT-021","FCT-022"],"routes":["OBJECT_INVESTIGATION","ATTRIBUTION","COUNTER_HYPOTHESES"],"source_id":"INV-134_RUN_CARD","status":"SATURATED"}
LED-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-010","QRY-015"],"evidence_excerpt":"Toute accusation et tout démenti sont des claims; official statement != proof; adjacent attribution edges do not inherit proof.","kind":"METHOD_CONSTRAINT","lead":"Official accusation and official denial are both claims; technical infrastructure, operator identity, commanditaire, intention and effect must not be inherited from adjacent edges.","linked_ids":["CLM-001","CLM-002","CLM-003","CLM-004","CLM-005","CLM-006","CLM-007","CLM-008","CLM-009","CAU-001","CAU-002","CTRL-001","CTRL-002","CTRL-003","CTRL-004"],"locator":"SCOPE","materiality":"DECISIVE","result_ids":["FCT-001","FCT-002","FCT-003","FCT-005","FCT-007","FCT-008","FCT-010","FCT-013","FCT-015","FCT-016","FCT-021","FCT-022"],"routes":["RULES_CONTROLS","COUNTER_HYPOTHESES"],"source_id":"INV-134_RUN_CARD","status":"SATURATED"}

### CLAIM_REGISTRY_V1
CLM-001 | {"claim":"Attribution is not binary: the defensible public chain is incident/event -> observable artifact/infrastructure -> operator -> intermediary -> commanditaire/state -> tasking/intent -> exposure -> effect, and each edge requires its own evidence.","claimant":"INV-134 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-008","FCT-010","FCT-013","FCT-015","FCT-016","FCT-021"]}
CLM-002 | {"claim":"In the Plovdiv case, a crew-reported GPS-approach problem is supported, but the public record inspected does not establish that the aircraft was GPS-jammed; contemporaneous raw ADS-B indicators and later Bulgarian statements materially contradict the stronger initial jamming narrative.","claimant":"INV-134 synthesis","counter":"FCT-001(initial official jamming statement)","gap":"Aircraft/airline avionics logs and any completed Bulgarian technical investigation were not public in the scoped record.","gap_type":"ACCESS","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005"]}
CLM-003 | {"claim":"The stronger Plovdiv proposition that Russia deliberately targeted von der Leyen aircraft is not established by the public evidence inspected: the initial statement reported Bulgarian suspicion, the Commission later said it had not claimed targeting, and the Russian denial is not exculpatory proof.","claimant":"INV-134 synthesis","counter":"FCT-007(official denial is only a claim)","gap":"No public technical chain from signal source/operator to Russian state tasking/intent was found.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"PARTIAL","support":["FCT-001","FCT-002","FCT-005","FCT-007"]}
CLM-004 | {"claim":"Rokh Solis is strongly established as an inauthentic foreign operation with Israeli technical markers, but the Blackcore edge remains qualified and the identity/origin of the commanditaires is explicitly unresolved; visibility was low and electoral persuasion/effect is not established.","claimant":"INV-134 synthesis","counter":"NONE_FOUND","gap":"Commanditaire identity and causal electoral effect remain unresolved.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-008","FCT-009","FCT-010","FCT-011"]}
CLM-005 | {"claim":"Portal Kombat demonstrates the same evidentiary stop at a different layer: TigerWeb infrastructure/administration is documented, while VIGINUM only hypothesizes a service-provider relationship to an unknown ultimate operator.","claimant":"INV-134 synthesis","counter":"NONE_FOUND","gap":"Ultimate operator/commanditaire not identified in the scoped public source.","gap_type":"ATTRIBUTION","materiality":"HIGH","status":"SUPPORTED","support":["FCT-012","FCT-013"]}
CLM-006 | {"claim":"Doppelganger/RRN provides a materially stronger public state-command chain than Rokh Solis or Portal Kombat because the DOJ attribution references internal strategy meeting notes, project proposals and records, and Treasury separately imposed administrative designations for acting on behalf of the Russian government.","claimant":"INV-134 synthesis","counter":"The DOJ language is allegation based on an affidavit and Treasury is an executive administrative designation, not a final criminal adjudication.","gap":"NONE","gap_type":"NONE","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-014","FCT-015","FCT-016","FCT-017","FCT-018"]}
CLM-007 | {"claim":"The RRN/Doppelganger record shows attribution can strengthen over time: VIGINUM 2023 established operation and Russian actors/companies without public Presidential Administration command, while 2024 US actions and 2025 VIGINUM synthesis added a documented state-direction layer.","claimant":"INV-134 synthesis","counter":"NONE_FOUND","gap":"NONE","gap_type":"NONE","materiality":"HIGH","status":"SUPPORTED","support":["FCT-014","FCT-015","FCT-016","FCT-017","FCT-018"]}
CLM-008 | {"claim":"For Storm-1516, VIGINUM can attribute specific operations to the MOI with high confidence, but the public bridge from that MOI to GRU Unit 29155 is presented in the municipal report as an open-source attribution; independent evidence that Unit 29155 exists and conducts cyber operations does not itself prove tasking of Storm information operations.","claimant":"INV-134 synthesis","counter":"NONE_FOUND","gap":"Direct public tasking evidence between GRU Unit 29155 and the specific Storm information operations was not identified in the scoped sources.","gap_type":"ATTRIBUTION","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-019","FCT-020","FCT-021","FCT-022"]}
CLM-009 | {"claim":"Even strong attribution of an operation or command chain does not establish democratic effect: the reviewed sources often measure visibility, infrastructure and intent, while persuasion, vote change and counterfactual electoral outcomes remain unobserved or explicitly difficult to estimate.","claimant":"INV-134 synthesis","counter":"NONE_FOUND","gap":"General causal effects require exposure/behavior data and credible counterfactual designs.","gap_type":"CAUSALITY","materiality":"DECISIVE","status":"SUPPORTED","support":["FCT-011","FCT-018","FCT-019","FCT-020"]}

### AXIS_REGISTRY_V1
AXS-001 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"ATTRIBUTION_MODEL","links":["CLM-001"],"question":"What are the separable evidentiary edges from incident to effect?","result_ids":["FCT-008","FCT-010","FCT-013","FCT-015","FCT-016","FCT-021"],"sought_objects":["ATTRIBUTION_MODEL"],"status":"SATURATED"}
AXS-002 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"PLOVDIV","links":["CLM-002","CLM-003"],"question":"Which parts of the Plovdiv GPS/Russia narrative survived technical and official contradiction?","result_ids":["FCT-001","FCT-002","FCT-003","FCT-004","FCT-005","FCT-006","FCT-007"],"sought_objects":["PLOVDIV"],"status":"SATURATED"}
AXS-003 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"ROKH_SOLIS","links":["CLM-004"],"question":"How far can Rokh Solis be attributed from operation to Blackcore/client/effect?","result_ids":["FCT-008","FCT-009","FCT-010","FCT-011"],"sought_objects":["ROKH_SOLIS"],"status":"SATURATED"}
AXS-004 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"PORTAL_KOMBAT","links":["CLM-005"],"question":"Does infrastructure/operator identification establish commanditaire?","result_ids":["FCT-012","FCT-013"],"sought_objects":["PORTAL_KOMBAT"],"status":"SATURATED"}
AXS-005 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"DOPPELGANGER","links":["CLM-006","CLM-007"],"question":"What public evidence supports the stronger Russian state-command attribution?","result_ids":["FCT-014","FCT-015","FCT-016","FCT-017","FCT-018"],"sought_objects":["DOPPELGANGER"],"status":"SATURATED"}
AXS-006 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"STORM1516","links":["CLM-008"],"question":"How strong are operation-to-MOI and MOI-to-GRU edges separately?","result_ids":["FCT-019","FCT-020","FCT-021","FCT-022"],"sought_objects":["STORM1516"],"status":"SATURATED"}
AXS-007 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"IMPACT","links":["CLM-009","CAU-001"],"question":"Does attribution establish persuasion or electoral effect?","result_ids":["FCT-011","FCT-018","FCT-019"],"sought_objects":["IMPACT"],"status":"SATURATED"}
AXS-008 | {"attempt_ids":["QRY-001","QRY-002","QRY-003","QRY-004","QRY-005","QRY-006","QRY-007","QRY-008","QRY-009","QRY-010","QRY-011","QRY-012","QRY-013","QRY-014","QRY-015"],"axis":"SYMMETRY","links":["CLM-001","CTRL-004"],"question":"Does the method downgrade both official accusations and denials when evidence is absent?","result_ids":["FCT-001","FCT-005","FCT-007","FCT-010","FCT-015","FCT-016"],"sought_objects":["SYMMETRY"],"status":"SATURATED"}

### CAUSALITY_REGISTRY_V1
CAU-001 | {"counter":"Low/limited visibility in Rokh Solis and low effectiveness assessment for RRN; operation existence is insufficient.","gap":"The reviewed public sources do not identify individual/group persuasion or a counterfactual vote effect.","gap_type":"CAUSALITY","limit":"Requires reliable exposure and outcome data plus experimental/quasi-experimental or strong comparative identification.","mechanism":"Attributed influence operation -> authentic exposure/reception -> opinion or vote change","status":"UNRESOLVED","support":["FCT-011","FCT-018","FCT-019"]}
CAU-002 | {"counter":"The Plovdiv narrative changed materially after technical/official contradiction, but downstream belief/policy effects were not measured.","gap":"No causal design in the scoped evidence identifies the effect of the attribution claim itself.","gap_type":"CAUSALITY","limit":"Requires time-resolved media/public-opinion/policy data and a defensible counterfactual.","mechanism":"Public attribution/denial -> public belief or policy response","status":"UNRESOLVED","support":["FCT-001","FCT-002","FCT-007"]}

### CONTROL_REGISTRY_V1
CTRL-001 | {"control":"Plovdiv positive-control test: the same aircraft raw ADS-B fields showed NIC/NACp collapse during a genuine interference episode the previous day but not on the Plovdiv flight, so the technical counter is not merely absence of a visible anomaly.","status":"SUPPORTED","support":["FCT-005"]}
CTRL-002 | {"control":"Rokh Solis commanditaire control: VIGINUM itself warns technical/intermediary geography can differ from commanditaire origin and explicitly says the client identity/origin is not established.","status":"SUPPORTED","support":["FCT-008","FCT-010"]}
CTRL-003 | {"control":"Doppelganger evidence-quality control: state-direction attribution is supported by reported internal strategy records plus separate administrative sanctions and later French synthesis, unlike cases based only on infrastructure similarity.","status":"SUPPORTED","support":["FCT-015","FCT-016","FCT-017","FCT-018"]}
CTRL-004 | {"control":"Symmetric authority control: Commission/Russia/VIGINUM/DOJ/Treasury statements are encoded according to their evidence and procedural status; no official statement or denial is promoted merely because of institutional authority.","status":"SUPPORTED","support":["FCT-001","FCT-002","FCT-007","FCT-010","FCT-015","FCT-016"]}

### ACTION_REGISTRY_V1

SEARCH_ACTIVITY_V1:WEB:0|FETCH:15|EXA:0
SECTION_STATUS_V1:{"ACTOR_NETWORK_MAP":"SET","CAUSALITY_REGISTRY":"DERIVED","CLAIM_REGISTRY":"DERIVED","COGNITIVE_MAP":"SET","CONTRADICTION_LEDGER":"SET","CONTROL_MAP":"DERIVED","CREDO":"SET","DIALECTICAL_MAP":"SET","EDI_REPORT":"SET","GATE_STATUS_V1":"SET","IMPACT_MAP":"SET","INVESTIGATION_MAP":"DERIVED","LEAD_REGISTRY":"DERIVED","MANIPULATION_REPORT":"SET","MODULE_EXECUTION":"EMPTY","NEXT_QUERIES":"SET","OPEN_GAPS":"DERIVED","RESOURCE_FLOW_MAP":"SET","RESPONSIBILITY_MAP":"SET","SCOPING_REPORT":"SET","STATUS_DELTA":"DERIVED","TEMPORAL_STATE":"SET","TRACE_MATRIX":"DERIVED","VERIFICATION_REPORT":"SET"}

## REQUEST_LOG
SYS-001 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-002 | SYS | NONE | runtime | - | MEMORY_PROBE
SYS-003 | SYS | FAIL:MNEMO_UNAVAILABLE | MNEMO | subject-fp lookup | MNEMO_Q
SYS-004 | SYS | OK | web | INV-134 | WEB_RESEARCH
SYS-005 | SYS | PASS | runtime | ATTEMPT-001 | PERSIST_REBIND
QRY-001 | FETCH | FOUND | SRC-001 | https://www.reuters.com/world/europe/eu-says-von-der-leyens-plane-gps-system-was-jammed-russian-interference-2025-09-01/ | Reuters initial Plovdiv attribution claim
QRY-002 | FETCH | FOUND | SRC-002 | https://audiovisual.ec.europa.eu/en/media/video/I-276622 | European Commission Plovdiv follow-up briefing
QRY-003 | FETCH | FOUND | SRC-003 | https://www.bta.bg/en/news/bulgaria/960380-pm-zhelyazkov-no-gps-interference-detected-during-plovdiv-landing- | Bulgarian News Agency PM Plovdiv statement
QRY-004 | FETCH | FOUND | SRC-004 | https://www.flightradar24.com/blog/aviation-explainer-series/ursula-von-der-leyen-gps-jamming/ | Flightradar24 Plovdiv technical analysis
QRY-005 | FETCH | FOUND | SRC-005 | https://www.reuters.com/world/europe/russia-rejects-accusations-over-eu-plane-jamming-fake-2025-09-04/ | Reuters Russian denial Plovdiv
QRY-006 | FETCH | FOUND | SRC-006 | https://www.sgdsn.gouv.fr/viginum/publications/rokh-solis-analyse-dun-mode-operatoire-informationnel-ayant-cible-les | VIGINUM Rokh Solis public page
QRY-007 | FETCH | FOUND | SRC-007 | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | VIGINUM municipal elections 2026 report
QRY-008 | FETCH | FOUND | SRC-008 | https://www.sgdsn.gouv.fr/publications/portal-kombat-suite-des-investigations-sur-le-reseau-structure-et-coordonne-de | VIGINUM Portal Kombat follow-up
QRY-009 | FETCH | FOUND | SRC-009 | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et | VIGINUM RRN 2023
QRY-010 | FETCH | FOUND | SRC-010 | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign | US DOJ Doppelganger disruption
QRY-011 | FETCH | FOUND | SRC-011 | https://home.treasury.gov/news/press-releases/jy2195 | US Treasury Kremlin-directed influence sanctions
QRY-012 | FETCH | FOUND | SRC-012 | https://www.sgdsn.gouv.fr/files/2025-02/20250224_TLP-CLEAR_NP_SGDSN_VIGINUM_War%20in%20Ukraine_Three%20years%20of%20Russian%20information%20operations_1.0_VF.pdf | VIGINUM three years of Russian information operations
QRY-013 | FETCH | FOUND | SRC-013 | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | VIGINUM Storm-1516 analysis
QRY-014 | FETCH | FOUND | SRC-014 | https://www.sgdsn.gouv.fr/publications/storm-1516-detection-dune-operation-dingerence-numerique-etrangere-ciblant-emmanuel | VIGINUM Storm-1516 Macron operation
QRY-015 | FETCH | FOUND | SRC-015 | https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/article/3895808/nsa-fbi-cisa-and-allies-issue-advisory-about-russian-military-cyber-actors/ | NSA/FBI/CISA/allies GRU Unit 29155 advisory

## EVIDENCE_REGISTRY
SRC-001 | ◈ | fam:other:reuters | REUTERS-PLOVDIV-INITIAL | Reuters initial Plovdiv attribution claim | 2025-09-01 | 2026-09-06T16:05:00Z | Commission statement; Bulgarian suspicion; targeting not established | https://www.reuters.com/world/europe/eu-says-von-der-leyens-plane-gps-system-was-jammed-russian-interference-2025-09-01/
SRC-002 | ◈ | fam:other:eu-commission | EC-PLOVDIV-FOLLOWUP | European Commission Plovdiv follow-up briefing | 2025-09-04 | 2026-09-06T16:05:00Z | Commission keeps interference claim but says it never claimed deliberate targeting | https://audiovisual.ec.europa.eu/en/media/video/I-276622
SRC-003 | ◈ | fam:other:bta | BTA-PLOVDIV | Bulgarian News Agency PM Plovdiv statement | 2025-09-04 | 2026-09-06T16:05:00Z | Bulgarian PM statement; onboard systems operational | https://www.bta.bg/en/news/bulgaria/960380-pm-zhelyazkov-no-gps-interference-detected-during-plovdiv-landing-
SRC-004 | ◈ | fam:other:flightradar24 | FR24-PLOVDIV | Flightradar24 Plovdiv technical analysis | 2025-09-04 | 2026-09-06T16:05:00Z | ADS-B NIC/NACp technical control; previous-day positive control | https://www.flightradar24.com/blog/aviation-explainer-series/ursula-von-der-leyen-gps-jamming/
SRC-005 | ◈ | fam:other:reuters | REUTERS-PLOVDIV-DENIAL | Reuters Russian denial Plovdiv | 2025-09-04 | 2026-09-06T16:05:00Z | Russian Foreign Ministry denial; claim only | https://www.reuters.com/world/europe/russia-rejects-accusations-over-eu-plane-jamming-fake-2025-09-04/
SRC-006 | ◈ | fam:other:viginum | VIGINUM-ROKH-PAGE | VIGINUM Rokh Solis public page | 2026-06-11 | 2026-09-06T16:05:00Z | Operation, Israeli technical markers, Blackcore, low visibility | https://www.sgdsn.gouv.fr/viginum/publications/rokh-solis-analyse-dun-mode-operatoire-informationnel-ayant-cible-les
SRC-007 | ◈ | fam:other:viginum | VIGINUM-MUNICIPALES-2026 | VIGINUM municipal elections 2026 report | 2026-06-11 | 2026-09-06T16:05:00Z | Definition, commanditaire caveat, Rokh details, visibility/impact limits, Storm open-source attribution | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf
SRC-008 | ◈ | fam:other:viginum | VIGINUM-PORTAL-KOMBAT | VIGINUM Portal Kombat follow-up | 2024-02-14 | 2026-09-06T16:05:00Z | TigerWeb infrastructure/operator layer; ultimate operator unknown | https://www.sgdsn.gouv.fr/publications/portal-kombat-suite-des-investigations-sur-le-reseau-structure-et-coordonne-de
SRC-009 | ◈ | fam:other:viginum | VIGINUM-RRN-2023 | VIGINUM RRN 2023 | 2023-06-13 | 2026-09-06T16:05:00Z | RRN observable campaign and Russian/russophone actors before later state-command attribution | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et
SRC-010 | ◈ | fam:other:us-doj | DOJ-DOPPELGANGER-2024 | US DOJ Doppelganger disruption | 2024-09-04 | 2026-09-06T16:05:00Z | Affidavit-based direction/control claim and internal strategy records | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign
SRC-011 | ◈ | fam:other:us-treasury | TREASURY-DOPPELGANGER-2024 | US Treasury Kremlin-directed influence sanctions | 2024-03-20 | 2026-09-06T16:05:00Z | Administrative designation of SDA/Structura; Presidential Administration direction | https://home.treasury.gov/news/press-releases/jy2195
SRC-012 | ◈ | fam:other:viginum | VIGINUM-RRN-2025 | VIGINUM three years of Russian information operations | 2025-02-24 | 2026-09-06T16:05:00Z | French synthesis of DOJ attribution plus low-effect/vendor-incentive caution | https://www.sgdsn.gouv.fr/files/2025-02/20250224_TLP-CLEAR_NP_SGDSN_VIGINUM_War%20in%20Ukraine_Three%20years%20of%20Russian%20information%20operations_1.0_VF.pdf
SRC-013 | ◈ | fam:other:viginum | VIGINUM-STORM-1516-2025 | VIGINUM Storm-1516 analysis | 2025-05-06 | 2026-09-06T16:05:00Z | 77 operations, actor network, real impact difficult to estimate | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516
SRC-014 | ◈ | fam:other:viginum | VIGINUM-STORM-MACRON-2026 | VIGINUM Storm-1516 Macron operation | 2026-02-06 | 2026-09-06T16:05:00Z | High-confidence MOI attribution based on narrative/content/distribution chain | https://www.sgdsn.gouv.fr/publications/storm-1516-detection-dune-operation-dingerence-numerique-etrangere-ciblant-emmanuel
SRC-015 | ◈ | fam:other:multiagency-cyber | NSA-GRU29155-2024 | NSA/FBI/CISA/allies GRU Unit 29155 advisory | 2024-09-05 | 2026-09-06T16:05:00Z | Multiagency cyber attribution to GRU Unit 29155; does not itself bridge to Storm information operations | https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/article/3895808/nsa-fbi-cisa-and-allies-issue-advisory-about-russian-military-cyber-actors/

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.reuters.com/world/europe/eu-says-von-der-leyens-plane-gps-system-was-jammed-russian-interference-2025-09-01/ | other:reuters | 2025-09-01 | Initial Commission/Bulgarian Plovdiv attribution | Reuters reported a Commission spokesperson saying GPS jamming was confirmed and that Bulgarian authorities suspected blatant interference by Russia; the EU supplied no further public technical detail and did not say the aircraft was deliberately targeted. | -
FCT-002 | FACT | ✧ | https://audiovisual.ec.europa.eu/en/media/video/I-276622 | other:eu-commission | 2025-09-04 | Commission follow-up narrows targeting claim | At the 4 September Commission briefing, the spokesperson cited the initial Bulgarian release saying the GPS signal disappeared and ground-based navigation was used, but explicitly said the Commission had never claimed deliberate targeting and had no information supporting targeting. | -
FCT-003 | FACT | ✧ | https://www.bta.bg/en/news/bulgaria/960380-pm-zhelyazkov-no-gps-interference-detected-during-plovdiv-landing- | other:bta | 2025-09-04 | Bulgarian PM operational-system counter | BTA reported Prime Minister Rosen Zhelyazkov saying the aircraft onboard systems were fully operational and the flight continuously monitored; the article was published under the headline that no GPS interference was detected during the Plovdiv landing. | -
FCT-004 | FACT | ✧ | https://www.flightradar24.com/blog/aviation-explainer-series/ursula-von-der-leyen-gps-jamming/ | other:flightradar24 | 2025-09-04 | Plovdiv crew issue without incident | Flightradar24 reports that the crew said it had an issue flying a GPS-based arrival, requested an ILS approach and landed without incident; this supports a navigation-approach problem without itself proving jamming. | -
FCT-005 | FACT | ✧ | https://www.flightradar24.com/blog/aviation-explainer-series/ursula-von-der-leyen-gps-jamming/ | other:flightradar24 | 2025-09-04 | Plovdiv raw ADS-B negative jamming indicators | Flightradar24 reports NIC=8 and NACp=10 throughout the Warsaw-Plovdiv flight, values not indicating GPS jamming, while the same aircraft the previous day showed NIC/NACp drops to zero during a separately observed interference episode, providing a positive technical control. | -
FCT-006 | FACT | ✧ | https://www.flightradar24.com/blog/aviation-explainer-series/ursula-von-der-leyen-gps-jamming/ | other:flightradar24 | 2025-09-04 | Plovdiv hour/paper-map narrative contradicted | Flightradar24 flight data contradicts the initial claim that the aircraft circled for an hour and relied on paper maps; the flight was extended by only a few minutes. | -
FCT-007 | FACT | ✧ | https://www.reuters.com/world/europe/russia-rejects-accusations-over-eu-plane-jamming-fake-2025-09-04/ | other:reuters | 2025-09-04 | Russian Plovdiv denial | The Russian Foreign Ministry called allegations of Russian responsibility fake and paranoia; this is an official denial and is not treated as proof of non-involvement. | -
FCT-008 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | other:viginum | 2026-06-11 | VIGINUM four-part INE definition and commanditaire caveat | VIGINUM defines a foreign digital interference through content, inauthentic behavior, harmful purpose and direct or indirect foreign involvement, and explicitly states that the geographic origin of digital assets or technical intermediaries may differ from the origin of the commanditaire. | -
FCT-009 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/rokh-solis-analyse-dun-mode-operatoire-informationnel-ayant-cible-les | other:viginum | 2026-06-11 | Rokh Solis operation and Israeli markers | VIGINUM says Rokh Solis used technically related sites and coordinated inauthentic relays, targeted French municipal candidates, and displayed technical foreignness markers indicating involvement of Israeli actors, including an influence company named Blackcore. | -
FCT-010 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | other:viginum | 2026-06-11 | Rokh Solis Blackcore edge is partial and client unknown | In the detailed municipal report, VIGINUM says Rokh Solis could present common characteristics with Blackcore activity and explicitly states that no element then allowed it to establish the identity or origin of the commanditaires who may have used the company. | -
FCT-011 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | other:viginum | 2026-06-11 | Rokh Solis visibility and impact bound | The municipal report says Rokh Solis content visibility remained limited despite artificial amplification; more generally the RCPE assessed detected operations as having limited visibility and weak impact on the national digital public debate, while distinguishing impact-risk estimation from observed effects. | -
FCT-012 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/portal-kombat-suite-des-investigations-sur-le-reseau-structure-et-coordonne-de | other:viginum | 2024-02-14 | Portal Kombat TigerWeb infrastructure role | VIGINUM identified a major role for Crimea-based Russian company TigerWeb in creating and administering Portal Kombat sites. | -
FCT-013 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/portal-kombat-suite-des-investigations-sur-le-reseau-structure-et-coordonne-de | other:viginum | 2024-02-14 | Portal Kombat ultimate operator remains hypothesis | VIGINUM says similarities with Inforos support the hypothesis that TigerWeb may be a service provider for an operator whose identity was unknown at that stage; technical/infrastructure attribution therefore did not close the commanditaire edge. | -
FCT-014 | FACT | ✧ | https://www.sgdsn.gouv.fr/viginum/publications/rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et | other:viginum | 2023-06-13 | RRN observable campaign before state-command closure | In 2023 VIGINUM documented RRN as a coordinated manipulation campaign using 355 impersonating domains, at least 58 French-targeting false articles and Russian or russophone individuals and Russian companies; the public synthesis did not yet establish Presidential Administration command. | -
FCT-015 | FACT | ✧ | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign | other:us-doj | 2024-09-04 | Doppelganger Presidential Administration direction allegation | The DOJ said 32 domains were used in Doppelganger and, as alleged in an unsealed FBI affidavit, SDA, Structura and ANO Dialog operated under the direction and control of the Russian Presidential Administration, particularly Sergei Kiriyenko, to spread covert propaganda and influence voters. | -
FCT-016 | FACT | ✧ | https://www.justice.gov/usao-edpa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign | other:us-doj | 2024-09-04 | Doppelganger internal-record basis | The DOJ says the underlying affidavit describes perpetrators own internal strategy meeting notes, project proposals and other records obtained in the investigation, providing a materially stronger public basis for tasking/command than infrastructure similarity alone. | -
FCT-017 | FACT | ✧ | https://home.treasury.gov/news/press-releases/jy2195 | other:us-treasury | 2024-03-20 | Treasury administrative state-direction finding | OFAC stated SDA and Structura were involved in a persistent foreign malign influence campaign at the direction of the Russian Presidential Administration and designated them for acting for or on behalf of the Government of Russia. | -
FCT-018 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/2025-02/20250224_TLP-CLEAR_NP_SGDSN_VIGINUM_War%20in%20Ukraine_Three%20years%20of%20Russian%20information%20operations_1.0_VF.pdf | other:viginum | 2025-02-24 | VIGINUM adoption of Doppelganger attribution with efficacy caution | VIGINUM later summarized the DOJ public attribution of RRN/Doppelganger to Sergei Kiriyenko and SDA/Structura/ANO Dialog, while judging campaign effectiveness low and noting internal SDA material indicating commercial incentives to exaggerate effective influence. | -
FCT-019 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/analyse-du-mode-operatoire-informationnel-russe-storm-1516 | other:viginum | 2025-05-06 | Storm-1516 operation-level characterization | VIGINUM says its Storm-1516 analysis covers 77 documented operations and a coordinated Russian influence ecosystem; it also states that real impact on the digital public debate remains difficult to estimate. | -
FCT-020 | FACT | ✧ | https://www.sgdsn.gouv.fr/publications/storm-1516-detection-dune-operation-dingerence-numerique-etrangere-ciblant-emmanuel | other:viginum | 2026-02-06 | Storm-1516 high-confidence MOI attribution | For a February 2026 operation targeting Emmanuel Macron, VIGINUM attributed the operation with high confidence to Storm-1516, with CopyCop technical support, based on the narrative, content type and dissemination chain. | -
FCT-021 | FACT | ✧ | https://www.sgdsn.gouv.fr/files/files/viginum/Publications/20260611_SGDSN_VIGINUM_Rapport-public_Elections-municipales.pdf | other:viginum | 2026-06-11 | Storm GRU bridge is presented as open-source attribution | The 2026 municipal report describes Storm-1516 as attributed to GRU Unit 29155 in open sources, then separately says VIGINUM attributed two municipal operations to Storm-1516/CopyCop with high confidence; the public text therefore contains different evidentiary levels for operation-to-MOI and MOI-to-state-unit. | -
FCT-022 | FACT | ✧ | https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/article/3895808/nsa-fbi-cisa-and-allies-issue-advisory-about-russian-military-cyber-actors/ | other:multiagency-cyber | 2024-09-05 | GRU Unit 29155 cyber attribution is not Storm proof | NSA, FBI, CISA and international partners assess GRU Unit 29155-affiliated cyber actors responsible for malicious cyber activity since at least 2020; this independently supports the existence/activity of the unit but does not by itself prove that Storm-1516 information operations are tasked by that unit. | -
<!-- /FACT_REGISTRY_V1 -->

## FCT_SOURCE_MAP_V1
FCT-001 | SRC-001
FCT-002 | SRC-002
FCT-003 | SRC-003
FCT-004 | SRC-004
FCT-005 | SRC-004
FCT-006 | SRC-004
FCT-007 | SRC-005
FCT-008 | SRC-007
FCT-009 | SRC-006
FCT-010 | SRC-007
FCT-011 | SRC-007
FCT-012 | SRC-008
FCT-013 | SRC-008
FCT-014 | SRC-009
FCT-015 | SRC-010
FCT-016 | SRC-010
FCT-017 | SRC-011
FCT-018 | SRC-012
FCT-019 | SRC-013
FCT-020 | SRC-014
FCT-021 | SRC-007
FCT-022 | SRC-015

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
CP-001 | LEADS | PASS | LAST_COMPLETED:5 LEADS | NEXT_ACTION:7 SCOPE
CP-002 | SCOPE | PASS | LAST_COMPLETED:7 SCOPE | NEXT_ACTION:9 SEARCH
CP-003 | SEARCH | PASS | LAST_COMPLETED:9 SEARCH | NEXT_ACTION:10 FACTS
CP-004 | FACTS | PASS | LAST_COMPLETED:10 FACTS | NEXT_ACTION:11 CAUSAL_GAP
CP-005 | CAUSAL_GAP | PASS | LAST_COMPLETED:11 CAUSAL_GAP | NEXT_ACTION:13 VERIFY
CP-006 | VERIFY | PASS | LAST_COMPLETED:13 VERIFY | NEXT_ACTION:17 INVESTIGATION_ACCOUNTABILITY
CP-007 | INVESTIGATION_ACCOUNTABILITY | PASS | LAST_COMPLETED:17 INVESTIGATION_ACCOUNTABILITY | NEXT_ACTION:18 FINALIZATION

## WRITEBACK_ATTEMPT_LOG_V1
ATTEMPT-001 | {"created_at":"2026-09-06T16:17:51.837646+00:00","fact_mem":{},"mnemo_row":"BLOCKED:MNEMO_UNAVAILABLE","result":"PASS","writeback_execution":[{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-001","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-002","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-003","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-004","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-005","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-006","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-007","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-008","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-009","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-010","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-011","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-012","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-013","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-014","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-015","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-016","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-017","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-018","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-019","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-020","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-021","reason":"MNEMO_UNAVAILABLE","success":0},{"action":"ELIGIBLE:VERIFIE","attempted":0,"blocked":1,"failure":0,"fct":"FCT-022","reason":"MNEMO_UNAVAILABLE","success":0}],"writeback_row":{"attempted":0,"blocked":22,"eligible":22,"failure":0,"success":0}}

PERSISTENCE_META: MNEMO_ROW:BLOCKED:MNEMO_UNAVAILABLE | SELF_WRITE_ROW:PENDING_AT_SERIALIZATION | WRITEBACK_ROW:{eligible:22;attempted:0;success:0;failure:0;blocked:22} | WRITEBACK_EXECUTION_V1:[22 rows, see section]

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
