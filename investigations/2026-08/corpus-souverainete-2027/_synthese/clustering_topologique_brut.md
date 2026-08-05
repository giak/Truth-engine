# Clustering topologique exhaustif : matrice acteur/concept x fiche (2026-08)

Date : 2026-08-05 | Heure : 03:00 CEST | Methode : grep -ci sur 22 quintessences (A-V) | Seuil nominal : max(4, ceil(22/10)) = 4 (regime N>=10)

---

## 1. Cartographie des fiches

| Code | Fiche | Type | Faits | Date |
|------|-------|------|-------|------|
| A | mythe_souverainiste | APEX | 14 (F-INT) | 15-15 |
| B | rassemblement_souverainiste_ric | APEX | 20 (F-RIC) | 15-20 |
| C | dilution_pretendants_2027 | APEX | 20 (F-DIL) | 15-25 |
| D | faisceau_neutralisation_souverainete | APEX | 22 (F-FAI) | 15-30 |
| E | reseau_er_bollore_lhg | APEX | 18 (F-RES) | 15-29 |
| F | comparaison_democratie_directe | SIMPLE | 13 (F-INT) | 15-45 |
| G | souverainistes_opposition_controlee | APEX | 20 (F-OPP) | 15-50 |
| H | atlas_souverainistes_2027 | COMPLEX | 22 (F-ATLAS) | 15-55 |
| I | souverainistes_angles_morts | SIMPLE | 17 (F-AM) | 16-55 |
| J | chouard_ric_theoricien | SIMPLE | 10 (F-CHO) | 17-10 |
| K | gilets_jaunes_figures_2027 | SIMPLE | 12 (F-GJ) | 17-12 |
| L | poulin_presidinde_2027 | SIMPLE | 8 (F-POU) | 17-15 |
| M | think_tanks_medias_souverainistes | APEX | 29 (F-TT) | 18-00 |
| N | lassalle_souverainisme_girondin | APEX | 20 (F-LAS) | 18-30 |
| O | pochon_ric_parlementaire | APEX | 10 (F-POC) | 19-30 |
| P | marechal_identite_libertes | APEX | 13 (F-MAR) | 19-35 |
| Q | chouard_reseau_influence | APEX | 14 (F-CHO2) | 19-40 |
| R | bollore_influence_editoriale_niveau3 | APEX | 20 (F-BOL3) | 20-10 |
| S | temps_antenne_souverainistes_gap | SIMPLE | 15 (F-GAP) | 20-50 |
| T | arcom_2022_temps_parole_souverainistes | APEX | 27 (F-AR2) | 21-35 |
| U | censure_algorithmique_souverainistes | SIMPLE | 31 (F-SHB) | 23-30 |
| V | ric_verrou_historique | APEX | 25 (F-RIC2) | 23-55 |

---

## 2. Matrice acteurs individuels x 22 fiches

Presence binaire (>=1 occurrence grep -ci). 1 = present, 0 = absent.
Recalcul complet sur 22 fiches (A-V). Deltas /20 → /22 documentes en §2.2.

### 2.1 Acteurs eligibles (>=4/22) : 28 entites (23 acteurs + 5 concepts)

| Acteur | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | **Fiches** |
|-----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|----------|
| RIC* | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | **20** |
| Frexit/sortie UE* | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | **15** |
| Asselineau | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | **14** |
| CNews | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | **13** |
| ENA* | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | **10** |
| Bollore | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | **11** |
| RIP* | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | **11** |
| Philippot | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | **10** |
| 500 parrainages* | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **9** |
| Dupont-Aignan | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | **9** |
| Arcom | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | **8** |
| Chouard | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | **7** |
| Lassalle | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | **7** |
| Conseil constit. | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **7** |
| Zemmour | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | **7** |
| Le Pen/RN | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | **7** |
| Sud Radio | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | **7** |
| Kuzmanovic | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **6** |
| Pochon | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | **6** |
| Lagardere | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **5** |
| 83 % (RIC 2017)* | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **5** |
| Villiers | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| TV Libertes | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| Bardella | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| opposition controlee* | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| Melenchon | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| Branco | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| Soral/E&R | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **4** |
| Marechal | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |

