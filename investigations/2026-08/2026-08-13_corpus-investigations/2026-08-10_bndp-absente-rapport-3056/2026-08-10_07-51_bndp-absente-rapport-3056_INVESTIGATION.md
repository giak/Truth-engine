# INVESTIGATION — GAP-005 RÉSOLU : la BNDP est absente du rapport 3056, même quand il décrit l'exploitation CdC

```
STATE          : FINAL
DATE           : 2026-08-10 07:51 CEST
TYPE           : INVESTIGATION
KERNEL         : v2.8
SUJET          : Recherche des mentions de la BNDP (Base Nationale des Données Patrimoniales)
                 dans le rapport n° 3056 (commission d'enquête « imposition des plus hauts
                 patrimoines »), Tomes 1 et 2 lus intégralement — exécution du GAP-005 du
                 dossier 07-46 (bndp-acces-exceptionnel).
OBJECT_QUESTION : « La DGFiP, la CdC ou le CPO ont-ils évoqué la BNDP et son régime d'accès
                 pendant les auditions de la commission Mattei/de Courson ? »
METHODE         : Grep exhaustif sur ce_t1.txt (Tome 1, 327 p., texte 946 Ko) et ce_t2.txt
                 (Tome 2, auditions) pour « BNDP » et 9 termes connexes (données
                 patrimoniales, base nationale, habilitation, données fiscales, FICOBA,
                 bases de données, accès aux données, données inédites) ; lecture des
                 contextes des passages pertinents ; identification des auditions (DESF,
                 DNVSF, Insee, CSN, CGPIF, ministre) ; lecture de la note (2) du T1 décrivant
                 l'exploitation CdC.
CONTEXTE        : Dossier 07-46 : la CdC a exploité la BNDP pour le rapport Dutreil (Annexe 4 :
                 « communiquées par la DGFiP à la Cour » + habilitation des rapporteurs).
                 Question ouverte : cette base a-t-elle été évoquée par la commission
                 d'enquête parlementaire constituée sur le même objet 6 mois plus tard ?
```

## 1. RÉSULTAT PRINCIPAL — CONSTAT D'ABSENCE (vérifié exhaustivement)

**La BNDP n'est JAMAIS nommée dans le rapport n° 3056 — ni dans le Tome 1 (lu intégralement), ni dans le Tome 2 (auditions, lu intégralement).**

Grep exhaustif (10 motifs) sur les deux tomes :
| Motif | T1 (ce_t1.txt) | T2 (ce_t2.txt) |
|-------|----------------|----------------|
| « BNDP » | **0** | **0** |
| « base nationale » | **0** | **0** |
| « habilitation » | 0 | 0 |
| « données inédites » | 1 (l. 7402 : reprise du rapport CdC) | 0 |
| « données patrimoniales » | 2 (l. 4421, 4536 — contexte général) | 2 (l. 11112, 11886) |
| « FICOBA » | — | 4 (l. 3632, 7219, 13135, 32430) |
| « données fiscales » | — | 8 |
| « bases de données » | — | 8 |
| « accès aux données » | — | 6 |

**La base que la commission interroge partout (Ficoba, Ficovie, déclarations de succession, « base à créer ») n'est jamais la BNDP — y compris par les acteurs qui l'utilisent.**

## 2. LA PREUVE DE L'ELLIPSE — note (2) du T1 (l. 7428-7436, verbatim)

Le Tome 1 décrit pourtant, en note de bas de page, l'exploitation exacte que la CdC a faite de la BNDP — **sans la nommer** :

> « (2) **La Cour des comptes a exploité des données fiscales issues des directions régionales ou départementales des finances publiques.** Ces informations comportant des lacunes, "la Cour a complété le périmètre des transmissions sous pacte Dutreil grâce à un **algorithme de reclassement statistique élaboré par l'IPP**, permettant d'y réintégrer des donations et des successions qui n'avaient pas été enregistrées par l'administration comme 'Dutreil' alors qu'elles avaient bénéficié de l'avantage fiscal". **Malgré cette correction, la Cour des comptes reconnaît que les données relatives au pacte Dutreil présentées dans son rapport demeurent encore probablement sous-estimées.** »
> — T1, note (2) p. 164.

