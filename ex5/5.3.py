# a simple program that detects if a number given by the user is prime number or not
number = int(input("Anna luku: "))
i = 0
dividers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# we can't use len as a range, since we remove one number
# we eliminate the number given by the user and then can check if the number can be divided by others in the list
for i in range(7):
    if number in dividers:
        dividers.remove(number)

for i in range(len(dividers)):
    if number % dividers[i] == 0:
        print(f"{number} isn't a prime number")
        break
    elif i == len(dividers) - 1:
        if number % number == 0 and number % 1 == 0:
            print(f"{number} is a prime number")

