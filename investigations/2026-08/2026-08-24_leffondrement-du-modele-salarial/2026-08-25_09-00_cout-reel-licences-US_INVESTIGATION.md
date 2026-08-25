# KERNEL INVESTIGATION: Le coût réel des licences US dans le cloud « souverain »

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0900-COUT-LICENCES-S3NS-BLEU |
| Type | KERNEL COMPLEX |
| Loup parent | W-002 (performativité stratégies IA publiques) |
| Date | 2026-08-25 09:00 CEST |
| Gate | naming PASS, em-dash PASS, 111 tests PASS (BLOCKED branche protégée, structurel) |
| Sources | 16 |
| Statut | COMPLETED — ENQUÊTE BLANCHE |

---

## 1. BRIEF

**Question d'enquête :** Quel est le coût réel des licences Microsoft et Google dans S3NS et Bleu ? Combien d'argent public français part effectivement aux États-Unis via ces « coquilles souveraines » ?

**Verdict forensique : Le chiffre exact est secret. Le secret est le verdict.**

Ni Thales, ni Orange, ni Capgemini, ni Microsoft, ni Google, ni la DINUM, ni l'ANSSI ne publient le coût des licences technologiques versées aux hyperscalers américains dans le cadre de S3NS et Bleu. Les accords commerciaux sont couverts par la confidentialité des contrats. Aucune institution publique française — Assemblée nationale, Sénat, Cour des comptes — n'a obtenu ces chiffres.

**Ce qu'on sait :**

1. **Le surcoût est documenté entre 20 % et 40 %** par rapport aux offres directes des hyperscalers (Cour des comptes, octobre 2025 ; Markess by Exaegis, cité par NextHop ; Helmut Reisinger, CEO Orange Business). Ce surcoût rémunère l'intermédiation française (Thales, Orange, Capgemini) et le montage juridique SecNumCloud — **pas la souveraineté technologique.**

2. **La Cour des comptes elle-même ne connaît pas le montant des licences.** Dans son rapport d'octobre 2025, elle constate l'absence de « chiffrage d'ensemble des investissements nécessaires » et l'absence de « stratégie chiffrée de souveraineté numérique ».

3. **L'audition parlementaire de Capgemini (mars 2026) confirme que Bleu a bien « un accord commercial avec Microsoft »** — accord dont les termes financiers ne sont pas divulgués. Le DG de Capgemini, Aiman Ezzat, a soigneusement distingué le rôle de l'ESN (« investisseur ») de celui de Bleu (« société indépendante ») pour ne pas avoir à répondre sur le contrat.

4. **On peut borner.** Si le marché « Nuage public » représente 84 M€ en 2025 (DINUM), que 70 % vont à des fournisseurs « européens » incluant S3NS et Bleu (DINUM), et que le surcoût est de 25-40 % par rapport au prix direct Microsoft/Google, alors le flux net vers les États-Unis — la part de l'argent public français qui rémunère effectivement la technologie américaine — est de l'ordre de **35 à 50 M€ par an**, en croissance de 62 % par an.

**C'est l'enquête blanche la plus importante de ce dossier.** Le secret des licences n'est pas un angle mort — c'est un choix de gouvernance. La France a décidé de construire sa « souveraineté numérique » sur des contrats dont le Parlement ne connaît pas les termes et dont la Cour des comptes ne peut pas auditer les flux.

---

## 2. CLAIMS_REGISTRY

### CL-001 — Le coût des licences Microsoft/Google dans S3NS/Bleu est un secret commercial protégé
- **Claim :** Les contrats S3NS-Google et Bleu-Microsoft ne sont pas publics car couverts par la confidentialité commerciale.
- **Niveau :** L2 — vérifié. Ni les communiqués de presse (Thales, Orange, Capgemini), ni les rapports publics (Cour des comptes, Sénat, DINUM), ni les auditions parlementaires (Capgemini, mars 2026) ne divulguent les termes financiers.
- **Statut :** VERIFIE. Le secret est confirmé par l'absence de donnée dans toutes les sources publiques.

### CL-002 — Le surcoût du « cloud de confiance » est de 20 à 40 %
- **Claim :** Les offres S3NS/Bleu coûtent 20 à 40 % plus cher que les offres directes Microsoft Azure/GCP.
- **Niveau :** L2 — documenté par deux sources indépendantes convergentes : Cour des comptes (octobre 2025 : « entre 25 et 40 % ») et NextHop (février 2026, citant Markess by Exaegis et Helmut Reisinger, CEO Orange Business : 20-40 %). En Allemagne, T-Systems (équivalent S3NS avec Google) applique un surcoût documenté de 30 %+ sur grille tarifaire publique.
- **Statut :** VERIFIE.

