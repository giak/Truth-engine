# VocabF Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Créer une application web pour enrichir le vocabulaire français avec LLM local (Mistral/LM Studio), PostgreSQL + pgvector, et interface de révision spaced repetition.

**Architecture:** Application SvelteKit avec API routes, connexion directe à PostgreSQL MnemoLite, appels LM Studio pour enrichissement linguistique.

**Tech Stack:** SvelteKit, PostgreSQL + pgvector, LM Studio (Mistral), MnemoLite embedding

---

## Phase 1: Setup & Configuration

### Task 1: Initialiser le projet SvelteKit

**Files:**
- Create: `package.json`
- Create: `svelte.config.js`
- Create: `vite.config.ts`
- Create: `tsconfig.json`
- Create: `.env.example`

**Step 1: Créer package.json**

```json
{
  "name": "vocabf",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "vite dev",
    "build": "vite build",
    "preview": "vite preview",
    "check": "svelte-kit sync && svelte-check --tsconfig ./tsconfig.json",
    "lint": "eslint ."
  },
  "devDependencies": {
    "@sveltejs/adapter-auto": "^3.0.0",
    "@sveltejs/kit": "^2.0.0",
    "@sveltejs/vite-plugin-svelte": "^3.0.0",
    "svelte": "^4.2.0",
    "svelte-check": "^3.6.0",
    "typescript": "^5.0.0",
    "vite": "^5.0.0",
    "eslint": "^8.56.0"
  },
  "dependencies": {
    "pg": "^8.11.0",
    "dotenv": "^16.4.0"
  },
  "type": "module"
}
```

**Step 2: Créer svelte.config.js**

```javascript
import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter()
  }
};

export default config;
```

**Step 3: Créer vite.config.ts**

```typescript
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [sveltekit()]
});
```

**Step 4: Créer tsconfig.json**

```json
{
  "extends": "./.svelte-kit/tsconfig.json",
  "compilerOptions": {
    "allowJs": true,
    "checkJs": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "skipLibCheck": true,
    "sourceMap": true,
    "strict": true,
    "moduleResolution": "bundler"
  }
}
```

**Step 5: Créer .env.example**

```bash
# Database (MnemoLite)
DATABASE_URL=postgresql://user:password@localhost:5432/mnemolite

# LM Studio
LM_STUDIO_URL=http://localhost:1234/v1/chat/completions
LM_STUDIO_MODEL=mistral
```

**Step 6: Commit**

```bash
cd ~/projects/vocabf
git init
git add .
git commit -m "feat: initialize SvelteKit project"
```

---

### Task 2: Créer la structure des dossiers

**Files:**
- Create: `src/app.html`
- Create: `src/app.d.ts`
- Create: `src/routes/+page.svelte`
- Create: `src/routes/+layout.svelte`
- Create: `src/lib/db.ts`
- Create: `src/lib/llm.ts`

**Step 1: Créer src/app.html**

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%sveltekit.assets%/favicon.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>VocabF</title>
    %sveltekit.head%
  </head>
  <body data-sveltekit-preload-data="hover">
    <div style="display: contents">%sveltekit.body%</div>
  </body>
</html>
```

**Step 2: Créer src/app.d.ts**

```typescript
declare global {
  namespace App {
    interface Locals {}
    interface PageData {}
    interface PageState {}
    interface Platform {}
  }
}

export {};
```

**Step 3: Créer src/routes/+layout.svelte**

```svelte
<nav>
  <a href="/">Dashboard</a>
  <a href="/ajouter">Ajouter</a>
  <a href="/mots">Mots</a>
  <a href="/reviser">Reviser</a>
  <a href="/explorer">Explorer</a>
</nav>

<slot />

<style>
  nav {
    padding: 1rem;
    background: #f5f5f5;
    display: flex;
    gap: 1rem;
  }
