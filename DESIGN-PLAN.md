# Doodle Design System Plan — The Web Was Here

## Direction: Earth Doodle

Dark background (rich warm brown, like aged parchment or a well-worn desk) with hand-drawn earth-toned elements. Every surface gets the sketchy treatment. Think: nature journal meets vintage field notes meets maker's workshop.

---

## 1. Color Palette

### Background
- `--bg: #1a1714` (deep warm brown, not pure black)
- `--bg-elevated: #231f1a`
- `--bg-card: #2a2520`

### Earth Doodle Colors (primary palette)
- `--terracotta: #c47a5a` (warm orange-brown)
- `--sage: #7a9e7e` (muted green)
- `--ochre: #d4a853` (golden yellow)
- `--clay: #a67c5b` (medium brown)
- `--moss: #5c7a5e` (deep green)
- `--rust: #b85c3c` (burnt orange)
- `--earth: #8b7355` (warm neutral)

### Text
- `--text-primary: #f5f0e8` (warm cream)
- `--text-secondary: #c8bfb0` (muted warm gray)
- `--text-muted: #7a7060` (dim warm brown)

### Accents
- `--cream: #f5f0e8` (for hand-drawn lines)
- `--bark: #4a4035` (dark brown border)
- `--parchment: #e8dfd0` (light warm background)

---

## 2. Typography

### Display / Headlines
- **"Caveat"** (Google Fonts) — handwritten feel, used for large headings
- Fallback: cursive

### Body
- **"Space Grotesk"** — clean, modern, readable
- For event narratives and long-form text

### Mono / Data
- **"JetBrains Mono"** — for dates, scores, metadata
- Used sparingly for data labels

---

## 3. Doodle Elements (SVG + CSS)

### Borders
- Rough.js for sketchy card borders
- Hand-drawn underlines on headings
- Wobbly dividers between sections

### Decorations
- Hand-drawn stars, arrows, squiggles
- Doodle icons for categories (web, design, social, etc.)
- Corner doodles on cards (stars, swirls, lightning bolts)

### SVG Assets to Create
1. Category icons (hand-drawn style):
   - Web: globe with wobbly lines
   - Design: pencil/pen sketch
   - Social: speech bubbles
   - Hardware: phone/computer doodle
   - Viral: lightning bolt / explosion
   - Software: floppy disk / window

2. Decorative elements:
   - Stars (various sizes)
   - Arrows (pointing, curvy)
   - Squiggly underlines
   - Circles and rings
   - Lightning bolts
   - Swirls
   - Dots and speckles

3. Section dividers:
   - Wavy lines
   - Zigzag lines
   - Dotted paths
   - Hand-drawn horizontal rules

---

## 4. Component Design

### Navigation
- Logo: hand-drawn "TWWH" or full "The Web Was Here" in Caveat
- Links: sketchy underline on hover
- Border bottom: wobbly hand-drawn line

### Year Cards (homepage grid)
- Sketchy border (not clean 1px)
- Warm glow on hover (terracotta/ochre shadow)
- Slight rotation/tilt on hover
- Doodle corner decorations

### Event Cards
- Full sketchy border
- Category tags: pill-shaped with hand-drawn outline
- Impact/nostalgia scores: hand-drawn bar chart style
- Sources: small doodle arrow pointing to link

### "What it felt like" Section
- Chalkboard background texture (subtle)
- Hand-drawn grid lines
- Warm text for values (ochre/terracotta)

### Hero Section
- Giant hand-drawn title
- Animated doodle decorations (subtle float/wobble)
- Sketchy CTA buttons

---

## 5. Animation & Motion

### Hover States
- Slight scale (1.02-1.05)
- Warm glow intensifies
- Doodle elements wiggle slightly

### Page Transitions
- Elements draw-in on scroll (stroke-dashoffset animation)
- Cards fade + slide with slight rotation

### Micro-interactions
- Buttons: slight bounce on click
- Links: squiggly underline animates in
- Score bars: draw-in animation

### Easing
- `cubic-bezier(0.34, 1.56, 0.64, 1)` — bouncy overshoot
- `cubic-bezier(0.68, -0.55, 0.265, 1.55)` — elastic

---

## 6. Technical Implementation

### Rough.js Integration
- Install: `npm install roughjs`
- Use for all card borders, dividers, and decorative lines
- SVG-based, works server-side with Astro

### SVG Inline Doodles
- Hand-crafted SVG files in `public/doodles/`
- Inline in components for styling
- Animated via CSS

### CSS Custom Properties
- All colors as CSS variables for easy theming
- Doodle-specific variables for glow effects

### Font Loading
- Google Fonts: Caveat + Space Grotesk + JetBrains Mono
- Preconnect for performance

---

## 7. Page-by-Page Changes

### Homepage
- Hero: giant Caveat title, animated doodle decorations
- Era cards: sketchy borders, earth-toned accents per era
- Year grid: wobbly grid lines, glow on hover
- Purpose section: hand-drawn illustrations

### Year Pages (e.g., 2007)
- Year number: giant Caveat, warm glow
- "What it felt like": chalkboard-style grid
- Event list: sketchy cards, hand-drawn dividers
- Category tags: doodle pills

### Event Detail (future)
- Full doodle treatment
- Hand-drawn timeline connections
- Source citations with doodle arrows

---

## 8. Assets to Generate

### SVG Icons (hand-drawn style)
1. Globe (web)
2. Pencil (design)
3. Speech bubbles (social)
4. Lightning bolt (viral)
5. Phone (hardware)
6. Code brackets (development)
7. Chart (business)
8. Magnifying glass (search)
9. Play button (entertainment)
10. Envelope (communication)

### SVG Decorations
1. Stars (5 variations)
2. Arrows (4 variations)
3. Squiggly underlines
4. Circles/rings
5. Lightning bolts
6. Swirls
7. Dots pattern
8. Wavy divider
9. Zigzag divider
10. Hand-drawn box/border

### CSS Effects
1. Warm glow (box-shadow + text-shadow)
2. Sketchy border (Rough.js or SVG filter)
3. Wobble animation
4. Draw-in animation (stroke-dashoffset)
5. Float animation for decorations

---

## 9. Implementation Order

### Phase 1: Foundation
1. Update color palette in CSS variables
2. Add Caveat font
3. Create base SVG doodle assets
4. Set up Rough.js

### Phase 2: Components
1. Redesign navigation with doodle style
2. Redesign hero section
3. Redesign year cards
4. Redesign event cards
5. Redesign "what it felt like" section

### Phase 3: Polish
1. Add hover animations
2. Add page transitions
3. Add decorative doodles
4. Test responsive behavior

---

## 10. Reference Inspiration

- Google Doodles (playful, colorful)
-知essian (hand-drawn UI elements)
- Notion's hand-drawn icons
- Figma's community doodles
- Procreate illustrations on dark backgrounds
- Chalkboard art / street chalk art
