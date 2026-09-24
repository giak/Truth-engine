NARRATIVE_START

# Cui bono du différentiel IRL — loyers effectifs : quantification annuelle 2019-2025

## Objet et filiation

Ce run est l'UPDATE du run `20260920-2154-irl-ecart-loyers-reels-elc`. Le parent avait établi que l'écart entre l'indice de référence des loyers (IRL) et les loyers effectivement constatés est bidirectionnel — protection du locataire en 2022-2023, rattrapage ensuite — et avait routé un gap nommé : extraire le sous-indice IPC « loyers effectifs » (Coicop 04.1) et convertir l'écart annuel en transfert locataires-bailleurs. Le présent run clôt ce gap : la série Insee BDM 001763530 (mensuelle, base 2015, ensemble des ménages, France) a été extraite via l'API SDMX, recombinée en moyennes annuelles, et confrontée à l'IRL trimestrielle (moyenne arithmétique des quatre glissements T/T-4 de l'année).

## Résultat central (FCT-001, ✦)

Glissements annuels des moyennes (IRL : moyenne des T/T-4 hexagone, tableau ANIL vérifié identique à la fiche Insee ; ELC : sous-indice 04.1) :

| Année | IRL | ELC (loyers effectifs) | IRL − ELC |
|---|---|---|---|
| 2022 | +3,27 % | +0,68 % | +2,59 pt |
| 2023 | +3,49 % | +2,13 % | +1,36 pt |
| 2024 | +2,75 % | +2,34 % | +0,41 pt |
| 2025 | +1,02 % | +2,32 % | −1,30 pt |

L'extraction ELC est corroborée par l'Insee lui-même (IR n°8 du 15/01/2026, inspecté) : « les prix des loyers effectivement payés par les locataires augmentent au même rythme qu'en 2024 (+2,3 % en moyenne) » — nos moyennes recombines donnent +2,34 % (2024) et +2,32 % (2025). En 2025, l'ELC dépasse l'IRL pour la première fois de la période couverte (FCT-004, ✧) : c'est la signature statistique du rattrapage des loyers en place vers les loyers de marché après le gel relatif de 2022.

## Trois référentiels, trois verdicts (FCT-003, ✧)

Le « cui bono » dépend du référentiel choisi, et c'est la raison pour laquelle le débat public est si instable sur ce point :

- **Bailleur en place vs sa propre formule d'indexation** : l'IRL appliquée aux loyers en place a progressé plus vite que les loyers effectivement constatés — cumul 2022-2025 (indice 2021 = base) : IRL +10,9 % contre ELC +7,7 %. Avantage cumulé au bailleur qui révisionne chaque année par l'IRL : environ +3,2 points sur quatre ans.
- **Locataire en place vs inflation générale** : l'IRL plafonnée a progressé moins vite que l'IPC hors tabac (cumul +10,9 % contre +13,2 %). Le locataire en place a été protégé contre le choc de prix de 2022-2023 (+3,27 % contre +5,2 % en 2022 ; +3,49 % contre +4,8 % en 2023).
- **Locataire entrant vs loyers de marché** : en 2022 les loyers de marché n'ont presque pas bougé (+0,68 %) alors que l'inflation générale explosait — le choc a été absorbé par l'énergie et l'alimentation, pas par les loyers. Puis les loyers en place ont rattrapé en 2024-2025 (+2,3 %/an) tandis que l'inflation retombait à +0,9 % (2025).

Aucun de ces trois verdicts n'en annule un autre : ils décrivent le même système depuis trois observatoires différents.

## Le plafond de 3,5 % a mordu l'indice, pas les loyers

La fiche Insee IRL (inspectée) documente elle-même le plafonnement (loi 2022-1158 art. 12, applicable T3 2022 – T1 2024) : la variation de l'IRL ne pouvait excéder 3,5 %. Or sa formule (IPC hors tabac et hors loyers, moyenne sur douze mois) aurait produit environ +5 % en 2022. Le plafond a donc réellement morde l'indice de révision. Mais la même année, les loyers effectivement constatés n'ont fait que +0,68 % : le plafond légal a protégé les locataires contre un choc que les loyers de marché n'ont, en substance, pas transmis. Le rattrapage s'est opéré en 2024-2025 via les révisions annuelles aux baux et les nouvelles locations — d'où la bascule de 2025 (ELC +2,32 % > IRL +1,02 %), sans que le législateur n'ait à intervenir à nouveau.

## Réponse à la question d'objet

Le transfert annuel induit par la convention IRL est quantifiable par année avec les seules séries publiques (CLM-1, SUPPORTED) et son signe n'est pas stable : gagnant bailleur en place sur 2022-2025 cumulé face à sa propre formule ; gagnant locataire en place face à l'inflation générale ; gagnant locataire entrant en 2022 ; gagnant bailleur face au marché en 2024-2025. La thèse d'un gagnant structurel permanent (CLM-2) est réfutée par les cumuls eux-mêmes : aucun des trois écarts ne garde le même signe sur la fenêtre étendue. Le « cui bono » est conjoncturel, et le mécanisme de rattrapage (révisions annuelles aux baux) réabsorbe en deux ans une protection conjoncturelle (CAU-001, SUPPORTED ; plafond légal 2022-2024 documenté par la source primaire).

## Vérification et réfutation

Le recoupement demandé (CTRL-001) est concluant : niveaux et variations de l'IRL T3 2025 (145,77, +0,87 %) et T4 2025 (145,78, +0,79 %) identiques à l'arrondi près entre le tableau ANIL et la fiche Insee. Les deux requêtes de réfutation formelles n'ont trouvé aucune contradiction : la série 001763530 n'est ni supprimée ni révisée de façon incompatible avec nos recombinaisons (dernière mise à jour 15/01/2026), et aucune source ne décrit un changement de convention IRL/ELC sur 2019-2025. Contre-lectures testées et rejetées : la fenêtre 2022-2023 seule (elle ignore le rattrapage 2024-2025 et le cumul) ; la confusion entre proxy tous baux et baux en révision (limite de typage, pas contradiction) ; la masse de base (95 Md€ tous locataires contre ~60 % pour le seul privé — bornes rappelées, signes inchangés).

## Limites typées

L'ELC est un proxy « tous baux » : elle inclut les nouvelles locations et les révisions, pas strictement les baux en révision à date. La masse de 95 Md€ (FCT-005, ✧ ; SDES, loyers réels des locataires 2024) couvre privé et social ; le parc IRL est le seul privé. L'IRL hexagone exclut par dérogation Outre-mer et Corse. Le délai moyen effectif de révision des baux n'est pas observé dans les sources publiques — gap typé ACCESS, non matériel pour le signe annuel.

## Ce que ce run apporte à la campagne

Le gap routé par le run IRL parent est clos par extraction primaire : la série « loyers effectifs » est désormais chiffrée année par année, recoupée par l'Insee lui-même, et le récit d'un avantage unidirectionnel — dans un sens ou dans l'autre — est démenti par les données. La chaîne causale (convention légale → révision annuelle → écart conjoncturel → transfert) est supportée de bout en bout, chaque maillon porté par une source inspectée.

NARRATIVE_END
