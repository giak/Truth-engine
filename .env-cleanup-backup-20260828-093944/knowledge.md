# Truth Engine — Project Knowledge

> Contrat d’intégration du runtime Truth Engine. Ce fichier route vers les autorités canoniques ; il ne les recopie pas.

## 1. Racine canonique

```text
TRUTH_ENGINE_ROOT := /home/giak/projects/truth-engine
KERNEL            := /home/giak/projects/truth-engine/truth-engine-v2/KERNEL.md
VERIFY             := /home/giak/projects/truth-engine/tools/verify/verify.py
INVESTIGATIONS     := /home/giak/projects/truth-engine/investigations
GLOBAL_AGENTS      := /home/giak/.agents
```

Le répertoire courant du projet appelant n’est jamais utilisé pour déduire ces chemins.

## 2. Frontière projet externe / Truth Engine

Un projet externe fournit le sujet, les documents, le contexte local et le livrable demandé.

Truth Engine reste propriétaire de :

- KERNEL et ses modules ;
- l’état d’exécution de l’investigation ;
- MnemoLite pour la mémoire du pipeline ;
- la vérification déterministe ;
- les fichiers sous `INVESTIGATIONS`.

Invariant :

```text
EXTERNAL_PROJECT != TRUTH_ENGINE_RUNTIME
```

Ne jamais redéfinir KERNEL, MnemoLite, les gates ou les chemins Truth Engine dans un projet appelant.

## 3. Autorités

```text
Investigation semantics  -> truth-engine-v2/KERNEL.md
Fact semantics           -> truth-engine-v2/protocol/FACT_VERIFICATION.md
Gate semantics           -> truth-engine-v2/forensic/GATES.md
Request accounting       -> truth-engine-v2/forensic/REQUEST_LOG.md
Output schema             -> truth-engine-v2/output/TEMPLATE.md
Deterministic verifier    -> tools/verify/verify.py
MnemoLite behavior        -> /home/giak/.agents/skills/mnemolite-mem-first/SKILL.md
MCP server configuration  -> /home/giak/.agents/mcp.json
```

Règle : `ONE RULE -> ONE OWNER -> N REFERENCES`.

En cas de contradiction, le propriétaire canonique ci-dessus prévaut. Ce fichier ne doit jamais contenir une copie divergente de sa règle.

## 4. Lancement d’une investigation

Quand l’utilisateur demande une enquête, une investigation ou explicitement KERNEL :

1. lire `KERNEL` au chemin absolu ci-dessus ;
2. exécuter ce KERNEL sans substituer le `knowledge.md` du projet appelant ;
3. conserver les sorties sous `INVESTIGATIONS` ;
4. utiliser les outils MnemoLite globaux si le client les expose correctement ;
5. appliquer exclusivement les commandes PRE/DELIVERY définies par la version courante de KERNEL.

Ne jamais reconstruire le protocole depuis un ancien exemple, un ancien `knowledge.md`, un transcript ou une mémoire MnemoLite.

## 5. MnemoLite

MnemoLite est une mémoire persistante, pas une preuve primaire.

Pour une investigation KERNEL :

- appliquer la cadence définie par KERNEL ;
- utiliser la mémoire comme warm route vers les faits, `memory_id`, URLs et gaps connus ;
- ne pas ajouter des recherches Mnemo redondantes hors protocole ;
- ne pas explorer OpenAPI/REST si le MCP natif fonctionne ;
- si le schéma MCP exposé par le client est invalide, utiliser le fallback défini dans le skill global et journaliser `TOOL_SCHEMA_UNAVAILABLE`.

Le skill global ne peut pas modifier les exigences probatoires d’une investigation KERNEL.

## 6. Vérification et livraison

Le contrat de livraison d’une investigation appartient uniquement à la version courante de KERNEL et à `verify.py`.

Pour KERNEL 2.9.4, les invocations contractuelles sont :

```text
python3 tools/verify/verify.py gate --file <INVESTIGATION_PATH> --kernel-contract pre
python3 tools/verify/verify.py gate --file <INVESTIGATION_PATH> --kernel-contract delivery
```

Un gate générique ne certifie pas une investigation KERNEL.

Les résultats de delivery restent externes au contenu sémantique du dossier conformément à KERNEL.

## 7. Discipline

- ne pas transformer ce fichier en documentation générale du dépôt ;
- ne pas y recopier RTK, Headroom, Sublimator, bugs d’outils, conventions historiques ou documentation JSON-RPC ;
- documenter ces sujets chez leur propriétaire ;
- vérité, provenance, anti-hallucination et absence de fabrication restent obligatoires, mais les contrôles détaillés appartiennent à KERNEL et à ses modules pour les investigations.