</style>
```

**Step 4: Créer src/routes/+page.svelte (Dashboard)**

```svelte
<h1>VocabF</h1>
<p>Enrichissez votre vocabulaire français</p>
```

**Step 5: Commit**

```bash
git add src/
git commit -m "feat: add basic SvelteKit structure"
```

---

## Phase 2: Base de données

### Task 3: Créer les tables PostgreSQL

**Files:**
- Create: `scripts/init-db.sql`

**Step 1: Créer le script SQL**

```sql
-- Table principale des mots
CREATE TABLE IF NOT EXISTS mots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mot VARCHAR(255) NOT NULL,
    linguistique JSONB NOT NULL DEFAULT '{}',
    semantique JSONB DEFAULT '{}',
    registre JSONB DEFAULT '{}',
    ontologie JSONB DEFAULT '{}',
    embedding VECTOR(768),
    source VARCHAR(50) DEFAULT 'ajoute',
    tags TEXT[] DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Table de révision (spaced repetition)
CREATE TABLE IF NOT EXISTS revisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mot_id UUID REFERENCES mots(id) ON DELETE CASCADE,
    ease_factor FLOAT DEFAULT 2.5,
    interval INTEGER DEFAULT 0,
    repetitions INTEGER DEFAULT 0,
    lapses INTEGER DEFAULT 0,
    next_review TIMESTAMP,
    last_review TIMESTAMP,
    total_reviews INTEGER DEFAULT 0,
    correct_reviews INTEGER DEFAULT 0
);

-- Index
CREATE INDEX IF NOT EXISTS idx_mots_embedding ON mots USING hnsw (embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS idx_mots_mot ON mots USING gin (mot gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_revisions_next_review ON revisions (next_review);
```

**Step 2: Exécuter le script**

```bash
# Se connecter à MnemoLite PostgreSQL et exécuter
psql -h localhost -U user -d mnemolite -f scripts/init-db.sql
```

**Step 3: Commit**

```bash
git add scripts/init-db.sql
git commit -m "feat: add PostgreSQL schema for mots and revisions"
```

---

### Task 4: Créer le module de connexion DB

**Files:**
- Modify: `src/lib/db.ts` (créé précédemment)
- Create: `tests/lib/db.test.ts`

**Step 1: Créer src/lib/db.ts**

```typescript
import pg from 'pg';
import { DATATYPES } from 'pg';
import 'dotenv/config';

const { Pool } = pg;

export const pool = new Pool({
  connectionString: process.env.DATABASE_URL
});

export async function query(text: string, params?: unknown[]) {
  const start = Date.now();
  const res = await pool.query(text, params);
  const duration = Date.now() - start;
  console.log('Executed query', { text: text.substring(0, 50), duration, rows: res.rowCount });
  return res;
}
```

**Step 2: Écrire le test**

```typescript
import { describe, it, expect } from 'vitest';

describe('db', () => {
  it('should export pool', () => {
    expect(pool).toBeDefined();
  });
});
```

**Step 3: Commit**

```bash
git add src/lib/db.ts tests/lib/db.test.ts
git commit -m "feat: add database connection module"
```

---

## Phase 3: Intégration LLM

### Task 5: Créer le module LLM

**Files:**
- Create: `src/lib/llm.ts`
- Create: `tests/lib/llm.test.ts`

**Step 1: Créer src/lib/llm.ts**

```typescript
import 'dotenv/config';

interface LLMResponse {
  definition: string;
  etymologie: string;
  synonymes: string[];
  antonymes: string[];
  champ_semantique: string;
  expressions: string[];
  concepts_philo: string[];
  registre: 'familier' | 'soutenu' | 'standard' | 'vieilli';
  conjugaison?: object;
}

const SYSTEM_PROMPT = `Tu es un expert de la langue française. Analyse le mot fourni et retourne un JSON avec les champs suivants:
- definition: définition claire et précise
- etymologie: origine et évolution du mot
- synonymes: tableau de synonymes
- antonymes: tableau d'antonymes
- champ_semantique: champ lexical associé
- expressions: expressions courantes utilisant ce mot
- concepts_philo: concepts philosophiques ou ontologiques liés
- registre: familier, soutenu, standard ou vieilli
- conjugaison: objet avec les conjugaisons (si verbe)

Retourne uniquement le JSON, sans texte supplémentaire.`;

export async function enrichWord(word: string): Promise<LLMResponse> {
  const response = await fetch(process.env.LM_STUDIO_URL || 'http://localhost:1234/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: process.env.LM_STUDIO_MODEL || 'mistral',
      messages: [
        { role: 'system', content: SYSTEM_PROMPT },
        { role: 'user', content: `Analyse le mot français suivant: "${word}"` }
      ],
      temperature: 0.3
    })
  });

  const data = await response.json();
  const content = data.choices[0].message.content;
  
  // Parse JSON from response
  const jsonMatch = content.match(/\{[\s\S]*\}/);
  if (!jsonMatch) {
    throw new Error('Invalid LLM response');
  }
  
  return JSON.parse(jsonMatch[0]);
}
```

**Step 2: Commit**

```bash
git add src/lib/llm.ts
git commit -m "feat: add LLM integration module"
```

---

## Phase 4: API Routes

### Task 6: API - Ajouter un mot

**Files:**
- Create: `src/routes/api/mots/+server.ts`
- Create: `tests/api/mots.test.ts`

**Step 1: Créer la route API**

```typescript
import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { enrichWord } from '$lib/llm';
import { query } from '$lib/db';

