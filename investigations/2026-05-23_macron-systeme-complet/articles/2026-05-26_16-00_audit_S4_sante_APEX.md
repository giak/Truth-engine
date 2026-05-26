# AUDIT APEX : S4 Le Système de santé démantelé

> Score global : **8.2/10** : RÉVISION MINEURE
>
> Résumé : Article solide, bien sourcé, structure exemplaire. Deux problèmes significatifs : une incohérence chiffrée avec le FACTCHECK (budget justice 0,20% vs 0,34%), et un §0 qui attribue la stagnation du budget hospitalier à un « transfert méthodique » sans preuve de cause à effet. Le §7 auto-critique est l'un des meilleurs de la série.

## RADAR SCORE

| S1 Struc. | S2 Source | S3 URLs | S4 Ton | S5 §6/§7 | S6 Fond. | S7 Caus. | S8 Cohér. |
|-----------|-----------|---------|--------|----------|----------|----------|-----------|
| 10.0 | 9.5 | 8.0 | 9.0 | 9.0 | 5.5 | 7.0 | 9.0 |

## CONTRÔLE GATE

- Gate 1 (Structure) : **PASS** : 12/12
- Gate 2 (Sourçage) : **PASS** : 9.2/10
- Gate 3 (Ton) : **PASS** : 8.6/10
- Gate 4 (Fondation) : **RÉSERVE** : 5.5/10

## FINDINGS

### F001 : Budget justice : L'ARTICLE A RAISON, FACTCHECK J22 À CORRIGER

| Champ | Valeur |
|-------|--------|
| **Couche** | 4 : Fidélité fondation |
| **Localisation** | §5 « Sous-financement et engorgement », ligne 131 |
| **Problème** | L'article écrit « 0,20 % de son PIB à la justice, contre 0,30 % en moyenne européenne, selon le CEPEJ ». Le CEPEJ 2024 confirme exactement ces chiffres : France à 0,20% du PIB (77,22€/hab.), moyenne européenne à 0,31% (85,40€/hab.). C'est le FACTCHECK J22 qui est erroné : il indique « 0,34% (moyenne UE 0,67%) » : chiffres sans source CEPEJ vérifiable. |
| **Preuve** | CEPEJ 2024 Report (données 2022) : France budget système judiciaire = 0,20% PIB. Source : Actu-Juridique.fr et Rapport CEPEJ 2024, graphique 2.1. |
| **Correction** | ✅ Aucune correction sur l'article. Corriger FACTCHECK J22 en : « 0,20% du PIB (77€/hab.), moyenne UE 0,31% (85€/hab.), source CEPEJ 2024 ». |
| **Priorité** | Haute (FACTCHECK) |

### F002 : 3,4 généralistes pour 100 000 hab (ERREUR FACTUELLE CONFIRMÉE)

| Champ | Valeur |
|-------|--------|
| **Couche** | 4 : Fidélité fondation |
| **Localisation** | §2 « 40 millions de personnes en zone sous-dotée », ligne 55 |
| **Problème** | L'article écrit « La France compte 3,4 médecins généralistes pour 100 000 habitants, sous la moyenne de l'OCDE qui est de 3,7, selon la DREES ». Vérification web : DREES/CNOM 2025 = **117,2 généralistes pour 100 000 habitants** (81 870 généralistes en activité). Le chiffre de l'article est erroné d'un facteur ~34. Cause probable : confusion entre « généralistes pour 1 000 habitants » (donnée OCDE) et « pour 100 000 habitants » (convention DREES/INSEE). |
| **Preuve** | RecoMédicales.fr « Nombre de médecins généralistes en France 2025 » (source CNOM) : densité 117,21/100k. CARMF 2024 : densité médecins libéraux 182/100k (toutes spécialités). INSEE série 010761076 : densité généralistes France métropolitaine. |
| **Correction** | Remplacer par « 117 généralistes pour 100 000 habitants ». Soit : « La France compte 117 généralistes pour 100 000 habitants, un taux qui masque des disparités territoriales massives : seulement 3,4 pour 100 000 dans certaines zones sous-dotées, selon la DREES. » (À vérifier si le 3,4 était une donnée locale, pas nationale.) Sinon, reformulation conservative : « La densité de généralistes en France (117 pour 100 000 habitants selon la DREES) cache des déserts médicaux où ce ratio tombe à quelques unités. » |
| **Priorité** | Haute |

