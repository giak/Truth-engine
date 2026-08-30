# INVESTIGATION — Licenciements « IA » et prix des services

**Date :** 2026-08-25  
**Investigation ID :** `INV-AILAYOFF-001`  
**Protocole :** RENARD CORE V3  
**Objet :** auditer 20 restructurations/licenciements associés publiquement à l'IA et tester le canal `IA → productivité → prix des services → emploi`.

## [DECOMPOSE]

| Atom | Sous-question | Verdict recherché |
|---|---|---|
| L1 | La technologie effectuait-elle réellement le travail des postes supprimés ? | DIRECT / PARTIEL / NON ÉTABLI |
| L2 | L'IA finance-t-elle ou motive-t-elle seulement une réallocation de ressources ? | OUI/NON |
| L3 | L'entreprise subit-elle plutôt une disruption externe par l'IA ? | OUI/NON |
| L4 | Les causes classiques précèdent-elles l'annonce IA ? | OUI/NON |
| L5 | La réduction locale est-elle une destruction nette au niveau du groupe ? | OUI/NON/OPEN |
| P1 | L'IA modifie-t-elle déjà la facturation des services avant l'emploi ? | OUI/PARTIEL/OPEN |

## [SHADOW]

Sous une vraie substitution directe, on attend : technologie nommée, production avant licenciement, tâche mesurée, gain net après supervision, rôle humain correspondant, baisse/non-remplacement postérieure, et peu de causes concurrentes.

Sous le rival « restructuration classique + récit IA », on attend : plan de coûts ou ralentissement antérieur, M&A/cession/sur-embauche, technologie encore en pilote ou future, absence de mapping tâche→poste, et réembauche/redéploiement ailleurs.

## Résultat central

Dans ce panel **délibérément biaisé vers des cas où l'IA est citée**, seuls Klarna et la fonction support de Salesforce offrent une chaîne publique relativement forte `IA en production → tâche comprimée → besoin humain réduit`. Duolingo fournit un cas partiel sur les contractants.

La majorité des autres dossiers relève plutôt de :
- réallocation de capital et de compétences vers l'IA ;
- restructuration multicausale ;
- anticipation de capacités futures ;
- disruption externe du modèle économique ;
- communication IA superposée à des causes traditionnelles.

Ce panel n'est pas représentatif du marché du travail. Il est précisément construit pour tester les annonces les plus favorables à la thèse « l'IA supprime déjà les emplois ».

## Les 20 cas

