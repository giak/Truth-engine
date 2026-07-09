# Prompts d'illustration — Article RIC

**Source** : `articles/2026-07-08_22-00_ric_verrouillage_francais_anatomie_ARTICLE.md`
**Méthode** : `promptsmith-leonardo v4` (FLUX 2 Pro) puis brainstorming Phoenix 1.0
**Date** : 2026-07-07

> **Note modèles** : Les prompts §3 FLUX 2 Pro ci-dessous sont optimisés pour le pipeline FLUX (prose naturelle, vocabulaire caméra, pas de négation). La section §4 contient une version optimisée pour **Phoenix 1.0** (Leonardo.ai) qui exploite ses forces : rendu de texte lisible, adhérence au prompt, langage naturel.

---

## §1 : Analyse du texte (La Moelle Épinière)

**Thèse Cardinale** : Le RIC n'est pas verrouillé par la Constitution seule — il l'est par l'indifférence de ceux qui le veulent. 237 ans d'absence documentée, 5 strates superposées, 73 % de favorables mais moins de 5 % de priorité. Le verrou est invisible parce qu'il n'a pas besoin d'être actif : l'indifférence suffit.

**Paradoxe Visuel** : Une porte monumentale verrouillée depuis 1789, dont la clé est suspendue à portée de main mais que personne ne saisit. L'écart entre la volonté déclarée (73 %) et l'action (moins de 5 %) est de 12 fois — un abîme statistique invisible à l'œil nu. La Constitution est « constitutionnellement incapable de se modifier ».

**Synecdoque** : Une urne électorale enfermée dans un coffre à 5 cadenas superposés, chacun gravé d'un article constitutionnel. La clé est là, mais le citoyen la regarde sans la prendre.

---

## §3 : Concepts Visuels (APEX)

### Concept #1 : La Forteresse de Papier

**Explication** : Le verrou constitutionnel comme architecture physique — une porte monumentale faite de strates de papier juridique empilées depuis 1789, chaque couche plus lourde que la précédente. La clé « RIC » est suspendue à portée de main, mais aucun geste ne se produit.

**Prompt FLUX 2 Pro** :

```text
A monumental archival door constructed from stacked layers of aged French legal documents and parchment, each layer visibly thicker and more compressed than the last, engraved with the year 1789. A single brass key labeled RIC hangs from a hook on the doorframe, within arm's reach, illuminated by a shaft of warm light. A silhouetted citizen stands before the door, hand half-raised but not grasping. The overall color palette utilizes deep black shadows #0a0a0f, a single warning amber highlight #ff6b35 on the key, and cold authority blue #2563eb ambient light seeping from behind the door. 85mm lens, dramatic chiaroscuro, cinematic photorealism with fine grain film texture.
```

---

### Concept #2 : L'Écart de 12x

**Explication** : Le paradoxe statistique visualisé comme un abîme architectural — deux colonnes/piliers démesurés dans un espace institutionnel, l'un flamboyant à 73 %, l'autre à peine visible à 5 %. L'écart de 12 fois est la mesure exacte du verrou.

**Prompt FLUX 2 Pro** :

```text
A vast institutional hall with towering stone columns, two massive pillars rising toward an unseen ceiling. One pillar blazes with intense warning amber light #ff6b35 at 73 percent of its full height, its light casting long dramatic shadows. The other pillar barely flickers at 5 percent with a faint cold blue glow #2563eb, almost extinguished. A lone citizen silhouette stands at the edge of the blazing pillar, staring across the dark chasm that separates the two. The floor is polished black marble reflecting deep black shadows #0a0a0f. 50mm lens, dramatic volumetric lighting from above, cinematic photorealism with documentary photojournalism aesthetic and subtle film grain.
```

---

### Concept #3 : Les Chaises du Conseil Vide

**Explication** : Le coût humain du verrou — 11 chaises vides dans une salle institutionnelle. Une seule est occupée. Les autres portent les traces de ceux qui ont tenté d'ouvrir la porte et ont été neutralisés. L'organisation existe, mais elle est éparpillée, atomisée.

**Prompt FLUX 2 Pro** :

```text
An institutional council chamber with eleven wooden chairs arranged in a scattered semicircle, not gathered around a table but pushed apart as if abandoned mid-session. Only one chair is occupied, a woman's silhouette illuminated by a single shaft of warm amber light #ff6b35. The other ten chairs stand in cold blue shadow #2563eb, some with faint nameplates barely legible, others simply gathering dust. The walls are dark paneled wood dissolving into deep black shadow #0a0a0f. Dust motes float in the single beam of light cutting diagonally across the room. 35mm lens, Rembrandt lighting with deep chiaroscuro, cinematic photorealism with grainy documentary texture.
```

---

## §4 : Version Phoenix 1.0 (Leonardo.ai) — La Forteresse de Papier

> **Modèle cible** : Phoenix 1.0 (Leonardo.ai, modèle propriétaire, 2025).
> **Forces exploitées** : rendu de texte lisible (1789, RIC, Article 11/89), adhérence élevée au prompt, langage naturel structuré.
> **Formule** : CRAFT implicite (Context, Rendering, Atmosphere, Fidelity, Tools).

