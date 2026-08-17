# PROTOCOLE OPÉRATIONNEL — Test PLF 2027 de la rec. n° 7 (numérisation successorale) : baseline PAP 156 vérifiée + check-list P1-P7 détaillée

- **Date** : 2026-08-10 | **Heure** : 11:27 CEST | **Type** : INVESTIGATION (protocole à date fixe — exécution octobre 2026) | **KERNEL** : v2.8
- **État** : `STATE          : FINAL`
- **Dossier** : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_protocole-plf2027-rec7/
- **Fait suite à** : 07-33 (baseline PAP 156), 07-39 (réponse 3056), 07-18 (rec. n° 7 verbatim), 07-26 (DESF 0,5 ETP), 11-24 (point consolidé final — Angle 1)

## 1. CONTEXTE

Le point consolidé final 11-24 a identifié l'Angle 1 comme test décisif daté : au dépôt du PLF 2027 (octobre 2026), la rec. n° 7 du rapport n° 3056 (« Prioriser parmi les projets de la DGFiP la numérisation des déclarations de succession et leur centralisation en vue notamment de leur exploitation statistique » — T1 l. 4545) devient-elle visible dans le bleu budgétaire du programme 156 ? Le dossier 07-33 a posé la baseline chiffrée PAP 2026 et une check-list P1-P7 minimale (7 lignes). Ce dossier : (1) vérifie la **complétude** de la baseline ; (2) transforme P1-P7 en **check-list opérationnelle exécutable** avec lieux de recherche exacts, motifs de grep, seuils et **critères de verdict** (fil brisé / partiel / confirmé).

## 2. VÉRIFICATION DE COMPLÉTUDE DE LA BASELINE 07-33

| Élément de baseline | Présent au 07-33 | Verdict | Complément nécessaire |
|---------------------|------------------|---------|-----------------------|
| Totaux AE/CP programme 156 (PAP 2026 + prévisions 2027) | ✅ FCT-001/003 (AE 8 299,8 M€ 2026 ; prévision 2027 : AE 8 269,4 / CP 8 294,1 M€) | COMPLET | — |
| Titre 5 investissement (2026 : 236,7 M€ AE +66 % ; prévision 2027 : 158,6 M€ AE) | ✅ FCT-002/003 | COMPLET | — |
| Les 3 grands projets SI chiffrés (facturation électronique 267,72 M€, PILAT, PAYSAGE) | ✅ FCT-005/006/007 | COMPLET | — |
| Mentions e-enregistrement/succession dans l'action 03 (95 %, 2021) | ✅ FCT-008 | COMPLET | — |
| Actions 03 et 09 (AE/CP + T5 action 09) | ✅ FCT-009/010 | COMPLET | — |
| Routes d'accès au PDF (AN en priorité, replis) | ✅ FCT-011 | COMPLET | — |
| **Plafond d'emplois 156 (ETPT), notamment action 03** | ❌ LIMITE 4 (non extrait) | **INCOMPLET — à compléter au test** | La rec. n° 7 est une « priorisation » : elle se lit aussi en **effectifs**. Le DESF a 0,5 ETP (07-26). Une hausse d'ETPT sur l'action 03 ou un poste « statistique/analyse » = signal de priorisation sans ligne de crédits |
| Programmes cofinanceurs des SI (218, 349, 363) | ⚠️ LIMITE 1 (mentionnés, non extraits) | BORNÉ | Si T5 156 stable mais SI successoraux financés : chercher les lignes transverses 349/363 (facturation électronique est cofinancée) |
| Correspondance « IA Enregistrement (nom CPO) ↔ ligne budgétaire » | ⚠️ LIMITE 3 (à établir en octobre) | ATTENDU | Fait l'objet de la check-list P4 |

**Verdict de complétude : baseline CRÉDITS complète ; 2 compléments à exécuter le jour J (ETPT action 03 ; programmes cofinanceurs).** Aucune correction nécessaire des chiffres du 07-33.

## 3. RAPPEL — LE TEXTE DE LA REC. N° 7 ET SA NATURE

