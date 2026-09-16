import json
import os

ERA1_UPDATES = {
    1990: {
        "felt_like": {
            "os": "MS-DOS 4.0 / Windows 3.0",
            "browser": "N/A (Pre-web era)",
            "messenger": "IRC / BBS dial-up message boards",
            "social_network": "Usenet newsgroups",
            "music": "Cassette tapes, Sony Walkman, and vinyl 45s",
            "phone": "Rotary landlines & brick-sized Motorola DynaTACs",
            "video": "VHS tapes rented from Blockbuster",
            "website": "info.cern.ch (served on a NeXT Cube)",
            "fashion": "Neon windbreakers, parachute pants, scrunchies & acid-wash denim",
            "gadget": "Nintendo Game Boy (bundled with Tetris)",
            "news": "Nelson Mandela freed; Germany formally reunifies",
            "culture": "The Simpsons season one & Twin Peaks hysteria"
        },
        "new_events": [
            {
                "id": "game-boy-mania-1990",
                "title": "Nintendo Game Boy & Tetris Craze",
                "year": 1990,
                "date": "1990-09-28",
                "category": ["gadget", "gaming"],
                "type": "launch",
                "summary": "The Nintendo Game Boy exploded globally in 1990 bundled with Tetris, making portable gaming a cultural obsession.",
                "narrative": "Commuters on trains and kids in schoolyards were suddenly united by the hypnotic Russian folk melody of Tetris. Gunpei Yokoi's rugged gray brick with its four-shade pea-soup screen ran for 30 hours on four AA batteries, outlasting color rivals and selling tens of millions of units. It proved that gaming didn't belong solely to living rooms and arcades—it belonged in everyone's pocket.",
                "why_it_matters": "The Game Boy established portable electronic entertainment as a permanent facet of daily life, paving the psychological runway for mobile phones decades later.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Game Boy - Wikipedia", "url": "https://en.wikipedia.org/wiki/Game_Boy" }
                ]
            },
            {
                "id": "reunification-mandela-1990",
                "title": "Nelson Mandela Freed & German Reunification",
                "year": 1990,
                "date": "1990-10-03",
                "category": ["news", "history"],
                "type": "milestone",
                "summary": "Nelson Mandela walked free after 27 years and Germany officially reunited, reshaping global geopolitics.",
                "narrative": "1990 dismantled twentieth-century divisions in real time on international television. In February, Nelson Mandela walked out of Victor Verster Prison hand-in-hand with Winnie Mandela, heralding the end of apartheid in South Africa. By October, East and West Germany were formally reunited after the fall of the Berlin Wall. The optimism of an open, interconnected world fueled the early philosophy of the budding internet.",
                "why_it_matters": "These historic breakthroughs closed chapters of the Cold War and racial subjugation, setting an optimistic, borderless tone for the dawn of the internet era.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "German Reunification - Wikipedia", "url": "https://en.wikipedia.org/wiki/German_reunification" },
                    { "title": "Nelson Mandela - Wikipedia", "url": "https://en.wikipedia.org/wiki/Nelson_Mandela" }
                ]
            },
            {
                "id": "madonna-vogue-mchammer-1990",
                "title": "Madonna's 'Vogue' & MC Hammer's Dance-Pop Reign",
                "year": 1990,
                "date": "1990-03-27",
                "category": ["music", "fashion"],
                "type": "cultural_shift",
                "summary": "Madonna brought underground ballroom vogueing to the top of Billboard while MC Hammer made baggy pants and hip-hop dance universal.",
                "narrative": "MTV was the planet's cultural bulletin board. Madonna's black-and-white David Fincher-directed video for 'Vogue' celebrated Harlem's underground LGBTQ+ ballroom scene and became the best-selling single of the year. Meanwhile, MC Hammer's 'U Can't Touch This' soundtracked every school dance, making golden parachute pants and lightning-fast footwork an inescapable global trend.",
                "why_it_matters": "It demonstrated MTV's power to export niche subcultures, fashion silhouettes, and street dance straight into mainstream suburban households worldwide.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Vogue (Madonna song) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Vogue_(Madonna_song)" }
                ]
            }
        ]
    },
    1991: {
        "felt_like": {
            "os": "MS-DOS 5.0 / Mac System 7",
            "browser": "CERN Line Mode Browser / WorldWideWeb",
            "messenger": "IRC / MUDs / Talk command",
            "social_network": "Usenet newsgroups & Fidonet",
            "music": "Cassette mixtapes, grunge CD albums, boomboxes",
            "phone": "Clear plastic landlines with neon lights & car phones",
            "video": "VHS rentals & MTV music video blocks",
            "website": "First public HTML files hosted on NeXT",
            "fashion": "Thrift store flannels, ripped denim, Doc Martens, Hypercolor shirts",
            "gadget": "Super Nintendo Entertainment System (SNES)",
            "news": "Dissolution of the Soviet Union; Operation Desert Storm",
            "culture": "Nirvana's Nevermind, Terminator 2, Silence of the Lambs"
        },
        "new_events": [
            {
                "id": "nirvana-nevermind-grunge-1991",
                "title": "Nirvana Drops 'Nevermind' & Grunge Explodes",
                "year": 1991,
                "date": "1991-09-24",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Nirvana's 'Nevermind' and 'Smells Like Teen Spirit' wiped out 80s hair metal and made alternative rock the defining sound of Gen X.",
                "narrative": "When Kurt Cobain struck the opening distorted chords of 'Smells Like Teen Spirit', the 1980s officially died. Recorded in Sound City, 'Nevermind' knocked Michael Jackson's 'Dangerous' from the number one spot on the Billboard chart by early 1992. Overnight, flannel shirts, thrifted cardigans, and raw emotional disillusionment replaced spandex and hairspray.",
                "why_it_matters": "It marked a colossal paradigm shift in youth culture, ushering in the 1990s aesthetic of authentic cynicism and alternative independence.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Nevermind - Wikipedia", "url": "https://en.wikipedia.org/wiki/Nevermind" }
                ]
            },
            {
                "id": "super-nintendo-snes-launch-1991",
                "title": "Super Nintendo (SNES) Ignites the 16-Bit Wars",
                "year": 1991,
                "date": "1991-08-23",
                "category": ["gadget", "gaming"],
                "type": "launch",
                "summary": "Nintendo launched the Super Nintendo Entertainment System in North America alongside Super Mario World.",
                "narrative": "With rich 256-color palettes, Mode 7 pseudo-3D scaling, and custom Sony audio chips, the SNES turned neighborhood rivalries with Sega Genesis into playground battlegrounds. 'Super Mario World' introduced Yoshi and expansive secret exits, establishing an unmatched standard for 16-bit perfection that defined childhood for millions.",
                "why_it_matters": "The SNES vs. Sega Genesis showdown represented the golden age of competitive console marketing and elevated video game design to high art.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Super Nintendo Entertainment System - Wikipedia", "url": "https://en.wikipedia.org/wiki/Super_Nintendo_Entertainment_System" }
                ]
            },
            {
                "id": "ussr-dissolution-desert-storm-1991",
                "title": "End of the USSR & Desert Storm on 24-Hour Cable News",
                "year": 1991,
                "date": "1991-12-25",
                "category": ["news", "history"],
                "type": "milestone",
                "summary": "The Soviet Union officially dissolved on Christmas Day, while Desert Storm established CNN's 24-hour real-time war coverage.",
                "narrative": "Mikhail Gorbachev resigned on Christmas night 1991, and the red hammer-and-sickle banner over the Kremlin was lowered for the last time, formally concluding the nearly half-century Cold War. Earlier that year, CNN reporters broadcast live anti-aircraft fire over Baghdad through hotel window microphones, fundamentally altering how humanity experienced breaking international crises.",
                "why_it_matters": "The end of the bipolar world order opened Eastern Europe to western computing technologies, while 24-hour news foreshadowed the internet's insatiable demand for real-time updates.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Dissolution of the Soviet Union - Wikipedia", "url": "https://en.wikipedia.org/wiki/Dissolution_of_the_Soviet_Union" }
                ]
            }
        ]
    },
    1992: {
        "felt_like": {
            "os": "Windows 3.1 / Mac System 7.1",
            "browser": "Erwise / ViolaWWW / Lynx",
            "messenger": "IRC / Bitnet RELAY / Usenet",
            "social_network": "The WELL / CompuServe forums",
            "music": "Dr. Dre's G-Funk, cassette singles, Boyz II Men",
            "phone": "Motorola MicroTAC flip phone & beepers",
            "video": "VHS home camcorders & LaserDiscs",
            "website": "Pure text and raw hyperlink documents",
            "fashion": "Flannel tied at the waist, babydoll dresses with combat boots, backward ballcaps",
            "gadget": "Sony MiniDisc player & IBM Simon smartphone prototype",
            "news": "1992 Los Angeles Riots; Bill Clinton elected US President",
            "culture": "Wayne's World, Aladdin, MTV's The Real World debuts"
        },
        "new_events": [
            {
                "id": "first-sms-text-message-1992",
                "title": "First SMS Text Message Sent: 'Merry Christmas'",
                "year": 1992,
                "date": "1992-12-03",
                "category": ["gadget", "communication"],
                "type": "milestone",
                "summary": "22-year-old engineer Neil Papworth sent the world's first text message over the Vodafone GSM network.",
                "narrative": "Sitting at a desktop computer terminal in Berkshire, England, software developer Neil Papworth typed the 15-character message 'Merry Christmas' and sent it across Vodafone's cellular network to Richard Jarvis's 4.6-pound Orbitel 901 handset. The handset couldn't even reply—it was built solely to receive. Neither man imagined that 160-character bursts would soon rival phone calls and shape global social communication.",
                "why_it_matters": "SMS invented mobile messaging, giving birth to texting culture, acronyms like LOL and BRB, and eventually modern chat ecosystems.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "SMS - Wikipedia", "url": "https://en.wikipedia.org/wiki/SMS" }
                ]
            },
            {
                "id": "dr-dre-the-chronic-gfunk-1992",
                "title": "Dr. Dre Drops 'The Chronic' & G-Funk Takes Over",
                "year": 1992,
                "date": "1992-12-15",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Dr. Dre released 'The Chronic', introducing Snoop Doggy Dogg and lazy Parliament-Funk synthesizer melodies to hip-hop.",
                "narrative": "With rolling basslines, whining Moog synths, and laid-back cadence, 'The Chronic' redefined hip-hop from gritty New York street realism into sunny, low-riding West Coast cinema. Hits like 'Nuthin' but a 'G' Thang' dominated MTV rotations and car stereos, turning Death Row Records into an entertainment empire and cementing hip-hop as pop culture's definitive vanguard.",
                "why_it_matters": "It established production values in hip-hop that matched major pop releases and launched Snoop Dogg into an enduring global cultural icon.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "The Chronic - Wikipedia", "url": "https://en.wikipedia.org/wiki/The_Chronic" }
                ]
            },
            {
                "id": "la-riots-and-clinton-1992",
                "title": "Los Angeles Riots & Bill Clinton's 'It's the Economy, Stupid'",
                "year": 1992,
                "date": "1992-04-29",
                "category": ["news", "culture"],
                "type": "cultural_shift",
                "summary": "Six days of civil unrest engulfed Los Angeles after the Rodney King verdict, while Bill Clinton won the White House on MTV appeal.",
                "narrative": "The acquittal of LAPD officers in the videotaped beating of Rodney King ignited six days of intense civil disturbance across Los Angeles, captured from news helicopters in dizzying live TV feeds. Months later, 46-year-old Arkansas Governor Bill Clinton appeared on MTV playing the saxophone in sunglasses, bypassing traditional gatekeepers and capturing the youth vote to end 12 years of Republican presidency.",
                "why_it_matters": "The LA riots exposed deep racial and economic fractures, while Clinton's MTV appearance signaled the modern fusion of youth media and politics.",
                "impact": 4,
                "nostalgia": 4,
                "sources": [
                    { "title": "1992 Los Angeles riots - Wikipedia", "url": "https://en.wikipedia.org/wiki/1992_Los_Angeles_riots" }
                ]
            }
        ]
    },
    1993: {
        "felt_like": {
            "os": "Windows 3.11 for Workgroups / MS-DOS 6.2",
            "browser": "NCSA Mosaic 1.0 / Lynx / Cello",
            "messenger": "IRC / Local BBS chat / University talk",
            "social_network": "Usenet alt.* hierarchies",
            "music": "Snoop Dogg, Wu-Tang Clan, Nirvana Unplugged, Pearl Jam",
            "phone": "Motorola flip phone & translucent alphanumeric pagers",
            "video": "VHS tapes & cathode-ray tube TVs with built-in VCRs",
            "website": "Grey backgrounds with inline <img> tags in Mosaic",
            "fashion": "Baggy overalls with one strap unbuckled, skater hoodies, backward ballcaps",
            "gadget": "Apple Newton MessagePad & Sega Game Gear",
            "news": "European Union established (Maastricht Treaty); World Trade Center bombing",
            "culture": "Jurassic Park CGI revolution; The X-Files premieres"
        },
        "new_events": [
            {
                "id": "cern-public-domain-web-1993",
                "title": "CERN Puts the World Wide Web into the Public Domain",
                "year": 1993,
                "date": "1993-04-30",
                "category": ["standards", "web"],
                "type": "milestone",
                "summary": "CERN made the World Wide Web source code available on a royalty-free basis forever.",
                "narrative": "Had CERN decided to patent and license the World Wide Web software, the web as we know it would likely not exist. Instead, CERN directors and Tim Berners-Lee signed a historic declaration placing the underlying code into the public domain with no royalties or fees. This single decision made it risk-free for developers, hobbyists, and universities around the globe to build browsers and host websites without paying a cent.",
                "why_it_matters": "This is widely celebrated as the single most consequential legal decision in internet history, guaranteeing the open architecture of the web.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "CERN puts the World Wide Web in public domain - CERN", "url": "https://home.cern/news/news/computing/thirty-years-open-web" }
                ]
            },
            {
                "id": "doom-shareware-multiplayer-1993",
                "title": "id Software Releases DOOM: 3D Gaming & LAN Deathmatches",
                "year": 1993,
                "date": "1993-12-10",
                "category": ["gaming", "software"],
                "type": "launch",
                "summary": "John Carmack and John Romero released DOOM via shareware, bringing university computer networks to a screeching halt.",
                "narrative": "Uploaded to an FTP server at the University of Wisconsin at midnight, DOOM's first episode was free to copy and distribute. With texture-mapped 3D lighting, visceral shotgun combat, and peer-to-peer four-player LAN 'deathmatches', it became an instant international addiction. System administrators at Intel and universities had to write custom scripts just to purge DOOM network packets from their clogged servers.",
                "why_it_matters": "DOOM pioneered first-person 3D game engines, shareware viral distribution, user-created mods (WADs), and multiplayer competitive gaming.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Doom (1993 video game) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Doom_(1993_video_game)" }
                ]
            },
            {
                "id": "jurassic-park-cgi-revolution-1993",
                "title": "Jurassic Park Ushers in the Photorealistic CGI Era",
                "year": 1993,
                "date": "1993-06-11",
                "category": ["culture", "media"],
                "type": "cultural_shift",
                "summary": "Steven Spielberg and ILM amazed the world with computer-generated dinosaurs, transforming Hollywood cinema forever.",
                "narrative": "When paleontologist Alan Grant took off his sunglasses to gaze upon a living, breathing digital Brachiosaurus grazing in the canopy, audiences around the world gasped in unison. Industrial Light & Magic's Dennis Muren proved that Silicon Graphics computers could render lifelike living creatures with skin weight and lighting. Stop-motion animator Phil Tippett famously whispered, 'I think I'm extinct.'",
                "why_it_matters": "Jurassic Park proved computer graphics could carry emotional narrative weight, setting the gold standard for visual effects for the next three decades.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Jurassic Park (film) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Jurassic_Park_(film)" }
                ]
            }
        ]
    },
    1994: {
        "felt_like": {
            "os": "Windows 3.11 / Mac System 7.5",
            "browser": "Netscape Navigator 1.0 / Mosaic 2.0",
            "messenger": "IRC / PowWow / BBS chat",
            "social_network": "Usenet & CompuServe forums",
            "music": "Green Day's Dookie, Weezer, TLC, Nas, Biggie",
            "phone": "Motorola MicroTAC & translucent neon numeric pagers",
            "video": "VHS tapes & laserdiscs",
            "website": "Grey backgrounds with blue underlined hyperlinks",
            "fashion": "Plaid flannel, slip dresses over baby tees, knee-high socks, Doc Martens",
            "gadget": "Sony PlayStation (Japan debut) & Iomega Zip Drive 100MB",
            "news": "O.J. Simpson Ford Bronco chase; Nelson Mandela elected President",
            "culture": "Friends premieres on NBC; Pulp Fiction wins Cannes Palme d'Or"
        },
        "new_events": [
            {
                "id": "playstation-japan-launch-1994",
                "title": "Sony Unveils the PlayStation in Japan",
                "year": 1994,
                "date": "1994-12-03",
                "category": ["gadget", "gaming"],
                "type": "launch",
                "summary": "Ken Kutaragi's 32-bit CD-ROM powerhouse launched in Japan, forever altering the console gaming landscape.",
                "narrative": "Born from a bitter broken partnership with Nintendo, Sony's gamble was led by engineer Ken Kutaragi. The PlayStation relied on cheap CD-ROM media that could store real orchestral soundtracks, full-motion video, and complex 3D polygon graphics. Lines wrapped around Tokyo electronics retailers on launch day, initiating a dynasty that would dethrone cartridged giants Nintendo and Sega.",
                "why_it_matters": "The PlayStation matured video games from toys for kids into an edgy lifestyle entertainment medium for teenagers and young adults.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "PlayStation (console) - Wikipedia", "url": "https://en.wikipedia.org/wiki/PlayStation_(console)" }
                ]
            },
            {
                "id": "oj-simpson-chase-media-1994",
                "title": "The O.J. Simpson Bronco Chase Captivates 95M Viewers",
                "year": 1994,
                "date": "1994-06-17",
                "category": ["news", "culture"],
                "type": "cultural_shift",
                "summary": "A low-speed chase along California freeways drew 95 million viewers and interrupted the NBA Finals.",
                "narrative": "On June 17, 1994, helicopters tracked Al Cowlings driving football legend O.J. Simpson in a white Ford Bronco down Interstate 405. Domino's Pizza reported record delivery volumes as the entire nation stayed glued to their living room screens. On early internet message boards and Usenet, people posted real-time commentary, previewing the dual-screen social viewing habits of the modern age.",
                "why_it_matters": "It established the template for the modern 24/7 cable news sensation and live participatory pop-culture event.",
                "impact": 4,
                "nostalgia": 4,
                "sources": [
                    { "title": "O.J. Simpson chase - Wikipedia", "url": "https://en.wikipedia.org/wiki/O._J._Simpson_murder_case" }
                ]
            },
            {
                "id": "hiphop-golden-illmatic-ready-to-die-1994",
                "title": "Nas Drops 'Illmatic' & Biggie Drops 'Ready to Die'",
                "year": 1994,
                "date": "1994-04-19",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "East Coast hip-hop hit its zenith with two of the most critically celebrated and influential albums in music history.",
                "narrative": "In April 1994, 20-year-old Queensbridge prodigy Nas released 'Illmatic'—ten tracks of poetic, razor-sharp lyricism over beats by DJ Premier, Large Professor, and Pete Rock. Five months later, The Notorious B.I.G. released 'Ready to Die', blending cinematic Brooklyn street narratives with infectious Bad Boy pop hooks. The albums restored New York to hip-hop primacy and defined 90s urban culture.",
                "why_it_matters": "These albums set the gold standard for rhyme cadence, storytelling, and hip-hop album production that influenced generations of artists.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Illmatic - Wikipedia", "url": "https://en.wikipedia.org/wiki/Illmatic" },
                    { "title": "Ready to Die - Wikipedia", "url": "https://en.wikipedia.org/wiki/Ready_to_Die" }
                ]
            }
        ]
    },
    1995: {
        "felt_like": {
            "os": "Windows 95 / Mac OS 7.5.1",
            "browser": "Netscape Navigator 2.0 / Internet Explorer 1.0",
            "messenger": "ICQ / PowWow / IRC",
            "social_network": "GeoCities neighborhoods / The Palace",
            "music": "Alanis Morissette, Coolio, TLC, Oasis, cassette & CD mix",
            "phone": "Nokia 2110 & Motorola StarTAC predecessor",
            "video": "VHS rentals & animated GIF loops",
            "website": "Hit counters, Under Construction animated GIFs, MIDI music",
            "fashion": "Slip dresses, choker necklaces, platform sneakers, bucket hats",
            "gadget": "Sony PlayStation (US launch) & Iomega 100MB Zip Drive",
            "news": "Oklahoma City bombing; Million Man March in Washington",
            "culture": "Pixar's Toy Story debuts; Clueless defines 90s teen lexicon"
        },
        "new_events": [
            {
                "id": "toy-story-pixar-cgi-1995",
                "title": "Pixar & Disney Release 'Toy Story': First 3D CGI Feature",
                "year": 1995,
                "date": "1995-11-22",
                "category": ["culture", "tech"],
                "type": "cultural_shift",
                "summary": "Director John Lasseter and Steve Jobs' Pixar released the first entirely computer-animated feature film.",
                "narrative": "Woody and Buzz Lightyear weren't just beloved characters—they were milestones in rendering technology. Produced using Pixar's RenderMan software on a farm of 117 Sun Microsystems computers, the film took 800,000 machine hours to compute. Critics praised its heartfelt story and witty script, earning over $373 million and proving computer graphics could rival traditional hand-drawn animation in artistic soul.",
                "why_it_matters": "Toy Story launched Pixar into an animation titan, revitalized Steve Jobs' personal fortune, and permanently altered feature animation history.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Toy Story - Wikipedia", "url": "https://en.wikipedia.org/wiki/Toy_Story" }
                ]
            },
            {
                "id": "ebay-auctionweb-founded-1995",
                "title": "Pierre Omidyar Launches eBay (AuctionWeb)",
                "year": 1995,
                "date": "1995-09-03",
                "category": ["business", "web"],
                "type": "launch",
                "summary": "On Labor Day weekend, French-born Iranian-American software engineer Pierre Omidyar coded AuctionWeb in his San Jose apartment.",
                "narrative": "The first item Omidyar posted was a broken laser pointer for $1. Astonished when a collector bought it for $14.83, Omidyar realized the internet could connect buyers and sellers of niche, long-tail goods with zero friction. Within months, people were bidding on vintage Pez dispensers, Beanie Babies, and sports cards, inventing peer-to-peer online commerce and consumer feedback ratings.",
                "why_it_matters": "eBay democratized global commerce, proving complete strangers across the globe could trust each other to exchange money and goods online.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "eBay - Wikipedia", "url": "https://en.wikipedia.org/wiki/EBay" }
                ]
            },
            {
                "id": "alanis-morissette-jagged-little-pill-1995",
                "title": "Alanis Morissette's 'Jagged Little Pill' Sweeps the World",
                "year": 1995,
                "date": "1995-06-13",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "21-year-old Canadian singer-songwriter Alanis Morissette released an unfiltered, cathartic alt-rock tour de force.",
                "narrative": "Singles like 'You Oughta Know' (featuring Flea and Dave Navarro on bass and guitar) and 'Ironic' exploded onto radio airwaves and MTV. With unflinching honesty, vocal vulnerability, and raw rage, Morissette spoke to a generation of young women hungry for authentic expression. The album went on to sell over 33 million copies worldwide and won four Grammy Awards including Album of the Year.",
                "why_it_matters": "It smashed the glass ceiling for 90s female rock artists on commercial radio and opened doors for Lilith Fair and alternative pop.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Jagged Little Pill - Wikipedia", "url": "https://en.wikipedia.org/wiki/Jagged_Little_Pill" }
                ]
            }
        ]
    },
    1996: {
        "felt_like": {
            "os": "Windows 95 OSR2 / Mac OS 7.6",
            "browser": "Netscape Navigator 3.0 / Internet Explorer 3.0",
            "messenger": "ICQ ('Uh-oh!') / AIM prototype / IRC",
            "social_network": "GeoCities / Tripod / WebChat Broadcasting System",
            "music": "Spice Girls, 2Pac, The Fugees, No Doubt, CD players",
            "phone": "Motorola StarTAC (clamshell icon) & Nokia 8110 (banana phone)",
            "video": "VHS tapes & early DVD demonstration discs",
            "website": "Framesets, table layouts, blinking text, guestbooks",
            "fashion": "Spice Girls platform boots, Tommy Hilfiger logos, cargo pants, frosted lip gloss",
            "gadget": "Nintendo 64 & PalmPilot 1000 PDA",
            "news": "Dolly the Sheep becomes first cloned mammal; Atlanta Centennial Olympic Games",
            "culture": "Independence Day box office smash; Scream revitalizes teen horror"
        },
        "new_events": [
            {
                "id": "nintendo-64-mario-64-1996",
                "title": "Nintendo 64 Launches with 'Super Mario 64'",
                "year": 1996,
                "date": "1996-06-23",
                "category": ["gadget", "gaming"],
                "type": "launch",
                "summary": "Nintendo released the N64 featuring an analog thumbstick and the groundbreaking 3D masterpiece Super Mario 64.",
                "narrative": "Shigeru Miyamoto didn't just translate Mario to 3D; he invented the camera system, fluid analog movement, and open-ended playground exploration that defined all modern third-person action games. From triple jumps outside Princess Peach's castle to four-player couch multiplayer in GoldenEye 007, the N64 made living rooms the epicenter of social gaming.",
                "why_it_matters": "Super Mario 64 established the rules of 3D spatial navigation, camera control, and momentum in video games that are still standard today.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Nintendo 64 - Wikipedia", "url": "https://en.wikipedia.org/wiki/Nintendo_64" }
                ]
            },
            {
                "id": "spice-girls-girl-power-1996",
                "title": "Spice Girls Unleash 'Wannabe' & the 'Girl Power' Wave",
                "year": 1996,
                "date": "1996-07-08",
                "category": ["music", "fashion"],
                "type": "cultural_shift",
                "summary": "Posh, Baby, Scary, Sporty, and Ginger Spice topped charts in 37 countries with their debut single 'Wannabe'.",
                "narrative": "Bursting onto hotel banisters in the iconic one-shot music video, the Spice Girls brought unapologetic female friendship, high-energy pop, and distinct individual personas to global youth. Merchandising followed instantly: Union Jack dresses, platform Buffalo sneakers, Chupa Chups lollipops, and Polaroid cameras. 'Girl Power' became the defining feminist pop slogan of the decade.",
                "why_it_matters": "The Spice Girls spearheaded the late-90s teen pop explosion, reviving British pop culture globally in a phenomenon nicknamed 'Spicemania'.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Wannabe (song) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Wannabe_(song)" }
                ]
            },
            {
                "id": "dolly-the-sheep-cloned-1996",
                "title": "Dolly the Sheep Cloned at Roslin Institute",
                "year": 1996,
                "date": "1996-07-05",
                "category": ["science", "news"],
                "type": "milestone",
                "summary": "Scientists in Scotland successfully cloned the first mammal from an adult somatic cell.",
                "narrative": "Born at the Roslin Institute near Edinburgh, a Finn-Dorset sheep named Dolly shattered long-held scientific dogma that adult specialized cells could not be reprogrammed to create an entirely new living creature. When the news went public, it sparked global debate on genetics, ethics, stem cell research, and the potential cloning of human beings.",
                "why_it_matters": "Dolly was hailed as one of the century's great scientific breakthroughs, opening the door to modern stem cell therapeutics and regenerative medicine.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Dolly (sheep) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Dolly_(sheep)" }
                ]
            }
        ]
    },
    1997: {
        "felt_like": {
            "os": "Windows 95 / Windows 98 beta / Mac OS 8",
            "browser": "Internet Explorer 4.0 / Netscape Communicator",
            "messenger": "AOL Instant Messenger (AIM) / ICQ",
            "social_network": "SixDegrees.com / GeoCities communities",
            "music": "The Notorious B.I.G., Radiohead, Hanson, Puff Daddy, Winamp MP3s",
            "phone": "Nokia 6110 with Snake game",
            "video": "VHS & early Toshiba DVD players",
            "website": "Flash intros, scrolling marquee text, webrings",
            "fashion": "Baggy JNCO jeans, butterfly hair clips, tracksuits, bucket hats",
            "gadget": "Tamagotchi virtual pets & first commercial DVD players",
            "news": "Death of Princess Diana; Hong Kong handover to China",
            "culture": "James Cameron's Titanic breaks records; Harry Potter book one published"
        },
        "new_events": [
            {
                "id": "princess-diana-global-grief-1997",
                "title": "The World Mourns Princess Diana",
                "year": 1997,
                "date": "1997-08-31",
                "category": ["news", "culture"],
                "type": "cultural_shift",
                "summary": "The tragic death of Diana, Princess of Wales in Paris triggered an unprecedented wave of global grief.",
                "narrative": "Over 2.5 billion people tuned in to watch Princess Diana's funeral, while Elton John performed 'Candle in the Wind 1997' at Westminster Abbey. Outside Kensington Palace, a sea of over 60 million flowers piled feet deep. On the emerging World Wide Web, remembrance sites and news portals crashed under the weight of people seeking information, marking one of the first major web traffic surges.",
                "why_it_matters": "The tragedy transformed the British monarchy's public relationship and demonstrated how the web had become an international communal mourning ground.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Death of Diana, Princess of Wales - Wikipedia", "url": "https://en.wikipedia.org/wiki/Death_of_Diana,_Princess_of_Wales" }
                ]
            },
            {
                "id": "tamagotchi-craze-1997",
                "title": "Bandai's Tamagotchi Virtual Pet Craze",
                "year": 1997,
                "date": "1997-05-01",
                "category": ["gadget", "culture"],
                "type": "cultural_shift",
                "summary": "Japanese toy company Bandai released Tamagotchi in the West, creating a worldwide virtual pet frenzy.",
                "narrative": "Egg-shaped keychains with low-res LCD screens and three small buttons beeped insistently from children's backpacks. Players had to feed, discipline, clean up after, and entertain their pixelated digital pets or watch them sprout angel wings and perish. Schools across the US and UK banned them from classrooms as kids desperately checked on their pets between lessons.",
                "why_it_matters": "Tamagotchi proved that humans could develop profound emotional attachments to simple software and digital entities.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Tamagotchi - Wikipedia", "url": "https://en.wikipedia.org/wiki/Tamagotchi" }
                ]
            },
            {
                "id": "radiohead-ok-computer-1997",
                "title": "Radiohead Releases 'OK Computer'",
                "year": 1997,
                "date": "1997-05-21",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Radiohead's third studio album presaged 21st-century technological alienation, digital surveillance, and consumerist anxiety.",
                "narrative": "Recorded in a secluded 16th-century mansion near Bath, 'OK Computer' blended lush guitars with Mellotrons, glitching Roland electronic drums, and robotic speech synthesizers like 'Fitter Happier'. Songs like 'Paranoid Android' and 'Karma Police' captured a visceral foreboding about modern automated life just as computers and office cubicles were swallowing everyday routine.",
                "why_it_matters": "Widely ranked among the greatest rock albums ever recorded, it served as the prophetic philosophical soundtrack to the digital transition.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "OK Computer - Wikipedia", "url": "https://en.wikipedia.org/wiki/OK_Computer" }
                ]
            }
        ]
    },
    1998: {
        "felt_like": {
            "os": "Windows 98 / Mac OS 8.5",
            "browser": "Internet Explorer 4.01 / Netscape Communicator 4.5",
            "messenger": "AIM ('Buddy List' door slam) / ICQ / Yahoo Messenger",
            "social_network": "SixDegrees.com / TalkCity chatrooms",
            "music": "Britney Spears, Lauryn Hill, Cher 'Believe' Auto-Tune, MP3 downloads",
            "phone": "Nokia 5110 with interchangeable faceplates",
            "video": "DVD rentals entering Blockbuster & VHS",
            "website": "Flash animations, cascading stylesheets (CSS), banner ad networks",
            "fashion": "Frosted hair tips, oval wire-rim sunglasses, cargo pants, baby tees",
            "gadget": "Apple iMac G3 Bondi Blue & Game Boy Color",
            "news": "Clinton-Lewinsky scandal; Good Friday Agreement signed in Northern Ireland",
            "culture": "The Truman Show presages reality TV; Pokémon Red & Blue launch in the West"
        },
        "new_events": [
            {
                "id": "apple-imac-g3-bondi-blue-1998",
                "title": "Steve Jobs Unveils the Bondi Blue iMac G3",
                "year": 1998,
                "date": "1998-05-06",
                "category": ["gadget", "design"],
                "type": "launch",
                "summary": "Apple introduced the translucent Bondi Blue all-in-one iMac G3, reviving the company and redefining industrial design.",
                "narrative": "Steve Jobs walked onto the Flint Center stage and pulled the cloth off a computer that looked like candy from another planet. Designed by Jony Ive, the iMac dumped beige plastic boxes and murdered the legacy 3.5-inch floppy drive in favor of twin USB ports. It promised one-step connection to the internet in under ten minutes, instantly transforming Apple from near-bankruptcy into a cultural icon.",
                "why_it_matters": "The iMac G3 kicked off Apple's golden renaissance and sparked a design revolution that brought vibrant translucent plastics to everything from irons to Game Boys.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "iMac G3 - Wikipedia", "url": "https://en.wikipedia.org/wiki/IMac_G3" }
                ]
            },
            {
                "id": "pokemon-red-blue-craze-1998",
                "title": "Pokémon Red & Blue Conquers the West",
                "year": 1998,
                "date": "1998-09-28",
                "category": ["gadget", "gaming", "culture"],
                "type": "cultural_shift",
                "summary": "Nintendo released Pokémon Red and Blue for Game Boy in North America, launching an unmatched multimedia juggernaut.",
                "narrative": "Equipped with Game Boy link cables, kids huddled in schoolyards trading Pikachu, Charizard, and Mew. The tagline 'Gotta catch 'em all!' fueled an obsession spanning animated television series, foil trading cards that sold for hundreds of dollars, and feature films. Created by Satoshi Tajiri out of his childhood passion for insect collecting, Pokémon became the highest-grossing media franchise in history.",
                "why_it_matters": "Pokémon demonstrated the power of transmedia franchises and community-driven social trading games decades before smartphone app stores.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Pokmon Red and Blue - Wikipedia", "url": "https://en.wikipedia.org/wiki/Pok%C3%A9mon_Red_and_Blue" }
                ]
            },
            {
                "id": "drudge-report-breaks-lewinsky-1998",
                "title": "Drudge Report Breaks the Clinton-Lewinsky Scandal Online",
                "year": 1998,
                "date": "1998-01-17",
                "category": ["news", "web"],
                "type": "cultural_shift",
                "summary": "Matt Drudge published what Newsweek had chosen to sit on, inaugurating internet news supremacy.",
                "narrative": "Operating from a dingy Hollywood apartment, independent web journalist Matt Drudge typed a late-night dispatch revealing that Newsweek had killed a story investigating President Bill Clinton's relationship with a White House intern named Monica Lewinsky. The link ricocheted across bulletin boards and talk radio, forcing mainstream television networks to report on an internet post.",
                "why_it_matters": "It demonstrated that internet aggregators and bloggers could bypass traditional editorial gatekeepers and dictate the national news cycle.",
                "impact": 4,
                "nostalgia": 3,
                "sources": [
                    { "title": "Drudge Report - Wikipedia", "url": "https://en.wikipedia.org/wiki/Drudge_Report" }
                ]
            }
        ]
    },
    1999: {
        "felt_like": {
            "os": "Windows 98 Second Edition / Mac OS 9",
            "browser": "Internet Explorer 5.0 / Netscape Communicator 4.7",
            "messenger": "AIM / MSN Messenger / ICQ 99b",
            "social_network": "LiveJournal / Open Diary / BlackPlanet",
            "music": "Napster MP3s, Backstreet Boys, TLC, Blink-182, Limp Bizkit",
            "phone": "Nokia 3210 (internal antenna, composer) & Matrix slider 8110",
            "video": "DVD players going mainstream & VHS recording",
            "website": "Flash portals, animated intro screens, dot-com company billboards",
            "fashion": "Y2K metallic shirts, visor sunglasses, bleached hair, inflatable furniture",
            "gadget": "RIM BlackBerry 850 pager & Sega Dreamcast with 56k modem",
            "news": "Y2K bug panic reaches fever pitch; Columbine High School shooting",
            "culture": "The Matrix redefines action cinema & cyberpunk style; Fight Club"
        },
        "new_events": [
            {
                "id": "the-matrix-cyberpunk-1999",
                "title": "The Matrix Hits Theaters & Defines Cyberpunk Cool",
                "year": 1999,
                "date": "1999-03-31",
                "category": ["culture", "tech"],
                "type": "cultural_shift",
                "summary": "The Wachowskis' sci-fi masterpiece fused cyberpunk philosophy, anime stunts, and 'bullet time' visual effects.",
                "narrative": "Audiences were asked to take the red pill and woke up inside a simulated world. Keanu Reeves dodging bullets on a rooftop in slow-motion green phosphor tint became the visual wallpaper of the millennium. Everything from black leather trench coats, tiny sunglasses, and Nokia slider phones to philosophical debates about simulated reality seeped directly into global tech culture.",
                "why_it_matters": "The Matrix permanently encoded cyberpunk aesthetics and simulation anxiety into modern internet culture and cinema visual effects.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "The Matrix - Wikipedia", "url": "https://en.wikipedia.org/wiki/The_Matrix" }
                ]
            },
            {
                "id": "y2k-panic-preparations-1999",
                "title": "The Y2K Bug Panic & The Midnight Countdown",
                "year": 1999,
                "date": "1999-12-31",
                "category": ["tech", "news"],
                "type": "cultural_shift",
                "summary": "Fears that older two-digit year computer systems would crash at midnight caused worldwide preparations and dread.",
                "narrative": "Doomsday preppers stockpiled canned peaches, bottled water, and generators, while airlines grounded midnight flights. Corporations and governments invested over $300 billion in heroic remediation efforts to rewrite legacy COBOL and database systems. When the clock struck midnight in Sydney, Tokyo, London, and New York, the lights stayed on and computers hummed along peacefully, turning terror into celebration.",
                "why_it_matters": "The Y2K bug represented the first time global society collectively recognized its absolute dependency on silent digital infrastructure.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Year 2000 problem - Wikipedia", "url": "https://en.wikipedia.org/wiki/Year_2000_problem" }
                ]
            },
            {
                "id": "teen-pop-explosion-britney-backstreet-1999",
                "title": "Britney Spears & Backstreet Boys Lead Teen Pop Mania",
                "year": 1999,
                "date": "1999-05-18",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Britney Spears' '...Baby One More Time' and the Backstreet Boys' 'Millennium' shattered music industry sales records.",
                "narrative": "MTV's studio in Times Square for Total Request Live (TRL) with Carson Daly became the screaming epicenter of American adolescence. Backstreet Boys' 'Millennium' sold over 1.1 million copies in its first week alone, while 17-year-old Britney Spears became an overnight pop titan. CD sales peaked at their all-time historical high just as Napster was quietly being born in a college dorm.",
                "why_it_matters": "It marked the commercial apex of the physical CD music industry right before digital file-sharing decentralized music distribution forever.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "...Baby One More Time (album) - Wikipedia", "url": "https://en.wikipedia.org/wiki/...Baby_One_More_Time_(album)" },
                    { "title": "Millennium (Backstreet Boys album) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Millennium_(Backstreet_Boys_album)" }
                ]
            }
        ]
    }
}

