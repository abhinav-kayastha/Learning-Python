while True:
    UserInchNum = float(input("Enter length in inches: "))
    if UserInchNum < 0:
        break
    InCentimeters = UserInchNum * 2.54
    print(f"The length in centimeters is {InCentimeters}.")
