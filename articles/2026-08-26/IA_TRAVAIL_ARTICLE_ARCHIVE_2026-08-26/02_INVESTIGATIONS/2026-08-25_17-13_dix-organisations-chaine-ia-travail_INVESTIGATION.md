# INVESTIGATION — Dix organisations : chaîne causale IA → travail

**Date :** 2026-08-25  
**Protocole :** RENARD CORE V3  
**Objet :** reconstruire, pour dix organisations contrastées, la chaîne  
`technologie réellement déployée → tâche modifiée → poste redessiné → recrutement → compétence → savoir capturé → données utilisées → décision algorithmique → rapports de pouvoir → destination économique du gain`.

## Verdict synthétique

Le corpus ne soutient pas un mécanisme unique `IA → suppression d'emploi`. Il documente au moins cinq régimes organisationnels :

1. **Substitution/coût** : Klarna ; Salesforce partiellement.
2. **Automatisation hybride** : IBM, BT, Walmart.
3. **Augmentation + réinvestissement** : JPMorganChase, Morgan Stanley.
4. **Capitalisation du savoir** : A&O Shearman.
5. **Gouvernance AI-first / filtre de ressources** : Shopify, Duolingo.

La variable discriminante n'est pas seulement la capacité de la technologie, mais la **règle d'allocation du gain** : baisse des coûts, non-création, redéploiement, croissance, intensification, rémunération, ou transformation du savoir en actif logiciel.

---

## Matrice des dix organisations

