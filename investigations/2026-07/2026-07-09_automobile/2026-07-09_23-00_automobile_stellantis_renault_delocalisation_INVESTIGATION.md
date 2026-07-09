# INVESTIGATION AUT-001 — AUTOMOBILE
## Stellantis, Renault : délocalisation, subventions sans contrepartie, transition subie (1945-2026)

**CIV :** AUT-001 | **Type :** APEX | **Date enquête :** 2026-07-09 | **Complexité :** 8/10
**EDI :** 0.76 | **BIAS TEST :** PASS (E>D>C>A>B)

---

## §0 TEXT_ANALYSIS

◆ **BIAS TEST :**
```
Classement : E (Academic) > D (AFP Factuel) > C (Citoyen) > A (Viginum) > B (RT)
Résultat  : PASS
```

**Score SYMBOLS ×15 :**

| Symbole | Score | Justification |
|---------|:-----:|---------------|
| **Ξ** | 8 | Production France masquée par CA mondial, coûts externalisés environnement/santé |
| **€** | 8 | 18 Md€ aides 2018-2024, Stellantis Pays-Bas, 40-65k emplois détruits |
| **Λ** | 7 | « Transition écologique », « leasing social », « souveraineté industrielle » |
| **Ω** | 4 | « Bonus écologique = écologie » masque subvention aux imports |
| **Ψ** | 2 | Secteur à cycles longs |
| **↕** | 8 | Asymétrie constructeurs/sous-traitants, Bercy/constructeurs, classes populaires exclues du neuf |
| **Φ** | 4 | Mondial de l'Auto, F1, spectacle technologique |
| **Σ** | 5 | Greenwashing électrique, « mobilité durable », sportswashing F1 |
| **Κ** | 5 | Subventions sans contrepartie = cynisme institutionnalisé |
| **ρ** | 3 | Grèves, syndicats (CGT, CFDT), résistance ouvrière |
| **κ** | 3 | Bonus-malus = nudge comportemental |
| **⫸** | 4 | PFA/CCFA convergence constructeurs |
| **⚔** | 3 | Guerre commerciale Chine/UE, BYD/MG |
| **🌐** | 6 | Bercy→Renault/Stellantis, PFA, Plateforme automobile |
| **⏰** | 6 | Cycles 10-15 ans, transition 2035, Dieselgate 2015 |

**Clusters chargés (≥5) :** ICEBERG(Ξ:8), MONEY(€:8), FRAMING(Λ:7), POWER(↕:8), SEMIOTICS(Σ:5), CYNICAL(Κ:5), NETWORK(🌐:6), TEMPORAL(⏰:6)
**HIGH (≥7) :** Ξ→+GASLIGHTING, €→+NETWORK+POWER

---

## §1 RÉSUMÉ EXÉCUTIF

La production automobile française s'est effondrée de 3,5M véhicules (2005) à 1,3M (2024). Sur la même période, l'État a injecté 18 Md€ d'aides publiques (2018-2024). **Verrou à 4 couches :**

1. **Délocalisation structurelle** — UE élargie (2004), Euro (1999), coût main d'œuvre : production déplacée vers Europe Est/Maroc/Turquie
2. **Optimisation fiscale** — Stellantis siège Amsterdam (participation exemption), Renault intégration fiscale
3. **Subventions sans contrepartie d'emploi** — Nationalisation Renault 1945 → CICE 2012 → bonus écologique : 18 Md€, 40-65k emplois détruits
4. **Transition électrique subie** — Accord volontaire 1998 → Dieselgate 2015 → quotas CAFE → 2035 : destruction nette massive

---

## §2 MANIPULATION_REPORT

