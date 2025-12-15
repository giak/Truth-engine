# L'Europe construit-elle un crédit social à la française ?

## Chat Control, DSA, eIDAS, euro numérique : anatomie d'une architecture de surveillance que personne n'a votée

Protéger les enfants. Lutter contre la désinformation. Sécuriser l'espace numérique. Qui pourrait être contre ? C'est précisément cette question qui devrait nous alerter. Quand un projet de loi s'arme d'un bouclier moral, il devient presque impossible de le critiquer sans passer pour complice du mal qu'il prétend combattre.

Derrière les acronymes DSA, Chat Control, eIDAS et "euro numérique", une architecture se déploie. Pas une dictature brutale — l'Europe ne fonctionne pas ainsi. Quelque chose de plus subtil : un système où la liberté devient statistiquement improbable. Où la parole n'est plus un droit, mais une permission révocable. Où le citoyen n'est plus innocent jusqu'à preuve du contraire, mais suspect par défaut.

Cette investigation révèle ce que la surface cache : des conflits d'intérêts documentés à hauteur de millions d'euros, des taux de faux positifs soigneusement omis, des ONG "indépendantes" financées à 95% par l'État, et trois circuits — argent, contrôle, surveillance — qui convergent vers un profil citoyen complet.

---

## I - L'homme qui vend la solution qu'il impose

Commençons par une question simple : qui écrit les lois européennes sur la détection automatique des contenus pédocriminels ? La réponse officielle : la Commission européenne, sous l'impulsion de la commissaire aux Affaires intérieures Ylva Johansson. La réponse complète est plus instructive.

En 2023, le média d'investigation néerlandais Follow the Money publie une enquête explosive. L'ONG Thorn, fondée par l'acteur Ashton Kutcher, a dépensé **600.000 euros par an en lobbying** à Bruxelles via le cabinet FGS Global. Or Thorn ne fait pas que militer pour Chat Control — elle **vend le logiciel "Safer"** qui implémente exactement ce que la loi rendrait obligatoire.

Les documents obtenus par les journalistes montrent que Johansson elle-même qualifie Thorn de "partner" dans sa correspondance officielle. Le site Netzpolitik.org titre : "Dude, Where's My Privacy? Comment une star hollywoodienne fait du lobbying pour plus de surveillance en Europe."

Le schéma est limpide :

1. Thorn finance le lobbying pour Chat Control
2. Chat Control rendrait le scanning obligatoire pour toutes les messageries
3. Thorn vend la solution de scanning aux messageries contraintes de se conformer
4. Le marché captif est créé avant même le vote parlementaire

Ce n'est pas une théorie du complot. C'est un conflit d'intérêts documenté par des sources primaires.

Le réseau s'étend bien au-delà de Kutcher. La Oak Foundation, fondation privée basée en Suisse, a versé **24 millions de dollars** à un écosystème d'ONG : Thorn, ECPAT, WeProtect Global Alliance. Toutes militent pour la même législation. Ces organisations sont ensuite citées comme "experts de la société civile" dans les consultations de la Commission, sans que leur financement commun soit mentionné.

Le magazine Fortune résume en septembre 2023 : "Thorn, l'ONG d'Ashton Kutcher, a fait du lobbying pour la loi européenne sur les abus sexuels sur mineurs." L'article détaille comment Julie Cordua, CEO de Thorn, entretient une correspondance directe avec la commissaire Johansson.

L'ombudsman européen (médiateur) a ouvert une enquête sur le manque de transparence de ces consultations. Ses conclusions : la Commission n'a pas suffisamment documenté ses contacts avec les parties prenantes. Le secret demeure.

👉 **Conséquence** : Ceux qui écrivent la loi vendent la solution. Le marché captif est créé avant même le vote.

---

## II - 58% de faux positifs : le chiffre qu'on vous cache

Chat Control, officiellement "Règlement CSAR" (Child Sexual Abuse Regulation), impose aux messageries de scanner les communications privées **avant chiffrement** pour détecter les contenus pédocriminels. C'est ce qu'on appelle le "client-side scanning" (CSS) : l'analyse se fait sur votre appareil, avant que le message ne soit chiffré et envoyé.

La technologie principalement utilisée : PhotoDNA, développée par Microsoft et déployée par des entreprises comme Thorn via leur produit "Safer". Son principe : comparer les images aux bases de données de contenus illégaux connus en créant des "empreintes" (hashes) résistantes aux modifications mineures.

Quelle est sa fiabilité ? Les promoteurs avancent un chiffre extraordinaire : **"1 fausse alerte sur 50 milliards d'images"**. Thorn et le NCMEC (National Center for Missing & Exploited Children américain) répètent ce nombre dans chaque audition parlementaire.

