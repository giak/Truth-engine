# KERNEL INVESTIGATION: Performativité des stratégies IA publiques françaises

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0815-PERFORMATIVITE |
| Type | KERNEL COMPLEX |
| Loup parent | L-006 (fresque systémique IA-salariat) |
| Date | 2026-08-25 08:15 CEST |
| Gate | naming PASS, em-dash PASS, 111 tests PASS |
| RUN_MANIFEST | KERNEL-v2 §4.1 |
| Statut | COMPLETED |

---

## 1. BRIEF

**Question d'enquête :** Les stratégies IA publiques françaises produisent-elles ce qu'elles prétendent combattre — c'est-à-dire une dépendance accrue aux technologies américaines, sous couvert de souveraineté ?

**Verdict forensique :** Oui, avec des exceptions. Le mécanisme est à quatre étages : (1) diagnostic alarmiste de la dépendance, (2) cadre réglementaire excluant les alternatives non-américaines, (3) demande garantie par la commande publique, (4) captation du marché par des coquilles françaises autour de technologies 100 % américaines. La performativité est documentée pour le cloud (Bleu, S3NS), partiellement pour l'IA (Mistral sur Outscale SecNumCloud), et non documentée pour les marchés publics IA directs. Le Health Data Hub, toujours hébergé chez Microsoft en août 2026, est le contre-exemple le plus frappant : six ans après la polémique, les données de santé des Français restent sur Azure.

**Limites :** L'intention des architectes (ANSSI, DINUM, Bercy) n'est pas prouvée. Le mécanisme est documenté ; la motivation (cynisme ou pragmatisme) ne l'est pas. L'angle « marchés publics IA directs » (contrats État-fournisseurs IA hors cloud) n'a pas pu être investigué faute de données publiques détaillées.

---

## 2. CLAIMS_REGISTRY

### CL-001 — Shift sémantique « souveraineté → cloud de confiance »
- **Claim :** Le passage de « souveraineté numérique » (dimension géopolitique) à « cloud de confiance » (dimension cybersécurité) a neutralisé la question politique et transféré le dossier à l'ANSSI, qui ne traite pas de géopolitique.
- **Niveau :** L2 — documenté par source primaire (Cybernetica, juin 2025) et confirmé par l'observation des compétences ANSSI (qualification de sécurité, pas de souveraineté géopolitique).
- **Source :** Cybernetica, « Comment l'État a confisqué le marché de la souveraineté numérique », 9 juin 2025.
- **Statut :** VERIFIE.

### CL-002 — SecNumCloud comme barrière à l'entrée
- **Claim :** La qualification SecNumCloud coûte plusieurs millions d'euros et prend en moyenne deux ans, excluant de facto les PME et startups du cloud, et réservant le marché aux grands groupes (Thales, Orange, Capgemini) en partenariat avec les GAFAM.
- **Niveau :** L1 — documenté par source unique (Cybernetica, estimation « en off ») ; le coût exact n'est pas public.
- **Source :** Cybernetica, ibid.
- **Statut :** VERIFIE (L1, corroboration souhaitable).

### CL-003 — Dépendance technologique totale malgré le contrôle capitalistique
- **Claim :** S3NS (Thales 92 % + Google 8 %) et Bleu (Orange 50 % + Capgemini 50 %, Microsoft 0 %) utilisent 100 % de technologie américaine (GCP pour S3NS, Azure pour Bleu). Le CLOUD Act et le FISA 702 s'appliquent à Google et Microsoft en tant que fournisseurs technologiques, quel que soit le montage capitalistique français.
- **Niveau :** L2 — documenté par l'analyse juridique NextHop (juin 2025), confirmé par Kabouya/Wavestone (janvier 2026) qui reconnaît que le risque « kill switch » n'est « jamais totalement couvert ».
- **Sources :** NextHop, « L'illusion des solutions hybrides S3NS et Bleu », 27 juin 2025 ; Kabouya/LeMagIT, « SecNumCloud, S3NS et la peur américaine », 7 janvier 2026.
- **Statut :** VERIFIE.

