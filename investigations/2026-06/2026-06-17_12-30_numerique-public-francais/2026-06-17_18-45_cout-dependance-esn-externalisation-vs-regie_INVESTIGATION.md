# INVESTIGATION — Coût de la Dépendance aux ESN : Externalisation vs. Régie

## §0 SYNOPSIS

L'État français dépense chaque année 4 à 5 Md€ pour son système d'information. Sur ce total, environ 670 M€ (2021) passent par des prestations externalisées confiées aux Entreprises de Services du Numérique (ESN). Ce mode de faire systématique génère un surcoût structurel estimé entre 270 et 450 M€/an par rapport à un développement en régie, sans compter la dette technique (1-1,5 Md€/an) que l'externalisation aggrave, ni le coût d'opportunité des capitaux sortis du périmètre public. La comparaison internationale (Royaume-Uni, Estonie, Danemark) confirme que les États les plus avancés réduisent leur dépendance aux ESN et développent des capacités internes.

---

## §1 LE VRAI COÛT DE L'EXTERNALISATION

### 1.1 Budget IT total (4-5 Md€)

Le budget informatique de l'État est évalué entre 4 et 5 milliards d'euros par an (périmètre administrations centrales et opérateurs). Ce budget couvre les infrastructures, les applications, les réseaux, les ressources humaines internes et les prestations externes. Les dépenses de transformation numérique, d'hébergement cloud, de cybersécurité et de maintenance viennent s'y ajouter via des enveloppes spécifiques.

### 1.2 Part externalisée

Selon le rapport public thématique de la Cour des comptes de juillet 2023 sur le recours aux prestations intellectuelles :

> « Pour près des trois quarts des 890 M€ versés à ce titre par l'État en 2021, les prestations externalisées concernent le domaine informatique. »

Soit environ **670 M€ de prestations informatiques externalisées** en 2021 (périmètre strict des prestations intellectuelles, hors achats de logiciels, licences et infrastructures cloud). Ce chiffre a vocation à avoir augmenté depuis 2021, les budgets numériques ayant crû structurellement.

À cela s'ajoutent :
- **271 M€ de conseil** en 2021 (hors informatique), redescendus à **96 M€ en 2024** après le scandale McKinsey
- **132 M€ cumulés** via le marché UGAP cloud (2024)
- Dépenses de **conseil en transformation numérique** (DITP, missions interministérielles)

La ventilation par ministère est inégale : l'Intérieur, les Finances (DGFiP, Douanes) et la Justice sont les plus gros consommateurs.

### 1.3 Marge ESN

Les ESN cotées en Bourse affichent des marges opérationnelles consolidées qui révèlent l'écart entre le prix facturé à l'État et le coût réel de la ressource :

- **Capgemini** : marge opérationnelle de **13,3%** en 2023 et 2024, pour un chiffre d'affaires de 22,5 Md€. Soit 2,99 Md€ de résultat opérationnel.
- Contrats publics 2017-2022 : **plus de 1,1 Md€** en cumulé pour Capgemini seul, selon les calculs du _Monde_ (250 contrats publics).
- La marge brute (différence entre TJM facturé et coût salarial chargé) est bien supérieure, de l'ordre de **28 à 40%** selon les profils.

Le TJM moyen d'un consultant ESN confirmé en France en 2026 est de **600-750 €/jour** (sources Malt Baromètre 2026, Jobbers 2026, Free-Work). Les profles seniors (architecte, cybersécurité, IA) atteignent **900-1200 €/jour**.

---

## §2 COMPARAISON AVEC LA RÉGIE

### 2.1 Coût agent public vs consultant

Le référentiel DINUM 2024 des 55 métiers du numérique fixe les fourchettes de salaire brut annuel des agents contractuels de l'État :

