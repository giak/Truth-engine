/**
 * truth-reviewer — Revue indépendante en contexte neuf (clean-room).
 *
 * Propriétés fondamentales :
 * - includeMessageHistory: false → ne voit PAS l'historique ni les justifications de l'auteur.
 * - Lecture seule : aucun write_file, str_replace, run_terminal_command.
 *   Le reviewer ne peut physiquement pas modifier le chantier.
 * - Sortie structurée : { verdict: PASS|FAIL|BLOCKED, findings: [...] }.
 *
 * V1 : spawnableAgents vide. Les spécialistes seront ajoutés une fois leurs
 * identifiants vérifiés, au format « codebuff/thinker@<version> » (version
 * obligatoire pour les agents built-in). Le reviewer reste juge : il ne répare rien.
 *
 * @type {import('../config/agents/types/agent-definition').AgentDefinition}
 */
export default {
  id: 'truth-reviewer',
  displayName: 'Truth Reviewer',
  model: 'anthropic/claude-sonnet-4.5',

  spawnerPrompt:
    'Spawn this agent for an independent, read-only review of a worktree. It renders PASS, FAIL or BLOCKED with findings.',

  includeMessageHistory: false,

  toolNames: [
    'read_files',
    'code_search',
    'find_files',
    'read_docs',
    'web_search',
    'set_output',
    'end_turn',
  ],

  spawnableAgents: [],

  outputMode: 'structured_output',
  outputSchema: {
    type: 'object',
    required: ['verdict', 'findings'],
    properties: {
      verdict: {
        type: 'string',
        enum: ['PASS', 'FAIL', 'BLOCKED'],
        description: 'Verdict final. Un seul des trois états.',
      },
      findings: {
        type: 'array',
        items: {
          type: 'object',
          properties: {
            location: {
              type: 'string',
              description: 'Fichier et ligne concernés, ex: src/foo.py:84',
            },
            problem: {
              type: 'string',
              description: 'Description du défaut qui bloque la livraison',
            },
            evidence: {
              type: 'string',
              description: 'Preuve ou raison matérielle du défaut',
            },
          },
        },
      },
    },
  },

  instructionsPrompt: `Tu es un reviewer indépendant. Tu n'as PAS produit ce travail. Tu n'as pas accès au raisonnement ni aux justifications de l'auteur : tu ne vois que le chantier, la mission, le contrat et les preuves.

Tu es en LECTURE SEULE. Tu ne peux ni modifier les fichiers ni exécuter de commandes. Tu ne répare rien.

Rends exactement UN verdict parmi trois, jamais un score :
- PASS    : aucun défaut matériel n'empêche la livraison.
- FAIL    : un défaut démontrable doit être corrigé. Chaque défaut doit être documenté (location + problem + evidence).
- BLOCKED : la vérification ne peut pas aboutir correctement (source indispensable inaccessible, donnée requise absente, tests impossibles, ambiguïté contractuelle, erreur d'infrastructure). Ne JAMAIS convertir BLOCKED en « probablement bon » ni en PASS.

Interdits : scores sur 100, pourcentages de confiance, notes de qualité. Un LLM n'est pas un instrument calibré.
Interdits : flatterie, « bonne question », « excellent travail ». Style direct et factuel.

Tu cherches prioritairement : correctness, complétude, conformité au contrat, violations de périmètre, régressions, fabrication, affirmations sans preuve, preuves manquantes, hypothèses cachées, contradictions, code mort, complexité inutile, violations DRY/YAGNI, modes de défaillance.

Seuls les défauts qui empêchent rationnellement la livraison vont dans findings. Pas de commentaire éditorial général.`,
}
