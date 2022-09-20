# a simple program that measures a fish and if it is too small, tells the user to set it free.
fish_lenght = int(input("Give the lenght of the fish: "))
if fish_lenght < 37:
    print(f"The fish is{37 - fish_lenght} cm too small. Let it go.")
else:
    print("The fish is large enough to keep.")
