# a program that tells the user which class of cabins they occupy
# LUX: is a cabin with a balcony in the upper deck.
# A: is a cabin with a window above the parking deck.
# B: is a cabin without a window above the parking deck.
# C: is a cabin without a window below the parking deck.

classes_explained = {"LUX": "LUX: is a cabin with a balcony in the upper deck.",
           "A": "A: is a cabin with a window above the parking deck.",
           "B": "B: is a cabin without a window above the parking deck.",
           "C": "C: is a cabin without a window below the parking deck."}

# at first we must check if the user's input is correct
while True:
    cabin_class = input("Please, insert your cabin class (LUX, A, B, C): ")
    cabin_class = cabin_class.upper()
    if cabin_class in classes_explained:
        break
    else:
        print(f"Cabin class {cabin_class} could not be found.\n")

for cabin in classes_explained:
    if cabin == cabin_class:
        print(classes_explained[cabin])