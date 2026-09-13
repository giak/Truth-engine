---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "truth_engine_narrative"
artifact_id: "INV-093-NARRATIVE"
version: "1.0"
status: "technical_frozen"
updated: "2026-09-07"
inv_id: "INV-093"
---

<!-- TRACE: run=20260907-1811-campaign-financing-france; engine=2.10.6/R3P1; facts=FCT-001..FCT-028 -->

# INV-093 — Financement des campagnes françaises : argent, prêts, partis, prestations et contournements

## Question et règle de preuve

L'enquête ne cherche pas à démontrer que l'argent « achète » mécaniquement une campagne, un candidat ou une élection. Elle reconstruit une chaîne plus exigeante : `source des fonds -> véhicule juridique -> transaction ou prestation -> compte de campagne -> règle applicable -> contrôle CNCCFP -> décision ou recours -> conséquence -> effet politique éventuel`.

Les séparations suivantes gouvernent tout le run : `donation != prêt`, `prêt != financement illicite`, `prestation != avantage caché`, `irrégularité != fraude`, `réformation ou rejet du compte != corruption`, `financement != commandement politique`, `conséquence institutionnelle != résultat électoral modifié`. Le financement étranger n'est utilisé ici que comme frontière juridique ou trou de traçabilité ; son analyse propre relève d'INV-094 et d'INV-140.

## 1. Une architecture fortement réglementée, mais composée de plusieurs canaux

Le droit français n'organise pas un canal unique de financement. Il distingue plusieurs formes de ressources et impose des contraintes différentes selon l'origine et le véhicule. Les dons des personnes physiques sont plafonnés à 4 600 euros pour les mêmes élections. Les personnes morales autres que les partis ou groupements politiques ne peuvent financer un candidat par don, ni lui fournir des biens, services ou avantages à un prix anormalement bas. Les contributions ou aides matérielles provenant d'un État étranger ou d'une personne morale étrangère sont prohibées, sous réserve des exceptions prévues pour certains établissements financiers de l'Union européenne ou de l'Espace économique européen. [FCT-001, FCT-002, FCT-003]

Les prêts consentis par des personnes physiques sont, eux, expressément possibles sous conditions. Ils ne doivent pas constituer une activité habituelle, leur durée est bornée et leur remboursement fait l'objet d'un suivi. Cela interdit de traiter le mot « prêt » comme un synonyme de financement clandestin. [FCT-004]

Le compte de campagne doit retracer les recettes selon leur origine et les dépenses selon leur nature. Les dépenses engagées pour le candidat par des soutiens ou des partis peuvent devoir être intégrées. La Commission nationale des comptes de campagne et des financements politiques dispose ensuite d'une gamme de décisions distinctes : approbation, réformation, rejet, modulation du remboursement, et, selon les cas, transmission au juge de l'élection ou au parquet. [FCT-005, FCT-006, FCT-007, FCT-008]

Le premier résultat est donc négatif à l'égard d'un modèle trop simple : le système n'est pas un espace non réglementé dans lequel tout flux est invisible. Il existe une architecture de déclaration, de contrôle contradictoire, de réformation et de sanction. Cette densité ne signifie toutefois pas que l'origine économique ultime de chaque euro est toujours parfaitement observable.

## 2. Les prêts et l'intervention des partis sont des mécanismes ordinaires

La présidentielle de 2022 fournit un contrôle particulièrement utile. Les données de la CNCCFP montrent que les campagnes combinent argent personnel, dons, financements des partis, prêts et remboursement public. Pour cette élection, les candidats ont déclaré environ 83,5 millions d'euros de dépenses et 85,2 millions d'euros de recettes ; le remboursement de l'État atteint environ 42,2 millions, les dons environ 9 millions et les contributions des partis environ 27 millions. [FCT-020]

