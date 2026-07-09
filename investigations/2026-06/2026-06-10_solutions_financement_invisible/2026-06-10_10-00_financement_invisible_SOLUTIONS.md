# FINANCEMENT INVISIBLE — Comment déplacer 8 000€/mois sans détection

**Solutions Investigation · KERNEL v2.0 Protocol**

**Date** : 2026-06-10  |  **Type** : `SOLUTIONS`  |  **Complexité** : COMPLEX  |  **Statut** : COMPLETE

---

## §0 PROBLÈME : Le gap de traçabilité

L'investigation FINANCING établit qu'une cellule de 5 personnes nécessite 6 050€/mois (72 600€/an) pour survivre et 8 150€/mois (97 800€/an) pour fonctionner. Mais aucune solution concrète n'est identifiée pour déplacer ces sommes sans déclenchement des systèmes de détection français.

Le problème est le suivant : le système bancaire français est interconnecté avec TRACFIN via la plateforme ERMES (décret du 30 janvier 2025 rendant ERMES obligatoire pour toutes les professions assujetties). Toute transaction supérieure à 1 000€ en espèces est interdite entre un particulier et un professionnel. Les crypto-monnaies sont pseudonymes mais traçables sur les blockchains publiques. Les plateformes de crowdfunding (Patreon, Leetchi, KissKissBankBank) collaborent avec les autorités.

Ce rapport examine chaque mécanisme disponible en France en 2026, évalue son niveau de traçabilité réel, son risque légal, et sa capacité de volume.

**Cadre pénal applicable** : art.450-1 CP (association de malfaiteurs : 10 ans + 150 000€), art.324-1 CP (blanchiment simple : 5 ans + 375 000€), art.324-1-1 CP (nouveau depuis juin 2025 : présomption de blanchiment pour tout usage de crypto-actif à fonction d'anonymisation), art.421-1 CP (financement du terrorisme : jusqu'à 30 ans), LOPMI 2023 (surveillance IA, vidéosurveillance algorithmique, cyber).

---

## §1 TRACFIN : Seuils et critères de détection (2026)

### 1.1 Volume de déclarations

En 2024, TRACFIN a reçu 215 410 informations dont 211 165 déclarations de soupçon transmises par les 50 professions assujetties. Hausse de 13,2% par rapport à 2023. Le secteur bancaire représente 57,2% des déclarations totales. Les professions non-financières (notaires, agents immobiliers, experts-comptables) augmentent chaque année. Source : https://risqueblanchiment.fr/articles/tracfin-bilan-2025-declarations-soupcon

### 1.2 Seuil espèces

Le plafond de paiement en espèces entre un particulier et un professionnel est de 1 000€ (art. L112-6 du Code monétaire et financier). Pour les non-résidents, le plafond est de 15 000€. Entre particuliers, aucun plafond n'existe, mais une transaction immobilière est limitée à 3 000€ en espèces. Sources : https://www.banque-france.fr/fr/aide-faq/Moyens%20de%20paiement , https://www.service-public.gouv.fr/particuliers/vosdroits/F10999

### 1.3 Critères de déclenchement d'une déclaration de soupçon

L'article L.561-15 du Code monétaire et financier pose trois critères alternatifs, un seul suffit :

1. Soupçon de blanchiment : sommes provenant d'une infraction punie d'au moins 1 an de prison
2. Soupçon de fraude fiscale
3. Complexité inhabituelle ou montant disproportionné

Les banques utilisent des algorithmes de scoring depuis LOPMI 2023. Critères d'alerte typiques : dépôt d'espèces fragmenté (structuring), virements vers des exchanges crypto sans justification, flux entrants de l'étranger sans origine claire, comptes professionnels avec flux personnels. Source : https://www.risksonnar.com/blog/tracfin-declaration-soupcon-guide

### 1.4 ERMES obligatoire

Depuis le 1er février 2025, toutes les déclarations de soupçon doivent transiter par la plateforme ERMES (décret du 30 janvier 2025). Les déclarations papier sont réservées aux urgences. Source : https://www.caceis.com/regwatch/january-2025

### 1.5 Amendes

Défaut de déclaration de soupçon : 5% du montant de la transaction non déclarée, avec un minimum de 10 000€. Pour les personnes physiques, amende administrative jusqu'à 75 000€. Source : https://globallawexperts.com/how-do-i-make-a-tracfin-declaration

---

## §2 Crypto-anonymité : Audit 2026

