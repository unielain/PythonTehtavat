import random
# a simple program with a function without parameters that tosses a die until the result is six
def roll_the_die():
    roll_result = random.randint(1, 6)
    return roll_result

# the main program prints the numbers
roll_result_main = 0
while roll_result_main != 6:
    roll_result_main = roll_the_die()
    print(roll_result_main)
    if roll_result_main == 6:
        break
