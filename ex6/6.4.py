# a simple function that gives the sum of the list (without using the sum()-function)

def list_sum(list_of_numbers: list):
    sum_of_numbers = 0
    for i in range(len(list_of_numbers)):
        sum_of_numbers += list_of_numbers[i]
    return sum_of_numbers


# the main program tests the function
list_of_numbers_main = [11, 4, 5, 15, 7]
sum_of_list = list_sum(list_of_numbers_main)
print(sum_of_list)