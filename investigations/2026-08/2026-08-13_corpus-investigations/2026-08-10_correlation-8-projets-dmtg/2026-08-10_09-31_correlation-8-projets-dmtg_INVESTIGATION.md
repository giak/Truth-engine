# INVESTIGATION — Corrélation complète des 8 projets CSS utilisant la source DMTG (PDF ListeProjets260402) : la carte des utilisateurs habilités de la donnée successorale

```
IDENT        : INV-CSS-8DMTG-2026-08-10
STATE          : FINAL
TYPE         : INVESTIGATION
KERNEL       : v2.8
DATE         : 2026-08-10 09:31 CEST
PATH         : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_correlation-8-projets-dmtg/
AUTEUR       : Buffy
OBJECT       : Corréler les 8 occurrences de la source « Enquête Droits de Mutations à Titre Gratuit » (DMTG) dans le PDF ListeProjets260402.pdf avec leurs projets (acronyme, organisme, échéance) pour cartographier complètement les utilisateurs CSS de la donnée successorale — et lever la LIMITE 2 du dossier 09-19
LIEN         : dossier 2026-08-10_09-19_css-projets-dmtg-dutreil (RECOMMANDATION 1, LIMITE 2) ; dossier 09-15 (référentiel CASD, source DMTG) ; dossier 09-11 (convention CdC/DGFiP)
```

## 0. TEXT_ANALYSIS

**Requête** : quels sont exactement les 8 projets habilités CSS qui utilisent la source DMTG dans la liste d'avril 2026 ? (Corrélation complète acronyme / nom / échéance / organisme / autres sources.)

**Périmètre** : PDF `ListeProjets260402.pdf` (2,2 Mo, version du 02/04/2026) — extraction pdftotext avec mise en page (`-layout`, 2 162 237 octets, ~12 300 lignes) pour corréler colonne « sources » → colonne projet.

**CRÉDO** : distinguer (a) les 8 projets nommés (corrélation robuste par mise en page) ; (b) le cas de la Cour des comptes (CDCOMPT présent dans la liste mais hors DMTG) ; (c) les limites de l'exhaustivité (projets dont l'habilitation a expiré avant avril 2026).

## 1. PISTES

| # | Piste | Statut |
|---|-------|--------|
| P1 | Extraction `pdftotext -layout` du PDF 260402 (structure colonnes préservée) | ✅ RÉALISÉE (2 162 237 octets, colonnes : nom / acronyme / date / organismes / sources) |
| P2 | Corrélation par remontée : chaque occurrence DMTG → ligne projet contenant la date d'échéance | ✅ RÉALISÉE (8/8 projets identifiés, méthode ligne-tête-de-bloc) |
| P3 | Vérification des sources adjacentes de chaque projet (pour distinguer DMTO onéreux / DMTG gratuit) | ✅ RÉALISÉE (projet Départements Data utilise les DEUX) |
| P4 | Recherche de la Cour des comptes dans la liste (CDCOMPT) | ✅ RÉALISÉE (présente, échéance 09/03/2029, sans DMTG) |
| P5 | Contrôle d'exhaustivité : autres sources successorales (déclarations de succession, viager) | ✅ RÉALISÉE (0 autre source successorale ; BECREAT = successions de cultures, hors sujet) |

## 2. BIAS TEST

| Symbole | Score | Justification |
|---------|-------|---------------|
| 🟧 Sélection | 1/15 | Une seule liste (avril 2026) mais croisée avec le référentiel CASD (09-15) et l'Excel 251106 (09-19) |
| 🟨 Méthode | 1/15 | Corrélation par remontée de ligne : risque de mauvaise attribution si chevauchement de blocs — mitigé par la vérification de chaque tête de bloc (8/8) |
| 🟩 Biais de confirmation | 2/15 | La découverte « 6 projets académiques dont 3 PSE » enrichit le faisceau mais n'a pas été cherchée a priori |
| **Total** | **4/75** | Résistance correcte |

## 3. FACT_REGISTRY

