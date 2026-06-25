# INVESTIGATION — Les 45 Grands Projets Numériques de l'État : Anatomie d'un Pipeline

## §0 SYNOPOSIS

Depuis 2016, la DINUM publie chaque semestre le panorama des grands projets numériques de l'État. En décembre 2025, 45 projets dépassant 9 M€ sont suivis, pour un budget cumulé de 3,3 Md€. Ce rapport analyse ce pipeline : qui porte les projets, combien ils coûtent, qui les développe, et ce qui se passe quand ils échouent.

Les chiffres officiels (surcoût moyen 6,5 %, retard 21 %) sont trompeurs. La Cour des comptes a démontré que ces indicateurs excluent les projets sortis du périmètre en difficulté, que la DINUM n'a qu'un accès partiel aux données via Chorus, et que les gains de productivité ne sont jamais mesurés. Sur les projets les plus risqués (+50 M€, +8 ans), les dérives dépassent 30 %.

Les échecs passés (Louvois, ONP, Cassiopée) ont coûté des centaines de millions. Les échecs présents (ANTS, NexSIS, facturation électronique, 4-Flight) confirment que les causes profondes — absence de pilotage stratégique, dépendance aux ESN, sous-dimensionnement DINUM — n'ont pas été corrigées.

## §1 LE PANORAMA : CHIFFRES CLÉS

### 1.1 Métriques globales (22e édition, déc. 2025)

| Indicateur | Valeur | Source |
|-----------|--------|--------|
| Nombre de projets | 45 | DINUM panorama déc. 2025 |
| Budget cumulé | 3,3 Md€ | DINUM |
| Budget cumulé (estimation 2024) | 3,8 Md€ | CIO Online |
| Projets 9-20 M€ | 9 | DINUM |
| Projets 20-100 M€ | 30 | DINUM |
| Projets >100 M€ | 6 | DINUM |
| Durée moyenne | 6,3 ans | DINUM |
| Retard moyen | 21 % | DINUM |
| Surcoût moyen | 6,5 % | DINUM |
| Surcoût moyen (1er sem. 2024) | 17,5 % | DINUM |

### 1.2 Le vrai surcoût

Le surcoût officiel de 6,5 % est un artefact statistique pour plusieurs raisons :

1. **Exclusion des projets sortis** : GMBI (DGFiP) est sorti du panorama alors qu'il était encore en développement. La Cour des comptes a signalé des sorties de périmètre abusives.

2. **Réduction de périmètre** : Un projet « réussi » est souvent un projet dont le périmètre fonctionnel a été réduit pour respecter le budget initial. Les fonctionnalités abandonnées ne sont pas comptées comme surcoût.

3. **Coûts exclus** : Les coûts de maintenance, d'hébergement, de formation et de migration après mise en production ne sont pas inclus dans le budget du projet.

4. **Déclarations ministérielles** : Les données sont déclarées par les ministères eux-mêmes, sans vérification indépendante. La Cour des comptes confirme que la DINUM n'a qu'un « accès partiel aux données des projets via Chorus ».

### 1.3 Évolution

Le panorama passé de 57 projets (2016) à 45 (2025). Cette baisse peut être interprétée de deux façons : soit l'État concentre ses efforts sur moins de projets, soit les projets sont fractionnés pour rester sous le seuil des 9 M€ échappant ainsi au contrôle de la DINUM.

## §2 LES PROJETS EMBLÉMATIQUES

### 2.1 Chorus (DGFiP)

| Métrique | Valeur |
|----------|--------|
| Budget | 292,7 M€ cumulés |
| Périmètre | SI financier de l'État (24k utilisateurs) |
| Technologie | SAP |
| État | Migration S/4HANA réussie mai 2024 (78,4 M€) |
| Problème | État ne possède pas le code source. Cour des comptes 2026 : « défaut de cadrage et de pilotage stratégique » |

Chorus est à la fois le plus gros projet et le plus emblématique des contradictions du SI public : l'État a confié son système financier central à un progiciel propriétaire (SAP) dont il ne contrôle ni le développement ni l'évolution. La migration S/4HANA a coûté 78,4 M€ supplémentaires, sans que l'État n'acquière jamais la propriété intellectuelle.

