import math
# a simple program that calculates an area of circle using given radius

radius = float(input("Give the radius (meters): "))
area = math.pi * radius ** 2
area = round(area, 2)

#used unicode for superstring to make output look prettier:
print(f"Area is: {area} m\u00B2")