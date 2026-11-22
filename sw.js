// Offline-Speicher der App. Bei jeder Änderung VERSION erhöhen.
const VERSION = "polski-v1";
const CORE = ["./", "./index.html", "./lessons.json", "./manifest.webmanifest", "./img/badge-30.webp", "./img/badge-7.webp", "./img/badge-b2.webp", "./img/badge-start.webp", "./img/celebrating.webp", "./img/ch-pierwsze.webp", "./img/ch-przyjaciele.webp", "./img/ch-rodzina.webp", "./img/ch-spoleczenstwo.webp", "./img/flaga.webp", "./img/flying.webp", "./img/happy.webp", "./img/head.webp", "./img/icon-180.png", "./img/icon-192.png", "./img/icon-512.png", "./img/kawa.webp", "./img/krakow.webp", "./img/kwiat.webp", "./img/listening.webp", "./img/mascot.webp", "./img/obwarzanek.webp", "./img/pierogi.webp", "./img/pisanka.webp", "./img/reading.webp", "./img/sleeping.webp", "./img/speaking.webp", "./img/thinking.webp"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(VERSION).then(async c => {
    await c.addAll(CORE);
    // natürliche Stimmen gleich mit speichern, damit sie offline da sind
    try {
      const idx = await (await fetch("./audio/index.json", {cache: "no-cache"})).json();
      await Promise.allSettled([...new Set(Object.values(idx))].map(f => c.add("./audio/" + f)));
    } catch (err) {}
  }).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
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
  e.respondWith(caches.match(req).then(r => r || fetch(req).then(res => {
    if (res.ok || res.type === "opaque") { const c = res.clone(); caches.open(VERSION).then(x => x.put(req, c)); }
    return res;
  })));
});
