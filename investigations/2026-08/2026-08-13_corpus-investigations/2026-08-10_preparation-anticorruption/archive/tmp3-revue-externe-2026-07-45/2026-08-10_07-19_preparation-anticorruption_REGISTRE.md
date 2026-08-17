# DASHBOARD : PRÉPARATION AUX INVESTIGATIONS ANTICORRUPTION — REGISTRE DE TRACABILITÉ

> Type : REGISTRE. Dernière mise à jour : 2026-08-10_07-19 (CEST). Ce registre est le tableau de bord du dossier `2026-08-10_preparation-anticorruption/` : toute décision, tout artefact, tout fact-check, toute session y est tracé.

## 1. Décisions actées (historique)

| Date | Décision | Détail | Statut |
|------|----------|--------|--------|
| 2026-08-10 | Usage final : mixte | Signalement AFA/PNF, publication, base interne : trois paliers selon la qualité du faisceau | ACTÉ |
| 2026-08-10 | Ordre de construction : pilote d'abord | La méthode se valide sur un cas concret, l'infrastructure émerge en legs (Approche C) | ACTÉ |
| 2026-08-10 | Terrain pilote : approfondir l'existant | Pas de nouveau sujet : capitaliser sur le corpus août 2026 | ACTÉ |
| 2026-08-10 | Projet pilote : Canal Seine-Nord (SESN) | 30 contrats, 5 exercices, angle avenants ; volume borné (74-76 marchés), rapport CdC 04/2026 récent | ACTÉ |
| 2026-08-10 | Approche C : pilote itératif avec legs | Chaque phase produit un artefact réutilisable (script + CSV + hash) ; infrastructure par co-production | ACTÉ |
| 2026-08-10 | Dossier commun | `2026-08-10_preparation-anticorruption/` remplace `_doctrine/` ; README + dashboard + 3 docs de doctrine + protocole regroupés | ACTÉ |

## 2. Fichiers du dossier commun

| Fichier | Rôle | Version | État |
|---------|------|---------|------|
| `README.md` | Point d'entrée du dossier | 1.0 (2026-08-10) | STABLE |
| `corruption_defintion.md` | Doctrine juridique | référence (2026-08) | RÉFÉRENCE |
| `corruption_brainstorm.md` | Protocole générique | référence (2026-08) | RÉFÉRENCE |
| `corruption_brainstorm_2.md` | Doctrine multi-canal | référence (2026-08) | RÉFÉRENCE |
| `2026-08-10_07-10_pilote-avenants-sesn_ARCHITECTURE.md` | Protocole pilote SESN | 1.0 (2026-08-10_07-10) | CONTRAT ACTIF |

## 3. Fact-checks réalisés (protocole mem-first)

| Date | Objet | Verdict | Source | Memory ID |
|------|-------|---------|--------|-----------|
| 2026-08-10 | Accès RBE/INPI bénéficiaires effectifs | Restriction 31/07/2024 confirmée ; intérêt légitime (journaliste/chercheur) ; données partielles par entité ; durcissement 10/11/2026 | INPI, data.inpi.fr, service-public | `e639ea7e-cf21-49f8-b74c-fc0391451a0e` |
| 2026-08-10 | Cour de cassation 26/02/2025 (doc 1 §10) | Référence erronée : l'arrêt du 26/02/2025 est Civ. 1re LCEN ; la bonne ancre est Crim. 25/02/2025 n° 23-84.563. Doctrine (bonne foi en 2 temps) confirmée | legalplanet.pro, doctrine.fr | `65b113b4-265a-4ddc-bd40-23c0a113ff8b` |
| 2026-08-10 | Secret des sources, art. 2 loi 1881 | Lettre exacte (régulier + rétribué) ; nuance : approche fonctionnelle jurisprudentielle, pas de carte de presse exigée | Légifrance, rapport AN n°1622 | `6f0709f1-b78e-467e-bfbd-6499b01b39e3` |

## 4. Gaps et trous noirs connus (hérités)

| Gap | Origine | Statut |
|-----|---------|--------|
| GAP-001 : aucun agrégat d'avenants publié par aucune institution (5 grands projets) | Enquête APEX 22-33 | CŒUR DU PILOTE : l'agréger soi-même |
| Rapport commission d'enquête Sénat GPE 2023 introuvable (URL 404) | Enquête APEX 22-33 | GAP tracé, non reconstitué |
| Ventilation dérive/avenants/inflation : jamais publiée sur aucun projet | Enquête APEX 22-33 | OBJECTIF PILOTE |

## 5. Artefacts produits / à produire (pilote SESN)

| Phase | Artefact | Statut |
|-------|----------|--------|
| 1 | `data/decp_sesn_raw.csv` + sha256 + `scripts/01_extract_decp.py` | EN ATTENTE |
| 2 | `data/decp_sesn_norm.csv` + `scripts/02_normalize_siren.py` | EN ATTENTE |
| 3 | `data/mesures_sesn.csv` + `data/concentration_sesn.csv` + `scripts/03_mesures.py` | EN ATTENTE |
| 4 | `data/cas_selection.csv` (3 anomalies + 2 témoins) | EN ATTENTE |
| 5 | `data/cada_lettres/` (5 lettres) + réponses | EN ATTENTE |
| 6 | `data/acteurs_sesn.csv` + graphe minimal | EN ATTENTE |
| 7 | `data/sources_sesn.md` + `data/registre_rumeurs.csv` + matrice versions/traces | EN ATTENTE |
| 8 | `data/hypotheses_sesn.md` | EN ATTENTE |
| 9 | `data/droit_reponse/` | EN ATTENTE |
| 10 | INVESTIGATION finale + REGISTRE + quintessence + write-back | EN ATTENTE |

## 6. Sessions

| Date | Session | Résumé | Artefacts |
|------|---------|--------|-----------|
| 2026-08-10_07-10→07-19 | Brainstorm + double-check + restructuration | Double-check des 2 brainstorm LLM (3 fact-checks), décisions actées (mixte, pilote SESN, approche C), protocole écrit, dossier commun restructuré | Protocole, README, dashboard, 3 mémoires Mnemolite |

## 7. NEXT_ACTION

1. Vérifier la cohérence des références (AGENTS.md pointe-t-il encore vers d'anciens chemins ?)
2. Lancer le pilote SESN : phase 1 (extraction DECP) selon protocole §3
3. Mettre à jour ce dashboard à chaque phase réalisée

## 8. Journal des modifications du dashboard

| Date | Modification |
|------|--------------|
| 2026-08-10_07-19 | Création (restructuration `_doctrine/` → `2026-08-10_preparation-anticorruption/`) |
