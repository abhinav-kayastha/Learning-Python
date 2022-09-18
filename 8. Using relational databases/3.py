# NOTE: ICAO code did not exist in my database therefore I had to use GPS code instead.

import mysql.connector
from geopy import distance


def getAirportCoordinates(gps_code):
    sql = 'SELECT latitude_deg, longitude_deg FROM airport WHERE gps_code = ' + f'"{gps_code}"' + ";"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="2012004",
    autocommit=True

)

gps_code_one = input("Enter GPS Code of 1st Airport: ")
gps_code_two = input("Enter GPS Code of 2nd Airport: ")

coordinates_1 = []
coordinates_2 = []

for x in getAirportCoordinates(gps_code_one)[0]:
    coordinates_1.append(float(x))

for x in getAirportCoordinates(gps_code_two)[0]:
    coordinates_2.append(float(x))

coordinates_1 = tuple(coordinates_1)
coordinates_2 = tuple(coordinates_2)

print(f"The distance between {gps_code_one} and {gps_code_two} is {distance.distance(coordinates_1, coordinates_2)}.")
