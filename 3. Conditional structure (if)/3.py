gender = input("Enter your gender (M/F): ")
hemoglobinValue = int(input("Enter your hemoglobin value (g/l): "))

if gender == "F":
    if 117 <= hemoglobinValue >= 155:
        print("Normal hemoglobin.")
    elif hemoglobinValue > 155:
        print("High hemogblin.")
    else:
       print("Low hemoglobin")

if gender == "M":
    if 134 <= hemoglobinValue >= 167:
        print("Normal hemoglobin.")
    elif hemoglobinValue > 167:
        print("High hemoglobin.")
    else:
        print("Low hemoglobin.")