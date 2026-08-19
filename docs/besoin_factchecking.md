# Besoin : fact-checking des données stockées dans Mnemolite

> Document de besoin. Énoncé minimal, en remplacement de l'empilement `boucle_de_verification.md` (2 532 lignes) + `architecture_verification.md` + `suivi_verification.md` + spec.
> Principes : KISS, DRY, YAGNI, pas d'overengineering. Freebuff d'abord, pas de LLM local.

## 1. Le besoin en une phrase

Tout fait, date, chiffre, pourcentage, thèse ou idée qui entre dans Mnemolite doit être vérifié contre une source primaire lue, classé (EPI), recoupé (≥ 2 familles indépendantes), daté et porteur d'une URL cliquable. Le vérificateur est Freebuff (agent principal à outils + sous-agents). Pas de LLM local : un modèle sans outils ne peut pas lire une source.

## 2. Démêler : deux problèmes, un seul besoin

Le chantier « vérification » a mélangé deux natures différentes.

### Problème A : le fact-checking (le besoin réel)

Vérifier la vérité du contenu : URL vivante, la source lue dit bien ce que le fait affirme, le chiffre, la date, le pourcentage sont exacts, la thèse est étayée, le recoupement est indépendant.

- Exige de fetch + lire la source. Donc un agent avec outils : web_search, read_url, read_files, MCP Mnemolite.
- C'est le cœur de Truth Engine.

### Problème B : la gate de livraison (orthogonal)

Vérifier la forme du livrable : nommage, em-dash, tests, branche protégée, horodatage non-futur, intégrité d'état (STATE_ID).

- Déterministe. Déjà fait : `verify.py check` / `certify`.
- Ce n'est pas du fact-checking et n'en sera jamais.

Règle de séparation : la vérité se vérifie avec un agent à outils ; la forme se vérifie avec un script. Un LLM sans outils ne peut pas fact-checker. Un script ne peut pas juger la vérité (AGENTS.md §4 : « un script déterministe ne doit pas traiter du texte produit par un LLM »).

## 3. Ce qui existe déjà et reste (ne pas refaire)

| Brique | Rôle | Statut |
|---|---|---|
| `truth-engine-v2/protocol/FACT_VERIFICATION.md` | échelle L0→L4, gate EPI, schéma du registre des faits | correct, canonique |
| `KERNEL.md` §10-13 + §19b | fetch → ancrage → recoupement → EPI → write-back `status:CONFIRME` | correct, câblé |
| `tools/verify_facts.py`, `detect_contradictions.py`, `monitor_urls.py`, `classify_legacy.py` | contrôles de structure (jamais la vérité) | correct, garder |
| `tools/verify/verify.py` check / certify | gate de livraison déterministe | correct, garder |
| `.agents/truth-verifier.ts` / `truth-reviewer.ts` | agents Freebuff (spawn premium, clean-room) | garder, chemin dégradé |

## 4. Ce qui est overengineered (couper / archiver)

1. Le reviewer local Ollama (`qwen3.6:35b`) dans `verify.py gate`. **Supprimé 2026-08-18.** Preuve de l'impasse : le modèle ne fetch rien (`/api/generate`, aucun outil), cutoff < 2026, hallucinait des faits (éditeur « L'Harmattan », « Blanchard 2021 »). Un fait ne se vérifie pas sans lire la source.
2. L'appareillage de preuve : fixtures, benchmark, `variance_*.json`, étude « 3/4 vs 4/4 ». **Supprimé 2026-08-18** (dossier `tools/verify/fixtures/`).
3. La doc hypertrophiée : `boucle_de_verification.md` 2 532 lignes, `architecture_verification.md` 332, `suivi_verification.md` 156, spec 135, soit ~3 155 lignes pour une gate qui tient en un script + un protocole. Résorber.

## 5. Ce qui manque (le vrai chantier)

Le besoin « tout ce qui est dans Mnemolite doit être vérifié » n'est pas opérationnalisé :

- Backlog factuel non vérifié : 6 436 mémoires factuelles (5 091 investigation, 1 019 note, 180 reference, 52 article, 94 quintessence), hors 33 612 `conversation` (non factuelles, 84 % des 40 107 au total). Le corpus legacy `livre-cst` (~3 942 claims) est au mieux L0 : le statut « C1 Confirmé » ≠ `status:CONFIRME` (FACT_VERIFICATION §11).
- Aucune campagne systématique de re-vérification L0→L4 du backlog. Seulement la vérification à la production (KERNEL) et à la demande.

