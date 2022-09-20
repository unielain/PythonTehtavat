import random
import math
# the program will calculate the pi from the points given by the user
amount = int(input("Amount of points (bigger amounts give more specific answer): "))
i = 0
n = 0
while i <= amount:
    x = random.random()
    y = random.random()
    if math.pow(x, 2) + math.pow(y, 2) < 1:
        n += 1
    i += 1

pii = 4 * n / amount
print(pii)
