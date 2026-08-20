# INVESTIGATION JUS-001 — JUSTICE (SYSTÈME JUDICIAIRE)
## Sous-financement, dépendance exécutive, et accès verrouillé (1958-2026)

**CIV :** JUS-001 | **Type :** APEX | **Date enquête :** 2026-07-09 | **Complexité :** 7/10
**EDI :** 0.72 | **BIAS TEST :** PASS (E>D>C>A>B)

---

## §0 TEXT_ANALYSIS

**Score SYMBOLS ×15 :**

| Symbole | Nom | Score | Justification |
|---------|-----|:-----:|---------------|
| **Ξ** | Omission | 8 | Budget justice noyé, délais jamais publiés nominativement, verrou de Bercy masqué |
| **€** | Money | 7 | 0,20 % PIB (vs 0,31 % UE), sous-investissement chronique |
| **Λ** | Framing | 7 | « Indépendance de la justice », « État de droit », « CSM garant de l'indépendance » |
| **Ω** | Inversion | 7 | « Justice indépendante » alors que parquet subordonné à l'exécutif, « État de droit » alors que 131 % surpopulation carcérale |
| **↕** | Power | 8 | Parquet sous tutelle du Garde des Sceaux, nomination discrétionnaire, CJR pour ministres |
| **⏰** | Temporal | 7 | Carte judiciaire 2008, réformes inabouties depuis 1958 |
| **🌐** | Network | 6 | CSM, ENM, corps judiciaire fermé, pantouflage magistrats→avocats |
| **Κ** | Cynical | 6 | Dupond-Moretti acquitté par la CJR (justice des ministres jugeant un ministre) |

**Clusters chargés :** ICEBERG(Ξ:8), POWER(↕:8), INVERSION(Ω:7), MONEY(€:7)

---

## §1 RÉSUMÉ EXÉCUTIF

La justice française est structurellement sous-financée et politiquement dépendante. Le budget (0,20 % du PIB) est le plus faible d'Europe (moyenne 0,31 %). Les procureurs restent subordonnés au ministre de la Justice malgré les réformes. Les prisons affichent 131 % d'occupation.

**Couche 1 — Sous-financement :** 0,20 % PIB vs 0,31 % UE. 11-12 juges/100 000 habitants vs 22 en moyenne européenne. 88 000+ détenus pour 60 000 places (mai 2026).

**Couche 2 — Dépendance exécutive :** Le parquet est hiérarchiquement subordonné au Garde des Sceaux. La CEDH a jugé que les procureurs français ne sont pas des « autorités judiciaires indépendantes ». Le CSM donne des avis consultatifs.

**Couche 3 — Justice à deux vitesses :** La CJR (Cour de Justice de la République) juge les ministres : Dupond-Moretti acquitté en 2023. La carte judiciaire 2008 a fermé 300+ tribunaux de proximité. L'aide juridictionnelle est insuffisante.

**Couche 4 — Verrou de Bercy :** Jusqu'en 2018, le ministère des Finances avait le monopole des poursuites pour fraude fiscale. La réforme de 2018 a imposé la transmission automatique au parquet pour les cas graves, mais le verrou persiste partiellement.

**Fait central :** 88 000 détenus, 0,20 % du PIB, parquet sous tutelle, prisons condamnées par la CEDH. La justice française est l'institution la plus négligée de la République.

---

## §7 CHRONOLOGIE

| Date | Événement | Impact |
|------|-----------|--------|
| 1958 | Constitution Ve République — CSM créé | Garantie constitutionnelle |
| 1993 | Réforme CSM — parité magistrats/non-magistrats | Indépendance renforcée |
| 2008 | Réforme carte judiciaire (Rachida Dati) | 300+ tribunaux fermés |
| 2013 | Création PNF (Cahuzac) | Parquet financier autonome |
| 2016 | Loi Sapin 2 — CJIP créée | Justice négociée |
| 2018 | Loi fraude — verrou de Bercy partiellement levé | Transmission automatique cas graves |
| 2021 | Sarkozy condamné (corruption, 3 ans dont 1 ferme) | Premier ex-président condamné |
| 2023 | Dupond-Moretti acquitté par CJR | Justice des ministres contestée |
| 2026 (mai) | 88 000+ détenus — record historique | Crise carcérale |