| Organisation | Technologie réellement déployée | Tâche modifiée | Poste redessiné | Recrutement / effectif | Compétence | Savoir capturé | Données utilisées | Décision algorithmique | Rapport de pouvoir | Destination économique du gain | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Klarna | Assistant OpenAI, copilots, ML underwriting | 80% chats CS 2025, code, personnalisation, underwriting | support moins volumineux, davantage d'ingénierie/data | 4 352 FTE (2023) → 2 831 (2025), réduction explicitement reliée à l'IA | ingénierie/data, cas complexes | historique transactions + logs + SKU | 2,6 Md points SKU/an + apprentissages >6,4 Md transactions | underwriting ML, personnalisation, routage support | décision managériale assumée de réduire le headcount ; syndicats/works councils présents | opex ↓, revenue/employee ↑, compensation/employee ↑ | **FORT** |
| IBM | AskHR + watsonx Orchestrate | ~80-90 workflows RH | support RH à deux niveaux, self-service managers | pas de volume public de suppressions ; IBM documente de nouveaux jobs RH de plateforme | RH stratégique, agents, gouvernance | ~7 000 pages de politiques + feedback + workflows | données RH et systèmes Workday/SAP/Concur | transferts, org updates, compensation workflows, promotions initiées | IBM a fermé téléphone/email RH et retiré support HRBP à 21k managers en 2018 ; humain réintroduit pour cas complexes après chute NPS | coûts RH -40%, temps réalloué, jobs plateforme créés | **FORT** |
| Shopify | outils IA généralisés, code editor, Sidekick, outils internes | code, prototypage, processus | AI usage = baseline de travail | règle : démontrer que l'IA ne suffit pas avant headcount ; ~8 100 employés 2024 → ~7 600 en 2025, causalité non établie | maîtrise IA devient attente ; talent IA critique | contexte/code internes, détail public insuffisant | données internes/merchant, provenance employee-use non détaillée | pas de décision HR automatisée prouvée ; **gate managérial** avant ressources | management transforme l'IA en condition d'accès aux ressources | croissance/FCF 2025 forts, mais attribution du gain à l'IA **OPEN** | **MOYEN** |
| Duolingo | genAI contenu, Video Call, Roleplay, systèmes ML | génération de cours/contenu | moins de certains travaux contractuels, plus d'AI-native production | politique contractor/headcount AI-first ; salariés ~830 (2024) → >900 (2025) | AI fluency + supervision de contenu | corpus pédagogique + expertise + gigantesque dataset utilisateur | ~2 Md exercices/jour, données d'apprentissage | personnalisation produit ; pas de décision RH algorithmique publique | politique CEO affecte contractants/headcount ; backlash publique reconnue dans 10-K | vitesse de production et expansion du catalogue ; coûts IA augmentent aussi | **FORT comme contre-exemple** |
| BT | >50 AI in-house, ~90 apps AI, AI Ops, Aimee, dev tools | incidents auto-heal, support, code | guides → cas complexes ; digital ops simplifiées | 94 135 employés FY24 → 79 390 FY26 ; grads 244→77 ; apprentis 1 021→718 ; mais ~13k embauches FY26 et causes multiples | 2 500 formés AI/cloud/digital ; 30k heures digital learning | données réseau, interactions clients, code/process | incidents réseau, conversations, données opérationnelles | AI Ops auto-résout incidents ; Aimee triage support | 93,5% UK couverts par collective bargaining ; board workforce engagement et deep dives AI | économies et effort humain ↓, mais part AI du programme de coûts non isolable | **FORT, causalité emploi FAIBLE** |
| JPMorganChase | LLM Suite, Employee Assistant, code assistants, AI screening | screening, code, support, forecasting | opérateurs traitent plus de volume avec moins de checks manuels | headcount 317 233 (2024) → 318 512 (2025) ; doctrine explicite de redeploy/upskill | AI upskilling ; >90% engineers code assistants | data estate + données client/entreprise | environnement contrôlé ; transaction data | screening, pricing/risk/inventory tools ; supervision humaine | politique déclarée : technologie au service de croissance, pas objectif de headcount ↓ | capacité libérée **réinvestie en croissance**, formation, redéploiement | **TRÈS FORT contre-exemple** |
| Walmart | Element ML, task management, conversational AI, MyAssistant, AR/RFID | planning shifts 90→30 min, task prioritization, process guidance | managers moins de planning ; associates suivent des priorités IA | aucune baisse d'effectif attribuée publiquement à l'IA | usage outils + upskilling/career pathways | guides de processus, connaissances retail | schedules, task/store/inventory data ; gouvernance annoncée | priorise/recommande tâches ; workflow algorithmique | déplacement partiel du pouvoir de séquencement vers l'outil ; contrôle humain exact peu documenté | temps manager gagné ; investissement simultané salaires/formation, allocation monétaire non prouvée | **FORT** |
| Salesforce | Agentforce + Data Cloud | auto-résolution support, routage/escalade | fonction support réduite / agents + humains | CEO : ~9k→~5k support ; centaines redéployés ; détail complet des 4k non réconcilié publiquement | supervision agents, sales/pro services/customer success | CRM/Data Cloud + conversations support | dizaines de trillions de records Data Cloud | agent résout/escalade cases | management choisit le ratio agent/humain ; transparence du redéploiement incomplète | case volume ↓, économies revendiquées ; marges/cashflow/buybacks élevés mais causalité AI→distribution **non démontrée** | **FORT tech, MOYEN emploi** |
| A&O Shearman | Harvey, ContractMatrix, Analyze, Vantage, agents | drafting, review, negotiation, antitrust/cyber/funds/loan review | juriste centré stratégie/jugement, human-in-loop | pas de réduction documentée ; firme dit que leadership AI attire des jeunes juristes | expertise juridique + conception playbooks + contrôle IA | « 20–30 ans » de savoir legal/market/product distillés dans outils | matter docs, curated data, client playbooks | agents produisent work products avec oversight ; avocat valide | la firme capture de l'expertise individuelle/collective dans son tech stack ; AI Steering Committee | **SaaS + subscription/usage fees**, revenus logiciels partagés avec Harvey | **TRÈS FORT savoir→valeur** |
| Morgan Stanley | Assistant, Debrief, AskResearchGPT | recherche, notes, résumé, email, CRM | conseiller recentré relation/jugement ; moins de travail de prise de notes | aucun impact headcount documenté | jugement, relation, critique, utilisation IA | Morgan Stanley intellectual capital + >70k research reports/an | contenu propriétaire ; meeting data avec consentement ; feedback queries | notes/action items générés ; adviser édite/envoie à discrétion | consentement client + validation humaine ; outil sous contrôle firme | temps/capacité client ↑ ; P&L/headcount non publié | **TRÈS FORT augmentation** |

---

## Cas 1 — Klarna : substitution explicitement assumée

