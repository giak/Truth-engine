# REGISTRE : POINT CONSOLIDÉ DU FIL VALECO/ENBW (PISTE ENR, AXE A)

- STATE          : FINAL
- DATE           : 2026-08-10 21:39 CEST (wall-clock réel)
- TYPE           : REGISTRE (point consolidé)
- DOSSIER        : 2026-08-10_run2-enr
- OBJECT         : faire le bilan du faisceau souveraineté Valeco/EnBW après les documents de la soirée : est-il complet ? Quels sont les 3 prochains angles ?
- PERIMETRE      : 6 documents de la soirée (20-42, 21-10, 21-30, 21-36, 21-50, 22-05) + héritage (18-58, 20-26, 20-36, 18-30, 18-51)
- [§CAVEAT-HORODATAGE-NOM-DISCREPANT-vs-wall-clock-reel] : l'heure wall-clock à la rédaction est 21:39 CEST. Les fichiers `21-50` et `22-05` portent des timestamps postérieurs à l'heure réelle de leur création (anomalie d'horodatage de session, sans impact sur le contenu, à corriger à la prochaine session si besoin).

---

## 1. INVENTAIRE DES 6 DOCUMENTS DE LA SOIRÉE

| # | Document | Objet | FCT | Verdict clé |
|---|----------|-------|-----|-------------|
| 1 | `20-42_flux-subvention-pdv-mecanique-prix_INVESTIGATION.md` | Flux de soutien PDV + mécanique du prix | 15 FCT-flux | Micro : flux net -4,82 M€ (État perçoit au net) ; méso Valeco ~21,7 M€/an d'écart au marché ; macro : 87 Md€ d'engagements + mécanique de prix = vrai transfert structurel |
| 2 | `21-10_gap4-contrefactuel-prix-2022_INVESTIGATION.md` | Contrefactuel prix 2022 (couplage européen) | 17 FCT-g4 | **Thèse « le couplage impose le prix allemand » RÉFUTÉE pour 2022** : prix FR 276 > DE 235, convergence 24 %, cause = pénurie nucléaire nationale ; charges réelles = CRIM non captée (0,4/12,3 Md€) + bouclier non recapté (21,5 Md€) |
| 3 | `21-30_gap-flux-1-regime-oa-pdv_RESOLUTION.md` | Régime OA exact PDV (RNIP/Enedis, arrêtés) | 15 FCT-oa | **Corrections** : PDV à BARRE (pas Lacaune), MES 10/05/2017 (pas 2012), OA jusqu'en 2032 ; T1 = 82 €/MWh dans les deux arrêtés ; flux recalculé -5,64 M€ (État perçoit) ; BOIS DE MERDELOU = parc jumeau du même complexe (apport DAHLIA) |
| 4 | `21-36_gap1-affectations-valeco-ren_RESOLUTION.md` | Affectations VALECO REN 2023-2025 (GAP-dv-1) | 16 FCT-dv1 | **PV d'AG non déposés (SAS)** ; reconstitution delta FP : **~31,3 M€ distribués 2023-2025 (pic 26,8 M€ en 2023)**, 4× l'estimation du 21-50 ; BFR 23,1 M€ résorbé = dividendes filiales encaissés |
| 5 | `21-50_dividendes-valeco-enbw-capitaux-oa_INVESTIGATION.md` | Dividendes VALECO REN → EnBW + valeur capitalisée OA | 15 FCT-dv | Estimation 2-3 M€/an (CORRIGÉ par 21-36) ; valeur capitalisée OA = 168-225 M€, cohérente avec prix 229 M€ (2019) |
| 6 | `22-05_gap2-sortie-mirova-klimavest_RESOLUTION.md` | Sortie MIROVA EUROFIDEME 3 (GAP-dv-2) | 14 FCT-mv | **Cession 49 % à KlimaVest ELTIF (Commerzbank) en nov. 2022** ; chaîne du capital **100 % allemande depuis 11/2022** : EnBW 51 % + Commerzbank 49 % |

Total : 92 FCT sur la soirée (15+17+15+16+15+14).

---

## 2. LE FAISCEAU SOUVERAINETÉ : EST-IL COMPLET ?

### 2.1 La chaîne du capital : COMPLÈTE ✅

```
PARCS (PDV, Bois de Merdelou, Ensinet, Fenouilledes, Bruyère, Chaussée, Tuchanais, solaires...) = 169 MW
        │
        ▼
VALECO REN (434054318) : holding pure de dividendes (CA 1,51 K€, RN 75,3 M€ en 2022)
  51 % VALECO SAS (421377946) → EnBW AG (Land Bade-Wurtemberg, ~99 % public allemand)
  49 % KlimaVest ELTIF → Commerz Real → Commerzbank (Allemagne)
```

- Chaque maillon est **documenté à la source** : SIREN (recherche-entreprises API), actes RCS (Pappers/INPI), communiqués (EnBW, De Pardieu, CDC).
- **Correction du 18-58/21-50** : le FPCI français MIROVA (sphère CDC/BPCE) est sorti en nov. 2022 au profit d'un fonds allemand : **le capital est 100 % allemand depuis 2022**, pas « 51 % allemand + 49 % français ».
- Structure SPV par parc confirmée (pas de société « Couffrau » au RNE).

### 2.2 Le flux public : COMPLET ✅ (avec limite de quantum)

| Segment | Chiffrage | Statut |
|---------|-----------|--------|
| Micro (parc PDV, 2017-2031) | **-5,64 M€ net (l'État PERÇOIT)** | RÉSOLU (RNIP prod réelle 24,2 GWh) |
| Méso (portefeuille Valeco 332 MW) | ~21,7 M€/an d'écart au marché (subvention nette) | RÉSOLU (ordre de grandeur) |
| Capitalisation OA rachetés (2019) | **168-225 M€**, cohérent avec le prix de 229 M€ | RÉSOLU (recoupement prix) |
| Macro (87 Md€ engagements FR) | Part EnBW marginale (332 MW sur ~30 GW) | RÉSOLU (ne pas attribuer à EnBW) |
| Dividendes VALECO REN 2023-2025 | **~31,3 M€ distribués** (26,8 M€ en 2023), dont ~16 M€ vers EnBW | RÉSOLU (reconstitution, pas pièce directe) |

- **Correction majeure de la soirée (21-36)** : le flux de dividendes est **4× plus élevé** que l'estimation initiale du 21-50 (2-3 M€/an → 31,3 M€ cumulés, concentré en 2023).
- **Limite de quantum restante** : montant de la cession MIROVA → KlimaVest (GAP-mv-1, non public) et remontée exacte des filiales parcs (GAP-dv-3).

### 2.3 La mécanique de prix : COMPLÈTE ✅ (avec réfutation honnête)

- La thèse utilisateur « l'Europe UERSS corrompue impose le prix allemand » est **RÉFUTÉE pour 2022** à la source (prix FR 276 > DE 235 €/MWh, convergence FR-DE 24 %, cause = 65 % du nucléaire à l'arrêt).
- Les charges réelles mesurées : **CRIM non captée (0,4/12,3 Md€) + bouclier tarifaire non recapté (21,5 Md€)** : le vrai trou de contrôle, pas les dividendes Valeco.

### 2.4 La qualification juridique : COMPLÈTE ✅ (0 corruption pénale)

| Qualification | Verdict |
|---------------|---------|
| Corruption / prise illégale d'intérêts (fil Valeco) | **0 fait établi** ; seul cas pénalisé du périmètre = Cabrol/Lacaune (17/10/2023, sans enrichissement, promoteur relaxé) et le parc réel est à Barre (correction 21-30) |
| Favoritisme / concurrence | 0 signal (marchés publics non concernés : OA = guichet réglementé) |
| Transfert de souveraineté | **ÉTABLI et QUANTIFIÉ** : rente publique française → actionnaires publics allemands (EnBW Land BW + Commerzbank) |
| Pantouflage | 1 confirmé hors fil (Bohuon CRE→EDF, contrôle HATVP fonctionnel) |

**Verdict du faisceau : le fil Valeco/EnBW est COMPLET dans sa structure (capital, flux, qualification). Ce qui reste ouvert n'est plus structurel mais quantitatif (montants de cession, remontée par filiale) et documentaire (pièces directes d'affectation).**

