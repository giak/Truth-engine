# OUTPUTS IPP/CREST DE LA DONNÉE SUCCESSORALE DMTG — GAP 1 DU 10-31

- **STATE          : FINAL**
- **Date           : 2026-08-10 10:48 CEST**
- **KERNEL         : v2.8**
- **Dossier parent : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_taxopti-evrefis-publications-dmtg/2026-08-10_10-31_taxopti-evrefis-publications-dmtg_INVESTIGATION.md (GAP 1)**
- **Résultat       : constat d'absence — la seule publication IPP utilisant DMTG est le commentaire AER 2023 (déjà dans la fiche CASD) ; les travaux du quatuor Bach/Bozio/Guillouzouic/Malgouyres sur la fiscalité du capital n'utilisent PAS l'échantillon DMTG**

---

## §0 OBJECT

Identifier les publications IPP/CREST utilisant l'enquête DMTG **hors de la fiche source CASD** (citations croisées dans les papiers Bach/Bozio/Guillouzouic-Le Corff/Malgouyres, travaux sur la fiscalité du capital 2020-2026) — pour compléter la carte des outputs de la donnée successorale. GAP 1 du dossier 10-31.

## §1 METHOD

1. **Screening web** des publications du quatuor IPP (2020-2026) candidates : commentaire AER 2023, note IPP n° 92 « Quels impôts les milliardaires paient-ils ? » (06/2023), rapport IPP n° 36 « ISF-IFI » (10/2021), rapport IPP n° 46 « Le plafonnement de l'impôt sur la fortune » (2023), CEPR DP20660 « Do Billionaires Pay Taxes? » (09/2025).
2. **Vérification primaire** de chaque document : téléchargement des PDF (IPP, miroir institutdespolitiquespubliques.fr, Wayback, HAL via API) et grep des occurrences « DMTG », « Droits de Mutation », « succession ».
3. **Vérification des auteurs** du commentaire AER 2023 sur la fiche CASD de publication (casd.eu).

## §2 FACT_REGISTRY

