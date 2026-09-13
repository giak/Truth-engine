---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "truth_engine_narrative"
artifact_id: "INV-094-NARRATIVE"
version: "1.0"
status: "technical_frozen"
updated: "2026-09-07"
inv_id: "INV-094"
---

<!-- TRACE: run=20260907-1946-foreign-party-financing-europe; engine=2.10.6/R3P1; facts=FCT-001..FCT-028 -->

# INV-094 — Financement étranger direct ou indirect des partis et candidats européens

## Question et règle de preuve

Cette enquête ferme le bord laissé ouvert par INV-093 : lorsqu'un financement a une origine étrangère ou transite par un véhicule étranger, que peut-on réellement établir sur sa légalité, son bénéficiaire économique, un éventuel commandement politique et son effet électoral ?

La chaîne testée est : `principal étranger -> banque/personne/société/intermédiaire -> prêt/don/avantage -> parti ou candidat -> règle applicable -> contrôle/décision -> contrepartie ou tasking éventuel -> effet politique -> résultat électoral`. Chaque flèche reste indépendante. Les gardes sont donc : `foreign funding != interference`, `funding != command`, `loan != donation`, `intermediary != concealed principal`, `illegality != electoral effect`, `sanction != result changed`.

## 1. Le droit européen comparé ne traite pas « l'argent étranger » comme une catégorie unique

En France, le changement de 2017-2018 est matériel. Avant 2018, le code électoral et le régime de financement des partis interdisaient déjà les contributions et aides matérielles provenant d'un État étranger ou d'une personne morale étrangère, mais les versions examinées ne contenaient pas encore l'interdiction expresse ultérieure des prêts étrangers. Depuis 2018, les prêts d'un État étranger ou d'une personne morale de droit étranger sont expressément interdits, sauf établissements de crédit ou sociétés de financement répondant aux conditions UE/EEE. Pour les partis, les dons de personnes physiques sont en outre réservés aux personnes françaises ou résidant en France. [FCT-001 à FCT-007]

Cette architecture ne se généralise pas telle quelle à toute l'Europe. En Espagne, la loi organique permet des dons non affectés de personnes physiques étrangères sous les limites générales et les règles de mouvements de capitaux, tout en interdisant les financements de gouvernements, organismes et entreprises publiques étrangers ou d'entreprises qui leur sont liées. [FCT-019, FCT-020]

Pour les partis politiques européens, le règlement 1141/2014 interdit notamment les dons anonymes, ceux d'autorités publiques de pays tiers, ceux d'entreprises dominées par elles, ainsi que ceux d'entités privées établies dans un pays tiers et de certaines personnes de pays tiers non électrices aux élections européennes. Les dons non permis doivent être retournés ou faire l'objet d'une procédure de récupération. [FCT-021 à FCT-023]

Le Royaume-Uni applique encore une autre logique de « source permissible » : l'identité réelle du donateur et son éligibilité doivent être vérifiées au-dessus du seuil légal, et les fonds non identifiables ou non permis doivent être retournés. [FCT-024]

Le premier résultat est donc net : **origine étrangère et illégalité ne sont pas synonymes sans qualification de la juridiction, du type de source et du véhicule**. Une personne physique étrangère peut être admissible en Espagne dans des conditions où un État étranger ne l'est pas ; un établissement bancaire UE/EEE peut être admissible comme prêteur dans le droit français post-2018 là où une autre personne morale étrangère ne l'est pas.

## 2. Le prêt FN/RN–First Czech Russian Bank est un cas réel de financement étranger, mais un cas de droit ancien

Le Sénat documente qu'en 2014 le Front national a bénéficié d'un prêt supérieur à 9,1 millions d'euros de First Czech Russian Bank, établissement bancaire russe. Après la faillite de la banque en 2016, la créance a été reprise par la société russe Aviazapchast. Le prêt a été renégocié en 2019. [FCT-008, FCT-009]

Le point juridique décisif est temporel : le prêt a été contracté sous les règles antérieures à l'entrée en vigueur de la réforme de 2017, et la loi nouvelle a expressément préservé les contrats antérieurs. Le parti pouvait donc conserver cette dette au passif pendant son remboursement. [FCT-001, FCT-004, FCT-007, FCT-009]

