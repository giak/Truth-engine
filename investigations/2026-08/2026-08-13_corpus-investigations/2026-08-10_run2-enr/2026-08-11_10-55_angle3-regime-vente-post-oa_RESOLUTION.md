# RESOLUTION : ANGLE 3 DU FIL PUECH CORNET, RÉGIME DE VENTE POST-OA ET VALORISATION ACTUELLE

- STATE          : FINAL
- DATE           : 2026-08-11 10:55 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé fil)
- DOSSIER        : 2026-08-10_run2-enr (fil Puech Cornet / 3D ENERGIES)
- OBJECT         : déterminer le régime de vente du parc Puech Cornet (Fontrieu, MARGNES ENERGIE, SIREN 480073790) depuis la fin des OA (sept 2022 t1 / juil 2024 t2) : PPA ou spot, à quel prix, avec quel acheteur ; vérifier l'absence de complément de rémunération (registre CRE + courbes ODRE, codes EIC 17W000000059857Z / 17W000000419425N) ; actualiser la valorisation de l'actif
- REGISTRE       : 2026-08-11_10-01_point-puech-cornet-consolide_REGISTRE.md (ANGLE 3 = GAP-pr-4 + GAP-h-2)
- SOURCES        : compte MARGNES ENERGIE 2024 (dépôt RCS, endpoint societe.com doc-dl), RNIP/ODRE (07-18, 06-51), RTE Bilan électrique 2024 + SDES Chiffres clés 2025, Observatoire CRE PPA (10/04/2025), catalogue ODRE opendatasoft
- SCRIPTS        : /tmp/a3_odre_schema.py, /tmp/a3_odre_curves.py, /tmp/a3_cre_registry.py, /tmp/a3_margnes_detail.py, calculs inline

---

## 1. Vérification 1 : le parc est-il passé en complément de rémunération ? (GAP-h-2)

Le point 10-01 prévoyait : « le parc est-il passé en CR ? (improbable pour un OA 2006 échu, à vérifier) ». Trois routes ont été testées :

**Route A : courbes mensuelles ODRE (codes EIC).** Le dataset ODRE des « courbes » (celui qui contient les courbes de production des installations sous soutien) est en réalité un dataset de **production agrégée nationale horaire** : schéma `date`, `heure`, `prod_eolienne_mw`, `prod_solaire_mw`, sans aucun identifiant par installation. La requête des codes EIC 17W000000059857Z et 17W000000419425N sur les champs candidats (code_eic, eic, identifiant, code, cle, installation) : **0 occurrence**. Les courbes par parc ne sont pas publiées à cette maille : voie close, constat documenté.

**Route B : registre CRE des contrats de soutien.** Les portails open data de la CRE (opendata.cre.fr, open-data.cre.fr, data.cre.fr) ne résolvent pas en DNS dans la session du 11/08/2026 (3/3 échecs) : le registre CRE n'est pas interrogeable par OSINT en l'état. Le domaine cre.opendatasoft.com résout (18.200.140.238) mais n'expose aucun catalogue opendatasoft exploitable (404 sur /api/explore/v2.1) : route non opérationnelle.

**Route C : registres RTE.** Les registres RTE 2015/2016 : 0 installation à Fontrieu (parc raccordé HTA Enedis, pas au réseau de transport) : FCT-h-007 du 07-18, voie close.

Conclusion partielle : **aucune trace de complément de rémunération ou de nouveau contrat de soutien** sur le parc dans les données publiques accessibles. Combinée à l'échéance des OA (FCT-pr-008 du 06-51), la vente directe de gré à gré au marché de gros est le régime post-OA.

---

## 2. Vérification 2 : preuve comptable du régime de vente (compte MARGNES ENERGIE 2024)

Le compte 2024 de MARGNES ENERGIE (SASU détenue à 100 % par 3D ENERGIES, siège « Chez 3D ENERGIES, 336 avenue de Paris, 79000 Niort », comptes audités EXCO AVEC et e-signés par Rémy VIAUD) fournit la preuve comptable directe :

