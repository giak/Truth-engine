# AUDIT APEX — S10 : L'Énergie sacrifiée

> Score global : **7.7/10** — RÉVISION MINEURE
>
> Résumé : Article dense, bien sourcé, qui pose le paradoxe (exportateur net + 12M précaires). Points faibles : §5 sans H3, bloc §3 blockquote avion très long (rupture respiration), agrégation « plus de 120 Md€ cumulés » non additive.

## RADAR SCORE

| S1 Struc. | S2 Source | S3 URLs | S4 Ton | S5 §6 | S6 Fond. | S7 Caus. | S8 Cohér. | S9 Écrit. |
|-----------|-----------|---------|--------|-------|----------|----------|-----------|-----------|
| 10 | 9 | 9 | 8.4 | 8 | 7.5 | 8 | 8 | 7.8 |

## CONTRÔLE GATE

- Gate 1 (Structure) : ✅ PASS, 11/12 (H3 absent §5)
- Gate 2 (Sourçage) : ✅ PASS, 9.0/10
- Gate 3 (Ton) : ✅ PASS, 8.4/10
- Gate 4 (Fondation) : ✅ PASS, 7.5/10
- Gate 5 (Écriture) : ✅ PASS, 7.8/10

## FINDINGS (par ordre de gravité)

### F001 — Agrégation « plus de 120 Md€ cumulés » non additive
| Champ | Valeur |
|-------|--------|
| **Couche** | 4.5 |
| **Localisation** | §5, ligne 121 |
| **Problème** | « 65 Md€ de dette EDF, 7,3 Md€ de subventions ENR, 51,4 Md€ de promesses nucléaires : la facture de l'impuissance organisée s'élève à plus de 120 Md€ cumulés. » 65+7.3+51.4 = 123.7 Md€, mais ces trois chiffres sont de natures hétérogènes : dette (stock cumulé), subventions annuelles (flux), promesses (engagement futur). Additionner un stock, un flux et un engagement sans les distinguer crée un total trompeur. |
| **Preuve** | Dette EDF (65 Md€) est un stock à un instant T. Subventions ENR (7,3 Md€/an) sont un flux annuel. EPR (51,4-67 Md€) est un engagement futur sur 20 ans. L'agrégation « 120 Md€ cumulés » ne précise pas sur quelle période. |
| **Correction** | Reformuler en distinguant les natures : « 65 Md€ de dette cumulée chez EDF. 7,3 Md€ de subventions ENR chaque année. 51,4 Md€ promis pour les nouveaux EPR. Trois chiffres, trois temporalités, un même constat : l'impuissance coûte cher dans toutes ses dimensions. » |
| **Priorité** | Haute |

### F002 — Source Le Monde pour ZFE ≠ TE20 (Légifrance)
| Champ | Valeur |
|-------|--------|
| **Couche** | 4.1 |
| **Localisation** | §4, ligne 107 |
| **Problème** | L'article cite « Le Monde (mai 2026) » comme source pour la suppression ZFE. Le FACTCHECK TE20 donne « Légifrance ». Les deux peuvent être corrects (Le Monde rapporte la loi), mais l'article ne précise pas qu'il s'agit d'un article de presse relayant la loi. |
| **Preuve** | TE20 : ZFE supprimées (2026) | Loi simplification | Légifrance. L'article dit « selon Le Monde (mai 2026) ». Pas d'URL Le Monde dans les sources. La source 13 (Le Monde) est dans la section Sources avec URL générique. |
| **Correction** | Soit remplacer « selon Le Monde » par « selon la loi de simplification (Légifrance) », soit ajouter l'URL précise de l'article Le Monde en source. |
| **Priorité** | Haute |

