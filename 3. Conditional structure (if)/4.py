year = int(input("Enter the year: "))

if year <= 999 and year % 4 == 0:
    print(f"{year} is a leap year.")
elif year > 999 and (year % 100 == 0 and year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print("Not a leap year.")