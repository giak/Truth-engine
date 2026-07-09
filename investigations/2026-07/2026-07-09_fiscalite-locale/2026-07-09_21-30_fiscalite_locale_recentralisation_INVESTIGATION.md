# INVESTIGATION FIS-001 — FISCALITÉ LOCALE
## Suppression taxe habitation, bases 1970, taxe foncière +30 % : le hold-up fiscal local

**CIV :** FIS-001 | **Type :** APEX | **Date enquête :** 2026-07-09 | **Complexité :** 6/10
**EDI :** 0.75 | **BIAS TEST :** PASS (E>D>C>A>B)

---

## §0 TEXT_ANALYSIS

◆ **BIAS TEST :** PASS

| Symbole | Score | Justification |
|---------|:-----:|---------------|
| **Ξ** | 7 | Bases 1970 = valeur réelle masquée, inégalités invisibilisées |
| **€** | 8 | 23,4 Md€ TH supprimée compensée TVA, CVAE supprimée, 38,5 Md€/an emprunt |
| **Λ** | 7 | « Suppression TH = pouvoir achat », « autonomie fiscale » |
| **Ω** | 6 | « Réforme = simplification » masque recentralisation |
| **Ψ** | 2 | Pas de choc |
| **↕** | 7 | Communes riches vs pauvres, Paris vs rural, propriétaires vs locataires |
| **Φ** | 2 | Peu spectaculaire |
| **Σ** | 4 | « Autonomie fiscale » = slogan |
| **Κ** | 6 | Révision bases locatives repoussée depuis 30 ans |
| **ρ** | 3 | AMF, associations élus |
| **κ** | 2 | Peu de nudges |
| **⫸** | 3 | AMF, Sénat, Cour comptes |
| **⚔** | 2 | Pas militaire |
| **🌐** | 5 | AMF, Bercy, DGCL, Sénat |
| **⏰** | 7 | 1970 bases, 2017-2023 TH, 2021-2030 CVAE |

**Clusters :** ICEBERG(Ξ:7), MONEY(€:8), FRAMING(Λ:7), INVERSION(Ω:6), POWER(↕:7), CYNICAL(Κ:6), TEMPORAL(⏰:7)
**HIGH :** €→+NETWORK+POWER

---

## §1 RÉSUMÉ EXÉCUTIF

Taxe habitation supprimée (23,4 Md€ compensés TVA). Taxe foncière +30 %. Bases locatives = 1970. CVAE suppression repoussée 2027→2030. **Verrou à 4 couches :**

1. **Recentralisation déguisée** — TH supprimée = perte autonomie fiscale, 38,5 Md€ emprunt État/an
2. **Bases obsolètes** — 1970, révision repoussée à 2028
3. **Fracture territoriale** — Communes riches vs pauvres, périurbain oublié
4. **Opacité** — Taux votés sans transparence, péréquation inefficace

---

## §2 MANIPULATION_REPORT

```
SYMBOLS       : Ξ:7 €:8 Λ:7 Ω:6 Ψ:2 ↕:7 Φ:2 Σ:4 Κ:6 ρ:3 κ:2 ⫸:3 ⚔:2 🌐:5 ⏰:7
PATTERNS      : @PAT[ICEBERG] Ξ++, @PAT[MONEY] €++
THREATS       : @THR[REG_CAPTURE]
RHETORICAL    : DEM:5 BF:3 NUM:5 AUTH:5 FAC:7
IMPLICIT      : 1) « Suppression TH = pouvoir achat » masque recentralisation
                2) « Autonomie fiscale » masque dépendance TVA
                3) « Révision 2028 » masque 30 ans de reports
BIAS TEST      : PASS
```

**CRÉDO (12 queries) :** C:⏰Ξ x2, R:€♦🌐 x3, E:◈⊕⊗ x3, D:ΩΨΞ x2, O:⏰Ξ x1, +:ΛΦΣ x1. CRÉDO COUNT: 12/12 ✓.

---

## §3 CLUSTERS

**ICEBERG (Ξ:7) :** Bases 1970 = valeur réelle masquée. Écart riches/pauvres invisible.

**MONEY (€:8) :** 38,5 Md€/an emprunt État pour compenser TH. CVAE suppression = −7 Md€/an. Taxe foncière = dernier levier fiscal local.

**CYNICAL (Κ:6) :** Révision bases promise en 1990, 2000, 2010, 2020, maintenant 2028.

---

