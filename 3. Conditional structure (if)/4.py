year = int(input("Enter a year (in integer): "))

if year < 1000:
    if year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print("Not a leap year.")
elif year >= 1000:
    if year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print("Not a leap year.")
else:
    print("Enter a valid year.")