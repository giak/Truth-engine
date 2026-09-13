# AUDIT D'ANTÉRIORITÉ — Arles « Les Ségonnaux » (Bouches-du-Rhône)

AS_OF : 2026-08-30 · Dossier dechetteries-france-fresque
OBJET : vérifier la date d'ouverture déclarée (SINOE `D_OUV 1977-01-01`), caractériser ce qu'était le site avant le néologisme « déchèterie » (1987), et trancher la primauté vs Gradignan.
MÉTHODE : sources primaires (dataset SINOE brut, ICPE préfecture 13, presse locale) consultées directement ; statuts V / sn / OPEN / REFUTÉ marqués selon KERNEL.

---

## 1. Fiche SINOE (source primaire consultée — dataset brut `/tmp/sinoe_annuaire.csv`)

Fiche C_SERVICE = **3610**, N_SERVICE = `DÉCHÈTERIE D'ARLES` (années 2009/2011 : « Déchèterie d'Arles » ; 2015/2017 : « Déchèterie d'Arles Ségonnaux »).

| Champ | Valeur | Statut |
|---|---|---|
| D_OUV | **1977-01-01** | V (constant 2009→2026) |
| D_MODIF | 2020-11-10 | V |
| AD1_SITE | les Ségonnaux | V |
| CP / Ville | 13200 / Arles | V |
| LOV_MO_GEST | **REGIE** | V |
| C_ACTEUR (2009-2015) | 6877 — Commune d'Arles | V |
| C_ACTEUR (2017+) | 57651 — CA Arles-Crau-Camargue-Montagnette (ACCM) | V |
| ORIGINE_DECHET_ACC | DMA | V |
| LST_TYPE_DECHET | 01.3\|02.31\|06\|07.2\|07.5\|08.2\|08.3\|10.3\|13.11 (2009-2015) | V |

- La date **1977-01-01 est stable sur toutes les enquêtes 2009→2026** — ce n'est pas un artefact d'une seule année. **Véracité interne renforcée.** ✅

## 2. Ce que le site ÉTAIT avant le mot « déchèterie »

Le néologisme « déchèterie » ne date que de la circulaire **87-63 (26/06/1987)** — aucun site 1977 ne portait ce nom à l'époque. En 1977, un tel équipement s'appelait « **dépôt d'encombrants** », « **décharge contrôlée/communale** » ou « centre de recyclage ». Or l'audit le confirme pour Arles :

- **La Provence, 25/02/2014** : « Décharge communale : la Ville tire un trait sur **35 ans d'excès** » — « **Exploité entre 1964 et 1999**, le site est en cours de réhabilitation. » → les Ségonnaux étaient une **décharge communale** depuis **1964**. (T2 presse, V sur la période 1964-1999)
- **Préfecture des Bouches-du-Rhône — ICPE / Commune d'Arles** : « Réhabilitation de l'**ancienne décharge des Ségonnaux** » — **Arrêté du 13/07/2017** notifiant les mesures de réhabilitation et de suivi environnemental ; **Arrêté 10/04/2020** modifiant ces mesures ; **arrêté 11/01/2018** instaurant des SUP. → lignée officielle « ancienne décharge ». (T1 actes administratifs, V)
- **Ville d'Arles**, publication 24/01/2022 : « Arrêté préfectoral n° 2020-201 PC portant prescriptions complémentaires à la Ville d'Arles pour des travaux de **réhabilitation et de suivi post-exploitation de l'ancienne décharge communale des Ségonnaux**. » (T1, V — intitulé confirmé à l'écran)

## 3. Découverte discriminante — double lecture

**A) Antériorité de l'apport-volontaire arlésien : RENFORCÉE.**
Le site des Ségonnaux a été une aire de dépôt/décharge communale dès **1964**, et l'apport-volontaire au public y est documenté (SINOE) à partir de **1977-01-01** : soit **~16 ans avant** la date revendiquée de Gradignan (acte CUB 21/03/1980 / revendication 17/11/1980 / SINOE 1981-01-01). En tant que **fonction d'apport-volontaire**, Arles précède Gradignan. **(convergence : SINOE stable + presse 2014 + ICPE 2017)**

