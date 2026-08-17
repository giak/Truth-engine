# ANGLE A DU RUN2-ENR : TEST DE LA MÉTHODE DECP SUR LA CONSTRUCTION DE PARCS ENR (ÉOLIEN/SOLAIRE)

> Type : INVESTIGATION. Date : 2026-08-11 05:00 CEST.
> Objet : ANGLE A de la stratégie 04-56 (gonflement des factures sur construction de parcs). Test de viabilité du canal DECP (données essentielles de la commande publique) pour détecter avenants/surfacturation sur les marchés de construction de parcs éoliens et solaires.
> Contexte : la méthode DECP a été validée sur le pilote SESN (avenants SCSNE, dédup SIREN, mesures). Question : est-elle transposable au secteur ENR ?
> Sources : `data/decp-global.json` (1 Go, hashé 10/08, dataset DECP data.gouv.fr), scripts `data/extraire_enr.py` et `data/analyse_enr.py`, API recherche-entreprises.data.gouv.fr.

## 1. MÉTHODE (EXÉCUTÉE, PAS SIMULÉE)

1. Parcours du fichier DECP global (705 471 objets JSON, 1 Go) avec filtrage des objets contenant un mot-clé ENR dans le champ objet (eolien, eolienne, photovolta, centrale solaire, parc solaire, ferme eolienne, aerogenerateur, aerogener, eoliennes).
2. Extraction des records ENR, distribution des natures, comptage des avenants.
3. Filtrage >= 1 MEUR, dédup par (objet normalisé, acheteur, montant).
4. Identification des acheteurs via l'API recherche-entreprises.data.gouv.fr (SIREN -> nom).
5. Séparation éolien / solaire et lecture détaillée des objets pour distinguer parcs au sol vs toitures/ombrières.

Artefacts : `/tmp/enr_angle_a/decp_enr_big.csv` (129 lignes dedup >= 1 MEUR), scripts dans `data/` du pilote SESN (réutilisés, R-règles code reuse).

## 2. FACT-CHECKS (FCT)

