# KERNEL INVESTIGATION: France Travail CCRE — L'algorithme qui trie les chômeurs en « suspects »

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0930-FRANCE-TRAVAIL-CCRE |
| Type | KERNEL COMPLEX |
| Loup parent | L-007 (fresque systémique IA-salariat) |
| Date | 2026-08-25 09:30 CEST |
| Gate | — |
| Sources | 20 |
| Statut | COMPLETED |

---

## 1. BRIEF

**Question d'enquête :** Que fait exactement l'algorithme « Ciblage du Contrôle de la Recherche d'Emploi » (CCRE) de France Travail ? Quels sont ses critères, son ampleur, ses conséquences ? S'agit-il d'un cas d'école d'IA appliquée au contrôle social des populations précaires ?

**Verdict forensique : Le CCRE est un algorithme de profilage des chômeurs à des fins de contrôle, déployé sans transparence, sans accès au code source, et en violation des demandes CADA. Il applique 26 variables pour classer 6 millions de personnes en « suspects » et « non suspects », avec pour objectif de passer de 200 000 contrôles en 2017 à 1,5 million en 2027 (×7,5). C'est le cas le plus documenté et le plus inquiétant d'IA appliquée au contrôle social en France — et il s'inscrit dans un pattern plus large (CNAF, Assurance maladie) désormais bien établi par La Quadrature du Net.**

---

## 2. FACT_REGISTRY

### 2.1 L'algorithme — ce qu'il fait

| ID | Fait | Source |
|----|------|--------|
| F-001 | Nom officiel : « Ciblage du Contrôle de la Recherche d'Emploi » (CCRE). Objectif déclaré : « recourir à l'IA afin d'identifier les dossiers nécessitant un examen approfondi et alimenter automatiquement l'outil de contrôle de la recherche d'emploi. » | Document France Travail présenté au comité d'éthique IA, 10 décembre 2025, publié par LQDN |
| F-002 | Technologie : arbre de décision (machine learning), paramètres sélectionnés par itérations successives. Pas d'IA générative — mais LQDN alerte sur le risque d'extension future. | LQDN, 20 juillet 2026 |
| F-003 | Entraîné sur 60 000 contrôles passés. Deux campagnes de tests de ~7 000 personnes chacune (sur les ruptures conventionnelles uniquement). | LQDN, ibid. |
| F-004 | Classification binaire : chaque demandeur d'emploi se voit attribuer un profil « suspect » ou « non suspect ». Les « suspects » sont placés sur une liste de contrôle prioritaire. | LQDN, ibid. |
| F-005 | Le document prévoit d'« étendre l'utilisation du modèle à d'autres publics » et de « transmettre chaque mois des listes de contrôle ciblés. » | LQDN, ibid. |

### 2.2 Les 26 variables — ce qui détermine si vous êtes « suspect »

| ID | Catégorie | Variables connues | Source |
|----|-----------|-------------------|--------|
| F-006 | Inscription/ancienneté | Ancienneté d'inscription, niveau de formation | LQDN, document CCRE |
| F-007 | Recherche d'emploi | « Visibilité » (CV en ligne ou non), abonnements aux offres, actions récentes, métier recherché (en tension ou non) | LQDN, ibid. |
| F-008 | Activité déclarée | Heures travaillées, activité non salariée, création d'entreprise | LQDN, ibid. |
| F-009 | Rendez-vous/obligations | Historique des manquements (absence à un RDV), refus d'offres raisonnables d'emploi | LQDN, ibid. |
| F-010 | Règles de classification | **Non publiées.** Les pondérations, seuils et interactions entre variables sont inconnus. Seule la liste des variables est publique. | LQDN, ibid. |

### 2.3 L'ampleur — l'industrialisation du contrôle