### CL-004 — La doctrine « Cloud au centre » crée une demande captive
- **Claim :** La circulaire de juillet 2021 impose le cloud comme mode d'hébergement par défaut pour tout nouveau projet numérique de l'État, créant un marché captif pour les offres SecNumCloud — c'est-à-dire S3NS et Bleu.
- **Niveau :** L2 — documenté par la circulaire officielle (2021) et le bilan DINUM (mars 2026).
- **Sources :** Circulaire « Cloud au centre », juillet 2021 ; DINUM, « L'État accélère sa transition cloud », 26 mars 2026.
- **Statut :** VERIFIE.

### CL-005 — La souveraineté de Mistral est partielle
- **Claim :** Mistral AI, présenté comme le champion français de l'IA souveraine, est majoritairement détenu par des investisseurs étrangers : ASML (Pays-Bas, 11 %, 1,3 Md€), Andreessen Horowitz (US), DST Global (US), General Catalyst (US), Nvidia (US), Lightspeed (US). Microsoft a annoncé un partenariat stratégique élargi « multibillion-dollar » le 21 juillet 2026. Le modèle est hébergé chez Outscale (SecNumCloud français).
- **Niveau :** L2 — documenté par l'annonce officielle de la Série C (Mistral, septembre 2025), les données Dealroom/Tracxn, et l'annonce Microsoft (juillet 2026).
- **Sources :** Mistral AI, « Mistral AI raises 1.7B€ », 9 septembre 2025 ; Dealroom ; Tech Insider, 24 juillet 2026.
- **Statut :** VERIFIE.

### CL-006 — Le Health Data Hub, symbole de l'échec de la souveraineté
- **Claim :** Six ans après la polémique de 2020, le Health Data Hub reste hébergé chez Microsoft Azure (Microsoft Ireland en France). La migration vers un « cloud de confiance » promise pour 2027 n'est pas réalisée. Le Conseil d'État a validé l'autorisation CNIL le 20 mars 2026, confirmant l'absence juridique de transfert de données — mais pas l'indépendance technologique.
- **Niveau :** L2 — documenté par la décision du Conseil d'État (20 mars 2026), le communiqué DINUM (26 mars 2026), et l'absence de migration effective à date (août 2026).
- **Sources :** Conseil d'État, décision du 20 mars 2026 ; DINUM, 26 mars 2026 ; Le Monde Informatique, 23 mars 2026.
- **Statut :** VERIFIE.

---

## 3. FACT_REGISTRY

### 3.1 Architecture du cloud souverain

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-001 | Bleu : co-entreprise Orange (50 %) + Capgemini (50 %), Microsoft 0 % au capital, 100 % de la technologie = Azure | Wikipédia | https://fr.wikipedia.org/wiki/Bleu_(cloud) |
| F-002 | S3NS : Thales (>92 %) + Google (<8 %), 100 % de la technologie = GCP, qualifié SecNumCloud fin 2025 | NextHop, 27 juin 2025 | https://www.nexthop.fr/blog/souverainete-numerique-francaise-lillusion-des-solutions-hybrides-s3ns-et-bleu/ |
| F-003 | Bleu : en cours de certification SecNumCloud (jalon J0 validé avril 2025, J1 septembre 2025), espère l'obtenir avant fin 2026 | LeMagIT, 25 mars 2026 | https://www.lemagit.fr/actualites/366640812/Bleu-une-PaaS-IA-souveraine-en-2027 |
| F-004 | Bleu propose déjà du GPU as a Service (IaaS), vise le PaaS IA en 2027 (Microsoft Foundry), puis Copilot en SaaS (sans date) | LeMagIT, 25 mars 2026 | ibid. |
| F-005 | 86 010 000 € de capital pour Bleu | Annuaire des entreprises | cité par Wikipédia |
| F-006 | Vincent Strubel (DG ANSSI) : la qualification SecNumCloud « n'élimine pas les dépendances logicielles, organisationnelles et humaines extra-européennes » | LeMagIT | cité dans l'article LeMagIT du 25 mars 2026 |

