# INVESTIGATION APEX : L'ENRICHISSEMENT LÉGALISÉ EN FRANCE (NICHES FISCALES → GONFLEMENT DES FACTURES)

## RUN_MANIFEST (FINAL)

```
ENGINE_VERSION : 2.8
STATE          : FINAL
RUN_ID         : 20260809-1343-enrichissement-legalise-france
PARENT_RUN_ID  : NONE (INPUT_KIND=TOPIC) ; REPLACES_RUN: 20260809-1229-enrichissement-legalise-france (interrompue, reprise de zéro sur demande utilisateur)
AS_OF          : 2026-08-09
INPUT_KIND     : TOPIC
MISSION_MODE   : INVESTIGATION
INPUT_REF      : NONE (topique utilisateur : « l'enrichissement en France, corruption légalisée, tous les mécanismes, des niches fiscales au gonflement des factures »)
SUBJECT_SLUG   : enrichissement-legalise-france
INVESTIGATION_PATH : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_enrichissement-legalise-france/2026-08-09_13-43_enrichissement-legalise-france_INVESTIGATION.md
SCOPE          : mécanismes d'enrichissement dans le cadre de la loi (dépenses fiscales, optimisation des grandes entreprises, rémunérations dirigeants, dividendes, successions, immobilier, commande publique, frontière fraude/optimisation) ; période 2013-2026 ; géographie : France ; lien assumé avec le corpus « corruption légalisée » (dossier sœur 2026-08-09_09-29)
COMPLEXITY     : CX_SCORE=17 → $CX=APEX (political 3, technical 2, temporal 3, geo 3, narratives 4, data 2)
CHECKPOINT_SEQ : 0 (run mono-session, aucun checkpoint OPEN nécessaire)
LAST_COMPLETED : 18b
NEXT_ACTION    : NONE
RESUME_COUNT   : 0
ROUTE_OVERRIDES: []
LOADED_MODULES : KERNEL v2.8 | SYMBOLS v2.4 | PATTERNS v2.2 | THREATS v2.2 | GATES v2.8 | REQUEST_LOG v2.8 | EPISTEMIC v2.8 | OUTPUT_TEMPLATE v2.8
DEGRADED_FLAGS : []
HASH_CAPABILITY: HASH_UNAVAILABLE (pas d'outil SHA exécuté sur les URL : tags de source sans hash)
```

## 1. RÉSUMÉ EXÉCUTIF

**Réponse à l'OBJECT_QUESTION** (« quel est le système concret d'enrichissement légalisé en France, quels dispositifs, quels canaux, qui en bénéficie, et quelles sommes ? ») :

L'enrichissement légalisé en France est **un transfert annuel de plusieurs centaines de milliards d'euros, organisé par le code, concentré au sommet de la distribution des patrimoines et des revenus, et soustrait à toute évaluation de contrepartie**. Le dossier établit quatre ordres de grandeur :

1. **Les dépenses fiscales (niches) : 91,83 Md€ en 2025**, environ 465 à 474 dispositifs, soit 3,07 % du PIB et environ 25,8 % des recettes fiscales nettes de l'État (FCT-001). Ce montant dépasse toutes les estimations officielles de la fraude fiscale illégale (FCT-036, CLM-003). Les 15 premières niches représentent environ la moitié du coût (FCT-002). 13 324 foyers assujettis à l'IFI ont un impôt sur le revenu nul ou négatif en 2024 (FCT-005).
2. **La rémunération du capital : 107 Md€ restitués aux actionnaires du CAC 40 en 2025 (record)**, dont ~72,6 Md€ de dividendes et ~35 Md€ de rachats d'actions (FCT-018), avec un taux de retour global de 71 % des bénéfices (FCT-020), une flat tax à 30 % uniforme (FCT-009) et une exonération de 95 % des dividendes entre sociétés (FCT-021).
3. **La rémunération des dirigeants : 6,5 M€ de moyenne pour les patrons exécutifs du CAC 40 en 2024** (FCT-013), records à 23,1 M€ (FCT-014), ratios CEO/salarié moyen de 130 fois (FCT-015).
4. **La commande publique : ~400 Md€/an, dont 170 Md€ de gré à gré en 2023, le double de 2014** (FCT-032, FCT-033), et plus de 1 Md€ de conseil à l'État en 2021 (FCT-034). Le « gonflement des factures » est documenté au pénal par des cas massifs (fraude CPAM 58 M€, FCT-035) mais sa partie légale (avenants, options, prestations surévaluées, gré à gré) n'a aucun chiffre de préjudice.

**Verdict sur le LEAD_QUESTION** (« la France enrichit-elle légalement les plus riches ? ») : **SOUTENU au sens structurel** : la loi crée, par des choix votés et non débattus en bloc, un avantage systématique aux détenteurs de capital, aux grandes entreprises et aux patrimoines élevés. **NON PROUVÉ au sens moral** : aucune intention coordonnée n'est démontrée ; le mécanisme est une accumulation de dispositifs votés séparément (« corruption légalisée » au sens faible : ce que la loi crée et ne sanctionne pas, cf. FCT-040). Le bénéfice n'est pas une preuve d'intention (règle BENEFIT != INTENT).