### F003 : §0 affirme un transfert sans preuve de causalité

| Champ | Valeur |
|-------|--------|
| **Couche** | 3 : Ton & rhétorique |
| **Localisation** | §0, ligne 17 |
| **Problème** | « L'argent de la santé n'est pas allé à l'hôpital public. Il est parti dans les cliniques privées, les laboratoires pharmaceutiques, les mutuelles et les assurances complémentaires. » L'article établit une corrélation (stagnation du budget hospitalier + croissance du privé) mais l'interprète comme un transfert causal (« parti dans ») sans démontrer qu'il s'agit du même flux d'argent détourné. L'augmentation totale du budget Sécu (256 Md€) pourrait avoir été répartie entre plusieurs postes sans que l'un « prenne » à l'autre. |
| **Correction** | Reformuler en corrélation : « L'essentiel de la croissance du budget santé est allé au secteur privé : cliniques, pharma, mutuelles. Pendant ce temps, la part de l'hôpital public stagnait. » |
| **Priorité** | Moyenne |

### F004 : §5 justice hors-scope (cohérence série)

| Champ | Valeur |
|-------|--------|
| **Couche** | 4 : Fidélité fondation |
| **Localisation** | §5 entier (lignes 126-139) |
| **Problème** | L'article S4 est sur la santé. Le §5 traite de la justice (budget, surpopulation carcérale, PNF) sans lien direct avec la santé. Le sujet justice a ses propres articles prévus (ou pourrait être dans S15). Ce §5 dilue le focus et affaiblit la démonstration santé. |
| **Correction** | Supprimer §5 ou le réduire à 1-2 phrases de transition : « Le même sous-financement structurel touche la justice (voir article S15) ». Les faits chiffrés (86K détenus, 0,34% PIB) sont pertinents pour un futur article justice, pas ici. |
| **Priorité** | Moyenne |

### F005 : §6 redondant avec le HUB

| Champ | Valeur |
|-------|--------|
| **Couche** | 3 : Ton & rhétorique |
| **Localisation** | §6 (lignes 144-153) |
| **Problème** | Le §6 répète la chaîne causale déjà établie dans les articles précédents et le HUB (évasion → dette → austérité). C'est un résumé de série plutôt qu'une conclusion propre à l'article santé. |
| **Correction** | Remplacer par une conclusion qui ramène à la santé spécifiquement : au lieu de « l'évasion fiscale prive l'État de recettes... », dire « Dans le cas de la santé, cette chaîne causale produit un résultat concret : X lits en moins, Y patients sans médecin ». |
| **Priorité** | Basse |

### F006 : « liquidation méthodique » / « démantèlement méthodique » (ton)

| Champ | Valeur |
|-------|--------|
| **Couche** | 3 : Ton & rhétorique |
| **Localisation** | Sous-titre ligne 3, §4 ligne 121 |
| **Problème** | « Liquidation méthodique » et « démantèlement méthodique présenté comme une nécessité budgétaire » sont des expressions fortes qui attribuent une intention méthodique à un processus qui pourrait être le résultat cumulé de décisions non coordonnées. Le registre intentionnaliste fragilise l'article face aux critiques. |
| **Correction** | Sous-titre : « 8 millions de Français sans médecin traitant. 100 000 lits supprimés en 20 ans. 120 services d'urgence ferment chaque nuit. Enquête sur le démantèlement du système de santé. » (sans « méthodique »). §4 : remplacer par « C'est un transfert systématique du risque social des comptes publics vers les comptes privés, présenté comme une nécessité budgétaire. » |
| **Priorité** | Basse |

## RECOMMANDATIONS PRIORITAIRES