| Organisation | Emplois/postes | Type | Grade causal | Risque narratif | Verdict |
|---|---:|---|---|---|---|
| Block | ~4,000 / ~40% | ANTICIPATORY_AI_RESTRUCTURE | B | HIGH | AI is central to the stated decision, but causal magnitude is not independently demonstrated. |
| Klarna | 5,527 → 2,831 employees | DIRECT_SUBSTITUTION | A | LOW | Strongest task→productivity→headcount case in the panel. |
| Salesforce | Support ~9,000 → ~5,000 | FUNCTIONAL_SUBSTITUTION | A- | MEDIUM | Strong local substitution, false if narrated as 4,000 net company jobs destroyed. |
| Duolingo | 10% contractor offboarding; salaried headcount ↑ | CONTRACTOR_SUBSTITUTION | B | MEDIUM | Recomposition of status and skill mix, not aggregate salaried contraction. |
| IBM | ~7,800 roles over five years (forecast) | NON_REPLACEMENT_FORECAST | C | HIGH | Classic example of a projection becoming a headline that looks like an observed job loss. |
| HP | 4,000–6,000 | DIRECT_FUTURE_PLAN | B- | MEDIUM | Credible AI-linked plan, but still prospective rather than demonstrated substitution. |
| Meta | ~10% workforce; 7,000 moved to AI initiatives | ANTICIPATORY_AI_RESTRUCTURE | C | HIGH | Rare evidence that organizational anticipation ran ahead of expected technical capability. |
| Amazon | 14,000 then 16,000 corporate roles | MULTICAUSAL_RESTRUCTURE | D | HIGH | AI is a material context, not a clean causal explanation for the 30,000-role program. |
| Microsoft | 4,800 | PORTFOLIO_REALLOCATION | E | HIGH | Strong control against reading every Big Tech cut as AI replacement. |
| Workday | 1,750 / 8.5% | RESOURCE_REALLOCATION | C | MEDIUM | AI helps explain where resources are redirected, not proof that AI performed 1,750 jobs. |
| Intuit | ~3,000 / 17% | DISRUPTION_AND_REALLOCATION | C | MEDIUM | AI is both an external competitive shock and an investment priority, not simple internal replacement. |
| Chegg | 388 / ~45% | EXTERNAL_AI_DISRUPTION | B | LOW | Strong evidence of AI-linked employment impact through market disruption rather than automation. |
| Indeed / Glassdoor | ~1,300 / 6% HR-tech unit | INTEGRATION_AND_MERGER | D | HIGH | AI-rich announcement, weak public causal mapping. |
| Cisco | 7% global workforce | RESOURCE_SHIFT | C | HIGH | Primarily capital/talent reallocation toward growth areas. |
| SAP | up to ~10,000 roles evaluated | SKILLS_AND_CLOUD_SHIFT | C | MEDIUM | AI-era restructuring, not measured AI replacement. |
| Accenture | $865m restructuring; role exits not fully quantified in source | SKILLS_SHIFT | C | MEDIUM | Skill composition change is better supported than net AI substitution. |
| BT Group | up to 55,000 incl. contractors | MULTICAUSAL_LONG_TERM | D | MEDIUM | Major long-run transformation, but AI share remains unidentified. |
| Capgemini | ~€700m restructuring; 5,800 headcount decline H1 2026 excl. acquisition effects | SKILLS_SHIFT | C | MEDIUM | Real business shift and real restructuring, but no public task→job causal mapping. |
| Société Générale | 1,800 net positions | MULTICAUSAL_NATURAL_ATTRITION | D | LOW | Good forensic example of why '1,800 jobs cut by AI' would exceed the source. |
| Michelin | up to 1,500 positions, voluntary | CONTROL_NO_PRIMARY_AI | E | LOW | Control case: contemporaneous white-collar restructuring without a primary AI claim. |

### Répartition analytique du panel

- Grade **A/A-** : 2 cas.
- Grade **B/B-** : 4 cas.
- Grade **C** : 8 cas.
- Grade **D** : 4 cas.
- Grade **E** : 2 cas.

**Important :** ce grade mesure la qualité du lien public `IA → changement d'effectif`, pas la qualité générale de l'entreprise ni la performance de sa technologie.

## Perles forensiques

### Meta : restructurer sur une capacité qui n'arrive pas au rythme attendu
Meta a restructuré 10% de ses effectifs et déplacé 7 000 salariés vers des initiatives IA selon des principes d'organisation « AI native ». Quelques semaines plus tard, Mark Zuckerberg a reconnu que les agents n'avaient pas accéléré comme attendu et que le timing de la restructuration avait été mal estimé.

Ce cas est exceptionnel parce qu'il documente :
`anticipation technique → décision organisationnelle → capacité plus lente que prévu`.

Il établit qu'une restructuration peut être causée par **l'attente de l'IA**, indépendamment de la productivité déjà réalisée.

### Microsoft : contre-preuve explicite
Microsoft supprime 4 800 postes dans une restructuration Xbox, mais sa responsable RH écrit explicitement que les postes éliminés « ne sont pas remplacés par l'IA ». Le même article relie néanmoins la discipline de headcount à la nécessité de financer des investissements IA massifs.

Donc deux canaux différents :
`IA remplace le travail != capex IA évince des budgets de personnel`.

### IBM : le « 7 800 emplois perdus » est d'abord une projection de non-remplacement
Le chiffre de 7 800 correspond à 30% de fonctions non-client estimées remplaçables sur cinq ans, y compris par attrition. Ce n'est pas un registre de 7 800 salariés licenciés par une IA.

