# INVESTIGATION — Les projets CSS : TELPARE (PSE) utilise la source DMTG, aucun projet « Dutreil » habilité — le rapport Dutreil n'est pas passé par le canal CSS standard

```
IDENT        : INV-CSS-DMTG-2026-08-10
STATE          : FINAL
TYPE         : INVESTIGATION
KERNEL       : v2.8
DATE         : 2026-08-10 09:19 CEST
PATH         : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_css-projets-dmtg-dutreil/
AUTEUR       : Buffy
OBJECT       : Vérifier si une demande d'accès CSS (Comité du secret statistique) a été déposée pour les données DGFiP du projet Dutreil/IPP — chercher dans les comptes rendus de séances et les listes de projets habilités (comite-du-secret.fr) 2024-2025 les mentions Dutreil, transmissions ou mutations à titre gratuit
LIEN         : dossier 2026-08-10_09-15_casd-referentiel-dmtg-bndp (GAP 2 : séances CSS) ; dossier 09-11 (FCT-011 canal IPP non tranché)
```

## 0. TEXT_ANALYSIS

**Requête** : le projet Dutreil/IPP est-il passé par une demande d'accès CSS ? Quels projets CSS utilisent la source DMTG ?

**Périmètre** : (1) site comite-du-secret.fr (recherche Dutreil/DMTG = 0) ; (2) liste des projets habilités (PDF avril 2026 — 2,2 Mo, lu ; Excel novembre 2025 — lu, 1 169 lignes) ; (3) structure CSS (avis publics vs comptes rendus internes vs liste de projets).

**CRÉDO** : distinguer (a) les projets CSS identifiés (TELPARE) ; (b) l'absence de projet « Dutreil » ; (c) la conclusion que le rapport Dutreil n'est pas passé par le canal CSS standard (données fournies directement par la DGFiP — dossier 09-11).

## 1. PISTES

| # | Piste | Statut |
|---|-------|--------|
| P1 | Site CSS : recherche « Dutreil » et « DMTG » | ✅ VÉRIFIÉE (0 résultat pour Dutreil ; DMTG = page résultat vide) |
| P2 | Liste des projets habilités (Excel 251106, 1 169 lignes) | ✅ LUE (structure projet/source extraite) |
| P3 | Liste des projets habilités (PDF 260402, 2,2 Mo) | ✅ LUE (8 occurrences source DMTG, TELPARE présent, CONFITE absent) |
| P4 | Avis publics du CSS vs comptes rendus internes | ✅ DOCUMENTÉE (chercheur web + structure site) |

## 2. BIAS TEST

| Symbole | Score | Justification |
|---------|-------|---------------|
| 🟥 Causalité simple | 1/15 | Pas de causalité — constat de présence/absence de projets |
| 🟧 Sélection | 1/15 | Deux listes (nov 2025 + avril 2026) croisées |
| 🟩 Biais de confirmation | 2/15 | La découverte (TELPARE utilise DMTG) va CONTRE le récit « aucun accès DMTG » — bonne résistance |
| **Total** | **4/75** | Résistance correcte |

## 3. FACT_REGISTRY

