import functions

# this little program calculates the area and the perimeter of a rectangle

unit = functions.a_correct_unit()
base = float(input("Please, give the base of the rectangle: "))
height = float(input("Please, give the height of the rectangle: "))

area = base * height
area = round(area, 2)
perimeter = base * 2 + height * 2
perimeter = round(perimeter, 2)
print(f"The area is: {area} {unit}\u00B2\n"
      f"The perimeter is: {perimeter}{unit}")
