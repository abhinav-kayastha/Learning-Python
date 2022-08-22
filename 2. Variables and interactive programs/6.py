import random

FirstThreeDigitCode = random.randint(100, 999)
SecondThreeDigitCode = random.randint(100, 999)

while True:
    if SecondThreeDigitCode != FirstThreeDigitCode:
        break
    else:
        SecondThreeDigitCode = random.randint(100, 999)

print(FirstThreeDigitCode)
print(SecondThreeDigitCode)

FirstFourthDigitCode = random.randint(1000, 9999)
SecondFourthDigitCode = random.randint(1000, 9999)

while True:
    if SecondFourthDigitCode != FirstFourthDigitCode:
        break
    else:
        SecondFourthDigitCode = random.randint(1000, 9999)

print(FirstFourthDigitCode)
print(SecondFourthDigitCode)


