import random
# a program that asks the amount of dice and gives the sum of rolls
amount_of_dice = int(input("Amount of dice: "))
i = 0
sum_of_rolls = 0

for i in range(amount_of_dice):
    toss = random.randint(1, 6)
    sum_of_rolls += toss
    i += 1

print(f"sum: {sum_of_rolls}")