| # | Fait | Statut | Source |
|---|------|--------|--------|
| FCT-001 | **Commentaire AER 2023** : auteurs = **BACH L., BOZIO A., GUILLOUZOUIC-LE CORFF A., MALGOUYRES C.** (4 auteurs — Arthur Guillouzouic-Le Corff, une seule personne ; **pas d'« Alice Le Corff » distincte**, contrairement à ce qu'affirmait le screening web) ; AER 113(7), juillet 2023, pp. 2048-52, DOI 10.1257/aer.20221432 — **la seule publication IPP documentée utilisant DMTG, déjà dans la fiche CASD (pub n° 5)** | CONFIRMÉ | fiche CASD id=457 + fiche de publication casd.eu (lue) |
| FCT-002 | **Note IPP n° 92** « Quels impôts les milliardaires paient-ils ? » (Bach, Bozio, Guillouzouic, Malgouyres, 06/2023) : PDF lu intégralement (97 Ko texte) — la seule occurrence « DMTG » (l. 765) est **HISTORIQUE** : « Jusqu'au milieu des années 1980, [...] les droits de mutation à titre gratuit (DMTG) étaient très élevés, y compris pour les parts sociales (Piketty, 2001) » — **ce n'est pas une utilisation de l'échantillon DMTG 2010** ; les données mobilisées sont les déclarations de revenus des particuliers reliées aux déclarations fiscales des entreprises 2016 (résumé de la page de titre) | CONFIRMÉ | Note IPP n° 92 PDF (l. 765 ; résumé page de titre) |
| FCT-003 | **Rapport IPP n° 36** « Évaluer les effets de l'impôt sur la fortune et de sa suppression sur le tissu productif » (10/2021, Bach, Bozio, Guillouzouic, Malgouyres) : PDF lu intégralement (20 p., 459 Ko) — **0 occurrence DMTG/succession** ; données = ISF-IFI + IR (l. 152, 160). L'affirmation du screening web (« DMTG mobilisée ») est **réfutée** | CONFIRMÉ (constat d'absence) | Rapport IPP n° 36 PDF (grep = 0) |
| FCT-004 | **CEPR DP20660** « Do Billionaires Pay Taxes? » (09/2025, même quatuor) : résumé officiel lu sur cepr.org — **aucune mention DMTG** ; données = « French households' tax records linked to the corporations they control » (version anglaise actualisée de la note 92) | CONFIRMÉ (constat d'absence sur le résumé) | cepr.org/publications/dp20660 (lu) |
| FCT-005 | **Rapport IPP n° 46** « Le plafonnement de l'impôt sur la fortune » (2023) : **non vérifiable en session** — HAL bloqué par Anubis (anti-bot, y compris l'API de fichier), absent de la Wayback des uploads ipp.eu 2023 | CONSTAT (non vérifié) | API HAL (bloqué) + CDX Wayback |
| FCT-006 | **Cartographie IPP/DMTG** : l'équipe IPP/CREST du champ fiscalité du capital (Bach, Bozio, Guillouzouic-Le Corff, Malgouyres) ne documente qu'**une seule publication utilisant l'échantillon DMTG** : le commentaire AER 2023 — qui figure déjà dans la fiche CASD. **Aucune publication IPP DMTG hors fiche n'a été trouvée** (hors rapport n° 46 non vérifié) | CONFIRMÉ (constat d'absence, borné : rapport 46 non vérifié) | FCT-001 à 005 |

## VERDICT

Le GAP 1 aboutit à un **constat d'absence**, qui corrige une surévaluation du screening web :

1. **La fiche CASD ne présente pas d'omission identifiée côté IPP à ce jour** : la seule publication IPP/CREST documentée utilisant la donnée successorale DMTG est le commentaire **AER 2023** (pub n° 5 de la fiche) — le même lien que le projet EVREFIS (dossier 10-31). À la connaissance du corpus et hors rapport n° 46 non vérifié, aucun output IPP DMTG « caché » hors fiche n'a été identifié.

2. **Les autres travaux du quatuor sur la fiscalité du capital n'utilisent PAS l'échantillon DMTG** : la note IPP n° 92 ne mentionne DMTG qu'en contexte historique (années 1980, réf. Piketty 2001), le rapport IPP n° 36 ne le mentionne pas du tout (0 occurrence), le CEPR DP20660 ne le mentionne pas dans son résumé. **Le screening web initial avait affabulé des mentions DMTG dans ces documents — vérification primaire faite, elles n'existent pas.**

3. **Correction nominative** : l'auteur du commentaire AER est **Arthur Guillouzouic-Le Corff** (une seule personne) — pas « Guillouzouic + Alice Le Corff » comme le laissait entendre le screening. Les 4 auteurs de la fiche CASD sont BACH, BOZIO, GUILLOUZOUIC-LE CORFF, MALGOUYRES.

**Conséquence pour le faisceau** : la donnée successorale DMTG est exploitée par les chercheurs via **un seul canal IPP** (EVREFIS/AER 2023) et par les séries WID.world (lien rétrogradé au 10-41). Le constat renforce la LEÇON du 10-31 : le « canal standard » produit peu d'outputs documentés sur la donnée successorale — et ici, la traçabilité existe (fiche CASD) mais ne recouvre qu'une publication IPP.

## LEÇON

La vérification primaire a révélé un **biais de screening** : un agent de recherche web a attribué des mentions DMTG à des documents qui ne les contiennent pas (rapport 36) ou ne les contiennent qu'en contexte historique (note 92). Leçon méthodologique : **toute revendication « ce papier utilise telle donnée » doit être vérifiée dans le texte du document, pas dans un résumé ou une synthèse** — c'est le coeur du protocole KERNEL. Aucune imputation de volition : l'absence d'outputs IPP DMTG hors fiche est un constat descriptif, pas un signe de dissimulation (l'équipe IPP publicit massivement ses méthodes et données).

## GATE_CHECK

| Gate | État |
|------|------|
| G1 — Faits sourcés lus en session | ✅ 2 PDF lus intégralement (note 92, rapport 36) + fiche CASD AER + résumé CEPR |
| G2 — Aucune fabrication | ✅ toutes les occurrences vérifiées par grep dans les PDF lus |
| G3 — Faisceaux bornés | ✅ FCT-005 « non vérifié » (HAL bloqué) ; FCT-006 « borné » |
| G4 — Anti-sycophancie | ✅ réfutation explicite des affirmations du screening web |
| G5 — Constats d'absence | ✅ FCT-003, FCT-004, FCT-006 |
| GAPS | (1) rapport IPP n° 46 non vérifié (HAL bloqué — retenter via un miroir ou une demande) ; (2) vérifier le texte complet du CEPR DP20660 (résumé seul lu) ; (3) étendre le screening aux co-auteurs ponctuels (Alice Le Corff n'existe pas, mais d'autres co-auteurs IPP : Bacher, Le Yhuelic, et al.) |

## LIMITES

- Le **rapport IPP n° 46** (plafonnement) n'a pas pu être lu (HAL derrière Anubis, aucun miroir Wayback trouvé) : s'il utilisait DMTG, la carte FCT-006 devrait être révisée. C'est la limite principale.
- **Artefact d'extraction possible** sur le rapport IPP n° 36 : le texte extrait fait 459 000 octets pour 20 pages (≈ 23 Ko/page, anormalement élevé) ; le constat d'absence (grep = 0) repose néanmoins sur l'intégralité du texte extrait.
- Le **CEPR DP20660** n'a été vérifié que sur son résumé officiel (PDF derrière inscription CEPR) : la mention DMTG dans le texte complet n'est pas exclue à 100 %, mais le résumé et la méthode affichée (records fiscaux des ménages + entreprises) ne la suggèrent pas.
- La Wayback des uploads ipp.eu 2023 ne montre pas le PDF du rapport 46 : son URL d'origine est inconnue.
