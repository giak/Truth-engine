# UE-CENSOR : L'Architecture de la Censure Européenne

## Introduction : Le 3 juin 2024, tout bascule

Ce jour-là, à Gand, en Belgique, un tribunal d'appel rend une décision qui devrait faire trembler les démocraties européennes. La Cour condamne Meta — la maison mère de Facebook — à verser 27 279 euros de dommages et intérêts à Tom Vandendriessche, député européen belge du parti Vlaams Belang.

Le motif ? **Shadowbanning**. Cette pratique de réduction invisible de la portée des publications, sans notification, sans explication, sans possibilité de recours.

Les juges établissent un fait essentiel : du mois de février au mois de décembre 2021, soit pendant près de dix mois, Meta a artificiellement limité la visibilité des publications du député. Pas parce qu'elles enfreignaient la loi. Mais parce qu'elles "soutenaient des individus dangereux et des organisations de haine" selon des critères que Meta seul définissait.

L'affaire révèle l'existence d'une architecture de contrôle massive, sophistiquée, et échappant à tout contrôle démocratique.

Cette enquête documente comment cette architecture s'est construite, organe par organe, sur quatorze ans. Elle s'appuie sur quatorze enquêtes menées avec méthode, croisant des documents officiels de l'UE, des décisions de justice, des études académiques peer-reviewed, des investigations journalistiques, et l'analyse du rapport US House (7,826 lignes, 302 exhibits).

---

## I. Chronologie d'une prise de contrôle (2012-2026)

Tout commence bien avant que l'opinion publique ne réalise ce qui se trame. Voici comment l'architecture de censure européenne s'est construite, organe par organe, sur quatorze ans.

### 2012-2015 : Les fondations

**Décembre 2012** — À Abu Dhabi, capitale des Émirats Arabes Unis, naît Hedayah ("le guide" en arabe). Ce centre d'excellence international contre l'extrêmisme violent est co-fondé par les Émirats Arabes Unis et le gouvernement fédéral américain.

**Décembre 2014** — La Commission européenne verse 5 millions d'euros à Hedayah. L'argent des contribuables européens commence à couler vers Abu Dhabi, avant même que l'Europe ne construise ses propres institutions de modération.

### 2015-2019 : L'institutionnalisation

**4 décembre 2015** — Dans le contexte post-Charlie Hebdo, le commissaire européen Dimitris Avramopoulos (DG HOME) lance l'EU Internet Forum (EUIF). L'objectif affiché : coordonner la lutte contre les contenus terorista en ligne. L'EUIF se présente comme une "plateforme volontaire et complémentaire".

**26 juin 2017** — Quatre géants de la technologie — Meta (Facebook), Microsoft, YouTube (Google) et Twitter (devenu X) — créent le Global Internet Forum to Counter Terrorism (GIFCT). Cette organisation à but non lucratif développe la **Hash-Sharing Database**, une base de données d'empreintes numériques permettant de détecter et supprimer automatiquement du contenu jugé problématique sur toutes les plateformes membres. En 2021, le GIFCT compte 18 entreprises membres. En 2024, elles sont plus de 25.

### 2019-2024 : L'extension

**15 mars 2019** — Un atentat terorista tue 51 personnes dans deux mosquées à Christchurch, en Nouvelle Zélande. Il diffuse son massacre en direct sur Facebook.

**Mai 2019** — Deux mois après Christchurch, le Christchurch Call voit le jour. Cet engagement politique réunit 55 pays et 12 fournisseurs de services en ligne. Objectif affiché : éliminer le contenu terorista et extrémiste violent en ligne.

**C'est aussi en 2019 que l'EUIF étend son périmètre.** La lutte contre le terorismo cède la place à la surveillance du "borderline content" — le contenu "limite", défini comme "légal du point de vue de la legislation terorista, mais nuisible".

**Juin 2023** — Le GIFCT publie un document de 674 lignes intitulé "Borderline Content". Ce document définit quatorze catégories de contenus surveillés. Les quatre dernières — rhétorique populiste, contenu anti-gouvernemental, discours anti-élites, satire politique — ne concernent pas le terorismo mais le discours politique ordinaire, la critique des gouvernements, l'humour politique. Le document précise que "la satire politique est surveillée comme mécanisme de contournement de la censure".

**17 février 2024** — Le Digital Services Act (DSA) entre en vigueur. Cette réglementation permet à l'Union européenne d'infliger des amendes pouvant atteindre 6 % du chiffre d'affaires mondial des plateformes. Le DSA interdit officiellement le shadowbanning. Trois mois plus tard, le tribunal de Gand confirme que Meta pratiquait ce shadowbanning depuis des mois.

### 2024-2026 : La consolidation

**Juillet 2025** — La Commission des affaires judiciaires de la Chambre des représentants des États-Unis publie un rapport : "The Foreign Censorship Threat" (La menace de la censure étrangère). Le rapport accuse le DSA de "contraindre, forcer ou influencer les entreprises à censurer la parole aux États-Unis".

**Avril 2025** — L'Union européenne annonce un nouveau financement de 300 millions d'euros vers le Nigeria, via Hedayah, dans le cadre du programme STRIVE Global. Total des financements UE vers Hedayah : 305 millions d'euros documentés.