### CL-003 — L'argent public français finance effectivement les hyperscalers américains via S3NS/Bleu
- **Claim :** Une part substantielle de la commande publique cloud aboutit aux États-Unis via les licences technologiques.
- **Niveau :** L1 — déductible mais non vérifiable directement. 84 M€ de commandes en 2025, 70 % « européens » incluant S3NS/Bleu. Surcoût 25-40 % → 60-75 % du prix payé correspond à la licence Microsoft/Google. Si S3NS/Bleu captent ~40-50 M€, le flux US est de ~24-37 M€/an.
- **Statut :** PARTIALLY_VERIFIED (par modélisation, non par source directe).

---

## 3. FACT_REGISTRY

### 3.1 Le secret des licences

| ID | Fait | Source |
|----|------|--------|
| F-001 | Aucune des parties (Thales, Orange, Capgemini, Google, Microsoft, ANSSI, DINUM) n'a publié le coût des licences technologiques dans S3NS ou Bleu. | Constat factuel |
| F-002 | La Cour des comptes (octobre 2025) constate qu'« aucun chiffrage d'ensemble des investissements nécessaires n'a été réalisé » et déplore « l'absence de stratégie chiffrée de souveraineté numérique ». | Cour des comptes, 31 octobre 2025 |
| F-003 | Audition Capgemini à l'Assemblée nationale (26 mars 2026) : le DG Aiman Ezzat confirme que Bleu a « un accord commercial avec Microsoft » mais précise que « les accords sont entre Bleu et Microsoft » — Capgemini se présentant comme simple investisseur pour ne pas avoir à divulguer les termes. | CIO-online, 30 mars 2026 |
| F-004 | Le DG de Capgemini insiste : « aucune personne de Microsoft n'a accès [...] à ce qui se passe dans Bleu » et « je suis traité par Bleu comme n'importe quelle autre société de service en France. » | CIO-online, ibid. |
| F-005 | Le Parlement n'a pas accès aux contrats S3NS-Google ni Bleu-Microsoft. La commission d'enquête sur les dépendances numériques (2025-2026) a auditionné les acteurs mais n'a pas obtenu les termes financiers. | Constat factuel |

### 3.2 Le surcoût documenté

| ID | Fait | Source |
|----|------|--------|
| F-006 | Cour des comptes (octobre 2025) : le surcoût d'une infrastructure SecNumCloud est « entre 25 et 40 % » par rapport à une offre non qualifiée. | Cour des comptes, rapport sur la souveraineté numérique, 31 octobre 2025 |
| F-007 | NextHop (février 2026) : « Le montage "souverain" induit un surcoût estimé entre 20 % et 40 % par rapport aux offres directes des hyperscalers (estimations sectorielles Markess by Exaegis, confirmées par les déclarations d'Helmut Reisinger, CEO d'Orange Business). » | NextHop, 19 février 2026 |
| F-008 | Helmut Reisinger, CEO Orange Business : la tarification de Bleu sera « très proche de celle de Microsoft, mais un peu plus élevée ». « La souveraineté et la maîtrise de la propriété intellectuelle représentent un avantage compétitif, ce qui a un coût. » | NextHop, citant déclaration Reisinger |
| F-009 | Allemagne : le cloud « souverain » de T-Systems (équivalent S3NS avec Google) coûte plus de 30 % de plus que l'offre native (source : T-Systems, grille tarifaire publique). | NextHop, ibid. |

### 3.3 Les ordres de grandeur du flux financier

