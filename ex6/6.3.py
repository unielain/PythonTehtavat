def gallona_litroiksi(gal: int):
    litra = gal * 3.78541178
    return litra
gallona = 0
while gallona >= 0:
    gallona = int(input("Anna määrä gallonoina: "))
    if gallona < 0:
        break
    gallona = gallona_litroiksi(gallona)
    print(gallona)