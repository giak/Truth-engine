# DATA COVERAGE — vérité du bundle

## Portée générale

Ce bundle vise l’audit externe **de l’article V4.4 avec son corpus forensique**, pas seulement l’audit de sa prose.

Le socle `10_A7_FULL_CORPUS/` est l’extraction intégrale de `A7_EXTERNAL_RECONSTRUCTION_BUNDLE_V3.zip` du 12 septembre 2026 : **3 474 fichiers**. Il contient la base de preuves maître, le corpus forensique reconstruit des dossiers CLOSED, ses index/manifests, les archives d’investigation disponibles et le delta des investigations tardives.

Le corpus reconstruit documente **121 dossiers logiques CLOSED**, correspondant à **113 fichiers physiques présents**, avec les classes d’autorité suivantes : 96 handoffs originaux PRIMARY/CASE, 1 récupération bornée INV-044, 2 récupérations bornées INV-139/140 via INV-146, 13 synthèses, 8 objets contrôle/structurel réduits à 3 fichiers, et INV-035 explicitement absent.

## Règles d’autorité

1. Source primaire externe / pièce citée > artefact d’investigation.
2. Investigation détaillée / RUN_STATE / facts > handoff terminal pour l’audit de détail.
3. Handoff terminal = résultat certifié, mais pas pièce primaire externe.
4. SYNTHESIS = dérivé, **aucune preuve indépendante supplémentaire**.
5. RECOVERY = plafond explicite ; ne jamais le promouvoir en handoff original.
6. CONTROL/METHOD = méthode, pas preuve de cas.
7. Absence de fichier ≠ preuve d’absence du phénomène.

## Autorités dégradées connues

- `INV-035` : artefact terminal non récupéré ; **EXCLUDED** comme soutien autonome.
- `INV-044` : `BOUNDED_RECOVERY_HANDOFF`.
- `INV-139`, `INV-140` : récupération uniquement via `INV-146_SYNTHESIS.md`.
- `INV-156` : protocole reconstruit ; aucun replay canonique du registre n’est revendiqué.

## Delta tardif ajouté hors A7 / enrichi

Le répertoire `04_LATE_RUNTIME/` ajoute les livrables et fichiers machine encore accessibles pour les runs qui, dans A7, étaient surtout représentés par leurs handoffs.

| Investigation | Données supplémentaires présentes | Limite actuelle |
|---|---|---|
| INV-024 | INVESTIGATION, RUN_STATE, MNEMO | INPUT/CERT/NARRATIVE non récupérés ici |
| INV-031 | INVESTIGATION, INPUT, RUN_STATE, MNEMO | CERT/NARRATIVE non récupérés ici |
| INV-123 | INVESTIGATION, INPUT, RUN_STATE, MNEMO, CERTIFICATION | NARRATIVE non récupérée ici |
| INV-148 | INVESTIGATION ; PRE_COLLECTION + HANDOFF dans A7 | fichiers machine non récupérés ici |
| INV-149 | INVESTIGATION ; PRE_COLLECTION + HANDOFF dans A7 | fichiers machine non récupérés ici |
| INV-150 | INVESTIGATION ; PRE_COLLECTION + HANDOFF dans A7 | fichiers machine non récupérés ici |
| INV-151 | INVESTIGATION, RUN_STATE ; HANDOFF dans A7 | autres fichiers runtime non récupérés ici |
| INV-152 | INVESTIGATION, RUN_STATE, CERTIFICATION ; HANDOFF dans A7 | INPUT/MNEMO/NARRATIVE non récupérés ici |
| INV-153 | INVESTIGATION ; HANDOFF dans A7 | fichiers machine non récupérés ici |
| INV-154 | INVESTIGATION ; HANDOFF dans A7 | fichiers machine non récupérés ici |
| INV-155 | HANDOFF certifié dans A7 | livrable détaillé non récupérable sur la surface actuelle |
| INV-156 | INVESTIGATION, INPUT, RUN_STATE, MNEMO, NARRATIVE, CERTIFICATION ; HANDOFF dans A7 | autorité `PROTOCOL_RECONSTRUCTED_R3P1` |
| INV-157 | INVESTIGATION, RUN_STATE, MNEMO, NARRATIVE ; HANDOFF dans A7 | INPUT/CERT non récupérés ici |

`INV-084` est déjà présent dans la base A7 avec investigation, handoff et artefacts associés.

## Alstom

`05_ALSTOM/INVESTIGATION_ALSTOM_GE_MACRON_2026-09-12.md` est un delta postérieur au corpus des 113. Il n’est pas compté rétroactivement dans ce dénominateur.

## Ce que “toutes les data” signifie ici

Le bundle contient **tout le corpus maître reconstruit disponible + les deltas tardifs accessibles + les index de provenance et d’autorité**. Il ne fabrique pas les artefacts explicitement manquants ou non récupérables. Ces absences sont elles-mêmes des données d’audit.
