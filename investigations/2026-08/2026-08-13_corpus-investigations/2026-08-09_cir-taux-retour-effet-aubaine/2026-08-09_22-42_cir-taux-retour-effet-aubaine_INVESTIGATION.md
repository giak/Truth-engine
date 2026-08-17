# INVESTIGATION APEX : « LA CJIR DU CIR » (COMPARAISON DU TAUX DE RETOUR DU CRÉDIT D'IMPÔT RECHERCHE) — TAUX DE RETOUR EFFECTIF PAR GROUPE (ANNEXE 12 × R&D PUBLIÉES) ET EFFETS D'AUBAINE

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260809-2242-cir-taux-retour-effet-aubaine
PARENT_RUN_ID  : 20260809-2215-beneficiaires-niches-cessions (GAP-007 : Annexe 12 CIR nominative, FCT-001 à 008)
AS_OF          : 2026-08-09
INPUT_KIND     : UPDATE (croisement de l'Annexe 12 avec les dépenses R&D publiées pour estimer le taux de retour effectif et les effets d'aubaine)
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique : « croiser l'Annexe 12 nominative (8 groupes) avec les résultats R&D publiés pour estimer le taux de retour effectif du CIR par groupe et documenter les effets d'aubaine »)
SUBJECT_SLUG   : cir-taux-retour-effet-aubaine
NOTE_SLUG      : « CJIR » = comparaison du taux de retour (défini au premier emploi)
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cir-taux-retour-effet-aubaine/2026-08-09_22-42_cir-taux-retour-effet-aubaine_INVESTIGATION.md
SCOPE          : taux de retour effectif du CIR par groupe (8 groupes de l'Annexe 12 du Sénat 808) ; comparaison avec le taux théorique (30 %/5 %, seuil 100 M€) ; effets d'aubaine (additionnalité IPP/CNEPI/CdC) ; tension de périmètre entre base Annexe 12 et R&D comptable publié ; période 2019-2026 ; France (+ R&D mondiale des groupes pour comparaison)
COMPLEXITY     : CX_SCORE=13 → $CX=APEX (political 2, technical 2, temporal 3, geo 2, narratives 2, data 2)
CHECKPOINT_SEQ : 0 (run mono-session)
LAST_COMPLETED : 18b
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS | PATTERNS | THREATS | GATES | REQUEST_LOG | EPISTEMIC | TEMPLATE (héritage des runs parents)
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« quel est le taux de retour effectif du CIR par grand groupe, et quelle est la part d'effet d'aubaine ? ») :

**Le taux de retour effectif est calculable sur la base Annexe 12 (ratios publiés 4,32 % à 13,66 %), mais sa comparaison avec les R&D comptables publiées révèle une tension de périmètre qui interdit toute lecture naïve.** Le cœur de l'enquête :

