---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "post_run_review"
artifact_id: "INV-039-POST-RUN-REVIEW"
version: "1.0"
status: "pass"
updated: "2026-09-06"
canonical_ref: "INVESTIGATION_REGISTRY.csv"
inv_id: "INV-039"
---

<!-- DERIVED_FROM: te_run=20260906-1639-pouvoir-institutions-ue; certification=DELIVERY_PASS_R3P1 -->
<!-- DECISION: review=PASS; renard=NO; close=true -->

# POST-RUN REVIEW — INV-039

```text
P0 = 0
P1 = 0
P2 = 2
REVIEW = PASS
RENARD = NO
```

## ROBUSTE

1. `CLM-001` casse correctement le faux objet « qui gouverne l'UE ? » en séparant compétence, initiative, adoption, veto, mise en œuvre, budget, monnaie, justice et accès d'influence.
2. `CLM-002 / CTRL-002` conserve simultanément les deux faits nécessaires : les États restent constituants et détenteurs de veto dans certains domaines, mais aucun État ne dispose d'un veto général sous majorité qualifiée.
3. `CLM-003 / CTRL-001` distingue proprement le Conseil européen non-législateur en droit de son rôle politique réel d'agenda/crise/impasse.
4. `CLM-004..006 / CTRL-003` empêche de convertir initiative, codécision ou budget en suprématie institutionnelle générale.
5. `CLM-007..008` traite BCE et CJUE comme centres de pouvoir forts mais spécialisés, sans en faire un gouvernement général.
6. `CLM-009 / CAU-001` préserve la frontière fondamentale `accès/lobbying != capture != effet causal`.
7. La provenance est diversifiée : 16 SRC, 12 familles ; les règles formelles viennent principalement de sources institutionnelles primaires, tandis que les deux contrôles de fait utilisent CEPS et la Cour des comptes européenne.

## P2

1. `CAU-002` : la taille de l'effet causal propre des mandats du Conseil européen sur la vitesse ou le contenu des textes reste non identifiée. Le résultat central n'en dépend pas ; un test dossier par dossier serait nécessaire si cette causalité devient décisive.
2. `CAU-001` : l'effet causal général du lobbying sur le texte adopté reste hors de portée d'un registre de transparence. À traiter dans `INV-042` avec positions, amendements, chronologie et comparateurs, pas par accumulation de réunions.

## RENARD

```text
RENARD = NO
```

Les résiduels sont précisément des gaps d'identification causale. Une recherche générique supplémentaire ajouterait surtout des descriptions d'accès ou des cas d'intervention sans identifier le contrefactuel. Le modèle central est déjà discriminé par plusieurs familles et ne dépend d'aucune conclusion centrale mono-source.
