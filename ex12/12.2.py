import requests
import json

#funktio muuttaa API:sta saadut arvot oikeaan muotoon
def objekti_floatiksi(merkkijono):
    i = 0
    leikattumjono = merkkijono
    asteet = []
    while i < len(leikattumjono):
        if leikattumjono[i].isdigit() or leikattumjono[i] == ".":
            vain_tarpeellinen = leikattumjono[i]
            asteet.append(vain_tarpeellinen)
        i += 1
    mjono = ' '.join(asteet)
    ilmanvaleja = mjono.replace(" ", "")
    tulos = float(ilmanvaleja)
    return tulos

#funktio tuottaa leveysasteen
def leveys_aste(paikkakunta):
    paikka = f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&appid=b0fd0200dc71a71449b2ba70e6853d1a"
    data = requests.get(paikka).json()
    mjono = json.dumps(data)
    indeksi = mjono.find('"lat": ')
    indeksi2 = mjono.find(' "lon": ')
    leikattumjono = mjono[indeksi:indeksi2]
    leveys = objekti_floatiksi(leikattumjono)
    return leveys

#funktio tuottaa pituusasteen
def pituus_aste(paikkakunta):
    paikka = f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&appid=b0fd0200dc71a71449b2ba70e6853d1a"
    data = requests.get(paikka).json()
    mjono = json.dumps(data)
    indeksi = mjono.find('"lon": ')
    indeksi2 = mjono.find(' "contry":')
    leikattumjono = mjono[indeksi:indeksi2]
    pituus = objekti_floatiksi(leikattumjono)
    return pituus
def saa_haku(lat, long):
    säätila = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=b0fd0200dc71a71449b2ba70e6853d1a"
    ilma = requests.get(säätila).json()
    print(json.dumps(ilma, indent=2))

latid = leveys_aste("Helsinki")
print(latid)
longit = pituus_aste("Helsinki")
print(longit)
saa_haku(latid, longit)