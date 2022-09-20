import math
import functions

# a simple program that calculates an area of circle using given radius
# first we ask which unit would user like to use, and we make sure that it comes out properly:
unit = functions.a_correct_unit()
radius = float(input("Give the radius: "))
area = math.pi * radius ** 2
area = round(area, 2)

# used unicode for superstring to make output look prettier:
print(f"Area is: {area} {unit}\u00B2")