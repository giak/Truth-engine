# Quintessence : CIR — taux réels vs théorique, effet d'aubaine des grandes entreprises

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-09_cir-taux-retour-effet-aubaine/2026-08-09_22-42_cir-taux-retour-effet-aubaine_INVESTIGATION.md` (364 lignes, 16 FCT-001..016)
Date extraction : 2026-08-13 07:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, bloc 09-*)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format léger, axe anticorruption, bloc niches fiscales (CIR)
- **Date source** : 2026-08-09 22:42 CEST, STATE FINAL
- **Identifiants source** : 16 FCT-001..016, 5 CLM-001..005, 4 CONTR-001..004, 4 CAU-001..004
- **Object** : confronter le taux théorique du CIR (6,25 % à 2 Md€) aux ratios publiés de l'Annexe 12 (4,32 à 13,66 %) et tester l'effet d'aubaine des grandes entreprises
- **Verdict source** : l'effet d'aubaine GE est un faisceau agrégé (IPP/CNEPI + CdC convergents), pas une preuve individuelle ; la tension de périmètre (base éligible vs R&D comptable) rend tout arbitrage public indécidable en rigueur

## 2. Faits atomiques préservés

- FCT-001 : Taux CIR : 30 % sur dépenses ≤ 100 M€, 5 % au-delà (CGI 244 quater B, LF 2008) ; taux effectif théorique pour 2 Md€ : 6,25 % (30 + 95 = 125 M€) [L197 (mesuré)]
- FCT-002 : CIR STMicro : 119 M€ pour 871 M€ de R&D = 13,66 % (ratio ~2× le théorique) [L198 (mesuré)]
- FCT-003 : CIR Safran : 152 M€ pour 2 000 M€ = 7,60 % [L199 (mesuré)]
- FCT-004 : CIR Renault : 133,9 M€ pour 2 000 M€ = 6,70 % [L200 (mesuré)]
- FCT-005 : CIR Thales : 171 M€ pour 2 520 M€ = 6,79 % [L201 (mesuré)]
- FCT-006 : CIR Sanofi : 108 M€ pour 2 500 M€ = 4,32 % [L202 (mesuré)]
- FCT-007 : R&D comptable Thales 2024 : 1 273,7 M€ (compte de résultat) — vs 2 520 M€ base annexe (écart ×2) [L203 (mesuré)]
- FCT-008 : R&D comptable Safran 2024 : 1 980 M€ totales (1 348 autofinancées) — cohérent avec la base annexe 2 000 M€ [L204 (mesuré)]
- FCT-009 : R&D comptable STMicro 2024 : 2 077 M$ (~1 900 M€, mondial) — vs 871 M€ base annexe [L205 (mesuré)]
- FCT-010 : R&D comptable Sanofi 2024 : ~7,4 Md€ — vs 2 500 M€ base annexe (écart ×3) [L206 (mesuré)]
- FCT-011 : R&D comptable 2024 des 3 autres : Stellantis ~5,7 Md€, Michelin ~700-800 M€, ArcelorMittal ~300-335 M$ [L207 (mesuré)]
- FCT-012 : IPP 2019 (Bozio et al.) : 1 € de CIR → 1,3-1,5 € de R&D supplémentaire (multiplicateur), effet 15-18 % [L208 (mesuré)]
- FCT-013 : IPP n° 33 / CNEPI 06/2021 : effets causals significatifs pour TPE/PME ; AUCUN effet causal documenté pour les grandes entreprises [L209 (mesuré)]
- FCT-014 : Rendement brevet par M€ de CIR : 1,165 pour les TPE vs 0,464 pour les grandes entreprises (2,5×) [L210 (mesuré)]
- FCT-015 : CdC 07/2023 : recommande le recentrage du CIR sur les PME (note « Piloter et évaluer les dépenses fiscales ») [L211 (mesuré)]
- FCT-016 : Cumul CIR des 8 groupes de l'annexe : 827,5 M€ ≈ 10,7 % du CIR national (~7,7 Md€) — calcul [L212 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : DGFiP, MESR, Sénat (commission d'enquête n° 808), IPP (Bozio, Cottet, Py), CNEPI, Cour des comptes.
**Entreprises** : STMicroelectronics, Safran, Renault, Thales, Sanofi, Stellantis, Michelin, ArcelorMittal.

## 4. Sources externes citées

CGI art. 244 quater B + BOFiP BOI-BIC-RICI-10-10-30-10, MESR fiche CIR 2025, Sénat 808 Annexe 12 (01/07/2025), Thales états financiers 2024, Safran résultats 2024, STMicro Form 20-F 2025, Sanofi rapports financiers 2024, Stellantis rapport annuel 2024, Michelin DEU 2024, ArcelorMittal rapport annuel 2024, IPP 03/2019, IPP n° 33/CNEPI 06/2021, CdC note 07/2023.

## 5. Chronologie datée

2008 : LF 2008 (taux CIR) ; 03/2019 : IPP évaluation d'impact ; 06/2021 : CNEPI ; 07/2023 : CdC ; 01/07/2025 : Annexe 12 ; 02-04/2025 : publications des comptes 2024 des 8 groupes.

## 6. Mécanismes / chaînes causales

**M1 : Le CIR en volume favorise structurellement les gros volumes** : taux 30 %/5 % avec seuil 100 M€ ; le taux décroît avec la taille (6,25 % à 2 Md€) mais le volume croît plus vite — les GE captent les montants absolus les plus élevés (171 M€ Thales) ; 8 groupes ≈ 827,5 M€ cumulés. Type : STRUCTUREL. Force : HAUTE. [L170-L171 (mesuré)]
**M2 : L'effet d'aubaine est concentré sur les grandes entreprises au niveau agrégé** : IPP/CNEPI 2021 : aucun effet causal GE vs effets PME ; rendement brevet GE 2,5× inférieur ; les R&D des GE existaient indépendamment du CIR (inférence agrégée, pas par groupe). Type : STATISTIQUE. Force : HAUTE au niveau agrégé, NON individuel. [L173-L174 (mesuré)]
**M3 : La tension de périmètre empêche l'arbitrage public** : Annexe 12 = base éligible ? R&D comptables = autre base ; ratios 13,66 % vs ~6,3 % pour STMicro selon la base ; sans normalisation, tout débat « qui profite du CIR » est indécidable en rigueur. Type : MÉTHODOLOGIQUE. Force : HAUTE. [L176-L177 (mesuré)]
**M4 (rejetée) : « Les grands groupes fraudent le CIR »** : réfutée — aucun fait pénal documenté ; la question est l'effet d'aubaine (légal), pas la fraude. [L179 (mesuré)]

## 7. Verbatim et citations

- « Le taux théorique du CIR pour un grand groupe est ~6,25 % : 30 % × 100 M€ + 5 % × 1 900 M€ = 125 M€ / 2 000 M€ (CGI 244 quater B). » [CLM-001, L187 (mesuré)]
- « Les ratios Annexe 12 sont hétérogènes (4,32 à 13,66 %) : STMicro 13,66 %, Sanofi 4,32 %, Thales 6,79 %. » [CLM-002, L188 (mesuré)]
- « L'absence de preuve ≠ preuve d'absence (l'IPP note des limites) ; l'aubaine reste une inférence agrégée. » [CONTR-004, L221 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : FCT-001 à 010 = ✦ (sources primaires : CGI/BOFiP, comptes 2024, Annexe 12) ; FCT-011 = ✧ ; FCT-016 = ⁂ calcul encadré.
- **F-##** : 16/16 identifiants FCT-001..016 préservés verbatim.
- **Contradictions documentées** : CONTR-001 à 003 (tensions de base STMicro/Thales/Sanofi) résolues comme différences de périmètre (éligible France vs R&D monde) ; CONTR-004 borne le verdict (absence de preuve ≠ preuve d'absence).
- **Méthode** : croisement Annexe 12 × comptes 2024, calculs de ratios sur deux bases, revue des évaluations causales (IPP/CNEPI).

## 9. Limites connues (case-limites)

- Les bases exactes de l'Annexe 12 (éligible vs périmètre groupe France) ne sont pas explicitées par le Sénat — la tension de périmètre demeure.
- Le rendement brevet (FCT-014) provient du CNEPI ; la méthode n'est pas détaillée ici.
- EDI mesuré : 0.6725 (BROAD) ; perspective des 8 groupes (défense du CIR, bénéfices d'innovation réels) absente du corpus.
- FCT-011 (3 groupes) repose sur des sources ✧ (macrotrends, rapports annuels via agent).