**L'ellipse est documentée** : le rapport de la commission d'enquête sur l'imposition des plus hauts patrimoines décrit la source réelle du rapport CdC (données des directions des finances publiques + algorithme IPP + sous-estimation), mais le libellé « données fiscales issues des directions régionales ou départementales des finances publiques » **remplace** l'identification « base nationale des données patrimoniales (BNDP) » qu'utilise l'Annexe 4 du rapport CdC lui-même. Deux documents publiés à 6 mois d'intervalle désignent la même source de deux manières différentes — l'une la nomme, l'autre non.

## 3. LE PAYSAGE DE DONNÉES DÉCRIT PAR LES AUDITIONS (T2) — les substituts

| Audition (identifiée) | Passage | Ce qui est dit | BNDP ? |
|-----------------------|---------|----------------|--------|
| **DESF — Mme Sophie Maillard** (directrice du DESF) | l. 3620-3645 | Ficovie « pas encore complet » (amende max pour un assureur non déclarant : **1 500 €**) ; Ficoba à enrichir ; « l'exploitation des données de succession » pour reconstituer le patrimoine ; « À la manière des pièces d'un puzzle » — plutôt que d'instaurer une déclaration obligatoire | NON |
| **DNVSF — M. Tarick Adeida** (audition DNVSF : Fénelon, Créange, Perraud) | l. 11886-11888 | « Nous ne disposons pas de la même masse de données qu'à l'époque de l'ISF, mais nous obtenons un certain nombre de données patrimoniales, sur les opérations de flux » | NON |
| **Insee — M. Fabrice Lenglart** | l. 7169-7172 | « l'Insee a absolument besoin que la **DGFIP progresse dans la constitution d'une base de données des transmissions de patrimoine** » (le dit à Maillard et Verdier) | NON (demande une base à créer) |
| **CSN (notaires)** | l. 13125-13145 | Ficoba « relativement fiable, mais pas à 100 % » ; immobilier non déclaré « très marginal » ; assurance-vie traitée par les assureurs | NON |
| **Un commissaire (question)** — la réponse du **ministre David Amiel** suit (l. 32432+) | l. 32430 | Cryptoactifs : « la création de tels fichiers s'inscrirait dans la droite ligne d'outils existants, comme le **Ficovie** pour les contrats d'assurance vie et le **Ficoba** pour les comptes bancaires » (question du commissaire) ; la réponse d'Amiel (l. 32432+) ne nomme pas non plus la BNDP | NON |
| **CGPIF — M. Yves Mazin** (conseillers en gestion de patrimoine) | l. 11112-11140 | Données clients : « protégées par le RGPD », aucune consolidation, « la chambre n'a ni vocation, ni légitimité à les collecter » | NON |

**Fait notable en passant (FCT)** : l'amende maximale pour un assureur qui ne déclare pas tous les contrats d'assurance-vie est de **1 500 €** (l. 3624-3628, DESF) — un plafond dérisoire au regard des enjeux (l'assurance-vie représente ~2 100 Md€ d'encours, corpus 12-29).

## 4. INTERPRÉTATION — DEUX HYPOTHÈSES NON TRANCHABLES, UN FAIT OBJECTIF

**Le fait objectif :** la commission d'enquête sur les plus hauts patrimoines a mené des dizaines d'auditions, interrogé la DGFiP (DESF, DNVSF), l'Insee, les notaires, le CPO, la CdC — et **personne n'a nommé la BNDP**, alors que :
1. la CdC l'avait exploitée 6 mois plus tôt (rapport Dutreil, 18/11/2025) ;
2. la note (2) du T1 en décrit l'usage sans l'identifier ;
3. l'Insee demande la création d'une « base de données des transmissions de patrimoine » alors que l'outil existe depuis 2005 (dossier 07-46) ;
4. la DESF (qui gère la base au quotidien) décrit le paysage Ficoba/Ficovie sans la mentionner.

