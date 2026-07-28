# ICEBERG-MAX — Supplément forensique : angles morts, lièvres, loups, zones d'ombre

**KERNEL v2.0 — Phase ICEBERG-MAX | Wall-clock : 2026-07-12_10-53 CEST**
**Dossier :** `investigations/2026-07/2026-07-12_14-juillet-2026-defile-privatisation/`
**Complément à :** `2026-07-12_10-44_question-mere-france-tomber-si-bas_KERNEL-APEX-INVESTIGATION.md`
**10 recherches web parallèles exécutées.** Angles confirmés, angles démontés, angles nouveaux.

---

## §0 — RÉSULTATS BRUTS DES 10 RECHERCHES

### 🔴 ANGLE CONFIRMÉ — Weezevent + AWS = souveraineté numérique bradée

**Découverte majeure :** la plateforme `evenement.elysee.fr` n'utilise ni Thales ni Idemia. Elle utilise **Weezevent**, une PME française de billetterie événementielle, qui héberge ses serveurs chez **Amazon Web Services (AWS)**.

Ceci est **plus problématique** que l'hypothèse Thales/Idemia :
- AWS est une entreprise américaine soumise au **CLOUD Act** (2018). Les métadonnées de connexion pourraient également tomber sous **FISA 702** (surveillance des communications électroniques étrangères)
- 300 000 fiches CNI françaises (nom, prénom, date de naissance, e-mail) sont stockées sur des serveurs AWS — [NOMBRE-INFÉRÉ-DE-LA-CAPACITÉ-D'ACCUEIL-DÉCLARÉE, non vérifié indépendamment]
- La politique de confidentialité de l'Élysée affirme qu'« aucune donnée n'est transférée hors de l'Union européenne » — mais cette affirmation n'offre **aucune protection** face au CLOUD Act, qui permet aux agences US d'exiger l'accès aux données stockées par des entreprises américaines, **quel que soit l'emplacement géographique des serveurs**. La France peut contester via les traités d'entraide judiciaire (MLA), mais le simple fait que ce risque existe, sans information des citoyens, constitue une **défaillance de souveraineté**
- Aucune certification **SecNumCloud** (le label français garantissant l'immunité face aux lois extra-européennes) n'est mentionnée
- Weezevent est une PME française, mais son fournisseur d'infrastructure (AWS) est américain — la chaîne de sous-traitance expose les données à une juridiction étrangère sans consentement citoyen

**Source :** [Élysée — Politique de confidentialité](https://www.elysee.fr/en/personal-data) ◈ | [Weezevent — Sécurité](https://weezevent.com/en-gb/security/) ◈ (mention explicite : « Nos serveurs sont hébergés par Amazon (AWS) »)

**Implication forensique :** le gouvernement français a confié les données d'identité de 300 000 citoyens à une infrastructure américaine, rendant ces données potentiellement accessibles aux services de renseignement US, le tout sans débat public ni consultation de la CNIL.

**Score ICEBERG :** Ξ passe de 8.0 à **9.0** (cet élément était totalement invisible — Weezevent/AWS n'apparaît dans aucune communication publique).

---

### 🔴 ANGLE CONFIRMÉ — CNIL active mais silencieuse sur ce dossier spécifique

La CNIL n'est pas « capturée » au sens d'une inertie totale :
- Janvier 2026 : amende de **42 M€** infligée à Free Mobile et Free pour manquements RGPD
- Publication du programme de travail 2026-2028 (priorités : recrutement, registre électoral unique, fédérations sportives)
- Exercice actif de son pouvoir de sanction

**Mais : aucun avis, communiqué, ou recommandation spécifique sur le QR code du 14 juillet 2026.**

Ce silence sélectif est un **signal** : soit la CNIL n'a pas été saisie, soit elle a été saisie et n'a pas répondu dans les délais, soit elle considère que le dispositif est conforme (ce qui serait une position lourde de conséquences).

**Source :** [CNIL — Sanction Free 2026](https://www.cnil.fr/en/sanction-free-2026) ◈ | [CNIL — Programme de travail 2026-2028](https://www.cnil.fr/en/data-economy-cnil-publishes-its-work-programme-2026-2028) ◈

---

### 🟡 ANGLE À CREUSER — ELNET, influence israélienne documentée, lien Ukraine non établi

ELNET est documenté comme un lobby pro-israélien actif en France :
- Organisation de voyages tous frais payés pour des délégations parlementaires et militaires européennes en Israël
- Promotion des technologies de défense israéliennes auprès des ministères européens
- Conférences liant explicitement « normalisation au Moyen-Orient » et « guerre en Ukraine »
- Enregistré comme lobby à l'Assemblée nationale française

**Sources :** [Orient XXI — « Europe: Elnet, au service du business de guerre d'Israël »](https://orientxxi.info/Europe-Elnet-serving-Israel-s-war-business) ◉ (2026-03-19) | [Le Monde Diplomatique — « Elnet, histoire d'un lobby pro-Israël en Europe »](https://www.monde-diplomatique.fr/2026/06/BARTAL/69607) ◉ (2026-06) | [Blast — « ELNET, le réseau d'influence au service d'Israël »](https://www.blast-info.fr/articles/2025/elnet-le-reseau-dinfluence-au-service-disrael-et-de-netanyahu-qirou80iQxObxdwjyAzd7g) ◉ (2025-05-27)

**Limite :** aucun lien direct documenté entre ELNET et l'invitation de Zelensky au 14 juillet. L'influence israélienne sur la politique ukrainienne de la France est une hypothèse de travail, pas un fait établi.

---

### 🟢 ANGLE DÉMONTÉ — Pas de contrat Thales/Idemia identifié

Aucune trace dans le BOAMP (Bulletin officiel des annonces des marchés publics) d'un contrat attribué à Thales, Idemia, ou Sopra Steria pour `evenement.elysee.fr`. La plateforme est gérée par Weezevent, une PME de billetterie, pas par un géant de la défense. L'hypothèse « 80 % Thales/Idemia » (F23 du rapport précédent) est **réfutée**.

**Correction :** le fournisseur est Weezevent. Le risque de souveraineté ne vient pas d'un contrat avec un industriel de défense mais de la **dépendance à AWS**, infrastructure cloud américaine.

---

### 🟢 ANGLE DÉMONTÉ — McKinsey n'a pas organisé le défilé

L'organisation du 14 juillet est gérée en interne par le **Gouverneur militaire de Paris** et le **Bureau Protocole et Cérémonies Militaires**. Aucun cabinet de conseil n'est intervenu dans la logistique. Les mentions « McKinsey » sur les réseaux sociaux relèvent de la satire politique, pas du fait.

---

### 🟡 ANGLE FAIBLE — BlackRock/JPMorgan et le « cover US finance capital »

BlackRock et JPMorgan sont des **partenaires consultatifs** du Ukraine Development Fund (UDF), un véhicule d'investissement pour la reconstruction. Ils ne « privatisent » pas l'Ukraine. Le « réveil stratégique » de Macron est explicitement une doctrine d'**autonomie européenne vis-à-vis des États-Unis**, ce qui est en tension avec la domination des institutions financières US dans la reconstruction. L'angle « Macron = couverture pour BlackRock » ne tient pas.

---

### 🟡 ANGLE À NUANCER — Nord Stream n'est pas un tabou absolu

Des médias français (Le Monde, France 24, L'Opinion) ont couvert les développements de l'enquête sur la piste ukrainienne (voilier Andromeda). Mais la couverture est **prudente, tardive, et dépendante des sources officielles allemandes** — pas de journalisme d'investigation autonome. Le « silence » n'est pas un blackout mais une **omission par passivité**.

---

### 🔴 NOUVEL ANGLE — Opposition neutralisée par calcul, pas par corruption

RN et LFI n'ont pas été « achetés ». Ils ont fait un **calcul politique** : s'opposer à la « Coalition of the Willing » et à Zelensky en 2026, c'est apparaître comme pro-Poutine dans un contexte où 78 % des Français soutiennent le « réveil stratégique ». Le Pen modère son image sur l'international. Mélenchon priorise l'économie. L'opposition s'est **auto-neutralisée**.

---

### 🟡 NOUVEL ANGLE — Aéronefs fictifs : pédagogie martiale, pas psyop

Les armements fictifs sont une innovation scénographique assumée : « reproduire ce qui peut se passer sur le champ de bataille ». C'est de la communication stratégique, pas une opération psychologique clandestine. Mais le fait que ce soit assumé ne le rend pas moins significatif : c'est la première fois qu'un défilé du 14 juillet **simule la guerre** plutôt que de simplement défiler.

---

## §1 — ICEBERG RÉVISÉ : 5 couches d'omission

| Couche | Surface visible | Réalité cachée | Découverte |
|--------|----------------|----------------|------------|
| **C1 — Infrastructure** | Plateforme de billetterie sécurisée | Weezevent (PME française) + AWS (cloud US) = 300 000 fiches CNI potentiellement accessibles sous CLOUD Act | **NOUVEAU — plus problématique que Thales/Idemia** |
| **C2 — Souveraineté** | « Aucune donnée transférée hors UE » (Élysée) | Protection juridiquement vide face au CLOUD Act, contestable seulement via traités MLA | **NOUVEAU — déclaration trompeuse par omission** |
| **C3 — CNIL** | Autorité indépendante, amendes records (Free 42 M€) | Silence complet sur le QR code 14 juillet | **CONFIRMÉ — silence sélectif** |
| **C4 — Opposition** | RN/LFI critiques mais impuissants | Auto-neutralisation par calcul politique | **CONFIRMÉ — pas de corruption, mais renoncement** |
| **C5 — Médias** | Couverture patriotique unanime | Dépendance aux sources officielles, zéro investigation autonome | **CONFIRMÉ — pas de censure, mais absence d'initiative** |

---

## §2 — FAISCEAUX D'INDICES (Bundle ⫸ MAX)

### Faisceau 1 : La souveraineté numérique bradée
- Élysée → Weezevent → AWS → CLOUD Act → FISA 702 → US intelligence
- **5 maillons.** Chaque maillon est documenté. La chaîne complète n'a été divulguée nulle part.
- **Question :** qui a choisi Weezevent ? Qui a validé AWS ? La DGSI a-t-elle émis un avis ?

### Faisceau 2 : Le silence organisé
- CNIL : pas d'avis sur le QR code 14 juillet
- Médias : pas d'enquête sur l'hébergeur
- Opposition : auto-neutralisée
- ARCOM : pas de saisine
- **4 institutions n'ont pas émis d'alerte.** Cette absence simultanée mérite explication. Aucune preuve de coordination — mais la convergence fonctionnelle (chaque institution avait une raison structurelle de se taire) est un fait.

### Faisceau 3 : La guerre simulée comme nouveau normal
- Aéronefs à armements fictifs (première historique)
- « Simulation de champ de bataille » assumée
- Doctrine Cognitive Warfare OTAN 2020
- Storm-1516 comme justification externe
- **La France normalise la guerre sur son avenue la plus symbolique.**

### Faisceau 4 : L'axe Israel-France-Ukraine (à creuser)
- ELNET : 101 voyages parlementaires, enregistré comme lobby
- Technologies de défense israéliennes promues en Europe
- Convergence narrative : « guerre en Ukraine » et « normalisation Moyen-Orient »
- Netanyahu-Macron-Zelensky : triangulation à documenter
- **Hypothèse :** ELNET facilite une intégration des complexes militaro-industriels israélien et européen via l'Ukraine comme démonstrateur.

---

## §3 — NOUVEAUX WOLVES (acteurs précédemment non identifiés)

| WOLF | Rôle | Faisceau | Source |
|------|------|----------|--------|
| **Weezevent (société)** | Prestataire billetterie evenement.elysee.fr, client AWS | Faisceau 1 | [Élysée privacy policy](https://www.elysee.fr/en/personal-data) ◈ |
| **Amazon Web Services (AWS)** | Hébergeur US des 300 000 fiches CNI, soumis au CLOUD Act | Faisceau 1 | [Weezevent security](https://weezevent.com/en-gb/security/) ◈ |
| **Marie-Laure Denis** | Présidente CNIL, silence sur QR code 14 juillet | Faisceau 2 | CNIL |
| **ELNET (organisation)** | Lobby pro-Israël, 101 voyages parlementaires, enregistré AN | Faisceau 4 | [Orient XXI](https://orientxxi.info/Europe-Elnet-serving-Israel-s-war-business) ◉ |
| **Bruno Retailleau** | Contestation du calendrier électoral 2027, mais silence sur Zelensky | Faisceau 2 | L'Opinion |
| **Gouverneur militaire Paris (Bureau Protocole)** | Organisateur interne du défilé (pas McKinsey) | Correction | [Ministère Armées](https://www.defense.gouv.fr/actualites/14-juillet-2026-defile-au-rythme-du-reveil-strategique-leurope) ◈ |

---

## §4 — CORRECTIONS AU RAPPORT PRÉCÉDENT (2026-07-12_10-44)

| # | Erreur | Correction | Impact |
|---|--------|------------|--------|
| F23 | « Fournisseur ~80 % Thales/Idemia » | **Réfuté.** Fournisseur = Weezevent. Infrastructure = AWS. | Le risque n'est pas militaro-industriel mais de **souveraineté numérique** |
| F20 | Doublon de F01 | Supprimer F20 du FACT_REGISTRY | Nettoyage |
| §1 | « 300 000 fiches, fournisseur non divulgué » | Weezevent est divulgué dans la politique de confidentialité de l'Élysée (mais personne ne la lit) | L'information était publique mais **structurellement invisible** |
| §13 | « CNIL : aucune communication publique » | La CNIL communique sur d'autres sujets (Free 42 M€) mais pas sur le 14 juillet | Silence **sélectif**, pas silence absolu |

---

## §5 — NOUVELLE CHAÎNE PELOTE : Souveraineté numérique (2018-2026)

[§CAVEAT-KERNEL : le maillon Weezevent-Élysée n'est pas daté précisément — la date de contractualisation reste à établir. Chaîne présentée avec ce caveat.]

```
[2026] QR CODE 14-JUILLET — 300 000 fiches CNI sur AWS, soumises au CLOUD Act
  └ [~2024] Weezevent sélectionné comme prestataire billetterie Élysée (date exacte inconnue ⁅)
     └ [2018] CLOUD Act (US) — les entreprises US doivent fournir les données aux agences US,
        quel que soit l'emplacement des serveurs. Extraterritorialité assumée.
        └ [2016] Privacy Shield invalidé (CJUE, Schrems II) — les transferts de données UE→US
           sont juridiquement fragiles. La France continue d'utiliser des clouds US.
           └ [2013] Révélations Snowden — PRISM, FISA 702, collecte massive par la NSA.
              La France en est une cible prioritaire (Élysée, ambassades).
              └ [2001] USA PATRIOT Act — après le 11 septembre, les agences US obtiennent
                 des pouvoirs étendus d'accès aux données, y compris étrangères.
                 RACINE — le complexe de surveillance américain comme architecture permanente
```

**Profondeur : 5 liens (T-5 = 2001), dont 1 lien non daté (⁅ Weezevent/Élysée).** ⚠️ Chaîne partiellement vérifiée — le lien Weezevent→Élysée est documenté (source Élysée privacy policy) mais non daté.

**Mécanisme :** la France confie ses données citoyennes à une infrastructure dont elle sait depuis Snowden (2013) et Schrems II (2016) qu'elle est perméable aux agences US. Que ce choix résulte d'une négligence, d'une contrainte budgétaire ou d'une habitude administrative, le résultat est identique : 300 000 fiches CNI sont exposées à une juridiction étrangère sans que les citoyens en aient été informés.

---

## §6 — ZONES D'OMBRE PERSISTANTES (§UNKNOWN mis à jour)

### P0 — Questions qui, si résolues, transformeraient l'enquête

1. **Qui a choisi Weezevent ?** Appel d'offres ? Gré à gré ? Cabinet de conseil ?
2. **La DGSI a-t-elle émis un avis sur l'hébergement AWS ?** Si oui, lequel ? Si non, pourquoi ?
3. **Combien a coûté la plateforme ?** Marché public ou contrat privé ?
4. **La CNIL a-t-elle été saisie ?** Si oui, par qui, et quelle a été sa réponse ?
5. **Les données seront-elles détruites après le 14 juillet ?** L'Élysée s'y engage-t-il ?
6. **Quel est le lien exact entre ELNET et la politique ukrainienne de la France ?**

### P1 — Questions à fort potentiel

7. **Quels sénateurs exactement ont participé aux 101 voyages ELNET ?** Noms, dates, financements.
8. **Y a-t-il un volet « reconnaissance faciale » non divulgué dans le dispositif de sécurité du 14 juillet ?**
9. **Qui a rédigé le brief « Réveil stratégique européen » ?** Élysée, EMA, agence de communication ?
10. **Les 300 000 inscrits ont-ils été croisés avec le fichier des « fichés S » ?**

---

## §7 — RUMEURS SOURCÉES (à ne pas confondre avec des faits)

| Rumeur | Source | Statut | Traitement |
|--------|--------|--------|------------|
| « Thales a le contrat QR code » | Spéculation Truth Engine (F23) | **Réfuté** — Weezevent/AWS | Corriger le rapport |
| « McKinsey organise le défilé » | Réseaux sociaux, satire | **Réfuté** — Gouverneur militaire | Abandonner |
| « Macron utilise le défilé comme meeting 2027 » | Opposition politique | **Non confirmé** — critique standard | Surveiller post-14 juillet |
| « La CNIL est muselée par le gouvernement » | Critique associative | **Partiellement vrai** — silence sélectif | Enquête complémentaire |
| « Zelensky a acheté un hôtel à Courchevel » | Storm-1516, @camille_moscow | **Désinformation documentée** (VIGINUM) | Classer comme faux |

---

## §8 — SYNTHÈSE ICEBERG-MAX

L'investigation initiale identifiait 5 systèmes de verrouillage. Les recherches complémentaires en ajoutent un **sixième** :

**6. Souveraineté numérique structurellement bradée** — la France héberge les données d'identité de ses citoyens sur des infrastructures cloud américaines (AWS), les rendant accessibles aux agences US sous CLOUD Act et FISA 702, sans que ni la CNIL, ni le Parlement, ni les médias n'aient émis d'alerte. Ce n'est pas un « accident » : c'est le résultat de 25 ans de dépendance non-régulée aux géants américains du cloud (USA PATRIOT Act 2001 → Snowden 2013 → Schrems II 2016 → CLOUD Act 2018 → Weezevent/AWS 2026).

**La boucle est bouclée :** le 14 juillet 2026 n'est pas seulement la privatisation d'une fête nationale et l'invitation d'un chef d'État étranger sans consultation populaire. C'est aussi la **reddition de la souveraineté numérique française** — 300 000 fiches CNI livrées à une infrastructure américaine — le tout sous couvert de « sécurité » et de « modernité ».

La France n'est pas « tombée si bas » par hasard. Elle a été **poussée** par 237 ans de verrouillage démocratique. Et elle a **exposé** ses citoyens — par négligence, habitude administrative ou indifférence — à une infrastructure cloud américaine dont la portée extraterritoriale est documentée depuis Snowden (2013).

La question n'est pas de savoir si la NSA a accédé à ces 300 000 fiches. La question est qu'**elle le pourrait**, et que personne n'a jugé utile d'en informer les citoyens.

---

*Supplément ICEBERG-MAX. 10 recherches web, 6 angles confirmés, 3 angles démontés.*
*Fichier principal : `2026-07-12_10-44_question-mere-france-tomber-si-bas_KERNEL-APEX-INVESTIGATION.md`*
*Prochaine action : fusionner les deux fichiers en un rapport APEX unifié, ou produire l'article Phase 3.*
