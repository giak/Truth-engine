# FRESQUE 9D — TRAVAIL & IA
**Investigation:** 2026-08-25 17:03 Europe/Paris  
**Objet:** suivre simultanément le poste, la tâche, le recrutement, la compétence, le savoir, la décision, la donnée, le pouvoir et la valeur.  
**Statut:** enquête intermédiaire, non destinée à publication brute.

## 1. Verdict de travail

Les données consultées ne montrent pas un remplacement massif et agrégé des travailleurs par l'IA en 2026. Elles montrent une transformation multi-niveaux : les tâches changent avant les métiers, l'embauche des jeunes semble constituer un signal plus précoce que les licenciements, l'intégration organisationnelle importe davantage que l'usage individuel, et les outils algorithmiques déplacent aussi le pouvoir de décision, la collecte de données et la répartition de la valeur.

## 2. Matrice 9 dimensions

| Dimension | Fait / signal principal | Niveau | Contre-lecture / limite | Prochaine preuve discriminante |
|---|---|---|---|---|
| Poste | L'intégration IA peut redessiner fonctions et rôles sans destruction immédiate. Au Danemark, réorganisation des tâches et nouveaux rôles IA sans effet >2 % sur heures ou revenus deux ans après ChatGPT. | SUPPORTED | Un pays, horizon court ; effets futurs ouverts. | Panels firm-level France : descriptions de postes avant/après adoption. |
| Tâche | L'automatisation agit d'abord au niveau des tâches. L'exposition moyenne déprime la demande, mais la concentration de l'exposition peut permettre réallocation interne. | SUPPORTED | Exposition != automatisation ; effets modestes sur emploi agrégé. | Études causales par tâche × entreprise. |
| Recrutement | Chez les 22-25 ans américains dans les métiers très exposés, l'écart relatif d'emploi atteint 19 %, surtout par baisse des embauches. | SUPPORTED, non causal | Divergences préexistantes et limites d'échantillon ; auteurs parlent de signaux descriptifs. | Données administratives France, cohortes juniors exposées/non exposées. |
| Compétence | Les novices tirent souvent plus de gains ; experts parfois peu gagnants ou pénalisés. Les besoins en compétences analytiques, IA et jugement augmentent. | SUPPORTED | Forte hétérogénéité selon tâche, modèle et organisation. | Longitudinal : compétence sans IA après période assistée. |
| Savoir | Dans le support client, le système diffuse des pratiques des meilleurs agents aux novices ; l'IA peut donc capturer et redistribuer du savoir opérationnel. | SUPPORTED | Cas unique ; preuve d'appropriation économique du savoir non établie. | Qui possède/valorise le savoir capturé ? clauses, données, rémunération. |
| Décision | Les outils de gestion algorithmique instruisent, surveillent et évaluent déjà les travailleurs. | VERIFIED comme pratique | Définition OECD large, pas uniquement GenAI. | Inventaire France : recrutement, planning, scoring, promotion, sanction. |
| Donnée | Temps, vitesse, contenu de communications, localisation et autres données deviennent des entrées de gestion ; les régulateurs encadrent la proportionnalité. | VERIFIED | Toute collecte n'est pas abusive ; finalité et proportionnalité comptent. | Cartographier data lineage travailleur → score → décision → recours. |
| Pouvoir | La contestabilité dépend de transparence, contrôle humain, représentation collective et capacité de surseoir à une décision automatisée. | SUPPORTED | Effet causal sur rapport de force difficile à quantifier. | Cas de négociation collective et contentieux avec résultat mesuré. |
| Valeur | Les gains micro de productivité sont réels mais se traduisent mal dans les agrégats ; baisse du coût du capital d'automatisation peut réduire la part du travail dans certains modèles. | SUPPORTED | LCE IMF n'est pas un gain de PIB ; distribution effective ouverte. | Tracer euro économisé : salaire, prix, profit, capex, fournisseur IA. |

## 3. Découvertes discriminantes

### D1 — Usage individuel != restructuration
Le Census 2026 trouve que 66 % des entreprises utilisatrices se servent de l'IA seulement pour augmenter des tâches, tandis que 2 % déclarent des baisses d'emploi liées à l'IA. En revanche, la largeur d'intégration fonctionnelle et l'investissement opérationnel sont associés aux baisses d'effectifs, alors que l'usage par les travailleurs ne l'est plus une fois ces dimensions contrôlées.