## 6. Architecture cible (KISS : une boucle, deux temps)

Acteurs :

- Agent principal Freebuff : outils web_search + read_url + read_files + MCP Mnemolite. C'est le fact-checker.
- Sous-agent `truth-reviewer` (lecture seule, web_search/read) : clean-room premium, quand le runtime l'expose. Dans cette session, `spawn_agents` n'est pas exposé (confirmé lors du POC) : l'agent principal Freebuff suffit, ne pas construire dessus.

Boucle :

1. Production : chaque FCT-### monte L0→L4 (fetch → ancrage → recoupement ≥ 2 familles → gate EPI=FACT → ✦) puis write-back `status:CONFIRME`. Déjà dans KERNEL. Fait par l'agent principal.
2. Backlog : campagne de re-vérification des mémoires factuelles sans `status:` (et legacy `livre-cst`), par lots, via L0→L4. Menée par l'agent principal.
3. Livraison : `verify.py check`/`certify` (déterministe) avant tout write-back. Orthogonal, déjà fait.

Panne Freebuff : vérification reportée, jamais d'écriture non vérifiée. Aucun LLM local en substitution de fetch (supprimé).

## 7. Non-objectifs (YAGNI)

- Pas de vérificateur déterministe de la vérité (impossible et interdit, §4).
- Pas de gate LLM local (supprimé 2026-08-18).
- Pas d'infrastructure dépendant du spawn `base2-free`.
- Pas de score de confiance ni de pourcentage sur les faits.
- Pas d'expiration automatique des CONFIRME (déjà tranché).

## 8. Définition de « fait vérifié » (rappel du contrat)

`status:CONFIRME` = L4 : source primaire fetchée, ancrée (URL + locator + date), recoupée ≥ 2 familles indépendantes, classée EPI=FACT, datée `verifie-YYYY-MM-DD`, hash source, extrait verbatim. Cela garantit le processus enregistré, pas l'infaillibilité.

## 9. Ordre des travaux

1. Résorber l'overengineering (§4) : **FAIT** (Ollama supprimé de `verify.py`, fixtures supprimées, KERNEL §19a et README à jour). Reste : condenser `boucle_de_verification.md` / `architecture_verification.md` / `suivi_verification.md`.
2. Inventorier précisément le backlog non vérifié de Mnemolite (scan des mémoires factuelles sans `status:`).
3. Lancer la campagne de re-vérification par lots (priorité : legacy REFUTE/CANDIDAT, puis notes sans statut).
4. Garder la gate de livraison déterministe inchangée.

## 10. La chaîne complète : du KERNEL à l'article (traçage)

Le fait est vérifié UNE fois, au moment de l'investigation, puis circule par référence. La garantie « on ne se pose plus de question » est portée par le processus enregistré, pas par le LLM.

```
KERNEL (investigation)
  §10-13 : FCT-### = fetch → ancrage → recoupement → EPI → tier (✦ ✧ ⁅ ❧)
  §19b   : write-back → Mnemolite
           ✦ + L4 + EPI=FACT  → status:CONFIRME   (tier « sans question »)
           ✧ + L1-L3          → status:VERIFIE    (vérifié, source unique, re-questionnable)
  ✅ §19b reboucle le memory_id dans FACT_REGISTRY_V1 (colonne mem:, correctif 1 fait)
  ↓
Phase 1 (v36, quintessence) : §2 « Faits atomiques » + suffixe EPI:<classe> + mem:<uuid>
  ✅ mem: est lu verbatim depuis le registre (plus de recherche sémantique)
  ↓
Phase 2 (v37, rapport) : §2 « F-## sous-jacents » propage EPI + mem:
  ↓
Phase 3 (v38, article) : read_memory(id) → {source + URL + citation verbatim + date}
                         ZÉRO re-recherche, ZÉRO re-vérification (le write-back fait foi)
```

Invariant : un fait Mnemolite vaut « sans question » ssi `status:CONFIRME` (L4). Tout le reste (VERIFIE, sans status:, legacy) reste à questionner avant citation en aval. C'est le sens exact de « Mnemolite = pierre angulaire » : la pierre est sûre, pas magique.

## 11. Les 6 brèches mesurées (forensic, preuves sur disque)

