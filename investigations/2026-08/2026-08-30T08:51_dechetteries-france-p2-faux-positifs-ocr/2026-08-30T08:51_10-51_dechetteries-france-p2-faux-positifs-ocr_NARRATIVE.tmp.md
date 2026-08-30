# P2 — Vérifier les fac-similés OCR des faux positifs 1885/1937 (test d'antériorité)

## Objet
Sécuriser le test d'antériorité du mot « déchèterie » : confirmer au **niveau numéro** que les occurrences OCR reportées « 1885 » et « 1937 » par la passe chaîne sont bien des **faux positifs OCR**, et non de réels usages pré-1980 du mot.

## Méthode (adversaire, descendue à la racine)
La passe chaîne s'appuyait sur un balayage plein-texte **agrégé**. Cette passe P2 descend **au numéro** :
1. **SRU full-text** `gallica any "dechetterie"` → **258 records** ; scan complet = **218 parses**, dont **43 séries** à date de couverture <1980.
2. **Identification** : `dc.date any "1885"` → 1 record = **Le Petit colon algérien** (cb328359935, couverture 1877-1896) ; `dc.date any "1937"` → 1 record = **L'Éclair comtois** (cb32763706t, 1903-1939).
3. **Calibration** : ces dates sont des **couvertures de SÉRIES** de périodiques, pas des datations de contenu. Le « seuls 1885/1937 » du parent sous-estimait le balayage (43 séries) — distinction série vs numéro.
4. **Vérification issue-par-issue (ContentSearch)** :
   - Petit colon **1885** (bpt6k50017815) : `dechetterie`=**0** ; témoins `colonie`=1, `Alger`=4 ✓
   - Petit colon **1895** (bpt6k5005994q) : `dechetterie`=**0** ✓
   - Éclair comtois **1937** (bpt6k9311672p) : `dechetterie`=**0** ; témoins `Besancon`=6 ✓

## Faits
- **FCT-001 · ✧ (familie E — BnF/Gallica)** : le token OCR « dechetterie » est **absent de tous les numéros pré-1980 vérifiés** (0/0/0), témoins OCR sains. Les dates 1885/1937 proviennent de l'indexation par série (couverture pluri-annuelle), pas d'un contenu daté. **Faux positifs OCR confirmés.**

## Verdict / status
- **Test d'antériorité sécurisé** : le mot « déchèterie » est un **néologisme absent avant 1980** dans le corpus OCR libre Gallica, vérifié au niveau numéro sur le cas décisif 1885/1937.
- Aucune contradiction avec la datation Gradignan 17/11/1980.
- **CAU-001** : la cause du « 1885/1937 » est la **granularité d'indexation par série** (dc.date = couverture), effet = fausses dates de première occurrence.

## Gaps résiduels
- 43 séries pré-1980 non **toutes** inspectées au niveau numéro (échantillon 1885/1895/1937 épuise le cas central) → suite : échantillonner Spelunca 1961, Espaces et sociétés 1970, Pyrénées 1950.
- Presse quotidienne payante 1980 (Sud Ouest/RetroNews) toujours non sondée au niveau numéro : GAP INDEPENDENCE structurel, cf passe P1.