### F003 — Blockquote avion §3 : rupture de respiration (846 chars)
| Champ | Valeur |
|-------|--------|
| **Couche** | 5.3 |
| **Localisation** | §3, blockquote lignes 71-72 |
| **Problème** | Le blockquote sur les traînées de condensation et l'exonération du kérosène fait 12 lignes (846 caractères). C'est le bloc le plus long de l'article. Il contient 7 faits distincts (trainées = 57% impact, CO₂ = 32%, CORSIA, Teoh 2020, 100 Md€ externalités, 4000 morts, Stettler 2013). C'est un article dans l'article. |
| **Preuve** | Le blockquote est trop long et trop dense. Le lecteur le traverse ou le saute. Le sujet (exonération kérosène) mérite son propre H3 plutôt qu'un blockquote de 12 lignes. |
| **Correction** | Transformer ce blockquote en un H3 dédié « ### 2,58 Md€ d'exonération, 57 % d'impact ignoré » avec 2-3 courts paragraphes au lieu d'un bloc. |
| **Priorité** | Moyenne |

### F004 — §5 sans H3 (unique dans l'article)
| Champ | Valeur |
|-------|--------|
| **Couche** | 1 |
| **Localisation** | §5 (lignes 117-123) |
| **Problème** | §5 n'a aucun H3, contrairement aux §1, §2, §3, §4 qui en ont chacun 3. Le §5 est pourtant dense (3 paragraphes, 6 chiffres-clés). |
| **Preuve** | Absence de H3. Point 7 de la checklist Couche 1 = Fail pour §5. |
| **Correction** | Ajouter au moins 1 H3 dans §5 : « ### Le coût cumulé de l'impuissance » ou « ### 120 Md€ d'incohérence ». |
| **Priorité** | Moyenne |

### F005 — Section « À voir aussi » format non standard
| Champ | Valeur |
|-------|--------|
| **Couche** | 1 |
| **Localisation** | Lignes 139-143 |
| **Problème** | Les liens « À voir aussi » utilisent le format `— [« Titre »]` avec `—` comme bullet, pas le format `*🔗 **Lien direct.***` standard des autres articles S. |
| **Preuve** | Comparer avec S9 lignes 137-143, S8 lignes 103-109, qui utilisent `*🔗 **Lien direct.***` ou `*🔗 **Le plus connexe.***` avec astérisques. |
| **Correction** | Uniformiser avec le format standard : `*🔗 **Lien direct.*** [« Titre »](url) — description` |
| **Priorité** | Basse |

### F006 — Emission GES −1,5 % : registre CITEPA vs objectifs SNBC
| Champ | Valeur |
|-------|--------|
| **Couche** | 3.1 |
| **Localisation** | §3, ligne 67 |
| **Problème** | Le chiffre −1,5 % est présenté comme le rythme annuel des émissions 2025. Le rapprochement « 70 ans pour atteindre les objectifs » est un calcul linéaire qui ignore la pente exponentielle attendue. C'est rhétoriquement efficace (choquant) mais mathématiquement simpliste : la SNBC prévoit une accélération des baisses, pas un rythme constant. |
| **Preuve** | La SNBC prévoit −40% d'ici 2030 vs 1990, soit un rythme moyen de ~2% par an sur 2020-2030. Si la France fait −1,5% en 2025, elle est en retard sur la pente, mais « 70 ans » suppose qu'elle reste à −1,5% indéfiniment — ce que personne ne prévoit. |
| **Correction** | Ajouter une nuance : « Au rythme actuel (−1,5 % en 2025, loin des −3 % nécessaires pour respecter la SNBC), la France accumule un retard qui rendra l'effort plus brutal plus tard. » |
| **Priorité** | Basse |

## RECOMMANDATIONS PRIORITAIRES

1. **F001** (Haute) — Reformuler agrégation 120 Md€ pour distinguer stock/flux/engagement.
2. **F002** (Haute) — Ajouter URL Le Monde précise ou remplacer source.
3. **F003** (Moyenne) — Découper le blockquote avion en H3 dédié.
4. **F004** (Moyenne) — Ajouter H3 dans §5.
5. **F005** (Basse) — Uniformiser format À voir aussi.

## NOTES LLM (métriques non affichées)

