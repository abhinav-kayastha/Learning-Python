userInput = int(input("Enter a positive integer: "))
primeChecker = True

if userInput == 1:
    primeChecker = False
else:
    for divisor in range(2, userInput):
        if userInput % divisor == 0:
            primeChecker = False
            break

if primeChecker:
    print(f"{userInput} is a prime number")
else:
    print(f"{userInput} is not a prime number.")











