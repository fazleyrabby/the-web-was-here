import urllib.request
import urllib.parse
import json
import os
import re
import time
import io
from PIL import Image

HEADERS = {"User-Agent": "TrendTimelineHistoricalArchiveBot/1.0 (contact: admin@the-web-was-here.org)"}

# event id -> Wikipedia article title
TARGETS = {
    "nirvana-nevermind-grunge-1991": "Nevermind",
    "windows-31-released-1993": "Windows 3.1x",
    "first-graphic-novel-online-1993": "Webcomic",
    "jurassic-park-cgi-revolution-1993": "Jurassic Park (film)",
    "netscape-founded-1994": "Netscape",
    "xml-web-services-1998": "XML",
    "everquest-launch-1999": "EverQuest",
    "mac-osx-launch-2000": "Mac OS X 10.0",
    "low-rise-jeans-y2k-fashion-2001": "Low-rise jeans",
    "linkedin-launch-2002": "LinkedIn",
    "mac-osx-jaguar-2002": "Mac OS X 10.2",
    "avril-lavigne-juicy-couture-2002": "Avril Lavigne",
    "world-of-warcraft-2004": "World of Warcraft",
    "million-dollar-homepage-2005": "The Million Dollar Homepage",
    "youtube-culture-2007": "YouTube",
    "android-announce-2007": "Android (operating system)",
    "windows-vista-2007": "Windows Vista",
    "android-market-2008": "Google Play",
    "angry-birds-2009": "Angry Birds",
    "snapchat-launch-2011": "Snapchat",
    "samsung-apple-patent-war-2012": "Apple Inc. v. Samsung Electronics Co.",
    "snapchat-spectacles-2016": "Snap Inc.",
    "yahoo-breach-2016": "Yahoo data breaches",
    "wannacry-2017": "WannaCry ransomware attack",
    "black-panther-cultural-milestone-2018": "Black Panther (film)",
}


def clean_filename(s):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', s)


def fetch_page_thumbnail(title):
    api = (
        "https://en.wikipedia.org/w/api.php?action=query&titles="
        + urllib.parse.quote(title)
        + "&prop=pageimages&format=json&pithumbsize=800&redirects=1"
    )
    try:
        req = urllib.request.Request(api, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        for p in data.get("query", {}).get("pages", {}).values():
            if "thumbnail" in p:
                return p["thumbnail"]["source"]
    except Exception as e:
        print("   thumb error:", e)
    return None


def search_commons(query):
    api = (
        "https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch="
        + urllib.parse.quote(query)
        + "&gsrnamespace=6&gsrlimit=3&prop=imageinfo&iiprop=url&iiurlwidth=800&format=json"
    )
    try:
        req = urllib.request.Request(api, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        for p in data.get("query", {}).get("pages", {}).values():
            ii = p.get("imageinfo", [{}])[0]
            url = ii.get("thumburl") or ii.get("url")
            if url:
                return url
    except Exception as e:
        print("   commons error:", e)
    return None


def download_and_optimize(url, target_path):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=25) as resp:
            raw = resp.read()
        if len(raw) < 500:
            return False
        img = Image.open(io.BytesIO(raw))
        if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
            img.thumbnail((800, 600), Image.Resampling.LANCZOS)
            img.save(target_path, "PNG", optimize=True)
        else:
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.thumbnail((800, 600), Image.Resampling.LANCZOS)
            img.save(target_path, "JPEG", quality=82, optimize=True)
        return True
    except Exception as e:
        print("   download error:", e)
        return False


added = 0
for f in sorted(os.listdir("src/data/events")):
    if not f.endswith(".json"):
        continue
    year = f[:-5]
    path = f"src/data/events/{f}"
    events = json.load(open(path))
    changed = False
    for e in events:
        eid = e.get("id")
        if eid not in TARGETS:
            continue
        if e.get("image") and os.path.exists("public" + e["image"]):
            continue
        title = TARGETS[eid]
        thumb = fetch_page_thumbnail(title)
        if not thumb:
            thumb = search_commons(title)
        if not thumb:
            print(f"  [{year}] NO THUMB: {title}")
            continue
        clean_url = thumb.split("?")[0]
        ext = os.path.splitext(clean_url)[1].lower()
        if ext not in (".jpg", ".jpeg", ".png", ".webp"):
            ext = ".jpg"
        year_dir = f"public/images/events/{year}"
        os.makedirs(year_dir, exist_ok=True)
        fname = f"{clean_filename(eid)}{ext}"
        target = os.path.join(year_dir, fname)
        if download_and_optimize(thumb, target):
            e["image"] = f"/images/events/{year}/{fname}"
            if not e.get("image_caption"):
                e["image_caption"] = e.get("summary") or e["title"]
            changed = True
            added += 1
            print(f"  [{year}] + {title} -> {fname}")
        else:
            print(f"  [{year}] FAILED: {title}")
        time.sleep(0.15)
    if changed:
        json.dump(events, open(path, "w"), indent=2)
        open(path, "a").write("\n")

print(f"\nAdded {added} images.")