### Chaîne
`OpenAI assistant + ML + copilots → automatisation CS/code → réduction support/vendors → headcount ↓ → compétences engineering/data ↑ → transaction/SKU data → underwriting/personnalisation/support → management assume workforce shrinkage → Opex ↓ + revenue/employee ↑ + compensation/employee ↑`

**Pièces cardinales**
- Klarna Group 2025 Annual Report / SEC : 80% des chats support traités par l'assistant ; 2,6 Md de points SKU collectés en 2025 ; apprentissages sur >6,4 Md transactions ; 4 352 FTE fin 2023, 3 422 fin 2024, 2 831 fin 2025 ; le dépôt dit explicitement que la baisse résulte d'une décision stratégique de réduire le headcount en s'appuyant sur l'IA.
- Depuis Q4 2022 : revenus +104%, operating expenses -8%, revenue/employee 3,6x, compensation/employee en hausse.

**Contre-factuel :** retirer la pièce SEC reliant explicitement headcount et IA ferait chuter fortement le verdict causal. C'est le cas le plus fragile à une seule pièce, mais cette pièce est primaire et décisive.

Sources :
- https://www.sec.gov/Archives/edgar/data/2003292/000200329226000007/klar-20251231.htm
- https://www.sec.gov/Archives/edgar/data/2003292/000162828026038366/annualreport2025.htm

---

## Cas 2 — IBM : automatiser n'est pas seulement supprimer

### Chaîne
`AskHR/watsonx → ~80-90 workflows RH → self-service + support humain complexe → nouveaux rôles plateforme → compétences RH stratégiques → 7 000 pages politiques + feedback + données RH → transactions RH initiées/exécutées → accès au support humain reconfiguré → coûts RH -40% + temps réalloué`

IBM documente un épisode rare de **pouvoir organisationnel** : en 2018, téléphone et email RH ont été supprimés et l'accès HR Partner retiré à 21 000 managers de première ligne. L'expérience a d'abord fait tomber le NPS à -35, puis le support humain a été retravaillé, jusqu'à +74. Cela réfute l'idée « digitalisation = amélioration univoque ».

Sources :
- https://www.ibm.com/case-studies/ibm-askhr
- https://www.ibm.com/think/insights/embracing-future-of-hr-ai-first-enterprise
- https://canada.newsroom.ibm.com/articles-ai-driven-data-analytics-and-automation-ibm-as-client-zero

---

## Cas 3 — Shopify : le poste qui n'est peut-être jamais demandé

### Chaîne
`AI partout → code/prototypage/process → AI baseline → headcount request gate → compétence AI obligatoire → savoir interne partiellement absorbé → décision humaine de ressources conditionnée par capacité AI → pouvoir managérial → gain économique non séparé`

Le signal le plus important n'est pas les 500 employés de moins entre fin 2024 et fin 2025. **Aucune preuve primaire ne permet de dire que l'IA explique ces 500.** Le mécanisme documenté est plus subtil : avant de demander du headcount, les équipes doivent démontrer pourquoi l'IA ne suffit pas.

Sources :
- https://www.sec.gov/Archives/edgar/data/1594805/000159480525000012/shop-20241231.htm
- https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm

---

## Cas 4 — Duolingo : AI-first sans contraction des salariés

### Chaîne
`genAI content → production cours accélérée → réduction ciblée de certaines tâches contractuelles → filtre headcount AI-first → AI fluency → dataset d'apprentissage → personnalisation/production → pouvoir CEO sur critères de ressources → croissance de contenu`

Le contre-exemple est important : **les salariés passent d'environ 830 à plus de 900 entre fin 2024 et fin 2025**. Le virage AI-first ne se traduit donc pas par une contraction du headcount salarié sur cette période. L'impact sur les contractants reste insuffisamment quantifié publiquement.

Sources :
- https://www.sec.gov/Archives/edgar/data/1562088/000156208825000042/duol-20241231.htm
- https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm

---

## Cas 5 — BT : l'effet IA est noyé dans une transformation industrielle

### Chaîne
`AI Ops + Aimee + dev tools → auto-heal/support/code → rôles support plus complexes → workforce ↓ mais causes multiples → reskilling → données réseau/client → décisions opérationnelles automatiques → forte représentation collective → coûts/effort humain ↓`

