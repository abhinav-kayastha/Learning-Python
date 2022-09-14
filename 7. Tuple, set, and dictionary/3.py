airports = {}

while True:
    userInput = input("(f)etch, (a)dd new airport, (q)uit: ")
    if userInput == "q":
        break
    elif userInput == "a":
        airportName = input("Enter name of the airport: ")
        airportICAO = input("Enter ICAO code of the airport: ")
        airports[airportICAO] = airportName
    elif userInput == "f":
        airportICAO = input("Enter ICAO code of the airport: ")
        print(f"The name of the airport is {airports[airportICAO]}.")
    else:
        print("Enter a valid command.")


