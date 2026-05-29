# ENTITIES — Inondations Tonneins Février 2026

## Acteurs institutionnels

| Entité | Type | Rôle | Propriétaire/Contrôle | bias_flag |
|--------|------|------|----------------------|-----------|
| Météo-France | Service public | Alertes météo | État français | false |
| Vigicrues | Service public | Surveillance crues | État français (Min. Écologie) | false |
| Préfecture Lot-et-Garonne | Administration | Coordination crise | État français | false |
| SDIS 47 | Service public | Secours, pompiers | État + Département | false |
| Enedis | Entreprise publique | Réseau électrique | EDF (majorité État) | unknown |
| Mairie de Tonneins | Collectivité | Gestion locale | Commune | false |
| Val de Garonne Agglomération | Intercommunalité | Compétences transférées | Interco | unknown |

## Acteurs médiatiques

| Entité | Type | Propriétaire | bias_flag | Notes |
|--------|------|--------------|-----------|-------|
| BFM TV | Média TV | Altice (Patrick Drahi) | true | Concentration médias, liens pouvoir |
| France 3 | Média public | France Télévisions | false | Service public |
| Sud Ouest | Presse régionale | Groupe Sud Ouest | false | Indépendant |
| actu.fr | Web média | Actu.fr | unknown | Régional |
| Le Monde | Presse nationale | Le Monde Libre | false | Indépendant |
| La Dépêche | Presse régionale | Groupe La Dépêche | unknown | Sud-Ouest |

## Acteurs de terrain

| Entité | Type | Rôle | Notes |
|--------|------|------|-------|
| Témoin | Habitants Tonneins | Témoignage, résilience locale | Connaît terrain, expérimenté (crues 2019, 2021) |
| Voisins, famille | Habitants | Entraide, préparation | Réseau local |
| Pompiers Limousin (SDIS 19, 23, 87) | Renforts | Évacuations, déblaiement | Ne connaissent pas le terrain |
| Police nationale (?) | Forces ordre | Filtrage pont | Application protocoles |

## Structures administratives (contexte GEMAPI)

| Entité | Compétence | Problème identifié |
|--------|------------|-------------------|
| Communes | Perdu compétence zones inondées | Plus de lien direct habitants |
| Communautés de communes | Compétence GEMAPI depuis 2018 | Budgets insuffisants, déconnexion terrain |
| État | Pilotage centralisé | Désengagement financier, couches administratives |

## Relations (Γ)

```
Mairie Tonneins --[tente coordonner]--> Enedis
Enedis --[central dépassé]--> Mairie Tonneins
SDIS 47 --[demande renforts]--> SDIS Limousin
SDIS Limousin --[ne connaît pas]--> Terrain local
Préfecture 47 --[protocoles]--> Police
Police --[applique sans discernement]--> Habitants
BFM TV --[spectacle]--> Inondations
BFM TV --[pas enquête]--> Déficience GEMAPI
Habitants --[autosuffisance]--> Crise
État --[transfert compétences]--> Intercommunalités
Intercommunalités --[budgets insuffisants]--> Gestion crues
```

## Absences notables (silence_qui_parle)

| Acteur attendu | Absence constatée | Interprétation |
|----------------|-------------------|----------------|
| État (niveau national) | Pas de visite, pas de déclaration spécifique | Désengagement assumé |
| Ministre Écologie | Réponse dilatoire sur GEMAPI | Évitement responsabilité |
| Médias nationaux | Pas d'enquête sur échec gestion | Sensationnel > analyse |
| Intercommunalités | Peu visibles sur terrain | Incompétence/désengagement |
