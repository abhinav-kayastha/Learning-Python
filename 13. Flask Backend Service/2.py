import  mysql.connector
from flask import Flask, request

app = Flask(__name__)

@app.route('/icao')
def icao():
    args = request.args
    icao_code = args.get('icao_code')
    sql = 'SELECT name, municipality FROM airport WHERE gps_code = ' + f'"{icao_code}"' + ';'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    name = result[0][0]
    town = result[0][1]

    response = {
        'ICAO': icao_code,
        'Name': name,
        'Location': town
    }

    return response



connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="2012004",
    autocommit=True

)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)