import random
# a simple function that takes as a parameter the faces of a die given by the user and throws the die


def dnd_die(faces: int):
    result_of_roll = random.randint(1, faces)
    return result_of_roll


# main program prints the numbers until the number is equal to number of faces of the die
result_of_roll_main = 0
number_of_faces = 0

while number_of_faces <= 2:
    print("A die must have 3 or more faces")
    number_of_faces = int(input("How many faces: "))


while result_of_roll_main != number_of_faces:
    result_of_roll_main = dnd_die(number_of_faces)
    print(result_of_roll_main)