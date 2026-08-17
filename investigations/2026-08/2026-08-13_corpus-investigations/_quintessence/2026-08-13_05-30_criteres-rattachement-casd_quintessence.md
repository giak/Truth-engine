# Quintessence : Le critère de rattachement CASD : la publication hérite des sources de son projet, pas de son usage réel (GAP 1 résolu)

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_criteres-rattachement-casd/2026-08-10_11-20_criteres-rattachement-casd_INVESTIGATION.md` (9 FCT-001..009)
Date extraction : 2026-08-13 05:30 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot bloc DMTG/BNDP/CDC)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format léger, axe anticorruption, bloc connaissance patrimoniale (DMTG/CASD)
- **Date source** : 2026-08-10 11:20 CEST, STATE FINAL
- **Identifiants source** : 9 FCT-001..009
- **Object** : identifier le mécanisme réel par lequel une publication se retrouve listée sur une fiche source du CASD
- **Verdict source** : le rattachement publication→source est INDIRECT : publication → projet → toutes les sources du projet ; un registre d'accès potentiel, pas un registre d'usage vérifié

## 2. Faits atomiques préservés

- FCT-001 : le rattachement publication→source est INDIRECT : une publication est rattachée à un projet (formulaire de remontée, champ « Code projet CASD »), et la fiche de la publication liste toutes les sources « mises à disposition » de ce projet, pas les sources effectivement utilisées dans le texte [L45 (mesuré)]
- FCT-002 : preuve arithmétique (identité ensembliste) : fiche publi 108 (BdF WP 636) = 19 sources = projet 254 (TAXOPTI) ; fiche publi 457 (AER 2023) = 68 sources = projet 1107 (EVREFIS) ; fiches publi 454/455 (notes FS) = 97 sources chacune = projet 1041 : 3 projets, 3 identités : 19=19, 68=68, 97=97 [L46 (mesuré)]
- FCT-003 : le libellé de l'interface est explicite : « Données mises à disposition via le CASD (N) » : le mot « utilisées » n'apparaît pas : le référentiel documente l'accès potentiel, pas l'usage effectif [L47 (mesuré)]
- FCT-004 : la déclaration est volontaire et auto-déclarée : « Le CASD a besoin de vos publications ! » : objectif affiché « faire la preuve de sa pertinence auprès de ses partenaires et bailleurs de fonds » : indicateur de performance, pas registre d'usage vérifié [L48 (mesuré)]
- FCT-005 : les 5 publications de la fiche DMTG héritent de 3 projets : TAXOPTI (254, 19 sources) → BdF WP 636 + WID WP 2017/4 ; EVREFIS (1107, 68 sources) → AER 2023 ; France Stratégie/CGSP (1041, 97 sources) → notes FS 120/121 [L49 (mesuré)]
- FCT-006 : le projet France Stratégie (1041) a accès à la source DMTG parmi 97 sources : les notes 120/121 sont listées parce que LEUR PROJET avait DMTG dans son périmètre, pas parce qu'elles la citent [L50 (mesuré)]
- FCT-007 : la fiche publi 108 pointe vers un PDF mort (dt-633.pdf, HTTP → 404) et un numéro de WP (dt-633) différent du n° 636 retenu au 11-13 : seconde faille de fiabilité documentaire du référentiel [L51 (mesuré)]
- FCT-008 : la source DMTG (src.php?id=106) documente son périmètre réel : échantillon de successions ayant payé des DMTG, MOOREA « exhaustives mais incomplètes », produits 2010 (DOI 10.34724/CASD.106.881.V1), 2006, 1994 [L52 (mesuré)]
- FCT-009 : la « sur-liste » de la fiche DMTG n'est ni une erreur ni une tromperie : c'est la conséquence structurelle du critère projet : toute publication d'un projet habilité DMTG hérite de la mention, indépendamment de son contenu [L53 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : CASD (référentiel, formulaire de remontée), CDAP, chercheurs (auto-déclaration), projets 254 (TAXOPTI), 1107 (EVREFIS), 1041 (France Stratégie/CGSP), Banque de France (PDF mort).

## 4. Sources externes citées

casd.eu/declaration-publications, casd.eu/remontees-des-publications, casd.eu/publi.php?id=108/457/454/455, casd.eu/prj.php?id=254/1107/1041, casd.eu/src.php?id=106, test HTTP dt-633.pdf.

## 5. Chronologie datée

26/02/2015 : mise à disposition DMTG 2010 (DOI) ; 10/08/2026 : identification du critère de rattachement (GAP 1 du 10-54 résolu).

## 6. Mécanismes / chaînes causales

**M1 — Le registre d'accès potentiel** : publication → projet → toutes les sources du projet : la chaîne ne contient AUCUNE vérification d'usage dans le texte ; la fiche source agrège les héritages de projet, pas les exploitations documentées. Force : EXTRÊME. Niveau : L1. [L45-L47 (mesuré)]
**M2 — La preuve par identité ensembliste** : 19=19, 68=68, 97=97 : l'égalité exacte des ensembles établit le mécanisme de façon démonstrative (3 projets vérifiés). Force : EXTRÊME. Niveau : L1. [L46 (mesuré)]
**M3 — Le biais de plaidoyer structurel** : le dispositif sur-atteste l'usage dans un sens favorable à sa propre démonstration de pertinence (preuve auprès des bailleurs) : à lire avec cette clé, sans imputation de mauvaise foi. Force : HAUTE. Niveau : L2. [L48, L53 (mesuré)]

## 7. Verbatim et citations

- « Un registre d'accès n'est pas un registre d'usage » [L59 (mesuré)]
- « Le CASD documente ce que ses projets pouvaient toucher, pas ce que leurs papiers ont utilisé : et il le fait par construction (formulaire de remontée par code projet, libellé "mises à disposition") » [L60 (mesuré)]
- « Ne jamais citer une fiche source CASD comme preuve d'exploitation d'une donnée » [L61 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : 6 pages CASD lues (formulaires, fiches publi/prj/src) ; identité ensembliste vérifiée par identifiants src.php?id ; FCT-007 constat (URL morte + numérotation flottante).
- **F-##** : 9/9 identifiants FCT-001..009 préservés.
- **Méthode** : hypothèse « thème vs usage » dépassée par le mécanisme projet, preuve arithmétique 3 projets, pelote, gate_check.

## 9. Limites connues (case-limites)

- Le traitement interne (validation CASD, mise à jour des fiches) n'est pas documenté publiquement : la chaîne exacte « soumission → fiche publi → fiche source » est déduite de la structure des pages, cohérente sur 3 projets.
- La page de méthodologie du référentiel CDAP n'a pas été identifiée.
- L'exhaustivité des 97 sources du projet 1041 n'a pas été recoupée page à page (DMTG id=106 vérifiée par grep).
- Recommandations : réutiliser le critère (projet + mention dans le texte), documenter la faille dt-633, cadrer une demande CADA au CASD (procédure interne de validation).
