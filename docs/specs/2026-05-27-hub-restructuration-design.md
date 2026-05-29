# HUB Restructuration : Architecture deux-étages

## Problème

Le HUB actuel (306 lignes) condense 16 articles + 40 articles pré-publiés + 38 enquêtes KERNEL + 746 faits vérifiés. Le lecteur voit un résumé, pas la masse sous-jacente. Le nouveau HUB doit être :
- **porte d'entrée** pour le lecteur qui arrive directement (navigation)
- **centre de navigation** pour le lecteur qui veut explorer

Approche retenue : **deux étages dans un seul article**.

## Structure générale

```
NIVEAU 1 — « Je veux la thèse » (~200 lignes)
├── §0 : Tableau de bord — 7 chiffres qui résument tout
├── §1 : Les 5 tensions ancrées (chaque § finit par → Sx)
├── §2 : Test des 3 réformes (inchangé) + transition niveau 2
│
◈◈◈ LIGNE DE FLOTAISON ◈◈◈
│
NIVEAU 2 — « Je veux voir l'enquête » (~350 lignes)
├── §3 : Les 16 articles en 4 actes (tableau navigation)
├── §4 : 40 articles pré-publiés (carte thématique)
├── §5 : 10 révélations que le débat public vous cache
└── §6 : Au-delà (Adieu aux partis, Protocole du ré-enracinement)
```

## Détail des sections

### §0 : Tableau de bord — 7 chiffres

Accroche sous forme de constantes vitales. 7 chiffres, chaque ligne = lien hypertexte vers l'article correspondant. Remplace l'incipit actuel.

Structure :
```
> 200 Md€ par an disparaissent des caisses publiques.
> 20 familles en captent la moitié.
> 9 milliardaires contrôlent 90 % de l'audience médiatique.
> 8M de Français sans médecin traitant.
> 57 % d'abstention.
> 100 000 fermes disparues en 10 ans.
> 70 % des données françaises sur serveurs américains.
>
> Ce n'est pas 7 problèmes. C'est un seul système : les 5 tensions du piège français.
```

### §1 : Les 5 tensions ancrées

Chaque tension conserve sa structure actuelle (thèse/antithèse/mécanisme) mais ajoute une phrase d'ancrage finale en italique :
- T1 → « *S2 documente les 80-100 Md€ d'évasion fiscale. S3 montre que la dette n'est pas la cause mais la trace.* »
- T2 → « *S15 détaille les 28×49.3, les 120 ordonnances, les 40 conventions d'impunité.* »
- T3 → « *S4 (8M sans médecin), S5 (9,8M pauvres), S7 (école), S9 (logement).* »
- T4 → « *S14 (AUKUS), S13 (UE-Mercosur), S6 (81 Md€ déficit commercial).* »
- T5 → « *S10 (arnaque climatique, ZFE), S11 (100 000 fermes), S8 (immigration).* »

### §2 : Test des 3 réformes

Identique au HUB actuel. Pas de modification. Ajout d'une transition visuelle vers le niveau 2 :
```
◈◈◈

Si vous voulez approfondir une tension, un article, ou voir comment les 40 enquêtes
antérieures ont construit ce diagnostic, la suite est pour vous.
```

### §3 : Les 16 articles en 4 actes

Tableau navigation structuré par acte. Chaque article = question directrice + fait-clé + lien.

```
ACTE 1 — LE DOSSIER D'ACCUSATION
S1 : La Caste Parasite — Qui gouverne et pour qui ? [fait-clé] [LIEN]
S2 : L'Argent qui disparaît — Combien extrait la caste ? [fait-clé] [LIEN]
S3 : La Dette instrumentalisée — Cause ou trace ? [fait-clé] [LIEN]
S15 : Le Verrou — Comment les institutions sont-elles neutralisées ? [fait-clé] [LIEN]

ACTE 2 — LES SCÈNES DE CRIME
S4, S5, S7, S9 : T3 — coût humain de l'extraction [LIENS]

ACTE 3 — L'ÉCHELLE DU CRIME
S10, S11, S6, S13, S14, S8, S16 : T4-T5 — souveraineté, climat, agriculture, numérique [LIENS]

ACTE 4 — LE VERDICT
HUB : le système est irréformable de l'intérieur
```

### §4 : 40 articles pré-publiés — la carte

Pas une liste plate. Carte thématique en 5 clusters :
1. Architecture du verrouillage : La démocratie en cage, La Machine à silence, L'Ingénierie de l'enclos, etc.
2. Mécanismes d'extraction : Comment la richesse verrouille le système, Budget 2026, etc.
3. Scènes de crime : France 2025, L'Empire des miettes, Le Grand manège, etc.
4. Dimension numérique : Le Goulag digital, Viginum, Le Narcotique numérique, etc.
5. La sortie : L'Adieu aux partis, Le Protocole du ré-enracinement

Chaque titre est un lien Substack. Pas de description — le titre suffit à orienter.

### §5 : 10 révélations

Format colonne : idée reçue ↔ réalité forensique. 5 tensions × 2 révélations.

```
1. « La France dépense trop » → L'État perd 200 Md€/an, il ne les dépense pas. (S2, S3)
2. « Les riches paient leur part » → Taux effectif 5-10 % GAFAM vs 25 % PME. (S2, S16)
... (10 lignes)
```

### §6 : Au-delà

Même contenu que le HUB actuel : L'Adieu aux partis + Le Protocole du ré-enracinement. + note sur le travail d'enquête (identique).

## Ligne de flottaison

Séparateur visuel entre niveau 1 (thèse) et niveau 2 (navigation) :
```
◈◈◈
⋮
◈◈◈
```

Le niveau 1 se lit debout dans le métro. Le niveau 2 se lit à un bureau, avec les onglets ouverts pour cliquer.

## Impact estimé

| Métrique | Actuel | Cible |
|----------|--------|-------|
| Lignes totales | ~306 | ~550 |
| Articles référencés | 16 | 16 + 40 |
| Liens explicites | ~8 | ~60 |
| Faits HUB | ~80 | 80 (inchangé) |
| Temps lecture niveau 1 | 8 min | 5 min (tableau de bord + ancrages) |
| Navigation possible | non | oui (tous les articles sont cliquables) |