export const POST: RequestHandler = async ({ request }) => {
  const { mot } = await request.json();
  
  if (!mot) {
    return json({ error: 'Mot requis' }, { status: 400 });
  }
  
  // Appeler le LLM pour enrichir le mot
  const enrichment = await enrichWord(mot);
  
  // Insérer en base de données
  const result = await query(
    `INSERT INTO mots (mot, linguistique, semantique, registre, ontologie)
     VALUES ($1, $2, $3, $4, $5)
     RETURNING id`,
    [
      mot,
      JSON.stringify({ definition: enrichment.definition, etymologie: enrichment.etymologie }),
      JSON.stringify({ synonymes: enrichment.synonymes, antonymes: enrichment.antonymes, champ_semantique: enrichment.champ_semantique }),
      JSON.stringify({ expressions: enrichment.expressions, registre: enrichment.registre }),
      JSON.stringify({ concepts_philo: enrichment.concepts_philo })
    ]
  );
  
  return json({ id: result.rows[0].id, mot, enrichment });
};
```

**Step 2: Commit**

```bash
git add src/routes/api/mots/+server.ts
git commit -m "feat: add POST /api/mots endpoint"
```

---

### Task 7: API - Lister les mots

**Files:**
- Modify: `src/routes/api/mots/+server.ts`

**Step 1: Ajouter GET à la route**

```typescript
export const GET: RequestHandler = async ({ url }) => {
  const limit = url.searchParams.get('limit') || 20;
  const offset = url.searchParams.get('offset') || 0;
  const search = url.searchParams.get('search');
  
  let queryText = 'SELECT * FROM mots';
  const params: unknown[] = [];
  
  if (search) {
    queryText += ' WHERE mot ILIKE $1';
    params.push(`%${search}%`);
  }
  
  queryText += ' ORDER BY created_at DESC LIMIT $${params.length + 1} OFFSET $${params.length + 2}';
  params.push(limit, offset);
  
  const result = await query(queryText, params);
  
  return json({ mots: result.rows });
};
```

**Step 2: Commit**

```bash
git add src/routes/api/mots/+server.ts
git commit -m "feat: add GET /api/mots endpoint"
```

---

### Task 8: API - Recherche sémantique

**Files:**
- Create: `src/routes/api/mots/search/+server.ts`

**Step 1: Créer la route**

```typescript
import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { query } from '$lib/db';

