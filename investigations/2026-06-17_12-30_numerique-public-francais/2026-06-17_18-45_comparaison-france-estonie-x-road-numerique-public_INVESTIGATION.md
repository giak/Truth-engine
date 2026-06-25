# INVESTIGATION — France vs Estonie : Architecture, Coûts et Sécurité du Numérique Public

> **Date :** 2026-06-17
> **Type :** Analyse comparée
> **Périmètre :** Architecture x-Road, budgets IT publics, sécurité, adoption citoyenne, gouvernance
> **Sources :** Eurostat, Commission européenne (Digital Decade), Riigikontroll (Cour des comptes estonienne), ERR, RIA, ANSSI, DINUM, INSEE, OECD, e-Estonia, NIIS

---

## §0 SYNOPSIS

L'Estonie (1,37 M d'habitants, PIB ~43 Md€) et la France (68 M d'habitants, PIB ~2 800 Md€) représentent deux modèles radicalement différents d'administration numérique. L'Estonie a bâti un écosystème fédéré autour de x-Road (X-tee) depuis 2001, avec 100 % des services publics disponibles en ligne depuis décembre 2024. La France, avec un budget IT public 15 à 20 fois supérieur en valeur absolue mais 5 à 8 fois inférieur par habitant, peine à unifier son système d'information étatique, marqué par une architecture ministérielle en silos, des grands projets en dérive (6,5 % de dépassement budgétaire moyen, 21 % de retard) et un pilotage encore incomplet de la DSI de l'État.

Cette investigation compare systématiquement les deux modèles sur 12 dimensions clés : budget, architecture, sécurité, adoption, coûts, externalisation, gouvernance, souveraineté, et tire les leçons pour la France.

---

## §1 L'ARCHITECTURE ESTONIENNE

### 1.1 x-Road : principe et coûts

x-Road est une couche d'échange de données distribuée, open source (licence MIT), développée depuis 2001. Son principe fondamental est l'absence de hub central : les données restent dans les systèmes source, et x-Road assure l'interopérabilité via des serveurs de sécurité standardisés.

**Chiffres clés (2025) :**
- Plus de 2 611 jours de fonctionnement ininterrompu (plus de 7 ans)
- Plus de 17,9 milliards de transactions cumulées, dont ~2,4 milliards par an
- ~295 millions de requêtes par mois
- Seulement 3 % des requêtes initiées par un citoyen (97 % en machine-to-machine)
- 1 300+ systèmes d'information interconnectés
- 450+ institutions et entreprises connectées directement
- 52 000 organisations comme utilisateurs indirects
- Fédération transfrontalière avec la Finlande (2018)

**Coûts de développement et maintenance :**
- x-Road a été développé initialement par Cybernetica pour le gouvernement estonien (2001). Le coût exact de développement initial n'est pas publiquement décomposé, mais les estimations de la littérature le situent entre 5 et 10 M€ cumulés sur les premières versions.
- Depuis 2017, le développement est géré par le NIIS (Nordic Institute for Interoperability Solutions), financé par les contributions de l'Estonie, de la Finlande et de l'Islande. Le budget annuel de NIIS est d'environ 1,5-2 M€ pour le développement cœur.
- Le coût total de possession (TCO) pour un pays adoptant x-Road est estimé par les outils NIIS à 0,5-2 M€ par an selon la taille du déploiement.
- Pour les organisations membres, le coût d'un serveur de sécurité est d'environ 5 000-15 000 € par an (maintenance + hébergement).

**Gains :**
- Économie estimée de 1 345 à 2 589 années de travail par an pour l'administration et les citoyens
- Chaque requête machine-to-machine économise ~10-15 minutes de travail manuel
- 1,48 million d'heures de travail économisées par mois
- La signature numérique aurait permis d'économiser environ 2 % du PIB estonien depuis son déploiement
- Coût d'un vote électronique : 2,30 € contre 20,40 € pour un vote physique (facteur ~9)

### 1.2 Services déployés

Depuis décembre 2024, 100 % des services publics estoniens sont disponibles en ligne, y compris des services complexes comme le divorce (53 % des demandes déposées en ligne dès les premiers mois). Services emblématiques :

| Service | Adoption | Note |
|---------|----------|------|
| Déclaration fiscale | ~95 % en ligne | Temps moyen : 3 minutes |
| Vote électronique | 44 % des votes | Depuis 2005, 10+ scrutins |
| Prescription médicale | 99 % numérique | Interopérable pharmacies |
| Naissance | 85 % en ligne | Déclaration automatisée |
| Mariage | 56 % en ligne | Dépôt numérique |
| Casier judiciaire | 100 % en ligne | Réponse instantanée |
| Authentification eID | 91 % des 16-74 ans | Utilisation dans les 12 mois |

L'identifiant unique (isikukood, code personnel à 11 chiffres) permet le chaînage des données via x-Road sans stockage centralisé. Le principe constitutionnel « une seule fois » (once-only) interdit à l'administration de demander deux fois la même information.

### 1.3 Budget et organisation

**Structure IT publique estonienne (2025) :**

L'Estonie dispose de 7 agences IT centralisées, dont le budget combiné atteint 265,5 M€ en 2025 (contre 66 M€ il y a 10 ans, soit un quadruplement). L'effectif total est de 1 765 employés.

| Agence | Budget 2025 | Employés | Rôle |
|--------|-------------|----------|------|
| **RIA** (Info System Authority) | 49 M€ | 307 | Plateformes centrales, cybersécurité, eesti.ee, x-tee |
| **RIT** (State IT Center) | 46,5 M€ | 226 | Infrastructures, postes de travail, serveurs, achats IT |
| **RMIT** (Min. Finances IT) | 30,4 M€ | 197 | SI financier de l'État |
| **SMIT** (Min. Intérieur IT) | 59 M€ | — | SI sécurité intérieure |
| **RIK** (Registres & SI) | 15,3 M€ | 274 | Centres de registres, développement |
| **TEHIK** (Santé) | — | — | SI santé et bien-être |
| **KEMIT** (Environnement) | 13,3 M€ | — | SI climat/environnement |

**Évolution budgétaire 2019-2024 :**
- IT investments : 45 M€ → 83 M€ (+84 %)
- IT administrative costs : 38 M€ → 77 M€ (+103 %)
- IT staff costs : 40 M€ → 97 M€ (+143 %)
- **Total IT public : 123 M€ → 257 M€ (+109 %)**

Budget IT total par habitant (2024) : **~188 €/hab** (257 M€ / 1,37 M hab).
Budget des agences IT centrales par habitant (2025) : **~194 €/hab** (265,5 M€ / 1,37 M hab).

La forte hausse est attribuée à :
- Une enveloppe exceptionnelle de 30 M€ pour la cybersécurité (2021)
- La création du RIT (fusion d'agences, 2021)
- La hausse des coûts matériels et logiciels
- La guerre en Ukraine et l'augmentation des menaces cyber

**Réforme en cours (2026) :** Le gouvernement a annoncé la fusion de RIT et RIA au 1er janvier 2027, puis l'intégration de RIKS d'ici juillet 2029, pour créer un « bouclier cyber unique » et économiser ~50 postes sur 3 ans.

---

## §2 COMPARAISON FRANCE-ESTONIE

### Tableau systématique

| Dimension | Estonie | France | Ratio / Écart |
|-----------|---------|--------|---------------|
| **Population** | 1,37 M | 68 M | France 50× plus peuplée |
| **PIB** | ~43 Md€ | ~2 800 Md€ | France 65× |
| **Dépenses IT publiques (total)** | ~257 M€ (2024) | ~4-5 Md€ (est. 2024) | France 16-19× |
| **Dépenses IT / habitant** | ~188 €/hab | ~60-74 €/hab | **Estonie 2,5-3× plus** |
| **Dépenses IT / PIB** | ~0,60 % | ~0,16-0,18 % | **Estonie 3,3-3,7× plus** |
| **Dépenses IT centrales / habitant** | ~194 €/hab (2025) | ~66 €/hab (4,5 Md€ / 68 M) | **Estonie 2,9× plus** |
| **Agents IT publics** | 1 765 | ~15 000-20 000 (est.) | ~10-11× (pour 50× pop) |
| **Architecture** | Distribuée (x-Road) | Ministérielle en silos | Modèle opposé |
| **Interopérabilité** | Standard unique x-Road | Aucun standard transverse | Écart structurant |
| **Services publics en ligne** | 100 % (2024) | ~75-80 % (est. 2024) | Écart significatif |
| **eID utilisée (12 mois)** | 91 % | 84 % | Comparable |
| **e-Gov utilisé (12 mois)** | 96 % | 91 % | Comparable |
| **Satisfaction usagers** | 82 % | ~60-65 % (est. OCDE) | Écart notable |
| **Cyber incidents (2024)** | Données non comparables directement | 4 386 événements, 1 361 incidents | France 100×+ population |
| **Budget ANSSI / équivalent** | RIA : 49 M€ (cyber + infra) | ANSSI : 29,6 M€ (hors masse salariale) | RIA 1,65× pour 1/50 pop |
| **Taux d'incidents cyber / hab** | Non disponible | ~0,02 / hab | Pas de données estoniennes |
| **Externalisation** | Principalement régie (agences internes) | Forte externalisation (DGFiP, Éducation : contrats Microsoft, etc.) | **Modèle opposé** |
| **Direction centrale du numérique** | RIA (unique) | DINUM (interministérielle, faible pouvoir) | **RIA a des pouvoirs exécutifs** |
| **Grands projets >9 M€** | ~5-10 (est.) | 45 suivis par DINUM | France 5-9× plus |
| **Indépendance technologique** | Open source (x-Road, eID) | Dépendance Microsoft, AWS, etc. | **Écart critique** |
| **Temps de déclaration fiscale** | ~3 minutes | ~15-30 minutes (pré-rempli mais contrôles) | Facteur 5-10 |
| **Gain productivité admin.** | 1 345-2 589 années travail/an | Non mesuré | Pas d'équivalent français |

### Analyse des écarts structurants

**1. Budget par habitant :** La France investit 2,5 à 3 fois moins par habitant que l'Estonie dans son IT public. En proportion du PIB, l'écart est de 1 à 3,7. Cela s'explique notamment par le fait que l'Estonie a construit son administration numérique *from scratch* après 1991, sans legacy, tandis que la France porte des décennies de systèmes d'information hétérogènes.

**2. Architecture :** L'Estonie a fait le choix d'une architecture distribuée (x-Road) où les données restent dans les systèmes source et sont échangées via une couche standardisée. La France a une architecture ministérielle où chaque ministère possède son propre SI, sans couche d'interopérabilité obligatoire. Le «  programme d'urbanisation » de la DINUM n'a pas l'autorité technique du modèle estonien.

**3. Pilotage :** RIA est une agence exécutive avec pouvoir de sanction et de supervision sur les SI des ministères et des opérateurs. La DINUM en France a un rôle de conseil et de conformité (avis sur les projets >9 M€), mais la Cour des comptes note qu'elle « peine à prendre le rôle effectif de DSI de l'État ».

**4. Grands projets :** La France compte 45 grands projets numériques de plus de 9 M€, avec un dépassement budgétaire moyen de 6,5 % et un retard de 21 %. Le projet PILAT de la DGFiP a vu son coût passer de 36 M€ à 123,6 M€ (+243 %) et sa durée de 48 à 91 mois. La facturation électronique atteint 258,7 M€ après 8 ans de développement.

---

## §3 CE QUE LA FRANCE POURRAIT APPRENDRE

### 1. Architecture fédérée plutôt que hub central

L'Estonie prouve qu'une couche d'échange de données standardisée et distribuée élimine le besoin d'intégrations point-à-point coûteuses. La France pourrait s'inspirer de x-Road pour créer une couche d'interopérabilité obligatoire entre tous les SI de l'État, au lieu de multiplier les interfaces bilatérales.

### 2. Principe « une seule fois » (once-only)

L'Estonie a constitutionnalisé l'interdiction de demander deux fois la même information au citoyen. La France a adopté ce principe dans le code des relations entre le public et l'administration (CRPA) mais son application reste lacunaire faute de couche d'échange technique universelle.

### 3. Agence exécutive de pilotage

RIA combine les rôles de DSI de l'État, d'autorité de cybersécurité, et d'opérateur d'infrastructure. La France a séparé ces fonctions entre DINUM, ANSSI, et les DSI ministérielles, créant une complexité de gouvernance que l'Estonie a évitée.

### 4. Standardisation des identités

Le code personnel unique estonien (isikukood) permet le chaînage des données sans duplication. La France bute sur FranceConnect+ et l'identité numérique (T6/T7) sans avoir résolu le chaînage inter-administrations.

### 5. Open source comme levier de souveraineté

x-Road est open source (MIT), utilisé dans 20+ pays. La France, malgré la doctrine « cloud au centre » et le mouvement vers le logiciel libre, reste massivement dépendante de fournisseurs non-européens (Microsoft pour l'Éducation nationale : 176 M€, contrats cloud AWS/Azure).

### 6. Mesure systématique des gains

L'Estonie mesure l'impact de son système en années de travail économisées, en transactions traitées, en temps par service. La France ne dispose pas d'indicateurs comparables pour le SI de l'État dans son ensemble.

---

## §4 LIMITES ET RISQUES DU MODÈLE ESTONIEN

### 1. Taille et transposabilité

L'Estonie est un petit pays (1,37 M hab.) sans legacy administratif pré-numérique majeur (indépendance en 1991). La transposition à une échelle 50 fois plus grande comme la France n'est pas triviale : la complexité d'un système fédéré croît avec le nombre de nœuds.

### 2. Dépendance à l'eID unique

La vulnérabilité ROCA de 2017 (failles Infineon sur 800 000 cartes d'identité, soit ~58 % des cartes actives) a exposé le risque d'un système trop centralisé autour d'un seul identifiant cryptographique. L'Estonie a mitigé via la mise à jour à distance vers ECC, mais le risque systémique demeure.

### 3. Single point of failure de l'autorité de certification

Le certificat d'authentification estonien (SK ID Solutions) est un quasi-monopole privé. Les experts pointent l'absence d'alternative publique comme un risque.

### 4. Vie privée et surveillance

Bien que l'architecture soit distribuée, le chaînage des données via l'isikukood crée un risque théorique de « profiling » global. L'Estonie a mis en place un système de logs consultables par le citoyen (log system), mais la confiance reste un enjeu.

### 5. Coûts croissants

Le quadruplement du budget des agences IT en 10 ans (66 M€ → 265,5 M€) interroge sur la soutenabilité du modèle. La Cour des comptes estonienne (Riigikontroll) note que même cette hausse est inférieure aux besoins estimés par les ministères.

### 6. Résilience cyber

Malgré l'architecture distribuée, l'Estonie reste une cible privilégiée des attaques russes depuis les cyberattaques de 2007. La guerre en Ukraine a accentué la pression. La fusion RIA-RIT répond à ce besoin de « bouclier unique », mais la concentration des compétences crée aussi un point de défaillance unique.

### 7. Pas de service de remplacement physique

En cas d'indisponibilité majeure (cyberattaque, panne électrique), le modèle estonien n'a pas de « plan B » physique pour de nombreux services qui n'existent qu'en ligne. Le divorce numérique en est un exemple.

### 8. Limites de la mesure d'impact

L'estimation des « années de travail économisées » (1 345 à 2 589) est basée sur des hypothèses fortes (15 minutes économisées par requête). La propre étude d'impact du gouvernement estonien (IBS, 2022) reconnaît que ces calculs comportent une « marge d'erreur élevée » et que les données de coûts par transaction ne sont pas collectées systématiquement.

---

## §5 SYNTHÈSE

### Faits

| ID | Fait | Source |
|----|------|--------|
| F-EST-001 | L'Estonie a 100 % de ses services publics disponibles en ligne depuis décembre 2024 | e-Estonia, 2025 |
| F-EST-002 | x-Road traite ~295 M requêtes/mois, 97 % en machine-to-machine | e-Estonia, Nortal, 2025 |
| F-EST-003 | L'Estonie économise 1 345 à 2 589 années de travail/an via x-Road | e-Estonia, Cybernetica, 2018-2025 |
| F-EST-004 | Le budget IT public estonien a doublé en 6 ans (123 M€ → 257 M€, 2019-2024) | Riigikontroll, 2025 |
| F-EST-005 | Le budget des agences IT centrales a quadruplé en 10 ans (66 M€ → 265,5 M€) | ERR, 2025 |
| F-EST-006 | L'Estonie investit ~188 €/hab/an dans l'IT public, la France ~60-74 €/hab | Calculs investigateur |
| F-EST-007 | L'Estonie consacre ~0,60 % de son PIB à l'IT public, la France ~0,16-0,18 % | Calculs investigateur |
| F-EST-008 | 91 % des Estoniens ont utilisé l'eID dans les 12 mois (vs 84 % France) | Eurostat, 2025 |
| F-EST-009 | 96 % des Estoniens ont utilisé l'e-gov dans les 12 mois (vs 91 % France) | Eurostat, 2025 |
| F-EST-010 | 82 % de satisfaction sur les services publics (vs 10 points au-dessus moyenne EU) | OECD, 2025 |
| F-EST-011 | 800 000 cartes eID affectées par la vulnérabilité ROCA en 2017 (58 % du parc) | RIA, Schneier, 2017 |
| F-EST-012 | Migration réussie de RSA vers ECC à distance en 2 semaines (nov. 2017) | Cybernetica, 2017 |
| F-EST-013 | RIA combine cybersécurité, infra IT et supervision des SI de l'État (budget 49 M€, 307 agents) | RIA, 2025-2026 |
| F-EST-014 | Fusion RIA-RIT-RIKS annoncée pour créer un « bouclier cyber unique » d'ici 2029 | ERR, 2026 |
| F-EST-015 | x-Road est open source (MIT), géré par NIIS (Estonie + Finlande + Islande) | NIIS, 2025 |
| F-EST-016 | 45 grands projets numériques >9 M€ suivis en France, dépassement moyen 6,5 %, retard 21 % | DINUM Panorama, 2025 |
| F-EST-017 | Budget IT France estimé à 4-5 Md€ (2024), soit ~0,9 % du budget général de l'État | IT for Business, 2025 |
| F-EST-018 | ANSSI : 656 agents, budget 29,6 M€ (hors masse salariale), 4 386 événements de sécurité traités en 2024 | ANSSI rapport 2024 |
| F-EST-019 | Projet PILAT DGFiP : coût passé de 36 M€ à 123,6 M€ (+243 %), durée 48 à 91 mois | Assemblée nationale, 2024 |
| F-EST-020 | L'ANSSI note la forte dépendance française aux équipements de sécurité non-européens | ANSSI Panorama 2024 |
| F-EST-021 | Signature numérique estimée à 2 % du PIB d'économie potentielle | e-Estonia, 2020 |
| F-EST-022 | Vote électronique : 2,30 € vs 20,40 € physique (facteur 9) | e-Estonia, 2017 |
| F-EST-023 | x-Road : 2 611 jours sans interruption opérationnelle | e-Estonia / Nortal, 2025 |
| F-EST-024 | L'Estonie a 7 agences IT centrales (1 765 employés), en cours de fusion vers RIA unifiée | ERR, 2025-2026 |
| F-EST-025 | La Cour des comptes estonienne note que le ministère de la Justice et du Numérique n'a PAS de vue centrale des dépenses IT — même constat que la France | Riigikontroll, 2025 |
| F-EST-026 | Le nombre d'employés IT publics estoniens a plus que doublé (722 → 1 765) en 10 ans | ERR, 2025 |
| F-EST-027 | Budget ANSSI (hors masse salariale) : 29,6 M€ (2024), en hausse de 15 % | ANSSI, 2025 |
| F-EST-028 | 280 visas de sécurité, 196 qualifications et 94 certifications délivrés par l'ANSSI en 2024 | ANSSI, 2025 |
| F-EST-029 | 144 attaques par rançongiciel traitées par l'ANSSI en 2024 (niveau comparable à 2023) | ANSSI, 2025 |
| F-EST-030 | La DINUM « peine à prendre le rôle effectif de DSI de l'État », selon la Cour des comptes | IT for Business / Cour des comptes |

### Loups — signaux faibles

- **L-EST-001** : L'Estonie n'a pas de « plan B » physique pour ses services 100 % numériques en cas de panne majeure.
- **L-EST-002** : Le quadruplement du budget IT en 10 ans interroge la soutenabilité du modèle quand la pression budgétaire s'accroît (réduction de 10 % des dépenses publiques annoncée).
- **L-EST-003** : La fusion RIA-RIT-RIKS concentre les compétences critiques dans une agence unique — résilience ou fragilité ?
- **L-EST-004** : Le modèle estonien repose sur un identifiant unique (isikukood) qui n'existe pas en France — la transposition nécessiterait une réforme profonde du système d'état civil.
- **L-EST-005** : Les économies d'échelle déclarées par l'Estonie (années de travail, % PIB) sont basées sur des extrapolations non vérifiées par un audit indépendant.
- **L-EST-006** : L'Estonie externalise la production de ses cartes d'identité (IDEMIA) — la même entreprise qui a réintroduit le défaut d'enveloppe PIN en 2018 après l'avoir corrigé en 2002.
- **L-EST-007** : La France dépense autant en 3 grands projets (>9 M€) que l'Estonie pour l'ensemble de son IT public annuel.
- **L-EST-008** : L'absence de vue centrale des dépenses IT par le ministère de tutelle est un problème commun aux deux pays.

---

### Sources

1. **e-Estonia** — X-Road overview. https://e-estonia.com/solutions/interoperability-services/x-road/
2. **Riigikontroll** — Information technology investments and costs of public institutions 2019-2024. https://www.riigikontroll.ee/en/audits/information-technology-investments-and-costs-public-institutions
3. **ERR** — Total budget of Estonia's public sector IT organizations has quadrupled in 10 years. https://news.err.ee/1609573945/total-budget-of-estonia-s-public-sector-it-organizations-has-quadrupled-in-10-years
4. **ERR** — Estonia's public IT spending and investments doubled in 6 years. https://news.err.ee/1609813497/estonia-s-public-it-spending-and-investments-doubled-in-6-years-finds-audit
5. **ERR** — Estonia to bring core public IT services under a single agency. https://news.err.ee/1610056174/estonia-to-bring-core-public-it-services-under-a-single-agency
6. **RIA** — Tasks and structure. https://www.ria.ee/en/authority-news-and-contact/authority-and-management/tasks-and-structure-authority
7. **RIA** — Strategy 2026-2030. https://www.ria.ee/en/authority-news-and-contact/authority-and-management/ria-strategy
8. **NIIS** — Making of X-Road 8, June 2025 Status Update. https://www.niis.org/blog/2025/6/11/making-of-x-road-8-june-2025-status-update
9. **Eurostat** — E-government and electronic identification 2025. https://ec.europa.eu/eurostat/statistics-explained/SEPDF/cache/131512.pdf
10. **ANSSI** — Panorama de la cybermenace 2024. https://www.cert.ssi.gouv.fr/uploads/CERTFR-2025-CTI-003.pdf
11. **ANSSI** — Rapport d'activité 2024. https://cyber.gouv.fr/actualites/lanssi-publie-son-rapport-dactivite-2024/
12. **IT for Business** — Le « move to cloud » de l'État. https://www.itforbusiness.fr/le-move-to-cloud-de-letat-une-doctrine-a-faire-respecter-90338
13. **ZDNet** — Grands projets IT de l'État : du mieux au niveau budgétaire. https://www.zdnet.fr/actualites/grands-projets-it-de-letat-du-mieux-au-niveau-budgetaire-481086.htm
14. **OECD** — User satisfaction with Estonia's public services among highest in EU. https://news.err.ee/1609826124/oecd-user-satisfaction-with-estonia-s-public-services-among-highest-in-eu
15. **Schneier on Security** — Lessons Learned from the Estonian National ID Security Flaw. https://www.schneier.com/blog/archives/2017/12/lessons_learned.html
16. **Cybernetica** — Estonian Interoperability Framework X-Road Case Study. https://cyber.ee/resources/case-studies/estonian-interoperability-framework-x-road/
17. **Nortal** — Why digital sovereignty matters and how X-Road makes it happen. https://nortal.com/insights/why-digital-sovereignty-matters-and-how-x-road-makes-it-happen
18. **EC** — Estonia 2025 Digital Decade Country Report. https://digital-strategy.ec.europa.eu/en/factpages/estonia-2025-digital-decade-country-report
19. **EC** — Rapport par pays sur la décennie numérique 2025 pour la France. https://digital-strategy.ec.europa.eu/fr/node/13535/printable/pdf
20. **IBS** — Impact assessment of the Estonian e-government services. https://www.ibs.ee/wp-content/uploads/2022/01/Impact_assessment_of_the_Estonian_e-government_services.pdf
21. **BleepingComputer** — Estonia Cancels 760,000 Electronic ID Cards. https://www.bleepingcomputer.com/news/government/estonia-cancels-760-000-electronic-id-cards-because-of-crypto-flaw/
22. **BBC** — Security flaw forces Estonia ID 'lockdown'. https://www.bbc.co.uk/news/technology-41858583
23. **Assemblée nationale** — Rapport spécial sur le budget informatique de la DGFiP. https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L16B1745-tIII-a25.html
24. **EC** — OSS Country Intelligence Report Estonia 2025. https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/OSS%20Country%20Intelligence%20Report%20Estonia%202025.pdf
25. **E-Estonia** — How do Estonians save annually 820 years of work. https://e-estonia.com/how-save-annually-820-years-of-work/
26. **E-Estonia** — E-governance saves money and working hours. https://e-estonia.com/e-governance-saves-money-and-working-hours/
27. **E-Estonia** — Estonia: 100% digital government services. https://e-estonia.com/estonia-100-digital-government-services/
28. **France Info** — Cyberattaques : 4 386 « événements de sécurité » détectés en France en 2024. https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/cyberattaques-4-386-evenements-de-securite-detectes-en-france-en-2024-en-augmentation-de-15-selon-l-anssi_7123173.html
29. **INSEE** — Dépenses et recettes des administrations publiques en 2024. https://www.insee.fr/fr/statistiques/8574705?sommaire=8574832
30. **GovInsider** — How Estonia tackled security flaws in its ID cards. https://govinsider.asia/intl-en/article/how-estonia-tackled-security-flaws-in-its-id-cards-liisa-past
