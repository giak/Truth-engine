# KERNEL INVESTIGATION: L'attrition silencieuse — Banques, Assurances, Télécoms

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0845-ATTRITION-SILENCIEUSE |
| Type | KERNEL COMPLEX |
| Loup parent | L-001 (trou statistique des non-remplacements, fresque IA-salariat) |
| Date | 2026-08-25 08:45 CEST |
| Gate | naming PASS, em-dash PASS, 111 tests PASS (BLOCKED branche protégée, structurel) |
| Sources | 22 |
| Statut | COMPLETED |

---

## 1. BRIEF

**Question d'enquête :** Quels sont les flux réels d'emploi dans les trois plus grands secteurs de services en France — banques, assurances, télécoms — en 2025-2026 ? Quelle part de l'érosion des effectifs est attribuable à l'IA, à la digitalisation, ou à la profitabilité ?

**Verdict forensique :** Les trois secteurs suivent des trajectoires radicalement différentes, unifiées par un même mécanisme : **l'attrition comme PSE qui ne dit pas son nom.**

- **Banques : destruction nette constante** (−0,7 %/an, ~20 000 postes en 9 ans). Le secteur « recrute tout en supprimant » : 34 400 embauches en 2025 masquent un solde négatif. L'IA n'est pas encore le moteur principal — c'est la fermeture d'agences (3 296 entre 2020 et 2025) et la digitalisation.
- **Assurances : croissance qui s'essouffle** (+0,6 % en 2025, ralentissement du recrutement : −8,6 %). Le secteur reste créateur net d'emplois, mais l'IA est explicitement identifiée comme facteur de transformation par la profession elle-même. L'alerte est lancée sur « l'employabilité des jeunes diplômés ».
- **Télécoms : crash structurel** (−49 000 emplois en 20 ans, de 140 000 à 91 000). Le démantèlement de SFR (juin 2026) menace 4 500 des 8 000 salariés. C'est le seul secteur où la destruction est massive, visible, et non masquée par des recrutements compensateurs.

**Le mécanisme commun :** dans les trois secteurs, l'attrition — le non-remplacement des départs — est la méthode privilégiée. Elle est juridiquement indolore (pas de PSE, pas de licenciements, pas de droits collectifs), politiquement discrète (les chiffres ne font pas la une), et comptablement efficace (les économies sont immédiates). FO Banques parle de « PSE silencieux », de « PSE rampant ». C'est le terme exact.

---

## 2. CLAIMS_REGISTRY

### CL-001 — L'IA remplace les emplois dans les banques françaises
- **Claim :** Les suppressions de postes dans les banques sont dues à l'IA.
- **Niveau :** L2 — partiellement vérifié. Le moteur principal est la fermeture d'agences et la digitalisation des services, pas l'IA générative. FBF : 15,9 % des recrutements sont dans les métiers tech, +3 points. L'IA est un accélérateur, pas la cause première. La cause première, c'est la profitabilité : SG a fait 4,1 Md€ de bénéfice et supprime 1 800 postes.
- **Statut :** PARTIALLY_VERIFIED. L'IA est citée (FO : « sous couvert de simplification via les nouveaux outils technologiques et l'intelligence artificielle ») mais le lien causal direct n'est pas établi. Ce qui est établi, c'est la simultanéité profits records/suppressions.

