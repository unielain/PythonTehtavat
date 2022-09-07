def listan_summa(luvut: list):
    summa = 0
    for i in range(len(luvut)):
        summa += luvut[i]
    return summa

lista = [11, 4, 5, 15, 7]
tulos = listan_summa(lista)
print(tulos)