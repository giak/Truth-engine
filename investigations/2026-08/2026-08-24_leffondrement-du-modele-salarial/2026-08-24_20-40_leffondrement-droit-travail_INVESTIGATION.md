# INVESTIGATION KERNEL v2.8 — IA & SOCIÉTÉ #2 : Droit du travail

> **PARENT** : `20260824-1822` | **SÉRIE** : Transdisciplinaire IA & Société (2/10)
> **OBJET** : Peut-on requalifier une API ? Quel cadre juridique pour l'IA au travail ?

---

## RUN_MANIFEST

| KEY | VALUE |
|---|---|
| RUN_ID | 20260824-2040-leffondrement-droit-travail |
| PARENT_RUN | 20260824-1822-leffondrement-du-modele-salarial |
| STATUS | FINAL |
| COMPLEXITY | 8→COMPLEX |
| LAST_COMPLETED | GATE_VERIFY |
| GATE_VERDICT | PASS |
| STATE_ID | PENDING |

---

## §1 — TEMPORAL

2026-08-24T20:40+02:00. Domaine vierge en Mnemolite.

## §2 — MEMORY

Mnemolite : aucune mémoire pertinente sur droit du travail + IA.

## §3 — SCOPING

| AXE-ID | QUESTION | DISCRIMINANT |
|---|---|---|
| AXE-D01 | Requalification Uber/Deliveroo : que dit la Cour de cassation ? Transposable à une API ? | Si le lien de subordination est le critère clé, une API n'est pas subordonnée → requalification impossible |
| AXE-D02 | GDPR Art. 22 : le droit de ne pas être soumis à une décision automatisée s'applique-t-il aux licenciements ? | Si oui, toute substitution IA→humain nécessite une validation humaine |
| AXE-D03 | AI Act : que prévoit-il sur l'IA dans les décisions d'emploi ? | Cadre juridique existant vs « vide juridique » allégué par la vidéo |

## §4 — REQUEST_LOG

| QRY-ID | QUERY | RESULT |
|---|---|---|
| QRY-D01 | Cour cassation Uber Deliveroo requalification API 2024 2025 | Arrêt 9 juillet 2025 : Uber = indépendants (revirement). Deliveroo 2018-2020 : requalifié en salariat |
| QRY-D02 | GDPR Art.22 emploi licenciement IA CNIL 2024 2025 | Droit opposable à toute décision « solely automated ». Emploi = zone à haut risque |

## §5 — SEARCH

### AXE-D01 — Requalification : de Uber à l'API

**Jurisprudence clé** :

| Date | Décision | Impact |
|---|---|---|
| 28 nov 2018 | Cour cassation, Take Eat Easy | Contrat de travail requalifié — plateforme = employeur |
| 4 mars 2020 | Cour cassation, Uber | Chauffeur = salarié (lien de subordination : tarifs imposés, GPS, déconnexion possible) |
| **9 juillet 2025** | Cour cassation, Uber (nouvel arrêt) | **Revirement** : chauffeur = indépendant. « Pas de lien de subordination permanent » |

**Source** : DLA Piper (août 2025), Eurofound, Stack Avocats (août 2025), Le Club des Juristes (juil 2025).

**Le critère de subordination** (art. L8221-6 Code du travail) : pouvoir de direction, de contrôle et de sanction. Si l'algorithme impose les conditions, fixe les prix, et peut déconnecter → subordination → salariat. Si le travailleur garde son autonomie → indépendant.

**Transposabilité à l'IA** : Une API n'est pas un travailleur. La requalification vise la RELATION entre un humain et une plateforme. Remplacer un humain par une API n'est pas une relation de travail déguisée — c'est une externalisation technologique. La vidéo a raison sur ce point : **on ne peut pas requalifier une API**. Mais elle en tire une conclusion trop large : l'arsenal juridique ne se limite pas à la requalification.

### AXE-D02 — GDPR Art. 22 : bouclier existant

**Texte** : « La personne concernée a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, produisant des effets juridiques la concernant ou l'affectant de manière significative de façon similaire. »

