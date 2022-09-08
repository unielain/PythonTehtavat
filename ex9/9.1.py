class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0



#Pääohjelma
auto = Auto("ABC-123", 142)
print(f"rekisteritunnus: {auto.rekisteritunnus:s}\nhuippunopeus: {auto.huippunopeus:d}km/h")
print(f"tämänhetkinen nopeus: {auto.nopeus_nyt:d}km/h\nkuljettu matka: {auto.kuljettu_matka:d}km.")
