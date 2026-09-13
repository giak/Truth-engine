# BACKLOG STRUCTURE AUDIT — post INV-002

**Verdict : FAIL de la structure plate v0.5 ; PASS après refactor v0.6.**
**Aucune investigation de fond lancée.**

## 1. Défauts constatés dans v0.5

1. `INV-003..008` mélangeaient des règles méthodologiques avec des investigations de fond. Elles deviennent des `CONTROL_SPEC` et ne consommeront aucun run Truth Engine séparé.
2. Plusieurs objets étaient de vraies synthèses mais apparaissaient comme des runs primaires (`INV-040`, `052`, `068`, `082`, `088`, `095`, `102`, `104`, `129`). Ils sont désormais bloqués derrière leurs evidence packs.
3. Six recouvrements suffisamment forts créaient du travail redondant : `020→019`, `050→049`, `055→058`, `060→059`, `083→081`, `086→085`.
4. `INV-038` violait l’atomicité en combinant Maroc et Algérie. Il devient une comparaison/synthèse après `INV-130` et `INV-131`.
5. Les réseaux d’élites nommés (`113..118`) étaient prêts à partir sans gate de matérialité. Ils deviennent conditionnels derrière `INV-132`.
6. `INV-101` (RIC) était mêlé au noyau causal alors qu’il relève surtout des alternatives institutionnelles : `DEFER_CONTEXT`.
7. `INV-110` utilisait un cadrage psychologique fragile (`learned helplessness`) : il devient conditionnel et doit être reformulé autour de l’efficacité politique/résignation empirique.
8. La priorité `P1` était saturée et donc non discriminante. L’ordre est désormais porté principalement par `wave + gate + dependencies`.
9. La requalification `SUBSTANTIAL_PRIOR/PARTIAL/NEW` d’INV-002 reste un **triage de couverture**, pas une certification probatoire. La nouvelle colonne `coverage_basis` qualifie seulement la solidité du lien au corpus (`STRONG/MEDIUM/THIN`), jamais la vérité.

## 2. Nouvelle typologie

- `STRUCTURAL` : intégrité/cartographie du corpus.
- `CONTROL_SPEC` : règles transverses du runtime, zéro run TE séparé.
- `PRIMARY` : enquête autonome.
- `CASE` : deep-dive rattaché à un objet plus large.
- `SYNTHESIS` : recompose uniquement après evidence packs.
- `CONDITIONAL_CASE` : n’existe comme run que si un lead matériel l’active.
- `MERGED` : ID conservé pour traçabilité, zéro run propre.
- `DEFER_CONTEXT` : hors chemin causal principal.

## 3. Compteurs v0.6

Total registry : **133** entrées (IDs historiques conservés + 4 ajouts structurels).

### Par type
- CASE: **13**
- CONDITIONAL_CASE: **7**
- CONTROL_SPEC: **6**
- DEFER_CONTEXT: **1**
- MERGED: **6**
- PRIMARY: **87**
- STRUCTURAL: **2**
- SYNTHESIS: **11**

### Par statut
- BACKLOG: **95**
- BLOCKED: **16**
- CLOSED: **2**
- CONDITIONAL: **7**
- DEFERRED: **1**
- MERGED: **6**
- READY: **6**

### Par lane d’exécution
- 0: **2**
- COND: **7**
- DEFER: **1**
- FINAL: **1**
- G0: **6**
- MAIN_DYNAMIC: **95**
- N/A: **6**
- PILOT: **5**
- SYNTH: **10**

`MAIN_DYNAMIC` n’est pas une batch : une seule prochaine investigation est choisie après chaque résultat selon `model_change > discrimination > dependency_unlock > coverage_gap > utility`. Aucun ordre artificiel de 100 sujets n’est figé.

## 4. Les 4 ajouts structurels

- `INV-130` — Maroc, enquête autonome.
- `INV-131` — Algérie, enquête autonome.
- `INV-132` — cartographie comparative des réseaux d’élites ; gate des cas 113..118.
- `INV-133` — synthèse systémique finale départageant les modèles concurrents.

Aucun autre sujet n’a été ajouté.

## 5. Merges DRY

| ID conservé | Exécuté dans | Motif |
|---|---|---|
| INV-020 | INV-019 | frontière soft/public/covert est un axe natif de l’architecture US |
| INV-050 | INV-049 | OSF France/UE doit être dans le même run que les flux/mécanismes OSF |
| INV-055 | INV-058 | financement public est un test d’accountability des ONG |
| INV-060 | INV-059 | les think tanks nommés sont les cas comparatifs de la cartographie française |
| INV-083 | INV-081 | propriété et dépendances économiques forment une même économie politique des médias |
| INV-086 | INV-085 | sélection des sujets et des experts sont deux gates éditoriaux du même mécanisme |

## 6. Synthèses bloquées

`INV-038`, `040`, `052`, `068`, `082`, `088`, `095`, `102`, `104`, `129`, `133`.

Elles ne doivent recevoir aucun prompt de recherche primaire avant satisfaction de leurs dépendances.

## 7. Gate réseaux d’élites

`INV-113..118` ne sont plus automatiquement `DO`.
D’abord `INV-132`. Un deep-dive n’est activé que si le comparatif produit :
- un lien matériel avec le sujet ;
- un mécanisme précis ;
- une chronologie testable ;
- des traces accessibles ;
- une question discriminante.

Notoriété, appartenance ou proximité sociale seules ne suffisent pas.

## 8. Vague pilote

Avant industrialisation, seulement **5 runs** représentatifs après METHOD_PACK :

1. `INV-010` — archive/intervention clandestine historique ;
2. `INV-019` — architecture institutionnelle publique/soft/covert ;
3. `INV-049` — flux privés/fondation/ONG ;
4. `INV-071` — dispositif étatique français de gouvernance informationnelle ;
5. `INV-103` — littérature empirique sur défiance/institutions.

**Revue après chaque run.** Le but est de vérifier que Truth Engine + RENARD produisent la bonne profondeur sur cinq familles de preuves différentes avant N exécutions.


## 8bis. Overlaps conservés volontairement

Le refactor ne fusionne pas tout ce qui partage des sources. Certains couples restent séparés car ils posent des questions causales différentes :

- `INV-045` (certification/fact-checking UE) != `INV-088` (synthèse générale de l’infrastructure de qualification).
- `INV-076` (aides publiques à la presse) != `INV-081` (économie politique globale des médias), mais `076` est rattaché à `081`.
- `INV-017` (cas Cambridge Analytica) != `INV-096` (microtargeting France/UE), mais `017` sert de cas de calibration.
- `INV-054` (contentieux stratégique des ONG) != `INV-129` (synthèse transversale lawfare/coercition juridique).

Règle : partager des sources ou un vocabulaire n’est pas suffisant pour fusionner ; la fusion n’est faite que lorsque le **test discriminant et le mécanisme principal** sont réellement les mêmes.

## 9. Chemin critique

```text
INV-001 PASS
  -> INV-002 PASS
  -> METHOD_PACK (INV-003..008 consolidés, zéro TE)
  -> PILOT x5, revu run par run
  -> MAIN_DYNAMIC (une investigation choisie à la fois)
  -> conditional cases seulement si gate matériel
  -> synthèses intermédiaires
  -> INV-133 final
```

## 10. Verdict

La v0.5 était trop plate pour être industrialisée sans risque de répétition, de synthèse prématurée et de coûts inutiles.

La v0.6 est **structurellement exploitable**, mais le prochain objet n’est toujours pas une investigation de fond :
**construire et auditer le METHOD_PACK à partir de INV-003..008 + Truth Engine + RENARD.**
