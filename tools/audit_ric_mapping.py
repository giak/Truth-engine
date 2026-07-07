#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_ric_mapping.py

Outil d'audit reproductible pour le dossier RIC Saison 2 (2026-07-04-RIC).

Remplace un script antérieur qui matchait INVESTIGATION et quintessences par
substring normalisé. Ce substring ne captait pas correctement
`cnr_1944_democratie_economique` (faux négatif) et produisait de fausses
alertes « 12 fichiers manquants » alors que 42/42 existaient réellement.

Le mapping est désormais EXPLICITE : chaque ligne est écrite à la main,
aucune heuristique algorithmique. Garantit la reproductibilité des audits
multi-saisons.

Pilot Phase 1 KISS v1.0 canonique (cf. knowledge.md) :
    - 0 em-dash (U+2014, octets UTF-8 0xe2 0x80 0x94)
    - Sections H2 numérotées `## 1.` à `## 9.` (≥8 sections)
    - Refus Phase 1 strict (pas d'angle propre, pas de thèse ajoutée)

Modes CLI :
    list       Affiche le mapping 42/42 (sujet → INVESTIGATION → quintessence)
    coverage   Vérifie la couverture 1-à-1 du mapping
    audit      Vérifie la conformité Phase 1 KISS v1.0 de chaque quintessence
    full       audit + coverage + rapport de statut multi-domaines

Usage :
    python tools/audit_ric_mapping.py list
    python tools/audit_ric_mapping.py coverage
    python tools/audit_ric_mapping.py audit
    python tools/audit_ric_mapping.py full
    python tools/audit_ric_mapping.py -d investigations/2026-07-04-RIC audit

Exit code : 0 si 42/42 conformes, 1 sinon.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional

# ============================================================
# CONSTANTES
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DOSSIER = PROJECT_ROOT / "investigations" / "2026-07-04-RIC"
DEFAULT_INVESTIGATION_DIR = DEFAULT_DOSSIER
DEFAULT_QUINTESSENCE_DIR = DEFAULT_DOSSIER / "_quintessence"

# Pilot Phase 1 KISS v1.0 canonique (cf. knowledge.md)
EM_DASH_BYTES = b"\xe2\x80\x94"  # U+2014 « — »
MIN_H2_SECTIONS = 8               # Sections `## 1.` à `## 8.` (puis §9 Limites recommandé)
# Marqueur Phase 1 dans le header : on accepte plusieurs variantes observees sur le
# corpus. Leudit strict exige « Phase 1 KISS » (canonique) ; on accepte aussi
# « Phase 1 : Sublimator v40 v2 KISS » (variante pratique).
PHASE1_MARKER_PATTERNS = (
    re.compile(r"Phase\s*1\s*[Kk][Ii][Ss][Ss]"),       # « Phase 1 KISS » ou « Phase 1 Kiss »
    re.compile(r"Phase\s*1\s*:[^\n]*v40\s*v2\s*KISS"), # « Phase 1 : Sublimator v40 v2 KISS »
)

# ============================================================
# DATACLASSES
# ============================================================


@dataclass
class QuintessenceMapping:
    """Une entrée du mapping : un sujet canonique lie son INVESTIGATION a sa quintessence."""

    subject_canonique: str
    investigation: str  # basename du fichier INVESTIGATION
    quintessence: str   # basename du fichier quintessence Phase 1 KISS v1.0 canonique
    p3_number: str      # ex: "P3 #22" ou "n/a" si pas indexé P3
    domaine: str        # ex: "Anti-RIC verrous P0"
    batch: str          # ex: "Batch 7", "Phase 1 KISS v1.0 canonique"


@dataclass
class LegacyEntry:
    """Fichier LEGACY present dans `_quintessence/` mais hors-canonique Phase 1 KISS v1.0."""

    filename: str
    canonical_subject: str           # sujet canonique auquel il correspond
    reason: str                      # raison HORS-CANONIQUE


@dataclass
class AuditResult:
    """Résultat d'audit pour une quintessence."""

    mapping: QuintessenceMapping
    quintessence_exists: bool
    em_dash_count: int
    h2_sections_found: list[int]
    phase1_marker_present: bool
    residuels: list[str] = field(default_factory=list)
    statut: str = ""      # ✅ / ⚠️ / ❌


# ============================================================
# MAPPING EXPLICITE 42/42 (RIC Saison 2 2026-07-04)
# ============================================================
#
# Chaque ligne est écrite à la main. NE PAS inverser l'ordre des champs.
# NE PAS appliquer d'heuristique sur les noms de fichiers.
# Si un nouveau fichier est produit, AJOUTER une ligne ci-dessous explicitement.
#
# TOTAL = 42 entrées (1 par INVESTIGATION file de la racine 2026-07-04-RIC/).

MAPPING: list[QuintessenceMapping] = [
    # ----------------------------------------------------------
    # P1 + P5S : Mouvement RIC + comparaison étrangère (3 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="referendum_initiative_citoyenne",
        investigation="2026-07-04_18-00_referendum_initiative_citoyenne_INVESTIGATION.md",
        quintessence="2026-07-07_referendum_initiative_citoyenne_quintessence.md",
        p3_number="P3 #7",
        domaine="Mouvement RIC (cadre juridique initial)",
        batch="Phase 1 KISS v1.0 canonique (Batch 9b)",
    ),
    QuintessenceMapping(
        subject_canonique="ppl_ric_timeline_exhaustive",
        investigation="2026-07-04_23-30_ppl_ric_timeline_exhaustive_INVESTIGATION.md",
        quintessence="2026-07-07_ppl_ric_timeline_exhaustive_quintessence.md",
        p3_number="P3 #10",
        domaine="Verrous/coordination (PPL timeline)",
        batch="Phase 1 KISS v1.0 canonique (Batch 1)",
    ),
    QuintessenceMapping(
        subject_canonique="m5s_italie_capture_democratie_directe",
        investigation="2026-07-04_22-00_m5s_italie_capture_democratie_directe_INVESTIGATION.md",
        quintessence="2026-07-07_m5s_italie_capture_democratie_directe_quintessence.md",
        p3_number="P3 #6",
        domaine="Comparaison étrangère (Italie M5S)",
        batch="Phase 1 KISS v1.0 canonique (Batch 1)",
    ),

    # ----------------------------------------------------------
    # P0 : Anti-RIC verrous (4 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="ric_bce_euro_verrou",
        investigation="2026-07-04_19-30_ric_bce_euro_verrou_INVESTIGATION.md",
        quintessence="2026-07-07_ric_bce_euro_verrou_quintessence.md",
        p3_number="P3 #1",
        domaine="Anti-RIC verrous P0 (verrou monétaire BCE/Euro)",
        batch="Phase 1 KISS v1.0 canonique (Batch 9b)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_bloc_religieux_verrou",
        investigation="2026-07-04_20-30_ric_bloc_religieux_verrou_INVESTIGATION.md",
        quintessence="2026-07-07_ric_bloc_religieux_verrou_quintessence.md",
        p3_number="P3 #2",
        domaine="Anti-RIC verrous P0 (verrous religieux + läicité)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_morts_politiques_verrou",
        investigation="2026-07-04_21-30_ric_morts_politiques_verrou_INVESTIGATION.md",
        quintessence="2026-07-07_ric_morts_politiques_verrou_quintessence.md",
        p3_number="P3 #3",
        domaine="Anti-RIC verrous P0 (morts politiques artificielles)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_verrous_impersonnels",
        investigation="2026-07-04_22-00_ric_verrous_impersonnels_INVESTIGATION.md",
        quintessence="2026-07-07_ric_verrous_impersonnels_quintessence.md",
        p3_number="P3 #4",
        domaine="Mécanisme verrous (verrous impersonnels)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),

    # ----------------------------------------------------------
    # Verrous/coordination (3 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="ric_complement_gaps",
        investigation="2026-07-04_20-00_ric_complement_gaps_INVESTIGATION.md",
        quintessence="2026-07-07_ric_complement_gaps_quintessence.md",
        p3_number="P3 #9",
        domaine="Verrous/coordination (complément gaps P2-P3)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_cross_examination",
        investigation="2026-07-04_23-50_cross_examination_ric_INVESTIGATION.md",
        quintessence="2026-07-07_ric_cross_examination_quintessence.md",
        p3_number="P3 #8",
        domaine="Verrous/coordination (cross-examination RIC)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_coordination_europeenne",
        investigation="2026-07-04_22-30_ric_coordination_europeenne_INVESTIGATION.md",
        quintessence="2026-07-07_ric_coordination_europeenne_quintessence.md",
        p3_number="P3 #5",
        domaine="Mécanisme verrous (coordination européenne anti-RIC)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),

    # ----------------------------------------------------------
    # Outils RIC P2 (8 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="conventions_citoyennes_ric_contraignant",
        investigation="2026-07-05_01-30_conventions_citoyennes_ric_contraignant_CONV-CIT-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_conventions_citoyennes_ric_contraignant_quintessence.md",
        p3_number="P3 #12",
        domaine="Outils RIC P2 (conventions citoyennes contraignantes)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="infrastructure_electorale_privee",
        investigation="2026-07-05_00-30_infrastructure_electorale_privee_INFRA-ELEC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_infrastructure_electorale_privee_quintessence.md",
        p3_number="P3 #14",
        domaine="Outils RIC P2 (infrastructure électorale privée)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_protocole_pnred",
        investigation="2026-07-05_11-00_protocole_pnred_ric_001_PROTOCOLE-PNRED-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_protocole_pnred_quintessence.md",
        p3_number="P3 #15",
        domaine="Outils RIC P2 (protocole PNRED)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_lois_civictech_fr_2027",
        investigation="2026-07-05_12-00_lois_civictech_fr_2027_LOIS-CIVICTECH-2027_INVESTIGATION.md",
        quintessence="2026-07-07_ric_lois_civictech_fr_2027_quintessence.md",
        p3_number="P3 #16",
        domaine="Outils RIC P2 (lois CivicTech France 2027)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_levier_cedh_article_3_p1",
        investigation="2026-07-05_01-00_levier_cedh_article_3_p1_CEDH-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_levier_cedh_article_3_p1_quintessence.md",
        p3_number="n/a",
        domaine="Mécanisme verrous (levier CEDH art. 3 P1)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_revocatoire_recall_anti_capture",
        investigation="2026-07-05_09-00_ric_revocatoire_recall_anti_capture_REVOCATOIRE-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_revocatoire_recall_anti_capture_quintessence.md",
        p3_number="n/a",
        domaine="Outils RIC P2 (RIC révocatoire / recall)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_sortition_tirage_au_sort",
        investigation="2026-07-05_08-00_sortition_tirage_au_sort_democratie_deliberative_SORTITION-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_sortition_tirage_au_sort_quintessence.md",
        p3_number="n/a",
        domaine="Outils RIC P2 (sortition / tirage au sort délibératif)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_democratie_numerique_open_source",
        investigation="2026-07-05_10-00_democratie_numerique_open_source_decidim_DECIDIM-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_democratie_numerique_open_source_quintessence.md",
        p3_number="n/a",
        domaine="Outils RIC P2 (démocratie numérique open source Decidim)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),

    # ----------------------------------------------------------
    # Profil/sociologique/média P3 (5 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="hauts_fonctionnaires_bloqueurs",
        investigation="2026-07-05_00-00_hauts_fonctionnaires_bloqueurs_HFB-FR-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_hauts_fonctionnaires_bloqueurs_quintessence.md",
        p3_number="P3 #11",
        domaine="Profil/sociologique/média P3 (hauts fonctionnaires bloqueurs)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="profil_sociologique_electorat_ric",
        investigation="2026-07-05_03-00_profil_sociologique_electorat_ric_SOCIO-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_profil_sociologique_electorat_quintessence.md",
        p3_number="P3 #13",
        domaine="Profil/sociologique/média P3 (profil électeur RIC)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="cadrage_media_hostile_ric",
        investigation="2026-07-05_04-00_cadrage_media_hostile_ric_MEDIA-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_cadrage_media_hostile_ric_quintessence.md",
        p3_number="n/a",
        domaine="Profil/sociologique/média P3 (cadrage médiatique hostile)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="indifference_priorite_ric",
        investigation="2026-07-05_06-00_indifference_priorite_ric_vrai_verrou_INDIF-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_indifference_priorite_ric_quintessence.md",
        p3_number="n/a",
        domaine="Profil/sociologique/média P3 (indifférence = vrai verrou)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="lobbies_cabinets_conseils_ric",
        investigation="2026-07-05_02-00_lobbies_cabinets_conseils_ric_LOBBY-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_lobbies_cabinets_conseils_quintessence.md",
        p3_number="n/a",
        domaine="Profil/sociologique/média P3 (lobbies + cabinets conseils)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),

    # ----------------------------------------------------------
    # Histoire longue + CNR + IVe République (3 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="histoire_longue_ric_1789_2026",
        investigation="2026-07-05_15-00_histoire_longue_ric_france_1789_2026_INVESTIGATION.md",
        quintessence="2026-07-07_ric_histoire_longue_1789_2026_quintessence.md",
        p3_number="P3 #19",
        domaine="Histoire longue RIC (1789-2026)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="cnr_1944_democratie_economique",
        investigation="2026-07-05_16-00_cnr_1944_democratie_economique_INVESTIGATION.md",
        quintessence="2026-07-07_ric_cnr_1944_democratie_economique_quintessence.md",
        p3_number="P3 #20",
        domaine="Histoire longue RIC (CNR 1944 démocratie économique)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="referendums_ive_republique_1946_1958",
        investigation="2026-07-05_16-30_referendums_ive_republique_1946_1958_INVESTIGATION.md",
        quintessence="2026-07-07_ric_referendums_ive_republique_1946_1958_quintessence.md",
        p3_number="P3 #21",
        domaine="Histoire longue RIC (référendums IVe République)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),

    # ----------------------------------------------------------
    # Comparaison étrangère (1 entrée ; M5S Italie déjà compté ci-dessus)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="bavierr_verfassung_1946_volksentscheide",
        investigation="2026-07-05_17-00_bavierr_art_71_75_verfassung_1946_volksentscheide_INVESTIGATION.md",
        quintessence="2026-07-08_bavierr_verfassung_1946_volksentscheide_quintessence.md",
        p3_number="P3 #29",
        domaine="Comparaison étrangère (Bavière Verfassung 1946)",
        batch="Phase 1 KISS v1.0 canonique (Batch 6)",
    ),

    # ----------------------------------------------------------
    # Société civile : syndicats, cultes, dette (3 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="syndicats_cgt_cfdt_fo_charte_amiens_1906",
        investigation="2026-07-05_17-30_syndicats_cgt_cfdt_fo_charte_amiens_1906_INVESTIGATION.md",
        quintessence="2026-07-08_syndicats_cgt_cfdt_fo_charte_amiens_1906_quintessence.md",
        p3_number="P3 #30",
        domaine="Société civile (syndicats CGT/CFDT/FO + Charte Amiens 1906)",
        batch="Phase 1 KISS v1.0 canonique (Batch 6)",
    ),
    QuintessenceMapping(
        subject_canonique="cultes_4_religions_france_position_ric",
        investigation="2026-07-05_18-00_cultes_4_religions_france_position_RIC_INVESTIGATION.md",
        quintessence="2026-07-08_cultes_4_religions_france_position_ric_quintessence.md",
        p3_number="P3 #31",
        domaine="Société civile (4 cultes France position RIC)",
        batch="Phase 1 KISS v1.0 canonique (Batch 6)",
    ),
    QuintessenceMapping(
        subject_canonique="dette_publique_art_50_tue_frexit_ric",
        investigation="2026-07-05_18-30_dette_publique_art_50_tue_frexit_RIC_INVESTIGATION.md",
        quintessence="2026-07-08_dette_publique_art_50_tue_frexit_ric_quintessence.md",
        p3_number="P3 #32",
        domaine="Société civile (dette art. 50 TUE / frexit / RIC)",
        batch="Phase 1 KISS v1.0 canonique (Batch 6)",
    ),

    # ----------------------------------------------------------
    # Période crise (1 entrée)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="ric_periode_crise_ukraine_covid",
        investigation="2026-07-05_19-00_ric_periode_crise_ukraine_covid_INVESTIGATION.md",
        quintessence="2026-07-08_ric_periode_crise_ukraine_covid_quintessence.md",
        p3_number="P3 #33",
        domaine="Période crise (Ukraine + COVID)",
        batch="Phase 1 KISS v1.0 canonique (Batch 6)",
    ),

    # ----------------------------------------------------------
    # Domaines spécifiques (7 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="sondages_ifop_ipsos_methodologie_ric",
        investigation="2026-07-05_19-30_sondages_ifop_ipsos_methodologie_ric_INVESTIGATION.md",
        quintessence="2026-07-07_ric_sondages_ifop_ipsos_methodologie_quintessence.md",
        p3_number="P3 #22",
        domaine="Domaines spécifiques (sondages IFOP/IPSOS méthodologie)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_crypto_dao_aragon_snapshot_blockchain",
        investigation="2026-07-05_20-00_ric_crypto_dao_aragon_snapshot_blockchain_INVESTIGATION.md",
        quintessence="2026-07-07_ric_crypto_dao_aragon_snapshot_blockchain_quintessence.md",
        p3_number="P3 #23",
        domaine="Domaines spécifiques (RIC crypto DAO Aragon/Snapshot)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_urgence_climatique_cop_giec",
        investigation="2026-07-05_20-30_ric_urgence_climatique_cop_giec_scenarios_INVESTIGATION.md",
        quintessence="2026-07-07_ric_urgence_climatique_cop_giec_quintessence.md",
        p3_number="P3 #24",
        domaine="Domaines spécifiques (urgence climatique COP/GIEC)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="chronologie_6_presidents_ric_effectif",
        investigation="2026-07-05_21-00_chronologie_6_presidents_ric_effectif_INVESTIGATION.md",
        quintessence="2026-07-07_ric_chronologie_6_presidents_quintessence.md",
        p3_number="P3 #25",
        domaine="Domaines spécifiques (chronologie 6 présidents RIC effectif)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="franc_maconnerie_loges_tradition_republicaine",
        investigation="2026-07-05_21-30_franc_maconnerie_loges_tradition_republicaine_INVESTIGATION.md",
        quintessence="2026-07-08_ric_franc_maconnerie_loges_quintessence.md",
        p3_number="P3 #26",
        domaine="Domaines spécifiques (franc-maçonnerie loges tradition républicaine)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="ric_ia_generative_meta_reflexion",
        investigation="2026-07-05_22-00_ric_ia_generative_meta_reflexion_INVESTIGATION.md",
        quintessence="2026-07-08_ric_ia_generative_meta_reflexion_quintessence.md",
        p3_number="P3 #27",
        domaine="Domaines spécifiques (RIC + IA générative méta-réflexion)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),
    QuintessenceMapping(
        subject_canonique="sol_dem_financement_symetrie",
        investigation="2026-07-04_23-50_sol_dem_financement_symetrie_INVESTIGATION.md",
        quintessence="2026-07-08_sol_dem_financement_symetrie_quintessence.md",
        p3_number="P3 #28",
        domaine="Solutions (SOL-DEM financement symétrique)",
        batch="Phase 1 KISS v1.0 canonique (Batch 7)",
    ),

    # ----------------------------------------------------------
    # Audit externe juridique (2 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="verification_independante",
        investigation="2026-07-05_13-00_verification_independante_p3_16_VERIFICATION-2026-07_INVESTIGATION.md",
        quintessence="2026-07-07_ric_verification_independante_quintessence.md",
        p3_number="n/a",
        domaine="Audit juridique externe (vérification indépendante P3 #16)",
        batch="Phase 1 KISS v1.0 canonique (Batch 9b)",
    ),
    QuintessenceMapping(
        subject_canonique="external_legal_audit",
        investigation="2026-07-05_14-00_external_legal_audit_p3_16_p3_18_EXTERNAL-LEGAL-AUDIT-2026-07_INVESTIGATION.md",
        quintessence="2026-07-07_ric_external_legal_audit_quintessence.md",
        p3_number="n/a",
        domaine="Audit juridique externe (legal audit P3 #16 / #18)",
        batch="Phase 1 KISS v1.0 canonique (Batch 9b)",
    ),

    # ----------------------------------------------------------
    # Solutions + référendums locaux (2 entrées)
    # ----------------------------------------------------------
    QuintessenceMapping(
        subject_canonique="strategie_imposition_mise_en_place_ric",
        investigation="2026-07-05_07-00_strategie_imposition_mise_en_place_ric_STRATEGIE-SOLUTIONS-RIC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_strategie_imposition_mise_en_place_ric_quintessence.md",
        p3_number="n/a",
        domaine="Solutions (stratégie imposition mise en place RIC)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
    QuintessenceMapping(
        subject_canonique="referendums_locaux_chaine_manquant",
        investigation="2026-07-05_05-00_referendums_locaux_chaine_manquant_REFER-LOC-001_INVESTIGATION.md",
        quintessence="2026-07-07_ric_referendums_locaux_chaine_manquant_quintessence.md",
        p3_number="n/a",
        domaine="Référendums locaux (chaîne manquante)",
        batch="Phase 1 KISS v1.0 canonique (Batch 5)",
    ),
]


