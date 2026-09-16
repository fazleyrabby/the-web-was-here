import urllib.request
import json
import os
import time

TARGETS = [
    # (year, event_id, wikipedia_page_title, local_filename, caption)
    (1990, "game-boy-mania-1990", "Game_Boy", "game-boy-dmg01.png", "The original 8-bit Nintendo Game Boy (DMG-01) with monochrome green LCD screen."),
    (1990, "first-web-server-1990", "NeXT_Computer", "next-cube-cern.jpg", "Tim Berners-Lee's NeXT Computer at CERN, the world's first web server."),
    (1991, "super-nintendo-snes-launch-1991", "Super_Nintendo_Entertainment_System", "snes-console.png", "Super Nintendo Entertainment System (SNES) with two-tone purple sliding power switch."),
    (1993, "doom-shareware-multiplayer-1993", "Doom_(1993_video_game)", "doom-1993.jpg", "id Software's DOOM, the revolutionary 3D multiplayer PC shareware title."),
    (1994, "playstation-japan-launch-1994", "PlayStation_(console)", "playstation-1.png", "Sony PlayStation (SCPH-1000) 32-bit CD-ROM console."),
    (1996, "nintendo-64-mario-64-1996", "Nintendo_64", "nintendo-64.png", "Nintendo 64 with analog thumbstick controller."),
    (1996, "dolly-the-sheep-cloned-1996", "Dolly_(sheep)", "dolly-the-sheep.jpg", "Dolly the sheep, the world's first cloned mammal, at the Roslin Institute."),
    (1997, "tamagotchi-craze-1997", "Tamagotchi", "tamagotchi.png", "Original Bandai Tamagotchi virtual pet digital egg keychain."),
    (1998, "apple-imac-g3-bondi-blue-1998", "IMac_G3", "imac-g3-bondi.png", "Apple iMac G3 in translucent Bondi Blue, designed by Jony Ive."),
    (1999, "the-matrix-cyberpunk-1999", "The_Matrix", "the-matrix.jpg", "The Matrix, directed by the Wachowskis."),
    (2000, "nokia-3310-snake-2000", "Nokia_3310", "nokia-3310.png", "Nokia 3310 mobile phone, renowned for indestructible durability and Snake II."),
    (2000, "playstation-2-2000", "PlayStation_2", "playstation-2.png", "Sony PlayStation 2, the best-selling video game console in history."),
    (2001, "apple-ipod-launch-2001", "IPod_(original)", "ipod-1st-gen.png", "Original 1st Generation Apple iPod with mechanical scroll wheel (5GB)."),
    (2001, "halo-combat-evolved-xbox-2001", "Xbox_(console)", "original-xbox.png", "Microsoft Xbox console with Duke controller."),
    (2004, "motorola-razr-v3-2004", "Motorola_Razr_V3", "motorola-razr-v3.png", "Motorola RAZR V3 ultra-slim aircraft-grade aluminum flip phone."),
    (2004, "nintendo-ds-touchscreen-2004", "Nintendo_DS", "nintendo-ds.png", "Original clamshell Nintendo DS with dual screens and touch stylus."),
    (2005, "xbox-360-hd-gaming-2005", "Xbox_360", "xbox-360.png", "Microsoft Xbox 360 HD video game console."),
    (2006, "nintendo-wii-motion-craze-2006", "Wii", "nintendo-wii.png", "Nintendo Wii console with motion-sensing Wiimote."),
    (2007, "iphone-2007", "IPhone_(1st_generation)", "original-iphone.png", "The original 2007 Apple iPhone with 3.5-inch multi-touch display."),
    (2007, "amazon-kindle-ereader-2007", "Amazon_Kindle", "amazon-kindle-1.png", "First generation Amazon Kindle with asymmetric keyboard and E-Ink screen."),
    (2008, "first-android-phone-2008", "HTC_Dream", "htc-dream-android.png", "HTC Dream (T-Mobile G1), the first commercially released Android smartphone."),
    (2010, "ipad-original-launch-2010", "IPad_(1st_generation)", "ipad-1st-gen.png", "Original 9.7-inch Apple iPad unveiled by Steve Jobs."),
    (2012, "higgs-boson-curiosity-mars-2012", "Curiosity_(rover)", "curiosity-rover.jpg", "NASA's Curiosity rover on the surface of Mars."),
    (2015, "apple-watch-launch-2015", "Apple_Watch", "apple-watch.png", "First generation Apple Watch smartwatch with Digital Crown."),
    (2016, "apple-airpods-cord-cutting-2016", "AirPods", "apple-airpods.png", "Original Apple AirPods true wireless earbuds in charging case."),
    (2017, "nintendo-switch-zelda-botw-2017", "Nintendo_Switch", "nintendo-switch.png", "Nintendo Switch hybrid console with neon blue and red Joy-Cons."),
    (2017, "fidget-spinner-craze-2017", "Fidget_spinner", "fidget-spinner.png", "Three-pronged ball-bearing plastic fidget spinner."),
    (2019, "first-black-hole-photograph-2019", "Messier_87", "m87-black-hole.jpg", "First direct image of the supermassive black hole at the core of galaxy M87."),
    (2022, "james-webb-telescope-deep-field-2022", "Webb%27s_First_Deep_Field", "jwst-deep-field.jpg", "NASA James Webb Space Telescope's First Deep Field (SMACS 0723)."),
    (2024, "apple-vision-pro-ships-2024", "Apple_Vision_Pro", "apple-vision-pro.png", "Apple Vision Pro spatial computing headset.")
]

os.makedirs("public/images/hardware", exist_ok=True)

def fetch_and_link():
    headers = {"User-Agent": "TrendTimelineHistoricalBot/1.0 (contact: admin@the-web-was-here.org)"}
    
    for year, event_id, page_title, filename, caption in TARGETS:
        local_path = f"public/images/hardware/{filename}"
        public_url = f"/images/hardware/{filename}"
        
        # Download if not already saved
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
                else:
                    print(f"No thumbnail found for {page_title}")
                    continue
            except Exception as e:
                print(f"Error fetching {page_title}: {e}")
                continue
            time.sleep(0.5)
            
        # Update events file
        events_path = f"src/data/events/{year}.json"
        if os.path.exists(events_path):
            with open(events_path, "r") as f:
                events = json.load(f)
            updated = False
            for e in events:
                if e["id"] == event_id or (event_id in e.get("title", "").lower()) or (event_id in e["id"]):
                    e["image"] = public_url
                    e["image_caption"] = caption
                    updated = True
                    print(f"Linked image for {e['title']} in {year}")
                    break
            if updated:
                with open(events_path, "w") as f:
                    json.dump(events, f, indent=2)
                    f.write("\n")

if __name__ == "__main__":
    fetch_and_link()
