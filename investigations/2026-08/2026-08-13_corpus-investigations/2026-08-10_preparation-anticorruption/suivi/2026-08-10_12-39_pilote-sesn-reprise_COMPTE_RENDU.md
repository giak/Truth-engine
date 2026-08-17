# COMPTE RENDU DE REPRISE : Pilote Avenants SESN (Phase 1 + double-check faits, Phase 2 en cours)

- Horodatage : 2026-08-10 12:39 CEST
- Auteur du CR : session opencode antérieure (10/08/2026, 07:00-12:40)
- Destinataire : LLM en contexte VIERGE. Ce document suffit pour reprendre sans conversation antérieure.
- Projet : Truth Engine. Pipeline : `truth-engine-v2/KERNEL.md`. Règles : `AGENTS.md` (racine projet), conventions de nommage, règle RTK (préfixer les commandes shell `rtk`), anti-fausse-précision (pas de parsing regex de texte LLM), mnemolite-mem-first pour tout fait.

## 1. OBJET DU PILOTE

Détecter d'éventuelles anomalies dans les avenants/modifications de marchés publics de la **Société du Canal Seine-Nord Europe (SCSNE/SESN)**, SIREN 829535996, sur la période 2021-2026 (coupure : 30/06/2026). Contrat d'exécution : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/2026-08-10_07-10_pilote-avenants-sesn_ARCHITECTURE.md` (v1.1, 10 phases). Dossier commun de préparation : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/`.

## 2. RÉPERTOIRES ET ARTEFACTS (état au 10/08/2026 12:40)

Dossier d'enquête : `/home/giak/projects/truth-engine/investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_pilote-avenants-sesn/`

- `RUN_MANIFEST.md` : manifeste du run (date de coupure 30/06/2026, bilan, § DOUBLE-CHECK).
- `2026-08-10_09-30_avenants-sesn-pilote_REGISTRE.md` : registre de progression (faits SRC-ID P1-F01..F07, gaps GAP-001..003, section DOUBLE-CHECK datée).
- `scripts/01_extract_decp.py` : extraction SCSNE depuis decp-global.json (déterministe, stdlib + ijson, venv `/tmp/opencode/pilote-venv`, ijson 3.5.1).
- `scripts/01b_recensement_univers.py` : recensement fusionné (DECP + page SCSNE + widget).
- `data/decp-global.json` : fichier consolidé ministère des Finances (dataset data.gouv « Données essentielles de la commande publique - fichiers consolidés », sha256 `73dc1476cc81c9b61060be8434d79e21346831dce1691d4c21413d2a7256b575`). 704 699 marchés, nœud racine unique `marches` (pas de `concessions`).
- `data/decp_sesn_raw.csv` : les 46 lignes SCSNE de la fenêtre (sha256 `6347499af8f881732f6aa41c329adc62cfead91cbce780a20985f438ca5f699d`).
- `data/recensement_univers.csv` : 115 lignes (46 DECP + 57 page SCSNE + 12 widget), 69 sans montant (sha256 `2fd4f5ba...`).
- `data/marches_sans_montant.csv`, `data/registre_pistes.csv` (vierge), `data/artefacts_phase1.sha256`.
- `data/decp-2019.json` (900 Mo), `data/decp-2022.json` (19,6 Mo) : ressources FLOTTANTES, EXCLUES du socle de preuve (voir § 5, fait F03c ; hashes dans `data/artefacts_annuels_flottants.sha256`).
- `data/decp-global.json.sha256`, `data/decp_sesn_raw.sha256` générés par les scripts.

## 3. FAITS ÉTABLIS (double-check du 10/08/2026, ré-exécutés en indépendant)

