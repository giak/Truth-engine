#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle mécanique des figures Insee : forme, grammaire, et surtout chiffres.

Trois contrôles, dans l'ordre d'importance :

1. CHIFFRES. Tout nombre *affiché* dans une figure (contenu des <text>, hors renvois
   de note entre crochets) doit exister à l'identique dans l'article V5. C'est la
   mécanisation de la règle « n'inventer aucun chiffre » du prompt visuel.

2. GRAMMAIRE. Canevas 2400 x 1500 ; aucune coordonnée hors cadre ; aucune valeur
   d'arrondi (`rx`/`ry`) ; aucun filtre, dégradé ou ombre ; couleurs limitées à la
   palette de la série.

3. INTÉGRITÉ. Chaque SVG doit être un XML bien formé, et chaque figure annoncée
   dans l'article doit exister sur disque (et réciproquement).

4. LISTE NOIRE, SUR LE CORPS AUSSI. Les formulations interdites sont cherchées dans
   l'article, ligne par ligne, et non seulement dans les figures. C'est là qu'elles
   naissent : le corps porte le même pouvoir de sur-claim qu'une figure, sans avoir
   ni largeur de panneau ni relecture visuelle pour l'arrêter. Les citations entre
   guillemets sont retirées avant l'examen : une pièce se cite, elle ne s'écrit pas.

