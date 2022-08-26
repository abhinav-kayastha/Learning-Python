numbers = []

while True:
    UserNumberStr = input("Enter a number: ")
    if UserNumberStr == "":
        break
    else:
        UserNumberFloat = float(UserNumberStr)
        numbers.append(UserNumberFloat)

print(f"The largest number is {max(numbers)}")
print(f"The smallest number is {min(numbers)}")