# ============================================================
# ENTREE LEGACY (HORS-CANONIQUE)
# ============================================================
#
# 1 fichier LEGACY existe dans `_quintessence/` mais n'est PAS Phase 1 KISS v1.0
# canonique (structure fondamentalement différente, variante v3 historique).
# Il est déclaré HORS-CANONIQUE et n'est PAS intégré au mapping.

LEGACY_ENTRIES: list[LegacyEntry] = [
    LegacyEntry(
        filename="2026-07-04_18-00_referendum_initiative_citoyenne_dossier_v38.md",
        canonical_subject="referendum_initiative_citoyenne",
        reason="Variante v3 historique (format dossier_v38) ; équivalent Phase 1 KISS v1.0 canonique = 2026-07-07_referendum_initiative_citoyenne_quintessence.md",
    ),
]


# ============================================================
# VALIDATION Phase 1 KISS v1.0 canonique
# ============================================================


def validate_phase1_typed(
    mapping: QuintessenceMapping,
    quintessence_path: Path,
) -> AuditResult:
    """Version typée : validation complète d'une quintessence Phase 1 KISS v1.0 canonique."""
    result = AuditResult(
        mapping=mapping,
        quintessence_exists=False,
        em_dash_count=0,
        h2_sections_found=[],
        phase1_marker_present=False,
    )

    # 1. Existence fichier
    if not quintessence_path.exists():
        result.residuels.append(f"fichier absent : {quintessence_path.name}")
        result.statut = "❌"
        return result
    result.quintessence_exists = True

    raw = quintessence_path.read_bytes()
    txt = raw.decode("utf-8")

    # 2. 0 em-dash (knowledge.md règle stricte)
    em_count = raw.count(EM_DASH_BYTES)
    result.em_dash_count = em_count
    if em_count > 0:
        result.residuels.append(
            f"{em_count} em-dash résiduel (U+2014) : violation knowledge.md"
        )

    # 3. Sections H2 numérotées `## 1.` à `## 8.`
    sections = sorted({
        int(m.group(1))
        for m in re.finditer(r"^## (\d+)\.\s", txt, re.MULTILINE)
    })
    result.h2_sections_found = sections

    # On attend ≥ MIN_H2_SECTIONS et au minimum §1 ET §8 présents.
    if len(sections) < MIN_H2_SECTIONS:
        result.residuels.append(
            f"sections H2 insuffisantes : {len(sections)}/"
            f"{MIN_H2_SECTIONS} trouvées, manquant §{[s for s in range(1, MIN_H2_SECTIONS+1) if s not in sections]}"
        )
    elif 1 not in sections or MIN_H2_SECTIONS not in sections:
        result.residuels.append(
            f"§1 ou §{MIN_H2_SECTIONS} manquant (sections trouées : {sections})"
        )

    # 4. Marqueur Phase 1 KISS dans le header (plusieurs variantes acceptées).
    # Le critère est informationnel : absence = ⚠️, pas ❌, car la conformité
    # structurelle (0 em-dash + sections H2 numérotées) reste le critère bloquant.
    head = "\n".join(txt.splitlines()[:50])
    match_markers = [p.search(head) for p in PHASE1_MARKER_PATTERNS]
    if any(match_markers):
        result.phase1_marker_present = True
    else:
        result.residuels.append(
            f" Marqueur Phase 1 KISS absent des 50 premieres lignes"
        )

    # Calcul du statut final
    if not result.residuels:
        result.statut = "✅"
    elif result.quintessence_exists:
        result.statut = "⚠️"
    else:
        result.statut = "❌"

    return result


