# PACTE SOURCAGE — Protocole de sourçage KERNEL v2.0

## Type: PROTOCOL · KERNEL v2.0 Protocol
**Date** : 2026-06-11 · **Type** : PROTOCOL · **Complexité** : SIMPLE · **Statut** : PROPOSITION

---

## §1 PRÉAMBULE — Pourquoi un protocole de sourçage

Le corpus Truth Engine contient des analyses de coordination, de répression, de mouvement sociaux. Ces analyses engagent la sécurité des personnes qui les lisent et les utilisent. Une source erronée peut mener à une décision dangereuse.

Le protocole de sourçage garantit :
- **Traçabilité** : chaque fait remonte à une source vérifiable
- **Fiabilité** : les sources sont classées par niveau de confiance
- **Pérennité** : les URLs sont archivées (Internet Archive, screenshots)
- **Transparence** : le lecteur sait ce qui est vérifié et ce qui ne l'est pas

---

## §2 HIÉRARCHIE DES SOURCES — Les 5 tiers

| Tier | Type | Exemple | Fiabilité | Usage |
|:----:|------|---------|:---------:|-------|
| **T1** | Source primaire vérifiée | Données officielles, arrêts de justice, rapports d'enquête parlementaires, études académiques peer-reviewed, photos/vidéos authentifiées | Haute | Fait central — peut fonder une thèse |
| **T2** | Source secondaire qualifiée | Articles de journaux référencés, rapports d'ONG, synthèses académiques, enquêtes de journalistes reconnus | Moyenne | Fait d'appui — peut illustrer une thèse |
| **T3** | Source tertiaire | Encyclopédies, articles de vulgarisation, synthèses non sourcées | Faible | Contexte — ne peut pas fonder une thèse |
| **T4** | Témoignage direct | Entretien, déclaration publique, citation de première main | Variable | À traiter avec précaution — nécessaire pour les gaps subjectifs |
| **T5** | Source anonyme/non vérifiable | Fuite, source interne anonyme, document non authentifié | Très faible | À mentionner avec avertissement explicite |

### Règles

1. **Un fait T1 est un fait. Un fait T2 est une indication. Un fait T3 est un contexte.**
2. **Jamais un Tier 3 seul ne peut fonder une thèse.** Un fait T3 doit toujours être corroboré par un T2 ou T1.
3. **Un fait T4 (témoignage) doit être croisé avec au moins une autre source de même type ou supérieure.**
4. **Les sources T5 sont interdites dans les APEX** — sauf mention explicite « information non vérifiable ».

---

## §3 LE SYSTÈME DE GLYPHES — Scoring visuel de fiabilité

| Glyphe | Signification | Condition |
|:------:|--------------|-----------|
| **✦** | Source Tier 1 + URL HEAD 200 OK + archive Internet Archive disponible | Source primaire fiable, accessible, archivée |
| **✧** | Source Tier ≥2 + URL HEAD 200 OK | Source secondaire accessible |
| **⁅** | URL présente mais 4xx/5xx (cassée) | Source inaccessible — chercher un miroir |
| **❧** | Pas d'URL (source absente) | Source non vérifiable — ne pas utiliser pour un fait central |

### Règles

1. **Tout fait FACT_REGISTRY doit avoir un glyphe.** Pas d'exception.
2. **✦** est le standard visé — tout fait important doit être Tier 1 + URL active.
3. **❧** est une alarme : si un fait important est ❧, l'enquête est incomplète.
4. **⁅** déclenche une recherche de source miroir (Internet Archive, DOI, version PDF).

---

## §4 INTERDICTION ABSOLUE — Wikipedia et assimilés

### 4.1 La règle

**Zéro Wikipedia dans le corpus.** Aucune exception.

Wikipedia est :
- Tier 2-3 (variable)
- Édité par des anonymes
- Changeable à tout moment
- Non fiable pour des faits sensibles

### 4.2 Que faire à la place

| Au lieu de Wikipedia | Utiliser |
|---------------------|----------|
| Article sur un événement | Source journalistique primaire (Le Monde, Mediapart, AFP), ou rapport officiel |
| Donnée statistique | Source officielle (INSEE, Eurostat, BEH, CNCDH) ou étude académique |
| Biographie | Page personnelle, entretien, article de presse référencé |
| Conflit/guerre | Rapport d'ONG (ICG, HRW, Amnesty), documentation officielle |

### 4.3 Sanction

Toute URL Wikipedia trouvée dans le corpus déclenche :
1. Identification du fait concerné
2. Recherche d'une source primaire équivalente
3. Remplacement de l'URL
4. Audit de l'enquête (combien de Wikipedia ?) → révision complète si >3 occurrences

---

## §5 FORMAT DES URLs

### 5.1 Règles

1. **URLs complètes** : pas de raccourcisseurs (bit.ly, t.co, etc.)
2. **HTTPS** obligatoire (sauf site inaccessible en HTTPS)
3. **URLs stables** : DOI préféré aux URLs dynamiques
4. **Date d'accès** : notée dans le commentaire ou metadata

