# a simple function that gets a list as a parameter and returns a list without odd numbers


def remove_odd_numbers(list_of_numbers: list):
    only_even_numbers = []
    for element in list_of_numbers:
        if element % 2 == 0:
            only_even_numbers.append(element)
    return only_even_numbers


# main program tests if the function works
list_of_numbers_main = [4, 3, 5, 7, 9, 12, 64, 15]
result = remove_odd_numbers(list_of_numbers_main)
print(f"the original list: {list_of_numbers_main}\n"
      f"the new list: {result}")
