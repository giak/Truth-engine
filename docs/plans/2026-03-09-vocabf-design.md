# VocabF - Design Document

**Date:** 2026-03-09  
**Status:** Approuvé

## 1. Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Interface Web  │────▶│   SvelteKit     │────▶│  PostgreSQL     │
│   (SvelteKit)   │     │   (API + DB)    │     │  (Mnemolite)    │
└─────────────────┘     └────────┬────────┘     └─────────────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │  LM Studio      │
                        │  (Mistral LLM)  │
                        └─────────────────┘
```

## 2. Base de données

### Table `mots`

```sql
CREATE TABLE mots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mot VARCHAR(255) NOT NULL,
    
    -- Données linguistiques enrichies
    linguistique JSONB NOT NULL,  -- definition, etymologie, conjugaison, etc.
    semantique JSONB,              -- synonymes, antonymes, champ_lexical
    registre JSONB,                -- expressions, registres, nuances
    
    -- Ontologie / concepts
    ontologie JSONB,               -- concepts_philo, hiérarchie, relations
    
    -- Embedding pour recherche sémantique
    embedding VECTOR(768),
    
    -- Métadonnées
    source VARCHAR(50),            -- 'ajoute', 'import', 'decouverte'
    tags TEXT[],
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Table `revisions`

```sql
CREATE TABLE revisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mot_id UUID REFERENCES mots(id) ON DELETE CASCADE,
    
    -- Algorithme SM-2 (spaced repetition)
    ease_factor FLOAT DEFAULT 2.5,
    interval INTEGER DEFAULT 0,
    repetitions INTEGER DEFAULT 0,
    lapses INTEGER DEFAULT 0,
    
    next_review TIMESTAMP,
    last_review TIMESTAMP,
    
    -- Statistiques
    total_reviews INTEGER DEFAULT 0,
    correct_reviews INTEGER DEFAULT 0
);
```

### Index

```sql
CREATE INDEX idx_mots_embedding ON mots USING hnsw (embedding vector_cosine_ops);
CREATE INDEX idx_mots_mot ON mots USING gin (mot gin_trgm_ops);
CREATE INDEX idx_revisions_next_review ON revisions (next_review);
```

## 3. API Endpoints

| Méthode | Route | Description |
|---------|-------|-------------|
| `POST` | `/api/mots` | Ajouter un mot (trigger LLM processing) |
| `GET` | `/api/mots` | Lister mots (filtres, pagination) |
| `GET` | `/api/mots/[id]` | Détail d'un mot |
| `GET` | `/api/mots/search` | Recherche sémantique (pgvector) |
| `POST` | `/api/revisions` | Créer session de révision |
| `POST` | `/api/revisions/[motId]` | Enregistrer résultat révision |
| `GET` | `/api/revisions/next` | Prochain mot à réviser |

## 4. Interface Web

### Pages

1. **`/` Dashboard** — stats, mots récents, révisions à faire
2. **`/ajouter`** — formulaire ajout mot → appelle LLM
3. **`/mots`** — liste searchable avec filtres (registre, date, tags)
4. **`/mots/[id]`** — détail complet avec visualisations
5. **`/explorer`** — exploration visuelle (graphes de connexions)
6. **`/reviser`** — quiz avec spaced repetition

## 5. Flux LLM

```
User soumet "épistémologie"
        ↓
SvelteKit API → LM Studio (Mistral)
        ↓
Prompt structuré:
"Analyse le mot français 'épistémologie'.
Retourne JSON avec:
- definition
- etymologie  
- synonymes[]
- antonymes[]
- champ_semantique
- expressions[]
- concepts_philo
- registre (familier/soutenu/standard)
- conjugaison (si verbe)"
        ↓
Parse JSON → Insert PostgreSQL + embedding
        ↓
Return confirmation user
```

## 6. Stack

| Composant | Tech |
|-----------|------|
| Frontend | SvelteKit |
| Backend | SvelteKit (API routes) |
| Database | PostgreSQL + pgvector (MnemoLite) |
| LLM | LM Studio (Mistral) |
| Embeddings | MnemoLite (nomic-embed-text-v1.5) |