> **Rec. n° 7** (T1 l. 4545 et l. 12302) : « Prioriser **parmi les projets de la DGFiP** la numérisation des déclarations de succession et leur centralisation en vue notamment de leur exploitation statistique. »

**Nature (établie au 07-18)** : ce n'est PAS une demande d'argent neuf — c'est une **réallocation interne** (« parmi les projets »). Le test PLF 2027 ne doit donc pas chercher uniquement une ligne dédiée : il doit détecter **trois degrés** de prise en compte : (a) ligne/projet chiffré dédié (fort) ; (b) mention textuelle dans la justification d'action ou les dépenses pluriannuelles (moyen) ; (c) signal indirect par effectifs ou T5 action 03 (faible mais mesurable). L'absence des trois = rec. n° 7 non traduite en budget.

## 4. CHECK-LIST OPÉRATIONNELLE D'EXÉCUTION (dépôt PLF 2027, ~08/10/2026)

### Étape 0 — Acquisition du document (route AN prioritaire)

| # | Action | Détail |
|---|--------|--------|
| 0.1 | Localiser le bleu | `assemblee-nationale.fr/dyn/17/dossiers/plf2027` (index Documents budgétaires) OU pattern direct `PAP2027_BG_Gestion_finances_publiques_GA.pdf` (même pattern que 2026) |
| 0.2 | Télécharger + pdftotext | PDF programme 156 (mission « Gestion des finances publiques », ~170-180 p.) → texte brut `/tmp/pap2027_156.txt` |
| 0.3 | Repli | Wayback performance-publique.budget.gouv.fr (DNS en panne au 10/08/2026) ; budget.gouv.fr (Incapsula) ; en dernier recours : document budgétaire du Sénat (senat.fr/dossier-legislatif/plf2027) |
| 0.4 | **Nouveau — ETPT** | Extraire le plafond d'emplois du programme 156 et par action (tableau « plafond des autorisations d'emplois ») — comparer 2026 vs 2027, focus action 03 |

### Étape P1 — Totaux du programme (seuil de continuité)

| # | Vérification | Cible (baseline 07-33) | Seuil / verdict |
|---|--------------|------------------------|-----------------|
| P1 | Total AE 2027 programme 156 | 8 269 357 633 € (prévision PAP 2026) | Écart > ±5 % = signal à analyser (motif : politique budgétaire générale) |
| P1bis | Total CP 2027 | 8 294 093 638 € | idem |

### Étape P2 — Titre 5 investissement (le test SI)

