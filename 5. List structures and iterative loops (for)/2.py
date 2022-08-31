NumbersList = []
FiveGreatestNumbers = []

# The code block below asks the user for a number and then appends it to NumbersList, if the user enters an empty
# string, the program will stop taking numbers from the user, and then stops.

while True:
    UserInput = input("Enter a number: ")
    if UserInput == "":
        break
    else:
        NumbersList.append(float(UserInput))

# The code block below checks the largest number in NumbersList 5 times, and in each iteration it appends the largest
# number to FiveGreatestNumbers and removes that number from NumbersList for the next iteration to find the largest
# number.

for x in range(5):
    LargestNumber = max(NumbersList)
    FiveGreatestNumbers.append(LargestNumber)
    NumbersList.remove(LargestNumber)


FiveGreatestNumbers.sort(reverse=True)

print(FiveGreatestNumbers)
