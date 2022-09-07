import mysql.connector
def hae_maa(maakoodi):
    sql = 'select type, count(*) from airport'
    sql += ' WHERE iso_country="'+maakoodi+'"'
    sql += ' group by type'
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f" {maakoodi} has {rivi[1]} {rivi[0]}")
    else:
        print(f"Code {maakoodi} didn't find any airports")
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

maakoodi = input("Anna maakoodi:" )
hae_maa(maakoodi)
