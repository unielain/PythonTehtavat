import random
kuutioita = int(input("Montako arpakuutiota: "))
i = 0
summa = 0
for i in range(kuutioita):
    luku = random.randint(1, 6)
    summa += luku
    i += 1
print(f"summa: {summa}")
