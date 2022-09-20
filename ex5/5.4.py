# a simple program that asks 4 city names from the user and prints them in order they were given
i = 0
cities = []

for i in range(5):
    city = input("Give the name of a city: ")
    cities.append(city)

for city in cities:
    print(city)