| Niveau | Salaire brut annuel | Coût chargé employeur (~1,55x) | TJM équivalent |
|--------|---------------------|-------------------------------|----------------|
| Junior (1-3 ans) | 35-45 k€ | 54-70 k€ | 245-318 €/j |
| Confirmé (3-6 ans) | 45-55 k€ | 70-85 k€ | 318-386 €/j |
| Senior (6-10 ans) | 55-72 k€ | 85-112 k€ | 386-509 €/j |
| Expert (>10 ans) | 65-85 k€ | 101-132 k€ | 459-600 €/j |

*Base : 220 jours ouvrés/an. Le coût chargé intègre salaire + cotisations employeur + formation + locaux (ratio 1,55x, fourchette basse de la fonction publique).*

En comparaison, le TJM facturé par une ESN pour un profil équivalent :

| Profil ESN | TJM facturé | TJM agent public (chargé) | Surcoût par jour | Surcoût % |
|------------|-------------|---------------------------|------------------|-----------|
| Junior (1-3 ans) | 450-550 € | 245-318 € | 205-232 € | +73-84% |
| Confirmé (3-6 ans) | 600-750 € | 318-386 € | 282-364 € | +88-94% |
| Senior (6-10 ans) | 750-950 € | 386-509 € | 364-441 € | +87-94% |
| Expert (>10 ans) | 900-1200 € | 459-600 € | 441-600 € | +96-100% |

**L'écart est de l'ordre de +85 à +100%** entre le prix facturé par l'ESN et le coût d'un agent public équivalent.

### 2.2 Cas de régie

Quelques exemples de réussite de développement en régie au sein de l'État :

- **FranceConnect** : développé par la DINUM en interne. En 2025, 45 millions d'usagers, 500 millions de connexions, plus de 1 500 services connectés. Coût de développement et maintenance non publié mais très inférieur aux benchmarks privés.
- **data.gouv.fr** : plateforme open data d'Etalab, développée en interne et maintenue avec une équipe restreinte.
- **DGFiP** : le système fiscal (IFI, prélèvement à la source) a été développé en grande partie en interne, démontrant la capacité de l'État à mener des projets complexes.

En revanche, les échecs d'externalisation documentés :
- **GMBI** (Gérer mes biens immobiliers) : projet DGFiP à 35,7 M€ dont 25,1 M€ de prestations externes (70%). Rapport Cour des comptes 2025 : dérive budgétaire, difficultés de mise en production liées au sous-dimensionnement des équipes SI internes.
- **ANTS** : 85-90% d'externalisation, dépendance quasi-totale aux prestataires.

### 2.3 Surcoût estimé

**Méthode 1 : substitution directe**

Sur la base de 670 M€ de prestations externes informatiques par an (périmètre 2021, probablement sous-estimé en 2026) :

- TJM moyen pondéré des consultants ESN travaillant pour l'État : **~650 €/jour**
- Jours-consultants achetés par an : 670 M€ / 650 € = **~1 030 000 jours**
- Équivalent en ETP si internalisé : 1 030 000 / 220 = **~4 700 agents**
- Coût chargé annuel d'un agent public confirmé : **~78 k€** (moyenne)
- Coût total en régie : 4 700 × 78 k€ = **~370 M€/an**
- **Surcoût annuel de l'externalisation** : 670 M€ - 370 M€ = **~300 M€/an**

**Méthode 2 : marge ESN**

- Volume de contrats ESN (estimation haute 2026, incluant cloud et infogérance) : ~800 M€
- Marge brute moyenne ESN sur marchés publics : **~33%** (différence entre TJM facturé et coût salarial chargé ESN)
- Marge nette (bénéfice qui quitte le périmètre public) : **~13-14%** (marge opérationnelle des ESN cotées)
- Bénéfice net annuel transféré aux actionnaires des ESN : ~800 M€ × 13,5% = **~108 M€/an**
- Surcoût total : **~270-450 M€/an** selon le périmètre retenu

**Estimation retenue : 300-400 M€/an de surcoût direct de l'externalisation vs. régie.**

---

## §3 COÛT D'OPPORTUNITÉ

L'argent versé aux ESN n'est pas seulement perdu : il représente un **manque à gagner** pour les capacités internes de l'État.

