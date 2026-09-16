import urllib.request
import urllib.parse
import json
import os
import re
import time
import io
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image

HEADERS = {"User-Agent": "TrendTimelineHistoricalArchiveBot/2.0 (contact: admin@the-web-was-here.org)"}

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
        with urllib.request.urlopen(req, timeout=8) as resp:
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
        search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query_text)}&format=json&srlimit=2"
        req = urllib.request.Request(search_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
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
        with urllib.request.urlopen(req, timeout=12) as resp:
            raw_data = resp.read()
            if len(raw_data) < 500:
                return False
                
        img = Image.open(io.BytesIO(raw_data))
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img.thumbnail((640, 480), Image.Resampling.LANCZOS)
            img.save(target_path, "PNG", optimize=True)
        else:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((640, 480), Image.Resampling.LANCZOS)
            img.save(target_path, "JPEG", quality=80, optimize=True)
        return True
    except Exception:
        try:
            with open(target_path, "wb") as f:
                f.write(raw_data)
            return True
        except Exception:
            return False

def process_single_event(year, event, year_dir):
    # If already has valid local image, skip
    if "image" in event and event["image"]:
        local_check = event["image"].lstrip("/")
        if os.path.exists(f"public/{local_check}"):
            return False

    wiki_title = get_wiki_title_from_event(event)
    thumb_url = None
    if wiki_title:
        thumb_url = fetch_page_thumbnail(wiki_title)
        
    if not thumb_url:
        thumb_url = search_wiki_for_image(event["title"])
        
    if not thumb_url and wiki_title:
        thumb_url = search_wiki_for_image(wiki_title.replace("_", " "))
        
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
            print(f"[{year}] Downloaded: {fname} ({event['title'][:40]})", flush=True)
            return True
    return False

def process_year(year):
    events_path = f"src/data/events/{year}.json"
    if not os.path.exists(events_path):
        return 0
        
    with open(events_path, "r") as f:
        events = json.load(f)
        
    year_dir = f"public/images/events/{year}"
    os.makedirs(year_dir, exist_ok=True)
    
    updated = False
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(process_single_event, year, e, year_dir): e for e in events}
        for future in as_completed(futures):
            try:
                res = future.result()
                if res:
                    updated = True
            except Exception as e:
                pass
                
    if updated:
        with open(events_path, "w") as f:
            json.dump(events, f, indent=2)
            f.write("\n")
            
    # Count how many events now have images
    has_img = sum(1 for e in events if "image" in e and os.path.exists(f"public/{e['image'].lstrip('/')}"))
    print(f"=== Year {year} complete: {has_img}/{len(events)} events have local images ===", flush=True)
    return has_img

def main():
    print("Starting high-speed parallel image fetch across 1990-2026...", flush=True)
    total_imgs = 0
    total_events = 0
    
    for y in range(1990, 2027):
        has_img = process_year(y)
        total_imgs += has_img
        
    print(f"\nAll years processed! Total events with local cached images: {total_imgs}", flush=True)

if __name__ == "__main__":
    main()