**Fait atomique** : F-GP-001 — Chorus : 292,7 M€, SAP propriétaire, État sans code source. Migration S/4HANA 78,4 M€.

### 2.2 SIRHEN (Éducation nationale)

| Métrique | Valeur |
|----------|--------|
| Budget | 188,1 M€ |
| Périmètre | Gestion RH de l'Éducation nationale |
| État | Dépassements budgétaires documentés |

SIRHEN devait moderniser la gestion des carrières, paies et congés des personnels de l'Éducation nationale. Le projet a rencontré des difficultés de mise en œuvre majeures avec des dépassements budgétaires. Il illustre la difficulté de remplacer les systèmes hérités (souvent développés en interne depuis les années 1970-80) par des solutions modernes mutualisées.

**Fait atomique** : F-GP-002 — SIRHEN : 188,1 M€, dépassements budgétaires, difficultés mise en œuvre RH Éducation nationale.

### 2.3 Facturation électronique (MEFSIN)

| Métrique | Valeur |
|----------|--------|
| Budget | 258,7 M€ |
| Durée | ~8 ans (début ~2017) |
| État fin 2024 | Phase conception/réalisation |
| Retard | Significatif (pas de date de déploiement) |

Le projet devait généraliser la facturation électronique pour toutes les transactions B2G. Après 8 ans et 258,7 M€, le projet est encore en conception. La France a pris un retard considérable par rapport à d'autres pays européens (Italie, facturation électronique obligatoire depuis 2019 ; Espagne, depuis 2015).

**Fait atomique** : F-GP-003 — Facturation électronique : 258,7 M€, 8 ans, encore en conception fin 2024.

### 2.4 Paysage (MEFSIN)

| Métrique | Valeur |
|----------|--------|
| Budget | 59 M€ |
| Durée | >10 ans (initié 2014) |
| État | En cours |

Paysage est le projet le plus long du panorama. Démarré en 2014 au ministère de l'Économie, il dépasse les 10 ans de développement pour un budget de 59 M€. C'est l'exemple type du projet qui n'en finit pas.

**Fait atomique** : F-GP-004 — Paysage : 59 M€, >10 ans (2014-), projet le plus long du panorama.

### 2.5 4-Flight (DGAC/contrôle aérien)

| Métrique | Valeur |
|----------|--------|
| Budget initial | ~400 M€ |
| Surcoût | +100 % (~800 M€) |
| Retard | 10 ans |
| État | Partiellement déployé |

4-Flight, le système de contrôle aérien nouvelle génération, est le plus gros échec informatique de l'État français. Rapport Sénat 2023 : « 10 ans de retard, surcoûts de 100 %, ambitions drastiquement revues à la baisse ». Le projet a été lancé dans les années 2010 avec l'ambition de créer un standard européen. Aujourd'hui, il ne sera utilisé que par la DGAC française.

**Fait atomique** : F-GP-005 — 4-Flight : 400→800 M€ (+100%), 10 ans retard, standard européen abandonné.

### 2.6 NexSIS (Sécurité civile)

| Métrique | Valeur |
|----------|--------|
| Budget réévalué | 300 M€ (2018-2031) |
| Surcoût | +40 % |
| Retard | >3 ans |
| Déploiement mi-2025 | 9 départements seulement |
| Cible | Généralisation fin 2028 |

NexSIS devait unifier la gestion des appels d'urgence (18-112) des services d'incendie et de secours. Rapport Cour des comptes : l'agence ANSC est « sous-dimensionnée », le modèle économique est « fragile », le déploiement « standardisé » reste un défi.

**Fait atomique** : F-GP-006 — NexSIS : 300 M€, +40%, >3 ans retard, 9/101 départements mi-2025.

### 2.7 GMBI (DGFiP)

| Métrique | Valeur |
|----------|--------|
| Coût initial | 35,7 M€ |
| Coût réel | 56,4 M€ (+58 %) |
| Prestations externes | 25,1 M€ (2/3 du coût) |
| Mesures d'urgence | 19,2 M€ supplémentaires |

