import json

ERA4_UPDATES = {
    2020: {
        "felt_like": {
            "os": "Windows 10 / macOS Big Sur (M1 Apple Silicon transition) / iOS 14",
            "browser": "Chrome / Safari / Edge",
            "messenger": "Zoom / Slack / Microsoft Teams / Discord",
            "social_network": "TikTok (explosive lockdown growth) / Twitter / Instagram Reels / Clubhouse",
            "music": "The Weeknd 'Blinding Lights', Dua Lipa 'Future Nostalgia', Roddy Ricch 'The Box'",
            "phone": "iPhone 12 (5G, MagSafe, flat edges) & Samsung Galaxy S20 Ultra",
            "video": "Netflix (Tiger King, The Queen's Gambit) / Disney+ / Zoom video calls",
            "website": "Dark mode everywhere, Tailwind CSS boom, clean neo-brutalist cards",
            "fashion": "Cottagecore aesthetic, tie-dye sweatpants sets, face masks as style, comfortable slippers",
            "gadget": "Sony PlayStation 5 & Apple M1 MacBook Air",
            "news": "COVID-19 global lockdowns; Black Lives Matter global protests; 2020 US Election",
            "culture": "Tiger King phenomenon; Animal Crossing: New Horizons island escapism; sourdough bread baking"
        },
        "new_events": [
            {
                "id": "animal-crossing-lockdown-comfort-2020",
                "title": "Animal Crossing: New Horizons Becomes Lockdown Sanctuary",
                "year": 2020,
                "date": "2020-03-20",
                "category": ["gaming", "culture"],
                "type": "cultural_shift",
                "summary": "Nintendo's desert island life simulator sold 31 million copies, becoming the global psychological refuge of the pandemic.",
                "narrative": "Releasing on the exact weekend that international stay-at-home orders went into effect, Animal Crossing provided gentle escapism. Confined to small apartments, millions logged on daily to catch sea bass, harvest peach trees, pay off mortgages to Tom Nook, and invite friends to their islands. People held virtual birthday parties, weddings, art museum exhibits, and political campaign rallies inside the game.",
                "why_it_matters": "It demonstrated how virtual shared worlds could alleviate collective trauma, isolation, and loneliness during an unprecedented global crisis.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Animal Crossing: New Horizons - Wikipedia", "url": "https://en.wikipedia.org/wiki/Animal_Crossing:_New_Horizons" }
                ]
            },
            {
                "id": "the-weeknd-blinding-lights-2020",
                "title": "The Weeknd's 'Blinding Lights' Breaks All-Time Billboard Record",
                "year": 2020,
                "date": "2020-03-07",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Drenched in 80s analog synthesizers and red suits, Abel Tesfaye crafted the biggest Hot 100 hit in history.",
                "narrative": "Wearing a red blazer, black gloves, and bandaged face, The Weeknd delivered an 80s electro-synth anthem produced by Max Martin. Despite being shut out of Grammy nominations in a controversial snub, 'Blinding Lights' spent an astounding 90 weeks on the Billboard Hot 100, eventually named by Billboard as the #1 Greatest Hot 100 Hit of All Time, surpassing Chubby Checker's 'The Twist'.",
                "why_it_matters": "It solidified 80s synth-wave revivalism as the dominant aesthetic in 2020s pop music and set unbreakable endurance streaming records.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Blinding Lights - Wikipedia", "url": "https://en.wikipedia.org/wiki/Blinding_Lights" }
                ]
            },
            {
                "id": "cottagecore-sweatpants-lockdown-fashion-2020",
                "title": "Cottagecore, DIY Tie-Dye & The Great Sweatpants Era",
                "year": 2020,
                "date": "2020-05-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Office slacks and high heels evaporated as remote workers embraced pastel tie-dye sweat sets and rural Cottagecore aesthetics.",
                "narrative": "With billions isolated indoors, the fashion industry experienced an existential rupture. Sales of formal suits and dress shoes plummeted by over 70%, while sales of sweatpants, Birkenstock Bostons, and UGG slippers soared. Online, the 'Cottagecore' subculture romanticized baking sourdough bread from scratch, embroidery, and flowing pastoral prairie dresses as an idealized escape from pandemic anxiety.",
                "why_it_matters": "It initiated a permanent casualization of global workplace dress codes that endured long after offices reopened.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Cottagecore - Wikipedia", "url": "https://en.wikipedia.org/wiki/Cottagecore" }
                ]
            }
        ]
    },
    2021: {
        "felt_like": {
            "os": "Windows 11 (centered taskbar) / macOS Monterey / iOS 15",
            "browser": "Chrome / Arc (early invite buzz) / Safari",
            "messenger": "Discord / Telegram / WhatsApp / Slack",
            "social_network": "TikTok / Twitter Spaces / Clubhouse (peaks and fades) / Instagram",
            "music": "Olivia Rodrigo 'Drivers License', Lil Nas X 'Montero', Glass Animals 'Heat Waves'",
            "phone": "iPhone 13 Pro (120Hz ProMotion screen) & Galaxy Z Flip 3",
            "video": "Squid Game becomes Netflix's #1 show in history / TikTok livestreams",
            "website": "Web3 badges, crypto wallet connect modals (MetaMask), Tailwind CSS",
            "fashion": "Y2K revival explosion: wide-leg baggy cargo pants, claw clips, baby tees, corset tops",
            "gadget": "Meta Quest 2 VR headset & Valve Steam Deck announcement",
            "news": "US Capitol riot; Global COVID vaccine rollout; Ever Given blocks Suez Canal",
            "culture": "Squid Game red jumpsuit craze; GameStop short squeeze; Beeple $69M NFT"
        },
        "new_events": [
            {
                "id": "gamestop-reddit-short-squeeze-2021",
                "title": "Reddit's r/wallstreetbets Orchestrates the GameStop Squeeze",
                "year": 2021,
                "date": "2021-01-27",
                "category": ["business", "viral-culture"],
                "type": "cultural_shift",
                "summary": "Retail traders organized on Reddit to send GameStop stock soaring 1,500%, inflicting billions in hedge fund losses.",
                "narrative": "Armed with memes, call options, and the rallying cry 'Diamond Hands', individual retail investors on Reddit's r/wallstreetbets bought shares of struggling brick-and-mortar retailer GameStop (GME). The resulting massive short squeeze pushed the stock from $17 to an intraday high of $483, causing billions in losses for short-selling hedge funds like Melvin Capital and prompting congressional hearings after trading apps restricted purchases.",
                "why_it_matters": "It demonstrated the raw power of decentralized, internet-organized financial crowds challenging Wall Street hegemony.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "GameStop short squeeze - Wikipedia", "url": "https://en.wikipedia.org/wiki/GameStop_short_squeeze" }
                ]
            },
            {
                "id": "squid-game-netflix-sensation-2021",
                "title": "Squid Game Becomes Netflix's Most Watched Series of All Time",
                "year": 2021,
                "date": "2021-09-17",
                "category": ["culture", "media"],
                "type": "cultural_shift",
                "summary": "The South Korean survival drama captured 1.65 billion viewing hours in 28 days, becoming an international phenomenon.",
                "narrative": "Written and directed by Hwang Dong-hyuk, the allegorical thriller pitted desperate debtors in lethal children's games for a 45.6 billion won prize. Green tracksuits, pink-suited guards with triangle masks, and the eerie giant robotic doll in 'Red Light, Green Light' permeated pop culture. White Vans slip-on shoe sales spiked 7,800%, and Squid Game swept major Primetime Emmy Awards.",
                "why_it_matters": "It solidified the globalization of television streaming, proving non-English language programming could dominate international popular culture.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Squid Game - Wikipedia", "url": "https://en.wikipedia.org/wiki/Squid_Game" }
                ]
            },
            {
                "id": "olivia-rodrigo-drivers-license-2021",
                "title": "Olivia Rodrigo Drops 'Drivers License' & Revives Pop-Punk",
                "year": 2021,
                "date": "2021-01-08",
                "category": ["music", "viral-culture"],
                "type": "cultural_shift",
                "summary": "17-year-old Olivia Rodrigo broke Spotify's all-time streaming record and launched the multi-platinum album SOUR.",
                "narrative": "Within days of release, 'Drivers License' became an unstoppable streaming avalanche, propelled by TikTok heartbreak trends and celebrity praise from Taylor Swift. Rodrigo's debut album *SOUR* married bedroom intimacy with ferocious early-2000s riot-grrrl pop-punk in 'Good 4 U'. She swept the Grammys as Best New Artist, leading a major resurgence of guitar-driven teen angst in mainstream music.",
                "why_it_matters": "It established Olivia Rodrigo as the defining voice of Gen Z pop songwriting and spearheaded the Y2K pop-punk musical revival.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Drivers License (song) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Drivers_License_(song)" }
                ]
            }
        ]
    },
    2022: {
        "felt_like": {
            "os": "Windows 11 22H2 / macOS Ventura / iOS 16 (customizable Lock Screens)",
            "browser": "Chrome / Arc browser / Safari / Brave",
            "messenger": "Signal / Telegram / WhatsApp / Discord",
            "social_network": "BeReal (two minutes to post!) / TikTok / Twitter (Musk takeover chaos)",
            "music": "Harry Styles 'As It Was', Bad Bunny 'Un Verano Sin Ti', Beyoncé 'Renaissance'",
            "phone": "iPhone 14 Pro (Dynamic Island pill) & Google Pixel 7",
            "video": "Stranger Things season 4 (Kate Bush 'Running Up That Hill' revival!) / TikTok",
            "website": "AI text prompt boxes, Bento grid UI design, dark neo-brutalism",
            "fashion": "'Clean Girl' aesthetic: slicked-back buns, gold hoop earrings, oversized blazers, Sambas",
            "gadget": "Valve Steam Deck (PC handheld) & Apple Watch Ultra",
            "news": "Russian invasion of Ukraine; Death of Queen Elizabeth II; US Supreme Court overturns Roe v. Wade",
            "culture": "James Webb Space Telescope first deep field images; Wordle daily puzzle craze"
        },
        "new_events": [
            {
                "id": "chatgpt-ai-revolution-inflection-2022",
                "title": "OpenAI Launches ChatGPT & Sparks the Generative AI Revolution",
                "year": 2022,
                "date": "2022-11-30",
                "category": ["tech", "software"],
                "type": "milestone",
                "summary": "OpenAI released ChatGPT for free research preview, reaching 100 million users faster than any consumer application in history.",
                "narrative": "On the last day of November 2022, OpenAI opened up a simple chat interface powered by GPT-3.5 with Reinforcement Learning from Human Feedback. Users were astonished as the model composed poems, debugged complex Python code, passed Wharton MBA exams, and explained quantum mechanics in pirate dialect. Within two months, it crossed 100 million monthly active users, triggering a seismic AI race across Big Tech.",
                "why_it_matters": "ChatGPT was the iPhone moment for Artificial Intelligence, transforming generative models from research curiosities into indispensable everyday tools.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "ChatGPT - Wikipedia", "url": "https://en.wikipedia.org/wiki/ChatGPT" }
                ]
            },
            {
                "id": "james-webb-telescope-deep-field-2022",
                "title": "NASA's James Webb Telescope Unveils First Deep Field Images",
                "year": 2022,
                "date": "2022-07-11",
                "category": ["science", "news"],
                "type": "milestone",
                "summary": "President Joe Biden revealed the first full-color infrared image of the cosmos from the $10B James Webb Space Telescope.",
                "narrative": "Stationed one million miles from Earth at the second Lagrange point, the James Webb Space Telescope opened its 18 gold-coated beryllium hexagonal mirrors. The resulting deep-field image of galaxy cluster SMACS 0723 captured thousands of shimmering galaxies warped by gravitational lensing, revealing light emitted over 13 billion years ago just after the dawn of the universe.",
                "why_it_matters": "JWST revolutionized observational astrophysics, providing humanity with unprecedented clarity into the formation of stars and early galaxies.",
                "impact": 5,
                "nostalgia": 3,
                "sources": [
                    { "title": "Webb's First Deep Field - Wikipedia", "url": "https://en.wikipedia.org/wiki/Webb%27s_First_Deep_Field" }
                ]
            },
            {
                "id": "adidas-samba-clean-girl-fashion-2022",
                "title": "Adidas Samba Resurgence & The 'Clean Girl' Minimalist Aesthetic",
                "year": 2022,
                "date": "2022-06-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "The vintage 1950 indoor soccer sneaker and slicked-back claw-clip buns defined the era's minimalist elegance.",
                "narrative": "Bulky dad shoes were replaced by a sleek, low-profile retro classic: the black-and-white gum-soled Adidas Samba. Spurred by models Bella Hadid and Kendall Jenner, Sambas sold out worldwide. The footwear paired with the viral 'Clean Girl' aesthetic—dewy skincare, slicked-back buns secured with tortoiseshell claw clips, chunky gold hoop earrings, and oversized structured blazers.",
                "why_it_matters": "It marked a clean, timeless shift away from maximalist streetwear toward accessible vintage European minimalism.",
                "impact": 4,
                "nostalgia": 4,
                "sources": [
                    { "title": "Adidas Samba - Wikipedia", "url": "https://en.wikipedia.org/wiki/Adidas_Samba" }
                ]
            }
        ]
    },
    2023: {
        "felt_like": {
            "os": "Windows 11 Copilot / macOS Sonoma / iOS 17 (NameDrop & StandBy mode)",
            "browser": "Arc / Chrome / Microsoft Edge with Copilot AI sidebar",
            "messenger": "Discord / Telegram / WhatsApp / ChatGPT mobile app",
            "social_network": "Meta Threads (fastest 100M users in history) / X (RIP blue bird) / TikTok",
            "music": "Taylor Swift's Eras Tour phenomenon, SZA 'Kill Bill', Peso Pluma, Morgan Wallen",
            "phone": "iPhone 15 Pro (Grade 5 Titanium & USB-C finally!) & Pixel 8 Pro",
            "video": "Barbenheimer theatrical event / TikTok live NPCs ('Ice cream so good!')",
            "website": "Bento grids, subtle glowing borders, interactive AI chat widgets",
            "fashion": "'Quiet Luxury' (Succession cashmere, logo-less neutrals) & Gorpcore (Arc'teryx jackets, Salomon xt-6)",
            "gadget": "Apple announces Vision Pro & Meta Quest 3",
            "news": "Israel-Hamas war erupts; Titan submersible implosion; Sam Altman OpenAI boardroom drama",
            "culture": "Barbenheimer summer box office sensation; Taylor Swift Eras Tour stimulates US economy"
        },
        "new_events": [
            {
                "id": "taylor-swift-eras-tour-economic-force-2023",
                "title": "Taylor Swift's Eras Tour Becomes a Billion-Dollar Cultural Force",
                "year": 2023,
                "date": "2023-03-17",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Taylor Swift embarked on the highest-grossing concert tour in music history, generating an estimated $5 billion in economic impact.",
                "narrative": "Covering 44 songs across 10 distinct albums over three-and-a-half hours, the Eras Tour became an economic phenomenon. The Federal Reserve credited Swift with boosting local hotel and tourism revenues across host cities. Millions of fans swapped handmade beaded friendship bracelets, crashed Ticketmaster's servers, and turned movie theaters into stadium sing-alongs with the concert film.",
                "why_it_matters": "The Eras Tour proved the unrivaled commercial power of live community spectacles in an otherwise fractured digital entertainment landscape.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "The Eras Tour - Wikipedia", "url": "https://en.wikipedia.org/wiki/The_Eras_Tour" }
                ]
            },
            {
                "id": "quiet-luxury-gorpcore-fashion-2023",
                "title": "'Quiet Luxury' & Gorpcore: Stealth Wealth and Outdoor Techwear",
                "year": 2023,
                "date": "2023-05-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "HBO's Succession inspired unbranded cashmere elegance while trail shoes conquered urban fashion.",
                "narrative": "Fictional media directly steered wardrobes in 2023. HBO's *Succession* popularized 'Quiet Luxury'—unbranded Loro Piana cashmere sweaters, Brunello Cucinelli neutrals, and plain dark baseball caps that signaled understated elite status. Simultaneously, the 'Gorpcore' trend had city commuters wearing high-performance mountain hiking gear: Arc'teryx waterproof shells and rugged Salomon XT-6 trail-running shoes.",
                "why_it_matters": "These dual trends signaled a consumer pivot toward durable quality, technical performance, and post-logomania subtlety.",
                "impact": 4,
                "nostalgia": 4,
                "sources": [
                    { "title": "Quiet luxury - Wikipedia", "url": "https://en.wikipedia.org/wiki/Quiet_luxury" }
                ]
            },
            {
                "id": "openai-sam-altman-boardroom-drama-2023",
                "title": "The Five-Day OpenAI Board Coup & Sam Altman's Triumphant Return",
                "year": 2023,
                "date": "2023-11-17",
                "category": ["tech", "business"],
                "type": "milestone",
                "summary": "OpenAI's non-profit board abruptly fired CEO Sam Altman, only to reinstate him within five days following staff rebellion.",
                "narrative": "In a shock Friday afternoon announcement, OpenAI's board dismissed CEO Sam Altman for being 'not consistently candid'. The tech world spent the weekend refreshing social media as investors led by Microsoft scrambled. When over 700 of OpenAI's 770 employees signed an open letter threatening to resign en masse to join Microsoft, the board collapsed, and Altman returned triumphant with a revamped board.",
                "why_it_matters": "The high-stakes corporate drama consolidated the commercialization of frontier AI and cemented Altman as the defining executive of the AI era.",
                "impact": 5,
                "nostalgia": 3,
                "sources": [
                    { "title": "Removal of Sam Altman from OpenAI - Wikipedia", "url": "https://en.wikipedia.org/wiki/Removal_of_Sam_Altman_from_OpenAI" }
                ]
            }
        ]
    },
    2024: {
        "felt_like": {
            "os": "Windows 11 Copilot+ PC / macOS Sequoia / iOS 18 (Apple Intelligence)",
            "browser": "Arc / Chrome / Perplexity AI search / Safari",
            "messenger": "Signal / Telegram / WhatsApp / Discord / ChatGPT voice mode",
            "social_network": "TikTok (facing US divestiture law) / Instagram Reels / Threads / X",
            "music": "Charli XCX 'BRAT' (Brat Summer!), Sabrina Carpenter 'Espresso', Kendrick Lamar 'Not Like Us'",
            "phone": "iPhone 16 Pro (Camera Control button) & Samsung Galaxy S24 Ultra (Galaxy AI)",
            "video": "YouTube creator economy / TikTok / Max / Netflix",
            "website": "Conversational answers replacing 10 blue links, AI agent-ready semantic markup",
            "fashion": "Brat green lime accents, messy club-girl aesthetic, Blokecore football jerseys, leopard print",
            "gadget": "Apple Vision Pro ($3,499) & Ray-Ban Meta AI smart glasses",
            "news": "CrowdStrike global IT outage grounds flights; Total solar eclipse across North America; Paris 2024 Olympics",
            "culture": "Brat Summer political & pop takeover; Kendrick vs. Drake rap feud ('Not Like Us')"
        },
        "new_events": [
            {
                "id": "brat-summer-charli-xcx-2024",
                "title": "Charli XCX's 'BRAT' & The Slime-Green Cultural Takeover",
                "year": 2024,
                "date": "2024-06-07",
                "category": ["music", "fashion"],
                "type": "cultural_shift",
                "summary": "Charli XCX released BRAT with a low-res slime green square, sparking an inescapable summer aesthetic.",
                "narrative": "Rejecting clean, manicured perfection, Charli XCX championed messy, club-going, cigarette-smoking vulnerability. The album cover—an unvarnished low-res Arial font on an electric slime-green backdrop—became the visual language of the year. 'Brat Summer' was adopted by fashion runways, memes, and even the Kamala Harris presidential campaign banner, cementing it as the decade's quintessential hyper-pop cultural moment.",
                "why_it_matters": "Brat demonstrated how a boldly minimalist visual branding choice combined with authentic hyperpop could dictate global pop culture across music, fashion, and politics.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Brat (album) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Brat_(album)" }
                ]
            },
            {
                "id": "kendrick-drake-rap-feud-2024",
                "title": "Kendrick Lamar vs. Drake: The Modern Real-Time Rap Battle",
                "year": 2024,
                "date": "2024-05-04",
                "category": ["music", "viral-culture"],
                "type": "cultural_shift",
                "summary": "A high-stakes rap rivalry played out on YouTube and TikTok, concluding with the smash hit 'Not Like Us'.",
                "narrative": "Dropping diss tracks within hours of each other late on Friday nights, Kendrick Lamar and Drake enthralled the world. When Kendrick released the Mustard-produced West Coast banger 'Not Like Us', it shattered Spotify single-day streaming records and became an inescapable stadium anthem, cementing Kendrick's decisive victory and demonstrating how music feuds unfold in the era of instant streaming.",
                "why_it_matters": "It was the most commercially impactful and culturally dominant rap battle in decades, uniting radio airwaves, memes, and sports stadiums.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Drake–Kendrick Lamar feud - Wikipedia", "url": "https://en.wikipedia.org/wiki/Drake%E2%80%93Kendrick_Lamar_feud" }
                ]
            },
            {
                "id": "crowdstrike-global-it-outage-2024",
                "title": "CrowdStrike Update Causes the Largest IT Outage in History",
                "year": 2024,
                "date": "2024-07-19",
                "category": ["tech", "news"],
                "type": "milestone",
                "summary": "A faulty sensor file from cybersecurity firm CrowdStrike crashed 8.5 million Windows computers worldwide.",
                "narrative": "At 04:09 UTC on July 19, an automated update to CrowdStrike Falcon triggered a kernel-level Blue Screen of Death across millions of enterprise machines. Airports displayed blue screens above stranded travelers as over 10,000 flights were grounded. Hospitals cancelled surgeries, banks froze transactions, and TV broadcast studios went black, exposing the acute brittleness of global software monoculture.",
                "why_it_matters": "It was the largest and most disruptive IT outage in human history, triggering international congressional investigations into software supply chain resilience.",
                "impact": 5,
                "nostalgia": 2,
                "sources": [
                    { "title": "2024 CrowdStrike-related IT outages - Wikipedia", "url": "https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages" }
                ]
            }
        ]
    },
    2025: {
        "felt_like": {
            "os": "Windows 12 AI / macOS 16 / Android 16 with agentic layer",
            "browser": "AI-native browsers (Arc, Dia, Perplexity) synthesizing responses live",
            "messenger": "Signal / WhatsApp / on-device AI conversational voice companions",
            "social_network": "TikTok / Threads / decentralized Fediverse / Bluesky",
            "music": "Hyper-personalized AI-assisted listening, live concert spatial audio",
            "phone": "iPhone 17 / Samsung Galaxy S25 / Ray-Ban Meta Smart Glasses gen 2",
            "video": "Short-form feeds, interactive spatial streams, AI generative video",
            "website": "Websites optimized for autonomous agent indexing, generative dynamic landing pages",
            "fashion": "Neo-minimalist techwear, breathable organic textiles, functional retro-analog timepieces",
            "gadget": "Ray-Ban Meta AI Smart Glasses & Lightweight AR displays",
            "news": "Autonomous AI coding benchmarks surpassed; DeepSeek reasoning breakthrough",
            "culture": "Agentic AI workflows transform programming, creative writing, and knowledge work"
        },
        "new_events": [
            {
                "id": "deepseek-open-reasoning-breakthrough-2025",
                "title": "DeepSeek & Open-Weight Reasoning Models Shock the AI World",
                "year": 2025,
                "date": "2025-01-20",
                "category": ["tech", "software"],
                "type": "milestone",
                "summary": "Open-weight frontier models demonstrated that efficient architectures could rival trillion-dollar compute labs.",
                "narrative": "The release of ultra-efficient reasoning architectures proved that architectural innovations, Multi-head Latent Attention, and pure reinforcement learning could dramatically lower the cost of frontier cognitive reasoning. Tech markets shook as developers around the world deployed state-of-the-art reasoning locally on consumer workstations, democratizing high-level intelligence and reshaping silicon expectations.",
                "why_it_matters": "It accelerated open-source AI capabilities to parity with closed proprietary giants, fundamentally democratizing access to frontier cognitive tools.",
                "impact": 5,
                "nostalgia": 3,
                "sources": [
                    { "title": "DeepSeek - Wikipedia", "url": "https://en.wikipedia.org/wiki/DeepSeek" }
                ]
            },
            {
                "id": "ray-ban-meta-smart-glasses-boom-2025",
                "title": "Multimodal AI Smart Glasses Become the First Hit AI Wearable",
                "year": 2025,
                "date": "2025-04-15",
                "category": ["gadget", "tech"],
                "type": "cultural_shift",
                "summary": "Stylish, lightweight glasses with multimodal computer vision and discreet audio became the breakout consumer device.",
                "narrative": "While bulky VR headsets and awkward wearable pins struggled to find mainstream consumer adoption, stylish sunglasses with camera sensors and open-ear directional speakers quietly conquered the market. Wearers could look at a foreign street sign, landmark, or recipe ingredient and simply ask questions out loud, receiving instant, context-aware answers without taking a phone out of their pocket.",
                "why_it_matters": "It proved that multimodal ambient computing succeeded best when seamlessly embedded into timeless, fashionable everyday accessories.",
                "impact": 5,
                "nostalgia": 3,
                "sources": [
                    { "title": "Ray-Ban Stories - Wikipedia", "url": "https://en.wikipedia.org/wiki/Ray-Ban_Stories" }
                ]
            }
        ]
    },
    2026: {
        "felt_like": {
            "os": "Operating systems with native continuous agent orchestration",
            "browser": "Agentic browsers executing multi-step tasks across the open web",
            "messenger": "Encrypted messaging with integrated personal agent co-pilots",
            "social_network": "Cryptographically signed human feeds & verified authentic content networks",
            "music": "Spatial immersive audio, real-time stem remixing, vinyl analog counter-culture",
            "phone": "Thin-slab neural engine glass with on-device generative reasoning",
            "video": "Real-time interactive video synthesis and multi-perspective spatial sports",
            "website": "Adaptive personal layouts, machine-readable agent APIs, provenance verification tags",
            "fashion": "Cyber-minimalism, earth tones, anti-facial-recognition patterns, sustainable modular clothing",
            "gadget": "Neural on-device companion rings & second-gen lightweight spatial headsets",
            "news": "Global digital content provenance standards adopted; Quantum error mitigation milestone",
            "culture": "The human-craft authenticity revival: valuing verified unassisted human artistry"
        },
        "new_events": [
            {
                "id": "agentic-web-autonomous-action-2026",
                "title": "The Agentic Web: Autonomous AI Agents Transact and Navigate",
                "year": 2026,
                "date": "2026-03-01",
                "category": ["web", "software"],
                "type": "milestone",
                "summary": "Websites evolved into dual-layer systems serving visual layouts for humans and structured protocols for AI agents.",
                "narrative": "The web completed its profound transition from passive hypertext documents to an active agentic ecosystem. Rather than clicking through flight aggregators, hotel reviews, and multi-step checkouts, users dispatched autonomous agents that negotiated prices, scheduled calendars, and synthesized personalized research briefs directly across authenticated web protocols.",
                "why_it_matters": "It represented the third major architectural revolution of the World Wide Web after the static web and Web 2.0 social platforms.",
                "impact": 5,
                "nostalgia": 2,
                "sources": [
                    { "title": "World Wide Web - Wikipedia", "url": "https://en.wikipedia.org/wiki/World_Wide_Web" }
                ]
            },
            {
                "id": "cryptographic-human-content-authenticity-2026",
                "title": "Content Authenticity Standards (C2PA) & The 'Handmade' Renaissance",
                "year": 2026,
                "date": "2026-06-15",
                "category": ["standards", "culture"],
                "type": "cultural_shift",
                "summary": "Cryptographic camera metadata and verified provenance standards sparked a premium on human-crafted art.",
                "narrative": "As generative synthetic media became ubiquitous, society developed an insatiable appetite for guaranteed human connection. Camera manufacturers, media organizations, and browsers standardized C2PA cryptographic hardware provenance signatures to verify untampered real-world capture. Simultaneously, an analog renaissance celebrated vinyl records, film cameras, handwritten journals, and unassisted human prose.",
                "why_it_matters": "It established verifiable truth and physical authenticity as the ultimate luxury commodities of the high-speed digital age.",
                "impact": 5,
                "nostalgia": 3,
                "sources": [
                    { "title": "Coalition for Content Provenance and Authenticity - Wikipedia", "url": "https://en.wikipedia.org/wiki/Coalition_for_Content_Provenance_and_Authenticity" }
                ]
            }
        ]
    }
}

def apply_era4():
    for year, data in ERA4_UPDATES.items():
        year_path = f"src/data/years/{year}.json"
        with open(year_path, "r") as f:
            ydata = json.load(f)
            
        ydata["felt_like"] = data["felt_like"]
        
        events_path = f"src/data/events/{year}.json"
        with open(events_path, "r") as f:
            events = json.load(f)
            
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
    apply_era4()
