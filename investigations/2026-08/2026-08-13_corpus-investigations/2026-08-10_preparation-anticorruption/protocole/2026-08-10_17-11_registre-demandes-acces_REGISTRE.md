# REGISTRE CENTRAL DES DEMANDES D'ACCÈS AUX DOCUMENTS ADMINISTRATIFS

> Type : REGISTRE. Version : 1.0 (2026-08-10 17:11 CEST). Statut : EN VIGUEUR.
> Principe acté : le protocole d'accès aux documents (CADA et voies numériques) est un **principe général transverse à toutes les enquêtes anticorruption**. Il vit dans le dossier commun `2026-08-10_preparation-anticorruption/`, jamais dans un dossier d'enquête spécifique. Ce fichier est le registre unique qui référence TOUTES les demandes, quel que soit leur dossier d'origine.

## 1. PRINCIPE ET RÉPARTITION DES RÔLES

1. **Le protocole est transverse** : les canaux numériques (`2026-08-10_17-10_canaux-numeriques-acces_ARCHITECTURE.md`), ce registre, et les modèles génériques vivent dans le dossier commun anticorruption.
2. **Les demandes spécifiques vivent dans leur dossier d'enquête** : chaque enquête (SESN, ENR, BNDP...) garde ses pièces de demande près de l'investigation qu'elles servent (sous-dossier `cada_lettres/`), parce que leur objet est propre à cette enquête (références de marché, documents ciblés).
3. **Ce registre est le point d'entrée unique** : toute demande, où qu'elle soit rédigée, doit être référencée ici le jour même (règle R11).
4. **Canal exclusivement numérique** (décision 17:10) : email direct, formulaire web, téléprocédure. Aucune lettre papier.

## 2. INVENTAIRE DES DEMANDES RÉDIGÉES (8)

| N° | Dossier d'enquête d'origine | Cible | Objet | Canal numérique | Pièce (chemin relatif au dossier d'origine) | Statut |
|----|-----------------------------|-------|-------|-----------------|---------------------------------------------|--------|
| D01 | `2026-08-10_pilote-avenants-sesn` | SCSNE | Liste complète des avenants MOE et justificatifs (148 avenants) | marches@scsne.fr | `data/cada_lettres/2026-08-10_cada-1-SCSNE-avenants-MOE.md` | RÉDIGÉE, envoi PENDING |
| D02 | `2026-08-10_pilote-avenants-sesn` | SCSNE | DCE du marché 20TRI086 (justification durée 12 ans, R.2162-5) | marches@scsne.fr | `data/cada_lettres/2026-08-10_cada-2-SCSNE-20TRI086.md` | RÉDIGÉE, envoi PENDING |
| D03 | `2026-08-10_pilote-avenants-sesn` | SCSNE | Avis de la commission consultative des contrats (suppléments MOE) | marches@scsne.fr | `data/cada_lettres/2026-08-10_cada-3-SCSNE-commission-contrats.md` | RÉDIGÉE, envoi PENDING |
| D04 | `2026-08-10_pilote-avenants-sesn` | Cour des comptes | Pièces du contrôle CSNE (rapport 04/2026 : protocoles transactionnels) | courdescomptes@ccomptes.fr / formulaire ccomptes.fr | `data/cada_lettres/2026-08-10_cada-4-CdC-pieces-controle.md` | RÉDIGÉE, envoi PENDING |
| D05 | `2026-08-10_run2-enr` | CRE | Plan d'audit ENR (rec. n°1 CdC), données coûts/recettes de soutien, ET résultats des collectes d'échantillonnage déjà menées (biogaz 2024, hydro < 4,5 MW 2025, petit PV bâtiment, biométhane) | surveillance@cre.fr / formulaire cre.fr | `cada_lettres/email_CRE.md` (+ `lettre_CADA_CRE.md`) | RÉDIGÉE, envoi PENDING |
| D06 | `2026-08-10_run2-enr` | DGEC | Cadres de soutien ENR, données de versement et sanctions | formulaire economie.gouv.fr / PRADA | `cada_lettres/email_DGEC.md` (+ `lettre_CADA_DGEC.md`) | RÉDIGÉE, envoi PENDING |
| D07 | `2026-08-10_demande-cada-convention-bndp` | DGFiP | Convention/protocole d'accès continu à la BNDP (R.141-4 CJF, décret 2023-520) | PRADA economie.gouv.fr | modèle A dans `2026-08-10_11-33_demande-cada-convention-bndp_INVESTIGATION.md` | RÉDIGÉE, envoi PENDING |
| D08 | `2026-08-10_demande-cada-convention-bndp` | Cour des comptes | Convention CdC/DGFiP et base de données utilisée pour le rapport Dutreil | courdescomptes@ccomptes.fr | modèle B dans `2026-08-10_11-33_demande-cada-convention-bndp_INVESTIGATION.md` | RÉDIGÉE, envoi PENDING |

## 3. PIPELINE DES DEMANDES À RÉDIGER

| N° | Cible | Objet | Canal numérique | Justification |
|----|-------|-------|-----------------|---------------|
| D09 | HATVP | Avis non publiés sur les départs APE vers la finance privée (matrice F4, 432-13 : Azéma, Turrini, Bézard, Vial) | email contact hatvp.fr | Seule voie pénale encore ouverte du corpus (matrices juridiques 16:55) |
| D10 | Archives nationales | Fonds FRAN_IR_061758 (Commission de déontologie de la fonction publique 1990-2011) : modalités de consultation | salle des inventaires virtuelle (francearchives.gouv.fr) | Trou central de la fenêtre 2014-2019 (P2-1 du 09/08) |
| D11 | INPI | Bénéficiaires effectifs des titulaires de marchés (intérêt légitime journaliste/chercheur) | data.inpi.fr (démarche dédiée, procédure au 10/11/2026) | Traçabilité des bénéficiaires réels des contrats publics |

## 4. PROCÉDURE DE SUIVI (statuts et délais)

1. Statuts possibles : `RÉDIGÉE` → `ENVOYÉE (date)` → `RÉPONSE (date, contenu)` → `REFUS` → `REFUS TACITE (J+1 mois, silence)` → `SAISINE CADA`.
2. Délai légal de réponse : 1 mois (CRPA). Le silence vaut refus tacite.
3. En cas de refus ou de silence : saisine CADA en ligne `https://www.cada.fr/formulaire-de-saisine` (gratuit, délai 2 mois) ou email cada@mail.cada.fr.
4. Preuve de la demande : conserver l'email envoyé ou la copie HTML du formulaire dans `data/` du dossier d'enquête.
5. Toute nouvelle demande : rédiger la pièce dans le dossier d'enquête concerné, puis ajouter une ligne à ce registre le jour même (règle R11).

## 5. ÉTAT DE VÉRIFICATION

- Em-dash (U+2014) : 0 (vérifié).
- Hash SHA-256 : `2026-08-10_17-11_registre-demandes-acces_REGISTRE.md` consigné dans `registers.sha256`.
- Références : dashboard (fichier du dossier commun) et README (ordre de lecture) mis à jour le 10/08/2026 17:11.

STATE          : FINAL
VERSION        : 1.0
CREATED        : 2026-08-10_17-11 CEST
HASH           : (consigné dans registers.sha256)
