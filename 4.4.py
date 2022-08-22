import random
luku = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku: "))
    if luku > arvaus:
        print("Liian pieni arvaus")
    elif luku < arvaus:
        print("Liian suuri arvaus")
    else:
        print("Okein")
        break