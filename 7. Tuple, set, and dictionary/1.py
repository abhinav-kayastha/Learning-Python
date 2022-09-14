seasons = ("spring", "summer", "autumn", "winter")
userMonth = int(input("Enter a month (1-12): "))

if userMonth == 12 or userMonth == 1 or userMonth == 2:
    print(f"The season at that time is {userMonth[1]}.")
elif userMonth == 3 or userMonth == 4 or userMonth == 5:
    print(f"The season at that time is {userMonth[0]}.")
elif userMonth == 6 or userMonth == 7 or userMonth == 8:
    print(f"The season at that time is {seasons[1]}.")
elif userMonth == 9 or userMonth == 10 or userMonth == 11:
    print(f"The season at that time is {seasons[2]}.")
else:
    print("Enter a valid month.")



