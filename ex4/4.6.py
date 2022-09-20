import random
import math
maara = int(input("Montako pistettä: "))
i = 0
n = 0
while i < maara + 1:
    x = random.random()
    y = random.random()
    if math.pow(x, 2) + math.pow(y, 2) < 1:
        n += 1
    if i == maara:
        pii = 4 * n / maara
        break
    i += 1
print(pii)