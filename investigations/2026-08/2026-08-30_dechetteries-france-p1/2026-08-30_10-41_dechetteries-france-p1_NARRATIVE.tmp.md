# P1 — Corroboration presse indépendante (Sud Ouest / RetroNews 1979-1981)

## Objet
Trouver une corroboration par la **presse quotidienne datée 1979-1985** de la revendication « première déchetterie de France à Gradignan, ouverte le 17/11/1980 », afin de rendre cette assertion indépendante de la seule famille officielle (Archives Bordeaux Métropole).

## Contexte du run
Suite du dossier `dechetteries-france` : la passe chaîne (20260830-0957) et la passe P0 (20260830-1038, lecture acte primaire) ont établi que l'acte reste **LOCALIZED** et que la corroboration presse indépendante datée 1980 était un **GAP INDEPENDENCE**. Le run P1 attaque ce gap.

## Recherches exécutées (résumé réel)
- **Gallica SRU** : recherche `dechetterie` → **258 records** (corpus global). Le **TSM** (Techniques Sciences Méthodes, revue AGHTM) ressort avec `dechetterie` + `Gradignan`.
- **Fascicule TSM septembre 1986** (ARK `bpt6k9608124h`, notice datée 1986-09-01) : ContentSearch page **395 → « Déchetterie de Gradignan »**, mention de la **Communauté Urbaine de Bordeaux**, photo légendée « Doc. ANRED ».
- **RetroNews (BnF)** : site accessible (200) mais **API 401** (clé/SPA payante) ; couverture éditoriale **~1631-1945/1951** (droit d'auteur) → **la presse de 1980 n'est PAS disponible** sur ce corpus.
- **Sud Ouest archives** : page 200 (portail payant), contenus derrière abonnement, non indexables librement.
- Conclusion d'accès : la presse quotidienne de 1980 est **structurellement inaccessible en corpus libre** (right of auteur), ce n'est pas un simple paywall contournable.

## Faits
- **FCT-001 · ✧ (famille B — presse technique)** : TSM/AGHTM septembre 1986, p.395 « Déchetterie de Gradignan » (+ C.U. Bordeaux, photo ANRED). Confirme **l'existence réelle du site** de Gradignan et sa notoriété professionnelle en 1986, comme équipement référencé — **famille indépendante des Archives BM**.

## Verdict / status
- **Existence réelle du site de Gradignan** : **renforcée** (FCT-001 ✧, seconde famille indépendante).
- **Portée « première de France, 17/11/1980 »** : **non indépendante en corpus libre** ; la corroboration presse quotidienne datée 1980 reste un **GAP INDEPENDENCE structurel** (retroNews ~1950, Sud Ouest payant).
- **CAU-001** : la barrière est structurelle (droit d'auteur → numérisation ~1950 → presse 1980 sous paywall), documentée, non contournable par web libre.

## Gaps restants
- Corroboration presse quotidienne datée 1979-1981 → requiert **accès payant** (Sud Ouest archives) ou **consultation en salle de lecture**.
- Contenu OCR plein texte de la page 395 du TSM (citation exacte) — endpoint OCR non résolu.