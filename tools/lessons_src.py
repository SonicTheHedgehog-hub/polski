"""Eigene Lektionen, aufgebaut nach den Themen und der Grammatik von „Polski na dobry start“ (Module 1–5).
Alle Dialoge und Sätze sind selbst geschrieben. Ausführen: python3 tools/lessons_src.py
Zeilenformat: (Sprecher, polnischer Satz, Wort-für-Wort mit Leerzeichen getrennt, Sinn, Tipp)"""
import json

NEW = [
 {"id": "b1c", "book": "1C", "title": "Mieszkam w Gdańsku", "de": "Wohnort, Adresse, Telefonnummer", "lines": [
  ("Urzędniczka", "Dzień dobry. Gdzie pan mieszka?", "Tag guter. wo Sie wohnt?", "Guten Tag. Wo wohnen Sie?", ""),
  ("Semyon", "Mieszkam w Gdańsku, na ulicy Długiej.", "wohne-ich in Danzig, auf Straße Langen.", "Ich wohne in Danzig, in der Długa-Straße.", "w Gdańsku: Ort steht im Lokativ"),
  ("Urzędniczka", "A jaki jest pana numer telefonu?", "und welche ist Ihre Nummer Telefons?", "Und wie ist Ihre Telefonnummer?", ""),
  ("Semyon", "Pięćset dwa, trzysta dziesięć, czterysta osiem.", "fünfhundert zwei, dreihundert zehn, vierhundert acht.", "502 310 408.", "Nummern in Dreiergruppen"),
  ("Urzędniczka", "Dziękuję. A pana adres e-mail?", "danke. und Ihre Adresse E-Mail?", "Danke. Und Ihre E-Mail-Adresse?", ""),
  ("Semyon", "Semyon małpa poczta kropka pl.", "Semyon Affe post Punkt pl.", "semyon@poczta.pl", "@ heißt małpa (Affe)")],
  "chunks": [("Gdzie mieszkasz?", "Wo wohnst du?"), ("Mieszkam w Gdańsku.", "Ich wohne in Danzig."), ("na ulicy Długiej", "in der Długa-Straße"), ("Jaki jest twój numer telefonu?", "Wie ist deine Telefonnummer?"), ("Jaki jest twój adres?", "Wie ist deine Adresse?")],
  "words": [("urzędniczka", "Beamtin"), ("ulica", "Straße"), ("numer", "Nummer"), ("adres", "Adresse"), ("małpa", "Affe; @"), ("kropka", "Punkt")],
  "qa": [("Urzędniczka", "Gdzie pan mieszka?", "Wo wohnen Sie?", "Mieszkam w Gdańsku.", "Ich wohne in Danzig."), ("Ola", "Jaki jest twój numer telefonu?", "Wie ist deine Telefonnummer?", "Mój numer to pięćset dwa, trzysta dziesięć, czterysta osiem.", "Meine Nummer ist 502 310 408.")],
  "grammar": ("w + Lokativ: wo?", "Nach w (in) für einen Ort steht der Lokativ. Städte enden dann meist auf -ie oder -u: Berlin → w Berlinie, Kraków → w Krakowie, Gdańsk → w Gdańsku, Warszawa → w Warszawie. Bei Straßen sagt man na: na ulicy Długiej. Das Verb mieszkać: mieszkam, mieszkasz, mieszka, mieszkamy, mieszkacie, mieszkają."),
  "tips": ["Telefonnummern liest man in Dreiergruppen: 502 310 408 = pięćset dwa, trzysta dziesięć, czterysta osiem.", "Höflich fragt man mit pan (zu einem Mann) oder pani (zu einer Frau) und der 3. Person: Gdzie pan mieszka?"]},

 {"id": "b1d", "book": "1D", "title": "Co to jest?", "de": "Dinge benennen: ten, ta, to", "lines": [
  ("Ola", "Co to jest?", "was das ist?", "Was ist das?", "co ≈ tso"),
  ("Semyon", "To jest klucz. A to?", "das ist Schlüssel. und das?", "Das ist ein Schlüssel. Und das?", ""),
  ("Ola", "To jest mój telefon, a to moja książka.", "das ist mein Telefon, und das meine Buch.", "Das ist mein Telefon, und das ist mein Buch.", ""),
  ("Semyon", "A kto to jest na zdjęciu?", "und wer das ist auf Foto?", "Und wer ist das auf dem Foto?", "kto für Menschen, co für Dinge"),
  ("Ola", "To moja siostra, Kasia.", "das meine Schwester, Kasia.", "Das ist meine Schwester Kasia.", ""),
  ("Semyon", "Ta torba jest bardzo ładna!", "diese Tasche ist sehr hübsch!", "Die Tasche ist sehr hübsch!", ""),
  ("Ola", "Dziękuję, to prezent od mamy.", "danke, das Geschenk von Mama.", "Danke, das ist ein Geschenk von Mama.", "")],
  "chunks": [("Co to jest?", "Was ist das?"), ("Kto to jest?", "Wer ist das?"), ("To jest mój telefon.", "Das ist mein Telefon."), ("na zdjęciu", "auf dem Foto"), ("prezent od mamy", "ein Geschenk von Mama")],
  "words": [("klucz", "Schlüssel"), ("książka", "Buch"), ("torba", "Tasche"), ("zdjęcie", "Foto"), ("prezent", "Geschenk"), ("od", "von")],
  "qa": [("Ola", "Co to jest?", "Was ist das?", "To jest mój telefon.", "Das ist mein Telefon."), ("Ola", "Kto to jest?", "Wer ist das?", "To jest moja siostra.", "Das ist meine Schwester.")],
  "grammar": ("Drei Geschlechter: ten, ta, to", "Männlich enden Nomen meist auf einen Konsonanten: ten telefon, ten klucz. Weiblich meist auf -a: ta torba, ta książka. Sächlich auf -o, -e oder -ę: to okno, to zdjęcie. Danach richten sich mein und dieser: mój telefon, moja torba, moje zdjęcie. „To jest …“ (das ist …) bleibt immer gleich."),
  "tips": ["In „To moja siostra“ darf jest wegfallen, das ist umgangssprachlich ganz normal.", "zdjęcie ≈ SDJEN-tsche, ę vor ć klingt wie „en“."]},

 {"id": "b2b", "book": "2B", "title": "Jaki on jest?", "de": "Menschen beschreiben, Befinden", "lines": [
  ("Ola", "Jak się czujesz? Jesteś zmęczony?", "wie sich fühlst-du? bist-du müde?", "Wie fühlst du dich? Bist du müde?", ""),
  ("Semyon", "Trochę. Ale jestem zadowolony, bo mam nowego kolegę w pracy.", "bisschen. aber bin-ich zufrieden, weil habe-ich neuen Kollegen in Arbeit.", "Ein bisschen. Aber ich bin zufrieden, weil ich einen neuen Kollegen auf der Arbeit habe.", "nowego kolegę: Akkusativ, belebt"),
  ("Ola", "Jaki on jest?", "was-für-einer er ist?", "Wie ist er so?", ""),
  ("Semyon", "Jest wysoki, ma ciemne włosy i jest bardzo miły.", "ist-er groß, hat-er dunkle Haare und ist-er sehr nett.", "Er ist groß, hat dunkle Haare und ist sehr nett.", ""),
  ("Ola", "A ile ma lat?", "und wie-viel hat-er Jahre?", "Und wie alt ist er?", "Alter mit mieć"),
  ("Semyon", "Ma trzydzieści lat. Jest spokojny i zabawny.", "hat-er dreißig Jahre. ist-er ruhig und lustig.", "Er ist dreißig. Er ist ruhig und lustig.", "")],
  "chunks": [("Jak się czujesz?", "Wie fühlst du dich?"), ("Jestem zmęczony.", "Ich bin müde."), ("Jaki on jest?", "Wie ist er (so)?"), ("Ile masz lat?", "Wie alt bist du?"), ("ma ciemne włosy", "er hat dunkle Haare")],
  "words": [("zmęczony", "müde"), ("zadowolony", "zufrieden"), ("wysoki", "groß"), ("ciemny", "dunkel"), ("włosy", "Haare"), ("spokojny", "ruhig"), ("zabawny", "lustig")],
  "qa": [("Ola", "Jak się czujesz?", "Wie fühlst du dich?", "Jestem trochę zmęczony, ale zadowolony.", "Ich bin etwas müde, aber zufrieden."), ("Ola", "Jaki jest twój brat?", "Wie ist dein Bruder?", "Mój brat jest wysoki i bardzo miły.", "Mein Bruder ist groß und sehr nett.")],
  "grammar": ("Adjektive passen sich an", "Das Adjektiv richtet sich nach dem Nomen: on jest miły (er), ona jest miła (sie), dziecko jest miłe (es). Im Plural bei Dingen und Frauen -e: ciemne włosy. Fragen: Jaki? (welcher, wie), jaka?, jakie? Das Alter sagt man mit haben: Mam trzydzieści lat (wörtlich: ich habe 30 Jahre)."),
  "tips": ["Als Frau sagt man: jestem zmęczona, jestem zadowolona.", "Nach 5 und mehr kommt lat: dwa lata, pięć lat, trzydzieści lat."]},

 {"id": "b2c", "book": "2C", "title": "Kim jesteś z zawodu?", "de": "Berufe und der Instrumental", "lines": [
  ("Ola", "Kim jesteś z zawodu?", "wer bist-du von Beruf?", "Was bist du von Beruf?", "kim: Instrumental von kto"),
  ("Semyon", "Jestem inżynierem. A ty?", "bin-ich Ingenieur. und du?", "Ich bin Ingenieur. Und du?", "inżynier → inżynierem"),
  ("Ola", "Jestem nauczycielką. Uczę angielskiego w szkole.", "bin-ich Lehrerin. lehre-ich Englisch in Schule.", "Ich bin Lehrerin. Ich unterrichte Englisch in der Schule.", ""),
  ("Semyon", "A twój brat?", "und dein Bruder?", "Und dein Bruder?", ""),
  ("Ola", "Mój brat jest kucharzem, a jego żona jest lekarką.", "mein Bruder ist Koch, und seine Frau ist Ärztin.", "Mein Bruder ist Koch, und seine Frau ist Ärztin.", ""),
  ("Semyon", "Kucharz w rodzinie to świetny pomysł!", "Koch in Familie das toll Idee!", "Ein Koch in der Familie ist eine tolle Idee!", "")],
  "chunks": [("Kim jesteś z zawodu?", "Was bist du von Beruf?"), ("Jestem inżynierem.", "Ich bin Ingenieur."), ("Jestem nauczycielką.", "Ich bin Lehrerin."), ("Uczę angielskiego.", "Ich unterrichte Englisch."), ("To świetny pomysł!", "Das ist eine tolle Idee!")],
  "words": [("zawód", "Beruf"), ("inżynier", "Ingenieur"), ("nauczycielka", "Lehrerin"), ("kucharz", "Koch"), ("lekarka", "Ärztin"), ("świetny", "toll")],
  "qa": [("Ola", "Kim jesteś z zawodu?", "Was bist du von Beruf?", "Jestem inżynierem.", "Ich bin Ingenieur."), ("Ola", "Kim jest twój brat?", "Was ist dein Bruder von Beruf?", "Mój brat jest kucharzem.", "Mein Bruder ist Koch.")],
  "grammar": ("być + Instrumental", "Nach być (sein) steht der Beruf im Instrumental. Männlich -em, nach k und g -iem: lekarz → lekarzem, informatyk → informatykiem. Weiblich -ą: nauczycielka → nauczycielką. Aber nach to bleibt der Nominativ: To jest lekarz. Viele Berufe bekommen für Frauen -ka: nauczyciel → nauczycielka, lekarz → lekarka."),
  "tips": ["Wer bist du? heißt Kim jesteś? nur bei Beruf oder Rolle. Nach dem Namen fragt man: Jak się nazywasz?", "uczyć + Genitiv: uczę angielskiego, uczę polskiego."]},

 {"id": "b2d", "book": "2D", "title": "Gdzie pracujesz?", "de": "Arbeitsort und Arbeitszeit", "lines": [
  ("Ola", "Gdzie pracujesz?", "wo arbeitest-du?", "Wo arbeitest du?", "pracować → pracuję"),
  ("Semyon", "Pracuję w dużej firmie w centrum.", "arbeite-ich in großer Firma in Zentrum.", "Ich arbeite in einer großen Firma im Zentrum.", ""),
  ("Ola", "Pracujesz od poniedziałku do piątku?", "arbeitest-du von Montag bis Freitag?", "Arbeitest du von Montag bis Freitag?", "od, do + Genitiv"),
  ("Semyon", "Tak, od ósmej do szesnastej.", "ja, von achten bis sechzehnten.", "Ja, von acht bis sechzehn Uhr.", ""),
  ("Ola", "A w weekend?", "und in Wochenende?", "Und am Wochenende?", ""),
  ("Semyon", "Czasem muszę pracować w sobotę.", "manchmal muss-ich arbeiten in Samstag.", "Manchmal muss ich samstags arbeiten.", "muszę + Infinitiv"),
  ("Ola", "Biedny! Ja w sobotę odpoczywam.", "Armer! ich in Samstag ruhe-mich-aus.", "Du Armer! Ich ruhe mich samstags aus.", "")],
  "chunks": [("Gdzie pracujesz?", "Wo arbeitest du?"), ("od poniedziałku do piątku", "von Montag bis Freitag"), ("od ósmej do szesnastej", "von acht bis sechzehn Uhr"), ("Muszę pracować.", "Ich muss arbeiten."), ("w sobotę", "am Samstag")],
  "words": [("firma", "Firma"), ("centrum", "Zentrum"), ("czasem", "manchmal"), ("musieć", "müssen"), ("odpoczywać", "sich ausruhen"), ("biedny", "arm")],
  "qa": [("Ola", "Gdzie pracujesz?", "Wo arbeitest du?", "Pracuję w dużej firmie.", "Ich arbeite in einer großen Firma."), ("Ola", "Od której do której pracujesz?", "Von wann bis wann arbeitest du?", "Pracuję od ósmej do szesnastej.", "Ich arbeite von acht bis sechzehn Uhr.")],
  "grammar": ("Verben auf -ować und od … do", "Bei Verben auf -ować wird -owa- zu -uj-: pracować → pracuję, pracujesz, pracuje, pracujemy, pracujecie, pracują. Genauso kupować → kupuję. Eine Zeitspanne: od … do … mit Genitiv: od poniedziałku do piątku, od ósmej do szesnastej. Am Wochentag: w + Akkusativ: w sobotę, w poniedziałek. musieć + Infinitiv: muszę pracować."),
  "tips": ["Uhrzeiten sind im Polnischen Ordnungszahlen: o ósmej = um acht (wörtlich: um der achten).", "czasem und czasami bedeuten beide manchmal."]},

 {"id": "b3a", "book": "3A", "title": "Gdzie jest piekarnia?", "de": "Nach dem Weg fragen", "lines": [
  ("Semyon", "Przepraszam, gdzie jest najbliższa piekarnia?", "Entschuldigung, wo ist nächste Bäckerei?", "Entschuldigung, wo ist die nächste Bäckerei?", ""),
  ("Pani", "Proszę iść prosto, a potem w lewo.", "bitte gehen geradeaus, und dann nach links.", "Gehen Sie geradeaus und dann links.", "Proszę + Infinitiv = höflich"),
  ("Semyon", "Czy to daleko?", "ob das weit?", "Ist das weit?", ""),
  ("Pani", "Nie, blisko. Pięć minut pieszo.", "nein, nah. fünf Minuten zu-Fuß.", "Nein, nah. Fünf Minuten zu Fuß.", ""),
  ("Semyon", "A apteka?", "und Apotheke?", "Und eine Apotheke?", ""),
  ("Pani", "Apteka jest obok piekarni, naprzeciwko poczty.", "Apotheke ist neben Bäckerei, gegenüber Post.", "Die Apotheke ist neben der Bäckerei, gegenüber der Post.", "obok, naprzeciwko + Genitiv"),
  ("Semyon", "Dziękuję bardzo!", "danke sehr!", "Vielen Dank!", "")],
  "chunks": [("Gdzie jest apteka?", "Wo ist eine Apotheke?"), ("Proszę iść prosto.", "Gehen Sie geradeaus."), ("potem w lewo", "dann links"), ("Czy to daleko?", "Ist das weit?"), ("obok piekarni", "neben der Bäckerei")],
  "words": [("piekarnia", "Bäckerei"), ("najbliższy", "nächster"), ("pieszo", "zu Fuß"), ("obok", "neben"), ("naprzeciwko", "gegenüber"), ("poczta", "Post")],
  "qa": [("Pani", "Czego pan szuka?", "Was suchen Sie?", "Szukam apteki.", "Ich suche eine Apotheke."), ("Ola", "Gdzie jest piekarnia?", "Wo ist die Bäckerei?", "Proszę iść prosto, a potem w lewo.", "Geh geradeaus und dann links.")],
  "grammar": ("Ortsangaben mit Genitiv", "Nach obok (neben), naprzeciwko (gegenüber), blisko (nahe bei) und koło (bei) steht der Genitiv: obok piekarni, naprzeciwko poczty, blisko domu. Auch szukać (suchen) braucht den Genitiv: szukam apteki. Proszę + Infinitiv ist eine höfliche Aufforderung: Proszę iść prosto, proszę skręcić w prawo."),
  "tips": ["w lewo = nach links, w prawo = nach rechts, prosto = geradeaus.", "najbliższy ≈ naj-BLISCH-schy, ż klingt wie das j in „Journal“."]},

 {"id": "b3c", "book": "3C", "title": "Ile kosztuje?", "de": "Preise und Mengen", "lines": [
  ("Semyon", "Ile kosztują te pomidory?", "wie-viel kosten diese Tomaten?", "Wie viel kosten diese Tomaten?", ""),
  ("Sprzedawczyni", "Osiem złotych za kilogram.", "acht Złoty für Kilogramm.", "Acht Złoty pro Kilo.", "5+ złotych"),
  ("Semyon", "Poproszę pół kilo. I jeszcze dziesięć jajek.", "bitte halbes Kilo. und noch zehn Eier.", "Ein halbes Kilo, bitte. Und noch zehn Eier.", "dziesięć jajek: Genitiv Plural"),
  ("Sprzedawczyni", "Coś jeszcze?", "etwas noch?", "Sonst noch etwas?", ""),
  ("Semyon", "Tak, butelkę wody i paczkę herbaty.", "ja, Flasche Wassers und Packung Tees.", "Ja, eine Flasche Wasser und eine Packung Tee.", ""),
  ("Sprzedawczyni", "Razem dwadzieścia trzy złote pięćdziesiąt groszy.", "zusammen zwanzig drei Złoty fünfzig Groschen.", "Zusammen 23,50 Złoty.", "2–4 złote")],
  "chunks": [("Ile kosztuje?", "Was kostet das?"), ("za kilogram", "pro Kilo"), ("pół kilo", "ein halbes Kilo"), ("butelka wody", "eine Flasche Wasser"), ("Coś jeszcze?", "Sonst noch etwas?")],
  "words": [("pomidor", "Tomate"), ("kilogram", "Kilogramm"), ("pół", "halb"), ("butelka", "Flasche"), ("paczka", "Packung"), ("razem", "zusammen")],
  "qa": [("Sprzedawczyni", "Co podać?", "Was darf es sein?", "Poproszę pół kilo pomidorów.", "Ein halbes Kilo Tomaten, bitte."), ("Sprzedawczyni", "Coś jeszcze?", "Sonst noch etwas?", "Tak, butelkę wody, proszę.", "Ja, eine Flasche Wasser, bitte.")],
  "grammar": ("Zahlen und Złoty", "Nach 1 steht złoty, nach 2, 3, 4 złote, ab 5 złotych. Genauso grosz, grosze, groszy. Nach Mengen steht der Genitiv: butelka wody, paczka herbaty, kilo pomidorów, dziesięć jajek. Mit poproszę steht das, was man möchte, im Akkusativ: poproszę butelkę wody."),
  "tips": ["Bei Preisen sagt man oft nur die Zahlen: dwadzieścia trzy pięćdziesiąt.", "jajek ≈ JA-jek, der Plural von jajko ist jajka, nach Zahlen ab 5 jajek."]},

 {"id": "b3d", "book": "3D", "title": "Na targu", "de": "Auf dem Markt: billiger, teurer, lieber", "lines": [
  ("Ola", "Lubisz robić zakupy na targu?", "magst-du machen Einkäufe auf Markt?", "Kaufst du gern auf dem Markt ein?", ""),
  ("Semyon", "Bardzo! Na targu warzywa są tańsze niż w supermarkecie.", "sehr! auf Markt Gemüse sind billiger als in Supermarkt.", "Sehr! Auf dem Markt ist Gemüse billiger als im Supermarkt.", "tańszy = billiger"),
  ("Ola", "I smaczniejsze. Spójrz, jakie piękne truskawki!", "und leckerer. schau, was-für schöne Erdbeeren!", "Und leckerer. Schau, was für schöne Erdbeeren!", ""),
  ("Semyon", "Ale są droższe niż jabłka.", "aber sind-sie teurer als Äpfel.", "Aber sie sind teurer als Äpfel.", "droższy = teurer"),
  ("Ola", "Trudno. Wolę truskawki od jabłek.", "schwer. bevorzuge-ich Erdbeeren vor Äpfeln.", "Egal. Ich mag Erdbeeren lieber als Äpfel.", "trudno = da kann man nichts machen"),
  ("Semyon", "Dobrze, kupmy jedno i drugie.", "gut, kaufen-wir eins und anderes.", "Gut, kaufen wir beides.", "")],
  "chunks": [("robić zakupy", "einkaufen"), ("tańsze niż w supermarkecie", "billiger als im Supermarkt"), ("Wolę truskawki.", "Ich mag lieber Erdbeeren."), ("Trudno.", "Da kann man nichts machen."), ("jedno i drugie", "beides")],
  "words": [("targ", "Markt"), ("tańszy", "billiger"), ("droższy", "teurer"), ("truskawka", "Erdbeere"), ("niż", "als"), ("woleć", "lieber mögen")],
  "qa": [("Ola", "Co wolisz: truskawki czy jabłka?", "Was magst du lieber: Erdbeeren oder Äpfel?", "Wolę truskawki.", "Ich mag lieber Erdbeeren."), ("Ola", "Gdzie jest taniej: na targu czy w supermarkecie?", "Wo ist es billiger: auf dem Markt oder im Supermarkt?", "Na targu jest taniej.", "Auf dem Markt ist es billiger.")],
  "grammar": ("Steigern: tańszy, droższy", "Die Steigerung endet meist auf -szy oder -ejszy: tani → tańszy, drogi → droższy, smaczny → smaczniejszy. Unregelmäßig: dobry → lepszy, zły → gorszy. „Als“ heißt niż: tańsze niż jabłka. woleć heißt lieber mögen: wolę, wolisz, woli. Wolę X od Y: Y steht im Genitiv."),
  "tips": ["Beim Adverb: taniej (billiger), drożej (teurer), lepiej (besser).", "truskawki ≈ tru-SKAF-ki, w vor k klingt wie f."]},

 {"id": "b4a", "book": "4A", "title": "Śniadanie w barze", "de": "Frühstück bestellen: jeść, pić, wie oft", "lines": [
  ("Kelnerka", "Dzień dobry, co dla pana?", "Tag guter, was für Sie?", "Guten Tag, was darf es für Sie sein?", ""),
  ("Semyon", "Poproszę jajecznicę i bułkę z masłem.", "bitte Rührei und Brötchen mit Butter.", "Ein Rührei und ein Brötchen mit Butter, bitte.", ""),
  ("Kelnerka", "Do picia kawa czy herbata?", "zum Trinken Kaffee oder Tee?", "Zum Trinken Kaffee oder Tee?", ""),
  ("Semyon", "Kawę z mlekiem, proszę. Rano zawsze piję kawę.", "Kaffee mit Milch, bitte. morgens immer trinke-ich Kaffee.", "Kaffee mit Milch, bitte. Morgens trinke ich immer Kaffee.", ""),
  ("Kelnerka", "Coś słodkiego? Mamy świeże pączki.", "etwas Süßes? haben-wir frische Krapfen.", "Etwas Süßes? Wir haben frische Krapfen.", "pączek = Berliner"),
  ("Semyon", "Czasem jem pączki, ale dziś nie, dziękuję.", "manchmal esse-ich Krapfen, aber heute nicht, danke.", "Manchmal esse ich Krapfen, aber heute nicht, danke.", "")],
  "chunks": [("Co dla pana?", "Was darf es sein?"), ("bułka z masłem", "Brötchen mit Butter"), ("do picia", "zum Trinken"), ("Rano zawsze piję kawę.", "Morgens trinke ich immer Kaffee."), ("coś słodkiego", "etwas Süßes")],
  "words": [("jajecznica", "Rührei"), ("bułka", "Brötchen"), ("masło", "Butter"), ("pączek", "Krapfen"), ("świeży", "frisch"), ("rzadko", "selten")],
  "qa": [("Kelnerka", "Co pan pije rano?", "Was trinken Sie morgens?", "Rano zawsze piję kawę.", "Morgens trinke ich immer Kaffee."), ("Ola", "Często jesz pączki?", "Isst du oft Krapfen?", "Nie, rzadko jem pączki.", "Nein, ich esse selten Krapfen.")],
  "grammar": ("jeść, pić und wie oft", "jeść (essen): jem, jesz, je, jemy, jecie, jedzą. pić (trinken): piję, pijesz, pije, pijemy, pijecie, piją. Wie oft: zawsze (immer), często (oft), czasem (manchmal), rzadko (selten), nigdy nie (nie): Nigdy nie piję kawy. Achtung: Nach Verneinung steht der Genitiv (kawy statt kawę)."),
  "tips": ["Ein Bar mleczny oder Bar ist in Polen oft eine einfache Kantine, keine Kneipe.", "pączki ≈ PONTSCH-ki, ą vor cz klingt wie „on“."]},

 {"id": "b4b", "book": "4B", "title": "W restauracji", "de": "Mittagessen bestellen, nie ma + Genitiv", "lines": [
  ("Kelnerka", "Czy mogę przyjąć zamówienie?", "ob kann-ich annehmen Bestellung?", "Darf ich Ihre Bestellung aufnehmen?", ""),
  ("Semyon", "Tak. Na pierwsze danie poproszę żurek.", "ja. auf erstes Gericht bitte Żurek.", "Ja. Als Vorspeise bitte einen Żurek.", "żurek = saure Mehlsuppe"),
  ("Kelnerka", "Przykro mi, dziś nie ma żurku. Polecam barszcz.", "leid mir, heute nicht gibt Żurek. empfehle-ich Barszcz.", "Tut mir leid, heute gibt es keinen Żurek. Ich empfehle Barszcz.", "nie ma + Genitiv"),
  ("Semyon", "Dobrze, to barszcz. A na drugie danie schabowy z ziemniakami.", "gut, dann Barszcz. und auf zweites Gericht Schnitzel mit Kartoffeln.", "Gut, dann Barszcz. Und als Hauptgericht ein Schnitzel mit Kartoffeln.", ""),
  ("Kelnerka", "A do picia?", "und zum Trinken?", "Und zum Trinken?", ""),
  ("Semyon", "Sok jabłkowy, ale bez lodu.", "Saft Apfel-, aber ohne Eis.", "Apfelsaft, aber ohne Eis.", "bez + Genitiv")],
  "chunks": [("na pierwsze danie", "als Vorspeise (Suppe)"), ("na drugie danie", "als Hauptgericht"), ("Przykro mi.", "Tut mir leid."), ("Nie ma żurku.", "Es gibt keinen Żurek."), ("bez lodu", "ohne Eis")],
  "words": [("zamówienie", "Bestellung"), ("żurek", "saure Mehlsuppe"), ("barszcz", "Rote-Bete-Suppe"), ("schabowy", "Schweineschnitzel"), ("polecać", "empfehlen"), ("lód", "Eis")],
  "qa": [("Kelnerka", "Co pan zamawia?", "Was bestellen Sie?", "Poproszę barszcz i schabowy.", "Barszcz und ein Schnitzel, bitte."), ("Kelnerka", "Z lodem czy bez lodu?", "Mit oder ohne Eis?", "Bez lodu, proszę.", "Ohne Eis, bitte.")],
  "grammar": ("nie ma + Genitiv", "„Es gibt nicht“ heißt nie ma, danach steht der Genitiv: nie ma żurku, nie ma kawy, nie ma mleka. Auch nach bez (ohne) kommt der Genitiv: bez lodu, bez cukru. Bei manchen Wörtern fällt das e weg: żurek → żurku, lód → lodu."),
  "tips": ["Ein polnisches Mittagessen hat oft zwei Gänge: erst Suppe (pierwsze danie), dann Hauptgericht (drugie danie).", "barszcz ≈ BAR-schtsch."]},

 {"id": "b4d", "book": "4D", "title": "Na wynos", "de": "Essen zum Mitnehmen, bezahlen", "lines": [
  ("Kasjerka", "Na miejscu czy na wynos?", "auf Ort oder zum Mitnehmen?", "Hier essen oder zum Mitnehmen?", ""),
  ("Semyon", "Na wynos. Poproszę zapiekankę i dwie kawy.", "zum Mitnehmen. bitte Zapiekanka und zwei Kaffees.", "Zum Mitnehmen. Eine Zapiekanka und zwei Kaffee, bitte.", "zapiekanka = überbackenes Baguette"),
  ("Kasjerka", "Duże czy małe?", "große oder kleine?", "Groß oder klein?", ""),
  ("Semyon", "Jedną dużą i jedną małą.", "eine große und eine kleine.", "Einen großen und einen kleinen.", "Akkusativ weiblich: -ą"),
  ("Kasjerka", "Płaci pan kartą czy gotówką?", "zahlt Sie mit-Karte oder bar?", "Zahlen Sie mit Karte oder bar?", "Instrumental: womit?"),
  ("Semyon", "Telefonem, jeśli można.", "mit-Telefon, wenn man-kann.", "Mit dem Handy, wenn das geht.", ""),
  ("Kasjerka", "Oczywiście. Proszę przyłożyć telefon tutaj.", "natürlich. bitte anhalten Telefon hier.", "Natürlich. Halten Sie das Handy bitte hier dran.", "")],
  "chunks": [("Na miejscu czy na wynos?", "Hier essen oder zum Mitnehmen?"), ("dwie kawy", "zwei Kaffee"), ("kartą czy gotówką", "mit Karte oder bar"), ("jeśli można", "wenn das geht"), ("Proszę przyłożyć telefon.", "Halten Sie das Handy dran.")],
  "words": [("na wynos", "zum Mitnehmen"), ("na miejscu", "hier (essen)"), ("zapiekanka", "überbackenes Baguette"), ("gotówka", "Bargeld"), ("można", "man kann; es geht"), ("przyłożyć", "anhalten, auflegen")],
  "qa": [("Kasjerka", "Na miejscu czy na wynos?", "Hier essen oder zum Mitnehmen?", "Na wynos, proszę.", "Zum Mitnehmen, bitte."), ("Kasjerka", "Jak pan płaci?", "Wie zahlen Sie?", "Kartą, proszę.", "Mit Karte, bitte.")],
  "grammar": ("Womit? Instrumental", "Womit man etwas tut, steht im Instrumental: płacę kartą, gotówką, telefonem; jadę tramwajem. Weiblich -ą, männlich und sächlich -em. Bei Zahlen: jedna kawa, dwie kawy (2–4 weiblich: dwie), pięć kaw. Weibliche Adjektive im Akkusativ enden auf -ą: jedną dużą kawę."),
  "tips": ["Kontaktlos mit Handy oder Karte zu zahlen ist in Polen fast überall üblich.", "gotówką ≈ go-TUF-kom, ó klingt wie u."]},

 {"id": "b5b", "book": "5B", "title": "Mój pokój", "de": "Möbel: steht, liegt, hängt", "lines": [
  ("Ola", "Twój pokój jest ładny! Gdzie śpisz?", "dein Zimmer ist hübsch! wo schläfst-du?", "Dein Zimmer ist hübsch! Wo schläfst du?", ""),
  ("Semyon", "Łóżko stoi pod oknem, a obok jest szafa.", "Bett steht unter Fenster, und daneben ist Schrank.", "Das Bett steht unter dem Fenster, und daneben ist der Schrank.", "pod + Instrumental"),
  ("Ola", "A gdzie pracujesz?", "und wo arbeitest-du?", "Und wo arbeitest du?", ""),
  ("Semyon", "Przy biurku. Biurko stoi między szafą a regałem.", "an Schreibtisch. Schreibtisch steht zwischen Schrank und Regal.", "Am Schreibtisch. Er steht zwischen Schrank und Regal.", "między … a …"),
  ("Ola", "Ładny obraz! Wisi nad kanapą.", "schönes Bild! hängt-es über Sofa.", "Schönes Bild! Es hängt über dem Sofa.", ""),
  ("Semyon", "A na podłodze leży dywan od babci.", "und auf Boden liegt Teppich von Oma.", "Und auf dem Boden liegt ein Teppich von Oma.", "na + Lokativ")],
  "chunks": [("Łóżko stoi pod oknem.", "Das Bett steht unter dem Fenster."), ("przy biurku", "am Schreibtisch"), ("między szafą a regałem", "zwischen Schrank und Regal"), ("Obraz wisi nad kanapą.", "Das Bild hängt über dem Sofa."), ("na podłodze", "auf dem Boden")],
  "words": [("biurko", "Schreibtisch"), ("regał", "Regal"), ("obraz", "Bild"), ("wisieć", "hängen"), ("leżeć", "liegen"), ("dywan", "Teppich")],
  "qa": [("Ola", "Gdzie stoi łóżko?", "Wo steht das Bett?", "Łóżko stoi pod oknem.", "Das Bett steht unter dem Fenster."), ("Ola", "Co wisi nad kanapą?", "Was hängt über dem Sofa?", "Nad kanapą wisi obraz.", "Über dem Sofa hängt ein Bild.")],
  "grammar": ("stoi, leży, wisi und Präpositionen", "Wie im Deutschen: stać (stehen), leżeć (liegen), wisieć (hängen): stoi, leży, wisi. Nach w, na, przy (wo?) steht der Lokativ: na podłodze, w szafie, przy biurku. Nach pod, nad, przed, za, między steht der Instrumental: pod oknem, nad kanapą, między szafą a regałem."),
  "tips": ["Zwischen A und B: między A a B, beide im Instrumental.", "łóżko ≈ WUSCH-ko, ł klingt wie englisches w."]},

 {"id": "b5c", "book": "5C", "title": "Szukam mieszkania", "de": "Eine Wohnung mieten: chcieć + Infinitiv", "lines": [
  ("Semyon", "Dzień dobry, dzwonię w sprawie ogłoszenia. Mieszkanie jest jeszcze wolne?", "Tag guter, rufe-ich-an in Sache Anzeige. Wohnung ist noch frei?", "Guten Tag, ich rufe wegen der Anzeige an. Ist die Wohnung noch frei?", "w sprawie + Genitiv = wegen"),
  ("Pani Anna", "Tak. Ma dwa pokoje, kuchnię i balkon.", "ja. hat-sie zwei Zimmer, Küche und Balkon.", "Ja. Sie hat zwei Zimmer, eine Küche und einen Balkon.", ""),
  ("Semyon", "Ile wynosi czynsz?", "wie-viel beträgt Miete?", "Wie hoch ist die Miete?", ""),
  ("Pani Anna", "Dwa tysiące złotych miesięcznie plus media.", "zwei tausend Złoty monatlich plus Nebenkosten.", "Zweitausend Złoty im Monat plus Nebenkosten.", "media = Strom, Wasser, Gas"),
  ("Semyon", "Chcę je zobaczyć. Kiedy mogę przyjść?", "will-ich sie sehen. wann kann-ich kommen?", "Ich möchte sie ansehen. Wann kann ich kommen?", "chcę + Infinitiv"),
  ("Pani Anna", "Jutro o osiemnastej, dobrze?", "morgen um achtzehnten, gut?", "Morgen um achtzehn Uhr, passt das?", "")],
  "chunks": [("w sprawie ogłoszenia", "wegen der Anzeige"), ("Mieszkanie jest wolne.", "Die Wohnung ist frei."), ("Ile wynosi czynsz?", "Wie hoch ist die Miete?"), ("Chcę je zobaczyć.", "Ich möchte sie ansehen."), ("Kiedy mogę przyjść?", "Wann kann ich kommen?")],
  "words": [("ogłoszenie", "Anzeige"), ("wolny", "frei"), ("czynsz", "Miete"), ("miesięcznie", "monatlich"), ("media", "Nebenkosten"), ("wynająć", "mieten")],
  "qa": [("Pani Anna", "Czego pan szuka?", "Was suchen Sie?", "Szukam mieszkania.", "Ich suche eine Wohnung."), ("Pani Anna", "Kiedy chce pan zobaczyć mieszkanie?", "Wann möchten Sie die Wohnung ansehen?", "Chcę je zobaczyć jutro.", "Ich möchte sie morgen ansehen.")],
  "grammar": ("chcieć und móc + Infinitiv", "chcieć (wollen): chcę, chcesz, chce, chcemy, chcecie, chcą. móc (können): mogę, możesz, może, możemy, możecie, mogą. Danach folgt der Infinitiv: chcę wynająć mieszkanie, mogę przyjść. „je“ ist das Akkusativ-Pronomen für ein sächliches Wort (mieszkanie): Chcę je zobaczyć. szukać braucht den Genitiv: szukam mieszkania."),
  "tips": ["Bei Wohnungen fragt man oft: Ile metrów? (Wie viele Quadratmeter?)", "czynsz ≈ tschynsch, wie das deutsche „Zins“."]},

 {"id": "b5d", "book": "5D", "title": "Moja okolica", "de": "Die Nachbarschaft: iść und jechać", "lines": [
  ("Ola", "Jak jest w twojej okolicy?", "wie ist in deiner Gegend?", "Wie ist es in deiner Gegend?", ""),
  ("Semyon", "Bardzo spokojnie. Blisko jest park i duży sklep.", "sehr ruhig. nah ist Park und großer Laden.", "Sehr ruhig. In der Nähe gibt es einen Park und einen großen Laden.", ""),
  ("Ola", "A przystanek?", "und Haltestelle?", "Und eine Haltestelle?", ""),
  ("Semyon", "Przystanek jest za rogiem. Do centrum jadę tramwajem dziesięć minut.", "Haltestelle ist hinter Ecke. zu Zentrum fahre-ich mit-Straßenbahn zehn Minuten.", "Die Haltestelle ist um die Ecke. Ins Zentrum fahre ich zehn Minuten mit der Straßenbahn.", "jadę = ich fahre"),
  ("Ola", "Super. Idziemy na spacer po twojej okolicy?", "super. gehen-wir auf Spaziergang durch deine Gegend?", "Super. Machen wir einen Spaziergang durch deine Gegend?", "idziemy = wir gehen"),
  ("Semyon", "Chętnie! Idę po kurtkę.", "gern! gehe-ich nach Jacke.", "Gern! Ich hole schnell meine Jacke.", "iść po = holen gehen")],
  "chunks": [("w twojej okolicy", "in deiner Gegend"), ("za rogiem", "um die Ecke"), ("Jadę tramwajem.", "Ich fahre mit der Straßenbahn."), ("Idziemy na spacer?", "Gehen wir spazieren?"), ("Idę po kurtkę.", "Ich hole meine Jacke.")],
  "words": [("okolica", "Gegend"), ("spokojnie", "ruhig"), ("przystanek", "Haltestelle"), ("róg", "Ecke"), ("spacer", "Spaziergang"), ("chętnie", "gern")],
  "qa": [("Ola", "Jak jest w twojej okolicy?", "Wie ist es in deiner Gegend?", "Bardzo spokojnie. Blisko jest park.", "Sehr ruhig. In der Nähe ist ein Park."), ("Ola", "Jak jedziesz do centrum?", "Wie fährst du ins Zentrum?", "Jadę tramwajem.", "Ich fahre mit der Straßenbahn.")],
  "grammar": ("iść und jechać", "iść heißt zu Fuß gehen: idę, idziesz, idzie, idziemy, idziecie, idą. jechać heißt fahren: jadę, jedziesz, jedzie, jedziemy, jedziecie, jadą. Das Fahrzeug steht im Instrumental: jadę tramwajem, autobusem. iść po + Akkusativ heißt etwas holen: idę po chleb, idę po kurtkę."),
  "tips": ["Im Deutschen „gehen“ wir auch mit dem Bus. Im Polnischen nicht: Mit Fahrzeug immer jechać.", "idę ≈ I-de, das ę am Wortende klingt fast wie e."]},
]

