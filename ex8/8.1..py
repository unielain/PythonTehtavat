import mysql.connector
# a simple program that searches an aiport from database matching to ICAO-code submitted by the user.


def find_icao(icao_code):
    sql = 'select name from airport'
    sql += ' WHERE iata_code="' + icao_code + '"'
    cursor_find_icao = connection.cursor()
    cursor_find_icao.execute(sql)
    result = cursor_find_icao.fetchall()
    airport = ""

    if cursor_find_icao.rowcount > 0:
        for row in result:
            airport = f"The ICAO belongs to {row[0]}"
    else:
        airport = f"Could not find any airport with {icao_code}"
    return airport


# Connection to database
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='m4*Rv1n42',
    autocommit=True
)

# Main
icao_code_main = input("Anna icao: ")
find_icao(icao_code_main)
