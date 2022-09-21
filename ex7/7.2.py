# a simple program that asks names from user and adds them to a set.


names = set(())
name = "Lovelace"
while name != "":
    name = input("Give a name, exit with enter: ")
    if name in names:
        print("You have already entered this name.")
    elif name not in names:
        names.add(name)
        print("A new name")
for element in names:
    print(element)