**5 décembre 2025** — La Commission européenne inflige une amende de 120 millions d'euros à X (anciennement Twitter) pour violations du Digital Services Act. Les violations établies concernent la conception trompeuse du "blue checkmark", l'opacité du répertoire publicitaire, et le refus d'accès aux données publiques pour les chercheurs. Cette décision marque la première application concrète du DSA contre une plateforme majeure.

**3 février 2026** — La Commission des affaires judiciaires de la Chambre des représentants des États-Unis publie un deuxième rapport ("PART II") qui approfondit et confirme les accusations initiales. Le rapport documente une campagne de censure systématique de la Commission européenne sur une décennie (2015-2025), l'application extraterritoriale du DSA, et l'absence de contrepoids démocratiques. Le rapport PART II établit comment le DSA est devenu un instrument de politique étrangère informationnelle de l'Union européenne.

---

## II. L'architecture du contrôle

Le système repose sur quatre niveaux interconnectés : politique, opérationnel, influence et technique.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#e8f4f8', 'primaryTextColor': '#1a1a2e', 'primaryBorderColor': '#4a90a4', 'lineColor': '#666', 'secondaryColor': '#f5f5f5', 'tertiaryColor': '#fff' }}}%%
flowchart TB
    subgraph POL[" Niveau POLITIQUE "]
        direction LR
        EUIF["🏛️ EUIF<br/>2015 · Commission UE"]
        DSA["📜 DSA<br/>2024 · Amendes 6%"]
    end

    subgraph OPS[" Niveau OPÉRATIONNEL "]
        direction LR
        GIFCT["🔗 GIFCT<br/>2017 · Meta · Microsoft · Google · X"]
        CC["🌍 Christchurch Call<br/>55 pays"]
    end

    subgraph INF[" Niveau INFLUENCE "]
        direction LR
        RAN["👥 RAN<br/>6 500 membres"]
        HED["🇦🇪 Hedayah<br/>Abu Dhabi · €305M UE"]
    end

    subgraph TECH[" Niveau TECHNIQUE "]
        direction LR
        HASH["📂 Hash-Sharing<br/>Database"]
        AI["🤖 AI Classifiers<br/>Faculty.ai · Jigsaw"]
        SHADOW["👁️ Shadowbanning<br/>Downranking"]
    end

    %% Flux principaux
    EUIF ==> DSA
    DSA ==> GIFCT
    GIFCT ==> CC

    %% Flux Influence
    EUIF -.-> RAN
    HED -.-> RAN

    %% Flux Technique
    GIFCT ==> HASH
    GIFCT ==> AI
    AI ==> SHADOW

    %% Styling
    class POL,OPS,INF,TECH fill:#f8f9fa,stroke:#333,stroke-width:1px,rx:8,ry:8
    class EUIF,DSA,GIFCT,CC,RAN,HED fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    class HASH,AI,SHADOW fill:#fff3e0,stroke:#f57c00,stroke-width:2px
```

### Le triangle institutionnel

Trois structures forment l'ossature du système :

1. **L'EU Internet Forum (EUIF)** : créé en 2015, coordonne la politique européenne
2. **Le GIFCT** : créé en 2017 par les Big Tech, opère la modération technique
3. **Le Christchurch Call** : créé en 2019, internationalise les standards

Ces trois institutions ne sont pas isolées. Elles forment un système intégré où les décisions politiques de l'UE se traduisent en algorithmes opérationnels par les entreprises technologiques.

### Les "Trusted Flaggers" — Censure par délégation

Le système dispose d'une couche supplémentaire documentée dans les 302 exhibits du rapport US House : les **Trusted Flaggers** (Drapeaux Fiables). Ces organisations — ONGs pro-censure agréées par la Commission UE — disposent d'un pouvoir de requête prioritaire auprès des plateformes, tout en échappant à toute responsabilité juridique directe.

> "Coordination with civil society organizations to compel American technology platforms to censor lawful American speech."
> — U.S. House Judiciary Report, Part II (février 2026)

### L'influence émiratie : une chaîne documentée

L'enquête révèle une chaîne d'influence troublante :

```
Émirats Arabes Unis (Abu Dhabi)
    ↓
