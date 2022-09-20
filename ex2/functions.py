# functions used in these exercizes

# we prompt the user to choose a unit of their choice and check if it's right.
def a_correct_unit():
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

    return unit