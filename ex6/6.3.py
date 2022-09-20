# a simple function that converts gallons to litres


def gallon_to_litres(gal: int):
    litre = gal * 3.78541178
    return litre


# main asks for gallons until the user gives a negative number
gallon = 0
while gallon >= 0:
    gallon = gallon_to_litres(gallon)
    print(gallon)
    gallon = int(input("How many gallons: "))