\* Concepts transversaux, pas des acteurs.

### 2.2 Deltas /20 → /22

| Acteur | /20 | /22 | Delta | Explication |
|--------|-----|-----|-------|-------------|
| RIP | 8 | 11 | **+3** | U (censure: RIP mentionne comme cadre legal) et V (RIC verrou: RIP art. 11 modifie) |
| Chouard | 5 | 7 | **+2** | U (censure: shadowban YouTube) et V (RIC verrou: theoricien cite) |
| Dupont-Aignan | 7 | 9 | **+2** | U (censure: mentionne comme figure) et N etait deja compte, correction : +1 en U |
| RIC | 18 | 20 | **+2** | U et V, tous deux mentionnent le RIC |
| Asselineau | 13 | 14 | **+1** | U (censure: figure citee), V ne le mentionne pas |
| CNews | 12 | 13 | **+1** | U (censure: citee comme chaine analysee) |
| Philippot | 9 | 10 | **+1** | U (censure: figure citee) |
| Arcom | 7 | 8 | **+1** | U (censure: DSA/Arcom) |
| Conseil const. | 6 | 7 | **+1** | V (RIC verrou: verrou institutionnel) |
| Sud Radio | 6 | 7 | **+1** | Correction (Q etait compte a 6, reste a 7: A,G,H,J,Q,T) |
| Lassalle | 6 | 7 | **+1** | U (censure: figure citee) |
| Pochon | 5 | 6 | **+1** | V (RIC verrou: PPL citees) |
| 83 % | 4 | 5 | **+1** | V (RIC verrou: sondage IFOP 2017) |
| Frexit | 14 | 15 | **+1** | U (censure: mentionne en contexte souverainiste) |

Stables (delta 0) : ENA(10), Bollore(11), 500 parrainages(9), Zemmour(7), Le Pen(7), Kuzmanovic(6), Lagardere(5), Villiers(4), TV Libertes(4), Bardella(4), opposition controlee(4), Melenchon(4), Branco(4), Soral(4), Marechal(4).

### 2.3 Nouveaux acteurs introduits par U et V (sous le seuil, 1-3/22)

| Acteur | Fiches | Note |
|--------|--------|------|
| DSA | U | Censure algorithmique : cadre legal europeen |
| shadowban | U | Censure algorithmique : mecanisme documente |
| YouTube | U | Plateforme analysee |
| Twitter/X | U | Plateforme analysee |
| Viginum | U | Organe de censure numerique francais |
| Suisse | B, F, V | Droit compare RIC (etait a 2/20, passe a 3/22) |
| Baviere | V | Droit compare RIC |
| Taïwan | V | Droit compare RIC |
| Macron | D, U | Deja present mais isole (1→2/22) |

### 2.4 Acteurs exclus (2-3/22)

Onfray(3), Ludosky(3), d'Escufon(3), CNCCFP(3), Latouche(3), pouvoir au peuple(3), Egger(2), Knafo(2), Retailleau(2), Ciotti(2), Sterin(2), Ruffin(2), Villepin(2), Le Gallou(2), Grimal(2), Mouraud(2), Drouet(2), Nicolle(2), Poulin(2), Glucksmann(2), 49.3(2), Espoir RIC(2), Frontieres(2), remigration(2), Suisse(3)

### 2.5 Acteurs isoles (1/22)