| ID | Fait | Source |
|----|------|--------|
| F-011 | Contrôles CRE en 2017 : ~200 000. En 2025 : **960 000** (officiel France Travail, août 2026 — soit ×4,8). Le chiffre de 730 000 cité par LQDN date du document CCRE de décembre 2025 ; les données définitives 2025 publiées en août 2026 donnent 960 000. | France Travail, août 2026 |
| F-012 | Hausse 2024 → 2025 : +63,9 %. Moyenne mensuelle 2025 : 80 000. | France Travail, ibid. |
| F-013 | Objectif gouvernemental 2027 : **1 500 000 contrôles** (annoncé par Gabriel Attal, 2024). Soit ×7,5 vs 2017. | Le Parisien, 24 avril 2025 |
| F-014 | Contrôles ciblés (ceux que le CCRE alimente) : ~40 % du total, soit ~500 000 en 2025, objectif ~600 000 en 2027. Le reste = contrôles aléatoires + signalements. | LQDN, document CCRE |
| F-015 | **6 millions de personnes potentiellement profilables par mois :** 5 752 600 inscrits en catégories A,B,C fin 2025 (DARES) + allocataires RSA dont l'inscription est obligatoire depuis le 1er janvier 2026. | DARES, janvier 2026 ; LQDN, juillet 2026 |
| F-016 | 83 % des contrôles aboutissent à une absence de sanction (2024). 17 % de sanctions : radiation, suspension, réduction d'allocations. | Le Parisien, avril 2025 |

### 2.4 L'opacité — ce que France Travail refuse de montrer

| ID | Fait | Source |
|----|------|--------|
| F-017 | **Toutes les demandes d'accès au code source des IA de France Travail sont restées sans réponse.** Y compris MatchFT (présélection candidats) et ChatFT (assistance conseillers). | LQDN, 20 juillet 2026 |
| F-018 | Pour MatchFT et ChatFT, France Travail « n'a même pas pris la peine de motiver sa décision auprès de la CADA — en violation flagrante de la loi. » | LQDN, ibid. |
| F-019 | Question au Sénat (31 juillet 2026) : « Il souhaite donc savoir quand le Gouvernement entend rendre transparent le code source de l'algorithme. » Pas de réponse publique à date. | Sénat, question n°SEQ260709657, 31 juillet 2026 |
| F-020 | Une « Charte de France Travail pour une éthique de ses usages de l'IA » existe et vante « transparence » et « éthique » — en contradiction directe avec le refus d'accès au code. | LQDN, citant la charte |

### 2.5 Les précédents — le pattern CNAF/Assurance maladie

| ID | Fait | Source |
|----|------|--------|
| F-021 | CNAF : algorithme de scoring des allocataires. Code source obtenu seulement après « longue bataille juridique et médiatique. » Résultat : sur-contrôle organisé des femmes isolées, personnes au RSA, personnes en situation de handicap. | LQDN |
| F-022 | Assurance maladie : algorithme de profilage. Code source obtenu « à la faveur d'une erreur de caviardage par l'administration. » Même pattern de sur-contrôle documenté. | LQDN |
| F-023 | Dans les deux cas, l'opacité a permis d'organiser le sur-contrôle de populations vulnérables « sans jamais avoir à rendre de comptes. » | LQDN |

---

## 3. ANALYSE — Les quatre mécanismes de l'IA de contrôle social

### 3.1 La dépolitisation du contrôle

Le document CCRE contient une phrase clé, citée par LQDN : l'IA permettrait « **une suppression des a priori** en proposant des dossiers à contrôler sur la base de critères objectifs. »

C'est la mécanique centrale du solutionnisme technologique appliqué au contrôle social : transformer un choix politique — qui contrôler, sur quels critères, avec quelle intensité — en calcul technique. L'algorithme n'a pas d'« a priori » — il a des biais statistiques, entraînés sur des données historiques de contrôle qui reflètent déjà des choix politiques passés. Mais ces biais sont opaques, donc incontestables.

### 3.2 L'individualisation de la discrimination

Le profilage algorithmique individualise le processus de sélection : personne n'est contrôlé « parce qu'il est au RSA » ou « parce qu'il est une femme isolée » — il est contrôlé parce que son « score » s'est dégradé. Ce que le score capture, c'est précisément l'appartenance à ces catégories. Mais la médiation algorithmique rend le lien causal invisible, donc juridiquement inattaquable.

### 3.3 L'effet cliquet de la massification

```
2017 : 200 000 contrôles
2025 : 960 000 contrôles (+63,9 % vs 2024)
2027 objectif : 1 500 000 contrôles
```

