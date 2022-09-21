# a program that returns an airport depending on the ICAO code by the user.


airports = {}
while True:
    print(" 'A' Search for an airport\n"
          "'B' Add a new airport\n"
          "'C' Exit")
    action = input("What do you want to do: ")
    if action == "A":
        ICAO = input("Submit the ICAO for the airport: ")
        if ICAO in airports:
            print(airports[ICAO])
        else:
            print("Could not find an airport matching the ICAO.")
    elif action == "B":
        ICAO = input("Submit the ICAO: ")
        airport = input("Submit the airport name: ")
        if ICAO not in airports:
            airports[ICAO] = airport
        else:
            print("Airport is already in the list.")
    elif action == "C":
        break


