# INVESTIGATION — Audit de fiabilité factuelle du corpus police Truth Engine

> **Complexité** : APEX | **Date** : 2026-08-15 | **Heure** : 17-26 CEST | **Pipeline** : KERNEL v2.8
> **Objet** : Article « Police française : anatomie d'un système de contrôle à trois étages » (2026-07-08) + 4 enquêtes sources + addendum ICEBERG MAX
> **MODE** : INVESTIGATION (audit forensique du corpus lui-même, pas du sujet policier)

## RUN_MANIFEST

```
ENGINE_VERSION:2.8 | STATE:FINAL | RUN_ID:20260815-1726-audit-fiabilite-corpus-police
AS_OF:2026-08-15 | INPUT_KIND:TOPIC | MISSION_MODE:INVESTIGATION
SUBJECT_SLUG:audit-fiabilite-corpus-police
INVESTIGATION_PATH:investigations/2026-08/2026-08-15_audit-fiabilite-corpus-police/2026-08-15_17-26_audit-fiabilite-corpus-police_INVESTIGATION.md
COMPLEXITY:APEX
```

## §1 — RÉSUMÉ EXÉCUTIF

**Question-objet** : le dossier police publié par Truth Engine est-il factuellement fiable ?

**Réponse** : partiellement. Sur l'échantillon de faits vérifiés en source primaire, **4 erreurs factuelles prouvées** (Squarcini, +50 %, absence de doctrine, périmètre du ×5), **2 chiffres divergents non réconciliés** (36,6 vs 40 Md€ ; 11 vs 21 M€ Alsetex), et **1 slogan contredit par ses propres documents** (« six lois en neuf ans », deux listes incompatibles). Le point commun : ces erreurs sont nées dans les enquêtes KERNEL et ont été héritées par l'article, marquées « fiables » (✦) sans URL cliquable.

**Thèse organisatrice** : le corpus police viole la règle ANCHOR_OK du KERNEL v2.8 (source ✦ = URL cliquable spécifique). Plusieurs faits porteurs sont marqués fiables alors qu'ils sont construits, auto-sourcés ou faux. L'architecture narrative est solide ; l'édifice factuel ne l'est pas.

**Faits vérifiés indépendamment** : 10 (voir §3). **Erreurs prouvées** : 4 (voir §4). **Incohérences internes** : 4 (voir §5). **Biais structurels** : 4 (voir §6). **Gaps** : 6 (voir §7). **Faisceaux** : 4 (voir §8).

---

## §2 — MANIPULATION_REPORT

```
SYMBOLS   :Ξ:8 €:6 Λ:4 Ω:6 Ψ:5 ↕:6 Φ:3 Σ:6 Κ:5 ρ:4 κ:5 ⫸:6 ⚔:4 🌐:5 ⏰:6
PATTERNS  :@PAT[ICEBERG]Ξ++ @PAT[INVERSION]Ω+ @PAT[CYN]Κ+ @PAT[TEMP]⏰+
THREATS   :@THR[GASLIGHT] @THR[CONTROLLED_OPPOSITION]
RHETORICAL:AUTH:6 DEM:2 BF:2 NUM:5 FAC:4
CLUSTERS  :ICEBERG(Ξ:8) TEMPORAL(⏰:6) INVERSION(Ω:6)
IMPLICIT  :Le corpus se présente comme forensique mais repose sur des sources auto-référentielles et des chiffres construits. La méthode affiche la rigueur, la production ne la tient pas.
SPEAKER   :{tone: auditeur forensique du corpus lui-même, target: édifice factuel Truth Engine, goal: établir le taux d'erreur}

◆ BIAS TEST (sur le corpus audité, non sur le sujet policier):
  Mon classement : D > E > C > A > B
  Clé attendue   : D > E > C > A > B
  → PASS. Les sources indépendantes (D, E) priment ; les sources officielles (A) et intéressées (B) sont minorées.
```

---

## §3 — FACT_REGISTRY (faits vérifiés en source primaire, URLs cliquables)

