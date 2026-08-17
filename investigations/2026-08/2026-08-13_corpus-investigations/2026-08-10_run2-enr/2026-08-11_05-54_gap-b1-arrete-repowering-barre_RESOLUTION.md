# RESOLUTION : GAP-b-1 : L'ARRETE PREFECTORAL DU REPOWERING DE BARRE TROUVE (RUBRIQUE OFFICIELLE tarn.gouv.fr, CHAINE 2017-2026)

- STATE          : FINAL
- DATE           : 2026-08-11 05:54 CEST
- TYPE           : RESOLUTION (GAP-b-1 du document 05-40 ANGLE B, KERNEL v2.8)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, ANGLE B de la stratégie 04-56)
- OBJECT         : résoudre le GAP-b-1 : trouver l'arrêté préfectoral du repowering de Barre dans le RAA du Tarn et les archives tarn.gouv.fr 2024-2026, compléter le constat d'absence partiel (pages 1-4 sur 28)
- METHODE        : découverte du mécanisme de pagination SPIP (offset), scan complet des 28 pages de la rubrique « Arrêtés d'autorisation », identification des SPV via API Recherche Entreprises, lecture intégrale de 2 articles La Dépêche (01/02/2025, 19/07/2023) + rappel 27/06/2026
- HASHS          : vérifiés (0 em-dash, nomenclature FCT-b1)

## Verdict

**Le GAP-b-1 est RESOLU : l'arrêté préfectoral du repowering existe, est publié, et porte la date du 16/05/2023.** Le constat d'absence partiel du 05-40 (FCT-b-016) est CORRIGÉ : le problème n'était pas l'absence d'arrêté mais le mécanisme de pagination (SPIP `(offset)/N`, pas `?page=N`) qui avait fait renvoyer la page 1 pour toutes les requêtes.

