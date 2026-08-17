# GAP 2 du 10-54 — Vérification des 3 publications restantes de la fiche DMTG (BdF WP 636, WID WP 2017/4, AER 2023)

- **Date** : 2026-08-10 | **Heure** : 11:13 CEST | **Type** : INVESTIGATION | **KERNEL** : v2.8
- **État** : `STATE          : FINAL`
- **Dossier** : investigations/2026-08/2026-08-13_corpus-investigations/2026-08-10_verif-3-publications-fiche-dmtg/
- **Fait suite à** : 2026-08-10_10-54_notes-france-strategie-dmtg (GAP 2) et 2026-08-10_10-31_taxopti-evrefis-publications-dmtg (GAP 3 résolu)

## 1. CONTEXTE

La fiche source CASD de l'enquête « Droits de Mutations à Titre Gratuit » (DMTG, échantillon 2010 de déclarations de succession/transmission DGFiP) liste 5 publications. Au 10-54, les 2 notes France Stratégie (n° 120 et n° 121) ont été vérifiées dans le texte : **elles n'utilisent pas l'enquête DMTG** (sources réelles : FQP 2014-2015 ; Enquêtes Emploi 2004-2019). Il restait 3 publications à vérifier dans le texte pour achever la carte des usages réels de la donnée successorale.

| # | Publication listée | Référence fiche CASD |
|---|---------------------|----------------------|
| 1 | Garbinti, Goupille-Lebret, Piketty — « Accounting for Wealth Inequality Dynamics » | BdF Working Paper n° 636 (2017) |
| 2 | Garbinti, Goupille-Lebret, Piketty — « Income Inequality in France, 1900-2014 » | WID.world WP 2017/4 |
| 3 | Bach, Bozio, Guillouzouic-Le Corff, Malgouyres — « Dividend Taxes and the Allocation of Capital: Comment » | AER 113(7), 2023, pp. 2048-52 |

## 2. OBJECT

Vérifier dans le **texte des documents** (pas les répertoires) la mention explicite de l'échantillon DMTG / des déclarations de succession 2010 dans la méthodologie de chacune des 3 publications. Achèvement de la carte des usages réels de la donnée successorale.

## 3. SOURCES LUES

- `SRC-001` : GGP2016DINA.pdf — piketty.pse.ens.fr/files/GGP2016DINA.pdf (497 Ko, PDF 61 pages, daté 26/12/2016) = **version exacte du WID.world WP 2017/4** « Income Inequality in France, 1900-2014: Evidence from Distributional National Accounts (DINA) », Garbinti, Goupille-Lebret, Piketty. Extrait texte : 81 879 octets (pdftotext -layout).
- `SRC-002` : GGP2016Wealth.pdf — piketty.pse.ens.fr/files/GGP2016Wealth.pdf (1,1 Mo, PDF 68 pages, index daté 03/02/2017) = **version de travail du papier publié ensuite comme Banque de France WP n° 636** « Accounting for Wealth Inequality Dynamics: Methods, Estimates and Simulations for France (1800-2014) », Garbinti, Goupille-Lebret, Piketty. Extrait texte : 121 533 octets (pdftotext -layout).
- `SRC-003` : Page AEA (aeaweb.org/articles?id=10.1257/aer.20221432) lue via r.jina.ai le 10/08/2026 — résumé officiel officiel du commentaire AER 113(7) 2023 pp. 2048-52 (DOI 10.1257/aer.20221432).

## 4. FACT_REGISTRY

