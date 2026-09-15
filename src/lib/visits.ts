const ABACUS_BASE = 'https://abacus.jasoncameron.dev';
const ABACUS_NAMESPACE = 'twwh-archive';
const ABACUS_KEY = 'visits';

let cached: number | null = null;

export async function getVisitCount(): Promise<number> {
  if (cached !== null) return cached;
  try {
    const res = await fetch(`${ABACUS_BASE}/get/${ABACUS_NAMESPACE}/${ABACUS_KEY}`, {
      signal: AbortSignal.timeout(3000),
    });
    if (res.ok) {
      const data = await res.json();
      if (typeof data?.value === 'number') {
        cached = data.value;
        return cached;
      }
    }
  } catch (_) {
    // fall through
  }
  cached = 0;
  return cached;
}
