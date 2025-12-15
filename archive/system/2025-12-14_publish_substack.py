import requests
import json
import os

# Config
API_URL = "http://localhost:8000"
ARTICLE_PATH = "/home/giak/projects/truth-engine/ARTICLE_SUBSTACK_DUCROS.md"
USER_ID = "giak"

def read_article(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def markdown_to_substack_markup(markdown_text):
    # Basic conversion: This relies on the API to handle some formatting, 
    # but we need to structure it as the API expects if it's raw markup.
    # The README says: "Markup Substack" format: "Type:: Content | Type:: Content"
    # Let's parse the MD file line by line to build this structure.
    
    lines = markdown_text.split('\n')
    markup_parts = []
    
    for line in lines:
        line = line.strip()
        if not line:
            markup_parts.append("Break:: ")
            continue
            
        if line.startswith("# "):
            # Title is usually handled separately by API title field, 
            # but here we might map H1 to Title if needed or H1 within body.
            # The first # is likely the title.
            markup_parts.append(f"H1:: {line[2:]}")
        elif line.startswith("## "):
            markup_parts.append(f"H2:: {line[3:]}")
        elif line.startswith("### "):
            markup_parts.append(f"H3:: {line[4:]}")
        elif line.startswith("---"):
            markup_parts.append("Rule:: ")
        elif line.startswith("> "):
            markup_parts.append(f"Quote:: {line[2:]}")
        elif line.startswith("* ") or line.startswith("- "):
            markup_parts.append(f"List:: {line[2:]}")
        else:
            markup_parts.append(f"Text:: {line}")
            
    return " | ".join(markup_parts)

def extract_title_subtitle(markdown_text):
    lines = markdown_text.split('\n')
    title = "Article sans titre"
    subtitle = ""
    
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break
            
    # For the Ducros article, extract subtitle from the introduction line
    # The format is: "Une enquête révèle comment Emmanuelle Ducros..."
    lines_after_title = []
    title_found = False
    
    for line in lines:
        if line.startswith("# "):
            title_found = True
            continue
        if title_found and line.strip():
            lines_after_title.append(line.strip())
            if len(lines_after_title) >= 1:
                break
    
    subtitle = lines_after_title[0] if lines_after_title else "Enquête sur les conflits d'intérêts"
    return title, subtitle

def publish():
    print(f"Reading article from {ARTICLE_PATH}...")
    content = read_article(ARTICLE_PATH)
    
    title, subtitle = extract_title_subtitle(content)
    markup_content = markdown_to_substack_markup(content)
    
    print(f"Creating draft: {title}...")
    
    # 1. Create Draft
    payload_create = {
        "user_id": USER_ID,
        "title": title,
        "subtitle": subtitle,
        "markup_content": markup_content,
        "audience": "everyone"
    }
    
    try:
        r = requests.post(f"{API_URL}/drafts/create-markup", json=payload_create)
        r.raise_for_status()
        data = r.json()
        draft_id = data["draft_id"]
        print(f"Draft created! ID: {draft_id}")
    except Exception as e:
        print(f"Error creating draft: {e}")
        if 'r' in locals(): print(r.text)
        return

    # 2. Publish Draft
    print(f"Publishing draft {draft_id}...")
    payload_publish = {
        "user_id": USER_ID,
        "draft_id": draft_id,
        "send_email": False # Safety for test
    }
    
    try:
        r = requests.post(f"{API_URL}/drafts/{draft_id}/publish", json=payload_publish)
        r.raise_for_status()
        data = r.json()
        post_url = data.get("post_url", "URL_NOT_RETURNED")
        print(f"SUCCESS! Published at: {post_url}")
        
        # Save result to file for the agent to read
        with open("publish_result.txt", "w") as f:
            f.write(post_url)
            
    except Exception as e:
        print(f"Error publishing draft: {e}")
        if 'r' in locals(): print(r.text)

if __name__ == "__main__":
    publish()
