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

#pääohjelma

h = Hissi(0, 42)

h.siirry_kerrokseen(28)
for i in range(h.nykyinen):
    h.kerros_alas()