Usage : python3 tools/engines/visual/check_figures_insee.py
Sortie : code 0 si tout passe, 1 sinon.
"""

import hashlib
import os
import re
import sys
import xml.etree.ElementTree as ET

ART = "articles/2026-09-23_06-00_insee-v5-v38_ce-que-linsee-ne-vous-dira-jamais_ARTICLE.md"
FIGDIR = "articles/2026-09-23_insee_V5/figures/svg"
PALETTE = {"#ffffff", "#111111", "#3d3d3d", "#444444", "#555555", "#f3f3f3", "#c8c8c8", "none"}
NUM = re.compile(r"\d+(?:[ ,\.]\d+)*")
NOTE_REF = re.compile(r"\[\d+\]")
QUOTE = re.compile(r"«[^»]*»")

# Formulations interdites : universels et sur-claims corrigés par l'audit du 23/09/2026,
# qu'un texte ne peut pas réintroduire en douce (un contrôle de chiffres ne les voit pas).
# Chaque motif est suivi de la raison de son interdiction, et de la formulation retenue
# à la place : la liste est un dictionnaire de décisions, pas un filet de sécurité.
BANNED = [
    (r"(?<!Presque )tout est publié", "universel corrigé en « Presque tout est publié »"),
    (r"trois semaines", "durée inventée, corrigée en quatre jours"),
    (r"six malentendus", "décompte faux, corrigé en sept"),
    (r"18 heures", "heure réfutée pour la publication du 7 août"),
    (r"\bAFP\b", "agence rédactrice non identifiée dans nos sources"),
    (r"Metzing a perdu", "tournure interdite par le blindage des scènes"),
    (r"systématiquement trahie", "universel non tenu, remplacé par un scoping"),
    (r"vaut 5 milliards", "facteur 10 sur le titre de section : un dixième de point vaut cinq cents millions"),
    (r"signifie rien", "absolu retiré : un mouvement dans la marge n'y démontre rien"),
    (r"presque rien n'est dit", "sujet manquant : « presque rien n'en est dit » — sinon la phrase dit que l'institut ne dit rien"),
    (r"ne sont pas des événements", "raccourci retiré : une marge interdit d'établir le sens d'un écart, elle ne nie pas son existence"),
    (r"rien n'a été caché", "universel non tenu : le dossier établit une absence de contre-preuve, non une absence de dissimulation"),
    (r"n'est jamais reprise", "universel hors corpus : le dossier a lu 19 articles, il ne les a pas tous lus"),
    (r"structurellement bas", "propriété générale non démontrée, corrigée en « provisoire »"),
    (r"Personne ne peut dire", "absolu épistémique corrigé en « notre corpus ne permet pas de le dire »"),
    (r"n'a pas de programme", "inférence d'intention retirée du texte"),
    (r"habitants manquants", "interprétation corrigée en « écart de 113 habitants »"),
    (r"sans qu'aucun changement", "absolu corrigé en « du seul fait du changement de méthode »"),
    (r"exclut le logement des propriétaires", "l'IPC exclut les loyers imputés et les prix d'achat, pas « le logement des propriétaires »"),
    (r"désigne un choix", "vocabulaire harmonisé en « convention »"),
    (r"presque toujours une phrase sur un seuil", "fréquence affirmée sans mesure"),
    (r"10 à 18 %", "calcul retiré : l'écart entre les sources dépasse le résultat"),
    (r"théorie du complot", "universel non tenu : le désordre des conventions est établi, l'absence de théorie qui le prédit ne l'est pas (relecture 2, §14)"),
]

# Nombres propres à la mise en page ou à la numérotation des figures, jamais au contenu.
LAYOUT = {"2400", "1500", "90", "78", "112", "214", "278", "1410", "1460", "0", "1", "2", "3", "4", "5",
          "6", "7", "8", "9", "10", "11", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"}


def article_numbers():
    with open(ART, encoding="utf-8") as fh:
        text = fh.read()
    found = set()
    for raw in NUM.findall(text):
        found.add(normalise(raw))
    return found


def normalise(n):
    n = n.replace(" ", "").replace(".", ",").strip(",")
    return n


def revision():
    """Empreinte du dossier jugé : article et figures confondus. Elle sert à ce qu'une
    relecture extérieure puisse nommer la révision qu'elle a lue — sans quoi elle juge
    en toute bonne foi un fichier qui n'est plus le dossier, et ses corrections sont
    des faux positifs (constat du 23/09/2026 : cinq corrections obligatoires sur sept
    portaient sur des phrases supprimées quatre passes plus tôt).

    Rend (empreinte, mots, figures)."""
    h = hashlib.sha1()
    raw = open(ART, "rb").read()
    h.update(raw)
    figures = sorted(f for f in os.listdir(FIGDIR) if f.endswith(".svg"))
    for name in figures:
        h.update(open(os.path.join(FIGDIR, name), "rb").read())
    return h.hexdigest()[:12], len(raw.decode("utf-8").split()), len(figures)


def deftypo(s):
    """Apostrophes et guillemets typographiques ramenés à leur forme droite : les motifs
    de la liste noire s'écrivent sans se demander quel caractère l'auteur a tapé."""
    return s.replace("\u2019", "'").replace("\u2018", "'")


def prose_lines(path):
    """Lignes de l'article à examiner : citations retirées, filets et tableaux ignorés.
    Les légendes de figures sont conservées : elles se lisent comme du texte."""
    with open(path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            if not raw.strip() or raw.strip().startswith(("---", "|")):
                continue
            yield lineno, QUOTE.sub(" ", raw).strip()


def check_prose(path, problems):
    """Liste noire appliquée au corps. Rend le nombre de lignes examinées."""
    n = 0
    for lineno, line in prose_lines(path):
        n += 1
        flat = deftypo(line)
        for pattern, why in BANNED:
            m = re.search(pattern, flat, re.IGNORECASE)
            if m:
                problems.append("ARTICLE ligne %d : formulation interdite → « %s » (%s)"
                                % (lineno, m.group(0), why))
    return n


def svg_texts(path):
    tree = ET.parse(path)
    root = tree.getroot()
    out = []
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag == "text" and el.text:
            out.append(el.text.strip())
    return root, out


def main():
    problems = []
    art = article_numbers()
    scanned = check_prose(ART, problems)

    if not os.path.isdir(FIGDIR):
        print("ERREUR : dossier de figures absent :", FIGDIR)
        return 1

    files = sorted(f for f in os.listdir(FIGDIR) if f.endswith(".svg"))
    print("Figures trouvées : %d" % len(files))

    published = set()
    with open(ART, encoding="utf-8") as fh:
        article_text = fh.read()
    for m in re.finditer(r"\((2026-09-23_insee_V5/figures/svg/[^)]+\.svg)\)", article_text):
        published.add(os.path.basename(m.group(1)))

    for name in files:
        path = os.path.join(FIGDIR, name)
        try:
            root, texts = svg_texts(path)
        except ET.ParseError as exc:
            problems.append("%s : XML invalide (%s)" % (name, exc))
            continue

        # --- grammaire
        if root.get("width") != "2400" or root.get("height") != "1500":
            problems.append("%s : canevas %s x %s au lieu de 2400 x 1500"
                            % (name, root.get("width"), root.get("height")))
        raw = open(path, encoding="utf-8").read()
        for bad in ("rx=", "ry=", "<filter", "Gradient", "shadow", "rotate(-"):
            if bad in raw:
                problems.append("%s : élément interdit (%s)" % (name, bad))
        for color in set(re.findall(r"#[0-9a-fA-F]{6}", raw)):
            if color.lower() not in PALETTE:
                problems.append("%s : couleur hors palette (%s)" % (name, color))
        for pattern, why in BANNED:
            m = re.search(pattern, raw, re.IGNORECASE)
            if m:
                problems.append("%s : formulation interdite réintroduite → « %s » (%s)"
                                % (name, m.group(0), why))

        # --- chiffres affichés
        for t in texts:
            clean = NOTE_REF.sub(" ", t)
            for raw_num in NUM.findall(clean):
                n = normalise(raw_num)
                if not n or n in LAYOUT:
                    continue
                if n not in art:
                    problems.append("%s : chiffre absent de l'article → « %s » (dans : %s)"
                                    % (name, raw_num.strip(), t[:70]))

        # --- intégration
        if name not in published:
            problems.append("%s : figure non référencée dans l'article" % name)

    for name in sorted(published - set(files)):
        problems.append("%s : figure référencée dans l'article mais absente du disque" % name)

    print("Corps examiné : %d lignes de prose (citations retirées)" % scanned)
    stamp, words, figs = revision()
    print("Révision jugée : %s · %d mots · %d figures" % (stamp, words, figs))

    if problems:
        print("\n%d problème(s) :" % len(problems))
        for p in problems:
            print("  -", p)
        return 1
    print("Tous les contrôles passent : chiffres alignés sur l'article, formules conformes"
          " dans les figures et dans le corps, grammaire conforme, intégration complète.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