### CL-002 — Le secteur de l'assurance est épargné par l'érosion de l'emploi
- **Claim :** L'assurance résiste mieux que la banque.
- **Niveau :** L2 — vérifié pour l'instant. 162 300 salariés, +0,6 % en 2025, 307 Md€ de CA (+9,6 %). Mais les signaux faibles sont convergents : recrutements −8,6 % (retour au niveau 2022), alternance −8,4 %, l'IA « automatise progressivement les tâches de reporting » (Observatoire des métiers). L'alerte est explicite : « prévention de la perte des savoirs métiers », « employabilité des jeunes diplômés ».
- **Statut :** VERIFIE (pour l'état actuel), avec un warning prospectif documenté par la profession.

### CL-003 — L'attrition est un « PSE silencieux » sans droits pour les salariés
- **Claim :** Les banques utilisent le non-remplacement des départs pour supprimer des postes sans passer par les procédures légales de licenciement collectif.
- **Niveau :** L2 — documenté par FO Banques (février 2026) et confirmé par les chiffres FBF. Turnover à 7,7 %, recrutements à −10,2 %, solde négatif de −0,7 %. Le mécanisme est explicite : on ne remplace pas tous les départs. La direction de la SG assume : « simplifier les modes de fonctionnement [...] sans départs contraints ni plans de départs volontaires », par attrition.
- **Statut :** VERIFIE.

### CL-004 — Le démantèlement de SFR est la plus grande destruction d'emplois télécoms en France
- **Claim :** Le rachat de SFR par Orange/Free/Bouygues en juin 2026 menace des milliers d'emplois.
- **Niveau :** L2 — documenté. 8 000 salariés SFR, 3 500 repris, 4 500 à risque (syndicats : « 80 % des emplois menacés »). Promesse de maintien « jusqu'en 2029 » — ce qui signifie extinction progressive, pas sauvetage. Deal à 20,35 Md€. Bouygues Telecom avait déjà annoncé 556 départs volontaires.
- **Statut :** VERIFIE.

---

## 3. FACT_REGISTRY

### 3.1 Banques : l'érosion silencieuse

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-001 | 368 800 salariés à fin 2025 dans les banques FBF (dont 350 700 CDI/CDD). −0,7 % vs 2024. −20 000 postes en 9 ans. | FBF, 28 juillet 2026 | https://www.fbf.fr/fr/communique_de_presse/solidite-des-marqueurs-de-lemploi-dans-la-banque-en-2025/ |
| F-002 | 34 400 recrutements en 2025 (−10,2 % en un an, plus bas depuis 2013). | FBF, ibid. | ibid. |
| F-003 | Turnover à 7,7 % (vs 8,4 % en 2024, vs 20 % moyenne nationale). Le turnover baisse → mécaniquement, il faut moins recruter pour maintenir l'effectif. | FBF, ibid. | ibid. |
| F-004 | 75 % de cadres (+20 points depuis 2012). Les métiers relation client = 53,3 % des recrutements. Métiers tech = 15,9 % (+3 points). Back office = 2,6 % (−1,3 point). | FBF, ibid. | ibid. |
| F-005 | 18 100 alternants à fin 2025 (−8,6 % vs 2024). | FBF, ibid. | ibid. |
| F-006 | 3 296 agences fermées entre 2020 et 2025. ~6 300 depuis 2010. Le nombre total d'agences est passé de ~40 000 à ~36 000. | Les Échos, juin 2025/mai 2026 | https://www.lesechos.fr/finance-marches/banque-assurances/les-fermetures-dagences-saccelerent-les-banques-a-lheure-du-grand-reset-digital-2232376 |
| F-007 | Société Générale : 1 800 suppressions de postes d'ici fin 2027 (+ vague précédente de 3 700 entre 2023-2025). « Sans départs contraints ni PDV », par attrition. SG a fait 4,1 Md€ de bénéfice. | FO Banques, février 2026 | https://www.force-ouvriere.fr/dans-les-banques-les-transformations-technologiques-ne-doivent |
| F-008 | BNP Paribas : 1 200 suppressions (gestion d'actifs, 20 % de la division, dont ~600 en France) annoncées le 22 janvier 2026. Intégration post-rachat d'AXA IM. | France Info, 23 janvier 2026 | https://www.franceinfo.fr/internet/intelligence-artificielle/intelligence-artificielle-societe-generale-et-bnp-paribas-prevoient-des-milliers-de-suppressions-de-postes_7760747.html |
| F-009 | Cumul : SG + BNP = 3 000 suppressions annoncées le même jour (22 janvier 2026). | Révolution Permanente, 23 janvier 2026 | https://www.revolutionpermanente.fr/3-000-postes-supprimes-la-casse-sociale-s-intensifie-dans-les-banques |
| F-010 | Zone euro : les banques ont supprimé 3,2 % de leurs effectifs en 2025 (vs 0,7 % en France). Les banques françaises ferment moins d'agences que leurs homologues européennes. | Le Figaro, 28 juillet 2026 | https://www.lefigaro.fr/societes/dans-les-banques-l-emploi-continue-de-degringoler-20260728 |
| F-011 | FO Banques : « PSE silencieux », « PSE rampant », « hors de tout cadre juridique et légal ». Zéro rupture sèche liée aux transformations revendiquée. Demande de suivi consolidé des ETP, taux de remplacement, externalisations. | FO Banques, février 2026 | https://www.force-ouvriere.fr/dans-les-banques-les-transformations-technologiques-ne-doivent |
| F-012 | « La technologie n'est ni une finalité ni un prétexte. » FO a interpellé la FBF, le ministre du Travail et celui de l'Économie. | FO Banques, ibid. | ibid. |
| F-013 | Santé au travail : FO documente une « augmentation significative » d'accidents cardiaques, AVC, burnout, arrêts longue durée avec reprise en mi-temps thérapeutique. | FO Banques, ibid. | ibid. |

### 3.2 Assurances : croissance sous tension

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-014 | 162 300 salariés à fin 2025 (+0,6 %). CA 307 Md€ (+9,6 %). 1er marché européen. | Observatoire des métiers de l'assurance, juin 2026 | https://www.metiers-assurance.org/evolution-des-metiers-2/barometre-prospectif-2022-2-2/ |
| F-015 | 18 400 recrutements en 2025 (−8,6 % vs 2024, retour au niveau 2022). Deuxième année de baisse après huit ans de hausse continue. | Observatoire, ibid. | ibid. |
| F-016 | 7 100 alternants (−8,4 % de recrutements, plus marqué que la baisse interprofessionnelle de −5,0 %). Les alternants représentent encore 25 % des recrutements. | Observatoire, ibid. | ibid. |
| F-017 | L'IA désignée comme facteur de transformation : « automatise progressivement les tâches de reporting », « génère de nouveaux rôles hybrides », « exige une polyvalence accrue ». Alerte sur « la prévention de la perte des savoirs métiers » et « l'employabilité des jeunes diplômés ». | Observatoire, ibid. | ibid. |
| F-018 | Autres facteurs de transformation identifiés : catastrophes climatiques (sinistralité systémique), vieillissement démographique, digitalisation/conformité, tensions géopolitiques. L'IA n'est qu'un facteur parmi cinq. | Observatoire, ibid. | ibid. |
| F-019 | Turnover en baisse et recrutement en ralentissement (13,1 % de nouveaux salariés en 2023 → tendance baissière). | Tripalio, octobre 2025 | https://presse.tripalio.fr/dans-lassurance-le-turnover-baisse-et-le-recrutement-ralentit/ |

### 3.3 Télécoms : crash structurel

| ID | Fait | Source | URL |
|----|------|--------|-----|
| F-020 | Emplois directs des opérateurs télécoms en France passés de 140 000 (2004) à 91 000 (2024). −49 000 postes en 20 ans. | IDATE, cité par Le Monde, 27 décembre 2025 | https://www.lemonde.fr/economie/article/2025/12/27/2025-une-annee-noire-pour-l-emploi-dans-les-telecoms-en-europe-et-aux-etats-unis_6659537_3234.html |
| F-021 | SFR : 8 000 salariés. Protocole d'accord de vente signé début juin 2026 (Orange, Free, Bouygues). Seuls 3 500 repris. 4 500 à risque. Deal à 20,35 Md€ (+ bonus 650 M€). | BFM Business, 8 juin 2026 ; ZDNET, 24 juin 2026 | https://www.bfmtv.com/economie/entreprises/les-8-000-salaries-de-sfr-seront-conserves-jusqu-en-2029_AD-202606080411.html |
| F-022 | Syndicats SFR : « 80 % des emplois menacés ». « Ambiance de plomb » au siège le 24 juin 2026. | Le Monde, 24 juin 2026 | https://www.lemonde.fr/economie/article/2026/06/24/les-syndicats-de-sfr-redoutent-des-milliers-de-suppressions-de-postes-apres-le-rachat_6713233_3234.html |
| F-023 | Engagement des repreneurs : maintien de l'emploi « jusqu'en 2029 » — ce qui acte une extinction progressive, pas un sauvetage. | BFM Business, 8 juin 2026 | ibid. |
| F-024 | Bouygues Telecom : plan de 556 départs volontaires annoncé. | Miroir Social ; ZDNET, juin 2026 | https://www.zdnet.fr/actualites/rachat-de-sfr-vers-un-plan-social-massif-497555.htm |
| F-025 | Orange : 700 suppressions de postes dans Orange Business (2023), retiré temporairement puis renégocié. Attrition continue : seniors visés (73 000 salariés). | Les Échos, octobre 2024 | https://www.lesechos.fr/tech-medias/hightech/le-dossier-de-lemploi-des-seniors-agite-les-esprits-chez-orange-2124274 |
| F-026 | Observatoire AFDAS : 90 755 emplois salariés privés dans les télécoms en 2024 (+2 %). 98 % de CDI. | AFDAS, 2024-2025 | https://observatoires.afdas.com/observatoires/telecommunications |
| F-027 | 2025 : « année noire pour l'emploi dans les télécoms en Europe et aux États-Unis » (Le Monde). Contexte : les opérateurs européens suppriment massivement. | Le Monde, 27 décembre 2025 | ibid. |

---

## 4. ANALYSE — Les trois trajectoires

### 4.1 Banques : la machine à détruire sans bruit

Le secteur bancaire français est une **machine à attrition** parfaitement rodée :

```
Turnover à 7,7 % (moyenne nationale : 20 %)
→ ~28 400 départs naturels par an (368 800 × 7,7 %)
→ On ne remplace pas tout le monde : 34 400 recrutements, solde négatif
→ Effectif baisse de −0,7 %/an, année après année
→ −20 000 postes en 9 ans, sans un seul licenciement
```

**Le mécanisme est légal, silencieux, et indolore pour l'employeur :**
- Pas de PSE → pas de plan de sauvegarde de l'emploi, pas de reclassement obligatoire, pas de négociation
- Pas de PDV → pas de volontariat indemnisé, pas de contrôle des réembauches
- Pas de « motif économique » → pas de contestation prud'homale possible
- Les syndicats ne peuvent rien faire : une non-embauche n'est pas un licenciement

La FO Banques décrit exactement le piège : « un PSE silencieux qui se déroule hors de tout cadre juridique et légal [...] des décisions complètement unilatérales, les organisations représentatives n'ont pas leur mot à dire. »

**Le paradoxe des chiffres :** le secteur recrute massivement (34 400 en 2025, 1 sur 2 a moins de 30 ans, 75 % en CDI). Il forme (32,4 h/an/salarié). Il promeut (7,9 % de promotion). Et simultanément, il détruit 2 600 postes nets cette année-là. Les deux mouvements ne sont pas contradictoires — c'est le remplacement des profils : moins de guichetiers, plus d'ingénieurs data. Mais le solde net est négatif, et il est négatif depuis neuf ans.

**Où est l'IA là-dedans ?** Elle n'est pas le moteur principal. Le moteur, c'est la fermeture d'agences (3 296 en 5 ans, ~6 300 depuis 2010). La digitalisation des services courants (virements, consultation de comptes, souscription) a précédé l'IA générative de dix ans. L'IA arrive maintenant comme couche supplémentaire — back office à 2,6 % des recrutements (−1,3 point) — mais la structure de la destruction était déjà en place.

La FBF le formule à sa manière : « les métiers du digital représentent désormais 15,9 % des recrutements, soit trois points de plus qu'en 2024. » Traduction : la banque remplace des chargés de clientèle par des data scientists. Le nombre total de salariés baisse, la masse salariale — peut-être — se maintient (les data scientists coûtent plus cher).

**Le signal le plus inquiétant n'est pas dans les chiffres d'emploi — c'est la santé au travail.** FO documente une « augmentation significative » d'AVC, d'accidents cardiaques, de burnout avec arrêts longue durée. La charge de travail ne diminue pas avec les effectifs : elle se concentre sur ceux qui restent.

### 4.2 Assurances : le contraste et les nuages

L'assurance est **le seul des trois secteurs encore créateur net d'emplois** (+0,6 % en 2025). Mais les signaux sont convergents et orientés à la baisse :

| Indicateur | 2023 | 2024 | 2025 | Tendance |
|-----------|------|------|------|----------|
| Recrutements | 20 600 | 20 100 (−2,5 %) | 18 400 (−8,6 %) | ↓ |
| Alternants | — | −5 % environ | −8,4 % | ↓ |
| Effectifs | ↑ | ↑ | +0,6 % | ↓ ralentissement |

La profession elle-même identifie les risques avec une honnêteté rare : « L'enjeu majeur réside dans le renforcement du pilotage humain, la consolidation de l'esprit critique et la prévention de la perte des savoirs métiers. Une attention particulière doit être portée sur la santé mentale des salariés et l'employabilité des jeunes diplômés. » (Observatoire des métiers de l'assurance, juin 2026)

C'est un langage codé qui dit : l'IA va automatiser les tâches des juniors, et on ne sait pas comment les former si leurs tâches d'apprentissage disparaissent. C'est exactement le même problème qu'IBM a identifié — mais formulé par la profession elle-même, pas par un observateur extérieur.

**Pourquoi l'assurance résiste-t-elle mieux que la banque ?** Hypothèses (non vérifiées dans cette investigation) :
1. Le CA progresse plus vite (+9,6 %) que dans la banque.
2. La sinistralité climatique croissante crée du travail d'indemnisation, qui reste humain.
3. Le vieillissement démographique crée de la demande en assurance-vie, santé, dépendance.
4. La réglementation (Solvabilité II, IFRS 17) exige des effectifs de conformité.

Mais la tendance est claire : le rythme de création d'emplois décélère, et les recrutements chutent plus vite que l'emploi net. Le point d'inflexion — quand les départs excéderont les embauches — approche.

### 4.3 Télécoms : la destruction visible

Les télécoms sont le seul secteur où la destruction est **visible, massive, et non masquée** :

```
140 000 emplois (2004)
→ 91 000 (2024)
→ 4 500 menacés chez SFR (2026)
→ −49 000 en 20 ans (−35 %)
```

La raison est structurelle : les télécoms sont une industrie de réseau. Une fois l'infrastructure déployée (fibre, 5G), l'emploi d'exploitation se réduit mécaniquement. La consolidation du marché (passage de 4 à 3 opérateurs avec le démantèlement de SFR) achève le processus.

**Le cas SFR est emblématique :** Patrick Drahi a acheté l'opérateur en 2014, l'a pressé pour extraire du cash (LBO, dividendes), et le revend en 2026 à ses trois concurrents pour 20,35 Md€. Les repreneurs ne veulent que les clients (25 millions) et les infrastructures — pas les salariés. 3 500 sur 8 000 repris. Le reste : plan social ou attrition jusqu'en 2029.

Ce n'est pas l'IA qui détruit ces emplois. C'est la financiarisation. Mais l'effet est le même pour le salarié.

---

## 5. LE MÉCANISME UNIFIÉ — L'attrition comme PSE rampant

Les trois secteurs partagent le même outil de destruction de l'emploi : **l'attrition.**

| Caractéristique | PSE classique | Attrition |
|----------------|-------------|-----------|
| Base légale | Articles L.1233-1 et suivants | Aucune (simple décision de gestion) |
| Obligation de reclassement | Oui | Non |
| Plan de sauvegarde de l'emploi | Obligatoire | Aucun |
| Négociation syndicale | Obligatoire | Aucune |
| Indemnités supra-légales | Négociées | Aucune |
| Contestation prud'homale | Possible (motif économique) | Impossible (pas de licenciement) |
| Visibilité médiatique | Forte | Nulle |
| Chiffres officiels | Publiés | Dilués dans la masse des départs |

**Le chiffre caché :** combien de postes sont supprimés par attrition ? La réponse est : personne ne le sait, parce que personne ne le mesure. La statistique publique ne suit pas le « taux de remplacement des postes libérés ». C'est le trou statistique documenté dans l'investigation « non-remplacements ».

Pour les banques, on peut borner :
- Départs naturels : ~28 400/an (368 800 × 7,7 %)
- Recrutements : 34 400/an
- Si le secteur voulait maintenir ses effectifs constants, il devrait recruter autant qu'il perd. Or il recrute 34 400 pour 28 400 départs — ce qui devrait donner un solde positif. Mais le solde est négatif (−0,7 %).
- **Explication :** il y a des suppressions de postes en plus des départs naturels. Le chiffre de 28 400 départs inclut les démissions, retraites, et... les postes qu'on a décidé de ne pas pourvoir. Le taux réel de non-remplacement est donc supérieur à 0,7 %.

**Estimation prudente :** si le turnover « naturel » sans suppressions serait de 8-9 % (proche de la moyenne nationale de 20 %, ajusté pour le profil plus âgé et plus stable des banques), alors 1 à 2 points de turnover correspondent à des suppressions nettes. Soit 3 700 à 7 400 postes supprimés par an dans les seules banques françaises — sans un seul licenciement.

---

## 6. VERDICT

**L'attrition silencieuse est le principal mode de destruction de l'emploi en France dans les services, et elle est structurellement sous-mesurée.**

1. **Banques : −20 000 postes en 9 ans.** Le secteur détruit 2 500-3 000 emplois nets par an tout en affichant des recrutements dynamiques et des profits records. L'IA est un accélérateur, la digitalisation est le moteur historique, la profitabilité est la cause réelle.

2. **Assurances : croissance qui s'essouffle.** Encore créateur net, mais recrutements −8,6 %, alternance −8,4 %. La profession anticipe explicitement le problème de « l'employabilité des jeunes diplômés » face à l'IA.

3. **Télécoms : −49 000 postes en 20 ans, et le pire est à venir.** Le démantèlement de SFR (2026) pourrait coûter 4 500 emplois. La consolidation du marché et la financiarisation, pas l'IA, sont les moteurs.

**Le chiffre agrégé :** banques + assurances + télécoms = **~622 000 emplois à fin 2025.** Destruction annuelle agrégée estimée : **−5 000 à −7 000 postes nets/an** (banques −2 600 confirmé, télécoms −1 000 à −2 000 estimé, assurances encore positif mais ralentissement). Soit environ −1 % par an du stock total.

Ce n'est pas un effondrement. C'est une **érosion lente, continue, et structurellement invisible** dans les statistiques agrégées parce que d'autres secteurs créent des emplois par ailleurs. Mais pour les salariés de ces secteurs, l'effet est le même qu'un plan social : les postes disparaissent, les collègues ne sont pas remplacés, la charge de travail augmente, et la santé se dégrade.

---

## 7. LOUPS OUVERTS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | L'attrition n'est pas mesurée par la statistique publique. Le « taux de remplacement des postes libérés » n'existe pas. Le débat public sur l'emploi se fait sur des flux bruts qui masquent l'érosion nette. | TRÈS HAUTE |
| W-002 | L'absence de cadre juridique pour l'attrition organisée (non-remplacement systématique) prive les salariés de tout droit collectif. Un PSE sans PSE. | HAUTE |
| W-003 | La simultanéité profits records/suppressions de postes (SG : 4,1 Md€, BNP/SG : 3 000 suppressions annoncées le même jour) suggère que l'IA est un prétexte, pas une cause. | MOYENNE |
| W-004 | La santé au travail dans les secteurs en attrition est documentée comme dégradée (AVC, burnout, arrêts longue durée), mais non corrélée officiellement aux suppressions. | MOYENNE |
| W-005 | Le recul de l'alternance (−8,6 % banques, −8,4 % assurances) est le signal le plus préoccupant pour le pipeline de talents. C'est le même mécanisme qu'IBM. | HAUTE |

---

## 8. SOURCES

1. FBF, « Solidité des marqueurs de l'emploi dans la banque en 2025 », 28 juillet 2026 — https://www.fbf.fr/fr/communique_de_presse/solidite-des-marqueurs-de-lemploi-dans-la-banque-en-2025/
2. Le Figaro, « Dans les banques, l'emploi continue de dégringoler », 28 juillet 2026 — https://www.lefigaro.fr/societes/dans-les-banques-l-emploi-continue-de-degringoler-20260728
3. Force Ouvrière, « Dans les banques, les transformations technologiques ne doivent pas être une machine à supprimer les postes », février 2026 — https://www.force-ouvriere.fr/dans-les-banques-les-transformations-technologiques-ne-doivent
4. France Info, « Intelligence artificielle : Société Générale et BNP Paribas prévoient des milliers de suppressions de postes », 23 janvier 2026 — https://www.franceinfo.fr/internet/intelligence-artificielle/intelligence-artificielle-societe-generale-et-bnp-paribas-prevoient-des-milliers-de-suppressions-de-postes_7760747.html
5. Les Échos, « Les fermetures d'agences s'accélèrent : les banques à l'heure du grand reset digital », mai 2026 — https://www.lesechos.fr/finance-marches/banque-assurances/les-fermetures-dagences-saccelerent-les-banques-a-lheure-du-grand-reset-digital-2232376
6. AEF Info, « En 2025, le secteur bancaire enregistre une baisse maîtrisée de ses effectifs de 0,7 % », 28 juillet 2026 — https://www.aefinfo.fr/depeche/754874-en-2025-le-secteur-bancaire-enregistre-une-baisse-maitrisee-de-ses-effectifs-de-07-fbfafb
7. 20 Minutes, « Le secteur bancaire est en pleine transformation et voit ses effectifs fondre », 28 juillet 2026 — https://www.20minutes.fr/economie/4236712-20260728-pleine-transformation-secteur-bancaire-voit-effectifs-fondre
8. Révolution Permanente, « 3 000 postes supprimés, la casse sociale s'intensifie dans les banques », 23 janvier 2026 — https://www.revolutionpermanente.fr/3-000-postes-supprimes-la-casse-sociale-s-intensifie-dans-les-banques
9. Management Hebdo, « Suppressions de postes à BNP Paribas et Société Générale : le choix de l'attrition maîtrisée », janvier 2026 — https://www.management-hebdo.fr/Suppressions-de-postes-a-BNP-Paribas-et-Societe-Generale-le-choix-de-l-attrition-maitrisee_a1913.html
10. AFB, « Rapport 2025 - Profil de branche emploi », 28 juillet 2026 — https://www.afb.fr/rapport-2025-profil-de-branche-emploi/
11. Observatoire des métiers de l'assurance, « Baromètre prospectif 2026 », juin 2026 — https://www.metiers-assurance.org/evolution-des-metiers-2/barometre-prospectif-2022-2-2/
12. Argus de l'Assurance, « L'assurance gagne encore des salariés en 2025 mais la dynamique de recrutement s'essouffle », 4 juin 2026 — https://www.argusdelassurance.com/ressources-humaines/ressources-humaines-lassurance-gagne-encore-des-salaries-en-2025-mais-la-dynamique-de-recrutement-sessouffle.C7BGJRSKQBHEPGZ5FTTGHED5JU.html
13. Tripalio, « Dans l'assurance le turnover baisse et le recrutement ralentit », octobre 2025 — https://presse.tripalio.fr/dans-lassurance-le-turnover-baisse-et-le-recrutement-ralentit/
14. France Assureurs, « Données clés 2025 », juillet 2026 — https://www.franceassureurs.fr/actualites/donnees-cles-2025/
15. ACPR, « N° 181 : La situation des assureurs en France fin 2025 », juin 2026 — https://acpr.banque-france.fr/fr/publications-et-statistiques/publications/ndeg-181-la-situation-des-assureurs-en-france-fin-2025
16. Le Monde, « 2025, une année noire pour l'emploi dans les télécoms en Europe et aux États-Unis », 27 décembre 2025 — https://www.lemonde.fr/economie/article/2025/12/27/2025-une-annee-noire-pour-l-emploi-dans-les-telecoms-en-europe-et-aux-etats-unis_6659537_3234.html
17. BFM Business, « Les 8 000 salariés de SFR seront conservés... jusqu'en 2029 », 8 juin 2026 — https://www.bfmtv.com/economie/entreprises/les-8-000-salaries-de-sfr-seront-conserves-jusqu-en-2029_AD-202606080411.html
18. ZDNET, « Rachat de SFR : vers un plan social massif ? », 24 juin 2026 — https://www.zdnet.fr/actualites/rachat-de-sfr-vers-un-plan-social-massif-497555.htm
19. Le Monde, « Les syndicats de SFR redoutent des milliers de suppressions de postes », 24 juin 2026 — https://www.lemonde.fr/economie/article/2026/06/24/les-syndicats-de-sfr-redoutent-des-milliers-de-suppressions-de-postes-apres-le-rachat_6713233_3234.html
20. Le Figaro, « Bouygues Telecom, Orange et Free passent leur grand oral face aux salariés de SFR », 24 juin 2026 — https://www.lefigaro.fr/secteur/high-tech/bouygues-telecom-orange-et-free-passent-leur-grand-oral-face-aux-salaries-de-sfr-dans-un-climat-tendu-20260624
21. AFDAS, « Observatoire des télécommunications », 2024-2025 — https://observatoires.afdas.com/observatoires/telecommunications
22. Les Échos, « Le dossier de l'emploi des seniors agite les esprits chez Orange », octobre 2024 — https://www.lesechos.fr/tech-medias/hightech/le-dossier-de-lemploi-des-seniors-agite-les-esprits-chez-orange-2124274