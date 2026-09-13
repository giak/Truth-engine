# INV-090 — Shadow banning, démonétisation, déréférencement et friction algorithmique

## Résultat central

Les restrictions de visibilité sans suppression totale sont réelles et documentées. Elles ne nécessitent pas le mot imprécis « shadow ban » pour être établies : Meta a explicitement modifié le ranking du contenu politique, Instagram/Threads ont limité les recommandations politiques de comptes non suivis, X publie des données de « restricted reach labels », TikTok distingue contenu supprimé et contenu inéligible au For You Feed, et TikTok applique aussi des restrictions catégorielles de monétisation aux comptes politiques (FCT-001, FCT-005, FCT-011, FCT-031 à FCT-035).

La frontière centrale est toutefois stricte : **baisse de portée != shadowban politique != intention partisane != tasking étatique != persuasion != effet électoral**. Le corpus établit fortement les mécanismes en amont, partiellement leurs volumes et erreurs, mais ne ferme pas généralement les arêtes d’intention ni d’effet démocratique aval.

## Les plateformes modifient réellement la visibilité politique

Meta fournit le cas le plus clair de politique explicite. Dès 2021, la plateforme teste une réduction de distribution du contenu politique ; en 2022, elle dit avoir globalement implémenté un ranking donnant moins de poids à certains signaux pour réduire la quantité de politique vue (FCT-001/FCT-002). En 2024, Instagram et Threads annoncent qu’ils ne recommanderont plus proactivement le contenu politique de comptes non suivis sur Explore, Reels, recommandations de Feed et comptes suggérés (FCT-005/FCT-006). Cela établit une friction politique réelle et intentionnelle au niveau de la catégorie de contenu.

Mais ce mécanisme n’est ni caché ni stable : Meta annonce en janvier 2025 une réintroduction plus personnalisée du contenu civique/politique (FCT-008/FCT-009). Une baisse de reach observée en 2024 ne peut donc pas être projetée mécaniquement sur 2025-2026 sans identifier l’état de politique correspondant.

## France/UE : reach restrictions et corrections sont quantifiables

Le rapport DSA de X est un contrôle opérationnel précieux. Il nomme explicitement des Restricted Reach Labels et, pour la France entre avril et septembre 2024, rapporte 39 454 labels automatisés pour Hateful Conduct ; l’addition des lignes affichées de reach restriction pour Hateful Conduct, Abuse & Harassment et Violent Speech atteint 61 550 actions dans le rapport (FCT-011 à FCT-013). Ce nombre n’est pas un dénominateur politique : il prouve l’échelle d’une technique de limitation de portée, pas une prévalence de shadowban idéologique.

Les recours montrent en parallèle que l’action initiale n’est pas une vérité finale. X rapporte 46 222 plaintes françaises contre des suspensions, dont 12 047 renversées, et 6 772 plaintes contre des actions de contenu, dont 793 renversées (FCT-016/FCT-017). À l’échelle UE, la Commission indique que près de 30 % des 165 millions de décisions contestées via les mécanismes internes ont été inversées, tandis que les organismes extrajudiciaires ont renversé 52 % des affaires clôturées étudiées au premier semestre 2025 (FCT-018/FCT-020). L’erreur et la correction sont donc des composantes matérielles du système.

## L’État n’explique pas automatiquement la modération

Le corpus ne justifie pas de convertir la régulation ou l’existence de demandes publiques en commande générale de la visibilité. Dans le rapport X étudié, la France apparaît avec cinq information requests sous « negative effects on civic discourse or elections », mais aucun ordre de retrait français dans cette catégorie ; les huit ordres de retrait français listés concernent les produits dangereux ou illégaux (FCT-014/FCT-015).

Plus largement, la Commission indique qu’au premier semestre 2025, 99 % des plus de neuf milliards de décisions de modération déclarées relevaient des propres conditions générales des plateformes plutôt que de signalements de contenu illégal (FCT-019). Cela n’exclut pas des cas de tasking public. Cela interdit seulement d’attribuer l’agrégat au pouvoir public sans chaîne décisionnelle précise.

## « Shadowban politique » : les audits imposent une forte discipline

L’audit Journal of Communication d’environ 25 000 comptes Twitter conclut que les shadowbans étaient rares. Les comptes de type bot étaient plus touchés ; les réponses politiques étaient davantage downtiered, mais à gauche comme à droite (FCT-022 à FCT-024).

Une autre expérience de grande échelle, publiée dans PNAS, montre qu’un ranking algorithmique peut produire une asymétrie politique : sur sept pays, la droite bénéficiait en moyenne d’une amplification supérieure à la gauche (FCT-025/FCT-026). C’est une différence d’exposition réelle, pas une preuve autonome d’intention partisane (FCT-027).

Le contrôle TikTok 2026 est encore plus important méthodologiquement : un écart apparemment massif dans des centaines de milliers d’observations horaires disparaît quand l’unité indépendante devient le compte. Les auteurs ne détectent alors pas de suppression de portée modérée à forte sur les trois sujets testés et attribuent le faux signal à la pseudoréplication/confusion (FCT-028 à FCT-030). Un gros volume de mesures corrélées n’est pas un gros faisceau indépendant.

## Démonétisation et curation politique

TikTok fournit un exemple de démonétisation politique réellement établie mais non clandestine : les comptes de politiciens et partis ont accès aux fonctions publicitaires automatiquement coupé et sont exclus de plusieurs outils de monétisation (FCT-031/FCT-032). Cela est une restriction économique catégorielle déclarée ; démonétisation != censure idéologique (FCT-033).

TikTok peut également rendre certains contenus électoraux inéligibles au For You Feed sans les supprimer, ce qui matérialise une restriction de recommandation (FCT-034/FCT-035). YouTube adopte une autre forme de curation en mettant en avant des sources dites autoritatives dans recherche et recommandations électorales (FCT-036/FCT-037). Dans les deux cas, la structure d’exposition est modifiée, mais l’effet électoral aval reste une question distincte.

## Plafond I0–I7

- I0 VERIFIED : plateformes, règles et types d’intervention identifiés.
- I1 VERIFIED : capacité de réduire/amplifier visibilité ou monétisation établie.
- I2 VERIFIED : interventions réelles documentées, y compris en France/UE.
- I3 VERIFIED/PARTIAL : règles et certains déclencheurs connus ; décision-level classifier/tasking souvent inaccessible.
- I4 VERIFIED case-specifically : changements d’exposition et asymétries mesurables dans plusieurs audits/rapports.
- I5 NOT_ESTABLISHED generally : motif politique/partisan non déductible de la seule asymétrie ou action.
- I6 NOT_ESTABLISHED generally : persuasion/comportement non fermés par les sources de visibilité ici.
- I7 NOT_ESTABLISHED : aucun effet causal général sur un résultat électoral n’est établi.

## Résidu matériel

Un nouvel effort ne changerait le modèle que s’il apporte un dataset France/UE à dénominateur politique comparatif reliant classification ou demande précise à l’action de reach, des logs d’appel/correction par orientation ou type de contenu, des documents de tasking public ou interne, ou un design causal reliant restriction de visibilité, exposition réelle, persuasion et vote. Des plaintes isolées de « shadowban » sans trace d’action ni dénominateur sont cumulatives, pas décisives.
