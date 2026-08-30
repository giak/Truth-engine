# INVESTIGATION — Suite P0 : dix organisations, non-création, valeur, pouvoir et savoir

**Date :** 2026-08-25  
**Protocole :** RENARD CORE V3  
**Parent :** `INV-ORG10-001`  
**Objectif :** traiter les gaps P0 apparus après la reconstruction des dix chaînes organisationnelles.

## [DECOMPOSE]

| Atom | Sous-affirmation à tester | Niveau de source requis | Verdict |
|---|---|---:|---|
| P0-A | Shopify : le gate « AI avant headcount » produit-il des emplois non créés quantifiables ? | T1-T2 | **MÉCANISME VÉRIFIÉ / QUANTITÉ OPEN** |
| P0-B | Duolingo : la stratégie AI-first réduit-elle réellement le travail humain ? | T1-T2 | **RECOMPOSITION, PAS CONTRACTION SALARIÉE** |
| P0-C | BT : quelle part de la contraction d'effectifs est attribuable à l'IA ? | T1-T2 | **NON ISOLABLE À CE STADE** |
| P0-D | Salesforce : « 4 000 postes remplacés par l'IA » décrit-il une perte nette d'emploi ? | T1-T2 | **TROMPEUR AU NIVEAU GROUPE** |
| P0-E | Où va le gain de productivité IA ? | T1-T2 | **PLUSIEURS DESTINATIONS DOCUMENTÉES** |
| P0-F | Qui possède le savoir des experts incorporé dans les outils IA ? | T1-T2 | **CADRE JURIDIQUE PARTIEL, CONTRATS INTERNES OPEN** |
| P0-G | L'humain conserve-t-il réellement un droit d'override/recours ? | T1-T2 | **HÉTÉROGÈNE, PARFOIS ABSENT AU FRONTLINE** |

---

# 1. Shopify — le mécanisme de non-création est prouvé, pas son volume

Le 7 avril 2025, Tobi Lütke a rendu public un mémo interne imposant une règle explicite : avant de demander du headcount ou des ressources, les équipes doivent montrer pourquoi elles ne peuvent pas atteindre le résultat avec l'IA. L'usage de l'IA entre également dans les évaluations de performance et de pairs.

**Ce que cela établit :** un mécanisme organisationnel situé *avant* le recrutement.

**Ce que cela n'établit pas :** le nombre de postes effectivement refusés, différés ou supprimés par ce gate.

Shopify comptait environ **8 100 salariés fin 2024** et **7 600 fin 2025**, soit -500 salariés et -6.2% sur un an. Mais cette baisse ne peut pas être attribuée causalement à la règle IA avec les données publiques actuelles.

Surtout, les comptes 2025 compliquent la lecture « moins de salariés = moins de coût humain » : les coûts liés aux employés ont **augmenté de 105 M$ en R&D** et de **41 M$ en ventes/marketing**. En parallèle, Shopify annonce +30% de chiffre d'affaires et +26% de free cash-flow.

### Verdict
**SUPPORTED :** l'IA est devenue un filtre d'allocation du headcount.  
**OPEN :** combien d'emplois contrefactuels ce filtre a supprimés.  
**CONTRADICTED :** on ne peut pas déduire des 500 salariés en moins un gain salarial net causé par l'IA.

Sources :
- https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/
- https://www.sec.gov/Archives/edgar/data/1594805/000159480525000012/shop-20241231.htm
- https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm

---

# 2. Duolingo — le travail ne disparaît pas, il change de statut et de composition

En janvier 2024, Duolingo a confirmé avoir **off-boardé 10% de sa main-d'œuvre contractuelle** ; son porte-parole reconnaissait que l'IA contribuait à cette réduction dans certains cas, tout en refusant d'en faire la cause unique.

En avril 2025, le mémo AI-first de Luis von Ahn a durci la règle :
- arrêt progressif des contractants pour les tâches que l'IA peut traiter ;
- IA prise en compte dans le recrutement et la performance ;
- headcount accordé seulement si une équipe ne peut pas automatiser davantage.

Mais la trajectoire salariale est inverse à une contraction :
- environ **830 salariés fin 2024** ;
- **plus de 900 fin 2025**, soit au minimum +8.4% ;
- plus de 430 ingénieurs fin 2025.