Le CCRE n'est pas un outil de ciblage — c'est un outil de **massification.** Pour passer de 960 000 à 1 500 000 en deux ans, il faut automatiser la sélection. Un humain ne peut pas traiter ce volume. L'algorithme est la condition de possibilité de la massification.

Et une fois l'infrastructure de contrôle automatisée déployée, elle ne sera jamais démontée. La trajectoire 2017 → 2027 est une courbe exponentielle : ×2,4 en 8 ans, ×1,6 en 2 ans. Prochaine étape logique : l'IA générative qui formulera la « suggestion » de décision — LQDN l'anticipe explicitement.

### 3.4 L'inversion du fardeau de la preuve

Avec l'algorithme, ce n'est plus France Travail qui doit justifier pourquoi elle contrôle untel — c'est le chômeur qui doit prouver qu'il cherche du travail. Le profilage devient le mécanisme par défaut : tout le monde est « suspectable », l'algorithme détermine qui est « suspect », et la personne classée « suspecte » doit se disculper.

**83 % des contrôles n'aboutissent à aucune sanction.** Cela signifie que 83 % des personnes contrôlées sont « innocentes » — et pourtant elles subissent le stress, le temps perdu, la stigmatisation du contrôle. Le taux d'erreur administratif est massif, mais il est traité comme un coût de fonctionnement acceptable.

---

## 4. LE TABLEAU DE BORD DU CONTRÔLE ALGORITHMIQUE

### Les trois IA de France Travail (connues à ce jour)

| Nom | Fonction | Transparence |
|-----|----------|-------------|
| **CCRE** | Profilage pré-contrôle. 26 variables. « suspect/non suspect. » | Liste des variables publique. Code source, pondérations, seuils : **REFUSÉ.** |
| **MatchFT** | Présélection de candidats pour offres d'emploi via SMS. | **REFUSÉ.** Pas même de motivation CADA. |
| **ChatFT** | Assistance aux conseillers (généralisé). | **REFUSÉ.** Pas même de motivation CADA. |

### La chaîne d'automatisation (existante + probable)

```
CCRE (sélection des cibles)
    ↓
Robots de décision (clôture automatique des contrôles, déjà déployés)
    ↓
[Probable] IA générative (suggestion de décision pour le contrôleur)
    ↓
[Futur] Automatisation totale de la chaîne de contrôle
```

---

## 5. LE CONTEXTE — Ce qui rend le CCRE particulièrement toxique

### 5.1 L'inscription obligatoire des allocataires RSA (1er janvier 2026)

Depuis le 1er janvier 2026, tous les allocataires du RSA sont obligatoirement inscrits à France Travail. Cela ajoute environ 1,8 million de personnes à la base de données, dont beaucoup n'étaient pas inscrites auparavant parce qu'elles n'étaient pas « disponibles pour l'emploi » (handicap, garde d'enfants, problèmes de santé...). Ces personnes sont désormais profilables par le CCRE.

### 5.2 La simultanéité avec la réforme de l'assurance chômage

Les règles d'indemnisation ont été durcies en 2024-2025 (réduction de la durée, conditions d'affiliation). Moins de droits + plus de contrôles = pression maximale sur les chômeurs.

### 5.3 France Travail revendique une IA « éthique »

Le décalage entre la charte officielle (« éthique », « transparente ») et le refus systématique d'accès au code source est un cas d'école de **performativité institutionnelle** : l'institution produit des énoncés qui ne correspondent à aucun acte réel. Exactement le mécanisme documenté dans l'investigation sur les stratégies IA publiques françaises.

---

## 6. VERDICT

**Le CCRE est un algorithme de profilage social déployé sans contrôle démocratique, qui applique l'IA au tri des populations précaires avec l'objectif explicite de multiplier les contrôles par 7,5 en dix ans.**

Les faits sont établis et sourcés :
- 26 variables, 6 millions de personnes profilables, 960 000 contrôles en 2025, objectif 1,5 million en 2027
- Code source refusé, en violation de la loi CADA
- Pattern identique à la CNAF et l'Assurance maladie : opacité → sur-contrôle des populations vulnérables → découverte fortuite → révélation des biais