export const GET: RequestHandler = async ({ url }) => {
  const q = url.searchParams.get('q');
  const limit = url.searchParams.get('limit') || 10;
  
  if (!q) {
    return json({ error: 'Query requise' }, { status: 400 });
  }
  
  // TODO: Générer embedding via MnemoLite
  // Pour l'instant, recherche textuelle simple
  const result = await query(
    `SELECT * FROM mots 
     WHERE mot ILIKE $1 
     OR linguistique::text ILIKE $1
     OR semantique::text ILIKE $1
     ORDER BY created_at DESC 
     LIMIT $2`,
    [`%${q}%`, limit]
  );
  
  return json({ mots: result.rows });
};
```

**Step 2: Commit**

```bash
git add src/routes/api/mots/search/+server.ts
git commit -m "feat: add semantic search endpoint"
```

---

### Task 9: API - Révisions spaced repetition

**Files:**
- Create: `src/routes/api/revisions/+server.ts`

**Step 1: Créer les endpoints de révision**

```typescript
import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { query } from '$lib/db';

// GET - Prochain mot à réviser
export const GET: RequestHandler = async () => {
  const result = await query(
    `SELECT m.*, r.next_review, r.ease_factor, r.interval
     FROM mots m
     JOIN revisions r ON m.id = r.mot_id
     WHERE r.next_review IS NULL OR r.next_review <= NOW()
     ORDER BY r.next_review ASC
     LIMIT 1`
  );
  
  return json({ revision: result.rows[0] || null });
};

// POST - Enregistrer résultat de révision
export const POST: RequestHandler = async ({ request }) => {
  const { motId, quality } = await request.json();
  // Quality: 0-5 (0= blackout, 5= perfect)
  // Algorithme SM-2 simplifié
  
  const result = await query(
    `SELECT * FROM revisions WHERE mot_id = $1`,
    [motId]
  );
  
  const rev = result.rows[0];
  
  let easeFactor = rev?.ease_factor || 2.5;
  let interval = rev?.interval || 0;
  let repetitions = rev?.repetitions || 0;
  let lapses = rev?.lapses || 0;
  
  if (quality >= 3) {
    // Réponse correcte
    if (repetitions === 0) {
      interval = 1;
    } else if (repetitions === 1) {
      interval = 6;
    } else {
      interval = Math.round(interval * easeFactor);
    }
    repetitions++;
  } else {
    // Réponse incorrecte
    repetitions = 0;
    interval = 1;
    lapses++;
  }
  
  easeFactor = Math.max(1.3, easeFactor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)));
  
  const nextReview = new Date();
  nextReview.setDate(nextReview.getDate() + interval);
  
  await query(
    `INSERT INTO revisions (mot_id, ease_factor, interval, repetitions, lapses, next_review, last_review, total_reviews, correct_reviews)
     VALUES ($1, $2, $3, $4, $5, $6, NOW(), $7, $8)
     ON CONFLICT (mot_id) DO UPDATE SET
       ease_factor = $2, interval = $3, repetitions = $4, lapses = $5,
       next_review = $6, last_review = NOW(),
       total_reviews = revisions.total_reviews + 1,
       correct_reviews = revisions.correct_reviews + $7`,
    [motId, easeFactor, interval, repetitions, lapses, nextReview, quality >= 3 ? 1 : 0]
  );
  
  return json({ success: true, nextReview, interval });
};
```

**Step 2: Commit**

```bash
git add src/routes/api/revisions/+server.ts
git commit -m "feat: add spaced repetition revision endpoints"
```

---

## Phase 5: Interface Web

### Task 10: Page Dashboard

**Files:**
- Modify: `src/routes/+page.svelte`

**Step 1: Implémenter le dashboard**

```svelte
<script lang="ts">
  let stats = { total: 0, aReviser: 0, aujourdhui: 0 };
  
  async function loadStats() {
    const res = await fetch('/api/stats');
    stats = await res.json();
  }
  
  loadStats();
</script>

<h1>VocabF</h1>

<div class="stats">
  <div class="stat">
    <span class="number">{stats.total}</span>
    <span class="label">Mots total</span>
  </div>
  <div class="stat">
    <span class="number">{stats.aReviser}</span>
    <span class="label">À réviser</span>
  </div>
</div>

<style>
  .stats {
    display: flex;
    gap: 2rem;
    margin: 2rem 0;
  }
  .stat {
    text-align: center;
  }
  .number {
    font-size: 2rem;
    font-weight: bold;
  }
