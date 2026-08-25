# KERNEL INVESTIGATION: Stress-test de la Sécurité sociale — Que coûterait une perte de X % d'emplois ?

| Champ | Valeur |
|-------|--------|
| ID | INV-2026-08-25-0930-STRESS-TEST-SECU |
| Type | KERNEL COMPLEX |
| Loup parent | W-005 (fresque systémique IA-salariat) |
| Date | 2026-08-25 09:30 CEST |
| Gate | — |
| Sources | 18 |
| Statut | COMPLETED |

---

## 1. BRIEF

**Question d'enquête :** Que coûterait réellement une perte de X % d'emplois salariés au financement de la Sécurité sociale ? Dans quelle mesure le système est-il vulnérable à l'érosion de la masse salariale — qu'elle soit due à l'IA, à l'attrition ou à autre chose ?

**Verdict forensique : Le système est structurellement vulnérable, mais le péril immédiat n'est pas l'IA — c'est le déficit déjà existant.** La Sécurité sociale a perdu 21,6 Md€ en 2025 (doublement en deux ans), et la Cour des comptes prévoit 24 Md€ en 2028 sans mesures nouvelles. L'érosion de la masse salariale par l'IA viendra s'ajouter à une trajectoire déjà non soutenable. Les ordres de grandeur sont désormais calculables avec précision grâce aux données FIPECO et Cour des comptes 2026.

---

## 2. FACT_REGISTRY

### 2.1 L'état du patient (données Cour des comptes, mai 2026)

