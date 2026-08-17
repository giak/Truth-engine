# CARTOGRAPHIE DU PANTOUFLAGE HATVP : Ministère × Secteur

- STATE : FINAL
- DATE : 2026-08-11_23-45 CEST
- TYPE : INVESTIGATION (KERNEL v2.8, format allégé)
- PARENT : REGISTRE ICEBERG MAX `2026-08-11_23-14_iceberg-max_REGISTRE.md`
- SOURCES : 773 PDFs HATVP (2014-2026) + registre lobbys JSON (4065 entrées) + data.gouv.fr HATVP

---

## 1. ÉTAT DES DONNÉES HATVP

### Ce qui existe

| Dataset | Format | Accès | Contenu |
|---|---|---|---|
| Avis de mobilité | PDFs individuels (in extenso ou résumé) | hatvp.fr/consulter-les-deliberations-et-avis | 698 avis identifiés 2020-2026 dans /tmp/vp44_txt (sur 773 fichiers, incluant délibérations non-mobilité) |
| Registre des représentants d'intérêts | JSON (137 MB) | data.gouv.fr + hatvp.fr/agora/opendata | 3 989 entités uniques, 4 065 publications |
| Déclarations d'intérêts/patrimoine | XML | data.gouv.fr | Déclarations des responsables publics |
| Statistiques agrégées | Rapports annuels PDF | hatvp.fr | 639 avis en 2024, 641 en 2025, 4,5% incompatibilités |

### Ce qui N'EXISTE PAS

- **Pas de base structurée des avis de mobilité** : pas de CSV, pas d'API, pas de tableau croisé origine × destination
- **Pas de noms dans 95% des avis publiés** : la plupart des PDFs sont des résumés anonymisés. Seuls ~165 avis 2024 sont publiés in extenso avec noms
- **Pas de données 2014-2019** : la compétence mobilité HATVP date du 01/02/2020 (avant : Commission de déontologie, avis jamais publiés)

---

## 2. DISTRIBUTION DES AVIS DE MOBILITÉ (698 avis 2020-2026)

### Par année

| Année | Nombre |
|---|---|
| 2020 | 21 |
| 2021 | 24 |
| 2022 | 42 |
| 2023 | 120 |
| 2024 | 197 |
| 2025 | 233 |
| 2026 | 51 (partiel) |

**Tendance :** explosion post-2022 (+458% entre 2022 et 2025), liée à l'élargissement de la publication décidé par le collège HATVP le 07/02/2023.

### Par type d'avis

| Type | Nombre | % |
|---|---|---|
| COMPATIBILITÉ | 577 | 82,7% |
| COMPATIBILITÉ AVEC RÉSERVES | 75 | 10,7% |
| AUTRE | 34 | 4,9% |
| INCOMPATIBILITÉ | 2 | 0,3% |

**Note :** la ventilation diffère des statistiques agrégées (4,5% incompatibilités selon rapport 2024) car la publication est sélective — les incompatibilités sont sur-représentées par rapport au total réel (seulement 6,5% à 25% des avis sont publiés).

### Par destination sectorielle (depuis les keywords explicites)

| Secteur | Nombre | % |
|---|---|---|
| Conseil/Consulting | 121 | 17,3% |
| Médias | 78 | 11,2% |
| Numérique/Tech | 57 | 8,2% |
| Énergie | 48 | 6,9% |
| Commerce/Distribution | 36 | 5,2% |
| BTP/Immobilier | 13 | 1,9% |
| Télécoms | 10 | 1,4% |
| Fonds d'investissement | 8 | 1,1% |
| Assurance | 6 | 0,9% |
| Transport | 5 | 0,7% |
| Pharma/Santé | 4 | 0,6% |
| Eau | 4 | 0,6% |
| Banque | 1 | 0,1% |
| Défense/Armement | 1 | 0,1% |
| Non identifié | 296 | 42,4% |

**⚠️ Limite :** 42,4% des destinations non identifiées dans les 3000 premiers caractères du PDF. La distribution réelle est probablement différente.

---

## 3. REGISTRE DES LOBBIES (3 989 entités)

### Distribution sectorielle (mentions dans les publications)

| Secteur | Entités |
|---|---|
| Finance | 2 736 |
| Conseil | 2 585 |
| Environnement | 2 259 |
| Santé | 1 562 |
| Énergie | 1 516 |
| Construction | 1 313 |
| Agriculture/Agroalimentaire | ~2 578 |
| Numérique | 1 172 |
| Défense | 927 |
| Médias | 763 |
| Banque | 592 |
| Éolien | 103 |
| Solaire | 100 |
| Pharmaceutique | 143 |
| Nucléaire | 160 |

---

## 4. MATRICE CROISÉE ORIGINE × DESTINATION (filtrage keywords 773 PDFs)

| Origine \\ Destination | Énergie | Pharma | Banque | Conseil | Télécoms | Eau | Défense | Médias |
|---|---|---|---|---|---|---|---|---|
| **CRE** | 87 | 76 | 171 | 536 | 12 | 157 | 21 | 207 |
| **Santé** | 4 | 88 | 11 | 72 | 0 | 30 | 1 | 24 |
| **Trésor** | 6 | 1 | 13 | 8 | 1 | 9 | 0 | 1 |
| **Défense** | 3 | 2 | 8 | 19 | 1 | 5 | 24 | 7 |
| **Cabinet** | 57 | 41 | 85 | 253 | 7 | 82 | 6 | 69 |