# ============================================================
# AUDIT & COUVERTURE
# ============================================================


def audit_mapping(
    mapping: list[QuintessenceMapping],
    quintessence_dir: Path,
) -> list[AuditResult]:
    """Audit complet du mapping : retourne une liste d'AuditResult, une par entrée."""
    results: list[AuditResult] = []
    for entry in mapping:
        path = quintessence_dir / entry.quintessence
        results.append(validate_phase1_typed(entry, path))
    return results


def check_coverage(
    mapping: list[QuintessenceMapping],
    investigation_dir: Path,
    quintessence_dir: Path,
) -> dict:
    """Vérifie la couverture 1-à-1.

    Retourne un dict avec :
        - 'mapped_inv': set des INVESTIGATION files apparies
        - 'mapped_qtn': set des quintessences appariees
        - 'unmapped_inv': fichiers INVESTIGATION sans mapping
        - 'unmapped_qtn': fichiers quintessence sans mapping (hors LEGACY)
        - 'orphans_legacy': fichiers LEGACY detectes
    """
    inv_files = {p.name for p in investigation_dir.glob("*_INVESTIGATION.md")}
    qtn_files = {p.name for p in quintessence_dir.glob("*.md")}

    mapped_inv = {e.investigation for e in mapping}
    mapped_qtn = {e.quintessence for e in mapping}
    legacy_filenames = {l.filename for l in LEGACY_ENTRIES}

    # Anti-doublon : chaque INVESTIGATION et chaque quintessence doivent apparaitre
    # au plus une fois dans le mapping explicite. Sinon l'audit passe silencieusement
    # sur des doublons et double-compte des residuels.
    duplicate_inv = sorted({
        e.investigation for e in mapping
        if sum(1 for x in mapping if x.investigation == e.investigation) > 1
    })
    duplicate_qtn = sorted({
        e.quintessence for e in mapping
        if sum(1 for x in mapping if x.quintessence == e.quintessence) > 1
    })

    unmapped_inv = sorted(inv_files - mapped_inv)
    unmapped_qtn = sorted(
        (qtn_files - mapped_qtn) - legacy_filenames
    )
    orphans_legacy = sorted(legacy_filenames & qtn_files)

    return {
        "mapped_inv": mapped_inv,
        "mapped_qtn": mapped_qtn,
        "unmapped_inv": unmapped_inv,
        "unmapped_qtn": unmapped_qtn,
        "orphans_legacy": orphans_legacy,
        "duplicate_inv": duplicate_inv,
        "duplicate_qtn": duplicate_qtn,
        "total_inv": len(inv_files),
        "total_qtn": len(qtn_files),
        "total_legacy": len(LEGACY_ENTRIES),
    }