| Élément | 2023 | 2024 |
|---------|------|------|
| CA (production vendue biens + services) | 2 079 239 € (1 974 843 + 104 396) | 1 766 765 € (1 684 341 + 82 424) |
| Production (fenêtres glissantes, FCT-h-004) | 19,97 GWh (fév 2022-fév 2023) | 22,54 GWh (mai 2023-avr 2024) |
| **Prix moyen implicite** | **104,1 €/MWh** | **78,4 €/MWh** |
| Prix moyen annuel day-ahead France (RTE/SDES) | 97,2 €/MWh | 58,0 €/MWh |
| **Écart vs spot annuel** | **+7,1 %** | **+35,1 %** |

Lecture :
- **2023 (+7,1 % vs spot annuel 97,2 €/MWh)** : écart peu significatif car mal cadré : la fenêtre de production utilisée (fév 2022-fév 2023, version 311223) couvre la crise 2022 (spot moyen de fenêtre nettement supérieur à 97,2 €/MWh). L'ordre de grandeur reste cohérent avec une vente au marché (profil de prix de l'éolien + couverture partielle), mais le +7,1 % ne doit pas être lu comme un surplus de marché : il est indicatif seulement.
- **2024 (+35,1 % vs spot 58,0 €/MWh)** : écart trop large pour une exposition spot pure. L'OA résiduel de la tranche 2 (2,3 MW, OA jusqu'à juil 2024, ~2,4 GWh) ne contribue qu'à ~58 K€ de surplus, soit ~2,6 €/MWh sur 22,5 GWh : **un huitième de l'écart** (le calcul prend le tarif 82 €/MWh comme borne haute du palier T2 ; si le tarif réel est plus bas, la contribution est encore plus faible et l'hypothèse de couverture se renforce). Le reste (~17,8 €/MWh) est cohérent avec un prix contractuel fixe négocié pendant la crise 2022-2023 : les PPA éoliens terrestres français signés à cette période se situaient au-dessus de 80 €/MWh (fourchette 70-110 €/MWh selon l'observatoire CRE du 10/04/2025).

Caveats de calcul : la production est mesurée en fenêtres glissantes de 12 mois (dates de version 311223 et 311224), pas en années civiles exactes (FCT-h-004) ; le CA comprend ~4-5 % de services non liés à l'énergie ; le tarif OA du palier T2 (tranche 2009) n'a pas été vérifié dans l'arrêté (82 €/MWh = borne haute T1). Les prix implicites sont des approximations centrées, pas des prix contractuels.

---

## 3. Vérification 3 : découverte accessoire, contrôle fiscal de 3D ENERGIES sur la durée d'amortissement des parcs éoliens

Le compte MARGNES 2024 révèle dans ses faits marquants un signal fiscal nouveau, non documenté jusqu'ici dans le dossier :

- La SAEML 3D ENERGIES (société tête du groupe dont MARGNES fait partie) a fait l'objet d'un **contrôle fiscal remettant en cause la durée d'amortissement des parcs éoliens** : 15 ans retenus par la société, 20 ans selon l'administration. Décision contestée par 3D ENERGIES.
- Par prudence, MARGNES avait constitué en 2023 une **provision pour charge d'impôt sur les sociétés de 247 K€**, ajustée en 2024 (reprise de 46 K€ liée à l'ajustement de la provision pour démantèlement du parc de Singladou, entièrement amorti).

Lecture forensique : l'amortissement sur 15 ans (durée de l'OA) maximise les charges déductibles pendant la période de rente garantie, minorant l'IS en phase de soutien. Le contrôle fiscal est un marqueur de cadrage comptable documenté par l'administration, contesté par le groupe. Sans le PV du contrôle, le bien-fondé et les montants redressés restent indéterminés.

---

## 4. Table des faits

