# a simple program that tells if the user has a correct, too low, or too high hmg.
# note that this is a programming exercise and cannot be used for treating, or diagnosing illnesses consult your doctor.
# there are only two genders available in this program since the ex. didn't provide more usable data.

genders_hmgs = {"male": {
                "min": 133,
                "max": 196
                },
                "female": {
                "min": 116,
                "max": 176
                }
                }
# we now check if user has input a correct gender
while True:
    gender = input("Are you a male or a female: ")
    gender = gender.lower()
    if gender in genders_hmgs:
        break
    else:
        print(f"data for {gender} could not be found")

hmg = int(input("What is your hmg: "))

# now we can check the hmg for either of gender using the same code.
for type in genders_hmgs:
    if type == gender:
        if genders_hmgs[gender]["min"] < hmg < genders_hmgs[gender]["max"]:
            print("Your hemoglobine is normal level")
        elif hmg > genders_hmgs[gender]["max"]:
            print("Your hemoglobine is high.")
        else:
            print("Your hemoglobine is low.")
