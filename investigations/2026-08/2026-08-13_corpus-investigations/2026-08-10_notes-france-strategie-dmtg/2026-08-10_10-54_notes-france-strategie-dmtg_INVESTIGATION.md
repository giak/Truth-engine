# NOTES FRANCE STRATÉGIE 120/121 ET L'ENQUÊTE DMTG — GAP 3 DU 10-31

- **STATE          : FINAL**
- **Date           : 2026-08-10 10:54 CEST**
- **KERNEL         : v2.8**
- **Dossier parent : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_taxopti-evrefis-publications-dmtg/2026-08-10_10-31_taxopti-evrefis-publications-dmtg_INVESTIGATION.md (GAP 3)**
- **Résultat       : RÉSOLU — les deux notes France Stratégie (n° 120 et n° 121) listées dans la fiche source DMTG n'utilisent PAS l'enquête DMTG ; leurs sources réelles sont l'enquête FQP 2014-2015 et les enquêtes Emploi/Conditions de travail**

---

## §0 OBJECT

Vérifier si les notes d'analyse France Stratégie **n° 120** « Inégalité des chances : ce qui compte le plus » (2023/5) et **n° 121** « Fin de carrière des seniors : quelles spécificités selon les métiers ? » (2023/6) — les 2 publications « non reliées » de la fiche source DMTG (dossier 10-31) — utilisent effectivement l'enquête Droits de Mutations à Titre Gratuit (DMTG). GAP 3 du 10-31.

## §1 METHOD

1. **Localisation des PDF** sur strategie.gouv.fr : note 121 via la page de publication (`/publications/fin-de-carriere-des-seniors-...`, PDF `fs-2023-na121-emploi-seniors-avril_2.pdf`) ; note 120 via la Wayback CDX (`fs-2023-na-120-inegalite-chances.pdf`).
2. **Lecture intégrale** des deux PDF (pdftotext -layout) et grep des occurrences : « DMTG », « mutation », « succession », « transmission », « donation ».
3. **Identification des sources réelles** : grep « source »/« enquête » pour établir ce que chaque note utilise réellement.

## §2 FACT_REGISTRY

