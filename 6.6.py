import math
def pizzan_neliohinta(halk: float, hinta: float):
    #pizzan pinta-ala: (pii/4)*d^^2
    a = (math.pi/4)*pow(halk,2)
    hinta_ala = hinta/a
    return hinta_ala
koko1 = float(input("Ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Ensimmäisen pizzan hinta: "))
koko2 = float(input("Toisen pizzan halkaisija: "))
hinta2 = float(input("Toisen pizzan hinta: "))
pizza1 = pizzan_neliohinta(koko1, hinta1)
pizza2 = pizzan_neliohinta(koko2, hinta2)
if pizza1 < pizza2:
    print("Ensimmäinen pizza on parempi")
else:
    print("Toinen pizza on parempi")



