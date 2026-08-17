# CANAUX NUMÉRIQUES DE DEMANDE D'ACCÈS AUX DOCUMENTS ADMINISTRATIFS

> Type : ARCHITECTURE. Version : 1.0 (2026-08-10 17:10). Statut : EN VIGUEUR.
> Décision utilisateur (10/08/2026) : « oublie la CADA, on fait du OSINT numérique, pas le temps ni les moyens d'envoyer des lettres, sauf si on peut formaliser par des emails ou voie numérique par un site web ». Vérification effectuée : TOUS les canaux ciblés disposent d'une voie 100 % numérique (email ou téléprocédure). Aucune lettre papier n'est nécessaire.

## 1. DÉCISION ET PORTÉE

1. **Aucun envoi papier** : plus aucune lettre postale n'est préparée ni envoyée.
2. **Toute demande d'accès passe par une voie numérique** : email direct, formulaire web, téléprocédure en ligne.
3. **Priorité OSINT** : la demande d'accès n'est qu'un complément ; le travail principal reste la collecte de sources ouvertes (playbook 12-38).
4. **Traçabilité numérique** : chaque demande conserve son email/formulaire, sa date, son accusé (mail conservé, copie du formulaire), le silence d'un mois valant refus tacite (CRPA).

## 2. LES CANAUX NUMÉRIQUES VÉRIFIÉS (par institution)

| Institution | Canal numérique | URL / adresse | Statut vérification | Notes |
|-------------|-----------------|---------------|---------------------|-------|
| **CADA (recours)** | Téléprocédure de saisine en ligne | https://www.cada.fr/formulaire-de-saisine | VÉRIFIÉ (curl 10/08/2026, 20 Ko, page « Formulaire de saisine », lien `/formulaire-de-saisine` présent sur cada.fr) | Gratuit, après refus ou silence 1 mois ; délai de saisine 2 mois ; traite en moyenne 66 jours |
| **CADA (email)** | Email direct | cada@mail.cada.fr (page officielle) ; cada@cada.fr (service-public) | RAPPORTÉ (chercheur + page cada.fr) | Alternative au formulaire |
| **Ma Dada (madada.fr)** | Portail associatif de demandes d'accès | https://madada.fr | VÉRIFIÉ (curl 10/08/2026, 40 Ko) ; ACTIF en 2026 (51 000+ demandes, réponses d'administrations publiées en 2026) | Open Knowledge France ; permet d'envoyer et publier les demandes ; code open source (Alaveteli) |
| **Cour des comptes** | Formulaire de contact en ligne + email | https://www.ccomptes.fr/fr/contact/formulaire_de_contact ; courdescomptes@ccomptes.fr | RAPPORTÉ (chercheur, annuaire service-public mis à jour 23/02/2026) | Pour la convention CdC/DGFiP (BNDP) et les rapports |
| **DGFiP / ministères éco-fin** | Formulaire de contact + PRADA | https://www.economie.gouv.fr/documentation/acces-aux-documents-administratifs | RAPPORTÉ (chercheur, economie.gouv.fr consulté 08/2026) | Pas de guichet numérique unique DGFiP : passer par la PRADA des ministères économiques et financiers ou le service détenteur |
| **SCSNE** | Emails dédiés | marches@scsne.fr ; dpo.scsne@scsne.fr (mentions légales) | RAPPORTÉ (chercheur, canal-seine-nord-europe.fr mentions légales consultées 08/2026) | Pour les DCE et justifications de durée (marchés publics) |
| **CRE** | Formulaire de contact + emails thématiques | https://www.cre.fr/nous-contacter.html ; surveillance@cre.fr ; opendata@cre.fr | RAPPORTÉ (chercheur, cre.fr mis à jour 23/01/2026) | Pour le plan d'audit ENR et les données coûts/recettes |
| **Service-public (référentiel)** | Fiche « Accès aux documents administratifs » | https://www.service-public.gouv.fr/particuliers/vosdroits/F2467 | RAPPORTÉ (chercheur, vérifié 08/10/2025) | Confirme : demande par mail possible, saisine CADA en ligne ou par mail |
| **Archives nationales** | Demandes en ligne | (salle des inventaires virtuelle, formulaires par fonds) | À VÉRIFIER | Pour le fonds FRAN_IR_061758 (Commission de déontologie 1990-2011) |
| **HATVP** | Avis publiés en ligne + contact | hatvp.fr (thématheque, open data) | À VÉRIFIER | Les avis publiés n'exigent pas de demande ; pour les avis non publiés, contact email |
| **INPI** | Formulaire de demande bénéficiaires effectifs | data.inpi.fr (démarche dédiée) | À VÉRIFIER | Intérêt légitime requis (journaliste/chercheur) ; procédure changée au 10/11/2026 |