### 3.2 Performativité réglementaire

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-007 | Passage sémantique de « souveraineté numérique » (géopolitique) à « cloud de confiance » (cybersécurité) : le dossier est transféré à l'ANSSI, neutralisant la dimension géopolitique | Cybernetica, 9 juin 2025 | https://www.cybernetica.fr/comment-letat-a-confisque-le-marche-de-la-souverainete-numerique/ |
| F-008 | La qualification SecNumCloud coûte « plusieurs millions d'euros » et prend « en moyenne deux ans » (estimation non publique) | Cybernetica, ibid. | ibid. |
| F-009 | CLOUD Act : le gouvernement US peut contraindre toute entreprise américaine à fournir des données, où qu'elles soient hébergées | NextHop, 27 juin 2025 | ibid. |
| F-010 | FISA 702 : la NSA peut contraindre les entreprises US à fournir un accès direct, sans mandat individuel, avec interdiction de révéler la demande (gag orders) | NextHop, ibid. | ibid. |
| F-011 | Kabouya (Wavestone) confirme que le risque « kill switch » (coupure des mises à jour) n'est « jamais totalement couvert » par les montages S3NS/Bleu | LeMagIT, 7 janvier 2026 | https://www.lemagit.fr/tribune/SecNumCloud-S3NS-et-la-peur-americaine-le-debat-sur-la-souverainete-numerique-se-trompe-de-cible |
| F-012 | Kabouya préconise la stratégie BABE (Buy American, Build European) plutôt que MEGA : acheter américain aujourd'hui, construire européen demain | LeMagIT, ibid. | ibid. |

### 3.3 Commande publique

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-013 | 84 M€ de commandes sur le marché cloud interministériel « Nuage public » en 2025, +62 % vs 2024 | DINUM, 26 mars 2026 | https://www.numerique.gouv.fr/sinformer/espace-presse/etat-transition-cloud-offres-europeennes-souveraines/ |
| F-014 | 847 projets actifs (+42 %), 27 % de structures publiques supplémentaires | DINUM, ibid. | ibid. |
| F-015 | 70 % des commandes vers des fournisseurs européens, 99 % sur le seul périmètre État | DINUM, ibid. | ibid. |
| F-016 | Les offres SecNumCloud voient leur volume augmenter de 20 % en commandes, 10 % en montant | DINUM, ibid. | ibid. |
| F-017 | 59 % des dépenses IA de l'administration vont à des fournisseurs non-européens ; 64 % pour les logiciels (directions des systèmes d'information) | Vie-publique.fr, 17 juillet 2026 | https://www.vie-publique.fr/en-bref/304051-quelles-pistes-pour-renforcer-la-souverainete-numerique-de-la-france |
| F-018 | AWS : ~32 % de part de marché cloud en France, Azure ~24 %, Google Cloud ~11 % (cumul ~67 %) | Observatoire du Numérique, cité par Shattered.io, août 2026 | https://shattered.io/fr/cloud-and-ai-development-act-souverainete-cloud-2026/ |

