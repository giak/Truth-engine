# INVESTIGATION — VIGINUM : Service de Vigilance et Protection contre les Ingérences Numériques Étrangères

## §0 RÉSUMÉ EXÉCUTIF

VIGINUM (Service de vigilance et de protection contre les ingérences numériques étrangères) est un service technique et opérationnel de l'État français, créé le 13 juillet 2021 par décret n°2021-922, rattaché au Secrétaire général de la défense et de la sécurité nationale (SGDSN) sous l'autorité du Premier ministre. Sa mission officielle : détecter et caractériser les campagnes de manipulation de l'information provenant d'acteurs étrangers sur les plateformes numériques. Budget global estimé : ~7,3 M€ en 2024 (3,1 M€ fonctionnement + 4,2 M€ masse salariale). 65 agents en 2026. Dirigé par Marc-Antoine Brillant (depuis octobre 2023).

---

## §1 CRÉATION ET CADRE JURIDIQUE

### Origine
- **Décret de création** : n°2021-922 du 13 juillet 2021, publié au JO du 14/07/2021
- **Contexte** : annoncé par Stéphane Bouillon (SGDSN) début juin 2021, à quelques mois de la présidentielle 2022
- **Précurseur** : succède à la Task Force Honfleur (dirigée par Marc-Antoine Brillant), créée après l'affaire Samuel Paty (octobre 2020) pour enquêter sur la campagne de désinformation anti-française
- **Rattachement** : SGDSN (Secrétariat général de la défense et de la sécurité nationale), sous l'autorité directe du Premier ministre

### Cadre légal
- **Décret n°2021-922** (13 juillet 2021) : création du service, définition des missions
- **Décret n°2021-1587** (7 décembre 2021) : autorisation de collecter/traiter des données personnelles sur les plateformes > 5 millions de visiteurs uniques/mois, pris après avis de la CNIL
- **Loi du 22 décembre 2018** relative à la lutte contre la manipulation de l'information (dite "loi infox") : cadre préexistant
- **Loi SREN** (n°2024-449 du 21 mai 2024) : renforce le cadre de régulation numérique, désigne l'Arcom comme coordinateur des services numériques (DSA/DMA)
- **Décret du 12 février 2026** : fusionne les deux décrets de 2021, supprime le seuil de 5 millions de visiteurs, étend la collecte aux petites plateformes (Discord, etc.), allonge les durées de conservation des données, ajoute des missions R&D/IA

### Définition légale d'une ingérence numérique étrangère (4 critères cumulatifs)
1. Contenu manifestement inexact ou trompeur
2. Diffusion artificielle et automatisée
3. Implication directe ou indirecte d'un acteur étranger (étatique ou non étatique)
4. Atteinte potentielle aux intérêts fondamentaux de la Nation

---

## §2 BUDGET ET EFFECTIFS

### Budget
| Année | Budget fonctionnement | Masse salariale | Budget global | Source |
|-------|----------------------|-----------------|---------------|--------|
| 2021-2022 | 4 M€ (ligne dédiée logiciels cyber-analyse) | Inclus SGDSN | ~12 M€ (budget initial annoncé) | Les Echos, Intelligence Online |
| 2024 | 3,1 M€ | ~4,2 M€ | ~7,3 M€ | Sénat, amendement II-1835 |
| 2025 | Coupes budgétaires : -8 M€ combinés ANSSI/VIGINUM | - | - | La Lettre A, 22/01/2025 |