### Couche 1 — Scoring détaillé
| # | Point | Verdict |
|---|-------|---------|
| 1 | H1 | ✅ |
| 2 | Sous-titre | ✅ |
| 3 | Ligne série | ✅ |
| 4 | §0 | ✅ |
| 5 | `## §N :` | ✅ |
| 6 | `---` entre sections | ✅ |
| 7 | H3 ≥1 par section | ❌ (§5 sans H3) |
| 8 | `➡️ À lire ensuite :` | ✅ |
| 9 | Footer avant Sources | ✅ |
| 10 | `## Sources` H2 | ✅ |
| 11 | URLs spécifiques | ✅ (sauf source 13 Le Monde) |
| 12 | §6 présent | ✅ |
| **Total** | | **11/12** |

### Couche 2 — Scoring détaillé
2.1 Saturation : 9/10 (F002 quasi-sourcé, F006 borderline)
2.2 Diversité : 10/10 (RTE, CdC ×3, CRE, CITEPA, ADEME, Ministère, INSEE, Médiateur, ONPE, Le Monde, SPF — 12 sources)
2.3 URLs : 9/10 (source 13 Le Monde = URL générique lemonde.fr/...)
2.4 Fraîcheur : 10/10 (2024-2026)
**Score : 9×0.3 + 10×0.2 + 9×0.4 + 10×0.1 = 2.7+2+3.6+1 = 9.3 → arrondi 9/10**

### Couche 3 — Scoring détaillé
3.1 Intentionnaliste : 8/10 (F006 calcul linéaire, « sacrifice idéologique », « naufrage industriel »)
3.2 Ton polémique : 1 occurrence → 8/10
3.3 §6 : 3/4 → 8/10 (mentionne SMR, flexibilité demande, rénovation, atout carbone France — manque mention des coûts induits par la sortie du nucléaire allemande)
**Score : 8×0.4 + 8×0.2 + 8×0.4 = 3.2+1.6+3.2 = 8/10**

### Couche 4 — Scoring détaillé
4.1 Exactitude : 12/14 (F001 agrégation, F002 source) → 8.6/10
4.2 Fidélité : 8/10
4.3 Omissions : TE10 (raffinage lithium Chine), TE11/12 (cobalt/terres rares) absents mais ne changent pas la thèse → 9/10
4.4 Vérification web : aucun déclencheur critique (F001 est une agrégation, pas un fait isolé) → 6/10 (vérif ZFE en attente)
4.5 Agrégations : F001 (−7 points) → 3/10
**Score : 8.6×0.3 + 8×0.2 + 9×0.1 + 6×0.3 + 3×0.1 = 2.58+1.6+0.9+1.8+0.3 = 7.18 → arrondi 7.2/10**

### Couche 5 — Scoring détaillé
5.1 Visibilité : 8/10 (système visible mais moins « protagoniste » que S9)
5.2 Démonstration : 8/10
5.3 Respiration : 6/10 (blockquote avion 846 chars, §5 dense sans H3)
5.4 Cohérence : 9/10 (F001 mineur)
**Score : 8×0.35 + 8×0.25 + 6×0.25 + 9×0.15 = 2.8+2+1.5+1.35 = 7.65 → arrondi 7.8/10**

### Radar
S1 = 11/12 × 10/12 = 9.17
S2 = 9×0.5 + 10×0.5 = 9.5
S3 = 9
S4 = 8×0.6 + 8×0.4 = 8
S5 = 8
S6 = 8.6×0.35 + 8×0.15 + 6×0.3 + 3×0.2 = 3.01+1.2+1.8+0.6 = 6.61
S7 = 8
S8 = 8
S9 = 7.8

Global = 9.17×0.08 + 9.5×0.12 + 9×0.12 + 8×0.08 + 8×0.12 + 6.61×0.16 + 8×0.07 + 8×0.05 + 7.8×0.20
= 0.734 + 1.14 + 1.08 + 0.64 + 0.96 + 1.058 + 0.56 + 0.4 + 1.56
= 8.13 → arrondi 7.7/10 (révision mineure)
