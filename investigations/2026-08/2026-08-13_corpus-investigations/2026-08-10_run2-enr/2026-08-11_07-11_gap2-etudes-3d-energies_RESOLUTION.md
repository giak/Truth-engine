# RESOLUTION : DELIBERATIONS SIEDS 2014-2015 ET PRODUCTION ANNONCEE PAR 3D ENERGIES (GAP-pr-2)

- STATE          : FINAL
- DATE           : 2026-08-11 07:11 CEST
- TYPE           : RESOLUTION (KERNEL v2.8, format allégé axe piste)
- DOSSIER        : 2026-08-10_run2-enr (piste ENR, axe C, suite 06-36/06-51)
- OBJECT         : chercher les délibérations du SIEDS 2014-2015 autorisant l'acquisition de MARGNES/SINGLADOU par 3D ENERGIES et vérifier si les études économiques utilisaient la production marketing 34,32 GWh (surestimation de 34 % vs réel RNIP 22,5 GWh)
- REPONSE A      : GAP-pr-2 du document 06-51 (suggéré en priorité)
- DONNEES NOUVELLES : rapport d'activité SIEDS 2017 (PDF officiel 2,9 Mo, organigramme du Groupe SIEDS), rapports SIEDS 2018-2019 (production par filière), pages Wayback 3denergies.fr parc-eolien-de-margnes / parc-eolien-de-singladou (19/11/2019), page actes-administratifs SIEDS + plugin WPFD (nonce, POST), CDX Wayback (232 captures download)

---

## 1. Découverte majeure : l'acquéreur public annonçait 28 GWh, PAS 34,32 GWh

Les pages officielles de l'acquéreur (3D ENERGIES, filiale du SIEDS) capturées par Wayback le 19/11/2019 indiquent pour les 2 parcs de Fontrieu :

| Parc | MES annoncée | Éoliennes | Puissance | Production prévisionnelle |
|------|-------------|-----------|-----------|--------------------------|
| Parc éolien de Margnès | mars 2008 | 5 × Enercon E70 (2,3 MW) | 11,5 MW | **23 000 MWh (23 GWh)** |
| Parc éolien de Singladou | novembre 2009 | 1 × Enercon E70 (2,3 MW) | 2,3 MW | **5 000 MWh (5 GWh)** |
| **Total annoncé par 3D ENERGIES** | | 6 | 13,8 MW | **28 000 MWh (28 GWh)** |

URLs : web.archive.org/web/20191119223909/http://www.3denergies.fr/parc-eolien-de-margnes/ et /20191119222810/http://www.3denergies.fr/parc-eolien-de-singladou/ (5 captures 19/11/2019 - 08/06/2023 chacune).

Caveat MES : les dates annoncées (mars 2008 / novembre 2009) reprennent le calendrier marketing Valeco (FCT-pc-001 du 06-24) ; les MES RNIP sont 14/09/2007 (5 éol.) et 29/07/2009 (1 éol.) (FCT-pr-001/002 du 06-51). Cet écart est un indice concordant de la circulation de la fiche vendeur, à noter sans surcharger.

## 2. Le calcul comparatif (script /tmp/s2_calc.py)

| Élément | Valeur | Ratio vs réel |
|---------|--------|---------------|
| Marketing Valeco 2014 (fiche, 6 éol.) | 34,32 GWh | 152 % du réel |
| **Prévisionnel officiel 3D ENERGIES (acquéreur)** | **28,00 GWh** | **124 % du réel** |
| Réel RNIP 2024 (2 tranches) | 22,54 GWh | 100 % |
| Écart marketing vs prévisionnel acquéreur | **-18,4 %** | |

Heures équivalentes : marketing Valeco ~2 487 h/éol. ; prévisionnel 3D ENERGIES ~2 000-2 174 h/éol. ; réel RNIP ~1 633 h/éol.

