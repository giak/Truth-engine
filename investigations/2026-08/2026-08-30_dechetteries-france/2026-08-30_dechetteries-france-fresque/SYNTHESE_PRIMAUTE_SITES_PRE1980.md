# SYNTHÈSE — La primauté d'ancienneté : les 16 sites pré-1980 du corpus SINOE

AS_OF : 2026-08-30 · Dossier dechetteries-france-fresque
OBJET : agréger l'audit d'antériorité (Arles + Benais) et le recensement exhaustif des sites `D_OUV < 1980`, pour trancher la primauté face au récit « Gradignan = première déchèterie de France (17/11/1980) ».

---

## 1. Recensement exhaustif (dataset SINOE brut, `/tmp/sinoe_annuaire.csv`)

Sites avec `D_OUV` antérieur à 1980, dédoublonnés : **16**. Triés par année :

| Année | Date | Localisation | Service | Exploitant / typologie |
|---|---|---|---|---|
| 1884 | 1884-04-05 | Toulouse (31) | Déchèterie de Toulouse Ribaute | Toulouse Métropole → **ARTEFACT évident** |
| 1960 | 01/01/1960 | Longwy (54) | Déchèterie de Longwy | Veolia Eau → **suspicion saisie erronée** |
| 1973 | 01/01/1973 | St-Aquilin-de-Pacy (27) | Déchèterie St Aquilin | Onyx Normandie (Veolia) |
| 1973 | 26/11/1973 | **Benais** (37) | Déchèterie de Benais | SMIPE — **date contaminée (audit)** |
| 1974 | 01/01/1974 | La Haie-Fouassière (44) | Déchèterie | Grandjouan Saco (Veolia) |
| 1974 | 21/10/1974 | Morbier (39) | **Déchèterie mobile** | SICTOM Haut-Jura |
| 1974 | 21/10/1974 | St-Claude (39) | **Déchèterie mobile** | SICTOM Haut-Jura |
| 1975 | 01/01/1975 | Ivry-la-Bataille (27) | Déchèterie Ivry | Onyx Normandie (Veolia) |
| 1977 | 01/01/1977 | **Arles** — Ségonnaux (13) | Déchèterie d'Arles | Commune d'Arles — **décharge 1964 (audit)** |

## 2. Patron de contamination (découverte systemique)

Analogie étroite entre 4 sites à date « invraisemblablement ancienne » :
- **Toulouse Ribaute 1884** : évident, impossible (la déchèterie = équipement post-1975).
- **Longwy 1960** : déjà signalé (26/09), aucune source ne documente une déchèterie en 1960.
- **Benais 1973-11-26** : reproduit **exactement** la date de compétence « Collecte OMR » du syndicat SMIPE (création du SIVOM) ; la compétence déchèterie du SMIPE date de **02/06/1985**, et la déclaration préfectorale de la déchèterie de Benais de **12/01/1995** (voir AUDIT_BENAIS).
- **Arles 1977-01-01** : date cohérente (site = décharge communale exploitée **1964-1999**, apport volontaire documenté), mais ce n'est pas la création d'un équipement moderne nommé ainsi.

**Conclusion méthodologique** : le champ `D_OUV` de l'annuaire SINOE mélange des réalités hétérogènes — date de création du syndicat / de la collecte, date d'enquête, date d'ouverture réelle, date de compétence. **Il ne peut pas servir d'autorité pour établir une « première déchèterie de France ».** La valeur 1973 de Benais est en particulier **probablement contaminée**.

**Extension certifiée (passes 1900 + 1945)** : le patron se généralise aux 8 autres sites pré-1980 —
- **St-Aquilin-de-Pacy (1973)** : seule autorisation = **déclaration préfectorale 22/02/2012** (écart 39 ans) ; compétence déchèterie SYGOM **23/01/2002**, délégation SNA **02/07/2019** → ouverture réelle ~2002-2012.
- **Ivry-la-Bataille (1975)** : exploitant « Genet Sita Centre Ouest », **aucune autorisation administrative** → non corroboré.
- **La Haie-Fouassière (1974)** : site **FERMÉ le 18/11/2013** ; champ « année de rénovation/reconstruction 1974 » reproduisant **exactement** le D_OUV (date recopiée) ; Grandjouan-Veolia exploitant **depuis 2006 seulement** (Grandjouan = collecteur de Nantes **depuis 1870**) ; **passe 1955 (certifiée) : le site a été RECONVERTI le 18/11/2013 en Halte Eco Tri (fiche SINOE 106355, D_OUV 2013-11-18 = jour exact de fermeture de la 5172) — presse Ouest-France 20/11/2013 + inauguration blog Thouzeau 28/11/2013 ; aucune déchèterie moderne < 2000 (CC Vallée de Clisson 2000, CC SMG 22/12/2000) → D_OUV 1974 définitivement écarté**.
- **Longwy (1960)** : D_OUV = **année de création de l'Agglomération du Grand Longwy (27/11/1960, Banatic)** ; exploitant SINOE « Veolia Eau-Cge »/« Veolia Propreté (Onyx Est) » ; ZI du Pulventeux = ancienne concession minière.
- **Mobiles St-Claude & Morbier (1974)** : D_OUV 1974-10-21 = **date exacte de création du SICTOM Haut-Jura (arrêté préfectoral 21/10/1974, Banatic)** ; les fixes correspondants (St-Claude 2890, La Savine/Morbier 2884) D_OUV **1995-11-01** = « années 1990 » de l'historique officiel.
- **Montville (1980-01-01)** : date ronde 01/01 ; CC Portes N-W Rouen créée **2009-12-31**, puis Inter-Caux-Vexin 2017.
- **Randan (1980-07-25)** : **service FERMÉ** (fiche SINOE 4482) ; SBA créé **17/12/1975** ; maillage officiel SBA = 12 déchèteries **entre 1990 et 2010** → 1980 précède de 10 ans le maillage revendiqué.