GMBI (gestion des biens immobiliers) a été retiré du suivi des grands projets alors qu'il était encore en développement. C'est le cas type du « projet qui disparaît du radar » quand il dérape.

**Fait atomique** : F-GP-007 — GMBI : 35,7→56,4 M€ (+58%), retiré du panorama pendant développement.

### 2.8 Linky SI (Enedis)

| Métrique | Valeur |
|----------|--------|
| Coût prévu SI | 273 M€ |
| Coût réel SI | 450 M€ (+64 %) |
| Projet global | 3,9→4,8 Md€ (+23 %, maîtrisé) |

Le SI du déploiement Linky a doublé (273→450 M€) alors que le projet global des compteurs n'a dérivé que de 23 %. Le SI s'est avéré beaucoup plus complexe que prévu.

**Fait atomique** : F-GP-008 — Linky SI : 273→450 M€ (+64%), surcoût SI concentré.

### 2.9 ANTS (Titres sécurisés) — Piratage 2026

| Métrique | Valeur |
|----------|--------|
| Incident | 15 avril 2026 |
| Comptes compromis | 11,7 millions |
| Faille | IDOR (probable) |
| Budget d'urgence | 200 M€ (France 2030) |
| Premier signalement | Septembre 2025 (non confirmé) |

L'ANTS, qui gère les titres d'identité des Français, a subi une fuite de 11,7 millions de comptes en avril 2026. Une première alerte en septembre 2025 avait été écartée par l'ANSSI comme « recyclage de fuites antérieures ». L'IGA enquête sur la chaîne de responsabilité.

L'ANTS illustre le paradoxe de la sécurité IT publique : 85-90 % externalisation, sous-traitance de la stratégie d'audit à des prestataires privés, et budget cybersécurité en baisse de 3 % en 2024-2025 pendant que la surface d'attaque explose.

**Fait atomique** : F-GP-009 — ANTS 2026 : 11,7M comptes piratés, 200M€ urgence, alerte sept. 2025 non traitée.

### 2.10 Mon Espace Santé

| Métrique | Valeur |
|----------|--------|
| Budget | >1 Md€ (estimation) |
| Taux d'activation | 15 % (janvier 2024) |
| Problème | Refus des médecins d'alimenter |

Le carnet de santé numérique est un échec d'adoption massif. Les médecins refusent d'alimenter les dossiers, les patients ne consultent pas. Mais le projet continue d'être développé.

**Fait atomique** : F-GP-010 — Mon Espace Santé : >1 Md€, 15% activation, échec adoption massif.

## §3 LES GRANDS ABSENTS DU PANORAMA

### 3.1 Les projets classifiés

Les projets de la Défense et de la sécurité nationale ne figurent pas dans le panorama public. Leur budget total est inconnu.

### 3.2 Les projets sous 9 M€

La Cour des comptes et le Sénat ont recommandé d'abaisser le seuil de contrôle à 5 M€ (Sénat 2023) et d'imposer une intervention systématique de la DINUM dès 50 M€ (Cour des comptes 2020). Aucune de ces recommandations n'a été suivie.

### 3.3 Les projets externalisés

Les projets développés en régie (par des agents publics) sont de plus en plus rares. La part des prestations externes dans les grands projets n'est pas publiée.

## §4 LES ÉCHECS STRUCTURELS RÉCURRENTS

### 4.1 Causes documentées (Cour des comptes, Sénat)

| Cause | Référence |
|-------|-----------|
| Absence de mesure des gains de productivité | Cour des comptes fév. 2025 |
| Intervention tardive de la DINUM | Cour des comptes 2020 |
| Accès insuffisant de la DINUM aux données Chorus | Sénat 2023 |
| Projets trop longs (>5 ans) | Recommandation Cour des comptes 2020 |
| Périmètre trop large, fractionnement insuffisant | Sénat 2023 (recommandation : fractionner en 5-20 M€) |
| Aucune sanction des dérives | Aucune mention dans aucun rapport |

### 4.2 Le biais des « projets réussis »

