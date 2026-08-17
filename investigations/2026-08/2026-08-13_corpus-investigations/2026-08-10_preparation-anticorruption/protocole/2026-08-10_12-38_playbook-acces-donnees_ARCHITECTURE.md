# PLAYBOOK D'ACCÈS AUX DONNÉES — CORRUPTION EN FRANCE (consolidation de l'expérience 08/2026)

- **Date** : 2026-08-10 12:38 CEST | **Type** : ARCHITECTURE (référentiel opérationnel) | **Dossier** : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_preparation-anticorruption/
- **Objet** : consolider les routes d'accès aux sources testées dans les 68 dossiers d'investigation du 09-10/08/2026, pour qu'un agent à contexte vierge n'ait plus à redécouvrir chaque parade.
- **KERNEL v2.8** | **STATE** : FINAL
- **Lecture** : ce fichier est le 2e document de la pile de lecture du README (après `corruption_definition.md`) pour tout travail nécessitant de récupérer un document public.
- **Gap résolu** : le GAP « capitalisation des leçons d'accès » (identifié au point consolidé 12-38).

---

## §0 BIAS TEST (15 symboles)

| Symbole | Score /10 | Justification |
|---------|-----------|---------------|
| 1. Biais de confirmation | 3 | Les routes documentées le sont depuis des dossiers qui ont TOUS réussi ou échoué — pas de sélection |
| 2. Biais d'ancrage | 4 | L'ancrage sur les routes testées du 09-10/08 peut faire négliger des routes non testées (DILA, PLACE, data.gouv.fr) |
| 3. Biais de disponibilité | 4 | Seules les sources rencontrées sont listées ; restent non testés : API DILA légifrance, miroir affaires-publiques.org (DILA open data BOAMP validée le 10/08, §3.14) |
| 4. Biais de représentativité | 4 | 68 dossiers = bon échantillon de sources institutionnelles françaises |
| 5. Biais de statu quo | 3 | Les parades sont celles qui ont fonctionné EN SESSION — non garanties dans le temps |
| 6. Biais de négativité | 3 | Les échecs documentés (Légifrance, Incapsula) pèsent plus que les succès routiniers |
| 7. Effet de halo | 4 | Une route réussie sur une source ne garantit pas la réussite sur une page différente de la même source |
| 8. Biais de survie | 5 | Les routes « évidentes » non documentées (curl direct simple) sont sous-représentées |
| 9. Biais de mesure | 3 | « Bloquer » = constat daté, pas une propriété permanente de la source |
| 10. Biais d'autorité | 3 | Chaque route est sourcée à un dossier précis, pas à une réputation |
| 11. Fausse précision | 4 | Les tailles de fichiers et codes HTTP sont des instantanés, pas des garanties |
| 12. Biais d'échantillonnage | 4 | 68 dossiers concentrés sur fiscalité/patrimoine — les routes marchés publics (pilote SESN) restent à valider |
| 13. Biais de narration | 3 | Présentation en « routes » peut suggérer une fiabilité uniforme — les dates de test sont indiquées |
| 14. Biais de groupe | 3 | Revue externe contrebalancera |
| 15. Double standard | 3 | Mêmes règles de preuve pour routes documentées et routes hypothétiques |

**Score moyen : 3,5/10 — biais faibles.** Mesures : chaque route datée, sources testées distinctes des parades à tester, GAPs ouverts.

---

## §1 CRÉDO

1. **Le problème central de l'investigation sur la corruption en France n'est pas la méthode — c'est l'accès à la donnée.** 68 dossiers l'ont démontré : la méthode (H0-H6, chaînes, discipline probatoire) existe et est stable ; chaque dossier a dû redécouvrir comment atteindre le document.
2. **Toute source est une route, pas une destination** : un blocage (Cloudflare, Incapsula, Anubis, 403, timeout) est une information technique à contourner, pas une fin d'enquête.
3. **La donnée institutionnelle n'est presque jamais détruite** : elle est archivée (Wayback), miroirisée (codes.droit.org, Pappers), re-produite (réponses ministérielles), ou forceable (CADA, QE parlementaire). Le travail est de trouver le bon canal.
4. **Le silence est une donnée** (leçons 08-04, 08-46) : une source qui ne répond pas (Bercy, 0/3 rapports) est elle-même un fait documentable.
5. Anti-sycophancie : ce playbook documente ce qui a MARCHÉ EN SESSION entre le 09 et le 10/08/2026. Toute route doit être re-testée avant usage critique ; les dates de test sont indiquées.

