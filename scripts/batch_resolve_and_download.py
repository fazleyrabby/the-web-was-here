import urllib.request
import urllib.parse
import json
import os
import re
import time
import io
from PIL import Image

HEADERS = {"User-Agent": "TrendTimelineHistoricalArchiveBot/3.0 (https://the-web-was-here.org; contact: admin@the-web-was-here.org)"}

def clean_filename(s):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', s)

def get_wiki_title_from_event(event):
    for s in event.get("sources", []):
        url = s.get("url", "")
        if "wikipedia.org/wiki/" in url:
            parts = url.split("/wiki/")
            if len(parts) > 1:
                return urllib.parse.unquote(parts[1].split("#")[0])
    # Fallback to title
    return event["title"].replace(" ", "_")

def batch_query_wikipedia_thumbs(titles):
    """Query up to 50 Wikipedia titles in a single HTTP request."""
    result = {}
    if not titles:
        return result
        
    chunk_size = 35
    for i in range(0, len(titles), chunk_size):
        chunk = titles[i:i + chunk_size]
        encoded_titles = "|".join(urllib.parse.quote(t) for t in chunk)
        api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={encoded_titles}&prop=pageimages&format=json&pithumbsize=640"
        
        for attempt in range(3):
            try:
                req = urllib.request.Request(api_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=12) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})
                for p in pages.values():
                    t = p.get('title', '')
                    thumb = p.get('thumbnail', {}).get('source')
                    if thumb:
                        result[t.lower()] = thumb
                        result[t.replace(' ', '_').lower()] = thumb
                break
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print("  [API 429] Backing off 4 seconds...", flush=True)
                    time.sleep(4)
                else:
                    break
            except Exception as e:
                time.sleep(2)
        time.sleep(0.5)
        
    return result

def download_and_optimize(url, target_path):
    for attempt in range(3):
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
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print("  [Download 429] Waiting 3 seconds...", flush=True)
                time.sleep(3)
            else:
                return False
        except Exception:
            try:
                with open(target_path, "wb") as f:
                    f.write(raw_data)
                return True
            except Exception:
                return False
    return False

def search_fallback_thumb(query_text):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query_text)}&format=json&srlimit=2"
    for attempt in range(2):
        try:
            req = urllib.request.Request(search_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode('utf-8'))
            results = data.get('query', {}).get('search', [])
            for r in results:
                t = r['title']
                res = batch_query_wikipedia_thumbs([t])
                if t.lower() in res:
                    return res[t.lower()]
        except Exception:
            time.sleep(1)
    return None

def process_all_years():
    print("Collecting all events across 1990-2026...", flush=True)
    all_events = [] # list of (year, event_dict)
    titles_to_query = set()
    
    for y in range(1990, 2027):
        epath = f"src/data/events/{y}.json"
        if not os.path.exists(epath):
            continue
        with open(epath, "r") as f:
            events = json.load(f)
        for e in events:
            # Check if event already has working local image
            if "image" in e and e["image"]:
                lpath = f"public/{e['image'].lstrip('/')}"
                if os.path.exists(lpath) and os.path.getsize(lpath) > 1000:
                    continue
            t = get_wiki_title_from_event(e)
            if t:
                titles_to_query.add(t)
            all_events.append((y, e))
            
    print(f"Found {len(all_events)} events needing images. Querying {len(titles_to_query)} unique Wikipedia pages in batch...", flush=True)
    
    thumbs_map = batch_query_wikipedia_thumbs(list(titles_to_query))
    print(f"Batch resolution finished! Found {len(thumbs_map)} direct thumbnails.", flush=True)
    
    # Now process year by year
    years_map = {}
    for y, e in all_events:
        years_map.setdefault(y, []).append(e)
        
    downloaded_total = 0
    
    for y in sorted(years_map.keys()):
        ydir = f"public/images/events/{y}"
        os.makedirs(ydir, exist_ok=True)
        epath = f"src/data/events/{y}.json"
        with open(epath, "r") as f:
            events = json.load(f)
            
        updated = False
        year_added = 0
        
        for e in events:
            # Skip if already exists
            if "image" in e and e["image"]:
                lpath = f"public/{e['image'].lstrip('/')}"
                if os.path.exists(lpath) and os.path.getsize(lpath) > 1000:
                    continue
                    
            wt = get_wiki_title_from_event(e)
            thumb = None
            if wt:
                thumb = thumbs_map.get(wt.lower()) or thumbs_map.get(wt.replace('_', ' ').lower())
                
            if not thumb:
                # Fallback search
                thumb = search_fallback_thumb(e["title"])
                time.sleep(0.3)
                
            if thumb:
                clean_url = thumb.split("?")[0]
                ext = os.path.splitext(clean_url)[1].lower()
                if ext not in [".jpg", ".jpeg", ".png", ".webp"]:
                    ext = ".jpg"
                fname = f"{clean_filename(e['id'])}{ext}"
                target_path = os.path.join(ydir, fname)
                pub_path = f"/images/events/{y}/{fname}"
                
                if download_and_optimize(thumb, target_path):
                    e["image"] = pub_path
                    if not e.get("image_caption"):
                        e["image_caption"] = e.get("summary") or e["title"]
                    year_added += 1
                    downloaded_total += 1
                    updated = True
                    print(f"  [{y}] Saved: {fname} for {e['title'][:40]}", flush=True)
                time.sleep(0.2)
                
        if updated:
            with open(epath, "w") as f:
                json.dump(events, f, indent=2)
                f.write("\n")
                
        total_in_year = sum(1 for ev in events if "image" in ev and os.path.exists(f"public/{ev['image'].lstrip('/')}"))
        print(f"Year {y}: {total_in_year}/{len(events)} events now have cached images (+{year_added} new)", flush=True)
        
    print(f"\nCOMPLETED! Downloaded and linked {downloaded_total} new images across the archive.", flush=True)

if __name__ == "__main__":
    process_all_years()
