kayttajatunnus = "python"
salasana = "rules"
i = 0
while i < 6:
    kayttaja = input("Anna käyttäjätunnus: ")
    salas = input("Anna salasana: ")
    if i > 4:
        print("Pääsy evätty!")
        break
    elif kayttajatunnus == kayttaja and salas == salasana:
        print("Tervetuloa!")
        break
    else:
        print("Pääsy evätty!")
        #print(f"Yrityksiä jäljellä: {4 - i}")
        i += 1