BT montre pourquoi les headlines « X emplois supprimés par l'IA » sont dangereuses : la société combine fibre, fermeture de réseaux historiques, simplification, cessions, attrition, transformation immobilière et IA. La baisse des juniors est réelle, la causalité IA ne l'est pas.

Sources :
- https://www.bt.com/about/annual-reports/2026summary/assets/files/BT-Annual-Report-2026.pdf
- https://www.bt.com/about/annual-reports/2026summary/assets/files/Responsible-Business-Addendum-2026.pdf
- https://www.bt.com/bt-plc/assets/documents/investors/financial-reporting-and-news/annual-reports/2025/2025-bt-group-plc-strategic-report.pdf

---

## Cas 6 — JPMorganChase : productivité sans objectif de réduction du headcount

### Chaîne
`LLM Suite + screening + code AI → contrôles manuels ↓ → opérateurs/engineers augmentés → headcount global stable/↑ → upskill/redeploy → data estate → décisions screening/risk assistées → doctrine growth-first → gains réinvestis`

Le groupe documente plus du double de volume de transaction screening avec moitié moins de checks manuels. Pourtant la lettre aux actionnaires dit explicitement que l'objectif n'est pas « fewer headcount » : capacité, compétences et talents doivent être redéployés pour la croissance.

Source :
- https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/annualreport-2025.pdf
- https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letter-jennifer-piepszak

---

## Cas 7 — Walmart : de l'automatisation au management algorithmique

### Chaîne
`Element ML + task management → priorisation tâches/planning → manager moins planificateur → pas de réduction headcount documentée → nouveaux usages/skills → process/store/inventory data → workflow recommandé par IA → pouvoir de séquencement partiellement logiciel → gain temps`

Le cas est moins un dossier « emploi supprimé » qu'un dossier **qui décide de la journée de travail**. Un outil comprend, priorise et recommande les tâches d'équipes, tandis que le temps de planification d'un shift passe de 90 à 30 minutes.

Source :
- https://corporate.walmart.com/news/2025/06/24/walmart-unveils-new-ai-powered-tools-to-empower-1-5-million-associates

---

## Cas 8 — Salesforce : substitution visible, traçabilité sociale incomplète

### Chaîne
`Agentforce → résolution/routage support → fonction support réduite → non-backfill + redéploiement partiel → agent supervision → Data Cloud/conversations → décision de résolution/escalade → pouvoir agent/humain → coûts/case volume ↓`

La technologie est incontestable : 380 000 conversations et 84% de résolution sur help.salesforce.com fin FY25 ; case volume ensuite -7% YoY. La narration de 9 000 → 5 000 personnels support provient du CEO, tandis que l'entreprise a parlé de centaines de redéploiements. **Le devenir exact d'environ 4 000 postes n'est pas réconcilié publiquement.**

Sources :
- https://www.salesforce.com/news/press-releases/2025/02/26/fy25-q4-earnings/
- https://www.salesforce.com/news/press-releases/2025/05/28/fy26-q1-earnings/
- https://www.salesforce.com/news/press-releases/2026/02/25/fy26-q4-earnings/

---

## Cas 9 — A&O Shearman : l'expertise devient actif logiciel

### Chaîne
`Harvey + ContractMatrix + agents → drafting/review/reasoning → lawyers stratégiques/human-in-loop → pas de job cuts documentés → expertise/AI skill → 20-30 ans de savoir distillés → docs/playbooks/curated data → agents produisent work products → firm controls stack → SaaS + revenue share`

C'est le cas le plus net de **capitalisation du savoir**. La firme écrit explicitement qu'elle « distille » 20 à 30 ans de connaissances juridiques, marché et produit de ses avocats dans des outils. Les agents sont ensuite vendus aux clients et autres cabinets ; A&O Shearman partage les revenus logiciels.

Sources :
- https://www.aoshearman.com/en/insights/alumni-yearbook/ai-leadership-practicing-what-we-preach
- https://www.aoshearman.com/en/news/ao-shearman-and-harvey-to-roll-out-agentic-ai-agents-targeting-complex-legal-workflows
- https://www.aoshearman.com/en/insights/analyze-is-the-new-contractmatrix-module-making-contract-review-even-more-powerful

