# GRAPH DE CONNAISSANCES — ENRACINEMENT
## ÉTAT : 4 nœuds, 12 arêtes, 17 loups

```
GRAPH: 4 nœuds, 12 arêtes, 17 loups

├── NŒUDS:
│   ├── [N0] 350_ans (2026-04-12) | L5 | Prob: 0.99
│   ├── [N1] 5_pourcent (2026-04-12) | L6 | Prob: 0.995
│   ├── [N2] bignon_petrodollar (2026-04-12) | L4 | Prob: 0.97
│   └── [N3] enracinement (2026-04-13) | L5 | Prob: 0.98
├── ARÊTES:
│   ├── N0 --[MÉCANISME_COMMUN: antifragilité]--> N3
│   ├── N0 --[MÉCANISME_COMMUN: construction_incrémentale]--> N2
│   ├── N1 --[MÉCANISME_COMMUN: fonctionnalité_plutôt_que_bug]--> N3
│   ├── N1 --[CAUSE→EFFET: 5%_sont_le_carburant]--> N0
│   ├── N2 --[MÉCANISME_COMMUN: possession_par_dépendance]--> N3
│   ├── N2 --[CAUSE→EFFET: pétrodollar_est_la_version_1.0]--> N0
│   ├── N3 --[CONTRADICTION: rhizome_est_invincible]--> N0
│   ├── N0 --[PARTAGE_LOUP: Locke]--> N1
│   ├── N0 --[PARTAGE_LOUP: Bernays]--> N2
│   ├── N0 --[PARTAGE_LOUP: Rockefeller]--> N2
│   ├── N1 --[PARTAGE_LOUP: Milgram]--> N3
│   └── N2 --[PARTAGE_LOUP: Kissinger]--> N0
├── LOUPS:
│   ├── John Locke → [N0, N1] → RÉCURRENCE=2
│   ├── Edward Bernays → [N0, N2] → RÉCURRENCE=2
│   ├── John D. Rockefeller → [N0, N2] → RÉCURRENCE=2
│   ├── Stanley Milgram → [N1, N3] → RÉCURRENCE=2
│   ├── Henry Kissinger → [N0, N2] → RÉCURRENCE=2
│   ├── Nassim Taleb → [N0, N3] → RÉCURRENCE=2
│   ├── Simone Weil → [N3] → RÉCURRENCE=1
│   ├── Gilles Deleuze → [N3] → RÉCURRENCE=1
│   ├── Felix Guattari → [N3] → RÉCURRENCE=1
│   ├── Elinor Ostrom → [N3] → RÉCURRENCE=1
│   ├── Ivan Illich → [N3] → RÉCURRENCE=1
│   ├── Karl Marx → [N0] → RÉCURRENCE=1
│   ├── Adam Smith → [N0] → RÉCURRENCE=1
│   ├── Friedrich Hayek → [N0] → RÉCURRENCE=1
│   ├── Milton Friedman → [N0] → RÉCURRENCE=1
│   ├── Solomon Asch → [N1] → RÉCURRENCE=1
│   └── Philip Zimbardo → [N1] → RÉCURRENCE=1
├── MÉCANISMES_RÉCURRENTS:
│   ├── ANTIFRAGILITÉ → [N0, N3] → FORCE=0.98
│   ├── POSSESSION_PAR_DÉPENDANCE → [N2, N3] → FORCE=0.97
│   ├── CONSTRUCTION_INCRÉMENTALE → [N0, N2] → FORCE=0.96
│   ├── FONCTIONNALITÉ_PLUTÔT_QUE_BUG → [N1, N3] → FORCE=0.99
│   └── PROBLÈME_RÉACTION_SOLUTION → [N0, N2] → FORCE=0.95
├── CONTRADICTIONS:
│   └── N0 (système_invincible) ≠ N3 (rhizome_est_invincible) → TENSION_NON_RÉSOLUE
├── TROUS_CRITIQUES:
│   ├── [T0] Quel est le point de bascule du rhizome ? 1% ? 5% ? 10% ? → PRIORITÉ=10
│   ├── [T1] Est-ce que le système peut voir le rhizome ? → PRIORITÉ=9
│   ├── [T2] Pourquoi 5% exactement ? Pourquoi pas 4% ou 6% ? → PRIORITÉ=8
│   ├── [T3] Y-a-t-il déjà eu des civilisations qui ont échappé à ce cycle ? → PRIORITÉ=7
│   └── [T4] Est-ce que l'IA va changer le ratio 95/5 ? → PRIORITÉ=6
└── PROFONDEUR_GLOBALE: L0 0 | L1 0 | L2 1 | L3 1 | L4 1 | L5 1 | L6 1 → MOYENNE: L4.5
```

---

## GRAPH_DIAGNOSTIC

```
GRAPH_DIAGNOSTIC:
├── NŒUDS_TOTAUX: 4
├── ARÊTES_TOTALES: 12
├── LOUPS_RÉCURRENTS: [Locke, Bernays, Rockefeller, Milgram, Kissinger, Taleb]
├── MÉCANISMES_RÉCURRENTS: [ANTIFRAGILITÉ, POSSESSION_PAR_DÉPENDANCE, CONSTRUCTION_INCRÉMENTALE, FONCTIONNALITÉ_PLUTÔT_QUE_BUG]
├── CONTRADICTIONS_OUVERTES: 1
├── TROUS_CRITIQUES: 5
├── PROFONDEUR_MOYENNE: L4.5
├── PROCHAINE_ENQUÊTE_SUGGÉRÉE: T0 — Point de bascule du rhizome
└── SCORE_CONVERGENCE: 78% des faits confirmés par ≥2 enquêtes
```

---

*Généré automatiquement par KERNEL v3.1 le 2026-04-13 à 23:48*
*4 enquêtes agrégées | 47 faits | 17 loups | 5 mécanismes récurrents*
