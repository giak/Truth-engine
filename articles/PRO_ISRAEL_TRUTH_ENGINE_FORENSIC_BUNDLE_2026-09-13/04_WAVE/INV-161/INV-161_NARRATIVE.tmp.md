# INV-161 — ELNET : voyages parlementaires et effet causal

## Objet

Tester si les voyages parlementaires financés ou organisés par ELNET en Israël produisent un effet politique mesurable en France, en séparant strictement financement, accès, exposition, réception, comportement parlementaire et résultat politique.

## Résultat central

**FACT.** Les voyages ELNET constituent un canal d'exposition parlementaire quantitativement important. Au 1er décembre 2025, sous la XVIIe législature, le rapport de la commission des affaires étrangères recense 82 déclarations d'invitations à voyager émanant de 47 députés, dont 38 financées par ELNET. Le même passage cite, à titre de comparaison, 6 déclarations financées par Taïwan et 4 par le Qatar (FCT-001). Le cadre déontologique impose la déclaration préalable des voyages financés par un tiers (FCT-002).

**FACT.** Le phénomène n'est pas nouveau. Des déclarations officielles identifient de nombreux participants à une mission ELNET de juillet 2021 et décrivent une délégation de 38 élus reçue par de hautes autorités israéliennes, avec comme objectif déclaré le renforcement de la relation stratégique France-Israël (FCT-003 à FCT-005).

**FACT.** En mars 2023, ELNET rapporte avoir conduit quinze députés Les Républicains en Israël. Le programme combinait diplomatie publique, sécurité/défense et transition écologique (FCT-006). Le compte rendu de l'organisateur documente trois objets particulièrement discriminants : proposition d'un groupe parlementaire français sur les Accords d'Abraham (FCT-007), engagement rapporté de vigilance sur les fonds européens destinés à l'Autorité palestinienne (FCT-008), et inspiration revendiquée en matière de sécurité (FCT-009).

**FACT.** Des productions parlementaires postérieures sont congruentes avec certains de ces thèmes. Annie Genevard défend en mai 2023 une lecture favorable d'Israël et souligne l'importance des Accords d'Abraham (FCT-010). Pierre-Henri Dumont et Annie Genevard figurent parmi les cosignataires d'une résolution du 13 octobre 2023 sur l'éducation palestinienne (FCT-012) ; Dumont intervient ensuite sur les aides aux Palestiniens en janvier 2024 (FCT-013).

**CONTROL.** Cette congruence ne ferme pas l'effet causal. Pierre-Henri Dumont avait déjà pris position sur le cadrage des débats liés à Israël en février 2019, plusieurs années avant la mission de mars 2023 (FCT-011). Annie Genevard indique elle-même en mai 2023 avoir déjà rencontré à deux reprises des acteurs israéliens et palestiniens (FCT-010). Les participants ne sont donc pas assimilables à un groupe traité aléatoirement.

**CONTROL.** Le 7 octobre 2023 constitue en outre un choc externe majeur. Les actes parlementaires d'octobre 2023 et 2024 ne permettent pas d'isoler un effet marginal du voyage de mars 2023 de l'effet du conflit, des positions partisanes ou des préférences antérieures.

**FACT.** La HATVP qualifie les activités d'ELNET France de représentation d'intérêts exercée en propre et mentionne explicitement ses délégations parlementaires ainsi que diverses méthodes d'influence politique (FCT-014, FCT-015). ELNET affirme de son côté que la participation à ses délégations est volontaire et qu'aucune contrepartie politique n'est attendue (FCT-016). Cette affirmation intéressée est un contre-claim, non une preuve d'absence d'influence.

## Plafond causal

Le run ferme solidement :

`ressources ELNET -> voyage organisé/financé -> rencontres et briefings ciblés -> exposition parlementaire` = **SUPPORTED**.

Il ferme partiellement :

`exposition -> prompts/engagements politiques identifiables -> productions parlementaires congruentes` = **PARTIAL**.

Il ne ferme pas :

`voyage ELNET -> changement d'attitude -> comportement parlementaire causé -> résultat politique contre-factuel` = **CAUSAL_DESIGN GAP**.

Le mécanisme le plus plausible à tester n'est donc pas un « achat de votes », mais un effet de sélection et de renforcement : ELNET offre un accès structuré à des élus souvent déjà intéressés ou alignés, fournit des cadres, interlocuteurs et thèmes, puis certains thèmes réapparaissent dans l'activité parlementaire. Le corpus inspecté ne permet pas encore de mesurer la part propre du voyage dans cette réapparition.

## Ce que le corpus réfute ou borne

- `voyage financé = capture` : non établi ;
- `exposition = persuasion` : non établi ;
- `position congruente après voyage = effet du voyage` : non établi ;
- `ELNET France = mandataire de l'État israélien` : non établi dans ce run ;
- `absence de causalité démontrée = absence d'influence` : faux raccourci ; le canal d'accès et d'exposition est matériellement établi.

## Upgrade probatoire nécessaire

Le prochain niveau exige un dataset longitudinal : univers complet des participants 2017-2026, date et financeur de chaque voyage, positions et productions avant/après, groupe/commission, appartenance au groupe d'amitié, et contrôles non exposés comparables. Les voyages préérieurs au 7 octobre 2023 doivent être privilégiés pour limiter le confondant de guerre. Les trois traces spécifiques de mars 2023 — caucus Accords d'Abraham, financement de l'Autorité palestinienne, sécurité — doivent être recherchées comme outputs versionnés et datés, non comme simples similitudes discursives.
