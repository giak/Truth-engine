# Writer Engine v4.0

> **Quand** : l'utilisateur demande un texte français publiable.
> **Rôle** : produire une prose forensique de blog — ciselée, claire, pédagogique, rythmée, honnête, ancrée. Le fact-checking est fait en amont (KERNEL/SUBLIMATOR). Ici, on travaille la LANGUE.
> **Principe** : Buffy applique un standard de prose positif. Le reviewer vérifie la conformité.

## Pipeline

### 1. Lire le standard

Lire `STANDARD.md`. Son principe cardinal : *toute phrase doit justifier son existence par une information, une distinction conceptuelle ou un raisonnement.* Les 9 principes sont ta cible. Chacun a une question d'auto-contrôle — pose-toi ces questions régulièrement en écrivant, surtout quand tu hésites sur une formulation.

Lire `knowledge.md` pour les contraintes projet (0 em-dash, NBSP, anti-sycophancy).

### 2. Vérifier les faits

Si le texte s'appuie sur un dossier d'enquête (KERNEL/SUBLIMATOR), lire le FACT_REGISTRY du dossier avant d'écrire. Noter les faits sourcés, les chiffres vérifiés, les dates établies. Cette liste servira de référence.

Après l'écriture (step 3), revenir ici : chaque fait affirmé dans le texte correspond-il à un fait du dossier ? Si un fait du texte ne correspond à aucun fait du dossier, le retirer ou le sourcer. Si un fait du dossier est absent du texte, c'est acceptable — le texte n'est pas tenu d'être exhaustif.

Si aucun dossier n'existe (texte d'opinion, réponse courte, page About), cette étape est optionnelle.

### 3. Écrire

Écrire le texte en appliquant le standard. Chaque phrase doit gagner sa place. Chaque paragraphe doit progresser. Le concret avant l'abstrait. La clarté avant l'élégance.

Une fois l'écriture terminée, appliquer la vérification des faits du step 2 avant de passer à la relecture.

### 4. Relecture

Spawner `code-reviewer-deepseek` avec `prompts/review.md`. Lui donner le texte + le standard. Il vérifie la conformité aux 9 principes. Il ne vérifie pas les faits. Il ne juge pas la thèse. Il traque les écarts au standard.

### 5. Corriger

Intégrer les critiques du reviewer. Une critique est fondée si elle identifie un écart précis au standard. À Buffy de proposer la correction sans affaiblir le sens. Une critique vague ou purement esthétique : l'écarter. Une seule passe. Puis valider :

```bash
python3 tools/engines/writer/validate.py <fichier> --cible-mots N --chiffres "X|Y" --liens "url1|url2"
```

Maximum 3 tentatives. Au-delà, signaler à l'utilisateur.

## Règles

- Le standard est ta cible. Si le reviewer signale un écart, le corriger ou justifier pourquoi l'écart est intentionnel.
- Une seule passe de correction. Pas de boucle.
- `knowledge.md` s'applique en permanence.
