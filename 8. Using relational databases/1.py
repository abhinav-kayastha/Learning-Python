# NOTE: ICAO code did not exist in my database therefore I had to use GPS code instead.

import mysql.connector


def getAirportNameAndTown(gps_code):
    sql = 'SELECT name, municipality FROM airport WHERE gps_code = ' + f'"{gps_code}"' + ";"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Name: {result[0][0]}, Town: {result[0][1]}")
        return


connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="2012004",
    autocommit=True

)

gps_code_from_user = input("Enter GPS Code: ")
getAirportNameAndTown(gps_code_from_user)
