# ANNEXE DATA — Recensement réel du parc (SINOE annuaire)

SOURCE : `data.ademe.fr/data-fair/api/v1/datasets/sinoe-(r)-annuaire-des-decheteries-dma/raw` (CSV 24 Mo)
Récupéré : 2026-08-30 · champs : C_REGION..GPS_LAT (35 cols) · dél séparateur `;` · UTF-8 BOM
Méthode : téléchargement direct (curl -L) + analyse numpy/csv ; déduction du site ouvert = présence d'un record au dernier millésime (>=2025) par C_SERVICE.

## 1. Chiffres clés

| Métrique | Valeur |
|---|---|
| Enregistrements (records par année × service) | **45 169** |
| Services distincts (C_SERVICE) | **5 217** |
| **Sites ouverts au dernier millésime (>=2025)** | **4 635** |
| Enquêtes dans l'annuaire | 2009, ’11, ’13, ’15, ’17, ’19, ’21, ’23, ’25, ’26 (bisannuelle impaire, +2009) |

## 2. Sites ouverts par région (dernier millésime)

| Région | Sites | | Région | Sites |
|---|---|---|---|---|
| Nouvelle-Aquitaine | 613 | | Bretagne | 282 |
| Auvergne-Rhône-Alpes | 612 | | Normandie | 262 |
| Occitanie | 559 | | Centre-Val de Loire | 255 |
| Grand Est | 462 | | Île-de-France | 208 |
| Pays de la Loire | 328 | | DROM-COM | 104 |
| Bourgogne-Franche-Comté | 321 | | Corse | 30 |
| Provence-Alpes-Côte d'Azur | 302 | | Hauts-de-France | 297 |

**Ordre de grandeur réseau : ~4 600-4 700 sites ouverts** (référence chiffrée réelle, vs « ~4 000 » cité en presse). 45 169 enregistrements = série pluriannuelle, PAS le nombre de sites.

## 3. Distribution des dates d'ouverture (tous services, dernier record) — courbe du réseau

| Année | Sites | Année | Sites |
|---|---|---|---|
| 1977 | 1 | 1990 | 61 |
| 1980 | 2 | 1991 | 93 |
| 1981 | 4 | 1992 | 156 |
| 1982 | 5 | 1993 | 175 |
| 1983 | 5 | 1994 | 224 |
| 1984 | 4 | 1995 | 227 |
| 1985 | 8 | 1996 | 260 |
| 1986 | 23 | 1997 | 275 |
| 1987 | 7 | 1998 | 277 |
| 1988 | 34 | 1999 | 310 |
| 1989 | 35 | 2000 | 336 |
| | | 2001 | 450 (**pic**) |

➤ Pic de création : **1994-2001** (déploiement massif post-TRIVAC 1993 et réglementation déchets 1992). Croissance lente 1977-1989 (pionniers), explosion 1990-2001, tassement après 2010 (nécessité/renouvellement site). **Ceci corrobore quantitativement la chaîne Gradignan 1980 → réseau 1990-2009.**

## 4. ⚠ DÉCOUVERTE DATA — Gradignan = 1981 dans SINOE (pas 1980)

Parc CUB/gironde (C_SERVICE, SINOE) :
- **Déchèterie de Gradignan : D_OUV = 1981-01-01** (ouverte, OUI)
- Bruges 1988-02-01 · Bassens 1983-06-01 · Villenave-d'Ornon 1982-08-01 · Pessac-Beutre 1983-01-01 (fermée) · Bordeaux (Deschamps-Bastide) 1989-11-01 · Saint-Caprais 2000-07-06 · Pessac (Gutenberg) 2008-12-01 · Bordeaux (Surcouf) 2009-06-01 · Pessac (Bourgailh) 2012-10-29 · Bordeaux (Carle Vernet) 2023-10-01.

**Contradiction latente (FAISCEAU B renforcé)** : la revendication officielle « ouverte le **17/11/1980** » (panneau + actualité Archives BM, même famille) est confrontée à un **chiffrage autonome SINOE D_OUV = 1981**. Pas de séance plénière CUB au 17/11/1980 (registre W74 : 17/10, 21/11, 19/12). Trois dates en jeu : acte 21/03/1980 (registre), SINOE 1981, revendication 17/11/1980. À discriminer.

## 5. ⚠ DÉCOUVERTE — sites FIXES déclarés ANTÉRIEURS à 1980 (perturbateurs du « première de France »)

| D_OUV | Nom | Ville | Dép. | Ouvert aujourd'hui |
|---|---|---|---|---|
| **1960-01-01** | Déchèterie de Longwy | Longwy | 54 | OUI ⚠ outlier probable (erreur ou aire de dépôt historique) |
| **1973-01-01** | Déchèterie Saint-Aquilin-de-Pacy | St-Aquilin-de-Pacy | 27 | OUI |
| **1973-11-26** | Déchèterie de Benais | BENAIS | 37 | OUI |
| 1975-01-01 | Déchèterie Ivry-la-Bataille | Ivry-la-Bataille | 27 | OUI |
| 1977-01-01 | Déchèterie d'Arles Ségonnaux | Arles | 13 | OUI |
| 1980 | Montville / Randan | 76 / 63 | | OUI |

(+ 2 déchèteries mobiles déclarées 1974 : Saint-Claude & Morbier, Jura)

**Interprétation prudente (PAS de conclusion hâtive) :** ces D_OUV sont **autodéclarés par les collectivités** dans SINOE et peuvent refléter une **date de création du site/équipement** ou une **rétro-datation** (« on existe depuis toujours »). Ils concurrencent néanmoins la primauté revendiquée de Gradignan. Longwy 1960 est un outlier « trop tôt » suspect (à contrôler — éventuel ancien dépôt/encombrants). Ne pas dire « Longwy première » sans vérification (DISCIPLINE : sans source d'ouverture nominale, rester OPEN).

## 6. Opacité des données (angle « paradis de la data »)

- Champs **`LST_TYPE_DECHET` (flux acceptés) : 0 site renseigné** sur les 4 635 ouverts — le cœur descriptif (quels déchets acceptés) est **vide dans l'annuaire public** (données non publiées / reporters ne renseignent pas). Fissure d'exhaustivité.
- `GPS_QUALITY` : 4 246 sites qualifiés '1' ; 53 à '-1' ; 348 avec valeur aberrante/flottante → géolocalisation non homogène.
- Aucun site sans GPS (lat/long présents partout) mais précision hétérogène.
- Pas de champ coût/financement/éco-organisme dans l'annuaire (données hors périmètre annuaire public).

## 7. Traçabilité
- CSV source conservé : `/tmp/sinoe_annuaire.csv` · 45 169 enr · licence ouverte.
- Analyses : scripts python ad hoc (bucketing par ANNEE/C_SERVICE/D_OUV), pas de package ajouté.
- Interprétations marquées ⚠/OPEN quand non vérifiées niveau source nominative.

> Statut : soit intégré dans une future passe KERNEL certification (nouveau RUN), soit enrichi au besoin immédiat. Chiffre « 4 635 sites ouverts » = résultat analytique direct de l'annuaire, non encore passé par les gates KERNEL.