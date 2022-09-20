luku = 0
luvut = []
while luku != "":
    luku = input("Anna luku: ")
    if luku != "":
        int(luku)
        luvut.append(luku)
print(f"Suurin: {max(luvut)}\nPienin: {min(luvut)}")