# a simple program that asks numbers from user and prints out them in a reverse order
number = 0
numbers = []

while number != "":
    number = input("Anna luku: ")
    if number.isdigit():
        number = int(number)
        numbers.append(number)

for i in range(len(numbers)):
    numbers.sort(reverse=True)
    print(numbers[i])
