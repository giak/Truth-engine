# Audit automatisé Phase 1 Sublimator v35 : n=42 + 1 LEGACY

**Date :** 2026-07-08  
**Méthodologie :** 6 critères objectifs (C1, C2, C5, C6, C7, C10) + scoring binaire 1/0.5/0 sur 6 points max.  
**C3 (zéro em-dash) NEUTRALISÉ 2026-07-08** : scope originel = articles (Phase 3), pas fiches internes (Phase 1 quintessence). Champ `n_em_dash` reste tracké informativement. Cf. docstring pour note scope complète.
**Critères subjectifs exclus :** C4 (Refus Phase 1), C8 (Fidélité citations), C9 (Pas de jugement) ; réservés à l'audit manuel échantillonné (cf. n=6).  
**Critère C10** : strict = match exact des 9 noms canoniques ; lenient = tolérance de la variante §9 « Limites (case-limites) ».

---

## 1. Synthèse globale n=42 canoniques

- **Total fichiers canoniques :** 120
- **Score strict moyen :** 5.98 / 6.0
- **Score lenient moyen :** 5.98 / 6.0

### 1.1 Taux par critère (canoniques)

| Critère | ✅ | ⚠️ | ❌ | Taux OK strict | Taux OK+Warn |
|---------|----|----|----|----------------|---------------|
| **C1** | 120 | 0 | 0 | 100.0% | 100.0% |
| **C2** | 120 | 0 | 0 | 100.0% | 100.0% |
| **C3** | 20 | 0 | 100 | 16.7% | 16.7% |
| **C5** | 120 | 0 | 0 | 100.0% | 100.0% |
| **C6** | 115 | 5 | 0 | 95.8% | 100.0% |
| **C7** | 120 | 0 | 0 | 100.0% | 100.0% |
| **C10** | 120 | 0 | 0 | 100.0% | 100.0% |
| **C10_strict** | 120 | 0 | 0 | 100.0% | 100.0% |
| **Δ Source** | 98 | 22 | 0 | 81.7% | 100.0% |

## 2. Tableau détaillé (42 canoniques)

| Fichier | C1 | C2 | C3* | C5 | C6 | C7 | C10 (strict) | C10 (variant §9) | Δ Source | Score strict |
|---------|----|----|-----|----|----|----|---------------|--------------------|----------|---------------|

*C3 = zéro em-dash, NEUTRALISÉ (informatif uniquement, hors score).*

*Δ Source = contrôle Delta Source-Quintessence (v2026-07-08) : compare les F-## source vs quintessence. ❌ si fabrication détectée.*