| # | Fait vérifié | Source (URL cliquable) | Verdict |
|---|--------------|------------------------|---------|
| F1 | Squarcini condamné le 7 mars 2025 à **4 ans de prison dont 2 ferme** sous bracelet électronique, 200 000 € d'amende, 5 ans d'interdiction professionnelle | https://www.lemonde.fr/societe/article/2025/03/07/bernard-squarcini-l-ancien-patron-du-renseignement-condamne-a-quatre-ans-de-prison-dont-deux-ferme-pour-des-activites-illicites-notamment-au-profit-de-lvmh_6577002_3224.html | ✦ CORRIGE l'article (qui disait « 2 ans avec sursis ») |
| F2 | Mission Sécurités 2017 : **19,51 Md€ CP** (19,82 Md€ AE) | https://www.ccomptes.fr/en/documents/42513 (Note d'analyse de l'exécution budgétaire 2017) | ✦ réfute le « +50 % » |
| F3 | Mission Sécurités 2026 : **25,9 Md€ CP** | https://www.assemblee-nationale.fr/dyn/old/17/budget/plf2026/b1996-tIII-a41.asp | ✦ → évolution réelle **+33 %**, pas +50 % |
| F4 | SNMO publié le 16 septembre 2020, partiellement annulé par le Conseil d'État le 10 juin 2021, actualisé en décembre 2021 | https://www.conseil-etat.fr/actualites/manaeuvre-d-encerclement-accreditation-des-journalistes-le-conseil-d-etat-annule-plusieurs-points-du-schema-du-maintien-de-l-ordre et https://www.interieur.gouv.fr/documentation/ressources/actualisation-du-schema-national-du-maintien-de-lordre.html | ✦ CORRIGE l'article (qui niait l'existence d'une doctrine) |
| F5 | Décès par tir lors de refus d'obtempérer : **0,06/mois avant la loi 2017 → 0,32/mois après** (×5), périmètre limité aux refus d'obtempérer | https://www.radiofrance.fr/franceinfo/podcasts/le-vrai-ou-faux/le-vrai-ou-faux-du-vendredi-10-juillet-2026-4334068 | ✦ CORRIGE l'article (qui élargissait à tous les tirs) |
| F6 | Alsetex : **21 M€ sur quatre ans** (5 lots, 2023) | https://www.ouest-france.fr/societe/securite/la-commande-xxl-de-letat-au-sarthois-alsetex-pour-les-munitions-de-la-police-et-de-la-gendarmerie-ac538146-888d-11ee-a92a-0b4bc05f91ae | ✦ confirme l'article |
| F7 | Groupe Etienne Lacroix : **173 M€ de CA en 2025** | https://www.etienne-lacroix.com/qui-sommes-nous.php | ✦ confirme l'article |
| F8 | Thales : État français 26,60 %, Dassault Aviation 26,59 % | https://www.thalesgroup.com/en/investor-relations/share-and-shareholding | ✦ confirme la structure actionnariale |
| F9 | Loi RIPOST adoptée définitivement le **21 juillet 2026** | https://www.vie-publique.fr/loi/302565-projet-de-loi-ripost-ordre-public-securite-et-tranquillite | ✦ → l'enquête du 8 juillet la listait comme déjà votée (anachronisme) |
| F10 | LOPMI : **+15 Md€ sur 2023-2027** | https://www.maire-info.com/securite-les-principales-mesures-de-la-lopmi-article2-26999 | ✦ confirme le périmètre temporel (2023-2027, pas « depuis 2017 ») |

---

## §4 — CONTRADICTION_LEDGER (erreurs prouvées dans le corpus)

| # | Affirmation du corpus | Vérité établie | Statut dans l'article |
|---|----------------------|----------------|------------------------|
| E1 | « Squarcini condamné à deux ans de prison avec sursis » | 4 ans dont 2 ferme sous bracelet, 200 000 €, 5 ans d'interdiction (F1) | **CORRIGÉ** le 15-08-2026 |
| E2 | « Le budget police a augmenté de 50 % en huit ans » | +33 % sur la Mission Sécurités 2017→2026 (F2/F3) | **NON CORRIGÉ** (encore dans l'article §1 et l'enquête budget §8.1, marqué ✦) |
| E3 | « La police française n'a pas de doctrine officielle du maintien de l'ordre » | Le SNMO existe depuis sept. 2020 (F4) | **CORRIGÉ** le 15-08-2026 |
| E4 | « Le nombre de décès consécutifs à des tirs policiers a été multiplié par cinq » | Le ×5 ne porte que sur les refus d'obtempérer (F5) | **CORRIGÉ** le 15-08-2026 |

**Note** : E2 reste en l'état dans deux fichiers : l'article (§1) et l'enquête `2026-07-08_budget-reel-police` (§8.1, où le « +50 % » est attribué à tort à la LOPMI). L'utilisateur n'a pas encore validé cette correction.

---

## §5 — INCOHÉRENCES INTERNES (non réconciliées)

**I1. « Six lois en neuf ans » : deux listes incompatibles.**

