# VERIFICATION DATEE : LA COMMISSION DES AFFAIRES ECONOMIQUES A-T-ELLE PUBLIE ENTRE-TEMPS UN CR ECRIT DE L'AUDITION DE LA PRESIDENTE DE LA CRE DU 29/04/2026 ? (PROTOCOLE DE CONTRE-PREUVE POUR LA QE 04-38)

- STATE          : FINAL
- DATE           : 2026-08-11 04:46 CEST (baseline établie) ; prochaine vérification : 2026-09-01 à 2026-09-05
- TYPE           : VERIFICATION (KERNEL v2.8, protocole à date fixe, sécurisation du fondement factuel de la QE 04-38)
- DOSSIER        : 2026-08-10_run2-enr (fil Valeco/EnBW, axe légitimité, rec. n°1 CdC, QE 04-38)
- OBJECT         : vérifier, à date fixe (début septembre 2026), si la commission des affaires économiques de l'AN a publié un compte rendu écrit des débats de l'audition de la présidente de la CRE du 29/04/2026 (CR 81), alors que le CR 81 déclare au 10/08 et au 11/08 « Ce point de l'ordre du jour n'a pas fait l'objet d'un compte rendu écrit ». Objectif : sécuriser l'affirmation n°4 de la QE (04-38) avant dépôt
- VERDICT        : BASELINE ÉTABLIE LE 11/08/2026 : AUCUN CR ÉCRIT DES DÉBATS PUBLIÉ. Le CR 81 (réf. l17cion-eco2526081, déposé 30/04/2026) est re-téléchargé à la source primaire : PDF bit-identique au 10/08 (sha256 e4c4f17e...38747, 3 pages, texte 3 584 o identique, 0 diff), contient toujours la phrase « Ce point de l'ordre du jour n'a pas fait l'objet d'un compte rendu écrit. Les débats sont accessibles sur le portail vidéo de l'Assemblée nationale à l'adresse suivante : https://assnat.fr/C5J2WN ». Aucun addendum, aucun CR 81 bis, aucune transcription complémentaire détectée. Le fondement factuel de la QE est donc VALIDE à la date du 11/08 ; le protocole ci-dessous fixe la re-vérification à début septembre 2026 avant dépôt effectif de la QE
- GAP_SEVERITY   : 0.02 (fait établi par double vérification à 24 h d'intervalle sur hash ; la seule inconnue résiduelle est la publication éventuelle entre le 11/08 et la date de dépôt, couverte par le protocole §4)

## 1. Pourquoi cette vérification est nécessaire (lien avec la QE 04-38)

- La QE `2026-08-11_04-38_qe-rec1-collecte-couts_QUESTION.md` (10 FCT-qe, FINAL) affirme notamment : « lors de l'audition de la présidente de la CRE par la commission des affaires économiques de l'Assemblée nationale le 29 avril 2026, il n'a pas été demandé à cette dernière d'expliciter sa position sur cette recommandation » et « cette audition n'a pas, en outre, fait l'objet d'un compte rendu écrit publié par la commission ».
- La précaution est documentée au §5 du 04-38 : « vérifier à la date de dépôt que l'audition du 29/04/2026 n'a pas entre-temps fait l'objet d'une publication de CR écrit (contre-preuve) ».
- Ce document opérationnalise cette précaution : baseline au 11/08/2026 (fait, ci-dessous) + protocole de re-vérification à date fixe (début septembre 2026, §4) + arbre de décision si publication (§5).

## 2. Baseline au 11/08/2026 : aucun CR écrit publié (vérification à la source primaire)

### 2.1 La référence exacte (établie au 22-38, re-confirmée le 11/08)

- CR n° 81 de la commission des affaires économiques, session 2025-2026, réf. `l17cion-eco2526081`, uid open data `CRCANR5L17S2026PO419610N081`.
- URL : `https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/cion-eco/l17cion-eco2526081_compte-rendu` (+ `.pdf`).
- Déposé le 30/04/2026 (dateCreation/dateDepot, JSON open data lu au 22-38).

### 2.2 La vérification du 11/08/2026 (hash + texte)

| Élément | Baseline 10/08 (archivé) | Re-vérification 11/08 | Verdict |
|---------|--------------------------|------------------------|---------|
| PDF CR 81 | `data/audition_wargon_29042026/cr81_audition-wargon_2026-04-29.pdf` sha256 e4c4f17e...38747 | `/tmp/cr81_recheck.pdf` sha256 e4c4f17e...38747 | BIT-IDENTIQUE |
| Texte PDF | `cr81_texte.txt` sha256 8c568f00...6766 | `/tmp/cr81_recheck.txt` sha256 8c568f00...6766 | IDENTIQUE (diff = 0) |
| Mention clé | « Ce point de l'ordre du jour n'a pas fait l'objet d'un compte rendu écrit » | Présente (grep confirmé) | INCHANGÉE |
| Pages | 3 | 3 | INCHANGÉ |

### 2.3 Conséquence pour la QE

- L'affirmation « cette audition n'a pas fait l'objet d'un compte rendu écrit publié par la commission » est VRAIE à la date du 11/08/2026, vérifiée par téléchargement direct du PDF officiel et comparaison de hash à 24 h d'intervalle.
- Le CR 81 ne contient AUCUN mot de Wargon (3 pages : fiche de séance, informations commission, présents/excusés) : la seule source des débats est la vidéo (assnat.fr/C5J2WN, page vidéo 18767384), dont la transcription complète a été réalisée par whisper (23-20, 73 715 car.) : c'est sur cette transcription que repose le constat d'absence de question sur la rec. n°1 (04-09 §5.4).

## 3. Le fait de pratique qui rend la publication improbable (mais pas impossible)

- Le 23-39 a établi que la commission des affaires économiques ne transcrit AUCUNE audition ordinaire : les 281 CR des sessions 2024-2025 et 2025-2026 portent tous la mention « ce point de l'ordre du jour n'a pas fait l'objet d'un compte rendu écrit », quel que soit l'auditionné (régulateurs, ministres, entreprises, experts). Seule exception : les auditions en application de l'article 13 de la Constitution (nominations), transcrites intégralement.
- Le 04-09 a établi que la politique de non-transcription est propre à la commission des affaires économiques (et culture) : la commission des finances, elle, transcrit intégralement les auditions des régulateurs financiers (Villeroy 108 410 car., Barbat-Layani 86 334 car.).
- Probabilité de publication d'un CR écrit rétroactif de l'audition Wargon : FAIBLE (aucun précédent de transcription rétroactive identifié dans les 281 CR). Mais le protocole §4 l'exclut factuellement à chaque date de vérification plutôt que de s'y fier.

## 4. Protocole de vérification à date fixe (début septembre 2026)

### 4.1 Quand

- Date cible : 2026-09-01 à 2026-09-05 (début septembre, avant tout dépôt effectif de la QE). Une exécution suffit ; la re-exécuter seulement si la QE n'est pas encore déposée après le 15/09.

### 4.2 Quoi (3 vérifications indépendantes)

1. **PDF du CR 81** : re-télécharger `https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/cion-eco/l17cion-eco2526081_compte-rendu.pdf`, comparer sha256 à la baseline e4c4f17e2dc31ae4c285466a00c381e0346217b52e6ff6d4a12369c5cea38747. Si identique : AUCUN changement. Si différent : extraire le texte, chercher « compte rendu écrit », « Wargon », « CRE ».
2. **Page du CR 81** : re-télécharger la page HTML, chercher « compte rendu écrit » (la page charge le contenu en JS, le PDF reste la source fiable : la vérification PDF suffit).
3. **Index des CR de la commission** : vérifier s'il existe un CR 81 bis ou un document séparé « transcription » / « compte rendu intégral » dans la série cion-eco (scan des CR 80-121, comme au 22-38) et dans l'open data AN (`CRCANR5L17S2026PO419610N081` pour d'éventuelles versions successives).

### 4.3 Comment consigner

- Mettre à jour ce document : remplacer la date de baseline par la date de vérification, coller les nouveaux hash, noter le verdict (CHANGÉ / INCHANGÉ).
- Mettre à jour l'entrée RUN_MANIFEST (retirer la précaution « à vérifier » si inchangé).

## 5. Arbre de décision si publication (contre-preuve)

- **Scénario A (probable) : CR inchangé, aucune transcription publiée.** La QE 04-38 est déposable telle quelle. Aucune modification.
- **Scénario B : une transcription des débats du 29/04/2026 est publiée entre-temps** (par exemple un CR « intégral » ou une fiche reprenant les échanges). Actions : (1) lire la transcription, chercher si une question a porté sur la rec. n°1 (collecte des coûts) ; (2) si oui, réécrire l'exposé des motifs de la QE pour remplacer « il n'a pas été demandé » par la citation exacte de la question et de la réponse de la présidente de la CRE (le fond du dossier, la position de refus de la collecte exhaustive, reste inchangé) ; (3) si non, la QE reste valide et gagne même en force (la transcription publiée confirmerait l'absence de question) ; (4) croiser avec la transcription whisper (23-20) qui constitue déjà la trace indépendante des débats.
- **Scénario C : le CR 81 est modifié (réécriture rétroactive).** Comparer les hash : toute modification serait tracée par la différence avec la baseline e4c4f17e. Documenter la modification (date, contenu) : en soi un fait probatoire (modification d'un document officiel).

## 6. Table de faits

| ID | Proposition | Source | Localisation | Nature | Statut |
|----|-------------|--------|--------------|--------|--------|
| FCT-vf-001 | Le CR 81 (l17cion-eco2526081) déclare le 11/08/2026 « ce point de l'ordre du jour n'a pas fait l'objet d'un compte rendu écrit » | PDF re-téléchargé 11/08 | /tmp/cr81_recheck.pdf | Fait | ÉTABLI |
| FCT-vf-002 | PDF CR 81 bit-identique entre 10/08 et 11/08 (sha256 e4c4f17e...38747) | comparaison hash | data/audition_wargon_29042026/ vs /tmp | Fait | ÉTABLI |
| FCT-vf-003 | Texte du CR 81 identique entre 10/08 et 11/08 (diff = 0) | diff | cr81_texte.txt vs cr81_recheck.txt | Fait | ÉTABLI |
| FCT-vf-004 | Le CR 81 ne contient aucun mot de Wargon (3 pages, fiche de séance) : la seule source des débats est la vidéo 18767384 | PDF | p. 1-3 | Fait (absence) | ÉTABLI |
| FCT-vf-005 | La transcription whisper (23-20, 73 715 car.) est la trace indépendante des débats : constat d'absence de question sur la rec. n°1 (0 mention collecte/échantillonnage/plan d'audit/CdC) | 23-20, 04-09 §5.4 | documents dossier | Fait | ÉTABLI |
| FCT-vf-006 | La commission eco ne transcrit aucune audition ordinaire (281 CR, seule exception art. 13) : publication rétroactive sans précédent | 23-39, 04-09 | documents dossier | Fait (pratique) | ÉTABLI |
| FCT-vf-007 | Protocole de re-vérification à date fixe (01-05/09/2026) : PDF + page + index, comparaison hash, consignation dans ce document | ce document | §4 | Procédure | À EXÉCUTER |
| FCT-vf-008 | Arbre de décision : Scénario A (inchangé = QE déposable), B (transcription publiée = adapter ou renforcer), C (CR modifié = tracer le changement) | ce document | §5 | Analyse | PRÊT |
| FCT-vf-009 | Le fondement factuel de la QE 04-38 est valide à la date du 11/08/2026 | ce document | §2.3 | Verdict | ÉTABLI |

## 7. Sources

1. PDF CR 81 re-téléchargé : `https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/cion-eco/l17cion-eco2526081_compte-rendu.pdf` (11/08/2026, sha256 e4c4f17e2dc31ae4c285466a00c381e0346217b52e6ff6d4a12369c5cea38747).
2. Artefacts baseline : `data/audition_wargon_29042026/` (CR 80/81/82, texte, page vidéo), du 10/08/2026.
3. Documents croisés : 22-38 (réf. exacte du CR 81), 23-39 (281 CR, pratique), 04-09 (contre-test commissions, pattern), 23-20 (whisper), 04-38 (QE à sécuriser).
