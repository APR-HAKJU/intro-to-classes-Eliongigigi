# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:

- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""

class Buch:
    def __init__(self, titel, autor, seiten, gelesen):
        self.titel= titel
        self.autor= autor
        self.seiter= seiten
        self.gelesen= gelesen
        print("Neues Buch wurde erstellt!")

buch_1= Buch(title = "Harry Potter", autor= "Jk Rowling", seiten=100,gelesen= True)
buch_2=Buch(titel= "Nibellungenlied", autor= "Horst Unteregger", seiten=150, gelesen=False)

print(buch_1.titel)

buch_3 = Buch("Die drei Fragezeichen", "Horst Untereggr", 100, True)



# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.

print(f"{buch_1.titel}wurde gelesen:{buch_1.gelesen}")
print(f"{buch_2.titel}wurde gelesen:{buch_2.gelesen}")
print(f"{buch_3.titel}wurde gelesen:{buch_3.gelesen}")