Or une étude publiée dans les actes de l'ACM (Association for Computing Machinery) en 2023 révèle des données radicalement différentes. Les chercheurs ont analysé les signalements réels transmis aux autorités :

- **LinkedIn (utilisant PhotoDNA)** : Sur 75 signalements transmis au NCMEC, **44 étaient des faux positifs** — soit **58%** d'erreur
- **Facebook** : **75%** des signalements classés "non-malicious" après examen humain

D'où vient l'écart entre "1 sur 50 milliards" et 58% d'erreur ? Le "1 sur 50 milliards" concerne les correspondances de hash **exactes**. Mais les systèmes réels utilisent des variations floues ("perceptual hashing") pour attraper les images légèrement modifiées (recadrées, compressées, filtrées) — et c'est là que les faux positifs explosent.

**Cas concrets documentés :**

L'EFF (Electronic Frontier Foundation) documente plusieurs cas emblématiques. En 2022, un père envoie à son pédiatre des photos de l'infection génitale de son fils pour obtenir un avis médical à distance — pratique encouragée pendant la pandémie. Google scanne automatiquement les images, les signale au NCMEC comme potentiel CSAM (Child Sexual Abuse Material).

La police enquête. Le père est innocenté. Mais son compte Google — 15 ans d'emails, photos de famille, documents de travail — est supprimé définitivement. Google refuse de le restaurer malgré l'abandon des poursuites. La technologie a tranché ; l'humain ne peut plus revenir en arrière.

Un autre cas documenté par Gizmodo : un adolescent de 16 ans partage une image consensuelle avec sa petite amie du même âge. Techniquement illégal. Signalement automatique. Enquête policière. Le jeune est fiché.

Ces cas ne sont pas des dysfonctionnements. Ce sont les **conséquences prévisibles** d'un système de surveillance de masse appliqué à des communications intimes.

Pourquoi cette omission sur les taux réels ? Parce que si les citoyens européens savaient que plus de la moitié des alertes concernent des innocents, le débat démocratique serait différent. Le choix binaire "protection des enfants versus vie privée" s'effondrerait face à une question plus juste : "Acceptons-nous que des millions de citoyens innocents soient signalés pour attraper des coupables ?"

👉 **Conséquence** : Les promesses de fiabilité sont invérifiables. Les taux réels contredisent radicalement la communication officielle.

---

## III - Les "signaleurs de confiance" : quand l'État finance ses propres délateurs

Le DSA (Digital Services Act), entré en vigueur en 2024, crée une catégorie juridique nouvelle : les **"trusted flaggers"** (signaleurs de confiance). Ces organisations voient leurs signalements traités **en priorité** par les plateformes. Un contenu signalé par un trusted flagger doit être examiné et traité sous 24 heures. Un statut accordé par les régulateurs nationaux, pas par les plateformes elles-mêmes.

Qui sont ces "signaleurs de confiance" ? En théorie, des associations de la société civile, expertes de leur domaine. En pratique, l'enquête révèle une réalité différente.

En Allemagne, l'association "Respect" figure parmi les premiers trusted flaggers accrédités sous le DSA. Une enquête d'Euronews (août 2025) révèle sa structure de financement : **95% de ses ressources proviennent du programme gouvernemental "Demokratie Leben"** (Vivre la démocratie), financé par le ministère fédéral de la Famille.

Le juriste Ralf Höcker, interrogé par Euronews, résume : "C'est de la **censure étatique avec des caractéristiques supplémentaires**." Quand l'État finance une organisation, lui accorde un statut prioritaire auprès des plateformes, et que cette organisation détermine ce qui est "haineux" — la "société civile indépendante" n'est plus qu'une façade juridique.

Le mécanisme européen reproduit ce schéma à grande échelle :

1. La Commission ou les États financent des organisations via divers programmes (Horizon, Digital Europe, fonds nationaux)
2. Ces organisations demandent le statut de "trusted flagger" auprès des régulateurs nationaux
3. Leurs signalements obligent les plateformes à agir sous 24 heures — délai trop court pour une analyse juridique sérieuse
4. Aucun contrôle judiciaire préalable n'est requis — le juge intervient après, si l'utilisateur conteste
5. L'utilisateur moyen ne conteste jamais (coût, temps, méconnaissance des recours)

Le Centre for Democracy and Technology (CDT) alerte dans un rapport de 2024 : "Les trusted flaggers créent un système de **censure à deux vitesses**. Les signalements ordinaires sont traités selon les procédures standard. Les signalements 'de confiance' déclenchent une suppression quasi-automatique."

