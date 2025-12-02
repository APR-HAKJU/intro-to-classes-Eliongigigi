"""
Übung 2: Kaffeemaschine mit Parametern

Aufgabe:
Erstelle eine Klasse `Kaffeemaschine` mit:
- Konstruktor mit Parameter: wasserstand (in ml, z.B. 1000)
- Methode kaffee_machen(menge) mit Parameter:
  - Prüft, ob genug Wasser da ist
  - Wenn ja: Reduziert Wasserstand und gibt aus "☕ Kaffee gemacht! X ml"
  - Wenn nein: Gibt aus "❌ Nicht genug Wasser! Bitte nachfüllen."
- Methode wasser_nachfuellen(menge) mit Parameter: Erhöht den Wasserstand
- Methode zeige_status() ohne Parameter: Zeigt aktuellen Wasserstand

Erstelle eine Kaffeemaschine mit 500ml Wasser, mache 2x Kaffee (je 200ml),
versuche es nochmal (es sollte dieses Mal fehlschlagen), fülle Wasser nach und mache nochmal Kaffee.

💡 Tipps:
- Verwende if self.wasserstand >= menge: um zu prüfen
- self.wasserstand -= menge verringert den Wasserstand
- self.wasserstand += menge erhöht den Wasserstand

Erwartetes Ergebnis:
Wasserstand: 500 ml
☕ Kaffee gemacht! 200 ml
☕ Kaffee gemacht! 200 ml
❌ Nicht genug Wasser! Bitte nachfüllen.
💧 500 ml Wasser nachgefüllt
☕ Kaffee gemacht! 200 ml
Wasserstand: 400 ml
"""

# TODO: Erstelle hier die Klasse Kaffeemaschine
class Kaffeemaschine:
    def __init__(self, wasserstand):
        self.wasserstand = wasserstand
        print("Neue Kaffeemaschine wurde erstellt!")
    def kaffe_machen(self,menge):
        if menge > self.wasserstand:
            print("Nicht genug Wasser!")
        else:
            print("Kaffe wird gemacht! :)")
            self.wasserstand = self.wasserstand - menge
            print(f"Neuer Wasser: {self.wasserstand}")

    def zeige_info(self):
        print(f"Aktueller Wasserstand: {self.wasserstand}ml")
    def wasser_nachfüllen(self, menge):
        self.wasserstand += menge
# TODO: Erstelle eine Kaffeemaschine mit 500ml Wasser
kaffe_maschine_1 = Kaffeemaschine(wasserstand=500)

# TODO: Zeige den Status
kaffe_maschine_1.zeige_info()


# TODO: Mache 2x Kaffee mit je 200ml
kaffe_maschine_1.kaffe_machen(200)
kaffe_maschine_1.kaffe_machen(200)

# TODO: Versuche nochmal Kaffee zu machen (sollte fehlschlagen)
kaffe_maschine_1.kaffe_machen(200)

# TODO: Fülle 500ml Wasser nach
kaffe_maschine_1.wasser_nachfüllen(500)
kaffe_maschine_1.kaffe_machen(200)
kaffe_maschine_1.kaffe_machen(50)
kaffe_maschine_1.kaffe_machen(1000)

kaffe_maschine_2 = Kaffeemaschine(1000)


# TODO: Mache nochmal Kaffee mit 200ml
kaffe_maschine_1.kaffe_machen(200)

# TODO: Zeige den Status erneut
kaffe_maschine_1.zeige_info()