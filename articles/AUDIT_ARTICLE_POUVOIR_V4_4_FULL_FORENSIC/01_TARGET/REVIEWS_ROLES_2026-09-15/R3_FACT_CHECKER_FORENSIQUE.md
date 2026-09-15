# Vérification forensique des faits – Rôle R3

## Vérification des faits

### 1. BNP Paribas
- Source: `bnp_bnpp_jina.txt`
- Claim: 8,97 milliards de dollars, plaider-coupable du 30 juin 2014, interdiction temporaire d'un an de compensation en dollars pour les activités pétrole et gaz.
- Statut: **CONFIRMÉ**
- Phrase exacte de la source: 
  - Montant: « BNP Paribas accepte également de payer un total de 8,97 milliards de dollars (6,6 milliards d'euros). »
  - Plaider-coupable: « Dans le cadre de cet accord, BNP Paribas SA reconnaît sa responsabilité (« guilty plea ») pour avoir enfreint certaines lois et réglementations des Etats-Unis. »
  - Suspension: « BNP Paribas accepte une suspension temporaire, pour une durée d’un an à compter du 1er janvier 2015, de certaines opérations directes de compensation en dollars US, portant principalement sur le périmètre de l’activité de financement du négoce international de matières premières, pour la partie pétrole et gaz. »

### 2. Alstom
- Source: `alstom_doj_jina.txt` (et `alstom_doj.html`)
- Claim: 772,29 M$ de pénalité, plaider-coupable du 22 décembre 2014.
- Statut: **NON VÉRIFIABLE**
- Justification: Le fichier source est présent mais ne contient aucun contenu substantiel (seulement une redirection vers la page du DOJ). Aucune mention du montant ni de la date.

### 3. TotalEnergies / South Pars 11
- Sources: 
  - `total_southpars.txt` pour le coût total et la date d'annonce
  - `total_conversation.txt` pour la répartition des actionnaires
  - `total_cnbc.txt` pour la dépendance au refinancement en dollars
- Claim: 
  - 4,8 milliards de dollars de coût total, annonce du 16 mai 2018
  - 40 % d'investisseurs nord-américains contre 25,3 % d'actionnaires français
  - Question de la dépendance au refinancement en dollars
- Statut: **DIVERGENT**
- Détails:
  - Le premier chiffre (4,8 milliards de dollars) n'apparaît pas dans `total_southpars.txt`. Ce fichier indique plutôt que le contrat a été exécuté le 4 juillet 2017 (« On 4 July 2017, Total, together with the other partner Petrochina, executed the contract related to the South Pars 11 (SP11) project ») et ne mentionne pas le montant de 4,8 milliards de dollars.
  - Le deuxième chiffre est confirmé par `total_conversation.txt` : « Les investisseurs des États-Unis détiennent déjà près de [40% du capital de TotalEnergies, en 2024, contre 25,3% pour les actionnaires français] ».
  - Le troisième point (dépendance au refinancement en dollars) n'est pas abordé dans `total_cnbc.txt` ; l'article traite des sanctions américaines sur l'Iran et de l'utilisation du dollar par l'Inde, mais pas de la dépendance de Total au financement en dollars.

### 4. Cloud européen
- Sources: `synergy_cloud.txt`, `synergy_cloud2.txt`, `synergy_cloud3.txt` (et `synergy_archive.txt`)
- Claim: « 70 % du marché européen du cloud d'infrastructure détenu par trois fournisseurs américains »
- Statut: **NON VÉRIFIABLE**
- Justification: Les trois fichiers principaux renvoient une erreur 404 (Page Not Found). Le fichier `synergy_archive.txt` contient un message d'erreur concernant un blocage d'accès à web.archive.org. Aucun des fichiers ne fournit la partie de marché des fournisseurs américains.

### 5. Health Data Hub
- Sources: `cnil_healthdata.txt`, `cuggia_healthdata.txt`
- Claim: « plus de 66 millions de personnes » couvertes par l'assurance maladie
- Statut: **CONFIRMÉ**
- Phrase exacte de la source (extrait de `cuggia_healthdata.txt`) : « SNDS covers 98.8% of the French population, more than 66 million persons, making it possibly the world’s largest continuous homogeneous claim database ». Le SNDS (Système National des Données de Santé) est basé sur les données de l'assurance maladie, comme confirmé par la référence [24] dans le même document : « Value of a national administrative database to guide public decisions: From the système national d’information interrégimes de l’Assurance Maladie (SNIIRAM) to the système national des données de santé (SNDS) in France ».

### 6. Contrôle des investissements étrangers
- Sources: `tresor_ief.txt` (rapport annuel), `tresor_communique.txt` (communiqué n° 815)
- Claim: 392 dossiers en 2024 contre 309 en 2023 ; 337 décisions dont 182 dans le champ ; 54 % des autorisations conditionnées ; six refus en trois ans
- Statut: **NON VÉRIFIABLE**
- Justification: Les deux fichiers sont des erreurs de récupération (`tresor_ief.txt` présente une erreur de connexion refusée, `tresor_communique.txt` une erreur 404 Not Found). Aucun contenu exploitable n'est disponible.

### 7. HATVP
- Sources: `hatvp_2024.txt` (et `hatvp_bilan.pdf`, rapport Cour des comptes non disponible)
- Claim: 751 projets soumis pour avis en 2024 ; 7 % d'avis d'incompatibilité en 2023 ; moins de dix par ministère sur 2020-2023 ; 77 % de compatibilités avec réserves
- Statut: **DIVERGENT**
- Détails:
  - Le premier chiffre est confirmé par `hatvp_2024.txt` : « La Haute Autorité a été saisie de 751 projets de mobilité, contre 418 en 2023 ».
  - Le deuxième chiffre (7 % d'avis d'incompatibilité en 2023) ne figure pas dans `hatvp_2024.txt` ; seules les données pour 2024 sont présentes (4,5 % d'avis d'incompatibilité).
  - Le troisième chiffre (moins de dix par ministère sur 2020-2023) n'est pas présent dans les sources disponibles.
  - Le quatrième chiffre (77 % de compatibilités avec réserves) diverge avec la source : `hatvp_2024.txt` indique que « 74,3 % [des avis] étaient assortis de réserves ».

## Affirmations du corps sans renvoi ou dont le renvoi ne porte pas la phrase

Liste des affirmations du corps (points 1 à 7) pour lesquelles le renvoi cité ne contient pas la phrase exacte revendiquée :

- Point 2 (Alstom) : le renvoi (`alstom_doj_jina.txt`/`alstom_doj.html`) ne contient aucune mention du montant 772,29 M$ ni de la date du 22 décembre 2014.
- Point 3 (TotalEnergies / South Pars 11) : 
  - Le renvoi `total_southpars.txt` ne contient pas la phrase « 4,8 milliards de dollars de coût total, annonce du 16 mai 2018 ».
  - Le renvoi `total_cnbc.txt` ne contient pas de mention de la « dépendance au refinancement en dollars » de Total.
- Point 4 (Cloud européen) : les renvois (`synergy_cloud.txt`, `synergy_cloud2.txt`, `synergy_cloud3.txt`) sont muets (erreurs 404) et ne contiennent aucune donnée sur la part de marché des fournisseurs américains.
- Point 6 (Contrôle des investissements étrangers) : les renvois (`tresor_ief.txt`, `tresor_communique.txt`) sont muets (erreurs de récupération) et ne contiennent aucun des chiffres avancés.
- Point 7 (HATVP) :
  - Le renvoi `hatvp_2024.txt` ne fournit pas le pourcentage d'avis d'incompatibilité pour 2023 (données manquantes).
  - Le renvoi `hatvp_2024.txt` ne fournit pas de donnée sur le nombre de projets par ministère sur 2020-2023.
  - Le renvoi `hatvp_2024.txt` indique 74,3 % d'avis assortis de réserves, divergeant du chiffre revendiqué de 77 %.

Les points 1 et 5 sont confirmés et ne figurent donc pas dans cette liste.