Cela ferme deux erreurs symétriques. Premièrement, le prêt n'est pas une invention ou une simple allégation : sa source bancaire étrangère et sa chaîne de créance sont établies dans un document parlementaire officiel. Deuxièmement, l'existence de cette dette ne prouve pas qu'un prêt identique serait aujourd'hui juridiquement admissible sous les mêmes conditions ; le droit français a précisément été durci.

La limite probatoire est tout aussi importante. Auditionné par la commission d'enquête du Sénat, le président de la CNCCFP a indiqué que la Commission n'avait jamais pris une position permettant de qualifier positivement ce prêt d'« ingérence » et qu'elle ne disposait d'aucun moyen de savoir s'il était ou non assorti de contreparties. [FCT-010]

Le résultat correct est donc : `prêt étranger établi + dette/chaîne de créance établies + régime ancien établi`, mais `contrepartie politique`, `tasking`, `commandement` et `effet électoral` non établis par ce dossier réglementaire. Dire « financement étranger » est factuel ; dire « commandement étranger » exige une autre preuve.

## 3. Le dossier AfD montre pourquoi l'intermédiaire n'est pas le principal

Le cas allemand fournit un autre mécanisme. En 2017, dix-sept virements totalisant environ 132 000 euros sont arrivés depuis les comptes de deux sociétés suisses sur un compte de l'AfD Bodensee avec une mention les reliant à la campagne numérique d'Alice Weidel. [FCT-011]

L'enquête administrative et pénale a toutefois compliqué la chaîne d'attribution. La liste de donateurs produite par le parti comprenait des personnes qui ont ensuite indiqué ne pas avoir donné ; le parti a déclaré ne pas disposer d'informations fiables sur le véritable donateur. Le rapport du Bundestag indique qu'une enquête assistée par les autorités suisses a finalement fait apparaître le nom d'un donateur présumé, décrit comme un entrepreneur immobilier allemand résidant en Suisse. [FCT-012]

La décision de l'Oberverwaltungsgericht Berlin-Brandenburg ferme encore plus précisément le bord pertinent : économiquement, le don n'était pas attribuable aux deux sociétés suisses de transfert, mais à un donateur non identifié dans le constat juridictionnel. La juridiction a également rejeté l'argument d'un don direct à la candidate : le versement sur le compte du parti contribuait à le qualifier comme don au parti. [FCT-013, FCT-014]

La conséquence institutionnelle est forte : environ 396 000 euros de sanction, soit le triple du montant du don. [FCT-015, FCT-018]

Mais la qualification correcte reste bornée. Le dossier démontre qu'un véhicule étranger peut masquer ou ne pas révéler le bénéficiaire économique réel du flux et qu'une telle opacité peut produire une violation et une sanction lourdes. Il ne démontre pas, dans les pièces examinées, qu'un État étranger était le principal, ni que les sociétés suisses étaient elles-mêmes le principal économique, ni qu'un tasking étatique pilotait le parti. **Le pays du compte de transit n'est pas une preuve de la nationalité ou de la qualité du principal.**

## 4. Une violation de financement n'est pas automatiquement une preuve de corruption ou de commandement

Le rapport du Bundestag fournit ici un contrôle particulièrement utile. Pour qu'un don soit qualifié d'« influence donation » au sens du droit allemand, il faut une convention expresse ou implicite mais reconnaissable reliant le don à un avantage économique ou politique déterminé. Le rapport précise également que la proximité temporelle entre un don et une décision publique favorable ne suffit pas, à elle seule, à établir cette qualification. [FCT-016, FCT-017]

Ce seuil est cohérent avec la séparation nécessaire entre plusieurs étages :

`source étrangère -> donation interdite ou anonyme -> sanction` peut être démontré sans que `contrepartie spécifique -> commandement -> acte politique` le soit.

Le droit et les autorités ne traitent donc pas l'irrégularité financière comme une preuve automatique de corruption. Cette distinction est centrale pour INV-095 : un financeur peut avoir fourni une ressource matérielle ; il faut encore établir un accès particulier, une dette politique, une contrepartie, un pouvoir de sélection ou un tasking si l'on veut passer du financement au contrôle du candidat.

