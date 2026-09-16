import json

ERA2_UPDATES = {
    2000: {
        "felt_like": {
            "os": "Windows 98 / Windows 2000 / Mac OS 9",
            "browser": "Internet Explorer 5.5 / Netscape 6",
            "messenger": "AIM / ICQ 2000 / MSN Messenger",
            "social_network": "Napster / LiveJournal / Webring forums",
            "music": "Napster MP3s, Eminem, Outkast, burned CD-Rs with Sharpie labels",
            "phone": "Nokia 3310 with Snake II & custom monochromatic ringtones",
            "video": "RealPlayer buffering clips & Blockbuster DVD rentals",
            "website": "Flash intro splash screens, 800x600 resolution banners, visitor counters",
            "fashion": "Y2K metallics, low-rise cargo pants, bandana halter tops, visor sunglasses",
            "gadget": "Sony PlayStation 2 & Nokia 3310",
            "news": "Bush vs. Gore Florida recount election; Dot-com bubble collapses",
            "culture": "Cast Away, Gladiator, Survivor season one finale attracts 51M viewers"
        },
        "new_events": [
            {
                "id": "nokia-3310-snake-2000",
                "title": "Nokia 3310 & the 'Snake II' Mobile Craze",
                "year": 2000,
                "date": "2000-09-01",
                "category": ["gadget", "culture"],
                "type": "launch",
                "summary": "Nokia released the legendary 3310, selling 126 million units and making mobile gaming universal.",
                "narrative": "Practically indestructible, with battery life lasting over a week and customizable Xpress-on clip-on covers, the Finnish phone was an instant classic. School buses and dorm rooms fell silent as teenagers navigated pixelated reptiles around dot obstacles in Snake II or keyed in custom monophonic ringtones note-by-note. It turned the mobile phone from a corporate executive tool into an indispensable teen lifestyle accessory.",
                "why_it_matters": "The 3310 democratized mobile ownership for youth, popularizing SMS shorthand and mobile gaming years before smartphones.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Nokia 3310 - Wikipedia", "url": "https://en.wikipedia.org/wiki/Nokia_3310" }
                ]
            },
            {
                "id": "bush-gore-election-hanging-chads-2000",
                "title": "Bush vs. Gore: The Florida Recount & Early Viral Satire",
                "year": 2000,
                "date": "2000-11-07",
                "category": ["news", "culture"],
                "type": "cultural_shift",
                "summary": "A 537-vote margin in Florida triggered a 36-day recount saga that birthed modern internet political satire.",
                "narrative": "Terms like 'hanging chads', 'pregnant chads', and 'butterfly ballots' dominated evening news for five weeks as officials held paper punch cards up to magnifying glasses. On the web, satirical Flash animations on sites like JibJab and early political blogs exploded, providing irreverent real-time commentary before the Supreme Court ended the recount in Bush v. Gore.",
                "why_it_matters": "The election hyper-charged online political engagement and established the web as a central theater for civic discussion and political satire.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "2000 United States presidential election - Wikipedia", "url": "https://en.wikipedia.org/wiki/2000_United_States_presidential_election" }
                ]
            },
            {
                "id": "eminem-marshall-mathers-outkast-2000",
                "title": "Eminem's 'MMLP' & Outkast's 'Stankonia' Dominate Pop Culture",
                "year": 2000,
                "date": "2000-05-23",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Eminem sold 1.76 million copies in seven days, while Atlanta duo Outkast elevated hip-hop into cosmic art.",
                "narrative": "Bleached-blonde Detroit rapper Eminem became the biggest lightning rod in American culture. 'The Marshall Mathers LP' broke Nielsen SoundScan records for the fastest-selling solo album in US history, propelled by the manic satire of 'The Real Slim Shady'. Later that autumn, Outkast dropped 'Stankonia' with 'Ms. Jackson' and 'B.O.B.', blending Southern bounce with psychedelic funk.",
                "why_it_matters": "Hip-hop cemented its role as the dominant creative and commercial force in global music, transcending traditional racial and genre boundaries.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "The Marshall Mathers LP - Wikipedia", "url": "https://en.wikipedia.org/wiki/The_Marshall_Mathers_LP" },
                    { "title": "Stankonia - Wikipedia", "url": "https://en.wikipedia.org/wiki/Stankonia" }
                ]
            }
        ]
    },
    2001: {
        "felt_like": {
            "os": "Windows XP (Bliss wallpaper) / Mac OS X 10.0 Cheetah",
            "browser": "Internet Explorer 6.0 / Netscape 6.2",
            "messenger": "AIM / MSN Messenger with custom emoticons / Yahoo Messenger",
            "social_network": "Napster (shutting down) / Audiogalaxy / Kazaa / LiveJournal",
            "music": "Apple iPod (1,000 songs in your pocket), white earbuds, Daft Punk, Jay-Z",
            "phone": "Motorola V60 & Ericsson T68 with color screen",
            "video": "QuickTime trailers, Flash cartoons (Homestar Runner), DVD boxsets",
            "website": "Rounded aqua buttons, drop shadows, bevels, Bliss green hills",
            "fashion": "Low-rise flare jeans, whale tails, trucker hats, newsboy caps, frosted lip gloss",
            "gadget": "Apple iPod (mechanical scroll wheel) & Microsoft Xbox",
            "news": "September 11 attacks reshape geopolitics, aviation, and digital journalism",
            "culture": "The Lord of the Rings: Fellowship of the Ring; Harry Potter film debut"
        },
        "new_events": [
            {
                "id": "halo-combat-evolved-xbox-2001",
                "title": "Bungie Releases 'Halo: Combat Evolved' on Xbox",
                "year": 2001,
                "date": "2001-11-15",
                "category": ["gaming", "culture"],
                "type": "launch",
                "summary": "Bungie and Microsoft released Halo: Combat Evolved, defining twin-stick console shooters and Xbox LAN culture.",
                "narrative": "With its sweeping orchestral choral theme, shield-recharging mechanics, and Master Chief, Halo proved first-person shooters could feel brilliant on a gamepad. Basements and college dorms were transformed into LAN arenas as friends strung Ethernet cables across halls to link four bulky Xbox consoles and CRT TVs for 16-player Blood Gulch Capture the Flag matches.",
                "why_it_matters": "Halo single-handedly validated Microsoft's gamble on the original Xbox console and laid the design foundation for modern console competitive shooters.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Halo: Combat Evolved - Wikipedia", "url": "https://en.wikipedia.org/wiki/Halo:_Combat_Evolved" }
                ]
            },
            {
                "id": "apple-first-retail-stores-2001",
                "title": "Apple Opens Its First Retail Stores",
                "year": 2001,
                "date": "2001-05-19",
                "category": ["business", "design"],
                "type": "launch",
                "summary": "Steve Jobs opened Apple's first retail stores in Virginia and California, defying predictions of failure.",
                "narrative": "Pundits scoffed, with one business magazine writing: 'Sorry Steve, here's why Apple Stores won't work.' But Jobs and retail architect Ron Johnson threw out traditional tech store clutter. Instead of boxes stacked on metal shelves, they designed minimalist temples with blonde maple tables, glass staircases, and the 'Genius Bar' where customers could get free technical help face-to-face.",
                "why_it_matters": "The Apple Store became the most profitable retail space per square foot on Earth, establishing direct customer relationships that powered Apple's ecosystem.",
                "impact": 4,
                "nostalgia": 4,
                "sources": [
                    { "title": "Apple Store - Wikipedia", "url": "https://en.wikipedia.org/wiki/Apple_Store" }
                ]
            },
            {
                "id": "low-rise-jeans-y2k-fashion-2001",
                "title": "Britney's Python, Low-Rise Denim & Y2K Style Apex",
                "year": 2001,
                "date": "2001-09-06",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Britney Spears performed 'I'm a Slave 4 U' draped in a live Burmese python at the MTV VMAs, crowning low-rise denim.",
                "narrative": "The 2001 MTV Video Music Awards captured the pinnacle of Y2K pop fashion. Britney's ultra-low-rise green halter and live snake performance became an instant pop-culture legend. Across shopping malls, denim brands like Frankie B and Miss Sixty lowered waistlines to unprecedented depths, paired with visible thong straps, rhinestones, and belly button piercings.",
                "why_it_matters": "It defined the silhouette of early 2000s celebrity youth culture, inaugurating the tabloid-paparazzi aesthetic that dominated the decade.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "I'm a Slave 4 U - Wikipedia", "url": "https://en.wikipedia.org/wiki/I%27m_a_Slave_4_U" }
                ]
            }
        ]
    },
    2002: {
        "felt_like": {
            "os": "Windows XP Service Pack 1 / Mac OS X 10.2 Jaguar",
            "browser": "Internet Explorer 6.0 / Mozilla 1.0 / Opera 6",
            "messenger": "AIM (custom buddy icons & away messages) / MSN Messenger / Yahoo",
            "social_network": "Friendster (beta buzz) / LiveJournal / Kazaa P2P",
            "music": "Eminem 'Lose Yourself', Avril Lavigne, Nelly 'Hot in Herre', Kazaa MP3s",
            "phone": "Sanyo SCP-5300 (first US camera phone) & Nokia 3510i",
            "video": "Kazaa AVI movie clips & Netflix DVD red envelopes in mail",
            "website": "Flash menu bars, CSS tableless layout movement begins",
            "fashion": "Juicy Couture pink velour tracksuits, skater ties over tank tops, Von Dutch caps",
            "gadget": "Sanyo SCP-5300 camera phone & iPod (2nd Gen with touch wheel)",
            "news": "Euro currency physical banknotes enter circulation; Enron scandal",
            "culture": "American Idol season one with Kelly Clarkson; Spider-Man box office sensation"
        },
        "new_events": [
            {
                "id": "avril-lavigne-juicy-couture-2002",
                "title": "Juicy Couture Velour & Avril Lavigne's Pop-Punk Skater Look",
                "year": 2002,
                "date": "2002-06-04",
                "category": ["fashion", "music"],
                "type": "cultural_shift",
                "summary": "Paris Hilton made pink velour Juicy tracksuits ubiquitous, while 17-year-old Avril Lavigne led a pop-punk revolution.",
                "narrative": "Street fashion splintered in 2002: paparazzi photos showed Paris Hilton and Kim Kardashian living in matching pastel Juicy Couture velour tracksuits with 'JUICY' emblazoned across the back. Meanwhile, 17-year-old Canadian singer Avril Lavigne dropped 'Let Go', pairing loose men's neckties over white tank tops, baggy skater shorts, and studded wristbands in her 'Sk8er Boi' video, sparking a wave of mall-punk style.",
                "why_it_matters": "The contrasting aesthetics showed how teen culture was negotiating between ultra-glam consumerism and alternative rebellion.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Let Go (Avril Lavigne album) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Let_Go_(Avril_Lavigne_album)" }
                ]
            },
            {
                "id": "american-idol-kelly-clarkson-2002",
                "title": "American Idol Debuts & Kelly Clarkson Crowned",
                "year": 2002,
                "date": "2002-09-04",
                "category": ["culture", "media"],
                "type": "cultural_shift",
                "summary": "Fox launched American Idol, turning Simon Cowell's scathing critique and audience landline voting into a national ritual.",
                "narrative": "Over 22 million viewers tuned into the live finale as Texas cocktail waitress Kelly Clarkson belted out 'A Moment Like This', tears streaming down her face. Simon Cowell's blunt British takedowns and Ryan Seacrest's countdowns gripped living rooms. Viewers flooded phone lines with over 15 million votes, demonstrating the power of interactive mass entertainment.",
                "why_it_matters": "American Idol dominated American television ratings for eight consecutive years and created the prototype for reality competition television.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "American Idol (season 1) - Wikipedia", "url": "https://en.wikipedia.org/wiki/American_Idol_(season_1)" }
                ]
            },
            {
                "id": "eminem-lose-yourself-8mile-2002",
                "title": "Eminem Drops 'Lose Yourself' & Conquers Hollywood in '8 Mile'",
                "year": 2002,
                "date": "2002-10-28",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Eminem's semi-autobiographical film 8 Mile became a box office smash, and 'Lose Yourself' won the Academy Award.",
                "narrative": "Opening with 'his palms are sweaty, knees weak, arms are heavy, mom's spaghetti', 'Lose Yourself' became one of hip-hop's most indelible anthems. The film '8 Mile', directed by Curtis Hanson, grossed $242 million and earned critical acclaim for capturing Detroit battle rap culture. When 'Lose Yourself' won the Oscar for Best Original Song, Eminem was asleep at home, having assumed a rap song had zero chance of winning.",
                "why_it_matters": "It was the first hip-hop song in history to win an Academy Award, establishing rap's artistic credibility among traditional cultural institutions.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Lose Yourself - Wikipedia", "url": "https://en.wikipedia.org/wiki/Lose_Yourself" },
                    { "title": "8 Mile (film) - Wikipedia", "url": "https://en.wikipedia.org/wiki/8_Mile_(film)" }
                ]
            }
        ]
    },
    2003: {
        "felt_like": {
            "os": "Windows XP / Mac OS X 10.3 Panther",
            "browser": "Internet Explorer 6.0 / Apple Safari 1.0",
            "messenger": "AIM (subprofile lyrics, away messages) / MSN / Yahoo",
            "social_network": "Friendster (server meltdowns) / MySpace (launching) / LiveJournal",
            "music": "iTunes 99¢ downloads, Beyoncé 'Crazy in Love', 50 Cent, Outkast 'Hey Ya!'",
            "phone": "Motorola V600, Nokia 6600, Sony Ericsson T610",
            "video": "QuickTime Movie Trailers, DVD box sets, Kazaa P2P downloads",
            "website": "Blogging explosion on WordPress & TypePad, clean CSS layouts",
            "fashion": "Von Dutch trucker hats, low-rise flare jeans, layered polo shirts, studded belts",
            "gadget": "iPod 3rd Gen (dock connector, red touch buttons) & Game Boy Advance SP",
            "news": "Space Shuttle Columbia disaster; US-led invasion of Iraq",
            "culture": "The Lord of the Rings: Return of the King sweeps 11 Oscars; Finding Nemo"
        },
        "new_events": [
            {
                "id": "columbia-disaster-iraq-war-2003",
                "title": "Space Shuttle Columbia Disaster & Iraq War Begins",
                "year": 2003,
                "date": "2003-02-01",
                "category": ["news", "history"],
                "type": "milestone",
                "summary": "Space Shuttle Columbia disintegrated during reentry, followed weeks later by the televised invasion of Iraq.",
                "narrative": "On the morning of February 1, 2003, NASA lost contact with Columbia as it streaked across Texas skies, claiming all seven astronauts aboard. Weeks later, television screens glowed with night-vision green 'Shock and Awe' bombing over Baghdad. Online, independent war bloggers and early citizen journalists posted direct reports from Baghdad, challenging official media narratives.",
                "why_it_matters": "The tragedy grounded the shuttle program for over two years, while the Iraq War catalyzed the early political blogosphere and digital anti-war organizing.",
                "impact": 5,
                "nostalgia": 3,
                "sources": [
                    { "title": "Space Shuttle Columbia disaster - Wikipedia", "url": "https://en.wikipedia.org/wiki/Space_Shuttle_Columbia_disaster" }
                ]
            },
            {
                "id": "beyonce-crazy-in-love-50cent-2003",
                "title": "Beyoncé Steps Out Solo & 50 Cent's 'Get Rich or Die Tryin''",
                "year": 2003,
                "date": "2003-02-06",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Beyoncé launched her solo superstar era with 'Crazy in Love', while 50 Cent dominated radio with 'In Da Club'.",
                "narrative": "Stepping out from Destiny's Child in white tank top, denim cutoffs, and red pumps, Beyoncé teamed with Jay-Z for the triumphant horn blasts of 'Crazy in Love'. Meanwhile, Queens rapper 50 Cent, backed by Eminem and Dr. Dre, released 'Get Rich or Die Tryin'', selling 872,000 copies in its first week. His titanium physique and bullet-scarred backstory made him an unstoppable global sensation.",
                "why_it_matters": "Beyoncé and 50 Cent defined mid-2000s urban-pop crossover dominance, setting trends in fashion, music video choreography, and branding.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Crazy in Love - Wikipedia", "url": "https://en.wikipedia.org/wiki/Crazy_in_Love" },
                    { "title": "Get Rich or Die Tryin' - Wikipedia", "url": "https://en.wikipedia.org/wiki/Get_Rich_or_Die_Tryin%27" }
                ]
            },
            {
                "id": "von-dutch-trucker-hats-2003",
                "title": "Von Dutch Trucker Hats & Ashton Kutcher's 'Punk'd'",
                "year": 2003,
                "date": "2003-04-25",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Foam and mesh trucker hats by Von Dutch became the defining fashion craze of Hollywood and malls alike.",
                "narrative": "When actor Ashton Kutcher launched MTV's hidden-camera practical joke show 'Punk'd', he wore a rotating collection of colorful Von Dutch mesh trucker hats. Within weeks, Justin Timberlake, Britney Spears, Lindsay Lohan, and Paris Hilton were photographed wearing them daily. Knockoffs flooded every suburban flea market and mall kiosk across America.",
                "why_it_matters": "It exemplified mid-2000s ironic blue-collar chic, turning a cheap utilitarian work accessory into an expensive high-fashion commodity.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Von Dutch - Wikipedia", "url": "https://en.wikipedia.org/wiki/Von_Dutch" }
                ]
            }
        ]
    },
    2004: {
        "felt_like": {
            "os": "Windows XP Service Pack 2 / Mac OS X 10.3",
            "browser": "Mozilla Firefox 1.0 / Internet Explorer 6",
            "messenger": "AIM / MSN Messenger / Yahoo Messenger",
            "social_network": "MySpace ('Thanks for the add!') / Thefacebook (Harvard only) / Orkut",
            "music": "Kanye West 'The College Dropout', Usher 'Yeah!', Green Day 'American Idiot'",
            "phone": "Motorola RAZR V3 (anodized silver flip icon) & Sidekick II",
            "video": "DVD rentals, bit torrent downloads, LimeWire, QuickTime",
            "website": "Clean CSS, rounded corners, glossy buttons, Web 2.0 gradients",
            "fashion": "Motorola RAZR in pocket, UGG boots with denim skirts, Hollister / Abercrombie tees",
            "gadget": "Motorola RAZR V3 & Nintendo DS",
            "news": "Indian Ocean tsunami disaster; Janet Jackson Super Bowl wardrobe malfunction",
            "culture": "Mean Girls defines high school quote culture; World of Warcraft launches"
        },
        "new_events": [
            {
                "id": "motorola-razr-v3-2004",
                "title": "Motorola RAZR V3: The Ultimate Flip Phone Icon",
                "year": 2004,
                "date": "2004-10-01",
                "category": ["gadget", "design"],
                "type": "launch",
                "summary": "Motorola unveiled the ultra-slim aluminum RAZR V3, selling 130 million units as a global status symbol.",
                "narrative": "At just 13.9 millimeters thin, crafted from aircraft-grade aluminum with an electroluminescent laser-etched keypad, the RAZR was pure pocket jewelry. Snapping it shut with one hand to hang up a call was the most satisfying gesture in consumer technology. From Hollywood red carpets to high school hallways, owning a silver—and later hot pink—RAZR was an unmistakable statement of cool.",
                "why_it_matters": "The RAZR demonstrated that mobile phones were primarily fashion and identity accessories, setting high industrial design expectations before the smartphone era.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Motorola Razr V3 - Wikipedia", "url": "https://en.wikipedia.org/wiki/Motorola_Razr_V3" }
                ]
            },
            {
                "id": "nintendo-ds-touchscreen-2004",
                "title": "Nintendo DS Introduces Dual Screens & Touchscreen Gaming",
                "year": 2004,
                "date": "2004-11-21",
                "category": ["gadget", "gaming"],
                "type": "launch",
                "summary": "Nintendo launched the clamshell DS with dual screens and a stylus, defying doubters to sell 154 million units.",
                "narrative": "Critics initially derided the dual screens and resistive stylus as an awkward gimmick. But Nintendo's vision of intuitive touch control proved prophetic. With games like Super Mario 64 DS, Nintendogs (where players spoke into the built-in microphone), and Brain Age, the DS attracted millions of non-gamers and became the second best-selling video game system of all time.",
                "why_it_matters": "The Nintendo DS normalized touchscreen interfaces for hundreds of millions of people three years before the original iPhone launched.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Nintendo DS - Wikipedia", "url": "https://en.wikipedia.org/wiki/Nintendo_DS" }
                ]
            },
            {
                "id": "indian-ocean-tsunami-2004",
                "title": "Indian Ocean Tsunami & the Dawn of Citizen Video Reporting",
                "year": 2004,
                "date": "2004-12-26",
                "category": ["news", "web"],
                "type": "milestone",
                "summary": "A magnitude 9.1 undersea earthquake triggered catastrophic tsunamis, claiming over 227,000 lives across 14 countries.",
                "narrative": "On the morning after Christmas, massive waves swept across coastal communities from Indonesia and Thailand to Sri Lanka and Somalia. For the first time, dramatic digital video footage captured on vacation camcorders and phone cameras was uploaded directly to blogs and forum threads, bypassing news networks. Internet users mobilized global donation drives through online relief links.",
                "why_it_matters": "The tragedy catalyzed the modern era of crowdsourced emergency relief and citizen-led digital journalism during humanitarian crises.",
                "impact": 5,
                "nostalgia": 2,
                "sources": [
                    { "title": "2004 Indian Ocean earthquake and tsunami - Wikipedia", "url": "https://en.wikipedia.org/wiki/2004_Indian_Ocean_earthquake_and_tsunami" }
                ]
            }
        ]
    },
    2005: {
        "felt_like": {
            "os": "Windows XP Media Center / Mac OS X 10.4 Tiger (Dashboard widgets)",
            "browser": "Firefox 1.5 / Internet Explorer 6",
            "messenger": "AIM 5.9 / MSN Messenger 7.5 (nudges, winks) / Skype",
            "social_network": "MySpace (custom HTML, music autoplay) / Facebook (expanding to high schools)",
            "music": "iPod video with 5G click wheel, Fall Out Boy, Green Day, Gorillaz 'Feel Good Inc.'",
            "phone": "Motorola RAZR / T-Mobile Sidekick II / Sony Ericsson Walkman phone",
            "video": "YouTube (early grainy 320x240 uploads) & video iPod",
            "website": "MySpace profiles with embedded songs, glittering text, top 8 friends",
            "fashion": "Scene hair with flat-ironed side-swept bangs, skinny black jeans, checkerboard Vans, studded belts",
            "gadget": "Xbox 360 (first HD console) & Apple iPod Nano (pencil-thin)",
            "news": "Hurricane Katrina devastates New Orleans; London 7/7 bombings",
            "culture": "Brokeback Mountain, Star Wars Episode III: Revenge of the Sith, The Office US debuts"
        },
        "new_events": [
            {
                "id": "xbox-360-hd-gaming-2005",
                "title": "Microsoft Launches Xbox 360 & Ushers in HD Gaming",
                "year": 2005,
                "date": "2005-11-22",
                "category": ["gadget", "gaming"],
                "type": "launch",
                "summary": "Microsoft launched the Xbox 360 with wireless controllers, unified Gamerscore Achievements, and 720p HD graphics.",
                "narrative": "Selling out instantly at midnight launches, the concave white Xbox 360 set the standard for seventh-generation console gaming. Its unified Xbox Live online network, wireless controller, and addictive 'Achievement Unlocked' chime turned every digital achievement into social bragging rights. Hits like Call of Duty 2 and Gears of War proved high-definition gaming had arrived.",
                "why_it_matters": "The Xbox 360 established Achievements, party voice chat, and unified online infrastructure as mandatory standards for all video game platforms.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Xbox 360 - Wikipedia", "url": "https://en.wikipedia.org/wiki/Xbox_360" }
                ]
            },
            {
                "id": "hurricane-katrina-devastation-2005",
                "title": "Hurricane Katrina Devastates the Gulf Coast",
                "year": 2005,
                "date": "2005-08-29",
                "category": ["news", "history"],
                "type": "milestone",
                "summary": "Catastrophic levee failures submerged 80% of New Orleans, exposing systemic failures and sparking digital relief.",
                "narrative": "When Hurricane Katrina struck, the failure of federal levees flooded New Orleans, trapping tens of thousands of residents in the Superdome and on rooftops in sweltering heat. As television cameras broadcast harrowing scenes of stranded American citizens, online forums, blogs, and makeshift missing-person databases demonstrated how citizens could coordinate mutual aid when government bureaucracies stalled.",
                "why_it_matters": "Katrina exposed deep racial and economic inequalities in America and permanently damaged public faith in federal disaster response.",
                "impact": 5,
                "nostalgia": 3,
                "sources": [
                    { "title": "Hurricane Katrina - Wikipedia", "url": "https://en.wikipedia.org/wiki/Hurricane_Katrina" }
                ]
            },
            {
                "id": "scene-emo-myspace-subculture-2005",
                "title": "Scene Kids, Emo Bangs & MySpace Top 8 Drama",
                "year": 2005,
                "date": "2005-09-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Flat-ironed side bangs, band tees, and MySpace friend rankings defined a massive youth subculture movement.",
                "narrative": "MySpace was the epicenter of teen self-expression. Users spent hours writing raw HTML code to style glittery profiles, choose the perfect profile song from bands like Fall Out Boy and My Chemical Romance, and rank their 'Top 8' friends—a social ranking that sparked real-life friendship feuds. The look was unmistakable: razor-cut coiffed bangs, neon skinny jeans, rubber bracelets, and high-angle digital camera selfies.",
                "why_it_matters": "It was the first youth subculture created, nurtured, and distributed almost entirely through social networking algorithms and music embeds.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Scene (subculture) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Scene_(subculture)" }
                ]
            }
        ]
    },
    2006: {
        "felt_like": {
            "os": "Windows XP SP2 / Mac OS X 10.4 Tiger (Intel transition)",
            "browser": "Firefox 2.0 / Internet Explorer 7 (tabbed browsing!)",
            "messenger": "AIM / MSN Messenger / Windows Live Messenger",
            "social_network": "MySpace (peak year) / Facebook (opens to public) / Bebo",
            "music": "Amy Winehouse, Justin Timberlake 'FutureSex/LoveSounds', iPod Video",
            "phone": "Motorola RAZR / T-Mobile Sidekick 3 / BlackBerry Pearl",
            "video": "YouTube (acquired by Google for $1.65B) & BitTorrent",
            "website": "Glossy Web 2.0 badges, Ajax auto-complete dropdowns, RSS readers",
            "fashion": "Skinny jeans replacing bootcut, oversized sunglasses, American Apparel basics, Ray-Ban Wayfarers",
            "gadget": "Nintendo Wii & Apple MacBook (first Intel polycarbonate unibody)",
            "news": "Pluto demoted from planet status; North Korea conducts first nuclear test",
            "culture": "High School Musical phenomenon; Borat box office mockumentary hit"
        },
        "new_events": [
            {
                "id": "nintendo-wii-motion-craze-2006",
                "title": "Nintendo Wii Sports Sparks a Global Motion Control Craze",
                "year": 2006,
                "date": "2006-11-19",
                "category": ["gadget", "gaming"],
                "type": "launch",
                "summary": "Nintendo launched the Wii console, converting nursing homes, parents, and hardcore gamers into motion-swinging bowlers.",
                "narrative": "Instead of competing in the high-cost HD graphics race, Nintendo CEO Satoru Iwata bet on a clean white console with an intuitive motion-sensing remote. Bundled with 'Wii Sports', anyone could pick up the wand, swing their arm, and bowl a strike or play tennis. Sold out for months and prompting hospital reports of 'Wiiitis' and shattered TV screens from flying remotes, it sold over 101 million units.",
                "why_it_matters": "The Wii proved that accessible, intuitive physical interaction could dramatically expand the video game audience far beyond traditional gamers.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Wii - Wikipedia", "url": "https://en.wikipedia.org/wiki/Wii" }
                ]
            },
            {
                "id": "amy-winehouse-back-to-black-2006",
                "title": "Amy Winehouse Drops 'Back to Black' & Modern Soul Revives",
                "year": 2006,
                "date": "2006-10-27",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Amy Winehouse's beehive hair, winged eyeliner, and raw Motown-tinged heartbreak in 'Rehab' captivated the world.",
                "narrative": "Produced with Mark Ronson and backed by the Dap-Kings, 'Back to Black' transported 1960s girl-group harmonies into gritty 21st-century confessional songwriting. With her soaring contralto vocals, towering beehive, and jazz phrasing on 'Rehab', 'You Know I'm No Good', and 'Back to Black', Winehouse became a critical sensation, later sweeping five Grammy Awards in one night.",
                "why_it_matters": "Winehouse's breakthrough revitalized British soul, clearing a massive international runway for artists like Adele, Duffy, and Florence Welch.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Back to Black - Wikipedia", "url": "https://en.wikipedia.org/wiki/Back_to_Black" }
                ]
            },
            {
                "id": "skinny-jeans-indie-sleaze-dawn-2006",
                "title": "Skinny Jeans Conquer Bootcut & the Rise of Indie Sleaze",
                "year": 2006,
                "date": "2006-08-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Spray-on skinny jeans, American Apparel deep V-necks, and point-and-shoot flash photography took over youth fashion.",
                "narrative": "Bootcut jeans vanished from downtown sidewalks almost overnight. Inspired by British garage-rock revivalists like The Libertines and Arctic Monkeys, young people squeezed into skin-tight stretch denim. Photo blogs like The Cobrasnake documented sweaty warehouse parties filled with neon sunglasses, messy bedhead hair, and electroclash music, minting the aesthetic later known as 'indie sleaze'.",
                "why_it_matters": "Skinny jeans became the dominant pants silhouette across the globe for the next fifteen years, fundamentally reshaping denim manufacturing.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Indie sleaze - Wikipedia", "url": "https://en.wikipedia.org/wiki/Indie_sleaze" }
                ]
            }
        ]
    },
    2007: {
        "felt_like": {
            "os": "Windows Vista (Aero glass) / Mac OS X 10.5 Leopard",
            "browser": "Firefox 2 / Internet Explorer 7 / Safari on iPhone",
            "messenger": "AIM / MSN Messenger / early Twitter SMS (40404)",
            "social_network": "MySpace (losing ground) / Facebook (News Feed backlash) / Tumblr",
            "music": "iPod Classic (click wheel), Kanye West 'Graduation', Rihanna 'Umbrella'",
            "phone": "Original iPhone (2G, multi-touch, no App Store) & Nokia N95",
            "video": "YouTube / early Netflix streaming / Hulu announces",
            "website": "Gradients, bevels, shiny mirrors, Web 2.0 badges, drop shadows",
            "fashion": "American Apparel hoodies, skinny jeans, deep V-neck tees, oversized scarves, gladiator sandals",
            "gadget": "Original iPhone & Amazon Kindle E-reader",
            "news": "Subprime mortgage crisis begins; Virginia Tech tragedy",
            "culture": "Mad Men premieres; Superbad captures teen comedy; Harry Potter book 7 released"
        },
        "new_events": [
            {
                "id": "amazon-kindle-ereader-2007",
                "title": "Amazon Unveils the Kindle & Ignites E-Book Revolution",
                "year": 2007,
                "date": "2007-11-19",
                "category": ["gadget", "business"],
                "type": "launch",
                "summary": "Jeff Bezos introduced the Kindle with an electronic ink display and free built-in cellular connectivity.",
                "narrative": "With its quirky asymmetric keyboard and crisp electrophoretic E-Ink screen that read like real paper in sunlight, the first Kindle sold out in five and a half hours. Amazon's revolutionary feature was Whispernet: users could buy and download any of 90,000 books in under 60 seconds over Sprint's 3G network without connecting to a computer or paying a monthly data fee.",
                "why_it_matters": "The Kindle transformed the multi-century publishing industry, establishing e-books as a permanent format and changing how people read.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Amazon Kindle - Wikipedia", "url": "https://en.wikipedia.org/wiki/Amazon_Kindle" }
                ]
            },
            {
                "id": "rihanna-umbrella-graduation-2007",
                "title": "Rihanna's 'Umbrella' & Kanye's 'Graduation' Defeats 50 Cent",
                "year": 2007,
                "date": "2007-09-11",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Rihanna's 'Umbrella' became the song of the summer, while Kanye West outsold 50 Cent in a historic sales battle.",
                "narrative": "With its infectious 'ella, ella, eh, eh' hook and Jay-Z intro, Rihanna's 'Umbrella' sat atop the UK charts for 10 consecutive weeks amid record summer rain. Meanwhile, on September 11, Kanye West's arena-synth *Graduation* faced off against 50 Cent's *Curtis*. Kanye moved 957,000 units to 50 Cent's 691,000, formally ending street gangster rap's decade-long stranglehold on mainstream radio.",
                "why_it_matters": "The sales duel marked a permanent shift toward electronic, emotional, and introspective hip-hop, paving the way for Drake, Kid Cudi, and modern trap.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Umbrella (song) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Umbrella_(song)" },
                    { "title": "Graduation (album) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Graduation_(album)" }
                ]
            }
        ]
    },
    2008: {
        "felt_like": {
            "os": "Windows Vista Service Pack 1 / Mac OS X 10.5 Leopard",
            "browser": "Google Chrome (brand new comic book launch!) / Firefox 3",
            "messenger": "AIM / MSN / BBM (BlackBerry Messenger PIN)",
            "social_network": "Facebook (surpasses MySpace) / Twitter / Tumblr",
            "music": "Lady Gaga 'Just Dance', Katy Perry, Coldplay 'Viva La Vida', iPod Touch",
            "phone": "iPhone 3G (plastic back, App Store!) / BlackBerry Curve / T-Mobile G1",
            "video": "Hulu, YouTube 720p HD option, Netflix on Xbox 360",
            "website": "Clean typography, CSS rounded corners (-webkit-border-radius), microblogging widgets",
            "fashion": "Kanye shutter shades, keffiyeh scarves, band tees with blazers, gladiator sandals",
            "gadget": "Apple iPhone 3G (with App Store) & First Android Phone (HTC Dream)",
            "news": "Global Financial Crisis & Lehman Brothers collapse; Barack Obama elected US President",
            "culture": "The Dark Knight (Heath Ledger's Joker); Twilight vampire mania"
        },
        "new_events": [
            {
                "id": "lehman-brothers-financial-crisis-2008",
                "title": "Lehman Brothers Collapses & Great Recession Hits",
                "year": 2008,
                "date": "2008-09-15",
                "category": ["news", "business"],
                "type": "milestone",
                "summary": "The collapse of Wall Street titan Lehman Brothers triggered the worst global financial crisis since the Great Depression.",
                "narrative": "Employees carrying cardboard boxes out of Lehman's Manhattan headquarters became the iconic image of a global economic meltdown. Toxic subprime mortgage debt froze credit markets, leading to government bailouts, massive foreclosures, and skyrocketing unemployment. Out of the ashes and cynicism toward centralized banking, Satoshi Nakamoto published the Bitcoin whitepaper weeks later.",
                "why_it_matters": "The Great Recession reshaped global politics, devastated millennial career starts, and catalyzed the rise of decentralized cryptocurrencies and FinTech.",
                "impact": 5,
                "nostalgia": 2,
                "sources": [
                    { "title": "Bankruptcy of Lehman Brothers - Wikipedia", "url": "https://en.wikipedia.org/wiki/Bankruptcy_of_Lehman_Brothers" }
                ]
            },
            {
                "id": "lady-gaga-the-fame-2008",
                "title": "Lady Gaga Explodes with 'The Fame' & Revives Dance Pop",
                "year": 2008,
                "date": "2008-08-19",
                "category": ["music", "fashion"],
                "type": "cultural_shift",
                "summary": "Stefani Germanotta burst onto pop airwaves with 'Just Dance' and 'Poker Face', reviving theatrical electro-pop.",
                "narrative": "Sporting sharp blonde bangs, metallic leotards, and origami sunglasses, Lady Gaga brought downtown New York avant-garde performance art to daytime radio. 'The Fame' yielded consecutive #1 hits in 'Just Dance' and 'Poker Face', fusing European electronic synthesizers with stadium pop hooks and reigniting dance music across mainstream America.",
                "why_it_matters": "Lady Gaga redefined pop stardom for the digital era, blending theatrical haute couture fashion, viral video spectacles, and LGBTQ+ advocacy.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "The Fame - Wikipedia", "url": "https://en.wikipedia.org/wiki/The_Fame" }
                ]
            },
            {
                "id": "shutter-shades-keffiyeh-streetwear-2008",
                "title": "Kanye Shutter Shades, Keffiyeh Scarves & Indie-Hop Style",
                "year": 2008,
                "date": "2008-04-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Slotted plastic Venetian sunglasses and woven keffiyeh scarves became unavoidable youth fashion statements.",
                "narrative": "After Kanye West wore custom Alain Mikli slotted plastic 'shutter shades' in his 'Stronger' music video and Grammy performance, cheap plastic knockoffs flooded concert festivals and high school hallways. Paired with patterned keffiyeh scarves, brightly colored Nike Dunks, and graphic hoodies, this clash of hip-hop and indie aesthetics defined late-2000s streetwear.",
                "why_it_matters": "It exemplified how viral music videos could turn an impractical novelty accessory into an inescapable global micro-trend within weeks.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Shutter Shades - Wikipedia", "url": "https://en.wikipedia.org/wiki/Shutter_Shades" }
                ]
            }
        ]
    },
    2009: {
        "felt_like": {
            "os": "Windows 7 (huge relief after Vista!) / Mac OS X 10.6 Snow Leopard",
            "browser": "Firefox 3.5 / Google Chrome / Internet Explorer 8",
            "messenger": "BBM (BlackBerry PIN sharing) / Facebook Chat / WhatsApp (early)",
            "social_network": "Facebook (status updates in third person) / Twitter (hashtag boom) / Tumblr",
            "music": "The Black Eyed Peas 'I Gotta Feeling', Taylor Swift, Lady Gaga 'Bad Romance'",
            "phone": "BlackBerry Bold 9000 & iPhone 3GS ('The S stands for Speed')",
            "video": "Avatar 3D in IMAX & YouTube 1080p Full HD launch",
            "website": "Clean minimal layouts, CSS3 gradients, early HTML5 demos, social share buttons",
            "fashion": "Hipster indie sleaze at peak: galaxy leggings, deep V-necks, Toms canvas shoes, Ray-Ban clubmasters",
            "gadget": "Apple iPhone 3GS & BlackBerry Bold 9700",
            "news": "Michael Jackson's sudden death crashes web servers; Miracle on the Hudson",
            "culture": "James Cameron's Avatar shatters box office; Kanye interrupts Taylor Swift at VMAs"
        },
        "new_events": [
            {
                "id": "michael-jackson-death-internet-crash-2009",
                "title": "Michael Jackson Passes Away: The Day the Internet Froze",
                "year": 2009,
                "date": "2009-06-25",
                "category": ["news", "culture"],
                "type": "cultural_shift",
                "summary": "The sudden death of the King of Pop caused unprecedented web traffic surges that crashed AIM, Twitter, and Wikipedia.",
                "narrative": "When TMZ broke the news that Michael Jackson had suffered cardiac arrest at his Los Angeles home, the collective global rush for verification nearly buckled the internet. AOL Instant Messenger collapsed for 40 minutes. Twitter saw its tweet volume double in seconds and disabled features to stay online. Google believed it was under a massive coordinated DDoS attack after millions searched his name simultaneously.",
                "why_it_matters": "It demonstrated the sheer scale of the global internet population relying on digital networks for communal grieving and breaking news.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Death of Michael Jackson - Wikipedia", "url": "https://en.wikipedia.org/wiki/Death_of_Michael_Jackson" }
                ]
            },
            {
                "id": "kanye-taylor-vma-interruption-2009",
                "title": "Kanye Interrupts Taylor Swift: 'Imma Let You Finish'",
                "year": 2009,
                "date": "2009-09-13",
                "category": ["culture", "viral-culture"],
                "type": "cultural_shift",
                "summary": "Kanye West walked onstage at the MTV VMAs and took the microphone from 19-year-old Taylor Swift.",
                "narrative": "When Taylor Swift won Best Female Video for 'You Belong with Me', Kanye West jumped onstage with a bottle of Hennessy, grabbed the microphone, and uttered the immortal line: 'Yo Taylor, I'm really happy for you, Imma let you finish, but Beyoncé had one of the best videos of all time!' The internet erupted into an avalanche of memes, launching a feud that reverberated through pop culture for over a decade.",
                "why_it_matters": "The interruption birthed one of the most prolific and enduring meme formats in internet history and permanently altered the public personas of both megastars.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "2009 MTV Video Music Awards - Wikipedia", "url": "https://en.wikipedia.org/wiki/2009_MTV_Video_Music_Awards" }
                ]
            },
            {
                "id": "avatar-3d-cinema-revolution-2009",
                "title": "James Cameron's 'Avatar' Breaks Records & Sparks 3D Craze",
                "year": 2009,
                "date": "2009-12-18",
                "category": ["culture", "tech"],
                "type": "cultural_shift",
                "summary": "James Cameron returned with a motion-captured photorealistic 3D sci-fi spectacle, becoming the highest-grossing film in history.",
                "narrative": "Transporting audiences to the bioluminescent moon of Pandora, Cameron utilized groundbreaking stereoscopic digital cameras and performance-capture rigs to make CGI characters feel palpably real. The film grossed an astounding $2.9 billion, triggering a multi-year craze where electronics makers scrambled to put 3D glasses and 3D displays into every living room television.",
                "why_it_matters": "Avatar represented a massive technological leap in stereoscopic digital cinematography and visual effects worldbuilding.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Avatar (2009 film) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Avatar_(2009_film)" }
                ]
            }
        ]
    }
}

def apply_era2():
    for year, data in ERA2_UPDATES.items():
        year_path = f"src/data/years/{year}.json"
        with open(year_path, "r") as f:
            ydata = json.load(f)
        
        ydata["felt_like"] = data["felt_like"]
        
        events_path = f"src/data/events/{year}.json"
        with open(events_path, "r") as f:
            events = json.load(f)
            
        # If in 2007, clean up the misattributed "Imma Let You Finish" (which happened in 2009)
        if year == 2007:
            events = [e for e in events if "finish" not in e.get("id", "").lower() and "finish" not in e.get("title", "").lower()]
            
        existing_ids = set(e["id"] for e in events)
        for ne in data["new_events"]:
            if ne["id"] not in existing_ids:
                events.append(ne)
                existing_ids.add(ne["id"])
                
        ydata["events"] = [e["id"] for e in events]
        
        with open(year_path, "w") as f:
            json.dump(ydata, f, indent=2)
            f.write("\n")
            
        with open(events_path, "w") as f:
            json.dump(events, f, indent=2)
            f.write("\n")
            
        print(f"Enriched {year}: {len(events)} events, 12 felt_like keys.")

if __name__ == "__main__":
    apply_era2()