### 2.1 Monero (XMR) : le gold standard, mais sous pression

Monero reste la crypto offrant le meilleur niveau de confidentialité par défaut : signatures de groupe (ring signatures), adresses furtives (stealth addresses), RingCT (montants cachés), Dandelion++ (protection réseau). Chaque transaction est privée par défaut. Source : https://www.elliptic.co/blockchain-basics/what-are-privacy-coins

**Problème n°1 : Delistage des exchanges.** Binance et Kraken ont délisté XMR dans l'UE en 2024. Les exchanges qui listent encore XMR en 2026 : KuCoin, MEXC, TradeOgre, Godex.io, Bisq (P2P sans KYC), ChangeNOW. Mais le nombre de plateformes accessibles depuis la France diminue chaque année. Source : https://coinbureau.com/analysis/top-privacy-coins

**Problème n°2 : Traçabilité partielle.** Des chercheurs de TRM Labs ont documenté des heuristiques de traçage : le "10 Block Decoy Bug" permet d'identifier le vrai spend dans certaines transactions. Des firmes de blockchain analytics (Chainalysis, CipherTrace) ont développé des capacités de tracing limitées mais en amélioration constante. L'IRS américain a offert 625 000$ de bounty pour le tracing de Monero en 2020. Source : https://www.trmlabs.com/resources/blog/the-rise-of-monero-traceability-challenges-and-research-review

**Problème n°3 : L'article 324-1-1 CP (loi n°2025-532 du 13 juin 2025).** Cet article établit une présomption légale de blanchiment pour toute opération utilisant un crypto-actif "comportant une fonction d'anonymisation intégrée". En clair : posséder ou transiger en Monero est désormais présumé illicite en France, sans que l'accusation ait à prouver l'origine illicite des fonds. Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051743092

### 2.2 Zcash (ZEC) : scellé optionnel

Zcash offre des transactions shielded (z-addresses) via zk-SNARKs, mais les transactions transparentes (t-addresses) sont publiques comme Bitcoin. La majorité des utilisateurs n'utilisent pas le mode shielded, ce qui réduit l'anonymity set. Plus listé que Monero, mais l'article 324-1-1 CP s'applique aussi. Source : https://coinbureau.com/analysis/top-privacy-coins

### 2.3 Bitcoin mixers / tumblers : RISQUE CRITIQUE

Les mixeurs Bitcoin (Wasabi Wallet, Samourai Whirlpool, etc.) ont été la cible d'opérations judiciaires majeures. En 2023-2024, les fondateurs de Samourai Wallet ont été arrêtés, Tornado Cash sanctionné par l'OFAC. Utiliser un mixer en 2026 est un signalement automatique pour toute banque utilisant un logiciel de compliance. Les mixeurs sont illégaux dans plusieurs juridictions et constituent en France un blanchiment aggravé (art.324-2 CP : 10 ans + 750 000€). Source : https://www.elliptic.co/blockchain-basics/what-are-privacy-coins

### 2.4 Crypto KYC en France 2026

Depuis la transposition de la 5e directive AML (2020) et MiCA (2023), tous les PSAN (Prestataires de Services sur Actifs Numériques) enregistrés en France doivent appliquer le KYC complet. L'AMF a mis à jour l'Instruction DOC-2019-23 au 1er janvier 2025. Le seuil de KYC est de 0€ pour les transactions crypto: tout utilisateur doit être identifié. Les exchanges sans KYC (Bisq, TradeOgre) sont inaccessibles depuis les IP françaises ou présentent un risque de blocage. Source : https://regulaforensics.com/blog/kyc-crypto , https://shuftipro.com/blog/kyc-crypto-exchanges-regulations-requirements

### 2.5 Fiat off-ramp : le vrai problème

Même avec du Monero parfaitement anonyme, le passage en monnaie fiat (euros) est le point de rupture. Tout retrait vers un compte bancaire français déclenche une vérification d'origine des fonds. Les distributeurs automatiques crypto (BTC ATM) sont régulés et limités à 1 000€. Le P2P (LocalMonero, Bisq) est traçable via les dépôts bancaires associés. Source : https://coinbureau.com/analysis/top-privacy-coins

### Conclusion crypto 2026

Le schéma "donateurs anonymes -> Monero -> fiat" est théoriquement le plus robuste, mais l'article 324-1-1 CP rend sa simple possession présumée criminelle. La fenêtre d'opacité réelle est étroite et temporaire. Le volume mensuel de 8 000€ en Monero via Bisq ou P2P est faisable mais détectable à la sortie fiat.

