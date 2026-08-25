# KERNEL INVESTIGATION: Comparaison des stratégies cloud souverain — Allemagne, Suède, Belgique vs France

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0915-COMPARAISON-CLOUD |
| Type | KERNEL COMPLEX |
| Date | 2026-08-25 09:15 CEST |
| Gate | pending |
| Statut | COMPLETED |

---

## 1. BRIEF

**Question :** Comment les stratégies cloud souverain de l'Allemagne, de la Suède et de la Belgique se comparent-elles au modèle français S3NS/Bleu ?

**Verdict : La France est le pays le plus avancé dans le verrouillage réglementaire — et le plus dépendant des hyperscalers US sous couvert de souveraineté. L'Allemagne a une approche multicloud pragmatique avec de vraies alternatives (STACKIT, IONOS, Deutschland-Stack). La Suède et la Belgique sont en retard institutionnel mais abritent des acteurs réellement souverains (Safespring, Cleura, Belgian Critical Cloud). Le cadre européen (Cloud Sovereignty Framework SEAL) expose les faiblesses du modèle français.**

---

## 2. TABLEAU COMPARATIF

| Critère | France (S3NS/Bleu) | Allemagne | Suède | Belgique |
|---------|-------------------|-----------|-------|----------|
| **Modèle** | Coquille française + 100% tech US | Multicloud : coquilles US + vraies alternatives | Cloud-first pragmatique, alternatives nordiques | Tender européen + initiative privée BCC |
| **Label** | SecNumCloud (ANSSI) | C5 (BSI), C3A (autonomie) | Aucun label national | Aucun label national |
| **Acteurs US en coquille** | S3NS (Thales/GCP), Bleu (Orange-Cap/Azure) | Delos (SAP/Microsoft), T-Systems/GCP, AWS ESC Brandenburg (direct) | Aucun (Safespring, Cleura = cap 100% EU) | Proximus/S3NS (via tender EU) |
| **Alternatives réelles** | OVHcloud, Scaleway, Outscale (marginalisées) | STACKIT (Schwarz), IONOS, Open Telekom Cloud | Safespring (86,25% SEAL), Cleura, Elastx | Belgian Critical Cloud (Keyes/Cegeka), Proximus |
| **Budget cloud public** | 84 M€ (+62%/an) | 250 M€ (tender BMDS DT/SAP seul) | Non publié (cloud-first sans cadre) | 180 M€/6 ans EU + initiatives nationales |
| **Stratégie IA** | Mistral/Outscale | Deutschland-Stack (DT/SAP/Siemens, 10 000 GPU) | Pas de stratégie IA dédiée | Via AWS ESC Local Zone |
| **Verrouillage** | MAXIMAL (SecNumCloud obligatoire pour données sensibles) | MODÉRÉ (multicloud, BSI C5 non exclusif) | FAIBLE (cloud-first sans préférence souveraine) | ÉMERGENT (framework SEAL appliqué) |

---

## 3. ALLEMAGNE — Le pragmatisme multicloud

### 3.1 Architecture

L'Allemagne ne croit pas au modèle de la coquille unique. Sa stratégie est multicloud par construction :

1. **Delos Cloud** (SAP + Microsoft) : équivalent allemand de Bleu. Hyperscaler Microsoft Azure opéré par une entité allemande, certifié BSI C5, destiné à l'administration fédérale. SAP est l'actionnaire (comme Orange/Capgemini pour Bleu). Microsoft est le partenaire technologique exclusif.

2. **Thales/Google Cloud Allemagne** (mai 2026) : réplique du modèle S3NS, dédiée au marché allemand. Entité allemande détenue et contrôlée par Thales. Google Cloud fournit la technologie. Cible les certifications BSI C5 et C3A. Offre de « geo-redundancy » transfrontalière France-Allemagne (première mondiale).

3. **AWS European Sovereign Cloud** (Brandenburg, janvier 2026) : 7,8 Md€ d'investissement. Entité AWS dédiée, staff EU-only, infrastructure physiquement et logiquement séparée. Ce n'est PAS une coquille — c'est AWS directement, mais en version « souveraine ». Le gouvernement allemand (ministre Wildberger) le présente comme un succès de souveraineté.