**⚠️ ALERTE MÉTHODOLOGIQUE :** Les chiffres sont BRUTS et non dédoublonnés. La CRE apparaît dans 616 fichiers mais ce sont majoritairement des mentions dans le texte de réserves (« abstention de toute démarche auprès de la CRE... »), PAS des mobilités réelles CRE → secteur. Les vrais départs de la CRE vers le privé sont de l'ordre de quelques unités par an (Carenco, Bohuon documentés dans le run2-enr).

---

## 5. FAITS ÉTABLIS (FCT-carto)

| # | Fait | Source | Fiabilité |
|---|---|---|---|
| FCT-carto-001 | Le HATVP ne publie PAS de base structurée des avis de mobilité (CSV/API) — uniquement des PDFs individuels sur un moteur de recherche | Investigation 2026-08-09 base HATVP | ◈ ✦ |
| FCT-carto-002 | 698 avis de mobilité publiés 2020-2026 (sur ~3 000+ rendus) ; 42% n'ont pas de destination identifiable dans les premiers 3000 caractères du PDF | Parsing 773 PDFs | ◈ ✧ |
| FCT-carto-003 | La destination #1 est le CONSEIL/CONSULTING (17,3% des avis identifiés) — McKinsey, BCG, Capgemini, etc. | Parsing PDFs | ◈ ✧ |
| FCT-carto-004 | La destination #2 est les MÉDIAS (11,2%) — cohérent avec le constat de 78 avis vers ce secteur | Parsing PDFs | ◈ ✧ |
| FCT-carto-005 | Le registre des représentants d'intérêts compte 3 989 entités uniques en 2026 | JSON HATVP data.gouv.fr | ◈ ✦ |
| FCT-carto-006 | Les secteurs les plus représentés au registre des lobbys : Finance (2 736), Conseil (2 585), Énergie (1 516), Santé (1 562) | JSON HATVP | ◈ ✧ |
| FCT-carto-007 | 103 entités du registre des lobbys mentionnent l'éolien ; 100 le solaire — cohérent avec l'enquête run2-enr | JSON HATVP | ◈ ✧ |
| FCT-carto-008 | La HATVP a rendu 639 avis de mobilité en 2024 et 641 en 2025 ; 4,5% d'incompatibilités | Rapports annuels HATVP | ◈ ✦ |
| FCT-carto-009 | Le taux de publication des avis est passé de 6,5% (2022) à 25% (2023) à ~165 in extenso (2024) — la majorité des avis reste non publiée | Investigation base HATVP | ◈ ✦ |
| FCT-carto-010 | Aucune base de données ne permet de répondre « combien de DG Énergie → ENR » ou « combien de Santé → Pharma » sans parser manuellement tous les PDFs | Constat | ◈ ✦ |

---

## 6. RÉPONSE À LA QUESTION INITIALE

**« Combien de DG Énergie → ENR, combien de Santé → Pharma ? »**

**Réponse : IMPOSSIBLE à quantifier précisément avec les données publiques actuelles.**

1. **Les données ne sont pas structurées** : pas de CSV, pas d'API, pas de filtre par administration d'origine
2. **Les noms sont majoritairement anonymisés** : seuls ~165 avis 2024 sont publiés in extenso avec noms
3. **70-93% des avis ne sont jamais publiés** : une étude exhaustive est structurellement impossible
4. **Les PDFs publiés exigent un parsing manuel** : 698 PDFs, temps estimé ~35 heures

**Estimations minimales à partir du parsing 773 PDFs :**
- Destination Énergie : 48 avis identifiés (6,9% des 698)
- Destination Pharma/Santé : 4 avis identifiés (0,6%)
- Ces chiffres sont des **bornes inférieures** (42% non identifiés)

**Pour le run2-enr (CRE → ENR) :** le parsing identifie 87 croisements CRE+Énergie, mais la quasi-totalité sont des mentions de la CRE dans les réserves, pas des départs réels. Le vrai nombre est probablement inférieur à 5 (Carenco vers Samfi Ingénierie documenté, Bohuon vers Transdev/énergie documenté, + quelques autres non publiés).

---

## 7. RECOMMANDATION

**Pour cartographier le pantouflage de façon exploitable, il faut :**

1. **Parser TOUS les PDFs in extenso** (165 en 2024, estimation ~200 en 2025) — pas seulement les 3000 premiers caractères
2. **Extraire le nom de l'agent, son administration d'origine, l'entreprise de destination, le secteur**
3. **Croiser avec le registre des lobbys** HATVP pour identifier les entités qui embauchent d'anciens régulateurs ET font du lobbying
4. **Utiliser l'API data.gouv.fr** pour les déclarations d'intérêts (XML structuré) comme source complémentaire
5. **Automatiser** : un script Python de parsing PDF + NLP pour extraire les triplets (nom, origine, destination)

**Temps estimé :** 8-12 heures de développement + parsing pour une base exploitable.