**Deux hypothèses explicatives, toutes deux non tranchables avec les sources disponibles :**
- **H1 — méconnaissance** : la BNDP est un outil de gestion interne, connu des seuls praticiens du contrôle ; les auditionnés (y compris la DESF) ne la considèrent pas comme une source statistique et ne la citent pas ;
- **H2 — ellipse délibérée** : la commission n'a pas souhaité mettre en avant l'existence d'une base patrimoniale nationale exploitée par la CdC, qui aurait affaibli le récit du « trou de connaissance » (l'« angle mort statistique majeur » du Sénat 760).

Le corpus ne peut pas trancher entre H1 et H2 — c'est un constat d'absence, pas une preuve d'intention. **Mais le contraste est objectif et documenté** : d'un côté, la BNDP exploitée intégralement par la CdC (dossier 07-46) ; de l'autre, une commission parlementaire qui interroge Ficoba/Ficovie et demande à créer une base que la BNDP aurait pu fournir. La chaîne « l'État sait, le parlement interroge, le public ignore » (dossier 23-25) se prolonge d'un maillon : **le parlement lui-même n'identifie pas l'outil qu'il pourrait contraindre**.

## 5. FACT_REGISTRY

| ID | Fait | Valeur | Source | Statut |
|----|------|--------|--------|--------|
| FCT-001 | **BNDP : 0 mention dans le rapport 3056** (T1 + T2 lus intégralement, grep 10 motifs) | 0 | ce_t1.txt, ce_t2.txt | ✦ (constat d'absence) |
| FCT-002 | **Note (2) du T1 (l. 7428-7436)** : le rapport décrit l'exploitation CdC — « données fiscales issues des directions régionales ou départementales des finances publiques », algorithme de reclassement IPP, « données... probablement sous-estimées » — **sans nommer la BNDP** (contrairement à l'Annexe 4 du rapport CdC) | verbatim | T1 note (2) p. 164 | ✦ |
| FCT-003 | **DESF (Maillard, audition)** : Ficovie « pas encore complet » ; **amende max 1 500 €** pour assureur non déclarant ; Ficoba à enrichir ; exploitation des données de succession en « pièces d'un puzzle » ; pas de BNDP | 1 500 € | T2 l. 3620-3645 | ✦ |
| FCT-004 | **DNVSF — M. Tarick Adeida** : « nous ne disposons pas de la même masse de données qu'à l'époque de l'ISF » | verbatim | T2 l. 11886-11888 | ✦ |
| FCT-005 | **Insee (Lenglart)** : « l'Insee a absolument besoin que la DGFIP progresse dans la constitution d'une base de données des transmissions de patrimoine » — demande une base à créer, sans évoquer la BNDP existante | verbatim | T2 l. 7169-7172 | ✦ |
| FCT-006 | **CSN (notaires)** : Ficoba « relativement fiable, mais pas à 100 % » ; immobilier non déclaré « très marginal » | verbatim | T2 l. 13125-13145 | ✦ |
| FCT-007 | **Un commissaire (question, l. 32430)** cite Ficovie/Ficoba comme modèles d'outils pour les fichiers crypto — pas la BNDP ; la réponse du **ministre David Amiel** (l. 32432+) ne la nomme pas non plus | verbatim | T2 l. 32430, 32432+ | ✦ |
| FCT-008 | **CGPIF (Mazin)** : données clients protégées RGPD, aucune consolidation, la chambre « n'a ni vocation, ni légitimité à les collecter » | verbatim | T2 l. 11112-11140 | ✦ |
| FCT-009 | La même source est désignée différemment : **« données fiscales issues des directions... » (3056, note 2) vs « BNDP » (CdC, Annexe 4)** — ellipse d'identification documentée | 2 désignations | T1 note (2) ; CdC Annexe 4 (07-46) | ✦ |

## 6. CONTRADICTIONS