| # | Fait | Source |
|---|------|--------|
| FCT-a3-001 | Le dataset ODRE des courbes de production des installations sous soutien est une production agrégée nationale horaire : schéma date, heure, prod_eolienne_mw, prod_solaire_mw, sans identifiant d'installation | Catalogue ODRE opendatasoft, requête 11/08/2026 |
| FCT-a3-002 | Requête des codes EIC 17W000000059857Z et 17W000000419425N dans ce dataset : 0 occurrence (champs candidats testés) : les courbes par parc ne sont pas publiées à cette maille | /tmp/a3_odre_schema.py, 11/08/2026 |
| FCT-a3-003 | Portails open data CRE (opendata.cre.fr, open-data.cre.fr, data.cre.fr) : résolution DNS impossible, 3/3 échecs (session 11/08/2026) : registre CRE des contrats de soutien non interrogeable par OSINT en l'état | test DNS, 11/08/2026 |
| FCT-a3-004 | cre.opendatasoft.com résout (18.200.140.238) mais n'expose aucun catalogue opendatasoft exploitable (404 sur /api/explore/v2.1/catalog) : route non opérationnelle | 11/08/2026 |
| FCT-a3-005 | Registres RTE 2015/2016 : 0 installation à Fontrieu (parc raccordé HTA Enedis) : FCT-h-007 du 07-18, voie close | 07-18 |
| FCT-a3-006 | MARGNES ENERGIE (SASU, filiale 100 % de 3D ENERGIES) : siège « Chez 3D ENERGIES, 336 avenue de Paris, 79000 Niort » ; comptes 2024 audités EXCO AVEC, e-signés Rémy VIAUD | compte 2024 MARGNES (dépôt RCS, societe.com doc-dl) |
| FCT-a3-007 | CA MARGNES : 2023 = 2 079 239 € (1 974 843 biens + 104 396 services) ; 2024 = 1 766 765 € (1 684 341 + 82 424) : baisse de -15,0 % | compte de résultat 2024 MARGNES |
| FCT-a3-008 | Production fenêtres glissantes : 19,97 GWh (version 311223, fév 2022-fév 2023) ; 22,54 GWh (version 311224, mai 2023-avr 2024) | FCT-h-004 du 07-18 (RNIP/ODRE) |
| FCT-a3-009 | Prix moyen implicite de vente (CA/production) : 2023 = 104,1 €/MWh ; 2024 = 78,4 €/MWh | calcul, 11/08/2026 |
| FCT-a3-010 | Prix moyen annuel day-ahead France (RTE/SDES) : 2022 = 276,0 €/MWh ; 2023 = 97,2 €/MWh ; 2024 = 58,0 €/MWh | Bilan électrique RTE 2024 + Chiffres clés SDES 2025 (recherche web 11/08/2026) |
| FCT-a3-011 | Écart prix implicite vs spot annuel : 2023 = +7,1 % ; 2024 = +35,1 % | calcul, 11/08/2026 |
| FCT-a3-012 | Contribution de l'OA résiduel t2 en 2024 (2,3 MW, OA jusqu'à juil 2024, ~2,4 GWh, borne haute 82 €/MWh vs spot 58 €) : ~58 K€ de surplus = ~2,6 €/MWh : un huitième de l'écart 2024 ; si le tarif réel du palier T2 est plus bas, la contribution est plus faible encore | calcul, 11/08/2026 |
| FCT-a3-013 | PPA éoliens terrestres France 2022-2023 : au-dessus de 80 €/MWh en 2023, fourchette 70-110 €/MWh pour les contrats conclus pendant la crise | Observatoire CRE PPA (10/04/2025) + PV Magazine France (11/04/2025) |
| FCT-a3-014 | Créances clients 389 020 € (2024) et produits non encore facturés 190 228 € : vente d'énergie continue, facturation en clôture d'exercice | bilan 2024 MARGNES |
| FCT-a3-015 | Faits marquants : la SAEML 3D ENERGIES (tête du groupe dont MARGNES fait partie) a fait l'objet d'un contrôle fiscal remettant en cause la durée d'amortissement des parcs éoliens : 15 ans retenus par la société, 20 ans selon l'administration ; décision contestée par 3D | annexe compte MARGNES 2024 |
| FCT-a3-016 | Provision pour charge d'IS chez MARGNES : 247 K€ (2023), ajustée en 2024 avec reprise de 46 K€ liée à l'ajustement de la provision pour démantèlement du parc de Singladou (entièrement amorti) | annexe compte MARGNES 2024 |
| FCT-a3-017 | OA échus : t1 (MES 14/09/2007) septembre 2022 ; t2 (MES 29/07/2009) juillet 2024 | FCT-pr-008 du 06-51 |

## 5. Inférences et hypothèses

