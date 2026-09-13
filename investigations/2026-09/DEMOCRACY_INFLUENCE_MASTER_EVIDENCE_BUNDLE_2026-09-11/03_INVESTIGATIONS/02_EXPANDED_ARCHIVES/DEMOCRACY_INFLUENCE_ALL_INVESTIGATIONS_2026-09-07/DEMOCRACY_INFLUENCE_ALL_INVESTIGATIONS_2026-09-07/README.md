---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "master_bundle_readme"
artifact_id: "ALL-INVESTIGATIONS-2026-09-07"
version: "1.0"
status: "frozen"
updated: "2026-09-07"
---

# Bundle consolidé — toutes les données d'investigations

## Périmètre

Snapshot du programme `democracy-influence-investigations` au 7 septembre 2026 après fermeture d'INV-093.

Registre : **146 investigations**, dont **33 CLOSED**.

Ce bundle représente les **33 CLOSED** :
- 8 investigations structurales/méthodologiques (`INV-001..008`);
- 25 enquêtes/synthèses substantielles.

## Structure

- `00_CONTROL_PLANE/` — registre courant, TRACELOG, dashboard, control.py, README, METHOD_PACK, policy et audits.
- `01_RUNTIME_AND_CORPUS/` — Truth Engine R3P1 canonique, baseline Substack, snapshot bootstrap/control.
- `02_INVESTIGATIONS/` — données lisibles des 25 enquêtes/synthèses fermées.
- `03_STRUCTURAL_METHOD/` — INV-001/002 et METHOD_PACK représentant INV-003..008.
- `04_ROUTING_HISTORY/` — reclassifications du cycle final.
- `99_SOURCE_BUNDLES/` — bundles sources conservés pour traçabilité bit-à-bit.
- `STATUS_SNAPSHOT_ALL_146.csv` — registre complet figé.
- `CLOSED_INVESTIGATIONS_INDEX.csv` — index des 33 fermetures et niveau de packaging.
- `ANALYTIC_POINT_2026-09-07.md` — point analytique demandé.
- `MANIFEST_SHA256.csv` — SHA-256 de chaque fichier du bundle.

## Limites / récupération

- `INV-139` et `INV-140` : les artefacts terminaux originaux n'étaient plus disponibles dans la Library. Seuls les `RECOVERY_HANDOFF` bornés sont inclus. Ils ne recréent ni IDs ni octets absents.
- `INV-138` : aucun ZIP terminal canonique n'a été retrouvé ; ses artefacts canoniques individuels ont été réassemblés sous `CANONICAL_ASSEMBLED/`.
- Les copies Library suffixées `(1)`, `(2)`, etc. qui dupliquent des canoniques ne sont pas reprises systématiquement. Les versions canoniques et les bundles sources sont conservés.
- Les investigations non exécutées restent représentées par le registre, le backlog et le corpus, mais n'ont évidemment pas de faux artefacts d'exécution.

## Contrat de vérité

Le bundle ne transforme jamais :
`funding -> command`,
`coordination -> control`,
`operation -> effect`,
`official_statement -> proof`,
`legal -> legitimate`,
ou `convergence -> architecture`.

Voir `00_CONTROL_PLANE/CORE_INGERENCE_ROUTING_2026-09-06.md` et `METHOD_PACK.md`.
