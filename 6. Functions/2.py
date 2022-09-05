import random

diceSides = int(input("How many side dice do you want to roll?: "))

def randomRoll(diceSides):
    return random.randint(1, diceSides)


def main(diceSides):
    roll = None
    while roll != diceSides:
        roll = randomRoll(diceSides)
        print(roll)

main(diceSides)