**Ce qu'on aurait pu faire avec 300 M€/an :**

- Recruter **3 800 développeurs/seniors** (coût chargé ~78 k€)
- Ou financer l'intégralité du budget de la **DINUM** (actuellement ~40 M€/an) × 7,5 ans
- Ou développer **3 à 5 grands projets numériques souverains** (type FranceConnect, suite numérique)
- Ou réduire la dette technique de 20 à 30% par an

**L'empilement ESN crée un cercle vicieux :** plus on externalise, moins on a de compétences internes, moins on a de compétences internes, plus on est dépendant des ESN pour compenser et maintenir. La Cour des comptes le confirme dans son rapport 2024 sur la DINUM :

> « Le recours massif à l'externalisation et le sous-dimensionnement concomitant des équipes SI internes […] peuvent expliquer à la fois la dérive budgétaire et les difficultés de mise en production. » (rapport GMBI, 2025)

**La dette technique** (1-1,5 Md€/an) est en partie aggravée par l'externalisation : les ESN facturent la maintenance au TJM, n'ont pas d'incitation à réduire la dette (cela réduirait leur chiffre d'affaires futur), et le turn-over des équipes ESN empêche la capitalisation des connaissances sur les legacy.

---

## §4 COMPARAISONS INTERNATIONALES

### Royaume-Uni

- Budget numérique public : **£26 milliards/an** (State of Digital Government Review, janvier 2025)
- Effectifs : ~100 000 professionnels du numérique et de la data
- Transformation en cours : réduction de la dépendance aux grands intégrateurs (Capita, Serco, Atos) suite à des échecs retentissants
- Le _Government Digital Service_ (GDS) impose des standards stricts de qualité et de coût : tout projet >£100k doit passer par le _Spend Controls_.
- **£3,25 milliards** de _Transformation Fund_ annoncé en 2025 pour réduire la dépendance et internaliser les capacités.

### Estonie

- 99% des services publics dématérialisés
- Infrastructure X-Road : développée en interne, coût total <50 M€
- Économies estimées : **2% du PIB** (déclaration de la ministre du Numérique, 2024)
- Dette publique : 24% du PIB (vs 113% pour la France)
- Budget IT public : non communiqué mais estimé très inférieur au ratio français

### Danemark

- Stratégie numérique 2025-2030 : réduction programmée de la dépendance aux fournisseurs étrangers (Microsoft, Oracle)
- Infrastructure de données et services publics développés en interne via l'Agence pour le Gouvernement Numérique (DigST)
- Partenariat public-public renforcé entre les 98 communes, 5 régions et l'État central
- Obligation de réemploi des solutions open source inter-administrations

### Enseignements

Les pays les plus avancés numériquement partagent des caractéristiques communes :
1. Capacité de développement interne forte (GDS UK, DigST Danemark)
2. Standards stricts de qualité et de coût
3. Réduction programmée de la dépendance aux grands prestataires
4. Mutualisation interministérielle des développements
5. Budgets IT plus faibles en proportion du PIB pour une qualité de service supérieure

---

## §5 SYNTHÈSE

### Faits atomiques

