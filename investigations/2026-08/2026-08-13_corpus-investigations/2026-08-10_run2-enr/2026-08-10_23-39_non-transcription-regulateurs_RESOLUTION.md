# RESOLUTION : NON-TRANSCRIPTION DES AUDITIONS : MOTIF GÉNÉRALISÉ À TOUS LES RÉGULATEURS (COMMISSION DES AFFAIRES ÉCONOMIQUES, 2 SESSIONS COMPLÈTES : 281 CR SCANNÉS), EXCEPTION CONFIRMÉE : AUDITIONS ART. 13 (NOMINATIONS) TRANSCRITES

- STATE          : FINAL
- DATE           : 2026-08-10 23:39 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste, suite du 22-38 GAP-ll2-2 et du 23-20 transcription whisper)
- DOSSIER        : 2026-08-10_run2-enr (fil Valeco/EnBW, axe légitimité, critère 7 de la grille : opacité de la parole des régulateurs)
- OBJECT         : déterminer si la non-publication de CR écrit des auditions (constatée pour la CRE/Wargon 29/04/2026 au 22-38) est propre à la CRE ou généralisée à tous les régulateurs et à toutes les auditions de la commission des affaires économiques de l'AN, en scannant les comptes rendus des sessions 2024-2025 et 2025-2026 et en vérifiant les auditions de l'ARCOM, de l'ACPR, de l'Autorité de la concurrence et de l'ARCEP
- VERDICT        : LE MOTIF EST GÉNÉRALISÉ À TOUS LES RÉGULATEURS ET À TOUTES LES AUDITIONS ORDINAIRES. Scan exhaustif des 281 CR de la commission des affaires économiques (160 CR session 2024-2025 + 121 CR session 2025-2026, PDF téléchargés et lus intégralement) : TOUTES les auditions ordinaires portent la mention « Ce point de l'ordre du jour n'a pas fait l'objet d'un compte rendu écrit », quel que soit l'auditionné (régulateur : CRE, Autorité de la concurrence, ARCEP, Médiateur de l'énergie ; administration : DGCCRF, DGDDI, Bpifrance, Business France ; entreprises : Saint-Gobain, Carrefour, CMA CGM, E.Leclerc, Intermarché ; ministres ; experts). SEULE exception : les auditions en application de l'article 13 de la Constitution (nominations présidentielles : EDF/Debon, EDF/Fontana, CEA/Jacq ×2, INRAE/Mauguin, CEA/Etienvre, Orano/Imauven) sont transcrites intégralement (69 000-115 000 caractères chacune). La non-transcription n'est donc PAS propre à la CRE : elle est la règle générale de la commission des affaires économiques pour les auditions ordinaires, avec la seule exception procédurale des nominations art. 13
- GAP_SEVERITY   : 0.05 (le motif est tranché à la source primaire sur 2 sessions complètes ; le contre-test des autres commissions de l'AN, culture/finances, reste ouvert mais ne change pas la conclusion sur la commission des affaires économiques)

## 1. Méthode : scan exhaustif des CR de la commission des affaires économiques (2 sessions)

- Téléchargement des PDF des comptes rendus de la commission des affaires économiques, pattern validé au 22-38 : `https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/cion-eco/l17cion-eco{session}{n:03d}_compte-rendu.pdf` (session 2425 = 2024-2025, session 2526 = 2025-2026).
- Volume : 160 PDF (session 2024-2025, CR n° 1-160) + 121 PDF (session 2025-2026, CR n° 1-121) = 281 comptes rendus téléchargés et convertis en texte (pdftotext -layout), le 10/08/2026 entre 23:24 et 23:39.
- Recherche dans chaque CR : (1) la phrase « a auditionné » (auditions), (2) les noms de régulateurs (ARCOM, ACPR, Autorité de la concurrence, ARCEP, Médiateur), (3) la mention « n'a pas fait l'objet d'un compte rendu écrit », (4) « article 13 de la Constitution » (exception procédurale).
- Artefacts : `/tmp/cr_pdf_2526_*.pdf` et `/tmp/cr_pdf_2425_*.pdf` (281 PDF), logs `/tmp/scan_reg_log.txt` (session 2526) et `/tmp/scan_reg_2425_log.txt` (session 2425).

## 2. Constat 1 : la mention « pas de CR écrit » est systématique pour toutes les auditions ordinaires

Extraction de la phrase exacte dans les CR : « Ce point de l'ordre du jour n'a pas fait l'objet d'un compte rendu écrit. Les débats sont accessibles sur le portail vidéo de l'Assemblée nationale. » Vérifiée dans TOUTES les auditions listées ci-dessous, sans exception :

### 2.1 Régulateurs auditionnés (le cœur de la question) : TOUS sans CR écrit

| CR | Date | Régulateur | Auditionné | CR écrit |
|----|------|-----------|------------|----------|
| 2526/081 | 29/04/2026 | CRE | Emmanuelle Wargon, présidente | **NON** (assnat.fr/C5J2WN, déjà documenté 22-38) |
| 2526/047 | 27/01/2026 | Autorité de la concurrence | Benoît Cœuré, président | **NON** (assnat.fr/0CH9yN) |
| 2526/107 | 24/06/2026 | ARCEP | Laure de La Raudière, présidente | **NON** (renvoi vidéo) |
| 2526/091 | 13/05/2026 | Médiateur national de l'énergie | Bernard Doroszczuk | **NON** (assnat.fr/dc81n5) |
| 2425/116 | 25/06/2025 | Médiateur national de l'énergie | Olivier Challan-Belval | **NON** (assnat.fr/2A455Q) |
| 2526/044+045 | 20/01/2026 | DGCCRF + DGDDI (administration) | Sarah Lacoche + Florian Colas | **NON** (renvoi vidéo) |

### 2.2 Auditions ordinaires non-régulateurs (échantillon représentatif, toutes sans CR écrit)

- CR 002 (08/10/2025) : Benoît Bazin, PDG Saint-Gobain : NON
- CR 026 (25/11/2025) : Philippe Michaud + Michel-Édouard Leclerc (E.Leclerc) : NON
- CR 027 (06/01/2026) : Frédéric Merlin, président Groupe SGM : NON
- CR 036 (16/12/2025) : Naïma Moutchou, ministre des Outre-mer : NON
- CR 037 (17/12/2025) : Nicolas Dufourcq, DG Bpifrance : NON
- CR 040 (07/01/2026) : Clément Beaune, haut-commissaire au Plan : NON
- CR 043 (14/01/2026) : Thierry Cotillard (Les Mousquetaires), G. Van Ooteghem (Intermarché), G. Ferrari (Everest) : NON
- CR 049 (28/01/2026) : Denis Ferrand, DG Rexecode : NON
- CR 056 (11/02/2026) : Dominique Anract, président CNBPF : NON
- CR 060 (18/02/2026) : table ronde tourisme (Philippe Sueur, Anett) : NON
- CR 063 (25/03/2026) : Alexandre Bompard, PDG Carrefour : NON
- CR 064 (25/03/2026) : Franck Sander, président CGB : NON
- CR 100 (09/06/2026) : Louis Margueritte, DG Business France : NON
- CR 101 (09/06/2026) : Rodolphe Saadé, PDG CMA CGM + Ramon Fernandez, DAF : NON
- CR 102 (10/06/2026) : Olivier Salleron, président FFB : NON
- CR 104 (16/06/2026) : François Houllier, PDG Ifremer : NON
- CR 108 (24/06/2026) : table ronde ameublement : NON
- CR 110 (30/06/2026) : Éric Lelong (InterApi), filière miel : NON
- CR 112 (07/07/2026) : Jean-Christophe Repon, président Capeb : NON
- CR 115 (15/07/2026) : Olivier Le Nézet, président Comité national des pêches : NON

## 3. Constat 2 : la SEULE exception est l'article 13 de la Constitution (nominations présidentielles), transcrites intégralement

| CR | Date | Nomination (art. 13) | Transcription |
|----|------|----------------------|---------------|
| 2526/006 | automne 2025 | Marie-Ange Debon, présidente du CA EDF | INTÉGRALE (114 585 car.) |
| 2526/046 | 21/01/2026 | Claude Imauven, renouvellement président CA Orano (+ vote) | INTÉGRALE (66 554 car., 21 pages) |
| 2526/074 | 2026 | François Jacq, renouvellement président CA CEA | INTÉGRALE (70 116 car.) |
| 2425/006 | 2024 | Philippe Mauguin, président INRAE | INTÉGRALE (87 566 car.) |
| 2425/085 | 2025 | François Jacq, nomination président CA CEA | INTÉGRALE (69 428 car.) |
| 2425/086 | 2025 | Bernard Fontana, nomination PDG EDF | INTÉGRALE (98 804 car.) |
| 2425/123 | 2025 | Anne-Isabelle Etienvre, administratrice générale CEA | INTÉGRALE (73 717 car.) |

Explication institutionnelle : l'article 13 de la Constitution prévoit que les nominations aux emplois les plus sensibles de l'État (dont les présidents d'EDF, du CEA, d'Orano, de l'INRAE) sont soumises à l'avis de la commission parlementaire compétente, avec un vote public. Ces auditions donnent lieu à un compte rendu écrit intégral (c'est une exigence de transparence du processus de nomination), contrairement aux auditions ordinaires de la commission, qui relèvent d'une pratique de non-transcription.

## 4. Lecture pour le faisceau du dossier

1. **La non-transcription n'est PAS propre à la CRE** : elle est la règle générale de la commission des affaires économiques pour toutes les auditions ordinaires, quel que soit l'auditionné (régulateur, administration, entreprise, ministre, expert). Les régulateurs CRE, Autorité de la concurrence, ARCEP et Médiateur de l'énergie sont TOUS concernés.
2. **La seule exception (art. 13) est significative** : quand le Parlement doit donner un avis de nomination sur un dirigeant public (EDF, CEA, Orano, INRAE), la transcription est intégrale et publique. Quand le régulateur vient rendre compte de sa politique (collecte des coûts ENR, tarifs, contrôle), il n'y a pas de trace écrite. L'asymétrie est structurelle : la transparence suit le pouvoir de nomination du Parlement, pas le pouvoir de rendre compte des régulateurs.
3. **Conséquence pour le fil** : la position orale de Wargon sur la collecte des coûts (rec. n°1 CdC) reste confinée à la vidéo (transcription whisper en cours, 23-20) ; la position de Cœuré (ADLC) sur la concurrence dans les ENR, de La Raudière (ARCEP) et des médiateurs de l'énergie est dans le même confinement vidéo. Le motif « la parole des régulateurs n'existe qu'en vidéo » est généralisé et renforce le critère 7 de la grille (opacité structurelle).
4. **Réutilisabilité** : le scan des 281 CR confirme que la méthode « scan des CR de commission + vérification de la mention d'absence » fonctionne à la source primaire pour cartographier les auditions de n'importe quelle commission de l'AN.

## 5. Contre-test des autres commissions (ARCOM → commission culture, ACPR → commission finances) : ouvert

- La question posée visait aussi ARCOM et ACPR : ces régulateurs sont auditionnés par d'autres commissions (affaires culturelles pour l'ARCOM, finances pour l'ACPR), pas par la commission des affaires économiques.
- Premiers éléments (presse + Google News) : audition d'ARCOM (Martin Ajdari, président) le 08/10/2025 (page AN + LCP), audition ACPR (Jean-Paul Faugère, candidat) au Sénat. Le statut de transcription de ces auditions (CR écrit ou non) dans les commissions culture/finances n'a pas pu être vérifié à la source dans cette passe (le pattern des CR de ces commissions diffère de `cion-eco` et reste à identifier).
- Cette ouverture ne change pas la conclusion sur la commission des affaires économiques : le motif y est généralisé à tous les régulateurs, établi à la source primaire.

## 6. Table de faits

| ID | Proposition | Source | Localisation | Nature | Statut |
|----|-------------|--------|--------------|--------|--------|
| FCT-cr-001 | 281 CR de la commission des affaires économiques ont été téléchargés et lus (160 session 2024-2025 + 121 session 2025-2026) | scan 10/08/2026 | /tmp/cr_pdf_*.pdf | Fait | ÉTABLI |
| FCT-cr-002 | Toutes les auditions ordinaires portent la mention « Ce point de l'ordre du jour n'a pas fait l'objet d'un compte rendu écrit » | 281 CR, vérification phrase | logs scan_reg_*.txt | Fait (pratique) | ÉTABLI |
| FCT-cr-003 | Autorité de la concurrence (Benoît Cœuré) auditionnée le 27/01/2026 (CR 047) SANS CR écrit | CR 047 PDF | renvoi assnat.fr/0CH9yN | Fait | ÉTABLI |
| FCT-cr-004 | ARCEP (Laure de La Raudière) auditionnée le 24/06/2026 (CR 107) SANS CR écrit | CR 107 PDF | renvoi vidéo | Fait | ÉTABLI |
| FCT-cr-005 | Médiateur de l'énergie auditionné 2 fois (Challan-Belval 25/06/2025 CR 2425/116, Doroszczuk 13/05/2026 CR 2526/091) SANS CR écrit | CR 116 + CR 091 PDF | assnat.fr/2A455Q + dc81n5 | Fait | ÉTABLI |
| FCT-cr-006 | DGCCRF + DGDDI auditionnées le 20/01/2026 (CR 044+045) SANS CR écrit | CR 044/045 PDF | renvoi vidéo | Fait | ÉTABLI |
| FCT-cr-007 | Les auditions ordinaires de ministres, entreprises, experts sont également sans CR écrit (Bpifrance, Saint-Gobain, Carrefour, CMA CGM, E.Leclerc, FFB, etc.) | échantillon 20 CR | §2.2 | Fait | ÉTABLI |
| FCT-cr-008 | Les auditions en application de l'article 13 de la Constitution (nominations présidentielles) sont TOUTES transcrites intégralement | CR 2526/006+046+074, 2425/006+085+086+123 | §3, 69 000-115 000 car. | Fait (exception) | ÉTABLI |
| FCT-cr-009 | L'audition art. 13 de Claude Imauven (Orano, 21/01/2026, CR 046) est transcrite intégralement avec vote (21 pages, 66 554 car.) | CR 046 PDF | §3 | Fait | ÉTABLI |
| FCT-cr-010 | La non-transcription n'est PAS propre à la CRE : elle est la règle générale des auditions ordinaires de la commission des affaires économiques | synthèse des 281 CR | §4 | Fait (généralisation) | ÉTABLI |
| FCT-cr-011 | La transparence suit le pouvoir de nomination du Parlement (art. 13 transcrit) mais pas le pouvoir de rendre compte des régulateurs (auditions ordinaires non transcrites) | analyse | §4.2 | Inférence | CORROBORÉ |
| FCT-cr-012 | Le contre-test des commissions culture (ARCOM) et finances (ACPR) reste ouvert : pattern des CR différent de cion-eco, à identifier | recherche web 10/08/2026 | §5 | Limite | PARTIEL |

## 7. Grille de verdict 3 axes (doctrine §13)

```text
PÉNAL    : 0 fait. La non-transcription des auditions est une pratique parlementaire, pas une infraction.
LÉGAL    : oui. Le règlement de l'AN permet que les auditions ordinaires ne donnent pas lieu à CR écrit.
LÉGITIME : contestable et STRUCTURELLEMENT ASYMÉTRIQUE. Le Parlement transcrit intégralement les auditions où il détient un pouvoir (art. 13, nominations EDF/CEA/Orano/INRAE) mais ne transcrit AUCUNE audition ordinaire, y compris celles où le régulateur rend compte de l'argent public (Wargon sur 1,2 Md€ de soutien ENR, Cœuré sur la concurrence, La Raudière sur les télécoms). La parole des régulateurs existe uniquement en vidéo non indexable (confirmé : aucune piste de sous-titres, 23-20). Critère 7 de la grille (opacité) renforcé, généralisé à tous les régulateurs.
```

## 8. Conclusion graduée

Le GAP est résolu : la non-transcription des auditions de la commission des affaires économiques est **généralisée à tous les régulateurs et à toutes les auditions ordinaires**, établie à la source primaire sur 281 CR (2 sessions complètes). Les régulateurs concernés : CRE (Wargon), Autorité de la concurrence (Cœuré), ARCEP (La Raudière), Médiateur de l'énergie (×2), et les administrations DGCCRF/DGDDI. La seule exception est l'article 13 de la Constitution (nominations présidentielles), transcrites intégralement. L'asymétrie est structurelle : la transparence suit le pouvoir de nomination du Parlement, pas le pouvoir de rendre compte des régulateurs. Pour le fil Valeco/EnBW, la position orale de Wargon sur la collecte des coûts reste confinée à la vidéo (transcription whisper en cours, 23-20) : le motif d'opacité est désormais documenté comme général, pas spécifique. Contre-test restant : commissions culture/finances (ARCOM/ACPR), pattern de CR à identifier.

## 9. Sources

1. 281 comptes rendus de la commission des affaires économiques (sessions 2024-2025 et 2025-2026) : `https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/cion-eco/l17cion-eco{session}{n:03d}_compte-rendu.pdf`, téléchargés et lus 10/08/2026 (artefacts /tmp/cr_pdf_*.pdf, logs /tmp/scan_reg_log.txt et /tmp/scan_reg_2425_log.txt).
2. CR 047 (27/01/2026) : audition Benoît Cœuré, Autorité de la concurrence.
3. CR 107 (24/06/2026) : audition Laure de La Raudière, ARCEP.
4. CR 091 (13/05/2026) et 2425/116 (25/06/2025) : auditions Médiateur de l'énergie.
5. CR 046 (21/01/2026) : audition art. 13 Claude Imauven (Orano), transcrite intégralement.
6. CR 2526/006, 074, 2425/006, 085, 086, 123 : auditions art. 13 (EDF, CEA, INRAE), transcrites intégralement.
7. Documents croisés : 22-38 (GAP-ll2-2, CR 81 Wargon), 23-20 (transcription whisper, pas de sous-titres), 21-58 (GAP-ll2), 22-30 (fascicule réponses CdC).