</style>
```

**Step 2: Commit**

```bash
git add src/routes/+page.svelte
git commit -m "feat: add dashboard page"
```

---

### Task 11: Page Ajouter un mot

**Files:**
- Create: `src/routes/ajouter/+page.svelte`
- Create: `src/routes/ajouter/+page.server.ts`

**Step 1: Créer le formulaire**

```svelte
<script lang="ts">
  let mot = '';
  let loading = false;
  let result: any = null;
  let error = '';
  
  async function ajouter() {
    if (!mot.trim()) return;
    loading = true;
    error = '';
    
    try {
      const res = await fetch('/api/mots', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mot: mot.trim() })
      });
      
      if (!res.ok) throw new Error('Erreur lors de l\'ajout');
      
      result = await res.json();
      mot = '';
    } catch (e: any) {
      error = e.message;
    } finally {
      loading = false;
    }
  }
</script>

<h1>Ajouter un mot</h1>

<form on:submit|preventDefault={ajouter}>
  <input 
    type="text" 
    bind:value={mot} 
    placeholder="Entrez un mot français..."
    disabled={loading}
  />
  <button type="submit" disabled={loading || !mot.trim()}>
    {loading ? 'Enrichissement...' : 'Ajouter'}
  </button>
</form>

{#if error}
  <p class="error">{error}</p>
{/if}

{#if result}
  <div class="result">
    <h2>{result.mot}</h2>
    <pre>{JSON.stringify(result.enrichment, null, 2)}</pre>
  </div>
{/if}

<style>
  form {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
  }
  input {
    flex: 1;
    padding: 0.5rem;
    font-size: 1.2rem;
  }
  pre {
    background: #f5f5f5;
    padding: 1rem;
    overflow-x: auto;
  }
</style>
```

**Step 2: Commit**

```bash
git add src/routes/ajouter/
git commit -m "feat: add word addition page"
```

---

### Task 12: Page Liste des mots

**Files:**
- Create: `src/routes/mots/+page.svelte`

**Step 1: Créer la page**

```svelte
<script lang="ts">
  let mots: any[] = [];
  let search = '';
  let loading = false;
  
  async function searchMots() {
    loading = true;
    const url = search ? `/api/mots?search=${encodeURIComponent(search)}` : '/api/mots';
    const res = await fetch(url);
    const data = await res.json();
    mots = data.mots;
    loading = false;
  }
  
  searchMots();
</script>

<h1>Mes mots</h1>

<input 
  type="text" 
  bind:value={search} 
  on:input={searchMots}
  placeholder="Rechercher..."
/>

{#if loading}
  <p>Chargement...</p>
{:else}
  <ul class="mots-list">
    {#each mots as mot}
      <li>
        <a href="/mots/{mot.id}">{mot.mot}</a>
        <span class="date">{new Date(mot.created_at).toLocaleDateString()}</span>
      </li>
    {/each}
  </ul>
{/if}

<style>
  ul {
    list-style: none;
    padding: 0;
  }
  li {
    padding: 0.5rem;
    border-bottom: 1px solid #eee;
    display: flex;
    justify-content: space-between;
  }
</style>
```

**Step 2: Commit**

```bash
git add src/routes/mots/+page.svelte
git commit -m "feat: add mots list page"
```

---

### Task 13: Page Réviser

**Files:**
- Create: `src/routes/reviser/+page.svelte`

**Step 1: Créer la page de révision**

```svelte
<script lang="ts">
  let currentMot: any = null;
  let showDefinition = false;
  let loading = true;
  
  async function loadNext() {
    loading = true;
    showDefinition = false;
    const res = await fetch('/api/revisions');
    const data = await res.json();
    currentMot = data.revision;
    loading = false;
  }
  
  async function rate(quality: number) {
    await fetch('/api/revisions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ motId: currentMot.mot_id, quality })
    });
    loadNext();
  }
  
  loadNext();
</script>

<h1>Réviser</h1>

{#if loading}
  <p>Chargement...</p>
{:else if !currentMot}
  <p>Aucun mot à réviser !</p>
{:else}
  <div class="card">
    <h2>{currentMot.mot}</h2>
    
    {#if showDefinition}
      <div class="definition">
        <pre>{JSON.stringify(JSON.parse(currentMot.linguistique), null, 2)}</pre>
      </div>
      
      <div class="buttons">
        <button on:click={() => rate(0)}>0 - blackout</button>
        <button on:click={() => rate(1)}>1</button>
        <button on:click={() => rate(2)}>2</button>
        <button on:click={() => rate(3)}>3</button>
        <button on:click={() => rate(4)}>4</button>
        <button on:click={() => rate(5)}>5 - Parfait</button>
      </div>
    {:else}
      <button class="show-btn" on:click={() => showDefinition = true}>
        Voir la définition
      </button>
    {/if}
  </div>
{/if}

<style>
  .card {
    max-width: 600px;
    margin: 2rem auto;
    text-align: center;
  }
  pre {
    text-align: left;
    background: #f5f5f5;
    padding: 1rem;
  }
  .buttons {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    margin-top: 1rem;
  }
  button {
    padding: 0.5rem 1rem;
  }
</style>
```

**Step 2: Commit**

```bash
git add src/routes/reviser/+page.svelte
git commit -m "feat: add revision page with spaced repetition"
```

---

## Phase 6: Recherche sémantique & Explorer

### Task 14: Page Explorer - Visualisation

**Files:**
- Create: `src/routes/explorer/+page.svelte`

**Step 1: Créer la page d'exploration**

```svelte
<script lang="ts">
  let mots: any[] = [];
  let selectedMot: any = null;
  
  async function loadMots() {
    const res = await fetch('/api/mots?limit=50');
    const data = await res.json();
    mots = data.mots;
  }
  
  function selectMot(mot: any) {
    selectedMot = mot;
  }
  
  loadMots();
</script>

<h1>Explorer</h1>

<div class="explorer">
  <div class="mots-list">
    {#each mots as mot}
      <button 
        class:active={selectedMot?.id === mot.id}
        on:click={() => selectMot(mot)}
      >
        {mot.mot}
      </button>
    {/each}
  </div>
  
  <div class="detail">
    {#if selectedMot}
      <h2>{selectedMot.mot}</h2>
      <pre>{JSON.stringify(selectedMot, null, 2)}</pre>
    {:else}
      <p>Sélectionnez un mot</p>
    {/if}
  </div>
</div>

<style>
  .explorer {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 1rem;
    min-height: 400px;
  }
  .mots-list {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }
  .mots-list button {
    text-align: left;
  }
  .mots-list button.active {
    background: #e0e0e0;
  }
</style>
```

**Step 2: Commit**

```bash
git add src/routes/explorer/+page.svelte
git commit -m "feat: add explorer page"
```

---

## Fin

Le plan est complet. Voici les 14 tâches à exécuter.

**Prochaine étape:** Dois-je exécuter le plan (subagent-driven) ou prefers-tu ouvrir une nouvelle session ?

---

## Résumé des fichiers à créer

```
~/projects/vocabf/
├── package.json
├── svelte.config.js
├── vite.config.ts
├── tsconfig.json
├── .env.example
├── scripts/init-db.sql
├── src/
│   ├── app.html
│   ├── app.d.ts
│   ├── lib/
│   │   ├── db.ts
│   │   └── llm.ts
│   └── routes/
│       ├── +layout.svelte
│       ├── +page.svelte (Dashboard)
│       ├── ajouter/
│       │   └── +page.svelte
│       ├── mots/
│       │   └── +page.svelte
│       ├── reviser/
│       │   └── +page.svelte
│       ├── explorer/
│       │   └── +page.svelte
│       └── api/
│           ├── mots/
│           │   ├── +server.ts
│           │   └── search/+server.ts
│           └── revisions/
│               └── +server.ts
└── tests/
    ├── lib/
    │   ├── db.test.ts
    │   └── llm.test.ts
    └── api/
        └── mots.test.ts
```