- Amendement sénatorial (2024-2025) : +1 M€ proposé par la commission d'enquête sur les influences étrangères (Rachid Temal, Dominique de Legge)
- Budget géré via le programme 129 "Coordination du travail du gouvernement"
- Pas de ligne budgétaire spécifique pour la masse salariale (incluse dans l'enveloppe SGDSN)

### Effectifs
- **2021** : 25 postes supplémentaires créés
- **2024** : 58 ETP prévus (dont ~40 affectés aux opérations)
- **2026** : 65 agents
- **Profil** : moyenne d'âge 32-33 ans, parité H/F (45%/55%), 2/3 contractuels de droit public
- **Compétences** : OSINT, data science, marketing digital, géopolitique, linguistique, cybersécurité

### Direction
| Période | Chef de service | Profil |
|---------|----------------|--------|
| Oct. 2021 - Juil. 2023 | Gabriel Ferriol | Magistrat Cour des comptes, ingénieur |
| Oct. 2023 - présent | Marc-Antoine Brillant | Lieutenant-colonel, Saint-Cyr, ESCP, ex-ANSSI, préfigurateur VIGINUM |

---

## §3 COMITÉ ÉTHIQUE ET SCIENTIFIQUE

### Composition initiale (arrêté du 5 octobre 2021)

**Présidente** : Béatrice Bourgeois-Machureau, Conseillère d'État

**Membres** (8 personnalités qualifiées) :
- **Pauline Talagrand** — Responsable du service d'investigation numérique, Agence France-Presse (AFP)
- **Julie Joly** — Directrice de L'Obs (hebdomadaire) ; précédemment identifiée comme directrice du CFJ (Centre de formation des journalistes)
- **Jean-Maurice Ripert** — Ambassadeur de France, ex-ambassadeur en Chine et en Russie, ex-conseiller de Michel Rocard et Lionel Jospin
- **Benoît Loutrel** — Membre du collège de l'Arcom, ex-Google
- **Aymeril Hoang** — Expert numérique, ex-directeur de cabinet de Mounir Mahjoubi (secrétariat d'État au numérique)
- **Marie-Christine Tarrare** — Procureure au tribunal de Besançon
- **Claude Kirchner** — Directeur de recherche émérite à l'INRIA

**Évolution** : Jean-Luc Sauron nommé président du comité en novembre 2023 (succédant à Béatrice Bourgeois-Machureau) — source : Contexte, 06/11/2023

### Missions du comité
- Suivre l'activité opérationnelle de VIGINUM
- Recevoir toute information relative aux missions du service
- Adresser des recommandations au chef de service
- Produire un rapport annuel public (remis au Premier ministre)
- Premier rapport : juillet 2021 – décembre 2022, publié le 26 juin 2023

### Critiques sur le comité
- Le rapport annuel est adressé au Premier ministre — interrogé sur l'impartialité en période électorale (Le Monde du Droit, 05/05/2022)
- Composition initiale incluant des proches du pouvoir (Aymeril Hoang, ex-cabinet de Mounir Mahjoubi)
- Julie Joly : lien avec le CFJ, institution critiquée pour son "politiquement correct" (Ojim.fr, 29/12/2021)

---

## §4 MISSIONS ET ACTIONS CONCRÈTES

### Missions officielles
1. Détecter et caractériser les opérations d'ingérence numérique étrangère (source ouverte)
2. Analyser les effets de ces opérations
3. Animer et coordonner la protection interministérielle
4. Fournir des informations au CSA/Arcom et à la Commission nationale de contrôle de campagne électorale
5. Contribuer aux travaux européens et internationaux
6. Protection spécifique des périodes électorales

### Rapports techniques publiés (dénominations publiques)

| Campagne | Date de publication | Description |
|----------|---------------------|-------------|
| **RRN / Doppelgänger** | Juin 2023 (MAJ 19/06/2023) | Campagne prorusse depuis sept. 2022, 355 domaines typosquattés (Le Monde, Le Figaro, 20 Minutes, Le Parisien), usurpation du site du ministère des Affaires étrangères, 160+ pages Facebook sponsorisées |
| **Portal Kombat** | Fév. 2024 (3 rapports) | Réseau de 193→224 "portails d'information" pro-russes, géré par la société TigerWeb (Crimée, Evgeniy Chevtchenko), ciblant presque tous les pays UE, pravda-fr.com pour la France |
| **Matriochka** | Juin 2024 | Campagne depuis sept. 2023 : faux contenus (reportages, graffitis, mèmes) diffusés coordonnés sur X dans les réponses de médias/personnalités dans 60+ pays, contenu d'abord publié sur Telegram russe |
| **UN-notorious BIG** | 2024 | Campagne prorusse (détails dans rapports publics) |
| **Olimpiya** | 2024 | Campagne de dénigrement des Jeux Olympiques de Paris 2024 |
| **s'engager-Ukraine** | 2024 | Faux site de recrutement pour l'armée de Terre |
| **Influence azerbaïdjanaise** | 2024 | Fiche technique sur les manœuvres informationnelles ciblant la France dans le contexte des émeutes en Nouvelle-Calédonie |

### Opérations de protection ciblées
- Élections présidentielle et législatives 2022
- Référendum Nouvelle-Calédonie (déc. 2021)
- Élections européennes et législatives anticipées 2024
- Jeux Olympiques et Paralympiques de Paris 2024
- Élections municipales 2026 (guide de sensibilisation publié en déc. 2025)

### Partenariats
- **Arcom** : convention-cadre signée le 4 juillet 2024 (Roch-Olivier Maistre + Marc-Antoine Brillant)
- **INRIA** : laboratoire commun
- **Éducation nationale** : diffusion de ressources (2026)
- **Académie de lutte contre la manipulation de l'information** : en création

### Évolution des pouvoirs (février 2026)
- Suppression du seuil de 5 millions de visiteurs uniques → collecte étendue aux petites plateformes (Discord, etc.)
- Extension de la durée de conservation des données
- Nouvelles missions : documentation des modes opératoires, recherche, information du public, éducation aux médias
- R&D : utilisation des données collectées pour entraîner des outils IA

---

## §5 LIENS AVEC LE POUVOIR

### Rattachement institutionnel
- **Autorité de tutelle** : SGDSN (Secrétaire général de la défense et de la sécurité nationale)
- **Secrétaire général actuel** : Stéphane Bouillon (directement responsable de VIGINUM)
- **Rattachement politique** : Premier ministre (Matignon)
- **Budget** : programme 129 "Coordination du travail du gouvernement"

### Interfaces avec les services de renseignement
- Le CLMI (Comité opérationnel de lutte contre les manipulations de l'information) inclut la DGSI et la Direction du renseignement militaire
- La commission Bronner (2021) — présidée par Gérald Bronner — a précédé la création de VIGINUM
- Liens possibles avec la DGSE et la DGSI pour des membres "opérationnels" du comité éthique (Intelligence Online)

### Proximités identifiées dans le comité éthique initial
- Aymeril Hoang : ex-directeur de cabinet de Mounir Mahjoubi (secrétaire d'État au numérique sous Macron)
- Jean-Maurice Ripert : diplomate carrière, conseiller de Michel Rocard et Lionel Jospin
- Benoît Loutrel : ex-Google, membre du collège de l'Arcom

---

## §6 CRITIQUES ET CONTROVERSES

### 6.1 Collecte de données personnelles — Avis de la CNIL
La CNIL a exprimé des réserves sur le décret de décembre 2021 :
- Collecte automatisée de données publiées sur les réseaux sociaux en "énorme quantité et à tout instant"
- Les données collectées sont susceptibles de révéler des informations sensibles : opinions politiques, convictions religieuses/philosophiques, état de santé, orientation sexuelle
- Collecte "hors du cadre légal encadrant les procédures judiciaires et de la législation relative aux techniques de renseignement"
- La CNIL relève que "la collecte automatisée d'un grand nombre de données [...] implique la collecte et le traitement de données non pertinentes au regard des finalités poursuivies"
- Source : délibération CNIL citée par Strategika (01/01/2023) et Jeune Nation (15/02/2024)

### 6.2 Accusations de censure — Février 2024 (Portal Kombat)
- Le 12 février 2024, suite à la publication du rapport Portal Kombat, un "grand nombre de canaux Telegram, sites internet ou comptes de réseaux sociaux ont été censurés en France"
- Le ministère des Affaires étrangères a justifié ces blocages en pointant la "découverte d'un vaste réseau de propagande" par VIGINUM
- Critique : les médias censurés étaient "pro-russes" mais aussi critiques du "narratif otanesque" et de la politique gouvernementale
- Sources : Jeune Nation (15/02/2024), Strategika (29/02/2024), ADNM (14/02/2024)

### 6.3 Flou des critères d'intervention
- "Contenu manifestement inexact ou trompeur" : qui juge ? Selon quels critères ?
- "Intérêts fondamentaux de la Nation" : définition large et interprétable
- Le décret ne précise pas explicitement qui met fin aux ingérences identifiées (Le Monde du Droit, 05/05/2022)
- Risque de "chasse à toute personne jugée arbitrairement dissidente" (Strategika, Jeune Nation)

### 6.4 Rapport au Premier ministre
- Le rapport annuel du comité éthique est remis au Premier ministre — impartialité interrogée en période électorale, alors que les élections sont expressément visées par le décret de création

### 6.5 Rapport VIGINUM sur Portal Kombat — travail sous-traité ?
- ADNM (14/02/2024) note que le rapport Portal Kombat utilise le framework MITRE DISARM
- Critique : VIGINUM n'aurait fait que "résumer un travail mené par une institution qui est un outil clair de l'état profond américain"
- Le rapport Portal Kombat cite des similarités avec les rapports Inforos, considérés par les USA comme administrés par le gouvernement russe

### 6.6 Coupes budgétaires 2025
- VIGINUM et l'ANSSI perdent 8 M€ combinés en 2025 (La Lettre A, 22/01/2025)
- Paradoxe : les missions s'étendent tandis que les moyens sont réduits

### 6.7 Extension des pouvoirs en 2026
- Décret du 12 février 2026 : collecte étendue aux petites plateformes, durées de conservation allongées, R&D IA
- Critique : surveillance élargie hors du cadre initial "électoral"

---

## §7 VERDICT — RÔLE DE CENSURE NUMÉRIQUE

### Faits établis
1. **VIGINUM n'a pas de pouvoir de censure direct** — il détecte, caractérise et publie des rapports. La décision de bloquer revient à l'État (MAE, Arcom, plateformes)
2. **Les blocages de février 2024** ont été justifiés par les rapports VIGINUM (Portal Kombat) — lien causal indirect mais réel
3. **La collecte de données** est massive et automatisée, avec les réserves de la CNIL sur les données sensibles
4. **Les critères d'ingérence** sont larges et interprétables, permettant une extension progressive du périmètre
5. **Le rattachement au Premier ministre** pose la question de l'indépendance politique, surtout en période électorale
6. **L'extension de 2026** (petites plateformes, IA, conservation allongée) élargit significativement le champ de surveillance

### Évaluation
VIGINUM est un outil de **surveillance informationnelle d'État** doté d'un cadre juridique formellement protecteur (comité éthique, rapports publics, source ouverte). Dans les faits :
- Son rôle est d'**identifier et attribuer** des campagnes d'influence étrangères
- Les **conséquences opérationnelles** de ses rapports incluent des blocages de contenus et de comptes
- Le **glissement progressif** des missions (électoral → permanent, grandes plateformes → toutes plateformes, détection → R&D IA) élargit le périmètre de surveillance
- La **proximité institutionnelle** avec l'exécutif (SGDSN, Premier ministre) et la composition du comité éthique initial interrogent sur l'indépendance réelle

### Conclusion
VIGINUM n'est pas formellement un organe de censure. Il est un organe de **détection et d'attribution** dont les productions servent de base à des décisions de censure prises par d'autres acteurs (État, plateformes). Le mécanisme est indirect mais fonctionnel : VIGINUM identifie → l'État agit → les plateformes exécutent. L'extension continue des pouvoirs (2026) et l'absence de contrôle juridictionnel a priori sur les qualifications d'"ingérence" constituent les principaux risques pour la liberté d'expression.

---

## §8 SOURCES

### Sources officielles
- Décret n°2021-922 du 13 juillet 2021 — Legifrance
- Décret n°2021-1587 du 7 décembre 2021 — Legifrance
- Décret du 12 février 2026 — JO
- Loi n°2024-449 du 21 mai 2024 (SREN) — Legifrance
- SGDSN : page VIGINUM — sgdsn.gouv.fr
- Rapport d'activité 2024 VIGINUM — sgdsn.gouv.fr
- Rapport comité éthique 2021-2022 — sgdsn.gouv.fr (26/06/2023)
- Convention Arcom-VIGINUM — arcom.fr (04/07/2024)
- Rapports techniques RRN, Portal Kombat, Matriochka — sgdsn.gouv.fr

### Presse et médias
- Les Echos : "Sept questions sur Viginum" (15/10/2021)
- Intelligence Online : "Le budget du SGDSN dope Viginum" (18/10/2021) ; "À l'approche des municipales" (09/01/2026)
- La Lettre A : "Coupes budgétaires : les renoncements de l'Anssi et de Viginum" (22/01/2025)
- Le Monde du Droit : "VIGINUM, ou comment l'État se dote d'un outil" (05/05/2022)
- Ojim.fr : "Contrôle de l'information : après la commission Bronner, Viginum" (29/12/2021)
- Contexte : "Gabriel Ferriol quitte la tête de Viginum" (31/07/2023) ; "Jean-Luc Sauron nommé président du comité" (06/11/2023)
- RFI : "Viginum se muscle face à la recrudescence des ingérences" (08/03/2024)
- Next.ink : "VIGINUM doté de moyens renforcés" (12/02/2026)
- Ministère des Armées : "Viginum : le rempart contre les ingérences" (17/03/2025)
- IH2EF : Grand entretien VIGINUM — ih2ef.gouv.fr

### Sources critiques
- Strategika : "Viginum : le plan de l'État français pour le flicage de la dissidence" (01/01/2023) ; "Vaste opération de censure sur Telegram" (29/02/2024)
- Jeune Nation : "Vaste opération de censure sur Telegram en France" (15/02/2024)
- ADNM : "Complexe Industriel de la Censure : l'interview de Poutine, et le scandale du rapport VIGINUM" (14/02/2024)

### Données budgétaires
- Sénat : Amendement II-1835 (2024-2025) — senat.fr
- Wikidata : Q107398134 — budget 12 M€ / 7,2 M€
- Assemblée nationale : Annexe 13 PLF 2026 — assemblee-nationale.fr