def apply_era1():
    for year, data in ERA1_UPDATES.items():
        # 1. Update year file
        year_path = f"src/data/years/{year}.json"
        with open(year_path, "r") as f:
            ydata = json.load(f)
        
        # update felt_like
        ydata["felt_like"] = data["felt_like"]
        
        # 2. Update events file
        events_path = f"src/data/events/{year}.json"
        with open(events_path, "r") as f:
            events = json.load(f)
        
        # Fix known inaccuracies in existing events
        if year == 1990:
            # fix EuropaNet typo and Mosaic nascent
            for e in events:
                if e["id"] == "europanet-launch-1990":
                    e["title"] = "EuropaNet: Early European Network"
                if e["id"] == "ncsa-mosaic-nascent-1990":
                    e["summary"] = "Research into distributed hypertext interfaces expanded, inspiring subsequent browser development at NCSA."
        elif year == 1993:
            for e in events:
                if e["id"] == "windows-3-1-1993":
                    e["title"] = "Windows for Workgroups 3.11 Released"
                    e["summary"] = "Microsoft released Windows for Workgroups 3.11 with integrated peer-to-peer networking support."
        
        # Add new events (avoid duplicates)
        existing_ids = set(e["id"] for e in events)
        for ne in data["new_events"]:
            if ne["id"] not in existing_ids:
                events.append(ne)
                existing_ids.add(ne["id"])
        
        # sync event IDs in ydata["events"]
        ydata["events"] = [e["id"] for e in events]
        
        with open(year_path, "w") as f:
            json.dump(ydata, f, indent=2)
            f.write("\n")
            
        with open(events_path, "w") as f:
            json.dump(events, f, indent=2)
            f.write("\n")
            
        print(f"Enriched {year}: {len(events)} events, 12 felt_like keys.")

if __name__ == "__main__":
    apply_era1()
