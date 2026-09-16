import urllib.request
import json
import os

EXTRA_TARGETS = [
    (1990, "first-web-server-1990", "NeXTcube", "next-cube-cern.png", "Tim Berners-Lee's NeXTcube at CERN, the world's first web server."),
    (1999, "the-matrix-cyberpunk-1999", "The_Matrix_(franchise)", "the-matrix-code.png", "The iconic green falling digital code from The Matrix."),
    (2000, "playstation-2-2000", "PlayStation_2", "playstation-2.png", "Sony PlayStation 2, the best-selling home console of all time."),
    (2001, "apple-ipod-launch-2001", "IPod", "ipod-classic.png", "Original 1st Generation Apple iPod with mechanical scroll wheel."),
    (2005, "xbox-360-hd-gaming-2005", "Xbox_360_technical_specifications", "xbox-360-spec.png", "Microsoft Xbox 360 console with wireless controller."),
    (2008, "first-android-phone-2008", "HTC_Dream", "htc-dream-android.png", "HTC Dream (T-Mobile G1), the first commercial Android smartphone."),
    (2015, "apple-watch-launch-2015", "Apple_Watch", "apple-watch.png", "First generation Apple Watch with Digital Crown."),
    (2024, "apple-vision-pro-2024", "Apple_Vision_Pro", "apple-vision-pro.png", "Apple Vision Pro spatial computing headset.")
]

headers = {"User-Agent": "TrendTimelineHistoricalBot/1.0 (contact: admin@the-web-was-here.org)"}

for year, event_id, page_title, filename, caption in EXTRA_TARGETS:
    local_path = f"public/images/hardware/{filename}"
    public_url = f"/images/hardware/{filename}"
    
    if not os.path.exists(local_path) or os.path.getsize(local_path) < 1000:
        api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={page_title}&prop=pageimages&format=json&pithumbsize=640"
        try:
            req = urllib.request.Request(api_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            thumb_url = None
            for p in pages.values():
                if 'thumbnail' in p:
                    thumb_url = p['thumbnail']['source']
                    break
            if thumb_url:
                req_img = urllib.request.Request(thumb_url, headers=headers)
                with urllib.request.urlopen(req_img, timeout=10) as resp, open(local_path, 'wb') as f:
                    f.write(resp.read())
                print(f"Downloaded {filename} ({os.path.getsize(local_path)} bytes)")
        except Exception as e:
            print(f"Error fetching {page_title}: {e}")
            
    # Link to event
    events_path = f"src/data/events/{year}.json"
    if os.path.exists(events_path):
        with open(events_path, "r") as f:
            events = json.load(f)
        for e in events:
            if (event_id in e["id"]) or (event_id.replace('-', ' ') in e["title"].lower()) or (e["id"] in event_id):
                e["image"] = public_url
                e["image_caption"] = caption
                print(f"Linked image for {e['title']} ({year})")
                break
            # Also check if title contains keywords
            if ("ipod" in event_id and "ipod" in e["title"].lower()) or \
               ("playstation 2" in event_id.replace('-', ' ') and "playstation 2" in e["title"].lower()) or \
               ("vision pro" in event_id.replace('-', ' ') and "vision pro" in e["title"].lower()) or \
               ("android" in event_id and "android" in e["title"].lower() and year == 2008) or \
               ("apple watch" in event_id.replace('-', ' ') and "watch" in e["title"].lower() and year == 2015):
                e["image"] = public_url
                e["image_caption"] = caption
                print(f"Linked image for {e['title']} ({year})")
                break
        with open(events_path, "w") as f:
            json.dump(events, f, indent=2)
            f.write("\n")