Le chiffre d'affaires passe de 748,0 M$ à 1 037,6 M$, soit +38.7%. Les dépenses R&D augmentent de 71,0 M$, principalement à cause de **59,6 M$ de coûts nets de personnel supplémentaires**, entraînés par la croissance du headcount. Le 10-K indique aussi que les coûts de revenus incluent désormais explicitement les **coûts d'IA** et toujours, dans une moindre mesure, les **frais de contractants**.

### Ce que cela change
Le cas Duolingo montre une substitution **de statut et de tâches**, pas une disparition agrégée de la main-d'œuvre :
`contractants ↓ sur certaines tâches → salariés/ingénieurs ↑ + coûts IA ↑`.

### Verdict
**VERIFIED :** 10% des contractants ont été off-boardés début 2024, avec contribution partielle de l'IA.  
**VERIFIED :** la politique 2025 vise explicitement les contractants et les demandes de headcount.  
**REFUTED :** « AI-first = contraction de la main-d'œuvre salariée » sur 2024-2025.  
**OPEN :** nombre total de contractants concernés en 2025 et fonctions exactes.

Sources :
- https://www.cbsnews.com/pittsburgh/news/duolingo-lays-off-contractors-artificial-intelligence/
- https://www.linkedin.com/news/story/duolingo-to-swap-contractors-for-ai-6785921/
- https://www.linkedin.com/posts/luis-von-ahn-duolingo_one-of-the-most-important-things-leaders-activity-7331386411670982658-jpfX
- https://www.sec.gov/Archives/edgar/data/1562088/000156208825000090/duolingodecember312024an.htm
- https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm

---

# 3. BT — un signal très fort sur les juniors, mais l'IA n'est pas isolée comme cause

Les données sociales de BT sont maintenant verrouillées :

| Indicateur | 2024 | 2026 | Évolution |
|---|---:|---:|---:|
| Total salariés | 94 135 | 79 390 | -15.7% |
| Diplômés recrutés | 244 | 77 | -68.4% |
| Apprentis recrutés | 1 021 | 718 | -29.7% |
| Part des recrutements internes | 36,2% | 47,6% | +11.4 points |
| Turnover involontaire | 4,2% | 10,2% | +6,0 points |

En parallèle, BT documente l'utilisation de l'IA pour le développement logiciel, l'auto-résolution d'incidents et le support. La directrice générale Allison Kirkby a également déclaré en 2025 que l'IA pourrait conduire à des suppressions plus profondes que celles déjà planifiées.

Mais les réductions actuelles se superposent à :
- extinction du cuivre et des réseaux historiques ;
- déploiement fibre ;
- simplification organisationnelle ;
- cessions internationales ;
- consolidation immobilière ;
- attrition et plans de départ.

### Signal nouveau
Le fait le plus intéressant n'est pas seulement l'effectif total : **les voies d'entrée se contractent beaucoup plus vite**, tandis que la part des recrutements internes augmente.

Cela est compatible avec une entreprise qui :
1. réduit la taille totale ;
2. remplace davantage ses besoins par mobilité interne ;
3. ouvre moins de portes aux entrants.

L'IA peut contribuer à ce modèle, mais la preuve causale n'est pas encore disponible.

### Verdict
**VERIFIED :** chute très forte des recrutements diplômés et apprentis.  
**SUPPORTED :** l'IA est réellement intégrée à la transformation.  
**OPEN :** part causale précise de l'IA dans les baisses d'effectifs et d'entrées.

Sources :
- https://www.bt.com/about/annual-reports/2026summary/
- https://www.bt.com/about/annual-reports/2026summary/assets/files/Responsible-Business-Addendum-2026.pdf
- https://www.reuters.com/business/media-telecom/bt-ceo-eyes-deeper-job-cuts-ai-becomes-more-powerful-ft-reports-2025-06-15/

---

# 4. Salesforce — la phrase « l'IA a supprimé 4 000 emplois » est trop grossière

La fonction support est bien passée d'environ **9 000 à 5 000 personnes**. Salesforce explique que :
- Agentforce a réduit le volume de cas humains ;
- des **centaines de support engineers ont été redéployés** ;
- d'autres postes n'ont plus été backfillés.