Le précédent américain est éclairant. L'affaire **Murthy v. Missouri** (2023-2024) a révélé que l'administration Biden pratiquait le "jawboning" : pression informelle sur les plateformes pour supprimer des contenus légaux. Des emails internes montrent des responsables gouvernementaux demandant à Facebook et Twitter de retirer des posts critiquant la politique sanitaire — posts parfois factuellement corrects.

La Cour suprême américaine a examiné si ces pratiques violaient le Premier Amendement (liberté d'expression). En Europe, la question ne se pose même pas : le DSA **institutionnalise** ce que les États-Unis qualifient de dérive.

👉 **Conséquence** : L'État censure par procuration via des ONG qu'il finance lui-même, sans contrôle judiciaire préalable.

---

## IV - eIDAS Article 45 : la bombe à retardement que 400 experts dénoncent

Pendant que Chat Control monopolise l'attention médiatique, une modification apparemment technique du règlement eIDAS (electronic IDentification, Authentication and trust Services) pourrait avoir des conséquences bien plus graves pour la sécurité de tous les Européens.

L'**Article 45** du règlement eIDAS 2.0 obligerait les navigateurs web (Chrome, Firefox, Safari, Edge) à faire confiance aux **autorités de certification (CA) désignées par les gouvernements européens**. Traduction technique : n'importe quel État membre pourrait créer ses propres certificats de sécurité, et les navigateurs seraient légalement obligés de les accepter.

Pourquoi est-ce grave ? Les certificats sont ce qui garantit que lorsque vous visitez votre banque en ligne, vous communiquez vraiment avec votre banque — pas avec un imposteur. Le cadenas dans votre navigateur repose sur ce système. Si un gouvernement peut émettre de faux certificats, il peut **intercepter le trafic HTTPS** de ses citoyens en se faisant passer pour n'importe quel site.

Ce n'est pas de la paranoïa technique. C'est exactement ce que le **Kazakhstan a tenté en 2019**. Le gouvernement kazakh a annoncé que tous les citoyens devaient installer un "certificat de sécurité nationale" permettant aux autorités de déchiffrer tout le trafic internet. Chrome, Firefox et Safari ont immédiatement **bloqué ce certificat**, le rendant inopérant.

Sous eIDAS Article 45, cette protection disparaîtrait pour les CA européennes. Les navigateurs ne pourraient plus refuser un certificat émis par un État membre, même s'ils suspectent un usage malveillant.

En novembre 2023, **plus de 400 experts en cybersécurité** de 34 pays signent une lettre ouverte. Mozilla, l'EFF, l'OpenSSF (Open Source Security Foundation) et des cryptographes renommés comme ceux de l'université de Stanford dénoncent un texte qui "**reculerait la sécurité du web de 12 ans**".

L'**Internet Society** (ISOC), organisation internationale de référence sur les standards internet, publie un "Impact Brief" détaillant les risques :

> "Les gouvernements pourraient intercepter le trafic web de n'importe quel citoyen européen. Les entreprises pourraient être contraintes d'installer des certificats permettant la surveillance de leurs employés. Le modèle de confiance du web — construit sur des décennies — serait fondamentalement compromis."

Le **Register**, publication technique britannique respectée, titre : "L'Europe se prépare à briser la sécurité des navigateurs".

La Commission européenne répond que ces craintes sont "exagérées" et que les gouvernements n'utiliseraient jamais ces pouvoirs de manière abusive. Mais elle **refuse de modifier le texte** pour explicitement interdire l'usage des CA étatiques pour l'interception de trafic.

Question simple : pourquoi laisser la porte ouverte si l'intention n'existe pas ?

👉 **Conséquence** : L'architecture technique permettrait aux gouvernements d'intercepter toutes les communications chiffrées. La capacité crée l'usage.

---

## V - Le précédent PATRIOT Act : 0,9% pour le terrorisme, 99,1% pour le reste

Les partisans de Chat Control et du DSA promettent que ces pouvoirs ne seront utilisés que contre les crimes les plus graves. L'histoire de la surveillance étatique suggère systématiquement le contraire.

Aux États-Unis, le **PATRIOT Act** de 2001 — voté dans l'émotion du 11 septembre — a introduit les "sneak and peek warrants". Ces mandats permettent aux forces de l'ordre de perquisitionner secrètement un domicile sans prévenir le propriétaire. Justification officielle : la **lutte antiterroriste**. Les criminels terroristes ne doivent pas être alertés des enquêtes en cours.

Les statistiques du Département de la Justice américain pour la période 2006-2009 révèlent l'usage réel de ces mandats :

- **15 mandats** pour terrorisme
- **122 mandats** pour fraude financière
- **1.618 mandats** pour trafic de drogue

Le terrorisme représente **0,9%** des utilisations d'un outil créé et justifié par le terrorisme. La drogue représente 97%.

Ce phénomène porte un nom : le **"mission creep"** (dérive de finalité) ou "scope creep" (extension de périmètre). Une infrastructure de surveillance, une fois en place, trouve **toujours** de nouvelles applications. Les garanties initiales s'érodent. Les exceptions deviennent la norme. La surveillance créée pour un usage limité s'étend à tous les usages possibles.

Le site They Are Watching, dédié à la documentation des abus de surveillance, compile des dizaines d'exemples similaires. La NSA (National Security Agency), créée pour l'espionnage étranger, a fini par surveiller les communications domestiques américaines (révélations Snowden, 2013).

**Chat Control suivra le même chemin.** L'infrastructure est conçue pour le CSAM. Mais une fois déployée :

- Le terrorisme sera ajouté (déjà évoqué dans les débats)
- L'extrémisme violent suivra (définition élastique)
- La "désinformation" viendra ensuite (terme que chaque gouvernement définit à sa convenance)
- Les "contenus haineux" compléteront (catégorie aux contours flous)

L'infrastructure est **la même**. Seuls les critères de recherche changent. Et ces critères sont modifiables par simple mise à jour logicielle, sans nouveau vote parlementaire.

Le **Clipper Chip** américain (1993-1996) offre un précédent direct pour Chat Control. Cette puce cryptographique avec backdoor gouvernementale était présentée comme "protection de la sécurité nationale". L'administration Clinton promettait qu'elle ne serait utilisée que contre les criminels les plus dangereux.

En 1994, le cryptographe **Matt Blaze** (AT&T Bell Labs) publie une analyse démontrant des failles techniques majeures dans le système. Le Clipper Chip est abandonné en 1996. Trente ans plus tard, l'Europe relance **exactement la même idée** sous le nom de "client-side scanning" — avec les mêmes promesses et les mêmes failles structurelles.

👉 **Conséquence** : Les outils de surveillance créés pour un usage limité s'étendent systématiquement. L'histoire n'a pas d'exception.

---

## VI - Le DSA : 6% du chiffre d'affaires mondial, ou l'économie de la peur

Le Digital Services Act impose aux "très grandes plateformes en ligne" (VLOP - Very Large Online Platforms, plus de 45 millions d'utilisateurs européens actifs) des obligations de modération renforcées. La sanction en cas de non-conformité : **jusqu'à 6% du chiffre d'affaires annuel mondial**.

Pour X (ex-Twitter), cela représenterait potentiellement **plusieurs milliards d'euros**. Pour Meta ou Google, des **dizaines de milliards**. Ces montants ne sont pas des plafonds théoriques — la Commission a explicitement rappelé ces sanctions dans ses procédures contre X en 2024.

Face à de tels montants, aucune plateforme rationnelle ne prendra le risque de la sous-modération. Le calcul économique est simple :

- Coût d'un retrait injustifié : quelques utilisateurs mécontents, pas de sanction
- Coût d'un non-retrait sanctionné : potentiellement des milliards d'euros

Le résultat prévisible et documenté : la **sur-conformité préventive** ("algorithmic overcompliance"). Les plateformes retirent le **licite** "par précaution". Elles implémentent des filtres plus stricts que la loi n'exige, car le coût asymétrique rend la censure excédentaire économiquement rationnelle.

Thierry Breton, alors commissaire au Marché intérieur, a illustré cette logique dans un échange devenu viral avec Elon Musk en octobre 2023. **Avant même qu'une infraction soit constatée**, il a publiquement averti X des conséquences du non-respect du DSA. Musk a répondu : "Le tyran de l'Europe."

Le précédent britannique confirme ce mécanisme. L'**Online Safety Act** (2023) britannique prévoit des amendes jusqu'à 10% du CA mondial et jusqu'à £18 millions pour les dirigeants personnellement. L'analyse du juriste Richard Miller (publiée sur ALOR) documente comment les plateformes ont commencé à sur-modérer les contenus légaux dès l'annonce de la loi, avant même son application.

Le problème structurel est le suivant : **le juge arrive après l'algorithme**. Quand un contenu est retiré automatiquement en 24 heures suite à un signalement de trusted flagger, qui saisit les tribunaux pour le contester ? L'utilisateur lambda n'a ni le temps, ni les ressources, ni souvent la connaissance des recours disponibles.

Le DSA prévoit des mécanismes de contestation. Mais ces mécanismes supposent que l'utilisateur :
1. Soit informé du retrait et de sa justification
2. Comprenne ses droits
3. Dispose du temps et de l'énergie pour contester
4. Soit prêt à potentiellement s'identifier publiquement

Pour un post supprimé parmi des milliers, combien font ce parcours du combattant ?

La Commission européenne présente le DSA comme un "**modèle d'exportation normative mondiale**" — et elle a raison. Le Brésil, l'Australie, l'Inde examinent des législations similaires. La norme exportée est celle du contrôle algorithmique avec sur-censure intégrée, pas celle de la liberté d'expression avec garanties judiciaires.

👉 **Conséquence** : Les amendes massives créent une économie de la sur-censure où le doute profite systématiquement à la suppression.

---

## VII - ARCOM : le régulateur sous contrôle politique

En France, l'Autorité de régulation de la communication audiovisuelle et numérique (ARCOM) — née de la fusion du CSA et de l'Hadopi en 2022 — illustre les dérives possibles d'un régulateur théoriquement indépendant.

En janvier 2025, **Martin Ajdari** devient président de l'ARCOM. Détail significatif : la commission des Affaires culturelles du Sénat a voté **17 contre, 12 pour** sa nomination. Un **avis défavorable** — le premier depuis la création de ce mécanisme de contrôle parlementaire sous l'Article 13 de la Constitution de 1958.

Le système constitutionnel français prévoit que le président ne peut procéder à la nomination si les votes négatifs des commissions compétentes des deux assemblées représentent au moins 3/5 des suffrages exprimés. L'Assemblée nationale ayant voté favorablement, l'avis défavorable du Sénat seul ne suffit pas mathématiquement à bloquer. Ajdari est donc nommé malgré l'opposition sénatoriale.

Pourquoi cette défiance exceptionnelle ? Le contexte : l'ARCOM avait refusé, quelques mois plus tôt, le renouvellement des fréquences TNT des chaînes **C8 et NRJ12**, dans un contexte de tensions avec le groupe Bolloré. Les sénateurs de droite et du centre y voyaient un "deux poids, deux mesures" — des chaînes conservatrices sanctionnées plus sévèrement que leurs équivalentes progressistes.

Un chiffre a été largement médiatisé : "16 sanctions contre C8/CNews en 2024". Ce chiffre agrège des réalités très différentes : avertissements, mises en demeure et amendes effectives. En réalité, **6 amendes** ont été prononcées. L'amalgame permet de construire un récit d'acharnement — ou de laxisme, selon le camp.

La question n'est pas de savoir si C8 méritait ou non des sanctions — les manquements déontologiques documentés (séquences de Cyril Hanouna notamment) sont réels et parfois spectaculaires. La question est **structurelle** : **7 des 9 membres du collège ARCOM sont désignés par des autorités politiques**. Le Président de la République en nomme trois. Les présidents de l'Assemblée nationale et du Sénat en nomment chacun deux.

L'indépendance proclamée repose entièrement sur la bonne volonté des nomminants. Quand ces nomminants sont du même bord politique, le collège penche. Quand ils changent, le collège peut changer aussi.

Le phénomène de **"revolving door"** (pantouflage) aggrave cette capture structurelle. L'exemple le plus récent : en 2024, **Nicholas Banasevic**, haut fonctionnaire de la DG Competition (antitrust) de la Commission européenne — celle qui enquête sur les Big Tech — rejoint... **Microsoft**.

L'homme qui hier enquêtait sur les pratiques anticoncurrentielles des géants tech travaille aujourd'hui pour l'un d'eux. Le Corporate Europe Observatory a documenté ce cas dans un rapport d'octobre 2024 intitulé "Comment les portes tournantes de la Big Tech érodent les lois antitrust européennes".

Une étude du Harvard Kennedy School documente qu'aux États-Unis, **63% des dirigeants de la FTC** (Federal Trade Commission, équivalent de l'autorité de la concurrence) ont travaillé dans l'industrie tech avant ou après leur mandat public.

L'UE n'est pas épargnée. Entre 2008 et 2016, **252 personnes** ont circulé entre Google et l'administration Obama — dans les deux sens. Les régulateurs qui écrivent les règles ont souvent travaillé pour ceux qu'ils régulent, ou y travailleront ensuite.

👉 **Conséquence** : Les régulateurs "indépendants" sont structurellement liés au pouvoir politique et aux intérêts qu'ils sont censés contrôler.

---

## VIII - Les données de santé françaises chez Microsoft : un symbole

Le **Health Data Hub** (HDH), plateforme française destinée à centraliser les données de santé pour la recherche, illustre le fossé entre les discours de souveraineté numérique et la réalité des choix technologiques.

En décembre 2023, la CNIL (Commission Nationale de l'Informatique et des Libertés) autorise l'hébergement des données du HDH chez **Microsoft Azure**. La formule utilisée est révélatrice : autorisation "**avec regrets**". La CNIL reconnaît que cette solution n'est pas idéale sur le plan de la souveraineté, mais l'accepte faute d'alternative opérationnelle à court terme.

Pourquoi "avec regrets" ? Parce que les données hébergées chez Microsoft sont soumises au **CLOUD Act** américain (2018). Cette loi permet aux autorités américaines d'exiger l'accès aux données stockées par des entreprises américaines, **quel que soit le lieu de stockage physique**. Vos données de santé françaises, sur un serveur Azure situé en France, restent accessibles à la justice américaine.

En novembre 2024, le **Conseil d'État** valide définitivement cette configuration, rejetant les recours des associations de protection des données. La décision juridique ne conteste pas la réalité du risque — elle constate simplement que les garanties contractuelles offertes par Microsoft sont jugées "suffisantes" au regard du droit européen actuel.

Stéphanie Combes, directrice du HDH, avait annoncé une migration vers un cloud souverain "pas avant 2025". Nous sommes fin 2025 ; la migration n'est toujours pas achevée.

Plus largement, une étude révèle que **44% des CHU français** hébergent des données sur des clouds non-européens. La "souveraineté numérique" — terme omniprésent dans les discours officiels — reste un "mot creux" sans contrôle effectif des serveurs.

Le paradoxe est saisissant : l'Europe légifère sur la protection des données (RGPD), impose des obligations aux plateformes (DSA), crée des systèmes d'identité numérique (eIDAS)... tout en hébergeant les données les plus sensibles de ses citoyens chez des entreprises soumises à des juridictions étrangères.

👉 **Conséquence** : La souveraineté numérique européenne est un discours sans infrastructure. Les données critiques restent sous juridiction américaine.

---

## IX - L'euro numérique : programmable ou pas ?

La Banque centrale européenne (BCE) prépare l'introduction d'un "euro numérique" à horizon 2027-2029. La question centrale : sera-t-il **programmable** ?

La programmabilité permettrait de conditionner les transactions. Exemples théoriques :
- Limites géographiques (euros utilisables uniquement en zone euro)
- Dates d'expiration (monnaie "périmée" si non dépensée)
- Catégories de dépenses autorisées (interdiction d'acheter certains produits)
- Rationnement automatique (quotas de carbone intégrés)

La **position officielle de la BCE** est claire : l'euro numérique "**ne sera pas programmable**". Christine Lagarde l'a répété. Les documents officiels l'affirment.

Mais **Burkhard Balz**, membre du directoire de la Bundesbank (banque centrale allemande), déclare que l'euro numérique "**pourrait supporter des paiements programmables**". Nuance sémantique : il ne serait pas programmable par défaut, mais l'architecture le permettrait si décidé ultérieurement.

Cette distinction est cruciale. La **capacité technique** existe. L'**usage politique** est (pour l'instant) exclu. Mais une fois l'infrastructure déployée, rien n'empêche de changer les paramètres.

Le parallèle avec Chat Control est frappant : l'infrastructure de scanning est créée pour le CSAM. Les usages futurs dépendent des décisions politiques — qui peuvent changer sans nouveau vote citoyen.

Le précédent chinois pèse sur ce débat. Le yuan numérique chinois intègre des fonctionnalités de programmabilité et de traçabilité complète. Personne ne prétend que l'Europe copiera la Chine. Mais la question légitime est : quelles **garanties structurelles** empêchent une dérive ?

Si la réponse est "la bonne volonté des gouvernants actuels", ce n'est pas une garantie — c'est un pari.

👉 **Conséquence** : L'euro numérique ne sera pas programmable... tant que le pouvoir politique ne décidera pas qu'il l'est. L'architecture le permet.

---

## X - Trois circuits vers le profil citoyen complet

Vue d'ensemble, l'architecture européenne dessine trois circuits distincts — argent, contrôle, surveillance — qui convergent vers un même point : le **profil citoyen complet**.

**Circuit 1 : L'argent**

```
Oak Foundation (24M$)
    ↓
Thorn, ECPAT, WeProtect
    ↓
Lobbying Chat Control (600k€/an)
    ↓
Obligation CSS = marché captif Thorn
```

Ceux qui financent le lobbying vendent la solution rendue obligatoire. Le conflit d'intérêts est structurel, documenté, assumé.

**Circuit 2 : Le contrôle**

```
Commission UE / États membres
    ↓ financement
Trusted Flaggers (95% État)
    ↓ signalements prioritaires
DSA obligations (24h)
    ↓
Plateformes sur-modèrent
    ↓
Censure sans juge
```

L'État censure via des ONG qu'il finance, sans contrôle judiciaire préalable. La "société civile" est un paravent.

**Circuit 3 : La surveillance**

```
Chat Control CSS           eIDAS Art.45 CA           Euro numérique
       ↓                         ↓                         ↓
Scan messages              Interception HTTPS        Traçabilité paiements
       ↓                         ↓                         ↓
       └─────────────────────────┼─────────────────────────┘
                                 ↓
                    PROFIL CITOYEN COMPLET
```

Trois systèmes présentés comme "indépendants" et sans lien. Assemblés, ils permettent de reconstituer l'**intégralité du comportement numérique** d'un individu : ce qu'il dit (messages), ce qu'il consulte (navigation), ce qu'il achète (paiements).

**Le tableau des taux cachés** synthétise l'écart entre promesses et réalité :

| Système | Taux faux positifs réel | Taux officiel |
|---------|------------------------|---------------|
| PhotoDNA (LinkedIn) | 58% (44/75) | "1 sur 50 milliards" |
| PhotoDNA (Facebook) | 75% "non-malicious" | Non communiqué |
| PATRIOT Act sneak-peek | 0.9% terrorisme | "Anti-terrorisme" |

Dans chaque cas, les chiffres réels contredisent radicalement les justifications officielles.

👉 **Conséquence** : Des systèmes présentés comme distincts s'emboîtent pour créer une infrastructure de surveillance totale. Ce n'est plus de la paranoïa. C'est de l'ingénierie institutionnelle.

---

## XI - Le double standard de la "liberté de la presse"

La crédibilité des discours européens sur la liberté d'expression se mesure aussi à leur cohérence.

En 2022, l'Union européenne interdit la diffusion de **RT** (Russia Today) et **Sputnik**, médias russes accusés de désinformation systématique. Décision compréhensible dans le contexte de l'invasion de l'Ukraine.

En 2024, **Israël interdit Al Jazeera** sur son territoire, accusant la chaîne qatarie de soutenir le Hamas. 145 journalistes palestiniens sont tués à Gaza selon le CPJ (Committee to Protect Journalists). L'Union européenne... garde le silence.

**Reporters Sans Frontières** (RSF) condamne l'interdiction d'Al Jazeera — ce qui est cohérent. Mais RSF est elle-même classée "organisation indésirable" en Russie — au même titre que l'UE traite RT.

La structure de financement de RSF, documentée par SourceWatch, révèle :
- **40%+ de financement institutionnel** : MAE français, ministère de la Défense français, AFD
- **35% de fondations privées** : NED (National Endowment for Democracy, financé par le Congrès américain), Open Society (Soros), Ford Foundation

Robert Ménard, fondateur de RSF devenu maire RN de Béziers, a lui-même reconnu la dépendance historique de l'organisation aux "financements d'organisations américaines liées à la politique étrangère".

La critique n'est pas que RSF mente — ses rapports sont généralement factuellement solides. La critique est que RSF est **structurellement plus vocal sur les adversaires géopolitiques de l'Occident** (Russie, Chine, Cuba, Venezuela) que sur les abus des alliés (Israël, Arabie Saoudite, Maroc).

Freedom of the Press Foundation résume : "Le silence américain sur Al Jazeera en dit long sur ses politiques concernant TikTok et RT."

Le même double standard s'applique à la régulation européenne. Le DSA s'applique à X et TikTok. S'appliquera-t-il avec la même vigueur à un média européen qui diffuserait des contenus problématiques ? La question reste ouverte.

👉 **Conséquence** : La "liberté de la presse" et la "lutte contre la désinformation" sont des armes géopolitiques sélectives, pas des principes universels.

---

## XII - Les 15 loups : cartographie du pouvoir

Toute architecture de contrôle a des architectes. En voici quinze, documentés avec leurs rôles et leurs intérêts.

**Niveau Commission européenne**

| # | Acteur | Rôle | Note |
|---|--------|------|------|
| 1 | **Ursula von der Leyen** | Présidente CE | Promotrice du "pre-bunking", DSA comme norme mondiale |
| 2 | **Thierry Breton** (ex) | Ex-Commissaire Marché intérieur | Artisan DSA, "tyran de l'Europe" selon Musk |
| 3 | **Ylva Johansson** | Commissaire Affaires intérieures | Architecte Chat Control, "partner" de Thorn |

**Niveau national**

| # | Acteur | Rôle | Note |
|---|--------|------|------|
| 4 | **Emmanuel Macron** | Président France | "Domestiquer les réseaux sociaux" (Sarrebruck 2024) |
| 5 | **Martin Ajdari** | Président ARCOM | Nommé malgré avis défavorable Sénat |
| 6 | **Nancy Faeser** | Ministre Intérieur Allemagne | Position clé sur blocage Chat Control |

**Niveau plateformes**

| # | Acteur | Rôle | Note |
|---|--------|------|------|
| 7 | **Elon Musk** | Propriétaire X | Cible DSA, qualifie Breton de "tyran" |
| 8 | **Vincent Bolloré** | Groupe Canal+ | Propriétaire C8/CNews, perd TNT |
| 9 | **Pavel Durov** | Fondateur Telegram | Mis en examen France août 2024 |

**Niveau lobbying/ONG**

| # | Acteur | Rôle | Note |
|---|--------|------|------|
| 10 | **Ashton Kutcher** | Fondateur Thorn | Vend la tech qu'il promeut (600k€/an lobbying) |
| 11 | **Julie Cordua** | CEO Thorn | Correspondance directe avec Johansson |
| 12 | **Douglas Griffiths** | Oak Foundation | 24M$ vers écosystème pro-Chat Control |

**Niveau technique/régulation**

| # | Acteur | Rôle | Note |
|---|--------|------|------|
| 13 | **Nicholas Banasevic** | Ex-DG COMP → Microsoft | Pantouflage emblématique |
| 14 | **Roch-Olivier Maistre** | Ex-président ARCOM | Décisions C8/CNews sous son mandat |
| 15 | **Ralf Höcker** | Juriste allemand | Dénonce trusted flaggers comme "censure étatique" |

Ce réseau n'est pas une conspiration secrète. C'est un **écosystème d'intérêts convergents** où chaque acteur poursuit rationnellement ses objectifs — et où la résultante est une architecture de contrôle.

👉 **Conséquence** : L'architecture n'est pas abstraite. Elle a des visages, des intérêts, des réseaux traçables.

---

## CONCLUSION

L'Europe n'installe pas une dictature. Elle construit quelque chose de plus subtil et peut-être plus durable : une **algocratie ergonomique**. Un système où la surveillance est rationnelle, la censure préventive, et la conformité statistiquement inévitable.

Chaque dispositif isolé — DSA, Chat Control, eIDAS, euro numérique, ARCOM — peut se défendre individuellement. La protection des mineurs est légitime. La lutte contre la désinformation est compréhensible. L'identité numérique simplifie les démarches. La régulation des plateformes répond à des abus réels.

Mais leur **convergence** crée une infrastructure où :

- **La parole devient conditionnelle** — non plus un droit fondamental mais une permission révocable par algorithme, sans contrôle judiciaire préalable
- **Le citoyen devient suspect par défaut** — la présomption d'anomalie (scanning systématique) remplace la présomption d'innocence (surveillance ciblée sur mandat)
- **La résistance devient statistiquement improbable** — qui conteste un retrait automatique ? Qui lit les conditions d'utilisation ? Qui saisit les tribunaux pour un post supprimé ?

Le chiffre qui cristallise tout : **58%**. C'est le taux de faux positifs réel de PhotoDNA selon les études indépendantes. Contre "1 sur 50 milliards" promis par ses promoteurs. Cette omission n'est pas une erreur technique — c'est un **choix politique**. Si les citoyens européens connaissaient ce taux, voteraient-ils Chat Control avec la même légèreté ?

Le précédent historique est sans appel : le PATRIOT Act américain, créé pour le terrorisme, a été utilisé à **99,1%** pour autre chose. L'outil de surveillance créé pour un usage exceptionnel devient l'instrument de surveillance généralisée. Il n'y a pas d'exception à cette règle.

L'histoire ne retiendra pas : "Ils ont perdu leur liberté d'un coup."

Elle retiendra : **"Ils l'ont cédée morceau par morceau, application après application, protection après protection, dans le confort de l'indifférence."**

La vraie question n'est plus "la censure est-elle en place ?" — des mécanismes de contrôle existent, documentés, légaux. La question est : **"Qui décide des limites, avec quels contre-pouvoirs effectifs, et comment les citoyens peuvent-ils contester ?"**

Quand la réponse est "des algorithmes décident, les trusted flaggers signalent, les plateformes exécutent, et bonne chance pour contester" — le problème n'est plus technique.

Il est **démocratique**.