---

## §3 Financement collectif légal en France

### 3.1 Association loi 1901

L'association loi 1901 est la structure la plus simple pour collecter et redistribuer des fonds. Dépôt en préfecture, compte bancaire dédié, déclaration des comptes annuels si subventions > 153 000€. La comptabilité doit être régulière mais n'est pas publique. Les dons manuels (espèces) jusqu'à 1 000€ sont possibles. Source : https://www.service-public.gouv.fr/particuliers/vosdroits/N31931

**Limite** : Les banques exigent les statuts, le PV d'AG, la liste des dirigeants. Une association est identifiée par son SIRET. TRACFIN peut demander communication des comptes. Les banques signalent les flux suspects (dépôts espèces > 1 000€, virements entrants sans origine claire). L'association est transparente pour les autorités.

### 3.2 SCIC (Société Coopérative d'Intérêt Collectif)

La SCIC est une société commerciale (SARL, SAS ou SA) à but d'utilité sociale. Multi-sociétariat obligatoire (3 catégories : salariés, bénéficiaires, autres parties prenantes). Principe "une personne = une voix". Les bénéfices sont réinvestis à 57,5% minimum. Source : https://www.les-scop.coop/les-scic

**Intérêt pour le financement** : La SCIC peut émettre des parts sociales (capital variable). Les apports en compte courant d'associés sont possibles sans limite théorique. Les collectivités territoriales peuvent entrer au capital (ce qui apporte une couverture légale). Les flux financiers entre associés sont justifiés par l'activité coopérative. Source : https://bpifrance-creation.fr/encyclopedie/structures-juridiques/structures-less/scic-societe-cooperative-dinteret-collectif

**Limite** : La SCIC est immatriculée au RCS (Registre du Commerce et des Sociétés). Ses comptes sont déposés au greffe du tribunal de commerce. L'objet social doit être authentique (activité réelle d'utilité sociale). Une SCIC fictive serait une fraude.

**Chiffres clés 2024** : 1 417 SCIC actives en France, 15 720 salariés, 1,6 milliard d'€ de CA. Source : https://pro.orange.fr/lemag/scic-societe-cooperative-d-interet-collectif-definition-avantages-et-inconvenients-CNT000002oifCp.html

### 3.3 Fond de dotation

Créé par la loi LME 2008-776, le fonds de dotation est une personne morale de droit privé à but non lucratif qui reçoit et gère des biens pour une mission d'intérêt général. Plus souple qu'une fondation reconnue d'utilité publique. Doté d'un conseil d'administration (minimum 3 membres). Source : https://www.village-justice.com/articles/fonds-dotation-association-loi-1901-quelle-difference,39354.html

**Limite** : Les dons au fonds de dotation sont publics (reçus fiscaux). La comptabilité est contrôlée par la préfecture. Les flux doivent correspondre à l'objet social déclaré.

### 3.4 Caisse de solidarité / Caisse de grève

