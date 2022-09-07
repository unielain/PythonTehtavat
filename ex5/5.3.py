luku = int(input("Anna luku: "))
i = 0
luvut = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for i in range(11):
    if luku in luvut:
        luvut.remove(luku)
for i in range(len(luvut)):
    if luku % luvut[i] == 0:
        print(f"{luku} ei ole alkuluku")
        break
    elif i == len(luvut) - 1:
        if luku % luku == 0 and luku % 1 == 0:
            print(f"{luku} on alkuluku")

