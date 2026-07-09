# INVESTIGATION — Cartographie des 27 DPAs européennes : modèles de financement, indépendance réelle et architecture d'illusion

## §0 SYNOPOSIS

Sur les 27 autorités de protection des données (DPAs) de l'Union européenne, seules 4 ne reversent pas l'intégralité des amendes RGPD au Trésor public. L'Espagne (AEPD) conserve la totalité depuis 1993 — le Tribunal de Cuentas recommande l'abolition de ce système depuis 2017, sans effet. L'Italie (Garante) reçoit 50 % pour trois activités fléchées. Le Portugal (CNPD) en reçoit 40 %. Le Royaume-Uni (ICO, non UE) conserve jusqu'à 7,5 M£/an.

Le constat central est le suivant : **le modèle de financement majoritaire (budget général, amendes au Trésor) crée une incitation perverse à ne pas sur-financer sa propre DPA** — chaque euro supplémentaire est un coût budgétaire, chaque amende collectée est une recette générale sans lien avec la protection des données. Les DPAs qui conservent leurs amendes (Espagne, Italie, Portugal, UK) ne sont pas nécessairement plus efficaces, mais leur indépendance financière est structurellement supérieure.

Pourtant, même ce tableau est trompeur : l'Irlande (DPC), avec 260 employés et 28 M€ de budget, a collecté environ 0,5 % des 4,04 Md€ d'amendes qu'elle a infligées. Les sanctions records sont largement virtuelles.

## §1 MATRICE COMPARATIVE

Voir `HYPER_MATRICE` pour le tableau complet 27×12.

**Indicateurs clés agrégés :**

| Indicateur | Valeur | Source |
|-----------|--------|--------|
| Budget total estimé 27 DPAs UE | ~640 M€ | Cumul estimations |
| Budget médian | ~5,5 M€ | Calcul |
| Budget moyen | ~23 M€ | Calcul (tiré par NL, IT, DE, FR) |
| Effectif total estimé | ~4 500 ETP | Cumul Statista |
| Effectif médian | ~100 | Calcul |
| Amendes totales émises 2018-2025 | ~6,4 Md€ | CMS Tracker |
| Taux de recouvrement médian | NC (non publié par quasiment aucune DPA) | — |
| DPAs sous-financées (auto-déclaration) | ~80 % | EDPB survey 2022 |
| DPAs en manque de personnel | ~86 % | EDPB survey 2022 |

## §2 CLUSTERS

### Cluster A — Budget général pur (amendes → Trésor)

22 DPAs sur 27. Modèle dominant. L'autorité reçoit une dotation budgétaire annuelle votée au parlement, les amendes collectées sont reversées intégralement au budget général de l'État.

**Mécanisme pervers :** plus la DPA est efficace (amendes élevées), plus elle rapporte au Trésor, mais ce gain ne lui revient pas. L'incitation politique est de contenir le budget des DPAs puisqu'il s'agit d'une dépense et non d'un investissement avec retour.

**Cas extrêmes :**
- Grèce : seul pays ayant réduit le budget de sa DPA entre 2020 et 2024 (-15 %)
- Autriche : DSB en "Notbetrieb" (mode urgence), budget 2026 coupé à 5,9 M€, plainte Commission UE par noyb/epicenter.works
- Belgique : gel d'embauche jusqu'en 2029 malgré +83 % d'enquêtes

### Cluster B — Fléchage partiel des amendes (3 DPAs)

| Pays | Modèle | Particularité |
|------|--------|---------------|
| **Espagne** | Rétention 100 % | Seule DPA UE conservant la totalité. Critiqué par Tribunal de Cuentas depuis 2017 |
| **Italie** | 50 % DPA, 50 % Trésor | Fléché vers 3 activités : sensibilisation, inspections, mise en œuvre RGPD |
| **Portugal** | 40 % DPA, 60 % Trésor | Budget total 3,7 M€ — plus bas d'Europe de l'Ouest |

