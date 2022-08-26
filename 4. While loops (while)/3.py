while True:
    numbers = []
    UserNumbers = float(input("Enter a number: "))
    print("Just press enter to quit.")
    if UserNumbers == "":
        break
    numbers.append(UserNumbers)

print(f"The largest number is {max(numbers)}")
print(f"The smallest number is {min(numbers)}")