1. ~~Le lien porteur (memory_id) n'est pas rebouclé.~~ **CORRIGÉ (correctif 1, 2026-08-18)** : §19b capture l'id, FACT_REGISTRY_V1 a la colonne mem:, Phase 1 lit verbatim. Reste à l'exécuter sur les prochains runs réels (les 146 quintessences YAML présentes sur disque restent sans `mem:` (grep = 0)).
2. Doublons dans le registre des faits. Deux mémoires distinctes pour le même fait « Check First = société privée à but lucratif » (ffe5c867-…, 4c7ca865-…), toutes deux status:CONFIRME. Le dédoublonnage par evidence_key (FACT_VERIFICATION §4) n'a pas joué. Violation du « une seule source de vérité ».
3. Drift résiduel dans le corps. Le fait pauvreté porte le tag status:VERIFIE mais son corps dit « ✧ / PLAUSIBLE », statut que le serveur rejette (FACT_VERIFICATION §9). Le tag a été corrigé, pas le contenu.
4. CONFIRME est structurellement rare. Pour un fait à émetteur unique (ex. INSEE, taux de pauvreté), ✦ exige ≥2 familles indépendantes, donc hors d'atteinte : tout tombe en ✧/VERIFIE. Le tier « sans question » couvre une minorité des faits, pas la majorité. La règle est juste ; la conséquence doit être assumée : la plupart des faits restent « à questionner ».
5. Backlog non vérifié. Legacy livre-cst (~3 942 claims au mieux L0) + mémoires sans status: cohabitent dans Mnemolite avec les CONFIRME. La pierre angulaire contient donc des données non vérifiées.
6. Le KERNEL n'émet pas le registre des faits en exécution réelle. Sur le dossier Conspiracy Watch (~50 fichiers de sortie), `verify_facts.py` rend « AUCUN REGISTRE TROUVÉ » : zéro bloc `FACT_REGISTRY_V1`, alors que KERNEL §10 l'exige et liste son absence comme violation de barrière. La colonne de glyphes (`✦✧⁕⁂⁅`) conflate la classe EPI et le tier de source : `⁕` (allégué) et `⁂` (hypothèse) sont hors vocabulaire `TIERS = {✦,✧,⁅,❧}`. Résultat : la prose est rigoureuse, mais rien n'entre dans Mnemolite en `status:CONFIRME`.

## 12. Correctifs minimaux (KISS : fermer les brèches, pas de nouvelle machine)

1. ~~Reboucler le memory_id.~~ **FAIT.** §19b capture l'id, FACT_REGISTRY_V1 a la colonne mem:, parseur + Phase 1 à jour, 228 tests passent.
2. Dédoublonnage au write-back. §19b exige dedup_check + traite duplicate_warning par update_memory (jamais un second write). Corriger les doublons Check First existants (fusionner).
3. Nettoyer le drift. Scan des corps pour le résidu « PLAUSIBLE » → réécrire le corps sans ce mot (le tag status:VERIFIE est déjà correct).
4. Étiqueter le tier partout. CONFIRME = sans question ; VERIFIE = à re-questionner. Déjà dans §6 de FACT_VERIFICATION ; le rendre visible dans les prompts v36/v37/v38 (c'est déjà écrit, le faire appliquer).
5. Campagne backlog. Re-vérifier L0→L4 le legacy livre-cst et les mémoires sans status:, par lots, par l'agent principal Freebuff (outils fetch + MCP).
6. ~~Forcer l'émission du FACT_REGISTRY_V1.~~ **FAIT (2026-08-19), règle souple.** Décision tranchée : le registre n'est exigé QUE pour les runs qui écrivent en Mnemolite (write-back ✦/L4), jamais pour la prose exploratoire (APPROFONDISSEMENT, GAPS, BLUEPRINT). EPI et tier sont séparés dans le bloc (epi = texte, tier ∈ {✦,✧,⁅,❧}) ; `⁕`/`⁂`/`⊗`/`⊙` (statuts épistémiques SYMBOLS.md) sont bannis du champ tier et reportés en EPI texte. La vérification se fait au sein de l'investigation, vers la fin, avant le Markdown final. Tout l'aval (Phase 1/2/3) lit `mem:` verbatim puis `read_memory(id)` : zéro re-recherche web. Mapping : ✦→EPI=FACT tier=✦ (CONFIRME) ; ✧→EPI=FACT tier=✧ (VERIFIE) ; ⁕→EPI=UNKNOWN ; ⁂→EPI=HYPOTHESIS.

Ce qui n'est PAS à construire (YAGNI réaffirmé) : pas de fact-checker LLM local (supprimé 2026-08-18), pas de vérificateur déterministe de vérité (§4), pas d'infra dépendant du spawn base2-free, pas de score de confiance.
