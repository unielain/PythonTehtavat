class Hissi:
    def __init__(self,alin,ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin
    def siirry_kerrokseen(self, kerros):
        if self.nykyinen + kerros >= self.alin and self.nykyinen + kerros <= self.ylin:
            self.nykyinen += kerros
        print(self.nykyinen)
    def kerros_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
        print(self.nykyinen)
    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
        print(self.nykyinen)


class Talo:
    def __init__(self, kerrokset, hissit):
        self.kerrokset = kerrokset
        self.hissit = hissit
        self.hissilista = []
        for i in range(self.hissit):
            hissi = Hissi(0,self.kerrokset)
            self.hissilista.append(hissi)
    def aja_hissiä(self, hissi, kerrokset):
        hissi = self.hissilista[hissi]
        hissi.siirry_kerrokseen(kerrokset)




#pääohjelma
t = Talo(42, 5)
t.aja_hissiä(2, 13)