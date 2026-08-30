# XQ204E — BAT forensique final post-rollback — 25 août 2026

## Verdict

**PASS_WITH_BOUNDS**

Cible : **Substack**. La passe D mobile-first est rejetée comme régression visuelle/YAGNI. Les figures de publication ont été restaurées exactement depuis XQ203, puis le BAT a été relancé.

## Candidat

- `QUINTESSENCE_ARTICLE_FACTCHECK_TRUST_XQ204_2026-08-25.md`
- SHA-256 : `0ddd1ab44ff314d10b49be90036c360374727a2b5f6f1bb64f7e26ad6e051b4e`
- Sources : 113/113
- Appels de citation : 187
- Citations orphelines : 0
- Cibles relatives manquantes : 0

## Gates

- [x] `article_sources_113_contiguous`
- [x] `all_113_sources_used`
- [x] `no_orphan_citations`
- [x] `relative_targets_exist`
- [x] `emdash_zero`
- [x] `endash_zero`
- [x] `five_canonical_figure_refs`
- [x] `no_mobile_or_rejected_article_ref`
- [x] `10_figures_byte_identical_xq203`
- [x] `5_svgs_xml_valid`
- [x] `5_pngs_2400x1500`
- [x] `repair_case_count_synced`
- [x] `fresque_count_synced`
- [x] `sqlite_integrity_ok`
- [x] `sqlite_pass_d_rejected_traced`
- [x] `afp_bound_preserved`
- [x] `fact_furious_bound_preserved`

## Figures

- `FIG_01_VERIFICATION_ET_LABEL.png` : PASS, identique XQ203
- `FIG_01_VERIFICATION_ET_LABEL.svg` : PASS, identique XQ203
- `FIG_02_CONTINUUM_EPISTEMIQUE.png` : PASS, identique XQ203
- `FIG_02_CONTINUUM_EPISTEMIQUE.svg` : PASS, identique XQ203
- `FIG_03_MODELE_AU_SLOGAN_X12.png` : PASS, identique XQ203
- `FIG_03_MODELE_AU_SLOGAN_X12.svg` : PASS, identique XQ203
- `FIG_04_CORRECTION_CONTEXTUALISATION_REPARATION.png` : PASS, identique XQ203
- `FIG_04_CORRECTION_CONTEXTUALISATION_REPARATION.svg` : PASS, identique XQ203
- `FIG_05_FALSIFICATION_REPARATION.png` : PASS, identique XQ203
- `FIG_05_FALSIFICATION_REPARATION.svg` : PASS, identique XQ203

10/10 fichiers canoniques sont identiques octet pour octet à XQ203. Les variantes D restent archivées dans `annexes/rejected/XQ204_PASS_D_VISUAL_REGRESSION/` et ne sont pas utilisées par l’article.

## Lisibilité

- Blocs de prose : 239
- Médiane : 45 mots
- >100 mots : 10
- >120 mots : 0
- Maximum : 119 mots

## Données et traçabilité

- Registre de réparation : 6 cas.
- Fresque : 45 événements.
- SQLite : `integrity_check = ok`.
- Findings XQ204 : 17.
- Findings D explicitement rejetés/supplantés : 3.
- Gap mobile : `CLOSED_NOT_REQUIREMENT`.

## Double-check externe ciblé

- Yahoo 23/07/2021 : modélisation Pasteur et prudence — **confirmé**.
- *Conspiracy Watch* : mise à jour du 16/04/2020 distinguant la fuite accidentelle — **confirmé**.
- AFP Bridle : note d’édition du 29/06/2021 — **confirmé** ; formulation antérieure non retrouvée.
- EPI-PHARE 2025 : 527 564 éligibles ; 130 338 exposés ; OR 0,98 ; IC 95 % 0,93-1,04 — **confirmé**.

## Bornes ouvertes

1. AFP Bridle : formulation exacte avant le 29/06/2021.
2. *Fact & Furious* pharmacovigilance : original complet et historique de correction.

## Gate

`PASS_WITH_BOUNDS / READY_FOR_HUMAN_SUBSTACK_PUBLICATION_REVIEW`
