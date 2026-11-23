"""Erzeugt zu jeder Geschichte aus stories.json zwei durchgehende Hördateien (frei, mit Piper):
  both: Polnisch – Pause – Deutsch – Pause – Polnisch – Pause
  pl:   nur Polnisch mit Pausen
Eine durchgehende Datei läuft auf dem iPhone auch bei gesperrtem Bildschirm weiter.
Schreibt audio/stories.json mit Dateinamen und den Startzeiten jedes Satzes.
"""
import hashlib, json, os, subprocess, sys, tempfile, wave, glob
from piper import PiperVoice
from piper.config import SynthesisConfig

VDIR = sys.argv[1] if len(sys.argv) > 1 else "voices"
VERSION = "1"
RATE = 24000

def load(name):
    p = os.path.join(VDIR, name + ".onnx")
    return PiperVoice.load(p) if os.path.exists(p) else None
PL = load("pl_PL-gosia-medium") or load("pl_PL-darkman-medium")
DE = load("de_DE-thorsten-medium")
if not PL: sys.exit("Keine polnische Stimme.")
PLC = SynthesisConfig(length_scale=1.12)
DEC = SynthesisConfig(length_scale=1.0)

tmp = tempfile.mkdtemp()
cache = {}
def pcm(voice, cfg, text):
    """Text sprechen, als 24-kHz-Mono-PCM zurückgeben."""
    key = (id(voice), text)
    if key in cache: return cache[key]
    raw, out = os.path.join(tmp, "a.wav"), os.path.join(tmp, "b.wav")
    with wave.open(raw, "wb") as w: voice.synthesize_wav(text, w, syn_config=cfg)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", raw, "-ac", "1", "-ar", str(RATE), "-sample_fmt", "s16", out], check=True)
    with wave.open(out) as w: data = w.readframes(w.getnframes())
    cache[key] = data
    return data
sil = lambda s: b"\x00\x00" * int(RATE * s)

S = json.load(open("stories.json", encoding="utf-8"))["stories"]
os.makedirs("audio", exist_ok=True)
outp = "audio/stories.json"
old = json.load(open(outp, encoding="utf-8")) if os.path.exists(outp) else {}
res, keep = {}, set()
for st in S:
    res[st["id"]] = {}
    for mode in (["both", "pl"] if DE else ["pl"]):
        h = hashlib.sha1((VERSION + mode + json.dumps(st["lines"], ensure_ascii=False)).encode()).hexdigest()[:12]
        f = "s" + st["id"] + "-" + mode + "-" + h + ".mp3"
        keep.add(f)
        prev = old.get(st["id"], {}).get(mode)
        if prev and prev.get("f") == f and os.path.exists("audio/" + f):
            res[st["id"]][mode] = prev; continue
        buf, starts = [sil(0.6)], []
        pos = lambda: sum(len(b) for b in buf) / 2 / RATE
        for pl, de in st["lines"]:
            starts.append(round(pos(), 2))
            p = pcm(PL, PLC, pl)
            if mode == "both":
                buf += [p, sil(1.0), pcm(DE, DEC, de), sil(1.0), p, sil(2.2)]
            else:
                buf += [p, sil(1.6)]
        wav = os.path.join(tmp, "s.wav")
        with wave.open(wav, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(b"".join(buf))
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-ac", "1", "-b:a", "48k", "audio/" + f], check=True)
        res[st["id"]][mode] = {"f": f, "t": starts, "d": round(pos(), 1)}
        print("Geschichte", st["id"], mode, res[st["id"]][mode]["d"], "s")
for f in glob.glob("audio/s*-*-*.mp3"):
    if os.path.basename(f) not in keep: os.remove(f)
json.dump(res, open(outp, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