Cheminade(H), Macron(D,U), Charaudeau(D), Italie(F), Puy du Fou(G), Attal(C), Fayard(H), Lalanne(A), Conversano(I), GRECE/de Benoist(I), La Cocarde(I), Les Ruches(I), GP-TV(G), Messiha(H), Jean-Christophe Bollore(M), Rerolle(M), Berruyer(M), Genevard(M), Zimmern(M), Laarman(M), Schraen(N), Bayrou(N), Elucid(I), Contribuables Associes(M), Sellner(I), DSA(U), shadowban(U), YouTube(U), Twitter(U), Viginum(U), Baviere(V), Taïwan(V)

---

## 3. Clusters topologiques nominaux (seuil = 4 fiches)

**Regle** : ensemble de >=2 acteurs eligibles (>=4/22) co-occurrents dans >=4 fiches identiques.

### 3.1 Clusters d'acteurs

**C1 : Asselineau + Kuzmanovic** : 6 fiches (A, B, C, D, G, H)
Co-occurrence parfaite. Ces deux acteurs apparaissent dans exactement les memes 6 fiches. STABLE depuis /20 : les nouvelles fiches (U,V) ne mentionnent pas Kuzmanovic. Asselineau est a 14/22, Kuzmanovic fige a 6/22. La co-occurrence est un artefact du corpus originel (A-H).

**C2 : Asselineau + Philippot + Dupont-Aignan** : 9 fiches (A, B, G, H, N, R, S, T, U)
Le trio souverainistes historiques. PROGRESSION MAJEURE depuis /20 : passe de 4 a 9 fiches. Les fiches N (lassalle), R (bollore_niveau3), S (gap ARCOM), T (arcom_2022) et U (censure) contiennent toutes les trois figures. Note : P (marechal) a Asselineau mais pas Philippot/Dupont-Aignan. O (pochon) n'a qu'Asselineau.

**C3 : Bollore + CNews + TV Libertes** : 4 fiches (A, D, E, H)
L'empire mediatique conservateur. STABLE. Bollore(11), CNews(13), TV Libertes(4) est le facteur limitant.

**C4 : Bollore + Lagardere + Arcom** : 4 fiches (A, D, E, G)
Le duo de magnats + regulateur. STABLE. Lagardere(5) est le facteur limitant.

**C5 : Le Pen/RN + Bardella** : 4 fiches (A, B, C, H)
Le duo RN. STABLE. Bardella(4) est le facteur limitant.

**C6 : Zemmour + Conseil constitutionnel** : 4 fiches (C, D, G, H)
STABLE. Conseil constitutionnel gagne +1 (V) mais Zemmour ne la mentionne pas.

**C7 : CNews + Conseil constitutionnel** : 5 fiches (C, D, G, H, I)
PROGRESSION : +1 fiche (I: angles_morts). Les deux apparaissent dans C,D,G,H,I.

**C8 : Asselineau + Lassalle** : 7 fiches (N, O, Q, R, S, T, U)
PROGRESSION : +1 fiche (U: censure). Artefact d'elargissement du corpus : toute enquete sur une figure ou un mecanisme du champ mentionne Asselineau ET Lassalle comme points de comparaison. F-LAS-12 documente l'absence d'alliance entre eux.

**C9 (NOUVEAU) : Asselineau + Philippot + Chouard** : 5 fiches (G, H, O, Q, U)
Cluster emergent via U (censure). Les trois sont co-occurrents dans G (opposition controlee), H (atlas), O (pochon), Q (chouard2), U (censure). Reflete l'intersection des figures souverainistes Frexit avec le theoricien du RIC dans les fiches thematiques.

**C10 (NOUVEAU) : RIP + Conseil constitutionnel** : 4 fiches (C, D, I, V)
Cluster emergent via V (RIC verrou). Les deux concepts institutionnels co-occurrent dans C (dilution: parrainages), D (faisceau: neutralisation), I (angles_morts), V (RIC verrou: cadre constitutionnel).

### 3.2 Clusters de concepts

**C-CON1 : RIC + ENA** : 9 fiches (A, B, C, D, E, F, G, H, I)
Les deux concepts les plus transversaux du corpus originel A-I. STABLE. RIC(20), ENA(10). Les nouvelles fiches (J-V) elargissent RIC (+6) mais pas ENA (qui reste fige a 10).