### D2 — Le recrutement semble précéder le licenciement
Le papier Stanford/ADP révisé en août 2026 trouve un écart relatif de 19 % pour les 22-25 ans dans les professions fortement exposées, principalement par baisse d'embauche. Les auteurs insistent : il s'agit d'indicateurs descriptifs précoces, pas d'une estimation causale définitive.

### D3 — Le savoir expert peut devenir un actif incorporé au système
Dans le support client, l'assistant augmente la productivité moyenne d'environ 15 %, surtout pour les novices. Les auteurs trouvent des indices que le système diffuse les meilleures pratiques des agents plus performants. Cela crée un nouveau dossier : extraction/capture/redistribution du savoir tacite et partage de la valeur correspondante.

### D4 — La gestion algorithmique est déjà une infrastructure de pouvoir
L'OECD définit la gestion algorithmique comme l'automatisation ou le soutien de tâches managériales. Dans son enquête, 81 % des entreprises françaises couvertes utilisent au moins un outil pour instruire, surveiller ou évaluer. Les managers utilisateurs citent aussi l'opacité, la responsabilité en cas d'erreur et la santé des travailleurs parmi leurs inquiétudes.

### D5 — La donnée du travailleur devient simultanément preuve, métrique et levier
CNIL, OECD et directive européenne sur le travail via plateformes convergent : la donnée peut affecter planning, accès au travail, évaluation, rémunération, sécurité, formation et statut. La question forensique devient la lignée : donnée collectée → transformation → score → décision → humain responsable → recours.

### D6 — Le gain de productivité ne dit pas qui gagne
L'IMF estime un « labor cost equivalent » de 2,7 T$ annualisés à partir d'usages de Claude, mais précise qu'il ne s'agit pas d'un effet direct sur le PIB ni d'une mesure des effets d'emploi. L'OIT souligne le paradoxe d'agrégation : les gains micro ne sont pas encore clairement visibles à l'échelle macro. La distribution reste un objet distinct.

## 4. H à maintenir / affaiblir

| Hypothèse | Statut | Motif |
|---|---|---|
| H1 : « l'IA remplace déjà massivement le travail » | WEAKEN fortement | données agrégées et firm-level ne le montrent pas |
| H2 : « l'IA transforme d'abord tâches et organisation » | STRENGTHEN | Danemark, Census, OIT, QJE |
| H3 : « l'embauche junior est un canal précoce » | STRENGTHEN prudent | Stanford/ADP, mais causalité non close |
| H4 : « la compétence humaine devient inutile » | KILL | effets hétérogènes, besoin de jugement/compétence souvent accru |
| H5 : « le savoir expert peut être capturé et redistribué » | MAINTAIN/STRENGTHEN | support client + systèmes fondés sur historique de bonnes pratiques |
| H6 : « la gestion algorithmique déplace le pouvoir managérial » | STRENGTHEN | OECD, UE, CNIL |
| H7 : « plus de productivité = plus de prospérité partagée » | KILL comme identité automatique | distribution dépend d'institutions, prix, salaires, concurrence, bargaining |
| H8 : « les effets sont déterminés par la technologie seule » | KILL | organisation, formation, droit, dialogue social changent les résultats |

## 5. Gaps P0

1. France : causalité IA → baisse des embauches juniors.
2. Poste : mesurer le redessin réel des descriptions de postes avant/après intégration.
3. Savoir : propriété économique et rémunération du savoir capturé dans les systèmes.
4. Donnée : reconstruire des chaînes concrètes donnée → score → décision → recours.
5. Valeur : suivre l'euro de gain de productivité au niveau entreprise.
6. Pouvoir : mesurer l'effet de consultation/négociation collective sur les résultats.
7. Emploi contrefactuel : mesurer les postes jamais créés.
8. Agrégation : expliquer pourquoi gains micro ne deviennent pas toujours productivité macro.

## 6. Sources effectivement consultées