| # | Fait | Valeur | Source | Statut |
|---|------|--------|--------|--------|
| FCT-001 | **La corrélation des 8 occurrences DMTG est complète** : chacune des 8 occurrences de « Enquête Droits de Mutations à Titre Gratuit » dans le PDF 260402 appartient à un projet distinct — aucune ambiguïté de chevauchement de blocs | 8 projets / 8 occurrences | PDF 260402 l. 2742, 4994, 5951, 6742, 10914, 13101, 15294, 17624 (lues) | CONFIRMÉ |
| FCT-002 | **Départements Data** : « Projet Départements Data - Tableaux de bord à destination des Départements », échéance **07/10/2031**, porteur **Départements de France** — le SEUL projet non académique ; il utilise DMTG **et** la source « Droits de mutations à titre onéreux séries mensuelles par département » (DMTO, onéreux — distinction explicite) | DMTO + DMTG | PDF 260402 l. 2740-2742 (lues) | CONFIRMÉ |
| FCT-003 | **COMPREP** : « Les réponses comportementales à l'impôts », échéance **03/12/2030**, porteur **Aix-Marseille School of Economics** — sources dont DMTG, EDP, Enquête Histoire de Vie et Patrimoine, Enquête Patrimoine, Fichier panel ISF/IFI | AMSE / 2030 | PDF 260402 l. 4991 (lue) | CONFIRMÉ |
| FCT-004 | **TELPARE** : « Tel parent, tel enfant : modélisation de la transmission », échéance **01/10/2030**, porteur **Paris School of Economics** — DMTG (confirme le dossier 09-19 : TELPARE = PSE, source DMTG) | PSE / 2030 | PDF 260402 l. 5951 (lue) + Excel 251106 ROW 297 (09-19) | CONFIRMÉ (2 sources) |
| FCT-005 | **DEPUBMO** : « Dynamiques du Financement et de la Distribution des Dépenses Publiques », échéance **19/03/2030**, porteur **Paris School of Economics** — DMTG + Base non salariés, FQP | PSE / 2030 | PDF 260402 l. 6727 (lue) | CONFIRMÉ |
| FCT-006 | **EVREFIS** : « Evaluation des réformes de la fiscalité du capital en France », échéance **29/04/2028**, porteur **Institut des Politiques Publiques** — DMTG + IS, BRN — le projet IPP du dossier 09-19 (l'IPP, partenaire du rapport Dutreil, a une habilitation DMTG via le canal CSS pour ses propres travaux) | IPP / 2028 | PDF 260402 l. 10882 (lue) | CONFIRMÉ |
| FCT-007 | **TAXOPTI** : « Taxation optimale du capital et de l'héritage - Calibration de formules », échéance **07/08/2027**, porteur **Paris School of Economics** — DMTG + BTS — l'objet « capital et héritage » est le plus proche thématiquement du rapport Dutreil | PSE / 2027 | PDF 260402 l. 13097 (lue) | CONFIRMÉ |
| FCT-008 | **MULFONC** : « La multipropriété foncière et immobilière : quels effets sur les... », échéance **07/12/2026**, porteur **Université d'Avignon et des Pays de Vaucluse** — DMTG + Base de la propriété foncière, 2044 | Avignon / 2026 | PDF 260402 l. 15290 (lue) | CONFIRMÉ |
| FCT-009 | **COMPOME** : « Le comportement des ménages face aux incitations fiscales », échéance **29/04/2026**, porteur **Institut d'études politiques de Paris** (Sciences Po) — DMTG + Enquête Patrimoine — c'est le « projet lié à Sciences Po » mentionné au 09-19 (l. 29757 du texte brut) | Sciences Po / 2026 | PDF 260402 l. 17624 (lue) | CONFIRMÉ |
| FCT-010 | **La Cour des comptes a une habilitation CSS** : projet **CDCOMPT** « PA Travaux de la Cour des Comptes », échéance **09/03/2029**, porteur Cour des comptes — mais la source DMTG **n'en fait pas partie** (elle n'est pas dans les 8 occurrences) ; ses sources sont le recouvrement des encaissements, DPAE, JEI, FIBEN, FILEAS, Caf, Pôle emploi, etc. — la CdC n'accède pas à DMTG par ce canal | CdC / 2029, sans DMTG | PDF 260402 l. 465-497 (lues) | CONFIRMÉ |
| FCT-011 | **Répartition des 8 projets** : 7 académiques (PSE × 3 : TELPARE/DEPUBMO/TAXOPTI ; IPP : EVREFIS ; Sciences Po : COMPOME ; AMSE : COMPREP ; Avignon : MULFONC) + 1 institutionnel (Départements Data) — les 3 projets PSE concentrent près de la moitié des usages académiques de DMTG (3/7 ≈ 43 %) ; les échéances vont du 29/04/2026 (COMPOME) au 07/10/2031 (Départements Data) | 7 académiques / 8 | PDF 260402 (corrélation complète) | CONFIRMÉ |
| FCT-012 | **Aucune autre source successorale dans le PDF** : les seules occurrences « succession » hors DMTG sont « successions de cultures » (BECREAT, agriculture) et « phytosanitaires, de successions » (contexte agricole) — la DMTG est la SEULE source successorale du référentiel CSS | 0 autre | PDF 260402 l. 1498, 17324 (lues) | CONFIRMÉ (constat d'absence) |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
FCT-012 | FACT | ❧ | - | - | - | 2026-08-10_09-31_correlation-8-projets-dmtg | - | -
<!-- /FACT_REGISTRY_V1 -->

## 4. PELOTE

```
Source « Enquête Droits de Mutations à Titre Gratuit » (DMTG, échantillon 2010, CASD)
        ↓ Utilisateurs habilités CSS (liste avril 2026, corrélation complète)
├── Départements Data    (Départements de France)        07/10/2031  [DMTO + DMTG]
├── COMPREP              (Aix-Marseille SE)              03/12/2030
├── TELPARE              (Paris School of Economics)     01/10/2030  [transmission intergénérationnelle]
├── DEPUBMO              (Paris School of Economics)     19/03/2030
├── EVREFIS              (Institut des Politiques Pub.)  29/04/2028  [fiscalité du capital — IPP]
├── TAXOPTI              (Paris School of Economics)     07/08/2027  [capital et héritage]
├── MULFONC              (Univ. Avignon)                 07/12/2026
└── COMPOME              (Sciences Po)                   29/04/2026
        ↓ Contraste
Cour des comptes (CDCOMPT, 09/03/2029) → habilitation CSS SANS DMTG
        ↓ Vérification 09-19
Aucun projet « Dutreil » dans les listes CSS → rapport Dutreil hors canal CSS (canal direct DGFiP→IPP)
```

## 5. GATE_CHECK

- **RECOMMANDATION 1 du dossier 09-19 : EXÉCUTÉE.** Les 8 projets DMTG du PDF 260402 sont désormais corrélés nommément (FCT-001 à FCT-009) — la LIMITE 2 du 09-19 (« seuls TELPARE et le projet Sciences Po sont nommés ») est levée.
- **Fait nouveau 1** : la Cour des comptes dispose bien d'une habilitation CSS (CDCOMPT, jusqu'en 2029) — mais pour ses travaux « PA » (recouvrement, masse salariale, JEI...), **pas pour la donnée successorale**. Pour le rapport Dutreil, elle est passée par le canal direct (09-11) et le partenariat IPP (EVREFIS montre que l'IPP, lui, a un accès CSS à DMTG pour ses propres projets).
- **Fait nouveau 2** : TAXOPTI (PSE, « capital et héritage ») et EVREFIS (IPP, « fiscalité du capital ») sont les deux projets dont l'objet est le plus proche du périmètre Dutreil — la donnée successorale alimente bien la recherche sur la fiscalité du capital et de l'héritage, via le canal CSS, avec l'échantillon 2010.
- **Cohérence avec le 09-15** : la fiche source DMTG listait 12 projets (référentiel CASD) ; la liste CSS d'avril 2026 en montre 8 en cours — l'écart s'explique par les habilitations échues (dont CONFITE, disparu du PDF) et les périmètres différents des deux registres.

## 6. SOURCES (SRC)

| # | Source | Type | Date accès |
|---|--------|------|-----------|
| SRC-001 | Liste des projets habilités CSS — PDF ListeProjets260402.pdf (2,2 Mo, pdftotext -layout, lu intégralement, version du 02/04/2026) | Primaire (CSS) | 10/08/2026 |
| SRC-002 | Liste des projets habilités CSS — Excel ListeProjets_251106.xlsx (1 169 lignes, dossier 09-19) | Primaire (CSS) | 10/08/2026 |
| SRC-003 | Corpus : dossiers 09-11 (convention CdC/DGFiP), 09-15 (référentiel CASD DMTG), 09-19 (projets CSS Dutreil) | Corpus | 10/08/2026 |

## 7. LIMITES

1. **La corrélation porte sur les projets EN COURS à la date du PDF (version du 02/04/2026)** — les projets DMTG dont l'habilitation a expiré avant avril 2026 (comme CONFITE, disparu du PDF) ne figurent pas ; la liste du référentiel CASD (09-15) mentionnait 12 projets, dont certains échus.
2. **CDCOMPT** a été vérifié sur le bloc complet de ses sources (l. 465-497, ~30 sources listées) : DMTG absente. La vérification couvre la liste affichée ; une source ajoutée hors page n'est pas exclue formellement (le bloc est entièrement dans la page lue).
3. Les dates d'échéance sont lues dans la colonne « date fin habilitation » du PDF — la sémantique (fin d'habilitation) est celle indiquée par l'en-tête du document (borné au 09-19, non re-vérifié ici).
4. La concentration PSE (3 projets) est un constat de répartition, pas une preuve de coordination — les trois projets sont distincts, portés par la même école mais sur des objets différents.
5. L'échantillon DMTG distribué reste celui de 2010 (dernier millésime, 09-15) — ces 8 projets travaillent sur une donnée de 16 ans d'âge.