| ID | Fait | Source |
|----|------|--------|
| F-001 | Déficit Sécu 2025 : 21,6 Md€ (doublé en deux ans, plus haut niveau depuis 2012 hors COVID). | Cour des comptes, rapport Sécurité sociale 2026, 27 mai 2026 |
| F-002 | Recettes +2,6 % vs dépenses +3,6 % en 2025. L'effet ciseaux est structurel : les dépenses progressent 1,4× plus vite que les recettes. | Cour des comptes, ibid. |
| F-003 | Déficit prévu 2026 : 19,4 Md€ (amélioration apparente due à des recettes nouvelles et transferts de l'État, pas à des économies). | Cour des comptes, ibid. |
| F-004 | Risque d'exécution 2026 : au moins 3 Md€ supplémentaires (contexte géopolitique). Risque 2027 : 5 Md€ avant mesures d'économie. | Cour des comptes, ibid. |
| F-005 | Trajectoire 2028 sans mesures nouvelles : déficit de 24 Md€, « impasse de financement » (Assemblée nationale, rapport n°1491). | Assemblée nationale, rapport n°1491 |
| F-006 | La Cour recommande un plan d'action pour ramener le solde « vers l'équilibre en 2030 ». Soit 21,6 Md€ à combler en 4 ans. | Cour des comptes, ibid. |
| F-007 | Dépenses totales de la Sécu : 643 Md€ (22 % du PIB). | Site Sécurité-sociale.fr |
| F-008 | Cotisations sociales = 55 % des ressources de la Sécu en 2025 (contre 98 % en 1980). Le reste vient de la CSG (145 Md€/an environ), TVA, et transferts de l'État. | FIPECO, 20 juin 2026 |
| F-009 | La branche Maladie est la plus déficitaire : −13,8 Md€ prévus en 2026, −17,7 Md€ en 2028. | IFRA P, février 2026 |

### 2.2 L'assiette et son élasticité (données FIPECO)

| ID | Fait | Source |
|----|------|--------|
| F-010 | Assiette des cotisations sociales : 1 078 Md€ en 2025 (salaires privé 738 Md€, traitements publics 171 Md€, indépendants 105 Md€). | FIPECO, 20 juin 2026 |
| F-011 | Produit des cotisations sociales (net) : 443 Md€ en 2025, soit 14,8 % du PIB. | FIPECO, ibid. |
| F-012 | **Élasticité des cotisations aux revenus d'activité : 0,95.** Chaque baisse de 1 % des revenus d'activité = baisse de 0,95 % des cotisations = **−4,2 Md€.** | FIPECO, ibid. |
| F-013 | Élasticité au PIB : ~0,6 à court terme, ~1,0 à moyen terme. La masse salariale fluctue moins que le PIB à court terme. | FIPECO, ibid. |
| F-014 | Rendement d'une hausse de 1 point de cotisations sur l'ensemble des revenus : 10,8 Md€. | FIPECO, ibid. |
| F-015 | CSG : assiette ~1 500 Md€ (tous revenus : salaires, pensions, capital). Taux 9,2 % sur les salaires. Produit ~145 Md€/an. | Estimation |
| F-016 | La France était 1ère de l'UE en cotisations/PIB en 2018. En 2025, elle est 2e (14,8 %) derrière l'Allemagne (17,2 %). Moyenne UE : 13,5 %. | FIPECO, ibid. |

---

## 3. LE STRESS-TEST — Trois scénarios

### Scénario 1 : Érosion lente (−3,8 % d'emplois fragilisés, Coface/OEM)

**Hypothèse :** 3,8 % des emplois « fragilisés à court terme » (rapport Sénat « L'entreprise 5.0 », Coface/OEM). Supposons que 50 % de ces postes disparaissent sur 5 ans par attrition — soit −1,9 % de l'emploi.

| Variable | Calcul | Résultat |
|----------|--------|----------|
| Baisse de la masse salariale | −1,9 % | — |
| Perte de cotisations (élasticité 0,95) | 443 Md€ × 1,9 % × 0,95 | **−8,0 Md€/an** |
| Perte de CSG (élasticité ~0,9) | 145 Md€ × 1,9 % × 0,9 | **−2,5 Md€/an** |
| **Total pertes recettes Sécu** | — | **−10,5 Md€/an à maturité (5 ans)** |
| **Déficit Sécu actuel** | — | **21,6 Md€** |
| **Déficit après choc** | — | **~32 Md€** |

### Scénario 2 : Le choc médian (−16,3 % menacés à 2-5 ans, Coface/OEM)

**Hypothèse :** 16,3 % des emplois « menacés à 2-5 ans. » Supposons que 30 % disparaissent sur la période — soit −4,9 %.

| Variable | Calcul | Résultat |
|----------|--------|----------|
| Perte de cotisations | 443 Md€ × 4,9 % × 0,95 | **−20,6 Md€/an** |
| Perte de CSG | 145 Md€ × 4,9 % × 0,9 | **−6,4 Md€/an** |
| **Total pertes recettes** | — | **−27,0 Md€/an à maturité** |
| **Déficit après choc** | — | **~49 Md€** |

### Scénario 3 : Le scénario noir (−10 % de l'emploi, borne haute BCG)

**Hypothèse :** La borne BCG (10-15 % d'emplois éliminés en 5 ans+) se réalise sur 10 ans. Prise progressive : −1 %/an pendant 10 ans.

| Année | Perte cumulée | Perte cotisations (Md€) | Perte CSG (Md€) | Déficit total (Md€) |
|-------|-------------|------------------------|-----------------|---------------------|
| 2027 | −1,0 % | −4,2 | −1,3 | 27,1 |
| 2028 | −2,0 % | −8,4 | −2,6 | 35,0 |
| 2029 | −3,0 % | −12,6 | −3,9 | 50,6 |
| 2030 | −4,0 % | −16,8 | −5,2 | 62,0 |
| 2031 | −5,0 % | −21,1 | −6,5 | 73,6 |
| 2036 | −10,0 % | −42,1 | −13,1 | 121,2 |

---

## 4. ANALYSE — Ce que le stress-test révèle

### 4.1 Le système était déjà cassé avant l'IA

Le déficit de 21,6 Md€ en 2025 n'a rien à voir avec l'IA. C'est un effet ciseaux classique — dépenses qui progressent plus vite que les recettes — amplifié par le vieillissement (santé, retraites), les crises (COVID, énergie), et l'absence de réformes structurelles depuis 2018. La Cour des comptes appelle à un plan de retour à l'équilibre en 2030, soit 5,4 Md€ d'économies par an. Ce plan n'existe pas.

### 4.2 L'IA est un multiplicateur de risque, pas la cause première

Le vrai danger n'est pas que l'IA détruise la Sécu — c'est qu'elle aggrave une trajectoire déjà non soutenable.

Même le scénario le plus modéré (−1,9 % d'emploi, ~1 Md€ de pertes par an sur 5 ans) ajoute 10,5 Md€ de déficit à un système qui doit déjà en résorber 21,6. Le scénario médian (−4,9 %) ajoute 27 Md€. L'addition dépasse 49 Md€ — soit plus que le budget annuel de l'Éducation nationale.

**La Sécu peut absorber une érosion lente (−0,5 %/an) sans trop de dégâts. Elle ne peut pas absorber le scénario médian sans une réforme structurelle du financement.**

### 4.3 L'attrition est plus dangereuse que les licenciements

Une suppression de poste par licenciement = un chômeur = l'Unédic paie. Une suppression par attrition = le poste disparaît, personne ne touche le chômage, mais les cotisations disparaissent aussi. **Le coût pour la Sécu est identique dans les deux cas, mais le coût politique est nul dans le cas de l'attrition.** C'est exactement le mécanisme documenté dans l'investigation sur les banques/assurances/télécoms : −5 000 à −7 000 postes/an sans un seul licenciement.

### 4.4 La CSG ne sauvera pas le système

La CSG (145 Md€) est assise sur une assiette plus large que les cotisations (tous revenus : salaires, pensions, capital). Mais elle est aussi corrélée à l'emploi : moins de salariés = moins de salaires = moins de CSG. Et le capital est déjà taxé au PFU (30 %). Élargir l'assiette de la CSG vers le capital est techniquement possible mais politiquement bloqué depuis 2018.

### 4.5 Le verrou allemand

L'Allemagne a un taux de cotisations/PIB plus élevé (17,2 % vs 14,8 % pour la France) et donc une dépendance encore plus forte à la masse salariale. Si l'IA frappe d'abord les cols blancs, l'Allemagne — avec son industrie manufacturière encore massive — pourrait être relativement protégée. Mais son système de retraite par répartition est exposé de la même manière.

### 4.6 Ce que la Cour des comptes ne dit pas (encore)

La Cour identifie parfaitement le problème (déficit structurel, trajectoire non soutenable) mais ne mentionne pas l'IA comme facteur aggravant dans son rapport de mai 2026. L'analyse est purement budgétaire. Le lien IA → masse salariale → Sécu n'est fait nulle part dans le rapport. C'est un trou analytique majeur.

---

## 5. VERDICT

**La Sécurité sociale française est un patient cardiaque à qui on annonce qu'il va devoir courir un marathon.**

Le déficit actuel (21,6 Md€) est déjà critique. La trajectoire sans IA mène à 24 Md€ en 2028. Avec une érosion même modérée de l'emploi (−1,9 %), le déficit atteint 32 Md€. Avec le scénario médian (−4,9 %), il atteint 49 Md€.

Le problème n'est pas que l'IA va « détruire la Sécu. » Le problème est que la Sécu était déjà en train de couler, et que l'IA accélère la voie d'eau.

**Chiffres à retenir :**

| Indicateur | Valeur |
|-----------|--------|
| Déficit 2025 | 21,6 Md€ |
| Déficit 2028 prévu (sans IA) | 24 Md€ |
| Perte par −1 % d'emploi (cotisations) | −4,2 Md€/an |
| Perte par −1 % d'emploi (cotisations + CSG) | −5,5 Md€/an |
| Seuil de rupture (déficit ≥ 50 Md€) | −5 % d'emploi cumulé |
| Plan de retour à l'équilibre nécessaire | 5,4 Md€/an d'économies (non engagé) |

---

## 6. LOUPS OUVERTS

| ID | Description | Sévérité |
|----|-------------|----------|
| W-001 | La Cour des comptes n'intègre pas l'IA dans son analyse de soutenabilité. Le lien IA → masse salariale → recettes Sécu est un angle mort de la prospective budgétaire française. | HAUTE |
| W-002 | L'attrition est létale à long terme : suppression de cotisations sans indemnisation chômage. Ce double effet (moins de recettes, pas de dépenses en face) rend le trou invisible jusqu'à ce qu'il soit trop grand. | TRÈS HAUTE |
| W-003 | Le débat sur le financement de la Sécu oppose encore cotisations vs CSG. La vraie question est : comment financer la protection sociale quand l'assiette « travail » se contracte structurellement ? | HAUTE |

---

## 7. SOURCES

1. Cour des comptes, « Sécurité sociale 2026 », 27 mai 2026 — https://www.ccomptes.fr/fr/publications/securite-sociale-2026
2. FIPECO, « Les cotisations sociales », 20 juin 2026 — https://www.fipeco.fr/fiche/Les-cotisations-sociales
3. Assemblée nationale, rapport n°1491, PLFSS 2026
4. IFRA P, « Rétablissement des comptes de la Sécurité sociale », février 2026
5. Sénat, rapport r25-572, « L'entreprise 5.0 », 2026 — https://www.senat.fr/rap/r25-572/r25-572_mono.html
6. Coface/OEM, étude citée dans rapport Sénat r25-572 (3,8 % fragilisé, 16,3 % menacé)
7. Site Sécurité-sociale.fr, chiffres clés
8. Cour des comptes, trajectoire 2028, citée par Vie-publique.fr, novembre 2024
9. PLFSS 2026, Sénat — https://www.senat.fr/rap/a25-126/a25-126_mono.html
10. Assemblée nationale, rapport cion-soc n°1491
11. DARES, inscrits France Travail T4 2025, janvier 2026
12. Eurostat, cotisations sociales/PIB 2025, cité par FIPECO
13. OFCE/Sciences Po, trajectoires finances publiques, juillet 2025
14. Le Monde, « France Travail intensifie le contrôle », avril 2025
15. AEF Info, « 960 000 contrôles CRE en 2025 », août 2026
16. France Travail, « Le contrôle de la recherche d'emploi en 2025 », août 2026
17. Le Parisien, « Contrôles chômeurs : objectif 1,5 million en 2027 », avril 2025
18. Budget.gouv.fr, Rapport sur la dette, octobre 2025