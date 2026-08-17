# NEXT-A1 DE L'ANGLE A : DÉPOUILLEMENT DES MARCHÉS SDEM MORBIHAN ET SOREGIES VIENNE (DECP)

> Type : INVESTIGATION. Date : 2026-08-11 05:18 CEST.
> Objet : NEXT-A1 du document 05-00 (angle A). Dépouillement des 6 marchés SDEM (118,2 M€) et 8 marchés SOREGIES (21,9 M€) identifiés par le filtre ENR, élargi aux 521 marchés DECP de ces deux acheteurs publics.
> Contexte : le DECP est le seul canal public pour le PV de toiture/ombrières (les parcs privés en sont absents, 05-00). Question : y a-t-il concentration anormale, candidatures uniques répétées, ou avenants (gonflement) chez ces deux syndicats d'énergie ?
> Sources : `data/decp-global.json` (1 Go hashé), scripts `data/extraire_sdem_soregies.py`, `data/analyse_sdem_soregies.py`, `data/matrice_concentration.py`, `data/concentration_siren.py`, `data/offres_modifications.py`, `data/signaux.py`, `data/verif_modifications.py`, API recherche-entreprises.data.gouv.fr. CSV : /tmp/enr_angle_a/sdem_soregies_detail.csv.

## 1. MÉTHODE (EXÉCUTÉE)