## 3. PROCÉDURE NUMÉRIQUE STANDARD (à appliquer pour toute demande)

1. **Tenter l'OSINT d'abord** (playbook 12-38) : le document est-il déjà publié quelque part ? (Wayback, data.gouv.fr, page institutionnelle, presse).
2. **Choisir le canal numérique** du tableau ci-dessus (email dédié préféré, sinon formulaire web).
3. **Rédiger un modèle email** (objet clair, référence exacte des documents, acceptation de l'occultation, format électronique natif demandé) : les lettres déjà rédigées dans les dossiers (run2-enr/cada_lettres, pilote SESN/cada_lettres, BNDP) sont converties en modèles email, pas en courriers papier.
4. **Conserver la trace** : email envoyé (copie dans data/), ou copie d'écran/HTML du formulaire soumis, avec date.
5. **Suivre le délai** : 1 mois, silence = refus tacite ; en cas de refus ou silence, saisine CADA en ligne (formulaire cada.fr) ou email cada@mail.cada.fr.
6. **Consigner dans le registre central des demandes** `2026-08-10_17-11_registre-demandes-acces_REGISTRE.md` (même dossier `protocole/`, transverse à toutes les enquêtes) : cible, canal, date, statut, réponse. Toute demande, où qu'elle soit rédigée, y est référencée le jour même (règle R11).

## 4. CE QUI CHANGE PAR RAPPORT À L'EXISTANT

| Avant (doctrine) | Après (décision 17:10) |
|------------------|------------------------|
| Lettres papier prêtes à envoyer (DELIVERABLE_PENDING) | Modèles email ou formulaires web, envoi immédiat possible |
| Courrier recommandé évoqué (Phase 5 pilote) | Écarté : pas d'envoi physique |
| Délai de réponse par courrier | Délai identique (1 mois) mais traçabilité numérique |
| Contact des institutions à trouver | Tableau §2 fournit les canaux numériques |

## 5. LIMITES HONNÊTES

1. Le formulaire CADA en ligne et l'email cada@mail.cada.fr sont confirmés ; les emails institutionnels (CRE, CdC, SCSNE) sont rapportés par chercheur web : à re-vérifier au moment de l'envoi (page contact consultée ce jour-là).
2. Certains services n'ont pas de guichet numérique unique (DGFiP) : la demande devra passer par la PRADA ou le service détenteur, avec risque de renvoi.
3. madada.fr est un tiers (Open Knowledge France) : l'utiliser comme outil de suivi/publication, pas comme canal officiel.
4. Le silence vaut refus tacite : sans envoi physique, la preuve de la demande repose sur l'email conservé ou la copie du formulaire : les conserver soigneusement.

## 6. ACTIONS IMMÉDIATES

1. Convertir les lettres `run2-enr/cada_lettres/` (CRE, DGEC) en modèles email avec les canaux §2.
2. Convertir les lettres `pilote-avenants-sesn/data/cada_lettres/` (SCSNE ×3, CdC) en modèles email.
3. Convertir la lettre `demande-cada-convention-bndp` (CdC + DGFiP) en modèle email.
4. Référencer les 8 demandes dans le registre central `2026-08-10_17-11_registre-demandes-acces_REGISTRE.md` (fait le 10/08 17:11).
5. Mettre à jour le dashboard (décision actée, section « demandes d'accès ») et le README.