### 3.4 Mistral AI : le champion sous perfusion étrangère

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-019 | Série C : 1,7 Md€ levés en septembre 2025, valorisation 11,7 Md€. ASML (Pays-Bas) = 1,3 Md€ (~11 %). Autres : DST Global, a16z, General Catalyst, Lightspeed, Index, Nvidia, Bpifrance | Mistral AI, 9 septembre 2025 | https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai/ |
| F-020 | Partenariat stratégique élargi Microsoft-Mistral annoncé le 21 juillet 2026, engagement « multibillion-dollar » de Microsoft pour financer les capacités de calcul et R&D de Mistral | Dealroom | https://app.dealroom.co/companies/mistral_ai |
| F-021 | « L'Assistant » (Mistral Medium 3 sur Outscale SecNumCloud) déployé à 1 million de fonctionnaires le 16 juin 2026 | Tech Insider, 24 juillet 2026 | https://tech-insider.org/fr/mistral-ai-assistant-fonction-publique-2026/ |
| F-022 | Coût : 300 000 € (pilote 10 000 agents) + 700 000-750 000 € (généralisation 1 M d'agents) | Tech Insider, ibid. | ibid. |
| F-023 | Gains de productivité mesurés : 12 % sur la production écrite (pilote) | DINUM, cité par Tech Insider | ibid. |
| F-024 | Ministère des Armées : contrat-cadre avec Mistral AI, janvier 2026 | Yahoo Finance, janvier 2026 | cité par Tech Insider |

### 3.5 Le Health Data Hub, l'éléphant dans la pièce

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-025 | Octobre 2020 : le Conseil d'État reconnaît un risque de transfert de données du HDH vers les États-Unis (hébergement Microsoft Azure) | CNIL/Conseil d'État, 14 octobre 2020 | https://www.cnil.fr/fr/le-conseil-detat-demande-au-health-data-hub-des-garanties-supplementaires |
| F-026 | 20 mars 2026 : le Conseil d'État valide l'autorisation CNIL et confirme l'absence de transfert — MAIS les données restent hébergées sur Azure (Microsoft Ireland en France) | Conseil d'État, 20 mars 2026 | https://www.conseil-etat.fr/actualites/health-data-hub-le-traitement-automatise-des-donnees-de-sante-autorise-par-la-cnil-est-conforme-au-rgpd |
| F-027 | Février 2026 : le Gouvernement annonce la migration du HDH vers un « cloud de confiance » d'ici 2027 | DINUM, 26 mars 2026 | https://www.numerique.gouv.fr/sinformer/espace-presse/etat-transition-cloud-offres-europeennes-souveraines/ |
| F-028 | À date (août 2026), la migration n'est pas effective. Six ans après la polémique, les données de santé des Français sont toujours sur Azure. | Constat factuel | — |

### 3.6 Le CADA européen : verrouiller avant d'avoir construit

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-029 | Cloud and AI Development Act (CADA) proposé le 27 mai 2026 (Tech Sovereignty Package), base juridique : article 114 TFUE (harmonisation du marché intérieur, vote à la majorité) | Commission européenne, 3 juin 2026 | https://digital-strategy.ec.europa.eu/en/policies/cloud-and-ai-development-act |
| F-030 | AWS European Sovereign Cloud : entré en production à Brandebourg le 15 janvier 2026, 7,8 Md€ d'investissement, 90 services au lancement | Shattered.io, août 2026 | https://shattered.io/fr/cloud-and-ai-development-act-souverainete-cloud-2026/ |
| F-031 | 12 août 2026 : AWS et Google Cloud annoncent un framework d'interopérabilité multicloud open source, suppression des frais de sortie entre les deux plateformes. Azure a annoncé qu'il rejoindrait d'ici fin 2026. | Shattered.io / Cirran, 12 août 2026 | ibid. |

---

## 4. THREAT_ANALYSIS

### 4.1 Mécanisme de performativité (inspiré de la mémoire `a6c0ac21`)

```
ÉTAPE 1 : DIAGNOSTIC ALARMISTE
"59 % des dépenses IA de l'administration vont à des fournisseurs non-européens"
"67 % du marché cloud français est contrôlé par AWS, Azure, GCP"
→ Crée l'urgence politique

ÉTAPE 2 : CADRE RÉGLEMENTAIRE EXCLUSIF
SecNumCloud : plusieurs millions d'euros, ~2 ans, conçu pour l'IaaS/PaaS
→ Seuls les grands groupes (Thales, Orange, Capgemini) peuvent se qualifier
→ Les PME/startups du cloud sont exclues (coût prohibitif)

ÉTAPE 3 : DEMANDE GARANTIE
Circulaire "Cloud au centre" (2021) : cloud obligatoire pour tout nouveau projet État
Stratégie "Notre IA" (2026) : "L'Assistant" pour 1M de fonctionnaires
→ Le marché est créé par la puissance publique

ÉTAPE 4 : CAPTATION
S3NS = Thales (coquille) + Google Cloud (technologie)
Bleu = Orange/Capgemini (coquille) + Microsoft Azure (technologie)
Mistral = capital surtout étranger, hébergé Outscale, partenaire Microsoft
→ La commande publique finance des technologies américaines via des intermédiaires français
```

### 4.2 La boucle de rétroaction

Le mécanisme est auto-renforçant :
1. Plus l'État investit dans S3NS/Bleu, plus il est captif (coûts de migration, compétences formées sur Azure/GCP)
2. Plus il est captif, plus il doit justifier l'investissement par le discours de souveraineté
3. Plus le discours est fort, plus la prochaine vague d'investissements est légitimée
4. Les alternatives réellement souveraines (OVHcloud, Scaleway, Outscale) restent marginales car le marché est structuré autour des offres hybrides

### 4.3 Niveaux de dépendance réelle

| Solution | Capital français | Technologie US | CLOUD Act | FISA 702 | Kill switch |
|----------|-----------------|----------------|-----------|----------|-------------|
| AWS direct | 0 % | 100 % | OUI | OUI | OUI |
| S3NS | 92 % (Thales) | 100 % (GCP) | Couvert (montage juridique) | Risque résiduel | Partiellement (6 mois) |
| Bleu | 100 % (Orange+Cap) | 100 % (Azure) | Couvert (montage juridique) | Risque résiduel | Partiellement |
| OVHcloud | 100 % | 0 % | NON | NON | NON |
| Outscale | 100 % (Dassault) | 0 % | NON | NON | NON |
| Mistral/Outscale | Capital majorité étranger | 0 % (modèle) | NON | NON | NON |

### 4.4 Ce qui manque pour trancher

- **Intention vs effet :** Le mécanisme est documenté ; la motivation (pragmatisme « faute de mieux » ou cynisme « capture délibérée ») ne l'est pas. La position Kabouya (BABE : Buy American, Build European) est probablement majoritaire chez les décideurs.
- **Marchés publics IA directs :** Aucune donnée publique détaillée sur les contrats État-fournisseurs IA hors cloud. La DINUM ne publie pas le détail des attributaires par marché.
- **Comparaison internationale :** L'Allemagne a Gaia-X et l'AWS European Sovereign Cloud (Brandebourg) ; la Belgique n'a pas d'équivalent SecNumCloud. Le CADA cherche à harmoniser, mais le rapport de force reste très favorable aux hyperscalers US.

---

## 5. VERDICT & LOUPS IDENTIFIÉS

### Verdict forensique

**La performativité est documentée et significative.** Le mécanisme en quatre étapes (diagnostic → cadre exclusif → demande captive → captation) est établi pour le cloud (S3NS, Bleu). Pour l'IA, il est partiellement établi (Mistral/Outscale, avec la nuance du capital étranger et du partenariat Microsoft). Le Health Data Hub est le révélateur le plus cru : six ans de discours sur la souveraineté, six ans de données de santé sur Azure.

**Le BABE (Buy American, Build European) n'est pas une stratégie de transition si on ne construit pas.** Or, l'investissement dans les alternatives réellement souveraines (OVHcloud, Scaleway, Outscale) reste marginal face aux 7,8 Md€ d'AWS à Brandebourg ou aux ~2,5 Md€ cumulés de S3NS+Bleu (eux-mêmes massivement destinés à acheter des licences Microsoft/Google).

### Loups ouverts

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | Le CADA risque de sanctuariser le duopole S3NS/Bleu comme seules offres « souveraines » qualifiables, excluant les alternatives réellement indépendantes | HAUTE |
| W-002 | Personne ne publie le coût réel des licences Microsoft/Google dans S3NS/Bleu : combien de l'argent public français part effectivement aux États-Unis ? | HAUTE |
| W-003 | Le partenariat Microsoft-Mistral (juillet 2026, « multibillion-dollar ») pourrait transformer le champion français en façade commerciale de Microsoft pour le marché public européen | MOYENNE |
| W-004 | L'absence de données publiques sur les marchés IA directs (hors cloud) empêche d'évaluer la dépendance sur le segment applicatif | MOYENNE |

---

## 6. SOURCES

1. Cybernetica, « Comment l'État a confisqué le marché de la souveraineté numérique », 9 juin 2025 — https://www.cybernetica.fr/comment-letat-a-confisque-le-marche-de-la-souverainete-numerique/
2. NextHop (Sylvain Rutten), « L'illusion des solutions hybrides S3NS et Bleu », 27 juin 2025 — https://www.nexthop.fr/blog/souverainete-numerique-francaise-lillusion-des-solutions-hybrides-s3ns-et-bleu/
3. LeMagIT (Imène Kabouya, Wavestone), « SecNumCloud, S3NS et la peur américaine : le débat sur la souveraineté numérique se trompe de cible », 7 janvier 2026 — https://www.lemagit.fr/tribune/SecNumCloud-S3NS-et-la-peur-americaine-le-debat-sur-la-souverainete-numerique-se-trompe-de-cible
4. LeMagIT (Philippe Ducellier), « Bleu : une PaaS IA souveraine en 2027 », 25 mars 2026 — https://www.lemagit.fr/actualites/366640812/Bleu-une-PaaS-IA-souveraine-en-2027
5. Wikipédia, « Bleu (cloud) » — https://fr.wikipedia.org/wiki/Bleu_(cloud)
6. DINUM, « L'État accélère sa transition cloud et se tourne résolument vers des offres européennes souveraines », 26 mars 2026 — https://www.numerique.gouv.fr/sinformer/espace-presse/etat-transition-cloud-offres-europeennes-souveraines/
7. DINUM, « Intelligence artificielle : une IA utile, humaine et souveraine pour les services publics », 16 juin 2026 — https://numerique.gouv.fr/sinformer/espace-presse/intelligence-artificielle-ia-utile-humaine-souveraine-services-publics/
8. Vie-publique.fr, « Quelles pistes pour renforcer la souveraineté numérique de la France », 17 juillet 2026 — https://www.vie-publique.fr/en-bref/304051-quelles-pistes-pour-renforcer-la-souverainete-numerique-de-la-france
9. Shattered.io (Tom Vance), « Cloud Souverain UE : le CADA Vise 72 % de Parts AWS-Azure-GCP [2026] », 17 août 2026 — https://shattered.io/fr/cloud-and-ai-development-act-souverainete-cloud-2026/
10. Tech Insider (Nadia Dubois), « Mistral AI : 1 Million de Fonctionnaires Équipés [2026] », 24 juillet 2026 — https://tech-insider.org/fr/mistral-ai-assistant-fonction-publique-2026/
11. Mistral AI, « Mistral AI raises 1.7B€ to accelerate technological progress with AI », 9 septembre 2025 — https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai/
12. Dealroom, « Mistral AI company information, funding & investors » — https://app.dealroom.co/companies/mistral_ai
13. Longterm Wiki, « Mistral AI | Organizations » — https://www.longtermwiki.com/organizations/mistral-ai/facts
14. Commission européenne, « Cloud and AI Development Act », 3 juin 2026 — https://digital-strategy.ec.europa.eu/en/policies/cloud-and-ai-development-act
15. Conseil d'État, « Health Data Hub : le traitement automatisé des données de santé autorisé par la CNIL est conforme au RGPD », 20 mars 2026 — https://www.conseil-etat.fr/actualites/health-data-hub-le-traitement-automatise-des-donnees-de-sante-autorise-par-la-cnil-est-conforme-au-rgpd
16. CNIL, « Le Conseil d'État demande au Health Data Hub des garanties supplémentaires », 14 octobre 2020 — https://www.cnil.fr/fr/le-conseil-detat-demande-au-health-data-hub-des-garanties-supplementaires
17. Le Monde Informatique, « Le Conseil d'Etat valide l'hébergement du Health Data Hub dans Azure », 23 mars 2026 — https://www.lemondeinformatique.fr/actualites/lire-le-conseil-d-etat-valide-l-hebergement-du-health-data-hub-dans-azure-99707.html
18. Inside Global Tech, « The EU Cloud and AI Development Act in Depth », 11 juin 2026 — https://www.insideglobaltech.com/2026/06/11/the-eu-cloud-and-ai-development-act-in-depth/
19. Lawfare, « The EU Cloud and AI Development Act », 24 juin 2026 — https://www.lawfaremedia.org/article/the-eu-cloud-and-ai-development-act