- F01 : SIREN/SIRET SCSNE = 829535996 / 82953599600039 (API recherche-entreprises).
- F02 : 47 lignes SCSNE dans decp-global.json, toutes notifiées 2024-2026 ; 46 dans la fenêtre (la 47e, id `2026T17080`, notifiée 2026-07-03, EST HORS CUPURE : exclue ; à traiter séparément si fenêtre élargie).
- F03 : le fichier global CONTIENT 508 957 entrées `modifications` sur 170 557 marchés (24,2 %), 129 167 avec montant, dont 51 en source AIFE_PLACE. MAIS 0 modification sur les 47 lignes SCSNE.
- F03b : 0 DECP SCSNE avant 2024. Le global couvre 100 177 marchés notifiés avant 2024 (2019 : 1 180 ; 2020 : 4 029 ; 2021 : 12 714 ; 2022 : 24 759 ; 2023 : 57 495) : aucun n'est SCSNE.
- F03c : decp-2019.json / decp-2022.json sont des ressources FLOTTANTES de data.gouv (réécrites entre 2 téléchargements : structures et volumes différents, ex. decp-2022 re-téléchargé = 8 756 items e-marchespublics 2023-2024 ; decp-2019 = 803 487 items mix PES/aws). Non reproductibles : EXCLUS du socle.
- F04 : montant cumulé des 46 DECP de la fenêtre = **526 420 107,98 € HT** (brut 47 = 527 392 024,98 € ; hors-fenêtre 2026T17080 = 971 917 €). Vérifié ligne à ligne JSON↔CSV en Decimal, 0 écart. ATTENTION : le chiffre 514 438 257,98 € trouvé dans des comptes rendus antérieurs est FAUX (erreur de dédup silencieuse sur les 5 lignes à id `000`).
- F05 : page SCSNE « Les marchés publics de la SCSNE sont publiés sur la plateforme AWS » ; 57 numéros SESN 2014-2022 listés ; widget « 120 résultats » mais seulement 12 cartes récupérables (GAP-002).
- F06 : recherche publique AWS (marches-publics.info) : 1 seule annonce retournée (000M524), accès complet réservé aux acheteurs (GAP-003).
- F07 : recensement fusionné 115 lignes, 69 sans montant.

## 4. GAPS (état au 10/08/2026 ; GAP = nature, tentative, résultat)

- GAP-001-P1 : 0 modification SCSNE dans les consolidés alors que le format le permet (508 957 entrées ailleurs). Interprétation : non-publication côté SCSNE, PAS une limite du format. À trancher Phase 3 via PLACE (marches-publics.gouv.fr renvoyait vide le 10/08), BOAMP/TED.
- GAP-001-P1b : 0 DECP SCSNE avant 2024 (prouvé sur le global seul).
- GAP-002-P1 : widget SCSNE non paginé (Livewire JS) : 12 cartes seulement.
- GAP-003-P1 : recherche publique AWS non exhaustive (accès acheteur requis).

## 5. DÉCOUVERTE CRITIQUE EN COURS DE TRAITEMENT (doublon inter-source suspecté)

Paire détectée dans decp_sesn_raw.csv :

- Ligne AWS `id=000` (source `marches-publics_aws`), objet « Marché de travaux de réhabilitation de 4 quais existants sur le Canal du Nord - Secteur 2 », montant **422 841 600,00 €**, notifié 2025-11-20, CPV 45241100 (sans -9), titulaires 32065170600071 + 38181855800144.
- Ligne PLACE `id=2844722` (source `AIFE_PLACE`), objet « ...travaux d'aménagement, de réhabilitation et de construction de quais fluviaux... - M214 - Lot Q2 » (le texte mentionne deux lots : Q1-M213 réhabilitation de quais existants, Q2-M214 quai neuf de Catigny), montant **4 228 416,00 €**, notifié 2025-11-20, CPV 45241100-9, titulaire 32065170600071.

Faits de corrélation : même date de notification, même CPV (45241100(-9)), titulaire commun 32065170600071, rapport des montants EXACTEMENT ×100 (422 841 600 / 4 228 416 = 100). Interprétation NON conclue : soit erreur d'unité ×100 (centimes/euros) sur la ligne AWS, soit deux lots distincts (Q1/Q2) du même AAPC avec un montant AWS erroné. À trancher avant Phase 3 car le montant AWS représente ~80 % du cumul 526 M€ : si l'AWS doit être ramené à ~4,2 M€ (ou dédupliqué), le cumul chute à ~107 M€. Sources à consulter : avis BOAMP/TED du marché M213/M214 (idweb à chercher), page SCSNE (20S1I015 = quais Pimprez/Ribécourt : marché DIFFÉRENT).

Les 5 lignes `id=000` (toutes marches-publics_aws) ont des objets distincts : quel = 422 841 600 ; accord-cadre AMO foncier = 5 000 000 (10/04/2026) ; AMO économiste = 1 381 850 (12/05/2026) ; AMO communication = 700 000 (22/05/2026) ; plateforme trimodale Ribécourt = 4 900 000 (12/06/2026). + `000D0390` : accord-cadre prestations intellectuelles = 1 800 000 (14/04/2026). Ne PAS dédupliquer entre elles (objets distincts ; le script 01 a déjà géré la clé id+objet).

## 6. ÉTAT DES PHASES (contrat v1.1)

