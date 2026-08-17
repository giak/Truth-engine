# Quintessence : Vérification des 3 publications restantes de la fiche DMTG : 1 usage avéré sur 5, la fiche source CASD sur-liste massivement

Source : `investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_verif-3-publications-fiche-dmtg/2026-08-10_11-13_verif-3-publications-fiche-dmtg_INVESTIGATION.md` (50 lignes, 5 FCT-001..005)
Date extraction : 2026-08-13 05:00 CEST
Pilote : Buffy (FreeBuff) : Sublimator v36 Phase 1 (corpus complet, lot bloc DMTG/BNDP/CDC)

---

## 1. Métadonnées & trace source

- **Autorité** : KERNEL v2.8, format léger, axe anticorruption, bloc connaissance patrimoniale (DMTG)
- **Date source** : 2026-08-10 11:13 CEST, STATE FINAL
- **Identifiants source** : 5 FCT-001..005
- **Object** : vérifier dans le texte des documents (pas les répertoires) la mention explicite de l'échantillon DMTG / des déclarations de succession 2010 dans la méthodologie des 3 publications restantes de la fiche source DMTG du CASD
- **Verdict source** : la carte des usages réels est complète : sur 5 publications listées, 1 usage avéré (BdF WP 636) ; la fiche source CASD sur-liste massivement (rattachement thématique, pas preuve d'usage)

## 2. Faits atomiques préservés

- FCT-001 : le WID WP 2017/4 « Income Inequality in France » (GGP2016DINA.pdf, 61 pages, 26/12/2016) ne contient AUCUNE occurrence des termes DMTG, droits de mutation, mutation, gift tax, estate, succession (grep 0 sur 81 879 octets) [L32 (mesuré)]
- FCT-002 : le papier « Accounting for Wealth Inequality Dynamics » (GGP2016Wealth.pdf, 68 pages, devenu BdF WP 636) utilise explicitement les micro-échantillons nationaux de déclarations de succession, dont l'année 2010 : « national micro-samples of inheritance tax returns in 1977, 1984, 1987, 1994, 2000, 2006 and 2010 [...] We applied the estate multiplier method to the 1984-2010 samples » (l. 1092-1097) [L33 (mesuré)]
- FCT-003 : la méthode estate multiplier (méthode multiplicateur fondée sur les déclarations de succession) est la méthode de référence avant 1970 et appliquée aux échantillons 1984-2010 (l. 921, 1092-1097) [L34 (mesuré)]
- FCT-004 : le commentaire AER 2023 (Bach, Bozio, Guillouzouic-Le Corff, Malgouyres) : le résumé officiel AEA ne contient aucune mention de DMTG/mutations/succession ; il déclare utiliser « identical data » (données fiscales d'entreprises FARE/FICUS de l'article commenté) : résumé seul, texte intégral non lu [L35 (mesuré)]
- FCT-005 : la référence DMTG dans la fiche CASD est exacte pour 1 publication sur 5 (BdF WP 636) ; parmi les 4 autres : 2 vérifiées intégralement sans mention (notes FS 120/121, dossier 10-54), 1 vérifiée intégralement sans mention (WID WP 2017/4), 1 résumé seul sans mention (AER 2023) [L36 (mesuré)]

## 3. Acteurs nominaux

**Institutions** : CASD (fiche source), Garbinti, Goupille-Lebret, Piketty (WID.world, PSE), Bach, Bozio, Guillouzouic-Le Corff, Malgouyres (IPP/CREST), AEA, France Stratégie, Banque de France.

## 4. Sources externes citées

GGP2016DINA.pdf (piketty.pse.ens.fr), GGP2016Wealth.pdf (version de travail BdF WP 636), page AEA (DOI 10.1257/aer.20221432), dossier 10-54 (notes France Stratégie 120/121).

## 5. Chronologie datée

26/12/2016 : WID WP 2017/4 (61 p.) ; 03/02/2017 : GGP2016Wealth.pdf (index) ; 06/2017 : BdF WP 636 ; 2023 : AER 113(7) 2023 pp. 2048-52 ; 10/08/2026 : vérification textuelle (grep).

## 6. Mécanismes / chaînes causales

**M1  :  La preuve textuelle par grep** : l'usage d'une donnée se vérifie dans le texte de la méthodologie, pas dans les répertoires : 0 occurrence DMTG dans le WID WP 2017/4 (papier sur les revenus DINA), mention explicite des micro-échantillons 1984-2010 dans le WP 636. Force : EXTRÊME. Niveau : L1. [L32-L34 (mesuré)]
**M2  :  La sur-liste du dispositif** : la fiche source CASD liste 5 publications dont 1 seule utilise réellement la donnée : son critère de rattachement (probablement thématique : publication → projet → toutes les sources du projet, résolu au 11-20) n'atteste pas l'usage. Force : EXTRÊME. Niveau : L1. [L36 (mesuré)]
**M3  :  La frontière du vérifiable** : le commentaire AER 2023 reste borné au résumé officiel (paywall AEA, HAL bloqué) : FCT-004 marqué « résumé seul ». Force : HAUTE. Niveau : L2. [L35 (mesuré)]

## 7. Verbatim et citations

- « La fiche source du CASD ne peut être utilisée comme preuve d'usage d'une donnée : 1 liste exacte sur 5 dans le cas DMTG » [L38 (mesuré)]
- « Le dispositif documente des rattachements thématiques sans attester l'exploitation. Ce constat structurel prolonge le fil "la donnée existe mais sa traçabilité est confinée" : même le canal officiel de documentation des usages (fiche source) ne résiste pas à une vérification dans le texte » [L39 (mesuré)]

## 8. Notes méthodologiques source

- **Fiabilité** : occurrences vérifiées par grep dans les textes extraits des PDF téléchargés en session (sources primaires) ou dans le résumé officiel (AEA) ; aucune fabrication, limites déclarées.
- **F-##** : 5/5 identifiants FCT-001..005 préservés verbatim.
- **Méthode** : vérification textuelle intégrale (pdftotext -layout + grep), agrégation avec le dossier 10-54, achèvement de la carte des usages.

## 9. Limites connues (case-limites)

- Texte intégral du commentaire AER 2023 non lu (paywall AEA + HAL bloqué par Anubis) : FCT-004 borné au résumé officiel.
- Le BdF WP 636 a été vérifié sur sa version de travail (GGP2016Wealth.pdf, 03/02/2017), pas sur le PDF définitif publications.banque-france.fr (introuvable).
- Le critère de rattachement CASD a été résolu au dossier 11-20 (publication → projet → sources du projet).
