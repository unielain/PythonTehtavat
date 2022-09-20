# the classic one! A program that checks if the year in question is a leap year:

year = int(input("What year is it: "))
if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} isn't a leap year")