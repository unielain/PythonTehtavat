class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        return f"nimi:{self.nimi}"

class Kirja(Julkaisu):
    def __init__(self, nimi, sivut, kirjoittanut):
        super().__init__(nimi)
        self.sivut = sivut
        self.kirjoittanut = kirjoittanut
        self.kirjat = []
        if nimi not in self.kirjat:
            self.kirjat.append(nimi)

    def tulosta_tiedot(self):
        if self.nimi in self.kirjat:
            nimi = super().tulosta_tiedot()
            return f"nimi:{self.nimi}\n sivut:{self.sivut}\n kirjoittanut:{self.kirjoittanut}"


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
        self.lehdet = []
        if self.lehdet not in self.lehdet:
            self.lehdet.append(nimi)

    def tulosta_tiedot(self):
        if self.nimi in self.lehdet:
            nimi = super().tulosta_tiedot()
            return f" nimi:{self.nimi}\n päätoimittaja:{self.päätoimittaja}\n"
#pääohjelma
ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti = Kirja("Hytti no:6", 200, "Rosa Liksom")
print(ankka.tulosta_tiedot(), hytti.tulosta_tiedot())
