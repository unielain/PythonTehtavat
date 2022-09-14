import random
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

    def kulje(self, tunnit):
        matka = tunnit * self.nopeus_nyt
        self.kuljettu_matka += int(matka)


class Kilpailu():
    def __init__(self, nimi, km, a_rekkari, a_nopeus):
        self.nimi = nimi
        self.km = km
        self.osallistujat = []
        self.reku = a_rekkari
        self.nopea = a_nopeus
        for i in range(len(a_rekkari)):
            auto = Auto(a_rekkari[i], a_nopeus[i])
            self.osallistujat.append(auto)


    def tunti_kuluu(self):
        for auto in self.osallistujat:
            wroom = random.randrange(-10, 15)
            auto.kiihdyta(wroom)
            auto.kulje(1)

    def tulosta_tilanne(self):
        tilanne = {}
        for auto in self.osallistujat:
            tilanne["register"] = auto.rekisteritunnus
            tilanne["top speed"] = auto.huippunopeus
            tilanne["driven km"] = auto.kuljettu_matka
            print(tilanne)

    def kilpailu_ohi(self):
        ohi = False
        for auto in self.osallistujat:
            if auto.kuljettu_matka >= self.km:
                ohi = True
                return ohi
#Pääohjelma
#luo autolle rekisteri
def rekisteri(i):
    num = str(i)
    car_reg = "ABC-" + num
    return car_reg
#auton huippunopeus
def speed():
    spd = random.randrange(100, 200)
    return spd


rekkari = []
nopeus = []
for i in range(1, 11):
    rekkari_muuttuja = rekisteri(i)
    rekkari.append(rekkari_muuttuja)
    nopeus_muuttuja = speed()
    nopeus.append(nopeus_muuttuja)

suuri_romuralli = Kilpailu("suuri romuralli", 8000, rekkari, nopeus)
kilpailu = suuri_romuralli.kilpailu_ohi()
i = 0
while kilpailu != True:
    if kilpailu == True:
        break;
    suuri_romuralli.tunti_kuluu()
    i += 1
    if i == 10:
        suuri_romuralli.tulosta_tilanne()
    kilpailu = suuri_romuralli.kilpailu_ohi()
suuri_romuralli.tulosta_tilanne()