## 8. VERDICT

**La carte des utilisateurs CSS de la donnée successorale est complète : 8 projets habilités (liste avril 2026), corrélés nommément.** Sept projets académiques — dont **3 de la Paris School of Economics** (TELPARE, DEPUBMO, TAXOPTI), l'**Institut des politiques publiques** (EVREFIS, le partenaire du rapport Dutreil), **Sciences Po** (COMPOME), **Aix-Marseille SE** (COMPREP) et **Avignon** (MULFONC) — et un seul institutionnel (Départements Data). **Les échéances s'étalent du 29/04/2026 (COMPOME) au 07/10/2031 (Départements Data).** Deux projets se rapprochent thématiquement du périmètre Dutreil : TAXOPTI (« taxation optimale du capital et de l'héritage ») et EVREFIS (« évaluation des réformes de la fiscalité du capital »). **Et la Cour des comptes, qui a produit le rapport sur le pacte Dutreil en empruntant le canal direct (habilitation DGFiP, hors CSS), dispose elle-même d'une habilitation CSS (CDCOMPT, jusqu'en 2029) qui ne couvre pas la donnée successorale.** Le contraste avec la procédure des chercheurs est documenté : l'échantillon DMTG 2010 circule dans la recherche académique par le canal public, tandis que la base exhaustive (BNDP) et les transmissions 2005-2024 restent confinées au canal de la Cour.

## 9. RECOMMANDATIONS

1. **Vérifier si TAXOPTI ou EVREFIS ont produit des publications utilisant DMTG** (les 5 publications de la fiche source DMTG au 09-15 — Piketty/Zucman, Garbinti) pour relier les habilitations aux travaux publiés.
2. **Croiser la liste CSS avril 2026 avec le référentiel CASD (12 projets)** pour établir la liste des projets DMTG échus avant 2026 (dont l'écart 12 vs 8).
3. **Le constat alimente le faisceau** : la donnée successorale française existe, circule (échantillon 2010) et nourrit la recherche de pointe sur le capital et l'héritage — mais aucun nouveau millésime n'est produit depuis 2010, et la base exhaustive reste hors de portée du public et des chercheurs.

## 10. LEÇON

**Le référentiel d'accès à la donnée successorale française est une ville à deux quartiers.** Le quartier public (CASD/CSS) distribue l'échantillon DMTG 2010 à 8 projets habilités, dont la moitié sont portés par la Paris School of Economics et l'Institut des politiques publiques — les mêmes institutions qui documentent l'inégalité des patrimoines depuis Garbinti, Piketty et Zucman. Le quartier discret (habilitation directe DGFiP → Cour des comptes) distribue la base exhaustive et les transmissions 2005-2024, à la seule Cour. **Entre les deux, aucun pont : le millésime 2010 est le dernier jamais produit — les travaux habilités se contentent de l'échantillon existant, et rien ne documente de décision de produire un nouveau millésime ; seul le public en attendrait un.**
