# XQ204 : Passe D : audit figures mobile

## Décision

**VALIDÉE.** Les cinq figures existantes ont été recomposées en mobile-first, sans ajouter de nouvelle figure et sans modifier les thèses ou valeurs probatoires portées par les schémas.

## Contrôles

- Cinq figures avant et après : nombre inchangé.
- Noms de fichiers inchangés : les cinq références Markdown de l’article restent valides.
- Largeur SVG : 1 200 px.
- Corps typographique minimal : 34 px, soit environ 11,05 px à une largeur d’affichage de 390 px.
- Ancienne borne XQ203A : environ 3,58 à 3,74 px à 390 px.
- Tiret cadratin dans les SVG : 0.
- QA visuelle manuelle à 390 px : pas de chevauchement résiduel bloquant, hiérarchie lisible, chiffres clés conservés.
- Figure 3 : 12,1 ; R₀ = 5 ; 70/80/90 % ; environ 4× à 60 % ; environ 10× à 80 % conservés.
- Figure 5 : 14 dossiers ; 41 questions ; 39/41 sorties valides conservés.

## Fichiers et empreintes

- `FIG_01_VERIFICATION_ET_LABEL.svg` : 1200 × 1920, min 34 px, ~11.05 px à 390 px, SHA-256 `88399b469d88632bf1cdba1f7287c63fdfe40ca16ae288bf656e5753b8c119c8`.
- `FIG_02_CONTINUUM_EPISTEMIQUE.svg` : 1200 × 1840, min 34 px, ~11.05 px à 390 px, SHA-256 `ed5dc953afb6724396ebdebcb30c13c8e203fb19de81263978376b41d0f9c7ef`.
- `FIG_03_MODELE_AU_SLOGAN_X12.svg` : 1200 × 2100, min 34 px, ~11.05 px à 390 px, SHA-256 `f556406902c5174b18c770cac71396a0ffe91c8c772d6b96a12593cefcfba84d`.
- `FIG_04_CORRECTION_CONTEXTUALISATION_REPARATION.svg` : 1200 × 1920, min 34 px, ~11.05 px à 390 px, SHA-256 `d4ff696ba076f7c195e4bf1fff755d24a7c015f6a4abac7f90d0ab080f30c11d`.
- `FIG_05_FALSIFICATION_REPARATION.svg` : 1200 × 1900, min 34 px, ~11.05 px à 390 px, SHA-256 `d753d03f97d0c1e6f26057ec23a92e4e0322235c5f8d0f54851870e710a0c40b`.

## Preuve visuelle

- `annexes/XQ204_PASS_D_MOBILE_QA_390PX.png`

## Borne

Cette QA valide la lisibilité à une largeur simulée de 390 px. Elle ne constitue pas un test automatisé du moteur de rendu Substack sur tous les appareils. Le BAT final doit donc encore vérifier les chemins d’images et la cohérence de publication.