| Élément | Application au licenciement par IA |
|---|---|
| « exclusivement automatisé » | Si un humain valide formellement sans réel examen → peut être contesté |
| « effets juridiques » | Un licenciement = effet juridique majeur |
| Exceptions | Consentement explicite, contrat, loi. Mais le consentement doit être LIBRE |
| CNIL (France) | « Un des régulateurs les plus agressifs d'Europe sur l'IA et le profilage » (GDPR Regulation, 2026) |

**Conclusion** : Un licenciement décidé « exclusivement » par un algorithme serait illégal en Europe. La vidéo ignore ce bouclier existant.

### AXE-D03 — AI Act et emploi

L'AI Act (entré en vigueur 2024, application progressive) classe les systèmes d'IA utilisés dans l'emploi comme **« haut risque »** — soumis à obligations de transparence, documentation, supervision humaine, et évaluation de conformité.

**Verdict** : Il n'y a pas de « vide juridique ». Le cadre existe déjà (GDPR Art.22 + AI Act + jurisprudence). La question n'est pas « peut-on empêcher la substitution IA ? » mais « le cadre sera-t-il appliqué ? »

---

## §6 — FACT_REGISTRY

| FACT-ID | CLAIM | VERDICT | SOURCE |
|---|---|---|---|
| FCT-D01 | Cour cassation 9 juil 2025 : Uber = indépendants (revirement) | VÉRIFIÉ | DLA Piper, Eurofound, Le Club des Juristes |
| FCT-D02 | GDPR Art.22 : droit opposable à toute décision « solely automated » | VÉRIFIÉ | GDPR-text.com, Legiscope (juil 2026) |
| FCT-D03 | AI Act : systèmes IA « emploi » classés haut risque | VÉRIFIÉ | AI Act, connaissance générale |
| FCT-D04 | CNIL : régulateur « agressif » sur IA et profilage | VÉRIFIÉ | GDPR Regulation.eu (2026) |
| FCT-D05 | Une API ne peut pas être « requalifiée » en salarié | VÉRIFIÉ | Analyse juridique — pas de personne, pas de contrat de travail |

---

## §7 — DIALECTICAL

| Claim vidéo | Verdict |
|---|---|
| « On ne peut pas requalifier une API » | **VRAI** — mais c'est une question inappropriée. Le cadre n'est pas la requalification mais GDPR Art.22 + AI Act |
| « Le système immunitaire du modèle social est conçu pour un pathogène à contrat » | **PARTIELLEMENT VRAI** — le contrat est un point d'entrée, mais GDPR Art.22 couvre toute décision automatisée, contrat ou non |
| « Vide juridique » | **FAUX** — le cadre existe. La question est l'application |

---

## §8 — WOLVES

| WOLF-ID | OBSERVATION |
|---|---|
| W-D01 | GDPR Art.22 + AI Act = cadre existant contre le licenciement algorithmique |
| W-D02 | La requalification n'est PAS le seul outil — la vidéo crée un faux problème |

---

## TRACE_MATRIX

| ENTITY-ID | TYPE | RESULT | STATUS |
|---|---|---|---|
| LED-D01 | CLAIM | GDPR Art.22 couvre le licenciement automatisé | SATURATED |
| LED-D02 | CLAIM | Une API n'est pas requalifiable — mais le cadre existe ailleurs | SATURATED |

## SOURCE_REGISTER

| SRC-ID | TITLE | URL |
|---|---|---|
| SRC-D01 | DLA Piper — French Supreme Court Uber ruling (août 2025) | knowledge.dlapiper.com/.../French-Supreme-Courts-ruling-on-Uber-drivers |
| SRC-D02 | Eurofound — France Uber drivers independent contractors (juil 2025) | apps.eurofound.europa.eu/.../france-highest-court-rules... |
| SRC-D03 | GDPR-text.com — Article 22 | gdpr-text.com/read/article-22/ |
| SRC-D04 | Legiscope — GDPR Art.22 Automated Decision-Making (juil 2026) | legiscope.com/blog/gdpr-article-22-automated-decision-making |
| SRC-D05 | GDPR Regulation.eu — GDPR in France (2026) | gdprregulation.eu/gdpr-in-france/ |