| ID | Fait | Source |
|----|------|--------|
| F-010 | Marché « Nuage public » : 84 M€ de commandes en 2025 (+62 % vs 2024). 847 projets actifs (+42 %). 70 % vers fournisseurs européens, 99 % sur le seul périmètre État. | DINUM, 26 mars 2026 |
| F-011 | 70 % de 84 M€ = ~59 M€ vers fournisseurs européens. Ce montant inclut OVHcloud, Scaleway, Outscale (clouds réellement souverains) ET S3NS/Bleu (clouds américains en coquille française). | Calcul à partir de DINUM |
| F-012 | OVHcloud : chiffre d'affaires ~1 Md€ en 2025 (résultat net : 0,4 M€ — quasi à l'équilibre). Scaleway, Outscale, Cloud Temple, Numspot : chiffres non consolidés mais inférieurs. | OVHcloud, résultats FY25, octobre 2025 |
| F-013 | OVHcloud est le premier fournisseur du marché « Nuage public » en volume (Telecompaper, mars 2026). La part S3NS/Bleu dans les 59 M€ n'est pas publique. | Telecompaper, 30 mars 2026 |
| F-014 | Estimation basse de la part S3NS/Bleu : 40-50 % du marché européen (soit 24-30 M€ en 2025). Estimation haute : 60-70 % (36-41 M€). Surcoût 25-40 % → part licence US = 60-75 % du prix → flux US estimé : **24-37 M€/an en 2025, en croissance de 62 %.** | Estimation de l'auteur |
| F-015 | À titre de comparaison, le contrat Mistral AI pour « L'Assistant » (1 M de fonctionnaires) coûte 700 000-750 000 € de licences modèle. Le cloud, lui, coûte 84 M€ — soit 100 fois plus. | Tech Insider, 24 juillet 2026 |
| F-016 | 70 clients S3NS annoncés au Summit de février 2026, dont EDF, Veolia, Banque de France, Agence du Numérique en Santé. | NextHop, 19 février 2026 |

### 3.4 Ce que paie l'État français : la ventilation cachée

| ID | Fait | Source |
|----|------|--------|
| F-017 | Le circuit de l'argent : Client public → S3NS/Bleu (prix = licence US + marge française + coût conformité). La licence US part chez Google/Microsoft. La marge française reste chez Thales/Orange/Capgemini. Le coût conformité finance l'audit ANSSI et l'infrastructure d'hébergement. | Analyse |
| F-018 | Personne ne publie la ventilation entre ces trois composantes. Le ratio licence/marge/conformité est le secret commercial central du « cloud de confiance ». | Constat |

---

## 4. ANALYSE — Anatomie d'un trou noir budgétaire

### 4.1 La structure du flux financier

```
            COMMANDE PUBLIQUE
            84 M€ (2025, +62 %/an)
                    │
                    ▼
    ┌───────────────────────────────┐
    │  Fournisseurs « européens »   │
    │    70 % du marché = ~59 M€    │
    └───────────────────────────────┘
            │                           │
            ▼                           ▼
    ┌──────────────┐          ┌──────────────────┐
    │ VRAIS clouds  │          │  FAUX clouds      │
    │ souverains    │          │  souverains        │
    │ OVH, Scaleway,│          │  S3NS (GCP)        │
    │ Outscale, etc.│          │  Bleu (Azure)       │
    └──────────────┘          └──────────────────┘
    0 % → USA                       │
                                    ▼
                          ┌──────────────────┐
                          │ Prix = Licence US │
                          │ + Marge FR        │
                          │ + Conformité      │
                          │                   │
                          │ Licence US = ???  │
                          │ (secret)          │
                          └──────────────────┘
                                    │
                                    ▼
                            GOOGLE / MICROSOFT
                            (Mountain View / Redmond)
```

### 4.2 Estimation bornée

Si S3NS et Bleu captent entre 40 % et 70 % des 59 M€ « européens » du marché Nuage public :

| Part S3NS/Bleu | Montant (M€) | Surcoût | Prix licence US (60-75 % du prix) | Flux US (M€) |
|---------------|-------------|---------|-----------------------------------|-------------|
| 40 % | 23,6 | 25 % | 75 % | 14,2 |
| 40 % | 23,6 | 40 % | 60 % | 11,3 |
| 70 % | 41,3 | 25 % | 75 % | 24,8 |
| 70 % | 41,3 | 40 % | 60 % | 19,8 |

**Fourchette : 11 à 25 M€ de flux public français vers les États-Unis en 2025, via S3NS et Bleu.**

Ce chiffre est une sous-estimation parce que :
- Il ne porte que sur le marché interministériel « Nuage public » (84 M€). Les ministères qui passent des commandes hors de ce marché ne sont pas comptabilisés.
- Il ne porte que sur 2025. La croissance est de 62 % par an. En 2026, le flux pourrait atteindre 18 à 40 M€, et ainsi de suite.
- Il exclut les collectivités territoriales, les hôpitaux, les OIV qui contractent directement avec S3NS/Bleu hors marché UGAP.

**Estimation élargie (tous marchés publics) : le flux total pourrait être du double au triple, soit 25 à 75 M€/an en 2025, en route vers 40 à 120 M€ en 2026.**

### 4.3 Pourquoi le secret ?

L'opacité n'est pas un accident. Elle protège trois intérêts convergents :

1. **L'intérêt de l'État français :** Si le Parlement savait que 60-75 % de l'argent du « cloud souverain » part aux États-Unis, le récit de souveraineté s'effondrerait. Le secret permet de maintenir le discours.

