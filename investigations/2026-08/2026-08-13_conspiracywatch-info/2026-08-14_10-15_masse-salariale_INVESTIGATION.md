# INVESTIGATION — Masse salariale réelle vs budget déclaré de 230 k€

Date : 2026-08-14 | Heure : 10:15 CEST | Type : INVESTIGATION | Complexité : MEDIUM
Objet : recouper l'effectif salarié (IDCC 1480, journalistes) contre le budget déclaré de ~230 000 €.
Protocole : KERNEL v2.8 — vérification forensique arithmétique, primaire uniquement.
Suite de : `2026-08-14_07-26_rudy-reichstadt-comptes-verification_INVESTIGATION.md` (dont je corrige une erreur d'effectif).

---

## §0 CORRECTION MAJEURE D'UN DOSSIER ANTÉRIEUR (avant tout)

Le dossier 07-26 écrivait : « Effectif salarié (tranche) : 03 = **3 à 5 salariés** (2023) ».

**C'est FAUX.** La tranche INSEE « 03 » vaut **6 à 9 salariés**, pas « 3 à 5 ». Source officielle INSEE / API Entreprise :

> « 00 : 0 salarié ; 01 : 1 ou 2 salariés ; 02 : 3 à 5 salariés ; **03 : 6 à 9 salariés** ; 11 : 10 à 19 salariés. »

L'erreur vient de la confusion entre le **code** « 03 » et la borne « 3 ». La tranche « 3 à 5 salariés » est le code **02**.

**Conséquence directe** : l'effectif réel de l'Observatoire du conspirationnisme est **6 à 9 salariés** (année de référence 2023, Sirene), tous sous IDCC 1480 (convention collective des journalistes). C'est **presque le double** de ce que j'écrivais. Cette correction durcit, au lieu de l'affaiblir, la tension arithmétique qui suit.

---

## §1 LES TROIS CHIFFRES À RECOUPER (primaire)

| Donnée | Valeur | Source | Statut |
|---|---|---|---|
| Effectif salarié | **6 à 9 salariés** (tranche 03, année 2023) | Sirene 805407194 | ✦ |
| Convention collective | IDCC 1480 (journalistes) | Sirene | ✦ |
| Budget annuel déclaré | ~230 000 € | Reichstadt, Sénat 29/05/2023 | ✦ (déclaré, non audité) |
| Subventions publiques | 45 000 € (2023) | Annexe Jaune PLF 2023 | ✦ |
| Local | Maison des Associations du 11e (pas de loyer privé) | Sirene | ✦ |
| Financement privé « essentiel » | FMS, montant inconnu | Sénat 30/05/2023 | ✦ (flux réel, montant ⊗) |

**Point de méthode** : le budget de 230 k€ est une **déclaration**, l'effectif 6-9 est une **donnée INSEE**. Si les deux sont vrais simultanément, la masse salariale doit « tenir » dans 230 k€. C'est ce que je teste.

---

## §2 LA GRILLE IDCC 1480 (ce que coûte réellement un journaliste)

Source : grilles conventionnelles annexées à la convention collective nationale des journalistes (IDCC 1480), vérifiées à la source le 31/07/2026.

### 2.1 Minimums mensuels bruts

| Grille | Bas de grille | Haut de grille |
|---|---|---|
| PQN (presse quotidienne nationale) | 1 910 € (stagiaire 1.1) | 5 505 € (direction éditoriale 4.3) |
| PIS (presse d'information spécialisée) | 1 827 € (stagiaire) | 2 899 € (directeur de rédaction) |

**Trois dispositifs gonflent le coût au-dessus du brut de base :**
1. **13e mois OBLIGATOIRE** (article 25) : chaque journaliste perçoit en décembre une somme égale à son salaire de décembre → +8,3 % sur l'année.
2. **Prime d'ancienneté** (article 23) : +3 % (5 ans) à +11 % (20 ans de profession), cumulable avec l'ancienneté dans l'entreprise.
3. **Charges patronales** ≈ 42-45 % du brut (régime général + journaliste).

**Salaire médian constaté de la profession** : 30 000 € brut/an.

### 2.2 Coût complet par équivalent temps plein (ETP), tout compris

| Scénario | Brut annuel | + 13e mois | + charges (42 %) | Coût complet/ETP |
|---|---|---|---|---|
| SMIC (plancher légal absolu) | ~22 400 € | +8,3 % | +42 % | **~34 500 €** |
| Minimum conventionnel PIS (~2 000 €/mois) | ~24 000 € | +8,3 % | +42 % | **~37 000 €** |
| Médiane marché (30 000 €) | 30 000 € | +8,3 % | +42 % | **~46 000 €** |
| PQN production éditoriale (3 000 €/mois) | 36 000 € | +8,3 % | +42 % | **~55 000 €** |
| Direction éditoriale (Reichstadt, 4.1-4.3) | 55 000-66 000 € | +8,3 % | +42 % | **~85 000-101 000 €** |

### 2.3 Combien de salariés « tiennent » dans 230 000 € ?

| Niveau de salaire | 230 000 € ÷ coût complet | ETP finançables |
|---|---|---|
| SMIC | 230 000 ÷ 34 500 | **6,7 ETP** |
| Minimum conventionnel | 230 000 ÷ 37 000 | **6,2 ETP** |
| Médiane marché | 230 000 ÷ 46 000 | **5,0 ETP** |
| PQN mid | 230 000 ÷ 55 000 | **4,2 ETP** |

**Et c'est sans compter les coûts hors salaires** : le concours de dessin (30 000 €), l'hébergement, les frais juridiques (procédures Soral, etc.), les déplacements. Chaque euro hors salaire réduit d'autant le nombre d'ETP finançables.

---

## §3 LE RÉSULTAT : INCOMPATIBILITÉ ARITHMÉTIQUE

Les deux données INSEE et la déclaration ne sont **pas simultanément vraies à pleine valeur** :

- **6 salariés** : impossible sauf si **tous** sont au SMIC (6,7 ETP max) — or un journaliste au SMIC est **sous le minimum conventionnel** de sa catégorie dès qu'il sort du statut stagiaire. Au minimum conventionnel, 6,2 ETP consomment déjà la totalité du budget, ne laissant **rien** pour le concours et les frais.
- **9 salariés** : arithmétiquement impossible à quelque salaire que ce soit (9 × 34 500 € SMIC = 310 500 € > 230 000 €).
- **Avec Reichstadt payé en « direction éditoriale »** (4.x) : son poste seul = 85 000-101 000 € all-in, soit **37 à 44 % du budget à lui seul**. Il ne reste alors ~130-145 000 € pour 5 à 8 autres salariés + concours + frais. Impossible au niveau conventionnel.

**Trois réconciliations possibles, non exclusives :**

| Hypothèse | Lecture | Probabilité |
|---|---|---|
| **(a) Effectif en ETP ≪ headcount** : les 6-9 salariés incluent des **pigistes** (présumés salariés, L.7112-1 du Code du travail, comptés par l'INSEE) et des temps partiels | La rédaction est un noyau dur de ~3-4 permanents + une traîne de pigistes | **Élevée** (structure classique d'une petite presse en ligne) |
| **(b) Salaires au ras des minimums** : les journalistes sont payés au bas de grille, contredisant la posture d'« expertise » et de « professionnalisation » (FMS) | La « professionnalisation » revendiquée est une précarité déguisée | Moyenne |
| **(c) Budget réel > 230 k€** : financements non divulgués, dont le montant FMS (« l'essentiel » du privé) reste inconnu | Le 230 k€ déclaré est sous-évalué | Moyenne — c'est le candidat le plus lourd de conséquences |

**Aucune de ces trois hypothèses ne peut être tranchée en primaire**, car CW ne dépose aucun compte et la FMS ne publie pas le détail par bénéficiaire. Mais l'incompatibilité arithmétique, elle, est **établie et quantifiée**.

---

## §4 CE QUE CELA DÉMONTRE ET CE QUE CELA NE DÉMONTRE PAS

**Établi (✦)** :
1. L'effectif INSEE est **6 à 9 salariés** (tranche 03), pas 3-5 (correction du dossier 07-26).
2. 6-9 journalistes IDCC 1480 ne « tiennent » **pas** dans un budget de 230 k€ à salaire conventionnel ou médian.
3. Le 230 k€ n'est compatible qu'avec ≤ 6,7 ETP payés au SMIC — donc avec une rédaction **pigiste/temps-partiel** ou un budget réel **supérieur**.

**Non établi (⊗)** :
- Le budget réel (aucun compte déposé).
- Le montant FMS (« l'essentiel » du privé, inconnu).
- La répartition permanents/pigistes.
- Le salaire réel de Reichstadt.
- Toute infraction : payer ses journalistes au bas de grille n'est pas illégal, et employer des pigistes non plus.

**Le fait dur** : les trois déclarations publiques (230 k€ au Sénat, 6-9 salariés à l'INSEE, « professionnalisation » revendiquée) ne peuvent pas être toutes vraies à leur valeur faciale. L'une au moins est déformée — très probablement le **budget** (hypothèse c), ou l'**effectif en ETP** (hypothèse a). C'est une **anomalie structurelle quantifiée**, pas une accusation. Elle justifie de rouvrir la question du budget réel, exactement comme le défaut de publication des comptes la rendait déjà invérifiable.

---

## §5 SOURCES

1. INSEE / API Entreprise, nomenclature tranche d'effectif salarié — https://entreprise.api.gouv.fr/catalogue/insee/etablissements (« 03 : 6 à 9 salariés »)
2. INSEE, Transferts d'établissements (REE/Sirene) — https://www.insee.fr/fr/information/1896455
3. Sirene / recherche-entreprises.api.gouv.fr — SIREN 805407194 (tranche 03, IDCC 1480, année 2023) — https://recherche-entreprises.api.gouv.fr/search?q=805407194
4. Grille IDCC 1480, vérifiée à la source (31/07/2026) — https://salerya.fr/conventions/journalistes/ et https://www.snj.fr/les-grilles-de-salaire
5. Convention collective nationale des journalistes (IDCC 1480), Legifrance — articles 22 (minima), 23 (ancienneté), 25 (13e mois) — https://www.legifrance.gouv.fr/conv_coll/id/KALITEXT000052051868/
6. Code du travail, art. L.7112-1 (pigiste présumé salarié)
7. Sénat, audition Reichstadt Fonds Marianne (29/05/2023), budget ~230 k€ — https://www.senat.fr/compte-rendu-commissions/20230529/fin.html
8. Annexe Jaune PLF 2023 (45 000 €) — dossier 07-12, data.economie.gouv.fr