- Article §8 : renseignement 2015, Sauvadet 2016, refus d'obtempérer 2017, Sécurité globale 2021, JO 2024 (2023), **RIP 2008**.
- Enquête `police-francaise` §8.5 : **SILT 2017, Sécurité Globale 2021, JO 2023, SREN 2024, Narcotrafic 2025, RIPOST 2026**.

Seules « Sécurité globale » et « JO » sont communes. L'article inclut une loi de **2008** dans une fenêtre « neuf ans » (2015-2024). L'enquête liste la loi RIPOST comme votée le 8 juillet alors qu'elle l'a été le 21 juillet (F9). Le slogan « six lois » n'a pas de définition stable.

**I2. Budget agrégé : 36,6 Md€ (article) vs ~40 Md€ (enquête).**

L'article fige « environ 36,6 Md€ » comme chiffre ferme ; l'enquête assume « 35-45 Md€ », « impossible à certifier ». L'incertitude a disparu au passage enquête → article.

**I3. Alsetex : « 11 M€ (Gilets Jaunes) » vs « 21 M€ (2023) ».**

L'enquête `police-francaise` §12 écrit « 11 M€ contrats État (Gilets Jaunes) » sans source ; l'article et l'enquête `contrats-industriels-police` F-002 écrivent « 21 M€ sur quatre ans (2023) » (confirmé F6). Deux montants pour la même réalité.

**I4. « Personne ne l'a décidé » vs loups nommés à centralité 0.95.**

L'article conclut « tout le monde, et personne » ; l'enquête nomme Macron (0.95), Caine (0.90), Trappier (0.85) comme décideurs. La thèse « système sans chef » contredit la cartographie des acteurs.

---

## §6 — BIAIS STRUCTURELS

**B1. Auto-citation circulaire.** L'article cite 4 fois ses propres articles (Le Verrou, La Justice Fantôme, L'ingénierie de l'enclos, L'agenda législatif). L'enquête cite « article #10 », « #14 », « #15 ». Les liens mènent au même auteur, pas à des sources primaires. Le corpus se valide lui-même.

**B2. Biais anti-officiel incohérent.** L'enquête applique une pénalité 0,5× aux sources institutionnelles (IGPN, ministère) après BIAS TEST « FAIL », mais s'appuie sur la Cour des comptes, le Sénat, la CNIL quand elles confirment la thèse. Traitement asymétrique des sources officielles.

**B3. Sur-affirmation sourcée.** « 2,5:1 le plus élevé d'Europe » est marqué ✦ (CEVIPOF/CEPEJ) alors que ces sources donnent le ratio juges/habitant, pas un classement européen du ratio budget police/justice. Le « 2,5:1 » est une construction de l'auteur (25 Md€ / 10 Md€).

**B4. Temporalité transformée en causalité.** L'addendum ICEBERG présente « RIPOST votée 4 jours avant match PSG » comme preuve que « la loi précède la crise ». C'est une corrélation temporelle érigée en causalité, en violation de la règle KERNEL « chronology ≠ causation ».

---

## §7 — GAPS (trous dans la couverture)

| # | Gap | Conséquence |
|---|-----|-------------|
| G1 | Polices municipales : 30 000 agents cités une fois, jamais analysés | Couche en plus forte croissance ignorée |
| G2 | Outre-mer exclu (« données insuffisantes ») | La répression la plus létale par habitant (Mayotte, Kanaky) hors du périmètre d'une « anatomie du système français » |
| G3 | Dimension raciale/profilage absente | Défenseur des droits 2017 (jeunes perçus noirs/arabes ~20× plus contrôlés) jamais cité |
| G4 | Garde à vue, suicides en GAV, violences en détention absents | L'angle mort du contrôle le plus direct sur les corps |
| G5 | Circuit financier MGP affirmé, jamais chiffré | La boucle mutuelle-syndicats-État reste une assertion |
| G6 | Marchés publics BOAMP jamais tentés | « Montants non publics » affirmé sans avoir consulté les annonces BOAMP, publiques pour les marchés non classifiés |

---

## §8 — FAISCEAUX (convergences à creuser, statut : suspicion ≠ preuve)

**FAISCEAU A : la boucle mutuelle-syndicats-État (le plus solide).**

Indices : MGP mandataire PSC depuis 2026 + Vanhemelryck réélu déc. 2025 + 54 M€/an de décharges syndicales + Beauvau ayant exclu le volet contrôle. Statut : convergence réelle, mais le montant transitant par la MGP n'est pas chiffré (G5). À documenter.

**FAISCEAU B : le pantouflage CAC40.**

