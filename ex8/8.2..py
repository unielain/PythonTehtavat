import mysql.connector
# a simple program that counts how many airports is there in a country submitted by the user


def find_country(country_code_par):
    sql = 'select type, count(*) from airport'
    sql += ' WHERE iso_country="' + country_code_par + '"'
    sql += ' group by type'
    sql += ' order by count(*)'
    cursor_for_func = connection.cursor()
    cursor_for_func.execute(sql)
    result = cursor_for_func.fetchall()
    if cursor_for_func.rowcount > 0:
        for row in result:
            print(f"{country_code_par} has {row[1]} {row[0]}")
    else:
        print(f"Code {country_code_par} didn't find any airports")
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


country_code_main = input("Give the country code: ")
find_country(country_code_main)