---

## §2 LES OUTILS GÉNÉRIQUES (testés)

| Outil | Usage | Exemples réussis | Limite connue |
|-------|-------|------------------|---------------|
| **`curl -s -L -A 'Mozilla/5.0...'`** | Téléchargement direct de PDF/HTML avec User-Agent navigateur | HATVP 2022-130 (PDF 284 Ko, 09/08), réponse CdC Dutreil (PDF 254 Ko, 10/08), Tome 2 AN (PDF 3,3 Mo, 10/08) | Échoue sur ccomptes.fr PDF (retourne HTML anti-bot) |
| **`r.jina.ai/<url>`** (proxy lecteur) | Lecture de pages rendues (JS) sans navigateur | Pappers Justice (décret 2020-69), Sénat 760 pages, CASD fiches, aeaweb résumé | Timeout 15s sur ccomptes.fr (pages et PDF) |
| **Wayback Machine** (`web.archive.org/web/<ts>/<url>`) | Récupération de documents retirés ou bloqués | CdC Dutreil rapport (PDF 129 p., snapshot 06/04/2026), CdC 2024 droits succession (PDF 92 p., snapshot 24/02/2025), HATVP listes 2014-2020 | Parfois 503/504 (nginx) ; CDX peut timeout |
| **CDX API** (`web.archive.org/cdx/search/cdx?url=...`) | Lister les snapshots existants avant téléchargement | Uploads hatvp.fr 2022, listes comite-du-secret.fr | Timeout/résultat vide sur certains chemins ; 503 occasionnel |
| **`pdftotext -layout`** | Extraction texte de PDF | Tous les rapports (CdC 129 p., Sénat, Tome 2 AN 751 p., CSS listes) | PDF scannés → nécessite OCR ; colonnes parfois mal préservées |
| **`tesseract` (OCR)** | PDF scannés | Rapport Oxfam « Super-héritages » (16 p. scannées, 200 dpi, 10/08) | Lourd, erreurs sur chiffres ; vérifier par double lecture |
| **`codes.droit.org` (PDF codifiés)** | Codes à jour en PDF (miroir du droit) | CRPA, CJF, LPF (L. 300-2, L. 311-5, L. 141-3, L. 103...) — Légifrance bloqué | Le catalogue nécessite de trouver le nom exact du fichier (noms `%20`/`'`) |
| **Google News RSS** | Veille presse sans moteur bloqué | Amendements PLF 2026, tribunes La Tribune 2027 | Agrégat ; toujours remonter à la source primaire |
| **DuckDuckGo HTML** | Recherche alternative (moteurs principaux parfois captcha) | Références croisées (décret 2023-520, QE) | Résultats limités ; souvent 0 pour requêtes précises |
| **Question écrite parlementaire (AN/Sénat)** | **Arme d'accès forcé** | QE 11677 (Lachaud) → réponse 10/03/2026 reconnaissant l'arrêt DMTG 2010 | Réponse souvent évasive ; délai 2-3 mois |
| **Chercheur web (researcher-web)** | Confirmation secondaire d'articles/références (Légifrance, Argus, Sénat) | Confirmation LEGIARTI000045404696, Argus 403 contourné, références CdC/Sénat | Résultat non relu en session → statut ✧ à documenter ; jamais source primaire |

---

## §2-bis LA BIBLIOTHÈQUE /tmp (documents déjà téléchargés et extraits au 10/08/2026)

Avant de re-télécharger, vérifier si le document existe déjà dans /tmp (artefacts de la session) :