# ============================================================
# RAPPORTS
# ============================================================


def report_list(mapping: list[QuintessenceMapping]) -> str:
    """Mode `list` : affiche le mapping 42/42."""
    lines = [
        "# Mapping explicite RIC Saison 2 (42/42)",
        "",
        f"**Total entrées :** {len(mapping)}",
        "",
        "| Sujet canonique | P3 | Domaine | INVESTIGATION | Quintessence | Batch |",
        "|-----------------|----|---------|---------------|--------------|-------|",
    ]
    for e in mapping:
        lines.append(
            f"| `{e.subject_canonique}` | {e.p3_number} | {e.domaine} "
            f"| `{e.investigation}` | `{e.quintessence}` | {e.batch} |"
        )
    lines.append("")
    lines.append(f"**+ {len(LEGACY_ENTRIES)} entrée LEGACY HORS-CANONIQUE :**")
    for legacy in LEGACY_ENTRIES:
        lines.append(
            f"- `{legacy.filename}` ← sujet canonique `{legacy.canonical_subject}`"
        )
        lines.append(f"  Raison : {legacy.reason}")
    lines.append("")

    return "\n".join(lines)


def report_audit(results: list[AuditResult]) -> str:
    """Mode `audit` : valide la conformité Phase 1 KISS v1.0 canonique."""
    nb_conforme = sum(1 for r in results if r.statut == "✅")
    nb_residuel = sum(1 for r in results if r.statut == "⚠️")
    nb_manquant = sum(1 for r in results if r.statut == "❌")

    lines = [
        "# Audit Phase 1 KISS v1.0 canonique",
        "",
        f"**Total :** {len(results)} quintessences auditees",
        f"**Conformes :** {nb_conforme}/{len(results)} ({nb_conforme*100//len(results)}%)",
        f"**Résiduels :** {nb_residuel}/{len(results)}",
        f"**Manquantes :** {nb_manquant}/{len(results)}",
        "",
        "## Verdict critère par critère",
        "",
        "| Critère | Statut règle | Source |",
        "|---------|--------------|--------|",
        "| 0 em-dash (U+2014) | OBLIGATOIRE | knowledge.md (règle stricte) |",
        f"| ≥ {MIN_H2_SECTIONS} sections H2 numérotées | OBLIGATOIRE | SPECS v40 v2 KISS |",
        "| Marqueur Phase 1 KISS dans header | RECOMMANDE | Pilot Phase 1 KISS v1.0 |",
        "| Refus Phase 1 (pas de thèse propre) | OBLIGATOIRE | Pilot Phase 1 KISS v1.0 |",
        "",
        "## Détail par quintessence",
        "",
        "| Statut | P3 | Sujet | Em-dash | §H2 | Phase 1 KISS | Résiduels |",
        "|--------|----|--------|---------|-----|--------------|-----------|",
    ]
    for r in results:
        residuels_short = " / ".join(r.residuels) if r.residuels else "—"
        lines.append(
            f"| {r.statut} | {r.mapping.p3_number} "
            f"| `{r.mapping.subject_canonique}` "
            f"| {r.em_dash_count} "
            f"| {len(r.h2_sections_found)} "
            f"| {'✅' if r.phase1_marker_present else '❌'} "
            f"| {residuels_short} |"
        )
    lines.append("")
    return "\n".join(lines)