### Chegg : l'IA peut supprimer des emplois sans automatiser l'entreprise
Chegg réduit 45% de son personnel parce que les utilisateurs et Google se déplacent vers des réponses IA. Ici :
`IA concurrente → trafic/revenus ↓ → emploi ↓`.
La machine ne remplace pas directement les salariés de Chegg : elle détruit une partie de leur marché.

### Challenger : mesurer le récit, pas confondre avec la causalité
Challenger comptabilise en juillet 2026 112 713 suppressions annoncées où l'IA est citée, 24% des coupes annoncées de l'année. Challenger précise aussi que citer l'IA peut séduire les investisseurs. Cette base est très utile pour mesurer le **motif déclaré**, pas pour prouver la substitution technique.

## Détecteur de « bullshit IA »

Le terme est ici un nom de travail. Le score ne mesure jamais un mensonge. Il mesure le **risque d'écart probatoire** entre une affirmation et les éléments publics permettant de la vérifier.

| # | Question | Preuve attendue | Signal d'alerte |
|---|---|---|---|
| BS-01 | Technologie nommée ? | Produit/modèle/agent identifiable, version et fournisseur. | 'AI' générique sans système identifiable. |
| BS-02 | En production ? | Date de mise en production et périmètre réel. | POC, pilote ou futur présenté comme capacité actuelle. |
| BS-03 | Utilisateurs/volume ? | Nombre d'utilisateurs, cas, transactions, requêtes. | Adoption non quantifiée. |
| BS-04 | Tâche exacte ? | Workflow avant/après explicite. | 'Productivité' sans tâche. |
| BS-05 | KPI avant/après ? | Temps, coût, qualité, volume ou revenue mesuré. | Pourcentage sans baseline ou sans période. |
| BS-06 | Erreur/qualité ? | Taux d'erreur, escalade, rework, supervision. | Gain de vitesse sans coût de vérification. |
| BS-07 | Coût complet ? | Licences, compute, intégration, maintenance, formation. | Économies brutes sans coûts IA. |
| BS-08 | Causalité emploi ? | Tâches automatisées reliées aux postes touchés et chronologie cohérente. | Licenciement + IA dans la même annonce. |
| BS-09 | Contre-factuel ? | Demande, conjoncture, sur-embauche, M&A, cessions, simplification contrôlées. | Aucune cause concurrente discutée. |
| BS-10 | Recrutement ailleurs ? | Headcount groupe, postes ouverts, redéploiements, internal hires. | Réduction d'une fonction racontée comme perte nette. |
| BS-11 | Destination du gain ? | Salaire, prix, profit, capex, croissance, cloud, buyback identifiés. | 'Valeur créée' sans bénéficiaire. |
| BS-12 | Qui mesure ? | Audit indépendant, filing, KPI reproductible ou seulement management/vendor. | Vendor/CEO comme seule preuve. |

### Règle d'usage
Une annonce ne devient « substitution IA » que si les items 1 à 8 sont suffisamment documentés. Les items 9 à 12 servent à casser la causalité apparente et à tracer la distribution du gain.

## Dossier services : le prix bouge avant l'emploi

| Secteur | État | Observation |
|---|---|---|
| IT services / India | OBSERVED_MARKET_SHIFT | Clients demand more productivity for lower prices; TCS/Infosys/Wipro/HCL/Cognizant move part of contracting from time-and-materials toward outcome/performance models. |
| Legal services | COMMERCIAL_MODEL_LAG | 71% of in-house legal professionals expect outside firms to change commercial models as AI rises; only 28% of law firms report pricing changes so far. |
| Legal services | RATES_STILL_RISING | Major US law-firm billing rates and revenues rose strongly in 2025 while firms also absorbed rising AI-tech and labor costs. |
| Consulting | PRICING_MODEL_THEORY | Recent Stanford Digital Economy Lab framework predicts movement toward hybrid and asset/outcome-based structures as AI changes input and outcome observability. |
| Tax / accounting | EMERGING_SUBSCRIPTIONS_OUTCOMES | Industry evidence points toward packages, subscriptions and value/outcome pricing as hourly work becomes easier to automate. |

### IT services : première bascule commerciale clairement observable
Dans les services informatiques indiens, des contrats passent du temps/homme à la performance ou au résultat. Les clients exigent davantage de productivité pour moins cher. Les acteurs de taille moyenne peuvent gagner des contrats avec des équipes plus petites et des pilotes plus rapides.

