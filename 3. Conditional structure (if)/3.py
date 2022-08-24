gender = input("Enter your gender (M/F): ")
hemoglobinValue = int(input("Enter your hemoglobin value (g/l): "))

if gender == "F":
    if 117 <= hemoglobinValue >= 155:
        print("Normal hemoglobin.")
    elif hemoglobinValue > 155:
        print("High hemogblin.")
    else:
        print("Low hemoglobin")