# INVESTIGATION : P11 — FRAUDE AU CPF (COMPTE PERSONNEL DE FORMATION)

- STATE          : FINAL
- DATE           : 2026-08-12 04:30 CEST
- TYPE           : INVESTIGATION (KERNEL v2.8, format léger, axe anticorruption)
- DOSSIER        : 2026-08-11_corpus-anticorruption (ICEBERG MAX, piste P11)
- OBJECT         : documenter la fraude au CPF : montants, mécanismes, réseaux criminels, répression, failles structurelles
- SOURCES        : France Info, TF1 Info, Douane française (ONAF), CDC, Légifrance (loi 2022-1587), Landot Avocats, Centre Inffo
- PRIOR          : GAP-ice-009 du REGISTRE ICEBERG MAX v3 (P1)

---

## SYNTHÈSE

La fraude au CPF est le cas le plus pur de **détournement massif d'argent public sans corruption politique identifiée**. Entre 300 et 400 M€ de préjudice total estimé depuis le lancement, deux réseaux criminels majeurs démantelés (31 M€ à Trappes, 15 M€ en Auvergne-Rhône-Alpes/PACA), et un taux de fraude de 90 % parmi les organismes contrôlés (171/185 frauduleux). La faille est structurelle : un système conçu pour la fluidité (crédits individuels, accès simplifié) sans contrôles ex ante, corrigé seulement après coup par la loi de 2022. Le pattern est inverse de celui des ENR : ici la fraude est pénale et documentée, mais le système a été volontairement conçu sans garde-fous.

**Verdict 3 axes** : Pénal = FRAUDE MASSIVE (réseaux criminels, blanchiment). Légal = ILLÉGAL (escroquerie en bande organisée). Légitime = NON — le contribuable paie deux fois : les crédits CPF détournés + le coût de la répression.

---

## FAITS

| ID | Fait | Source | Date |
|---|---|---|---|
| FCT-p11-001 | Préjudice total estimé de la fraude au CPF : 300-400 M€ depuis le lancement | Douane française, France Info | 2020-2025 |
| FCT-p11-002 | Réseau de Trappes/Yvelines démantelé en septembre 2024 : 31 M€, 120-200 sociétés écrans, blanchiment via achat de voitures revendues au Maroc | France Info, PJ Versailles | 09/2024 |
| FCT-p11-003 | Donneur d'ordres du réseau Trappes : homme de 35 ans issu du trafic de stupéfiants | France Info | 09/2024 |
| FCT-p11-004 | Réseau Auvergne-Rhône-Alpes/PACA démantelé par ONAF le 28/01/2025 : 15 M€+, 9 interpellations, 1,27 M€ d'avoirs saisis | Douane française (ONAF) | 28/01/2025 |
| FCT-p11-005 | Loi n° 2022-1587 du 19/12/2022 : interdiction totale du démarchage CPF, décloisonnement données CDC↔Tracfin↔ fisc, renforcement sanctions | Légifrance | 19/12/2022 |
| FCT-p11-006 | CDC : 171 organismes sur 185 contrôlés étaient frauduleux (taux de fraude 92 %) lors d'enquêtes pilotes | TF1 Info / CDC | 2023-2024 |
| FCT-p11-007 | Convention CDC-ONAF signée le 07/10/2025 pour croiser les données et accélérer les enquêtes | CDC (Politiques Sociales) | 07/10/2025 |
| FCT-p11-008 | FranceConnect+ déployé comme barrière technique anti-fraude sur MonCompteFormation | CDC / Centre Inffo | 2024-2025 |
| FCT-p11-009 | Aucune personnalité politique de premier plan impliquée dans les enquêtes CPF | France Info, TF1 | 2024-2026 |
| FCT-p11-010 | Profil des fraudeurs : narcotrafiquants reconvertis, faux comptables, créateurs en série de sociétés écrans | France Info, TF1 | 2024-2025 |
| FCT-p11-011 | Mécanisme principal : création de sociétés fictives de formation → démarchage abusif → inscription de faux stagiaires → facturation CDC → blanchiment | TF1 Info, Douane | 2020-2025 |
| FCT-p11-012 | TA de Lyon a confirmé en 2026 des blocages de fonds et déréférencements d'un an pour des fraudes de plusieurs centaines de milliers d'euros par structure | Landot Avocats | 02/2026 |
| FCT-p11-013 | Budget annuel CPF : plusieurs milliards d'euros (crédits individuels gérés par la CDC via France Compétences) | CDC | Permanent |
| FCT-p11-014 | ONAF (Office National Anti-Fraude) : officiers de douane judiciaire dédiés aux fraudes aux finances publiques — outil principal de répression CPF | Douane française | 2024-2026 |

---

## MÉCANISMES STRUCTURELS APPLICABLES