La chaîne devient :
`IA → temps nécessaire ↓ → valeur du jour-homme ↓ → prix/contrat renégocié → pyramid staffing ↓ → recrutement junior sous pression`.

### Droit : attente forte, économie encore résistante
Le contraste est très instructif :
- 71% des juristes d'entreprise attendent un changement des modèles commerciaux avec l'IA ;
- seulement 28% des cabinets déclarent avoir modifié leur tarification ;
- en parallèle, les taux horaires des grands cabinets ont encore fortement augmenté.

Donc le billable hour n'est pas mort. **La tension est réelle, la bascule n'est pas achevée.**

### Consulting : mécanisme probable, adoption à mesurer
Le récent cadre du Stanford Digital Economy Lab montre pourquoi les agents IA poussent économiquement vers des contrats hybrides, par actifs ou par résultats. C'est un mécanisme théorique/stratégique solide, pas encore une mesure de prévalence.

## [ADVERSARY]

| Test | H « substitution IA » | Rival | Observation |
|---|---|---|---|
| Timing | technologie productive avant coupe | coupe précède ou accompagne le pari | Meta affaiblit H |
| Mapping | tâches précises → rôles précis | aucune cartographie | majorité du panel favorise rival |
| Causes concurrentes | faibles | sur-embauche, coûts, M&A, demande, simplification | Amazon, Microsoft, SG, Michelin, Cisco favorisent rival |
| Headcount groupe | baisse nette | redéploiement/recrutement ailleurs | Salesforce, Duolingo, Workday nuancent H |
| Disruption externe | non | AI change demande/prix du marché | Chegg, Intuit |
| Prix services | inchangé | productivité change contrats avant emplois | IT indien favorise rival « effet indirect » |

## [EVALUATE]

| Hypothèse | Statut | Confiance |
|---|---|---:|
| « Une grande part des licenciements estampillés IA sont des remplacements techniques directs » | **WEAKEN** | 0.90 |
| « L'IA sert déjà de justification ou de langage de réallocation organisationnelle » | **STRENGTHEN** | 0.94 |
| « Certaines restructurations sont déclenchées par l'anticipation de capacités futures » | **SUPPORTED** | 0.91 |
| « L'IA détruit aussi des emplois par disruption externe du modèle économique » | **SUPPORTED FORT** | 0.94 |
| « Le choc des services passe déjà par les prix/contrats » | **SUPPORTED sur IT, SIGNAL ailleurs** | 0.89 |
| « Le temps facturable va disparaître rapidement partout » | **WEAKEN** | 0.88 |

## [REPORT]

| Field | Content |
|---|---|
| what_changed_since_last | On sépare désormais substitution interne, réallocation vers l'IA, anticipation, disruption externe et restructuration classique |
| surviving_H | Le récit IA a un effet organisationnel réel même quand la technologie ne remplace pas encore directement les salariés |
| killed_H | « licenciement + IA dans le communiqué = emploi remplacé par IA » |
| confidence_before -> confidence_after | risque d'inflation narrative 0,70 → 0,94 |
| next_priority | Étudier la **pyramide des services** : juniors, taux d'utilisation, prix/jour, effectifs par grade et modèles de facturation France/Europe |
| CALIBRATION | assez robuste pour l'architecture éditoriale ; pas pour un chiffre net d'emplois attribuable à l'IA |

## Conclusion

Le mot « IA » recouvre au moins quatre causalités différentes :

1. **substitution** : la machine fait effectivement une partie du travail ;
2. **réallocation** : on supprime ailleurs pour financer ou recruter autour de l'IA ;
3. **anticipation** : l'organisation réduit aujourd'hui sur la foi de gains futurs ;
4. **disruption** : l'IA détruit la demande ou le prix du service vendu.

Les statistiques de licenciements mélangent ces mécanismes.

La prochaine étape ne doit donc plus être « combien de licenciements IA ? », mais :
**quelle causalité, à quel étage de la chaîne, et avec quel contre-factuel ?**