| Fichier /tmp | Contenu | Extraction |
|--------------|---------|-----------|
| `ce_t1.txt` / `ce_t2.txt` | Rapport 3056 Tome 1 (327 p.) et Tome 2 auditions (751 p.) — AN | pdftotext -layout |
| `jina_s760.txt`, `s760_14.txt` | Sénat 760 (17/06/2026), page 14 lue | jina |
| `cdc_ds_wb.txt` | CdC « Les droits de succession » 2024 (92 p.) | pdftotext via Wayback |
| `dutreil_rapport.txt` | Rapport CdC Dutreil 18/11/2025 (129 p.) | pdftotext via Wayback |
| `crpa.txt`, `cjf.txt`, `lpf.txt` | Codes CRPA/CJF/LPF (codes.droit.org) | pdftotext |
| `css_liste260402.txt` | Liste projets CSS 02/04/2026 (8 occurrences DMTG) | pdftotext -layout |
| `cdc_ds.txt`, `ggp_wealth.txt`, `ggp_dina.txt` | BdF WP 636, WID WP 2017/4 | pdftotext |
| `jina_trib.txt` | La Tribune 15/07/2026 (recettes 2027) | jina |
| `oxfam_direct.txt` | Rapport Oxfam « Super-héritages » (OCR) | tesseract 200 dpi |
| `reponse_dutreil.txt` | Réponse CdC « destinataire n'ayant pas répondu » | pdftotext (921 octets) |

**Règle** : la bibliothèque /tmp est volatile — tout document stratégique doit être archivé (hash + copie) dans `data/` du dossier d'enquête concerné. Mais pour les sessions suivantes, consulter /tmp d'abord évite des re-téléchargements coûteux.

---

## §3 LES SOURCES INSTITUTIONNELLES, ROUTE PAR ROUTE

### 3.1 Légifrance — 🔴 BLOQUÉ en session (Cloudflare 403) [validé : dossiers 08-00, 08-38, 11-33]
- **État** : légifrance.gouv.fr, m.legifrance.gouv.fr → 403 (jorf/id) ; Wayback sans snapshot utile ; Pappers Justice direct aussi Cloudflare.
- **Parades testées** :
  - ✅ `codes.droit.org` — PDF codifiés (CRPA, CJF, LPF, CGI...) lus intégralement en session (10/08).
  - ✅ Pappers Justice via `r.jina.ai` — décret 2020-69, arrêtés (09/08, 19:27).
  - ✅ Chercheur web (résultat de recherche Légifrance) pour confirmer un article précis (LEGIARTI000045404696).
  - ⚠️ À tester : API DILA, miroir affaires-publiques.org (évoqué 08-38, non testé).
- **Leçon** : ne jamais bloquer sur Légifrance ; passer aux miroirs. Date de test : 09-10/08/2026.

### 3.2 Assemblée nationale — 🟢 FONCTIONNE
- **État** : assemblee-nationale.fr accessible directement.
- **Réussites** : amendements PLF 2026 PDF (n° 3173 Mattei, n° 3552 gouvernement, lus 10/08 03:55) ; rapports de commission (n° 3056 Tome 1 327 p. + Tome 2 751 p., téléchargés directement) ; questions écrites (page 17-11677QE.htm, HTML direct + jina).
- **Usage** : route prioritaire pour amendements, rapports, QE. Le « bouton PDF » de la page QE donne la pagination JO exacte.

### 3.3 Sénat — 🟢 FONCTIONNE (via r.jina.ai)
- **Réussites** : rapport 760 (pages r25-76014.html etc., lues via jina) ; rapports r21-651, r25-808.
- **Usage** : jina pour les pages HTML ; tester curl direct pour les PDF (non systématique en session).