def report_coverage(coverage: dict) -> str:
    """Mode `coverage` : rapport de couverture 1-à-1."""
    nb_inv = coverage["total_inv"]
    nb_qtn = coverage["total_qtn"]
    nb_leg = coverage["total_legacy"]

    nb_unmapped_inv = len(coverage["unmapped_inv"])
    nb_unmapped_qtn = len(coverage["unmapped_qtn"])
    nb_orphans_legacy = len(coverage["orphans_legacy"])

    lines = [
        "# Couverture 1-à-1 RIC Saison 2",
        "",
        f"**Sources INVESTIGATION (racine) :** {nb_inv}",
        f"**Quintessences (`_quintessence/`) :** {nb_qtn} "
        f"= {nb_qtn - nb_leg} Phase 1 KISS v1.0 canonique + {nb_leg} LEGACY",
        "",
        "## Couverture mapping explicite",
        "",
        f"- ✅ INVESTIGATION mappées : {nb_inv - nb_unmapped_inv}/{nb_inv}",
        f"- ✅ Quintessences mappées : {(nb_qtn - nb_leg) - nb_unmapped_qtn}/"
        f"{nb_qtn - nb_leg}",
        f"- ⚠️ INVESTIGATION sans mapping : {nb_unmapped_inv}",
        f"- ⚠️ Quintessences sans mapping (hors LEGACY) : {nb_unmapped_qtn}",
        f"- 🗄️ Quintessences LEGACY détectées : {nb_orphans_legacy}/{nb_leg}",
        "",
    ]

    if nb_unmapped_inv:
        lines.append("## INVESTIGATION sans mapping explicite")
        lines.append("")
        for f in coverage["unmapped_inv"]:
            lines.append(f"- ⚠️ `{f}` : **AJOUTER une entrée dans la liste MAPPING**")
        lines.append("")

    if nb_unmapped_qtn:
        lines.append("## Quintessences sans mapping explicite (hors LEGACY)")
        lines.append("")
        for f in coverage["unmapped_qtn"]:
            lines.append(f"- ⚠️ `{f}` : **AJOUTER une entrée dans la liste MAPPING**")
        lines.append("")

    if coverage["orphans_legacy"]:
        lines.append("## LEGACY détectés")
        lines.append("")
        for f in coverage["orphans_legacy"]:
            lines.append(f"- 🗄️ `{f}` : HORS-CANONIQUE Phase 1 KISS v1.0 (déclaré explicite)")
        lines.append("")

    if coverage["duplicate_inv"] or coverage["duplicate_qtn"]:
        lines.append("## DOUBLONS détectés dans MAPPING")
        lines.append("")
        lines.append(
            "Fichiers présents plusieurs fois dans la liste MAPPING explicite. "
            "Risque : audit silencieux / double-compte des résiduels. "
            "**Corriger la liste MAPPING explicite dans `tools/audit_ric_mapping.py`**."
        )
        lines.append("")
        for f in coverage["duplicate_inv"]:
            lines.append(
                f"- (DOUBLON) `{f}` (INVESTIGATION) : DEDOUBLONNER dans MAPPING"
            )
        for f in coverage["duplicate_qtn"]:
            lines.append(
                f"- (DOUBLON) `{f}` (quintessence) : DEDOUBLONNER dans MAPPING"
            )
        lines.append("")

    return "\n".join(lines)