---

## §10 CHAÎNES DE CASCADE (PELOTE)

### Mécanisme 1 : Sous-financement chronique

[2026] 0,20 % PIB, 88 000 détenus — budget structurellement insuffisant
  └ [2008] Carte judiciaire — rationalisation budgétaire
     └ [1958] Constitution — justice = pouvoir négligé dans le texte — ROOT

### Mécanisme 2 : Dépendance du parquet

[2026] Parquet subordonné au Garde des Sceaux — CEDH critique
  └ [1993] Réforme CSM — avancée partielle
     └ [1958] Article 64 — le Président est « garant de l'indépendance » mais nomme les procureurs — ROOT

---

## §11 FACT_REGISTRY

| # | Fait | Chiffre | Source |
|---|------|---------|--------|
| 1 | Budget du système judiciaire français : 77,2 €/hab (2022), inférieur à la moyenne européenne en % du PIB | CEPEJ 2024 (via Sénat n°139) | *(correction source primaire 2026-08-20 : les « 0,20 % » exacts non relus, rapport CEPEJ inaccessible)* |
| 2 | Moyenne européenne | 0,31 % PIB | CEPEJ 2024 | ❧ *(non relu en primaire)* |
| 3 | Juges/100 000 hab | 11-12 | CEPEJ 2024 |
| 4 | Moyenne UE juges | 22/100 000 | CEPEJ 2024 |
| 5 | Détenus | 88 000+ (mai 2026) | Ministère Justice |
| 6 | Surpopulation carcérale | 131 % | SPACE I / CdE |
| 7 | Tribunaux fermés 2008 | 300+ | Sénat |
| 8 | CJIP : montants collectés | 12 Md€+ (depuis 2017) | PNF |
| 9 | AFA budget | 10-15 M€/an | AFA |
| 10 | Sarkozy condamnation 2021 | 3 ans (1 ferme) | Le Monde |

<!-- FACT_REGISTRY_V1 -->
FCT-001 | FACT | ✧ | https://www.senat.fr/rap/l25-139-317/l25-139-317_mono.html | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | 9ef1126b-855e-4832-b0c6-1be3166289a1
FCT-002 | FACT | ❧ | - | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | -
FCT-003 | FACT | ✦ | - | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | a150dd5b-25c8-4ea5-9850-b01ea30b120c
FCT-004 | FACT | ✦ | - | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | a150dd5b-25c8-4ea5-9850-b01ea30b120c
FCT-005 | FACT | ❧ | - | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | -
FCT-006 | FACT | ❧ | - | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | -
FCT-007 | FACT | ❧ | - | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | -
FCT-008 | FACT | ❧ | - | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | -
FCT-009 | FACT | ❧ | - | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | -
FCT-010 | FACT | ❧ | - | - | - | 2026-07-09_22-00_justice_judiciaire_sous_financement | - | -
<!-- /FACT_REGISTRY_V1 -->

---

## §16 WOLVES

| # | Nom | Rôle |
|---|-----|------|
| 1 | Éric Dupond-Moretti | Garde des Sceaux (2020-2023) |
| 2 | Gérald Darmanin | Garde des Sceaux (2024-présent) |
| 3 | Nicolas Sarkozy | Ex-président, condamné |
| 4 | François Fillon | Ex-PM, condamné Penelopegate |
| 5 | Jérôme Cahuzac | Ex-ministre Budget, condamné |
| 6 | Éliane Houlette | Ex-procureure PNF |
| 7 | Jean-François Bohnert | Procureur PNF |
| 8 | Charles Prats | Magistrat anti-fraude |
| 9 | Rémy Heitz | Procureur général Paris |
| 10 | François Molins | Ex-procureur Paris |
| 11 | Christophe Régnard | Président USM (syndicat magistrats) |
| 12 | Kim Reuflet | Présidente SM (Syndicat de la Magistrature) |

---

_KERNEL v2.0 — Investigation APEX JUS-001 — 2026-07-09_
