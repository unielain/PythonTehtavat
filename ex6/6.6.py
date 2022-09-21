import math
# a simple function that gets the diameter and price and gives the price of a pizza per a square cm.


def square_price_of_a_pizza(diameter: float, price: float):
    # pizza's area: (pi/4)*d^^2
    area = (math.pi/4)*pow(diameter, 2)
    square_price = price / area
    return square_price


# main program asks for the diameters and prices of two pizzas and tells which is more profitable
diameter_main = 0
price_main = 0
i = 0
square_prices = []

while i < 2:
    diameter_main = float(input("Give the diameter of a pizza: "))
    price_main = float(input("Give the price of a pizza: "))
    # remember to check that the input is somewhat sensible
    if diameter_main < 0 or price_main < 0:
        continue
    square_price_main = square_price_of_a_pizza(diameter_main, price_main)
    square_prices.append(square_price_main)
    i += 1

smaller = 10000

for element in square_prices:
    if element < smaller:
        smaller = element

# add 1 to index, because the list indexes begin from 0
print(f"The best pizza is number {square_prices.index(smaller) + 1}")


