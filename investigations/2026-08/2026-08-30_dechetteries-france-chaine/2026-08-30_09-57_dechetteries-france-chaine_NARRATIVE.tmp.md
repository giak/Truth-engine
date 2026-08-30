# Passe KERNEL UPDATE certifiée — La chaîne consolidée des déchetteries en France

RUN_ID : 20260830-0957-dechetteries-france-chaine · PARENT_RUN_ID : 20260830-0927-dechetteries-france-histoire
AS_OF : 2026-08-30 · INPUT_KIND : UPDATE (revalidation différentielle) · MISSION_MODE : INVESTIGATION

## 1. La chaîne consolidée

La genèse du réseau des déchetteries en France se décompose en trois maillons vérifiés, chacun ancré dans une famille de preuve distincte :

1. **Gradignan, 17/11/1980 — le dépôt fixe pionnier** (FCT-001). La source amont — le service d'archives de Bordeaux Métropole, panneau de l'exposition « La gestion des déchets dans la Cub » — déclare textuellement : « ouverture de la première déchetterie en France à Gradignan le 17 novembre 1980 ». Cette page a été **inspectée** via le snapshot Wayback du 24/05/2024 (site live bloqué par anti-bot Anubis). Nature : document officiel du dépositaire (tier T2). La revue professionnelle TSM (juillet 1985) présente « l'expérience de la Communauté Urbaine de Bordeaux, celle d'une déchetterie » comme référence nationale (SRC-005) : corroboration indirecte de famille (AGHTM ≠ Archives BM).

2. **1987 — le néologisme-marque ANRED** (FCT-002, FCT-006). Le mot « déchetterie » est un néologisme + marque déposée par l'ANRED en 1987 (concept d'apport volontaire, licence) ; l'orthographe à un seul « t » a été validée par l'Académie française (panneau d'Escolives, 1990). L'ANRED (créée 1976, loi 75-633) puis l'ADEME (fusion 1990/91, active 01/01/1992) déclarent avoir inventé les déchetteries : l'invention est **étatique**, antérieure à la diffusion massive du réseau.

3. **1990-2009 — la massification** (FCT-004). L'annuaire SINOE/ADEME (saisie 2026, dataset primaire téléchargé et analysé) recense **4 630 sites**, dont 2 058 ouverts dans les années 1990 et 2 371 dans les années 2000 (pic) : ~90 % du réseau courant a été construit entre 1990 et 2009, après la loi n° 92-646 (13/07/1992) imposant dès le 01/07/2002 l'admission des seuls déchets ultimes en décharge (CAU-001, enabler documenté).

## 2. Ce qui change par rapport au parent

- **FCT-001 passe de revendication relayée à T2 INSPECTED** : la source amont (Archives BM) a été inspectée textuellement ; corroboration indirecte TSM 1985 ajoutée (famille B).
- **Acte primaire localisé** (FCT-003) : la délibération CUB de 1980 se trouve dans le fonds **BXM 511 W** « Délibérations de la communauté urbaine de Bordeaux (1967-2003) », notice « Délibérations de 1980 » (view:8586), registres numérisés **PDF avec OCR** (1 028 registres, 373 275 pages, recherche plein-texte) ; tables index BXM 27 W (1967-1999). Statut : **LOCALIZED, pas encore INSPECTED** (Anubis bloque la lecture automatique ; l'actualité officielle du 15/04/2025 confirme la mise en ligne).
- **Preuve textuelle « comment c'était avant »** (FCT-005) : TSM janvier 1971 (article J. Rougier sur Grenoble) — « le ramassage des déchets encombrants est assuré par deux bennes à ordures traditionnelles qui opèrent chaque jour dans un quartier différent ». En 1971, la collecte était **mobile et tournante**, sans lieu fixe de dépôt : le modèle déchèterie n'existait pas.
- **Les 9 sites SINOE avec D_OUV < 1980 sont neutralisés** (FCT-007) : 2 « Déchèteries Mobiles » du Jura (21/10/1974) correspondent à la création du syndicat SICTOM du Haut-Jura (les fixes datent des années 1990, déclaration officielle du gestionnaire) ; 6 dates rondes au 01/01 sont des valeurs par défaut d'enquête ; 1 date aberrante (Toulouse 1884). Le champ D_OUV est déclaratif depuis 2005 (enquêtes bisannuelles) — non fiable au jour près.

## 3. Test adversaire et limites

- **Test d'antériorité** (réfutation FCT-001) : sur ~300 documents OCR Gallica contenant « dechetterie », aucun daté entre 1937 et 1985 ; les seuls 1885/1937 sont des faux positifs OCR ; le même corpus contient des centaines d'occurrences « encombrants » en 1971-1979 — l'absence du mot n'est pas un artefact de couverture.
- **Limites explicites** : corroboration indépendante datée 1980-85 impossible dans les corpus libres (RetroNews et Sud Ouest payants) → GAP INDEPENDENCE (LED-003) ; acte primaire non lu → GAP ACCESS (LED-001).
- **Verdict** : la chaîne Gradignan 1980 → néologisme 1987 → réseau 1990-2009 est **MAINTAIN** (renforcée), avec deux gaps typés explicites. Rien dans SINOE, Gallica ou les sources locales ne la conteste.

## 4. État du dossier

- 7 faits revalidés (4 ✦, 3 ✧), 10 sources, 3 réfutations exécutées (toutes NONE), 4 LED (2 SATURATED, 2 GAP typés), 7 axes, 6 claims, 1 CAU (GAP CAUSALITY).
- Sections : TEMPORAL_STATE, SCOPING_REPORT, CREDO, COGNITIVE_MAP, DIALECTICAL_MAP, RESOURCE_FLOW_MAP, ACTOR_NETWORK_MAP, IMPACT_MAP, CONTRADICTION_LEDGER, VERIFICATION_REPORT, EDI_REPORT, RESPONSIBILITY_MAP, NEXT_QUERIES, MANIPULATION_REPORT.
