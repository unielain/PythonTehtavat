import requests
# a simple program to get data from API


source_of_joke = "https://api.chucknorris.io/jokes/random"
joke = requests.get(source_of_joke).json()
try:
    print(joke["value"])
except:
    print("Oops! Something went wrong.")