Mais au niveau du groupe :
- 76 453 salariés au 31 janvier 2025 ;
- 83 334 au 31 janvier 2026 ;
- soit **+6,881 salariés**, environ **+9.0%**.

Donc :

`support ~-4 000 != groupe -4 000 emplois`

Une partie a été redéployée, une partie absorbée par attrition/non-backfill, tandis que Salesforce recrutait massivement dans d'autres fonctions et créait de nouveaux rôles liés à l'IA.

### Correction forensique
La formulation exacte devient :

> **Salesforce a réduit d'environ 4 000 postes dans sa fonction support tout en augmentant fortement son effectif global.**

Ce n'est pas un détail rhétorique : c'est la différence entre **substitution locale de tâches/postes** et **destruction nette d'emploi**.

### Verdict
**VERIFIED :** contraction d'environ 4 000 postes support.  
**VERIFIED :** centaines de redéploiements et non-backfill.  
**VERIFIED :** effectif global +6 881 sur le même intervalle fiscal.  
**REFUTED / MISLEADING :** « Salesforce a perdu 4 000 emplois à cause de l'IA » comme description du groupe.  
**OPEN :** ventilation individuelle exacte des ~4 000 postes support.

Sources :
- https://www.salesforce.com/news/stories/salesforce-reshaping-workforce-in-age-of-ai/
- https://www.salesforce.com/news/stories/agentic-enterprise-workforce-evolution/
- https://www.sec.gov/Archives/edgar/data/1108524/000110852425000006/crm-20250131.htm
- https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/crm-20260131.htm

---

# 5. Value ledger — le gain n'a pas de destination naturelle

## Klarna — extraction de coût + partage partiel avec les survivants
Klarna chiffre son assistant IA à l'équivalent du travail de **853 agents à temps plein** et à **58 M$ d'économies annuelles estimées**. L'entreprise attribue explicitement sa réduction de headcount à sa stratégie IA :
- 5 527 employés en 2022 ;
- 2 831 en 2025, soit environ -48.8% ;
- revenu par salarié : 344 k$ → 1,24 M$ ;
- compensation moyenne par salarié en hausse.

**Destination observable :** coût et effectifs ↓, productivité comptable ↑, rémunération des salariés restants ↑.

## JPMorganChase — capacité réinvestie
En transaction screening :
- plus du double du volume ;
- deux fois moins de vérifications manuelles.

La direction dit explicitement que la capacité libérée sera **réinvestie dans la croissance**, avec upskilling, reskilling et redéploiement. Le headcount global passe de 317 233 à 318 512, soit +0.4%.

**Destination observable :** croissance et capacité, pas objectif global de réduction de headcount.

## A&O Shearman — le savoir devient une rente logicielle
A&O Shearman :
- « distille » 20 à 30 ans de savoir juridique dans ses outils ;
- vend ContractMatrix en SaaS ;
- commercialise avec Harvey des agents sur abonnement ou à l'usage ;
- **partage les revenus logiciels**.

**Destination observable :** conversion de capital humain collectif en actif logiciel et revenu récurrent.

## Salesforce — redistribution interne
Le support se contracte, mais l'effectif groupe augmente de près de 9%. Salesforce documente le redéploiement de support engineers vers professional services, ventes, customer success et de nouveaux rôles IA.

**Destination observable :** déplacement intra-organisationnel + croissance, pas simple économie de masse salariale.

## Duolingo — substitution de contractants + hausse du salariat et du compute
Contractants partiellement réduits, mais salariés et dépenses R&D/personnel augmentent ; les coûts d'IA entrent explicitement dans le coût de revenus.

**Destination observable :** transfert de coûts du travail externalisé vers salariés qualifiés + infrastructure/modèles IA.

## Shopify — résultat indéterminé
Headcount -6%, mais coûts employés R&D et ventes/marketing en hausse. Les gains financiers 2025 sont forts, mais leur part causée par l'IA n'est pas isolée.

**Destination : OPEN.**

### Conclusion du ledger
> **L'euro économisé par l'IA ne possède pas de destination économique automatique.**

Il peut devenir :
- baisse de coût ;
- rémunération supérieure des survivants ;
- croissance ;
- nouveaux recrutements ;
- redéploiement ;
- dépenses de compute ;
- rente logicielle ;
- profit.