4. **Vraies alternatives allemandes** : STACKIT (groupe Schwarz/Lidl, 100 % allemand), IONOS (100 % européen), Open Telekom Cloud (Deutsche Telekom). Ces acteurs ne dépendent d'aucune technologie US.

5. **Deutschland-Stack** : le projet le plus ambitieux. DT + SAP + Siemens. 10 000 GPU Nvidia à Munich. Tender BMDS de 250 M€ remporté en mai 2026 (après retrait du recours Google Cloud/Adesso). Plateforme PaaS pour l'IA publique allemande. Infrastructure contrôlée, scalable, interopérable. Première application : KIPITZ (traitement documentaire IA pour l'administration).

### 3.2 Forces

- **Multicloud réel** : l'administration allemande peut choisir entre 6+ offres (Delos, Thales/GCP, AWS ESC, STACKIT, IONOS, Open Telekom Cloud). Pas de duopole.
- **Alternatives crédibles** : STACKIT et IONOS ne sont pas des coquilles. Ce sont des clouds construits sur des technologies propres.
- **Deutschland-Stack** : investissement dans la capacité industrielle européenne, pas dans l'intermédiation.
- **BSI C5 plus pragmatique que SecNumCloud** : certification de sécurité, pas d'exigence de souveraineté juridique absolue. Moins de verrouillage, plus de concurrence.

### 3.3 Faiblesses

- **AWS ESC = AWS** : le gouvernement allemand célèbre l'arrivée d'AWS en Brandenburg comme une victoire de souveraineté. C'est l'équivalent de célébrer l'ouverture d'une base militaire américaine comme une victoire de l'indépendance nationale. Même staff EU, même entité dédiée — mais le code, la propriété intellectuelle, les mises à jour viennent de Seattle.
- **Delos = Bleu** : même modèle, mêmes limites. 100 % Microsoft sous le capot.
- **C3A n'est pas SecNumCloud** : le standard allemand d'« autonomie cloud » (C3A) est moins contraignant juridiquement que SecNumCloud. Il évalue la sécurité, pas l'indépendance.

---

## 4. SUÈDE — Le pragmatisme sans cadre

### 4.1 Une politique cloud-first... sans préférence souveraine

La Suède a publié sa première politique cloud en mai 2026 : « Strengthened Digital Sovereignty and Reduced Vendor Lock-in » (DIGG). Le document pose des principes pour l'usage du cloud par l'administration, mais **n'impose pas de label national, n'exclut pas les hyperscalers US, et ne subventionne pas d'offre « souveraine ».**

C'est l'approche la plus libérale des quatre pays : cloud-first pour l'innovation, confiance dans le marché pour la sécurité.

### 4.2 Safespring — le champion réellement souverain

Safespring (Stockholm) est un cloud 100 % suédois, 100 % open source, self-assessment SEAL de 86,25 %. Scores SEAL : SOV-1 (stratégique) = 4, SOV-2 (juridiction) = 4, SOV-3 (données) = 4, SOV-4 (opérationnel) = 4, SOV-5 (supply chain) = 2 (seul point faible : hardware non-européen inévitable), SOV-6 (technologie) = 3, SOV-7 (sécurité) = 4, SOV-8 (environnement) = 4.

Safespring a volontairement publié ses scores SEAL — seul fournisseur européen à le faire. **C'est l'antithèse exacte de S3NS/Bleu : tout est open source, tout est auditable, tout est public.**

Mais Safespring est un petit acteur. La commande publique suédoise reste dominée par AWS, Azure et GCP.

### 4.3 Forces

- **Safespring, Cleura, Elastx** : des clouds réellement souverains, sans technologie US.
- **Pragmatisme** : pas de verrouillage réglementaire, les administrations choisissent librement.
- **Transparence** : Safespring publie ses scores SEAL. Aucun acteur français ne le fait.

### 4.4 Faiblesses

- **Pas de stratégie nationale contraignante** : « cloud-first » signifie souvent « AWS-first ».
- **Pas d'alternative crédible à l'échelle** : Safespring est un nain face aux hyperscalers.
- **Pas de label national** : aucune certification type SecNumCloud ou C5. La souveraineté est une déclaration d'intention, pas une obligation.

---

## 5. BELGIQUE — Le laboratoire du cadre européen

### 5.1 Le tender Proximus/S3NS : la Commission valide le modèle français

