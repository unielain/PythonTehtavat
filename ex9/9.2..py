class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        if self.nopeus_nyt + nopeuden_muutos >= 0 and self.nopeus_nyt + nopeuden_muutos <= self.huippunopeus:
            self.nopeus_nyt += nopeuden_muutos
        elif self.nopeus_nyt + nopeuden_muutos > self.huippunopeus:
            self.nopeus_nyt = self.huippunopeus
        elif self.nopeus_nyt + nopeuden_muutos < 0:
            self.nopeus_nyt = 0




#Pääohjelma
auto = Auto("ABC-123", 142)
print(f"rekisteritunnus: {auto.rekisteritunnus:s}\nhuippunopeus: {auto.huippunopeus:d}km/h")
print(f"tämänhetkinen nopeus: {auto.nopeus_nyt:d}km/h\nkuljettu matka: {auto.kuljettu_matka:d}km.")
auto.kiihdyta(70)
auto.kiihdyta(30)
auto.kiihdyta(50)
print(f"tämänhetkinen nopeus:{auto.nopeus_nyt:d}km/h")
auto.kiihdyta(-200)
print(f"tämänhetkinen nopeus:{auto.nopeus_nyt:d}km/h")