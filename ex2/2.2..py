import math

# a simple program that calculates an area of circle using given radius
# first we ask which unit would user like to use, and we make sure that it comes out properly:
while True:
    unit = input("Please, choose which unit you like to use (mm, cm, m): ")
    unit = unit.lower()
    acceptable_units = ['m', 'mm', 'cm']

# we check if user has used correct units (upper, or lower case doesn't matter, since we converted it already)
    if unit in acceptable_units:
        break
    else:
        print("\n"
              "Error, unit not found."
              "\nMake sure there are no spaces in your unit"
              "\n")

radius = float(input("Give the radius: "))
area = math.pi * radius ** 2
area = round(area, 2)

# used unicode for superstring to make output look prettier:
print(f"Area is: {area} {unit}\u00B2")