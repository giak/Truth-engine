# ARCHIVE RNIP/ENEDIS - COMPLEXE EOLIEN DE COUFFRAU (BARRE, TARN)

Source : ODRE, dataset `registre-national-installation-production-stockage-electricite-agrege-311224`
(Registre National des Installations de Production, extraction 31/12/2024), route exports/csv, interrogée le 10/08/2026.
URL API : https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/registre-national-installation-production-stockage-electricite-agrege-311224/exports/csv

## Parc de Lacaune (commune 81124)

| idpeps | nom | MES | Puissance (kW) | Prod 2024 (kWh) | Gestionnaire |
|--------|-----|-----|----------------|-----------------|--------------|
| 17X100A100A0001A-50045296662202 | ENERTRAG LACAUNE SCS D ESCOURNADOUYRE | 02/10/2019 | 10 863 | 31 800 391 | Enedis |
| 17X100A100A0001A-50068844625016 | Confidentiel | 13/12/2017 | 13 036 | 40 207 877 | Enedis |

## Complexe de Couffrau (commune de Barre, code 81023)

| idpeps | nom | MES | Puissance (kW) | Prod 2024 (kWh) |
|--------|-----|-----|----------------|-----------------|
| RTE-COUFFE01000000000000000203 | COUFFE01 - ADP 01 (LA BESSIERE) | (vide) | 13 800 | 29 110 541 |
| RTE-COUFFE02000000000000000204 | COUFFE02 - ADP 02 (PUECH DE L HOMME) | (vide) | 16 100 | 44 185 582 |
| RTE-COUFFE03000000000000000205 | COUFFE03 - ADP 03 (MURASSON) | (vide) | 2 300 | 5 610 251 |
| RTE-COUFFE04000000000000000206 | COUFFE04 - ADP 04 (MURATEL) | (vide) | 11 500 | 25 893 276 |
| **RTE-COUFFE05000000000000006880** | **COUFFE05 - ADP 05 (PUECH DEL VERT)** | **10/05/2017** | **11 500** | **24 202 829** |
| RTE-COUFFE06000000000000006881 | COUFFE06 - ADP 06 (BOIS DE MERDELOU) | 10/05/2017 | 16 100 | 51 570 677 |

## Autres (Barre et Murat-sur-Vèbre)

| idpeps | nom | MES | Puissance (kW) | Prod 2024 (kWh) | Commune |
|--------|-----|-----|----------------|-----------------|---------|
| (non extrait) | Confidentiel | 21/02/2007 | 15 000 | 15 685 680 | Barre |
| (non extrait) | Confidentiel | 15/06/2007 | 9 000 | 5 799 083 | Barre |
| (non extrait) | Confidentiel | 31/07/2013 | 11 500 | 29 468 349 | Murat-sur-Vèbre |
| (non extrait) | Confidentiel | 31/07/2013 | 4 600 | 12 405 959 | Murat-sur-Vèbre |

## Faits consolidés

1. **COUFFE05 PUECH DEL VERT** : commune BARRE (81023), 11,5 MW, MES 10/05/2017, production 2024 = 24,2 GWh (facteur de charge ~24 %). CORRIGE le dossier 18-51 (qui disait Lacaune/MES 2012) et CONFIRME le chercheur 20-42 (MES 2017). Le nom RNIP « PUECH DEL VERT » et l'idpeps RTE-COUFFE05 confirment l'identification.
2. **COUFFE06 BOIS DE MERDELOU** : Barre, 16,1 MW, MES 10/05/2017, production 2024 = 51,6 GWh. C'est le parc objet de l'apport partiel d'actif à DAHLIA HOLDING documenté au GAP-1 (20-26) : les 2 parcs font partie du même complexe Couffrau.
3. Complexe Couffrau total : 6 ADP nominatifs = 71,3 MW (13,8+16,1+2,3+11,5+11,5+16,1) + 2 installations « Confidentiel » 2007 (24 MW) = ~95 MW à Barre.
4. Les MES des COUFFE01-04 sont vides dans le dataset agrégé 2024 (probablement des ADR/ADP plus anciens, MES 2006-2013) : cohérent avec l'hypothèse du 18-58 (parcs anciens, OA échue avant 2021).
5. Le « Confidentiel » de Lacaune (13 036 kW, MES 13/12/2017) est une installation distincte (probablement un autre parc Valeco/EnBW, nom masqué).
