luku = 0
luvut = []
i = 0
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break

    luku = int(luku)
    luvut.append(luku)
for i in range(5):
    luvut.sort(reverse=True)
    print(luvut[i])
