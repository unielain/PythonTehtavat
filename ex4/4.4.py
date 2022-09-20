# a guessing game where user must guess a number between 1 and 10.
import random
number = random.randint(1, 10)
guess = 0
while guess != number:
    guess = int(input("Guess the number: "))
    if number > guess:
        print(f"The number is larger than {guess}")
    elif number < guess:
        print(f"The number is smaller than {guess}")

print("You won!")