| # | Vérification | Cible | Seuil / verdict |
|---|--------------|-------|-----------------|
| P2 | T5 AE 2027 | 158 635 455 € (prévision PAP 2026) | **Écart > +10 % (seuil d'analyse du dossier 07-33) = crédits SI supplémentaires — chercher la cause en P3-P7** |
| P2bis | T5 CP 2027 | 155 226 444 € | idem |

### Étape P3 — Mentions textuelles numérisation successorale (le test rec. n° 7, degré moyen)

| # | Motif grep (case-insensitive) | Lieu de recherche | Verdict |
|---|-------------------------------|-------------------|---------|
| P3a | `succession` + `numéris` | Justification action 03 « Fiscalité des particuliers » ; section « Dépenses pluriannuelles » ; présentation stratégique | Mention = degré moyen (rec. visible, financement non fléché) |
| P3b | `e-enregistrement` / `enregistrement` (service en ligne) | idem + objectifs/indicateurs de performance | Comparer à la baseline 2026 (FCT-008 : ouvert depuis 2021, extension 95 % sans droits) |
| P3c | `statistique` + `succession` / `DESF` | idem | Mention statistique = proximité avec la finalité de la rec. 7 (« exploitation statistique ») |
| P3d | `déclarations de succession` | idem | Occurrence exacte du vocabulaire de la rec. |

### Étape P4 — Projet « IA Enregistrement » (nom CPO — le test du projet spécifique)

| # | Vérification | Verdict |
|---|--------------|---------|
| P4 | Le nom « IA Enregistrement » (ou un projet SI d'enregistrement OCR/statistique) apparaît-il dans les grands projets informatiques chiffrés ? | **OUI = degré fort (le projet sort du générique)** ; NON = toujours subsumé dans les crédits génériques (constat d'absence reconduit) |

### Étape P5 — PILAT (variable de contrôle)

| # | Vérification | Verdict |
|---|--------------|---------|
| P5 | Statut 2027 du « reste à faire » (étude de cadrage annoncée au PAP 2026) ; PILAT v1 + complément toujours en trajectoire 31/12/2026 ? | PILAT est la variable de contrôle : s'il progresse normalement alors que rien n'apparaît pour la numérisation successorale, la priorisation rec. 7 n'a pas eu lieu |

### Étape P6 — Facturation électronique (variable de contrôle n° 2)

| # | Vérification | Cible |
|---|--------------|-------|
| P6 | Trajectoire 2027 (AE/CP) | 108,07 / 112,94 M€ (prévision PAP 2026) ; coût actualisé 267,72 M€ + Δ |
| P6bis | Le 1er déploiement (GE/ETI 01/09/2026) a-t-il eu lieu ? (information contextuelle, hors PAP) | Déploiement PME/TPE attendu 01/09/2027 |

### Étape P7 — Dépenses pluriannuelles : nouveaux projets chiffrés

| # | Vérification | Verdict |
|---|--------------|---------|
| P7 | La liste 2027 des dépenses pluriannuelles contient-elle un projet de numérisation successorale / enregistrement statistique (aujourd'hui : NON — seuls facturation électronique, PILAT, PAYSAGE) ? | **OUI = fil BRISÉ (rec. 7 financée)** ; NON = constat d'absence reconduit |

### Étape P7bis — Signal indirect (complément nouveau)

| # | Vérification | Verdict |
|---|--------------|---------|
| P7bis | ETPT action 03 en hausse notable 2027 vs 2026 ? | Oui sans ligne SI = priorisation en effectifs (degré faible mais réel — à croiser avec le DESF 0,5 ETP, 07-26) |

## 5. GRILLE DE VERDICT — LE TEST QUI BRISE OU CONFIRME LE FIL

| Scénario | Verdict | Conséquence corpus |
|----------|---------|--------------------|
| **S1** : P4 OUI ou P7 OUI (projet dédié chiffré « IA Enregistrement » ou numérisation successorale dans les dépenses pluriannuelles) | **FIL BRISÉ — rec. n° 7 financée** | Documenter la ligne, le montant, la trajectoire ; comparer au « quelques dizaines de M€ » du CPO (07-26) ; le fil « production absente » ne tient plus sur ce point |
| **S2** : P3a-P3d mention textuelle sans ligne (degré moyen) | **PARTIEL — rec. visible, non fléchée** | Le discours existe, le budget ne suit pas ; vérifier si une ligne apparaît au PLF 2028 (next test) |
| **S2bis** : signaux mixtes (ex. P3 mention + P7bis hausse ETPT ; P4 OUI mais non chiffré ; P3c statistique seule) | **PARTIEL — signal le plus fort** | Règle de détermination : P4/P7 > P3 > P7bis — le verdict est fixé par le signal le plus fort présent (déterministe, sans arbitraire d'exécution) |
| **S3** : aucun signal P3/P4/P7, T5 = prévision (±10 %), ETPT stables | **FIL CONFIRMÉ — rec. n° 7 non traduite** | Constat d'absence reconduit ; documenter le P5/P6 inchangés (les variables de contrôle progressent, la rec. 7 non) |
| **S4** : T5 > +10 % sans cause identifiée P3-P7 | ANALYSE APPROFONDIE | Chercher les lignes dans les programmes cofinanceurs 218/349/363 et la justification par action avant verdict |

**Anti-sycophancie** : S1 (fil brisé) n'est pas un échec — c'est le test qui marche. Si le gouvernement finance réellement la rec. n° 7 (2029-2030 « en y mettant les moyens », T1 l. 4542), le dossier doit le documenter comme une **rupture positive** du pattern d'absence, pas chercher à le minimiser.

## 6. FACT_REGISTRY

| ID | Fait | Statut | Source |
|----|------|--------|--------|
| FCT-001 | La baseline crédits du 07-33 est **complète** : totaux AE/CP 2026-2027, T5, 3 grands projets SI, mentions action 03, actions 03/09, routes d'accès — aucun chiffre à corriger (vérification de complétude effectuée) | CONFIRMÉ | 07-33 (relu) |
| FCT-002 | La baseline présente **2 compléments à exécuter au test** : plafond ETPT du programme 156 (action 03 — non extrait au 07-33, LIMITE 4) et lignes des programmes cofinanceurs (218/349/363 — bornées, LIMITE 1) | CONSTAT (compléments) | 07-33 LIMITES 1/4 |
| FCT-003 | La rec. n° 7 est une **réallocation interne** (« prioriser parmi les projets »), pas une demande d'argent neuf — le test doit donc chercher 3 degrés (ligne dédiée / mention textuelle / signal indirect) | CONFIRMÉ | 07-18 (T1 l. 4545) |
| FCT-004 | Le protocole P1-P7 est opérationnalisé : **18 points de contrôle** (0.1-0.4 : 4 ; P1/P1bis, P2/P2bis : 4 ; P3a-d : 4 ; P4, P5 : 2 ; P6/P6bis : 2 ; P7, P7bis : 2) avec lieux de recherche, motifs de grep, seuils chiffrés et grille de verdict S1-S4 | CONFIRMÉ (élaboration) | ce dossier |
| FCT-005 | Les variables de contrôle sont identifiées : PILAT (P5) et facturation électronique (P6) — si elles progressent pendant que la rec. 7 reste invisible, la non-priorisation est démontrée par contraste | CONFIRMÉ (analyse) | 07-33 + ce dossier |
| FCT-006 | Le seuil de verdict du fil est explicite : P4 OUI ou P7 OUI = fil brisé ; S3 (aucun signal) = fil confirmé | CONFIRMÉ (critère) | ce dossier |

## 7. GAPS / ACTIONS

| ID | Action | Date | Déclencheur |
|----|--------|------|-------------|
| GAP-001 | **Exécuter la check-list 0.1-0.4** (acquisition + ETPT) | ~08/10/2026 (date de dépôt à confirmer) | Dépôt PLF 2027 |
| GAP-002 | Exécuter P1-P7bis et appliquer S1-S4 | idem | Après 0.x |
| GAP-003 | Compléter la baseline ETPT (action 03) et cofinanceurs (218/349/363) | idem | Au moment du test |
| GAP-004 | Mettre à jour le 07-33, le 11-24 et le registre 27a* avec le verdict | idem | Après verdict |
| GAP-005 | Si S3 (confirmé) : programmer le test suivant au PLF 2028 | idem | Conditionnel |

## 8. LIMITES

1. Ce protocole est prêt à exécuter mais n'a pas encore été exécuté (le PLF 2027 n'est pas déposé au 10/08/2026) — il est un mode d'emploi, pas une vérification.
2. La date de dépôt exacte du PLF 2027 (~08/10/2026) est une estimation basée sur la pratique (dernier lundi de septembre / début octobre) — à confirmer à l'approche.3. Les seuils sont des choix d'analyse du corpus : ±10 % sur T5 (hérité du 07-33), **±5 % sur P1/P1bis totaux (introduit dans ce dossier — signal à analyser, pas seuil de verdict)**, pas des standards officiels.
4. L'ETPT et les cofinanceurs ne sont pas encore extraits : la baseline ETPT sera posée au moment du test (GAP-003).

## 9. LEÇON

**Le test PLF 2027 est désormais un protocole exécutable, pas une intention.** La baseline 07-33 était complète sur les crédits ; ce dossier la complète (ETPT, cofinanceurs) et transforme la check-list en 18 points de contrôle (dont la règle de détermination des signaux mixtes) avec critères de verdict objectifs. La rec. n° 7 étant une réallocation interne, le test détecte trois degrés de prise en compte — et les variables de contrôle (PILAT, facturation électronique) permettent de démontrer par contraste une éventuelle non-priorisation. Le verdict S1 (fil brisé) est un résultat légitime : le corpus a été construit pour être falsifiable.