## 5. Les contrôles britanniques cassent deux inférences trop faciles

L'enquête de l'Electoral Commission sur UKIP et les structures européennes ADDE/IDDE constitue un bon contrôle négatif. Le polling financé par ces structures portait sur des zones et sujets potentiellement stratégiques pour UKIP, et deux prestataires avaient aussi occupé des fonctions de campaign managers pour des candidats UKIP. Pourtant, après collecte documentaire et auditions, la Commission a conclu qu'elle ne disposait pas de preuves suffisantes pour établir que les sondages avaient été commandés au bénéfice de UKIP ou que UKIP en avait reçu ou tiré bénéfice. Elle a donc conclu qu'ils ne constituaient pas un don à UKIP au sens du droit britannique. [FCT-027]

La Commission a en outre explicité que son appréciation d'une infraction devait satisfaire le standard pénal applicable, ce qui explique qu'elle puisse différer d'une appréciation institutionnelle européenne du même environnement factuel. [FCT-028]

Ce contrôle est important : `pertinence stratégique + chevauchement de personnes + financement externe` ne suffit pas à démontrer `avantage effectivement transféré au parti`.

Le contrôle Brexit Party produit une borne différente. L'Electoral Commission a estimé qu'une architecture de collecte en ligne créait un risque élevé et persistant d'accepter des dons non permis, et le parti a retourné un don de 1 000 livres parce qu'il ne pouvait pas déterminer si la source était permissible. [FCT-025, FCT-026]

Là encore, le bon verdict n'est pas « financement étranger démontré », mais `risque de conformité établi + mécanisme de retour utilisé + origine admissible non vérifiable dans un cas`. Le risque n'est pas l'acte prouvé.

## 6. Ce qui est établi, ce qui ne l'est pas

Le corpus ferme solidement I0 à I4 dans plusieurs cas : catégorie de source, véhicule, transfert, règle juridique, décision administrative ou judiciaire et sanction. Le prêt RN et les virements AfD démontrent que des flux d'origine ou de transit étrangers vers des structures partisanes sont des objets réels, et pas seulement des hypothèses. Les régimes français, allemand, espagnol, européen et britannique montrent simultanément que la qualification juridique varie fortement selon la source et la structure.

En revanche, **I5 n'est pas généralisable à partir du financement**. Le corpus ne ferme pas une chaîne générale `financeur étranger -> ordre politique -> comportement du candidat`. Dans le cas RN, la CNCCFP dit précisément ne pas disposer de preuve de contreparties. Dans le cas allemand, le standard de preuve d'une convention de contrepartie est plus exigeant que la seule existence du don. Dans le contrôle UKIP, le bénéfice lui-même n'est pas établi malgré la proximité organisationnelle.

I6 et I7 restent plus faibles encore. Aucune source examinée ne fournit un design permettant d'isoler une persuasion des électeurs ou de démontrer qu'un financement étranger donné a changé le vainqueur ou le résultat contrefactuel d'une élection.

## Conclusion opérationnelle

INV-094 ferme le principal trou laissé par INV-093 sur la **qualification de l'argent étranger** :

1. des financements étrangers directs ou indirects de partis/candidats existent et peuvent être documentés ;
2. la légalité dépend du régime, de la date et de la catégorie de source ;
3. la France a durci les prêts étrangers à compter de 2018 et préservé les contrats antérieurs ;
4. un intermédiaire étranger ne suffit pas à identifier le principal économique ;
5. une violation financière, une anonymisation ou une sanction ne suffisent pas à établir commandement ou corruption ;
6. le financement ne ferme pas, sans preuve supplémentaire, les arêtes persuasion et résultat électoral.

Le delta à transmettre à INV-095 est donc précis : **les flux financiers peuvent créer capacité, dépendance ou accès potentiel, mais la sélection/cooptation d'un candidat doit être établie par des arêtes supplémentaires — bénéficiaire réel, contrepartie, tasking, accès, veto ou choix organisationnel — et non déduite de l'origine étrangère du financement.**

<!-- TRACE: terminal_delta=foreign_finance_real+legal_regimes_non_isomorphic+intermediary_not_principal+illegality_not_command+causal_ceiling; route=INV-095 -->