| FCT | Fait | Source | Verdict |
|-----|------|--------|---------|
| FCT-ena-001 | Le DECP contient 3 325 marchés ENR (objet éolien/solaire) | Extraction décp-global.json, filtre mots-clés | CONFIRMÉ |
| FCT-ena-002 | **Zéro avenant** dans le périmètre ENR du DECP (nature = Marché pour 3 320/3 325, 1 partenariat, 3 concessions travaux, 1 concession service) | Distribution natures, extraction | CONFIRMÉ (constat d'absence) |
| FCT-ena-003 | 129 marchés ENR dédupés >= 1 MEUR, total brut 3,05 Md€ (dont montants plafonds encodés non réels : UGAP 1,25 Md€, Grasse 999 999 999 €, CA Saint-Louis 202,5 M€) ; **hors plafonds, le total réel est ~500 M€** | CSV /tmp/enr_angle_a/decp_enr_big.csv | CONFIRMÉ (agrégat à lire hors montants plafonds) |
| FCT-ena-004 | **1 seul marché éolien** >= 1 MEUR (accord-cadre international d'études/conseil à 5 M€, acheteur 77566559900129 = **AFD, Agence française de développement** via API recherche-entreprises) : les marchés de construction de parcs éoliens sont ABSENTS du DECP | analyse_enr.py + API entreprise | CONFIRMÉ (trou de couverture) |
| FCT-ena-005 | Les gros montants solaires sont des accords-cadres de fourniture et des concessions d'ombrières : UGAP 1,25 Md€ (fourniture panneaux/PAC, valeur max indicative), Grasse 999 999 999 € (concession parking, montant encodé au plafond), CA Saint-Louis 202,5 M€ (centrale site sportif) | CSV + API entreprise | CONFIRMÉ |
| FCT-ena-006 | Les acheteurs publics ENR récurrents sont les syndicats d'énergie locaux : SDEM Morbihan (255601106, 118,2 M€, 6 marchés construction centrales PV > 100 kW) et SOREGIES Vienne (450889225, 21,9 M€, 8 marchés dont 2 centrales au sol à Vivonne) | API recherche-entreprises + CSV | CONFIRMÉ |
| FCT-ena-007 | L'essentiel des marchés solaires >= 1 MEUR porte sur des toitures/ombrières/bâtiments (techno-centre, parking, hangars, réhabilitations), pas sur des parcs au sol de grande taille | Lecture détaillée 115 objets | CONFIRMÉ |
| FCT-ena-008 | Aucun titulaire renseigné dans le DECP global pour les marchés ENR (champ titulaires vide dans l'extraction) | CSV (colonne titulaires vide) | CONFIRMÉ (limite dataset, déjà connue du pilote SESN) |

## 3. VERDICT : L'ANGLE A VIA LE CANAL DECP EST INFIRMÉ (TROU DE COUVERTURE STRUCTUREL)

1. **Hypothèse testée** : le DECP permet de recenser les marchés de construction de parcs ENR et d'y chercher des avenants (gonflement des factures), comme pour le pilote SESN.
2. **Résultat** : NON. Le DECP est quasi vide pour la construction de parcs éoliens au sol (1 accord-cadre d'études de l'AFD sur 3 325 records). Les parcs éoliens et les grandes centrales solaires au sol sont construits par des sociétés de projet (SPV) privées sur fonds propres : l'argent public n'entre pas par un marché de construction mais par le contrat de soutien en aval (OA/CR). Leur passation et leurs avenants échappent donc à la commande publique par nature, pas par contournement : c'est le trou de transparence structurel du secteur (à distinguer du cas où une SPV serait financée majoritairement par un pouvoir adjudicateur, qui l'assujettirait).
3. **Ce que le DECP capture bien** : les marchés publics de PV sur bâtiments publics (écoles, parkings, toitures) et les programmes des syndicats départementaux d'énergie (SDEM Morbihan 118 M€, SOREGIES). Ce segment est un terrain possible, mais il relève du petit PV en toiture, pas des parcs qui concentrent la rente (ceux des AO CRE / contrats OA).
4. **Implication méthodologique** : l'angle « gonflement des factures » ne peut PAS passer par le canal DECP pour les parcs privés. La cause structurelle exacte : dans les parcs, l'argent public entre par le contrat de soutien (OA/CR avec la CRE), pas par un marché de construction ; le développeur privé construit avec ses fonds, donc il n'y a par nature pas de commande publique à publier (le parallèle SESN n'est pas transposable : la SCSNE était elle-même un acheteur public). La formulation « SPV non assujetties » serait une simplification : une SPV créée pour un besoin d'intérêt général et financée majoritairement par un pouvoir adjudicateur (art. L. 1211-1 s. code de la commande publique) peut être soumise (les 3 concessions de travaux relevées en FCT-ena-002 le montrent). Les canaux alternatifs documentés dans le playbook : avis BOAMP/TED publiés volontairement par certains opérateurs, presse spécialisée, demandes d'accès directes (hors CADA pour les SPV privées), et les registres des coûts si la rec. n°1 CdC était un jour mise en oeuvre (verrou documenté 21-58/22-30/04-38).
5. **Réserve honnête** : le DECP consolidé ne couvre qu'une partie des acheteurs (data.gouv, pes, aws). Le constat d'absence vaut pour ce dataset ; il est corroboré par la structure de financement du secteur (construction sur fonds privés, soutien public en aval), pas seulement par le dataset.

## 4. IMPLICATIONS POUR LA STRATÉGIE (04-56)

1. **ANGLE A requalifié** : de « priorité 1, méthode DECP transposable » à « canal DECP invalidé pour les parcs privés, à redéployer sur le PV public de toiture + CADA travaux ».
2. **Le PV public de toiture devient un terrain viable** : SDEM Morbihan (118,2 M€), SOREGIES (21,9 M€) sont des acheteurs publics assujettis DECP, avec des programmes pluriannuels : on peut y chercher concentration, avenants, montants ronds. Premier candidat : les 6 marchés SDEM de construction de centrales PV > 100 kW.
3. **Les parcs privés** (le coeur de la rente : Puech del Vert, Barre, etc.) nécessitent : BOAMP/TED (si publiés), CADA marchés de travaux, presse locale, et la donnée de coûts qui n'existe pas (verrou rec. n°1).
4. **La découverte vaut aussi comme fait probatoire du fil central** : la construction des parcs éoliens est invisible dans les données publiques de la commande publique, exactement comme les coûts d'exploitation sont invisibles dans les données CRE (rec. n°1). Le trou de transparence n'est pas un accident de dataset : il découle de la structure de financement du secteur (construction sur fonds privés, soutien public en aval via des contrats OA/CR sans obligation de reporting des coûts).

## 5. PROCHAINES ÉTAPES ACTIONNABLES

1. **NEXT-A1** : dépouiller les 6 marchés SDEM Morbihan (118,2 M€) + les 8 marchés SOREGIES (21,9 M€) : objets, montants par lot, procédures, dates, concentration des titulaires (à reconstruire via RNE/INPI car champ DECP vide).
2. **NEXT-A2** : pour 1 parc privé identifié (ex. Puech del Vert/Barre), vérifier d'abord si la SPV est financée majoritairement par fonds publics (qualité d'organisme soumis à la CADA : art. L. 300-2 CRPA) ; si oui, demande CADA « marchés de travaux de construction » ; si non, demande d'accès directe à la SPV (hors champ CADA) ou canal des subventionneurs (DREAL, ADEME si subventions). Vérifier aussi les avis BOAMP/TED publiés volontairement.
3. **NEXT-A3** : documenter dans le playbook (12-38) le constat « DECP = vide pour les parcs privés ENR, cause : financement privé de la construction + soutien public en aval » comme route invalidée (gain de temps pour les prochains agents).

## 6. GAP ET LIMITES

- GAP-ena-1 : champ titulaires vide dans le DECP global : la concentration par titulaire n'est PAS calculable sans rapprochement RNE/INPI (le pilote SESN avait déjà noté cette limite). **Conséquence sur le verdict** : on a invalidé le canal (données absentes), pas l'hypothèse de fond (avenants/surfacturation sur parcs) : celle-ci reste NON TESTÉE (UNKNOWN), à poursuivre via les canaux alternatifs.
- GAP-ena-2 : les montants UGAP 1,25 Md€, Grasse 999 999 999 € et CA Saint-Louis 202,5 M€ sont des valeurs plafonds encodées (accords-cadres/concessions), pas des montants réels : exclus des agrégats ou lus comme valeurs maximales indicatives.
- Limite : extraction par mots-clés dans le champ objet uniquement (pas par code CPV ni par SIREN titulaire) : quelques marchés de construction de parcs sans mention explicite « éolien/solaire » dans l'objet peuvent échapper au filtre.

STATE          : FINAL
VERSION        : 1.0
CREATED        : 2026-08-11_05-00 CEST
HASH           : (consigné après mise à jour du RUN_MANIFEST)
