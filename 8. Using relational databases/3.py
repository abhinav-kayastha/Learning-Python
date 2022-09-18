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


def coordinates_1():
    for x in getAirportCoordinates(gps_code_one)[0]:
        float(x)
    return


def coordinates_2():
    for x in getAirportCoordinates(gps_code_two)[0]:
        float(x)
    return

#distance = print(f"The distance between {gps_code_one} and {gps_code_two} is x km.")
