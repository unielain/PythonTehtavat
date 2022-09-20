# a program that asks numbers from the user, and when input is empty it prints the max and min value of the numer
number = 0
numbers = []
while number != "":
    number = input("Anna luku: ")
    if number != "":
        int(number)
        numbers.append(number)
print(f"Suurin: {max(numbers)}\nPienin: {min(numbers)}")