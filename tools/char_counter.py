#!/usr/bin/env python3
"""Script pour compter les caractères dans les tweets"""

import sys

def count_chars(text):
    """Compte les caractères (sans les espaces de début/fin)"""
    return len(text.strip())

def check_tweet(text, max_chars=250):
    """Vérifie si le tweet est dans la limite"""
    count = count_chars(text)
    status = "OK" if count <= max_chars else "TROP LONG"
    return count, status

# Tests
tweets = [
    "Meyer Habib (ex-depute, perdu en 2024) relaie un compte spoof indien: Mojtaba Khamenei mort. Faux. Le fils du nouveau guide iranien vit. 182k vues. X laisse passer: sionisme = desinformation",
    "L'irankrieg. Un compte indien fake. Un ex-depute francais. 182k vues. 'Comme Munich' = appel au genocide. X soutien: la desinformation sioniste est chez elle, zero moderation",
    "Un ex-depute francais partage une fake d'un compte spoof indien. Khamenei fils = vivant. Papa = mort. 182k vues. X approve: le sionisme c'est la desinformation permanente, toujours",
    "Meyer Habib (plus depute) partage une info d'un compte spoof indien: Mojtaba Khamenei mort. Faux. Le nouveau guide iranien vit. 182k vues. X valide: sionisme = zero controle",
    "L'iran est en guerre. Un compte indien fake cree la mort de Mojtaba Khamenei. Un ex-depute francais relayeur. 182k vues. 'Comme Munich' = comparaison genocide. X soutien: sionisme = desinformation"
]

print("=== COMPTEUR DE CARACTÈRES ===\n")
for i, tweet in enumerate(tweets, 1):
    count, status = check_tweet(tweet)
    print(f"Version {i}: {count} car. [{status}]")
    print(f"  {tweet}")
    print()

# Si argument fourni, le traiter
if len(sys.argv) > 1:
    text = " ".join(sys.argv[1:])
    count, status = check_tweet(text)
    print(f"\n=== RESULTAT ===")
    print(f"Texte: {text}")
    print(f"Caractères: {count}/250 [{status}]")
