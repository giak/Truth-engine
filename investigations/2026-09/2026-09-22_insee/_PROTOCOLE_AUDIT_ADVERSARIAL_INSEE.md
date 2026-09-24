# PROTOCOLE D'AUDIT ADVERSARIAL DE L'INSEE — « INDEC-killer FR » (v1, 2026-09-22)
## Conception opérationnelle : données croisées, tests de falsification, signaux automatisables

**Posture** : l'audit adversarial n'est pas une accusation. Les contrôles réglementaires existants (Eurostat/GNI, peer reviews ESS, ASP, Cour des comptes) sont de conformité ; ce protocole ajoute la couche qui **manque par design** : une recherche continue, outillée, de *divergences* entre les chiffres publiés et des étalons indépendants. ABSENCE!=CONCEALMENT : un signal orange n'incrimine pas, il **oblige à expliquer publiquement** — symétrique de ce qu'Eurostat impose aux États. Trois verdicts par indicateur : VERT (conforme) / ORANGE (divergence à expliquer) / ROUGE (divergence non expliquée après réponse).

**Garde-fous anti-abus** : tests **pré-enregistrés** (seuils fixés avant chaque exercice), journal d'exécution horodaté, publication des résultats négatifs (un audit qui ne trouve rien doit le dire), interdiction de modifier les tests après observation des données.

---

## M1 — ÉTALONS INDÉPENDANTS (triangulation externe)

### 1a. Inflation
**Données croisées** : IPC Insee (BDM, ~700 séries) vs (i) indices de prix scanner privés (NielsenIQ/Circana — accès par convention recherche ou CASD ; coût ⁅, accessibilité non vérifiée) ; (ii) **étalon « panier figé »** reconstruit par scraping public de prix (supermarchés en ligne, drive — biais d'échantillon corrigé par quotas INSEE-PCS) ; (iii) IPCH Eurostat (référence harmonisée) ; (iv) indice FAO (alimentaire mondial) pour l'ancre importée.
**Tests de falsification** (seuils proposés, à calibrer) :
- F1 : écart glissant 12 mois |IPC − étalon| > 1,5 pt pendant ≥ 3 mois → ORANGE ; > 2,5 pt → ROUGE.
- F2 : divergence France/zone euro sur un poste COICOP identique > 2 pts non expliquée par composition → ORANGE.
- F3 : test de substitution : quand l'Insee mesure des produits « remplacés », le poids du remplaçant dans l'étalon doit suivre la consommation réelle (scanner) — dérive du panier public non justifiée → ORANGE.
**Signaux automatisables** : fetch quotidien BDM + Eurostat API ; scraping hebdo de 2 000-5 000 SKU ; calcul mensuel des écarts ; alerte CUSUM (cumulative sum) sur l'écart étalon.

### 1b. Emploi / chômage
**Données croisées** : taux BIT (EEC) vs (i) **masse salariale DSN** (URSSAF/Agirc-Arrco — administrative, massive, indisponible au mois ⁅) ; (ii) ré-estimation BIT **à l'aveugle** par un chercheur CASD sur les microdonnées EEC brutes (replication indépendante du process) ; (iii) cat A France Travail vs BIT (l'écart 2,3 M vs 3,0 M doit être explicable par halo/inactivité — la décomposition AEF : 49/25/17/9 % est l'étalon de cohérence) ; (iv) consommations marchandes (cartes bancaires agrégées) comme proxy d'activité.
**Tests** : 
- F4 : décomposition BIT/cat A qui s'écarte de sa structure historique > 2 σ pendant 2 trimestres (changement de régime des règles, ex. bascule radiation→suspension 11/2025) → ORANGE **si la série « ajustée des règles » n'est pas publiée**.
- F5 : réplication CASD : |BIT répliqué − BIT publié| > 0,3 pt (IC à 95 %) → ROUGE.
**Signaux** : pipeline mensuel cat A/BIT ; versionnage des règles de comptage (radiations, suspensions) publié en diff ; alerte sur rupture de série sans note méthodologique associée.

### 1c. Comptes nationaux / dette
**Données croisées** : PIB/déficit vs (i) **TVA encaissée** (DGFiP) vs consommation finale ; (ii) masse salariale administrative vs rémunérations APU ; (iii) douanes vs balance des paiements BdF ; (iv) encours d'émissions AFT (valeur faciale) vs dette Maastricht (valeur de marché — l'écart doit être traçable aux taux, tout résidu = reclassification ou erreur) ; (v) comptes des collectivités (OFGL/DGCL).
**Tests** :
- F6 : identité dette : Δdette(N) = solde(N) + émissions nettes ajustées + variation de valeur de marché + reclassifications — tout résidu > 0,3 % du PIB non ligne-à-ligne → ORANGE.
- F7 : élasticité TVA/consommation hors bornes historiques (±2 σ) sans explication → ORANGE.
- F8 : élasticité prélèvements/PIB prévue vs réalisée, série longue — asymétrie systématique signée (test de Student sur les révisions) → ORANGE sur la *gouvernance des prévisions* (côté Bercy, pas Insee).
**Signaux** : pont comptable automatique AFT/BdF/Insee ; détection d'événements de périmètre par rupture de série + croisement presse/Eurostat.

