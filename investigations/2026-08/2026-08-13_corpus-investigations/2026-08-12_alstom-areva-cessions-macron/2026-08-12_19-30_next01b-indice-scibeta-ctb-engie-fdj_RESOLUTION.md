# APEX-NEXT-01b : Verification Engie/FDJ dans l'indice SciBeta CTB

- STATE : FINAL
- DATE : 2026-08-12 19:30 CEST
- TYPE : RESOLUTION (KERNEL v2.8)
- SUJET : apex-next01b-indice-scibeta-ctb-engie-fdj
- FCT : 7
- PREREQUIS : 2026-08-12_19-15_next01-frr-erafp-blackrock-engie-fdj_RESOLUTION.md (verdict PARTIEL, chainon manquant identifie)

---

## 0. OBJECT_QUESTION

Verifier si Engie et/ou FDJ sont dans l'indice **Scientific Beta Eurozone Max Sharpe Ratio ERAFP SRI Carbon Efficient Index** (indice CTB que replique le mandat Lot 2 ERAFP confie a BlackRock le 23/11/2023).

---

## 1. FACT_REGISTRY (7 FCT)

| FCT-next01b-01 | Nom complet de l'indice : Scientific Beta Eurozone Max Sharpe Ratio ERAFP SRI Carbon Efficient Index (lance en 2016 pour l'ERAFP) | -- | Scientific Beta, RAFP CP 26/05/2016 |
| FCT-next01b-02 | Fournisseur : Scientific Beta (EDHEC Risk Institute, cree 2012) | -- | Yahoo Finance, Scientific Beta |
| FCT-next01b-03 | Composition complete de l'indice NON PUBLIQUE : acces restreint aux clients de Scientific Beta via plateforme securisee | -- | Scientific Beta Terms of Service |
| FCT-next01b-04 | BlackRock ne publie pas la composition de l'indice dans ses rapports publics | -- | Constat |
| FCT-next01b-05 | L'ERAFP mentionne l'indice mais n'en publie pas la composition dans ses rapports annuels | -- | RAFP |
| FCT-next01b-06 | L'indice est conforme au reglement CTB (UE 2019/2089) : decarbonation -7 %/an, -30 % intensite carbone initiale, obligation d'inclure les secteurs a fort impact climatique | -- | Scientific Beta |
| FCT-next01b-07 | Indices comparables (MSCI EMU SRI) incluent Engie. FDJ est generalement incluse dans les indices ESG/SRI europeens (absence controverse majeure). | -- | Amundi, Interactive Brokers |

---

## 2. VERDICT

### Verification directe

**IMPOSSIBLE.** La composition de l'indice Scientific Beta ERAFP n'est pas publique. Elle est accessible uniquement aux clients de Scientific Beta (ERAFP, BlackRock) via une plateforme securisee.

### Verification indirecte (proxys)

**Engie** : quasi certainement dans l'indice. Le reglement CTB OBLIGE a inclure les « secteurs a fort impact climatique » (High Climate Impact Sectors, classification NACE). Les utilities/energies renouvelables en font partie. Engie, entreprise de transition energetique, est dans les indices comparables (MSCI EMU SRI).

**FDJ** : probablement dans l'indice ou dans un indice comparable. FDJ est generalement eligible aux indices ESG/SRI (pas d'exclusion pour controverse majeure). Mais le jeu d'argent n'est pas un secteur CTB prioritaire.

### Verdict

| Question | Verdict |
|---|---|
| Engie est-elle dans l'indice SciBeta CTB de l'ERAFP ? | **TRES PROBABLE (non verifiable directement).** Obligation reglementaire CTB + presence dans indices comparables. |
| FDJ est-elle dans l'indice SciBeta CTB de l'ERAFP ? | **PROBABLE (non verifiable directement).** Eligible aux indices ESG/SRI, mais pas de certitude. |
| Le chainon « mandat ERAFP/BlackRock -> Engie » est-il confirme ? | **PLAUSIBLE mais non confirme.** L'indice est CTB, Engie est dans les indices CTB comparables. |
| Le chainon « mandat ERAFP/BlackRock -> FDJ » est-il confirme ? | **FAIBLE.** FDJ n'a pas de raison forte d'etre dans un indice CTB (pas un secteur climat). |

---

## 3. CONSEQUENCES POUR LE CORPUS

### APEX-NEXT-01 reaffirme

Le verdict du document 19-15 est confirme : le double circuit est PARTIEL, l'intention NON PROUVEE. Le chainon manquant (composition de l'indice) reste non verifiable sans acces client Scientific Beta.

**Seule l'ERAFP (ou BlackRock, ou Scientific Beta) peut confirmer la presence d'Engie/FDJ dans l'indice.**

### Recommandation

**Fermer la piste.** La verification directe est impossible en OSINT. Le faisceau est suffisamment documente pour conclure que le circuit est plausible mais structurel (mecanique indicielle, pas corruption). Une QE parlementaire a l'ERAFP demandant la composition publique de l'indice permettrait de trancher.

---

*APEX-NEXT-01b -- 7 FCT, verdict UNVERIFIABLE (proprietaire), proxies ENGIE probable, FDJ faible. Chaine du double circuit non confirmable en OSINT. 12 aout 2026, 19:30 CEST.*