Surtout, la CNCCFP a identifié 38 partis ayant participé au financement des douze candidats. Tous les candidats ont bénéficié d'un prêt d'une formation politique et, pour neuf d'entre eux, ce prêt constituait la principale modalité d'intervention du parti. Dans six cas, le parti avait lui-même emprunté auprès d'une banque afin de prêter au candidat, ce que la Commission décrit comme un « prêt miroir ». Pour Valérie Pécresse, Anne Hidalgo et Yannick Jadot, les contributions définitives du parti dominaient au contraire. [FCT-021, FCT-022, FCT-023, FCT-024]

Ces constats ont une fonction méthodologique importante. Un prêt de parti, un prêt miroir, une dette envers une structure politique ou un financement via un véhicule partisan peuvent mériter un audit, mais leur seule existence ne démontre ni contournement, ni fraude, ni contrôle du candidat par le financeur. Le caractère licite ou illicite dépend de la qualité du prêteur, des conditions, de la comptabilisation, de la tarification des prestations et des faits propres au dossier.

La structure des financements évolue également. Le rapport 2024 de la CNCCFP indique une baisse de la part du crédit bancaire dans le financement des candidats, de 23 % en 2017 à 18 % en 2022 puis 8 % lors des législatives de 2024, tandis que les prêts de personnes physiques passent de 5 % à 9 % puis 13 %. [FCT-025, FCT-026]

## 3. Réformation, modulation, rejet et fraude ne sont pas le même objet

La présidentielle de 2017 fournit un deuxième contrôle négatif. La CNCCFP a relevé dans le compte de François Fillon 88 349 euros de dépenses omises et l'utilisation de quatre salles de réunion provenant de personnes morales non autorisées. La Commission a réformé le compte et diminué le remboursement de 50 000 euros ; elle ne l'a pas rejeté. [FCT-017]

Pour Emmanuel Macron, la Commission a examiné 87 600 euros de dons apparaissant initialement supérieurs au plafond individuel. Dans vingt cas sur vingt-quatre, l'analyse a retenu notamment l'imputation au conjoint et la bonne foi ; quatre dons restaient au-dessus du plafond pour un total de 18 300 euros. Là encore, le compte n'a pas été rejeté : le remboursement a été réduit. [FCT-018]

Ces exemples ne prouvent pas que les irrégularités sont bénignes. Ils prouvent autre chose, plus important pour la classification : le droit et le régulateur distinguent la correction comptable, la modulation financière, le rejet du compte et l'infraction pénale. Une analyse qui transforme toute réformation en fraude ou tout dépassement en corruption détruit cette gradation et produit un faux positif méthodologique.

## 4. Sarkozy 2012 et Bygmalion : deux voies juridiques distinctes

Le compte de Nicolas Sarkozy pour la présidentielle de 2012 se situe à un niveau différent. La CNCCFP l'a rejeté en décembre 2012. Elle relevait notamment un dépassement initial du plafond de 363 615 euros, ainsi que 1 567 425 euros de dépenses réintégrées, soit 7,35 % des dépenses déclarées. Elle a également traité comme contribution interdite de personne morale certaines manifestations à caractère électoral financées par le budget de l'État sans refacturation au mandataire. [FCT-009, FCT-010, FCT-011]

Le Conseil constitutionnel a ensuite réformé le compte, fixé les dépenses à 22 975 118 euros et les recettes à 23 094 932 euros, et maintenu le rejet. Le dépassement retenu du plafond autorisé était de 466 118 euros. [FCT-012, FCT-013]

Cette décision n'épuise toutefois pas le dossier Bygmalion. Dans l'arrêt du 26 novembre 2025, la Cour de cassation a rejeté les pourvois contre l'arrêt d'appel pénal de 2024 et confirmé des condamnations liées au financement illégal de la campagne, avec des qualifications comprenant notamment faux, escroquerie ou complicité selon les prévenus. Surtout, la Cour a explicitement borné la portée de l'autorité attachée à la décision du Conseil constitutionnel sur le compte de campagne : celle-ci ne bloque pas, de manière générale, un jugement pénal distinct sur des faits et infractions propres. [FCT-014, FCT-015]

