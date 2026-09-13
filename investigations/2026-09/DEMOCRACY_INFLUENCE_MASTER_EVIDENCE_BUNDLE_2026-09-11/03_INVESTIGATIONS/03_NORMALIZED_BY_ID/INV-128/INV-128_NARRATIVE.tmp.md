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
