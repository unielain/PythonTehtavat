import mysql.connector
from geopy import distance
# a simple program that searches the distances of two different airports


# finds airport cordinates from database
def cordinates(icao: str):
    airport_cordinates = []
    sql = 'select latitude_deg, longitude_deg from airport'
    sql += ' where iata_code="'+icao+'"'
    cursor_for_func = connection.cursor()
    cursor_for_func.execute(sql)
    result = cursor_for_func.fetchall()
    airport_cordinates.append(result)
    return airport_cordinates


def find_distance(cord1, cord2):
    airport1 = (cord1[0:1])
    airport2 = (cord2[0:1])
    print(f"The distance between airports is {round(distance.distance(airport1, airport2).km,3)} km")
    return


# connection to database
connection = mysql.connector.connect(
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
    icao_code_main = input("Give the icao:")
    icaos.append(icao_code_main)
    i += 1

cords1_main = cordinates(icaos[0])
cords2_main = cordinates(icaos[1])
find_distance(cords1_main, cords2_main)
