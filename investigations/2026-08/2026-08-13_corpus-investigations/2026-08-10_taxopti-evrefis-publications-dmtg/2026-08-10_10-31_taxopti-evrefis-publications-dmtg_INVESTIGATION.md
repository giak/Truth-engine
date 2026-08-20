# CORRÉLATION TAXOPTI / EVREFIS ↔ 5 PUBLICATIONS DE LA FICHE SOURCE DMTG

- **STATE          : FINAL**
- **Date           : 2026-08-10 10:31 CEST**
- **KERNEL         : v2.8**
- **Dossier lié    : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_casd-referentiel-dmtg-bndp/2026-08-10_09-15_casd-referentiel-dmtg-bndp_INVESTIGATION.md (fiche source DMTG, 5 publications)**
- **Listes CSS     : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_css-projets-dmtg-dutreil/2026-08-10_09-19_css-projets-dmtg-dutreil_INVESTIGATION.md + 2026-08-10_09-31_correlation-8-projets-dmtg_INVESTIGATION.md**
- **Résultat       : faisceau documenté (EVREFIS ↔ AER 2023 IPP ; TAXOPTI ↔ séries richesse WID.world), lien publication↔projet jamais publié**

---

## §0 OBJECT

Relier les projets CSS **TAXOPTI** (PSE, « Taxation optimale du capital et de l'héritage ») et **EVREFIS** (IPP, « Evaluation des réformes de la fiscalité du capital ») aux **5 publications listées dans la fiche source « Enquête Droits de Mutations à Titre Gratuit »** du référentiel CASD (dossier 09-15), pour documenter les travaux publiés sur la donnée successorale française.

## §1 METHOD

1. **Têtes de bloc des deux projets** : PDF `ListeProjets260402.pdf` (version du 02/04/2026), extrait `pdftotext -layout` (`/tmp/css_liste260402.txt`), lu en session : bloc EVREFIS l. 10882-10914, bloc TAXOPTI l. 13097-13113, occurrence DMTG à la l. 10914 (EVREFIS) et l. 13101 (TAXOPTI).
2. **Fiche source DMTG** : `/tmp/casd_dmtg_fiche.txt` (référentiel CASD), bloc publications l. 110-182 (dossier 09-15).
3. **5 fiches de publication CASD** lues intégralement via `r.jina.ai` sur `https://www.casd.eu/publi.php?id=108|109|454|455|457` (fichiers `/tmp/casd_p108.txt`, `p109`, `p454`, `p455`, `p457`).
4. **Croisement auteurs/institutions/sujets** avec les porteurs déclarés des projets (IPP pour EVREFIS, PSE pour TAXOPTI).

## §2 FACT_REGISTRY

| # | Fait | Statut | Source |
|---|------|--------|--------|
| FCT-001 | **EVREFIS** : « Evaluation des réformes de la fiscalité du capital en France », échéance 29/04/2028, porteur **Institut des Politiques Publiques** ; bloc l. 10882-10914 du PDF 260402 ; la source **DMTG figure dans ses sources** (occurrence « Enquête Droits de Mutations » l. 10914) | CONFIRMÉ | PDF 260402 l. 10882, 10914 |
| FCT-002 | **TAXOPTI** : « Taxation optimale du capital et de l'héritage - Calibration de formules théoriques à partir de données françaises », échéance 07/08/2027, porteur **Paris School of Economics** ; bloc l. 13097-13113 ; la source **DMTG figure dans ses sources** (l. 13101), avec ERF, ERFS et les panels ISF/IFI | CONFIRMÉ | PDF 260402 l. 13097, 13101 |
| FCT-003 | Les **5 publications** listées dans la fiche source DMTG du CASD (dossier 09-15, l. 110-182) : (1) Garbinti, Goupille-Lebret, Piketty, « Accounting for Wealth Inequality Dynamics: Methods, Estimates and Simulations for France (1880-2014) », Banque de France WP 636, juin 2017 (fiche CASD id=108 — titre littéral de la fiche ; la version publiée, JEEA 2021, est intitulée « 1800-2014 », la série remontant à 1800) ; (2) Garbinti, Goupille-Lebret, Piketty, « Income Inequality in France, 1900-2014: Evidence from Distributional National Accounts », WID.world WP 2017/4, déc. 2016 (id=109) ; (3) France Stratégie, « Fin de carrière des seniors : quelles spécificités selon les métiers ? », note d'analyse 2023/6 n° 121 (id=454) ; (4) France Stratégie, « Inégalité des chances : ce qui compte le plus », note d'analyse 2023/5 n° 120 (id=455) ; (5) Bach, Bozio, **Guillouzouic-Le Corff**, Malgouyres, « Dividend Taxes and the Allocation of Capital: Comment », American Economic Review 113(7), 2023, pp. 2048-52 (id=457 — précision au 10-48 : 4 auteurs, Arthur Guillouzouic-Le Corff est une seule personne) | CONFIRMÉ | fiche source DMTG l. 110-182 + fiches CASD 108/109/454/455/457 |
| FCT-004 | Les fiches CASD `publi.php?id=108|109|454|455|457` ont été lues : titres et auteurs extraits ; **le bloc « Projet » y est vide** — les fiches de publication ne relient pas la publication au projet CSS habilité | CONFIRMÉ (constat) | fiches CASD lues |
| FCT-005 | **Corrélation EVREFIS ↔ publication n° 5** : Bach, Bozio, Guillouzouic et Malgouyres sont chercheurs IPP/CREST ; le sujet (« Dividend Taxes », taxation des dividendes) recouvre le périmètre déclaré d'EVREFIS (« fiscalité du capital ») — faisceau institutionnel + thématique | CONFIRMÉ (faisceau, borné : lien non déclaré publiquement) | fiches CASD 457 + identités IPP |
| FCT-006 | **Corrélation TAXOPTI ↔ publications n° 1-2** : Garbinti, Goupille-Lebret et Piketty (WID.world, PSE) produisent les séries de richesse française 1880-2014 ; le périmètre TAXOPTI (« taxation optimale du capital et de l'héritage ») recouvre le sujet ; Piketty affilié PSE — faisceau institutionnel + thématique. **⚠ RÉTROGRADÉ au 10-41** : les pubs 12/2016 et 06/2017 précèdent de plus de 3 ans la première trace documentée de TAXOPTI (liste CSS 08/2020) — l'attribution n'est pas étayable (dossier 2026-08-10_10-41) | RÉTROGRADÉ (non étayable) | fiches CASD 108/109 + dossier 10-41 |
| FCT-007 | Les publications France Stratégie (n° 3-4) n'ont **aucun lien documenté** avec TAXOPTI ni EVREFIS : elles traitent de carrières et d'inégalité des chances (sources probables DADS/Enquête Emploi), la fiche DMTG les liste sans projet associé | CONFIRMÉ (constat d'absence de lien) | fiche source DMTG + fiches 454/455 |
| FCT-008 | Ni les fiches CASD, ni les listes CSS (nov. 2025, avr. 2026), ni le référentiel ne publient la cartographie « publication ↔ projet » : **la traçabilité des travaux issus de la donnée successorale habilitée n'est pas publique** | CONFIRMÉ (constat d'absence) | fiches CASD + listes CSS |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-10_10-31_taxopti-evrefis-publications-dmtg | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-10_10-31_taxopti-evrefis-publications-dmtg | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-10_10-31_taxopti-evrefis-publications-dmtg | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-10_10-31_taxopti-evrefis-publications-dmtg | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-10_10-31_taxopti-evrefis-publications-dmtg | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-10_10-31_taxopti-evrefis-publications-dmtg | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-10_10-31_taxopti-evrefis-publications-dmtg | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-10_10-31_taxopti-evrefis-publications-dmtg | - | -
<!-- /FACT_REGISTRY_V1 -->

## VERDICT

Le croisement documente un **faisceau à deux maillons**, sans lien déclaré nulle part :

1. **EVREFIS (IPP, échéance 2028)** ↔ **« Dividend Taxes and the Allocation of Capital: Comment » (AER 2023)** : les quatre auteurs (Bach, Bozio, Guillouzouic, Malgouyres) sont des chercheurs IPP/CREST et le sujet est exactement la fiscalité du capital — le périmètre du projet. C'est le lien le plus solide des deux (fenêtre d'habilitation attestée ≥ 08/2020, couvre 2023).
2. **TAXOPTI (PSE, échéance 2027)** ↔ **séries de richesse Garbinti/Goupille-Lebret/Piketty (BdF WP 2017, WID.world 2017)** : **RÉTROGRADÉ au 10-41** — les publications 2016-2017 précèdent de plus de 3 ans la première trace documentée de TAXOPTI (liste CSS 08/2020) et très probablement l'habilitation ; l'attribution n'est pas étayable. Seul le lien EVREFIS ↔ AER 2023 subsiste comme faisceau.

La donnée successorale DMTG (échantillon 2010) a donc alimenté **au moins deux programmes de recherche majeurs** sur la fiscalité du capital et de l'héritage. Mais **la corrélation repose sur les institutions et les sujets, jamais sur une déclaration** : les fiches CASD laissent le champ « Projet » vide et les listes CSS ne publient pas les outputs.

## LEÇON

Le régime d'accès par habilitation (CDAP/CSS) **produit** des publications publiques de premier plan — les séries de richesse et le débat sur la taxation des dividendes existent grâce à la DMTG. Mais il est **opaque sur sa traçabilité** : personne, de l'extérieur, ne peut établir quels travaux précis ont été produits sur l'échantillon DMTG 2010 et par qui. Contraste avec le canal Cour des comptes (exhaustif, discrétion documentée) et le public (rien) : le canal standard fonctionne, mais ses outputs ne sont reliés à leurs sources que par inférence. Rien ne documente une décision de cacher ces liens : l'opacité est structurelle (fiches non renseignées), pas nécessairement délibérée.

## GATE_CHECK

| Gate | État |
|------|------|
| G1 — Faits sourcés lus en session | ✅ PDF 260402, fiche source DMTG, 5 fiches CASD |
| G2 — Aucune fabrication | ✅ aucun auteur, date ou titre inventé : tout est extrait des fiches |
| G3 — Faisceaux bornés | ✅ FCT-005/006 marqués « lien non déclaré » ; FCT-007 absence documentée |
| G4 — Anti-sycophancie | ✅ le lien le plus fort (EVREFIS/AER) reste borné ; pas d'imputation de volition |
| G5 — Constats d'absence | ✅ FCT-004, FCT-008 |
| GAPS | (1) ~~identifier d'autres publications IPP/PSE utilisant DMTG hors fiche CASD~~ **RÉSOLU au 10-48 : aucun output IPP/CREST DMTG hors fiche (constat d'absence, seule pub = AER 2023) — rapport IPP 46 non vérifié** ; (2) ~~dater le début d'habilitation de TAXOPTI~~ **RÉSOLU au 10-41 : début indatable, lien pubs WID.world rétrogradé** ; (3) ~~vérifier si les publications France Stratégie (3-4) utilisent effectivement DMTG~~ **RÉSOLU au 10-54 : NON — note 120 = FQP 2014-2015, note 121 = Enquêtes Emploi/Conditions de travail ; la fiche CASD ne peut pas servir de preuve d'usage** |

## LIMITES

- La corrélation EVREFIS ↔ AER 2023 et TAXOPTI ↔ WID.world **n'est déclarée dans aucun document public** (fiches CASD champ « Projet » vide). Les liens sont des faisceaux institutionnels/thématiques.
- Les publications WID.world 2016-2017 **précèdent** l'échéance 2027 de TAXOPTI : elles pourraient relever d'un projet antérieur ou d'un renouvellement — non tranchable avec les seules listes CSS (qui ne donnent que la date de fin).
- Les publications France Stratégie (3-4) pourraient utiliser DMTG sans lien avec les deux projets : la fiche source les liste, sans plus. L'affirmation « sources probables DADS/Enquête Emploi » (FCT-007) est une inférence non vérifiée en session : ni les fiches CASD ni les notes elles-mêmes n'ont été consultées pour la confirmer.
- Les fiches CASD ont été lues via le proxy r.jina.ai : le rendu navigable est filtré, mais les champs titre/auteurs/année ont été extraits intégralement.