1. Extraction de TOUS les marchés des acheteurs 255601106 (SDEM Morbihan) et 450889225 (SOREGIES) depuis le DECP global : 521 marchés au total (300 SDEM + 221 SOREGIES), un objet JSON par ligne, sources megalis/pes/AIFE_ATLINE.
2. Normalisation SIREN (9 premiers chiffres du SIRET) : leçon du pilote SESN, un même groupe apparaît sous plusieurs SIRET (Bouygues E&S sous 3 SIRET, SPIE CityNetworks et INEO sous 2).
3. Mesures : concentration par groupe (nb d'apparitions, part, somme des montants), distribution des offres reçues, offres uniques, modifications (avenants).
4. Vérification forensique de la structure des modifications (montant cumulé vs avenant unitaire).

## 2. FACT-CHECKS (FCT)

| FCT | Fait | Source | Verdict |
|-----|------|--------|---------|
| FCT-a1-001 | Le DECP contient 300 marchés SDEM + 221 marchés SOREGIES = 521 | Extraction decp-global.json | CONFIRMÉ |
| FCT-a1-002 | Les montants des ACCORDS-CADRES MULTI-ATTRIBUTAIRES SDEM sont des PLAFONDS, pas des dépenses réelles (ex. 10 records PV « Lot 2 » à 56 M€ chacun avec 10 titulaires distincts, même objet). Les marchés PONCTUELS (typiques de SOREGIES) portent des montants exécutés réels : centrales de Vivonne 4,57 M€ (Bouygues E&S), modules PV SunPower 3,3 M€, batteries Entech 2 M€, VRD Colas 1,63 M€ | Structure records + détail SOREGIES (05-00) | CONFIRMÉ (scindé par type de marché) |
| FCT-a1-003 | Concentration SDEM par SIREN : aucun groupe dominant. Top 5 = Bouygues E&S 23 app (5,9 %), INEO 18 (4,6 %), RESO 17 (4,3 %), SPIE CityNetworks 16 (4,1 %), ARTELIA 16 (4,1 %). 106 groupes distincts sur 393 apparitions | concentration_siren.py | CONFIRMÉ |
| FCT-a1-004 | Concentration SOREGIES : pas de groupe dominant non plus. Top = personnes physiques et petites structures (Décoularé-Delafontaine 10 app 3,7 %, Arigault 8, GREEN Poitou-Charentes 8). 148 groupes distincts sur 267 apparitions | concentration_siren.py | CONFIRMÉ |
| FCT-a1-005 | Offres uniques SDEM : 48/300 (16 %), total 17,1 M€, dont 6 PV (0,5 M€). Leaders des offres uniques : INEO 9, Bouygues 6, RESO 4, SDEL 4, SPIE 4, Citéos 4. Objets : maintenance/lots réseaux, pas les marchés PV de construction | signaux.py | CONFIRMÉ |
| FCT-a1-006 | Offres uniques SOREGIES : 15/221, total 0,42 M€, objets annexes (assurances, fontaines, mobilier, serrurerie), 0 PV | signaux.py | CONFIRMÉ |
| FCT-a1-007 | Croisement PV SDEM : 8 titulaires sur les 10 sont présents à la fois sur Lot 1 (PV < 100 kW) et Lot 2 (PV > 100 kW) : EES-MB, Quenea ER, Photovolt, Emeraude Solaire, Cegelec, Bouygues E&S, Entech, Circuit Court Énergie | matrice_concentration.py | CONFIRMÉ (stabilité des attributaires) |
| FCT-a1-008 | Modifications : 46 marchés SDEM ont des modifications, 43 avec montant. Les montants publiés ne sont PAS des avenants unitaires : M2020-015 L3 (plafond initial 28 M€) porte 13 modifications dont les montants oscillent 30,2 -> 33,08 -> 31,2 M€ (retour sous le plafond initial), M2020-015 L4 (32 M€) 18 modifications, mêmes oscillations | verif_modifications.py | INFÉRENCE (étayée par l'oscillation) : les montants sont des plafonds réencodés, la preuve directe (actes d'avenant) n'est pas lue |
| FCT-a1-009 | L'agrégat naïf « 461,8 M€ d'avenants » (signaux.py, somme des montants de modifications) est FAUX : somme de plafonds réencodés, à écarter | verif_modifications.py | CONTREDIT (corrigé) |
| FCT-a1-010 | Champs de concurrence présents : offresRecues renseigné pour 100 % des 521 marchés, dont 36 NC (non communiqué) pour SDEM ; dateNotification renseigné pour 100 % | stats_dates2.py | CONFIRMÉ (NC compté comme valeur) |
| FCT-a1-011 | Distribution des procédures : SDEM 300 marchés = 212 AO ouvert (70,7 %), 60 MAPA, 25 avec négociation, 3 SANS PUBLICITÉ NI MEC (SIG Morbihan Énergies 220 K€ x2, hydrogène 7,5 K€, titulaires CIRIL Group et HYGO, 1 offre chacun). SOREGIES 221 = 109 négociation + 109 MAPA + 3 AO restreint (0 sans publicité). Gros lots >= 1 MEUR : SDEM 96/108 en AO ouvert, SOREGIES 11/15 en négociation | procedures.py + sans_publicite.py | CONFIRMÉ |

## 3. VERDICT : NI CONCENTRATION ANORMALE, NI OFFRE UNIQUE SUR LE PV, NI AVENANTS DÉMONTRABLES

1. **Hypothèses testées** (angle A) : (a) concentration des titulaires chez les syndicats d'énergie publics ; (b) candidatures uniques répétées ; (c) avenants/gonflement des factures sur le PV public.
2. **Résultat (a)** : pas de concentration dominante. Le top 5 SDEM cumule ~23 % des apparitions réparties entre 5 groupes différents (aucun au-dessus de 5,9 %), et 106 groupes distincts coexistent. C'est un paysage multi-attributaire classique des accords-cadres de syndicat d'énergie. **Caveat de comparabilité** : ces 23 % sont une part d'APPARITIONS dans le DECP (un accord-cadre multi-attributaire compte chaque titulaire une fois par contrat, ce qui dilue la mesure), alors que les chiffres CRE (EDF 9 %, Neoen 8 %, Urbasolar 5 %, rapport 2026-01) sont des parts de PROJETS RETENUS en appels d'offres nationaux : les deux métriques ne sont pas directement comparables. Le verdict H0 tient néanmoins par l'absence de groupe dominant et le grand nombre de groupes distincts.
3. **Résultat (b)** : les 48 offres uniques SDEM (16 %) portent sur la maintenance, l'assurance, les lots réseaux en reconduction, pas sur les marchés de construction PV (qui affichent 9-13 offres). Aucun titulaire PV n'est en offre unique. Le signal « candidature unique répétée au bénéfice d'un même groupe » n'est PAS observé. Signal de procédure à noter (grille §6, sans être un signal de corruption) : 3 marchés SDEM passés sans publicité ni MEC (SIG 220 K€ x2, hydrogène 7,5 K€, 1 offre chacun) et 25 en procédure avec négociation ; SOREGIES recourt massivement à la négociation (109/221, dont 11/15 des gros lots >= 1 MEUR), ce qui réduit la publicité mais reste une procédure réglementée.
4. **Résultat (c)** : les modifications existent (46 marchés SDEM), mais les montants publiés dans le DECP sont des plafonds d'accord-cadre réencodés, non interprétables comme des avenants unitaires. Le gonflement des factures n'est PAS démontrable via ce dataset : le DECP ne contient pas les montants exécutés. Constat d'indétermination (UNKNOWN), pas d'infirmation : la donnée nécessaire n'existe pas dans le canal.
5. **Stabilité PV à noter** (pas un signal de corruption, mais un fait de structure) : les 8 mêmes groupes sur Lot 1 et Lot 2 PV (FCT-a1-007). Dans un accord-cadre multi-attributaire, c'est attendu (les candidats qualifiés sont les mêmes) ; ce n'est un signal que si les marchés subséquents étaient systématiquement attribués au même, ce que le DECP ne permet pas de vérifier (pas de suivi par marché subséquent dans ce dataset).

## 4. IMPLICATIONS POUR L'ANGLE A ET LA STRATÉGIE (04-56)

1. **Le PV public de toiture (SDEM/SOREGIES) ne produit pas de signal** à ce stade : la concentration est répartie, les offres sont plurinominées sur le PV, les avenants ne sont pas mesurables. L'angle A se heurte à la même limite que partout : **la donnée exécutée (montants réellement payés, marchés subséquents attribués) n'est pas dans le DECP**.
2. **Ce qui manque pour aller plus loin** : le suivi par marché subséquent (attribution réelle des 10 titulaires qualifiés sur chaque projet) et les montants exécutés. Canaux : rapports d'activité des syndicats (SDEM/SOREGIES publient leurs bilans), marchés subséquents via PLACE (si accessible), CADA ciblée sur les attributions de marchés subséquents PV.
3. **Le DECP reste un canal d'écrémage utile** : il a permis d'exclure proprement deux signaux (concentration, offre unique PV) chez les 2 plus gros acheteurs publics ENR, et de corriger un faux signal (461 M€ d'avenants = plafonds réencodés). Cette correction est un apport forensique du run : elle évite qu'un prochain agent n'agrège des plafonds comme des avenants.
4. **Recommandation** : ne pas poursuivre sur SDEM/SOREGIES sans nouvelle source ; redéployer l'effort de l'angle A vers le suivi des échéances datées (angle D de la stratégie) et les parcs privés via CADA/marchés volontaires (NEXT-A2), qui restent les seuls terrains où la donnée exécutée existe.

## 5. PROCHAINES ÉTAPES ACTIONNABLES

1. **NEXT-A2 (priorité)** : pour 1 parc privé (ex. Puech del Vert/Barre), vérifier la qualité CADA de la SPV (art. L. 300-2 CRPA) ou passer par la demande d'accès directe / canal DREAL-ADEME, et chercher les avis BOAMP/TED volontaires.
2. **NEXT-A4 (nouveau)** : ajouter au playbook 12-38 la leçon « montants de modifications DECP = plafonds réencodés, ne jamais agréger comme avenants » (correction forensique).
3. **NEXT-A5 (nouveau)** : archiver un point « canaux morts de l'angle A » (parcs privés : DECP vide ; PV public : données exécutées absentes) pour éviter la redondance.

## 6. GAP ET LIMITES

- GAP-a1-1 : le DECP ne contient ni les montants exécutés ni les attributions par marché subséquent : la mesure du « vrai » gonflement est impossible dans ce canal (limite structurelle, documentée).
- GAP-a1-2 : les personnes physiques en tête de la concentration SOREGIES (Décoularé-Delafontaine 10 app, Arigault 8) ne sont pas identifiées par fonction : à qualifier si l'on creuse SOREGIES (probablement maîtrise d'oeuvre ou contrôle, à vérifier).
- GAP-a1-3 : 36 marchés SDEM ont offresRecues = NC (non communiqué) : la distribution complète de la concurrence est partielle.
- Limite : le périmètre est limité aux deux acheteurs publics identifiés en 05-00 ; d'autres syndicats (SDE 24, SICAE, etc.) n'ont pas été dépouillés.

STATE          : FINAL
VERSION        : 1.0
CREATED        : 2026-08-11_05-18 CEST
HASH           : (consigné après mise à jour du RUN_MANIFEST)
