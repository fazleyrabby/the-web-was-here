// Web Audio API Synthesizer for "The Web Was Here"
// Zero external assets - 100% generated in real-time in the browser

let audioCtx: AudioContext | null = null;
let dialUpTimeout: number | null = null;
let isDialing = false;

function getAudioContext(): AudioContext | null {
  if (typeof window === 'undefined') return null;
  const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
  if (!AudioContextClass) return null;
  if (!audioCtx) {
    audioCtx = new AudioContextClass();
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  return audioCtx;
}

export function isSoundMuted(): boolean {
  if (typeof window === 'undefined') return false;
  return localStorage.getItem('twwh_sound_muted') === 'true';
}

export function toggleSoundMute(): boolean {
  if (typeof window === 'undefined') return false;
  const current = isSoundMuted();
  const next = !current;
  localStorage.setItem('twwh_sound_muted', String(next));
  if (next && isDialing) {
    stopDialUp();
  }
  window.dispatchEvent(new CustomEvent('twwh-sound-toggled', { detail: { muted: next } }));
  return next;
}

// 8-Bit Retro Celebration Chime for "Relive"
export function playChimeSound() {
  if (isSoundMuted()) return;
  const ctx = getAudioContext();
  if (!ctx) return;

  const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
  const now = ctx.currentTime;

  notes.forEach((freq, index) => {
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(freq, now + index * 0.07);

    gain.gain.setValueAtTime(0, now + index * 0.07);
    gain.gain.linearRampToValueAtTime(0.18, now + index * 0.07 + 0.01);
    gain.gain.exponentialRampToValueAtTime(0.001, now + index * 0.07 + 0.22);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start(now + index * 0.07);
    osc.stop(now + index * 0.07 + 0.25);
  });
}

// Retro Sci-Fi Warp Sound for "Random Year / Time Warp"
export function playWarpSound() {
  if (isSoundMuted()) return;
  const ctx = getAudioContext();
  if (!ctx) return;

  const now = ctx.currentTime;
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();

  osc.type = 'sawtooth';
  osc.frequency.setValueAtTime(150, now);
  osc.frequency.exponentialRampToValueAtTime(900, now + 0.35);

  gain.gain.setValueAtTime(0.12, now);
  gain.gain.exponentialRampToValueAtTime(0.001, now + 0.38);

  osc.connect(gain);
  gain.connect(ctx.destination);

  osc.start(now);
  osc.stop(now + 0.4);
}

// Synthesized 56k Dial-Up Modem Handshake sequence
export function playDialUpSound(onProgress?: (status: string) => void): () => void {
  if (isSoundMuted()) return () => {};
  const ctx = getAudioContext();
  if (!ctx) return () => {};

  if (isDialing) {
    stopDialUp();
    return () => {};
  }

  isDialing = true;
  const now = ctx.currentTime;

  // 1. Dial Tone (350Hz + 440Hz)
  const osc1 = ctx.createOscillator();
  const osc2 = ctx.createOscillator();
  const dialGain = ctx.createGain();

  osc1.frequency.value = 350;
  osc2.frequency.value = 440;
  dialGain.gain.setValueAtTime(0.1, now);
  dialGain.gain.setValueAtTime(0, now + 0.9);

  osc1.connect(dialGain);
  osc2.connect(dialGain);
  dialGain.connect(ctx.destination);

  osc1.start(now);
  osc2.start(now);
  osc1.stop(now + 0.9);
  osc2.stop(now + 0.9);
  if (onProgress) onProgress('DIALING...');

  // 2. DTMF Rotary / Tones (0.9s - 2.2s)
  const dtmfFreqs = [
    [941, 1336], [697, 1209], [770, 1336], [852, 1477],
    [697, 1477], [770, 1209], [941, 1209]
  ];

  dtmfFreqs.forEach(([f1, f2], idx) => {
    const tStart = now + 1.0 + idx * 0.16;
    const tone1 = ctx.createOscillator();
    const tone2 = ctx.createOscillator();
    const tGain = ctx.createGain();

    tone1.frequency.value = f1;
    tone2.frequency.value = f2;
    tGain.gain.setValueAtTime(0.12, tStart);
    tGain.gain.setValueAtTime(0, tStart + 0.09);

    tone1.connect(tGain);
    tone2.connect(tGain);
    tGain.connect(ctx.destination);

    tone1.start(tStart);
    tone2.start(tStart);
    tone1.stop(tStart + 0.1);
    tone2.stop(tStart + 0.1);
  });

  // 3. Ringing & Handshake Carrier (2.4s - 5.5s)
  setTimeout(() => {
    if (!isDialing || isSoundMuted()) return;
    if (onProgress) onProgress('NEGOTIATING CARRIER...');

    const cNow = ctx.currentTime;
    // Carrier Whine
    const carrier = ctx.createOscillator();
    const cGain = ctx.createGain();
    carrier.type = 'sine';
    carrier.frequency.setValueAtTime(1800, cNow);
    carrier.frequency.linearRampToValueAtTime(2400, cNow + 0.6);
    carrier.frequency.setValueAtTime(1200, cNow + 0.8);
    cGain.gain.setValueAtTime(0.08, cNow);
    cGain.gain.exponentialRampToValueAtTime(0.001, cNow + 1.8);

    carrier.connect(cGain);
    cGain.connect(ctx.destination);
    carrier.start(cNow);
    carrier.stop(cNow + 1.8);

    // Handshake Noise Burst (Modem hash/static)
    const bufferSize = ctx.sampleRate * 2.2;
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * 0.14;
    }

    const noise = ctx.createBufferSource();
    noise.buffer = buffer;

    const filter = ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(1600, cNow + 0.4);
    filter.Q.value = 3.0;

    const nGain = ctx.createGain();
    nGain.gain.setValueAtTime(0, cNow + 0.4);
    nGain.gain.linearRampToValueAtTime(0.12, cNow + 0.6);
    nGain.gain.setValueAtTime(0.12, cNow + 1.8);
    nGain.gain.exponentialRampToValueAtTime(0.001, cNow + 2.5);

    noise.connect(filter);
    filter.connect(nGain);
    nGain.connect(ctx.destination);

    noise.start(cNow + 0.4);
    noise.stop(cNow + 2.6);
  }, 2200);

  // 4. Connection Success Ding (4.8s)
  setTimeout(() => {
    if (!isDialing || isSoundMuted()) return;
    if (onProgress) onProgress('CONNECTED @ 56,000 BPS!');

    const dingNow = ctx.currentTime;
    const ding = ctx.createOscillator();
    const dGain = ctx.createGain();
    ding.type = 'triangle';
    ding.frequency.setValueAtTime(880, dingNow);
    dGain.gain.setValueAtTime(0.15, dingNow);
    dGain.gain.exponentialRampToValueAtTime(0.001, dingNow + 0.6);

    ding.connect(dGain);
    dGain.connect(ctx.destination);
    ding.start(dingNow);
    ding.stop(dingNow + 0.6);

    setTimeout(() => {
      isDialing = false;
      if (onProgress) onProgress('ONLINE');
    }, 1200);
  }, 4800);

  return stopDialUp;
}

export function stopDialUp() {
  isDialing = false;
  if (dialUpTimeout) {
    clearTimeout(dialUpTimeout);
    dialUpTimeout = null;
  }
}