Les caisses de grève sont des mécanismes syndicaux historiques. Exemples : Caisse de grève de la France Insoumise (https://lafranceinsoumise.fr/caisse-de-greve-insoumise-2025/), Caisse de solidarité CGT (https://cgtbressuire.fr/index.php/2025/09/30/caisse-de-solidarite-avec-les-grevistes/), Fonds de solidarité SNES-FSU (https://www.snes.edu/agissons/outils/greve-fonds-de-solidarite/). Ces caisses collectent via HelloAsso, PayPal, virements, ou espèces lors de rassemblements.

**Intérêt** : Mécanisme socialement accepté. Pas de déclaration individuelle des donateurs si dons < 1 000€ (seuil de déclaration fiscale des prêts entre particuliers).

**Limite** : Les plateformes de collecte (HelloAsso, Leetchi) transmettent les données des collecteurs à TRACFIN sur demande. Les comptes bancaires des syndicats sont surveillés comme tout compte professionnel.

---

## §4 Systèmes non-bancaires

### 4.1 Prêt entre particuliers (PAP)

Le prêt entre particuliers est légal en France, encadré par les articles 1892 et suivants du Code civil. Pour un montant supérieur à 5 000€, le prêt doit être déclaré aux impôts via le formulaire de déclaration de prêt (annexe à la déclaration de revenus). En dessous de 5 000€, aucune déclaration n'est requise. Source : https://www.service-public.gouv.fr/particuliers/vosdroits/F1059

**Mécanisme de pooling** : 10 personnes prêtant 600€/mois chacune = 6 000€/mois. Chaque prêt individuel < 5 000€. Pas de déclaration fiscale. Pas de trace bancaire centralisée. Les remboursements peuvent être en nature ou différés.

**Limite** : La multiplication des prêts entre les mêmes personnes peut être qualifiée d'opération en banque sans agrément (exercice illégal de la profession bancaire, art. L511-5 CMF). Le prêt doit avoir une durée déterminée. Un prêt sans terme fixe ni intérêt peut être requalifié en don déguisé (fiscalité des donations).

### 4.2 Tontine

La tontine (au sens classique : système d'épargne collectif où les participants cotisent et le dernier survivant reçoit le capital) est interdite en France en tant que produit d'assurance depuis les années 1930. Les tontines informelles (cercles d'épargne africains, "tontines" communautaires) ne sont pas explicitement interdites mais constituent un risque juridique : absence de contrat écrit, risque de qualification d'exercice illégal de la banque. Source : https://www.france-immoplus.fr/tontine-interdite-france/

### 4.3 SEL (Systèmes d'Échange Local)

Les SEL sont des associations loi 1901 permettant l'échange de biens et services sans monnaie nationale, via des unités de compte internes. Il existe environ 700 SEL en France. Les transactions en SEL sont officiellement non-imposables si elles relèvent de l'échange non-professionnel. Source : https://www.selidaire.org/

**Limite** : Les SEL ne permettent pas de financer des dépenses en euros (loyer, nourriture, transport). Le volume d'échange est limité. Un SEL ne peut servir à contourner le système bancaire pour des flux monétaires.

### 4.4 Cash pooling sans banque

Le cash pooling physique (collecte d'espèces lors de réunions, événements, rassemblements) est le seul mécanisme qui échappe totalement à la traçabilité bancaire. 

**Contrainte n°1** : Plafond espèces de 1 000€ par transaction (art. L112-6 CMF). Impossible de payer un loyer (1 500€) ou un achat important en espèces.

**Contrainte n°2** : Dépôt en banque des espèces collectées. Tout dépôt > 1 000€ en une fois ou des dépôts fragmentés réguliers (structuring) déclenchent une déclaration de soupçon. Les banques ont des algorithmes anti-structuring depuis LOPMI 2023.

**Contrainte n°3** : Conservation d'espèces en grande quantité : risque de vol, de perte, de destruction. Pas de justification possible si découvert (présomption de blanchiment).

### 4.5 Cartes prépayées anonymes

Les cartes prépayées anonymes étaient un outil de contournement jusqu'en 2020. Depuis la 5e directive AML (transposée en 2020-2022), toutes les cartes prépayées doivent être identifiées. Le plafond de charge est de 150€ pour les cartes anonymes (disparues). Les cartes identifiées sont traçables. Source : https://www.amf-france.org/en/news-publications/depth/money-laundering

---

## §5 Cas internationaux de financement dissident

### 5.1 Hong Kong : Spark Alliance (2019)

Spark Alliance, groupe de financement des protestataires hongkongais, a collecté environ 10 millions de dollars via crowdfunding en ligne pendant les 6 mois de protestations de 2019. Utilisation de comptes bancaires HSBC et de plateformes de donation en ligne. Résultat : HSBC a fermé le compte en novembre 2019, la police hongkongaise a gelé 70 millions HKD (9 millions USD) en décembre 2019, et arrêté 4 membres pour blanchiment d'argent. Les fonds avaient été placés sur des produits d'assurance-vie personnelle, ce qui a déclenché les soupçons. Sources : https://www.bloomberg.com/news/articles/2019-12-20/mysterious-bags-of-cash-trigger-major-hong-kong-protest-arrests , https://www.cnn.com/2019/12/20/asia/hong-kong-protests-money-frozen-intl-hnk/ , https://www.sparkalliance.org/

**Leçon** : Le crowdfunding bancarisé est vulnérable à la fermeture de compte et au gel des fonds. L'utilisation de comptes personnels pour des fonds collectifs est un signalement de blanchiment.

### 5.2 Navalny : Bitcoin comme assurance (2016-2024)

L'équipe d'Alexei Navalny a commencé à accepter les dons en Bitcoin dès 2016 comme "assurance" contre le blocage des comptes bancaires par les autorités russes. En janvier-février 2021, l'équipe a reçu 300 000$ en Bitcoin. En septembre 2022, 840 000$ en crypto, dont une partie en Monero. Les donations affluaient via les adresses BTC publiques de Navalny, relayées sur les réseaux sociaux. Sources : https://www.reuters.com/world/bitcoin-donations-surge-jailed-kremlin-critic-navalnys-cause-data-2021-02-11/ , https://www.themoscowtimes.com/2021/02/11/russian-opposition-finds-refuge-in-bitcoin-a72907 , https://vk.com/wall-209024007_12866

**Leçon** : Les adresses Bitcoin publiques sont pseudonymes mais transparentes. Les échanges crypto-fiat en Russie ont été tracés par les autorités. Le Monero a été utilisé pour les transferts internes après 2022. Le schéma a fonctionné parce que l'État russe n'a pas de système de surveillance financière comparable à TRACFIN/ERMES. En France, les mêmes adresses publiques auraient été signalées.

### 5.3 Ukraine : Crypto donations d'État (2022-2024)

En février 2022, le gouvernement ukrainien a ouvert des adresses Bitcoin, Ethereum et USDT pour recevoir des dons internationaux. Mécanisme simple : adresses publiques relayées par le compte Twitter officiel @Ukraine. Source : https://www.cryptoaltruism.org/blog/donate-cryptocurrency-to-support-ukraine

**Leçon** : Un État peut faire ce qu'une cellule clandestine ne peut pas : ouvrir des comptes bancaires publics, déclarer les fonds, utiliser les exchanges régulés. La transparence ici est une force, pas une faiblesse. Cette approche n'est pas reproductible pour une structure clandestine.

---

## §6 Tableau comparatif

| Mécanisme | Traçabilité | Risque légal | Capacité volume | Complexité |
|-----------|------------|-------------|-----------------|------------|
| Association loi 1901 | Haute (compte bancaire, SIRET, préfecture) | Faible si activité réelle | 2 000-5 000€/mois | Faible |
| SCIC | Haute (RCS, comptes déposés) | Faible si activité réelle | 5 000-50 000€/mois | Moyenne |
| Fond de dotation | Haute (contrôle préfectoral) | Faible si objet réel | 5 000-20 000€/mois | Moyenne |
| Caisse de grève (syndicale) | Moyenne (compte bancaire, mais flux justifiés par l'activité sociale) | Faible si syndicat réel | 2 000-10 000€/mois | Faible |
| Monero + P2P exit | Théoriquement basse, mais présomption 324-1-1 CP | CRITIQUE (présomption de blanchiment) | 1 000-8 000€/mois | Élevée |
| Bitcoin mixer | Haute (tracé Chainalysis, illégal) | CRITIQUE (blanchiment aggravé 10 ans) | Variable | Moyenne |
| Cash multi-donateurs | Très basse (pas de trace) | Moyenne (structuring, 1 000€ plafond) | < 3 000€/mois pratique | Élevée |
| Prêt entre particuliers | Moyenne (<5 000€ sans déclaration) | Faible si déclaré >5 000€ | 5 000€/mois (multiples < 5k) | Faible |
| Cartes prépayées | Haute (identifiées depuis 2020) | Faible si KYC | < 1 000€/mois | Très faible |
| SEL | Très basse (hors système monétaire) | Nulle si non-professionnel | 0€ (pas d'euros) | Faible |

---

## §7 Analyse synergique : La combinaison la moins pire

Aucun mécanisme pris isolément ne permet de déplacer 8 150€/mois sans risque. La seule approche viable est une combinaison :

**Pilier A (30% du besoin = 2 445€/mois) : Prêts entre particuliers déclarés.** 5 prêteurs différents prêtant 489€/mois chacun (< 5 000€/an, seuil de déclaration fiscale). Pas de déclaration aux impôts. Remboursement différé à N+5 ans. Cadre légal : art.1892 CC.

**Pilier B (30% = 2 445€/mois) : Caisse de solidarité associative ouverte.** Association loi 1901 déclarée en préfecture avec objet social authentique (ex: "éducation populaire", "entraide numérique"). Collecte via HelloAsso (plateforme française, conforme RGPD et LCB-FT). Les donateurs reçoivent un reçu fiscal (réduction d'impôt 66%). Le flux est justifié par l'objet social. Les fonds sont réalloués via des prestations de service facturées.

**Pilier C (25% = 2 037€/mois) : Cash lors d'événements physiques.** Collecte d'espèces lors de rassemblements, conférences, ateliers. Plafond de 1 000€ par participant. Dépôt en banque par tranches < 1 000€ (risque de structuring, mais acceptable si justifié par l'activité associative).

**Pilier D (15% = 1 223€/mois) : Crypto (Monero via Bisq P2P) pour les donateurs tech.** Risque 324-1-1 CP accepté par le donneur. Conversion en euros via P2P (pas d'exchange centralisé). Impact limité en volume pour minimiser l'exposition.

**Mise en garde** : Article 450-1 CP (association de malfaiteurs) : 10 ans d'emprisonnement si les infractions préparées sont punies de 10 ans. Le simple fait d'organiser un système de financement contournant TRACFIN peut être qualifié d'association de malfaiteurs, même si aucune infraction sous-jacente n'est commise. Source : https://boutique.lamy-liaisons.fr/ressources/association-de-malfaiteurs-que-dit-le-code-penal.html

---

## §8 Fact Registry

| F | Donnée | Source |
|---|--------|--------|
| F001 | Plafond espèces France : 1 000€ entre particulier et professionnel | https://www.banque-france.fr/fr/aide-faq/Moyens%20de%20paiement |
| F002 | Aucun plafond espèces entre particuliers | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000022361055 |
| F003 | Déclaration de prêt obligatoire aux impôts si > 5 000€ | https://www.service-public.gouv.fr/particuliers/vosdroits/F1059 |
| F004 | TRACFIN a reçu 215 410 déclarations en 2024, +13.2% | https://risqueblanchiment.fr/articles/tracfin-bilan-2025-declarations-soupcon |
| F005 | ERMES obligatoire depuis 1er février 2025 | https://www.caceis.com/regwatch/january-2025 |
| F006 | Article 324-1-1 CP : présomption de blanchiment pour crypto anonyme | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051743092 |
| F007 | Monero est le privacy coin le plus robuste techniquement | https://www.elliptic.co/blockchain-basics/what-are-privacy-coins |
| F008 | Delistage XMR sur Binance et Kraken UE (2024) | https://ccn.com/education/crypto/countries-banning-privacy-coins-monero-zcash-2026/ |
| F009 | 1 417 SCIC actives en France en 2024 | https://pro.orange.fr/lemag/scic-societe-cooperative-d-interet-collectif-definition-avantages-et-inconvenients-CNT000002oifCp.html |
| F010 | Spark Alliance HK : 9M$ gelés, 4 arrestations (2019) | https://www.cnn.com/2019/12/20/asia/hong-kong-protests-money-frozen-intl-hnk/ |
| F011 | Navalny : 300 000$ en Bitcoin en 2021, 840 000$ en 2022 | https://www.reuters.com/world/bitcoin-donations-surge-jailed-kremlin-critic-navalnys-cause-data-2021-02-11/ |
| F012 | Art.450-1 CP : association de malfaiteurs jusqu'à 10 ans | https://boutique.lamy-liaisons.fr/ressources/association-de-malfaiteurs-que-dit-le-code-penal.html |
| F013 | Art.324-1 CP : blanchiment simple 5 ans + 375 000€ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051743092 |
| F014 | KYC obligatoire sur tous les PSAN français (MiCA + 5e directive) | https://regulaforensics.com/blog/kyc-crypto |
| F015 | LOPMI 2023 : vidéosurveillance IA, algorithmes anti-structuring | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000047046768/ |

---

## §9 ANNEXE : Toutes les URLs

Banque de France - Moyens de paiement : https://www.banque-france.fr/fr/aide-faq/Moyens%20de%20paiement

Service Public - Paiement en espèces : https://www.service-public.gouv.fr/particuliers/vosdroits/F10999

Service Public - Déclaration prêt entre particuliers : https://www.service-public.gouv.fr/particuliers/vosdroits/F1059

Legifrance - Code monétaire et financier art. L112-6 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000022361055

TRACFIN bilan 2025 : https://risqueblanchiment.fr/articles/tracfin-bilan-2025-declarations-soupcon

RiskSonnar - Guide déclaration TRACFIN 2026 : https://www.risksonnar.com/blog/tracfin-declaration-soupcon-guide

Global Law Experts - TRACFIN déclaration : https://globallawexperts.com/how-do-i-make-a-tracfin-declaration

CACEIS - RegWatch janvier 2025 (décret ERMES) : https://www.caceis.com/regwatch/january-2025

Elliptic - Privacy coins : https://www.elliptic.co/blockchain-basics/what-are-privacy-coins

TRM Labs - Monero traceability : https://www.trmlabs.com/resources/blog/the-rise-of-monero-traceability-challenges-and-research-review

CCN - 10 countries banning privacy coins 2026 : https://ccn.com/education/crypto/countries-banning-privacy-coins-monero-zcash-2026/

CoinBureau - Top privacy coins 2026 : https://coinbureau.com/analysis/top-privacy-coins

Legifrance - Article 324-1 CP : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051743092

Lamy Liaisons - Association de malfaiteurs art.450-1 : https://boutique.lamy-liaisons.fr/ressources/association-de-malfaiteurs-que-dit-le-code-penal.html

Lexbase - Blanchiment art.324-1 : https://www.lexbase.fr/encyclopedie-juridique/etude-le-blanchiment/8054269-8054359

AMF - AML regulation : https://www.amf-france.org/en/news-publications/depth/money-laundering

RegulaForensics - KYC crypto 2026 : https://regulaforensics.com/blog/kyc-crypto

ShuftiPro - KYC crypto exchanges 2026 : https://shuftipro.com/blog/kyc-crypto-exchanges-regulations-requirements

Service Public - Associations et fonds de dotation : https://www.service-public.gouv.fr/particuliers/vosdroits/N31931

Village Justice - Fonds de dotation vs association : https://www.village-justice.com/articles/fonds-dotation-association-loi-1901-quelle-difference,39354.html

Les Scop - Tout savoir sur les SCIC : https://www.les-scop.coop/les-scic

Bpifrance Création - SCIC : https://bpifrance-creation.fr/encyclopedie/structures-juridiques/structures-less/scic-societe-cooperative-dinteret-collectif

Orange Pro - SCIC chiffres 2024 : https://pro.orange.fr/lemag/scic-societe-cooperative-d-interet-collectif-definition-avantages-et-inconvenients-CNT000002oifCp.html

France Insoumise - Caisse de grève : https://lafranceinsoumise.fr/caisse-de-greve-insoumise-2025/

CGT - Caisse de solidarité : https://cgtbressuire.fr/index.php/2025/09/30/caisse-de-solidarite-avec-les-grevistes/

SNES-FSU - Fonds de solidarité : https://www.snes.edu/agissons/outils/greve-fonds-de-solidarite/

La finance pour tous - Prêt familial : https://www.lafinancepourtous.com/pratique/credit/autres-types-de-credit/pret-familial-ou-amical

Acocia-Agaps - Prêt entre particuliers fiscalité 2026 : https://acocia-agaps.com/blog/pret-entre-particuliers-regles-et-fiscalite

France Immo Plus - Tontine interdite : https://www.france-immoplus.fr/tontine-interdite-france/

Bloomberg - HK Spark Alliance cash : https://www.bloomberg.com/news/articles/2019-12-20/mysterious-bags-of-cash-trigger-major-hong-kong-protest-arrests

CNN - HK police freeze 9M : https://www.cnn.com/2019/12/20/asia/hong-kong-protests-money-frozen-intl-hnk/

Wikipedia - Spark Alliance : https://www.sparkalliance.org/

Reuters - Navalny Bitcoin donations : https://www.reuters.com/world/bitcoin-donations-surge-jailed-kremlin-critic-navalnys-cause-data-2021-02-11/

Moscow Times - Russian opposition Bitcoin : https://www.themoscowtimes.com/2021/02/11/russian-opposition-finds-refuge-in-bitcoin-a72907

Crypto Altruism - Ukraine crypto donations : https://www.cryptoaltruism.org/blog/donate-cryptocurrency-to-support-ukraine

Legifrance - LOPMI 2023 : https://www.legifrance.gouv.fr/loda/id/JORFTEXT000047046768/

Verspieren - Impact LOPMI cyber : https://www.verspieren.com/article/consequences-loi-lopmi-assurance-risques-cyber

ICLG - Anti-Money Laundering France 2026 : https://iclg.com/practice-areas/anti-money-laundering-laws-and-regulations/france

Eversheds Sutherland - France AML Guide : https://ezine.eversheds-sutherland.com/global-aml-guide/france

LegalStart - Encaissement espèces entreprise : https://www.legalstart.fr/fiches-pratiques/banque/encaissement-especes-entreprise

---

## §X LIMITES — Ce que le financement invisible ne resout pas

1. **Volumetrie** : deplacer 8 000€/mois est possible (cash + crypto + prets). Deplacer 80 000€/mois (expansion scenario 3) l'est beaucoup moins.
2. **Dependance crypto** : Monero est plus anonyme mais illiquide et interdit par les echangeurs europeens (reglementation 2025). Le cash est liquide mais detectable a grande echelle.
3. **Risque penal** : toutes les methodes decrites sont illegales (blanchiment art.324-1, AM art.450-1, financement terroriste art.421-1).
4. **Preuve numerique** : la blockchain est un registre public. Les transactions Monero sont anonymes mais l'analyse de chaine (Chainalysis) progresse.

---

## §XI FAISCEAUX — Connexions P1-P9

| Faisceau | FINANCEMENT INVISIBLE | Investigation |
|----------|------------------------|---------------|
| FINANCEMENT + INVISIBLE | Les solutions concretisent les budgets de P11-FINANCEMENT | P11-FINANCEMENT : 6 050-8 150€/mois a deplacer |
| RISQUE + INVISIBLE | Toutes les methodes sont illegales | P10-RISQUE : art.324-1, 450-1, 421-1 |
| EMPIRIQUE + INVISIBLE | Les methodes doivent etre testees | P9-EMPIRIQUE : simulation de detection TRACFIN |
| CAS + INVISIBLE | Le financement est la condition du sanctuaire | P8-CAS : un sanctuaire exige un budget invisible |
| MODELE + INVISIBLE | L'autonomie communautaire a besoin de fonds invisibles | PX-NON-ESCALADE : le modele non-escalade exige un budget |
| PUITS + INVISIBLE | La SCIC peut etre le receptacle legal du financement invisible | PX-PUITS-DROIT : le puits comme interface financement legal/clandestin |
| SUCCESSION + INVISIBLE | Un DAO dead man's switch peut transferer les fonds automatiquement | PX-SUCCESSION : la continuite financiere en cas d'arrestation |
| DROIT COMPARE + INVISIBLE | Le Benelux a des regles de blanchiment differentes | PX-DROIT-COMPARE : comparer les plafonds especes France/Benelux |
| ACE + INVISIBLE | L'action acephale a besoin de fonds sans leader identifie | ACE-INVESTIGATION : financement acephale = financement invisible |
| OLI + INVISIBLE | Le verrou financier (mecanisme 10 d'OLI) est contourne par l'invisible | OLI-INVESTIGATION : l'argent invisible comme trou dans la machine |
| PSYCHO + INVISIBLE | La securite financiere reduit le stress militant | P7-PSYCHO : ne pas s'inquieter de l'argent libere l'action |

---

## §XII SUSPICION_SCORE — Auto-critique du financement invisible

**Score composite : 4.5/10**

| Critère | Score | Justification |
|---------|:-----:|---------------|
| Sources techniques (TRACFIN, LOPMI, Monero) | 6/10 | Procedures documentees mais hors contexte militant |
| Test empirique | 1/10 | Aucune methode testee en contexte repressif francais |
| Contre-exemples (crypto tracee, cash detecte) | 4/10 | Les limites sont citees mais pas explorees en profondeur |
| Falsifiabilite | 5/10 | Si TRACFIN detecte le flux, la methode est invalide — mesurable |
| Auto-critique | 6/10 | 4 limites mais pas de critique de la volumetrie reelle |

**Biais identifiés :**
1. **Biais techno-optimiste** : Monero et crypto sont presentes comme anonymes — Chainalysis progresse
2. **Biais penal** : toutes les methodes sont illegales — le fichier normalise l'infraction
3. **Biais de volumetrie** : 8 000€/mois est possible, 80 000€/mois ne l'est pas — l'ecart n'est pas assez souligne
4. **Biais de detection** : les algorithmes bancaires (LOPMI 2023) detectent le structuring — le fichier le mentionne mais le minimise

---

## §XIII SOURCES & FACTS ADDITIONNELS

| ID | Fait | Fiabilité |
|----|------|:---------:|
| F-FINV-001 | TRACFIN a recu 215 410 declarations en 2024 (+13.2%) | ✦ |
| F-FINV-002 | Le plafond especes entre particulier et professionnel est de 1 000€ | ✦ |
| F-FINV-003 | Les algorithmes de scoring bancaire detectent le structuring depuis LOPMI 2023 | ✧ |
| F-FINV-004 | Monero est plus anonyme que BTC mais bloque par les echangeurs europeens | ✧ |
| F-FINV-005 | Aucune methode de financement invisible n'a ete testee en contexte repressif francais | ✧ |
