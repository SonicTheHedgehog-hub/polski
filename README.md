# Polski

Polnisch lernen für Semyon, von null bis B2, nach der Birkenbihl-Methode (Dekodieren, aktives und passives Hören, Anwenden), mit FSRS-Wiederholung und viel Sprechtraining.

Eine installierbare Web-App (PWA) ohne Server. Auf dem iPhone in Safari öffnen › Teilen › **Zum Home-Bildschirm**.

## Aufbau

- `index.html`: die ganze App (Lernweg, Lektionen, Wörter mit FSRS, Hören, Sprechen, Fortschritt)
- `lessons.json`: Kapitel, Lektionen (Dialoge mit Wort-für-Wort-Dekodierung, Aussprache-Hinweise, Grammatik, Wörter, Sprechfragen) und Laut-Training
- `img/`: Wawel-Drache, Icons, Abzeichen, Kapitelbilder
- `sw.js`: Offline-Speicher. **Bei jeder Änderung `VERSION` erhöhen.**

## Stimmen

Die GitHub Action **Stimmen erzeugen** erstellt die Audiodateien in `audio/` automatisch, sobald sich `lessons.json` ändert:
- Standard: **Piper** (Open Source, kostenlos, ohne Konto), Stimmen `pl_PL-gosia-medium` und `pl_PL-darkman-medium` aus rhasspy/piper-voices.
- Optional: **Azure Neural** (Tarif Free F0) über die Secrets `AZURE_SPEECH_KEY` und `AZURE_SPEECH_REGION`.