| ID | Contradiction | Résolution |
|----|---------------|------------|
| CONTR-001 | L'Insee demande une « base de données des transmissions de patrimoine » à créer (l. 7169) alors que la BNDP existe depuis 2005 et contient ces transmissions (07-46) | La BNDP est un outil de gestion (saisie des transmissions pour l'impôt), pas une base statistique : l'Insee demande une base **exploitable statistiquement** (comme le module DMTG 2.0 du Sénat 760). La nuance est réelle — mais elle n'explique pas que la BNDP ne soit jamais nommée par la DESF elle-même. |
| CONTR-002 | La DNVSF dit « ne pas disposer de la même masse de données qu'à l'époque de l'ISF » (l. 11886) alors que la BNDP agrège les données patrimoniales (07-46) | Les deux se cumulent : la perte ISF a appauvri la connaissance patrimoniale *déclarée*, et la BNDP (base de gestion, volet DMTG insuffisant pour la statistique — Sénat 760) ne compense pas. La remarque DNVSF porte sur la connaissance statistique, pas sur l'existence de l'outil. |

## 7. LIMITES

1. Le grep porte sur les fichiers texte extraits (pdftotext -layout) : une mention de « BNDP » dans une note de bas de page mal extraite pourrait théoriquement manquer — le double grep (T1/T2) et la présence des motifs connexes rendent ce risque faible mais non nul.
2. Les intitulés exacts des auditions (dates, compte-rendus) n'ont pas tous été extraits : les identifications (DESF/Maillard, DNVSF/Adeida-Fénelon-Créange-Perraud, Insee/Lenglart, CSN, question crypto + réponse Amiel, CGPIF/Mazin) reposent sur les répliques et le contexte — **y compris l'identification des locuteurs individuels : deux erreurs d'attribution ont été corrigées à la revue (la citation « moins de données qu'à l'époque de l'ISF » est d'Adeida, pas de Fénelon ; la citation Ficovie/Ficoba est du commissaire, pas du ministre Amiel)**.
3. H1/H2 (§4) sont des hypothèses : le corpus ne peut pas trancher entre méconnaissance et ellipse délibérée.
4. Le rapport 3056 a été lu intégralement (T1, T2) mais les comptes-rendus d'auditions complets (documents séparés) n'ont pas tous été relus — une mention de la BNDP hors rapport n'est pas exclue (mais le rapport n° 3056 lui-même ne la contient pas).

## 8. GAPS / ACTIONS

| ID | Action | Priorité |
|----|--------|----------|
| GAP-001 | Vérifier si la BNDP apparaît dans les comptes-rendus d'auditions publiés à part (page AN de la commission) — complément hors rapport | 3 |
| GAP-002 | Interroger directement la DESF ou le CPO (questions écrites) : « Pourquoi la BNDP n'a-t-elle pas été évoquée devant la commission ? » — seule voie pour tester H1/H2 | 3 |
| GAP-003 | Croiser avec le Sénat 760 : le Sénat nomme-t-il la BNDP ? (oui — p. 14, dossier 07-26) : la commission AN ne la nomme pas, le Sénat si — documenter la divergence inter-chambres | 2 |

## 9. LEÇON

La commission d'enquête sur les plus hauts patrimoines a interrogé les données patrimoniales pendant des mois, a décrit l'exploitation d'une source d'une richesse inédite, exploitée intégralement pour la première fois (note 2), et **ne l'a jamais nommée**. La BNDP — base nationale détenue depuis 2005, exploitée intégralement par la CdC avec l'IPP, dotée d'un régime d'accès à cinq (DGFiP, douanes, TRACFIN, CdC, IPP) — est l'angle mort d'un rapport consacré à l'imposition des plus hauts patrimoines. Deux lectures possibles, aucune tranchable : l'outil est si interne qu'il n'existe pas dans le langage statistique même de la DESF qui le gère (H1), ou la commission a préféré le récit du « manque de données » à la réalité d'une base exploitable sur demande (H2). Dans les deux cas, le constat renforce le fil du corpus (07-46, 07-26, 23-25) : **la connaissance patrimoniale existe, elle est confinée, et même le parlement, qui aurait pu la contraindre, ne l'identifie pas** — au point que l'Insee demande la création d'une base qui existe depuis vingt ans.
