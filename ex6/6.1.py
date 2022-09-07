import random
def heita_noppaa():
    luku = random.randint(1, 6)
    return luku

silmaluku = 0
while silmaluku != 6:
    silmaluku = heita_noppaa()
    print(silmaluku)
    if silmaluku == 6:
        break
