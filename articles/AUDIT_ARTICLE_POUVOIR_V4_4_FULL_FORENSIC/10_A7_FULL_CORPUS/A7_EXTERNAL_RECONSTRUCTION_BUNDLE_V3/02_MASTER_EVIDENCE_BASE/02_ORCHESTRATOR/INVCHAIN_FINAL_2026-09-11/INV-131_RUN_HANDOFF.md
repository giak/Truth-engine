---
trace_schema: "forensic-md/v1"
project: "democracy-influence-investigations"
artifact_type: "run_handoff"
status: "terminal"
inv_id: "INV-131"
truth_engine: "DELIVERY_PASS_R3P1"
renard: "NO"
reclass_impact: "INV-038;INV-147"
updated: "2026-09-10"
---

# RUN_HANDOFF — INV-131

## Certification

- Truth Engine: `DELIVERY_PASS_R3P1`
- Run: `20260910-1932-algerie-influence-france`
- Deliverable: `INV-131_INVESTIGATION.md`
- Deliverable SHA-256: `a98c4850dcdd8fa4680e480de6c11f2eb958a182d6c74cf1ad951bbb5a0dd797`
- Corpus runtime: `QRY=22 / SRC=13 / FCT=19 / provenance_families=5`
- Persistence: `PASS / eligible=17 / blocked=17 / success=0 / failure=0 / fabricated_memory_ids=0 / reason=MNEMO_UNAVAILABLE`

## Delta central

Le corpus ferme plusieurs mécanismes algériens en France sans les fusionner en une architecture unique. L'État algérien exerce une influence institutionnelle explicite sur une partie de l'organisation du culte musulman via subventions, imams détachés et relations avec la Grande Mosquée de Paris. Les instruments consulaires et diplomatiques constituent des leviers réciproques observables, mais l'épisode français de restriction générale des visas fournit un contrôle négatif important : existence d'un levier ne signifie pas efficacité coercitive. L'affaire Amir Boukhors documente une opération clandestine violente et des liens officiels algériens faisant l'objet de procédures judiciaires, sans fermer encore la chaîne de tasking/commandement étatique. Aucune chaîne publique ne démontre un pilotage politique général de la diaspora algérienne ni un effet électoral français.

## Highest supported influence/effect edge

- `État/ambassade algériens -> financement/personnel/accords -> Grande Mosquée de Paris et structures cultuelles -> capacité institutionnelle en France` = **SUPPORTED** ; `-> relais politique/électoral de diaspora` = **NOT ESTABLISHED**.
- `décisions consulaires/diplomatiques -> capacité administrative française -> visas/éloignements/cooperation` = **SUPPORTED** ; coercition unilatérale efficace = **NOT ESTABLISHED**, avec contrôle négatif documenté.
- `personnes liées à des structures algériennes -> repérage/intermédiaires -> enlèvement/intimidation d'un opposant en France` = **PARTIAL / strongly documented operation** ; `-> tasking de l'État algérien` et chaîne de commandement = **UNRESOLVED**.
- `services/consulats -> élus locaux d'origine algérienne -> tasking -> décision politique` = **ACCESS GAP**, la note primaire publiquement invoquée n'étant pas accessible dans le corpus inspecté.

## Material gaps / contradictions

- **RESPONSIBILITY/TASKING** — jugement définitif et preuve publique du commandement étatique requis pour l'affaire Amir Boukhors et le volet Bercy/OFII.
- **ACCESS** — note primaire sur d'éventuelles approches d'élus locaux non publique ; aucun saut de la déclaration parlementaire à un fait certifié.
- **EFFECT** — aucun effet électoral français ou changement de politique publique terminal attribuable à l'influence cultuelle ou diasporique.
- **COERCION** — des leviers bilatéraux existent, mais leur efficacité varie et peut produire des effets contraires au but recherché.

## Contradictory review / causal ceiling

Le financement transparent du culte ne démontre pas un tasking politique ; imams détachés et formation ne démontrent pas un relais électoral ; une mise en examen ou un mandat d'arrêt ne vaut ni condamnation définitive ni ordre étatique prouvé ; des représailles diplomatiques ne prouvent pas la culpabilité dans un dossier pénal. Le cas algérien n'est donc pas isomorphe au cas marocain en bloc : la comparaison valide est mécanisme par mécanisme et niveau de preuve par niveau de preuve.

## RENARD

`NO` — les upgrades matériels restants exigent des décisions judiciaires définitives, la publication/déclassification de pièces primaires de tasking, ou des designs causaux sur l'effet. Une collecte générique supplémentaire sur « l'influence algérienne » serait cumulative et risquerait de transformer des institutions, une diaspora ou une nationalité en proxy de commandement.

## New ideas triaged

- `INV-038` peut devenir dependency-complete après fermeture mécanique d'`INV-131`; sa synthèse doit comparer Maroc/Algérie mécanisme par mécanisme, sans Truth Engine générique.
- `INV-147` reçoit un nouveau comparateur matériel : mêmes catégories d'influence, mais niveaux de clandestinité, preuve et conséquences institutionnelles hétérogènes. Cela ne ferme pas encore son dataset apparié de labels/enforcement.
- Aucun nouveau bundle actor-first n'est créé.

## Mechanical transition expected

`INV-131 TE_ACTIVE -> CLOSED`; `truth_engine=DELIVERY_PASS_R3P1`; `renard=NO`; `result_path=INV-131_RUN_HANDOFF.md`; semantic reclassification impact bounded to `INV-038;INV-147`.