| ID | Fait | Statut | Source |
|----|------|--------|--------|
| FCT-001 | Le WID WP 2017/4 « Income Inequality in France » (GGP2016DINA.pdf, 61 pages, 26/12/2016) ne contient **aucune** occurrence des termes DMTG, droits de mutation, mutation, gift tax, estate, succession dans son texte intégral (grep 0 résultat sur 81 879 octets ; pattern : DMTG\|droits de mutation\|mutation\|gift tax\|estate\|succession) | CONFIRMÉ | SRC-001 |
| FCT-002 | Le papier « Accounting for Wealth Inequality Dynamics » (GGP2016Wealth.pdf, 68 pages — version devenue BdF WP 636) **utilise explicitement les micro-échantillons nationaux de déclarations de succession**, dont l'année **2010** : « national micro-samples of inheritance tax returns in 1977, 1984, 1987, 1994, 2000, 2006 and 2010 (with limited sample size). We applied the estate multiplier method to the 1984-2010 samples (the 1977 file is not usable) » (l. 1092-1097) | CONFIRMÉ | SRC-002 |
| FCT-003 | La mention « estate multiplier method » (méthode multiplicateur d'échantillons fondée sur les déclarations de succession) est utilisée comme **méthode de référence avant 1970** et **appliquée aux échantillons 1984-2010** pour les décennies récentes (l. 921, 1092-1097) | CONFIRMÉ | SRC-002 |
| FCT-004 | Le commentaire AER 2023 (Bach, Bozio, Guillouzouic-Le Corff, Malgouyres) : le résumé officiel AEA ne contient **aucune mention** de DMTG, mutations, succession, inheritance ou estate ; il déclare utiliser « identical data » (les données de l'article commenté Boissel & Matray 2022, données fiscales d'entreprises FARE/FICUS) | CONFIRMÉ (résumé seul — texte intégral non lu) | SRC-003 |
| FCT-005 | La référence « DMTG » dans la fiche CASD est donc **exacte pour 1 publication sur 5** (BdF WP 636) ; parmi les 4 autres : 2 vérifiées intégralement sans mention (notes FS 120/121, dossier 10-54), 1 vérifiée intégralement sans mention (WID WP 2017/4), 1 résumé seul sans mention (AER 2023, texte intégral non lu) | CONFIRMÉ (agrégation FCT-001 à 004 + dossier 10-54) | SRC-001, SRC-002, SRC-003, 10-54 |

## 5. VERDICT

**GAP 2 du 10-54 RÉSOLU.** Sur les 5 publications de la fiche source DMTG du CASD, une seule utilise effectivement l'enquête DMTG / les déclarations de succession 2010 dans sa méthodologie : le papier « Accounting for Wealth Inequality Dynamics » (Garbinti, Goupille-Lebret, Piketty, devenu BdF WP 636) — qui applique la méthode estate multiplier aux micro-échantillons 1984-2010, dont **2010** (l'échantillon DMTG du CASD). Les 4 autres : WID WP 2017/4 (0 mention — papier sur les **revenus** DINA, pas sur les mutations), AER 2023 (résumé sans mention, données Boissel-Matray), notes France Stratégie 120/121 (déjà réfutées au 10-54).

**La carte des usages réels est désormais complète** : sur 5 publications listées par le dispositif, **1 usage avéré** (BdF WP 636) + 3 listages sans mention dans le texte vérifié intégralement (WID WP 2017/4, FS 120/121) + 1 résumé seul sans mention (AER 2023). La fiche source CASD **sur-liste** massivement : son critère de rattachement (probablement thématique) n'atteste pas l'usage de la source.

## 6. LEÇON

Renforcement du constat des 10-48 et 10-54 : **la fiche source du CASD ne peut être utilisée comme preuve d'usage d'une donnée** — 1 liste exacte sur 5 dans le cas DMTG. Le dispositif documente des rattachements thématiques sans attester l'exploitation. Ce constat structurel prolonge le fil « la donnée existe mais sa traçabilité est confinée » : même le canal officiel de documentation des usages (fiche source) ne résiste pas à une vérification dans le texte. Aucune imputation de volition au CASD.

## 7. GAPS OUVERTS

- `GAP-1` : texte intégral du commentaire AER 2023 non lu (paywall AEA + HAL bloqué par Anubis) — le FCT-004 repose sur le résumé officiel seul. Borné : le résumé ne mentionne pas la donnée.
- `GAP-2` : **RÉSOLU au 11-20 (dossier 2026-08-10_11-20_criteres-rattachement-casd)** : le critère est documenté par le dispositif — publication → projet → toutes les sources du projet (identités 19=19, 68=68, 97=97) ; la fiche source documente l'accès potentiel, pas l'usage.
- `GAP-3` : le BdF WP 636 a été vérifié sur sa version de travail (GGP2016Wealth.pdf, 03/02/2017) et non sur le PDF définitif publications.banque-france.fr (introuvable via Wayback/portail actuel) — la section données du papier définitif pourrait différer marginalement.

## 8. ÉTHIQUE

Aucune fabrication. Toutes les occurrences vérifiées par grep dans les textes extraits des PDF téléchargés en session (SRC-001, SRC-002) ou dans le résumé officiel (SRC-003). Les limites (texte intégral AER non lu, version de travail du WP 636) sont déclarées, pas masquées.