### Variante A : La Porte aux 5 Verrous (recommandée)

> **Note sur le comptage** : Phoenix 1.0 ne peut pas compter exactement. La V3 (ci-dessous) décrit chaque serrure **individuellement** par sa position sur une colonne verticale unique, sans jamais dire « cinq ». Cinq descriptions = cinq serrures. Si le résultat donne 4 ou 6, utiliser « Iterate » pour ajuster.
>
> **Note sur « RIC »** : la clé est placée en **premier plan massif** (remplissant le tiers inférieur de l'image) pour que le texte gravé soit assez grand pour être lisible. Ne pas la mettre « accrochée au cadre » (trop petit), la mettre en avant-plan, suspendue à une chaîne qui descend du cadre vers l'objectif.

**Prompt Phoenix 1.0 (V3, serrures séquentielles + clé massive)** :

```text
An ultrarealistic monumental door made of thousands of compressed layers of aged parchment and constitutional texts, filling a dark institutional chamber. The year "1789" is deeply engraved in the stone lintel above. A vertical iron reinforcement bar runs from top to bottom of the door. On this bar, a brass lock at the very top is engraved with the text "Art. 11". Below it, a second brass lock is engraved "Art. 89". Below that, a third brass lock is engraved "Art. 16". Below that, a fourth brass lock is engraved "RIP 2008". At the very bottom, a fifth brass lock is engraved "BCE/UE". In the extreme foreground, filling the bottom third of the frame, a single oversized brass key suspended from a chain hangs close to the viewer, its handle engraved with the bold letters "R.I.C." catching a shaft of golden-amber light. Behind the key, a silhouetted figure stands dwarfed by the door, one hand slightly lifted but frozen mid-gesture. Dust motes float in the diagonal light beam. Deep black shadows dominate, cold blue ambient light seeps from beneath the door. Ultrarealistic, hyperdetailed textures, cinematic photorealism, 85mm lens, dramatic chiaroscuro, grainy documentary texture, raw photojournalism.
```

**Workflow Phoenix 1.0 recommandé** :

1. **Génération 1** : copier le prompt ci-dessus. Attendu : 5 serrures en colonne + clé « R.I.C. » massive au premier plan.
2. **Si trop/pas assez de serrures** : « Iterate » avec `remove the extra lock` ou `add a missing lock between the third and fourth locks`.
3. **Si « R.I.C. » absent** : « Iterate » avec `engrave the bold letters RIC on the handle of the large brass key in the foreground`.
4. **Si « 1789 » absent** : « Iterate » avec `engrave the year 1789 clearly in the stone lintel above the door`.

### Variante B : La Clé Suspendue (minimaliste)

```text
An extreme close-up of a single brass key suspended from a rusted hook on a massive doorframe made of compressed legal parchment layers. The key is engraved with the bold letters "RIC" that catch the light. The door behind it is deeply textured with visible layers of yellowed documents dating back to 1789, the year barely visible engraved in stone above. Warm amber light illuminates only the key and the immediate surrounding area, while the rest of the frame dissolves into deep black shadow with hints of cold blue ambient light. The composition suggests someone could take the key but chooses not to. Photorealistic, macro lens, shallow depth of field, fine grain film texture.
```

### Variante C : L'Archive Vivante (surréaliste)

```text
A surreal archival library where a massive doorway is framed not by stone but by living shelves of leather-bound legal volumes that have grown organically over centuries, their spines marked with dates from 1789 to 2026. A single brass key engraved "RIC" rests on a marble pedestal in the foreground, illuminated by a spotlight, while the doorway behind remains dark and impassable. A lone human silhouette stands at the edge of the light, facing the key but not approaching it. The shelves cast long shadows in deep black, the key glows with warm amber light, and a faint cold blue glow emanates from the darkness beyond the door. Cinematic photorealism, wide angle lens, volumetric lighting, museum exhibition aesthetic.
```

### Paramètres Phoenix 1.0

- **Model** : Leonardo Phoenix 1.0
- **Aspect Ratio** : 16:9 (paysage)
- **Guidance Scale** : 5-7 (Phoenix adhère bien au prompt, ne pas forcer au-delà de 7)
- **Steps** : 25-30 (défaut suffisant)
- **Negative Prompt** : laisser vide ou minimal (« blurry, low quality »)
- **Features** : activer « Prompt Magic » si disponible pour affiner l'adhérence

### Différences clés Phoenix vs FLUX 2 Pro

| Dimension | FLUX 2 Pro | Phoenix 1.0 |
|-----------|-----------|-------------|
| Rendu de texte | Faible, éviter | **Excellent**, exploiter |
| Adhérence au prompt | Bonne | **Très élevée** |
| Style de prompt | Prose naturelle 40-80 mots | Langage naturel structuré, plus détaillé |
| Palette | HEX codes utiles | Compréhension sémantique des couleurs |
| Consistance | Variable | **Forte** (Character Reference, LoRA) |

---

*Produit avec promptsmith-leonardo v4 (Pure Visual Brainstorming) + brainstorming Phoenix 1.0. Article source : 5257 mots, 9 sections, 5 dimensions transdisciplinaires.*
