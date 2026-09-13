# 🦊 Passe KERNEL — Audit des 5 derniers sites SINOE pré-1980 (clôture du recensement 9/9)

**Run `20260830-1945-audit-sites-restants-pre1980`** · parent `20260830-1900-audit-onyx-veolia-sites-pre1980` · INPUT_KIND=UPDATE · MISSION_MODE=INVESTIGATION · AS_OF 2026-08-30

## Sujet

Les 9 sites SINOE avec D_OUV<1980 du recensement P0 : après les audits individuels de Benais (1830), Arles (1830), St-Aquilin/Ivry/La Haie-Fouassière (1900), il restait **5 sites non audités individuellement** :

1. **Longwy (54)** — fiche 2690 — D_OUV 1960-01-01 (outlier « trop tôt »)
2. **Montville (76)** — fiche 2857 — D_OUV 1980-01-01 (date ronde)
3. **Randan (63)** — fiche 4482 — D_OUV 1980-07-25 (date précise)
4. **Déchèterie mobile de Saint-Claude (39)** — fiche 8983 — D_OUV 1974-10-21
5. **Déchèterie mobile de Morbier (39)** — fiche 8982 — D_OUV 1974-10-21

## Méthode

- **MNEMO_Q (mémoire d'abord)** : mem 4d1ea161 (fait consolidé VERIFIE, passe chaîne 0957) — « 2 mobiles Jura 1974 = création SICTOM Haut-Jura (fixes années 1990), 6 rondes 01/01, 1 aberrante » — patron global déjà établi, GAP : identité/audit individuel des 5 sites restants.
- **Discriminant** : croiser chaque D_OUV SINOE avec la **date de création de l'EPCI/acteur** (Banatic) et les **historiques officiels** des syndicats (SICTOM, SBA). Le patron de contamination (Benais/St-Aquilin/Ivry) prédisait : D_OUV = date de structure, pas d'ouverture.

## Résultats (sources INSPECTED par FETCH/lecture directe)

| FCT | Fait | Preuve | Statut |
|---|---|---|---|
| **FCT-001** | **Longwy 1960 = année de création de l'intercommunalité** : AGL (Agglomération du Grand Longwy) créée le **27/11/1960** (Banatic) ; exploitant SINOE actuel « Veolia Eau-Cge » (Dombasle) puis « Veolia Propreté (Onyx Est) » — entreprise d'eau/déchets, gestion ENTRE ; ZI du Pulventeux = ancienne concession minière/sidérurgie ; aucune déchèterie moderne 1960 documentée | dataset SINOE raw (2690) + Banatic AGL + fiches SINOE | ✧ |
| **FCT-002** | **Montville 1980 = date ronde non corroborée** : D_OUV 01/01/1980 ; CC Portes N-W Rouen créée **2009-12-31** (Banatic), puis Inter-Caux-Vexin (2017) ; déchèterie communautaire en régie ; aucune autorisation/acte 1980 | dataset SINOE (2857) + Banatic CC + fiche SINOE | ✧ |
| **FCT-003** | **Randan 1980-07-25 non corroboré + service FERMÉ** : fiche SINOE 4482 marquée « Service fermé » (MàJ 19/10/2021) ; SBA créé par arrêté préfectoral du **17/12/1975** (Banatic) ; historique officiel SBA : **maillage de 12 déchèteries entre 1990 et 2010** → le D_OUV 1980 précède de 10 ans le maillage revendiqué | fiche SINOE 4482 (fermée) + SBA 40 ans (sba63.fr) + Banatic SBA + dataset | ✦ (2 familles, réfutation NONE) |
| **FCT-004** | **Mobiles Jura 1974 = date exacte de création du SICTOM** : D_OUV 1974-10-21 = **21/10/1974** (Banatic, arrêté préfectoral, opérationnel 01/07/1979) ; historique officiel SICTOM : « premières décennies : déchets broyés puis mis en **décharge** » ; « **années 1990 : construction des premières déchèteries à Saint-Claude et à la Savine (Morbier)** » ; les fixes correspondants (2890 St-Claude, 2884 La Savine) ont D_OUV **1995-11-01** = cohérent | historique SICTOM (sictomhautjura.fr) + Banatic SICTOM + dataset SINOE (8983/8982/2890/2884) | ✦ (2 familles, réfutation NONE) |
| **FCT-005** | **Verdict : 9/9 sites pré-1980 audités, aucun ne documente une déchèterie moderne pré-1980** — les D_OUV sont des dates de création de syndicat/intercommunalité (SICTOM 1974, AGL 1960, SBA 1975), des dates rondes 01/01 (Montville), ou non corroborés (Longwy, Randan) → **la primauté Gradignan (acte 21/03/1980, SINOE 1981) sort renforcée** | synthèse FCT-001..004 | ✧ |

## Réfutations adversariales

- **Randan** : aucune source ne documente une ouverture réelle de déchèterie à Randan en 1980 (pas d'acte, pas de presse, maillage SBA daté 1990-2010) → **NONE**
- **Mobiles Jura** : aucune source ne documente une déchèterie mobile SICTOM ouverte en 1974 ; l'historique officiel dit « décharges » dans les premières décennies et « premières déchèteries années 1990 » → **NONE**

## Mécanisme causal (CAU-001/002)

Le champ D_OUV SINOE est **renseigné par les déclarants (EPCI/exploitants) sans contrôle de cohérence temporelle** : la date de création du syndicat/intercommunalité (ou une date ronde 01/01) est recopiée dans le champ « date d'ouverture de la déchèterie ». Signature identique à Benais (26/11/1973 = création SMIPE), St-Aquilin (déclaration préfectorale 2012 vs D_OUV 1973), Ivry (aucune autorisation).

## Traçabilité

- Sources : SRC-001 (historique SICTOM, INSPECTED), SRC-002 (SBA 40 ans, INSPECTED), SRC-003 (Banatic AGL), SRC-004 (fiche SINOE 2690, INSPECTED), SRC-005 (dataset SINOE raw, T1), SRC-006 (fiche SINOE 4482 fermée, INSPECTED), SRC-007 (fiche SINOE 2857, INSPECTED), SRC-008 (Banatic SICTOM), SRC-009 (Banatic SBA).
- 2 familles indépendantes sur les FCT ✦ : A (SINOE dataset + fiches) + B (Banatic, historiques officiels syndicats).
- Limite assumée : presse locale 1970s (Longwy, Montville) payante/non numérisée ; archives départementales non consultées dans cette passe.
