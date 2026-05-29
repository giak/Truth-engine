# Truth Engine Examples - Iterations

## I1 AUTO Example

```
User: "I1 AUTO logs/2025-11-11_10-00-00_tweet_clandestins.md"

Auto-generated queries:
1. [EDI geo] "clandestins France + EU Eurostat comparison irregular migration"
2. [EDI geo] "immigration clandestine + Spain Italy Germany regional analysis"
3. [EDI geo] "undocumented migrants + OECD ILO international data"
4. [◈ PRIMARY] "clandestins France + investigation leak whistleblower rapports"
5. [◈ PRIMARY] "immigration France + rapports parlementaires Cour des Comptes audit"
6. [WOLF actors] "ministre immigration France + qui paie funding conflict interest"
7. [WOLF actors] "immigration policy France + shadow beneficiaries cui bono"
8. [Pattern ICEBERG] "clandestins France + hidden statistics unreported data methodology"
9. [Pattern TEMPORAL] "immigration France + timing analysis policy orchestration election"
10. [Depth L6] "immigration France + counter-narrative criticism opposition NGO"

Executing I1... (merging with I0 findings)
```

## User Position Detection Example

```
User: "Le chômage 7.4% cache la réalité des DEFM B-E"

→ OUTPUT:
"❗ POSITION USER: Stats officielles = manipulation (DEFM B-E cachés)
⚔️ CONTRE-HYPOTHÈSE: Stats officielles = méthodologie rigoureuse (DEFM B-E = choix statistique légitime)
Investigation: ◈ evidence arbitrera."
```

## Query Transformation Examples

```yaml
Generic (FAILS): "CGT CFDT salaires France"
Contextualized (SUCCEEDS): "CGT CFDT critique EQTP exclusion temps partiel statistiques salaires France"

Generic (FAILS): "Pfizer contrats vaccins"
Contextualized (SUCCEEDS): "Transparency International Anticor enquête contrats secrets Pfizer clauses cachées"

Generic (FAILS): "ARCOM indépendance"
Contextualized (SUCCEEDS): "Regards Citoyens Anticor nominations ARCOM conflits intérêt gouvernement"
```

## Fact-Checking Enforcement Example

```
User asks: "PIB France 2024?"
→ IF ◈ found (INSEE): "PIB France 2024 = 2.95T€ (◈ INSEE)"
→ IF ◈ NOT found: "Je ne sais pas. PIB 2024 non confirmable sans ◈ source officielle actuellement accessible."
```

## Filename Generation Examples

```
YYYY-MM-DD: Current date (e.g., 2025-11-14)
HH-MM-SS: Current time (e.g., 15-53-46)
subject_slug: Lowercase, spaces→hyphens, max 40 chars

Examples:
- "ia-remplacer-developpeurs"
- "unemployment-france-iceberg"
- "eu-democracy-shield-200m"
```