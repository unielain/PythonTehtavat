sukup = input("Oletko mies vai nainen: ")
hmg = int(input("Anna hemoglobiiniarvosi: "))
if sukup == "nainen":
    if hmg > 116 and hmg < 176:
        print("Normaali hemoglobiini")
    elif hmg < 117:
        print("Alhainen hemoglobiini")
    else:
        print("Korkea hemoglobiini")
elif sukup == "mies":
    if hmg > 133 and hmg < 196:
        print("Normaali hemoglobiini")
    elif hmg < 134:
        print("Alhainen hemoglobiini")
    else:
        print("Korkea hemoglobiini")