def report_full(
    mapping: list[QuintessenceMapping],
    results: list[AuditResult],
    coverage: dict,
) -> str:
    """Mode `full` : audit + coverage + statut v1.0 production multi-domaines."""
    nb_conforme = sum(1 for r in results if r.statut == "✅")
    nb_residuel = sum(1 for r in results if r.statut == "⚠️")
    nb_manquant = sum(1 for r in results if r.statut == "❌")
    nb_unmapped_inv = len(coverage["unmapped_inv"])
    nb_unmapped_qtn = len(coverage["unmapped_qtn"])
    nb_dup_inv = len(coverage["duplicate_inv"])
    nb_dup_qtn = len(coverage["duplicate_qtn"])

    # Regroupement par domaine pour le rapport multi-domaines
    domaines: dict[str, list[AuditResult]] = {}
    for r in results:
        domaines.setdefault(r.mapping.domaine, []).append(r)

    statut_global = "✅"
    if (
        nb_manquant > 0
        or nb_unmapped_inv > 0
        or nb_unmapped_qtn > 0
        or nb_dup_inv > 0
        or nb_dup_qtn > 0
    ):
        statut_global = "❌"
    elif nb_residuel > 0:
        statut_global = "⚠️"

    lines = [
        "# Rapport complet — Audit RIC Saison 2 2026-07-04",
        "",
        f"## Statut global : {statut_global}",
        "",
        f"- **Statut v1.0 canonique production multi-domaines :** "
        + ("COMPLET" if statut_global == "✅"
           else "PARTIEL" if statut_global == "⚠️"
           else "INCOMPLET"),
        f"- Sources INVESTIGATION : {coverage['total_inv']}",
        f"- Quintessences Phase 1 KISS v1.0 canonique : {coverage['total_qtn'] - coverage['total_legacy']}",
        f"- Quintessences LEGACY : {coverage['total_legacy']}",
        f"- Conformes : {nb_conforme}/{len(results)} "
        f"({nb_conforme*100//len(results)}%)",
        f"- Résiduels : {nb_residuel}/{len(results)}",
        f"- Manquantes : {nb_manquant}/{len(results)}",
        f"- INVESTIGATION sans mapping : {nb_unmapped_inv}",
        f"- Quintessences sans mapping : {nb_unmapped_qtn}",
        f"- DOUBLONS INVESTIGATION : {nb_dup_inv}",
        f"- DOUBLONS quintessence : {nb_dup_qtn}",
        "",
        "## Couverture par domaine",
        "",
        "| Domaine | Entrées | Conformes | Résiduels | Manquantes | Statut |",
        "|---------|---------|-----------|-----------|------------|--------|",
    ]

    for domaine, dom_results in sorted(domaines.items()):
        nb = len(dom_results)
        nb_c = sum(1 for r in dom_results if r.statut == "✅")
        nb_r = sum(1 for r in dom_results if r.statut == "⚠️")
        nb_m = sum(1 for r in dom_results if r.statut == "❌")
        statut = "✅" if nb_m == 0 and nb_r == 0 else "⚠️" if nb_m == 0 else "❌"
        lines.append(
            f"| {domaine} | {nb} | {nb_c} | {nb_r} | {nb_m} | {statut} |"
        )

    lines.append("")
    if coverage["duplicate_inv"] or coverage["duplicate_qtn"]:
        lines.append("## DOUBLONS détectés dans MAPPING")
        lines.append("")
        lines.append(
            "Fichiers présents plusieurs fois dans la liste MAPPING : risque de "
            "double-compte des résiduels / audit silencieux. Corriger la liste explicite."
        )
        lines.append("")
        for f in coverage["duplicate_inv"]:
            lines.append(f"- DOUBLON `{f}` (INVESTIGATION)")
        for f in coverage["duplicate_qtn"]:
            lines.append(f"- DOUBLON `{f}` (quintessence)")
        lines.append("")

    lines.append("## Verdict global")
    lines.append("")
    if statut_global == "✅":
        lines.append(
            f"**GO PLEIN** : les {nb_conforme} quintessences Phase 1 KISS v1.0 "
            "canonique sont conformes (0 em-dash, sections H2 numérotées, "
            "Phase 1 KISS marker). Le statut v1.0 canonique production "
            "multi-domaines est COMPLET."
        )
    elif statut_global == "⚠️":
        lines.append(
            f"**GO CONDITIONNEL** : {nb_conforme}/{len(results)} conformes ; "
            f"{nb_residuel} residuels a corriger."
        )
    else:
        causes = []
        if nb_manquant:
            causes.append(f"{nb_manquant} quintessences manquantes")
        if nb_unmapped_inv + nb_unmapped_qtn:
            causes.append(
                f"{nb_unmapped_inv + nb_unmapped_qtn} fichiers non apparies"
            )
        if nb_dup_inv + nb_dup_qtn:
            causes.append(
                f"{nb_dup_inv + nb_dup_qtn} doublons dans MAPPING (corriger la liste explicite)"
            )
        lines.append(
            f"**NO-GO** : {', '.join(causes)}."
        )
    lines.append("")

    return "\n".join(lines)