### 5.2 Format standard

```
Source complète — https://example.com/chemin/vers/la/source
```

### 5.3 Sources multiples

Si un fait est corroboré par plusieurs sources :
```
Principale : https://...
Secondaire : https://...
```

---

## §6 ARCHIVAGE — Internet Archive

### 6.1 Règle

Toute URL dans le corpus doit être archivée sur Internet Archive (wayback machine) :
1. Aller sur https://web.archive.org
2. Coller l'URL
3. Cliquer « Save »
4. Noter l'URL d'archive dans les métadonnées

### 6.2 Pourquoi

- Les sites ferment, les articles sont dépubliés, les gouvernements censurent
- Une URL sans archive = un fait sans preuve dans 5 ans
- L'archive permet la vérification indépendante

---

## §7 SOURCES PAR TYPE DE SUJET

### 7.1 Sujets politiques français

| Type de source | Recommandé | Éviter |
|---------------|-----------|--------|
| Loi/décret | Légifrance | Wikipedia |
| Données économiques | INSEE, Banque de France | Médias grand public |
| Justice | Cour de cassation, Conseil d'État | Commentaires médiatiques |
| Police | IGPN, Défenseur des Droits | Rapports non officiels |
| Élections | Ministère de l'Intérieur, CEVIPOF | Sondages non référencés |

### 7.2 Mouvements sociaux

| Type de source | Recommandé | Éviter |
|---------------|-----------|--------|
| Répertoire | Base de données académique (CNRS) | Wikipedia |
| Bilan répressif | Amnesty International, ONU | Média unique |
| Concessions | Presse, sources officielles | Rumeur |
| Fractures | Rapports IGPN, enquêtes journalistiques | Réseaux sociaux |

### 7.3 Cas historiques internationaux

| Type de source | Recommandé | Éviter |
|---------------|-----------|--------|
| Conflit | ICG, HRW, Chatham House, IISS | Wikipedia |
| Traité | Texte officiel du traité | Commentaire |
| Insurrection | Chenoweth & Stephan, Sharp | Wikipédia |
| Guerre | Rapport d'enquête officiel, journalisme de terrain | Source unique |

---

## §8 VÉRIFICATION DES URLS — Protocole HEAD

Avant d'intégrer une source :
1. Vérifier que l'URL répond (HTTP 200)
2. Vérifier que le contenu correspond au fait cité
3. Vérifier la date de publication (un fait de 2026 avec une source de 2010 est suspect)
4. Archiver sur Internet Archive

---

## §9 MÉTADONNÉES — Informations à conserver par source

Pour chaque source dans le §13 SOURCES d'un APEX :

| Champ | Obligatoire | Exemple |
|-------|:-----------:|---------|
| Auteur | Oui | Balazard & Cottin-Marx |
| Titre | Oui | *Burn-out militant* |
| Éditeur/Publication | Oui | Payot |
| Date | Oui | 2025 |
| URL | Oui | https://... |
| Archive URL | Non mais recommandé | https://web.archive.org/... |
| Tier | Oui | T1 |

### Format

```
Auteur — *Titre* (Éditeur, Date) — https://...
```

---

## §10 GESTION DES SOURCES CASSÉES

Si une URL est cassée (⁅) :
1. Chercher sur Internet Archive (wayback machine)
2. Chercher le DOI (pour articles académiques)
3. Chercher une version PDF
4. Si rien trouvé → downgrade le fait (✦ → ✧ → ❧)
5. Si le fait est critique et la source perdue → mentionner explicitement

---

## §11 RÉFÉRENCES

Ce protocole s'inspire de :
- KERNEL v2.0 — GATE_G scoring protocol (glyphes ✦/✧/⁅/❧)
- Standards journalistiques : Reuter's Handbook, AFP Style Guide
- Standards académiques : APA 7e édition, Chicago Manual of Style
- Archivage numérique : Internet Archive, DOI, HAL (archive ouverte française)

---

## §12 CHECKLIST FINALE

Avant de publier un APEX, vérifier :
- [ ] Tous les faits FACT_REGISTRY ont un glyphe
- [ ] Aucune URL Wikipedia dans le document
- [ ] Toutes les URLs sont complètes (pas de raccourcisseur)
- [ ] Toutes les URLs sont en HTTPS
- [ ] Chaque source a auteur + titre + date + URL
- [ ] Les sources Tier 1 sont prioritaires
- [ ] Les sources cassées sont documentées (⁅)
- [ ] Les sources manquantes sont signalées (❧)
- [ ] Les sources sont classées par Tier
- [ ] L'Internet Archive a été utilisé pour les sources critiques

---

*Protocole KERNEL v2.0 — 5 tiers de sources, 4 glyphes de fiabilité, interdiction Wikipedia, vérification HEAD, archivage Internet Archive, 10 points de checklist. Garantit la traçabilité et la fiabilité de chaque fait du corpus.*