---

# 6. Le savoir capturé — le droit ne se résume pas à « l'entreprise possède le cerveau du salarié »

Le cas A&O Shearman rend ce problème concret : la firme dit intégrer « 20–30 ans de savoir juridique, marché et produit » de ses avocats dans sa pile technologique.

Le cadre britannique donne plusieurs réponses différentes selon la nature du résultat :

1. **Œuvres protégées par copyright créées dans le cours de l'emploi** : l'employeur est généralement le premier titulaire, sauf accord contraire.
2. **Inventions de salariés** : certaines inventions réalisées dans le cadre normal des fonctions ou d'obligations particulières appartiennent à l'employeur ; une compensation existe dans des cas étroits lorsqu'un brevet procure un bénéfice exceptionnel.
3. **Freelances / contractants** : ils conservent en principe le copyright, sauf transfert contractuel.
4. **Savoir-faire / expérience générale** : ce n'est pas automatiquement un « bien » possédé par l'employeur au même titre qu'un fichier ou un brevet.
5. **Informations confidentielles / secrets d'affaires** : peuvent être protégés contractuellement et par le droit de la confidentialité.

### Trou probatoire précis
Les sources publiques d'A&O documentent que les avocats participent au développement et que leur expertise devient partie de la tech stack. Elles **ne publient pas** :
- les clauses internes de consentement ;
- la rémunération particulière associée à cette extraction ;
- les droits individuels sur les playbooks / prompts / datasets dérivés ;
- le traitement des contributions de contractants.

Le problème n'est donc plus « à qui appartient le savoir ? » en général, mais :

> **quel régime juridique s'applique à chaque couche de savoir transformée en actif IA ?**

Sources :
- https://www.aoshearman.com/en/insights/alumni-yearbook/ai-leadership-practicing-what-we-preach
- https://www.aoshearman.com/en/news/ao-shearman-and-harvey-to-roll-out-agentic-ai-agents-targeting-complex-legal-workflows
- https://www.aoshearman.com/en/expertise/Artificial-intelligence
- https://www.gov.uk/guidance/ownership-of-copyright-works
- https://www.gov.uk/guidance/the-patent-act-1977/section-39-employees-inventions-right-to-employees-inventions
- https://www.gov.uk/guidance/the-patent-act-1977/section-40-employees-inventions-compensation-of-employees-for-certain-inventions

---

# 7. Override et recours — « human in the loop » peut vouloir dire des choses très différentes

## IBM
IBM écrit explicitement que **l'humain reste décideur final** et donne l'exemple des recommandations de hausses salariales : l'IA recommande, l'humain décide.

Mais le même cas montre une asymétrie organisationnelle forte :
- suppression du téléphone et de l'e-mail RH ;
- retrait du support HR Partner à 21 000 managers ;
- NPS passant de +19 à -35 avant de remonter à +74.

Le contrôle humain au niveau de la **décision finale** n'empêche donc pas un transfert de pouvoir au niveau de **l'accès au service** et du canal imposé.

## Walmart
Walmart publie une gouvernance Responsible AI et affirme privilégier choix, transparence et équité. Mais le dispositif de task management « comprend, priorise et recommande » le travail des associés. Aucun document public consulté ne décrit précisément :
- si l'associé peut ignorer la recommandation ;
- si le manager peut la surclasser ;
- si le refus est enregistré ;
- si ces signaux entrent ensuite dans l'évaluation de performance.

**Gap maintenu.**

## Klarna
Pour certaines décisions de crédit, Klarna précise que les décisions d'approbation sont automatisées et que les agents du service client **ne peuvent ni changer ni influencer** un refus.

Cela montre qu'un « humain disponible » ne signifie pas nécessairement « humain ayant autorité d'override ».

Attention : ceci concerne une décision client/crédit, pas une décision RH. Il est utilisé comme cas de gouvernance algorithmique dans la chaîne Klarna, pas comme preuve d'un pouvoir sur les salariés.

Sources :
- https://www.ibm.com/think/insights/chro-guide-ai-hr
- https://www.ibm.com/downloads/documents/gb-en/1227a45cbc308026
- https://corporate.walmart.com/news/2025/06/24/walmart-unveils-new-ai-powered-tools-to-empower-1-5-million-associates
- https://www.klarna.com/us/customer-service/how-can-i-get-approved-to-pay-with-klarna/