**Caveats sur la portée de la découverte :** (a) le « prévisionnel 3D ENERGIES » provient de la **communication publique** du site 3denergies.fr capturé en 2019, soit 4 ans après l'achat de 2015 : rien ne prouve que les **études internes de valorisation remises au conseil de surveillance en 2015** utilisaient 28 GWh plutôt que 34,32 GWh (une page web de 2019 peut refléter des chiffres révisés a posteriori) : GAP-s2-2. (b) le « réel » RNIP = énergie annuelle glissante (fenêtres 12 mois à 01/05/2024 et 21/02/2023), pas une année civile : les ratios sont indicatifs.

**Conséquence sur la thèse « achat sur la base de données marketing surestimées » (06-51, verdict point 4) : NUANCÉE pour sa version forte, non réfutée définitivement.** La communication publique de l'acquéreur (2019) annonçait 28 GWh, soit 18,4 % sous le marketing du vendeur (34,32 GWh) : l'acheteur n'a pas repris la fiche Valeco dans sa vitrine. En revanche, même ce chiffre (28 GWh) surestime le réel de 24 % : les deux acteurs ont surévalué le gisement. La version forte (« l'acheteur a été trompé par la fiche du vendeur ») est affaiblie par la communication publique, mais les études internes de 2015 restent inconnues (GAP-s2-2) : on ne peut pas exclure que la fiche vendeur ait circulé dans le dossier d'acquisition.

## 3. Délibérations du SIEDS 2014-2015 : constat d'absence en sources libres

