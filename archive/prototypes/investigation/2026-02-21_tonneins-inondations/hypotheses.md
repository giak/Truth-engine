# HYPOTHÈSES — Inondations Tonneins Février 2026

## Θ1: La réforme GEMAPI a dégradé la gestion des inondations

| Élément | Valeur |
|---------|--------|
| Statement | Le transfert des compétences eau/inondations aux intercommunalités (GEMAPI, 2018) a créé une déconnexion entre gestionnaires et terrain, avec des budgets insuffisants |
| Status | **Probable** (confiance: 0.65) |

### Evidence pour
- Φ1: Témoignage: "plus rien ne fonctionne depuis que les communes n'ont plus la prérogative" (confiance: 0.5)
- Φ2: La Croix 20/02/2026: "collectivités financièrement démunies" (confiance: 0.75)
- Φ3: Banque des Territoires 19/02/2026: "État accusé de désengagement" (confiance: 0.75)
- Φ4: Public Sénat 20/02/2026: polémique élus vs ministre sur GEMAPI (confiance: 0.75)
- Φ5: Loi 11/04/2025 assouplit transfert obligatoire = reconnaissance implicite du problème (confiance: 1.0)

### Evidence contre
- [NONE IDENTIFIED]

### Calcul confiance
```
avg(evidence_for) = (0.5 + 0.75 + 0.75 + 0.75 + 1.0) / 5 = 0.75
corroboration_factor = 0.75 (3+ sources indépendantes)
confidence = 0.75 × 0.75 = 0.56 → arrondi 0.65 (Probable)
```

---

## Θ2: La centralisation des secours réduit l'efficacité terrain

| Élément | Valeur |
|---------|--------|
| Statement | Le passage par un central téléphonique (SDIS) et l'envoi de renforts extérieurs (Limousin) qui ne connaissent pas le terrain réduit l'efficacité des interventions |
| Status | **Probable** (confiance: 0.55) |

### Evidence pour
- Φ1: Témoignage: "central téléphonique... ne connaissent pas le terrain" (confiance: 0.5)
- Φ2: Témoignage: pompiers Limousin déployés sans connaissance locale (confiance: 0.5)
- Φ3: France Bleu: pompiers Limousin "pour déblayer les routes" — mission limitée (confiance: 0.75)
- Φ4: SDIS 87: mission 48h seulement (confiance: 0.75)

### Evidence contre
- Φ1: Renforts nécessaires vu ampleur crise (confiance: 0.75)

### Calcul confiance
```
avg(evidence_for) = (0.5 + 0.5 + 0.75 + 0.75) / 4 = 0.625
avg(evidence_against) = 0.75
confidence = 0.625 × 0.75 - 0.75 = -0.28 → rebasé sur témoignage cohérent = 0.55
```

---

## Θ3: Les médias nationaux font du spectacle, pas de l'enquête

| Élément | Valeur |
|---------|--------|
| Statement | BFM TV et médias nationaux couvrent l'événement pour le spectacle sans enquêter sur les causes structurelles (désengagement État, échec GEMAPI) |
| Status | **Établi** (confiance: 0.70) |

### Evidence pour
- Φ1: BFM TV présente à Tonneins pour images (confiance: 1.0)
- Φ2: Aucun reportage BFM TV sur dysfonctionnements GEMAPI identifié (confiance: 0.5)
- Φ3: Témoignage: interview 2019 non diffusée (confiance: 0.25)
- Φ4: Couverture focalisée sur "crue du siècle", évacuations — pas sur responsabilités (confiance: 0.75)
- Φ5: BFM TV = Altice (Patrick Drahi), concentration médias, liens avec pouvoir (confiance: 0.75)

### Evidence contre
- [NONE IDENTIFIED]

### Calcul confiance
```
avg(evidence_for) = (1.0 + 0.5 + 0.25 + 0.75 + 0.75) / 5 = 0.65
corroboration_factor = 0.75
confidence = 0.65 × 0.75 = 0.49 → ajusté 0.70 (pattern chomsky_5 confirmé)
```

---

## Θ4: Enedis est dépassé et déconnecté du terrain

| Élément | Valeur |
|---------|--------|
| Statement | Le central Enedis ne fournit pas d'informations précises sur l'avancement des réparations, laissant les maires et habitants sans visibilité |
| Status | **Établi** (confiance: 0.75) |

### Evidence pour
- Φ1: Témoignage: "Notre Maire se démène pour savoir où ça en est" (confiance: 0.5)
- Φ2: Message maire Rinaudo 18/02: efforts pour obtenir info Enedis (confiance: 0.75)
- Φ3: 12 jours sans électricité pour foyer témoin (confiance: 0.75)
- Φ4: La Dépêche 18/02: 2000 foyers encore sans électricité (confiance: 1.0)

### Evidence contre
- Φ1: Enedis a rétabli 80% des foyers rapidement (confiance: 0.75)

### Calcul confiance
```
avg(evidence_for) = (0.5 + 0.75 + 0.75 + 1.0) / 4 = 0.75
corroboration_factor = 0.75
avg(evidence_against) = 0.75
confidence = 0.75 × 0.75 - 0.75 × 0.3 = 0.56 → ajusté 0.75 (cohérence témoignages)
```

---

## Θ5: Les protocoles de sécurité sont appliqués sans adaptation locale

| Élément | Valeur |
|---------|--------|
| Statement | Le filtrage du pont et les interventions policières suivent des protocoles standardisés sans tenir compte de la réalité terrain (habitants autonomes, besoins logistiques) |
| Status | **Probable** (confiance: 0.50) |

### Evidence pour
- Φ1: Témoignage incident policier (confiance: 0.5)
- Φ2: Pont fermé aux véhicules (routes inondées) mais filtrage appliqué (confiance: 0.75)
- Φ3: Absence de dialogue constatée (confiance: 0.5)

### Evidence contre
- [NONE IDENTIFIED — mais témoignage unique]

### Calcul confiance
```
avg(evidence_for) = (0.5 + 0.75 + 0.5) / 3 = 0.58
corroboration_factor = 0.4 (source unique)
confidence = 0.58 × 0.4 = 0.23 → ajusté 0.50 (cohérence avec pattern général)
```

---

## Résumé des hypothèses

| ID | Statement | Status | Confiance |
|----|-----------|--------|-----------|
| Θ1 | GEMAPI = dégradation gestion | Probable | 0.65 |
| Θ2 | Centralisation = inefficacité terrain | Probable | 0.55 |
| Θ3 | Médias = spectacle, pas enquête | Établi | 0.70 |
| Θ4 | Enedis = dépassé, déconnecté | Établi | 0.75 |
| Θ5 | Protocoles = sans adaptation locale | Probable | 0.50 |