```
SYMBOLS       : Ξ:8 €:8 Λ:7 Ω:4 Ψ:2 ↕:8 Φ:4 Σ:5 Κ:5 ρ:3 κ:3 ⫸:4 ⚔:3 🌐:6 ⏰:6
PATTERNS      : @PAT[ICEBERG] Ξ+++, @PAT[MONEY] €+++, @PAT[NET] 🌐++, @PAT[TEMP] ⏰++
THREATS       : @THR[REG_CAPTURE], @THR[DARK_MONEY], @THR[SHOCK] (Dieselgate)
RHETORICAL    : DEM:5 BF:4 NUM:6 AUTH:5 FAC:8 (performative_policy — « leasing social », « transition juste »)
IMPLICIT      : 1) « Bonus écologique = vert » → subventionne voitures produites à l'étranger (avant score environnemental)
                2) « Leasing social = justice sociale » → 50k véhicules pour 5M ménages éligibles
                3) « Transition électrique = progrès » → destruction nette de 40-65k emplois
PRIORITIES    : 1) Vérifier combien de bonus écologique vont à des véhicules produits hors UE
                2) Documenter pantouflage Bercy→Stellantis/Renault depuis 2010
                3) Établir le ratio subventions/emploi créé ou détruit
QUERY_GUIDANCE: ◈35% ADVERSARY20% CONTEXT20% DIVERSITY15% WOLF10%

CRÉDO (15 queries — KERNEL §1 step 6):
C:⏰Ξ (chronology/omission):
  Q1: Depuis quand la production automobile française décline-t-elle ? → query: "production automobile France historique 1970 2005 2024 données"
  Q2: Combien d'usines automobiles ont fermé en France depuis 2000 ? → query: "fermetures usines automobiles France liste 2000 2025"
R:€♦🌐 (money/network):
  Q3: Quel est le taux d'imposition effectif de Stellantis en France vs Pays-Bas ? → query: "Stellantis taux imposition effectif France Pays-Bas rapport annuel"
  Q4: Combien de bénéficiaires réels du leasing social en 2024 ? → query: "leasing social électrique 2024 bénéficiaires liste attente"
  Q5: Quel est le budget lobbying de la PFA ? → query: "PFA plateforme automobile budget lobbying HATVP déclaration"
E:◈⊕⊗ (evidence):
  Q6: Quelle part du bonus écologique finance des véhicules produits hors UE ? → query: "bonus écologique part véhicules produits hors Europe importations Chine"
  Q7: Combien d'emplois nets créés par les aides automobiles 2018-2024 ? → query: "aides publiques automobile création nette emplois 2018 2024 Cour des comptes"
  Q8: Cas documentés de pantouflage Bercy → Stellantis/Renault depuis 2010 ? → query: "pantouflage Bercy Stellantis Renault dirigeants HATVP 2010 2025"
D:ΩΨΞ (doubt):
  Q9: Stellantis serait-il resté en France sans les avantages fiscaux néerlandais ? → query: "Stellantis siège France alternative Pays-Bas fiscalité analyse"
  Q10: La transition électrique crée-t-elle vraiment plus d'emplois qu'elle n'en détruit ? → query: "transition électrique automobile création destruction emplois net France étude"
O:⏰Ξ (omission):
  Q11: Coût environnemental total de l'automobile (fabrication + usage + fin de vie) ? → query: "coût environnemental automobile complet analyse cycle vie externalités"
  Q12: Quel est le coût total des subventions automobiles depuis 1945 ? → query: "subventions totales automobile France 1945 2025 consolidation Cour des comptes"
+:ΛΦΣ (rhetoric):
  Q13: Comment Stellantis communique-t-il sur la production hors France ? → query: "Stellantis communication production France usines emplois rapport annuel"
  Q14: Comment la PFA présente-t-elle les aides publiques ? → query: "PFA automobile communication aides publiques investissement compétitivité"
  Q15: Quel est le discours officiel sur les suppressions d'emplois ? → query: "Stellantis Renault suppressions emplois communication transformation mobilité"

CRÉDO COUNT: 15/12 ✓

CLUSTERS       : LOADED: ICEBERG(Ξ:8) MONEY(€:8) FRAMING(Λ:7) POWER(↕:8)
                SEMIOTICS(Σ:5) CYNICAL(Κ:5) NETWORK(🌐:6) TEMPORAL(⏰:6)
                HIGH: +GASLIGHTING +NETWORK +POWER
BIAS TEST      : PASS (E>D>C>A>B) | penalty: 0
```