| # | Mécanisme | Application au CPF | Force |
|---|---|---|---|
| **M1** | Contrôle ineffectif | Conçu SANS contrôle ex ante : crédits individuels, accès libre. Contrôle ajouté APRÈS la fraude (loi 2022). 171/185 faux organismes non détectés avant enquête. | EXTRÊME |
| **M2** | Chiffres absents ou tardifs | La CDC ne publie pas de chiffres consolidés de la fraude détectée. Les montants (300-400 M€) viennent de la presse judiciaire, pas d'un rapport officiel. | HAUTE |
| **M3** | Capture du cadre légal | Le CPF a été conçu comme un « droit individuel » avec accès simplifié — au détriment de tout contrôle. La loi 2022 n'est intervenue qu'après le scandale. | HAUTE |
| **M5** | Sous-traitance opaque | La sous-traitance en cascade des formations (organisme certificateur → sous-traitant → formateur fantôme) est le vecteur principal de fraude | HAUTE |
| **M7** | Criminalité organisée | Contrairement aux autres pistes (ENR, DSP, conseil) où la corruption est politico-administrative, le CPF attire le crime organisé (narcotrafiquants). Pattern distinct. | EXTRÊME |

---

## 5 CHAÎNES (doctrine anticorruption §12)

| Chaîne | État | Détail |
|---|---|---|
| **1. AUTORITÉ** | IDENTIFIÉE | CDC (gestionnaire MonCompteFormation), France Compétences (régulateur), État (loi 2022), ONAF (répression) |
| **2. ARGENT** | CHIFFRÉE | Budget CPF : plusieurs Md€/an. Fraude estimée : 300-400 M€ cumulés. Réseau Trappes : 31 M€. Réseau ONAF : 15 M€. |
| **3. BÉNÉFICIAIRE** | IDENTIFIÉ | Réseaux criminels (narcotrafiquants reconvertis), organismes de formation fictifs, prête-noms. PAS de politiciens identifiés — pattern distinct. |
| **4. CONTRE-AVANTAGE** | DOCUMENTÉ | Blanchiment d'argent sale via le CPF : achat de voitures revendues au Maroc, saisies d'avoirs criminels (1,27 M€ réseau ONAF) |
| **5. CONTRÔLE** | RENFORCÉ MAIS TARDIF | Loi 2022 (interdiction démarchage, décloisonnement données), convention CDC-ONAF 10/2025, FranceConnect+, détection algorithmique. Le contrôle a été ajouté APRÈS 300-400 M€ de fraude. |

---

## VERDICT 3 AXES

| Axe | Verdict | Détail |
|---|---|---|
| **PÉNAL** | FRAUDE MASSIVE | Deux réseaux démantelés (46 M€ cumulés). Escroquerie en bande organisée, blanchiment. Narcotrafiquants reconvertis. Enquêtes ONAF actives. |
| **LÉGAL** | ILLÉGAL | Escroquerie au sens du code pénal. Loi 2022 a corrigé le cadre mais n'a pas annulé le préjudice déjà commis. |
| **LÉGITIME** | NON | Le système a été conçu sans garde-fous, corrigé seulement après 300-400 M€ de pertes. Le contribuable paie deux fois : les crédits détournés + le coût de la répression. |

---

## GAPs

| ID | GAP | Priorité |
|---|---|---|
| GAP-p11-1 | Chiffre officiel consolidé de la fraude CPF par la CDC/Cour des comptes | P0 |
| GAP-p11-2 | Rapport d'activité ONAF 2025 : bilan complet des saisies et démantèlements CPF | P1 |
| GAP-p11-3 | Cartographie des organismes de formation radiés (liste CDC/Qualiopi) | P2 |
| GAP-p11-4 | Volume des crédits CPF non consommés (dormants) = cible potentielle de fraude future | P2 |

---

## INTERPRÉTATION

Le cas CPF est le **miroir inversé des ENR** dans le corpus anticorruption :

| Caractéristique | ENR (Valeco, OA) | CPF |
|---|---|---|
| Type de détournement | Rente légale sans plafond | Fraude pénale massive |
| Bénéficiaires | Grands groupes (EnBW, EDF, Engie) | Crime organisé (narcotrafiquants) |
| Contrôle | Inexistant (rec. n°1 CdC refusée) | Ajouté APRÈS (loi 2022, ONAF) |
| État de la répression | 0 CJIP ENR | 2 réseaux démantelés, saisies |
| Visibilité politique | Nulle | Forte (scandale médiatique) |

La différence fondamentale : le CPF est un **détournement criminel par le bas** (petites sociétés écrans, crime organisé), alors que les ENR sont un **détournement légal par le haut** (grands groupes, OA sans plafond, absence de contrôle). Le premier est réprimé ; le second ne l'est pas.

Cette asymétrie est structurelle : il est politiquement plus facile de réprimer des narcotrafiquants que de s'attaquer aux rentes d'EDF, Engie, EnBW et aux 87 Md€ d'engagements de l'État sur les contrats OA.