---

# [ADVERSARY]

| Axe | H_prediction | Rival_prediction | Observation | Favors |
|---|---|---|---|---|
| Shopify | gate IA → baisse de 500 salariés | baisse peut venir d'autres choix | gate vérifié, aucune donnée sur refus de headcount ; coûts employés R&D/S&M ↑ | **Rival / OPEN** |
| Duolingo | AI-first → moins de salariés | contractants ↓ mais salariés/compute ↑ | 10% contractants off-boardés en 2024, >900 salariés en 2025, personnel R&D ↑ | **Rival fort** |
| BT | effectif/juniors ↓ à cause de l'IA | transformation industrielle multicausale | chute réelle + IA déployée, mais nombreux confounders | **Rival actuel** |
| Salesforce | 4 000 emplois détruits | support se contracte mais effectif groupe peut augmenter | support ~9k→5k, groupe +6 881 salariés | **Rival fort** |
| Valeur | gain IA → profit / baisse payroll | plusieurs allocations possibles | Klarna, JPM, A&O, Salesforce, Duolingo divergent fortement | **Rival fort** |
| Savoir | expertise capturée = propriété automatique employeur | droits varient selon œuvre, brevet, contrat, secret, statut | cadre juridique fragmenté ; contrats internes non publics | **Rival** |
| Override | présence d'un humain = contrôle réel | humain peut être final décideur mais accès/override limités | IBM final decision humain mais canal imposé ; Klarna frontline sans override | **Rival** |

---

# [EVALUATE]

| Atom | Source_tier | Independent? | Survives_break? | Status | Confidence |
|---|---:|---|---|---|---:|
| P0-A Shopify gate | T1-T3 | Y | Y | SUPPORTED / QUANT OPEN | 0.90 |
| P0-B Duolingo recomposition | T1-T3 | Y | Y | VERIFIED/SUPPORTED | 0.94 |
| P0-C BT attribution | T1-T3 | Y | N causal | OPEN | 0.86 |
| P0-D Salesforce net jobs | T1-T2 | Y | Y | VERIFIED | 0.97 |
| P0-E Value ledger | T1-T2 | Y | Y | SUPPORTED fort | 0.93 |
| P0-F Knowledge property | T1-T2 | Y | Y partiel | SUPPORTED / CONTRACTS OPEN | 0.87 |
| P0-G Override | T1-T2 | Y | Y partiel | SUPPORTED / HETEROGENEOUS | 0.89 |

**EPISTEMIC_LEDGER** := verified: 3 | supported: 3 | disputed/open: 1 | refuted: 1

---

# [REPORT]

| Field | Content |
|---|---|
| what_changed_since_last | Salesforce : correction majeure entre réduction fonctionnelle et emploi net ; Duolingo : substitution contractants ≠ contraction salariale ; BT : pipeline junior devient signal fort ; value ledger documente plusieurs destinations du gain |
| surviving_H | non-création comme mécanisme réel ; recomposition statutaire ; capture du savoir ; distribution organisationnelle du gain ; management algorithmique |
| killed_H | « 4 000 postes Salesforce = 4 000 emplois nets détruits » ; « AI-first = baisse nécessaire des salariés » ; « gain IA = baisse automatique de payroll » |
| confidence_before -> confidence_after | modèle organisationnel/distributif 0,94 → 0,97 ; causalité uniforme IA→emploi reste faible |
| next_priority | **pipeline d'entrée / emplois non créés** : construire une cohorte comparable de 15-20 entreprises avec junior hiring, internal hires, attrition, AI integration timing |
| CALIBRATION | robuste sur mécanismes ; quantification macro toujours OPEN |

## Conclusion

La suite de l'enquête renforce une thèse plus précise :

> **L'IA ne remplace pas un “emploi”. Elle modifie d'abord une architecture d'allocation : qui entre, qui reste, qui monte en compétence, qui est redéployé, qui perd un contrat, qui commande, qui possède le savoir et qui capte le gain.**

Le licenciement n'est qu'une sortie possible parmi plusieurs.