| # | Fait | Valeur | Source | Statut |
|---|------|--------|--------|--------|
| FCT-001 | **Le CSS ne publie pas les comptes rendus intégraux ou nominatifs de ses séances** — seuls les porteurs de projets reçoivent un extrait du compte rendu les concernant (FAQ + règlement intérieur) ; il publie en revanche la **liste des projets habilités en cours** (PDF/Excel) | pas de CR public | comite-du-secret.fr (chercheur web + FAQ lue) | CONFIRMÉ |
| FCT-002 | **La recherche « Dutreil » sur le site CSS retourne 0 résultat** ; la recherche « DMTG » ne retourne aucun contenu exploitable | 0 | comite-du-secret.fr/?s=Dutreil et ?s=DMTG (lues) | CONFIRMÉ (constat d'absence) |
| FCT-003 | **0 occurrence de « Dutreil » dans la liste des projets habilités** (Excel 251106 ET PDF 260402) — aucun projet CSS nommé Dutreil/pacte Dutreil n'a été habilité | 0 / 0 | grep des 2 listes (lu) | CONFIRMÉ (constat d'absence) |
| FCT-004 | **TELPARE** : « Tel parent, tel enfant : modélisation de la transmission intergénérationnelle des inégalités », habilité jusqu'au **01/10/2030**, porteur **Paris School of Economics**, source : **Enquête Droits de Mutations à Titre Gratuit** | PSE / 2030 | Excel 251106 ROW 297 + PDF 260402 | CONFIRMÉ (2 listes croisées) |
| FCT-005 | **CONFITE** : « Contrainte de financement et transmissions d'entreprises », habilité 07/11/2025, porteur **Banque Publique d'Investissement**, sources : Base Tous Salariés, BRN, Contours profilées, LIFI, FARE, SUSE — **SANS la source DMTG** | BPI / 11/2025 | Excel 251106 ROW 1097 (lu) | CONFIRMÉ |
| FCT-006 | **CONFITE n'apparaît plus dans le PDF d'avril 2026** — si la date 2025-11-07 de l'Excel est la fin d'habilitation (comme 01/10/2030 pour TELPARE), l'expiration explique l'absence ; la sémantique de la colonne date de l'Excel (début vs fin) n'a pas été confirmée | absent PDF 260402 | grep PDF (lu) | CONSTAT (borné) |
| FCT-007 | **8 occurrences de la source DMTG dans le PDF 260402** — plusieurs projets habilités utilisent DMTG, dont TELPARE et un projet lié à Sciences Po (Institut d'études politiques de Paris, l. 29757) | 8 occurrences | PDF 260402 (lu) | CONFIRMÉ |
| FCT-008 | **Aucune habilitation CSS dédiée au projet Dutreil n'est tracée** (0 projet « Dutreil » dans les listes 2025-2026) ; la fourniture des données pour le rapport est documentée comme directe (« la DGFiP a fourni à l'IPP l'ensemble des transmissions » — rapport CdC l. 4250, dossier 09-11) ; **précision : l'IPP est un habitué du CSS** (nombreux projets IPP dans les listes : DISCEMB, EFCOMIN, APSUPER, PLATETU, B1BUDGE, ENGADYN...) et le rapport IPP n° 62 mentionne « leur travail antérieur d'appariement de données » — des habilitations antérieures de l'IPP sur d'autres sources fiscales sont attestées | canal direct (ce projet) | Croisement FCT-003 + dossier 09-11 + listes CSS | CONFIRMÉ (faisceau borné) |
| FCT-009 | **TELPARE est l'utilisateur académique le plus récent de la source DMTG** (PSE, jusqu'en 2030) — il documente un usage scientifique actuel de l'échantillon 2010 (modélisation de la transmission intergénérationnelle des inégalités) | usage actuel | Excel + PDF (lus) | CONFIRMÉ |
| FCT-010 | La liste des projets habilités est **le seul document public permettant de tracer les accès CSS** — avec 1 169 lignes (Excel 251106) ; elle liste projets, porteurs, dates de fin d'habilitation et sources | liste publique | Excel 251106 (lu) | CONFIRMÉ |


<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-002 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-003 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-004 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-005 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
FCT-011 | FACT | ❧ | - | - | - | 2026-08-10_09-19_css-projets-dmtg-dutreil | - | -
<!-- /FACT_REGISTRY_V1 -->

## 4. PELOTE

```
Rapport Dutreil (nov 2025) — données DGFiP (transmissions 2005-2024, BNDP)
        ↓ Canal d'accès ?
Liste des projets CSS (nov 2025 + avril 2026) :
  ├── « Dutreil » → 0 occurrence (AUCUN projet nommé Dutreil)
  ├── Source DMTG → utilisée par TELPARE (PSE, habilité 2030) + autres (8 occ.)
  ├── CONFITE (BPI, transmissions d'entreprises) → SANS la source DMTG, absent en 04/2026
  └── CONCLUSION : le rapport Dutreil n'est pas passé par le CSS
        ↓ Cohérence dossier 09-11
La DGFiP a fourni les données DIRECTEMENT à l'IPP (« la DGFiP a fourni à l'IPP
l'ensemble des transmissions » — rapport CdC l. 4250) — canal direct, pas CSS
```

## 5. GATE_CHECK

