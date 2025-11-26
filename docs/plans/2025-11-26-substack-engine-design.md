# Substack Engine v1.0 - Design Document

**Date:** 2025-11-26
**Status:** Validated (Brainstorming complete)
**Author:** Claude + User

---

## 1. Architecture Overview

### 1.1 Objectif

Maximiser la portée des investigations Truth Engine via:
- **Tweets courts** (≤235 chars) avec hook accrocheur + lien Substack
- **Articles complets** sur Substack pour le contenu détaillé
- **Publication semi-automatisée** via API locale open-source

### 1.2 Stack Technique

| Composant | Solution |
|-----------|----------|
| API Publication | [JPres-Projects/Substack-API](https://github.com/JPres-Projects/Substack-API) |
| Serveur | localhost:8000 (REST API) |
| Auth | Email/password ou cookies (2FA) |
| Format Article | Markup natif API |
| Système Prompt | `prompts/systems/substack-engine-v1.0.md` |

### 1.3 Relation avec tweet-engine-v4.0

```
tweet-engine-v4.0.md          substack-engine-v1.0.md
├── HOOK_FORMULAS ──────────→ HOOK_FORMULAS (copié)
├── SECTION_TEMPLATES ──────→ SECTION_TEMPLATES (adapté ##)
├── CONCLUSION_TEMPLATE ────→ CONCLUSION_TEMPLATE (copié)
├── ANTI_LLM_BLACKLIST ─────→ ANTI_LLM_BLACKLIST (copié)
└── Mode LONG ──────────────→ Base article structure
```

---

## 2. Workflow

### 2.1 Invocation

```bash
claude "Mode SUBSTACK: logs/2025-11-26_sujet-investigation.md"
```

### 2.2 Phases

```
PHASE 0: INPUT
├── Fichier: logs/YYYY-MM-DD_sujet.md
└── Extraction: FactLedger, EDI, sources, wolves

PHASE 1: ANALYSIS
├── Identifier angle principal
├── Extraire 3-5 faits clés
└── Sélectionner hook formula appropriée

PHASE 2: GENERATION
├── 2.1 Tweet Hook (≤235 chars)
│   └── Hook formula + emoji
├── 2.2 Article Substack
│   ├── Titre + sous-titre
│   ├── Sections ## I, ## II...
│   ├── 👉 Conséquence par section
│   └── Conclusion L1-L2-L3
└── Preview → User validation

PHASE 3: PUBLICATION
├── POST /drafts/create-markup → draft_id
├── POST /drafts/{id}/publish → article_url
└── Compose tweet: hook + URL

PHASE 4: OUTPUT
├── prompts/outputs/YYYY-MM-DD_sujet-substack.md
├── prompts/outputs/YYYY-MM-DD_sujet-tweet.txt
└── prompts/outputs/YYYY-MM-DD_sujet-meta.json
```

---

## 3. Article Structure (adapté v4.0 LONG)

```markdown
# {TITRE ACCROCHEUR}
## {Sous-titre: hook_line ≤120 chars}

{Paragraphe d'accroche - contexte immédiat}

---

## I - {SECTION TITRE}

{Paragraph 1: thesis}

{Paragraph 2: facts from FactLedger}

{Paragraph 3: analysis}

👉 **Conséquence**: {angle explicite, ≤22 mots}

---

## II - {SECTION TITRE}

{Paragraph 1: thesis}

{Paragraph 2: facts}

{Paragraph 3: analysis}

👉 **Conséquence**: {angle explicite, ≤22 mots}

---

## CONCLUSION

{L1: Synthesis - ce que les faits démontrent}

{L2: Justification - 1 pivot number qui ancre}

{L3: Next step - question ouverte OU appel réflexion}
```

---

## 4. Publication (JPres-Projects/Substack-API)

### 4.1 Installation

```bash
git clone https://github.com/JPres-Projects/Substack-API.git
cd Substack-API
pip install -r requirements.txt
python change_env.py  # Configure credentials
python api_server.py  # → localhost:8000
```

### 4.2 Configuration

```bash
# .env (créé par change_env.py)
SUBSTACK_EMAIL=votre@email.com
SUBSTACK_PASSWORD=***
# OU cookies si 2FA:
CONNECT_SID=s%3A...
SUBSTACK_SID=...
```

### 4.3 Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/drafts/create-markup` | POST | Créer draft avec markup |
| `/drafts` | GET | Lister drafts |
| `/drafts/{id}/publish` | POST | Publier draft |
| `/docs` | GET | Documentation interactive |

### 4.4 Workflow API

```
1. POST /drafts/create-markup
   Body: { title, subtitle, body_markup, audience: "everyone" }
   → Response: { draft_id }

2. POST /drafts/{draft_id}/publish
   → Response: { url: "https://xxx.substack.com/p/slug" }

3. Compose tweet:
   "{hook}\n\n{article_url}"
```

---

## 5. Quality Gates

### 5.1 Tweet Hook

| Critère | Valeur |
|---------|--------|
| Longueur max | 235 chars (réserve 45 pour URL) |
| Hook formula | PROVOCATIVE \| CONTRARIAN \| CONSEQUENCE \| PATTERN \| EMOTIONAL \| REVELATION |
| Emoji | 1 seul, position initiale |
| Anti-LLM | Aucune phrase blacklistée |
| CTA | Question OU révélation (jamais "Cliquez") |

### 5.2 Article Substack

| Critère | Valeur |
|---------|--------|
| Titre | Hook formula + emoji |
| Sous-titre | ≤120 chars |
| Sections | Minimum 2 (## I, ## II) |
| Par section | 3 paragraphes + 1x 👉 Conséquence |
| Conclusion | Template L1-L2-L3 |
| Acronymes | Expansion première occurrence |
| Longueur | 800-2000 mots |

### 5.3 Anti-LLM Blacklist

```
BANNED_PHRASES:
- "Il est important de noter"
- "Force est de constater"
- "Dans un contexte où"
- "Il convient de souligner"
- "À l'heure où"
- "En définitive"
- "Cela étant dit"
- "En fin de compte"
- "Il va sans dire"
```

### 5.4 Checklist Pré-Publication

```
PRE-PUBLISH_CHECK:
□ Tweet ≤235 chars
□ Article 800-2000 mots
□ Zéro phrase Anti-LLM
□ Tous acronymes expandés
□ Sources citées (minimum 3)
□ 👉 Conséquence par section
□ Conclusion L1-L2-L3
□ API server running (localhost:8000)
```

---

## 6. Output Files

```
prompts/outputs/
├── YYYY-MM-DD_sujet-substack.md      # Article markdown (backup)
├── YYYY-MM-DD_sujet-tweet.txt        # Tweet: hook + URL
└── YYYY-MM-DD_sujet-meta.json        # Metadata
```

### 6.1 Format meta.json

```json
{
  "investigation_source": "logs/YYYY-MM-DD_sujet.md",
  "draft_id": "123456",
  "article_url": "https://xxx.substack.com/p/slug",
  "published_at": "2025-11-26T14:30:00Z",
  "tweet_chars": 234,
  "article_words": 1250
}
```

---

## 7. Prochaines Étapes

1. **Créer** `prompts/systems/substack-engine-v1.0.md` (système prompt complet)
2. **Installer** JPres-Projects/Substack-API
3. **Configurer** credentials Substack
4. **Tester** avec une investigation existante
5. **Itérer** selon feedback

---

## 8. Références

- [tweet-engine-v4.0.md](../../prompts/systems/tweet-engine-v4.0.md) - Source hooks/templates
- [JPres-Projects/Substack-API](https://github.com/JPres-Projects/Substack-API) - API publication
- [Truth Engine system.md](../../system.md) - Protocole investigation source
