from random import randint

DicesToRoll = int(input("How many times to roll a dice?: "))
NumbersRolled = []

for x in range(DicesToRoll):
    DiceNumber = randint(1, 6)
    NumbersRolled.append(DiceNumber)

print(f"Sum of the rolls: {sum(NumbersRolled)}")