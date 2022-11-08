import requests
import json



# function that gets the weather
def get_the_weather(country):
    get_place_weather = f"https://api.openweathermap.org/data/2.5/weather?q={country}&appid=e637ea82f6ff2a50f09cf283c917dd77"
    weather = requests.get(get_place_weather).json()
    degrees = weather["main"]["temp"]
    kelvins_to_celcius = -272.15 / degrees
    return round(kelvins_to_celcius, 2)


# main program to test the function
place = "Helsinki"
celcius_main = get_the_weather(place)
print(f"It is {celcius_main} C\u00B0 in {place} currently")

place = "Ankara"
celcius_main = get_the_weather(place)
print(f"It is {celcius_main} C\u00B0 in {place} currently")

