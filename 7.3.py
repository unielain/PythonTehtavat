lentoasemat = {}
while True:
    print(" 'A' Hakee lentoaseman\n 'B' syöttää uuden lentoaseman \n 'C' lopettaa")
    toiminto = input("Mitä haluat tehdä: ")
    if toiminto == "A":
        ICAO = input("Syötä aseman ICAO-koodi: ")
        if ICAO in lentoasemat:
            print(lentoasemat[ICAO])
        else:
            print("Lentoasemaa ei löydy")
    elif toiminto == "B":
        ICAO = input("Syötä aseman ICAO-koodi: ")
        asema = input("Anna lentoaseman nimi: ")
        if ICAO not in lentoasemat:
            lentoasemat[ICAO] = asema
        else:
            print("Asema löytyy jo listalta.")
    elif toiminto == "C":
        break