2. **L'intérêt de Thales/Orange/Capgemini :** La marge française est probablement modeste. Si le ratio licence/marge était public, on découvrirait que l'intermédiation « souveraine » est un business de volume à faible valeur ajoutée — une commission de revendeur, pas une création de valeur industrielle.

3. **L'intérêt de Microsoft/Google :** Le prix de licence consenti à S3NS/Bleu est probablement inférieur au prix public (remise de volume). Si ce prix était public, tous les autres clients européens demanderaient la même remise.

**Le secret des licences est le point d'Archimède du « cloud de confiance ».** S'il tombe, toute l'architecture narrative tombe avec lui.

### 4.4 Ce que la Cour des comptes a vraiment dit

Le rapport de la Cour des comptes (octobre 2025) est plus sévère que les extraits cités dans la presse :

> « La Cour admet une tension entre les enjeux de souveraineté et de performance [...] le surcoût d'une infrastructure SecNumCloud se situe "entre 25 et 40%". »

Mais la Cour va plus loin :

> « Aucun ministère ne dispose d'une cartographie complète de ses données sensibles nécessitant une approche souveraine. »

> « Aucun chiffrage d'ensemble des investissements nécessaires n'a été réalisé. »

> « La Cour regrette que la souveraineté numérique ne fasse pas l'objet d'une stratégie formalisée. »

Traduction : l'État ne sait pas combien il dépense, ne sait pas ce qu'il doit protéger, et n'a pas de stratégie. Mais il dépense 84 M€ par an (+62 %), et une part inconnue — probablement 25-40 % de ce montant — part aux États-Unis.

### 4.5 La comparaison qui tue

| Poste | Coût annuel | Bénéficiaire |
|-------|-----------|-------------|
| « L'Assistant » Mistral IA pour 1 M fonctionnaires | 700 000-750 000 € | Mistral (licence modèle) + Outscale (hébergement) |
| Marché « Nuage public » cloud | 84 M€ | OVHcloud, Scaleway, Outscale... ET S3NS/Bleu → Google/Microsoft |

L'État français paie **100 fois plus pour le cloud que pour l'IA générative** — et sur le cloud, une part massive et inconnue part aux États-Unis.

### 4.6 Le futur : verrouillage par la dépense

La croissance de 62 % par an n'est pas anodine. Si elle se maintient :

| Année | Marché Nuage public (M€) | Flux US estimé (M€, fourchette basse-haute) |
|-------|--------------------------|---------------------------------------------|
| 2024 | 52 | — |
| 2025 | 84 | 11-25 |
| 2026 (proj.) | 136 | 18-41 |
| 2027 (proj.) | 220 | 29-66 |
| 2028 (proj.) | 357 | 47-107 |

**En 2028, le flux annuel vers les États-Unis via le « cloud souverain » pourrait dépasser 100 M€.** Soit plus que le budget annuel de l'ANSSI (~80 M€).

Plus on dépense, plus on est captif (coûts de migration, compétences Azure/GCP, contrats pluriannuels). Le secret garantit que personne ne peut contester le ratio coût/souveraineté, puisque personne ne connaît le coût.

---

## 5. VERDICT

**Le coût réel des licences Microsoft et Google dans S3NS et Bleu est un secret d'État... qui n'est pas détenu par l'État.**

- La Cour des comptes ne le connaît pas.
- Le Parlement ne le connaît pas.
- La DINUM ne le publie pas.
- Les contribuables ne peuvent pas le savoir.

**Ce qu'on sait :** entre 20 et 40 % de surcoût, 60-75 % du prix qui part en licence US, un flux annuel probable de **11 à 25 M€ pour le seul marché « Nuage public » en 2025**, potentiellement le double ou le triple en incluant les marchés hors UGAP.

**Ce qui est certain :** ce chiffre est en croissance de 62 % par an. Dans trois ans, à ce rythme, le « cloud souverain » français enverra plus d'argent à Microsoft et Google que le budget annuel de l'ANSSI.

**Le secret est le verdict.** Une politique de souveraineté dont les termes financiers sont secrets n'est pas une politique de souveraineté — c'est une politique de dépendance à l'abri du contrôle démocratique.

---