**Chaîne probatoire complète du repowering (2017-2026)** :
1. **2017** : Valeco dépose sa demande de repowering (La Dépêche 19/07/2023 : « c'est en 2017 que Valéco a déposé sa demande de Repowering »)
2. **16/05/2022** : arrêté d'autorisation environnementale « Cambert énergie, à Barre et Murat-sur-Vèbre » (rubrique officielle tarn.gouv)
3. **16/05/2023** : arrêté d'autorisation environnementale « Ferme éolienne de Puech Cambert, Barre » (rubrique officielle tarn.gouv)
4. **12/07/2023** : visite du préfet Lauch sur le site (Combaynart/Puech de Cambert), guidé par Daumard (président Valeco), avec Vidal (maire de Barre), Berly (DREAL Occitanie), président CdC (La Dépêche 19/07/2023)
5. **08/2024** : démarrage du chantier de renouvellement sur Barre et Murat-sur-Vèbre (La Dépêche 01/02/2025)
6. **11/06/2026** : inauguration des 8 nouvelles éoliennes (La Dépêche 27/06/2026, déjà documenté 05-40)

## Table des faits (FCT-b1)

| ID | Fait | Source | Verdict |
|----|------|--------|---------|
| FCT-b1-001 | La rubrique « Arrêtés d'autorisation » du tarn.gouv.fr utilise la pagination SPIP `(offset)/N` (offset 0, 10, 20... 270), PAS `?page=N` : les 7 requêtes paginées avec `?page=2` à `?page=8` avaient toutes renvoyé la page 1 (91 354 octets identiques vérifiés), d'où le constat d'absence erroné du 05-40 | Téléchargements comparés (tarn_ar_2.html à tarn_ar_8.html, 91 354 octets chacun) + ancres HTML `<a ...>(offset)/10</a>` | CONFIRMÉ |
| FCT-b1-002 | Scan complet des 28 pages (offset 0-270) : 12 pages contiennent des arrêtés éoliens/énergie, couvrant 2016-2026 ; aucun arrêté « Combaynart » ou « Valeco » littéral | Script scan_arretes.py (28 pages téléchargées et analysées) | CONFIRMÉ |
| FCT-b1-003 | Page 17 (offset 160) : « Arrêté du 16/05/2023 - autorisation environnementale, société Ferme éolienne de Puech Cambert, Barre » publié le 22/05/2023 | tarn.gouv.fr rubrique arrêtés, page 17 | CONFIRMÉ |
| FCT-b1-004 | Page 17 (offset 160) : « Arrêté du 16/05/2022 - autorisation environnementale - Cambert énergie, à Barre et Murat-sur-Vèbre » publié le 22/05/2023 | tarn.gouv.fr rubrique arrêtés, page 17 | CONFIRMÉ |
| FCT-b1-005 | SPV FERME EOLIENNE DE PUECH DE CAMBERT : SIREN 488018730, créée 13/01/2006, SNC (5499), siège 188 rue Maurice Béjart 34080 Montpellier (adresse Valeco), gérant Daumard, état actif | API Recherche Entreprises | CONFIRMÉ |
| FCT-b1-006 | SPV CAMBERT ENERGIE : SIREN 450758925, créée 10/11/2003, siège 188 rue Maurice Béjart Montpellier, gérants Daumard ET Gay Erick Alain (fondateur du groupe Valeco), état actif | API Recherche Entreprises | CONFIRMÉ |
| FCT-b1-007 | Le parc renouvelé est identifié par la presse comme « Puech de Cambert » et « Cap Redounde » sur les communes de Barre et Murat-sur-Vèbre ; le CP Valeco 2026 le nomme « Combaynart » (dénominations du même site) | La Dépêche 01/02/2025 (lu intégralement) + CP Valeco (05-40) | CONFIRMÉ (synonymie documentée) |
| FCT-b1-008 | 12 éoliennes de 76 m (MES 2006) remplacées par 8 de 119 m ; production 30 → 55 GWh/an (+83 %) selon La Dépêche 01/02/2025 ; 17 → 24 MW (+50 %) selon La Dépêche 19/07/2023 (chiffres du promoteur à 2 dates) | La Dépêche 01/02/2025 + 19/07/2023 | CONFIRMÉ (écart source documenté) |
| FCT-b1-009 | « Les autorisations pour ce renouvellement ont été obtenues en mai 2023 » : confirme la date de l'arrêté du 16/05/2023 | La Dépêche 01/02/2025 | CONFIRMÉ |
| FCT-b1-010 | Valeco propriétaire et exploitant du parc, maintenance confiée au turbinier Enercon, terres de particuliers louées par Valeco ; assemblage en Allemagne, acheminement via le port de Sète | La Dépêche 01/02/2025 | CONFIRMÉ |
| FCT-b1-011 | Démantèlement démarré en août 2024, chantier achevé au 1er trimestre 2026 ; recyclage ≥ 90 % des composants avec attestation de destination finale à la préfecture | La Dépêche 01/02/2025 | CONFIRMÉ |
| FCT-b1-012 | Retombées fiscales du renouvellement : IFER reversée à 20 % communes de Barre et Murat-sur-Vèbre, 50 % CdC Haut Languedoc, 30 % Département (+ CFE, taxe foncière) | La Dépêche 01/02/2025 + 27/06/2026 | CONFIRMÉ |
| FCT-b1-013 | Le préfet François-Xavier Lauch a visité le site de Combaynart le 12/07/2023 (ascension d'une éolienne), 2 mois après l'arrêté du 16/05/2023, guidé par François Daumard (président Valeco), en présence du maire Vidal, de Frédéric Berly (DREAL Occitanie) et du président de la CdC des Monts de Lacaune et Montagne du Haut Languedoc | La Dépêche 19/07/2023 (lu intégralement) | CONFIRMÉ |
| FCT-b1-014 | La demande de repowering a été déposée par Valeco en 2017, autorisée en mai 2023 : 6 ans de procédure, lenteur relevée par le préfet lui-même (« inadéquation entre l'urgence et la lenteur de traitement des dossiers ») | La Dépêche 19/07/2023 | CONFIRMÉ |
| FCT-b1-015 | « 30 ans qu'on n'avait pas eu la visite d'un préfet dans notre commune » (Vincent Vidal, maire de Barre, 12/07/2023) | La Dépêche 19/07/2023 | CONFIRMÉ |
| FCT-b1-016 | Le RAA (Recueil des Actes Administratifs) du Tarn existe au format `recueil-81-AAAA-NNN-recueil-des-actes-administratifs[-special].pdf` ; les snapshots Wayback couvrent 2024-2025 (numéros 222-521 pour 2024, 69-103 pour 2025) mais pas 2023 ni 2026 ; le numéro exact de l'arrêté Cambert n'est PAS accessible en OSINT (page de détail tarn.gouv : connexion échouée HTTP 000, cause non établie) | Wayback CDX + essais de fetch | CONSTAT D'ABSENCE (numéro) |
| FCT-b1-017 | L'arrêté du 16/05/2022 (Cambert énergie) précède celui du 16/05/2023 (Ferme éolienne Puech de Cambert) : probablement autorisation préalable puis autorisation du titulaire final, ou 2 étapes du même dossier. INDICE : les 2 arrêtés sont publiés le même jour (22/05/2023), cohérent avec une publication par lots de la rubrique ; à confirmer par le texte des arrêtés (page de détail inaccessible) | Rubrique officielle (2 entrées distinctes, même date de publication) | INFÉRENCE étayée |

## Analyse

### 1. Le constat d'absence était une erreur de méthode, pas une absence réelle

Le 05-40 avait conclu à un « constat d'absence partiel » (FCT-b-016) après n'avoir scanné que les pages 1-4 avec `?page=N`. En réalité :
- La pagination SPIP utilise `(offset)/N` dans le chemin, pas un paramètre `?page=`
- Toutes les pages `?page=2` à `?page=8` renvoyaient la page 1 (91 354 octets identiques vérifiés)
- Le scan correct (offset 10-270) révèle l'arrêté dès la page 17

**Leçon méthodologique** : devant une rubrique « paginée sur 28 pages », vérifier le mécanisme réel de pagination dans les ancres HTML avant de conclure à une absence. Le 05-40 avait vu « 28 pages » dans le HTML mais n'avait pas extrait le format des liens.

### 2. Identification du parc et des SPV

- **Parc** : Puech de Cambert + Cap Redounde (La Dépêche) = Combaynart (CP Valeco) = le premier parc éolien du Tarn (2006)
- **SPV** : FERME EOLIENNE DE PUECH DE CAMBERT (488018730, 2006) + CAMBERT ENERGIE (450758925, 2003), adresse 188 rue Maurice Béjart Montpellier = siège du groupe Valeco
- **Gérants** : Daumard (les 2 SPV) + Gay Erick (Cambert énergie, fondateur du groupe) : structure familiale Gay → Daumard, cohérente avec l'histoire Valeco (rachat EnBW 2019)
- La synonymie Combaynart/Puech de Cambert/Cap Redounde est documentée par le croisement presse + arrêtés (FCT-b1-007)

### 3. La chaîne complète 2017-2026 (FCT-b1-014)

Demande 2017 → arrêté 16/05/2022 (Cambert énergie) → arrêté 16/05/2023 (Ferme éolienne Puech de Cambert) → visite préfet 12/07/2023 → chantier 08/2024 → inauguration 11/06/2026. Le délai de 6 ans (2017-2023) est le point notable : le préfet lui-même a relevé la lenteur de traitement.

### 4. Signaux pour le faisceau

- **Aucun signal de corruption** sur cette chaîne : procédure complète, autorisation publiée, visite du préfet, maire satisfait.
- **Signal souveraineté** renforcé : le plus ancien parc éolien du Tarn (2006), développé par un groupe familial français, est aujourd'hui la propriété d'un groupe public allemand (EnBW), qui a obtenu son autorisation de repowering en mai 2023 et en tire +83 % de production (55 GWh/an).
- **Signal de rente (ordre de grandeur, à nuancer)** : la production passe de 30 à 55 GWh/an. Si l'on appliquait le tarif d'obligation d'achat de l'époque (82 EUR/MWh, régime 2008/2014), l'écart vaudrait ~2 M EUR/an. MAIS le régime de rémunération de la production issue du repowering (2026) n'est PAS vérifié : le nouveau contrat est probablement un contrat de complément de rémunération/spot au tarif bien inférieur (74-96 EUR/MWh en AO, ou prix de marché). Le chiffre ~2 M EUR/an est donc un PLAFOND théorique, pas un montant établi (à vérifier via le registre des contrats CRE pour les installations repowered, GAP à ouvrir).
- Le maire Vidal : « 30 ans qu'on n'avait pas eu la visite d'un préfet » : acceptation locale totale, aucun conflit documenté (contrairement au cas Cabrol de Lacaune).

## Verrou restant et actions

| ID | Question ouverte | Action |
|----|------------------|--------|
| GAP-b1-1 | Numéro exact de l'arrêté du 16/05/2023 (référence RAA : recueil-81-2023-XXX) | Télécharger le RAA 2023 (semaine du 16-22/05/2023) via Wayback ou le site ; les RAA 2023 ne sont pas dans les snapshots 2024-2026 visibles, requête CADA préfecture |
| GAP-b1-2 | Texte intégral des arrêtés (2022 et 2023) : page de détail tarn.gouv inaccessible (HTTP 000, WAF) | Wayback (pages de détail non archivées au CDX), CADA préfecture, ou consultation RAA |
| GAP-b1-3 | Distinction 2022 vs 2023 (Cambert énergie vs Ferme éolienne Puech de Cambert) : 2 étapes ou 2 titulaires | Texte des arrêtés (GAP-b1-2) |
| GAP-b1-4 | Le parc « Cap Redounde » a-t-il sa propre SPV ? (le renouvellement couvre 2 parcs : Puech de Cambert ET Cap Redounde) | API Recherche Entreprises (Cap Redounde), Pappers |

## Leçons pour le protocole anticorruption

1. **Ne jamais conclure à l'absence d'un document administratif sans avoir vérifié le mécanisme de pagination du site** : la rubrique tarn.gouv est paginée en SPIP `(offset)/N`, pas en `?page=`. La vérification des ancres HTML (<a href=".../(offset)/10">) aurait évité le faux négatif.
2. **Les arrêtés préfectoraux SONT publiés et indexés** : la rubrique officielle du tarn.gouv.fr est la source primaire de la chaîne d'autorisation (28 pages, 2016-2026). L'OSINT ne bute que sur les pages de détail (WAF HTTP 000) et les numéros RAA.
3. **Le croisement presse locale (La Dépêche) + rubrique officielle + RNE est la méthode qui résout la chaîne** : 3 sources indépendantes convergent sur la date (mai 2023), le titulaire (Valeco) et l'objet (repowering 12→8).
4. **Synonymie des parcs** : Combaynart = Puech de Cambert = Cap Redounde : toujours croiser le nom commercial (CP) avec le nom administratif (arrêté) et le nom presse avant d'identifier un parc.