Le 17 avril 2026, la Commission européenne a attribué un contrat-cadre de 180 M€ sur 6 ans à quatre fournisseurs : Post Telecom (Luxembourg), STACKIT (Allemagne), Scaleway (France), et un consortium mené par **Proximus (Belgique) incluant S3NS.**

C'est la première application du Cloud Sovereignty Framework (SEAL). Le seuil minimal était SEAL-2. Proximus l'a atteint en s'appuyant sur S3NS — c'est-à-dire sur Google Cloud Platform.

**Implication majeure : la Commission européenne a labellisé « souverain » un service dont la technologie sous-jacente est 100 % américaine (GCP). C'est une validation du modèle français au niveau européen — et un précédent qui sanctuarise les coquilles S3NS/Bleu comme offre « souveraine » qualifiable.**

### 5.2 Belgian Critical Cloud (BCC) : l'alternative 100 % belge

Keyes et Cegeka ont lancé le « Belgian Critical Cloud » (BCC) en mai 2026 : un cloud privé dédié aux infrastructures critiques belges. Pas de technologie US, pas de dépendance extraterritoriale. Mais c'est une initiative privée, pas une commande publique.

### 5.3 AWS ESC Local Zone en Belgique

AWS a annoncé en janvier 2026 l'extension de l'European Sovereign Cloud vers la Belgique via une Local Zone. Le gouvernement belge (vice-Premier ministre Clarinval) a salué l'investissement comme « une étape importante pour les entreprises et le secteur public belges. »

### 5.4 Forces

- **Adoption du framework SEAL** : la Belgique est le premier pays à appliquer concrètement le cadre européen via le tender Proximus/S3NS.
- **Belgian Critical Cloud** : une alternative réelle, souveraine, pour les infrastructures critiques.
- **Position géographique** : hub européen, attire les investissements (AWS, Google, Proximus).

### 5.5 Faiblesses

- **Le tender Proximus/S3NS valide le modèle de la coquille US** : SEAL-2 permet explicitement « des dépendances non-européennes matérielles » et « un contrôle indirect par des tiers non-européens ». La France a réussi à imposer son modèle au niveau européen.
- **Pas de stratégie nationale** : la Belgique suit le cadre européen sans politique propre.
- **Pas de label national** : dépendance au framework SEAL, qui est moins contraignant que SecNumCloud.

---

## 6. ANALYSE TRANSVERSALE

### 6.1 Les quatre modèles

| Pays | Modèle | Verdict |
|------|--------|---------|
| **France** | Coquille unique réglementée (SecNumCloud obligatoire) | Verrouillage maximal au profit de deux fournisseurs, 100 % dépendance US |
| **Allemagne** | Multicloud pragmatique (coquilles + alternatives réelles) | Meilleur équilibre : vraies alternatives disponibles, concurrence préservée |
| **Suède** | Cloud-first libéral (pas de label, confiance dans le marché) | Alternatives réelles existent mais sont marginales. AWS domine. |
| **Belgique** | Laboratoire européen (framework SEAL, tender Commission) | Valide le modèle français au niveau UE tout en gardant des alternatives |

### 6.2 Le piège SEAL-2

Le Cloud Sovereignty Framework européen est une avancée conceptuelle majeure : pour la première fois, la souveraineté est mesurable et opposable dans les marchés publics. Mais le seuil SEAL-2 est un cheval de Troie :

- **SEAL-2 = « EU law applicable and enforceable, with material non-EU dependencies remaining; service, technology or operations under indirect control of non-EU third parties. »**
- Traduction : la loi européenne s'applique, mais des dépendances matérielles non-européennes sont autorisées. Contrôle indirect par des tiers non-européens autorisé.
- **C'est exactement le modèle S3NS/Bleu.**

Le framework était supposé favoriser les clouds réellement européens. En pratique, avec un seuil SEAL-2, il labellise les coquilles US comme « souveraines. » La France a gagné la bataille du cadre réglementaire européen.

### 6.3 La transparence comme marqueur de souveraineté réelle

**Aucun acteur français (S3NS, Bleu, OVHcloud, Scaleway, Outscale) n'a publié son auto-évaluation SEAL.** Le seul fournisseur européen à l'avoir fait est Safespring (Suède).