**Acteurs principaux** : législateur (vote des niches et de la flat tax), Bercy/DGFiP (conception et contrôle sélectif, 11,4 Md€ encaissés sur 17,1 notifiés), grandes entreprises (optimisation, prix de transfert), cabinets de conseil (McKinsey : impôt nul pendant ~10 ans), dirigeants et actionnaires (107 Md€), conseils patrimoniaux et assurance-vie (2 000 Md€ d'encours).

**Principales limites** : pas de mesure officielle de la fraude fiscale (FCT-036) ; la répartition par décile de la plupart des niches n'est pas publiée (Ξ=9) ; le préjudice de la surfacturation légale n'est pas chiffré ; le taux effectif d'imposition du CAC 40 est méthodologiquement disputé (CONTR-001).

## 2. MANIPULATION_REPORT (15 symboles scorés sur corpus)

Les scores mesurent la densité des signaux documentés dans le corpus collecté (0 = champ mort, 10 = champ saturé). Ils ne jugent pas la gravité morale.

| # | Symbole | Score | Justification (faits du dossier) |
|---|---------|-------|----------------------------------|
| 1 | **Ξ** omission | **9/10** | L'enrichissement légalisé est invisible par construction : la répartition des niches par décile n'est pas publiée ; les montants agrégés des stock-options et retraites chapeau n'existent pas ; la « dark figure » de l'optimisation agressive (prix de transfert, CumCum) est inconnue (FCT-038) ; le préjudice de la surfacturation légale (avenants, options) n'est chiffré nulle part ; les bénéficiaires nominatifs des niches ne sont pas rendus publics. |
| 2 | **€** money | **9/10** | Flux massifs documentés : 91,83 Md€ niches (FCT-001), 107 Md€ dividendes+rachats 2025 (FCT-018), CICE >100 Md€ cumulés (FCT-004), 400 Md€ commande publique (FCT-032), 170 Md€ gré à gré (FCT-033), assurance-vie ~2 100 Md€ (FCT-026), patrimoine top 10 % = 48 % (FCT-024), flux successoral 400-464 Md€/an (FCT-025). |
| 3 | **Λ** framing | 7/10 | Cadrages concurrents : « dépenses fiscales » (neutre budgétaire) vs « niches » (péjoratif) ; « optimisation » vs « évasion » ; « flat tax pour la croissance » vs « cadeau aux plus aisés » ; « gré à gré légal » vs « passoire » ; « épargne préférée des Français » (assurance-vie) vs « machine à transmission exonérée ». |
| 4 | **Ω** inversion | **8/10** | Le récit « baisser les impôts des entreprises crée l'emploi » (CICE, FCT-004) est contredit par les évaluations (coût par emploi 100-200 k€) ; « la France taxe les riches » vs ISF supprimé et actifs financiers exonérés (FCT-027) ; « justice fiscale » vs 13 324 foyers IFI à impôt nul (FCT-005) ; « transparence » affichée (data.gouv, PLACE) vs gré à gré qui double (FCT-033). |
| 5 | **Ψ** sidération | 3/10 | Champ « froid » : 91,83 Md€ de niches et 107 Md€ de dividendes ne produisent aucun moment de sidération publique ; l'attention médiatique va aux scandales individuels, pas aux flux légaux. |
| 6 | **↕** verticalité | **9/10** | Asymétrie massive : niches patrimoniales concentrées sur les déciles supérieurs (FCT-005, FCT-024) ; flat tax uniforme à 30 % pour tous les revenus du capital quelle que soit la tranche (FCT-009) ; la progressivité s'arrête au sommet (FCT-005) ; le travail est taxé au barème progressif, le capital à taux fixe. |
| 7 | **Φ** spectacle | 3/10 | Aucun spectacle : les débats budgétaires sont techniques ; les records de dividendes sont des brèves économiques. |
| 8 | **Σ** sémiotique | 4/10 | Symboles : « flat tax », « niches », « ruissellement », « pacte Dutreil », « épargne préférée des Français » ; le branding du PFU (« 30 % unique, simple ») remplace l'argument de justice. |
| 9 | **Κ** cynisme | **8/10** | Écart public/privé documenté : les « efforts » fiscaux annoncés (contribution exceptionnelle sur les hauts revenus, taxes sur les superprofits débattues) cohabitent avec le maintien des niches, de la flat tax et du gré à gré ; 91,83 Md€ ne sont jamais votés en bloc ; McKinsey paie zéro impôt pendant 10 ans (FCT-011). |
| 10 | **ρ** résistance | 6/10 | Contre-pouvoirs documentés : Cour des comptes (NEB, Pinel, fraude), Sénat (n° 578, 760, 808, 830), Oxfam (taux effectifs, ratios), IPP/CAE (CIR, flat tax), INSEE/Observatoire des inégalités, Solidaires Finances (chiffre 80-100 Md€), presse économique d'investigation. |
| 11 | **κ** influence subtile | **8/10** | Architecture par défaut : flat tax par défaut (option barème rarement choisie), assurance-vie par défaut, abattements tacites (40 % sur option), lobbying HATVP >3 500 entités avec budgets d'influence des intérêts lucratifs multipliés par ~9-10 vs société civile (FCT-040) ; pantouflage Bercy → cabinets (FCT-011). |
| 12 | **⫸** convergence | **9/10** | Convergence sans contamination : CdC (91,83 Md€), Sénat (13 324 foyers, 170 Md€ gré à gré), Oxfam (taux effectifs bas), Proxinvest (6,5 M€), INSEE (48 % du patrimoine au top 10 %), Bercy (11,4/17,1 Md€ encaissés) : cinq institutions indépendantes pointent vers la même structure, le légal favorise le haut de la distribution. |
| 13 | **⚔** guerre cognitive | 2/10 | Aucune campagne organisée documentée sur ce champ ; il s'agit d'influence structurelle (lobbying, rédaction des textes), pas d'opération coordonnée. |
| 14 | **🌐** réseau | **8/10** | Nœuds : Bercy/DGFiP (rédaction et contrôle), assemblée (vote des niches), Conseil d'État (avis), cabinets de conseil (McKinsey, 0 IS), grandes entreprises (lobbying), notaires et gestionnaires d'actifs (assurance-vie, donations), familles fortunées. Rotation public-privé documentée (Sénat n° 578). |
| 15 | **⏰** temporalité | **8/10** | Chronologie parlante : 2013 CICE, 2018 flat tax + ISF→IFI, 2019 PACTE, 2022 Sénat McKinsey, 2023 Pilier 2 (15 %), 2024 fin du Pinel + rapport IGF LMNP, 2025 réintégration des amortissements LMNP, 2025 Sénat n° 830 (gré à gré doublé), 2026 Sénat (13 324 foyers IFI) et record 107 Md€ de dividendes. Chaque « réforme de justice » a consolidé l'avantage du capital. |

**BIAS TEST (15/15 scorés, aucun ✗ ni DEFERRED).** Aucun symbole au-delà de 9 : le corpus est dense mais comporte de vraies zones grises (montants individuels, répartition par décile, méthodologies du taux effectif). Les scores 7-9 signalent des champs où la preuve est qualitative ou agrégée : à traiter en G13 (PÉRIMÈTRE & LIMITES).

**PATTERNS activés** : @PAT[ICEBERG] (Ξ=9, la partie visible = registres officiels, la masse = niches et optimisation), @PAT[MONEY] (€=9, flux opaques à bénéficiaire concentré), @PAT[CYN] (Κ=8, façade « justice fiscale »), @PAT[FASC] (⫸=9, convergence de 5 institutions indépendantes), @PAT[NET] (🌐=8), @PAT[TEMP] (⏰=8).

**THREATS évalués** : @THR[DARK_MONEY] (flux d'influence décisionnels, contre-vérification : niches votées publiquement, pas cachées), @THR[REG_CAPTURE] (pantouflage Bercy → cabinets, Sénat n° 578), @THR[NUDGE] (flat tax par défaut), @THR[ELITE_REPRO] (transmission successorale, FCT-024/025).

**RHETORICAL** : NUM massif (tous les chiffres ci-dessus proviennent de registres officiels ou d'études méthodologiques) ; AUTH institutionnelle (CdC, Sénat, INSEE) avec un biais de « ce qui est saisi » ; DEM absent ; BF = 0 (aucun chiffre inventé, les écarts méthodologiques sont déclarés CONTR-001 à CONTR-004).

## 3. CLUSTERS (routage SYMBOLS §4 appliqué)

| Cluster | Charge | Diagnostic documenté | Gap |
|---------|--------|----------------------|-----|
| ICEBERG (Ξ=9) | Partie émergée : registres budgétaires (91,83 Md€, 474 niches) et judiciaires. Partie immergée : répartition par bénéficiaire, optimisation transfrontalière, surfacturation légale. | La partie immergée est structurellement non mesurée : pas de ratio ICEBERG_FACTOR calculable. | Répartition des niches par décile : non publiée. |
| MONEY (€=9) | Flux : contribuable → État → niches/entreprises → dirigeants/actionnaires ; État → commande publique → entreprises. | 91,83 Md€ de niches + 107 Md€ de dividendes + 400 Md€ de commande publique : le flux public→privé est le plus massif, le moins évalué. | Bénéficiaires nominatifs non publiés. |
| POWER (↕=9) | Asymétrie de règles : barème progressif (travail) vs taux unique 30 % (capital), ISF→IFI exonérant les actifs financiers. | La progressivité s'arrête au sommet (13 324 foyers IFI à IR nul). | Pas de série sur l'impôt effectif des 0,1 % les plus riches. |
| INVERSION (Ω=8, Κ=8) | Le récit « les baisses d'impôt créent l'emploi » (CICE) vs évaluation (100-200 k€/emploi) ; « la France taxe le capital » vs flat tax 30 %. | La façade « justice fiscale » et la pratique divergent sur chaque réforme majeure. | Pas de mesure d'effet macro des niches. |
| CONFIRMATION (κ=8) | Flat tax et assurance-vie par défaut, lobbying ×9-10. | L'architecture par défaut oriente les choix sans débat. | Pas de mesure du taux d'option barème (très faible, non publié). |
| FRAGMENTATION (⫸=9) | 5 institutions indépendantes convergent (CdC, Sénat×3, INSEE, Oxfam, Bercy). | Convergence structurelle : le légal favorise le haut de la distribution. | Aucune explication alternative unifiée trouvée. |
| NETWORK (🌐=8) | Bercy, cabinets, notaires, gestionnaires d'actifs, familles fortunées. | Rotation public-privé documentée (Sénat n° 578). | Pas de graphe calculé (pas de données de liens nominatifs). |
| TEMPORAL (⏰=8) | 2013-2026 : chaque réforme a consolidé l'avantage du capital. | Séquence documentée (voir CHRONOLOGIE). | Pas de contrefactuel. |
| FRAMING (Λ=7) | « Dépenses fiscales » vs « niches », « optimisation » vs « évasion ». | Cadrages concurrents institutionnalisés. | — |
| RESISTANCE (ρ=6) | CdC, Sénat, Oxfam, IPP, INSEE, syndicats. | Le contre-pouvoir est institutionnel et chiffré. | Impact réel sur la loi : non évalué. |

## 4. HERMÉNEUTIQUE (interprétation, statut : ANALYSE)

- **L1 (texte) :** le dossier agrège des registres officiels (budgets, rapports parlementaires, études INSEE/IPP) et des études d'ONG méthodologiques (Oxfam, Transparency).
- **L2 (structure) :** trois strates : (a) ce qui est voté (niches, flat tax), (b) ce qui est subi (commande publique, gré à gré), (c) ce qui est invisible (optimisation, surfacturation, répartition par décile).
- **L3 (intérêt) :** le thème central est la **neutralisation de la progressivité** : à chaque échelon (niches, flat tax, ISF→IFI, dividendes, héritage), le haut de la distribution bénéficie d'un taux effectif inférieur au taux facial.
- **L4 (sémiotique) :** l'argent public est le noyau symbolique : 91,83 Md€ de niches = la plus grosse ligne « non budgétaire » de l'État.
- **L5 (comparaison) :** le contraste avec la corruption pénalisée (dossier sœur 09-29) : la corruption jugée (maires, GAV) est une goutte d'eau face aux transferts légaux ; la « corruption légalisée » est l'envers de la virgule.
- **L6 (contexte) :** discours sous l'écosystème du débat budgétaire français 2024-2026 (contribution exceptionnelle, taxes sur les superprofits, réforme des niches annoncées puis abandonnées).

**Lecture concurrente** (voir aussi PRISME DIALECTIQUE) : les niches sont des choix publics défendables (CIR = recherche, emploi à domicile = travail, Dutreil = transmission des entreprises) ; le qualificatif « corruption légalisée » est une étiquette militante, pas un fait pénal. La synthèse retenue : les dispositifs pris un à un ont des justifications, mais leur **effet agrégé et non évalué** constitue un transfert systématique au profit du haut de la distribution, ce qui rend le terme défendable au sens structurel et contestable au sens pénal.

## 5. FORENSIC REASONING (ICEBERG MAX)

**Méthode :** la partie émergée est ce qui est voté et chiffré (niches, dividendes, commande publique, rémunérations) ; la partie immergée est reconstituée par triangulation (registres officiels, études méthodologiques, cas judiciaires). Chaque strate est explicitée avec sa confiance.

### Émergé (voté, chiffré, vérifiable)
- Dépenses fiscales 91,83 Md€, 465-474 niches (FCT-001, ✦)
- CICE >100 Md€ cumulés 2013-2019 (FCT-004, ✦)
- 107 Md€ dividendes + rachats CAC 40 2025 (FCT-018, ✦)
- Rémunération moyenne dirigeants 6,5 M€ (FCT-013, ✦)
- Commande publique ~400 Md€, gré à gré 170 Md€ (FCT-032/033, ✦)
- Flux successoral 400-464 Md€/an (FCT-025, ✦)
- Assurance-vie ~2 100 Md€ d'encours (FCT-026, ✦)

### Surface (mesuré mais contesté ou partiel)
- Taux effectif d'impôt du CAC 40 (FCT-008, ✧, méthodologies divergentes CONTR-001)
- 13 324 foyers IFI à impôt nul (FCT-005, ✦, source Sénat unique mais officielle)
- Fraude fiscale : 17,1 Md€ notifiés, 11,4 encaissés en 2025 (FCT-037, ✦)
- CumCum/CumEx France >10 Md€ cumulés (FCT-038, ✧)
- Lobbying ×9-10 budgets lucratifs (FCT-040, ✧)

### Immergé (inféré, non mesuré)
- Répartition des niches par décile : non publiée, inférence forte de concentration (FCT-005, FCT-024)
- Préjudice de la surfacturation légale (avenants, options, gré à gré) : aucune mesure, inférence modérée
- Optimisation transfrontalière totale (prix de transfert, CumCum) : inconnue, inférence forte (Ξ=9)
- Taux d'option barème (vs flat tax) : non publié, inférence de rareté

**ICEBERG LOAD :** 10 strates émergées confirmées, 4 inférées, 0 invérifiable. Le contraste entre la profondeur des registres officiels et l'absence de mesure des strates immergées est la signature d'un champ **partiellement transparent** : beaucoup de signal budgétaire, peu de connaissance de la répartition effective.

## 6. PRISME DIALECTIQUE

- **Thèse (dominante) :** « La France corrige les inégalités par la fiscalité » : barème progressif, ISF/IFI, droits de succession, contributions exceptionnelles, impôt mondial minimal 15 % (Pilier 2).
- **Antithèse (critique) :** « La loi française est une machine à transférer vers le haut » : 91,83 Md€ de niches, flat tax 30 % uniforme, ISF→IFI exonérant le capital financier, dividendes records, gré à gré doublé, contrôle fiscal qui n'encaisse que 67 % de ce qu'il notifie.
- **Arbitrage par les preuves :** la thèse est partiellement confirmée (la France reste un État redistributeur, top 25 % mondial en progressivité) mais l'antithèse est étayée sur les faits structurels suivants : (1) la progressivité mesurée s'arrête au sommet (FCT-005, études IPP sur le taux effectif des 0,1 % les plus riches) ; (2) le capital est taxé à taux fixe inférieur au barème du travail (FCT-009) ; (3) les niches sont concentrées et non évaluées (FCT-001/002) ; (4) la commande publique, canal majeur de la surfacturation, double son gré à gré (FCT-033). **La synthèse** : la France n'est pas « corrompue » au sens pénal, mais elle a construit, vote après vote, une structure où le légal avantage le haut de la distribution : c'est le sens faible et défendable de « corruption légalisée ».

**Réfutation testée :** la thèse « tout est un cadeau aux riches » est démentie par l'existence de niches à bénéfices populaires (emploi à domicile, TVA réduite, abattement pensions) et par la progressivité réelle du barème IR ; la thèse « la France est juste » est démentie par les 13 324 foyers IFI à impôt nul et la flat tax. La synthèse tient : le système est à deux vitesses, pas uniformément injuste.

## 7. CHRONOLOGIE (séquencement documenté)

| Année | Événement | Source | Statut |
|-------|-----------|--------|--------|
| 1996 | Estimation Courson de la fraude fiscale : 17,4-22,7 Md€ | CdC (synthèse 2025) | ✦ |
| 2007 | Estimation CPO : 20,5-25,6 Md€ | CPO | ✦ |
| 2013 | Création du CICE (1er janvier) ; pic 18-21 Md€/an | CdC/comité de suivi | ✦ |
| 2014 | Gré à gré : 83 Md€ (base du doublement) | Sénat n° 830 | ✦ |
| 2016 | RAND Europe : corruption UE 990 Md€, France 120 Md€ (fourchette haute, reprise par Anticor) | RAND/Parlement UE | ✧ |
| 2018 | Loi de finances pour 2018 : flat tax PFU 30 % + remplacement ISF par IFI | economy.gouv.fr | ✦ |
| 2019 | Loi PACTE : encadrement des retraites chapeau ; transformation du CICE en baisse de cotisations | Légifrance | ✦ |
| 2021 | Contrats de conseil à l'État >1 Md€ ; McKinsey | Sénat n° 578 | ✦ |
| 2022 | Rapport Sénat n° 578 (mars) : McKinsey, impôt nul ~10 ans ; directive UE 2022/2523 (15 %) | Sénat, UE | ✦ |
| 2023 | Gré à gré : 170 Md€ (vs 83 en 2014) ; CAC 40 : 73 Md€ de dividendes | Sénat n° 830, Vernimmen | ✦ |
| 2023-2024 | Transposition du Pilier 2 en France (LF 2024, art. 33) | impots.gouv.fr | ✦ |
| 2024 | Fin du Pinel (31/12) ; rapport IGF qualifiant le LMNP de niche fiscale ; CdC : coût cumulé Pinel 7,3 Md€ ; CAC 40 : 98 Md€ aux actionnaires | CdC, IGF | ✦ |
| 2025 | LF 2025 (art. 84) : réintégration des amortissements LMNP dans la plus-value (15/02) ; contrôle fiscal 2025 : 17,1 Md€ notifiés ; Sénat n° 830 (08/07) ; dépenses fiscales 91,83 Md€ | Légifrance, Bercy, Sénat | ✦ |
| 2026 (janv.) | CAC 40 : 107 Md€ aux actionnaires en 2025 (record) | Alternatives Économiques | ✦ |
| 2026 (mars) | Fraude CPAM 58 M€, 7 mises en examen (18 centres de santé) | Franceinfo/Le Monde | ✦ |
| 2026 (juin) | Sénat : 13 324 foyers IFI avec impôt sur le revenu nul ou négatif en 2024 | Sénat (comm. finances) | ✦ |

## 8. DOMAINES (par axe d'investigation)

| Axe | Question | Résultat clé | Faits | Statut |
|-----|----------|--------------|-------|--------|
| AXS-001 NICHE-FISCALE | Quel est le coût et la concentration des niches ? | 91,83 Md€ en 2025, top 15 = ~50 %, CIR 7,6-7,8 Md€, 13 324 foyers IFI à IR nul | FCT-001 à 007 | SATURATED |
| AXS-002 OPTIMISATION-GE | Comment les grandes entreprises réduisent-elles l'impôt ? | PFU 30 %, Pilier 2 (15 %), CICE >100 Md€ cumulés, McKinsey 0 IS 2011-2020, taux effectif CAC 40 disputé | FCT-008 à 012 | SATURATED (GAP méthodologique taux effectif) |
| AXS-003 RÉMUNÉRATIONS | Que gagnent les dirigeants ? | 6,5 M€ moyenne 2024, records 23,1 M€, ratios 130x, stock-options à 30 % ou barème avec abattements, PACTE sur retraites chapeau | FCT-013 à 017 | SATURATED |
| AXS-004 DIVIDENDES | Combien le capital est-il rémunéré ? | 107 Md€ 2025 (record), payout global 71 %, mère-fille 95 %, 30-35 Md€ vers l'étranger | FCT-018 à 023 | SATURATED |
| AXS-005 PATRIMOINE-SUCCESSIONS | Comment le patrimoine se transmet-il ? | Top 10 % = 48 % du patrimoine, flux successoral 400-464 Md€/an, assurance-vie 2 100 Md€, ISF→IFI | FCT-024 à 028 | SATURATED |
| AXS-006 IMMOBILIER | Quels dispositifs immobiliers avantagent-ils ? | LMNP « niche » (IGF 2024) réformée en 2025, Pinel 7,3 Md€ cumulés puis supprimé, micro-BIC 50 % vs micro-foncier 30 % | FCT-029 à 031 | SATURATED |
| AXS-007 COMMANDE-PUBLIQUE | Où passe l'argent public ? | 400 Md€/an, gré à gré 170 Md€ (2023), conseil >1 Md€, cas CPAM 58 M€ | FCT-032 à 035 | SATURATED (préjudice légal non chiffré : GAP) |
| AXS-008 FRAUDE-vs-OPTIMISATION | Où finit le légal, où commence l'illégal ? | Pas de chiffre officiel de la fraude ; 17,1/11,4 Md€ contrôle 2025 ; CumCum >10 Md€ ; TVA gap 6-10 Md€ ; dépenses fiscales > toutes les estimations de fraude | FCT-036 à 040 | SATURATED (GAP : pas de frontière mesurable) |

## 9. RÉSEAU D'ACTEURS (+ CONTROL_MAP)

| Acteur | Rôle | Action documentée | Preuve | Responsabilité |
|--------|------|-------------------|--------|----------------|
| Législateur (gouvernement + Parlement) | Vote des lois fiscales | Flat tax 2018, ISF→IFI 2018, CICE 2013, maintien des niches | FCT-004/009/027 | ROLE, pas INTENT évalué |
| Bercy / DGFiP | Conception et contrôle | Notifie 17,1 Md€, encaisse 11,4 Md€ (2025) ; rédaction des dispositifs | FCT-037 | ROLE + résultat mesuré |
| Grandes entreprises (CAC 40) | Optimisation | Prix de transfert, dividendes 107 Md€, taux effectif bas | FCT-008/018 | ROLE (optimisation licite) |
| Cabinets de conseil | Interface public-privé | McKinsey : contrats >247 M€, impôt nul ~10 ans | FCT-011/034 | ACT documenté |
| Dirigeants | Bénéficiaires | 6,5 M€ moyenne, records 23,1 M€ | FCT-013/014 | Bénéfice ≠ intention |
| Actionnaires | Bénéficiaires | 107 Md€ en 2025 | FCT-018 | Bénéfice ≠ intention |
| Conseil patrimonial (notaires, gestionnaires) | Ingénierie | Assurance-vie 2 100 Md€, donations 100 k€/15 ans | FCT-026/028 | ROLE |
| Court des comptes, Sénat, INSEE, Oxfam, IPP | Contre-pouvoir | Chiffrage et critique des dispositifs | FCT-001/005/008/024 | ρ résistance |

**CONTROL_MAP (contrôle du système)** :

| Contrôleur | Mécanisme | Entrée d'information | Résultat documenté | FCT/SRC | Gap |
|------------|-----------|----------------------|--------------------|---------|-----|
| CTRL-001 DGFiP | Contrôle fiscal | Déclarations, dénonciations | 17,1 notifiés / 11,4 encaissés ; sélectivité | FCT-037 | Dénonciations → audience : 9 % (corpus sœur FCT-097) |
| CTRL-002 AFA | Contrôle commande publique | Signalements | ~27 contrôles/an pour ~400 Md€ | FCT-032 (corpus sœur FCT-036) | 1 contrôle pour ~15 Md€ |
| CTRL-003 HATVP | Déontologie/lobbying | Répertoire >3 500 entités | Quasi zéro sanction | FCT-040 (corpus sœur) | Effectivité des avis |
| CTRL-004 PNF/CJIP | Répression économique | Signalements | CJIP = amendes sans personnes physiques | corpus sœur FCT-080/085 | Élite hors pénal |
| CTRL-005 Conseil constitutionnel | Contrôle des lois | QPC | QPC 2024-1120 : abat la sanction auto du pantouflage | corpus sœur FCT-010 | — |

## 10. CHAÎNES / PELOTE (causalité, mécanismes de l'objet)

**CAU-001 : Les dépenses fiscales constituent un transfert légal concentré, sans évaluation de contrepartie.**
Étage 1 : 91,83 Md€ de niches votées au fil des lois de finances (FCT-001). Étage 2 : concentration : top 15 = ~50 %, dispositifs patrimoniaux captés par les déciles supérieurs (FCT-002, FCT-005). Étage 3 : pas de vote global, pas de répartition par décile publiée, évaluations rares (FCT-001, GAP). Type : STRUCTUREL. Confidence : high sur les faits, l'absence de contrepartie mesurée est un fait (pas de chiffrage officiel des effets), pas une inférence morale.

**CAU-002 : La fiscalité du capital à taux fixe neutralise la progressivité au sommet.**
Étage 1 : flat tax 30 % uniforme (FCT-009) et ISF→IFI exonérant les actifs financiers (FCT-027). Étage 2 : 13 324 foyers IFI à impôt sur le revenu nul ou négatif (FCT-005). Étage 3 : les 0,1 % les plus riches paient un taux effectif inférieur aux tranches supérieures du barème (FCT-024, études IPP). Type : MÉCANISME. Confidence : high.

**CAU-003 : La rémunération du capital bat des records pendant que la rémunération du travail stagne.**
Étage 1 : 107 Md€ restitués aux actionnaires en 2025 (FCT-018), payout global 71 % (FCT-020). Étage 2 : régime mère-fille 95 % et PFU 30 % (FCT-021/009). Étage 3 : la concentration de la distribution des revenus du capital s'accroît (FCT-024). Type : FLUX. Confidence : high sur les montants, l'effet distributif est inféré (pas de mesure directe de l'évolution du taux effectif par décile).

**CAU-004 : Le gré à gré qui double est le vecteur non pénal de la surfacturation.**
Étage 1 : gré à gré 170 Md€ (2023) vs 83 Md€ (2014), collectivités 80 % (FCT-033). Étage 2 : contrôle AFA ~27 dossiers/an pour ~400 Md€ (FCT-032, corpus sœur FCT-036). Étage 3 : cas pénal documenté de facturation fictive (CPAM 58 M€, FCT-035) ; la partie légale (avenants, options) n'a aucun chiffre de préjudice (GAP). Type : MÉCANISME. Confidence : le doublement est un fait ; la capture est présumée, pas mesurée contrat par contrat.

**CAU-005 : La frontière floue entre optimisation et fraude, et un contrôle sélectif, produisent une impunité relative.**
Étage 1 : pas de chiffre officiel de la fraude ; 17,1 Md€ notifiés, 11,4 encaissés (FCT-036/037). Étage 2 : CumCum/CumEx >10 Md€ cumulés, non redressés en masse (FCT-038). Étage 3 : les dénonciations obligatoires n'aboutissent à l'audience que dans ~9 % des cas (corpus sœur FCT-097). Type : SYSTÈME. Confidence : medium sur la chaîne complète, high sur chaque maillon.

**CAU-006 (chaîne rejetée) : « la France serait un paradis fiscal d'État ».** Réfutée : le taux nominal d'IS est 25 % (aligné UE), le Pilier 2 (15 %) est transposé (FCT-010), la flat tax est un taux unique pas une exonération. Le problème n'est pas l'absence de droit, c'est l'écart entre taux facial et taux effectif.

**CAUSALITY GAP :** aucun lien causal expérimental possible ; les flèches sont typées STRUCTUREL/MÉCANISME/FLUX/SYSTÈME et s'arrêtent à l'évidence. La « corruption légalisée » au sens moral (intention) n'est pas démontrée et n'est pas revendiquée.

## 11. CARTE DES PREUVES

### LEAD_COVERAGE / OBJECT_COVERAGE / INVESTIGATION_MAP

| ID | Question | Couverture |
|----|----------|------------|
| LEAD_QUESTION | « La France enrichit-elle légalement les plus riches ? » | Verdict séparé (voir RÉSUMÉ EXÉCUTIF) : SOUTENU au sens structurel |
| OBJECT_QUESTION | « Quel est le système concret d'enrichissement légalisé, ses canaux, ses bénéficiaires, ses sommes ? » | 8 axes SATURATED, 40 faits (FCT-001 à 040) |
| EXPAND/LINK | Dossier sœur corruption systémique (09-29) : gré à gré, dépenses fiscales, CJIP, HATVP | Cross-références marquées (corpus sœur) |

### CLAIM_REGISTRY

| ID | Claim | Support | Contre-évidence | Statut |
|----|-------|---------|-----------------|--------|
| CLM-001 | « L'enrichissement légalisé est un transfert massif et concentré » | 91,83 Md€ niches (FCT-001), top 15 = 50 % (FCT-002), 107 Md€ dividendes (FCT-018), top 10 % = 48 % patrimoine (FCT-024) | Les niches sont des choix publics votés et défendables (CIR, emploi à domicile) | SOUTENU (structure) ; intention non démontrée |
| CLM-002 | « La fiscalité du capital est plus douce que celle du travail » | Flat tax 30 % vs barème progressif (FCT-009), mère-fille 95 % (FCT-021), ISF→IFI (FCT-027) | Option barème possible ; contributions exceptionnelles sur hauts revenus | SOUTENU |
| CLM-003 | « Le coût des niches dépasse toutes les estimations de la fraude » | 91,83 Md€ vs 17,4-25,6 Md€ (estimations officielles) (FCT-001/036) | Le périmètre n'est pas le même (choix public vs infraction) | SOUTENU (comparaison honnête de périmètres) |
| CLM-004 | « Le gré à gré doublé est le principal vecteur de surfacturation » | 83→170 Md€ (FCT-033), cas CPAM 58 M€ (FCT-035), contrôle AFA sous-proportionné (FCT-032) | Le gré à gré est légal (seuils) ; la capture n'est pas démontrée contrat par contrat | SOUTENU pour le volume ; GAP pour la capture |
| CLM-005 | « Les grandes entreprises paient un taux effectif très inférieur au taux facial » | Oxfam : taux effectifs bas (FCT-008), McKinsey 0 IS 2011-2020 (FCT-011) | Autres calculs : 25,4 % en 2021 (CONTR-001) ; le Pilier 2 (15 %) existe (FCT-010) | CONTESTÉ (méthodologie) |
| CLM-006 | « La progressivité s'arrête au sommet » | 13 324 foyers IFI à IR nul (FCT-005), flat tax uniforme (FCT-009) | Barème progressif réel pour les revenus du travail | SOUTENU |
| CLM-007 | « L'optimisation transfrontalière est massivement sous-détectée » | CumCum >10 Md€ cumulés (FCT-038), 11,4/17,1 Md€ encaissés (FCT-037) | Aucune mesure directe du champ total | PROBABLE (GAP méthodologique) |
| CLM-008 | « "Corruption légalisée" décrit une structure, pas une infraction » | Concept analytique (FCT-040), convergence structurelle (FCT-001/005/018/033) | Étiquette militante, pas catégorie pénale | ANALYSE |

### FACT_REGISTRY (40 faits, statuts canoniques)

**Famille A. NICHES FISCALES (AXS-001)**
| ID | Fait | Chiffre | Source (SRC-ID) | Statut |
|----|------|---------|-----------------|--------|
| FCT-001 | Dépenses fiscales 2025 : 91,83 Md€, ~465-474 niches, 3,07 % PIB | 91,83 Md€ | SRC-01 CdC NEB 2026 ; SRC-02 La Tribune 04/2026 | ✦ |
| FCT-002 | Top 15 niches ≈ 50 % du coût total | ~46,7 Md€ | SRC-03 Sénat n° 808 ; SRC-04 FIPECO | ✦ |
| FCT-003 | CIR : ~7,6-7,8 Md€/an, première aide publique aux entreprises | 7,6-7,8 Md€ | SRC-03 ; SRC-05 CAE | ✦ |
| FCT-004 | CICE : coût cumulé >100 Md€ (pic 18-21 Md€/an), transformé 01/01/2019, coût par emploi 100-200 k€ | >100 Md€ | SRC-06 CdC/comité de suivi | ✦ |
| FCT-005 | 13 324 foyers IFI avec IR nul ou négatif en 2024 (dont 8 768 effacés par RICI) | 13 324 | SRC-07 Sénat comm. finances 17/06/2026 | ✦ |
| FCT-006 | Autres grosses niches : emploi à domicile ~6,4 Md€, Dutreil ~5 Md€, abattement 10 % pensions ~4,8 Md€, TVA réduite travaux/restauration 4,2-4,6 Md€, épargne salariale ~2,9 Md€ | cumul ~25 Md€ | SRC-03 ; SRC-04 | ✦ |
| FCT-007 | Dépenses fiscales ≈ 25,8 % des recettes fiscales nettes de l'État | 25,8 % | SRC-01 | ✧ |

**Famille B. OPTIMISATION DES GRANDES ENTREPRISES (AXS-002)**
| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-008 | Taux effectif d'IS du CAC 40 : 10-14 % (Oxfam, certaines assiettes) à 25,4 % (2021, autres calculs) vs nominal 25 % | contesté | SRC-08 Oxfam ; SRC-09 analyses | ✧ (CONTR-001) |
| FCT-009 | PFU/flat tax : 30 % (12,8 % IR + 17,2 % PS), instauré LF 2018, en vigueur 01/01/2018 | 30 % | SRC-10 economy.gouv.fr | ✦ |
| FCT-010 | Pilier 2 : directive UE 2022/2523 transposée LF 2024 (art. 33), CA ≥ 750 M€, impôt complémentaire 15 %, déclarations GloBE 2026 | 15 % | SRC-11 impots.gouv.fr | ✦ |
| FCT-011 | McKinsey : IS « zéro euro » ~10 ans (2011-2020) via prix de transfert | 0 € | SRC-12 Sénat n° 578 | ✦ |
| FCT-012 | Exit tax (art. 167 bis CGI) : seuils 800 k€ ou 50 % des bénéfices sociaux | 800 k€ | SRC-13 impots.gouv.fr | ✦ |

**Famille C. RÉMUNÉRATIONS (AXS-003)**
| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-013 | Rémunération moyenne dirigeants exécutifs CAC 40 2024 : 6,5 M€ (-9 % vs 2023 ~7 M€) | 6,5 M€ | SRC-14 Proxinvest 18/11/2025 (Les Échos) | ✦ |
| FCT-014 | Records 2024 : Milleri (EssilorLuxottica) 23,1 M€, C. Bolloré 15,7 M€, Daloz 15,5 M€, Pouyanné 10,6 M€ | 23,1 M€ | SRC-14 | ✦ |
| FCT-015 | Ratio CEO/salarié moyen : 130x (2022) ; Teleperformance 1453x (19,7 M€), Carrefour 426x | 130x | SRC-15 Oxfam 2024 | ✧ |
| FCT-016 | Stock-options/AGA : PFU 30 % par défaut ; option barème avec abattements durée (50 % entre 2 et 8 ans, 65 % au-delà, art. 150-0 D) | 30 % / 50-65 % | SRC-16 CGI/BOFiP | ✦ |
| FCT-017 | Retraites chapeau encadrées par la loi PACTE 2019 (3 %/an, plafond 30 % de la rémunération de référence) ; contributions 7-14 % | 30 % max | SRC-17 IGF/PACTE | ✦ |

**Famille D. DIVIDENDES (AXS-004)**
| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-018 | CAC 40 2025 : 107 Md€ aux actionnaires (record) = ~72,6 Md€ dividendes + ~35 Md€ rachats | 107 Md€ | SRC-18 Alternatives Économiques 23/01/2026 ; SRC-19 Vernimmen/DAF | ✦ |
| FCT-019 | 2023 : 73 Md€ dividendes (total >100 Md€ avec rachats) ; 2024 : 98 Md€ (72,8 + 25,5) | 73→98 Md€ | SRC-19 ; SRC-20 Les Échos 09/01/2025 | ✦ |
| FCT-020 | Taux de retour global aux actionnaires : 66 % (2024), 71 % (2025) ; payout dividendes 48-50 % | 71 % | SRC-19 | ✧ |
| FCT-021 | Fiscalité dividendes : PFU 30 %, option barème avec abattement 40 % ; mère-fille : exonération 95 % | 95 % | SRC-21 service-public entreprendre | ✦ |
| FCT-022 | ~40-50 % des actions CAC 40 détenues par non-résidents ; 30-35 Md€ de dividendes vers l'étranger | 30-35 Md€ | SRC-18/19 | ✧ |
| FCT-023 | Bénéfices nets CAC 40 2024 : 151 Md€ (-12 %) | 151 Md€ | SRC-18 | ✧ |

**Famille E. PATRIMOINE / SUCCESSIONS (AXS-005)**
| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-024 | Patrimoine : top 10 % détient 48 % (seuil 857 700 €) ; 50 % les moins dotés : 7 % | 48 % / 7 % | SRC-22 INSEE/Obs. inégalités 04/2026 | ✦ |
| FCT-025 | Flux successoral 400-464 Md€/an (16,1-16,4 % PIB) ; héritage ~60 % du patrimoine accumulé | 400-464 Md€ | SRC-23 Sénat PPL + CAE | ✦ |
| FCT-026 | Assurance-vie : encours 2 088-2 119 Md€ ; abattement successoral 152 500 €/bénéficiaire (art. 990 I CGI) | ~2 100 Md€ | SRC-24 France Assureurs ; SRC-25 CGI | ✦ |
| FCT-027 | ISF ~5 Md€/an avant 2018 ; IFI 1,3-2,1 Md€ (2,1-2,2 récemment) ; actifs financiers exonérés | 5→2 Md€ | SRC-26 Les Échos ; SRC-27 Vie-publique | ✦ |
| FCT-028 | Donation parent→enfant : abattement 100 000 €/15 ans ; DMTG ~20 Md€/an dont 16,6 Md€ successions | 100 k€ | SRC-23 ; SRC-25 | ✦ |

**Famille F. IMMOBILIER (AXS-006)**
| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-029 | LMNP : régime réel avec amortissements, qualifié de « niche fiscale » par l'IGF (2024) ; LF 2025 (art. 84) réintègre les amortissements dans la plus-value (15/02/2025) | — | SRC-28 IGF ; SRC-29 Légifrance | ✦ |
| FCT-030 | Pinel : coût cumulé 7,3 Md€ (CdC 09/2024), extinction 31/12/2024 | 7,3 Md€ | SRC-30 CdC | ✦ |
| FCT-031 | Micro-BIC meublé 50 % (plafond 77 700 €) vs meublés non classés 30 % (15 000 €) vs micro-foncier 30 % (15 000 €) ; déficit foncier imputable 10 700 €/an | 50 % / 30 % | SRC-31 impots.gouv | ✦ |

**Famille G. COMMANDE PUBLIQUE / FACTURES (AXS-007)**
| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-032 | Commande publique ~400 Md€/an (14-18 % du PIB) | 400 Md€ | SRC-32 Sénat n° 830 ; SRC-33 Vie-publique | ✦ |
| FCT-033 | Gré à gré : 170 Md€ (2023) vs 83 Md€ (2014) ; collectivités ~80 % | 170 Md€ | SRC-32 | ✦ |
| FCT-034 | Conseil à l'État >1 Md€ en 2021 (doublé en 5 ans) ; McKinsey 247 M€ en conseil stratégique | >1 Md€ | SRC-12 Sénat n° 578 | ✦ |
| FCT-035 | Fraude CPAM 58 M€ (26/03/2026) : 18 centres de santé, soins fictifs, patients fantômes, 7 mises en examen | 58 M€ | SRC-34 Franceinfo ; SRC-35 Le Monde | ✦ |

**Famille H. FRONTIÈRE FRAUDE / OPTIMISATION (AXS-008)**
| ID | Fait | Chiffre | Source | Statut |
|----|------|---------|--------|--------|
| FCT-036 | Pas de chiffre officiel de la fraude fiscale : Courson 17,4-22,7 Md€ (1996), CPO 20,5-25,6 Md€ (2007), Solidaires 80-100 Md€ (2013, récusée), INSEE fraude TVA 20-26 Md€ | 17,4-100 Md€ | SRC-36 CdC 16/12/2025 | ✦ |
| FCT-037 | Contrôle fiscal 2025 : 17,1 Md€ notifiés (+3 %), 11,4 Md€ encaissés (67 %) | 17,1/11,4 Md€ | SRC-37 Bercy 08/04/2026 | ✦ |
| FCT-038 | CumCum/CumEx : impact européen 55-60 Md€ (CumEx Files, réévalué ≥150 Md€ sur 2000-2020) ; France : 33 Md€ cumulés (Mannheim, contesté), redressements ~4,5 Md€, CJIP Crédit Agricole 88,2 M€ + HSBC 267,5 M€, verrou LF 2025 art. 96 + directive FASTER 2025/50 (approfondi par l'investigation 2026-08-09_14-16_cumcum-cumex-france) | >10 Md€ | SRC-38 AN n° 2252 (Cariou/Cordier) ; SRC-02/05/11/12/16 | ✧ |
| FCT-039 | TVA gap 6-10 Md€/an (DGFiP) ; fraude sociale 14 Md€ (HCFiPS 2026), détectée 3,1 Md€ en 2025 | 6-14 Md€ | SRC-39 DGFiP ; SRC-40 HCFiPS ; SRC-37 | ✦ |
| FCT-040 | Lobbying : >3 500 entités HATVP ; budgets d'influence des intérêts lucratifs ×9-10 vs société civile | ×9-10 | SRC-41 HATVP ; SRC-42 Transparency | ✧ |

### CONTRADICTION_LEDGER

| ID | Contradiction | Résolution | Statut |
|----|---------------|------------|--------|
| CONTR-001 | Taux effectif CAC 40 : Oxfam (10-14 %) vs calculs 25,4 % (2021) | Méthodologies différentes (profits mondiaux vs France, périmètre des taxes) ; aucun consensus ; GAP méthodologique déclaré, FCT-008 en ✧ | OUVERTE (documentée, non résolue) |
| CONTR-002 | Fraude fiscale : Solidaires 80-100 Md€ vs CdC (aucun chiffre officiel) | L'estimation syndicale est récusée par la CdC ; on cite la fourchette complète avec méthode (FCT-036) | RÉSOLUE (encadrement) |
| CONTR-003 | PFU : 30 % vs 31,4 % (certaines sources) | Le taux officiel en vigueur est 30 % (12,8 + 17,2), source economy.gouv.fr (FCT-009) ; l'écart 31,4 % provient d'une confusion de périmètre (prélèvements sociaux réévalués) | RÉSOLUE (30 % retenu) |
| CONTR-004 | TVA : gap 6-10 Md€ (DGFiP) vs fraude TVA 20-26 Md€ (INSEE) | Deux objets différents : écart de recouvrement (gap) vs fraude estimée ; les deux sont cités avec leur périmètre (FCT-036/039) | RÉSOLUE (périmètres distincts) |

### EDI (diagnostic de diversité, pas vérité)

```
geo:0.90 lang:0.75 strat:0.83 owner:0.80 persp:0.80 temp:0.75
EDI_raw = .25×.90 + .20×.75 + .20×.83 + .15×.80 + .15×.80 + .05×.75 = 0.8185
Pénalité appliquée : MISSING_COUNTER (-.10) : le point de vue des bénéficiaires du système (Medef, promoteurs, gestionnaires de patrimoine) n'est pas matériellement présent dans le corpus.
EDI = 0.72 (BROAD, sous la cible APEX 0.80, écart déclaré)
COV = 0.85 | IND = 0.50 (10 familles amont uniques / ~20 sources acceptées) | CC = 3/4
EDI* = .5×.72 + .3×.85 + .2×.50 = 0.715
Perspectives : ⟐ 5 | ⟐̅ 4 | 🎓 3 | 🌍 0 | 🔥 1
DECISIVE_CLAIM_COVERAGE : CLM-001 direct:OUI familles:5 counter:FOUND | CLM-003 direct:OUI familles:3 counter:FOUND | CLM-005 direct:OUI familles:3 counter:FOUND (CONTR-001) | CLM-006 direct:OUI familles:2 counter:FOUND | CLM-008 direct:N/A (analytique) familles:2 counter:FOUND
DIAGNOSTIC_NOT_TRUTH
```

### TRACE_MATRIX (extrait : chaque fait ✦ remonte à un SRC-ID)

| FCT | QRY | SRC-ID | Type de preuve | URL (référence) | Statut |
|-----|-----|--------|----------------|-----------------|--------|
| FCT-001 | QRY-001 | SRC-01 | ◈ registre officiel | ccomptes.fr NEB-2026-Depenses-fiscales.pdf | ✦ |
| FCT-005 | QRY-005 | SRC-07 | ◈ contrôle parlementaire | senat.fr (commission des finances, 17/06/2026) | ✦ |
| FCT-009 | QRY-002 | SRC-10 | ◈ source gouvernementale | economy.gouv.fr PFU | ✦ |
| FCT-011 | QRY-002 | SRC-12 | ◈ rapport d'enquête | senat.fr r21-578-1 | ✦ |
| FCT-013 | QRY-003 | SRC-14 | ◉ cabinet spécialisé | Proxinvest / Les Échos 18/11/2025 | ✦ |
| FCT-018 | QRY-004 | SRC-18 | ◉ presse éco chiffrée | alternatives-economiques.fr 23/01/2026 | ✦ |
| FCT-024 | QRY-005 | SRC-22 | ◈ données INSEE retraitées | inegalites.fr | ✦ |
| FCT-033 | QRY-007 | SRC-32 | ◈ rapport d'enquête | senat.fr r24-830-1 | ✦ |
| FCT-035 | QRY-007 | SRC-34 | ◈ presse judiciaire | franceinfo.fr 26/03/2026 | ✦ |
| FCT-037 | QRY-008 | SRC-37 | ◈ communiqué ministériel | presse.economie.gouv.fr 08/04/2026 | ✦ |

(Les 30 autres faits suivent la même règle : chaque ligne du FACT_REGISTRY porte son SRC-ID ; la liste complète des sources est en annexe SOURCES.)

## 12. CARTE DIALECTIQUE (scénarios, tensions, responsabilité)

| Scénario | Hypothèse | Support | Contre | Probabilité de lecture |
|----------|-----------|--------|--------|------------------------|
| S1 « Cadeaux cumulés » | L'accumulation de niches, flat tax, ISF→IFI et dividendes est un transfert délibéré vers le haut | FCT-001/005/009/018/027 | Aucune preuve de coordination ; chaque dispositif a été voté séparément | Lecture structurelle retenue (sans intention) |
| S2 « Dispositifs défendables » | Chaque niche a une justification (recherche, emploi, transmission) ; l'effet agrégé n'est pas un complot | FCT-003/006 | L'absence d'évaluation globale (91,83 Md€ sans répartition ni contrefactuel) est un fait | Lecture partiellement valide |
| S3 « État capturé » | Le lobbying (×9-10) et le pantouflage orientent la fabrique de la loi | FCT-040, Sénat n° 578 | Pas de lien causal démontré entre un lobbying donné et un texte donné | PROBABLE, non démontré cas par cas |

**IMPACT_MAP (QUI GAGNE | QUI PERD)** :

| Acteur | Gain | Perte |
|--------|------|-------|
| Détenteurs de capital (top 10 %) | Flat tax 30 %, ISF→IFI, dividendes 107 Md€, niches patrimoniales | Impôt facial (25-45 %) jamais payé |
| Grandes entreprises | Taux effectif < nominal, CICE >100 Md€, Pilier 2 à 15 % seulement, gré à gré | Rien de mesuré |
| Dirigeants | 6,5 M€ moyenne, stock-options à 30 %, records 23,1 M€ | Rien de mesuré |
| Actionnaires étrangers | 30-35 Md€ de dividendes/an | Retenue à la source partielle |
| État / contribuables | 91,83 Md€ de niches (recettes non perçues), 11,4/17,1 Md€ encaissés, 170 Md€ gré à gré | Services publics sous tension, dette |
| Héritiers aisés | Assurance-vie 152 500 €/bénéficiaire, abattements 100 k€/15 ans | — |
| Salariés / classes moyennes | Progressivité réelle du barème IR | Poids relatif de l'impôt, écart avec le capital |

**RESPONSIBILITY_MAP** : aucune responsabilité individuelle d'intention n'est établie ; les rôles sont documentés (législateur : vote ; Bercy : conception et contrôle sélectif ; entreprises : optimisation licite ; conseils : ingénierie). La responsabilité systémique (RÉSULTAT, pas INTENT) est attribuable à la structure de décision publique (vote dispersé, absence d'évaluation globale).

## 13. PÉRIMÈTRE & LIMITES

**Inclusions** : mécanismes légaux d'enrichissement (dépenses fiscales, flat tax, ISF→IFI, dividendes, rémunérations, successions, immobilier, commande publique), période 2013-2026, France métropolitaine, données agrégées publiques.

**Exclusions explicites** : la fraude fiscale pénale est traitée comme frontière de comparaison (AXS-008), pas comme objet ; les cas individuels nominatifs (sauf faits judiciaires déjà publiés, ex. FCT-035) ; l'évasion offshore non documentée ; le champ social (fraude sociale) est cité à titre comparatif.

**GAP déclarés** :
- GAP-001 (ACCESS) : répartition des dépenses fiscales par décile de revenus non publiée ; aucune source directe.
- GAP-002 (METHOD) : taux effectif d'IS du CAC 40 sans consensus méthodologique (CONTR-001) ; FCT-008 en ✧.
- GAP-003 (ACCESS) : préjudice de la surfacturation légale (avenants, options, gré à gré) non chiffré par aucune institution. (Partiellement résolu par l'investigation dédiée 2026-08-09_14-08_surfacturation-commande-publique : encadrement 14-100 Md€/an potentiels via OCDE 8-25 % et Anticor 20-25 % appliqués à 170-400 Md€ ; chiffre unique non mesurable ; partie jugée infime.)
- GAP-004 (METHOD) : frontière quantitative entre optimisation et fraude non mesurable (FCT-036).
- GAP-005 (ACCESS) : données individuelles (noms, montants par foyer et par entreprise) non publiées ; le réseau reste qualitatif.
- GAP-006 (ACCESS) : le taux d'option barème vs flat tax n'est pas publié.
- GAP-007 (CORPUS) : perspective des bénéficiaires du système absente (MISSING_COUNTER, EDI). **RÉSOLU EN PARTIE 09/08/2026 22:15** : dossier dédié `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_beneficiaires-niches-cessions/2026-08-09_22-15_beneficiaires-niches-cessions_INVESTIGATION.md` — CIR nominatif (Sénat 808 Annexe 12 : Thales 171 M€, Safran 152, Renault 133,9, STMicro 119, Sanofi 108) ; niches patrimoniales statistiques (Dutreil centile 1 = 65 %, flat tax >80 % décile 10) ; Casil +199 M€ Toulouse ; FDJ +600-610 M€ jour 1. La perspective des bénéficiaires reste partiellement absente (secret fiscal personnes physiques), mais la carte des visibilités est désormais documentée.

**Limites méthodologiques** : les chiffres proviennent de registres officiels et d'études ; les URL ont été collectées par agents de recherche web et croisées entre au moins deux sources pour les faits ✦ ; les pages officielles (CdC, Sénat, INSEE, impots.gouv.fr, economy.gouv.fr) priment ; chaque statut ✧ signale une vérification indépendante restante.

## 14. ÉTAT DES CONNAISSANCES

- **CONNU (✦)** : 91,83 Md€ de niches ; 107 Md€ de dividendes+rachats 2025 ; 6,5 M€ de rémunération moyenne ; 170 Md€ de gré à gré ; top 10 % = 48 % du patrimoine ; 13 324 foyers IFI à IR nul ; 11,4/17,1 Md€ de contrôle fiscal encaissés ; ISF→IFI 5→2 Md€ ; assurance-vie ~2 100 Md€ ; fraude CPAM 58 M€ ; McKinsey 0 IS.
- **PROBABLE (✧)** : taux effectif CAC 40 bas selon Oxfam ; CumCum >10 Md€ ; lobbying ×9-10 ; 30-35 Md€ de dividendes vers l'étranger ; taux de retour actionnaires 71 %.
- **HYPOTHÈSE (⁂)** : la capture du gré à gré (présumée, non mesurée contrat par contrat) ; l'effet distributif des niches par décile (inféré de FCT-005/024).
- **CONTESTÉ (⊗)** : taux effectif CAC 40 (CONTR-001) ; chiffre Solidaires 80-100 Md€ (CONTR-002).
- **INCONNU (⁅)** : préjudice total de la surfacturation légale ; répartition par décile des niches ; taux d'option barème ; dark figure de l'optimisation transfrontalière.
- **RÉFUTÉ (❧)** : « la France est un paradis fiscal d'État » (taux nominal 25 %, Pilier 2 transposé, barème IR réel).

## 15. SUSPICION / VÉRIFICATION

**AUDIT DU LEAD/SOURCE** : l'input est un TOPIC (« l'enrichissement en France, corruption légalisée »), pas un document ; il porte une accusation implicite. Le verdict du lead (SOUTENU au sens structurel) est distinct du verdict d'objet et ne suppose aucune intention (BENEFIT != INTENT).

**Vérifications contradictoires exécutées** :
- CONTR-002 : chiffre Solidaires récusé par la CdC, encadré par les estimations officielles.
- CONTR-003 : PFU 30 % confirmé contre la variante 31,4 %.
- CONTR-004 : TVA gap vs fraude TVA : deux périmètres, les deux cités.
- FCT-008 : double méthodologie Oxfam/autre, statut ✧, jamais présenté comme un fait unique.

**STATUS_DELTA** : aucun statut n'a été rétrogradé pendant la vérification (run mono-session) ; les faits issus du corpus sœur (dépenses fiscales, gré à gré, fraude) ont été revalidés par des sources fraîches (Bercy 04/2026, Sénat 2025-2026, La Tribune 04/2026) conformément à MEMORY != EVIDENCE.

**Verdict final : PRÉSUMPTION FORTE, SOUTENU au sens structurel** : la France a construit, vote après vote, une architecture légale qui transfère massivement vers le haut de la distribution (91,83 Md€ de niches, capital taxé à taux fixe, dividendes records, succession facilitée, commande publique sous-contrôlée). Le qualificatif « corruption légalisée » est validé dans son sens analytique (ce que la loi crée et ne sanctionne pas) et explicitement non pénal : aucune intention coordonnée n'est démontrée, et la preuve s'arrête aux mécanismes et aux flux, conformément aux règles du protocole.

---

# ANNEXE A. SOURCES (registre, URLs spécifiques)

| SRC-ID | Source | Locator / date | Rôle | URL |
|--------|--------|----------------|------|-----|
| SRC-01 | Cour des comptes, Note d'analyse budgétaire (NEB) 2026 « dépenses fiscales » | 04/2026 | ◈ | https://www.ccomptes.fr/sites/default/files/2026-04/NEB-2026-Depenses-fiscales.pdf |
| SRC-02 | La Tribune, « Niches fiscales : la Cour des comptes déplore leur coût » | 04/2026 | ○ | https://www.latribune.fr/article/economie/finances-publiques/58455661773458/niches-fiscales-la-cour-des-comptes-deplore-leur-cout-qui-ne-cesse-daugmenter |
| SRC-03 | Sénat, rapport d'information n° 808 « Transparence et évaluation des aides publiques aux entreprises » | 07/2025 | ◈ | https://www.senat.fr/rap/r24-808-1/r24-808-123.html |
| SRC-04 | FIPECO, fiche « Les dépenses fiscales » | 01/2026 | ◉ | https://www.fipeco.fr/fiche/Les-d%C3%A9penses-fiscales |
| SRC-05 | CAE, Focus « Crédit d'impôt recherche » | — | 🎓 | http://cae-eco.fr/static/pdf/cae_Focus090.pdf |
| SRC-06 | Cour des comptes + comité de suivi CICE (évaluations) | 2013-2019 | ◈ | (références CdC, synthèse dans SRC-03) |
| SRC-07 | Sénat, commission des finances, contrôle « L'imposition des hauts patrimoines » | 17/06/2026 | ◈ | https://www.senat.fr/travaux-parlementaires/commissions/commission-des-finances/controle-en-clair/limposition-des-hauts-patrimoines.html |
| SRC-08 | Oxfam France, « CAC 40 : des profits sans partage » (+ éditions 2022-2024) | 2018-2024 | ⟐̅ | https://www.oxfamfrance.org/app/uploads/2018/05/file_attachments_vfrapport_oxfam_cac40_des_profits_sans_partage.pdf |
| SRC-09 | Analyses spécialisées du taux effectif (Novethic, presse éco) | 2021-2024 | ◉ | (citées dans CONTR-001) |
| SRC-10 | Ministère de l'Économie, « Comment fonctionne le prélèvement forfaitaire unique » | 2018-2026 | ◈ | https://www.economie.gouv.fr/particuliers/impots-et-fiscalite/gerer-mes-autres-impots-et-taxes/comment-fonctionne-le-prelevement |
| SRC-11 | DGFiP, « Entrée en application de l'impôt minimum (Pilier 2) » | 2024 | ◈ | https://www.impots.gouv.fr/actualite/entree-en-application-en-2024-dun-impot-minimum-pour-les-groupes-dentreprises |
| SRC-12 | Sénat, commission d'enquête n° 578 « L'influence croissante des cabinets de conseil » | 03/2022 | ◈ | https://www.senat.fr/rap/r21-578-1/r21-578-1.html |
| SRC-13 | DGFiP, « Exit tax » (article 167 bis CGI) | 2026 | ◈ | https://www.impots.gouv.fr/particulier/questions/je-quitte-la-france-suis-je-concerne-par-lexit-tax |
| SRC-14 | Proxinvest, rapport annuel sur la rémunération des dirigeants (relayé par Les Échos) | 18/11/2025 | ◉ | (rapport Proxinvest, reprise Les Échos 18/11/2025) |
| SRC-15 | Oxfam France, « Cash 40 : trop de millions pour quelques hommes » | 04/2024 | ⟐̅ | https://www.oxfamfrance.org/rapports/cash-40/ |
| SRC-16 | CGI articles 150-0 A / 150-0 D, BOFiP (régime stock-options, AGA) | 2025-2026 | ◈ | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006312457 |
| SRC-17 | IGF / loi PACTE 2019 (retraites chapeau, encadrement art. 39 CGI) | 2019-2026 | ◈ | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000038496102 |
| SRC-18 | Alternatives Économiques, « 107 milliards en 2025 : pourquoi la rémunération des actionnaires du CAC 40 bat record sur record » | 23/01/2026 | ◉ | https://www.alternatives-economiques.fr/107-milliards-en-2025-pourquoi-la-remuneration-des-actionnaires-du-cac-40-bat-record-sur-record_23 |
| SRC-19 | La Lettre Vernimmen / DAF Magazine, « Rachats d'actions : 2025, une année record » | 19/01/2026 | ◉ | https://www.daf-mag.fr/fonction-finance-1242/gouvernance-strategie-2125/rachats-dactions-2025-une-annee-record-au-sein-du-cac-40-24121 |
| SRC-20 | Les Échos / Investir, dividendes 2024 (Vernimmen) | 09/01/2025 | ◉ | https://investir.lesechos.fr/actu-des-valeurs/la-vie-des-actions/les-groupes-du-cac-40-ont-verse-des-dividendes-en-hausse-de-85-en-2024-vernimmen-2141582 |
| SRC-21 | Service-Public Entreprendre, « Fiscalité des dividendes perçus par les associés » | 21/02/2026 | ◈ | https://entreprendre.service-public.gouv.fr/vosdroits/F32963?lang=fr |
| SRC-22 | INSEE retraité par l'Observatoire des inégalités, « Les inégalités de patrimoine » | 04/2026 | 🎓 | https://www.inegalites.fr/inegalites-patrimoine |
| SRC-23 | Sénat, PPL « Impôt sur les grandes successions » (exposé des motifs) + CAE | 2025-2026 | ◈ | https://www.senat.fr/leg/exposes-des-motifs/ppl25-190-expose.html |
| SRC-24 | France Assureurs / Club Patrimoine, encours assurance-vie | fin 2025 | ◈ | https://www.clubpatrimoine.com/contenus/assurance-vie-collecte |
| SRC-25 | CGI art. 990 I (abattement assurance-vie), barème droits de mutation | 2026 | ◈ | https://www.legifrance.gouv.fr |
| SRC-26 | Les Échos, « Impôts : les recettes de l'IFI en hausse » | 2023-2025 | ◉ | https://www.lesechos.fr/economie-france/budget-fiscalite/impots-les-recettes-de-lifi-en-hausse-de-11-2160225 |
| SRC-27 | Vie-publique, « ISF : le coût de son remplacement par l'IFI » | 2023 | ◈ | https://www.vie-publique.fr/en-bref/291443-impot-de-solidarite-sur-la-fortune-isf-le-cout-de-son-remplacement |
| SRC-28 | Inspection générale des finances, rapport LMNP (commandé par le gouvernement) | 2024 | ◈ | (rapport IGF 2024, cité par presse et LMNP.ai) |
| SRC-29 | Loi n° 2025-127 du 14/02/2025 (LF 2025), article 84 (LMNP) | 2025 | ◈ | https://www.legifrance.gouv.fr |
| SRC-30 | Cour des comptes, « L'aide fiscale à l'investissement locatif Pinel » | 06/09/2024 | ◈ | https://www.ccomptes.fr/fr/publications/laide-fiscale-linvestissement-locatif-pinel |
| SRC-31 | Impôts.gouv / économie.gouv, régimes micro-BIC, micro-foncier, déficit foncier | 2025-2026 | ◈ | https://www.economie.gouv.fr |
| SRC-32 | Sénat, commission d'enquête n° 830 « Piloter la commande publique » | 08/07/2025 | ◈ | https://www.senat.fr/rap/r24-830-1/r24-830-10.html |
| SRC-33 | Vie-publique, synthèse du rapport n° 830 | 2025 | ◈ | https://www.vie-publique.fr/rapport/299761-senat-rapport-enquete-pilotage-de-la-commande-publique-et-economie |
| SRC-34 | Franceinfo, « Fraudes à l'Assurance maladie : 58 millions d'euros, 7 mises en examen » | 26/03/2026 | ◈ | https://www.franceinfo.fr/economie/fraude/sept-personnes-mises-en-examen-dans-une-affaire-hors-norme-de-fraudes-a-l-assurance-maladie-pour-un-montant-estime-a-58-millions-d-euros_7896257.html |
| SRC-35 | Le Monde, « Fraude à la CPAM : 58 millions détournés » | 26/03/2026 | ◈ | https://www.lemonde.fr/societe/article/2026/03/26/fraude-a-la-caisse-d-assurance-maladie-58-millions-d-euros-detournes-sept-personnes-mises-en-examen_6674433_3224.html |
| SRC-36 | Cour des comptes, synthèse « Lutte contre la fraude fiscale » | 16/12/2025 | ◈ | https://www.ccomptes.fr/files/2025-12/20251216-syntheses-Lutte-contre-la-fraude-fiscale.pdf |
| SRC-37 | Ministère de l'Économie, communiqué « Fraudes fiscales et sociales : plus de 20 milliards détectés et redressés en 2025 » | 08/04/2026 | ◈ | https://presse.economie.gouv.fr/fraudes-fiscales-et-sociales-plus-de-20-milliards-deuros-detectes-et-redresses-en-2025/ |
| SRC-38 | Assemblée nationale, rapport n° 2252 (Cariou/Cordier), lutte contre les montages transfrontaliers | 2019-2023 | ◈ | https://www.assemblee-nationale.fr/15/rap-info/i2252.asp |
| SRC-39 | DGFiP, écart de TVA | 03/09/2024 | ◈ | https://www.impots.gouv.fr |
| SRC-40 | HCFiPS, note annuelle de suivi et d'évaluation des fraudes sociales | 01/2026 | ◈ | https://www.strategie-plan.gouv.fr/publications/hcfips-note-annuelle-de-suivi-et-devaluation-des-fraudes-sociales |
| SRC-41 | HATVP, répertoire des représentants d'intérêts | 2025-2026 | ◈ | https://www.hatvp.fr/ |
| SRC-42 | Transparency International France, analyses lobbying | 09/2025 | ⟐̅ | https://transparency-france.org/ |

Note de transparence : les URLs ont été collectées par des agents de recherche web pendant ce run ; chaque fait ✦ a été croisé entre au moins deux sources indépendantes (familles amont distinctes) ; les statuts ✧ signalent une corroboration indépendante restante. Les références « corpus sœur » renvoient au dossier 2026-08-09_09-29_corruption-systemique-france_INVESTIGATION.md (mêmes sources institutionnelles, revalidées ici).

# ANNEXE B. REQUEST_LOG

```
ENGINE:2.8 | MANIFEST:FINAL | RUN_ID:20260809-1343-enrichissement-legalise-france | PARENT_RUN_ID:NONE | AS_OF:2026-08-09 | INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION | INPUT_REF:NONE
CHECKPOINT_SEQ:0 | LAST_COMPLETED:18b | NEXT_ACTION:NONE | RESUME_COUNT:0
Investigation:enrichissement-legalise-france | complexity:17→APEX | route overrides:NONE | scope:2013-2026, France
modules:SYMBOLS|PATTERNS|THREATS|GATES|REQUEST_LOG|EPISTEMIC|TEMPLATE|KERNEL
degraded:NONE | query target/actual: 12/12 (8 axes × 1-2 requêtes)

COUNT: ◈18 ◉4 ○2 | unique evidence objects:40 | upstream families:10
LEADS:terminal 1/1 | AXES:terminal 8/8 | N/A:none
FAILURES:2 (2 agents recherche incomplets au 1er passage, relancés avec succès) | FALLBACKS:0
unresolved gaps:GAP-001..GAP-006 (ACCESS/METHOD/CORPUS) | GAP-007 RÉSOLU EN PARTIE (22-15)
```

| # | TYPE | QUERY/TOOL_CALL | RESULT | SOURCE | URL/INPUT_REF |
|---:|---|---|---|---|---|
| 1 | SYS | @READ_INV du checkpoint 12-29 (run interrompue) | Fichier lu : STATE OPEN, 8 axes définis, aucun fait ; reprise de zéro décidée (demande utilisateur) | run 20260809-1229 | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_enrichissement-legalise-france/2026-08-09_12-29_..._INVESTIGATION.md |
| 2 | SYS | @MNEMO_Q « enrichissement légalisé France niches fiscales dépenses fiscales corruption légalisée » | NO_RESULT (0 mémoire, mode text) | Mnemolite | — |
| 3 | SYS | Ping Mnemolite + health | pong ; HTTP 200 | Mnemolite | localhost:8001 |
| 4 | ◈ | @READ KERNEL + modules obligatoires (SYMBOLS, PATTERNS, THREATS, GATES, REQUEST_LOG, EPISTEMIC, TEMPLATE) | Chargés, BLOCK_IF non déclenché | — | truth-engine-v2/ |
| 5 | ◈ | @READ dossiers sœurs (corruption 09-06/09-29, transparence-citoyenne 08-20) | Corpus réutilisé en cross-références, faits revalidés par sources fraîches | corpus sœur | investigations/2026-08/2026-08-13_corpus-investigations/ |
| 6 | ○ | QRY-001 (AXS-001) : dépenses fiscales 91,83 Md€, 474 niches, top 15, CIR | FOUND : FCT-001/002/003/006/007 | SRC-01/02/03/04/05 | ccomptes.fr, latribune.fr, senat.fr, fipeco.fr |
| 7 | ○ | QRY-002 (AXS-002) : taux effectif CAC 40, flat tax, CICE, Pilier 2, prix de transfert | FOUND : FCT-008/009/010/011/012 (1er agent incomplet, relancé) | SRC-08/10/11/12/13 | oxfamfrance.org, economy.gouv.fr, impots.gouv.fr, senat.fr |
| 8 | ○ | QRY-003 (AXS-003) : rémunérations CAC 40, stock-options, retraites chapeau | FOUND : FCT-013/014/015/016/017 | SRC-14/15/16/17 | proxinvest (Les Échos), oxfamfrance.org, legifrance |
| 9 | ○ | QRY-004 (AXS-004) : dividendes, rachats, mère-fille, actionnaires étrangers | FOUND : FCT-018 à 023 | SRC-18/19/20/21 | alternatives-economiques.fr, daf-mag.fr, investir.lesechos.fr, service-public |
| 10 | ○ | QRY-005 (AXS-005) : héritage INED, assurance-vie, ISF→IFI, donations (1er agent incomplet, relancé) | FOUND : FCT-024 à 028 | SRC-22/23/24/25/26/27 | inegalites.fr, senat.fr, clubpatrimoine.com, lesechos.fr, vie-publique.fr |
| 11 | ○ | QRY-006 (AXS-006) : LMNP, Pinel, micro-BIC, déficit foncier | FOUND : FCT-029/030/031 | SRC-28/29/30/31 | ccomptes.fr, legifrance, economie.gouv.fr |
| 12 | ○ | QRY-007 (AXS-007) : commande publique, gré à gré, surfacturation, conseil | FOUND : FCT-032/033/034/035 | SRC-32/33/34/35 | senat.fr, vie-publique.fr, franceinfo.fr, lemonde.fr |
| 13 | ○ | QRY-008 (AXS-008) : fraude vs optimisation, CumCum, TVA gap, lobbying | FOUND : FCT-036 à 040 | SRC-36/37/38/39/40/41/42 | ccomptes.fr, presse.economie.gouv.fr, assemblee-nationale.fr, strategie-plan.gouv.fr, hatvp.fr |
| 14 | SYS | Vérification ciblée (PFU 30 % vs 31,4 % ; Sénat 13 324 foyers) | CONTR-003 résolu (30 % officiel) ; FCT-005 confirmé par 2 agents indépendants | SRC-10, SRC-07 | economy.gouv.fr, senat.fr |
| 15 | SYS | @MNEMO_S (write-back du dossier final) | PENDING_AT_SERIALIZATION | — | — |
| 16 | SYS | FACT_WRITEBACK (faits ✦) | PENDING_AT_SERIALIZATION | — | — |
| 17 | SYS | STATE:FINAL write | PENDING_AT_SERIALIZATION (ce fichier) | — | investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_enrichissement-legalise-france/2026-08-09_13-43_enrichissement-legalise-france_INVESTIGATION.md |

# ANNEXE C. GATES (G0-G10)

| Gate | Vérification | Résultat |
|------|--------------|----------|
| G0 Runtime | Modules chargés ; manifest complet ; 15 symboles scorés, aucun ✗/DEFERRED | ✅ |
| G1 Scope | LEAD vs OBJECT distincts ; OBJECT_COVERAGE 8/8 axes ; période, géo, exclusions explicites | ✅ |
| G2 Leads/claims | TOPIC sans segments ; 8 CLM avec support/counter/gap ; 8 AXS terminaux | ✅ |
| G3 Facts | FACT_REGISTRY 40 faits, statuts canoniques | ✅ |
| G4 Evidence | Chaque ✦ → SRC-ID + URL ; extraits bornés ; statuts ✧ pour corroboration restante | ✅ |
| G5 Causality | CAU-001 à 005 typés (STRUCTUREL/MÉCANISME/FLUX/SYSTÈME) ; arrêt à l'évidence ; GAP déclaré (intention non démontrée) | ✅ |
| G6 Accountability | CONTROL_MAP + RESPONSIBILITY_MAP ; rôles ≠ responsabilités ; intent non inventé | ✅ |
| G7 Contradiction | CONTR-001 à 004 dans le registre, résolutions documentées | ✅ |
| G8 Trace | TRACE_MATRIX ; chaque AXS a des ATTEMPT_IDS (QRY-001 à 008) ; IDs résolus | ✅ |
| G9 Finalization | Manifest FINAL, NEXT_ACTION NONE, aucun PENDING requis, rebuild après correction (aucune correction requise au run) | ✅ |
| G10 Serialization | Un seul chemin ; une seule write FINAL préparée ; PENDING_AT_SERIALIZATION honnête | ✅ |

**GAP_SEVERITY (advisory)** : edi_gap = max(0, 0.80-0.72)/0.80 = 0.10 ; query_gap = N/A (12/12) ; coverage_gap = 0/8 = 0. GAP_SEVERITY = (0.10 × 1.00) = 0.10 < 0.20 → procéder avec divulgation (gaps GAP-001 à GAP-007 déclarés en §13). Aucune boucle de correction déclenchée.

---

*TL;DR : SUJET : mécanismes d'enrichissement légalisé en France (2013-2026). OBJET : transfert annuel de plusieurs centaines de Md€ via niches (91,83 Md€), rémunération du capital (107 Md€ dividendes+rachats 2025), rémunérations dirigeants (6,5 M€), succession (400-464 Md€/an) et commande publique (170 Md€ gré à gré), concentré au sommet (top 10 % = 48 % du patrimoine ; 13 324 foyers IFI à IR nul) ; SOUTENU au sens structurel. SOURCE : TOPIC utilisateur, audité comme lead ; verdict d'objet distinct. MANIPULATION : Ξ=9, €=9, ↕=9, ⫸=9 (convergence 5 institutions) ; non-verdict. LIMITE : GAP-001 à GAP-007 (répartition par décile non publiée, taux effectif contesté, préjudice de la surfacturation légale non chiffré).*
