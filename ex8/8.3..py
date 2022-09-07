import mysql.connector
from geopy import distance
def koordinaatit(icao: str):
    koord = []
    sql = 'select latitude_deg, longitude_deg from airport'
    sql += ' where iata_code="'+icao+'"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    koord.append(tulos)
    return koord


def hae_etaisyys(koord1, koord2):
    kentta1 = (koord1[0:1])
    kentta2 = (koord2[0:1])
    print(f"The distance between airports is {round(distance.distance(kentta1, kentta2).km,3)} km")
    return

#Main
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='m4*Rv1n42',
    autocommit=True
)
icaos = []
i = 0
while i < 2:
    icao_koodi = input("Give the icao:" )
    icaos.append(icao_koodi)
    i += 1

koords1 = koordinaatit(icaos[0])
koords2 = koordinaatit(icaos[1])
hae_etaisyys(koords1, koords2)