**C-CON2 : Frexit + 500 parrainages** : 6 fiches (A, B, C, D, H, N)
STABLE. Frexit gagne +1 (U), 500 parrainages stable. Le cluster ne gagne pas de nouvelle fiche (U n'a pas 500 parrainages, N deja compte).

**C-CON3 : RIC + Frexit + 500 parrainages** : 5 fiches (A, B, C, D, H)
Le triptyque souverainiste procedural. STABLE. Note : U contient RIC + Frexit mais pas 500 parrainages. V contient RIC mais pas Frexit ni 500 parrainages.

**C-CON4 (NOUVEAU) : RIP + RIC** : 9 fiches (A, B, C, D, F, I, L, U, V)
Cluster conceptuel emergent. RIP(11) et RIC(20) sont les deux concepts institutionnels les plus transversaux. Leur co-occurrence dans U (censure: RIP comme cadre legal, RIC comme revendication) et V (RIC verrou: RIP art. 11) renforce le cluster.

### 3.3 M-themes (mecanismes, seuil >=4)

| # | M-theme | Fiches /20 | Fiches /22 | Nb /22 |
|---|---------|-----------|------------|--------|
| M1 | Bollore/medias/concentration | A, D, E, G, H, O, R | A, D, E, G, H, O, R | **7** |
| M2 | Fragmentation/auto-neutralisation | A, B, C, G | A, B, C, G | **4** |

M1 stable. M2 stable. U et V n'enrichissent pas les M-themes au seuil nominal.

M-themes sous le seuil :
- M3 (verrou electoral/500 parrainages) : 3 fiches (B, C, D)
- M4 (RIC/captation institutionnelle) : 3 fiches (B, D, G)
- M6 (invisibilisation structurelle ARCOM) : 3 fiches (S, T, U) — PROGRESSION (+1 via U: censure algorithmique)
- M7 (censure algorithmique/shadowban) : 1 fiche (U) — NOUVEAU, emerge de la fiche U
- M8 (verrou historique RIC) : 1 fiche (V) — NOUVEAU, emerge de la fiche V

---

## 4. Classement complet par etendue

### 4.1 Acteurs eligibles (>=4/22) : 28 entites

| Rang | Acteur | /22 | /20 | Delta |
|------|--------|-----|-----|-------|
| 1 | RIC* | 20 | 18 | +2 |
| 2 | Frexit* | 15 | 14 | +1 |
| 3 | Asselineau | 14 | 13 | +1 |
| 4 | CNews | 13 | 12 | +1 |
| 5 | Bollore | 11 | 11 | 0 |
| 6 | RIP* | 11 | 8 | **+3** |
| 7 | ENA* | 10 | 10 | 0 |
| 8 | Philippot | 10 | 9 | +1 |
| 9 | 500 parrainages* | 9 | 9 | 0 |
| 10 | Dupont-Aignan | 9 | 7 | **+2** |
| 11 | Arcom | 8 | 7 | +1 |
| 12 | Chouard | 7 | 5 | **+2** |
| 13 | Lassalle | 7 | 6 | +1 |
| 14 | Conseil constitutionnel | 7 | 6 | +1 |
| 15 | Zemmour | 7 | 7 | 0 |
| 16 | Le Pen/RN | 7 | 7 | 0 |
| 17 | Sud Radio | 7 | 6 | +1 |
| 18 | Kuzmanovic | 6 | 6 | 0 |
| 19 | Pochon | 6 | 5 | +1 |
| 20 | Lagardere | 5 | 5 | 0 |
| 21 | 83 %* | 5 | 4 | +1 |
| 22 | Villiers | 4 | 4 | 0 |
| 23 | TV Libertes | 4 | 4 | 0 |
| 24 | Bardella | 4 | 4 | 0 |
| 25 | opposition controlee* | 4 | 4 | 0 |
| 26 | Melenchon | 4 | 4 | 0 |
| 27 | Branco | 4 | 4 | 0 |
| 28 | Soral/E&R | 4 | 4 | 0 |
| 29 | Marechal | 4 | 4 | 0 |

\* Concepts transversaux, pas des acteurs.

### 4.2 Top 5 des plus fortes progressions /20 → /22

| Acteur | /20 | /22 | Delta | Explication |
|--------|-----|-----|-------|-------------|
| RIP | 8 | 11 | **+3** | U (cadre legal censure) + V (art. 11 modifie) |
| Chouard | 5 | 7 | **+2** | U (YouTube shadowban) + V (theoricien cite) |
| Dupont-Aignan | 7 | 9 | **+2** | U (censure: figure citee) + correction N |
| RIC | 18 | 20 | **+2** | U + V |
| Asselineau | 13 | 14 | +1 | U (censure: figure citee) |

---

## 5. Ce que le clustering topologique dit reellement

### Constats mathematiques (sans interpretation)

1. **RIC = connecteur quasi-universel** (20/22). Absent uniquement de R (bollore niveau 3, focus editorial) et S (gap ARCOM, focus methodologique). RIP(11) et Frexit(15) suivent.

2. **RIP = progression la plus spectaculaire** (8→11, +3). U et V ont considerablement renforce la presence du RIP dans le corpus. Le RIP est desormais le 6e concept le plus present (egalite avec Bollore a 11).

3. **C2 (Asselineau+Philippot+Dupont-Aignan) explose de 4→9 fiches.** Les fiches N,R,S,T,U contiennent systematiquement les trois figures. Ce n'est plus un cluster fragile : c'est le cluster d'acteurs le plus dense du corpus apres C-CON1.

4. **C9 (Asselineau+Philippot+Chouard, 5 fiches) emerge.** L'intersection des figures Frexit avec le theoricien du RIC, via les fiches thematiques (G,H,O,Q,U).

5. **C10 (RIP+Conseil constitutionnel, 4 fiches) emerge.** Le duo institutionnel du verrouillage du RIC : le RIP comme mecanisme, le Conseil constitutionnel comme gardien.

6. **Asselineau reste l'acteur le plus mentionne** (14/22). Son omnipresence est en partie un biais d'enquete (point de comparaison systematique).

7. **Kuzmanovic fige a 6/22.** Aucune nouvelle fiche ne le mentionne. C1 (co-occurrence parfaite avec Asselineau) est un artefact fossilise du corpus originel.

8. **M6 (invisibilisation ARCOM) progresse a 3/22** (+U). Encore sous le seuil nominal (4/22) mais qualitativement majeur.

9. **M7 (censure algorithmique) et M8 (verrou historique RIC) emergent** a 1/22 chacun. Nouveaux M-themes non encore clusters.

### Ce que le clustering ne peut PAS dire

1. **Causalite.** Co-occurrence documentaire != lien reel.
2. **Exhaustivite du champ.** La matrice reflete les choix editoriaux, pas la realite.
3. **Ponderation.** 1 mention = 44 mentions en binaire.
4. **Meta-fiche D.** D agree A+B+C, double-compte les co-occurrences.
5. **N=22.** Seuil nominal (4) est conservateur. Onfray(3), Ludosky(3), d'Escufon(3) meritent attention.
6. **Artefact Asselineau.** Sa presence dans 14/22 fiches est en partie un biais d'enquete.

---

## 6. References croisees

- **Heatmap ASCII** : `_synthese/heatmap_ascii.md` (visualisation complete 29x22, a jour)
- **Rapport Phase 2** : `_synthese/rapport_synthese_phase2.md` (9 H2 canoniques, 5 theses, CP1=OUI, N=22)
- **REGISTRE** : `../REGISTRE.md` (22 enquetes, 22 quintessences, ~500 faits)
