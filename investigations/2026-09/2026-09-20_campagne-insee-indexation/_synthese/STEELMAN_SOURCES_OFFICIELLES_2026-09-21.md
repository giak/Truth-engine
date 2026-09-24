# STEELMAN : les sources officielles au moment du procès

> Phase 3 (Sublimator v38). Entrée : runs certifiés de la campagne + passages verbatim re-vérifiés en direct le 21/09/2026 sur les sources primales (re-fetch/re-lecture non circulaires, jamais les extraits des runs comme preuve).
> Objet : donner à l'article les meilleurs arguments DE LA DEFENSE, dans leur texte exact. La thèse de l'article (conventions légiférées, effets jamais consolidés) doit survivre à ces passages ou être amendée.
> Méthode de lecture : chaque passage est cité verbatim, avec URL exacte et mode d'accès observé le jour de la vérification. Les divergences constatées entre sources du corpus sont documentées en §2 (2H) et §4 (2C).

## 0. Sources et traçabilité

| ID | Source | URL | Accès observé 21/09/2026 | Preuve locale |
|----|--------|-----|--------------------------|---------------|
| S1 | Insee, « Le logement dans l'IPC » (page méthodo) | https://www.insee.fr/fr/statistiques/4126450 | curl 200, texte extrait | /tmp/steelman_src/insee_ipc.txt |
| S2 | Insee Analyses n° 109, avril 2025 (Chabaud, Olivia, Rubin, Blanchet) | https://www.insee.fr/fr/statistiques/ (page IA 109) | curl 200 | /tmp/steelman_src/ia109.txt |
| S3 | Article L161-25 du Code de la sécurité sociale | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031781092 | lecteur 200 | ce fichier |
| S4 | Article 17-1 de la loi n° 89-462 du 6 juillet 1989 | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028778231 | lecteur 200 (le 20/09 et le 21/09) | evidence/ des runs |
| S5 | DGCL, « DGF des communes » (collectivites-locales.gouv.fr) | URL du run certifié 20260920-2008 | curl 200 | /tmp/steelman_src/dgcl_dgf.html |
| S6 | Sénat, question orale n° 104 de M. Mizzon, publiée 17/10/2024, réponse 25/06/2025 | https://www.senat.fr/questions/base/2024/qSEQ24100104S.html | curl 200 (archive locale complète) | evidence/.../senat_metzing.txt |
| S7 | Fipeco, « Impact de l'inflation sur les finances publiques » | page inspectée (run 04-28) | curl 200 au run | evidence/.../fipeco_impact_inflation.txt |
| S8 | Geerolf (note), comparaison internationale IPC/loyers imputés | fiche inspectée (run 13-50) | curl 200 | /tmp/steelman_src/geerolf.txt |
| S9 | OFCE, « Après la censure » (Prévision automne 2024) | page inspectée (run 16-36) | curl 200 | /tmp/steelman_src/ofce.txt |
| S10 | economie.gouv.fr, « Ce qui change avec l'adoption du budget 2025 » (17/02/2025) | page ministérielle | curl 403, lecteur 200 | /tmp/steelman_src/eco_gouv.txt |
| S11 | ANIL, plafonnement de l'IRL (bouclier 2022-2024) | page inspectée (run 17-07) | curl 200 | evidence/ du run |
| S12 | Loi n° 51-711 du 7 juin 1951, art. 1er | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000022405540 | lecteur 200 au run, re-lecture 403 (note d'archivage honnête) | evidence/.../legifrance_loi1951_art1.txt |

Accès anormal documenté : la question écrite n° 1114 de l'Assemblée nationale (règles population DGF) était en 404 sur les deux suffixes à la date du 21/09 (URL enregistrée `.html` désormais morte, variante `.htm` vivante plus tôt dans la journée, sans snapshot Wayback). Son contenu reste corroboré par S5 et S6 ; à citer avec statut d'accès honnête ou via le Sénat.

## 1. Les passages, par convention

### 1.1 IRL : l'exclusion des loyers est une protection contre la circularité (S4 + preuves ANIL/Service-Public)

Texte légal (article 17-1 de la loi du 6 juillet 1989, version en vigueur, lecture Legifrance) : l'indice de référence des loyers est défini à partir de l'évolution des prix à la consommation **hors tabac et hors loyers**, moyenne des douze derniers indices mensuels publiés par l'Insee. Le texte administratif et l'ANIL énoncent la règle à l'identique (extrait du run 04-28) : « moyenne de l'évolution des prix à la consommation hors tabac et hors loyers, sur les 12 derniers mois ».

Argument de la défense : on n'indexe pas les loyers par les loyers. Une boucle fermée (loyers indexés sur les loyers) transformerait tout choc locatif en trajectoire auto-entretenue. L'exclusion est dans la loi, pas dans une zone grise de l'Insee. C'est la convention la plus défendable du corpus. Limite connue et assumée (runs 12-05/13-15) : la boucle n'est pas totalement fermée car l'IPC d'ensemble, qui indexe d'autres grandeurs, contient les loyers réels (poids 6 %).

### 1.2 Retraites : indexation sur les prix comme protection du pouvoir d'achat (S3 + Cour des comptes)

L161-25, verbatim : « La revalorisation annuelle des montants de prestations dont les dispositions renvoient au présent article est effectuée sur la base d'un coefficient égal à l'évolution de la moyenne annuelle des prix à la consommation, hors tabac, calculée sur les douze derniers indices mensuels de ces prix publiés par l'Institut national de la statistique et des études économiques l'avant-dernier mois qui précède la date de revalorisation des prestations concernées. Si ce coefficient est inférieur à un, il est porté à cette valeur. »

Argument de la défense : la clause « porté à cette valeur » garantit qu'un choc déflationniste ne baissera jamais une pension. Le choix des prix plutôt que des salaires garantit le pouvoir d'achat nominal des retraités : la Cour des comptes (rapport inspecté, PDF local) documente l'autre face : indexer sur les prix « fige » la place relative des retraités, qui ne partagent pas les gains de productivité. Le steelman est donc réel mais borné : la règle protège contre l'inflation, elle ne promet pas la participation à la croissance. L'IA 109 (S2) chiffre ce que coûterait l'autre choix : environ 3,7 points de PIB de dépenses de retraite en plus à long terme (variante salaires).

### 1.3 Barème de l'IR : annualité = acte démocratique, pas oubli technique (S9 + S10 + débat parlementaire)

Chaîne documentée par les runs (16-36) : gel 2023, PLF 2024 chiffrant le gel total à +6,1 Md€ (S7/Merci : « 6,1 milliards d'euros les recettes potentielles de l'impôt sur le revenu »), censure du 4 décembre 2024, loi spéciale adoptée AN 11/12 et Sénat 16/12 « et promulguée le 21 décembre 2024 » (S9, verbatim), gel de fait des revenus 2024, puis LF 2025 revalorisant le barème de 1,8 % (S10, verbatim : « revalorisé de 1,8 % pour chacune des tranches », premier seuil 11 497 euros), LF 2026 plein régime (0,9 %).

Argument de la défense : chaque année, le Parlement VOTE le maintien ou la revalorisation : c'est le principe d'annualité de l'impôt. L'indexation n'est pas un droit, c'est un choix budgétaire débattu, chiffré et arbitré chaque année (le PLF 2026 chiffrait même un gel partiel : environ +2 Md€, 200 000 foyers concernés, avant amendement). Le contre-argument (INV-E) reste : le chiffrage existe une année à la fois, aucune publication ne consolide l'effet cumulé des arbitrages successifs.

### 1.4 DGF : le champ population DGF compense des charges saisonnières réelles (S5 + S6)

DGCL, verbatim : « la variation de la dotation forfaitaire d'une commune d'une année sur l'autre s'explique par : L'évolution de la population dite "DGF" de la commune, qui ajoute à la population authentifiée par l'INSEE, le nombre de résidences secondaires ainsi que les places de caravanes conventionnées ».

Argument de la défense : la majoration n'est pas une erreur statistique, c'est une compensation législative de charges dues aux résidences secondaires (voirie, ordures, assainissement en saison). La même logique vaut pour la règle « 0,5 habitant par résidence secondaire » sous conditions. Le ministère répond publiquement au cas Metzing (S6, verbatim) : estimation 678 contre 791 au dénombrement municipal, écart supérieur à 15 %, « pénalise la commune, puisque le montant de la dotation globale de fonctionnement est essentiellement calculé sur la base de sa population » ; le rattrapage de collecte fonctionne (678 à 699 à 715 dans les séries OFGL).

### 1.5 IPC sans loyers imputés : l'Insee a traité la question et publie les alternatives (S1)

Deux passages verbatim, à citer ensemble (voir §4C pour l'attribution exacte des poids) :
- « Une façon de prendre en compte le logement des propriétaires dans l'inflation d'ensemble est de leur imputer un loyer correspondant à ce qu'ils payeraient tous les mois pour se loger s'ils étaient locataires, conformément à ce qui est fait par la comptabilité nationale. Cette imputation accroît par construction le poids du logement dans l'IPC (25,8 % contre 14,0 % en 2018). »
- « Le poids de l'ensemble des dépenses en logement dans cet indice "y compris investissement des propriétaires occupants" passe de 14,0 % à 20,9 %. »
- Et la conclusion de la page sur les variantes : leurs évolutions « diffèrent également peu » de l'IPC (figure 3).

Argument de la défense : le choix français (loyers réels, pas d'imputés) est documenté, argumenté, et l'Insee calcule publiquement l'indice alternatif : rien n'est caché. La critique Eurostat 2017 (champ « trop étroit », S8 : les États-Unis incluent 23,5 % d'imputés + 7,6 % de loyers réels, l'Allemagne 20,7 %) reste la meilleure attaque, mais la défense a des chiffres : sur la période documentée par l'Insee, l'alternative imputée évolue de façon similaire. Le débat est sur le champ, pas sur la compétence.

### 1.6 L'indexation comme question de recherche ouverte : l'Insee explore lui-même les règles alternatives (S2)

IA 109, avril 2025, verbatim (extrait) : « Par défaut, les retraites de base sont revalorisées selon l'évolution des prix plutôt que des salaires. Le retour de l'inflation a ainsi ouvert un débat sur les règles d'indexation des pensions. » Et : « L'indexation pleine sur les salaires ferait disparaître cette dépendance mais augmenterait très fortement la part des dépenses de retraite dans le PIB. Si on souhaite l'éviter, il faut que la référence aux salaires soit contrebalancée par des prises en compte directes, via des coefficients correcteurs, de l'évolution démographique ou de la cible de dépenses que l'on souhaite respecter. »

Usage dans l'article : la caisse de résonance scientifique existe, portée par l'institution elle-même (avec un signataire externe, Blanchet). L'Insee ne défend pas ses conventions comme des dogmes : il simule les contre-règles. C'est le meilleur argument contre la thèse d'un chiffre captif : un organisme captif ne publie pas le coût de ses propres conventions.

### 1.7 Le contrôle existe et s'exerce (S6 + S12 + avis CNIS/ASP des runs)

Loi de 1951, art. 1er : « La conception, la production et la diffusion des statistiques publiques sont effectuées en toute indépendance professionnelle », sous le contrôle d'une Autorité de la statistique publique de neuf membres dont le président est nommé par décret en Conseil des ministres. Cas réel d'exercice (S6, verbatim) : la CNERP « vient de recommander la réduction de ce décalage à deux ans, délai qui a été unanimement reconnu comme le meilleur équilibre entre fraîcheur et robustesse des données. Cette adaptation sera mise en oeuvre par l'Insee à la fin de l'année 2026. » Et la réplique du sénateur : « Ce gain d'une année profitera à tout le monde, sauf peut-être aux communes qui perdent des habitants et qui verront leur dotation baisser un an plus tôt. » (la boucle est bouclée : même la correction crée des gagnants et des perdants).

## 2. Contradiction détectée en cours d'extraction (2H) : la date de la loi spéciale

- Run certifié 20260921-16-36 (fait FCT) : loi spéciale « du 20 décembre 2024 ».
- S9, verbatim du jour : « promulguée le 21 décembre 2024 » (adoptée AN 11/12, Sénat 16/12).

Résolution pour l'article : citer le verbatim OFCE (21/12) ou vérifier le JORF avant publication ; ne jamais écrire « 20/12 » sans source. Aucun autre chiffre vedette n'est affecté (la censure du 4 décembre et la chronologie du barème restent corroborées par S9 et S10).

## 3. Ce que le steelman NE dit PAS (confrontation honnête)

| Convention | Justification officielle documentée | Ce qui reste sans réponse officielle |
|-----------|--------------------------------------|--------------------------------------|
| IRL | circularité évitée, texte légal clair (1.1) | aucun document ne chiffre la masse des loyers indexées par l'IRL ni l'effet d'un dixième de point (gap ACCESS, runs 04-28) |
| Retraites | pouvoir d'achat garanti, clause anti-déflation (1.2) | le choix prix vs salaires n'a jamais fait l'objet d'une motivation écrite consolidée ; le coût du contre-factuel (3,7 pts de PIB) n'est chiffré que dans une note d'analyse, pas dans un document d'arbitrage |
| Barème IR | annualité démocratique, chiffrage annuel (1.3) | aucune consolidation pluriannuelle des gels et revalorisations successifs (INV-E, runs 14-25 et 16-36) |
| DGF | compensation saisonnière légiférée (1.4) | l'effet d'un dixième de point d'IPC (ou d'une erreur de population) sur la masse des dotations n'est estimé nulle part ; seule une commune est chiffrée publiquement |
| IPC/imputés | alternative calculée et publiée (1.5) | la motivation du champ français n'est pas consolidée dans un document contradictoire public face à la lecture Eurostat |

Synthèse pour l'article : le steelman gagne sur l'origine et la nature des conventions (légiférées, argumentées, publiques, simulées par l'institution elle-même), il ne fournit rien sur la consolidation des effets dans la durée. C'est exactement l'espace que l'article occupe : « chiffrés ponctuellement, jamais consolidés ».

## 4. Contresens corrigés pendant l'extraction (2C)

- (4A, résolu au 20/09) I-Frap ne dit pas « 200 Md€ depuis 2000 » : la fiche porte sur environ 6 Md€ de trop-payé récent.
- (4B, résolu au 20/09) « Plafond IRL 4,25 % » : le 4,25 % est le SMIC de juin 2022 ; le bouclier IRL 3,5 % (lois 2022-1158 art. 12 et 2023-568 art. 2, S11) était exceptionnel, du T3 2022 au T1 2024.
- (4C, détecté le 21/09 en cours d'extraction) Le corpus (INV-C et 3 occurrences dans les livrables de synthèse) attribue 20,9 % aux « loyers imputés » : la source S1 attribue 25,8 % aux loyers imputés et 20,9 % à la variante « y compris investissement des propriétaires occupants ». Les 3 occurrences des synthèses ont été corrigées le jour même. L'argument steelman subsiste à l'identique (l'Insee publie une alternative avec imputés, poids 25,8 % ; les variantes évoluent de façon similaire à l'IPC).
- (4D, résolu le 21/09) USA/Allemagne : 23,5 % (imputés) + 7,6 % (réels) et 20,7 % confirmés dans S8 (point décimal, premier grep non concluant).