ORDER = ["l1", "l2", "b1c", "b1d", "l3", "b2b", "b2c", "b2d", "b3a", "l6", "b3c", "b3d", "b4a", "b4b", "l5", "b4d", "l4", "b5b", "b5c", "b5d"]
BOOK_OLD = {"l1": "1A", "l2": "1B", "l3": "2A", "l6": "3B", "l5": "4C", "l4": "5A"}
UPCOMING_A2 = ["Która godzina?", "Mój poranek", "Godziny pracy", "Plany na weekend", "Tramwajem czy autobusem?", "Na dworcu", "Gdzie byłeś wczoraj?", "Mój urlop",
               "Jaka będzie pogoda?", "Kupuję kurtkę", "Boli mnie głowa", "U specjalisty", "Ogłoszenie o pracę", "Co umiesz?", "Rozmowa kwalifikacyjna", "Pierwszy dzień w pracy",
               "Szkoła w Polsce", "Pierwszy dzień w szkole", "Praca domowa", "Zebranie z rodzicami"]

D = json.load(open("lessons.json", encoding="utf-8"))
by = {l["id"]: l for l in D["lessons"]}
for n in NEW:
    lines = []
    for who, pl, gl, sense, tip in n["lines"]:
        a, b = pl.split(), gl.split()
        assert len(a) == len(b), (n["id"], pl, len(a), len(b))
        ln = {"who": who, "t": [[x, y] for x, y in zip(a, b)], "sense": sense}
        if tip: ln["tip"] = tip
        lines.append(ln)
    by[n["id"]] = {"id": n["id"], "chapter": "pierwsze", "book": n["book"], "title": n["title"], "de": n["de"], "lines": lines,
                   "chunks": [list(c) for c in n["chunks"]], "words": [list(w) for w in n["words"]],
                   "qa": [dict(zip(["who", "q", "qde", "a", "ade"], q)) for q in n["qa"]],
                   "grammar": {"title": n["grammar"][0], "text": n["grammar"][1]}, "tips": n["tips"]}
