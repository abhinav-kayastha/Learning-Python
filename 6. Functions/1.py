import random


def randomRoll():
    return random.randint(1, 6)


def main():
    roll = None
    while roll != 6:
        roll = randomRoll()
        print(roll)

main()
