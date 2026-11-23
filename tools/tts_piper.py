"""Erzeugt Audiodateien mit Piper (frei, ohne Konto) für alles, was die App vorliest.

Läuft als GitHub Action, wenn kein Azure-Schlüssel hinterlegt ist.
Stimmen: pl_PL-gosia-medium (weiblich) und pl_PL-darkman-medium (männlich) aus rhasspy/piper-voices.
Die Azure-Namen in lessons.json sind nur Rollen; hier werden sie auf Piper-Stimmen abgebildet.
"""
import hashlib, json, os, re, subprocess, sys, tempfile, wave
from piper import PiperVoice
from piper.config import SynthesisConfig

VDIR = sys.argv[1] if len(sys.argv) > 1 else "voices"
D = json.load(open("lessons.json", encoding="utf-8"))
V = D["voices"]; default = V["default"]; me = V["speakers"].get("Semyon", default)

def load(name):
    p = os.path.join(VDIR, name + ".onnx")
    return PiperVoice.load(p) if os.path.exists(p) else None
female = load("pl_PL-gosia-medium"); male = load("pl_PL-darkman-medium")
female = female or male; male = male or female
if not female: sys.exit("Keine Piper-Stimme gefunden.")
ROLES = {
    "pl-PL-ZofiaNeural": (female, SynthesisConfig(length_scale=1.08)),
    "pl-PL-AgnieszkaNeural": (female, SynthesisConfig(length_scale=1.15, noise_scale=0.7)),
    "pl-PL-MarekNeural": (male, SynthesisConfig(length_scale=1.08)),
}

norm_word = lambda w: re.sub(r"[!?.,…]", "", w).strip()
line_text = lambda ln: " ".join(p[0] for p in ln["t"])
items = {}
def add(voice, text):
    text = text.strip()
    if text: items[voice + "|" + text] = (voice, text)
for l in D["lessons"]:
    for ln in l["lines"]:
        add(V["speakers"].get(ln["who"], default), line_text(ln))
        for p in ln["t"]: add(default, norm_word(p[0]))
    for c in l["chunks"]: add(default, c[0])
    for w in l.get("words", []): add(default, w[0])
    for q in l.get("qa", []):
        add(V["speakers"].get(q["who"], default), q["q"]); add(me, q["a"])
for g in D.get("sounds", []):
    for w in g["words"]: add(default, w[0])
if os.path.exists("vocab.json"):
    for pk in json.load(open("vocab.json", encoding="utf-8"))["packs"]:
        for w in pk["words"]:
            add(default, w[0]); add(default, w[3])
            m = re.search(r"pf\.: ([^;]+)", w[5])
            if m: add(default, m.group(1).strip())
if os.path.exists("drills.json"):
    DRL = json.load(open("drills.json", encoding="utf-8"))
    for it in DRL["cases"]["items"]: add(default, it["full"])
    for it in DRL["aspect"]["items"]: add(default, it["full"]); add(default, it["ipf"]); add(default, it["pf"])
    for g in DRL["sounds"]:
        for pr in g["pairs"]:
            for w in pr[:2]: add(default, w); add(me, w)

os.makedirs("audio", exist_ok=True)
idx_path = "audio/index.json"
index = json.load(open(idx_path, encoding="utf-8")) if os.path.exists(idx_path) else {}
made = 0
for key, (voice, text) in items.items():
    if key in index and os.path.exists("audio/" + index[key]): continue
    f = "p" + hashlib.sha1(("piper|" + key).encode()).hexdigest()[:13] + ".mp3"
    pv, cfg = ROLES.get(voice, ROLES["pl-PL-ZofiaNeural"])
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        with wave.open(tmp.name, "wb") as w: pv.synthesize_wav(text, w, syn_config=cfg)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", tmp.name, "-ac", "1", "-ar", "24000", "-b:a", "48k", "audio/" + f], check=True)
    index[key] = f; made += 1
for k in list(index):
    if k not in items:
        try: os.remove("audio/" + index[k])
        except OSError: pass
        del index[k]
json.dump(index, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"Piper: {made} neue Dateien, gesamt {len(index)}.")