1. **Le taux théorique du CIR pour un grand groupe est ~6,25 %** : 30 % sur la part ≤ 100 M€ + 5 % au-delà (LF 2008, CGI 244 quater B). Pour 2 Md€ de dépenses éligibles : 30 M€ + 95 M€ = 125 M€ = 6,25 % (FCT-001, calcul vérifié par le chercheur).
2. **Les ratios de l'Annexe 12 s'écartent du théorique dans les deux sens** : STMicro 13,66 % (~2× le théorique), Sanofi 4,32 % (sous le théorique), Thales 6,79 %, Safran 7,60 %, Renault 6,70 % (FCT-002 à 006, hérités du 22-15). **L'hétérogénéité des taux est elle-même un fait d'enquête** : plus de trois fois plus élevé pour STMicro que pour Sanofi (13,66/4,32 = 3,16), à périmètre supposé comparable. **Tableau croisé consolidé (objet de l'enquête) :**

| Groupe | CIR (M€) | Base Annexe 12 (M€) | Ratio Annexe | R&D comptable publiée (M€) | Ratio comptable | Écart de base |
|--------|----------|---------------------|--------------|----------------------------|-----------------|---------------|
| STMicro | 119 | 871 | 13,66 % | ~1 900 (2 077 M$) | ~6,3 % | ×2,2 |
| Safran | 152 | 2 000 | 7,60 % | 1 980 (autof. 1 348) | 7,7 % (11,3 % autof.) | ~cohérent |
| Renault | 133,9 | 2 000 | 6,70 % | 4 066 (CAPEX+R&D nets) | 3,3 % | ×0,5 |
| Thales | 171 | 2 520 | 6,79 % | 1 273,7 (compte résultat) | 13,4 % | ×2 |
| Sanofi | 108 | 2 500 | 4,32 % | ~7 400 | 1,5 % | ×0,34 |
| Stellantis | 63,2 | (non publié) | — | ~5 700 | ~1,1 % | — |
| Michelin | 40,4 | (non publié) | — | ~750 | ~5,4 % | — |
| ArcelorMittal | 40 | (non publié) | — | ~300 | ~13,3 % | — |

**Le ratio de retour effectif varie de 1,1 % à 13,66 % selon la base et le groupe — la discordance des bases est la mesure de l'incertitude.**
3. **TENSION DE PÉRIMÈTRE (découverte principale)** : les « dépenses de R&D » de l'Annexe 12 (Thales 2 520 M€, Safran 2 000, Renault 2 000, STMicro 871, Sanofi 2 500) **ne correspondent pas aux R&D comptables publiées 2024** (Thales 1 273,7 M€ au compte de résultat, STMicro 2 077 M$ ≈ 1 900 M€ mondial, Sanofi ~7,4 Md€, Stellantis ~5,7 Md€) (FCT-007 à 011). Deux lectures possibles, non tranchables par sources publiques : (a) l'annexe utilise les dépenses éligibles CIR (périmètre France, plus étroit), (b) elle utilise des données d'années ou de périmètres différents (autofinancé vs total, France vs monde). **Le taux de retour « réel » dépend du choix de base — l'écart entre ratios (Annexe 12) et ratios (R&D comptable) est la mesure de l'incertitude.**
4. **L'effet d'aubaine est documenté par les évaluations officielles, avec une asymétrie taille marquée** : IPP 2019 (Bozio et al.) : 1 € de CIR génère 1,3-1,5 € de R&D supplémentaire (multiplicateur), soit 15-18 % d'effet sur les dépenses ; **IPP n° 33 / CNEPI 06/2021 : effets causals significatifs pour TPE/PME, AUCUN effet causal documenté pour les grandes entreprises** ; rendement brevet : 1,165/M€ pour les TPE vs 0,464/M€ pour les grandes entreprises — **l'effet d'aubaine est prononcé chez les grands groupes** (FCT-012 à 014). Cour des comptes 07/2023 : recommande le recentrage du CIR sur les PME (FCT-015).

**Verdict sur le LEAD_QUESTION** (« le CIR des grands groupes est-il un effet d'aubaine ? ») : **FAISCEAU FORT, NON PROUVÉ INDIVIDUELLEMENT.** Les évaluations institutionnelles (IPP/CNEPI/CdC) convergent : aucun effet causal documenté sur les grandes entreprises → la majeure partie des ~827,5 M€ cumulés des 8 groupes (FCT-016, calcul) serait de la R&D réalisée de toute façon. **Mais l'effet d'aubaine est une inférence statistique agrégée, pas une mesure par groupe** : aucun fait ne démontre qu'un CIR particulier de Thales ou Sanofi était « d'aubaine ». La tension de périmètre (point 3) renforce la prudence : les ratios publiés ne permettent pas de hiérarchiser les groupes en rigueur.

**Acteurs** : 8 groupes (Thales, Safran, Renault, STMicro, Sanofi, Stellantis, Michelin, ArcelorMittal), DGFiP (contrôle), Sénat 808 (divulgation), IPP/CNEPI (évaluation), CdC (recommendations).

**Principales limites** : périmètre exact de l'Annexe 12 non confirmé (source Sénat accessible mais annexe elle-même non isolée — la page r24-808-151 est le sommaire) ; R&D comptables mondiaux vs éligibles France non ventilés ; les ratios Annexe 12 (Thales 6,79 % etc.) sont arithmétiquement vérifiés mais leur base exacte reste à confirmer ; pas d'accès aux déclarations CIR individuelles (secret fiscal).

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

| # | Symbole | Score | Justification (corpus) |
|---|---------|-------|------------------------|
| 1 | **Ξ** omission | **9/10** | La DGFiP ne publie pas les taux de retour par entreprise ; l'Annexe 12 du Sénat est un échantillon d'auditions, sans définition précise du périmètre « dépenses de R&D » ; les déclarations CIR individuelles restent secrètes. |
| 2 | **€** money | **8/10** | CIR 7,6-7,8 Md€/an ; 8 groupes = ~827,5 M€ cumulés ; taux 30 %/5 % ; multiplicateur 1,3-1,5. |
| 3 | **Λ** framing | 7/10 | « Aide à l'innovation » (positif) vs « effet d'aubaine » (négatif) ; « taux de retour » (neutre) vs « rente » ; « recentrer le CIR sur les PME » (CdC) vs « ne pas casser l'innovation » (lobby). |
| 4 | **Ω** inversion | **8/10** | Le CIR est présenté comme « levier d'innovation » alors que les évaluations montrent qu'il ne stimule que les PME ; les grands groupes « déclarent » des R&D qui existaient de toute façon ; la « transparence » de l'annexe 12 coexiste avec un périmètre indéfini. |
| 5 | **Ψ** sidération | 2/10 | Champ froid. |
| 6 | **↕** verticalité | **8/10** | Asymétrie : les 8 groupes captent ~10 % du CIR national (~827,5/7 700 M€) sans effet causal documenté, pendant que les PME (effets prouvés) partagent le reste ; le taux théorique décroît avec la taille (30 % pour les petits, 6,25 % pour les gros), mais les volumes rendent les gros bénéficiaires nets dominants. |
| 7 | **Φ** spectacle | 2/10 | Aucun spectacle. |
| 8 | **Σ** sémiotique | 3/10 | « Crédit d'impôt », « innovation », « R&D » : vocabulaire positif naturalisant le transfert. |
| 9 | **Κ** cynisme | **8/10** | La France « subventionne l'innovation » en versant 7,7 Md€/an, dont les évaluations montrent qu'une grande part est d'aubaine chez les géants ; le Sénat force une annexe nominative que la DGFiP ne publie pas ; la CdC recommande de recentrer depuis 2018 sans effet. |
| 10 | **ρ** résistance | 7/10 | IPP (2019, 2021), CNEPI, CdC (2023), Sénat 808 (2025), presse économique. |
| 11 | **κ** influence subtile | 7/10 | Architecture par défaut : le CIR en volume (2008) bénéficie proportionnellement plus aux gros ; les seuils (100 M€) bornent le taux mais pas le volume ; le recentrage est débattu sans décision. |
| 12 | **⫸** convergence | 7/10 | IPP 2019 + IPP/CNEPI 2021 + CdC 2023 convergent : effet PME documenté, effet GE non documenté, recentrage recommandé — trois institutions indépendantes. |
| 13 | **⚔** guerre cognitive | 1/10 | Aucune campagne organisée documentée. |
| 14 | **🌐** réseau | 7/10 | 8 groupes, DGFiP, Sénat, IPP, CNEPI, CdC, cabinets fiscaux (ingénierie CIR), sous-traitants agréés. |
| 15 | **⏰** temporalité | 7/10 | 2008 réforme en volume ; 2016 CAE ; 2019 IPP ; 2021 IPP/CNEPI ; 2023 CdC ; 2025 Sénat 808 (annexe nominative). |

**BIAS TEST (15/15 scorés).** Aucun symbole au-delà de 9. Les champs 1, 4, 9 signalent la tension : la donnée existe (annexe), le périmètre ne permet pas une lecture définitive.

**PATTERNS** : @PAT[ICEBERG] (Ξ=9), @PAT[MONEY] (€=8), @PAT[CYN] (Κ=8), @PAT[FASC] (⫸=7). **THREATS** : @THR[REG_CAPTURE] (CIR volume), @THR[SUBSIDY] (aubaine GE).

**RHETORICAL** : NUM (ratios, taux, multiplicateurs) ; AUTH (IPP, CNEPI, CdC) ; DEM et BF = 0.

## 3. CLUSTERS (routage SYMBOLS §4)

| Cluster | Diagnostic | Gap |
|---------|------------|-----|
| ICEBERG (Ξ=9) | Émergé : ratios Annexe 12, taux théorique, évaluations. Immergé : périmètre exact de l'annexe, déclarations CIR individuelles. | Périmètre non confirmé. |
| MONEY (€=8) | Flux : contribuable → État → 8 groupes (~827,5 M€) + PME ; retour supposé : R&D. | Taux de retour réel par groupe indéterminé (tension de base). |
| POWER (↕=8) | Taux décroissant avec la taille, volumes croissants ; effet GE non documenté. | — |
| INVERSION (Ω=8, Κ=8) | « Levier d'innovation » vs « aubaine GE » ; transparence vs périmètre indéfini. | — |
| CONFIRMATION (κ=7) | CIR en volume par défaut ; recentrage débattu sans décision. | — |
| FRAGMENTATION (⫸=7) | IPP 2019, IPP/CNEPI 2021, CdC 2023 convergent. | — |
| NETWORK (🌐=7) | Groupes, DGFiP, cabinets fiscaux, sous-traitants. | — |
| TEMPORAL (⏰=7) | 2008 → 2025 : pas de recentrage effectif. | — |

## 4. HERMÉNEUTIQUE (statut : ANALYSE)

- **L1 (texte) :** Sénat 808 Annexe 12 (ratios), CGI 244 quater B (taux), IPP 2019/2021 (évaluations), CdC 2023 (recentrage), R&D publiées (rapports annuels).
- **L2 (structure) :** deux bases de calcul possibles — (a) dépenses éligibles CIR (Annexe 12 : Thales 2 520 M€), (b) R&D comptable publiée (Thales 1 273,7 M€). Les ratios changent radicalement selon la base : Thales 6,79 % (base a) vs 13,4 % (base b, 171/1273,7) ; STMicro 13,66 % (a) vs ~6,3 % (b, 119/1900). **Le choix de base est l'arbitre du verdict.**
- **L3 (intérêt) :** la DGFiP sait quel périmètre est dans l'annexe ; le Sénat l'a obtenue par auditions sans normalisation ; les groupes ont intérêt à déclarer un périmètre maximisant le ratio.
- **L4 (sémiotique) :** « dépenses de R&D » est présenté comme un fait simple alors qu'il recouvre éligible/comptable, France/monde, autofinancé/total.
- **L5 (comparaison) :** contraste avec le reste du corpus : les niches patrimoniales sont anonymes (22-15), le CIR est nominatif mais à périmètre flou — la visibilité sans normalisation est une semi-transparence.
- **L6 (contexte) :** débat 2024-2026 sur le « recentrage du CIR » (CdC, PLF) où la connaissance du taux de retour par groupe est l'enjeu.

**Lecture concurrente** : les groupes déclarent leurs R&D de bonne foi ; l'annexe 12 est un échantillon d'auditions sans prétention statistique ; l'effet d'aubaine est une moyenne qui ne dit rien d'un groupe particulier. La synthèse retenue : le taux de retour est incertain par choix de base, l'effet d'aubaine GE est documenté au niveau agrégé, et l'hétérogénéité des ratios (13,66 % vs 4,32 %) appelle une normalisation que personne n'a faite.

## 5. FORENSIC REASONING (ICEBERG MAX)

**Émergé (chiffré, vérifié)** : taux théorique 6,25 % (2 Md€) ; ratios Annexe 12 (STMicro 13,66 %, Safran 7,60 %, Renault 6,70 %, Thales 6,79 %, Sanofi 4,32 %) ; multiplicateur 1,3-1,5 (IPP) ; rendement brevet GE 0,464 vs TPE 1,165/M€ ; cumul 8 groupes ~827,5 M€.

**Surface (chiffré, périmètre incertain)** : R&D comptables publiées 2024 (Thales 1 273,7 M€, Safran 1 980 totale/1 348 autofinancée, Renault 4 066 CAPEX+R&D, STMicro 2 077 M$, Sanofi ~7,4 Md€, Stellantis ~5,7 Md€, Michelin ~700-800 M€, ArcelorMittal ~300-335 M$) — bases non comparables à l'annexe.

**Immergé (jamais publié)** : périmètre exact de l'annexe 12 ; déclarations CIR individuelles ; taux de retour effectif par groupe sur base éligible ; ventilation France/monde.

**ICEBERG LOAD :** 8 strates émergées/surface confirmées, 3 inférées. La signature : les ratios sont publics et vérifiés, leur interprétation est suspendue à un périmètre que personne ne normalise.

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « Le CIR est le premier levier d'innovation français, 7,7 Md€/an, plébiscité par les entreprises » : réforme 2008, volume, PME et grands groupes.
- **Antithèse (critique) :** « Le CIR des grands groupes est un effet d'aubaine massif » : aucun effet causal GE (IPP/CNEPI 2021), rendement brevet 2,5× inférieur, CdC recommande le recentrage.
- **Arbitrage par les preuves :** la thèse est confirmée pour les PME (effets causals documentés) ; l'antithèse est confirmée pour les GE au niveau agrégé (absence d'effet causal + rendement inférieur). **La synthèse** : le CIR est un outil à efficacité différenciée — prouvé pour les petites, non prouvé pour les grandes ; les 8 groupes de l'annexe captent ~10 % du flux sans effet documenté, ce qui constitue un faisceau d'aubaine sans preuve individuelle.

**Réfutation testée** : « l'absence d'effet causal prouve l'aubaine » — non : l'absence de preuve n'est pas la preuve d'absence (l'IPP lui-même note des limites d'estimation) ; « les ratios de l'annexe hiérarchisent les groupes » — non : la tension de périmètre interdit la hiérarchie. Les deux réfutations bornent le verdict.

## 7. CHRONOLOGIE

| Année | Événement | Source | Statut |
|-------|-----------|--------|--------|
| 2008 | Réforme CIR en volume : 30 % ≤ 100 M€, 5 % au-delà | CGI 244 quater B / LF 2008 | ✦ |
| 2016 | CAE : évaluations du CIR (premières critiques d'aubaine) | CAE | ✧ |
| 03/2019 | IPP (Bozio et al.) : multiplicateur 1,3-1,5, effet 15-18 % | IPP | ✦ |
| 06/2021 | IPP n° 33 / CNEPI : effet causal PME, AUCUN effet GE documenté ; brevet 0,464 vs 1,165/M€ | IPP/CNEPI | ✦ |
| 07/2023 | CdC : note « Piloter et évaluer les dépenses fiscales » — recentrer le CIR sur les PME | CdC | ✦ |
| 01/07/2025 | Sénat 808 : Annexe 12 = CIR et R&D nominatifs des 8 groupes (auditions) | Sénat | ✦ |

## 8. DOMAINES (par axe)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 TAUX-THÉORIQUE | Quel est le taux effectif théorique ? | 30 % ≤ 100 M€ + 5 % au-delà = 6,25 % pour 2 Md€ | FCT-001 | SATURATED |
| AXS-002 RATIOS-ANNEXE | Quels sont les ratios publiés ? | STMicro 13,66 %, Safran 7,60 %, Renault 6,70 %, Thales 6,79 %, Sanofi 4,32 % — hétérogènes | FCT-002 à 006 | SATURATED |
| AXS-003 R&D-PUBLIÉES | Quelles R&D comptables publiées ? | Thales 1 273,7 M€, Safran 1 980, STMicro 2 077 M$, Sanofi ~7,4 Md€, Stellantis ~5,7 — discordantes avec l'annexe | FCT-007 à 011 | SATURATED |
| AXS-004 AUBAINE | L'effet d'aubaine est-il documenté ? | IPP 2019 : multiplicateur 1,3-1,5 ; IPP/CNEPI 2021 : AUCUN effet causal GE ; brevet 0,464/M€ GE ; CdC 2023 : recentrer | FCT-012 à 015 | SATURATED |
| AXS-005 SYNTHÈSE | Peut-on calculer le taux de retour par groupe ? | Oui sur base Annexe (ratios publiés), mais tension de base (éligible vs comptable) interdit la hiérarchie en rigueur | FCT-016 | ANALYSE (calcul encadré) |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| 8 groupes CIR | Bénéficiaires | CIR 40-171 M€/an chacun ; déclarent R&D | FCT-002 à 011 | Bénéfice ≠ intention |
| DGFiP | Contrôleur | Contrôle des déclarations ; ne publie pas les taux par entreprise | Ξ=9 | ROLE |
| Sénat 808 | Divulgateur | Annexe 12 nominative (auditions publiques) | FCT-002 à 006 | ρ |
| IPP/CNEPI | Évaluateur | Effet causal PME, aucun GE ; brevet 0,464/M€ GE | FCT-012/013 | 🎓 |
| Cour des comptes | Contrôleur | Recommande le recentrage PME (2023) | FCT-015 | ρ |
| Cabinets fiscaux | Ingénierie | Optimisation CIR (non documenté ici) | — | ROLE |

**CONTROL_MAP** :

| Contrôleur | Mécanisme | Résultat | Gap |
|------------|-----------|----------|-----|
| CTRL-001 DGFiP | Contrôle des déclarations CIR | Contrôles ciblés | Pas de publication des taux par entreprise |
| CTRL-002 Sénat 808 | Auditions publiques | Annexe nominative (8 groupes) | Périmètre non normalisé |
| CTRL-003 IPP/CNEPI | Évaluation d'impact | Effet PME prouvé, GE non | Pas de mesure par groupe |
| CTRL-004 CdC | Note dépenses fiscales | Recentrage recommandé | Sans effet législatif à date |

## 10. CHAÎNES / PELOTE (causalité)

**CAU-001 : Le CIR en volume favorise structurellement les gros volumes.**
Étage 1 : taux 30 %/5 % avec seuil 100 M€ (FCT-001). Étage 2 : le taux décroît avec la taille (6,25 % à 2 Md€), mais le volume croît plus vite — les GE captent les montants absolus les plus élevés (171 M€ Thales). Étage 3 : 8 groupes ≈ 827,5 M€ cumulés. Type : STRUCTUREL. Confidence : high.

**CAU-002 : L'effet d'aubaine est concentré sur les grandes entreprises au niveau agrégé.**
Étage 1 : IPP/CNEPI 2021 : aucun effet causal GE vs effets PME (FCT-012/013). Étage 2 : rendement brevet GE 2,5× inférieur (FCT-014). Étage 3 : les R&D des GE existaient indépendamment du CIR (inférence agrégée, pas par groupe). Type : STATISTIQUE. Confidence : high au niveau agrégé, NON individuel.

**CAU-003 : La tension de périmètre empêche l'arbitrage public.**
Étage 1 : Annexe 12 = base X (éligible ?), R&D comptables = base Y. Étage 2 : ratios 13,66 % vs ~6,3 % pour STMicro selon la base. Étage 3 : sans normalisation, tout débat « qui profite du CIR » est indécidable en rigueur. Type : MÉTHODOLOGIQUE. Confidence : high.

**CAU-004 (rejetée) : « Les grands groupes fraudent le CIR ».** Réfutée : aucun fait pénal documenté dans ce dossier ; la question est l'effet d'aubaine (légal), pas la fraude. Le bénéfice n'implique pas l'intention.

## 11. CARTE DES PREUVES

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « Le taux théorique du CIR pour un grand groupe est ~6,25 % » | 30 % × 100 M€ + 5 % × 1 900 M€ = 125 M€ / 2 000 M€ (CGI 244 quater B) | Le taux dépend du périmètre éligible réel | SOUTENU (calcul) |
| CLM-002 | « Les ratios Annexe 12 sont hétérogènes (4,32 à 13,66 %) » | STMicro 13,66 %, Sanofi 4,32 %, Thales 6,79 % | Échantillon d'auditions, pas une base | SOUTENU (faits publiés) |
| CLM-003 | « Les bases Annexe 12 et R&D comptables sont discordantes » | Thales 2 520 (annexe) vs 1 273,7 M€ (comptes 2024) ; STMicro 871 vs ~1 900 M€ | Périmètres différents possibles (éligible vs comptable, France vs monde) | SOUTENU (constat, cause indéterminée) |
| CLM-004 | « Aucun effet causal du CIR documenté pour les grandes entreprises » | IPP n° 33 / CNEPI 06/2021 | Absence de preuve ≠ preuve d'absence | SOUTENU (au niveau agrégé) |
| CLM-005 | « L'effet d'aubaine GE est un faisceau, pas une preuve individuelle » | IPP + CNEPI + CdC convergent ; brevet 0,464/M€ GE | Aucun fait par groupe | SOUTENU (faisceau) |

### FACT_REGISTRY (16 faits)

| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-001 | Taux CIR : 30 % sur dépenses ≤ 100 M€, 5 % au-delà (CGI 244 quater B, LF 2008) ; taux effectif théorique pour 2 Md€ : 6,25 % (30 + 95 = 125 M€) | 30 %/5 % ; 6,25 % | SRC-01 CGI/BOFiP ; SRC-02 MESR | ✦ |
| FCT-002 | CIR STMicro : 119 M€ pour 871 M€ de R&D = 13,66 % (ratio ~2× le théorique) | 13,66 % | SRC-03 Sénat 808 Annexe 12 | ✦ |
| FCT-003 | CIR Safran : 152 M€ pour 2 000 M€ = 7,60 % | 7,60 % | SRC-03 | ✦ |
| FCT-004 | CIR Renault : 133,9 M€ pour 2 000 M€ = 6,70 % | 6,70 % | SRC-03 | ✦ |
| FCT-005 | CIR Thales : 171 M€ pour 2 520 M€ = 6,79 % | 6,79 % | SRC-03 | ✦ |
| FCT-006 | CIR Sanofi : 108 M€ pour 2 500 M€ = 4,32 % | 4,32 % | SRC-03 | ✦ |
| FCT-007 | R&D comptable Thales 2024 : 1 273,7 M€ (compte de résultat) — vs 2 520 M€ base annexe (écart ×2) | 1 273,7 M€ | SRC-04 Thales comptes 2024 | ✦ |
| FCT-008 | R&D comptable Safran 2024 : 1 980 M€ totales (1 348 autofinancées) — cohérent avec la base annexe 2 000 M€ | 1 980/1 348 M€ | SRC-05 Safran 2024 | ✦ |
| FCT-009 | R&D comptable STMicro 2024 : 2 077 M$ (~1 900 M€, mondial) — vs 871 M€ base annexe | 2 077 M$ | SRC-06 STMicro 20-F | ✦ |
| FCT-010 | R&D comptable Sanofi 2024 : ~7,4 Md€ — vs 2 500 M€ base annexe (écart ×3) | ~7,4 Md€ | SRC-07 Sanofi 2024 | ✦ |
| FCT-011 | R&D comptable 2024 des 3 autres : Stellantis ~5,7 Md€, Michelin ~700-800 M€, ArcelorMittal ~300-335 M$ | 5,7 / 0,75 / 0,3 Md€ | SRC-08/09/10 | ✧ |
| FCT-012 | IPP 2019 (Bozio et al.) : 1 € de CIR → 1,3-1,5 € de R&D supplémentaire (multiplicateur), effet 15-18 % | 1,3-1,5 | SRC-11 IPP 03/2019 | ✦ |
| FCT-013 | IPP n° 33 / CNEPI 06/2021 : effets causals significatifs pour TPE/PME ; AUCUN effet causal documenté pour les grandes entreprises | GE : aucun effet | SRC-12 IPP/CNEPI 2021 | ✦ |
| FCT-014 | Rendement brevet par M€ de CIR : 1,165 pour les TPE vs 0,464 pour les grandes entreprises (2,5×) | 1,165 vs 0,464 | SRC-12 | ✦ |
| FCT-015 | CdC 07/2023 : recommande le recentrage du CIR sur les PME (note « Piloter et évaluer les dépenses fiscales ») | recentrage | SRC-13 CdC 07/2023 | ✦ |
| FCT-016 | Cumul CIR des 8 groupes de l'annexe : 171+152+133,9+119+108+63,2+40,4+40 = 827,5 M€ ≈ 10,7 % du CIR national (~7,7 Md€) | ~827,5 M€ | calcul (SRC-03, SRC-14) | ⁂ calcul |

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | STMicro : 13,66 % (annexe) vs ~6,3 % (R&D comptable mondiale 119/1 900) | Tension de base : éligible France (871) vs R&D monde (~1 900) ; le ratio dépend du périmètre — les deux sont cités avec leur base | DOCUMENTÉE |
| CONTR-002 | Thales : 6,79 % (annexe, base 2 520) vs 13,4 % (base comptable 1 273,7) | Même tension : base éligible vs comptable ; l'annexe utilise probablement l'éligible (ou un périmètre groupe France) | DOCUMENTÉE |
| CONTR-003 | Sanofi : 4,32 % (annexe, 2 500) vs 1,5 % (base comptable ~7 400) | La R&D monde Sanofi (~7,4 Md€) inclut des acquisitions ; l'éligible CIR France est plus étroit | DOCUMENTÉE |
| CONTR-004 | « L'absence d'effet causal GE prouve l'aubaine » | L'absence de preuve n'est pas la preuve d'absence (l'IPP note des limites) ; l'aubaine reste une inférence agrégée | RÉSOLUE (borne le verdict) |

### EDI

```
geo:0.75 lang:0.80 strat:0.80 owner:0.70 persp:0.80 temp:0.80
EDI_raw = .25×.75 + .20×.80 + .20×.80 + .15×.70 + .15×.80 + .05×.80 = 0.7725
Pénalité : MISSING_COUNTER (-.10) : perspective des 8 groupes (défense du CIR, bénéfices d'innovation réels) absente du corpus.
EDI = 0.6725 (BROAD, sous la cible APEX 0.80, écart déclaré)
COV = 0.85 | IND = 0.65 | CC = 3/3
EDI* = .5×.6725 + .3×.85 + .2×.65 = 0.72
Perspectives : ⟐ 4 | ⟐̅ 2 | 🎓 3 (IPP, CNEPI, CdC) | 🌍 0 | 🔥 0
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait)

| FCT | QRY | SRC | URL (référence) | Statut |
|-----|-----|-----|-----------------|--------|
| FCT-001 | QRY-001 | SRC-01/02 | bofip.impots.gouv.fr ; enseignementsup-recherche.gouv.fr | ✦ |
| FCT-002 à 006 | QRY-002 | SRC-03 | senat.fr/rap/r24-808-1/r24-808-151.html (Annexe 12 — hérité 22-15) | ✦ |
| FCT-007 | QRY-003 | SRC-04 | lesechos-comfi.lesechos.fr (Thales états financiers 2024) | ✦ |
| FCT-008 | QRY-003 | SRC-05 | safran-group.com résultats 2024 | ✦ |
| FCT-009 | QRY-003 | SRC-06 | macrotrends.net STM R&D | ✦ |
| FCT-010 | QRY-003 | SRC-07 | sanofi.com rapports financiers | ✦ |
| FCT-012/013 | QRY-004 | SRC-11/12 | ipp.eu 03/2019 ; strategie-plan.gouv.fr (CNEPI 2021) | ✦ |
| FCT-015 | QRY-004 | SRC-13 | ccomptes.fr 07/2023 note dépenses fiscales | ✦ |

## 12. CARTE DIALECTIQUE (scénarios + responsabilité)

| Scénario | Hypothèse | Support | Contre | Lecture |
|----------|-----------|--------|--------|---------|
| S1 « Rente GE » | Les 8 groupes captent le CIR sans effet d'aubaine | Aucun effet causal GE (IPP/CNEPI) ; brevet 0,464/M€ | Les GE déclarent de la R&D réelle | Retenue (faisceau agrégé) |
| S2 « Outil PME » | Le CIR est efficace là où il cible les petites | Effets causals PME documentés | Les GE captent les volumes absolus | Retenue (synthèse) |
| S3 « Périmètre indéterminé » | On ne peut pas hiérarchiser les groupes sans normalisation | Discordance Annexe 12 / comptes | Les ratios publiés sont arithmétiquement exacts | Retenue (méthode) |

**IMPACT_MAP** :

| Acteur | Gain | Perte |
|--------|------|-------|
| 8 groupes | ~827,5 M€/an cumulés | — |
| PME | CIR avec effets causals | Part minoritaire du flux |
| État | — | 7,7 Md€/an sans effet GE documenté |
| Contribuables | — | Subvention d'aubaine présumée |

**RESPONSIBILITY_MAP** : aucun auteur d'intention n'est établi (BENEFIT != INTENT). Rôles : législateur (CIR en volume 2008), DGFiP (pas de publication), Sénat (divulgation), évaluateurs (recommandations sans effet). Responsabilité systémique : un dispositif dont l'efficacité par taille est documentée depuis 2021 sans décision de recentrage.

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : taux de retour CIR par groupe (Annexe 12 × R&D publiées), effet d'aubaine (IPP/CNEPI/CdC), tension de périmètre. Période 2019-2026.

**Exclusions explicites** : la fraude au CIR (aucun fait pénal) ; les déclarations CIR individuelles (secret fiscal) ; la ventilation France/monde des R&D des groupes.

**GAP déclarés** :
- GAP-001 (ACCESS) : périmètre exact de l'Annexe 12 (éligible vs comptable) — non confirmé par la source Sénat accessible.
- GAP-002 (ACCESS) : taux de retour effectif par groupe sur base éligible (déclarations CIR secrètes).
- GAP-003 (METHOD) : hiérarchisation des groupes impossible sans normalisation de base.
- GAP-004 (CORPUS) : perspective des 8 groupes absente (MISSING_COUNTER, EDI).

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : taux 30 %/5 %, seuil 100 M€ ; ratios Annexe 12 (13,66 % à 4,32 %) ; multiplicateur 1,3-1,5 ; aucun effet causal GE ; brevet 0,464/M€ GE ; CdC recentrage ; discordance bases (Thales ×2, Sanofi ×3).
- **PROBABLE (✧)** : R&D Stellantis/Michelin/ArcelorMittal (via agent) ; cause de la discordance = éligible vs comptable.
- **HYPOTHÈSE (⁂)** : cumul ~827,5 M€ ≈ 10,7 % du CIR national ; part d'aubaine GE (inférence agrégée, non mesurée).
- **CONTESTÉ (⊗)** : interprétation des ratios (périmètre de base).
- **INCONNU (⁅)** : périmètre Annexe 12 ; déclarations individuelles ; effet causal GE individuel.
- **RÉFUTÉ (❧)** : « la fraude des GE est prouvée » ; « les ratios hiérarchisent les groupes en rigueur ».

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD** : input UPDATE (croisement Annexe 12 × R&D publiées). Le verdict d'objet est distinct du verdict de lead : « taux de retour par groupe » reçoit une réponse honnête en deux volets (ratios publiés calculables, interprétation suspendue au périmètre).

**Vérifications contradictoires exécutées** : CONTR-001 à 004 (tensions de base STMicro/Thales/Sanofi ; absence de preuve ≠ preuve d'absence). Ratios arithmétiquement vérifiés (119/871 = 13,66 % ; 152/2000 = 7,60 %). Faits du 22-15 revalidés (montants nominatifs) et complétés (R&D comptables, évaluations).

**Verdict final : FAISCEAU FORT, NON PROUVÉ INDIVIDUELLEMENT.** Le taux de retour effectif est calculable sur la base Annexe 12 (hétérogène, 4,32-13,66 %), mais la discordance avec les R&D comptables publiées interdit la hiérarchie en rigueur ; l'effet d'aubaine des grandes entreprises est documenté au niveau agrégé par trois institutions indépendantes (IPP, CNEPI, CdC) — il reste une inférence statistique, pas une preuve par groupe. **Le résultat le plus actionnable : la normalisation du périmètre de l'Annexe 12 (éligible vs comptable) est la condition de tout arbitrage public éclairé sur le recentrage du CIR.**

---

# ANNEXE A. SOURCES

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | CGI art. 244 quater B + BOFiP BOI-BIC-RICI-10-10-30-10 | 2008-2026 | ◈ | https://bofip.impots.gouv.fr/bofip/6483-PGP.html |
| SRC-02 | Ministère Enseignement supérieur et Recherche, fiche CIR (taux) | 2025 | ◈ | https://www.enseignementsup-recherche.gouv.fr/fr/le-credit-d-impot-recherche-cir-47773 |
| SRC-03 | Sénat, commission d'enquête n° 808, Annexe 12 (CIR/R&D nominatifs) | 01/07/2025 | ◈ | https://www.senat.fr/rap/r24-808-1/r24-808-151.html |
| SRC-04 | Thales, états financiers consolidés 2024 (R&D 1 273,7 M€) | 04/03/2025 | ◈ | https://lesechos-comfi.lesechos.fr/press-release/thales-epa-ho-thales-met-a-disposition-ses-etats-financiers-2024-9XsI7x428Ku |
| SRC-05 | Safran, résultats annuels 2024 (R&D 1 980/1 348 M€) | 14/02/2025 | ◈ | https://www.safran-group.com/fr/espace-presse/safran-publie-ses-resultats-annuels-2024-2025-02-14 |
| SRC-06 | STMicroelectronics, Form 20-F / R&D 2 077 M$ | 2025 | ◈ | https://www.macrotrends.net/stocks/charts/STM/stmicroelectronics/research-development-expenses |
| SRC-07 | Sanofi, rapports financiers 2024 (R&D ~7,4 Md€) | 2025 | ◈ | https://www.sanofi.com/fr/investisseurs/rapports-financiers-et-information-reglementee |
| SRC-08 | Stellantis, rapport annuel 2024 (R&D ~5,7 Md€) | 02-03/2025 | ◈ | https://www.stellantis.com/fr/finance/reporting/rapports-financiers |
| SRC-09 | Michelin, DEU 2024 (R&D ~700-800 M€) | 07/04/2025 | ◈ | https://www.michelin.com/investisseurs/rapport-annuel-documents-legaux-reglementes |
| SRC-10 | ArcelorMittal, rapport annuel 2024 (R&D ~300-335 M$) | 10/03/2025 | ◈ | https://corporate.arcelormittal.com |
| SRC-11 | IPP (Bozio, Cottet, Py), « Évaluation d'impact de la réforme 2008 du CIR » | 03/2019 | 🎓 | https://www.ipp.eu/publication/evaluation-dimpact-de-la-reforme-2008-du-credit-impot-recherche/ |
| SRC-12 | IPP n° 33 / CNEPI, « Les impacts du CIR sur la performance économique » | 06/2021 | 🎓 | https://www.strategie-plan.gouv.fr/publications/evaluation-credit-dimpot-recherche-rapport-cnepi-2021 |
| SRC-13 | Cour des comptes, note « Piloter et évaluer les dépenses fiscales » | 07/2023 | ◈ | https://www.ccomptes.fr/system/files/2023-07/20230707-note-thematique-Depenses-fiscales.pdf |
| SRC-14 | Montants CIR des 3 groupes restants (Stellantis 63,2, Michelin 40,4, ArcelorMittal 40 M€) | 07/2025 | ◉ | (hérités du 22-15, via agent) |

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260809-2242-cir-taux-retour-effet-aubaine | PARENT_RUN_ID:20260809-2215 | AS_OF:2026-08-09 | INPUT_KIND:UPDATE | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:cir-taux-retour-effet-aubaine | complexity:13→APEX | route overrides:NONE | scope:2019-2026, France (+R&D monde)
modules:KERNEL|SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|INVESTIGATION
degraded:NONE | query target/actual: 8/8 (4 agents × 2 passes)

COUNT: ◈14 ◉1 | unique evidence objects:16 | upstream families:10
LEADS:terminal 1/1 | AXES:terminal 5/5 | N/A:none
FAILURES:1 (Annexe 12 : page r24-808-151 = sommaire, pas l'annexe — périmètre via agent 22-15, GAP-001) | FALLBACKS:0
unresolved gaps:GAP-001..GAP-004 (ACCESS/METHOD/CORPUS)
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @MNEMO_Q « CIR taux retour aubaine » + lecture parent 22-15 (Annexe 12) | Ratios hérités (13,66 % STMicro, 7,60 % Safran, 6,70 % Renault, 6,79 % Thales, 4,32 % Sanofi) | 22-15 | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_beneficiaires-niches-cessions/ |
| 2 | ◈ | QRY-001 (AXS-001) : taux CIR, seuils, périmètre éligible | FOUND : 30 % ≤ 100 M€ + 5 % au-delà ; 6,25 % pour 2 Md€ ; doctorants 2× ; sous-traitance publique 2× ; plafonds 2/10 M€ | SRC-01/02 | bofip.impots.gouv.fr ; MESR |
| 3 | ◈ | QRY-002 (AXS-002/005) : ratios Annexe 12 + cumul | FOUND : ratios hérités + cumul 827,5 M€ (calcul) | SRC-03 | senat.fr |
| 4 | ◈ | QRY-003 (AXS-003) : R&D comptables publiées des 8 groupes | FOUND : Thales 1 273,7 ; Safran 1 980/1 348 ; STMicro 2 077 M$ ; Sanofi ~7,4 Md€ ; Stellantis ~5,7 ; Michelin ~0,75 ; ArcelorMittal ~0,3 — discordance avec l'annexe (CONTR-001 à 003) | SRC-04 à 10 | rapports annuels |
| 5 | ◈ | QRY-004 (AXS-004) : effet d'aubaine, IPP/CNEPI/CdC | FOUND : multiplicateur 1,3-1,5 ; aucun effet causal GE ; brevet 0,464 vs 1,165/M€ ; CdC recentrage | SRC-11/12/13 | ipp.eu ; strategie-plan.gouv.fr ; ccomptes.fr |
| 6 | SYS | Calculs FCT-001 (6,25 %), FCT-016 (827,5 M€ ≈ 10,7 %) | ANALYSE étiquetée (calculs encadrés) | SRC-01/03 | — |
| 7 | SYS | @MNEMO_S + FACT_WRITEBACK | PENDING_AT_SERIALIZATION | — | — |
| 8 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cir-taux-retour-effet-aubaine/2026-08-09_22-42_cir-taux-retour-effet-aubaine_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 | Modules chargés ; manifest FINAL ; 15 symboles scorés, aucun ✗ | ✅ |
| G1 | LEAD vs OBJECT distincts ; 5 axes terminaux ; périmètre explicite | ✅ |
| G2 | 5 CLM avec support/counter/gap | ✅ |
| G3 | FACT_REGISTRY 16 faits, statuts canoniques | ✅ |
| G4 | Chaque ✦ → SRC-ID + URL ; ✧ pour corroboration restante | ✅ |
| G5 | CAU-001 à 004 typés, arrêt à l'évidence, aubaine = inférence agrégée | ✅ |
| G6 | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités | ✅ |
| G7 | CONTR-001 à 004 documentés et résolus | ✅ |
| G8 | TRACE_MATRIX ; QRY-001 à 004 tracés ; IDs résolus | ✅ |
| G9 | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis | ✅ |
| G10 | Un seul chemin ; une seule write FINAL ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY** : edi_gap = (0.80-0.6725)/0.80 = 0.159 ; query_gap = N/A ; coverage_gap = 0. GAP_SEVERITY = 0.159 × 1.00 = 0.16 < 0.20 → procéder avec divulgation (gaps GAP-001 à GAP-004 déclarés).

---

*TL;DR : SUJET : « la CJIR du CIR » — taux de retour effectif du crédit d'impôt recherche par groupe. OBJET : les ratios Annexe 12 (Sénat 808) sont publics et arithmétiquement vérifiés (STMicro 13,66 %, Safran 7,60 %, Renault 6,70 %, Thales 6,79 %, Sanofi 4,32 %) contre un taux théorique de 6,25 % pour 2 Md€ (30 % ≤ 100 M€ + 5 % au-delà) ; la TENSION DE PÉRIMÈTRE est la découverte centrale : les bases de l'annexe (Thales 2 520, STMicro 871, Sanofi 2 500 M€) sont discordantes avec les R&D comptables publiées (1 273,7, ~1 900, ~7 400 M€) — les ratios changent radicalement selon la base, interdisant la hiérarchie en rigueur. L'effet d'aubaine est documenté au niveau agrégé par IPP 2019 (multiplicateur 1,3-1,5), IPP/CNEPI 2021 (aucun effet causal GE vs effets PME ; brevet 0,464 vs 1,165/M€) et CdC 2023 (recentrage recommandé) : FAISCEAU FORT, non prouvé individuellement. Les 8 groupes cumulent ~827,5 M€ ≈ 10,7 % du CIR national. SOURCE : UPDATE du 22-15. MANIPULATION : Ξ=9, €=8, ↕=8, Κ=8. LIMITE : GAP-001 à GAP-004 (périmètre annexe non normalisé, déclarations secrètes, perspective des groupes absente).*
