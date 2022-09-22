import mysql.connector
import json
from flask import Flask, request
# a program that returns the airport name and municipality when iata/icao code is used.
# (if cannot find the airport with icao, try iata)
app = Flask(__name__)


@app.route('/airport_data')
def airport_data():
    args = request.args
    arg_icao = str(args.get('arg_icao'))
    name = find_icao(arg_icao)
    municipality = find_the_city(arg_icao)
    municipality = str(municipality)
    municipality = municipality.replace("{", "")
    municipality = municipality.replace("}", "")
    result = {"ICAO": arg_icao,
              "Name": name,
              "Municipality": municipality}
    json_data = json.dumps(result, default=lambda o: o.__dict__, indent=4)
    return json_data


def find_the_city(icao_code):
    connection = connect_to_flight_game()
    sql = 'SELECT municipality FROM airport'
    sql += ' WHERE iata_code="' + icao_code + '"'
    cursor_find_icao = connection.cursor()
    cursor_find_icao.execute(sql)
    result = cursor_find_icao.fetchall()
    municipality_find = ""
    for row in result:
        municipality_find = {row[0]}
    return municipality_find


def find_icao(icao_code):
    connection = connect_to_flight_game()
    sql = 'SELECT name FROM airport'
    sql += ' WHERE iata_code="' + icao_code + '"'
    cursor_find_icao = connection.cursor()
    cursor_find_icao.execute(sql)
    result = cursor_find_icao.fetchall()
    airport = ""
    for row in result:
        airport = row[0]

    return airport


def connect_to_flight_game():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='root',
        password='m4*Rv1n42',
        autocommit=True
    )
    return connection


app.run(use_reloader=True, host='127.0.0.1', port=5000)