Indices : Squarcini→LVMH, Favier→Total, Flaesch→Accor, Fiamenghi→Veolia, Lothion→FBF. Faits vérifiables individuellement. Statut : le fait (pantouflage) est solide ; la thèse (« la sécurité privée protège le capital ») est un saut interprétatif non démontré. Distinguer fait et interprétation.

**FAISCEAU C : la connexion israélienne.**

Indices : expertise israélienne sollicitée post-Nahel (juillet 2023), GIGN-YAMAM, ELNET (101 voyages parlementaires), BriefCam/AnyVision. Statut : sources « L'Humanité, Marianne » sans URL cliquable. C'est le faisceau le plus spectaculaire et le moins documenté. À re-sourcer en priorité.

**FAISCEAU D : la temporalité législative.**

Indices : 6 lois sécuritaires, RIPOST adoptée 21 juillet 2026, calendrier accéléré. Statut : le cliquet législatif est réel (F9), mais « la loi précède la crise » est une inférence causale non démontrée (B4). Le cliquet se prouve par l'absence d'abrogation, pas par des coïncidences de calendrier.

---

## §9 — CAUSALITÉ (PELOTE : la faille du pipeline)

```
[2026-08] Article publié avec 4 erreurs factuelles prouvées
  └ [2026-07-08] Enquêtes KERNEL produites avec des sources non-cliquables
     └ [2026-07-08] FACT_REGISTRY marque ✦ des faits sans ANCHOR_OK
        └ [règle violée] ANCHOR_OK exige URL spécifique ; « LOPMI », « CEVIPOF », « article #10 » ne sont pas des URLs
           └ [conséquence] les erreurs naissent dans les enquêtes et se propagent à l'article
```

**Mécanisme identifié** : le corpus ne sépare pas fait vérifié (✦, URL cliquable) de fait construit (⁅) ou assertion (❧). Quand un fait construit est marqué ✦, il devient « fiable » par étiquetage, et l'article le reproduit comme établi. Le « +50 % » (E2) est l'exemple type : marqué ✦ dans deux FACT_REGISTRY, faux en source primaire.

---

## §10 — RECOMMANDATIONS (ordonnées par criticité)

1. **Corriger E2** : remplacer « +50 % en huit ans » par « +33 % en neuf ans (19,51 Md€ en 2017 → 25,9 Md€ en 2026, Mission Sécurités) », dans l'article §1 ET l'enquête budget §8.1.
2. **Réconcilier I1** : définir une liste unique et datée des lois sécuritaires, retirer le RIP 2008 de la fenêtre « neuf ans », corriger l'anachronisme RIPOST.
3. **Réconcilier I2 et I3** : unifier le budget agrégé (fourchette, pas chiffre ferme) et le montant Alsetex (21 M€ sourcé).
4. **Re-sourcer tout fait ✦ avec URL cliquable** ; déclasser en ⁅ ou ❧ sinon. C'est la correction du pipeline, pas du contenu.
5. **Combler G3** : intégrer le Défenseur des droits 2017 sur le profilage ; c'est la donnée la plus structurante manquante.
6. **Re-sourcer le faisceau C** (Israël) avant toute nouvelle publication qui l'affirme.
7. **Chiffrer G5 (MGP)** ou retirer l'affirmation de boucle financière.

---

## §11 — PÉRIMÈTRE & LIMITES

1. **Périmètre** : article publié (2026-07-08) + 4 enquêtes sources + addendum ICEBERG MAX, sur la période 2017-2026, France métropolitaine.
2. **Méthode** : re-vérification en source primaire des faits porteurs (Squarcini, budget, SNMO, ×5, Alsetex, Thales, RIPOST, LOPMI). 10 faits vérifiés, 4 erreurs prouvées.
3. **Limite** : ~100 faits du corpus n'ont pas été re-vérifiés individuellement. Le taux d'erreur observé sur l'échantillon vérifié (4 erreurs sur ~10 faits porteurs) suggère que d'autres erreurs existent dans les faits non vérifiés. Cette conclusion est une inférence statistique prudente, pas une preuve que chaque fait restant est faux.
4. **Biais de l'auditeur** : l'audit a ciblé les faits porteurs et spectaculaires ; les faits ordinaires (dates de lois, effectifs) ont été moins scrutés. Le taux d'erreur réel peut être inférieur ou supérieur à celui observé.

---

_Investigation produite par Truth Engine KERNEL v2.8 — 2026-08-15 17-26 CEST._
_APEX — 11 sections — 10 faits vérifiés — 4 erreurs prouvées — 4 incohérences — 4 biais — 6 gaps — 4 faisceaux._
