# CORRUPTION_CORE — Corpus anticorruption France (10-12 août 2026)

## Ce que contient ce ZIP

Matière analytique et données structurées du corpus anticorruption Truth Engine. Tous les fichiers d'investigation, synthèses, registres, matrices de faits, données structurées et résultats de scraping. Les pièces primaires lourdes (PDF, dumps) sont dans CORRUPTION_SOURCES.zip.

## Arborescence

```
truth-engine/
├── README.md                          <- ce fichier
├── knowledge.md                       <- règles du projet, éthique, formatage
├── AGENTS.md                          <- règles globales agents
├── truth-engine-v2/                   <- KERNEL v2.8, protocoles, templates
│   ├── KERNEL.md                      <- pipeline d'investigation (TEXT_ANALYSIS → PELOTE → FACT_REGISTRY)
│   ├── protocol/                      <- protocoles INVESTIGATION, PERSO_FRESQUE, UPDATE
│   ├── forensic/                      <- GATES, REQUEST_LOG
│   ├── definitions/                   <- SYMBOLS.md, grille 3 axes
│   └── search/                        <- EPISTEMIC.md, TEMPLATES.md
├── tools/                             <- scripts Python d'audit et d'extraction
│   ├── audit_phase1_sublimator_v35.py
│   ├── audit_phase2_sublimator_v37.py
│   ├── audit_ric_mapping.py
│   ├── fetch_canoniques.py
│   ├── compare_v1_v2.py
│   └── extract_synthesis_data.py
├── investigations/2026-08/2026-08-13_corpus-investigations/
│   ├── 2026-08-10_run2-enr/           <- DOSSIER PRINCIPAL 1 : ENR, 89 docs, ~1 043 FCT
│   ├── 2026-08-11_corpus-anticorruption/ <- DOSSIER PRINCIPAL 2 : ICEBERG MAX, 32 docs, 451 FCT
│   ├── 2026-08-12_buzyn-vaccination-enfants/ <- DOSSIER PRINCIPAL 3 : Buzyn, 5 docs, 50 FCT
│   ├── 2026-08-10_preparation-anticorruption/ <- doctrine et préparation méthodologique
│   └── 2026-08-09_enrichissement-legalise-france/ <- cadre théorique légal ≠ légitime
└── outputs/                           <- articles et réponses publiés antérieurement
```

## Points d'entrée recommandés (ordre de lecture)

### Niveau 1 — Synthèses globales

1. `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-12_12-15_synthese-massive-2-jours_SYNTHESE.md`
   Synthèse massive des 2 jours. 15 découvertes majeures, 5 mécanismes, invariant transversal.
2. `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/2026-08-12_11-30_point-consolide-final_SYNTHESE.md`
   Synthèse finale run2-ENR. 7 découvertes, verdict 3 axes.
3. `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-11_corpus-anticorruption/2026-08-12_10-15_point-consolide-final_SYNTHESE.md`
   Synthèse finale ICEBERG MAX. 16 pistes, 7 découvertes.
4. `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-11_corpus-anticorruption/2026-08-12_13-00_iceberg-max-v4_REGISTRE.md`
   REGISTRE v4. État des 16 pistes, 3 invariants.

### Niveau 2 — Dossiers par thématique

**ENR / Capture réglementaire :**
- `2026-08-10_run2-enr/RUN_MANIFEST.md` — inventaire complet des 89 documents
- `2026-08-10_run2-enr/2026-08-11_17-14_fil-pantouflage-regulateurs-enr-v2_REGISTRE.md` — synthèse pantouflage
- `2026-08-10_run2-enr/2026-08-10_21-39_point-valeco-enbw-consolide_REGISTRE.md` — fil Valeco/EnBW

**ICEBERG MAX / 16 secteurs :**
- `2026-08-11_corpus-anticorruption/2026-08-12_12-50_p1-p8-v3_INVESTIGATION.md` — P1-P8 approfondies (49 FCT)
- `2026-08-11_corpus-anticorruption/2026-08-12_13-15_gaps-p1-p8-resolus_RESOLUTION.md` — GAPs P1-P8 résolus (26 FCT)
- `2026-08-11_corpus-anticorruption/2026-08-12_09-40_gap1-registre-administrateurs-ca_RESOLUTION.md` — 0 registre CA publics
- `2026-08-11_corpus-anticorruption/2026-08-12_09-55_gap2-croisement-ca-5-operateurs_RESOLUTION.md` — ANDRA=EDF+CEA

**Buzyn / Vaccination :**
- `2026-08-12_buzyn-vaccination-enfants/2026-08-12_06-00_buzyn-vaccination-obligatoire_INVESTIGATION.md` — enquête APEX complète

### Niveau 3 — Méthodologie

- `truth-engine-v2/KERNEL.md` — pipeline complet
- `truth-engine-v2/protocol/INVESTIGATION.md` — protocole d'investigation
- `knowledge.md` — règles éthiques, formatage, conventions

## Convention de nommage

`YYYY-MM-DD_HH-MM_<sujet>_<TYPE>.md`

Types : INVESTIGATION, RESOLUTION, REGISTRE, SYNTHESE, QUESTION, APPLICATION

## Format des faits (FCT)

Chaque fait est préfixé `FCT-<prefix>-NNN` et contient source, date, fiabilité.
Les FCT sont regroupés dans des tables de faits (FACT_REGISTRY) au sein des documents.

## Grille de vérification

Pour chaque claim :
1. `FCT → pièce source → contexte → contre-preuve → qualification → conclusion`
2. 3 axes : pénal / légal / légitime
3. EPI : FACT ≠ EVIDENCE ≠ INFERENCE ≠ HYPOTHESIS ≠ SPECULATION ≠ UNKNOWN

## Fichiers CONTREDIT et anomalies

Les documents marqués `ERRATA` ou `CORRECTION` contiennent des invalidations de claims antérieurs :
- `2026-08-11_14-50_gap1-26-incompatibilites-hatvp_INVESTIGATION.md` : errata 2024-294 (AAI mal identifiée)
- `2026-08-10_21-36_gap1-affectations-valeco-ren_RESOLUTION.md` : correction dividendes 31,3 M€ vs 7,52 M€

Les GAPs marqués `OSINT IMPOSSIBLE` ou `SECRET INSTRUCTION` documentent les limites de l'enquête.

## Chiffres clés du corpus

| Dossier | Docs | FCT | Objet |
|---|---|---|---|
| run2-ENR | 89 | 1 043 | Capture rente ENR, pantouflage, opacité |
| ICEBERG MAX | 32 | 451 | 16 secteurs anticorruption |
| Buzyn | 5 | 50 | Vaccination obligatoire 2017 |
| Autres | 3 | 43 | Doctrine, cadre théorique |
| **TOTAL** | **~129** | **~1 466** (cross-dossier unique) | |

## Ce qui n'est PAS dans ce ZIP

- Pièces lourdes (PDF, dumps) → CORRUPTION_SOURCES.zip
- Caches, logs techniques, fichiers temporaires
- Doublons exacts
- /tmp/ (fichiers de session)
- book/ (sous-module git du livre)
- pilote-avenants-sesn/data/ (1,9 GB de DECP JSON)

---

*Corpus produit par Buffy (Freebuff, deepseek-v4-pro) et Giak. KERNEL v2.8. 10-12 août 2026.*
