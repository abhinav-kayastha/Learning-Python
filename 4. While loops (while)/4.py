from random import randint

randomInt = randint(1, 10)

while True:
    userGuess = int(input("Try to guess a number between 1 and 10: "))
    if userGuess < randomInt:
        print("Too low.")
    elif userGuess > randomInt:
        print("Too high.")
    else:
        print("Correct")
        break