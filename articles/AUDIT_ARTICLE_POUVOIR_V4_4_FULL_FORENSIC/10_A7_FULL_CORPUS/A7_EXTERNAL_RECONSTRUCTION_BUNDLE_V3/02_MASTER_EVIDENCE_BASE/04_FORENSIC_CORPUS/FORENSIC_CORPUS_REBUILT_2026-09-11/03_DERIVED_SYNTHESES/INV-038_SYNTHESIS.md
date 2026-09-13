---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "dependency_synthesis"
artifact_id: "INV-038-SYNTHESIS"
version: "1.0-kiss"
status: "final"
updated: "2026-09-11"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-038"
truth_engine: "NOT_RUN_BY_DESIGN"
input_gate: "PASS"
---

<!-- TRACE: dependency_only=true; web_collection=false; truth_engine=false; dependencies=2/2 -->
<!-- DECISION: compare_mechanism_by_mechanism=true; country_bundle_inference=false -->

# INV-038 — Maroc et Algérie : influence politique, diplomatique et diasporique en France

## Gate d’entrée

Entrées terminales : `INV-130_RUN_HANDOFF.md` et `INV-131_RUN_HANDOFF.md`, toutes deux `CLOSED / DELIVERY_PASS_R3P1 / RENARD=NO`. Aucun web ni Truth Engine.

## Résultat central

La comparaison ne soutient pas une catégorie homogène « influence maghrébine ». Elle soutient des mécanismes partiellement isomorphes dont la force probatoire varie par chaîne. Maroc et Algérie disposent tous deux de relations étatiques explicites avec des institutions cultuelles en France ; ces relations ferment `État -> financement/personnel/accord -> capacité institutionnelle`, mais pas `diaspora -> relais politique/électoral`.

Les deux corpus contiennent aussi des mécanismes plus coercitifs ou clandestins, mais non isomorphes au même niveau : le Maroc ferme un ciblage Pegasus lié au Maroc sans fermer `information acquise -> levier -> politique`; l’Algérie ferme fortement une opération de repérage/enlèvement autour d’Amir Boukhors sans fermer le tasking/commandement final de l’État. Les canaux diplomatiques ouverts restent encore distincts : plaidoyer parlementaire aligné avec la position marocaine sur le Sahara d’un côté, leviers consulaires/visas et coopération administrative de l’autre.

## Comparaison appariée

| Mécanisme | Maroc | Algérie | Verdict comparatif |
|---|---|---|---|
| Culte / institutions religieuses | recrutement, financement, formation/désignation d’imams | financement, personnel, imams détachés, Grande Mosquée de Paris | **ISOMORPHE au niveau capacité institutionnelle** ; relais politique/électoral non établi dans les deux cas |
| Diplomatie / accès | groupe d’amitié et plaidoyer Sahara, alignement final sans causalité marginale isolée | leviers consulaires/diplomatiques réciproques, efficacité coercitive non générale | influence ouverte réelle, mécanismes différents |
| Opération clandestine | Pegasus : ciblage de responsables français | Boukhors : opération violente fortement documentée | clandestinité établie/fortement documentée ; effet politique terminal et commandement complet non fermés |
| Corruption / tasking | Moroccogate : chaîne publique finale non fermée | approches alléguées d’élus : pièce primaire manquante | **UNRESOLVED** des deux côtés |
| Diaspora | aucun pilotage politique général démontré | aucun pilotage politique général démontré | **NOT_ESTABLISHED** ; nationalité/origine ne vaut pas lien étatique |
| Effet électoral français | non établi | non établi | **NOT_ESTABLISHED** |

## Modèles concurrents

- **Diplomatie/cooperation ordinaires** : **SUPPORTED** pour plusieurs canaux ouverts.
- **Influence politique actor-specific** : **SUPPORTED/PARTIAL** sur des chaînes bornées, notamment plaidoyer et accès.
- **Tasking clandestin étatique** : **PARTIAL / case-specific**, sans chaîne terminale générale.
- **Coercition efficace** : **HETEROGENEOUS** ; existence d’un levier ne garantit pas son efficacité.
- **Pilotage politique de diaspora** : **NOT_ESTABLISHED**.
- **Architecture transversale coordonnée propre à chaque État** : **NOT_ESTABLISHED**.

## Plafonds causaux

`financement cultuel != tasking politique`; `proximité/diaspora != relais`; `plaidoyer -> décision alignée != causalité marginale`; `ciblage clandestin != levier politique démontré`; `mise en examen / procédure != commandement étatique final`; `un cas marocain != preuve sur l’Algérie` et inversement.

## Verdict

**SYNTHESIS PASS.** La comparaison Maroc/Algérie est utile précisément parce qu’elle empêche la fusion actor-first. Les deux États exercent des formes documentées d’influence ouverte et disposent de capacités institutionnelles en France ; certaines opérations clandestines sont également documentées. Mais les chaînes probatoires ne convergent pas vers un modèle commun de contrôle politique de diaspora, de capture systémique ou d’effet électoral français. La bonne unité d’analyse reste le **mécanisme + niveau de preuve**, pas la nationalité du sponsor.

## RENARD

`NO` — les gaps exigent pièces judiciaires/tasking définitives, dossiers internes de décision ou designs causaux ; collecte générique cumulative.

## Route

Résultat borné à transmettre à `INV-133` et à conserver comme contrôle de symétrie actor-specific.