**Ce qui est nouveau par rapport à la CNAF et l'Assurance maladie :** l'échelle. 6 millions de personnes, c'est 10 % de la population active française. La chaîne d'automatisation est en cours de déploiement (CCRE → robots de décision → probable IA générative). Et l'infrastructure, une fois construite, ne sera jamais démontée.

**Le CCRE n'est pas un cas isolé. C'est la forme la plus aboutie d'un modèle français de contrôle social algorithmique qui combine :**
1. Objectifs politiques de massification des contrôles (1,5 M en 2027)
2. Outils techniques opaques (code source refusé)
3. Dépolitisation du ciblage (« suppression des a priori »)
4. Individualisation de la discrimination (« votre score est mauvais », pas « vous êtes au RSA »)
5. Inversion du fardeau de la preuve (c'est au chômeur de prouver sa bonne foi)

---

## 7. LOUPS OUVERTS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | L'extension probable du CCRE à l'IA générative (suggestion de décision) créerait une automatisation totale de la chaîne de contrôle — sans supervision humaine réelle. | TRÈS HAUTE |
| W-002 | L'inscription obligatoire des allocataires RSA depuis janvier 2026 ajoute 1,8 million de personnes vulnérables dans le périmètre de profilage. | HAUTE |
| W-003 | La violation répétée de la loi CADA par France Travail (absence de motivation des refus) est un mépris institutionnel du droit d'accès aux documents administratifs. | HAUTE |
| W-004 | Le taux de 83 % de contrôles sans sanction révèle un taux d'erreur massif du ciblage. Le coût humain (stress, stigmatisation, temps perdu) n'est jamais évalué. | MOYENNE |

---

## 8. SOURCES

1. La Quadrature du Net, « France Travail déploie un outil de profilage algorithmique à des fins de contrôle », 20 juillet 2026 — https://www.laquadrature.net/2026/07/20/france-travail-deploie-un-outil-de-profilage-algorithmique-a-des-fins-de-controle/
2. Yahoo! Actualités / Radio France, « France Travail utilise désormais un algorithme pour noter chaque demandeur d'emploi », 20 juillet 2026 — https://fr.news.yahoo.com/france-travail-utilise-d%C3%A9sormais-algorithme-060017551.html
3. Next.ink, « France Travail : un algorithme pour accélérer le profilage des chômeurs », 20 juillet 2026 — https://next.ink/248042/france-travail-un-algorithme-pour-accelerer-le-profilage-des-chomeurs-et-les-controles/
4. Kand, « Algorithme France Travail : les 26 critères de contrôle », 30 juillet 2026 — https://kand.fr/ressources/algorithme-france-travail-controle-chomeurs
5. Sénat, question n°SEQ260709657, « Utilisation de l'intelligence artificielle par France Travail », 31 juillet 2026 — https://www.senat.fr/questions/base/2026/qSEQ260709657.html
6. France Travail, « Le contrôle de la recherche d'emploi en 2025 », août 2026 — https://www.francetravail.org/statistiques-analyses/demandeurs-demploi/trajectoires-et-retour-a-lemploi/le-controle-de-la-recherche-d-emploi-en-2025.html
7. AEF Info, « En 2025, 960 000 contrôles de la recherche d'emploi ont été démarrés », août 2026
8. Le Parisien, « Recherche d'emploi : les contrôles des chômeurs devront doubler d'ici à 2027 », 24 avril 2025
9. Le Monde, « France Travail intensifie encore le contrôle des demandeurs d'emploi », 24 avril 2025
10. DARES, « Les inscrits à France Travail au 4e trimestre 2025 », janvier 2026
11. Korben, « France Travail — 26 variables décident si vous êtes suspect », 20 juillet 2026
12. Journal du Geek, « France Travail utilise un algorithme IA pour repérer et contrôler les chômeurs suspects », 22 juillet 2026
13. Demarchesadministratives.fr, « France Travail : le contrôle des demandeurs d'emploi a explosé », août 2026
14. CNAF / Assurance maladie, précédents de profilage algorithmique — documents LQDN
15. France Travail, « Charte pour une éthique de ses usages de l'IA »
16. Document CCRE présenté au comité d'éthique IA du 10 décembre 2025, publié par LQDN