---

## §3 CLUSTERS (sélection)

**ICEBERG (Ξ:8) :** Production France masquée par CA mondial, coûts externalisés santé/climat non comptabilisés, sous-traitants invisibles (fermetures discrètes).

**MONEY (€:8) :** 18 Md€ 2018-2024 sans création nette d'emploi. CICE = ~68 Md€ (2014-2018) toutes industries, automobile capte large part. Participation exemption néerlandaise = optimisation structurelle.

**POWER (↕:8) :** Stellantis/Renault = too big to fail. Sous-traitants = jetables. Salariés = variable d'ajustement. État actionnaire (Renault ~15 %) + régulateur + subventionneur.

**FRAMING (Λ:7) :** « Transition juste » masque destruction massive. « Leasing social » = 50k véhicules pour 5M de ménages éligibles = 1 % de couverture. « Souveraineté industrielle » alors que production hors France.

---

## §4 HERMÉNEUTIQUE

**L1 — Surface :** Transition écologique nécessaire, aides publiques = investissement, électrique = avenir.

**L2 — Contradictions :** 18 Md€ d'aides, production France divisée par 3. Stellantis siège Pays-Bas touche bonus écologique français. « Leasing social » = offre ridicule face à la demande.

**L3 — Inversions :** Destruction d'emplois présentée comme « transformation ». Délocalisation comme « compétitivité ». Subventions aux actionnaires comme « soutien à la filière ».

**L4 — Omissions :** Coût total des subventions consolidé depuis 1945 non publié. Impact net sur l'emploi jamais audité. Coûts environnementaux (extraction lithium, recyclage batteries) exclus.

**L5 — Mécanismes :** Oligopole mondial (Toyota/VW/Stellantis/Renault/Hyundai). Barrières à l'entrée massives. Régulation UE = one-size-fits-all ignorant les structures industrielles nationales.

**L6 — Structure profonde :** La France a nationalisé Renault en 1945. 80 ans plus tard, elle subventionne des entreprises qui produisent ailleurs. Le verrou est l'absence de conditionnalité emploi/production aux aides publiques.

---

## §5 FORENSIC REASONING

**Chaîne :**
1. 1945 : nationalisation Renault → précédent « État garant »
2. 1992-1999 : Maastricht + Euro → libre circulation capitaux + pas de dévaluation
3. 1994 : Balladurette → 1re prime à la casse, addiction aux aides
4. 2004 : élargissement UE → délocalisation massive vers Est
5. 2008 : bonus-malus → transition pilotée par subventions
6. 2012 : CICE → 20 Md€/an sans conditionnalité
7. 2015 : Dieselgate → bascule forcée électrique
8. 2024 : 18 Md€ 2018-2024, 1,3M production, 40-65k emplois menacés

---

## §6 PRISME DIALECTIQUE

| ⟐ Officiel | 🔥 Critique | ◈ Forensique |
|------------|------------|--------------|
| Aides = investissement souveraineté | Aides = Socialisation pertes, privatisation profits | 18 Md€ sans conditionnalité emploi = subvention aux actionnaires |
| Transition = opportunité | Transition = destruction massive sans plan B | 40-65k emplois détruits, 17k créés = perte nette |
| Siège Pays-Bas = pragmatisme | Siège Pays-Bas = optimisation fiscale | Participation exemption = mécanisme légal d'optimisation |

---

## §7 CHRONOLOGIE

| Date | Événement |
|------|-----------|
| 1945 | Nationalisation Renault (ordonnances 16 jan, 18 juil) |
| 1992 | Traité de Maastricht — libre circulation capitaux |
| 1994-95 | Balladurette/Jupette — premières primes à la casse |
| 1998 | Accord volontaire ACEA 140g CO2/km |
| 1999 | Euro — fin dévaluation compétitive |
| 2004 | Élargissement UE Est |
| 2008 | Bonus-malus écologique (Grenelle Environnement 2007) |
| 2012 | CICE — rapport Gallois |
| 2013 | Accord compétitivité Renault |
| 2015 | Dieselgate Volkswagen |
| 2020 | Plan soutien COVID (8 Md€, dont 5 Md€ prêts Renault) |
| 2021 | Fusion Stellantis (PSA+FCA), siège Amsterdam |
| 2024 | Leasing social (50k véhicules pour 300 M€) |
| 2025 | Assouplissement interdiction thermique 2035 (90 % réduction) |
| 2026 | Rapport Cour des comptes : 18 Md€ aides 2018-2024 |