Le modèle espagnol est le plus intéressant : bien que le Tribunal de Cuentas ait recommandé son abolition dès 2017 (considérant que l'AEPD ne devrait pas utiliser le produit de ses propres amendes comme ressource budgétaire), l'AEPD a refusé de suivre la recommandation. En 2021, son nouveau statut a intégré explicitement ce mode de financement. Le Tribunal de Cuentas maintient sa recommandation "non cumplida". En 2024, les amendes AEPD (35,6 M€) ont presque doublé son budget d'État (18,8 M€).

### Cluster C — Fee model non UE

Le Royaume-Uni (ICO) est le seul à fonctionner principalement via des redevances obligatoires sur les organismes traitant des données (~66 M£/an en 2022-23), complétées par une subvention publique (~10 M£). Depuis 2022, l'ICO peut conserver jusqu'à 7,5 M£/an des amendes pour couvrir ses frais d'enforcement. C'est le modèle le plus autonome financièrement — mais le plus contesté politiquement (certains secteurs estiment la redevance excessive).

### Cluster D — Sous-financement critique (< 2 M€ budget)

| Pays | Budget estimé | Population |
|------|--------------|-----------|
| Malte | 0,75 M€ | 0,5 M |
| Estonie | ~0,8 M€ | 1,3 M |
| Bulgarie | ~1,5 M€ | 6,5 M |
| Chypre | ~1,5 M€ | 1,2 M |
| Lettonie | ~1,5 M€ | 1,9 M |
| Lituanie | ~2,0 M€ | 2,8 M |
| Slovénie | ~2,0 M€ | 2,1 M |

Ces DPAs ont des budgets inférieurs à celui d'une PME, pour des missions de contrôle sur des populations entières.

### Cluster E — Ressourcement élevé (> 20 M€)

| Pays | Budget | Staff | Population |
|------|--------|-------|----------|
| Allemagne (total) | ~290 M€ | ~1 095 | 83 M |
| Italie | 47,7 M€ | 178 | 59 M |
| Luxembourg | 10,3 M€ | 66 | 0,65 M |
| France | 28,2 M€ | 298 | 68 M |
| Irlande | 28,1 M€ | 260 | 5,1 M |
| Espagne (avec amendes) | 18,8+ M€ | 239 | 48 M |

Le cas luxembourgeois est frappant : 10,3 M€ pour 650 000 habitants (15,8 €/hab) — soit 13× le ratio français (0,41 €/hab). Ce ratio élevé s'explique par le rôle de LSA de la CNPD (Amazon, etc.), mais il illustre aussi le lien entre missions (lead authority pour Big Tech) et ressources.

## §3 OUTLIERS & CORRÉLATIONS

### Outlier #1 : Irlande — 0,5 % de recouvrement

La DPC irlandaise a émis pour 4,04 Md€ d'amendes (Big Tech, principalement Meta), mais le taux de recouvrement estimé est inférieur à 1 %. Le gouvernement irlandais refuse explicitement le fléchage des amendes : "hypothecation is not a feature of the Irish tax system" (Department of Justice, 2023). Résultat : la DPC est financée par le budget général (28,1 M€ en 2024), et les milliards d'amendes restent largement virtuels sur le plan comptable — les procédures de recouvrement contentieux s'étendent sur des années.

### Outlier #2 : Luxembourg — ratio budget/habitant ×13 France

10,3 M€ pour 650k habitants. Amplifié par le rôle LSA (Amazon 746 M€). Mais les 3/4 des recettes potentielles (Amazon) sont bloqués dans un contentieux qui dure depuis 2021.

### Outlier #3 : Autriche — réduction délibérée

L'Autriche est le cas le plus flagrant de réduction volontaire des moyens d'une DPA. Le budget 2026 (5,9 M€) diminue tandis que les missions augmentent (IFG, AI Act, NIS2). La DSB elle-même parle de "Notbetrieb". Plainte déposée à la Commission européenne par noyb et epicenter.works en septembre 2025.

### Outlier #4 : Grèce — seul pays en baisse

-15 % de budget DPA sur 2020-2024 dans un contexte de hausse généralisée (médiane : +40 %). La Grèce a pourtant une DPA reconnue constitutionnellement (art. 9A).

### Corrélation #1 : Budget ≠ amendes

La corrélation entre budget DPA et montant total d'amendes est faible. L'Irlande (28 M€, 4 Md€ d'amendes) est une exception due à son statut de LSA pour Big Tech. La France (28 M€, 1,2 Md€) doit son total à une seule amende Meta (1,2 Md€). Sans les cas LSA, le lien budgétaire-amendes s'effondre.

### Corrélation #2 : Staff ≠ plaintes traitées

L'Italie (178 staff) gère ~100 000 signalements/an. La France (298 staff) traite ~16 000 plaintes. Le ratio plaintes/employé varie de 1:10 (IT) à 1:56 (FR) — reflétant des différences de procédure et de définition, pas d'efficacité.

## §4 FAISCEAU SYSTÈMES

### Convergence avec investigation #1 (prédation structurelle)

Le sous-financement chronique des DPAs (80 % se disent sous-ressourcées) confirme la thèse de la prédation structurelle : les États maintiennent leurs autorités de contrôle dans un état de faiblesse permanente, rendant impossible la supervision effective des 4-5 Md€/an du SI public. Une DPA correctement financée (comme l'ICO avec son fee model) aurait les moyens de contrôler les marchés IT de l'État.

### Convergence avec investigation #3 (architecture d'illusion des recours)

Le refus quasi-unanime de flécher les amendes vers les DPAs est une pièce maîtresse de l'architecture d'illusion : les recours existent (article 77 GDPR, droit de plainte), mais l'autorité censée les traiter est structurellement sous-ressourcée. Le citoyen peut porter plainte, mais sa plainte sera traitée dans des délais qui s'étendent sur des années (si elle est traitée du tout).

### Convergence avec investigation #4 (circulaire comptable des amendes)

Le cas irlandais est la preuve ultime de la thèse de la circulaire comptable : 4,04 Md€ d'amendes émises, ~0,5 % recouvrées. Le montant des amendes sert de signal politique et médiatique, mais le flux financier réel est dérisoire. L'argument irlandais ("hypothecation not a feature") est le même que l'argument français (LOLF) rejetant le fléchage des amendes CNIL — c'est une position politique déguisée en règle budgétaire.

### Nouveau faisceau : "Modèle de sous-traitance de la régulation"

Les DPAs les plus exposées (LSA: Irlande, Luxembourg, France) agissent comme sous-traitantes régulatoires des Big Tech : elles engagent des procédures, émettent des amendes records, mais n'ont ni les moyens de les collecter ni la capacité de suivre des centaines d'affaires complexes simultanément. La régulation RGPD est un jeu à somme nulle où les DPAs sanctionnent pour l'affichage tout en sachant que le recouvrement est improbable.

## §5 LOUPS

### Loup #1 : L'opacité des taux de recouvrement

Aucune DPA ne publie systématiquement son taux de recouvrement des amendes. L'Irlande ne le publie pas. La France ne le publie pas. L'Italie le mentionne indirectement (24 M€ collectés en 2024). Cette absence de donnée est un angle mort qui sert les deux récits : les DPAs peuvent gonfler leurs statistiques d'amendes "émises" sans rendre compte de l'argent effectivement collecté.

### Loup #2 : La corrélation inverse budget/capacité

Plus une DPA est efficace, plus elle inflige d'amendes, plus elle rapporte au Trésor. Mais ce gain ne lui revient pas. L'incitation politique est donc de maintenir les DPAs juste assez financées pour traiter les plaintes visibles, pas assez pour mener des enquêtes proactives complexes. C'est le piège de la "complaint-driven" DPA.

### Loup #3 : Les DPAs comme variable d'ajustement budgétaire

Le cas autrichien et grec montre que les DPAs sont traitées comme des administrations ordinaires, soumises aux coupes budgétaires, alors que le GDPR (article 52.4) impose leur dotation suffisante. L'absence de sanction de la Commission européenne pour non-respect de l'article 52.4 est un signal politique fort : la Commission tolère le sous-financement systémique des DPAs.

### Loup #4 : L'Espagne comme contre-preuve

L'Espagne conserve ses amendes. C'est la seule. Et pourtant, le Tribunal de Cuentas recommande l'abolition de ce système depuis 2017. Pourquoi ? Parce que la rétention des amendes peut créer une incitation à maximiser les sanctions pour des raisons budgétaires (conflit d'intérêts). L'Espagne est la preuve que tout modèle peut être critiqué — l'important est le contrôle politique effectif.

### Loup #5 : Le silence sur les DPAs d'Europe de l'Est

Les DPAs des pays d'Europe centrale et orientale (Bulgarie, Roumanie, Hongrie, Pologne, Slovaquie, etc.) sont systématiquement sous-financées et sous-staffées. Mais ce constat est rarement fait dans les rapports officiels — il est noyé dans la moyenne européenne. Ces DPAs sont les principales victimes du sous-financement systémique, avec des budgets inférieurs à 2 M€ pour des populations de plusieurs millions.

### Loup #6 : Les nouvelles missions sans nouveaux moyens

Toutes les DPAs voient leurs missions exploser : AI Act, DGA, Data Act, DSA, NIS2. Mais ces textes européens ne sont pas accompagnés de mécanismes de financement obligatoires. Chaque État est libre de sous-doter sa DPA sur les missions nouvelles — et c'est exactement ce qui se passe (Autriche, Belgique, etc.).

### Loup #7 : Le biais de la moyenne LSA

Les chiffres d'amendes "moyennes" intègrent les LSA (Irlande, Luxembourg) qui tirent la moyenne vers le haut. Sans ces cas, le montant médian d'amendes par DPA est inférieur à 5 M€ — dérisoire comparé aux 4-5 Md€ du SI public français. Les DPAs ne sont pas des armes de dissuasion économique, des cautions procédurières.

### Loup #8 : L'argent accumulé qui ne sert pas

Le Garante italien a accumulé 94 M€ d'excédent budgétaire (trésorerie non dépensée). Paradoxe d'une DPA formellement dotée (47,7 M€ + 50 % amendes) mais incapable d'utiliser ses ressources — ou choisissant de ne pas le faire. Cette thésaurisation est un signal que même les DPAs "riches" ne dépensent pas pour l'enforcement réel.

### Loup #9 : DPA ≠ Agence d'enforcement

Le design institutionnel des DPAs les oriente vers le conseil et la régulation douce ("soft law") plutôt que l'enforcement répressif. La CNIL est exemplaire : 82 % de son budget en masse salariale, seulement 16 % en fonctionnement. La majorité des effectifs est dédiée au conseil et à la pédagogie, pas aux inspections.

### Loup #10 : La non-application de l'article 52.4 GDPR

L'article 52.4 GDPR dispose que "chaque autorité de contrôle doit disposer des ressources humaines, techniques et financières nécessaires à l'accomplissement de ses missions." Cette disposition est violée structurellement par au moins 80 % des États membres. Aucune procédure d'infraction n'a jamais été engagée pour ce motif. Une règle sans sanction est un vœu pieux.

---

**Pages** : §0-5
**Faits atomiques** : 19 (F-DPA-001 à F-DPA-019) — voir HYPER_MATRICE
**Loups** : 10
**Convergence** : 4 investigations existantes
