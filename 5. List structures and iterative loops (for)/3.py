userInput = int(input("Enter an integer: "))

if userInput == 1:
    print(f"{userInput} is not a prime number.")

for divisor in range(2, 10):
    if divisor == userInput:
        continue
    elif userInput % divisor == 0:
        print(f"{userInput} is not a prime number.")
        break
    else:
        continue










