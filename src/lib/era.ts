export type Era =
  | 'foundation'
  | 'early-web'
  | 'bust-rebuild'
  | 'web-2'
  | 'mobile'
  | 'platform'
  | 'pandemic'
  | 'ai'
  | 'now';

export function eraForYear(year: number): Era {
  if (year <= 1994) return 'foundation';
  if (year <= 1999) return 'early-web';
  if (year <= 2004) return 'bust-rebuild';
  if (year <= 2009) return 'web-2';
  if (year <= 2014) return 'mobile';
  if (year <= 2019) return 'platform';
  if (year <= 2022) return 'pandemic';
  if (year >= 2026) return 'now';
  return 'ai';
}

export const ERA_META: Record<Era, { label: string; years: string; blurb: string }> = {
  foundation: {
    label: 'Foundation',
    years: '1990–1994',
    blurb: 'Plain HTML. Times New Roman. Blue links. The web before design.',
  },
  'early-web': {
    label: 'Early Web',
    years: '1995–1999',
    blurb: 'GeoCities. Tiled backgrounds. Marquees. Guestbooks. Pure chaos.',
  },
  'bust-rebuild': {
    label: 'Bust & Rebuild',
    years: '2000–2004',
    blurb: 'Flash intros. Bevel buttons. "Best viewed in Internet Explorer."',
  },
  'web-2': {
    label: 'Web 2.0',
    years: '2005–2009',
    blurb: 'Glossy buttons. Gradients. Reflections. Beta badges everywhere.',
  },
  mobile: {
    label: 'Mobile + Social',
    years: '2010–2014',
    blurb: 'Flat design. Big hero photos. Cards. Long scroll.',
  },
  platform: {
    label: 'Platform Era',
    years: '2015–2019',
    blurb: 'Material Design. Bold type. Elevation. Feeds everywhere.',
  },
  pandemic: {
    label: 'Pandemic Web',
    years: '2020–2022',
    blurb: 'Dark mode. Glassmorphism. Bento grids. Everything remote.',
  },
  ai: {
    label: 'AI Era',
    years: '2023–2025',
    blurb: 'Gradient mesh. Glass. Micro-interactions. Machines that answer.',
  },
  now: {
    label: 'The Present',
    years: '2026',
    blurb: 'Hairline borders. Bento grids. Command palettes. AI-native and restrained.',
  },
};
