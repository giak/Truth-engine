# PROMPT — AUDIT FORENSIQUE COMPLET DE L’ARTICLE V4.4

Tu reçois un bundle complet d’audit. Ta mission est de **tenter de casser l’article**, puis de conserver uniquement ce qui résiste.

## Ordre strict

### 1. Blind review
Lis uniquement `01_TARGET/`. Donne un verdict initial sans consulter les investigations.

### 2. Corpus authority review
Lis `00_READ_FIRST/DATA_COVERAGE.md`, `03_FORENSIC_INDEX/RECONSTRUCTION_REPORT.md`, `CORPUS_121_AUDIT.csv`, `SOURCE_INDEX.csv` et l’annexe forensique. Comprends les classes d’autorité avant de compter des dossiers.

### 3. Claim-by-claim trace
Pour chaque affirmation substantielle de l’article :
- identifie l’investigation qui la soutient ;
- retrouve le handoff / investigation détaillée / RUN_STATE disponibles ;
- vérifie que le statut publié ne dépasse pas le statut forensique ;
- identifie les gaps, contrôles négatifs et contre-hypothèses ;
- si le web est disponible, remonte aux sources primaires externes citées et vérifie-les.

### 4. Anti-double-counting
Ne compte jamais :
- une SYNTHESIS comme nouvelle preuve indépendante ;
- plusieurs copies du même handoff comme plusieurs corroborations ;
- un RECOVERY comme artefact terminal original ;
- un fichier METHOD/CONTROL comme preuve de cas.

### 5. Tests adversariaux obligatoires
Teste au minimum :
1. la thèse positive est-elle réellement démontrée ou seulement une discipline de prudence ?
2. “modifier l’espace des options” est-il falsifiable ?
3. les cas sont-ils comparés ou juxtaposés ?
4. existe-t-il du cherry-picking ?
5. les contre-cas peuvent-ils réellement faire perdre le modèle ?
6. le standard probatoire est-il symétrique entre USA/UE/Russie/Chine/acteurs privés ?
7. l’article confond-il parfois capacité, action, effet organisationnel, décision publique et effet politique final ?
8. Alstom suggère-t-il narrativement plus de causalité que le dossier n’en établit ?
9. les figures codent-elles une causalité plus forte que le texte ?
10. le volume de dossiers/références crée-t-il une illusion de robustesse par accumulation ?

## Sortie exigée

1. `PUBLISHABLE / PUBLISHABLE_AFTER_FIXES / NOT_READY`.
2. 5 problèmes les plus graves : sévérité, localisation, preuve, conséquence, patch minimal.
3. 5 éléments les plus robustes à préserver.
4. Carte des 15 claims centraux : `claim | article | investigation | autorité | verdict | gap | formulation sûre`.
5. Audit des 4 figures : `KEEP/FIX/DROP`.
6. Audit Alstom séparant : pression DOJ, fragilisation, vente, choix GE, autorisation française, instrumentalisation DOJ, quid pro quo/corruption, conséquences stratégiques.
7. Audit de symétrie probatoire.
8. Audit des contre-cas et falsifiabilité.
9. Audit factuel/source par source des points matériels si accès web.
10. Patch minimal ordonné, max 12 modifications.
11. Ce qui demeure inconclusif même après réécriture.

## Discipline

Pas de complaisance. Pas de faits inventés. Pas de “probablement” pour remplir un gap. Absence de preuve ≠ preuve d’absence. Une chronologie ≠ causalité. Un financement ≠ tasking. Un réseau ≠ coordination. Une exposition ≠ persuasion. Une adaptation ≠ concession souveraine. KISS/DRY/YAGNI.