Hedayah (centre d'excellence, 2012)
    ↓
RAN (Réseau de sensibilisation à la radicalisation)
    ↓
Définitions européennes de la "radicalisation"
    ↓
Critères de modération appliqués par le GIFCT
```

Un rapport de la NGO Report (7 juin 2023) documente cette influence : "Présence notable d'individus au sein des réseaux RAN et Hedayah qui s'alignent sur la position des Émirats arabes unis concernant l'islam politique, la radicalisation, la Turkey, le Qatar, les Frères musulman et l'Iran."

### Les outils de la censure moderne

Le système repose sur plusieurs mécanismes technologiques interconnectés :

- **Hash-Sharing Database** : base de données d'empreintes partagées entre 25+ entreprises
- **AI Classifiers** : algorithmes développés par Faculty.ai et Jigsaw (Google) pour classifier automatiquement le contenu
- **Shadowbanning** : réduction invisible de la visibilité, sans notification
- **Démonétisation** : suppression des revenus publicitaires
- **Downranking** : suppression des recommandations algorithmiques
- **Menaces financières** : amendes DSA jusqu'à 6% du CA mondial

La différence avec la censure d'État traditionnelle réside dans son invisibilité. L'utilisateur ne sait pas qu'il est censuré. Ses publications existent, mais personne ne les voit.

---

## III. Les preuves : ce que l'enquête a établi

### 1. L'opacité structurelle

Une étude de Just Security (25 septembre 2019), think tank de la NYU Law School, analyse le rapport de transparence du GIFCT. Son titre : **"Raises More Questions Than Answers"** (Soulève plus de questions qu'il n'apporte de réponses).

L'étude conclut que "la tendance croissante à déléguer aux entreprises privées le contrôle proactif de contenu 'terroriste' vaguement défini peut avoir un impact sérieux sur les droits et libertés fondamentaux".

En septembre 2024, Wired publie une enquête : "Two Years of Turmoil at Big Tech's Anti-Terrorism Group". L'article documente des conflits internes au conseil d'administration du GIFCT entre Meta, YouTube, Microsoft et X, avec des tensions sur l'adhésion de TikTok.

### 2. Les seuils algorithmiques différents

En 2024, l'Université d'Anvers publie une étude académique peer-reviewed : "AI content moderation and freedom of expression: a study of meta's double standards in Ukraine and Gaza censorship".

L'étude établit que **Meta applique des seuils de sensibilité algorithmiques différents selon les contextes géopolitiques**. Même type de contenu, traitement différent selon qu'il concerne l'Ukraine ou Gaza.

### 3. Les faux positifs massifs

L'Université d'Auckland (Nouvelle-Zélan a étudié le Christchurch Call. Ses conclusions : **22 % des contenus supprimés étaient des faux positifs** — des contenus légitimes retirés par erreur.

Plus d'un contenu légitime sur cinq est supprimé de manière erronée, sans que l'utilisateur puisse le savoir ou le contester efficacement.

### 4. Les cas judiciaires

L'investigation a identifié **cinq cas judiciaires majeurs** contre Meta :

- **Belgique, 3 juin 2024** : Shadowbanning confirmé illégal (€27 779)
- **Pologne, mars 2024** : Restauration de pages ordonnée, mais Meta fait appel et le contenu reste indisponible un an plus tard
- **Allemagne, 4 juillet 2023** : La Cour de justice de l'UE condamne Meta pour abus de position dominante et utilisation des données (€1,2 milliard d'amende)
- **Kenya, 20 septembre 2024** : La Cour d'appel du Kenya reconnaît les droits des modérateurs de contenu et la responsabilité de Meta
- **Commission UE, 15 novembre 2023** : Action en cours contre Meta pour non-respect du Digital Markets Act

**Constat** : les plaignants gagnent environ 60 % des cas, mais l'exécution des décisions est inefficace (seulement 33 % des décisions sont appliquées rapidement).

### 5. La décision X €120M — Application DSA

La sanction de 120 millions d'euros contre X (5 décembre 2025) constitue la première application du DSA par la Commission européenne.

**Implications documentées** :

- **Précedent juridique** : Le DSA peut être appliqué avec des amendes substantielles
- **Portée extraterritoriale** : X est une plateforme globale ; la décision affecte ses opérations mondiales
- **Effet dissuasif** : Les autres plateformes ajustent leurs politiques pour éviter des sanctions similaires
- **Mécanisme de contrôle** : La Commission dispose d'un levier économique majeur pour influencer les pratiques de modération

### 6. Les cas documentés de censure politique

Des cas concrets illustrent le fonctionnement du système :

**A. Slovaquie 2023 — La censure du discours biologique**

Contexte : Gouvernement Fico en place, UE inquiète de la rhétorique "anti-genre".

**Exemples de contenus supprimés documentés** (Exhibits 201-250 du rapport US House) :
- "Il n'y a que deux genres" → SUPPRIMÉ
- "Les enfants ne peuvent pas être trans" → SUPPRIMÉ  
- "L'idéologie LGBTIQ est une menace" → SUPPRIMÉ

**Mécanisme** : Gouvernement slovaque → EUIF → Plateformes → Suppression automatique algorithmique

**B. Roumanie 2024 — Élections annulées sans preuve**

Candidat : Calin Georgescu (discours conservateur)
Résultat : Victoire surprise annulée sans preuve d'ingérence russe

**Email interne TikTok documenté** (Exhibit 287) :
> "After comprehensive review, we found NO EVIDENCE of Russian interference in the Georgescu campaign content."
> — TikTok Trust & Safety Europe à la Commission UE, lignes 5754-5757

Malgré cette conclusion interne, les élections sont annulées, TikTok sanctionné pour "manque de vigilance". Le rapport US House note que la campagne Georgescu était financée par le parti libéral roumain — contradiction avec la thèse de l'ingérence étrangère.

**C. COVID-19 — Censure extraterritoriale**

Échange documenté Commission UE → YouTube (Exhibits 4113-4131) :
1. Commission : "Please verify why this content [documentaire américain] has not been removed"
2. YouTube : "We have removed the content"

Ce cas illustre une censure extraterritoriale : contenu américain protégé par le 1er Amendement, supprimé sous pression européenne. Le critère appliqué est politique, pas juridique.

---

## IV. Comparaison avec la censure soviétique

Le parallèle peut sembler provocateur. Il est pourtant méthodologiquement fondé.

### Architecture et mécanismes

| URSS | Union européenne |
|------|------------------|
| Goskomnadzor → KGB | EUIF → GIFCT → DSA |
| Censure manuelle | Censure algorithmique (IA) |
| Fichiers NKVD | Hash-sharing GIFCT |
| Critères explicites : "anti-soviétique" | Critères flous : "borderline content" |
| Satire politique : interdite | Satire politique : surveillée |
| Pas de shadowbanning | Downranking algorithmique |
| "Protection du peuple" | "Protection de l'enfance" |
| Transparence : zéro | Transparence : apparente |

L'architecture européenne diffère de son prédécesseur soviétique par trois caractéristiques : le partenariat public-privé (les décisions de modération sont prises par des entreprises privées sur critères publics), l'efficacité massive permise par l'algorithme, et la vitesse de propagation des censures via les bases de données partagées.

Les mécanismes fondamentaux restent identiques : la catégorisation floue comme arme politique, le contrôle hybride où l'État et les entreprises partagent la responsabilité sans que personne ne soit pleinement accountable, la couverture émotionnelle pour justifier la surveillance, et l'absence de contre-pouvoirs démocratiques effectifs.

### La différence technologique

L'Europe dispose d'outils que l'URSS n'avait pas : intelligence artificielle, bases de données globales, modération algorithmique à l'échelle de milliards d'utilisateurs. Cette technologie permet une censure invisible, où l'utilisateur ne sait pas qu'il est censuré.

---

## V. L'Invisibilisation Algorithmique — Pratiques Actuelles (2024-2026)

L'affaire belge de 2024 n'était pas un cas isolé. Une investigation Truth Engine complémentaire (février 2026) confirme que le shadowbanning et l'invisibilisation algorithmique sont des pratiques documentées chez toutes les plateformes majeures.

### Ce que les plateformes nient officiellement

Meta, X, YouTube et TikTok maintiennent la même ligne : "Nous ne pratiquons pas le shadowbanning." Des dizaines d'enquêtes journalistiques et académiques démontrent le contraire :

- **The Markup** (février 2024) : Investigation technique prouvant la réduction de visibilité sur Instagram
- **Washington Post** (octobre 2024) : "Algorithmic suppression" confirmée sur toutes les plateformes
- **RJI** (septembre 2024) : Journalistes shadowbanned pour leurs reportages
- **ArXiv** (NDSS 2026) : Étude académique "Revealing The Secret Power" sur les filtres de visibilité Twitter/X

### Les mécanismes d'invisibilisation

Les plateformes utilisent un éventail de techniques pour réduire la visibilité sans avertir l'utilisateur :

1. **Réduction du reach** — Les posts existent mais n'apparaissent pas dans les feeds des abonnés
2. **Suppression des hashtags** — Les contenus ne sont plus trouvables via la recherche
3. **Démonétisation** — L'utilisateur peut poster, mais ne génère plus de revenus (YouTube, "yellow dollar icon")
4. **Exclusion du For You Page** — TikTok et Instagram retirent les vidéos de l'algorithme de découverte
5. **Ghosts bans** — Les commentaires sont visibles pour l'auteur mais invisibles pour les autres

**Témoignage** : "Je continue de poster comme d'habitude. Mes vidéos sont publiées. Mais d'un coup, je passe de 10 000 vues à 100 vues. Sans notification. Sans explication. Sans recours."

### Le taux de réussite des recours : 33%

Quand un créateur conteste une restriction de visibilité, le taux de succès est de 33%. Les plateformes rejettent systématiquement les appels, ou les ignorent.

### L'écart entre le DSA et la réalité

Le Digital Services Act (février 2024) interdit officiellement le shadowbanning. Mais deux ans après son entrée en vigueur, la pratique continue sans que les régulateurs ne sanctionnent efficacement. L'affaire belge de 2024 reste l'unique condamnation judiciaire majeure en Europe.

Les créateurs sont réduits au silence algorithmiquement, sans savoir pourquoi, sans pouvoir se défendre, et sans que la loi ne les protège réellement.

---

## VI. Ce qu'on ne sait toujours pas

Malgré quatorze enquêtes approfondies, des zones d'ombre persistent :

**Les individus pro-UAE dans le RAN**

Le NGO Report affirme qu'il existe "une présence notable d'individus alignés avec la position des Émirats" au sein du RAN. Mais le rapport ne cite aucun nom. L'investigation n'a pu identifier aucun de ces individus spécifiquement.

**Les critères exacts d'ajout à la base de données**

Comment un contenu est-il ajouté à la Hash-Sharing Database du GIFCT ? Quels sont les critères précis ? Comment peut-on en sortir ? Ces informations ne sont pas publiques.

**L'étendue réelle du shadowbanning**

L'affaire belge documente une période de dix mois en 2021. L'investigation 2026 révèle que la pratique continue actuellement, malgré l'interdiction par le DSA. La durée exacte de l'impunité des plateformes reste documentée.

**Les voies de recours**

Le document GIFCT mentionne un "feedback on hashes". Aucune procédure claire de recours n'est documentée. Un utilisateur peut-il contester une décision de modération ? Qui examine ces contestations ? Dans quel délai ?

**L'application extraterritoriale du DSA**

Le rapport US House PART II accuse l'UE d'utiliser le DSA pour influencer la modération au-delà des frontières européennes. Les mécanismes précis de cette influence restent à documenter. Quelles plateformes ont modifié leurs politiques globales pour se conformer aux demandes UE ? Quels contenus ont été affectés ?

---

## VII. L'EU Democracy Shield — Ce qui se prépare

Les documents analysés révèlent un projet en préparation : l'**EU Democracy Shield** (Bouclier Démocratique UE), documenté aux lignes 6000-6200 du rapport US House (février 2026).

Ces éléments figurent dans les 302 exhibits officiels analysés par le rapport du Congrès américain.

### Composantes annoncées

**1. Fin de l'anonymat en ligne**
- Obligation d'identification pour tous les comptes
- Tracking obligatoire des créateurs de contenu
- Suppression du pseudonymat protecteur

**2. Centre Résilience Démocratique**
- Nouveau hub de coordination censure
- 500+ employés dédiés
- Accès direct aux algorithmes des plateformes

**3. Réseau de 50+ "fact-checkers" agréés UE**
- Financement direct par la Commission européenne
- Décisions de modération centralisées
- Pouvoir de requête prioritaire sans contre-pouvoir

**4. Protocole "Crisis Response"**
- Interrupteur "censure d'urgence"
- Activation sans vote parlementaire
- Périmètre vague : "désinformation en temps de crise"

### L'escalade logique

Ce projet représente l'escalade naturelle de l'architecture existante :

- **Phase 1 — Volontaire** (2015-2019) : Codes de conduite → Terrorisme
- **Phase 2 — Régulée** (2019-2024) : DSA → "Borderline content"
- **Phase 3 — Coercitive** (2024-2025) : Amendes 6% CA → Discours politique
- **Phase 4 — Totale** (2025+) : Democracy Shield → Contrôle systémique

Chaque phase utilise la précédente comme justification. On passe de la lutte contre le terrorisme à la surveillance de la satire politique, puis à l'identification obligatoire de tous les citoyens.

### La rationalisation

L'EU Democracy Shield se présentera comme une mesure de "protection de la démocratie" contre les "ingérences étrangères" et la "désinformation". Mais les documents révèlent un décalage entre le discours et les pratiques :

> "After comprehensive review, we found NO EVIDENCE of Russian interference in the Georgescu campaign content."
> — TikTok Trust & Safety Europe, lignes 5754-5757

Malgré cette conclusion interne, les élections roumaines ont été annulées. Le cas illustre que la menace invoquée ("ingérence étrangère") n'est pas nécessairement celle qui motive les décisions.

---

## VIII. La Dimension Géopolitique — Guerre de l'Information

### Le conflit UE-USA

Le rapport US House "The Foreign Censorship Threat" PART II (février 2026) révèle une dimension géopolitique majeure dans la question de la censure.

**Position américaine** : Le DSA est utilisé comme une arme de politique étrangère pour exporter les normes de modération européennes et influencer le discours public américain

**Position européenne** : Le DSA est un instrument de souveraineté numérique et de protection des citoyens européens

**La réalité** : Les deux positions sont partiellement vraies. Le DSA a des effets extraterritoriaux documentés (cas X), et les plateformes modifient leurs politiques globales pour se conformer aux exigences européennes.

### L'effet domino

La décision X €120M démontre que le DSA crée un effet domino :

1. L'UE impose des règles aux plateformes opérant en Europe
2. Les plateformes, pour éviter la complexité de modération par juridiction, appliquent les règles les plus strictes globalement
3. Les citoyens non-européens sont affectés par des décisions prises à Bruxelles
4. La "régulation européenne" devient de facto le standard mondial

Ce mécanisme explique comment une régulation européenne influence le discours mondial, au-delà des frontières de l'UE.

---

## IX. La Matrice — L'architecture globale du contrôle

### Du concept à la réalité concrète

Cette enquête s'inscrit dans une série d'articles qui documentent comment la France et l'Europe ont construit une architecture du mensonge et de la censure.

L'article **[🎭 L'EMPIRE DU MENSONGE : rapport d'autopsie d'une civilisation sous anesthésie](https://empire-mensonge.substack.com/p/empire-mensonge-civilisation)** publié le 7 janvier 2026 posait un diagnostic : la désinformation n'est pas un dysfonctionnement. C'est un **système**. Cette enquête sur l'UE-Censor démontre ce que l'Empire du mensonge décrivait en théorie : une architecture concrète, documentée, mesurable, qui contrôle ce que les citoyens peuvent voir, dire et partager.

Ce que cette enquête apporte, c'est la **matérialisation** du concept. On ne parle plus d'abstraction philosophique. On parle de 305 millions d'euros versés à Abu Dhabi. De 6 500 membres dont on ne connaît pas les noms. De 22% de contenus supprimés par erreur. De cinq jugements contre Meta. D'une amende de 120 millions d'euros contre X.

Ce système n'est pas théorique. Il s'applique à des gens réels.

Il ne faut pas confondre les acteurs et les victimes. L'article **[🎭 Tristan Mendès France : la machine à effacer](https://empire-mensonge.substack.com/p/tristan-mendes-france-machine-a-effacer)** du 4 février 2026 analyse le cas d'un chercheur spécialiste des cultures numériques, enseignant à l'Université de Paris et directeur de projets à Conspiracy Watch. Tristan Mendès France n'est pas une victime de la censure — il en est un architecte.

En tant que "fact-checker" et défenseur de la modération de contenu, il participe activement à la construction de l'architecture UE-Censor. Son travail consiste à définir ce qui est "vrai" et ce qui est "faux", ce qui relève du "complotisme" et doit être censuré. L'article "la machine à effacer" montre comment ces défenseurs de la "vraie information" deviennent les rouages indispensables du système de contrôle.

Les autres articles posaient le diagnostic. Celui-ci apporte les radios, les analyses de sang, les rapports d'autopsie. Et l'identification des acteurs.

### La naturalisation du contrôle

L'architecture UE-Censor ne se présente pas comme de la censure. Elle utilise des mots bienveillants : "Protection des citoyens", "Lutte contre le terrorisme", "Partenariat volontaire", "Safety". C'est la même méthode que l'URSS parlant de "défense du peuple", que la Chine parlant de "harmonie sociale", que les démocraties occidentales parlant de "liberté responsable".

Le contrôle le plus efficace est celui que nous demandons nous-mêmes.

Ce contrôle n'est jamais totalitaire pour tout. Il est sélectif.

L'article **[🇫🇷 L'État qui veut tout contrôler, mais échoue à tout](https://empire-mensonge.substack.com/p/etat-veut-tout-controler)** du 28 janvier 2026 révèle cette sélectivité. L'État français dépense des millions pour surveiller TikTok et "protéger les enfants" en ligne. Il construit l'architecture UE-Censor. Mais pendant ce temps, 396 900 enfants placés sous sa responsabilité (ASE) sont abandonnés, victimes de violences, parfois morts.

Le contrôle est à géométrie variable. On contrôle ce qui dérange le pouvoir (dissidence, satire, critique) mais pas ce qui l'arrange (négligence, corruption, incompétence). La machine à censurer fonctionne. La machine à protéger ne fonctionne pas.

Cette sélectivité révèle la nature du système : ce n'est pas de la protection. C'est de la préservation du pouvoir.

```
ÉVOLUTION DES MÉCANISMES DE CONTRÔLE :

1648 — Westphalie : État contrôle territoire (souveraineté)
1789 — Révolutions : État contrôle citoyens (conscription, impôts)
1917 — Totalitarismes : État contrôle esprits (propagande)
1948 — Orwell : État contrôle vérité (réécriture permanente)
1984 — Réalité : Marché contrôle désirs (publicité)
2024 — UE-Censor : Système contrôle discours (algorithmes)

La différence ? Le contrôle est :
- INVISIBLE (pas de soldats dans la rue)
- PARTICIPATIF (nous validons les règles)
- FRAGMENTÉ (personne ne voit l'ensemble)
- RÉVERSIBLE (on peut toujours dire "c'était une erreur")
```

### Les trois piliers du système

L'Empire du mensonge repose sur trois piliers interconnectés :

**PILIER I — Contrôle de l'information (UE-Censor)**
Vous venez de le lire. Le GIFCT et ses 25+ entreprises. Les 14 catégories. Les algorithmes. C'est le bras technique du système.

**PILIER II — Contrôle narratif (médias/industrie de l'influence)**
L'article **[💶 L'INDUSTRIE DE L'INFLUENCE : enquête sur le journalisme sous contrat](https://empire-mensonge.substack.com/p/industrie-influence)** révèle comment 90% des médias français appartiennent à 10 milliardaires. Ce n'est pas un écosystème médiatique. C'est une machine à produire le récit officiel. L'article **[📢 Annie Genevard : « Plus de cas de DNC »](https://empire-mensonge.substack.com/p/genevard-cas-dnc)** montre le mécanisme : un mensonge répété par un ministre devient « fait établi » sans qu'aucun journal ne vérifie.

**PILIER III — Contrôle matériel (lois, amendes, exclusion)**
L'article **[⚖️ La Justice Spectrale : L'Ère du Bannissement Administratif](https://empire-mensonge.substack.com/p/justice-spectrale)** documente comment la justice administrative française est devenue un outil d'exclusion. L'article **[🕸️ Ce que Macron appelle « protection des enfants »](https://empire-mensonge.substack.com/p/macron-protection-enfants)** montre comment le décret SMP et la loi SREN ferment la boucle : ce qui n'est pas supprimé en ligne est interdit hors ligne.

### La différence avec les totalitarismes classiques

- **Censeur** : Commissaire du peuple (identifiable, URSS) contre Algorithme + "communauté" (diffus, UE)
- **Critères** : "Anti-révolutionnaire = mort" (clairs, URSS) contre "Borderline" (flous, UE)
- **Résistance** : Visible (dissidents emprisonnés, URSS) contre Impossible (pas de procès, UE)
- **Coût** : Élevé (Goulag, exécutions, URSS) contre Nul (downranking, demonetization, UE)

L'oppression douce est plus efficace que l'oppression brutale parce qu'elle ne suscite pas de révolte. Quand on vous tue, vos amis se souviennent. Quand on vous rend invisible, personne ne remarque votre absence.

### Les investigations complémentaires

Les investigations complémentaires confirment cette architecture :

🔍 **INVESTIGATION FOIA (Financements)**
€305M vers Hedayah documentés. Opacité : 85-90%. Ce qu'on ne voit pas est plus important que ce qu'on voit.

🔍 **INVESTIGATION RAN (Membres)**
6 500 membres, seulement 0.5% identifiés. Influence UAE confirmée mais individus non nommés. La gouvernance est opaque par conception.

🔍 **INVESTIGATION JUDICIAIRE (Cas)**
5 cas majeurs contre Meta, 60% de victoires. Exécution des décisions : seulement 33%. Le droit existe mais ne fonctionne pas contre les plateformes.

🔍 **INVESTIGATION X €120M**
Première application DSA confirmée. Effet domino extraterritorial documenté. La Commission européenne dispose d'un levier économique majeur.

### La dimension psychologique

**COMMENT CES SYSTÈMES NOUS TRAQUENT :**

1. **USURE COGNITIVE** — Trop d'informations = impossibilité de vérifier
2. **CHAMBRE D'ÉCHO** — Algorithme ne montre que ce que vous aimez déjà
3. **PEUR DIFFUSE** — "Terrorisme", "désinformation" = acceptation de la surveillance
4. **DIVISION POUR RÉGNER** — Camps adverses empêchent l'alliance citoyenne
5. **FAUSSE TRANSPARENCE** — Rapports qui "en disent plus qu'ils ne cachent"

Résultat : Nous croyons être libres alors que nous sommes dans une cage dorée.

### Cartographie de l'Empire du Mensonge

🏛️ **CONTRÔLE INSTITUTIONNEL** (ce que vous lisez maintenant)
→ **UE-Censor** : L'architecture technique [VOUS ÊTES ICI]
→ [Tristan Mendès France](https://empire-mensonge.substack.com/p/tristan-mendes-france-machine-a-effacer) : La machine à effacer — les architectes de la censure
→ [L'État qui veut tout contrôler](https://empire-mensonge.substack.com/p/etat-veut-tout-controler) : L'hypocrisie du contrôle sélectif

🗞️ **CONTRÔLE MÉDIATIQUE**
→ [L'Industrie de l'Influence](https://empire-mensonge.substack.com/p/industrie-influence) : Qui possède la presse ?
→ [Les Télégraphistes de la Terreur](https://empire-mensonge.substack.com/p/telegraphistes-terreur) : La mécanique totalitaire

🌾 **CONTRÔLE ÉCONOMIQUE**
→ [L'État-Mafia](https://empire-mensonge.substack.com/p/etat-mafia-autopsie) : Liquidation de l'agriculture
→ [La Dernière Récolte](https://empire-mensonge.substack.com/p/derniere-recolte) : Autopsie d'une trahison

⚖️ **CONTRÔLE JURIDIQUE**
→ [La Justice Spectrale](https://empire-mensonge.substack.com/p/justice-spectrale) : L'ère du bannissement
→ [Annie Genevard](https://empire-mensonge.substack.com/p/genevard-cas-dnc) : Le mensonge ministériel
→ [Ce que Macron appelle « protection des enfants »](https://empire-mensonge.substack.com/p/macron-protection-enfants) : L'architecture de contrôle déguisée

🎭 **PSYCHOLOGIE DU POUVOIR**
→ [L'Empire du Mensonge](https://empire-mensonge.substack.com/p/empire-mensonge-civilisation) : Diagnostic civilisationnel
→ [Ils Ont Quitté l'Humanité](https://empire-mensonge.substack.com/p/quitte-humanite) : Psychopathologie de l'élite

**14+ articles. Une seule machine.**

Chaque texte explore un pan différent du même système. L'UE-Censor que vous venez de lire est le pilier technique — celui qui rend possible la censure algorithmique, invisible, globale. Mais il ne fonctionne qu'en synergie avec les autres piliers : le contrôle médiatique qui étouffe la vérité, le contrôle juridique qui bannit les opposants, le contrôle économique qui liquide les résistances, la psychologie du pouvoir qui justifie l'injustifiable.

### Le choix qui reste

Vous avez lu jusqu'ici. Vous savez maintenant ce que l'enquête a établi.

Ce que vous faites de cette connaissance est votre choix.

Vous pouvez fermer cet article et oublier. Le système compte là-dessus. L'oubli est son allié le plus fidèle.

Ou vous pouvez résister. Pas avec des armes — avec votre attention. Partagez. Vérifiez. Questionnez. Refusez la facilité narrative.

La cage n'est solide que si nous acceptons d'y rester.

Les articles liés ci-dessus montrent que d'autres ont commencé à creuser. Rejoignez-les. Ou commencez votre propre investigation.

La vérité n'a besoin que d'être vue pour devenir dangereuse pour le mensonge.

---

## Conclusion

Ce que l'Europe a construit en dix ans n'est pas simplement une régulation du numérique. C'est une **architecture de contrôle de l'information globale**, opérée par un cartel de quatre entreprises technologiques (Meta, Microsoft, Google, X), avec des critères influencés par des intérêts étrangers (Émirats Arabes Unis via Hedayah), et des décisions prises en dehors de tout contrôle démocratique.

**Les éléments établis** :

- La satire politique est explicitement surveillée comme catégorie de modération
- 22 % des contenus supprimés sont des erreurs (faux positifs)
- L'influence émiratie sur les définitions de "radicalisation" est documentée
- Le shadowbanning a été pratiqué secrètement pendant des mois
- Une amende de 120 millions d'euros a été infligée à X (décembre 2025)
- L'application extraterritoriale du DSA est confirmée
- Aucune procédure de recours effectif n'existe
- L'EU Democracy Shield prépare la fin de l'anonymat en ligne (500+ employés dédiés)
- Le protocole "crisis response" permettra une censure d'urgence sans vote parlementaire
- Les "Trusted Flaggers" (ONGs) disposent d'un pouvoir de requête prioritaire

Ce système est invisible. Il ne supprime pas les dissidents — il les rend inaudibles. Il ne ferme pas les journaux — il les démonétise et les déréférence. Il n'emprisonne pas les opposants — il réduit leur visibilité algorithmique jusqu'à les faire disparaître de l'espace public.

L'EU Democracy Shield (documenté aux lignes 6000-6200 du rapport US House) prévoit la fin de l'anonymat en ligne, un Centre Résilience Démocratique avec 500+ employés, et un interrupteur de "censure d'urgence" activable sans vote parlementaire. L'architecture actuelle n'est que le prélude.

Les faits établis dessinent un schéma cohérent d'une ingénierie sociale. L'architecture existe. Elle fonctionne. Elle échappe aux contrôles démocratiques.

La dimension géopolitique des rapports US House (juillet 2025 + février 2026) confirme que ce système dépasse les frontières européennes et affecte le discours global.

Reste à savoir si les Européens accepteront de financer, via leurs impôts et via l'usage des plateformes qui captent leur attention, une machine de censure qui, un jour, pourrait se retourner contre eux.

---

## Méthodologie et sources

Cet article s'appuie sur **quatorze enquêtes Truth Engine** et s'inscrit dans une série de **quatorze articles** de l'Empire du Mensonge qui documentent le système global de contrôle.

### Sources documentaires

**Documents officiels** :

- **U.S. House Judiciary Committee, "The Foreign Censorship Threat — PART II"** (3 février 2026)
  - 7,826 lignes documentant la campagne de censure européenne sur une décennie
  - Confirme l'application extraterritoriale du DSA
  - Détaille les modifications de politiques des plateformes sous pression UE
  - 302 exhibits : emails internes Google, lettres Commission UE, actes réunions EUIF, réponses aux RFIs
  - 94+ réunions EUIF documentées (2022-2024)
  - Documentation EU Democracy Shield (lignes 6000-6200)

- **European Commission Decision IP_25_2934** (5 décembre 2025)
  - Amende de 120 millions d'euros contre X
  - Violations : blue checkmark trompeur, opacité publicitaire, refus de données chercheurs

- Brochure EU Internet Forum "10 Years" (2025)
- Document GIFCT "Borderline Content" (juin 2023, 674 lignes)
- Règlement DSA (Digital Services Act)

**Sources académiques peer-reviewed** :

- University of Antwerp, "AI content moderation and freedom of expression" (2024)
- University of Auckland, Christchurch Call Study
- Columbia Global Freedom of Expression, case law database

**Investigations journalistiques** :

- Just Security, "GIFCT Transparency Report Raises More Questions Than Answers" (25 septembre 2019)
- Wired, "Two Years of Turmoil at Big Tech's Anti-Terrorism Group" (30 septembre 2024)
- US House Judiciary, "The Foreign Censorship Threat" (25 juillet 2025)

**Décisions judiciaires** :

- Cour d'appel de Gand, Case 2022/AR/508 (3 juin 2024)
- CJUE, Affaire C-252/21 (4 juillet 2023)
- Tribunal de Varsovie, SIN v. Meta (mars 2024)
- Kenya Court of Appeal, E595 of 2023 (20 septembre 2024)

**Rapports d'ONG** :

- NGO Report, "Hedayah" (7 juin 2023)
- Panoptykon Foundation, "6 Years in Court Fighting Against Arbitrary Censorship" (2025)

---

**Date de l'enquête : 5 février 2026**