Le cas est donc décisif pour la méthode. `Compte rejeté` et `fraude pénalement établie` ne sont ni synonymes ni mutuellement exclusifs. Ce sont deux voies de contrôle différentes, qui peuvent se succéder et porter sur des objets juridiques distincts. L'existence ultérieure d'une condamnation pénale ne permet pas, en retour, de requalifier automatiquement en fraude chaque réformation administrative observée dans d'autres campagnes.

## 5. Associations, prestations et « kits de campagne » : le véhicule peut être abusé sans être coupable par nature

Le dossier lié à l'association Jeanne et aux campagnes législatives de 2012 documente une autre famille de mécanismes. L'arrêt de la Cour de cassation du 19 juin 2024 retrace l'utilisation d'une association politique et d'une société autour d'un système de « kits de campagne », de prestations facturées et de crédit fournisseur, ainsi que d'autres prises en charge par une société. Les procédures pénales ont abouti à des condamnations pour des infractions comprenant escroquerie, recel et financement illégal selon les acteurs et les faits concernés. [FCT-028]

Ce cas établit qu'un véhicule associatif ou partisan, un prestataire, un kit standardisé ou un crédit fournisseur peuvent être intégrés dans un montage illicite lorsqu'une chaîne factuelle et juridique précise le démontre. Il n'établit pas que les micro-partis, associations de financement, prestations mutualisées ou crédits fournisseurs seraient frauduleux par nature. Le bon niveau d'analyse reste transactionnel : prix, service effectivement rendu, créancier, bénéficiaire, comptabilisation, remboursement, intention et décision judiciaire.

## 6. Le trou réel : l'origine amont de certains fonds individuels

La densité du contrôle aval ne ferme pas toute la chaîne. La CNCCFP explique demander des justificatifs sur l'origine de certains apports personnels importants, mais signale ne pas disposer de moyens juridiques suffisants pour établir pleinement l'origine des fonds prêtés par des personnes physiques ou donnés. Ce point devient plus matériel à mesure que les prêts de personnes physiques progressent dans la structure de financement. [FCT-025, FCT-026, FCT-027]

Il s'agit d'un trou de responsabilité et de traçabilité, pas d'une preuve positive de financement illicite. Le constat justifie une investigation ciblée sur l'origine bénéficiaire des fonds lorsqu'un cas matériel l'exige. Il ne justifie pas d'attribuer une origine étrangère, un prête-nom ou un commanditaire sans pièce supplémentaire. Cette frontière doit être routée vers INV-094 et INV-140.

## 7. Plafond causal et conséquences

Le run ferme solidement plusieurs étages de la chaîne : source juridique autorisée ou interdite, véhicule, transaction ou prestation, intégration au compte, contrôle, réformation ou rejet, et, dans certains dossiers, conséquence judiciaire ou pénale. On peut donc soutenir fortement I0 à I4 de manière cas-spécifique sur les dossiers les mieux documentés.

En revanche, l'enquête ne ferme pas les étages `financement -> commandement politique`, `financement -> persuasion des électeurs` ou `financement -> résultat électoral contrefactuel`. L'argent permet matériellement de mener une campagne ; le remboursement, le rejet ou une condamnation peuvent avoir des conséquences institutionnelles et politiques. Mais ces constats ne suffisent pas à établir qu'un financeur dirige politiquement le candidat, ni qu'un mécanisme de financement donné a changé le résultat du scrutin.

Le modèle le mieux soutenu est donc mixte : la France possède un système de financement électoral fortement réglementé, avec des mécanismes de financement ordinaires et une gradation réelle des contrôles ; des contournements ou fraudes peuvent être établis dans des cas précis lorsque la chaîne probatoire est fermée ; enfin, un trou de traçabilité amont subsiste pour certains fonds individuels. Le modèle « tout financement atypique est un contournement » est réfuté par les contrôles normaux. Le modèle inverse « le contrôle institutionnel rend le système entièrement traçable » est lui aussi trop fort.

<!-- TRACE: terminal_delta=regulated_multi-channel_system+graded_controls+case_specific_abuse+upstream_origin_gap; routes=INV-095,INV-102,INV-094,INV-140 -->
