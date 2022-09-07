import mysql.connector
def haeICAO(icao_koodi):
    sql = 'select name from airport'
    sql += ' WHERE iata_code="'+icao_koodi+'"'
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Antamasi koodi kuuluu {rivi[0]}-lentokentälle")
    else:
        print(f"Koodilla {icao_koodi} ei löytynyt yhtään kenttää")
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

icao_koodi = input("Anna icao:" )
haeICAO(icao_koodi)
