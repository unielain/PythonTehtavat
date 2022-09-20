# a simple program that converts inches to centimeters until the user input is negative
inch = 0
while inch > -1:
    inch = int(input("Inches: "))
    cm = 2.54 * inch
    if cm > -1:
        print(cm)
