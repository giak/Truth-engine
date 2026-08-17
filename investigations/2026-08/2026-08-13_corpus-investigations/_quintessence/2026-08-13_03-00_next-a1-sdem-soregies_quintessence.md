# Quintessence : NEXT-A1, dépouillement des marchés SDEM Morbihan et SOREGIES Vienne (DECP)

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_run2-enr/2026-08-11_05-18_next-a1-sdem-soregies_INVESTIGATION.md` (62 lignes, 11 FCT-a1)
Date extraction : 2026-08-13 03:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot run2-enr)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format allégé, NEXT-A1 de l'ANGLE A (05-00)
- **Date source** : 2026-08-11 05:18 CEST, STATE FINAL
- **Identifiants source** : 11 FCT-a1-001 à 011
- **Object** : dépouiller les 6 marchés SDEM (118,2 M€) et 8 marchés SOREGIES (21,9 M€) identifiés par le filtre ENR, élargi aux 521 marchés DECP de ces deux acheteurs publics : concentration anormale ? candidatures uniques répétées ? avenants (gonflement) ?
- **Verdict source** : ni concentration anormale, ni offre unique sur le PV, ni avenants démontrables ; correction forensique majeure (461,8 M€ d'« avenants » = plafonds réencodés)

## 2. Faits atomiques préservés

- FCT-a1-001 : le DECP contient 300 marchés SDEM + 221 marchés SOREGIES = 521 [L19 (mesuré)]
- FCT-a1-002 : les montants des ACCORDS-CADRES MULTI-ATTRIBUTAIRES SDEM sont des PLAFONDS, pas des dépenses réelles (ex. 10 records PV « Lot 2 » à 56 M€ chacun avec 10 titulaires distincts, même objet) ; les marchés PONCTUELS (typiques de SOREGIES) portent des montants exécutés réels (Vivonne 4,57 M€ Bouygues E&S, modules PV SunPower 3,3 M€, batteries Entech 2 M€, VRD Colas 1,63 M€) [L20 (mesuré)]
- FCT-a1-003 : concentration SDEM par SIREN : aucun groupe dominant ; top 5 = Bouygues E&S 23 app (5,9 %), INEO 18 (4,6 %), RESO 17 (4,3 %), SPIE CityNetworks 16 (4,1 %), ARTELIA 16 (4,1 %) ; 106 groupes distincts sur 393 apparitions [L21 (mesuré)]
- FCT-a1-004 : concentration SOREGIES : pas de groupe dominant ; top = personnes physiques et petites structures (Décoularé-Delafontaine 10 app 3,7 %, Arigault 8, GREEN Poitou-Charentes 8) ; 148 groupes distincts sur 267 apparitions [L22 (mesuré)]
- FCT-a1-005 : offres uniques SDEM : 48/300 (16 %), total 17,1 M€, dont 6 PV (0,5 M€) ; leaders : INEO 9, Bouygues 6, RESO 4, SDEL 4, SPIE 4, Citéos 4 ; objets = maintenance/lots réseaux, pas les marchés PV de construction [L23 (mesuré)]
- FCT-a1-006 : offres uniques SOREGIES : 15/221, total 0,42 M€, objets annexes (assurances, fontaines, mobilier, serrurerie), 0 PV [L24 (mesuré)]
- FCT-a1-007 : croisement PV SDEM : 8 titulaires sur 10 présents à la fois sur Lot 1 (PV < 100 kW) et Lot 2 (PV > 100 kW) : EES-MB, Quenea ER, Photovolt, Emeraude Solaire, Cegelec, Bouygues E&S, Entech, Circuit Court Énergie (stabilité des attributaires) [L25 (mesuré)]
- FCT-a1-008 : modifications : 46 marchés SDEM avec modifications, 43 avec montant ; les montants publiés ne sont PAS des avenants unitaires : M2020-015 L3 (plafond initial 28 M€) porte 13 modifications dont les montants oscillent 30,2 → 33,08 → 31,2 M€ (retour sous le plafond initial), M2020-015 L4 (32 M€) 18 modifications [L26 (mesuré)]
- FCT-a1-009 : l'agrégat naïf « 461,8 M€ d'avenants » (signaux.py) est FAUX : somme de plafonds réencodés, à écarter [L27 (mesuré)]
- FCT-a1-010 : champs de concurrence : offresRecues renseigné pour 100 % des 521 marchés, dont 36 NC pour SDEM ; dateNotification renseigné pour 100 % [L28 (mesuré)]
- FCT-a1-011 : distribution des procédures : SDEM = 212 AO ouvert (70,7 %), 60 MAPA, 25 avec négociation, 3 SANS PUBLICITÉ NI MEC (SIG Morbihan Énergies 220 K€ x2, hydrogène 7,5 K€, titulaires CIRIL Group et HYGO, 1 offre chacun) ; SOREGIES = 109 négociation + 109 MAPA + 3 AO restreint (0 sans publicité) ; gros lots >= 1 MEUR : SDEM 96/108 en AO ouvert, SOREGIES 11/15 en négociation [L29 (mesuré)]

## 3. Acteurs nominaux

**Acheteurs publics** : SDEM Morbihan (255601106), SOREGIES (450889225), SIG Morbihan Énergies.
**Groupes attributaires** : Bouygues E&S, INEO, RESO, SPIE CityNetworks, ARTELIA, Cegelec, Entech, EES-MB, Quenea ER, Photovolt, Emeraude Solaire, Circuit Court Énergie, Décoularé-Delafontaine, Arigault, GREEN Poitou-Charentes, CIRIL Group, HYGO, Colas, SunPower.

## 4. Sources externes citées

data/decp-global.json (1 Go hashé), scripts data/extraire_sdem_soregies.py, data/analyse_sdem_soregies.py, data/matrice_concentration.py, data/concentration_siren.py, data/offres_modifications.py, data/signaux.py, data/verif_modifications.py, API recherche-entreprises.data.gouv.fr, CSV /tmp/enr_angle_a/sdem_soregies_detail.csv.

## 5. Chronologie datée

11/08/2026 05:18 : extraction des 521 marchés (300 SDEM + 221 SOREGIES), normalisation SIREN, mesures de concentration/offres/modifications, vérification forensique de la structure des modifications.

## 6. Mécanismes / chaînes causales

**M1 — La correction forensique des « avenants »** : les montants de modifications DECP sont des plafonds d'accord-cadre réencodés (oscillations autour du plafond initial) : ne jamais les agréger comme des avenants. Apport réutilisable (playbook 12-38). Niveau : L2. [L26-L27 (mesuré)]
**M2 — La limite structurelle du canal** : le DECP ne contient ni montants exécutés ni attributions par marché subséquent : la mesure du « vrai » gonflement est impossible dans ce canal (constat d'indétermination UNKNOWN, pas d'infirmation). Niveau : L2. [L31 (mesuré)]
**M3 — Les signaux de procédure sans signal de corruption** : 3 marchés SDEM sans publicité ni MEC, recours massif de SOREGIES à la négociation (109/221, dont 11/15 des gros lots) : réduit la publicité mais reste une procédure réglementée. Niveau : L1. [L29 (mesuré)]

## 7. Verbatim et citations

- « Les montants publiés ne sont PAS des avenants unitaires » (M2020-015 L3 : 30,2 → 33,08 → 31,2 M€) [L26 (mesuré)]
- « le DECP ne contient pas les montants exécutés. Constat d'indétermination (UNKNOWN), pas d'infirmation : la donnée nécessaire n'existe pas dans le canal » [L34 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : mesures exécutées par scripts sur le dataset complet (521 marchés), normalisation SIREN (leçon du pilote SESN : un même groupe sous plusieurs SIRET).
- **F-##** : 11/11 identifiants FCT-a1-001 à 011 préservés verbatim.
- **Méthode** : concentration par groupe, distribution des offres, offres uniques, modifications + vérification forensique (montant cumulé vs avenant unitaire).

## 9. Limites connues (case-limites)

- GAP-a1-1 : pas de montants exécutés ni d'attributions par marché subséquent (limite structurelle documentée) ; GAP-a1-2 : personnes physiques en tête SOREGIES non identifiées par fonction ; GAP-a1-3 : 36 marchés SDEM avec offresRecues = NC.
- Périmètre limité aux 2 acheteurs publics identifiés ; d'autres syndicats (SDE 24, SICAE) non dépouillés.
- Recommandation source : redéployer l'effort vers les parcs privés via CADA/marchés volontaires (NEXT-A2), seuls terrains où la donnée exécutée existe.
