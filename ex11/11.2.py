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

    def tulosta(self):
        return f"auto: {self.rekisteritunnus} kuljettu matka: {self.kuljettu_matka} km"



class Sähköauto(Auto):
    def __init__(self, akkukapasiteetti, rekisteritunnus, huippunopeus):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, bensatankki, rekisteritunnus, huippunopeus):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

#Pääohjelma
s_auto = Sähköauto(52.5, "ABC-15", 180)
p_auto = Polttomoottoriauto(32.3, "ACD-123", 165)
s_auto.kiihdyta(120)
p_auto.kiihdyta(80)
p_auto.kulje(3)
s_auto.kulje(3)
print(s_auto.tulosta())
print(p_auto.tulosta())