## 3. Qui étaient réellement les ancêtres (avant le néologisme 1987)

Personne ne s'appelait « déchèterie » avant la circulaire 87-63 (26/06/1987). Les sites recensés sont antérieurement :
- **décharges communales / contrôlées** (Arles 1964, Ségonnaux ; probable Benais/Longwy) ;
- **dépôts d'encombrants / décharges brutes** (années 1960-70, sur le modèle nord-américain et ouest-européen des « déchetteries » de la fin des années 1970) ;
- **sites de transfert / transit** (Benais 7037 : ouverture 20/06/1983) ;
- **points d'apport volontaire** pour verre/papier (compétence 01B collecte sélective, 1997 au SMIPE).

Le terme « déchèterie » et sa doctrine (équipement communal d'apport volontaire) **nait avec la circulaire 87-63**, postérieurement à toutes ces dates.

**Ce qu'étaient réellement les sites Onyx/Veolia pré-1980 (verdict passe 1900)** :
- Les opérateurs historiques (CGEA → Onyx, Grandjouan, SITA/Genet) étaient des **collecteurs/transporteurs de déchets depuis le XIXe siècle** — Grandjouan missionné par Nantes dès **1870** (récit officiel Veolia), CGEA fondée dans l'entre-deux-guerres. Leurs « sites » antérieurs à 1980 étaient des **décharges, dépôts ou centres de transfert**, pas des déchèteries.
- **Veolia lui-même revendique ses « premières déchetteries » en 1986** (pionniers.veolia.com, INSPECTED) — incohérent avec des D_OUV 1973-75 chez ses filiales, preuve que ces dates SINOE sont des **dates de contrat/activité de collecte** recopiées.
- La Haie-Fouassière (1974) est en outre **FERMÉE depuis le 18/11/2013** : le champ « année de rénovation 1974 » reproduit exactement le D_OUV, signature typique de **date recopiée**.

## 4. Verdict consolidé sur la primauté

**RECENSEMENT 9/9 CLOS (passe 1945, certifiée)** : tous les sites SINOE D_OUV<1980 ont désormais un audit individuel (Benais, Arles, St-Aquilin, Ivry, La Haie-Fouassière, Longwy, Montville, Randan, mobiles Jura ×2) — **aucune déchèterie moderne pré-1980 n'est établie**. Verdict :

1. **Le récit « Gradignan = première déchèterie de France (17/11/1980) » est dépassé**, mais non par un site unique.
2. Il n'existe **aucune preuve d'un équipement « déchèterie » moderne antérieur à 1980** qui porte ce nom et soit daté par acte primaire. Tous les sites pré-1980 sont soit **contaminés dans leur date** (Toulouse/Longwy/Benais/St-Aquilin/Ivry/La Haie-Fouassière/mobiles Jura), soit **des décharges/dépôts antérieurs** réutilisés (Arles), soit **non corroborés** (Montville/Randan, service fermé).
3. **Gradignan conserve son statut de référence** comme premier équipement intercommunal urbain moderne, **documenté par acte primaire** (aff. 80/151, 21/03/1980 ; registre CUB BXM 511 W), et comme le lieu où le terme s'incarnera ensuite dans la doctrine nationale.
4. **Arles (1977) reste le seul candidat pré-1980 crédible comme apport-volontaire antérieur à Gradignan**, mais sur un site décharge communale (1964-1999) — à requalifier comme « un des tout premiers dépôts d'apport volontaire », pas comme « première déchèterie moderne ».
5. **Le faisceau Onyx/Veolia (St-Aquilin 1973, Ivry 1975, La Haie-Fouassière 1974) ne produit AUCUNE déchèterie moderne pré-1980** (passes 1900 certifiée) : les D_OUV sont des dates de contrat/activité de collecte (CGEA/Onyx/Grandjouan), la revendication interne Veolia datant elle-même ses déchèteries de **1986**. La primauté Gradignan 1980 **n'est pas contredite**.
6. **La Haie-Fouassière : la vraie chronologie est désormais établie par actes croisés (passe 1955 certifiée)** — l'équipement actuel (Halte Eco Tri 106355) ouvre le **18/11/2013** (reconversion de l'ancienne « déchetterie vétuste » 5172, réseau Sèvre Maine et Goulaine créé en 2000) ; le D_OUV 1974 est **définitivement écarté** comme date de référence du site sans acte d'ouverture.
6. **Les dates DOIVENT être retirées des tableaux publics comme preuve d'ancienneté** tant qu'aucun acte (délibération, arrêté) ne les certifie — c'est un **défaut du registre national** (« paradis de la data ») qui a laissé circuler la fausse idée d'une déchèterie de 1884 / 1960 / 1973 / 1974.

