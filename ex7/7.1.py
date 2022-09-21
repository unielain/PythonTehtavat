# a simple program that tells which season month belongs to

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

number_of_month = ""
while number_of_month not in range(13):
    # to ensure that the user gives a sensible number
    number_of_month = int(input("Give the number of the month (1-12): "))

month = months[number_of_month - 1]
if month == "December" or month == "January" or month == "February":
    print(month, "is in winter.")
elif month == "March" or month == "April" or month == "May":
    print(month, "is in spring.")
elif month == "June" or month == "July" or month == "August":
    print(month, "in summer.")
elif month == "September" or month == "October" or month == "November":
    print(month, "is in autumn.")
