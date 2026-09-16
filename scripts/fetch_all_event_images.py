import urllib.request
import urllib.parse
import json
import os
import re
import time
import io
from PIL import Image

HEADERS = {"User-Agent": "TrendTimelineHistoricalArchiveBot/1.0 (contact: admin@the-web-was-here.org)"}

def clean_filename(s):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', s)

def get_wiki_title_from_event(event):
    for s in event.get("sources", []):
        url = s.get("url", "")
        if "wikipedia.org/wiki/" in url:
            parts = url.split("/wiki/")
            if len(parts) > 1:
                return urllib.parse.unquote(parts[1].split("#")[0])
    return None

def fetch_page_thumbnail(title):
    try:
        api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=640"
        req = urllib.request.Request(api_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        pages = data.get('query', {}).get('pages', {})
        for p in pages.values():
            if 'thumbnail' in p:
                return p['thumbnail']['source']
    except Exception:
        pass
    return None

def search_wiki_for_image(query_text):
    try:
        search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query_text)}&format=json&srlimit=3"
        req = urllib.request.Request(search_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        results = data.get('query', {}).get('search', [])
        for r in results:
            thumb = fetch_page_thumbnail(r['title'])
            if thumb:
                return thumb
    except Exception:
        pass
    return None

def download_and_optimize(url, target_path):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw_data = resp.read()
            if len(raw_data) < 500:
                return False
                
        # Optimize with Pillow
        img = Image.open(io.BytesIO(raw_data))
        # Handle transparency or palette modes
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            # Save as PNG with optimization
            img.thumbnail((640, 480), Image.Resampling.LANCZOS)
            img.save(target_path, "PNG", optimize=True)
        else:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((640, 480), Image.Resampling.LANCZOS)
            img.save(target_path, "JPEG", quality=82, optimize=True)
            
        return True
    except Exception as e:
        # Fallback raw write
        try:
            with open(target_path, "wb") as f:
                f.write(raw_data)
            return True
        except Exception:
            return False

def process_year(year):
    events_path = f"src/data/events/{year}.json"
    if not os.path.exists(events_path):
        return 0, 0
        
    with open(events_path, "r") as f:
        events = json.load(f)
        
    year_dir = f"public/images/events/{year}"
    os.makedirs(year_dir, exist_ok=True)
    
    updated_count = 0
    total_events = len(events)
    
    for event in events:
        # Check if already has valid local image
        if "image" in event and event["image"]:
            local_check = event["image"].lstrip("/")
            if os.path.exists(f"public/{local_check}"):
                continue
                
        wiki_title = get_wiki_title_from_event(event)
        thumb_url = None
        if wiki_title:
            thumb_url = fetch_page_thumbnail(wiki_title)
            
        if not thumb_url:
            thumb_url = search_wiki_for_image(event["title"])
            
        if not thumb_url and wiki_title:
            clean_title = wiki_title.replace("_", " ")
            thumb_url = search_wiki_for_image(clean_title)
            
        if thumb_url:
            clean_url = thumb_url.split("?")[0]
            ext = os.path.splitext(clean_url)[1].lower()
            if ext not in [".jpg", ".jpeg", ".png", ".webp"]:
                ext = ".jpg"
                
            fname = f"{clean_filename(event['id'])}{ext}"
            target_path = os.path.join(year_dir, fname)
            public_path = f"/images/events/{year}/{fname}"
            
            if download_and_optimize(thumb_url, target_path):
                event["image"] = public_path
                if not event.get("image_caption"):
                    event["image_caption"] = event.get("summary") or event["title"]
                updated_count += 1
                print(f"  [{year}] + Image: {event['title']}")
            else:
                print(f"  [{year}] Download failed: {event['title']}")
        else:
            print(f"  [{year}] No image found: {event['title']}")
            
        time.sleep(0.1)
        
    with open(events_path, "w") as f:
        json.dump(events, f, indent=2)
        f.write("\n")
        
    return updated_count, total_events

if __name__ == "__main__":
    import sys
    start_year = int(sys.argv[1]) if len(sys.argv) > 1 else 1990
    end_year = int(sys.argv[2]) if len(sys.argv) > 2 else 2026
    
    total_added = 0
    for y in range(start_year, end_year + 1):
        added, total = process_year(y)
        total_added += added
        print(f"Year {y}: {added} images cached (out of {total} events)")
        
    print(f"\nAll done! Added {total_added} optimized images across {start_year}-{end_year}.")