for k, v in BOOK_OLD.items(): by[k]["book"] = v
assert set(ORDER) == set(by), set(by) ^ set(ORDER)
D["lessons"] = [by[k] for k in ORDER]
for c in D["chapters"]:
    if c["id"] == "pierwsze": c["de"] = "Erste Schritte: vorstellen, Familie, Einkaufen, Essen, Wohnen. Passt zu „Polski na dobry start“, Module 1 bis 5."
    if c["id"] == "rodzina": c["de"] = "Alltag: Zeit, Verkehr, Wetter, Arzt, Arbeit, Schule. Passt zu „Polski na dobry start“, Module 6 bis 10."
D["upcoming"] = {"pierwsze": [], "rodzina": UPCOMING_A2}
D["book"] = {"title": "Polski na dobry start", "level": "A1", "by": "Fundacja Linguae Mundi, 2017",
             "links": [["Lehrbuch (PDF)", "https://www.gov.pl/attachment/1bd0a4d2-94ed-421a-aa87-13b86ba834e6"],
                       ["Übungsheft (PDF)", "https://www.gov.pl/attachment/7cf9eba5-22f4-487a-a3c8-4e2bcc4293e8"],
                       ["Sprachführer Polnisch–Englisch (PDF)", "https://www.gov.pl/attachment/7f391f9c-b55d-4c6e-86b9-e1e3895ccf83"],
                       ["Audios und weitere Materialien (EPALE)", "https://epale.ec.europa.eu/pl/resource-centre/content/materialy-dydaktyczne-do-nauki-jezyka-polskiego-dla-doroslych"]]}
json.dump(D, open("lessons.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(D["lessons"]), "Lektionen")