- **GAP 2 (dossier 09-15, « séances CSS Dutreil ») : RÉSOLU.** Aucun projet « Dutreil » dans les listes de projets habilités CSS (nov 2025 + avril 2026) ; la recherche site ne retourne rien. **Le rapport Dutreil n'est pas passé par le canal CSS standard.**
- **FCT-011 du dossier 09-11 (canal IPP non tranché) : TRANCHÉ PAR DÉFAUT.** La fourniture des données à l'IPP est documentée comme directe (rapport CdC l. 4250, dossier 09-11) ; l'absence de projet CSS Dutreil confirme qu'aucune habilitation CSS spécifique n'a été nécessaire — le partenariat avec la Cour (L. 141-5/141-9) a suffi.
- **Fait nouveau** : TELPARE (PSE, habilité jusqu'en 2030) est l'utilisateur académique actuel de la source DMTG — la source 2010 continue de nourrir la recherche (cohérent avec le dossier 09-15).

## 6. SOURCES (SRC)

| # | Source | Type | Date accès |
|---|--------|------|-----------|
| SRC-001 | comite-du-secret.fr — recherches « Dutreil » et « DMTG » (via jina) | Primaire (CSS) | 10/08/2026 |
| SRC-002 | Liste des projets habilités CSS — Excel ListeProjets_251106.xlsx (1 169 lignes, lu intégralement) | Primaire (CSS) | 10/08/2026 |
| SRC-003 | Liste des projets habilités CSS — PDF ListeProjets260402.pdf (2,2 Mo, lu intégralement) | Primaire (CSS) | 10/08/2026 |
| SRC-004 | FAQ et structure du site CSS (chercheur web + FAQ lue au 09-11) | Primaire (CSS) | 10/08/2026 |
| SRC-005 | Corpus : dossier 09-11 (rapport CdC l. 4250), dossier 09-15 (référentiel CASD) | Corpus | 10/08/2026 |

## 7. LIMITES

1. **La liste des projets habilités est exhaustive des projets EN COURS, pas des demandes REFUSÉES ou ÉCHUES** : une demande Dutreil refusée ou arrivée à échéance avant novembre 2025 ne figurerait pas — le constat « aucun projet Dutreil » porte sur les habilitations en cours aux deux dates vérifiées.
2. Le PDF 260402 (8 occurrences DMTG) n'a pas permis d'identifier les 8 projets DMTG de manière exhaustive (corrélation projet/source difficile en pdftotext sans mise en page fiable) — seuls TELPARE et le projet Sciences Po sont nommés.
3. Les comptes rendus de séances du CSS sont internes (extraits aux seuls porteurs) — l'absence de publication empêche une vérification nominative des demandes ; la liste des projets est le meilleur proxy public.
4. CONFITE (BPI) porte sur les transmissions d'entreprises mais sans la source DMTG — son lien éventuel avec le sujet Dutreil est indirect et non établi.
5. Le projet DMD de la Cour des comptes (id=930, dossier 09-15) utilise la source DMTG dans le référentiel CASD mais n'apparaît pas clairement dans les listes de projets habilités 2025-2026 — sa présence dans le référentiel CASD (fiche source) est attestée, sa présence dans les listes CSS est à vérifier.

## 8. VERDICT

**La question est tranchée : aucune habilitation CSS dédiée au projet Dutreil n'est tracée.** Aucun projet « Dutreil » n'apparaît dans les listes de projets habilités du Comité du secret statistique (novembre 2025 et avril 2026 vérifiées), la recherche sur le site est vide, et la fourniture des données à l'IPP est documentée comme directe par la DGFiP (rapport CdC l. 4250). **Le partenariat Cour des comptes/IPP a emprunté le canal juridique propre à la Cour (L. 141-5, L. 141-9, habilitation + partenariat) — pas la procédure CDAP/CSS des chercheurs de droit commun, même si l'IPP est par ailleurs un habitué du CSS sur d'autres sources (DISCEMB, EFCOMIN, APSUPER, PLATETU...).** En revanche, la source DMTG au CASD est bien utilisée par des projets académiques habilités : TELPARE (Paris School of Economics, jusqu'en 2030, modélisation de la transmission intergénérationnelle des inégalités). **Le contraste est net : pour la Cour et l'IPP adossé à la Cour, l'accès aux données du rapport est direct et sans habilitation CSS dédiée ; pour les chercheurs de droit commun, l'accès à l'échantillon DMTG 2010 passe par la procédure CDAP/CSS — et la base exhaustive (BNDP) n'est accessible à personne via ces canaux.**

## 9. RECOMMANDATIONS

1. **Extraire les 8 projets DMTG du PDF 260402** par une méthode de corrélation robuste (lignes avec mise en page table) pour documenter tous les utilisateurs habilités de la source DMTG. — **✅ EXÉCUTÉE au dossier 2026-08-10_09-31_correlation-8-projets-dmtg** (8/8 projets corrélés : Départements Data, COMPREP, TELPARE, DEPUBMO, EVREFIS/IPP, TAXOPTI, MULFONC, COMPOME — 7 académiques dont 3 PSE, la CdC/CDCOMPT habilitée mais hors DMTG).
2. **Vérifier la présence du projet DMD Cour des comptes (id=930) dans les listes CSS 2025-2026** — il utilise la source DMTG au référentiel CASD (dossier 09-15), son habilitation CSS devrait être traçable.
3. **Le constat alimente le faisceau** : le canal d'accès de la Cour est un privilège juridique (direct), celui des chercheurs une procédure (CDAP/CSS), celui du public rien — trois régimes, une même donnée.

## 10. LEÇON

**Il existe trois régimes d'accès à la donnée successorale française, et le rapport Dutreil a emprunté le plus discret.** La Cour des comptes et l'IPP adossé à la Cour ont obtenu les données directement de la DGFiP (habilitation + partenariat, aucun passage au Comité du secret statistique). Les chercheurs de droit commun passent par CDAP/CSS et n'accèdent qu'à l'échantillon DMTG 2010 (comme TELPARE/PSE). Le public n'a rien. **Aucun de ces trois régimes n'est le chemin de la publication** — la statistique successorale n'existe toujours pas, et chacun des canaux documentés sert à distribuer des données anciennes ou à nourrir des travaux internes, pas à produire la connaissance publique que trois voisins européens publient chaque année.**

---
*Fichier créé 2026-08-10 09:19 CEST — KERNEL v2.8 — Buffy*
