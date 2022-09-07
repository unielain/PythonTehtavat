def parilliset(luvut: list):
    uusi_lista = []
    for alkio in luvut:
        if alkio % 2 == 0:
            uusi_lista.append(alkio)
    return uusi_lista

lista = [4, 3, 5, 7, 9, 12, 64, 15]
tulos = parilliset(lista)
print(f"alkuperäinen lista: {lista}\nuusi lista: {tulos}")