- **S1** | T2 | OIT | 2026-06-01 | The impact of GenAI on jobs, productivity and work organization | https://www.ilo.org/publications/impact-genai-jobs-productivity-and-work-organization-review-empirical
- **S2** | T2 | Stanford Digital Economy Lab | 2026-08-12 | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence | https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/
- **S3** | T1/T2 | U.S. Census Bureau | 2026-05-07 | The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks | https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html
- **S4** | T2 | NBER / Danish administrative data | 2026-03 revision | Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI | https://www.nber.org/papers/w33777
- **S5** | T2 | QJE | 2025-05 | Generative AI at Work | https://academic.oup.com/qje/article/140/2/889/7990658
- **S6** | T2 | OECD | 2026-06-05 | AI and skills: What we know so far | https://www.oecd.org/en/publications/ai-and-skills_f843b352-en/full-report.html
- **S7** | T2 | OECD | 2025-12-19 | How widespread is algorithmic management in workplaces? | https://www.oecd.org/en/publications/how-widespread-is-algorithmic-management-in-workplaces_cda7a114-en/full-report.html
- **S8** | T2 | OIT | 2026-04-30 | AI systems @ work: a changing psychosocial work environment | https://www.ilo.org/publications/ai-systems-work-changing-psychosocial-work-environment
- **S9** | T2 | OIT / Weizenbaum Journal | 2026-05-01 | Challenging the Myth of AI Autonomy | https://researchrepository.ilo.org/esploro/outputs/journalArticle/Challenging-the-Myth-of-AI-Autonomy/995703567802676?institution=41ILO_INST
- **S10** | T1 | Union européenne | 2024-10-23 | Directive (UE) 2024/2831 sur le travail via plateformes | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202402831
- **S11** | T1/T2 | CNIL | 2026-07 | Travail, ressources humaines : le contrôle de l’activité des personnes employées | https://www.cnil.fr/fr/controle-de-lactivite-des-personnes-employees
- **S12** | T1/T2 | CNIL | 2025-02-04 | Surveillance excessive des salariés : sanction de 40 000 euros | https://www.cnil.fr/fr/surveillance-excessive-des-salaries-sanction-de-40-000-euros-entreprise-secteur-immobilier
- **S13** | T1 | EEOC | 2023-09-11 | iTutorGroup to Pay $365,000 to Settle EEOC Discriminatory Hiring Suit | https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit
- **S14** | T2 | IMF | 2026-07-10 | Aggregate Gains from AI and Their Distribution: Global Evidence from Usage Data | https://www.imf.org/en/publications/wp/issues/2026/07/10/aggregate-gains-from-ai-and-their-distribution-global-evidence-from-usage-data-577586
- **S15** | T2 | AEA | 2026-04 | Not a Typical Firm: Capital–Labor Substitution and Firms' Labor Shares | https://www.aeaweb.org/articles?id=10.1257%2Fmac.20230325
- **S16** | T2 | OIT | 2025-07-10 | Global case studies of social dialogue on AI and algorithmic management | https://www.ilo.org/publications/global-case-studies-social-dialogue-ai-and-algorithmic-management
- **S17** | T2 | OIT et partenaires | 2026-08-13 | Changing landscape of skills in the age of AI | https://www.ilo.org/publications/changing-landscape-skills-age-ai
- **S18** | T2 | NBER / multi-country executives | 2026-03 revision | Firm Data on AI | https://www.nber.org/papers/w34836
- **S19** | T2 | HBS/BCG | 2026 version | Navigating the Jagged Technological Frontier | https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf

## 7. Limites

- Plusieurs résultats 2026 sont des working papers ou rapports institutionnels, pas des causalités définitives.
- Les données américaines ne se transfèrent pas automatiquement à la France.
- « Gestion algorithmique » couvre des outils plus larges que la seule GenAI.
- Les gains de productivité à la tâche ne préjugent ni de l'emploi net, ni des salaires, ni de la répartition.
- Les chiffres de « valeur » fondés sur usages IA dépendent d'hypothèses de temps gagné, salaires et pénétration de marché.
- Les sources web sont enregistrées par URL et date de consultation, mais leurs snapshots locaux restent à archiver.

## 8. Prochaine salve

Priorité : construire 10 cas causaux complets en France/Europe, chacun tracé sur les neuf dimensions. Un cas ne sera retenu que s'il permet de documenter au minimum : technologie réellement déployée, tâche modifiée, décision organisationnelle, effet RH mesuré, données utilisées, mécanisme de contrôle, et destination du gain économique.