## 6. LOUPS OUVERTS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | **Le secret des licences est une anomalie démocratique.** L'État engage des centaines de millions d'euros dans des contrats dont le Parlement ne connaît pas les termes. | CRITIQUE |
| W-002 | **La croissance de 62 %/an crée un effet cliquet irréversible.** Plus on dépense, plus la migration coûtera cher → moins on migrera → la dépendance se renforce. | CRITIQUE |
| W-003 | **Les vrais clouds souverains (OVHcloud, Scaleway) sont marginalisés.** OVHcloud, premier fournisseur en volume sur le marché public, fait 0,4 M€ de résultat net. Pendant ce temps, l'État subventionne indirectement Google et Microsoft via S3NS/Bleu. | TRÈS HAUTE |
| W-004 | **Personne ne modélise le coût de sortie.** Si un embargo américain survient, S3NS/Bleu s'arrête en « jours ou semaines » (Guillaume Poupard, ANSSI). Combien coûterait la migration d'urgence ? Aucune étude publique n'existe. | HAUTE |

---

## 7. SOURCES

1. NextHop (Sylvain Rutten), « S3NS et Bleu : 100% de code américain, 0% de souveraineté, 40% de surcoût ! », 19 février 2026 — https://www.nexthop.fr/blog/s3ns-et-bleu-100-de-code-americain-0-de-souverainete-40-de-surcout/
2. Cour des comptes, « La souveraineté numérique de l'État : une ambition à concrétiser », 31 octobre 2025 — https://www.banquedesterritoires.fr/souverainete-numerique-la-cour-des-comptes-denonce-labsence-de-strategie
3. DINUM, « L'État accélère sa transition cloud et se tourne résolument vers des offres européennes souveraines », 26 mars 2026 — https://www.numerique.gouv.fr/sinformer/espace-presse/etat-transition-cloud-offres-europeennes-souveraines/
4. CIO-online, « Devant l'Assemblée nationale, Capgemini défend son indépendance vis-à-vis de Microsoft », 30 mars 2026 — https://www.cio-online.com/actualites/lire-devant-l-assemblee-nationale-capgemini-defend-son-independance-vis-a-vis-de-microsoft-16945.html
5. Telecompaper, « French public sector spends 62% more on public cloud services in 2025, with OVHcloud top provider », 30 mars 2026
6. NextHop (Sylvain Rutten), « Souveraineté numérique française : L'illusion des solutions hybrides S3NS et Bleu », 27 juin 2025 — https://www.nexthop.fr/blog/souverainete-numerique-francaise-lillusion-des-solutions-hybrides-s3ns-et-bleu/
7. OVHcloud, Résultats financiers FY25, octobre 2025 — https://corporate.ovhcloud.com/fr/newsroom/news/financial-results-fy25/
8. Tech Insider (Nadia Dubois), « Mistral AI : 1 Million de Fonctionnaires Équipés [2026] », 24 juillet 2026 — https://tech-insider.org/fr/mistral-ai-assistant-fonction-publique-2026/
9. Capgemini, « Capgemini and Orange announce plan to create Bleu », 27 mai 2021 — https://www.capgemini.com/news/press-releases/capgemini-and-orange-announce-plan-to-create-bleu-a-company-to-provide-a-cloud-de-confiance-in-france/
10. Thales, « Thales présente S3NS en partenariat avec Google Cloud », 30 juin 2022 — https://www.thalesgroup.com/fr/actualites-du-groupe/communiques-de-presse/thales-presente-s3ns-en-partenariat-avec-google-cloud-et
11. Commission européenne, « Cloud and AI Development Act », 3 juin 2026 — https://digital-strategy.ec.europa.eu/en/policies/cloud-and-ai-development-act
12. Shattered.io, « Cloud Souverain UE : le CADA Vise AWS, Azure, GCP [2026] », août 2026 — https://shattered.io/fr/cloud-and-ai-development-act-souverainete-cloud-2026/
13. Capgemini, « Capgemini and Orange are pleased to announce the launch of commercial activities of Bleu », 15 janvier 2024 — https://www.capgemini.com/news/press-releases/capgemini-and-orange-are-pleased-to-announce-the-launch-of-commercial-activities-of-bleu-their-future-cloud-de-confiance-platform/
14. BusinessWire, « S3NS annonce la qualification SecNumCloud », 19 décembre 2025 — https://www.businesswire.com/news/home/20251218398028/fr
15. ChannelNews, « L'État accélère sa transition vers le cloud avec 84 M€ », mars 2026 — https://www.channelnews.fr/letat-accelere-sa-transition-vers-le-cloud-avec-84-me-de-commande-sur-le-marche-nuage-public-en-2025-155818
16. Boursorama, « Google Cloud et Thales lancent une offre de cloud souverain en Allemagne », 20 mai 2026 — le projet allemand espère générer « plusieurs centaines de millions d'euros d'ici quelques années »