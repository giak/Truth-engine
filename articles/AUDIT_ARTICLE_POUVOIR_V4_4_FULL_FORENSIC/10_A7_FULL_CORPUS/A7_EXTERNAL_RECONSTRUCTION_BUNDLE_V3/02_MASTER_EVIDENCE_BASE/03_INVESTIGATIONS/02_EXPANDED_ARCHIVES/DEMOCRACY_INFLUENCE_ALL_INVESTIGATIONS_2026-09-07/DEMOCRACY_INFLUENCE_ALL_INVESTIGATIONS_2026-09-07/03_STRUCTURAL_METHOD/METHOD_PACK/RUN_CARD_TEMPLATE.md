# RUN_CARD — template

> Fill from `INVESTIGATION_REGISTRY.csv`. This card is project input; Truth Engine remains authoritative for runtime semantics.

```text
INV_ID := {{INV_ID}}
SUBJECT := {{TITLE}}
ITEM_TYPE := {{ITEM_TYPE}}
EXECUTION_MODE := {{EXECUTION_MODE}}
COVERAGE_CURRENT := {{COVERAGE_CURRENT}}
CORPUS_REFS := {{CORPUS_REFS}}
PARENT_ID := {{PARENT_ID}}
DEPENDENCIES := {{DEPENDENCIES}}
AS_OF := {{AS_OF}}
SCOPE_NOTE := {{SCOPE_NOTE}}
```

## Execution instruction

Use the current canonical Truth Engine `KERNEL.md` v2.10.6.
Apply `METHOD_PACK/METHOD_PACK.md` as a project-level non-regression overlay.

Conduct the investigation at maximum useful forensic depth on `SUBJECT`.
Do not write the final article.
Do not defend a predetermined global thesis.
Treat `CORPUS_REFS` as leads/context only; re-open material evidence as required by Truth Engine and METHOD_PACK.
Distinguish relation / coordination / intent / causality / impact.
Seek the strongest credible rival explanations and counter-evidence.
If the object is systemic, inspect bridges, implementation, observed use and effects, not only components.

Do not run RENARD inside the Truth Engine canonical run.
After Truth Engine FINAL, create a separate project handoff using `RUN_HANDOFF_TEMPLATE.md`, then decide the RENARD gate.
