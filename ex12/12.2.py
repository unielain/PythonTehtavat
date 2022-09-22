import requests
import json


# a program that gets the longitude and latitude of a place and prints the weather as celcius degrees


# a function that converts json object to a float number
def object_to_float(convertable_object):
    i = 0
    cut_string = convertable_object
    list_of_degrees = []
    while i < len(cut_string):
        if cut_string[i].isdigit() or cut_string[i] == ".":
            only_necessary = cut_string[i]
            list_of_degrees.append(only_necessary)
        i += 1
    convertable_string = ' '.join(list_of_degrees)
    spaces_removed = convertable_string.replace(" ", "")
    degrees_in_float = float(spaces_removed)
    return degrees_in_float


# function that fetches the latitude
def get_latitude(get_the_place):
    get_place_info = f"http://api.openweathermap.org/geo/1.0/direct?q={get_the_place}" \
                     f"{secrets.API_KEY}"
    data = requests.get(get_place_info).json()
    get_lat_formatted = json.dumps(data)
    index_of_lat = get_lat_formatted.find('"lat": ')
    lat_ends_index = get_lat_formatted.find(' "lon": ')
    cut_string = get_lat_formatted[index_of_lat:lat_ends_index]
    latitude = object_to_float(cut_string)
    return latitude


# function that fetches the longitude
def get_longitude(get_the_place):
    get_place_info = f"http://api.openweathermap.org/geo/1.0/direct?q={get_the_place}" \
                     f"{secrets.API_KEY}"
    data = requests.get(get_place_info).json()
    get_lon_formatted = json.dumps(data)
    index_of_lon = get_lon_formatted.find('"lon": ')
    lon_ends_index = get_lon_formatted.find(' "contry":')
    cut_string = get_lon_formatted[index_of_lon:lon_ends_index]
    longitude = object_to_float(cut_string)
    return longitude


# function that gets the weather
def get_the_weather(lat, long):
    get_place_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}" \
              f"&appid=b0fd0200dc71a71449b2ba70e6853d1a"
    weather = requests.get(get_place_weather).json()
    degrees = weather["main"]["temp"]
    kelvins_to_celcius = -272.15 / degrees
    return round(kelvins_to_celcius, 2)


# main program to test the function
place = "Helsinki"
latitude_main = get_latitude(place)
longitude_main = get_longitude(place)
celcius_main = get_the_weather(latitude_main, longitude_main)
print(f"It is {celcius_main} C\u00B0 in {place} currently")
