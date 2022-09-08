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
def register(i):
    num = str(i)
    car_reg = "ABC-" + num
    return car_reg
def speed():
    spd = random.randrange(100,200)
    return spd
def arvo_nopeus():
    wroom = random.randrange(-10,15)
    return wroom

#Pääohjelma
cars = []
for i in range(10):
    car = Auto(register(i+1),speed())
    cars.append(car)
voittaja = False
while voittaja != True:
    for car in cars:
        car.kiihdyta(arvo_nopeus())
    for car in cars:
        car.kulje(1)
    for car in cars:
        if car.kuljettu_matka >= 10000:
            voittaja = True
            print(f"Voittaja on {car.rekisteritunnus:s}")
            break
autoi = {}
for car in cars:
    autoi["register"] = car.rekisteritunnus
    autoi["top speed"] = car.huippunopeus
    autoi["driven km"] = car.kuljettu_matka
    print(autoi)
