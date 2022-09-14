import requests
import json
tsoukki = "https://api.chucknorris.io/jokes/random"
vitsi = requests.get(tsoukki).json()
print(vitsi["value"])
