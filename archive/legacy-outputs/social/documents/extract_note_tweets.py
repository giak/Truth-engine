#!/usr/bin/env python3
"""
Script pour extraire les note-tweets (tweets longs) de l'utilisateur gigicicicricri
et les sauvegarder en fichiers markdown individuels.
"""

import json
import os
import re
from datetime import datetime

# Chemins
NOTE_TWEETS_FILE = "/home/giak/projects/truth-engine/documents/twitter_save_tweet/note-tweet.js"
OUTPUT_DIR = "/home/giak/projects/truth-engine/documents/mes_note_tweets"

# Votre screen_name
MY_SCREEN_NAME = "gigicicicricri"


def clean_filename(text: str, max_length: int = 50) -> str:
    """Nettoie le texte pour en faire un nom de fichier valide."""
    # Supprime les caractères spéciaux
    text = re.sub(r'[<>:"/\\|?*\n\r\t]', '', text)
    # Remplace les espaces multiples par un seul
    text = re.sub(r'\s+', '_', text)
    # Limite la longueur
    if len(text) > max_length:
        text = text[:max_length]
    # Supprime les underscores en fin
    text = text.rstrip('_')
    return text


def parse_iso_date(date_str: str) -> datetime:
    """Parse une date au format ISO."""
    # Format: "2023-11-21T08:11:13.000Z"
    return datetime.fromisoformat(date_str.replace('Z', '+00:00'))


def extract_hashtags(hashtags_list: list) -> str:
    """Extrait les hashtags en une chaîne formatée."""
    if not hashtags_list:
        return ""
    tags = [f"#{h.get('text', '')}" for h in hashtags_list]
    return " ".join(tags)


def extract_note_tweets():
    """Extrait les note-tweets du fichier et les sauvegarde en markdown."""
    
    # Créer le dossier de sortie
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Lire le fichier note-tweet.js
    print(f"Lecture du fichier: {NOTE_TWEETS_FILE}")
    with open(NOTE_TWEETS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Supprimer le préfixe JavaScript pour obtenir du JSON valide
    # Le fichier commence par "window.YTD.note_tweet.part0 = "
    json_start = content.find('[')
    if json_start == -1:
        print("Erreur: impossible de trouver le début du JSON")
        return
    
    json_content = content[json_start:]
    
    # Parser le JSON
    print("Parsing du JSON...")
    note_tweets_data = json.loads(json_content)
    print(f"Nombre total de note-tweets dans le fichier: {len(note_tweets_data)}")
    
    # Extraire tous les note-tweets
    note_tweets = []
    
    for item in note_tweets_data:
        note_tweet = item.get('noteTweet', {})
        core = note_tweet.get('core', {})
        text = core.get('text', '')
        
        if text:  # Seulement si le texte n'est pas vide
            note_tweets.append({
                'id': note_tweet.get('noteTweetId', ''),
                'text': text,
                'created_at': note_tweet.get('createdAt', ''),
                'updated_at': note_tweet.get('updatedAt', ''),
                'hashtags': core.get('hashtags', []),
                'urls': core.get('urls', []),
                'mentions': core.get('mentions', [])
            })
    
    print(f"Nombre de note-tweets avec contenu: {len(note_tweets)}")
    
    # Trier par date (du plus ancien au plus récent)
    note_tweets.sort(key=lambda t: parse_iso_date(t.get('created_at', '2000-01-01T00:00:00.000Z')))
    
    # Sauvegarder chaque note-tweet en markdown
    for i, note_tweet in enumerate(note_tweets, 1):
        tweet_id = note_tweet.get('id', str(i))
        text = note_tweet.get('text', '')
        created_at = note_tweet.get('created_at', '')
        updated_at = note_tweet.get('updated_at', '')
        hashtags = note_tweet.get('hashtags', [])
        
        # Parser la date
        try:
            tweet_date = parse_iso_date(created_at)
            date_str = tweet_date.strftime("%Y-%m-%d %H:%M:%S")
            date_prefix = tweet_date.strftime("%Y%m%d_%H%M%S")
        except:
            date_str = created_at
            date_prefix = str(i).zfill(5)
        
        # Formater les hashtags
        hashtags_str = extract_hashtags(hashtags)
        
        # Créer le nom de fichier
        text_preview = clean_filename(text[:40])
        filename = f"{date_prefix}_{text_preview}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Créer le contenu markdown
        markdown_content = f"""# Note Tweet

**Date:** {date_str}  
**ID:** {tweet_id}

---

{text}

---
"""
        
        # Ajouter les hashtags s'il y en a
        if hashtags_str:
            markdown_content += f"\n**Hashtags:** {hashtags_str}\n"
        
        markdown_content += f"\n*@{MY_SCREEN_NAME}*\n"
        
        # Sauvegarder le fichier
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        if i % 100 == 0:
            print(f"  ... {i} note-tweets traités")
    
    print(f"\n✅ Extraction terminée!")
    print(f"   {len(note_tweets)} note-tweets sauvegardés dans: {OUTPUT_DIR}")


if __name__ == "__main__":
    extract_note_tweets()
