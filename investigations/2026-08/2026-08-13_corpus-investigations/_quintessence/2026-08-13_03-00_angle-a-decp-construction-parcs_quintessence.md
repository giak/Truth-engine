# Quintessence : Angle A, test de la méthode DECP sur la construction de parcs ENR

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/2026-08-11_05-00_angle-a-decp-construction-parcs_INVESTIGATION.md` (61 lignes, 8 FCT-ena)
Date extraction : 2026-08-13 03:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot run2-enr)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format allégé, ANGLE A de la stratégie 04-56 (gonflement des factures sur construction de parcs)
- **Date source** : 2026-08-11 05:00 CEST, STATE FINAL
- **Identifiants source** : 8 FCT-ena-001 à 008
- **Object** : tester la transposabilité de la méthode DECP (validée sur le pilote SESN) au secteur ENR : détection d'avenants/surfacturation sur les marchés de construction de parcs éoliens et solaires
- **Verdict source** : l'angle A via le canal DECP est INFIRMÉ pour les parcs privés (trou de couverture structurel) ; le DECP capture bien le PV public de toiture (SDEM/SOREGIES)

## 2. Faits atomiques préservés

- FCT-ena-001 : le DECP contient 3 325 marchés ENR (objet éolien/solaire) [L22 (mesuré)]
- FCT-ena-002 : ZÉRO avenant dans le périmètre ENR du DECP (nature = Marché pour 3 320/3 325, 1 partenariat, 3 concessions travaux, 1 concession service) [L23 (mesuré)]
- FCT-ena-003 : 129 marchés ENR dédupés >= 1 MEUR, total brut 3,05 Md€ (dont montants plafonds encodés non réels : UGAP 1,25 Md€, Grasse 999 999 999 €, CA Saint-Louis 202,5 M€) ; hors plafonds, le total réel est ~500 M€ [L24 (mesuré)]
- FCT-ena-004 : 1 SEUL marché éolien >= 1 MEUR (accord-cadre international d'études/conseil à 5 M€, acheteur = AFD, Agence française de développement) : les marchés de construction de parcs éoliens sont ABSENTS du DECP [L25 (mesuré)]
- FCT-ena-005 : les gros montants solaires sont des accords-cadres de fourniture et des concessions d'ombrières (UGAP, Grasse, CA Saint-Louis) [L26 (mesuré)]
- FCT-ena-006 : les acheteurs publics ENR récurrents sont les syndicats d'énergie locaux : SDEM Morbihan (255601106, 118,2 M€, 6 marchés construction centrales PV > 100 kW) et SOREGIES Vienne (450889225, 21,9 M€, 8 marchés dont 2 centrales au sol à Vivonne) [L27 (mesuré)]
- FCT-ena-007 : l'essentiel des marchés solaires >= 1 MEUR porte sur des toitures/ombrières/bâtiments, pas sur des parcs au sol de grande taille [L28 (mesuré)]
- FCT-ena-008 : aucun titulaire renseigné dans le DECP global pour les marchés ENR (champ titulaires vide) [L29 (mesuré)]

## 3. Acteurs nominaux

**Acheteurs publics** : SDEM Morbihan, SOREGIES Vienne, UGAP, CA Saint-Louis, Grasse, AFD.
**Structure** : SPV privées (sociétés de projet) des parcs éoliens/solaires au sol, financées sur fonds propres.
**Institutions** : CRE, EDF OA (contrats de soutien en aval), data.gouv.fr (dataset DECP).

## 4. Sources externes citées

data/decp-global.json (1 Go, hashé 10/08, 705 471 objets), scripts data/extraire_enr.py et data/analyse_enr.py, API recherche-entreprises.data.gouv.fr, CSV /tmp/enr_angle_a/decp_enr_big.csv.

## 5. Chronologie datée

10/08/2026 : hash du dataset DECP ; 11/08/2026 05:00 : extraction et analyse (filtre mots-clés éolien/solaire, dédup >= 1 MEUR, lecture 115 objets).

## 6. Mécanismes / chaînes causales

**M1 — Le trou de transparence par construction, pas par contournement** : dans les parcs privés, l'argent public entre par le contrat de soutien (OA/CR avec la CRE) en aval, pas par un marché de construction ; le développeur construit sur fonds propres, donc aucune commande publique à publier. Niveau : L2. [L36 (mesuré)]
**M2 — La nuance juridique sur les SPV** : une SPV financée majoritairement par un pouvoir adjudicateur (art. L. 1211-1 s. code de la commande publique) peut être soumise (les 3 concessions de travaux de FCT-ena-002 le montrent) : la formulation « SPV non assujetties » serait une simplification. Niveau : L2. [L36 (mesuré)]
**M3 — Le fil central renforcé** : l'invisibilité de la construction (DECP vide) et des coûts (rec. n°1 CdC non mise en œuvre) n'est pas un accident de dataset : elle découle de la structure de financement. Niveau : L2. [L36 (mesuré)]

## 7. Verbatim et citations

- « les marchés de construction de parcs éoliens sont ABSENTS du DECP » (trou de couverture) [L25 (mesuré)]
- « le parallèle SESN n'est pas transposable : la SCSNE était elle-même un acheteur public » [L36 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : extraction exécutée (pas simulée) sur le dataset complet ; API entreprise pour les identifications SIREN.
- **F-##** : 8/8 identifiants FCT-ena-001 à 008 préservés verbatim.
- **Méthode** : réutilisation des scripts du pilote SESN (R-règles code reuse), filtrage par mots-clés objet, dédup (objet, acheteur, montant).

## 9. Limites connues (case-limites)

- GAP-ena-1 : champ titulaires vide : la concentration par titulaire n'est pas calculable sans rapprochement RNE/INPI ; l'hypothèse de fond (avenants/surfacturation sur parcs) reste NON TESTÉE (UNKNOWN), pas infirmée.
- GAP-ena-2 : montants plafonds encodés exclus des agrégats.
- Limite : extraction par mots-clés objet uniquement (pas par CPV ni SIREN titulaire) ; le DECP consolidé ne couvre qu'une partie des acheteurs (data.gouv, pes, aws).
- Les canaux alternatifs restants : BOAMP/TED volontaires, presse spécialisée, demandes d'accès directes, CADA à l'administration (autorisations).