C'est un test simple de souveraineté réelle : si vous ne publiez pas vos scores de dépendance, c'est que vous avez quelque chose à cacher. La France, qui a le discours de souveraineté le plus fort, est aussi le pays le plus opaque sur la réalité de ses dépendances.

### 6.4 Le Deutschland-Stack : ce que la France aurait dû faire

Le projet Deutschland-Stack (DT + SAP + Siemens, 10 000 GPU, 250 M€) est exactement ce que la France aurait dû construire au lieu de S3NS/Bleu :
- Infrastructure contrôlée
- Technologies européennes (SAP, Siemens)
- Ouvert à l'interopérabilité
- Pas de dépendance à un hyperscaler US pour la couche logicielle
- Investissement dans la capacité industrielle, pas dans l'intermédiation

La France a choisi la location de technologie US avec un drapeau français. L'Allemagne a choisi de construire. Les deux pays dépensent des montants comparables (84 M€/an côté français vs 250 M€ de tender ponctuel côté allemand), mais la destination de l'argent n'est pas la même.

---

## 7. VERDICT

**La France est le pays européen le plus avancé dans la construction d'une façade de souveraineté numérique — et le plus dépendant des États-Unis dans la réalité technologique.**

- L'Allemagne fait mieux sur le fond (multicloud, Deutschland-Stack) mais moins bien sur la forme (AWS ESC célébré comme une victoire).
- La Suède a les acteurs les plus purs (Safespring 86 % SEAL) mais la plus faible volonté politique.
- La Belgique est le laboratoire où le modèle français est en train d'être sanctuarisé au niveau européen via le framework SEAL.

**Le combat n'est plus franco-français. Il est européen. Et pour l'instant, la France est en train de gagner — mais c'est le modèle de la dépendance qui gagne, pas celui de la souveraineté.**

---

## 8. SOURCES

1. AWS, « AWS Launches AWS European Sovereign Cloud », 15 janvier 2026 — https://press.aboutamazon.com/aws/2026/1/aws-launches-aws-european-sovereign-cloud-and-announces-expansion-across-europe
2. Bertelsmann, « First Sovereign Cloud Platform For The German Administration », 23 septembre 2024 — https://www.bertelsmann.com/en/news-and-media/news/first-sovereign-cloud-platform-for-the-german-administration-on-the-home-straight.jsp
3. Insight42, « Sovereign Cloud Germany: Public Sector Guide 2026 », février 2026 — https://insight42.com/sovereign-cloud-germany/
4. RCR Wireless, « German sovereignty play builds — DT/SAP win federal gig, Thales expands Google model », 22 mai 2026 — https://rcrwireless.com/20260522/network-infrastructure/german-sovereignty-builds-dt-sap-thales-google
5. Safespring, « The EU just defined Sovereign Cloud, here is our score », novembre 2025 — https://www.safespring.com/blogg/2025/2025-11-the-eu-just-defined-sovereign-cloud-here-is-our-score/
6. BeLibre, « Europe Measures Digital Sovereignty. Why Doesn't It Publish the Results? », 21 avril 2026 — https://belibre.be/en/sovereignty/2026-04-21-european-sovereign-cloud/
7. European Commission, « Commission advances cloud sovereignty through strategic procurement », 17 avril 2026 — https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en
8. ACA Group, « Digital sovereignty and the public cloud in Belgium », août 2026 — https://acagroup.be/en/blog/digital-sovereignty-and-the-public-cloud-in-belgium-how-do-the-pieces-fit-together
9. Reddit r/BuyFromEU, « Sweden's first cloud policy », mai 2026
10. LinkedIn, Laurence Mathieu, « Belgian Critical Cloud », mai 2026
11. Tech Insider, « Cloud Souverain UE 180 M€ : OVHcloud, Scaleway Écartent AWS », avril 2026 — https://tech-insider.org/fr/cloud-souverain-europe-180-millions-ovhcloud-scaleway-2026/
12. DINUM, « L'État accélère sa transition cloud », 26 mars 2026 — https://www.numerique.gouv.fr/sinformer/espace-presse/etat-transition-cloud-offres-europeennes-souveraines/
13. Cloud Security Alliance, « EU Tech Sovereignty: Cloud Concentration Risk », juin 2026
14. Gartner, « Sovereign cloud spending to triple 2025-2027 », cité par ASEE, avril 2026