Un projet est « réussi » si :
- Le budget initial est respecté (même si le périmètre est réduit)
- Le logiciel fonctionne techniquement (même si personne ne l'utilise)
- Il est livré (même avec des années de retard)

Les indicateurs d'usage, d'impact, de satisfaction usager ou de gain de productivité ne sont jamais suivis.

### 4.3 L'absence de conséquences

Aucun directeur de projet, aucun chef de service, aucun prestataire n'a jamais été sanctionné pour l'échec d'un grand projet numérique. Les surcoûts sont absorbés par le budget de l'État, les retards sont justifiés par la complexité, les réductions de périmètre sont présentées comme des « recentrages stratégiques ».

## §5 QUELQUES CHIFFRES SUPPLÉMENTAIRES

| Échec passé | Coût | Source |
|------------|------|--------|
| Louvois (paie Armées) | 80 M€ + 156,4 M€ dysfonctionnements | Cour des comptes 2020 |
| ONP (paie fonction publique) | Excès d'ambition, abandonné | Cour des comptes 2020 |
| Cassiopée (Justice) | Plusieurs centaines de M€ | Cour des comptes 2020 |
| SI-DEP (dépistage COVID) | Développé en urgence, abandonné post-COVID | Presse |

**Fait atomique** : F-GP-011 — Aucune sanction pour échecs projets numériques État. Absorption systématique des surcoûts.

## §6 SYNTHÈSE

Les 45 grands projets numériques sont un **pipeline à dépenses** plutôt qu'un **programme de transformation**. Les caractéristiques structurelles :

1. **Pas de mesure d'impact** : personne ne vérifie si les projets tiennent leurs promesses
2. **Pas de sanction** : les dérives sont absorbées, pas corrigées
3. **Pas de transparence** : les données sont déclaratives, les périmètres sont ajustés, les projets sortent du radar
4. **Pas de limite de taille** : les projets de +50 M€ et +8 ans continuent d'être lancés
5. **Externalisation massive** : la part des prestations externes dans les grands projets n'est pas publiée

### Faisceau : Le panorama comme outil de communication

La publication semestrielle du panorama donne l'illusion d'un pilotage rigoureux. En réalité, c'est un outil de communication politique : il montre que « l'État se modernise » et que « la DINUM contrôle ». Mais les données sont incomplètes, les indicateurs sont biaisés, et aucune conséquence n'est tirée des dérives.

### Faisceau : Le fractionnement comme stratégie

Le passage de 57 (2016) à 45 (2025) projets peut cacher un fractionnement. Un projet de 15 M€ est plus facile à « réussir » qu'un projet de 50 M€. Le seuil de 9 M€ crée une incitation à déclarer les projets juste en dessous. Les projets en dessous du seuil représentent la majorité des 4-5 Md€ annuels — ils échappent à tout contrôle de la DINUM.

### Loup — 6,5 % de surcoût comme artefact

L'amélioration spectaculaire (17,5 % → 6,5 % en un an) est trop rapide pour être réelle. Elle résulte probablement d'un changement de méthodologie de calcul ou d'une exclusion de projets difficiles du périmètre. La Cour des comptes n'a pas validé ce chiffre.

### Loup — Les échecs ne coûtent rien à leurs responsables

Louvois a coûté 236 M€. Personne n'a été sanctionné. NexSIS a 3 ans de retard et +40 % de surcoût. Personne n'a été sanctionné. L'ANTS s'est fait pirater 11,7 millions de comptes. Personne n'a été sanctionné. L'absence de responsabilité est le moteur de la répétition des échecs.

### Loup — Le coût d'opportunité

Les 500+ M€ gaspillés sur les échecs des 10 dernières années (Louvois, ONP, Cassiopée, GMBI, Linky SI, 4-Flight dépassements) auraient pu financer l'ANSSI pendant 12 ans ou la DINUM pendant 6 ans.

---

**Pages** : §0-6
**Faits atomiques** : 11 (F-GP-001 à F-GP-011)
**Loups** : 4
**Sources** : DINUM panorama déc. 2025, Cour des comptes (2020, 2023, 2025), Sénat (2020, 2023), CIO Online, ZDNet, Contrepoints, Cour des comptes NexSIS, Sénat 4-Flight, AEF Info