---

## Cas 10 — Morgan Stanley : automatiser le back-office cognitif pour préserver le conseiller

### Chaîne
`Assistant + Debrief + AskResearchGPT → recherche/notes/email/CRM → conseiller recentré relation/jugement → aucun headcount impact → esprit critique/relations → intellectual capital + 70k reports/an → meeting data consentie → conseiller valide → human touch explicite → capacité client`

Le système transforme la division cognitive du travail sans supprimer le rôle : Debrief prend notes, action items, draft d'email et écrit dans Salesforce ; le conseiller reste celui qui édite et envoie. 98% des équipes d'advisers avaient adopté l'Assistant. Le gain monétaire n'est pas publié.

Sources :
- https://www.morganstanley.com/press-releases/key-milestone-in-innovation-journey-with-openai
- https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch
- https://www.morganstanley.com/press-releases/morgan-stanley-research-announces-askresearchgpt

---

## Findings transversaux

### F1 — Cinq régimes organisationnels
`SUBSTITUTION | HYBRIDATION | AUGMENTATION | CAPITALISATION_DU_SAVOIR | GATE_DE_RESSOURCES`

### F2 — Le recrutement est le maillon le moins visible
Klarna est explicite. Shopify et Duolingo instaurent des gates « AI avant headcount », mais les impacts quantitatifs ne sont pas publiés. BT montre une chute des cohortes juniors mais avec des confounders majeurs. JPMorganChase documente le contraire : redéploiement et croissance.

### F3 — Le savoir est une forme de capital en cours de conversion
A&O Shearman est la preuve la plus nette. Morgan Stanley transforme également une bibliothèque propriétaire et les pratiques de recherche en couche d'assistance généralisée. IBM transforme politiques/processus RH en agent transactionnel.

### F4 — La décision algorithmique est souvent en amont du licenciement
Walmart priorise les tâches ; IBM exécute des transactions RH ; Klarna automatise underwriting ; JPM automatise screening ; Salesforce automatise résolution/escalade. L'impact sur le pouvoir peut précéder l'impact sur l'emploi.

### F5 — « gain de productivité » ne dit rien sur son bénéficiaire
- Klarna : coûts/headcount ↓ + rémunération moyenne ↑.
- JPM : capacité → croissance/redeploy.
- A&O : expertise → produit SaaS.
- Walmart/Morgan : temps → relation/service.
- Shopify/Duolingo : expansion/innovation, distribution monétaire non isolée.
- Salesforce : gain support réel, mais destination distributive non démontrée.
- BT : économies multi-factorielles.
- IBM : coûts RH ↓ + nouveaux postes plateforme.

---

## Gaps P0 ouverts

1. **SHOPIFY-AI-HEADCOUNT** : quantifier combien de demandes de headcount ont été refusées/modifiées par le gate AI.
2. **DUOLINGO-CONTRACTORS** : nombre, fonctions et trajectoire des contractants affectés.
3. **BT-AI-ATTRIBUTION** : séparer IA/fibre/cessions/attrition dans la baisse d'effectif.
4. **SALESFORCE-4000** : réconcilier départs, attrition, non-backfill et redéploiements.
5. **VALUE-LEDGER** : pour chaque firme, tracer un euro de gain vers salaire/prix/profit/capex/fournisseur/cloud.
6. **KNOWLEDGE-PROPERTY** : droits/compensation associés au savoir des experts incorporé dans des outils internes.
7. **ALGO-POWER** : documenter recours, override et métriques d'acceptation pour IBM/Walmart/Klarna.
8. **EARLY-CAREER** : cohortes junior/graduate/apprentice avant-après adoption par entreprise.

## Conclusion RENARD

**REFUTÉ :** une chaîne universelle `IA → tâches automatisées → postes supprimés`.

**SUPPORTED fort :** l'organisation choisit la destination du gain, et cette règle produit des conséquences sociales radicalement différentes.

**SUPPORTED fort :** l'effet le plus important peut survenir avant le licenciement : gate de recrutement, disparition de tâches formatrices, transfert de décision, capture du savoir.

**OPEN :** quantification des emplois non créés et de la destination distributive des gains.

