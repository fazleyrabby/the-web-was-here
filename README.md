# The Web Was Here

An interactive, static archive of internet history from 1990 through 2026. Built with Astro. Each year has a curated narrative, events, sources, and local images.

## Run locally

Requires Node.js 22.12 or newer.

```sh
npm ci
npm run dev
```

Open the URL printed by Astro. For a production check, run `npm run build`; the generated site is in `dist/`. `npm run preview` serves that output locally.

## Content workflow

- `src/data/years/YYYY.json` holds the year summary, era, and event IDs.
- `src/data/events/YYYY.json` holds the events shown on that year's page.
- `public/images/events/YYYY/` and `public/images/hardware/` hold event artwork. Use an absolute public path such as `/images/events/2007/example.webp` in JSON.
- `schemas/` describes year and event data. Keep allowed category, type, and era values current when introducing a new one.

Run `npm run validate:data` after editing content. It checks both schemas, matching years, unique IDs, year event references, and local image paths. The production build runs the same check first. Source links should support the event's factual claims; the validator checks their format, not their accuracy or availability.

## Code map

- `src/pages/index.astro`: timeline homepage
- `src/pages/the-web/[year].astro`: generated year pages
- `src/layouts/`: shared shell and year layout
- `src/components/`: interactive UI, event lists, and decorative effects
- `src/styles/eras.css`: era styling

The 3D decoration on the 2026 page downloads Three.js when it nears the viewport. Visitors who do not scroll to it do not download that module.

## Deploy

Deploy the `dist/` folder to a static host after `npm run build`. The canonical URL and Open Graph image are configured in `src/layouts/Base.astro`; update `SITE_URL` there if the production domain changes.
