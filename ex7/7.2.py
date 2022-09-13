nimet = set(())
while True:
    nimi = input("Anna nimi, tyhjä lopettaa: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    elif nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi")
for sana in nimet:
    print(sana)
