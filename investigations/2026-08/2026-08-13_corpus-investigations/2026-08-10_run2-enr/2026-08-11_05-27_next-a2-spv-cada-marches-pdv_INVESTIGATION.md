# NEXT-A2 DE L'ANGLE A : SPV DU PUECH DEL VERT, QUALITÉ CADA ET MARCHÉS DE TRAVAUX DU PARC

> Type : INVESTIGATION. Date : 2026-08-11 05:27 CEST.
> Objet : NEXT-A2 du document 05-00 (angle A). Vérifier si la SPV du parc (FERME EOLIENNE DE PUECH DEL VERT, SIREN 495300600) est soumise à la CADA (art. L. 300-2 CRPA) et chercher ses marchés de travaux de construction via BOAMP/TED, presse locale et sources primaires.
> Contexte : le DECP est vide pour les parcs privés (05-00, 05-18). Question : quel canal permet de documenter la construction du parc ?
> Sources : Pappers (fiche 495300600), API recherche-entreprises.data.gouv.fr (495300600, 434054318), Wayback Machine (groupevaleco.com), communiqué de presse Valeco juin 2026 (repowering Combaynart, PDF 3 p.), The Wind Power (fiche 18493 Puech de l'Homme), Le Journal d'Ici 17/01/2025, dossiers du run (18-30, 18-51, 21-30, 21-39), BOAMP open data (API opendatasoft).

## 1. MÉTHODE (EXÉCUTÉE)

1. État documenté de la SPV : relecture du dossier 18-30 (identité, actionnariat) + vérification API entreprise (statut actuel, gérant, actionnaire).
2. Vérification CADA : analyse de la structure de capital (qui détient la SPV, financement public majoritaire ou non) au sens de l'art. L. 300-2 CRPA.
3. Recherche des marchés de travaux : BOAMP open data (API opendatasoft, requêtes Barre + éolien, Valeco, Lacaune), Wayback groupevaleco.com (fiches parcs), presse locale (Le Journal d'Ici, La Dépêche via liens DDG).
4. Identification du parc réel : clarification avec les dossiers 21-30/21-39 (complexe Couffrau à Barre) et le CP Valeco juin 2026 (repowering Combaynart).

## 2. FACT-CHECKS (FCT)

| FCT | Fait | Source | Verdict |
|-----|------|--------|---------|
| FCT-a2-001 | SPV : FERME EOLIENNE DE PUECH DEL VERT, SIREN 495300600, SARL, capital 500 €, RCS Montpellier, créée 11/04/2007 (API : 2007-04-01), gérant actuel Daumard François, établissement LD Puech del Vert 81230 Lacaune | Pappers + API entreprise (11/08/2026) | CONFIRMÉ |
| FCT-a2-002 | Associé unique : VALECO REN (434054318) depuis la cession de parts Valeco SAS → VALECO REN (16/09/2016, acte Pappers) ; VALECO REN a pour DG Daumard (même personne que le gérant de la SPV) | Pappers (actes) + API entreprise | CONFIRMÉ |
| FCT-a2-003 | Le capital de la chaîne est PRIVÉ et étranger : VALECO REN = EnBW 51 % + KlimaVest (Commerzbank) 49 % depuis 11/2022 (dossier 22-05, 100 % allemand). AUCUN financement public majoritaire documenté au capital | Dossier 22-05 + 21-39 | CONFIRMÉ |
| FCT-a2-004 | **Qualité CADA : la SPV N'EST PAS assujettie** à l'art. L. 300-2 CRPA (2° : personnes de droit privé chargées d'une mission de service public ; 3° : gestion d'un service public) : personne de droit privé (SARL) sans mission de service public, le soutien public (OA/CR) est un revenu, pas un financement majoritaire du capital. Une demande CADA directe à la SPV pour ses contrats internes serait rejetée in limine | Analyse juridique art. L. 300-2 CRPA (2° et 3°) | INFÉRENCE (étayée par la structure du capital) |
| FCT-a2-005 | Aucun avis BOAMP/TED de construction du parc : les recherches « Barre + éolien » (31 résultats) renvoient à l'éolien offshore du Havre (quais Hermann du Pasquier), « Valeco » (96 résultats) à des syndicats de déchets homonymes (Valcom), « Lacaune » (112) à des marchés publics locaux sans lien | API BOAMP opendatasoft (5 requêtes, 11/08/2026) | CONFIRMÉ (constat d'absence) |
| FCT-a2-006 | Le parc réel documenté : complexe éolien de COUFFRAU à Barre (Tarn), 6 ADP (COUFFE01-06) + 2 installations anciennes, ~95 MW, dont COUFFE05 = Puech del Vert et COUFFE06 = Bois de Merdelou (16,1 MW, MES 10/05/2017, OA jusqu'en 2032) | RNIP/Enedis (dossier 21-30) | CONFIRMÉ |
| FCT-a2-007 | Fiche Wayback Valeco (2014) : « Parc éolien de Puech de l'Homme (Barre - 81) : 17 500 kW », 7 aérogénérateurs, mise en service novembre 2011, production 49 950 000 kWh, hauteur 64 m + 35 m rotor | Wayback groupevaleco.com, snapshot 20/02/2014 | CONFIRMÉ |
| FCT-a2-008 | Un parc distinct de Barre (Combaynart) est en REPOWERING : 12 → 8 éoliennes, +54 % de puissance, 55 GWh/an, inauguré 2026, « premier repowering du Parc naturel régional du Haut-Languedoc », > 250 000 € de retombées fiscales annuelles pour les collectivités | CP Valeco juin 2026 (PDF intégral) + Le Journal d'Ici 17/01/2025 (Duffes, repowering) | CONFIRMÉ |
| FCT-a2-009 | Le CP Valeco nomme les corps de métier des travaux (terrassement, génie civil, voirie, raccordement, logistique, entreprises locales) mais AUCUN nom d'entreprise, AUCUN montant, AUCUN contrat | CP Valeco juin 2026 | CONFIRMÉ (absence de données dans la source) |
| FCT-a2-010 | The Wind Power : Puech de l'Homme (Barre - Murat-sur-Vèbre), 16,1 MW, en production | thewindpower.net fiche 18493 | CONFIRMÉ |
| FCT-a2-011 | Les autorisations du parc (permis de construire sept 2011 sous municipalité Cabrol, autorisation environnementale, études d'impact, enquêtes publiques) sont des DOCUMENTS ADMINISTRATIFS détenus par l'État (préfecture du Tarn, DREAL Occitanie) : communicables via CADA à l'administration, indépendamment du statut de la SPV | Dossier 18-51 (FCT-gap1b-003) + art. L. 300-2 CRPA (1°) | CONFIRMÉ (voie CADA réelle) |

## 3. VERDICT : LA VOIE CADA DIRECTE EST FERMÉE, LES AUTORISATIONS SONT LA VOIE RÉELLE

1. **Qualité CADA de la SPV : NON.** La SPV est une SARL de droit privé, associé unique VALECO REN, capital 100 % privé et étranger (EnBW + Commerzbank). Elle n'exerce pas de mission de service public et n'est pas financée majoritairement par une personne publique : l'art. L. 300-2 CRPA (2° et 3°) ne s'applique pas. Une demande CADA « marchés de travaux » adressée directement à la SPV serait rejetée comme irrecevable (la CADA ne peut viser que les administrations et organismes chargés d'une mission de service public). C'est la confirmation au cas par cas du constat structurel du 05-00 : la construction des parcs privés échappe au droit d'accès public.
2. **La voie CADA RÉELLE est l'administration et les canaux voisins, pas seulement les autorisations** : (a) la préfecture du Tarn et la DREAL Occitanie détiennent les autorisations (permis de construire 2011, autorisation environnementale, études d'impact, rapports d'enquête publique, arrêtés ICPE), communicables sous réserve des secrets protégés (art. L. 311-5/311-6 CRPA) ; (b) le CONTRAT D'OBLIGATION D'ACHAT est détenu par la CRE / EDF OA (autorités soumises à la CADA) : communicable en partie, sous réserve du secret des affaires, et c'est le document qui porte le tarif, donc le coeur de la rente ; (c) ENEDIS, organisme chargé d'une mission de service public (distribution d'électricité), tient les documents de raccordement du parc : susceptibles d'entrer au champ de la CADA dans cette mesure ; (d) l'occupation du domaine public (AOT, baux, voirie d'accès) : si une partie de l'emprise est sur domaine public, les actes d'occupation sont communicables.
3. **La construction récente (repowering Combaynart 2024-2026) est documentée par la presse et les CP**, mais sans noms ni montants : Valeco annonce un recours aux « entreprises locales » sans publicité des contrats. Le seul moyen de chiffrer est la CADA à la préfecture (autorisation de repowering = arrêté préfectoral), le contrat d'achat via la CRE et le suivi presse.
4. **Clarification géographique consolidée** : il y a DEUX parcs distincts à Barre dans le périmètre Valeco : (a) le complexe Couffrau (dont Puech del Vert COUFFE05 et Bois de Merdelou COUFFE06, ~95 MW, MES 2017) et (b) Combaynart (premier parc éolien du Tarn, 2005-2006, repowering 2026). La SPV 495300600 est celle du complexe Couffrau (COUFFE05), pas de Combaynart.

## 4. IMPLICATIONS POUR L'ANGLE A ET LA STRATÉGIE (04-56)

1. **L'angle « marchés de travaux des parcs privés » se heurte à une double fermeture** : pas de DECP (05-00), pas de BOAMP/TED (05-27), pas de CADA directe (05-27). La seule voie probatoire est la CADA à l'administration (autorisations) + presse + données de production.
2. **Le point CADA est désormais documenté juridiquement** : la distinction « SPV privée non assujettie vs administration détentrice des autorisations assujettie » est un apport réutilisable pour tous les parcs privés (pas seulement Valeco).
3. **Le repowering de Combaynart est un cas d'école pour l'angle A** : chantier 2024-2026, entreprises locales mobilisées, mais zéro donnée publique sur les montants. Une CADA à la préfecture du Tarn sur l'arrêté d'autorisation du repowering est l'action la plus rentable.
4. **Le fil central est renforcé** : la construction et les coûts des parcs privés sont inaccessibles par 4 canaux testés (DECP, BOAMP/TED, CADA directe, presse/CP sans chiffres). L'absence de collecte des coûts (rec. n°1 CdC) n'est pas un accident : c'est la condition de l'invisibilité.

## 5. PROCHAINES ÉTAPES ACTIONNABLES

1. **NEXT-A2a (priorité : repowering 2026, pas le permis 2011)** : rédiger le cadre d'une demande CADA à la préfecture du Tarn (et DREAL Occitanie) pour l'arrêté d'autorisation environnementale du repowering de Combaynart (2024-2026, enquête publique récente, arrêté le plus accessible), puis en second le permis de construire initial 2011 du Puech del Vert (ancien, potentiellement mal archivé). Référencer au registre 17-11.
2. **NEXT-A2b** : documenter au playbook 12-38 le constat « SPV privée ENR = hors CADA directe pour ses contrats internes, mais la voie reste ouverte par l'administration (autorisations), la CRE/EDF OA (contrat d'achat), Enedis (raccordement) et le domaine public » (gain de temps pour les prochains dossiers).
3. **NEXT-A2c** : compléter la carte des parcs Valeco (Couffrau vs Combaynart) dans la stratégie 04-56, avec la clarification des 2 parcs distincts de Barre.

## 6. GAP ET LIMITES

- GAP-a2-1 : montants des travaux de construction du complexe Couffrau : inconnus (aucune source publique). Une CADA préfecture pourrait documenter le coût déclaré dans le dossier d'autorisation.
- GAP-a2-4 : résidu de contradiction Lacaune/Barre : l'adresse RNE de la SPV (LD Puech del Vert, 81230 Lacaune, Pappers) diffère du site physique documenté par le RNIP (COUFFE05, Barre, correction 21-30 qui infirme 18-51 : 5 Enercon E70, MES 2012). L'identification SPV = COUFFE05 repose sur le nom RNIP « (PUECH DEL VERT) » : à consolider via le PV d'AG ou le registre du RCS.
- GAP-a2-2 : identité précise des entreprises de travaux de Combaynart : non publiée (CP sans noms). Presse locale à surveiller (La Dépêche, Le Journal d'Ici).
- GAP-a2-3 : le CP Valeco de juin 2026 mentionne des retombées fiscales > 250 K€/an mais sans ventilation (IFER, CFE, TFPB) : chiffrage possible via les bases fiscales si nécessaire.
- Limite : la fiche Wayback 2014 (17 500 kW, 7 éoliennes) concerne Puech de l'Homme (sous-ensemble ou ancien nom du complexe) ; The Wind Power indique 16,1 MW : la puissance exacte du complexe Couffrau (~95 MW selon RNIP, toutes ADP) reste à consolider.

STATE          : FINAL
VERSION        : 1.0
CREATED        : 2026-08-11_05-27 CEST
HASH           : (consigné après mise à jour du RUN_MANIFEST)
