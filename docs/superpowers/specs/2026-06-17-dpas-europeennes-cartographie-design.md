# Design — Cartographie exhaustive des 27 DPAs européennes et leurs modèles de financement

## Objectif

Cartographier les 27 autorités de protection des données (DPAs) de l'UE sur 11 dimensions pour révéler les patterns de financement, d'indépendance réelle et d'efficacité. Cette cartographie alimente directement la thèse de « l'architecture d'illusion » : les recours existent en droit mais sont structurellement sous-ressourcés ou neutralisés par le circuit de financement.

## Architecture du livrable

Deux fichiers :

1. **INVESTIGATION** (`investigations/YYYY-MM-DD_HH-MM_dpas-europeennes_modeles_financement_INVESTIGATION.md`)
   - Récit complet avec clusters, outliers, faisceaux
2. **HYPER_MATRICE** (`investigations/YYYY-MM-DD_HH-MM_dpas-europeennes_modeles_financement_HYPER_MATRICE.md`)
   - Données brutes exploitables, format standardisé

## Structure du document principal

| Section | Contenu |
|---------|---------|
| §0 Synopsis | Trouvaille centrale, nombre de DPAs avec fléchage, tendance macro |
| §1 Matrice comparative | Tableau 27 lignes × 11 colonnes, pays par ordre alphabétique |
| §2 Clusters | 3-5 clusters thématiques |
| §3 Outliers & corrélations | DPAs qui cassent les tendances |
| §4 Faisceau systèmes | Convergence/contradiction avec 4 investigations existantes |
| §5 Loups | Patterns cachés, biais, angles morts |

## 11 dimensions de la matrice

1. Budget total (€, dernier exercice disponible)
2. Budget per capita (€/citoyen)
3. Effectifs (ETP)
4. Staff par million d'habitants
5. Source financement (budget général / fléché amendes / mixte / redevances)
6. Amendes RGPD émises (€ cumulé 2018-2025)
7. Taux de recouvrement estimé (%)
8. Plaintes reçues/an (2023-2024)
9. Taux de résolution (%)
10. Indépendance (constitutionnelle / loi organique / simple loi / administrative)
11. Pouvoir de sanction (avec/sans injonction ministère tutelle)

## Sources

- Rapports annuels 27 DPAs (sites officiels + EDPB)
- EDPB Contribution 2024
- Chiffres CNIL, ICO (UK), DPC (IE), BfDI (DE), AEPD (ES), Garante (IT), APD/GBA (BE)
- Articles académiques (indépendance DPAs, compliance gap)
- Cour des Comptes française (rapport CNIL/ANSSI)
- Rapports BEUC, Access Now

## Méthode de collecte

1. Priorité aux chiffres officiels 2023-2024 (rapports annuels)
2. Données manquantes → marquées « NC » (non communiqué)
3. Taux de recouvrement : croisement amendes prononcées vs encaissées (quand disponible)
4. Sources systématiquement citées en inline (URL/lien)

## Clusters attendus (hypothèses de travail)

- **Cluster A — Fléchage amendes** : Espagne (AEPD), Autriche (DSB), Hongrie (NAIH), etc.
- **Cluster B — Budget général pur** : France (CNIL), Allemagne (BfDI), Pays-Bas (AP)
- **Cluster C — Mixte** : Belgique (APD/GBA), Portugal (CNPD)
- **Cluster D — Sous-financés critiques** : DPAs Est-Européennes (budget < 1M€, staff < 20)
- **Cluster E — Indépendance constitutionnelle** : Allemagne, Autriche, etc.

## Critères de succès

- Au moins 24/27 DPAs avec données dans ≥ 9/11 dimensions
- Au moins 1 outlier documenté avec preuve contradictoire
- Au moins 2 corrélations significatives entre financement et efficacité
- Lien explicite vers ≥ 2 des 4 investigations MnemoLite existantes
