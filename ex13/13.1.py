import json
from flask import Flask, request
# a simple program that uses flask
app = Flask(__name__)


@app.route('/prime_number')
def prime_number():
    args = request.args
    number = int(args.get("number"))
    dividers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_prime = False
    for i in range(7):
        if number in dividers:
            dividers.remove(number)

    for i in range(len(dividers)):
        if number % dividers[i] == 0:
            break
        elif i == len(dividers) - 1:
            if number % number == 0 and number % 1 == 0:
                is_prime = True

    result = {
        "Number": number,
        "isPrime": is_prime,
    }
    json_data = json.dumps(result, default=lambda o: o.__dict__, indent=4)
    return json_data


app.run(use_reloader=True, host='127.0.0.1', port=5000)