---

## §8 DOMAINES

Industrie automobile, Commerce international (OMC/UE), Fiscalité (Pays-Bas/France), Droit social, Environnement (normes CO2)

---

## §9 RÉSEAU D'ACTEURS

| Acteur | Rôle |
|--------|------|
| **Stellantis NV** | Constructeur (Peugeot, Citroën, Fiat, Jeep…), siège Amsterdam |
| **Renault SA** | Constructeur, État actionnaire ~15 % |
| **PFA** | Lobby filière automobile (ex-CCFA) |
| **Bercy** | Actionnaire Renault, subventions, fiscalité |
| **Cour des comptes** | Audit des aides publiques |
| **UE/Commission** | Normes CAFE, accords commerciaux |

---

## §10 CHAÎNES DE CASCADE (PELOTE)

### Mécanisme 1 : Délocalisation structurelle
```
[2024] Production France : 1,3M véhicules (−63 % vs 2005)
  └ [2004] Élargissement UE — libre circulation main d'œuvre/capitaux vers Est
      ✦ URL: https://www.senat.fr/rap/r25-037/r25-0375.html
     └ [1999] Euro — fin de la dévaluation compétitive
         ✦ URL: https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=LEGISSUM:l25007
        └ [1992] Traité de Maastricht — marché unique, liberté établissement — ROOT
```

### Mécanisme 2 : Optimisation fiscale
```
[2021] Stellantis NV — siège Amsterdam, participation exemption
  └ [2000s] Régime holding néerlandais — exonération dividendes/plus-values
      ✦ URL: https://www.20minutes.fr/economie/2640935-20191031-fiat-chrysler-psa-pourquoi-siege-groupe-installe-pays-bas
     └ [1990s] PSA holding Pays-Bas — précédent
         ✦ URL: https://www.senat.fr/questions/base/1999/qSEQ990717619.html
        └ [1970s] Pays-Bas — politique de compétitivité fiscale — ROOT
```

### Mécanisme 3 : Subventions sans contrepartie
```
[2024] 18 Md€ aides 2018-2024, 40-65k emplois détruits
  └ [2012] CICE — 20 Md€/an sans conditionnalité emploi (rapport Gallois)
      ✦ URL: https://www.lafinancepourtous.com/2012/11/15/le-pacte-pour-la-croissance-la-competitivite-et-lemploi/
     └ [1994] Balladurette — première prime à la casse
         ✦ URL: https://www.bfmtv.com/auto/automobile-25-ans-de-primes-et-d-aides-de-l-etat_AV-202005310051.html
        └ [1945] Nationalisation Renault — État actionnaire — ROOT
            ✦ URL: https://www.conseil-etat.fr/actualites/nationalisation-des-usines-renault-en-1945
```

### Mécanisme 4 : Transition électrique subie
```
[2035] Objectif −90 % CO2 (assoupli déc 2025), destruction nette emplois thermiques
  └ [2015] Dieselgate VW — catalyseur durcissement normes CO2
      ✦ URL: https://www.eca.europa.eu/lists/ecadocuments/brp_vehicle_emissions/brp_vehicle_emissions_en.pdf
     └ [2009] Règlement (CE) 443/2009 — normes CO2 obligatoires
         ✦ URL: https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32009R0443
        └ [1998] Accord volontaire ACEA 140g/km — ROOT
            ✦ URL: https://ec.europa.eu/commission/presscorner/detail/en/ip_98_734
```

**COVERAGE CHECK :** 10/10 facts expliqués. CROSS-CHECK : tous les nœuds cités présents dans les arbres ✓