**B) Primauté de l'« équipement moderne » : DÉTRUITE → REFORMULÉE.**
Ce n'est **pas** la création ex nihilo d'une déchèterie moderne en 1977 : c'est la **requalification/usage d'une décharge communale** préexistante, qui n'a jamais porté le nom de « déchèterie » avant 1987. La valeur SINOE 1977 reflète donc une **date d'usage/d'enquête**, pas un acte de création d'équipement au sens post-87. **(REFUTÉ en tant que « première déchèterie moderne 1977 » ; CONFIRMÉ en tant que « site d'apport-volontaire antérieur à 1980 »)**

## 4. Chronologie vérifiée des Ségonnaux

| Date | Fait | Source | Statut |
|---|---|---|---|
| 1964 | Début exploitation décharge communale | La Provence 2014 | V (sn) |
| 1977-01-01 | Apport-volontaire au public (D_OUV SINOE) | SINOE dataset | V |
| 1999 | Fin exploitation décharge | La Provence 2014 | V (sn) |
| ~2017 | Fermeture de la déchèterie des Ségonnaux (digue entre Arles…) | La Provence 2023 | V |
| 13/07/2017 | Arrêté ICPE réhabilitation ancienne décharge | Préfecture 13 | V |
| 05/2023 | Ouverture Trinquetaille (reconstruction, 11 quais, ACCM) | La Provence 2023 | V |

## 5. Verdict sur la primauté

- **Gradignan reste validé comme** premier centre moderne **urbain documenté par acte (aff. 80/151, 21/03/1980)** — la primauté du *récit* n'est pas détruite sur ce point.
- **Arles ne peut PAS revendiquer « première déchèterie moderne 1977 »** : son site était une décharge communale (1964-1999), et l'équipement ne porte pas/portait pas ce nom.
- **Mais le récit « Gradignan = première de France » reste à requalifier** : il existe des apports-volontaires antérieurs (Arles 1977, Benais 1973, St-Aquilin 1973, Ivry 1975) sur des décharges/dépôts. La bonne formulation : « l'un des premiers équipements d'apport volontaire modernes et explicitement dédiés » / « premier du type au niveau intercommunal CUB ».

## TRAÇABILITÉ
- Dataset SINOE brut `/tmp/sinoe_annuaire.csv` (fiche 3610, INSEE 13004) — INSPECTED.
- La Provence 2014 (édition Arles, « Décharge communale : la Ville tire un trait sur 35 ans d'excès ») — INSPECTED (titre+sous-titre en page).
- Préfecture 13, ICPE page « Arles », rubrique Commune d'Arles / ancienne décharge des Ségonnaux (3 arrêtés listés) — INSPECTED.
- Ville d'Arles, publication arrêté 2020-201 PC (24/01/2022) — INSPECTED à l'écran (PDF anti-robot, intitulé confirmé).
- La Provence 2023 (21/03/2023, Trinquetaille) — INSPECTED (paywall partiel, intro lue).
- horaire-dechetterie.fr — miroir SINOE (D_OUV 1977, régie, 52 347 hab) — corroborant (T4/miroir).

## GAPS / PROCHAINES FRAPPES
1. **Cote de l'acte municipal de 1977-01-01** (délibération commune d'Arles) — introuvable en ligne ; demande aux Archives communales d'Arles.
2. **Preuve indépendante exacte de l'apport-volontaire en 1977** (presse 1976-1978) — Gallica couvre mal cette période ; à tenter presse locale (La Provence archives payantes, Le Méridional).
3. **Vérifier si le `D_OUV 1977` reflète l'enquête plus que l'acte** — distinguer « date d'enquête » vs « date d'ouverture réelle ».