## M2 — SYMÉTRIE ET PRÉDICTIBILITÉ DES RÉVISIONS (base de vintages)

**Données** : base de **vintages** = chaque estimation publiée (première estimation → provisoire → semi-définitif → définitif, tous les rebasings) croisée au trimestre/année de référence. Matériel existant : publications successives Insee (IR, comptes de la Nation), **décomposition des révisions déjà produite par le CNP** (5ᵉ rapport, 14/04/2025, graphique A2 base 2020) — le protocole exige sa continuité et sa publicité systématique.
**Tests** :
- F9 : **asymétrie signée** des révisions (H0 : E[rev] = 0) par millésime et par type (rebase vs données nouvelles) — 20 ans de fenêtre.
- F10 : **prédictibilité** : régression de la révision finale sur l'information disponible à t1 — une révision prévisible = estimation initiale non efficace (le signal INDEC-like n'est pas « réviser », c'est « réviser dans une direction annoncée par des données déjà publiques »).
- F11 : **benchmark UE** : amplitude des révisions France vs Allemagne/Italie/Espagne — plus petites que la moyenne UE en régime d'actualité comparable = suspect ; plus grandes = justement documentées (transparence).
**Signaux automatisables** : ingestion systématique des vintages ; CUSUM sur les révisions cumulées ; carte de chaleur par poste (débit/credit du compte).

## M3 — TRANSPARENCE DES FRONTIÈRES (le point dur documenté en 2026)

**Exigences (à publier par l'Insee, formats machine-lisibles)** :
- T1 : **registre consolidé des changements de périmètre APU** (entité, date, effet dette €, effet déficit €, décision Eurostat référencée) — aujourd'hui : cas par cas, jamais agrégé (constat artefact _RECLASSIFICATIONS_APU_ : ≥ 100 Md€ de marches 2012/2019/2020-22 sans tableau pont).
- T2 : **pont dette annuel** : dette N-1 → N avec lignes explicites (émissions nettes, ajustement valeur de marché, reclassifications, autres).
- T3 : **versionning public des méthodos** (l'Insee a déjà GitHub — exiger les mêmes diffs pour les méthodes que pour le code) + calendrier des révisions en API.
- T4 : séries « alternatives » à égalité de visibilité : IPC y compris loyers imputés (existe), BIT ajusté des effets de règles (à créer), dette nette d'actifs (existe).
**Tests** : F12 : tout changement de série publiée > 0,1 pt doit résolre vers une entrée de T1-T3 ; sinon ORANGE automatique (test 100 % scriptable : diff de BDM).

## M4 — RED TEAM INSTITUTIONNALISÉ

- **Unité adversariale** adossée au **CASD** (existe : accès chercheurs aux microdonnées, Comité du secret) : 4-6 chercheurs accrédités en rotation annuelle, mandat explicite « chercher la divergence, pas la confirmation », accès EEC + microdonnées IPC + fichiers de notification ; publication obligatoire des rapports (version française et continue des peer reviews ESS) ; rattachement parlementaire (type office parlementaire d'évaluation) pour l'indépendance budgétaire.
- **Circuit d'alerte interne** : ASP + défenseur des droits + régime lanceurs d'alerte ; traité < 3 mois, réponse publique motivée.
- **Benchmarks de conception** : GSO/ANDEC indiens (forensique statistique), FSO suisse (transparence des vintages), statbel (communication des révisions).

---

## PIPELINE AUTOMATISABLE (architecture)

```
SOURCES: BDM API | Eurostat API | DGFiP open data | AFT | BdF Webstat | OFGL
         scraping SKU (2-5k) | presse (NLP) | notes méthodo (versioned)
STOCKAGE: base de vintages versionnée (chaque donnée = (série, vintage, valeur, date_pub))
TRAITEMENT: écarts étalons (F1-F3) | identités comptables (F6-F7) | révisions (F9-F11)
            diff de séries (F12) | CUSUM/z-scores pré-enregistrés
SORTIE: dashboard public — verdicts VERT/ORANGE/ROUGE par indicateur, historique,
        chaque ORANGE avec l'espace de réponse officiel lié
```
**Coûts ordres de grandeur** : scraping + pipeline ≈ 1-2 ETP ; unité CASD ≈ 4-6 ETP chercheurs ; licences scanner privées ⁅ (alternatives publiques préférables en v1).

## LIMITES DU PROTOCOLE (honnêteté)

1. Il détecte des **divergences**, jamais des **intentions** — l'issue d'un ORANGE est une obligation d'explication, pas un verdict de culpabilité.
2. Les étalons ont leurs propres biais (scraping : panier digitalisé ; scanner : licence et représentativité) — la triangulation à 3 sources minimum est la règle.
3. Certains accès restent ouverts ⁅ : licences scanner, DSN mensuelle par entreprise, archives de vintages pré-2000 — documentés comme gaps d'accès, pas supposés dissimulés.
4. Le protocole ne remplace pas Eurostat : il le **concurrence** — c'est sa fonction. Un institut honnête n'a rien à craindre d'un adversaire public, prévisible et journalisé ; c'est le test final que ce document propose.