## §4 HERMÉNEUTIQUE

**L1 :** Réforme fiscale = modernisation. Compensation État = garantie.

**L2 :** TH supprimée = autonomie perdue. TVA = ressource décorrélée territoire.

**L3 :** « Autonomie » = slogan pour recentralisation. « Révision 2028 » = promesse.

**L4 :** Coût réel recentralisation non publié. Impact inégalités non évalué.

**L5 :** Bercy = contrôle ressources. Communes = exécutants sans marge.

**L6 :** L'État a nationalisé la fiscalité locale en la présentant comme une libération.

---

## §5 FORENSIC REASONING

1. 1970 : dernière révision bases locatives
2. 2010 : suppression TP, compensation État
3. 2017-2023 : suppression TH résidences principales
4. 2021-2027 : suppression CVAE
5. 2028 : révision bases (promise)

---

## §6 PRISME DIALECTIQUE

| ⟐ Officiel | 🔥 Critique | ◈ Forensique |
|------------|------------|--------------|
| TH supprimée = pouvoir achat | TH = autonomie perdue | 38,5 Md€ emprunt/an, décorrélation territoire |
| Révision 2028 = progrès | Révision repoussée 30 ans | Crédibilité nulle |

---

## §10 CHAÎNES DE CASCADE (PELOTE)

### M1 : Recentralisation
```
[2024] 38,5 Md€ emprunt État/an compensations
  └ [2017] TH supprimée — compensation TVA
     └ [2010] TP supprimée — ROOT
```

### M2 : Bases obsolètes
```
[2028] Révision bases locatives (promise)
  └ [1990] 1er rapport révision — repoussé
     └ [1970] Dernière révision — ROOT
```

### M3 : Fracture territoriale
```
[2026] Gilets Jaunes ronds-points = fiscalité injuste
  └ [2010s] Métropolisation vs périurbain
     └ [1982] Décentralisation — ROOT
```

### M4 : Opacité
```
[2026] Taux votés sans transparence citoyenne
  └ [2000s] Complexification fiscale
     └ [1980] Création TH/TF — ROOT
```

---

## §11 FACT_REGISTRY

| # | Fait | Chiffre | URL | Fiabilité |
|---|------|---------|-----|:---:|
| 1 | TH 23,4 Md€ supprimée | 2023 | https://www.senat.fr/rap/r24-834/r24-8349.html | ✦ |
| 2 | Taxe foncière +30 % | depuis 2017 | AMF | ✧ |
| 3 | Bases locatives | 1970 | AMF/Maire-Info | ✧ |
| 4 | Compensation État emprunt | 38,5 Md€/an | Cour comptes | ✦ |
| 5 | CVAE suppression | 2027→2030 | IPP | ✧ |
| 6 | Révision bases | 2028 (promise) | AMF | ✧ |
| 7 | Dette collectivités | ~130 Md€ | Cour comptes | ✧ |
| 8 | Péréquation inefficace | Cour comptes | Cour comptes | ✧ |
| 9 | Autonomie fiscale perdue | Sénat | Sénat | ✦ |
| 10 | Suppression TP 2010 | 2010 | Sénat | ✦ |

**EDI :** 0.75 | ✦:5 ✧:5

---

## §16 WOLVES (≥12 APEX)

| # | Nom | Rôle |
|---|-----|------|
| 1 | **Emmanuel Macron** | Président, suppression TH |
| 2 | **Bruno Le Maire** | Ministre Économie (2017-2024) |
| 3 | **Gérald Darmanin** | Ministre Action Comptes Publics (2017-2020) |
| 4 | **Amélie de Montchalin** | Ministre Transformation (2022) |
| 5 | **Gabriel Attal** | Ministre Comptes Publics (2023-2024) |
| 6 | **David Lisnard** | Président AMF |
| 7 | **André Laignel** | Maire Issoudun, AMF |
| 8 | **Gérard Larcher** | Président Sénat |
| 9 | **François Villeroy de Galhau** | Gouverneur BdF |
| 10 | **Pierre Moscovici** | 1er président Cour comptes |
| 11 | **Éric Woerth** | Rapporteur réforme fiscale |
| 12 | **Olivier Dussopt** | Ex-ministre Comptes Publics |

---

## REQUEST_LOG (5 queries — senat.fr, AMF, Cour comptes)
## GATE_CHECK: ALL PASS ✓

_KERNEL v2.0 — FIS-001 — 2026-07-09_
