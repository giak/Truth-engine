# MANIPULATION PATTERNS — Inondations Tonneins Février 2026

## Patterns détectés (Λ)

---

### Λ1: chomsky_5 — Filtres médiatiques

**Déclencheur**: Médias nationaux (BFM TV) cités dans couverture événement

| Critère | Évidence | Confiance |
|---------|----------|-----------|
| Propriétaire | Altice (Patrick Drahi) | 1.0 |
| Dépendance publicité | Oui (modèle économique TV) | 1.0 |
| Ratio sources officielles | Élevé (Météo-France, Préfet, Enedis cités) | 0.75 |
| Flak historique | Concentration médias Drahi, liens pouvoir | 0.5 |
| Anti-commun | Pas de débat sur échec politique/GEMAPI | 0.75 |

**Acteurs impliqués**: BFM TV, Altice

**Conclusion**: [MEDIA_CAPTURE] détecté — couverture sensationnaliste, absence d'enquête sur responsabilités

---

### Λ2: silence_qui_parle — Absences significatives

**Déclencheur**: always (appliqué systématiquement)

| Acteur absent | Attendu | Absence constatée | Interprétation |
|---------------|---------|-------------------|----------------|
| Président/Matignon | Visite zone sinistrée | Aucun déplacement annoncé | Crise non prioritaire politiquement |
| Ministre Écologie | Réponse sur GEMAPI | Dilatoire, renvoi aux collectivités | Évitement responsabilité |
| Intercommunalités | Présence terrain | Invisible | Incompétence/désengagement assumé |
| Médias nationaux | Enquête causes | Spectacle images | Éviter débat politique |

**Acteurs impliqués**: État central, intercommunalités, médias dominants

**Conclusion**: [NOTABLE_ABSENCE] — Les responsables de la gestion (État, interco) invisibles, laissant habitants seuls

---

### Λ3: biderman — Coercition par absurdité

**Déclencheur**: Conformité population malgré situation absurde

| Critère Biderman | Évidence terrain | Détecté |
|------------------|------------------|---------|
| Isolement | Zones inondées, pont fermé, pas de contacts pompiers | ✓ |
| Monopolisation | Central téléphonique unique (SDIS) | ✓ |
| Épuisement | 12 jours sans électricité, déplacements en bateau | ✓ |
| Menaces | Verbales (policier) | ✓ |
| Indulgences | Aucune identifiée | ✗ |
| Omnipotence | Protocoles immuables, pas d'exception | ✓ |
| Dégradation | Conditions de vie, animaux à soigner | ✓ |
| Exigences absurdes | Filtrer piétons sur pont, ne pas photographier piles | ✓ |

**Acteurs impliqués**: SDIS, Police, Administration

**Conclusion**: [PARTIAL_MATCH] — Situation de crise gérée par procédures rigides, créant absurdité vécue

---

### Λ4: spirale_silence — Coût du dissentiment

**Déclencheur**: Témoin évite interview BFM TV (expérience 2019: interview non diffusée)

| Élément | Évidence |
|---------|----------|
| Dissentiment | Critique système, GEMAPI, État |
| Conséquence | Interview 2019 non diffusée |
| Coût social | Être "le raleur" vs "victime résiliente" |
| Auto-censure | Refus interview 2026 |

**Acteurs impliqués**: Médias, témoin

**Conclusion**: [SPIRALE_SILENCE] — Les voix critiques sont filtrées, les discours consensuels (victimes résilientes) privilégiés

---

### Λ5: overton_window — Normalisation de l'échec

**Déclencheur**: Crises répétées (2019, 2021, 2026) sans changement structurel

| Étape Overton | État | Acteurs |
|---------------|------|---------|
| Impensable | L'État abandonne les zones inondées | — |
| Radicalement inacceptable | Perte compétences communes | — |
| Inacceptable | GEMAPI transfert interco | Loi 2014-2015 |
| Acceptable | Interco gère avec budgets insuffisants | Loi NOTRe |
| Sensible | Élus critiquent mais rien change | Débat 2026 |
| Populaire/Poliq | Loi 2025 assouplit mais ne revient pas | Statu quo |

**Acteurs impliqués**: Législateur, intercommunalités

**Conclusion**: [OVERTON_CONFIRMED] — L'échec de la gestion est devenu acceptable, les habitants s'adaptent

---

## Résumé des patterns

| Pattern | Statut | Confiance | Acteurs |
|---------|--------|-----------|---------|
| chomsky_5 | MEDIA_CAPTURE | 0.75 | BFM TV, Altice |
| silence_qui_parle | NOTABLE_ABSENCE | 0.80 | État, interco, médias |
| biderman | PARTIAL_MATCH | 0.60 | SDIS, Police, Admin |
| spirale_silence | CONFIRMED | 0.65 | Médias, témoin |
| overton_window | CONFIRMED | 0.70 | Législateur |

---

## Ce qui manque pour confirmer

| Pattern | Information manquante |
|---------|----------------------|
| biderman | Témoignages autres habitants, audit SDIS |
| spirale_silence | Statistiques diffusion interviews critiques |
| overton_window | Évolution discours politique 2014-2026 |

## Ce que le récit dominant omet

1. **Responsabilité politique**: GEMAPI, NOTRe, transferts compétences non financés
2. **Désengagement État**: Abandon progressif des zones rurales/périphériques
3. **Résilience forcée**: Habitants autonomes par nécessité, pas par choix
4. **Coût humain**: Fatigue, stress, animaux, économies — non comptabilisé