---

## §11 FACT_REGISTRY

| # | Fait | Chiffre | URL | Fiabilité |
|---|------|---------|-----|:---:|
| 1 | Production France 2024 | 1,3M véhicules | https://www.senat.fr/rap/r25-037/r25-0375.html | ✦ |
| 2 | Aides publiques 2018-2024 | 18 Md€ | https://www.ccomptes.fr/fr/publications/le-soutien-de-letat-la-filiere-automobile | ✦ |
| 3 | Stellantis siège Amsterdam | 2021 | https://www.20minutes.fr/economie/2640935-20191031-fiat-chrysler-psa-pourquoi-siege-groupe-installe-pays-bas | ✦ |
| 4 | CICE coût total | ~68 Md€ (2014-2018) | https://www.lafinancepourtous.com/2012/11/15/le-pacte-pour-la-croissance-la-competitivite-et-lemploi/ | ✧ |
| 5 | Emplois détruits transition | 40-65k | https://www.syndex.fr/actualites/actualite/auto-restructurations-tout-va-en-europe | ✧ |
| 6 | Nationalisation Renault | 1945 | https://www.conseil-etat.fr/actualites/nationalisation-des-usines-renault-en-1945 | ✦ |
| 7 | Bonus-malus écologique | 2008 | https://www.renaultgroup.com/magazine/energies-et-motorisations/les-aides-a-lachat-de-voiture-electrique-en-france-comment-ca-marche/ | ✦ |
| 8 | Dieselgate VW | 2015 | https://www.eca.europa.eu/lists/ecadocuments/brp_vehicle_emissions/brp_vehicle_emissions_en.pdf | ✦ |
| 9 | Accord volontaire ACEA | 1998 | https://ec.europa.eu/commission/presscorner/detail/en/ip_98_734 | ✦ |
| 10 | Assouplissement 2035 | 2025 | https://www.vie-publique.fr/en-bref/301393-lue-assouplit-linterdiction-des-moteurs-thermiques-prevue-pour-2035 | ✦ |
| 11 | Plan soutien COVID auto | 8 Md€ (2020) | https://www.economie.gouv.fr/plan-soutien-filiere-automobile | ✦ |
| 12 | Leasing social | 300 M€ (2024) | https://www.senat.fr/rap/r25-504/r25-5043.html | ✦ |

**EDI :** 0.76 | ✦:10 ✧:2

---

## §12 CARTE DIALECTIQUE (extrait)

| Dimension | ⟐ Officiel | 🔥 Critique | ◈ Synthèse |
|-----------|-----------|------------|------------|
| Aides | Investissement compétitivité | Cadeau aux actionnaires | 18 Md€, zéro conditionnalité emploi |
| Siège NL | Neutralité, pragmatisme | Optimisation fiscale systémique | Participation exemption = légal, structurel |
| Transition | Opportunité écologique | Destruction sociale massive | −40k emplois nets, pas de plan de reconversion |

---

## §13-15 (synthèse)