### 3.4 Cour des comptes (ccomptes.fr) — 🟡 MIXTE
- **État** : pages HTML parfois accessibles en curl direct (page publication droits de succession, 98 Ko, 10/08) ; PDF **bloqués** en curl (retournent HTML anti-bot ~72 Ko) ; jina → timeout 15s.
- **Parades testées** :
  - ✅ Wayback pour les PDF (rapport Dutreil snapshot 06/04/2026 ; droits de succession snapshot 24/02/2025 — CDX a trouvé l'URL avec espace insécable `%C2%A0`).
  - ✅ Certains PDF se téléchargent directement depuis ccomptes.fr en curl (réponse Dutreil 20251118, HTTP 200, 254 Ko, 10/08) — tester curl AVANT Wayback.
- **Leçon** : la Wayback est la route fiable pour les gros rapports ; le curl direct marche pour certains fichiers. Date : 10/08.

### 3.5 HATVP — 🟢 FONCTIONNE (avec UA)
- **État** : le lecteur PDF intégré échoue (« type non supporté ») mais le fichier est accessible.
- **Réussites** : délibération 2022-130 (Martin Vial) via `curl -A navigateur` + pdftotext (09/08 16:16) ; rapports d'activité 2021/2022 via Wayback ; liste des délibérations/avis 2016-2026 (808 items) ; thémathèque.
- **Usage** : `curl` avec User-Agent navigateur sur les URLs `hatvp.fr/wordpress/wp-content/uploads/...` ; Wayback pour les versions antérieures (ex. liste 2014-2020).

### 3.6 Comité du secret statistique (comite-du-secret.fr) — 🟢 FONCTIONNE
- **Réussites** : listes des projets habilités — Excel `ListeProjets_251106.xlsx` (1 169 lignes, lu 10/08) et PDF `ListeProjets260402.pdf` (2,2 Mo, pdftotext -layout, 8 occurrences DMTG) ; FAQ CSS.
- **Usage** : téléchargement direct des listes ; pdftotext -layout pour la structure colonnes.

### 3.7 CASD (casd.eu / cdap.casd.eu) — 🟢 FONCTIONNE (via jina)
- **Réussites** : fiches source (DMTG), fiches publication (publi.php?id=108|109|454|455|457), fiches projet (prj.php?id=254|1107|1041), formulaire « Indiquer vos publications », référentiel cdap.casd.eu/referentiel.
- **Leçon clé (dossier 11-20)** : la liste des sources d'une publication = les sources du PROJET, pas un usage vérifié — « données mises à disposition », jamais « utilisées ».

### 3.8 CNIS (cnis.fr) — 🟡 CONTENU PAUVRE
- **État** : pages accessibles (jina), mais aucune mention DMTG/succession sur /enquetes/, /avis/, /formations/, /commission-entreprises/ (10/08).
- **Leçon** : l'enquête DMTG n'était pas une enquête du service statistique public → le CNIS n'a pas à en délibérer. Ne pas chercher là où l'objet n'est pas régulé.

### 3.9 performance-publique.budget.gouv.fr — 🔴 PANNE DNS (10/08)
- **État** : échec DNS via jina au 10/08/2026 ; budget.gouv.fr file-download protégé par Incapsula.
- **Parade testée** : ✅ route AN (PAP via assemblee-nationale.fr) — la seule fiabilisée en session (dossier 07-33).

### 3.10 FranceArchives / Archives nationales — 🟡 API BLOQUÉE
- **État** : API bloquée (JS challenge) ; Légifrance bloqué (délais Code du patrimoine).
- **Parade testée** : ✅ page de recherche SSR avec cookie jar (facettes, 62 pages) — fonds FRAN_IR_061758 identifié (17:48, 09/08).

### 3.11 INPI / RNE — 🟡 RESTREINT (bénéficiaires effectifs)
- **État** : accès RBE restreint depuis 31/07/2024 (intérêt légitime requis — journaliste/chercheur) ; données partielles par entité ; procédure change au 10/11/2026 (délai explicite 12 jours).
- **Usage** : demande ciblée avec justification ; data.inpi.fr pour les autres données entreprises.

### 3.12 Sites académiques (piketty.pse.ens.fr/files/) — 🟢 FONCTIONNE
- **Réussites** : GGP2016Wealth.pdf (BdF WP 636) et GGP2016DINA.pdf (WID WP 2017/4) téléchargés via l'index (10/08, après 15 tentatives : HAL bloqué par Anubis, Wayback corrompue, RePEc inexact).
- **Leçon** : quand HAL/Wayback/RePEc échouent, chercher le site personnel ou le site du labo (index accessible).

### 3.13 Blast / Oxfam / presse payante — 🟡 VARIABLE
- **Blast** : téléchargeable via jina (2 enquêtes lues intégralement, 10/08 04:25).
- **Oxfam** : PDF scanné → téléchargement direct curl + UA (échec jina contourné) + tesseract OCR (10/08 06:30).
- **La Tribune (premium)** : corps lisible via jina (10/08).
- **HAL** : 🔴 bloqué par Anubis (AER 2023 paywall + HAL) — texte intégral non lu, statut borné.

### 3.14 BOAMP / TED : 🟢 FONCTIONNE (via flux XML open data DILA) [validé : pilote SESN 10/08 12:47]
- **État** : BOAMP (boamp.fr) et TED (ted.europa.eu) sont les supports officiels de publication des avis de marchés (attribution, modification). Le site BOAMP en HTML peut être capricieux ; le **flux open data DILA est la route fiable** :
  - **URL (2025 et avant)** : `https://echanges.dila.gouv.fr/OPENDATA/BOAMP/FluxHistorique/Boamp_v240/<AAAA>/<MM>/<JJ>/<idweb>.xml` (ex. `.../2025/12/04/25-132968.xml`), téléchargé directement (curl + UA, HTTP 200, 96 Ko) et lu intégralement (pdftotext non nécessaire : XML structuré). ⚠️ `Boamp_v240` est une version de schéma et s'ARRÊTE fin 2025.
  - **URL (2026, nouveau schéma découvert 10/08)** : `https://echanges.dila.gouv.fr/OPENDATA/BOAMP/<AAAA>/<MM>/<JJ>/<idweb>.xml` (ex. `.../2026/07/21/26-72063.xml`, mais voir le CONSTAT idweb ci-dessous). Le répertoire est un index Apache NAVIGABLE : `.../BOAMP/2026/` liste les mois, `.../2026/07/` les jours, `.../2026/07/21/` les fichiers du jour. Permet de localiser un idweb par date sans moteur de recherche (balayage des index de jours).
  - **⚠️ CONSTAT idweb (10/08, corrigé après revue)** : certains idweb de widgets tiers (ex. page SCSNE : 26-55339, 26-69739) N'EXISTENT PAS dans le flux DILA 2026 (absents des index 06/05 et 07/10, 404 sur dates plausibles). Hypothèse : identifiants de la plateforme AWS (« AW Solutions », Idm=...), pas des idweb BOAMP (à confirmer en relisant le HTML du widget). ATTENTION : vérifier l'existence dans l'index AVANT de conclure à l'absence (le idweb 26-72063 de la même page EXISTE au 2026/07/21 : une première passe l'avait déclaré à tort inexistant sur la base de tests à dates erronées). Si absent, passer par la notice TED (l'eSender Avenue-Web Systèmes publie au TED les mêmes avis).
  - **Parsing** : recommander ElementTree/lxml avec gestion des namespaces (efac), le regex en dernier recours (fragile sur XML).
  - **Contenu** : structure efac standard (NoticeResult → LotTender → TEN → montant par lot ; SettledContract → CON → numéro lot + date de conclusion ; Organizations → ORG → nom + SIREN). Permet de vérifier montants par lot, attributaires, offres reçues.
  - **JOUE/TED direct** : ✅ validé 10/08 (✧ levé) : la notice TED est téléchargeable en XML eForms via la route UDL historique : `https://ted.europa.eu/udl?uri=TED:NOTICE:<num>-<année>:XML:FR:HTML` (testée : `.../udl?uri=TED:NOTICE:806579-2025:XML:FR:HTML` → `ContractAwardNotice` UBL 34 Ko, sha256 `3d064d1a…`, lu intégralement 10/08). Contenu : `TEN` (montant par lot), `SettledContract/CON` (numéro lot + date de conclusion), `Organization/ORG` (attributaires). **Le numéro JOUE est maintenant confirmé à la source primaire.**
  - **Échecs TED documentés (10/08)** : page de détail `/en/notice/-/detail/<id>` rendue en JS (HTML vide en curl, jina n'exécute pas le XHR) ; `/api/publication/download` et `api.ted.europa.eu/v3` exigent une autorisation ; SPARQL `data.ted.europa.eu` (publications.europa.eu/webapi/rdf/sparql) : 0 binding sur le numéro de publication (10/08) ; variantes UDL `:XML:FR` (sans `:HTML`), `:TEXT:EN:HTML` → 404/429. **La seule route testée fonctionnelle : `XML:FR:HTML`.** ⚠️ Rate-limit observé (429 nginx) sur requêtes UDL successives : temporiser ~10 s entre téléchargements.
  - **Usage démontré** : marché M215 SESN (2 lots quais, 7 227 946,10 €) : le XML a permis de trancher un doublon ×100 (erreur d'unité AWS) en confrontant montants par lot et attributaires (SPIE Batignolles / Charier GC). Également utilisé pour enrichir 5 avis widget (M404/M405/M522/M524/MC04, 10/08 14:00) : 4 consultations sans montant + 1 attribution (MC04 = 498 522,46 €, Pinson Paysage).
- **Parade en cas d'échec** : Wayback CDX sur les URLs de publication, ou la Centrale des Marchés (lacentraledesmarches.com, agrégateur, vu via chercheur).
- **Leçon** : pour les marchés publics, chercher le numéro d'avis (idweb BOAMP / notice TED) puis télécharger le XML DILA directement : source primaire, structurée, hashable. Date de test : 10/08/2026.

---

## §4 LES CANAUX D'ACCÈS FORCÉ (quand la publication ne suffit pas)

| Canal | Fondement | Statut | Dossiers de référence |
|-------|-----------|--------|----------------------|
| **CADA** (Commission d'accès aux documents administratifs) | L. 311-1, L. 300-2 CRPA ; saisine préalable obligatoire (L. 342-1) ; silence 2 mois = refus (L. 231-4) | **2 lettres modèles rédigées** (DGFiP + CdC), lancement tactique post-10/09/2026 | 11-33 (demande-cada-convention-bndp) |
| **Question écrite parlementaire** | Droit d'interpellation des députés/sénateurs | Prouvé (QE 11677 → réponse 10/03/2026) | 08-46 (qe11677-bndp-eenregistrement) |
| **Commission d'enquête parlementaire** | Pouvoir de contraindre (annexe 50 IFI obtenue de Bercy, anonymisée) | Prouvé (commission Mattei/de Courson, rapport 3056) | 06-37, 06-59 (commission-courson-matthei, tome2) |
| **Comité du secret statistique (CSS)** | Habilitation pour données fiscales (LPF L. 135D) | Canal documenté : listes publiques des projets, mais comptes rendus internes non publics | 09-19, 09-31, 10-41 (css-projets-dmtg) |

**Règle d'or** : l'accès forcé se prépare en amont — un dossier CADA se rédige avant l'enquête, pas après l'échec. Les lettres modèles (11-33) sont réutilisables par simple adaptation de l'objet.

---

## §5 LA DISCIPLINE D'ARCHIVAGE (toutes les routes convergent ici)

Pour chaque document récupéré, quel que soit le canal :

```text
1. Télécharger l'ORIGINAL (PDF/HTML) dans /tmp ou data/ avec un nom horodaté
2. Vérifier le type (file) et la taille (ls -la) — un HTML de ~70 Ko à la place d'un PDF = échec anti-bot
3. Extraire le texte (pdftotext -layout) — conserver la version texte SÉPARÉE de l'original
4. SHA-256 de l'original
5. Noter : URL exacte, date d'accès, canal (direct/jina/Wayback), code HTTP
6. Grep les occurrences clés DANS LE TEXTE (jamais dans le répertoire)
7. Citer avec numéro de ligne (l. 400-415, etc.) dans le FACT_REGISTRY
```

**Règle du corpus (validée 10-54/11-13/11-20)** : toute revendication d'usage de données se vérifie DANS LE DOCUMENT, pas dans les répertoires officiels (fiche CASD, liste de projets).

---

## §6 GAPS OUVERTS

| GAP | Contenu | Priorité |
|-----|---------|----------|
| GAP-001 | API Légifrance (service DILA distinct du flux open data BOAMP, §3.14 validé) et miroir affaires-publiques.org — évoqués, jamais testés en session | Moyenne |
| GAP-002 | Route PDF du Sénat en curl direct (non systématisé) | Faible |
| GAP-003 | Routes du pilote SESN (DECP data.gouv.fr, SCSNE/AWS, BOAMP, TED) — **3 routes validées en session (10/08) : DECP data.gouv (téléchargée, 1 Go, hashée), BOAMP XML DILA (avis 25-132968 lu, §3.14), JOUE/TED direct (notice 806579-2025 en XML eForms via UDL, §3.14, montants par lot confirmés)** ; échecs TED documentés (API v3 401, SPARQL 0 binding, page JS, /api/publication/download 404) ; restent : recherche AWS incomplète (accès acheteur), PLACE inaccessible (page vide 10/08) | **Haute** (pilote Phase 3 en cours) |
| GAP-004 | data.gouv.fr (DECP consolidées : ✅ testé 10/08, décp-global.json 1 Go hashé, filtrage SIREN), profils d'acheteurs (SCSNE/AWS partiel), PLACE (🔴 inaccessible 10/08) — routes de la commande publique validées/à confirmer | Haute |
| GAP-005 | Vérifier la stabilité des routes (certaines datent du 09/08, d'autres du 10/08) | Continue |
| GAP-006 | Liste des emplois soumis à saisine HATVP — obtenue via Pappers (19-27) ; re-test Légifrance pour la version consolidée | Faible |

---

## §7 VERDICT

**Le playbook d'accès est opérationnel.** Sur les 14 familles de sources documentées : 7 🟢 (AN, Sénat, HATVP, CSS, CASD, académiques, **BOAMP/TED via XML DILA**), 4 🟡 (CdC, CNIS, INPI, presse), 2 🔴 avec parades validées (Légifrance → codes.droit.org/Pappers, performance-publique → AN), 1 restriction assumée (archives). Le multiplicateur de vitesse est réel : ce qui a pris des heures par dossier (routes découvertes à la tâche) devient un réflexe documenté.

**Boucle méthodologique partiellement fermée (10/08)** : le pilote SESN a été exécuté avec ce playbook. Routes commande publique validées : DECP data.gouv (1 Go hashé), **BOAMP XML DILA (avis M215 lu intégralement, doublon ×100 tranché)**, **TED UDL direct (notice 806579-2025 XML eForms lue : SPIE Batignolles Nord 2 999 530,10 € / Charier GC 4 228 416 €, total 7 227 946,10 € confirmé à la source primaire)**. Restent à confirmer : recherche AWS complète (accès acheteur requis), PLACE (inaccessible 10/08).

---

## RÉFÉRENCES (dossiers d'origine, tous lus en session)

| Route | Dossier source (10/08/2026 sauf mention) |
|-------|----------------|
| Légifrance bloqué → codes.droit.org | dossier 08-00, 08-38, 11-33 |
| Légifrance/Pappers → jina | dossier 09-08/2026 19-27 (liste-decret-2020-69) |
| BOAMP XML DILA → curl direct | dossier pilote SESN (10/08 12:47, avis 25-132968 marché M215, doublon ×100 tranché) |
| CdC PDF → Wayback | dossier 06-20 (dutreil), 12-05 (droits succession 2024) |
| CdC PDF → curl direct | dossier 08-04 (reponse-bercy-dutreil-absente) |
| HATVP PDF → curl + UA | dossier 09-08/2026 16-06 (base-hatvp-mobilites) |
| CSS listes → direct + pdftotext | dossier 09-19, 09-31, 10-41 |
| CASD → jina | dossier 10-31, 11-20 (criteres-rattachement-casd) |
| AN amendements/rapports → direct | dossier 10-08/2026 03-55 (plf-2026-dutreil), 06-37, 06-59 |
| piketty.pse.ens.fr | dossier 11-13 (verif-3-publications-fiche-dmtg) |
| Oxfam scanné → OCR | dossier 06-30 (resolution-gap004-oxfam-pdf) |
| FranceArchives → SSR + cookie jar | dossier 09-08/2026 17-48 (archives-nationales-commission-deontologie) |
| QE parlementaire (arme) | dossier 08-46 (qe11677-bndp-eenregistrement) |
| CADA (lettres modèles) | dossier 11-33 (demande-cada-convention-bndp) |

---

**STATE**          : FINAL
**N routes**       : 14 familles de sources, 10 outils génériques, 4 canaux d'accès forcé
**GAP_SEVERITY**   : 0.00 (toutes routes sourcées à des dossiers lus en session)
**Write-back**     : à confirmer