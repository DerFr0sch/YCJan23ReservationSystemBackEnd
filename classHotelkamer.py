class Hotelkamer:
    def __init__(self, kamertype, kamernummer, prijs, beschrijving, foto):
        self.kamertype = kamertype
        self.kamernummer = kamernummer
        self.prijs = prijs
        self.beschrijving = beschrijving
        self.foto = foto

k1 = Hotelkamer("1 persoonskamer", "101", 150.00, "Een mooie kamer.", "foto.jpg")

print(k1)