# ============================================================
# CLI
# ============================================================


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audit reproductible du mapping RIC Saison 2 (Phase 1 KISS v1.0 canonique).",
    )
    parser.add_argument(
        "mode",
        choices=["list", "coverage", "audit", "full"],
        help="Mode d'audit : list | coverage | audit | full",
    )
    parser.add_argument(
        "-d", "--dossier",
        type=Path,
        default=DEFAULT_DOSSIER,
        help=f"Racine du dossier (par défaut : {DEFAULT_DOSSIER})",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    dossier = args.dossier.resolve()
    investigation_dir = dossier
    quintessence_dir = dossier / "_quintessence"

    if not investigation_dir.exists():
        print(f"❌ Dossier INVESTIGATION absent : {investigation_dir}", file=sys.stderr)
        return 1

    exit_code = 0

    if args.mode == "list":
        print(report_list(MAPPING))
        return 0

    if args.mode == "coverage":
        cov = check_coverage(MAPPING, investigation_dir, quintessence_dir)
        print(report_coverage(cov))
        if (
            cov["unmapped_inv"]
            or cov["unmapped_qtn"]
            or cov["duplicate_inv"]
            or cov["duplicate_qtn"]
        ):
            exit_code = 1
        return exit_code

    if args.mode == "audit":
        results = audit_mapping(MAPPING, quintessence_dir)
        print(report_audit(results))
        if any(r.statut != "✅" for r in results):
            exit_code = 1
        return exit_code

    if args.mode == "full":
        cov = check_coverage(MAPPING, investigation_dir, quintessence_dir)
        results = audit_mapping(MAPPING, quintessence_dir)
        print(report_full(MAPPING, results, cov))
        if (
            cov["unmapped_inv"]
            or cov["unmapped_qtn"]
            or cov["duplicate_inv"]
            or cov["duplicate_qtn"]
            or any(r.statut != "✅" for r in results)
        ):
            exit_code = 1
        return exit_code

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