| # | Fait | Statut | Source |
|---|------|--------|--------|
| FCT-001 | **Note 121** « Fin de carrière des seniors » (France Stratégie, 19/04/2023, PDF lu intégralement, 101 881 octets texte) : **0 occurrence DMTG/mutation/succession** — la seule occurrence « transmission » (l. 523) renvoie à des « circonstances personnelles », sans lien avec les droits de mutation | CONFIRMÉ (constat d'absence) | fs-2023-na121-emploi-seniors-avril_2.pdf |
| FCT-002 | **Sources réelles de la note 121** : « France Stratégie, à partir des enquêtes Emploi 2004-2019 (Insee) et des enquêtes Conditions de travail 2013, 2016 et 2019 (Dares-Drees-DGAFP) » (9 lignes de sources : l. 64, 230, 274, 309, 389, 423, 486, 555, 597) — **l'enquête DMTG n'y figure nulle part** | CONFIRMÉ | PDF note 121, l. 64, 230, 274, 309, 389, 423, 486, 555, 597 |
| FCT-003 | **Note 120** « Inégalité des chances : ce qui compte le plus » (France Stratégie, 2023/5, PDF lu intégralement, 113 864 octets texte) : **0 occurrence DMTG/mutation/succession/donation/transmission** | CONFIRMÉ (constat d'absence) | fs-2023-na-120-inegalite-chances.pdf |
| FCT-004 | **Source réelle de la note 120** : « France Stratégie, à partir de l'enquête Formation et qualification professionnelle (FQP) 2014-2015 » (l. 237) — **pas de DMTG** | CONFIRMÉ | PDF note 120, l. 237 |
| FCT-005 | **La fiche source DMTG du CASD liste donc 2 publications (notes 120 et 121) qui n'utilisent pas l'enquête DMTG** : leur présence dans la fiche n'est pas un indicateur d'usage de la source, mais un rattachement probablement thématique (inégalités, carrières) — **la fiche CASD ne peut pas être utilisée comme preuve d'usage de la source** (les 3 autres publications de la fiche n'ont pas été vérifiées dans le texte) | CONFIRMÉ (faisceau, borné : le critère de rattachement de la fiche CASD n'est pas publié) | FCT-001 à 004 + fiche source DMTG (dossier 09-15) |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-10_10-54_notes-france-strategie-dmtg | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-10_10-54_notes-france-strategie-dmtg | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-10_10-54_notes-france-strategie-dmtg | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-10_10-54_notes-france-strategie-dmtg | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-10_10-54_notes-france-strategie-dmtg | - | -
<!-- /FACT_REGISTRY_V1 -->

## VERDICT

Le GAP 3 est résolu : **les deux notes France Stratégie listées dans la fiche source DMTG n'utilisent pas l'enquête DMTG**. Leurs sources réelles, vérifiées dans le texte :
- Note 120 (inégalité des chances) : **enquête FQP 2014-2015** (Insee)
- Note 121 (fin de carrière des seniors) : **enquêtes Emploi 2004-2019** (Insee) + **enquêtes Conditions de travail 2013/2016/2019** (Dares-Drees-DGAFP)

Ce constat a une conséquence méthodologique importante : **la fiche source CASD mêle publications utilisant réellement la source et publications rattachées thématiquement** — elle ne peut pas servir d'inventaire fiable des usages de la DMTG. Combiné au 10-48 (les travaux IPP/CREST n'utilisent DMTG que dans l'AER 2023) et au 10-41 (le lien WID.world/TAXOPTI rétrogradé), **la carte des utilisateurs réels de l'échantillon DMTG 2010 se réduit à : EVREFIS/AER 2023 (documenté) et les travaux WID.world historiques (lien rétrogradé)**.

## LEÇON

La fiche source CASD, outil de référence du dispositif d'accès, n'atteste pas l'usage d'une source par une publication : elle agrège des rattachements dont le critère n'est pas publié. Deux enseignements : (1) pour toute revendication d'usage de données, vérifier la méthodologie du document (coeur du protocole KERNEL — déjà appliqué au 10-48) ; (2) l'inventaire des publications utilisant DMTG publié par le dispositif lui-même est **non fiable**, ce qui renforce le constat de traçabilité confinée déjà établi (dossiers 10-41 et 09-19). Aucune imputation de volition : le flou du rattachement est un défaut documentaire du CASD, pas une démonstration d'intention.

## GATE_CHECK

| Gate | État |
|------|------|
| G1 — Faits sourcés lus en session | ✅ 2 PDF lus intégralement (notes 120 et 121) |
| G2 — Aucune fabrication | ✅ tous les greps effectués sur les textes extraits |
| G3 — Faisceaux bornés | ✅ FCT-005 borné (critère de rattachement CASD non publié) |
| G4 — Anti-sycophancie | ✅ constat défavorable au dispositif (fiche CASD non fiable) étayé par les textes |
| G5 — Constats d'absence | ✅ FCT-001, FCT-003 |
| GAPS | (1) identifier le critère exact de rattachement des publications à la fiche source DMTG (demande au CASD — non publié) ; (2) **RÉSOLU au 11-13 (dossier 2026-08-10_11-13_verif-3-publications-fiche-dmtg)** : les 3 publications restantes vérifiées — BdF WP 636 = seul usage avéré (échantillons de succession 1984-2010 dont 2010, l. 1092-1097), WID WP 2017/4 = 0 mention (papier DINA revenus), AER 2023 = résumé seul sans mention (texte intégral non lu) ; (3) croiser avec les projets CSS 09-31 (DEPUBMO, TAXOPTI, etc.) pour savoir si les notes 120/121 correspondent à un projet CSS de France Stratégie (aucun trouvé — France Stratégie n'apparaît pas dans les 8 projets DMTG) |

## LIMITES

- Le **critère de rattachement** des publications aux fiches sources du CASD n'est pas publié : FCT-005 est un faisceau (les textes des notes ne citent pas DMTG), pas une preuve du critère interne du CASD.
- Les PDF ont été extraits en `pdftotext -layout` : une mention DMTG dans une annexe ou une bibliographie non textuelle (image/scannée) pourrait échapper au grep — improbabilité faible mais non nulle.
- La note 120 a été trouvée via la Wayback CDX (URL `fs-2023-na-120-inegalite-chances.pdf`) : la version en ligne actuelle pourrait différer, mais le contenu de la version archivée est conforme au titre et au format de la note.
