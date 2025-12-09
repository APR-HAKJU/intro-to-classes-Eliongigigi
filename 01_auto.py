"""
Übung 1: Auto-Klasse mit Methoden

Aufgabe:
Erstelle eine Klasse `Auto` mit:
- Konstruktor mit Parametern: marke, modell, kilometerstand
- Methode fahren() ohne Parameter: Erhöht den Kilometerstand um 100
  und gibt aus: "Gefahren! Neuer Stand: X km"
- Methode zeige_info() ohne Parameter: Gibt Marke, Modell und 
  Kilometerstand aus

Erstelle ein Auto und lass es dreimal fahren.

💡 Tipp:
- In fahren() verwendest du self.kilometerstand += 100
- Denke daran, dass Methoden immer self als ersten Parameter haben!

Erwartetes Ergebnis:
VW Golf, Kilometerstand: 50000 km
Gefahren! Neuer Stand: 50100 km
Gefahren! Neuer Stand: 50200 km
Gefahren! Neuer Stand: 50300 km
VW Golf, Kilometerstand: 50300 km
"""

# TODO: Erstelle hier die Klasse Auto
class Auto:
    def __init__(self, marke, modell, kilometerstand):
        self.marke = marke
        self.modell= modell
        self.kilometerstand= kilometerstand

    def zeige_info(self):
        print(f"{self.marke} hat Kilometer {self.kilometerstand}")

    def fahren(self):
        self.kilometerstand = self.kilometerstand +100
        print(f"Gefahren! Neuer Stand: {self.kilometerstand} km")

# TODO: Erstelle ein Auto-Objekt (z.B. VW Golf mit 50000 km)
auto_1 =Auto("VW","Golf", 50000)
auto_1.zeige_info

auto_2 = Auto("Audi", "A4", 400000)
auto_2.zeige_info
 
auto_3 = Auto("BMW", "X6MF 96 Competition", 13)
auto_3.zeige_info
# TODO: Zeige die Info


# TODO: Lass das Auto dreimal fahren
auto_1.fahren()
auto_1.fahren()
auto_2.fahren()
auto_3.fahren()

# TODO: Zeige die Info erneut