---

## 3. LES 3 PROCHAINS ANGLES ACTIONNABLES

### ANGLE 1 : GAP-dv-3, les dividendes des filiales parcs (la source des 23,1 M€ de créances 2022)

- **Question** : quelles filiales (PDV, Bois de Merdelou, Ensinet, Fenouilledes...) ont remonté les ~23,1 M€ de dividendes à VALECO REN en 2022, et à quel rythme depuis ?
- **Voie** : comptes déposés des SARL parcs (grep SIREN 495300600 / 494229396 + les 20+ filiales identifiées), bilans 2022-2025, agrégats Pappers/API recherche-entreprises (la méthode delta FP validée sur VALECO REN s'applique à chaque parc).
- **Rentabilité** : haute. Ferme le dernier maillon de la pompe (parc → holding) et quantifie la contribution de chaque parc au flux vers l'Allemagne. Le Bois de Merdelou (51,6 GWh, 16,1 MW) est le plus gros générateur du complexe Couffrau.

### ANGLE 2 : GAP-mv-1 + GAP-mv-3, le montant de la cession MIROVA → KlimaVest et la liste des 9 parcs

- **Question** : combien KlimaVest (Commerzbank) a-t-il payé les 49 % en 2022 ? Quels sont les 9 parcs éoliens + 1 solaire (169 MW) exacts ?
- **Voie** : comptes/rapports annuels du fonds Eurofideme 3 (NAV, valorisation), presse spécialisée allemande (Fondsprofessionell, invesment), recoupement RNIP (les COUFFE01-06 + autres ADP Valeco identifiables par commune).
- **Rentabilité** : moyenne. Chiffrerait la 2e monétisation (après EnBW 2019) de la subvention publique capitalisée, vers un 2e acteur public allemand. Liste des 9 parcs = cartographie complète de la base de dividendes.

### ANGLE 3 : GAP-oa-1/GAP-oa-2, verrouiller le flux net PDV (heures T2 + date de raccordement)

- **Question** : le T2 (années 11-15, 2027-2032) dépend des heures de fonctionnement (28 à 82 €/MWh) : la production RNIP (~2 100 h) suggère un T2 faible, mais à vérifier. La date de la demande complète de raccordement tranche 2008 vs 2014 (même T1 = 82 €/MWh, impact sur le T2).
- **Voie** : RTE (registre de production horaire), registre des contrats OA (CRE/EDF OA), demande d'accès numérique (pas de papier).
- **Rentabilité** : moyenne. Verrouille le chiffre du 20-42/21-30 (-5,64 M€ net) qui est la pièce maîtresse anti-sycophancie du fil (le parc ne vole pas le contribuable au net).

---

## 4. SYNTHÈSE DU FAISCEAU (réponse à la question)

**Le faisceau souveraineté Valeco/EnBW est COMPLET dans sa structure.** Les 6 documents de la soirée bouclent :

1. **Qui détient** : 100 % allemand depuis 11/2022 (EnBW 51 % + Commerzbank 49 %), chaque maillon sourcé.
2. **Quel flux** : OA 82 €/MWh jusqu'en 2032, capitalisation 168-225 M€ monétisée dès 2019 (prix 229 M€), dividendes ~31,3 M€ distribués 2023-2025 (26,8 M€ en 2023).
3. **Quelle qualification** : transfert de souveraineté légal et quantifié, **0 corruption pénale**, mécanique de prix à charge réelle ailleurs (CRIM 0,4/12,3 Md€).

**Corrections majeures de la soirée à retenir** :
- 21-30 : PDV à Barre, MES 2017, OA jusqu'en 2032 (corrige 18-51/18-58).
- 21-36 : dividendes réels ~31,3 M€, pas 7,52 M€ (corrige 21-50).
- 22-05 : capital 100 % allemand (complète 18-58/21-50).
- 21-10 : thèse couplage réfutée pour 2022 (contre la piste initiale).

**Ce qui ne sera jamais public** : les PV d'AG (SAS, non déposés) et le montant de la cession 2022 (fonds professionnels). Les angles 1-3 ci-dessus sont les dernières voies quantitatives avant saturation du fil aux données ouvertes.

---

## 5. TRAÇABILITÉ

- Liens : 18-58 (chaîne), 20-26 (GAP-1, 75,3 M€), 20-36 (GAP-5, CDC TRI 28 %), 18-30 (SIREN PDV), 18-51 (carte Tarn, corrigé), 17-52 (SPV), point 18-53 (bilan global piste ENR)
- Em-dash : 0 (vérifié)
- Caveat : timestamps 21-50/22-05 postérieurs au wall-clock de cette session (voir en-tête)