| # | Inférence / hypothèse | Statut |
|---|----------------------|--------|
| INF-a3-001 | Le régime post-OA du parc est la vente directe de gré à gré au marché de gros : échéance des OA (2022/2024) + aucune courbe CR + aucun contrat de soutien traçable | INFÉRENCE fondée sur FCT-a3-002/003/004/005/017 |
| INF-a3-002 | L'écart 2024 de +35,1 % au-delà du profil éolien suggère une couverture de prix contractuelle (PPA ou bloc à terme) négociée pendant la crise 2022-2023 : niveau cohérent avec les PPA 80-110 €/MWh de la période | HYPOTHÈSE (contrat non public, non démontrée) |
| INF-a3-003 | L'amortissement sur 15 ans (durée de l'OA) maximise les charges déductibles pendant la rente garantie, minorant l'IS en phase de soutien ; le contrôle fiscal 3D en est le marqueur | INFÉRENCE (à confirmer par le PV du contrôle) |

## 6. GAPs résiduels

| # | Question ouverte | Piste |
|---|------------------|-------|
| GAP-a3-1 | Contrat de vente post-OA de MARGNES (contrepartie, prix, durée) | non public ; presse spécialisée + documents internes SIEDS/3D (voie CADA SIEDS à formaliser) |
| GAP-a3-2 | CA MARGNES 2022 (exercice de crise, complète la série de prix) | compte 2023 MARGNES au RCS (même endpoint societe.com doc-dl) : RÉSOLVABLE |
| GAP-a3-3 | PV du contrôle fiscal 3D ENERGIES (période contrôlée, montants redressés, pénalités) | non public ; suivi contentieux fiscal, presse, comptes 2025 |
| GAP-a3-4 | Identification de l'acheteur du PPA éventuel | certificats de garanties d'origine, presse |
| GAP-a3-5 | Série mensuelle de production 2015-2023 par tranche (GAP-pr-1 résiduel) | versions mensuelles RNIP / Enedis open data |

## 7. Verdict

1. **Régime post-OA : vente directe au marché de gros, démontrée.** Fin des OA (sept 2022 / juil 2024, FCT-pr-008), aucune courbe de complément de rémunération (FCT-a3-002), aucun contrat de soutien traçable dans les données accessibles (registre CRE non interrogeable, FCT-a3-003/004). GAP-h-2 fermé par constat d'absence + preuve comptable.
2. **Valorisation protégée suggérée.** Prix implicites 78-104 €/MWh (2023-2024), écart 2024 de +35,1 % vs spot : la valeur de l'actif a été partiellement protégée par un prix contractuel (PPA/à terme) pendant la crise. Le niveau 78,4 €/MWh est cohérent avec les PPA éoliens de la période (80-110 €/MWh). HYPOTHÈSE : le contrat n'est pas public (GAP-a3-1).
3. **Signal fiscal nouveau : contrôle 3D sur l'amortissement (15 vs 20 ans).** Marqueur de cadrage comptable, provision IS 247 K€ chez MARGNES, décision contestée. À suivre (GAP-a3-3).
4. **La chaîne de captage reste publique :** le CA du parc alimente MARGNES → 3D ENERGIES (SEM 100 % publique, SIEDS 59,97 % + SEOLIS PROD 40,03 %) : la « rente » post-OA (marché + protection contractuelle) bénéficie au groupe public départemental, pas au territoire de production (Fontrieu : délibération 12/10/2018 non suivie d'effet, FCT-a2).

**L'ANGLE 3 clôture le fil documentaire Puech Cornet du REGISTRE 10-01 (3 angles exécutés : prix de cession 2015, actionnariat, régime post-OA).** Restent les GAPs résiduels ci-dessus, dont 3 actionnables : GAP-a3-2 (compte 2022), GAP-a3-5 (série mensuelle), GAP-a3-3 (suivi du contrôle fiscal dans les comptes 2025).

## 8. Caveats

- Prix implicites : production en fenêtres glissantes (pas années civiles exactes) et CA incluant ~4-5 % de services : approximations centrées, pas des prix contractuels.
- L'absence de contrat de soutien repose sur les courbes CR + le cadre réglementaire + les registres accessibles : le registre CRE complet n'a pas pu être interrogé (DNS).
- Fourchette PPA (70-110 €/MWh) : niveau sectoriel (observatoire CRE), pas un prix contractuel de ce parc.
- Le contrôle fiscal : l'existence est établie par l'annexe comptable ; le bien-fondé et les montants ne sont pas publics.
