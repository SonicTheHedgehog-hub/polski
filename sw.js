// Offline-Speicher der App. Bei jeder Änderung VERSION erhöhen.
const VERSION = "polski-v6", AUDIO_CACHE = "polski-audio";
const CORE = ["./", "./index.html", "./lessons.json", "./vocab.json", "./drills.json", "./stories.json", "./manifest.webmanifest", "./img/badge-30.webp", "./img/badge-7.webp", "./img/badge-b2.webp", "./img/badge-start.webp", "./img/celebrating.webp", "./img/ch-pierwsze.webp", "./img/ch-przyjaciele.webp", "./img/ch-rodzina.webp", "./img/ch-spoleczenstwo.webp", "./img/flaga.webp", "./img/flying.webp", "./img/happy.webp", "./img/head.webp", "./img/icon-180.png", "./img/icon-192.png", "./img/icon-512.png", "./img/kawa.webp", "./img/krakow.webp", "./img/kwiat.webp", "./img/listening.webp", "./img/mascot.webp", "./img/obwarzanek.webp", "./img/pierogi.webp", "./img/pisanka.webp", "./img/reading.webp", "./img/sleeping.webp", "./img/speaking.webp", "./img/thinking.webp"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});
// Stimmen im Hintergrund speichern: eigener Speicher, der bei Updates bleibt (Dateinamen ändern sich mit dem Inhalt)
async function cacheAudio() {
  try {
    const idx = await (await fetch("./audio/index.json", {cache: "no-cache"})).json();
    const want = new Set(Object.values(idx).map(f => new URL("./audio/" + f, self.registration.scope).href));
    const c = await caches.open(AUDIO_CACHE), have = await c.keys();
    await Promise.all(have.filter(r => !want.has(r.url)).map(r => c.delete(r)));
    const haveSet = new Set(have.map(r => r.url)), todo = [...want].filter(u => !haveSet.has(u));
    for (let i = 0; i < todo.length; i += 8) await Promise.allSettled(todo.slice(i, i + 8).map(u => c.add(u)));
  } catch (err) {}
}
self.addEventListener("message", e => { if (e.data === "cacheAudio") e.waitUntil(cacheAudio()); });
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION && k !== AUDIO_CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()).then(() => { cacheAudio(); }));
});
self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  const fresh = url.origin === location.origin && (req.mode === "navigate" || url.pathname.endsWith(".html") || url.pathname.endsWith(".json") || url.pathname.endsWith("/"));
  if (fresh) {
    // Seite und Lektionen: erst Netz (für Updates), sonst Offline-Kopie
    e.respondWith(fetch(req, {cache: "no-cache"}).then(r => { const c = r.clone(); caches.open(VERSION).then(x => x.put(req, c)); return r; }).catch(() => caches.match(req).then(r => r || caches.match("./index.html"))));
    return;
  }
  // Bilder und Schriften: erst Offline-Kopie, sonst Netz und merken
  // Geschichten direkt vom Netz (Safari braucht dafür Teilabrufe)
  if (/\/audio\/s[^/]*\.mp3$/.test(url.pathname)) return;
  const store = url.pathname.includes("/audio/") ? AUDIO_CACHE : VERSION;
  e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => {
    if (res.ok || res.type === "opaque") { const c = res.clone(); caches.open(store).then(x => x.put(req, c)); }
    return res;
  })));
});
