# Quintessence : Cartographie du pantouflage HATVP (Ministère × Secteur)

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-11_corpus-anticorruption/2026-08-11_23-45_cartographie-pantouflage-hatvp_INVESTIGATION.md` (166 lignes, 10 FCT-carto)
Date extraction : 2026-08-13 04:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot corpus-anticorruption)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format allégé, PARENT : REGISTRE ICEBERG MAX (2026-08-11_23-14)
- **Date source** : 2026-08-11 23:45 CEST, STATE FINAL
- **Identifiants source** : 10 FCT-carto-001 à 010
- **Object** : cartographier le pantouflage HATVP par croisement ministère × secteur : combien de DG Énergie → ENR, combien de Santé → Pharma ?
- **Verdict source** : IMPOSSIBLE à quantifier précisément avec les données publiques actuelles (pas de base structurée, 70-93 % des avis non publiés, noms anonymisés) ; destination n°1 = conseil/consulting (17,3 %), n°2 = médias (11,2 %)

## 2. Faits atomiques préservés

- FCT-carto-001 : la HATVP ne publie PAS de base structurée des avis de mobilité (CSV/API), uniquement des PDFs individuels sur un moteur de recherche [L119 (mesuré)]
- FCT-carto-002 : 698 avis de mobilité publiés 2020-2026 (sur ~3 000+ rendus) ; 42 % n'ont pas de destination identifiable dans les premiers 3000 caractères du PDF [L123 (mesuré)]
- FCT-carto-003 : la destination #1 est le CONSEIL/CONSULTING (17,3 % des avis identifiés) : McKinsey, BCG, Capgemini, etc. [L124 (mesuré)]
- FCT-carto-004 : la destination #2 est les MÉDIAS (11,2 %), cohérent avec le constat de 78 avis vers ce secteur [L125 (mesuré)]
- FCT-carto-005 : le registre des représentants d'intérêts compte 3 989 entités uniques en 2026 [L126 (mesuré)]
- FCT-carto-006 : secteurs les plus représentés au registre des lobbys : Finance (2 736), Conseil (2 585), Énergie (1 516), Santé (1 562) [L127 (mesuré)]
- FCT-carto-007 : 103 entités du registre des lobbys mentionnent l'éolien ; 100 le solaire (cohérent avec l'enquête run2-enr) [L128 (mesuré)]
- FCT-carto-008 : la HATVP a rendu 639 avis de mobilité en 2024 et 641 en 2025 ; 4,5 % d'incompatibilités [L129 (mesuré)]
- FCT-carto-009 : le taux de publication des avis est passé de 6,5 % (2022) à 25 % (2023) à ~165 in extenso (2024) : la majorité des avis reste non publiée [L130 (mesuré)]
- FCT-carto-010 : aucune base de données ne permet de répondre « combien de DG Énergie → ENR » ou « combien de Santé → Pharma » sans parser manuellement tous les PDFs [L131 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : HATVP, Commission de déontologie (contexte pré-2020), data.gouv.fr.
**Secteurs destinations** : Conseil/consulting (121 avis), Médias (78), Numérique/Tech (57), Énergie (48), Commerce/Distribution (36), BTP/Immobilier (13), Télécoms (10), Fonds d'investissement (8), Assurance (6), Transport (5), Pharma/Santé (4), Eau (4), Banque (1), Défense (1).
**Origines croisées (matrice brute)** : CRE (616 mentions, majoritairement des réserves), Santé, Trésor, Défense, Cabinet.

## 4. Sources externes citées

773 PDFs HATVP (2014-2026, /tmp/vp44_txt), registre lobbys JSON (137 MB, 3 989 entités, 4 065 publications), data.gouv.fr HATVP (déclarations d'intérêts XML), rapports annuels HATVP (639 avis 2024, 641 en 2025).

## 5. Chronologie datée

01/02/2020 : compétence mobilité HATVP (avant : Commission de déontologie, avis jamais publiés) ; 2020 : 21 avis ; 2021 : 24 ; 2022 : 42 ; 07/02/2023 : élargissement de la publication décidé par le collège ; 2023 : 120 avis ; 2024 : 197 (639 rendus) ; 2025 : 233 (641 rendus) ; 2026 : 51 (partiel) ; +458 % d'avis publiés entre 2022 et 2025.

## 6. Mécanismes / chaînes causales

**M1 — Le trou de transparence structurel** : pas de base structurée, 70-93 % des avis jamais publiés, 95 % des PDFs anonymisés, 42 % des destinations non identifiables : une étude exhaustive du pantouflage est structurellement impossible en sources ouvertes. Niveau : L2. [L119, L123, L130-L131 (mesuré)]
**M2 — La destination dominante : le conseil** : 17,3 % des avis publiés vont vers le conseil/consulting (McKinsey, BCG, Capgemini), 11,2 % vers les médias : le pantouflage nourrit d'abord les cabinets de conseil et les médias, avant l'énergie (6,9 %). Niveau : L2. [L124-L125 (mesuré)]
**M3 — L'alerte méthodologique sur la matrice brute** : les 616 mentions « CRE » sont majoritairement des réserves (abstention de démarche auprès de la CRE), pas des départs réels : les vrais départs CRE → privé sont de l'ordre de quelques unités/an (Carenco, Bohuon). Niveau : L2 (correction méthodologique). [L119 (estimé)]

## 7. Verbatim et citations

- « Combien de DG Énergie → ENR, combien de Santé → Pharma ? Réponse : IMPOSSIBLE à quantifier précisément avec les données publiques actuelles » [L114 (mesuré)]
- « Le taux de publication des avis est passé de 6,5 % (2022) à 25 % (2023) : la majorité des avis reste non publiée » [L130 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : parsing 773 PDFs (keywords), registre lobbys JSON, rapports annuels ; ALERTE MÉTHODOLOGIQUE documentée sur les chiffres bruts non dédoublonnés.
- **F-##** : 10/10 identifiants FCT-carto-001 à 010 préservés verbatim.
- **Méthode** : extraction table HATVP, distribution par année/type/secteur, registre des lobbys, matrice croisée origine × destination, recommandation (parser tous les PDFs in extenso, 8-12 h de développement).

## 9. Limites connues (case-limites)

- 42,4 % des destinations non identifiées (dans les 3000 premiers caractères) : la distribution réelle est probablement différente.
- 2014-2019 : aucune donnée (avis jamais publiés avant la compétence HATVP du 01/02/2020).
- La matrice croisée est brute et non dédoublonnée : à ne pas lire comme des départs réels (faux positifs massifs).
- Action recommandée : parser les ~165-200 PDFs in extenso par an + NLP pour extraire les triplets (nom, origine, destination), 8-12 h de développement.