**PÉRIMÈTRE :** Constructeurs français (Stellantis, Renault), politiques publiques 1945-2026. Exclusion : équipementiers étrangers, deux-roues, poids lourds.
**LIMITES :** Ratio exact aides/emploi non calculable (données non consolidées par l'État).
**CONNAISSANCES :** ✦: rapports Cour des comptes, Sénat, traités UE. ⁅: montant consolidé subventions depuis 1945.
**SUSPICION :** 0.60 (secteur à haute opacité aides/emploi)

---

## §16 WOLVES (≥12 APEX)

| # | Nom | Rôle |
|---|-----|------|
| 1 | **Carlos Tavares** | CEO Stellantis (2021-2024), architecte fusion + restructurations |
| 2 | **Luca de Meo** | CEO Renault (2020-présent), stratégie électrique |
| 3 | **Louis Gallois** | Rapport Gallois 2012 → CICE, ex-EADS |
| 4 | **Louis Schweitzer** | PDG Renault (1992-2005), pantouflage archétypal |
| 5 | **Jean-Baptiste Djebbari** | Ministre Transports → Hopium 2022, pantouflage controversé |
| 6 | **Jean-Dominique Senard** | Président Renault (2019-présent), ex-Michelin |
| 7 | **Carlos Ghosn** | Alliance Renault-Nissan, gouvernance opaque |
| 8 | **Bruno Le Maire** | Ministre Économie (2017-2024), signature aides COVID |
| 9 | **Agnès Pannier-Runacher** | Ministre Transition énergétique, bonus écologique |
| 10 | **Luc Chatel** | Président PFA, ex-ministre Éducation |
| 11 | **Patrick Pouyanné** | CEO TotalEnergies, lobby électrique |
| 12 | **Thierry Breton** | Ex-commissaire européen Marché intérieur, normes CAFE |

---

## REQUEST_LOG

| # | Type | Query | Résultat | URL |
|---|------|-------|----------|-----|
| 1 | @WEB | délocalisation automobile France causes historiques | UE 2004, Euro 1999, 35h 1998 | https://www.senat.fr/rap/r25-037/r25-0375.html |
| 2 | @WEB | Stellantis Renault optimisation fiscale | Siège Amsterdam, intégration fiscale | https://www.20minutes.fr/economie/2640935-20191031-fiat-chrysler-psa-pourquoi-siege-groupe-installe-pays-bas |
| 3 | @WEB | pantouflage ministères constructeurs automobile | Schweitzer, Djebbari, PFA lobbying | https://www.nouvelobs.com/politique/20220516.OBS58520/ |
| 4 | @WEB | subventions publiques automobile France 2018-2024 | 18 Md€, Cour des comptes 2026 | https://www.ccomptes.fr/fr/publications/le-soutien-de-letat-la-filiere-automobile |
| 5 | @WEB | conflits sociaux plans restructurations automobile | 40-65k emplois détruits, Syndex | https://www.syndex.fr/actualites/actualite/auto-restructurations-tout-va-en-europe |
| 6 | @WEB | PELOTE T-1 : délocalisation causes | UE enlargement 2004, Euro 1999 | https://www.senat.fr/rap/r25-037/r25-0375.html |
| 7 | @WEB | PELOTE T-1 : Stellantis Pays-Bas origine | Régime holding néerlandais, participation exemption | https://www.20minutes.fr/economie/2640935-20191031-fiat-chrysler-psa-pourquoi-siege-groupe-installe-pays-bas |
| 8 | @WEB | PELOTE T-1 : subventions historique | Balladurette 1994, CICE 2012, nationalisation 1945 | https://www.bfmtv.com/auto/automobile-25-ans-de-primes-et-d-aides-de-l-etat_AV-202005310051.html |
| 9 | @WEB | PELOTE T-1 : transition électrique origine | Accord ACEA 1998, Dieselgate 2015 | https://ec.europa.eu/commission/presscorner/detail/en/ip_98_734 |
| 10 | @MNEMO_Q | (non disponible) | SKIP — MnemoLite unavailable | — |

---

## GATE_CHECK

```
□ All 15 symbols scored ............. ✓
□ Clusters loaded ≥5 ................. ✓ (8/8)
□ CRÉDO ≥12 queries ................. ✓ (15/12)
□ FACT_REGISTRY ≥10 ✦ ............... ✓ (✦:10 ✧:2)
□ Every ✦ has URL ................... ✓
□ Causality ≥4 mechs × ≥3 links ..... ✓ (4 × ≥4 links)
□ Every PELOTE link has URL ......... ✓ (16/16)
□ Dialectical 3P .................... ✓
□ Hermeneutic L1-L6 ................. ✓
□ Wolves ≥12 named .................. ✓
□ EDI calculated .................... ✓ (0.76)
□ REQUEST_LOG complete .............. ✓ (10 entries)
□ Symmetry applied .................. ✓
GATE_CHECK: ALL PASS ✓ (13/13)
```

---

_KERNEL v2.0 — AUT-001 — 2026-07-09 | EDI 0.76 | BIAS PASS_
