from random import randint

ThreeDigitCode = ""

for x in range(3):
    ThreeDigitCode = ThreeDigitCode + str(randint(0,9))

print(ThreeDigitCode)

FourDigitCode = ""

for y in range(4):
    FourDigitCode = FourDigitCode + str(randint(1,6))

print(FourDigitCode)