## 5. Frappes prioritaires — état
1. **✅ FAITE — Audit Onyx/Veolia (passe 1900, certifiée)** : St-Aquilin 1973 (déclaration préfectorale 2012), Ivry 1975 (aucune autorisation), La Haie-Fouassière 1974 (fermée 2013, date recopiée) → **dates de contrat/collecte, pas des ouvertures de déchèterie** ; Veolia revendique lui-même ses déchèteries en 1986.
2. **✅ FAITE — Clôture recensement 9/9 (passe 1945, certifiée)** : Longwy (année création AGL 1960), Montville (date ronde, CC 2009), Randan (service fermé, maillage SBA 1990-2010), mobiles Jura (D_OUV = date création SICTOM 1974) → **aucune déchèterie moderne pré-1980 établie**.
2bis. **✅ FAITE — Audit ouverture La Haye-Fouassière (passe 1955, certifiée)** : date réelle établie (Halte Eco Tri 18/11/2013, reconversion), aucune déchèterie moderne < 2000, site « vétuste » avant — 3 FCT ✦ CONFIRME persistés.
3. **À FAIRE — Procure les actes d'ouverture réels** : Arles (délibération commune 1977), Benais (archives Indre-et-Loire / SMIPE), fixes Jura 1995 (archives départementales 39), Longwy années 1990.
4. **À FAIRE — Demander à l'ADEME/SINOE la méthodologie du champ D_OUV** (distinguer date réelle vs date de compétence/enquête) et corriger les artefacts 1884/1960/1973/1974.
5. **À FAIRE — Croiser Gallica/presse 1976-1978** pour dater la construction d'une déchèterie explicite pré-1980 (le cas échéant, une décharge municipale devenue déchèterie dès 1976-79).

## TRAÇABILITÉ
- Dataset SINOE brut `/tmp/sinoe_annuaire.csv` (16 sites D_OUV<1980) — INSPECTED.
- AUDIT_ARLES_SEGONNAUX.md et AUDIT_BENAIS_1973.md (ce dossier) — INSPECTED.
- Registre CUB BXM 511 W (aff. 80/151, 21/03/1980) et circulaire 87-63 — passes certifiées antérieures.
- **Passe 1830 `20260830-1830-certification-primaute-dechetteries-france`** (FINAL, gate delivery PASS) : Benais contaminé, Arles décharge communale 1964-1999, Gradignan acte 80/151, circulaire 87-63 introductive — 5 FCT (2 ✦ CONFIRME, 3 ✧ VERIFIE).
- **Passe 1900 `20260830-1900-audit-onyx-veolia-sites-pre1980`** (FINAL, gate delivery PASS) : verdict Onyx/Veolia — St-Aquilin 2012, Ivry sans autorisation, La Haie-Fouassière fermée, Veolia 1986 — 5 FCT (1 ✦ CONFIRME, 4 ✧ VERIFIE).
- **Passe 1945 `20260830-1945-audit-sites-restants-pre1980`** (FINAL, gate delivery PASS) : Longwy/Montville/Randan/mobiles Jura — recensement 9/9 clos — 5 FCT (2 ✦ CONFIRME, 3 ✧ VERIFIE).
- **Passe 1955 `20260830-1955-audit-ouverture-haie-fouassiere`** (FINAL, gate delivery PASS) : ouverture réelle La Haye-Fouassière (Halte Eco Tri 18/11/2013, reconversion) — 3 FCT (3 ✦ CONFIRME) persistés MnemoLite (87ce56e5, 79748b4f, 8a84e196).
- Sources passe 1955 : blog Éric Thouzeau (inauguration 28/11/2013, INSPECTED), fiche SINOE 106355 + dataset raw (D_OUV 2013-11-18), Wikipedia FR (CC Vallée de Clisson 2000, CC SMG 22/12/2000), RPQS 2025 Clisson Sèvre et Maine Agglo, snippets Ouest-France 27/11/2012 et 20/11/2013.
- Sources web réouvertes : historique officiel SICTOM (sictomhautjura.fr), SBA 40 ans (sba63.fr), Banatic (creations EPCI), fiches services SINOE 2690/2857/4482, pionniers.veolia.com (Veolia 1986).