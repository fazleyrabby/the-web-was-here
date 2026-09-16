import json

ERA3_UPDATES = {
    2010: {
        "felt_like": {
            "os": "Windows 7 / Mac OS X 10.6 Snow Leopard / iOS 4",
            "browser": "Google Chrome / Safari / Firefox 3.6",
            "messenger": "WhatsApp (early) / BBM / Facebook Chat",
            "social_network": "Facebook (surpasses 500M) / Twitter / Tumblr / early Instagram",
            "music": "Katy Perry 'Teenage Dream', Kesha 'TiK ToK', Eminem 'Recovery'",
            "phone": "iPhone 4 (Retina Display, glass back) & HTC Evo 4G",
            "video": "YouTube 1080p, Netflix streaming on PS3 & Wii",
            "website": "Responsive web design, CSS3 animations, flat UI beginnings",
            "fashion": "Hipster mustache motifs, peplum tops, statement necklaces, Toms shoes, colored skinny jeans",
            "gadget": "Apple iPad (original) & iPhone 4",
            "news": "Deepwater Horizon oil spill; Haiti earthquake; WikiLeaks Afghan war logs",
            "culture": "The Social Network movie; Inception spinning top debate; One Direction forms"
        },
        "new_events": [
            {
                "id": "ipad-original-launch-2010",
                "title": "Steve Jobs Unveils the Original Apple iPad",
                "year": 2010,
                "date": "2010-01-27",
                "category": ["gadget", "design"],
                "type": "launch",
                "summary": "Steve Jobs introduced the 9.7-inch iPad, selling 300,000 units on day one and launching the modern tablet era.",
                "narrative": "Sitting comfortably on stage in a black turtleneck and jeans on a classic leather armchair, Steve Jobs demonstrated browsing the web, flipping through photo albums, and reading The New York Times on a thin 9.7-inch glass slab. While cynics initially dismissed it as 'just a giant iPod touch', consumers fell in love with lean-back couch computing, buying 15 million iPads in its first nine months.",
                "why_it_matters": "The iPad created the modern consumer tablet category, transforming reading, education, airplane entertainment, and retail point-of-sale systems.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "iPad (1st generation) - Wikipedia", "url": "https://en.wikipedia.org/wiki/IPad_(1st_generation)" }
                ]
            },
            {
                "id": "deepwater-horizon-haiti-2010",
                "title": "Deepwater Horizon Disaster & Haiti Earthquake SMS Relief",
                "year": 2010,
                "date": "2010-04-20",
                "category": ["news", "history"],
                "type": "milestone",
                "summary": "Millions watched the underwater oil spill livestream, while the Haiti earthquake mobilized $30M in $10 text donations.",
                "narrative": "On April 20, the Deepwater Horizon offshore drilling rig exploded in the Gulf of Mexico, killing 11 workers and discharging nearly five million barrels of oil. A continuous underwater 'Spillcam' video feed transfixed viewers around the world. Earlier in January, when a catastrophic earthquake devastated Haiti, the Red Cross raised over $30 million by allowing mobile users to simply text 'HAITI' to 90999.",
                "why_it_matters": "It demonstrated how live streaming video brought ecological disasters directly to screens, and proved mobile micro-donations could rapidly organize disaster relief.",
                "impact": 5,
                "nostalgia": 2,
                "sources": [
                    { "title": "Deepwater Horizon oil spill - Wikipedia", "url": "https://en.wikipedia.org/wiki/Deepwater_Horizon_oil_spill" }
                ]
            },
            {
                "id": "katy-perry-teenage-dream-2010",
                "title": "Katy Perry's 'Teenage Dream' Ties Michael Jackson Record",
                "year": 2010,
                "date": "2010-08-24",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Katy Perry produced five Billboard #1 singles from one album, tying Michael Jackson's Bad.",
                "narrative": "Coated in whipped cream, candy landscapes, and sun-soaked California nostalgia, Katy Perry's 'Teenage Dream' was a pop juggernaut. Produced by Max Martin and Dr. Luke, 'California Gurls', 'Teenage Dream', 'Firework', 'E.T.', and 'Last Friday Night' all hit number one on the Billboard Hot 100, matching a chart record previously held only by Michael Jackson's 1987 album *Bad*.",
                "why_it_matters": "It was the commercial high-water mark of early 2010s radio pop perfection before streaming fractured the universal monoculture.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Teenage Dream (Katy Perry album) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Teenage_Dream_(Katy_Perry_album)" }
                ]
            }
        ]
    },
    2011: {
        "felt_like": {
            "os": "Windows 7 / OS X Lion / iOS 5 (iMessage & Siri!)",
            "browser": "Chrome (fastest browser on earth) / Firefox 4",
            "messenger": "iMessage (blue vs green bubbles born!) / WhatsApp / BBM",
            "social_network": "Instagram (photo filters: Kelvin, Toaster, Earlybird) / Twitter / Google+",
            "music": "Adele '21' ('Rolling in the Deep'), LMFAO 'Party Rock Anthem', Spotify US",
            "phone": "iPhone 4S (with Siri) & Samsung Galaxy S II",
            "video": "Netflix streaming taking over, YouTube viral sensations",
            "website": "Infinite scroll, CSS3 transitions, Google web fonts",
            "fashion": "Color blocking, high-waisted denim shorts, Jeffrey Campbell Lita boots, sheer maxi skirts",
            "gadget": "Nintendo 3DS (glasses-free 3D) & Apple iPhone 4S (Siri)",
            "news": "Death of Steve Jobs; Arab Spring revolutions; Fukushima nuclear disaster",
            "culture": "Game of Thrones premieres on HBO; Royal Wedding of Prince William & Kate Middleton"
        },
        "new_events": [
            {
                "id": "death-of-steve-jobs-2011",
                "title": "Steve Jobs Passes Away at Age 56",
                "year": 2011,
                "date": "2011-10-05",
                "category": ["news", "tech"],
                "type": "milestone",
                "summary": "The visionary co-founder of Apple passed away, sparking spontaneous digital and physical memorials worldwide.",
                "narrative": "One day after Apple unveiled the iPhone 4S, Steve Jobs passed away from pancreatic cancer. Spontaneous memorials erupted outside glass Apple Stores across Tokyo, London, Paris, and New York, where grieving fans laid white roses, apples with bite marks, and illuminated iPads with condolences. His biographer Walter Isaacson published his definitive biography weeks later, becoming an instant global bestseller.",
                "why_it_matters": "Jobs' passing was mourned like that of an artist or statesman, symbolizing technology's deep emotional connection to human creativity.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Steve Jobs - Wikipedia", "url": "https://en.wikipedia.org/wiki/Steve_Jobs" }
                ]
            },
            {
                "id": "adele-21-global-phenomenon-2011",
                "title": "Adele's '21' Sells 31M Copies & Defies Streaming Transition",
                "year": 2011,
                "date": "2011-01-24",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "With heartbroken power ballads like 'Rolling in the Deep', 22-year-old Adele swept the planet.",
                "narrative": "In an era when music pundits proclaimed that the full-length album was dead and physical sales were obsolete, London singer-songwriter Adele proved them spectacularly wrong. Armed with a volcanic voice and unvarnished emotional pain from a broken relationship, '21' spawned universal anthems like 'Someone Like You' and 'Set Fire to the Rain', spending 24 weeks at #1 in the US and selling 31 million copies globally.",
                "why_it_matters": "It became the best-selling album of the 21st century, proving raw vocal authenticity and classic songwriting could unite all demographics.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "21 (Adele album) - Wikipedia", "url": "https://en.wikipedia.org/wiki/21_(Adele_album)" }
                ]
            },
            {
                "id": "imessage-blue-bubbles-2011",
                "title": "Apple Launches iMessage & Creates the Blue vs. Green Bubble Divide",
                "year": 2011,
                "date": "2011-10-12",
                "category": ["communication", "gadget"],
                "type": "launch",
                "summary": "Apple released iOS 5 featuring iMessage, introducing end-to-end encrypted chats, typing dots, and blue bubbles.",
                "narrative": "Shipped as an automatic upgrade in iOS 5, iMessage allowed iPhone, iPad, and Mac users to text, send high-res photos, and see real-time typing indicators over Wi-Fi and cellular without SMS carrier charges. Messages to fellow Apple users were colored vibrant blue, while SMS messages to Android phones reverted to standard green, unintentionally creating a potent social dynamic among young smartphone users.",
                "why_it_matters": "iMessage became one of Apple's stickiest lock-in features, defining mobile social messaging etiquette in North America for over a decade.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "iMessage - Wikipedia", "url": "https://en.wikipedia.org/wiki/IMessage" }
                ]
            }
        ]
    },
    2012: {
        "felt_like": {
            "os": "Windows 8 (Start button removed!) / OS X Mountain Lion / iOS 6",
            "browser": "Chrome (officially overtakes IE as #1 globally) / Safari",
            "messenger": "WhatsApp / iMessage / Facebook Messenger",
            "social_network": "Instagram (bought by Facebook) / Twitter / Tumblr / Vine (acquired)",
            "music": "Psy 'Gangnam Style' (breaks YouTube!), Carly Rae Jepsen 'Call Me Maybe', Kendrick Lamar",
            "phone": "iPhone 5 (taller 4-inch screen, Lightning connector) & Samsung Galaxy S3",
            "video": "Gangnam Style 1 Billion views / Netflix Originals announced",
            "website": "Flat design starts killing skeuomorphism; parallax scrolling craze",
            "fashion": "Peplum tops, sneaker wedges (Isabel Marant), dip-dyed ombre hair, galaxy print",
            "gadget": "Raspberry Pi & Apple iPhone 5 (with Lightning port)",
            "news": "London 2012 Olympics; Curiosity rover lands on Mars; Sandy Hook tragedy",
            "culture": "The Avengers unites Marvel Cinematic Universe; Mayan calendar apocalypse panic"
        },
        "new_events": [
            {
                "id": "psy-gangnam-style-billion-views-2012",
                "title": "Psy's 'Gangnam Style' Breaks YouTube's 32-Bit View Counter",
                "year": 2012,
                "date": "2012-07-15",
                "category": ["music", "viral-culture"],
                "type": "cultural_shift",
                "summary": "Psy's comedic horse-riding dance video became the first video in history to hit 1 Billion YouTube views.",
                "narrative": "Dressed in a tuxedo jacket and dark sunglasses, South Korean rapper Psy galloped across saunas, elevators, and horse stables. The infectious K-pop beat exploded across every continent, danced by everyone from world leaders to schoolchildren. By December 21, 2012, it crossed one billion views, eventually exceeding 2,147,483,647 views and forcing YouTube engineers to rewrite their integer view counter from 32-bit to 64-bit.",
                "why_it_matters": "Gangnam Style proved non-English music could conquer global digital culture and demonstrated YouTube's power as the planetary jukebox.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Gangnam Style - Wikipedia", "url": "https://en.wikipedia.org/wiki/Gangnam_Style" }
                ]
            },
            {
                "id": "higgs-boson-curiosity-mars-2012",
                "title": "Discovery of the Higgs Boson & Mars Curiosity Landing",
                "year": 2012,
                "date": "2012-07-04",
                "category": ["science", "news"],
                "type": "milestone",
                "summary": "CERN discovered the elusive 'God Particle' in Geneva, while NASA landed Curiosity on Mars using a sky crane.",
                "narrative": "At CERN's Large Hadron Collider, physicists announced the detection of the Higgs Boson with 5-sigma certainty, confirming the fundamental mechanism that gives mass to subatomic particles. One month later, millions watched a nail-biting NASA control room livestream as the Curiosity rover executed 'Seven Minutes of Terror', touching down safely on the Martian surface with a rocket-powered sky crane.",
                "why_it_matters": "These twin achievements marked a golden triumph for international scientific collaboration and digital public science communication.",
                "impact": 5,
                "nostalgia": 3,
                "sources": [
                    { "title": "Higgs boson - Wikipedia", "url": "https://en.wikipedia.org/wiki/Higgs_boson" },
                    { "title": "Curiosity (rover) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Curiosity_(rover)" }
                ]
            },
            {
                "id": "sneaker-wedges-peplum-fashion-2012",
                "title": "Isabel Marant Sneaker Wedges & Peak Tumblr Girl Aesthetic",
                "year": 2012,
                "date": "2012-05-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Hidden-heel chunky wedge sneakers, structured peplum tops, and pastel ombre hair ruled youth fashion.",
                "narrative": "French designer Isabel Marant's 'Bekket' high-top sneakers with concealed three-inch wedge heels became the most sought-after footwear in the world, cloned by Zara, Steve Madden, and Target. Alongside peplum skirts that flared at the waist and dip-dyed turquoise or pink hair tips, this look was cataloged across millions of curated Tumblr and Lookbook.nu moodboards.",
                "why_it_matters": "It marked the era when aesthetic micro-trends spread globally through social blogging curation rather than traditional print fashion magazines.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Isabel Marant - Wikipedia", "url": "https://en.wikipedia.org/wiki/Isabel_Marant" }
                ]
            }
        ]
    },
    2013: {
        "felt_like": {
            "os": "iOS 7 (Jony Ive kills skeuomorphism with neon flat design) / Windows 8.1",
            "browser": "Chrome / Safari / Firefox",
            "messenger": "Snapchat (Stories launched!) / WhatsApp / iMessage / Slack (beta)",
            "social_network": "Vine (6-second comedy loop boom) / Instagram (video added) / Twitter IPO",
            "music": "Daft Punk 'Get Lucky', Lorde 'Royals', Robin Thicke 'Blurred Lines', Drake",
            "phone": "iPhone 5s (Touch ID fingerprint sensor & Gold color) & Moto X",
            "video": "Vine loops / Netflix drops full seasons at once (House of Cards, Orange Is the New Black)",
            "website": "Flat design everywhere, bright pastels, hero video headers, hamburger menus",
            "fashion": "Normcore emerges, flannel tied around high-waisted shorts, black skinny jeans with ripped knees",
            "gadget": "Sony PlayStation 4 & Apple iPhone 5s with Touch ID",
            "news": "Edward Snowden leaks NSA PRISM surveillance; Boston Marathon bombing",
            "culture": "Breaking Bad series finale; Disney's Frozen and 'Let It Go' madness"
        },
        "new_events": [
            {
                "id": "vine-short-form-video-2013",
                "title": "Vine Launches & Pioneers 6-Second Comedy Video Culture",
                "year": 2013,
                "date": "2013-01-24",
                "category": ["social", "culture"],
                "type": "launch",
                "summary": "Twitter released Vine, where users looped 6-second clips that established short-form comedic video.",
                "narrative": "Constrained by an ultra-short six-second limit and seamless looping, Vine creators mastered jump-cuts, slapstick timing, and rapid punchlines. Teenagers made videos in bedrooms that racked up tens of millions of loops, launching stars like Shawn Mendes and David Dobrik. The app became a thriving incubator for Black creative comedy and viral catchphrases ('Do it for the Vine!', 'Yeet!', 'What are those!?').",
                "why_it_matters": "Vine invented the rhythm, visual language, and creator culture of short-form vertical video that TikTok and Reels later transformed into an empire.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Vine (service) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Vine_(service)" }
                ]
            },
            {
                "id": "ios-7-flat-design-2013",
                "title": "Apple Releases iOS 7: The Death of Skeuomorphism",
                "year": 2013,
                "date": "2013-09-18",
                "category": ["design", "software"],
                "type": "launch",
                "summary": "Jony Ive overhauled Apple's interface, replacing leather textures and glossy buttons with neon flat minimalism.",
                "narrative": "Gone was the green felt in Game Center, the yellow legal pad in Notes, and the faux leather stitching in Calendar. Jony Ive ushered in frosted translucent blurs, razor-thin typography, dynamic parallax wallpapers, and bold neon color palettes. The tech world gasped in shock, but within months, virtually every mobile app, operating system, and website on earth discarded skeuomorphism in favor of flat digital surfaces.",
                "why_it_matters": "iOS 7 represented the most radical and influential design reboot in consumer software history, shaping digital aesthetics for a decade.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "iOS 7 - Wikipedia", "url": "https://en.wikipedia.org/wiki/IOS_7" }
                ]
            },
            {
                "id": "daft-punk-get-lucky-lorde-2013",
                "title": "Daft Punk's 'Get Lucky' & Lorde's Anti-Pop Sensation 'Royals'",
                "year": 2013,
                "date": "2013-04-19",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "French robots Daft Punk revived live disco-funk with Pharrell, while 16-year-old Lorde conquered the world with 'Royals'.",
                "narrative": "With Nile Rodgers' sublime rhythmic guitar scratching and Pharrell Williams' falsetto, Daft Punk's 'Get Lucky' from *Random Access Memories* was the inescapable sound of summer. Meanwhile, from suburban Auckland, New Zealand, 16-year-old Ella Yelich-O'Connor (Lorde) dropped 'Royals'—a minimalist bass-and-finger-snap critique of pop star luxury that won Song of the Year and ushered in melancholic, whispery pop.",
                "why_it_matters": "These tracks signaled a rebellion against cookie-cutter EDM synths, steering mainstream music back toward organic funk instrumentation and bedroom minimalism.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Get Lucky (Daft Punk song) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Get_Lucky_(Daft_Punk_song)" },
                    { "title": "Royals (song) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Royals_(song)" }
                ]
            }
        ]
    },
    2014: {
        "felt_like": {
            "os": "iOS 8 / Mac OS X Yosemite / Android 5.0 Lollipop (Material Design)",
            "browser": "Chrome / Safari / Firefox",
            "messenger": "WhatsApp (bought for $19B!) / WeChat / Telegram / Facebook Messenger",
            "social_network": "Instagram / Snapchat / Twitter / Vine / Tumblr",
            "music": "Taylor Swift '1989' (kills streaming, sells 1.28M opening week), Pharrell 'Happy'",
            "phone": "iPhone 6 & 6 Plus ('Bendgate'!) & OnePlus One",
            "video": "Netflix binge-watching / Twitch (acquired by Amazon for $970M)",
            "website": "Material Design, card layouts, parallax scrolling, parallax hero banners",
            "fashion": "Normcore: plain white sneakers, Stan Smiths, dad caps, monochrome gray hoodies",
            "gadget": "Apple Watch announced & iPhone 6 / 6 Plus",
            "news": "Ebola epidemic in West Africa; Ferguson protests; annexation of Crimea",
            "culture": "Gamergate controversy; Guardians of the Galaxy; Flappy Bird creator deletes game"
        },
        "new_events": [
            {
                "id": "taylor-swift-1989-pop-transition-2014",
                "title": "Taylor Swift Drops '1989' & Pulls Catalog from Spotify",
                "year": 2014,
                "date": "2014-10-27",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "Swift completed her transition to pure 80s synth-pop, selling 1.28 million copies in week one.",
                "narrative": "Named after her birth year and recorded with Swedish hitmaker Max Martin, '1989' turned Taylor Swift from country-pop darling into an untouchable global pop titan with 'Shake It Off' and 'Blank Space'. Days after release, she pulled her entire catalog from Spotify, writing an op-ed declaring that 'music is art, and art is important and rare, and valuable things should be paid for.'",
                "why_it_matters": "Swift's standoff catalyzed an industry-wide reckoning over music streaming economics, artist royalties, and the value of digital intellectual property.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "1989 (Taylor Swift album) - Wikipedia", "url": "https://en.wikipedia.org/wiki/1989_(Taylor_Swift_album)" }
                ]
            },
            {
                "id": "normcore-fashion-movement-2014",
                "title": "Normcore: The Unpretentious Anti-Fashion Trend",
                "year": 2014,
                "date": "2014-02-26",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "The deliberate rejection of luxury logos in favor of ordinary, nondescript basics took the fashion world by storm.",
                "narrative": "First highlighted by trend-forecasting agency K-Hole, 'Normcore' found coolness in looking completely unexceptional. Fashionistas traded designer footwear for plain white Adidas Stan Smiths, chunky gray New Balance 990s, fleece zip-ups, Patagonia vests, and generic baseball caps. It was an ironic, comfortable antidote to exhausting hipster elitism and hyper-trendy fashion cycles.",
                "why_it_matters": "Normcore presaged the shift toward utilitarian comfort, minimalist wardrobe capsules, and modern relaxed-fit workwear.",
                "impact": 4,
                "nostalgia": 4,
                "sources": [
                    { "title": "Normcore - Wikipedia", "url": "https://en.wikipedia.org/wiki/Normcore" }
                ]
            },
            {
                "id": "iphone-6-bendgate-2014",
                "title": "Apple Releases iPhone 6 & Sparks 'Bendgate' Internet Frenzy",
                "year": 2014,
                "date": "2014-09-19",
                "category": ["gadget", "viral-culture"],
                "type": "launch",
                "summary": "Apple gave in to consumer demand for large screens, but viral bend-test videos created an international PR storm.",
                "narrative": "With screens expanded to 4.7 and 5.5 inches, the iPhone 6 and 6 Plus sold a record 10 million units in their opening weekend. But when early buyers reported their ultra-thin aluminum phones warping inside tight front pockets, YouTuber Unbox Therapy posted a video bending a 6 Plus barehanded. The video racked up tens of millions of views, forcing Apple to open its secret stress-testing labs to journalists.",
                "why_it_matters": "Bendgate elevated YouTube product torture tests into high-stakes consumer journalism and prompted Apple to adopt hardened aerospace aluminum.",
                "impact": 4,
                "nostalgia": 4,
                "sources": [
                    { "title": "iPhone 6 - Wikipedia", "url": "https://en.wikipedia.org/wiki/IPhone_6" }
                ]
            }
        ]
    },
    2015: {
        "felt_like": {
            "os": "Windows 10 (free upgrade!) / iOS 9 / macOS El Capitan",
            "browser": "Chrome / Edge (IE retired) / Safari",
            "messenger": "Slack (default work communication) / Discord (launching) / WhatsApp",
            "social_network": "Instagram (ditching strict square photos) / Snapchat (Lenses / dog filter!) / Twitter",
            "music": "Apple Music launches, Adele '25' ('Hello'), Drake 'Hotline Bling', Kendrick Lamar",
            "phone": "iPhone 6s (3D Touch, Rose Gold) & Samsung Galaxy S6 Edge",
            "video": "Periscope & Meerkat live streaming craze / Netflix 4K",
            "website": "Clean card UI, Flexbox, SVG icons, subtle micro-interactions",
            "fashion": "Athleisure boom: Lululemon leggings everywhere, Yeezy Boost 350s, bomber jackets",
            "gadget": "Apple Watch (first gen) & DJI Phantom 3 4K drone",
            "news": "US Supreme Court legalizes same-sex marriage; Paris terrorist attacks & Climate Accord",
            "culture": "Star Wars: The Force Awakens reboots franchise; Drake Hotline Bling meme dance"
        },
        "new_events": [
            {
                "id": "same-sex-marriage-rainbow-filter-2015",
                "title": "US Legalizes Same-Sex Marriage & 26M Facebook Rainbow Filters",
                "year": 2015,
                "date": "2015-06-26",
                "category": ["news", "culture"],
                "type": "milestone",
                "summary": "The Supreme Court's Obergefell v. Hodges ruling legalized same-sex marriage, turning feeds into a sea of rainbows.",
                "narrative": "When the Supreme Court recognized equal marriage rights nationwide, the White House was bathed in rainbow floodlights. Under the hashtag #LoveWins, Facebook deployed a 'Celebrate Pride' tool that allowed users to overlay a translucent rainbow filter on their profile photo with one tap. Over 26 million users transformed their digital avatars, generating over half a billion likes and comments.",
                "why_it_matters": "It demonstrated social media's power to coordinate an instantaneous, worldwide celebration of civil rights progress.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Obergefell v. Hodges - Wikipedia", "url": "https://en.wikipedia.org/wiki/Obergefell_v._Hodges" }
                ]
            },
            {
                "id": "yeezy-boost-athleisure-boom-2015",
                "title": "Kanye West Unveils Yeezy Boost 350 & Athleisure Explodes",
                "year": 2015,
                "date": "2015-06-27",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Kanye West partnered with Adidas on the Yeezy Boost 350, igniting the sneakerhead resale boom.",
                "narrative": "With Primeknit uppers and pillowy Adidas Boost soles, the Yeezy Boost 350 in 'Turtle Dove' and 'Pirate Black' sold out in seconds. Automated sneaker buying bots, camping lines outside retailers, and secondary market prices exceeding $1,000 transformed sneakers into alternative financial assets. Simultaneously, athleisure cemented leggings, track joggers, and designer athletic gear as everyday casual wear.",
                "why_it_matters": "The Yeezy phenomenon redefined streetwear culture, establishing the direct-to-consumer hype-drop model that dominated the fashion industry for years.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Adidas Yeezy - Wikipedia", "url": "https://en.wikipedia.org/wiki/Adidas_Yeezy" }
                ]
            },
            {
                "id": "drake-hotline-bling-meme-2015",
                "title": "Drake's 'Hotline Bling' Video Birthes the Ultimate Meme Format",
                "year": 2015,
                "date": "2015-10-19",
                "category": ["music", "viral-culture"],
                "type": "cultural_shift",
                "summary": "Drake's quirky dancing inside James Turrell-inspired glowing cubes created an immortal two-panel meme.",
                "narrative": "Wearing an oversized gray turtleneck sweater, Moncler puffer, and Timberland boots, Drake performed uninhibited, goofy dance moves in pastel-lit minimalist rooms. The video was instantly chopped into millions of Vines and GIFs. In particular, the two-panel screenshot of Drake turning away in disgust versus smiling in approval became one of the most widely used and durable meme formats in internet history.",
                "why_it_matters": "It exemplified artists intentionally choreographing music videos for memeability and viral second-screen distribution.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Hotline Bling - Wikipedia", "url": "https://en.wikipedia.org/wiki/Hotline_Bling" }
                ]
            }
        ]
    },
    2016: {
        "felt_like": {
            "os": "Windows 10 Anniversary / iOS 10 / Android 7.0 Nougat",
            "browser": "Chrome / Safari / Firefox Quantum in development",
            "messenger": "iMessage with stickers & fireworks / WhatsApp end-to-end encryption / Telegram",
            "social_network": "Instagram Stories (Snapchat clone) / Musical.ly / Snapchat Spectacles",
            "music": "Drake 'Views' ('One Dance' hits 1B streams), Frank Ocean 'Blonde', Beyoncé 'Lemonade'",
            "phone": "iPhone 7 (No headphone jack! Jet Black) & Google Pixel (first gen)",
            "video": "Facebook Live (chewbacca mom) / YouTube creator drama / Netflix downloads",
            "website": "Mobile-first, accelerated mobile pages (AMP), dark mode experiments",
            "fashion": "Millennial pink, choker necklaces, Off-White industrial belts, dad hats",
            "gadget": "Apple AirPods & Nintendo NES Classic Mini",
            "news": "Donald Trump elected US President; Brexit referendum passes in UK; Cubs win World Series",
            "culture": "Stranger Things season one retro craze; Leonardo DiCaprio finally wins Oscar"
        },
        "new_events": [
            {
                "id": "apple-airpods-cord-cutting-2016",
                "title": "Apple Ditches Headphone Jack & Launches AirPods",
                "year": 2016,
                "date": "2016-09-07",
                "category": ["gadget", "design"],
                "type": "launch",
                "summary": "Apple removed the century-old 3.5mm headphone jack on the iPhone 7, introducing wireless AirPods.",
                "narrative": "Phil Schiller invoked the word 'Courage' on stage to explain ditching the analog audio jack, inviting intense mockery and memes comparing the white AirPods to broken electric toothbrush heads. But when consumers popped open the dental-floss dental case and experienced seamless optical ear detection and beamforming microphones, AirPods became an instant status symbol and a multi-billion dollar business.",
                "why_it_matters": "AirPods normalized true wireless audio, rendering wired headphones nearly obsolete for general consumer use.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "AirPods - Wikipedia", "url": "https://en.wikipedia.org/wiki/AirPods" }
                ]
            },
            {
                "id": "brexit-and-trump-election-2016",
                "title": "Brexit Vote & Trump Election: The Social Media Echo Chamber",
                "year": 2016,
                "date": "2016-11-08",
                "category": ["news", "culture"],
                "type": "milestone",
                "summary": "Two seismic political shockwaves sparked intense global scrutiny into algorithmic newsfeeds and digital polarization.",
                "narrative": "In June, the UK voted to exit the European Union; in November, reality television host and billionaire Donald Trump won the US presidency. Both results defied establishment polling models and forced an agonizing post-mortem into how algorithmic Facebook news feeds, targeted ad micro-targeting, and online polarization reshaped democratic consensus.",
                "why_it_matters": "2016 was the pivotal turning point when governments and tech leaders recognized social media algorithms as powerful geopolitical forces.",
                "impact": 5,
                "nostalgia": 2,
                "sources": [
                    { "title": "2016 United States presidential election - Wikipedia", "url": "https://en.wikipedia.org/wiki/2016_United_States_presidential_election" },
                    { "title": "Brexit - Wikipedia", "url": "https://en.wikipedia.org/wiki/Brexit" }
                ]
            },
            {
                "id": "millennial-pink-chokers-2016",
                "title": "Millennial Pink & the 90s Choker Renaissance",
                "year": 2016,
                "date": "2016-05-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "A soft muted salmon blush color and velvet neck chokers became the defining visual markers of the generation.",
                "narrative": "Coined by design writers, 'Millennial Pink'—a calming, androgynous grapefruit-tinted blush—dominated everything from Glossier cosmetic packaging to Instagram interior design and tech gadgets like the Rose Gold iPhone. Simultaneously, 90s velvet ribbon and plastic tattoo chokers re-emerged on every red carpet and festival grounds.",
                "why_it_matters": "It became the definitive aesthetic shade of a generation, signaling a design shift toward gender-fluid minimalism and nostalgic retro revival.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Millennial pink - Wikipedia", "url": "https://en.wikipedia.org/wiki/Shades_of_pink#Millennial_pink" }
                ]
            }
        ]
    },
    2017: {
        "felt_like": {
            "os": "Windows 10 Fall Creators / iOS 11 / macOS High Sierra",
            "browser": "Chrome (dominating 60%+ market share) / Safari",
            "messenger": "Discord (server boom) / WhatsApp / iMessage / Slack",
            "social_network": "Instagram Stories overtakes Snapchat / Musical.ly / Twitter expands to 280 characters",
            "music": "Luis Fonsi 'Despacito', Kendrick Lamar 'HUMBLE.', Ed Sheeran 'Shape of You'",
            "phone": "iPhone X ($999, Face ID, notch, no home button) & Samsung Galaxy S8",
            "video": "YouTube livestreaming / Netflix interactive shows / Twitch IRL streaming",
            "website": "CSS Grid layout officially supported across browsers, smooth web animations",
            "fashion": "Balenciaga Triple S 'chunky dad sneakers', bike shorts, tiny Matrix sunglasses",
            "gadget": "Nintendo Switch & Apple iPhone X",
            "news": "Solar eclipse across America; Hurricane Maria in Puerto Rico; Las Vegas shooting",
            "culture": "Fidget spinner mania in every school; Jordan Peele's Get Out"
        },
        "new_events": [
            {
                "id": "nintendo-switch-zelda-botw-2017",
                "title": "Nintendo Switch Launches with 'Zelda: Breath of the Wild'",
                "year": 2017,
                "date": "2017-03-03",
                "category": ["gadget", "gaming"],
                "type": "launch",
                "summary": "Nintendo released the hybrid Switch console, uniting home television and portable handheld gaming.",
                "narrative": "Recovering from the sluggish Wii U era, Nintendo delivered an innovative hybrid: a tablet with detachable Joy-Con controllers that slipped into a TV dock and seamlessly transitioned to portable play. Launching alongside 'The Legend of Zelda: Breath of the Wild'—an open-world masterpiece of physics, climbing, and exploration—the Switch became one of the best-selling gaming systems of all time.",
                "why_it_matters": "The Switch dissolved the historic wall between home console performance and on-the-go portable handheld gaming.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Nintendo Switch - Wikipedia", "url": "https://en.wikipedia.org/wiki/Nintendo_Switch" }
                ]
            },
            {
                "id": "fidget-spinner-craze-2017",
                "title": "Fidget Spinners Become the Global Toy Obsession",
                "year": 2017,
                "date": "2017-04-15",
                "category": ["gadget", "viral-culture"],
                "type": "cultural_shift",
                "summary": "Three-pronged ball-bearing spinners exploded across classrooms, street corners, and viral YouTube videos.",
                "narrative": "Promoted originally as sensory calming tools for ADHD and anxiety, ball-bearing plastic and brass fidget spinners became an all-consuming viral craze. Children practiced finger balance tricks, schools banned them from desks, and factories in Dongguan retooled around the clock to pump out millions of units before the fad evaporated almost as quickly as it arrived.",
                "why_it_matters": "It was a textbook example of modern algorithmic viral product frenzies accelerated by YouTube trick videos and social media.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "Fidget spinner - Wikipedia", "url": "https://en.wikipedia.org/wiki/Fidget_spinner" }
                ]
            },
            {
                "id": "despacito-latin-pop-streaming-2017",
                "title": "Luis Fonsi & Daddy Yankee's 'Despacito' Breaks YouTube",
                "year": 2017,
                "date": "2017-01-12",
                "category": ["music", "culture"],
                "type": "cultural_shift",
                "summary": "The Puerto Rican reggaeton-pop smash tied the all-time Billboard record with 16 weeks at #1.",
                "narrative": "Shot on the colorful streets of La Perla in Old San Juan, 'Despacito' blended acoustic guitar lines with irresistible reggaeton dembow percussion. Amplified by an English-Spanish remix featuring Justin Bieber, the track became a global juggernaut, shattering streaming records and becoming the first video to surpass 3, 4, 5, 6, and 7 billion views on YouTube.",
                "why_it_matters": "Despacito permanently opened the global streaming ecosystem to Spanish-language Latin music, paving the way for Bad Bunny and Rosalía.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Despacito - Wikipedia", "url": "https://en.wikipedia.org/wiki/Despacito" }
                ]
            }
        ]
    },
    2018: {
        "felt_like": {
            "os": "Windows 10 October / iOS 12 / Android 9 Pie",
            "browser": "Chrome (celebrates 10th birthday) / Safari / Firefox Quantum",
            "messenger": "WhatsApp (2 billion users) / Discord / Telegram / iMessage",
            "social_network": "TikTok (merges with Musical.ly) / Instagram (IGTV launches) / Reddit redesign",
            "music": "Drake 'Scorpion' ('In My Feelings' Kiki challenge), Ariana Grande 'thank u, next'",
            "phone": "iPhone XS Max & iPhone XR (vibrant colors) & Google Pixel 3 (Night Sight)",
            "video": "TikTok 15-second vertical clips / Fortnite Twitch streams with Drake",
            "website": "GDPR cookie banners everywhere, dark mode system preference (prefers-color-scheme)",
            "fashion": "Chunky 'ugly' sneakers, neon cycling shorts, oversized streetwear blazers, Supreme box logos",
            "gadget": "Apple Watch Series 4 (with ECG heart sensor) & Oculus Go",
            "news": "Thai cave rescue captivated global livestreams; Death of Stephen Hawking",
            "culture": "Marvel's Black Panther becomes cultural milestone; Spider-Man: Into the Spider-Verse"
        },
        "new_events": [
            {
                "id": "fortnite-ninja-drake-twitch-2018",
                "title": "Fortnite Conquers Youth Culture: Ninja Streams with Drake",
                "year": 2018,
                "date": "2018-03-14",
                "category": ["gaming", "culture"],
                "type": "cultural_shift",
                "summary": "Epic Games' free-to-play battle royale became an international sensation, culminating in a record Twitch stream.",
                "narrative": "Fortnite's cartoonish battle bus, build mechanics, and emote dances like the 'Floss' invaded schoolyards, soccer goal celebrations, and mainstream media. In March, streamer Tyler 'Ninja' Blevins was joined on squad chat by superstar rapper Drake, NFL receiver JuJu Smith-Schuster, and Travis Scott, shattering Twitch's all-time concurrent record with over 628,000 viewers.",
                "why_it_matters": "It firmly established live streaming as mainstream pop culture and elevated competitive gaming into the default social playground for Gen Z.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Fortnite Battle Royale - Wikipedia", "url": "https://en.wikipedia.org/wiki/Fortnite_Battle_Royale" }
                ]
            },
            {
                "id": "black-panther-cultural-milestone-2018",
                "title": "Marvel's 'Black Panther' Becomes a Global Cultural Phenomenon",
                "year": 2018,
                "date": "2018-02-16",
                "category": ["culture", "media"],
                "type": "cultural_shift",
                "summary": "Director Ryan Coogler and Chadwick Boseman brought the Afrofuturist world of Wakanda to life, grossing $1.34B.",
                "narrative": "Starring Chadwick Boseman as T'Challa alongside Michael B. Jordan's Killmonger, 'Black Panther' was a watershed cultural event. The crossed-arms 'Wakanda Forever' salute became an international symbol of Black pride and celebration. With an Oscar-nominated score and soundtrack curated by Kendrick Lamar, it became the first superhero film nominated for Best Picture at the Academy Awards.",
                "why_it_matters": "It shattered long-held Hollywood industry myths about the global box office viability of Black-led blockbuster cinema.",
                "impact": 5,
                "nostalgia": 4,
                "sources": [
                    { "title": "Black Panther (film) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Black_Panther_(film)" }
                ]
            },
            {
                "id": "ugly-dad-sneaker-trend-2018",
                "title": "The Balenciaga Triple S & The 'Ugly Dad Sneaker' Craze",
                "year": 2018,
                "date": "2018-04-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Chunky, orthotic-looking multi-layered sneakers became the undisputed kings of luxury fashion.",
                "narrative": "Designed by Demna Gvasalia at Balenciaga, the $895 'Triple S' sneaker featured three stacked athletic soles, pre-scuffed leather, and exaggerated proportions that looked like something a 1990s suburban dad would wear to mow the lawn. Fashion critics were polarized, but hypebeasts and influencers snapped them up, sparking copycat chunky silhouettes from Gucci, Fila, and Nike.",
                "why_it_matters": "The chunky dad shoe trend permanently loosened sleek fashion aesthetics, making voluminous silhouettes and comfort central to luxury streetwear.",
                "impact": 4,
                "nostalgia": 4,
                "sources": [
                    { "title": "Sneakers as fashion - Wikipedia", "url": "https://en.wikipedia.org/wiki/Sneakers_as_fashion" }
                ]
            }
        ]
    },
    2019: {
        "felt_like": {
            "os": "macOS Catalina / iOS 13 (system-wide Dark Mode!) / Windows 10",
            "browser": "Chrome / Edge switches to Chromium engine / Safari",
            "messenger": "Discord / Telegram / WhatsApp / Signal",
            "social_network": "TikTok (surpasses 1B downloads) / Instagram (hiding likes experiment) / Twitter",
            "music": "Lil Nas X 'Old Town Road', Billie Eilish 'Bad Guy', Lizzo 'Truth Hurts'",
            "phone": "iPhone 11 Pro (triple camera 'stove top' layout) & Samsung Galaxy Fold",
            "video": "Disney+ launches with The Mandalorian (Baby Yoda!) / TikTok",
            "website": "Dark mode default toggle, JAMstack, Jamstack headless architectures",
            "fashion": "VSCO girl aesthetic (Hydro Flasks, scrunchies, oversized tees) & E-girl / E-boy chains",
            "gadget": "Apple AirPods Pro (Noise Cancelling) & Nintendo Switch Lite",
            "news": "First image of a Black Hole; Notre-Dame Cathedral fire; Greta Thunberg climate strikes",
            "culture": "Avengers: Endgame becomes #1 box office film; Game of Thrones series finale"
        },
        "new_events": [
            {
                "id": "old-town-road-tiktok-record-2019",
                "title": "Lil Nas X's 'Old Town Road' Breaks the All-Time Billboard Record",
                "year": 2019,
                "date": "2019-04-05",
                "category": ["music", "viral-culture"],
                "type": "cultural_shift",
                "summary": "20-year-old Lil Nas X used TikTok memes to propel a $30 beat to a record 19 consecutive weeks at #1.",
                "narrative": "After buying a beat built on a Nine Inch Nails banjo sample for $30 online, Montero Hill (Lil Nas X) promoted 'Old Town Road' through cowboy memes on TikTok's 'Yeehaw Challenge'. When Billboard controversially removed it from the country chart, Billy Ray Cyrus joined for a remix. The track spent an unprecedented 19 consecutive weeks at number one on the Billboard Hot 100, smashing the all-time 61-year chart record.",
                "why_it_matters": "It demonstrated that TikTok was now the supreme kingmaker of the global music industry, capable of circumventing traditional radio and record labels.",
                "impact": 5,
                "nostalgia": 5,
                "sources": [
                    { "title": "Old Town Road - Wikipedia", "url": "https://en.wikipedia.org/wiki/Old_Town_Road" }
                ]
            },
            {
                "id": "first-black-hole-photograph-2019",
                "title": "Event Horizon Telescope Captures First Photograph of a Black Hole",
                "year": 2019,
                "date": "2019-04-10",
                "category": ["science", "news"],
                "type": "milestone",
                "summary": "Scientists unveiled the first direct visual evidence of a supermassive black hole at the center of galaxy M87.",
                "narrative": "Combining petabytes of data from a synchronized network of eight radio telescopes spanning Hawaii, Chile, Spain, and the South Pole, the Event Horizon Telescope team synthesized a glowing orange ring of superheated plasma surrounding a pitch-black shadow. The awe-inspiring image was splashed across newspaper front pages worldwide, confirming Albert Einstein's century-old equations.",
                "why_it_matters": "It was hailed as one of the supreme technical achievements in astronomy and computational data processing of the 21st century.",
                "impact": 5,
                "nostalgia": 3,
                "sources": [
                    { "title": "Event Horizon Telescope - Wikipedia", "url": "https://en.wikipedia.org/wiki/Event_Horizon_Telescope" }
                ]
            },
            {
                "id": "vsco-girl-scrunchie-aesthetic-2019",
                "title": "VSCO Girls, Hydro Flasks & the Viral Subculture Explosion",
                "year": 2019,
                "date": "2019-07-01",
                "category": ["fashion", "culture"],
                "type": "cultural_shift",
                "summary": "Hydro Flask water bottles, velvet scrunchies, Birkenstocks, and oversized pastel tees became a summer phenomenon.",
                "narrative": "Named after the minimalist photo-editing app VSCO, the 'VSCO Girl' aesthetic conquered TikTok and high school hallways. The uniform was precise: oversized pastel t-shirts falling past running shorts, wrists stacked with velvet scrunchies, metal straws ('sksksk and I oop'), Carmex lip balm, and pastel Hydro Flask bottles covered in vinyl stickers. It was celebrated, satirized, and replicated across millions of viral videos.",
                "why_it_matters": "It marked the moment TikTok fully displaced Instagram as the birthplace and incubator of fast-moving youth fashion archetypes.",
                "impact": 4,
                "nostalgia": 5,
                "sources": [
                    { "title": "VSCO girl - Wikipedia", "url": "https://en.wikipedia.org/wiki/VSCO_girl" }
                ]
            }
        ]
    }
}

def apply_era3():
    for year, data in ERA3_UPDATES.items():
        year_path = f"src/data/years/{year}.json"
        with open(year_path, "r") as f:
            ydata = json.load(f)
            
        ydata["felt_like"] = data["felt_like"]
        
        events_path = f"src/data/events/{year}.json"
        with open(events_path, "r") as f:
            events = json.load(f)
            
        # Clean duplicate in 2015 if Amazon acquires Twitch was duplicated from 2014
        if year == 2015:
            events = [e for e in events if not ("twitch" in e.get("id", "").lower() and "amazon" in e.get("id", "").lower())]
            
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
    apply_era3()