| Phase | Contenu | État |
|-------|---------|------|
| 0 | RUN_MANIFEST (checkpoint KERNEL) | TERMINÉE |
| 1 | extraction DECP + recensement + artefact + double-check | TERMINÉE (double-check : 09:15-10:15, voir RUN_MANIFEST § DOUBLE-CHECK) |
| 2 | normalisation SIREN/SIRET (Luhn, zéros perdus, dédup par id marché/acheteur/lot/schéma ; JAMAIS (SIREN, objet, montant)) ; rapprochement RNE/INPI attributaires ; sorties `data/decp_sesn_norm.csv` + `scripts/02_normalize_siren.py` + liste SIREN non résolus | **EN COURS** : rien d'écrit encore, script 02 NON créé. La règle anti-LLM s'applique (nettoyage déterministe pur). Préalable : trancher le doublon § 5 |
| 3 | mesures (montants initiaux/finaux, nb événements, taux modif, concentration 5 premiers, proximité seuils R.2194-8/2194-9, comparaisons homogènes) | À FAIRE (rappel : 0 modif connue = taux 0, interpréter comme lacune DECP, vérifier PLACE) |
| 4 | sélection 3 anomalies + 2 témoins (critères GELÉS avant calcul ; Voie 1 recensement, Voie 2 pistes) | À FAIRE |
| 5 | 5 courriers CADA (DELIVERABLE_PENDING, pas d'envoi réel) | À FAIRE |
| 6 | cartographie acteurs + graphe (base HATVP, OpenSanctions, BODACC) | À FAIRE |
| 7 | collecte multi-canal + évaluation sources (8 familles ; RÉPÈTE ≠ CORROBORE) | À FAIRE (registre_pistes.csv vierge) |
| 8 | matrice hypothèses H0-H6 | À FAIRE |
| 9 | questionnaires droit de réponse | À FAIRE |
| 10 | dossier INVESTIGATION final | À FAIRE |

## 7. PROCHAINE ACTION RECOMMANDÉE (reprise vierge)

1. Lire `RUN_MANIFEST.md`, `2026-08-10_09-30_avenants-sesn-pilote_REGISTRE.md`, le contrat `ARCHITECTURE` v1.1 (chemin § 1), le présent CR.
2. TRANCER LE DOUBLON § 5 : chercher l'avis d'attribution M213/M214 (quais Secteur 2) sur BOAMP/TED (idweb 25-140463 et voisins, notices à récupérer via ted.europa.eu ; vérifier les prix par lot ; rechercher un éventuel avis « 25-xxxxx » pour Marché de travaux réhabilitation quais). Sortie : décision écrite + si nécessaire correction du CSV (nouvelle version horodatée, hash), MAJ REGISTRE/RUN_MANIFEST et de la mémoire Mnemolite.
3. Écrire `scripts/02_normalize_siren.py` (Luhn SIRET, SIREN 9 chiffres, zéros/espaces, colonnes statut ; dédup clé id-normalisé+acheteur+lot+schéma ; pas de LLM) → `data/decp_sesn_norm.csv`, liste SIREN non résolus ; rapprochement titulaires via RNE/INPI (recherche-entreprises.api.gouv.fr) pour les trous.
4. Phase 3 (mesures) : décider l'impact du doublon sur le cumul avant de publier tout indicateur agrégé.
5. Mettre à jour la mémoire Mnemolite après chaque phase (write_memory/update_memory ; le MCP peut timeout sur le embedding : relire la mémoire après pour confirmer l'écriture ; l'API est idempotente).

## 8. PIÈGES ET RÈGLES À RESPECTER (appris pendant cette session)

- Ajouter des sections DATÉES au REGISTRE, ne jamais réécrire au-dessus de la section « Prochaine session ».
- Ne pas dédupliquer les lignes à id `000` entre elles (objets distincts). La dédup par id écrase silencieusement : toujours itérer sur le CSV complet pour les sommes.
- Les montants du CSV sont des strings (`'422841600.0'`) : convertir en Decimal pour toute somme, comparer ligne à ligne JSON↔CSV.
- data.gouv réécrit les fichiers annuels : TOUJOURS vérifier sha256 avant usage ; les artefacts de preuve doivent être épinglés par hash dans `artefacts_phase1.sha256`.
- PLACE (marches-publics.gouv.fr) était inaccessible (page vide) le 10/08 : ne pas conclure sur « absence » à partir de cette source tant qu'elle n'a pas répondu ; re-tester.
- venv : `/tmp/opencode/pilote-venv` (ijson 3.5.1). Téléchargements lourds : User-Agent `truth-engine-pilote-sesn`.
- Style : pas d'em-dash (U+2014) dans les écrits ; zéro flagornerie ; toute donnée doit avoir un SRC-ID et un hash si fichier.