# Guide d'utilisation — SUBLIMATOR v34

Sublimator transforme N enquêtes journalistiques brutes en 1 article publiable, avec traçabilité forensique complète (chaque fait a une URL vérifiée). Le LLM fait le travail. Toi, tu valides aux checkpoints.

---

## Ce dont tu as besoin

1. **Un dossier d'enquêtes** dans `investigations/<sujet>/`. Une enquête = un fichier `.md`. Exemple : `investigations/2026-06-03_sumer_article/`.
2. **Mnemolite** (OBLIGATOIRE, via MCP). Le LLM hôte doit avoir un MCP configuré vers Mnemolite. Vérifie qu'il tourne : `get_system_snapshot` (outil MCP). Si Mnemolite est DOWN, Sublimator s'arrête — pas de mode dégradé.
3. **Un LLM hôte** (Claude, ChatGPT, Codebuff, Grok, Gemini…). N'importe lequel.

---

## Utilisation (3 étapes)

### Étape 1 — Lance Sublimator

Ouvre une session **fraîche** avec ton LLM hôte. Copie-colle l'intégralité du prompt système comme premier message :

```
tools/engines/sublimator/prompt-v34.md
```

Le LLM devient le pilote Sublimator. Il va te guider.

### Étape 2 — Donne-lui tes enquêtes

Juste après avoir collé le prompt, envoie un second message avec la liste des chemins :

```
Traite les enquêtes suivantes :
- investigations/2026-06-03_sumer_article/S_INVESTIGATION.md
- investigations/2026-06-03_sumer_article/R_INVESTIGATION.md
- investigations/2026-06-03_sumer_article/MA_INVESTIGATION.md
...

Dossier de sortie : investigations/2026-06-03_sumer_article/
```

Le LLM les lit une par une, extrait les faits, interroge Mnemolite, et produit des fiches YAML.

### Étape 3 — Valide aux 4 checkpoints

Le LLM s'arrête 4 fois pour te demander ton avis. Tu réponds par une lettre :

| Action | Signification |
|--------|-------------|
| **V** | Valider. Passe à la suite. |
| **M** | Modifier. Tu corriges un truc, puis V. |
| **R** | Refuser. Le LLM re-génère. Max 3 refus par CP. |
| **E** | Enrichir. Tu ajoutes du contexte, puis V. |
| **AIDE** | Rappelle cette liste. |

Les 4 checkpoints :

- **CP1** — Après chaque enquête. Le LLM te montre un résumé (nombre de faits extraits, URLs vérifiées, glyphes de fiabilité). Tu valides ou tu refuses.
- **CP2** — Après le YAML de synthèse. Le LLM te montre les 5 thèses cardinales, les transversalités détectées, le shadow factor global. Tu valides ou tu refuses.
- **CP2.5** — **LE PLUS IMPORTANT.** Le LLM produit un `rapport_synthese.md` lisible : pourquoi ces thèses ? pourquoi pas d'autres ? qu'est-ce qui est fragile ? que manque-t-il ? Il recommande ou non de passer à l'article. Tu lis ce rapport, tu décides.
- **CP3** — Après l'article. Le LLM te montre l'article complet, le rapport d'audit, les URLs vérifiées. Tu relis 30 minutes, tu valides, et tu publies sur Substack.

---

## Ce que tu obtiens

```
investigations/<sujet>/_quintessence/
  S_quintessence.yaml       ← 1 fiche par enquête
  R_quintessence.yaml
  ...

investigations/<sujet>/_synthese/
  synthese.yaml              ← synthèse cross-enquête (Phase 2)
  rapport_synthese.md        ← rapport lisible: justifications, critique, recommandation (Phase 2.5)

articles/
  2026-06-07_<sujet>_ARTICLE.md  ← article publiable
```

L'article contient :
- 3 000–5 000 mots (pas 8 000 : une thèse, pas un catalogue)
- Accroche immédiate (pas de « §0 Méthodologie »)
- Émoji H1 + sous-titre en italique
- Thèse unique défendue section par section
- Section `## Sources` avec URLs numérotées (pas de glyphes ✦✧⁅❧ visibles)
- 9 propositions de titre (3 choc, 3 forensiques, 3 conceptuels)

---

## En cas de problème

**Mnemolite DOWN.** Le LLM le détecte automatiquement (`get_system_snapshot`). Il s'arrête immédiatement. Aucun fichier n'est produit tant que Mnemolite n'est pas UP. Vérifie le serveur Mnemolite (`systemctl status mnemolite` ou équivalent).

**Mnemolite retourne 0 résultats.** Le LLM reformule ses requêtes 2-3 fois. Si toujours 0, il le note explicitement : la base n'est pas indexée pour ce sujet. Ce n'est pas bloquant (Mnemolite est UP, la base est juste vide sur ce thème).

**URL cassée.** Le LLM teste chaque URL. Si une URL retourne 404 ou timeout, le glyphe passe à ⁅ (source cassée). L'article le signale.

**3 refus consécutifs (L14).** Si tu refuses 3 fois le même checkpoint, le LLM s'arrête avec un bilan. L'état est préservé (les YAML déjà produits sont sauvés). Tu peux reprendre plus tard.