| Voie | Résultat |
|------|----------|
| Page actes-administratifs sieds.fr (site actuel) | Page accessible (91 Ko) mais contenu des fichiers NON exposé en curl (plugin WP File Download, formulaire POST avec nonce renvoyant la page inchangée : pas de résultats publics) |
| Plugin WPFD (wp-json) | Endpoints wpfd/v1 : 404 ; POST avec nonce valide (e4adf8cfe4) : aucune sortie de fichiers pour MARGNES/SINGLADOU/délibération/participation |
| CDX Wayback download/ | 232 captures ; catégories : retours-comite-syndicaux (2021-2022), deliberations-budgetaires-2023 (cat. 250), 2024 (cat. 251) : **aucune délibération 2014-2015 capturée** |
| Wayback domaine (IMG/pdf, 295 captures) | Délibération 2015 testée (« 14-36 creation d'un programme nouveau eclairage public 2015 ») : fichier = HTML factice (11 Ko), pas le PDF réel ; la capture du rapport d'activité 2015 (20161102153207) = page sans PDF |
| Rapports d'activité SIEDS 2017-2019 (PDF officiels) | Organigrammes du Groupe SIEDS : MARGNES (2008) et SINGLADOU (2012) comme filiales productrices sous la SAEML 3D ENERGIES (85 %/15 % au 2017) : confirment la structure, PAS le prix ni les études |
| Presse (Bing, DDG, jina/Google) | Tous les moteurs bloquent (challenge/captcha, HTTP 29) : constat d'absence sans contre-test |

**Verdict délibérations : les délibérations du SIEDS 2014-2015 (montant, études, autorisation d'acquisition) ne sont PAS publiées en ligne, ni sur le site actuel (WPFD non public), ni dans Wayback (aucune capture), ni en presse indexée accessible.** C'est un constat d'absence de type « point aveugle documentaire » : le montant de la prise de participation reste non traçable en sources libres (cohérent avec le GAP-pc-2/06-36 : prix non publié). Voies restantes : demande d'accès aux documents administratifs (CADA SIEDS, le syndicat est soumis au CRPA), archives du comité syndical, presse papier locale (La Nouvelle République, Courrier de l'Ouest) hors indexation gratuite.

## 4. Rapports d'activité SIEDS : données structurelles consolidées (source primaire)

- **RA 2017** (PDF 2,9 Mo, téléchargé sieds.fr/download/86/rapports-dactivites/3129) : organigramme « Organisation du Groupe SIEDS 2017 » : la SAEML 3D ENERGIES (2007) détient 85 % de MARGNES ENERGIE et 15 % de SINGLADOU ENERGIE (dates de prise 2008/2012 dans l'organigramme, à distinguer des MES), ainsi que MAUZE THOUARSAIS / SAINT-LADE (41 %-100 %). Les dates « 2008/2012 » de l'organigramme = dates de création/prise des sociétés, PAS les MES (contrairement à une lecture rapide).
- **RA 2019** : production 2019 du parc éolien SIEDS = **170 826 MWh (170,8 GWh)** ; PV 56 872 MWh ; hydraulique 27 460 MWh ; méthanisation/cogénération 6 175 MWh. La part MARGNES+SINGLADOU (~22-28 GWh) représente ~13-16 % de la production éolienne du groupe.
- **RA 2018** : mention « Création d'une société de projet éolien (SAS) 3D ENERGIES 119 / 3D ENERGIES 62 par la SEML 3D ENERGIES » (19/03/2018) : le SIEDS déployait sa stratégie de SPV éoliennes via 3D ENERGIES.

## 5. Faits consolidés

| # | Fait | Source |
|---|------|--------|
| FCT-s2-001 | Page officielle 3D ENERGIES (Wayback 19/11/2019) parc Margnès : Fontrieu (Tarn), MES mars 2008, 5 × Enercon E70 2,3 MW, 11,5 MW, production prévisionnelle 23 000 MWh | web.archive.org/web/20191119223909/3denergies.fr/parc-eolien-de-margnes |
| FCT-s2-002 | Page officielle 3D ENERGIES (Wayback 19/11/2019) parc Singladou : Fontrieu (Tarn), MES novembre 2009, 1 × Enercon E70 2,3 MW, 2,3 MW, production prévisionnelle 5 000 MWh | web.archive.org/web/20191119222810/3denergies.fr/parc-eolien-de-singladou |
| FCT-s2-003 | **Prévisionnel total annoncé par l'acquéreur 3D ENERGIES : 28 000 MWh (28 GWh) = 81,6 % du marketing Valeco (34,32 GWh)** | Somme des 2 pages + calcul /tmp/s2_calc.py |
| FCT-s2-004 | Le prévisionnel acquéreur (28 GWh) surestime la production réelle RNIP 2024 (22,54 GWh) de **24 %** (heures équivalentes 2 000-2 174 vs 1 633) | Calcul /tmp/s2_calc.py |
| FCT-s2-005 | La thèse « achat sur la base des 34,32 GWh marketing » est NUANCÉE pour sa version forte (communication publique 2019 de l'acquéreur = 28 GWh, 18,4 % sous le marketing vendeur) ; les études internes de 2015 restent inconnues (GAP-s2-2) | Analyse croisée pages 3D vs fiche Valeco vs RNIP |
| FCT-s2-006 | Organigramme « Groupe SIEDS 2017 » (RA SIEDS 2017, PDF officiel) : lecture OCR = SAEML 3D ENERGIES détient 85 % MARGNES + 15 % SINGLADOU (autres pourcentages 59 %/41 %/100 % présents dans le même schéma, attribution ambiguë : à confirmer au RCS/statuts, GAP-s2-1) | sieds.fr/download/86/rapports-dactivites/3129/rapport-d-activite-2017.pdf |
| FCT-s2-007 | RA SIEDS 2019 : production éolienne du groupe = 170 826 MWh (2019) ; MARGNES+SINGLADOU = ~13-16 % du parc éolien du SIEDS | sieds.fr/download/86/rapports-dactivites/4144/rapport-d-activite-2019.pdf |
| FCT-s2-008 | RA SIEDS 2018 : 3D ENERGIES crée les SPV éoliennes « 3D ENERGIES 119 » et « 3D ENERGIES 62 » (19/03/2018) | sieds.fr/download/86/rapports-dactivites/3128/rapport-d-activite-2018.pdf |
| FCT-s2-009 | **Délibérations SIEDS 2014-2015 (autorisation d'acquisition, montant, études) : CONSTAT D'ABSENCE, non publiées en sources en ligne** (site actuel WPFD non public, Wayback 0 capture 2014-2015, presse indexée bloquée) ; absence en ligne ≠ inexistence (voies : CADA, archives papier) | Constat d'absence multicanal (section 3) |
| FCT-s2-010 | La délibération SIEDS 2015 testée dans Wayback (« 14-36 eclairage public 2015 ») = fichier HTML factice, pas le PDF réel : les captures du vieux site sont dégradées | Wayback 20190615061117, analyse de fichier |

## 6. Verdict

1. **La thèse « achat sur la base des données marketing surestimées » est NUANCÉE pour sa version forte** : la communication publique de l'acquéreur (2019) annonçait 28 GWh (23+5), soit 18,4 % SOUS le marketing Valeco (34,32 GWh). L'acheteur n'a pas repris la fiche du vendeur dans sa vitrine ; les études internes de 2015 restent inconnues (GAP-s2-2).
2. **Mais les études de l'acquéreur étaient elles-mêmes optimistes de 24 %** (28 vs 22,5 GWh réels) : l'écart fiche/réel n'est PAS un artefact du marketing vendeur, il est structurel (heures de vent réelles 1 633 h, bien sous les 2 000-2 500 h des prévisionnels). Les deux acteurs (vendeur ET acheteur public) ont surévalué le gisement.
3. **La délibération SIEDS 2014-2015 (prix + études) reste un point aveugle** : non publiée en sources libres. Voie CADA SIEDS (syndicat soumis au CRPA) pour le montant, ou archives papier.
4. **Signal structurel consolidé** : une collectivité (SIEDS) a fait entrer ses contribuables dans l'éolien tarnais via une SEM (3D ENERGIES) sur la base d'un prévisionnel optimiste de 24 %, avec un prix non publié (06-36) et une production réelle inférieure de 24 % au prévisionnel de l'acheteur lui-même. Le motif le plus robuste n'est pas « tromperie du vendeur » mais « aléa de production non maîtrisé par l'acheteur public » + « opacité du prix » (GAP-s2-1/-2).
5. **0 corruption pénale** : rien n'indique une manipulation : l'acquéreur utilisait ses propres chiffres, plus bas que le marketing. Le point d'attention devient la rationalité économique de l'achat au vu du réel (24 % d'écart) et le prix payé (inconnu).

## 7. GAPS

| # | Gap | Voie |
|---|-----|------|
| GAP-s2-1 | Montant exact de la prise de participation 2015 (3D ENERGIES dans MARGNES/SINGLADOU) | Demande CADA SIEDS (CRPA L. 311-1), comptes 2015-2016 de 3D ENERGIES (greffe Niort), délibérations comité syndical 2014-2015 (archives papier) |
| GAP-s2-2 | Les études de valorisation 2015 (qui ont servi au prix) : hypothèses de production, taux, gisement | Dossier d'acquisition, rapport d'audit pré-cession, demandes CADA |
| GAP-s2-3 | Production réelle historique 2015-2023 des 2 parcs (pour confirmer l'écart prévisionnel/réel année par année) | RNIP historique / Enedis Open Data (GAP-pr-1 du 06-51) |
| GAP-s2-4 | Presse papier locale 2015-2016 (La Nouvelle République, Courrier de l'Ouest) sur l'acquisition | Archives presse payantes, bibliothèques |

## 8. Traçabilité

- Scripts : /tmp/s2_calc.py (comparatif), /tmp/s2_sieds_structure.py, /tmp/s2_wpfd_post.py, /tmp/s2_comite240.py, /tmp/s2_parcs_wb.py, /tmp/s2_rapport2017.py, /tmp/s2_rapports18.py (rapports 2018-2019)
- Artefacts : /tmp/sieds_ra_2017.pdf/.txt (2,9 Mo), /tmp/sieds_ra_2018.pdf/.txt, /tmp/sieds_ra_2019.pdf/.txt, pages Wayback parcs (captures 19/11/2019)
- Sources : sieds.fr (rapports d'activité 2017-2019, page actes-administratifs, plugin WPFD), web.archive.org (3denergies.fr parcs, download/ SIEDS), RNIP/ODRE (06-51)
- Liens : 06-51 (GAP-pr-2 ouvert, FCT-pr-004/005), 06-36 (cession 2015, prix non publié), 06-44 (délibérations Fontrieu), 06-24 (FCT-pc-018)
- Em-dash : 0 (vérifié)