| `2026-08-13_01-00_alstom-areva-cessions-macron_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_angle1-chaine-valeco-enbw_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_avenants-5-grands-projets_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_buzyn-vaccination-obligatoire_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_corruption-systemique-france_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_cumcum-cumex-france_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_decoupe-actifs-strategiques_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_flux-subvention-pdv-mecanique-prix_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_p1-p8-v3_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_p11-fraude-cpf-v2_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_run4-autoroutes-aeroports-flamanville_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_01-00_run5-speculation-fonciere-dvf_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_02-00_cre-ppe2-concentration_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_02-00_pantouflage-energie_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_02-00_run2-enr-premices_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_02-00_spv-beneficiaires-effectifs_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_02-15_collectivites-autorisations_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_02-15_dividendes-valeco-enbw-capitaux-oa_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_02-15_gap1-puech-del-vert_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_02-15_gap1-qui-a-ecrit-la-regle-oa_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_angle-a-decp-construction-parcs_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_angle-b-chaines-autorisation_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_angle-c-puech-cornet_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_eolien-mer-tarifs-laureats_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_gap1-26-incompatibilites-hatvp_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_gap1b-parcs-valeco-tarn_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_gap2-arguments-cre-ministere-collecte_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_gap2-scan-598-compatibilites-reserves_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_gap3-ardian-semiconductor-enr_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_03-00_gap4-contrefactuel-prix-2022_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_03-00_gap4-extension-autres-aai_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_next-a1-sdem-soregies_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_next-a2-spv-cada-marches-pdv_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_03-00_surremunerations-enr-croisement_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_vp1-elus-proprietaires-fonciers-tarn_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_03-00_vp2-gouvernance-ser_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_03-00_vp4-pantouflage-cre-enr_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_cartographie-pantouflage-hatvp_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p1-p8-v2_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p10-jo2024-solideo-btp_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p11-fraude-cpf_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p12-cabinets-conseil-it_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p12-cabinets-it-v2_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p13-subventions-associations-v2_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p13-subventions-associations_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p14-nominations-croisees-v2_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p14-nominations-croisees_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | 5.5/6 |
| `2026-08-13_04-00_p15-agences-etat-v2_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p15-agences-etat_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p9-p10-v2_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_p9-speculation-fonciere-plu_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_04-00_preparation-investigations-corruption_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_05-00_bndp-acces-exceptionnel_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_casd-referentiel-dmtg-bndp_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_cdc-acces-donnees-fiscales_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_convention-cdc-dgfip-bndp_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_correlation-8-projets-dmtg_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_css-projets-dmtg-dutreil_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_dates-habilitation-taxopti-evrefis_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_decision-ou-defaut-arret-dmtg_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_decret-2023-520-acces-donnees_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_demande-cada-convention-bndp_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_montage-ribecourt-v3_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_statistiques-successorales-europe_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_taxopti-evrefis-publications-dmtg_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_tome2-auditions-commission_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_trou-circulation-cdc-insee_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-00_verif-3-publications-fiche-dmtg_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | 5.5/6 |
| `2026-08-13_05-30_blast-oxfam-centile-dutreil_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_05-30_criteres-rattachement-casd_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-30_notes-france-strategie-dmtg_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | 5.5/6 |
| `2026-08-13_05-30_outputs-ipp-dmtg-hors-fiche_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-30_reponse-bercy-dutreil-absente_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_05-30_resolution-contr001-cdc-dutreil_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | 5.5/6 |
| `2026-08-13_06-00_bndp-absente-rapport-3056_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_06-00_confite-disparition_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_06-00_financement-base-successions_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_06-00_qe11677-bndp-eenregistrement_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_06-00_resolution-gap003b-senat760-corps_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_06-00_resolution-gap004-oxfam-pdf_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_06-30_architectes-banques-conseils_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_06-30_archives-commission-deontologie_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_06-30_archives-nationales-commission-deontologie_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_06-30_avis-hatvp-vincent-renault_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_06-30_base-hatvp-mobilites_quintessence.md` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_base-donnees-successions-eenregistrement_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_beneficiaires-niches-cessions_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_chiffrage-mandats-banques-conseils_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_cir-taux-retour-effet-aubaine_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_cjip-cumcum-banques_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_07-00_consolidation-ecarts-cession_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_corruption-systemique-france_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_croisement-directeurs-cessions_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_decisionnaire-edf-opa-2022_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_dutreil-110-donataires_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_07-00_effectivite-anti-cumcum-lf2025_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_enrichissement-legalise-france_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_07-00_grille-ief-photonis-latecoere_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_liste-decret-2020-69-saisine-obligatoire_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_07-00_mandat-rothschild-fdj_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_plf-2026-dutreil-reforme-a-minima_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_resolution-gap002-bollore-operation2024_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_07-00_revolving-doors-ape-bercy_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-00_suite-pnf-azema_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-30_axe4-filiere-archeologie_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_07-30_bilan-connaissance-patrimoniale_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_07-30_commission-courson-matthei_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_07-30_surfacturation-commande-publique_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_07-30_transparence-citoyenne-lerois_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_08-00_gonflement-moe-sesn_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_08-00_pap156-ligne-base-plf2027_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_08-00_pilote-sesn-phase10_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_08-00_point-controle-reponse-3056_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_08-00_protocole-plf2027-rec7_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_08-30_apex-max-faisceaux-additionnels_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_08-30_iceberg-max-alstom-areva_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 6.0/6 |
| `2026-08-13_08-30_impact-exclusions-dutreil-dmtg_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_08-30_note-axe1-niches-fiscales_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | 5.5/6 |
| `2026-08-13_08-30_rec-10-12-plf-2027_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |
| `2026-08-13_08-30_taxe-holdings-20pct_quintessence.md` | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 6.0/6 |

## 4. Patterns de déviation

- **C10 strict = ❌** : 0/42 = 0.0%
- **C10 strict = ⚠️** : 0/42 = 0.0%
- **C7 = ❌** (ni Verbatim ni Notes canoniques) : 0/42 = 0.0%

## 5. Distribution des noms H2 réels (top patterns)

- `## 1. Métadonnées & trace source` : 120 occurrences
- `## 3. Acteurs nominaux` : 120 occurrences
- `## 4. Sources externes citées` : 120 occurrences
- `## 5. Chronologie datée` : 120 occurrences
- `## 6. Mécanismes / chaînes causales` : 120 occurrences
- `## 7. Verbatim et citations` : 120 occurrences
- `## 8. Notes méthodologiques source` : 120 occurrences
- `## 9. Limites connues (case-limites)` : 120 occurrences
- `## 2. Faits atomiques préservés` : 116 occurrences
- `## 2. Faits atomiques préservés (sélection chiffrée)` : 2 occurrences
- `## 2. Faits atomiques préservés (extraction du croisement)` : 1 occurrences
- `## 2. Faits atomiques préservés (FACT_REGISTRY)` : 1 occurrences
