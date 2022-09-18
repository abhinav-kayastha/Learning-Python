import mysql.connector


def getAirportType(iso_country_code):
    sql = 'SELECT name, type FROM airport WHERE iso_country = ' f'"{iso_country_code}"' + ' ORDER BY type;'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for rows in result:
        print(f"Name: {rows[0]}, Type: {rows[1]}")
    return


connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="2012004",
    autocommit=True

)

iso_country_code = input("Enter area code: ")
getAirportType(iso_country_code)