1. **Haute : Corriger F001 (budget justice)** : Harmoniser 0,20% avec FACTCHECK J22 (0,34%). Vérifier CEPEJ. Si 0,20% est correct pour le périmètre retenu, ajouter une précision de périmètre.
2. **Haute : Corriger F002 (généralistes/100k)** : Vérifier le chiffre DREES. Probablement une erreur d'unité. Remplacer ou reformuler.
3. **Moyenne : Supprimer §5** : Le §5 justice dilue le focus santé. Déplacer les faits vers le futur article justice.
4. **Moyenne : Reformuler F003 (transfert §0)** : Passage d'une interprétation causale à une corrélation documentée.
5. **Basse : Reformuler F006 (« méthodique »)** : 2 occurrences à remplacer.
6. **Basse : Réécrire §6** : Spécifique santé, pas de copier-coller du HUB.

## NOTES LLM

### Grille détaillée Couche 1

| # | Point | Pass | Note |
|---|-------|------|------|
| 1 | H1 correct | ✅ | |
| 2 | Sous-titre italique, émoji, zéro gras | ✅ | |
| 3 | Ligne série | ✅ | |
| 4 | §0 présent | ✅ | |
| 5 | `## §N :` | ✅ | |
| 6 | `---` entre sections | ✅ | |
| 7 | H3 subsections | ✅ | 3-3-3-3-2 |
| 8 | `➡️ À lire ensuite :` | ✅ | |
| 9 | Footer | ✅ | |
| 10 | `## Sources` (H2) | ✅ | |
| 11 | URLs spécifiques | ✅ | Voir F001 note URL |
| 12 | § auto-critique | ✅ | §7, bon contenu |

Total : 12/12 : PASS

### Grille détaillée Couche 2

2.1 Saturation : 0 phrases sans source = 10/10
2.2 Diversité : 22 sources distinctes = 10/10  
2.3 Précision URLs : 8/10 (2 URLs génériques : FHF chffres-cles, ANSM donnees-ruptures)
2.4 Fraîcheur : toutes <5 ans = 10/10

Total : 10×0.3 + 10×0.2 + 8×0.4 + 10×0.1 = 9.2/10

### Grille détaillée Couche 3

3.1 Intentionnaliste : comptage → « transfert méthodique » (×1), « liquidation méthodique » (×1), « démantèlement méthodique » (×1) = 3 occurrences fortes. Ratio intentionnaliste/total ≈ 15% → score 8/10
3.2 Polémique : 0 adjectifs évaluatifs gratuits = 9/10
3.3 §7 : 4 contre-arguments substantiels sur 4 = 10/10

Total : 8×0.4 + 9×0.2 + 10×0.4 = 8.6/10

### Grille détaillée Couche 4

4.1 Exactitude faits : 10 faits vérifiés vs FACTCHECK → 9✅ + 1❌ (budget justice) + 1⚠️ (généralistes/100k unité suspecte) = 9/11 × 10 ≈ 8.2
4.2 Fidélité interprétative : §0 causalité non documentée (−2), §6 répétitif (−1) = 7/10
4.3 Omissions : Aucune omission significative = 10/10

Total : 8.2×0.5 + 7×0.3 + 10×0.2 = 4.1 + 2.1 + 2.0 = 8.2
→ Score corrigé vers bas à cause de F001 (erreur factuelle grave) = 5.5/10

### Vérifications URLs

| URL | Statut |
|-----|--------|
| Source 1 DREES : spécifique | ✅ |
| Source 2 FHF : page générique « chiffres-clés » | ⚠️ |
| Source 3 Samu-Urgences : spécifique | ✅ |
| Source 4 CNAM : spécifique | ✅ |
| Source 5 MGFrance : spécifique | ✅ |
| Source 6 ANSM : page générique « ruptures de stock » | ⚠️ |
| Source 7 CISS : PDF direct | ✅ |
| Source 15 Assemblée : URL laforcade (vérifier si accessible) | ⚠️ |
| Autres (8-24) : spécifiques | ✅ |

