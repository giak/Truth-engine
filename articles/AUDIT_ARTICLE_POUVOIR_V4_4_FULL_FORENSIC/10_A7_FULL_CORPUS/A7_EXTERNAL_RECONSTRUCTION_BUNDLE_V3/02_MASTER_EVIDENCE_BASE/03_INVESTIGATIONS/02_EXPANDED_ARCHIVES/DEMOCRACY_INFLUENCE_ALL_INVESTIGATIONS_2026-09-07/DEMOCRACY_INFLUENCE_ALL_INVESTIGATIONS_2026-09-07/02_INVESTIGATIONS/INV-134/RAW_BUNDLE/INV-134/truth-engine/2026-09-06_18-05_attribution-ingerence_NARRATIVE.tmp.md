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
