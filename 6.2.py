import random
def dnd_noppa(maksi: int):
    luku = random.randint(1, maksi)
    return luku
noppa = int(input("Montako tahkoa: "))
while True:
    silmaluku = dnd_noppa(noppa)
    print(silmaluku)
    if silmaluku == noppa:
        break