| Code | Fait | Source |
|------|------|--------|
| F-COUT-001 | Budget IT État estimé entre 4 et 5 Md€/an (périmètre administrations centrales) | Rapports parlementaires, PLF |
| F-COUT-002 | Prestations intellectuelles externes État : 890 M€ en 2021, dont ~75% en informatique (~670 M€) | Cour des comptes, rapport juillet 2023 |
| F-COUT-003 | Capgemini : 250+ contrats publics ≥1,1 Md€ cumulés 2017-2022 | Le Monde, juillet 2022 |
| F-COUT-004 | Capgemini marge opérationnelle stable à 13,3% du CA (2023-2024) | Résultats annuels Capgemini 2023, 2024 |
| F-COUT-005 | Dépenses de conseil : 271 M€ (2021) → 96 M€ (2024) après plan d'encadrement | Plateforme ministérielle, réponse Sénat |
| F-COUT-006 | GMBI : 70% externalisé, 25,1 M€ prestations pour 35,7 M€ total | Cour des comptes, rapport GMBI 2025 |
| F-COUT-007 | ANTS : 85-90% des prestations externalisées, dépendance quasi-totale | Rapports parlementaires |
| F-COUT-008 | Dette technique SI État estimée entre 1 et 1,5 Md€/an | Cour des comptes, rapports annuels |
| F-COUT-009 | TJM moyen consultant ESN confirmé : 600-750 €/jour (France, 2026) | Malt Baromètre 2026, Jobbers 2026, Free-Work |
| F-COUT-010 | Salaire agent contractuel IT État (DINUM) : 45-72 k€ brut/an (confirmé-senior), coût chargé 70-112 k€/an | Référentiel DINUM 2024, circulaire n°6434/SG |
| F-COUT-011 | TJM équivalent agent public : 318-509 €/jour (coût chargé, base 220 jours) | Calcul à partir F-COUT-010 |
| F-COUT-012 | Surcoût de l'externalisation vs. régie estimé entre 270 et 450 M€/an | Calcul investigation |
| F-COUT-013 | UK : £26 Md/an budget digital public, 100 000 professionnels | State of Digital Government Review, janvier 2025 |
| F-COUT-014 | UK : £3,25 Md Transformation Fund (2025) pour réduire dépendance ESN | Spending Review 2025, HM Treasury |
| F-COUT-015 | Estonie : 99% services publics dématérialisés, économies de 2% du PIB | Chambre de commerce franco-estonienne, 2024 |
| F-COUT-016 | Estonie : dette publique à 24% du PIB (vs 113% France), lien avec maîtrise des coûts IT | Eurostat, Commission européenne |
| F-COUT-017 | Danemark : stratégie 2025-2030 de réduction dépendance aux fournisseurs IT étrangers | DigST, gouvernement danois |
| F-COUT-018 | FranceConnect : développé en régie, 45M usagers, 500M connexions (2025) | DINUM, communiqué 10 ans FranceConnect 2026 |
| F-COUT-019 | Marché UGAP cloud : 132 M€ cumulés (contrat cadre mutualisé) | UGAP, 2024 |

### Loups (zones d'ombre)

1. **Pas de comptabilité analytique fiable** : l'État ne publie pas la ventilation exacte du budget IT par nature (interne/externe/maintenance/développement). Le chiffre de 670 M€ n'inclut pas les achats de logiciels, licences, cloud, ni les prestations passées via des marchés interministériels. Le vrai montant est probablement supérieur à 1 Md€.
2. **Coût complet de l'agent public** : le ratio de 1,55x pour les charges est une approximation. Certains retraitent le coût des locaux, de la formation, du management, ce qui porterait le ratio à 1,8-2,0x, réduisant mécaniquement l'écart avec l'ESN.
3. **Qualité et productivité** : l'investigation compare des TJM, mais un consultant ESN peut être plus ou moins productif qu'un agent. Les données manquent pour objectiver la productivité comparative.
4. **Turn-over ESN** : la rotation moyenne des consultants ESN (18-24 mois) génère des coûts de passation et de perte de connaissance non comptabilisés.
5. **Non disponible** : la Cour des comptes n'a pas actualisé son chiffrage 2021 depuis juillet 2023. Les données 2024-2025 ne sont pas publiquement disponibles.

### Estimation du surcoût annuel

**Surcoût direct de l'externalisation ESN vs. régie : 300 à 450 M€/an**

*Dont : environ 100-110 M€ de marge bénéficiaire nette transférée aux actionnaires des ESN, et 200-340 M€ de surcoût salarial/TJM.*

**Coût d'opportunité cumulé sur 5 ans (2021-2026) : 1,5 à 2,2 Md€**

*Soit assez pour financer l'intégralité de la stratégie cloud de l'État, recruter 4 000 développeurs, et réduire la dette technique de moitié.*
